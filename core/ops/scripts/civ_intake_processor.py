import os
import shutil
import time
import sys
import subprocess
from datetime import datetime

OMNICLAW_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
OER_INBOX = os.path.join(OMNICLAW_ROOT, 'vault', 'tmp', 'state_queues', 'OER_INBOX')
QUARANTINE_DIR = os.path.join(OMNICLAW_ROOT, 'vault', 'quarantine')

def run_intake():
    os.makedirs(OER_INBOX, exist_ok=True)
    if not os.path.exists(QUARANTINE_DIR):
        print(f"Directory not found: {QUARANTINE_DIR}")
        return

    print("==================================================")
    print(" 🚀 OMNICLAW: CIV INTAKE / OSF GATEKEEPER ")
    print("==================================================")

    while True:
        items = os.listdir(QUARANTINE_DIR)
        pending = [i for i in items if os.path.isdir(os.path.join(QUARANTINE_DIR, i))]
        
        if not pending:
            print(f"[{datetime.now().strftime('%H:%M:%S')}] Intake Queue Empty. Waiting for Network Drops...")
            time.sleep(10)
            continue
            
        print(f"[{datetime.now().strftime('%H:%M:%S')}] Found {len(pending)} dropped repositories. Engaging OSF Guard...")
        
        censor_script = os.path.join(OMNICLAW_ROOT, 'core', 'ops', 'scripts', 'osf_malware_censor.py')
        
        for repo in pending[:10]: # Process in batches of 10
            src = os.path.join(QUARANTINE_DIR, repo)
            dest = os.path.join(OER_INBOX, repo)
            try:
                # 1. Handshake: OSF Validation
                print(f" -> [OSF SCAN] {repo}")
                scan_res = subprocess.run([sys.executable, censor_script, '--target', src], capture_output=True, text=True)
                
                if scan_res.returncode != 0:
                    print(f"\033[91m [X] OSF BLOCKED: {repo}. Vaporizing immediately!\033[0m")
                    shutil.rmtree(src, ignore_errors=True)
                    continue

                # 2. Handshake: OER Inbox Handoff
                if os.path.exists(dest):
                    print(f" [WARN] Duplicate found in Inbox. Discarding.")
                    shutil.rmtree(src)
                else:
                    shutil.move(src, dest)
                print(f" [✓] OSF PASSED. Handoff to OER_INBOX: {repo[:40]}...")
            except Exception as e:
                print(f" [X] Architecture Error on {repo}: {e}")
                
        time.sleep(2) # Breathing room for IO

if __name__ == "__main__":
    run_intake()
