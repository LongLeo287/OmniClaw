"""Tests for the issue solver engine.

Tests for v2.0.0 issue-driven mode: fetch_solvable_issues,
solve_issue_deep, multi-file parsing, linked PR detection.
"""

from unittest.mock import AsyncMock

import pytest

from contribai.core.models import ContributionType, FileNode, Issue, RepoContext
from contribai.issues.solver import IssueCategory, IssueSolver


@pytest.fixture
def solver(mock_llm, mock_github):
    return IssueSolver(llm=mock_llm, github=mock_github)


@pytest.fixture
def bug_issue():
    return Issue(
        number=1, title="App crashes on login", body="TypeError when user logs in", labels=["bug"]
    )


@pytest.fixture
def feature_issue():
    return Issue(
        number=2,
        title="Add dark mode support",
        body="Please add dark theme toggle",
        labels=["enhancement"],
    )


@pytest.fixture
def docs_issue():
    return Issue(
        number=3, title="Fix typo in README", body="Line 42 has a typo", labels=["documentation"]
    )


@pytest.fixture
def unlabeled_issue():
    return Issue(number=4, title="Fix the broken login page", body="Login doesn't work")


@pytest.fixture
def good_first_issue():
    return Issue(
        number=10,
        title="Update header text",
        body="Simple text change needed",
        labels=["good first issue"],
    )


class TestClassifyIssue:
    def test_bug_by_label(self, solver, bug_issue):
        assert solver.classify_issue(bug_issue) == IssueCategory.BUG

    def test_feature_by_label(self, solver, feature_issue):
        assert solver.classify_issue(feature_issue) == IssueCategory.FEATURE

    def test_docs_by_label(self, solver, docs_issue):
        assert solver.classify_issue(docs_issue) == IssueCategory.DOCS

    def test_security_by_label(self, solver):
        issue = Issue(number=5, title="Something", labels=["security"])
        assert solver.classify_issue(issue) == IssueCategory.SECURITY

    def test_good_first_issue(self, solver):
        issue = Issue(number=6, title="Something", labels=["good first issue"])
        assert solver.classify_issue(issue) == IssueCategory.GOOD_FIRST_ISSUE

    def test_keyword_fallback_bug(self, solver, unlabeled_issue):
        assert solver.classify_issue(unlabeled_issue) == IssueCategory.BUG

    def test_keyword_fallback_feature(self, solver):
        issue = Issue(number=7, title="Add support for webhooks", labels=[])
        assert solver.classify_issue(issue) == IssueCategory.FEATURE

    def test_keyword_fallback_docs(self, solver):
        issue = Issue(number=8, title="Update documentation for API", labels=[])
        assert solver.classify_issue(issue) == IssueCategory.DOCS

    def test_performance_by_label(self, solver):
        issue = Issue(number=9, title="Slow query", labels=["performance"])
        assert solver.classify_issue(issue) == IssueCategory.PERFORMANCE

    def test_ui_ux_by_keyword(self, solver):
        issue = Issue(number=10, title="Improve accessibility for screen readers", labels=[])
        assert solver.classify_issue(issue) == IssueCategory.UI_UX


class TestEstimateComplexity:
    def test_good_first_issue_simple(self, solver):
        issue = Issue(number=1, title="Easy fix", labels=["good first issue"])
        assert solver._estimate_complexity(issue) == 1

    def test_beginner_label_simple(self, solver):
        issue = Issue(number=1, title="Easy fix", labels=["beginner"])
        assert solver._estimate_complexity(issue) == 1

    def test_short_issue_moderate(self, solver, bug_issue):
        assert solver._estimate_complexity(bug_issue) <= 3

    def test_long_body_complex(self, solver):
        issue = Issue(number=2, title="Complex bug", body="x" * 3000, labels=[])
        assert solver._estimate_complexity(issue) >= 3

    def test_very_long_body_very_complex(self, solver):
        issue = Issue(number=2, title="Complex bug", body="x" * 6000, labels=[])
        assert solver._estimate_complexity(issue) >= 4

    def test_many_file_references(self, solver):
        issue = Issue(
            number=3,
            title="Fix stuff",
            body="Change src/a.py src/b.py src/c.py src/d.py src/e.py",
            labels=[],
        )
        assert solver._estimate_complexity(issue) >= 3

    def test_no_body_moderate(self, solver):
        issue = Issue(number=5, title="Fix something", body=None, labels=[])
        assert solver._estimate_complexity(issue) == 2

    def test_max_5(self, solver):
        issue = Issue(
            number=6,
            title="Refactor",
            body="x" * 10000 + " a.py b.py c.py d.py e.py",
            labels=[],
        )
        assert solver._estimate_complexity(issue) <= 5


class TestFilterSolvable:
    def test_filters_basic(self, solver, bug_issue, docs_issue):
        issues = [bug_issue, docs_issue]
        solvable = solver.filter_solvable(issues, max_complexity=3)
        assert len(solvable) == 2

    def test_filters_complex(self, solver):
        complex_issue = Issue(
            number=99,
            title="Redesign everything",
            body="x" * 10000 + " file1.py file2.py file3.py file4.py",
            labels=[],
        )
        solvable = solver.filter_solvable([complex_issue], max_complexity=2)
        assert len(solvable) == 0

    def test_filters_empty_list(self, solver):
        assert solver.filter_solvable([]) == []


class TestSolveIssue:
    @pytest.mark.asyncio
    async def test_solve_returns_finding(self, solver, bug_issue, sample_repo):
        solver._llm.complete = AsyncMock(
            return_value="""FILE_PATH: src/auth.py
SEVERITY: high
TITLE: Fix TypeError in login handler
DESCRIPTION: The login handler raises TypeError when user object is None
SUGGESTION: Add null check before accessing user properties"""
        )

        context = RepoContext(
            repo=sample_repo,
            file_tree=[FileNode(path="src/auth.py", type="blob", size=500, sha="x")],
        )
        finding = await solver.solve_issue(bug_issue, sample_repo, context)
        assert finding is not None
        assert finding.file_path == "src/auth.py"
        assert "login" in finding.title.lower() or "TypeError" in finding.title

    @pytest.mark.asyncio
    async def test_solve_handles_llm_failure(self, solver, bug_issue, sample_repo):
        solver._llm.complete = AsyncMock(side_effect=Exception("LLM down"))
        context = RepoContext(repo=sample_repo)
        result = await solver.solve_issue(bug_issue, sample_repo, context)
        assert result is None


class TestSolveIssueDeep:
    @pytest.mark.asyncio
    async def test_deep_solve_returns_multiple_findings(self, solver, bug_issue, sample_repo):
        solver._github.get_issue_comments = AsyncMock(return_value=[])
        solver._llm.complete = AsyncMock(
            return_value="""
---FILE---
PATH: src/auth.py
ACTION: modify
SEVERITY: high
TITLE: Fix login handler
DESCRIPTION: Add null check
SUGGESTION: if user is None: return error
---END---

---FILE---
PATH: tests/test_auth.py
ACTION: create
SEVERITY: medium
TITLE: Add login tests
DESCRIPTION: Create test for null user case
SUGGESTION: def test_login_none_user():
---END---
"""
        )
        context = RepoContext(
            repo=sample_repo,
            file_tree=[FileNode(path="src/auth.py", type="blob", size=500, sha="x")],
            relevant_files={"src/auth.py": "def login(user): return user.name"},
        )
        findings = await solver.solve_issue_deep(bug_issue, sample_repo, context)
        assert len(findings) == 2
        assert findings[0].file_path == "src/auth.py"
        assert findings[1].file_path == "tests/test_auth.py"

    @pytest.mark.asyncio
    async def test_deep_solve_falls_back_on_no_blocks(self, solver, bug_issue, sample_repo):
        """When LLM returns no ---FILE--- blocks, fall back to solve_issue."""
        solver._github.get_issue_comments = AsyncMock(return_value=[])
        solver._llm.complete = AsyncMock(
            return_value="""FILE_PATH: src/auth.py
SEVERITY: high
TITLE: Fix login
DESCRIPTION: Fix it
SUGGESTION: Fix the code"""
        )
        context = RepoContext(
            repo=sample_repo,
            file_tree=[FileNode(path="src/auth.py", type="blob", size=500, sha="x")],
        )
        findings = await solver.solve_issue_deep(bug_issue, sample_repo, context)
        assert len(findings) == 1
        assert findings[0].file_path == "src/auth.py"

    @pytest.mark.asyncio
    async def test_deep_solve_handles_failure(self, solver, bug_issue, sample_repo):
        solver._github.get_issue_comments = AsyncMock(side_effect=Exception("fail"))
        solver._llm.complete = AsyncMock(side_effect=Exception("LLM down"))
        context = RepoContext(repo=sample_repo)
        findings = await solver.solve_issue_deep(bug_issue, sample_repo, context)
        assert findings == []


class TestFetchSolvableIssues:
    @pytest.mark.asyncio
    async def test_fetches_and_filters(self, solver, sample_repo):
        solver._github.list_issues = AsyncMock(
            return_value=[
                {
                    "number": 1,
                    "title": "Easy fix",
                    "body": "Simple change",
                    "labels": [{"name": "good first issue"}],
                    "state": "open",
                    "html_url": "https://github.com/test/1",
                },
                {
                    "number": 2,
                    "title": "Another fix",
                    "body": "Another change",
                    "labels": [{"name": "bug"}],
                    "state": "open",
                    "html_url": "https://github.com/test/2",
                },
            ]
        )
        solver._github.get_issue_timeline = AsyncMock(return_value=[])
        issues = await solver.fetch_solvable_issues(sample_repo, max_issues=5)
        assert len(issues) >= 1

    @pytest.mark.asyncio
    async def test_fetches_deduplicates(self, solver, sample_repo):
        """Same issue appears in multiple label queries."""
        issue_data = {
            "number": 1,
            "title": "Easy fix",
            "body": "Simple",
            "labels": [{"name": "good first issue"}, {"name": "help wanted"}],
            "state": "open",
            "html_url": "https://github.com/test/1",
        }
        solver._github.list_issues = AsyncMock(return_value=[issue_data])
        solver._github.get_issue_timeline = AsyncMock(return_value=[])
        issues = await solver.fetch_solvable_issues(sample_repo)
        # Should only appear once despite matching multiple label groups
        assert sum(1 for i in issues if i.number == 1) <= 1

    @pytest.mark.asyncio
    async def test_skips_issues_with_linked_prs(self, solver, sample_repo):
        solver._github.list_issues = AsyncMock(
            return_value=[
                {
                    "number": 5,
                    "title": "Fix bug",
                    "body": "A bug",
                    "labels": [{"name": "bug"}],
                    "state": "open",
                    "html_url": "https://github.com/test/5",
                },
            ]
        )
        # Timeline indicates a cross-referenced PR
        solver._github.get_issue_timeline = AsyncMock(
            return_value=[
                {
                    "event": "cross-referenced",
                    "source": {
                        "type": "issue",
                        "issue": {"pull_request": {"url": "https://..."}},
                    },
                }
            ]
        )
        issues = await solver.fetch_solvable_issues(sample_repo)
        assert len(issues) == 0

    @pytest.mark.asyncio
    async def test_handles_api_errors(self, solver, sample_repo):
        solver._github.list_issues = AsyncMock(side_effect=Exception("API error"))
        issues = await solver.fetch_solvable_issues(sample_repo)
        assert issues == []


class TestHasLinkedPR:
    @pytest.mark.asyncio
    async def test_no_linked_pr(self, solver, sample_repo):
        solver._github.get_issue_timeline = AsyncMock(return_value=[])
        issue = Issue(number=1, title="Test", labels=[])
        result = await solver._has_linked_pr(sample_repo, issue)
        assert result is False

    @pytest.mark.asyncio
    async def test_has_linked_pr(self, solver, sample_repo):
        solver._github.get_issue_timeline = AsyncMock(
            return_value=[
                {
                    "event": "cross-referenced",
                    "source": {
                        "type": "issue",
                        "issue": {"pull_request": {"url": "https://..."}},
                    },
                }
            ]
        )
        issue = Issue(number=1, title="Test", labels=[])
        result = await solver._has_linked_pr(sample_repo, issue)
        assert result is True

    @pytest.mark.asyncio
    async def test_timeline_error(self, solver, sample_repo):
        solver._github.get_issue_timeline = AsyncMock(side_effect=Exception("fail"))
        issue = Issue(number=1, title="Test", labels=[])
        result = await solver._has_linked_pr(sample_repo, issue)
        assert result is False


class TestBuildIssueContext:
    @pytest.mark.asyncio
    async def test_includes_comments(self, solver, sample_repo):
        solver._github.get_issue_comments = AsyncMock(
            return_value=[
                {"user": {"login": "dev1"}, "body": "I can reproduce this bug"},
                {"user": {"login": "dev2"}, "body": "Same issue here, stack trace:..."},
            ]
        )
        issue = Issue(number=1, title="Bug", body="Main description", labels=[])
        context = await solver._build_issue_context(issue, sample_repo)
        assert "Main description" in context
        assert "dev1" in context
        assert "reproduce" in context

    @pytest.mark.asyncio
    async def test_handles_comment_error(self, solver, sample_repo):
        solver._github.get_issue_comments = AsyncMock(side_effect=Exception("fail"))
        issue = Issue(number=1, title="Bug", body="Description", labels=[])
        context = await solver._build_issue_context(issue, sample_repo)
        assert "Description" in context

    @pytest.mark.asyncio
    async def test_no_body(self, solver, sample_repo):
        solver._github.get_issue_comments = AsyncMock(return_value=[])
        issue = Issue(number=1, title="Bug", body=None, labels=[])
        context = await solver._build_issue_context(issue, sample_repo)
        assert "No description" in context


class TestBuildFileTreeSummary:
    def test_groups_by_directory(self, solver, sample_repo):
        context = RepoContext(
            repo=sample_repo,
            file_tree=[
                FileNode(path="src/main.py", type="blob", size=100, sha="a"),
                FileNode(path="src/utils.py", type="blob", size=100, sha="b"),
                FileNode(path="tests/test_main.py", type="blob", size=100, sha="c"),
                FileNode(path="README.md", type="blob", size=100, sha="d"),
            ],
        )
        summary = solver._build_file_tree_summary(context)
        assert "src/" in summary
        assert "tests/" in summary

    def test_skips_tree_nodes(self, solver, sample_repo):
        context = RepoContext(
            repo=sample_repo,
            file_tree=[
                FileNode(path="src", type="tree", size=0, sha="a"),
                FileNode(path="src/main.py", type="blob", size=100, sha="b"),
            ],
        )
        summary = solver._build_file_tree_summary(context)
        assert "main.py" in summary


class TestParseMultiFileResponse:
    def test_parses_multiple_blocks(self, solver):
        response = """
---FILE---
PATH: src/auth.py
ACTION: modify
SEVERITY: high
TITLE: Fix login
DESCRIPTION: Add null check
SUGGESTION: if user is None: return
---END---

---FILE---
PATH: src/utils.py
ACTION: modify
SEVERITY: low
TITLE: Add helper
DESCRIPTION: New utility function
SUGGESTION: def helper(): pass
---END---
"""
        issue = Issue(number=1, title="Fix bug", labels=["bug"])
        findings = solver._parse_multi_file_response(response, issue, ContributionType.CODE_QUALITY)
        assert len(findings) == 2
        assert findings[0].file_path == "src/auth.py"
        assert findings[1].file_path == "src/utils.py"

    def test_skips_invalid_blocks(self, solver):
        response = """
---FILE---
PATH: src/auth.py
ACTION: modify
SEVERITY: high
TITLE: Fix login
DESCRIPTION: Fix it
SUGGESTION: Fix
---END---

---FILE---
PATH: unknown
---END---
"""
        issue = Issue(number=1, title="Fix", labels=[])
        findings = solver._parse_multi_file_response(response, issue, ContributionType.CODE_QUALITY)
        assert len(findings) == 1

    def test_max_5_files(self, solver):
        blocks = ""
        for i in range(8):
            blocks += f"""
---FILE---
PATH: src/file{i}.py
ACTION: modify
SEVERITY: low
TITLE: Change {i}
DESCRIPTION: Change file {i}
SUGGESTION: Update
---END---
"""
        issue = Issue(number=1, title="Big change", labels=[])
        findings = solver._parse_multi_file_response(blocks, issue, ContributionType.CODE_QUALITY)
        assert len(findings) == 5

    def test_empty_response(self, solver):
        issue = Issue(number=1, title="Test", labels=[])
        findings = solver._parse_multi_file_response("", issue, ContributionType.CODE_QUALITY)
        assert findings == []

    def test_no_end_marker(self, solver):
        response = """
---FILE---
PATH: src/auth.py
TITLE: Fix
DESCRIPTION: Fix it
"""
        issue = Issue(number=1, title="Test", labels=[])
        findings = solver._parse_multi_file_response(response, issue, ContributionType.CODE_QUALITY)
        assert findings == []
