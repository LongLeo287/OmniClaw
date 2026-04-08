# Kế hoạch Đồng hóa OER (OAP)
# Khung Kiến trúc: V2.1
# Quản trị viên: Kiến trúc sư Quản lý Omni (OMA) & Tường lửa Bảo mật (OSF)

## 1. Tóm tắt Thực thi

**OER Assimilation Pipeline (OAP)** là cỗ máy trao đổi chất trung tâm của hệ điều hành OmniClaw. Nó tiêu chuẩn hóa quy trình nhập dữ liệu (mã nguồn, tệp tri thức, dự án từ bên ngoài) và chuyển đổi chúng thành các "Nút Vệ Tinh" (Assimilated Nodes) siêu nén, bảo mật 100% trong Rốn Não.

Bất kỳ Daemon hay tập lệnh nào cố gắng tiêm dữ liệu vào OmniClaw ĐỀU PHẢI tuân thủ trình tự 5 giai đoạn nghiêm ngặt này. Mọi hành vi phá rào đều bị coi là phá hoại hệ thống.

---

## 2. Giao Thức 5 Giai Đoạn (Pipeline Topology)

### 🟢 Giai đoạn 1: NẠP VÀO (Lực lượng Thu thập)
- **Actor:** `sandbox_intake_pipeline.py`
- **Tọa độ:** Internet ➔ `vault/quarantine`
- **Quy tắc:**
  - Dữ liệu thô lập tức được kéo mù từ internet.
  - PHẢI được thả thẳng vào Rổ Cách ly (Quarantine).
  - Không có bất kỳ dòng code nào được khởi chạy trong giai đoạn này.

### 🟡 Giai đoạn 2: KIỂM DỊCH (Lính Gác Cổng)
- **Actor:** `civ_intake_processor.py` chứa (OSF Quarantine Guard)
- **Tọa độ:** `vault/quarantine`
- **Quy tắc:**
  - OSF quét mã độc dựa theo `OSF_THREAT_INTELLIGENCE.json`.
  - Kiểm tra các lệnh mã hóa Base64 độc hại, Reverse Shells, v.v.
  - **Phán quyết:**
    - `Sạch (Exit 0)`: OSF tự tay di dời khối hàng sang thùng rác `OER_INBOX`.
    - `Độc (Exit 1)`: Kích hoạt Lò Thiêu OHD.

### 🟠 Giai đoạn 3: PHÂN LOẠI (Lực lượng Chống Trùng lặp)
- **Actor:** `oa_inbox_triage.py` (Governed by Omni Agent - OA)
- **Tọa độ:** `vault/tmp/state_queues/OER_INBOX`
- **Quy tắc:**
  - OA băm mã MD5 toàn bộ cây thư mục để lọc Dữ liệu Ma (Repositories trùng lặp).
  - Đóng dấu Căn cước Công Dân `_DIR_IDENTITY.md` để xác lập nó thuộc nhóm "Tooling" hay "Algorithm".

### 🔴 Giai đoạn 4: HÓA CHÍN (Lò Tiêu Hóa)
- **Actor:** `oa_swallow_engine.py` (The Swallow Algorithm)
- **Tọa độ:** `vault/tmp/state_queues/OER_INBOX`
- **Quy tắc:**
  - Quét dọn toàn bộ các thư mục rỗng và dọn đi những cặn rác (như `node_modules`).
  - Hầm nhừ toàn bộ Logic Mạng thành Thẻ Bài Mardown Cô Đặc: `*_DISTILLED.md`.

### 🟣 Giai đoạn 5: ĐỒNG HÓA & DỌN RÁC (Kiến trúc sư OMA)
- **Actor:** `oma_knowledge_mapper.py` & `oma_robo_purger.py`
- **Tọa độ:** `brain/knowledge/assimilated_repos/`
- **Quy tắc:**
  - Đẩy thẻ bài `DISTILLED` lên Vỏ Não.
  - Ghi nhận kỹ năng vào Sổ Bìa Đen `SKILL_REGISTRY.json`.
  - Khởi động Kẻ Xóa Sổ (Robo Purger) vác đao xuống `vault/` nhằm TIÊU HỦY không để dính 1 Tệp Raw nào. Hoàn tất chu kỳ Khép Kín Xoay Vòng.
