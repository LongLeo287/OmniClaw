import os
import shutil
import stat
from typing import List

DAEMON_NAME = "OA [Swallow Engine]"
TARGET_DOMAINS = [
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "brain\knowledge"),
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "ecosystem\skills"),
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\state_queues\OER_INBOX"),
    os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "vault\tmp\state_queues\OA_DISPATCH_QUEUE")
]
PRIORITY_FILES = ["README.md", "readme.md", "README.txt", "package.json", "setup.py", "main.py", "index.js", "requirements.txt"]
VALID_CODE_EXTS = {".py", ".js", ".ts", ".go", ".rs", ".java", ".c", ".cpp", ".cs", ".php", ".html", ".css", ".md", ".json", ".yaml", ".txt", ".sh", ".ps1"}
MAX_CHARS = 50000

def log(msg):
    print(f"\033[92m[{DAEMON_NAME}]\033[0m {msg}")

def remove_readonly(func, path, _):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except: pass

def check_is_valid_repo_root(path: str) -> str:
    """Returns the identity content if this folder is a valid repo root to be swallowed."""
    id_file = os.path.join(path, "_DIR_IDENTITY.md")
    if not os.path.exists(id_file): return ""
    try:
        with open(id_file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
            if "type: directory_identity" in content.lower():
                return "" # Root pillar, do not swallow!
            if "type: knowledge" in content.lower() or "owner: oa_triage" in content.lower() or "type: api" in content.lower():
                return content
    except: pass
    return ""

def distill_folder(repo_path: str, repo_name: str, identity_content: str) -> bool:
    """Returns True if distillation was successful"""
    all_files = []
    
    for r, dirs, files in os.walk(repo_path):
        # Ignore junk
        dirs[:] = [d for d in dirs if d not in ['.git', 'node_modules', '__pycache__', 'venv', 'dist', '.next']]
        for f in files:
            ext = os.path.splitext(f)[1].lower()
            fp = os.path.join(r, f)
            if f != "_DIR_IDENTITY.md" and (f.lower() in [pf.lower() for pf in PRIORITY_FILES] or ext in VALID_CODE_EXTS):
                all_files.append((fp, f, ext))

    # 2. Extract content
    compiled_text = []
    
    if identity_content:
        compiled_text.append(identity_content.strip() + "\n\n")
    else:
        compiled_text.append(f"---\nid: {repo_name}\ntype: distilled_knowledge\n---\n# {repo_name}\n\n")
        
    compiled_text.append("## SWALLOW ENGINE DISTILLATION\n\n")
    
    total_chars = 0
    # Prioritize root files and specific names
    all_files.sort(key=lambda x: (0 if x[1].lower() in [pf.lower() for pf in PRIORITY_FILES] else 1, x[0].count(os.sep)))
    
    for fp, fname, ext in all_files:
        if total_chars > MAX_CHARS:
            compiled_text.append(f"\n\n> [!WARNING]\n> Distillation threshold ({MAX_CHARS} chars) reached. Truncating further files.\n")
            break
            
        try:
            sz = os.path.getsize(fp)
            if sz > 200 * 1024: continue # Skip single files > 200KB to save memory
            
            with open(fp, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read()
            
            # Extract relative path
            rel_path = os.path.relpath(fp, repo_path)
            content_len = len(content)
            if content_len > 15000:
                content = content[:15000] + "\n... [TRUNCATED]"
                content_len = len(content)
                
            compiled_text.append(f"### File: {rel_path}\n```{ext[1:] if ext else 'text'}\n{content}\n```\n\n")
            total_chars += content_len
        except Exception: pass

    # 3. Write core knowledge out OUTSIDE the folder
    final_output = "".join(compiled_text)
    out_name = f"{repo_name.replace('FETCHED_', '').replace('-master','').replace('-main','')}_DISTILLED.md"
    parent_dir = os.path.dirname(repo_path)
    out_path = os.path.join(parent_dir, out_name)
    
    try:
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(final_output)
    except Exception as e:
        log(f"Failed writing {out_path}: {e}")
        return False
        
    return True

if __name__ == "__main__":
    import sys
    test_mode = "--test" in sys.argv
    swallowed = 0
    failed = 0
    
    for domain in TARGET_DOMAINS:
        if not os.path.exists(domain): continue
            
        # Top-down walk so we can prune subdirectories if we process a repo
        for root, dirs, files in os.walk(domain, topdown=True):
            to_remove = []
            for d in dirs:
                target_path = os.path.join(root, d)
                # Ensure we only check identity if it's not a banned dir
                if any(x in target_path for x in ['__pycache__', '.git', 'node_modules']): continue
                
                identity = check_is_valid_repo_root(target_path)
                if identity:
                    # Target Locked!
                    success = distill_folder(target_path, d, identity)
                    if success:
                        log(f"Swallowed: {d}")
                        if not test_mode:
                            try:
                                shutil.rmtree(target_path, onerror=remove_readonly)
                                swallowed += 1
                                to_remove.append(d) # Prevent os.walk from entering the now-deleted directory
                            except Exception as e:
                                log(f"Error vaporizing {target_path}: {e}")
                                failed += 1
                        else:
                            log(f"[TEST RUN] Would vaporize: {target_path}")
                            swallowed += 1
                            to_remove.append(d)
                            
            for p in to_remove:
                if p in dirs: dirs.remove(p)

    log(f"MISSION COMPLETE.")
    log(f"Total Repositories Swallowed & Vaporized: {swallowed}")
    if failed > 0:
        log(f"Failed to vaporize: {failed} items.")
