"""MCP Client — consume external MCP servers.

Allows ContribAI to connect to external MCP servers (e.g. code search,
linting, or other tool providers) via the Model Context Protocol.

v3.0.0: Initial implementation with StdioMCPClient.
"""

from __future__ import annotations

import asyncio
import json
import logging
from typing import Any

logger = logging.getLogger(__name__)


class MCPToolResult:
    """Result from calling an MCP tool."""

    def __init__(self, content: list[dict[str, Any]], is_error: bool = False):
        self.content = content
        self.is_error = is_error

    @property
    def text(self) -> str:
        """Extract text content from result."""
        texts = []
        for item in self.content:
            if item.get("type") == "text":
                texts.append(item.get("text", ""))
        return "\n".join(texts)


class MCPClient:
    """Base MCP client interface."""

    async def connect(self) -> None:
        """Establish connection to MCP server."""

    async def disconnect(self) -> None:
        """Close connection to MCP server."""

    async def list_tools(self) -> list[dict[str, Any]]:
        """List available tools from the MCP server.

        Returns:
            List of tool definitions with name, description, inputSchema.
        """
        return []

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> MCPToolResult:
        """Call a tool on the MCP server.

        Args:
            name: Tool name.
            arguments: Tool arguments.

        Returns:
            MCPToolResult with content.
        """
        raise NotImplementedError


class StdioMCPClient(MCPClient):
    """MCP client that communicates via stdio with a subprocess.

    Spawns an MCP server process and communicates using JSON-RPC
    over stdin/stdout.

    Usage:
        client = StdioMCPClient("python", "-m", "some_mcp_server")
        await client.connect()
        tools = await client.list_tools()
        result = await client.call_tool("search", {"query": "test"})
        await client.disconnect()
    """

    def __init__(self, *cmd: str, env: dict[str, str] | None = None, timeout: float = 30.0):
        self._cmd = cmd
        self._env = env
        self._timeout = timeout
        self._process: asyncio.subprocess.Process | None = None
        self._request_id = 0

    async def connect(self) -> None:
        """Spawn the MCP server subprocess."""
        logger.info("🔌 Connecting to MCP server: %s", " ".join(self._cmd))
        self._process = await asyncio.create_subprocess_exec(
            *self._cmd,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            env=self._env,
        )

        # Send initialize request
        init_result = await self._send_request(
            "initialize",
            {
                "protocolVersion": "2024-11-05",
                "capabilities": {},
                "clientInfo": {"name": "contribai", "version": "3.0.0"},
            },
        )
        logger.info("MCP server initialized: %s", init_result.get("serverInfo", {}))

        # Send initialized notification
        await self._send_notification("notifications/initialized", {})

    async def disconnect(self) -> None:
        """Kill the MCP server subprocess."""
        if self._process and self._process.returncode is None:
            self._process.terminate()
            await self._process.wait()
            logger.info("MCP server disconnected")

    async def list_tools(self) -> list[dict[str, Any]]:
        """List tools from the MCP server."""
        result = await self._send_request("tools/list", {})
        return result.get("tools", [])

    async def call_tool(self, name: str, arguments: dict[str, Any]) -> MCPToolResult:
        """Call a tool on the MCP server."""
        result = await self._send_request(
            "tools/call",
            {
                "name": name,
                "arguments": arguments,
            },
        )
        return MCPToolResult(
            content=result.get("content", []),
            is_error=result.get("isError", False),
        )

    async def _send_request(self, method: str, params: dict[str, Any]) -> dict[str, Any]:
        """Send a JSON-RPC request and wait for response."""
        if not self._process or not self._process.stdin or not self._process.stdout:
            raise RuntimeError("MCP server not connected")

        self._request_id += 1
        request = {
            "jsonrpc": "2.0",
            "id": self._request_id,
            "method": method,
            "params": params,
        }

        payload = json.dumps(request) + "\n"
        self._process.stdin.write(payload.encode())
        await self._process.stdin.drain()

        # Read response line
        line = await asyncio.wait_for(self._process.stdout.readline(), timeout=self._timeout)
        response = json.loads(line.decode())

        if "error" in response:
            error = response["error"]
            logger.error("MCP error: %s", error.get("message", "Unknown"))
            raise RuntimeError(f"MCP error: {error.get('message', 'Unknown')}")

        return response.get("result", {})

    async def _send_notification(self, method: str, params: dict[str, Any]) -> None:
        """Send a JSON-RPC notification (no response expected)."""
        if not self._process or not self._process.stdin:
            raise RuntimeError("MCP server not connected")

        notification = {
            "jsonrpc": "2.0",
            "method": method,
            "params": params,
        }

        payload = json.dumps(notification) + "\n"
        self._process.stdin.write(payload.encode())
        await self._process.stdin.drain()
