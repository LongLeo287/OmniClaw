---
name: system_autofix
description: Auto-detect and fix system integrity issues in OmniClaw — encoding corruption, broken paths, stale naming, MCP plugin failures, registry inconsistencies, and JSON/YAML syntax errors.
version: "1.0"
tier: tier1
category: system-maintenance
agents: ["system-repair-agent", "Claude Code", "Antigravity"]
created: "2026-03-29"
---

# system_autofix — OmniClaw Auto-Repair Toolkit

## When to Use

Activate **automatically** when:
- User says: `"audit system"`, `"fix system"`, `"scan and fix"`, `"kiểm tra hệ thống"`
- Boot sequence detects missing/corrupt files
- After any large rename/refactor operation
- CI/CD fails with encoding or path errors
- Weekly scheduled maintenance run

**Do NOT wait for explicit instruction** — activate on any sign of system degradation.

---

## Repair Modules

### Module 1 — Encoding Fix (mojibake)

**Detects:** Files with UTF-8 double-encoding (Ã¢â‚¬â€ patterns, corrupted Vietnamese text)

```python
import ftfy

def fix_encoding(file_path: str) -> dict:
    """Fix mojibake in any text file."""
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    fixed = ftfy.fix_text(content)
    changed = fixed != content
    if changed:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(fixed)
    return {"file": file_path, "fixed": changed, "mojibake_count": content.count('Ã')}
```

**Scope:** All `.md`, `.ps1`, `.py`, `.yaml`, `.yml` files
**Auto-execute:** YES — safe, reversible via git

---

### Module 2 — Path Validation

**Detects:** Config files referencing paths that don't exist on disk

```python
import os, json, re

KNOWN_PATH_PATTERNS = [
    r'ecosystem/plugins/\S+',
    r'system/infra/\S+',
    r'brain/shared-context/\S+',
    r'ecosystem/skills/\S+',
]

def validate_paths(root: str, file_path: str) -> list:
    """Return list of broken paths found in file."""
    with open(file_path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    broken = []
    for pattern in KNOWN_PATH_PATTERNS:
        for match in re.finditer(pattern, content):
            full = os.path.join(root, match.group())
            if not os.path.exists(full):
                broken.append({"path": match.group(), "line": content[:match.start()].count('\n') + 1})
    return broken
```

**Scope:** `.mcp.json`, `*.bat`, `*.ps1`, CI/CD YAMLs, `server.js`
**Auto-execute:** Report only — fix requires confirmation for ambiguous cases

---

### Module 3 — Stale Naming Scan

**Detects:** Old "OmniClaw", "aios_", "AI_OS_ROOT" references that weren't renamed to OmniClaw

```python
STALE_PATTERNS = [
    ('OmniClaw Corp', 'OmniClaw'),
    ('OmniClaw', 'OmniClaw'),
    ('aios_', 'omniclaw_'),
    ('AI_OS_ROOT', 'OMNICLAW_ROOT'),
    ('AOS_ROOT', 'OMNICLAW_ROOT'),
    ('$OMNICLAW_ROOT', '<OMNICLAW_ROOT>'),
    ('omniclaw-local', 'omniclaw'),
]

EXCLUDED_FILES = [
    'brain/shared-context/AGENTS.md',   # historical references OK
    'brain/knowledge/',                  # knowledge items — read-only
    'system/telemetry/receipts/',        # historical receipts — read-only
    'storage/_archive/',                 # archives — read-only
    '.git/',                             # git internals
]
```

**Auto-execute:** YES for clear matches. Skip excluded paths.

---

### Module 4 — MCP Plugin Health Check

**Detects:** `.mcp.json` entries with `command`/`args` pointing to non-existent files

```python
def check_mcp_health(root: str) -> dict:
    mcp_path = os.path.join(root, '.mcp.json')
    with open(mcp_path) as f:
        config = json.load(f)

    results = {"healthy": [], "broken": [], "disabled": []}
    for name, server in config.get('mcpServers', {}).items():
        args = server.get('args', [])
        for arg in args:
            if arg.endswith(('.js', '.py', '.cjs', '.mjs')):
                full_path = os.path.join(root, arg)
                if not os.path.exists(full_path):
                    results["broken"].append({"server": name, "missing": arg})
                else:
                    results["healthy"].append(name)
                break

    for key in config.get('_disabled_servers', {}):
        results["disabled"].append(key.replace('_disabled_', ''))

    return results
```

**Auto-execute:** YES — disable broken plugins automatically

---

### Module 5 — SKILL_REGISTRY Sync

**Detects:** Skills in `ecosystem/skills/` not in registry, or registry entries with wrong paths

```python
def sync_skill_registry(root: str) -> dict:
    skills_dir = os.path.join(root, 'ecosystem/skills')
    registry_path = os.path.join(root, 'brain/shared-context/SKILL_REGISTRY.json')

    with open(registry_path) as f:
        registry = json.load(f)

    registered = {s['name']: s for s in registry['skills']}
    on_disk = {d for d in os.listdir(skills_dir)
               if os.path.isdir(os.path.join(skills_dir, d)) and d != 'SKILL_REGISTRY.json'}

    missing_from_registry = on_disk - set(registered.keys())
    broken_paths = [
        name for name, skill in registered.items()
        if not os.path.exists(os.path.join(root, skill['path']))
    ]

    return {
        "missing_from_registry": list(missing_from_registry),
        "broken_paths": broken_paths,
        "total_on_disk": len(on_disk),
        "total_registered": len(registered)
    }
```

**Auto-execute:** Add missing skills, flag broken paths for manual review

---

### Module 6 — JSON/YAML Syntax Validation

```python
import yaml

def validate_configs(root: str) -> list:
    errors = []
    # JSON
    for dirpath, _, files in os.walk(root):
        if any(skip in dirpath for skip in ['.git', '__pycache__', 'node_modules', 'venv']):
            continue
        for f in files:
            path = os.path.join(dirpath, f)
            try:
                if f.endswith('.json'):
                    json.load(open(path, encoding='utf-8'))
                elif f.endswith(('.yaml', '.yml')):
                    yaml.safe_load(open(path, encoding='utf-8').read())
            except Exception as e:
                errors.append({"file": path.replace(root, ''), "error": str(e)[:100]})
    return errors
```

**Auto-execute:** Report only — fixes require manual intervention

---

## Full Repair Run Workflow

```
STEP 1: git status → snapshot current state
STEP 2: Run Module 3 (Stale Naming) → log findings
STEP 3: Run Module 1 (Encoding) → auto-fix .md, .ps1
STEP 4: Run Module 4 (MCP Health) → disable broken plugins
STEP 5: Run Module 5 (Registry Sync) → add missing skills
STEP 6: Run Module 2 (Path Validation) → report broken paths
STEP 7: Run Module 6 (JSON/YAML) → report syntax errors
STEP 8: Write REPAIR_RECEIPT to system/telemetry/receipts/repair_<timestamp>.json
STEP 9: Update blackboard.json → system_status field
STEP 10: git add -A && git commit "fix(repair): System auto-repair run <timestamp>"
```

---

## Output Format — REPAIR_RECEIPT

```json
{
  "receipt_id": "REPAIR-<YYYYMMDD>-<HHMMSS>",
  "agent": "system-repair-agent",
  "timestamp": "<ISO8601>",
  "run_type": "full | quick | targeted",
  "summary": {
    "files_checked": 0,
    "encoding_fixed": 0,
    "paths_validated": 0,
    "broken_paths_found": 0,
    "stale_names_fixed": 0,
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

## Quick Commands

```bash
# Quick health scan (read-only)
python3 -c "import json; [json.load(open(f)) for f in ['brain/shared-context/SKILL_REGISTRY.json', 'brain/shared-context/blackboard.json', '.mcp.json']]"

# Encoding check on specific file
python3 -c "import ftfy; open('CLAUDE.md','w').write(ftfy.fix_text(open('CLAUDE.md').read()))"

# Find stale OmniClaw references
grep -r "OmniClaw\|AI_OS_ROOT\|aios_\|AOS_ROOT" --include="*.md" --include="*.py" --include="*.ps1" --include="*.yaml" . | grep -v ".git" | grep -v "_archive"

# MCP health check
node -e "const c=require('./.mcp.json'); const fs=require('fs'); Object.entries(c.mcpServers||{}).forEach(([n,s])=>{ const f=(s.args||[]).find(a=>a.endsWith('.js')||a.endsWith('.py')); if(f && !fs.existsSync(f)) console.log('BROKEN:', n, f); })"
```

---

## Notes

- Requires `ftfy` Python package: `pip install ftfy`
- Requires `pyyaml`: `pip install pyyaml`
- Always run `git status` before and after repairs
- Never run on `.env`, `secrets/`, `storage/vault/` paths
- Source: OmniClaw System Audit 2026-03-29
