"""Integration test: full pipeline dry run with mocked externals."""

from unittest.mock import AsyncMock, patch

import pytest

from contribai.core.config import ContribAIConfig, GitHubConfig, LLMConfig, StorageConfig
from contribai.core.models import (
    AnalysisResult,
    Contribution,
    ContributionType,
    FileChange,
    FileNode,
    Finding,
    PRResult,
    Repository,
    Severity,
)


@pytest.fixture
def pipeline_config(tmp_path):
    return ContribAIConfig(
        github=GitHubConfig(token="ghp_test", max_repos_per_run=1, max_prs_per_day=5),
        llm=LLMConfig(provider="gemini", api_key="test_key"),
        storage=StorageConfig(db_path=str(tmp_path / "test.db")),
    )


@pytest.fixture
def mock_repo():
    return Repository(
        owner="testorg",
        name="testrepo",
        full_name="testorg/testrepo",
        description="Test repo for integration",
        language="python",
        stars=500,
        forks=50,
        open_issues=10,
        default_branch="main",
        has_license=True,
    )


@pytest.fixture
def sample_finding():
    return Finding(
        type=ContributionType.CODE_QUALITY,
        severity=Severity.MEDIUM,
        title="Dead code detected",
        description="Unused import on line 5",
        file_path="main.py",
    )


@pytest.fixture
def sample_contribution(sample_finding):
    return Contribution(
        finding=sample_finding,
        contribution_type=ContributionType.CODE_QUALITY,
        title="Remove dead code",
        description="Removed unused import",
        changes=[FileChange(path="main.py", new_content="# clean code")],
        commit_message="fix: remove unused import",
        branch_name="contribai/fix/dead-code",
    )


class TestPipelineDryRun:
    @pytest.mark.asyncio
    async def test_dry_run_skips_pr_creation(
        self, pipeline_config, mock_repo, sample_finding, sample_contribution
    ):
        """Dry run should analyze and generate but NOT create PRs."""
        from contribai.orchestrator.pipeline import ContribPipeline

        pipeline = ContribPipeline(pipeline_config)

        # Pre-assign all mocked components so _init_components is skipped
        pipeline._github = AsyncMock()
        pipeline._github.close = AsyncMock()

        pipeline._llm = AsyncMock()
        pipeline._llm.close = AsyncMock()

        pipeline._discovery = AsyncMock()
        pipeline._discovery.discover = AsyncMock(return_value=[mock_repo])

        pipeline._analyzer = AsyncMock()
        pipeline._analyzer.analyze = AsyncMock(
            return_value=AnalysisResult(
                repo=mock_repo,
                findings=[sample_finding],
                analyzed_files=1,
                analysis_duration_sec=0.5,
            )
        )

        pipeline._generator = AsyncMock()
        pipeline._generator.generate = AsyncMock(return_value=sample_contribution)

        pipeline._pr_manager = AsyncMock()
        pipeline._pr_manager.create_pr = AsyncMock(
            return_value=PRResult(
                repo=mock_repo,
                contribution=sample_contribution,
                pr_number=42,
                pr_url="https://github.com/test/pr/42",
            )
        )

        # Use real Memory with tmp_path
        from contribai.orchestrator.memory import Memory

        pipeline._memory = Memory(pipeline_config.storage.resolved_db_path)
        await pipeline._memory.init()

        pipeline._github.get_file_tree = AsyncMock(
            return_value=[
                FileNode(path="main.py", type="blob", size=500, sha="abc"),
            ]
        )
        pipeline._github.get_file_content = AsyncMock(return_value="import unused\nprint('hello')")

        # Patch _init_components to be a no-op (components already set)
        with patch.object(pipeline, "_init_components", new=AsyncMock()):
            result = await pipeline.run(dry_run=True)

        # In dry run, PR should NOT be created
        pipeline._pr_manager.create_pr.assert_not_called()
        assert result.repos_analyzed >= 0

        await pipeline._memory.close()

    @pytest.mark.asyncio
    async def test_analyze_only_mode(self, pipeline_config, mock_repo):
        """Analyze-only should return analysis without generating contributions."""
        from contribai.orchestrator.pipeline import ContribPipeline

        pipeline = ContribPipeline(pipeline_config)

        pipeline._github = AsyncMock()
        pipeline._github.get_repo_details = AsyncMock(return_value=mock_repo)
        pipeline._github.close = AsyncMock()

        pipeline._llm = AsyncMock()
        pipeline._llm.close = AsyncMock()

        finding = Finding(
            type=ContributionType.SECURITY_FIX,
            severity=Severity.HIGH,
            title="SQL injection",
            description="Parameterize queries",
            file_path="main.py",
        )

        pipeline._analyzer = AsyncMock()
        pipeline._analyzer.analyze = AsyncMock(
            return_value=AnalysisResult(
                repo=mock_repo,
                findings=[finding],
            )
        )

        from contribai.orchestrator.memory import Memory

        pipeline._memory = Memory(pipeline_config.storage.resolved_db_path)
        await pipeline._memory.init()

        with patch.object(pipeline, "_init_components", new=AsyncMock()):
            result = await pipeline.analyze_only("https://github.com/testorg/testrepo")

        assert result is not None
        assert len(result.findings) == 1
        assert result.findings[0].title == "SQL injection"

        await pipeline._memory.close()
