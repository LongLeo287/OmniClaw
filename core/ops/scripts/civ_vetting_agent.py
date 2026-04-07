import os
import shutil
from datetime import datetime

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
CIV_DIR = os.path.join(ROOT, "brain", "knowledge", "CIV")
RAW_DUMPS = os.path.join(ROOT, "vault", "tmp", "raw_knowledge_dumps")

def evaluate_repo(path):
    """
    Returns (is_good, reason)
    """
    try:
        files = os.listdir(path)
        if len(files) == 0:
            return False, "Empty directory"
            
        # Check size heuristic
        total_size = 0
        file_count = 0
        has_readme = False
        has_code = False
        
        for root, dirs, fnames in os.walk(path):
            if '.git' in root or '__pycache__' in root or 'node_modules' in root:
                continue
            for f in fnames:
                file_count += 1
                if f.lower() in ["readme.md", "readme.txt", "readme"]:
                    has_readme = True
                if f.endswith(('.py', '.js', '.ts', '.html', '.md', '.go', '.json')):
                    has_code = True
                fpath = os.path.join(root, f)
                try:
                    total_size += os.path.getsize(fpath)
                except:
                    pass
                    
        if total_size < 1024: # Less than 1KB
            return False, "Extremely small size (<1KB)"
            
        if not has_code and not has_readme:
            return False, "No code or README found"
            
        return True, f"{file_count} files, {total_size//1024} KB"
        
    except Exception as e:
        return False, f"Read error: {e}"

def clean_civ():
    print("\033[94m[INFO]\033[0m Initiating CIV In-Place Vetting Protocol...")
    if not os.path.exists(CIV_DIR):
        print("CIV directory not found.")
        return
        
    os.makedirs(RAW_DUMPS, exist_ok=True)
    
    kept = 0
    demoted = 0
    
    for cand in os.listdir(CIV_DIR):
        cand_path = os.path.join(CIV_DIR, cand)
        if not os.path.isdir(cand_path):
            continue
            
        if "FETCHED_" in cand:
            is_good, reason = evaluate_repo(cand_path)
            if is_good:
                # Approve
                new_name = cand.replace("FETCHED_", "").replace("fetched_", "").strip("_")
                new_path = os.path.join(CIV_DIR, new_name)
                
                # Check target exists
                if os.path.exists(new_path) and new_path != cand_path:
                    new_path = new_path + "_0" # resolve collision
                    new_name = new_name + "_0"
                    
                # Move/Rename IN PLACE
                os.rename(cand_path, new_path)
                
                # Stamp Identity
                ts = datetime.now().isoformat()
                id_file = os.path.join(new_path, "_DIR_IDENTITY.md")
                content = f"---\nid: {new_name}\ntype: knowledge_domain\nowner: OA\nregistered_at: {ts}\ntags: [civ-auto-approved]\n---\n# {new_name}\nAssimilated automatically by CIV Vetting Agent based on structural integrity.\n"
                with open(id_file, "w", encoding="utf-8") as f:
                    f.write(content)
                    
                print(f"\033[92m[✓ APPROVED]\033[0m {new_name} ({reason})")
                kept += 1
            else:
                # Reject
                dest_path = os.path.join(RAW_DUMPS, cand)
                try:
                    shutil.move(cand_path, dest_path)
                    print(f"\033[93m[✗ DEMOTED ]\033[0m {cand} -> Rác ({reason})")
                    demoted += 1
                except Exception as e:
                    print(f"\033[91m[ERR]\033[0m Cannot move {cand}: {e}")

    print(f"\n\033[92m[DONE]\033[0m Vetting Complete! Kept \033[96m{kept}\033[0m Repos in CIV. Demoted \033[93m{demoted}\033[0m to RAW_DUMPS.")

if __name__ == "__main__":
    clean_civ()
