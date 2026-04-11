import os
import sys
import subprocess
from pathlib import Path

current_dir = Path(__file__).resolve().parent
OMNICLAW_ROOT = Path(os.getenv("OMNICLAW_ROOT", current_dir.parents[1])).resolve()


def resolve_script_path():
    explicit_script = os.getenv("OMNICLAW_SYSTEM_PULSE_SCRIPT")
    if explicit_script:
        return Path(explicit_script).resolve()

    candidates = [
        (OMNICLAW_ROOT / "ecosystem" / "workflows" / "daemons" / "system_pulse.py").resolve(),
        (OMNICLAW_ROOT / "workflows" / "daemons" / "system_pulse.py").resolve(),
        (current_dir / ".." / "workflows" / "daemons" / "system_pulse.py").resolve(),
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]

def launch():
    print("[OmniClaw Bridge] Igniting System Pulse (Telegram Daemon)...")
    script_path = resolve_script_path()
    
    if not script_path.exists():
        print(f"[OmniClaw Bridge] Error: Daemon not found at {script_path}")
        print("[OmniClaw Bridge] Action required: set OMNICLAW_SYSTEM_PULSE_SCRIPT or provision the daemon in a supported workspace.")
        sys.exit(1)

    try:
        subprocess.run([sys.executable, str(script_path), "--loop"], check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Terminated safely.")
    except subprocess.CalledProcessError as e:
        print(f"[OmniClaw Bridge] System Pulse exited with failure: {e}")
        sys.exit(e.returncode or 1)

if __name__ == "__main__":
    launch()
