#!/usr/bin/env python3
"""
[daemon_manager.py] OmniClaw Stealth Boot Manager
Handles PID tracking and execution of core daemons in the background.
"""
import os
import sys
import json
import subprocess
import time

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))
PID_FILE = os.path.join(ROOT, "vault/tmp/daemons.pid")

DAEMONS = [
    "core/daemons/ohd_health.py",
    "core/daemons/obd_harbor.py",
    "core/daemons/oiw_intake.py",
    "core/daemons/oma_architect.py",
    "core/daemons/oer_registry.py",
    "core/daemons/oa_academy.py"
]

def load_pids():
    if os.path.exists(PID_FILE):
        try:
            with open(PID_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}

def save_pids(pids):
    os.makedirs(os.path.dirname(PID_FILE), exist_ok=True)
    with open(PID_FILE, "w", encoding="utf-8") as f:
        json.dump(pids, f, indent=4)

def is_running(pid):
    try:
        # Tasklist check for Windows
        output = subprocess.check_output(f'tasklist /FI "PID eq {pid}" /NH', shell=True).decode()
        return str(pid) in output
    except Exception:
        return False

def start_daemons():
    pids = load_pids()
    new_pids = {}
    
    print("\033[96m[STAT]\033[0m Initiating Stealth Spawn for Core Daemons...")
    
    for d_rel in DAEMONS:
        d_path = os.path.join(ROOT, d_rel.replace('/', os.sep))
        if not os.path.exists(d_path):
            print(f"  \033[93m[WARN]\033[0m Cannot find: {d_rel}")
            continue

        # Check existing
        existing_pid = pids.get(d_rel)
        if existing_pid and is_running(existing_pid):
            print(f"  \033[92m[OK]\033[0m {d_rel} already running (PID: {existing_pid}). Skipped to prevent duplicates.")
            new_pids[d_rel] = existing_pid
            continue
            
        print(f"  \033[94m[INFO]\033[0m Spawning {d_rel}...")
        try:
            # CREATE_NO_WINDOW = 0x08000000 for detached stealth processing
            CREATE_NO_WINDOW = 0x08000000
            cmd_args = [sys.executable, d_path]
            # OHD requirements flag
            if "ohd_health.py" in d_rel:
                cmd_args.append("--watch")
                
            proc = subprocess.Popen(cmd_args, creationflags=CREATE_NO_WINDOW, cwd=ROOT)
            new_pids[d_rel] = proc.pid
            print(f"    -> Spawned PID: {proc.pid}")
        except Exception as e:
            print(f"  \033[91m[ERR]\033[0m Failed to spawn {d_rel}: {e}")

    save_pids(new_pids)
    print("\033[92m[OK]\033[0m All designated Daemons pushed to background successfully.")

def stop_daemons():
    pids = load_pids()
    if not pids:
        print("\033[94m[INFO]\033[0m No registered PID file found. System already completely stopped.")
        return
        
    print("\033[91m[STAT]\033[0m Executing Order 66: Terminating all Core Daemons...")
    
    for d_rel, pid in pids.items():
        if is_running(pid):
            print(f"  \033[94m[INFO]\033[0m Terminating {d_rel} (PID: {pid})...")
            try:
                subprocess.run(f"taskkill /F /PID {pid}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except Exception as e:
                print(f"    -> \033[91m[ERR]\033[0m Failed: {e}")
        else:
            print(f"  \033[93m[WARN]\033[0m {d_rel} (PID: {pid}) was already dead.")
            
    if os.path.exists(PID_FILE):
        os.remove(PID_FILE)
    print("\033[92m[OK]\033[0m Core Daemons neutralized.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python daemon_manager.py [start|stop]")
        sys.exit(1)
        
    cmd = sys.argv[1].lower()
    if cmd == "start":
        start_daemons()
    elif cmd == "stop":
        stop_daemons()
    else:
        print("Unknown command. Use [start] or [stop].")
