import sqlite3
import json
import datetime
import os
import threading
from pathlib import Path

# Dynamic path: use AOS_ROOT env var or calculate from current file
_AOS_ROOT = os.getenv("OMNICLAW_ROOT") or str(Path(__file__).resolve().parents[3])
DB_PATH = os.path.join(_AOS_ROOT, "brain", "shared-context", "event_bus.db")

class AgentBus:
    def __init__(self):
        os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        self._lock = threading.Lock()
        self._local = threading.local()
        self._init_db()

    def _get_conn(self):
        conn = getattr(self._local, "conn", None)
        if conn is None:
            conn = sqlite3.connect(DB_PATH, check_same_thread=False)
            self._local.conn = conn
        return conn

    def _init_db(self):
        conn = self._get_conn()
        conn.execute('''
            CREATE TABLE IF NOT EXISTS events (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                topic TEXT NOT NULL,
                payload TEXT NOT NULL,
                status TEXT DEFAULT 'PENDING',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                picked_by TEXT
            )
        ''')
        conn.commit()

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
        query = f"SELECT id, topic, payload FROM events WHERE status='PENDING' AND topic IN ({placeholders}) ORDER BY created_at ASC"

        with self._lock:
            conn = self._get_conn()
            rows = conn.execute(query, topics).fetchall()

            events = []
            for row in rows:
                event_id, topic, payload_str = row
                conn.execute("UPDATE events SET status='PROCESSING', picked_by=? WHERE id=?", (agent_id, event_id))
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
            conn.execute("UPDATE events SET status='COMPLETED' WHERE id=?", (event_id,))
            conn.commit()

    def mark_failed(self, event_id):
        with self._lock:
            conn = self._get_conn()
            conn.execute("UPDATE events SET status='FAILED' WHERE id=?", (event_id,))
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
