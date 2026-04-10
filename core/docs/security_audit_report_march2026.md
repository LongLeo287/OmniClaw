---
id: security-audit-report-march2026
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.659546
---

# GitHub Issues — OmniClaw Code Review
> Copy a section below to create an issue at: https://github.com/OmniClaw-Corp/omniclaw-local/issues/new

---

## ISSUE 1 of 9

**Title:** `[CRITICAL][server.js] CORS Wildcard + No Body Size Limit + No Rate Limiting`

**Labels:** `bug`, `security`

**Body:**
```
## 🔴 Critical Security Issues — `system/infra/api/server.js`

**Review date:** 2026-03-28

---

### C1 — CORS Wildcard `*` (Line 20-26)

```javascript
const CORS = {
  "Access-Control-Allow-Origin": "*",  // ← DANGEROUS
};
```

**Risk:** Any website can send requests to this API → CSRF, data exfiltration.
**Fix:** Whitelist origin from env var `ALLOWED_ORIGINS`.

---

### C2 — No Request Body Size Limit (Line 41-48)

```javascript
req.on("data", chunk => body += chunk);  // ← No limit!
```

**Risk:** Attacker sends GB-sized request → memory exhaustion, crash entire API server.
**Fix:** Add `MAX_BODY_SIZE = 1MB`, destroy request if it exceeds limit.

---

### C3 — No Rate Limiting / Authentication (All endpoints)

- No rate limiting
- No API key validation
- `/api/corp/escalate` can be flooded → file system full
- GET endpoints are easily DDoS-able

**Fix:** Add rate-limit middleware + API key header check.
```

---

## ISSUE 2 of 9

**Title:** `[HIGH][server.js] Unvalidated Input Write to File + JSON Parse No Try-Catch + Manual YAML Parsing`

**Labels:** `bug`, `security`

**Body:**
```
## 🟠 High Issues — `system/infra/api/server.js`

**Review date:** 2026-03-28

---

### C4 — Unvalidated Input Write to File System (Line 95-105)

```javascript
const { dept, level, issue } = body;
// "issue" is not sanitized!
const entry = `\n## [${ts}] ${level} — ${dept}\n${issue}\n_Status: OPEN_\n`;
fs.writeFileSync(escPath, existing + entry);
```

**Risk:** `issue` length is not validated → resource exhaustion. Injection risk if file is parsed later.
**Fix:** Validate `issue.length <= 5000`, strip control characters.

---

### C5 — JSON Parse Missing Try-Catch (Line 34)

```javascript
function readJson(filePath) {
  return fs.existsSync(filePath) ? JSON.parse(fs.readFileSync(filePath, "utf-8")) : null;
  //                                ↑ Corrupt file → uncaught exception → server crash!
}
```

**Risk:** Corrupt `blackboard.json` or `SKILL_REGISTRY.json` → API server crashes completely.
**Fix:** Wrap `JSON.parse` in `try-catch`, return `null` on error.

---

### C7 — Manual YAML Parsing with Weak Regex (Line 137-148)

```javascript
const [k, v] = line.trim().split(": ");  // ← Value contains ": " → split fails!
result[k] = v;                           // ← v can be undefined → crash!
```

**Fix:** Use `js-yaml` npm package instead of manual regex.

---

### L4 — parseBody() Silent Error (Line 46)

```javascript
try { resolve(JSON.parse(body)); } catch { resolve({}); }  // ← No logging!
```

**Impact:** Invalid JSON body is treated as empty object → subtle bugs that are hard to debug.
**Fix:** Log a warning when parsing fails.

---

### L5 — Query Parameter Filter Missing Validation (Line 66-68)

```javascript
if (query.tier) entries = entries.filter(s => String(s.tier) === query.tier);
```

**Fix:** Validate `query.tier` is in `['0','1','2','3','4']` before filtering.

---

### S5 — Missing Audit Logging For Write Operations

`/api/corp/escalate` writes to file but does not log requester IP, timestamp, or content.
**Fix:** Write audit log before `fs.writeFileSync()`.
```

---

## ISSUE 3 of 9

**Title:** `[HIGH][batch_repo_intake.py] Bare except: Swallows All Exceptions`

**Labels:** `bug`

**Body:**
```
## 🟠 High — `system/ops/scripts/batch_repo_intake.py`

**Review date:** 2026-03-28

### C6 — Silent Exception Swallowing (Line 86-90)

```python
try:
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read().decode('utf-8', errors='ignore')
except:  # ← Bare except! Swallows ALL errors including KeyboardInterrupt!
    return None
```

**Risk:**
- Blind to execution failures
- Cannot be debugged
- Swallows `KeyboardInterrupt`, `SystemExit`

**Fix:**
```python
except (urllib.error.URLError, urllib.error.HTTPError, socket.timeout) as e:
    print(f"[WARN] Failed to fetch {owner}/{repo}: {e}", file=sys.stderr)
    return None
```

This pattern repeats across the file — audit all bare `except:` clauses.
```

---

## ISSUE 4 of 9

**Title:** `[HIGH][omniclaw_integrate.py] Unvalidated CLI Arg Split + Broken .env Parser`

**Labels:** `bug`

**Body:**
```
## 🟠 High — `system/ops/scripts/omniclaw_integrate.py`

**Review date:** 2026-03-28

### C9 — Unvalidated CLI Argument Split (Line 49)

```python
owner, repo_name = full_name.split('/')  # ← If no '/' → ValueError crash!
```

Input from `sys.argv` is unpacked without validation. Any string lacking `/` → crash.

**Fix:**
```python
if '/' not in full_name or full_name.count('/') != 1:
    print(f"[ERROR] Invalid format: '{full_name}'. Expected: owner/repo")
    continue
owner, repo_name = full_name.split('/')
```

---

### C10 — Flawed .env Parser (Line 11-17)

```python
def get_github_token():
    if os.path.exists(ENV_FILE):
        with open(ENV_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('GITHUB_TOKEN='):
                    return line.strip().split('=', 1)[1]
    return None
```

**Issues:**
- Does not skip comment lines starting with `#`
- Does not skip blank lines
- `GITHUB_TOKEN=` (empty value) → returns `""` — truthy but invalid
- Missing error handling if file read fails

**Fix:** Use the `python-dotenv` library or add robust validation.
```

---

## ISSUE 5 of 9

**Title:** `[HIGH][sync_identity_1_1.js] Hardcoded Placeholder <OMNICLAW_ROOT> Never Replaced`

**Labels:** `bug`

**Body:**
```
## 🟠 High — `system/ops/scripts/sync_identity_1_1.js`

**Review date:** 2026-03-28

### C8 — Hardcoded Placeholder (Line 4)

```javascript
const rootDir = '<OMNICLAW_ROOT>';  // ← Unreplaced template placeholder!
```

This script will **fail entirely** execution because `<OMNICLAW_ROOT>` is not a valid path on any OS.

**Fix Option A** (dynamic):
```javascript
const rootDir = path.resolve(__dirname, '../../..');
```

**Fix Option B** (env-based):
```javascript
const rootDir = process.env.OMNICLAW_ROOT || path.resolve(__dirname, '../../..');
```

Audit entire codebase for any unreplaced `<OMNICLAW_ROOT>` placeholders.
```

---

## ISSUE 6 of 9

**Title:** `[MEDIUM][omniclaw_orchestrator.py] Silent LTM Module Import Failure`

**Labels:** `bug`

**Body:**
```
## 🟡 Medium — `system/ops/omniclaw_orchestrator.py`

**Review date:** 2026-03-28

### L1 — Silent Module Import Failure (Line 27-37)

```python
try:
    from system.ops.scripts.memory_daemon import MemoryCore as _MemoryCore
    from system.ops.scripts.agent_bus import AgentBus as _AgentBus
    _MEMORY_CORE = _MemoryCore()
    _AGENT_BUS   = _AgentBus()
    _LTM_ONLINE  = True
except Exception as _e:
    _LTM_ONLINE = False   # ← _e is swallowed entirely, nobody knows why LTM is offline!
    _MEMORY_CORE = None
    _AGENT_BUS   = None
```

Graceful degradation is good, but failure to log exceptions makes debugging LTM offline states extremely difficult in production.

**Fix:**
```python
except Exception as _e:
    import sys
    print(f"[WARN] LTM components unavailable: {type(_e).__name__}: {_e}", file=sys.stderr)
    _LTM_ONLINE = False
    _MEMORY_CORE = None
    _AGENT_BUS   = None
```
```

---

## ISSUE 7 of 9

**Title:** `[MEDIUM][system_pulse.py] Telegram Credentials Not Validated + No Message Length Check`

**Labels:** `bug`

**Body:**
```
## 🟡 Medium — `system/automations/daemons/system_pulse.py`

**Review date:** 2026-03-28

### L2 — Telegram Credentials Unvalidated (Line 42-43)

```python
TOKEN   = _ENV.get("TELEGRAM_BOT_TOKEN", "")
CHAT_ID = _ENV.get("TELEGRAM_CHAT_ID", "")
```

If `TOKEN=""`, `send_telegram()` is still called generating an invalid URL → Telegram API rejects silently with HTTP error.

**Fix:**
```python
TOKEN   = _ENV.get("TELEGRAM_BOT_TOKEN") or ""
CHAT_ID = _ENV.get("TELEGRAM_CHAT_ID") or ""
if not TOKEN or not CHAT_ID:
    print("[WARN] Telegram credentials not configured. Alerts disabled.", file=sys.stderr)
```

---

### L3 — Message Length Unvalidated (Line 89-101)

Telegram API limits payloads to 4096 characters/message. If message is longer → API rejects silently, alert is lost.

**Fix:**
```python
def send_telegram(text: str):
    if not TOKEN or not CHAT_ID:
        return
    if len(text) > 4096:
        text = text[:4093] + "..."
    # ... rest of function
```
```

---

## ISSUE 8 of 9

**Title:** `[MEDIUM][SKILL_REGISTRY.json] dependabot-secretary skill exists on disk but not registered`

**Labels:** `bug`, `documentation`

**Body:**
```
## 🟡 Medium — `brain/registry/SKILL_REGISTRY.json`

**Review date:** 2026-03-28

### S2 — Skill Registry Mismatch

| | Count |
|---|---|
| Skills on disk (`ecosystem/skills/`) | 29 |
| Skills in registry | 28 |
| **Missing** | **1** |

**Missing Skill:** `dependabot-secretary`
- File exists: `ecosystem/skills/dependabot-secretary/SKILL.md` ✅
- In SKILL_REGISTRY.json: ❌ MISSING

**Impact:** Skill cannot be autos-discovered by the agent routing engine.

**Fix:** Add entry for `dependabot-secretary` to `brain/registry/SKILL_REGISTRY.json` with all required fields: `id`, `name`, `description`, `tier`, `category`, `status`, `path`.
```

---

## ISSUE 9 of 9

**Title:** `[MEDIUM][CLAUDE.md] Missing CLAUDE_CODE_TASKS.md + UTF-8 Encoding Corruption`

**Labels:** `bug`, `documentation`

**Body:**
```
## 🟡 Medium — `CLAUDE.md` + `.clauderules`

**Review date:** 2026-03-28

### S1 — Missing CLAUDE_CODE_TASKS.md

`CLAUDE.md` Step 9 requirements:
> ⚡ READ & AUTO-EXECUTE TASK QUEUE [CLAUDE_CODE_TASKS.md]

But this file **DOES NOT EXIST** in the repo.

Every boot → fallback mechanism triggers → warning logged → CEO needs notification.

**Fix:** Either:
1. Create `CLAUDE_CODE_TASKS.md` with an empty template (preferred)
2. Remove/comment out the reference in `CLAUDE.md` Step 9

---

### S4 — UTF-8 Encoding Corruption

**Affected files:** `CLAUDE.md`, `.clauderules`

Vietnamese/Unicode characters are garbled:
- `→` displays as `Ã¢â€â€™`
- `—` displays as `Ã¢â‚¬â€œ`
- `✅` corrupts into multi-byte garbage

**Cause:** Files saved with Windows-1252 or Latin-1 encoding, then re-read as UTF-8.

**Impact:** Boot protocols and governance rules can be misread by text tools (CI/CD, grep, diff tools).

**Fix:** Convert all entirely to UTF-8 without BOM:
```bash
# PowerShell
Get-Content CLAUDE.md -Encoding UTF8 | Set-Content CLAUDE.md -Encoding UTF8NoBOM
```
```

---

## SUMMARY

| # | File | Severity | Issues |
|---|------|----------|--------|
| 1 | `system/infra/api/server.js` | 🔴 Critical | CORS wildcard, no body limit, no rate limiting |
| 2 | `system/infra/api/server.js` | 🟠 High | Unvalidated file write, JSON parse no try-catch, manual YAML |
| 3 | `system/ops/scripts/batch_repo_intake.py` | 🟠 High | Bare except swallows all errors |
| 4 | `system/ops/scripts/omniclaw_integrate.py` | 🟠 High | Split crash, broken .env parser |
| 5 | `system/ops/scripts/sync_identity_1_1.js` | 🟠 High | Hardcoded `<OMNICLAW_ROOT>` placeholder |
| 6 | `system/ops/omniclaw_orchestrator.py` | 🟡 Medium | Silent LTM import failure |
| 7 | `system/automations/daemons/system_pulse.py` | 🟡 Medium | Telegram no validation |
| 8 | `brain/registry/SKILL_REGISTRY.json` | 🟡 Medium | dependabot-secretary unregistered |
| 9 | `CLAUDE.md` + `.clauderules` | 🟡 Medium | Missing boot file + UTF-8 corruption |

**Total:** 5 Critical, 6 High, 8 Medium issues
