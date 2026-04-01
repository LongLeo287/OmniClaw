#!/usr/bin/env python3
"""
AOS START - OmniClaw Cognitive Boot Protocol v1.0
Owner: Antigravity | Based on GEMINI.md SECTION 2 Boot Sequence
"""

import os, json, datetime, sys, subprocess
import io

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
os.environ.setdefault('PYTHONIOENCODING', 'utf-8')

CYAN   = "\033[96m"
GREEN  = "\033[92m"
YELLOW = "\033[93m"
RED    = "\033[91m"
GRAY   = "\033[90m"
BOLD   = "\033[1m"
RESET  = "\033[0m"

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.."))

BOOT_FILES = [
    (1, "GEMINI.md              (Entry Point)",      "GEMINI.md",                                          True),
    (2, "SOUL.md                (Identity)",         "brain/shared-context/SOUL.md",                       True),
    (3, "GOVERNANCE.md          (Rules)",            "brain/shared-context/GOVERNANCE.md",                 True),
    (4, "AGENTS.md              (Roster)",           "brain/shared-context/AGENTS.md",                     True),
    (5, "THESIS.md              (Strategy)",         "brain/shared-context/THESIS.md",                     False),
    (6, "report_formats.md      (Output Format)",    "brain/shared-context/report_formats.md",             False),
    (7, "event_bus.db           (Task Pub/Sub)",     "brain/shared-context/event_bus.db",                  False),
    (8, "SKILL_REGISTRY.json    (Skill Registry)",   "ecosystem/skills/SKILL_REGISTRY.json",           False),
]

def banner():
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"\n{CYAN}{BOLD}{'='*60}{RESET}")
    print(f"{CYAN}{BOLD}  OmniClaw CORP - COGNITIVE BOOT PROTOCOL{RESET}")
    print(f"{CYAN}{BOLD}  Antigravity | Boot v1.0 | {now}{RESET}")
    print(f"{CYAN}{BOLD}{'='*60}{RESET}\n")

def check_file(step, label, rel_path, required):
    full_path = os.path.join(ROOT, rel_path)
    exists = os.path.exists(full_path)

    if exists:
        size = os.path.getsize(full_path)
        size_label = f"{size//1024}KB" if size > 1024 else f"{size}B"

        status = f"{GREEN}✓{RESET}"
        if full_path.endswith('.json'):
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    json.load(f)
            except Exception as e:
                status = f"{RED}SYNTAX ERROR{RESET}"
                print(f"  {RED}[STEP {step:02d}] ✗  {label:<42} {RED}(JSON Parse Error: {e}){RESET}")
                return False, full_path

        print(f"  {GREEN}[STEP {step:02d}] {status}{RESET}  {label:<42} {GRAY}({size_label}){RESET}")
        return True, full_path
    else:
        marker = f"{RED}[MISSING]{RESET}" if required else f"{YELLOW}[SKIP]{RESET}"
        print(f"  {marker} [STEP {step:02d}]  {label}")
        return False, None

def check_event_bus():
    try:
        sys.path.append(ROOT)
        from system.ops.scripts.agent_bus import AgentBus
        bus = AgentBus()
        cnt = bus.get_pending_count()

        print(f"\n  {CYAN}── EVENT BUS (PUB/SUB) ────────────────────────────{RESET}")
        print(f"  {BOLD}📡 Task Signals:{RESET} {YELLOW}{cnt} PENDING TASKS{RESET} in queue")

        bus.cursor.execute("SELECT id, topic, status, picked_by, payload FROM events WHERE status='PENDING' ORDER BY id ASC LIMIT 5")
        rows = bus.cursor.fetchall()
        if rows:
            for r in rows:
                payload_obj = {}
                try: payload_obj = json.loads(r[4]) if r[4] else {}
                except: pass
                task_desc = payload_obj.get('task', 'No description')
                print(f"     • [{r[1]:<10}] ID:{r[0]:03d} - {task_desc}")
            if cnt > 5:
                print(f"     {GRAY}... and {cnt-5} other signals{RESET}")
        else:
            print(f"  {GREEN}✓ Workforce is idle. Event Bus is clear.{RESET}")

    except Exception as e:
        print(f"  {YELLOW}[WARN] Cannot access Event Bus: {e}{RESET}")

def read_skill_registry(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            reg = json.load(f)

        entries = reg.get('skills', [])
        active = [e for e in entries if str(e.get('status')).lower() == 'active']
        count  = reg.get('count', len(entries))

        print(f"\n  {CYAN}── SKILL REGISTRY ─────────────────────────────────{RESET}")
        print(f"  {BOLD}🎛️  Skills registered:{RESET} {count} total | {GREEN}{len(active)} active{RESET}")

        domains = {}
        for e in active:
            d = e.get('domain', 'unknown')
            domains[d] = domains.get(d, 0) + 1
        for dom, cnt in sorted(domains.items()):
            print(f"     {dom:<15} {cnt} skills")

    except Exception as e:
        print(f"  {YELLOW}[WARN] Cannot parse SKILL_REGISTRY: {e}{RESET}")

def check_environment():
    print(f"\n  {CYAN}── SYSTEM ENVIRONMENT ───────────────────────────────{RESET}")
    py_ver = sys.version.split()[0]
    print(f"  {BOLD}🐍 Python:{RESET} {py_ver}")
    try:
        branch = subprocess.check_output(["git", "branch", "--show-current"], cwd=ROOT, stderr=subprocess.DEVNULL).decode().strip()
        print(f"  {BOLD}🌿 Git Branch:{RESET} {branch}")
    except:
        print(f"  {BOLD}🌿 Git Branch:{RESET} {YELLOW}Not a git repository{RESET}")

    env_path = os.path.join(ROOT, "system/ops/secrets/MASTER.env")
    if os.path.exists(env_path):
        size = os.path.getsize(env_path)
        print(f"  {BOLD}🔐 MASTER.env:{RESET} {GREEN}Loaded ({size} bytes){RESET}")
    else:
        print(f"  {BOLD}🔐 MASTER.env:{RESET} {RED}MISSING! Autonomous execution will fail.{RESET}")

def check_knowledge_pulse():
    print(f"\n  {CYAN}── KNOWLEDGE PULSE ────────────────────────────────{RESET}")
    active_path = os.path.join(ROOT, "storage/vault/DATA/ACTIVE_REPOS.md")
    pending_path = os.path.join(ROOT, "storage/vault/DATA/PENDING_REPOS.md")

    def count_links(p):
        if not os.path.exists(p): return 0
        with open(p, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip().startswith("- [") and "](http" in line)

    active_cnt = count_links(active_path)
    pending_cnt = count_links(pending_path)

    print(f"  {BOLD}📚 Repositories:{RESET} {GREEN}{active_cnt} Active{RESET} | {YELLOW}{pending_cnt} Pending{RESET} in System Vault")

def check_memory_core():
    print(f"\n  {CYAN}── LONG-TERM MEMORY (LTM) ─────────────────────────{RESET}")
    try:
        sys.path.append(ROOT)
        from system.ops.scripts.memory_daemon import MemoryCore
        core = MemoryCore()
        memories = core.get_all()
        count = len(memories) if memories else 0
        print(f"  {BOLD}🧠 Cortex Status:{RESET} {GREEN}ONLINE & READY{RESET}")
        print(f"  {BOLD}📚 Total Memories:{RESET} {count} Neural Nodes mapped in Vector Database")
    except Exception:
        print(f"  {BOLD}🧠 Cortex Status:{RESET} {YELLOW}OFFLINE / SYNCING{RESET}")

def check_automations():
    print(f"\n  {CYAN}── AUTOMATIONS & DAEMONS ──────────────────────────{RESET}")
    auto_path = os.path.join(ROOT, "system/automations/AUTOMATION_REGISTRY.yaml")
    if not os.path.exists(auto_path):
        print(f"  {YELLOW}Registry missing.{RESET}")
        return

    try:
        import yaml
        with open(auto_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        automations = data.get('automations', {})
        active    = [(k, a) for k, a in automations.items() if a.get('status') == 'active']
        paused    = [(k, a) for k, a in automations.items() if a.get('status') == 'paused']
        on_demand = [(k, a) for k, a in automations.items() if a.get('status') == 'on_demand']
        print(f"  {BOLD}⚙️  Daemons:{RESET} {GREEN}{len(active)} active{RESET} | {YELLOW}{len(paused)} paused{RESET} | {GRAY}{len(on_demand)} on-demand{RESET} / {len(automations)} total")
        for k, a in active[:3]:
            path_show = str(a.get('path', k))[:40]
            print(f"     • {path_show}...")
        if len(active) > 3:
            print(f"     {GRAY}... and {len(active)-3} more{RESET}")
        if paused:
            print(f"   {YELLOW}  Paused:{RESET} {', '.join(k for k,_ in paused)}")
    except ImportError:
        print(f"  {YELLOW}[WARN] PyYAML not installed. Fallback to basic mode.{RESET}")
    except Exception as e:
        print(f"  {RED}Error parsing yaml: {e}{RESET}")

def boot_summary(results):
    ok      = sum(1 for ok, _ in results if ok)
    total   = len(results)
    missing = [(step, label) for (step, label, _, req), (ok, _) in zip(BOOT_FILES, results) if not ok and req]

    print(f"\n{CYAN}{'='*60}{RESET}")
    print(f"  Boot result: {GREEN if not missing else RED}{ok}/{total}{RESET} components loaded")

    if missing:
        print(f"\n  {RED}⚠ MISSING REQUIRED COMPONENTS:{RESET}")
        for step, label in missing:
            print(f"    STEP {step:02d}: {label}")
        print(f"\n  {YELLOW}Boot INCOMPLETE - Resolve missing assets before continuing.{RESET}")
    else:
        print(f"\n  {GREEN}{BOLD}☀ SYSTEM ONLINE. READY FOR DAILY CYCLE.{RESET}")
        print(f"\n  {BOLD}AVAILABLE COMMANDS:{RESET}")
        print(f"  {GRAY}  aos corp start   -> Initiate daily routine{RESET}")
        print(f"  {GRAY}  aos hud          -> Display operations dashboard{RESET}")
        print(f"  {GRAY}  aos ingest <url> -> Append external intelligence{RESET}")

    print(f"{CYAN}{'='*60}{RESET}\n")

if __name__ == "__main__":
    banner()
    check_environment()
    check_knowledge_pulse()
    check_memory_core()
    check_automations()

    print(f"\n  {BOLD}── BOOT SEQUENCE ───────────────────────────────────{RESET}")
    results = []
    bb_path   = None
    sk_path   = None

    for step, label, rel, required in BOOT_FILES:
        ok, path = check_file(step, label, rel, required)
        results.append((ok, path))
        if step == 7 and ok: bb_path = path
        if step == 8 and ok: sk_path = path

    if bb_path: check_event_bus()
    if sk_path: read_skill_registry(sk_path)
    
    boot_summary(results)