# 🏛️ Các Nguyên Tắc Kiến Trúc Lõi Của OmniClaw

OmniClaw không chỉ là một mớ script trộn lại với nhau; nó là một Hệ Điều Hành Nguyên Khối (Monolithic OS) được đặc chế tỉ mỉ nhằm tự duy trì, tiêu hóa dữ liệu và thực thi tác vụ qua hàng chục đặc vụ (Agents). Để duy trì độ phức tạp khổng lồ này, hệ thống áp đặt những nguyên tắc kiến trúc cực kỳ nghiêm ngặt.

---

## Nguyên Tắc 1: Khung Xương Nhận Thức Tích Hợp (Bộ Nhớ Zero-Config)

Thiếu sót kinh niên của đa số RAG Framework và ứng dụng AI nội bộ là rào cản khởi tạo. Bạn thường phải chạy hàng loạt `setup.sh` lằng nhằng để tạo các Folder Cache, Database ảo và Cây bộ nhớ (Memory Tree) trước khi Agent đầu tiên có thể tỉnh dậy.

**OmniClaw loại bỏ 100% bước rườm rà đó.**

### Cách Chúng Tôi Làm: Kỹ Thuật Bơm `.gitkeep`
Nền tảng Git tự động bỏ qua (Ignore) các thư mục trống. Do đó, toàn bộ cấu trúc não bộ rỗng thường bị biến mất khi người dùng Clone Repo về. Tại OmniClaw, chúng tôi đã "Bơm" **hàng trăm tệp tin dò đường `.gitkeep`** vào tận sâu mao mạch của khu vực `brain/`.

### Ý Nghĩa Sống Còn:
1. **Zero-Configuration:** Khi bạn Clone OmniClaw, bạn ngay lập tức kế thừa một **Cấu trúc 300+ Thư mục** đã được khởi tạo sẵn sàng.
2. **Phân Bổ Bộ Nhớ Tức Thì:** Các Agents của hệ thống chỉ tìm kiếm dữ liệu ở các ngách sâu (VD: `brain/memory/.ai-memory/active_session/` hay `brain/agents/strix_agent/`). Nhờ bộ khung xương `.gitkeep`, bọn chúng sẽ không bao giờ bị Crash vì lỗi "Không tìm thấy thư mục".
3. **Chiến Đấu Từ Ngày Đầu Tiên (Day-1):** Hệ thống RAG và không gian lưu trữ cá nhân đã sẵn sàng băm nhỏ, tiêu hóa và sắp xếp dữ liệu ngay giây phút Repo đáp xuống ổ cứng của bạn.

---

## Nguyên Tắc 2: Chính Sách Ngôn Ngữ Nguyên Bản Cấu Trúc (OS-Agnostic)

Một hệ điều hành AI cấp độ Tập đoàn phải vận hành mượt mà bất kể nền tảng và hỗ trợ được đủ loại Modle Toàn Cầu (OpenAI của Mỹ, Mistral của Châu Âu, hay DeepSeek/Qwen của Trung Quốc). Để ngăn chặn các cuộc đụng độ Tokenization chí mạng, OmniClaw ép một bộ luật ngôn ngữ tàn khốc xuống vùng Lõi.

### Luật Thép: Thuần Tiếng Anh Kỹ Thuật (Technical English Only)
Mọi file mã nguồn, Lệnh Prompt của Agent, Tri thức (Knowledge Items `KI-*`), thuật toán Workflow và bản đồ cấu trúc trong `brain/knowledge` **Bắt Buộc** phải viết bằng Tiếng Anh.

### Ý Nghĩa Sống Còn:
1. **Tối Ưu Token Tối Đa:** Các ký tự ngoài bảng mã Latinh (Tiếng Việt, Trung, Ả Rập) đốt một lượng token khổng lồ trong LLM. Bằng cách khóa chặt lõi Prompt Hệ thống sang tiếng Anh, chúng tôi cắt giảm triệt để chi phí Token và tăng tốc độ xử lý.
2. **Chống Crash Encoding:** Việc RAG và nhồi nhét file UTF-8 đa byte quá dày đặc thường xuyên gây vỡ mã khi đẩy vào Vector Database. Tiếng Anh đóng vai trò là Lồng Kính An Toàn tuyệt đối.
3. **Hỗ Trợ RAG Hoàn Hảo:** Các thuật toán cào dữ liệu đồ thị đồ sộ (Như `LightRAG`) chạy mượt mà và bóc tách thực thể (Entity Extraction) chính xác gấp nhiều lần khi duyệt một bản đồ thuần tiếng Anh.

### Dành Cho Người Dùng Bản Địa (`-vn.md`)
Dù Lõi "Máy Đọc" (Machine-Readable) bắt buộc là Tiếng Anh, chúng tôi Tôn trọng sự Tiện lợi của Người dùng. OmniClaw quy định sử dụng đuôi tệp `*-vn.md` cho các tài liệu Giao Diện Người Dùng (VD: `README-vn.md` hay `MASTER_SYSTEM_MAP-vn.md`). Qua đó, Các Lập trình viên người Việt có thể đọc trơn tru kiến trúc, trong khi tụi Agents và RAG Database chỉ việc húp trọn vùng lõi Tiếng Anh!

---

*Các Nguyên Tắc Lõi Của OmniClaw v1.0 | Cập nhật: 2026-04-01*
