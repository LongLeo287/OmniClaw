"""
Check Github.txt repos vs existing clones in OmniClaw
Outputs: MISSING repos + FOUND repos
"""
import os
import re
from pathlib import Path

GITHUB_TXT = Path(r"D:\OmniClaw\brain\knowledge\library\github_archives\master_github.txt")
SEARCH_ROOTS = [
    Path(r"D:\OmniClaw\plugins"),
    Path(r"D:\OmniClaw\plugins"),
    Path(r"D:\OmniClaw\ecosystem\skills"),
    Path(r"D:\OmniClaw\brain\knowledge\library\Github_Archives"),
]

# Read all URLs from Github.txt
urls = []
seen = set()
for line in GITHUB_TXT.read_text(encoding="utf-8", errors="ignore").splitlines():
    url = line.strip().rstrip("/")
    if url.startswith("https://github.com/") and url not in seen:
        seen.add(url)
        urls.append(url)

print(f"Total unique repos in Github.txt: {len(urls)}")

# Extract repo names from URLs
def repo_name(url):
    parts = url.rstrip("/").split("/")
    return parts[-1].lower() if parts else ""

# Collect all existing cloned repo names
existing = {}
for root in SEARCH_ROOTS:
    if not root.exists():
        continue
    for p in root.rglob(".git"):
        if p.is_dir():
            name = p.parent.name.lower()
            existing[name] = str(p.parent)

print(f"Existing clones found: {len(existing)}")
print()

missing = []
found   = []

for url in urls:
    name = repo_name(url)
    if name in existing:
        found.append((url, existing[name]))
    else:
        missing.append(url)

print(f"{'='*60}")
print(f"✅ ALREADY CLONED ({len(found)}):")
for url, path in found:
    short = path.replace(r"D:\OmniClaw\\", "")
    print(f"  {url.split('/')[-1]:<30} → {short}")

print(f"\n{'='*60}")
print(f"❌ MISSING / NOT CLONED ({len(missing)}):")
for url in missing:
    print(f"  {url}")

# Save missing list
out = Path(r"D:\OmniClaw\brain\knowledge\library\github_archives\master_github.txt")
out.write_text("\n".join(missing), encoding="utf-8")
print(f"\n📄 Missing list saved: {out}")
