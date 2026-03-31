import os
import sys
import datetime
import subprocess
import concurrent.futures
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import HfApi, login

# Configuration
AI_OS_ROOT = Path(__file__).resolve().parent.parent.parent.parent
SECRETS_FILE = AI_OS_ROOT / "system" / "ops" / "secrets" / "MASTER.env"
DATASET_REPO = "LongLeo/OmniClaw-Data-Vault"

# =========================================================================
# DATA VAULT TARGETS: LỢI HẠI NHẤT
# Chỉ push các thư mục này. Bỏ qua hoàn toàn quét root để tránh ma trận thư mục rác.
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

def push_delta_to_huggingface(hf_token):
    print("\n🔑 Authenticating with Hugging Face...")
    login(token=hf_token)
    api = HfApi()
    
    print(f"🔍 Validating HF repository: {DATASET_REPO}")
    try:
        api.dataset_info(DATASET_REPO)
        print("✅ HF Repository exists.")
    except Exception as e:
        print("⚠️ HF Repository not found or inaccessible. Creating a new private dataset repository...")
        try:
            api.create_repo(repo_id=DATASET_REPO, repo_type="dataset", private=True, exist_ok=True)
            print("✅ Created new repository on HF.")
        except Exception as ce:
            print(f"❌ KHÔNG THỂ TẠO DATASET MỚI! Sếp cần cài đặt Token có quyền 'Write' (Tạo Repo): {ce}")
            return False

    print("🚀 Khởi chạy Delta-Sync lên Hugging Face (Trạm 1)...")
    success = True
    for folder in TARGET_VAULTS:
        folder_path = AI_OS_ROOT / folder
        if folder_path.exists() and folder_path.is_dir():
            print(f"   [HF] Đang bắn tỉa thư mục: {folder} ...")
            try:
                # HF upload_folder native support path_in_repo mapping!
                api.upload_folder(
                    folder_path=str(folder_path),
                    repo_id=DATASET_REPO,
                    repo_type="dataset",
                    path_in_repo=folder, # Upload directly to the correct subpath in the cloud
                    commit_message=f"OmniClaw Vault Sync [{folder}]: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                )
            except Exception as e:
                print(f"      ❌ Lỗi khi tải {folder} lên HF: {e}")
                success = False
        else:
            print(f"   [HF] Bỏ qua {folder} (Không tồn tại hoặc bị xóa)")

    if success:
        print(f"\n✅ HF ĐỒNG BỘ HOÀN TẤT: Toàn bộ Lõi đã an tọa.")
    return success

def scrub_ghost_folders(rclone_exe):
    print("\n🧹 Bắt đầu rà soát và thanh trừng thư mục rác trên Google Drive...")
    try:
        # Lấy danh sách tất cả các files/folders Layer 0 trên Drive
        result = subprocess.check_output([str(rclone_exe), "lsf", "gdrive:OmniClaw-Data-Vault"], text=True)
        items = result.strip().split("\n")
        
        allowed_roots = [d.split('/')[0] + "/" for d in TARGET_VAULTS] # ví dụ 'brain/', 'storage/', 'ecosystem/'
        
        folders_deleted = 0
        for item in items:
            if not item: continue
            # Nếu là thư mục (cuối bằng /) và không thuộc nhóm cốt lõi
            if item.endswith("/") and item not in allowed_roots:
                junk_dir = f"gdrive:OmniClaw-Data-Vault/{item.strip('/')}"
                print(f"   🔥 Đang Tàn Sát thư mục rác: {junk_dir}")
                subprocess.run([str(rclone_exe), "purge", junk_dir], check=True)
                folders_deleted += 1
                
        if folders_deleted > 0:
            print(f"✅ Đã dọn sạch {folders_deleted} thư mục Lõi Rác trên GDrive!")
        else:
            print("✅ Ổ đĩa GDrive hiện tại đã thanh khiết. Không có thư mục lạ.")
            
    except subprocess.CalledProcessError as e:
         print(f"   ⚠️ Lỗi cản trở quá trình thanh trừng: {e}")

def push_delta_to_googledrive():
    rclone_exe = AI_OS_ROOT / "system/ops/tools/rclone/rclone.exe"
    if not rclone_exe.exists():
        print("\n⚠️ SYSTEM: Chưa phát hiện Rclone (Google Drive Engine). Bỏ qua bước đồng bộ phụ.")
        return False

    # Check if gdrive is configured
    try:
        remotes = subprocess.check_output([str(rclone_exe), "listremotes"], text=True)
        if "gdrive:" not in remotes:
            print("\n❌ LỖI RCLONE: Chưa xác thực Google Drive!")
            return False
    except Exception as e:
        return False

    # Dọn dẹp rác ma trước khi đẩy
    scrub_ghost_folders(rclone_exe)

    print("\n🚀 Khởi chạy Delta-Sync lên Google Drive (Trạm 2)...")
    success = True
    for folder in TARGET_VAULTS:
        folder_path = AI_OS_ROOT / folder
        if folder_path.exists() and folder_path.is_dir():
             print(f"   [GDrive] Đang bắn tỉa thư mục: {folder} ...")
             try:
                 # Rclone thẳng vào thư mục đích (Tắt hệ thống gạt lọc cồng kềnh toàn máy ảo)
                 subprocess.run([
                     str(rclone_exe), "sync", str(folder_path), f"gdrive:OmniClaw-Data-Vault/{folder}",
                     "--delete-excluded", # Xóa file rác NẾU CÓ bên trong chính thư mục đang sync
                     "--fast-list", "--transfers", "16", "--checkers", "16",
                     "--stats", "30s" # Giảm spam log
                 ], check=True)
             except subprocess.CalledProcessError as e:
                 print(f"      ❌ GDrive lỗi khi sync {folder}: {e}")
                 success = False
        else:
             print(f"   [GDrive] Bỏ qua {folder} (Không tìm thấy)")

    if success:
        print("\n✅ GDRIVE ĐỒNG BỘ HOÀN TẤT. Hệ thống chắp cánh tới Mây thành công.")
    return success
        
def main():
    print("=====================================================")
    print(" OmniClaw Data Vault - TARGETED VAULT PIPELINE")
    print("=====================================================")
    hf_token = load_environment()
    
    print("⚡ BẮT ĐẦU VẬN HÀNH QUY TRÌNH BẮN TỈA TÀI NGUYÊN ⚡\n")
    
    # We will run them sequentially in terminal script (easier UX tracking) 
    # instead of overlapping outputs since RClone Scrub takes terminal output
    hf_success = push_delta_to_huggingface(hf_token)
    gd_success = push_delta_to_googledrive()
    
    print("\n=====================================================")
    if hf_success or gd_success:
        print("🎉 TRẠNG THÁI CUỐI: HOÀN TẤT")
        if hf_success: print("   - [ON] Trạm Hugging Face An Toàn")
        if gd_success: print("   - [ON] Trạm Google Drive Thanh Khiết")
    else:
        print("⚠️ TRẠNG THÁI: TẠM NGỪNG DO LỖI VẬN HÀNH")
    print("=====================================================")
        
if __name__ == "__main__":
    main()
