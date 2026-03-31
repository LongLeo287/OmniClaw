#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OmniClaw Repair - Wave 9: legacy env var + stale path fixes"""
import os, sys
from pathlib import Path

ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))
print("[Wave 9] Root: %s" % ROOT)
total = 0

EXCLUDE_DIRS = {"_archive", "__pycache__", ".git", "node_modules", ".claude"}

# Build old/new strings at runtime to prevent linter auto-replacement
_OLD_VAR = "AOS" + "_ROOT"
_NEW_VAR = "OMNICLAW_ROOT"

def read_file(path):
    for enc in ["utf-8", "utf-8-sig", "latin-1"]:
        try:
            return open(path, "r", encoding=enc, errors="replace").read(), enc
        except Exception:
            pass
    return None, None

def write_file(path, content):
    open(path, "w", encoding="utf-8", errors="replace").write(content)

def fix_file(path, replacements):
    global total
    content, enc = read_file(path)
    if content is None:
        return
    changed = 0
    for old, new in replacements:
        if old in content:
            n = content.count(old)
            content = content.replace(old, new)
            changed += n
    if changed:
        write_file(path, content)
        print("  [%3d] %s" % (changed, str(path.relative_to(ROOT))))
        total += changed

# Python patterns
py_fixes = [
    ('os.getenv("%s")' % _OLD_VAR,          'os.getenv("%s")' % _NEW_VAR),
    ("os.getenv('%s')" % _OLD_VAR,          "os.getenv('%s')" % _NEW_VAR),
    ('os.environ.get("%s"' % _OLD_VAR,      'os.environ.get("%s"' % _NEW_VAR),
    ("os.environ.get('%s'" % _OLD_VAR,      "os.environ.get('%s'" % _NEW_VAR),
    ('os.environ["%s"]' % _OLD_VAR,         'os.environ["%s"]' % _NEW_VAR),
    ("os.environ['%s']" % _OLD_VAR,         "os.environ['%s']" % _NEW_VAR),
    # comment references
    ('env var %s' % _OLD_VAR,               'env var %s' % _NEW_VAR),
    ('# %s' % _OLD_VAR,                     '# %s' % _NEW_VAR),
]

print("\n=== Phase 1: Python env var fixes ===")
for search_dir in [ROOT/"system", ROOT/"ecosystem", ROOT/"storage", ROOT/"brain"]:
    if not search_dir.exists():
        continue
    for f in search_dir.rglob("*.py"):
        if any(p in f.parts for p in EXCLUDE_DIRS):
            continue
        fix_file(f, py_fixes)

# PS1 patterns
ps1_fixes = [
    ("$env:%s" % _OLD_VAR,   "$env:%s" % _NEW_VAR),
    ("$%s" % _OLD_VAR,       "$%s" % _NEW_VAR),
    (" %s " % _OLD_VAR,      " %s " % _NEW_VAR),
    ("=%s" % _OLD_VAR,       "=%s" % _NEW_VAR),
]

print("\n=== Phase 2: PS1 env var fixes ===")
for search_dir in [ROOT/"system", ROOT/"ecosystem"]:
    if not search_dir.exists():
        continue
    for f in search_dir.rglob("*.ps1"):
        if any(p in f.parts for p in EXCLUDE_DIRS):
            continue
        fix_file(f, ps1_fixes)

# BAT patterns
bat_fixes = [
    ("%s" % _OLD_VAR, "%s" % _NEW_VAR),
]
print("\n=== Phase 3: BAT env var fixes ===")
for f in (ROOT/"system").rglob("*.bat"):
    if any(p in f.parts for p in EXCLUDE_DIRS):
        continue
    fix_file(f, bat_fixes)

# Fix start-infrastructure.bat paths (root calc + service paths)
print("\n=== Phase 4: start-infrastructure.bat path repair ===")
infra = ROOT / "system" / "ops" / "scripts" / "start-infrastructure.bat"
if infra.exists():
    content, _ = read_file(infra)
    if content:
        path_fixes = [
            # Fix root depth: scripts/ is 4 levels under project root
            # (project/system/ops/scripts -> need ..\\..\\..\\.. not ..\\..)
            ('%~dp0\\..\\..',     '%~dp0\\..\\..\\..\\..'),
            # Fix sub-paths
            ('\\%s\\ops\\scripts' % _NEW_VAR,       '\\%s\\system\\ops\\scripts' % _NEW_VAR),
            ('\\%s\\ops\\telemetry' % _NEW_VAR,     '\\%s\\system\\ops\\telemetry' % _NEW_VAR),
            ('\\%s\\.env' % _NEW_VAR,               '\\%s\\system\\ops\\secrets\\MASTER.env' % _NEW_VAR),
            ('\\%s\\api\\server.js' % _NEW_VAR,     '\\%s\\system\\infra\\api\\server.js' % _NEW_VAR),
            ('\\%s\\mcp\\servers\\' % _NEW_VAR,     '\\%s\\system\\infra\\mcp\\servers\\' % _NEW_VAR),
            # Branding
            ('AI OS Corp',    'OmniClaw Corp'),
            ('START AI OS',   'START OmniClaw'),
        ]
        changed = 0
        for old, new in path_fixes:
            if old in content:
                n = content.count(old)
                content = content.replace(old, new)
                changed += n
        if changed:
            write_file(infra, content)
            print("  [%3d] start-infrastructure.bat" % changed)
            total += changed

# Fix launch_claude_phase4.bat
print("\n=== Phase 5: launch_claude_phase4.bat fix ===")
p4 = ROOT / "system" / "ops" / "scripts" / "launch_claude_phase4.bat"
if p4.exists():
    content, _ = read_file(p4)
    if content:
        fixes = [
            ('cd /d $env:%s' % _OLD_VAR,  'cd /d %%%s%%' % _NEW_VAR),
            ('AI OS Corp',                'OmniClaw Corp'),
        ]
        changed = 0
        for old, new in fixes:
            if old in content:
                n = content.count(old)
                content = content.replace(old, new)
                changed += n
        if changed:
            write_file(p4, content)
            print("  [%3d] launch_claude_phase4.bat" % changed)
            total += changed

# Fix start_lightrag.ps1 additional paths
print("\n=== Phase 6: start_lightrag.ps1 path repair ===")
lr = ROOT / "system" / "ops" / "scripts" / "start_lightrag.ps1"
if lr.exists():
    content, _ = read_file(lr)
    if content:
        fixes = [
            ('"$%s\\ops\\scripts\\lightrag_server.py"' % _NEW_VAR,
             '"$%s\\system\\ops\\scripts\\lightrag_server.py"' % _NEW_VAR),
            ('$serverScript = "$%s\\ops\\scripts' % _NEW_VAR,
             '$serverScript = "$%s\\system\\ops\\scripts' % _NEW_VAR),
            ('AI OS LightRAG',   'OmniClaw LightRAG'),
            ('=== AI OS',        '=== OmniClaw'),
            # inline python placeholders
            ('<AI' + '_OS_ROOT>',  '" + $env:OMNICLAW_ROOT + "'),
        ]
        changed = 0
        for old, new in fixes:
            if old in content:
                n = content.count(old)
                content = content.replace(old, new)
                changed += n
        if changed:
            write_file(lr, content)
            print("  [%3d] start_lightrag.ps1" % changed)
            total += changed

# Fix start_supervisor_openclaw.ps1
print("\n=== Phase 7: start_supervisor_openclaw.ps1 fix ===")
oc = ROOT / "system" / "ops" / "scripts" / "start_supervisor_openclaw.ps1"
if oc.exists():
    content, _ = read_file(oc)
    if content:
        # Add root var if missing
        if ('$%s' % _NEW_VAR) not in content:
            content = '$%s = if ($env:%s) { $env:%s } else { (Resolve-Path "$PSScriptRoot\\..\\..\\..\\..").Path }\n' % (
                _NEW_VAR, _NEW_VAR, _NEW_VAR) + content
            total += 1
        fixes = [
            ('<AI' + '_OS_ROOT>\\plugins\\openclaw',
             '$%s\\ecosystem\\plugins\\openclaw' % _NEW_VAR),
            ('Set-Location "<AI' + '_OS_ROOT>\\plugins\\openclaw"',
             'Set-Location "$%s\\ecosystem\\plugins\\openclaw"' % _NEW_VAR),
            ('[INFRA] Loading Workspace: <AI' + '_OS_ROOT>',
             '[INFRA] Loading Workspace: $%s' % _NEW_VAR),
            ('$OPENCLAW_DIR = "<AI' + '_OS_ROOT>\\plugins\\openclaw"',
             '$OPENCLAW_DIR = "$%s\\ecosystem\\plugins\\openclaw"' % _NEW_VAR),
            ('AI OS CORP - OPENCLAW', 'OmniClaw Corp - OpenClaw'),
            ('AI OS CORP',            'OmniClaw Corp'),
        ]
        changed = 0
        for old, new in fixes:
            if old in content:
                n = content.count(old)
                content = content.replace(old, new)
                changed += n
        if changed:
            write_file(oc, content)
            print("  [%3d] start_supervisor_openclaw.ps1" % changed)
            total += changed

# Fix storage/vault/rules/INDEX.md placeholders
print("\n=== Phase 8: placeholder cleanup in md/json/yaml ===")
placeholder_fixes = [
    ('<AI' + '_OS_ROOT>', '$OMNICLAW_ROOT'),
    ('<' + _OLD_VAR + '>', '$OMNICLAW_ROOT'),
]
for search_dir in [ROOT/"storage", ROOT/"brain", ROOT/"system", ROOT/"ecosystem"]:
    if not search_dir.exists():
        continue
    for ext in ["*.md", "*.json", "*.yaml", "*.ps1"]:
        for f in search_dir.rglob(ext):
            if any(p in f.parts for p in EXCLUDE_DIRS):
                continue
            fix_file(f, placeholder_fixes)

print("\n" + "="*60)
print("Wave 9 Complete! Total replacements: %d" % total)
print("="*60)
