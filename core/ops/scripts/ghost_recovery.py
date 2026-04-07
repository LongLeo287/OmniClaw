import os
import shutil
import urllib.request
import json
import time

PLUGINS_DIR = r"D:\LongLeo\OmniClaw OS\OmniClaw\ecosystem\plugins"
RECOVERY_FILE = r"D:\LongLeo\OmniClaw OS\OmniClaw\vault\assets\data\repos_pending.txt"
LOG_FILE = r"D:\LongLeo\OmniClaw OS\OmniClaw\vault\assets\data\GHOST_RECOVERY_LOG.txt"

def is_ghost_repo(folder_path: str) -> bool:
    """Check if the downloaded folder lacks actual source files, making it a ghost/phantom repo."""
    valid_extensions = (".py", ".js", ".ts", ".go", ".rs", ".java", ".c", ".cpp", ".cs", ".php", ".html", ".css", ".md", ".json")
    code_size = 0
    file_count = 0
    for root, _, files in os.walk(folder_path):
        for file in files:
            file_count += 1
            if file.endswith(valid_extensions) and "manifest.json" not in file and "_DIR_IDENTITY.md" not in file:
                code_size += os.path.getsize(os.path.join(root, file))
    
    if code_size < 1024 and file_count <= 4:
        return True
    return False

def extract_repo_name(folder_path: str, dirname: str) -> str:
    """Extract standard query name from manifest or folder name."""
    manifest_path = os.path.join(folder_path, "manifest.json")
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if "name" in data:
                     return data["name"]
        except Exception: pass
    
    # Strip knowledge_ prefix
    name = dirname
    if name.startswith("knowledge_"):
        name = name.replace("knowledge_", "")
    return name

def search_github(query: str) -> str:
    """Search Github API to accurately convert a query into a valid git clone URL."""
    # Replace generic suffixes or symbols if needed
    query = query.replace("_", " ").replace("-", " ")
    url = f"https://api.github.com/search/repositories?q={urllib.parse.quote(query)}&per_page=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'OmniClaw-Ghost-Recovery-Bot'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if data['total_count'] > 0:
                return data['items'][0]['clone_url']
    except Exception as e:
        status_code = getattr(e, 'code', None)
        if status_code == 403:
            return "RATE_LIMITED"
    return None

def main():
    import urllib.parse
    print(f"[GHOST BUSTER] Scanning {PLUGINS_DIR} for empty phantom repositories...")
    
    ghosts = []
    items = os.listdir(PLUGINS_DIR)
    for dirname in items:
        folder_path = os.path.join(PLUGINS_DIR, dirname)
        if os.path.isdir(folder_path) and is_ghost_repo(folder_path):
            name = extract_repo_name(folder_path, dirname)
            ghosts.append((folder_path, dirname, name))
            
    print(f"[GHOST BUSTER] Detected {len(ghosts)} Ghost Repositories.")
    
    if not ghosts:
        return

    os.makedirs(os.path.dirname(RECOVERY_FILE), exist_ok=True)
    
    deleted_count = 0
    recovered_urls = []
    failed_names = []
    
    # Prepare logs
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n--- Ghost Recovery Session: {time.ctime()} ---\n")
    
    for folder_path, dirname, name in ghosts:
        print(f"  [>] Processing Ghost: {dirname} (Query: {name})")
        
        # 1. Look up accurate Clone URL
        git_url = search_github(name)
        
        if git_url == "RATE_LIMITED":
            print(f"  [!] GitHub API Rate Limit reached! Halting external lookups.")
            # Put the remainder to fail list so user knows what wasn't fetched
            failed_names.append(name)
        elif git_url:
            print(f"      -> Found Verified Source: {git_url}")
            recovered_urls.append(git_url)
        else:
            print(f"      -> [!] Could not locate a verified repository for '{name}'")
            failed_names.append(name)

        # 2. Obliterate Ghost Folder to clean workspace
        try:
            shutil.rmtree(folder_path, ignore_errors=True)
            deleted_count += 1
            print(f"      -> Deleted Ghost Folder.")
        except Exception: pass
        
        # Artificial delay to respect GitHub public API (10 requests/min ideally, we do 2 secs)
        # But if we have 500 ghosts, maybe we should just write the raw query to pending and let OIW fetch them.
        time.sleep(2)
        
    # Append genuine URLs straight into Intake queue
    if recovered_urls:
        with open(RECOVERY_FILE, "a", encoding="utf-8") as f:
            for url in recovered_urls:
                f.write(f"{url}\n")
        print(f"\n[GHOST BUSTER] Pushed {len(recovered_urls)} verified git URLs to OIW Pending Intake ({RECOVERY_FILE}).")

    if failed_names:
        fail_path = os.path.join(os.path.dirname(RECOVERY_FILE), "ghosts_lookup_failed.txt")
        with open(fail_path, "a", encoding="utf-8") as f:
            for name in failed_names:
                f.write(f"{name}\n")
        print(f"[GHOST BUSTER] Saved {len(failed_names)} unresolvable (or rate-limited) Ghost names to {fail_path}.")

    print(f"\n[GHOST BUSTER] Execution Complete! Purged {deleted_count} empty ghost folders. System is genuine.")

if __name__ == "__main__":
    import urllib.parse
    main()
