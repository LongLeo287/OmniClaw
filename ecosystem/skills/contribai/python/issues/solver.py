"""Issue-driven contribution engine.

Reads open GitHub issues, classifies them, and generates
targeted contributions that solve specific issues.

v2.0.0: Deep multi-file solving with codebase understanding.
"""

from __future__ import annotations

import logging
import re
from enum import StrEnum

from contribai.core.models import (
    ContributionType,
    Finding,
    Issue,
    RepoContext,
    Repository,
    Severity,
)

logger = logging.getLogger(__name__)


class IssueCategory(StrEnum):
    """Classification categories for GitHub issues."""

    BUG = "bug"
    FEATURE = "feature"
    DOCS = "docs"
    SECURITY = "security"
    PERFORMANCE = "performance"
    UI_UX = "ui_ux"
    GOOD_FIRST_ISSUE = "good_first_issue"
    UNSOLVABLE = "unsolvable"


# Labels that map to categories
LABEL_MAP: dict[str, IssueCategory] = {
    "bug": IssueCategory.BUG,
    "fix": IssueCategory.BUG,
    "defect": IssueCategory.BUG,
    "feature": IssueCategory.FEATURE,
    "enhancement": IssueCategory.FEATURE,
    "feature-request": IssueCategory.FEATURE,
    "documentation": IssueCategory.DOCS,
    "docs": IssueCategory.DOCS,
    "security": IssueCategory.SECURITY,
    "vulnerability": IssueCategory.SECURITY,
    "performance": IssueCategory.PERFORMANCE,
    "ui": IssueCategory.UI_UX,
    "ux": IssueCategory.UI_UX,
    "accessibility": IssueCategory.UI_UX,
    "good first issue": IssueCategory.GOOD_FIRST_ISSUE,
    "good-first-issue": IssueCategory.GOOD_FIRST_ISSUE,
    "beginner": IssueCategory.GOOD_FIRST_ISSUE,
    "help wanted": IssueCategory.GOOD_FIRST_ISSUE,
}

CATEGORY_TO_CONTRIB = {
    IssueCategory.BUG: ContributionType.CODE_QUALITY,
    IssueCategory.FEATURE: ContributionType.FEATURE_ADD,
    IssueCategory.DOCS: ContributionType.DOCS_IMPROVE,
    IssueCategory.SECURITY: ContributionType.SECURITY_FIX,
    IssueCategory.PERFORMANCE: ContributionType.PERFORMANCE_OPT,
    IssueCategory.UI_UX: ContributionType.UI_UX_FIX,
    IssueCategory.GOOD_FIRST_ISSUE: ContributionType.CODE_QUALITY,
}

# Labels that indicate an issue is good for automated solving
SOLVABLE_LABELS = {
    "good first issue",
    "good-first-issue",
    "help wanted",
    "help-wanted",
    "beginner",
    "easy",
    "low-hanging-fruit",
    "bug",
    "documentation",
    "docs",
    "enhancement",
    "feature",
}


class IssueSolver:
    """Analyzes and solves GitHub issues using LLM."""

    def __init__(self, llm, github):
        self._llm = llm
        self._github = github

    # ── Issue Discovery ────────────────────────────────────────────────────

    async def fetch_solvable_issues(
        self,
        repo: Repository,
        *,
        max_issues: int = 5,
        max_complexity: int = 3,
    ) -> list[Issue]:
        """Fetch open issues from a repo that are good candidates for solving.

        Filters:
        - Unassigned only (nobody is working on it)
        - Has solvable labels (good first issue, help wanted, bug, etc.)
        - No linked PRs (not already being addressed)
        - Complexity <= max_complexity
        """
        all_issues: list[Issue] = []

        # Try fetching with preferred labels first
        for label_group in [
            ["good first issue"],
            ["help wanted"],
            ["bug"],
            ["enhancement"],
            ["documentation"],
        ]:
            try:
                raw_issues = await self._github.list_issues(
                    repo.owner,
                    repo.name,
                    labels=label_group,
                    assignee="none",
                    per_page=10,
                )
                for raw in raw_issues:
                    issue = Issue(
                        number=raw["number"],
                        title=raw["title"],
                        body=raw.get("body"),
                        labels=[
                            lbl["name"] for lbl in raw.get("labels", []) if isinstance(lbl, dict)
                        ],
                        state=raw.get("state", "open"),
                        html_url=raw.get("html_url", ""),
                    )
                    # Deduplicate by number
                    if not any(i.number == issue.number for i in all_issues):
                        all_issues.append(issue)
            except Exception as e:
                logger.debug("Failed to fetch issues with labels %s: %s", label_group, e)

        if not all_issues:
            # Fallback: fetch any open issues
            try:
                raw_issues = await self._github.list_issues(
                    repo.owner,
                    repo.name,
                    assignee="none",
                    per_page=20,
                )
                for raw in raw_issues:
                    issue = Issue(
                        number=raw["number"],
                        title=raw["title"],
                        body=raw.get("body"),
                        labels=[
                            lbl["name"] for lbl in raw.get("labels", []) if isinstance(lbl, dict)
                        ],
                        state=raw.get("state", "open"),
                        html_url=raw.get("html_url", ""),
                    )
                    if not any(i.number == issue.number for i in all_issues):
                        all_issues.append(issue)
            except Exception as e:
                logger.debug("Failed to fetch fallback issues: %s", e)

        # Filter: skip issues with linked PRs
        filtered = []
        for issue in all_issues:
            if await self._has_linked_pr(repo, issue):
                logger.debug(
                    "Skipping issue #%d (has linked PR): %s",
                    issue.number,
                    issue.title,
                )
                continue
            filtered.append(issue)

        # Filter by complexity and solvability
        solvable = self.filter_solvable(filtered, max_complexity=max_complexity)

        logger.info(
            "📋 Found %d solvable issues in %s (from %d total)",
            len(solvable),
            repo.full_name,
            len(all_issues),
        )

        return solvable[:max_issues]

    async def _has_linked_pr(self, repo: Repository, issue: Issue) -> bool:
        """Check if an issue already has a linked pull request."""
        try:
            events = await self._github.get_issue_timeline(repo.owner, repo.name, issue.number)
            for event in events:
                if event.get("event") == "cross-referenced":
                    source = event.get("source", {})
                    if source.get("type") == "issue":
                        issue_data = source.get("issue", {})
                        if issue_data.get("pull_request"):
                            return True
            return False
        except Exception:
            return False

    # ── Classification ─────────────────────────────────────────────────────

    def classify_issue(self, issue: Issue) -> IssueCategory:
        """Classify an issue based on labels and title keywords.

        Args:
            issue: GitHub issue to classify.

        Returns:
            IssueCategory enum value.
        """
        # Check labels first (most reliable)
        for label in issue.labels:
            label_lower = label.lower().strip()
            if label_lower in LABEL_MAP:
                return LABEL_MAP[label_lower]

        # Fall back to keyword matching on title
        title_lower = issue.title.lower()
        keyword_map = {
            IssueCategory.BUG: [
                "bug",
                "fix",
                "error",
                "crash",
                "broken",
                "fail",
                "issue",
            ],
            IssueCategory.FEATURE: [
                "add",
                "feature",
                "implement",
                "support",
                "new",
            ],
            IssueCategory.DOCS: [
                "doc",
                "readme",
                "typo",
                "documentation",
                "example",
            ],
            IssueCategory.SECURITY: [
                "security",
                "vulnerability",
                "cve",
                "xss",
                "injection",
            ],
            IssueCategory.PERFORMANCE: [
                "slow",
                "performance",
                "optimize",
                "speed",
                "memory",
            ],
            IssueCategory.UI_UX: [
                "ui",
                "ux",
                "responsive",
                "accessibility",
                "design",
            ],
        }

        for category, keywords in keyword_map.items():
            if any(kw in title_lower for kw in keywords):
                return category

        return IssueCategory.BUG  # Default to bug

    def _estimate_complexity(self, issue: Issue) -> int:
        """Estimate issue complexity (1-5). Lower is easier.

        Args:
            issue: GitHub issue to assess.

        Returns:
            Complexity score from 1 (trivial) to 5 (very complex).
        """
        score = 2  # baseline

        # Good first issues are simple
        if any("first" in label.lower() or "beginner" in label.lower() for label in issue.labels):
            return 1

        # Body length hints at complexity
        body_len = len(issue.body or "")
        if body_len > 2000:
            score += 1
        if body_len > 5000:
            score += 1

        # Multiple file references = complex
        if issue.body:
            file_refs = re.findall(r"[\w/]+\.\w{1,4}", issue.body)
            if len(file_refs) > 3:
                score += 1

        return min(score, 5)

    def filter_solvable(self, issues: list[Issue], max_complexity: int = 3) -> list[Issue]:
        """Filter issues to only those the agent can likely solve.

        Args:
            issues: List of GitHub issues.
            max_complexity: Maximum complexity score to attempt.

        Returns:
            Filtered list of solvable issues.
        """
        solvable = []
        for issue in issues:
            category = self.classify_issue(issue)
            if category == IssueCategory.UNSOLVABLE:
                continue

            complexity = self._estimate_complexity(issue)
            if complexity > max_complexity:
                continue

            solvable.append(issue)

        return solvable

    # ── Issue Solving ──────────────────────────────────────────────────────

    async def solve_issue(
        self,
        issue: Issue,
        repo: Repository,
        context: RepoContext,
    ) -> Finding | None:
        """Convert a GitHub issue into a Finding for the generator.

        Uses LLM to understand the issue and identify the relevant
        files and changes needed.

        Args:
            issue: GitHub issue to solve.
            repo: Repository containing the issue.
            context: Repository context for LLM prompting.

        Returns:
            Finding object that can be fed to the ContributionGenerator.
        """
        category = self.classify_issue(issue)
        contrib_type = CATEGORY_TO_CONTRIB.get(category, ContributionType.CODE_QUALITY)

        # Build context prompt
        file_tree_str = "\n".join(f"  {f.path}" for f in context.file_tree[:50] if f.type == "blob")

        relevant_code = ""
        for path, content in list(context.relevant_files.items())[:3]:
            relevant_code += f"\n### {path}\n```\n{content[:2000]}\n```\n"

        prompt = f"""Analyze this GitHub issue and determine:
1. Which file(s) need changes
2. What changes are needed
3. The severity of the issue

## Repository: {repo.full_name} ({repo.language})

## Issue #{issue.number}: {issue.title}
{issue.body or "No description provided."}

## Labels: {", ".join(issue.labels) if issue.labels else "none"}

## File Tree:
{file_tree_str}

{relevant_code}

Respond in this exact format:
FILE_PATH: <main file to change>
SEVERITY: <low|medium|high|critical>
TITLE: <short descriptive title>
DESCRIPTION: <what needs to be changed and why>
SUGGESTION: <specific implementation suggestion>
"""

        try:
            response = await self._llm.complete(
                prompt,
                system="You are a senior developer analyzing GitHub issues. "
                "Identify the root cause and suggest a specific fix.",
            )

            # Parse structured response
            lines = response.strip().split("\n")
            parsed = {}
            for line in lines:
                if ":" in line:
                    key, _, value = line.partition(":")
                    parsed[key.strip().upper()] = value.strip()

            file_path = parsed.get("FILE_PATH", "unknown")
            severity_str = parsed.get("SEVERITY", "medium").lower()
            severity_map = {
                "low": Severity.LOW,
                "medium": Severity.MEDIUM,
                "high": Severity.HIGH,
                "critical": Severity.CRITICAL,
            }

            return Finding(
                id=f"issue-{issue.number}",
                type=contrib_type,
                severity=severity_map.get(severity_str, Severity.MEDIUM),
                title=parsed.get("TITLE", issue.title),
                description=parsed.get("DESCRIPTION", issue.body or issue.title),
                file_path=file_path,
                suggestion=parsed.get("SUGGESTION"),
                confidence=0.85,
            )

        except Exception as e:
            logger.error("Failed to analyze issue #%d: %s", issue.number, e)
            return None

    async def solve_issue_deep(
        self,
        issue: Issue,
        repo: Repository,
        context: RepoContext,
    ) -> list[Finding]:
        """Deep multi-file issue solving with codebase understanding.

        Unlike solve_issue() which returns a single Finding,
        this method understands the full codebase and returns
        multiple Findings for multi-file changes.

        Phases:
        1. Read issue + comments to understand requirements
        2. Identify relevant files and dependencies
        3. Plan multi-file solution
        4. Return list of Findings (one per file to modify)

        Args:
            issue: GitHub issue to solve.
            repo: Repository containing the issue.
            context: Repository context with file tree and code.

        Returns:
            List of Finding objects for multi-file changes.
        """
        category = self.classify_issue(issue)
        contrib_type = CATEGORY_TO_CONTRIB.get(category, ContributionType.CODE_QUALITY)

        # Phase 1: Read issue body + comments
        issue_context = await self._build_issue_context(issue, repo)

        # Phase 2: Build codebase map
        file_tree_str = self._build_file_tree_summary(context)

        # Build relevant code context (up to 10 files)
        relevant_code = ""
        for path, content in list(context.relevant_files.items())[:10]:
            relevant_code += f"\n### {path}\n```\n{content[:3000]}\n```\n"

        # Phase 3: Ask LLM to plan multi-file solution
        prompt = f"""You are solving a GitHub issue. Analyze the issue carefully and create
a detailed plan for which file(s) to create or modify.

## Repository: {repo.full_name} ({repo.language})

## Issue #{issue.number}: {issue.title}
{issue_context}

## File Tree:
{file_tree_str}

## Relevant Code:
{relevant_code}

## Instructions:
1. Identify ALL files that need to be created or modified
2. For each file, explain what changes are needed
3. Be specific about the implementation

Respond with one or more blocks in this exact format (one per file):

---FILE---
PATH: <path to file>
ACTION: <modify|create>
SEVERITY: <low|medium|high|critical>
TITLE: <what this change does>
DESCRIPTION: <detailed description of the change>
SUGGESTION: <specific implementation details>
---END---
"""

        try:
            response = await self._llm.complete(
                prompt,
                system=(
                    "You are an expert open-source developer solving GitHub issues. "
                    "You understand codebases deeply and create comprehensive, "
                    "multi-file solutions. Be specific about implementation details. "
                    "Only include files that actually need changes."
                ),
                temperature=0.2,
            )

            # Parse multi-file response
            findings = self._parse_multi_file_response(response, issue, contrib_type)

            if not findings:
                # Fall back to single-file solving
                logger.info("Deep solve returned no findings, falling back to single-file")
                single = await self.solve_issue(issue, repo, context)
                return [single] if single else []

            logger.info(
                "🧠 Deep solve for issue #%d: %d file(s) to change",
                issue.number,
                len(findings),
            )
            return findings

        except Exception as e:
            logger.error("Deep solve failed for issue #%d: %s", issue.number, e)
            # Fall back to single-file solve
            single = await self.solve_issue(issue, repo, context)
            return [single] if single else []

    async def _build_issue_context(self, issue: Issue, repo: Repository) -> str:
        """Build full issue context including comments."""
        parts = [issue.body or "No description provided."]

        try:
            comments = await self._github.get_issue_comments(repo.owner, repo.name, issue.number)
            for comment in comments[:5]:  # Max 5 comments
                author = comment.get("user", {}).get("login", "unknown")
                body = comment.get("body", "")
                if body and len(body) > 10:
                    parts.append(f"\n**Comment by @{author}:**\n{body[:1000]}")
        except Exception:
            pass

        return "\n".join(parts)

    def _build_file_tree_summary(self, context: RepoContext) -> str:
        """Build a compact file tree summary for LLM context."""
        # Group files by directory
        dirs: dict[str, list[str]] = {}
        for f in context.file_tree[:200]:
            if f.type != "blob":
                continue
            parts = f.path.rsplit("/", 1)
            if len(parts) == 2:
                dir_name, file_name = parts
            else:
                dir_name, file_name = ".", parts[0]
            dirs.setdefault(dir_name, []).append(file_name)

        lines = []
        for dir_name in sorted(dirs.keys())[:30]:
            files = dirs[dir_name]
            files_str = ", ".join(files[:8])
            if len(files) > 8:
                files_str += f" (+{len(files) - 8} more)"
            lines.append(f"  {dir_name}/  [{files_str}]")

        return "\n".join(lines)

    def _parse_multi_file_response(
        self,
        response: str,
        issue: Issue,
        default_type: ContributionType,
    ) -> list[Finding]:
        """Parse LLM response with multiple ---FILE--- blocks."""
        findings: list[Finding] = []
        blocks = re.split(r"---FILE---", response)

        severity_map = {
            "low": Severity.LOW,
            "medium": Severity.MEDIUM,
            "high": Severity.HIGH,
            "critical": Severity.CRITICAL,
        }

        for block in blocks:
            block = block.strip()
            if not block or "---END---" not in block:
                continue

            # Remove ---END--- marker
            block = block.split("---END---")[0].strip()

            parsed: dict[str, str] = {}
            for line in block.split("\n"):
                if ":" in line:
                    key, _, value = line.partition(":")
                    key = key.strip().upper()
                    if key in (
                        "PATH",
                        "ACTION",
                        "SEVERITY",
                        "TITLE",
                        "DESCRIPTION",
                        "SUGGESTION",
                    ):
                        parsed[key] = value.strip()

            file_path = parsed.get("PATH")
            if not file_path or file_path == "unknown":
                continue

            severity_str = parsed.get("SEVERITY", "medium").lower()

            findings.append(
                Finding(
                    id=f"issue-{issue.number}-{len(findings)}",
                    type=default_type,
                    severity=severity_map.get(severity_str, Severity.MEDIUM),
                    title=parsed.get("TITLE", issue.title),
                    description=parsed.get("DESCRIPTION", issue.body or issue.title),
                    file_path=file_path,
                    suggestion=parsed.get("SUGGESTION"),
                    confidence=0.80,
                )
            )

        return findings[:5]  # Max 5 files per issue
