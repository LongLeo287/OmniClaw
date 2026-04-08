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
cargo test --manifest-path crates/contribai-rs/Cargo.toml
```

3. **Update version number**
Update `version` in `crates/contribai-rs/Cargo.toml`:
```toml
[package]
name = "contribai"
version = "X.Y.Z"
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
git commit -m "release: vX.Y.Z — short description"
```

6. **Create git tag**
```bash
git tag -a vX.Y.Z -m "Release vX.Y.Z"
```

7. **Push to remote**
```bash
git push origin main --tags
```

8. **Build release binary**
// turbo
```bash
cargo build --manifest-path crates/contribai-rs/Cargo.toml --release
```

9. **Create GitHub Release** (triggers CI auto-build)
```bash
gh release create vX.Y.Z --title "vX.Y.Z - Release Title" --generate-notes --latest
```
> GitHub Actions `release.yml` cross-compiles the binary for Linux/macOS/Windows and
> attaches the artifacts to the release. No PyPI — distribution is a single static binary.

10. **Update release notes** (if auto-generated notes are insufficient)
```bash
gh release edit vX.Y.Z --notes-file /tmp/release_notes.md
```
> **Tip**: On Windows/PowerShell, avoid inline `--notes "..."` with backticks — it hangs. Use `--notes-file` or heredoc in bash.

## Version Numbering (SemVer)
- **MAJOR** (X): Breaking changes to CLI interface, config format, or DB schema
- **MINOR** (Y): New features, new analyzers, new CLI commands
- **PATCH** (Z): Bug fixes, documentation improvements
