import os

AGENT_DIR = r"D:\OmniClaw\ecosystem\workforce\agents"
DEPT_FILE = r"D:\OmniClaw\ecosystem\workforce\departments\system_daemons\DEPARTMENT.md"

daemons_meta = {
    "oa_academy": {
        "name": "OA Academy Daemon",
        "description": "Supreme educational and rule orchestrator. Bootstraps missing elements, governs neural bus, and dictates task routing.",
        "skills": ["oa_academy.py", "oa_heuristics.py"],
        "autonomy": "supreme-academy"
    },
    "oma_architect": {
        "name": "OMA Architect Daemon",
        "description": "Master Map Architect. Synthesizes graph structures and cross-links workforce pathways to OAP pipeline.",
        "skills": ["oma_architect.py", "oma_synapse.py"],
        "autonomy": "supreme-architect"
    },
    "obd_harbor": {
        "name": "OBD Bridge Daemon",
        "description": "Sub-process Harbor Master. Controls execution contexts and daemon bridging APIs to external runtimes.",
        "skills": ["obd_harbor.py"],
        "autonomy": "supreme-bridge"
    },
    "oer_registry": {
        "name": "OER Registry Daemon",
        "description": "Global validation orchestrator. Authenticates identity protocols, issues certificates, and enforces OAP naming structures.",
        "skills": ["oer_registry.py"],
        "autonomy": "supreme-registry"
    },
    "oiw_intake": {
        "name": "OIW Intake Daemon",
        "description": "Web Fetcher and Repo crawler. Pulls down knowledge from civilization repos into sandbox intake before mapping.",
        "skills": ["oiw_intake.py"],
        "autonomy": "supreme-intake"
    }
}

WATERMARK = "\n---\n*Created by OmniClaw OS Martial Law workflow. Zero-Trust Policy Enforced.*"

for d_id, meta in daemons_meta.items():
    d_path = os.path.join(AGENT_DIR, d_id)
    os.makedirs(d_path, exist_ok=True)
    
    # 1. Identity
    identity = f"""---
node_type: "agent"
node_id: "{d_id}"
node_name: "{meta['name']}"
department: "system_daemons"
status: "active"
---

# {meta['name']}
{meta['description']}
{WATERMARK}"""
    with open(os.path.join(d_path, "_DIR_IDENTITY.md"), "w", encoding="utf-8") as f:
        f.write(identity)
        
    # 2. Agent
    agent = f"""# AGENT: {meta['name']}
# Department: system_daemons
# Status: ACTIVE 

## Identity
| Field | Value |
|-------|-------|
| **ID** | `{d_id}` |
| **Name** | {meta['name']} |
| **Department** | system_daemons |
| **Loyalty** | OmniClaw OS |

## Role & Scope
{meta['description']}

## Tools 
{', '.join([f'`{s}`' for s in meta['skills']])}

## Autonomy
`autonomy_level: {meta['autonomy']}`
{WATERMARK}"""
    with open(os.path.join(d_path, "AGENT.md"), "w", encoding="utf-8") as f:
        f.write(agent)

    # 3. Prompt
    sys_prompt = f"""# SYSTEM PROMPT
You are the {meta['name']} ({d_id.upper()}).
Your primary role is to act as a Core Daemon enforcing system-level logic.

Rules of operation:
- Never break Zero-Trust boundaries.
- Produce fully compliant task receipts to the OAP pipeline.
- If errors arise, escalate to OA/OHD.
{WATERMARK}"""
    with open(os.path.join(d_path, "system_prompt.md"), "w", encoding="utf-8") as f:
        f.write(sys_prompt)

    # 4. SKILL.md
    skills_fmt = "\n".join([f"- **Real Skill**: `{s}` (Mapped directly to core daemon script)" for s in meta['skills']])
    skill = f"""# SKILL PROFILE: {d_id}
# Department Registry: system_daemons
---

## 1. Domain Capability
{meta['description']}

## 2. Linked Toolkit
{skills_fmt}
- **Stubbed Skill**: AI Dynamic Execution -> [WARNING: AI LOGIC IS MOCKED OR HANDLED BY SUBAGENTS]

---
*Capability Register hardened by OmniClaw OA Skill Auditor.*"""
    with open(os.path.join(d_path, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(skill)

print(f"Formalized {len(daemons_meta)} daemons successfully.")

# Mop up the DEPARTMENT.md to reflect the EXACT roster.
new_dept = """# OSD (OmniClaw System Daemons)

## Leadership
- **Manager**: oma_architect

## Workforce Roster
- **oa_academy** (active): *Supreme educational and rule orchestrator.*
- **oma_architect** (active): *Master Map Architect.*
- **obd_harbor** (active): *Sub-process Harbor Master.*
- **oer_registry** (active): *Global validation orchestrator.*
- **oiw_intake** (active): *Web Fetcher and Repo crawler.*

## Core Capabilities
- **Skills**: deep_scan, fast_trace

*System_daemons Department - Reconstructed by OmniClaw OS Martial Law workflow. Zero-Trust Policy Enforced.*"""

with open(DEPT_FILE, "w", encoding="utf-8") as f:
    f.write(new_dept)

print("Updated system_daemons DEPARTMENT.md roster.")
