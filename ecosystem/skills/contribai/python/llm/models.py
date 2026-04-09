"""Model registry with capabilities, costs, and context windows.

Catalogs available Gemini models and their strengths for
intelligent task-to-model routing.
"""

from __future__ import annotations

import logging
from dataclasses import dataclass, field
from enum import StrEnum

logger = logging.getLogger(__name__)


class TaskType(StrEnum):
    """Types of tasks that models can be assigned to."""

    ANALYSIS = "analysis"  # Security, code quality analysis
    CODE_GEN = "code_gen"  # Code generation / fixes
    REVIEW = "review"  # Self-review, PR review
    DOCS = "docs"  # Documentation improvements
    QUICK_FIX = "quick_fix"  # Simple, targeted fixes
    BULK = "bulk"  # High-volume, low-complexity
    PLANNING = "planning"  # Architecture, strategy
    MULTIMODAL = "multimodal"  # Image/UI analysis


class ModelTier(StrEnum):
    """Model performance tiers."""

    PRO = "pro"  # Highest capability, highest cost
    FLASH = "flash"  # Good capability, balanced cost
    LITE = "lite"  # Basic capability, lowest cost


@dataclass
class ModelSpec:
    """Specification of a model's capabilities and costs."""

    name: str  # e.g. "gemini-3.1-pro-preview"
    display_name: str  # e.g. "Gemini 3.1 Pro"
    tier: ModelTier = ModelTier.FLASH
    context_window: int = 1_000_000  # tokens
    max_output: int = 65_536

    # Cost per 1M tokens (approximate, USD)
    input_cost: float = 0.0
    output_cost: float = 0.0

    # Capability scores (0-100)
    coding: int = 70
    analysis: int = 70
    reasoning: int = 70
    speed: int = 70
    multimodal: int = 50

    # Best-fit task types
    best_for: list[TaskType] = field(default_factory=list)

    # Description
    description: str = ""

    @property
    def overall_score(self) -> float:
        return (self.coding + self.analysis + self.reasoning + self.speed) / 4.0

    @property
    def cost_efficiency(self) -> float:
        """Higher = more cost-efficient."""
        total_cost = self.input_cost + self.output_cost
        if total_cost == 0:
            return 100.0
        return self.overall_score / total_cost


# ── Model Catalog ─────────────────────────────────────


GEMINI_3_1_PRO = ModelSpec(
    name="gemini-3.1-pro-preview",
    display_name="Gemini 3.1 Pro",
    tier=ModelTier.PRO,
    context_window=1_000_000,
    input_cost=1.25,
    output_cost=10.0,
    coding=98,
    analysis=97,
    reasoning=98,
    speed=55,
    multimodal=95,
    best_for=[
        TaskType.CODE_GEN,
        TaskType.ANALYSIS,
        TaskType.PLANNING,
        TaskType.REVIEW,
    ],
    description=(
        "Most powerful agentic and coding model. 1M context, best multimodal understanding."
    ),
)

GEMINI_3_PRO = ModelSpec(
    name="gemini-3-pro-preview",
    display_name="Gemini 3 Pro",
    tier=ModelTier.PRO,
    context_window=1_000_000,
    input_cost=1.25,
    output_cost=10.0,
    coding=95,
    analysis=95,
    reasoning=96,
    speed=60,
    multimodal=93,
    best_for=[
        TaskType.CODE_GEN,
        TaskType.ANALYSIS,
        TaskType.PLANNING,
    ],
    description=("Powerful agentic and coding model with best multimodal capabilities."),
)

GEMINI_3_FLASH = ModelSpec(
    name="gemini-3-flash-preview",
    display_name="Gemini 3 Flash",
    tier=ModelTier.FLASH,
    context_window=1_000_000,
    input_cost=0.15,
    output_cost=0.60,
    coding=88,
    analysis=87,
    reasoning=85,
    speed=85,
    multimodal=80,
    best_for=[
        TaskType.ANALYSIS,
        TaskType.REVIEW,
        TaskType.QUICK_FIX,
        TaskType.CODE_GEN,
    ],
    description=("Agentic workhorse — near-Pro intelligence with balanced cost and speed."),
)

GEMINI_3_1_FLASH_LITE = ModelSpec(
    name="gemini-3.1-flash-lite-preview",
    display_name="Gemini 3.1 Flash Lite",
    tier=ModelTier.LITE,
    context_window=1_000_000,
    input_cost=0.02,
    output_cost=0.10,
    coding=72,
    analysis=70,
    reasoning=68,
    speed=95,
    multimodal=60,
    best_for=[
        TaskType.BULK,
        TaskType.DOCS,
        TaskType.QUICK_FIX,
    ],
    description=(
        "High-volume, cost-sensitive. Massive quality leap over previous Lite generations."
    ),
)

GEMINI_2_5_FLASH = ModelSpec(
    name="gemini-2.5-flash",
    display_name="Gemini 2.5 Flash",
    tier=ModelTier.FLASH,
    context_window=1_000_000,
    input_cost=0.15,
    output_cost=0.60,
    coding=82,
    analysis=80,
    reasoning=78,
    speed=88,
    multimodal=70,
    best_for=[
        TaskType.ANALYSIS,
        TaskType.REVIEW,
        TaskType.DOCS,
    ],
    description="Previous-gen Flash, still solid for general tasks.",
)


# ── Registry ──────────────────────────────────────────


ALL_MODELS: list[ModelSpec] = [
    GEMINI_3_1_PRO,
    GEMINI_3_PRO,
    GEMINI_3_FLASH,
    GEMINI_3_1_FLASH_LITE,
    GEMINI_2_5_FLASH,
]

MODELS_BY_NAME: dict[str, ModelSpec] = {m.name: m for m in ALL_MODELS}

MODELS_BY_TIER: dict[ModelTier, list[ModelSpec]] = {}
for _m in ALL_MODELS:
    MODELS_BY_TIER.setdefault(_m.tier, []).append(_m)


def get_model(name: str) -> ModelSpec | None:
    """Get model spec by name."""
    return MODELS_BY_NAME.get(name)


def get_models_for_task(
    task_type: TaskType,
) -> list[ModelSpec]:
    """Get models best suited for a task type, sorted by fit."""
    matching = [m for m in ALL_MODELS if task_type in m.best_for]
    # Sort by relevant capability score
    score_key = {
        TaskType.CODE_GEN: lambda m: m.coding,
        TaskType.ANALYSIS: lambda m: m.analysis,
        TaskType.REVIEW: lambda m: m.reasoning,
        TaskType.PLANNING: lambda m: m.reasoning,
        TaskType.DOCS: lambda m: m.speed,
        TaskType.QUICK_FIX: lambda m: m.speed,
        TaskType.BULK: lambda m: m.cost_efficiency,
        TaskType.MULTIMODAL: lambda m: m.multimodal,
    }
    key_fn = score_key.get(task_type, lambda m: m.overall_score)
    return sorted(matching, key=key_fn, reverse=True)


def get_cheapest_capable(
    task_type: TaskType,
    min_score: int = 70,
) -> ModelSpec | None:
    """Get the cheapest model that meets minimum capability."""
    candidates = get_models_for_task(task_type)
    capable = [m for m in candidates if m.overall_score >= min_score]
    if not capable:
        return None
    return min(
        capable,
        key=lambda m: m.input_cost + m.output_cost,
    )
