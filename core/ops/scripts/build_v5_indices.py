#!/usr/bin/env python3
"""
build_v5_indices.py — OmniClaw V5.0 Architecture Index Builder
Rebuilds the 6 Core FAST Indices based strictly on Namespace (physical paths)
to prevent legacy `type:` tags from leaking across architectural boundaries.
"""

import os
import re
import json
import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
INDICES_DIR = os.path.join(ROOT, "brain", "indices")

EXCLUDES = {
    ".git", ".github", "__pycache__", "node_modules", "dist", "build",
    ".venv", "venv", ".pixi", ".cargo", ".cache", "vault/tmp"
}

# Namespace map to physical topologies
BUCKETS = {
    "AGENT": [os.path.normpath("ecosystem/workforce/departments")],
    "SKILL": [os.path.normpath("ecosystem/skills"), os.path.normpath("ecosystem/tools"), os.path.normpath("ecosystem/ui_components")],
    "WORKFLOW": [os.path.normpath("ecosystem/workflows")],
    "PLUGIN": [os.path.normpath("ecosystem/plugins")],
    "KNOWLEDGE": [os.path.normpath("vault/knowledge"), os.path.normpath("brain/knowledge")],
    "DOCUMENT": [os.path.normpath("vault/docs"), os.path.normpath("core/docs")]
}

def parse_frontmatter(content: str) -> dict:
    m = re.match(r'^---\s*\n(.*?)\n---', content, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ':' in line:
            k, _, v = line.partition(':')
            fm[k.strip()] = v.strip().strip("'\"")
    return fm

def get_bucket(rel_path: str) -> str:
    norm_rel = os.path.normpath(rel_path)
    for bucket_name, prefixes in BUCKETS.items():
        for prefix in prefixes:
            if norm_rel.startswith(prefix):
                return bucket_name
    return "KNOWLEDGE"  # Default fallback if unknown

def main():
    os.makedirs(INDICES_DIR, exist_ok=True)
    registry_map = {k: [] for k in BUCKETS.keys()}
    registry_map["KNOWLEDGE"] = []

    count = 0
    logging.info("Initiating V5.0 OS Directory Scan for _DIR_IDENTITY.md...")

    # Only scan our architectural roots perfectly mapping to indices
    scan_roots = []
    for buckets in BUCKETS.values():
        for b in buckets:
            full_path = os.path.join(ROOT, b)
            if os.path.exists(full_path):
                scan_roots.append(full_path)
    
    for scan_root in scan_roots:
        scan_root_depth = scan_root.count(os.sep)
        for root, dirs, files in os.walk(scan_root):
            current_depth = root.count(os.sep)
            
            # Prune directories starting with dot or explicitly excluded
            dirs[:] = [d for d in dirs if d.lower() not in EXCLUDES and not d.startswith('.')]
            
            # Prevent scanning too deep (max 4 levels below scan_root)
            if current_depth - scan_root_depth > 4:
                dirs[:] = []
                continue
                
            if "_DIR_IDENTITY.md" in files:
                file_path = os.path.join(root, "_DIR_IDENTITY.md")
            rel_path = os.path.relpath(file_path, ROOT).replace("\\", "/")
            
            # Read identity
            try:
                with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()
            except Exception as e:
                logging.warning(f"Could not read {rel_path}: {e}")
                continue
                
            fm = parse_frontmatter(content)
            
            # Parse identity
            identity_id = fm.get("id", os.path.basename(os.path.dirname(file_path)))
            identity_name = fm.get("name", identity_id)
            description = fm.get("description", "")
            
            # Determine mapping bucket via Strict Physical Namespace
            bucket = get_bucket(rel_path)
            
            record = {
                "id": identity_id,
                "type": bucket,
                "coord": rel_path,
                "name": identity_name,
                "description": description
            }
            
            registry_map[bucket].append(record)
            count += 1

    logging.info(f"Scan complete. Discovered {count} identity nodes.")
    
    # Write output indices
    for bucket, records in registry_map.items():
        filename = f"FAST_{bucket}_INDEX.json"
        out_path = os.path.join(INDICES_DIR, filename)
        
        output_data = {
            "registry": records
        }
        
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=2, ensure_ascii=False)
            
        logging.info(f"Compiled {len(records):5} {bucket:10} -> {filename}")

    logging.info("V5.0 Architectural Indices generation complete.")

if __name__ == "__main__":
    main()
