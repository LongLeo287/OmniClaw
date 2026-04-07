---
id: "osf_monitoring"
name: "OSF Warden Toolchain"
version: "2.0.0"
tier: 1
status: "active"
description: "Core scripts to enforce the OmniClaw Sandbox Framework (OSF). Ensures path isolation, file integrity locks, and malicious payload scanning."
domain: "security"
cost_tier: "economy"
category: "system_integrity"
accessible_by:
  - "osf_warden"
  - "osf_auditor"
  - "osf_quarantine_guard"
  - "Orchestrator"
dependencies:
  - "context_manager"
exposed_functions:
  - name: "run_sandbox_audit"
  - name: "fix_sandbox_breaches"
  - name: "lock_core_files"
  - name: "censor_malware_quarantine"
tags:
  - "osf"
  - "security"
  - "sandbox"
  - "malware"
---

## Tool 1: oma_sandbox_auditor.py
Runs a deep scan across `core` to find hardcoded external drives (`C:\`, `D:\tmp`).
`python core/ops/scripts/oma_sandbox_auditor.py`

## Tool 2: oma_sandbox_fixer.py
Patches any breaches found by replacing absolute paths with OmniClaw dynamic paths.
`python core/ops/scripts/oma_sandbox_fixer.py`

## Tool 3: osf_file_locker.py
Freezes structural hierarchy into Read-Only state. Use `--unlock` to reverse.
`python core/ops/scripts/osf_file_locker.py`

## Tool 4: osf_malware_censor.py
Scans `vault/quarantine` for structural anomalies (Reverse shells, B64 obfuscation).
`python core/ops/scripts/osf_malware_censor.py`
