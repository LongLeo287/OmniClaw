import os, shutil, hashlib, subprocess, stat

DAEMON_NAME = "OA [Heuristic Analyser]"

OMNICLAW_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
INBOX = os.path.join(OMNICLAW_ROOT, "vault", "tmp", "state_queues", "OER_INBOX")
EMPTY_DIR = os.path.join(OMNICLAW_ROOT, "vault", "tmp", "empty_smasher")

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

def hash_directory_structure(path):
    # Calculates a hash based on file names and sizes (ignoring modification times)
    # This prevents duplicate repos with slightly different names from passing.
    hasher = hashlib.md5()
    file_list = []
    
    for r, d, fs in os.walk(path):
        d[:] = [x for x in d if x not in ('.git', 'node_modules', '__pycache__')]
        for f in fs:
            try:
                f_path = os.path.join(r, f)
                sz = os.path.getsize(f_path)
                rel = os.path.relpath(f_path, path)
                file_list.append(f"{rel}:{sz}")
            except: pass
            
    file_list.sort() # Ensure deterministic order
    for s in file_list:
        hasher.update(s.encode('utf-8'))
        
    return hasher.hexdigest(), file_list

print(f"\033[96m[{DAEMON_NAME}]\033[0m Initiating Deep Triage on OER_INBOX...")

try: items = os.listdir(INBOX)
except: items = []

hashes_seen = {}
ghosts = 0
retained = 0
data_heavy = 0

for item in items:
    path = os.path.join(INBOX, item)
    if not os.path.exists(path) or not os.path.isdir(path): continue
        
    dir_hash, file_list = hash_directory_structure(path)
    
    # 1. Deduplication Check
    if dir_hash in hashes_seen:
        original = hashes_seen[dir_hash]
        print(f"\033[93m[DUPLICATE]\033[0m {item} is an EXACT clone of {original}. Vaporizing clone.")
        robocopy_purge(path)
        ghosts += 1
        continue
        
    # 2. Heuristic Semantic Classification (Basic)
    is_tooling = any("langchain" in f.lower() or "claude" in f.lower() for f in file_list)
    has_large_data = any(f.endswith(".csv") for f in file_list) and len(file_list) < 5
    
    if len(file_list) == 0:
        print(f"\033[91m[LÕI RỖNG]\033[0m {item} is structurally empty. Vaporizing.")
        robocopy_purge(path)
        ghosts += 1
        continue
        
    if has_large_data:
        print(f"\033[91m[DATA DUMPS]\033[0m {item} is mostly raw data drops, not logic. Purging to save brain mass.")
        robocopy_purge(path)
        data_heavy += 1
        continue
        
    # If Valid, record signature
    hashes_seen[dir_hash] = item
    
    domain_tag = "AI/Tooling" if is_tooling else "Algorithm/App"
    print(f"\033[92m[PRIME CORE]\033[0m {item} | Tag: [{domain_tag}] | Validated for Distillation.")
    retained += 1
    
    # Stamp it with _DIR_IDENTITY for OER logic compliance if missing
    id_path = os.path.join(path, "_DIR_IDENTITY.md")
    if not os.path.exists(id_path):
        with open(id_path, "w", encoding="utf-8") as f:
            f.write(f"---\nname: {item}\ntype: knowledge_repo\ndomain: {domain_tag}\n---\n")

if os.path.exists(EMPTY_DIR): os.rmdir(EMPTY_DIR)
print(f"\n\033[96m[{DAEMON_NAME}]\033[0m Triage Complete.")
print(f"Clones/Ghosts Cleansed: {ghosts}")
print(f"Data Dumps Cleansed: {data_heavy}")
print(f"Final Prime Repos ready for Swallow Engine: {retained}")
