import os, shutil, stat

DAEMON_NAME = "OMA [Deep Janitor]"
TMP_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp")
PROTECTED_ITEMS = {"quarantine", "raw_knowledge_dumps", "state_queues", "_DIR_IDENTITY.md", "daemons.pid", ".gitkeep"}

def log(msg):
    print(f"\033[96m[{DAEMON_NAME}]\033[0m {msg}")

def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except: pass

log("Initiating Deep Clean of vault/tmp (Targeting Stray Blobs)...")

total_mb_freed = 0
items_deleted = 0

for item in os.listdir(TMP_DIR):
    if item in PROTECTED_ITEMS:
        continue
        
    path = os.path.join(TMP_DIR, item)
    sz = 0
    try:
        if os.path.isdir(path):
            # Calculate size before smash
            for r, _, fs in os.walk(path):
                for f in fs:
                    try: sz += os.path.getsize(os.path.join(r, f))
                    except: pass
            
            shutil.rmtree(path, onerror=remove_readonly)
        else:
            sz = os.path.getsize(path)
            os.remove(path)
            
        mb = sz / (1024 * 1024)
        total_mb_freed += mb
        items_deleted += 1
        log(f"Vaporized: {item} ({mb:.2f} MB)")
    except Exception as e:
        log(f"Failed to vaporize {item}: {e}")

log(f"DEEP CLEAN COMPLETE.")
log(f"Smashed {items_deleted} stray items.")
log(f"Recovered {total_mb_freed:.2f} MB ({(total_mb_freed/1024):.2f} GB) from vault/tmp root!")
