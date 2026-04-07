import os
from datetime import datetime

base_dir = os.path.join(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")), "ecosystem\workforce\agents")

agents = {
    'omni_observer': {
        'name': 'Omni-Sensory Observer (OSO)',
        'core': 'qwen2_5_omni',
        'desc': 'Department of Vision and Audio Processing. Grants OmniClaw sensory capabilities.'
    },
    'database_engineer': {
        'name': 'Omni Data Engineer (ODE)',
        'core': 'repo_supabase_agent_skills',
        'desc': 'Database Management Department. Handles SQL execution and Supabase integration.'
    },
    'frontend_command_center': {
        'name': 'Frontend UI Operations',
        'core': 'office_ui_fabric_core',
        'desc': 'Node-based Workflow Builder and UI Dashboard engineering team.'
    },
    'swarm_logistics': {
        'name': 'Swarm Agent Logistics',
        'core': 'qwen_agent',
        'desc': 'Factory for spawning micro-agents using Qwen Agent framework architectures.'
    }
}

for folder, data in agents.items():
    p = os.path.join(base_dir, folder)
    os.makedirs(p, exist_ok=True)
    
    # 1. Identity
    ts = datetime.now().isoformat()
    id_content = f"""---
id: {folder}
type: agent
owner: SYSTEM
registered_at: {ts}
tags: [department, {data['core']}]
---
# {data['name']}
{data['desc']}
Powered by core library: {data['core']}
"""
    with open(os.path.join(p, '_DIR_IDENTITY.md'), 'w', encoding='utf-8') as f:
        f.write(id_content)
        
    # 2. Stub Python Script
    py_content = f"""# OmniClaw Native Agent: {data['name']}
import os
import sys

class {folder.replace('_', ' ').title().replace(' ', '')}Agent:
    def __init__(self):
        self.department = '{data['name']}'
        self.core_dependency = '{data['core']}'
        
    def boot(self):
        print(f'[AGENT BOOT] {{self.department}} activating using {{self.core_dependency}} backbone...')
        # Implementation to be patched dynamically

if __name__ == '__main__':
    agent = {folder.replace('_', ' ').title().replace(' ', '')}Agent()
    agent.boot()
"""
    with open(os.path.join(p, f"{folder}.py"), 'w', encoding='utf-8') as f:
        f.write(py_content)
    print(f"Created {folder}")
