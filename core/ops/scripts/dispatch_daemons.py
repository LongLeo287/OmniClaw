import os
import json
import subprocess
from datetime import datetime
from pathlib import Path

# Paths
ROOT_DIR = r"D:\LongLeo\AI OS CORP\AI OS"
OER_SCRIPT = os.path.join(ROOT_DIR, "core", "ops", "scripts", "oer_register.py")
OIW_INBOX = os.path.join(ROOT_DIR, "vault", "tmp", "state_queues", "OIW_INBOX")
OIW_SCRIPT = os.path.join(ROOT_DIR, "core", "daemons", "daemon_run_oiw.ps1")
REPORT_FILE = os.path.join(ROOT_DIR, "vault", "tmp", "sandbox_env", "OA_workshop", "CONTENT_UPGRADE_AUDIT.md")
SKILLS_DIR = os.path.join(ROOT_DIR, "ecosystem", "skills")

def parse_report():
    healthy = []
    empty_or_data = []
    
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    current_section = 0
    for line in lines:
        if line.startswith("## 🔴 1. Empty Skills") or line.startswith("## 🟡 2. Skills With Data"):
            current_section = 1
        elif line.startswith("## 🟢 3. Healthy Skills"):
            current_section = 2
            
        if line.startswith("- ") and line.endswith("\n"):
            skill_name = line.split("")[1]
            if current_section == 1:
                empty_or_data.append(skill_name)
            elif current_section == 2:
                healthy.append(skill_name)
                
    return healthy, empty_or_data

def dispatch():
    healthy, empty_or_data = parse_report()
    
    print("\n==================================")
    print("1. DISPATCH OER TASKS (29 HEALTHY SKILLS)")
    print("==================================")
    for skill in healthy:
        print(f"[OER] Syncing & Registering: {skill}")
        # Call OER directly for each skill. In this implementation, OER updates the map.
        cmd = f'python "{OER_SCRIPT}" --path "ecosystem/skills/{skill}" --type skill --name "{skill}"'
        subprocess.run(cmd, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
    print("\n==================================")
    print("2. DISPATCH OIW FETCH TASKS (54 SKILLS)")
    print("==================================")
    os.makedirs(OIW_INBOX, exist_ok=True)
    
    for i, skill in enumerate(empty_or_data):
        task_id = f"oiw_fetch_{skill}_{datetime.now().strftime('%H%M%S')}_{i}"
        task_data = {
            "source": f"[GIT/WEB REPO MAPPING NEEDED FOR: {skill}]",
            "type": "repo",
            "target_skill": skill,
            "dest_hint": "quarantine"
        }
        with open(os.path.join(OIW_INBOX, f"{task_id}.json"), "w", encoding="utf-8") as f:
            json.dump(task_data, f, ensure_ascii=False, indent=2)
            
    print(f"[OIW] Pushed 54 tasks into OIW_INBOX. (Waiting for OIW Daemon to pick up...)")
    
    # Launch OIW in background
    print("\nActivating OIW Daemon (Background)...")
    subprocess.Popen(["powershell", "-File", OIW_SCRIPT], creationflags=subprocess.CREATE_NEW_CONSOLE | getattr(subprocess, 'DETACHED_PROCESS', 0x00000008))
    
    print("\n✅ DAEMON DISPATCH COMPLETE (Running independently on CLI). Handoff complete!")

if __name__ == '__main__':
    dispatch()
