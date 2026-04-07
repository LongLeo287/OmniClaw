#!/usr/bin/env python3
"""
OMNICLAW DAEMON UTILS  BRAIN FOR GENERAL USE
=======================================
Shared utility module for all 5 Core Daemons.
Provides: Deep Scan, Fast Trace, OMA Map loader, Report system.

Import: from daemon_utils import deep_scan, fast_trace, report_before, report_after, load_oma_map
"""
import os
import json
import time
from datetime import datetime
from typing import Optional

# [System log: Legacy non-English comment removed]
import sys
sys.path.insert(0, os.path.dirname(__file__))
from daemon_trust import PATHS, abs_path

CLI_LOG = abs_path("brain/registry/cli_run.log")
REPORT_LOG = abs_path(PATHS.HANDOFF_LOG)


# [System log: Legacy non-English comment removed]
#  1. OMA MAP LOADER
# [System log: Legacy non-English comment removed]
def load_oma_map() -> dict:
    """ [System log: Legacy non-English docstring localized] """
    map_path = abs_path(PATHS.SYSTEM_MAP)
    if os.path.exists(map_path):
        try:
            with open(map_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def load_fast_index() -> list:
    """ [System log: Legacy non-English docstring localized] """
    idx_path = abs_path(PATHS.FAST_INDEX)
    if os.path.exists(idx_path):
        try:
            with open(idx_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return []
    return []


# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def fast_trace(file_id: str) -> Optional[dict]:
    """
    Lookup ngay trong FAST_INDEX.json theo ID.
    Returns entry dict if found, None if not.
    """
    index = load_fast_index()
    for entry in index:
        if entry.get("id") == file_id:
            return entry
    return None


def fast_trace_coord(coord: str) -> Optional[dict]:
    """Lookup by relative path (coord)."""
    index = load_fast_index()
    for entry in index:
        if entry.get("coord", "").endswith(coord):
            return entry
    return None


# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def deep_scan(root: str, extensions: tuple = (".md", ".json", ".yaml", ".py"),
              skip_dirs: tuple = (".git", "__pycache__", "node_modules")) -> list:
    """
    Qut  quy t root. Tr v danh sch dict vi metadata tng file.
    Dng cho OMA (Deepscan), OHD (Health Check), OA (Knowledge Harvest).
    """
    results = []
    aios_root = abs_path("")

    for dirpath, dirs, files in os.walk(root):
        # Prune ignored dirs in-place
        dirs[:] = [d for d in dirs if d not in skip_dirs and not d.startswith(".")]

        for fname in files:
            if not fname.endswith(extensions):
                continue
            fpath = os.path.join(dirpath, fname)
            rel = os.path.relpath(fpath, aios_root).replace("\\", "/")
            try:
                stat = os.stat(fpath)
                has_frontmatter = False
                has_id = False
                if fname.endswith(".md"):
                    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                        head = f.read(512)
                    has_frontmatter = head.startswith("---")
                    has_id = "id:" in head[:200] if has_frontmatter else False

                results.append({
                    "path": fpath,
                    "coord": rel,
                    "name": fname,
                    "size": stat.st_size,
                    "modified": datetime.fromtimestamp(stat.st_mtime).isoformat(),
                    "has_frontmatter": has_frontmatter,
                    "has_id": has_id,
                    "healthy": has_id if fname.endswith(".md") else True,
                })
            except Exception:
                pass
    return results


def find_stray_files(root: str) -> list:
    """Find Markdown files that do not have _DIR_IDENTITY.md in the parent folder, or are missing a YAML ID."""
    all_files = deep_scan(root, extensions=(".md",))
    return [f for f in all_files if not f["has_id"] and "_DIR_IDENTITY" not in f["name"]]


def find_orphan_folders(root: str) -> list:
    """Look for folders without _DIR_IDENTITY.md or README.md with frontmatter."""
    orphans = []
    aios_root = abs_path("")
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("__pycache__", "node_modules")]
        has_identity = any(f in files for f in ["_DIR_IDENTITY.md", "README.md"])
        if not has_identity and dirpath != root:
            orphans.append(os.path.relpath(dirpath, aios_root).replace("\\", "/"))
    return orphans


# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
def _write_log(path: str, line: str):
    """Write a line to the log file, create a file if it does not exist."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def report_before(daemon: str, action: str, targets: list):
    """Report BEFORE the Daemon takes action."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    targets_str = ", ".join(str(t) for t in targets[:5])
    line = f"[{ts}] [{daemon}]  START {action} | targets={targets_str} (count={len(targets)})"
    print(f"\033[94m[INFO]\033[0m {line}")
    _write_log(REPORT_LOG, line)
    _write_log(CLI_LOG, line)


def report_after(daemon: str, action: str, results: dict):
    """Report AFTER Daemon completes. results = {'success': N, 'failed': M, 'skipped': K}"""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ok = results.get("success", 0)
    fail = results.get("failed", 0)
    skip = results.get("skipped", 0)
    status = " OK" if fail == 0 else " PARTIAL"
    line = f"[{ts}] [{daemon}] {status} END {action} | success={ok} failed={fail} skipped={skip}"
    print(f"\033[96m[STAT]\033[0m {line}")
    _write_log(REPORT_LOG, line)
    _write_log(CLI_LOG, line)


def report_error(daemon: str, action: str, error: str):
    """Report critical error."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [{daemon}]  ERROR {action} | {error}"
    print(f"\033[91m[ERR]\033[0m {line}")
    _write_log(REPORT_LOG, line)
    _write_log(CLI_LOG, line)

# [System log: Legacy non-English comment removed]
#  5. NEURAL BUS (SQLITE BROKER)
# [System log: Legacy non-English comment removed]
def _init_db(db_path):
    import sqlite3
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            queue_name TEXT NOT NULL,
            payload TEXT NOT NULL,
            status TEXT DEFAULT 'PENDING',
            retry_count INTEGER DEFAULT 0,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

def queue_enqueue(queue_name: str, payload_dict: dict):
    """Push task to Neural Bus (SQLite Queue)."""
    import sqlite3, json
    db_path = abs_path(PATHS.ASSETS_DB + "/neural_bus.db")
    _init_db(db_path)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(
        "INSERT INTO messages (queue_name, payload, status, created_at, updated_at) VALUES (?, ?, ?, ?, ?)",
        (queue_name, json.dumps(payload_dict), 'PENDING', datetime.now().isoformat(), datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def queue_dequeue(queue_name: str) -> Optional[dict]:
    """Get task from Neural Bus, return dict with id and payload."""
    import sqlite3, json
    db_path = abs_path(PATHS.ASSETS_DB + "/neural_bus.db")
    _init_db(db_path)
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute("BEGIN EXCLUSIVE")
    c.execute("SELECT id, payload FROM messages WHERE queue_name=? AND status='PENDING' ORDER BY id ASC LIMIT 1", (queue_name,))
    row = c.fetchone()
    if row:
        msg_id, payload = row['id'], json.loads(row['payload'])
        c.execute("UPDATE messages SET status='PROCESSING', updated_at=? WHERE id=?", (datetime.now().isoformat(), msg_id))
        conn.commit()
        conn.close()
        return {"id": msg_id, "payload": payload}
    conn.commit()
    conn.close()
    return None

def queue_mark_success(msg_id: int):
    """Task deleted successfully."""
    import sqlite3
    db_path = abs_path(PATHS.ASSETS_DB + "/neural_bus.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM messages WHERE id=?", (msg_id,))
    conn.commit()
    conn.close()

def queue_mark_failed(msg_id: int) -> int:
    """Increase error. Reach level 3 => enter DEAD_LETTER queue."""
    import sqlite3
    db_path = abs_path(PATHS.ASSETS_DB + "/neural_bus.db")
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT retry_count FROM messages WHERE id=?", (msg_id,))
    row = c.fetchone()
    count = 0
    if row:
        count = row[0] + 1
        status = 'PENDING' if count < 3 else 'DEAD_LETTER'
        c.execute("UPDATE messages SET status=?, retry_count=?, updated_at=? WHERE id=?", (status, count, datetime.now().isoformat(), msg_id))
    conn.commit()
    conn.close()
    return count

# -------------------------------------------------------------
# 6. OMNICLAW AI CORE (LLM)
# -------------------------------------------------------------
def get_env_var(key: str, default: str) -> str:
    """Reads environment variables from MASTER.env or defaults."""
    env_path = abs_path("system/ops/secrets/MASTER.env")
    if os.path.exists(env_path):
        with open(env_path, "r", encoding="utf-8") as f:
            for line in f:
                if "=" in line and not line.startswith("#"):
                    k, v = line.strip().split("=", 1)
                    if k.strip() == key:
                        return v.strip()
    return default

def call_omniclaw_model(prompt: str, json_format: bool = False, timeout=1800) -> Optional[str]:
    """
    Core AI call directly from Daemon. 
    Smart Routing: Automatically falls back to secondary ports/models if the primary fails.
    """
    import urllib.request
    import urllib.error
    import time
    
    # Routing Table: Strictly OBD Controlled (Port and Fleet bound to config.json)
    routes = []
    config_path = abs_path("core/config/config.json")
    if os.path.exists(config_path):
        try:
            with open(config_path, "r", encoding="utf-8") as f:
                cfg = json.load(f)
                ollama = cfg.get("services", {}).get("ollama", {})
                if ollama:
                    port = ollama.get("port")
                    base = f"http://localhost:{port}/v1"
                    default_mod = ollama.get("default_model")
                    if default_mod:
                        routes.append({"url": base, "model": default_mod, "key": "ollama"})
                    # Append all fleet models
                    for _, mod_name in ollama.get("fleet", {}).items():
                        if mod_name not in [r["model"] for r in routes]:
                            routes.append({"url": base, "model": mod_name, "key": "ollama"})
                            
                # CLOUD FALLBACK: Multi-cloud injection
                clouds = ["nvidia", "groq", "openrouter"]
                for cloud in clouds:
                    c_cfg = cfg.get("services", {}).get(cloud, {})
                    if c_cfg and c_cfg.get("url") and c_cfg.get("api_key") and "YOUR_" not in c_cfg.get("api_key"):
                        routes.append({
                            "url": c_cfg.get("url"), 
                            "model": c_cfg.get("default_model", ""), 
                            "key": c_cfg.get("api_key")
                        })
                    
        except Exception: pass
        
    if not routes:
        raise ValueError("[AI_CORE] FATAL: OBD Configuration missing or invalid. Cannot find routing ports or models.")
    
    for route in routes:
        endpoint = f"{route['url'].rstrip('/')}/chat/completions"
        payload = {
            "model": route["model"],
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.3
        }
        if json_format:
            payload["response_format"] = {"type": "json_object"}
            
        data = json.dumps(payload).encode('utf-8')
        headers = {'Content-Type': 'application/json'}
        if route["key"] != "ollama":
            headers["Authorization"] = f"Bearer {route['key']}"
            
        req = urllib.request.Request(endpoint, data=data, headers=headers)
        
        try:
            with urllib.request.urlopen(req, timeout=timeout) as response:
                res_body = response.read().decode('utf-8')
                res_json = json.loads(res_body)
                return res_json["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            report_error("AI_CORE", f"Router {route['url']} (Model: {route['model']})", f"HTTP {e.code}")
            continue # Fallback next route
        except urllib.error.URLError as e:
            report_error("AI_CORE", f"Router {route['url']} Connection Failed", str(e.reason))
            continue # Fallback next route
        except Exception as e:
            report_error("AI_CORE", f"Router Execution Error", str(e))
            continue
            
    report_error("AI_CORE", "ALL ROUTING FALLBACKS FAILED", "System has no active AI connection.")
    return None
