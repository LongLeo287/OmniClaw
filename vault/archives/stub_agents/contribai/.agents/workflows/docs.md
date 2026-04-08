---
description: Documentation workflow – create, update and verify project documentation
---

# Documentation Workflow

## Steps

1. **Review current docs**
// turbo
```bash
find . -name "*.md" -not -path "./.git/*" | sort | while read f; do
  printf "  %-60s %6d bytes\n" "$f" "$(wc -c < "$f")"
done
```

2. **Check doc comment coverage**
// turbo
```bash
# Build docs and surface warnings about missing /// comments on public items
cargo doc --manifest-path crates/contribai-rs/Cargo.toml --no-deps 2>&1 | grep "warning"
```
Target: no `missing_docs` warnings on public structs, enums, and functions.

3. **Update README.md**
Ensure these sections are present and current:
- Project description & badges
- Features list
- Installation instructions (cargo build --release)
- Configuration guide
- Usage examples (all 13 CLI commands)
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
- Development setup (rustup, cargo build)
- Code standards (cargo fmt, cargo clippy)
- Testing requirements (cargo test, 323 tests)
- PR process
- Agent roles

6. **Add missing doc comments**
Use Rust `///` doc comment format on all public items:
```rust
/// Short one-line description.
///
/// Longer explanation if needed.
///
/// # Arguments
///
/// * `param` - Description of the parameter.
///
/// # Returns
///
/// `true` if condition met.
///
/// # Errors
///
/// Returns [`Error::Config`] if the input is empty.
pub fn function_name(param: &str) -> Result<bool, Error> {
    // ...
}
```

7. **Generate and open API docs**
// turbo
```bash
cargo doc --manifest-path crates/contribai-rs/Cargo.toml --no-deps --open
```

8. **Check for broken links**
Manually verify any URLs in README and docs.

9. **Commit documentation changes**
```bash
git add -A
git commit -m "docs: update documentation"
```
