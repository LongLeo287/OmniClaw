import os
import yaml
import re

ROOT = r'd:\LongLeo\AI OS CORP\AI OS'
AGENTS_DIR = os.path.join(ROOT, 'ecosystem', 'workforce', 'agents')
ORG_CHART = os.path.join(ROOT, 'brain', 'corp', 'org_chart.yaml')
AGENTS_MD = os.path.join(ROOT, 'brain', 'shared-context', 'AGENTS.md')

def classify_dept(agent_id, content):
    c = content.lower()
    if any(k in c for k in ['video', 'tiktok', 'youtube', 'content', 'marketing', 'seo', 'audio', 'tts']):
        return 'marketing'
    if any(k in c for k in ['data', 'analytics', 'database', 'sql', 'predict']):
        return 'data'
    if any(k in c for k in ['deploy', 'cloud', 'aws', 'docker', 'ci/cd', 'nginx', 'tunnel', 'cloudflare']):
        return 'operations'
    if any(k in c for k in ['security', 'scan', 'vulnerability', 'owasp']):
        return 'security'
    if any(k in c for k in ['test', 'qa', 'quality']):
        return 'qa'
    return 'engineering' # Default

with open(ORG_CHART, 'r', encoding='utf-8') as f:
    org = yaml.safe_load(f)

# 1. Clean up old auto_created from engineering
org['departments']['engineering']['workers'] = [
    w for w in org.get('departments', {}).get('engineering', {}).get('workers', [])
    if not w.get('auto_created')
]

with open(AGENTS_MD, 'r', encoding='utf-8') as f:
    md_content = f.read()

# Remove old added lines in AGENTS.md
lines = md_content.split('\n')
md_content = '\n'.join([l for l in lines if 'Tự động sinh từ Knowledge assimilation' not in l])

added_counts = {}

# 2. Re-assign
for agent_id in os.listdir(AGENTS_DIR):
    agent_path = os.path.join(AGENTS_DIR, agent_id)
    if os.path.isdir(agent_path) and not agent_id.startswith('_'):
        
        # Check if already in org chart WITHOUT auto_created flag
        # (Meaning it was a permanent original agent)
        is_original = False
        for d, data in org.get('departments', {}).items():
            if data and data.get('workers'):
                for w in data['workers']:
                    if w['agent'] == agent_id and not w.get('auto_created'):
                        is_original = True
            if data and data.get('head') == agent_id:
                is_original = True
                
        if is_original: continue

        # Read agent context to classify
        agent_md = os.path.join(agent_path, f'{agent_id}.md')
        if not os.path.exists(agent_md):
            agent_md = os.path.join(agent_path, 'AGENT.md')
            
        content = ''
        if os.path.exists(agent_md):
            with open(agent_md, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                
        dept = classify_dept(agent_id, content)
        
        if dept not in org['departments']:
            org['departments'][dept] = {'workers': [], 'head': None}
            
        if 'workers' not in org['departments'][dept] or org['departments'][dept]['workers'] is None:
            org['departments'][dept]['workers'] = []
            
        org['departments'][dept]['workers'].append({
            'agent': agent_id,
            'role': f'Auto-scaffolded specialist from {agent_id}. Auto-classified to {dept}.',
            'prompt': f'ecosystem/workforce/departments/{dept}/WORKER_PROMPT.md',
            'created_by': 'Auto_Assimilator',
            'auto_created': True
        })
        added_counts[dept] = added_counts.get(dept, 0) + 1
        
        # AGENTS.md
        table_header = '| Subagent | Role | Activated by |\n|----------|------|--------------|'
        if table_header in md_content:
            new_row = f'\n| {agent_id} | Chuyên viên {dept} (Auto-created) | arch-chief-agent |'
            md_content = md_content.replace(table_header, table_header + new_row)

with open(ORG_CHART, 'w', encoding='utf-8') as f:
    yaml.dump(org, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
    
with open(AGENTS_MD, 'w', encoding='utf-8') as f:
    f.write(md_content)

print(added_counts)
