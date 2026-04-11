#!/usr/bin/env python3
"""
process_github_queue.py — OmniClaw Batch GitHub Intake Tool (Update RULE-CIV-02)
Read URLs from vault/vault/DATA/Github.txt and push to PENDING_REPOS.md.
Strictly forbidden to clone directly here to comply with PENDING GATE.
After successfully pushing to PENDING, remove URLs from Github.txt.
"""

import os
import sys
import datetime
import re

ROOT = os.path.normpath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
VAULT_FILE = os.path.join(ROOT, "storage", "vault", "DATA", "Github.txt")
PENDING_FILE = os.path.join(ROOT, "storage", "vault", "DATA", "PENDING_REPOS.md")

def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def process_queue():
    if not os.path.exists(VAULT_FILE):
        print(f"File not found: {VAULT_FILE}")
        return

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip() and line.startswith("http")]

    if not urls:
        print("No URLs found in Github.txt to process.")
        return

    print(f"=> Found {len(urls)} URLs to process in Github.txt.")

    # Read existing PENDING to avoid duplicates
    existing_pending = set()
    if os.path.exists(PENDING_FILE):
        with open(PENDING_FILE, "r", encoding="utf-8") as f:
            existing_pending = set(re.findall(r'https://github\.com/[\w\-\.]+/[\w\-\.]+', f.read()))

    added_count = 0
    with open(PENDING_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n## Batch from Github.txt — {now()}\n\n")
        f.write("| No | Repo | Notes | Date Added |\n")
        f.write("|-----|------|---------|-----------|\n")

        for i, url in enumerate(urls, 1):
            url_clean = url.rstrip('/')
            if url_clean in existing_pending:
                print(f"  [!] {url_clean} already exists in PENDING_REPOS.md. Skipping.")
                continue

            repo_name = url_clean.split("/")[-1]
            owner_repo = "/".join(url_clean.split("/")[-2:])

            f.write(f"| {i} | [{owner_repo}]({url_clean}) | Auto-queued from Github.txt | {now()[:10]} |\n")
            print(f"  [+] Added to PENDING: {owner_repo}")
            added_count += 1

    # Clear Github.txt file after processing (if URLs were read)
    if urls:
        with open(VAULT_FILE, 'w', encoding='utf-8') as _f:
            pass
        print(f"\n=> [RULE-CIV-02 OK] Transferred {added_count} new URLs to PENDING_REPOS.md.")
        print("=> Github.txt has been cleared.")
    else:
        print(f"\n=> [RULE-CIV-02 OK] No new URLs were added.")

    print("=> Next step: Run core/ops/scripts/civ_classifier.py to review.")

if __name__ == "__main__":
    process_queue()