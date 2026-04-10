---
id: chroma_db
type: directory_identity
namespace: brain.example.path
owner: OSF_Daemon
status: standard_v5
description: "This directory contains the database used by OmniClaw for storing vectorized data and metadata."
registered_by: OMA_AI_FORGER
tags: ["database", "vector_storage"]
---

# Chroma Db Identity

This directory contains the database used by OmniClaw for storing vectorized data and metadata.

## Topological View

```mermaid
graph TD
  Parent("brain") --> Node("chroma_db")
  Node --> Sub1("chroma.sqlite3")
```

---
*OmniClaw V5.0 | Forged by AI Architect | Evaluated dynamically*
