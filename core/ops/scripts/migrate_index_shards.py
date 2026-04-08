import os
import json
import shutil
from collections import defaultdict

def migrate():
    repo_root = r"D:\OmniClaw"
    legacy_fast_index = os.path.join(repo_root, "brain", "registry", "FAST_INDEX.json")
    indices_dir = os.path.join(repo_root, "brain", "indices")
    archives_dir = os.path.join(repo_root, "vault", "archives")
    
    os.makedirs(indices_dir, exist_ok=True)
    os.makedirs(archives_dir, exist_ok=True)
    
    if not os.path.exists(legacy_fast_index):
        print("Legacy FAST_INDEX.json not found. Migration skipped.")
        return

    with open(legacy_fast_index, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    registry = data.get("registry", data) if isinstance(data, dict) else data
    if not isinstance(registry, list):
        print("Invalid registry format.")
        return

    shards = defaultdict(list)
    for entry in registry:
        asset_type = entry.get("type", "UNKNOWN").upper()
        shards[asset_type].append(entry)
        
    for asset_type, entries in shards.items():
        shard_path = os.path.join(indices_dir, f"FAST_{asset_type}_INDEX.json")
        with open(shard_path, "w", encoding="utf-8") as f:
            json.dump({"registry": entries}, f, indent=2, ensure_ascii=False)
        print(f"Created shard: FAST_{asset_type}_INDEX.json with {len(entries)} entries.")
        
    # Archive monolithic
    archive_path = os.path.join(archives_dir, "FAST_INDEX_ARCHIVED.json")
    shutil.move(legacy_fast_index, archive_path)
    print(f"Successfully archived legacy index to: {archive_path}")

if __name__ == "__main__":
    migrate()
