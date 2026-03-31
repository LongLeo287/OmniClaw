<!-- DEPRECATED — This workflow has been superseded by the current OmniClaw ecosystem.
     Kept for historical reference only. DO NOT USE in active flows.
     See ecosystem/workflows/ for current versions.
-->

---
description: Tiêu chuẩn thu thập và Truy vết Log LLM API
---
# Workflow Nhãn Giới Diều Hâu: Telemetry Tracing (Dept 14/23)

## Triết lý (The Philosophy)
Dựa trên kiến trúc `OpenTelemetry`, hệ thống OmniClaw KHÔNG THỂ cứ mập mờ "đang chạy" mà Sếp không biết nó tốn bao lâu, tiêu bao nhiêu Token, và chững lại ở Node nào. Mọi Request đều phải đội nón bảo hiểm mang tên `Trace_ID`.

## Giai đoạn 1: Bao bọc Yêu Cầu (Wrap the Call)
Khi 1 Agent (Đặc biệt là `sre-agent` hoặc `backend-architect`) gọi API nội bộ hoặc Web Search:
- Bắt buộc tạo mã ngẫu nhiên `Trace_ID = TX_<random_hex>`.
- Ghi log (Start Time): `<Timestamp> [Trace_ID] Bắt đầu gõ Web Request tới Google.`

## Giai đoạn 2: Đo Đạc Đỉnh Vị (Measure the Peak)
- Bất kể kết quả trả về là Lỗi (500) hay Thành Công (200), cũng phải đập thêm Log:
  `<Timestamp> [Trace_ID] Hoàn tất Call. Duration: 1205ms. Payload: 4Kb.`

## Giai đoạn 3: Hội tụ & Vẽ Biểu Đồ (Span Convergence)
- SRE Agent sẽ định kỳ quét file log (hoặc `.mcp.json`) để túm lại những `Trace_ID` có thời gian (Duration) > 10,000ms.
- Phân loại chúng thành `Bottleneck` (Nút thắt cổ chai).
- Tự động báo cáo trên `HUD.md` (BẢNG ĐIỀU KHIỂN) cho Sếp biết: "Dept 01 gọi DB đang chậm hơn bình thường 200%".
