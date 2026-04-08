#!/usr/bin/env python3
"""
[OPS] Workforce Cleanup & Pipeline Enforcer (Zero-Trust)
========================================================
Scans the root of ecosystem/workforce for any stray/rogue folders
that bypass the Daemons. It acts as a vacuum, moving all unrecognized
entities securely into vault/tmp/state_queues/OER_INBOX for proper routing.
"""

import os
import shutil
from pathlib import Path

ROOT = Path(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
WORKFORCE_DIR = ROOT / "ecosystem" / "workforce"
OER_INBOX = ROOT / "vault" / "tmp" / "state_queues" / "OER_INBOX"

# Immutable structural folders that are ALLOWED to exist in workforce/ root
# Everything else is considered rogue and will be vacuumed.
ALLOWED_ROOT_DIRS = {
    "agents",
    "departments",
    "subagents",
    "system"
}

def main():
    print("--- [ZERO-TRUST SWEEPER] INITIATING WORKFORCE SCAN ---")
    OER_INBOX.mkdir(parents=True, exist_ok=True)
    
    rogue_items = []
    
    for item in WORKFORCE_DIR.iterdir():
        # Ignore files directly in workforce (like markdown docs)
        if item.is_file():
            continue
            
        # Vacuum any directory not in the allowed list
        if item.name not in ALLOWED_ROOT_DIRS and not item.name.startswith(('.', '__')):
            rogue_items.append(item)
            
    if not rogue_items:
        print("\033[92m[OK]\033[0m No rogue/stray folders found in ecosystem/workforce. Architecture strictly intact.")
        print("--- [ZERO-TRUST SWEEPER] COMPLETE ---")
        return

    print(f"\033[93m[WARN]\033[0m Detected {len(rogue_items)} rogue folder(s) bypassing the Pipeline!")
    
    moved_count = 0
    for rogue in rogue_items:
        dest_path = OER_INBOX / rogue.name
        
        # If destination already exists in INBOX, remove it to prevent crash
        if dest_path.exists():
            shutil.rmtree(dest_path, ignore_errors=True)
            
        print(f"  -> Teleporting rogue asset: \033[91m{rogue.name}\033[0m to OER_INBOX")
        try:
            shutil.move(str(rogue), str(dest_path))
            moved_count += 1
        except Exception as e:
            print(f"  [X] Failed to teleport {rogue.name}: {e}")
            
    print(f"\n--- [ZERO-TRUST SWEEPER] OPERATION COMPLETE ---")
    print(f"\033[92m[OK]\033[0m Successfully quarantined {moved_count}/{len(rogue_items)} items to OER_INBOX.")

if __name__ == "__main__":
    main()
