import os
import sys
import subprocess
from pathlib import Path

# Port Assignment from OBD Harbor
PORT = sys.argv[1] if len(sys.argv) > 1 else "Unknown"

current_dir = Path(__file__).resolve().parent
REPO_ROOT = Path(os.getenv("OMNICLAW_ROOT", current_dir.parents[1])).resolve()
REMOTE_ROOT = Path(os.getenv("OMNICLAW_REMOTE_ROOT", REPO_ROOT.parent / "OmniClaw REMOTE")).resolve()

def launch():
    remote_path = (REMOTE_ROOT / "plugins" / "open_notebook" / "run_api.py").resolve()
    
    if not remote_path.exists():
        print(f"[OmniClaw Bridge] ERR: Remote target not found at {remote_path}")
        sys.exit(1)
        
    print(f"[OmniClaw Bridge] Activating Open Notebook Remote at {remote_path} (Assigned Port: {PORT})")
    try:
        subprocess.run([sys.executable, str(remote_path)], cwd=str(remote_path.parent), check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Open Notebook terminated safely.")
    except subprocess.CalledProcessError as e:
        print(f"[OmniClaw Bridge] Open Notebook exited with failure: {e}")
        sys.exit(e.returncode or 1)

if __name__ == "__main__":
    launch()
