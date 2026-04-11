---
id: rule-structure-01-system-structure
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.199113
---

# [RULE-STRUCTURE-01] OmniClaw System & Data Structure
# Issued by: CEO LongLeo | Date: 2026-03-22 | Status: MANDATORY
# Scope: All agents â€” Antigravity, Claude Code, Orchestrator Pro, all Corp workers
# NOTE: No hardcoded paths per RULE-DYNAMIC-01. Use relative paths from AI_OS_ROOT.

---

## 1. SYSTEM STRUCTURE â€” Agent Tiers

```
TIER 0: CEO (Human â€” LongLeo)
         â”‚
TIER 1: ANTIGRAVITY (Orchestrator â€” Gemini)
         Boot: GEMINI.md
         â”‚
TIER 2: CLAUDE CODE CLI (Executor â€” only when terminal open)
         Boot: CLAUDE.md
         Fallback: ORCHESTRATOR PRO (when Claude Code offline)
         â”‚
TIER 3: SPECIALIST AGENTS (Corp Dept Workers)
         N departments â€” count from corp/org_chart.yaml (do NOT hardcode)
         â”‚
TIER 4: SUBAGENTS (spawned per task)
```

**Rule:** Higher tier ALWAYS overrides lower tier.
**Rule:** Antigravity + Claude Code share the SAME project workspace â€” different boot file, same data.

---

## 2. DATA STRUCTURE â€” Source of Truth

> **AI_OS_ROOT** = directory containing GEMINI.md + CLAUDE.md (discovered at boot, NOT hardcoded)
> All paths below are RELATIVE to AI_OS_ROOT.

```
$OMNICLAW_ROOT/                             â† PROJECT ROOT (Source of Truth for ALL agents)
â”‚
â”œâ”€â”€ GEMINI.md                             â† Antigravity boot entry point
â”œâ”€â”€ CLAUDE.md                             â† Claude Code boot entry point
â”‚
â”œâ”€â”€ brain/
â”‚   â”œâ”€â”€ brain/memory/                â† SHARED â€” all agents read/write
â”‚   â”‚   â”œâ”€â”€ blackboard.json            â† Active task state (ALL agents sync here)
â”‚   â”‚   â”œâ”€â”€ AGENTS.md                  â† Agent roster & authority
â”‚   â”‚   â”œâ”€â”€ SOUL.md                    â† Platform identity
â”‚   â”‚   â”œâ”€â”€ GOVERNANCE.md              â† Safety anchors & rules
â”‚   â”‚   â”œâ”€â”€ THESIS.md                  â† 34 Pillars
â”‚   â”‚   â””â”€â”€ SKILL_REGISTRY.json        â† All skills index
â”‚   â”‚
â”‚   â”œâ”€â”€ skills/                        â† Skill definitions (all agents load on demand)
â”‚   â”‚   â””â”€â”€ [skill-name]/SKILL.md
â”‚   â”‚
â”‚   â””â”€â”€ knowledge/                     â† Reference library (all agents read)
â”‚       â”œâ”€â”€ notes/                     â† CEO notes + rules (RULE-*.md)
â”‚       â””â”€â”€ repos/, web/, brain/knowledge/docs_legacy/...     â† KI artifacts
â”‚
â”œâ”€â”€ corp/
â”‚   â”œâ”€â”€ memory/
â”‚   â”‚   â”œâ”€â”€ global/                    â† Cross-dept decisions, decisions_log.md
â”‚   â”‚   â”œâ”€â”€ agents/                    â† Per-agent memory (notebook_agent.md, etc.)
â”‚   â”‚   â””â”€â”€ departments/               â† Per-dept cycle memory
â”‚   â”‚
â”‚   â”œâ”€â”€ departments/                   â† N dept configs + rules + MANAGER_PROMPT (see org_chart.yaml)
â”‚   â”œâ”€â”€ sops/                          â† Standard Operating Procedures
â”‚   â”‚   â””â”€â”€ workflows/                 â† Workflow definitions
â”‚   â””â”€â”€ prompts/                       â† Agent prompt templates
â”‚
â”œâ”€â”€ infra/
â”‚   â””â”€â”€ llm/
â”‚       â””â”€â”€ router.yaml                â† LLM routing rules (all agents use)
â”‚
â”œâ”€â”€ ops/
â”‚   â”œâ”€â”€ runtime/                       â† Runtime state (ephemeral, not for boot)
â”‚   â”‚   â”œâ”€â”€ notebooks/                 â† Notebook agent store
â”‚   â”‚   â””â”€â”€ blackboard.json            â† OPS MIRROR ONLY (not source of truth)
â”‚   â”œâ”€â”€ scripts/config.json            â† Service URLs (ports, endpoints)
â”‚   â””â”€â”€ workflows/                     â† Boot + daily cycle workflows
â”‚
â”œâ”€â”€ tools/
â”‚   â”œâ”€â”€ clawtask/                      â† ClawTask API server (port 7474)
â”‚   â”‚   â”œâ”€â”€ module_*.py                â† Feature modules
â”‚   â”‚   â””â”€â”€ tests/                     â† CI/CD tests (run only when port 7474 UP)
â”‚   â””â”€â”€ mcp/                           â† MCP servers (Antigravity + Claude)
â”‚
â”œâ”€â”€ plugins/                           â† External plugins (vetted via Dept: CIV)
â””â”€â”€ channels/                          â† Remote bridges (Telegram, Discord, Zalo)
    â””â”€â”€ telegram_bridge.py             â† Telegram (only active when service running)
```

> Paths in this diagram are RELATIVE to AI_OS_ROOT. See RULE-DYNAMIC-01 for discovery rules.

---

## 3. CRITICAL PATHS â€” Agents Must Know

| Data | Path | Who reads |
|------|------|-----------|
| **Blackboard (primary)** | `brain/memory/blackboard.json` | ALL agents at boot |
| **Blackboard (ops mirror)** | `ops/runtime/blackboard.json` | Runtime only, NOT at boot |
| **LLM routing** | `infra/llm/router.yaml` | All agents when calling LLM |
| **Service config** | `ops/scripts/config.json` | Modules needing service URLs |
| **Agent memory** | `corp/memory/agents/<name>.md` | Agent on session start |
| **Dept memory** | `corp/memory/departments/<dept>.md` | Dept head at Phase 3 |
| **Skills** | `ecosystem/skills/<name>/SKILL.md` | Worker on task start |
| **CI/CD tests** | `tools/clawtask/tests/` | Only when port 7474 UP |
| **Telegram** | `channels/telegram_bridge.py` | Only when service connected |

---

## 4. AGENT DATA DOMAINS

| Agent | Reads | Writes |
|-------|-------|--------|
| **Antigravity** | All project files | blackboard, corp/memory, proposals, daily_briefs |
| **Claude Code** | All project files | code files, telemetry/receipts, blackboard (handoff) |
| **Corp Workers** | dept config + memory + skills | receipts, dept memory, blackboard updates |
| **Notebook Agent** | content input, blackboard | ops/runtime/notebooks/, blackboard (primary) |

---

## 5. SERVICE AVAILABILITY GATES

```
Service         Port    Active when
â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€
ClawTask API    7474    Docker running OR direct python start
9router         20128   Docker running
Ollama          11434   Ollama app running
Open-notebook   5055    Docker running (full mode only)
Telegram bot    3000    nullclaw bot service running
```

**Rule: Always check if service is UP before using it. Never assume.**
- CI/CD tests â†’ only run if `localhost:7474` responds
- Telegram notify â†’ only fire if `localhost:3000` OR `/api/telegram/test` responds
- LLM calls â†’ use router.yaml for fallback chain (9router â†’ Ollama â†’ extractive)

---

## 6. SYNCHRONIZATION RULES

- **blackboard.json** is the ONLY cross-agent state sync channel
- Notebook agent writes to `brain/memory/blackboard.json` â†’ all agents see it
- `ops/runtime/blackboard.json` = runtime operation mirror only (NOT for boot reads)
- **receipts** go to `telemetry/receipts/<dept>/<task-id>.json`
- **proposals** go to `brain/memory/system_memory/proposals/PROPOSAL_<date>_<topic>.md`

---

*Issued: 2026-03-22 | All agents must load this after RULE-STORAGE-01 during boot*

