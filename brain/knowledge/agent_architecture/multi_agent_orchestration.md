---
id: multi-agent-orchestration
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.445664
---

# Multi-Agent Orchestration — Knowledge Base

## Description
Advanced coordination strategies for collaborative AI systems, focusing on context isolation and scoped execution. Derived from `openclaw-multi-agent-kit`.

## Key Concepts
1. **Scoped Brains:** Isolating agent memory and workspaces to prevent context rot.
2. **Channel Routing:** Directing tasks based on agent specialization and toolsets.
3. **Agent-to-Agent (A2A) Interaction:** Allowing agents to invoke each other for sub-tasks.

## Implementation in OmniClaw
- Upgrade `orchestrator_rules.md`.
- Implement sub-workspace partitioning in `tasks/`.
