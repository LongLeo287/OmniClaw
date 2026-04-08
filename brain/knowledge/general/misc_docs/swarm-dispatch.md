---
id: swarm-dispatch
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:19.426002
---

# Department: operations
---
description: Agent Swarm Mode dispatch protocol for OmniClaw Corp — parallel multi-agent task execution
---

# Agent Swarm Mode — Dispatch Protocol (RD-001)

## Concept

**Agent Swarm Mode** enables OmniClaw Corp to run tasks in parallel across specialized sub-agents, inspired by the Kimi K2.5 agentic swarm paradigm. Each swarm session spawns N concurrent mini-agents, each owning one task from the queue.

---

## Architecture

```
                    ┌──────────────────┐
                    │  SWARM CONDUCTOR │  ← Antigravity (Tier 1 Orchestrator)
                    │  (orchestrator)  │
                    └────────┬─────────┘
                             │
           ┌─────────────────┼─────────────────┐
           ▼                 ▼                 ▼
    ┌──────────┐      ┌──────────┐      ┌──────────┐
    │ Agent-A  │      │ Agent-B  │      │ Agent-C  │
    │ ENG task │      │ SEC task │      │ PMO task │
    └────┬─────┘      └────┬─────┘      └────┬─────┘
         │                 │                 │
         ▼                 ▼                 ▼
    ClawTask API ──────────────────────────────────→ Supabase DB
```

---

## Step 1: Swarm Trigger

```json
POST /api/swarm/dispatch
{
  "session_id": "SWARM-2026-03-20-001",
  "max_agents": 5,
  "filter": { "status": "todo", "priority": ["high", "critical"] }
}
```

---

## Step 2: Queue Pull

The conductor pulls tasks from `/api/tasks/queue` and assigns one task per agent:

```python
queue = GET /api/tasks/queue
agents = GET /api/agents  # active agents pool
assignment = zip(agents, queue[:max_agents])
```

---

## Step 3: Agent Execution Protocol

Each spawned agent follows the `AGENT_WORK_CYCLE`:

```
1. PULL:  GET /api/tasks/:id  → read task + briefing
2. START: PATCH /api/tasks/:id { status: "inprogress" }
3. EXECUTE: run task against codebase / file system / API
4. CLARIFY (if needed): POST /api/tasks/:id/clarification
5. DONE: PATCH /api/tasks/:id { status: "done", notes: "..." }
6. NOTIFY: auto-sent via telegram_notify on status change
```

---

## Step 4: Swarm Monitoring

```
GET /api/swarm/status → per-agent live status
GET /api/bot/digest   → summary for Telegram
```

---

## Cycle 5 PoC Implementation Plan

### Phase 1 (Mock Swarm)

Simulate with Antigravity acting as all 3 agents:

```
Swarm-001 [ENG-agent]:  C5-ENG-001 task
Swarm-002 [SEC-agent]:  C5-SEC-001 task  
Swarm-003 [PMO-agent]:  C5-PMO-001 task
```

### Phase 2 (Real Multi-Agent)

Requires multi-context execution support. Target: Cycle 6.

---

## Swarm Benefits

| Metric | Single-agent | Swarm (5 agents) |
|--------|-------------|-----------------|
| Tasks/cycle | ~10 | ~40-50 |
| Cycle duration | ~30-40 min | ~10-15 min |
| Throughput | 1x | 4-5x |

---

*RD-001 — R&D Dept | Agent: rd-chief-agent | Target: Cycle 5 PoC → Cycle 6 production*
