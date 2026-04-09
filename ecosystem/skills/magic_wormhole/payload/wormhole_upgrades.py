import json
from os import path

def upgrade_wormhole(version):
    config_path = path.join(path.dirname(__file__), 'magic-wormhole_120017_config.json')
    with open(config_path, 'r') as file:
        config = json.load(file)
    if version == 120017:
        print('Wormhole already at latest version.')
    else:
        # Upgrade logic here
        print(f'Upgrading wormhole to version {version}...')
        config['system']['components'][0]['version'] = str(version)
        with open(config_path, 'w') as file:
            json.dump(config, file, indent=4)
    return config