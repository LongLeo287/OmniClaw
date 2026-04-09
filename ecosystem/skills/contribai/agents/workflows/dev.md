---
description: ContribAI development workflow - code, patrol, hunt, and release
---

# ContribAI Development Workflow

// turbo-all

## Code Changes

1. Make changes to the relevant files in `crates/contribai-rs/src/`
2. Run formatting and linting:
   ```bash
   cargo fmt --manifest-path crates/contribai-rs/Cargo.toml
   cargo clippy --manifest-path crates/contribai-rs/Cargo.toml -- -D warnings
   ```
3. Run tests:
   ```bash
   cargo test --manifest-path crates/contribai-rs/Cargo.toml
   ```
4. Commit with conventional commits + DCO signoff:
   ```bash
   git add -A && git commit -s -m "feat|fix|refactor: description"
   ```
5. Push and verify CI:
   ```bash
   git push origin main
   ```

## Architecture (v5.0.0)

Key modules to know:

| Module | Purpose |
|--------|---------|
| `core/middleware.rs` | Pipeline middleware chain (RateLimit, Validation, Retry, DCO, QualityGate) |
| `core/events.rs` | EventBus with 15 typed events + JSONL logging |
| `analysis/skills.rs` | 17 progressive analysis skills + framework detection |
| `agents/registry.rs` | Sub-agent registry (Analyzer, Generator, Patrol, Compliance) |
| `tools/mod.rs` | Tool protocol (GitHubTool, LLMTool) |
| `orchestrator/memory.rs` | rusqlite persistence + outcome learning (7 tables) |
| `analysis/analyzer.rs` | Code analysis + context compression |
| `mcp/server.rs` | MCP stdio server (21 tools for Claude Desktop) |
| `mcp/client.rs` | MCP client for external tool servers |
| `sandbox/mod.rs` | Docker-based code validation with local fallback |

## PR Patrol

Run patrol to monitor and respond to PR review feedback:

```bash
# Dry run (no changes)
contribai patrol --dry-run

# Target specific PR
contribai patrol --pr <PR_NUMBER>

# Live run (responds to feedback)
contribai patrol
```

### Key files:
- `crates/contribai-rs/src/pr/patrol.rs` - Patrol engine
- `crates/contribai-rs/src/core/models.rs` - FeedbackItem, PatrolResult, FeedbackAction
- `crates/contribai-rs/src/github/client.rs` - GitHub API (create_or_update_file, get_assigned_issues)
- `crates/contribai-rs/src/cli/mod.rs` - CLI patrol command

### DCO Signoff
All commits via GitHub API automatically include `Signed-off-by:` trailer.
Configured via `github.dco_signoff: true` in `config.yaml`.

**IMPORTANT**: When fixing DCO on existing PRs, do NOT use `git rebase --signoff` on branches
with merge commits — it flattens the history. Instead:
```bash
# Safe approach: reset to upstream and reapply
git fetch upstream
git reset --hard upstream/master
# Apply changes manually
git commit -s -m "fix: description"
git push --force-with-lease origin <branch>
```

### Bot Review Context
When a maintainer replies to a bot review (Coderabbit, etc.), patrol reads the bot's
original analysis via `in_reply_to_id` and passes it as context to the LLM for
generating accurate code fixes.

## Hunt Mode

```bash
# Hunt for repos and generate PRs
contribai hunt --rounds 1

# Hunt with multiple languages
contribai hunt --rounds 3 -l python -l javascript

# Dry run
contribai hunt --rounds 1 --dry-run

# Single repo test
contribai run owner/repo --dry-run
```

## Release

1. Bump version in `crates/contribai-rs/Cargo.toml`
2. Update `CHANGELOG.md` with new version section
3. Update `README.md` badges (version, test count)
4. Update `AGENTS.md` if architecture changed
5. Commit and push:
   ```bash
   git add -A && git commit -s -m "feat: release vX.Y.Z"
   git push origin main
   ```
6. Create release:
   ```bash
   gh release create v<VERSION> --repo tang-vu/ContribAI --title "v<VERSION> - Title" --generate-notes
   ```
7. Verify all CI checks pass

## Config Reference

Key config fields in `config.yaml`:

```yaml
github:
  dco_signoff: true          # Auto Signed-off-by (default: true)
  max_repos_per_run: 5
  max_prs_per_day: 10

llm:
  provider: gemini
  model: gemini-2.5-flash

analysis:
  enabled_analyzers:         # Only load needed analyzers
    - security
    - code_quality
    - performance

contribution:
  commit_convention: conventional
```
