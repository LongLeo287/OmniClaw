import os, shutil, subprocess, stat

DAEMON_NAME = "OA [Auditor Sweep Judge]"
TARGET = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\quarantine\auditor_sweeps")
OER_INBOX = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\state_queues\OER_INBOX")
EMPTY_DIR = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\empty_smasher")

VALID_EXTENSIONS = {".py", ".js", ".ts", ".go", ".rs", ".java", ".c", ".cpp", ".cs", ".php", ".html", ".css", ".md", ".json", ".yaml"}

def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except: pass

def robocopy_purge(target_dir):
    if not os.path.exists(EMPTY_DIR): os.makedirs(EMPTY_DIR)
    subprocess.run(f'robocopy "{EMPTY_DIR}" "{target_dir}" /PURGE /E /R:0 /W:0', shell=True, capture_output=True)
    try: os.rmdir(target_dir)
    except: pass

def get_dir_size_and_count(path):
    sz = 0
    file_count = 0
    try:
        for r, d, fs in os.walk(path):
            d[:] = [x for x in d if x not in ('.git', 'node_modules', '__pycache__')]
            for f in fs:
                ext = os.path.splitext(f)[1].lower()
                if ext in VALID_EXTENSIONS:
                    try:
                        sz += os.path.getsize(os.path.join(r, f))
                        file_count += 1
                    except: pass
    except: pass
    return sz, file_count

print(f"\033[95m[{DAEMON_NAME}]\033[0m Court in Session. Analyzing {TARGET}...")

items = []
try: items = os.listdir(TARGET)
except: pass

survivors = 0
ghosts = 0

for item in items:
    path = os.path.join(TARGET, item)
    if not os.path.exists(path): continue
        
    is_valid_candidate = False
    
    if os.path.isdir(path):
        code_mass, code_count = get_dir_size_and_count(path)
        if code_count > 0 and code_mass > 1024:
            is_valid_candidate = True
        
        if is_valid_candidate:
            dest = os.path.join(OER_INBOX, item)
            try:
                shutil.move(path, dest)
                survivors += 1
                print(f"\033[92m[VERDICT: SURVIVED]\033[0m Handing over {item} ({code_mass/1024:.1f} KB) to INBOX for Distillation.")
            except Exception as e:
                # If move fails (already exists), we purge it to avoid conflict.
                print(f"\033[93m[COLLISION]\033[0m {item} already in INBOX. Purging duplicate.")
                robocopy_purge(path)
                ghosts += 1
        else:
            robocopy_purge(path)
            ghosts += 1
            print(f"\033[91m[VERDICT: CONDEMNED]\033[0m Vaporized Ghost Repo/Folder: {item}")
    else:
        # Lone files in sweeps
        if path.endswith(".md") and os.path.getsize(path) > 100:
            dest = os.path.join(OER_INBOX, item)
            shutil.move(path, dest)
            survivors += 1
        else:
            os.remove(path)
            ghosts += 1

if os.path.exists(EMPTY_DIR): os.rmdir(EMPTY_DIR)
print(f"\n\033[95m[{DAEMON_NAME}]\033[0m COURT ADJOURNED.")
print(f"Total Ghost/Empty Elements ERADICATED: {ghosts}")
print(f"Total Valid Rescued Apps: {survivors}")
