import os
import shutil

AGENTS_DIR = r"D:\OmniClaw\ecosystem\workforce\agents"

guards = {
    "osf_warden": {
        "name": "Warden of OSF (Hải Quan Trưởng)",
        "description": "Trưởng ban quản lý Firewall vòng đệm. Đảm bảo toàn bộ Script, Pipeline và Đặc vụ tuân thủ ISLAND_SANDBOX_PROTOCOL.",
        "tools": ["oma_sandbox_auditor.py", "oma_sandbox_fixer.py"]
    },
    "osf_auditor": {
        "name": "OSF Supply Chain Auditor",
        "description": "Thanh tra nội bộ cục OSF. Càn quét mảng Supply Chain Dependencies.",
        "tools": ["os_file_locker.py", "oma_sandbox_auditor.py"]
    },
    "osf_quarantine_guard": {
        "name": "OSF Quarantine Guard",
        "description": "Cảnh vệ canh gác vùng QUARANTINE thắt chặt quyền sinh sát các File Độc hại.",
        "tools": ["os_quarantine_manager.py", "virus_total_scan.py"]
    }
}

WATERMARK = "\n---\n*Created by OmniClaw OS Martial Law workflow. OSF Supreme Security Override.*"

for g_id, g_data in guards.items():
    dpath = os.path.join(AGENTS_DIR, g_id)
    os.makedirs(dpath, exist_ok=True)
    
    # Generate _DIR_IDENTITY.md
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

    # Generate AGENT.md
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
    
    print(f"Created Identity and Agent profile for: {g_id}")
    
    # Delete the old yaml file if it exists
    old_yaml = os.path.join(AGENTS_DIR, f"{g_id}.yaml")
    if os.path.exists(old_yaml):
        os.remove(old_yaml)
        print(f"Deleted old stray YAML: {g_id}.yaml")

print("OSF Guardians properly assimilated.")
