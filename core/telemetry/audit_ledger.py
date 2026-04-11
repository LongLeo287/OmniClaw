#!/usr/bin/env python3
"""
[OER] Core Audit Ledger
======================================================
Mission: 
  1. Hash-chain implementation for OmniClaw's event bus.
  2. Maintain immutable JSONL logs to meet Pillar 5 specifications.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_EVENT_BUS_PATH = REPO_ROOT / "core" / "telemetry" / "event_bus.db"
DEFAULT_LEDGER_PATH = REPO_ROOT / "vault" / "archives" / "audit.jsonl"
DEFAULT_STATE_PATH = REPO_ROOT / "vault" / "archives" / "audit_ledger_state.json"
GENESIS_HASH = "0" * 64


class LedgerIntegrityError(RuntimeError):
    """Raised when the audit ledger has been tampered with or is malformed."""


@dataclass(frozen=True)
class LedgerState:
    last_event_id: int = 0
    last_hash: str = GENESIS_HASH


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_json(payload: dict[str, Any]) -> str:
    return json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _sha256_hex(raw: str) -> str:
    return hashlib.sha256(raw.encode("utf-8")).hexdigest()


def _decode_payload(raw_payload: str) -> Any:
    try:
        return json.loads(raw_payload)
    except json.JSONDecodeError:
        return {"raw": raw_payload}


def _read_last_nonempty_line(path: Path) -> str | None:
    if not path.exists() or path.stat().st_size == 0:
        return None

    with path.open("rb") as handle:
        handle.seek(0, 2)
        position = handle.tell()
        buffer = bytearray()

        while position > 0:
            position -= 1
            handle.seek(position)
            chunk = handle.read(1)
            if chunk == b"\n":
                if buffer:
                    break
                continue
            buffer.extend(chunk)

    return bytes(reversed(buffer)).decode("utf-8")


class AuditLedger:
    """Exports immutable audit records from the event bus into a hash-chained JSONL ledger."""

    def __init__(
        self,
        event_bus_path: Path | str = DEFAULT_EVENT_BUS_PATH,
        ledger_path: Path | str = DEFAULT_LEDGER_PATH,
        state_path: Path | str = DEFAULT_STATE_PATH,
    ) -> None:
        self.event_bus_path = Path(event_bus_path)
        self.ledger_path = Path(ledger_path)
        self.state_path = Path(state_path)

    def load_state(self) -> LedgerState:
        if self.state_path.exists():
            payload = json.loads(self.state_path.read_text(encoding="utf-8"))
            return LedgerState(
                last_event_id=int(payload.get("last_event_id", 0)),
                last_hash=str(payload.get("last_hash", GENESIS_HASH)),
            )

        ledger_tail = self._read_last_record()
        if ledger_tail is None:
            return LedgerState()

        return LedgerState(
            last_event_id=int(ledger_tail["event_id"]),
            last_hash=str(ledger_tail["signature"]),
        )

    def save_state(self, state: LedgerState) -> None:
        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "last_event_id": state.last_event_id,
            "last_hash": state.last_hash,
            "updated_at": _utc_now_iso(),
        }
        self.state_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    def verify(self) -> tuple[int, str]:
        if not self.ledger_path.exists():
            return 0, GENESIS_HASH

        previous_hash = GENESIS_HASH
        record_count = 0

        with self.ledger_path.open("r", encoding="utf-8") as handle:
            for line_number, raw_line in enumerate(handle, start=1):
                line = raw_line.strip()
                if not line:
                    continue
                try:
                    record = json.loads(line)
                except json.JSONDecodeError as exc:
                    raise LedgerIntegrityError(f"Invalid JSON on line {line_number}") from exc

                expected_prev_hash = record.get("prev_hash")
                if expected_prev_hash != previous_hash:
                    raise LedgerIntegrityError(
                        f"Broken hash chain at line {line_number}: expected prev_hash {previous_hash}, got {expected_prev_hash}"
                    )

                signature = record.get("signature")
                if not isinstance(signature, str):
                    raise LedgerIntegrityError(f"Missing signature on line {line_number}")

                unsigned_record = dict(record)
                unsigned_record.pop("signature", None)
                expected_signature = _sha256_hex(_canonical_json(unsigned_record))
                if signature != expected_signature:
                    raise LedgerIntegrityError(
                        f"Signature mismatch on line {line_number}: expected {expected_signature}, got {signature}"
                    )

                previous_hash = signature
                record_count += 1

        return record_count, previous_hash

    def sync(self, *, limit: int | None = None) -> int:
        self.verify()
        state = self.load_state()
        rows = self._fetch_events_after(state.last_event_id, limit=limit)
        if not rows:
            return 0

        self.ledger_path.parent.mkdir(parents=True, exist_ok=True)
        previous_hash = state.last_hash
        last_event_id = state.last_event_id

        with self.ledger_path.open("a", encoding="utf-8", newline="\n") as handle:
            for row in rows:
                record = self._build_record(row=row, prev_hash=previous_hash)
                handle.write(_canonical_json(record) + "\n")
                previous_hash = record["signature"]
                last_event_id = int(row["id"])

        self.save_state(LedgerState(last_event_id=last_event_id, last_hash=previous_hash))
        return len(rows)

    def _build_record(self, *, row: sqlite3.Row, prev_hash: str) -> dict[str, Any]:
        unsigned_record = {
            "event_id": int(row["id"]),
            "topic": row["topic"],
            "status": row["status"],
            "created_at": row["created_at"],
            "picked_by": row["picked_by"],
            "exported_at": _utc_now_iso(),
            "prev_hash": prev_hash,
            "payload": _decode_payload(row["payload"]),
        }
        signature = _sha256_hex(_canonical_json(unsigned_record))
        return {**unsigned_record, "signature": signature}

    def _fetch_events_after(self, event_id: int, *, limit: int | None = None) -> list[sqlite3.Row]:
        if not self.event_bus_path.exists():
            raise FileNotFoundError(f"Event bus database not found: {self.event_bus_path}")

        query = """
            SELECT id, topic, payload, status, created_at, picked_by
            FROM events
            WHERE id > ?
            ORDER BY id ASC
        """
        params: list[Any] = [event_id]
        if limit is not None:
            query += " LIMIT ?"
            params.append(limit)

        with sqlite3.connect(self.event_bus_path) as connection:
            connection.row_factory = sqlite3.Row
            return list(connection.execute(query, params))

    def _read_last_record(self) -> dict[str, Any] | None:
        tail = _read_last_nonempty_line(self.ledger_path)
        if tail is None:
            return None
        try:
            return json.loads(tail)
        except json.JSONDecodeError as exc:
            raise LedgerIntegrityError("The last ledger record is not valid JSON") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Append event bus records into a hash-chained JSONL audit ledger.")
    parser.add_argument("--event-bus", default=str(DEFAULT_EVENT_BUS_PATH), help="Path to event_bus.db")
    parser.add_argument("--ledger", default=str(DEFAULT_LEDGER_PATH), help="Path to audit.jsonl")
    parser.add_argument("--state", default=str(DEFAULT_STATE_PATH), help="Path to ledger cursor/state JSON")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of events to export in this run")
    parser.add_argument("--verify", action="store_true", help="Verify ledger integrity without exporting new rows")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    ledger = AuditLedger(event_bus_path=args.event_bus, ledger_path=args.ledger, state_path=args.state)

    if args.verify:
        count, last_hash = ledger.verify()
        print(f"Ledger OK: {count} records, tip={last_hash}")
        return 0

    appended = ledger.sync(limit=args.limit)
    print(f"Ledger sync complete: appended {appended} record(s) to {ledger.ledger_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
