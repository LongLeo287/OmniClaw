---
id: repo-on-demand
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:08.713699
---

# Department: operations
---
description: Repo On-Demand — how agents clone large repos when starting a project
---

# 🗂️ Repo On-Demand Workflow

## Khi nào trigger
Tự động khi:
- Agent/dept bắt đầu project mới (phase 3: dispatch)
- CEO tạo brief có từ khóa liên quan (frontend, security, analytics, etc.)
- `omniclaw.py project init <name>` được gọi
- Telegram: `/project <description>`

Manual khi:
- CEO paste yêu cầu dự án → Antigravity nhận diện

---

## Step 1 — Auto-Detect (repo_resolver.py)

```powershell
# Từ Description: dự án
python ops/scripts/repo_resolver.py "Build analytics dashboard with KPI charts"

# Từ phòng ban
python ops/scripts/repo_resolver.py --dept engineering

# Từ file proposal
python ops/scripts/repo_resolver.py --file brain/shared-context/corp/proposals/PROP_xyz.md

# Auto-clone ngay
python ops/scripts/repo_resolver.py "Build security scanner for CIV" --clone
```

---

## Step 2 — Clone On-Demand

```powershell
# Lệnh clone cho từng repo (xem LARGE_REPOS_CATALOG.md để chọn)
git clone --depth 1 <URL> "$OMNICLAW_ROOT\plugins\github-repos\<REPO>"
```

---

## Step 3 — Notify CEO

Sau khi clone → Antigravity gửi Telegram:
```
📥 REPO CLONED
Source: github.com/...
Project: <tên dự án>
Dept: <phòng ban>
Path: plugins/github-repos/<name>
Size: xxx MB
```

---

## Step 4 — Cleanup (tùy chọn)

```powershell
# Xóa repo sau khi dự án xong (nếu không cần giữ)
Remove-Item -Recurse -Force "$OMNICLAW_ROOT\plugins\github-repos\<REPO>"
```

---

## Tag Map (auto-detect keywords)

| Tag | Keywords | Repos |
|-----|----------|-------|
| FRONTEND | web app, ui, dashboard, react | next.js, anime |
| VISUALIZATION | chart, graph, kpi, plot | plotly.js |
| ANALYTICS | analytics, tracking, metrics | posthog |
| SECURITY | scan, vulnerability, audit, civ | trivy |
| AI-PATTERNS | llm, rag, prompt, research | openai-cookbook |
| TRAINING | training, onboard, roadmap | developer-roadmap, agents-course |
| INTEGRATION | api, external, webhook | public-apis |
| DIAGRAM | whiteboard, architecture, draw | excalidraw |
| TEMPLATE | gitignore, repo setup | gitignore |

---

## Dept Defaults

| Dept | Auto-resolve repos |
|------|--------------------|
| engineering | next.js, plotly.js, openai-cookbook |
| design | excalidraw, anime, next.js |
| rd | openai-cookbook, agents-course, public-apis |
| security | trivy |
| analytics | posthog, plotly.js |
| training | agents-course, developer-roadmap |
| devops | trivy, gitignore |
| product | next.js, excalidraw, posthog |

---

## Integration Points

- `ops/omniclaw.py project init <name> --dept <dept>` → runs repo_resolver
- `ops/scripts/brief_writer.py` → appends repo suggestions per dept
- `infra/channels/bridge_router.py` → `/project <desc>` Telegram command
- `brain/knowledge/notes/LARGE_REPOS_CATALOG.md` → human-readable catalog

---

*Workflow v1.0 | 2026-03-25 | Owner: Antigravity*

