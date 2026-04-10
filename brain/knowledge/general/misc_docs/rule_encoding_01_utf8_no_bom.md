---
id: rule-encoding-01-utf8-no-bom
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:10.155321
---

# RULE-ENCODING-01 — UTF-8 Without BOM Standard
**Issued:** 2026-03-31
**Status:** MANDATORY
**Owner:** strix-agent / engineering
**Applies to:** ALL text files in OmniClaw

---

## Core Rule

**ALL text files must be UTF-8 without BOM.**

- Python scripts: `# -*- coding: utf-8 -*-` header (optional but recommended)
- JSON files: no BOM, UTF-8
- Markdown: UTF-8
- PS1/BAT: UTF-8 without BOM (CRLF line endings per `.gitattributes`)
- YAML: UTF-8

**FORBIDDEN:** UTF-16, UTF-32, Windows-1252 (cp1252), Latin-1, UTF-8 WITH BOM for Python/JSON/MD.

---

## Why BOM Causes Problems

- Python: `utf-8` mode raises decode error or inserts `\ufeff` at file start
- JSON: BOM breaks `json.loads()` with JSONDecodeError (occurred in `core/infra/mcp/config.json`)
- PowerShell: wrong encoding garbles multi-byte characters
- Git: BOM causes spurious diffs and merge conflicts

---

## Detecting BOM

```powershell
# PowerShell — check single file
$bytes = [System.IO.File]::ReadAllBytes("path\to\file.py")
if ($bytes[0] -eq 0xEF -and $bytes[1] -eq 0xBB -and $bytes[2] -eq 0xBF) {
    Write-Host "BOM detected"
}
```

```bash
# Bash — find all BOM files
grep -rl $'\xef\xbb\xbf' . --include="*.py" --include="*.json" --include="*.md"
```

---

## Fixing Encoding

### Fix single file (PowerShell)
```powershell
Get-Content "file.py" -Encoding UTF8 | Set-Content "file.py" -Encoding UTF8NoBOM
```

### Fix all BOM files (batch)
```powershell
# Run the OmniClaw BOM fixer:
pwsh core/ops/scripts/fix_encoding_bom.ps1
# Dry-run (no changes):
pwsh core/ops/scripts/fix_encoding_bom.ps1 -DryRun
```

### Python — always use explicit encoding
```python
# Good
with open(path, encoding="utf-8") as f: ...
with open(path, encoding="utf-8-sig") as f: ...  # tolerates BOM on read

# Bad — platform-dependent default
with open(path) as f: ...
```

---

## .gitattributes Enforcement

`.gitattributes` at root sets `encoding=utf-8` for all text files and normalizes line endings.
This prevents encoding drift when files are committed from different machines.

See: `ecosystem/skills/fix_encoding_bom.ps1` for batch repair tool.

---

## Responsible Agent

- **Primary:** engineering / Claude Code — fix during code review
- **Monitor:** strix-agent — scan for BOM in weekly security scan

---

*RULE-ENCODING-01 | OmniClaw Corp | 2026-03-31*
