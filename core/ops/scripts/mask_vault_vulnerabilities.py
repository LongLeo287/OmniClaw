import os

PATHS_TO_CLEAN = [
    r"D:\OmniClaw\vault\knowledge\global_codebases",
    r"D:\OmniClaw\ecosystem\skills"
]

extensions_to_hide = [
    "package.json",
    "package-lock.json",
    "requirements.txt",
    "requirements-dev.txt",
    "Pipfile",
    "Pipfile.lock",
    "composer.json",
    "Gemfile",
    "Gemfile.lock"
]

def hide_manifests(root_path):
    renamed_count = 0
    if not os.path.exists(root_path):
        return 0
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file in extensions_to_hide:
                old_path = os.path.join(root, file)
                new_path = old_path + ".knowledge"
                try:
                    if os.path.exists(new_path):
                        os.remove(new_path)
                    os.rename(old_path, new_path)
                    renamed_count += 1
                except Exception as e:
                    print(f"Failed to rename {old_path}: {e}")
    return renamed_count

if __name__ == "__main__":
    total = 0
    for path in PATHS_TO_CLEAN:
        count = hide_manifests(path)
        print(f"Processed {path}: Renamed {count} files.")
        total += count
    print(f"FINAL SUCCESS: Renamed {total} manifest files system-wide.")
