import re

en_file = r'D:\OmniClaw\README.md'
vn_file = r'D:\OmniClaw\README-vn.md'

en_additions = """
## 🔒 Strict Daemon Segregation (OSF vs OA)

A fundamental principle of OmniClaw's Zero-Trust architecture is the absolute segregation of execution capabilities from learning capabilities:
- **OSF (Sandbox Firewall)** holds exclusive supremacy over the `QUARANTINE` sectors. Only its dedicated Border Agents (`osf_warden`, `osf_auditor`, `osf_quarantine_guard`) possess the clearance to neutralize threats via Martial Law intercepts.
- **OA (Academy)**, despite being the ultimate architectural Auditor, is strictly barred from accessing the `QUARANTINE`. If OA requires analyzing a malfunctioning repository to build a pipeline, the payload must first be neutralized and certified by OSF.

---
"""

vn_additions = """
## 🔒 Phân lập Quyền lực Tuyệt đối (OSF vs OA)

Nguyên tắc bất di bất dịch của kiến trúc Zero-Trust trong OmniClaw đó là sự phân tách giữa Năng lực Học tập và Quyền hạn Trừng phạt:
- **OSF (Sandbox Firewall)** sở hữu uy quyền độc tôn (Supreme Override) trên toàn bộ Vùng Cách ly (`QUARANTINE`). Chỉ những đặc vụ chuyên trách của OSD (`osf_warden`, `osf_auditor`, `osf_quarantine_guard`) mới được phép thao túng, cách ly và tiêu hủy mã độc thông qua Thiết Quân Luật.
- **OA (Academy)**, dù sở hữu năng lực định đoạt và thiết kế của một Đại trưởng lão, vẫn bị chặn đứng Quyền Lực khi chạm đến Sandbox phòng vệ. OA tuyệt đối không được tự ý tiếp cận các file nhiễm độc nếu chưa có con dấu làm sạch của OSF.

---
"""

def update_en():
    with open(en_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '## 🔒 Strict Daemon Segregation' not in content:
        content = content.replace('## 💽 Installation', en_additions.strip() + '\n\n## 💽 Installation')
        with open(en_file, 'w', encoding='utf-8') as f:
            f.write(content)

def update_vn():
    with open(vn_file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if '## 🔒 Phân lập Quyền lực' not in content:
        content = content.replace('## 💽 Cài đặt', vn_additions.strip() + '\n\n## 💽 Cài đặt')
        with open(vn_file, 'w', encoding='utf-8') as f:
            f.write(content)

update_en()
update_vn()
print("OSF Security Segregation applied to documentation.")
