---
name: secret-scanner
description: Scans codebase for accidentally committed secrets, API keys, tokens, passwords, and credentials. Primary tool for strix-agent security monitoring.
owner: strix-agent
department: security_grc
---

# Secret Scanner — Credentials Leak Detector

## What it Does
Scans files and git history for leaked secrets: API keys, tokens, passwords, private keys, database URLs.
Complements `.gitignore` enforcement with runtime detection.

## When to Use
- Before any `git push` or PR creation
- Periodic scan (weekly via strix-agent)
- When `RULE-SECRETS-01` violation is suspected
- After onboarding a new developer or agent

## Detection Patterns

### API Key Patterns
```
sk-[a-zA-Z0-9]{20,}          # OpenAI
gsk_[a-zA-Z0-9]{50,}         # Groq
github_pat_[a-zA-Z0-9_]{50,} # GitHub PAT
AIza[0-9A-Za-z_-]{35}        # Google API
AKIA[0-9A-Z]{16}              # AWS Access Key
xoxb-[0-9]+-[a-zA-Z0-9]+     # Slack Bot Token
```

### Generic Patterns
```
password\s*=\s*["'][^"']{6,}  # password=
api_key\s*=\s*["'][^"']{10,}  # api_key=
secret\s*=\s*["'][^"']{6,}    # secret=
Bearer\s+[a-zA-Z0-9._-]{20,}  # Bearer tokens
-----BEGIN.*PRIVATE KEY-----   # PEM keys
```

## Scan Procedure (Claude Code Native)

### Step 1: Scan staged files before commit
```bash
git diff --cached --name-only | xargs grep -E "sk-|gsk_|github_pat_|password\s*=|api_key\s*="
```

### Step 2: Scan all Python/PS1 files
```bash
grep -rn --include="*.py" --include="*.ps1" -E "(api_key|password|secret|token)\s*=\s*['\"][^'\"]{8,}" . --exclude-dir=.git
```

### Step 3: Check gitignore coverage
```bash
git check-ignore -v system/ops/secrets/MASTER.env
git check-ignore -v .env
git check-ignore -v brain/shared-context/vault_tokens.json
```

### Step 4: Git history scan
```bash
git log --all --full-history --oneline -- .env system/ops/secrets/MASTER.env
```

## Response Protocol (strix-agent)

| Severity | Trigger | Action |
|----------|---------|--------|
| CRITICAL | Real key found in tracked file | Immediately report to CEO + block push |
| HIGH | Key found in staged but not committed | Remove from staging, add to .gitignore |
| MEDIUM | Key in untracked file not gitignored | Add pattern to .gitignore |
| LOW | Suspicious pattern (false positive likely) | Log to security audit report |

## Output Format
```
[SECRET-SCANNER] Date: YYYY-MM-DD
Status: CLEAN / VIOLATION_FOUND
Files_scanned: N
Violations: []
Action_taken: none / blocked_commit / rotated_key
Next_scan: (date)
```
