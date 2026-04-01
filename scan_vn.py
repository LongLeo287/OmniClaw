import os
from pathlib import Path

target_dirs = [
    Path(r'D:\LongLeo\AI OS CORP\AI OS\brain\knowledge'), 
    Path(r'D:\LongLeo\AI OS CORP\AI OS\brain\memory')
]

words = [' là ', ' thì ', ' mà ', ' các ', ' được ', ' cho ', ' có ', ' không ', ' với ', ' trong ', ' về ']
files_to_translate = []

def has_vietnamese(content):
    c_lower = content.lower()
    for w in words:
        if w in c_lower:
            return True
    return False

for td in target_dirs:
    for dirpath, dirnames, filenames in os.walk(td):
        for f in filenames:
            if f.endswith('.md') and not f.endswith('-vn.md'):
                p = Path(dirpath) / f
                try:
                    content = p.read_text(encoding='utf-8')
                    if has_vietnamese(content):
                        files_to_translate.append(str(p))
                except Exception:
                    pass

print(f'FOUND {len(files_to_translate)} FILES:')
for idx, f in enumerate(files_to_translate):
    print(f)
