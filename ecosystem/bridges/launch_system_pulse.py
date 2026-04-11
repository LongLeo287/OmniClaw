import os
import sys
import subprocess
from pathlib import Path

current_dir = Path(__file__).resolve().parent
SCRIPT_PATH = (current_dir / ".." / "workflows" / "daemons" / "system_pulse.py").resolve()

def launch():
    print("[OmniClaw Bridge] Igniting System Pulse (Telegram Daemon)...")
    
    if not SCRIPT_PATH.exists():
        print(f"[OmniClaw Bridge] Error: Daemon not found at {SCRIPT_PATH}")
        sys.exit(1)

    try:
        subprocess.run([sys.executable, str(SCRIPT_PATH), "--loop"], check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Terminated safely.")
    except subprocess.CalledProcessError as e:
        print(f"[OmniClaw Bridge] System Pulse exited with failure: {e}")
        sys.exit(e.returncode or 1)

if __name__ == "__main__":
    launch()
