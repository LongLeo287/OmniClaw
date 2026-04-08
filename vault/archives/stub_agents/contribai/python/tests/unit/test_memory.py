"""Tests for the memory system."""

import pytest

from contribai.orchestrator.memory import Memory


@pytest.fixture
async def memory(tmp_path):
    mem = Memory(tmp_path / "test.db")
    await mem.init()
    yield mem
    await mem.close()


class TestMemory:
    @pytest.mark.asyncio
    async def test_record_and_check_analysis(self, memory):
        assert not await memory.has_analyzed("owner/repo")
        await memory.record_analysis("owner/repo", "python", 500, 5)
        assert await memory.has_analyzed("owner/repo")

    @pytest.mark.asyncio
    async def test_get_analyzed_repos(self, memory):
        await memory.record_analysis("a/b", "python", 100, 2)
        await memory.record_analysis("c/d", "javascript", 200, 3)
        repos = await memory.get_analyzed_repos()
        assert len(repos) == 2

    @pytest.mark.asyncio
    async def test_record_and_get_prs(self, memory):
        await memory.record_pr(
            repo="owner/repo",
            pr_number=42,
            pr_url="https://github.com/owner/repo/pull/42",
            title="Fix: security issue",
            pr_type="security_fix",
        )
        prs = await memory.get_prs()
        assert len(prs) == 1
        assert prs[0]["pr_number"] == 42

    @pytest.mark.asyncio
    async def test_update_pr_status(self, memory):
        await memory.record_pr("a/b", 1, "url", "title", "fix")
        await memory.update_pr_status("a/b", 1, "merged")
        prs = await memory.get_prs(status="merged")
        assert len(prs) == 1

    @pytest.mark.asyncio
    async def test_run_log(self, memory):
        run_id = await memory.start_run()
        assert run_id is not None
        await memory.finish_run(run_id, repos_analyzed=3, prs_created=2, findings=10, errors=1)
        stats = await memory.get_stats()
        assert stats["total_runs"] == 1

    @pytest.mark.asyncio
    async def test_stats_empty(self, memory):
        stats = await memory.get_stats()
        assert stats["total_repos_analyzed"] == 0
        assert stats["total_prs_submitted"] == 0
        assert stats["prs_merged"] == 0
        assert stats["total_runs"] == 0

    @pytest.mark.asyncio
    async def test_today_pr_count(self, memory):
        assert await memory.get_today_pr_count() == 0
        await memory.record_pr("a/b", 1, "url", "title", "fix")
        assert await memory.get_today_pr_count() == 1
