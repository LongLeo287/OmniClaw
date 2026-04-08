---
description: Documentation workflow – create, update and verify project documentation
---

# Documentation Workflow

## Steps

1. **Review current docs**
// turbo
```bash
python -c "import pathlib; docs = list(pathlib.Path('.').rglob('*.md')); print('Documentation files:'); [print(f'  {d} ({d.stat().st_size} bytes)') for d in sorted(docs) if '.git' not in str(d)]"
```

2. **Check docstring coverage**
// turbo
```bash
python -c "
import pathlib, ast, sys
total = covered = 0
for f in pathlib.Path('contribai').rglob('*.py'):
    try:
        tree = ast.parse(f.read_text())
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                if node.name.startswith('_'): continue
                total += 1
                if ast.get_docstring(node): covered += 1
    except: pass
pct = (covered/total*100) if total else 0
print(f'Docstring coverage: {covered}/{total} ({pct:.0f}%)')
"
```

3. **Update README.md**
Ensure these sections are present and current:
- Project description & badges
- Features list
- Installation instructions
- Configuration guide
- Usage examples (all CLI commands)
- Project structure
- Development setup
- License

4. **Update CHANGELOG.md**
Add entries for any changes since last update:
```markdown
## [Unreleased]
### Added
### Fixed
### Changed
### Removed
```

5. **Update CONTRIBUTING.md**
Verify it covers:
- Development setup
- Code standards
- Testing requirements
- PR process
- Agent roles

6. **Add missing docstrings**
Use Google-style format:
```python
def function_name(param: str) -> bool:
    """Short description.

    Args:
        param: Description of param.

    Returns:
        True if condition met.

    Raises:
        ValueError: If param is empty.
    """
```

7. **Verify code examples work**
// turbo
```bash
python -c "print('contribai package importable:', end=' '); exec('from contribai import __version__; print(__version__)')"
```

8. **Check for broken links**
Manually verify any URLs in README and docs.

9. **Commit documentation changes**
```bash
git add -A
git commit -m "docs: update documentation"
```
