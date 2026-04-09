---
description: Debugging workflow – systematic approach to finding and fixing bugs
---

# Debug Workflow

## Steps

1. **Reproduce the issue**
Run the failing command with verbose logging:
```bash
RUST_LOG=debug contribai <command>
```

2. **Check the error output**
Read the full error message and backtrace. Identify:
- Which module emitted the error
- The error variant (from `crates/contribai-rs/src/core/error.rs`)
- The root cause vs. symptom

3. **Enable debug logging**
// turbo
```bash
RUST_LOG=contribai=debug,contribai::github=trace contribai <command>
```
Use `RUST_BACKTRACE=1` for full panic backtraces:
```bash
RUST_BACKTRACE=1 RUST_LOG=debug contribai <command>
```

4. **Run specific test in debug mode**
// turbo
```bash
cargo test --manifest-path crates/contribai-rs/Cargo.toml test_name -- --nocapture
```

5. **Common debugging patterns**

### GitHub API issues
```bash
# Check rate limit via CLI
contribai status

# Or inspect with curl
curl -H "Authorization: Bearer $CONTRIBAI_GITHUB_TOKEN" \
  https://api.github.com/rate_limit
```

### LLM issues
```bash
# Test LLM config directly
RUST_LOG=contribai::llm=debug contribai analyze https://github.com/some-repo --dry-run
```

### Memory/DB issues
```bash
# Inspect SQLite DB directly
sqlite3 ~/.contribai/memory.db ".tables"
sqlite3 ~/.contribai/memory.db "SELECT COUNT(*) FROM pull_requests;"
sqlite3 ~/.contribai/memory.db "SELECT * FROM pull_requests ORDER BY created_at DESC LIMIT 5;"
```

6. **Fix the bug**
- Create a `fix/` branch
- Write a failing test first (TDD)
- Implement the fix
- Verify the test passes

7. **Verify no regressions**
// turbo
```bash
cargo test --manifest-path crates/contribai-rs/Cargo.toml
```

8. **Commit the fix**
```bash
git add -A
git commit -m "fix(<module>): <description of fix>"
```

## Common Issues & Solutions

| Symptom | Likely Cause | Solution |
|---------|-------------|----------|
| `RateLimitError` | GitHub API quota exceeded | Wait for reset, reduce `max_repos_per_run` |
| `LlmRateLimitError` | LLM API quota exceeded | Switch provider, wait, or reduce requests |
| `ConfigError` | Invalid config.yaml | Check YAML syntax, compare with `config.example.yaml` |
| `GitHubApiError(404)` | Repo not found or private | Verify URL, check token permissions |
| `LlmError` | API key invalid or wrong model | Verify API key and model name in config |
