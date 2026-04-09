"""Tests for v2.0.0 pipeline issue-driven mode."""

import pytest

from contribai.core.models import FileNode, Repository


@pytest.fixture
def sample_pipeline(sample_config):
    """Create a pipeline instance for testing."""
    from contribai.orchestrator.pipeline import ContribPipeline

    return ContribPipeline(sample_config)


class TestIdentifyKeyFiles:
    def test_finds_readme_and_config(self, sample_pipeline, sample_repo):
        file_tree = [
            FileNode(path="README.md", type="blob", size=100, sha="a"),
            FileNode(path="setup.py", type="blob", size=100, sha="b"),
            FileNode(path="src/main.py", type="blob", size=100, sha="c"),
            FileNode(path="tests/test_main.py", type="blob", size=100, sha="d"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, sample_repo)
        assert "README.md" in keys
        assert "setup.py" in keys

    def test_finds_python_entry_points(self, sample_pipeline):
        repo = Repository(
            owner="a",
            name="b",
            full_name="a/b",
            language="python",
            default_branch="main",
        )
        file_tree = [
            FileNode(path="myapp/__init__.py", type="blob", size=100, sha="a"),
            FileNode(path="myapp/main.py", type="blob", size=200, sha="b"),
            FileNode(path="myapp/cli.py", type="blob", size=150, sha="c"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, repo)
        assert any("__init__.py" in k for k in keys)

    def test_finds_javascript_entry_points(self, sample_pipeline):
        repo = Repository(
            owner="a",
            name="b",
            full_name="a/b",
            language="JavaScript",
            default_branch="main",
        )
        file_tree = [
            FileNode(path="package.json", type="blob", size=100, sha="a"),
            FileNode(path="src/index.js", type="blob", size=200, sha="b"),
            FileNode(path="src/app.js", type="blob", size=150, sha="c"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, repo)
        assert "package.json" in keys

    def test_finds_src_dir_files(self, sample_pipeline, sample_repo):
        file_tree = [
            FileNode(path="src/module_a.py", type="blob", size=100, sha="a"),
            FileNode(path="src/module_b.py", type="blob", size=100, sha="b"),
            FileNode(path="lib/helper.py", type="blob", size=100, sha="c"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, sample_repo)
        assert "src/module_a.py" in keys or "src/module_b.py" in keys

    def test_max_15_files(self, sample_pipeline, sample_repo):
        file_tree = [
            FileNode(path=f"src/file_{i}.py", type="blob", size=100, sha=str(i)) for i in range(30)
        ]
        keys = sample_pipeline._identify_key_files(file_tree, sample_repo)
        assert len(keys) <= 15

    def test_skips_tree_nodes(self, sample_pipeline, sample_repo):
        file_tree = [
            FileNode(path="src", type="tree", size=0, sha="a"),
            FileNode(path="src/main.py", type="blob", size=100, sha="b"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, sample_repo)
        assert "src" not in keys

    def test_contributing_md(self, sample_pipeline, sample_repo):
        file_tree = [
            FileNode(path="CONTRIBUTING.md", type="blob", size=100, sha="a"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, sample_repo)
        assert "CONTRIBUTING.md" in keys

    def test_finds_go_files(self, sample_pipeline):
        repo = Repository(
            owner="a",
            name="b",
            full_name="a/b",
            language="Go",
            default_branch="main",
        )
        file_tree = [
            FileNode(path="go.mod", type="blob", size=100, sha="a"),
            FileNode(path="cmd/main.go", type="blob", size=200, sha="b"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, repo)
        assert "go.mod" in keys

    def test_finds_rust_files(self, sample_pipeline):
        repo = Repository(
            owner="a",
            name="b",
            full_name="a/b",
            language="Rust",
            default_branch="main",
        )
        file_tree = [
            FileNode(path="Cargo.toml", type="blob", size=100, sha="a"),
            FileNode(path="src/main.rs", type="blob", size=200, sha="b"),
            FileNode(path="src/lib.rs", type="blob", size=150, sha="c"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, repo)
        assert "Cargo.toml" in keys

    def test_unknown_language(self, sample_pipeline):
        repo = Repository(
            owner="a",
            name="b",
            full_name="a/b",
            language="Brainfuck",
            default_branch="main",
        )
        file_tree = [
            FileNode(path="README.md", type="blob", size=100, sha="a"),
        ]
        keys = sample_pipeline._identify_key_files(file_tree, repo)
        assert "README.md" in keys


class TestPipelineHuntMode:
    def test_hunt_has_mode_param(self, sample_pipeline):
        import inspect

        sig = inspect.signature(sample_pipeline.hunt)
        assert "mode" in sig.parameters
        assert sig.parameters["mode"].default == "both"


class TestPipelineResult:
    def test_pipeline_result_defaults(self):
        from contribai.orchestrator.pipeline import PipelineResult

        result = PipelineResult()
        assert result.repos_analyzed == 0
        assert result.findings_total == 0
        assert result.contributions_generated == 0
        assert result.prs_created == 0
        assert result.prs == []
        assert result.errors == []


class TestTitlesSimilar:
    def test_similar_titles(self):
        from contribai.orchestrator.pipeline import _titles_similar

        assert _titles_similar(
            "Fix null pointer in login handler",
            "Fix null pointer exception in login handler",
        )

    def test_different_titles(self):
        from contribai.orchestrator.pipeline import _titles_similar

        assert not _titles_similar(
            "Update README documentation",
            "Fix performance bottleneck in database",
        )

    def test_empty_titles(self):
        from contribai.orchestrator.pipeline import _titles_similar

        assert not _titles_similar("", "")

    def test_short_words_ignored(self):
        from contribai.orchestrator.pipeline import _titles_similar

        assert not _titles_similar("a the in", "b or on")
