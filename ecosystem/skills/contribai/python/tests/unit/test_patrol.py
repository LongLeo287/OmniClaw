"""Unit tests for PR Patrol engine."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from contribai.core.models import FeedbackAction, FeedbackItem, PatrolResult
from contribai.pr.patrol import (
    OUR_REPLY_MARKERS,
    REVIEW_BOT_LOGINS,
    PRPatrol,
)

# ── Test constants ─────────────────────────────────────────────────────────


class TestReviewBotLogins:
    """Test REVIEW_BOT_LOGINS constant."""

    def test_contains_coderabbitai(self):
        assert "coderabbitai" in REVIEW_BOT_LOGINS

    def test_contains_copilot(self):
        assert "copilot" in REVIEW_BOT_LOGINS

    def test_contains_dependabot(self):
        assert "dependabot" in REVIEW_BOT_LOGINS

    def test_contains_codecov(self):
        assert "codecov" in REVIEW_BOT_LOGINS


class TestOurReplyMarkers:
    """Test OUR_REPLY_MARKERS constant."""

    def test_contains_contribai(self):
        assert any("contribai" in m for m in OUR_REPLY_MARKERS)

    def test_contains_fixed(self):
        assert any("Fixed" in m for m in OUR_REPLY_MARKERS)


# ── Test PatrolResult ──────────────────────────────────────────────────────


class TestPatrolResult:
    """Test PatrolResult model."""

    def test_defaults(self):
        result = PatrolResult()
        assert result.prs_checked == 0
        assert result.fixes_pushed == 0
        assert result.replies_sent == 0
        assert result.cla_signed == 0
        assert result.prs_skipped == 0
        assert result.issues_found == 0
        assert result.assigned_issues == []
        assert result.errors == []

    def test_increment(self):
        result = PatrolResult()
        result.prs_checked += 1
        result.fixes_pushed += 2
        assert result.prs_checked == 1
        assert result.fixes_pushed == 2

    def test_assigned_issues(self):
        result = PatrolResult()
        result.assigned_issues.append({"repo": "test/repo", "number": 1})
        result.issues_found += 1
        assert result.issues_found == 1
        assert len(result.assigned_issues) == 1


# ── Test FeedbackItem ──────────────────────────────────────────────────────


class TestFeedbackItem:
    """Test FeedbackItem model."""

    def test_basic(self):
        item = FeedbackItem(
            comment_id=123,
            author="user1",
            body="Fix this",
            action=FeedbackAction.CODE_CHANGE,
        )
        assert item.comment_id == 123
        assert item.author == "user1"
        assert item.action == FeedbackAction.CODE_CHANGE
        assert item.is_inline is False
        assert item.bot_context is None

    def test_inline_with_bot_context(self):
        item = FeedbackItem(
            comment_id=456,
            author="maintainer",
            body="Please fix",
            action=FeedbackAction.CODE_CHANGE,
            file_path="server.py",
            line=26,
            is_inline=True,
            bot_context="[Bot review] Unused import detected",
        )
        assert item.is_inline is True
        assert item.bot_context == "[Bot review] Unused import detected"
        assert item.file_path == "server.py"
        assert item.line == 26


# ── Test FeedbackAction ────────────────────────────────────────────────────


class TestFeedbackAction:
    """Test FeedbackAction enum."""

    def test_values(self):
        assert FeedbackAction.CODE_CHANGE == "code_change"
        assert FeedbackAction.QUESTION == "question"
        assert FeedbackAction.STYLE_FIX == "style_fix"
        assert FeedbackAction.APPROVE == "approve"
        assert FeedbackAction.REJECT == "reject"
        assert FeedbackAction.ALREADY_HANDLED == "already_handled"

    def test_lookup(self):
        action_map = {a.value: a for a in FeedbackAction}
        assert action_map["code_change"] == FeedbackAction.CODE_CHANGE


# ── Test PRPatrol ──────────────────────────────────────────────────────────


class TestPRPatrolInit:
    """Test PRPatrol initialization."""

    def test_init(self):
        github = MagicMock()
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        assert patrol._github is github
        assert patrol._llm is llm
        assert patrol._user is None

    @pytest.mark.asyncio
    async def test_get_user(self):
        github = MagicMock()
        github.get_authenticated_user = AsyncMock(return_value={"login": "tang-vu"})
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        user = await patrol._get_user()
        assert user["login"] == "tang-vu"
        # Second call should use cache
        user2 = await patrol._get_user()
        assert user2["login"] == "tang-vu"
        github.get_authenticated_user.assert_called_once()


class TestCollectFeedback:
    """Test _collect_feedback method."""

    @pytest.mark.asyncio
    async def test_filters_own_comments(self):
        github = MagicMock()
        github.get_pr_comments = AsyncMock(
            return_value=[
                {"id": 1, "user": {"login": "tang-vu", "type": "User"}, "body": "test"},
            ]
        )
        github.get_pr_review_comments = AsyncMock(return_value=[])
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol._collect_feedback("owner", "repo", 1, "tang-vu")
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_filters_bot_comments(self):
        github = MagicMock()
        github.get_pr_comments = AsyncMock(
            return_value=[
                {"id": 1, "user": {"login": "netlify[bot]", "type": "Bot"}, "body": "deploy"},
            ]
        )
        github.get_pr_review_comments = AsyncMock(return_value=[])
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol._collect_feedback("owner", "repo", 1, "tang-vu")
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_filters_review_bot_logins(self):
        github = MagicMock()
        github.get_pr_comments = AsyncMock(return_value=[])
        github.get_pr_review_comments = AsyncMock(
            return_value=[
                {"id": 1, "user": {"login": "coderabbitai[bot]", "type": "Bot"}, "body": "review"},
            ]
        )
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol._collect_feedback("owner", "repo", 1, "tang-vu")
        assert len(result) == 0

    @pytest.mark.asyncio
    async def test_keeps_human_comments(self):
        github = MagicMock()
        github.get_pr_comments = AsyncMock(
            return_value=[
                {"id": 1, "user": {"login": "maintainer", "type": "User"}, "body": "LGTM"},
            ]
        )
        github.get_pr_review_comments = AsyncMock(return_value=[])
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol._collect_feedback("owner", "repo", 1, "tang-vu")
        assert len(result) == 1
        assert result[0]["author"] == "maintainer"

    @pytest.mark.asyncio
    async def test_bot_context_linked(self):
        """When human replies to bot review, bot_context is attached."""
        github = MagicMock()
        github.get_pr_comments = AsyncMock(return_value=[])
        github.get_pr_review_comments = AsyncMock(
            return_value=[
                {
                    "id": 100,
                    "user": {"login": "coderabbitai[bot]", "type": "Bot"},
                    "body": "Unused import detected: start_http_server",
                    "path": "server.py",
                    "line": 26,
                    "original_line": 26,
                    "diff_hunk": "@@ -23,6 +23,7 @@",
                    "in_reply_to_id": None,
                    "created_at": "2026-03-20",
                },
                {
                    "id": 200,
                    "user": {"login": "moshemorad", "type": "User"},
                    "body": "Hi can you please take a look?",
                    "path": "server.py",
                    "line": 26,
                    "original_line": 26,
                    "diff_hunk": "@@ -23,6 +23,7 @@",
                    "in_reply_to_id": 100,
                    "created_at": "2026-03-23",
                },
            ]
        )
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol._collect_feedback("owner", "repo", 1816, "tang-vu")
        assert len(result) == 1
        assert result[0]["author"] == "moshemorad"
        assert result[0]["bot_context"] is not None
        assert "Unused import" in result[0]["bot_context"]
        assert "coderabbitai" in result[0]["bot_context"]

    @pytest.mark.asyncio
    async def test_no_bot_context_when_no_reply(self):
        github = MagicMock()
        github.get_pr_comments = AsyncMock(return_value=[])
        github.get_pr_review_comments = AsyncMock(
            return_value=[
                {
                    "id": 300,
                    "user": {"login": "reviewer", "type": "User"},
                    "body": "This needs fixing",
                    "path": "main.py",
                    "line": 10,
                    "original_line": 10,
                    "diff_hunk": "@@ some diff",
                    "in_reply_to_id": None,
                    "created_at": "2026-03-23",
                },
            ]
        )
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol._collect_feedback("owner", "repo", 1, "tang-vu")
        assert len(result) == 1
        assert result[0]["bot_context"] is None


class TestBuildFixPrompt:
    """Test _build_fix_prompt method."""

    def test_basic_prompt(self):
        github = MagicMock()
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        item = FeedbackItem(
            comment_id=1,
            author="reviewer",
            body="Fix the typo",
            action=FeedbackAction.CODE_CHANGE,
        )
        prompt = patrol._build_fix_prompt(item, "file content", "main.py", "")
        assert "Fix the typo" in prompt
        assert "main.py" in prompt

    def test_prompt_includes_bot_context(self):
        github = MagicMock()
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        item = FeedbackItem(
            comment_id=1,
            author="maintainer",
            body="Please fix",
            action=FeedbackAction.CODE_CHANGE,
            bot_context="[Bot review by @coderabbitai] Unused import: start_http_server",
        )
        prompt = patrol._build_fix_prompt(item, "file content", "server.py", "")
        assert "bot code review" in prompt
        assert "Unused import" in prompt
        assert "coderabbitai" in prompt

    def test_prompt_includes_diff_hunk(self):
        github = MagicMock()
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        item = FeedbackItem(
            comment_id=1,
            author="reviewer",
            body="Fix it",
            action=FeedbackAction.CODE_CHANGE,
            diff_hunk="@@ -1,3 +1,4 @@",
        )
        prompt = patrol._build_fix_prompt(item, "", None, "diff content")
        assert "@@ -1,3 +1,4 @@" in prompt


class TestExtractFixedContent:
    """Test _extract_fixed_content method."""

    def test_plain_content(self):
        patrol = PRPatrol(github=MagicMock(), llm=MagicMock())
        result = patrol._extract_fixed_content("import os\nprint('hello')")
        assert "import os" in result

    def test_strips_code_fences(self):
        patrol = PRPatrol(github=MagicMock(), llm=MagicMock())
        result = patrol._extract_fixed_content("```python\nimport os\nprint('hello')\n```")
        assert result.strip() == "import os\nprint('hello')"
        assert "```" not in result


class TestParseClassifications:
    """Test _parse_classifications method."""

    def test_parses_yaml(self):
        patrol = PRPatrol(github=MagicMock(), llm=MagicMock())
        response = """```yaml
classifications:
  - comment_number: 1
    action: code_change
```"""
        feedback = [
            {
                "id": 1,
                "author": "user",
                "body": "fix this",
                "is_inline": True,
                "file_path": "main.py",
                "line": 10,
                "diff_hunk": None,
                "bot_context": None,
            }
        ]
        items = patrol._parse_classifications(response, feedback)
        assert len(items) == 1
        assert items[0].action == FeedbackAction.CODE_CHANGE

    def test_invalid_yaml(self):
        patrol = PRPatrol(github=MagicMock(), llm=MagicMock())
        result = patrol._parse_classifications("not yaml {{[", [])
        assert result == []

    def test_out_of_range_index(self):
        patrol = PRPatrol(github=MagicMock(), llm=MagicMock())
        response = """```yaml
classifications:
  - comment_number: 5
    action: code_change
```"""
        feedback = [{"id": 1, "author": "user", "body": "x", "is_inline": False}]
        items = patrol._parse_classifications(response, feedback)
        assert len(items) == 0


class TestCheckAssignedIssues:
    """Test _check_assigned_issues method."""

    @pytest.mark.asyncio
    async def test_finds_assigned_issues(self):
        github = MagicMock()
        github.get_assigned_issues = AsyncMock(
            return_value=[
                {"number": 42, "title": "Fix bug", "html_url": "https://example.com/42"},
            ]
        )
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = PatrolResult()
        repos = {"owner/repo"}
        await patrol._check_assigned_issues(repos, "tang-vu", result, dry_run=True)
        assert result.issues_found == 1
        assert result.assigned_issues[0]["number"] == 42

    @pytest.mark.asyncio
    async def test_empty_repos(self):
        patrol = PRPatrol(github=MagicMock(), llm=MagicMock())
        result = PatrolResult()
        await patrol._check_assigned_issues(set(), "tang-vu", result)
        assert result.issues_found == 0

    @pytest.mark.asyncio
    async def test_handles_api_error(self):
        github = MagicMock()
        github.get_assigned_issues = AsyncMock(side_effect=Exception("API error"))
        patrol = PRPatrol(github=github, llm=MagicMock())
        result = PatrolResult()
        await patrol._check_assigned_issues({"owner/repo"}, "tang-vu", result)
        assert result.issues_found == 0


class TestPatrolSkips:
    """Test patrol method skip logic."""

    @pytest.mark.asyncio
    async def test_skips_non_open_prs(self):
        github = MagicMock()
        github.get_authenticated_user = AsyncMock(return_value={"login": "tang-vu"})
        github.get_assigned_issues = AsyncMock(return_value=[])
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol.patrol(
            [{"repo": "o/r", "pr_number": 1, "status": "closed"}],
            dry_run=True,
        )
        assert result.prs_skipped == 1
        assert result.prs_checked == 0

    @pytest.mark.asyncio
    async def test_filters_by_pr_number(self):
        github = MagicMock()
        github.get_authenticated_user = AsyncMock(return_value={"login": "tang-vu"})
        github.get_assigned_issues = AsyncMock(return_value=[])
        github._get = AsyncMock(return_value={"state": "closed"})
        llm = MagicMock()
        patrol = PRPatrol(github=github, llm=llm)
        result = await patrol.patrol(
            [
                {"repo": "o/r", "pr_number": 1, "status": "open"},
                {"repo": "o/r", "pr_number": 2, "status": "open"},
            ],
            dry_run=True,
            pr_filter=1,
        )
        # Only PR #1 should be checked
        assert result.prs_checked <= 1
