---
id: chroma_segment_hnsw_synapse_nodes
type: directory_identity
namespace: brain.chroma_db.segment
owner: ChromaDB_Engine
status: system_managed
description: "HNSW persisted vector index segment for the 'synapse_nodes' collection. Auto-generated and managed by ChromaDB v1.5.6. Contains the Hierarchical Navigable Small World graph enabling approximate nearest-neighbor (ANN) search across 18 knowledge nodes at 384 dimensions."
registered_by: ChromaDB_Auto
tags: ["hnsw", "vector_index", "segment", "system_managed", "chromadb"]
segment_id: "48aea028-e32b-4a00-86e2-32e46d33fcd2"
segment_type: "urn:chroma:segment/vector/hnsw-local-persisted"
collection: synapse_nodes
collection_id: "2d5dd4fc-61bd-4d49-9f5d-e0b8d0eaf226"
dimension: 384
node_count: 18
---

# HNSW Segment — synapse_nodes Vector Index

> [!CAUTION]
> Thư mục này do **ChromaDB Engine tự quản lý**. KHÔNG chỉnh sửa, đổi tên, hay xóa thủ công bất kỳ file nào. Mọi thao tác phải qua ChromaDB Python client.

Đây là segment lưu trữ **index vector HNSW** (Hierarchical Navigable Small World) cho collection `synapse_nodes`. Khi query semantic search được gửi tới ChromaDB, engine đọc trực tiếp từ các file trong thư mục này để tìm vector gần nhất.

## Topological View

```mermaid
graph TD
  Parent("chroma_db") --> Node("48aea028-e32b-4a00-86e2-32e46d33fcd2/")

  Node --> F1("data_level0.bin<br/>[164KB]<br/>Vector matrix: 18 × 384 float32")
  Node --> F2("header.bin<br/>[100B]<br/>HNSW config: dim=384, M=16, ef=200")
  Node --> F3("length.bin<br/>[400B]<br/>Node count: 18")
  Node --> F4("link_lists.bin<br/>[0B]<br/>Upper-layer graph links")

  style Node fill:#1a3a5c,color:#fff
```

## HNSW Parameters

| Parameter | Value | Ý nghĩa |
|---|---|---|
| `dimension` | 384 | Số chiều mỗi vector (all-MiniLM-L6-v2) |
| `M` | 16 | Số kết nối tối đa mỗi node ở tầng 0 |
| `ef_construction` | 200 | Độ chính xác khi xây index |
| `space` | cosine | Hàm đo khoảng cách |

---
*OmniClaw V5.0 | ChromaDB Segment Identity | System-managed | 2026-04-10*
