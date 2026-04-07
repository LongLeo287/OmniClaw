import os, shutil, stat
import time

DAEMON_NAME = "OA [Endgame Executioner]"
DEAD_LETTERS = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\archives\dead_letters")

def log(msg):
    print(f"\033[91m[{DAEMON_NAME}]\033[0m {msg}")

def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except: pass

def get_dir_size(path):
    sz = 0
    try:
        for r, _, fs in os.walk(path):
            for f in fs:
                try: sz += os.path.getsize(os.path.join(r, f))
                except: pass
    except: pass
    return sz

log("OA Standing By. Authorizing absolute vaporization of all Dead Letters.")

if not os.path.exists(DEAD_LETTERS):
    log("Dead letters completely empty. Nothing to execute.")
else:
    items = os.listdir(DEAD_LETTERS)
    log(f"Detected {len(items)} condemned Ghost Repositories awaiting execution.")
    
    total_vaporized_mb = 0
    executed_count = 0
    
    for item in items:
        target_path = os.path.join(DEAD_LETTERS, item)
        if os.path.isdir(target_path):
            sz = get_dir_size(target_path)
            mb = sz / (1024 * 1024)
            try:
                shutil.rmtree(target_path, onerror=remove_readonly)
                total_vaporized_mb += mb
                executed_count += 1
                if executed_count % 500 == 0:
                    log(f"Progress: Vaporized {executed_count} Ghost Repos. Recovered {total_vaporized_mb:.2f} MB so far...")
            except Exception as e:
                pass
                
    log(f"FINAL VERDICT COMPLETE. Successfully EXECUTED {executed_count} Ghost Repositories.")
    log(f"TOTAL SPACE RECOVERED: {total_vaporized_mb:.2f} MB ({(total_vaporized_mb/1024):.2f} GB) from Dead Letters.")
