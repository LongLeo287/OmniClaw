# OmniClaw Master Registry 🗄️📜

**Path:** `brain/registry/`
**Namespace:** `brain.registry`
**Status:** V5.0 (Curated & Sync-Enabled)

Welcome to the **Master Registry** of OmniClaw. This directory serves as the authoritative truth for all registered external skills, dynamic topological indexing, and execution routing within the V5.0 architecture.

Chào mừng đến với **Hệ thống Đăng ký Lõi (Master Registry)** của OmniClaw. Thư mục này đóng vai trò là chân lý tối thượng định nghĩa các kỹ năng ngoại vi, lập chỉ mục địa hình động và định tuyến thực thi trong kiến trúc V5.0.

---

## 🚀 Core Competencies (Cốt Lõi Hệ Thống)

1. **`SKILL_REGISTRY.json` (OER - OmniClaw Execution Registry)**
   *EN:* The monolithic database containing over 5,000+ available skill tools, heavily utilized by the execution daemons. Do not edit directly unless triggered by OER Daemon logic.
   *VN:* Cơ sở dữ liệu nguyên khối chứa hơn 5,000+ công cụ kỹ năng, được các Daemon thao tác sử dụng liên tục. Không sửa trực tiếp trừ phi kích hoạt qua luồng OER Daemon.

2. **`SYSTEM_INDEX.yaml` (OMA Map)**
   *EN:* Auto-generated index of the massive physical directory topology mapped by `oma_indexer.py`. It serves as a rapid resolution fallback for system scans.
   *VN:* Bản đồ địa hình vật lý khổng lồ tự động render bởi `oma_indexer.py`. Đóng vai trò là màng lọc truy xuất cực nhanh cho các lệnh quét hệ thống.

3. **`SKILL_ROUTER.yaml`**
   *EN:* The Execution Matrix deciding which OS Daemon handles which specific execution payloads (e.g. `OAP` handles Code, `OIW` handles Scrapes, `OHD` handles Cleanups).
   *VN:* Ma trận thực thi phân bổ luồng công việc cho 8-Daemon (VD: `OAP` xử lý Code, `OIW` chuyên đi cào dữ liệu, `OHD` dọn rác).

4. **`EXTERNAL_SKILL_SOURCES.yaml` & `version.json`**
   *EN:* External Git sources mapping and exact active component firmware configuration.
   *VN:* Quét trỏ về các nguồn Git kỹ năng bên ngoài và quản lý cấu hình firmware ở trạng thái đang hoạt động.

---

> ⚠️ **THE ISOLATION BOUNDARY (GIT SECURITY)**
> *EN:* This space is heavily restricted and strictly monitored by the `OSF_Daemon`. All untracked logs (e.g., `cli_run.log`) or machine-specific trash are blocked by `.gitignore`.
> *VN:* Khu vực này bị hạn chế gắt gao và được theo dõi bởi `OSF_Daemon`. Moị file log tự do (như `cli_run.log`) hoặc rác phát sinh từ máy cục bộ đều bị chặn đứng bởi `.gitignore` và bị cấm đưa lên đây.

---
*OmniClaw V5.0 Blueprint | Forged by Antigravity OS Architect | brain.registry | 2026-04-11*
