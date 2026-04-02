---
id: claude_code_tasks
type: core_agent_prompt
registered: true
---

# CLAUDE_CODE_TASKS.md — Task Queue for Claude Code Auto-Execution
# Read by CLAUDE.md STEP 9 on every boot session
# Format: One task per block. Status: READY | IN_PROGRESS | DONE | BLOCKED

---

## Queue

### TASK-003
Status: DONE
Priority: HIGH
Assigned: mcp-health-agent → dependency-audit-agent
Description: |
  Check Ollama online, then create a LightRAG instance.
  Step 1: Check if http://localhost:11434 responds.
  Step 2: If online → call POST http://localhost:9621/init
  Step 3: Verify GET http://localhost:9621/health → rag_initialized: true
  Step 4: Log results into blackboard.json field "lightrag_status"
Blocker: Ollama must be running with model gemma2:2b and nomic-embed-text
Manual_check: Run `ollama list` to verify available models before this task runs

### TASK-004
Status: DONE
Priority: MEDIUM
Assigned: pmo-agent → registry-sync-agent
Description: |
  Run SYSTEM_INDEX registry scanner again to update the 15 new entities
  from Task-001 and Task-002 have not been indexed.
  Command: python system/ops/scripts/registry_indexer.py
  Expected: total_entities increased from 356 (placeholder) to actual value
  Output: brain/registry/SYSTEM_INDEX.yaml (overwrite)
  After: Update omniclaw_system_index.total_entities in header

### TASK-005
Status: DONE
Priority: MEDIUM
Assigned: pmo-agent → backend-architect-agent → cost-manager-agent
Description: |
  Activate the 5 highest priority placeholder agents (according to the priority list from activation_status.json).
  For each agent:
    1. Read the role from brain/agents/<name>.md (or create it if you don't have one)
    2. Write MANAGER_PROMPT.md and WORKER_PROMPT.md for that agent's dept
    3. Update activation_status.json: status PLACEHOLDER → ACTIVE
    4. Test by assigning a small task
  Priority order:
    1. growth-agent (Dept 04 Marketing — no head agent)
    2. channel-agent (Dept 05 Support)
    3. ops-agent (Dept 11 Operations)
    4. cost-manager-agent (Dept 08 Finance — needs GATE for costs)
    5. health-chief-agent (Dept 17 System Health)

### TASK-006
Status: DONE
Priority: LOW
Assigned: git-integrity-agent
Description: |
  Scan the entire repo to find secret patterns and orphaned branches.
  Modules to run:
    - SECRET_PATTERNS scan: API keys, tokens, passwords in tracked files
    - Orphaned branch list: branches do not have PR and are older than 30 days
    - Stash check: git stash list → notify if there are unprocessed stashes
  Output: system/telemetry/receipts/git-integrity-YYYY-MM-DD.json
  Authority: READ-ONLY (don't delete branches, don't delete stashes)

---

## Backlog (not READY — needs CEO approval)

### BACKLOG-001
Status: PENDING_APPROVAL
Priority: HIGH
Description: |
  Write a full prompt for coo-agent.
  The COO is the C-Suite agent, the CEO needs to clearly define scope and authority
  before activating. Recommended scope: managing cross-dept workflows,
  approve resource requests, escalate from dept heads.
  Requires: CEO input on COO authority scope

### BACKLOG-002
Status: PENDING_APPROVAL
Priority: MEDIUM
Description: |
  Integrate Telegram notification when system-repair-agent finds an issue.
  Requires: TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in MASTER.env
  Workflow: system/ops/workflows/notification-bridge.md
  Trigger: repair receipt has issues_found > 0

---

## Completed

### TASK-001
Status: DONE
Completed: 2026-03-29
Description: Full audit and repair of OmniClaw project (encoding, paths, naming, MCP, registry, Dept 32 creation)
Result: 388 files encoding-fixed, 30 skills registered, Dept 32 System Integrity created with 12 agents

### TASK-002
Status: DONE
Completed: 2026-03-29
Description: System expansion — PM2 autostart, docs sync, all 9 registry/governance files updated
Result: |
  - blackboard.json: Task-002 logged, lightrag_status updated
  - SYSTEM_INDEX.yaml: OMNICLAW_ROOT → OMNICLAW_ROOT (replace_all), header updated
  - MASTER_SYSTEM_MAP.md: v3.0 — 23 depts, fixed double paths, PM2 services, Dept 32
  - GEMINI.md: v2.6 — sync date, garbled chars fixed, Dept 32 + RULE-AUTOFIX-01 added
  - README.md: repo URLs fixed, 9-dept table, `omniclaw` CLI command
  - server.test.js: API smoke tests (9 endpoints)
  - .github/workflows/ci.yml: GitHub Actions CI (Node + Python health checks)
  - repair receipt: system/telemetry/receipts/REPAIR-TASK002-2026-03-29.json
