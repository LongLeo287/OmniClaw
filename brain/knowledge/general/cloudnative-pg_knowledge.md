---
id: cloudnative-pg-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:07.214624
---

# KNOWLEDGE EXTRACT: cloudnative-pg
> **Extracted on:** 2026-03-30 17:34:26
> **Source:** cloudnative-pg

---

## File: `cloudnative-pg.md`
```markdown
# 📦 cloudnative-pg/cloudnative-pg [🔖 PENDING/APPROVE]
🔗 https://github.com/cloudnative-pg/cloudnative-pg
🌐 https://cloudnative-pg.io

## Meta
- **Stars:** ⭐ 8310 | **Forks:** 🍴 641
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
CloudNativePG is a comprehensive platform designed to seamlessly manage PostgreSQL databases within Kubernetes environments, covering the entire operational lifecycle from initial deployment to ongoing maintenance

## README (trích đầu)
```
[![CNCF Landscape](https://img.shields.io/badge/CNCF%20Landscape-5699C6)][cncf-landscape]
[![Latest Release](https://img.shields.io/github/v/release/cloudnative-pg/cloudnative-pg.svg)][latest-release]
[![GitHub License](https://img.shields.io/github/license/cloudnative-pg/cloudnative-pg)][license]
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/9933/badge)][openssf]
[![OpenSSF Baseline](https://www.bestpractices.dev/projects/9933/baseline)][openssf]
[![OpenSSF Scorecard Badge][openssf-scorecard-badge]][openssf-socrecard-view]
[![Documentation][documentation-badge]][documentation]
[![Stack Overflow](https://img.shields.io/badge/stackoverflow-cloudnative--pg-blue?logo=stackoverflow&logoColor=%23F48024&link=https%3A%2F%2Fstackoverflow.com%2Fquestions%2Ftagged%2Fcloudnative-pg)][stackoverflow]
[![FOSSA Status][fossa-badge]][fossa]
[![CLOMonitor](https://img.shields.io/endpoint?url=https://clomonitor.io/api/projects/cncf/cloudnative-pg/badge)](https://clomonitor.io/projects/cncf/cloudnative-pg)
[![Artifact Hub](https://img.shields.io/endpoint?url=https://artifacthub.io/badge/repository/cloudnative-pg)](https://artifacthub.io/packages/search?repo=cloudnative-pg)

# Welcome to the CloudNativePG Project!

**CloudNativePG (CNPG)** is an open-source platform designed to seamlessly
manage [PostgreSQL](https://www.postgresql.org/) databases in Kubernetes
environments. It covers the entire operational lifecycle—from deployment to
ongoing maintenance—through its core component, the CloudNativePG operator.

## Table of Contents

- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Governance Policies](https://github.com/cloudnative-pg/governance/blob/main/GOVERNANCE.md)
- [Contributing](CONTRIBUTING.md)
- [Adopters](ADOPTERS.md)
- [Commercial Support](https://cloudnative-pg.io/support/)
- [License](LICENSE)

## Getting Started

The best way to get started is the [Quickstart Guide](https://cloudnative-pg.io/brain/knowledge/docs_legacy/devel/quickstart/).

## Scope

### Mission

CloudNativePG aims to increase PostgreSQL adoption within Kubernetes by making
it an integral part of the development process and GitOps-driven CI/CD
automation.

### Core Principles & Features

Designed by PostgreSQL experts for Kubernetes administrators, CloudNativePG
follows a Kubernetes-native approach to PostgreSQL primary/standby cluster
management. Instead of relying on external high-availability tools (like
Patroni, repmgr, or Stolon), it integrates directly with the Kubernetes API to
automate database operations that a skilled DBA would perform manually.

Key design decisions include:

- Direct integration with Kubernetes API: The PostgreSQL cluster’s status is
  available directly in the `Cluster` resource, allowing users to inspect it
  via the Kubernetes API.
- Operator pattern: The operator ensures that the desired PostgreSQL state is
  reconciled automatically, following Kubernetes best practices.
- Immutable application containers: Updates follow an immutable infrastructure
  model, as ex
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

