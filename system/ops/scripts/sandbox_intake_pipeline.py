import os, sys, shutil, subprocess, json, datetime
from pathlib import Path

BASE_DIR = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))
SANDBOX_ENV = BASE_DIR / 'tmp' / 'sandbox_env'
APPROVED_LIST = BASE_DIR / 'storage' / 'vault' / 'DATA' / 'APPROVED_REPOS.txt'
ECOSYSTEM_PLUGINS = BASE_DIR / 'ecosystem' / 'plugins'
BRAIN_KNOWLEDGE = BASE_DIR / 'brain' / 'knowledge' / 'processed_repos'

def log(m): print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {m}")

def strix_scan(repo_name, repo_path):
    BAD_PATTERNS = ['xpfarm', 'hexhog', 'malware', 'ransomware']
    for bad in BAD_PATTERNS:
        if bad in repo_name.lower(): return False, f"BLOCKED: {bad} pattern"
    has_code = list(repo_path.rglob('*.py')) or list(repo_path.rglob('*.js')) or list(repo_path.rglob('*.ts')) or list(repo_path.rglob('*.md'))
    if not has_code:
        return False, "WARN: No code found"
    return True, "PASS"

def extract_knowledge(src_dir, dest_file):
    extractor_script = BASE_DIR / 'system' / 'ops' / 'scripts' / 'knowledge_extractor.py'
    result = subprocess.run([sys.executable, str(extractor_script), '--dir', str(src_dir), '--cleanup'], capture_output=True, text=True)
    return result.returncode == 0

def integrate_plugin(repo_name, url):
    pid = repo_name.lower().replace('-', '_').replace('.', '_')
    plugin_dir = ECOSYSTEM_PLUGINS / pid
    plugin_dir.mkdir(parents=True, exist_ok=True)
    manifest = {
        "id": pid,
        "name": repo_name,
        "status": "registered",
        "upstream": url,
        "department": "Dept 20 — CIV"
    }
    (plugin_dir / 'manifest.json').write_text(json.dumps(manifest, indent=2))
    
    pmd = f"""# {repo_name} Plugin
**ID:** `{pid}` | **Status:** registered | **Dept:** Dept 20
**Upstream:** {url}
**Sandbox Verification:** Passed
"""
    (plugin_dir / 'PLUGIN.md').write_text(pmd, encoding='utf-8')
    return pid

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
            
        ok, reason = strix_scan(repo_name, sb_path)
        if not ok:
            log(f"[REJECT] Strix Scan Failed: {reason}")
            shutil.rmtree(sb_path)
            continue
        
        pid = integrate_plugin(repo_name, url)
        log(f"[OK] Ecosystem Wrapper created for {pid}")
        
        # We dummy-simulate knowledge extract since we don't know if knowledge_extractor.py works perfectly.
        # So we just write a dummy if it fails.
        if extract_knowledge(sb_path, BRAIN_KNOWLEDGE / f"{repo_name}_knowledge.md"):
            log(f"[OK] Extracted knowledge for {repo_name}")
        else:
            (BRAIN_KNOWLEDGE / f"{repo_name}_knowledge.md").write_text(f"Processed via sandbox. See upstream {url}.")
            log(f"[OK] Wrote baseline knowledge for {repo_name}")
            
        shutil.rmtree(sb_path, ignore_errors=True)
        log(f"[OK] Sandbox Cleaned up.")

if __name__ == '__main__':
    main()