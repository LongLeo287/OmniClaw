import os
import json
from pathlib import Path
from collections import defaultdict

ROOT_DIR = Path(os.getenv("OMNICLAW_ROOT", Path(__file__).resolve().parents[2]))
SKILLS_DIR = ROOT_DIR / "ecosystem" / "skills"
REGISTRY_FILE = SKILLS_DIR / "SKILL_REGISTRY.json"
ECOSYSTEM_GRAPH = SKILLS_DIR / "_ECOSYSTEM_GRAPH.md"
REGIONAL_MAP = SKILLS_DIR / "_REGIONAL_MAP.md"

def generate_maps():
    if not REGISTRY_FILE.exists():
        print("Error: SKILL_REGISTRY.json not found.")
        return 1

    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        registry = json.load(f)

    # 1. Generate Regional Map (Alphabetical Index)
    regional_content = [
        "# 🗺️ OmniClaw Regional Map (Alphabetical Index)",
        "> **Total Active Skills**: " + str(len(registry)),
        "> **Standard enforced**: `snake_case` (Python Standard)\n"
    ]

    alphabet_groups = defaultdict(list)
    for skill_id in sorted(registry.keys()):
        first_char = skill_id[0].upper()
        if not first_char.isalpha():
            first_char = "#"
        alphabet_groups[first_char].append(skill_id)

    for letter in sorted(alphabet_groups.keys()):
        regional_content.append(f"## 📍 Cluster [{letter}]")
        for skill in alphabet_groups[letter]:
            regional_content.append(f"- `{skill}`")
        regional_content.append("")

    with open(REGIONAL_MAP, "w", encoding="utf-8") as f:
        f.write("\n".join(regional_content))

    # 2. Generate Ecosystem Graph (Prefix Hubs)
    graph_content = [
        "# 🕸️ Ecosystem Topological Graph",
        "> **Skill Segmentation by Functional Hub (Clans/Families)**",
        "> This topology maps the OmniClaw network utilizing prefix-based major tech hubs.\n"
    ]

    # Find common prefixes (e.g., azure_, odoo_, seo_, huggging_face_)
    prefix_groups = defaultdict(list)
    for skill_id in sorted(registry.keys()):
        parts = skill_id.split('_')
        if len(parts) > 1:
            # We group by the first token if it's common enough, else "General"
            prefix = parts[0]
            prefix_groups[prefix].append(skill_id)
        else:
            prefix_groups["core_standalone"].append(skill_id)

    # Filter out small groups to avoid noise in the graph, but keep them visible in a catch-all section.
    major_hubs = {k: v for k, v in prefix_groups.items() if len(v) >= 5}
    minor_hubs = {k: v for k, v in prefix_groups.items() if len(v) < 5}

    for hub, skills in sorted(major_hubs.items(), key=lambda x: len(x[1]), reverse=True):
        graph_content.append(f"## 🏢 {hub.upper()} Ecosystem (Count: {len(skills)})")
        graph_content.append("```text\n[Ecosystem-HUB]")
        for skill in skills:
            graph_content.append(f" ├── {skill}")
        graph_content.append("```\n")

    if minor_hubs:
        graph_content.append("## 🌱 Emerging / Standalone Skills")
        for hub, skills in sorted(minor_hubs.items()):
            graph_content.append(f"- `{hub}`: {', '.join(skills)}")

    with open(ECOSYSTEM_GRAPH, "w", encoding="utf-8") as f:
        f.write("\n".join(graph_content))

    print(f"Successfully generated Regional Map ({REGIONAL_MAP.name}) and Ecosystem Graph ({ECOSYSTEM_GRAPH.name}).")
    return 0

if __name__ == "__main__":
    raise SystemExit(generate_maps())
