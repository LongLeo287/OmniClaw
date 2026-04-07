import os, shutil, subprocess, stat

DAEMON_NAME = "OA [Final Judge]"
TARGET = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\state_queues\OA_FINAL_CHECK")
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
    os.rmdir(target_dir)

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

print(f"\033[95m[{DAEMON_NAME}]\033[0m Court in Session. Analyzing OA_FINAL_CHECK...")

items = []
try: items = os.listdir(TARGET)
except: pass

survivors = 0
ghosts = 0

for item in items:
    path = os.path.join(TARGET, item)
    if not os.path.exists(path): continue
        
    is_pathological = False
    if "OA_REJECTED_" in item and item.count("OA_REJECTED_") >= 2: is_pathological = True
    if "__pycache__" in item and item.count("__pycache__") >= 2: is_pathological = True
        
    is_valid_candidate = False
    
    if is_pathological:
        # Straight to vaporization via Robocopy Executioner
        print(f"\033[91m[PATHOLOGICAL ANOMALY]\033[0m Sentenced: {item[:40]}...")
        robocopy_purge(path)
        ghosts += 1
    else:
        if os.path.isdir(path):
            code_mass, code_count = get_dir_size_and_count(path)
            if code_count > 0 and code_mass > 1024:
                is_valid_candidate = True
        else:
            if path.endswith(".md") and os.path.getsize(path) > 100:
                is_valid_candidate = True
    
        if is_valid_candidate:
            dest = os.path.join(OER_INBOX, item)
            try:
                shutil.move(path, dest)
                survivors += 1
                print(f"\033[92m[VERDICT: SURVIVED]\033[0m Handing over {item} for Distillation.")
            except: pass
        else:
            try:
                if os.path.isdir(path): shutil.rmtree(path, onerror=remove_readonly)
                else: os.remove(path)
                ghosts += 1
                print(f"\033[93m[VERDICT: CONDEMNED]\033[0m Standard Vaporize: {item}")
            except: pass

if os.path.exists(EMPTY_DIR): os.rmdir(EMPTY_DIR)
print(f"\n\033[95m[{DAEMON_NAME}]\033[0m COURT ADJOURNED.")
print(f"Total Structural Anomalies ERADICATED: {ghosts}")
print(f"Total Valid Knowledge Rescued: {survivors}")
