"""Middleware chain for pipeline processing.

Inspired by DeerFlow's middleware architecture: each middleware handles
a specific cross-cutting concern, executing in strict order.
"""

from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass, field
from typing import Any, Protocol

logger = logging.getLogger(__name__)


@dataclass
class PipelineContext:
    """Context passed through the middleware chain.

    Collects data and decisions as middlewares process it.
    """

    repo_name: str = ""
    owner: str = ""
    repo: Any = None  # Repository model
    dry_run: bool = False

    # Decisions
    should_skip: bool = False
    skip_reason: str = ""

    # Rate limiting
    remaining_prs: int = 10
    rate_limited: bool = False

    # Compliance
    cla_required: bool = False
    cla_signed: bool = False
    dco_required: bool = False
    signoff: str | None = None

    # Quality
    quality_score: float = 0.0
    quality_passed: bool = True

    # Data collected
    guidelines: Any = None
    analysis: Any = None
    contribution: Any = None
    pr_result: Any = None

    # Errors & metadata
    errors: list[str] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)


class Middleware(Protocol):
    """Protocol for pipeline middlewares."""

    async def process(
        self,
        ctx: PipelineContext,
        next_mw: MiddlewareChain,
    ) -> PipelineContext:
        """Process context and call next middleware."""
        ...


class MiddlewareChain:
    """Executes middlewares in order, passing context through each.

    Index is stored per-call frame rather than as shared mutable state so that
    RetryMiddleware can re-invoke the chain from the same position without
    silently skipping downstream middlewares on the second attempt.
    """

    def __init__(self, middlewares: list[Middleware], _start_index: int = 0):
        self._middlewares = list(middlewares)
        self._start_index = _start_index

    async def __call__(self, ctx: PipelineContext) -> PipelineContext:
        # Bug 2 fix: use a snapshot of the current index rather than advancing
        # shared mutable state. Each call creates a child chain at the next
        # position, so retries re-enter from the correct position.
        if self._start_index >= len(self._middlewares):
            return ctx
        mw = self._middlewares[self._start_index]
        next_chain = MiddlewareChain(self._middlewares, self._start_index + 1)
        return await mw.process(ctx, next_chain)


# ── Built-in Middlewares ──────────────────────────────────────────────────


class RateLimitMiddleware:
    """Check GitHub API and daily PR limits before processing."""

    def __init__(self, max_prs_per_day: int = 10):
        self._max = max_prs_per_day

    async def process(self, ctx: PipelineContext, next_mw: MiddlewareChain) -> PipelineContext:
        if ctx.remaining_prs <= 0 and not ctx.dry_run:
            ctx.should_skip = True
            ctx.skip_reason = f"Daily PR limit reached ({self._max})"
            ctx.rate_limited = True
            logger.warning("⏳ %s: %s", ctx.repo_name, ctx.skip_reason)
            return ctx
        return await next_mw(ctx)


class ValidationMiddleware:
    """Validate repo is suitable for contribution."""

    def __init__(self, skip_analyzed: bool = True):
        self._skip_analyzed = skip_analyzed

    async def process(self, ctx: PipelineContext, next_mw: MiddlewareChain) -> PipelineContext:
        if not ctx.repo:
            ctx.should_skip = True
            ctx.skip_reason = "No repo data"
            return ctx
        return await next_mw(ctx)


class RetryMiddleware:
    """Wrap downstream processing with retry logic."""

    def __init__(self, max_retries: int = 2, base_delay: float = 5.0):
        self._max_retries = max_retries
        self._base_delay = base_delay

    async def process(self, ctx: PipelineContext, next_mw: MiddlewareChain) -> PipelineContext:
        last_error = None
        for attempt in range(1, self._max_retries + 1):
            try:
                return await next_mw(ctx)
            except Exception as e:
                last_error = e
                if attempt < self._max_retries:
                    delay = self._base_delay * (2 ** (attempt - 1))
                    logger.warning(
                        "⚠️ %s attempt %d failed: %s. Retrying in %.0fs...",
                        ctx.repo_name,
                        attempt,
                        e,
                        delay,
                    )
                    await asyncio.sleep(delay)
        ctx.errors.append(f"All {self._max_retries} attempts failed: {last_error}")
        return ctx


class DCOMiddleware:
    """Auto-compute DCO signoff from authenticated user."""

    async def process(self, ctx: PipelineContext, next_mw: MiddlewareChain) -> PipelineContext:
        user = ctx.metadata.get("user")
        if user:
            name = user.get("name") or user.get("login", "")
            email = user.get("email")
            if not email:
                uid = user.get("id", "")
                login = user.get("login", "")
                email = f"{uid}+{login}@users.noreply.github.com"
            if name:
                ctx.signoff = f"{name} <{email}>"
                ctx.dco_required = True
        return await next_mw(ctx)


class QualityGateMiddleware:
    """Check contribution quality before PR creation."""

    def __init__(self, min_score: float = 5.0):
        self._min_score = min_score

    async def process(self, ctx: PipelineContext, next_mw: MiddlewareChain) -> PipelineContext:
        result = await next_mw(ctx)
        if result.quality_score > 0 and result.quality_score < self._min_score:
            result.quality_passed = False
            logger.info(
                "🚫 %s: Quality score %.1f < %.1f threshold",
                result.repo_name,
                result.quality_score,
                self._min_score,
            )
        return result


# ── Factory ───────────────────────────────────────────────────────────────


def build_default_chain(
    max_prs_per_day: int = 10,
    max_retries: int = 2,
    min_quality_score: float = 5.0,
) -> list[Middleware]:
    """Build the default middleware chain."""
    return [
        RateLimitMiddleware(max_prs_per_day),
        ValidationMiddleware(),
        RetryMiddleware(max_retries),
        DCOMiddleware(),
        QualityGateMiddleware(min_quality_score),
    ]
