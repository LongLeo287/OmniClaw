"""Sub-agent registry and protocol.

Inspired by DeerFlow's sub-agent system: each agent has a scoped context,
specific tools, and is orchestrated by a lead agent.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Protocol

logger = logging.getLogger(__name__)


class AgentRole(str, Enum):  # noqa: UP042
    """Roles available for sub-agents."""

    ANALYZER = "analyzer"
    GENERATOR = "generator"
    PATROL = "patrol"
    ISSUE_SOLVER = "issue_solver"
    COMPLIANCE = "compliance"


@dataclass
class AgentContext:
    """Isolated context for a sub-agent."""

    role: AgentRole
    repo_name: str = ""
    owner: str = ""
    data: dict[str, Any] = field(default_factory=dict)
    tools: list[str] = field(default_factory=list)
    max_duration_sec: int = 900  # 15min default like DeerFlow
    parent_context: dict[str, Any] | None = None


class SubAgent(Protocol):
    """Protocol for sub-agents."""

    @property
    def role(self) -> AgentRole: ...

    @property
    def description(self) -> str: ...

    async def execute(self, ctx: AgentContext) -> dict[str, Any]:
        """Execute the agent's task with the given context."""
        ...


class AgentRegistry:
    """Registry for discovering and managing sub-agents.

    Agents register themselves and can be looked up by role.
    Supports concurrent execution of multiple agents.
    """

    def __init__(self, max_concurrent: int = 3):
        self._agents: dict[AgentRole, SubAgent] = {}
        self._max_concurrent = max_concurrent

    def register(self, agent: SubAgent) -> None:
        """Register a sub-agent."""
        self._agents[agent.role] = agent
        logger.info("Registered agent: %s (%s)", agent.role.value, agent.description)

    def get(self, role: AgentRole) -> SubAgent | None:
        """Get a registered agent by role."""
        return self._agents.get(role)

    def list_agents(self) -> list[dict[str, str]]:
        """List all registered agents."""
        return [{"role": a.role.value, "description": a.description} for a in self._agents.values()]

    async def execute(self, role: AgentRole, ctx: AgentContext) -> dict[str, Any]:
        """Execute a specific agent."""
        agent = self._agents.get(role)
        if not agent:
            raise ValueError(f"No agent registered for role: {role.value}")

        logger.info("Executing agent: %s for %s", role.value, ctx.repo_name)
        return await agent.execute(ctx)

    async def execute_parallel(
        self,
        tasks: list[tuple[AgentRole, AgentContext]],
    ) -> list[dict[str, Any]]:
        """Execute multiple agents in parallel (up to max_concurrent)."""
        import asyncio

        sem = asyncio.Semaphore(self._max_concurrent)
        results: list[dict[str, Any]] = []

        async def _run(role: AgentRole, ctx: AgentContext) -> dict[str, Any]:
            async with sem:
                return await self.execute(role, ctx)

        gathered = await asyncio.gather(
            *[_run(r, c) for r, c in tasks],
            return_exceptions=True,
        )

        for i, result in enumerate(gathered):
            if isinstance(result, Exception):
                role = tasks[i][0]
                logger.error("Agent %s failed: %s", role.value, result)
                results.append({"error": str(result), "role": role.value})
            else:
                results.append(result)

        return results


# ── Built-in Agent Stubs ──────────────────────────────────────────────────
# These are lightweight stubs that wrap existing ContribAI components.
# They serve as the integration layer for the sub-agent architecture.


class AnalyzerAgent:
    """Wraps CodeAnalyzer as a sub-agent."""

    @property
    def role(self) -> AgentRole:
        return AgentRole.ANALYZER

    @property
    def description(self) -> str:
        return "Analyze repository code for security, quality, and performance issues"

    async def execute(self, ctx: AgentContext) -> dict[str, Any]:
        analyzer = ctx.data.get("analyzer")
        repo = ctx.data.get("repo")
        if not analyzer or not repo:
            return {"error": "Missing analyzer or repo in context"}
        result = await analyzer.analyze(repo)
        return {"findings": len(result.findings), "result": result}


class GeneratorAgent:
    """Wraps ContributionGenerator as a sub-agent."""

    @property
    def role(self) -> AgentRole:
        return AgentRole.GENERATOR

    @property
    def description(self) -> str:
        return "Generate code fixes and contributions from analysis findings"

    async def execute(self, ctx: AgentContext) -> dict[str, Any]:
        generator = ctx.data.get("generator")
        if not generator:
            return {"error": "Missing generator in context"}
        findings = ctx.data.get("findings", [])
        repo_context = ctx.data.get("repo_context")
        contributions = []
        for finding in findings:
            contrib = await generator.generate(finding, repo_context)
            if contrib:
                contributions.append(contrib)
        return {"contributions": contributions, "count": len(contributions)}


class PatrolAgent:
    """Wraps PRPatrol as a sub-agent."""

    @property
    def role(self) -> AgentRole:
        return AgentRole.PATROL

    @property
    def description(self) -> str:
        return "Monitor open PRs for review feedback and auto-respond with fixes"

    async def execute(self, ctx: AgentContext) -> dict[str, Any]:
        patrol = ctx.data.get("patrol")
        if not patrol:
            return {"error": "Missing patrol in context"}
        pr_records = ctx.data.get("pr_records", [])
        dry_run = ctx.data.get("dry_run", False)
        result = await patrol.patrol(pr_records, dry_run=dry_run)
        return {"feedback_count": result.feedback_processed, "result": result}


class ComplianceAgent:
    """Handles CLA signing, DCO signoff, and CI monitoring."""

    @property
    def role(self) -> AgentRole:
        return AgentRole.COMPLIANCE

    @property
    def description(self) -> str:
        return "Handle CLA auto-signing, DCO signoff, and post-PR CI monitoring"

    async def execute(self, ctx: AgentContext) -> dict[str, Any]:
        actions = []
        pr_manager = ctx.data.get("pr_manager")
        pr_result = ctx.data.get("pr_result")

        if pr_manager and pr_result:
            # CLA check
            cla_needed = ctx.data.get("cla_required", False)
            if cla_needed:
                actions.append("cla_signed")

            # DCO check
            signoff = ctx.data.get("signoff")
            if signoff:
                actions.append(f"dco_signoff:{signoff}")

        return {"actions": actions, "count": len(actions)}


class IssueSolverAgent:
    """Wraps IssueSolver as a sub-agent for issue-driven contributions."""

    @property
    def role(self) -> AgentRole:
        return AgentRole.ISSUE_SOLVER

    @property
    def description(self) -> str:
        return "Solve open GitHub issues by generating targeted code contributions"

    async def execute(self, ctx: AgentContext) -> dict[str, Any]:
        solver = ctx.data.get("solver")
        if not solver:
            return {"error": "Missing solver in context"}
        repo = ctx.data.get("repo")
        issues = ctx.data.get("issues", [])
        max_issues = ctx.data.get("max_issues", 5)

        if not issues:
            return {"solved": 0, "contributions": []}

        contributions = []
        for issue in issues[:max_issues]:
            result = await solver.solve_issue(repo, issue)
            if result:
                contributions.append(result)

        return {"contributions": contributions, "solved": len(contributions)}


def create_default_registry() -> AgentRegistry:
    """Create a registry with all built-in agents."""
    registry = AgentRegistry(max_concurrent=3)
    registry.register(AnalyzerAgent())
    registry.register(GeneratorAgent())
    registry.register(PatrolAgent())
    registry.register(ComplianceAgent())
    registry.register(IssueSolverAgent())
    return registry
