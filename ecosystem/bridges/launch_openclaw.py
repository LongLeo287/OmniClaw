import os
import sys
import subprocess
from pathlib import Path

# Hardcoded Port Assignment (Enforced by backend repo compatibility)
PORT = "18789"

current_dir = Path(__file__).resolve().parent
REPO_ROOT = Path(os.getenv("OMNICLAW_ROOT", current_dir.parents[1])).resolve()
REMOTE_ROOT = Path(os.getenv("OMNICLAW_REMOTE_ROOT", REPO_ROOT.parent / "OmniClaw REMOTE")).resolve()
TARGET_DIR = (REMOTE_ROOT / "plugins" / "openclaw").resolve()
NODE_MODULES_DIR = TARGET_DIR / "node_modules"

if not TARGET_DIR.exists():
    print(f"[OmniClaw Bridge] ERR: OpenClaw target directory not found: {TARGET_DIR}")
    sys.exit(1)

os.environ["OPENCLAW_HOME"] = str(TARGET_DIR)

def repair_install():
    print("[OmniClaw Bridge] Repair mode: provisioning OpenClaw dependencies with pnpm install...")
    subprocess.run(["pnpm", "install"], cwd=TARGET_DIR, check=True)
    print("[OmniClaw Bridge] Repair mode completed successfully.")

print(f"[OmniClaw Bridge] Launching OpenClaw Gateway from {TARGET_DIR} on Port {PORT}...")
COMMAND = ["pnpm", "openclaw", "gateway", "--port", str(PORT), "--verbose", "--allow-unconfigured"]

if "--repair" in sys.argv or os.getenv("OMNICLAW_BRIDGE_REPAIR") == "1":
    repair_install()

if not NODE_MODULES_DIR.exists():
    print("[OmniClaw Bridge] ERR: OpenClaw dependencies are missing.")
    print("[OmniClaw Bridge] Action required: provision the workspace first or rerun this bridge with --repair.")
    sys.exit(1)

try:
    subprocess.run(COMMAND, cwd=TARGET_DIR, check=True)
except KeyboardInterrupt:
    print("\n[OmniClaw Bridge] OpenClaw killed via KeyboardInterrupt.")
except FileNotFoundError as e:
    print(f"[OmniClaw Bridge] Missing runtime dependency for OpenClaw launch: {e}")
    sys.exit(1)
except Exception as e:
    print(f"[OmniClaw Bridge] OpenClaw crashed: {e}")
    sys.exit(1)
