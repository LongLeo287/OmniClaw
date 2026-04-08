"""Tests for contribai.core.middleware — Middleware chain system."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest

from contribai.core.middleware import (
    DCOMiddleware,
    MiddlewareChain,
    PipelineContext,
    QualityGateMiddleware,
    RateLimitMiddleware,
    RetryMiddleware,
    ValidationMiddleware,
    build_default_chain,
)


class TestPipelineContext:
    """Tests for PipelineContext dataclass."""

    def test_defaults(self):
        ctx = PipelineContext()
        assert ctx.repo_name == ""
        assert ctx.should_skip is False
        assert ctx.metadata == {}
        assert ctx.errors == []
        assert ctx.dry_run is False
        assert ctx.remaining_prs == 10
        assert ctx.quality_passed is True

    def test_custom_values(self):
        ctx = PipelineContext(
            repo_name="foo/bar",
            should_skip=True,
            skip_reason="test",
            metadata={"key": "val"},
            errors=["err1"],
        )
        assert ctx.should_skip is True
        assert ctx.skip_reason == "test"
        assert ctx.metadata["key"] == "val"
        assert len(ctx.errors) == 1

    def test_dco_fields(self):
        ctx = PipelineContext(
            signoff="User <user@email.com>",
            dco_required=True,
        )
        assert ctx.signoff == "User <user@email.com>"
        assert ctx.dco_required is True

    def test_quality_fields(self):
        ctx = PipelineContext(quality_score=7.5, quality_passed=True)
        assert ctx.quality_score == 7.5


class TestRateLimitMiddleware:
    """Tests for RateLimitMiddleware."""

    @pytest.fixture
    def mw(self):
        return RateLimitMiddleware(max_prs_per_day=10)

    @pytest.mark.asyncio
    async def test_passes_under_limit(self, mw):
        ctx = PipelineContext(repo_name="owner/repo", remaining_prs=5)
        # Create chain with just rate limit (wraps empty chain)
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.should_skip is False

    @pytest.mark.asyncio
    async def test_blocks_at_zero(self):
        mw = RateLimitMiddleware(max_prs_per_day=2)
        ctx = PipelineContext(repo_name="owner/repo", remaining_prs=0)
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.should_skip is True
        assert result.rate_limited is True


class TestValidationMiddleware:
    """Tests for ValidationMiddleware."""

    @pytest.mark.asyncio
    async def test_passes_with_repo(self):
        mw = ValidationMiddleware()
        ctx = PipelineContext(repo_name="owner/repo", repo=MagicMock())
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.should_skip is False

    @pytest.mark.asyncio
    async def test_fails_without_repo(self):
        mw = ValidationMiddleware()
        ctx = PipelineContext(repo_name="owner/repo", repo=None)
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.should_skip is True
        assert "No repo" in result.skip_reason


class TestRetryMiddleware:
    """Tests for RetryMiddleware."""

    @pytest.mark.asyncio
    async def test_passes_through(self):
        mw = RetryMiddleware(max_retries=2, base_delay=0.01)
        ctx = PipelineContext(repo_name="owner/repo")
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.repo_name == "owner/repo"


class TestDCOMiddleware:
    """Tests for DCOMiddleware."""

    @pytest.mark.asyncio
    async def test_sets_signoff(self):
        mw = DCOMiddleware()
        ctx = PipelineContext(
            repo_name="owner/repo",
            metadata={
                "user": {
                    "name": "Test User",
                    "email": "test@example.com",
                    "login": "testuser",
                    "id": 123,
                }
            },
        )
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.signoff == "Test User <test@example.com>"
        assert result.dco_required is True

    @pytest.mark.asyncio
    async def test_generates_noreply_email(self):
        mw = DCOMiddleware()
        ctx = PipelineContext(
            repo_name="owner/repo",
            metadata={"user": {"name": "Test", "login": "testuser", "id": 123}},
        )
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert "noreply.github.com" in result.signoff

    @pytest.mark.asyncio
    async def test_no_user_no_signoff(self):
        mw = DCOMiddleware()
        ctx = PipelineContext(repo_name="owner/repo")
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.signoff is None


class TestQualityGateMiddleware:
    """Tests for QualityGateMiddleware."""

    @pytest.mark.asyncio
    async def test_passes_default(self):
        mw = QualityGateMiddleware(min_score=5.0)
        ctx = PipelineContext(repo_name="owner/repo", quality_score=0.0)
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.quality_passed is True  # score=0 means not yet scored

    @pytest.mark.asyncio
    async def test_fails_low_score(self):
        mw = QualityGateMiddleware(min_score=5.0)
        ctx = PipelineContext(repo_name="owner/repo", quality_score=3.0)
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.quality_passed is False

    @pytest.mark.asyncio
    async def test_passes_high_score(self):
        mw = QualityGateMiddleware(min_score=5.0)
        ctx = PipelineContext(repo_name="owner/repo", quality_score=8.0)
        chain = MiddlewareChain([mw])
        result = await chain(ctx)
        assert result.quality_passed is True


class TestMiddlewareChain:
    """Tests for MiddlewareChain."""

    @pytest.mark.asyncio
    async def test_runs_all_middlewares(self):
        mw_list = [
            RateLimitMiddleware(10),
            DCOMiddleware(),
        ]
        ctx = PipelineContext(
            repo_name="test",
            remaining_prs=5,
            metadata={"user": {"name": "User", "email": "u@e.com", "login": "u", "id": 1}},
        )
        chain = MiddlewareChain(mw_list)
        result = await chain(ctx)
        assert result.signoff is not None

    @pytest.mark.asyncio
    async def test_stops_on_skip(self):
        """When rate limit blocks, downstream middlewares don't run."""
        mw_list = [
            RateLimitMiddleware(10),
            DCOMiddleware(),
        ]
        ctx = PipelineContext(repo_name="test", remaining_prs=0)
        chain = MiddlewareChain(mw_list)
        result = await chain(ctx)
        assert result.should_skip is True
        assert result.signoff is None  # DCO didn't run

    @pytest.mark.asyncio
    async def test_empty_chain(self):
        chain = MiddlewareChain([])
        ctx = PipelineContext(repo_name="test")
        result = await chain(ctx)
        assert result.repo_name == "test"


class TestBuildDefaultChain:
    """Tests for build_default_chain factory."""

    def test_returns_list(self):
        chain = build_default_chain()
        assert isinstance(chain, list)
        assert len(chain) == 5

    def test_creates_middleware_chain(self):
        mw_list = build_default_chain()
        chain = MiddlewareChain(mw_list)
        assert isinstance(chain, MiddlewareChain)

    def test_custom_params(self):
        chain = build_default_chain(max_prs_per_day=5, max_retries=3, min_quality_score=7.0)
        assert len(chain) == 5
