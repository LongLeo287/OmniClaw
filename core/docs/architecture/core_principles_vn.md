---
id: core-principles-vn
type: document
owner: SYSTEM
lang: vi
---

# 🏛️ Các Nguyên Tắc Kiến Trúc Cốt Lõi của OmniClaw

OmniClaw không chỉ là một tập hợp các script; đây là một Hệ Điều Hành Vận Hành (Operational System) được thiết kế tỉ mỉ, dạng nguyên khối (monolithic), với khả năng tự điều tiết, tiếp nhận dữ liệu và thực thi tác vụ qua khung đa tác nhân. Để duy trì sự phức tạp khổng lồ này ở quy mô lớn, hệ thống thực thi nghiêm ngặt một số nguyên tắc kiến trúc cơ bản.

[**🇬🇧 View in English**](CORE_PRINCIPLES.md) | [**Quay về Mục Lục Docs**](../README-vn.md)

---

## Nguyên Tắc 1: Bộ Khung Nhận Thức Tiền Xây Dựng (Zero-Config Memory)

Một thách thức tiêu chuẩn trong các ứng dụng LLM cục bộ và khung RAG là rào cản khởi tạo. Hầu hết các hệ thống yêu cầu bạn chạy các script thiết lập phức tạp để tạo cơ sở dữ liệu, thư mục cache và cây bộ nhớ cần thiết trước khi agent đầu tiên có thể khởi động.

**OmniClaw loại bỏ hoàn toàn điều này.**

### Cách Chúng Tôi Giải Quyết: Kỹ thuật `.gitkeep` injection
Vì Git vốn bỏ qua các thư mục rỗng, các cấu trúc nhận thức khổng lồ thường bị mất khi người dùng clone một repository. Trong OmniClaw, chúng tôi đã tiêm có hệ thống **hàng trăm file `.gitkeep` tracer chuyên biệt** sâu vào thư mục `brain/` của hệ thống.

### Tại Sao Điều Này Quan Trọng:
1. **Zero-Configuration:** Khi clone OmniClaw, bạn ngay lập tức kế thừa một **cấu trúc 300+ thư mục** đã được khởi tạo đầy đủ.
2. **Phân Bổ Bộ Nhớ Tức Thì:** Các agent của chúng tôi tìm kiếm các đường dẫn lồng nhau cụ thể (vd: `brain/memory/.ai-memory/active_session/conversations/`). Vì khung xương được theo dõi trước qua `.gitkeep`, các agent sẽ không bao giờ crash do lỗi "Directory Not Found".
3. **Sẵn Sàng Ngay Ngày Đầu:** Bộ nhớ RAG cục bộ và cơ sở tri thức đa tác nhân của bạn sẵn sàng tiêu hóa, phân loại và phân vùng dữ liệu ngay giây đầu tiên repository chạm đến ổ cứng nội bộ.

---

## Nguyên Tắc 2: Chính Sách Ngôn Ngữ Toàn Cầu Không Phụ Thuộc OS

Một Hệ Điều Hành Đa Tác Nhân phải mở rộng toàn cầu và hỗ trợ lượng lớn mô hình nền khác nhau (OpenAI từ Mỹ, Mistral từ EU, DeepSeek/Qwen từ Trung Quốc). Để ngăn xung đột tokenization chết người, OmniClaw thực thi chính sách ngôn ngữ nghiêm ngặt trong phần lõi.

### Quy Tắc: Chỉ Tiếng Anh Kỹ Thuật
Tất cả file hệ thống lõi, Agent Prompt, Knowledge Item (`KI-*.md`), thuật toán Workflow và bản đồ kiến trúc `brain/knowledge` **phải** được viết bằng tiếng Anh kỹ thuật chuẩn.

### Tại Sao Điều Này Quan Trọng:
1. **Tối Ưu Hóa Tokenization:** Ký tự không Latin (như tiếng Việt hay tiếng Trung) tiêu thụ nhiều token hơn đáng kể trong kiến trúc LLM. Bằng cách buộc các prompt backend khổng lồ của hệ thống vào tiếng Anh, chúng tôi giảm đáng kể chi phí token và vận hành.
2. **Ngăn Crash Encoding:** Thực thi mô hình đa nền tảng thường có thể thất bại khi phân tích cú pháp cấu trúc UTF-8 đa byte phức tạp. Tiếng Anh đóng vai trò ràng buộc nơi trú ẩn an toàn tối thượng.
3. **Truy Xuất RAG Hoàn Hảo:** Thuật toán tìm kiếm ngữ nghĩa (như `LightRAG`) hoạt động tốt hơn theo cấp số nhân trong việc trích xuất thực thể khi đánh giá đồ thị tiếng Anh thống nhất.

### Bản Địa Hóa Cho Con Người (`-vn.md`)
Trong khi "backend Đọc-bởi-Máy" hoàn toàn bằng tiếng Anh, chúng tôi hoàn toàn hỗ trợ bản địa hóa cho con người. OmniClaw sử dụng hậu tố file `*-vn.md` rõ ràng cho tài liệu hướng đến con người (như `README-vn.md`). Điều này đảm bảo con người có thể đọc kiến trúc thoải mái bằng ngôn ngữ mẹ đẻ, trong khi các Agent và hệ thống RAG tiếp tục dùng độc quyền phần lõi tiếng Anh.

---

*OmniClaw Core Principles v1.0 | Cập nhật: 2026-04-01*
