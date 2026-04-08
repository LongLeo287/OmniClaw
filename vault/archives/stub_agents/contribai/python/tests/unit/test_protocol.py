"""Tests for contribai.tools.protocol — MCP-inspired tool protocol."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from contribai.tools.protocol import (
    GitHubTool,
    LLMTool,
    ToolRegistry,
    ToolResult,
    create_default_tools,
)


class TestToolResult:
    """Tests for ToolResult dataclass."""

    def test_success(self):
        result = ToolResult(success=True, data="hello")
        assert result.success is True
        assert result.data == "hello"
        assert result.error is None

    def test_failure(self):
        result = ToolResult(success=False, error="not found")
        assert result.success is False
        assert result.error == "not found"

    def test_metadata(self):
        result = ToolResult(success=True, metadata={"key": "val"})
        assert result.metadata["key"] == "val"


class TestToolRegistry:
    """Tests for ToolRegistry."""

    @pytest.fixture
    def registry(self):
        return ToolRegistry()

    def test_empty_registry(self, registry):
        assert registry.list_tools() == []
        assert registry.has("anything") is False

    def test_register_and_list(self, registry):
        tool = MagicMock()
        tool.name = "test_tool"
        tool.description = "A test tool"
        registry.register(tool)
        tools = registry.list_tools()
        assert len(tools) == 1
        assert tools[0]["name"] == "test_tool"
        assert tools[0]["description"] == "A test tool"

    def test_get(self, registry):
        tool = MagicMock()
        tool.name = "my_tool"
        registry.register(tool)
        assert registry.get("my_tool") is tool
        assert registry.get("nonexistent") is None

    def test_has(self, registry):
        tool = MagicMock()
        tool.name = "check"
        registry.register(tool)
        assert registry.has("check") is True
        assert registry.has("nope") is False

    @pytest.mark.asyncio
    async def test_execute_missing(self, registry):
        result = await registry.execute("nonexistent")
        assert result.success is False
        assert "not found" in result.error

    @pytest.mark.asyncio
    async def test_execute_success(self, registry):
        tool = MagicMock()
        tool.name = "ok_tool"
        tool.execute = AsyncMock(return_value=ToolResult(success=True, data="done"))
        registry.register(tool)
        result = await registry.execute("ok_tool")
        assert result.success is True
        assert result.data == "done"

    @pytest.mark.asyncio
    async def test_execute_error(self, registry):
        tool = MagicMock()
        tool.name = "err_tool"
        tool.execute = AsyncMock(side_effect=RuntimeError("boom"))
        registry.register(tool)
        result = await registry.execute("err_tool")
        assert result.success is False
        assert "boom" in result.error


class TestGitHubTool:
    """Tests for GitHubTool wrapper."""

    def test_name_and_description(self):
        tool = GitHubTool(MagicMock())
        assert tool.name == "github"
        assert "GitHub" in tool.description

    @pytest.mark.asyncio
    async def test_unknown_action(self):
        tool = GitHubTool(MagicMock())
        result = await tool.execute(action="unknown_action")
        assert result.success is False
        assert "Unknown action" in result.error

    @pytest.mark.asyncio
    async def test_get_file(self):
        client = MagicMock()
        client.get_file_content = AsyncMock(return_value="file content")
        tool = GitHubTool(client)
        result = await tool.execute(action="get_file", owner="o", repo="r", path="p")
        assert result.success is True
        assert result.data == "file content"

    @pytest.mark.asyncio
    async def test_get_user(self):
        client = MagicMock()
        client.get_authenticated_user = AsyncMock(return_value={"login": "user"})
        tool = GitHubTool(client)
        result = await tool.execute(action="get_user")
        assert result.success is True
        assert result.data["login"] == "user"

    @pytest.mark.asyncio
    async def test_error_handling(self):
        client = MagicMock()
        client.get_file_content = AsyncMock(side_effect=Exception("API error"))
        tool = GitHubTool(client)
        result = await tool.execute(action="get_file", owner="o", repo="r", path="p")
        assert result.success is False
        assert "API error" in result.error


class TestLLMTool:
    """Tests for LLMTool wrapper."""

    def test_name_and_description(self):
        tool = LLMTool(MagicMock())
        assert tool.name == "llm"
        assert "LLM" in tool.description

    @pytest.mark.asyncio
    async def test_complete(self):
        provider = MagicMock()
        provider.complete = AsyncMock(return_value="LLM response")
        tool = LLMTool(provider)
        result = await tool.execute(prompt="Hello", system="Be helpful")
        assert result.success is True
        assert result.data == "LLM response"

    @pytest.mark.asyncio
    async def test_error_handling(self):
        provider = MagicMock()
        provider.complete = AsyncMock(side_effect=Exception("rate limited"))
        tool = LLMTool(provider)
        result = await tool.execute(prompt="Hello")
        assert result.success is False
        assert "rate limited" in result.error


class TestCreateDefaultTools:
    """Tests for create_default_tools factory."""

    def test_empty(self):
        registry = create_default_tools()
        assert isinstance(registry, ToolRegistry)
        assert registry.list_tools() == []

    def test_with_github(self):
        registry = create_default_tools(github_client=MagicMock())
        assert registry.has("github") is True
        assert registry.has("llm") is False

    def test_with_both(self):
        registry = create_default_tools(
            github_client=MagicMock(),
            llm_provider=MagicMock(),
        )
        assert registry.has("github") is True
        assert registry.has("llm") is True
        assert len(registry.list_tools()) == 2
