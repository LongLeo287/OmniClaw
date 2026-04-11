import os
import sys
import subprocess

# Hardcoded Port Assignment (Enforced by backend repo compatibility)
PORT = "18789"

current_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(current_dir, "..", "..", "..", "OmniClaw REMOTE", "plugins", "openclaw")

if not os.path.exists(TARGET_DIR):
    print(f"[OmniClaw Bridge] ERR: OpenClaw target directory not found: {TARGET_DIR}")
    sys.exit(1)

os.environ["OPENCLAW_HOME"] = TARGET_DIR
os.chdir(TARGET_DIR)

if not os.path.exists(os.path.join(TARGET_DIR, "node_modules")):
    print("[OmniClaw Bridge] Auto-Healing: Missing node_modules. Initiating Plug&Play setup -> pnpm install...")
    try:
        subprocess.run(["pnpm", "install"], check=True)
    except Exception as e:
        print(f"[OmniClaw Bridge] Plug&Play Setup Failed: {e}")

print(f"[OmniClaw Bridge] Launching OpenClaw Gateway from {TARGET_DIR} on Port {PORT}...")
COMMAND = ["pnpm", "openclaw", "gateway", "--port", str(PORT), "--verbose", "--allow-unconfigured"]

try:
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("\n[OmniClaw Bridge] OpenClaw killed via KeyboardInterrupt.")
except Exception as e:
    print(f"[OmniClaw Bridge] OpenClaw crashed: {e}")
