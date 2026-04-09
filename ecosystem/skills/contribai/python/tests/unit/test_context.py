"""Tests for LLM context management."""

from contribai.core.models import FileNode, RepoContext
from contribai.llm.context import (
    ContextBudget,
    build_repo_context_prompt,
    estimate_tokens,
    format_file_tree,
    truncate_to_tokens,
)


class TestEstimateTokens:
    def test_empty_string(self):
        assert estimate_tokens("") == 0

    def test_short_string(self):
        assert estimate_tokens("hello") == 1  # 5 chars / 4

    def test_long_string(self):
        text = "x" * 400
        assert estimate_tokens(text) == 100


class TestTruncateToTokens:
    def test_no_truncation_needed(self):
        text = "short text"
        assert truncate_to_tokens(text, 100) == text

    def test_truncation_applied(self):
        text = "x" * 1000
        result = truncate_to_tokens(text, 10)
        assert len(result) < len(text)
        assert "[truncated]" in result


class TestContextBudget:
    def test_remaining(self):
        budget = ContextBudget(max_tokens=100)
        assert budget.remaining == 100

    def test_add_reduces_remaining(self):
        budget = ContextBudget(max_tokens=100)
        budget.add("section1", "x" * 80)  # ~20 tokens
        assert budget.remaining < 100

    def test_can_fit(self):
        budget = ContextBudget(max_tokens=100)
        assert budget.can_fit("x" * 100)  # 25 tokens, fits in 100
        budget.used_tokens = 90
        assert not budget.can_fit("x" * 100)


class TestFormatFileTree:
    def test_formats_tree(self):
        nodes = [
            FileNode(path="README.md", type="blob", size=100, sha="a"),
            FileNode(path="src/main.py", type="blob", size=200, sha="b"),
            FileNode(path="src", type="tree", size=0, sha="c"),
        ]
        result = format_file_tree(nodes)
        assert "📁" in result  # directories
        assert "📄" in result  # files

    def test_respects_max_depth(self):
        nodes = [
            FileNode(path="a/b/c/d/e/deep.py", type="blob", size=100, sha="x"),
        ]
        result = format_file_tree(nodes, max_depth=2)
        assert "deep.py" not in result


class TestBuildRepoContextPrompt:
    def test_includes_metadata(self, sample_repo):
        ctx = RepoContext(repo=sample_repo)
        prompt = build_repo_context_prompt(ctx)
        assert sample_repo.full_name in prompt
        assert sample_repo.language in prompt

    def test_includes_readme(self, sample_repo):
        ctx = RepoContext(repo=sample_repo, readme_content="# Hello World")
        prompt = build_repo_context_prompt(ctx)
        assert "Hello World" in prompt

    def test_respects_token_budget(self, sample_repo):
        long_readme = "x" * 100_000
        ctx = RepoContext(repo=sample_repo, readme_content=long_readme)
        prompt = build_repo_context_prompt(ctx, max_tokens=500)
        assert len(prompt) < 100_000
