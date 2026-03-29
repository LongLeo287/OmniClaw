---
id: autonomous_git_merger
type: workflow
tags:
  - phase_sync
---

# 🐙 Đặc Vụ Bạch Tuột Git (Autonomous Git-Agent)

---
description: Tự động hóa quá trình sinh Nhánh Github, Resolve conflict và Đệ trình Pull Request. Dành riêng cho devops-agent.
---

Khi có lệnh đóng gói tính năng hoặc khi `frontend-agent` / `backend-architect` làm xong việc, tổ DevOps không chỉ đợi lệnh "Merge vào Main" thủ công. Bắt buộc Tuân Thủ Tự Động Hóa Môi Trường `open-gitagent`:

1. **Khởi Tạo Nhánh Biệt Phái (Feature Isolation):**
   Mở ngay nhánh `feature/task-name-xyz` khi AI bắt đầu gõ code, TUYỆT ĐỐI không gõ đè nhánh `main` / `master`! Sếp là người kiểm duyệt nhánh!

2. **Commit Nguyên Tử (Atomic Commits):**
   Bot tự chia nhỏ lần Save. 
   Sai: Bọc 10 file làm 1 commit "Update X".
   Đúng: Tự Push 3 Commit -> "Feat: Thêm Controller A", "Fix: Vá lỗi CSS nút B", "Chore: Dọn log C".

3. **Cơ Chế Khử Xung Đột (Conflict Resolver):**
   Nếu Repo gặp Conflict do sếp sửa tay, `devops-agent` phải nhảy vào phân tích tệp `<<<<<<< HEAD`. Nằm lòng quy tắc: Mã của LÃNH ĐẠO (Thường nằm ở Incoming) luôn là Thiên Tôn! Ký tự của Bot là Rác, đè Code Lãnh Đạo lên trên cùng. Hoặc báo cáo Sếp trước khi dọn Conflict.
