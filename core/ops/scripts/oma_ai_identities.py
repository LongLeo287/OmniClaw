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
    
    subdirs = []
    files = []
    
    for item in os.listdir(dir_path):
        if item.startswith('.') or item == "_DIR_IDENTITY.md":
            continue
        p = os.path.join(dir_path, item)
        if os.path.isdir(p):
            subdirs.append(item + "/")
        elif os.path.isfile(p):
            files.append(item)
            
    return {
        "folder_name": folder_name,
        "path": rel_path,
        "subdirs_found": subdirs,
        "files_found": files[:15]  # Limit to 15 files to save tokens
    }

def build_llm_prompt(context_dict: dict) -> str:
    ctx = json.dumps(context_dict, indent=2)
    return f"""You are the OMA Chief Architect of a Multi-Agent AI OS named OmniClaw (v5.0).
Your task is to enrich an empty taxonomy node by writing a rich semantic description and routing map.

Here is the directory context you discovered:
{ctx}

Generate a JSON object with the following schema:
{{
  "id": "A unique slug, e.g. brain_rules_governance",
  "type": "directory_identity",
  "namespace": "the dot-separated namespace, e.g. brain.rules.governance",
  "description": "A 1-2 sentence profound, rich semantic description of what this directory manages.",
  "tags": ["tag1", "tag2", "tag3"],
  "mermaid_graph": "A valid GitHub Mermaid diagram showing how this node connects to its subdirectories or parent."
}}

CRITICAL MERMAID RULES TO PREVENT PARSE CRASHES:
1. ALWAYS start with lowercase `graph TD` or `graph LR`.
2. Identify all nodes in quotes! Do NOT put dots `.` or slashes `/` inside unquoted nodes! Example: `Root("brain/rules")`.
3. Never use `\\n` raw inside node labels! Use `<br/>` instead. Example: `NodeA("File Name<br/>Descr")`
4. DO NOT use the `:::` syntax for styling classes (like `:::directory`) unless you also Output the `classDef` at the bottom. To be safe, just don't use `:::` at all.

Generate ONLY the JSON object, formatted strictly as valid JSON.
"""

def process_batch(limit=3):
    print(f"=== OMA AI Forger: Commencing Batch Scan (Limit: {limit}) ===")
    
    targets_processed = 0
    search_root = os.path.join(OMNICLAW_ROOT, "brain") # We stick to brain/ for now prioritizing knowledge/rules
    
    for root, dirs, files in os.walk(search_root):
        if targets_processed >= limit:
            break
            
        if "_DIR_IDENTITY.md" in files:
            id_path = os.path.join(root, "_DIR_IDENTITY.md")
            try:
                with open(id_path, "r", encoding="utf-8") as f:
                    content = f.read()
            except Exception:
                continue
                
            # Detect Auto-generated stub
            if "Auto-generated identity for" in content or "Auto-generated identity tag by OMA" in content:
                print(f"[OMA-FORGER] Discovered Hollow Node: {os.path.relpath(id_path, OMNICLAW_ROOT)}")
                
                # Fetch Context
                ctx = get_context_for_directory(root)
                prompt = build_llm_prompt(ctx)
                
                print(f"  -> Consulting Central Oracle (LLM) for semantic enrichment...")
                
                try:
                    result_json_str = call_omniclaw_model(prompt, json_format=True, timeout=120)
                    if not result_json_str:
                        print("  -> [ERROR] Timeout or empty response from LLM.")
                        continue
                        
                    data = json.loads(result_json_str)
                    
                    # Convert dict to beautiful Markdown
                    md_content = f"""---
id: {data.get('id', 'unknown_id')}
type: {data.get('type', 'directory_identity')}
namespace: {data.get('namespace', 'unknown.namespace')}
owner: OMA_AI_FORGER
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
                    # Write back to file
                    with open(id_path, "w", encoding="utf-8") as f:
                        f.write(md_content)
                    print(f"  -> [SUCCESS] Deep Identity Forged and Injected!")
                    targets_processed += 1

                except Exception as e:
                    print(f"  -> [CRASH] Failed to forge. Data schema mismatch? Error: {e}")

    print(f"\n[OMA-FORGER] Scan cycle complete. Processed {targets_processed} nodes.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--batch", type=int, default=3, help="Max number of files to process per run.")
    args = parser.parse_args()
    
    process_batch(limit=args.batch)
