"""Tests for Repo Intelligence module (v4.0)."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from contribai.analysis.repo_intel import RepoIntelligence, RepoProfile


@pytest.fixture
def mock_github():
    """Create a mock GitHub client."""
    client = MagicMock()
    client.list_pull_requests = AsyncMock(
        return_value=[
            {
                "title": "Fix null pointer in parser",
                "merged_at": "2026-03-20T10:00:00Z",
                "created_at": "2026-03-19T08:00:00Z",
            },
            {
                "title": "Add unit tests for auth module",
                "merged_at": "2026-03-18T14:00:00Z",
                "created_at": "2026-03-17T10:00:00Z",
            },
            {
                "title": "Update README badges",
                "merged_at": None,  # closed, not merged
                "created_at": "2026-03-15T10:00:00Z",
            },
            {
                "title": "refactor: simplify config loader",
                "merged_at": "2026-03-14T12:00:00Z",
                "created_at": "2026-03-14T08:00:00Z",
            },
        ]
    )
    client.get_issues = AsyncMock(
        return_value=[
            {
                "number": 42,
                "title": "Crash on empty input",
                "labels": [{"name": "bug"}, {"name": "good first issue"}],
                "reactions": {"total_count": 5},
                "comments": 3,
            },
            {
                "number": 43,
                "title": "Feature request: dark mode",
                "labels": [{"name": "enhancement"}],
                "reactions": {"total_count": 2},
                "comments": 1,
            },
            {
                "number": 44,
                "title": "Regular issue",
                "labels": [],
                "reactions": {"total_count": 0},
                "comments": 0,
            },
            {
                "number": 45,
                "title": "This is actually a PR",
                "pull_request": {"url": "..."},  # should be filtered
                "labels": [{"name": "bug"}],
                "reactions": {"total_count": 10},
                "comments": 5,
            },
        ]
    )
    return client


class TestRepoIntelligence:
    """Test RepoIntelligence class."""

    @pytest.mark.asyncio
    async def test_profile_builds_complete_profile(self, mock_github):
        """Test that profile() builds a complete profile."""
        intel = RepoIntelligence(mock_github)
        profile = await intel.profile("owner", "repo")

        assert profile.repo == "owner/repo"
        assert len(profile.preferred_types) > 0
        assert profile.avg_review_hours > 0
        assert profile.summary != ""

    @pytest.mark.asyncio
    async def test_pr_classification(self, mock_github):
        """Test that PRs are classified correctly."""
        intel = RepoIntelligence(mock_github)
        profile = await intel.profile("owner", "repo")

        # "Fix null pointer" → bug_fix
        assert "bug_fix" in profile.preferred_types
        # "refactor: simplify config loader" → refactor
        assert "refactor" in profile.preferred_types

    @pytest.mark.asyncio
    async def test_rejected_types_tracked(self, mock_github):
        """Test that closed (non-merged) PRs are tracked as rejected."""
        intel = RepoIntelligence(mock_github)
        profile = await intel.profile("owner", "repo")

        # "Update README badges" was closed without merge
        assert len(profile.rejected_types) > 0

    @pytest.mark.asyncio
    async def test_actionable_issues_filtered(self, mock_github):
        """Test that only high-value issues are returned."""
        intel = RepoIntelligence(mock_github)
        profile = await intel.profile("owner", "repo")

        # Issue #42 has "bug" + "good first issue" labels + 5 reactions → high score
        assert len(profile.actionable_issues) > 0
        # Issue #42 should be first (highest score)
        assert profile.actionable_issues[0]["number"] == 42

        # PR disguised as issue #45 should be filtered out
        issue_numbers = [i["number"] for i in profile.actionable_issues]
        assert 45 not in issue_numbers

    @pytest.mark.asyncio
    async def test_issues_without_labels_excluded(self, mock_github):
        """Test that issues without high-value labels are excluded."""
        intel = RepoIntelligence(mock_github)
        profile = await intel.profile("owner", "repo")

        # Issue #44 has no labels → score = 0 → excluded
        issue_numbers = [i["number"] for i in profile.actionable_issues]
        assert 44 not in issue_numbers

    @pytest.mark.asyncio
    async def test_review_hours_calculation(self, mock_github):
        """Test avg review hours are computed correctly."""
        intel = RepoIntelligence(mock_github)
        profile = await intel.profile("owner", "repo")

        # PR 1: 26h, PR 2: 28h, PR 4: 4h → avg = (26+28+4)/3 ≈ 19.3h
        assert 4.0 < profile.avg_review_hours < 30.0


class TestRepoProfile:
    """Test RepoProfile data class."""

    def test_to_prompt_context_with_data(self):
        """Test prompt context generation with full data."""
        profile = RepoProfile(
            repo="owner/repo",
            preferred_types=["bug_fix", "test"],
            rejected_types=["docs"],
            actionable_issues=[
                {"number": 42, "title": "Crash on empty input", "labels": ["bug"], "score": 5},
            ],
            avg_review_hours=24.0,
        )

        ctx = profile.to_prompt_context()
        assert "owner/repo" in ctx
        assert "bug_fix" in ctx
        assert "AVOID" in ctx
        assert "#42" in ctx
        assert "24h" in ctx

    def test_to_prompt_context_empty(self):
        """Test prompt context generation with no data."""
        profile = RepoProfile(repo="empty/repo")
        ctx = profile.to_prompt_context()
        assert "empty/repo" in ctx


class TestPRClassification:
    """Test the PR title classification logic."""

    def test_classify_security_pr(self):
        """Test security PR detection."""
        intel = RepoIntelligence(MagicMock())
        assert intel._classify_pr("fix critical security vulnerability") == "security"

    def test_classify_bug_fix(self):
        """Test bug fix detection."""
        intel = RepoIntelligence(MagicMock())
        assert intel._classify_pr("fix crash on null input") == "bug_fix"

    def test_classify_test(self):
        """Test test PR detection."""
        intel = RepoIntelligence(MagicMock())
        assert intel._classify_pr("add unit tests for parser") == "test"

    def test_classify_refactor(self):
        """Test refactor PR detection."""
        intel = RepoIntelligence(MagicMock())
        assert intel._classify_pr("refactor: simplify config loader") == "refactor"

    def test_classify_docs(self):
        """Test docs PR detection."""
        intel = RepoIntelligence(MagicMock())
        assert intel._classify_pr("Update README with installation guide") == "docs"

    def test_classify_unknown(self):
        """Test unknown PR type."""
        intel = RepoIntelligence(MagicMock())
        assert intel._classify_pr("miscellaneous changes") == "other"

    def test_classify_performance(self):
        """Test performance PR detection."""
        intel = RepoIntelligence(MagicMock())
        assert intel._classify_pr("optimize database query performance") == "performance"
