---
id: timescale-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.285853
---

# KNOWLEDGE EXTRACT: timescale
> **Extracted on:** 2026-03-30 17:54:18
> **Source:** timescale

---

## File: `pgvectorscale.md`
```markdown
# 📦 timescale/pgvectorscale [🔖 PENDING/APPROVE]
🔗 https://github.com/timescale/pgvectorscale


## Meta
- **Stars:** ⭐ 2941 | **Forks:** 🍴 131
- **Language:** Rust | **License:** PostgreSQL
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Postgres extension for vector search (DiskANN), complements pgvector for performance and scale. Postgres OSS licensed.

## README (trích đầu)
```
<p></p>
<div align=center>

# pgvectorscale

<h3>pgvectorscale builds on pgvector with higher performance embedding search and cost-efficient storage for AI applications. </h3>

[![Discord](https://img.shields.io/badge/Join_us_on_Discord-black?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/KRdHVXAmkp)
[![Try Timescale for free](https://img.shields.io/badge/Try_Timescale_for_free-black?style=for-the-badge&logo=timescale&logoColor=white)](https://tsdb.co/gh-pgvector-signup)
</div>

pgvectorscale complements [pgvector][pgvector], the open-source vector data extension for PostgreSQL, and introduces the following key innovations for pgvector data:
- A new index type called StreamingDiskANN, inspired by the [DiskANN](https://github.com/microsoft/DiskANN) algorithm, based on research from Microsoft.
- Statistical Binary Quantization: developed by Timescale researchers, This compression method improves on standard Binary Quantization.
- Label-based filtered vector search: based on Microsoft's Filtered DiskANN research, this allows you to combine vector similarity search with label filtering for more precise and efficient results.

On a benchmark dataset of 50 million Cohere embeddings with 768 dimensions
each, PostgreSQL with `pgvector` and `pgvectorscale` achieves **28x lower p95
latency** and **16x higher query throughput** compared to Pinecone's storage
optimized (s1) index for approximate nearest neighbor queries at 99% recall,
all at 75% less cost when self-hosted on AWS EC2.

<div align=center>

![Benchmarks](https://assets.timescale.com/docs/images/benchmark-comparison-pgvectorscale-pinecone.png)

</div>

To learn more about the performance impact of pgvectorscale, and details about benchmark methodology and results, see the [pgvector vs Pinecone comparison blog post](http://www.timescale.com/blog/pgvector-vs-pinecone).

In contrast to pgvector, which is written in C, pgvectorscale is developed in [Rust][rust-language] using the [PGRX framework](https://github.com/pgcentralfoundation/pgrx),
offering the PostgreSQL community a new avenue for contributing to vector support.

**Application developers or DBAs** can use pgvectorscale with their PostgreSQL databases.
   * [Install pgvectorscale](#installation)
   * [Get started using pgvectorscale](#get-started-with-pgvectorscale)

If you **want to contribute** to this extension, see how to [build pgvectorscale from source in a developer environment](./DEVELOPMENT.md) and our [testing guide](./TESTING.md).

For production vector workloads, get **private beta access to vector-optimized databases** with pgvector and pgvectorscale on Timescale. [Sign up here for priority access](https://timescale.typeform.com/to/H7lQ10eQ).

## Installation

The fastest ways to run PostgreSQL with pgvectorscale are:

* [Using a pre-built Docker container](#using-a-pre-built-docker-container)
* [Installing from source](#installing-from-source)
* [Enable pgvectorscale in a Timescale Cloud service](#enab
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `pg_textsearch.md`
```markdown
# 📦 timescale/pg_textsearch [🔖 PENDING/APPROVE]
🔗 https://github.com/timescale/pg_textsearch


## Meta
- **Stars:** ⭐ 3238 | **Forks:** 🍴 91
- **Language:** C | **License:** PostgreSQL
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
PostgreSQL extension for BM25 relevance-ranked full-text search. Postgres OSS licensed.

## README (trích đầu)
```
# pg_textsearch

[![CI](https://github.com/timescale/pg_textsearch/actions/workflows/ci.yml/badge.svg)](https://github.com/timescale/pg_textsearch/actions/workflows/ci.yml)
[![Benchmarks](https://github.com/timescale/pg_textsearch/actions/workflows/benchmark.yml/badge.svg)](https://timescale.github.io/pg_textsearch/benchmarks/)
[![Coverity Scan](https://scan.coverity.com/projects/32822/badge.svg)](https://scan.coverity.com/projects/pg_textsearch)

Modern ranked text search for Postgres.

- Simple syntax: `ORDER BY content <@> 'search terms'`
- BM25 ranking with configurable parameters (k1, b)
- Works with Postgres text search configurations (english, french, german, etc.)
- Fast top-k queries via Block-Max WAND optimization
- Parallel index builds for large tables
- Supports partitioned tables
- Best in class performance and scalability

🚧 **Development**: v1.0.0-dev - Working toward GA. See [ROADMAP.md](ROADMAP.md) for details.

![Tapir and Friends](images/tapir_and_friends_v1.0.0-dev.png)

## Historical note

The original name of the project was Tapir - **T**extual **A**nalysis for **P**ostgres **I**nformation **R**etrieval.  We still use the tapir as our
mascot and the name occurs in various places in the source code.

## PostgreSQL Version Compatibility

pg_textsearch supports PostgreSQL 17 and 18.

## Installation

### Pre-built Binaries

Download pre-built binaries from the
[Releases page](https://github.com/timescale/pg_textsearch/releases).
Available for Linux and macOS (amd64 and arm64), PostgreSQL 17 and 18.

### Build from Source

```sh
cd /tmp
git clone https://github.com/timescale/pg_textsearch
cd pg_textsearch
make
make install # may need sudo
```

## Getting Started

pg_textsearch must be loaded via `shared_preload_libraries`. Add the following
to `postgresql.conf` and restart the server:

```
shared_preload_libraries = 'pg_textsearch'  # add to existing list if needed
```

Then enable the extension (once per database):

```sql
CREATE EXTENSION pg_textsearch;
```

Create a table with text content

```sql
CREATE TABLE documents (id bigserial PRIMARY KEY, content text);
INSERT INTO documents (content) VALUES
    ('PostgreSQL is a powerful database system'),
    ('BM25 is an effective ranking function'),
    ('Full text search with custom scoring');
```

Create a pg_textsearch index on the text column

```sql
CREATE INDEX docs_idx ON documents USING bm25(content) WITH (text_config='english');
```

## Querying

Get the most relevant documents using the `<@>` operator

```sql
SELECT * FROM documents
ORDER BY content <@> 'database system'
LIMIT 5;
```

Note: `<@>` returns the negative BM25 score since Postgres only supports `ASC` order index scans on operators. Lower scores indicate better matches.

The index is automatically detected from the column. For explicit index specification:
```sql
SELECT * FROM documents
WHERE content <@> to_bm25query('database system', 'docs_idx') < -1.0;
```

Supported operations:
- `text <@> 'query'` - Scor
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

