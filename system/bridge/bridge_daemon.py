"""
OMNICLAW HQ - BRIDGE DAEMON (SUPERVISOR)
Tự động duy trì và phục hồi Bến Cảng (Port 8000) 24/7.
Không phụ thuộc vào file .bat thô sơ.
Tránh tình trạng Remote "Đất Cáp Lõi" do uvicorn sập ngầm.
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
RESTART_DELAY = 5  # Đợi 5s trước khi nổ máy lại để tránh loop

def start_guard():
    logging.info("🛡️ KÍCH HOẠT HỆ THỐNG PHÒNG THỦ CẢNG OMNICLAW (DAEMON MODE)")
    crash_count = 0
    
    while True:
        try:
            logging.info(f"▶️ Đang cấp điện cho Cầu Dao Tổng (Port {PORT})...")
            # Chạy uvicorn trực tiếp thông qua subprocess
            process = subprocess.Popen(
                [sys.executable, "-m", "uvicorn", TARGET_MODULE, "--host", "0.0.0.0", "--port", PORT],
                stdout=sys.stdout,
                stderr=subprocess.STDOUT,
                env=os.environ.copy()
            )
            
            # Đợi process kết thúc (Nếu sập, code sẽ đi tiếp qua đây)
            process.wait()
            
            # Nếu code chạy đến đây tức là Uvicorn đã chết
            crash_count += 1
            logging.error(f"❌ MẤT ĐIỆN! Cảng OmniClaw vừa sập (Lần {crash_count}). Exit Code: {process.returncode}")
            
        except Exception as e:
            logging.error(f"☠️ LỖI CHÍ TỬ TRONG DAEMON: {e}")
            crash_count += 1
            
        logging.warning(f"⏳ Tự động hồi sinh Cảng sau {RESTART_DELAY} giây...")
        time.sleep(RESTART_DELAY)

if __name__ == "__main__":
    os.chdir(str(_ROOT))
    start_guard()
