import os
import glob
import sys
import datetime

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
VAULT_DATA_DIR = os.path.join(BASE_DIR, 'storage', 'vault', 'DATA')

def main():
    force = "--force" in sys.argv
    print(f"[{datetime.datetime.now().isoformat()}] STARTING EMERGENCY ROLLBACK...")
    if not force:
        print("[!] DRY-RUN MODE: Add --force to actually delete files.")

    # Tìm tất cả các file do bulk_repo_intake_v2 tạo ra (bulk_intake_v2)
    # hoặc tất cả file KI-*.json có source_type: url_repo_bulk
    search_pattern = os.path.join(VAULT_DATA_DIR, 'KI-*_*.json')
    files = glob.glob(search_pattern)

    deleted_count = 0
    if force and files:
        confirm = input(f"[!] WARNING: This will delete files containing 'antigravity-bulk-intake-v2'. Continue? [y/N]: ")
        if confirm.lower() != 'y':
            print("Aborted.")
            return

    deleted_log = []
    for fpath in files:
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
            if '"submitted_by": "antigravity-bulk-intake-v2"' in content:
                if force:
                    real_path = os.path.realpath(fpath)
                    vault_real = os.path.realpath(VAULT_DATA_DIR)
                    if not real_path.startswith(vault_real):
                        print(f"  [!] SECURITY: Symlink points outside vault, skipping: {fpath}")
                        continue
                    if os.path.islink(fpath): os.unlink(fpath)
                    else: os.remove(fpath)
                    print(f"  [-] Rollback (Deleted): {os.path.basename(fpath)}")
                    deleted_log.append(fpath)
                else:
                    print(f"  [DRY-RUN] Will Delete: {os.path.basename(fpath)}")
                deleted_count += 1
        except Exception as e:
            print(f"  [!] Error reading/deleting {os.path.basename(fpath)}: {e}")

    if force and deleted_log:
        receipt_dir = os.path.join(BASE_DIR, 'system', 'telemetry', 'receipts', 'system')
        os.makedirs(receipt_dir, exist_ok=True)
        import json
        receipt = {
            "timestamp": datetime.datetime.now().isoformat(),
            "action": "ROLLBACK_BULK_INTAKE",
            "deleted_count": deleted_count,
            "deleted_files": deleted_log
        }
        with open(os.path.join(receipt_dir, f"rollback_{int(datetime.datetime.now().timestamp())}.json"), 'w') as rf:
            json.dump(receipt, rf, indent=2)

    print(f"\n[SUCCESS] Emptied/Identified {deleted_count} massive intake tickets from Vault.")
    if not force:
        print("[!] Run with --force to apply deletion.")
    else:
        print("The system is safe from digesting unfiltered data. Awaiting proper evaluation workflow.")

if __name__ == "__main__":
    main()
