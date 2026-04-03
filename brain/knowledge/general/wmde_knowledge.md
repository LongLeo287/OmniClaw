---
id: wmde-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:46.544696
---

# KNOWLEDGE EXTRACT: wmde
> **Extracted on:** 2026-03-30 18:01:18
> **Source:** wmde

---

## File: `WikidataMCP.md`
```markdown
# 📦 wmde/WikidataMCP [🔖 PENDING/APPROVE]
🔗 https://github.com/wmde/WikidataMCP
🌐 https://wd-mcp.wmcloud.org/

## Meta
- **Stars:** ⭐ 24 | **Forks:** 🍴 5
- **Language:** Python | **License:** BSD-3-Clause
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Model Context Protocol for Wikidata

## README (trích đầu)
```
# Wikidata MCP
The **Wikidata MCP (Model Context Protocol)** provides a set of standardized tools that allow large language models (LLMs) to explore and query Wikidata programmatically. It is designed for agentic AI or AI workflows that need to search, inspect, and query Wikidata, without relying on hardcoded assumptions about its structure or content.

The Wikidata MCP server is running at [https://wd-mcp.wmcloud.org/](https://wd-mcp.wmcloud.org/) \
You can connect your AI application to it at [https://wd-mcp.wmcloud.org/mcp](https://wd-mcp.wmcloud.org/mcp)
Tools are exposed as API endpoints and can be tested interactively at [https://wd-mcp.wmcloud.org/docs](https://wd-mcp.wmcloud.org/docs)

---

## 🧰 Tools
1. `search_items(query: str, lang: str = "en") -> str`
Searches Wikidata items (QIDs) using vector search when available and falls back to keyword search when needed. Returns matching QIDs with labels and descriptions.

**Use When**: Starting exploration from a concept or natural-language description.

2. `search_properties(query: str, lang: str = "en") -> str`
Searches Wikidata properties (PIDs) using vector search when available and falls back to keyword search when needed. Returns matching PIDs with labels and descriptions.

**Use When**: You need to find the right Wikidata property for relationships in statements or SPARQL.

3. `get_statements(entity_id: str, include_external_ids: bool = False, lang: str = "en") -> str`
Returns direct statements (property-value pairs) for an entity in triplet-like text form. This tool excludes qualifiers, references, and deprecated values.

**Use When**: You want a fast structural overview of an entity.

4. `get_statement_values(entity_id: str, property_id: str, lang: str = "en") -> str`
Returns all statement values for an entity-property pair, including qualifiers, references, and all ranks.

**Use When**: You need full statement detail for auditing, fact-checking, or provenance-sensitive tasks.

5. `get_instance_and_subclass_hierarchy(entity_id: str, max_depth: int = 5, lang: str = "en") -> str`
Retrieves hierarchical context using "instance of" (P31) and "subclass of" (P279), returning JSON-formatted hierarchy data.

**Use When**: You need to understand entity classification before building filters in SPARQL.

6. `execute_sparql(sparql: str, K: int = 10) -> str`
Executes a SPARQL query against Wikidata and returns up to `K` rows as CSV text.

**Use When**: You want structured retrieval and verification from Wikidata Query Service.

---

## 🚀 Running Locally
Run:

```bash
uv run python main.py
```

Then open:
- `http://localhost:8000/` for project page
- `http://localhost:8000/docs` for interactive Swagger UI
- `http://localhost:8000/mcp` for MCP clients

With Docker:

```bash
docker compose up --build
```

---

## 🌐 Services
### Vector Search

This service interfaces with the [Wikidata Vector Database](https://wd-vectordb.wmcloud.org/), enabling semantic search over Wikidata items using natural langua
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

