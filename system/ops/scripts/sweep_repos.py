import os
import re
import json
from pathlib import Path
import sys

_AOS_ROOT = Path("d:/LongLeo/AI OS CORP/AI OS")
DATA_DIR = _AOS_ROOT / "storage" / "vault" / "DATA"
QUAR_DIR = _AOS_ROOT / "system" / "security" / "QUARANTINE"
PROCESSED_DIR = _AOS_ROOT / "brain" / "knowledge" / "processed_repos"
PROGRESS_FILE = QUAR_DIR / "logs" / ".pipeline_progress.json"

URL_PATTERN = re.compile(r'https://github\.com/[\w\-\.]+/[A-Za-z0-9_\-\.]+')

def gather_all_urls():
    urls = set()
    for directory in [DATA_DIR, QUAR_DIR]:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith(".txt") or file.endswith(".md") or file.endswith(".json"):
                    if "intake_log" in file or "progress" in file:
                        continue # Skip logs to avoid infinite loop
                    filepath = Path(root) / file
                    try:
                        content = filepath.read_text(encoding="utf-8", errors="ignore")
                        found = URL_PATTERN.findall(content)
                        for u in found:
                            urls.add(u.rstrip('/'))
                    except Exception:
                        pass
    
    # Also check the failed list in progress file
    try:
        if PROGRESS_FILE.exists():
            data = json.loads(PROGRESS_FILE.read_text())
            for u in data.get("failed", []):
                 urls.add(u.rstrip('/'))
    except Exception:
        pass
    
    return urls

def filter_unprocessed(urls):
    todo = []
    for u in urls:
        repo_name = u.split("/")[-1]
        knowledge_file = PROCESSED_DIR / f"{repo_name}_knowledge.md"
        if not knowledge_file.exists():
            todo.append(u)
    return todo

all_urls = gather_all_urls()
todo_urls = filter_unprocessed(all_urls)

# Save to a new master list so active pipeline can handle it
SWEEP_FILE = DATA_DIR / "SWEEP_MASTER_REPOS.txt"
SWEEP_FILE.write_text("\n".join(todo_urls), encoding="utf-8")

print(f"Total Unique URLs Found: {len(all_urls)}")
print(f"Total Still Missing (To Process): {len(todo_urls)}")
print(f"Saved to {SWEEP_FILE}")
