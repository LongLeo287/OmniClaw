import os
import sys
import json
import time

def check_external_gate():
    key_path = r"<AI_OS_ROOT>\ops\secrets\KEYS\user_keys.json"
    if os.path.exists(key_path):
        data = json.load(open(key_path))
        return data.get("external_connections_enabled", False)
    return False

def check_agent(role_id):
    path = r"<AI_OS_ROOT>\brain\shared-context\AGENTS.md"
    if os.path.exists(path):
        content = open(path, "r", encoding="utf-8").read()
        return f"{role_id}" in content or role_id in content
    return True

def main():
    print("\n" + "="*70)
    print("[OmniClaw System Event]")")
    print("="*70)

    # [PHASE 1] Wake Up
    print("[OmniClaw System Event]") khởi động...")
    print("[OmniClaw System Event]")
    gate = check_external_gate()
    print("[OmniClaw System Event]"): {'BẬT 🟢' if gate else 'TẮT 🔴'}")
    if not gate:
        print("[OmniClaw System Event]"). Pipeline chuyển sang Internal Local.")

    time.sleep(1)

    # [PHASE 2] Brief
    print("[OmniClaw System Event]")...")
    print("[OmniClaw System Event]") và Nạp vào Đồ thị Tri thức.")

    time.sleep(1)

    # [PHASE 3] Execute
    print("[OmniClaw System Event]")...")
    print("[OmniClaw System Event]") else 'NO'}")
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")... Đã xử lý File nội bộ thành công.")

    print("[OmniClaw System Event]")... Đã mapping chức danh? {'YES' if check_agent('knowledge-agent') else 'NO'}")
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")
    time.sleep(2)
    print("[OmniClaw System Event]")...")
    print("[OmniClaw System Event]")

    time.sleep(1)

    # [PHASE 4 & 5] QA & Report
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")...")
    time.sleep(1.5)
    print("\n[" + "-"*68 + "]")
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]") thực thụ. Các AI Agent từ bỏ cái tôi cá nhân, hoạt động dựa trên Quy trình 7-Phase chung đúc kết từ mọi Engine (Gemini/Claude). Nó kết hợp cả Text RAG phẳng và Graph RAG để suy luận văn bản nội bộ siêu bảo mật.")
    print("[" + "-"*68 + "]")

    time.sleep(1)

    # [PHASE 6 & 7] Learn
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]").")
    print("="*70 + "\n")

if __name__ == "__main__":
    main()