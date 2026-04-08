"""Tests for the PR manager."""

from unittest.mock import AsyncMock

import pytest

from contribai.core.models import (
    Contribution,
    ContributionType,
    FileChange,
    Finding,
    PRStatus,
    Severity,
)
from contribai.pr.manager import PRManager


@pytest.fixture
def pr_manager(mock_github):
    return PRManager(github=mock_github)


@pytest.fixture
def sample_contribution():
    finding = Finding(
        id="test001",
        type=ContributionType.SECURITY_FIX,
        severity=Severity.HIGH,
        title="Fix SQL injection",
        description="Parameterize queries",
        file_path="db.py",
    )
    return Contribution(
        finding=finding,
        contribution_type=ContributionType.SECURITY_FIX,
        title="🔒 Security: Fix SQL injection",
        description="Parameterized all SQL queries",
        changes=[
            FileChange(path="db.py", new_content="safe_query()", is_new_file=False),
        ],
        commit_message="fix(security): parameterize sql queries",
        branch_name="fix/security/sql-injection",
    )


class TestPRBody:
    def test_contains_problem(self, pr_manager, sample_contribution):
        body = pr_manager._generate_pr_body(sample_contribution)
        assert "Problem" in body
        assert "Parameterize queries" in body

    def test_contains_severity(self, pr_manager, sample_contribution):
        body = pr_manager._generate_pr_body(sample_contribution)
        assert "high" in body

    def test_contains_files(self, pr_manager, sample_contribution):
        body = pr_manager._generate_pr_body(sample_contribution)
        assert "db.py" in body

    def test_contains_contribai_attribution(self, pr_manager, sample_contribution):
        body = pr_manager._generate_pr_body(sample_contribution)
        # Stealth mode: no ContribAI branding in PR body
        assert "ContribAI" not in body

    def test_contains_testing_checklist(self, pr_manager, sample_contribution):
        body = pr_manager._generate_pr_body(sample_contribution)
        assert "Testing" in body

    def test_contains_solution(self, pr_manager, sample_contribution):
        body = pr_manager._generate_pr_body(sample_contribution)
        assert "Solution" in body

    def test_docs_emoji(self, pr_manager):
        finding = Finding(
            type=ContributionType.DOCS_IMPROVE,
            severity=Severity.LOW,
            title="Add docs",
            description="Missing docs",
            file_path="README.md",
        )
        contrib = Contribution(
            finding=finding,
            contribution_type=ContributionType.DOCS_IMPROVE,
            title="📝 Docs: Add docs",
            description="Added documentation",
            changes=[FileChange(path="README.md", new_content="# Docs")],
        )
        body = pr_manager._generate_pr_body(contrib)
        assert "Missing docs" in body


class TestGetPRStatus:
    @pytest.mark.asyncio
    async def test_open_pr(self, pr_manager):
        pr_manager._github._get = AsyncMock(
            return_value={"state": "open", "merged": False, "requested_reviewers": []}
        )
        status = await pr_manager.get_pr_status("owner", "repo", 1)
        assert status == PRStatus.OPEN

    @pytest.mark.asyncio
    async def test_merged_pr(self, pr_manager):
        pr_manager._github._get = AsyncMock(return_value={"state": "closed", "merged": True})
        status = await pr_manager.get_pr_status("owner", "repo", 1)
        assert status == PRStatus.MERGED

    @pytest.mark.asyncio
    async def test_closed_pr(self, pr_manager):
        pr_manager._github._get = AsyncMock(return_value={"state": "closed", "merged": False})
        status = await pr_manager.get_pr_status("owner", "repo", 1)
        assert status == PRStatus.CLOSED

    @pytest.mark.asyncio
    async def test_review_requested(self, pr_manager):
        pr_manager._github._get = AsyncMock(
            return_value={
                "state": "open",
                "merged": False,
                "requested_reviewers": [{"login": "reviewer"}],
            }
        )
        status = await pr_manager.get_pr_status("owner", "repo", 1)
        assert status == PRStatus.REVIEW_REQUESTED

    @pytest.mark.asyncio
    async def test_error_returns_pending(self, pr_manager):
        pr_manager._github._get = AsyncMock(side_effect=Exception("API error"))
        status = await pr_manager.get_pr_status("owner", "repo", 1)
        assert status == PRStatus.PENDING
