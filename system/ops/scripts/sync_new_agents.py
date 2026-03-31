import os
import yaml

ROOT = r'd:\LongLeo\AI OS CORP\AI OS'
AGENTS_DIR = os.path.join(ROOT, 'ecosystem', 'workforce', 'agents')
ORG_CHART = os.path.join(ROOT, 'brain', 'corp', 'org_chart.yaml')
AGENTS_MD = os.path.join(ROOT, 'brain', 'shared-context', 'AGENTS.md')

def main():
    # Load org chart
    with open(ORG_CHART, 'r', encoding='utf-8') as f:
        org = yaml.safe_load(f)
        
    with open(AGENTS_MD, 'r', encoding='utf-8') as f:
        md_content = f.read()

    existing_in_org = set()
    for d, data in org.get('departments', {}).items():
        if data and data.get('workers'):
            for w in data['workers']:
                existing_in_org.add(w['agent'])
        if data and data.get('head'):
            existing_in_org.add(data['head'])

    added_count = 0
    # Scan all agent folders
    for agent_id in os.listdir(AGENTS_DIR):
        agent_path = os.path.join(AGENTS_DIR, agent_id)
        if os.path.isdir(agent_path) and not agent_id.startswith('_'):
            if agent_id not in existing_in_org:
                # Add to Engineering by default if auto_created
                eng = org['departments'].get('engineering', {})
                if 'workers' not in eng or eng['workers'] is None:
                    eng['workers'] = []
                
                eng['workers'].append({
                    'agent': agent_id,
                    'role': f'Auto-scaffolded specialist from {agent_id}',
                    'prompt': 'ecosystem/workforce/departments/engineering/WORKER_PROMPT.md',
                    'created_by': 'Auto_Assimilator',
                    'auto_created': True
                })
                added_count += 1
                
                # Add to AGENTS.md
                if agent_id not in md_content:
                    table_header = '| Subagent | Role | Activated by |\n|----------|------|--------------|'
                    if table_header in md_content:
                        new_row = f'\n| {agent_id} | Tự động sinh từ Knowledge assimilation | arch-chief-agent |'
                        md_content = md_content.replace(table_header, table_header + new_row)

    if added_count > 0:
        with open(ORG_CHART, 'w', encoding='utf-8') as f:
            yaml.dump(org, f, allow_unicode=True, default_flow_style=False, sort_keys=False)
        with open(AGENTS_MD, 'w', encoding='utf-8') as f:
            f.write(md_content)
            
    print(f'Done! Synced {added_count} new agents to Org Chart and AGENTS.md.')

if __name__ == '__main__':
    main()
