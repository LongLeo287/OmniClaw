import os
from pathlib import Path
import subprocess

def create_junctions():
    root = Path(__file__).resolve().parent.parent.parent.parent
    archive_dir = root / "storage" / "vault" / "ARCHIVE"
    repos_dir = root / "brain" / "knowledge" / "repos"

    if not archive_dir.exists():
        print(f"Directory {archive_dir} not found. Nothing to restore.")
        return

    # Ensure repos target exists
    repos_dir.mkdir(parents=True, exist_ok=True)

    archived_repos = [d for d in archive_dir.iterdir() if d.is_dir()]
    print(f"Found {len(archived_repos)} repos in Vault. Restoring Junction Links...")

    success_count = 0
    for repo in archived_repos:
        link_path = repos_dir / repo.name
        if not link_path.exists():
            try:
                subprocess.run(
                    f'cmd /c mklink /J "{link_path}" "{repo}"',
                    shell=True, check=True, stdout=subprocess.DEVNULL
                )
                success_count += 1
            except Exception as e:
                print(f"Error creating link for {repo.name}: {e}")
        else:
            print(f"Link or folder already exists for: {repo.name}")

    print(f"Restored {success_count} Junction Symlinks to {repos_dir}!")

if __name__ == "__main__":
    create_junctions()