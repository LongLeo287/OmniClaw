---
id: backup-project
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:56.390053
---

# Department: operations
---
description: Lưu chat history và brain data VÀO trong folder dự án để chuyển máy
---

# Backup dự án này

Khi user có lệnh rõ ràng: "Backup dự án [tên dự án]" (chỉ dùng riêng cho dự án, không dùng cho hệ thống OmniClaw):

1. Xác định project path: 
   - Ưu tiên 1 LẤY TÊN DỰ ÁN TỪ CÂU LỆNH CHAT của user (Vd: "Backup dự án Tiem_Nuoc_Nho_v5") và nối vào `$ProjectsRoot`.
   - Ưu tiên 2: Xác định từ workspace đang mở.

// turbo
2. Chạy script:
```powershell
& "$OMNICLAW_ROOT\scripts\backup.ps1" -ProjectPath "ĐƯỜNG_DẪN_TỚI_TÊN_DỰ_ÁN_TRONG_CÂU_CHAT"
```

Script sẽ tạo folder `.ai-memory\` bên trong project, chứa:
- `brain\` — toàn bộ chat session artifacts (task.md, walkthrough, plans...)
- `knowledge\` — knowledge items
- `memory_config.json` — metadata

3. Thông báo: "Đã lưu brain data vào [project]\.ai-memory\"

**Để chuyển máy:** chỉ cần copy toàn bộ project folder sang là xong — không cần làm gì thêm.

