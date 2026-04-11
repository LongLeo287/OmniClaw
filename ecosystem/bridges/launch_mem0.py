import os
import sys
import subprocess

# Hardcoded Port Assignment (Enforced by backend repo compatibility)
PORT = "7000"

current_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(current_dir, "..", "..", "..", "OmniClaw REMOTE", "plugins", "mem0")

if not os.path.exists(TARGET_DIR):
    print(f"[OmniClaw Bridge] ERR: Mem0 target directory not found: {TARGET_DIR}")
    sys.exit(1)

os.chdir(TARGET_DIR)

print(f"[OmniClaw Bridge] Launching Mem0 API Server from {TARGET_DIR} on Port {PORT}...")
COMMAND = ["poetry", "run", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", str(PORT)]

try:
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("\n[OmniClaw Bridge] Mem0 stopped safely.")
except Exception as e:
    print(f"[OmniClaw Bridge] Mem0 crashed: {e}")
