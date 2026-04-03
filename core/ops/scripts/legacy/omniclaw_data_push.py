import os
import sys
import datetime
import subprocess
import concurrent.futures
from pathlib import Path
from dotenv import load_dotenv
from huggingface_hub import HfApi, login

# Configuration (Dynamic paths)
AI_OS_ROOT = Path(__file__).resolve().parent.parent.parent.parent
SECRETS_FILE = AI_OS_ROOT / "system" / "ops" / "secrets" / "MASTER.env"
DATASET_REPO = "OmniClaw_Admin/OmniClaw-Data-Vault"

# =========================================================================
# DATA VAULT TARGETS
# Only push these highly curated folders. Ignore everything else.
# =========================================================================
TARGET_VAULTS = [
    "brain/memory",
    "storage/vault",
    "ecosystem/plugins"
]

IGNORE_PATTERNS = [".git", "node_modules", "__pycache__", ".env", "sandbox", "*.pack", "*.idx"]

def load_environment():
    if SECRETS_FILE.exists():
        load_dotenv(SECRETS_FILE)
    
    hf_token = os.getenv("HF_TOKEN")
    if not hf_token:
        print("[ERROR] HF_TOKEN missing from MASTER.env or environment variables.")
        exit(1)
    return hf_token

def push_delta_to_huggingface(hf_token):
    print("\n Authenticating with Hugging Face...")
    login(token=hf_token)
    api = HfApi()
    
    print(f" Validating HF repository: {DATASET_REPO}")
    try:
        api.dataset_info(DATASET_REPO)
        print(" HF Repository exists.")
    except Exception as e:
        print(" HF Repository not found or inaccessible. Creating a new private dataset repository...")
        try:
            api.create_repo(repo_id=DATASET_REPO, repo_type="dataset", private=True, exist_ok=True)
            print(" Created new repository on Hugging Face.")
        except Exception as ce:
            print(f" CANNOT CREATE NEW DATASET! Missing 'Write' permissions on HF Token: {ce}")
            return False

    print(" Initiating Delta-Sync to Hugging Face...")
    success = True
    for folder in TARGET_VAULTS:
        folder_path = AI_OS_ROOT / folder
        if folder_path.exists() and folder_path.is_dir():
            print(f"   [HF] Synchronizing heavy vault folder: {folder} ...")
            try:
                api.upload_folder(
                    folder_path=str(folder_path),
                    repo_id=DATASET_REPO,
                    repo_type="dataset",
                    path_in_repo=folder,
                    ignore_patterns=IGNORE_PATTERNS,
                    commit_message=f"OmniClaw Vault Sync [{folder}]: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
                )
            except Exception as e:
                print(f"       Failed to push {folder} to HF: {e}")
                success = False
        else:
            print(f"   [HF] Skipping {folder} (Path does not exist)")

    if success:
        print(f"\n HF SYNC COMPLETE: Core data vaults preserved (Trash excluded).")
    return success

def scrub_ghost_folders(rclone_exe):
    print("\n Scrubbing and purging ghost trash folders on Google Drive...")
    try:
        result = subprocess.check_output([str(rclone_exe), "lsf", "gdrive:OmniClaw-Data-Vault"], text=True)
        items = result.strip().split("\n")
        
        allowed_roots = [d.split('/')[0] + "/" for d in TARGET_VAULTS]
        
        folders_deleted = 0
        for item in items:
            if not item: continue
            if item.endswith("/") and item not in allowed_roots:
                junk_dir = f"gdrive:OmniClaw-Data-Vault/{item.strip('/')}"
                print(f"    Purging unexpected root directory on Cloud: {junk_dir}")
                subprocess.run([str(rclone_exe), "purge", junk_dir], check=True)
                folders_deleted += 1
                
        if folders_deleted > 0:
            print(f" Successfully vaporized {folders_deleted} ghost directories on Google Drive!")
        else:
            print(" Google Drive space is perfectly clean. No anomalies detected.")
            
    except subprocess.CalledProcessError as e:
         print(f"    Warning: Scrubbing process encountered an obstacle: {e}")

def push_delta_to_googledrive():
    rclone_exe = AI_OS_ROOT / "system" / "ops" / "tools" / "rclone" / "rclone.exe"
    if not rclone_exe.exists():
        print("\n WARNING: Rclone binary missing. Google Drive synchronization skipped.")
        return False

    try:
        remotes = subprocess.check_output([str(rclone_exe), "listremotes"], text=True)
        if "gdrive:" not in remotes:
            print("\n RCLONE ERROR: 'gdrive:' remote is not authenticated!")
            return False
    except Exception as e:
        return False

    scrub_ghost_folders(rclone_exe)

    print("\n Initiating Delta-Sync to Google Drive...")
    success = True
    
    filter_args = []
    for ignore in IGNORE_PATTERNS:
        if ignore.startswith("*"):
            filter_args.extend(["--exclude", f"{ignore}"])
        else:
            filter_args.extend(["--exclude", f"{ignore}/**"])

    for folder in TARGET_VAULTS:
        folder_path = AI_OS_ROOT / folder
        if folder_path.exists() and folder_path.is_dir():
             print(f"   [GDrive] Synchronizing heavy vault folder: {folder} ...")
             try:
                 cmd = [
                     str(rclone_exe), "sync", str(folder_path), f"gdrive:OmniClaw-Data-Vault/{folder}",
                     "--delete-excluded",
                     "--fast-list", "--transfers", "16", "--checkers", "16",
                     "--stats", "30s"
                 ] + filter_args
                 
                 subprocess.run(cmd, check=True)
             except subprocess.CalledProcessError as e:
                 print(f"       GDrive synchronization failed for {folder}: {e}")
                 success = False
        else:
             print(f"   [GDrive] Skipping {folder} (Path does not exist)")

    if success:
        print("\n GDRIVE SYNC COMPLETE. 100% Absolute Mirror with Zero Trash.")
    return success
        
import omniclaw_cleanup_crew

def main():
    print("=====================================================")
    print(" OmniClaw Core Vault - TARGETED DATA PIPELINE")
    print("=====================================================")
    hf_token = load_environment()
    
    # TRIGGER PRE-FLIGHT CLEANUP CHECK
    omniclaw_cleanup_crew.deploy_cleanup_crew(TARGET_VAULTS)
    
    print("\n INITIATING MASSIVE CLOUD DATA UPLOAD \n")
    
    hf_success = push_delta_to_huggingface(hf_token)
    gd_success = push_delta_to_googledrive()
    
    print("\n=====================================================")
    if hf_success or gd_success:
        print(" FINAL STATUS: OPERATION SUCCEEDED")
        if hf_success: print("   - [ON] Hugging Face Station Secure")
        if gd_success: print("   - [ON] Google Drive Sector Purified")
    else:
        print(" FINAL STATUS: OPERATION HALTED DUE TO ERRORS")
    print("=====================================================")
        
if __name__ == "__main__":
    main()