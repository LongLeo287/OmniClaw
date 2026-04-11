import os
from pathlib import Path

import os
__TEMP_ROOT__ = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))


ROOT_DIR = Path(__TEMP_ROOT__)
ECOSYSTEM_DIR = ROOT_DIR / "ecosystem"
REGIONAL_MAP = ECOSYSTEM_DIR / "_REGIONAL_MAP.md"

def generate_root_map():
    if not ECOSYSTEM_DIR.exists():
        return

    content = [
        "---",
        "id: ecosystem_master_map",
        "type: regional_map",
        "zone: ecosystem",
        "---",
        "",
        "# 🗺️ Master Ecosystem Geography",
        "",
        "> This index dynamically lists the major structural domains inside the `ecosystem` partition.",
        ""
    ]
    
    subdirs = [d.name for d in ECOSYSTEM_DIR.iterdir() if d.is_dir() and not d.name.startswith(('.', '__'))]
    subdirs.sort()

    content.append(f"## Primary Domains ({len(subdirs)})\n")
    
    # Specific descriptors mapping
    descriptors = {
        "skills": "The Passive Competency Warehouse (1900+ Prompts)",
        "tools": "The Active Armory (MCPs & Python Scripts)",
        "plugins": "The Cold Storage Library (3rd-party code & sandboxes)",
        "bridges": "The Harbor Layer (Docker compose triggers)",
        "ui_components": "Frontend UI/UX React assets",
        "workflows": "Hardcoded execution pipelines",
        "workforce": "Sub-agent identity rosters"
    }

    for d in subdirs:
        desc = descriptors.get(d, "System subsystem")
        content.append(f"### 📍 `{d}/`\n- **Role**: {desc}")
        
        # Check if there's a Registry or Regional Map inside to reference
        internal_reg = ECOSYSTEM_DIR / d / "_REGIONAL_MAP.md"
        if internal_reg.exists():
            content.append(f"- **Local Index**: [{d}/_REGIONAL_MAP.md]({d}/_REGIONAL_MAP.md)")
        content.append("")

    with open(REGIONAL_MAP, "w", encoding="utf-8") as f:
        f.write("\n".join(content))
        
    print(f"Ecosystem map regenerated at {REGIONAL_MAP.name}")

if __name__ == "__main__":
    generate_root_map()
