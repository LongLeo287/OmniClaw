# 🏛️ OER & Lục Bộ Daemons — Quản Trị Hệ Sinh Thái OmniClaw

> **Thẩm quyền:** CEO (LongLeo) | **Phiên bản:** 2.2 | **Ngày:** 2026-04-05
> **Trạng thái:** HOẠT ĐỘNG — Tài liệu này thay thế mọi định nghĩa phân quyền trước đó.

[**🇺🇸 English Version**](CORE_DAEMONS_AND_OER.md) | [**Back to Docs**](../README.md)

Tài liệu này định nghĩa Lục Mạch (6 Core Daemons) của hệ điều hành OmniClaw và **Quy trình 5 Bước Cổng Tự Động (5-Gate Pipeline)** quản lý cách mọi Kỹ năng (Skill), Plugin, Đặc vụ (Agent) bước chân vào hệ sinh thái.

---

## 1. Bản Mệnh Lục Bộ (The 6 Pillars)

Để ngăn chặn vi phạm bảo mật và tranh giành quyền lực, hệ thống chia nhỏ quyền cai trị cho 6 Cỗ máy (Daemons) và Nghiêm cấm tuyệt đối sự giẫm chân lên vai trò của nhau:

| Daemon | Tên Đầy Đủ | Vai Trò Chính | Nhiệm Vụ Tối Thượng |
|---|---|---|---|
| **OIW** | OmniClaw Intake Worker | **Kẻ Kéo Lưới** | Chỉ có nhiệm vụ kéo rác và Mã Nguồn (Code) từ internet vứt thẳng vào vùng Cấm. |
| **OSF** | OmniClaw Sandbox Firewall | **Tường Lửa Biên Giới** | Gác cổng ngoài cùng. Sử dụng các kỹ năng chẩn đoán mối đe dọa (một số mượn từ OHD) để phong tỏa mã độc. |
| **OHD** | OmniClaw Health Daemon | **Đại Bác Sĩ Nội Khoa** | Giải phẫu học Hệ thống. Dọn dẹp cache, Quét chuyên sâu chuỗi cung ứng, và nghiên cứu đẻ ra Cấp phát Skill diệt Virus cho OSF xài chung. |
| **OA** | OmniClaw Academy | **Nghị Viện / Phòng Nghiên Cứu** | Là Quan Tòa tối cao. Đọc và chấm điểm kho Repository `CIV`. Tuân thủ nghiệm ngặt 8 Định Luật. Khi nó đánh giá 1 mã nguồn là TUYỆT VỜI, nó sẽ phát lệnh bắt đầu "Chế Tác" (Forge) Hồ sơ năng lực mới! |
| **Dept 1** | Kỹ sư Công nghệ Lõi | **Thợ Đúc Form (Forge)** | Không phải Daemon nhưng là tay sai của OA. Được OA yêu cầu viết code trực tiếp sinh ra file `SKILL.md`, viết Agent và Test. |
| **OER** | OmniClaw Ecosystem Registry | **Thủ Kho Cấp ID (Registrar)** | **Độc Toàn Quyền** cấp mã định danh (SKILL-xxxx, PLG-xxxx), điền tên vào sổ cái `SKILL_REGISTRY.json` và xếp hàng lên kho `ecosystem/`. |
| **OMA** | Omni Management Architect | **Kỹ Sư Quản Lý Hạ Tầng** | Bảo vệ cấu trúc Phân mảnh File, gắn các Cục Não Kiến thức vào mạng lưới Neural siêu lớn `LIBRARY_GRAPH.json` và điều khiển xe Phân Hủy Rác chôn vùi số rác dư thừa. |

---

## 2. Đường Đồng Bộ Giao Ca (Asynchronous 5-Gate Handshake)

```
 [CỔNG 0: OER DUPLICATE CHECK]  -----> NẾU CÓ TRÙNG LẶP SẼ BLOCK NGAY LẬP TỨC!
        |
 [PHASE 1: OIW — KÉO LƯỚI]
   - Clone Repo vào vault/quarantine/
        |
 [PHASE 2: OSF & OHD — KIỂM DỊCH BIÊN GIỚI]
   - OSF chặn cổng ngoài tránh mã độc công khai.
   - OHD Bác sĩ quét chuyên sâu chuỗi cung ứng, clear cache rác.
        |        \___THẤT BẠI__> OHD Tiêu Hủy Payload.
 [PHASE 3: OA — NGHỊ VIỆN NGHIÊN CỨU & AUDIT]
   - Viện Hàn Lâm (Dept 9 An Ninh, Dept 12 Pháp Lý) nghiên cứu Code.
   - Thẩm định 8 Cột trụ bảo mật và Kiến trúc.
        |        \___THẤT BẠI__> Lập Báo cáo phong nhốt Code.
 [PHASE 4: Dept 1 (Kỹ Thuật) — RÈN HỒ SƠ NĂNG LỰC]
   - Trí Tuệ Nhân Tạo dùng Tool:
   - Viết File Báo Cáo Năng Lực `SKILL.md`.
   - Sinh bộ luật Nhận Diên Đặc vụ Agent và MCP mới.
        |
 [PHASE 5: OER — NHẬP KHO CHÍNH THỨC]
     (& Kết hợp OMA Xây Cầu Mạch)
   - Thủ kho OER cấp Căn Cước ID Độc Nhất.
   - Nhập tên vào gia phả `SKILL_REGISTRY.json`.
   - Chuyển nhà file vào đúng thư mục ecosystem/.
   - Kiến trúc sư OMA móc Mạch Nơ Ron vào khối LIBRARY_GRAPH.json.
```
