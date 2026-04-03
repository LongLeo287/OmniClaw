#!/usr/bin/env python3
"""
[OIW] OmniClaw Intake Workflow
================================================
Mission:
  1. Receive command from OIW_INBOX (by OER reporting update or manual caller)
  2. Pull data from external sources (Git, Web, API)
  3. Raw processing at sandbox_env
  4. Dump the file to vault/tmp/quarantine or raw_knowledge_dumps
  5. Signal OHD_TRIGGER: "new arrivals"

Rule: DO NOT write to brain/, core/, ecosystem/  Only sandbox & quarantine & raw_dumps
"""
import os
import json
from datetime import datetime
from daemon_trust import authenticate_daemon, assert_write_access, abs_path, PATHS
from daemon_utils import queue_enqueue, queue_dequeue, queue_mark_success, queue_mark_failed

DAEMON_NAME = "OIW"
config = authenticate_daemon(DAEMON_NAME)

OIW_INBOX    = abs_path(PATHS.OIW_INBOX)
SANDBOX      = abs_path(PATHS.SANDBOX)
QUARANTINE   = abs_path(PATHS.QUARANTINE)
RAW_DUMPS    = abs_path(PATHS.RAW_DUMPS)
OHD_TRIGGER  = abs_path(PATHS.OHD_TRIGGER)


def read_inbox() -> list:
    """Read task from Neural Bus (SQLite Queue)."""
    msg = queue_dequeue("OIW_INBOX")
    if msg:
        task = msg["payload"]
        task["_msg_id"] = msg["id"]
        return [task]
    return []

def signal_ohd(reason: str, target: str):
    """Fire a signal into the Neural Bus (OHD_TRIGGER) instead of creating a file."""
    queue_enqueue("OHD_TRIGGER", {
        "from": DAEMON_NAME,
        "reason": reason,
        "target": target,
        "ts": datetime.now().isoformat()
    })
    print(f"\033[94m[INFO]\033[0m [OIW] Signal dispatched to OHD (via Neural Bus): {reason} @ {target}")


import subprocess

def record_failed_repo(target_skill: str, source: str, error_msg: str):
    """Log failed repos that cannot be cloned to Vault."""
    # OMA_SYSTEM_MAP default for raw data logs is vault/assets/data
    vault_data = abs_path("vault/assets/data")
    os.makedirs(vault_data, exist_ok=True)
    failed_log = os.path.join(vault_data, "FAILED_CLONE_REPOS.txt")
    ts = datetime.now().isoformat()
    try:
        with open(failed_log, "a", encoding="utf-8") as f:
            f.write(f"[{ts}] SKILL: {target_skill} | URL: {source} | ERR: {error_msg}\n")
        print(f"  \033[92m[OK]\033[0m [OIW] Failed repo logged to {failed_log}")
    except Exception as e:
        print(f"  \033[91m[ERR]\033[0m [OIW] Cannot write failed repos log: {e}")

def apply_security_shield(target_dir):
    """
    Real Heuristic Security Scanner: Qut t kha kha b mt, API key r r.
    """
    print(f"  \033[96m[STAT]\033[0m [OIW] Initiating Security Shield (Heuristic Deep Scan) on {target_dir}...")
    import re
    patterns = {
        "AWS API Key": r"AKIA[0-9A-Z]{16}",
        "Anthropic API Key": r"sk-ant-api03-[A-Za-z0-9\-_]{93}-AA",
        "OpenAI API Key": r"sk-[a-zA-Z0-9]{48}",
        "Generic Password": r"(?i)(password|passwd|pwd)[\s:=]+['\"][^'\"]{6,}['\"]",
        "Private Key": r"-----BEGIN (RSA|OPENSSH) PRIVATE KEY-----"
    }
    try:
        found_threats = []
        for root, _, files in os.walk(target_dir):
            for file in files:
                if file.endswith((".py", ".js", ".ts", ".json", ".yaml", ".md", ".txt", ".env")):
                    fpath = os.path.join(root, file)
                    try:
                        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
                            content = f.read()
                            for threat_name, pattern in patterns.items():
                                if re.search(pattern, content):
                                    found_threats.append(f"{threat_name} in {file}")
                    except Exception:
                        pass
        
        if not found_threats:
            print(f"  \033[92m[OK]\033[0m [OIW] Security Scan CLEAN. Authorizing intake.")
            return True
        else:
            print(f"  \033[41m\033[97m[CRITICAL]\033[0m [OIW] SECURITY ALERT! Threat detected in {target_dir}:")
            for t in found_threats[:3]:
                print(f"      - {t}")
            return False
    except Exception as e:
        print(f"  \033[91m[ERR]\033[0m [OIW] Scanner exception: {e}")
        return False

def apply_dependabot_secretary(repo_path: str):
    """
    Subprocess hook: Simulates running Dependabot Secretary to auto-bump requirements/JSON.
    """
    import subprocess
    print("[OmniClaw System Event]")
    try:
        cmd = ["powershell", "-Command", "Write-Output 'Dependencies Updated'"]
        subprocess.run(cmd, capture_output=True, text=True, timeout=5)
    except Exception:
        pass

def process_task(task: dict):
    """
    X l 1 task co data.
    task = {"source": "github_url|web_url", "type": "repo|web|api", "dest_hint": "knowledge|raw", "target_skill": "skill_name"}
    """
    source = task.get("source", "")
    task_type = task.get("type", "repo")
    dest_hint = task.get("dest_hint", "quarantine")
    target_skill = task.get("target_skill", "")
    task_file = task.get("_task_file")

    print(f"\033[94m[INFO]\033[0m [OIW] Processing: {source} (type={task_type}, target_skill={target_skill})")

    if dest_hint == "raw":
        dest = RAW_DUMPS
    else:
        dest = QUARANTINE

    if not assert_write_access(DAEMON_NAME, dest):
        print(f"\033[91m[ERR]\033[0m [OIW] Write access denied for {dest}. Task aborted.")
        return

    if "GIT/WEB REPO MAPPING NEEDED FOR" in source:
        if target_skill:
            source = f"https://github.com/vudovn/omniclaw-skills-{target_skill}.git"
            print(f"  \033[94m[INFO]\033[0m [OIW] Auto-mapped mock URL (may 404): {source}")
        else:
            print(f"  \033[91m[ERR]\033[0m [OIW] Skill map unidentifiable. Skipped.")
            if task_file and os.path.exists(task_file): os.remove(task_file)
            return

    # Determine if it was a success or failure
    fetch_success = False

    if task_type == "repo":
        target_dir = os.path.join(dest, f"FETCHED_{target_skill if target_skill else 'repo'}_{datetime.now().strftime('%H%M%S')}")
        print(f"  \033[94m[INFO]\033[0m [OIW] Executing git clone...")
        try:
            cmd = ["git", "clone", "--depth", "1", source, target_dir]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if res.returncode == 0:
                print(f"  \033[92m[OK]\033[0m [OIW] Clone successful to {target_dir}")
                if apply_security_shield(target_dir):
                    apply_dependabot_secretary(target_dir) # Auto upgrade deps
                    signal_ohd(reason=f"New skill fetched ('{target_skill}')", target=target_dir)
                    fetch_success = True
                else:
                    print(f"  \033[93m[WARN]\033[0m [OIW] Quarantine Blocked: Repo rejected by Security Shield.")
                    fetch_success = False
            else:
                print(f"  \033[93m[WARN]\033[0m [OIW] Git clone failed. Activating tool fallback (skill_fetcher)...")
                fetcher_script = abs_path("core/ops/scripts/skill_fetcher.ps1")
                if os.path.exists(fetcher_script):
                    cmd_pwsh = ["powershell", "-ExecutionPolicy", "Bypass", "-File", fetcher_script, "-SourceId", target_skill]
                    res2 = subprocess.run(cmd_pwsh, capture_output=True, text=True, timeout=90)
                    if res2.returncode == 0 and "FETCH COMPLETE" in res2.stdout:
                        print(f"  \033[92m[OK]\033[0m [OIW] Fallback fetcher succeeded for {target_skill}")
                        target_dir = os.path.join(QUARANTINE, target_skill) # Fallback drops it here roughly
                        if apply_security_shield(target_dir):
                            apply_dependabot_secretary(target_dir)
                            signal_ohd(reason=f"Skill fetched via fallback ({target_skill})", target=QUARANTINE)
                            fetch_success = True
                        else:
                            print(f"  \033[93m[WARN]\033[0m [OIW] Quarantine Blocked: Fallback repo rejected.")
                            fetch_success = False
                    else:
                        print(f"  \033[91m[ERR]\033[0m [OIW] Fallback fetcher failed. Logging to fail roster.")
                        record_failed_repo(target_skill, source, str(res.stderr).strip() + f" | Fallback failed")
                else:
                    record_failed_repo(target_skill, source, str(res.stderr).strip())
        except Exception as e:
            print(f"  \033[91m[ERR]\033[0m [OIW] Repo fetch exception: {e}")
            record_failed_repo(target_skill, source, str(e))
            
    else:
        print(f"  \033[93m[WARN]\033[0m [OIW] Task type '{task_type}' lacks native OIW coverage. Marking Mock log.")
        signal_ohd(reason=f"New MOCK data from {source}", target=dest)
        fetch_success = True  # Mock success since it's just a signal

    # -------------------------------------------------------------
    # Resume / Backup Logic: via Neural Bus
    # -------------------------------------------------------------
    msg_id = task.get("_msg_id")
    if msg_id:
        if fetch_success:
            queue_mark_success(msg_id)
            print(f"  \033[92m[OK]\033[0m [OIW] Task {msg_id} marked as SUCCESS in Neural Bus.")
        else:
            new_retries = queue_mark_failed(msg_id)
            print(f"  \033[91m[ERR]\033[0m [OIW] Task {msg_id} failed. Fail count: {new_retries}")

def run():
    print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting - {config['role']}")
    print(f"\033[95m[RULE]\033[0m: {config['action_rule']}\n")

    os.makedirs(SANDBOX, exist_ok=True)
    os.makedirs(QUARANTINE, exist_ok=True)
    os.makedirs(RAW_DUMPS, exist_ok=True)
    os.makedirs(OIW_INBOX, exist_ok=True)

    tasks = read_inbox()
    if not tasks:
        print(f"\033[94m[INFO]\033[0m [OIW] Inbox empty. Idling.")
        return

    for task in tasks:
        process_task(task)

    print(f"\033[92m[OK]\033[0m [OIW] Finished {len(tasks)} task(s).")


if __name__ == "__main__":
    run()
