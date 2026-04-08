---
id: ki-batch02-infra-trio
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:00.382823
---

# KI Batch 2: Firecrawl + GitIngest + Strix
**Ingested:** 2026-03-21 | **Nova Batch 2** | Infrastructure Core Trio

---

## KI: Firecrawl — Web→LLM Data API
**Category:** Nova Intake Tool (ALREADY ACTIVE as plugin)

### What It Is
Turn any website into LLM-ready data. Industry-leading reliability (>80% benchmark score).

### 6 Core Capabilities
| Feature | API Endpoint | Nova Use Case |
|---------|-------------|---------------|
| **Scrape** | `/v2/scrape` | CEO gửi URL → Nova scrape markdown |
| **Search** | `/v2/search` | Search + full content extraction |
| **Browse** | `/v2/browser` | Interactive browser for JS-heavy sites |
| **Map** | `/v2/map` | Discover all URLs on a site |
| **Crawl** | `/v2/crawl` | Full site crawl async |
| **Agent** | `/v2/agent` | "Find X" → autonomous extraction |

### Key Outputs
- `markdown` — LLM-ready clean text
- `json` — Structured extraction with schema or prompt
- `screenshot` — Base64 visual capture
- `branding` — Colors, fonts, typography extraction

### Firecrawl Skill Install (already in OmniClaw stack)
```bash
npx -y firecrawl-cli@latest init --all --browser
# OR
npx skills add firecrawl/cli
```

### OmniClaw Integration
- **Nova's primary web intake tool** for CEO Standing Order URLs
- Firecrawl MCP server available → integrate with OmniClaw MCP cluster (port 7000)
- `/v2/agent` = autonomous research mode (no URL needed, just "find X")
- Cost note: `spark-1-mini` = 60% cheaper than pro model → default for routine intake

### Headroom + Firecrawl Synergy
Firecrawl → raw markdown (large) → Headroom compress → send to LLM (50-90% token reduction)

---

## KI: Strix — AI Security Hacker Agents
**Category:** Dept 10 (Security) core tool | ⚠️ POWERFUL — use with permission only

### What It Is
Open-source autonomous AI security agents that act like real hackers. Finds and validates vulnerabilities with actual PoCs.

### Security Coverage
- Access Control (IDOR, privilege escalation, auth bypass)
- Injection (SQL, NoSQL, command injection)
- Server-Side (SSRF, XXE, deserialization)
- Client-Side (XSS, prototype pollution)
- Business Logic (race conditions)
- Infrastructure (misconfigs, exposed services)

### 3-Mode Operation
```bash
strix --target ./app-directory        # Local codebase
strix --target https://github.com/org/repo  # GitHub repo  
strix --target https://app.com         # Black-box web app
```

### Multi-Agent Architecture
"Graph of Agents" → distributed, parallel, specialists for different attack types.
Agents collaborate + share discoveries = comprehensive coverage.

### LLM Config for OmniClaw
```bash
export STRIX_LLM="anthropic/claude-sonnet-4-6"  # or vertex_ai/gemini-3-pro
export LLM_API_BASE="http://localhost:7000"  # → OmniClaw API Bridge!
export LLM_API_KEY='[REDACTED_API_KEY]'
```

### OmniClaw Integration
- **Dept 10 (Security)**: Primary security testing tool for all plugins/agents
- **CI/CD gate**: Add Strix GitHub Actions to `strix -n --scan-mode quick` before any plugin deploy
- **Strix Protocol v2.0**: Strix CLI scan as step 3 in current 12-stage vetting workflow

### Note on Naming Conflict
⚠️ OmniClaw has "Strix" as Dept 10 name. This `strix` repo = external open-source tool.
The internal "Strix" department can adopt/use `strix` CLI as its primary scanning tool.

---

## KI: GitIngest — Repo→LLM Text Digest
**Category:** Nova Intake Tool | Supplement to native git reading

### What It Is
Turn any Git repo into a prompt-friendly text digest. CLI + Python package.

### Core Usage
```python
from gitingest import ingest

# Local dir
summary, tree, content = ingest("path/to/directory")

# GitHub URL
summary, tree, content = ingest("https://github.com/org/repo")

# Specific subdirectory
summary, tree, content = ingest("https://github.com/org/repo/tree/main/src")
```

### Output Includes
- **Summary**: File structure stats, size, token count
- **Tree**: Directory tree
- **Content**: Full file contents formatted for LLM

### CLI Quick Use
```bash
gitingest https://github.com/org/repo
gitingest https://github.com/org/repo -o repo-digest.md
gitingest https://github.com/org/repo --token $GITHUB_TOKEN  # private repos
```

### Tip: Gitingest.com URL Trick
Change `github.com` → `gitingest.com` in any GitHub URL to get the digest instantly.

### OmniClaw Integration
- **Nova CEO intake**: When CEO sends GitHub URL → `gitingest` → markdown → open-notebook
- **Alternative to manual README reading**: Full repo digest in one call
- **Batch processing**: Loop over all 100 repos → generate digests → batch ingest

### Batch Script for Remaining Repos
```python
from gitingest import ingest
import os

repos_dir = "$OMNICLAW_ROOT/brain/knowledge/repos"
for repo in os.listdir(repos_dir):
    if not os.path.exists(f"{repos_dir}/{repo}/ki-synthesis.md"):
        try:
            summary, tree, content = ingest(f"{repos_dir}/{repo}")
            # Save digest for Nova ingestion
            with open(f"{repos_dir}/{repo}/gitingest-digest.txt", "w") as f:
                f.write(f"{summary}\n\n{tree}\n\n{content[:5000]}")
        except Exception as e:
            print(f"Skipped {repo}: {e}")
```

## Routes
- **Firecrawl**: Dept 13 (Nova intake), Dept 8 (Ops MCP extension)
- **Strix tool**: Dept 10 (Security), Dept 20 (CIV vetting pipeline)
- **GitIngest**: Dept 13 (Nova batch ingestion), Dept 22 (Data Upgrade)
