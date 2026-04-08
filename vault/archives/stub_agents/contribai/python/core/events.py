"""Event-stream architecture for observable pipeline execution.

Inspired by OpenHands' event-stream pattern — all pipeline actions are
modeled as events that can be subscribed to, logged, and replayed.
"""

from __future__ import annotations

import json
import logging
from collections import defaultdict
from collections.abc import Callable, Coroutine
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)


class EventType(StrEnum):
    """Pipeline event types."""

    # Discovery
    DISCOVERY_START = "discovery.start"
    DISCOVERY_COMPLETE = "discovery.complete"

    # Analysis
    ANALYSIS_START = "analysis.start"
    ANALYSIS_COMPLETE = "analysis.complete"

    # Generation
    GENERATION_START = "generation.start"
    GENERATION_COMPLETE = "generation.complete"

    # PR lifecycle
    PR_CREATED = "pr.created"
    PR_CLOSED = "pr.closed"
    PR_MERGED = "pr.merged"

    # Pipeline
    PIPELINE_START = "pipeline.start"
    PIPELINE_COMPLETE = "pipeline.complete"
    PIPELINE_ERROR = "pipeline.error"

    # Hunt mode
    HUNT_ROUND_START = "hunt.round_start"
    HUNT_ROUND_COMPLETE = "hunt.round_complete"
    HUNT_REPO_START = "hunt.repo_start"
    HUNT_REPO_COMPLETE = "hunt.repo_complete"
    HUNT_REPO_SKIP = "hunt.repo_skip"

    # Memory
    MEMORY_STORE = "memory.store"
    MEMORY_RECALL = "memory.recall"


@dataclass
class Event:
    """Immutable event emitted by pipeline stages.

    Attributes:
        type: Event type enum.
        data: Arbitrary event payload.
        source: Module/class that emitted the event.
        timestamp: ISO 8601 timestamp.
        event_id: Unique event identifier.
    """

    type: EventType
    data: dict[str, Any] = field(default_factory=dict)
    source: str = ""
    timestamp: str = field(default_factory=lambda: datetime.now(UTC).isoformat())
    event_id: str = field(default_factory=lambda: datetime.now(UTC).strftime("%Y%m%d%H%M%S%f"))

    def to_dict(self) -> dict[str, Any]:
        """Serialize event to dict."""
        d = asdict(self)
        d["type"] = self.type.value
        return d

    def to_json(self) -> str:
        """Serialize event to JSON string."""
        return json.dumps(self.to_dict(), default=str)


# Type alias for event handlers
EventHandler = Callable[[Event], Coroutine[Any, Any, None]]


class EventBus:
    """Central event bus for pipeline observability.

    Supports async subscriber handlers and maintains event history
    for debugging and replay.

    Usage:
        bus = EventBus()
        bus.subscribe(EventType.PR_CREATED, my_handler)
        await bus.emit(Event(type=EventType.PR_CREATED, data={"url": "..."}))
    """

    def __init__(self, max_history: int = 1000):
        self._subscribers: dict[EventType, list[EventHandler]] = defaultdict(list)
        self._global_subscribers: list[EventHandler] = []
        self._history: list[Event] = []
        self._max_history = max_history

    def subscribe(self, event_type: EventType, handler: EventHandler) -> None:
        """Subscribe to a specific event type.

        Args:
            event_type: Type of events to receive.
            handler: Async callable to invoke when event fires.
        """
        self._subscribers[event_type].append(handler)

    def subscribe_all(self, handler: EventHandler) -> None:
        """Subscribe to ALL events.

        Args:
            handler: Async callable to invoke for any event.
        """
        self._global_subscribers.append(handler)

    async def emit(self, event: Event) -> None:
        """Emit an event to all matching subscribers.

        Args:
            event: Event to emit.
        """
        # Store in history
        self._history.append(event)
        if len(self._history) > self._max_history:
            self._history = self._history[-self._max_history :]

        # Notify specific subscribers
        handlers = self._subscribers.get(event.type, []) + self._global_subscribers
        for handler in handlers:
            try:
                await handler(event)
            except Exception:
                logger.exception("Event handler failed for %s", event.type.value)

    def history(
        self,
        event_type: EventType | None = None,
        limit: int = 100,
    ) -> list[Event]:
        """Get event history, optionally filtered by type.

        Args:
            event_type: Filter by type (None = all).
            limit: Max events to return.

        Returns:
            List of events, newest first.
        """
        events = self._history
        if event_type is not None:
            events = [e for e in events if e.type == event_type]
        return list(reversed(events[-limit:]))

    def clear_history(self) -> None:
        """Clear all event history."""
        self._history.clear()


class FileEventLogger:
    """Subscriber that writes events to a JSONL file.

    Usage:
        logger = FileEventLogger(Path("~/.contribai/events.jsonl"))
        bus.subscribe_all(logger.handle)
    """

    def __init__(self, path: Path):
        self._path = Path(path).expanduser()
        self._path.parent.mkdir(parents=True, exist_ok=True)

    async def handle(self, event: Event) -> None:
        """Append event as JSON line to file.

        Args:
            event: Event to log.
        """
        try:
            with open(self._path, "a", encoding="utf-8") as f:
                f.write(event.to_json() + "\n")
        except Exception:
            logger.debug("Failed to write event to %s", self._path, exc_info=True)
