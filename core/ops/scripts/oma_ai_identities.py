#!/usr/bin/env python3
"""
[OMA FORGER] AI Identity Forger Pipeline
Role: Core Automation Script for AI identity enrichment.
Function: Injects LLM cognitive logic to forge and enrich empty or auto-generated _DIR_IDENTITY.md files across the ecosystem.
"""
import os
import sys
import json
import traceback

OMNICLAW_ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# Add daemons path to import daemon_utils.call_omniclaw_model
DAEMONS_PATH = os.path.join(OMNICLAW_ROOT, "core", "daemons")
if DAEMONS_PATH not in sys.path:
    sys.path.append(DAEMONS_PATH)

try:
    from daemon_utils import call_omniclaw_model
except ImportError:
    print("[ERROR] Cannot import daemon_utils. Ensure omniclaw_model is installed.")
    sys.exit(1)

def get_context_for_directory(dir_path: str):
    """Gather spatial awareness of the directory to send to LLM."""
    folder_name = os.path.basename(dir_path)
    rel_path = os.path.relpath(dir_path, OMNICLAW_ROOT).replace("\\", "/")
    
    parent_dir = os.path.dirname(dir_path)
    parent_rel = os.path.relpath(parent_dir, OMNICLAW_ROOT).replace("\\", "/") if parent_dir != OMNICLAW_ROOT else "root"

    subdirs = []
    files = []
    
    for item in os.listdir(dir_path):
        if item.startswith('.') or item == "_DIR_IDENTITY.md":
            continue
        p = os.path.join(dir_path, item)
        if os.path.isdir(p):
            subdirs.append(item)
        elif os.path.isfile(p):
            files.append(item)
            
    return {
        "folder_name": folder_name,
        "path": rel_path,
        "parent_path": parent_rel,
        "subdirs_found": subdirs,
        "files_found": files[:10]
    }

def build_llm_prompt(context_dict: dict) -> str:
    ctx = json.dumps(context_dict, indent=2)
    return f"""You are the OMA Chief Architect of OmniClaw (v5.0).
Enrich this taxonomy node with a deep description and a TOPOLOGICAL graph.

DIRECTORY CONTEXT:
{ctx}

MANDATORY JSON SCHEMA:
{{
  "id": "unique_slug",
  "type": "directory_identity",
  "namespace": "brain.example.path",
  "description": "2-3 high-level impact sentences.",
  "tags": ["tag1", "tag2"],
  "mermaid_graph": "graph TD\\n  Parent(\\"parent_path\\") --> Node(\\"folder_name\\")\\n  Node --> Sub1(\\"subdir\\")..."
}}

CRITICAL MERMAID RULES:
1. USE ARROWS `-->` TO CONNECT THE PARENT TO THIS FOLDER, AND THIS FOLDER TO ITS SUBDIRS.
2. DISCONNECTED NODES ARE A SYSTEM FAILURE. Every node MUST have a connection.
3. Node names MUST be in DOUBLE QUOTES! Example: Root("core/ops") --> Scripts("scripts")
4. No backslashes in Mermaid labels. Use forward slashes.

Generate STRITCTLY VALID JSON.
"""

def process_batch(limit=None, force=False):
    print(f"=== OMA AI Forger: Commencing Scan (Force Overwrite: {force}) ===")
    
    targets_processed = 0
    search_root = os.path.join(OMNICLAW_ROOT, "brain")
    
    for root, dirs, files in os.walk(search_root):
        if limit and targets_processed >= limit:
            break
            
        if "_DIR_IDENTITY.md" in files:
            id_path = os.path.join(root, "_DIR_IDENTITY.md")
            try:
                with open(id_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
                
            is_hollow = "Auto-generated" in content or "No topology generated" in content or "graph TD\\n  " not in content.replace("graph TD\n", "graph TD\\n")
            # If the graph doesn't have connections (-->), it's considered poor quality
            is_disconnected = "-->" not in content and "graph" in content
            
            if force or is_hollow or is_disconnected:
                print(f"[OMA-FORGER] Targeting Node: {os.path.relpath(id_path, OMNICLAW_ROOT)}")
                
                ctx = get_context_for_directory(root)
                prompt = build_llm_prompt(ctx)
                
                try:
                    result_json_str = call_omniclaw_model(prompt, json_format=True, timeout=120)
                    if not result_json_str:
                        print("  -> [ERROR] Timeout/Empty response.")
                        continue
                        
                    data = json.loads(result_json_str)
                    
                    md_content = f"""---
id: {data.get('id', 'unknown_id')}
type: {data.get('type', 'directory_identity')}
namespace: {data.get('namespace', 'unknown.namespace')}
owner: OSF_Daemon
status: standard_v5
description: "{data.get('description', '')}"
registered_by: OMA_AI_FORGER
tags: {json.dumps(data.get('tags', []))}
---

# {ctx['folder_name'].replace('_', ' ').title()} Identity

{data.get('description', '')}

## Topological View

```mermaid
{data.get('mermaid_graph', 'graph TD\\n  NoGraph("No topology generated")')}
```

---
*OmniClaw V5.0 | Forged by AI Architect | Evaluated dynamically*
"""
                    with open(id_path, "w", encoding="utf-8") as f:
                        f.write(md_content)
                    print(f"  -> [SUCCESS] Deep Identity Forged with connections!")
                    targets_processed += 1

                except Exception as e:
                    print(f"  -> [CRASH] {e}")

    print(f"\n[OMA-FORGER] Scan complete. Processed {targets_processed} nodes.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=0, help="Max nodes to process (0 = all).")
    parser.add_argument("--force", action="store_true", help="Overwrite even if not detected as hollow.")
    args = parser.parse_args()
    
    process_batch(limit=args.batch if args.batch > 0 else None, force=args.force)

