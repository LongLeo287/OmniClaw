import os
import sys
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(current_dir, "..", "..", "..", "OmniClaw REMOTE", "plugins", "mem0")

if not os.path.exists(TARGET_DIR):
    print(f"Error: Mem0 target directory not found: {TARGET_DIR}")
    sys.exit(1)

os.chdir(TARGET_DIR)

print(f"[Bridge] Launching Mem0 Server from {TARGET_DIR} on Port 7000...")
# Assuming poetry run uvicorn or similar.
COMMAND = ["poetry", "run", "uvicorn", "server.main:app", "--host", "0.0.0.0", "--port", "7000"]

try:
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("[Bridge] Mem0 stopped.")
except Exception as e:
    print(f"[Bridge] Mem0 crashed: {e}")
