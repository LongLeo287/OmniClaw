# Code Review: Edge Case Audit — Pipeline, PR, Security, Web

**Date**: 2026-03-28
**Scope**: `contribai/orchestrator/`, `contribai/pr/`, `contribai/web/`, `contribai/generator/`, `contribai/github/`
**Version**: v3.0.4

---

## Edge Case Verdict Table

| # | Edge Case | Verdict | Evidence / Notes |
|---|-----------|---------|------------------|
| **Orchestrator / Pipeline** | | | |
| 1 | Invalid/expired GitHub token mid-run | **PARTIAL** | `client.py:52-53` catches `httpx.HTTPError` and raises `GitHubAPIError`, but pipeline `_guarded()` (line 275) catches generic `Exception` and appends to errors — run continues with other repos. **Gap**: no token-refresh or re-auth logic. If token expires mid-run, all subsequent repos fail silently. |
| 2 | Concurrent repo processing — can two tasks modify same fork? | **UNHANDLED** | `pipeline.py:256` creates `asyncio.Semaphore(max_conc)` for concurrent processing. Two findings in different repos could target the same popular dependency repo and race on the same fork. No per-fork locking. Branch name uniqueness (slug-based) provides partial mitigation, but `create_branch` (client.py:251) will 422 on collision with no retry. |
| 3 | Hunt mode — discovery returns 0 repos | **HANDLED** | `pipeline.py:397-401`: `if not repos: logger.info("No repos found this round")` then `continue` to next round with delay. No crash, no infinite retry. |
| 4 | SQLite concurrent writes from async tasks — WAL mode? | **UNHANDLED** | No `PRAGMA journal_mode=WAL` anywhere in codebase. `aiosqlite` serializes writes through a single connection, so within one process it is safe. But if two processes (e.g., web server + CLI) share the same DB, writes can block/error. Not critical for current single-process design, but becomes an issue with `contribai serve` + `contribai hunt` running simultaneously. |
| 5 | DB file corrupted/locked | **UNHANDLED** | `memory.py:110-112`: `aiosqlite.connect()` + `executescript(SCHEMA)` has no try/except. Corrupted DB = unrecoverable crash at startup. No integrity check, no recovery path (backup/recreate). |
| **PR Module** | | | |
| 6 | Fork already exists — reuse or error? | **HANDLED** | `manager.py:166-178`: `_fork_if_needed` checks `get_repo_details(username, repo.name)`, returns existing fork if `owner == username`. Falls through to create fork on any exception. |
| 7 | Branch name collision on fork | **UNHANDLED** | `manager.py:81`: calls `create_branch` directly. `client.py:251` posts to git refs API — returns 422 if branch already exists. No catch, no uniqueness suffix. This fails if a previous partial run left a branch behind. The outer `except` in `create_pr` (line 157) catches it as a generic `PRCreationError` but wastes all prior generation work. |
| 8 | Bot filtering — "bot" in legitimate username | **HANDLED** | `patrol.py:33-45`: Uses an explicit allowlist `REVIEW_BOT_LOGINS` of known bot login strings, plus checks `user.type == "Bot"` and `login.endswith("[bot]")`. Does NOT do substring match on "bot" — so `"robotfan42"` passes correctly. |
| 9 | PR force-closed while patrol processes feedback | **HANDLED** | `patrol.py:105-110`: Checks live PR state via API (`pr_data.get("state") != "open"`) before processing. If closed during processing, individual API calls fail gracefully via try/except in `_handle_code_fix` (line 589). |
| **Generator** | | | |
| 10 | LLM returns invalid JSON — retry limit exhausted | **HANDLED** | `engine.py:62-100`: 2-attempt loop (1 retry). On failure, logs warning and returns `None`. Pipeline handles `None` by skipping (`pipeline.py:849-850`). No crash. |
| 11 | Generated code removes entire file content | **PARTIAL** | `engine.py:351-358`: `_validate_changes` checks `len(content) < 10` for new files only. For existing files edited via search/replace, the check is `new_content == original_content` (no-op detection) — but there's no check against near-total deletion. An edit that replaces most of a file with a few characters passes validation. Self-review (line 721) is the second gate but relies on LLM judgment. |
| 12 | Quality score exactly 0.6 threshold — pass or fail? | **HANDLED** | `scorer.py:73-74`: `passed = total_score >= self._min_score`. Score of exactly 0.6 with default `min_score=0.6` **passes**. `>=` operator, deterministic. |
| **GitHub Client** | | | |
| 13 | 5xx retry — all 3 retries fail, exception type? | **HANDLED** | `client.py:66-84`: After 3 attempts, raises `GitHubAPIError` with the status code. Line 84: `raise last_error`. Type is `GitHubAPIError` (not a vague Exception). Clean propagation. |
| 14 | Rate limit `reset_at` in the past — timezone? | **PARTIAL** | `client.py:59`: `reset_at=int(reset)` stores raw epoch seconds from GitHub header. `RateLimitError` stores it but nothing in the codebase actually **waits** until reset. No timezone math involved since it's Unix epoch. However, there's no "wait and retry" for rate limits — the error propagates up immediately. If consumer code sleeps until `reset_at`, a clock-skewed system could sleep forever or negative time. No protection against that. |
| 15 | Search returns repos user already forked | **PARTIAL** | `discovery.py:92`: Dedup by `full_name` and `exclude_repos` config. But no check against already-forked repos. `pipeline.py:267` checks `has_analyzed()` in memory, which would skip re-analysis. If user manually forked a repo (not via ContribAI), `_fork_if_needed` reuses the fork. Not a crash, but could submit PRs to repos the user personally maintains. |
| **Web / Security** | | | |
| 16 | Empty `_valid_keys` list — `any()` behavior | **HANDLED** | `auth.py:50-51`: `if not _auth_enabled: return None`. `_auth_enabled` is set to `len(api_keys) > 0` on configure. Empty list = auth disabled = all requests pass. Correct behavior per design (opt-in auth). |
| 17 | Missing content-length header — payload bounded? | **UNHANDLED** | `webhooks.py:38-40`: `content_length = request.headers.get("content-length")`. If header is missing, `content_length` is `None`, the `if` block is skipped, and `request.body()` reads the full payload with no size limit (default FastAPI/Starlette behavior). **An attacker can omit the header and send an arbitrarily large payload to exhaust server memory.** |
| 18 | Integer overflow on content-length parsing | **PARTIAL** | `webhooks.py:39`: `int(content_length)` — Python ints have no overflow. However, a non-numeric string (e.g., `"abc"`) would raise `ValueError`, returning a 500 to the client. Not exploitable but produces unhandled exception. |
| 19 | Lifespan cleanup — close all connections on shutdown? | **PARTIAL** | `server.py:71-72`: Only closes `_memory`. Does NOT close a `GitHubClient` instance (because the lifespan doesn't create one — pipelines create their own and clean up via `_cleanup()`). However, background tasks triggered via `/api/run` (line 130-145) create their own pipeline+client and if the server shuts down mid-task, `_cleanup()` may not run (BackgroundTasks don't get cancellation signals). Leaked httpx connections. |

---

## Additional Critical Issues Found

### CRITICAL: Webhook signature bypass returns wrong format (webhooks.py:48)

```python
return {"error": "Invalid signature"}, 403  # BUG: tuple, not Response
```

FastAPI does **not** treat a returned tuple `(dict, int)` as `(body, status_code)` the way Flask does. This returns HTTP 200 with the tuple serialized as JSON: `[{"error": "Invalid signature"}, 403]`. **Invalid webhook signatures are silently accepted with a 200 status.** The payload continues to be processed at line 52-62.

**Fix**: Use `return JSONResponse({"error": "Invalid signature"}, status_code=403)` (consistent with line 40).

**Severity**: CRITICAL — bypasses webhook signature verification entirely.

### HIGH: Webhook body read twice (webhooks.py:45,52)

When `_webhook_secret` is set, the body is read at line 45: `body = await request.body()`. Then at line 52: `payload = await request.json()`. The second `request.json()` call re-reads the cached body (Starlette caches `body()`), so it works in practice. **But** when `_webhook_secret` is empty (line 43 is falsy), body is never read at line 45, so `request.json()` at line 52 reads it fresh. This is functionally correct but the signed-body path is fragile — if Starlette ever changes caching behavior, signature verification would use a different body than JSON parsing.

**Severity**: LOW (works now, fragile).

### HIGH: `get_pr_diff` lacks retry and error wrapping (client.py:381-388)

```python
async def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> str:
    resp = await self._client.get(...)
    resp.raise_for_status()
    return resp.text
```

This bypasses the `_request()` method (no retry, no rate limit check, no `GitHubAPIError` wrapping). A 502 from GitHub crashes with raw `httpx.HTTPStatusError` instead of `GitHubAPIError`. Callers in `patrol.py:521` have a bare `except Exception` so it won't crash, but telemetry/error categorization is lost.

**Severity**: HIGH — inconsistent error handling path.

### MEDIUM: No content-length validation in webhook when header missing

As noted in edge case #17. The fix is straightforward:

```python
body = await request.body()
if len(body) > MAX_PAYLOAD_SIZE:
    return JSONResponse({"error": "Payload too large"}, status_code=413)
```

Read the body once, check actual size, use for both signature verification and JSON parsing.

### MEDIUM: `_build_signoff` duplicated across PRManager and PRPatrol

`manager.py:31-43` and `patrol.py:65-73` contain identical `_build_signoff()` implementations. DRY violation.

---

## Positive Observations

1. **Comprehensive duplicate detection** — Pipeline checks both local memory AND GitHub API for existing PRs, using title similarity and file-path tracking (pipeline.py:740-800).
2. **AI policy respect** — Explicit check for AI_POLICY.md and ban keywords in CONTRIBUTING.md before processing (pipeline.py:1254-1312).
3. **Quality gate is well-designed** — 7-check scorer with meaningful heuristics; debug code detection, placeholder detection, file coherence.
4. **Constant-time key comparison** — `auth.py:61` uses `hmac.compare_digest` to prevent timing attacks.
5. **Graceful degradation** — Self-review failure defaults to approve (engine.py:772-773), LLM classification failure defaults to CODE_CHANGE (patrol.py:428-441), validation failure keeps the finding (pipeline.py:1249-1250).
6. **Pre-filter before LLM calls** — Findings on non-code files and protected meta files are filtered before expensive generation (pipeline.py:667-700).

---

## Recommended Actions (Prioritized)

1. **[CRITICAL]** Fix webhook signature bypass: change `return {"error": ...}, 403` to `return JSONResponse(...)` in `webhooks.py:48`.
2. **[HIGH]** Add actual body-size enforcement for webhooks when content-length header is missing.
3. **[HIGH]** Route `get_pr_diff` through `_request()` or add retry/error wrapping.
4. **[MEDIUM]** Add branch-name collision handling: append short hash/timestamp suffix if branch exists, or catch 422 and retry.
5. **[MEDIUM]** Add content-length parsing error handling (`try/except ValueError`).
6. **[MEDIUM]** Consider `PRAGMA journal_mode=WAL` in Memory.init() if multi-process usage is expected.
7. **[LOW]** Add per-fork mutex or serialization to prevent race conditions in concurrent pipeline processing.
8. **[LOW]** Extract `_build_signoff` to a shared utility to eliminate duplication.
9. **[LOW]** Add DB integrity check / recreation fallback for corrupted SQLite.

---

## Metrics

| Metric | Value |
|--------|-------|
| Files Reviewed | 10 |
| Edge Cases Checked | 19 |
| HANDLED | 8 (42%) |
| PARTIAL | 5 (26%) |
| UNHANDLED | 6 (32%) |
| Critical Issues | 1 |
| High Priority | 2 |
| Medium Priority | 4 |
| Low Priority | 3 |

---

## Unresolved Questions

1. Is multi-process usage of the SQLite DB (web server + CLI simultaneously) an intended deployment pattern? If yes, WAL mode is needed.
2. Should the webhook endpoint be protected by the API key auth dependency, or is signature verification the only gate?
3. Is there an intentional reason `get_pr_diff` bypasses `_request()`, or is it an oversight?
