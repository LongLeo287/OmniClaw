import os
import sys
import subprocess

def launch():
    remote_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/agentic_zone/nullclaw/zig-out/bin/nullclaw.exe"))
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/agentic_zone/nullclaw/configs/aios-corp.json"))
    
    if not os.path.exists(config_path):
        # Fallback if structure changes
        remote_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../REMOTE/claws/nullclaw/zig-out/bin/nullclaw.exe"))
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../REMOTE/claws/nullclaw/configs/aios-corp.json"))
        
    print(f"[BRIDGE ACTIVATE] Routing connection to REMOTE: {remote_path}")
    subprocess.Popen([remote_path, "--config", config_path], cwd=os.path.dirname(remote_path))

if __name__ == "__main__":
    launch()
