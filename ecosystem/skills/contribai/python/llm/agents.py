"""Multi-agent coordinator for ContribAI.

Specialized agents collaborate on repo analysis, code generation,
review, and documentation. Each agent uses the optimal model
for its specific task.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from contribai.llm.models import TaskType
from contribai.llm.router import CostStrategy, TaskRouter

logger = logging.getLogger(__name__)


@dataclass
class AgentResult:
    """Result from an agent execution."""

    agent_name: str
    model_used: str
    task_type: str
    output: str = ""
    tokens_used: int = 0
    success: bool = True
    error: str = ""


class BaseAgent:
    """Base class for specialized agents."""

    name: str = "base"
    task_type: TaskType = TaskType.ANALYSIS

    def __init__(self, llm_provider, router: TaskRouter):
        self._llm = llm_provider
        self._router = router

    async def execute(self, context: dict, **kwargs) -> AgentResult:
        """Execute the agent's task."""
        decision = self._router.route(
            self.task_type,
            complexity=context.get("complexity", 5),
            file_count=context.get("file_count", 1),
        )
        logger.info(
            "%s → %s (%s)",
            self.name,
            decision.model.display_name,
            decision.reason,
        )

        try:
            prompt = self.build_prompt(context)
            result = await self._llm.complete(
                prompt,
                system=self.system_prompt(),
            )
            return AgentResult(
                agent_name=self.name,
                model_used=decision.model.name,
                task_type=self.task_type.value,
                output=result,
                success=True,
            )
        except Exception as e:
            logger.warning("%s failed: %s", self.name, e)
            return AgentResult(
                agent_name=self.name,
                model_used=decision.model.name,
                task_type=self.task_type.value,
                success=False,
                error=str(e),
            )

    def system_prompt(self) -> str:
        return "You are a helpful coding assistant."

    def build_prompt(self, context: dict) -> str:
        return str(context)


class AnalysisAgent(BaseAgent):
    """Specialized agent for code analysis."""

    name = "Analyzer"
    task_type = TaskType.ANALYSIS

    def system_prompt(self) -> str:
        return (
            "You are a senior code reviewer specializing in "
            "security vulnerabilities, code quality issues, "
            "and best practices. Be precise and actionable."
        )

    def build_prompt(self, context: dict) -> str:
        code = context.get("code", "")
        lang = context.get("language", "unknown")
        file_path = context.get("file_path", "")
        return (
            f"Analyze this {lang} file for issues:\n"
            f"File: {file_path}\n\n"
            f"```{lang}\n{code[:8000]}\n```\n\n"
            "List all security, quality, and performance issues. "
            "For each: severity (critical/high/medium/low), "
            "line numbers, description, and fix suggestion."
        )


class CodeGenAgent(BaseAgent):
    """Specialized agent for code generation and fixes."""

    name = "CodeGen"
    task_type = TaskType.CODE_GEN

    def system_prompt(self) -> str:
        return (
            "You are an expert programmer. Generate clean, "
            "well-documented, production-ready code. Follow "
            "the project's existing style and conventions."
        )

    def build_prompt(self, context: dict) -> str:
        issue = context.get("issue", "")
        original = context.get("original_code", "")
        lang = context.get("language", "")
        return (
            f"Fix the following issue in this {lang} code:\n\n"
            f"Issue: {issue}\n\n"
            f"Original code:\n```{lang}\n{original[:6000]}\n```\n\n"
            "Provide the complete fixed code with comments "
            "explaining the changes."
        )


class ReviewAgent(BaseAgent):
    """Specialized agent for self-review of generated code."""

    name = "Reviewer"
    task_type = TaskType.REVIEW

    def system_prompt(self) -> str:
        return (
            "You are a meticulous code reviewer. Check for "
            "correctness, edge cases, style consistency, and "
            "potential regressions. Be critical but constructive."
        )

    def build_prompt(self, context: dict) -> str:
        original = context.get("original_code", "")
        modified = context.get("modified_code", "")
        issue = context.get("issue", "")
        return (
            f"Review this code change:\n\n"
            f"Issue being fixed: {issue}\n\n"
            f"Original:\n```\n{original[:4000]}\n```\n\n"
            f"Modified:\n```\n{modified[:4000]}\n```\n\n"
            "Check: correctness, edge cases, style, "
            "regressions. Approve or suggest improvements."
        )


class DocsAgent(BaseAgent):
    """Specialized agent for documentation improvements."""

    name = "DocsWriter"
    task_type = TaskType.DOCS

    def system_prompt(self) -> str:
        return (
            "You are a technical writer. Write clear, concise "
            "documentation. Use proper formatting, examples, "
            "and follow the project's documentation style."
        )

    def build_prompt(self, context: dict) -> str:
        code = context.get("code", "")
        doc_type = context.get("doc_type", "docstring")
        return (
            f"Improve the {doc_type} for this code:\n\n"
            f"```\n{code[:6000]}\n```\n\n"
            f"Generate improved {doc_type} with examples."
        )


class PlannerAgent(BaseAgent):
    """Specialized agent for contribution planning."""

    name = "Planner"
    task_type = TaskType.PLANNING

    def system_prompt(self) -> str:
        return (
            "You are a software architect. Analyze repositories "
            "and plan contributions strategically. Consider "
            "impact, feasibility, and maintainer expectations."
        )

    def build_prompt(self, context: dict) -> str:
        repo = context.get("repo_name", "")
        findings = context.get("findings", [])
        return (
            f"Plan contributions for {repo}.\n\n"
            f"Findings:\n{findings}\n\n"
            "Prioritize by: impact, feasibility, "
            "likelihood of acceptance. "
            "Output a ranked action plan."
        )


# ── Multi-Agent Coordinator ──────────────────────────


class AgentCoordinator:
    """Coordinates multiple specialized agents.

    Pipeline: Analyze → Plan → Generate → Review → Refine
    """

    def __init__(
        self,
        llm_provider,
        strategy: str = CostStrategy.BALANCED,
    ):
        self._llm = llm_provider
        self._router = TaskRouter(strategy=strategy)
        self._agents = {
            "analyzer": AnalysisAgent(llm_provider, self._router),
            "codegen": CodeGenAgent(llm_provider, self._router),
            "reviewer": ReviewAgent(llm_provider, self._router),
            "docs": DocsAgent(llm_provider, self._router),
            "planner": PlannerAgent(llm_provider, self._router),
        }
        self._results: list[AgentResult] = []

    async def run_analysis(self, code: str, language: str, file_path: str) -> AgentResult:
        """Run analysis agent on code."""
        result = await self._agents["analyzer"].execute(
            {
                "code": code,
                "language": language,
                "file_path": file_path,
                "complexity": min(len(code) // 500, 10),
                "file_count": 1,
            }
        )
        self._results.append(result)
        return result

    async def run_codegen(
        self,
        issue: str,
        original_code: str,
        language: str,
    ) -> AgentResult:
        """Run code generation agent."""
        result = await self._agents["codegen"].execute(
            {
                "issue": issue,
                "original_code": original_code,
                "language": language,
                "complexity": 7,
            }
        )
        self._results.append(result)
        return result

    async def run_review(
        self,
        original_code: str,
        modified_code: str,
        issue: str,
    ) -> AgentResult:
        """Run review agent on changes."""
        result = await self._agents["reviewer"].execute(
            {
                "original_code": original_code,
                "modified_code": modified_code,
                "issue": issue,
                "complexity": 5,
            }
        )
        self._results.append(result)
        return result

    async def run_full_pipeline(
        self,
        code: str,
        language: str,
        file_path: str,
    ) -> list[AgentResult]:
        """Run the full multi-agent pipeline.

        1. Analyze → find issues
        2. Generate fix → produce code
        3. Review → validate fix
        """
        results = []

        # Step 1: Analysis
        analysis = await self.run_analysis(code, language, file_path)
        results.append(analysis)

        if not analysis.success or not analysis.output:
            return results

        # Step 2: Code generation
        codegen = await self.run_codegen(
            issue=analysis.output,
            original_code=code,
            language=language,
        )
        results.append(codegen)

        if not codegen.success or not codegen.output:
            return results

        # Step 3: Review
        review = await self.run_review(
            original_code=code,
            modified_code=codegen.output,
            issue=analysis.output,
        )
        results.append(review)

        return results

    @property
    def routing_stats(self) -> dict:
        return self._router.stats

    @property
    def agent_stats(self) -> list[dict]:
        return [
            {
                "agent": r.agent_name,
                "model": r.model_used,
                "success": r.success,
                "tokens": r.tokens_used,
            }
            for r in self._results
        ]
