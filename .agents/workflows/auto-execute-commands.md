---
description: "Rules for autonomously running commands authorized by the CEO."
id: workflow-auto-execute-commands
version: "1.0"
updated_at: "2026-04-03"
type: workflow
platform: antigravity
tier: 1
trigger: "CEO pastes commands + 'auto do it' / 'handle it yourself' / 'add to system'"
---

# Workflow: Auto-Execute Commands

> **Rule ref:** `GEMINI.md § rule: auto-execute commands` — When CEO pastes a list
> of commands and signals auto-execution, Antigravity must classify and execute
> immediately. No asking. No clarification. Just execute and report.

---

## Trigger Phrases

- "auto do it"
- "handle it yourself"
- "add to system"
- "execute" / "run this" / "do it"
- CEO pastes a block of commands without explicit instruction

---

## Decision Table — Command Classification

| Type | Keywords / Pattern | Action | SafeToAutoRun |
|------|-------------------|--------|---------------|
| **one-time** | `install`, `fix`, `init`, `migrate`, `register`, `--write` | Run immediately | `true` |
| **long-running** | `server`, `watch`, `bridge`, `polling`, `daemon`, `start` | Start background + add to HUD | `true` |
| **verify** | `status`, `health`, `--check`, `list`, `show`, `ping` | Run + report output | `true` |
| **destructive** | `delete`, `drop`, `rm`, `format`, `reset`, `truncate`, `purge` | **STOP — ask CEO** | `false` |
| **secret-touching** | Writes to `.env`, `MASTER.env`, `secrets/` | **STOP — ask CEO** | `false` |

> If a command matches multiple categories → use the **most restrictive** category.

---

## Steps

### Step 1 — Classify All Commands

```
1. For each command in CEO's list:
   a. Match against Decision Table
   b. Assign: type, action, SafeToAutoRun
2. Build execution plan table (show to CEO only if mixed safe/unsafe)
```

### Step 2 — Execute Safe Commands

```
For all commands with SafeToAutoRun = true:
1. Execute in dependency order (installs before starts, inits before runs)
2. Long-running: use run_command with WaitMsBeforeAsync=500 (background)
3. Capture output for each command
4. On error: log + continue (non-blocking unless command is a prerequisite)
```

### Step 3 — Handle Unsafe Commands

```
For all commands with SafeToAutoRun = false:
1. DO NOT execute
2. Present to CEO with reason:
   "⚠️ This command requires confirmation — [reason]: <command>"
3. Wait for explicit CEO approval before executing
```

### Step 4 — Add to HUD

```
For all long-running commands that were started:
1. Add entry to brain/memory/core/STATUS.json under services[]
2. Format: { name: "<service>", command: "<cmd>", started: "<ts>", port: <port|null> }
```

### Step 5 — Report Results

Report via table (one-time, concise):

```markdown
| Command | Type | Result |
|---------|------|--------|
| python core/ops/omniclaw_startup.py | one-time | ✅ Exit 0 |
| python core/ops/omniclaw_orchestrator.py watch 30 | long-running | 🔄 Background PID 1234 |
| rm -rf /tmp/cache | destructive | ⏳ Needs CEO approval |
```

### Step 6 — Archive Log

```
Append to: brain/memory/daily/<YYYY-MM-DD>/auto_exec_log.md
Format:
  [<timestamp>] AUTO-EXEC SESSION
  Commands: <count_total>
  Executed: <count_executed>
  Skipped (needs approval): <count_skipped>
  Details: <full table from Step 5>
```

---

## Examples

**CEO input:** "install lightrag, start it, check status"

| Command | Type | Action |
|---------|------|--------|
| `pip install lightrag-hku==1.3.9` | one-time | Run immediately ✅ |
| `python ecosystem/plugins/lightrag/server.py` | long-running | Background + add to HUD ✅ |
| `curl http://localhost:9621/health` | verify | Run + report output ✅ |

**CEO input:** "drop the test database and reset"

| Command | Type | Action |
|---------|------|--------|
| `DROP DATABASE test` | destructive | ⚠️ STOP — ask CEO |
| `reset migrations` | destructive | ⚠️ STOP — ask CEO |
