# 🧩 OmniClaw Ecosystem Plugins

**Plugins (Công Cụ Mở Rộng)** đóng vai trò là não phụ và cánh tay nối dài bên thứ ba dành cho Hệ điều hành AI OmniClaw (`v5.0`).

Gõ nôm na: Nếu Core của OmniClaw là Hệ thống Tiêu hóa và Bộ não, thì thư mục này chính là Kho Chứa Đồ Nghề (Máy RAG, Server MCP, Database Vector, Máy cào dũ liệu Web) mua từ bên ngoài về để xài.

---

## 🛑 Luật Thép Sinh Thái Tiêu Chuẩn

1. **Kho Lạnh, Không Phải Sân Bay!**
   Các công cụ và đoạn mã để trong này chỉ được coi là thư viện tĩnh (Passive Storage). TUYỆT ĐỐI KHÔNG khởi chạy Server / Nghe Port trực tiếp từ thư mục này.
   👉 *Quy định của V5.0*: Nếu Plugin là một Web Server hoặc một ứng dụng chạy ngầm (ví dụ: `LightRAG`, `Mem0`, `Ollama`), nó **BẮT BUỘC** phải được lồng vào một "File mồi" nằm ở phân khu `ecosystem/bridges/` để chịu sự kiểm duyệt độc tài của Tường lửa OBD Harbor.
2. **Nguyên Tắc Zero-Trust:**
   Mọi Plugin đều bị coi là "Kẻ ngoại đạo". Nếu một plugin bị lỗi hoặc sập, nó bị cấm quyền đánh gục nhân Core OS. Code lỗi của Plugin phải tự thối rữa đơn lẻ.
3. **Tuân Thủ Đặc Tả:**
   Khi mang rác/tool từ Github về vứt vào đây, hãy mở `plugin_spec.md` ra xem quy cách đặt tên và tạo `manifest`.

---

## 🛠️ Cẩm nang Đọc Danh Bạ (Catalogs)

Thư mục này còn chứa Cuốn sổ Nam Tào ghi chép lịch sử lùng sục hàng ngàn công cụ AI của hệ thống:
* **`plugin_catalog.md`**: Danh bạ phân loại (Được duyệt / Chờ duyệt / Quẳng sọt rác) đối với các plugin cấp cao.
* **`master_repo_catalog.md`**: Sổ tay bưng nguyên hàng trăm repo từ Github về để ngâm cứu từ từ.

*Tài liệu Vận hành Thư Viện Plugin | OmniClaw V5.0*
