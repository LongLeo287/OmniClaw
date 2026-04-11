import os
import sys
import subprocess
import shutil

# Hardcoded Port Assignment (Enforced by backend repo compatibility)
PORT = "20128"

current_dir = os.path.dirname(os.path.abspath(__file__))
TARGET_DIR = os.path.join(current_dir, "..", "..", "..", "OmniClaw REMOTE", "plugins", "9router")

def is_global_installed():
    return shutil.which("9router") is not None

def ensure_installed():
    """Auto-heal by checking and installing 9Router globally or locally."""
    if is_global_installed():
        print("[OmniClaw Bridge] P&P Protocol: 9Router is already installed globally.")
    else:
        print("[OmniClaw Bridge] P&P Protocol: 9Router is missing! Auto-Healing active...")
        try:
            print("[OmniClaw Bridge] Attempting global installation (npm install -g 9router)...")
            subprocess.run(["npm", "install", "-g", "9router"], check=True)
            print("[OmniClaw Bridge] Global Auto-Healing successful.")
        except Exception:
            print("[OmniClaw Bridge] Global install failed (Permissions?). Attempting local install fallback...")
            os.makedirs(TARGET_DIR, exist_ok=True)
            try:
                subprocess.run(["npm", "install", "9router"], cwd=TARGET_DIR, check=True)
                print("[OmniClaw Bridge] Local Auto-Healing successful.")
            except Exception as e:
                print(f"[OmniClaw Bridge] ERR: All Auto-Healing attempts failed! Cannot run 9Router.\n{e}")
                sys.exit(1)

def launch():
    print(f"[OmniClaw Bridge] Igniting 9Router Gateway on Port {PORT}...")
    
    # Inject routing base URL logic per bridge specs
    os.environ["PORT"] = str(PORT)
    os.environ["NEXT_PUBLIC_BASE_URL"] = f"http://localhost:{PORT}"
    
    # Switch execution path to plugin dir
    if not os.path.exists(TARGET_DIR):
         os.makedirs(TARGET_DIR, exist_ok=True)
    os.chdir(TARGET_DIR)
    
    try:
        # PnP launch, either global or local fallback works with npx wrapper
        subprocess.run(["npx", "9router"], check=True)
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] 9Router terminated safely.")
    except Exception as e:
        print(f"[OmniClaw Bridge] 9Router crashed catastrophically: {e}")

if __name__ == "__main__":
    ensure_installed()
    launch()
