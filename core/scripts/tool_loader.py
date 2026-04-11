import os
import json
import logging
import sys
from pathlib import Path

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

ROOT_DIR = Path(os.getenv("OMNICLAW_ROOT", Path(__file__).resolve().parents[2])).resolve()
TOOLS_DIR = ROOT_DIR / "ecosystem" / "tools"
REGISTRY_FILE = TOOLS_DIR / "TOOL_REGISTRY.json"
REGIONAL_MAP = TOOLS_DIR / "_REGIONAL_MAP.md"

def build_tool_registry():
    registry = {}
    valid_tools = []
    invalid_tools = []
    
    if not TOOLS_DIR.exists():
        logging.error(f"Tools directory not found: {TOOLS_DIR}")
        return 1

    # Crawl tools
    for item in TOOLS_DIR.iterdir():
        if item.is_dir() and not item.name.startswith("_") and item.name != "tool_template":
            tool_id = item.name
            schema_path = item / "schema.json"
            
            if schema_path.exists():
                try:
                    with open(schema_path, "r", encoding="utf-8-sig") as f:
                        schema_data = json.load(f)
                        # Add relative physical path if not exists
                        if "path" not in schema_data:
                            schema_data["path"] = f"$OMNICLAW_ROOT\\ecosystem\\tools\\{tool_id}"
                        registry[tool_id] = schema_data
                        valid_tools.append(tool_id)
                except Exception as e:
                    invalid_tools.append(tool_id)
                    logging.error(f"Failed to parse {schema_path}: {e}")
            else:
                invalid_tools.append(tool_id)
                logging.warning(f"Tool {tool_id} is missing schema.json. Skipping.")

    # Write Master Registry
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=4)

    logging.info(f"Registry compiled successfully into {REGISTRY_FILE.name} with {len(registry)} tools.")
    
    # Generate Regional Map
    generate_regional_map(valid_tools)
    if invalid_tools:
        logging.error("Registry build completed with %s invalid tools skipped.", len(invalid_tools))
        return 1
    return 0

def generate_regional_map(tools_list):
    regional_content = [
        "---",
        "id: tools_regional_map",
        "type: regional_map",
        "zone: ecosystem/tools",
        "---",
        "",
        r"# _REGIONAL_MAP — $OMNICLAW_ROOT\ecosystem\tools",
        "",
        f"## Integrated Tools ({len(tools_list)})",
        "| ID | Type | Validated |",
        "|---|---|---|"
    ]
    
    for tool in sorted(tools_list):
        regional_content.append(f"| `{tool}` | Registered | OK |")
        
    regional_content.extend([
        "",
        "## System Files",
        "- `TOOL_SPEC.md`",
        "- `_DIR_IDENTITY.md`",
        "- `README.md`"
    ])
    
    with open(REGIONAL_MAP, "w", encoding="utf-8") as f:
        f.write("\n".join(regional_content))
    logging.info("Regional map regenerated.")

if __name__ == "__main__":
    raise SystemExit(build_tool_registry())
