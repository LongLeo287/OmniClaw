# 🧩 Cấu Trúc Plugin (Hệ Thống 3 Tầng)

OmniClaw áp dụng triệt để "Cấu trúc Plugin 3 Tầng" (3-Tier Plugin Architecture) nhằm cơi nới sức mạnh mở rộng của Đặc Vụ, nhưng vẫn khoá chặt rủi ro. Mọi dòng code chạm vào Internet hay tương tác Server đều phải đi qua 3 tầng phân cấp này.

[**🇬🇧 Read in English**](plugin_architecture.md) | [**Quay lại Mục Lục**](../README-vn.md) | [**📚 Tra Cứu Wiki**](https://github.com/LongLeo287/OmniClaw/wiki)

---

## 3 Tầng Lòng Tin (Tiers of Trust)

### 1. Tầng 1: Lõi OS Tối Thượng (Tier 1)
Bao gồm các lệnh chìm tận rễ ở thư mục `system/ops/`. Đây là hơi thở và máu thịt của Trí tuệ Hệ thống (System Intelligence). Chúng đọc, viết `blackboard.json` hay cho phép đẻ ra nhánh Agent khác. Bất khả xâm phạm.

### 2. Tầng 2: Vùng Đóng Gói An Toàn (Tier 2 - Vetted Plugins)
Trú ngụ ngay trong `ecosystem/plugins/`. Phụ kiện thứ ba, cộng đồng chia sẻ sẽ được cấp Thẻ Xanh sau khi lết qua cổng sát hạch tử thần tàn nhẫn của **Phòng Ban 20 (CIV - Content Intake)** và niêm yết vào Sổ Vàng `SKILL_REGISTRY.json`.
- **Ví dụ:** Tool hút data Github, RAG, Trình Shell Command đa năng.
- **Quy Luật Thép:** Trước khi Tầng 2 chạy bất cứ rủi ro (lệnh Xóa, Tải), Cú Vọ Dept 10 (Strix) sẽ liếc qua payload để diệt tận gốc mưu đồ độc hại.

### 3. Tầng 3: Ngoại Lai / Phương Thức MCP (Zero Trust)
Hệ kết nối ngoài hệ thống thông qua giao thức tối tân **Model Context Protocol (MCP)**.
- Chạy chung máy tính nhưng khác luồng tiến trình (Out-of-process).
- Được xem là Ngoại xâm Tiềm năng (Zero Trust) - Chỉ nghe lời từ bộ khung giao thức Schema đã thống nhất (Supabase MCP, Google Drive MCP).

## Tự Build Plugin Sinh Thái Mới
Luật chơi khi bạn muốn dâng hiến mã nguồn cho OmniClaw:
1. Soạn thảo bộ khung `SKILL.md` và tuồn vào `ecosystem/skills/TEN_CUA_BAN/`.
2. Khai báo Schema theo Chuẩn Mở Toàn Cầu (Open Standard).
3. Đẩy vào cho Orchestrator, nó sẽ ném thẳng cho Đặc nhiệm Tình Báo CIV (Dept 20).
4. Nếu Lọt khe! Cục Đăng kiểm (Dept 04) sẽ mở Sổ Vàng và chiêu mộ Plugin của bạn cho đủ 21 Bộ/Ngành xài chung ngay tức khắc.

---

## 📖 Đặc Quyền Sinh Thái: Cấp Bậc Ecosystem Manager (`brain/knowledge`)

Mặc dù cánh cửa Ghi chép (Intake) bị khóa chặt bởi OIW và Thằng Thủ Thư (Phòng 15), **Ecosystem Manager (Thực thể cao nhất của hệ sinh thái) sở hữu "Thẻ Thỉnh Kinh Từ Xa" (Free-Pass Authority)**.
* **Quyền hạn:** Chỉ có Chỉ huy cao nhất của `ecosystem/` mới được Tự do Đọc, Search Semantic, và lướt qua Mạng lưới Thư mục của `brain/knowledge/`. **Các Agent thường và Plugin tuyệt đối không có quyền này.**
* **Tương đương Bảo vệ (Protection Equivalence):** Thư mục `ecosystem/` và `brain/knowledge/` có mức độ bảo vệ giống hệt nhau: **Chỉ Xem (Read-Only Vault)**. Các Đặc vụ không được phép sửa đổi, thay đổi cấu trúc ở hai thư mục lõi này.
