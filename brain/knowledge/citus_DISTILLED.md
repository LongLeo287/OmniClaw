---
id: citus
type: knowledge
owner: OA_Triage
---
# citus
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

![Citus scales out from a single node](images/citus-scale-out.png)

Since Citus is an extension to Postgres, you can use Citus with the latest Postgres versions. And Citus works seamlessly with the PostgreSQL tools and extensions you are already familiar with.

- [Why Citus?](#why-citus)
- [Getting Started](#getting-started)
- [Using Citus](#using-citus)
- [Schema-based sharding](#schema-based-sharding)
- [Setting up with High Availability](#setting-up-with-high-availability)
- [Documentation](#documentation)
- [Architecture](#architecture)
- [When to Use Citus](#when-to-use-citus)
- [Need Help?](#need-help)
- [Contributing](#contributing)
- [Stay Connected](#stay-connected)

## Why Citus?

Developers choose Citus for two reasons:

1. Your application is outgrowing a single PostgreSQL node

	If the size and volume of your data increases over time, you may start seeing any number of performance and scalability problems on a single PostgreSQL node. For example: High CPU utilization and I/O wait times slow down your queries, SQL queries return out of memory errors, autovacuum cannot keep up and increases table bloat, etc.

	With Citus you can distribute and optionally compress your tables to always have enough memory, CPU, and I/O capacity to achieve high performance at scale. The distributed query engine can efficiently route transactions across the cluster, while parallelizing analytical queries and batch operations across all cores. Moreover, you can still use the PostgreSQL features and tools you know and love.

2. PostgreSQL can do things other systems can’t

	There are many data processing systems that are built to scale out, but few have as many powerful capabilities as PostgreSQL, including: Advanced joins and subqueries, user-defined functions, update/delete/upsert, constraints and foreign keys, powerful extensions (e.g. PostGIS, HyperLogLog), many types of indexes, time-partitioning, and sophisticated JSON support.

	Citus makes PostgreSQL’s most powerful capabilities work at any scale, allowing you to handle complex data-intensive workloads on a single database system.

## Getting Started

The quickest way to get started with Citus is to use the [Azure Cosmos DB for PostgreSQL](https://learn.microsoft.com/azure/cosmos-db/postgresql/quickstart-create-portal) managed service in the cloud—or [set up Citus locally](https://docs.citusdata.com/en/stable/installation/single_node.html).

### Citus Managed Service on Azure

You can get a fully-managed Citus cluster in minutes through the [Azure Cosmos DB for PostgreSQL portal](https://azure.microsoft.com/products/cosmos-db/). Azure will manage your backups, high availability through auto-failover, software updates, monitoring, and more for all of your servers. To get started Citus on Azure, use the [Azure Cosmos DB for PostgreSQL Quickstart](https://learn.microsoft.com/azure/cosmos-db/postgresql/quickstart-create-portal).

### Running Citus using Docker

The smallest possible Citus cluster is a single PostgreSQL node with the Citus extension, which means you can try out Citus by running a single Docker container.

```bash
# run PostgreSQL with Citus on port 5500
docker run -d --name citus -p 5500:5432 -e POSTGRES_PASSWORD=mypassword citusdata/citus

# connect using psql within the Docker container
docker exec -it citus psql -U postgres

# or, connect using local psql
psql -U postgres -d postgres -h localhost -p 5500
```

### Install Citus locally

If you already have a local PostgreSQL installation, the easiest way to install Citus is to use our packaging repo

Install packages on Ubuntu / Debian:

```bash
curl https://install.citusdata.com/community/deb.sh > add-citus-repo.sh
sudo bash add-citus-repo.sh
sudo apt-get -y install postgresql-17-citus-13.0
```

Install packages on Red Hat:
```bash
curl https://install.citusdata.com/community/rpm.sh > add-citus-repo.sh
sudo bash add-citus-repo.sh
sudo yum install -y citus130_17
```

To add Citus to your local PostgreSQL database, add the following to `postgresql.conf`:

```
shared_preload_libraries = 'citus'
```

After restarting PostgreSQL, connect using `psql` and run:

```sql
CREATE EXTENSION citus;
````
You’re now ready to get started and use Citus tables on a single node.

### Install Citus on multiple nodes

If you want to set up a multi-node cluster, you can also set up additional PostgreSQL nodes with the Citus extensions and add them to form a Citus cluster:

```sql
-- before adding the first worker node, tell future worker nodes how to reach the coordinator
SELECT citus_set_coordinator_host('10.0.0.1', 5432);

-- add worker nodes
SELECT citus_add_node('10.0.0.2', 5432);
SELECT citus_add_node('10.0.0.3', 5432);

-- rebalance the shards over the new worker nodes
SELECT rebalance_table_shards();
```

For more details, see our [documentation on how to set up a multi-node Citus cluster](https://docs.citusdata.com/en/stable/installation/multi_node.html) on various operating systems.

## Using Citus

Once you have your Citus cluster, you can start creating distributed tables, reference tables and use columnar storage.

### Creating Distributed Tables

The `create_distributed_table` UDF will transparently shard your table locally or across the worker nodes:

```sql
CREATE TABLE events (
  device_id bigint,
  event_id bigserial,
  event_time timestamptz default now(),
  data jsonb not null,
  PRIMARY KEY (device_id, event_id)
);

-- distribute the events table across shards placed locally or on the worker nodes
SELECT create_distributed_table('events', 'device_id');
```

After this operation, queries for a specific device ID will be efficiently routed to a single worker node, while queries across device IDs will be parallelized across the cluster.

```sql
-- insert some events
INSERT INTO events (device_id, data)
SELECT s % 100, ('{"measurement":'||random()||'}')::jsonb FROM generate_series(1,1000000) s;

-- get the last 3 events for device 1, routed to a single node
SELECT * FROM events WHERE device_id = 1 ORDER BY event_time DESC, event_id DESC LIMIT 3;
┌───────────┬──────────┬───────────────────────────────┬───────────────────────────────────────┐
│ device_id │ event_id │          event_time           │                 data                  │
├───────────┼──────────┼───────────────────────────────┼───────────────────────────────────────┤
│         1 │  1999901 │ 2021-03-04 16:00:31.189963+00 │ {"measurement": 0.88722643925054}     │
│         1 │  1999801 │ 2021-03-04 16:00:31.189963+00 │ {"measurement": 0.6512231304621992}   │
│         1 │  1999701 │ 2021-03-04 16:00:31.189963+00 │ {"measurement": 0.019368766051897524} │
└───────────┴──────────┴───────────────────────────────┴───────────────────────────────────────┘
(3 rows)

Time: 4.588 ms

-- explain plan for a query that is parallelized across shards, which shows the plan for
-- a query one of the shards and how the aggregation across shards is done
EXPLAIN (VERBOSE ON) SELECT count(*) FROM events;
┌────────────────────────────────────────────────────────────────────────────────────┐
│                                     QUERY PLAN                                     │
├────────────────────────────────────────────────────────────────────────────────────┤
│ Aggregate                                                                          │
│   Output: COALESCE((pg_catalog.sum(remote_scan.count))::bigint, '0'::bigint)       │
│   ->  Custom Scan (Citus Adaptive)                                                 │
│         ...                                                                        │
│         ->  Task                                                                   │
│               Query: SELECT count(*) AS count FROM events_102008 events WHERE true │
│               Node: host=localhost port=5432 dbname=postgres                       │
│               ->  Aggregate                                                        │
│                     ->  Seq Scan on public.events_102008 events                    │
└────────────────────────────────────────────────────────────────────────────────────┘
```

### Creating Distributed Tables with Co-location

Distributed tables that have the same distribution column can be co-located to enable high performance distributed joins and foreign keys between distributed tables.
By default, distributed tables will be co-located based on the type of the distribution column, but you define co-location explicitly with the `colocate_with` argument in `create_distributed_table`.

```sql
CREATE TABLE devices (
  device_id bigint primary key,
  device_name text,
  device_type_id int
);
CREATE INDEX ON devices (device_type_id);

-- co-locate the devices table with the events table
SELECT create_distributed_table('devices', 'device_id', colocate_with := 'events');

-- insert device metadata
INSERT INTO devices (device_id, device_name, device_type_id)
SELECT s, 'device-'||s, 55 FROM generate_series(0, 99) s;

-- optionally: make sure the application can only insert events for a known device
ALTER TABLE events ADD CONSTRAINT device_id_fk
FOREIGN KEY (device_id) REFERENCES devices (device_id);

-- get the average measurement across all devices of type 55, parallelized across shards
SELECT avg((data->>'measurement')::double precision)
FROM events JOIN devices USING (device_id)
WHERE device_type_id = 55;

┌────────────────────┐
│        avg         │
├────────────────────┤
│ 0.5000191877513974 │
└────────────────────┘
(1 row)

Time: 209.961 ms
```

Co-location also helps you scale [INSERT..SELECT](https://docs.citusdata.com/en/stable/articles/aggregation.html), [stored procedures](https://www.citusdata.com/blog/2020/11/21/making-postgres-stored-procedures-9x-faster-in-citus/), and [distributed transactions](https://www.citusdata.com/blog/2017/06/02/scaling-complex-sql-transactions/).

### Distributing Tables without interrupting the application


Some of you already start with Postgres, and decide to distribute tables later on while your application using the tables. In that case, you want to avoid downtime for both reads and writes. `create_distributed_table` command block writes (e.g., DML commands) on the table until the command is finished. Instead, with `create_distributed_table_concurrently` command, your application can continue to read and write the data even during the command.


```sql
CREATE TABLE device_logs (
  device_id bigint primary key,
  log text
);

-- insert device logs
INSERT INTO device_logs (device_id, log)
SELECT s, 'device log:'||s FROM generate_series(0, 99) s;

-- convert device_logs into a distributed table without interrupting the application
SELECT create_distributed_table_concurrently('device_logs', 'device_id', colocate_with := 'devices');


-- get the count of the logs, parallelized across shards
SELECT count(*) FROM device_logs;

┌───────┐
│ count │
├───────┤
│   100 │
└───────┘
(1 row)

Time: 48.734 ms
```



### Creating Reference Tables

When you need fast joins or foreign keys that do not include the distribution column, you can use `create_reference_table` to replicate a table across all nodes in the cluster.

```sql
CREATE TABLE device_types (
  device_type_id int primary key,
  device_type_name text not null unique
);

-- replicate the table across all nodes to enable foreign keys and joins on any column
SELECT create_reference_table('device_types');

-- insert a device type
INSERT INTO device_types (device_type_id, device_type_name) VALUES (55, 'laptop');

-- optionally: make sure the application can only insert devices with known types
ALTER TABLE devices ADD CONSTRAINT device_type_fk
FOREIGN KEY (device_type_id) REFERENCES device_types (device_type_id);

-- get the last 3 events for devices whose type name starts with laptop, parallelized across shards
SELECT device_id, event_time, data->>'measurement' AS value, device_name, device_type_name
FROM events JOIN devices USING (device_id) JOIN device_types USING (device_type_id)
WHERE device_type_name LIKE 'laptop%' ORDER BY event_time 
... [TRUNCATED]
```

### File: .devcontainer\requirements.txt
```txt
black==24.3.0
click==8.1.7
isort==5.12.0
mypy-extensions==1.0.0
packaging==23.2
pathspec==0.11.2
platformdirs==4.0.0
tomli==2.0.1
typing_extensions==4.8.0

```

### File: .devcontainer_DISTILLED.md
```md
---
id: .devcontainer
type: distilled_knowledge
---
# .devcontainer

## SWALLOW ENGINE DISTILLATION

### File: requirements.txt
```txt
black==24.3.0
click==8.1.7
isort==5.12.0
mypy-extensions==1.0.0
packaging==23.2
pathspec==0.11.2
platformdirs==4.0.0
tomli==2.0.1
typing_extensions==4.8.0

```

### File: devcontainer.json
```json
{
    "image": "ghcr.io/citusdata/citus-devcontainer:main",
    "runArgs": [
        "--cap-add=SYS_PTRACE",
        "--cap-add=SYS_NICE",                 // allow NUMA page inquiry
        "--security-opt=seccomp=unconfined",  // unblocks move_pages() in the container
        "--ulimit=core=-1",
    ],
    "forwardPorts": [
        9700
    ],
    "customizations": {
        "vscode": {
            "extensions": [
                "eamodio.gitlens",
                "GitHub.copilot-chat",
                "GitHub.copilot",
                "github.vscode-github-actions",
                "github.vscode-pull-request-github",
                "ms-vscode.cpptools-extension-pack",
                "ms-vsliveshare.vsliveshare",
                "rioj7.command-variable",
            ],
            "settings": {
                "files.exclude": {
                    "**/*.o": true,
                    "**/.deps/": true,
                }
            },
        }
    },
    "mounts": [
        "type=volume,target=/data",
        "source=citus-bashhistory,target=/commandhistory,type=volume",
    ],
    "updateContentCommand": "./configure",
    "postCreateCommand": "make -C .devcontainer/",
}


```


```

### File: autogen.sh
```sh
#!/bin/bash
#
# autogen.sh converts configure.ac to configure and creates
# citus_config.h.in. The resuting resulting files are checked into
# the SCM, to avoid everyone needing autoconf installed.

autoreconf -f

```

### File: cgmanifest.json
```json
{
    "Registrations": [
        {
            "Component": {
                "Type": "git",
                "git": {
                    "RepositoryUrl": "https://github.com/intel/safestringlib",
                    "CommitHash": "245c4b8cff1d2e7338b7f3a82828fc8e72b29549"
                }
            },
            "DevelopmentDependency": false
        },
        {
            "Component": {
                "Type": "git",
                "git": {
                    "RepositoryUrl": "https://github.com/postgres/postgres",
                    "CommitHash": "29be9983a64c011eac0b9ee29895cce71e15ea77"
                }
            },
            "license": "PostgreSQL",
            "licenseDetail": [
				"Portions Copyright (c) 1996-2010, The PostgreSQL Global Development Group",
				"",
				"Portions Copyright (c) 1994, The Regents of the University of California",
                "",
                "Permission to use, copy, modify, and distribute this software and its documentation for ",
                "any purpose, without fee, and without a written agreement is hereby granted, provided ",
                "that the above copyright notice and this paragraph and the following two paragraphs appear ",
                "in all copies.",
                "",
                "IN NO EVENT SHALL THE UNIVERSITY OF CALIFORNIA BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, ",
                "INCIDENTAL, OR CONSEQUENTIAL DAMAGES, INCLUDING LOST PROFITS, ARISING OUT OF THE USE OF THIS ",
                "SOFTWARE AND ITS DOCUMENTATION, EVEN IF THE UNIVERSITY OF CALIFORNIA HAS BEEN ADVISED OF THE ",
                "POSSIBILITY OF SUCH DAMAGE.",
                "",
                "THE UNIVERSITY OF CALIFORNIA SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, ",
                "THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE SOFTWARE PROVIDED ",
                "HEREUNDER IS ON AN \"AS IS\" BASIS, AND THE UNIVERSITY OF CALIFORNIA HAS NO OBLIGATIONS TO PROVIDE ",
                "MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS."
            ],
            "version": "0.0.1",
            "DevelopmentDependency": false
        }

    ]
}

```

### File: CHANGELOG.md
```md
### citus v14.0.0 (February 9, 2026) ###

* Drops PG15 support (#8372)

* Adds support for PostgreSQL 18 (#8065)

* Adds support for virtual generated columns on distributed tables
  for PostgreSQL 18 (#8346)

* Propagates publish_generated_columns publication option to worker
  nodes for distributed tables on PostgreSQL 18 (#8360)

* Respects VACUUM/ANALYZE ONLY semantics for Citus tables by
  skipping shard propagation when ONLY is specified on
  PostgreSQL 18 (#8365)

* Allows configuring sslkeylogfile connection parameter using
  citus.node_conn_info on PostgreSQL 18 (#8437)

* Fixes INSERT .. SELECT planning error with GROUP BY on
  PostgreSQL 18 (#8256)

* Fixes deparser error with named joins and whole-row references
  on PostgreSQL 18 (#8300)

* Fixes columnar temp table access failure on PostgreSQL 18 (#8309)

* Fixes multi-shard MIN/MAX on composite types by blessing record
  aggregates (#8429)

* Fixes distributed MIN/MAX for array types (#8421)

* Adds propagation of ENFORCED / NOT ENFORCED on CHECK
  constraints (#8349)

* Stops on-demand statistics collection for clusters and deprecates
  citus.enable_statistics_collection GUC (#8460)

* Disallows creating a distributed table or altering it to be colocated
  with another table if distribution key collations don't
  match (#8257)

* Makes citus_create_restore_point MX-safe by blocking 2PC commit
  decisions (#8352)

* Supports binary transfer from worker to coordinator for custom
  aggregates (#8446)

* Ensures query remains safe for deparse when a modify scan needs to
  evaluate expressions before worker query execution (#8443)

* Avoids local plan cache reuse for multi-shard queries (#8371)

* Tightens distributed plan check to cover distributed
  subplans (#8388)

* Improves performance by avoiding unnecessary shallow copy of target
  list when no array or json subscripts are present (#8155)

* Fixes a bug that ignores reference or schema sharded tables in worker
  subquery task construction when no distributed tables are
  involved (#8440)

* Fixes a bug in redundant WHERE clause detection (#8162)

* Fixes a bug that causes allowing UPDATE / MERGE queries that may
  change the distribution column value (#8214)

* Fixes a bug that causes an unexpected error when executing
  repartitioned MERGE (#8201)

* Fixes an assertion failure in Citus maintenance daemon that can
  happen in very slow systems (#8158)

* Removes an assertion from Postgres ruleutils that was rendered
  meaningless by a previous Citus commit (#8136)

* Fixes incorrect rejection of colocated joins when Row Level
  Security policies use volatile functions (#8357)

* Fixes metadata sync failure when distributed tables use domain
  types defined in non-public schemas (#8363)

* Fixes a crash on CREATE STATISTICS with non-table
  expressions (#8213, #8227)

* Fixes invalid input syntax for type bigint in citus_stats with
  large tables (#8166)

* Fixes an undefined behavior that could happen when computing
  tenant score for citus_stat_tenants (#7954)

### citus v13.1.1 (Oct 1st, 2025) ###

* Adds support for latest PG minors: 14.19, 15.14, 16.10 (#8142)

* Fixes an assertion failure when an expression in the query references
  a CTE (#8106)

* Fixes a bug that causes an unexpected error when executing
  repartitioned MERGE (#8201)

* Fixes a bug that causes allowing UPDATE / MERGE queries that may
  change the distribution column value (#8214)

* Updates dynamic_library_path automatically when CDC is enabled (#8025)

### citus v13.0.5 (Oct 1st, 2025) ###

* Adds support for latest PG minors: 14.19, 15.14, 16.10 (#7986, #8142)

* Fixes a bug that causes an unexpected error when executing
  repartitioned MERGE (#8201)

* Fixes a bug that causes allowing UPDATE / MERGE queries that may
  change the distribution column value (#8214)

* Fixes a bug in redundant WHERE clause detection (#8162)

* Updates dynamic_library_path automatically when CDC is enabled (#8025)

### citus v12.1.10 (Oct 1, 2025) ###

* Adds support for latest PG minors: 14.19, 15.14, 16.10 (#7986, #8142)

* Fixes a bug that causes allowing UPDATE / MERGE queries that may
  change the distribution column value (#8214)

* Fixes an assertion failure that happens when querying a view that is
  defined on distributed tables (#8136)

### citus v12.1.9 (Sep 3, 2025) ###

* Adds a GUC for queries with outer joins and pseudoconstant quals (#8163)

* Updates dynamic_library_path automatically when CDC is enabled (#7715)

### citus v13.2.0 (August 18, 2025) ###

* Adds `citus_add_clone_node()`, `citus_add_clone_node_with_nodeid()`,
  `citus_remove_clone_node()` and `citus_remove_clone_node_with_nodeid()`
  UDFs to support snapshot-based node splits. This feature allows promoting
  a streaming replica (clone) to a primary node and rebalancing shards
  between the original and newly promoted node without requiring a full data
  copy. This greatly reduces rebalance times for scale-out operations when
  the new node already has the data via streaming replication (#8122)

* Improves performance of shard rebalancer by parallelizing moves and removing
  bottlenecks that blocked concurrent logical-replication transfers. This
  reduces rebalance windows especially for clusters with large reference
  tables and allows multiple shard transfers to run in parallel (#7983)

* Adds citus.enable_recurring_outer_join_pushdown GUC (enabled by default)
  to allow pushing down LEFT/RIGHT outer joins having a reference table in
  the outer side and a distributed table on the inner side (e.g.,
  \<reference table\> LEFT JOIN \<distributed table\>) (#7973)

* Adds citus.enable_local_fast_path_query_optimization (enabled by default)
  GUC to avoid unnecessary query deparsing to improve performance of
  fast-path queries targeting local shards (#8035)

* Adds `citus_stats()` UDF that can be used to retrieve distributed `pg_stats`
  for the provided Citus table. (#8026)

* Avoids automatically creating citus_columnar when there are no relations
  using it (#8081)

* Makes sure to check if the distribution key is in the target list before
  pushing down a query with a union and an outer join (#8092)

* Fixes a bug in EXPLAIN ANALYZE to prevent unintended (duplicate) execution
  of the (sub)plans during the explain phase (#8017)

* Fixes potential memory corruptions that could happen when accessing
  various catalog tables after a Citus downgrade is followed by a Citus
  upgrade (#7950, #8120, #8124, #8121, #8114, #8146)

* Fixes UPDATE statements with indirection and array/jsonb subscripting with
  more than one field (#7675)

* Fixes an assertion failure that happens when an expression in the query
  references a CTE (#8106)

* Fixes an assertion failure that happens when querying a view that is
  defined on distributed tables (#8136)

### citus v13.1.0 (May 30th, 2025) ###

* Adds `citus_stat_counters` view that can be used to query
  stat counters that Citus collects while the feature is enabled, which is
  controlled by citus.enable_stat_counters. `citus_stat_counters()` can be
  used to query the stat counters for the provided database oid and
  `citus_stat_counters_reset()` can be used to reset them for the provided
  database oid or for the current database if nothing or 0 is provided (#7917)

* Adds `citus_nodes` view that displays the node name, port role, and "active"
  for nodes in the cluster (#7968)

* Adds `citus_is_primary_node()` UDF to determine if the current node is a
  primary node in the cluster (#7720)

* Adds support for propagating `GRANT/REVOKE` rights on table columns (#7918)

* Adds support for propagating `REASSIGN OWNED BY` commands (#7319)

* Adds support for propagating `CREATE`/`DROP` database from all nodes (#7240,
  #7253, #7359)

* Propagates `SECURITY LABEL ON ROLE` statement from any node (#7508)

* Adds support for issuing role management commands from worker nodes (#7278)

* Adds support for propagating `ALTER USER RENAME` commands (#7204)

* Adds support for propagating `ALTER DATABASE <db_name> SET ..` commands
  (#7181)

* Adds support for propagating `SECURITY LABEL` on tables and columns (#7956)

* Adds support for propagating `COMMENT ON <database>/<role>` commands (#7388)

* Moves some of the internal citus functions from `pg_catalog` to
  `citus_internal` schema (#7473, #7470, #7466, 7456, 7450)

* Adjusts `max_prepared_transactions` only when it's set to default on PG >= 16
  (#7712)

* Adds skip_qualify_public param to shard_name() UDF to allow qualifying for
  "public" schema when needed (#8014)

* Allows `citus_*_size` on indexes on a distributed tables (#7271)

* Allows `GRANT ADMIN` to now also be `INHERIT` or `SET` in support of PG16

* Makes sure `worker_copy_table_to_node` errors out with Citus tables (#7662)

* Adds information to explain output when using
  `citus.explain_distributed_queries=false` (#7412)

* Logs username in the failed connection message (#7432)

* Makes sure to avoid incorrectly pushing-down the outer joins between
  distributed tables and recurring relations (like reference tables, local
  tables and `VALUES(..)` etc.) prior to PG 17 (#7937)

* Prevents incorrectly pushing `nextval()` call down to workers to avoid using
  incorrect sequence value for some types of `INSERT .. SELECT`s (#7976)

* Makes sure to prevent `INSERT INTO ... SELECT` queries involving subfield or
  sublink, to avoid crashes (#7912)

* Makes sure to take improvement_threshold into the account
  in `citus_add_rebalance_strategy()` (#7247)

* Makes sure to disallow creating a replicated distributed
  table concurrently (#7219)

* Fixes a bug that causes omitting `CASCADE` clause for the commands sent to
  workers for `REVOKE` commands on tables (#7958)

* Fixes an issue detected using address sanitizer (#7948, #7949)

* Fixes a bug in deparsing of shard query in case of "output-table column" name
  conflict (#7932)

* Fixes a crash in columnar custom scan that happens when a columnar table is
  used in a join (#7703)

* Fixes `MERGE` command when insert value does not have source distributed
  column (#7627)

* Fixes performance issue when using `\d tablename` on a server with many
  tables (#7577)

* Fixes performance issue in `GetForeignKeyOids` on systems with many
  constraints (#7580)

* Fixes performance issue when distributing a table that depends on an
  extension (#7574)

* Fixes performance issue when creating distributed tables if many already
  exist (#7575)

* Fixes a crash caused by some form of `ALTER TABLE ADD COLUMN` statements. When
  adding multiple columns, if one of the `ADD COLUMN` statements contains a
  `FOREIGN` constraint ommitting the referenced
  columns in the statement, a `SEGFAULT` occurs (#7522)

* Fixes assertion failure in maintenance daemon during Citus upgrades  (#7537)

* Fixes segmentation fault when using `CASE WHEN` in `DO` block functions
  (#7554)

* Fixes undefined behavior in `master_disable_node` due to argument mismatch
  (#7492)

* Fixes incorrect propagating of `GRANTED BY` and `CASCADE/RESTRICT` clauses
  for `REVOKE` statements (#7451)

* Fixes the incorrect column count after `ALTER TABLE` (#7379)

* Fixes timeout when underlying socket is changed for an inter-node connection
  (#7377)

* Fixes memory leaks (#7441, #7440)

* Fixes leaking of memory and memory contexts when tracking foreign keys between
  Citus tables (#7236)

* Fixes a potential segfault for background rebalancer (#7694)

* Fixes potential `NULL` dereference in casual clocks (#7704)

### citus v13.0.4 (May 29th, 2025) ###

* Fixes an issue detected using address sanitizer (#7966)

* Error out for queries with outer joins and pseudoconstant quals in versions
  prior to PG 17 (#7937)

### citus v12.1.8 (May 29, 2025) ###

* Fixes a crash in left outer joins that can happen when there is an an
  aggregate on a column from the inner side of the join (#7904)

* Fixes an issue detected using address sanitizer (#7965)

* Fixes a crash when executing a prepared CALL, which is not pure SQL but
available with some drivers like npgsql and jpgdbc (#7288)

### citus v13.0.3 (March 20th, 2025) ###

* Fixes a version bump issue in 13.0.2

### citus v13.0.2 (March 12th, 2025) ###

* Fixes a crash in columnar custom scan that happens when a columnar table is
  used in a join. (#7647)

* Fixes a bug that breaks `UPDATE SET (...) = (SELECT some_func(),... )`
  type of queries on Citus tables (#7914)

* Fixes a planning error caused by a redundant WHERE clause (#7907)

* Fixes a crash in left outer joins that can happen when there is an aggregate
  on a column from the inner side of the join. (#7901)

* Fixes deadlock with transaction recovery that is possible during Citus
  upgrades. (#7910)

* Fixes a bug that prevents inserting into Citus tables that uses
  a GENERATED ALWAYS AS IDENTITY column. (#7920)

* Ensures that a MERGE command on a distributed table with a WHEN NOT MATCHED BY
  SOURCE clause runs against all shards of the distributed table. (#7900)

* Fixes a bug that breaks router updates on distributed tables
  when a reference table is used in the subquery (#7897)

### citus v12.1.7 (Feb 6, 2025) ###

* Fixes a crash that happens because of unsafe catalog access when re-assigning
  the global pid after `application_name` changes (#7791)

* Prevents crashes when another extension skips executing the
  `ClientAuthentication_hook` of Citus. (#7836)

### citus v13.0.1 (February 4th, 2025) ###

* Drops support for PostgreSQL 14 (#7753)

### citus v13.0.0 (January 22, 2025) ###

* Adds support for PostgreSQL 17 (#7699, #7661)

* Adds `JSON_TABLE()` support in distributed queries (#7816)

* Propagates `MERGE ... WHEN NOT MATCHED BY SOURCE` (#7807)

* Propagates `MEMORY` and `SERIALIZE` options of `EXPLAIN` (#7802)

* Adds support for identity columns in distributed partitioned tables (#7785)

* Allows specifying an access method for distributed partitioned tables (#7818)

* Allows exclusion constraints on distributed partitioned tables (#7733)

* Allows configuring sslnegotiation using `citus.node_conn_info` (#7821)

* Avoids wal receiver timeouts during large shard splits (#7229)

* Fixes a bug causing incorrect writing of data to target `MERGE` repartition
  command (#7659)

* Fixes a crash that happens because of unsafe catalog access when re-assigning
  the global pid after `application_name` changes (#7791)

* Fixes incorrect `VALID UNTIL` setting assumption made for roles when syncing
  them to new nodes (#7534)

* Fixes segfault when calling distributed procedure with a parameterized
  distribution argument (#7242)

* Fixes server crash when trying to execute `activate_node_snapshot()` on a
  single-node cluster (#7552)

* Improves `citus_move_shard_placement()` to fail early if there is a new node
  without reference tables yet (#7467)

### citus v12.1.6 (Nov 14, 2024) ###

* Propagates `SECURITY LABEL .. ON ROLE` statements (#7304)

* Fixes crash caused by running queries with window partition (
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Microsoft Open Source Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

Resources:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns

```

### File: CONTRIBUTING.md
```md
# Contributing to Citus

We're happy you want to contribute! You can help us in different ways:

* Open an [issue](https://github.com/citusdata/citus/issues) with
  suggestions for improvements
* Fork this repository and submit a pull request

Before accepting any code contributions we ask that contributors
sign a Contributor License Agreement (CLA). For an explanation of
why we ask this as well as instructions for how to proceed, see the
[Microsoft CLA](https://cla.opensource.microsoft.com/).

### Devcontainer / Github Codespaces

The easiest way to start contributing is via our devcontainer. This container works both locally in visual studio code with docker-desktop/docker-for-mac as well as [Github Codespaces](https://github.com/features/codespaces). To open the project in vscode you will need the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). For codespaces you will need to [create a new codespace](https://codespace.new/citusdata/citus).

With the extension installed you can run the following from the command pallet to get started

```
> Dev Containers: Clone Repository in Container Volume...
```

In the subsequent popup paste the url to the repo and hit enter.

```
https://github.com/citusdata/citus
```

This will create an isolated Workspace in vscode, complete with all tools required to build, test and run the Citus extension. We keep this container up to date with the supported postgres versions as well as the exact versions of tooling we use.

To quickly start we suggest splitting your terminal once to have two shells. The left one in the `/workspaces/citus`, the second one changed to `/data`. The left terminal will be used to interact with the project, the right one with a testing cluster.

To get citus installed from source we run `make install -s` in the first terminal. Once installed you can start a Citus cluster in the second terminal via `citus_dev make citus`. The cluster will run in the background, and can be interacted with via `citus_dev`. To get an overview of the available commands.

With the Citus cluster running you can connect to the coordinator in the first terminal via `psql -p9700`. Because the coordinator is the most common entrypoint the `PGPORT` environment is set accordingly, so a simple `psql` will connect directly to the coordinator.

### Debugging in the VS code

1. Start Debugging: Press F5 in VS Code to start debugging. When prompted, you'll need to attach the debugger to the appropriate PostgreSQL process.

2. Identify the Process: If you're running a psql command, take note of the PID that appears in your psql prompt. For example:
```
[local] citus@citus:9700 (PID: 5436)=#
```
This PID (5436 in this case) indicates the process that you should attach the debugger to.
If you are uncertain about which process to attach, you can list all running PostgreSQL processes using the following command:
```
ps aux | grep postgres
```

Look for the process associated with the PID you noted. For example:
```
citus      5436  0.0  0.0  0  0 ?        S    14:00   0:00 postgres: citus citus
```
4. Attach the Debugger: Once you've identified the correct PID, select that process when prompted in VS Code to attach the debugger. You should now be able to debug the PostgreSQL session tied to the psql command.

5. Set Breakpoints and Debug: With the debugger attached, you can set breakpoints within the code. This allows you to step through the code execution, inspect variables, and fully debug the PostgreSQL instance running in your container.

### Getting and building

[PostgreSQL documentation](https://www.postgresql.org/support/versioning/) has a
section on upgrade policy.

	We always recommend that all users run the latest available minor release [for PostgreSQL] for whatever major version is in use.

We expect Citus users to honor this recommendation and use latest available
PostgreSQL minor release. Failure to do so may result in failures in our test
suite. There are some known improvements in PG test architecture such as
[this commit](https://github.com/postgres/postgres/commit/3f323956128ff8589ce4d3a14e8b950837831803)
that are missing in earlier minor versions.

#### Mac

1. Install Xcode
2. Install packages with Homebrew

  ```bash
  brew update
  brew install git postgresql python
  ```

3. Get, build, and test the code

  ```bash
  git clone https://github.com/citusdata/citus.git

  cd citus
  ./configure
  # If you have already installed the project, you need to clean it first
  make clean
  make
  make install
  # Optionally, you might instead want to use `make install-all`
  # since `multi_extension` regression test would fail due to missing downgrade scripts.
  cd src/test/regress

  pip install pipenv
  pipenv --rm
  pipenv install
  pipenv shell

  make check
  ```

#### Debian-based Linux (Ubuntu, Debian)

1. Install build dependencies

  ```bash
  echo "deb http://apt.postgresql.org/pub/repos/apt/ $(lsb_release -cs)-pgdg main" | \
       sudo tee /etc/apt/sources.list.d/pgdg.list
  wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | \
       sudo apt-key add -
  sudo apt-get update

  sudo apt-get install -y postgresql-server-dev-14 postgresql-14 \
                          autoconf flex git libcurl4-gnutls-dev libicu-dev \
                          libkrb5-dev liblz4-dev libpam0g-dev libreadline-dev \
                          libselinux1-dev libssl-dev libxslt1-dev libzstd-dev \
                          make uuid-dev
  ```

2. Get, build, and test the code

  ```bash
  git clone https://github.com/citusdata/citus.git
  cd citus
  ./configure
  # If you have already installed the project previously, you need to clean it first
  make clean
  make
  sudo make install
  # Optionally, you might instead want to use `sudo make install-all`
  # since `multi_extension` regression test would fail due to missing downgrade scripts.
  cd src/test/regress

  pip install pipenv
  pipenv --rm
  pipenv install
  pipenv shell

  make check
  ```

#### Red Hat-based Linux (RHEL, CentOS, Fedora)

1. Find the RPM URL for your repo at [yum.postgresql.org](http://yum.postgresql.org/repopackages.php)
2. Register its contents with Yum:

  ```bash
  sudo yum install -y <url>
  ```

3. Register EPEL and SCL repositories for your distro.

  On CentOS:

  ```bash
  yum install -y centos-release-scl-rh epel-release
  ```

  On RHEL, see [this RedHat blog post](https://developers.redhat.com/blog/2018/07/07/yum-install-gcc7-clang/) to install set-up SCL first. Then run:

  ```bash
  yum install -y epel-release
  ```

4. Install build dependencies

  ```bash
  sudo yum update -y
  sudo yum groupinstall -y 'Development Tools'
  sudo yum install -y postgresql14-devel postgresql14-server     \
                      git libcurl-devel libxml2-devel libxslt-devel \
                      libzstd-devel llvm-toolset-7-clang llvm5.0 lz4-devel \
                      openssl-devel pam-devel readline-devel

  git clone https://github.com/citusdata/citus.git
  cd citus
  PG_CONFIG=/usr/pgsql-14/bin/pg_config ./configure
  # If you have already installed the project previously, you need to clean it first
  make clean
  make
  sudo make install
  # Optionally, you might instead want to use `sudo make install-all`
  # since `multi_extension` regression test would fail due to missing downgrade scripts.
  cd src/test/regress

  pip install pipenv
  pipenv --rm
  pipenv install
  pipenv shell

  make check
  ```

### Following our coding conventions

Our coding conventions are documented in [STYLEGUIDE.md](STYLEGUIDE.md).

### Making SQL changes

Sometimes you need to make change to the SQL that the citus extension runs upon
creations. The way this is done is by changing the last file in
`src/backend/distributed/sql`, or creating it if the last file is from a
published release. If you needed to create a new file, also change the
`default_version` field in `src/backend/distributed/citus.control` to match your
new version. All the files in this directory are run in order based on
their name. See [this page in the Postgres
docs](https://www.postgresql.org/docs/current/extend-extensions.html) for more
information on how Postgres runs these files.

#### Changing or creating functions

If you need to change any functions defined by Citus. You should check inside
`src/backend/distributed/sql/udfs` to see if there is already a directory for
this function, if not create one. Then change or create the file called
`latest.sql` in that directory to match how it should create the function. This
should be including any DROP (IF EXISTS), COMMENT and REVOKE statements for this
function.

Then copy the `latest.sql` file to `{version}.sql`, where `{version}` is the
version for which this sql change is, e.g. `{9.0-1.sql}`. Now that you've
created this stable snapshot of the function definition for your version you
should use it in your actual sql file, e.g.
`src/backend/distributed/sql/citus--8.3-1--9.0-1.sql`. You do this by using C
style `#include` statements like this:
```
#include "udfs/myudf/9.0-1.sql"
```

#### Other SQL

Any other SQL you can put directly in the main sql file, e.g.
`src/backend/distributed/sql/citus--8.3-1--9.0-1.sql`.

### Backporting a commit to a release branch

1. Check out the release branch that you want to backport to `git checkout release-11.3`
2. Make sure you have the latest changes `git pull`
3. Create a new release branch with a unique name `git checkout -b release-11.3-<yourname>`
4. Cherry-pick the commit that you want to backport `git cherry-pick -x <sha>` (the `-x` is important)
5. Push the branch `git push`
6. Wait for tests to pass
7. If the cherry-pick required non-trivial merge conflicts, create a PR and ask
   for a review.
8. After the tests pass on CI, fast-forward the release branch `git push origin release-11.3-<yourname>:release-11.3`

### Running tests

See [`src/test/regress/README.md`](https://github.com/citusdata/citus/blob/master/src/test/regress/README.md)

### Documentation

User-facing documentation is published on [docs.citusdata.com](https://docs.citusdata.com/). When adding a new feature, function, or setting, you can open a pull request or issue against the [Citus docs repo](https://github.com/citusdata/citus_docs/).

Detailed descriptions of the implementation for Citus developers are provided in the [Citus Technical Documentation](src/backend/distributed/README.md). It is currently a single file for ease of searching. Please update the documentation if you make any changes that affect the design or add major new features.

# Making a pull request ready for reviews

Asking for help and asking for reviews are two different things. When you're asking for help, you're asking for someone to help you with something that you're not expected to know.

But when you're asking for a review, you're asking for someone to review your work and provide feedback. So, when you're asking for a review, you're expected to make sure that:

* Your changes don't perform **unnecessary line addition / deletions / style changes on unrelated files / lines**.

* All CI jobs are **passing**, including **style checks** and **flaky test detection jobs**. Note that if you're an external contributor, you don't have to wait CI jobs to run (and finish) because they don't get automatically triggered for external contributors.

* Your PR has necessary amount of **tests** and that they're passing.

* You separated as much as possible work into **separate PRs**, e.g., a prerequisite bugfix, a refactoring etc..

* Your PR doesn't introduce a typo or something that you can easily fix yourself.

* After all CI jobs pass, code-coverage measurement job (CodeCov as of today) then kicks in. That's why it's important to make the **tests passing** first. At that point, you're expected to check **CodeCov annotations** that can be seen in the **Files Changed** tab and expected to make sure that it doesn't complain about any lines that are not covered. For example, it's ok if CodeCov complains about an `ereport()` call that you put for an "unexpected-but-better-than-crashing" case, but it's not ok if it complains about an uncovered `if` branch that you added.

* And finally, perform a **self-review** to make sure that:
  * Code and code-comments reflects the idea **without requiring an extra explanation** via a chat message / email / PR comment.
    This is important because we don't expect developers to reach out to author / read about the whole discussion in the PR to understand the idea behind a commit merged into `main` branch.
  * PR description is clear enough.
  * If-and-only-if you're **introducing a user facing change / bugfix**, your PR has a line that starts with `DESCRIPTION: <Present simple tense word that starts with a capital letter, e.g., Adds support for / Fixes / Disallows>`.
  * **Commit messages** are clear enough if the commits are doing logically different things.

```

### File: DEVCONTAINER.md
```md
# Devcontainer

## Coredumps
When postgres/citus crashes, there is the option to create a coredump. This is useful for debugging the issue. Coredumps are enabled in the devcontainer by default. However, not all environments are configured correctly out of the box. The most important configuration that is not standardized is the `core_pattern`. The configuration can be verified from the container, however, you cannot change this setting from inside the container as the filesystem containing this setting is in read only mode while inside the container.

To verify if corefiles are written run the following command in a terminal. This shows the filename pattern with which the corefile will be written.
```bash
cat /proc/sys/kernel/core_pattern
```

This should be configured with a relative path or simply a simple filename, such as `core`. When your environment shows an absolute path you will need to change this setting. How to change this setting depends highly on the underlying system as the setting needs to be changed on the kernel of the host running the container.

You can put any pattern in `/proc/sys/kernel/core_pattern` as you see fit. eg. You can add the PID to the core pattern in one of two ways;
- You either include `%p` in the core_pattern. This gets substituted with the PID of the crashing process.
- Alternatively you could set `/proc/sys/kernel/core_uses_pid` to `1` in the same way as you set `core_pattern`. This will append the PID to the corefile if `%p` is not explicitly contained in the core_pattern.

When a coredump is written you can use the debug/launch configuration `Open core file` which is preconfigured in the devcontainer. This will open a fileprompt that lists all coredumps that are found in your workspace. When you want to debug coredumps from `citus_dev` that are run in your `/data` directory, you can add the data directory to your workspace. In the command pallet of vscode you can run `>Workspace: Add Folder to Workspace...` and select the `/data` directory. This will allow you to open the coredumps from the `/data` directory in the `Open core file` debug configuration.

### Windows (docker desktop)
When running in docker desktop on windows you will most likely need to change this setting. The linux guest in WSL2 that runs your container is the `docker-desktop` environment. The easiest way to get onto the host, where you can change this setting, is to open a powershell window and verify you have the docker-desktop environment listed.

```powershell
wsl --list
```

Among others this should list both `docker-desktop` and `docker-desktop-data`. You can then open a shell in the `docker-desktop` environment.

```powershell
wsl -d docker-desktop
```

Inside this shell you can verify that you have the right environment by running

```bash
cat /proc/sys/kernel/core_pattern
```

This should show the same configuration as the one you see inside the devcontainer. You can then change the setting by running the following command.
This will change the setting for the current session. If you want to make the change permanent you will need to add this to a startup script.

```bash
echo "core" > /proc/sys/kernel/core_pattern
```

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
