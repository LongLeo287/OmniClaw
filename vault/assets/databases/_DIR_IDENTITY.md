---
id: vault_assets_databases
type: data_store
tier: 2
path: D:\OmniClaw\vault\assets\databases
owner: OmniClaw-System
---

# Directory Identity: databases
# Danh Tính Phân Khu: Cơ Sở Dữ Liệu Các Loại (databases)

**Role:** Persistent data storage layer for all vector indices, SQLite databases, and structured JSON data consumed by OmniClaw Daemons.
**Nhiệm Vụ:** Tầng Hầm Dữ Liệu Vĩnh Cửu chuyên chứa Vector Indices, SQLite DBs tĩnh, các bộ cấu trúc JSON mà bầy Daemons đang thèm khát.

## STRICT CONSTRAINTS (ENFORCED BY WATCHDOG) / LUẬT CỨNG (GIÁM SÁT BỞI HỆ THỐNG WATCHDOG OMA)

- ✅ ALLOWED: Files with extensions `.db`, `.sqlite`, `.sqlite3`, `.json`, `.idx`, `.bin`, `.faiss`
- ✅ CHO PHÉP: Đuôi file `.db`, `.sqlite`, `.sqlite3`, `.json`, `.idx`, `.bin`, `.faiss`
- ✅ ALLOWED: Subdirectories that are registered Engine namespaces (e.g. `chromadb`, `weaviate`, `qdrant`, `lancedb`, `neo4j`)
- ✅ CHO PHÉP: Thư mục gánh đuôi đăng ký Namespace hợp lệ (`chromadb`, `weaviate`, `neo4j`...)
- ❌ FORBIDDEN: Any subdirectory named `vault`, `QUARANTINE`, `tmp`, `system`, `core` or any name that mirrors a root-level OmniClaw directory.
- ❌ LUẬT TREO CỔ: Thư mục lai tạp cấm tên như `vault`, `QUARANTINE`, `tmp`, `system`, `core` - chống mọi hình dáng Phân Thân Ác Ma (Mirror Directories).
- ❌ FORBIDDEN: Source code files (`.py`, `.js`, `.ts`, `.sh`)
- ❌ LUẬT TREO CỔ: Tệp Mã Lệnh Máy (`.py`, `.js`, `.ts`) bẩn chân.
- ❌ FORBIDDEN: Repository dumps or raw Git clones
- ❌ LUẬT TREO CỔ: Gói File Bãi Rác Git Clones.

## Enforcement (Xử Lý Tàn Khốc)
Any unauthorized subfolder detected here will be automatically removed by:
`core/ops/scripts/utils/db_hygiene_sweep.py`
Nếu bất kì thư mục chui rúc trái phép nào mọc ở đây, chúng sẽ bị Đao Phủ `db_hygiene_sweep.py` chém văng tự động.

This policy is registered under: `GAP-2026-04-07-002`
Văn Bản Pháp Luật này đã được neo số: `GAP-2026-04-07-002`
