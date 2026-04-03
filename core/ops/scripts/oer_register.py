#!/usr/bin/env python3
"""
oer_register.py - OER (OmniClaw Ecosystem Registry) Intake Automation
-----------------------------------------------------------------------
PHASE 5 of the 5-Gate Ecosystem Pipeline.
This script is the ONLY authorized pathway to register new assets
into the OmniClaw ecosystem.

AUTHORITY: Dept 14 (registry-manager-agent) / OER Core Daemon
PREREQUISITE: OHD_CLEAN + OA_APPROVED stamps must exist in the asset folder.

USAGE:
  python oer_register.py --path storage/vault/quarantine/<asset_folder>
                         --type skill|plugin|agent|workflow|dept
                         [--name "My Skill Name"]
                         [--dry-run]
"""

import os
import sys
import json
import shutil
import argparse
import datetime
from pathlib import Path

# --------------------------------------------------------------------------
# PATH SETUP — No hardcoded paths
# --------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent
AI_OS_ROOT = SCRIPT_DIR.parent.parent.parent
REGISTRY_FILE = AI_OS_ROOT / "brain" / "registry" / "SKILL_REGISTRY.json"
ECOSYSTEM_DIR = AI_OS_ROOT / "ecosystem"
QUARANTINE_DIR = AI_OS_ROOT / "storage" / "vault" / "quarantine"
RECEIPT_DIR = AI_OS_ROOT / "telemetry" / "qa_receipts" / "gate_oer"

# ID prefixes per asset type
ID_PREFIXES = {
    "skill": "SKILL",
    "plugin": "PLG",
    "agent": "AGT",
    "workflow": "WRK",
    "dept": "DEPT",
}
ECOSYSTEM_TARGETS = {
    "skill": "skills",
    "plugin": "plugins",
    "agent": "workforce",
    "workflow": "workflows",
    "dept": "workforce",
}

# --------------------------------------------------------------------------
# HELPERS
# --------------------------------------------------------------------------

def log(msg: str, level: str = "INFO"):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tag = {"INFO": "✅", "WARN": "⚠️", "ERROR": "❌", "STEP": "🔹"}.get(level, "ℹ️")
    print(f"[{ts}][OER][{level}] {tag} {msg}")


def load_registry() -> dict:
    if not REGISTRY_FILE.exists():
        log(f"Registry not found at {REGISTRY_FILE}. Starting fresh.", "WARN")
        return {"assets": {}, "id_counters": {}}
    with open(REGISTRY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_registry(registry: dict):
    REGISTRY_FILE.parent.mkdir(parents=True, exist_ok=True)
    with open(REGISTRY_FILE, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2, ensure_ascii=False)
    log(f"Registry saved: {REGISTRY_FILE}")


def generate_id(registry: dict, asset_type: str) -> str:
    prefix = ID_PREFIXES[asset_type]
    counter = registry.get("id_counters", {}).get(prefix, 0) + 1
    if "id_counters" not in registry:
        registry["id_counters"] = {}
    registry["id_counters"][prefix] = counter
    return f"{prefix}-{counter:04d}"


def check_duplicate(registry: dict, asset_name: str) -> str | None:
    """Returns existing ID if duplicate found, else None."""
    for asset_id, meta in registry.get("assets", {}).items():
        if meta.get("name", "").lower() == asset_name.lower():
            return asset_id
    return None


def validate_stamps(asset_path: Path) -> tuple[bool, list]:
    """
    Validates that OHD_CLEAN and OA_APPROVED stamps exist.
    Returns (is_valid, list_of_missing_stamps)
    """
    required_stamps = ["OHD_CLEAN", "OA_APPROVED"]
    missing = []
    for stamp in required_stamps:
        stamp_file = asset_path / f".{stamp}"
        # Also check for stamp in a stamps/ subdirectory
        stamp_alt = asset_path / "stamps" / stamp
        if not stamp_file.exists() and not stamp_alt.exists():
            missing.append(stamp)
    return len(missing) == 0, missing


# --------------------------------------------------------------------------
# GATE 0: Duplicate Check
# --------------------------------------------------------------------------

def gate_zero_check(registry: dict, name: str, dry_run: bool) -> bool:
    log("GATE 0: Checking for duplicates in registry...", "STEP")
    existing_id = check_duplicate(registry, name)
    if existing_id:
        log(f"DUPLICATE DETECTED! '{name}' is already registered as {existing_id}.", "ERROR")
        log("Pipeline HALTED. Use the existing asset ID.", "ERROR")
        return False
    log(f"Gate 0 PASSED: '{name}' is not yet registered.")
    return True


# --------------------------------------------------------------------------
# PHASE 5: OER Registration
# --------------------------------------------------------------------------

def phase5_register(asset_path: Path, asset_type: str, name: str,
                    registry: dict, dry_run: bool) -> str | None:
    log("PHASE 5: OER Registration commencing...", "STEP")

    # Validate stamps
    valid, missing = validate_stamps(asset_path)
    if not valid:
        log(f"BLOCKED: Missing required stamps: {missing}", "ERROR")
        log("Ensure OHD (Phase 2) and OA (Phase 3) have both approved this asset.", "ERROR")
        return None

    log(f"Stamps verified: OHD_CLEAN + OA_APPROVED found.")

    # Generate unique ID
    asset_id = generate_id(registry, asset_type)
    log(f"Issued ID: {asset_id}")

    # Determine destination
    target_subdir = ECOSYSTEM_TARGETS[asset_type]
    dest_path = ECOSYSTEM_DIR / target_subdir / asset_path.name

    if not dry_run:
        # Move from quarantine to ecosystem
        if dest_path.exists():
            log(f"WARNING: Destination already exists: {dest_path}", "WARN")
        else:
            shutil.copytree(str(asset_path), str(dest_path))
            log(f"Copied to ecosystem: {dest_path}")

        # Update registry
        if "assets" not in registry:
            registry["assets"] = {}
        registry["assets"][asset_id] = {
            "id": asset_id,
            "name": name,
            "type": asset_type,
            "path": str(dest_path.relative_to(AI_OS_ROOT)),
            "registered_at": datetime.datetime.now().isoformat(),
            "stamps": {
                "OHD_CLEAN": True,
                "OA_APPROVED": True,
            },
            "status": "active",
        }
        save_registry(registry)

        # Write receipt
        RECEIPT_DIR.mkdir(parents=True, exist_ok=True)
        receipt = {
            "asset_id": asset_id,
            "name": name,
            "type": asset_type,
            "registered_at": datetime.datetime.now().isoformat(),
            "source_quarantine": str(asset_path),
            "destination": str(dest_path),
            "authority": "OER (Dept 14 - registry-manager-agent)",
        }
        receipt_file = RECEIPT_DIR / f"{asset_id}.json"
        with open(receipt_file, "w", encoding="utf-8") as f:
            json.dump(receipt, f, indent=2, ensure_ascii=False)
        log(f"Receipt written: {receipt_file}")
    else:
        log(f"[DRY RUN] Would copy: {asset_path} --> {dest_path}")
        log(f"[DRY RUN] Would register {asset_id} in SKILL_REGISTRY.json")

    log(f"REGISTRATION COMPLETE: {name} registered as {asset_id}", "INFO")
    log(f"Notify Orchestrator: Asset {asset_id} is ready for deployment.", "INFO")
    return asset_id


# --------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="OER — OmniClaw Ecosystem Registry. PHASE 5 intake automation."
    )
    parser.add_argument("--path", required=True,
                        help="Path to the asset folder in quarantine/ (relative or absolute)")
    parser.add_argument("--type", required=True,
                        choices=["skill", "plugin", "agent", "workflow", "dept"],
                        help="Type of asset being registered")
    parser.add_argument("--name", default=None,
                        help="Human-readable name (defaults to folder name)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Simulate registration without writing files")
    args = parser.parse_args()

    asset_path = Path(args.path)
    if not asset_path.is_absolute():
        asset_path = AI_OS_ROOT / asset_path
    if not asset_path.exists():
        log(f"Asset path not found: {asset_path}", "ERROR")
        sys.exit(1)

    name = args.name or asset_path.name

    print()
    print("=" * 60)
    print("  OER — OMNICLAW ECOSYSTEM REGISTRY — PHASE 5")
    print("=" * 60)
    if args.dry_run:
        log("DRY RUN MODE — No files will be written", "WARN")
    log(f"Asset: {name} | Type: {args.type}")
    log(f"Source: {asset_path}")
    print()

    # Load registry
    registry = load_registry()

    # Gate 0
    if not gate_zero_check(registry, name, args.dry_run):
        sys.exit(2)

    # Phase 5 Register
    result_id = phase5_register(asset_path, args.type, name, registry, args.dry_run)
    if not result_id:
        sys.exit(3)

    print()
    print("=" * 60)
    print(f"  REGISTERED SUCCESSFULLY: {result_id}")
    print("=" * 60)
    sys.exit(0)


if __name__ == "__main__":
    main()
