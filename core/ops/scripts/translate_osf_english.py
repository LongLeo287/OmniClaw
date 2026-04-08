import os

AGENTS_DIR = r"D:\OmniClaw\ecosystem\workforce\agents"

guards = {
    "osf_warden": {
        "name": "Warden of OSF",
        "description": "Chief administrator of the buffer Firewall. Ensures that all Scripts, Pipelines, and Agents strictly comply with the ISLAND_SANDBOX_PROTOCOL.",
        "tools": ["oma_sandbox_auditor.py", "oma_sandbox_fixer.py"]
    },
    "osf_auditor": {
        "name": "OSF Supply Chain Auditor",
        "description": "Internal inspector of the OSF sector. Performs deep scans on Supply Chain Dependencies and malicious payloads.",
        "tools": ["os_file_locker.py", "oma_sandbox_auditor.py"]
    },
    "osf_quarantine_guard": {
        "name": "OSF Quarantine Guard",
        "description": "Security guard of the QUARANTINE zone. Enforces absolute control over isolated malicious files.",
        "tools": ["os_quarantine_manager.py", "virus_total_scan.py"]
    }
}

WATERMARK = "\n---\n*Created by OmniClaw OS Martial Law workflow. OSF Supreme Security Override.*"

for g_id, g_data in guards.items():
    dpath = os.path.join(AGENTS_DIR, g_id)
    os.makedirs(dpath, exist_ok=True)
    
    identity = f"""---
node_type: "agent"
node_id: "{g_id}"
node_name: "{g_data['name']}"
department: "gateway_border_security"
status: "active"
---

# {g_data['name']}
{g_data['description']}
""" + WATERMARK

    tools_str = ", ".join([f"`{t}`" for t in g_data['tools']])
    agent = f"""# AGENT: {g_data['name']}
# Department: gateway_border_security
# Status: ACTIVE 

## Identity
| Field | Value |
|-------|-------|
| **ID** | `{g_id}` |
| **Name** | {g_data['name']} |
| **Department** | gateway_border_security |
| **Loyalty** | OSF (OmniClaw Sandbox Firewall) |

## Role & Scope
{g_data['description']}

## Tools 
{tools_str}

## Autonomy
`autonomy_level: supreme-firewall`
""" + WATERMARK

    with open(os.path.join(dpath, "_DIR_IDENTITY.md"), 'w', encoding='utf-8') as f:
        f.write(identity)
    
    with open(os.path.join(dpath, "AGENT.md"), 'w', encoding='utf-8') as f:
        f.write(agent)
        
print("Updated agents to pure English.")

# Fix DEPARTMENT.md in gateway_border_security
dept_file = r"D:\OmniClaw\ecosystem\workforce\departments\gateway_border_security\DEPARTMENT.md"

dept_content = """# GATEWAY BORDER SECURITY (OSF)

## Leadership
- **Manager**: osf-firewall-daemon

## Workforce Roster
- **osf_warden** (active): *Warden of OSF*
- **osf_auditor** (active): *OSF Supply Chain Auditor*
- **osf_quarantine_guard** (active): *OSF Quarantine Guard*

## Core Capabilities
- **Skills**: oma_sandbox_auditor, oma_sandbox_fixer, os_file_locker, virus_total_scan

*Gateway_border_security Department - Created by OmniClaw OS Martial Law workflow. OSF Supreme Security Override.*
"""

with open(dept_file, 'w', encoding='utf-8') as f:
    f.write(dept_content)
print("Updated department file to pure English.")
