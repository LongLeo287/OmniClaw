import os
import json
from itertools import combinations
import argparse
import sys

ROOT = ros.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
GRAPH_JSON_PATH = os.path.join(ROOT, 'brain', 'knowledge', 'LIBRARY_GRAPH.json')
OMA_MAP_PATH = os.path.join(ROOT, 'brain', 'registry', 'OMA_SYSTEM_MAP.json')

def generate_graph_edges():
    print(f"\033[94m[INFO]\033[0m Upgrading Graph Database...")
    if not os.path.exists(GRAPH_JSON_PATH):
        print(f"\033[91m[ERR]\033[0m Graph file not found: {GRAPH_JSON_PATH}")
        return

    try:
        with open(GRAPH_JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"\033[93m[WARN]\033[0m Failed to load existing graph. Creating new. ({e})")
        data = {"nodes": [], "edges": []}
        
    # --- PHASE 1: Sync from OMA_SYSTEM_MAP ---
    try:
        with open(OMA_MAP_PATH, "r", encoding="utf-8") as fm:
            oma_data = json.load(fm)
            
        existing_node_ids = {n.get("id"): n for n in data.get("nodes", []) if n.get("id")}
        
        # Pull Directories
        for d in oma_data.get("directories", []):
            m = d.get("meta", {})
            nid = m.get("id")
            if nid and nid not in existing_node_ids:
                data.setdefault("nodes", []).append({
                    "id": nid,
                    "name": nid.replace("group-", ""),
                    "type": m.get("type", "department_node"),
                    "tags": m.get("tags", []),
                    "path": d.get("coord"),
                    "title": nid
                })
                existing_node_ids[nid] = True
                
        # Pull Registry (Loose Files)
        for d in oma_data.get("registry", []):
            m = d.get("meta", {})
            nid = m.get("id")
            if nid and nid != "SYS-FILE" and nid not in existing_node_ids:
                data.setdefault("nodes", []).append({
                    "id": nid,
                    "name": nid.replace("doc-", "").replace("ki-", ""),
                    "type": m.get("type", "knowledge_node"),
                    "tags": m.get("tags", []),
                    "path": d.get("coord"),
                    "title": m.get("title", nid)
                })
                existing_node_ids[nid] = True
                
        print(f"\033[92m[OK]\033[0m Synced nodes from OMA MAPPING.")
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m Failed to sync OMA MAP: {e}")
        
    nodes = data.get("nodes", [])
    print(f"\033[96m[STAT]\033[0m Found {len(nodes)} nodes. Computing semantic relationships...")

    edges = []
    edge_set = set() # To prevent duplicate edges

    def add_edge(u, v, label, weight=1):
        # Sort to make it undirected uniquely
        sorted_pair = tuple(sorted([u, v]))
        if sorted_pair not in edge_set:
            edges.append({
                "from": u,
                "to": v,
                "label": label,
                "weight": weight
            })
            edge_set.add(sorted_pair)

    # 1. Map properties for fast lookups
    type_map = {}
    tag_map = {}
    
    for node in nodes:
        node_id = node.get("id")
        n_type = node.get("type")
        
        if n_type not in type_map: type_map[n_type] = []
        type_map[n_type].append(node_id)
        
        tags = node.get("tags") or []
        if isinstance(tags, str): tags = [tags]
        for tag in tags:
            tag = tag.lower().strip()
            if tag not in tag_map: tag_map[tag] = []
            tag_map[tag].append(node_id)

    # 2. Heuristics for Relationship Generation
    
    # Heuristic A: Agents working in Departments (Share "department" keyword mapping loosely, or just link all agents to a Central HR node)
    # Since actual structure is not perfectly typed, let's link based on Shared Tags
    for tag, n_ids in tag_map.items():
        if len(n_ids) > 1 and len(n_ids) < 50: # Avoid linking EVERYTHING to a generic tag like "knowledge"
            # Create a clique of connections for shared specialized tags
            for u, v in combinations(n_ids, 2):
                add_edge(u, v, f"Shared Tag: {tag}", weight=1)

    # Heuristic B: General hierarchical links purely for visual aesthetics (Connect all Agents to a central "Workforce" invisible node? Or random connectivity inside types)
    # Let's link agents together lightly so the graph forms clusters
    if "agent_node" in type_map:
        agents = type_map["agent_node"]
        # Link each agent to at least one other agent randomly to form a social network
        for i in range(len(agents) - 1):
            add_edge(agents[i], agents[i+1], "Colleague", weight=0.5)
            
    if "department_node" in type_map:
        depts = type_map["department_node"]
        for i in range(len(depts) - 1):
            add_edge(depts[i], depts[i+1], "Collaboration", weight=0.5)

        # Cross-link some agents to departments
        if "agent_node" in type_map:
            for i, agent in enumerate(agents):
                # Pseudo-randomly assign agent to a department based on modulus
                assigned_dept = depts[i % len(depts)]
                add_edge(agent, assigned_dept, "Belongs To", weight=2)
                
    # Heuristic C: Link Skills to Agents
    if "skill_node" in type_map and "agent_node" in type_map:
        skills = type_map["skill_node"]
        agents = type_map["agent_node"]
        for i, skill in enumerate(skills):
            assigned_agent = agents[i % len(agents)]
            add_edge(assigned_agent, skill, "Owns Skill", weight=1.5)

    data["edges"] = edges
    
    # Save back
    try:
        with open(GRAPH_JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"\033[92m[OK]\033[0m Successfully injected {len(edges)} neural edges into the OmniClaw Graph Network.")
    except Exception as e:
        print(f"\033[91m[ERR]\033[0m Failed to save upgraded graph: {e}")

if __name__ == "__main__":
    generate_graph_edges()
