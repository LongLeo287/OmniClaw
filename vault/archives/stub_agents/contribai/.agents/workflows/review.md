---
description: Code review workflow – systematic PR review process following the Code Reviewer agent standards
---

# Code Review Workflow

## Steps

1. **Read PR description and linked issue**
Understand the context: what problem is being solved and why.

2. **Check CI status**
// turbo
```bash
git fetch origin
git log origin/main..HEAD --oneline
```
CI must be green before review starts.

3. **Pull the PR branch locally**
```bash
git fetch origin <branch-name>
git checkout <branch-name>
```

4. **Run tests locally**
// turbo
```bash
cargo test --manifest-path crates/contribai-rs/Cargo.toml
```

5. **Run lint check**
// turbo
```bash
cargo clippy --manifest-path crates/contribai-rs/Cargo.toml -- -D warnings
```

6. **Review code changes**
Go through the Code Reviewer checklist:
- [ ] Functionality: code does what PR says, edge cases handled
- [ ] Architecture: correct module, no circular dependencies
- [ ] Code quality: functions < 50 lines, files < 200 lines, no duplication
- [ ] Documentation: `///` doc comments on public items, README updated if needed
- [ ] Testing: new code has `#[test]` / `#[tokio::test]` coverage, edge cases covered
- [ ] Security: no secrets, inputs validated, LLM output untrusted
- [ ] Performance: no blocking calls in async context, no unnecessary clones

7. **Check for breaking changes**
Review `crates/contribai-rs/src/core/models.rs` and `crates/contribai-rs/src/core/config.rs`
for any struct/enum changes that could break existing configs or serialized data.

8. **Leave review comments**
Use severity labels:
- `nit:` – Style preference, non-blocking
- `suggestion:` – Improvement idea, non-blocking
- `issue:` – Must fix before merge
- `question:` – Need clarification
- `blocker:` – Critical, blocks merge

9. **Write summary comment**
Overall assessment of the PR quality and any blocking issues.

10. **Approve or request changes**
- **Approve**: All checks pass, code is clean
- **Request Changes**: Has blocking issues
- **Comment**: Non-blocking suggestions only
