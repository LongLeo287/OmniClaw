"""Scheduled pipeline execution using APScheduler.

Supports cron expressions for periodic automated runs
with graceful shutdown and logging.
"""

from __future__ import annotations

import asyncio
import logging
import signal

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

from contribai.core.config import ContribAIConfig
from contribai.orchestrator.pipeline import ContribPipeline

logger = logging.getLogger(__name__)


class ContribScheduler:
    """Scheduler for automated pipeline runs."""

    def __init__(self, config: ContribAIConfig):
        self.config = config
        self._scheduler: AsyncIOScheduler | None = None
        self._running = False

    def _parse_cron(self, cron_expr: str) -> dict:
        """Parse a cron expression into APScheduler kwargs."""
        parts = cron_expr.strip().split()
        if len(parts) != 5:
            raise ValueError(
                f"Invalid cron expression: {cron_expr!r}. "
                "Expected 5 fields: minute hour day month day_of_week"
            )
        return {
            "minute": parts[0],
            "hour": parts[1],
            "day": parts[2],
            "month": parts[3],
            "day_of_week": parts[4],
        }

    async def _run_pipeline(self):
        """Execute a single pipeline run."""
        logger.info("Scheduled pipeline run starting...")
        pipeline = ContribPipeline(self.config)
        try:
            result = await pipeline.run()
            logger.info(
                "Scheduled run complete: %d repos analyzed, %d PRs created, %d errors",
                result.repos_analyzed,
                result.prs_created,
                len(result.errors),
            )
        except Exception:
            logger.exception("Scheduled pipeline run failed")

    def start(self):
        """Start the scheduler (blocking)."""
        sched_config = self.config.scheduler

        if not sched_config.enabled:
            logger.warning("Scheduler is disabled in config. Set scheduler.enabled=true to enable.")
            return

        cron_kwargs = self._parse_cron(sched_config.cron)

        self._scheduler = AsyncIOScheduler(timezone=sched_config.timezone)
        self._scheduler.add_job(
            self._run_pipeline,
            trigger=CronTrigger(**cron_kwargs),
            id="contribai_pipeline",
            name="ContribAI Pipeline Run",
            replace_existing=True,
        )

        # Graceful shutdown
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        def _shutdown(signum, frame):
            logger.info("Received signal %s, shutting down...", signum)
            self._running = False
            if self._scheduler:
                self._scheduler.shutdown(wait=False)

        signal.signal(signal.SIGINT, _shutdown)
        signal.signal(signal.SIGTERM, _shutdown)

        self._scheduler.start()
        self._running = True
        logger.info(
            "Scheduler started with cron: %s (tz: %s)",
            sched_config.cron,
            sched_config.timezone,
        )

        try:
            loop.run_forever()
        except (KeyboardInterrupt, SystemExit):
            logger.info("Scheduler stopped.")
        finally:
            if self._scheduler and self._scheduler.running:
                self._scheduler.shutdown()
            loop.close()

    def stop(self):
        """Stop the scheduler."""
        self._running = False
        if self._scheduler and self._scheduler.running:
            self._scheduler.shutdown()
            logger.info("Scheduler stopped.")
