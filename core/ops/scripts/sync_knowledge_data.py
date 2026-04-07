#!/usr/bin/env python3
"""
OmniClaw Knowledge Base — Data Sync Script
Target: HuggingFace Dataset + Google Drive
Source: D:\LongLeo\OC\brain\knowledge\

Usage:
    python sync_knowledge_data.py --target hf        # Sync to HuggingFace
    python sync_knowledge_data.py --target gdrive     # Sync to Google Drive
    python sync_knowledge_data.py --target all        # Sync to both
"""

import argparse
import os
import sys

# ===== CONFIGURATION =====
HF_REPO_ID = "longleo/omniclaw-knowledge-base"  # HuggingFace Dataset repo
HF_REPO_TYPE = "dataset"
KNOWLEDGE_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "brain\knowledge")

# Folders to sync (heavy data - primary storage)
SYNC_FOLDERS = [
    "general",        # 5.88 GB - knowledge dump .md files
    "repositories",   # 1.89 GB - FETCHED source repos
    "api",            # 935 MB  - API source repos
    "library",        # 29 MB   - curated docs
    "bmad_repo",      # 1.2 MB  - BMAD methodology
    "skills_standard_repo",  # curated skill standards
    "claude_bp_repo",        # Claude best practices
    "frameworks",            # framework repos
    "repo_godi13hub_io",
    "repo_hyperspace_db",
    "repo_gh_supabase_agent_skills",
]

# ===== HuggingFace Sync =====
def sync_to_huggingface():
    try:
        from huggingface_hub import HfApi, create_repo
    except ImportError:
        print("ERROR: Install huggingface_hub first: pip install huggingface_hub")
        sys.exit(1)

    api = HfApi()

    # Create repo if not exists
    try:
        create_repo(HF_REPO_ID, repo_type=HF_REPO_TYPE, exist_ok=True, private=True)
        print(f"[HF] Repo ready: {HF_REPO_ID}")
    except Exception as e:
        print(f"[HF] Repo create error: {e}")

    # Upload folders
    for folder in SYNC_FOLDERS:
        local_path = os.path.join(KNOWLEDGE_DIR, folder)
        if not os.path.exists(local_path):
            print(f"[HF] SKIP (not found): {folder}")
            continue
        print(f"[HF] Uploading: {folder} ...")
        try:
            api.upload_folder(
                folder_path=local_path,
                path_in_repo=f"knowledge/{folder}",
                repo_id=HF_REPO_ID,
                repo_type=HF_REPO_TYPE,
                ignore_patterns=["*.pyc", "__pycache__", ".git", "*.whl"],
            )
            print(f"[HF] DONE: {folder}")
        except Exception as e:
            print(f"[HF] ERROR {folder}: {e}")


# ===== Google Drive Sync (via rclone) =====
def sync_to_gdrive():
    import subprocess
    # Requires rclone configured with 'gdrive' remote
    GDRIVE_REMOTE = "gdrive:OmniClaw/knowledge"

    for folder in SYNC_FOLDERS:
        local_path = os.path.join(KNOWLEDGE_DIR, folder)
        if not os.path.exists(local_path):
            print(f"[GDrive] SKIP (not found): {folder}")
            continue
        print(f"[GDrive] Syncing: {folder} ...")
        result = subprocess.run([
            "rclone", "sync",
            local_path,
            f"{GDRIVE_REMOTE}/{folder}",
            "--progress",
            "--exclude", "*.pyc",
            "--exclude", "__pycache__/**",
            "--exclude", ".git/**",
            "--exclude", "*.whl",
        ], capture_output=False)
        if result.returncode == 0:
            print(f"[GDrive] DONE: {folder}")
        else:
            print(f"[GDrive] ERROR: {folder}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OmniClaw Knowledge Base Sync")
    parser.add_argument("--target", choices=["hf", "gdrive", "all"], default="all")
    args = parser.parse_args()

    if args.target in ("hf", "all"):
        print("\n=== Syncing to HuggingFace ===")
        sync_to_huggingface()

    if args.target in ("gdrive", "all"):
        print("\n=== Syncing to Google Drive ===")
        sync_to_gdrive()

    print("\nSync complete.")
