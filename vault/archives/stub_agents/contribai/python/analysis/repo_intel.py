"""Repo Intelligence — profile repos before contributing.

Analyzes a repository's contribution culture by examining:
- Recently merged PRs (what types get accepted)
- Open issues with high engagement (what maintainers want fixed)
- Contributor guidelines and preferences
- Review speed and maintainer activity

This intelligence is injected into analysis prompts to focus
ContribAI on contributions that are likely to be accepted.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from typing import ClassVar

from contribai.github.client import GitHubClient

logger = logging.getLogger(__name__)


@dataclass
class RepoProfile:
    """Intelligence gathered about a repository's contribution culture."""

    repo: str
    # What types of contributions this repo merges
    merged_pr_types: list[str] = field(default_factory=list)
    # High-value open issues (good first issue, help wanted, bug)
    actionable_issues: list[dict] = field(default_factory=list)
    # How fast the repo reviews PRs (avg hours)
    avg_review_hours: float = 0.0
    # Whether the repo is actively maintained
    is_active: bool = True
    # Preferred contribution types based on merged PRs
    preferred_types: list[str] = field(default_factory=list)
    # Types that were rejected (closed without merge)
    rejected_types: list[str] = field(default_factory=list)
    # Summary string for injection into prompts
    summary: str = ""

    def to_prompt_context(self) -> str:
        """Format profile as context for LLM prompts."""
        parts = [f"REPO INTELLIGENCE for {self.repo}:"]

        if self.preferred_types:
            parts.append(f"- Preferred contributions: {', '.join(self.preferred_types)}")
        if self.rejected_types:
            parts.append(f"- Rejected types (AVOID): {', '.join(self.rejected_types)}")
        if self.actionable_issues:
            parts.append("- High-value open issues:")
            for issue in self.actionable_issues[:5]:
                labels = ", ".join(issue.get("labels", []))
                parts.append(f"  #{issue['number']}: {issue['title']} [{labels}]")
        if self.avg_review_hours > 0:
            parts.append(f"- Avg review time: {self.avg_review_hours:.0f}h")

        return "\n".join(parts)


class RepoIntelligence:
    """Gather intelligence about a repo before contributing."""

    # Classify PR titles into contribution types
    TYPE_KEYWORDS: ClassVar[dict[str, list[str]]] = {
        "security": ["security", "vulnerability", "cve", "xss", "injection", "auth"],
        "bug_fix": ["fix", "bug", "crash", "error", "issue", "broken", "null", "none"],
        "test": ["test", "coverage", "spec", "unittest", "pytest"],
        "docs": ["doc", "readme", "changelog", "comment", "docstring"],
        "refactor": ["refactor", "cleanup", "simplify", "extract", "reorganize"],
        "performance": ["perf", "performance", "speed", "optimize", "cache", "memory"],
        "feature": ["add", "feat", "feature", "support", "implement", "new"],
        "ci": ["ci", "workflow", "github action", "pipeline", "build"],
        "deps": ["bump", "upgrade", "dependency", "update", "version"],
    }

    # Issue labels that indicate high-value contribution opportunities
    HIGH_VALUE_LABELS: ClassVar[set[str]] = {
        "good first issue",
        "help wanted",
        "bug",
        "enhancement",
        "easy",
        "beginner",
        "low-hanging fruit",
        "contributions welcome",
        "hacktoberfest",
    }

    def __init__(self, github: GitHubClient):
        self._github = github

    async def profile(self, owner: str, repo: str) -> RepoProfile:
        """Build a comprehensive profile of a repo's contribution culture.

        Args:
            owner: Repository owner.
            repo: Repository name.

        Returns:
            RepoProfile with intelligence for guiding contributions.
        """
        full_name = f"{owner}/{repo}"
        profile = RepoProfile(repo=full_name)

        # 1. Analyze recently merged PRs
        try:
            merged_types, rejected_types, avg_hours = await self._analyze_pr_history(owner, repo)
            profile.merged_pr_types = merged_types
            profile.preferred_types = list(set(merged_types))
            profile.rejected_types = list(set(rejected_types))
            profile.avg_review_hours = avg_hours
        except Exception as e:
            logger.debug("Could not analyze PR history for %s: %s", full_name, e)

        # 2. Find high-value open issues
        try:
            profile.actionable_issues = await self._find_actionable_issues(owner, repo)
        except Exception as e:
            logger.debug("Could not fetch issues for %s: %s", full_name, e)

        # 3. Build summary
        profile.summary = profile.to_prompt_context()
        logger.info(
            "🧠 Repo intel for %s: %d preferred types, %d actionable issues",
            full_name,
            len(profile.preferred_types),
            len(profile.actionable_issues),
        )

        return profile

    async def _analyze_pr_history(
        self, owner: str, repo: str
    ) -> tuple[list[str], list[str], float]:
        """Analyze recent PRs to understand what the repo values.

        Returns:
            Tuple of (merged_types, rejected_types, avg_review_hours).
        """
        prs = await self._github.list_pull_requests(owner, repo, state="closed", per_page=30)

        merged_types: list[str] = []
        rejected_types: list[str] = []
        review_hours: list[float] = []

        for pr in prs:
            title = (pr.get("title") or "").lower()
            pr_type = self._classify_pr(title)

            if pr.get("merged_at"):
                merged_types.append(pr_type)
                # Calculate review time
                created = pr.get("created_at", "")
                merged = pr.get("merged_at", "")
                if created and merged:
                    hours = self._time_diff_hours(created, merged)
                    if hours is not None and hours < 720:  # cap at 30 days
                        review_hours.append(hours)
            else:
                rejected_types.append(pr_type)

        avg_hours = sum(review_hours) / len(review_hours) if review_hours else 0.0
        return merged_types, rejected_types, avg_hours

    async def _find_actionable_issues(
        self, owner: str, repo: str, max_issues: int = 10
    ) -> list[dict]:
        """Find open issues that are good candidates for contribution.

        Prioritizes issues with high-value labels like 'good first issue',
        'help wanted', 'bug'.
        """
        try:
            issues = await self._github.get_issues(owner, repo, state="open", per_page=30)
        except Exception:
            return []

        actionable: list[dict] = []
        for issue in issues:
            # Skip pull requests (GitHub lists them as issues too)
            if issue.get("pull_request"):
                continue

            labels = [
                lbl.get("name", "").lower()
                for lbl in issue.get("labels", [])
                if isinstance(lbl, dict)
            ]

            # Score by labels — prioritize high-value
            score = sum(1 for lbl in labels if lbl in self.HIGH_VALUE_LABELS)
            # Boost issues with many reactions (community interest)
            reactions = issue.get("reactions", {})
            score += reactions.get("total_count", 0) if isinstance(reactions, dict) else 0

            if score > 0:
                actionable.append(
                    {
                        "number": issue["number"],
                        "title": issue.get("title", ""),
                        "labels": labels,
                        "score": score,
                        "comments": issue.get("comments", 0),
                    }
                )

        # Sort by score descending
        actionable.sort(key=lambda x: x["score"], reverse=True)
        return actionable[:max_issues]

    def _classify_pr(self, title: str) -> str:
        """Classify a PR title into a contribution type."""
        title_lower = title.lower()
        for pr_type, keywords in self.TYPE_KEYWORDS.items():
            if any(kw in title_lower for kw in keywords):
                return pr_type
        return "other"

    @staticmethod
    def _time_diff_hours(created: str, merged: str) -> float | None:
        """Calculate hours between two ISO timestamps."""
        from datetime import datetime

        try:
            fmt = "%Y-%m-%dT%H:%M:%SZ"
            c = datetime.strptime(created, fmt)
            m = datetime.strptime(merged, fmt)
            return (m - c).total_seconds() / 3600
        except Exception:
            return None
