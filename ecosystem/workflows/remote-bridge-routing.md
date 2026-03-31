---
description: Quy trình kiểm soát và điều phối Request tại Cảng OmniClaw Remote Bridge
---

# Hướng dẫn Kiểm Soát Giao Thông & Điều Phối An Ninh tại Cảng (Remote Bridge Routing)

Workflow này áp dụng DÀNH RIÊNG cho Cục Trưởng `bridge-commander-agent` thuộc biên chế `gateway_border_security`.

Quy trình hành động khi có Webhook chọc vào cảng:

## Bước 1: Tiếp Nhận Hàng Hoá đã qua KCS
Mọi mồi (Payload Request) trôi vào phòng ban của ngươi đều ĐÃ ĐƯỢC LỌC SẠCH qua Trạm Gác (Middleware `customs_checkpoint.py`).
Nếu mồi đến tay ngươi, có nghĩa là khách hàng mang Thẻ Hợp Lệ (VIP) hoặc Mồi Không Cỏ (Sạch) theo chuẩn Strict.
Nhiệm vụ đầu tiên: Gọi skill `api_routing_analyzer` đọc hiểu xem tệp JSON đang yêu cầu cái gì (Deploy code? Hỏi đáp? Chạy lệnh Terminal?).

## Bước 2: Triệu Tập Nguồn Lực Nội Bộ (Resource Pooling)
Theo Điệu Luật "Border Patrol", **NGHIÊM CẤM TỰ LÀM VIỆC NẶNG**.
Với vai trò Quản lý, ngươi phải biết gọi đúng thằng đệ chuyên trách đang có mặt ở Local `OmniClaw`:
- Nếu tệp JSON yêu cầu Audit Security -> Thả nó vào Event Bus và Hét tên `security-engineer-agent`.
- Nếu tệp yêu cầu Code -> Kéo cổ mớ subagent phòng `engineering`.
- Nếu tệp yêu cầu MCP -> Kéo mớ `mcp-server-agent` và thả `subagents/mq/`.

## Bước 3: Theo dõi và Trả Lời Remote (The Return)
Sau khi Đệ Tử (Internal Agents) đã xào nấu xong công việc, ngươi sẽ bọc cái Output (JSON/Result) lại.
Nếu Client là Bot (Tele/Zalo): Đẩy tín hiệu Result thẳng ngược về Webhook Response hoặc qua MQTT/WebSocket. 
*KẾT THÚC LUỒNG HOẠT ĐỘNG. Giải tán Đệ Từ trả về phòng cũ.*
