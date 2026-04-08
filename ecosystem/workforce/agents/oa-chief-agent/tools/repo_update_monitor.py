import os
import sys
import json
import urllib.request
import urllib.error
import datetime

from pathlib import Path
import os
_curr = Path(__file__).resolve().parent
while _curr != _curr.parent and not (_curr / "system" / "ops").is_dir():
    _curr = _curr.parent
BASE_DIR = str(_curr) if (_curr / "system" / "ops").is_dir() else os.environ.get("AOS_ROOT", str(Path(__file__).resolve().parents[6]))
REGISTRY_FILE = os.path.join(BASE_DIR, 'ecosystem', 'plugins', 'registry.json')
UPDATES_DIR = os.path.join(BASE_DIR, 'brain', 'knowledge', 'updates')
ENV_FILE = os.path.join(BASE_DIR, 'system', 'ops', 'secrets', 'MASTER.env')
QUARANTINE_DIR = os.path.join(BASE_DIR, 'system', 'security', 'QUARANTINE', 'incoming', 'UPDATE')
os.makedirs(UPDATES_DIR, exist_ok=True)
os.makedirs(QUARANTINE_DIR, exist_ok=True)

def get_github_token():
    env_token = os.environ.get('GITHUB_TOKEN')
    if env_token: return env_token
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line or line.startswith('#'): continue
                if '=' in line:
                    key, val = line.split('=', 1)
                    key = key.replace('export ', '').strip()
                    if key == 'GITHUB_TOKEN':
                        return val.strip().strip('"\'')
    return None

def fetch_latest_release(github_url, token):
    if not github_url.startswith('https://github.com/'):
        return None
    full_name = github_url.replace('https://github.com/', '').strip('/')
    
    url = f"https://api.github.com/repos/{full_name}/releases/latest"
    req = urllib.request.Request(url)
    if token: req.add_header('Authorization', f'token {token}')
    req.add_header('User-Agent', 'AI-OS-Corp-Update-Daemon/1.0')
    
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read().decode('utf-8'))
            return {
                "tag_name": data.get('tag_name'),
                "name": data.get('name'),
                "body": data.get('body'),
                "published_at": data.get('published_at'),
                "html_url": data.get('html_url')
            }
    except urllib.error.HTTPError as e:
        if e.code == 404:
            # Fallback for repos that don't deploy visual "releases"
            return fetch_latest_commit(full_name, token)
        print(f"Error API ({full_name}): {e.code}")
    except Exception as e:
        print(f"Error fetch {full_name}: {e}")
    return None

def fetch_latest_commit(full_name, token):
    url = f"https://api.github.com/repos/{full_name}/commits"
    req = urllib.request.Request(url)
    if token: req.add_header('Authorization', f'token {token}')
    req.add_header('User-Agent', 'AI-OS-Corp-Update-Daemon/1.0')
    
    try:
        with urllib.request.urlopen(req) as r:
            data = json.loads(r.read().decode('utf-8'))
            if data and isinstance(data, list):
                commit = data[0]
                sha = commit.get('sha')[:7]
                msg = commit.get('commit', {}).get('message', '')
                date = commit.get('commit', {}).get('author', {}).get('date', '')
                return {
                    "tag_name": f"commit-{sha}",
                    "name": f"Commit {sha}",
                    "body": msg,
                    "published_at": date,
                    "html_url": commit.get('html_url')
                }
    except Exception:
        pass
    return None

def main():
    if not os.path.exists(REGISTRY_FILE):
        print("[OmniClaw System Event] Registry missing.")
        return

    import time
    print("[OA Daemon] Starting OA Update Monitor Daemon in Background...")
    
    while True:
        with open(REGISTRY_FILE, 'r', encoding='utf-8') as f:
            registry = json.load(f)

        token = get_github_token()
        plugins = registry.get('plugins', [])
        updated_count = 0
    checked_count = 0

    print(f"[OmniClaw System Event] {len(plugins)} Active Plugins.")

    for plugin in plugins:
        github_url = plugin.get('github_url')
        if not github_url:
            continue
            
        manifest_path = os.path.join(BASE_DIR, 'ecosystem', plugin.get('path', ''), 'manifest.json')
        if not os.path.exists(manifest_path):
            continue

        with open(manifest_path, 'r', encoding='utf-8') as mf:
            manifest = json.load(mf)
            
        if not manifest.get('tracking', False):
            continue # Only track repos with explicit tracking flag
            
        checked_count += 1
        current_synced = manifest.get('last_synced_release', 'initial_intake')
        
        print(f"  > Checking {plugin['id']} (Current Sync: {current_synced})...", end='', flush=True)
        release_data = fetch_latest_release(github_url, token)
        
        if not release_data:
            print("[OmniClaw System Event]")
            continue
            
        new_tag = release_data['tag_name']
        
        if new_tag != current_synced:
            print("[OmniClaw System Event]")
            
            doc = f"## Plugin Update: {plugin['id']} ({new_tag})\n\n"
            doc += f"**Release Date:** {release_data.get('published_at')}\n"
            doc += f"**Original Link:** {release_data.get('html_url')}\n"
            doc += f"**Department:** {plugin.get('id')} - {plugin.get('type')}\n\n"
            doc += f"### Changelog/Notes:\n\n"
            doc += f"{release_data.get('body')}\n\n"
            doc += f"---\n\n> **Agent Support:** You can manually update the source code via Github or use script `git pull`."
            
            clean_tag = new_tag.replace('/', '-').replace('\\', '-')
            out_file = os.path.join(UPDATES_DIR, f"{plugin['id']}_release_{clean_tag}.md")
            with open(out_file, 'w', encoding='utf-8') as of:
                of.write(doc)
                
            # [System log: Legacy non-English comment removed]
            update_incoming_path = os.path.join(QUARANTINE_DIR, plugin['id'])
            if os.path.exists(update_incoming_path):
                import shutil
                shutil.rmtree(update_incoming_path, ignore_errors=True)
                
            print("[OmniClaw System Event]")
            import subprocess
            result = subprocess.run(
                ["git", "clone", "--depth=1", "--quiet", github_url, update_incoming_path],
                capture_output=True, text=True
            )
            
            if result.returncode == 0:
                print("[OmniClaw System Event] Extracting knowledge...")
                extractor_script = os.path.join(BASE_DIR, "ecosystem", "workforce", "system", "education", "registry-manager-agent", "tools", "knowledge_extractor.py")
                subprocess.run(
                    [sys.executable, extractor_script, "--dir", update_incoming_path, "--cleanup"],
                    capture_output=True, text=True, encoding="utf-8"
                )
                print("[OmniClaw System Event]")
            else:
                print(f"  [ERROR] Error Clone: {result.stderr[:100]}")

            manifest['last_synced_release'] = new_tag
            with open(manifest_path, 'w', encoding='utf-8') as mf:
                json.dump(manifest, mf, indent=2, ensure_ascii=False)
                
            updated_count += 1

        if updated_count > 0:
            print(f"[OA Daemon] Processed {updated_count} updates.")
            
        time.sleep(3600)  # Check every 1 hour

if __name__ == "__main__":
    main()