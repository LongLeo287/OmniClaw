import os
import sys
from huggingface_hub import HfApi, hf_hub_download

TARGET_DIR = r"D:\LongLeo\OmniClaw OS\OmniClaw MODELS"
REPO_ID = "douyamv/Gemma-4-31B-JANG_4M-CRACK-GGUF"

def find_q4_file():
    print(f"Scanning repo {REPO_ID} for Q4_K_M GGUF file...")
    api = HfApi()
    files = api.list_repo_files(REPO_ID)
    
    for f in files:
        if "q4_k_m" in f.lower() and f.endswith(".gguf"):
            return f
            
    # Fallback to any q4 file
    for f in files:
        if "q4" in f.lower() and f.endswith(".gguf"):
            return f
            
    print("Could not find a Q4 GGUF file. Available files:", [f for f in files if f.endswith(".gguf")])
    sys.exit(1)

def run():
    os.makedirs(TARGET_DIR, exist_ok=True)
    target_file = find_q4_file()
    print(f"Found target: {target_file}")
    
    print(f"Initiating extreme fetch to {TARGET_DIR}...")
    print("This will download ~18GB. Please monitor network usage.")
    
    # hf_hub_download blocks and shows progress bar to standard error usually.
    downloaded_path = hf_hub_download(
        repo_id=REPO_ID,
        filename=target_file,
        local_dir=TARGET_DIR,
        local_dir_use_symlinks=False
    )
    
    print(f"\n[DOWNLOAD COMPLETE] File saved at: {downloaded_path}")

if __name__ == "__main__":
    run()
