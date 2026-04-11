import os
import sys
import subprocess
from pathlib import Path

# Hardcoded Port Assignment (Enforced by backend repo compatibility)
PORT = "8501"

current_dir = Path(__file__).resolve().parent
REPO_ROOT = Path(os.getenv("OMNICLAW_ROOT", current_dir.parents[1])).resolve()
REMOTE_ROOT = Path(os.getenv("OMNICLAW_REMOTE_ROOT", REPO_ROOT.parent / "OmniClaw REMOTE")).resolve()
TARGET_DIR = (REMOTE_ROOT / "plugins" / "omniclaw_ui").resolve()


def detect_launch_command():
    """Return a concrete launch command when a real UI project exists."""
    if (TARGET_DIR / "package.json").exists():
        return ["npm", "run", "dev", "--", "--port", PORT]
    if (TARGET_DIR / "app.py").exists():
        return [sys.executable, "app.py"]
    if (TARGET_DIR / "main.py").exists():
        return [sys.executable, "main.py"]
    return None

def launch():
    print(f"[OmniClaw Bridge] Igniting OmniClaw UI Gateway on Port {PORT}...")

    if not TARGET_DIR.exists():
        print(f"[OmniClaw Bridge] ERR: UI workspace not found at {TARGET_DIR}")
        print("[OmniClaw Bridge] Action required: provision the omniclaw_ui project before launching this bridge.")
        sys.exit(1)

    command = detect_launch_command()
    if command is None:
        print(f"[OmniClaw Bridge] ERR: No supported UI entrypoint found in {TARGET_DIR}")
        print("[OmniClaw Bridge] Expected one of: package.json, app.py, or main.py")
        sys.exit(1)

    try:
        subprocess.run(command, cwd=TARGET_DIR, check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Terminated safely.")
    except FileNotFoundError as e:
        print(f"[OmniClaw Bridge] Missing runtime dependency for UI launch: {e}")
        sys.exit(1)
    except subprocess.CalledProcessError as e:
        print(f"[OmniClaw Bridge] UI process exited with failure: {e}")
        sys.exit(e.returncode or 1)

if __name__ == "__main__":
    launch()
