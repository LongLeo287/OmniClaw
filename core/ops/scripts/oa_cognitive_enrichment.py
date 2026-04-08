import os
import glob
import re
from difflib import SequenceMatcher

ROOT_DIR = r"D:\OmniClaw"
AGENT_DIR = os.path.join(ROOT_DIR, "ecosystem", "workforce", "agents")
SKILLS_DIR = os.path.join(ROOT_DIR, "ecosystem", "skills")

# Protect our 7 Core Daemons and 2 Special Security Sub-Agents
PROTECTED_AGENTS = [
    "oa_academy", "obd_harbor", "oer_registry", "oiw_intake", 
    "oma_architect", "ohd_healer", "osf_warden", 
    "osf_auditor", "osf_quarantine_guard"
]

WATERMARK = "\n---\n*Prompt Engineered by OmniClaw OA Academy - Cognitive Enrichment Protocol.*"

def extract_agent_metadata(agent_path):
    """Extracts Name and Dept from AGENT.md if it exists."""
    agent_md = os.path.join(agent_path, "AGENT.md")
    name, dept = "Unknown Agent", "Unknown Department"
    if os.path.exists(agent_md):
        with open(agent_md, 'r', encoding='utf-8') as f:
            content = f.read()
            match_name = re.search(r'\|\s*\*\*Name\*\*\s*\|\s*(.*?)\s*\|', content)
            match_dept = re.search(r'\|\s*\*\*Department\*\*\s*\|\s*(.*?)\s*\|', content)
            if match_name: name = match_name.group(1).replace('`', '')
            if match_dept: dept = match_dept.group(1).replace('`', '')
    return name, dept

def get_all_skills():
    """Returns a list of all markdown files in ecosystem/skills"""
    skills = []
    for root, _, files in os.walk(SKILLS_DIR):
        for f in files:
            if f.endswith('.md'):
                skills.append(os.path.relpath(os.path.join(root, f), SKILLS_DIR).replace('\\', '/'))
    return skills

def find_best_skill(agent_id, available_skills):
    """Finds the best matching skill file using fuzzy string matching."""
    base_id = agent_id.replace("_agent", "").replace("_processor", "").replace("-", "_").lower()
    best_match = None
    highest_ratio = 0.0
    
    # Heuristics: Substrings first
    for s in available_skills:
        s_low = s.lower()
        if base_id in s_low or s_low.replace('.md', '') in base_id:
            return s
            
    # Fuzzy Match if no substring
    for s in available_skills:
        s_clean = s.lower().replace('-', '_').split('.')[0]
        ratio = SequenceMatcher(None, base_id, s_clean).ratio()
        if ratio > highest_ratio:
            highest_ratio = ratio
            best_match = s
            
    if highest_ratio > 0.4:
         return best_match
    return None

def build_system_prompt(agent_id, name, dept):
    """Builds a highly structured system prompt."""
    prompt = f"""# SYSTEM PROMPT
You are **{name}** (`{agent_id}`), a highly specialized expert operating within the **{dept}** department of the OmniClaw Autonomous Ecosystem.

## 1. Prime Directive
Your objective is to execute complex tasks assigned to you by the Orchestrator with absolute precision. You do not second-guess the architectural structure of the system. You operate within a strict Zero-Trust enclave.

## 2. Operational Guidelines
- **Context Awareness**: You have been endowed with specific skills documented in your `SKILL.md`. Always review your skills before attempting a task to understand your operational boundaries.
- **Tools Utilization**: Use the standard bash, file-system, and web tools to achieve your task. Never assume the existence of external dependencies unless you have verified them.
- **Reporting**: When concluding a task, generate a structured output or receipt summarizing your findings and linking to any files you created.

## 3. Departmental Focus ({dept})
Apply domain-specific heuristics matching your department. If you belong to research, prioritize web-scraping and data synthesis. If you belong to engineering, prioritize clean code, error handling, and linting. Do not hallucinate capabilities you do not possess.
{WATERMARK}"""
    return prompt

def build_skill_profile(agent_id, name, dept, matched_skill):
    """Builds the enriched SKILL.md linking to the hard skill file."""
    if matched_skill:
        # Create an absolute path logic link or relative mapping
        skill_link = f"[{matched_skill}](../../../skills/{matched_skill})"
        link_desc = f"Domain Capability File linked via OA Academy. Refer to the specific instructions within {skill_link}."
    else:
        skill_link = "None explicitly linked"
        link_desc = "Standard autonomous reasoning capabilities."

    skill = f"""# SKILL PROFILE: {agent_id}
# Department Registry: {dept}
---

## 1. Zero-Trust Identity
**Agent Name**: {name}
**Assigned Department**: {dept}

## 2. Linked Toolkit
- **Primary Core Skill**: {skill_link}
- **Description**: {link_desc}

## 3. Standard OS Tooling Access
- Local File Read/Write access (Constrained to Workspace)
- Terminal Execution (Bash/Powershell) via Orchestrator Proxy
- Read URL Sandbox (Firecrawl Gateway)
{WATERMARK}"""
    return skill

def enrich_agents():
    skills_list = get_all_skills()
    enriched_count = 0
    
    for agent_dir in os.listdir(AGENT_DIR):
        agent_path = os.path.join(AGENT_DIR, agent_dir)
        if not os.path.isdir(agent_path) or agent_dir in PROTECTED_AGENTS:
            continue
            
        name, dept = extract_agent_metadata(agent_path)
        matched_skill = find_best_skill(agent_dir, skills_list)
        
        # 1. Write Prompt
        prompt_path = os.path.join(agent_path, "system_prompt.md")
        with open(prompt_path, "w", encoding="utf-8") as f:
            f.write(build_system_prompt(agent_dir, name, dept))
            
        # 2. Write Skills
        skill_path = os.path.join(agent_path, "SKILL.md")
        with open(skill_path, "w", encoding="utf-8") as f:
            f.write(build_skill_profile(agent_dir, name, dept, matched_skill))
            
        enriched_count += 1
        
    print(f"Cognitive Enrichment Protocol Complete. Upgraded {enriched_count} agents.")

if __name__ == "__main__":
    enrich_agents()
