import os
import json
import subprocess
from datetime import datetime

ROOT_DIR = r"D:\LongLeo\AI OS CORP\AI OS"
OER_SCRIPT = os.path.join(ROOT_DIR, "core", "ops", "scripts", "oer_register.py")
OIW_INBOX = os.path.join(ROOT_DIR, "vault", "tmp", "state_queues", "OIW_INBOX")
OIW_SCRIPT = os.path.join(ROOT_DIR, "core", "daemons", "daemon_run_oiw.ps1")
REPORT_FILE = os.path.join(ROOT_DIR, "vault", "tmp", "sandbox_env", "OA_workshop", "CONTENT_UPGRADE_AUDIT.md")
SKILLS_DIR = os.path.join(ROOT_DIR, "ecosystem", "skills")

def parse_report():
    healthy, empty_or_data = [], []
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()
    current_section = 0
    for line in lines:
        if line.startswith("## 🔴 1. Skills Rỗng") or line.startswith("## 🟡 2. Skills Có Data"):
            current_section = 1
        elif line.startswith("## 🟢 3. Skills Healthy"):
            current_section = 2
        
        if line.startswith("- "):
            skill_name = line.replace("- ", "").replace("", "").strip()
            if current_section == 1: empty_or_data.append(skill_name)
            elif current_section == 2: healthy.append(skill_name)
    return healthy, empty_or_data

def dispatch():
    healthy, empty_or_data = parse_report()
    os.makedirs(OIW_INBOX, exist_ok=True)
    for i, skill in enumerate(empty_or_data):
        task_id = f"oiw_fetch_{skill}_{datetime.now().strftime('%H%M%S')}_{i}"
        task_data = {"source": f"[GIT/WEB REPO MAPPING NEEDED FOR: {skill}]", "type": "repo", "target_skill": skill, "dest_hint": "quarantine"}
        with open(os.path.join(OIW_INBOX, f"{task_id}.json"), "w", encoding="utf-8") as f:
            json.dump(task_data, f, ensure_ascii=False, indent=2)
    print(f"[OIW] Regenerated {len(empty_or_data)} tasks into OIW_INBOX.")

if __name__ == '__main__':
    dispatch()
