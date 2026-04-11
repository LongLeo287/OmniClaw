import os
from pathlib import Path

ROOT = Path(r"D:\OmniClaw\ecosystem\workforce\departments")

def remediate_departments():
    remediations = {
        # Encoding bugs
        "‚¬€": "€”",
        "€ €™": "†’",
        "‚¬Å“": '"',
        "‚¬": '"',
        "ï»¿": "",  # BOM artifact
        
        # Branding
        "OmniClaw Corp": "OmniClaw OS",
        "OmniClaw CORP": "OmniClaw OS",
        "AI OS CORP": "OmniClaw OS",
        "AI OS Corp": "OmniClaw OS",
        
        # Broken Paths
        "brain/corp/departments": "ecosystem/workforce/departments",
        "corp/departments": "ecosystem/workforce/departments",
        "ecosystem/workforce/agents": "ecosystem/workforce/departments",
        "corp/memory/departments": "brain/knowledge/org",
        "shared-context/brain/corp/kpi_scoreboard.json": "brain/memory/system_memory/kpi_targets.json",
        "corp/kpi_targets.yaml": "brain/memory/system_memory/kpi_targets.json"
    }

    modified_files = 0
    total_files = 0
    
    for foldername, subfolders, filenames in os.walk(ROOT):
        for filename in filenames:
            if not filename.endswith(('.md', '.yaml', '.ps1', '.bat')):
                continue
                
            filepath = os.path.join(foldername, filename)
            total_files += 1
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                try:
                    with open(filepath, 'r', encoding='cp1252') as f:
                        content = f.read()
                except Exception as e:
                    print(f"Failed to read {filepath}: {e}")
                    continue
            
            original_content = content
            
            for old, new in remediations.items():
                content = content.replace(old, new)
                
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                modified_files += 1

    print(f"Audit Complete! Swept {total_files} files.")
    print(f"Remediated {modified_files} files with errors or broken paths.")

if __name__ == "__main__":
    remediate_departments()

