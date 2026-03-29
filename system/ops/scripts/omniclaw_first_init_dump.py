import os
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import HfApi, login

def first_time_dump():
    AI_OS_ROOT = Path("d:/LongLeo/AI OS CORP/AI OS")
    SECRETS_FILE = AI_OS_ROOT / "system/ops/secrets/MASTER.env"
    DATASET_REPO = "LongLeo/OmniClaw-Data-Vault"

    print("🚀 Bắt đầu chiến dịch đổ kho Data First-Time Exception!")
    
    if SECRETS_FILE.exists():
        load_dotenv(SECRETS_FILE)
    login(token=os.getenv("HF_TOKEN"))
    api = HfApi()

    # DUMP 1: SQLite Databases at Root
    for db_file in AI_OS_ROOT.glob("*.db"):
        print(f"📦 Đang đẩy CSDL ở Root: {db_file.name}")
        api.upload_file(path_or_fileobj=str(db_file), path_in_repo=db_file.name, repo_id=DATASET_REPO, repo_type="dataset")
    for db_file in AI_OS_ROOT.glob("*.sqlite*"):
        print(f"📦 Đang đẩy CSDL ở Root: {db_file.name}")
        api.upload_file(path_or_fileobj=str(db_file), path_in_repo=db_file.name, repo_id=DATASET_REPO, repo_type="dataset")

    # DUMP 2: BRAIN FOLDER (TRÍ TÚE)
    brain_dir = AI_OS_ROOT / "brain"
    if brain_dir.exists():
        print("🧠 Đang xuất file vùng Não Trí Tuệ (Brain)...")
        api.upload_folder(folder_path=str(brain_dir), path_in_repo="brain", repo_id=DATASET_REPO, repo_type="dataset")
        print("✅ Đổ Brain xong.")

    # DUMP 3: STORAGE FOLDER (KHO DỮ LIỆU)
    storage_dir = AI_OS_ROOT / "storage"
    if storage_dir.exists():
        print("💽 Đang xuất file vùng Lưu Trữ Không Gian (Storage)...")
        api.upload_folder(folder_path=str(storage_dir), path_in_repo="storage", repo_id=DATASET_REPO, repo_type="dataset", ignore_patterns=["*node_modules*", "*.git*"])
        print("✅ Đổ Storage xong.")

    print("\n🎉 CHIẾN DỊCH NGOẠI LỆ HOÀN TẤT. KHO DATA ĐÃ ĐẦY!")
    print(f"🔗 Mời Sếp kiểm tra: https://huggingface.co/datasets/{DATASET_REPO}/tree/main")

if __name__ == '__main__':
    first_time_dump()
