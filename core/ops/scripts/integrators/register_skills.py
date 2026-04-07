import json
from pathlib import Path

root = Path(r"D:\OmniClaw")
reg  = root / "brain" / "shared-context" / "SKILL_REGISTRY.json"

try:
    data = json.loads(reg.read_text(encoding="utf-8"))
except Exception:
    data = {}

if "skills" not in data:
    data["skills"] = []

existing_names = {s.get("name") for s in data["skills"] if isinstance(s, dict)}

new_skills = [
    {"name":"stitch-design","tier":"tier1","source":"google-labs-code/stitch-skills","path":".agents/skills/stitch-design","agents":["Antigravity"],"status":"active","added":"2026-03-25"},
    {"name":"stitch-loop","tier":"tier1","source":"google-labs-code/stitch-skills","path":".agents/skills/stitch-loop","agents":["Antigravity"],"status":"active","added":"2026-03-25"},
    {"name":"enhance-prompt","tier":"tier2","source":"google-labs-code/stitch-skills","path":".agents/skills/enhance-prompt","agents":["Antigravity"],"status":"active","added":"2026-03-25"},
    {"name":"design-md","tier":"tier2","source":"google-labs-code/stitch-skills","path":".agents/skills/design-md","agents":["Antigravity"],"status":"active","added":"2026-03-25"},
    {"name":"react-components","tier":"tier2","source":"google-labs-code/stitch-skills","path":".agents/skills/react-components","agents":["Antigravity"],"status":"active","added":"2026-03-25"},
    {"name":"stitch-wireframe-generator","tier":"tier1","source":"arinnem/stitchSkill","path":"plugins/stitchSkill","agents":["Antigravity"],"status":"active","added":"2026-03-25","notes":"CEO personal skill - 16 auto-screens"},
]

added = 0
for s in new_skills:
    if s["name"] not in existing_names:
        data["skills"].append(s)
        added += 1
        print(f"  [ADD] {s['name']}")
    else:
        print(f"  [SKIP] {s['name']} already registered")

data["last_updated"] = "2026-03-25"
reg.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

total = len([s for s in data.get("skills", []) if isinstance(s, dict)])
print(f"\nSKILL_REGISTRY.json OK — {added} new, total: {total} skills")

# Also wire browser-use as web-crawler backend note
note_path = root / "brain" / "knowledge" / "notes" / "KI-browser-use-wired-2026-03-25.md"
note_path.write_text("""# browser-use — Wired as Web-Crawler Backend
Date: 2026-03-25
Status: INSTALLED (pip install browser-use)
Route: CIV pipeline → web-crawler agent → browser-use

## Usage in CIV
When CIV classifies input as WEB type:
→ web-crawler agent calls browser_use.Agent
→ LLM: ChatGoogle (gemini-3-flash) or Groq
→ Output: extracted content → brain/knowledge/notes/KI-<name>.md

## Install note
- Installed: 2026-03-25
- Python: 3.14 (browser_use __version__ not exposed but functional)
- Config: add BROWSER_USE_API_KEY to .env for cloud, or use local Chromium
""", encoding="utf-8")
print("  browser-use wire note written")
