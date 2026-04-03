"""
omniclaw_oid_daemon.py — OmniClaw Ingestion Daemon V2 (Background Daemon)
Owner: registry-manager-agent (Dept: Intake & Registry — reporting to CEO)
Phase: 12 — OID V2

Architecture:
    Runs silently in the background. Polls vault/vault/DATA/ for new intake tickets.
    Processes each ticket sequentially (one at a time) through the full 7-step pipeline:

    [0] Process Lock      — Ensures single instance, kills zombie processes
    [1] Dedup             — Rejects already-processed sources (hash check)
    [2] Security Gate     — Strix-agent: malicious pattern scan
    [3] Classification    — knowledge_navigator: domain tagging + scoring
    [4] Queue Routing     — ACCEPTED → Accepted Queue | PENDING/REJECTED → Vault
    [5] Deep Extraction   — knowledge_enricher: compress repo into knowledge .md
    [6] Librarian         — Registry: mark source for future update tracking
    [7] Cleanup Crew      — archivist: wipe all raw/tmp files (zero residue)

Rules:
    - ALL code, logs, comments, created files: 100% English. No exceptions.
    - Never skip, bypass, or reorder steps.
    - Never open multiple terminal windows; use PID lock + subprocess management.
    - Runs completely in the background — does not block the IDE chat session.

Trigger:
    python core/automations/daemons/omniclaw_oid_daemon.py
    (Registered in AUTOMATION_REGISTRY.yaml under auto_evolution_engine)
"""

import sys
import time
import logging
import glob
from pathlib import Path

import os
import json
import re
import shutil
import subprocess
import traceback
from pathlib import Path
from datetime import datetime

# ── Root resolution ───────────────────────────────────────────────────────────
_DAEMON_DIR = Path(__file__).resolve().parent
OMNICLAW_ROOT = os.getenv("OMNICLAW_ROOT") or str(_DAEMON_DIR.parents[2])
os.environ["OMNICLAW_ROOT"] = OMNICLAW_ROOT  # propagate for sub-modules

# Add daemon dir to path so oid package is importable
sys.path.insert(0, str(_DAEMON_DIR))

# ── OID sub-modules (built in Steps 1-3) ─────────────────────────────────────
from oid.triage import triage, mark_as_processed, is_duplicate
from oid.scraper import fetch_repo, fetch_url, fetch_local_file
from oid.extractor import extract_knowledge

# ── Paths ─────────────────────────────────────────────────────────────────────
ROOT = Path(OMNICLAW_ROOT)
VAULT_DATA_DIR = ROOT / "storage" / "vault" / "DATA"
VAULT_DIR      = ROOT / "storage" / "vault"
STATE_DIR      = VAULT_DIR / "OID_STATE"
ACCEPTED_Q     = STATE_DIR / "accepted_queue.json"
PENDING_Q      = STATE_DIR / "pending_queue.json"
REJECTED_Q     = STATE_DIR / "rejected_queue.json"
QUARANTINE_DIR = ROOT / "system" / "security" / "QUARANTINE"
STAGING_DIR    = ROOT / "brain" / "knowledge" / "staging"
LOG_FILE       = ROOT / "system" / "ops" / "telemetry" / "logs" / "oid_daemon.log"
LOCK_FILE      = STATE_DIR / "oid_daemon.lock"

for d in [VAULT_DATA_DIR, STATE_DIR, QUARANTINE_DIR, STAGING_DIR, LOG_FILE.parent]:
    d.mkdir(parents=True, exist_ok=True)

POLL_INTERVAL_SECONDS = 10

# ── Logging ───────────────────────────────────────────────────────────────────

def log(msg: str, level: str = "INFO"):
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{ts}] [{level}] {msg}"
    print(line)
    with open(LOG_FILE, "a", encoding="utf-8-sig") as f:
        f.write(line + "\n")


# ── Step 0: Process Lock ──────────────────────────────────────────────────────

def enforce_single_instance():
    """Kill any previous zombie instance, then record our PID in the lock file."""
    current_pid = os.getpid()
    if LOCK_FILE.exists():
        try:
            old_pid = int(LOCK_FILE.read_text().strip())
            if old_pid != current_pid:
                try:
                    import psutil
                    p = psutil.Process(old_pid)
                    if "python" in p.name().lower():
                        log(f"Terminating stale OID process (PID={old_pid})", "WARN")
                        p.terminate()
                        p.wait(timeout=5)
                except Exception:
                    pass  # Process already dead — safe to proceed
        except Exception:
            pass
    LOCK_FILE.write_text(str(current_pid))
    log(f"OID Daemon locked (PID={current_pid})")


def release_lock():
    if LOCK_FILE.exists():
        LOCK_FILE.unlink()


# ── Queue helpers ─────────────────────────────────────────────────────────────

def _load_queue(path: Path) -> list:
    if not path.exists():
        return []
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return []


def _save_queue(path: Path, data: list):
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def _append_queue(path: Path, entry: dict):
    q = _load_queue(path)
    q.append(entry)
    _save_queue(path, q)


# ── Step 7: Cleanup Crew ──────────────────────────────────────────────────────

def cleanup_ticket_artifacts(ticket_id: str, clean_logs: bool = True):
    """
    archivist: wipe all raw/tmp artefacts for a completed ticket.
    Preserves: Accepted/Pending/Rejected queue entries and processed knowledge md.
    Wipes:
        - QUARANTINE raw clones
        - STAGING raw md
        - Any generated .log and .tmp files
    """
    log(f"[{ticket_id}] Cleanup Crew active — wiping raw artefacts, logs, and tmp files")
    
    # 1. Wipe specific quarantine and staging directories (Raw Clones & Workdirs)
    for parent in [QUARANTINE_DIR, STAGING_DIR]:
        target = parent / ticket_id
        if target.exists():
            try:
                if target.is_dir():
                    shutil.rmtree(target)
                else:
                    target.unlink()
                log(f"[{ticket_id}] Erased specific raw clone: {target}")
            except Exception as e:
                log(f"[{ticket_id}] Cleanup error at {target}: {e}", "ERROR")

    # 2. Deploy the Official OmniClaw Cleanup Crew for global sweeps
    if clean_logs:
        crew_script = ROOT / "system" / "ops" / "scripts" / "omniclaw_cleanup_crew.py"
        if crew_script.exists():
            log(f"[{ticket_id}] Deploying OmniClaw Cleanup Crew for OS-level sweep...")
            try:
                subprocess.run([
                    sys.executable, str(crew_script), 
                    "core/security/QUARANTINE", "vault/vault/DATA", "core/automations/daemons"
                ], capture_output=True)
                log(f"[{ticket_id}] Cleanup Crew executed sweep successfully.")
            except Exception as e:
                log(f"[{ticket_id}] Cleanup Crew failed: {e}", "WARN")


# ── Advanced: Auto-Evolution ──────────────────────────────────────────────────
def trigger_auto_evolution(ticket: dict):
    """
    Phase 7: Auto-Evolution
    Detects if the newly ingested knowledge implies a capability gap.
    If the domain lacks an existing department, it automatically scaffolds a new agent using create_agent.py.
    """
    ticket_id = ticket["id"]
    domain = ticket.get("triage", {}).get("domain", "general")
    confidence = ticket.get("triage", {}).get("confidence", 0.0)
    
    # We only evolve if we are confident about the domain, and it's not "general"
    if domain == "general" or confidence < 0.6:
        return

    dept_dir = ROOT / "ecosystem" / "workforce" / "departments" / domain
    if not dept_dir.exists():
        log(f"[{ticket_id}] 🧬 GAP DETECTED: Domain '{domain}' lacks a department. Triggering Auto-Evolution.")
        head_agent = f"{domain.replace('_', '-')}-specialist-agent"
        script = ROOT / "ecosystem" / "workforce" / "system" / "education" / "oa-chief-agent" / "tools" / "create_agent.py"
        
        if script.exists():
            try:
                cmd = [
                    sys.executable, str(script),
                    "--id", head_agent,
                    "--dept", domain,
                    "--tier", "3",
                    "--head",
                    "--title", f"Specialist for {domain.title()}"
                ]
                subprocess.run(cmd, capture_output=True, text=True)
                log(f"[{ticket_id}] 🧬 Auto-Evolution: Scaffolded {head_agent} for new dept '{domain}'.")
                
                # Update SYSTEM_INDEX with the newly spawned agent
                indexer_script = ROOT / "ecosystem" / "workforce" / "system" / "education" / "registry-manager-agent" / "tools" / "registry_indexer.py"
                if indexer_script.exists():
                    subprocess.run([sys.executable, str(indexer_script)], capture_output=True)
                
                # Notify CEO of the evolutionary leap
                msg = (f"🧬 [AUTO-EVOLUTION] OmniClaw evolved!\n"
                       f"Domain: {domain}\n"
                       f"New Agent Scaffolded: {head_agent}\n"
                       f"Trigger: Absorbed {ticket.get('source', 'Unknown')}\n"
                       f"Action Required: CEO Approval via propose_dept.py or manual review.")
                notify_bridge(msg)
            except Exception as e:
                log(f"[{ticket_id}] Auto-Evolution pipeline failed: {e}", "ERROR")

# ── Advanced: Ecosystem Broadcast ─────────────────────────────────────────────
def broadcast_success_event(ticket: dict):
    """
    Publish ingest event to Agent Bus and update global blackboard.json.
    """
    ticket_id = ticket["id"]
    source = ticket.get("source", "Unknown")
    domain = ticket.get("triage", {}).get("domain", "general")
    
    # 1. Update Blackboard stats
    bb_path = ROOT / "brain" / "shared-context" / "blackboard.json"
    if bb_path.exists():
        try:
            bb = json.loads(bb_path.read_text(encoding="utf-8"))
            stats = bb.get("oid_stats", {"total_ingested": 0})
            stats["total_ingested"] = stats.get("total_ingested", 0) + 1
            stats["last_ingested_source"] = source
            stats["last_ingested_domain"] = domain
            stats["last_ingested_time"] = datetime.now().isoformat()
            bb["oid_stats"] = stats
            bb["blackboard_updated_at"] = datetime.now().isoformat()
            bb_path.write_text(json.dumps(bb, indent=2, ensure_ascii=False), encoding="utf-8")
            log(f"[{ticket_id}] Updated blackboard.json OID stats.")
        except Exception as e:
            log(f"[{ticket_id}] Blackboard update failed: {e}", "WARN")

    # 2. Publish to SQLite Agent Bus for real-time orchestrator pickup
    bus_script = ROOT / "ecosystem" / "workforce" / "system" / "education" / "oa-chief-agent" / "tools" / "agent_bus.py"
    if bus_script.exists():
        try:
            payload = json.dumps({"id": ticket_id, "source": source, "domain": domain})
            subprocess.run([
                sys.executable, str(bus_script), "publish", "oid_knowledge_ingested", payload
            ], capture_output=True)
            log(f"[{ticket_id}] Broadcasted 'oid_knowledge_ingested' to Agent Bus 📡")
            
            # 3. Publish to Agent Bus for Skill Creator Ultra trigger
            skill_cmd = json.dumps({"target_repo": source, "knowledge_id": ticket_id, "domain": domain})
            subprocess.run([
                sys.executable, str(bus_script), "publish", "skill_discovery_required", skill_cmd
            ], capture_output=True)
            log(f"[{ticket_id}] Broadcasted 'skill_discovery_required' to trigger Skill Creator Ultra 🛠️")
        except Exception as e:
            log(f"[{ticket_id}] Agent Bus publish failed: {e}", "WARN")


# ── Step 5-6: Deep Process ────────────────────────────────────────────────────

def deep_process(source: str, source_type: str, ticket_id: str) -> bool:
    """
    knowledge_enricher + registry_manager: Extract knowledge, register with Librarian.

    Steps executed:
        5a — Clone/fetch source into QUARANTINE staging area
        5b — Extract full knowledge into brain/knowledge/processed_repos/
        6  — Mark source in processed DB (Librarian registration)
    """
    log(f"[{ticket_id}] BEGIN deep processing: {source_type.upper()} | {source[:80]}")

    cloned_path = None

    # ── 5a: Fetch ─────────────────────────────────────────────────────────────
    if source_type == "repo":
        cloned_path = fetch_repo(source, ticket_id)
        if not cloned_path:
            log(f"[{ticket_id}] Fetch failed — all clone strategies exhausted", "ERROR")
            return False

        # ── OIW INTAKE GATE: Empty / Broken Repo Check ────────────────────────
        # Check if the folder is functionally empty (e.g. only contains .git)
        has_real_content = False
        if cloned_path.exists() and cloned_path.is_dir():
            for item in cloned_path.iterdir():
                if item.name not in ('.git', '.DS_Store', 'desktop.ini', 'thumbs.db'):
                    has_real_content = True
                    break

        if not has_real_content:
            log(f"[{ticket_id}] OA ALERT: Fetched repository is EMPTY or BROKEN. (Likely a clone failure or hollow repo)", "ERROR")
            log(f"[{ticket_id}] OHD ACTION: Purging hollow directory {cloned_path}...", "WARN")
            try:
                # Call OHD (Cleanup) to eradicate the hollow directory
                shutil.rmtree(str(cloned_path))
            except Exception as e:
                log(f"[{ticket_id}] OHD Purge failed: {e}", "ERROR")
            return False

        # ── 5b: Extract ───────────────────────────────────────────────────────
        success = extract_knowledge(cloned_path, cleanup=True)  # cleanup=True wipes clone
        if not success:
            log(f"[{ticket_id}] Extraction failed for: {source}", "ERROR")
            return False

    elif source_type in ("url", "post", "doc"):
        content = fetch_url(source, ticket_id)
        if not content:
            log(f"[{ticket_id}] URL fetch failed for: {source}", "ERROR")
            return False

        # Save raw content as staging .md for further enrichment
        staging_md = STAGING_DIR / ticket_id / f"{ticket_id}_raw.md"
        staging_md.parent.mkdir(parents=True, exist_ok=True)
        staging_md.write_text(
            f"# RAW INTAKE: {source}\n\n{content}",
            encoding="utf-8"
        )
        log(f"[{ticket_id}] URL content staged: {staging_md}")

    elif source_type == "file":
        content = fetch_local_file(source)
        if not content:
            log(f"[{ticket_id}] File read failed: {source}", "ERROR")
            return False
        staging_md = STAGING_DIR / ticket_id / f"{ticket_id}_raw.md"
        staging_md.parent.mkdir(parents=True, exist_ok=True)
        staging_md.write_text(
            f"# FILE INTAKE: {source}\n\n{content}",
            encoding="utf-8"
        )
        log(f"[{ticket_id}] File staged: {staging_md}")

    else:
        log(f"[{ticket_id}] Unknown source type: {source_type}", "WARN")
        return False

    # ── Step 6: Librarian Registration via Native Indexer ────────────────────
    mark_as_processed(source, ticket_id)
    
    # Run the user's native registry_indexer.py to catalog the new repo
    try:
        indexer_script = ROOT / "ecosystem" / "workforce" / "system" / "education" / "registry-manager-agent" / "tools" / "registry_indexer.py"
        if indexer_script.exists():
            subprocess.run([sys.executable, str(indexer_script)], check=True, capture_output=True)
            log(f"[{ticket_id}] sys/ops/registry_indexer.py regenerated SYSTEM_INDEX.yaml successfully.")
    except Exception as e:
        log(f"[{ticket_id}] registry_indexer call failed: {e}", "WARN")

    # Run ki_indexer.py to map knowledge into KI_INDEX.md
    try:
        ki_script = ROOT / "ecosystem" / "workforce" / "system" / "education" / "registry-manager-agent" / "tools" / "ki_indexer.py"
        if ki_script.exists():
            subprocess.run([sys.executable, str(ki_script)], check=True, capture_output=True)
            log(f"[{ticket_id}] sys/ops/ki_indexer.py regenerated KI_INDEX.md successfully.")
    except Exception as e:
        log(f"[{ticket_id}] ki_indexer call failed: {e}", "WARN")

    # UPDATE SYSTEM MAP (OS Context Snapshot)
    try:
        snapshot_script = ROOT / "ecosystem" / "workforce" / "system" / "education" / "archivist" / "tools" / "os_state_snapshot.py"
        if snapshot_script.exists():
            subprocess.run([sys.executable, str(snapshot_script)], check=True, capture_output=True)
            log(f"[{ticket_id}] System Map updated via os_state_snapshot.py successfully.")
    except Exception as e:
        log(f"[{ticket_id}] System Map update call failed: {e}", "WARN")

    log(f"[{ticket_id}] Deep processing COMPLETE")
    
    # ── Alert CEO via Native Dispatch ───────────────────────────────────────
    try:
        dispatch_script = ROOT / "system" / "ops" / "telegram_dispatch.py"
        if dispatch_script.exists():
            msg = f"OID Ingested Successfully: {source}\nID: {ticket_id}"
            subprocess.run([sys.executable, str(dispatch_script), "alert", msg, "OK"], capture_output=True)
    except Exception:
        pass

    return True


# ── Main pipeline: process one ticket from Accepted Queue ────────────────────

MAX_RETRIES = 3

def process_one_accepted():
    """Pop one item off the Accepted Queue and run the full extraction pipeline."""
    queue = _load_queue(ACCEPTED_Q)
    if not queue:
        return

    entry = queue[0]  # Take the front of the queue
    tid = entry.get("id", "UNKNOWN")
    source = entry.get("source", "")
    stype = entry.get("source_type", "url")
    retries = entry.get("retry_count", 0)

    log(f"\n[{tid}] ===== STARTING OID EXTRACTION (Attempt {retries + 1}/{MAX_RETRIES}) =====")

    try:
        success = deep_process(source, stype, tid)

        if success:
            queue.pop(0)  # Remove ONLY on confirmed success
            _save_queue(ACCEPTED_Q, queue)
            cleanup_ticket_artifacts(tid)
            
            # Phase 7: Advance System Evolution (Auto-Create Agents if gap detected)
            trigger_auto_evolution(entry)
            
            # Phase 8: Broadcast to Ecosystem (Bus + Blackboard)
            broadcast_success_event(entry)
            
            log(f"[{tid}] ===== OID EXTRACTION COMPLETE =====\n")
        else:
            queue.pop(0)  # Remove from front
            if retries < MAX_RETRIES - 1:
                entry["retry_count"] = retries + 1
                queue.append(entry)  # Move to back of queue
                log(f"[{tid}] Extraction failed (Attempt {retries + 1}/{MAX_RETRIES}) — Re-queued to the back of Accepted Queue.", "WARN")
            else:
                log(f"[{tid}] Extraction failed {MAX_RETRIES} times. Moving to REJECTED queue.", "ERROR")
                _append_queue(REJECTED_Q, entry)
            _save_queue(ACCEPTED_Q, queue)
            time.sleep(2)  # Slight cooldown

    except Exception:
        log(f"[{tid}] CRITICAL EXCEPTION:\n{traceback.format_exc()}", "ERROR")
        queue.pop(0)
        if retries < MAX_RETRIES - 1:
            entry["retry_count"] = retries + 1
            queue.append(entry)
            log(f"[{tid}] Crash triggered (Attempt {retries + 1}/{MAX_RETRIES}) — Re-queued to the back of Accepted Queue.", "WARN")
        else:
            log(f"[{tid}] Critical failure {MAX_RETRIES} times. Moving to REJECTED queue.", "ERROR")
            _append_queue(REJECTED_Q, entry)
        _save_queue(ACCEPTED_Q, queue)
        time.sleep(5)


# ── Main poller: scan Vault/DATA for new raw tickets ─────────────────────────

def poll_vault_for_new_tickets():
    """
    Scan VAULT_DATA_DIR for new JSON intake tickets deposited by:
    - The Bridge gateway (Luong 1 — Telegram/Zalo/etc.)
    - CEO direct Vault commands (Luong 2)

    Each ticket is triaged and routed to the correct queue.
    """
    pattern = str(VAULT_DATA_DIR / "KI-*.json")
    files = sorted(glob.glob(pattern))

    for fpath in files:
        fpath = Path(fpath)
        try:
            ticket = json.loads(fpath.read_text(encoding="utf-8"))
        except Exception as e:
            log(f"Invalid ticket JSON {fpath.name}: {e}", "ERROR")
            fpath.unlink(missing_ok=True)
            continue

        source = ticket.get("source", "")
        tid = ticket.get("id", f"KI-{int(time.time())}")
        stype = ticket.get("source_type", "url")

        if not source:
            log(f"[{tid}] Empty source field — discarding ticket", "WARN")
            fpath.unlink(missing_ok=True)
            continue

        log(f"[{tid}] New ticket detected: {source[:80]}")

        # Run full triage (dedup + security + classification)
        result = triage(source, tid)
        verdict = result.get("verdict", "REJECTED")

        entry = {
            "id": tid,
            "source": source,
            "source_type": stype,
            "triage": result,
            "queued_at": datetime.now().isoformat()
        }

        if verdict == "ACCEPTED":
            _append_queue(ACCEPTED_Q, entry)
            log(f"[{tid}] Routed -> ACCEPTED QUEUE (domain={result.get('domain')})")
        elif verdict == "PENDING":
            _append_queue(PENDING_Q, entry)
            log(f"[{tid}] Routed -> PENDING VAULT — CEO review required")
        else:
            _append_queue(REJECTED_Q, entry)
            log(f"[{tid}] Routed -> REJECTED — reason: {result.get('reason')}")

        fpath.unlink()  # Remove raw ticket — it's now in the appropriate queue


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    enforce_single_instance()
    log("=" * 60)
    log("OmniClaw OID V2 Daemon — ONLINE")
    log(f"Root: {OMNICLAW_ROOT}")
    log(f"Polling: {VAULT_DATA_DIR}")
    log("=" * 60)

    try:
        while True:
            poll_vault_for_new_tickets()   # Route raw tickets to queues
            process_one_accepted()         # Deep-process 1 accepted item per tick
            time.sleep(POLL_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        log("OID Daemon stopped by operator — safe shutdown")
    finally:
        release_lock()


if __name__ == "__main__":
    main()
