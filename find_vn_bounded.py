import os
from pathlib import Path

target_dirs = [Path(r'D:\LongLeo\AI OS CORP\AI OS\brain\knowledge'), Path(r'D:\LongLeo\AI OS CORP\AI OS\brain\memory')]
words = [' là ', ' thì ', ' mà ', ' các ', ' được ', ' cho ', ' có ', ' không ', ' với ', ' trong ', ' về ']
files_to_translate = []

ignored_folders = ['.git', 'node_modules', 'repos', 'processed_repos', 'bmad_repo', 'claude_bp_repo', 'skills_standard_repo', '.claude']

for td in target_dirs:
    for dirpath, dirnames, filenames in os.walk(td):
        if any(ign in dirpath.replace('\\', '/') for ign in ignored_folders):
            continue

        for f in filenames:
            if f.endswith('.md') and not f.endswith('-vn.md'):
                p = Path(dirpath) / f
                try:
                    c = p.read_text(encoding='utf-8').lower()
                    if any(w in c for w in words):
                        files_to_translate.append(str(p))
                except Exception as e:
                    pass

print(f'\nTotal files to translate: {len(files_to_translate)}\n')
for f in files_to_translate:
    print(Path(f).relative_to(Path(r'D:\LongLeo\AI OS CORP\AI OS')))
