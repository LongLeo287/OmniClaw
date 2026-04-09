#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ui_library_fetcher.py - OmniClaw UI Components Bridge Tool
------------------------------------------------------------
PURPOSE:
  Acts as a structural bridge to allow the `ui_ux_agent` to search and fetch
  design patterns, color palettes, spacing rules, and framework stacks
  (like Tailwind, NextJS, React) from the `ecosystem/ui_components` library.

USAGE:
  python ui_library_fetcher.py "dashboard" --domain chart --max-results 2
  python ui_library_fetcher.py "auth" --stack nextjs

This script dynamically locates the 5th pillar (ui_components) and passes
the query along seamlessly.
"""

import os
import sys
import subprocess
import argparse
from pathlib import Path

# Resolve path to the global UI Components search engine
ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent.parent.parent
UI_SCRIPTS_DIR = ROOT / "ui_components" / "ui_ux_pro_max" / "scripts"
SEARCH_SCRIPT = UI_SCRIPTS_DIR / "search.py"


def fetch_ui_assets(query, domain=None, stack=None, max_results=3, json_format=False):
    """
    Subprocess call to the master search.py in ui_components.
    """
    if not SEARCH_SCRIPT.exists():
        print(f"Error: UI Components engine not found at {SEARCH_SCRIPT}")
        sys.exit(1)

    cmd = [sys.executable, str(SEARCH_SCRIPT), query]
    
    if domain:
        cmd.extend(["--domain", domain])
    if stack:
        cmd.extend(["--stack", stack])
    if max_results:
        cmd.extend(["--max-results", str(max_results)])
    if json_format:
        cmd.append("--json")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Fetch failed with exit code {e.returncode}:")
        print(e.stderr)
        sys.exit(e.returncode)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="UI Library Fetcher Bridge")
    parser.add_argument("query", help="What UI element are you looking for?")
    parser.add_argument("--domain", "-d", choices=["style", "prompt", "color", "chart", "landing", "product", "ux", "typography"], help="Filter by data domain")
    parser.add_argument("--stack", "-s", choices=["html_tailwind", "react", "nextjs", "flutter", "vue", "svelte"], help="Filter by tech stack")
    parser.add_argument("--max-results", "-n", type=int, default=3, help="Limit output (default 3)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON for strict parsing")
    
    args = parser.parse_args()
    fetch_ui_assets(args.query, args.domain, args.stack, args.max_results, args.json)
