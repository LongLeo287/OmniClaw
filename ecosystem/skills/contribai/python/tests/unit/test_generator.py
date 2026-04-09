"""Tests for the contribution generator."""

from unittest.mock import AsyncMock

import pytest

from contribai.core.config import ContributionConfig
from contribai.core.models import (
    Contribution,
    ContributionType,
    FileChange,
    Finding,
    RepoContext,
    Severity,
)
from contribai.generator.engine import ContributionGenerator


@pytest.fixture
def generator(mock_llm):
    config = ContributionConfig(max_files_per_pr=5)
    return ContributionGenerator(llm=mock_llm, config=config)


@pytest.fixture
def security_finding():
    return Finding(
        id="sec001",
        type=ContributionType.SECURITY_FIX,
        severity=Severity.HIGH,
        title="Hardcoded API key",
        description="API key is hardcoded in source",
        file_path="src/config.py",
        line_start=42,
        suggestion="Use environment variables",
    )


@pytest.fixture
def context(sample_repo):
    return RepoContext(
        repo=sample_repo,
        relevant_files={"src/config.py": "API_KEY = 'sk-1234'\n"},
    )


class TestGenerateBranchName:
    def test_security_fix_branch(self, generator, security_finding):
        name = generator._generate_branch_name(security_finding)
        assert name.startswith("contribai/fix/security/")
        assert "hardcoded" in name

    def test_docs_branch(self, generator):
        finding = Finding(
            type=ContributionType.DOCS_IMPROVE,
            severity=Severity.LOW,
            title="Missing README section",
            description="",
            file_path="README.md",
        )
        name = generator._generate_branch_name(finding)
        assert name.startswith("contribai/docs/")

    def test_branch_name_sanitized(self, generator):
        finding = Finding(
            type=ContributionType.FEATURE_ADD,
            severity=Severity.MEDIUM,
            title="Add feature: special chars! @#$ here",
            description="",
            file_path="x.py",
        )
        name = generator._generate_branch_name(finding)
        assert "@" not in name
        assert "!" not in name
        assert "$" not in name


class TestGeneratePRTitle:
    def test_security_title(self, generator, security_finding):
        title = generator._generate_pr_title(security_finding)
        assert "Security:" in title
        assert "Hardcoded API key" in title

    def test_docs_title(self, generator):
        finding = Finding(
            type=ContributionType.DOCS_IMPROVE,
            severity=Severity.LOW,
            title="Add API docs",
            description="",
            file_path="docs/api.md",
        )
        title = generator._generate_pr_title(finding)
        assert "Docs:" in title


class TestParseChanges:
    @pytest.fixture
    def mock_context(self, sample_repo):
        return RepoContext(
            repo=sample_repo,
            relevant_files={"src/config.py": "API_KEY = 'sk-1234'\n"},
        )

    def test_parse_json_response(self, generator, mock_context):
        response = """Here is the fix:
```json
{
  "changes": [
    {
      "path": "src/config.py",
      "content": "import os\\nAPI_KEY = os.getenv('API_KEY')",
      "is_new_file": false
    }
  ]
}
```"""
        changes = generator._parse_changes(response, mock_context)
        assert len(changes) == 1
        assert changes[0].path == "src/config.py"
        assert not changes[0].is_new_file

    def test_parse_new_file(self, generator, mock_context):
        response = """```json
{"changes": [{"path": "new_file.py", "content": "print('hello')", "is_new_file": true}]}
```"""
        changes = generator._parse_changes(response, mock_context)
        assert len(changes) == 1
        assert changes[0].is_new_file is True

    def test_parse_invalid_json(self, generator, mock_context):
        response = "This is not JSON at all"
        changes = generator._parse_changes(response, mock_context)
        assert len(changes) == 0

    def test_enforces_max_files(self, generator, mock_context):
        many_changes = [
            {"path": f"file{i}.py", "content": "x", "is_new_file": True} for i in range(20)
        ]
        response = f'{{"changes": {many_changes}}}'.replace("'", '"')
        changes = generator._parse_changes(response, mock_context)
        assert len(changes) <= generator._config.max_files_per_pr

    def test_parse_search_replace(self, generator, mock_context):
        """Test search/replace mode preserves original content."""
        response = """```json
{
  "changes": [
    {
      "path": "src/config.py",
      "is_new_file": false,
      "edits": [
        {
          "search": "API_KEY = 'sk-1234'",
          "replace": "API_KEY = os.getenv('API_KEY', '')"
        }
      ]
    }
  ]
}
```"""
        changes = generator._parse_changes(response, mock_context)
        assert len(changes) == 1
        assert "os.getenv" in changes[0].new_content
        assert not changes[0].is_new_file


class TestSelfReview:
    @pytest.mark.asyncio
    async def test_approve(self, generator, security_finding, context):
        generator._llm.complete = AsyncMock(return_value="APPROVE - looks good")
        contribution = Contribution(
            finding=security_finding,
            contribution_type=ContributionType.SECURITY_FIX,
            title="Fix security issue",
            description="Fixed it",
            changes=[FileChange(path="x.py", new_content="safe code")],
        )
        assert await generator._self_review(contribution, context) is True

    @pytest.mark.asyncio
    async def test_reject(self, generator, security_finding, context):
        generator._llm.complete = AsyncMock(return_value="REJECT - introduces new bug")
        contribution = Contribution(
            finding=security_finding,
            contribution_type=ContributionType.SECURITY_FIX,
            title="Bad fix",
            description="Bad",
            changes=[FileChange(path="x.py", new_content="buggy code")],
        )
        assert await generator._self_review(contribution, context) is False

    @pytest.mark.asyncio
    async def test_llm_failure_approves_by_default(self, generator, security_finding, context):
        generator._llm.complete = AsyncMock(side_effect=Exception("LLM down"))
        contribution = Contribution(
            finding=security_finding,
            contribution_type=ContributionType.SECURITY_FIX,
            title="Fix",
            description="",
            changes=[FileChange(path="x.py", new_content="code")],
        )
        # Should approve by default when LLM fails
        assert await generator._self_review(contribution, context) is True
