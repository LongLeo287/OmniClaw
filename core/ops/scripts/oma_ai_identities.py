#!/usr/bin/env python3
"""
[OMA FORGER v2.0] AI Identity Forger Pipeline
Role: Core Automation Script for AI identity enrichment.
Function: Injects LLM cognitive logic to forge and enrich empty or
          auto-generated _DIR_IDENTITY.md files across the ecosystem.

Usage:
  python oma_ai_identities.py                    # Forge all hollow nodes in brain/
  python oma_ai_identities.py --batch 10         # Forge first 10 only
  python oma_ai_identities.py --scan-only        # Dry-run: list targets without writing
  python oma_ai_identities.py --target-dir brain/knowledge/corp  # Forge specific dir tree
  python oma_ai_identities.py --force            # Overwrite even good-quality files
"""
import os
import sys
import json
import re
import datetime
import traceback

OMNICLAW_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Add daemons path to import daemon_utils.call_omniclaw_model
DAEMONS_PATH = os.path.join(OMNICLAW_ROOT, "core", "daemons")
if DAEMONS_PATH not in sys.path:
    sys.path.append(DAEMONS_PATH)

try:
    from daemon_utils import call_omniclaw_model
except ImportError:
    print("[ERROR] Cannot import daemon_utils. Ensure daemons path is correct.")
    sys.exit(1)

# ── SKIP PATTERNS ────────────────────────────────────────────────────────────
# These subdirectory patterns are NOT OmniClaw infrastructure — skip them
SKIP_DIR_PATTERNS = [
    "__pycache__", ".git", ".github", "node_modules",
    "chroma_db/48aea028",   # HNSW segment — system managed
    "48aea028-e32b",         # HNSW UUID
    "legacy/",               # Legacy scripts archive
]

# Folders inside ingested knowledge repos — don't forge these
SKIP_KNOWLEDGE_SUBPATHS = [
    "brain/knowledge/repositories/",
    "brain/knowledge/repo_",
    "brain/knowledge/bmad_repo/",
    "brain/knowledge/claude_bp_repo/",
    "brain/knowledge/skills_standard_repo/",
    "brain/knowledge/orphan_sweep_web3/",
]


def should_skip(dir_path: str) -> bool:
    rel = os.path.relpath(dir_path, OMNICLAW_ROOT).replace("\\", "/")
    for pat in SKIP_DIR_PATTERNS:
        if pat in rel:
            return True
    for pat in SKIP_KNOWLEDGE_SUBPATHS:
        if rel.startswith(pat) and rel != pat.rstrip("/"):
            # Allow the top-level of each, skip deep subdirs inside
            depth_inside = rel[len(pat.rstrip("/"))+1:].count("/")
            if depth_inside > 0:
                return True
    return False


def is_hollow(id_path: str) -> bool:
    """Detect if _DIR_IDENTITY.md is a placeholder/hollow file."""
    try:
        with open(id_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    except Exception:
        return False

    size = os.path.getsize(id_path)

    return (
        "brain.example.path" in content or   # Default placeholder namespace
        "unique_slug" in content or            # LLM forgot to fill in ID
        "Auto-generated" in content or
        "No topology generated" in content or
        size < 400                              # Too short to be meaningful
    )


def make_namespace(dir_path: str) -> str:
    """Convert filesystem path to dot-notation namespace."""
    rel = os.path.relpath(dir_path, OMNICLAW_ROOT).replace("\\", "/")
    # Clean up: remove leading '.' or './', convert slashes to dots
    rel = rel.lstrip("./")
    namespace = rel.replace("/", ".").lower()
    # Sanitize: remove non-alphanumeric except dots and underscores
    namespace = re.sub(r"[^a-z0-9._]", "_", namespace)
    return namespace


def make_id(folder_name: str) -> str:
    """Create a clean slug ID from folder name."""
    slug = folder_name.lower()
    slug = re.sub(r"[^a-z0-9_]", "_", slug)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return slug


def get_context(dir_path: str) -> dict:
    """Gather spatial context of the directory for LLM."""
    folder_name = os.path.basename(dir_path)
    rel = os.path.relpath(dir_path, OMNICLAW_ROOT).replace("\\", "/")
    parent = os.path.dirname(dir_path)
    parent_name = os.path.basename(parent)

    subdirs, files = [], []
    try:
        for item in sorted(os.listdir(dir_path)):
            if item.startswith(".") or item in ("_DIR_IDENTITY.md", "_REGIONAL_MAP.md"):
                continue
            p = os.path.join(dir_path, item)
            if os.path.isdir(p):
                subdirs.append(item)
            elif os.path.isfile(p):
                files.append(item)
    except Exception:
        pass

    return {
        "folder_name": folder_name,
        "path": rel,
        "parent_name": parent_name,
        "namespace": make_namespace(dir_path),
        "id": make_id(folder_name),
        "subdirs": subdirs[:12],
        "files": files[:12],
        "total_subdirs": len(subdirs),
        "total_files": len(files),
    }


def build_prompt(ctx: dict) -> str:
    ctx_json = json.dumps(ctx, indent=2, ensure_ascii=False)
    return f"""You are the OMA Chief Architect of OmniClaw v5.0.
Write a production-quality _DIR_IDENTITY.md for this directory node.

DIRECTORY CONTEXT:
{ctx_json}

OUTPUT: Respond with STRICTLY VALID JSON, no markdown fences, no extra text.

JSON SCHEMA:
{{
  "description_en": "2-3 sentences. What is this directory's purpose and responsibility within OmniClaw?",
  "description_vn": "2-3 câu tiếng Việt. Mô tả chức năng và trách nhiệm của thư mục này trong OmniClaw.",
  "tags": ["tag1", "tag2", "tag3"],
  "mermaid_graph": "FULL mermaid graph string here"
}}

MERMAID RULES (CRITICAL — violation = system failure):
1. Use `graph TD` direction.
2. EVERY node MUST be connected with `-->` arrows. NO disconnected nodes.
3. Structure: Parent("{ctx['parent_name']}") --> Node("{ctx['folder_name']}") --> Sub("subdir") etc.
4. Wrap ALL labels in double quotes: Node("label")
5. Use <br/> for line breaks inside labels, NEVER backslash-n.
6. NO special chars in labels: no colons, no slashes inside quotes.
7. If no subdirs/files exist, still draw at minimum: Parent --> Node.

EXAMPLE mermaid_graph value (follow this exact format):
"graph TD\\n  Parent(\\"brain\\") --> Node(\\"knowledge\\")\\n  Node --> S1(\\"corp\\")\\n  Node --> S2(\\"general\\")"
"""


def forge_one(dir_path: str, scan_only: bool = False) -> bool:
    """Forge identity for a single directory. Returns True on success."""
    id_path = os.path.join(dir_path, "_DIR_IDENTITY.md")
    ctx = get_context(dir_path)
    rel = ctx["path"]

    if scan_only:
        print(f"  [WOULD FORGE] {rel}  ({ctx['total_subdirs']} dirs, {ctx['total_files']} files)")
        return True

    print(f"  [FORGING] {rel} ...", end="", flush=True)

    prompt = build_prompt(ctx)

    try:
        raw = call_omniclaw_model(prompt, json_format=True, timeout=90)
        if not raw or not raw.strip():
            print(" TIMEOUT/EMPTY")
            return False

        # Clean up: sometimes LLM wraps in ```json ... ```
        cleaned = raw.strip()
        if cleaned.startswith("```"):
            cleaned = re.sub(r"```[a-z]*\n?", "", cleaned).replace("```", "").strip()

        data = json.loads(cleaned)

    except json.JSONDecodeError as e:
        print(f" JSON_ERROR: {e}")
        return False
    except Exception as e:
        print(f" ERROR: {e}")
        return False

    desc_en = data.get("description_en", "")
    desc_vn = data.get("description_vn", "")
    tags    = data.get("tags", [])
    graph   = data.get("mermaid_graph", f'graph TD\n  Parent("{ctx["parent_name"]}") --> Node("{ctx["folder_name"]}")')

    # Validate graph has arrows
    if "-->" not in graph:
        graph = f'graph TD\n  Parent("{ctx["parent_name"]}") --> Node("{ctx["folder_name"]}")'

    # Build output markdown
    folder_title = ctx["folder_name"].replace("_", " ").title()
    tags_yaml = json.dumps(tags)
    now = datetime.datetime.now().strftime("%Y-%m-%d")

    md = f"""---
id: {ctx['id']}
type: directory_identity
namespace: {ctx['namespace']}
owner: OSF_Daemon
status: standard_v5
description: "{desc_en}"
registered_by: OMA_AI_FORGER
tags: {tags_yaml}
forged_at: {now}
---

# {folder_title} Identity

{desc_en}

---

## Chức Năng (Tiếng Việt)

{desc_vn}

## Topological View

```mermaid
{graph}
```

---
*OmniClaw V5.0 | Forged by OMA AI Architect | {ctx['namespace']} | {now}*
"""

    try:
        with open(id_path, "w", encoding="utf-8") as f:
            f.write(md)
        print(f" OK ({len(md)}B)")
        return True
    except Exception as e:
        print(f" WRITE_ERROR: {e}")
        return False


def scan_targets(search_root: str) -> list:
    """Find all hollow _DIR_IDENTITY.md targets."""
    targets = []
    for root, dirs, files in os.walk(search_root):
        # Prune dirs in-place to avoid descending into skip paths
        dirs[:] = [d for d in sorted(dirs) if not should_skip(os.path.join(root, d))]

        if should_skip(root):
            continue

        if "_DIR_IDENTITY.md" in files:
            id_path = os.path.join(root, "_DIR_IDENTITY.md")
            if is_hollow(id_path):
                targets.append(root)

    return targets


def process_batch(search_root: str, limit=None, force=False, scan_only=False, target_dir=None):
    if target_dir:
        actual_root = os.path.join(OMNICLAW_ROOT, target_dir.replace("/", os.sep))
        if not os.path.isdir(actual_root):
            print(f"[ERROR] --target-dir not found: {actual_root}")
            sys.exit(1)
        search_root = actual_root

    print(f"=== OMA AI Forger v2.0 ({'DRY-RUN' if scan_only else 'LIVE'}) ===")
    print(f"Search root: {os.path.relpath(search_root, OMNICLAW_ROOT)}")
    if limit:
        print(f"Limit: {limit} nodes")
    if force:
        print("Mode: FORCE (overwrite all)")
    print()

    if force and not scan_only:
        # Force mode: collect all dirs with _DIR_IDENTITY.md
        targets = []
        for root, dirs, files in os.walk(search_root):
            dirs[:] = [d for d in sorted(dirs) if not should_skip(os.path.join(root, d))]
            if should_skip(root):
                continue
            if "_DIR_IDENTITY.md" in files:
                targets.append(root)
    else:
        targets = scan_targets(search_root)

    if limit:
        targets = targets[:limit]

    print(f"Targets found: {len(targets)}")
    print()

    success, fail = 0, 0
    for t in targets:
        ok = forge_one(t, scan_only=scan_only)
        if not scan_only:
            if ok:
                success += 1
            else:
                fail += 1

    if not scan_only:
        print()
        print(f"=== Done: {success} SUCCESS | {fail} FAILED ===")
    else:
        print(f"\n=== Scan complete: {len(targets)} targets would be forged ===")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="OMA AI Identity Forger v2.0")
    parser.add_argument("--batch", type=int, default=0, help="Max nodes to process (0 = all)")
    parser.add_argument("--force", action="store_true", help="Overwrite even good-quality files")
    parser.add_argument("--scan-only", action="store_true", help="Dry-run: list targets without writing")
    parser.add_argument("--target-dir", type=str, default=None, help="Relative path to target subtree (e.g. brain/knowledge/corp)")
    args = parser.parse_args()

    search_root = os.path.join(OMNICLAW_ROOT, "brain")
    process_batch(
        search_root=search_root,
        limit=args.batch if args.batch > 0 else None,
        force=args.force,
        scan_only=args.scan_only,
        target_dir=args.target_dir,
    )
