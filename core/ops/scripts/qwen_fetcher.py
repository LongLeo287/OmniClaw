import os
import sys
from huggingface_hub import hf_hub_download

TARGET_DIR = r"D:\LongLeo\OmniClaw OS\OmniClaw MODELS\Qwen-2.5-Coder-7B"
REPO_ID = "Qwen/Qwen2.5-Coder-7B-Instruct-GGUF"
FILENAME = "qwen2.5-coder-7b-instruct-q4_k_m.gguf"

def run():
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    print(f"Initiating high-speed solid state fetch to {TARGET_DIR}...")
    print(f"Targeting File: {FILENAME}")
    
    try:
        downloaded_path = hf_hub_download(
            repo_id=REPO_ID,
            filename=FILENAME,
            local_dir=TARGET_DIR,
            local_dir_use_symlinks=False
        )
        print(f"\n[DOWNLOAD COMPLETE] Qwen-2.5-Coder Core successfully hardened at:\n{downloaded_path}")
    except Exception as e:
        print(f"\n[ERROR] Fetch failed: {e}")

if __name__ == "__main__":
    run()
