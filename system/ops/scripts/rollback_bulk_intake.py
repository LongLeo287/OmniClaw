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
    for fpath in files:
        # Chỉ xóa những file do V2 tạo (có url_entry, hoặc những file thuộc 91 URLs)
        # Để an toàn, đọc nội dung xem submitter có phải là "antigravity-bulk-intake-v2" không
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
                        os.unlink(fpath) if os.path.islink(fpath) else os.remove(fpath)
                        print(f"  [-] Rollback (Deleted): {os.path.basename(fpath)}")
                    else:
                        print(f"  [DRY-RUN] Will Delete: {os.path.basename(fpath)}")
                    deleted_count += 1
        except Exception as e:
            print(f"  [!] Error reading/deleting {os.path.basename(fpath)}: {e}")

    print(f"\n[SUCCESS] Emptied/Identified {deleted_count} massive intake tickets from Vault.")
    if not force:
        print("[!] Run with --force to apply deletion.")
    else:
        print("The system is safe from digesting unfiltered data. Awaiting proper evaluation workflow.")

if __name__ == "__main__":
    main()
