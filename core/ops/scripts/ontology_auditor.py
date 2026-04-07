import os
import shutil
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
KNOWLEDGE_DIR = os.path.join(ROOT, "brain", "knowledge")

def print_log(action, target):
    print(f"[OMA-SRE] {action.ljust(15)} | {target}")

def merge_duplicate_domains():
    if not os.path.exists(KNOWLEDGE_DIR): return
    
    # We look for folders having a hypocrite hyphen where an underscore exists, or vice-versa
    # Preferably, we standardize to underscore `_`
    dirs = [d for d in os.listdir(KNOWLEDGE_DIR) if os.path.isdir(os.path.join(KNOWLEDGE_DIR, d))]
    
    for d in dirs:
        if "-" in d:
            underscore_version = d.replace("-", "_")
            if underscore_version in dirs:
                # Merge logic
                hyphen_path = os.path.join(KNOWLEDGE_DIR, d)
                under_path = os.path.join(KNOWLEDGE_DIR, underscore_version)
                
                print_log("MERGING", f"{d} -> {underscore_version}")
                for item in os.listdir(hyphen_path):
                    src = os.path.join(hyphen_path, item)
                    dst = os.path.join(under_path, item)
                    if not os.path.exists(dst):
                        shutil.move(src, dst)
                    else:
                        # Conflict, just forcefully remove src if it's identical or let it be
                        if os.path.isfile(src): os.remove(src)
                
                # Delete old dir if empty
                if not os.listdir(hyphen_path):
                    os.rmdir(hyphen_path)
                    print_log("DELETED", f"Empty legacy domain '{d}'")

def prune_ki_duplicates():
    if not os.path.exists(KNOWLEDGE_DIR): return
    files = [f for f in os.listdir(KNOWLEDGE_DIR) if os.path.isfile(os.path.join(KNOWLEDGE_DIR, f)) and f.startswith("KI_")]
    
    # Regex to match the timestamp ending
    # e.g., KI_authentik_knowledge_20260405_032142.md
    pattern = re.compile(r"^(KI_.*)_knowledge_(\d{8}_\d{6}(?:_\d+)*)\.md$")
    
    groups = {}
    for f in files:
        match = pattern.match(f)
        if match:
            prefix = match.group(1)
            if prefix not in groups:
                groups[prefix] = []
            groups[prefix].append(f)
            
    for prefix, filelist in groups.items():
        if len(filelist) > 1:
            # Sort chronologically. 
            filelist.sort() # alphabetical works because timestamp format is numeric
            latest = filelist[-1]
            outdated = filelist[:-1]
            
            for old_f in outdated:
                os.remove(os.path.join(KNOWLEDGE_DIR, old_f))
                print_log("PRUNED", f"Outdated KI version: {old_f}")

def clean_empty_directories():
    for dirpath, dirnames, filenames in os.walk(KNOWLEDGE_DIR, topdown=False):
        if dirpath == KNOWLEDGE_DIR: continue
        
        # Truly empty check (ignore _DIR_IDENTITY and .gitkeep and .git)
        visible_items = [f for f in os.listdir(dirpath) if f not in ("_DIR_IDENTITY.md", ".gitkeep") and not f.startswith(".git")]
        
        if not visible_items:
            shutil.rmtree(dirpath)
            print_log("PURGED", f"Empty folder: {os.path.basename(dirpath)}")

def enforce_identity_tagging():
    EXCLUDES = ["vault", "tmp", ".git", "node_modules", "quarantine", "archives"]
    total_tags = 0
    for target in [KNOWLEDGE_DIR, os.path.join(ROOT, "ecosystem")]:
        if not os.path.exists(target): continue
        for dirpath, dirnames, filenames in os.walk(target):
            dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in EXCLUDES]
            
            id_file = os.path.join(dirpath, "_DIR_IDENTITY.md")
            if os.path.exists(id_file): continue
            
            # Don't tag empty folders we literally just cleaned
            visible = [f for f in os.listdir(dirpath) if f not in ("_template_placeholder.md", "_DIR_IDENTITY.md", ".gitkeep") and not f.startswith(".")]
            if not visible: continue
            
            dir_name = os.path.basename(dirpath)
            rel_path = os.path.relpath(dirpath, ROOT).replace("\\", "/")
            
            content = f"---\nid: {rel_path.replace('/', '-').replace(' ', '_')}\nname: {dir_name.replace('_', ' ').title()}\npath: {rel_path}\ntype: directory_identity\nowner: OER\ncreated_by: OMA-v2.1\n---\n\n# {dir_name.replace('_', ' ').title()}\nStorage area for '{dir_name}' domain.\n> Auto-generated identity tag by OMA v2.1.\n"
            
            with open(id_file, "w", encoding="utf-8") as f:
                f.write(content)
            print_log("TAGGED", f"{rel_path}")
            total_tags += 1
            
    if total_tags > 0:
        print(f"✅ Injected {total_tags} new missing Ontology tags.")

def quarantine_misplaced_folders():
    quarantine_base = os.path.join(ROOT, "vault", "quarantine", "auditor_sweeps")
    os.makedirs(quarantine_base, exist_ok=True)
    
    dirs = [d for d in os.listdir(KNOWLEDGE_DIR) if os.path.isdir(os.path.join(KNOWLEDGE_DIR, d))]
    
    for d in dirs:
        # Condition 1: repo_fetched or repo_duplicates shouldn't be long-term stored here
        # Condition 2: forbidden nested names
        if d.startswith("repo_fetched_") or d.startswith("repo_duplicates_") or d in ["skills", "knowledge", "lightrag_db"]:
            src = os.path.join(KNOWLEDGE_DIR, d)
            dst = os.path.join(quarantine_base, d)
            
            # Anti-collision for quarantine
            if os.path.exists(dst):
                dst = dst + "_dup"
                
            shutil.move(src, dst)
            print_log("QUARANTINE", f"Misplaced folder '{d}' moved to vault/quarantine")

def run_auditor():
    print("=" * 60)
    print(" SRE ONTOLOGY AUDITOR - COMMENCING CLEANSING PROTOCOL")
    print("=" * 60)
    
    merge_duplicate_domains()
    prune_ki_duplicates()
    quarantine_misplaced_folders()
    clean_empty_directories()
    enforce_identity_tagging()
    
    print("=" * 60)
    print(" AUDIT SEQUENCE COMPLETE. REPOSITORY IS HEALTHY.")
    print("=" * 60)

if __name__ == "__main__":
    run_auditor()
