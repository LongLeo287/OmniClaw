import os
import yaml
import shutil
from pathlib import Path

DEPT_ROOT = Path(r"D:\OmniClaw\ecosystem\workforce\departments")

def upgrade_departments():
    converted_count = 0
    
    for item in DEPT_ROOT.iterdir():
        if item.is_file() and item.name.endswith(".yaml"):
            dept_id = item.name.replace(".yaml", "")
            
            # Read real config from YAML
            try:
                with open(item, "r", encoding="utf-8") as f:
                    config = yaml.safe_load(f)
            except Exception as e:
                print(f"Error reading {item.name}: {e}")
                continue
                
            # If the config has a wrapper 'department', extract it.
            if "department" in config:
                dept_data = config["department"]
            else:
                dept_data = config
            
            # Make sure directory exists
            dept_dir = DEPT_ROOT / dept_id
            dept_dir.mkdir(exist_ok=True)
            
            # Delete any hallucinated Identity file
            identity_file = dept_dir / "_DIR_IDENTITY.md"
            
            name = dept_data.get("name", dept_id.upper())
            
            # Write correct Identity
            with open(identity_file, "w", encoding="utf-8") as f:
                f.write(f"---\n")
                f.write(f"id: {dept_id}\n")
                f.write(f"type: department\n")
                f.write(f"version: 2.0.0\n")
                f.write(f"---\n")
                
            # Compile Department.md from YAML stats
            dept_md_file = dept_dir / "DEPARTMENT.md"
            
            # Reconstruct workforce
            workers_md = ""
            workers_list = config.get("workforce", [])
            if workers_list:
                for w in workers_list:
                    if isinstance(w, str):
                        aid = w
                        arole = "Worker"
                        astatus = "active"
                    else:
                        aid = w.get("agent_id", "Unknown")
                        arole = w.get("role", "Worker")
                        astatus = w.get("status", "active")
                    workers_md += f"- **{aid}** ({astatus}): *{arole}*\n"
            else:
                workers_md = "- No designated workforce.\n"
                
            # Reconstruct Leadership
            leader_md = "N/A"
            leaders = config.get("leadership", {})
            if isinstance(leaders, dict):
                leader_md = leaders.get("manager", "Unknown Manager")
                
            tools_data = config.get("tools_and_capabilities", {})
            skills = tools_data.get("skills", []) if isinstance(tools_data, dict) else []
            plugins = tools_data.get("plugins", []) if isinstance(tools_data, dict) else []
            
            md_content = f"# {name}\n\n"
            md_content += f"## Leadership\n- **Manager**: {leader_md}\n\n"
            md_content += f"## Workforce Roster\n{workers_md}\n"
            
            if skills or plugins:
                md_content += f"## Core Capabilities\n"
                if skills: md_content += f"- **Skills**: {', '.join(skills)}\n"
                if plugins: md_content += f"- **Plugins**: {', '.join(plugins)}\n"
                md_content += "\n"
                
            md_content += f"*Created by OmniClaw OS department-auto-create workflow. Supervised until first performance review.*\n"
            
            # Write markdown
            with open(dept_md_file, "w", encoding="utf-8") as f:
                f.write(md_content)
                
            # Delete old yaml
            try:
                os.remove(item)
            except Exception as e:
                print(f"Warning: could not delete {item.name}: {e}")
                
            converted_count += 1
            print(f"Upgraded: {dept_id}")

    print(f"Total departments converted: {converted_count}")

if __name__ == "__main__":
    upgrade_departments()
