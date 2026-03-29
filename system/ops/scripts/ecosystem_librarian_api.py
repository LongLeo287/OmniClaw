import os
import sys
import argparse
from pathlib import Path

BASE_DIR = Path('d:/LongLeo/AI OS CORP/AI OS')
ECOSYSTEM_DIR = BASE_DIR / 'ecosystem'

def build_index():
    index = []
    # Quét Skills
    skills_dir = ECOSYSTEM_DIR / 'skills'
    if skills_dir.exists():
        for d in skills_dir.iterdir():
            if d.is_dir() and (d / 'SKILL.md').exists():
                text = (d / 'SKILL.md').read_text('utf-8', errors='ignore')
                index.append({'type': 'Skill', 'id': d.name, 'path': str(d / 'SKILL.md'), 'desc': text[:300]})
    
    # Quét Agents
    agents_dir = ECOSYSTEM_DIR / 'workforce' / 'agents'
    if agents_dir.exists():
        for d in agents_dir.iterdir():
            if d.is_dir() and (d / 'AGENT.md').exists():
                text = (d / 'AGENT.md').read_text('utf-8', errors='ignore')
                index.append({'type': 'Agent', 'id': d.name, 'path': str(d / 'AGENT.md'), 'desc': text[:300]})
                
    # Quét Depts
    depts_dir = ECOSYSTEM_DIR / 'workforce' / 'departments'
    if depts_dir.exists():
        for d in depts_dir.iterdir():
            if d.is_dir() and (d / 'rules.md').exists():
                text = (d / 'rules.md').read_text('utf-8', errors='ignore')
                index.append({'type': 'Department', 'id': d.name, 'path': str(d), 'desc': text[:300]})
                
    # Quét Workflows
    wf_dir = ECOSYSTEM_DIR / 'workflows'
    if wf_dir.exists():
        for f in wf_dir.glob('*.md'):
            text = f.read_text('utf-8', errors='ignore')
            index.append({'type': 'Workflow', 'id': f.stem, 'path': str(f), 'desc': text[:300]})
            
    # Quét Plugins
    plug_dir = ECOSYSTEM_DIR / 'plugins'
    if plug_dir.exists():
        for d in plug_dir.iterdir():
            if d.is_dir() and (d / 'PLUGIN.md').exists():
                text = (d / 'PLUGIN.md').read_text('utf-8', errors='ignore')
                index.append({'type': 'Plugin', 'id': d.name, 'path': str(d / 'PLUGIN.md'), 'desc': text[:300]})
                
    return index

def search(query):
    index = build_index()
    results = []
    q = str(query).lower()
    for item in index:
        if q in item['id'].lower() or q in item['desc'].lower():
            results.append(item)
    return results

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Ecosystem Librarian API v1.0')
    parser.add_argument('action', choices=['search', 'list'], help='Action to perform')
    parser.add_argument('query', nargs='?', default='', help='Query string for semantic search')
    args = parser.parse_args()
    
    if args.action == 'search':
        if not args.query:
            print('LỖI: Bạn phải nhập từ khóa để tìm kiếm (VD: python ecosystem_librarian_api.py search "browser")')
            sys.exit(1)
        res = search(args.query)
        if not res:
            print(f'404 [LIBRARIAN]: Không tìm thấy mảnh tri thức nào cho: {args.query}')
            print(f'HƯỚNG DẪN: Nếu bạn là Agent, hãy yêu cầu Sếp duyệt intake repo mới.')
        else:
            print(f'200 [LIBRARIAN]: Tìm thấy {len(res)} kết quả khớp với yêu cầu của bạn:\\n')
            for r in res:
                print(f"[{r['type'].upper()}] ID: {r['id']}")
                print(f"ABSOLUTE PATH: {r['path']}")
                print("---")
                
    elif args.action == 'list':
        idx = build_index()
        print(f'TỔNG KIỂM KÊ THƯ VIỆN HỆ SINH THÁI (LIBRARIAN DB): {len(idx)} Items')
        counts = {}
        for item in idx:
            counts[item['type']] = counts.get(item['type'], 0) + 1
        for t, c in counts.items():
            print(f" - {t}: {c}")
