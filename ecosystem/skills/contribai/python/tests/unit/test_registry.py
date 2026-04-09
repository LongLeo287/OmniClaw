"""Tests for contribai.agents.registry — Sub-agent registry system."""

from __future__ import annotations

import pytest

from contribai.agents.registry import (
    AgentContext,
    AgentRegistry,
    AgentRole,
    AnalyzerAgent,
    ComplianceAgent,
    GeneratorAgent,
    PatrolAgent,
    create_default_registry,
)


class TestAgentRole:
    """Tests for AgentRole enum."""

    def test_values(self):
        assert AgentRole.ANALYZER == "analyzer"
        assert AgentRole.GENERATOR == "generator"
        assert AgentRole.PATROL == "patrol"
        assert AgentRole.ISSUE_SOLVER == "issue_solver"
        assert AgentRole.COMPLIANCE == "compliance"

    def test_all_roles(self):
        roles = list(AgentRole)
        assert len(roles) == 5


class TestAgentContext:
    """Tests for AgentContext dataclass."""

    def test_defaults(self):
        ctx = AgentContext(role=AgentRole.ANALYZER)
        assert ctx.role == AgentRole.ANALYZER
        assert ctx.repo_name == ""
        assert ctx.data == {}
        assert ctx.tools == []
        assert ctx.max_duration_sec == 900

    def test_custom_data(self):
        ctx = AgentContext(
            role=AgentRole.GENERATOR,
            repo_name="owner/repo",
            data={"findings": [1, 2, 3]},
        )
        assert ctx.repo_name == "owner/repo"
        assert len(ctx.data["findings"]) == 3


class TestAgentRegistry:
    """Tests for AgentRegistry."""

    @pytest.fixture
    def registry(self):
        return AgentRegistry()

    def test_list_agents_empty(self, registry):
        agents = registry.list_agents()
        assert agents == []

    def test_get_nonexistent(self, registry):
        agent = registry.get(AgentRole.ANALYZER)
        assert agent is None

    def test_max_concurrent(self):
        registry = AgentRegistry(max_concurrent=5)
        assert registry._max_concurrent == 5

    def test_default_max_concurrent(self):
        registry = AgentRegistry()
        assert registry._max_concurrent == 3

    def test_register_and_get(self):
        registry = AgentRegistry()
        agent = AnalyzerAgent()
        registry.register(agent)
        assert registry.get(AgentRole.ANALYZER) is agent

    def test_list_agents(self):
        registry = AgentRegistry()
        registry.register(AnalyzerAgent())
        agents = registry.list_agents()
        assert len(agents) == 1
        assert agents[0]["role"] == "analyzer"


class TestBuiltinAgents:
    """Tests for built-in agent stubs."""

    def test_analyzer_role(self):
        agent = AnalyzerAgent()
        assert agent.role == AgentRole.ANALYZER
        assert agent.description

    def test_generator_role(self):
        agent = GeneratorAgent()
        assert agent.role == AgentRole.GENERATOR
        assert agent.description

    def test_patrol_role(self):
        agent = PatrolAgent()
        assert agent.role == AgentRole.PATROL
        assert agent.description

    def test_compliance_role(self):
        agent = ComplianceAgent()
        assert agent.role == AgentRole.COMPLIANCE
        assert agent.description

    @pytest.mark.asyncio
    async def test_analyzer_missing_context(self):
        agent = AnalyzerAgent()
        ctx = AgentContext(role=AgentRole.ANALYZER)
        result = await agent.execute(ctx)
        assert "error" in result

    @pytest.mark.asyncio
    async def test_generator_missing_context(self):
        agent = GeneratorAgent()
        ctx = AgentContext(role=AgentRole.GENERATOR)
        result = await agent.execute(ctx)
        assert "error" in result

    @pytest.mark.asyncio
    async def test_patrol_missing_context(self):
        agent = PatrolAgent()
        ctx = AgentContext(role=AgentRole.PATROL)
        result = await agent.execute(ctx)
        assert "error" in result

    @pytest.mark.asyncio
    async def test_compliance_no_pr_manager(self):
        agent = ComplianceAgent()
        ctx = AgentContext(role=AgentRole.COMPLIANCE)
        result = await agent.execute(ctx)
        assert result["actions"] == []
        assert result["count"] == 0


class TestCreateDefaultRegistry:
    """Tests for create_default_registry factory."""

    def test_creates_registry(self):
        registry = create_default_registry()
        assert isinstance(registry, AgentRegistry)

    def test_has_all_agents(self):
        registry = create_default_registry()
        agents = registry.list_agents()
        roles = [a["role"] for a in agents]
        assert "analyzer" in roles
        assert "generator" in roles
        assert "patrol" in roles
        assert "compliance" in roles
