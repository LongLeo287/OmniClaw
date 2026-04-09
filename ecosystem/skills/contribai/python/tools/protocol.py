"""Tool protocol and registry for extensible tool support.

Inspired by DeerFlow's MCP tool ecosystem: tools follow a common protocol
and can be swapped, extended, or composed via a registry.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass
from typing import Any, Protocol

logger = logging.getLogger(__name__)


@dataclass
class ToolResult:
    """Result from a tool execution."""

    success: bool
    data: Any = None
    error: str | None = None
    metadata: dict[str, Any] | None = None


class Tool(Protocol):
    """Protocol for all tools in the system."""

    @property
    def name(self) -> str:
        """Unique tool name."""
        ...

    @property
    def description(self) -> str:
        """Human-readable description."""
        ...

    async def execute(self, **kwargs: Any) -> ToolResult:
        """Execute the tool with given parameters."""
        ...


class ToolRegistry:
    """Registry for managing tools.

    Supports registration, lookup, and capability checking.
    Designed for future MCP server integration.
    """

    def __init__(self):
        self._tools: dict[str, Tool] = {}

    def register(self, tool: Tool) -> None:
        """Register a tool."""
        self._tools[tool.name] = tool
        logger.info("Registered tool: %s — %s", tool.name, tool.description)

    def get(self, name: str) -> Tool | None:
        """Get a tool by name."""
        return self._tools.get(name)

    def list_tools(self) -> list[dict[str, str]]:
        """List all registered tools."""
        return [{"name": t.name, "description": t.description} for t in self._tools.values()]

    def has(self, name: str) -> bool:
        """Check if a tool is registered."""
        return name in self._tools

    async def execute(self, name: str, **kwargs: Any) -> ToolResult:
        """Execute a tool by name."""
        tool = self._tools.get(name)
        if not tool:
            return ToolResult(success=False, error=f"Tool not found: {name}")
        try:
            return await tool.execute(**kwargs)
        except Exception as e:
            logger.error("Tool %s failed: %s", name, e)
            return ToolResult(success=False, error=str(e))


# ── Built-in Tool Wrappers ────────────────────────────────────────────────


class GitHubTool:
    """Wraps GitHubClient as a tool."""

    def __init__(self, client: Any):
        self._client = client

    @property
    def name(self) -> str:
        return "github"

    @property
    def description(self) -> str:
        return "GitHub API: repos, files, PRs, issues, reviews"

    async def execute(self, **kwargs: Any) -> ToolResult:
        action = kwargs.get("action", "")
        try:
            if action == "get_file":
                content = await self._client.get_file_content(
                    kwargs["owner"], kwargs["repo"], kwargs["path"]
                )
                return ToolResult(success=True, data=content)
            elif action == "create_pr":
                result = await self._client.create_pull_request(
                    kwargs["owner"],
                    kwargs["repo"],
                    kwargs["title"],
                    kwargs["body"],
                    kwargs["head"],
                    kwargs.get("base"),
                )
                return ToolResult(success=True, data=result)
            elif action == "get_user":
                user = await self._client.get_authenticated_user()
                return ToolResult(success=True, data=user)
            else:
                return ToolResult(success=False, error=f"Unknown action: {action}")
        except Exception as e:
            return ToolResult(success=False, error=str(e))


class LLMTool:
    """Wraps LLMProvider as a tool."""

    def __init__(self, provider: Any):
        self._provider = provider

    @property
    def name(self) -> str:
        return "llm"

    @property
    def description(self) -> str:
        return "LLM completion: analyze, generate, classify text"

    async def execute(self, **kwargs: Any) -> ToolResult:
        try:
            prompt = kwargs.get("prompt", "")
            system = kwargs.get("system")
            response = await self._provider.complete(prompt, system_prompt=system)
            return ToolResult(success=True, data=response)
        except Exception as e:
            return ToolResult(success=False, error=str(e))


def create_default_tools(github_client: Any = None, llm_provider: Any = None) -> ToolRegistry:
    """Create a tool registry with default tools."""
    registry = ToolRegistry()
    if github_client:
        registry.register(GitHubTool(github_client))
    if llm_provider:
        registry.register(LLMTool(llm_provider))
    return registry
