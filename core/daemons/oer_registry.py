#!/usr/bin/env python3
"""
[OER] OmniClaw Ecosystem Registrar
======================================================
Mission:
  1. Get clean file from OER_INBOX (from OHD or OA)
  2. Registration: assign/confirm ID, tag, type in Frontmatter
  3. Look up OMA_SYSTEM_MAP  determine the correct destination folder
  4. Distribute files to brain/knowledge or ecosystem/skills/plugins/...
  5. Update _DIR_IDENTITY.md in the destination folder (add new files to the list)
  6. Update FAST_INDEX.json
  7. Proactively check updates  notify OIW via OIW_INBOX if necessary

Rule: DO NOT create content. Only registration, classification, distribution.
      DO NOT go to core/.
"""
import os
import json
import shutil
import re
from datetime import datetime
from daemon_trust import authenticate_daemon, assert_write_access, abs_path, PATHS

DAEMON_NAME = "OER"
config = authenticate_daemon(DAEMON_NAME)

OER_INBOX       = abs_path(PATHS.OER_INBOX)
OIW_INBOX       = abs_path(PATHS.OIW_INBOX)
OA_DISPATCH     = abs_path(PATHS.OA_DISPATCH)
SYSTEM_MAP_PATH = abs_path(PATHS.SYSTEM_MAP)
FAST_INDEX_PATH = abs_path(PATHS.FAST_INDEX)
HANDOFF_LOG     = abs_path(PATHS.HANDOFF_LOG)

# [System log: Legacy non-English comment removed]
DEFAULT_DEST_MAP = {
    "rules":        abs_path(PATHS.RULES),
    "skill":        abs_path(PATHS.SKILLS),
    "plugin":       abs_path(PATHS.PLUGINS),
    "workflow":     abs_path(PATHS.WORKFLOWS),
    "agent":        abs_path(PATHS.WORKFORCE),
    "knowledge":    abs_path(PATHS.KNOWLEDGE),
    "report":       abs_path(PATHS.KNOWLEDGE, "architecture"),
    "api":          abs_path(PATHS.KNOWLEDGE, "api"),
    "default":      abs_path(PATHS.KNOWLEDGE, "general"),
}


def parse_frontmatter(content: str) -> dict:
    """Read YAML frontmatter from Markdown file content."""
    meta = {}
    if not content.startswith("---"):
        return meta
    end = content.find("---", 3)
    if end == -1:
        return meta
    for line in content[3:end].strip().split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("\"'")
    return meta


def normalize_id(name: str) -> str:
    """Normalize a repository name to a standard ID format to prevent duplication."""
    if not name: return ""
    n = str(name).lower()
    for suffix in [".git", "-main", "-master", ".main", ".master"]:
        if n.endswith(suffix):
            n = n[:-len(suffix)]
    n = n.replace("-", "_").replace(".", "_")
    return n


def determine_destination(meta: dict) -> str:
    """Look up the OMA map to determine the destination folder for the file."""
    ftype = meta.get("type", "default").lower()
    return DEFAULT_DEST_MAP.get(ftype, DEFAULT_DEST_MAP["default"])


def is_ghost_repo(folder_path: str) -> bool:
    """Check if the downloaded folder lacks actual source files, making it a ghost/phantom repo."""
    valid_extensions = (".py", ".js", ".ts", ".go", ".rs", ".java", ".c", ".cpp", ".cs", ".php", ".html", ".css", ".md", ".json")
    code_size = 0
    file_count = 0
    has_manifest_or_identity = False

    for root, _, files in os.walk(folder_path):
        for file in files:
            file_count += 1
            if file in ("manifest.json", "_DIR_IDENTITY.md", "SKILL.md", "PLUGIN.md", "DEEP_KNOWLEDGE.md", "KNOWLEDGE_TUNNEL.aaak"):
                has_manifest_or_identity = True
            
            # Exclude structural/identity/knowledge files from the "source code" weight
            if file.endswith(valid_extensions) and file not in ("manifest.json", "_DIR_IDENTITY.md", "SKILL.md", "PLUGIN.md", "README.md", "DEEP_KNOWLEDGE.md", "KNOWLEDGE_TUNNEL.aaak"):
                code_size += os.path.getsize(os.path.join(root, file))
    
    # If it has DEEP_KNOWLEDGE.md, it is an OA decapitated knowledge crystal, NEVER a ghost repo.
    if os.path.exists(os.path.join(folder_path, "DEEP_KNOWLEDGE.md")):
        return False

    # STRICT RULE: Only sweep if it has a tracker (manifest/identity) AND has virtually zero code.
    # This prevents sweeping the user's deliberately created structural Wait-Rooms.
    if has_manifest_or_identity and code_size < 1024 and file_count <= 5:
        return True
    return False


def update_dir_identity(folder: str, file_entry: dict):
    """Update _DIR_IDENTITY.md in the destination folder to record the new file."""
    identity_path = os.path.join(folder, "_DIR_IDENTITY.md")
    if not os.path.exists(identity_path):
        return
    try:
        with open(identity_path, "r", encoding="utf-8") as f:
            content = f.read()
        entry_line = f"\n- `{file_entry['name']}`  id: `{file_entry.get('id','?')}` | type: `{file_entry.get('type','?')}` | registered: {file_entry['ts']}"
        if entry_line not in content:
            with open(identity_path, "a", encoding="utf-8") as f:
                f.write(entry_line)
        print(f"\033[92m[OK]\033[0m [OER] Updated _DIR_IDENTITY.md: {os.path.basename(folder)}")
    except Exception as e:
        print(f"\033[93m[WARN]\033[0m [OER] Cannot update _DIR_IDENTITY: {e}")


def update_fast_index(entry: dict):
    """Write additional information to FAST_INDEX.json."""
    if os.path.exists(FAST_INDEX_PATH):
        try:
            with open(FAST_INDEX_PATH, "r", encoding="utf-8") as f:
                index = json.load(f)
                # If FAST_INDEX is the new dict structure from rebuild scripts, skip manual append
                if isinstance(index, dict):
                    return
        except Exception:
            index = []
    else:
        index = []

    # Avoid duplication
    if isinstance(index, list):
            if entry.get("id") not in existing_ids:
                index.append(entry)
                try:
                    with open(FAST_INDEX_PATH, "w", encoding="utf-8") as f:
                        json.dump(index, f, indent=2, ensure_ascii=False)
                except Exception: pass

def update_skill_registry(meta: dict, dest_path: str):
    """
    [PHASE 5: REGISTER]
    OER is the exclusive owner of SKILL_REGISTRY.json.
    Assign a strict ID if missing and log it mathematically.
    """
    registry_path = abs_path(os.path.join(PATHS.REGISTRY, "SKILL_REGISTRY.json"))
    reg_data = {}
    if os.path.exists(registry_path):
        try:
            with open(registry_path, "r", encoding="utf-8") as f:
                reg_data = json.load(f)
        except: pass
        
    asset_type = meta.get("type", "knowledge").lower()
    
    # Generate ID if missing or generic
    asset_id = meta.get("id")
    if not asset_id or asset_id.startswith("repo-"):
        ts_id = datetime.now().strftime('%M%S')
        if asset_type == "skill": asset_id = f"SKILL-{ts_id}"
        elif asset_type == "plugin": asset_id = f"PLG-{ts_id}"
        elif asset_type == "agent": asset_id = f"AGT-{ts_id}"
        elif asset_type == "workflow": asset_id = f"WRK-{ts_id}"
        else: asset_id = f"KNO-{ts_id}"
        meta["id"] = asset_id
        
    if asset_id not in reg_data:
        reg_data[asset_id] = {
            "type": asset_type,
            "path": dest_path,
            "registered_at": datetime.now().isoformat(),
            "status": "active"
        }
        try:
            os.makedirs(os.path.dirname(registry_path), exist_ok=True)
            with open(registry_path, "w", encoding="utf-8") as f:
                json.dump(reg_data, f, indent=4)
            print(f"\033[96m[OER-REGISTRY]\033[0m Official ID Issued: {asset_id} -> SKILL_REGISTRY.json")
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [OER] Cannot update SKILL_REGISTRY: {e}")
    return asset_id

def apply_smart_memory(entry_path: str):
    """
    Subprocess hook: Simulates sending fully validated structure to VectorDB (LightRAG) via smart_memory.
    """
    import subprocess
    print("[OmniClaw System Event]")
    try:
        cmd = ["powershell", "-Command", "Write-Output 'Vector DB Sync OK'"]
        subprocess.run(cmd, capture_output=True, text=True, timeout=5)
    except Exception:
        pass

def register_file(filepath: str):
    """Register a file and distribute it to the correct location."""
    fname = os.path.basename(filepath)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read(2048)
    except Exception as e:
        print(f"\033[93m[WARN]\033[0m [OER] Read file failed: {fname} - {e}")
        return

    meta = parse_frontmatter(content)
    if not meta or "id" not in meta:
        print(f"\033[93m[WARN]\033[0m [OER] File missing ID, registration aborted: {fname}. Sent to OHD...")
        # [System log: Legacy non-English comment removed]
        return

    dest_folder = determine_destination(meta)
    os.makedirs(dest_folder, exist_ok=True)

    if not assert_write_access(DAEMON_NAME, dest_folder):
        return

    dest_path = os.path.join(dest_folder, fname)
    if os.path.exists(dest_path):
        dest_path = dest_path.replace(".md", f"_{datetime.now().strftime('%H%M%S')}.md")

    shutil.move(filepath, dest_path)
    print(f"\033[92m[OK]\033[0m [OER] Registered and distributed: {fname} -> {os.path.relpath(dest_folder, abs_path(''))}")

    ts = datetime.now().isoformat()
    entry = {"id": meta.get("id"), "type": meta.get("type", "?"),
             "coord": os.path.relpath(dest_path, abs_path("")).replace("\\", "/"),
             "owner": meta.get("owner", "OER"), "registered_at": ts}

    update_fast_index(entry)
    update_dir_identity(dest_folder, {**entry, "name": fname, "ts": ts})
    apply_smart_memory(dest_path)


def register_folder(folder_path: str):
    """Register a folder (usually Skill/Plugin/Agent download or Assimilated Repo) and distribute."""
    fname = os.path.basename(folder_path)
    
    # Phase 0: Validate against Ghost/Phantom Repositories (Placeholders from failed downloads)
    if is_ghost_repo(folder_path):
        print(f"\033[93m[WARN]\033[0m [OER] Rejected {fname}: Ghost Repo detected (No valid source code found). Moved to Quarantine.")
        quarantine_dir = os.path.join(abs_path(PATHS.QUARANTINE), fname)
        try:
            shutil.rmtree(quarantine_dir, ignore_errors=True)
            shutil.move(folder_path, quarantine_dir)
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [OER] Failed to move ghost repo to Quarantine: {e}")
        return

    # Phase 1: Hunt for Identity Documents
    skill_md = os.path.join(folder_path, "SKILL.md")
    agent_md = os.path.join(folder_path, "AGENT.md")
    plugin_md = os.path.join(folder_path, "PLUGIN.md")
    dir_identity = os.path.join(folder_path, "_DIR_IDENTITY.md")
    
    target_md = None
    inferred_type = "skill"
    if os.path.exists(dir_identity):
        target_md = dir_identity
    elif os.path.exists(agent_md):
        target_md = agent_md
        inferred_type = "agent"
    elif os.path.exists(plugin_md):
        target_md = plugin_md
        inferred_type = "plugin"
    elif os.path.exists(skill_md):
        target_md = skill_md
        inferred_type = "skill"
        
    import stat
    def remove_readonly(func, path, _):
        try:
            os.chmod(path, stat.S_IWRITE)
            func(path)
        except Exception: pass

    if target_md:
        try:
            with open(target_md, "r", encoding="utf-8") as f:
                content = f.read(2048)
            meta = parse_frontmatter(content)
        except Exception as e:
            print(f"\033[93m[WARN]\033[0m [OER] Read {os.path.basename(target_md)} failed in {fname}: {e}")
            return
            
        if not meta or "id" not in meta:
            parsed_id = fname.replace("CIV_FETCHED_", "").replace("FETCHED_", "").split("_")[0]
            meta = {"id": normalize_id(parsed_id), "type": meta.get("type", inferred_type)}
            
        if "type" not in meta:
            meta["type"] = inferred_type
            
        target_skill_name = normalize_id(meta.get("id", fname))
        meta["id"] = target_skill_name  # Update meta to ensure consistency downstream
        
        dest_folder = determine_destination(meta)
        dest_path = os.path.join(dest_folder, target_skill_name)
        
        if not assert_write_access(DAEMON_NAME, dest_folder):
            return
            
        if os.path.exists(dest_path):
            print(f"\033[94m[INFO]\033[0m [OER] Folder {target_skill_name} already exists! Engaging Smart Additive Merge...")
            # Smart merge: comparing timestamps and sizes to preserve existing integrity
            for root, dirs, files in os.walk(folder_path):
                rel_dir = os.path.relpath(root, folder_path)
                target_r = os.path.join(dest_path, rel_dir)
                try:
                    os.makedirs(target_r, exist_ok=True)
                except Exception as e:
                    print(f"\033[93m[WARN]\033[0m [OER] Merge collision! directory creation failed at {target_r}: {e}. Attempting safe skip/rename...")
                    target_r = target_r + "_dir"
                    try: os.makedirs(target_r, exist_ok=True)
                    except: pass
                for f in files:
                    src_file = os.path.join(root, f)
                    dst_file = os.path.join(target_r, f)
                    try:
                        should_overwrite = True
                        if os.path.exists(dst_file):
                            src_stat = os.stat(src_file)
                            dst_stat = os.stat(dst_file)
                            # Do not overwrite if the destination file is newer and at least as large
                            if dst_stat.st_mtime >= src_stat.st_mtime and dst_stat.st_size >= src_stat.st_size:
                                should_overwrite = False
                                
                        if should_overwrite:
                            try:
                                shutil.copy2(src_file, dst_file)
                            except FileExistsError: pass # Ignore if we copied over something that became a dir
                    except Exception: pass
            shutil.rmtree(folder_path, ignore_errors=True)
        else:
            try:
                shutil.move(folder_path, dest_path)
            except Exception as e:
                # Fallback to copy and ignore errors on rmtree
                try:
                    shutil.copytree(folder_path, dest_path, dirs_exist_ok=True)
                    shutil.rmtree(folder_path, ignore_errors=True)
                except Exception as ex:
                    print(f"\033[91m[ERR]\033[0m [OER] Move & Copy both failed for {fname}: {ex}")
            
        print(f"\033[92m[OK]\033[0m [OER] Registered folder: {fname} -> {os.path.relpath(dest_path, abs_path(''))}")
        
        ts = datetime.now().isoformat()
        entry = {"id": meta.get("id", target_skill_name), "type": meta.get("type", "skill"),
                 "coord": os.path.relpath(dest_path, abs_path("")).replace("\\", "/"),
                 "owner": meta.get("owner", "OER"), "registered_at": ts}

        update_fast_index(entry)
        update_dir_identity(os.path.dirname(dest_path), {**entry, "name": target_skill_name, "ts": ts})
        
        # [PHASE 5: REGISTRY ID ISSUANCE]
        update_skill_registry(meta, dest_path)
    else:
        print(f"\033[93m[WARN]\033[0m [OER] Folder {fname} lacks identity definition. Skipped auto-registration.")


def ecosystem_sweep_ghosts():
    """Proactively scan the ecosystem destinations and purge ghost repositories."""
    print(f"\n\033[93m[WARN]\033[0m [OER] Initiating Ecosystem-wide Ghost Sweep...")
    destinations = set(DEFAULT_DEST_MAP.values())
    purged = 0
    quarantine_base = abs_path(PATHS.QUARANTINE)
    
    for dest in destinations:
        if not os.path.exists(dest):
            continue
        for dirname in os.listdir(dest):
            folder_path = os.path.join(dest, dirname)
            if os.path.isdir(folder_path) and is_ghost_repo(folder_path):
                # Move to QUARANTINE
                quarantine_dir = os.path.join(quarantine_base, f"GHOST_SWEEP_{dirname}")
                try:
                    shutil.move(folder_path, quarantine_dir)
                    purged += 1
                    print(f"  -> Purged existing Ghost from ecosystem: {dirname}")
                except Exception:
                    try:
                        shutil.rmtree(folder_path, ignore_errors=True)
                        purged += 1
                    except Exception: pass
                    
    if purged > 0:
        print(f"\033[92m[OK]\033[0m [OER] Sweep complete. Purged {purged} ghost repos from the ecosystem.")
    else:
        print(f"\033[92m[OK]\033[0m [OER] Sweep complete. Ecosystem is clean.")

def ecosystem_sweep_duplicates():
    """Retroactive deduplication: Keeps the largest/newest version of duplicated files/folders and trashes the rest."""
    import re
    print(f"\033[96m[STAT]\033[0m [OER] Executing Boot-Time Retroactive Deduplication...")
    
    knowledge_dir = abs_path(PATHS.KNOWLEDGE)
    if not os.path.exists(knowledge_dir):
        return
        
    items = os.listdir(knowledge_dir)
    file_groups = {}
    folder_groups = {}
    
    for item in items:
        path = os.path.join(knowledge_dir, item)
        if os.path.isfile(path):
            # Example: KI_AutoGPT_knowledge_20260404_014610.md
            # Or ki_github...20260402_221918.md
            m = re.match(r"^([Kk][Ii]_.+?)_\d{8}_\d{6}\.md$", item)
            if m:
                base = m.group(1).lower()
                if base not in file_groups:
                    file_groups[base] = []
                file_groups[base].append((path, os.path.getsize(path), os.path.getmtime(path), item))
        elif os.path.isdir(path):
            # Example: repo-fetched-phoenix-034618
            # Or repo-fetched-phoenix-034618-034711
            m = re.match(r"^(repo-fetched-.+?)(?:-\d{6})+$", item)
            if m:
                base = m.group(1).lower()
                if base not in folder_groups:
                    folder_groups[base] = []
                # Count files inside to determine the "largest"
                file_count = sum(len(files) for r, d, files in os.walk(path))
                folder_groups[base].append((path, file_count, os.path.getmtime(path), item))
    
    purged = 0
    quarantine_base = os.path.join(abs_path(PATHS.QUARANTINE), "DUPLICATES")
    os.makedirs(quarantine_base, exist_ok=True)
    
    # Process Files - keep largest/newest
    for base, entries in file_groups.items():
        if len(entries) > 1:
            # Sort by size (desc), then mtime (desc)
            entries.sort(key=lambda x: (x[1], x[2]), reverse=True)
            keeper = entries[0]
            duplicates = entries[1:]
            for dup in duplicates:
                try:
                    shutil.move(dup[0], os.path.join(quarantine_base, dup[3]))
                    purged += 1
                except: pass
            print(f"  -> Merged {len(duplicates)} duplicate files for {base}. Kept {keeper[3]}.")
            
    # Process Folders - keep largest
    for base, entries in folder_groups.items():
        if len(entries) > 1:
            # Sort by file count (desc), then mtime (desc)
            entries.sort(key=lambda x: (x[1], x[2]), reverse=True)
            keeper = entries[0]
            duplicates = entries[1:]
            for dup in duplicates:
                try:
                    shutil.move(dup[0], os.path.join(quarantine_base, dup[3]))
                    purged += 1
                except: pass
            print(f"  -> Merged {len(duplicates)} duplicate folders for {base}. Kept {keeper[3]} ({keeper[1]} files).")
            
    if purged > 0:
        print(f"\033[92m[OK]\033[0m [OER] Deduplication Purged {purged} duplicate items.")
    else:
        print(f"\033[92m[OK]\033[0m [OER] Ecosystem is duplicate-free.")


def run():
    import time
    print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting - {config['role']}")
    print(f"\033[95m[RULE]\033[0m: {config['action_rule']}\n")

    os.makedirs(OER_INBOX, exist_ok=True)
    os.makedirs(abs_path(PATHS.KNOWLEDGE), exist_ok=True)

    # Boot-time Ecosystem Scrub
    ecosystem_sweep_ghosts()
    ecosystem_sweep_duplicates()

    print(f"\033[92m[STAT]\033[0m [{DAEMON_NAME}] Ecosystem Registrar entering Perpetual Loop...")
    while True:
        try:
            items = os.listdir(OER_INBOX)
            if not items:
                pass
            else:
                for fname in items:
                    fpath = os.path.join(OER_INBOX, fname)
                    if os.path.isfile(fpath):
                        register_file(fpath)
                    elif os.path.isdir(fpath):
                        register_folder(fpath)

            time.sleep(30)
            
        except KeyboardInterrupt:
            print(f"\033[93m[WARN]\033[0m [{DAEMON_NAME}] Keyboard Interrupt received. Exiting loop.")
            break
        except Exception as e:
            print(f"\033[91m[ERR]\033[0m [{DAEMON_NAME}] Critical Error in Daemon Loop: {e}. Sleeping before retry.")
            time.sleep(30)

if __name__ == "__main__":
    import sys
    if "--single-pass" in sys.argv:
        print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting in SINGLE-PASS mode...")
        ecosystem_sweep_ghosts()
        ecosystem_sweep_duplicates()
        process_inbox()
        print(f"\033[92m[OK]\033[0m [{DAEMON_NAME}] Single pass complete.")
    else:
        run()
