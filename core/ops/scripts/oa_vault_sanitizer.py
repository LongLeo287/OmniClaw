import os, shutil

DAEMON_NAME = "OA [Supreme Triage]"
ROOT_DIR = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RAW_DUMPS = os.path.join(ROOT_DIR, "vault", "tmp", "raw_knowledge_dumps")
DEAD_LETTERS = os.path.join(ROOT_DIR, "vault", "archives", "dead_letters")
OER_INBOX = os.path.join(ROOT_DIR, "vault", "tmp", "state_queues", "OER_INBOX")

VALID_EXTENSIONS = {".py", ".js", ".ts", ".go", ".rs", ".java", ".c", ".cpp", ".cs", ".php", ".html", ".css", ".md", ".json", ".yaml"}

def log(msg):
    print(f"\033[95m[{DAEMON_NAME}]\033[0m {msg}")

os.makedirs(DEAD_LETTERS, exist_ok=True)
os.makedirs(OER_INBOX, exist_ok=True)

log(f"Initiating Trial by Fire on 5400+ repositories in Vault...")

killed_ghosts = 0
approved_repos = 0

if os.path.exists(RAW_DUMPS):
    repos = os.listdir(RAW_DUMPS)
    for repo_name in repos:
        repo_path = os.path.join(RAW_DUMPS, repo_name)
        if not os.path.isdir(repo_path): continue
        
        # Deep Heuristic Appraisal
        file_count = 0
        valid_code_size = 0
        has_readme = False
        
        for root, _, files in os.walk(repo_path):
            for file in files:
                file_count += 1
                if file.lower() == "readme.md":
                    has_readme = True
                
                ext = os.path.splitext(file)[1].lower()
                if ext in VALID_EXTENSIONS:
                    try:
                        valid_code_size += os.path.getsize(os.path.join(root, file))
                    except: pass
                    
        # Judgment rules
        is_ghost = False
        reason = ""
        
        if file_count == 0:
            is_ghost = True; reason = "Completely Empty"
        elif valid_code_size < 1024:
            is_ghost = True; reason = "Virtual Phantom (No functional code mass)"
        
        if is_ghost:
            try:
                shutil.move(repo_path, os.path.join(DEAD_LETTERS, repo_name))
                killed_ghosts += 1
            except Exception as e: pass
        else:
            # Prepare Identity and Fast Track to OER
            id_path = os.path.join(repo_path, "_DIR_IDENTITY.md")
            if not os.path.exists(id_path):
                # Clean up the name
                skill_id = repo_name.replace("FETCHED_", "").split("_")[0]
                content = f"---\nid: {skill_id}\ntype: knowledge\nowner: OA_Triage\n---\n# {skill_id}\nRaw knowledge dump assimilated by OA.\n"
                with open(id_path, "w", encoding="utf-8") as f:
                    f.write(content)
            
            try:
                shutil.move(repo_path, os.path.join(OER_INBOX, repo_name))
                approved_repos += 1
            except: pass

log(f"TRIAGE COMPLETE. Exiled {killed_ghosts} ghost repos to Dead Letters.")
log(f"Approved and Fast-Tracked {approved_repos} valid repos to OER Inbox for immediate ecosystem registry.")
