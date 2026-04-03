# system/ops/secrets — OmniClaw Secrets Management

## Directory Structure

```
system/ops/secrets/
├── MASTER.env          <- Single source of truth for all API keys (gitignored)
├── MASTER.env.dpapi    <- DPAPI-encrypted backup (gitignored)
├── MASTER.env.example  <- Template with no real keys (safe to commit)
├── encrypt.ps1         <- Encrypt MASTER.env -> MASTER.env.dpapi
├── decrypt.ps1         <- Decrypt + load into $env:*
├── load-env.ps1        <- Utility for other scripts to import
└── README.md           <- This file
```

---

## Basic Workflow

### Initial setup:
```powershell
# Fill in keys in MASTER.env, then encrypt:
.\system\ops\secrets\encrypt.ps1
```

### Adding or updating a key:
```powershell
# 1. Edit MASTER.env (plaintext)
# 2. Re-run encrypt to update .dpapi
.\system\ops\secrets\encrypt.ps1
```

### Load secrets into terminal:
```powershell
# Dot-source to load into current session:
. .\system\ops\secrets\load-env.ps1

# Verify:
echo $env:TELEGRAM_BOT_TOKEN
```

### Use in another PowerShell script:
```powershell
# At the top of any script, before using any key:
$OMNICLAW_ROOT = if ($env:OMNICLAW_ROOT) { $env:OMNICLAW_ROOT } else {
    (Resolve-Path (Join-Path $PSScriptRoot ".." ".." "..")).Path
}
$SecretsLoader = Join-Path $OMNICLAW_ROOT "system\ops\secrets\load-env.ps1"
if (Test-Path $SecretsLoader) { . $SecretsLoader }

# Then use directly:
$token = $env:TELEGRAM_BOT_TOKEN
```

---

## Security Mechanisms

| Mechanism | Description |
|-----------|-------------|
| **DPAPI** | Windows user-level encryption. Only the encrypting user can decrypt. |
| **.gitignore** | `MASTER.env` and `*.dpapi` are never committed to git. |
| **Scope** | `CurrentUser` — not shareable even on the same machine by another user. |

> WARNING: MASTER.env.dpapi is NOT portable — cannot be copied to another machine and decrypted.
> On a new machine, re-enter keys into a fresh MASTER.env on that machine.

---

## Policy Reference

See: `brain/knowledge/notes/RULE-SECRETS-01-secrets-management.md`
