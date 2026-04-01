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

## Tự Build Plugin Sinh Thái Mới (Quy trình Handoff Chặt Chẽ)
Để tránh giẫm đạp quyền hạn (Overlapping Authority), việc Build Plugin tuân thủ 3 bước Bàn Giao Cứng:
1. **Cách Ly (Quarantine):** Code thô của Plugin (do R&D hoặc thợ code kéo về) phải được ném vào `storage/vault/quarantine/`.
2. **Trạm Kiểm Dịch (Phòng 10):** Cảnh sát `strix-agent` vào rà file. Nếu sạch, đóng dấu Mộc An Toàn (Pass Security).
3. **Mở Cửa Rừng (Phòng 14):** Chỉ duy nhất `registry-manager-agent` được phép cầm file Đã Duyệt mang vào `ecosystem/skills/`, ghi sổ Schema, và cập nhật kho tổng `SKILL_REGISTRY.json`. Mọi Agent khác (kể cả CTO hay Orchestrator) tuyệt đối KHÔNG ĐƯỢC thao tác file trực tiếp trong thư mục `ecosystem/`.

---

## 📖 Đặc Quyền Sinh Thái: Cấp Bậc Trưởng Phòng 14 (`brain/knowledge`)

Mặc dù cánh cửa Ghi chép (Intake) bị khóa chặt bởi OIW và Thằng Thủ Thư (Phòng 15), **Trưởng phòng 14 (`registry-manager-agent`) sở hữu "Thẻ Thỉnh Kinh Từ Xa" (Free-Pass Authority)** để phục vụ công tác điều phối Skill.
* **Quyền hạn:** Chỉ có Phòng 14 mới được Tự do Đọc, Search Semantic, và lướt qua Mạng lưới Thư mục của `brain/knowledge/`. **Các Agent thường, Plugin, CTO, Orchestrator tuyệt đối không có quyền này.**
* **Tương đương Bảo vệ (Protection Equivalence):** Thư mục `ecosystem/` và `brain/knowledge/` có mức độ bảo vệ giống hệt nhau: **Chỉ Xem (Read-Only Vault)**. Các Đặc vụ không được phép sửa đổi, thay đổi cấu trúc ở hai thư mục lõi này.
