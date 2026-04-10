---
description: New developer onboarding – environment setup, project orientation, and first contribution
---

# Setup Workflow (Onboarding)

## Steps

1. **Clone the repository**
```bash
git clone https://github.com/tang-vu/ContribAI.git
cd ContribAI
```

2. **Verify Python version**
// turbo
```bash
python --version
```
Requires Python 3.11+.

3. **Create virtual environment**
```bash
python -m venv .venv
```

4. **Activate virtual environment**
```bash
# Windows PowerShell
.venv\Scripts\Activate.ps1

# macOS/Linux
source .venv/bin/activate
```

5. **Install with dev dependencies**
```bash
pip install -e ".[dev]"
```

6. **Verify installation**
// turbo
```bash
contribai --help
```

7. **Set up configuration**
```bash
cp config.example.yaml config.yaml
```
Edit `config.yaml` and add:
- GitHub Personal Access Token (with `repo`, `read:org` scopes)
- Gemini API key (from https://aistudio.google.com/app/apikey)

8. **Verify configuration**
// turbo
```bash
contribai config
```

9. **Run tests to verify setup**
// turbo
```bash
pytest tests/ -v --tb=short
```

10. **Read the project docs**
Key files to read:
- `README.md` – Project overview
- `CONTRIBUTING.md` – How to contribute
- `.agents/agents/` – Team roles and responsibilities
- `.agents/workflows/` – Development workflows

11. **Explore the codebase**
// turbo
```bash
python -c "
import pathlib
for p in sorted(pathlib.Path('contribai').rglob('*.py')):
    lines = len(p.read_text().splitlines())
    print(f'  {str(p):50s} {lines:>4d} lines')
"
```

12. **Try a dry run**
```bash
contribai analyze https://github.com/some-small-public-repo
```

13. **Make your first contribution**
Follow the `/dev` workflow to make a small improvement.
