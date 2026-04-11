from __future__ import annotations

import argparse
import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parent
EVENT_BUS_PATH = REPO_ROOT / "core" / "telemetry" / "event_bus.db"
BLACKBOARD_PATH = REPO_ROOT / "brain" / "memory" / "blackboard.json"
ALLOWED_STATUSES = {"PENDING", "PROCESSING", "IN_REVIEW", "DONE", "FAILED"}


def _now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _load_blackboard() -> dict[str, Any]:
    if BLACKBOARD_PATH.exists():
        return json.loads(BLACKBOARD_PATH.read_text(encoding="utf-8"))
    return {"system_cycle_status": "IDLE", "handoff_trigger": "IDLE", "open_items": [], "review_queue": []}


def _save_blackboard(payload: dict[str, Any]) -> None:
    BLACKBOARD_PATH.parent.mkdir(parents=True, exist_ok=True)
    BLACKBOARD_PATH.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def ensure_event_bus_schema(db_path: Path = EVENT_BUS_PATH) -> None:
    db_path.parent.mkdir(parents=True, exist_ok=True)
    with sqlite3.connect(db_path) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                payload TEXT NOT NULL,
                status TEXT DEFAULT 'PENDING',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                picked_by TEXT
            )
            """
        )
        columns = {row[1] for row in cursor.execute("PRAGMA table_info(events)")}
        additions = {
            "review_started_at": "TEXT",
            "completed_at": "TEXT",
            "approved_by": "TEXT",
            "approved_at": "TEXT",
            "approval_note": "TEXT",
        }
        for column_name, column_type in additions.items():
            if column_name not in columns:
                cursor.execute(f"ALTER TABLE events ADD COLUMN {column_name} {column_type}")
        connection.commit()


def create_event(topic: str, payload: dict[str, Any], *, status: str = "PENDING", picked_by: str | None = None) -> int:
    ensure_event_bus_schema()
    if status not in ALLOWED_STATUSES:
        raise ValueError(f"Unsupported status: {status}")
    with sqlite3.connect(EVENT_BUS_PATH) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
            INSERT INTO events (topic, payload, status, created_at, picked_by)
            VALUES (?, ?, ?, ?, ?)
            """,
            (topic, json.dumps(payload, ensure_ascii=False), status, _now(), picked_by),
        )
        connection.commit()
        return int(cursor.lastrowid)


def _event_row(event_id: int) -> sqlite3.Row:
    ensure_event_bus_schema()
    with sqlite3.connect(EVENT_BUS_PATH) as connection:
        connection.row_factory = sqlite3.Row
        row = connection.execute("SELECT * FROM events WHERE id = ?", (event_id,)).fetchone()
        if row is None:
            raise KeyError(f"Event not found: {event_id}")
        return row


def mark_in_review(event_id: int, *, picked_by: str | None = None, note: str | None = None) -> None:
    ensure_event_bus_schema()
    with sqlite3.connect(EVENT_BUS_PATH) as connection:
        connection.execute(
            """
            UPDATE events
            SET status = 'IN_REVIEW',
                review_started_at = ?,
                picked_by = COALESCE(?, picked_by),
                approval_note = COALESCE(?, approval_note)
            WHERE id = ?
            """,
            (_now(), picked_by, note, event_id),
        )
        connection.commit()


def approve_event(event_id: int, *, approved_by: str, note: str | None = None) -> None:
    if approved_by.strip().upper() != "CEO":
        raise PermissionError("DONE can only be written by Human approval: approved_by must be CEO")

    ensure_event_bus_schema()
    with sqlite3.connect(EVENT_BUS_PATH) as connection:
        connection.execute(
            """
            UPDATE events
            SET status = 'DONE',
                approved_by = ?,
                approved_at = ?,
                completed_at = ?,
                approval_note = COALESCE(?, approval_note)
            WHERE id = ?
            """,
            (approved_by, _now(), _now(), note, event_id),
        )
        connection.commit()


def sync_blackboard_task(
    task_id: str,
    *,
    status: str,
    summary: str,
    agent_id: str | None = None,
    approved_by: str | None = None,
    note: str | None = None,
) -> None:
    payload = _load_blackboard()
    review_queue = payload.setdefault("review_queue", [])
    open_items = payload.setdefault("open_items", [])
    timestamp = _now()

    card = next((item for item in review_queue if item.get("task_id") == task_id), None)
    if card is None:
        card = {"task_id": task_id}
        review_queue.append(card)

    card.update(
        {
            "status": status,
            "summary": summary,
            "agent_id": agent_id,
            "updated_at": timestamp,
        }
    )

    if status == "IN_REVIEW":
        card["submitted_for_review_at"] = timestamp
        payload["handoff_trigger"] = "IN_REVIEW"
        open_items[:] = [item for item in open_items if item.get("task_id") != task_id]
        open_items.append({"task_id": task_id, "status": status, "summary": summary, "agent_id": agent_id})
    elif status == "DONE":
        card["approved_by"] = approved_by
        card["approved_at"] = timestamp
        if note:
            card["approval_note"] = note
        payload["handoff_trigger"] = "COMPLETE"
        open_items[:] = [item for item in open_items if item.get("task_id") != task_id]

    payload["blackboard_updated_at"] = timestamp
    _save_blackboard(payload)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage OmniClaw task review and approval state.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("migrate", help="Ensure the event_bus schema supports review approvals.")

    publish = subparsers.add_parser("publish", help="Create a new event bus task.")
    publish.add_argument("--topic", required=True)
    publish.add_argument("--payload", required=True, help="JSON payload")
    publish.add_argument("--status", default="PENDING")
    publish.add_argument("--picked-by", default=None)

    review = subparsers.add_parser("complete", help="Move an event/task into IN_REVIEW.")
    review.add_argument("--event-id", required=True, type=int)
    review.add_argument("--task-id", required=True)
    review.add_argument("--summary", required=True)
    review.add_argument("--agent-id", default=None)
    review.add_argument("--note", default=None)

    approve = subparsers.add_parser("approve", help="Approve an in-review task as CEO.")
    approve.add_argument("--event-id", required=True, type=int)
    approve.add_argument("--task-id", required=True)
    approve.add_argument("--summary", required=True)
    approve.add_argument("--approved-by", required=True)
    approve.add_argument("--note", default=None)
    return parser


def main() -> int:
    args = build_parser().parse_args()

    if args.command == "migrate":
        ensure_event_bus_schema()
        print(f"Event bus schema ready: {EVENT_BUS_PATH}")
        return 0

    if args.command == "publish":
        event_id = create_event(
            topic=args.topic,
            payload=json.loads(args.payload),
            status=args.status,
            picked_by=args.picked_by,
        )
        print(f"Created event {event_id}")
        return 0

    if args.command == "complete":
        mark_in_review(args.event_id, picked_by=args.agent_id, note=args.note)
        sync_blackboard_task(
            args.task_id,
            status="IN_REVIEW",
            summary=args.summary,
            agent_id=args.agent_id,
            note=args.note,
        )
        print(f"Task {args.task_id} moved to IN_REVIEW")
        return 0

    if args.command == "approve":
        approve_event(args.event_id, approved_by=args.approved_by, note=args.note)
        sync_blackboard_task(
            args.task_id,
            status="DONE",
            summary=args.summary,
            approved_by=args.approved_by,
            note=args.note,
        )
        print(f"Task {args.task_id} approved by {args.approved_by}")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
