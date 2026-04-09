"""Retry utilities with exponential backoff.

Provides decorators and helpers for resilient API calls
to GitHub and LLM providers.
"""

from __future__ import annotations

import asyncio
import functools
import hashlib
import json
import logging
from collections import OrderedDict
from collections.abc import Callable
from typing import Any

from contribai.core.exceptions import (
    GitHubAPIError,
    LLMError,
    LLMRateLimitError,
    RateLimitError,
)

logger = logging.getLogger(__name__)


def async_retry(
    max_retries: int = 3,
    base_delay: float = 1.0,
    max_delay: float = 60.0,
    backoff_factor: float = 2.0,
    retryable_exceptions: tuple[type[Exception], ...] = (Exception,),
    non_retryable_exceptions: tuple[type[Exception], ...] = (),
):
    """Decorator for async functions with exponential backoff retry.

    Args:
        max_retries: Maximum number of retry attempts.
        base_delay: Initial delay in seconds before first retry.
        max_delay: Maximum delay cap in seconds.
        backoff_factor: Multiplier for delay after each retry.
        retryable_exceptions: Exception types that trigger retry.
        non_retryable_exceptions: Exception types that immediately raise.
    """

    def decorator(func: Callable):
        @functools.wraps(func)
        async def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return await func(*args, **kwargs)
                except non_retryable_exceptions:
                    raise
                except retryable_exceptions as e:
                    last_exception = e
                    if attempt >= max_retries:
                        break

                    delay = min(base_delay * (backoff_factor**attempt), max_delay)
                    # Add jitter (±25%)
                    import random

                    delay *= 0.75 + random.random() * 0.5

                    logger.warning(
                        "Retry %d/%d for %s after %.1fs: %s",
                        attempt + 1,
                        max_retries,
                        func.__name__,
                        delay,
                        str(e)[:100],
                    )
                    await asyncio.sleep(delay)

            raise last_exception  # type: ignore

        return wrapper

    return decorator


def github_retry(func: Callable):
    """Retry decorator optimized for GitHub API calls."""
    return async_retry(
        max_retries=3,
        base_delay=2.0,
        max_delay=60.0,
        retryable_exceptions=(GitHubAPIError, RateLimitError),
        non_retryable_exceptions=(),
    )(func)


def llm_retry(func: Callable):
    """Retry decorator optimized for LLM API calls."""
    return async_retry(
        max_retries=3,
        base_delay=3.0,
        max_delay=60.0,
        retryable_exceptions=(LLMError, LLMRateLimitError),
        non_retryable_exceptions=(),
    )(func)


def rate_limit_retry(func: Callable):
    """Retry decorator specifically for 429 rate limit errors.

    Uses longer delays (10s base, 120s max, 5 retries) because
    Gemini rate limits can last 30-60 seconds during heavy usage.
    """
    return async_retry(
        max_retries=5,
        base_delay=10.0,
        max_delay=120.0,
        backoff_factor=2.0,
        retryable_exceptions=(LLMRateLimitError,),
        non_retryable_exceptions=(),
    )(func)


class LRUCache:
    """Simple async-safe LRU cache for LLM and API responses.

    Uses an OrderedDict to maintain insertion order and evict
    least-recently-used entries when capacity is exceeded.
    """

    def __init__(self, max_size: int = 100):
        self._cache: OrderedDict[str, Any] = OrderedDict()
        self._max_size = max_size
        self._hits = 0
        self._misses = 0

    def _make_key(self, *args, **kwargs) -> str:
        raw = json.dumps({"args": str(args), "kwargs": str(kwargs)}, sort_keys=True)
        return hashlib.sha256(raw.encode()).hexdigest()[:16]

    def get(self, key: str) -> Any | None:
        if key in self._cache:
            self._hits += 1
            self._cache.move_to_end(key)
            return self._cache[key]
        self._misses += 1
        return None

    def put(self, key: str, value: Any):
        if key in self._cache:
            self._cache.move_to_end(key)
        else:
            if len(self._cache) >= self._max_size:
                self._cache.popitem(last=False)
        self._cache[key] = value

    def clear(self):
        self._cache.clear()
        self._hits = 0
        self._misses = 0

    @property
    def stats(self) -> dict:
        total = self._hits + self._misses
        return {
            "hits": self._hits,
            "misses": self._misses,
            "hit_rate": f"{(self._hits / total * 100):.1f}%" if total > 0 else "0%",
            "size": len(self._cache),
            "max_size": self._max_size,
        }


# Global caches
llm_cache = LRUCache(max_size=200)
github_cache = LRUCache(max_size=500)
