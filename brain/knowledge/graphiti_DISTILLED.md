---
id: graphiti
type: knowledge
owner: OA_Triage
---
# graphiti
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <a href="https://www.getzep.com/">
    <img src="https://github.com/user-attachments/assets/119c5682-9654-4257-8922-56b7cb8ffd73" width="150" alt="Zep Logo">
  </a>
</p>

<h1 align="center">
Graphiti
</h1>
<h2 align="center">Build Temporal Context Graphs for AI Agents</h2>

<div align="center">

[![Lint](https://github.com/getzep/Graphiti/actions/workflows/lint.yml/badge.svg?style=flat)](https://github.com/getzep/Graphiti/actions/workflows/lint.yml)
[![Unit Tests](https://github.com/getzep/Graphiti/actions/workflows/unit_tests.yml/badge.svg)](https://github.com/getzep/Graphiti/actions/workflows/unit_tests.yml)
[![MyPy Check](https://github.com/getzep/Graphiti/actions/workflows/typecheck.yml/badge.svg)](https://github.com/getzep/Graphiti/actions/workflows/typecheck.yml)

[![GitHub Repo stars](https://img.shields.io/github/stars/getzep/graphiti)](https://github.com/getzep/graphiti/stargazers)
[![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white)](https://discord.com/invite/W8Kw6bsgXQ)
[![arXiv](https://img.shields.io/badge/arXiv-2501.13956-b31b1b.svg?style=flat)](https://arxiv.org/abs/2501.13956)
[![Release](https://img.shields.io/github/v/release/getzep/graphiti?style=flat&label=Release&color=limegreen)](https://github.com/getzep/graphiti/releases)

</div>
<div align="center">

<a href="https://trendshift.io/repositories/12986" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12986" alt="getzep%2Fgraphiti | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

</div>

> [!NOTE]
> **We're Hiring!** Build context graphs that power reliable, personalized, fast production AI agents.
> Come build with us — we're hiring Engineers and Developer Relations folks. [View open roles](https://www.getzep.com/careers/).

⭐ *Help us reach more developers and grow the Graphiti community. Star this repo!*

&nbsp;

> [!TIP]
> Check out the new [MCP server for Graphiti](mcp_server/README.md)! Give Claude, Cursor, and other MCP clients powerful
> context graph-based memory with temporal awareness.

Graphiti is a framework for building and querying temporal context graphs for AI agents. Unlike static knowledge graphs,
Graphiti's context graphs track how facts change over time, maintain provenance to source data, and support both
prescribed and learned ontology — making them purpose-built for agents operating on evolving, real-world data.

Unlike traditional retrieval-augmented generation (RAG) methods, Graphiti continuously integrates user interactions,
structured and unstructured enterprise data, and external information into a coherent, queryable graph. The framework
supports incremental data updates, efficient retrieval, and precise historical queries without requiring complete graph
recomputation, making it suitable for developing interactive, context-aware AI applications.

Use Graphiti to:

- Build context graphs that evolve with every interaction — tracking what's true now and what was true before.
- Give agents rich, structured context instead of flat document chunks or raw chat history.
- Query across time, meaning, and relationships with hybrid retrieval (semantic + keyword + graph traversal).

&nbsp;

<p align="center">
    <img src="images/graphiti-graph-intro.gif" alt="Graphiti temporal walkthrough" width="700px">
</p>

&nbsp;

## What is a Context Graph?

A **context graph** is a temporal graph of entities, relationships, and facts — like *"Kendra loves Adidas shoes (as of
March 2026)."* Unlike traditional knowledge graphs, each fact in a context graph has a validity window: when it became
true, and when (if ever) it was superseded. Entities evolve over time with updated summaries. Everything traces back to
**episodes** — the raw data that produced it.

What makes Graphiti unique is its ability to autonomously build context graphs from unstructured and structured data,
handling changing relationships while preserving full temporal history.

A context graph contains:

| Component | What it stores |
|-----------|---------------|
| **Entities** (nodes) | People, products, policies, concepts — with summaries that evolve over time |
| **Facts / Relationships** (edges) | Triplets (Entity → Relationship → Entity) with temporal validity windows |
| **Episodes** (provenance) | Raw data as ingested — the ground truth stream. Every derived fact traces back here |
| **Custom Types** (ontology) | Developer-defined entity and edge types via Pydantic models |

## Graphiti and Zep

Graphiti is the open-source temporal context graph engine at the core of
[Zep's](https://www.getzep.com) context infrastructure for AI agents. Zep manages context graphs at scale, providing
governed, low-latency context retrieval and assembly for production agent deployments.

Using Graphiti, we've demonstrated Zep is
the [State of the Art in Agent Memory](https://blog.getzep.com/state-of-the-art-agent-memory/).

Read our paper: [Zep: A Temporal Knowledge Graph Architecture for Agent Memory](https://arxiv.org/abs/2501.13956).

We're excited to open-source Graphiti, believing its potential as a context graph engine reaches far beyond memory
applications.

<p align="center">
    <a href="https://arxiv.org/abs/2501.13956"><img src="images/arxiv-screenshot.png" alt="Zep: A Temporal Knowledge Graph Architecture for Agent Memory" width="700px"></a>
</p>

## Zep vs Graphiti

| Aspect | Zep | Graphiti |
|--------|-----|---------|
| **What they are** | Managed context graph infrastructure for AI agents | Open-source temporal context graph engine |
| **Context graphs** | Manages vast numbers of per-user/entity context graphs with governance | Build and query individual context graphs |
| **User & conversation management** | Built-in users, threads, and message storage | Build your own |
| **Retrieval & performance** | Pre-configured, production-ready retrieval with sub-200ms performance at scale | Custom implementation required; performance depends on your setup |
| **Developer tools** | Dashboard with graph visualization, debug logs, API logs; SDKs for Python, TypeScript, and Go | Build your own tools |
| **Enterprise features** | SLAs, support, security guarantees | Self-managed |
| **Deployment** | Fully managed or in your cloud | Self-hosted only |

### When to choose which

**Choose Zep** if you want a turnkey, enterprise-grade platform with security, performance, and support baked in.

**Choose Graphiti** if you want a flexible OSS core and you're comfortable building/operating the surrounding system.

## Why Graphiti?

Traditional RAG approaches often rely on batch processing and static data summarization, making them inefficient for
frequently changing data. Graphiti addresses these challenges by providing:

- **Temporal Fact Management:** Facts have validity windows. When information changes, old facts are
  invalidated — not deleted. Query what's true now, or what was true at any point in time.
- **Episodes & Provenance:** Every entity and relationship traces back to the episodes (raw data) that produced it.
  Full lineage from derived fact to source.
- **Prescribed & Learned Ontology:** Define entity and edge types upfront via Pydantic models (prescribed), or let
  structure emerge from your data (learned). Start simple, evolve as patterns appear.
- **Incremental Graph Construction:** New data integrates immediately without batch recomputation. The graph evolves
  in real-time as episodes are ingested.
- **Hybrid Retrieval:** Combines semantic embeddings, keyword (BM25), and graph traversal for low-latency,
  high-precision queries without reliance on LLM summarization.
- **Scalability:** Efficiently manages large datasets with parallel processing, pluggable graph backends, suitable
  for enterprise workloads.

<p align="center">
    <img src="/images/graphiti-intro-slides-stock-2.gif" alt="Graphiti structured + unstructured demo" width="700px">
</p>

## Graphiti vs. GraphRAG

| Aspect | GraphRAG | Graphiti |
|--------|----------|---------|
| **Primary Use** | Static document summarization | Dynamic, evolving context for agents |
| **Data Handling** | Batch-oriented processing | Continuous, incremental updates |
| **Knowledge Structure** | Entity clusters & community summaries | Temporal context graph — entities, facts with validity windows, episodes, communities |
| **Retrieval Method** | Sequential LLM summarization | Hybrid semantic, keyword, and graph-based search |
| **Adaptability** | Low | High |
| **Temporal Handling** | Basic timestamp tracking | Explicit bi-temporal tracking with automatic fact invalidation |
| **Contradiction Handling** | LLM-driven summarization judgments | Automatic fact invalidation with temporal history preserved |
| **Query Latency** | Seconds to tens of seconds | Typically sub-second latency |
| **Custom Entity Types** | No | Yes, customizable via Pydantic models |
| **Scalability** | Moderate | High, optimized for large datasets |

Graphiti is specifically designed to address the challenges of dynamic and frequently updated datasets, making it
particularly suitable for applications requiring real-time interaction and precise historical queries.

## Installation

Requirements:

- Python 3.10 or higher
- Neo4j 5.26 / FalkorDB 1.1.2 / Kuzu 0.11.2 / Amazon Neptune Database Cluster or Neptune Analytics Graph + Amazon
  OpenSearch Serverless collection (serves as the full text search backend)
- OpenAI API key (Graphiti defaults to OpenAI for LLM inference and embedding)

> [!IMPORTANT]
> Graphiti works best with LLM services that support Structured Output (such as OpenAI and Gemini).
> Using other services may result in incorrect output schemas and ingestion failures. This is particularly
> problematic when using smaller models.

Optional:

- Google Gemini, Anthropic, or Groq API key (for alternative LLM providers)

> [!TIP]
> The simplest way to install Neo4j is via [Neo4j Desktop](https://neo4j.com/download/). It provides a user-friendly
> interface to manage Neo4j instances and databases.
> Alternatively, you can use FalkorDB on-premises via Docker and instantly start with the quickstart example:
> ```
> docker run -p 6379:6379 -p 3000:3000 -it --rm falkordb/falkordb:latest
> ```

```bash
pip install graphiti-core
```

or

```bash
uv add graphiti-core
```

### Installing with FalkorDB Support

If you plan to use FalkorDB as your graph database backend, install with the FalkorDB extra:

```bash
pip install graphiti-core[falkordb]

# or with uv
uv add graphiti-core[falkordb]
```

### Installing with Kuzu Support

If you plan to use Kuzu as your graph database backend, install with the Kuzu extra:

```bash
pip install graphiti-core[kuzu]

# or with uv
uv add graphiti-core[kuzu]
```

### Installing with Amazon Neptune Support

If you plan to use Amazon Neptune as your graph database backend, install with the Amazon Neptune extra:

```bash
pip install graphiti-core[neptune]

# or with uv
uv add graphiti-core[neptune]
```

### You can also install optional LLM providers as extras:

```bash
# Install with Anthropic support
pip install graphiti-core[anthropic]

# Install with Groq support
pip install graphiti-core[groq]

# Install with Google Gemini support
pip install graphiti-core[google-genai]

# Install with multiple providers
pip install graphiti-core[anthropic,groq,google-genai]

# Install with FalkorDB and LLM providers
pip install graphiti-core[falkordb,anthropic,google-genai]

# Install with Amazon Neptune
pip install graphiti-core[neptune]
```

## Default to Low Concurrency; LLM Provider 429 Rate Limit Errors

Graphiti's ingestion pipelines are designed for high concurrency. By default, concurrency is set low to avoid LLM
Provider 429 Rate Limit Errors. If you find Graphiti slow, please increase concurrency as described below.

Concurrency controlled by the `SEMAPHORE_LIMIT` environment variable. By default, `SEMAPHORE_LIMIT` is set to `10`
concurrent operations to help prevent `429` rate limit errors from your LLM provider. If you encounter such errors, try
lowering this value.

If your LLM provider allows higher throughput, you can increase `SEMAPHORE_LIMIT` to boost episode ingestion
performance.

## Quick Start

> [!IMPORTANT]
> Graphiti defaults to using OpenAI for LLM inference and embedding. Ensure that an `OPENAI_API_KEY` is set in your
> environment.
> Support for Anthropic and Groq LLM inferences is available, too. Other LLM providers may be supported via OpenAI
> compatible APIs.

For a complete working example, see the [Quickstart Example](examples/quickstart/README.md) in the examples directory.
The quickstart demonstrates:

1. Connecting to a Neo4j, Amazon Neptune, FalkorDB, or Kuzu database
2. Initializing Graphiti indices and constraints
3. Adding episodes to the graph (both text and structured JSON)
4. Searching for relationships (edges) using hybrid search
5. Reranking search results using graph distance
6. Searching for nodes using predefined search recipes

The example is fully documented with clear explanations of each functionality and includes a comprehensive README with
setup instructions and next steps.

### Running with Docker Compose

You can use Docker Compose to quickly start the required services:

- **Neo4j Docker:**

  ```bash
  docker compose up
  ```

  This will start the Neo4j Docker service and related components.

- **FalkorDB Docker:**

  ```bash
  docker compose --profile falkordb up
  ```

  This will start the FalkorDB Docker service and related components.

## MCP Server

The `mcp_server` directory contains a Model Context Protocol (MCP) server implementation for Graphiti. This server
allows AI assistants to interact with Graphiti's context graph capabilities through the MCP protocol.

Key features of the MCP server include:

- Episode management (add, retrieve, delete)
- Entity management and relationship handling
- Semantic and hybrid search capabilities
- Group management for organizing related data
- Graph maintenance operations

The MCP server can be deployed using Docker with Neo4j, making it easy to integrate Graphiti into your AI assistant
workflows.

For detailed setup instructions and usage examples, see the [MCP server README](mcp_server/README.md).

## REST Service

The `server` directory contains an API service for interacting with the Graphiti API. It is built using FastAPI.

Please see the [server README](server/README.md) for more information.

## Optional Environment Variables

In addition to the Neo4j and OpenAi-compatible credentials, Graphiti also has a few optional environment variables.
If you are using one of our supported models, such as Anthropic or Voyage models, the necessary environment variables
must be set.

### Database Configuration

Database names are configured directly in the driver constructors:

- **Neo4j**: Database name defaults to `neo4j` (hardcoded in Neo4jDriver)
- **FalkorDB**: Database name defaults to `default_db` (hardcoded in Fal
... [TRUNCATED]
```

### File: server\README.md
```md
# graph-service

Graph service is a fast api server implementing the [graphiti](https://github.com/getzep/graphiti) package.

## Container Releases

The FastAPI server container is automatically built and published to Docker Hub when a new `graphiti-core` version is released to PyPI.

**Image:** `zepai/graphiti`

**Available tags:**
- `latest` - Latest stable release
- `0.22.1` - Specific version (matches graphiti-core version)

**Platforms:** linux/amd64, linux/arm64

The automated release workflow:
1. Triggers when `graphiti-core` PyPI release completes
2. Waits for PyPI package availability
3. Builds multi-platform Docker image
4. Tags with version number and `latest`
5. Pushes to Docker Hub

Only stable releases are built automatically (pre-release versions are skipped).

## Running Instructions

1. Ensure you have Docker and Docker Compose installed on your system.

2. Add `zepai/graphiti:latest` to your service setup

3. Make sure to pass the following environment variables to the service

   ```
   OPENAI_API_KEY=your_openai_api_key
   NEO4J_USER=your_neo4j_user
   NEO4J_PASSWORD=your_neo4j_password
   NEO4J_PORT=your_neo4j_port
   ```

4. This service depends on having access to a neo4j instance, you may wish to add a neo4j image to your service setup as well. Or you may wish to use neo4j cloud or a desktop version if running this locally.

   An example of docker compose setup may look like this:

   ```yml
      version: '3.8'

      services:
      graph:
         image: zepai/graphiti:latest
         ports:
            - "8000:8000"
         
         environment:
            - OPENAI_API_KEY=${OPENAI_API_KEY}
            - NEO4J_URI=bolt://neo4j:${NEO4J_PORT}
            - NEO4J_USER=${NEO4J_USER}
            - NEO4J_PASSWORD=${NEO4J_PASSWORD}
      neo4j:
         image: neo4j:5.22.0
         
         ports:
            - "7474:7474"  # HTTP
            - "${NEO4J_PORT}:${NEO4J_PORT}"  # Bolt
         volumes:
            - neo4j_data:/data
         environment:
            - NEO4J_AUTH=${NEO4J_USER}/${NEO4J_PASSWORD}

      volumes:
      neo4j_data:
   ```

5. Once you start the service, it will be available at `http://localhost:8000` (or the port you have specified in the docker compose file).

6. You may access the swagger docs at `http://localhost:8000/docs`. You may also access redocs at `http://localhost:8000/redoc`.

7. You may also access the neo4j browser at `http://localhost:7474` (the port depends on the neo4j instance you are using).
```

### File: AGENTS.md
```md
# Repository Guidelines

## Project Structure & Module Organization
Graphiti's core library lives under `graphiti_core/`, split into domain modules such as `nodes.py`, `edges.py`, `models/`, and `search/` for retrieval pipelines. Service adapters and API glue reside in `server/graph_service/`, while the MCP integration lives in `mcp_server/`. Shared assets and collateral sit in `images/` and `examples/`. Tests cover the package via `tests/`, with configuration in `conftest.py`, `pytest.ini`, and Docker compose files for optional services. Tooling manifests live at the repo root, including `pyproject.toml`, `Makefile`, and deployment compose files.

## Build, Test, and Development Commands
- `uv sync --extra dev`: install the dev environment declared in `pyproject.toml`.
- `make format`: run `ruff` to sort imports and apply the canonical formatter.
- `make lint`: execute `ruff` plus `pyright` type checks against `graphiti_core`.
- `make test`: run the full `pytest` suite (`uv run pytest`).
- `uv run pytest tests/path/test_file.py`: target a specific module or test selection.
- `docker-compose -f docker-compose.test.yml up`: provision local graph/search dependencies for integration flows.

## Coding Style & Naming Conventions
Python code uses 4-space indentation, 100-character lines, and prefers single quotes as configured in `pyproject.toml`. Modules, files, and functions stay snake_case; Pydantic models in `graphiti_core/models` use PascalCase with explicit type hints. Keep side-effectful code inside drivers or adapters (`graphiti_core/driver`, `graphiti_core/utils`) and rely on pure helpers elsewhere. Run `make format` before committing to normalize imports and docstring formatting.

## Testing Guidelines
Author tests alongside features under `tests/`, naming files `test_<feature>.py` and functions `test_<behavior>`. Use `@pytest.mark.integration` for database-reliant scenarios so CI can gate them. Reproduce regressions with a failing test first and validate fixes via `uv run pytest -k "pattern"`. Start required backing services through `docker-compose.test.yml` when running integration suites locally.

## Commit & Pull Request Guidelines
Commits use an imperative, present-tense summary (for example, `add async cache invalidation`) optionally suffixed with the PR number as seen in history (`(#927)`). Squash fixups and keep unrelated changes isolated. Pull requests should include: a concise description, linked tracking issue, notes about schema or API impacts, and screenshots or logs when behavior changes. Confirm `make lint` and `make test` pass locally, and update docs or examples when public interfaces shift.

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Graphiti is a Python framework for building temporally-aware knowledge graphs designed for AI agents. It enables real-time incremental updates to knowledge graphs without batch recomputation, making it suitable for dynamic environments.

Key features:

- Bi-temporal data model with explicit tracking of event occurrence times
- Hybrid retrieval combining semantic embeddings, keyword search (BM25), and graph traversal
- Support for custom entity definitions via Pydantic models
- Integration with Neo4j and FalkorDB as graph storage backends
- Optional OpenTelemetry distributed tracing support

## Development Commands

### Main Development Commands (run from project root)

```bash
# Install dependencies
uv sync --extra dev

# Format code (ruff import sorting + formatting)
make format

# Lint code (ruff + pyright type checking)
make lint

# Run tests
make test

# Run all checks (format, lint, test)
make check
```

### Server Development (run from server/ directory)

```bash
cd server/
# Install server dependencies
uv sync --extra dev

# Run server in development mode
uvicorn graph_service.main:app --reload

# Format, lint, test server code
make format
make lint
make test
```

### MCP Server Development (run from mcp_server/ directory)

```bash
cd mcp_server/
# Install MCP server dependencies
uv sync

# Run with Docker Compose
docker-compose up
```

## Code Architecture

### Core Library (`graphiti_core/`)

- **Main Entry Point**: `graphiti.py` - Contains the main `Graphiti` class that orchestrates all functionality
- **Graph Storage**: `driver/` - Database drivers for Neo4j and FalkorDB
- **LLM Integration**: `llm_client/` - Clients for OpenAI, Anthropic, Gemini, Groq
- **Embeddings**: `embedder/` - Embedding clients for various providers
- **Graph Elements**: `nodes.py`, `edges.py` - Core graph data structures
- **Search**: `search/` - Hybrid search implementation with configurable strategies
- **Prompts**: `prompts/` - LLM prompts for entity extraction, deduplication, summarization
- **Utilities**: `utils/` - Maintenance operations, bulk processing, datetime handling

### Server (`server/`)

- **FastAPI Service**: `graph_service/main.py` - REST API server
- **Routers**: `routers/` - API endpoints for ingestion and retrieval
- **DTOs**: `dto/` - Data transfer objects for API contracts

### MCP Server (`mcp_server/`)

- **MCP Implementation**: `graphiti_mcp_server.py` - Model Context Protocol server for AI assistants
- **Docker Support**: Containerized deployment with Neo4j

## Testing

- **Unit Tests**: `tests/` - Comprehensive test suite using pytest
- **Integration Tests**: Tests marked with `_int` suffix require database connections
- **Evaluation**: `tests/evals/` - End-to-end evaluation scripts

## Configuration

### Environment Variables

- `OPENAI_API_KEY` - Required for LLM inference and embeddings
- `USE_PARALLEL_RUNTIME` - Optional boolean for Neo4j parallel runtime (enterprise only)
- Provider-specific keys: `ANTHROPIC_API_KEY`, `GOOGLE_API_KEY`, `GROQ_API_KEY`, `VOYAGE_API_KEY`

### Database Setup

- **Neo4j**: Version 5.26+ required, available via Neo4j Desktop
  - Database name defaults to `neo4j` (hardcoded in Neo4jDriver)
  - Override by passing `database` parameter to driver constructor
- **FalkorDB**: Version 1.1.2+ as alternative backend
  - Database name defaults to `default_db` (hardcoded in FalkorDriver)
  - Override by passing `database` parameter to driver constructor

## Development Guidelines

### Code Style

- Use Ruff for formatting and linting (configured in pyproject.toml)
- Line length: 100 characters
- Quote style: single quotes
- Type checking with Pyright is enforced
- Main project uses `typeCheckingMode = "basic"`, server uses `typeCheckingMode = "standard"`

### Testing Requirements

- Run tests with `make test` or `pytest`
- Integration tests require database connections and are marked with `_int` suffix
- Use `pytest-xdist` for parallel test execution
- Run specific test files: `pytest tests/test_specific_file.py`
- Run specific test methods: `pytest tests/test_file.py::test_method_name`
- Run only integration tests: `pytest tests/ -k "_int"`
- Run only unit tests: `pytest tests/ -k "not _int"`

### LLM Provider Support

The codebase supports multiple LLM providers but works best with services supporting structured output (OpenAI, Gemini). Other providers may cause schema validation issues, especially with smaller models.

#### Current LLM Models (as of November 2025)

**OpenAI Models:**
- **GPT-5 Family** (Reasoning models, require temperature=0):
  - `gpt-5-mini` - Fast reasoning model
  - `gpt-5-nano` - Smallest reasoning model
- **GPT-4.1 Family** (Standard models):
  - `gpt-4.1` - Full capability model
  - `gpt-4.1-mini` - Efficient model for most tasks
  - `gpt-4.1-nano` - Lightweight model
- **Legacy Models** (Still supported):
  - `gpt-4o` - Previous generation flagship
  - `gpt-4o-mini` - Previous generation efficient

**Anthropic Models:**
- **Claude 4.5 Family** (Latest):
  - `claude-sonnet-4-5-latest` - Flagship model, auto-updates
  - `claude-sonnet-4-5-20250929` - Pinned Sonnet version from September 2025
  - `claude-haiku-4-5-latest` - Fast model, auto-updates
- **Claude 3.7 Family**:
  - `claude-3-7-sonnet-latest` - Auto-updates
  - `claude-3-7-sonnet-20250219` - Pinned version from February 2025
- **Claude 3.5 Family**:
  - `claude-3-5-sonnet-latest` - Auto-updates
  - `claude-3-5-sonnet-20241022` - Pinned version from October 2024
  - `claude-3-5-haiku-latest` - Fast model

**Google Gemini Models:**
- **Gemini 2.5 Family** (Latest):
  - `gemini-2.5-pro` - Flagship reasoning and multimodal
  - `gemini-2.5-flash` - Fast, efficient
- **Gemini 2.0 Family**:
  - `gemini-2.0-flash` - Experimental fast model
- **Gemini 1.5 Family** (Stable):
  - `gemini-1.5-pro` - Production-stable flagship
  - `gemini-1.5-flash` - Production-stable efficient

**Note**: Model names like `gpt-5-mini`, `gpt-4.1`, and `gpt-4.1-mini` used in this codebase are valid OpenAI model identifiers. The GPT-5 family are reasoning models that require `temperature=0` (automatically handled in the code).

### MCP Server Usage Guidelines

When working with the MCP server, follow the patterns established in `mcp_server/cursor_rules.md`:

- Always search for existing knowledge before adding new information
- Use specific entity type filters (`Preference`, `Procedure`, `Requirement`)
- Store new information immediately using `add_memory`
- Follow discovered procedures and respect established preferences
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or
  advances of any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email
  address, without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
founders@getzep.com.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: conftest.py
```py
import os
import sys

# This code adds the project root directory to the Python path, allowing imports to work correctly when running tests.
# Without this file, you might encounter ModuleNotFoundError when trying to import modules from your project, especially when running tests.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__))))

from tests.helpers_test import graph_driver, mock_embedder

__all__ = ['graph_driver', 'mock_embedder']

```

### File: CONTRIBUTING.md
```md
# Contributing to Graphiti

We're thrilled you're interested in contributing to Graphiti! As firm believers in the power of open source collaboration, we're committed to building not just a tool, but a vibrant community where developers of all experience levels can make meaningful contributions.

When I first joined this project, I was overwhelmed trying to figure out where to start. Someone eventually pointed me to a random "good first issue," but I later discovered there were multiple ways I could have contributed that would have better matched my skills and interests.

We've restructured our contribution paths to solve this problem:

# Four Ways to Get Involved

### Pick Up Existing Issues

Our developers regularly tag issues with "help wanted" and "good first issue." These are pre-vetted tasks with clear scope and someone ready to help you if you get stuck.

### Create Your Own Tickets

See something that needs fixing? Have an idea for an improvement? You don't need permission to identify problems. The people closest to the pain are often best positioned to describe the solution.

For **feature requests**, tell us the story of what you're trying to accomplish. What are you working on? What's getting in your way? What would make your life easier? Submit these through our [GitHub issue tracker](https://github.com/getzep/graphiti/issues) with a "Feature Request" label.

For **bug reports**, we need enough context to reproduce the problem. Use the [GitHub issue tracker](https://github.com/getzep/graphiti/issues) and include:

- A clear title that summarizes the specific problem
- What you were trying to do when you encountered the bug
- What you expected to happen
- What actually happened
- A code sample or test case that demonstrates the issue

### Share Your Use Cases

Sometimes the most valuable contribution isn't code. If you're using our project in an interesting way, add it to the [examples](https://github.com/getzep/graphiti/tree/main/examples) folder. This helps others discover new possibilities and counts as a meaningful contribution. We regularly feature compelling examples in our blog posts and videos - your work might be showcased to the broader community!

### Help Others in Discord

Join our [Discord server](https://discord.com/invite/W8Kw6bsgXQ) community and pitch in at the helpdesk. Answering questions and helping troubleshoot issues is an incredibly valuable contribution that benefits everyone. The knowledge you share today saves someone hours of frustration tomorrow.

## What happens next?

### Notes for Large Changes
> Please keep the changes as concise as possible. For major architectural changes (>500 LOC), we would expect a GitHub issue (RFC) discussing the technical design and justification. Otherwise, we will tag it with rfc-required and might not go through the PR.

Once you've found an issue tagged with "good first issue" or "help wanted," or prepared an example to share, here's how to turn that into a contribution:

1. Share your approach in the issue discussion or [Discord](https://discord.com/invite/W8Kw6bsgXQ) before diving deep into code. This helps ensure your solution adheres to the architecture of Graphiti from the start and saves you from potential rework.

2. Fork the repo, make your changes in a branch, and submit a PR. We've included more detailed technical instructions below; be open to feedback during review.

## Setup

1. Fork the repository on GitHub.
2. Clone your fork locally:
   ```
   git clone https://github.com/getzep/graphiti
   cd graphiti
   ```
3. Set up your development environment:

   - Ensure you have Python 3.10+ installed.
   - Install uv: https://docs.astral.sh/uv/getting-started/installation/
   - Install project dependencies:
     ```
     make install
     ```
   - To run integration tests, set the appropriate environment variables

     ```
     export TEST_OPENAI_API_KEY=...
     export TEST_OPENAI_MODEL=...
     export TEST_ANTHROPIC_API_KEY=...

     # For Neo4j
     export TEST_URI=neo4j://...
     export TEST_USER=...
     export TEST_PASSWORD=...
     ```

## Making Changes

1. Create a new branch for your changes:
   ```
   git checkout -b your-branch-name
   ```
2. Make your changes in the codebase.
3. Write or update tests as necessary.
4. Run the tests to ensure they pass:
   ```
   make test
   ```
5. Format your code:
   ```
   make format
   ```
6. Run linting checks:
   ```
   make lint
   ```

## Submitting Changes

1. Commit your changes:
   ```
   git commit -m "Your detailed commit message"
   ```
2. Push to your fork:
   ```
   git push origin your-branch-name
   ```
3. Submit a pull request through the GitHub website to https://github.com/getzep/graphiti.

## Pull Request Guidelines

- Provide a clear title and description of your changes.
- Include any relevant issue numbers in the PR description.
- Ensure all tests pass and there are no linting errors.
- Update documentation if you're changing functionality.

## Code Style and Quality

We use several tools to maintain code quality:

- Ruff for linting and formatting
- Pyright for static type checking
- Pytest for testing

Before submitting a pull request, please run:

```
make check
```

This command will format your code, run linting checks, and execute tests.

## Third-Party Integrations

When contributing integrations for third-party services (LLM providers, embedding services, databases, etc.), please follow these patterns:

### Optional Dependencies

All third-party integrations must be optional dependencies to keep the core library lightweight. Follow this pattern:

1. **Add to `pyproject.toml`**: Define your dependency as an optional extra AND include it in the dev extra:
   ```toml
   [project.optional-dependencies]
   your-service = ["your-package>=1.0.0"]
   dev = [
       # ... existing dev dependencies
       "your-package>=1.0.0",  # Include all optional extras here
       # ... other dependencies
   ]
   ```

2. **Use TYPE_CHECKING pattern**: In your integration module, import dependencies conditionally:
   ```python
   from typing import TYPE_CHECKING
   
   if TYPE_CHECKING:
       import your_package
       from your_package import SomeType
   else:
       try:
           import your_package
           from your_package import SomeType
       except ImportError:
           raise ImportError(
               'your-package is required for YourServiceClient. '
               'Install it with: pip install graphiti-core[your-service]'
           ) from None
   ```

3. **Benefits of this pattern**:
   - Fast startup times (no import overhead during type checking)
   - Clear error messages with installation instructions
   - Proper type hints for development
   - Consistent user experience

4. **Do NOT**:
   - Add optional imports to `__init__.py` files
   - Use direct imports without error handling
   - Include optional dependencies in the main `dependencies` list

### Integration Structure

- Place LLM clients in `graphiti_core/llm_client/`
- Place embedding clients in `graphiti_core/embedder/`
- Place database drivers in `graphiti_core/driver/`
- Follow existing naming conventions (e.g., `your_service_client.py`)

### Adding a Graph Driver

Graphiti's driver layer is backend-agnostic. To add support for a new graph database, mirror the existing drivers in
`graphiti_core/driver/` and keep the implementation split between the top-level driver and provider-specific
operations.

1. Add the new provider to `graphiti_core/driver/driver.py` in `GraphProvider`.
2. Create `graphiti_core/driver/<backend>_driver.py` implementing the `GraphDriver` interface:
   `execute_query()`, `session()`, `close()`, `build_indices_and_constraints()`, and `delete_all_indexes()`.
3. Add `graphiti_core/driver/<backend>/operations/` and implement the operations interfaces from
   `graphiti_core/driver/operations/`:
   `EntityNodeOperations`, `EpisodeNodeOperations`, `CommunityNodeOperations`, `SagaNodeOperations`,
   `EntityEdgeOperations`, `EpisodicEdgeOperations`, `CommunityEdgeOperations`, `HasEpisodeEdgeOperations`,
   `NextEpisodeEdgeOperations`, `SearchOperations`, and `GraphMaintenanceOperations`.
4. Expose those concrete operations from the driver via the corresponding `@property` accessors on `GraphDriver`.
5. Add provider-specific query variants to `graphiti_core/models/nodes/node_db_queries.py` and
   `graphiti_core/models/edges/edge_db_queries.py`.
6. If the backend needs connection or transaction management, implement a matching `GraphDriverSession`.
7. Register the backend dependency in `pyproject.toml` under `[project.optional-dependencies]` and add tests under
   `tests/driver/`.

For reference implementations, start with `graphiti_core/driver/neo4j_driver.py`,
`graphiti_core/driver/falkordb_driver.py`, `graphiti_core/driver/kuzu_driver.py`, and
`graphiti_core/driver/neptune_driver.py`.

### Testing

- Add comprehensive tests in the appropriate `tests/` subdirectory
- Mark integration tests with `_int` suffix if they require external services
- Include both unit tests and integration tests where applicable

# Questions?

Stuck on a contribution or have a half-formed idea? Come say hello in our [Discord server](https://discord.com/invite/W8Kw6bsgXQ). Whether you're ready to contribute or just want to learn more, we're happy to have you! It's faster than GitHub issues and you'll find both maintainers and fellow contributors ready to help.

Thank you for contributing to Graphiti!

```

### File: depot.json
```json
{"id":"v9jv1mlpwc"}

```

### File: ellipsis.yaml
```yaml
# See https://docs.ellipsis.dev for all available configurations.

version: 1.3

pr_address_comments:
  delivery: "new_commit"
pr_review:
  auto_review_enabled: true  # enable auto-review of PRs
  auto_summarize_pr: true  # enable auto-summary of PRs
  confidence_threshold: 0.8  # Threshold for how confident Ellipsis needs to be in order to leave a comment, in range [0.0-1.0]
  rules:  # customize behavior
    - "Ensure the copyright notice is present as the header of all Python files"
    - "Ensure code is idiomatic"
    - "Code should be DRY (Don't Repeat Yourself)"
    - "Extremely Complicated Code Needs Comments"
    - "Use Descriptive Variable and Constant Names"
    - "Follow the Single Responsibility Principle"
    - "Function and Method Naming Should Follow Consistent Patterns"
    - "There should no secrets or credentials in the code"
    - "Don't log sensitive data"
```

### File: OTEL_TRACING.md
```md
# OpenTelemetry Tracing in Graphiti

Graphiti supports OpenTelemetry distributed tracing. Tracing is optional - without a tracer, operations use no-op implementations with zero overhead.

## Installation

```bash
uv add opentelemetry-sdk
```

## Basic Usage

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import ConsoleSpanExporter, SimpleSpanProcessor
from graphiti_core import Graphiti

# Set up OpenTelemetry
provider = TracerProvider()
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)

# Get tracer and pass to Graphiti
tracer = trace.get_tracer(__name__)
graphiti = Graphiti(
    uri="bolt://localhost:7687",
    user="neo4j",
    PASSWORD='[REDACTED_PASSWORD]',
    tracer=tracer,
    trace_span_prefix="myapp.graphiti"  # Optional, defaults to "graphiti"
)
```

## With Kuzu (In-Memory)

```python
from graphiti_core.driver.kuzu_driver import KuzuDriver

kuzu_driver = KuzuDriver()
graphiti = Graphiti(graph_driver=kuzu_driver, tracer=tracer)
```

## Example

See `examples/opentelemetry/` for a complete working example with stdout tracing


```

### File: SECURITY.md
```md
# Security Policy

## Supported Versions

Use this section to tell people about which versions of your project are
currently being supported with security updates.

| Version | Supported          |
|---------|--------------------|
| 0.x     | :white_check_mark: |


## Reporting a Vulnerability

Please use GitHub's Private Vulnerability Reporting mechanism found in the Security section of this repo.

```

### File: zep_cla.md
```md
# Contributor License Agreement (CLA)

In order to clarify the intellectual property license granted with Contributions from any person or entity, Zep Software, Inc. ("Zep") must have a Contributor License Agreement ("CLA") on file that has been signed by each Contributor, indicating agreement to the license terms below. This license is for your protection as a Contributor as well as the protection of Zep; it does not change your rights to use your own Contributions for any other purpose.

You accept and agree to the following terms and conditions for Your present and future Contributions submitted to Zep. Except for the license granted herein to Zep and recipients of software distributed by Zep, You reserve all right, title, and interest in and to Your Contributions.

## Definitions

**"You" (or "Your")** shall mean the copyright owner or legal entity authorized by the copyright owner that is making this Agreement with Zep. For legal entities, the entity making a Contribution and all other entities that control, are controlled by, or are under common control with that entity are considered to be a single Contributor. For the purposes of this definition, "control" means:

i. the power, direct or indirect, to cause the direction or management of such entity, whether by contract or otherwise, or
ii. ownership of fifty percent (50%) or more of the outstanding shares, or
iii. beneficial ownership of such entity.

**"Contribution"** shall mean any original work of authorship, including any modifications or additions to an existing work, that is intentionally submitted by You to Zep for inclusion in, or documentation of, any of the products owned or managed by Zep (the "Work"). For the purposes of this definition, "submitted" means any form of electronic, verbal, or written communication sent to Zep or its representatives, including but not limited to communication on electronic mailing lists, source code control systems, and issue tracking systems that are managed by, or on behalf of, Zep for the purpose of discussing and improving the Work, but excluding communication that is conspicuously marked or otherwise designated in writing by You as "Not a Contribution."

## Grant of Copyright License

Subject to the terms and conditions of this Agreement, You hereby grant to Zep and to recipients of software distributed by Zep a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable copyright license to reproduce, prepare derivative works of, publicly display, publicly perform, sublicense, and distribute Your Contributions and such derivative works.

## Grant of Patent License

Subject to the terms and conditions of this Agreement, You hereby grant to Zep and to recipients of software distributed by Zep a perpetual, worldwide, non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this section) patent license to make, have made, use, offer to sell, sell, import, and otherwise transfer the Work, where such license applies only to those patent claims licensable by You that are necessarily infringed by Your Contribution(s) alone or by combination of Your Contribution(s) with the Work to which such Contribution(s) was submitted. If any entity institutes patent litigation against You or any other entity (including a cross-claim or counterclaim in a lawsuit) alleging that your Contribution, or the Work to which you have contributed, constitutes direct or contributory patent infringement, then any patent licenses granted to that entity under this Agreement for that Contribution or Work shall terminate as of the date such litigation is filed.

## Representations

You represent that you are legally entitled to grant the above license. If your employer(s) has rights to intellectual property that you create that includes your Contributions, you represent that you have received permission to make Contributions on behalf of that employer, that your employer has waived such rights for your Contributions to Zep, or that your employer has executed a separate Corporate CLA with Zep.

You represent that each of Your Contributions is Your original creation (see section 7 for submissions on behalf of others). You represent that Your Contribution submissions include complete details of any third-party license or other restriction (including, but not limited to, related patents and trademarks) of which you are personally aware and which are associated with any part of Your Contributions.

## Support

You are not expected to provide support for Your Contributions, except to the extent You desire to provide support. You may provide support for free, for a fee, or not at all. Unless required by applicable law or agreed to in writing, You provide Your Contributions on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied, including, without limitation, any warranties or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A PARTICULAR PURPOSE.

## Third-Party Submissions

Should You wish to submit work that is not Your original creation, You may submit it to Zep separately from any Contribution, identifying the complete details of its source and of any license or other restriction (including, but not limited to, related patents, trademarks, and license agreements) of which you are personally aware, and conspicuously marking the work as "Submitted on behalf of a third party: [named here]".

## Notifications

You agree to notify Zep of any facts or circumstances of which you become aware that would make these representations inaccurate in any respect.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
