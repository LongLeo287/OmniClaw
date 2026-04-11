import os
import sys
import subprocess
import shutil
from pathlib import Path

# Hardcoded Port Assignment (Enforced by backend repo compatibility)
PORT = "20128"

current_dir = Path(__file__).resolve().parent
REPO_ROOT = Path(os.getenv("OMNICLAW_ROOT", current_dir.parents[1])).resolve()
REMOTE_ROOT = Path(os.getenv("OMNICLAW_REMOTE_ROOT", REPO_ROOT.parent / "OmniClaw REMOTE")).resolve()
TARGET_DIR = (REMOTE_ROOT / "plugins" / "9router").resolve()
LOCAL_BINARY = TARGET_DIR / "node_modules" / ".bin" / ("9router.cmd" if os.name == "nt" else "9router")

def is_global_installed():
    return shutil.which("9router") is not None

def repair_install():
    """Explicit repair path for provisioning 9Router dependencies."""
    os.makedirs(TARGET_DIR, exist_ok=True)
    print("[OmniClaw Bridge] Repair mode: installing 9Router locally into bridge workspace...")
    subprocess.run(["npm", "install", "9router"], cwd=TARGET_DIR, check=True)
    print("[OmniClaw Bridge] Repair mode completed successfully.")


def resolve_launch_command():
    if is_global_installed():
        return ["9router"]
    if LOCAL_BINARY.exists():
        return [str(LOCAL_BINARY)]
    return None

def launch():
    print(f"[OmniClaw Bridge] Igniting 9Router Gateway on Port {PORT}...")

    if "--repair" in sys.argv or os.getenv("OMNICLAW_BRIDGE_REPAIR") == "1":
        repair_install()

    command = resolve_launch_command()
    if command is None:
        print("[OmniClaw Bridge] ERR: 9Router is not installed.")
        print("[OmniClaw Bridge] Action required: run this bridge with --repair or provision 9router during bootstrap.")
        sys.exit(1)

    # Inject routing base URL logic per bridge specs
    os.environ["PORT"] = str(PORT)
    os.environ["NEXT_PUBLIC_BASE_URL"] = f"http://localhost:{PORT}"
    
    # Switch execution path to plugin dir
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    try:
        subprocess.run(command, cwd=TARGET_DIR, check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] 9Router terminated safely.")
    except FileNotFoundError as e:
        print(f"[OmniClaw Bridge] Missing runtime dependency for 9Router launch: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"[OmniClaw Bridge] 9Router crashed catastrophically: {e}")
        sys.exit(1)

if __name__ == "__main__":
    launch()
