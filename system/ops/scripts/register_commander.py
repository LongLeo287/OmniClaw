import os
AGENTS_MD = r'd:\LongLeo\AI OS CORP\AI OS\brain\shared-context\AGENTS.md'

with open(AGENTS_MD, 'r', encoding='utf-8') as f:
    content = f.read()

# Append to AGENTS.md
table_header = '| Subagent | Role | Activated by |\n|----------|------|--------------|'
if table_header in content:
    new_row = '\n| ridge-commander-agent | Cục Trưởng Cục Hải Quan & An Ninh Cửa Khẩu (Gateway) | arch-chief-agent |'
    content = content.replace(table_header, table_header + new_row)
else:
    # Just append
    content += '\n| ridge-commander-agent | Cục Trưởng Cục Hải Quan & An Ninh Cửa Khẩu (Gateway) | arch-chief-agent |'

with open(AGENTS_MD, 'w', encoding='utf-8') as f:
    f.write(content)

print("Đã đăng ký danh phận bridge-commander-agent vào AGENTS.md")
