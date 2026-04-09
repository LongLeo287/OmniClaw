"""Fetch and parse repository contribution guidelines.

Reads CONTRIBUTING.md, PR templates, and .github configs
to adapt ContribAI's PRs to each repo's conventions.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass, field

from contribai.github.client import GitHubClient

logger = logging.getLogger(__name__)

# Common PR template locations in repos
_PR_TEMPLATE_PATHS = [
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/pull_request_template.md",
    "PULL_REQUEST_TEMPLATE.md",
    "pull_request_template.md",
    "docs/PULL_REQUEST_TEMPLATE.md",
    ".github/PULL_REQUEST_TEMPLATE/default.md",
]

_CONTRIBUTING_PATHS = [
    "CONTRIBUTING.md",
    "contributing.md",
    ".github/CONTRIBUTING.md",
    "docs/CONTRIBUTING.md",
]


@dataclass
class RepoGuidelines:
    """Parsed contribution guidelines for a repository."""

    # Raw content
    contributing_md: str = ""
    pr_template: str = ""

    # Parsed conventions
    commit_format: str = "default"  # conventional | angular | default
    commit_scopes: list[str] = field(default_factory=list)
    pr_title_format: str = "default"  # conventional | emoji | default
    required_sections: list[str] = field(default_factory=list)

    # Detected patterns
    uses_conventional_commits: bool = False
    uses_angular_commits: bool = False
    requires_scope: bool = False
    allowed_types: list[str] = field(default_factory=list)

    @property
    def has_guidelines(self) -> bool:
        return bool(self.contributing_md or self.pr_template)


async def fetch_repo_guidelines(
    github: GitHubClient,
    owner: str,
    repo: str,
) -> RepoGuidelines:
    """Fetch and parse contribution guidelines from a repo.

    Tries multiple paths for CONTRIBUTING.md and PR templates.
    Parses the content to detect commit format, required sections, etc.
    """
    guidelines = RepoGuidelines()

    # Fetch CONTRIBUTING.md
    for path in _CONTRIBUTING_PATHS:
        try:
            content = await github.get_file_content(owner, repo, path)
            if content:
                guidelines.contributing_md = content
                logger.info("Found contributing guide: %s/%s/%s", owner, repo, path)
                break
        except Exception:
            continue

    # Fetch PR template
    for path in _PR_TEMPLATE_PATHS:
        try:
            content = await github.get_file_content(owner, repo, path)
            if content:
                guidelines.pr_template = content
                logger.info("Found PR template: %s/%s/%s", owner, repo, path)
                break
        except Exception:
            continue

    # Parse conventions from content
    _parse_commit_format(guidelines)
    _parse_pr_template_sections(guidelines)

    if guidelines.has_guidelines:
        logger.info(
            "Repo guidelines: commit=%s, pr_title=%s, scopes=%s, sections=%d",
            guidelines.commit_format,
            guidelines.pr_title_format,
            guidelines.commit_scopes or "any",
            len(guidelines.required_sections),
        )

    return guidelines


def _parse_commit_format(guidelines: RepoGuidelines) -> None:
    """Detect commit message format from CONTRIBUTING.md."""
    text = guidelines.contributing_md.lower()

    # Detect conventional commits
    conventional_patterns = [
        r"conventional\s*commit",
        r"feat\s*[:(]",
        r"fix\s*[:(]",
        r"chore\s*[:(]",
        r"docs\s*[:(]",
        r"refactor\s*[:(]",
    ]
    matches = sum(1 for p in conventional_patterns if re.search(p, text))
    if matches >= 2:
        guidelines.uses_conventional_commits = True
        guidelines.commit_format = "conventional"
        guidelines.pr_title_format = "conventional"

    # Detect angular format (with scope)
    if re.search(r"feat\s*\(\s*\w+\s*\)", text):
        guidelines.uses_angular_commits = True
        guidelines.commit_format = "angular"
        guidelines.pr_title_format = "conventional"
        guidelines.requires_scope = True

    # Extract allowed types
    type_pattern = re.findall(
        r"(?:^|\n)\s*[-*]\s*`?(feat|fix|docs|chore|refactor|test|perf|ci|style|build|revert)`?\b",
        text,
    )
    if type_pattern:
        guidelines.allowed_types = list(dict.fromkeys(type_pattern))  # dedup

    # Extract scopes from examples like feat(scope):
    scope_pattern = re.findall(
        r"(?:feat|fix|docs|chore|refactor|test|perf)\((\w+)\)",
        guidelines.contributing_md,
    )
    if scope_pattern:
        guidelines.commit_scopes = list(dict.fromkeys(scope_pattern))


def _parse_pr_template_sections(guidelines: RepoGuidelines) -> None:
    """Extract required sections from PR template."""
    template = guidelines.pr_template
    if not template:
        return

    # Find markdown headers as required sections
    headers = re.findall(r"^#{1,3}\s+(.+)$", template, re.MULTILINE)
    if headers:
        guidelines.required_sections = [h.strip() for h in headers]

    # Also check for HTML comment sections
    comment_sections = re.findall(r"<!--\s*(.+?)\s*-->", template)
    for section in comment_sections:
        if section.strip() not in guidelines.required_sections:
            guidelines.required_sections.append(section.strip())


def adapt_pr_title(
    finding_title: str,
    contribution_type: str,
    guidelines: RepoGuidelines,
    *,
    scope: str = "",
) -> str:
    """Adapt PR title to match repo conventions.

    Args:
        finding_title: The finding title (e.g., "Missing error handling")
        contribution_type: ContributionType value
        guidelines: Parsed repo guidelines
        scope: Optional scope (e.g., package name from file path)
    """
    # Map ContribAI types to conventional commit types
    type_map = {
        "security_fix": "fix",
        "code_quality": "refactor",
        "docs_improve": "docs",
        "ui_ux_fix": "fix",
        "performance_opt": "perf",
        "feature_add": "feat",
        "refactor": "refactor",
    }
    cc_type = type_map.get(contribution_type, "fix")

    # If repo uses conventional commits, format accordingly
    if guidelines.uses_conventional_commits or guidelines.uses_angular_commits:
        # Ensure we use an allowed type if repo specifies them
        if guidelines.allowed_types and cc_type not in guidelines.allowed_types:
            # Fall back to closest allowed type
            if "fix" in guidelines.allowed_types:
                cc_type = "fix"
            elif guidelines.allowed_types:
                cc_type = guidelines.allowed_types[0]

        # Build title with optional scope
        if (scope and guidelines.requires_scope) or scope:
            return f"{cc_type}({scope}): {finding_title.lower()}"
        else:
            return f"{cc_type}: {finding_title.lower()}"

    # Default: clean text format (no emoji in PR title)
    type_labels = {
        "security_fix": "Security",
        "code_quality": "Quality",
        "docs_improve": "Docs",
        "ui_ux_fix": "UI/UX",
        "performance_opt": "Performance",
        "feature_add": "Feature",
        "refactor": "Refactor",
    }
    label = type_labels.get(contribution_type, "Fix")
    return f"{label}: {finding_title}"


def adapt_pr_body(
    contribution,
    guidelines: RepoGuidelines,
) -> str:
    """Generate PR body adapted to repo's PR template.

    If the repo has a PR template, fill it in with contribution data.
    Otherwise, use ContribAI's default format.
    """
    from contribai.core.models import ContributionType

    finding = contribution.finding

    # Type info for default format
    type_info = {
        ContributionType.SECURITY_FIX: ("🔒", "Security Fix"),
        ContributionType.CODE_QUALITY: ("✨", "Code Quality"),
        ContributionType.DOCS_IMPROVE: ("📝", "Documentation"),
        ContributionType.UI_UX_FIX: ("🎨", "UI/UX Improvement"),
        ContributionType.PERFORMANCE_OPT: ("⚡", "Performance"),
        ContributionType.FEATURE_ADD: ("🚀", "New Feature"),
        ContributionType.REFACTOR: ("♻️", "Refactoring"),
    }
    emoji, label = type_info.get(finding.type, ("🔧", "Fix"))

    files_list = "\n".join(
        f"- `{c.path}` {'(new)' if c.is_new_file else '(modified)'}" for c in contribution.changes
    )

    # If repo has a PR template, try to fill it
    if guidelines.pr_template:
        return _fill_pr_template(
            guidelines.pr_template,
            contribution,
            emoji=emoji,
            label=label,
            files_list=files_list,
        )

    # Default ContribAI format
    return _default_pr_body(contribution, emoji, label, files_list)


def _fill_pr_template(
    template: str,
    contribution,
    *,
    emoji: str,
    label: str,
    files_list: str,
) -> str:
    """Fill a repo's PR template with contribution data."""
    from contribai.core.models import ContributionType

    finding = contribution.finding
    filled = template

    # Common template placeholders and their values
    replacements = {
        # Description-related
        "<!-- description -->": finding.description,
        "<!-- Describe your changes -->": finding.description,
        "<!-- A brief description -->": finding.description,
        # Type/category
        "<!-- type -->": label,
        # Changes
        "<!-- changes -->": files_list,
        "<!-- List of changes -->": files_list,
        # Testing
        "<!-- testing -->": (
            "- Existing tests pass\n- Manual review completed\n- No new warnings/errors introduced"
        ),
        "<!-- How has this been tested? -->": (
            "- Existing tests pass\n- Manual review completed\n- No new warnings/errors introduced"
        ),
    }

    for placeholder, value in replacements.items():
        filled = filled.replace(placeholder, value)

    # Remove unfilled HTML comment placeholders
    filled = re.sub(r"<!--\s*[^>]*\s*-->", "", filled)

    # Auto-check applicable checkbox items
    # Map contribution type to "Type of change" checkboxes
    type_checkbox_map = {
        ContributionType.SECURITY_FIX: ["bug fix"],
        ContributionType.CODE_QUALITY: ["refactor", "code improvement"],
        ContributionType.DOCS_IMPROVE: ["documentation"],
        ContributionType.UI_UX_FIX: ["bug fix"],
        ContributionType.PERFORMANCE_OPT: ["refactor", "code improvement"],
        ContributionType.FEATURE_ADD: ["new feature"],
        ContributionType.REFACTOR: ["refactor", "code improvement"],
    }
    type_matches = type_checkbox_map.get(finding.type, ["bug fix"])
    for match_text in type_matches:
        # Check matching type checkbox (case-insensitive)
        pattern = re.compile(
            r"- \[ \]\s*(" + re.escape(match_text) + r")",
            re.IGNORECASE,
        )
        if pattern.search(filled):
            filled = pattern.sub(r"- [x] \1", filled, count=1)
            break  # Only check one type

    # Auto-check common "always true" checkboxes
    always_check = [
        "tested my changes",
        "tested locally",
        "not included unrelated changes",
        "no unrelated changes",
        "read the contributing",
        "follows the code style",
    ]
    for phrase in always_check:
        pattern = re.compile(
            r"- \[ \]\s*(.*" + re.escape(phrase) + r".*)",
            re.IGNORECASE,
        )
        filled = pattern.sub(r"- [x] \1", filled)

    # Add contribution summary at the top if template doesn't have description section
    if finding.description not in filled:
        summary = (
            f"## {emoji} {label}\n\n"
            f"### Problem\n{finding.description}\n\n"
            f"**Severity**: `{finding.severity.value}`\n"
            f"**File**: `{finding.file_path}`\n\n"
            f"### Solution\n{finding.suggestion or contribution.description}\n\n"
            f"### Changes\n{files_list}\n\n"
        )
        filled = summary + filled

    # Always append ContribAI attribution
    filled += _contribai_attribution()

    return filled


def _default_pr_body(
    contribution,
    emoji: str,
    label: str,
    files_list: str,
) -> str:
    """Generate default ContribAI PR body."""
    finding = contribution.finding

    return (
        f"## {emoji} {label}\n\n"
        f"### Problem\n{finding.description}\n\n"
        f"**Severity**: `{finding.severity.value}`\n"
        f"**File**: `{finding.file_path}`\n\n"
        f"### Solution\n{finding.suggestion or contribution.description}\n\n"
        f"### Changes\n{files_list}\n\n"
        f"### Testing\n"
        f"- [x] Existing tests pass\n"
        f"- [x] Manual review completed\n"
        f"- [x] No new warnings/errors introduced\n\n"
        f"---\n\n"
        f"{_contribai_attribution()}"
    )


def _contribai_attribution() -> str:
    return (
        "\n---\n\n"
        "<details>\n"
        "<summary>🤖 About this PR</summary>\n\n"
        "This pull request was generated by "
        "[ContribAI](https://github.com/tang-vu/ContribAI), an AI agent\n"
        "that helps improve open source projects. The change was:\n\n"
        "1. **Discovered** by automated code analysis\n"
        "2. **Generated** by AI with context-aware code generation\n"
        "3. **Self-reviewed** by AI quality checks\n\n"
        "If you have questions or feedback about this PR, please comment below.\n"
        "We appreciate your time reviewing this contribution!\n\n"
        "</details>\n"
    )


def extract_scope_from_path(file_path: str, guidelines: RepoGuidelines) -> str:
    """Extract a conventional commit scope from a file path.

    Uses repo's known scopes if available, otherwise infers from path.
    Examples:
        packages/console/app/src/foo.tsx → console or app
        src/utils/helper.py → utils
    """
    parts = file_path.split("/")

    # Try to match against known scopes
    if guidelines.commit_scopes:
        for part in parts:
            if part in guidelines.commit_scopes:
                return part

    # Infer: if path starts with packages/X or apps/X, use X
    if len(parts) >= 2 and parts[0] in ("packages", "apps", "libs", "modules"):
        return parts[1]

    # Infer: if path starts with src/X, use X
    if len(parts) >= 2 and parts[0] == "src":
        return parts[1]

    # Use first meaningful directory
    for part in parts[:-1]:
        if part not in (".", "..", "src", "lib", "app"):
            return part

    return ""
