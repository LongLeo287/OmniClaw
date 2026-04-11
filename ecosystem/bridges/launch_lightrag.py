import os
import sys
import subprocess

# Port Assignment from OBD Harbor
PORT = sys.argv[1] if len(sys.argv) > 1 else "9621"

OMNICLAW_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def launch():
    print(f"[OmniClaw Bridge] Activating LightRAG Backend (Qdrant Docker) for Port {PORT}...")
    
    compose_file = os.path.join(OMNICLAW_ROOT, "docker-compose.yml")
    
    if not os.path.exists(compose_file):
        print(f"[OmniClaw Bridge] ERR: Topology not found at {compose_file}")
        sys.exit(1)
        
    cmd_up = ["docker", "compose", "-f", compose_file, "up", "qdrant"]

    try:
        print(f"[OmniClaw Bridge] LightRAG DB engaged. Press Ctrl+C to terminate container.")
        subprocess.run(cmd_up, cwd=OMNICLAW_ROOT, check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Signal caught. Terminating Qdrant Container...")
    except Exception as e:
        print(f"[OmniClaw Bridge] LightRAG crashed: {e}")
    finally:
        print("[OmniClaw Bridge] Shutting down instance...")
        subprocess.run(["docker", "compose", "-f", compose_file, "stop", "qdrant"], cwd=OMNICLAW_ROOT)

if __name__ == "__main__":
    launch()
