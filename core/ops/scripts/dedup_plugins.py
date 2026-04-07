import os
import shutil
from collections import defaultdict

PLUGINS_DIR = r"D:\LongLeo\OmniClaw OS\OmniClaw\ecosystem\plugins"

def normalize_id(name: str) -> str:
    n = name.lower()
    for suffix in [".git", "-main", "-master", ".main", ".master"]:
        if n.endswith(suffix):
            n = n[:-len(suffix)]
    return n.replace("-", "_").replace(".", "_")

def main():
    print(f"[DEDUP] Starting deduplication sweep on {PLUGINS_DIR}")
    if not os.path.exists(PLUGINS_DIR):
        print("Plugins dir doesn't exist.")
        return

    items = os.listdir(PLUGINS_DIR)
    groups = defaultdict(list)
    for item in items:
        item_path = os.path.join(PLUGINS_DIR, item)
        if os.path.isdir(item_path):
            norm_id = normalize_id(item)
            groups[norm_id].append(item)

    print(f"[DEDUP] Found {len(items)} items. Mapped to {len(groups)} unique normalized IDs.")
    
    merged_count = 0
    deleted_count = 0

    for norm_id, duplicates in groups.items():
        if len(duplicates) > 1:
            print(f"\n[GROUP MULTIPLE] ID: {norm_id}")
            print(f" -> Found Clones: {duplicates}")
            # Target is the one that exactly matches norm_id if it exists, otherwise the shortest name
            target = norm_id if norm_id in duplicates else sorted(duplicates, key=len)[0]
            target_path = os.path.join(PLUGINS_DIR, target)
            
            # If target didn't exist yet as a folder, but another did, create the target folder
            # Wait, target ALWAYS exists in `duplicates` by definition of the line above:
            # target = norm_id if norm_id in duplicates else sorted(duplicates, key=len)[0]
            if not os.path.exists(target_path):
                 os.makedirs(target_path, exist_ok=True)
                 
            for dup in duplicates:
                if dup != target:
                    dup_path = os.path.join(PLUGINS_DIR, dup)
                    print(f"  [>] Merging '{dup}' into '{target}'...")
                    for root, dirs, files in os.walk(dup_path):
                        rel = os.path.relpath(root, dup_path)
                        trg_dir = os.path.join(target_path, rel)
                        os.makedirs(trg_dir, exist_ok=True)
                        for f in files:
                            try:
                                shutil.copy2(os.path.join(root, f), os.path.join(trg_dir, f))
                            except Exception: pass
                    try:
                        shutil.rmtree(dup_path, ignore_errors=True)
                        deleted_count += 1
                    except Exception: pass
            
            # If norm_id was NOT in duplicates initially but we created it, we should move the shortest there.
            if target == norm_id and norm_id not in duplicates:
                # Actually, the logic above assigned target to shortest if norm_id wasn't in duplicates.
                # So we are fine, no need for extra logic.
                pass
                
            merged_count += 1

    print(f"\n[STAT] Deduplication complete. Duplicate Groups Merged: {merged_count}. Redundant Folders Swept: {deleted_count}.")

if __name__ == "__main__":
    main()
