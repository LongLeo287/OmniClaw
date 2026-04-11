import os
import sys
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(current_dir, "..", "..", "..", "OmniClaw REMOTE", "plugins", "openclaw")

if not os.path.exists(TARGET_DIR):
    print(f"Error: OpenClaw target directory not found: {TARGET_DIR}")
    sys.exit(1)

os.environ["OPENCLAW_HOME"] = TARGET_DIR
os.chdir(TARGET_DIR)

print(f"[Bridge] Launching OpenClaw Gateway from {TARGET_DIR} on Port 18789...")
# COMMAND: pnpm openclaw gateway --port 18789 --verbose --allow-unconfigured
COMMAND = ["pnpm", "openclaw", "gateway", "--port", "18789", "--verbose", "--allow-unconfigured"]

try:
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("[Bridge] OpenClaw killed via KeyboardInterrupt.")
except Exception as e:
    print(f"[Bridge] OpenClaw crashed: {e}")
