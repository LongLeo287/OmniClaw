---
description: "Handoff heavy execution tasks to Claude Code CLI to conserve quota."
id: workflow-handoff-omniclaw
version: "2.0"
updated_at: "2026-04-03"
type: workflow
platform: antigravity
tier: 1
trigger: "large code task / quota low / CEO explicit handoff command"
---

# Workflow: Handoff to OmniClaw Coder (Claude Code CLI)

Use this workflow when Antigravity needs to delegate **execution authority**
to the Claude Code CLI (routed via OmniClaw Router) — to conserve Gemini quota
or leverage the `omniclaw-coder` network for heavy code tasks.

---

## Trigger Conditions

| Condition | Signal |
|-----------|--------|
| Large code volume | Task requires creating/modifying >5 files or >200 lines |
| Quota conservation | Antigravity's Gemini quota is running low |
| CEO explicit command | "Send that task to OmniClaw" / "Handoff to Claude Code" |
| Complex execution | Multi-step shell operations, long-running builds |

---

## Steps

### Step 0 — Pre-flight Check

```
1. Verify Claude Code CLI process is running:
   → Check: running terminal commands list for "claude" process
   → If NOT running: warn CEO — "Claude Code CLI is not running. Please open the Claude Code terminal first."
   → STOP — do not proceed without confirmation CLI is active.

2. Load routing config from .env:
   → OMNICLAW_ROUTER_URL  (default: http://127.0.0.1:8080/v1)
   → OMNICLAW_MODEL       (default: omniclaw-coder)
   These values are set by CEO manually in .env — never hardcode here.
```

### Step 1 — Prepare the Prompt

```
1. Read the agreed request or approved plan from CEO.
2. Compress into a single, self-contained One-shot Prompt:
   - Include all necessary context (file paths, conventions, constraints)
   - Reference relevant docs: CLAUDE.md boot sequence, relevant brain/ files
   - Specify expected output format and archive path
   - Add: "Write receipt to vault/tmp/receipts/<task>-<date>.json when done" (per OMA rule)
3. Max prompt length: 2000 tokens (lean — sub-agent does its own reads)
```

### Step 2 — Execute Handoff via Claude CLI

// turbo
```powershell
# Race Condition Protection (OBD constraint)
if (Test-Path "vault/tmp/state_queues/handoff.lock") {
    Write-Host "⚠️ BLOCKED: Another Claude process is running."
    exit 1
}
New-Item -Path "vault/tmp/state_queues/handoff.lock" -ItemType File -Force

# Read routing from .env (Antigravity uses run_command to execute)
# Format: claude -p "<task description>"
# Claude Code CLI auto-routes to omniclaw-coder via configured base_url

claude -p "<compressed task description from Step 1>"

# Cleanup lock
Remove-Item "vault/tmp/state_queues/handoff.lock" -Force
```

**SECURITY RULE:**
> Antigravity **MUST NEVER** call the router port (8080) directly via HTTP API.
> This risks triggering Google's monitoring systems → silent account ban.
> ALL communication with local models = Terminal (CLI) layer ONLY.

### Step 3 — Monitor & Accept Results

```
1. Wait for Claude Code to finish (output appears in terminal)
2. Verify receipt was written to vault/tmp/receipts/
3. Update blackboard.json:
   → handoff_trigger: "complete"
   → last_task: "<task title>"
4. Report completion to CEO (Vietnamese):
   "✅ Claude Code has finished: <summary>. Receipt: vault/tmp/receipts/<file>"
```

### Step 4 — Reverse Handoff (Claude Code → Antigravity)

```
When Claude Code signals done (handoff_trigger: "complete" in blackboard):
1. Antigravity reads receipt: vault/tmp/receipts/<task>-<date>.json
2. Validates output exists and is correct
3. Archives session note to brain/memory/daily/<date>/handoff_log.md
4. Resumes CEO conversation with summary
5. Ensure handoff.lock is deleted.
```

---

## On Failure / Blocked

```
If Claude Code fails twice (2-strike rule from CLAUDE.md):
→ Claude sets: handoff_trigger = "blocked" in blackboard.json
→ Antigravity detects BLOCKED state at next check
→ Escalate to CEO: "⚠️ Claude Code is blocked at task <X>. CEO intervention required."
→ Log: brain/memory/corp_memory/escalations.md (L2 escalation)

**Timeout / Rogue Process (OBD Sandbox)**:
If the `claude` process runs wildly for > 30 minutes without completion:
→ Emit an OBD alert. OBD Harbor Master is authorized to execute a hard port-kill.
```

---

## Config Reference

All routing values read from `.env` — set once by CEO, never modified by agents:

| Env Key | Purpose | Example |
|---------|---------|---------|
| `OMNICLAW_ROUTER_URL` | Local router base URL | `http://127.0.0.1:8080/v1` |
| `OMNICLAW_MODEL` | Model name at router | `omniclaw-coder` |
