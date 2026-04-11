---
id: data-packaging-sync
type: document
owner: SYSTEM
tags: [deployment, sync]
---

# Packaging & Sync Workflow (Cloud Push Process)

[**🇻🇳 Vietnamese Translation**](data_packaging_sync_vn.md) | [**Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

This document describes deployment-specific state backup and sync policy. It is not part of the baseline public bootstrap path for a fresh OmniClaw clone.

---

## 1. Scope
The public OmniClaw core repository is intentionally lighter than a full private deployment. Large state, caches, and external datasets may exist outside GitHub and may require deployment-specific tooling.

Typical large-state zones include:
1. `brain/memory/`
2. `vault/`
3. `ecosystem/plugins/`

> **Warning:** Never force push raw database files, private state, or large archives directly to `main`.

---

## 2. Public Repository Rule
Bootstrap the core repository first with `omniclaw doctor`. Provision any external state intentionally for the target environment. Do not assume a fresh public clone includes private memory, private datasets, or cloud credentials.

> **Important:** Any deployment-specific commands further below should be treated as legacy internal examples unless they are explicitly validated for your environment.

---

## 3. Backup Soul Process (Session Packaging)
Before any GitHub code commits, system rules mandate backing up the "active session soul" of the Operator's current chat.

**Execution Script:**
```bash
powershell -ExecutionPolicy Bypass -File system\ops\scripts\memory\backup_soul.ps1
```

**Workflow:**
1. It copies the precise `.pb` file reflecting the most recent Agent conversation session.
2. It vacuums up all internal logic stored inside the `brain/` folder bound to that UUID.
3. This massive payload is tightly compressed into an airtight Zip file named: `soul_backup.zip`.
4. Once sealing completes, the file securely docks inside a protected local buffer zone. Only then is the Operator empowered to push the final Git Commit.

---

## 3. Automated CI/CD Gates (GitHub Actions)
The moment the Operator runs a **Git Push** command syncing code to the `main` branch, the cloud awakens two dedicated GitHub Actions C.I. workflow guardians:

- **`.github/workflows/omniclaw-tests.yml`:** Continuously checks for python syntax violations (`.py`, `.js`), whilst ensuring changes to expanding components and the newly integrated `docs/` module won't trigger engine crashes.
- **`.github/workflows/omniclaw-validate.yml`:** Scans through critical architectural metadata like the `SKILL_REGISTRY.json` and agent YAML configurations. It ensures every new Skill independently coded by A.I. meets perfect configuration syntax without duplicate IDs or corrupt JSON mapping rules.

---

Every Data Packaging and Git Push procedure must abide by this strict architecture. OmniClaw System Integrity is inviolable.

