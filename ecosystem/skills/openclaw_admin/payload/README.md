# 🦞 OpenClaw Admin Panel

Bảng Quản Trị giao diện Web (Web UI) hiện đại, chuyên nghiệp dành cho hệ thống **OpenClaw**. 
Phát triển bởi **Vũ Duy Mạnh** và cộng đồng **OpenClaw VN**.

![Preview](https://raw.githubusercontent.com/manhvicky/openclaw-admin/main/preview.png) *(Vui lòng cập nhật link ảnh thực tế nếu có)*

## ✨ Tính năng nổi bật
- **Tổng quan thời gian thực:** Xem trạng thái hoạt động của Gateway, Proxy, Model đang sử dụng.
- **Quản lý API Keys:** Thêm, xóa, xem hạn mức và chi tiết các Key nhà cung cấp (PikaAI, Claudible, OpenRouter...).
- **Lịch tự động (Cron Job):** Quản lý các task tự động, xem lịch sử chạy chi tiết cho từng task.
- **Nhật ký ngày (Daily Diary):** Theo dõi nhật ký hoạt động của AI theo từng ngày.
- **Phiên hội thoại:** Xem và quản lý các phiên chat, đọc lại lịch sử tin nhắn trong từng phiên.
- **Quản lý bộ nhớ (Memory):** Chỉnh sửa file ghi nhớ của OpenClaw trực tiếp trên web.
- **Skills & Profile:** Bật/tắt các kỹ năng và cấu hình hồ sơ AI dễ dàng.
- **🛑 Ngắt Khẩn Cấp:** Nút "cứu cánh" giúp dừng ngay lập tức trình duyệt và reset task khi AI đi sai hướng.
- **Hỗ trợ LAN/Wifi:** Truy cập bảng quản trị từ điện thoại hoặc thiết bị khác trong cùng mạng.

## 🚀 Hướng dẫn cài đặt & Chạy

### 1. Yêu cầu hệ thống
- Đã cài đặt [OpenClaw](https://github.com/openclaw/openclaw) thành công.
- Máy tính đã cài đặt Python 3.

### ⚡ Cách 1: Cài đặt SIÊU TỐC bằng chính OpenClaw (Khuyên dùng)
Nếu bạn đang sử dụng chính **OpenClaw (AI Agent)** để làm việc, bạn chỉ cần gửi link GitHub dự án này (`https://github.com/manhvicky/openclaw-admin`) và yêu cầu nó:
> *"Hãy clone và cài đặt OpenClaw Admin Panel từ repo này, sau đó khởi động server cho mình."*

OpenClaw sẽ tự động thực hiện mọi bước từ kéo code đến kích hoạt server cho bạn chỉ trong tích tắc!

### 🛠️ Cách 2: Cài đặt Thủ công
1. Tải toàn bộ source code này về máy (hoặc dùng lệnh `git clone`).
2. Mở Terminal (hoặc CMD) tại thư mục chứa code.
3. Chạy lệnh:
   ```bash
   python3 server.py
   ```
4. Mở trình duyệt và truy cập: `http://localhost:8765`

*Lưu ý: Bạn cũng có thể dùng file `start.sh` trên MacOS/Linux để khởi động nhanh.*

## 👥 Cộng đồng & Hỗ trợ
- **Tác giả:** [Vũ Duy Mạnh](https://www.facebook.com/vuduymanh.ken/)
- **Group thảo luận:** [Cộng Đồng OpenClaw VN](https://www.facebook.com/groups/852586990732832)

---
*Dự án này được tạo ra nhằm mục đích giúp cộng dùng OpenClaw VN có một giao diện quản lý thân thiện và hiệu quả hơn. Rất mong nhận được sự đóng góp từ mọi người!*
