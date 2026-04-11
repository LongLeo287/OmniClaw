import sqlite3
import json
import datetime
import os
import threading
from pathlib import Path

# Dynamic path: use AOS_ROOT env var or calculate from current file
_AOS_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[3])
DB_PATH = os.path.join(_AOS_ROOT, "brain", "shared-context", "event_bus.db")
CLAIM_LIMIT = max(1, int(os.getenv("OMNICLAW_EVENT_CLAIM_LIMIT", "25")))
LEASE_SECONDS = max(30, int(os.getenv("OMNICLAW_EVENT_LEASE_SECONDS", "900")))

class AgentBus:
    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self._lock = threading.Lock()
        self._local = threading.local()
        self._init_db()

    def _get_conn(self):
        conn = getattr(self._local, "conn", None)
        if conn is None:
            conn = sqlite3.connect(DB_PATH, check_same_thread=False, timeout=30)
            conn.execute("PRAGMA busy_timeout = 30000")
            conn.execute("PRAGMA journal_mode = WAL")
            conn.execute("PRAGMA synchronous = NORMAL")
            self._local.conn = conn
        return conn

    def _ensure_column(self, conn, column_name, column_sql):
        columns = {row[1] for row in conn.execute("PRAGMA table_info(events)").fetchall()}
        if column_name not in columns:
            conn.execute(f"ALTER TABLE events ADD COLUMN {column_sql}")

    def _init_db(self):
        conn = self._get_conn()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                payload TEXT NOT NULL,
                status TEXT DEFAULT 'PENDING',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                picked_by TEXT,
                processing_started_at TIMESTAMP
            )
        ''')
        self._ensure_column(conn, "processing_started_at", "processing_started_at TIMESTAMP")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_events_status_topic_created ON events(status, topic, created_at)")
        conn.execute("CREATE INDEX IF NOT EXISTS idx_events_processing_started ON events(status, processing_started_at)")
        conn.commit()

    def _requeue_stale_processing(self, conn):
        lease_cutoff = f"-{LEASE_SECONDS} seconds"
        conn.execute(
            """
            UPDATE events
            SET status='PENDING', picked_by=NULL, processing_started_at=NULL
            WHERE status='PROCESSING'
              AND processing_started_at IS NOT NULL
              AND processing_started_at < datetime('now', ?)
            """,
            (lease_cutoff,),
        )

    def publish(self, topic, payload_dict):
        """Publish signal to Bus. Payload is Dict."""
        payload_str = json.dumps(payload_dict, ensure_ascii=False)
        with self._lock:
            conn = self._get_conn()
            cursor = conn.execute(
                "INSERT INTO events (topic, payload) VALUES (?, ?)",
                (topic, payload_str)
            )
            conn.commit()
            return cursor.lastrowid

    def poll(self, topics, agent_id="unknown"):
        """Agent polls Bus for work (PENDING only)."""
        if not topics:
            return []
        placeholders = ','.join('?' * len(topics))
        query = (
            f"SELECT id, topic, payload FROM events "
            f"WHERE status='PENDING' AND topic IN ({placeholders}) "
            f"ORDER BY created_at ASC LIMIT ?"
        )

        with self._lock:
            conn = self._get_conn()
            conn.execute("BEGIN IMMEDIATE")
            self._requeue_stale_processing(conn)
            rows = conn.execute(query, [*topics, CLAIM_LIMIT]).fetchall()

            events = []
            for row in rows:
                event_id, topic, payload_str = row
                cursor = conn.execute(
                    """
                    UPDATE events
                    SET status='PROCESSING',
                        picked_by=?,
                        processing_started_at=CURRENT_TIMESTAMP
                    WHERE id=? AND status='PENDING'
                    """,
                    (agent_id, event_id),
                )
                if cursor.rowcount != 1:
                    continue
                events.append({
                    "id": event_id,
                    "topic": topic,
                    "payload": json.loads(payload_str)
                })
            conn.commit()
        return events

    def mark_completed(self, event_id):
        with self._lock:
            conn = self._get_conn()
            conn.execute(
                "UPDATE events SET status='COMPLETED', picked_by=NULL, processing_started_at=NULL WHERE id=?",
                (event_id,),
            )
            conn.commit()

    def mark_failed(self, event_id):
        with self._lock:
            conn = self._get_conn()
            conn.execute(
                "UPDATE events SET status='FAILED', processing_started_at=NULL WHERE id=?",
                (event_id,),
            )
            conn.commit()

    def get_pending_count(self):
        conn = self._get_conn()
        return conn.execute("SELECT COUNT(*) FROM events WHERE status='PENDING'").fetchone()[0]

    def clear_completed(self):
        with self._lock:
            conn = self._get_conn()
            conn.execute("DELETE FROM events WHERE status='COMPLETED'")
            conn.commit()

if __name__ == "__main__":
    import sys
    action = sys.argv[1] if len(sys.argv) > 1 else "status"
    bus = AgentBus()

    if action == "publish":
        topic = sys.argv[2]
        payload = sys.argv[3]
        eid = bus.publish(topic, {"task": payload})
        print(f"[PUB] Send successful! EventID={eid}")

    elif action == "status":
        cnt = bus.get_pending_count()
        print(f"[STATUS] Task Bus current: {cnt} PENDING")
        conn = bus._get_conn()
        rows = conn.execute("SELECT id, topic, status, picked_by FROM events ORDER BY id DESC LIMIT 5").fetchall()
        for r in rows:
            print(f"  ID:{r[0]:03d} | Topic:{r[1]:<15} | Status:{r[2]:<10} | Agent:{r[3]}")
