# [AGENT_NAME_PLACEHOLDER]

# Template Version: 1.0.0

# Status: DRAFT / ACTIVE

## 1. Identity & Routing

| Field          | Value                                        |
| -------------- | -------------------------------------------- |
| **ID**         | `agent_id_lowercase`                         |
| **Name**       | Agent Formal Name                            |
| **Department** | `department_id` (Mandatory for OAP Pipeline) |
| **Loyalty**    | OmniClaw OS                                  |

## 2. Role & Scope

[Detail the exact professional boundaries and capabilities of this agent. What happens if this agent is missing? Define its zero-trust limits.]

## 3. Toolkit & Skills

- **Skill 1**: [skill_id] - [Description]
- **Skill 2**: [skill_id] - [Description]
  _(Tools mapped here must physically exist in `ecosystem/tools` or `ecosystem/skills`)_

## 4. OAP Pipeline Hooks

- **Upstream (Input)**: Which agent or directory provides input?
- **Downstream (Output)**: Where does this agent save its output?

---

### Checklist for Fully Valid Agent:

- [ ] Has `_DIR_IDENTITY.md`
- [ ] Has `AGENT.md` (This file)
- [ ] Has `system_prompt.md` (System Instructions)
- [ ] Listed in a Department's `DEPARTMENT.md` Roster
- [ ] Passed OSF Firewall Checks

_Created by OmniClaw OS Standard Templates._
