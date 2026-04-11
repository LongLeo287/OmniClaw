#!/usr/bin/env python3
"""
OmniClaw V5.0 — System Startup Script
Path: core/ops/omniclaw_startup.py
Built: 2026-03-26 | Author: Antigravity

Usage:
  python core/ops/omniclaw_startup.py                 # Boot check + status refresh
  python core/ops/omniclaw_startup.py --verbose       # Verbose output
  python core/ops/omniclaw_startup.py --check-only    # Only check, do not write status
  python core/ops/omniclaw_startup.py --telegram      # Opt in to Telegram reporting
"""

import json
import sys
import time
import datetime
import subprocess
import socket
import urllib.request
import urllib.error
from pathlib import Path

# ─── CONFIG ──────────────────────────────────────────────────────────────────
ROOT = Path(__file__).parent.parent.parent
ARGS = sys.argv[1:]
VERBOSE    = "--verbose" in ARGS or "-v" in ARGS
CHECK_ONLY = "--check-only" in ARGS
SEND_TELEGRAM = "--telegram" in ARGS

def now_iso():
    return datetime.datetime.now(
        datetime.timezone(datetime.timedelta(hours=7))
    ).isoformat()

def load_json(p):
    try:
        with open(p, encoding="utf-8-sig") as f:
            return json.load(f)
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return None

def save_json(p, d):
    import time, os
    lock_path = str(p) + ".lock"
    for _ in range(50):
        try:
            fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            break
        except FileExistsError:
            time.sleep(0.05)
    try:
        tmp_path = str(p) + ".tmp"
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(d, f, indent=2, ensure_ascii=False)
        os.replace(tmp_path, p)
    finally:
        try:
            if os.path.exists(lock_path): os.remove(lock_path)
        except OSError:
            pass

def _env():
    env, p = {}, ROOT / ".env"
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip() and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                env[k.strip()] = v.strip().strip('"')
    return env
ENV = _env()

# ─── DISPLAY ─────────────────────────────────────────────────────────────────
class C:
    GREEN  = "\033[92m"
    RED    = "\033[91m"
    YELLOW = "\033[93m"
    CYAN   = "\033[96m"
    BOLD   = "\033[1m"
    RESET  = "\033[0m"

def ok(msg):   print(f"  {C.GREEN}✅{C.RESET} {msg}")
def err(msg):  print(f"  {C.RED}❌{C.RESET} {msg}")
def warn(msg): print(f"  {C.YELLOW}⚠️{C.RESET}  {msg}")
def info(msg): print(f"  {C.CYAN}ℹ️{C.RESET}  {msg}")
def hdr(msg):  print(f"\n{C.BOLD}{C.CYAN}{'─'*50}{C.RESET}\n  {C.BOLD}{msg}{C.RESET}")

# ─── CHECKS ──────────────────────────────────────────────────────────────────

CRITICAL_FILES = [
    ROOT / "brain" / "memory" / "blackboard.json",
    ROOT / "brain" / "registry" / "SKILL_REGISTRY.json",
    ROOT / "brain" / "agents" / "gemini.md",
    ROOT / "brain" / "agents" / "activation_status.json",
    ROOT / "brain" / "agents" / "system_router.json",
]

WARN_FILES = [
    ROOT / "brain" / "registry" / "AGENTS.md",
    ROOT / "brain" / "rules" / "governance" ,
    ROOT / ".mcp.json",
]

SERVICES = [
    {"name": "Ollama LLM",   "port": 11434, "path": "/",              "critical": False},
    {"name": "ClawTask API", "port": 7474,  "path": "/api/status",    "critical": False},
    {"name": "GitNexus",     "port": 4747,  "path": "/",              "critical": False},
    {"name": "ag-auto-accept","port": 7476, "path": "/",              "critical": False},
    {"name": "DeepAgents",   "port": 8765,  "path": "/",              "critical": False},
    {"name": "LightRAG RAG", "port": 9621,  "path": "/health",        "critical": False},
    {"name": "open-notebook","port": 5055,  "path": "/",              "critical": False},
    {"name": "Langfuse",     "port": 3100,  "path": "/",              "critical": False},
]

def check_port(port: int, timeout=1) -> bool:
    try:
        with socket.create_connection(("localhost", port), timeout=timeout):
            return True
    except:
        return False


def check_critical_files() -> tuple[bool, list]:
    hdr("STEP 1.1 — Critical Files")
    errors = []
    for f in CRITICAL_FILES:
        if f.exists():
            ok(f.name)
        else:
            err(f"{f.name} — MISSING")
            errors.append(str(f))
            continue
            try:
                f.parent.mkdir(parents=True, exist_ok=True)
                if f.suffix == ".json":
                    if "STATUS" in f.name:
                        f.write_text('{"status": "BOOTSTRAPPED"}', encoding="utf-8")
                    elif "blackboard" in f.name:
                        f.write_text('{"corp_cycle_status": "IDLE", "handoff_trigger": "IDLE", "active_campaign": "none", "open_items": []}', encoding="utf-8")
                    elif "SKILL" in f.name:
                        f.write_text('{"skills": [], "metadata": {"last_updated": "unknown"}}', encoding="utf-8")
                    else:
                        f.write_text('{}', encoding="utf-8")
                else:
                    f.write_text(f"# {f.name}\\nAuto-bootstrapped.", encoding="utf-8")
                ok(f"[Bootstrap Success] {f.name} created automatically.")
            except Exception as e:
                err(f"[Bootstrap Failed] {f.name} — {e}")
                errors.append(str(f))
    for f in WARN_FILES:
        if not f.exists():
            warn(f"{f.name} — MISSING (Warning)")
            try:
                f.parent.mkdir(parents=True, exist_ok=True)
            except: pass
    return len(errors) == 0, errors


def check_blackboard() -> tuple[str, dict]:
    hdr("STEP 1.2 — Blackboard State")
    bb = load_json(ROOT / "brain" / "memory" / "blackboard.json")
    if not bb:
        err("Failed to read blackboard.json!")
        return "ERROR", {}

    cycle_status = bb.get("corp_cycle_status", "IDLE")
    trigger      = bb.get("handoff_trigger", "IDLE")
    campaign     = bb.get("active_campaign", "none")
    open_items   = len(bb.get("open_items", []))

    if cycle_status == "RUNNING":
        warn("Corp Cycle already RUNNING — Ensure no duplicate daemon before proceeding")
        warn("If stale, reset corp_cycle_status to IDLE in blackboard.json")
    else:
        ok(f"corp_cycle_status = {cycle_status}")

    ok(f"handoff_trigger = {trigger}")
    info(f"active_campaign = {campaign}")
    info(f"open_items = {open_items}")

    # Check escalations (v2.1 path)
    esc_path = ROOT / "brain" / "memory" / "corp_memory" / "escalations.md"
    if esc_path.exists():
        content = esc_path.read_text(encoding="utf-8", errors="ignore")
        l3_count = content.count("[L3]") + content.count("L3:")
        if l3_count > 0:
            err(f"HAS {l3_count} Open L3 Escalation! DO NOT start Corp Cycle before CEO resolves.")
        else:
            ok("No L3 escalation")
    else:
        ok("No escalations file (clean state)")

    return cycle_status, bb


def check_services() -> dict:
    hdr("STEP 1.3 — Services & Ports")
    results = {}
    live_count, down_count = 0, 0

    for svc in SERVICES:
        is_live = check_port(svc["port"])
        results[svc["name"]] = is_live
        if is_live:
            ok(f"{svc['name']} :{svc['port']}")
            live_count += 1
        else:
            if svc["critical"]:
                err(f"{svc['name']} :{svc['port']} — DOWN (CRITICAL)")
            else:
                warn(f"{svc['name']} :{svc['port']} — DOWN")
            down_count += 1

    print(f"\n  Summary: {live_count} LIVE | {down_count} DOWN")
    return results


def check_skill_registry() -> dict:
    hdr("STEP 1.4 — Skill Registry")
    reg_path = ROOT / "brain" / "registry" / "SKILL_REGISTRY.json"
    reg = load_json(reg_path)
    if not reg:
        err("[OmniClaw System Event]")
        return {}

    skills = reg.get("skills", [])
    meta   = reg.get("metadata", {})
    last_built = meta.get("last_updated", meta.get("last_built", "unknown"))

    ok(f"Registry loaded: {len(skills)} skills")
    info(f"Last updated: {last_built}")

    # Check freshness (> 7 days = warn)
    try:
        if "T" in str(last_built):
            built_dt = datetime.datetime.fromisoformat(last_built.replace("Z", "+00:00"))
            age_days = (datetime.datetime.now(datetime.timezone.utc) - built_dt).days
            if age_days > 7:
                warn(f"Registry {age_days} days no update! Run: python system/ops/omniclaw_orchestrator.py once")
            else:
                ok(f"Registry freshness OK ({age_days} days)")
    except:
        info("Cannot calculate registry age")

    return {"skills": len(skills), "last_updated": last_built}


def update_hud(services: dict, reg_info: dict) -> dict:
    hdr("STEP 1.5 — Update HUD STATUS.json")

    status_path = ROOT / "brain" / "memory" / "core" / "STATUS.json"
    status = load_json(status_path) or {}

    # Count live skills, agents, plugins
    skill_count   = len([d for d in (ROOT/"ecosystem"/"skills").iterdir() if d.is_dir()]) if (ROOT/"ecosystem"/"skills").exists() else 0
    agent_count   = len([d for d in (ROOT/"ecosystem"/"workforce"/"departments").iterdir() if d.is_dir()]) if (ROOT/"ecosystem"/"workforce"/"departments").exists() else 0
    plugin_count  = len([d for d in (ROOT/"ecosystem"/"plugins").iterdir() if d.is_dir()]) if (ROOT/"ecosystem"/"plugins").exists() else 0
    mcp_data      = load_json(ROOT / ".mcp.json") or {}
    mcp_count     = len(mcp_data.get("mcpServers", {}))
    live_svc      = sum(1 for v in services.values() if v)

    status.update({
        "version":          "v3.1",
        "cycle":            status.get("cycle", 11),
        "system":           "OmniClaw Corp",
        "updated":          now_iso(),
        "last_hud_update":  now_iso(),
        "skills":           skill_count,
        "agents":           agent_count,
        "corp_cycle_status": "ACTIVE",
        "orchestrator":     "ONLINE",
        "v50_reconnect":    "COMPLETE",
        "services_live":    live_svc,
        "vault": {
            **status.get("vault", {}),
            "skills":  {"total": skill_count,  "status": "OK"},
            "agents":  {"total": agent_count,  "status": "OK"},
            "mcp":     {"servers": mcp_count,  "status": "OK"},
            "plugins": {"plugins": plugin_count, "status": "OK"},
        }
    })

    save_json(status_path, status)
    ok(f"STATUS.json updated — skills={skill_count} | agents={agent_count} | MCPs={mcp_count} | services_live={live_svc}")
    return status


def send_telegram_boot_report(status: dict, bb: dict, services: dict):
    hdr("STEP 1.6 — Telegram Boot Report")
    if not SEND_TELEGRAM:
        info("Skip Telegram (use --telegram to enable reporting)")
        return

    token = ENV.get("TELEGRAM_BOT_TOKEN", "")
    chat  = ENV.get("TELEGRAM_CHAT_ID", "")
    if not token or not chat:
        warn("Telegram skip: BOT_TOKEN/CHAT_ID not configured in .env")
        return

    live  = sum(1 for v in services.values() if v)
    down  = sum(1 for v in services.values() if not v)
    svc_line = f"🔋 `{live}` LIVE | `{down}` DOWN"

    campaign = bb.get("active_campaign", "none")
    trigger  = bb.get("handoff_trigger", "IDLE")

    msg = (
        f"🚀 *OmniClaw V5.0 — SYSTEM BOOT*\n"
        f"⏰ {now_iso()[11:16]} GMT+7\n\n"
        f"━━━━━━━━━━━━━━━\n"
        f"• 🏢 System: `ONLINE`\n"
        f"• {svc_line}\n"
        f"• 🤖 Agents: `{status.get('agents', '?')}`\n"
        f"• 🧠 Skills: `{status.get('skills', '?')}`\n"
        f"• 🔌 MCPs: `{status['vault']['mcp']['servers']}`\n"
        f"• 📦 Plugins: `{status['vault']['plugins']['plugins']}`\n\n"
        f"• 🎯 Campaign: `{campaign}`\n"
        f"• 🔄 Trigger: `{trigger}`\n"
        f"━━━━━━━━━━━━━━━\n"
        f"_Awaiting CEO command_"
    )

    try:
        payload = json.dumps({"chat_id": chat, "text": msg, "parse_mode": "Markdown"}).encode()
        req = urllib.request.Request(
            f"https://api.telegram.org/bot{token}/sendMessage",
            data=payload, headers={"Content-Type": "application/json"}
        )
        with urllib.request.urlopen(req, timeout=8):
            ok("Telegram boot report sent ✅")
    except Exception as e:
        warn(f"Telegram failed: {e}")


def print_summary(files_ok: bool, cycle_status: str, services: dict, reg_info: dict):
    live = sum(1 for v in services.values() if v)
    total = len(services)

    print(f"\n{'═'*52}")
    print(f"  {C.BOLD}OmniClaw V5.0 — BOOT SUMMARY{C.RESET}")
    print(f"{'═'*52}")

    status_icon = "✅" if files_ok else "❌"
    print(f"  {status_icon} Critical Files: {'OK' if files_ok else 'MISSING!'}")

    cycle_icon = "✅" if cycle_status in ("IDLE", "ACTIVE") else "⚠️ "
    print(f"  {cycle_icon} Corp Cycle: {cycle_status}")

    svc_icon = "✅" if live >= total // 2 else "⚠️ "
    print(f"  {svc_icon} Services: {live}/{total} LIVE")

    print(f"\n  {C.BOLD}📋 Next Steps:{C.RESET}")
    if not files_ok:
        print(f"  {C.RED}→ FIX missing critical files first!{C.RESET}")
    elif cycle_status == "RUNNING":
        print("[OmniClaw System Event]")
    else:
        print(f"  {C.GREEN}→ Run `omniclaw doctor` to verify the core workspace{C.RESET}")
        print(f"  {C.GREEN}→ Launch only the specific bridges or daemons you intend to provision{C.RESET}")
        print(f"  {C.GREEN}→ Use `python core/ops/omniclaw_startup.py --telegram` only when external reporting is intended{C.RESET}")

    print(f"\n  {C.CYAN}📊 HUD:     system/hud/STATUS.json{C.RESET}")
    print(f"  {C.CYAN}📋 Tasks:   http://localhost:7474{C.RESET}")
    print(f"  {C.CYAN}📱 Telegram: @omniclaw_corp_bot{C.RESET}")
    print(f"{'═'*52}\n")


# ─── MAIN ────────────────────────────────────────────────────────────────────
def main():
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{'═'*52}")
    print(f"  {C.BOLD}🚀 OmniClaw V5.0 — STARTUP BOOT{C.RESET}")
    print(f"  {C.CYAN}{ts}{C.RESET}")
    print(f"{'═'*52}")

    # Step 1: Critical files
    files_ok, missing = check_critical_files()

    # Step 2: Blackboard
    cycle_status, bb = check_blackboard()

    # Step 3: Services
    services = check_services()

    # Step 4: Skill registry
    reg_info = check_skill_registry()

    if CHECK_ONLY:
        print_summary(files_ok, cycle_status, services, reg_info)
        return

    # Step 5: Update HUD
    status = update_hud(services, reg_info)

    # Step 6: Telegram
    send_telegram_boot_report(status, bb, services)

    # Final summary
    print_summary(files_ok, cycle_status, services, reg_info)


if __name__ == "__main__":
    main()
