import os

os.makedirs('.github', exist_ok=True)
os.makedirs('.github/ISSUE_TEMPLATE', exist_ok=True)

def read_file(name):
    if os.path.exists(name):
        with open(name, 'r', encoding='utf-8') as f:
            return f.read()
    return ''

# 1. Merge CODE_OF_CONDUCT
en_coc = read_file('CODE_OF_CONDUCT.md')
vi_coc = read_file('CODE_OF_CONDUCT_vi.md')
if en_coc or vi_coc:
    with open('.github/CODE_OF_CONDUCT.md', 'w', encoding='utf-8') as f:
        en_content = en_coc.replace('*Đọc bản [Tiếng Việt (Vietnamese version) tại đây](CODE_OF_CONDUCT_vi.md).*', '*Tiếng Việt (Vietnamese version) is available below.*')
        vi_content = vi_coc.replace('*This page is available in [English](CODE_OF_CONDUCT.md).*', '')
        f.write(en_content + '\n\n---\n\n' + vi_content)

# 2. Merge CONTRIBUTING
en_con = read_file('CONTRIBUTING.md')
vi_con = read_file('CONTRIBUTING_vi.md')
if en_con or vi_con:
    with open('.github/CONTRIBUTING.md', 'w', encoding='utf-8') as f:
        en_content = en_con.replace('*Đọc bản [Tiếng Việt (Vietnamese version) tại đây](CONTRIBUTING_vi.md).*', '*Tiếng Việt (Vietnamese version) is available below.*')
        vi_content = vi_con.replace('*This page is available in [English](CONTRIBUTING.md).*', '')
        f.write(en_content + '\n\n---\n\n' + vi_content)

# 3. Merge SECURITY
en_sec = read_file('SECURITY.md')
vi_sec = read_file('SECURITY_vi.md')
if en_sec or vi_sec:
    with open('.github/SECURITY.md', 'w', encoding='utf-8') as f:
        en_content = en_sec.replace('*Đọc bản [Tiếng Việt (Vietnamese version) tại đây](SECURITY_vi.md).*', '*Tiếng Việt (Vietnamese version) is available below.*')
        vi_content = vi_sec.replace('*This page is available in [English](SECURITY.md).*', '')
        f.write(en_content + '\n\n---\n\n' + vi_content)

# 4. ISSUE_TEMPLATE
if os.path.exists('GITHUB_ISSUES.md'):
    with open('.github/ISSUE_TEMPLATE/bug_report.md', 'w', encoding='utf-8') as f:
        f.write(read_file('GITHUB_ISSUES.md'))

# 5. Combine README
en_rm = read_file('README.md')
vi_rm = read_file('README-vn.md')
if en_rm and vi_rm:
    with open('README.md', 'w', encoding='utf-8') as f:
        text = en_rm.replace('[Tiếng Việt Version / Bản Tiếng Việt](README-vn.md)', '[Tiếng Việt Version / Bản Tiếng Việt](#bản-tiếng-việt-vietnamese-version)')
        if 'Bản Tiếng Việt (Vietnamese version)' not in text:
            text += '\n\n---\n\n# Bản Tiếng Việt (Vietnamese version)\n\n' + vi_rm.replace('[English Version / Bản Tiếng Anh](README.md)', '')
        f.write(text)

print('Merge Complete!')
