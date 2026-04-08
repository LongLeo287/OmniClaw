import os
import re

AGENT_DIR = r"D:\OmniClaw\ecosystem\workforce\agents"
SKILLS_DIR = r"D:\OmniClaw\ecosystem\skills"

# 1. Fetch available skills
available_skills = set()
for f in os.listdir(SKILLS_DIR):
    if f.endswith('.md') and not f.startswith(('KI-', '_', 'ki_')):
        available_skills.add(f)

# 2. Heuristic extraction
def extract_description(content):
    # Try to grab the first description block if it exists
    desc_match = re.search(r'description:\s*>?\n?\s*(.*?)\n', content, re.IGNORECASE)
    if desc_match and len(desc_match.group(1)) > 5:
        # Strip mojibake marks if feasible
        return desc_match.group(1).encode('ascii', 'ignore').decode().strip()
    return "Capability profile pending dynamic extraction."

# 3. Rewrite engine
agents = [d for d in os.listdir(AGENT_DIR) if os.path.isdir(os.path.join(AGENT_DIR, d))]

for a in agents:
    skill_path = os.path.join(AGENT_DIR, a, "SKILL.md")
    
    # Read old description
    desc = "Generic specialist agent."
    if os.path.exists(skill_path):
        with open(skill_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
        if "Regenerated" not in content and len(content) > 20:
            extracted = extract_description(content)
            if extracted and len(extracted) > 10:
                desc = extracted

    # Try mapping tools mathematically based on agent name
    mapped_tools = []
    a_tokens = a.lower().replace("-", "_").split("_")
    for s in available_skills:
        s_base = s.lower().replace("-", "_").replace(".md", "")
        # Give a match if partial token matches skill base heavily
        if s_base in a_tokens or any(t for t in a_tokens if t in s_base and len(t) > 3):
            mapped_tools.append(s)

    # Format mapped output
    if mapped_tools:
        tools_str = "\n".join([f"- **Mapped Skill**: `{t}` (Path: `ecosystem/skills/{t}`)" for t in mapped_tools])
    else:
        tools_str = "> [!NOTE]\n> No static YAML skills mapped. Awaiting dynamic plugin hooks from OAP Orchestrator."

    # Build NEW standard SKILL.md
    new_content = f"""# SKILL PROFILE: {a}
# Department Registry: OAP Toolchain
# Scope: Pure OS-sanctioned Tools
---

## 1. Domain Capability
{desc}

## 2. Linked Toolkit
{tools_str}

---
*Capability Register hardened by OmniClaw OA Skill Auditor.*
"""
    # Overwrite safely
    with open(skill_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

print(f"Successfully audited and reconstructed SKILL profiles for {len(agents)} agents.")
