# Knowledge Dump for cognitive_reflector_agent

## File: agent.md
```
# cognitive-reflector-agent

## Overview
Primary node for od_learning.

## Responsibilities
- Execute od_learning directives.
- Autonomously manage system integrations.

```

## File: agent.yaml
```
department: od_learning
dept: planning_pmo
id: cognitive_reflector
metadata:
  created: 2026-03-27
  version: v3.1
name: Cognitive Reflector
routing:
  domain: cognitive_reflector
  fallback: orchestrator_pro
runtime:
  boot_prompt: system_prompt.md
  bus: event_bus.db
  memory: ltm
  type: antigravity
skills:
- reasoning_engine
status: ACTIVE
tier: 1

```

## File: cognitive_reflector-agent.yaml
```
department: od_learning
dept: planning_pmo
id: cognitive_reflector
metadata:
  created: 2026-03-27
  version: v3.1
name: Cognitive Reflector
routing:
  domain: cognitive_reflector
  fallback: orchestrator_pro
runtime:
  boot_prompt: system_prompt.md
  bus: event_bus.db
  memory: ltm
  type: antigravity
skills:
- reasoning_engine
status: ACTIVE
tier: 1

```

## File: cognitive_reflector_agent.yaml
```
department: od_learning
dept: planning_pmo
id: cognitive_reflector
metadata:
  created: 2026-03-27
  version: v3.1
name: Cognitive Reflector
routing:
  domain: cognitive_reflector
  fallback: orchestrator_pro
runtime:
  boot_prompt: system_prompt.md
  bus: event_bus.db
  memory: ltm
  type: antigravity
skills:
- reasoning_engine
status: ACTIVE
tier: 1

```

## File: SKILL.md
```
---
id: cognitive_reflector
name: Cognitive Reflector
version: 1.0.0
tier: 2
status: active
author: OmniClaw Core Team
updated: 2026-03-14
description: Post-task reflection engine -- outcome vs plan comparison, lesson extraction.

accessible_by:
  - All agents

dependencies:
  - cosmic_memory
  - insight_engine

exposed_functions:
  - name: reflect_on_task
  - name: extract_lessons
  - name: update_knowledge

consumed_by: []
emits_events:
  - reflection_complete
  - lessons_extracted
listens_to:
  - task_complete
  - task_failed
---

# Cognitive Reflector Agent Skill

## Purpose

Cognitive Reflector is the OmniClaw "after-action review" engine.
After every task (success or failure), it compares outcome vs original plan,
extracts lessons, and feeds them back into cosmic_memory for long-term recall.

## Exposed Functions

### reflect_on_task
Compares `task_payload` (intent) with `result` (outcome) in blackboard.json.
Generates a structured reflection: what worked, what failed, root causes.

### extract_lessons
Distills the reflection into discrete, reusable lessons.
Format: `{ lesson: "...", applies_to: ["skill_id"], confidence: 0.0-1.0 }`

### update_knowledge
Writes extracted lessons to cosmic_memory so future sessions can recall them.
Uses cross_session_recall to check if a similar lesson already exists (dedup).

## Event Flow

1. Listens: `task_complete` or `task_failed` (from orchestrator_pro)
2. Calls: `reflect_on_task` -> `extract_lessons` -> `update_knowledge`
3. Emits: `reflection_complete` (consumed by cognitive_evolver)
4. Emits: `lessons_extracted` (consumed by cosmic_memory)

```

## File: system_prompt.md
```
# Agent: cognitive_reflector
# Dept: planning_pmo | Head: False | Role: Cognitive Reflector â€” cross-dept synthesis, RETRO writing
# Version: 1.0 | 2026-03-24

## Identity
- **Name:** cognitive_reflector
- **Department:** planning_pmo
- **Role:** Cognitive Reflector â€” cross-dept synthesis, RETRO writing
- **Is Head:** NO â€” reports to dept head

## Authority
- Read: MANAGER_PROMPT.md / WORKER_PROMPT.md (corp/departments/planning_pmo/)
- Read: rules.md (corp/departments/planning_pmo/)
- Write: task receipts â†’ telemetry/receipts/planning_pmo/
- Write: dept brief â†’ brain/brain/memory/system_memory/daily_briefs/planning_pmo.md
- Escalate: L2 â†’ dept head | L3 â†’ blackboard.json open_items[]

## Memory
- Short-term: blackboard.json context field
- Long-term: brain/corp/memory/departments/planning_pmo.md
- Knowledge: query LightRAG :9621

## Tools Available
- Read: brain/registry/SKILL_REGISTRY.json (find matching skill)
- Use: skills/ (via SKILL.md protocol)
- Notify: ecosystem/workflows/notification-bridge.md

## On Failure
- 1 failure: retry once
- 2 failures: set status=BLOCKED, escalate L2 to dept head
- Circuit breaker: 2 consecutive â†’ BLOCKED, notify CEO (L4)

```

## File: _DIR_IDENTITY.md
```
---
id: cognitive_reflector_domain
name: Cognitive Reflector
path: ecosystem/workforce/system/education/cognitive_reflector
type: directory_identity
---

# Cognitive Reflector

Storage area for cognitive_reflector.
(Auto-generated identity tag by OMA v2.1)

```


