---
id: trailofbits-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:22.914732
---

# KNOWLEDGE EXTRACT: trailofbits
> **Extracted on:** 2026-03-30 17:54:20
> **Source:** trailofbits

---

## File: `skills.md`
```markdown
# 📦 trailofbits/skills [🔖 PENDING/APPROVE]
🔗 https://github.com/trailofbits/skills


## Meta
- **Stars:** ⭐ 3974 | **Forks:** 🍴 338
- **Language:** Python | **License:** CC-BY-SA-4.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Trail of Bits Claude Code skills for security research, vulnerability detection, and audit workflows

## README (trích đầu)
```
# Trail of Bits Skills Marketplace

A Claude Code plugin marketplace from Trail of Bits providing skills to enhance AI-assisted security analysis, testing, and development workflows.

> Also see: [claude-code-config](https://github.com/trailofbits/claude-code-config) · [skills-curated](https://github.com/trailofbits/skills-curated) · [claude-code-devcontainer](https://github.com/trailofbits/claude-code-devcontainer) · [dropkit](https://github.com/trailofbits/dropkit)

## Installation

### Claude Code Marketplace

```
/plugin marketplace add trailofbits/skills
```

### Browse and Install Plugins

```
/plugin menu
```

### Codex

Codex-native skill discovery is supported via the sidecar `.codex/skills/` tree in this repository.

Install with:

```sh
git clone https://github.com/trailofbits/skills.git ~/.codex/trailofbits-skills
~/.codex/trailofbits-skills/.codex/scripts/install-for-codex.sh
```

See [`.codex/INSTALL.md`](.codex/INSTALL.md) for additional details.

### Local Development

To add the marketplace locally (e.g., for testing or development), navigate to the **parent directory** of this repository:

```
cd /path/to/parent  # e.g., if repo is at ~/projects/skills, be in ~/projects
/plugins marketplace add ./skills
```

## Available Plugins

### Smart Contract Security

| Plugin | Description |
|--------|-------------|
| [building-secure-contracts](plugins/building-secure-contracts/) | Smart contract security toolkit with vulnerability scanners for 6 blockchains |
| [entry-point-analyzer](plugins/entry-point-analyzer/) | Identify state-changing entry points in smart contracts for security auditing |

### Code Auditing

| Plugin | Description |
|--------|-------------|
| [agentic-actions-auditor](plugins/agentic-actions-auditor/) | Audit GitHub Actions workflows for AI agent security vulnerabilities |
| [audit-context-building](plugins/audit-context-building/) | Build deep architectural context through ultra-granular code analysis |
| [burpsuite-project-parser](plugins/burpsuite-project-parser/) | Search and extract data from Burp Suite project files |
| [differential-review](plugins/differential-review/) | Security-focused differential review of code changes with git history analysis |
| [dimensional-analysis](plugins/dimensional-analysis/) | Annotate codebases with dimensional analysis comments to detect unit mismatches and formula bugs |
| [fp-check](plugins/fp-check/) | Systematic false positive verification for security bug analysis with mandatory gate reviews |
| [insecure-defaults](plugins/insecure-defaults/) | Detect insecure default configurations, hardcoded credentials, and fail-open security patterns |
| [semgrep-rule-creator](plugins/semgrep-rule-creator/) | Create and refine Semgrep rules for custom vulnerability detection |
| [semgrep-rule-variant-creator](plugins/semgrep-rule-variant-creator/) | Port existing Semgrep rules to new target languages with test-driven validation |
| [sharp-edges](plugins/sharp-edges/) | Identify er
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

