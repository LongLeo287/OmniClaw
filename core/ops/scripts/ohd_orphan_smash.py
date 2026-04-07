import os, shutil, stat

DAEMON_NAME = "OHD [Orphan Smasher]"
QUARANTINE = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\quarantine")

def log(msg):
    print(f"\033[93m[{DAEMON_NAME}]\033[0m {msg}")

def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except: pass

log("OHD Standing By. Fast Eradication Protocol Engaged.")

if not os.path.exists(QUARANTINE):
    log("Quarantine completely empty. Nothing to smash.")
else:
    items = os.listdir(QUARANTINE)
    executed_count = 0
    
    for item in items:
        target_path = os.path.join(QUARANTINE, item)
        log(f"Vaporizing Quarantine Blob: {item}...")
        try:
            if os.path.isdir(target_path):
                shutil.rmtree(target_path, onerror=remove_readonly)
            else:
                os.remove(target_path)
            executed_count += 1
        except Exception as e:
            pass
                
    log(f"ORPHAN SMASH COMPLETE. Smashed {executed_count} Quarantine Items.")
    log(f"Quarantine region is now a barren wasteland.")
