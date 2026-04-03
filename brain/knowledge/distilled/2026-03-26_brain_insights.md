# Distilled Insights from Brain Sessions (03/2026)
# Source: .gemini/antigravity/brain/ — March 2026 Sessions
# Generated: 2026-03-26 | By: facility-agent (Dept 22) + learning-agent (Dept 14)
# Policy: APPEND ONLY — do not overwrite existing knowledge

---

## 1. GitNexus — Lessons Learned

**Recorded Issues:**
- CDP port 9222 frequently returns 403 Forbidden when Browser automation attempts to connect.
- `gitnexus serve :4747` crashes after an idle period — requires daemon restart.
- Proxy endpoint `/api/gitnexus/api/repos` returns 502 when server is offline.

**Discovered Solutions:**
- Always perform a health check on `http://127.0.0.1:9222/json/version/` before establishing the Browser tool connection.
- Restart gitnexus via `gitnexus serve` prior to each CodeIntel session.
- Utilize the cache-buster `?t=<timestamp>` parameter upon page reload to prevent stale cache issues.

**OmniClaw Impact:**
- `it-manager-agent` must implement a health check protocol for gitnexus in Phase 0 (System Health).
- We should append auto-restart logic specifically for gitnexus within `launcher/START OmniClaw.ps1`.

---

## 2. Browser Automation — Common Errors

**Recorded Error Patterns:**
- `ERR_CONNECTION_REFUSED` occurs if the dev server (Vite/Next.js) has not fully initialized.
- Mixed Content/HTTPS issues arise when embedding HTTP resources within HTTPS pages.
- Browser tool connectivity is unstable, requiring multiple retries (4+ times) for external domains.

**Extracted Best Practices:**
- Definitively verify that the server is active BEFORE initializing browser interactions (`Test-NetConnection`).
- Use `http://127.0.0.1` explicitly rather than `http://localhost` to avoid systemic DNS lookup failures.
- The standard 30s timeout is insufficient for heavy React/Svelte pipelines — increase globally to 60s.

---

## 3. Tiem Nuoc Nho v5 Project — Architecture

**Notes from analysis.md (14/03):**
- Fullstack Web implementation using LadybugDB (custom storage layer).
- OmniClaw integration points defined for: client-facing operations + agent-assisted workflows.
- Architecture: Frontend SPA + Backend Python FastAPI.

**Status At That Time:** Code structure analysis in progress.

---

## 4. OmniClaw Architecture — Snapshot 03/2026

**Extracted from Scratchpad Sessions:**
- The overall OmniClaw matrix registered 567,772 nodes and 1,472,756 edges in GitNexus Code Intel logic (14/03).
- nullclaw domain: 335 nodes, 319 edges (drastically smaller compared to OmniClaw Core).
- Tech Stack for LiveMap visualization includes: Sigma.js + graphology + ForceAtlas2.

---

## 5. ClawTask — Resolved Bugs

**Session 21/03:**
- Fixed the Task checklist rendering issue (resolved completely).
- Browser CDP connection reliability measurably improved after this execution block.

---

*Note: Screenshots and associative media files (*.webp, *.png) logged with these sessions were purged post-distillation to free up disk space.*
