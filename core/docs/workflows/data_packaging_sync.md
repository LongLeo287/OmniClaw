---
id: data-packaging-sync
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:44:27.671754
---

# Packaging & Sync Workflow (Cloud Push Process)

[**🇻🇳 Xem Bản Tiếng Việt**](data_packaging_sync-vn.md) | [**Wiki Reference**](https://github.com/LongLeo287/OmniClaw/wiki)

---

This is the end-to-end workflow for backing up and packaging the entire Brain, State, and Memory of OmniClaw to simultaneously sync it to three cloud hubs: **HuggingFace**, **Google Drive**, and **GitHub**. Strict adherence to this workflow ensures no broken paths or large file constraint errors (Git LFS limit).

---

## 1. Targeted Data Push (The Cloud Sniper)
To prevent bloating the standard Git repository or flooding it with unnecessary junk folders, the system prioritizes "Targeted Data Sync" rather than a full root copy.

The core script handling this data vault operation is:
**`system/ops/scripts/omniclaw_data_push.py`** 

It intelligently extracts and pushes the three heaviest system directories:
1. `brain/memory/` (Long-term Agent Experience Memory)
2. `storage/vault/` (Library of Raw Extracted Data and Media Assets)
3. `ecosystem/plugins/` (Third-Party Repositories and Agent Source Code)

These large assets securely stream into the primary **HuggingFace Dataset** and **Google Drive** Vault.

> **⚠️ Warning:** Never force push raw database files (`.db`, `.sqlite`, `.webp`) or massive archival repositories (exceeding > 100MB) directly to the root GitHub branch (`main`). Doing so violates GitHub's LFS limit and will trigger a "pre-receive hook declined" failure.

---

## 2. Targeted Data Pull (Rehydrating the Vault)
Whenever a developer forks or clones OmniClaw from Github, their `storage/vault` and `brain/memory` will likely be empty.
To seamlessly redownload the missing heavy files straight into their correct local paths, run:
**`python system/ops/scripts/omniclaw_data_pull.py`**

This script utilizes HuggingFace's `snapshot_download` and RClone `copy` to **exactly match and rehydrate** the original directory structures (`d:/LongLeo/OmniClaw CORP/OmniClaw/storage/...`). Links will not break, and all Agents will instantly recognize the memory structures.

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

