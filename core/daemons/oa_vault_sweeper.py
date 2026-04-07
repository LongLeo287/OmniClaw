import os
import sys

# Add core/daemons to the path to import ohd_health
sys.path.append(os.path.dirname(__file__))

import ohd_health

OMNICLAW_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))
VAULT_DIR = os.path.join(OMNICLAW_ROOT, "vault")

healed_count = 0
scanned_count = 0

print("[OmniClaw System Event]")

# Scan entire vault, ignoring tmp folders (not archives)
for root, dirs, files in os.walk(VAULT_DIR):
    if "tmp" in root.replace('\\', '/') and not "quarantine" in root:
        continue
        
    for file in files:
        if file.endswith(".md"):
            scanned_count += 1
            fpath = os.path.join(root, file)
            try:
                # Press Heal!
                if ohd_health.heal_frontmatter(fpath):
                    healed_count += 1
            except Exception as e:
                pass

print("[OmniClaw System Event]")
print("[OmniClaw System Event]")
