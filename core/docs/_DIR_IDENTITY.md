---
id: core-docs
name: OmniClaw Documentation
path: core/docs
type: directory_identity
owner: OMA
tier: public
language: [en, vn]
---

# core/docs — OmniClaw Documentation Hub
# core/docs — Trung Tâm Tài Liệu OmniClaw

**Front door for all human-readable documentation.**
**Cánh cổng chính cho kho tài liệu dành cho con người.**
Every file in this directory comes in 2 versions:
Mọi tệp trong thư mục này đều tồn tại dưới 2 phiên bản:
- `<filename>.md` — English (primary) / Tiếng Anh (Bản gốc)
- `<filename>-vn.md` — Tiếng Việt (Bản dịch)

## Structure (Cấu trúc)
```
core/docs/
├── README.md              ← Entry point (EN) / Trạm trung chuyển (EN)
├── README-vn.md           ← Entry point (VN) / Trạm trung chuyển (VN)
├── architecture/          ← System architecture docs / Tài liệu Kiến trúc Hệ thống
├── usage_guides/          ← How-to guides / Hướng dẫn Vận hành
└── workflows/             ← Operational SOPs / Quy trình Hoạt động (SOPs)
```

## Rules (Luật)
- ✅ Human-readable `.md` docs only / Chỉ chứa tài liệu `.md` con người đọc được.
- ✅ Every doc MUST have both EN + VN version / Mọi tài liệu BẮT BUỘC phải có bản gốc EN và bản dịch VN.
- ❌ No scripts, no `.py`, no `.json` data files / Nghiêm cấm mã lệnh, tệp `.py`, tệp dữ liệu `.json`.
- ❌ No subdirectory that mirrors a root OmniClaw path / Nghiêm cấm đặt tên thư mục trùng với thư mục gốc của OmniClaw.
