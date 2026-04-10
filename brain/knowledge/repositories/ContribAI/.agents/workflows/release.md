---
description: Release workflow – version bump, changelog, tag, build, and publish
---

# Release Workflow

## Steps

1. **Ensure main is clean**
// turbo
```bash
git checkout main
git pull origin main
git status
```

2. **Run full test suite**
// turbo
```bash
pytest tests/ -v --cov=contribai --cov-report=term-missing
```

3. **Update version number**
Update version in `contribai/__init__.py` and `pyproject.toml`:
```python
# contribai/__init__.py
__version__ = "X.Y.Z"
```

4. **Update CHANGELOG.md**
Move items from `[Unreleased]` to the new version section:
```markdown
## [X.Y.Z] - YYYY-MM-DD
### Added
- ...
### Fixed
- ...
### Changed
- ...
```

5. **Commit release changes**
```bash
git add -A
git commit -m "chore: release vX.Y.Z"
```

6. **Create git tag**
```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z"
```

7. **Push to remote**
```bash
git push origin main --tags
```

8. **Build the package**
// turbo
```bash
python -m build
```

9. **Verify the build**
// turbo
```bash
python -m twine check dist/*
```

10. **Publish to PyPI** (manual approval required)
```bash
python -m twine upload dist/*
```

11. **Create GitHub Release**
```bash
# Write release notes to a temp file first (inline --notes hangs in PowerShell)
# Extract this version's section from CHANGELOG.md into a file, then:
gh release create vX.Y.Z --title "vX.Y.Z - Release Title" --notes-file /tmp/release_notes.md --latest
```
> **Tip**: Never use inline `--notes "..."` with backticks on Windows/PowerShell — it hangs. Always use `--notes-file`.

Mark this as the `--latest` release. Ensure title and notes match CHANGELOG.md content.

## Version Numbering (SemVer)
- **MAJOR** (X): Breaking changes to CLI or config format
- **MINOR** (Y): New features, new analyzers, new commands
- **PATCH** (Z): Bug fixes, documentation improvements
