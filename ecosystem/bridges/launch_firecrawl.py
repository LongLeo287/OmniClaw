import os
import sys
import subprocess
import time

# Port Assignment from OBD Harbor (Default to config port)
PORT = sys.argv[1] if len(sys.argv) > 1 else "3002"

OMNICLAW_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def launch():
    print(f"[OmniClaw Bridge] Activating Firecrawl Web Scraper (Docker) on Port {PORT}...")
    
    # Ensuring backend redis is up first, then firecrawl
    compose_file = os.path.join(OMNICLAW_ROOT, "docker-compose.yml")
    
    if not os.path.exists(compose_file):
        print(f"[OmniClaw Bridge] ERR: Topology not found at {compose_file}")
        sys.exit(1)

    # Start the service
    cmd_up = ["docker", "compose", "-f", compose_file, "up", "firecrawl-api"]
    
    try:
        # Run Docker Compose (blocking, so OBD Harbor can monitor it)
        print(f"[OmniClaw Bridge] Harbor Lock Engaged. Press Ctrl+C to terminate container.")
        subprocess.run(cmd_up, cwd=OMNICLAW_ROOT, check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Signal caught. Terminating Firecrawl Container...")
    except Exception as e:
        print(f"[OmniClaw Bridge] Firecrawl crashed: {e}")
    finally:
        # Cleanup when bridge is killed
        print("[OmniClaw Bridge] Shutting down instance...")
        subprocess.run(["docker", "compose", "-f", compose_file, "stop", "firecrawl-api"], cwd=OMNICLAW_ROOT)

if __name__ == "__main__":
    launch()
