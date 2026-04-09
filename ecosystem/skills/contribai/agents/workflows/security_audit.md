---
description: Security audit workflow – scan for vulnerabilities, review dependencies, check for secrets
---

# Security Audit Workflow

## Steps

1. **Check for hardcoded secrets**
// turbo
```bash
rg -i "password\s*=|secret\s*=|api_key\s*=|token\s*=" \
  crates/contribai-rs/src/ \
  --glob "*.rs" \
  --no-heading
```
Also check for raw string literals that look like tokens:
```bash
rg "ghp_[A-Za-z0-9]{36}|AIza[A-Za-z0-9_-]{35}" \
  crates/contribai-rs/src/ --glob "*.rs"
```

2. **Check dependencies for known vulnerabilities**
```bash
cargo audit --manifest-path crates/contribai-rs/Cargo.toml
```

3. **Run clippy security lints**
// turbo
```bash
cargo clippy --manifest-path crates/contribai-rs/Cargo.toml -- -D warnings \
  -W clippy::unwrap_used \
  -W clippy::expect_used \
  -W clippy::panic
```

4. **Review security-sensitive files**
Manually inspect these critical files:
- `crates/contribai-rs/src/core/config.rs` – Token/key handling
- `crates/contribai-rs/src/github/client.rs` – API authentication
- `crates/contribai-rs/src/llm/provider.rs` – API key handling
- `crates/contribai-rs/src/pr/manager.rs` – Git operations
- `crates/contribai-rs/src/analysis/analyzer.rs` – LLM output parsing

5. **Check for unsafe deserialization**
// turbo
```bash
# Check for unsafe serde usage or raw eval-equivalent patterns
rg "from_str_unchecked|unsafe\s*\{" \
  crates/contribai-rs/src/ --glob "*.rs"
```

6. **Check .gitignore covers sensitive files**
// turbo
```bash
for f in "config.yaml" ".env" "*.db" "*.sqlite"; do
  grep -q "$f" .gitignore \
    && echo "OK: $f" \
    || echo "MISSING: $f"
done
```

7. **Verify LLM output sanitization**
Check that all LLM responses are treated as untrusted:
- JSON parsing uses `serde_json::from_str` inside a `match` or `?` — no `unwrap()`
- No `std::process::Command` constructed from raw LLM output
- File paths from LLM are validated before use
- No `unsafe` blocks in LLM response handling

8. **Create security report**
Document findings in `docs/security-audit-YYYY-MM-DD.md`

9. **Fix critical issues immediately**
Any critical finding should be fixed on a `fix/security-*` branch with priority review.
