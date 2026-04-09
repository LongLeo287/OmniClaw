#!/usr/bin/env python3
"""
media_vault.py - OmniClaw Media File Manager
----------------------------------------------
PURPOSE:
  Scan the entire OmniClaw repository for media files (images, audio, video),
  classify them by size and age, move important ones to storage/vault/media/,
  and delete unimportant ones (tiny files, very old cache images, etc.)

USAGE:
  python system/ops/scripts/media_vault.py [--dry-run] [--min-size-kb N]

FLAGS:
  --dry-run       Preview what would happen, no actual moves/deletes
  --min-size-kb   Minimum file size in KB to keep (default: 10 KB)
                  Files below this are considered junk/cache and deleted

DELETION POLICY (safe defaults):
  - Files < 10 KB  → likely thumbnails/cache → DELETE
  - Files in __pycache__, node_modules, .git → skip entirely
  - Files > 10 KB  → move to VAULT for review

VAULT STRUCTURE:
  storage/vault/media/
    ├── images/     (.png, .jpg, .jpeg, .gif, .webp, .bmp, .ico, .svg)
    ├── audio/      (.mp3, .wav, .ogg, .flac, .m4a)
    ├── video/      (.mp4, .avi, .mov, .mkv, .webm)
    └── documents/  (.pdf, .pptx, .docx, .xlsx)
"""

import os
import shutil
import argparse
import datetime
from pathlib import Path

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent.parent.parent
VAULT_BASE = ROOT / "storage" / "vault" / "media"

MEDIA_TYPES = {
    "images":    {".png", ".jpg", ".jpeg", ".gif", ".webp", ".bmp", ".ico"},
    "audio":     {".mp3", ".wav", ".ogg", ".flac", ".m4a", ".aac"},
    "video":     {".mp4", ".avi", ".mov", ".mkv", ".webm", ".wmv"},
    "documents": {".pdf", ".pptx", ".docx", ".xlsx", ".ppt", ".doc"},
}

ALL_MEDIA_EXTENSIONS = set()
for exts in MEDIA_TYPES.values():
    ALL_MEDIA_EXTENSIONS.update(exts)

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", "venv", "env",
    "releases", "Trash_Before_Push", ".vscode", ".claude",
    # Skip vault itself to avoid re-processing
    "vault",
}

# Directories where media files almost always belong and should NOT be moved
# (they are part of third-party repo documentation)
PROTECTED_PARENT_DIRS = {"docs", "documentation", "assets", "public", "static"}


def get_category(extension: str) -> str:
    """Return vault subfolder name for a given file extension."""
    ext = extension.lower()
    for category, exts in MEDIA_TYPES.items():
        if ext in exts:
            return category
    return "misc"


def format_size(size_bytes: int) -> str:
    """Human-readable file size."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    else:
        return f"{size_bytes / (1024*1024):.2f} MB"


def format_date(timestamp: float) -> str:
    """Human-readable modification date."""
    return datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def is_in_protected_location(fp: Path) -> bool:
    """Check if file is inside a third-party repo documentation folder."""
    parts = fp.parts
    # If the file is deep inside brain/knowledge/repos, leave it alone
    if "brain" in parts and "knowledge" in parts:
        return True
    if "ecosystem" in parts and "plugins" in parts:
        return True
    if "QUARANTINE" in parts:
        return True
    return False


def scan_media_files(min_size_kb: int = 10) -> dict:
    """
    Walk the entire ROOT directory (excluding protected dirs),
    return classification results: delete_list, move_list, skip_list.
    """
    min_size_bytes = min_size_kb * 1024

    delete_list = []  # Too small → junk
    move_list = []    # OK size → move to vault
    skip_list = []    # Protected location or already in vault

    for dirpath, dirnames, filenames in os.walk(ROOT):
        # Prune traversal
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]

        for f in filenames:
            fp = Path(dirpath) / f
            if fp.suffix.lower() not in ALL_MEDIA_EXTENSIONS:
                continue

            try:
                stat = fp.stat()
                size = stat.st_size
                mtime = stat.st_mtime
            except Exception:
                continue

            # Skip if already in vault
            if VAULT_BASE in fp.parents:
                skip_list.append(fp)
                continue

            # Skip if in protected third-party location
            if is_in_protected_location(fp):
                skip_list.append(fp)
                continue

            if size < min_size_bytes:
                delete_list.append((fp, size, mtime))
            else:
                category = get_category(fp.suffix)
                move_list.append((fp, size, mtime, category))

    return {
        "delete": delete_list,
        "move": move_list,
        "skip": skip_list,
    }


def execute_media_vault(dry_run: bool = False, min_size_kb: int = 10):
    """Main entry point: scan, classify, move, and delete media files."""
    print("=" * 65)
    print("  OMNICLAW MEDIA VAULT MANAGER")
    print(f"  Root       : {ROOT}")
    print(f"  Vault      : {VAULT_BASE}")
    print(f"  Min size   : {min_size_kb} KB (below this = DELETED as junk)")
    print(f"  Mode       : {'DRY RUN (preview only)' if dry_run else 'LIVE (files will move/delete)'}")
    print("=" * 65)

    print("\n[SCANNING] Walking repository for media files...")
    results = scan_media_files(min_size_kb=min_size_kb)

    delete_list = results["delete"]
    move_list = results["move"]
    skip_list = results["skip"]

    total_delete_size = sum(s for _, s, _ in delete_list)
    total_move_size = sum(s for _, s, _, _ in move_list)

    print(f"\n  Found {len(delete_list)} junk files  → will DELETE  ({format_size(total_delete_size)} freed)")
    print(f"  Found {len(move_list)} media files   → will MOVE to vault ({format_size(total_move_size)})")
    print(f"  Found {len(skip_list)} protected files → will SKIP\n")

    # ── Phase 1: Create vault directories ──
    if not dry_run:
        for cat in list(MEDIA_TYPES.keys()) + ["misc"]:
            (VAULT_BASE / cat).mkdir(parents=True, exist_ok=True)

    # ── Phase 2: Delete junk files ──
    deleted_count = 0
    print("[PHASE 1] Deleting junk/cache media files...")
    for fp, size, mtime in sorted(delete_list, key=lambda x: x[1]):
        print(f"  DELETE ({format_size(size)}, {format_date(mtime)})  {fp.relative_to(ROOT)}")
        if not dry_run:
            try:
                fp.unlink()
                deleted_count += 1
            except Exception as e:
                print(f"    [ERROR] Cannot delete: {e}")

    # ── Phase 3: Move important media to vault ──
    moved_count = 0
    print(f"\n[PHASE 2] Moving media files to {VAULT_BASE.relative_to(ROOT)}...")
    for fp, size, mtime, category in sorted(move_list, key=lambda x: -x[1]):
        dest_dir = VAULT_BASE / category
        dest = dest_dir / fp.name

        # Handle filename collision
        if dest.exists():
            stem = fp.stem
            suffix = fp.suffix
            dest = dest_dir / f"{stem}_{int(mtime)}{suffix}"

        print(f"  MOVE ({format_size(size)}, {format_date(mtime)})  {fp.relative_to(ROOT)} -> {dest.relative_to(ROOT)}")
        if not dry_run:
            try:
                shutil.move(str(fp), str(dest))
                moved_count += 1
            except Exception as e:
                print(f"    [ERROR] Cannot move: {e}")

    # ── Summary ──
    print("\n" + "=" * 65)
    if dry_run:
        print(f"  [DRY RUN COMPLETE] No files were actually changed.")
        print(f"  Would delete : {len(delete_list)} files ({format_size(total_delete_size)})")
        print(f"  Would move   : {len(move_list)} files to vault")
    else:
        print(f"  [LIVE RUN COMPLETE]")
        print(f"  Deleted     : {deleted_count} junk files ({format_size(total_delete_size)} freed)")
        print(f"  Moved       : {moved_count} files → {VAULT_BASE.relative_to(ROOT)}")
    print("=" * 65)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OmniClaw Media Vault Manager")
    parser.add_argument("--dry-run", action="store_true", help="Preview without making changes")
    parser.add_argument("--min-size-kb", type=int, default=10,
                        help="Min size in KB to keep (smaller = deleted as junk, default: 10)")
    args = parser.parse_args()
    execute_media_vault(dry_run=args.dry_run, min_size_kb=args.min_size_kb)