"""Tests for P2: Working Memory and P4: Sandbox."""

from __future__ import annotations

import pytest

from contribai.sandbox.sandbox import Sandbox, SandboxResult


class TestWorkingMemory:
    """Tests for working memory methods on Memory class."""

    @pytest.mark.asyncio
    async def test_store_and_get_context(self, memory):
        await memory.store_context("owner/repo", "style_guide", "use snake_case", language="python")
        result = await memory.get_context("owner/repo", "style_guide")
        assert result == "use snake_case"

    @pytest.mark.asyncio
    async def test_get_context_missing(self, memory):
        result = await memory.get_context("nonexist/repo", "key")
        assert result is None

    @pytest.mark.asyncio
    async def test_get_similar_context(self, memory):
        await memory.store_context("a/repo", "patterns", "factory pattern", language="python")
        await memory.store_context("b/repo", "patterns", "observer pattern", language="python")
        await memory.store_context("c/repo", "patterns", "module pattern", language="javascript")

        results = await memory.get_similar_context("python", "patterns")
        assert len(results) == 2
        repos = {r["repo"] for r in results}
        assert "a/repo" in repos
        assert "b/repo" in repos

    @pytest.mark.asyncio
    async def test_archive_expired(self, memory):
        # Store with 0 TTL (already expired)
        await memory.store_context("x/repo", "temp", "data", ttl_hours=0)
        deleted = await memory.archive_expired()
        assert deleted >= 1

    @pytest.mark.asyncio
    async def test_store_overwrites(self, memory):
        await memory.store_context("owner/repo", "key", "v1")
        await memory.store_context("owner/repo", "key", "v2")
        result = await memory.get_context("owner/repo", "key")
        assert result == "v2"


class TestSandbox:
    """Tests for sandbox execution."""

    def test_sandbox_disabled(self):
        sandbox = Sandbox(enabled=False)
        assert not sandbox.enabled

    @pytest.mark.asyncio
    async def test_validate_disabled_returns_success(self):
        sandbox = Sandbox(enabled=False)
        result = await sandbox.validate("print('hello')", "python")
        assert result.success is True
        assert "disabled" in result.output.lower()

    @pytest.mark.asyncio
    async def test_validate_python_local_valid(self):
        sandbox = Sandbox(enabled=True)
        # Force local validation (no Docker)
        result = await sandbox._validate_local("x = 1 + 2\nprint(x)", "python")
        assert result.success is True

    @pytest.mark.asyncio
    async def test_validate_python_local_syntax_error(self):
        sandbox = Sandbox(enabled=True)
        result = await sandbox._validate_local("def foo(\n", "python")
        assert result.success is False
        assert "SyntaxError" in result.errors

    @pytest.mark.asyncio
    async def test_validate_unknown_language_local(self):
        sandbox = Sandbox(enabled=True)
        result = await sandbox._validate_local("some code", "ruby")
        assert result.success is True  # no validator, returns success

    def test_sandbox_result_defaults(self):
        result = SandboxResult()
        assert result.success is False
        assert result.output == ""
        assert result.errors == ""

    def test_get_extension(self):
        assert Sandbox._get_extension("python") == ".py"
        assert Sandbox._get_extension("javascript") == ".js"
        assert Sandbox._get_extension("unknown") == ".txt"
