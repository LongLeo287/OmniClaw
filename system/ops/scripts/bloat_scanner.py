import os
from pathlib import Path

_AOS_ROOT = os.getenv("AOS_ROOT") or str(Path(__file__).resolve().parents[3])
TARGET = Path(_AOS_ROOT) / "brain" / "knowledge" / "repos"

def get_size(path):
    total = 0
    for root, _, files in os.walk(path):
        for f in files:
            try:
                total += os.path.getsize(os.path.join(root, f))
            except Exception:
                pass
    return total

if __name__ == "__main__":
    if not TARGET.exists():
        print("Thu muc brain/knowledge/repos chua ton tai.")
        exit(0)

    sizes = []
    for org in TARGET.iterdir():
        if org.is_dir():
            for repo in org.iterdir():
                sizes.append((repo, get_size(repo)))
        else:
            sizes.append((org, get_size(org)))

    sizes.sort(key=lambda x: x[1], reverse=True)

    print("Top 15 Cuc Bloat Nang Nhat trong brain/knowledge/repos:")
    for path, size in sizes[:15]:
        print(f"{path.relative_to(TARGET)}: {size / (1024*1024):.2f} MB")

    total_gb = sum(s for _, s in sizes) / (1024**3)
    print(f"\nTong dung luong: {total_gb:.2f} GB")
    print(f"Tong so project tho: {len(sizes)}")
