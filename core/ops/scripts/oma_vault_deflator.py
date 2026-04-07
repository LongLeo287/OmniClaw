import os, shutil, stat

DAEMON_NAME = "OMA [Vault Deflator]"
RAW_DUMPS = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\raw_knowledge_dumps")
BANNED_DIRS = {".git", "node_modules", "__pycache__", "venv", ".venv", "dist", ".next", "build", ".idea", ".vscode"}

def log(msg):
    print(f"\033[96m[{DAEMON_NAME}]\033[0m {msg}")

def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except: pass

log(f"Commencing aggressive structural volume purge on 5400+ raw repositories...")

PurgeCount = 0

for root, dirs, files in os.walk(RAW_DUMPS, topdown=True):
    # Iterate copy to safely remove items from dirs to prevent traversing them
    for d in list(dirs):
        if d in BANNED_DIRS:
            target = os.path.join(root, d)
            try:
                # Fast tree deletion
                shutil.rmtree(target, ignore_errors=True)
                PurgeCount += 1
                if PurgeCount % 500 == 0:
                    log(f"Progress: Purged {PurgeCount} forbidden nodes...")
            except: pass
            
            # CRITICAL: Prevent os.walk from entering the banned dir which wastes enormous time
            dirs.remove(d)

log(f"DEFLATION COMPLETE: Purged {PurgeCount} garbage nodes.")
