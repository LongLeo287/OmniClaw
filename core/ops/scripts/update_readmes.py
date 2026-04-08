import os
import re

en_file = r'D:\OmniClaw\README.md'
vn_file = r'D:\OmniClaw\README-vn.md'

en_additions = """
---

## 🛡️ The OAP Pipeline (Zero-Trust Architecture)

OmniClaw OS enforces a strict **OmniClaw Autonomous Pipeline (OAP)** to govern how new assets, agents, and skills enter the system. It strictly prohibits rogue, unmapped file creation.

- **Gateway-Only Intake (`OER_INBOX`)**: All generators (Agent Generator, Skill Creator, etc.) cannot dump raw configuration files directly into the ecosystem. They must teleport their blueprints into a Quarantine Queue (INBOX).
- **Identity-First Registration (`_DIR_IDENTITY.md`)**: No Agent or Department can be invoked by the Orchestrator without a standardized `_DIR_IDENTITY.md` passport. Unmapped nodes are isolated and rejected.
- **Master Graph Synchronization**: Fully vetted assets are formally ingested into `FAST_INDEX.json` and the Global Capability Map, rendering them officially "Alive" in the system.

---

## ⚙️ Core System Daemons

OmniClaw orchestrates its autonomic functions through four immortal, continuously running background daemons:

| Daemon | Designation | Core Responsibility |
| :--- | :--- | :--- |
| **OIW** | OmniClaw Intake Watchdog | Scrutinizes external internet bounds, scraping raw context inputs and routing them inward to the OS. |
| **OHD** | OmniClaw Health Daemon | Monitors background health, system telemetry, and ensures active processes aren't leaking memory. |
| **OA** | OmniClaw Academy | The self-improvement engine. Analyzes system logs, recruits personnel, builds missing pipelines, and generates missing structures. |
| **OER** | OmniClaw Ecosystem Registrar | The Gatekeeper. Validates OAP identities (`_DIR_IDENTITY.md`), indexes nodes into `FAST_INDEX.json`, and grants official execution privileges. |

---
"""

vn_additions = """
---

## 🛡️ OAP Pipeline (Luồng Zero-Trust)

OmniClaw OS áp đặt một kỷ luật cực kỳ khắt khe: **Luồng Tự Trị OmniClaw (OAP)** nhằm kiểm soát toàn bộ vòng đời của dữ liệu và hệ thống quân lực. OAP hủy diệt mọi nguy cơ từ các file rác.

- **Cổng Báo Danh Duy Nhất (`OER_INBOX`)**: Bất cứ xưởng đúc nào tạo ra Agent mới hay Kỹ năng (Skill) đều không được phép vứt bừa vào bộ máy. Chúng buộc phải bị cách ly tại hàng đợi INBOX.
- **Định Danh Dưới Dạng Căn Cước (`_DIR_IDENTITY.md`)**: Mọi Phòng ban hay Agent đều phải sở hữu Căn Cước chính quy. Bất kỳ thực thể ma nào thiếu Căn Cước sẽ bị chặn đứng quyền biểu quyết bởi cổng Orchestrator.
- **Đồng Bộ Bản Đồ Cốt Lõi**: Những thực thể đã vượt qua đợt kiểm tra sẽ được nạp thông tin vào `FAST_INDEX.json`, chính thức "Hòa Mạng" vào hệ sinh thái.

---

## ⚙️ Core System Daemons (Tiến trình ngầm)

Để duy trì trạng thái luôn thức giấc, OmniClaw vắt sức của 4 Tiến trình Daemons bất tử hoạt động ngầm 24/7 dưới màn hình đen:

| Daemon | Tên Thể Hiện | Nhiệm vụ Tối Cáo |
| :--- | :--- | :--- |
| **OIW** | Intake Watchdog | Trấn giữ biên giới ngoại vi (Internet/Web), cào và thu gom tin tức, dữ liệu thô nạp từ ngoài vào. |
| **OHD** | Health Daemon | Giám sát nhịp tim hệ thống, mức độ ngốn CPU/RAM và đảm bảo các vòng lặp tác vụ không bị tràn bộ nhớ. |
| **OA** | Học Viện Đào Tạo | Cỗ máy tự tiến hóa. Đọc log hệ thống, tự động chắp vá quy trình hỏng, tuyển dụng Agent bù đắp chỗ trống. |
| **OER** | Ecosystem Registrar | Lễ tân tối cao. Đóng dấu duyệt thẻ Căn Cước (`_DIR_IDENTITY.md`) và nhập tịch các Node/Agent mới vào bản đồ hệ thống `FAST_INDEX.json`. |

---
"""

def update_en():
    with open(en_file, 'r', encoding='utf-8') as f: en_content = f.read()
    en_content = re.sub(r'\| \*\*`hr`\*\* \| Legacy hr placeholder.*?\|\n', '', en_content)
    en_content = en_content.replace('29 officially cataloged', '28 officially cataloged')
    en_content = en_content.replace('## 💽 Installation', en_additions.strip() + '\n\n## 💽 Installation')
    with open(en_file, 'w', encoding='utf-8') as f: f.write(en_content)

def update_vn():
    with open(vn_file, 'r', encoding='utf-8') as f: vn_content = f.read()
    vn_content = re.sub(r'\| \*\*`hr`\*\* \| Thư mục lưu trữ dữ liệu.*?\|\n', '', vn_content)
    vn_content = vn_content.replace('29 phòng ban chính quy', '28 phòng ban chính quy')
    vn_content = vn_content.replace('## 💽 Cài đặt', vn_additions.strip() + '\n\n## 💽 Cài đặt')
    with open(vn_file, 'w', encoding='utf-8') as f: f.write(vn_content)

update_en()
update_vn()
print("Success")
