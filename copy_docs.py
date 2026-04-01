import shutil
from pathlib import Path

repo_root = Path(r'D:\LongLeo\AI OS CORP\AI OS')
b_dir = repo_root / 'brain' / 'knowledge'
d_arch = repo_root / 'docs' / 'architecture'
d_ug = repo_root / 'docs' / 'usage_guides'

d_arch.mkdir(parents=True, exist_ok=True)
d_ug.mkdir(parents=True, exist_ok=True)

mappings = [
    (b_dir / 'ACTIVATION_BOARD.md', d_ug / 'ACTIVATION_GUIDE.md'),
    (b_dir / 'AI_OS_SYSTEM_MAP.md', d_arch / 'MASTER_SYSTEM_MAP.md'),
    (b_dir / 'CAPABILITY_MAP.md', d_arch / 'SKILLS_AND_PLUGINS_MAP.md'),
    (b_dir / 'LIBRARY_INDEX.md', d_ug / 'DATA_SCIENCE_LIBRARY.md')
]

for src, dst in mappings:
    if src.exists():
        shutil.copy2(src, dst)
        print(f'Copied: {src.name} -> {dst.relative_to(repo_root)}')
    else:
        print(f'Missing: {src}')
