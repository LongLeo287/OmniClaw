import os, sys, shutil, subprocess, json, datetime
from pathlib import Path

BASE_DIR = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))
SANDBOX_ENV = BASE_DIR / 'vault' / 'quarantine'
APPROVED_LIST = BASE_DIR / 'vault' / 'DATA' / 'APPROVED_REPOS.txt'
ECOSYSTEM_PLUGINS = BASE_DIR / 'ecosystem' / 'plugins'
BRAIN_KNOWLEDGE = BASE_DIR / 'brain' / 'knowledge' / 'assimilated_repos'

def log(m): print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {m}")

def main():
    if not APPROVED_LIST.exists():
        log("No APPROVED_REPOS.txt found.")
        return

    urls = APPROVED_LIST.read_text('utf-8').strip().split('\n')[:10]
    log(f"Executing Sandbox Intake for {len(urls)} repos (Testing batch of 10)")

    for i, url in enumerate(urls, 1):
        if not url: continue
        repo_name = url.split('/')[-1]
        log(f"\n[{i}/{len(urls)}] Processing {repo_name}...")
        
        sb_path = SANDBOX_ENV / repo_name
        shutil.rmtree(sb_path, ignore_errors=True)
        
        res = subprocess.run(['git', 'clone', '--depth=1', '--quiet', url, str(sb_path)], capture_output=True)
        if res.returncode != 0:
            log(f"[FAIL] Could not clone {url}")
            continue
            
        log(f"[OK] {repo_name} cloned into {SANDBOX_ENV.name}. Intake Daemon task complete.")

    log(f"All {len(urls)} repositories fetched into Quarantine Queues.")

if __name__ == '__main__':
    main()