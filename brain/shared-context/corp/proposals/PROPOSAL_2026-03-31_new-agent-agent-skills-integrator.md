---
proposal_id: PROPOSAL-2026-03-31-001
status: DRAFT
created: 2026-03-31T01:21:39
knowledge_source: KI-agent-skills-repo
---

# Agent Proposal: Microsoft Agent Skills Integrator

## Role
Manage, package and provide skill libraries to load directly into Agents of the OmniClaw ecosystem.

## Why needed
Gap identified: Lack of a central Hub or integration processing expert to extract skills from the microsoft/agent-skills repo into standard OmniClaw plugin form.
Source: brain/knowledge/processed_repos/agent-skills_knowledge.md

## Proposed agent ID
agent-skills-integrator

## Department
engineering — reports to arch-chief-agent

## Skills required
- git_operations (YES)
- python_ast_parser (NO)
- skill_registry_manager (YES)

## Tools / permissions needed
- Read input output from Python repo agent-skills code
- Grant Write permission to SKILL_REGISTRY.json and system/plugins/ folder

## LLM tier
balanced

## Autonomy level
supervised

## KPIs
- Number of Agents successfully injected with new skills
- Speed ​​of parsing and adapting skill code (seconds/skill)

## Sample tasks
1. Extract skill "Browser Control" from microsoft repo and turn it into OmniClaw plugin.
2. Updated SKILL_REGISTRY.json to share skill permissions for star-office-agent.

## Integration
- Reads from: brain/knowledge/processed_repos/agent-skills_knowledge.md
- Writes to: system/plugins/, SKILL_REGISTRY.json
- Reports to: arch-chief-agent
