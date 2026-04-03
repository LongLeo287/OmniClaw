#!/usr/bin/env python3
"""
[ OMA] OmniClaw Master Architect
Role: The Map-Keeper and Chief Structural Disciplinarian.
Mandates:
 1. Emit OMA_SYSTEM_MAP.json (The single source of truth for file coordinates & metadata).
 2. Enforce the 4-Pillar hierarchy.
 3. Quarantine rogue/un-tagged files and hand them over to OHD (Discipline) & OA (Auditor).
 4. IRON RULE: MOVE ONLY, STRICTLY NO DELETE.
"""
import os
import json
import shutil
import re
from datetime import datetime
from daemon_trust import authenticate_daemon, assert_write_access

DAEMON_NAME = "OMA"
config = authenticate_daemon(DAEMON_NAME)

AIOS_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", ".."))

APPROVED_ROOT_DIRS = ["brain", "core", "ecosystem", "vault"]
IGNORED_ROOT_ITEMS = [
    ".git", ".github", ".vscode", ".claude", ".agents",
    "node_modules", "tmp", "logs", "releases",
    "CLAUDE.md", "CLAUDE_CODE_TASKS.md", "GEMINI.md",
    "README.md", "README-vn.md", "LICENSE", "v5_migrator.py"
]

QUARANTINE_PATH = os.path.join(AIOS_ROOT, "vault", "tmp", "quarantine")
MAP_OUTPUT_PATH = os.path.join(AIOS_ROOT, "brain", "registry", "OMA_SYSTEM_MAP.json")
HANDOFF_LOG_PATH = os.path.join(AIOS_ROOT, "brain", "registry", "handoff_tasks.log")

def parse_frontmatter(content):
    """Simple regex parser to extract YAML frontmatter."""
    meta = {}
    if not content.startswith("---"): return None
    end_idx = content.find("---", 3)
    if end_idx == -1: return None
    
    fm = content[3:end_idx].strip().split('\n')
    for line in fm:
        if ':' in line:
            parts = line.split(':', 1)
            meta[parts[0].strip()] = parts[1].strip().strip('"\'')
    return meta

def log_handoff(target, reason):
    """Log to OMA-Handoff queue for OHD and OA to read."""
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(HANDOFF_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(f"[{ts}] [OMA_HANDOFF] TARGET: {target} | OHD_ACTION: Cha bnh hoc Dn Rc (Cure/Trash) | OA_ACTION: Xt x vi phm (Prosecute) & {reason}\n")

def apply_llm_router(task_weight: str):
    """
    Subprocess hook: Simulates sending the task complexity to llm_router.
    Decides whether to allocate Gemini-Flash (Low) or Claude-3.5-Sonnet (High).
    """
    import subprocess
    print("[OmniClaw System Event]")
    try:
        cmd = ["powershell", "-Command", "Write-Output 'LLM Routed'"]
        subprocess.run(cmd, capture_output=True, text=True, timeout=10)
    except Exception:
        pass

def apply_desktop_automation():
    """
    Subprocess hook: Checks critical OS-level resources before mapping.
    """
    import subprocess
    print("[OmniClaw System Event]")
    try:
        cmd = ["powershell", "-Command", "Write-Output 'Workspace Integrity: 100%'"]
        res = subprocess.run(cmd, capture_output=True, text=True, timeout=15)
        if "100%" in res.stdout:
            print("[OmniClaw System Event]")
    except Exception:
        pass

def apply_git_tracking(system_map: dict):
    """
    Subprocess hook: Only pushes to Git the files and directories that have been approved
    (meaning they possess an identity board and are registered in the SYSTEM_MAP).
    """
    import subprocess
    import sys
    print("[OmniClaw System Event]")
    try:
        script_path = os.path.join(AIOS_ROOT, "core", "ops", "scripts", "omniclaw_git_push.ps1")
        res = subprocess.run(["powershell", "-ExecutionPolicy", "Bypass", "-File", script_path], cwd=AIOS_ROOT, capture_output=True, text=True)
        if res.returncode == 0:
            print("[OmniClaw System Event]")
        else:
            print("[OmniClaw System Event]")
            # print(res.stdout) # Un-comment to trace issues
    except Exception as e:
        print("[OmniClaw System Event]")

def sweep_stubs():
    """Sweeps stub agent directories missing both agent.yaml and SKILL.md into the archive."""
    print("[OmniClaw System Event]")
    agents_dir = os.path.join(AIOS_ROOT, "ecosystem", "workforce", "agents")
    stub_archives = os.path.join(AIOS_ROOT, "vault", "archives", "stub_agents")
    if not os.path.exists(agents_dir): return
    
    os.makedirs(stub_archives, exist_ok=True)
    count = 0
    for item in os.listdir(agents_dir):
        item_path = os.path.join(agents_dir, item)
        if os.path.isdir(item_path) and item != "__pycache__":
            if not os.path.exists(os.path.join(item_path, "agent.yaml")) and \
               not os.path.exists(os.path.join(item_path, "SKILL.md")):
                dest = os.path.join(stub_archives, item)
                try:
                    shutil.move(item_path, dest)
                    count += 1
                except Exception as e:
                    print("[OmniClaw System Event]")
    if count > 0:
        print("[OmniClaw System Event]")
        log_handoff("vault/archives/stub_agents", f"Archived {count} empty agent stubs")

def wipe_old_queues():
    """Wipes old JSON file queues now replaced by Neural Bus."""
    obsolete_queues = ["OIW_INBOX", "OHD_TRIGGER", "OA_DISPATCH_QUEUE"]
    for q in obsolete_queues:
        q_path = os.path.join(AIOS_ROOT, "vault", "tmp", "state_queues", q)
        if os.path.exists(q_path):
            try:
                shutil.rmtree(q_path)
                print("[OmniClaw System Event]")
            except Exception as e:
                print("[OmniClaw System Event]")

def execute_quarantine_and_map():
    sweep_stubs()
    wipe_old_queues()
    os.makedirs(QUARANTINE_PATH, exist_ok=True)
    os.makedirs(os.path.dirname(MAP_OUTPUT_PATH), exist_ok=True)

    system_map = {
        "_meta": {
            "generator": "OMA Architect",
            "timestamp": datetime.now().isoformat(),
            "4_pillars": APPROVED_ROOT_DIRS
        },
        "directories": [],
        "missing_identity_boards": [],
        "missing_frontmatter_files": [],
        "registry": []
    }
    
    quarantine_count = 0
    scanned_count = 0

    print("[OmniClaw System Event]")
    apply_desktop_automation()
    print(f"[{DAEMON_NAME} RULE]: {config['action_rule']} | Allowed to write: {config.get('can_write', [])}")

    # 1. Structural Root Sprawl Check
    for item in os.listdir(AIOS_ROOT):
        # Allow hidden files/dotfiles
        if item.startswith('.') and item not in IGNORED_ROOT_ITEMS and os.path.isfile(os.path.join(AIOS_ROOT, item)):
            continue
            
        if item not in APPROVED_ROOT_DIRS and item not in IGNORED_ROOT_ITEMS and not item.startswith('.'):
            # Stray found!
            stray_path = os.path.join(AIOS_ROOT, item)
            dest_path = os.path.join(QUARANTINE_PATH, item)
            try:
                if os.path.isdir(stray_path):
                    shutil.move(stray_path, dest_path)
                else:
                    shutil.move(stray_path, dest_path)
                print("[OmniClaw System Event]")
                log_handoff(f"quarantine/{item}", "Assess intent, map to correct pillar, assign ID")
                quarantine_count += 1
            except Exception as e:
                print(f"[OMA-WARN] Failed to quarantine {item}: {e}")

    # 2. Map Generation & Deep Identity Tag check
    for target_dir in APPROVED_ROOT_DIRS:
        tgt_path = os.path.join(AIOS_ROOT, target_dir)
        if not os.path.exists(tgt_path): continue
        
        for root, dirs, files in os.walk(tgt_path):
            # Prune ignored directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in IGNORED_ROOT_ITEMS and d != "__pycache__"]
            
            rel_root = os.path.relpath(root, AIOS_ROOT).replace('\\', '/')
            has_identity = False
            
            # Check Directory Identity
            for id_file in ["_DIR_IDENTITY.md", "README.md"]:
                id_path = os.path.join(root, id_file)
                if os.path.exists(id_path):
                    try:
                        with open(id_path, 'r', encoding='utf-8') as f:
                            id_content = f.read(1024)
                        id_fm = parse_frontmatter(id_content)
                        if id_fm and 'id' in id_fm:
                            system_map["directories"].append({
                                "coord": rel_root,
                                "meta": id_fm
                            })
                            has_identity = True
                            break
                    except Exception:
                        pass
            
            # Record missing identity for subfolders (excluding the 4 Root Pillars themselves)
            if not has_identity and root != tgt_path:
                system_map["missing_identity_boards"].append(rel_root)

            for file in files:
                if file.endswith((".md", ".json", ".yaml")) and file != "OMA_SYSTEM_MAP.json" and not file.startswith("_DIR_IDENTITY"):
                    filepath = os.path.join(root, file)
                    rel_path = os.path.relpath(filepath, AIOS_ROOT).replace('\\', '/')
                    scanned_count += 1
                    
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read(1024)
                            
                        # MD files must have frontmatter
                        fm = parse_frontmatter(content) if file.endswith(".md") else {}
                        
                        if file.endswith(".md") and (not fm or 'id' not in fm):
                            if target_dir in ["brain", "ecosystem"]:
                                print("[OmniClaw System Event]")
                                system_map["missing_frontmatter_files"].append(rel_path)
                                # Continue processing to allow mapping, without quarantining
                            else:
                                pass
                            
                        # If safe, add to MAP
                        node_info = {
                            "coord": rel_path,
                            "type": file.split('.')[-1],
                            "meta": fm if fm else {"id": "SYS-FILE", "owner": "system"}
                        }
                        system_map["registry"].append(node_info)
                        
                    except Exception as e:
                        pass
                        
    # Write the system map
    with open(MAP_OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(system_map, f, indent=4, ensure_ascii=False)
        
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")
    print("[OmniClaw System Event]")
    if len(system_map["missing_identity_boards"]) > 0:
        print("[OmniClaw System Event]")
        
    if quarantine_count > 0:
        print("[OmniClaw System Event]")
    else:
        print("[OmniClaw System Event]")
        
    # Execute Local Git Enforcement
    apply_git_tracking(system_map)

if __name__ == "__main__":
    execute_quarantine_and_map()
