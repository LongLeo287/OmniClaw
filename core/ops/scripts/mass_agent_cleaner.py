import os

AGENTS_DIR = r"D:\OmniClaw\ecosystem\workforce\agents"
WATERMARK = "\n\n*Agent node certified by OmniClaw OS Martial Law OSF scan. Supervised until first review.*"

def process_agent(agent_folder):
    path = os.path.join(AGENTS_DIR, agent_folder)
    
    # 1. Provide missing stubs
    identity_path = os.path.join(path, "_DIR_IDENTITY.md")
    agent_path = os.path.join(path, "AGENT.md")
    
    if not os.path.exists(identity_path):
        content = f"""---
node_type: "agent"
node_id: "{agent_folder}"
node_name: "{agent_folder.title().replace('_', ' ')}"
status: "active"
---

# {agent_folder.title().replace('_', ' ')}
Recovered agent node by OSF Martial Law.
{WATERMARK}
"""
        with open(identity_path, "w", encoding="utf-8") as f:
            f.write(content)
            
    if not os.path.exists(agent_path):
        content = f"""# {agent_folder.title().replace('_', ' ')}
# Status: ACTIVE

## Identity
| Field | Value |
|-------|-------|
| **ID** | `{agent_folder}` |
| **Name** | {agent_folder.title().replace('_', ' ')} |
| **Department** | unassigned |

## Role & Scope
Recovered agent metadata by OmniClaw OS pipeline.

{WATERMARK}
"""
        with open(agent_path, "w", encoding="utf-8") as f:
            f.write(content)

    # 2. Fix Legacy texts
    for root, _, files in os.walk(path):
        for file in files:
            if not file.endswith('.md'):
                continue
            
            fpath = os.path.join(root, file)
            try:
                with open(fpath, "r", encoding="utf-8") as f:
                    data = f.read()
                
                changed = False
                if "OmniClaw Corp" in data:
                    data = data.replace("OmniClaw Corp", "OmniClaw OS")
                    changed = True
                if "brain/corp" in data:
                    data = data.replace("brain/corp", "brain/knowledge")
                    changed = True
                
                if changed:
                    with open(fpath, "w", encoding="utf-8") as f:
                        f.write(data)
            except Exception as e:
                pass # Skip files with severe errors (images, or true binaries disguised as .md)

if __name__ == "__main__":
    count = 0
    dirs = [d for d in os.listdir(AGENTS_DIR) if os.path.isdir(os.path.join(AGENTS_DIR, d))]
    for d in dirs:
        process_agent(d)
        count += 1
    
    print(f"Purification Pipeline Completed. Assessed and sanitized {count} agent nodes.")
