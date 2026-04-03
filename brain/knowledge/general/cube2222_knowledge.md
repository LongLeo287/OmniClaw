---
id: cube2222-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.061844
---

# KNOWLEDGE EXTRACT: cube2222
> **Extracted on:** 2026-03-30 17:35:41
> **Source:** cube2222

---

## File: `octosql.md`
```markdown
# 📦 cube2222/octosql [🔖 PENDING/APPROVE]
🔗 https://github.com/cube2222/octosql


## Meta
- **Stars:** ⭐ 5247 | **Forks:** 🍴 214
- **Language:** Go | **License:** MPL-2.0
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OctoSQL is a query tool that allows you to join, analyse and transform data from multiple databases and file formats using SQL.

## README (trích đầu)
```
<img src="https://raw.githubusercontent.com/cube2222/octosql/main/images/logo.png" width="168">OctoSQL
=======

OctoSQL is predominantly a CLI tool which lets you query a plethora of databases and file formats using SQL through a unified interface, even do JOINs between them. (Ever needed to join a JSON file with a PostgreSQL table? OctoSQL can help you with that.)

At the same time it's an easily extensible full-blown dataflow engine, and you can use it to add a SQL interface to your own applications.

[![GitHub](https://shields.io/github/actions/workflow/status/cube2222/octosql/test.yml?branch=main)](https://github.com/cube2222/octosql/actions/workflows/test.yml?query=branch%3Amain)
[![Go Report Card](https://goreportcard.com/badge/github.com/cube2222/octosql)](https://goreportcard.com/report/github.com/cube2222/octosql)
[![GoDoc](https://godoc.org/github.com/cube2222/octosql?status.svg)](https://godoc.org/github.com/cube2222/octosql)
[![License](https://shields.io/github/license/cube2222/octosql)](LICENSE)
[![Latest Version](https://shields.io/github/v/release/cube2222/octosql?display_name=tag&sort=semver)](https://github.com/cube2222/octosql/releases)
[![Gitter](https://badges.gitter.im/octosql/general.svg)](https://gitter.im/octosql/general?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

![Demo](images/octosql-demo.gif)

## Usage

```bash
octosql "SELECT * FROM ./myfile.json"
octosql "SELECT * FROM ./myfile.json" --describe  # Show the schema of the file.
octosql "SELECT invoices.id, address, amount
         FROM invoices.csv JOIN db.customers ON invoices.customer_id = customers.id
         ORDER BY amount DESC"
octosql "SELECT customer_id, SUM(amount)
         FROM invoices.csv
         GROUP BY customer_id"
```

OctoSQL supports a [bunch of file formats](#File-Access) out of the box, but you can additionally install plugins to add support for other databases.
```bash
octosql "SELECT * FROM plugins.available_plugins"
octosql plugin install postgres
echo "databases:
  - name: mydb
    type: postgres
    config:
      host: localhost
      port: 5443
      database: mydb
      user: postgres
      password: postgres" > octosql.yml
octosql "SELECT * FROM mydb.users" --describe
octosql "SELECT * FROM mydb.users"
```

You can specify the output format using the `--output` flag. Available values for it are `live_table`, `batch_table`, `csv` and `stream_native`.

The documentation about available aggregates and functions is contained within OctoSQL itself. It's in the `aggregates`, `aggregate_signatures`, `functions` and `function_signatures` tables in the `docs` database.
```bash
octosql "SELECT * FROM docs.functions fs"
+------------------+----------------------------------------+
|     fs.name      |             fs.description             |
+------------------+----------------------------------------+
| 'abs'            | 'Returns absolute value                |
|                  | of argument.'                          |
| 'ceil'   
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

