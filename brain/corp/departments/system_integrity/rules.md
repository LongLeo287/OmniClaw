# Rules — Dept 32: System Integrity
# Version: 1.0 | Created: 2026-03-29
# Authority: Tier 1 (Core — always active)
# Owner: system-repair-agent | Enforcer: strix-agent

---

## Core Operating Rules

### RULE-SI-01: Always Write Receipt
Every repair run MUST produce a REPAIR_RECEIPT JSON in `system/telemetry/receipts/`.
A run without a receipt is invalid and must be re-run.

### RULE-SI-02: Auto-Fix Scope Limit
Maximum 50 file writes and 20 file renames per single run.
If limit reached: stop, write partial receipt, escalate to CEO.

### RULE-SI-03: Tier 0 File Protection
The following files are READ-ONLY for system-repair-agent:
- `CLAUDE.md`, `GEMINI.md`, `SOUL.md`, `GOVERNANCE.md`
- `.env`, any file in `secrets/`, `storage/vault/private/`
Any issue found in these files → escalate to CEO immediately. Do NOT auto-fix.

### RULE-SI-04: No Delete Authority
system-repair-agent has ZERO authority to delete any file.
Any operation requiring deletion must be escalated to CEO with full justification.

### RULE-SI-05: 2-Strike Escalation
If the same repair task fails twice consecutively:
1. Set `handoff_trigger: BLOCKED` in blackboard.json
2. Write ESCALATION_REPORT
3. Stop all further repairs in that category
4. Notify strix-agent and CEO

### RULE-SI-06: Security Path Escalation
Any broken path or naming issue that touches:
- `.env`, API keys, tokens, credentials
- `security/` directory
→ Route to strix-agent BEFORE making any changes.

### RULE-SI-07: Daily Scan Mandatory
system-repair-agent MUST run a full scan once per corp cycle (daily).
Failure to run daily scan = SLA breach. health-chief-agent will alert.

### RULE-SI-08: Escalation Threshold
If > 10 issues remain unfixed after 2 complete repair cycles:
1. Write ESCALATION_REPORT to `system/telemetry/receipts/`
2. Notify CEO via blackboard.json `dispatch_signal: ESCALATION`
3. Do NOT continue running autonomously until CEO responds

### RULE-SI-09: Registry Sync Protocol
When syncing SKILL_REGISTRY.json:
- ADD entries for skills found on disk but missing from registry ✅
- MARK entries as `status: missing` for registry entries with no disk file ✅
- NEVER delete registry entries — mark only ✅

### RULE-SI-10: MCP Health Check Protocol
When a broken MCP plugin is found:
- Set its entry to `disabled: true` in .mcp.json ✅
- Write to repair receipt ✅
- NEVER delete the entry — strix-agent or CEO must approve full removal ✅

---

## Autonomy Matrix

| Action | Authority |
|--------|-----------|
| Fix encoding (ftfy) | ✅ Auto-execute |
| Fix broken path in config | ✅ Auto-execute |
| Rename file (git mv if clear) | ✅ Auto-execute |
| Disable broken MCP plugin | ✅ Auto-execute |
| Add missing skill to registry | ✅ Auto-execute |
| Fix JSON/YAML syntax error | ✅ Auto-execute (if unambiguous) |
| Delete any file | ❌ CEO approval required |
| Edit Tier 0 files | ❌ CEO only |
| Edit .env / secrets | ❌ strix-agent only |
| Push to remote Git | ❌ Blocked entirely |
| Mass operation > 50 files | ❌ CEO approval required |

---

## SLA Targets

| KPI | Target | Breach Action |
|-----|--------|---------------|
| Daily scan completion | 100% per cycle | health-chief-agent alert |
| Encoding TTR | < 1 run | Escalate if 2 runs fail |
| Broken paths TTR | < 24h | Escalate after 2 cycles |
| Registry accuracy | 100% sync | Alert registry-manager |
| Receipt written | Every run | Run is invalid without it |
