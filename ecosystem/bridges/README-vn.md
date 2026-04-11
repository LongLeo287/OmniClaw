# 🌉 Kiến trúc Giao thông OmniClaw Bridges

**Bridges (Cổng Gác)** là rãnh tường lửa và trạm trung chuyển huyết mạch của Hệ điều hành AI OmniClaw (`v5.0`).

Toàn bộ các tệp tin trong thư mục này đóng vai trò là **Kịch bản Khởi động Cảng (Harbor Launch Script)**, và chúng bị kiểm soát độc quyền dưới trướng của **OBD Harbor** (OmniClaw Bridge Daemon). 
Khu vực này được dùng để ép buộc nguyên tắc "Cô lập": Đảm bảo không có ứng dụng hay AI Agents nền nào có quyền tự do mở kết nối thẳng vào OmniClaw nếu chưa nhận lệnh Ủy quyền Mở Cảng từ OBD Console.

---

## 🛑 Bốn Luật Thép Tiêu Chuẩn

1. **Tuyệt đối phục tùng OBD:** Bridges KHÔNG được thiết kế để user click đúp hay tự chạy thủ công. Chúng được sinh ra để OBD điều phối và bắn lệnh khởi động ngầm.
2. **Tuân thủ quy hoạch Port ngầm:** Không hardcode Port mạng sâu trong script. Nếu app yêu cầu số Port, hãy trích xuất nó từ vị trí `sys.argv[1]` (do OBD đọc từ file lõi `core/config/config.json` truyền sang).
3. **Chứng nhận Không Zombie:**
   - Script bắt buộc phải tạo "bắt tín hiệu" (intercept `KeyboardInterrupt` hoặc `SIGTERM`).
   - Khi Bridge sập hoặc bị ép đóng từ OBD, nó **phải dọn dẹp và tiêu diệt tàn dư** (terminate/kill) các ứng dụng nền do chính nó khởi tạo, tránh để tiến trình ma mút RAM.
4. **Cô lập Localhost:** Quy tắc sống còn — Nếu Bridge khởi động app web, luôn gán cờ `--host 127.0.0.1`. **Tuyệt đối cấm sử dụng `0.0.0.0`** trừ khi sếp chủ đích muốn biến máy mình thành Gateway cho toàn bộ thiết bị chung sóng Wifi hoặc thiết bị LAN gọi API vào.

---

## 🛠️ Quy trình Đúc 1 Bridge Mới

Nếu sếp muốn nạp một Node thần kinh mới (như LobeChat, Dify, hay một Server Python Agent), tiến hành theo quy trình:

1. **Đăng ký Khai sinh Mỏ neo:** Vào `core/config/config.json` để cấp cho module đó 1 danh phận và 1 số `port`. Mặc định để `"autostart": false`.
2. **Chế tạo Cầu:** Cố định tên định dạng `launch_<tên_module>.py`.
3. **Mượn Khuôn đúc OBD:**
   - Tham khảo code từ `bridgetemplate.py` và sao chép nó. Đừng gõ lại từ đầu.
4. **Luồn lệnh khởi chạy:** Nhét lệnh khởi động module của sếp vào khúc `subprocess.Popen(...)`. Bridge sẽ chịu trách nhiệm bọc nó lại thành tiến trình nền (Background Daemon).

### 🤫 Bí thuật "Tạo Dummy Port" (Chuyên trị ứng dụng câm)
Nếu module sếp tích hợp là một con Cảnh binh chạy ngầm (ví dụ: Bot Telegram, Vòng lặp giám sát file) mà nó **không hề tự mở một Socket Network nào** >> OBD Harbor sẽ chửi là Cảng Chết (OFFLINE) do Ping Heartbeat thất bại.
**Cách fix:** Trong file Bridge, hãy mượn thư viện `socket` nặn ra một vòng lặp Listen ảo trên đúng số cổng được giao. Cảng giả này không lưu lượng, nó chỉ ngồi đó hứng Ping của OBD Harbor để báo cáo `ONLINE` đầy đủ! (Xem ví dụ tại `launch_system_pulse.py` hoặc đọc mô tả tại `bridgetemplate.md`).

---
## Chính sách Runtime Mới (Bắt buộc)

- Bridge phải khởi chạy **service thật** hoặc fail fast. Cấm bind cổng giả chỉ để OBD thấy `ONLINE`.
- Bridge phải bám vào **tiến trình thật** bằng `subprocess.run(...)` hoặc một vòng giám sát tường minh. Không được `Popen(...)` rồi tự thoát.
- Cài dependency, bootstrap repo, sinh config mặc định chỉ được phép trong luồng `--repair` hoặc một lệnh provisioning riêng.
- Nếu service không tự mở port, OBD cần đọc health từ lifecycle/process signal thật thay vì dummy socket.

*Tài liệu Vận hành Trạm điều tiết OBD | OmniClaw V5.0*
