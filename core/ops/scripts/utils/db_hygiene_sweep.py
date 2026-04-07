"""
db_hygiene_sweep.py
====================
OmniClaw Watchdog — Database Directory Enforcer

Rule: vault/assets/databases/ is a PURE DATA ZONE.
      No subdirectory that mirrors a root-level OmniClaw path is allowed.
      Violating folders are automatically quarantined or removed.

GAP Reference: GAP-2026-04-07-002
Author: Antigravity (OmniClaw Core Ops)
"""

import os
import shutil
import logging
from datetime import datetime

# ─────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────
DATABASES_ROOT = r"D:\OmniClaw\vault\assets\databases"

# Registered engine namespaces — the ONLY allowed subdirectories
ALLOWED_ENGINE_NAMES = {
    "chromadb", "weaviate", "qdrant", "lancedb", "neo4j",
    "faiss", "pgvector", "redis", "milvus", "pinecone",
}

# Forbidden directory names — root-level mirrors that must NEVER appear here
FORBIDDEN_DIR_NAMES = {
    "vault", "core", "system", "brain", "quarantine",
    "tmp", "temp", "scripts", "daemons", "agents",
    "trash_before_push",
}

ALLOWED_EXTENSIONS = {".db", ".sqlite", ".sqlite3", ".json", ".idx", ".bin", ".faiss", ".md", ".gitkeep", ".txt"}

ALLOWED_SYSTEM_DIRS = {"logs", "_perm"}  # OmniClaw-managed subdirs (not engines but allowed)

LOG_PATH = r"D:\OmniClaw\vault\assets\databases\_sweep_log.txt"

# ─────────────────────────────────────────────
# LOGGER
# ─────────────────────────────────────────────
logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)

def log(msg: str, level: str = "info"):
    print(f"[db_hygiene_sweep] {msg}")
    getattr(logging, level)(msg)


# ─────────────────────────────────────────────
# CORE SWEEP LOGIC
# ─────────────────────────────────────────────
def sweep(dry_run: bool = False) -> None:
    log(f"=== DB Hygiene Sweep Started @ {datetime.now().isoformat()} ===")
    violations = []

    if not os.path.isdir(DATABASES_ROOT):
        log(f"DATABASES_ROOT does not exist: {DATABASES_ROOT}", "warning")
        return

    for item_name in os.listdir(DATABASES_ROOT):
        item_path = os.path.join(DATABASES_ROOT, item_name)
        item_lower = item_name.lower()

        # Skip allowed top-level identity/log files
        if os.path.isfile(item_path):
            _, ext = os.path.splitext(item_name)
            if ext in ALLOWED_EXTENSIONS or item_name.startswith("."):
                continue
            else:
                log(f"[WARN] Unexpected file type: {item_path}", "warning")
                continue

        # It's a directory
        if os.path.isdir(item_path):
            if item_lower in ALLOWED_ENGINE_NAMES or item_lower in ALLOWED_SYSTEM_DIRS:
                log(f"[OK] Registered namespace: {item_name}")
                continue

            if item_lower in FORBIDDEN_DIR_NAMES:
                log(f"[VIOLATION] Forbidden directory detected: {item_path}", "error")
                violations.append(item_path)
                if not dry_run:
                    try:
                        shutil.rmtree(item_path)
                        log(f"[PURGED] Successfully removed: {item_path}", "warning")
                    except Exception as e:
                        log(f"[ERROR] Failed to remove {item_path}: {e}", "error")
                else:
                    log(f"[DRY-RUN] Would remove: {item_path}")
                continue

            # Unknown directory — log as suspicious but don't auto-delete (may be new engine)
            log(f"[UNKNOWN] Unregistered subdirectory (manual review needed): {item_path}", "warning")

    log(f"=== Sweep Complete. Violations found: {len(violations)} ===")
    if violations:
        log("─── VIOLATED PATHS ───", "error")
        for v in violations:
            log(f"  {v}", "error")


# ─────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────
if __name__ == "__main__":
    import sys
    dry = "--dry-run" in sys.argv
    sweep(dry_run=dry)
