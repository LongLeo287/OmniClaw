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
    remote_path = (REMOTE_ROOT / "agentic_zone" / "nullclaw" / "zig-out" / "bin" / "nullclaw.exe").resolve()
    config_path = (REMOTE_ROOT / "agentic_zone" / "nullclaw" / "configs" / "omniclaw_bridge.json").resolve()

    if not remote_path.exists():
        print(f"[OmniClaw Bridge] ERR: NullClaw binary not found at {remote_path}")
        print("[OmniClaw Bridge] Action required: provision the NullClaw binary before launching this bridge.")
        sys.exit(1)

    if not config_path.exists():
        if "--repair" in sys.argv or os.getenv("OMNICLAW_BRIDGE_REPAIR") == "1":
            print(f"[OmniClaw Bridge] Repair mode: generating default bridge config at {config_path}...")
            os.makedirs(config_path.parent, exist_ok=True)
            import json
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump({"agent": "nullclaw", "mode": "bridge", "allow_inbound": True}, f, indent=2)
        else:
            print(f"[OmniClaw Bridge] ERR: NullClaw bridge config not found at {config_path}")
            print("[OmniClaw Bridge] Action required: provision the config first or rerun this bridge with --repair.")
            sys.exit(1)

    print(f"[OmniClaw Bridge] Routing connection to REMOTE: {remote_path} (Assigned Port: {PORT})")
    try:
        subprocess.run([str(remote_path), "--config", str(config_path)], cwd=str(remote_path.parent), check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] NullClaw terminated safely.")
    except subprocess.CalledProcessError as e:
        print(f"[OmniClaw Bridge] NullClaw exited with failure: {e}")
        sys.exit(e.returncode or 1)

if __name__ == "__main__":
    launch()
