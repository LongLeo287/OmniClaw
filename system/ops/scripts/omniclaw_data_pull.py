import os
import sys
import datetime
import subprocess
import concurrent.futures
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import HfApi, login, snapshot_download

# Configuration
AI_OS_ROOT = Path(__file__).resolve().parent.parent.parent.parent
SECRETS_FILE = AI_OS_ROOT / "system" / "ops" / "secrets" / "MASTER.env"
DATASET_REPO = "LongLeo/OmniClaw-Data-Vault"

# =========================================================================
# DATA VAULT TARGETS: LỢI HẠI NHẤT
# Chỉ Tải/Extract các folder Cốt lõi của Hệ Sinh Thái. (Tránh rác mạng lạc lỏng)
# =========================================================================
TARGET_VAULTS = [
    "brain/memory",
    "storage/vault",
    "ecosystem/plugins"
]

def load_environment():
    if SECRETS_FILE.exists():
        load_dotenv(SECRETS_FILE)
    
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        print("[ERROR] HF_TOKEN missing from MASTER.env or environment.")
        exit(1)
    return hf_token

def pull_from_huggingface(hf_token):
    print("\n🔑 Authenticating with Hugging Face...")
    login(token=hf_token)
    api = HfApi()
    
    print(f"🔍 Validating HF repository: {DATASET_REPO}")
    try:
        api.dataset_info(DATASET_REPO)
        print("✅ HF Repository exists. Sẵn sàng Khôi Phục (Restore)...")
    except Exception as e:
        print(f"❌ KHO DATASET TRỐNG RỖNG HOẶC KHÔNG THỂ TRUY CẬP: {e}")
        return False

    print("🚀 Khởi chạy Delta-Download từ Hugging Face (Trạm 1)...")
    success = True
    
    # Chỉ hút đúng 3 Lõi mục tiêu
    # HF snapshot_download hỗ trợ filter allow_patterns trực tiếp!
    allow_list = [f"{vault}/**" for vault in TARGET_VAULTS]
    
    try:
        print(f"   [HF] Đang hút năng lượng lõi về Local: {TARGET_VAULTS} ...")
        # Snapshot Download: Tự động so sánh phiên bản, chỉ tải cục delta còn thiếu
        downloaded_path = snapshot_download(
            repo_id=DATASET_REPO,
            repo_type="dataset",
            allow_patterns=allow_list,
            local_dir=str(AI_OS_ROOT),
            local_dir_use_symlinks=False, # Yêu cầu file thật (không link tắt) để Agent còn truy cập
            ignore_patterns=["*gitkeep*"]
        )
        print(f"\n✅ HF DOWNLOAD HOÀN TẤT: Não bộ đã được ghép thành công vào Gốc.")
    except Exception as e:
        print(f"      ❌ Lỗi Cản Trở Quá Trình Download Lõi (HF): {e}")
        success = False

    return success

def pull_from_googledrive():
    rclone_exe = AI_OS_ROOT / "system/ops/tools/rclone/rclone.exe"
    if not rclone_exe.exists():
        print("\n⚠️ SYSTEM: Chưa phát hiện Rclone (Google Drive Engine). Tạm lược bỏ kéo luồng GDrive.")
        return False

    # Check if gdrive is configured
    try:
        remotes = subprocess.check_output([str(rclone_exe), "listremotes"], text=True)
        if "gdrive:" not in remotes:
            print("\n❌ LỖI RCLONE: Chưa xác thực Google Drive! Hệ thống không thể hút Data.")
            return False
    except Exception as e:
        return False

    print("\n🚀 Khởi chạy RClone Download từ Google Drive (Trạm 2)...")
    success = True
    for folder in TARGET_VAULTS:
        dest_path = AI_OS_ROOT / folder
        # Ensure base path exists for destination to avoid rclone panic
        dest_path.mkdir(parents=True, exist_ok=True)
        print(f"   [GDrive] Đang hút cấu trúc mây: {folder} ...")
        try:
             # Rclone COPY: Chỉ nhặt rương đắp vô máy tính, TUYỆT ĐỐI không xóa nhầm Data local mới tạo.
             subprocess.run([
                 str(rclone_exe), "copy", f"gdrive:OmniClaw-Data-Vault/{folder}", str(dest_path),
                 "--fast-list", "--transfers", "16", "--checkers", "16",
                 "--stats", "30s"
             ], check=True)
        except subprocess.CalledProcessError as e:
             print(f"      ❌ GDrive lỗi khi Bơm Lõi (Pull) {folder}: {e}")
             success = False

    if success:
        print("\n✅ GDRIVE BƠM HOÀN TẤT. Hệ sinh thái đã hút đầy đủ Rương Vàng.")
    return success
        
def main():
    print("=====================================================")
    print(" OmniClaw Data Vault - TARGETED PULL PIPELINE (DATA RESTORE)")
    print("=====================================================")
    hf_token = load_environment()
    
    print("⚡ BẮT ĐẦU VẬN HÀNH QUY TRÌNH HÚT DATA TỪ LÕI CLOUD ⚡\n")
    print("⚠️ THẬN TRỌNG: Quá trình này sẽ tốn nhiều Băng Thông do tải hàng Gigabytes Dữ Liệu.")
    
    pull_target = input("\n[?] Sếp muốn tải Lõi từ Trạm Mây nào? (1: Hugging Face, 2: Google Drive, 3: Song Song cả 2): ").strip()
    
    hf_success = False
    gd_success = False
    
    if pull_target == '1' or pull_target == '3':
        hf_success = pull_from_huggingface(hf_token)
    
    if pull_target == '2' or pull_target == '3':
        gd_success = pull_from_googledrive()
        
    # [NEW] Restore Symlink Junctions automatically after Cloud Pull
    if hf_success or gd_success:
        print("\n🔄 Đang Móc Nối Lại Mạng Lưới Rễ Data (Junction Symlinks)...")
        restore_script = AI_OS_ROOT / "system" / "ops" / "scripts" / "restore_links.py"
        if restore_script.exists():
            subprocess.run(["python", str(restore_script)])
            print("✅ Liên kết đã hoàn thiện. Data sắn sàng phục vụ hệ sinh thái.")
    
    print("\n=====================================================")
    print("🎉 TRẠNG THÁI TỔNG KẾT DATA RESTORE:")
    if pull_target in ['1', '3']:
        print(f"   - Trạm Hugging Face: {'[SUCCESS]' if hf_success else '[FAILED]'}")
    if pull_target in ['2', '3']:
        print(f"   - Trạm Google Drive: {'[SUCCESS]' if gd_success else '[FAILED]'}")
    print("=====================================================")
        
if __name__ == "__main__":
    main()
