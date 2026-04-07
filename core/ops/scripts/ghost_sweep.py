import os
import shutil

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
QUARANTINE_DIR = os.path.join(ROOT, 'vault', 'tmp', 'quarantine', 'GHOST_SWEEP')

def run_ghost_sweep():
    print(f"\033[94m[INFO]\033[0m Starting GHOST SWEEP Protocol...")
    os.makedirs(os.path.join(QUARANTINE_DIR, 'empty_files'), exist_ok=True)
    os.makedirs(os.path.join(QUARANTINE_DIR, 'empty_folders'), exist_ok=True)
    
    sweep_files = 0
    sweep_dirs = 0

    # Phase A: Sweep empty/trash files
    for base in ['brain', 'ecosystem']:
        base_path = os.path.join(ROOT, base)
        if not os.path.exists(base_path): continue
        
        for root, dirs, files in os.walk(base_path):
            for f in files:
                if f.endswith('.md'):
                    fpath = os.path.join(root, f)
                    try:
                        size = os.path.getsize(fpath)
                        # Less than 40 bytes usually means it's totally empty or just has a `# Title`
                        if size < 40 and not f.startswith("---"):
                            # But wait, what if it's EXACTLY frontmatter? Frontmatter alone is useless.
                            # Just sweep anything tiny.
                            sweep_files += 1
                            dest = os.path.join(QUARANTINE_DIR, 'empty_files', f"{sweep_files}_{f}")
                            shutil.move(fpath, dest)
                            print(f"  \033[93m[SWEEP]\033[0m Trashed empty file: {os.path.relpath(fpath, ROOT)}")
                    except Exception as e:
                        pass
                        
    # Phase B: Sweep empty directories (Bottom-Up to catch nested empties)
    for base in ['brain', 'ecosystem']:
        base_path = os.path.join(ROOT, base)
        if not os.path.exists(base_path): continue
        
        for root, dirs, files in os.walk(base_path, topdown=False):
            # Skip the root pillar dirs
            if root == base_path: continue
            
            # What defines "empty"?
            # If all it has is _DIR_IDENTITY.md (and no other actual subdirs or code files)
            # Or if it has strictly hidden files.
            visible_content = []
            for item in os.listdir(root):
                if item.startswith('.') or item == "__pycache__": continue
                visible_content.append(item)
                
            if len(visible_content) == 0 or (len(visible_content) == 1 and visible_content[0] == "_DIR_IDENTITY.md"):
                # Total Ghost Folder!
                try:
                    sweep_dirs += 1
                    dirname = os.path.basename(root)
                    dest = os.path.join(QUARANTINE_DIR, 'empty_folders', f"{sweep_dirs}_{dirname}")
                    shutil.move(root, dest)
                    print(f"  \033[93m[SWEEP]\033[0m Trashed Ghost directory: {os.path.relpath(root, ROOT)}")
                except: pass

    print(f"\033[92m[DONE]\033[0m Ghost Sweep complete. Cleared {sweep_files} hollow files and {sweep_dirs} ghost structures.")

if __name__ == "__main__":
    run_ghost_sweep()
