"""Integration tests for pipeline wiring — middleware, agents, tools."""

from __future__ import annotations

from unittest.mock import AsyncMock, MagicMock

import pytest

from contribai.agents.registry import (
    AgentContext,
    AgentRegistry,
    AgentRole,
    IssueSolverAgent,
    create_default_registry,
)
from contribai.core.middleware import (
    DCOMiddleware,
    MiddlewareChain,
    PipelineContext,
    RateLimitMiddleware,
    ValidationMiddleware,
    build_default_chain,
)
from contribai.tools.protocol import (
    GitHubTool,
    LLMTool,
    ToolRegistry,
    create_default_tools,
)


class TestAgentRegistry:
    """Tests for AgentRegistry and built-in agents."""

    def test_create_default_registry(self):
        registry = create_default_registry()
        agents = registry.list_agents()
        assert len(agents) == 5
        roles = {a["role"] for a in agents}
        assert roles == {"analyzer", "generator", "patrol", "compliance", "issue_solver"}

    def test_get_agent(self):
        registry = create_default_registry()
        analyzer = registry.get(AgentRole.ANALYZER)
        assert analyzer is not None
        assert analyzer.role == AgentRole.ANALYZER

    def test_get_unknown_agent_returns_none(self):
        registry = AgentRegistry()
        assert registry.get(AgentRole.ANALYZER) is None

    @pytest.mark.asyncio
    async def test_execute_raises_for_unknown_role(self):
        registry = AgentRegistry()
        ctx = AgentContext(role=AgentRole.ANALYZER)
        with pytest.raises(ValueError, match="No agent registered"):
            await registry.execute(AgentRole.ANALYZER, ctx)

    @pytest.mark.asyncio
    async def test_issue_solver_agent_no_solver(self):
        agent = IssueSolverAgent()
        ctx = AgentContext(role=AgentRole.ISSUE_SOLVER, data={})
        result = await agent.execute(ctx)
        assert result == {"error": "Missing solver in context"}

    @pytest.mark.asyncio
    async def test_issue_solver_agent_no_issues(self):
        agent = IssueSolverAgent()
        ctx = AgentContext(
            role=AgentRole.ISSUE_SOLVER,
            data={"solver": MagicMock(), "repo": MagicMock(), "issues": []},
        )
        result = await agent.execute(ctx)
        assert result == {"solved": 0, "contributions": []}


class TestMiddlewareChain:
    """Tests for middleware chain."""

    def test_build_default_chain(self):
        middlewares = build_default_chain()
        assert len(middlewares) == 5
        types = [type(m).__name__ for m in middlewares]
        assert types == [
            "RateLimitMiddleware",
            "ValidationMiddleware",
            "RetryMiddleware",
            "DCOMiddleware",
            "QualityGateMiddleware",
        ]

    @pytest.mark.asyncio
    async def test_rate_limit_skip(self):
        mw = RateLimitMiddleware(max_prs_per_day=10)
        ctx = PipelineContext(repo_name="test/repo", remaining_prs=0)

        async def noop(c):
            return c

        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.should_skip is True
        assert result.rate_limited is True

    @pytest.mark.asyncio
    async def test_validation_skip_no_repo(self):
        mw = ValidationMiddleware()
        ctx = PipelineContext(repo_name="test/repo", repo=None)
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.should_skip is True
        assert result.skip_reason == "No repo data"

    @pytest.mark.asyncio
    async def test_dco_middleware_sets_signoff(self):
        mw = DCOMiddleware()
        ctx = PipelineContext(
            repo_name="test/repo",
            repo=MagicMock(),
            metadata={
                "user": {"name": "Test User", "email": "test@example.com", "login": "testuser"}
            },
        )
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.signoff == "Test User <test@example.com>"
        assert result.dco_required is True


class TestToolRegistry:
    """Tests for ToolRegistry."""

    def test_create_default_tools_with_clients(self):
        gh_mock = MagicMock()
        llm_mock = MagicMock()
        registry = create_default_tools(github_client=gh_mock, llm_provider=llm_mock)
        tools = registry.list_tools()
        assert len(tools) == 2
        names = {t["name"] for t in tools}
        assert names == {"github", "llm"}

    def test_create_default_tools_empty(self):
        registry = create_default_tools()
        assert len(registry.list_tools()) == 0

    def test_has_tool(self):
        registry = create_default_tools(github_client=MagicMock())
        assert registry.has("github") is True
        assert registry.has("llm") is False

    @pytest.mark.asyncio
    async def test_execute_unknown_tool(self):
        registry = ToolRegistry()
        result = await registry.execute("nonexistent")
        assert result.success is False
        assert "not found" in result.error

    @pytest.mark.asyncio
    async def test_github_tool_get_user(self):
        mock_client = AsyncMock()
        mock_client.get_authenticated_user.return_value = {"login": "bot"}
        tool = GitHubTool(mock_client)
        result = await tool.execute(action="get_user")
        assert result.success is True
        assert result.data == {"login": "bot"}

    @pytest.mark.asyncio
    async def test_llm_tool_complete(self):
        mock_provider = AsyncMock()
        mock_provider.complete.return_value = "Hello world"
        tool = LLMTool(mock_provider)
        result = await tool.execute(prompt="Say hello")
        assert result.success is True
        assert result.data == "Hello world"
