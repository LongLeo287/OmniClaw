---
id: citusdata-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:02.030375
---

# KNOWLEDGE EXTRACT: citusdata
> **Extracted on:** 2026-03-30 17:31:18
> **Source:** citusdata

---

## File: `citus.md`
```markdown
# 📦 citusdata/citus [🔖 PENDING/APPROVE]
🔗 https://github.com/citusdata/citus
🌐 https://www.citusdata.com

## Meta
- **Stars:** ⭐ 12398 | **Forks:** 🍴 759
- **Language:** C | **License:** AGPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Distributed PostgreSQL as an extension

## README (trích đầu)
```
| **<br/>The Citus database is 100% open source.<br/><img width=1000/><br/>Learn what's new in the [Citus 13.0 release blog](https://www.citusdata.com/blog/2025/02/06/distribute-postgresql-17-with-citus-13/) and the [Citus Updates page](https://www.citusdata.com/updates/).<br/><br/>**|
|---|
<br/>



![Citus Banner](images/citus-readme-banner.png)

[![Latest Docs](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://docs.citusdata.com/)
[![Stack Overflow](https://img.shields.io/badge/Stack%20Overflow-%20-545353?logo=Stack%20Overflow)](https://stackoverflow.com/questions/tagged/citus)
[![Slack](https://cituscdn.azureedge.net/images/social/slack-badge.svg)](https://slack.citusdata.com/)
[![Code Coverage](https://codecov.io/gh/citusdata/citus/branch/master/graph/badge.svg)](https://app.codecov.io/gh/citusdata/citus)
[![Twitter](https://img.shields.io/twitter/follow/citusdata.svg?label=Follow%20@citusdata)](https://twitter.com/intent/follow?screen_name=citusdata)

[![Citus Deb Packages](https://img.shields.io/badge/deb-packagecloud.io-844fec.svg)](https://packagecloud.io/app/citusdata/community/search?q=&filter=debs)
[![Citus Rpm Packages](https://img.shields.io/badge/rpm-packagecloud.io-844fec.svg)](https://packagecloud.io/app/citusdata/community/search?q=&filter=rpms)

## What is Citus?

Citus is a [PostgreSQL extension](https://www.citusdata.com/blog/2017/10/25/what-it-means-to-be-a-postgresql-extension/) that transforms Postgres into a distributed database—so you can achieve high performance at any scale.

With Citus, you extend your PostgreSQL database with new superpowers:

- **Distributed tables** are sharded across a cluster of PostgreSQL nodes to combine their CPU, memory, storage and I/O capacity.
- **References tables** are replicated to all nodes for joins and foreign keys from distributed tables and maximum read performance.
- **Distributed query engine** routes and parallelizes SELECT, DML, and other operations on distributed tables across the cluster.
- **Columnar storage** compresses data, speeds up scans, and supports fast projections, both on regular and distributed tables.
- **Query from any node** enables you to utilize the full capacity of your cluster for distributed queries

You can use these Citus superpowers to make your Postgres database scale-out ready on a single Citus node. Or you can build a large cluster capable of handling **high transaction throughputs**, especially in **multi-tenant apps**, run **fast analytical queries**, and process large amounts of **time series** or **IoT data** for **real-time analytics**. When your data size and volume grow, you can easily add more worker nodes to the cluster and rebalance the shards.

Our [SIGMOD '21](https://2021.sigmod.org/) paper [Citus: Distributed PostgreSQL for Data-Intensive Applications](https://doi.org/10.1145/3448016.3457551) gives a more detailed look into what Citus is, how it works, and why it works that way.

![Citus scales out from a single node](i
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

