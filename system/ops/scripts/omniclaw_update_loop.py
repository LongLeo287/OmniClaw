import time
import os
import sys

# Đảm bảo import được daemon
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

import omniclaw_update_daemon

# Chu kỳ lặp: 12 tiếng / 1 lần (Tránh bị Github Block IP vì gọi API quá nhiều)
POLL_INTERVAL_SECONDS = 12 * 60 * 60

def run_loop():
    print(f"============================================================")
    print(f"  OMNICLAW TRACKER DAEMON (Chạy ngầm mỗi 12 giờ)            ")
    print(f"============================================================")
    print(f"[*] Tiến trình bắt đầu tại: {time.ctime()}")

    while True:
        try:
            print("\n" + "="*50)
            print(f"[*] Đang thực thi Kế hoạch Update lúc: {time.ctime()}")
            omniclaw_update_daemon.main()
            print(f"[*] Hoàn tất. Tiến trình sẽ ngủ đông trong 12 tiếng...")
        except Exception as e:
            print(f"[!] Lỗi nghiêm trọng lúc chạy: {e}")
            print(f"[*] Sẽ thử lại sau 12 tiếng...")
            
        time.sleep(POLL_INTERVAL_SECONDS)

if __name__ == "__main__":
    run_loop()
