---
description: Handoff Execution to Claude Code CLI (OmniClaw)
---

# Workflow: Handoff to OmniClaw Coder
Sử dụng workflow này khi Antigravity (hoặc Agent hiện hành) cần nhượng quyền thực thi lệnh (Handoff) sang cho hệ thống OmniClaw (cụ thể là Claude Code CLI) để tiết kiệm Quota hoặc tận dụng mạng lưới `omniclaw-coder` mạnh hơn.

## Điều kiện kích hoạt:
1. Khi có yêu cầu tạo/sửa đổi số lượng code lớn.
2. Khi Quota của Antigravity (Gemini) sắp cạn kiệt.
3. Khi Người dùng (CEO) ra chỉ thị trực tiếp: "Đưa lệnh đó về OmniClaw để thực hiện" hoặc "Handoff sang Claude Code".

## Các bước thực hiện:

1. **Chuẩn bị prompt cho Claude Code CLI:**
   - Đọc yêu cầu hoặc Plan đã thống nhất với user.
   - Gói gọn yêu cầu thành một câu lệnh duy nhất (One-shot Prompt). VD: "Implement the login form using React and Tailwind based on the PRD in docs/".

2. **Thực thi gọi Claude Code (Handoff):**
// turbo
1. Sử dụng công cụ `run_command` để mở Terminal.
2. Gõ lệnh gọi `claude` CLI, truyền kèm tham số `-p` (prompt) nội dung công việc.
3. Đảm bảo cấu hình mặc định của `claude` trong IDE của User đã được trỏ về `http://127.0.0.1:8080/v1` và Tên Model `omniclaw-coder`. (Điều này đã được setup thủ công bởi User).

```bash
# Lệnh mẫu thực thi chuyển giao:
claude -p "Dựa vào kế hoạch trong file PLAN.md, hãy tạo ra các component React tương ứng. Sử dụng styling TailwindCSS chuẩn."
```

3. **Giám sát và nghiệm thu:**
   - Chờ hệ thống Claude Code (chạy ngầm qua OmniClaw Router) thực hiện xong trên Terminal.
   - Báo cáo lại cho Người Dùng (CEO) kết quả hoàn thành.

## Ghi chú An Ninh:
- Antigravity **TUYỆT ĐỐI** KHÔNG dùng API trực tiếp chọc vào Cổng 8080 để tránh bị hệ thống Google giám sát/ban tài khoản ngầm. Mọi giao tiếp với mô hình Local phải đi qua lớp trung gian là Terminal (CLI).
