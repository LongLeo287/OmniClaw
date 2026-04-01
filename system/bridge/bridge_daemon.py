"""
OMNICLAW HQ - BRIDGE DAEMON (SUPERVISOR)
Automatically maintains and recovers Harbor (Port 8000) 24/7.
Does not depend on basic .bat files.
Avoids Core Disconnect situations due to silent uvicorn crashes.
"""

import sys
import os
import time
import subprocess
import logging
from pathlib import Path

# Root detection: system/bridge/ -> 2 levels up
_ROOT = Path(os.environ.get("OMNICLAW_ROOT",
             str(Path(__file__).resolve().parents[2])))
_LOG_PATH = _ROOT / "system" / "ops" / "telemetry" / "logs" / "bridge_daemon.log"
_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - [BRIDGE_DAEMON] - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(str(_LOG_PATH), encoding="utf-8"),
    ]
)

TARGET_MODULE = "system.bridge.main:app"
PORT = "8000"
RESTART_DELAY = 5  # Wait 5s before restarting to avoid loops

def start_guard():
    logging.info("🛡️ ACTIVATING OMNICLAW HARBOR DEFENSE SYSTEM (DAEMON MODE)")
    crash_count = 0
    
    while True:
        try:
            logging.info(f"▶️ Powering up Main Breaker (Port {PORT})...")
            # Run uvicorn directly via subprocess
            process = subprocess.Popen(
                [sys.executable, "-m", "uvicorn", TARGET_MODULE, "--host", "0.0.0.0", "--port", PORT],
                stdout=sys.stdout,
                stderr=subprocess.STDOUT,
                env=os.environ.copy()
            )
            
            # Wait for process to end (If it crashes, code continues here)
            process.wait()
            
            # If code reaches here, Uvicorn has died
            crash_count += 1
            logging.error(f"❌ BLACKOUT! OmniClaw Harbor just crashed (Count {crash_count}). Exit Code: {process.returncode}")
            
        except Exception as e:
            logging.error(f"☠️ FATAL ERROR IN DAEMON: {e}")
            crash_count += 1
            
        logging.warning(f"⏳ Auto-reviving Harbor in {RESTART_DELAY} seconds...")
        time.sleep(RESTART_DELAY)

if __name__ == "__main__":
    os.chdir(str(_ROOT))
    start_guard()