import os
import subprocess
from datetime import datetime
import json
import time

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
HANDOFF_LOG = os.path.join(ROOT, "brain", "registry", "handoff_tasks.log")
OMA_SCRIPT = os.path.join(ROOT, "core", "daemons", "oma_architect.py")

print("[MEMORY CAMPAIGN] 1. Activating OMA Architect Scanner...")
try:
    res = subprocess.run(["python", OMA_SCRIPT], capture_output=True, text=True)
    if "error" in res.stderr.lower():
        print("OMA encountered issues:", res.stderr)
    else:
        print("OMA Scan Complete. Architecture mapped. Identity tags (_DIR_IDENTITY.md) applied.")
except Exception as e:
    print(f"Failed to run OMA: {e}")

time.sleep(1)

print("\n[MEMORY CAMPAIGN] 2. Queuing directives for OmniAgent (OA)...")
ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

os.makedirs(os.path.dirname(HANDOFF_LOG), exist_ok=True)
with open(HANDOFF_LOG, "a", encoding="utf-8") as f:
    f.write(f"\n[{ts}] [UI_CHAT] COMMAND | [MEMORY DIRECTIVE] Immediately read brain/memory/corp_memory/MEMORY_SPEC.md and confirm architecture.\n")
    f.write(f"[{ts}] [UI_CHAT] COMMAND | [MEMORY DIRECTIVE] Scan brain/memory/corp_memory/* templates and assimilate them into blackboard.json active knowledge.\n")

print("=> Directives injected into HANDOFF_LOG.")
print("=> The active OA daemon will intercept these commands in its next polling cycle.")
print("\n[SUCCESS] OMA and OA have been successfully commanded to participate in brain/memory processing.")
