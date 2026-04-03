---
id: kobotoolbox-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:01.573370
---

# KNOWLEDGE EXTRACT: kobotoolbox
> **Extracted on:** 2026-03-30 17:38:56
> **Source:** kobotoolbox

---

## File: `kpi.md`
```markdown
# 📦 kobotoolbox/kpi [🔖 PENDING/APPROVE]
🔗 https://github.com/kobotoolbox/kpi
🌐 https://www.kobotoolbox.org

## Meta
- **Stars:** ⭐ 170 | **Forks:** 🍴 214
- **Language:** Python | **License:** AGPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
kpi is the server for KoboToolbox. It includes an API for users to access data and manage their forms, question library, sharing settings, create reports, and export data. 

## README (trích đầu)
```
# KPI

[![Python Build Status](https://github.com/kobotoolbox/kpi/actions/workflows/pytest.yml/badge.svg?branch=main)](https://github.com/kobotoolbox/kpi/actions?query=workflow%3Apytest+branch%3Amain)
[![Python Coverage Status](https://coveralls.io/repos/github/kobotoolbox/kpi/badge.svg?branch=main)](https://coveralls.io/github/kobotoolbox/kpi?branch=main)
[![JavaScript Build Status](https://github.com/kobotoolbox/kpi/actions/workflows/npm-test.yml/badge.svg?branch=main)](https://github.com/kobotoolbox/kpi/actions?query=workflow%3Anpm-test+branch%3Amain)

For production always use a specific release branch, `main` branch may include breaking changes. Run `git branch -rl 'origin/release/*'` to list release branches and then switch to a release branch of your choice.

We're open for [contributions](./CONTRIBUTING.md)!

## API Deprecation & Removal Notices

Please refer to the following documents for important information about deprecated or removed API endpoints:

[DEPRECATION.md](./DEPRECATION.md) — Lists all API endpoints that are deprecated.

[REMOVALS.md](./REMOVALS.md) — Documents API endpoints that have already been removed.

We recommend reviewing these files regularly to ensure your integrations remain compatible with future versions of the API.

## Important notice when upgrading from any release older than [`2.024.19`](https://github.com/kobotoolbox/kpi/releases/tag/2.024.19)

Prior to release [`2.024.19`](https://github.com/kobotoolbox/kpi/releases/tag/2.024.19), this project (KPI) and [KoboCAT](https://github.com/kobotoolbox/kobocat) were two separated projects.
KoboCAT is now part of KPI code base and its repository has been archived.

KoboCAT deprecation notices will be maintained in this repository.
[More details here](../../../README.md)

## Important notice when upgrading from any release older than [`2.020.18`](https://github.com/kobotoolbox/kpi/releases/tag/2.020.18)

Prior to release [`2.020.18`](https://github.com/kobotoolbox/kpi/releases/tag/2.020.18), this project (KPI) and [KoboCAT](https://github.com/kobotoolbox/kobocat) both shared a common Postgres database. They now each have their own. **If you are upgrading an existing single-database installation, you must follow [these instructions](https://community.kobotoolbox.org/t/upgrading-to-separate-databases-for-kpi-and-kobocat/7202)** to migrate the KPI tables to a new database and adjust your configuration appropriately.

If you do not want to upgrade at this time, please use the [`shared-database-obsolete`](https://github.com/kobotoolbox/kpi/tree/shared-database-obsolete) branch instead.

## Python Dependencies

Python dependencies are managed with `pip-compile` and `pip-sync` from the [`pip-tools`](https://github.com/jazzband/pip-tools/) package. The dependencies are listed in [`dependencies/pip/`](./dependencies/pip/), with core requirements in [`dependencies/pip/requirements.in`](./dependencies/pip/requirements.in). You may use `pip` directly with one of the
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

