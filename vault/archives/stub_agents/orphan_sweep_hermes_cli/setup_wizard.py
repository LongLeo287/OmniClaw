import os
from dotenv import load_dotenv
def configure_agent(agent_name, template):
    if template == 'ORPHAN_SWEEP_hermes_cli':
        backend = 'hermes'
        models = ['model1', 'model2']
        tools = ['tool1', 'tool2']
        config = {
            'backend': backend,
            'models': models,
            'tools': tools
        }
        with open(f'{agent_name}/config.json', 'w') as file:
            file.write(str(config))
    else:
        print('Template not found.')