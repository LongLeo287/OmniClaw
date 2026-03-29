---
description: How Dept 25 Orchestrates a complex Swarm Prompt
---
# Workflow Đẳng Cấp: Orchestration & Routing (Dept 25)

## Giai đoạn 1: Mổ Tẻ Prompt (Parse & Abstract)
- `orchestrator-prime` nhận lệnh. Trích xuất Mục tiêu cuối cùng (Final Product).
- Quét **Dependencies** để chia lệnh thành `Cây Phân Giã Công Việc (Work Breakdown Structure)`.

## Giai đoạn 2: Định Tuyến Nhạy Bén (ClawRouting)
- `router-agent` đọc bảng liệt kê `org_chart.yaml`.
- So khớp Skills của 21 phòng ban còn lại với Mảnh ghép của Cây công việc:
  - Nếu Design DB -> Chọn `database-agent` (Dept 03).
  - Nếu Design React UI -> Chọn `frontend-agent` (Dept 01).
  - Nếu cần kiểm duyệt SEO -> Gửi `content_review` (Dept 06).
- **Trigger**: Gán Assignee và ném lệnh sang `blackboard.json` hoặc Daily Briefs.

## Giai đoạn 3: Swarm Execution (Xử lý đồng loạt)
- Đóng cọc những Node yêu cầu tuần tự ("Xong A mới gọi B").
- Gọi MỌI Node khác hoạt động Song Song.

## Giai đoạn 4: Thu Nạp & Đúc Kết (Reduce)
- `swarm-coordinator` túc trực và hứng Data.
- Ngay khi 1 Cọc Đóng xong, cập nhật State Machine. Đẩy sang Node tiếp theo.
- Khi toàn bộ State Code trả về 200 (Thành công 100%), trộn toàn bộ Outputs thành một Markdown Artifact `walkthrough.md`.

## Giai đoạn 5: Hand-off (Bàn giao lại Tier 1)
- Truyền lệnh "Orchestration Complete" -> Đánh dấu `status: done` trên HUD.md. Hết.
