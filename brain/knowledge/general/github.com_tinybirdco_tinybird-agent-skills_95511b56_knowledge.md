---
id: github.com-tinybirdco-tinybird-agent-skills-95511b
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.920765
---

# KNOWLEDGE EXTRACT: github.com_tinybirdco_tinybird-agent-skills_95511b56
> **Extracted on:** 2026-04-01 16:20:38
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525053/github.com_tinybirdco_tinybird-agent-skills_95511b56

---

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Tinybird Agent Skills

Welcome to the Tinybird Agent Skills project! 🐦

## Quick Links
- **GitHub:** https://github.com/tinybirdco/tinybird-agent-skills
- **Slack Community:** https://www.tinybird.co/community
- **X/Twitter:** [@tinybird](https://x.com/tinybird)
- **Documentation:** https://www.tinybird.co/docs

## How to Contribute
1. **Bugs & small fixes** → Open a PR!
2. **New features / architecture** → Start a [GitHub Discussion](https://github.com/tinybirdco/tinybird-agent-skills/discussions) or ask in Slack first
3. **Questions** → Slack community

## Before You PR
- Test locally
- Keep PRs focused (one thing per PR)
- Describe what & why

## AI/Vibe-Coded PRs Welcome! 🤖

Built with Codex, Claude, or other AI tools? **Awesome - just mark it!**

Please include in your PR:
- [ ] Mark as AI-assisted in the PR title or description
- [ ] Note the degree of testing (untested / lightly tested / fully tested)
- [ ] Include prompts or session logs if possible (super helpful!)
- [ ] Confirm you understand what the code does

AI PRs are first-class citizens here. We just want transparency so reviewers know what to look for.
```

## File: `README.md`
```markdown
# Tinybird Agent Skills

A collection of skills for AI coding agents. Skills are packaged instructions that extend agent capabilities for working with Tinybird.

Skills follow the [Agent Skills](https://agentskills.io/) format.

Install with

```bash
npx skills add tinybirdco/tinybird-agent-skills
```

Update with

```bash
npx skills update
```

## Available Skills

### Core project skills

Use these for day-to-day Tinybird project work. They are safe defaults to keep enabled.

#### tinybird-best-practices

Tinybird project guidelines from Tinybird Engineering. Contains 18 rule files covering datasources, pipes, endpoints, SQL, deployments, and testing.

**Use when:**
- Creating or updating Tinybird resources (.datasource, .pipe, .connection)
- Working with queries, endpoints, or data exploration
- Managing Tinybird deployments, secrets, or tests
- Reviewing or refactoring Tinybird project files

**Categories covered:**
- Project structure and local development
- Datasource, pipe, and endpoint files
- SQL and query optimization
- Build and deploy workflows
- Testing and secrets management

### CLI workflow skills

Use these when operating Tinybird with the CLI (local dev, deployments, data ops) and the datafile (.pipe, .connection, .datasource) format

#### tinybird-cli-guidelines

Tinybird CLI commands, workflows, and operations. Use when running `tb` commands, managing local development, deploying, or working with data operations.

**Use when:**
- Running any `tb` command
- Local development with Tinybird Local
- Building and deploying projects
- Appending, replacing, or deleting data
- Managing tokens and secrets via CLI
- Generating mock data
- Running tests

### TypeScript SDK skills

Use these when working with the `@tinybirdco/sdk` package and type-safe projects.

#### tinybird-typescript-sdk-guidelines

Tinybird TypeScript SDK for defining datasources, pipes, and queries with full type inference. Use when working with @tinybirdco/sdk, TypeScript Tinybird projects, or type-safe data ingestion and queries.

**Use when:**
- Installing or configuring @tinybirdco/sdk
- Defining datasources or pipes in TypeScript
- Creating typed Tinybird clients
- Using type-safe ingestion or queries
- Running tinybird dev/build/deploy commands for TypeScript projects
- Migrating from legacy .datasource/.pipe files to TypeScript

### Python SDK skills

Use these when working with the `tinybird-sdk` package and Python projects.

#### tinybird-python-sdk-guidelines

Tinybird Python SDK for defining datasources, pipes, and queries in Python. Use when working with tinybird-sdk, Python Tinybird projects, or data ingestion and queries in Python.

**Use when:**
- Installing or configuring tinybird-sdk
- Defining datasources, pipes, or endpoints in Python
- Creating Tinybird clients in Python
- Using data ingestion or queries in Python
- Running tinybird dev/build/deploy commands for Python projects
- Migrating from legacy .datasource/.pipe files to Python
- Defining connections (Kafka, S3, GCS)
- Creating materialized views, copy pipes, or sink pipes

## Usage

Skills are automatically available once installed. The agent will use them when relevant tasks are detected. You can use the agent cli to check, e.g., `amp skill list`, or directly ask the agent to tell you what skills are available.

**Recommended defaults:**
- Always enable `tinybird-best-practices` for general Tinybird project work.
- Add `tinybird-cli-guidelines` whenever you plan to run `tb` commands.
- Add `tinybird-typescript-sdk-guidelines` for TypeScript SDK projects.
- Add `tinybird-python-sdk-guidelines` for Python SDK projects.

**Examples:**
- "Create a datasource for user events"
- "Optimize this endpoint for low latency"
- "Set up tests for my endpoints"

## Skill Structure

Each skill contains:
- `SKILL.md` - Instructions for the agent
- `rules/` - Individual guidance files
```

## File: `skills/tinybird-best-practices/SKILL.md`
```markdown
---
name: tinybird
description: Tinybird file formats, SQL rules, optimization patterns, and best practices for datasources, pipes, endpoints, and materialized views.
---

# Tinybird Best Practices

Guidance for Tinybird file formats, SQL rules, optimization patterns, and data modeling. Use this skill when creating or editing Tinybird datafiles.

## When to Apply

- Creating or updating Tinybird resources (.datasource, .pipe, .connection)
- Writing or optimizing SQL queries
- Designing endpoint schemas and data models
- Working with materialized views or copy pipes
- Implementing deduplication patterns
- Reviewing or refactoring Tinybird project files

## Rule Files

- `rules/project-files.md`
- `rules/build-deploy.md`
- `rules/datasource-files.md`
- `rules/pipe-files.md`
- `rules/endpoint-files.md`
- `rules/materialized-files.md`
- `rules/sink-files.md`
- `rules/copy-files.md`
- `rules/connection-files.md`
- `rules/sql.md`
- `rules/endpoint-optimization.md`
- `rules/tests.md`
- `rules/deduplication-patterns.md`

## Quick Reference

- Project local files are the source of truth.
- Build target comes from `tinybird.config.json` `dev_mode` (`local` or `branch`).
- `tb deploy` targets Tinybird Cloud production.
- Commands like `tb sql` and `tb logs` default to local unless `--cloud` or `--branch=<branch-name>` is set.
- SQL is SELECT-only with Tinybird templating rules and strict parameter handling.
- Use MergeTree by default; AggregatingMergeTree for materialized targets.
- Filter early, select only needed columns, push complex work later in the pipeline.
```

## File: `skills/tinybird-best-practices/rules/build-deploy.md`
```markdown
# Build & Deploy Targeting

Start new projects with `tb init`.

Use `tinybird.config.json` as the source of truth for `tb build` targeting.

Example:

```json
{
  "dev_mode": "branch",
  "include": [
    "tinybird"
  ]
}
```

## Build/Deploy Flow

1. Read `dev_mode` from `tinybird.config.json`.
2. Run `tb build` against the configured development target.
3. Run `tb deploy` only when deployment to cloud production is explicitly requested.

## `tb build` Targeting

- `dev_mode: "local"` -> `tb build` runs against Tinybird Local.
- `dev_mode: "branch"` -> `tb build` runs against a Tinybird Cloud branch.

## `tb deploy` Targeting

- `tb deploy` targets Tinybird Cloud production.
- Do not treat `tb build` as a production deployment.

## Non-Build Command Targeting

Commands like `tb sql` and `tb logs` run against local by default.

Use explicit overrides to target other environments:

- `--cloud` for cloud
- `--branch=<branch-name>` for a specific branch

Examples:

```bash
tb sql "SELECT 1"
tb sql --cloud "SELECT 1"
tb sql --branch=feature_metrics "SELECT 1"

tb logs
tb logs --cloud
tb logs --branch=feature_metrics
```
```

## File: `skills/tinybird-best-practices/rules/connection-files.md`
```markdown
# Connection Files

- Content cannot be empty.
- Connection names must be unique.
- No indentation for property names.
- Supported types: kafka, gcs, s3.
- If user requests an unsupported type, report it and do not create it.

Kafka example:
```
TYPE kafka
KAFKA_BOOTSTRAP_SERVERS {{ tb_secret("PRODUCTION_KAFKA_SERVERS", "localhost:9092") }}
KAFKA_SECURITY_PROTOCOL SASL_SSL
KAFKA_SASL_MECHANISM PLAIN
KAFKA_KEY {{ tb_secret("PRODUCTION_KAFKA_USERNAME", "") }}
KAFKA_SECRET {{ tb_secret("PRODUCTION_KAFKA_PASSWORD", "") }}
```

S3 example:
```
TYPE s3
S3_REGION {{ tb_secret("PRODUCTION_S3_REGION", "") }}
S3_ARN {{ tb_secret("PRODUCTION_S3_ARN", "") }}
```

GCS service account example:
```
TYPE gcs
GCS_SERVICE_ACCOUNT_CREDENTIALS_JSON {{ tb_secret("PRODUCTION_GCS_SERVICE_ACCOUNT_CREDENTIALS_JSON", "") }}
```

GCS HMAC example:
```
TYPE gcs
GCS_HMAC_ACCESS_ID {{ tb_secret("gcs_hmac_access_id") }}
GCS_HMAC_SECRET {{ tb_secret("gcs_hmac_secret") }}
```
```

## File: `skills/tinybird-best-practices/rules/copy-files.md`
```markdown
# Copy Pipe Files

- Do not create by default unless requested.
- Create under `/copies`.
- Do not include COPY_SCHEDULE unless explicitly requested.
- Use TYPE COPY and TARGET_DATASOURCE.
- The default `copy_mode` is `append`; but it's better if you set it explicitly. The other option is `replace`

Example:

```
DESCRIPTION Copy Pipe to export sales hour every hour to the sales_hour_copy Data Source

NODE daily_sales
SQL >
    %
    SELECT toStartOfDay(starting_date) day, country, sum(sales) as total_sales
    FROM teams
    WHERE day BETWEEN toStartOfDay(now()) - interval 1 day AND toStartOfDay(now())
    and country = {{ String(country, 'US')}}
    GROUP BY day, country

TYPE COPY
TARGET_DATASOURCE sales_hour_copy
COPY_SCHEDULE 0 * * * *
COPY_MODE append
```
```

## File: `skills/tinybird-best-practices/rules/datasource-files.md`
```markdown
# Datasource Files

- Content cannot be empty.
- Datasource names must be unique.
- No indentation for property names (DESCRIPTION, SCHEMA, ENGINE, etc.).
- Use MergeTree by default.
- Use AggregatingMergeTree for materialized targets.
- Always use JSON paths for schema (example: `user_id` String `json:$.user_id`).
- Array syntax: `items` Array(String) `json:$.items[:]`.
- DateTime64 requires precision (use DateTime64(3)).
- Only include ENGINE_PARTITION_KEY and ENGINE_PRIMARY_KEY when explicitly requested.
- Import configuration:
  - S3/GCS: set IMPORT_CONNECTION_NAME, IMPORT_BUCKET_URI, IMPORT_SCHEDULE (GCS supports @on-demand only, S3 supports @auto).
  - Kafka: set KAFKA_CONNECTION_NAME, KAFKA_TOPIC, KAFKA_GROUP_ID.
- For landing datasources created from a .ndjson file with no schema specified, use:
  - `SCHEMA >`
  - `` `data` String `json:$` ``

Example:

```
DESCRIPTION >
    Some meaningful description of the datasource

SCHEMA >
    `column_name_1` Type `json:$.column_name_1`,
    `column_name_2` Type `json:$.column_name_2`

ENGINE "MergeTree"
ENGINE_PARTITION_KEY "partition_key"
ENGINE_SORTING_KEY "sorting_key_1, sorting_key_2"
```

## Updating Datasource Schemas (Cloud)

If a schema change is incompatible with the deployed Cloud datasource, add a FORWARD_QUERY to transform data to the new schema. The query is a SELECT list only (no FROM/WHERE). Use accurateCastOrDefault for lossy conversions.

Example:

```
FORWARD_QUERY >
    SELECT timestamp, CAST(session_id, 'UUID') as session_id, action, version, payload
```

## Sharing Datasources

```
SHARED_WITH >
    destination_workspace,
    other_destination_workspace
```

Limitations:
- Shared datasources are read-only.
- You cannot share a shared datasource.
- You cannot create a materialized view from a shared datasource.
```

## File: `skills/tinybird-best-practices/rules/deduplication-patterns.md`
```markdown
# Deduplication and Lambda Architecture

Strategies for handling duplicates and combining batch with real-time processing.

## Deduplication Strategy Selection

| Strategy | When to use |
|----------|-------------|
| Query-time (`argMax`, `LIMIT BY`, subquery) | Prototyping or small datasets |
| ReplacingMergeTree | Large datasets, need latest row per key |
| Periodic snapshots (Copy Pipes) | Freshness not critical, need rollups or different sorting keys |
| Lambda architecture | Need freshness + complex transformations that MVs can't handle |

For dimensional/small tables, periodic full replace is usually best.

## Query-time Deduplication

```sql
-- argMax: get latest value per key
SELECT post_id, argMax(views, updated_at) as views
FROM posts GROUP BY post_id

-- LIMIT BY
SELECT * FROM posts ORDER BY updated_at DESC LIMIT 1 BY post_id

-- Subquery
SELECT * FROM posts WHERE (post_id, updated_at) IN (
    SELECT post_id, max(updated_at) FROM posts GROUP BY post_id
)
```

## ReplacingMergeTree

```
ENGINE "ReplacingMergeTree"
ENGINE_SORTING_KEY "unique_id"
ENGINE_VER "updated_at"
ENGINE_IS_DELETED "is_deleted"  -- optional, UInt8: 1=deleted, 0=active
```

- Always query with `FINAL` or use alternative deduplication method
- Deduplication happens during merges (asynchronous, uncontrollable)
- **Do not** build AggregatingMergeTree MVs on top of ReplacingMergeTree—MVs only see incoming blocks, not merged state, so duplicates persist

```sql
SELECT * FROM posts FINAL WHERE post_id = {{Int64(post_id)}}
```

## Snapshot-based Deduplication (Copy Pipes)

Use Copy Pipes when:
- ReplacingMergeTree + FINAL is too slow
- You need different sorting keys that change with updates
- You need downstream Materialized Views for rollups
- The default `copy_mode` is `append`.
- Use `COPY_MODE replace` for full refreshes when the table is not massive and you don't control when duplicates can occur.
- Keep `COPY_MODE append` (default) when you do control duplicate generation and can process incrementally.

```
NODE generate_snapshot
SQL >
    SELECT post_id, argMax(views, updated_at) as views, max(updated_at) as updated_at
    FROM posts_raw
    GROUP BY post_id

TYPE COPY
TARGET_DATASOURCE posts_snapshot
COPY_SCHEDULE 0 * * * *
COPY_MODE replace
```

## Lambda Architecture

Combine batch snapshots with real-time queries when:
- Aggregating over ReplacingMergeTree (MVs fail—they only see blocks, not merged state)
- Window functions requiring full table scans
- CDC workloads
- `uniqState` performance is problematic
- endpoints that require JOINs at query time

### Pattern

1. **Batch layer**: Copy Pipe creates periodic deduplicated snapshots or intermediate tables.
2. **Real-time layer**: Query fresh data since last snapshot  
3. **Serving layer**: UNION ALL combines both

```sql
SELECT * FROM posts_snapshot
UNION ALL
SELECT post_id, argMax(views, updated_at) as views, max(updated_at) as updated_at
FROM posts_raw
WHERE updated_at > (SELECT max(updated_at) FROM posts_snapshot)
GROUP BY post_id
```

### Freshness vs Cost Trade-off

- More frequent Copy Pipe runs = fresher snapshots but higher cost
- Less frequent = stale batch layer but real-time layer covers the gap
- Balance based on query patterns and data volume

## argMax with Null Values

**Warning**: `argMaxMerge` prefers non-null values over null, even with lower timestamps.

Workaround—convert nulls to epoch before aggregation:
```sql
SELECT post_id,
    argMaxState(CASE WHEN flagged_at IS NULL THEN toDateTime('1970-01-01 00:00:00') ELSE flagged_at END, updated_at) as flagged_at
FROM posts
GROUP BY post_id
```

Handle the sentinel value in downstream queries.
```

## File: `skills/tinybird-best-practices/rules/endpoint-files.md`
```markdown
# Endpoint Files

Endpoint files are `.pipe` files with `TYPE endpoint` and should live under `/endpoints`.

- Follow all general pipe rules.
- Ensure SQL follows Tinybird SQL rules (templating, SELECT-only, parameters).
- Include the output node in TYPE or in the last node.

Example:

```
DESCRIPTION >
    Some meaningful description of the endpoint

NODE endpoint_node
SQL >
    SELECT ...
TYPE endpoint
```

## Endpoint URLs

- Run `tb endpoint ls` to list all endpoints and their URLs.
- Include dynamic parameters when needed.
- Date formats:
  - DateTime64: `YYYY-MM-DD HH:MM:SS.MMM`
  - DateTime: `YYYY-MM-DD HH:MM:SS`
  - Date: `YYYYMMDD`

## OpenAPI definitions

- curl `<api_base_url>/v0/pipes/openapi.json?token=<token>` to get the OpenAPI definition for all endpoints.
```

## File: `skills/tinybird-best-practices/rules/endpoint-optimization.md`
```markdown
# Endpoint Optimization

Use this checklist when optimizing endpoints.

## Gathering Runtime Data

Before optimizing, collect evidence from these sources:

- **Endpoint source code**: SQL, datasources, materialized views, and pipes in the workspace.
- **`pipe_stats_rt`**: Query `SELECT * FROM tinybird.pipe_stats_rt WHERE pipe_name = 'endpoint_name'` to check execution duration percentiles (p50, p90, p95, p99), read_bytes, rows_read, and error counts.
- **Query plan**: Call the endpoint with `?explain=true` (e.g., `https://$TB_HOST/v0/pipes/endpoint_name?explain=true`) to inspect join strategies, aggregation stages, index usage, and partition pruning.

Ignore datasources with fewer than 10,000 rows or less than 50 MB of data.

1) Aggregations at query time?
- Fix: Move to materialized views when possible, to snapshots (copy pipes) or lambda architecture if MVs do not fit.

## Structural Rules

Schema, query-shape, or data-layout issues. Apply whenever detected — no runtime evidence needed.

### Selecting unnecessary columns
- `SELECT *` or unused columns increase I/O, decompression cost, and cache pressure.
- Fix: Explicitly select only required columns.

### Oversized data types
- Larger types than necessary reduce compression and increase CPU/memory usage.
- Fix: Use smallest safe types. Use `LowCardinality` for low-unique strings, defaults instead of `Nullable`.

### Unnecessary Nullable columns
- `Nullable` adds overhead from null bitmaps and extra checks.
- Fix: Replace `Nullable(T)` with `T` when the column never contains nulls.

### Inefficient ORDER BY key ordering
- High-cardinality columns first in `ORDER BY` reduce sparse index effectiveness and data skipping.
- Fix: Start `ORDER BY` with low-cardinality and/or time columns. Avoid timestamp as first key in multi-tenant cases.

### Unnecessary casting
- Casting a column to its existing type wastes CPU and can block partition pruning.
- Fix: Remove redundant casts; fix types at ingestion time if needed.

### Excessive string materialization
- Materializing full `String` values when only metadata is needed wastes memory and CPU.
- Fix: Extract required string properties at ingestion time into typed columns.

### Filter before join/aggregation
- Applying filters after joins or aggregations increases input size and cost.
- Fix: Push filters as early as possible in the query pipeline.

## Runtime-Dependent Rules

Apply only when runtime thresholds are exceeded, based on `pipe_stats_rt` and `EXPLAIN` data.

### Aggregations at query time
- **When**: p95 > 5s, or aggregation dominates `EXPLAIN`, or memory > 60%, or OOM/timeout errors.
- Fix: Precompute via materialized view.

### JOINs at query time
- **When**: p95 > 5s, or join dominates `EXPLAIN`, or memory spikes, or OOM/timeout errors.
- Fix: Move join to ingestion time via materialized view, or denormalize.

### Incorrect or missing sorting keys
- **When**: reads > 10% of granules, and p95 > 3s or rows_read/rows_returned > 100x.
- Fix: Rebuild datasource with `ORDER BY` aligned to selective filters.

### PREWHERE for early filtering
- **When**: rows_read/rows_returned > 50x, or p95 > 3s, or `EXPLAIN` shows late filtering.
- Fix: Push selective filters into `PREWHERE`.

### Data skipping indexes
- **When**: filters on non-primary-key columns, and rows_read/rows_returned > 100x, or p95 > 3s.
- Fix: Add appropriate skip indexes and validate with `EXPLAIN`.

### Large GROUP BY at query time
- **When**: p95 > 5s, or aggregation memory > 50%, or OOM/timeout errors.
- Fix: Pre-aggregate at ingestion time using materialized view.

### Regex at query time
- **When**: p95 > 3s, or CPU > 70%.
- Fix: Move regex logic to ingestion time.

### Unbounded history without TTL
- **When**: p95 increases week-over-week, or rows_read grows for identical queries.
- Fix: Create a TTL-backed datasource via materialized view.

### Misaligned or missing partition pruning
- **When**: >20% of partitions scanned, or p95 > 3s, or `EXPLAIN` shows ineffective pruning.
- Fix: Recreate datasource with an aligned partitioning key. Include partition key column in query filters.

### ORDER BY with LIMIT without pushdown
- **When**: rows sorted >> LIMIT (>100x), or p95 > 3s.
- Fix: Restructure query or pre-materialize top-k at ingestion time.

### DISTINCT instead of GROUP BY
- **When**: p95 > 5s, or memory > 50%.
- Fix: Replace with ingestion-time aggregation or `GROUP BY`.

### Overuse of FINAL
- **When**: p95 > 3s, or rows_read >> rows_returned.
- Fix: Remove `FINAL` by enforcing correctness at ingestion time (lambda architecture).

### Expensive JSON extraction at query time
- **When**: p95 > 3s, or CPU > 70%.
- Fix: Extract JSON fields into typed columns at ingestion time.

### Large IN lists
- **When**: p95 > 3s, or query planning time is high.
- Fix: Replace with lookup datasource or ingestion-time materialization.

### Approximate uniques
- **When**: exact `COUNT(DISTINCT)` with p95 > 5s, or memory > 50%, or OOM errors.
- Fix: Use `uniqHLL12` or similar approximate functions when acceptable.

## Monitoring and Validation

- Track `tinybird.pipe_stats_rt` and `tinybird.pipe_stats`.
- Success metrics: lower latency, lower read_bytes, improved read_bytes/write_bytes ratio.
- If for any reason these two datasources don't contain the needed information, check `system.query_log`

## Query Explain

- For more details, call the endpoint with explain=true parameter to understand the query plan. E.g: https://$TB_HOST/v0/pipes/endpoint_name?explain=true

## Templates

Materialized view:
```
NODE materialized_view_name
SQL >
  SELECT toDate(timestamp) as date, customer_id, countState(*) as event_count
  FROM source_table
  GROUP BY date, customer_id

TYPE materialized
DATASOURCE mv_datasource_name
ENGINE "AggregatingMergeTree"
ENGINE_PARTITION_KEY "toYYYYMM(date)"
ENGINE_SORTING_KEY "customer_id, date"
```

Optimized query:
```
NODE endpoint_query
SQL >
  %
  SELECT date, sum(amount) as daily_total
  FROM events
  WHERE customer_id = {{ String(customer_id) }}
    AND date >= {{ Date(start_date) }}
    AND date <= {{ Date(end_date) }}
  GROUP BY date
  ORDER BY date DESC
```
```

## File: `skills/tinybird-best-practices/rules/materialized-files.md`
```markdown
# Materialized Pipe Files

- Do not create by default unless requested.
- Create under `/materializations`.
- Use TYPE MATERIALIZED and set DATASOURCE to the target datasource.
- Use State modifiers in the pipe; use AggregateFunction in the target datasource.
- Use Merge modifiers when reading AggregateFunction columns.
- Put all dimensions in ENGINE_SORTING_KEY, ordered from least to most cardinality.

Example:

```
NODE daily_sales
SQL >
    SELECT toStartOfDay(starting_date) day, country, sumState(sales) as total_sales
    FROM teams
    GROUP BY day, country

TYPE MATERIALIZED
DATASOURCE sales_by_hour
```

Target datasource example:

```
SCHEMA >
    `total_sales` AggregateFunction(sum, Float64),
    `sales_count` AggregateFunction(count, UInt64),
    `dimension_1` String,
    `dimension_2` String,
    `date` DateTime

ENGINE "AggregatingMergeTree"
ENGINE_PARTITION_KEY "toYYYYMM(date)"
ENGINE_SORTING_KEY "date, dimension_1, dimension_2"
```

## Usual gotchas
- Materialized Views work as insert triggers, which means a delete or truncate operation on your original Data Source doesn't affect the related Materialized Views.

- As transformation and ingestion in the Materialized View is done on each block of inserted data in the original Data Source, some operations such as GROUP BY, ORDER BY, DISTINCT and LIMIT might need a specific engine, such as AggregatingMergeTree or SummingMergeTree, which can handle data aggregations.

- The Data Source resulting from a Materialized View generated using JOIN is automatically updated only if and when a new operation is performed over the Data Source in the FROM.
```

## File: `skills/tinybird-best-practices/rules/pipe-files.md`
```markdown
# Pipe Files (General)

- Pipe names must be unique.
- Node names must differ from the pipe name and any resource name.
- No indentation for property names (DESCRIPTION, NODE, SQL, TYPE, etc.).
- Allowed TYPE values: endpoint, copy, materialized, sink.
- Add the output node in the TYPE section or in the last node.

Example:

```
DESCRIPTION >
    Some meaningful description of the pipe

NODE node_1
SQL >
    SELECT ...
TYPE endpoint
```
```

## File: `skills/tinybird-best-practices/rules/project-files.md`
```markdown
# Project Files

## Project Root

- By default, create a `tinybird/` folder at the project root and nest Tinybird folders under it.
- Ensure the `.tinyb` credentials file is at the same level where the CLI commands are run.

## tb info

Use `tb info` to confirm CLI context, especially for credentials issues.

It reports information about Local and Cloud environments:
- Where the CLI is loading the `.tinyb` file from
- Current logged workspace
- API URL
- UI URL
- ClickHouse HTTP interface URL

It can show values for both Cloud and Local environments.

## File Locations

Default locations (use these unless the project uses a different structure):

- Endpoints: `/endpoints`
- Materialized pipes: `/materializations`
- Sink pipes: `/sinks`
- Copy pipes: `/copies`
- Connections: `/connections`
- Datasources: `/datasources`
- Fixtures: `/fixtures`

## File-Specific Rules

See these rule files for detailed requirements:

- `rules/datasource-files.md`
- `rules/pipe-files.md`
- `rules/endpoint-files.md`
- `rules/materialized-files.md`
- `rules/sink-files.md`
- `rules/copy-files.md`
- `rules/connection-files.md`

After making changes in the project files, check `rules/build-deploy.md` for next steps.
```

## File: `skills/tinybird-best-practices/rules/sink-files.md`
```markdown
# Sink Pipe Files

- Do not create by default unless requested.
- Create under `/sinks`.
- Valid external systems: Kafka, S3, GCS.
- Sink pipes depend on a connection; reuse existing connections when possible.
- Do not include EXPORT_SCHEDULE unless explicitly requested.
- Use TYPE SINK and set EXPORT_CONNECTION_NAME.

Example:

```
DESCRIPTION Sink Pipe to export sales hour every hour using my_connection

NODE daily_sales
SQL >
    %
    SELECT toStartOfDay(starting_date) day, country, sum(sales) as total_sales
    FROM teams
    WHERE day BETWEEN toStartOfDay(now()) - interval 1 day AND toStartOfDay(now())
    and country = {{ String(country, 'US')}}
    GROUP BY day, country

TYPE sink
EXPORT_CONNECTION_NAME "my_connection"
EXPORT_BUCKET_URI "s3://tinybird-sinks"
EXPORT_FILE_TEMPLATE "daily_prices"
EXPORT_SCHEDULE "*/5 * * * *"
EXPORT_FORMAT "csv"
EXPORT_COMPRESSION "gz"
EXPORT_STRATEGY "truncate"
```
```

## File: `skills/tinybird-best-practices/rules/sql.md`
```markdown
# SQL Rules

## Core Principles

1. Filter early and read as little data as possible.
2. Select only needed columns.
3. Do complex work later in the pipeline.
4. Prefer ClickHouse functions; only supported functions are allowed.

## Query Requirements

- SQL must be valid ClickHouse SQL with Tinybird templating (Tornado).
- Only SELECT statements are allowed.
- Avoid CTEs; use nodes or subqueries instead.
- Do not use system tables (system.tables, system.datasources, information_schema.tables).
- Do not use CREATE/INSERT/DELETE/TRUNCATE or currentDatabase().

## Parameter and Templating Rules

- If parameters are used, the query must start with `%` on its own line.
- Parameter functions: String, DateTime, Date, Float32, Float64, Int, Integer, UInt8, UInt16, UInt32, UInt64, UInt128, UInt256, Int8, Int16, Int32, Int64, Int128, Int256.
- Parameter names must be different from column names.
- Default values must be hardcoded.
- Parameters are never quoted.
- In `defined()` checks, do not quote the parameter name.

Bad:
```
SELECT * FROM events WHERE session_id={{String(my_param, "default")}}
```

Good:
```
%
SELECT * FROM events WHERE session_id={{String(my_param, "default")}}
```

## Join and Aggregation Rules

- Filter before JOINs and GROUP BY.
- Avoid joining tables with >1M rows without filtering.
- Avoid nested aggregates; use subqueries instead.
- Use AggregateFunction columns with -Merge combinators.

## Operation Order

1. WHERE filters
2. Select needed columns
3. JOIN
4. GROUP BY / aggregates
5. ORDER BY
6. LIMIT

## External Tables

Iceberg:
```
FROM iceberg('s3://bucket/path/to/table', {{tb_secret('aws_access_key_id')}}, {{tb_secret('aws_secret_access_key')}})
```

Postgres:
```
FROM postgresql({{ tb_secret("db_host_port") }}, 'database', 'table', {{tb_secret('db_username')}}, {{tb_secret('db_password')}}, 'schema_optional')
```

Do not split host and port into multiple secrets.
```

## File: `skills/tinybird-best-practices/rules/tests.md`
```markdown
# Tests

- Test file name must match the pipe name.
- Scenario names must be unique inside a test file.
- Parameters format: `param1=value1&param2=value2`.
- Preserve case and formatting when user provides parameters.
- If no parameters, create a single test with empty parameters.
- Use fixture data for expected results; do not query endpoints or SQL to infer data.
- Before creating tests, analyze fixture files used by the endpoint tables.
- `expected_result` should always be an empty string; the tool fills it.
- Only create tests when explicitly requested (e.g. "Create tests for this endpoint").
- If asked to "test" or "call" an endpoint, call the endpoint instead of creating tests.

Test format:

```
- name: kpis_single_day
  description: Test hourly granularity for a single day
  parameters: date_from=2024-01-01&date_to=2024-01-01
  expected_result: ''
```
```

## File: `skills/tinybird-cli-guidelines/SKILL.md`
```markdown
---
name: tinybird-cli-guidelines
description: Tinybird CLI commands, workflows, and operations. Use when running tb commands, managing local development, deploying, or working with data operations.
---

# Tinybird CLI Guidelines

Guidance for using the Tinybird CLI (tb) for local development, deployments, data operations, and workspace management.

## When to Apply

- Running any `tb` command
- Local development with Tinybird Local
- Building and deploying projects
- Appending, replacing, or deleting data
- Managing tokens and secrets via CLI
- Generating mock data
- Running tests

## Rule Files

- `rules/cli-commands.md`
- `rules/build-deploy.md`
- `rules/local-development.md`
- `rules/data-operations.md`
- `rules/append-data.md`
- `rules/mock-data.md`
- `rules/tokens.md`
- `rules/secrets.md`

## Quick Reference

- CLI 4.0 workflow: configure `dev_mode` once, then use plain `tb build` and `tb deploy`.
- `tb build` targets your configured development environment (`branch` or `local`) in tinybird.config.json
- `tb deploy` targets Tinybird Cloud production.
- Use `--cloud`/`--local`/`--branch` only as explicit manual overrides.
- Use `tb info` to check CLI context.
- Never invent commands or flags; run `tb <command> --help` to verify.
```

## File: `skills/tinybird-cli-guidelines/rules/append-data.md`
```markdown
# Append Data

Tinybird CLI supports three ways to append data to an existing datasource: local file, remote URL, or events payload.

## CLI: tb datasource append

```
tb datasource append [datasource_name] --file /path/to/local/file
```

```
tb datasource append [datasource_name] --url https://example.com/data.csv
```

```
tb datasource append [datasource_name] --events '{"a":"b", "c":"d"}'
```

Notes:
- The command appends to an existing datasource.
- Use `tb --cloud datasource append` to target Cloud; Local is the default.
- For ingesting data from Kafka, S3 or GCS, see: https://www.tinybird.co/docs/forward/get-data-in/connectors

You can also send POST request to v0/events (streaming) and v0/datasources (batch) endpoints.
```

## File: `skills/tinybird-cli-guidelines/rules/build-deploy.md`
```markdown
# Build & Deploy

Use this rule to keep local files, development environments, and production deployments aligned under the CLI 4.0 workflow.

## Default Workflow (CLI 4.0)

1. Configure `dev_mode` in `tinybird.config.json` (`branch`, `local`, or `manual`).
2. Run `tb build` to validate and sync to the configured development target.
3. Run `tb deploy` to deploy to Tinybird Cloud main (production).

In CLI 4.0, build/deploy should usually be run without `--cloud`, `--local`, or `--branch`.

## `tb build` Behavior

- `dev_mode=local`: builds against Tinybird Local.
- `dev_mode=branch`: builds against a Cloud branch derived from the current git branch (created automatically if needed).
- `dev_mode=manual`: requires explicit flags (`--local`, `--cloud`, `--branch`) for environment selection.
- In branch mode, building from `main`/`master` is blocked to avoid accidental production changes.

## `tb deploy` Behavior

- `tb deploy` deploys current project files to Tinybird Cloud main.
- Use only when the user explicitly requests a production deployment.
- Ask for confirmation before deploying.

## Deploy Check

- Run `tb deploy --check` before real deploys to catch schema/dependency issues early.
- Use check mode whenever deployment intent is uncertain.

## Destructive operations and flags

- Deleting datasources, pipes, or connections locally requires an explicit destructive deploy.
- Use `tb deploy --allow-destructive-operations` only when the user confirms deletion or data loss is acceptable.
- If you see warnings about deletions, stop and ask for confirmation before re-running with the flag.

Example:
```
tb deploy --allow-destructive-operations
```

## Manual Overrides

- Explicit flags still work and override `dev_mode`.
- Use overrides only when the user explicitly asks for a specific environment target.

## Validation intent (why)

- Building keeps development environments aligned with local files for fast iteration.
- Deploy checks reduce failed deployments by validating changes before publishing.

## What not to do

- Do not deploy destructive changes without `--allow-destructive-operations` and explicit user confirmation.
- Do not assume production is updated after `tb build`; `build` and `deploy` are separate operations.
```

## File: `skills/tinybird-cli-guidelines/rules/cli-commands.md`
```markdown
# Tinybird CLI Commands

**⚠️ Never invent commands or flags.** If you are unsure whether a command or flag exists, run `tb <command> --help` to verify before using it. Only use commands and flags documented here or confirmed via `--help`.

## Build/Deploy Context (CLI 4.0)

- Preferred flow: configure `dev_mode` once, then run plain `tb build` and `tb deploy`.
- Use `--cloud`, `--local`, and `--branch` only as explicit manual overrides.

## Global Overrides

- `tb --cloud <command>`: Run command against Cloud
- `tb --local <command>`: Run command against Local
- `tb --branch <branch_name> <command>`: Run command against a specific branch
- `tb --debug <command>`: Print debug information

## Project & Development

- `tb init`: Initialize a new project
- `tb create`: Deprecated alias for `tb init`
- `tb info`: Show project information and CLI context
- `tb build`: Validate and build the project
- `tb build --watch`: Build and watch for changes
- `tb dev`: Build and watch for changes
- `tb dev --ui`: Connect local project to Tinybird UI
- `tb preview`: Create/update preview environment for the current branch
- `tb open`: Open workspace in the browser
- `tb fmt <file>`: Format a .datasource, .pipe, or .connection file
- `tb fmt <file> --diff`: Show diff without modifying file

## Deploy & Deployments

- `tb deploy`: Deploy the project
- `tb deploy --check`: Validate deployment without actually creating
- `tb deploy --wait`: Wait for deployment to finish
- `tb deploy --allow-destructive-operations`: Allow destructive changes (requires explicit confirmation)
- `tb deployment ls`: List all deployments
- `tb deployment create`: Create a staging deployment and validate before promoting
- `tb deployment promote`: Promote a staging deployment to production
- `tb deployment discard`: Discard a pending deployment

## Logs

- `tb logs`: Show recent logs from common service datasources
- `tb logs --start -30m --source '*'`: Query all sources for a custom time range
- `tb logs --output json`: Emit logs as JSON for scripting

## Data Sources

- `tb datasource ls`: List all data sources
- `tb datasource append <name> --file <path>`: Append data from local file
- `tb datasource append <name> --url <url>`: Append data from URL
- `tb datasource append <name> --events '<json>'`: Append JSON events
- `tb datasource replace <name> <file_or_url>`: Full replace of data source
- `tb datasource replace <name> <file_or_url> --sql-condition "<condition>"`: Selective replace
- `tb datasource delete <name> --sql-condition "<condition>"`: Delete matching rows
- `tb datasource delete <name> --sql-condition "<condition>" --wait`: Delete and wait for completion
- `tb datasource truncate <name> --yes`: Delete all rows
- `tb datasource truncate <name> --cascade --yes`: Truncate including dependent MVs
- `tb datasource sync <name> --yes`: Sync from S3/GCS connection
- `tb datasource export <name> --format csv`: Export data to file

## Pipes & Endpoints

- `tb pipe ls`: List all pipes
- `tb endpoint ls`: List all endpoints
- `tb endpoint data <pipe_name>`: Get data from endpoint
- `tb endpoint data <pipe_name> --param_name value`: Get data with parameters
- `tb endpoint stats <pipe_name>`: Show endpoint stats for last 7 days
- `tb endpoint url <pipe_name>`: Print endpoint URL
- `tb endpoint token <pipe_name>`: Get token to read endpoint

## SQL Queries

- `tb sql "<query>"`: Run SQL query
- `tb sql "<query>" --stats`: Run query and show stats
- `tb sql --pipe <path> --node <node_name>`: Run SQL from a specific pipe node

## Materializations & Copy Pipes

- `tb materialization ls`: List all materializations
- `tb copy ls`: List all copy pipes
- `tb copy run <pipe_name>`: Run a copy pipe manually
- `tb copy run <pipe_name> --param key=value`: Run with parameters

## Testing

- `tb test run`: Run the full test suite
- `tb test run <file_or_test>`: Run specific test file or test
- `tb test update <file_or_test>`: Update test expectations

## Mock Data

- `tb mock` was removed in CLI 4.0
- Use the `fixtures/` folder and agent skills to generate sample data, then append with `tb datasource append`

## Tokens & Secrets

- `tb token ls`: List all tokens
- `tb secret ls`: List all secrets
- `tb secret set <name> <value>`: Create or update a secret
- `tb secret rm <name>`: Delete a secret

## Connections & Sinks

- `tb connection ls`: List all connections
- `tb sink ls`: List all sinks

## Jobs

- `tb job ls`: List all jobs
- `tb job cancel <job_id>`: Cancel a running job

## Branches

- `tb branch ls`: List all branches
- `tb branch create <name>`: Create a new branch
- `tb branch rm <name>`: Remove a branch
- `tb branch clear`: Clear branch state

## Tinybird Local

- `tb local start`: Start Tinybird Local container
- `tb local stop`: Stop Tinybird Local
- `tb local restart --yes`: Restart Tinybird Local
- `tb local status`: Check Tinybird Local status
- `tb local remove`: Remove Tinybird Local completely
- `tb local version`: Show Tinybird Local version
- `tb local clear`: Clear local workspace state

## Workspace

- `tb workspace ls`: List all workspaces
- `tb workspace current`: Show current workspace
- `tb workspace clear --yes`: Clear workspace state

## Authentication

- `tb login`: Authenticate via browser
- `tb logout`: Remove authentication
- `tb update`: Update CLI to latest version
```

## File: `skills/tinybird-cli-guidelines/rules/data-operations.md`
```markdown
# Data Operations (Replace & Delete)

Operations for updating and removing data from Data Sources.

## Delete Data Selectively

Delete rows matching a SQL condition:

```bash
tb datasource delete events --sql-condition "toDate(date) >= '2019-11-01' AND toDate(date) <= '2019-11-30'"
```

- Runs asynchronously (returns job ID); use `--wait` to block until complete
- **Does not cascade** to downstream Materialized Views—delete from MVs separately
- Requires ADMIN token scope
- Safe to run while actively ingesting data

## Truncate Data Source

Delete all rows from a Data Source:

```bash
tb datasource truncate events
```

Use `--cascade` to also truncate dependent Data Sources attached via Materialized Views.

## Replace Data Selectively (Partial Replace)

Replace only data matching a condition:

```bash
tb datasource replace events data.csv --sql-condition "toDate(date) >= '2019-11-01' AND toDate(date) <= '2019-11-30'"
```

**⚠️ Critical**: Never replace data in partitions where you are actively ingesting. You may lose data inserted during the operation.

**Rules**:
- **Always include the partition key** in the SQL condition
- The condition determines: (1) which partitions to operate on, (2) which rows from new data to append
- **Cascades automatically** to downstream Materialized Views (all must have compatible partition keys)
- Schema of new data must match existing Data Source exactly

### Why Partition Key Matters

If your Data Source uses `ENGINE_PARTITION_KEY "country"` and you run:
```bash
tb datasource replace events data.csv --sql-condition "status='active'"
```
This will **not work as expected**—the replace process uses payload rows to identify partitions. Always match the partition key.

## Replace Data Completely (Full Replace)

Replace entire Data Source contents (no `--sql-condition`):

```bash
tb datasource replace events data.csv
```

**⚠️ Critical**: Do not run while actively ingesting—you may lose data.
```

## File: `skills/tinybird-cli-guidelines/rules/local-development.md`
```markdown
# Tinybird Local Development

## Overview

- Tinybird Local runs as a Docker container managed by the Tinybird CLI.
- In CLI 4.0, `tb build` uses `dev_mode` from `tinybird.config.json`.
- Use Tinybird Local for fast local iteration (`dev_mode=local`), then deploy with `tb deploy`.

## Commands

- `tb local start`
  - Options: `--use-aws-creds`, `--volumes-path <path>`, `--skip-new-version`, `--user-token`, `--workspace-token`, `--daemon`.
- `tb local stop`
- `tb local restart`
  - Options: `--use-aws-creds`, `--volumes-path`, `--skip-new-version`, `--yes`.
- `tb local status`
- `tb local remove`
- `tb local version`
- `tb local generate-tokens`

Notes:
- If you remove the container without a persisted volume, local data is lost.
- Manual flags (`--local`, `--cloud`, `--branch`) still work as overrides.

## Local-First Workflow

1) `tb local start`
2) Set `dev_mode` to `local` in `tinybird.config.json`
3) Develop resources and run `tb build` as needed
4) Test endpoints/queries locally
5) Run `tb deploy` only when user explicitly requests production deployment

Use `--volumes-path` to persist data between restarts.

## Troubleshooting

- If status shows unhealthy, run `tb local restart` and re-check.
- If authentication is not ready, wait or restart the container.
- If memory warnings appear in status, increase Docker memory allocation.
- If Local is not running, start it with `tb local start`.
```

## File: `skills/tinybird-cli-guidelines/rules/mock-data.md`
```markdown
# Mock Data Generation

Tinybird mock data flow (as implemented by the agent) for a datasource:

1) Build a SQL query that returns mock rows.
2) Execute locally with a limit and format using `tb --output=json|csv '<sql>' --rows-limit <rows>` command.
3) Preview the generated output.
4) Confirm creation of a fixture file under `fixtures/`.
5) Write the fixture file:
   - `fixtures/<datasource_name>.ndjson` or `fixtures/<datasource_name>.csv`
6) Confirm append.
7) Append the fixture to the datasource in Tinybird Local.

## Example Mock Query

```
SELECT
    rand() % 1000 AS experience_gained,
    1 + rand() % 100 AS level,
    rand() % 500 AS monster_kills,
    concat('player_', toString(rand() % 10000)) AS player_id,
    rand() % 50 AS pvp_kills,
    rand() % 200 AS quest_completions,
    now() - rand() % 86400 AS timestamp
FROM numbers(ROWS)
```

Notes:
- The query must return exactly `ROWS` rows via `FROM numbers(ROWS)`.
- Do not add FORMAT or a trailing semicolon in the mock query itself.

## Error Handling Notes

- If the datasource is in quarantine, query `<datasource_name>_quarantine` and surface the first 5 rows.
- If append fails with "must be created first with 'mode=create'", rebuild the project and retry.
```

## File: `skills/tinybird-cli-guidelines/rules/secrets.md`
```markdown
# Secrets

## Usage in Files

- Secret syntax: `{{ tb_secret("SECRET_NAME", "DEFAULT_VALUE_OPTIONAL") }}`.
- Use secrets for credentials in connections and pipe SQL.
- Secrets in pipe files do not allow default values.
- Secrets in connection files may include default values.
- Do not replace secrets with dynamic parameters when secrets are required.

## CLI: tb secret

- List secrets:
  - `tb secret ls`
  - `tb secret ls --match _test`

- Set or update a secret:
  - `tb secret set SECRET_NAME SECRET_VALUE`
  - `tb secret set SECRET_NAME` (prompts securely)
  - `tb secret set SECRET_NAME --multiline` (opens editor)

- Remove a secret:
  - `tb secret rm SECRET_NAME`

## Local Secrets

- If a `.env.local` file is present, its secrets are loaded automatically in Tinybird Local.
```

## File: `skills/tinybird-cli-guidelines/rules/tokens.md`
```markdown
# Tokens

- Resource-scoped tokens are defined in datafiles.
- Tinybird tracks and updates resource-scoped tokens from datafile contents.

Scopes and usage:
- DATASOURCES:READ:datasource_name => `TOKEN <token_name> READ` in `.datasource` files
- DATASOURCES:APPEND:datasource_name => `TOKEN <token_name> APPEND` in `.datasource` files
- PIPES:READ:pipe_name => `TOKEN <token_name> READ` in `.pipe` files

Examples:
```
TOKEN app_read READ
TOKEN landing_append APPEND
```

For operational tokens (not tied to resources):
```
tb token create static new_admin_token --scope <scope>
```
Scopes: `TOKENS`, `ADMIN`, `ORG_DATASOURCES:READ`, `WORKSPACE:READ_ALL`.

## JWT Tokens

JWT tokens have a TTL and can only use `PIPES:READ` or `DATASOURCES:READ` scopes. They are intended for end users calling endpoints or reading datasources without exposing a master API key.

Create a JWT token:
```
tb token create jwt my_jwt_token --ttl 1h --scope PIPES:READ --resource my_pipe
```

Datasource read with filter:
```
tb token create jwt my_jwt_token --ttl 1h --scope DATASOURCES:READ --resource my_datasource --filter "column = 'value'"
```

Multiple scopes and resources (counts must match), with optional fixed params for PIPES:READ:
```
tb token create jwt my_jwt_token --ttl 1h \
  --scope PIPES:READ --resource my_pipe --fixed-params "k1=v1,k2=v2" \
  --scope DATASOURCES:READ --resource my_datasource --filter "column = 'value'"
```
```

## File: `skills/tinybird-python-sdk-guidelines/SKILL.md`
```markdown
---
name: tinybird-python-sdk-guidelines
description: Tinybird Python SDK for defining datasources, pipes, and queries in Python. Use when working with tinybird-sdk, Python Tinybird projects, or data ingestion and queries in Python.
---

# Tinybird Python SDK Guidelines

Guidance for using the `tinybird-sdk` package to define Tinybird resources in Python.

## When to Apply

- Installing or configuring tinybird-sdk
- Defining datasources, pipes, or endpoints in Python
- Creating Tinybird clients in Python
- Using data ingestion or queries in Python
- Running tinybird dev/build/deploy commands for Python projects
- Migrating from legacy .datasource/.pipe files to Python
- Defining connections (Kafka, S3, GCS)
- Creating materialized views, copy pipes, or sink pipes

## Rule Files

- `rules/getting-started.md`
- `rules/configuration.md`
- `rules/defining-datasources.md`
- `rules/defining-endpoints.md`
- `rules/client.md`
- `rules/low-level-api.md`
- `rules/cli-commands.md`
- `rules/connections.md`
- `rules/materialized-views.md`
- `rules/copy-sink-pipes.md`
- `rules/tokens.md`

## Quick Reference

- Install: `pip install tinybird-sdk`
- Initialize: `tinybird init`
- Dev mode: `tinybird dev` (uses configured `dev_mode`, typically branch)
- Build: `tinybird build` (builds against configured dev target)
- Deploy: `tinybird deploy` (deploys to main/production)
- Preview in CI: `tinybird preview`
- Migrate: `tinybird migrate` (convert .datasource/.pipe files to Python)
- Server-side only; never expose tokens in browsers
```

## File: `skills/tinybird-python-sdk-guidelines/rules/cli-commands.md`
```markdown
# SDK CLI Commands

The SDK installs `tinybird` as a runtime dependency. Some commands are handled by the SDK; others delegate to the Tinybird CLI.

## CLI 4.0 Build/Deploy Model

- Configure your default development target once in `tinybird.config.*` (`dev_mode`).
- Run `tinybird build` without environment flags for normal workflows.
- Run `tinybird deploy` to publish to Tinybird Cloud main.
- Use `--local`/`--branch` only as explicit overrides.

## tinybird init

Initialize a new Tinybird project:

```bash
tinybird init
tinybird init --force          # Overwrite existing files
tinybird init --skip-login     # Skip browser authentication
```

Creates `lib/datasources.py`, `lib/pipes.py`, `lib/client.py`, and `tinybird.config.json`.

## tinybird migrate

Migrate legacy datafiles to Python definitions:

```bash
tinybird migrate "tinybird/**/*.datasource" "tinybird/**/*.pipe" "tinybird/**/*.connection"
tinybird migrate tinybird/legacy --out ./tinybird.migration.py
tinybird migrate tinybird --dry-run
```

Converts `.datasource`, `.pipe`, and `.connection` files into a Python definitions file.

## tinybird dev

Watch schema files and auto-sync to Tinybird:

```bash
tinybird dev                   # Watch and sync using configured dev_mode
tinybird dev --local           # Sync with local container
tinybird dev --branch          # Force branch mode for this run
```

**Important**: In branch mode, feature branches are expected; main/master are blocked to prevent accidental production changes.

## tinybird build

Build and validate resources using your configured development target:

```bash
tinybird build                 # Build to dev_mode target (branch or local)
tinybird build --dry-run       # Preview build operations
tinybird build --local         # Build to local container
tinybird build --branch        # Build to branch for this run
```

Use `tinybird build` for iterative development; it does not publish to production.

## tinybird deploy

Deploy resources to the main workspace (production):

```bash
tinybird deploy                # Deploy to main/production
tinybird deploy --dry-run      # Preview without deploying
tinybird deploy --check        # Validate without deploying
tinybird deploy --wait         # Wait for deployment completion
tinybird deploy --allow-destructive-operations  # Allow breaking changes
```

This is the only way to deploy to main.

## tinybird preview

Create or refresh a CI preview environment for the current branch:

```bash
tinybird preview
```

Use this in pull request workflows so preview apps query isolated Tinybird preview branches.

## tinybird pull

Pull resources from remote workspace:

```bash
tinybird pull                  # Pull to default location
tinybird pull --output-dir ./tinybird-datafiles
tinybird pull --force          # Overwrite existing files
```

## tinybird login

Authenticate via browser:

```bash
tinybird login
```

Useful for existing projects or token refresh.

## tinybird branch

Manage branches:

```bash
tinybird branch list           # List all branches
tinybird branch status         # Show current branch status
tinybird branch delete <name>  # Delete a branch
```

## tinybird info

Display workspace, local, and project configuration:

```bash
tinybird info                  # Show configuration
tinybird info --json           # Output as JSON
```

## Development Workflow

1. `tinybird init` - Initialize project
2. Define datasources and pipes in Python
3. `tinybird build` or `tinybird dev` - Iterate against configured dev target
4. `tinybird preview` in CI - Create preview branch environment per PR
5. `tinybird deploy` - Deploy to production after merge

## Migration Workflow

1. `tinybird migrate "path/to/*.datasource" "path/to/*.pipe"` - Convert legacy files
2. Review generated Python file
3. Move definitions to `lib/datasources.py` and `lib/pipes.py`
4. Update `tinybird.config.json` to include Python files
5. `tinybird dev` - Verify sync works

## Important Notes

- The CLI auto-generates datafiles from Python definitions before `build`, `deploy`, and `preview`
- Use `--check`/`--dry-run` before production deploys when in doubt
- The CLI automatically loads `.env.local` and `.env` files
```

## File: `skills/tinybird-python-sdk-guidelines/rules/client.md`
```markdown
# Creating the Tinybird Client

## Client Setup

```python
# lib/client.py
from tinybird_sdk import Tinybird
from .datasources import page_views
from .pipes import top_pages

tinybird = Tinybird(
    {
        "datasources": {"page_views": page_views},
        "pipes": {"top_pages": top_pages},
    }
)

__all__ = ["tinybird", "page_views", "top_pages"]
```

## Using the Client

### Data Ingestion

```python
from lib.client import tinybird

# Ingest one row
tinybird.page_views.ingest(
    {
        "timestamp": "2024-01-15 10:30:00",
        "pathname": "/home",
        "session_id": "abc123",
        "country": "US",
    }
)

# Batch ingestion (list of rows)
tinybird.page_views.ingest([
    {"timestamp": "2024-01-15 10:30:00", "pathname": "/home", "session_id": "abc", "country": "US"},
    {"timestamp": "2024-01-15 10:31:00", "pathname": "/about", "session_id": "abc", "country": "US"},
])
```

### Querying Endpoints

```python
from lib.client import tinybird

result = tinybird.top_pages.query(
    {
        "start_date": "2024-01-01 00:00:00",
        "end_date": "2024-01-31 23:59:59",
        "limit": 5,
    }
)

# Access result data
for row in result["data"]:
    print(f"{row['pathname']}: {row['views']} views")
```

## Datasource Operations

The client provides several operations for managing datasource data:

### Append from URL
```python
tinybird.page_views.append(
    {
        "url": "https://example.com/page_views.csv",
    }
)
```

### Replace (Full Snapshot)
```python
tinybird.page_views.replace(
    {
        "url": "https://example.com/page_views_full_snapshot.csv",
    }
)
```

### Delete Rows
```python
# Delete matching rows
tinybird.page_views.delete(
    {
        "delete_condition": "country = 'XX'",
    }
)

# Dry run to preview deletions
tinybird.page_views.delete(
    {
        "delete_condition": "country = 'XX'",
        "dry_run": True,
    }
)
```

### Truncate
```python
tinybird.page_views.truncate()
```

## Client Benefits

- **Convenience**: Access datasources and pipes as attributes
- **Consistency**: All operations use the same pattern
- **Organization**: Keep definitions and client in dedicated modules

## Python App Integration

For Python web apps (FastAPI, Django, Flask), import from a dedicated module:

```python
# In your FastAPI app
from lib.client import tinybird

@app.get("/analytics")
async def get_analytics():
    result = tinybird.top_pages.query({"start_date": "2024-01-01", "end_date": "2024-01-31"})
    return result["data"]
```
```

## File: `skills/tinybird-python-sdk-guidelines/rules/configuration.md`
```markdown
# SDK Configuration

## Configuration File

Create a configuration file in your project root. Supported formats (in priority order):

1. `tinybird.config.py` - Python config with dynamic logic
2. `tinybird_config.py` - Python config alias
3. `tinybird.config.json` - Standard JSON (default)
4. `tinybird.json` - Legacy format

## JSON Configuration

```json
{
  "include": [
    "lib/*.py",
    "tinybird/**/*.datasource",
    "tinybird/**/*.pipe",
    "tinybird/**/*.connection"
  ],
  "token": "${TINYBIRD_TOKEN}",
  "base_url": "https://api.tinybird.co",
  "dev_mode": "branch"
}
```

## Python Configuration

```python
# tinybird.config.py
config = {
    "include": ["lib/*.py"],
    "token": "${TINYBIRD_TOKEN}",
    "base_url": "https://api.tinybird.co",
    "dev_mode": "branch",
}
```

For Python configs, export one of:
- `config` dict
- `CONFIG` dict
- `default` dict
- `get_config()` returning a dict

## Configuration Options

| Option | Type | Default | Description |
|--------|------|---------|-------------|
| `include` | `list[str]` | *required* | File paths or glob patterns for Python and raw datafiles |
| `token` | `str` | *required* | API token; supports `${ENV_VAR}` interpolation |
| `base_url` | `str` | `"https://api.tinybird.co"` | Tinybird API URL |
| `dev_mode` | `"branch"` \| `"local"` | `"branch"` | Development mode |

## Token Resolution

If `token` is omitted, SDK resolves from:
1. `TINYBIRD_TOKEN` environment variable
2. `.tinyb` file

## Base URL Resolution

If `base_url` is omitted, SDK resolves from:
1. `TINYBIRD_URL` environment variable
2. `TINYBIRD_HOST` environment variable
3. `.tinyb` file (`host` field)
4. Default: `https://api.tinybird.co`

## Mixed Formats

Combine Python files with legacy `.datasource`, `.pipe`, and `.connection` files:

```json
{
  "include": [
    "lib/datasources.py",
    "lib/pipes.py",
    "legacy/events.datasource",
    "legacy/analytics.pipe"
  ]
}
```

## Local Development Mode

Use a local Tinybird container:

1. Start the container:
   ```bash
   docker run -d -p 7181:7181 --name tinybird-local tinybirdco/tinybird-local:latest
   ```

2. Configure your project:
   ```json
   {
     "dev_mode": "local"
   }
   ```

   Or use CLI flag:
   ```bash
   tinybird dev --local
   ```
```

## File: `skills/tinybird-python-sdk-guidelines/rules/connections.md`
```markdown
# Defining Connections

Connections define external data sources that Tinybird can integrate with.

## Kafka Connection

```python
from tinybird_sdk import define_kafka_connection, secret

events_kafka = define_kafka_connection(
    "events_kafka",
    {
        "bootstrap_servers": "kafka.example.com:9092",
        "security_protocol": "SASL_SSL",
        "sasl_mechanism": "PLAIN",
        "key": secret("KAFKA_KEY"),
        "secret": secret("KAFKA_SECRET"),
    },
)
```

## S3 Connection

```python
from tinybird_sdk import define_s3_connection

landing_s3 = define_s3_connection(
    "landing_s3",
    {
        "region": "us-east-1",
        "arn": "arn:aws:iam::123456789012:role/tinybird-s3-access",
    },
)
```

## GCS Connection

```python
from tinybird_sdk import define_gcs_connection, secret

landing_gcs = define_gcs_connection(
    "landing_gcs",
    {
        "service_account_credentials_json": secret("GCS_SERVICE_ACCOUNT_CREDENTIALS_JSON"),
    },
)
```

## Using Secrets

The `secret()` function references secrets stored in Tinybird:

```python
from tinybird_sdk import secret

# Reference a secret by name
api_key = secret("MY_API_KEY")
```

Secrets must be created in Tinybird before deploying connections that use them.

## Connection Configuration Options

### Kafka Options

| Option | Description |
|--------|-------------|
| `bootstrap_servers` | Kafka broker addresses |
| `security_protocol` | Protocol (e.g., `SASL_SSL`, `PLAINTEXT`) |
| `sasl_mechanism` | SASL mechanism (e.g., `PLAIN`, `SCRAM-SHA-256`) |
| `key` | SASL username (use `secret()`) |
| `secret` | SASL password (use `secret()`) |

### S3 Options

| Option | Description |
|--------|-------------|
| `region` | AWS region |
| `arn` | IAM role ARN for cross-account access |

### GCS Options

| Option | Description |
|--------|-------------|
| `service_account_credentials_json` | Service account JSON (use `secret()`) |

## Using Connections in Sink Pipes

Connections are referenced when defining sink pipes:

```python
from tinybird_sdk import define_sink_pipe, node

kafka_sink = define_sink_pipe(
    "kafka_events_sink",
    {
        "sink": {
            "connection": events_kafka,  # Reference the connection
            "topic": "events_export",
            "schedule": "@on-demand",
        },
        "nodes": [
            node({"name": "publish", "sql": "SELECT * FROM events"})
        ],
    },
)
```
```

## File: `skills/tinybird-python-sdk-guidelines/rules/copy-sink-pipes.md`
```markdown
# Copy Pipes and Sink Pipes

## Copy Pipes

Copy pipes execute SQL and write results to a datasource on a schedule or on-demand.

### Scheduled Copy Pipe

```python
from tinybird_sdk import define_copy_pipe, node

daily_snapshot = define_copy_pipe(
    "daily_snapshot",
    {
        "datasource": events,  # Target datasource
        "copy_schedule": "0 0 * * *",  # Cron: daily at midnight
        "copy_mode": "append",
        "nodes": [
            node(
                {
                    "name": "snapshot",
                    "sql": """
                        SELECT today() AS snapshot_date, event_name, count() AS events
                        FROM events
                        WHERE toDate(timestamp) = today() - 1
                        GROUP BY event_name
                    """,
                }
            )
        ],
    },
)
```

### On-Demand Copy Pipe

```python
manual_report = define_copy_pipe(
    "manual_report",
    {
        "datasource": events,
        "copy_schedule": "@on-demand",
        "copy_mode": "replace",
        "nodes": [
            node(
                {
                    "name": "report",
                    "sql": "SELECT * FROM events WHERE timestamp >= now() - interval 7 day",
                }
            )
        ],
    },
)
```

### Copy Modes

| Mode | Description |
|------|-------------|
| `append` | Add rows to existing data (default) |
| `replace` | Replace all data in target datasource |

### Schedule Options

| Schedule | Description |
|----------|-------------|
| `"0 0 * * *"` | Cron expression (daily at midnight) |
| `"*/5 * * * *"` | Every 5 minutes |
| `"@on-demand"` | Manual trigger only |
| `"@once"` | Run once on deployment |

## Sink Pipes

Sink pipes publish query results to external systems (Kafka, S3).

### Kafka Sink

```python
from tinybird_sdk import define_sink_pipe, node

kafka_events_sink = define_sink_pipe(
    "kafka_events_sink",
    {
        "sink": {
            "connection": events_kafka,  # Kafka connection
            "topic": "events_export",
            "schedule": "@on-demand",
        },
        "nodes": [
            node(
                {
                    "name": "publish",
                    "sql": "SELECT timestamp, payload FROM kafka_events",
                }
            )
        ],
    },
)
```

### S3 Sink

```python
s3_events_sink = define_sink_pipe(
    "s3_events_sink",
    {
        "sink": {
            "connection": landing_s3,  # S3 connection
            "bucket_uri": "s3://my-bucket/exports/",
            "file_template": "events_{date}",
            "format": "csv",
            "schedule": "@once",
            "strategy": "create_new",
            "compression": "gzip",
        },
        "nodes": [
            node(
                {
                    "name": "export",
                    "sql": "SELECT timestamp, session_id FROM s3_landing",
                }
            )
        ],
    },
)
```

### S3 Sink Options

| Option | Description |
|--------|-------------|
| `bucket_uri` | S3 bucket and path prefix |
| `file_template` | Filename template (supports `{date}`, `{time}`) |
| `format` | Output format: `csv`, `json`, `parquet` |
| `schedule` | Cron expression or `@on-demand`, `@once` |
| `strategy` | `create_new` or `overwrite` |
| `compression` | `none`, `gzip`, `lz4` |
```

## File: `skills/tinybird-python-sdk-guidelines/rules/defining-datasources.md`
```markdown
# Defining Datasources

## Basic Datasource Definition

```python
from tinybird_sdk import define_datasource, t, engine

page_views = define_datasource(
    "page_views",
    {
        "description": "Page view tracking data",
        "schema": {
            "timestamp": t.date_time(),
            "pathname": t.string(),
            "session_id": t.string(),
            "country": t.string().low_cardinality().nullable(),
        },
        "engine": engine.merge_tree(
            {
                "sorting_key": ["pathname", "timestamp"],
            }
        ),
    },
)
```

## Schema Types

The `t` object provides type definitions:

### String Types
- `t.string()` - Variable-length string
- `t.fixed_string(n)` - Fixed-length string
- `t.uuid()` - UUID type

### Numeric Types
- `t.int32()`, `t.int64()` - Signed integers
- `t.uint32()`, `t.uint64()` - Unsigned integers
- `t.float32()`, `t.float64()` - Floating point
- `t.decimal(precision, scale)` - Decimal type

### Date/Time Types
- `t.date_time()` - DateTime type
- `t.date_time64(precision)` - DateTime64 with precision (0-9)
- `t.date()` - Date type

### Other Types
- `t.bool()` - Boolean type (stored as UInt8)
- `t.array(inner_type)` - Array of any type
- `t.map(key_type, value_type)` - Map/dictionary type

### Aggregate Types
- `t.simple_aggregate_function(func, inner_type)` - For summing merge tree
- `t.aggregate_function(func, inner_type)` - For aggregating merge tree

## Type Modifiers

Chain modifiers on types:

- `.nullable()` - Make column nullable
- `.low_cardinality()` - Use LowCardinality encoding for low-unique strings
- `.default(value)` - Set default value

Example:
```python
schema = {
    "tags": t.array(t.string()),
    "country": t.string().low_cardinality().nullable(),
    "score": t.float64().nullable(),
    "status": t.string().default("pending"),
}
```

## Engine Configuration

### MergeTree
```python
engine.merge_tree(
    {
        "sorting_key": ["column1", "column2"],
        "partition_key": "toYYYYMM(timestamp)",  # optional
        "ttl": "timestamp + INTERVAL 90 DAY",   # optional
    }
)
```

### ReplacingMergeTree
```python
engine.replacing_merge_tree(
    {
        "sorting_key": ["id"],
        "ver": "updated_at",
    }
)
```

### SummingMergeTree
```python
engine.summing_merge_tree(
    {
        "sorting_key": ["date", "category"],
        "columns": ["count", "total"],
    }
)
```

### AggregatingMergeTree
```python
engine.aggregating_merge_tree(
    {
        "sorting_key": ["date", "dimension"],
    }
)
```

## Schema Inference

Use the `infer` module to extract schemas:

```python
from tinybird_sdk.infer import infer_row_schema

row_schema = infer_row_schema(page_views)
# Returns dict with column names and types
```
```

## File: `skills/tinybird-python-sdk-guidelines/rules/defining-endpoints.md`
```markdown
# Defining Endpoints (Pipes)

## Basic Endpoint Definition

```python
from tinybird_sdk import define_endpoint, node, t, p

top_pages = define_endpoint(
    "top_pages",
    {
        "description": "Get the most visited pages",
        "params": {
            "start_date": p.date_time(),
            "end_date": p.date_time(),
            "limit": p.int32().optional(10),
        },
        "nodes": [
            node(
                {
                    "name": "aggregated",
                    "sql": """
                        SELECT pathname, count() AS views
                        FROM page_views
                        WHERE timestamp >= {{DateTime(start_date)}}
                          AND timestamp <= {{DateTime(end_date)}}
                        GROUP BY pathname
                        ORDER BY views DESC
                        LIMIT {{Int32(limit, 10)}}
                    """,
                }
            )
        ],
        "output": {
            "pathname": t.string(),
            "views": t.uint64(),
        },
    },
)
```

## Parameter Types

The `p` object provides parameter definitions:

- `p.string()` - String parameter
- `p.int32()`, `p.int64()` - Integer parameters
- `p.float32()`, `p.float64()` - Float parameters
- `p.date_time()` - DateTime parameter
- `p.date()` - Date parameter

## Parameter Modifiers

- `.optional(default_value)` - Make parameter optional with a default
- `.describe(text)` - Add description for documentation

Example:
```python
params = {
    "limit": p.int32().optional(10),
    "filter": p.string().optional(""),
    "status": p.string().optional("active").describe("Filter by status"),
}
```

## Internal Pipes (Non-API)

Use `define_pipe` for pipes not exposed as API endpoints:

```python
from tinybird_sdk import define_pipe, node, p

filtered_events = define_pipe(
    "filtered_events",
    {
        "description": "Filter events by date range",
        "params": {
            "start_date": p.date_time(),
            "end_date": p.date_time(),
        },
        "nodes": [
            node(
                {
                    "name": "filtered",
                    "sql": """
                        SELECT * FROM events
                        WHERE timestamp >= {{DateTime(start_date)}}
                          AND timestamp <= {{DateTime(end_date)}}
                    """,
                }
            )
        ],
    },
)
```

## Multi-Node Pipes

Define multiple nodes for complex transformations:

```python
nodes = [
    node(
        {
            "name": "filtered",
            "sql": """
                SELECT * FROM events
                WHERE timestamp >= {{DateTime(start_date)}}
            """,
        }
    ),
    node(
        {
            "name": "aggregated",
            "sql": """
                SELECT date, count() as total
                FROM filtered
                GROUP BY date
            """,
        }
    ),
]
```

## SQL Templating

Use Tinybird templating in SQL:

- `{{Type(param_name)}}` - Parameter with type
- `{{Type(param_name, default)}}` - Parameter with default value

```sql
WHERE user_id = {{String(user_id)}}
AND date >= {{Date(start_date, '2024-01-01')}}
LIMIT {{Int32(limit, 100)}}
```

## Schema Inference

```python
from tinybird_sdk.infer import infer_params_schema, infer_output_schema

params_schema = infer_params_schema(top_pages)
output_schema = infer_output_schema(top_pages)
```
```

## File: `skills/tinybird-python-sdk-guidelines/rules/getting-started.md`
```markdown
# Tinybird Python SDK Overview

## What is it

The `tinybird-sdk` is a Python package that enables developers to define Tinybird resources in Python. You can author datasources, pipes, connections, and queries in Python, then synchronize them directly to Tinybird.

## Requirements

- Python: Version 3.11 or higher
- Server-side only; web browsers are not supported to protect API credentials

## Installation

```bash
pip install tinybird-sdk
```

## Project Initialization

```bash
tinybird init
tinybird init --force          # Overwrite existing files
tinybird init --skip-login     # Skip browser authentication
```

This generates:
- `tinybird.config.json` - Configuration file
- `lib/datasources.py` - Data source definitions
- `lib/pipes.py` - Pipe/endpoint definitions
- `lib/client.py` - Tinybird client module

## Environment Setup

Create `.env.local`:
```
TINYBIRD_TOKEN=p.your_token_here
```

## Key Features

- Define datasources, pipes, and endpoints in Python
- Data ingestion with automatic schema validation
- Query endpoints with typed results
- Mixed formats: combine Python with legacy `.datasource`/`.pipe` files
- Branch safety: dev mode blocks deployment to main branch
- Connections: Kafka, S3, GCS integrations
- Materialized views for real-time aggregations
- Copy pipes and sink pipes for data workflows
```

## File: `skills/tinybird-python-sdk-guidelines/rules/low-level-api.md`
```markdown
# Public Tinybird API (Low-Level)

For cases requiring a decoupled API wrapper without the high-level client:

## Creating the API Client

```python
from tinybird_sdk import create_tinybird_api

api = create_tinybird_api(
    {
        "base_url": "https://api.tinybird.co",
        "token": "p.your_token",
    }
)
```

## Querying Endpoints

```python
top_pages = api.query(
    "top_pages",
    {
        "start_date": "2024-01-01",
        "end_date": "2024-01-31",
        "limit": 5,
    },
)

# top_pages["data"] contains the result rows
```

## Ingesting Data

```python
# Ingest one row
api.ingest(
    "events",
    {
        "timestamp": "2024-01-15 10:30:00",
        "event_name": "page_view",
        "pathname": "/home",
    },
)

# Batch ingestion
api.ingest(
    "events",
    [
        {"timestamp": "2024-01-15 10:30:00", "event_name": "page_view", "pathname": "/home"},
        {"timestamp": "2024-01-15 10:31:00", "event_name": "click", "pathname": "/home"},
    ],
)
```

## Retry Behavior

Retries are disabled by default. Enable with `max_retries`:

```python
api.ingest(
    "events",
    {"timestamp": "2024-01-15 10:31:00", "event_name": "button_click", "pathname": "/pricing"},
    {"max_retries": 3},
)
```

- 429 retries use `Retry-After` / `X-RateLimit-Reset` headers
- 503 retries use SDK default exponential backoff

## Datasource Operations

### Append from URL
```python
api.append_datasource(
    "events",
    {"url": "https://example.com/events.csv"},
)
```

### Delete Rows
```python
api.delete_datasource(
    "events",
    {"delete_condition": "event_name = 'test'"},
)

# Dry run
api.delete_datasource(
    "events",
    {"delete_condition": "event_name = 'test'", "dry_run": True},
)
```

### Truncate
```python
api.truncate_datasource("events")
```

## Executing Raw SQL

```python
sql_result = api.sql("SELECT count() AS total FROM events")
# sql_result["data"][0]["total"]
```

## Per-Request Token Override

```python
workspace_response = api.request_json(
    "/v1/workspace",
    token="p.branch_or_jwt_token",
)
```

## When to Use Low-Level API

- Existing projects not using Python definitions
- Dynamic endpoint names or parameters
- Direct SQL execution needs
- Gradual migration from other HTTP clients
- Multi-tenant scenarios with different tokens
```

## File: `skills/tinybird-python-sdk-guidelines/rules/materialized-views.md`
```markdown
# Materialized Views

Materialized views automatically aggregate data as it arrives, enabling real-time analytics.

## Basic Materialized View

A materialized view consists of:
1. A target datasource with aggregate columns
2. A materialized view definition that populates it

```python
from tinybird_sdk import define_datasource, define_materialized_view, engine, node, t

# Target datasource with aggregate columns
daily_stats = define_datasource(
    "daily_stats",
    {
        "schema": {
            "date": t.date(),
            "pathname": t.string(),
            "views": t.simple_aggregate_function("sum", t.uint64()),
            "unique_sessions": t.aggregate_function("uniq", t.string()),
        },
        "engine": engine.aggregating_merge_tree({"sorting_key": ["date", "pathname"]}),
    },
)

# Materialized view that populates it
daily_stats_mv = define_materialized_view(
    "daily_stats_mv",
    {
        "datasource": daily_stats,
        "nodes": [
            node(
                {
                    "name": "aggregate",
                    "sql": """
                        SELECT
                          toDate(timestamp) AS date,
                          pathname,
                          count() AS views,
                          uniqState(session_id) AS unique_sessions
                        FROM page_views
                        GROUP BY date, pathname
                    """,
                }
            )
        ],
    },
)
```

## Aggregate Types

### SimpleAggregateFunction

For simple aggregations (sum, min, max, any):

```python
"views": t.simple_aggregate_function("sum", t.uint64())
"min_value": t.simple_aggregate_function("min", t.float64())
"max_value": t.simple_aggregate_function("max", t.float64())
```

### AggregateFunction

For complex aggregations (uniq, quantile, etc.):

```python
"unique_users": t.aggregate_function("uniq", t.string())
"p95_latency": t.aggregate_function("quantile(0.95)", t.float64())
```

## SQL State Functions

In materialized view SQL, use state functions to prepare aggregates:

| Final Function | State Function |
|----------------|----------------|
| `count()` | `count()` (no state needed for SimpleAggregateFunction) |
| `sum(col)` | `sum(col)` (no state needed) |
| `uniq(col)` | `uniqState(col)` |
| `quantile(0.95)(col)` | `quantileState(0.95)(col)` |
| `avg(col)` | `avgState(col)` |

## Querying Materialized Views

When querying, use merge functions for AggregateFunction columns:

```python
endpoint = define_endpoint(
    "daily_stats_query",
    {
        "nodes": [
            node(
                {
                    "name": "query",
                    "sql": """
                        SELECT
                          date,
                          pathname,
                          sum(views) AS total_views,
                          uniqMerge(unique_sessions) AS unique_sessions
                        FROM daily_stats
                        GROUP BY date, pathname
                    """,
                }
            )
        ],
        "output": {
            "date": t.date(),
            "pathname": t.string(),
            "total_views": t.uint64(),
            "unique_sessions": t.uint64(),
        },
    },
)
```

## Engine Selection

Always use `aggregating_merge_tree` for materialized view targets:

```python
engine.aggregating_merge_tree(
    {
        "sorting_key": ["date", "dimension1", "dimension2"],
    }
)
```
```

## File: `skills/tinybird-python-sdk-guidelines/rules/tokens.md`
```markdown
# Tokens

## Static Tokens

Define named tokens and attach them to datasources and endpoints:

```python
from tinybird_sdk import define_datasource, define_endpoint, define_token, node, t

# Define tokens
app_token = define_token("app_read")
ingest_token = define_token("ingest_token")

# Attach to datasource
events = define_datasource(
    "events",
    {
        "schema": {
            "timestamp": t.date_time(),
            "event_name": t.string(),
        },
        "tokens": [
            {"token": app_token, "scope": "READ"},
            {"token": ingest_token, "scope": "APPEND"},
        ],
    },
)

# Attach to endpoint
top_events = define_endpoint(
    "top_events",
    {
        "nodes": [node({"name": "endpoint", "sql": "SELECT * FROM events LIMIT 10"})],
        "output": {"timestamp": t.date_time(), "event_name": t.string()},
        "tokens": [{"token": app_token, "scope": "READ"}],
    },
)
```

### Token Scopes

| Scope | Description |
|-------|-------------|
| `READ` | Read access |
| `APPEND` | Append/ingest access |

## JWT Token Creation

Create short-lived JWT tokens for secure scoped access:

```python
from datetime import datetime, timedelta, timezone
from tinybird_sdk import create_client

client = create_client(
    {
        "base_url": "https://api.tinybird.co",
        "token": "p.your_admin_token",
    }
)

result = client.tokens.create_jwt(
    {
        "name": "user_123_session",
        "expires_at": datetime.now(tz=timezone.utc) + timedelta(hours=1),
        "scopes": [
            {
                "type": "PIPES:READ",
                "resource": "user_dashboard",
                "fixed_params": {"user_id": 123},
            }
        ],
        "limits": {"rps": 10},
    }
)

jwt_token = result["token"]
```

### JWT Scope Types

| Scope | Description |
|-------|-------------|
| `PIPES:READ` | Read access to a specific pipe endpoint |
| `DATASOURCES:READ` | Read access to a datasource |
| `DATASOURCES:APPEND` | Append access to a datasource |

### JWT Scope Options

| Option | Description |
|--------|-------------|
| `resource` | Name of the pipe or datasource |
| `fixed_params` | Parameters embedded in token (cannot be overridden) |
| `filter` | SQL WHERE clause for datasource filtering |

### Example: Multi-Tenant Access

```python
# Create token for specific organization
org_token = client.tokens.create_jwt(
    {
        "name": "org_acme_access",
        "expires_at": datetime.now(tz=timezone.utc) + timedelta(days=1),
        "scopes": [
            {
                "type": "DATASOURCES:READ",
                "resource": "events",
                "filter": "org_id = 'acme'",
            },
            {
                "type": "PIPES:READ",
                "resource": "analytics_dashboard",
                "fixed_params": {"org_id": "acme"},
            },
        ],
        "limits": {"rps": 100},
    }
)
```

### JWT Limits

| Option | Description |
|--------|-------------|
| `rps` | Requests per second limit |
```

## File: `skills/tinybird-typescript-sdk-guidelines/SKILL.md`
```markdown
---
name: tinybird-typescript-sdk-guidelines
description: Tinybird TypeScript SDK for defining datasources, pipes, and queries with full type inference. Use when working with @tinybirdco/sdk, TypeScript Tinybird projects, or type-safe data ingestion and queries.
---

# Tinybird TypeScript SDK Guidelines

Guidance for using the `@tinybirdco/sdk` package to define Tinybird resources in TypeScript with complete type inference.

## When to Apply

- Installing or configuring @tinybirdco/sdk
- Defining datasources or pipes in TypeScript
- Creating typed Tinybird clients
- Using type-safe ingestion or queries
- Running tinybird dev/build/deploy commands for TypeScript projects
- Migrating from legacy .datasource/.pipe files to TypeScript
- Defining connections (Kafka, S3, GCS)
- Creating materialized views, copy pipes, or sink pipes

## Rule Files

- `rules/getting-started.md`
- `rules/configuration.md`
- `rules/defining-datasources.md`
- `rules/defining-endpoints.md`
- `rules/typed-client.md`
- `rules/low-level-api.md`
- `rules/cli-commands.md`
- `rules/connections.md`
- `rules/materialized-views.md`
- `rules/copy-sink-pipes.md`
- `rules/tokens.md`

## Quick Reference

- Install: `npm install @tinybirdco/sdk`
- Initialize: `npx tinybird init`
- Dev mode: `tinybird dev` (uses configured `devMode`, typically branch)
- Build: `tinybird build` (builds against configured dev target)
- Deploy: `tinybird deploy` (deploys to main/production)
- Preview in CI: `tinybird preview`
- Server-side only; never expose tokens in browsers
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/cli-commands.md`
```markdown
# SDK CLI Commands

The SDK includes CLI commands for development, preview, and deployment workflows.

## CLI 4.0 Build/Deploy Model

- Configure your default development target once in `tinybird.config.*` (`devMode`).
- Run `tinybird build` without environment flags for normal workflows.
- Run `tinybird deploy` to publish to Tinybird Cloud main.
- Use `--local`/`--branch` only as explicit overrides.

## tinybird init

Initialize a new TypeScript Tinybird project:

```bash
npx tinybird init
npx tinybird init --force          # Overwrite existing files
npx tinybird init --skip-login     # Skip browser authentication
```

Detects existing `.datasource` and `.pipe` files for incremental migration.

## tinybird migrate

Migrate legacy datafiles to TypeScript definitions:

```bash
tinybird migrate "tinybird/**/*.datasource" "tinybird/**/*.pipe" "tinybird/**/*.connection"
tinybird migrate tinybird/legacy --out ./tinybird.migration.ts
tinybird migrate tinybird --dry-run
```

Converts `.datasource`, `.pipe`, and `.connection` files into a TypeScript definitions file.

## tinybird dev

Watch schema files and auto-sync to Tinybird:

```bash
tinybird dev                       # Watch and sync using configured devMode
tinybird dev --local               # Sync with local container
tinybird dev --branch              # Force branch mode for this run
```

**Important**: In branch mode, feature branches are expected; main/master are blocked to prevent accidental production changes.

## tinybird build

Build and validate resources using your configured development target:

```bash
tinybird build                     # Build to devMode target (branch or local)
tinybird build --dry-run           # Preview build operations
tinybird build --local             # Build to local container
tinybird build --branch            # Build to branch for this run
```

Use `tinybird build` for iterative development; it does not publish to production.

## tinybird deploy

Deploy resources to the main workspace (production):

```bash
tinybird deploy                    # Deploy to main/production
tinybird deploy --dry-run          # Preview without deploying
tinybird deploy --check            # Validate without applying changes
tinybird deploy --wait             # Wait for deployment completion
tinybird deploy --allow-destructive-operations  # Allow breaking changes
```

This is the only way to deploy to main.

## tinybird preview

Create or refresh a CI preview environment for the current branch:

```bash
tinybird preview
```

Use this in pull request workflows so preview apps query isolated Tinybird preview branches.

## tinybird pull

Download cloud resources as native datafiles:

```bash
tinybird pull                      # Pull to default location
tinybird pull --output-dir ./tinybird-datafiles
tinybird pull --force              # Overwrite existing files
```

## tinybird login

Authenticate via browser:

```bash
tinybird login
```

Useful for existing projects or token refresh.

## tinybird branch

Manage branches:

```bash
tinybird branch list               # List all branches
tinybird branch status             # Show current branch status
tinybird branch delete <name>      # Delete a branch
```

## tinybird info

Display workspace, local, and project configuration:

```bash
tinybird info                      # Show configuration
tinybird info --json               # Output as JSON
```

## Development Workflow

1. `npx tinybird init` - Initialize project
2. Define datasources and pipes in TypeScript
3. `tinybird build` or `tinybird dev` - Iterate against configured dev target
4. `tinybird preview` in CI - Create preview branch environment per PR
5. `tinybird deploy` - Deploy to production after merge

## Important Notes

- The CLI auto-generates datafiles from TypeScript definitions before `build`, `deploy`, and `preview`
- Use `--check`/`--dry-run` before production deploys when in doubt
- The SDK CLI is separate from the `tb` CLI but complementary
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/configuration.md`
```markdown
# SDK Configuration

## Configuration File

Create a configuration file in your project root. Supported formats (in priority order):

1. `tinybird.config.mjs` - ESM with dynamic logic
2. `tinybird.config.cjs` - CommonJS with dynamic logic
3. `tinybird.config.json` - Standard JSON (default)
4. `tinybird.json` - Legacy format

## Configuration Options

```json
{
  "include": [
    "src/tinybird/datasources.ts",
    "src/tinybird/pipes.ts",
    "src/tinybird/legacy.datasource",
    "src/tinybird/legacy.pipe"
  ],
  "token": "${TINYBIRD_TOKEN}",
  "baseUrl": "https://api.tinybird.co",
  "devMode": "branch"
}
```

## Configuration Fields

- `include`: Array of file paths to include (TypeScript files and legacy `.datasource`/`.pipe` files)
- `token`: API token, supports environment variable interpolation with `${VAR_NAME}`
- `baseUrl`: Tinybird API base URL
- `devMode`: Development mode (`branch` for cloud branches, `local` for local container)

## Mixed Formats

You can combine TypeScript files with legacy `.datasource` and `.pipe` files for gradual migration:

```json
{
  "include": [
    "src/tinybird/datasources.ts",
    "src/tinybird/pipes.ts",
    "legacy/events.datasource",
    "legacy/analytics.pipe"
  ]
}
```

## Path Alias Configuration

Add to `tsconfig.json` for cleaner imports:

```json
{
  "compilerOptions": {
    "paths": {
      "@tinybird/client": ["./src/tinybird/client.ts"]
    }
  }
}
```
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/connections.md`
```markdown
# Defining Connections

Connections define external data sources that Tinybird can integrate with.

## Kafka Connection

```typescript
import { defineKafkaConnection, secret } from "@tinybirdco/sdk";

export const eventsKafka = defineKafkaConnection("events_kafka", {
  bootstrapServers: "kafka.example.com:9092",
  securityProtocol: "SASL_SSL",
  saslMechanism: "PLAIN",
  key: secret("KAFKA_KEY"),
  secret: secret("KAFKA_SECRET"),
});
```

## S3 Connection

```typescript
import { defineS3Connection } from "@tinybirdco/sdk";

export const landingS3 = defineS3Connection("landing_s3", {
  region: "us-east-1",
  arn: "arn:aws:iam::123456789012:role/tinybird-s3-access",
});
```

## GCS Connection

```typescript
import { defineGCSConnection, secret } from "@tinybirdco/sdk";

export const landingGCS = defineGCSConnection("landing_gcs", {
  serviceAccountCredentialsJson: secret("GCS_SERVICE_ACCOUNT_CREDENTIALS_JSON"),
});
```

## Using Secrets

The `secret()` function references secrets stored in Tinybird:

```typescript
import { secret } from "@tinybirdco/sdk";

// Reference a secret by name
const apiKey = secret("MY_API_KEY");
```

Secrets must be created in Tinybird before deploying connections that use them.

## Using Connections in Datasources

```typescript
import { defineDatasource, t, engine } from "@tinybirdco/sdk";
import { eventsKafka, landingS3, landingGCS } from "./connections";

// Kafka datasource
export const kafkaEvents = defineDatasource("kafka_events", {
  schema: {
    timestamp: t.dateTime(),
    payload: t.string(),
  },
  engine: engine.mergeTree({ sortingKey: ["timestamp"] }),
  kafka: {
    connection: eventsKafka,
    topic: "events",
    groupId: "events-consumer",
    autoOffsetReset: "earliest",
  },
});

// S3 datasource
export const s3Landing = defineDatasource("s3_landing", {
  schema: {
    timestamp: t.dateTime(),
    session_id: t.string(),
  },
  engine: engine.mergeTree({ sortingKey: ["timestamp"] }),
  s3: {
    connection: landingS3,
    bucketUri: "s3://my-bucket/events/*.csv",
    schedule: "@auto",
  },
});

// GCS datasource
export const gcsLanding = defineDatasource("gcs_landing", {
  schema: {
    timestamp: t.dateTime(),
    session_id: t.string(),
  },
  engine: engine.mergeTree({ sortingKey: ["timestamp"] }),
  gcs: {
    connection: landingGCS,
    bucketUri: "gs://my-gcs-bucket/events/*.csv",
    schedule: "@auto",
  },
});
```
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/copy-sink-pipes.md`
```markdown
# Copy Pipes and Sink Pipes

## Copy Pipes

Copy pipes execute SQL and write results to a datasource on a schedule or on-demand.

### Scheduled Copy Pipe

```typescript
import { defineCopyPipe, node } from "@tinybirdco/sdk";

export const dailySnapshot = defineCopyPipe("daily_snapshot", {
  description: "Daily snapshot of statistics",
  datasource: snapshotDatasource, // Target datasource
  schedule: "0 0 * * *", // Cron: daily at midnight
  mode: "append",
  nodes: [
    node({
      name: "snapshot",
      sql: `
        SELECT today() AS snapshot_date, pathname, count() AS views
        FROM page_views
        WHERE toDate(timestamp) = today() - 1
        GROUP BY pathname
      `,
    }),
  ],
});
```

### On-Demand Copy Pipe

```typescript
export const manualReport = defineCopyPipe("manual_report", {
  description: "On-demand report generation",
  datasource: reportDatasource,
  schedule: "@on-demand",
  mode: "replace",
  nodes: [
    node({
      name: "report",
      sql: `SELECT * FROM events WHERE timestamp >= now() - interval 7 day`,
    }),
  ],
});
```

### Copy Modes

| Mode | Description |
|------|-------------|
| `append` | Add rows to existing data (default) |
| `replace` | Replace all data in target datasource |

### Schedule Options

| Schedule | Description |
|----------|-------------|
| `"0 0 * * *"` | Cron expression (daily at midnight) |
| `"*/5 * * * *"` | Every 5 minutes |
| `"@on-demand"` | Manual trigger only |
| `"@once"` | Run once on deployment |

## Sink Pipes

Sink pipes publish query results to external systems (Kafka, S3).

### Kafka Sink

```typescript
import { defineSinkPipe, node } from "@tinybirdco/sdk";
import { eventsKafka } from "./connections";

export const kafkaEventsSink = defineSinkPipe("kafka_events_sink", {
  sink: {
    connection: eventsKafka,
    topic: "events_export",
    schedule: "@on-demand",
  },
  nodes: [
    node({
      name: "publish",
      sql: `SELECT timestamp, payload FROM kafka_events`,
    }),
  ],
});
```

### S3 Sink

```typescript
import { defineSinkPipe, node } from "@tinybirdco/sdk";
import { landingS3 } from "./connections";

export const s3EventsSink = defineSinkPipe("s3_events_sink", {
  sink: {
    connection: landingS3,
    bucketUri: "s3://my-bucket/exports/",
    fileTemplate: "events_{date}",
    format: "csv",
    schedule: "@once",
    strategy: "create_new",
    compression: "gzip",
  },
  nodes: [
    node({
      name: "export",
      sql: `SELECT timestamp, session_id FROM s3_landing`,
    }),
  ],
});
```

### S3 Sink Options

| Option | Description |
|--------|-------------|
| `bucketUri` | S3 bucket and path prefix |
| `fileTemplate` | Filename template (supports `{date}`, `{time}`) |
| `format` | Output format: `csv`, `json`, `parquet` |
| `schedule` | Cron expression or `@on-demand`, `@once` |
| `strategy` | `create_new` or `overwrite` |
| `compression` | `none`, `gzip`, `lz4` |
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/defining-datasources.md`
```markdown
# Defining Datasources

## Basic Datasource Definition

```typescript
import { defineDatasource, t, engine, type InferRow } from "@tinybirdco/sdk";

export const pageViews = defineDatasource("page_views", {
  description: "Page view tracking data",
  schema: {
    timestamp: t.dateTime(),
    pathname: t.string(),
    session_id: t.string(),
    country: t.string().lowCardinality().nullable(),
  },
  engine: engine.mergeTree({
    sortingKey: ["pathname", "timestamp"],
  }),
});

export type PageViewsRow = InferRow<typeof pageViews>;
```

## Schema Types

The `t` object provides type definitions:

- `t.string()` - String type
- `t.int32()`, `t.int64()`, `t.uint32()`, `t.uint64()` - Integer types
- `t.float32()`, `t.float64()` - Float types
- `t.dateTime()` - DateTime type
- `t.date()` - Date type
- `t.boolean()` - Boolean type (stored as UInt8)

## Type Modifiers

Chain modifiers on types:

- `.nullable()` - Make column nullable
- `.lowCardinality()` - Use LowCardinality encoding for low-unique strings
- `.array()` - Array of the type

Example:
```typescript
schema: {
  tags: t.string().array(),
  country: t.string().lowCardinality().nullable(),
  score: t.float64().nullable(),
}
```

## Engine Configuration

```typescript
engine: engine.mergeTree({
  sortingKey: ["column1", "column2"],
  partitionKey: "toYYYYMM(timestamp)",  // optional
})
```

For aggregating materialized views:
```typescript
engine: engine.aggregatingMergeTree({
  sortingKey: ["date", "dimension"],
})
```

## Type Inference

Use `InferRow` to extract the TypeScript type from a datasource:

```typescript
export type PageViewsRow = InferRow<typeof pageViews>;
// Results in: { timestamp: Date; pathname: string; session_id: string; country: string | null }
```
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/defining-endpoints.md`
```markdown
# Defining Endpoints (Pipes)

## Basic Endpoint Definition

```typescript
import {
  defineEndpoint, node, t, p,
  type InferParams,
  type InferOutputRow
} from "@tinybirdco/sdk";

export const topPages = defineEndpoint("top_pages", {
  description: "Get the most visited pages",
  params: {
    start_date: p.dateTime(),
    end_date: p.dateTime(),
    limit: p.int32().optional(10),
  },
  nodes: [
    node({
      name: "aggregated",
      sql: `
        SELECT pathname, count() AS views
        FROM page_views
        WHERE timestamp >= {{DateTime(start_date)}}
        AND timestamp <= {{DateTime(end_date)}}
        GROUP BY pathname
        ORDER BY views DESC
        LIMIT {{Int32(limit, 10)}}
      `,
    }),
  ],
  output: {
    pathname: t.string(),
    views: t.uint64(),
  },
});

export type TopPagesParams = InferParams<typeof topPages>;
export type TopPagesOutput = InferOutputRow<typeof topPages>;
```

## Parameter Types

The `p` object provides parameter definitions:

- `p.string()` - String parameter
- `p.int32()`, `p.int64()` - Integer parameters
- `p.float32()`, `p.float64()` - Float parameters
- `p.dateTime()` - DateTime parameter
- `p.date()` - Date parameter

## Parameter Modifiers

- `.optional(defaultValue)` - Make parameter optional with a default value

Example:
```typescript
params: {
  limit: p.int32().optional(10),
  filter: p.string().optional(""),
}
```

## Multi-Node Pipes

Define multiple nodes for complex transformations:

```typescript
nodes: [
  node({
    name: "filtered",
    sql: `
      SELECT * FROM events
      WHERE timestamp >= {{DateTime(start_date)}}
    `,
  }),
  node({
    name: "aggregated",
    sql: `
      SELECT date, count() as total
      FROM filtered
      GROUP BY date
    `,
  }),
],
```

## SQL Templating

Use Tinybird templating in SQL:

- `{{Type(param_name)}}` - Parameter with type
- `{{Type(param_name, default)}}` - Parameter with default value

```sql
WHERE user_id = {{String(user_id)}}
AND date >= {{Date(start_date, '2024-01-01')}}
LIMIT {{Int32(limit, 100)}}
```

## Type Inference

```typescript
export type TopPagesParams = InferParams<typeof topPages>;
// Results in: { start_date: Date; end_date: Date; limit?: number }

export type TopPagesOutput = InferOutputRow<typeof topPages>;
// Results in: { pathname: string; views: bigint }
```
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/getting-started.md`
```markdown
# Tinybird TypeScript SDK Overview

## What is it

The `@tinybirdco/sdk` is a TypeScript package that enables developers to define Tinybird resources with complete type inference. You can author datasources, pipes, and queries in TypeScript, then synchronize them directly to Tinybird.

## Requirements

- TypeScript: Version 4.9 or higher
- Node.js: 20 LTS or later (non-EOL versions officially supported)
- Server-side only; web browsers are not supported to protect API credentials

## Installation

```bash
npm install @tinybirdco/sdk
```

## Project Initialization

```bash
npx tinybird init
npx tinybird init --force          # Overwrite existing files
npx tinybird init --skip-login     # Skip browser authentication
```

This generates:
- `tinybird.config.json` - Configuration file
- `src/tinybird/datasources.ts` - Data source definitions
- `src/tinybird/pipes.ts` - Pipe/endpoint definitions
- `src/tinybird/client.ts` - Typed client

## Environment Setup

Create `.env.local`:
```
TINYBIRD_TOKEN=p.your_token_here
```

## Key Features

- Full type inference with autocomplete for datasources and pipes
- Type-safe data ingestion catching schema mismatches at development time
- Typed query results based on endpoint definitions
- Mixed formats: combine TypeScript with legacy `.datasource`/`.pipe` files
- Branch safety: dev mode blocks deployment to main branch
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/low-level-api.md`
```markdown
# Public Tinybird API (Low-Level)

For cases requiring a decoupled API wrapper without the typed client:

## Creating the API Client

```typescript
import { createTinybirdApi } from "@tinybirdco/sdk";

const api = createTinybirdApi({
  baseUrl: "https://api.tinybird.co",
  token: process.env.TINYBIRD_TOKEN!,
});
```

## Querying Endpoints

```typescript
interface TopPagesRow { pathname: string; visits: number }
interface TopPagesParams { start_date: string; end_date: string; limit?: number }

const topPages = await api.query<TopPagesRow, TopPagesParams>("top_pages", {
  start_date: "2024-01-01",
  end_date: "2024-01-31",
  limit: 5,
});

// topPages.data is typed as TopPagesRow[]
```

## Ingesting Data

```typescript
interface EventRow { timestamp: Date; event_name: string; pathname: string }

await api.ingest<EventRow>("events", {
  timestamp: new Date(),
  event_name: "page_view",
  pathname: "/home",
});

// Batch ingestion
await api.ingest<EventRow>("events", [
  { timestamp: new Date(), event_name: "page_view", pathname: "/home" },
  { timestamp: new Date(), event_name: "click", pathname: "/home" },
]);
```

## Executing Raw SQL

```typescript
interface CountResult { total: number }

const sqlResult = await api.sql<CountResult>(
  "SELECT count() AS total FROM events"
);

// sqlResult.data[0].total
```

## Per-Request Token Override

```typescript
await api.request("/v1/workspace", {
  token: process.env.TINYBIRD_BRANCH_TOKEN,
});
```

## When to Use Low-Level API

- Existing projects not using TypeScript definitions
- Dynamic endpoint names or parameters
- Direct SQL execution needs
- Gradual migration from other HTTP clients
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/materialized-views.md`
```markdown
# Materialized Views

Materialized views automatically aggregate data as it arrives, enabling real-time analytics.

## Basic Materialized View

A materialized view consists of:
1. A target datasource with aggregate columns
2. A materialized view definition that populates it

```typescript
import { defineDatasource, defineMaterializedView, t, engine, node } from "@tinybirdco/sdk";

// Target datasource with aggregate columns
export const dailyStats = defineDatasource("daily_stats", {
  description: "Daily aggregated statistics",
  schema: {
    date: t.date(),
    pathname: t.string(),
    views: t.simpleAggregateFunction("sum", t.uint64()),
    unique_sessions: t.aggregateFunction("uniq", t.string()),
  },
  engine: engine.aggregatingMergeTree({
    sortingKey: ["date", "pathname"],
  }),
});

// Materialized view that populates it
export const dailyStatsMv = defineMaterializedView("daily_stats_mv", {
  description: "Materialize daily page view aggregations",
  datasource: dailyStats,
  nodes: [
    node({
      name: "aggregate",
      sql: `
        SELECT
          toDate(timestamp) AS date,
          pathname,
          count() AS views,
          uniqState(session_id) AS unique_sessions
        FROM page_views
        GROUP BY date, pathname
      `,
    }),
  ],
});
```

## Aggregate Types

### SimpleAggregateFunction

For simple aggregations (sum, min, max, any):

```typescript
views: t.simpleAggregateFunction("sum", t.uint64()),
minValue: t.simpleAggregateFunction("min", t.float64()),
maxValue: t.simpleAggregateFunction("max", t.float64()),
```

### AggregateFunction

For complex aggregations (uniq, quantile, etc.):

```typescript
uniqueUsers: t.aggregateFunction("uniq", t.string()),
p95Latency: t.aggregateFunction("quantile(0.95)", t.float64()),
```

## SQL State Functions

In materialized view SQL, use state functions to prepare aggregates:

| Final Function | State Function |
|----------------|----------------|
| `count()` | `count()` (no state needed for SimpleAggregateFunction) |
| `sum(col)` | `sum(col)` (no state needed) |
| `uniq(col)` | `uniqState(col)` |
| `quantile(0.95)(col)` | `quantileState(0.95)(col)` |
| `avg(col)` | `avgState(col)` |

## Querying Materialized Views

When querying, use merge functions for AggregateFunction columns:

```typescript
const endpoint = defineEndpoint("daily_stats_query", {
  nodes: [
    node({
      name: "query",
      sql: `
        SELECT
          date,
          pathname,
          sum(views) AS total_views,
          uniqMerge(unique_sessions) AS unique_sessions
        FROM daily_stats
        GROUP BY date, pathname
      `,
    }),
  ],
  output: {
    date: t.date(),
    pathname: t.string(),
    total_views: t.uint64(),
    unique_sessions: t.uint64(),
  },
});
```

## Engine Selection

Always use `aggregatingMergeTree` for materialized view targets:

```typescript
engine.aggregatingMergeTree({
  sortingKey: ["date", "dimension1", "dimension2"],
});
```
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/tokens.md`
```markdown
# Tokens

## Static Tokens

Define named tokens and attach them to datasources and endpoints:

```typescript
import { defineToken, defineDatasource, defineEndpoint, t, node } from "@tinybirdco/sdk";

// Define tokens
const appToken = defineToken("app_read");
const ingestToken = defineToken("ingest_token");

// Attach to datasource
export const events = defineDatasource("events", {
  schema: {
    timestamp: t.dateTime(),
    event_name: t.string(),
  },
  tokens: [
    { token: appToken, scope: "READ" },
    { token: ingestToken, scope: "APPEND" },
  ],
});

// Attach to endpoint
export const topEvents = defineEndpoint("top_events", {
  nodes: [node({ name: "endpoint", sql: "SELECT * FROM events LIMIT 10" })],
  output: { timestamp: t.dateTime(), event_name: t.string() },
  tokens: [{ token: appToken, scope: "READ" }],
});
```

### Token Scopes

| Resource | Available Scopes |
|----------|-----------------|
| Datasources | `READ`, `APPEND` |
| Pipes/Endpoints | `READ` |

## JWT Token Creation

Create short-lived JWT tokens for secure scoped access. Useful for:
- Frontend applications calling Tinybird APIs directly
- Multi-tenant applications with row-level security
- Time-limited access with automatic expiration

```typescript
import { createClient } from "@tinybirdco/sdk";

const client = createClient({
  baseUrl: "https://api.tinybird.co",
  token: process.env.TINYBIRD_ADMIN_TOKEN!, // Requires ADMIN scope
});

const { token } = await client.tokens.createJWT({
  name: "user_123_session",
  expiresAt: new Date(Date.now() + 60 * 60 * 1000), // 1 hour
  scopes: [
    {
      type: "PIPES:READ",
      resource: "user_dashboard",
      fixed_params: { user_id: 123 },
    },
  ],
  limits: { rps: 10 },
});

// Use the JWT for client-side queries
const userClient = createClient({
  baseUrl: "https://api.tinybird.co",
  token, // The JWT
});
```

### JWT Scope Types

| Scope | Description |
|-------|-------------|
| `PIPES:READ` | Read access to a specific pipe endpoint |
| `DATASOURCES:READ` | Read access to a datasource |
| `DATASOURCES:APPEND` | Append access to a datasource |

### JWT Scope Options

| Option | Description |
|--------|-------------|
| `resource` | Name of the pipe or datasource |
| `fixed_params` | Parameters embedded in token (cannot be overridden) |
| `filter` | SQL WHERE clause for datasource filtering |

### Example: Multi-Tenant Access

```typescript
const orgToken = await client.tokens.createJWT({
  name: "org_acme_access",
  expiresAt: new Date(Date.now() + 24 * 60 * 60 * 1000), // 1 day
  scopes: [
    {
      type: "DATASOURCES:READ",
      resource: "events",
      filter: "org_id = 'acme'",
    },
    {
      type: "PIPES:READ",
      resource: "analytics_dashboard",
      fixed_params: { org_id: "acme" },
    },
  ],
  limits: { rps: 100 },
});
```

### JWT Limits

| Option | Description |
|--------|-------------|
| `rps` | Requests per second limit |
```

## File: `skills/tinybird-typescript-sdk-guidelines/rules/typed-client.md`
```markdown
# Creating the Typed Client

## Client Setup

```typescript
// src/tinybird/client.ts
import { createTinybirdClient } from "@tinybirdco/sdk";
import { pageViews, type PageViewsRow } from "./datasources";
import { topPages, type TopPagesParams, type TopPagesOutput } from "./pipes";

export const tinybird = createTinybirdClient({
  datasources: { pageViews },
  pipes: { topPages },
});

export type { PageViewsRow, TopPagesParams, TopPagesOutput };
export { pageViews, topPages };
```

## Using the Typed Client

### Type-Safe Ingestion

```typescript
import { tinybird, type PageViewsRow } from "@tinybird/client";

// Autocomplete and type checking for all fields
await tinybird.ingest.pageViews({
  timestamp: new Date(),
  pathname: "/home",
  session_id: "abc123",
  country: "US",
});

// Batch ingestion
await tinybird.ingest.pageViews([
  { timestamp: new Date(), pathname: "/home", session_id: "abc", country: "US" },
  { timestamp: new Date(), pathname: "/about", session_id: "abc", country: "US" },
]);
```

### Type-Safe Queries

```typescript
import { tinybird } from "@tinybird/client";

// Autocomplete for parameters, typed results
const result = await tinybird.query.topPages({
  start_date: new Date("2024-01-01"),
  end_date: new Date(),
  limit: 5,
});

// result.data is fully typed: { pathname: string, views: bigint }[]
for (const row of result.data) {
  console.log(`${row.pathname}: ${row.views} views`);
}
```

## Client Benefits

- **Autocomplete**: Full IDE support for datasource fields and endpoint parameters
- **Type Safety**: Catch schema mismatches at compile time
- **Refactoring**: Rename fields and parameters with confidence
- **Documentation**: Types serve as inline documentation
```

