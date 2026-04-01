#!/usr/bin/env python3
"""
omniclaw_cleanup_crew.py - OmniClaw Pre-Push Cleanup Utility
--------------------------------------------------------------
PURPOSE:
  Scan designated target folders for junk/ephemeral files and directories,
  then safely quarantine them before any cloud sync or git push operation.

JUNK TARGETS:
  Files : .log, .tmp, .temp, .bak, .swp, .dmp, .DS_Store, Thumbs.db
  Dirs  : __pycache__, .pytest_cache

SAFE DESIGN:
  - Junk is MOVED (not deleted) to a quarantine vault, allowing recovery
  - Does NOT touch .git, node_modules, or any system-critical directories
  - Idempotent: safe to run multiple times

USAGE:
  python omniclaw_cleanup_crew.py [folder1] [folder2] ...
  python omniclaw_cleanup_crew.py brain/memory storage/vault
  python omniclaw_cleanup_crew.py .   (scan entire repo)
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

# Dynamic root detection — NO hardcoded paths
AI_OS_ROOT = Path(__file__).resolve().parent.parent.parent.parent
TRASH_VAULT = AI_OS_ROOT / "storage" / "vault" / "QUARANTINE" / "Trash_Before_Push"

# Junk file signatures
TRASH_FILE_EXTENSIONS = {'.log', '.tmp', '.temp', '.bak', '.swp', '.dmp', '.DS_Store'}
TRASH_DIR_NAMES = {'__pycache__', '.pytest_cache'}

# Directories that must never be traversed
PROTECTED_DIRS = {'.git', 'node_modules', 'venv', 'env', 'vault', 'QUARANTINE'}


def is_junk(path_obj: Path) -> bool:
    """Return True if the given path is classified as junk."""
    if path_obj.is_file():
        return path_obj.suffix.lower() in TRASH_FILE_EXTENSIONS or \
               path_obj.name in {'Thumbs.db', 'desktop.ini'}
    if path_obj.is_dir():
        return path_obj.name in TRASH_DIR_NAMES
    return False

def flush_npm_cache():
    """Execute 'npm cache clean --force' to sterilize supply chain hazards."""
    print("\n  [NPM SANITATION] Pumping out global npm cache...")
    try:
        # We use shell=True on Windows to resolve "npm" from path correctly
        result = subprocess.run(["npm", "cache", "clean", "--force"], 
                                capture_output=True, text=True, shell=True, check=True)
        print("    [CLEAN] Cache incinerated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"    [WARN] npm cache clean failed: {e.stderr.strip()}")
    except FileNotFoundError:
        print("    [SKIP] 'npm' command not found on this system.")


def deploy_cleanup_crew(target_folders_list: list, base_path=AI_OS_ROOT, trash_vault=TRASH_VAULT) -> int:
    """
    Scan specified folders for junk, quarantine all found items.

    Args:
        target_folders_list: List of relative folder paths to scan.
        base_path: Root path to resolve folders against (default: AI_OS_ROOT).
        trash_vault: Override the destination for quarantined items.

    Returns:
        Number of items quarantined.
    """
    print("\n=====================================================")
    print("  [CLEANUP CREW] PRE-FLIGHT SCAN INITIATED")
    print("=====================================================")

    trash_vault.mkdir(parents=True, exist_ok=True)
    quarantine_count = 0

    for folder in target_folders_list:
        scan_path = Path(base_path) / folder
        if not scan_path.exists():
            print(f"  [SKIP] Target not found: {folder}")
            continue

        print(f"  [SCAN] Entering sector: {folder}")

        # Walk top-down to allow pruning of directories
        for root, dirs, files in os.walk(scan_path, topdown=True):
            # Prune protected directories to prevent deep traversal hangs
            dirs[:] = [d for d in dirs if d not in PROTECTED_DIRS]

            current = Path(root)

            # Phase 1: Quarantine junk files
            for file_name in files:
                file_path = current / file_name
                if is_junk(file_path):
                    dest = trash_vault / f"{file_path.parent.name}_{file_name}"
                    try:
                        shutil.move(str(file_path), str(dest))
                        quarantine_count += 1
                        print(f"    [TRASH] File: {file_name}")
                    except Exception:
                        pass

            # Phase 2: Quarantine junk directories
            for dir_name in list(dirs):
                dir_path = current / dir_name
                if is_junk(dir_path):
                    dest = trash_vault / f"{dir_path.parent.name}_{dir_name}"
                    try:
                        shutil.move(str(dir_path), str(dest))
                        quarantine_count += 1
                        dirs.remove(dir_name) # Prevent traversing deleted directory
                        print(f"    [TRASH] Directory: {dir_name}/")
                    except Exception:
                        pass

    # Summary
    if quarantine_count > 0:
        try:
            rel = trash_vault.relative_to(AI_OS_ROOT)
        except ValueError:
            rel = trash_vault
        print(f"\n  [DONE] {quarantine_count} items quarantined -> {rel}")
    else:
        print("\n  [DONE] Sector is clean. No junk detected.")

    return quarantine_count


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="OmniClaw Pre-Push Cleanup Utility")
    parser.add_argument("folders", nargs="*", default=["brain/memory", "storage/vault", "ecosystem/plugins"],
                        help="Target folders to scan (relative to AI_OS_ROOT)")
    parser.add_argument("--quarantine-path", type=str, default=str(TRASH_VAULT),
                        help="Override default quarantine path")
    args = parser.parse_args()

    custom_vault = Path(args.quarantine_path)
    deploy_cleanup_crew(args.folders, trash_vault=custom_vault)
    
    # Unleash NPM cache flush at the end of routine maintenance
    flush_npm_cache()