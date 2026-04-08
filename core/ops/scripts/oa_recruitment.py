import os
from pathlib import Path

ROOT = Path(r"D:\OmniClaw\ecosystem\workforce\departments")

EMPTY_SHELLS = ["facility", "hr", "system_daemons", "ux_design"]
UNDERSTAFFED = ["gateway_border_security", "it_infra", "od_learning", "orchestration", "planning_pmo", "system_health"]

WATERMARK = "\n\n---\n*Created by OmniClaw OS OA Academy workflow. Supervised until first performance review.*"

def build_dept_pipeline(dept_name):
    dept_path = ROOT / dept_name
    dept_path.mkdir(exist_ok=True)
    
    # Generate rules.md
    rules = f"""# {dept_name.upper()} — Department Rules
# Version: 1.0 | Builder: OA Academy
# Applies in addition to: ecosystem/workforce/rules/manager_rules.md

## DEPT DOMAIN RULES

RULE {dept_name.upper()[:3]}-01: AUTHORIZED SCOPE
  Agents in this department are strictly limited to {dept_name} operations.
  Out of bounds actions will trigger security_grc alerts.

RULE {dept_name.upper()[:3]}-02: QUALITY ASSURANCE
  All deliverables must pass internal self-reflection before submission.
""" + WATERMARK

    # Generate MANAGER_PROMPT.md
    mgr_prompt = f"""# {dept_name.capitalize()} — Dept Manager Prompt
# Head: {dept_name}-lead-agent

<{dept_name.upper()}_MANAGER_PROMPT>

## DEPT IDENTITY
Dept: {dept_name.upper()}
Mission: Handle core operations and orchestration for {dept_name} functionalities.
Your team: [Pending Allocation]

## TASK ASSIGNMENT RULES
- Managers do not execute terminal tasks. Delegate to workers.
- Verify all outputs against `rules.md` before returning to Orchestrator.

</{dept_name.upper()}_MANAGER_PROMPT>
""" + WATERMARK

    # Generate WORKER_PROMPT.md
    wkr_prompt = f"""# {dept_name.capitalize()} — Dept Worker Prompt

<{dept_name.upper()}_WORKER_PROMPT>

## WORKER PIPELINE
You are an execution unit for the {dept_name} department.

## AUTHORIZED TOOLS
- File System access
- Department-specific plugins (Ask manager for capability map)

</{dept_name.upper()}_WORKER_PROMPT>
""" + WATERMARK

    # Update DEPARTMENT.md to include leader
    dept_md = dept_path / "DEPARTMENT.md"
    if dept_md.exists():
        content = dept_md.read_text('utf-8')
        # If leader is missing, inject it
        if "Unknown" in content or "Manager**:" not in content:
            content = content.replace("Manager**: Unknown", f"Manager**: {dept_name}-lead-agent")
            content = content.replace("Manager**:", f"Manager**: {dept_name}-lead-agent")
        dept_md.write_text(content, 'utf-8')

    # Write files
    (dept_path / "rules.md").write_text(rules, 'utf-8')
    (dept_path / "MANAGER_PROMPT.md").write_text(mgr_prompt, 'utf-8')
    (dept_path / "WORKER_PROMPT.md").write_text(wkr_prompt, 'utf-8')
    
    print(f"[OA] Bootstrapped pipeline for: {dept_name}")

def recruit_leaders(depts):
    for dept_name in depts:
        dept_md = ROOT / dept_name / "DEPARTMENT.md"
        if dept_md.exists():
            content = dept_md.read_text('utf-8')
            if "Unknown" in content:
                content = content.replace("Manager**: Unknown", f"Manager**: {dept_name}-lead-agent")
                dept_md.write_text(content, 'utf-8')
                print(f"[OA] Recruited Manager for {dept_name}: {dept_name}-lead-agent")

print("--- OA Academy Recruitment & Reconstruction ---")
for dept in EMPTY_SHELLS:
    build_dept_pipeline(dept)

recruit_leaders(UNDERSTAFFED)

print("OA Reconstruction Complete.")
