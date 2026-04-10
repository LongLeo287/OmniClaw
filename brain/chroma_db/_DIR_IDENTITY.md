---
id: chroma_db
type: directory_identity
namespace: brain.chroma_db
owner: OSF_Daemon
status: standard_v5
description: "Persistent vector database (ChromaDB v1.5.6) powering OmniClaw's semantic memory layer. Stores 384-dim embeddings (all-MiniLM-L6-v2) for the synapse_nodes collection — enabling similarity search across all ingested knowledge nodes."
registered_by: OMA_AI_FORGER
tags: ["vector_database", "chromadb", "semantic_memory", "hnsw", "embeddings", "aaak_memory"]
collection: synapse_nodes
embedding_model: all-MiniLM-L6-v2
embedding_dimension: 384
node_count: 18
last_ingest: "2026-04-10T02:19:58"
---

# ChromaDB — Cơ Sở Dữ Liệu Vector Ngữ Nghĩa
*Persistent Semantic Vector Database*

Thư mục này chứa toàn bộ cơ sở hạ tầng lưu trữ vector của OmniClaw. Mọi tri thức được nạp qua pipeline CIV và ORPHAN_SWEEP đều được embedding và lưu tại đây dưới dạng **`aaak_memory`** nodes, phục vụ cho các truy vấn tìm kiếm ngữ nghĩa (semantic similarity search) của OA_Academy và các agents liên quan.

## Chức Năng Cốt Lõi

| Chức năng | Chi tiết |
|---|---|
| **Semantic Search** | Tìm kiếm theo nghĩa, không phải từ khóa (ANN via HNSW) |
| **Embedding Storage** | 18 nodes × 384 chiều (float32) |
| **Metadata Index** | Full-text search + structured metadata per node |
| **Collection** | `synapse_nodes` — unified memory namespace |

## Topological View

```mermaid
graph TD
  Parent("brain") --> Node("chroma_db")

  Node --> DB("chroma.sqlite3<br/>[256KB] Metadata + Queue + FTS")
  Node --> HNSW("48aea028-e32b-4a00-86e2-32e46d33fcd2/<br/>[HNSW Vector Index]")
  Node --> Identity("_DIR_IDENTITY.md")
  Node --> Map("_REGIONAL_MAP.md")

  HNSW --> H1("data_level0.bin<br/>[164KB] Vector matrix 18×384")
  HNSW --> H2("header.bin<br/>[100B] HNSW config: dim=384, M=16")
  HNSW --> H3("length.bin<br/>[400B] Node count")
  HNSW --> H4("link_lists.bin<br/>[0B] Graph links - grows with scale")

  DB --> C1("collections: synapse_nodes")
  DB --> C2("embeddings: 18 nodes")
  DB --> C3("embedding_metadata: 72 rows")
  DB --> C4("embedding_fulltext_search: FTS index")

  style HNSW fill:#1a3a5c,color:#fff
  style DB fill:#1a3a5c,color:#fff
```

## Data Flow

```
CIV Intake / ORPHAN_SWEEP
        │
        ▼
  OA_Academy Daemon
  (encode → all-MiniLM-L6-v2)
        │
        ▼
  chroma.sqlite3 ──► embeddings_queue
        │
        ▼ (flush on PersistentClient open)
  48aea028.../
  data_level0.bin  ──► HNSW Graph index
        │
        ▼
  semantic search queries
  (OA_Synapse / Knowledge Router)
```

## Node Naming Convention

```
node_{SOURCE}_{repo_name}_{HHMMSS}_{hash8}
  │       │         │          │        │
  │       │         │          │        └─ MD5 hash (8 chars)
  │       │         │          └─ ingestion timestamp
  │       │         └─ repository name
  │       └─ CIV_FETCHED | ORPHAN_SWEEP | mempalace | ...
  └─ fixed prefix
```

> [!CAUTION]
> Thư mục `48aea028-e32b-4a00-86e2-32e46d33fcd2/` được ChromaDB tự sinh theo segment UUID. **KHÔNG ĐỔI TÊN, KHÔNG XÓA THỦ CÔNG.** Mọi thao tác phải qua ChromaDB Python client.

> [!NOTE]
> `link_lists.bin` = 0 bytes là **bình thường** khi số nodes < M_threshold (~100). File này tự phát triển khi collection scale lên.

---
*OmniClaw V5.0 | Forged by AI Architect | brain.chroma_db | 2026-04-10*
