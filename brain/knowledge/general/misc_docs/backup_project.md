---
id: backup-project
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:56.390053
---

# Department: operations
---
description: Lưu chat history and brain data VÀO in folder dự án để chuyển máy
---

# Backup dự án this

Khi user has lệnh rõ ràng: "Backup dự án [tên dự án]" (chỉ dùng riêng for dự án, not dùng for hệ thống OmniClaw):

1. Xác định project path: 
   - Ưu tiên 1 LẤY TÊN DỰ ÁN from CÂU LỆNH CHAT of user (Vd: "Backup dự án Tiem_Nuoc_Nho_v5") and nối vào `$ProjectsRoot`.
   - Ưu tiên 2: Xác định from workspace đang mở.

// turbo
2. Chạy script:
```powershell
& "$OMNICLAW_ROOT\scripts\backup.ps1" -ProjectPath "ĐƯỜNG_DẪN_TỚI_TÊN_DỰ_ÁN_TRONG_CÂU_CHAT"
```

Script sẽ tạo folder `.ai-memory\` bên in project, chứa:
- `brain\` — toàn bộ chat session artifacts (task.md, walkthrough, plans...)
- `knowledge\` — knowledge items
- `memory_config.json` — metadata

3. Thông báo: "already lưu brain data vào [project]\.ai-memory\"

**Để chuyển máy:** chỉ cần copy toàn bộ project folder sang is xong — not cần làm gì thêm.

