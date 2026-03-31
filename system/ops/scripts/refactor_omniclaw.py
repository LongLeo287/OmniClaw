import os
import re
import shutil
from pathlib import Path

ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))
REMOTE_DIR = Path('d:/LongLeo/AI OS CORP/AI OS REMOTE')
REMOTE_SERVICES = REMOTE_DIR / 'services'

os.makedirs(REMOTE_SERVICES, exist_ok=True)

# File patterns to process
exts = ['.py', '.ps1', '.cmd', '.bat', '.md', '.json', '.yaml', '.yml']

# Specific replacement mapping (Order matters: longest match first)
REPLACEMENTS = [
    (re.compile(r'AI OS CORP', re.IGNORECASE), 'OmniClaw Corp'),
    (re.compile(r'AI OS Auto-Merge Secret', re.IGNORECASE), 'OmniClaw Auto-Merge Secret'),
    (re.compile(r'AI OS Auto-Test & Lint', re.IGNORECASE), 'OmniClaw Auto-Test & Lint'),
    (re.compile(r'AI OS Auto-Merge', re.IGNORECASE), 'OmniClaw Auto-Merge'),
    (re.compile(r'AI OS Auto-Test', re.IGNORECASE), 'OmniClaw Auto-Test'),
    (re.compile(r'\bAI OS\b', re.IGNORECASE), 'OmniClaw'),
    (re.compile(r'\bAI_OS\b', re.IGNORECASE), 'OMNICLAW'),
    (re.compile(r'\baios\b', re.IGNORECASE), 'omniclaw'),
    (re.compile(r'\baos\b', re.IGNORECASE), 'omniclaw'),
]

# Specifically exclude some massive directories or raw datasets
EXCLUDES = ['\\.git\\', '\\.claude\\worktrees\\', '\\brain\\knowledge\\repos\\', '\\node_modules\\', '\\__pycache__\\']

print("Starting Global Rename & Refactor...")

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        original = content
        for pattern, replacement in REPLACEMENTS:
            content = pattern.sub(replacement, content)
            
        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False
    except Exception as e:
        # Ignore binary or undecodable files
        return False

# 1. TEXT REPLACEMENTS
changed_files = 0
for root, dirs, files in os.walk(str(ROOT)):
    if any(ex in root for ex in EXCLUDES):
        continue
        
    for file in files:
        if any(file.endswith(ext) for ext in exts):
            file_path = os.path.join(root, file)
            # Extra check to ensure we don't refactor this exact script while it is running
            if 'refactor_omniclaw.py' in file_path:
                continue
            if process_file(file_path):
                print(f"[REFACTORED] {file_path}")
                changed_files += 1

print(f"Total files updated: {changed_files}")

# 2. GITHUB ACTIONS RENAME
gh_dir = ROOT / ".github" / "workflows"
if gh_dir.exists():
    for f in gh_dir.glob("*.yml"):
        if f.name.startswith("ai-os-"):
            new_name = f.name.replace("ai-os-", "omniclaw-")
            new_path = gh_dir / new_name
            shutil.move(str(f), str(new_path))
            print(f"[RENAMED] {f.name} -> {new_name}")

# 3. MIGRATE DISCONNECTED SERVICES
services_to_migrate = [
    "anything_llm", "flowise", "lobehub", "n8n", "open-notebook", 
    "open-notebooklm", "notebooklm-mcp", "llamafactory"
]

plugins_dir = ROOT / "ecosystem" / "plugins"

for srv in services_to_migrate:
    src = plugins_dir / srv
    if src.exists() and src.is_dir():
        dst = REMOTE_SERVICES / srv
        if dst.exists():
            shutil.rmtree(str(dst))
        shutil.move(str(src), str(dst))
        print(f"[MIGRATED] Plugin '{srv}' moved to AI OS REMOTE/services/")
