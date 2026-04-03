import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

TARGETS = [
    os.path.join(ROOT, "ecosystem"),
    os.path.join(ROOT, "brain")
]

EXCLUDES = ["vault", "tmp", ".git", "node_modules", "quarantine", "archives"]

def create_identity(dir_path):
    id_file = os.path.join(dir_path, "_DIR_IDENTITY.md")
    if os.path.exists(id_file):
        return False

    # Skip truly empty folders or folders with only placeholder files
    all_items = [
        f for f in os.listdir(dir_path)
        if f not in ("_template_placeholder.md", "_DIR_IDENTITY.md", ".gitkeep", ".gitignore")
        and not f.startswith(".")
    ]
    if len(all_items) == 0:
        return False  # Do not tag empty directories

    dir_name = os.path.basename(dir_path)
    rel_path = os.path.relpath(dir_path, ROOT).replace("\\", "/")

    # Determine description from path context
    desc = f"Storage area for the '{dir_name}' domain"
    if "ecosystem/skills" in rel_path:
        desc = f"Skill collection for the '{dir_name}' capability domain"
    elif "brain/knowledge" in rel_path:
        desc = f"Knowledge base domain: covers the '{dir_name}' subject area"
    elif "brain/rules" in rel_path:
        desc = f"Architecture rules for '{dir_name}'"
    elif "brain/registry" in rel_path:
        desc = f"System registry data for '{dir_name}'"

    content = f"""---
id: {rel_path.replace("/", "-").replace(" ", "_")}
name: {dir_name.replace("_", " ").title()}
path: {rel_path}
type: directory_identity
owner: OER
created_by: OMA-v2.1
---

# {dir_name.replace("_", " ").title()}

{desc}.

> Auto-generated identity tag by OMA v2.1. Do not delete — required for system integrity.
"""
    try:
        with open(id_file, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    except:
        return False

total_created = 0

for target in TARGETS:
    if not os.path.exists(target): continue
    for dirpath, dirnames, filenames in os.walk(target):
        # Exclude hidden or excluded
        dirnames[:] = [d for d in dirnames if not d.startswith(".") and d not in EXCLUDES]
        
        # We don't need identity for direct skill folders if they already have SKILL.md
        # but the rule says "Các tiểu khu thuộc brain/knowledge/ và ecosystem/skills/ BẮT BUỘC phải được OER cắm bảng _DIR_IDENTITY.md tại gốc"
        if create_identity(dirpath):
            total_created += 1
            print(f"[OMA-SYNC] Injected Identity Tag at {os.path.relpath(dirpath, ROOT)}")

print(f"✅ Identity generation complete. Total tags created: {total_created}")
