import os
import datetime
import json
import uuid

DAEMON_NAME = "OMA [Architect]"
OMNICLAW_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

KNOWLEDGE_DIR = os.path.join(OMNICLAW_ROOT, "brain", "knowledge")
ASSIMILATED_DIR = os.path.join(KNOWLEDGE_DIR, "assimilated_repos")
IDENTITY_PATH = os.path.join(ASSIMILATED_DIR, "_DIR_IDENTITY.md")
LIBRARY_GRAPH_PATH = os.path.join(KNOWLEDGE_DIR, "LIBRARY_GRAPH.json")

def process():
    if not os.path.exists(ASSIMILATED_DIR):
        print(f"\033[93m[{DAEMON_NAME}]\033[0m No assimilated repos directory found.")
        return

    # 1. Gather all DISTILLED markdown files
    files = [f for f in os.listdir(ASSIMILATED_DIR) if f.endswith('.md') and f != '_DIR_IDENTITY.md']
    if not files:
        print(f"\033[96m[{DAEMON_NAME}]\033[0m No distilled knowledge drops to map.")
        return

    # 2. Update Local _DIR_IDENTITY.md
    map_content = '\n\n## 🗺️ Knowledge Graph Map (Assimilated)\n\n'
    for f in files:
        name = f.replace('_DISTILLED.md', '')
        map_content += f'- `{name}` | type: `distilled_core` | registered: {datetime.datetime.now().isoformat()[:19]}\n'

    try:
        with open(IDENTITY_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
            if '## 🗺️ Knowledge Graph Map' in content:
                content = content.split('## 🗺️ Knowledge Graph Map')[0]
    except Exception:
        content = "---\nname: Assimilated Repositories\ntype: directory_identity\nowner: OA\n---\n# Assimilated Repos\nHouses highly compressed distilled knowledge md files.\n"

    with open(IDENTITY_PATH, 'w', encoding='utf-8') as f:
        f.write(content.strip() + map_content)

    # 3. Supercharge: Update LIBRARY_GRAPH.json Neural Network
    if os.path.exists(LIBRARY_GRAPH_PATH):
        print(f"[{DAEMON_NAME}] Connecting to Main Neural Graph -> {LIBRARY_GRAPH_PATH}")
        try:
            with open(LIBRARY_GRAPH_PATH, 'r', encoding='utf-8-sig') as gf:
                graph_data = json.load(gf)
            
            if 'nodes' not in graph_data:
                graph_data['nodes'] = []
            
            existing_ids = {node.get('id'): node for node in graph_data.get('nodes', [])}
            added_nodes = 0
            
            for f in files:
                repo_name = f.replace('_DISTILLED.md', '')
                node_id = f"assimilated_{repo_name.lower().replace('-', '_')}"
                
                # Check for existing node
                if node_id in existing_ids:
                    continue # Skip duplicates
                
                new_node = {
                    "id": node_id,
                    "type": "assimilated_core",
                    "name": f,
                    "title": f"Assimilated Knowledge: {repo_name}",
                    "path": f"brain/knowledge/assimilated_repos/{f}",
                    "tags": ["auto-assimilated", "oap_pipeline", "distilled"]
                }
                graph_data['nodes'].append(new_node)
                added_nodes += 1
            
            if added_nodes > 0:
                with open(LIBRARY_GRAPH_PATH, 'w', encoding='utf-8') as gf:
                    json.dump(graph_data, gf, indent=2, ensure_ascii=False)
                print(f"\033[92m[{DAEMON_NAME}]\033[0m Successfully injected {added_nodes} Neural Nodes into LIBRARY_GRAPH.json!")
            else:
                print(f"[{DAEMON_NAME}] All items already exist in the Graph. No update required.")
                
        except Exception as e:
            print(f"\033[91m[{DAEMON_NAME}]\033[0m FATAL ERROR injecting into Graph: {e}")

    print(f'\033[92m[{DAEMON_NAME}]\033[0m Cycle Complete. Mapped {len(files)} nodes to Local Identity.')

if __name__ == '__main__':
    process()
