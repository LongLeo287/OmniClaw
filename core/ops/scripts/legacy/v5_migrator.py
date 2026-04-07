import os
import re
import shutil

AIOS_ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# 1. Physical Directory Moves
def create_dir(path):
    os.makedirs(os.path.join(AIOS_ROOT, path), exist_ok=True)

def move_content(src, dest):
    src_path = os.path.join(AIOS_ROOT, src)
    dest_path = os.path.join(AIOS_ROOT, dest)
    if os.path.exists(src_path):
        for item in os.listdir(src_path):
            s = os.path.join(src_path, item)
            d = os.path.join(dest_path, item)
            try:
                shutil.move(s, d)
            except Exception as e:
                print(f"Failed to move {s} to {d}: {e}")

print("--- PHASE 1: DIRECTORY CONSOLIDATION ---")
create_dir("vault")
create_dir("vault/assets")
create_dir("vault/archives")
create_dir("vault/tmp")
create_dir("brain/knowledge/docs_legacy")

# Migrate asset -> vault/assets
move_content("asset", "vault/assets")
# Migrate storage -> vault
move_content("storage", "vault")
# Migrate backups -> vault/archives
move_content("backups", "vault/archives")
# Migrate tmp -> vault/tmp 
move_content("tmp", "vault/tmp")
# Migrate docs -> brain/knowledge/docs_legacy
move_content("docs", "brain/knowledge/docs_legacy")

# Rename system -> core
sys_path = os.path.join(AIOS_ROOT, "system")
core_path = os.path.join(AIOS_ROOT, "core")
if os.path.exists(sys_path):
    os.rename(sys_path, core_path)
    print("Renamed core/ to core/")

# Cleanup old empty dirs
for d in ["asset", "storage", "backups", "tmp", "docs"]:
    p = os.path.join(AIOS_ROOT, d)
    if os.path.exists(p) and not os.listdir(p):
        os.rmdir(p)
        print(f"Removed empty dir: {d}")

print("--- PHASE 2: PATH CORRECTION IN FILES ---")
def replace_in_files():
    target_extensions = {".py", ".json", ".md", ".yaml", ".ps1", ".sh", ".env", ".example"}
    exclude_dirs = {".git", ".claude", "node_modules", "vault"}
    
    replacements = [
        # Path replacements
        (re.compile(r'\bsystem/'), r'core/'),
        (re.compile(r'\bsystem\\'), r'core\\'),
        (re.compile(r'\basset/'), r'vault/assets/'),
        (re.compile(r'\basset\\'), r'vault\\assets\\'),
        (re.compile(r'\bstorage/'), r'vault/'),
        (re.compile(r'\bstorage\\'), r'vault\\'),
        (re.compile(r'\bdocs/'), r'brain/knowledge/docs_legacy/'),
        (re.compile(r'\bdocs\\'), r'brain\\knowledge\\docs_legacy\\'),
        # Python import replacements (system.XXX -> core.XXX)
        (re.compile(r'from core\.'), r'from core.'),
        (re.compile(r'import core\.'), r'import core.'),
    ]
    
    files_changed = 0
    for root, dirs, files in os.walk(AIOS_ROOT):
        # Exclude hidden and ignored directories
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in exclude_dirs]
        
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in target_extensions:
                fpath = os.path.join(root, file)
                try:
                    with open(fpath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    new_content = content
                    for pattern, repl in replacements:
                        new_content = pattern.sub(repl, new_content)
                        
                    if new_content != content:
                        with open(fpath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        files_changed += 1
                except Exception as e:
                    pass
    print(f"Updated paths in {files_changed} files.")

replace_in_files()
print("Migration script completed!")
