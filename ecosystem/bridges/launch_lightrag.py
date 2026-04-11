import os
import sys
import subprocess
from pathlib import Path

# Port Assignment from OBD Harbor
PORT = sys.argv[1] if len(sys.argv) > 1 else "9621"

CURRENT_DIR = Path(__file__).resolve().parent
OMNICLAW_ROOT = Path(os.getenv("OMNICLAW_ROOT", CURRENT_DIR.parents[1])).resolve()
COMPOSE_FILE = CURRENT_DIR / "docker-compose.yml"

def launch():
    print(f"[OmniClaw Bridge] Activating LightRAG Backend (Qdrant Docker) for Port {PORT}...")
    
    if not COMPOSE_FILE.exists():
        print(f"[OmniClaw Bridge] ERR: Topology not found at {COMPOSE_FILE}")
        sys.exit(1)

    cmd_up = ["docker", "compose", "-f", str(COMPOSE_FILE), "up", "qdrant"]

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
