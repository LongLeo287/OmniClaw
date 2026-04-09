"""Smart task-to-model router.

Routes tasks to the optimal model based on complexity,
cost constraints, and model capabilities.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass

from contribai.llm.models import (
    GEMINI_2_5_FLASH,
    GEMINI_3_1_FLASH_LITE,
    GEMINI_3_1_PRO,
    GEMINI_3_FLASH,
    ModelSpec,
    TaskType,
    get_cheapest_capable,
    get_models_for_task,
)

logger = logging.getLogger(__name__)


class CostStrategy:
    """Cost optimization strategies."""

    PERFORMANCE = "performance"  # Best model always
    BALANCED = "balanced"  # Good model, reasonable cost
    ECONOMY = "economy"  # Cheapest capable model


@dataclass
class RoutingDecision:
    """Result of a routing decision."""

    model: ModelSpec
    task_type: TaskType
    reason: str
    fallback: ModelSpec | None = None


class TaskRouter:
    """Routes tasks to optimal models."""

    def __init__(
        self,
        strategy: str = CostStrategy.BALANCED,
        default_model: str = "gemini-2.5-flash",
    ):
        self._strategy = strategy
        self._default = default_model
        self._task_count: dict[str, int] = {}
        self._cost_total: float = 0.0

    def route(
        self,
        task_type: TaskType,
        *,
        complexity: int = 5,
        file_count: int = 1,
        token_estimate: int = 1000,
    ) -> RoutingDecision:
        """Route a task to the best model.

        Args:
            task_type: Type of task
            complexity: 1-10 complexity score
            file_count: Number of files involved
            token_estimate: Estimated tokens needed
        """
        if self._strategy == CostStrategy.PERFORMANCE:
            return self._route_performance(task_type)
        if self._strategy == CostStrategy.ECONOMY:
            return self._route_economy(task_type)
        return self._route_balanced(
            task_type,
            complexity=complexity,
            file_count=file_count,
        )

    def _route_performance(self, task_type: TaskType) -> RoutingDecision:
        """Always pick the most powerful model."""
        models = get_models_for_task(task_type)
        model = models[0] if models else GEMINI_3_1_PRO
        return RoutingDecision(
            model=model,
            task_type=task_type,
            reason=f"Performance mode: {model.display_name}",
            fallback=GEMINI_3_FLASH,
        )

    def _route_economy(self, task_type: TaskType) -> RoutingDecision:
        """Always pick the cheapest capable model."""
        model = get_cheapest_capable(task_type, min_score=60)
        if not model:
            model = GEMINI_3_1_FLASH_LITE
        return RoutingDecision(
            model=model,
            task_type=task_type,
            reason=f"Economy mode: {model.display_name}",
            fallback=GEMINI_2_5_FLASH,
        )

    def _route_balanced(
        self,
        task_type: TaskType,
        *,
        complexity: int,
        file_count: int,
    ) -> RoutingDecision:
        """Smart routing based on task complexity."""
        # High complexity → Pro
        if complexity >= 8 or file_count >= 10:
            model = GEMINI_3_1_PRO
            reason = f"High complexity ({complexity}/10, {file_count} files) → Pro"
            fallback = GEMINI_3_FLASH

        # Medium complexity → Flash
        elif complexity >= 4:
            model = GEMINI_3_FLASH
            reason = f"Medium complexity ({complexity}/10) → Flash"
            fallback = GEMINI_2_5_FLASH

        # Low complexity → Flash Lite
        else:
            model = GEMINI_3_1_FLASH_LITE
            reason = f"Low complexity ({complexity}/10) → Lite"
            fallback = GEMINI_3_FLASH

        # Override for specific task types
        if task_type == TaskType.CODE_GEN and complexity < 8:
            model = GEMINI_3_FLASH
            reason = "Code gen → Flash (balanced)"
            fallback = GEMINI_3_1_PRO

        if task_type == TaskType.PLANNING:
            model = GEMINI_3_1_PRO
            reason = "Planning always → Pro"
            fallback = GEMINI_3_FLASH

        if task_type == TaskType.BULK:
            model = GEMINI_3_1_FLASH_LITE
            reason = "Bulk → Flash Lite (cost)"
            fallback = GEMINI_3_FLASH

        self._task_count[model.name] = self._task_count.get(model.name, 0) + 1

        return RoutingDecision(
            model=model,
            task_type=task_type,
            reason=reason,
            fallback=fallback,
        )

    def get_default_assignments(
        self,
    ) -> dict[str, str]:
        """Get default model assignment for each task type."""
        return {
            TaskType.ANALYSIS: GEMINI_3_FLASH.name,
            TaskType.CODE_GEN: GEMINI_3_FLASH.name,
            TaskType.REVIEW: GEMINI_3_FLASH.name,
            TaskType.PLANNING: GEMINI_3_1_PRO.name,
            TaskType.DOCS: GEMINI_3_1_FLASH_LITE.name,
            TaskType.QUICK_FIX: GEMINI_3_1_FLASH_LITE.name,
            TaskType.BULK: GEMINI_3_1_FLASH_LITE.name,
            TaskType.MULTIMODAL: GEMINI_3_1_PRO.name,
        }

    @property
    def stats(self) -> dict:
        """Get routing statistics."""
        return {
            "strategy": self._strategy,
            "tasks_routed": self._task_count,
            "total_tasks": sum(self._task_count.values()),
        }
