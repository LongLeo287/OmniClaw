---
id: CAPABILITY-MAP-001-vn
type: REFERENCE
domain: [system, skills, plugins, discovery]
dept: all
lang: vi
created: 2026-03-22
version: 1.0
authority: registry_capability
---

# OmniClaw Corp — Bản Đồ Năng Lực
## Chỉ Mục Khám Phá Skill / Plugin (Đọc được bởi Con Người + Agent)

> **Mục Đích:** `knowledge_navigator` đọc file này trong Giai Đoạn 3 để tìm skill/plugin đúng cho mỗi domain tag thay vì đoán từ khóa.
> Độ chính xác cải thiện từ ~65% → ~90% khi dùng CAPABILITY_MAP + LightRAG.

[**🇬🇧 View in English**](SKILLS_MAP.md) | [**Quay về Mục Lục Docs**](../README-vn.md)

---

## Lộ Trình Nâng Cấp

```
HIỆN TẠI (Giai Đoạn 1): knowledge_navigator đọc CAPABILITY_MAP.md → 90% chính xác
TIẾP THEO (Giai Đoạn 2): LightRAG graph index tất cả SKILL.md + manifest.json → 95%+
                          Chạy: python ops/scripts/index_skills_lightrag.py
TƯƠNG LAI (Giai Đoạn 3): Phân tích tác động GitNexus → bán kính phá hoại chính xác
                           Chạy: npx gitnexus analyze (trong OmniClaw root)
```

---

## Domain → Bản Đồ Skill/Plugin

### ai_ml (AI/ML, LLM, RAG, Embeddings)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Tìm kiếm tri thức / RAG | `knowledge_enricher` | skill | ecosystem/skills/knowledge_enricher/ |
| Graph-based RAG | `LightRAG` | plugin | plugins/LightRAG/ |
| Tiếp nhận tài liệu | `open-notebook` | plugin | plugins/open-notebook/ |
| Tổng hợp nghiên cứu | `notebooklm-skill` | plugin | plugins/notebooklm-skill/ |
| Tổng hợp đa nguồn | `multi-source-aggregation` | skill | ecosystem/skills/multi-source-aggregation/ |
| Lý luận + quyết định | `reasoning_engine` | skill | ecosystem/skills/reasoning_engine/ |
| Mẫu nhận thức | `cognitive_reflector` | skill | ecosystem/skills/cognitive_reflector/ |
| Định tuyến LLM | `llm_router` | skill | ecosystem/skills/llm_router/ |
| NLP + trích xuất dữ liệu | `langextract` | plugin | plugins/langextract/ |

### backend (Python, API, FastAPI, Node.js)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Shell + scripts | `shell_assistant` | skill | ecosystem/skills/shell_assistant/ |
| QA production | `production_qa` | skill | ecosystem/skills/production_qa/ |
| Lint kiến trúc | `fsd_architectural_linter` | skill | ecosystem/skills/domains/frontend/ |
| Resilience + retry | `resilience_engine` | skill | ecosystem/skills/resilience_engine/ |
| Profiling hiệu năng | `performance_profiler` | skill | ecosystem/skills/performance_profiler/ |
| Chẩn đoán | `diagnostics_engine` | skill | ecosystem/skills/diagnostics_engine/ |

### web_frontend (React, Vue, HTML, CSS, UI)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Tạo UI/UX | `visual_excellence` | skill | ecosystem/skills/visual_excellence/ |
| Tạo UI PRO | `ui-ux-pro-max` | plugin | plugins/ui-ux-pro-max/ |
| Accessibility | `accessibility_grounding` | skill | ecosystem/skills/accessibility_grounding/ |
| SEO/AEO | `seo-aeo-optimization` | skill | ecosystem/skills/seo-aeo-optimization/ |

### devops (Docker, CI/CD, k8s, hạ tầng)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Shell + deployment | `shell_assistant` | skill | ecosystem/skills/shell_assistant/ |
| Resilience | `resilience_engine` | skill | ecosystem/skills/resilience_engine/ |
| Chẩn đoán | `diagnostics_engine` | skill | ecosystem/skills/diagnostics_engine/ |
| Deploy Cloudflare | `cloudflare-skills` | plugin | plugins/cloudflare-skills/ |
| Deploy Vercel | `vercel-agent-skills` | plugin | plugins/vercel-agent-skills/ |

### cybersecurity (CVE, pentest, OWASP, secrets)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Quét GATE_SECURITY | `security_shield` | skill | ecosystem/skills/security_shield/ |
| Kiểm duyệt repo | `skill_sentry` | skill | ecosystem/skills/skill_sentry/ |
| Phát hiện rò rỉ | `zeroleaks` | plugin | plugins/zeroleaks/ |
| Theo dõi CVE | `cybersecurity` | skill | ecosystem/skills/cybersecurity/ |
| Quét Cert | `cerberus-cve-tool` | plugin | plugins/cerberus-cve-tool/ |

### marketing (SEO, content, social, campaigns)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Web intelligence | `web_intelligence` | skill | ecosystem/skills/web_intelligence/ |
| SEO/AEO | `seo-aeo-optimization` | skill | ecosystem/skills/seo-aeo-optimization/ |
| Quản lý kênh | `channel_manager` | skill | ecosystem/skills/channel_manager/ |
| Thông báo | `notification_bridge` | skill | ecosystem/skills/notification_bridge/ |

### legal (GDPR, hợp đồng, IP, tuân thủ)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Lý luận pháp lý | `reasoning_engine` | skill | ecosystem/skills/reasoning_engine/ |
| Làm giàu tri thức | `knowledge_enricher` | skill | ecosystem/skills/knowledge_enricher/ |
| Nghiên cứu Web | `web_intelligence` | skill | ecosystem/skills/web_intelligence/ |

### finance (ngân sách, chi phí, hóa đơn, API cost)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Theo dõi chi phí | `cost_manager_skill` | skill | ecosystem/skills/domains/finance/ |
| Số liệu hiệu năng | `performance_profiler` | skill | ecosystem/skills/performance_profiler/ |
| Phân tích dữ liệu | `insight_engine` | skill | ecosystem/skills/insight_engine/ |

### knowledge_mgmt (KI, memory, index, graph)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Điều hướng tri thức | `knowledge_navigator` | skill | ecosystem/skills/knowledge_navigator/ |
| Làm giàu tri thức | `knowledge_enricher` | skill | ecosystem/skills/knowledge_enricher/ |
| Bộ nhớ (phiên) | `cosmic_memory` | skill | ecosystem/skills/cosmic_memory/ |
| Bộ nhớ (dài hạn) | `smart_memory` | skill | ecosystem/skills/smart_memory/ |
| Bộ nhớ (thần kinh) | `neural_memory` | skill | ecosystem/skills/neural_memory/ |
| Lưu trữ | `archivist` | skill | ecosystem/skills/archivist/ |
| Graph RAG | `LightRAG` | plugin | plugins/LightRAG/ |
| Quản lý context | `context_manager` | skill | ecosystem/skills/context_manager/ |

### registry (vòng đời skill, plugin, agent)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Tạo skill | `skill_generator` | skill | ecosystem/skills/skill_generator/ |
| Sentry skill | `skill_sentry` | skill | ecosystem/skills/skill_sentry/ |
| Tạo agent | `orchestrator_pro` | skill | ecosystem/skills/orchestrator_pro/ |
| Công cụ đề xuất | `proposal_engine` | skill | ecosystem/skills/proposal_engine/ |

### codebase_navigation (hiểu code, refactoring, debug)
| Nhu Cầu | Dùng | Loại | Đường Dẫn |
|------|-----|------|------|
| Khám phá code | `gitnexus-exploring` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Phân tích tác động | `gitnexus-impact-analysis` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Truy vết bug | `gitnexus-debugging` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Refactoring | `gitnexus-refactoring` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Review PR | `gitnexus-pr-review` | skill | tools/gitnexus-web/gitnexus/skills/ |
| Truy vấn Cypher graph | `gitnexus-cli` | skill | tools/gitnexus-web/gitnexus/skills/ |

---

## Tra Cứu Nhanh: Theo Năng Lực

| Năng Lực | Công Cụ Tốt Nhất | Độ Chính Xác |
|-----------|-----------|---------| 
| Tìm kiếm ngữ nghĩa trên tài liệu | `LightRAG` (mix mode) | 95%+ |
| Đồ thị quan hệ code | `GitNexus` (cypher) | 95%+ |
| Phân tích tác động plugin | `GitNexus` (impact tool) | 90%+ |
| Bộ nhớ qua phiên | `cosmic_memory` / `smart_memory` | 85%+ |
| Web scraping | `web_intelligence` / `langextract` | 85%+ |
| Quét bảo mật (repo) | `security_shield` / `zeroleaks` | 95%+ |
| Tạo UI | `visual_excellence` / `ui-ux-pro-max` | 90%+ |
| Tiếp nhận tri thức | `knowledge_enricher` + `open-notebook` | 90%+ |
| Điều phối agent | `orchestrator_pro` / `corp_orchestrator` | 90%+ |
| Thông báo đến CEO | `notification_bridge` | 99%+ |

---

## Tìm Công Cụ — Cây Quyết Định

```
CẦN CÔNG CỤ CHO: <tác vụ>
    │
    ├─ Về AI/RAG/Memory?        → LightRAG, knowledge_enricher, open-notebook
    ├─ Về code/repo?            → GitNexus (explore/impact/debug/refactor)
    ├─ Về bảo mật?              → security_shield, zeroleaks, skill_sentry
    ├─ Về UI?                   → visual_excellence, ui-ux-pro-max
    ├─ Về deployment?           → shell_assistant, cloudflare-skills, vercel-agent-skills
    ├─ Về trích xuất dữ liệu?   → langextract, web_intelligence, knowledge_enricher
    ├─ Về bộ nhớ?               → cosmic_memory → smart_memory → LightRAG
    └─ Không chắc?              → query LightRAG: aquery("<tác vụ>", mode="mix")
                                 HOẶC kiểm tra knowledge_index.md
```

---

*Bản Đồ Năng Lực v1.0 | 2026-03-22 | Cập nhật bởi: registry-manager-agent*
*Kiểm tra chéo với: SKILL_REGISTRY.json, plugins/registry.json, knowledge_index.md*
