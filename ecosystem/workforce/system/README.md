# 🏛️ OmniClaw System Quadrant (Workforce Configuration)

**Phân khu Thể chế & Thiết đặt Tĩnh (Declarative Configuration Zone)**

Khu vực `ecosystem/workforce/system/` là trụ cột thứ 4 của Mạng lưới Lao động. Không giống như các Agents hay Phòng ban chuyên thực thi tác vụ, phân khu này hoạt động như một "Tủ hồ sơ Hành chính". Nó chỉ lưu trữ các đạo luật, khuôn mẫu Prompt, và thẻ căn cước khai báo của Hệ thống.

## 📂 Kiến Trúc Thư Mục Hiện Tại
- `corp_prompts/`: Chứa Hệ tư tưởng và Văn phong của OS. Các khuôn mẫu prompt phân cấp (CEO, C-Suite, Manager) và các loại bùa ngôn ngữ (`runes/`) bắt buộc mọi Agent phải nạp trước khi hành động.
- `daemons/`: Nơi lưu trữ Sổ đăng ký (các file cấu hình `.yaml`) của Tứ Đại Daemons chạy ngầm bảo vệ hệ thống (OA, OIW, OER, OHD).

---

## 🔒 SYSTEM PROTOCOL (Luật Bất Di Bất Dịch)

> [!CAUTION]  
> Phân khu này bị áp đặt Lệnh Cấm Tuyệt Đối (Zero-Trust Boundaries).

1. **Cấm Thực Thi Mã (No Code Execution):** Tuyệt đối không được chứa file `.py`, `.bat`, hay `.ps1`. Toàn bộ logic giải thuật phải nằm ở tầng não bộ `core/ops/` hoặc `core/daemons/`.
2. **Cấm Nuôi Cấy Đặc Vụ (No Autonomous Agents):** Không một Agent tự trị nào được phép cấp định danh (`AGENT.md`) tại đây. Toàn bộ Đặc vụ phải được sinh ra tại `workforce/agents/`.
3. **Bypass Trình Quét Ngầm (Daemon Immunity):** Để tiết kiệm tài nguyên vi xử lý, vòng lặp vô tận của OA Academy Daemon sẽ KHÔNG càn quét khu vực này. Mọi thay đổi tại đây chỉ được rà soát khi Quản Trị Viên kích hoạt lệnh **Bypass Scan** thủ công.
