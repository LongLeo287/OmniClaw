import os
import sys
import subprocess
from pathlib import Path

# Port Assignment from OBD Harbor (Default to config port)
PORT = sys.argv[1] if len(sys.argv) > 1 else "3002"

CURRENT_DIR = Path(__file__).resolve().parent
OMNICLAW_ROOT = Path(os.getenv("OMNICLAW_ROOT", CURRENT_DIR.parents[1])).resolve()
COMPOSE_FILE = CURRENT_DIR / "docker-compose.yml"

def launch():
    print(f"[OmniClaw Bridge] Activating Firecrawl Web Scraper (Docker) on Port {PORT}...")
    
    if not COMPOSE_FILE.exists():
        print(f"[OmniClaw Bridge] ERR: Topology not found at {COMPOSE_FILE}")
        sys.exit(1)

    # Start the service
    cmd_up = ["docker", "compose", "-f", str(COMPOSE_FILE), "up", "firecrawl-api"]
    
    try:
        # Run Docker Compose (blocking, so OBD Harbor can monitor it)
        print(f"[OmniClaw Bridge] Harbor Lock Engaged. Press Ctrl+C to terminate container.")
        subprocess.run(cmd_up, cwd=OMNICLAW_ROOT, check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Signal caught. Terminating Firecrawl Container...")
    except Exception as e:
        print(f"[OmniClaw Bridge] Firecrawl crashed: {e}")
        sys.exit(1)

if __name__ == "__main__":
    launch()
