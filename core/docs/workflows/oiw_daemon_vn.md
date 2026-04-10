---
id: oiw-daemon-vn
type: document
owner: SYSTEM
lang: vi
---

# OmniClaw Ingestion Daemon (OID) V2.5

> **Trạng Thái:** ĐANG HOẠT ĐỘNG
> **Tầng:** System Automation (Daemon)
> **Chủ Sở Hữu:** `registry-manager-agent` & `intake-chief-agent`

[**🇬🇧 View in English**](oiw_daemon.md) | [**Quay về Mục Lục Docs**](../README-vn.md)

---

## 1. Tổng Quan & Nhiệm Vụ

**OmniClaw Ingestion Daemon (OID)** là hệ thần kinh tiếp nhận dữ liệu trung tâm của OmniClaw. Nó thay thế các script thủ công phân mảnh bằng một **Pipeline 8 Giai Đoạn** tự động và mạnh mẽ.

OID hoạt động như một daemon chạy liên tục (`omniclaw_oid_daemon.py`). Nó giám sát các thư mục vault cụ thể tìm "ticket" tri thức mới, tiếp nhận nội dung được tham chiếu (URL, GitHub Repo, Tài liệu), bảo mật dữ liệu, trích xuất tri thức, ánh xạ vào registry OmniClaw, và kích hoạt **Tiến Hóa Tự Động** của lực lượng lao động (sinh Agent và Skill mới).

**Năng Lực Chính:**
- **Zero-Trust Security:** Mọi dữ liệu đến được cách ly và kiểm duyệt bởi Strix trước khi vào bộ nhớ lõi.
- **Zero-Token Overhead:** Routing, deduplication, và phân loại ban đầu được xử lý qua script cục bộ xác định (không cần LLM) để tiết kiệm chi phí.
- **Auto-Evolution:** Tự động sinh Agent Trưởng Phòng mới (`create_agent.py`) và kích hoạt Meta-Skill (`Skill Creator Ultra`) nếu dữ liệu đến thuộc lĩnh vực hoàn toàn mới.

---

## 2. Pipeline Kiến Trúc 8 Giai Đoạn

Khi ticket mới đến `storage/vault/DATA/`, daemon thực thi chuỗi sau:

### ⚙️ Giai Đoạn 1: Polling & Queuing
- Daemon liên tục poll `storage/vault/DATA/` tìm file `KI-*.json` phù hợp.
- File được phân tích an toàn. JSON không hợp lệ được chuyển vào thư mục `FAILED`.

### 🔁 Khả Năng Phục Hồi Queue & Round-Robin Retries
- Ticket được xử lý tuần tự từ index `0` của `ACCEPTED_Q`.
- Nếu trích xuất thất bại, ticket KHÔNG được retry ngay lập tức — nó được đẩy về cuối queue.
- Sau `MAX_RETRIES = 3`, ticket được chuyển vĩnh viễn vào `REJECTED_Q` để xem xét thủ công.

### 🛡️ Giai Đoạn 2: Deduplication
- MD5 hashing URL/Repo nguồn đảm bảo cùng dữ liệu không được tiếp nhận hai lần.

### 🛂 Giai Đoạn 3: Fast Triage
- Pattern matching gán Domain/Category cơ bản cho nguồn mà không cần LLM.
- Ví dụ output: `ai_ml`, `frontend`, `marketing`, `security`.

### 🚨 Giai Đoạn 4: Kiểm Duyệt Strix Security
- Daemon gọi script Pwsh (`system/security/QUARANTINE/vet_repo.ps1`) để sandbox và quét repository.
- Code sạch → `vetted/repos/` | Code độc hại → khóa vĩnh viễn trong `QUARANTINE/isolation/`.

### 🧠 Giai Đoạn 5: Trích Xuất Tri Thức & Scraper Nặng
OID thực thi chiến lược fetch từng bước để đảm bảo trích xuất 100%:
- **Chiến lược 1:** Shallow Native Git Clone (Nhanh nhất)
- **Chiến lược 2:** Full Native Git Clone
- **Chiến lược 3:** Github API Zipball nặng (Bỏ qua block Git port/IP)

### 🗂️ Giai Đoạn 6: Ánh Xạ Lõi & Đăng Ký
- `registry_indexer.py`: Thêm Repo và Agent vào `system/registry/SYSTEM_INDEX.yaml`.
- `ki_indexer.py`: Thêm artifact tri thức mới vào Graph trung tâm (`brain/knowledge/KI_INDEX.md`).

### 🧬 Giai Đoạn 7: Tiến Hóa Tự Động (Agent Genesis)
- Nếu Domain được xác định hoàn toàn mới với tổ chức, OID kích hoạt Agent Scaffolding.
- Thực thi `create_agent.py` để sinh Agent Trưởng Phòng Tầng-3 mới phù hợp với domain đó.

### 📡 Giai Đoạn 8: Phát Sóng Ecosystem Real-Time
- Đẩy thống kê động vào Dashboard CEO qua `blackboard.json`.
- Gửi cảnh báo SQLite kép tới `agent_bus.py`.

### 🧹 Giai Đoạn 9: Vệ Sinh
- Kích hoạt `omniclaw_cleanup_crew.py` để quét ticket `.json` tạm thời và giữ OS sạch.

---

## 3. Hướng Dẫn Nhanh

### Cách Chạy OID Daemon
```powershell
$env:OMNICLAW_ROOT = "D:\LongLeo\OmniClaw CORP\OmniClaw"
python system/automations/daemons/omniclaw_oid_daemon.py
```

### Cách Kích Hoạt Ingestion (Phương Pháp 1: File Drop)
1. Tạo file JSON ticket: `storage/vault/DATA/KI-TEST-001.json`
2. Điền thông tin ticket:
```json
{
  "id": "TICKET-999",
  "source": "https://github.com/example/awesome-python-plugin",
  "triage": { "domain": "backend_engineering" }
}
```
3. Theo dõi OID logs trong terminal để xem pipeline 8 giai đoạn thực thi real-time.

### Cách Kích Hoạt Ingestion (Phương Pháp 2: Telegram Bot)
1. Gửi link chứa GitHub shortcode hoặc URL đến OmniClaw Telecom Bot.
2. `telegram_dispatch.py` sẽ tự động định dạng ticket và đặt vào `storage/vault/DATA/`.

---

## 4. Bảo Trì & Vận Hành

- **Log File:** `system/automations/daemons/logs/oid_daemon.log`
- **Hash Database:** `system/automations/daemons/oid/processed_hashes.json`
- **Xử Lý Lỗi:** Ticket thất bại nghiêm trọng được chuyển vào `storage/vault/DATA/FAILED/`.

> *Tài liệu được tạo bởi Antigravity | OmniClaw V3.1*

