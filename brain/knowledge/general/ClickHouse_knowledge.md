---
id: clickhouse-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:06.526950
---

# KNOWLEDGE EXTRACT: ClickHouse
> **Extracted on:** 2026-03-30 17:34:25
> **Source:** ClickHouse

---

## File: `agent-skills.md`
```markdown
# 📦 ClickHouse/agent-skills [🔖 PENDING/APPROVE]
🔗 https://github.com/ClickHouse/agent-skills
🌐 https://clickhouse.ai

## Meta
- **Stars:** ⭐ 373 | **Forks:** 🍴 17
- **Language:** JavaScript | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
The official Agent Skills for ClickHouse and ClickHouse Cloud

## README (trích đầu)
```
# ClickHouse Agent Skills

The official Agent Skills for [ClickHouse](https://clickhouse.com/). These skills help LLMs and agents to adopt best practices when working with ClickHouse.

You can use these skills with open-source ClickHouse and managed ClickHouse Cloud. [Try ClickHouse Cloud with $300 in free credits](https://clickhouse.com/cloud?utm_medium=github&utm_source=github&utm_ref=agent-skills).

## Installation

```bash
npx skills add clickhouse/agent-skills
```

The CLI auto-detects installed agents and prompts you to select where to install.

## What is this?

Agent Skills are packaged instructions that extend AI coding agents (Claude Code, Cursor, Copilot, etc.) with domain-specific expertise. This repository provides skills for ClickHouse databases—covering schema design, query optimization, and data ingestion patterns.

When an agent loads these skills, it gains knowledge of ClickHouse best practices and can apply them while helping you design tables, write queries, or troubleshoot performance issues.

Skills follow the open specification at [agentskills.io](https://agentskills.io).

## Available Skills

### ClickHouse Best Practices

**28 rules** covering schema design, query optimization, and data ingestion—prioritized by impact.

| Category | Rules | Impact |
|----------|-------|--------|
| Primary Key Selection | 4 | CRITICAL |
| Data Type Selection | 5 | CRITICAL |
| JOIN Optimization | 5 | CRITICAL |
| Insert Batching | 1 | CRITICAL |
| Mutation Avoidance | 2 | CRITICAL |
| Partitioning Strategy | 4 | HIGH |
| Skipping Indices | 1 | HIGH |
| Materialized Views | 2 | HIGH |
| Async Inserts | 2 | HIGH |
| OPTIMIZE Avoidance | 1 | HIGH |
| JSON Usage | 1 | MEDIUM |

**Location:** [`skills/clickhouse-best-practices/`](./skills/clickhouse-best-practices/)

**For humans:** Read [SKILL.md](../../../.claude/skills/supabase-postgres-best-practices/SKILL.md) for an overview, or [AGENTS.md](../../../.claude/skills/supabase-postgres-best-practices/AGENTS.md) for the complete compiled guide.

**For agents:** The skill activates automatically when you work with ClickHouse—creating tables, writing queries, or designing data pipelines.

## Quick Start

After installation, your AI agent will reference these best practices when:

- Creating new tables with `CREATE TABLE`
- Choosing `ORDER BY` / `PRIMARY KEY` columns
- Selecting data types for columns
- Optimizing slow queries
- Writing or tuning JOINs
- Designing data ingestion pipelines
- Handling updates or deletes

Example prompt:
> "Create a table for storing user events with fields for user_id, event_type, properties (JSON), and timestamp"

The agent will apply relevant rules like proper column ordering in the primary key, appropriate data types, and partitioning strategy.

## Supported Agents

Skills are **agent-agnostic**—the same skill works across all supported AI coding assistants:

| Agent | Config Directory |
|-------|------------------|
| [Claude Code](https://claude.ai/code) | `.claude/skills/` |
| [Cursor](https://cursor.sh)
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `clickhouse-go.md`
```markdown
# 📦 ClickHouse/clickhouse-go [🔖 PENDING/APPROVE]
🔗 https://github.com/ClickHouse/clickhouse-go


## Meta
- **Stars:** ⭐ 3258 | **Forks:** 🍴 641
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Golang driver for ClickHouse

## README (trích đầu)
```
# ClickHouse [![run-tests](https://github.com/ClickHouse/clickhouse-go/actions/workflows/run-tests.yml/badge.svg?branch=v2)](https://github.com/ClickHouse/clickhouse-go/actions/workflows/run-tests.yml) [![Go Reference](https://pkg.go.dev/badge/github.com/ClickHouse/clickhouse-go/v2.svg)](https://pkg.go.dev/github.com/ClickHouse/clickhouse-go/v2)

Golang SQL database client for [ClickHouse](https://clickhouse.com/).

## Key features

* Uses ClickHouse native format for optimal performance. Utilises low level [ch-go](https://github.com/ClickHouse/ch-go) client for encoding/decoding and compression (versions >= 2.3.0).
* Supports both native ClickHouse TCP and HTTP client-server protocols
* Compatibility with [`database/sql`](#std-databasesql-interface) ([slower](#benchmark) than [native interface](#native-interface)!)
* [`database/sql`](#std-databasesql-interface) supports both native TCP and HTTP protocols for transport.
* Marshal rows into structs ([ScanStruct](examples/clickhouse_api/scan_struct.go), [Select](examples/clickhouse_api/select_struct.go))
* Unmarshal struct to row ([AppendStruct](benchmark/v2/write-native-struct/main.go))
* Connection pool (for both TCP-Native and HTTP)
* Failover and load balancing
* [Bulk write support](examples/clickhouse_api/batch.go) (for `database/sql` [use](examples/std/batch.go) `begin->prepare->(in loop exec)->commit`)
* [PrepareBatch options](#preparebatch-options)
* [AsyncInsert](benchmark/v2/write-async/main.go) (more details in [Async insert](#async-insert) section)
* Named and numeric placeholders support
* LZ4/ZSTD/LZ4HC/GZIP/Deflate/Brotli compression support
* External data
* [Query parameters](examples/std/query_parameters.go)
* Structured logging via `log/slog` ([Logger option](#logging))
* JWT authentication support
* Wide type support: BFloat16, QBit, Dynamic, Variant, Time, Time64, LineString, MultiLineString, and more

Support for the ClickHouse protocol advanced features using `Context`:

* Query ID
* Quota Key
* Settings
* [Query parameters](examples/clickhouse_api/query_parameters.go)
* OpenTelemetry
* Execution events:
	* Logs
	* Progress
	* Profile info
	* Profile events


## Supported ClickHouse Versions

The client is tested against the currently [supported versions](https://github.com/ClickHouse/ClickHouse/blob/master/SECURITY.md) of ClickHouse

## Supported Golang Versions

| Client Version | Golang Versions        |
|----------------|------------------------|
| => 2.0 <= 2.2  | 1.17, 1.18             |
| >= 2.3         | 1.18.4+, 1.19          |
| >= 2.14        | 1.20, 1.21             |
| >= 2.19        | 1.21, 1.22             |
| >= 2.28        | 1.22, 1.23             |
| >= 2.29        | 1.21, 1.22, 1.23, 1.24 |
| >= 2.41        | 1.24, 1.25             |

## Documentation

[https://clickhouse.com/brain/knowledge/docs_legacy/en/integrations/go](https://clickhouse.com/brain/knowledge/docs_legacy/en/integrations/go)

# `clickhouse` interface (formerly `native` interface)

```go
	conn, err := clickhouse.Open(&clickhouse.Optio
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

