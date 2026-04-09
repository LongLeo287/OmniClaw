"""Tests for P3: Event-Stream Architecture."""

from __future__ import annotations

import tempfile
from pathlib import Path

import pytest

from contribai.core.events import Event, EventBus, EventType, FileEventLogger


@pytest.fixture
def event_bus():
    return EventBus(max_history=100)


class TestEvent:
    def test_event_creation(self):
        event = Event(type=EventType.PR_CREATED, data={"url": "https://example.com"})
        assert event.type == EventType.PR_CREATED
        assert event.data["url"] == "https://example.com"
        assert event.timestamp
        assert event.event_id

    def test_event_to_dict(self):
        event = Event(type=EventType.ANALYSIS_COMPLETE, source="analyzer")
        d = event.to_dict()
        assert d["type"] == "analysis.complete"
        assert d["source"] == "analyzer"

    def test_event_to_json(self):
        event = Event(type=EventType.PIPELINE_START)
        j = event.to_json()
        assert '"pipeline.start"' in j


class TestEventBus:
    @pytest.mark.asyncio
    async def test_emit_and_subscribe(self, event_bus):
        received = []

        async def handler(event):
            received.append(event)

        event_bus.subscribe(EventType.PR_CREATED, handler)
        await event_bus.emit(Event(type=EventType.PR_CREATED, data={"pr": 1}))
        assert len(received) == 1
        assert received[0].data["pr"] == 1

    @pytest.mark.asyncio
    async def test_subscribe_all(self, event_bus):
        received = []

        async def handler(event):
            received.append(event)

        event_bus.subscribe_all(handler)
        await event_bus.emit(Event(type=EventType.PR_CREATED))
        await event_bus.emit(Event(type=EventType.ANALYSIS_COMPLETE))
        assert len(received) == 2

    @pytest.mark.asyncio
    async def test_history(self, event_bus):
        await event_bus.emit(Event(type=EventType.PR_CREATED))
        await event_bus.emit(Event(type=EventType.ANALYSIS_COMPLETE))
        await event_bus.emit(Event(type=EventType.PR_MERGED))

        history = event_bus.history()
        assert len(history) == 3

        pr_history = event_bus.history(event_type=EventType.PR_CREATED)
        assert len(pr_history) == 1

    @pytest.mark.asyncio
    async def test_history_max_limit(self):
        bus = EventBus(max_history=5)
        for i in range(10):
            await bus.emit(Event(type=EventType.PIPELINE_START, data={"i": i}))
        assert len(bus.history(limit=100)) == 5

    @pytest.mark.asyncio
    async def test_handler_error_doesnt_crash(self, event_bus):
        async def bad_handler(event):
            raise ValueError("boom")

        event_bus.subscribe(EventType.PR_CREATED, bad_handler)
        # Should not raise
        await event_bus.emit(Event(type=EventType.PR_CREATED))

    def test_clear_history(self, event_bus):
        event_bus.clear_history()
        assert len(event_bus.history()) == 0


class TestFileEventLogger:
    @pytest.mark.asyncio
    async def test_file_logger_writes_jsonl(self):
        with tempfile.TemporaryDirectory() as tmp:
            log_path = Path(tmp) / "events.jsonl"
            logger = FileEventLogger(log_path)
            await logger.handle(Event(type=EventType.PR_CREATED, data={"num": 42}))
            await logger.handle(Event(type=EventType.PIPELINE_COMPLETE))

            lines = log_path.read_text().strip().split("\n")
            assert len(lines) == 2
            assert '"pr.created"' in lines[0]
            assert '"pipeline.complete"' in lines[1]
