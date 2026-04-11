import os
import sys
import subprocess

# Port Assignment from OBD Harbor
PORT = sys.argv[1] if len(sys.argv) > 1 else "Unknown"

def launch():
    remote_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../OmniClaw REMOTE/plugins/open_notebook/run_api.py"))
    
    if not os.path.exists(remote_path):
        print(f"[OmniClaw Bridge] ERR: Remote target not found at {remote_path}")
        sys.exit(1)
        
    print(f"[OmniClaw Bridge] Activating Open Notebook Remote at {remote_path} (Assigned Port: {PORT})")
    subprocess.Popen([sys.executable, remote_path], cwd=os.path.dirname(remote_path))

if __name__ == "__main__":
    launch()
