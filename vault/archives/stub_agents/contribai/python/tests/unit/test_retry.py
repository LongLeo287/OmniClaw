"""Tests for retry utilities and LRU cache."""

import pytest

from contribai.core.retry import LRUCache, async_retry


class TestAsyncRetry:
    @pytest.mark.asyncio
    async def test_succeeds_first_try(self):
        call_count = 0

        @async_retry(max_retries=3, base_delay=0.01, retryable_exceptions=(Exception,))
        async def success():
            nonlocal call_count
            call_count += 1
            return "ok"

        result = await success()
        assert result == "ok"
        assert call_count == 1

    @pytest.mark.asyncio
    async def test_retries_on_failure(self):
        call_count = 0

        @async_retry(max_retries=3, base_delay=0.01, retryable_exceptions=(ValueError,))
        async def fail_twice():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("temporary")
            return "ok"

        result = await fail_twice()
        assert result == "ok"
        assert call_count == 3

    @pytest.mark.asyncio
    async def test_raises_after_max_retries(self):
        @async_retry(max_retries=2, base_delay=0.01, retryable_exceptions=(ValueError,))
        async def always_fail():
            raise ValueError("permanent")

        with pytest.raises(ValueError, match="permanent"):
            await always_fail()

    @pytest.mark.asyncio
    async def test_non_retryable_raises_immediately(self):
        call_count = 0

        @async_retry(
            max_retries=3,
            base_delay=0.01,
            retryable_exceptions=(ValueError,),
            non_retryable_exceptions=(TypeError,),
        )
        async def type_error():
            nonlocal call_count
            call_count += 1
            raise TypeError("not retryable")

        with pytest.raises(TypeError):
            await type_error()
        assert call_count == 1  # No retries


class TestLRUCache:
    def test_put_and_get(self):
        cache = LRUCache(max_size=3)
        cache.put("a", 1)
        assert cache.get("a") == 1

    def test_miss_returns_none(self):
        cache = LRUCache(max_size=3)
        assert cache.get("missing") is None

    def test_eviction(self):
        cache = LRUCache(max_size=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.put("c", 3)  # evicts "a"
        assert cache.get("a") is None
        assert cache.get("b") == 2
        assert cache.get("c") == 3

    def test_access_refreshes_order(self):
        cache = LRUCache(max_size=2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")  # refresh "a"
        cache.put("c", 3)  # should evict "b", not "a"
        assert cache.get("a") == 1
        assert cache.get("b") is None
        assert cache.get("c") == 3

    def test_clear(self):
        cache = LRUCache(max_size=3)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.clear()
        assert cache.get("a") is None
        assert len(cache._cache) == 0

    def test_stats(self):
        cache = LRUCache(max_size=3)
        cache.put("a", 1)
        cache.get("a")  # hit
        cache.get("b")  # miss
        stats = cache.stats
        assert stats["hits"] == 1
        assert stats["misses"] == 1
        assert stats["size"] == 1

    def test_update_existing_key(self):
        cache = LRUCache(max_size=3)
        cache.put("a", 1)
        cache.put("a", 2)
        assert cache.get("a") == 2
        assert len(cache._cache) == 1

    def test_make_key_deterministic(self):
        cache = LRUCache()
        key1 = cache._make_key("hello", key="value")
        key2 = cache._make_key("hello", key="value")
        assert key1 == key2

    def test_make_key_different_inputs(self):
        cache = LRUCache()
        key1 = cache._make_key("hello")
        key2 = cache._make_key("world")
        assert key1 != key2
