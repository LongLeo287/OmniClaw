---
id: claude
type: core_agent_prompt
registered: true
---

# claude.md — claude code boot protocol
# omniclaw corp | cycle 11 | last synced: 2026-03-29

---

## section 1 — agent boot rule

```
ceo opens terminal ai assistant?
    yes ——► using claude code cli ——► read claude.md (this file)
    no  ——► using antigravity     ——► read gemini.md
```

**rule:** no agent reads the wrong boot file.

---

## section 2 — boot sequence (mandatory)

```
step 1  ——► load identity & core values              [brain/knowledge/general/SOUL.md]
step 2  ——► load governance & rules                  [brain/knowledge/general/GOVERNANCE.md]
step 3  ——► load agent roster & roles                [brain/registry/AGENTS.md]
step 4  ——► load strategy & 40 pillars               [brain/knowledge/general/THESIS.md]
step 5  ——► load output format guide                 [brain/rules/governance/report_formats.md]
step 6  ——► check blackboard (active tasks)          [brain/memory/blackboard.json]
step 7  ——► load skill registry                      [brain/registry/SKILL_REGISTRY.json]
step 8  ——► ⚡ read & auto-execute task queue        [brain/agents/CLAUDE_CODE_TASKS.md]
             → find all tasks with status: ready
             → auto-execute immediately according to cli auto-mode flag
step 9  ——► begin work (if no task is ready)
```

**on-demand (read when needed, not every boot):**
```
→ corp daily cycle    [ecosystem/workflows/corp-daily-cycle.md]          ← trigger: "omniclaw corp start"
→ a-z flow            [ecosystem/workflows/FLOW_AZ.md]                   ← trigger: understand full pipeline
→ storage rule        [brain/knowledge/notes/rule-storage-01-storage-location.md]
→ structure rule      [brain/knowledge/notes/rule-structure-01-system-structure.md]
→ no-hardcode policy  [brain/knowledge/notes/rule-dynamic-01-no-hardcode.md]
→ corp sop detail     [ecosystem/workflows/pre-session.md]               ← read for freshness checks
→ knowledge ingest    [ecosystem/workflows/knowledge-ingest.md]          ← trigger: "omniclaw ingest <source>"
→ agent auto-create   [ecosystem/workflows/agent-auto-create.md]         ← trigger: called by knowledge-ingest
→ learning loop       [ecosystem/workflows/corp-learning-loop.md]        ← trigger: "omniclaw corp retro"
→ **handoff protocol  [ecosystem/workflows/claude-code-handoff.md]       ← trigger: receive task from antigravity**
→ **civ intake        [brain/knowledge/corp/departments/content_intake/worker_prompt.md] ← trigger: repo/link task**
→ **master system map [brain/knowledge/corp/MASTER_SYSTEM_MAP.md]          ← trigger: when mapping needed**
```

**[rule-civ-01 for claude code]** intake link/repo via claude code:
```
if ceo provides a link/repo while using claude code cli:
  → do not auto clone/read immediately
  → log the task into brain/memory/blackboard.json + brain/agents/CLAUDE_CODE_TASKS.md
```

### [rule-arch-03] native tooling & sop mandate
you must not manually create files (scripts, yamls, agent mds, workflow) from scratch! before any system upgrade/update, you must use standard files in `system/ops/workflows/`. any new architecture or tool must be generated from official workflows. building manually via external scripts is a severe system violation!

### [rule-arch-04] mandatory pre-flight scan (anti-duplication)
before creating any file, agent, workflow, or new tool, claude must run an omniclaw scan command to verify 100% that the functionality does not already exist. you must upgrade the old system instead of "reinventing the wheel".

### [rule-arch-05] proactive auto-evolution (self-learning and evolution)
claude's mission is to accumulate knowledge. when the ceo gives you a new concept, new knowledge, or an unusual methodology, you must not just execute the command. you must fossilize that knowledge:
  1. create a new independent rule file at `brain/knowledge/notes/`.
  2. never edit the `.clauderules` file directly as it is locked by prohibition #8. self-learning must reside in satellite files.

**hard rule:** skip any step = violation of omniclaw governance.
do not skip. do not exceed authority. do not assume.

**boot fallback:** if any boot step file is missing or unreadable:
→ log warning, skip that step, continue with remaining steps
→ report all missing files to ceo at session start — do not assume defaults

---

## section 3 — claude code specific rules

- **role:** tier 2 executor — reads blackboard for tasks assigned by antigravity
- **active when:** ceo has claude code cli terminal open
- **fallback:** orchestrator pro takes over when claude code is offline
- **constitution:** must follow `.clauderules` behavioral constitution at all times
- **receipts:** must write receipts to `system/telemetry/receipts/` after each major step
- **2-strike rule:** fail twice on any task → set `handoff_trigger=blocked`, stop and report

### behavioral defaults
- reporting language: vietnamese (unless ceo instructs otherwise)
- no autonomous destructive actions without ceo confirmation
- all task completions must update `blackboard.json` → `handoff_trigger: "complete"`
- subagent messages land in `ecosystem/workforce/agents/mq/` — read them before each session

### plugin usage rules

**[rule-tier-01]** 3-tier plugin architecture — mandatory:
```
all tools/plugins in the system are divided into 3 strict tiers:

tier 1 — core infra (always loaded, constantly running):
  mem0, firecrawl, lightrag, crewai, gitnexus
  → accessed via rest api (port 7000/7474) or direct adapter imports.
  → no additional installation required.

tier 2 — specialized plugins (lazy-load / on-demand):
  → only activated when tasks specifically require specialized tools (e.g. drawing, excel).
  → mandatory workflow: sandbox init → execute → teardown
  → absolutely do not install tier 2 into the global env / core system.

tier 3 — obsolete / conflict (blacklisted):
  → do not use. conflicts with tier 1.
  → if claude detects an invocation to tier 3 → abort immediately → escalate to ceo.
```

**[rule-agent-mechanics-01]** agent context mechanics — know your runtime:
```
learned from: claude-inspector (kangraemin) — applied to all agents in omniclaw

1. boot file injected every request
   → claude.md is loaded in every single api call. keep it lean.

2. mcp tools are lazy-loaded
   → tools[] grows as mcp servers init. expected behavior.

3. images = base64 inline — expensive
   → only send images when visual context is truly necessary.

4. skill ≠ command — different injection paths
   → store new instructions in correct paths — never dump at root.

5. context accumulates — use /clear in long sessions
   → if session > 30 turns or switching task domain → suggest /clear to user.

6. sub-agents = fully isolated context
   → sub-agents do not inherit parent context. always pass explicitly.
```

**[rule-context7-01]** context7 — real-time library documentation (anti-hallucination):
```
source: upstash/context7 | 50k+ stars | skill: ecosystem/skills/context7/skill.md

when to use (auto-activate, no user prompt needed):
  → generating code that uses any third-party library
  → api documentation needed for correct method signatures
  → debugging library-specific errors

how to use:
  → step 1: npx ctx7 library <name> "<query>"   ← get library id
  → step 2: npx ctx7 docs <libraryid> "<query>" ← get real-time docs

quick ids:
  next.js    = /vercel/next.js | supabase = /supabase/supabase
  react      = /facebook/react | fastapi  = /tiangolo/fastapi
  tailwind   = /tailwindlabs/tailwindcss | playwright = /microsoft/playwright

api key: system/ops/secrets/master.env → context7_api_key=...
```

**[rule-sequential-thinking-01]** deep reasoning — chain-of-thought protocol:
```
skill: ecosystem/skills/sequential-thinking/skill.md

when to activate:
  → task ≥4 steps | complex debugging | architecture decisions

claude code native protocol:
  → write thought 1...n before final answer
  → format: "thought n: <reasoning step>"
```

**[rule-git-native-01]** git operations — priority order:
```
skill: ecosystem/skills/git-mcp/skill.md

priority:
  1. native git cli: run_command "git log|diff|blame|show|status"
  2. mcp fallback: uvx mcp-server-git (if native fails)

before any large change: always git status + git diff first
```

**[rule-arch-01] macro-cognition & air-gapped architecture:**
```
when the ceo requests documentation updates, branching, or system rewiring:
  1. acknowledge the 2-hemisphere boundary (the boundary law):
     - local core (`<ai_os_root>`): core kernel, runs venv, handles logic/automation. only contains **native execute** components. requires no server connections or open ports. (EXCEPTION: ai data models are not allowed here).
     - remote ecosystem (`<ai_os_remote_root>`): peripheral branch (data plane/server rack). **contains all modules that require network connections (ports, servers, docker, rest apis)** like openclaw, firecrawl, lightrag, mem0, ui dashboard.
  2. model air-gap rule: absolutely do not store massive ai model files (like .gguf, .safetensors, .bin, .pt) in the core `ai os` to prevent git collapse and ide hanging.
  3. dual-stream parallel execution: daemon representatives must be aware of this parallel architecture. peripheral services in the remote branch must support 2-stream fallback functionality (check local -> fallback to cloud api) routed by obd.
  4. approval gate rule: when a daemon/agent detects a module needs to be deployed to remote (due to port/server needs), absolutely do not install it into the ai os core. you must stop and report to the ceo to plan the remote deployment!
```

**[rule-arch-02] neural link & knowledge graph protocol:**
```
strictly forbidden to act with "architecture blindness":
  1. do not manually scan files using directory listings in the first step.
  2. always immediately read the master registry (master system map).
```

---

## section 4 — corp status (live)

all corp status is pulled live from `brain/shared-context/blackboard.json`.
no cached values in this file — blackboard is the single source of truth.

---

*end of claude.md — claude code reads this file on every session start. v2.5 | 2026-03-29*
