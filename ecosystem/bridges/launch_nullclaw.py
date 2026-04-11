import os
import sys
import subprocess

# Port Assignment from OBD Harbor
PORT = sys.argv[1] if len(sys.argv) > 1 else "Unknown"

def launch():
    remote_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/agentic_zone/nullclaw/zig-out/bin/nullclaw.exe"))
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/agentic_zone/nullclaw/configs/omniclaw_bridge.json"))
    
    if not os.path.exists(config_path):
        print(f"[OmniClaw Bridge] P&P Fallback: Config missing at {config_path}. Auto-generating default payload...")
        os.makedirs(os.path.dirname(config_path), exist_ok=True)
        import json
        with open(config_path, "w") as f:
            json.dump({"agent": "nullclaw", "mode": "bridge", "allow_inbound": True}, f, indent=2)
            
    print(f"[OmniClaw Bridge] Routing connection to REMOTE: {remote_path} (Assigned Port: {PORT})")
    subprocess.Popen([remote_path, "--config", config_path], cwd=os.path.dirname(remote_path))

if __name__ == "__main__":
    launch()
