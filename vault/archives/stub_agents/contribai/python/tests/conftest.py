"""Shared test fixtures and mocks for ContribAI."""

from __future__ import annotations

from unittest.mock import AsyncMock

import pytest

from contribai.core.config import (
    AnalysisConfig,
    ContribAIConfig,
    ContributionConfig,
    DiscoveryConfig,
    GitHubConfig,
    LLMConfig,
    StorageConfig,
)
from contribai.core.models import (
    ContributionType,
    FileNode,
    Finding,
    Repository,
    Severity,
)

# ── Config Fixtures ────────────────────────────────────────────────────────


@pytest.fixture
def sample_config(tmp_path):
    """Full config with tmp path for DB."""
    return ContribAIConfig(
        github=GitHubConfig(token="ghp_test_token_12345"),
        llm=LLMConfig(provider="gemini", model="gemini-2.5-flash", api_key="test_key"),
        analysis=AnalysisConfig(),
        contribution=ContributionConfig(),
        discovery=DiscoveryConfig(languages=["python"]),
        storage=StorageConfig(db_path=str(tmp_path / "test.db")),
    )


# ── Model Fixtures ────────────────────────────────────────────────────────


@pytest.fixture
def sample_repo():
    """A sample repository model."""
    return Repository(
        owner="testowner",
        name="testrepo",
        full_name="testowner/testrepo",
        description="A test repository for unit testing",
        language="python",
        stars=500,
        forks=50,
        open_issues=10,
        topics=["python", "testing"],
        default_branch="main",
        html_url="https://github.com/testowner/testrepo",
        clone_url="https://github.com/testowner/testrepo.git",
        has_license=True,
    )


@pytest.fixture
def sample_finding():
    """A sample finding."""
    return Finding(
        id="test001",
        type=ContributionType.SECURITY_FIX,
        severity=Severity.HIGH,
        title="Hardcoded API key in config.py",
        description="An API key is hardcoded in the source code at line 42.",
        file_path="src/config.py",
        line_start=42,
        suggestion="Use environment variables instead of hardcoded keys.",
        confidence=0.9,
    )


@pytest.fixture
def sample_file_tree():
    """A sample file tree."""
    return [
        FileNode(path="README.md", type="blob", size=1024, sha="abc"),
        FileNode(path="src", type="tree", size=0, sha="def"),
        FileNode(path="src/main.py", type="blob", size=2048, sha="ghi"),
        FileNode(path="src/config.py", type="blob", size=512, sha="jkl"),
        FileNode(path="tests", type="tree", size=0, sha="mno"),
        FileNode(path="tests/test_main.py", type="blob", size=768, sha="pqr"),
    ]


# ── Mock Fixtures ──────────────────────────────────────────────────────────


@pytest.fixture
def mock_llm():
    """Mock LLM provider."""
    llm = AsyncMock()
    llm.complete = AsyncMock(return_value="APPROVE\nLooks good.")
    llm.chat = AsyncMock(return_value="OK")
    llm.close = AsyncMock()
    return llm


@pytest.fixture
def mock_github():
    """Mock GitHub client."""
    client = AsyncMock()
    client.search_repositories = AsyncMock(return_value=[])
    client.get_repo_details = AsyncMock()
    client.get_file_tree = AsyncMock(return_value=[])
    client.get_file_content = AsyncMock(return_value="# Sample content")
    client.get_open_issues = AsyncMock(return_value=[])
    client.get_contributing_guide = AsyncMock(return_value=None)
    client.fork_repository = AsyncMock()
    client.create_branch = AsyncMock()
    client.create_or_update_file = AsyncMock()
    client.create_pull_request = AsyncMock(
        return_value={"number": 1, "html_url": "https://github.com/test/pr/1"}
    )
    client.get_authenticated_user = AsyncMock(return_value={"login": "testuser"})
    client.check_rate_limit = AsyncMock(
        return_value={"remaining": 4999, "limit": 5000, "reset": 9999999}
    )
    client.list_issues = AsyncMock(return_value=[])
    client.get_issue_comments = AsyncMock(return_value=[])
    client.get_issue_timeline = AsyncMock(return_value=[])
    client.list_pull_requests = AsyncMock(return_value=[])
    client.close = AsyncMock()
    return client


@pytest.fixture
async def memory(tmp_path):
    """In-memory SQLite Memory instance for tests."""
    from contribai.orchestrator.memory import Memory

    mem = Memory(tmp_path / "test_memory.db")
    await mem.init()
    yield mem
    await mem.close()
