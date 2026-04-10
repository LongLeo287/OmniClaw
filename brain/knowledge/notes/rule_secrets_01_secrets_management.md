---
id: rule-secrets-01-secrets-management
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.906179
---

# RULE-SECRETS-01 â€” Secrets Management Policy
**Issued:** 2026-03-31
**Status:** MANDATORY
**Owner:** strix-agent / security_grc
**Applies to:** ALL agents, ALL code, ALL commits

---

## Core Rule

**NEVER commit secrets, credentials, tokens, or API keys to git.**

Secrets = API keys, tokens, passwords, private keys, database URLs, webhook secrets, HQ master keys.

---

## Where Secrets Live

| Type | Location | Gitignored? |
|------|----------|-------------|
| All runtime secrets | `system/ops/secrets/MASTER.env` | YES |
| Local overrides | `.env` (root) | YES |
| Bridge token store | `brain/memory/vault_tokens.json` | YES |
| Keys directory | `system/ops/secrets/KEYS/` | YES |
| DPAPI backup | `system/ops/secrets/MASTER.env.dpapi` | YES |

**Rule:** Secrets ONLY go in the locations above. Nowhere else.

---

## Loading Secrets in Code

### Python
```python
import os
api_key = os.environ.get("MY_API_KEY")          # from env
# OR load from MASTER.env explicitly:
from dotenv import load_dotenv
load_dotenv(ROOT / "system" / "ops" / "secrets" / "MASTER.env")
```

### PowerShell
```powershell
# Dot-source the loader (resolves path dynamically):
$SecretsLoader = Join-Path $OMNICLAW_ROOT "system\ops\secrets\load-env.ps1"
if (Test-Path $SecretsLoader) { . $SecretsLoader }
# Keys now available as $env:MY_API_KEY
```

### BAT
```bat
:: Load MASTER.env (see open_port.bat pattern)
IF EXIST "%OMNICLAW_ROOT%\system\ops\secrets\MASTER.env" (
    FOR /F "usebackq tokens=1,* delims==" %%A IN ("%OMNICLAW_ROOT%\system\ops\secrets\MASTER.env") DO (
        IF NOT "%%A"=="" IF NOT "%%A:~0,1%"=="#" SET %%A=%%B
    )
)
```

---

## Anti-Patterns (FORBIDDEN)

```python
# BAD â€” hardcoded key
api_key = "sk-abc123..."

# BAD â€” hardcoded path on local machine
ENV_FILE = r"D:\LongLeo\OmniClaw\AI OS\system\ops\secrets\MASTER.env"

# GOOD â€” dynamic root + env var
ROOT = Path(os.environ.get("OMNICLAW_ROOT", str(Path(__file__).resolve().parents[N])))
api_key = os.environ.get("MY_API_KEY")
```

---

## Git Safety Rules

1. `.gitignore` covers ALL known secret locations (see canonical list below)
2. NEVER use `git add -A` or `git add .` without reviewing diff first
3. NEVER force-push if secrets were accidentally committed â€” instead revoke the key immediately
4. Template/example files (`.env.example`) are safe to commit â€” they must NOT contain real values

---

## Canonical Gitignore Entries (NEVER remove)

```
.env
system/ops/secrets/MASTER.env
system/ops/secrets/*.dpapi
system/ops/secrets/KEYS/
brain/memory/vault_tokens.json
*.pem *.key *.p12 *.pfx id_rsa id_ed25519 *.ppk
```

---

## If a Secret Is Leaked

1. **Immediately revoke/rotate** the leaked key on the provider platform
2. **Audit git history**: `git log --all --full-history -- .env`
3. **Remove from history** if necessary (git filter-repo or BFG)
4. **Notify CEO** via blackboard.json with severity=CRITICAL

---

## Responsible Agent

- **Primary:** `strix-agent` (security_grc) â€” scans for leaks on every scheduled run
- **Secondary:** `sec-agent` â€” auto-backup/sync validation
- **Escalation:** CEO (LongLeo) for any CRITICAL leak

---

*RULE-SECRETS-01 | OmniClaw Corp | 2026-03-31*

