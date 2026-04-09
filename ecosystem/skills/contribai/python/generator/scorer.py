"""Contribution quality scorer.

Evaluates generated contributions before submission
to prevent low-quality PRs from being created.
"""

from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from contribai.core.models import Contribution, ContributionType

logger = logging.getLogger(__name__)


@dataclass
class QualityReport:
    """Quality assessment of a contribution."""

    score: float  # 0.0 - 1.0
    passed: bool
    checks: dict[str, CheckResult]

    @property
    def summary(self) -> str:
        passed = sum(1 for c in self.checks.values() if c.passed)
        total = len(self.checks)
        return f"{passed}/{total} checks passed (score: {self.score:.0%})"


@dataclass
class CheckResult:
    """Result of a single quality check."""

    name: str
    passed: bool
    score: float  # 0.0 - 1.0
    reason: str


class QualityScorer:
    """Evaluates contribution quality before PR submission.

    Runs a series of heuristic checks to catch low-quality
    contributions that would likely be rejected by maintainers.
    """

    def __init__(self, min_score: float = 0.6):
        self._min_score = min_score

    def evaluate(self, contribution: Contribution) -> QualityReport:
        """Run all quality checks on a contribution.

        Args:
            contribution: The generated contribution to evaluate.

        Returns:
            QualityReport with individual check results and overall score.
        """
        checks = {}

        checks["has_changes"] = self._check_has_changes(contribution)
        checks["change_size"] = self._check_change_size(contribution)
        checks["commit_message"] = self._check_commit_message(contribution)
        checks["description"] = self._check_description(contribution)
        checks["no_debug_code"] = self._check_no_debug_code(contribution)
        checks["no_placeholders"] = self._check_no_placeholders(contribution)
        checks["file_coherence"] = self._check_file_coherence(contribution)

        total_score = sum(c.score for c in checks.values()) / len(checks)
        passed = total_score >= self._min_score

        report = QualityReport(score=total_score, passed=passed, checks=checks)
        logger.info("Quality check: %s", report.summary)
        return report

    def _check_has_changes(self, c: Contribution) -> CheckResult:
        """At least one meaningful file change."""
        has = len(c.changes) > 0 and any(len(ch.new_content.strip()) > 0 for ch in c.changes)
        return CheckResult(
            name="has_changes",
            passed=has,
            score=1.0 if has else 0.0,
            reason="Has file changes" if has else "No file changes",
        )

    def _check_change_size(self, c: Contribution) -> CheckResult:
        """Changes should be focused (not too big, not trivial)."""
        total_lines = sum(len(ch.new_content.splitlines()) for ch in c.changes)

        if total_lines == 0:
            return CheckResult("change_size", False, 0.0, "Empty changes")
        elif total_lines < 3:
            return CheckResult(
                "change_size",
                False,
                0.3,
                f"Very small change ({total_lines} lines)",
            )
        elif total_lines > 500:
            return CheckResult(
                "change_size",
                False,
                0.4,
                f"Very large change ({total_lines} lines)",
            )
        elif total_lines > 200:
            return CheckResult("change_size", True, 0.7, f"Large change ({total_lines} lines)")
        else:
            return CheckResult("change_size", True, 1.0, f"Good change size ({total_lines} lines)")

    def _check_commit_message(self, c: Contribution) -> CheckResult:
        """Commit message follows conventional format."""
        msg = c.commit_message
        if not msg:
            return CheckResult("commit_message", False, 0.0, "Empty commit message")

        # Check conventional commit format: type: description
        conventional = re.match(r"^(feat|fix|docs|refactor|perf|test|chore)\(?.*\)?: .+", msg)
        if conventional:
            return CheckResult("commit_message", True, 1.0, "Follows conventional commits")

        if len(msg) > 10:
            return CheckResult("commit_message", True, 0.7, "Descriptive but not conventional")

        return CheckResult("commit_message", False, 0.3, "Poor commit message")

    def _check_description(self, c: Contribution) -> CheckResult:
        """PR description is meaningful."""
        desc = c.description
        if not desc:
            return CheckResult("description", False, 0.0, "Empty description")
        if len(desc) < 20:
            return CheckResult("description", False, 0.3, "Description too short")
        return CheckResult("description", True, 1.0, "Good description")

    def _check_no_debug_code(self, c: Contribution) -> CheckResult:
        """No debug statements in generated code."""
        debug_patterns = [
            r"\bprint\s*\(",
            r"\bconsole\.log\s*\(",
            r"\bdebugger\b",
            r"\bpdb\.set_trace\(",
            r"\bbreakpoint\(\)",
            r"#\s*TODO\b",
            r"#\s*FIXME\b",
            r"#\s*HACK\b",
        ]

        issues = []
        for change in c.changes:
            for pattern in debug_patterns:
                if re.search(pattern, change.new_content):
                    issues.append(f"{change.path}: {pattern}")

        if not issues:
            return CheckResult("no_debug_code", True, 1.0, "No debug code found")

        # Allow some patterns (TODO can be intentional)
        severity = 0.8 if len(issues) <= 2 else 0.4
        return CheckResult(
            "no_debug_code",
            severity >= 0.6,
            severity,
            f"Found {len(issues)} debug patterns",
        )

    def _check_no_placeholders(self, c: Contribution) -> CheckResult:
        """No placeholder text in generated code."""
        placeholder_patterns = [
            r"YOUR_.*_HERE",
            r"REPLACE_THIS",
            r"PLACEHOLDER",
            r"XXX",
            r"lorem ipsum",
            r"example\.com",
            r"foo\s*bar",
        ]

        for change in c.changes:
            content_lower = change.new_content.lower()
            for pattern in placeholder_patterns:
                if re.search(pattern, content_lower, re.IGNORECASE):
                    return CheckResult(
                        "no_placeholders",
                        False,
                        0.2,
                        f"Found placeholder: {pattern} in {change.path}",
                    )

        return CheckResult("no_placeholders", True, 1.0, "No placeholders found")

    def _check_file_coherence(self, c: Contribution) -> CheckResult:
        """Changes are related to the finding."""
        if not c.changes:
            return CheckResult("file_coherence", False, 0.0, "No changes")

        # Check that the finding's file is actually changed
        finding_file = c.finding.file_path
        changed_files = {ch.path for ch in c.changes}

        if finding_file in changed_files:
            return CheckResult("file_coherence", True, 1.0, "Finding file is changed")

        # Some contributions legitimately change different files
        if c.contribution_type in (ContributionType.DOCS_IMPROVE, ContributionType.FEATURE_ADD):
            return CheckResult("file_coherence", True, 0.8, "Different file but type allows it")

        return CheckResult(
            "file_coherence",
            False,
            0.4,
            f"Finding in {finding_file} but changes in {changed_files}",
        )
