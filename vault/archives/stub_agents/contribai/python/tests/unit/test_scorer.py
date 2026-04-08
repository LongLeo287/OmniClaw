"""Tests for contribution quality scorer."""

import pytest

from contribai.core.models import (
    Contribution,
    ContributionType,
    FileChange,
    Finding,
    Severity,
)
from contribai.generator.scorer import QualityScorer


@pytest.fixture
def scorer():
    return QualityScorer(min_score=0.6)


@pytest.fixture
def good_contribution():
    return Contribution(
        finding=Finding(
            type=ContributionType.SECURITY_FIX,
            severity=Severity.HIGH,
            title="Fix SQL injection",
            description="Parameterize queries to prevent injection",
            file_path="db.py",
        ),
        contribution_type=ContributionType.SECURITY_FIX,
        title="Fix SQL injection in db.py",
        description="Parameterized all raw SQL queries to prevent SQL injection attacks.",
        changes=[
            FileChange(
                path="db.py",
                new_content=(
                    "import sqlite3\n\n"
                    "def query(db, user_id):\n"
                    "    cursor = db.execute("
                    "'SELECT * FROM users WHERE id = ?', (user_id,))\n"
                    "    return cursor.fetchall()\n"
                ),
            )
        ],
        commit_message="fix(security): parameterize sql queries to prevent injection",
        branch_name="contribai/fix/sql-injection",
    )


@pytest.fixture
def bad_contribution():
    return Contribution(
        finding=Finding(
            type=ContributionType.CODE_QUALITY,
            severity=Severity.LOW,
            title="Fix stuff",
            description="",
            file_path="a.py",
        ),
        contribution_type=ContributionType.CODE_QUALITY,
        title="Fix",
        description="",
        changes=[FileChange(path="b.py", new_content="# TODO: fix later\nprint('debug')")],
        commit_message="fix",
    )


class TestQualityScorer:
    def test_good_contribution_passes(self, scorer, good_contribution):
        report = scorer.evaluate(good_contribution)
        assert report.passed is True
        assert report.score >= 0.6

    def test_bad_contribution_fails(self, scorer, bad_contribution):
        report = scorer.evaluate(bad_contribution)
        assert report.passed is False

    def test_empty_changes_fail(self, scorer):
        contrib = Contribution(
            finding=Finding(
                type=ContributionType.BUG_FIX
                if hasattr(ContributionType, "BUG_FIX")
                else ContributionType.CODE_QUALITY,
                severity=Severity.LOW,
                title="X",
                description="X",
                file_path="x.py",
            ),
            contribution_type=ContributionType.CODE_QUALITY,
            title="X",
            description="X",
            changes=[],
        )
        report = scorer.evaluate(contrib)
        assert report.checks["has_changes"].passed is False

    def test_conventional_commit_passes(self, scorer, good_contribution):
        report = scorer.evaluate(good_contribution)
        assert report.checks["commit_message"].passed is True
        assert report.checks["commit_message"].score == 1.0

    def test_non_conventional_commit(self, scorer, good_contribution):
        good_contribution.commit_message = "fixed the thing properly"
        report = scorer.evaluate(good_contribution)
        assert report.checks["commit_message"].score >= 0.5  # descriptive but not conventional

    def test_debug_code_detected(self, scorer, bad_contribution):
        report = scorer.evaluate(bad_contribution)
        assert report.checks["no_debug_code"].score < 1.0

    def test_placeholder_detected(self, scorer, good_contribution):
        good_contribution.changes[0].new_content = "API_KEY = 'YOUR_KEY_HERE'"
        report = scorer.evaluate(good_contribution)
        assert report.checks["no_placeholders"].passed is False

    def test_file_coherence_same_file(self, scorer, good_contribution):
        report = scorer.evaluate(good_contribution)
        assert report.checks["file_coherence"].passed is True

    def test_file_coherence_different_file(self, scorer, bad_contribution):
        report = scorer.evaluate(bad_contribution)
        # Finding is in a.py but changes are in b.py
        assert report.checks["file_coherence"].score < 1.0

    def test_summary_format(self, scorer, good_contribution):
        report = scorer.evaluate(good_contribution)
        assert "checks passed" in report.summary
        assert "score:" in report.summary

    def test_change_size_too_large(self, scorer, good_contribution):
        good_contribution.changes[0].new_content = "x\n" * 600
        report = scorer.evaluate(good_contribution)
        assert report.checks["change_size"].score < 1.0

    def test_change_size_too_small(self, scorer, good_contribution):
        good_contribution.changes[0].new_content = "x"
        report = scorer.evaluate(good_contribution)
        assert report.checks["change_size"].score < 1.0
