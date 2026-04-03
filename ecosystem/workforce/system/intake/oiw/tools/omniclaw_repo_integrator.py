import os, sys, json, re, urllib.request, urllib.error, datetime

from pathlib import Path
import os
_curr = Path(__file__).resolve().parent
while _curr != _curr.parent and not (_curr / "system" / "ops").is_dir():
    _curr = _curr.parent
BASE_DIR = str(_curr) if (_curr / "system" / "ops").is_dir() else os.environ.get("AOS_ROOT", str(Path(__file__).resolve().parents[6]))
PLUGINS_DIR = os.path.join(BASE_DIR, 'ecosystem', 'plugins')
VAULT_DATA = os.path.join(BASE_DIR, 'vault', 'assets', 'data')
REGISTRY_FILE = os.path.join(PLUGINS_DIR, 'registry.json')
ENV_FILE = os.path.join(BASE_DIR, '.env')
SPOOL_FILE = os.path.join(VAULT_DATA, 'github.txt')
SELECTED_CSV = os.path.join(VAULT_DATA, 'selected_repos.csv')
ERROR_CSV = os.path.join(VAULT_DATA, 'error_repos.csv')
OIW_INBOX = os.path.join(BASE_DIR, 'vault', 'tmp', 'sandbox_env', 'OIW_INBOX')

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

def fetch_repo_meta(full_name, token):
    url = f"https://api.github.com/repos/{full_name}"
    req = urllib.request.Request(url)
    if token: req.add_header('Authorization', f'token {token}')
    req.add_header('User-Agent', 'AI-OS-Corp-Integrate/1.0')
    try:
        with urllib.request.urlopen(req) as r:
            return json.loads(r.read().decode('utf-8'))
    except Exception as e:
        print(f"Error fetch meta {full_name}: {e}")
        return None

def fetch_repo_readme(full_name, token):
    url = f"https://api.github.com/repos/{full_name}/readme"
    req = urllib.request.Request(url)
    if token: req.add_header('Authorization', f'token {token}')
    req.add_header('Accept', 'application/vnd.github.v3.raw')
    req.add_header('User-Agent', 'AI-OS-Corp-Integrate/1.0')
    try:
        with urllib.request.urlopen(req) as r:
            return r.read().decode('utf-8', errors='ignore')
    except Exception:
        return ""

def integrate_repo(full_name):
    print("[OmniClaw System Event]")
    if not isinstance(full_name, str) or full_name.count('/') != 1:
        print("[OmniClaw System Event]")
        return False
    
    parts = full_name.split('/')
    if not parts[0].strip() or not parts[1].strip():
        print("[OmniClaw System Event] Invalid repo format")
        return False

    token = get_github_token()
    meta = fetch_repo_meta(full_name, token)
    if not meta: return False

    owner, repo_name = full_name.split('/')
    readme = fetch_repo_readme(full_name, token)

    os.makedirs(OIW_INBOX, exist_ok=True)
    
    # Pack raw metadata for Daemons
    clean_desc = meta.get('description', '')
    if clean_desc: clean_desc = clean_desc.replace('\n', ' ')
    
    payload_path = os.path.join(OIW_INBOX, f"OIW_RAW_{repo_name}.md")
    content = f"""---
id: {repo_name}
name: "{meta.get('name', repo_name)}"
type: raw_intake
owner: OIW
status: pending_health_check
github_url: https://github.com/{full_name}
stars: {meta.get('stargazers_count')}
description: "{clean_desc}"
---

# Repo Metadata: {full_name}

## README Payload
{readme[:2000]}
... (truncated by OIW logic) ...
"""
    with open(payload_path, 'w', encoding='utf-8') as f:
        f.write(content)


    # Skip legacy PENDING_FILE removal block 
    
    with open(SELECTED_CSV, 'a', encoding='utf-8') as f:
        desc = meta.get('description', '')
        if desc: desc = desc.replace(',', ';').replace('\n', ' ')
        else: desc = "No description"
        ts = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
        f.write(f"{ts},{repo_name},{repo_name},{meta.get('html_url')},{meta.get('stargazers_count')},{desc}\n")

    print(f"✅ Complete Integrate: {repo_name}")
    return True

if __name__ == '__main__':
    from datetime import datetime as dt
    if len(sys.argv) > 1:
        for repo in sys.argv[1:]:
            integrate_repo(repo)
    else:
        if os.path.exists(SPOOL_FILE):
            with open(SPOOL_FILE, 'r', encoding='utf-8') as f:
                urls = [line.strip() for line in f if line.strip()]
            
            if not urls:
                print("[OIW] No links in github.txt to process.")
                sys.exit(0)

            for url in urls:
                full_name = url
                if 'github.com/' in url:
                    full_name = url.split('github.com/')[-1].split('.git')[0].strip('/')
                
                try:
                    success = integrate_repo(full_name)
                    if not success:
                        with open(ERROR_CSV, 'a', encoding='utf-8') as ef:
                            ts = dt.now().strftime("%Y-%m-%dT%H:%M:%S")
                            ef.write(f"{ts},{full_name},{url},Fetch Failed\n")
                except Exception as e:
                    with open(ERROR_CSV, 'a', encoding='utf-8') as ef:
                        ts = dt.now().strftime("%Y-%m-%dT%H:%M:%S")
                        ef.write(f"{ts},{full_name},{url},Exception: {e}\n")

            with open(SPOOL_FILE, 'w', encoding='utf-8') as f:
                f.write('')
            print("[OIW] Completed intake spool. Emptied github.txt.")