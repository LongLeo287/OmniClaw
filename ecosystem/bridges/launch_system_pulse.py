import os
import sys
import time
import socket
import subprocess
import signal

# Hardcoded Port Assignment (Mock Port for OBD detection)
PORT = "9999"

current_dir = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(current_dir, "..", "workflows", "daemons", "system_pulse.py")

def launch():
    print(f"[OmniClaw Bridge] Igniting System Pulse (Telegram Daemon) on Port {PORT}...")
    
    if not os.path.exists(SCRIPT_PATH):
        print(f"[OmniClaw Bridge] Error: Daemon not found at {SCRIPT_PATH}")
        sys.exit(1)
        
    print(f"[OmniClaw Bridge] Spawning background worker: {SCRIPT_PATH} --loop")
    proc = subprocess.Popen(
        [sys.executable, SCRIPT_PATH, "--loop"],
        stdout=sys.stdout,
        stderr=sys.stderr
    )

    print(f"[OmniClaw Bridge] Emulating Active State (Mocking Port {PORT})...")
    
    try:
        # Open a dummy socket to satisfy the OBD Harbor heartbeat ping
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            s.bind(('127.0.0.1', int(PORT)))
            s.listen()
            while True:
                # If pulse worker dies, we should terminate the bridge
                if proc.poll() is not None:
                    print("\n[OmniClaw Bridge] Underlying Daemon crashed. Terminating bridge...")
                    break
                    
                s.settimeout(1.0)
                try:
                    conn, addr = s.accept()
                    conn.close()
                except socket.timeout:
                    pass
    except OSError as e:
        print(f"[OmniClaw Bridge] P&P Error: Port {PORT} might already be in use. Details: {e}")
    except KeyboardInterrupt:
        print("\n[OmniClaw Bridge] Terminated safely.")
    finally:
        if proc.poll() is None:
            proc.terminate()
            try:
                proc.wait(timeout=2)
            except subprocess.TimeoutExpired:
                proc.kill()

if __name__ == "__main__":
    launch()
