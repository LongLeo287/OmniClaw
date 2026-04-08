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
from daemon_utils import queue_enqueue, queue_dequeue, queue_mark_success, queue_mark_failed, call_omniclaw_model

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

def harvest_github_txt():
    """Reads user pasted github.txt, deduplicates URLs, and moves them to repos_pending.txt"""
    data_dir = abs_path("vault/assets/data")
    github_txt = os.path.join(data_dir, "github.txt")
    pending_txt = os.path.join(data_dir, "repos_pending.txt")
    selected_txt = os.path.join(data_dir, "repos_selected.txt")
    rejected_txt = os.path.join(data_dir, "repos_rejected.txt")
    
    if not os.path.exists(github_txt):
        return

    def normalize_link(link):
        l = link.strip().lower()
        if l.endswith(".git"): l = l[:-4]
        if l.endswith("/"): l = l[:-1]
        return l

    # Load existing links to avoid duplication
    existing = set()
    for file_path in [pending_txt, selected_txt, rejected_txt]:
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    clean = normalize_link(line)
                    if clean: existing.add(clean)
                    
    new_links = set()
    with open(github_txt, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            if not line.strip(): continue
            norm = normalize_link(line)
            if norm and norm.startswith("http") and norm not in existing:
                new_links.add(line.strip()) # keep original case
                existing.add(norm)
                
    # Filter only truly new links
    to_add = new_links
    if to_add:
        print(f"\033[94m[INFO]\033[0m [OIW] Harvested {len(to_add)} NEW unique repositories from github.txt.")
        with open(pending_txt, "a", encoding="utf-8") as f:
            for l in sorted(to_add):
                f.write(l + "\n")
    else:
        print(f"\033[94m[INFO]\033[0m [OIW] No new unique repositories found in github.txt.")

    # Wipe github.txt clean
    with open(github_txt, "w", encoding="utf-8") as f:
        f.write("")
    print(f"\033[92m[OK]\033[0m [OIW] Cleared github.txt successfully.")



def process_selected_repos():
    """Reads repos_selected.txt, clones a small batch, and removes them from the file to continue the data flow."""
    selected_path = abs_path("vault/assets/data/repos_selected.txt")
    if not os.path.exists(selected_path):
        return

    with open(selected_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    if not lines:
        return

    batch = lines[:10]  # Clone 10 at a time to keep throughput high but network stable
    remaining = lines[10:]

    print(f"\n\033[96m[STAT]\033[0m [OIW] Autobot pulling {len(batch)} AI-Approved Repos for Cloning...")
    
    for url in batch:
        target_name = url.strip("/").split("/")[-1].replace(".git", "")
        task_payload = {
            "source": url,
            "type": "repo",
            "dest_hint": "quarantine",
            "target_skill": target_name,
            "civ_approved": True
        }
        process_task(task_payload)

    # Overwrite selected with remaining un-processed
    with open(selected_path, "w", encoding="utf-8") as f:
        f.write("\n".join(remaining) + ("\n" if remaining else ""))

    print(f"\033[92m[OK]\033[0m [OIW] Finished cloning cycle. {len(remaining)} repos waiting in Selected list.\n")

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

def apply_security_shield_legacy(target_dir):
    # [OSF FIREWALL DELEGATION]
    # OIW no longer performs security scans. This is fully handed over to OSF Daemon.
    # OIW will simply drop the result into SANDBOX and OSF will scan it.
    return True



def apply_gitingest_plow(repo_path: str):
    """
    Simulates or executes a powerful 'gitingest' or similar tool
    to crush the repository into a single high-density context markdown file
    so OA can read it flawlessly.
    """
    print(f"  \033[96m[STAT]\033[0m [OIW] Activating Repo Plow (Gitingest) on {os.path.basename(repo_path)}...")
    ingest_out = os.path.join(repo_path, "_GIT_INGEST.md")
    
    # 1. First, we try to run python -m gitingest if the CLI is available
    try:
        import subprocess
        cmd = ["gitingest", repo_path, "-o", ingest_out, "--exclude", ".git,node_modules,__pycache__,venv"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if res.returncode == 0 and os.path.exists(ingest_out):
            print(f"  \033[92m[OK]\033[0m [OIW] Plowing Complete! Created _GIT_INGEST.md")
            return
    except Exception: pass
    
    # 2. Fallback: Native fast-concat
    print(f"  \033[93m[WARN]\033[0m [OIW] gitingest CLI failed. Using native concatenation plow...")
    try:
        payload = f"# OmniClaw Repo Plow: {os.path.basename(repo_path)}\n\n"
        for root, _, files in os.walk(repo_path):
            if any(x in root for x in [".git", "node_modules", "__pycache__"]): continue
            for f in files:
                if f.endswith((".py", ".js", ".ts", ".md", ".json", ".txt", ".go", ".rs", ".java")):
                    fpath = os.path.join(root, f)
                    try:
                        with open(fpath, "r", encoding="utf-8", errors="ignore") as file:
                            payload += f"\n\n================================================\n"
                            payload += f"FILE: {os.path.relpath(fpath, repo_path)}\n"
                            payload += f"================================================\n"
                            payload += file.read(5000) # Read up to 5k chars per file
                    except: pass
        with open(ingest_out, "w", encoding="utf-8") as fw:
            fw.write(payload)
        print(f"  \033[92m[OK]\033[0m [OIW] Native Plowing Complete! Created _GIT_INGEST.md")
    except Exception as e:
        print(f"  \033[91m[ERR]\033[0m [OIW] Plowing fallback failed: {e}")

def process_task(task: dict):
    """
    Process 1 data task.
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
        dest = SANDBOX  # [OAP PIPELINE UPGRADE] Hand off to OSF Sandbox first!

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
        is_civ = task.get("civ_approved", False)
        prefix = "CIV_FETCHED_" if is_civ else "FETCHED_"
        target_dir = os.path.join(dest, f"{prefix}{target_skill if target_skill else 'repo'}_{datetime.now().strftime('%H%M%S')}")
        
        print(f"  \033[94m[INFO]\033[0m [OIW] Executing git clone...")
        try:
            cmd = ["git", "clone", "--depth", "1", source, target_dir]
            res = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if res.returncode == 0:
                print(f"  \033[92m[OK]\033[0m [OIW] Clone successful to {target_dir}")
                
                # OSF HANDOFF: No security scan here anymore!
                # apply_dependabot_secretary(target_dir) # Removed: OSF Daemon handles this natively in SANDBOX
                
                # [PHASE 1: OIW Repo Plow] Crush it immediately
                apply_gitingest_plow(target_dir)
                
                # Signal OSF, not OHD
                print(f"  \033[94m[INFO]\033[0m [OIW] Passing baton to OSF Sandbox Firewall...")
                fetch_success = True
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
    import time
    print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting - {config['role']}")
    print(f"\033[95m[RULE]\033[0m: {config['action_rule']}\n")

    os.makedirs(SANDBOX, exist_ok=True)
    os.makedirs(QUARANTINE, exist_ok=True)
    os.makedirs(RAW_DUMPS, exist_ok=True)
    os.makedirs(OIW_INBOX, exist_ok=True)

    print(f"\033[92m[STAT]\033[0m [OIW] Intake Daemon entering Perpetual Loop...")
    while True:
        try:
            # 1. Harvest manual pastes from github.txt
            harvest_github_txt()

            # 2. Pull approved repos and actually CLONE them instances
            process_selected_repos()

            # 3. Regular Inbox Processing
            tasks = read_inbox()
            if tasks:
                for task in tasks:
                    process_task(task)
                print(f"\033[92m[OK]\033[0m [OIW] Finished {len(tasks)} Neural MQ task(s).")

            # 5. Check if we still have repos to clone across all queues
            has_more = False
            
            selected_check = abs_path("vault/assets/data/repos_selected.txt")
            if os.path.exists(selected_check) and os.path.getsize(selected_check) > 5:
                has_more = True
                
            pending_check = abs_path("vault/assets/data/repos_pending.txt")
            if os.path.exists(pending_check) and os.path.getsize(pending_check) > 5:
                has_more = True
                
            github_check = abs_path("vault/assets/data/github.txt")
            if os.path.exists(github_check) and os.path.getsize(github_check) > 5:
                has_more = True

            if has_more:
                print(f"\033[96m[STAT]\033[0m [OIW] CEO Throttle Policy: Sleeping for 15 minutes to prevent GitHub rate limiting...")
                time.sleep(900)
            else:
                print(f"\033[93m[WARN]\033[0m [OIW] ALL REPO QUEUES EMTPY! Committing Seppuku (Self-Kill) as ordered by CEO.")
                break
            
        except KeyboardInterrupt:
            print(f"\033[93m[WARN]\033[0m [OIW] Keyboard Interrupt received. Exiting loop.")
            break
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [OIW] Critical Error in Daemon Loop: {e}. Sleeping 60s before retry.")
            time.sleep(60)

if __name__ == "__main__":
    import sys
    if "--single-pass" in sys.argv:
        print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting in SINGLE-PASS mode...")
        os.makedirs(SANDBOX, exist_ok=True)
        os.makedirs(QUARANTINE, exist_ok=True)
        os.makedirs(RAW_DUMPS, exist_ok=True)
        os.makedirs(OIW_INBOX, exist_ok=True)
        harvest_github_txt()
        process_selected_repos()
        tasks = read_inbox()
        if tasks:
            for task in tasks:
                process_task(task)
        print(f"\033[92m[OK]\033[0m [{DAEMON_NAME}] Single pass complete.")
    else:
        run()
