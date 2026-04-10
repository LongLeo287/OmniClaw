---
id: chroma_db_regional_map
type: regional_map
zone: OmniClaw\brain\chroma_db
generated_at: 2026-04-10
total_files: 3
total_subdirs: 1
collection_count: 1
embedding_count: 18
---

# _REGIONAL_MAP — D:\OmniClaw\brain\chroma_db

## Subdirectories (1)

| Name | Type | Contents | Ghi chú |
|------|------|----------|---------|
| `48aea028-e32b-4a00-86e2-32e46d33fcd2/` | HNSW Vector Index | 4 files | Segment của collection `synapse_nodes` — do ChromaDB tự quản lý |

## Files (3)

| File | Size | Chức năng |
|------|------|-----------|
| `chroma.sqlite3` | 256 KB | SQLite backend: collections, embedding queue, metadata, FTS index |
| `_DIR_IDENTITY.md` | — | Khai báo định danh thư mục |
| `_REGIONAL_MAP.md` | — | Bản đồ khu vực (file này) |

## HNSW Segment Files

| File | Size | Chức năng |
|------|------|-----------|
| `data_level0.bin` | 164 KB | Ma trận vector float32 (18 nodes × 384 dim) |
| `header.bin` | 100 B | HNSW config: `dim=384, M=16, ef_construction=200` |
| `length.bin` | 400 B | Node count registry |
| `link_lists.bin` | 0 B | Graph links tầng cao (rỗng khi nodes < threshold) |

## Collection Registry

| Collection | ID | Dimension | Nodes | Model |
|---|---|---|---|---|
| `synapse_nodes` | `2d5dd4fc-61bd-4d49-9f5d-e0b8d0eaf226` | 384 | 18 | all-MiniLM-L6-v2 |

## Ingest History

| Batch | Nodes | Timestamp | Nguồn |
|---|---|---|---|
| CIV_FETCHED | 14 | 2026-04-09 08:52–09:00 | CIV Intake pipeline |
| mempalace | 1 | 2026-04-09 10:31 | Direct ingest |
| ORPHAN_SWEEP | 3 | 2026-04-09 17:09 → 2026-04-10 02:19 | Orphan sweep pipeline |

---
*OmniClaw V5.0 | brain.chroma_db | Generated: 2026-04-10*
