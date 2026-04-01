import os, json
from pathlib import Path

target_dirs = [Path(r'D:\LongLeo\AI OS CORP\AI OS\brain\knowledge'), Path(r'D:\LongLeo\AI OS CORP\AI OS\brain\memory')]
words = [' là ', ' thì ', ' mà ', ' các ', ' được ', ' cho ', ' có ', ' không ', ' với ', ' trong ', ' về ']
files_to_translate = []

for td in target_dirs:
    for dirpath, dirnames, filenames in os.walk(td):
        for f in filenames:
            if f.endswith('.md') and not f.endswith('-vn.md'):
                p = Path(dirpath) / f
                try:
                    c = p.read_text(encoding='utf-8').lower()
                    if any(w in c for w in words):
                        files_to_translate.append(str(p))
                except:
                    pass

with open('result.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(files_to_translate))
