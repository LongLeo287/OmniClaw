import os
import sys
import time
import json
import logging
import uuid
import subprocess
import shutil
from datetime import datetime
from pathlib import Path

# --- Initialization & Path Logic ---
current_file = Path(__file__).resolve()
AOS_ROOT = current_file.parent
while AOS_ROOT != AOS_ROOT.parent and not ((AOS_ROOT / "system").is_dir() and (AOS_ROOT / "brain").is_dir()):
    AOS_ROOT = AOS_ROOT.parent

if not ((AOS_ROOT / "system").is_dir() and (AOS_ROOT / "brain").is_dir()):
    AOS_ROOT = Path(os.getenv("AOS_ROOT", os.getcwd()))

sys.path.insert(0, str(AOS_ROOT))
try:
    from system.infra.notifications.telegram_dispatch import send_telegram_alert
except ImportError:
    def send_telegram_alert(msg, **kwargs):
        print(f"[FALLBACK TELEGRAM] {msg}")

# --- Constants & Configurations ---
DAEMON_NAME = "omniclaw_ohd_daemon"
PID_FILE = current_file.parent / "ohd.pid"
VAULT_QUARANTINE = AOS_ROOT / "storage" / "vault" / "FAILED_QUARANTINE"
OA_DISPATCH_QUEUE = AOS_ROOT / "storage" / "vault" / "OA_DISPATCH_QUEUE"
TRIGGER_DIR = AOS_ROOT / "storage" / "vault" / "OHD_TRIGGER"
LOG_DIR = AOS_ROOT / "storage" / "logs" / "daemons"
LOG_FILE = LOG_DIR / f"{DAEMON_NAME}.log"

# Polling intervals
IDLE_SLEEP_SECONDS = 60
CRON_SCAN_INTERVAL_SECONDS = 7 * 24 * 3600  # 7 days

def setup_logging():
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | OHD-MEDICAL | %(levelname)s | %(message)s',
        handlers=[
            logging.FileHandler(LOG_FILE, encoding='utf-8-sig'),
            logging.StreamHandler(sys.stdout)
        ]
    )

def ensure_directories():
    for d in [VAULT_QUARANTINE, OA_DISPATCH_QUEUE, TRIGGER_DIR]:
        d.mkdir(parents=True, exist_ok=True)

def lock_pid():
    if PID_FILE.exists():
        try:
            old_pid = int(PID_FILE.read_text().strip())
            os.kill(old_pid, 0)
            logging.error(f"OHD Daemon is already running (PID: {old_pid}). Aborting.")
            sys.exit(1)
        except (OSError, ValueError):
            logging.warning("Found stale PID file. Overwriting.")
            
    PID_FILE.write_text(str(os.getpid()))
    logging.info(f"Locked PID: {os.getpid()} for {DAEMON_NAME}")

def check_triggers():
    """Returns True if there is a manual trigger file, and consumes it."""
    triggered = False
    for f in TRIGGER_DIR.glob("*.trigger"):
        triggered = True
        try:
            f.unlink()
            logging.info(f"Consumed external trigger: {f.name}")
        except Exception as e:
            logging.error(f"Failed to delete trigger {f.name}: {e}")
    return triggered

def sweep_and_quarantine():
    """Call the existing cleanup crew but instruct it to move trash to FAILED_QUARANTINE instead of deleting."""
    logging.info("Initiating Sweep & Quarantine via cleanup crew...")
    crew_script = AOS_ROOT / "system" / "ops" / "scripts" / "omniclaw_cleanup_crew.py"
    
    if not crew_script.exists():
        logging.error("omniclaw_cleanup_crew.py not found! Cannot sweep.")
        return 0
        
    try:
        # Pass the quarantine flag to enforce ZERO DELETION rule
        # NOTE: cleanup_crew must be updated to accept --quarantine-path
        result = subprocess.run(
            [sys.executable, str(crew_script), "--quarantine-path", str(VAULT_QUARANTINE)],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            logging.warning(f"Cleanup crew reported non-zero exit code: {result.stderr}")
        
        # --- Sweep Dead Claude Worktrees ---
        claude_worktrees_dir = AOS_ROOT / ".claude/worktrees"
        if claude_worktrees_dir.exists():
            for wt in claude_worktrees_dir.iterdir():
                if wt.is_dir():
                    try:
                        res = subprocess.run(["git", "status"], cwd=str(wt), capture_output=True, text=True)
                        if res.returncode != 0 and "fatal: not a git repository" in res.stderr.lower():
                            dest = VAULT_QUARANTINE / f"DEAD_WORKTREE_{wt.name}"
                            shutil.move(str(wt), str(dest))
                            logging.warning(f"☠ Quarantined DEAD Claude Worktree: {wt.name}")
                    except Exception as e:
                        logging.error(f"Failed to scan worktree {wt.name} for garbage collection: {e}")

        # Count items currently in quarantine
        garbage_count = sum(1 for _ in VAULT_QUARANTINE.glob('DEAD_WORKTREE_*')) + sum(1 for _ in VAULT_QUARANTINE.rglob('*') if _.is_file())
        logging.info(f"Quarantine sweeping complete. Total garbage in Vault: {garbage_count} items")
        return garbage_count
    except Exception as e:
        logging.error(f"Error running cleanup crew: {e}")
        return 0

def generate_system_map():
    """Call the official OmniClaw OS state snapshot generator instead of reinventing the wheel."""
    logging.info("Updating OmniClaw System Map via os_state_snapshot.py...")
    snapshot_script = AOS_ROOT / "ecosystem" / "workforce" / "system" / "education" / "archivist" / "tools" / "os_state_snapshot.py"
    if snapshot_script.exists():
        try:
            result = subprocess.run([sys.executable, str(snapshot_script)], capture_output=True, text=True)
            if result.returncode == 0:
                logging.info("System Map updated perfectly.")
            else:
                logging.warning(f"System Map update warning: {result.stderr}")
        except Exception as e:
            logging.error(f"Failed to run os_state_snapshot.py: {e}")
    else:
        logging.error("os_state_snapshot.py not found! Cannot map system.")

def audit_and_heal_entities():
    """Scan ecosystem and brain for broken structure, missing skills, or bad naming, and attempt auto-healing."""
    generate_system_map()
    logging.info("Auditing System Entities & Auto-Healing...")
    issues = []
    
    # 1. Simple Agent Integrity Check (Orphaned Departments)
    workforce_dir = AOS_ROOT / "ecosystem" / "workforce"
    if workforce_dir.exists():
        for dept in workforce_dir.iterdir():
            if dept.is_dir() and dept.name not in ["system", "agents"]:
                agent_dirs = [d for d in dept.iterdir() if d.is_dir()]
                if not agent_dirs:
                    issues.append(f"Orphaned Department detected (Empty): {dept.name}")
                    
    # 2. Healing Loops (UTF-8, JSON, Naming)
    # Search the ENTIRE OmniClaw architecture
    scan_dirs = ["system", "ecosystem", "brain", "storage", "docs"]
    for d_name in scan_dirs:
        target = AOS_ROOT / d_name
        if not target.exists():
            continue
            
        for ext in ["*.md", "*.json", "*.yaml", "*.py"]:
            for file_path in target.rglob(ext):
                # Skip 3rd-party source code directories and raw data
                excluded_parts = {"node_modules", ".git", "repos", "plugins", "QUARANTINE", "tmp", "__pycache__", ".venv", "prompts"}
                if set(file_path.parts) & excluded_parts:
                    continue
                
                # --- Auto-fix Naming (Kebab-case enforce) ---
                if " " in file_path.name:
                    clean_name = file_path.name.replace(" ", "-").lower()
                    new_path = file_path.with_name(clean_name)
                    try:
                        file_path.rename(new_path)
                        logging.info(f"Auto-Healed Naming: {file_path.name} -> {clean_name}")
                        file_path = new_path
                    except Exception as e:
                        issues.append(f"Could not rename {file_path.name}: {e}")
                
                # --- Hardcode Encoding Standard (Split-Encoding Policy) ---
                if file_path.is_file() and file_path.suffix in [".md", ".json", ".yaml"]:
                    try:
                        if file_path.stat().st_size > 20 * 1024 * 1024:
                            continue # Skip huge files (> 20MB) to prevent memory overload
                            
                        # 1. Determine Target Encoding Protocol
                        is_vietnamese = file_path.name.lower().endswith("-vn.md") or file_path.name.lower().endswith("_vn.md")
                        
                        # 2. Probe byte signature
                        raw_bytes = file_path.read_bytes()
                        has_bom = raw_bytes.startswith(b'\xef\xbb\xbf')
                        
                        needs_rewrite = False
                        target_enc = "utf-8-sig" if is_vietnamese else "utf-8"
                        
                        # Enforce BOM Rules
                        if is_vietnamese and not has_bom:
                            needs_rewrite = True
                        elif not is_vietnamese and has_bom:
                            needs_rewrite = True
                            
                        # Validate UTF-8 Integrity & Heal Mojibake
                        content = None
                        try:
                            content = raw_bytes.decode('utf-8-sig' if has_bom else 'utf-8')
                        except UnicodeDecodeError:
                            # File is currently corrupted/ANSI, needs deep healing
                            needs_rewrite = True
                            try:
                                content = raw_bytes.decode('cp1258') # Recover from Windows Vietnamese ANSI
                            except UnicodeDecodeError:
                                content = raw_bytes.decode('utf-8', errors='replace') # Destructive fallback
                        
                        if needs_rewrite and content is not None:
                            try:
                                file_path.write_text(content, encoding=target_enc)
                                logging.info(f"Auto-Healed Encoding (Hardcoded {target_enc}): {file_path.name}")
                            except PermissionError:
                                logging.warning(f"Encoding rewrite blocked (Permission Denied): {file_path.name}")
                                
                    except Exception as e:
                        issues.append(f"Encoding Healing Failed for {file_path.name}: {e}")

                # --- Open-Source Agnostic Guardian (Detect Hardcoded Usernames Globally) ---
                # Exclude this daemon file to prevent self-flagging
                if file_path.name != "omniclaw_ohd_daemon.py":
                    try:
                        content = file_path.read_text(encoding="utf-8")
                        target_1, target_2 = "Long" + "Leo", "Long" + "Leo" + "287"
                        if target_1 in content or target_2 in content or "D:\\" + target_1 in content:
                            issues.append(f"OS-AGNOSTIC VIOLATION: Hardcoded username detected in {file_path.relative_to(AOS_ROOT)}")
                            logging.warning(f"🚨 [HARDCODE ALERT] Found local identity in {file_path.name}! Codebase must be decoupled for Open-Source.")
                            
                        # --- Auto-fix Branding: OmniClaw Corp -> OmniClaw ---
                        if "OmniClaw Corp" in content:
                            content = content.replace("OmniClaw Corp", "OmniClaw")
                            file_path.write_text(content, encoding="utf-8")
                            logging.info(f"Auto-Healed Branding (Corp removed): {file_path.name}")
                    except Exception:
                        pass

                # --- Isolate Broken JSON (For OA) ---
                if file_path.suffix == ".json":
                    try:
                        with open(file_path, "r", encoding="utf-8") as f:
                            json.load(f)
                    except json.JSONDecodeError as e:
                        issues.append(f"JSON Syntax Error in {file_path.relative_to(AOS_ROOT)}: {e}")
                        broken_dest = VAULT_QUARANTINE / f"BROKEN_{file_path.name}"
                        try:
                            import shutil
                            shutil.move(str(file_path), str(broken_dest))
                            logging.warning(f"Moved broken JSON to Vault: {broken_dest.name}")
                        except Exception:
                            pass
                
                # --- Isolate Broken YAML (For OA) ---
                if file_path.suffix == ".yaml":
                    try:
                        import yaml
                        with open(file_path, "r", encoding="utf-8") as f:
                            yaml.safe_load(f)
                    except Exception as e:
                        issues.append(f"YAML Syntax Error in {file_path.relative_to(AOS_ROOT)}: {str(e)[:100]}")
                        broken_dest = VAULT_QUARANTINE / f"BROKEN_{file_path.name}"
                        try:
                            import shutil
                            shutil.move(str(file_path), str(broken_dest))
                            logging.warning(f"Moved broken YAML to Vault: {broken_dest.name}")
                        except Exception:
                            pass
                
    if issues:
        logging.warning(f"Detected {len(issues)} structural issues requiring OA intervention.")
    return issues

def auto_heal_terminal_ime():
    """OHD Native TUI Vaccine: Heals Node.js/Ink terminals from \\x7f input buffer crashes caused by Vietnamese IME."""
    logging.info("Running Terminal IME Auto-Heal (Vaccine)...")
    issues = []
    
    # 1. Heal Claude Code (Default Native Target)
    try:
        # Use shell=True for npx on Windows to prevent 'file not found' cmd resolution errors
        res = subprocess.run("npx -y fix-vietnamese-claude-code", shell=True, capture_output=True, text=True)
        if "already patched" not in res.stdout.lower() and "Success" in res.stdout:
            logging.info("OHD successfully patched Claude Code for Vietnamese IME.")
    except Exception as e:
        logging.warning(f"Failed to run IME patch for Claude Code: {e}")
        
    # 2. Heal OmniClaw / Antigravity Custom Targets
    targets_config = current_file.parent / "ime_targets.json"
    if targets_config.exists():
        try:
            with open(targets_config, 'r', encoding='utf-8') as f:
                targets = json.load(f)
            for target_path in targets.get("patch_files", []):
                p = Path(target_path)
                if p.exists():
                    if p.suffix in ['.js', '.cmd', '.exe'] or not p.suffix:
                        res = subprocess.run(f'npx -y fix-vietnamese-claude-code -f "{str(p)}"', shell=True, capture_output=True, text=True)
                        if "already patched" not in res.stdout.lower() and "Success" in res.stdout:
                            logging.info(f"OHD successfully patched Node.js CLI for Vietnamese IME: {p.name}")
                    elif p.suffix == '.py':
                        healer_script_path = current_file.parent / "scripts" / "python_ime_healer.py"
                        healer_dir = str(healer_script_path.parent).replace('\\', '\\\\')
                        injection_string = f'# [OHD MEDICAL VACCINE]\nimport sys; sys.path.insert(0, r"{healer_dir}"); try: import python_ime_healer except ImportError: pass\n'
                        try:
                            content = p.read_text(encoding='utf-8')
                            if "# [OHD MEDICAL VACCINE]" not in content:
                                p.write_text(injection_string + content, encoding='utf-8')
                                logging.info(f"OHD successfully injected Python IME Healer into: {p.name}")
                        except Exception as inner_e:
                            logging.warning(f"Failed to inject Python healer into {p.name}: {inner_e}")
        except Exception as e:
            issues.append(f"Failed to process ime_targets.json: {e}")
            logging.error(f"IME Target processing error: {e}")
            
    return issues

def dispatch_to_oa(garbage_count, structural_issues):
    """If there are heavy issues or trash, OHD notifies OA (OmniClaw Academy) by Email API/Queue."""
    if garbage_count == 0 and not structural_issues:
        logging.info("System is perfectly healthy. No OA dispatch needed.")
        return
        
    logging.info("System anomalies detected. Dispatching Emergency Ticket to OmniClaw Academy (OA)...")
    
    ticket_id = f"OA_DISPATCH_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:6]}"
    dispatch_file = OA_DISPATCH_QUEUE / f"{ticket_id}.json"
    
    payload = {
        "ticket_id": ticket_id,
        "timestamp": datetime.now().isoformat(),
        "origin": "OHD_MEDICAL",
        "urgency": "HIGH" if structural_issues else "LOW",
        "metrics": {
            "garbage_items_awaiting_post_mortem": garbage_count,
            "structural_issues_count": len(structural_issues)
        },
        "issues_details": structural_issues,
        "status": "PENDING_OA_ACK"
    }
    
    try:
        dispatch_file.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')
        logging.info(f"Generated Dispatch Ticket: {dispatch_file.name}")
        
        # Ping CEO
        msg = (
            f"🚨 <b>[OHD MEDICAL ALERT]</b>\n"
            f"Status: Anomaly Detected (Dispatch sent to OA)\n"
            f"Quarantined Items: {garbage_count} files (Awaiting OA post-mortem)\n"
            f"Structural/Format Issues: {len(structural_issues)} errors\n"
            f"Required Action: Wait for OA to process before emptying the Vault."
        )
        send_telegram_alert(msg, thread_topic="OHD")
    except Exception as e:
        logging.error(f"Failed to create OA Dispatch: {e}")

def check_git_hygiene():
    """Git Sentinel Module: Prevents secrets & heavy junk from entering the repo"""
    import subprocess
    logging.info("[GIT SENTINEL] Scanning tracked files for hygiene...")
    try:
        result = subprocess.run(["git", "ls-files"], cwd=str(AOS_ROOT), capture_output=True, text=True, check=True)
        tracked_files = result.stdout.strip().split('\n')
        
        leaked_files = []
        for f in tracked_files:
            if not f: continue
            
            p = Path(f)
            # Rule 1: Secrets (.env files that are not examples)
            is_env = p.suffix == ".env" and "example" not in p.name.lower() and "template" not in p.name.lower()
            # Rule 2: Logs
            is_log = p.suffix == ".log"
            # Rule 3: Protected Memory (dynamic runtime files must not be tracked)
            is_history = "brain/corp/memory/" in f.replace('\\', '/') and p.suffix in [".md", ".json"] and p.name != "MEMORY_SPEC.md"
            # Rule 4: Heavy blobs (>50MB) 
            is_heavy = False
            full_p = AOS_ROOT / f
            
            # --- Whitelist Overrides: Never untrack templates or gitkeeps ---
            is_whitelisted = p.name.endswith(".template.md") or p.name.endswith(".template") or p.name == ".gitkeep"
            
            if full_p.exists() and not is_whitelisted:
                if full_p.stat().st_size > 50 * 1024 * 1024:
                    is_heavy = True
                    
            if (is_env or is_log or is_history or is_heavy) and not is_whitelisted:
                leaked_files.append(f)
                
        if leaked_files:
            logging.warning(f"🚨 [GIT LEAK DETECTED] Found {len(leaked_files)} violating files tracked in Git!")
            for lf in leaked_files:
                logging.warning(f"   -> Untracking: {lf}")
                subprocess.run(["git", "rm", "--cached", lf], cwd=str(AOS_ROOT), capture_output=True)
            logging.info("[GIT SENTINEL] Leak sealed successfully.")
            
        # --- Rule 5: Registry Guard (Hardcoded Path Audit) ---
        registry_path = AOS_ROOT / "brain" / "core" / "registry.json"
        if registry_path.exists():
            reg_content = registry_path.read_text(encoding='utf-8')
            if "D:\\" in reg_content or "C:\\" in reg_content:
                # We alert but don't auto-fix specifically because path variables vary
                logging.error(f"🚨 [REGISTRY LEAK] Hardcoded local paths detected in {registry_path.name}! Use $WORKSPACE_ROOT instead.")
                leaked_files.append(str(registry_path.relative_to(AOS_ROOT)))
                
        return leaked_files
            
    except Exception as e:
        logging.error(f"[GIT SENTINEL] Failed to run hygiene check: {e}")
    return []

def run_daemon():
    setup_logging()
    ensure_directories()
    lock_pid()
    
    logging.info(f"===")
    logging.info(f"🚀 OHD Daemon Initialized. Zero-Deletion Policy ACTIVATED.")
    logging.info(f"Vault Quarantine: {VAULT_QUARANTINE}")
    logging.info(f"===")
    
    last_cron_time = time.time() - CRON_SCAN_INTERVAL_SECONDS + 10 # trigger immediately on boot
    
    try:
        while True:
            current_time = time.time()
            triggered_by_file = check_triggers()
            triggered_by_cron = (current_time - last_cron_time) >= CRON_SCAN_INTERVAL_SECONDS
            
            if triggered_by_file or triggered_by_cron:
                reason = "External Prompt" if triggered_by_file else "1-Week Cron"
                logging.info(f"[*] Waking up OHD for Health Check (Trigger: {reason})")
                
                garbage_count = sweep_and_quarantine()
                issues = audit_and_heal_entities()
                
                # --- OHD Terminal Health (IME Fix) ---
                ime_issues = auto_heal_terminal_ime()
                issues.extend(ime_issues)
                
                leaks = check_git_hygiene()
                
                if leaks:
                    issues.extend([f"GIT_LEAK_SEALED: {l}" for l in leaks])
                dispatch_to_oa(garbage_count, issues)
                
                if triggered_by_cron:
                    last_cron_time = current_time
                
            time.sleep(IDLE_SLEEP_SECONDS)
            
    except KeyboardInterrupt:
        logging.info("OHD Daemon manually interrupted. Shutting down gracefully.")
    except Exception as e:
        logging.exception(f"CRITICAL OHD DAEMON CRASH: {e}")
        send_telegram_alert(f"💥 <b>CRITICAL OHD DAEMON CRASH!</b> Error: {str(e)[:100]}")
    finally:
        if PID_FILE.exists():
            PID_FILE.unlink()
        logging.info("OHD Daemon Terminated.")

if __name__ == "__main__":
    run_daemon()
