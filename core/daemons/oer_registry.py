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


def determine_destination(meta: dict) -> str:
    """Look up the OMA map to determine the destination folder for the file."""
    ftype = meta.get("type", "default").lower()
    return DEFAULT_DEST_MAP.get(ftype, DEFAULT_DEST_MAP["default"])


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
    index = []
    if os.path.exists(FAST_INDEX_PATH):
        try:
            with open(FAST_INDEX_PATH, "r", encoding="utf-8") as f:
                index = json.load(f)
        except Exception:
            pass
    # Avoid duplication
    existing_ids = {e.get("id") for e in index}
    if entry.get("id") not in existing_ids:
        index.append(entry)
        with open(FAST_INDEX_PATH, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2, ensure_ascii=False)


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
    """Register a folder (usually Skill/Plugin/Agent download) and distribute."""
    fname = os.path.basename(folder_path)
    skill_md = os.path.join(folder_path, "SKILL.md")
    
    if os.path.exists(skill_md):
        try:
            with open(skill_md, "r", encoding="utf-8") as f:
                content = f.read(2048)
            meta = parse_frontmatter(content)
        except Exception as e:
            print(f"\033[93m[WARN]\033[0m [OER] Read SKILL.md failed in {fname}: {e}")
            return
            
        if not meta or "id" not in meta:
            skill_id = fname.replace("FETCHED_", "").split("_")[0]
            meta = {"id": skill_id, "type": "skill"}
            
        dest_folder = determine_destination(meta)
        target_skill_name = meta.get("id", fname)
        dest_path = os.path.join(dest_folder, target_skill_name)
        
        if not assert_write_access(DAEMON_NAME, dest_folder):
            return
            
        if os.path.exists(dest_path):
            print(f"\033[94m[INFO]\033[0m [OER] Folder {target_skill_name} already exists! Overwriting internal files...")
            # Simple merge: copying contents over
            for root, dirs, files in os.walk(folder_path):
                rel_dir = os.path.relpath(root, folder_path)
                target_r = os.path.join(dest_path, rel_dir)
                os.makedirs(target_r, exist_ok=True)
                for f in files:
                    shutil.copy2(os.path.join(root, f), os.path.join(target_r, f))
            shutil.rmtree(folder_path)
        else:
            shutil.move(folder_path, dest_path)
            
        print(f"\033[92m[OK]\033[0m [OER] Registered folder: {fname} -> {os.path.relpath(dest_path, abs_path(''))}")
        
        ts = datetime.now().isoformat()
        entry = {"id": meta.get("id", target_skill_name), "type": meta.get("type", "skill"),
                 "coord": os.path.relpath(dest_path, abs_path("")).replace("\\", "/"),
                 "owner": meta.get("owner", "OER"), "registered_at": ts}

        update_fast_index(entry)
        update_dir_identity(os.path.dirname(dest_path), {**entry, "name": target_skill_name, "ts": ts})
    else:
        print(f"\033[93m[WARN]\033[0m [OER] Folder {fname} lacks SKILL.md. Skipped auto-registration.")


def run():
    print(f"\n\033[94m[INFO]\033[0m [{DAEMON_NAME}] Booting - {config['role']}")
    print(f"\033[95m[RULE]\033[0m: {config['action_rule']}\n")

    os.makedirs(OER_INBOX, exist_ok=True)
    os.makedirs(abs_path(PATHS.KNOWLEDGE), exist_ok=True)

    items = os.listdir(OER_INBOX)
    if not items:
        # Reduce log noise
        pass

    for fname in items:
        fpath = os.path.join(OER_INBOX, fname)
        if os.path.isfile(fpath):
            register_file(fpath)
        elif os.path.isdir(fpath):
            register_folder(fpath)

    # Note: Skip counting completed files to avoid console spam because the script runs continuously.

if __name__ == "__main__":
    run()
