import os

VAULT_PATH = r"D:\OmniClaw\vault\knowledge\global_codebases"

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
    for root, dirs, files in os.walk(root_path):
        for file in files:
            if file in extensions_to_hide:
                old_path = os.path.join(root, file)
                new_path = old_path + ".knowledge"
                try:
                    # If target already exists, delete it first to allow rename
                    if os.path.exists(new_path):
                        os.remove(new_path)
                    os.rename(old_path, new_path)
                    renamed_count += 1
                except Exception as e:
                    print(f"Failed to rename {old_path}: {e}")
    return renamed_count

if __name__ == "__main__":
    count = hide_manifests(VAULT_PATH)
    print(f"SUCCESS: Renamed {count} manifest files to .knowledge extension.")
