"""Persistent memory system using SQLite.

Tracks analyzed repos, submitted PRs, and learning data
to avoid duplicate work and improve over time.
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime
from pathlib import Path

import aiosqlite

logger = logging.getLogger(__name__)

SCHEMA = """
CREATE TABLE IF NOT EXISTS analyzed_repos (
    full_name   TEXT PRIMARY KEY,
    language    TEXT,
    stars       INTEGER,
    analyzed_at TEXT,
    findings    INTEGER DEFAULT 0,
    metadata    TEXT DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS submitted_prs (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    repo        TEXT NOT NULL,
    pr_number   INTEGER NOT NULL,
    pr_url      TEXT NOT NULL,
    title       TEXT NOT NULL,
    type        TEXT NOT NULL,
    status      TEXT DEFAULT 'open',
    branch      TEXT,
    fork        TEXT,
    created_at  TEXT,
    updated_at  TEXT,
    UNIQUE(repo, pr_number)
);

CREATE TABLE IF NOT EXISTS findings_cache (
    id          TEXT PRIMARY KEY,
    repo        TEXT NOT NULL,
    type        TEXT NOT NULL,
    severity    TEXT NOT NULL,
    title       TEXT NOT NULL,
    file_path   TEXT,
    status      TEXT DEFAULT 'new',
    created_at  TEXT
);

CREATE TABLE IF NOT EXISTS run_log (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    started_at  TEXT,
    finished_at TEXT,
    repos_analyzed INTEGER DEFAULT 0,
    prs_created  INTEGER DEFAULT 0,
    findings     INTEGER DEFAULT 0,
    errors       INTEGER DEFAULT 0,
    metadata     TEXT DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS pr_outcomes (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    repo        TEXT NOT NULL,
    pr_number   INTEGER NOT NULL,
    pr_url      TEXT NOT NULL,
    pr_type     TEXT NOT NULL,
    outcome     TEXT NOT NULL,
    feedback    TEXT DEFAULT '',
    time_to_close_hours REAL DEFAULT 0,
    recorded_at TEXT,
    UNIQUE(repo, pr_number)
);

CREATE TABLE IF NOT EXISTS repo_preferences (
    repo        TEXT PRIMARY KEY,
    preferred_types TEXT DEFAULT '[]',
    rejected_types  TEXT DEFAULT '[]',
    merge_rate  REAL DEFAULT 0.0,
    avg_review_hours REAL DEFAULT 0.0,
    notes       TEXT DEFAULT '',
    updated_at  TEXT
);

CREATE TABLE IF NOT EXISTS working_memory (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    repo        TEXT NOT NULL,
    key         TEXT NOT NULL,
    value       TEXT NOT NULL,
    language    TEXT DEFAULT '',
    created_at  TEXT,
    expires_at  TEXT,
    UNIQUE(repo, key)
);
"""


class Memory:
    """Persistent memory backed by SQLite."""

    def __init__(self, db_path: str | Path):
        self._db_path = Path(db_path).expanduser()
        self._db: aiosqlite.Connection | None = None

    async def init(self):
        """Initialize database connection and schema."""
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._db = await aiosqlite.connect(str(self._db_path))
        await self._db.executescript(SCHEMA)
        await self._db.commit()
        logger.info("Memory initialized at %s", self._db_path)

    async def close(self):
        if self._db:
            await self._db.close()

    # ── Repos ──────────────────────────────────────────────────────────────

    async def has_analyzed(self, full_name: str) -> bool:
        """Check if a repo has been analyzed before."""
        cursor = await self._db.execute(
            "SELECT 1 FROM analyzed_repos WHERE full_name = ?", (full_name,)
        )
        return await cursor.fetchone() is not None

    async def record_analysis(self, full_name: str, language: str, stars: int, findings_count: int):
        """Record that a repo was analyzed."""
        await self._db.execute(
            """INSERT OR REPLACE INTO analyzed_repos
               (full_name, language, stars, analyzed_at, findings)
               VALUES (?, ?, ?, ?, ?)""",
            (full_name, language, stars, datetime.now(UTC).isoformat(), findings_count),
        )
        await self._db.commit()

    async def get_analyzed_repos(self, limit: int = 50) -> list[dict]:
        """Get recently analyzed repos."""
        cursor = await self._db.execute(
            "SELECT * FROM analyzed_repos ORDER BY analyzed_at DESC LIMIT ?", (limit,)
        )
        rows = await cursor.fetchall()
        cols = [d[0] for d in cursor.description]
        return [dict(zip(cols, row, strict=False)) for row in rows]

    # ── PRs ────────────────────────────────────────────────────────────────

    async def record_pr(
        self,
        repo: str,
        pr_number: int,
        pr_url: str,
        title: str,
        pr_type: str,
        branch: str = "",
        fork: str = "",
    ):
        """Record a submitted PR."""
        now = datetime.now(UTC).isoformat()
        await self._db.execute(
            """INSERT OR REPLACE INTO submitted_prs
               (repo, pr_number, pr_url, title, type, branch, fork, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (repo, pr_number, pr_url, title, pr_type, branch, fork, now, now),
        )
        await self._db.commit()

    async def update_pr_status(self, repo: str, pr_number: int, status: str):
        """Update PR status."""
        await self._db.execute(
            "UPDATE submitted_prs SET status = ?, updated_at = ? WHERE repo = ? AND pr_number = ?",
            (status, datetime.now(UTC).isoformat(), repo, pr_number),
        )
        await self._db.commit()

    async def get_prs(self, status: str | None = None, limit: int = 50) -> list[dict]:
        """Get submitted PRs, optionally filtered by status."""
        if status:
            cursor = await self._db.execute(
                "SELECT * FROM submitted_prs WHERE status = ? ORDER BY created_at DESC LIMIT ?",
                (status, limit),
            )
        else:
            cursor = await self._db.execute(
                "SELECT * FROM submitted_prs ORDER BY created_at DESC LIMIT ?", (limit,)
            )
        rows = await cursor.fetchall()
        cols = [d[0] for d in cursor.description]
        return [dict(zip(cols, row, strict=False)) for row in rows]

    async def get_today_pr_count(self) -> int:
        """Get number of PRs created today."""
        today = datetime.now(UTC).date().isoformat()
        cursor = await self._db.execute(
            "SELECT COUNT(*) FROM submitted_prs WHERE created_at LIKE ?",
            (f"{today}%",),
        )
        row = await cursor.fetchone()
        return row[0] if row else 0

    async def get_repo_prs(self, repo: str) -> list[dict]:
        """Get all PRs previously submitted for a specific repo."""
        cursor = await self._db.execute(
            "SELECT * FROM submitted_prs WHERE repo = ? ORDER BY created_at DESC",
            (repo,),
        )
        rows = await cursor.fetchall()
        cols = [d[0] for d in cursor.description]
        return [dict(zip(cols, row, strict=False)) for row in rows]

    # ── Run Log ────────────────────────────────────────────────────────────

    async def start_run(self) -> int:
        """Record the start of a pipeline run. Returns run ID."""
        cursor = await self._db.execute(
            "INSERT INTO run_log (started_at) VALUES (?)",
            (datetime.now(UTC).isoformat(),),
        )
        await self._db.commit()
        return cursor.lastrowid

    async def finish_run(
        self,
        run_id: int,
        repos_analyzed: int,
        prs_created: int,
        findings: int,
        errors: int,
    ):
        """Record the completion of a pipeline run."""
        await self._db.execute(
            """UPDATE run_log
               SET finished_at = ?, repos_analyzed = ?, prs_created = ?,
                   findings = ?, errors = ?
               WHERE id = ?""",
            (datetime.now(UTC).isoformat(), repos_analyzed, prs_created, findings, errors, run_id),
        )
        await self._db.commit()

    async def get_stats(self) -> dict:
        """Get overall statistics."""
        stats = {}

        cursor = await self._db.execute("SELECT COUNT(*) FROM analyzed_repos")
        stats["total_repos_analyzed"] = (await cursor.fetchone())[0]

        cursor = await self._db.execute("SELECT COUNT(*) FROM submitted_prs")
        stats["total_prs_submitted"] = (await cursor.fetchone())[0]

        cursor = await self._db.execute(
            "SELECT COUNT(*) FROM submitted_prs WHERE status = 'merged'"
        )
        stats["prs_merged"] = (await cursor.fetchone())[0]

        cursor = await self._db.execute("SELECT COUNT(*) FROM run_log")
        stats["total_runs"] = (await cursor.fetchone())[0]

        return stats

    async def get_run_history(self, limit: int = 20) -> list[dict]:
        """Get recent run history."""
        cursor = await self._db.execute(
            "SELECT * FROM run_log ORDER BY started_at DESC LIMIT ?",
            (limit,),
        )
        rows = await cursor.fetchall()
        cols = [d[0] for d in cursor.description]
        return [dict(zip(cols, row, strict=False)) for row in rows]

    # ── Outcome Learning ──────────────────────────────────────────────────

    async def record_outcome(
        self,
        repo: str,
        pr_number: int,
        pr_url: str,
        pr_type: str,
        outcome: str,
        feedback: str = "",
        time_to_close_hours: float = 0.0,
    ):
        """Record the outcome of a PR (merged, closed, rejected)."""
        await self._db.execute(
            """INSERT OR REPLACE INTO pr_outcomes
               (repo, pr_number, pr_url, pr_type, outcome, feedback,
                time_to_close_hours, recorded_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
            (
                repo,
                pr_number,
                pr_url,
                pr_type,
                outcome,
                feedback,
                time_to_close_hours,
                datetime.now(UTC).isoformat(),
            ),
        )
        await self._db.commit()

        # Auto-update repo preferences
        await self._update_repo_preferences(repo)

    async def _update_repo_preferences(self, repo: str):
        """Recompute repo preferences from outcome history."""
        import json

        cursor = await self._db.execute(
            "SELECT pr_type, outcome, time_to_close_hours FROM pr_outcomes WHERE repo = ?",
            (repo,),
        )
        rows = await cursor.fetchall()
        if not rows:
            return

        merged_types: list[str] = []
        rejected_types: list[str] = []
        total_hours = 0.0
        merged_count = 0

        for pr_type, outcome, hours in rows:
            if outcome == "merged":
                merged_types.append(pr_type)
                merged_count += 1
                total_hours += hours or 0
            elif outcome in ("closed", "rejected"):
                rejected_types.append(pr_type)

        merge_rate = merged_count / len(rows) if rows else 0.0
        avg_hours = total_hours / merged_count if merged_count else 0.0

        await self._db.execute(
            """INSERT OR REPLACE INTO repo_preferences
               (repo, preferred_types, rejected_types, merge_rate,
                avg_review_hours, updated_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (
                repo,
                json.dumps(list(set(merged_types))),
                json.dumps(list(set(rejected_types))),
                round(merge_rate, 3),
                round(avg_hours, 1),
                datetime.now(UTC).isoformat(),
            ),
        )
        await self._db.commit()

    async def get_repo_preferences(self, repo: str) -> dict | None:
        """Get learned preferences for a specific repo."""
        import json

        cursor = await self._db.execute("SELECT * FROM repo_preferences WHERE repo = ?", (repo,))
        row = await cursor.fetchone()
        if not row:
            return None
        cols = [d[0] for d in cursor.description]
        prefs = dict(zip(cols, row, strict=False))
        prefs["preferred_types"] = json.loads(prefs.get("preferred_types", "[]"))
        prefs["rejected_types"] = json.loads(prefs.get("rejected_types", "[]"))
        return prefs

    async def get_rejection_patterns(self, limit: int = 20) -> list[dict]:
        """Get common rejection reasons across all repos."""
        cursor = await self._db.execute(
            """SELECT repo, pr_type, feedback
               FROM pr_outcomes
               WHERE outcome IN ('closed', 'rejected') AND feedback != ''
               ORDER BY recorded_at DESC LIMIT ?""",
            (limit,),
        )
        rows = await cursor.fetchall()
        return [{"repo": r[0], "pr_type": r[1], "feedback": r[2]} for r in rows]

    async def get_outcome_stats(self) -> dict:
        """Get outcome statistics."""
        stats = {}
        cursor = await self._db.execute(
            "SELECT outcome, COUNT(*) FROM pr_outcomes GROUP BY outcome"
        )
        for outcome, count in await cursor.fetchall():
            stats[outcome] = count
        cursor = await self._db.execute("SELECT AVG(merge_rate) FROM repo_preferences")
        row = await cursor.fetchone()
        stats["avg_merge_rate"] = round(row[0], 3) if row and row[0] else 0.0
        return stats

    # ── Working Memory (hot context) ──────────────────────────────────────

    async def store_context(
        self,
        repo: str,
        key: str,
        value: str,
        *,
        language: str = "",
        ttl_hours: float = 24.0,
    ) -> None:
        """Store hot context for a repo.

        Args:
            repo: Repository full name (owner/repo).
            key: Context key (e.g. 'analysis_summary', 'style_guide').
            value: Context value.
            language: Programming language (for similarity lookups).
            ttl_hours: Hours until this context expires.
        """
        now = datetime.now(UTC)
        from datetime import timedelta

        expires_dt = now + timedelta(hours=ttl_hours)
        await self._db.execute(
            """INSERT OR REPLACE INTO working_memory
               (repo, key, value, language, created_at, expires_at)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (repo, key, value, language, now.isoformat(), expires_dt.isoformat()),
        )
        await self._db.commit()

    async def get_context(self, repo: str, key: str) -> str | None:
        """Retrieve hot context for a repo, returns None if expired.

        Args:
            repo: Repository full name.
            key: Context key.

        Returns:
            Context value or None if not found/expired.
        """
        now = datetime.now(UTC).isoformat()
        cursor = await self._db.execute(
            """SELECT value FROM working_memory
               WHERE repo = ? AND key = ? AND expires_at > ?""",
            (repo, key, now),
        )
        row = await cursor.fetchone()
        return row[0] if row else None

    async def get_similar_context(self, language: str, key: str, limit: int = 5) -> list[dict]:
        """Find context from repos with the same language.

        Useful for transferring learned patterns to similar repos.

        Args:
            language: Programming language to match.
            key: Context key to look for.
            limit: Max results.

        Returns:
            List of {repo, value} dicts.
        """
        now = datetime.now(UTC).isoformat()
        cursor = await self._db.execute(
            """SELECT repo, value FROM working_memory
               WHERE language = ? AND key = ? AND expires_at > ?
               ORDER BY created_at DESC LIMIT ?""",
            (language, key, now, limit),
        )
        rows = await cursor.fetchall()
        return [{"repo": r[0], "value": r[1]} for r in rows]

    async def archive_expired(self) -> int:
        """Delete expired working memory entries.

        Returns:
            Number of entries deleted.
        """
        now = datetime.now(UTC).isoformat()
        cursor = await self._db.execute("DELETE FROM working_memory WHERE expires_at <= ?", (now,))
        await self._db.commit()
        return cursor.rowcount
