---
id: capability_legacy_forgers
name: OmniClaw Structural Forger Toolkit
type: operational_capability
owner: OA Academy / OER Daemon
authorized_agents: ["backend-architect-agent", "registry-manager-agent"]
status: active
---

# Capability Profile: Legacy Forgers

## Overview
This toolkit provides the OmniClaw system with native capabilities to dynamically scaffold rigid system files (`AGENT.md`, `SKILL.md`, `system_prompt.md`). It bypasses the need for manual file templating by generating highly compliant profiles in bulk.

## Core Assets
1. `agent_generator.js`
   - **Purpose**: Generates Tier-1, Tier-2, and Tier-3 Agent configurations.
   - **Command Line Interface**: `node core/ops/scripts/legacy_forgers/agent_generator.js <agent_name> <tier> <department>`

2. `skill_creator_ultra.js`
   - **Purpose**: Generates open-standard SKILL.md configurations for plugins and internal workflows.
   - **Command Line Interface**: `node core/ops/scripts/legacy_forgers/skill_creator_ultra.js <skill_name>`

## OA Academy Integration Workflow
When OA (OmniClaw Academy) successfully analyzes a new repository (`_assimilate_repo`) and determines that a new Agent or Skill must be forged (`_forge_capabilities`), OA can invoke these scripts (via the `run_command` tool assigned to `backend-architect-agent`) instead of natively prompting LLMs to write the file structure line-by-line. This guarantees 100% adherence to OmniClaw architecture standards.
