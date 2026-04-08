---
id: wakeup-project
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:32:45.396157
---

# Department: operations
---
description: Lấy brain data từ .ai-memory/ trong project ra restore vào session mới
---

# Wakeup dự án

Khi user có lệnh rõ ràng: "Wakeup dự án [tên dự án]" (lệnh gọi độc lập chỉ dành cho dự án, Note: rằng phần lớn thời gian hệ thống sẽ tự Wakeup khi khởi động bằng `pre-session`):

1. Xác nhận: "Tôi sẽ restore brain data từ .ai-memory\ trong project. Xác nhận chưa?"

1. Xác nhận: "Tôi sẽ restore brain data từ .ai-memory\ trong project [Tên]. Xác nhận chưa?"

2. Nếu user không cung cấp đường dẫn dự án cụ thể, hãy TÌM LẠI tên dự án trong CÂU LỆNH CHAT của user (Example: "Wakeup dự án Tiem_Nuoc_Nho_v5") để tự suy luận và nối vào `$ProjectsRoot`.

// turbo
3. Chạy script:
```powershell
& "$OMNICLAW_ROOT\scripts\wakeup.ps1" -ProjectPath "ĐƯỜNG_DẪN_TỚI_TÊN_DỰ_ÁN_TRONG_CÂU_CHAT"
```

Script sẽ:
- Đọc `.ai-memory\` từ bên trong project
- Restore brain sessions về `~\.gemini\antigravity\brain\`
- Restore knowledge items
- Auto-seed session hiện tại với key artifacts (task.md, walkthrough...)
- Hỏi user nếu không tự detect được session ID

4. Thông báo: "✅ Đã restore xong — tiếp tục làm việc bình thường!"

