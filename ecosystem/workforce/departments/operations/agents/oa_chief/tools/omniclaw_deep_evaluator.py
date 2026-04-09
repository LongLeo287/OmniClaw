"""
OmniClaw Deep Repo Evaluator (Official Workflow)
Owner: Antigravity + Dept 01 (AI Core), Dept 10 (Security), Dept 11 (Web Ops), Dept 20 (CIV)

Workflow:
1. Dept 10 (Strix): Dept 10 (Strix): Scan names to block Malware/Game/Ransomware.
2. Dept 11 (API Crawler): Fetch GitHub Metadata & README (0.3s delay to avoid Ban).
3. Dept 01 (Golden Eval): Read README to score Tech stack (Agent, RAG, MCP...).
4. Dept 20 (CIV): Filter APPROVE list, create CIV Tickets. Write REFERENCE to Catalog.

Input data: ALL_PENDING_REPOS.txt
"""

import os
import re
import json
import time
import datetime
import urllib.request
import urllib.error

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
INPUT_FILE = os.path.join(BASE_DIR, 'storage', 'vault', 'DATA', 'Github.txt')
ENV_FILE = os.path.join(BASE_DIR, 'system', 'ops', 'secrets', 'MASTER.env')
QUARANTINE_DIR = os.path.join(BASE_DIR, 'system', 'security', 'QUARANTINE', 'incoming', 'REPO')
REF_CATALOG_FILE = os.path.join(BASE_DIR, 'brain', 'knowledge', 'notes', 'REFERENCE_REPOS_CATALOG.md')

# --- CONFIG ---
BAD_PATTERNS = ["xpfarm", "hexhog", "malware", "ransomware", "prompt_leak", "jailbreak", "crack", "hack-tools", "stealer", "bypass"]
DEFER_KEYWORDS = ['ui', 'frontend', 'react', 'vue', 'angular', 'css', 'tailwind', 'design', 'boilerplate', 'tutorial', 'course', 'example']

GOLDEN_KEYWORDS = {
    "mcp": 15,          
    "orchestrator": 12, 
    "agent": 10,         
    "rag": 10,          
    "graph": 10,        
    "llm": 8,           
    "workflow": 8,
    "browser-use": 8,
    "scraper": 5
}

def log(msg):
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {msg}")

def load_token():
    if not os.path.exists(ENV_FILE):
        return None
    with open(ENV_FILE, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            line = line.strip()
            if line.startswith('GITHUB_TOKEN='):
                return line.split('=', 1)[1].strip()
    return None

GITHUB_TOKEN = load_token()

def api_request(url, is_raw=False):
    req = urllib.request.Request(url)
    if GITHUB_TOKEN:
        req.add_header('Authorization', f'token {GITHUB_TOKEN}')
    if is_raw:
        req.add_header('Accept', 'application/vnd.github.v3.raw')
    else:
        req.add_header('Accept', 'application/vnd.github.v3+json')
    req.add_header('User-Agent', 'AI-OS-OmniClaw-DeepEval/1.0')

    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            if is_raw:
                return resp.read().decode('utf-8', errors='replace'), None
            return json.loads(resp.read().decode('utf-8')), None
    except urllib.error.HTTPError as e:
        if e.code == 403:
            return None, 'RATE_LIMIT'
        return None, f'HTTP_{e.code}'
    except Exception as e:
        return None, str(e)

def dept10_strix_check(repo_name):
    """Dept 10: Security Pre-Check"""
    name_l = repo_name.lower()
    for bad in BAD_PATTERNS:
        if bad in name_l:
            return False, f"Contains malicious code '{bad}'"
    return True, "SAFE"

def dept01_golden_eval(readme, meta):
    """Dept 01: Central Intelligence Scoring"""
    if not readme or len(readme) < 50:
        return 'REJECT', 0, "No README / Empty"
        
    score = 0
    content = readme.lower()
    
    # Check defer keywords (Frontend/UI)
    for kw in DEFER_KEYWORDS:
        if re.search(r'\b' + kw + r'\b', content) and not ("agent" in content or "llm" in content):
            return 'DEFER', score, f"Frontend/UI ({kw})"

    # Scoring
    if "python" in content: score += 10
    if "typescript" in content or "node.js" in content: score += 5

    hit_features = []
    for kw, pts in GOLDEN_KEYWORDS.items():
        if re.search(r'\b' + kw + r'\b', content):
            score += pts
            hit_features.append(kw.upper())
            
    # Check stars context
    stars = meta.get('stargazers_count', 0)
    if stars > 1000: score += 10
    elif stars < 10: score -= 20

    if score >= 20 and hit_features:
        return 'APPROVE', score, f"Golden Match [{', '.join(hit_features)}]"
    
    return 'REFERENCE', score, f"Low Context (Score: {score})"

def run_deep_eval(urls, limit=10):
    log("[OmniClaw System Event]")
    results = {'APPROVE': [], 'REFERENCE': [], 'DEFER': [], 'REJECT': [], 'ERROR': []}

    for i, url in enumerate(urls[:limit], 1):
        try:
            url_clean = url.strip().rstrip('/')
            if not url_clean: continue
            
            repo_path = url_clean.split('github.com/')[-1]
            if repo_path.count('/') < 1: continue
            owner, repo_name = repo_path.split('/')[:2]
            
            log(f"[{i}/{limit}] Analyzing {owner}/{repo_name}...")

            # DEPT 10
            is_safe, sec_reason = dept10_strix_check(repo_name)
            if not is_safe:
                results['REJECT'].append({'url': url_clean, 'reason': sec_reason})
                continue
                
            # DEPT 11 (Wait to avoid rate limit)
            time.sleep(0.4)
            meta, err = api_request(f"https://api.github.com/repos/{owner}/{repo_name}")
            if err:
                results['ERROR'].append({'url': url_clean, 'reason': f"Meta Fetch: {err}"})
                continue
                
            updated = str(meta.get('updated_at', ''))[:10]
            if updated:
                last_up = datetime.datetime.strptime(updated, '%Y-%m-%d').date()
                if (datetime.date.today() - last_up).days > 730:
                    results['DEFER'].append({'url': url_clean, 'reason': "Outdated > 24m"})
                    continue

            time.sleep(0.4)
            readme, err2 = api_request(f"https://api.github.com/repos/{owner}/{repo_name}/readme", is_raw=True)
            if err2:
                results['REJECT'].append({'url': url_clean, 'reason': "No README (API Error)"})
                continue

            # DEPT 01
            verdict, score, ai_reason = dept01_golden_eval(readme, meta)
            
            results[verdict].append({
                'url': url_clean,
                'name': f"{owner}/{repo_name}",
                'score': score,
                'reason': ai_reason,
                'stars': meta.get('stargazers_count', 0)
            })

        except Exception as e:
            results['ERROR'].append({'url': url_clean, 'reason': f"Exception: {e}"})

    return results

def process_results(results):
    log("[OmniClaw System Event]") ===")
    
    # 1. GENERATE CIV TICKETS
    os.makedirs(QUARANTINE_DIR, exist_ok=True)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    ticket_count = 0
    
    for i, item in enumerate(results['APPROVE']):
        ticket_id = f"CIV-{date_str}-DEEPEVAL-{str(ticket_count).zfill(4)}"
        with open(os.path.join(QUARANTINE_DIR, f"{ticket_id}.txt"), 'w', encoding='utf-8') as f:
            f.write(f"Source: {item['url']}\n")
            f.write(f"Type: REPO_GOLDEN\n")
            f.write(f"Score: {item['score']}\n")
            f.write(f"Features: {item['reason']}\n")
            f.write(f"Agent: dept-01-golden-evaluator\n")
            f.write(f"Date: {date_str}\n")
        ticket_count += 1
        
    log("[OmniClaw System Event]")

    # 2. WRITE REFERENCES
    os.makedirs(os.path.dirname(REF_CATALOG_FILE), exist_ok=True)
    with open(REF_CATALOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"\n\n## 📚 BATCH UPDATE {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        for item in results['REFERENCE']:
            f.write(f"- {item['url']} (⭐ {item['stars']} | Match: {item['score']}đ)\n")
            
    log("[OmniClaw System Event]")} repos to reference library.")
    
    # 3. SUMMARY
    log("[OmniClaw System Event]")
    for k, v in results.items():
        log(f"{k}: {len(v)}")

if __name__ == '__main__':
    log("[OmniClaw System Event]")
    if not os.path.exists(INPUT_FILE):
        log("[OmniClaw System Event]")
        exit()
        
    with open(INPUT_FILE, 'r', encoding='utf-8') as f:
        urls = [l.strip() for l in f if l.strip()]
        
    log("[OmniClaw System Event]")} URLs.")
    
    import sys
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else len(urls)
    
    res = run_deep_eval(urls, limit=limit)
    process_results(res)
    
    # [System log: Legacy non-English comment removed]
    urls_remaining = urls[limit:]
    with open(INPUT_FILE, 'w', encoding='utf-8') as f:
        for u in urls_remaining:
            f.write(u + '\n')
    log("[OmniClaw System Event]")} unanalysed.")
    
    log("[OmniClaw System Event]")