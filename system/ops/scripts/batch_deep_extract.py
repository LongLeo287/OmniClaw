import os, sys, subprocess
from pathlib import Path

def main():
    root = Path(__file__).resolve().parent.parent.parent.parent
    repos_dir = root / "brain" / "knowledge" / "repos"
    extractor_path = root / "system" / "ops" / "scripts" / "knowledge_extractor.py"

    if not repos_dir.exists():
        print(f"Directory {repos_dir} not found.")
        return

    repos = [r for r in repos_dir.iterdir() if r.is_dir()]
    print(f"🚀 Bắt đầu Trích Xuất Tri Thức Sâu cho {len(repos)} Repositories...")

    success = 0
    failed = 0

    for i, repo in enumerate(repos):
        print(f"[{i+1}/{len(repos)}] Đang ép xung trích xuất {repo.name}...")
        try:
            # Chạy extractor, KHÔNG thêm --cleanup để bảo toàn Vault link
            res = subprocess.run(
                [sys.executable, str(extractor_path), "--dir", str(repo)],
                capture_output=True, text=True, encoding='utf-8', errors='replace'
            )
            if res.returncode == 0:
                success += 1
            else:
                print(f"  [LỖI] {repo.name}: {res.stderr}")
                failed += 1
        except Exception as e:
            print(f"  [LỖI GLOBAL] {repo.name}: {e}")
            failed += 1

    print(f"\n✅ HOÀN TẤT. Thành công: {success}. Thất bại: {failed}.")

if __name__ == "__main__":
    main()
