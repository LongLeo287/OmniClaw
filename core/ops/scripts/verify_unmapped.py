import os
import json

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GRAPH_JSON = os.path.join(ROOT, 'brain', 'knowledge', 'LIBRARY_GRAPH.json')

def main():
    if not os.path.exists(GRAPH_JSON):
        print(f"Graph not found: {GRAPH_JSON}")
        return

    with open(GRAPH_JSON, "r", encoding="utf-8") as f:
        graph = json.load(f)

    # Normalize graph mapped paths
    graph_paths = set()
    for n in graph.get('nodes', []):
        p = n.get('path', '')
        if p:
            # normalize forward/backward slashes
            p_norm = os.path.normpath(p).replace('\\', '/')
            graph_paths.add(p_norm)

    all_files = []
    # Check what is inside brain and ecosystem
    for d in ['brain', 'ecosystem']:
        for r, _, files in os.walk(os.path.join(ROOT, d)):
            for f in files:
                if f.endswith(('.md', '.json', '.py', '.txt')):
                    abs_path = os.path.join(r, f)
                    rel_path = os.path.relpath(abs_path, ROOT)
                    rel_norm = rel_path.replace('\\', '/')
                    all_files.append(rel_norm)

    unmapped = [p for p in all_files if p not in graph_paths]
    
    print(f"Total nodes in Graph: {len(graph_paths)}")
    print(f"Total potential files in brain & ecosystem: {len(all_files)}")
    print(f"Total UNMAPPED files: {len(unmapped)}")
    
    print("\nSample Unmapped:")
    for um in unmapped[:30]:
        print(f" - {um}")

if __name__ == "__main__":
    main()
