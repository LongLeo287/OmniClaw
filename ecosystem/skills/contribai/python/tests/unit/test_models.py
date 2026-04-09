"""Tests for data models."""

import pytest

from contribai.core.models import (
    AnalysisResult,
    ContributionType,
    Finding,
    Repository,
    Severity,
)


class TestRepository:
    def test_url_property(self, sample_repo):
        assert sample_repo.url == "https://github.com/testowner/testrepo"

    def test_create_minimal(self):
        repo = Repository(owner="x", name="y", full_name="x/y")
        assert repo.stars == 0
        assert repo.default_branch == "main"


class TestFinding:
    def test_priority_score(self, sample_finding):
        # HIGH severity (3.0) * 0.9 confidence = 2.7
        assert sample_finding.priority_score == pytest.approx(2.7)

    def test_critical_priority(self):
        f = Finding(
            type=ContributionType.SECURITY_FIX,
            severity=Severity.CRITICAL,
            title="Test",
            description="Test",
            file_path="test.py",
            confidence=1.0,
        )
        assert f.priority_score == 4.0

    def test_low_priority(self):
        f = Finding(
            type=ContributionType.DOCS_IMPROVE,
            severity=Severity.LOW,
            title="Test",
            description="Test",
            file_path="test.py",
            confidence=0.5,
        )
        assert f.priority_score == 0.5


class TestAnalysisResult:
    def test_top_findings_sorted(self, sample_repo):
        findings = [
            Finding(
                type=ContributionType.DOCS_IMPROVE,
                severity=Severity.LOW,
                title="Low",
                description="",
                file_path="a.py",
            ),
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.CRITICAL,
                title="Critical",
                description="",
                file_path="b.py",
            ),
            Finding(
                type=ContributionType.CODE_QUALITY,
                severity=Severity.MEDIUM,
                title="Medium",
                description="",
                file_path="c.py",
            ),
        ]
        result = AnalysisResult(repo=sample_repo, findings=findings)
        top = result.top_findings
        assert top[0].title == "Critical"
        assert top[-1].title == "Low"

    def test_filter_by_type(self, sample_repo):
        findings = [
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.HIGH,
                title="Sec",
                description="",
                file_path="a.py",
            ),
            Finding(
                type=ContributionType.DOCS_IMPROVE,
                severity=Severity.LOW,
                title="Doc",
                description="",
                file_path="b.py",
            ),
        ]
        result = AnalysisResult(repo=sample_repo, findings=findings)
        sec = result.filter_by_type(ContributionType.SECURITY_FIX)
        assert len(sec) == 1
        assert sec[0].title == "Sec"

    def test_filter_by_severity(self, sample_repo):
        findings = [
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.LOW,
                title="Low",
                description="",
                file_path="a.py",
            ),
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.HIGH,
                title="High",
                description="",
                file_path="b.py",
            ),
            Finding(
                type=ContributionType.SECURITY_FIX,
                severity=Severity.CRITICAL,
                title="Crit",
                description="",
                file_path="c.py",
            ),
        ]
        result = AnalysisResult(repo=sample_repo, findings=findings)
        high_plus = result.filter_by_severity(Severity.HIGH)
        assert len(high_plus) == 2
