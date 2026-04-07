import os
import shutil
import time

OMNICLAW_ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
REPORT_FILE = os.path.join(OMNICLAW_ROOT, "vault", "tmp", "sandbox_env", "OA_workshop", "CONTENT_UPGRADE_AUDIT.md")
OER_INBOX = os.path.join(OMNICLAW_ROOT, "vault", "tmp", "state_queues", "OER_INBOX")
ECOSYSTEM_SKILLS = os.path.join(OMNICLAW_ROOT, "ecosystem", "skills")

def get_healthy_skills():
    healthy = []
    current_section = 0
    with open(REPORT_FILE, "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith("## 🟢 3. Skills Healthy"):
                current_section = 2
            elif line.startswith("## "):
                current_section = 0
                
            if current_section == 2 and line.startswith("- "):
                skill = line.replace("- ", "").replace("", "").strip()
                if skill:
                    healthy.append(skill)
    return healthy

def drop_to_oer_inbox():
    healthy_skills = get_healthy_skills()
    os.makedirs(OER_INBOX, exist_ok=True)
    count = 0
    for skill in healthy_skills:
        src = os.path.join(ECOSYSTEM_SKILLS, skill)
        dest = os.path.join(OER_INBOX, f"RE_REG_{skill}")
        if os.path.exists(src) and os.path.isdir(src):
            try:
                # Copy entire folder to OER_INBOX so OER registers it and overwrites safely
                shutil.copytree(src, dest, dirs_exist_ok=True)
                count += 1
            except Exception as e:
                print(f"Error copying {skill}: {e}")
    print(f"[+] Dropped {count} healthy skills to OER_INBOX for re-registration.")

if __name__ == '__main__':
    drop_to_oer_inbox()
