import os
import json
import sys
from datetime import datetime

abs_daemons = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'daemons'))
sys.path.append(abs_daemons)
try:
    from daemon_utils import call_omniclaw_model
except ImportError:
    def call_omniclaw_model(prompt, *args, **kwargs):
        return '{"summary": "Abstract System Domain", "tags": ["abstract", "system"], "type": "knowledge"}'

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

def is_directory_vetted(dir_path):
    """Vetting Layer 2: A directory is valid ONLY IF it contains actual content files."""
    valid_extensions = ('.py', '.js', '.ts', '.go', '.rs', '.java', '.cpp', '.md', '.json', '.html', '.css', '.txt')
    for root, _, files in os.walk(dir_path):
        if "__pycache__" in root or ".git" in root: continue
        for f in files:
            if f.endswith(valid_extensions):
                fpath = os.path.join(root, f)
                try:
                    if os.path.getsize(fpath) > 100: # Has at least 1 valid payload file
                        return True
                except: pass
    return False

def stamp_directory_identity(dir_path, default_type="knowledge_domain"):
    if os.path.exists(os.path.join(dir_path, "_DIR_IDENTITY.md")): return False
    
    # [VETTING CHECK]
    if not is_directory_vetted(dir_path):
        print(f"  \033[93m[VETTING FAILED]\033[0m Directory empty/invalid: {os.path.basename(dir_path)}")
        return False
        
    dirname = os.path.basename(dir_path)
    contents = [f for f in os.listdir(dir_path) if not f.startswith('.')][:20]
    prompt = f"Analyze this OmniClaw System Directory.\nName: {dirname}\nContents: {contents}\nOutput purely in JSON a summary, 2 tags, and type. Format: {{\"summary\":\"...\",\"tags\":[\"...\",\"...\"]}}"
    
    summary = f"Aggregated Node for {dirname}"
    tags = [dirname.lower(), "vetted-domain"]
    
    try:
        res = call_omniclaw_model(prompt, json_format=True)
        if res:
            obj = json.loads(res.strip())
            summary = obj.get("summary", summary)
            if obj.get("tags"): tags = obj.get("tags")
    except: pass
    
    ts = datetime.now().isoformat()
    content = f"---\nid: group-{dirname.lower().replace(' ', '-')}\ntype: {default_type}\nowner: OA\nregistered_at: {ts}\ntags: {json.dumps(tags)}\n---\n\n# {dirname}\n\n## Summary\n{summary}\n"
    
    try:
        with open(os.path.join(dir_path, "_DIR_IDENTITY.md"), "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  \033[92m[OK]\033[0m Assmiliated: {dirname}")
        return True
    except: return False

def stamp_markdown_frontmatter(file_path):
    if not os.path.exists(file_path): return False
    
    # [VETTING CHECK]
    try:
        if os.path.getsize(file_path) < 100:
            print(f"  \033[93m[VETTING FAILED]\033[0m File too small payload (<100b): {os.path.basename(file_path)}")
            return False
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except: return False
    
    if content.strip().startswith("---"): return False
        
    filename = os.path.basename(file_path)
    prompt = f"Analyze Markdown file: {filename}\nContent:\n{content[:1500]}\nOutput ONLY JSON: {{\"title\": \"...\", \"type\": \"knowledge\", \"tags\": [\"...\", \"...\"]}}"
    
    m_title = os.path.splitext(filename)[0]
    m_type = "knowledge"
    m_tags = ["vetted-file"]
    
    try:
        res = call_omniclaw_model(prompt, json_format=True)
        if res:
            obj = json.loads(res.strip())
            m_title = obj.get("title", m_title)
            m_type = obj.get("type", m_type)
            if obj.get("tags"): m_tags = obj.get("tags")
    except: pass
    
    ts = datetime.now().isoformat()
    fm = f"---\nid: doc-{m_title.lower().replace(' ', '-')}\ntype: {m_type}\nowner: SYSTEM\ntags: {json.dumps(m_tags)}\n---\n\n"
    
    try:
        with open(file_path, "w", encoding="utf-8") as f: f.write(fm + content)
        print(f"  \033[96m[STAT]\033[0m Injected Index: {filename}")
        return True
    except: return False

def run_deep_assimilation():
    print("\033[94m[INFO]\033[0m Starting VETTED Deep Assimilation...")
    dir_count = 0; file_count = 0
    
    bk_path = os.path.join(ROOT, 'brain', 'knowledge')
    if os.path.exists(bk_path):
        for item in os.listdir(bk_path):
            ipath = os.path.join(bk_path, item)
            if os.path.isdir(ipath) and item not in ['catalog', 'library', 'CIV']:
                if stamp_directory_identity(ipath, "knowledge_domain"): dir_count += 1
            elif os.path.isfile(ipath) and item.endswith('.md'):
                if not item.startswith(('KI_', 'graph_', 'INDEX')):
                    if stamp_markdown_frontmatter(ipath): file_count += 1
                        
    es_path = os.path.join(ROOT, 'ecosystem', 'skills')
    if os.path.exists(es_path):
        for item in os.listdir(es_path):
            ipath = os.path.join(es_path, item)
            if os.path.isdir(ipath):
                if stamp_directory_identity(ipath, "skill_node"): dir_count += 1
                    
    print(f"\033[92m[DONE]\033[0m Assimilated {dir_count} Domain Groups and {file_count} Loose Files.")

if __name__ == "__main__":
    run_deep_assimilation()
