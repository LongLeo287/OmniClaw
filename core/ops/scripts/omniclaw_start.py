#!/usr/bin/env python3
"""
OmniClaw Start - OmniClaw Cognitive Boot Protocol v1.0
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
    (2, "OMA_SYSTEM_MAP.json    (System Topology)",  "brain/registry/OMA_SYSTEM_MAP.json",                 True),
    (3, "config.json            (System Config)",    "core/config/config.json",                            True),
    (4, "AGENTS.md              (Roster)",           "brain/registry/AGENTS.md",                           True),
    (5, "neural_bus.db          (Neural Bus MQ)",    "vault/tmp/neural_bus.db",                            False),
    (6, "SKILL_REGISTRY.json    (Skill Registry)",   "brain/registry/SKILL_REGISTRY.json",                 False),
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
        import sqlite3
        db_path = os.path.join(ROOT, "vault/tmp/neural_bus.db")
        if not os.path.exists(db_path):
            print(f"\n  {CYAN}── CỘT SỐNG NEURAL BUS (MQ) ───────────────────────{RESET}")
            print(f"  {GREEN}✓ Mạng nhàn rỗi. Chưa khởi tạo Cột sống DB.{RESET}")
            return
            
        con = sqlite3.connect(db_path)
        cur = con.cursor()
        
        # Check if table exists
        cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='neural_queue'")
        if not cur.fetchone():
            print(f"\n  {CYAN}── CỘT SỐNG NEURAL BUS (MQ) ───────────────────────{RESET}")
            print(f"  {GREEN}✓ Mạng nhàn rỗi. Neural Bus rỗng.{RESET}")
            con.close()
            return
            
        cur.execute("SELECT id, queue_name, status FROM neural_queue WHERE status='PENDING' ORDER BY id ASC LIMIT 5")
        rows = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM neural_queue WHERE status='PENDING'")
        cnt = cur.fetchone()[0]
        con.close()

        print(f"\n  {CYAN}── CỘT SỐNG NEURAL BUS (MQ) ───────────────────────{RESET}")
        print(f"  {BOLD}📡 Tín hiệu cần xử lý:{RESET} {YELLOW}{cnt} TÁC VỤ ĐANG CHỜ{RESET}")

        if rows:
            for r in rows:
                print(f"     • [{r[1]:<10}] ID:{r[0]:03d}")
            if cnt > 5:
                print(f"     {GRAY}... và {cnt-5} tác vụ khác{RESET}")
        else:
            print(f"  {GREEN}✓ Hệ thống nhánh rỗi. Neural Bus sạch sẽ.{RESET}")

    except Exception as e:
        print(f"  {YELLOW}[WARN] Không thể truy cập Neural Bus: {e}{RESET}")

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

    env_path = os.path.join(ROOT, ".env")
    if os.path.exists(env_path):
        size = os.path.getsize(env_path)
        print(f"  {BOLD}🔐 OS .env File:{RESET} {GREEN}Loaded ({size} bytes){RESET}")
    else:
        print(f"  {BOLD}🔐 OS .env File:{RESET} {YELLOW}MISSING! (Falling back to OS Vars){RESET}")

def check_knowledge_pulse():
    print(f"\n  {CYAN}── CHỈ SỐ HUYẾT ÁP TRI THỨC (KNOWLEDGE PULSE) ───────{RESET}")
    active_path = os.path.join(ROOT, "vault/assets/data/repos_selected.txt")
    pending_path = os.path.join(ROOT, "vault/assets/data/repos_pending.txt")

    def count_lines(p):
        if not os.path.exists(p): return 0
        with open(p, 'r', encoding='utf-8') as f:
            return sum(1 for line in f if line.strip())

    active_cnt = count_lines(active_path)
    pending_cnt = count_lines(pending_path)

    print(f"  {BOLD}📚 Kho Repo (Inbox):{RESET} {GREEN}{active_cnt} Đã Chọn (Đặc Quyền){RESET} | {YELLOW}{pending_cnt} Đang Chờ Xử Lý{RESET} trong Vault")

def check_memory_core():
    print(f"\n  {CYAN}── LONG-TERM MEMORY (LTM) ─────────────────────────{RESET}")
    try:
        brain_path = os.path.join(ROOT, "brain", "knowledge")
        if os.path.exists(brain_path):
            count = sum(len(files) for _, _, files in os.walk(brain_path))
            print(f"  {BOLD}🧠 Cortex Status:{RESET} {GREEN}ONLINE & READY{RESET}")
            print(f"  {BOLD}📚 Total Memories:{RESET} {count} Tệp Tri thức (Knowledge Nodes) đã được thiết lập.")
        else:
            print(f"  {BOLD}🧠 Cortex Status:{RESET} {YELLOW}OFFLINE / CHƯA ĐỒNG BỘ{RESET}")
    except Exception:
        print(f"  {BOLD}🧠 Cortex Status:{RESET} {YELLOW}OFFLINE / ERROR{RESET}")

def check_automations():
    print(f"\n  {CYAN}── CORE DAEMONS (HỆ THỐNG NGẦM) ───────────────────{RESET}")
    daemons_path = os.path.join(ROOT, "core", "daemons")
    
    if not os.path.exists(daemons_path):
        print(f"  {YELLOW}Không tìm thấy thư mục Daemons.{RESET}")
        return

    try:
        daemons = [f for f in os.listdir(daemons_path) if f.endswith('.py') and not f.startswith('__')]
        active_count = len(daemons)
        print(f"  {BOLD}⚙️  Daemons Khả dụng:{RESET} {GREEN}{active_count} Core files{RESET}")
        
        for d in daemons[:5]:
            print(f"     • {d}")
        if active_count > 5:
            print(f"     {GRAY}... và {active_count - 5} scripts khác{RESET}")
    except Exception as e:
        print(f"  {RED}Lỗi truy xuất Daemons: {e}{RESET}")

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
        print(f"  {GRAY}  omniclaw start   -> Initiate daily routine{RESET}")
        print(f"  {GRAY}  omniclaw hud          -> Display operations dashboard{RESET}")
        print(f"  {GRAY}  omniclaw ingest <url> -> Append external intelligence{RESET}")

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