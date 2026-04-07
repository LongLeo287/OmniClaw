"""
Wire Repo-on-Demand into AI OS integration points.
Run once. Safe to re-run (idempotent).
"""
import json, re
from pathlib import Path

ROOT = Path(r"D:\OmniClaw")

results = []

# ─── 1. GEMINI.md — add rule ──────────────────────────────────────────────────
gemini = ROOT / "GEMINI.md"
rule = """

## REPO-ON-DEMAND RULE (2026-03-25)
When starting any project or dispatch:
1. Run `python ops/scripts/repo_resolver.py "<description>"` to detect needed repos
2. Or by dept: `python ops/scripts/repo_resolver.py --dept <dept>`  
3. Auto-clone: `python ops/aos.py project init <name> --dept <dept> --clone`
4. Catalog: `brain/knowledge/notes/LARGE_REPOS_CATALOG.md`

Tag → Repo: FRONTEND→next.js | SECURITY→trivy | ANALYTICS→posthog | AI-PATTERNS→openai-cookbook | TRAINING→developer-roadmap | DIAGRAM→excalidraw | CHARTS→plotly.js | ANIMATION→anime | INTEGRATION→public-apis
"""
content = gemini.read_text(encoding="utf-8")
if "REPO-ON-DEMAND" not in content:
    gemini.write_text(content + rule, encoding="utf-8")
    results.append("✅ GEMINI.md — rule added")
else:
    results.append("⏭ GEMINI.md — already has rule")

# ─── 2. HUD.md — append control panel entry ──────────────────────────────────
hud = ROOT / "hud" / "HUD.md"
hud_entry = """
### 📦 Repo On-Demand
| Action | Command |
|--------|---------|
| Detect repos | `python ops/scripts/repo_resolver.py "mô tả dự án"` |
| By dept | `python ops/scripts/repo_resolver.py --dept engineering` |
| Project init | `python ops/aos.py project init <name> --dept <dept> --clone` |
| View catalog | `brain/knowledge/notes/LARGE_REPOS_CATALOG.md` |
"""
hud_content = hud.read_text(encoding="utf-8")
if "repo_resolver" not in hud_content:
    hud.write_text(hud_content + hud_entry, encoding="utf-8")
    results.append("✅ HUD.md — Repo On-Demand section added")
else:
    results.append("⏭ HUD.md — already wired")

# ─── 3. aos.py — add project command ─────────────────────────────────────────
aos = ROOT / "ops" / "aos.py"
aos_content = aos.read_text(encoding="utf-8")

project_fn = '''

# ─── Project Init (Repo-on-Demand) ─────────────────────────────────────────────

def cmd_project(args):
    """project init — resolve needed repos + optional auto-clone"""
    import subprocess as _sp
    sub  = args[0] if args else "init"
    rest = args[1:] if len(args) > 1 else []
    name = rest[0] if rest and not rest[0].startswith("--") else sub
    dept = ""
    auto_clone = False
    for i, a in enumerate(rest):
        if a == "--dept" and i+1 < len(rest): dept = rest[i+1]
        if a == "--clone": auto_clone = True

    print(f"\\n{'='*50}\\nPROJECT INIT: {name}\\n{'='*50}")
    if dept: print(f"  Dept: {dept}")
    resolver = os.path.join(ROOT, "ops", "scripts", "repo_resolver.py")
    cmd = [sys.executable, resolver] + (["--dept", dept] if dept else [name])
    if auto_clone: cmd += ["--clone"]
    _sp.run(cmd, cwd=ROOT)
    print(f"\\n  Catalog: brain/knowledge/notes/LARGE_REPOS_CATALOG.md")
    print(f"  Workflow: ops/workflows/repo-on-demand.md")
'''

if "cmd_project" not in aos_content:
    aos_content += project_fn
    results.append("✅ aos.py — cmd_project added")
else:
    results.append("⏭ aos.py — cmd_project exists")

# Wire dispatcher
if '"project"' not in aos_content and "cmd_project" in aos_content:
    aos_content = aos_content.replace(
        'elif cmd == "intake":',
        'elif cmd == "project":\n        cmd_project(args[1:])\n    elif cmd == "intake":'
    )
    results.append("✅ aos.py — project wired to dispatcher")
else:
    results.append("⏭ aos.py — dispatcher already wired or not found")

aos.write_text(aos_content, encoding="utf-8")

# ─── 4. bridge_router.py — add /project Telegram command ─────────────────────
router = ROOT / "infra" / "channels" / "bridge_router.py"
router_content = router.read_text(encoding="utf-8")

project_tg = '''
    elif cmd == "/project":
        if len(parts) < 2:
            return "Usage: /project <mieu ta du an>\\nEx: /project build analytics dashboard"
        desc = " ".join(parts[1:])
        import subprocess as _sp, sys as _sys
        try:
            r = _sp.run(
                [_sys.executable, str(_AIOS_ROOT/"ops"/"scripts"/"repo_resolver.py"), desc],
                capture_output=True, text=True, timeout=10, cwd=str(_AIOS_ROOT)
            )
            out = (r.stdout or "No match found").strip()[:600]
            return f"Repo Resolver: {desc[:50]}\\n{out}"
        except Exception as e:
            return f"Resolver error: {e}"
'''

if '"/project"' not in router_content:
    router_content = router_content.replace(
        '    elif cmd == "/intake":',
        project_tg + '\n    elif cmd == "/intake":'
    )
    router.write_text(router_content, encoding="utf-8")
    results.append("✅ bridge_router.py — /project added")
else:
    results.append("⏭ bridge_router.py — /project exists")

# ─── 5. telegram_bridge.py — register /project handler ───────────────────────
tg = ROOT / "infra" / "channels" / "telegram_bridge.py"
tg_content = tg.read_text(encoding="utf-8")
if '"project"' not in tg_content:
    tg_content = tg_content.replace(
        '"brief", "retro", "pulse", "proposals", "intake"',
        '"brief", "retro", "pulse", "proposals", "intake", "project"'
    )
    tg.write_text(tg_content, encoding="utf-8")
    results.append("✅ telegram_bridge.py — /project registered")
else:
    results.append("⏭ telegram_bridge.py — already registered")

# ─── Summary ──────────────────────────────────────────────────────────────────
print("\n=== WIRE RESULTS ===")
for r in results:
    print(f"  {r}")
print(f"\nDone — {sum(1 for r in results if r.startswith('✅'))} integrations wired")
