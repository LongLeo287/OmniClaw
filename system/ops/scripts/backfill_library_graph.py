#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent.parent.parent
LIBRARY_GRAPH = ROOT / "brain" / "knowledge" / "LIBRARY_GRAPH.json"
AGENTS_DIR = ROOT / "ecosystem" / "workforce" / "agents"
DEPT_DIR = ROOT / "ecosystem" / "workforce" / "departments"

def main():
    if not LIBRARY_GRAPH.exists():
        print("LIBRARY_GRAPH.json not found")
        return
        
    try:
        data = json.loads(LIBRARY_GRAPH.read_text(encoding="utf-8"))
        nodes = data.get("nodes", [])
        edges = data.get("edges", [])
        existing_ids = {n["id"] for n in nodes}
        
        # 1. Backfill Agents
        added_agents = 0
        if AGENTS_DIR.exists():
            for agent_dir in AGENTS_DIR.iterdir():
                if not agent_dir.is_dir() or agent_dir.name.startswith("_"):
                    continue
                    
                agent_id = agent_dir.name
                node_id = f"AGENT-{agent_id}"
                if node_id not in existing_ids:
                    # determine tier
                    tier = 3
                    # Try reading AGENT.md to find tier
                    agent_md = agent_dir / "AGENT.md"
                    if agent_md.exists():
                        txt = agent_md.read_text(encoding="utf-8", errors="ignore")
                        if "Tier: 2" in txt or "tier: 2" in txt: tier = 2
                        if "Tier: 1" in txt or "tier: 1" in txt: tier = 1
                        
                    new_node = {
                        "id": node_id,
                        "type": "agent_node",
                        "name": agent_id,
                        "title": f"AGENT PROFILE: {agent_id}",
                        "path": f"ecosystem/workforce/agents/{agent_id}/SKILL.md",
                        "tags": ["agent", "workforce", f"tier{tier}"]
                    }
                    nodes.append(new_node)
                    existing_ids.add(node_id)
                    added_agents += 1
                    
        # 2. Backfill Departments
        added_depts = 0
        if DEPT_DIR.exists():
            for dept_dir in DEPT_DIR.iterdir():
                if not dept_dir.is_dir(): continue
                
                dept = dept_dir.name
                node_id = f"DEPT-{dept}"
                if node_id not in existing_ids:
                    new_node = {
                        "id": node_id,
                        "type": "department_node",
                        "name": dept,
                        "title": f"DEPARTMENT: {dept}",
                        "path": f"ecosystem/workforce/departments/{dept}/rules.md",
                        "tags": ["department", "org_chart"]
                    }
                    nodes.append(new_node)
                    existing_ids.add(node_id)
                    added_depts += 1
                    
        data["nodes"] = nodes
        data["edges"] = edges
        LIBRARY_GRAPH.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Done backfilling. Added {added_agents} agents and {added_depts} departments to LIBRARY_GRAPH.json.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
