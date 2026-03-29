# Workflow: system-repair
# Owner: system-repair-agent | Dept 32 (System Integrity)
# Trigger: "audit system" | "fix system" | "scan and fix" | "kiểm tra hệ thống" | boot missing files | CI/CD encoding fail
# Version: 1.0 | Created: 2026-03-29

---

## Purpose

Full or targeted repair run of OmniClaw system integrity. Detects and fixes encoding corruption,
broken paths, stale naming, MCP plugin failures, skill registry inconsistencies, and config syntax errors.

---

## Trigger Conditions

| Trigger | Run Type |
|---------|----------|
| "audit system" / "kiểm tra hệ thống" | Full repair |
| "fix system" / "sửa lỗi hệ thống" | Full repair |
| "scan and fix" | Full repair |
| "aos repair" / "omniclaw repair" | Full repair |
| Boot: missing/unreadable files detected | Quick (targeted) |
| After large rename/refactor | Quick (encoding + naming) |
| CI/CD encoding/path failure | Targeted (affected files) |
| Scheduled (daily) | Full repair |

---

## Phase 0 — Pre-Flight

```bash
# Snapshot current state
git status
git stash list
```

**Check:**
- Any uncommitted changes? → Log them, proceed carefully
- Any stash entries? → Note and leave untouched
- Branch: confirm we're on working branch (not main)

---

## Phase 1 — Stale Naming Scan (Module 3)

**Tool:** `grep` / Python string scan
**Scope:** All `.md`, `.py`, `.ps1`, `.yaml`, `.yml`, `.json`, `.js` (excluding blocked paths)

```python
STALE_PATTERNS = [
    ('AI OS CORP', 'OmniClaw'),
    ('AI OS', 'OmniClaw'),
    ('aios_', 'omniclaw_'),
    ('AI_OS_ROOT', 'OMNICLAW_ROOT'),
    ('AOS_ROOT', 'OMNICLAW_ROOT'),
    ('<AI_OS_ROOT>', '<OMNICLAW_ROOT>'),
    ('aios-local', 'omniclaw'),
]
```

**Action:** Log all occurrences → Auto-replace clear matches → Skip excluded paths
**Output:** `stale_naming_report` in REPAIR_RECEIPT

---

## Phase 2 — Encoding Fix (Module 1)

**Tool:** `ftfy` Python library
**Scope:** All `.md`, `.ps1`, `.py`, `.yaml`, `.yml`

```bash
pip install ftfy -q
python3 -c "
import ftfy, os, glob
root = os.environ.get('OMNICLAW_ROOT', os.environ.get('AOS_ROOT', '.'))
for ext in ['*.md', '*.py', '*.ps1', '*.yaml', '*.yml']:
    for f in glob.glob(f'{root}/**/{ext}', recursive=True):
        if any(skip in f for skip in ['.git', '__pycache__', 'node_modules', 'venv', '_archive', 'receipts', 'knowledge']):
            continue
        try:
            content = open(f, encoding='utf-8', errors='replace').read()
            fixed = ftfy.fix_text(content)
            if fixed != content:
                open(f, 'w', encoding='utf-8').write(fixed)
                print(f'FIXED: {f}')
        except Exception as e:
            print(f'ERROR: {f}: {e}')
"
```

**Action:** Auto-fix all changed files
**Output:** `encoding_fixed` count in REPAIR_RECEIPT

---

## Phase 3 — MCP Plugin Health (Module 4)

**Tool:** Node.js / Python
**Scope:** `.mcp.json`

```bash
node -e "
const c=require('./.mcp.json');
const fs=require('fs');
const broken=[];
Object.entries(c.mcpServers||{}).forEach(([n,s])=>{
  const f=(s.args||[]).find(a=>a.endsWith('.js')||a.endsWith('.py')||a.endsWith('.cjs'));
  if(f && !fs.existsSync(f)) broken.push({server:n, missing:f});
});
if(broken.length) { console.log('BROKEN:', JSON.stringify(broken,null,2)); process.exit(1); }
else console.log('All MCP plugins healthy');
"
```

**Action:** Move broken plugin entries to `_disabled_servers` key in `.mcp.json`
**Output:** `mcp_plugins_disabled` count in REPAIR_RECEIPT

---

## Phase 4 — Skill Registry Sync (Module 5)

**Tool:** Python
**Scope:** `ecosystem/skills/` vs `brain/shared-context/SKILL_REGISTRY.json`

```python
import os, json
root = os.environ.get('OMNICLAW_ROOT', os.environ.get('AOS_ROOT', '.'))
skills_dir = os.path.join(root, 'ecosystem/skills')
registry_path = os.path.join(root, 'brain/shared-context/SKILL_REGISTRY.json')

with open(registry_path) as f:
    registry = json.load(f)

registered = {s['name'] for s in registry['skills']}
on_disk = {d for d in os.listdir(skills_dir)
           if os.path.isdir(os.path.join(skills_dir, d)) and not d.endswith('.json')}

missing = on_disk - registered
broken = [s['name'] for s in registry['skills']
          if not os.path.exists(os.path.join(root, s['path']))]

print(f'Missing from registry: {missing}')
print(f'Broken paths in registry: {broken}')
```

**Action:** Add missing skills to registry → Flag broken paths for manual review
**Output:** `registry_synced` count in REPAIR_RECEIPT

---

## Phase 5 — Path Validation (Module 2)

**Tool:** Python regex + `os.path.exists()`
**Scope:** `.mcp.json`, `*.bat`, `*.ps1`, CI/CD YAMLs, `server.js`

**Action:** Report all broken paths → Confirm with operator before fixing
**Output:** `broken_paths_found` in REPAIR_RECEIPT

---

## Phase 6 — JSON/YAML Syntax Validation (Module 6)

**Tool:** Python json/yaml
**Scope:** All `.json`, `.yaml`, `.yml` (excluding `.git`, `node_modules`, `venv`)

**Action:** Report all parse errors → Manual intervention required
**Output:** `json_yaml_errors` count in REPAIR_RECEIPT

---

## Phase 7 — Write REPAIR_RECEIPT

Write to `system/telemetry/receipts/repair_<YYYYMMDD>_<HHMMSS>.json`:

```json
{
  "receipt_id": "REPAIR-<YYYYMMDD>-<HHMMSS>",
  "agent": "system-repair-agent",
  "timestamp": "<ISO8601>",
  "run_type": "full | quick | targeted",
  "summary": {
    "files_checked": 0,
    "encoding_fixed": 0,
    "stale_names_fixed": 0,
    "broken_paths_found": 0,
    "mcp_plugins_disabled": 0,
    "registry_synced": 0,
    "json_yaml_errors": 0
  },
  "issues_pending": [],
  "requires_ceo_action": [],
  "next_scheduled": "<ISO8601>"
}
```

---

## Phase 8 — Update Blackboard & Commit

```bash
# Update blackboard.json → system_status: "healthy" or "needs_attention"
# Then commit:
git add -A
git commit -m "fix(repair): System auto-repair run $(date +%Y%m%d-%H%M%S)"
```

---

## Escalation Paths

| Condition | Action |
|-----------|--------|
| > 50 broken paths | Write ESCALATION_REPORT, stop, notify CEO |
| Any Tier 0 file affected | Notify CEO immediately |
| Delete file needed | CEO approval required |
| > 10 unfixed after 2 cycles | Escalate CEO |
| 2-strike failure on same task | `handoff_trigger: BLOCKED` → report |

---

## References

- **Agent definition:** `brain/agents/system-repair-agent.md`
- **Skill toolkit:** `ecosystem/skills/system_autofix/SKILL.md`
- **Knowledge base:** `brain/knowledge/notes/KI-SYSTEM-REPAIR-01.md`
- **Department:** `brain/corp/departments/system_integrity.yaml`
