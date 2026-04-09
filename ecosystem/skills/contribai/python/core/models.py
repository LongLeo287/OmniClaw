"""Shared data models for ContribAI."""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum

from pydantic import BaseModel, Field

# ── Enums ──────────────────────────────────────────────────────────────────────


class ContributionType(StrEnum):
    """Types of contributions the agent can make."""

    SECURITY_FIX = "security_fix"
    FEATURE_ADD = "feature_add"
    DOCS_IMPROVE = "docs_improve"
    UI_UX_FIX = "ui_ux_fix"
    PERFORMANCE_OPT = "performance_opt"
    REFACTOR = "refactor"
    CODE_QUALITY = "code_quality"


class Severity(StrEnum):
    """Severity level for findings."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class PRStatus(StrEnum):
    """Status of a submitted pull request."""

    PENDING = "pending"
    OPEN = "open"
    MERGED = "merged"
    CLOSED = "closed"
    REVIEW_REQUESTED = "review_requested"


# ── GitHub Models ──────────────────────────────────────────────────────────────


class Repository(BaseModel):
    """GitHub repository metadata."""

    owner: str
    name: str
    full_name: str  # owner/name
    description: str | None = None
    language: str | None = None
    languages: dict[str, int] = Field(default_factory=dict)
    stars: int = 0
    forks: int = 0
    open_issues: int = 0
    topics: list[str] = Field(default_factory=list)
    default_branch: str = "main"
    html_url: str = ""
    clone_url: str = ""
    has_contributing: bool = False
    has_license: bool = False
    last_push_at: datetime | None = None
    created_at: datetime | None = None

    @property
    def url(self) -> str:
        return f"https://github.com/{self.full_name}"


class Issue(BaseModel):
    """GitHub issue."""

    number: int
    title: str
    body: str | None = None
    labels: list[str] = Field(default_factory=list)
    state: str = "open"
    created_at: datetime | None = None
    html_url: str = ""


class FileNode(BaseModel):
    """A file or directory in the repo tree."""

    path: str
    type: str  # "blob" or "tree"
    size: int = 0
    sha: str = ""


# ── Analysis Models ────────────────────────────────────────────────────────────


class Finding(BaseModel):
    """An individual issue found during analysis."""

    id: str = ""
    type: ContributionType
    severity: Severity
    title: str
    description: str
    file_path: str
    line_start: int | None = None
    line_end: int | None = None
    suggestion: str | None = None
    confidence: float = 0.8  # 0.0 - 1.0

    @property
    def priority_score(self) -> float:
        """Higher = more important."""
        severity_weights = {
            Severity.CRITICAL: 4.0,
            Severity.HIGH: 3.0,
            Severity.MEDIUM: 2.0,
            Severity.LOW: 1.0,
        }
        return severity_weights[self.severity] * self.confidence


class AnalysisResult(BaseModel):
    """Aggregated results from code analysis."""

    repo: Repository
    findings: list[Finding] = Field(default_factory=list)
    analyzed_files: int = 0
    skipped_files: int = 0
    analysis_duration_sec: float = 0.0
    analyzer_versions: dict[str, str] = Field(default_factory=dict)

    @property
    def top_findings(self) -> list[Finding]:
        """Findings sorted by priority, highest first."""
        return sorted(self.findings, key=lambda f: f.priority_score, reverse=True)

    def filter_by_type(self, contrib_type: ContributionType) -> list[Finding]:
        return [f for f in self.findings if f.type == contrib_type]

    def filter_by_severity(self, min_severity: Severity) -> list[Finding]:
        order = [Severity.LOW, Severity.MEDIUM, Severity.HIGH, Severity.CRITICAL]
        min_idx = order.index(min_severity)
        return [f for f in self.findings if order.index(f.severity) >= min_idx]


# ── Contribution Models ────────────────────────────────────────────────────────


class FileChange(BaseModel):
    """A single file change in a contribution."""

    path: str
    original_content: str | None = None
    new_content: str
    is_new_file: bool = False
    is_deleted: bool = False


class Contribution(BaseModel):
    """A generated contribution ready to be submitted."""

    finding: Finding
    contribution_type: ContributionType
    title: str
    description: str
    changes: list[FileChange] = Field(default_factory=list)
    commit_message: str = ""
    tests_added: list[FileChange] = Field(default_factory=list)
    branch_name: str = ""
    generated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))

    @property
    def total_files_changed(self) -> int:
        return len(self.changes) + len(self.tests_added)


class PRResult(BaseModel):
    """Result of creating a pull request."""

    repo: Repository
    contribution: Contribution
    pr_number: int
    pr_url: str
    status: PRStatus = PRStatus.OPEN
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    branch_name: str = ""
    fork_full_name: str = ""


# ── Discovery Models ──────────────────────────────────────────────────────────


class DiscoveryCriteria(BaseModel):
    """Criteria for discovering repositories."""

    languages: list[str] = Field(default_factory=lambda: ["python"])
    stars_min: int = 50
    stars_max: int = 10000
    min_last_activity_days: int = 30
    require_contributing_guide: bool = False
    topics: list[str] = Field(default_factory=list)
    max_results: int = 20
    exclude_repos: list[str] = Field(default_factory=list)  # full_name list


class RepoContext(BaseModel):
    """Full context about a repository for LLM prompting."""

    repo: Repository
    file_tree: list[FileNode] = Field(default_factory=list)
    readme_content: str | None = None
    contributing_guide: str | None = None
    relevant_files: dict[str, str] = Field(default_factory=dict)  # path -> content
    open_issues: list[Issue] = Field(default_factory=list)
    coding_style: str | None = None  # detected coding conventions


# ── Patrol Models ──────────────────────────────────────────────────────────


class FeedbackAction(StrEnum):
    """What action to take for a review comment."""

    CODE_CHANGE = "code_change"
    QUESTION = "question"
    STYLE_FIX = "style_fix"
    APPROVE = "approve"
    REJECT = "reject"
    ALREADY_HANDLED = "already_handled"


class FeedbackItem(BaseModel):
    """A classified review comment requiring action."""

    comment_id: int
    author: str
    body: str
    action: FeedbackAction
    file_path: str | None = None
    line: int | None = None
    diff_hunk: str | None = None
    is_inline: bool = False  # True = code review comment, False = issue comment
    bot_context: str | None = None  # Original bot review context when human replies to bot


class PatrolResult(BaseModel):
    """Result of a patrol run."""

    prs_checked: int = 0
    fixes_pushed: int = 0
    replies_sent: int = 0
    cla_signed: int = 0
    prs_skipped: int = 0
    issues_found: int = 0
    assigned_issues: list[dict] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)
