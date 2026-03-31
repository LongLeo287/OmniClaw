import os
import sys
import subprocess
from pathlib import Path

# Cấu hình Đường dẫn chuẩn
AI_OS_ROOT = Path(__file__).resolve().parent.parent.parent.parent

def run_command(cmd, cwd=None, capture=False):
    """Tiện ích chạy subprocess có bắt lỗi"""
    try:
        if capture:
             return subprocess.check_output(cmd, cwd=cwd, text=True, stderr=subprocess.STDOUT)
        else:
             subprocess.run(cmd, cwd=cwd, check=True)
             return True
    except subprocess.CalledProcessError as e:
        print(f"❌ [LỖI LỆNH] {' '.join(cmd)}")
        if capture:
            print(f"Chi tiết: {e.output}")
        return False

def step_1_data_push():
    print("\n=========================================================")
    print(" [BƯỚC 1/3]: TẢI DỮ LIỆU NẶNG (DATA VAULT) LÊN HF & GDRIVE")
    print("=========================================================")
    script_path = AI_OS_ROOT / "system" / "ops" / "scripts" / "omniclaw_data_push.py"
    if script_path.exists():
        subprocess.run([sys.executable, str(script_path)], cwd=AI_OS_ROOT)
    else:
        print("⚠️ Không tìm thấy omniclaw_data_push.py! Bỏ qua bước đẩy Data Vault.")

def step_2_backup_soul():
    print("\n=========================================================")
    print(" [BƯỚC 2/3]: SAO LƯU TÂM TRÍ VÀ TRẠNG THÁI (BACKUP SOUL)")
    print("=========================================================")
    script_path = AI_OS_ROOT / "system" / "ops" / "scripts" / "memory" / "backup_soul.ps1"
    if script_path.exists():
        run_command(["powershell", "-ExecutionPolicy", "Bypass", "-File", str(script_path)], cwd=AI_OS_ROOT)
    else:
        print("⚠️ Không tìm thấy backup_soul.ps1. Bỏ qua bước này.")

def step_3_git_push():
    print("\n=========================================================")
    print(" [BƯỚC 3/3]: ĐÓNG GÓI VÀ ĐẨY LÊN GITHUB (GIT PUSH PIPELINE)")
    print("=========================================================")
    
    # [Bảo Mật] Làm sạch LFS (Xóa cache Git cho những thư mục Nặng nhỡ bị bắt dính)
    print("🧹 Thanh tẩy Cache để tránh lỗi 100MB của GitHub...")
    run_command(["git", "rm", "-r", "--cached", "storage/vault/ARCHIVE/knowledge_files/"], cwd=AI_OS_ROOT, capture=True)
    run_command(["git", "rm", "-r", "--cached", "brain/memory/"], cwd=AI_OS_ROOT, capture=True)
    
    # 2. Stage tất cả tệp an toàn (Theo luật của .gitignore)
    print("📦 Đang thu gom mã nguồn...")
    if not run_command(["git", "add", "."], cwd=AI_OS_ROOT):
        print("❌ Thu gom thất bại.")
        return

    # Check xem có gì thay đổi không
    status = run_command(["git", "status", "--porcelain"], cwd=AI_OS_ROOT, capture=True)
    if status is False or not str(status).strip():
        print("✅ Không có thay đổi Code nào mới để Commit lên Github. Hệ thống đã đạt chuẩn mới nhất.")
        print("🚀 Bắt đầu Push Lên Github (Push thủ công cho nhưng Lịch sử đợi)...")
        run_command(["git", "push"], cwd=AI_OS_ROOT)
        return

    # Lấy thông điệp Commit từ người dùng
    print("\n" + "-"*40)
    commit_msg = input("[?] Nhập nội dung cập nhật (Commit message): ").strip()
    if not commit_msg:
        commit_msg = "chore: Tự động Đóng Gói và Đồng Bộ OmniClaw Pipeline"
        print(f"👉 Dùng mặc định: '{commit_msg}'")
    
    # Commit
    if not run_command(["git", "commit", "-m", commit_msg], cwd=AI_OS_ROOT):
         return
         
    # Push
    print("\n🚀 Bắt đầu Push Lên Github (Nhánh Hiện Tại)...")
    if run_command(["git", "push"], cwd=AI_OS_ROOT):
         print("✅ THÀNH CÔNG: Github CI/CD Actions sẽ bắt đầu phân tích mã nguồn ngay lúc này!")

def main():
    print("""
    █████████   ██████    ██████ █████ ███    ███  ██████  
   ███░░░░░███ ███░░███  ███░░███░░███░░███  ███  ███░░███ 
  ███     ░░░ ░███ ░███ ░███ ░███ ░███ ░░██████  ░███ ░░░  
 ░███         ░███ ░███ ░███ ░███ ░███  ░░████   ░███      
 ░███    █████░███ ░███ ░███ ░███ ░███   ░███    ░███      
 ░░███  ░░███ ░███ ░███ ░███ ░███ ░███   ░███    ░░███ ███ 
  ░░█████████ ░░██████  ░░█████████████  █████    ░░█████  
   ░░░░░░░░░   ░░░░░░    ░░░░░░░░░░░░░  ░░░░░      ░░░░░   
     ================ OMNICLAW PIPELINE ================
       Quy trình Đóng Gói Liên Hợp (Data Vault & GitHub)
    """)
    
    try:
        step_1_data_push()
        step_2_backup_soul()
        step_3_git_push()
        
        print("\n🎉 HOÀN TẤT TẤT CẢ QUY TRÌNH! Hệ thống OmniClaw đã an vị trên cả 3 Đám Mây.")
        print("Sếp có thể thảnh thơi kiểm tra GitHub Actions tiến hành Testing!")
    except KeyboardInterrupt:
        print("\n⚠️ HỦY BỎ BỞI NGƯỜI DÙNG.")

if __name__ == "__main__":
    main()
