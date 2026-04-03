import os
import sys
import subprocess

def launch():
    # Route execution to OmniClaw REMOTE
    remote_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/plugins/LightRAG/lightrag/api/lightrag_server.py"))
    
    if not os.path.exists(remote_path):
        print(f"[BRIDGE DIAGNOSTIC] ERROR: Remote target not found at {remote_path}")
        sys.exit(1)
        
    print(f"[BRIDGE ACTIVATE] Routing connection to REMOTE: {remote_path}")
    subprocess.Popen([sys.executable, remote_path], cwd=os.path.dirname(remote_path))

if __name__ == "__main__":
    launch()
