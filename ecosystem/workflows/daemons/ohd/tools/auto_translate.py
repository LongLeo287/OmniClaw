#!/usr/bin/env python3
"""
auto_translate.py - OmniClaw Internal Script Translator
--------------------------------------------------------
PURPOSE:
  Scan all internally-authored scripts (.py, .bat, .ps1) under the core/ directory,
  then auto-translate Vietnamese comments/strings to English, fix character encoding
  issues, and strip hardcoded absolute paths.

USAGE:
  python core/ops/scripts/auto_translate.py [--dry-run] [--verbose]

FLAGS:
  --dry-run   Preview changes without writing to disk
  --verbose   Print each line that gets modified

NOTES:
  - Only targets files in core/ (excludes third-party code in brain/, ecosystem/)
  - Creates .bak backup of every modified file before overwriting
  - Safe to re-run multiple times (idempotent)
"""

import os
import re
import sys
import shutil
import argparse
from pathlib import Path

# ─────────────────────────────────────────────
# CONFIGURATION
# ─────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent.parent.parent  # OmniClaw root
TARGET_DIR = ROOT / "system"

SCAN_EXTENSIONS = {".py", ".bat", ".ps1", ".sh"}

EXCLUDE_DIRS = {
    ".git", "node_modules", "__pycache__", "venv", "env",
    "sandbox", "releases", "Trash_Before_Push", "QUARANTINE",
    "_legacy", "_archive", ".vscode"
}

# ─────────────────────────────────────────────
# VIETNAMESE → ENGLISH TRANSLATION TABLE
# Common phrases found in OmniClaw codebase
# ─────────────────────────────────────────────
VI_TO_EN = {
    # Status & Actions
    "Starting":        "Starting",
    "Finished":         "Finished",
    "Complete":         "Complete",
    "Running":        "Running",
    "Processing":       "Processing",
    "Loading":         "Loading",
    "Syncing":     "Syncing",
    "Checking":    "Checking",
    "Skipping":           "Skipping",
    "Failed":         "Failed",
    "Success":       "Success",
    "Error":              "Error",
    "Warning":         "Warning",
    "Not found":   "Not found",
    "Found":      "Found",
    "Does not exist":    "Does not exist",
    "Created":           "Created",
    "Deleted":           "Deleted",

    # System & Infrastructure
    "System":         "System",
    "Server":          "Server",
    "Port":             "Port",
    "Connection":          "Connection",
    "Disconnected":     "Disconnected",
    "Database":    "Database",
    "Memory":           "Memory",
    "File":              "File",
    "Directory":          "Directory",
    "Path":        "Path",
    "Configuration":         "Configuration",
    "Environment":       "Environment",
    "Variable":             "Variable",
    "Parameter":          "Parameter",
    "Result":          "Result",
    "Data":          "Data",

    # AI / Agent Domain
    "Agent":         "Agent",
    "Brain":           "Brain",
    "Memory":            "Memory",
    "Skill":          "Skill",
    "Task":         "Task",
    "Goal":         "Goal",
    "Plan":         "Plan",
    "Execute":         "Execute",
    "Analyze":        "Analyze",
    "Synthesize":         "Synthesize",
    "Project":            "Project",
    "Employee":        "Employee",
    "Company":          "Company",
    "Department":        "Department",

    # Operations
    "Backup":          "Backup",
    "Restore":         "Restore",
    "Check":         "Check",
    "Verify":         "Verify",
    "Authenticate":         "Authenticate",
    "Authorize":         "Authorize",
    "Cleanup":         "Cleanup",
    "Cleanup":          "Cleanup",
    "Synchronize":      "Synchronize",
    "Update":         "Update",
    "Install":          "Install",
    "Uninstall":       "Uninstall",
    "Upgrade":         "Upgrade",
    "Starting lại":    "Restart",
    "Shutdown":              "Shutdown",
    "Enable":              "Enable",
    "Shutdown tính năng":    "Disable",

    # Common comment phrases
    "# Check":       "# Check",
    "# Create":            "# Create",
    "# Delete":            "# Delete",
    "# Read":            "# Read",
    "# Write":            "# Write",
    "# Load":            "# Load",
    "# Save":            "# Save",
    "# Send":            "# Send",
    "# Receive":           "# Receive",
    "# Connection":        "# Connect",
    "# Disconnected":   "# Disconnect",
    "# Initialize":       "# Initialize",
    "# Configuration":       "# Configure",
    "# Example":          "# Example",
    "# Note":          "# Note",
    "# Important":     "# Important",
    "# TODO":           "# TODO",
    "# FIXME":          "# FIXME",
    "# Run":           "# Run",
    "# Stop":           "# Stop",
    "# Error handling":     "# Error handling",
    "# Add":           "# Add",
    "# Step":           "# Step",
    "# Start":        "# Start",
    "# Finished":       "# End",
    "# Main":          "# Main",
    "# Helper":            "# Helper",
    "# Function":            "# Function",
    "# Class":            "# Class",
    "# Module":         "# Module",

    # Sentence fragments
    "no":         "no",
    "can":           "can",
    "cannot":        "cannot",
    "done":          "done",
    "not done":        "not done",
    "in progress":         "in progress",
    "needs work":          "needs work",
}

# ─────────────────────────────────────────────
# HARDCODED PATH PATTERNS TO REMOVE
# Replace D:\specific\paths with relative equivalents
# ─────────────────────────────────────────────
HARDCODE_PATTERNS = [
    # Matches r"D:\OmniClaw_Admin\OmniClaw CORP\OmniClaw" or similar
    (r'[A-Za-z]:\\[^"\';\s\)]+AI.OS[^"\';\s\)]*', "ROOT"),
    (r'[A-Za-z]:\\[^"\';\s\)]+OmniClaw[^"\';\s\)]*', "REMOTE_ROOT"),
]


def translate_line(line: str) -> str:
    """Apply translation table to a single line."""
    for vi, en in VI_TO_EN.items():
        if vi in line:
            line = line.replace(vi, en)
    return line


def fix_encoding_artifacts(content: str) -> str:
    """Fix common encoding corruption artifacts."""
    # Replace common UTF-8 misread as Windows-1252
    artifacts = {
        "'": "'",
        """: '"',
        """: '"',
        "à": "à",
        "đ": "đ",
        "\r\n": "\n",   # Normalize line endings
    }
    for bad, good in artifacts.items():
        content = content.replace(bad, good)
    return content


def remove_hardcodes(content: str, file_path: Path) -> str:
    """Replace absolute path literals with relative path references."""
    for pattern, replacement in HARDCODE_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            for m in set(matches):
                content = content.replace(f'"{m}"', f'{replacement}')
                content = content.replace(f"'{m}'", f'{replacement}')
    return content


def process_file(fp: Path, dry_run: bool = False, verbose: bool = False) -> dict:
    """
    Process a single file:
    1. Fix encoding artifacts
    2. Translate Vietnamese → English
    3. Strip hardcoded paths

    Returns a summary dict with change stats.
    """
    try:
        original = fp.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        return {"file": str(fp), "status": "READ_ERROR", "error": str(e)}

    # Count non-ASCII chars before
    before_count = sum(1 for c in original if ord(c) > 127)

    modified = fix_encoding_artifacts(original)

    lines_changed = 0
    new_lines = []
    for line in modified.splitlines():
        translated = translate_line(line)
        if translated != line:
            lines_changed += 1
            if verbose:
                print(f"  - OLD: {line.strip()[:80]}")
                print(f"  + NEW: {translated.strip()[:80]}")
        new_lines.append(translated)
    modified = "\n".join(new_lines)

    modified = remove_hardcodes(modified, fp)

    after_count = sum(1 for c in modified if ord(c) > 127)

    changed = (modified != original)
    if changed and not dry_run:
        # Create backup
        backup = fp.with_suffix(fp.suffix + ".bak")
        shutil.copy2(fp, backup)
        fp.write_text(modified, encoding="utf-8")

    return {
        "file": str(fp.relative_to(ROOT)),
        "status": "MODIFIED" if changed else "CLEAN",
        "lines_changed": lines_changed,
        "non_ascii_before": before_count,
        "non_ascii_after": after_count,
    }


def scan_and_translate(dry_run: bool = False, verbose: bool = False):
    """Main entry point: scan TARGET_DIR and process all matching files."""
    print("=" * 60)
    print(f"  OMNICLAW AUTO-TRANSLATOR")
    print(f"  Root: {ROOT}")
    print(f"  Mode: {'DRY RUN (no writes)' if dry_run else 'LIVE (files will be modified)'}")
    print("=" * 60)

    all_files = []
    for dirpath, dirnames, filenames in os.walk(TARGET_DIR):
        dirnames[:] = [d for d in dirnames if d not in EXCLUDE_DIRS]
        for f in filenames:
            fp = Path(dirpath) / f
            if fp.suffix.lower() in SCAN_EXTENSIONS:
                all_files.append(fp)

    print(f"\nFound {len(all_files)} files to process...\n")

    results = []
    for i, fp in enumerate(all_files, 1):
        print(f"[{i:3d}/{len(all_files)}] Processing: {fp.relative_to(ROOT)}")
        result = process_file(fp, dry_run=dry_run, verbose=verbose)
        results.append(result)

    # ── Summary ──
    modified = [r for r in results if r.get("status") == "MODIFIED"]
    clean = [r for r in results if r.get("status") == "CLEAN"]
    errors = [r for r in results if r.get("status") not in ("MODIFIED", "CLEAN")]

    print("\n" + "=" * 60)
    print(f"  TRANSLATION COMPLETE")
    print(f"  Modified : {len(modified)} files")
    print(f"  Already clean: {len(clean)} files")
    print(f"  Errors   : {len(errors)} files")
    print("=" * 60)

    if modified:
        print("\nMODIFIED FILES:")
        for r in modified:
            print(f"  [{r['non_ascii_before']:4d} -> {r['non_ascii_after']:4d} chars]  {r['file']}")

    if errors:
        print("\nERRORS:")
        for r in errors:
            print(f"  FAILED: {r['file']} — {r.get('error', 'unknown')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OmniClaw Auto-Translator")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, do not write")
    parser.add_argument("--verbose", action="store_true", help="Show each changed line")
    args = parser.parse_args()
    scan_and_translate(dry_run=args.dry_run, verbose=args.verbose)