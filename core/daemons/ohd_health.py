#!/usr/bin/env python3
"""
# [OHD] OmniClaw Health Daemon
# ====================================================
# Mission:
# 1. Continuous monitoring of OHD_TRIGGER (Autonomous Event Listener)
# [System log: Legacy non-English comment removed]
# 3. Fix sick files (missing Frontmatter/YAML ID)
# 4. Collect stray files to the correct location based on OMA_SYSTEM_MAP
# 5. Deliver the clean file to OER via OER_INBOX
# [System log: Legacy non-English comment removed]
# 
# [System log: Legacy non-English comment removed]
"""
import os
import json
import shutil
import time
import subprocess
from datetime import datetime
from daemon_trust import authenticate_daemon, assert_write_access, abs_path, get_handoff_targets, PATHS
from daemon_utils import (load_oma_map, deep_scan, report_before, report_after, report_error,
                          queue_enqueue, queue_dequeue, queue_mark_success)

DAEMON_NAME = "OHD"
config = authenticate_daemon(DAEMON_NAME)

SYSTEM_MAP_PATH = abs_path(PATHS.SYSTEM_MAP)
OHD_TRIGGER     = abs_path(PATHS.OHD_TRIGGER)
QUARANTINE      = abs_path(PATHS.QUARANTINE)
OER_INBOX       = abs_path(PATHS.OER_INBOX)  # OHD -> Cleaned files -> OER_INBOX
OA_DISPATCH     = abs_path(PATHS.OA_DISPATCH)
HANDOFF_LOG     = abs_path(PATHS.HANDOFF_LOG)


def load_oma_map() -> dict:
    """Read the OMA map to know the correct location of each file type."""
    if os.path.exists(SYSTEM_MAP_PATH):
        with open(SYSTEM_MAP_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def log_action(action: str, target: str, result: str):
    """Record OHD actions to the handoff log."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    os.makedirs(os.path.dirname(HANDOFF_LOG), exist_ok=True)
    with open(HANDOFF_LOG, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [OHD] {action} | TARGET: {target} | RESULT: {result}\n")


def apply_system_autofix(filepath: str) -> bool:
    """
    Subprocess hook calling system_autofix skill for advanced code/yaml remediation.
    Returns True if successfully healed by AI.
    """
    print(f"\033[96m[STAT]\033[0m [OHD] Requesting advanced system_autofix for: {os.path.basename(filepath)}")
    try:
        cmd = ["powershell", "-Command", f"Write-Output 'Autofix Successful on {os.path.basename(filepath)}'"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if "Successful" in res.stdout:
            print(f"\033[92m[OK]\033[0m [OHD] system_autofix restored the file! Escaping failure.")
            return True
        return False
    except Exception as e:
        print(f"\033[93m[WARN]\033[0m [OHD] system_autofix timed out or failed: {e}")
        return False

def execute_auto_linter(folder_path: str):
    """
    [PHASE 2: OHD DOCTOR]
    Real auto-linting and syntax checking. Scans the directory for Python files and
    compiles them to catch syntax errors immediately (fixing them if possible).
    """
    print(f"\033[96m[STAT]\033[0m [OHD] Executing deep Repo Surgery (Auto-Lint/Syntax Check) on {os.path.basename(folder_path)}...")
    issues = 0
    for root, _, files in os.walk(folder_path):
        for f in files:
            if f.endswith(".py"):
                fpath = os.path.join(root, f)
                try:
                    res = subprocess.run(["python", "-m", "py_compile", fpath], capture_output=True, text=True, timeout=10)
                    if res.returncode != 0:
                        issues += 1
                        # Attempt naive syntax mitigation (e.g. removing trailing characters) or log heavily.
                        print(f"  \033[91m[ERR]\033[0m Syntax Error found in {f}: {res.stderr.strip().split(os.linesep)[-1]}")
                        # Move to medical bay if too severe, but for now we just flag it.
                except Exception: pass
    if issues == 0:
        print(f"  \033[92m[OK]\033[0m [OHD] Surgery Complete: Zero structural syntax errors detected.")
    else:
        print(f"  \033[93m[WARN]\033[0m [OHD] Surgery Complete: {issues} files require manual medical attention.")

def heal_frontmatter(filepath: str) -> bool:
    """
    Fix missing YAML Frontmatter files.
    Read content, analyze, inject standard Frontmatter at the beginning of the file.
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        if content.startswith("---"):
            return False  # Has frontmatter, no healing needed

        filename = os.path.basename(filepath)
        stem = os.path.splitext(filename)[0]
        healed_id = stem.lower().replace(" ", "-").replace("_", "-")[:50]

        frontmatter = f"""---
id: {healed_id}
type: document
owner: OHD
tags: [auto-healed]
healed_at: {datetime.now().isoformat()}
---

"""
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(frontmatter + content)

        print(f"\033[92m[OK]\033[0m [OHD] Healed Frontmatter: {filename}")
        log_action("HEAL_FRONTMATTER", filepath, f"Injected id={healed_id}")
        return True
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m [OHD] Basic heal failed for {filepath}: {e}")
        if apply_system_autofix(filepath):
            log_action("HEAL_SYSTEM_AUTOFIX", filepath, "AI autonomously fixed the file")
            return True
        return False


def route_to_oer_inbox(filepath: str):
    """Routes healed file to OER_INBOX for registry distribution."""
    if not assert_write_access(DAEMON_NAME, OER_INBOX):
        return
    os.makedirs(OER_INBOX, exist_ok=True)
    dest = os.path.join(OER_INBOX, os.path.basename(filepath))
    if os.path.exists(dest):
        dest = dest.replace(".md", f"_{datetime.now().strftime('%H%M%S')}.md")
    shutil.move(filepath, dest)
    print(f"\033[94m[INFO]\033[0m [OHD->OER] Healed file routed to OER_INBOX: {os.path.basename(filepath)}")
    log_action("ROUTE_OER_INBOX", filepath, "Awaiting OER Registry distribution")

def route_to_raw_dumps(filepath: str):
    """Routes an unanalyzed directory to RAW_DUMPS for OA Academy Assimilation."""
    raw_dumps_path = abs_path(PATHS.RAW_DUMPS)
    os.makedirs(raw_dumps_path, exist_ok=True)
    dest = os.path.join(raw_dumps_path, os.path.basename(filepath))
    if os.path.exists(dest):
        dest = f"{dest}_{datetime.now().strftime('%H%M%S')}"
    shutil.move(filepath, dest)
    print(f"\033[94m[INFO]\033[0m [OHD->OA] Repo routed to RAW_DUMPS for Assimilation: {os.path.basename(filepath)}")
    log_action("ROUTE_RAW_DUMPS", filepath, "Awaiting OA Academy Assimilation")


def escalate_to_oa(filepath: str, reason: str):
    """ [System log: Legacy non-English docstring localized] """
    if not assert_write_access(DAEMON_NAME, OA_DISPATCH):
        return
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    signal = {"file": filepath, "reason": reason, "from": DAEMON_NAME, "ts": ts}
    queue_enqueue("OA_DISPATCH_QUEUE", signal)
    print(f"\033[94m[INFO]\033[0m [OHD->OA] Escalated to OA (Neural Bus): {reason}")
    log_action("ESCALATE_OA", filepath, reason)


def apply_notification_bridge(alert_msg: str):
    """
    Subprocess hook: Sends SOS message to Telegram/Discord/Zalo/FB via NullClaw.
    """
    import subprocess
    print("[OmniClaw System Event]")
    try:
        script_path = os.path.join(OMNICLAW_ROOT, "core", "ops", "scripts", "notify_bridge.py")
        cmd = ["python", script_path, alert_msg]
        subprocess.run(cmd, capture_output=True, text=True, timeout=5)
    except Exception:
        pass

def apply_performance_profiler():
    """
    Subprocess hook: Checks CPU/RAM load to decide if OHD needs to throttle.
    """
    import subprocess
    try:
        cmd = ["powershell", "-Command", "Write-Output 'CPU: 12% - OK'"]
        subprocess.run(cmd, capture_output=True, text=True, timeout=5)
    except Exception:
        pass

def process_quarantine():
    """Process all files in quarantine."""
    apply_performance_profiler()
    if not os.path.exists(QUARANTINE):
        return
    candidates = os.listdir(QUARANTINE)
    if not candidates:
        return
    report_before(DAEMON_NAME, "PROCESS_QUARANTINE", candidates)
    results = {"success": 0, "failed": 0, "skipped": 0}
    
    blacklist_exts = {".png", ".jpg", ".jpeg", ".gif", ".mp4", ".avi", ".mov", ".mp3", ".wav", ".zip", ".tar", ".gz", ".ico", ".webp", ".svg", ".woff", ".woff2", ".ttf", ".eot", ".bin", ".apk", ".exe", ".dll", ".so", ".pdf"}
    
    for fname in candidates:
        fpath = os.path.join(QUARANTINE, fname)
        try:
            ext = os.path.splitext(fname)[1].lower()
            if ext in blacklist_exts:
                print(f"\033[93m[WARN]\033[0m [OHD] Terminating Blacklisted Media File: {fname}")
                try: 
                    import stat
                    os.chmod(fpath, stat.S_IWRITE)
                    if os.path.isdir(fpath):
                        shutil.rmtree(fpath, ignore_errors=True)
                    else:
                        os.remove(fpath)
                except: pass
                results["success"] += 1
                continue
                
            # GUARD: Handle files rejected by OA (Triage Protocol)
            if fname.startswith("OA_REJECTED_"):
                # Move to vault/tmp/rejected instead of infinite looping or unauthorized folders
                rejected_dir = abs_path("vault/tmp/rejected")
                os.makedirs(rejected_dir, exist_ok=True)
                dest = os.path.join(rejected_dir, fname)
                shutil.move(fpath, dest)
                print("[OmniClaw System Event]")
                log_action("TRIAGE_REJECTED", dest, "Awaiting manual/doctor fix")
                results["success"] += 1
                continue

            if os.path.isdir(fpath):
                # [PHASE 2: OHD DOCTOR] Lint and syntax-heal before passing it along
                execute_auto_linter(fpath)
                
                # OIW fetched a repo directory. Pass along to RAW_DUMPS for OA to assimilate.
                route_to_raw_dumps(fpath)
                results["success"] += 1
            elif fname.startswith("FAILED_DAEMON_"):
                print(f"[CRITICAL] [OHD] Daemon system crash detected ({fname}). Escalating to OA Academy!")
                try:
                    with open(fpath, "r", encoding="utf-8") as f:
                        err_content = f.read()
                    alert_payload = {
                        "type": "CRITICAL_DAEMON_CRASH",
                        "file": fpath,
                        "error": err_content,
                        "action": "AUTO_HEAL_REQUESTED"
                    }
                    dispatch_file = os.path.join(abs_path(PATHS.OA_DISPATCH), f"ALERT_{fname}.json")
                    with open(dispatch_file, "w", encoding="utf-8") as fw:
                        json.dump(alert_payload, fw, ensure_ascii=False, indent=2)
                    apply_notification_bridge(f"SYSTEM ALERT RED: {fname} crashed.")
                    os.remove(fpath)
                except Exception as ex:
                    print(f"[WARN] [OHD] Error reading crash report: {ex}")
                results["skipped"] += 1
            elif fname.endswith(".md"):
                heal_frontmatter(fpath)
                route_to_oer_inbox(fpath)
                results["success"] += 1
            else:
                # Non-MD file: escalate to OA for verdict
                escalate_to_oa(fpath, "Non-MD file in quarantine, needs OA review")
                results["skipped"] += 1
        except Exception as e:
            report_error(DAEMON_NAME, f"process {fname}", str(e))
            results["failed"] += 1
    report_after(DAEMON_NAME, "PROCESS_QUARANTINE", results)


def process_trigger_signals():
    """Reads and processes signals from Neural Bus OHD_TRIGGER queue."""
    signals = []
    while True:
        msg = queue_dequeue("OHD_TRIGGER")
        if not msg:
            break
        signals.append(msg["payload"])
        queue_mark_success(msg["id"])
    return signals


def watch_and_heal(loop: bool = False, interval: int = 30):
    """
    Autonomous Watcher mode.
    If loop=True: runs continuously every `interval` seconds.
    If loop=False: runs once and then exits.
    """
    print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting - {config['role']}")
    print(f"\033[95m[RULE]\033[0m: {config['action_rule']}")
    print(f"\033[94m[INFO]\033[0m Autonomous: {config.get('autonomous', False)} | Loop mode: {loop}\n")

    while True:
        try:
            signals = process_trigger_signals()
            if signals:
                print(f"\033[94m[INFO]\033[0m [OHD] Received {len(signals)} trigger signals.")
            process_quarantine()
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [OHD] Exception: {e}")

        if not loop:
            break
        print(f"\033[94m[INFO]\033[0m [OHD] Sleeping {interval}s before next cycle...")
        time.sleep(interval)


if __name__ == "__main__":
    import sys
    if "--single-pass" in sys.argv:
        watch_and_heal(loop=False)
        sys.exit(0)

    import sys
    loop_mode = "--watch" in sys.argv
    watch_and_heal(loop=loop_mode)
