# 🏛️ Tổng Quan Hệ Thống (Kiến trúc 21 Phòng Ban)

Tập đoàn OmniClaw Corp mô phỏng chính xác cấu trúc của một siêu công ty kỹ thuật số, sở hữu **21 "Phòng ban" tách biệt** được vận hành bởi các Đặc vụ Trí tuệ (AI Agents) dưới cơ chế đa luồng phức tạp.

[**🇬🇧 Read in English**](system_overview.md) | [**Quay lại Mục Lục**](../README-vn.md) | [**📚 Tra Cứu Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 1. Hệ Thống Cấp Bậc (Execution Hierarchy)

Toàn bộ hệ thống áp dụng cơ chế điều hành Từ Trên-Xuống-Dưới (Top-Down), đảm bảo không đặc vụ nào đưa ra quyết định vượt quyền.

1. **CEO Chủ Tịch (Tier 0)**: Chính là bạn (Human operator). Người ra mệnh lệnh chiến lược.
2. **Tổng Đặc Vụ Điều Phối (Tier 1)**: C-Suite (Ví dụ: Antigravity/Orchestrator). Có quyền phân tích và chia tải, điều hướng tác vụ khổng lồ nạp từ CEO.
3. **Trưởng Phòng Ban (Tier 2)**: Nhóm cấu trúc các Agent được rập khuôn vào các luật lệ `rules/` cực gắt (VD: Trưởng phòng QA, Kỹ Sư Frontend, Giám đốc Kiểm duyệt nội dung CIV).
4. **Đặc Vụ Công Nhật (Tier 3)**: Những Subagents (Agent nhỏ) tự sinh ra (Spawn) để xử lý một nghiệp vụ cụ thể xíu (như fix syntax, lọc JSON) và tự hủy sau khi hoàn tất vòng đời.

## 2. Nhận Thức Dùng Chung (Shared AI State)

Tất cả các phần tử này được liên kết thông qua Não Bộ máy (Trí nhớ cục bộ `brain/`). 

- **Cái Bảng Đen `blackboard.json`**: Hệ thống liên lạc chính. Nếu Đặc vụ Kỹ sư vừa fix xong cái Login, nó cập nhật bảng đen "Login đã fix". Đặc vụ QA sẽ đọc bảng và nhận ra "Đến giờ chạy Test!". 
- **RAG & Không Gian Tri Thức**: Bằng việc lưu đồ thị Graph-DB cục bộ, AI dễ dàng hấp thụ một tài liệu/repository lạ hoắc để lập trình vào ngày mai.

## 3. Các Phòng Ban Cốt Lõi Đáng Chú Ý

Mặc dù có đến 21 phòng ban, những Node sau cực kỳ quan trọng về mặt công nghệ:
- **Dept 01 (Engineering - Khối Kỹ thuật)**: Giải quyết lập trình backend, frontend...
- **Dept 10 (Strix Security - Khối Bảo mật Cú Vọ)**: Cách ly mã nguồn lạ, ngăn cấm mọi Plugin có hành vi chiếm đoạt thư mục lõi (Zero Trust).
- **Dept 20 (CIV - Khối Thẩm định Tình Báo)**: Chuyên nhằn và cắn vỡ các website ngoài, tài liệu PDF, Github Repos đem nấu lại cho hệ thống RAG tiêu hoá.
- **Dept 22 (Operations - Vận Hành)**: Liên tục tự chạy ngầm để dọn dẹp rác (Deep Cleaner) bảo vệ Git khỏi các cuộc xâm nhập và vấy bẩn bộ nhớ.
