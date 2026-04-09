"""LLM-powered contribution generator.

Takes findings from the analysis engine and generates
actual code changes, tests, and commit messages that
follow the target repository's coding conventions.
"""

from __future__ import annotations

import difflib
import json
import logging
import re
from datetime import UTC, datetime

from contribai.core.config import ContributionConfig
from contribai.core.models import (
    Contribution,
    ContributionType,
    FileChange,
    Finding,
    RepoContext,
)
from contribai.llm.context import build_repo_context_prompt
from contribai.llm.provider import LLMProvider

logger = logging.getLogger(__name__)


class ContributionGenerator:
    """Generate code contributions from analysis findings."""

    def __init__(self, llm: LLMProvider, config: ContributionConfig, *, memory=None):
        self._llm = llm
        self._config = config
        self._memory = memory  # Optional Memory for repo_preferences

    async def generate(
        self,
        finding: Finding,
        context: RepoContext,
        *,
        guidelines=None,
    ) -> Contribution | None:
        """Generate a contribution for a single finding.

        Steps:
        1. Build context-aware prompt
        2. Get LLM to generate the fix
        3. Parse structured output into FileChanges
        4. Generate commit message
        5. Self-review the generated code
        """
        try:
            # 1 & 2: Generate the fix (with retry on failure)
            repo_prefs = await self._get_repo_preferences(context)
            prompt = self._build_generation_prompt(finding, context, repo_prefs=repo_prefs)
            system = self._build_system_prompt(context)

            changes = None
            last_error = ""
            for attempt in range(2):  # max 1 retry
                if attempt > 0:
                    logger.info(
                        "Retrying generation (attempt %d) for: %s", attempt + 1, finding.title
                    )
                    retry_hint = (
                        f"\n\n## IMPORTANT: Your previous attempt failed.\n"
                        f"Error: {last_error}\n"
                        f"Please fix the issue and return ONLY valid JSON "
                        f"with no markdown fences or extra text.\n"
                    )
                    prompt_with_hint = prompt + retry_hint
                else:
                    prompt_with_hint = prompt

                response = await self._llm.complete(
                    prompt_with_hint, system=system, temperature=0.2
                )

                # 3: Parse output → apply search/replace to original content
                changes = self._parse_changes(response, context)
                if not changes:
                    last_error = "No valid changes could be parsed from your JSON output"
                    continue

                # 3b: Validate generated code (syntax sanity check)
                if not self._validate_changes(changes):
                    last_error = (
                        "Generated code failed syntax validation"
                        " (unbalanced brackets or empty edits)"
                    )
                    changes = None
                    continue

                break  # Success

            if not changes:
                logger.warning("No valid changes after retries for finding: %s", finding.title)
                return None

            # 4: Generate commit message
            commit_msg = await self._generate_commit_message(finding, changes, context)

            # 5: Generate branch name
            branch_name = self._generate_branch_name(finding)

            # Build the contribution
            contribution = Contribution(
                finding=finding,
                contribution_type=finding.type,
                title=self._generate_pr_title(finding, guidelines=guidelines),
                description=finding.description,
                changes=changes,
                commit_message=commit_msg,
                branch_name=branch_name,
                generated_at=datetime.now(UTC),
            )

            # 6: Self-review
            review_passed = await self._self_review(contribution, context)
            if not review_passed:
                logger.warning("Self-review failed for: %s", finding.title)
                return None

            logger.info(
                "Generated contribution: %s (%d files changed)",
                contribution.title,
                contribution.total_files_changed,
            )
            return contribution

        except Exception as e:
            logger.error("Failed to generate contribution for %s: %s", finding.title, e)
            return None

    async def _get_repo_preferences(self, context: RepoContext) -> dict | None:
        """Query memory for learned repo preferences.

        Returns dict with preferred_types, rejected_types, merge_rate
        or None if no memory or no data for this repo.
        """
        if not self._memory:
            return None
        try:
            return await self._memory.get_repo_preferences(context.repo.full_name)
        except Exception as e:
            logger.debug("Could not fetch repo preferences: %s", e)
            return None

    def _build_system_prompt(self, context: RepoContext) -> str:
        """Build system prompt with repository context and style awareness."""
        repo_context = build_repo_context_prompt(context, max_tokens=4000)

        # Inject style guide if available
        style_section = ""
        if context.coding_style:
            style_section = (
                "\n\nCODEBASE STYLE (learned from this repository):\n"
                f"{context.coding_style}\n\n"
                "You MUST match these conventions exactly. Do not introduce "
                "your own style preferences. Your changes should look like "
                "they were written by the same developer who wrote the rest "
                "of the codebase.\n"
            )

        return (
            "You are a senior open-source contributor who writes production-ready "
            "code. You understand that PRs are judged by maintainers who value "
            "minimal, focused, and convention-matching changes.\n\n"
            "RULES FOR GENERATING CHANGES:\n"
            "1. Match existing code style EXACTLY (indentation, naming, patterns)\n"
            "2. Make the SMALLEST change that correctly fixes the issue\n"
            "3. Include proper error handling consistent with the codebase\n"
            "4. Do NOT break existing functionality\n"
            "5. Do NOT add unnecessary dependencies or imports\n"
            "6. Do NOT refactor adjacent code — fix only the reported issue\n"
            "7. Do NOT add comments explaining what the code does (self-documenting)\n"
            "8. Do NOT modify files unrelated to the finding\n\n"
            "OUTPUT FORMAT RULES (CRITICAL):\n"
            "- Return ONLY raw JSON — no markdown fences, no ```json blocks\n"
            "- No explanatory text before or after the JSON\n"
            "- The response must be valid, parseable JSON and nothing else\n"
            "- Do NOT wrap your response in code blocks of any kind\n\n"
            "MAINTAINER ACCEPTANCE CRITERIA:\n"
            "- Would a busy maintainer merge this in under 30 seconds?\n"
            "- Is the change obviously correct with no side effects?\n"
            "- Does it follow the project's established patterns?\n"
            "- Is it genuinely useful (not busywork or cosmetic)?\n"
            f"{style_section}\n"
            f"REPOSITORY CONTEXT:\n{repo_context}"
        )

    def _build_generation_prompt(
        self, finding: Finding, context: RepoContext, *, repo_prefs: dict | None = None
    ) -> str:
        """Build the generation prompt based on finding type."""
        # Get the current file content if available
        current_content = context.relevant_files.get(finding.file_path, "")

        type_instructions = {
            ContributionType.SECURITY_FIX: (
                "Fix this SECURITY vulnerability. Ensure the fix is complete "
                "and doesn't introduce new vulnerabilities."
            ),
            ContributionType.CODE_QUALITY: (
                "Improve the CODE QUALITY. Make the code cleaner, more maintainable, "
                "and more robust. Keep changes minimal and focused."
            ),
            ContributionType.DOCS_IMPROVE: (
                "Improve the DOCUMENTATION. Add missing docstrings, improve README sections, "
                "or fix documentation issues. Be thorough but concise."
            ),
            ContributionType.UI_UX_FIX: (
                "Fix this UI/UX issue. Improve accessibility, user experience, or visual design. "
                "Follow WCAG guidelines where applicable."
            ),
            ContributionType.PERFORMANCE_OPT: (
                "Optimize PERFORMANCE. Reduce time/space complexity, "
                "eliminate wasteful operations, or improve resource usage."
            ),
            ContributionType.FEATURE_ADD: (
                "Add this FEATURE. Keep the implementation clean, well-structured, and consistent "
                "with the existing codebase patterns."
            ),
            ContributionType.REFACTOR: (
                "REFACTOR this code. Improve structure and readability without changing behavior."
            ),
        }

        instruction = type_instructions.get(finding.type, "Fix this issue.")

        prompt = (
            f"## Task\n{instruction}\n\n"
            f"## Finding\n"
            f"- **Title**: {finding.title}\n"
            f"- **Severity**: {finding.severity.value}\n"
            f"- **File**: {finding.file_path}\n"
            f"- **Description**: {finding.description}\n"
        )

        # Inject repo preferences from outcome learning
        if repo_prefs:
            prefs_section = "\n## Repo Preferences (learned from past PRs)\n"
            if repo_prefs.get("rejected_types"):
                prefs_section += (
                    f"- **Avoid these PR types** (historically rejected): "
                    f"{', '.join(repo_prefs['rejected_types'])}\n"
                )
            if repo_prefs.get("preferred_types"):
                prefs_section += (
                    f"- **Preferred PR types** (historically merged): "
                    f"{', '.join(repo_prefs['preferred_types'])}\n"
                )
            if repo_prefs.get("merge_rate") is not None:
                rate = repo_prefs["merge_rate"]
                prefs_section += f"- **Merge rate**: {rate:.0%}\n"
            prompt += prefs_section

        if finding.suggestion:
            prompt += f"- **Suggestion**: {finding.suggestion}\n"

        if current_content:
            prompt += (
                f"\n## Current File Content ({finding.file_path})\n"
                f"```\n{current_content[:6000]}\n```\n"
            )

        # Cross-file: find other files with the same pattern
        other_affected_files = self._find_cross_file_instances(finding, context)
        if other_affected_files:
            prompt += (
                f"\n## ⚠️ IMPORTANT: Same issue in "
                f"{len(other_affected_files)} OTHER file(s)\n"
                "Fix ALL instances across ALL files in a single contribution.\n"
                "This produces a higher-quality PR that addresses the issue comprehensively.\n\n"
            )
            for fpath, fcontent in other_affected_files.items():
                prompt += f"### {fpath}\n```\n{fcontent[:3000]}\n```\n\n"

        prompt += "\n## Output Format\nReturn your changes as a JSON object.\n\n"

        if current_content:
            # For EXISTING files: use search/replace blocks to preserve content
            prompt += (
                "Since this is an EXISTING file, use SEARCH/REPLACE blocks "
                "to make targeted edits. DO NOT rewrite the entire file.\n\n"
                "```json\n"
                "{\n"
                '  "changes": [\n'
                "    {\n"
                '      "path": "path/to/file",\n'
                '      "is_new_file": false,\n'
                '      "edits": [\n'
                "        {\n"
                '          "search": "exact text to find in the file",\n'
                '          "replace": "replacement text"\n'
                "        }\n"
                "      ]\n"
                "    }\n"
                "  ]\n"
                "}\n"
                "```\n\n"
                "RULES for search/replace:\n"
                "- `search` must be an EXACT substring from the current file\n"
                "- `replace` is what replaces it (can be longer/shorter)\n"
                "- To ADD new content, search for the text BEFORE the insertion "
                "point and include it + the new content in `replace`\n"
                "- To DELETE content, set `replace` to empty string\n"
                "- Keep each edit small and focused\n"
                "- DO NOT include the entire file in search or replace\n"
            )
        else:
            # For NEW files: provide full content
            prompt += (
                "Since this is a NEW file, provide the full content:\n\n"
                "```json\n"
                "{\n"
                '  "changes": [\n'
                "    {\n"
                '      "path": "path/to/file",\n'
                '      "content": "full content of the new file",\n'
                '      "is_new_file": true\n'
                "    }\n"
                "  ]\n"
                "}\n"
                "```\n"
            )

        return prompt

    def _validate_changes(self, changes: list) -> bool:
        """Validate generated code changes for basic syntax sanity.

        Quick checks before expensive self-review:
        - Non-empty new_content
        - No-op detection (original == new)
        - Balanced brackets for common languages (string/comment-aware)

        Returns True if changes pass validation.

        Note: `changes` is a list of FileChange objects (not raw dicts).
        At this point, edits have already been applied — we only see
        the final new_content.
        """
        if not changes:
            return False

        for change in changes:
            # Check new file content is non-trivial
            if change.is_new_file:
                content = change.new_content.strip()
                if len(content) < 10:
                    logger.debug(
                        "Validation: new file content too short (%d chars)",
                        len(content),
                    )
                    return False

            # Check that content actually changed
            if change.original_content and change.new_content == change.original_content:
                logger.debug("Validation: new_content identical to original (no-op)")
                return False

            # Balanced bracket check — skip brackets inside strings and comments
            code_text = change.new_content
            if code_text:
                unbalanced = self._count_unbalanced_brackets(code_text)
                if unbalanced > 5:
                    logger.debug("Validation: %d unbalanced brackets", unbalanced)
                    return False

        return True

    @staticmethod
    def _count_unbalanced_brackets(code: str) -> int:
        """Count unbalanced brackets, ignoring those inside strings and comments."""
        pairs = {"(": ")", "[": "]", "{": "}"}
        closers = set(pairs.values())
        stack: list[str] = []
        in_string: str | None = None  # tracks quote character
        in_line_comment = False
        prev_ch = ""

        for ch in code:
            # Handle newlines — reset line comment
            if ch == "\n":
                in_line_comment = False
                prev_ch = ch
                continue

            # Skip chars inside line comments
            if in_line_comment:
                prev_ch = ch
                continue

            # Detect line comment start (# for Python, // for others)
            if ch == "#" and not in_string:
                in_line_comment = True
                prev_ch = ch
                continue
            if ch == "/" and prev_ch == "/" and not in_string:
                in_line_comment = True
                prev_ch = ch
                continue

            # Handle string boundaries
            if ch in ('"', "'") and prev_ch != "\\":
                if in_string is None:
                    in_string = ch
                elif in_string == ch:
                    in_string = None
                prev_ch = ch
                continue

            # Skip chars inside strings
            if in_string:
                prev_ch = ch
                continue

            # Count brackets
            if ch in pairs:
                stack.append(pairs[ch])
            elif ch in closers and stack and stack[-1] == ch:
                stack.pop()

            prev_ch = ch

        return len(stack)

    def _find_cross_file_instances(self, finding: Finding, context: RepoContext) -> dict[str, str]:
        """Find other files in the repo with the same issue pattern.

        Searches relevant_files for code patterns similar to the primary
        finding's issue (e.g., same non-null assertion, same unsafe pattern).
        Returns {path: content} for files that likely have the same issue.
        """
        if not finding.file_path or not context.relevant_files:
            return {}

        # Extract key terms from the finding to search for
        keywords = self._extract_search_patterns(finding)
        if not keywords:
            return {}

        other_files: dict[str, str] = {}
        for fpath, content in context.relevant_files.items():
            if fpath == finding.file_path:
                continue
            # Check if any keyword pattern appears in this file
            content_lower = content.lower()
            matches = sum(1 for kw in keywords if kw.lower() in content_lower)
            if matches >= 2:  # At least 2 pattern matches = likely same issue
                other_files[fpath] = content
                if len(other_files) >= 3:  # Cap at 3 extra files to limit prompt size
                    break

        if other_files:
            logger.info(
                "🔗 Found same pattern in %d other file(s): %s",
                len(other_files),
                ", ".join(other_files.keys()),
            )
        return other_files

    @staticmethod
    def _extract_search_patterns(finding: Finding) -> list[str]:
        """Extract code patterns from finding description to search across files.

        Looks for code-like tokens in the finding's description and suggestion.
        """
        patterns = []
        text = f"{finding.description} {finding.suggestion or ''}"
        # Extract backtick-quoted code snippets
        import re

        for match in re.findall(r"`([^`]+)`", text):
            if len(match) > 3:  # Skip very short matches
                patterns.append(match)
        # Extract common code patterns mentioned
        for pattern in re.findall(r"(\w+\.\w+[!?]?(?:\(\))?)", text):
            if len(pattern) > 5:
                patterns.append(pattern)
        return patterns[:10]  # Cap at 10 patterns

    def _parse_changes(self, response: str, context: RepoContext) -> list[FileChange]:
        """Parse LLM response into FileChange objects.

        Supports two formats:
        1. Search/replace blocks (for existing files) — applies edits to original
        2. Full content (for new files) — uses content as-is
        """
        changes: list[FileChange] = []

        try:
            # Robust JSON extraction with multiple strategies
            json_text = self._extract_json(response)
            if not json_text:
                return []

            data = json.loads(json_text)
            raw_changes = data.get("changes", [])

            for item in raw_changes:
                if not isinstance(item, dict) or "path" not in item:
                    continue

                path = item["path"]
                is_new = item.get("is_new_file", False)

                if "edits" in item and not is_new:
                    # Search/replace mode — apply edits to original content
                    original = context.relevant_files.get(path, "")
                    if not original:
                        logger.warning(
                            "No original content for %s (finding file not fetched), skipping edits",
                            path,
                        )
                        continue

                    new_content = original
                    edits_applied = 0
                    edits_total = len(item["edits"])
                    for edit in item["edits"]:
                        search = edit.get("search", "")
                        replace = edit.get("replace", "")
                        if not search:
                            continue

                        matched = False

                        # Try 1: Exact match
                        if search in new_content:
                            new_content = new_content.replace(search, replace, 1)
                            matched = True

                        # Try 2: Normalize trailing whitespace per line
                        if not matched:
                            norm_search = "\n".join(line.rstrip() for line in search.split("\n"))
                            norm_content = "\n".join(
                                line.rstrip() for line in new_content.split("\n")
                            )
                            if norm_search in norm_content:
                                # Find position in normalized, apply to original
                                idx = norm_content.index(norm_search)
                                # Map back: count newlines to find line range
                                start_line = norm_content[:idx].count("\n")
                                end_line = start_line + norm_search.count("\n")
                                lines = new_content.split("\n")
                                lines[start_line : end_line + 1] = replace.split("\n")
                                new_content = "\n".join(lines)
                                matched = True
                                logger.debug(
                                    "Fuzzy match (whitespace normalized) for %s",
                                    path,
                                )

                        # Try 3: Strip all leading/trailing whitespace
                        if not matched:
                            stripped_search = search.strip()
                            if len(stripped_search) > 20 and stripped_search in new_content:
                                new_content = new_content.replace(
                                    stripped_search, replace.strip(), 1
                                )
                                matched = True
                                logger.debug(
                                    "Fuzzy match (stripped) for %s",
                                    path,
                                )

                        # Try 4: difflib fuzzy match (ratio > 0.8)
                        if not matched and len(search) > 20:
                            matched = self._fuzzy_replace(new_content, search, replace)
                            if matched:
                                new_content = matched
                                logger.debug("Fuzzy match (difflib) for %s", path)

                        if matched:
                            edits_applied += 1
                        else:
                            logger.warning(
                                "Search text not found in %s (tried exact + 3 fuzzy). "
                                "Search[:%d]: %.80s...",
                                path,
                                len(search),
                                search.replace("\n", "\\n"),
                            )

                    logger.info(
                        "Edits for %s: %d/%d applied",
                        path,
                        edits_applied,
                        edits_total,
                    )

                    if edits_applied == 0:
                        logger.warning("No edits applied to %s, skipping file", path)
                        continue

                    changes.append(
                        FileChange(
                            path=path,
                            new_content=new_content,
                            is_new_file=False,
                        )
                    )

                elif "content" in item:
                    # Full content mode (new files or fallback)
                    changes.append(
                        FileChange(
                            path=path,
                            new_content=item["content"],
                            is_new_file=is_new,
                        )
                    )

        except (json.JSONDecodeError, KeyError, TypeError) as e:
            logger.warning("Failed to parse changes JSON: %s", e)

        # Enforce max files limit
        if len(changes) > self._config.max_files_per_pr:
            logger.warning(
                "Too many files changed (%d > %d), truncating",
                len(changes),
                self._config.max_files_per_pr,
            )
            changes = changes[: self._config.max_files_per_pr]

        return changes

    async def _generate_commit_message(
        self, finding: Finding, changes: list[FileChange], context: RepoContext
    ) -> str:
        """Generate a conventional commit message."""
        type_prefixes = {
            ContributionType.SECURITY_FIX: "fix(security)",
            ContributionType.CODE_QUALITY: "refactor",
            ContributionType.DOCS_IMPROVE: "docs",
            ContributionType.UI_UX_FIX: "fix(ui)",
            ContributionType.PERFORMANCE_OPT: "perf",
            ContributionType.FEATURE_ADD: "feat",
            ContributionType.REFACTOR: "refactor",
        }

        prefix = type_prefixes.get(finding.type, "fix")
        files = ", ".join(c.path.split("/")[-1] for c in changes[:3])

        if self._config.commit_convention == "conventional":
            # Try to extract scope from file path
            scope = ""
            if changes:
                parts = changes[0].path.split("/")
                if (len(parts) >= 2 and parts[0] in ("packages", "apps", "libs")) or (
                    len(parts) >= 2 and parts[0] == "src"
                ):
                    scope = parts[1]
            if scope:
                return (
                    f"{prefix}({scope}): {finding.title.lower()}\n\n"
                    f"{finding.description}\n\n"
                    f"Affected files: {files}"
                )
            return (
                f"{prefix}: {finding.title.lower()}\n\n"
                f"{finding.description}\n\n"
                f"Affected files: {files}"
            )
        elif self._config.commit_convention == "angular":
            scope = changes[0].path.split("/")[0] if changes else ""
            return f"{prefix}({scope}): {finding.title.lower()}"
        else:
            return finding.title

    def _generate_branch_name(self, finding: Finding) -> str:
        """Generate a clean branch name from finding."""
        prefix_map = {
            ContributionType.SECURITY_FIX: "fix/security",
            ContributionType.CODE_QUALITY: "improve/quality",
            ContributionType.DOCS_IMPROVE: "docs",
            ContributionType.UI_UX_FIX: "fix/ui",
            ContributionType.PERFORMANCE_OPT: "perf",
            ContributionType.FEATURE_ADD: "feat",
            ContributionType.REFACTOR: "refactor",
        }
        prefix = prefix_map.get(finding.type, "fix")
        # Clean title for branch name
        slug = re.sub(r"[^a-zA-Z0-9]+", "-", finding.title.lower()).strip("-")[:40]
        return f"contribai/{prefix}/{slug}"

    def _generate_pr_title(self, finding: Finding, *, guidelines=None) -> str:
        """Generate a PR title adapted to repo conventions."""
        # Use adaptive title if guidelines available
        if guidelines and guidelines.has_guidelines:
            from contribai.github.guidelines import (
                adapt_pr_title,
                extract_scope_from_path,
            )

            scope = extract_scope_from_path(finding.file_path or "", guidelines)
            return adapt_pr_title(
                finding.title,
                finding.type.value,
                guidelines,
                scope=scope,
            )

        # Default: clean text format (no emoji in PR title)
        type_labels = {
            ContributionType.SECURITY_FIX: "Security",
            ContributionType.CODE_QUALITY: "Quality",
            ContributionType.DOCS_IMPROVE: "Docs",
            ContributionType.UI_UX_FIX: "UI/UX",
            ContributionType.PERFORMANCE_OPT: "Performance",
            ContributionType.FEATURE_ADD: "Feature",
            ContributionType.REFACTOR: "Refactor",
        }
        label = type_labels.get(finding.type, "Fix")
        return f"{label}: {finding.title}"

    async def _self_review(self, contribution: Contribution, context: RepoContext) -> bool:
        """Have the LLM self-review the generated contribution."""
        changes_summary = "\n".join(
            f"- {c.path} ({'new' if c.is_new_file else 'modified'})" for c in contribution.changes
        )

        prompt = (
            "Review the following code contribution for quality:\n\n"
            f"**Title**: {contribution.title}\n"
            f"**Type**: {contribution.contribution_type.value}\n"
            f"**Finding**: {contribution.finding.description}\n"
            f"**Changes**:\n{changes_summary}\n\n"
            "For each changed file:\n"
        )
        for change in contribution.changes[:5]:
            # Show diff-style context: include original vs new for better judgement
            original = context.relevant_files.get(change.path, "")
            if original and not change.is_new_file:
                # Show unified diff instead of full content
                diff_lines = list(
                    difflib.unified_diff(
                        original.splitlines(keepends=True)[:100],
                        change.new_content.splitlines(keepends=True)[:100],
                        fromfile=f"a/{change.path}",
                        tofile=f"b/{change.path}",
                        n=3,
                    )
                )
                diff_text = "".join(diff_lines)[:4000]
                prompt += f"\n### {change.path} (diff)\n```diff\n{diff_text}\n```\n"
            else:
                prompt += f"\n### {change.path}\n```\n{change.new_content[:4000]}\n```\n"

        prompt += (
            "\nAnswer these questions:\n"
            "1. Does the change address the described issue?\n"
            "2. Does it introduce any obvious new bugs or security vulnerabilities?\n"
            "3. Is the change reasonable and follows existing code style?\n\n"
            "IMPORTANT: Be lenient. APPROVE if the change is a net improvement, "
            "even if minor improvements could be made. Only REJECT if the change "
            "is clearly wrong, introduces a bug, or is completely unrelated to the issue.\n\n"
            "Reply with APPROVE or REJECT followed by brief reasoning."
        )

        try:
            response = await self._llm.complete(prompt, temperature=0.1)
            approved = "APPROVE" in response.upper()
            if not approved:
                logger.info("Self-review rejected: %s", response[:200])
            return approved
        except Exception as e:
            logger.warning("Self-review failed, approving by default: %s", e)
            return True  # Don't block on review failures

    @staticmethod
    def _extract_json(response: str) -> str | None:
        """Robustly extract JSON from LLM response.

        Tries multiple strategies to handle common LLM quirks:
        1. Extract from ```json fences
        2. Find raw JSON with "changes" key
        3. Strip trailing text after valid JSON
        """
        # Strategy 1: ```json blocks
        json_match = re.search(r"```json\s*\n(.*?)\n\s*```", response, re.DOTALL)
        if json_match:
            return json_match.group(1).strip()

        # Strategy 2: ``` blocks (no language tag)
        json_match = re.search(r"```\s*\n(\{.*?\})\n\s*```", response, re.DOTALL)
        if json_match:
            return json_match.group(1).strip()

        # Strategy 3: Find raw JSON object with "changes" key
        # Use a bracket-counting approach to find the complete JSON
        start = response.find('{"changes"')
        if start == -1:
            start = response.find("{\n")
        if start == -1:
            return None

        depth = 0
        end = start
        for i in range(start, len(response)):
            if response[i] == "{":
                depth += 1
            elif response[i] == "}":
                depth -= 1
                if depth == 0:
                    end = i + 1
                    break

        if depth == 0 and end > start:
            return response[start:end]

        return None

    @staticmethod
    def _fuzzy_replace(content: str, search: str, replace: str) -> str | None:
        """Find the closest matching block in content using difflib.

        Returns the modified content if a match with ratio > 0.8 is found,
        otherwise returns None.
        """
        search_lines = search.splitlines()
        content_lines = content.splitlines()
        search_len = len(search_lines)

        if search_len == 0 or search_len > len(content_lines):
            return None

        best_ratio = 0.0
        best_start = -1

        # Slide a window over content lines
        for i in range(len(content_lines) - search_len + 1):
            window = content_lines[i : i + search_len]
            ratio = difflib.SequenceMatcher(
                None, "\n".join(search_lines), "\n".join(window)
            ).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_start = i

        if best_ratio >= 0.8 and best_start >= 0:
            result_lines = (
                content_lines[:best_start]
                + replace.splitlines()
                + content_lines[best_start + search_len :]
            )
            return "\n".join(result_lines)

        return None
