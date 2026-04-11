import os
import sys
import subprocess

# Port Assignment from OBD Harbor
PORT = sys.argv[1] if len(sys.argv) > 1 else "Unknown"

def launch():
    remote_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/agentic_zone/nullclaw/zig-out/bin/nullclaw.exe"))
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/agentic_zone/nullclaw/configs/omniclaw_bridge.json"))

    if not os.path.exists(remote_path):
        print(f"[OmniClaw Bridge] ERR: NullClaw binary not found at {remote_path}")
        print("[OmniClaw Bridge] Action required: provision the NullClaw binary before launching this bridge.")
        sys.exit(1)

    if not os.path.exists(config_path):
        if "--repair" in sys.argv or os.getenv("OMNICLAW_BRIDGE_REPAIR") == "1":
            print(f"[OmniClaw Bridge] Repair mode: generating default bridge config at {config_path}...")
            os.makedirs(os.path.dirname(config_path), exist_ok=True)
            import json
            with open(config_path, "w", encoding="utf-8") as f:
                json.dump({"agent": "nullclaw", "mode": "bridge", "allow_inbound": True}, f, indent=2)
        else:
            print(f"[OmniClaw Bridge] ERR: NullClaw bridge config not found at {config_path}")
            print("[OmniClaw Bridge] Action required: provision the config first or rerun this bridge with --repair.")
            sys.exit(1)

    print(f"[OmniClaw Bridge] Routing connection to REMOTE: {remote_path} (Assigned Port: {PORT})")
    try:
        subprocess.run([remote_path, "--config", config_path], cwd=os.path.dirname(remote_path), check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] NullClaw terminated safely.")
    except subprocess.CalledProcessError as e:
        print(f"[OmniClaw Bridge] NullClaw exited with failure: {e}")
        sys.exit(e.returncode or 1)

if __name__ == "__main__":
    launch()
