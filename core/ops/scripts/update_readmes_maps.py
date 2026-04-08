import re

en_file = r'D:\OmniClaw\README.md'
vn_file = r'D:\OmniClaw\README-vn.md'

en_additions = """
## 🗺️ Master Mapping & Knowledge Tracking

To guarantee absolute synchronization across the internal filesystem, OmniClaw strictly avoids localized map files. Instead, it relies on two globally tracked Master Maps managed dynamically by the registry daemons:

- **The Fast Index (`FAST_INDEX.json`)**: The authoritative ledger of the operating system. Every legitimate Agent, Department, and Skill across the network is stamped here. If a file is not in the Fast Index, Orchestrator treats it as invisible.
- **The Library Graph (`LIBRARY_GRAPH.json`)**: Maps the complex relational edges between sub-agents and their required Knowledge files, rendering a 2D network diagram of the internal Brain matrix. 
- **Cognitive Tracking (`brain/knowledge`)**: All organizational memory, KPI Scoreboards, and long-term storage architectures are isolated within the `brain/` directory. System Agents strictly interface with this vault via their verified pointers, avoiding data contamination across the ecosystem.

---
"""

vn_additions = """
## 🗺️ Master Map & Cấu Trúc Đồ Thị Tri Thức (Knowledge Tracking)

Để triệt tiêu tình trạng dữ liệu mồ côi hoặc lạc mất trên đường truyền, OmniClaw cấm tuyệt đối việc tạo ra các bản đồ rác rải rác (`MAP.md`). Thay vào đó, toàn bộ mạng lưới cấu trúc được định vị tập trung tại 2 Bảng Đồ Chí Tôn (Master Maps):

- **Bản đồ Truy Tốc (`FAST_INDEX.json`)**: Là cuốn sổ sinh tử của Hệ điều hành. Mọi Agent, Phòng Ban hay Kỹ năng đều phải được nạp thẻ Căn Cước vào đây. Bất cứ thực thể nào không có tên trong Fast Index sẽ tự động bị hệ thống từ chối quyền truy cập.
- **Cấu trúc Đồ Thị (`LIBRARY_GRAPH.json`)**: Định tuyến các sợi dây liên kết vô hình giữa hệ thống Quân Lực (Agents) và Siêu Khối Trí Tuệ (Knowledge). Đồ thị này giúp hệ thống nhận diện sâu sự phụ thuộc của Agent vào kiến trúc hạ tầng.
- **Tàng Kinh Các (`brain/knowledge`)**: Khu vực đóng băng lưu trữ trí nhớ dài hạn (Memory), các Bảng Cận Cảnh Chỉ Tiêu (KPI Scoreboard). Toàn bộ Quân lực chỉ được kết nối với Vùng Não này thông qua đường truyền Mapped Links bảo mật, đảm bảo không một bit dữ liệu nào bị xâm phạm trái phép.

---
"""

def update_en():
    with open(en_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Inject before ## 💽 Installation
    if '## 🗺️ Master Mapping' not in content:
        content = content.replace('## 💽 Installation', en_additions.strip() + '\n\n## 💽 Installation')
        with open(en_file, 'w', encoding='utf-8') as f:
            f.write(content)

def update_vn():
    with open(vn_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '## 🗺️ Master Map' not in content:
        content = content.replace('## 💽 Cài đặt', vn_additions.strip() + '\n\n## 💽 Cài đặt')
        with open(vn_file, 'w', encoding='utf-8') as f:
            f.write(content)

update_en()
update_vn()
print("Graphs and Knowledge update applied.")
