import os
import sys
import subprocess

# Hardcoded Port Assignment (Enforced by Docker compose config)
PORT = "3002"

current_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(current_dir, "..", "..", "..", "OmniClaw REMOTE", "plugins", "firecrawl")

if not os.path.exists(TARGET_DIR):
    print(f"[OmniClaw Bridge] ERR: FireCrawl target directory not found: {TARGET_DIR}")
    sys.exit(1)

os.chdir(TARGET_DIR)

# Forwarding PORT to docker-compose context
os.environ["PORT"] = PORT

print(f"[OmniClaw Bridge] Launching FireCrawl (Docker) from {TARGET_DIR} on Port {PORT}...")
COMMAND = ["docker", "compose", "-f", "docker_compose.yaml", "up"]

try:
    subprocess.run(COMMAND, check=True)
except KeyboardInterrupt:
    print("\n[OmniClaw Bridge] Stopping FireCrawl...")
    subprocess.run(["docker", "compose", "-f", "docker_compose.yaml", "down"])
except Exception as e:
    print(f"[OmniClaw Bridge] FireCrawl crashed: {e}")
