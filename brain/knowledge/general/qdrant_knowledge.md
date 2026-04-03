---
id: qdrant-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:05.001314
---

# KNOWLEDGE EXTRACT: qdrant
> **Extracted on:** 2026-03-30 17:52:11
> **Source:** qdrant

---

## File: `qdrant.md`
```markdown
# 📦 qdrant/qdrant [🔖 PENDING/APPROVE]
🔗 https://github.com/qdrant/qdrant
🌐 https://qdrant.tech

## Meta
- **Stars:** ⭐ 29872 | **Forks:** 🍴 2138
- **Language:** Rust | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/

## README (trích đầu)
```
<p align="center">
  <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://github.com/qdrant/qdrant/raw/master/docs/logo-dark.svg">
      <source media="(prefers-color-scheme: light)" srcset="https://github.com/qdrant/qdrant/raw/master/docs/logo-light.svg">
      <img height="100" alt="Qdrant" src="https://github.com/qdrant/qdrant/raw/master/docs/logo.svg">
  </picture>
</p>

<p align="center">
    <b>Vector Search Engine for the next generation of AI applications</b>
</p>

<p align=center>
    <a href="https://github.com/qdrant/qdrant/actions/workflows/rust.yml"><img src="https://img.shields.io/github/actions/workflow/status/qdrant/qdrant/rust.yml?style=flat-square" alt="Tests status"></a>
    <a href="https://api.qdrant.tech/"><img src="https://img.shields.io/badge/Docs-OpenAPI%203.0-success?style=flat-square" alt="OpenAPI Docs"></a>
    <a href="https://github.com/qdrant/qdrant/blob/master/LICENSE"><img src="https://img.shields.io/github/license/qdrant/qdrant?style=flat-square" alt="Apache 2.0 License"></a>
    <a href="https://qdrant.to/discord"><img src="https://img.shields.io/discord/907569970500743200?logo=Discord&style=flat-square&color=7289da" alt="Discord"></a>
    <a href="https://qdrant.to/roadmap"><img src="https://img.shields.io/badge/Roadmap-2025-bc1439.svg?style=flat-square" alt="Roadmap 2025"></a>
    <a href="https://cloud.qdrant.io/"><img src="https://img.shields.io/badge/Qdrant-Cloud-24386C.svg?logo=cloud&style=flat-square" alt="Qdrant Cloud"></a>
</p>

**Qdrant** (read: _quadrant_) is a vector similarity search engine and vector database.
It provides a production-ready service with a convenient API to store, search, and manage points—vectors with an additional payload
Qdrant is tailored to extended filtering support. It makes it useful for all sorts of neural-network or semantic-based matching, faceted search, and other applications.

Qdrant is written in Rust 🦀, which makes it fast and reliable even under high load. See [benchmarks](https://qdrant.tech/benchmarks/).

With Qdrant, embeddings or neural network encoders can be turned into full-fledged applications for matching, searching, recommending, and much more!

Qdrant is also available as a fully managed **[Qdrant Cloud](https://cloud.qdrant.io/)** ⛅ including a **free tier**.

<p align="center">
<strong><a href="docs/QUICK_START.md">Quick Start</a> • <a href="#clients">Client Libraries</a> • <a href="#demo-projects">Demo Projects</a> • <a href="#integrations">Integrations</a> • <a href="#contacts">Contact</a>

</strong>
</p>

## Getting Started

### Python

```
pip install qdrant-client
```

The python client offers a convenient way to start with Qdrant locally:

```python
from qdrant_client import QdrantClient
qdrant = QdrantClient(":memory:") # Create in-memory Qdrant instance, for testing, CI/CD
# OR
client = QdrantClient(path="path/to/db")  # Persists changes to disk, fast prototyping
```

### Client-Server

To experience the full power of Qdr
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

