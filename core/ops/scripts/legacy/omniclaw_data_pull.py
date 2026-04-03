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
DATASET_REPO = "OmniClaw_Admin/OmniClaw-Data-Vault"

# =========================================================================
# [System log: Legacy non-English comment removed]
# [System log: Legacy non-English comment removed]
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
        print("[OmniClaw System Event]")...")
    except Exception as e:
        print("[OmniClaw System Event]")
        return False

    print("[OmniClaw System Event]")...")
    success = True
    
    # [System log: Legacy non-English comment removed]
    # [System log: Legacy non-English comment removed]
    allow_list = [f"{vault}/**" for vault in TARGET_VAULTS]
    
    try:
        print("[OmniClaw System Event]")
        # [System log: Legacy non-English comment removed]
        downloaded_path = snapshot_download(
            repo_id=DATASET_REPO,
            repo_type="dataset",
            allow_patterns=allow_list,
            local_dir=str(AI_OS_ROOT),
            local_dir_use_symlinks=False,  # [Removed legacy comment]
            ignore_patterns=["*gitkeep*"]
        )
        print("[OmniClaw System Event]")
    except Exception as e:
        print("[OmniClaw System Event]"): {e}")
        success = False

    return success

def pull_from_googledrive():
    rclone_exe = AI_OS_ROOT / "system/ops/tools/rclone/rclone.exe"
    if not rclone_exe.exists():
        print("[OmniClaw System Event]"). Tạm lược bỏ kéo luồng GDrive.")
        return False

    # Check if gdrive is configured
    try:
        remotes = subprocess.check_output([str(rclone_exe), "listremotes"], text=True)
        if "gdrive:" not in remotes:
            print("[OmniClaw System Event]")
            return False
    except Exception as e:
        return False

    print("[OmniClaw System Event]")...")
    success = True
    for folder in TARGET_VAULTS:
        dest_path = AI_OS_ROOT / folder
        # Ensure base path exists for destination to avoid rclone panic
        dest_path.mkdir(parents=True, exist_ok=True)
        print("[OmniClaw System Event]")
        try:
             # [System log: Legacy non-English comment removed]
             subprocess.run([
                 str(rclone_exe), "copy", f"gdrive:OmniClaw-Data-Vault/{folder}", str(dest_path),
                 "--fast-list", "--transfers", "16", "--checkers", "16",
                 "--stats", "30s"
             ], check=True)
        except subprocess.CalledProcessError as e:
             print("[OmniClaw System Event]") {folder}: {e}")
             success = False

    if success:
        print("[OmniClaw System Event]")
    return success
        
def main():
    print("=====================================================")
    print(" OmniClaw Data Vault - TARGETED PULL PIPELINE (DATA RESTORE)")
    print("=====================================================")
    hf_token = load_environment()
    
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")
    
    pull_target = input("\n[?] Sếp muốn tải Lõi từ Trạm Mây nào? (1: Hugging Face, 2: Google Drive, 3: Song Song cả 2): ").strip()
    
    hf_success = False
    gd_success = False
    
    if pull_target == '1' or pull_target == '3':
        hf_success = pull_from_huggingface(hf_token)
    
    if pull_target == '2' or pull_target == '3':
        gd_success = pull_from_googledrive()
        
    # [NEW] Restore Symlink Junctions automatically after Cloud Pull
    if hf_success or gd_success:
        print("[OmniClaw System Event]")...")
        restore_script = AI_OS_ROOT / "system" / "ops" / "scripts" / "restore_links.py"
        if restore_script.exists():
            subprocess.run(["python", str(restore_script)])
            print("[OmniClaw System Event]")
    
    print("\n=====================================================")
    print("[OmniClaw System Event]")
    if pull_target in ['1', '3']:
        print("[OmniClaw System Event]")
    if pull_target in ['2', '3']:
        print("[OmniClaw System Event]")
    print("=====================================================")
        
if __name__ == "__main__":
    main()