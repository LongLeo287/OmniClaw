#!/usr/bin/env python3
"""
OmniClaw Core Startup
Path: core/ops/omniclaw_startup.py

Internal-only startup flow for the OmniClaw core daemon system.
This script intentionally excludes bridge, remote, UI, ports, and
project-facing agent services.
"""

from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARGS = set(sys.argv[1:])
CHECK_ONLY = "--check-only" in ARGS
VERBOSE = "--verbose" in ARGS or "-v" in ARGS

BLACKBOARD = ROOT / "brain" / "memory" / "blackboard.json"
SKILL_REGISTRY = ROOT / "brain" / "registry" / "SKILL_REGISTRY.json"
TOOL_REGISTRY = ROOT / "ecosystem" / "tools" / "TOOL_REGISTRY.json"
ACTIVATION = ROOT / "brain" / "agents" / "activation_status.json"
SYSTEM_ROUTER = ROOT / "brain" / "agents" / "system_router.json"
STATUS_JSON = ROOT / "core" / "telemetry" / "STATUS.json"
RECEIPTS_DIR = ROOT / "core" / "telemetry" / "receipts"

CRITICAL_PATHS = [
    BLACKBOARD,
    SKILL_REGISTRY,
    ACTIVATION,
    SYSTEM_ROUTER,
]

OPTIONAL_PATHS = [
    TOOL_REGISTRY,
    STATUS_JSON,
    RECEIPTS_DIR,
]

CORE_DAEMONS = [
    "oma_architect",
    "oiw_intake",
    "ohd_health",
    "oer_registry",
    "oa_academy",
]


class C:
    GREEN = "\033[92m"
    RED = "\033[91m"
    YELLOW = "\033[93m"
    CYAN = "\033[96m"
    BOLD = "\033[1m"
    RESET = "\033[0m"


def now_iso() -> str:
    tz = datetime.timezone(datetime.timedelta(hours=7))
    return datetime.datetime.now(tz).isoformat()


def load_json(path: Path):
    try:
        with open(path, encoding="utf-8-sig") as handle:
            return json.load(handle)
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return None


def save_json(path: Path, data: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = path.with_suffix(path.suffix + ".tmp")
    with open(tmp_path, "w", encoding="utf-8") as handle:
        json.dump(data, handle, indent=2, ensure_ascii=False)
    tmp_path.replace(path)


def hdr(message: str) -> None:
    print(f"\n{C.BOLD}{C.CYAN}{'=' * 56}{C.RESET}")
    print(f"{C.BOLD}{message}{C.RESET}")


def ok(message: str) -> None:
    print(f"  {C.GREEN}OK{C.RESET} {message}")


def warn(message: str) -> None:
    print(f"  {C.YELLOW}WARN{C.RESET} {message}")


def err(message: str) -> None:
    print(f"  {C.RED}ERR{C.RESET} {message}")


def count_registry_entries(payload) -> tuple[int, str]:
    if isinstance(payload, dict):
        if isinstance(payload.get("skills"), list):
            return len(payload["skills"]), "list"
        return len(payload), "dict"
    if isinstance(payload, list):
        return len(payload), "list"
    return 0, "unknown"


def check_paths() -> tuple[bool, list[str]]:
    hdr("STEP 1 - Core State Files")
    missing: list[str] = []

    for path in CRITICAL_PATHS:
        rel = path.relative_to(ROOT)
        if path.exists():
            ok(str(rel))
        else:
            err(f"{rel} missing")
            missing.append(str(rel))

    for path in OPTIONAL_PATHS:
        rel = path.relative_to(ROOT)
        if path.exists():
            ok(str(rel))
        else:
            warn(f"{rel} not present")

    return not missing, missing


def check_blackboard() -> dict:
    hdr("STEP 2 - Blackboard")
    payload = load_json(BLACKBOARD)
    if not isinstance(payload, dict):
        err("blackboard.json unreadable")
        return {"status": "ERROR"}

    cycle_status = payload.get("corp_cycle_status", "IDLE")
    trigger = payload.get("handoff_trigger", "IDLE")
    open_items = payload.get("open_items", [])
    if not isinstance(open_items, list):
        open_items = []

    ok(f"corp_cycle_status = {cycle_status}")
    ok(f"handoff_trigger = {trigger}")
    ok(f"open_items = {len(open_items)}")

    if payload.get("active_campaign"):
        if VERBOSE:
            ok(f"active_campaign = {payload['active_campaign']}")

    return {
        "status": "OK",
        "corp_cycle_status": cycle_status,
        "handoff_trigger": trigger,
        "open_items": len(open_items),
    }


def check_activation() -> dict:
    hdr("STEP 3 - Core Daemon Activation")
    payload = load_json(ACTIVATION)
    if not isinstance(payload, dict):
        err("activation_status.json unreadable")
        return {"status": "ERROR", "online": 0, "offline": 0}

    daemon_status = payload.get("daemons", {})
    online = 0
    offline = 0
    details = {}

    for daemon_id in CORE_DAEMONS:
        state = str(daemon_status.get(daemon_id, "UNKNOWN")).upper()
        details[daemon_id] = state
        if state in {"UP", "ONLINE", "ACTIVE", "IDLE"}:
            ok(f"{daemon_id} = {state}")
            online += 1
        else:
            warn(f"{daemon_id} = {state}")
            offline += 1

    return {"status": "OK", "online": online, "offline": offline, "details": details}


def check_registries() -> dict:
    hdr("STEP 4 - Registries")
    summary = {"status": "OK", "skills": 0, "tools": 0}

    skill_payload = load_json(SKILL_REGISTRY)
    if skill_payload is None:
        err("SKILL_REGISTRY.json unreadable")
        summary["status"] = "DEGRADED"
    else:
        count, schema = count_registry_entries(skill_payload)
        summary["skills"] = count
        ok(f"skill registry loaded ({count} entries, schema={schema})")

    tool_payload = load_json(TOOL_REGISTRY)
    if tool_payload is None:
        warn("TOOL_REGISTRY.json unreadable or missing")
        summary["status"] = "DEGRADED"
    else:
        count, schema = count_registry_entries(tool_payload)
        summary["tools"] = count
        ok(f"tool registry loaded ({count} entries, schema={schema})")

    router_payload = load_json(SYSTEM_ROUTER)
    if isinstance(router_payload, dict):
        route_count = len(router_payload.get("ROUTING_TABLE", {}))
        dept_count = len(router_payload.get("DEPARTMENTS", {}))
        summary["routes"] = route_count
        summary["departments"] = dept_count
        ok(f"system router loaded ({route_count} rules, {dept_count} departments)")
    else:
        err("system_router.json unreadable")
        summary["status"] = "DEGRADED"

    return summary


def update_status(
    files_ok: bool,
    blackboard_info: dict,
    activation_info: dict,
    registry_info: dict,
) -> dict:
    hdr("STEP 5 - Core Telemetry")
    status = load_json(STATUS_JSON)
    if not isinstance(status, dict):
        status = {}

    overall = "OK"
    if not files_ok or blackboard_info.get("status") == "ERROR":
        overall = "ERROR"
    elif registry_info.get("status") != "OK":
        overall = "DEGRADED"

    status.update(
        {
            "version": "v5.0-core",
            "system": "OmniClaw Core",
            "updated": now_iso(),
            "last_startup_check": now_iso(),
            "core_startup_status": overall,
            "core_daemons_online": activation_info.get("online", 0),
            "core_daemons_offline": activation_info.get("offline", 0),
            "corp_cycle_status": blackboard_info.get("corp_cycle_status", "UNKNOWN"),
            "handoff_trigger": blackboard_info.get("handoff_trigger", "UNKNOWN"),
            "skills": registry_info.get("skills", 0),
            "tools": registry_info.get("tools", 0),
            "departments": registry_info.get("departments", 0),
            "routing_rules": registry_info.get("routes", 0),
        }
    )

    save_json(STATUS_JSON, status)
    ok(
        "core telemetry updated "
        f"(status={overall}, daemons={activation_info.get('online', 0)}/{len(CORE_DAEMONS)})"
    )
    return status


def print_summary(
    files_ok: bool,
    blackboard_info: dict,
    activation_info: dict,
    registry_info: dict,
) -> None:
    hdr("SUMMARY")
    print(f"  Files: {'OK' if files_ok else 'ERROR'}")
    print(f"  Blackboard: {blackboard_info.get('corp_cycle_status', 'UNKNOWN')}")
    print(
        "  Core daemons: "
        f"{activation_info.get('online', 0)} online / {activation_info.get('offline', 0)} non-ready"
    )
    print(
        "  Registries: "
        f"{registry_info.get('skills', 0)} skills, {registry_info.get('tools', 0)} tools"
    )
    print(f"  Receipts dir: {RECEIPTS_DIR.relative_to(ROOT)}")
    print()
    print("  Next:")
    print("  - Run `omniclaw sync` if registry counts look stale.")
    print("  - Run `omniclaw core` to keep internal upkeep running.")
    print("  - Start bridge/agent services separately from the agent system flow.")


def main() -> int:
    hdr("OMNICLAW CORE STARTUP")
    files_ok, _missing = check_paths()
    blackboard_info = check_blackboard()
    activation_info = check_activation()
    registry_info = check_registries()

    if not CHECK_ONLY:
        update_status(files_ok, blackboard_info, activation_info, registry_info)

    print_summary(files_ok, blackboard_info, activation_info, registry_info)

    if not files_ok or blackboard_info.get("status") == "ERROR":
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
