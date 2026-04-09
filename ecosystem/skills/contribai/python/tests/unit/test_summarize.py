"""Tests for summarize_findings and context summarization."""

from __future__ import annotations

from contribai.analysis.analyzer import CodeAnalyzer
from contribai.core.models import ContributionType, Finding, Severity


class TestSummarizeFindings:
    """Tests for CodeAnalyzer.summarize_findings()."""

    def test_empty_findings(self):
        result = CodeAnalyzer.summarize_findings([])
        assert result == "No issues found."

    def test_single_finding(self):
        findings = [
            Finding(
                id="f1",
                type=ContributionType.SECURITY_FIX,
                severity=Severity.HIGH,
                title="SQL injection in login",
                description="Unsanitized input",
                file_path="app.py",
            ),
        ]
        result = CodeAnalyzer.summarize_findings(findings)
        assert "1 findings" in result
        assert "security_fix" in result
        assert "SQL injection" in result

    def test_multiple_findings_same_type(self):
        findings = [
            Finding(
                id="f1",
                type=ContributionType.CODE_QUALITY,
                severity=Severity.MEDIUM,
                title="Unused import",
                description="Remove unused import",
                file_path="utils.py",
            ),
            Finding(
                id="f2",
                type=ContributionType.CODE_QUALITY,
                severity=Severity.LOW,
                title="Long function",
                description="Split function",
                file_path="handlers.py",
            ),
        ]
        result = CodeAnalyzer.summarize_findings(findings)
        assert "2 findings" in result
        assert "code_quality" in result
        assert "Unused import" in result
        assert "Long function" in result

    def test_findings_grouped_by_type(self):
        findings = [
            Finding(
                id="f1",
                type=ContributionType.SECURITY_FIX,
                severity=Severity.CRITICAL,
                title="XSS vulnerability",
                description="Fix XSS",
                file_path="views.py",
            ),
            Finding(
                id="f2",
                type=ContributionType.PERFORMANCE_OPT,
                severity=Severity.MEDIUM,
                title="N+1 query",
                description="Fix N+1",
                file_path="models.py",
            ),
        ]
        result = CodeAnalyzer.summarize_findings(findings)
        assert "security_fix" in result
        assert "performance_opt" in result
        assert "critical" in result.lower() or "CRITICAL" in result

    def test_more_than_two_findings_truncated(self):
        """When >2 findings of same type, should show +N more."""
        findings = [
            Finding(
                id=f"f{i}",
                type=ContributionType.CODE_QUALITY,
                severity=Severity.LOW,
                title=f"Issue {i}",
                description=f"Description {i}",
                file_path=f"file{i}.py",
            )
            for i in range(5)
        ]
        result = CodeAnalyzer.summarize_findings(findings)
        assert "+3 more" in result

    def test_severity_counts(self):
        findings = [
            Finding(
                id="f1",
                type=ContributionType.SECURITY_FIX,
                severity=Severity.CRITICAL,
                title="Critical bug",
                description="Fix it",
                file_path="a.py",
            ),
            Finding(
                id="f2",
                type=ContributionType.CODE_QUALITY,
                severity=Severity.CRITICAL,
                title="Another critical",
                description="Fix it",
                file_path="b.py",
            ),
            Finding(
                id="f3",
                type=ContributionType.REFACTOR,
                severity=Severity.LOW,
                title="Minor refactor",
                description="Clean up",
                file_path="c.py",
            ),
        ]
        result = CodeAnalyzer.summarize_findings(findings)
        assert "3 findings" in result
        assert "critical: 2" in result
        assert "low: 1" in result

    def test_uses_type_not_contribution_type(self):
        """Regression test: Finding has .type, not .contribution_type.

        This was the v2.4.0 bug that caused AttributeError during hunt mode.
        """
        finding = Finding(
            id="f1",
            type=ContributionType.DOCS_IMPROVE,
            severity=Severity.LOW,
            title="Missing docstring",
            description="Add docstring",
            file_path="module.py",
        )
        # This should NOT raise AttributeError
        result = CodeAnalyzer.summarize_findings([finding])
        assert "docs_improve" in result
        assert "Missing docstring" in result
