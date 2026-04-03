---
name: secret-scanner
description: Token/Password leak scanner for Strix Security department
---
# Lifesaver Weapon: Secret Scanner

Based on the super architecture of **Trufflehog**, this is a specialized skill ONLY FOR `strix-agent` (Dept 10) or `security-auditor`. Any other agent is prohibited from secretly scanning without C-Suite orders.

## Mission Definition (The Core Directives)
- Brutal Scan: Dig through every line of `.env`, `.yml`, `.json`, `*.py` of every target passed.
- Search for high-sensitivity patterns: `sk-...` (Stripe/OpenAI), `ghp_...` (Github PAT), `xoxb-...` (Slack), `AKIA...` (AWS), JSON garbage containing Regex of Private Keys (`-----BEGIN PRIVATE KEY-----`).

## Storm Workflow
1. Activate `secret_scanner`, report target directory coordinates.
2. It will Regex Matching all files in Target (Including Commit History if needed).
3. RED Alert: Immediately log to `QUARANTINE_REJECTED` if found, EVEN IF ONLY IN COMMENT. Trigger isolation of that repo immediately, no mercy.
4. NEVER print that key/token to the Leader Boss's Chat screen. Only allowed to log: `Cut the life of Repo abc because detected OpenAI key leaked in file script.py`.

## Tool Usage
The Python Core system has built-in blocking Regex functions by default. Agents carrying this skill have the right to refuse merging Knowledge and immediately block Engineer (Dept 01) Workflow.
