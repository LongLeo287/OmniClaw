#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix SKILL_REGISTRY.json:
1. Replace stale hardcoded path prefix with dynamic OMNICLAW_ROOT
2. Remove null entries from load_order arrays
3. Remove entries with null id/name
"""
import json, os
from pathlib import Path

ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[3])))
REGISTRY = ROOT / "brain" / "shared-context" / "SKILL_REGISTRY.json"

OLD_PREFIX = "D:\\LongLeo\\OmniClaw Corp\\OmniClaw\\"
NEW_PREFIX = str(ROOT) + "\\"

print("[fix_skill_registry] Root: %s" % ROOT)

with open(REGISTRY, encoding="utf-8-sig") as f:
    raw = f.read()

# 1. Fix path prefix
count_paths = raw.count(OLD_PREFIX)
raw = raw.replace(OLD_PREFIX, NEW_PREFIX)
print("  Path prefix fixed: %d occurrences" % count_paths)

data = json.loads(raw)

# 2. Remove nulls from load_order arrays
lo = data.get("load_order", {})
null_removed = 0
for tier, arr in lo.items():
    if isinstance(arr, list):
        before = len(arr)
        lo[tier] = [x for x in arr if x is not None]
        null_removed += before - len(lo[tier])
print("  Null load_order entries removed: %d" % null_removed)

# 3. Remove null-id entries from entries array
entries = data.get("entries", [])
before = len(entries)
data["entries"] = [e for e in entries if e.get("id") is not None and e.get("name") is not None]
removed_entries = before - len(data["entries"])
print("  Null-id entries removed: %d (was %d, now %d)" % (removed_entries, before, len(data["entries"])))

# 4. Save
with open(REGISTRY, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("  SKILL_REGISTRY.json saved OK")
print("[fix_skill_registry] Done.")
