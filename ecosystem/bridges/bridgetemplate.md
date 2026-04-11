---
id: bridge_template
type: template
namespace: ecosystem.bridges.template
---

# 🌉 Bridge Construction Protocol

Tài liệu hướng dẫn quy chuẩn chế tạo "Cổng gác" (Bridge) cho hệ sinh thái OmniClaw. 

Bridges là tầng kiểm soát vòng ngoài, đại diện cho **OBD Harbor** để khởi động và quản lý các vệ tinh (Satellites/Skills/Servers) trong chế độ cô lập.

### 📜 Tiêu chuẩn bắt buộc của 1 Bridge:
1. **Lấy tham số từ mảng lệnh:** Port phải được nhận tự động thông qua `sys.argv[1]` do OBD Harbor truyền xuống.
2. **Kế thừa lệnh tắt:** Bridge phải chặn `KeyboardInterrupt` để dọn dẹp (cleanup) tiến trình con một cách an toàn. Tránh để lại Zombie Process.
3. **Cơ chế mô phỏng Port (Port Spoofing/Mocking):** Nếu ứng dụng mục tiêu chỉ chạy ngầm (như `system_pulse.py` hay desktop app) và không cắm một Socket nào, Bridge phải tự cắm một Socket ảo trên port được giao để hệ thống Ping Heartbeat của OBD Harbor có thể quét và ghi nhận trạng thái `ONLINE`.
4. **Không tùy tiện mở 0.0.0.0:** Nếu cấu hình lệnh, mặc định cờ `--host` hoặc bind ip phải là `127.0.0.1`. Chỉ thay đổi khi có lệnh tuyệt đối.

*Tham khảo `bridgetemplate.py` để sao chép bộ khung khởi tạo chuẩn.*
