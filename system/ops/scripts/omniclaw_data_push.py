import os
import datetime
import subprocess
import concurrent.futures
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import HfApi, login

# Configuration
AI_OS_ROOT = Path("d:/LongLeo/AI OS CORP/AI OS")
SECRETS_FILE = AI_OS_ROOT / "system/ops/secrets/MASTER.env"
DATASET_REPO = "LongLeo/OmniClaw-Data-Vault"

# Các định dạng thư mục/files thuộc về Trí Nhớ và Core DB
HEAVY_PATTERNS = [
    "*.sqlite", "*.sqlite3", "*.db",
    "brain/memory/*",
    "brain/memory/**/*",
    "storage/_archive/*", 
    "storage/_archive/**/*",
    "storage/temp/*",
    "storage/temp/**/*",
    "storage/vault/memory/*",
    "storage/vault/memory/**/*",
    "system/telemetry/receipts/*",
    "ecosystem/plugins/*",
    "ecosystem/plugins/**/*",
    "*.webp", "*.mp4", "*.mkv", "*.webm", "*.jpg", "*.png"
]

IGNORE_PATTERNS = [
    ".git/*", ".git/**/*",
    "node_modules/*", "node_modules/**/*",
    "__pycache__/*", "__pycache__/**/*"
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
    print("🔑 Authenticating with Hugging Face...")
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
    try:
        res = api.upload_folder(
            folder_path=str(AI_OS_ROOT),
            repo_id=DATASET_REPO,
            repo_type="dataset",
            allow_patterns=HEAVY_PATTERNS,
            ignore_patterns=IGNORE_PATTERNS,
            commit_message=f"OmniClaw Delta Sync: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )
        print(f"\n✅ HF ĐỒNG BỘ HOÀN TẤT. Xem URL: {res}")
        return True
    except Exception as e:
        print(f"\n❌ Lỗi Cản Trở Quá Trình Sync HF: {e}")
        return False

def push_delta_to_googledrive():
    rclone_exe = AI_OS_ROOT / "system/ops/tools/rclone/rclone.exe"
    if not rclone_exe.exists():
        print("\n⚠️ SYSTEM: Chưa phát hiện Rclone (Google Drive Engine). Bỏ qua bước đồng bộ phụ.")
        print("   -> Sếp có thể chạy `system/ops/scripts/setup_gdrive_rclone.ps1` để cài đặt.")
        return False

    # Check if gdrive is configured
    try:
        remotes = subprocess.check_output([str(rclone_exe), "listremotes"], text=True)
        if "gdrive:" not in remotes:
            print("\n❌ LỖI RCLONE: Chưa xác thực Google Drive!")
            print("   -> Bạn cần chạy `system/ops/scripts/setup_gdrive_rclone.ps1` để đăng nhập Web.")
            return False
    except Exception as e:
        return False

    print("\n🚀 Khởi chạy Delta-Sync lên Google Drive (Trạm 2)...")
    
    # Xây dựng file Filter trực tiếp thay vì code tay thủ công
    filter_file = AI_OS_ROOT / "system/ops/tools/rclone/filter_omniclaw.txt"
    with open(filter_file, "w", encoding="utf-8") as f:
        for p in HEAVY_PATTERNS:
            f.write(f"+ {p}\n")
        f.write("- *\n")  # Ignore the rest

    try:
        subprocess.run([
            str(rclone_exe), "sync", str(AI_OS_ROOT), "gdrive:OmniClaw-Data-Vault",
            "--filter-from", str(filter_file),
            "--fast-list", "--transfers", "16", "--checkers", "16",
            "--stats", "10s"
        ], check=True)
        print("✅ GDRIVE ĐỒNG BỘ HOÀN TẤT. Hệ thống đã khớp thư mục với mây Google.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ GDRIVE BÁO LỖI KHI SYNC: {e}")
        return False
        
def main():
    print("=====================================================")
    print(" OmniClaw Data Vault - PARALLEL DUAL DELTA SYNC PIPELINE")
    print("=====================================================")
    hf_token = load_environment()
    
    hf_success = False
    gd_success = False
    
    # Chạy song song cả hai luồng đồng bộ bằng ThreadPoolExecutor
    print("⚡ BẮT ĐẦU ĐỔ SONG SONG CẢ 2 KHO (HUGGING FACE + GOOGLE DRIVE) ⚡\n")
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        future_hf = executor.submit(push_delta_to_huggingface, hf_token)
        future_gd = executor.submit(push_delta_to_googledrive)
        
        hf_success = future_hf.result()
        gd_success = future_gd.result()
    
    print("\n=====================================================")
    if hf_success or gd_success:
        print("🎉 TRẠNG THÁI CUỐI: HOÀN TẤT SONG SONG")
        if hf_success: print("   - [ON] Trạm Hugging Face Hoàn Tất")
        if gd_success: print("   - [ON] Trạm Google Drive Hoàn Tất")
    else:
        print("⚠️ TRẠNG THÁI: TẠM NGỪNG DO LỖI")
    print("=====================================================")
        
if __name__ == "__main__":
    main()

