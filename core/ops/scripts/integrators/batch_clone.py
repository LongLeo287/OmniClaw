"""
Batch clone missing GitHub repos from Github.txt
Target: D:\OmniClaw\plugins\github-repos\
"""
import subprocess, sys, os, re
from pathlib import Path
from datetime import datetime

MISSING_TXT = Path(r"D:\OmniClaw\brain\knowledge\library\github_archives\master_github.txt")
TARGET      = Path(r"D:\OmniClaw\plugins\github-repos")
LOG_FILE    = Path(r"D:\OmniClaw\brain\knowledge\library\Github_Archives\clone_log.md")

TARGET.mkdir(parents=True, exist_ok=True)

# Large repos to skip (too big for quick clone)
SKIP_REPOS = {
    "next.js", "plotly.js", "developer-roadmap", "openai-cookbook",
    "excalidraw", "posthog", "trivy", "agents-course", "public-apis",
    "gitignore", "anime", "vercel"
}

urls = [l.strip() for l in MISSING_TXT.read_text(encoding="utf-8").splitlines() if l.strip().startswith("http")]

print(f"Repos to clone: {len(urls)}")
print(f"Target: {TARGET}")
print(f"Skip large repos: {SKIP_REPOS}")
print("="*60)

results = {"ok": [], "skip": [], "fail": []}
start = datetime.now()

for i, url in enumerate(urls, 1):
    name = url.rstrip("/").split("/")[-1]
    dest = TARGET / name

    # Skip if already cloned (in target dir)
    if dest.exists() and (dest / ".git").exists():
        print(f"[{i:02d}] SKIP(exists) {name}")
        results["skip"].append(url)
        continue

    # Skip large known repos
    if name.lower() in SKIP_REPOS or any(s in name.lower() for s in SKIP_REPOS):
        print(f"[{i:02d}] SKIP(large) {name}")
        results["skip"].append(url)
        continue

    # Clone
    print(f"[{i:02d}] Cloning {name}...", end="", flush=True)
    try:
        r = subprocess.run(
            ["git", "clone", "--depth", "1", "--quiet", url, str(dest)],
            capture_output=True, text=True, timeout=60
        )
        if r.returncode == 0:
            print(" ✅")
            results["ok"].append(url)
        else:
            err = r.stderr.strip().split("\n")[-1][:80]
            print(f" ❌ {err}")
            results["fail"].append((url, err))
    except subprocess.TimeoutExpired:
        print(f" ⏱ TIMEOUT")
        results["fail"].append((url, "TIMEOUT"))
    except Exception as e:
        print(f" ❌ {e}")
        results["fail"].append((url, str(e)))

elapsed = (datetime.now() - start).seconds
print(f"\n{'='*60}")
print(f"Done in {elapsed}s:")
print(f"  ✅ Cloned: {len(results['ok'])}")
print(f"  ⏭ Skipped: {len(results['skip'])}")
print(f"  ❌ Failed: {len(results['fail'])}")

if results["fail"]:
    print(f"\nFailed repos:")
    for url, reason in results["fail"]:
        print(f"  {url.split('/')[-1]}: {reason}")

# Write log
log = [
    f"# Clone Log — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
    f"",
    f"| Result | Count |",
    f"|--------|-------|",
    f"| Cloned | {len(results['ok'])} |",
    f"| Skipped | {len(results['skip'])} |",
    f"| Failed | {len(results['fail'])} |",
    f"",
    f"## Cloned",
    "\n".join(f"- {u}" for u in results["ok"]),
    f"",
    f"## Failed",
    "\n".join(f"- {u}: {r}" for u, r in results["fail"]),
]
LOG_FILE.write_text("\n".join(log), encoding="utf-8")
print(f"\n📄 Log: {LOG_FILE}")
