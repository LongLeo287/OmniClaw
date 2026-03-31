import os
import json
import glob
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent.parent.parent.parent
REPOS_DIR = ROOT / "brain" / "knowledge" / "repos"
PROCESSED_DIR = ROOT / "brain" / "knowledge" / "processed_repos"

os.makedirs(PROCESSED_DIR, exist_ok=True)

def analyze_repo(repo_path):
    repo = Path(repo_path)
    name = repo.name
    
    # Extract README
    readme_content = ""
    for md in ["README.md", "readme.md", "Readme.md"]:
        rpath = repo / md
        if rpath.exists():
            readme_content = rpath.read_text(encoding='utf-8', errors='ignore')[:1500]
            break
            
    # Count files by extension
    ext_counts = {}
    for root, _, files in os.walk(repo):
        if '.git' in root: continue
        for f in files:
            ext = os.path.splitext(f)[1]
            ext_counts[ext] = ext_counts.get(ext, 0) + 1
            
    # Find dependencies
    tech_stack = []
    if (repo / "package.json").exists():
        tech_stack.append("Node.js/NPM")
    if (repo / "requirements.txt").exists() or (repo / "pyproject.toml").exists():
        tech_stack.append("Python")
    if (repo / "go.mod").exists():
        tech_stack.append("Go")
        
    return {
        "name": name,
        "readme_snippet": readme_content,
        "files_stats": ext_counts,
        "tech_stack": tech_stack
    }

def main():
    if not REPOS_DIR.exists():
        print(f"Directory {REPOS_DIR} does not exist. Nothing to analyze.")
        return

    repos = [d for d in REPOS_DIR.iterdir() if d.is_dir()]
    print(f"Found {len(repos)} repositories in staging for analysis.")
    
    analyzed = []
    for r in repos:
        print(f"Analyzing {r.name}...")
        try:
            data = analyze_repo(r)
            
            # Generate Knowledge Doc
            doc = f"# OmniClaw Knowledge Report: {data['name']}\n\n"
            doc += f"## Tech Stack\n{', '.join(data['tech_stack']) if data['tech_stack'] else 'Unknown'}\n\n"
            doc += f"## File Statistics\n```json\n{json.dumps(data['files_stats'], indent=2)}\n```\n\n"
            doc += f"## README Snippet\n```markdown\n{data['readme_snippet']}\n```\n\n"
            doc += f"**Processed by OmniClaw Automated Intake**"
            
            out_file = PROCESSED_DIR / f"{data['name']}_knowledge.md"
            out_file.write_text(doc, encoding='utf-8')
            analyzed.append(data['name'])
            
            # Move to ARCHIVE after successful analysis
            archive_dir = ROOT / "storage" / "vault" / "ARCHIVE" / data['name']
            if archive_dir.exists():
                shutil.rmtree(archive_dir) # Remove if already exists to overwrite
            shutil.move(str(r), str(archive_dir))
            
            # Khôi phục Symlink Junction để AI và user ở vị trí cũ vẫn thao tác bình thường
            try:
                subprocess.run(f'cmd /c mklink /J "{r}" "{archive_dir}"', shell=True, check=True, stdout=subprocess.DEVNULL)
            except Exception as e:
                print(f"Lỗi tạo Symlink cho {data['name']}: {e}")
            
        except Exception as e:
            print(f"Error analyzing {r.name}: {e}")
            
    print(f"Analysis complete. {len(analyzed)} repositories processed to {PROCESSED_DIR}.")

if __name__ == "__main__":
    main()
