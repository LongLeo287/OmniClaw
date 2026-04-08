# TEMPLATE: OmniClaw OS Standard Department Node

Every department within `ecosystem/workforce/departments/` MUST conform to this exact architecture. A department is a logical orchestration Node, not a physical code repository. It acts as the Operating Procedure and Access Control List (ACL) for agents working under its domain.

## 1. `_DIR_IDENTITY.md` (Formal Registry Tag)
This file is the passport. It tells OmniClaw daemons that this folder is a standard structural node.
```yaml
---
id: <dept_name>
type: department
name: <Human-Readable Department Name>
---
```

## 2. `DEPARTMENT.md` (Domain Overview & Roster)
This is the index node outlining the department's purpose, leader, and personnel roster mapping.
**Required Fields:**
- `Department`: Name of the department.
- `Objective`: High level mission.
- `Manager`: Target agent ID that runs this node (e.g., `hr_people-lead-agent`).
- `Roster`: List of agents mapped to this department, denoting their exact ID and status.
- `Capabilities`: List of skills/MCP links it has access to.

## 3. `MANAGER_PROMPT.md` (Dept Head Pipeline)
The system instruction for the Manager agent.
**Content Requirements:**
- Must extend base `corp/prompts/MANAGER_PROMPT.md`
- Outlines Task Routing Logic (which worker gets which task).
- Defines QA/Gate rules for outputs.

## 4. `WORKER_PROMPT.md` (Staff Execution Pipeline)
The system instruction bounds that restrict workers inside this department.
**Content Requirements:**
- Defines what Skills/MCP plugins this department is authorized to invoke.
- Formatting rules for task completion receipts.

## 5. `rules.md` (Disciplinary Matrix)
The strict behavioral rules for agents in this domain.
- Must contain enumerated rules (e.g., `RULE HR-01: NO UNAUTHORIZED TERMINATION`).
- Outlines exact penal actions if rules are broken (e.g., `Violation = Escalation to system_integrity`).

---
*OmniClaw OS Department Design Master - Created by OA Academy.*
