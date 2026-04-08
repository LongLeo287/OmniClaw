---
id: oap-architecture-vn
type: document
owner: SYSTEM
lang: vi
---

# THIẾT KẾ: Pipeline Đồng Hóa OER (OAP)
# Khung Kiến Trúc: V2.1
# Quản Trị: OMA Architect & OSF Security Firewall

[**🇬🇧 View in English**](OAP_ARCHITECTURE.md) | [**Quay về Mục Lục Docs**](../README-vn.md)

## 1. Tóm Tắt Điều Hành

**Pipeline Đồng Hóa OER (OAP)** là động cơ trao đổi chất trung tâm của OmniClaw OS. Nó chuẩn hóa quy trình tiếp nhận dữ liệu bên ngoài (repository, knowledge drop, code ngoài) và chuyển đổi thành các "Assimilated Node" được chắt lọc cao độ, bảo mật và có thể tìm kiếm bên trong vỏ não Brain.

Bất kỳ daemon hoặc script nào cố gắng đưa dữ liệu vào OmniClaw PHẢI tuân thủ 5 giai đoạn nghiêm ngặt này. Sai lệch là hành động thù địch với hệ thống.

---

## 2. Giao Thức 5 Giai Đoạn (Cấu Trúc Liên Lạc Pipeline)

### 🟢 Giai Đoạn 1: INTAKE (Cloner/Thu Mua)
- **Actor:** `civ_intake_processor.py` / `sandbox_intake_pipeline.py`
- **Vị Trí:** Mạng ➔ `vault/quarantine`
- **Quy Tắc:**
  - Dữ liệu thô được lấy từ internet một cách mù quáng.
  - PHẢI đặt trực tiếp vào quarantine hoặc sandbox_env.
  - Không cho phép thực thi code trực tiếp trong giai đoạn này.

### 🟡 Giai Đoạn 2: VALIDATION (Gatekeeper / X-Ray)
- **Actor:** `osf_malware_censor.py` (Điều hành bởi OSF Quarantine Guard)
- **Vị Trí:** `vault/quarantine`
- **Quy Tắc:**
  - OSF quét tất cả script đến bằng quy tắc được tạo động từ `OSF_THREAT_INTELLIGENCE.json`.
  - Kiểm tra encoding Base64, lệnh shell phá hoại và payload độc hại.
  - **Kết Quả:**
    - `0` (Sạch/Pass): Chuyển sang Giai Đoạn 3.
    - `1` (Độc/Fail): Dừng Pipeline. Gửi đến OHD để Vaporization.

### 🟠 Giai Đoạn 3: TRIAGE (Phân Loại & Deduplication)
- **Actor:** `oa_inbox_triage.py` (Điều hành bởi OA)
- **Vị Trí:** `vault/tmp/state_queues/OER_INBOX`
- **Quy Tắc:**
  - Dữ liệu an toàn được phép vào INBOX thực.
  - OA tạo hash cấu trúc sâu của các thư mục.
  - Deduplication xảy ra tự động để ngăn nhiễm độc logic.

### 🔴 Giai Đoạn 4: DISTILLATION (Bộ Tiêu Hóa)
- **Actor:** `oa_swallow_engine.py` (Thuật Toán Swallow)
- **Vị Trí:** `vault/tmp/state_queues/OER_INBOX`
- **Quy Tắc:**
  - Cây thư mục thô được scrape, phân tích và nén đệ quy.
  - Boilerplate không liên quan (như `node_modules` hoặc `.git`) bị loại bỏ.
  - Chuyển đổi dữ liệu thành thẻ Markdown mật độ cao: `*_DISTILLED.md`.
  - Thư mục thô gốc bị OMA Robo Purger xóa sạch.

### 🟣 Giai Đoạn 5: INTEGRATION (Mapper & Coder)
- **Actor:** `oma_knowledge_mapper.py` & `skill_loader.ps1`
- **Vị Trí:** `brain/knowledge/assimilated_repos/` & `ecosystem/skills/`
- **Quy Tắc:**
  - Thẻ tri thức đã chắt lọc được chuyển đến vị trí não vĩnh viễn.
  - Đồ thị `_DIR_IDENTITY.md` được cập nhật để đăng ký node con.
  - `SKILL_REGISTRY.json` và `LIBRARY_GRAPH.json` toàn cầu được làm mới động.

---

## 3. Chính Sách Thực Thi (Lời Hứa OSF)
Pipeline OAP đảm bảo OmniClaw luôn sạch, siêu tối ưu và không thể bị nhiễm. Bất kỳ nỗ lực nào bỏ qua **Giai Đoạn Validation (Giai Đoạn 2)** sẽ dẫn đến Orchestrator tạm dừng luồng Daemon chịu trách nhiệm về việc bỏ qua đó.

> Tất cả script trong `core/ops/scripts` lấy Git repository phải gọi OSF trước khi phân tích. Không làm vậy sẽ phá vỡ Island Sandbox Protocol.

---

## 4. Hình Thái File (Phân Loại Artifact)

Để ngăn lãng phí rải rác ("file pollution") và đảm bảo vòng lặp Ouroboros khép kín, Daemon bị nghiêm cấm tạo extension file tùy ý ngoài các loại artifact rõ ràng này:

### 🧟 Vùng Thô (`vault/quarantine` & `vault/tmp`)
- **Được Phép:** File thô không có cấu trúc (`*.py`, `*.js`, etc.) từ input clone bên ngoài.
- **Quy Tắc:** Không thể thực thi (Sandbox lock). Tự động Garbage Collected qua `oma_robo_purger.py` cuối chu kỳ.

### 🧠 Vùng Chắt Lọc (`brain/knowledge/assimilated_repos`)
- **Được Phép:**
  1. `[RepoName]_DISTILLED.md`: Logic/bộ nhớ thuần túy đã trích xuất.
  2. `_DIR_IDENTITY.md`: Thẻ Nhận Dạng Đồ Thị.
- **Quy Tắc:** File code thô (`.py, .js`) **BỊ CẤM** tồn tại trong vùng Brain.

### 🌐 Vùng Logic (`ecosystem/plugins` & `brain/shared-context`)
- **Được Phép:**
  1. `SKILL.md`: Plugin markdown thực thi được.
  2. `*.json` (Registry): `SKILL_REGISTRY.json`, `LIBRARY_GRAPH.json`, `OSF_THREAT_INTELLIGENCE.json`.
- **Quy Tắc:** Các file JSON và MD này là node đồ thị nặng về đọc. Chúng đại diện cho sự nhận thức sống của OmniClaw.

*Nếu một file không nằm trong Phân Loại này, nó không hợp pháp thuộc vòng đời OAP. Đây là orphan và sẽ bị vaporized.*
