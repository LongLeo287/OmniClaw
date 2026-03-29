---
name: code_interpreter
description: Kỹ năng Viết và Chạy lệnh ảo tự động.
---

# Code Interpreter Skill
**Nguồn Gốc:** Trích xuất từ kho chứa Awesome-Agent-Skills.

## Mô tả (Description)
Thay vì code xong vứt đó cho Sếp chạy, Agent tự quyền sinh ra một Môi trường cát (Sandbox / Docker / venv) để tự chạy thử nghiệm Script Python hoặc Javascript mình vừa tạo.

## Hướng dẫn sử dụng (Usage)
- Chèn trực tiếp Tool `execute_code`.
- Agent gọi `execute_code("python", "print('hello from sandbox')")` và nhận `Output` hoặc `Error` traceback.

## Cảnh Báo An Ninh (Strix Rules)
1. **Cô Lập:** Bất cứ mã nào chạy qua Kỹ năng này không được phép sửa đổi Local Filesystem cấp độ OS (như `.rclone`, `.gemini`). Cấm phá hoại.
2. **Không kết nối External DB:** Trừ khi là test DB (SQLite In-Memory).
