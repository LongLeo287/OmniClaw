---
id: CAPABILITY-MAP-001
type: REFERENCE
domain: [system, skills, plugins, discovery]
dept: all
created: 2026-03-22
version: 1.0
authority: registry_capability
---

# Lực Lượng Công Cụ OmniClaw Corp — Bản Đồ Chức Năng (Capability Map)
## Mục lục Khám phá Skill / Plugin (Dành người và Agent đọc)

> **Mục đích (Purpose):** Đặc vụ `knowledge_navigator` sẽ nội kiểm file này ở Phase 3 để truy vấn chính xác skill/plugin cho từng mã ngành (domain tag) thay vì đoán mò từ khóa rủi ro.  
> Tỷ lệ chính xác bật từ ~65% → ~90% khi ráp với động cơ đồ thị LightRAG.

---

## 🚀 Trục Tiến Hóa (Upgrade Path)

```
HIỆN TẠI (Phase 1): knowledge_navigator tự đọc file này → 90% chính xác
TƯƠNG LAI (Phase 2): Cỗ máy LightRAG lập chỉ mục toàn bộ SKILL.md + manifest.json → 95%+ chính xác
TƯƠNG LAI (Phase 3): Động cơ GitNexus quét cực sâu ảnh hưởng phân nhánh (blast radius) khi độ chế plugin mới
```

---

## 🗺️ Bản Đồ Ngành Vực → Kỹ Năng / Plugin

### Tự Động Hóa AI/ML (RAG, LLMs, Embeddings)
| Nhu Cầu | Công Cụ Gọi | Loại | Đường Dẫn Gốc |
|------|-----|------|------|
| Truy vấn Tri thức cơ bản | `knowledge_enricher` | skill | ecosystem/skills/knowledge_enricher/ |
| Truy vấn Graph Neural RAG | `LightRAG` | plugin | plugins/LightRAG/ |
| Kéo và Nghiền Tài liệu | `open-notebook` | plugin | plugins/open-notebook/ |
| Não bộ Tổng hợp Nghiên cứu | `notebooklm-skill` | plugin | plugins/notebooklm-skill/ |
| Bơm Dữ liệu Đa hình thái | `multi-source-aggregation` | skill | ecosystem/skills/multi-source-aggregation/ |
| Máy Toán Lý Luận Đỉnh Cao | `reasoning_engine` | skill | ecosystem/skills/reasoning_engine/ |
| Phản Xạ Cấu Trúc Nhận Thức | `cognitive_reflector` | skill | ecosystem/skills/cognitive_reflector/ |
| Bộ Định Tuyến (Router) Xuyên Tâm LLMs | `llm_router` | skill | ecosystem/skills/llm_router/ |
| Móc Ruột Data (NLP) | `langextract` | plugin | plugins/langextract/ |

### Cơ Sở Hạ Tầng Backend (Python, API, FastAPI, NodeJS)
| Nhu Cầu | Công Cụ Gọi | Loại | Đường Dẫn Gốc |
|------|-----|------|------|
| Thao Tác Console/Bash Cứng | `shell_assistant` | skill | ecosystem/skills/shell_assistant/ |
| Rà Soát Chất Lượng Sống Chín (Prod QA) | `production_qa` | skill | ecosystem/skills/production_qa/ |
| Đâm Lỗi Cấu Trúc File | `fsd_architectural_linter` | skill | ecosystem/skills/domains/frontend/ |
| Phục Hồi Tai Nạn Tuyến Trình | `resilience_engine` | skill | ecosystem/skills/resilience_engine/ |
| Quét Suy Vỡ Hiệu Suất | `performance_profiler` | skill | ecosystem/skills/performance_profiler/ |
| Khám Bệnh Chẩn Đoán Dữ Liệu | `diagnostics_engine` | skill | ecosystem/skills/diagnostics_engine/ |

### Trưng Bày Web Frontend (React, Vue, Giao Diện UI/UX)
| Nhu Cầu | Công Cụ Gọi | Loại | Đường Dẫn Gốc |
|------|-----|------|------|
| Phun Giao Diện Rực Rỡ | `visual_excellence` | skill | ecosystem/skills/visual_excellence/ |
| Nặn UI Đỉnh Cấp (PRO-MAX) | `ui-ux-pro-max` | plugin | plugins/ui-ux-pro-max/ |
| Vá Lỗi Tiêu Chuẩn Nền Trắng (A11y)| `accessibility_grounding`| skill | ecosystem/skills/accessibility_grounding/ |
| Thuật Cầu Khách Tới (SEO/AEO) | `seo-aeo-optimization`| skill | ecosystem/skills/seo-aeo-optimization/ |

### Thiết Quân Luật Cybersecurity (Bảo Mật, Lỗ Hổng Tiêm Nhiễm)
| Nhu Cầu | Công Cụ Gọi | Loại | Đường Dẫn Gốc |
|------|-----|------|------|
| Đóng Cổng GATE_SECURITY | `security_shield` | skill | ecosystem/skills/security_shield/ |
| Bẻ Cổ Repo Chưa Vetting | `skill_sentry` | skill | ecosystem/skills/skill_sentry/ |
| Vét Lật Mặt Kẽ Hở Rỉ (Leaks) | `zeroleaks` | plugin | plugins/zeroleaks/ |
| Chống Lún Lỗ Hổng Kênh Bơm (CVE)| `cybersecurity` | skill | ecosystem/skills/cybersecurity/ |
| Soi Chiếu Thẻ Thông Hành SSL | `cerberus-cve-tool`| plugin | plugins/cerberus-cve-tool/ |

### Trí Tuệ Quản Trị Hệ System Knowledge (KI, Bộ Nhớ Phân Mảnh)
| Nhu Cầu | Công Cụ Gọi | Loại | Đường Dẫn Gốc |
|------|-----|------|------|
| Thủy Thủ Dò Tri Thức | `knowledge_navigator` | skill | ecosystem/skills/knowledge_navigator/ |
| Bồi Đắp Dữ Liệu Tầng Ngầm | `knowledge_enricher`| skill | ecosystem/skills/knowledge_enricher/ |
| Nhớ Phiên Phù Du | `cosmic_memory` | skill | ecosystem/skills/cosmic_memory/ |
| Nhớ Hằn Sâu Sinh Tử | `smart_memory` | skill | ecosystem/skills/smart_memory/ |
| Nhớ Mạng Lưới Nhện Thần Kinh | `neural_memory` | skill | ecosystem/skills/neural_memory/ |
| Pháp Tắc Nén Cuộn Cố Tổ (Archivist)| `archivist` | skill | ecosystem/skills/archivist/ |
| Giữ Mạng Ngữ Cảnh Xuyên Phiên | `context_manager` | skill | ecosystem/skills/context_manager/ |

---

## 🔍 Cỗ Máy Tìm Kiếm Công Cụ — Cây Quyết Định Rễ Kép

```
TÔI CẦN CÔNG CỤ CHO: <tác_vụ_của_user>
    │
    ├─ Dính tới AI/RAG/Memory?      → Go gọi: LightRAG, knowledge_enricher, open-notebook
    ├─ Dính tới mổ xẻ code base?    → Go gọi: GitNexus (explore/impact/debug)
    ├─ Dính tới bảo mật cốt tủy?    → Go gọi: security_shield, zeroleaks, skill_sentry
    ├─ Dính tới Giao diện Tương tác?→ Go gọi: visual_excellence, ui-ux-pro-max
    ├─ Dính tới Bộ Nhớ Quá Khứ?     → Go gọi: cosmic_memory → smart_memory
    └─ Bị Hoang Mang Cục Bộ?        → Phi thẳng vào mồm LightRAG: aquery("<task>", mode="mix")
```

---
*Capability Map v1.0 | Cập Nhật 2026-03-22 | Bởi: registry-manager-agent*
