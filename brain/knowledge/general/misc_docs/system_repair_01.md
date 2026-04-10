---
id: ki-system-repair-01
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.796542
---

# KI-SYSTEM-REPAIR-01 — OmniClaw System Repair Knowledge Item
# Type: Operational Knowledge | Dept: System Integrity (32)
# Created: 2026-03-29 | Owner: system-repair-agent
# Source: OmniClaw Full Audit 2026-03-29

---

## Summary

Complete map of known failure patterns in OmniClaw and their corresponding auto-repair procedures.
Used by `system-repair-agent` as primary reference for repair runs.

---

## Failure Pattern Library

### FP-01 — UTF-8 Mojibake (Double Encoding)

**Symptom:** Files display garbled text like `Ã¢â‚¬â€`, `Ã¢â€â‚¬`, `Ã¢â€"Âº`
**Root cause:** UTF-8 bytes read as CP1252/Latin-1, then re-encoded as UTF-8
**Affected files:** `.md`, `.ps1`, `.py`, `.yaml`, `.yml`
**Detection:** `ftfy.fix_text()` returns different content than input
**Fix:** Apply `ftfy.fix_text()`, overwrite file
**Auto-execute:** YES
**Reversible:** YES (git)

**Example:**
```
Corrupted:  Ã¢â‚¬â€
Fixed:      —
```

### FP-02 — Stale Naming (OmniClaw → OmniClaw Migration)

**Symptom:** References to old names remain after project rename
**Patterns to replace:**
```
OmniClaw Corp → OmniClaw
OmniClaw → OmniClaw
aios_ → omniclaw_
AI_OS_ROOT → OMNICLAW_ROOT
AOS_ROOT → OMNICLAW_ROOT (env vars)
$OMNICLAW_ROOT → $env:OMNICLAW_ROOT (in PS1)
omniclaw-local → omniclaw
```
**Excluded paths:** `.git/`, `brain/knowledge/`, `core/telemetry/receipts/`, `vault/_archive/`
**Auto-execute:** YES for clear matches
**Reversible:** YES (git)

### FP-03 — Broken Config Paths

**Symptom:** Config files reference paths that don't exist on disk
**Common patterns:**
- `.mcp.json` plugin args pointing to non-built JS files
- `server.js` path constants using wrong root prefix
- `.ps1` scripts with literal `$OMNICLAW_ROOT` placeholder
- GitHub Actions referencing old directory layout
**Detection:** `os.path.exists()` check on extracted path tokens
**Fix:** Update path to correct location
**Auto-execute:** Report + confirm for ambiguous cases

### FP-04 — MCP Plugin Broken Entries

**Symptom:** `.mcp.json` has `mcpServers` entries where the `args[].js` file doesn't exist
**Cause:** Plugin was added to config before building its dist/ output
**Fix:** Move broken entry to `_disabled_servers` key
**Auto-execute:** YES — disabling is safe, reversible
**Known broken plugins (as of 2026-03-29):** `minimax-mcp-js`, `notebooklm-mcp`, `claude-mem`, `notebook-agent`

### FP-05 — SKILL_REGISTRY Out of Sync

**Symptom:** Skills exist on disk at `ecosystem/skills/` but not in `SKILL_REGISTRY.json`, or registry entries have wrong paths
**Detection:** Diff between `os.listdir("ecosystem/skills/")` and `registry["skills"][*]["name"]`
**Fix:** Add missing skills to registry; flag broken paths for review
**Auto-execute:** Add missing = YES; remove broken = CEO review

### FP-06 — JSON/YAML Syntax Errors

**Symptom:** Config files fail to parse
**Common causes:** Trailing commas, unquoted strings, wrong indent
**Detection:** `json.load()` or `yaml.safe_load()` raises exception
**Fix:** Manual — syntax errors require human judgment
**Auto-execute:** Report only

### FP-07 — Missing agent .md File

**Symptom:** Agent in `activation_status.json` has no corresponding `.md` in `brain/agents/`
**Fix:** Create stub `.md` using agent definition template
**Auto-execute:** Report + create stub with CEO confirmation

---

## Exclusion Rules

Never auto-fix these paths:
```
.git/
brain/knowledge/                  # knowledge items are read-only
core/telemetry/receipts/        # historical receipts
vault/_archive/                 # archives
.env / secrets/                   # security boundary
CLAUDE.md / GEMINI.md / SOUL.md   # Tier 0 — CEO only
GOVERNANCE.md                     # Tier 0 — CEO only
```

---

## Repair Run Checklist

```
[ ] 1. git status — snapshot before
[ ] 2. Module 3: Stale naming scan → log
[ ] 3. Module 1: Encoding fix → auto-fix .md .ps1 .py
[ ] 4. Module 4: MCP health → disable broken plugins
[ ] 5. Module 5: Registry sync → add missing skills
[ ] 6. Module 2: Path validation → report broken paths
[ ] 7. Module 6: JSON/YAML validation → report errors
[ ] 8. Write REPAIR_RECEIPT to core/telemetry/receipts/
[ ] 9. Update blackboard.json → system_status
[ ] 10. git commit "fix(repair): System auto-repair run <timestamp>"
```

---

## Known Audit Findings (2026-03-29)

From full audit on 2026-03-29:

| # | Issue | Status |
|---|-------|--------|
| 1 | CLAUDE.md mojibake (all instructions corrupted) | FIXED |
| 2 | GEMINI.md mojibake | FIXED |
| 3 | 4 MCP plugins broken (missing dist files) | FIXED (disabled) |
| 4 | server.js router.yaml path wrong | FIXED |
| 5 | server.js plugins/ path wrong | FIXED |
| 6 | start_lightrag.ps1 literal `$OMNICLAW_ROOT` | FIXED |
| 7 | start_supervisor_openclaw.ps1 `$OMNICLAW_ROOT` | FIXED |
| 8 | package.json name=omniclaw-local, bin=omniclaw | FIXED |
| 9 | 24 files with aios_/OmniClaw naming | FIXED |
| 10 | SKILL_REGISTRY duplicate agent-shield | FIXED |
| 11 | SKILL_REGISTRY wrong openclaw_tools path | FIXED |
| 12 | 5 skills on disk missing from registry | FIXED |
| 13 | GitHub workflows wrong skill paths | FIXED |

---

*Source: KI-SYSTEM-REPAIR-01 — OmniClaw Full Audit 2026-03-29 | Used by system-repair-agent (Dept 32)*
