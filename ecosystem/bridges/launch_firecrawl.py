import os
import sys
import subprocess

current_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(current_dir, "..", "..", "..", "OmniClaw REMOTE", "plugins", "firecrawl")

if not os.path.exists(TARGET_DIR):
    print(f"Error: FireCrawl target directory not found: {TARGET_DIR}")
    sys.exit(1)

os.chdir(TARGET_DIR)

print(f"[Bridge] Launching FireCrawl (Docker) from {TARGET_DIR} on Port 3002...")
# We use docker compose up
COMMAND = ["docker", "compose", "-f", "docker_compose.yaml", "up"]

try:
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("[Bridge] Stopping FireCrawl...")
    subprocess.run(["docker", "compose", "-f", "docker_compose.yaml", "down"])
except Exception as e:
    print(f"[Bridge] FireCrawl crashed: {e}")
