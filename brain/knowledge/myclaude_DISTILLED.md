---
id: myclaude
type: knowledge
owner: OA_Triage
---
# myclaude
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: package.json
```json
{
  "name": "myclaude",
  "version": "6.7.0",
  "private": true,
  "description": "Claude Code multi-agent workflows (npx installer)",
  "license": "AGPL-3.0",
  "bin": {
    "myclaude": "bin/cli.js"
  },
  "files": [
    "bin/",
    ".claude-plugin/",
    "agents/",
    "skills/",
    "memorys/",
    "templates/",
    "codeagent-wrapper/",
    "config.json",
    "install.py",
    "install.sh",
    "install.bat",
    "PLUGIN_README.md",
    "README.md",
    "README_CN.md",
    "LICENSE"
  ]
}

```

### File: README.md
```md
[中文](README_CN.md) [English](README.md)

# Claude Code Multi-Agent Workflow System

[![Run in Smithery](https://smithery.ai/badge/skills/stellarlinkco)](https://smithery.ai/skills?ns=stellarlinkco&utm_source=github&utm_medium=badge)
[![License: AGPL-3.0](https://img.shields.io/badge/License-AGPL_v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)
[![Claude Code](https://img.shields.io/badge/Claude-Code-blue)](https://claude.ai/code)
[![Version](https://img.shields.io/badge/Version-6.x-green)](https://github.com/stellarlinkco/myclaude)

> AI-powered development automation with multi-backend execution (Codex/Claude/Gemini/OpenCode)

## Quick Start

```bash
npx github:stellarlinkco/myclaude
```

## Modules Overview

| Module | Description | Documentation |
|--------|-------------|---------------|
| [do](skills/do/README.md) | **Recommended** - 5-phase feature development with codeagent orchestration | `/do` command |
| [omo](skills/omo/README.md) | Multi-agent orchestration with intelligent routing | `/omo` command |
| [bmad](agents/bmad/README.md) | BMAD agile workflow with 6 specialized agents | `/bmad-pilot` command |
| [requirements](agents/requirements/README.md) | Lightweight requirements-to-code pipeline | `/requirements-pilot` command |
| [essentials](agents/development-essentials/README.md) | 11 core dev commands: ask, bugfix, code, debug, docs, enhance-prompt, optimize, refactor, review, test, think | `/code`, `/debug`, etc. |
| [sparv](skills/sparv/README.md) | SPARV workflow (Specify→Plan→Act→Review→Vault) | `/sparv` command |
| course | Course development (combines dev + product-requirements + test-cases) | Composite module |
| claudekit | ClaudeKit: do skill + global hooks (pre-bash, inject-spec, log-prompt) | Composite module |

### Available Skills

Individual skills can be installed separately via `npx github:stellarlinkco/myclaude --list` (skills bundled in modules like do, omo, sparv are listed above):

| Skill | Description |
|-------|-------------|
| browser | Browser automation for web testing and data extraction |
| codeagent | codeagent-wrapper invocation for multi-backend AI code tasks |
| codex | Direct Codex backend execution |
| dev | Lightweight end-to-end development workflow |
| gemini | Direct Gemini backend execution |
| product-requirements | Interactive PRD generation with quality scoring |
| prototype-prompt-generator | Structured UI/UX prototype prompt generation |
| skill-install | Install skills from GitHub with security scanning |
| test-cases | Comprehensive test case generation from requirements |

## Installation

```bash
# Interactive installer (recommended)
npx github:stellarlinkco/myclaude

# List installable items (modules / skills / wrapper)
npx github:stellarlinkco/myclaude --list

# Detect installed modules and update from GitHub
npx github:stellarlinkco/myclaude --update

# Custom install directory / overwrite
npx github:stellarlinkco/myclaude --install-dir ~/.claude --force
```

`--update` detects already installed modules in the target install dir (defaults to `~/.claude`, via `installed_modules.json` when present) and updates them from GitHub (latest release) by overwriting the module files.

### Module Configuration

Edit `config.json` to enable/disable modules:

```json
{
  "modules": {
    "bmad": { "enabled": false },
    "requirements": { "enabled": false },
    "essentials": { "enabled": false },
    "omo": { "enabled": false },
    "sparv": { "enabled": false },
    "do": { "enabled": true },
    "course": { "enabled": false }
  }
}
```

## Workflow Selection Guide

| Scenario | Recommended |
|----------|-------------|
| Feature development (default) | `/do` |
| Bug investigation + fix | `/omo` |
| Large enterprise project | `/bmad-pilot` |
| Quick prototype | `/requirements-pilot` |
| Simple task | `/code`, `/debug` |

## Core Architecture

| Role | Agent | Responsibility |
|------|-------|----------------|
| **Orchestrator** | Claude Code | Planning, context gathering, verification |
| **Executor** | codeagent-wrapper | Code editing, test execution (Codex/Claude/Gemini/OpenCode) |

## Backend CLI Requirements

| Backend | Required Features |
|---------|-------------------|
| Codex | `codex e`, `--json`, `-C`, `resume` |
| Claude | `--output-format stream-json`, `-r` |
| Gemini | `-o stream-json`, `-y`, `-r` |
| OpenCode | `opencode`, stdin mode |

## Directory Structure After Installation

```
~/.claude/
├── bin/codeagent-wrapper
├── CLAUDE.md              (installed by default)
├── commands/              (from essentials module)
├── agents/                (from bmad/requirements modules)
├── skills/                (from do/omo/sparv/course modules)
├── hooks/                 (from claudekit module)
├── settings.json          (auto-generated, hooks config)
└── installed_modules.json (auto-generated, tracks modules)
```

## Documentation

- [codeagent-wrapper](codeagent-wrapper/README.md)
- [Plugin System](PLUGIN_README.md)

## Troubleshooting

### Common Issues

**Codex wrapper not found:**
```bash
# Select: codeagent-wrapper
npx github:stellarlinkco/myclaude
```

**Module not loading:**
```bash
cat ~/.claude/installed_modules.json
npx github:stellarlinkco/myclaude --force
```

**Backend CLI errors:**
```bash
which codex && codex --version
which claude && claude --version
which gemini && gemini --version
```

## FAQ

| Issue | Solution |
|-------|----------|
| "Unknown event format" | Logging display issue, can be ignored |
| Gemini can't read .gitignore files | Remove from .gitignore or use different backend |
| Codex permission denied | Set `approval_policy = "never"` in ~/.codex/config.yaml |

See [GitHub Issues](https://github.com/stellarlinkco/myclaude/issues) for more.

## License

AGPL-3.0 - see [LICENSE](LICENSE)

### Commercial Licensing

For commercial use without AGPL obligations, contact: support@stellarlink.co

## Support

- [GitHub Issues](https://github.com/stellarlinkco/myclaude/issues)

```

### File: skills\README.md
```md
# Skills

This directory contains agent skills (each skill lives in its own folder with a `SKILL.md`).

## Install with `npx` (recommended)

List installable items:

```bash
npx github:stellarlinkco/myclaude --list
```

Install (interactive; pick `skill:<name>`):

```bash
npx github:stellarlinkco/myclaude
```

Force overwrite / custom install directory:

```bash
npx github:stellarlinkco/myclaude --install-dir ~/.claude --force
```

```

### File: skills\browser\package.json
```json
{
  "dependencies": {
    "ws": "^8.18.3"
  }
}

```

### File: CHANGELOG.md
```md
# Changelog

All notable changes to this project will be documented in this file.

## [6.7.0] - 2026-02-10

### 🚀 Features

- feat(install): per-module agent merge/unmerge for ~/.codeagent/models.json
- feat(install): post-install verification (wrapper version, PATH, backend CLIs)
- feat(install): install CLAUDE.md by default
- feat(docs): document 9 skills, 11 commands, claudekit module, OpenCode backend

### 🐛 Bug Fixes

- fix(docs): correct 7-phase → 5-phase for do skill across all docs
- fix(install): best-effort default config install (never crashes main flow)
- fix(install): interactive quit no longer triggers post-install actions
- fix(install): empty parent directory cleanup on copy_file uninstall
- fix(install): agent restore on uninstall when shared by multiple modules
- fix(docs): remove non-existent on-stop hook references

### 📚 Documentation

- Updated USER_GUIDE.md with 13 CLI flags and OpenCode backend
- Updated README.md/README_CN.md with complete module and skill listings
- Added templates/models.json.example with all agent presets (do + omo)

## [6.6.0] - 2026-02-10

### 🚀 Features

- feat(skills): add per-task skill spec auto-detection and injection
- feat: add worktree support and refactor do skill to Python

### 🐛 Bug Fixes

- fix(test): set USERPROFILE on Windows for skills tests
- fix(do): reuse worktree across phases via DO_WORKTREE_DIR env var
- fix(release): auto-generate release notes from git history

### 📚 Documentation

- audit and fix documentation, installation scripts, and default configuration

## [6.0.0] - 2026-01-26

### 🚀 Features

- support `npx github:stellarlinkco/myclaude` for installation and execution
- default module changed from `dev` to `do`

### 🚜 Refactor

- restructure: create `agents/` and move `bmad-agile-workflow` → `agents/bmad`, `requirements-driven-workflow` → `agents/requirements`, `development-essentials` → `agents/development-essentials`
- remove legacy directories: `docs/`, `hooks/`, `dev-workflow/`
- update references across `config.json`, `README.md`, `README_CN.md`, `marketplace.json`, etc.

### 📚 Documentation

- add `skills/README.md` and `PLUGIN_README.md`

### 💼 Other

- add `package.json` and `bin/cli.js` for npx packaging

## [6.1.5] - 2026-01-25


### 🐛 Bug Fixes


- correct gitignore to not exclude cmd/codeagent-wrapper

## [6.1.4] - 2026-01-25


### 🐛 Bug Fixes


- support concurrent tasks with unique state files

## [6.1.3] - 2026-01-25


### 🐛 Bug Fixes


- correct build path in release workflow

- increase stdoutDrainTimeout from 100ms to 500ms

## [6.1.2] - 2026-01-24


### 🐛 Bug Fixes


- use ANTHROPIC_AUTH_TOKEN for Claude CLI env injection

### 💼 Other


- update codeagent version

### 📚 Documentation


- restructure root READMEs with do as recommended workflow

- update do/omo/sparv module READMEs with detailed workflows

- add README for bmad and requirements modules

### 🧪 Testing


- use prefix match for version flag tests

## [6.1.1] - 2026-01-23


### 🚜 Refactor


- rename feature-dev to do workflow

## [6.1.0] - 2026-01-23


### ⚙️ Miscellaneous Tasks


- ignore references directory

- add go.work.sum for workspace dependencies

### 🐛 Bug Fixes


- read GEMINI_MODEL from ~/.gemini/.env ([#131](https://github.com/stellarlinkco/myclaude/issues/131))

- validate non-empty output message before printing

### 🚀 Features


- add feature-dev skill with 7-phase workflow

- support \${CLAUDE_PLUGIN_ROOT} variable in hooks config

## [6.0.0-alpha1] - 2026-01-20


### 🐛 Bug Fixes


- add missing cmd/codeagent/main.go entry point

- update release workflow build path for new directory structure

- write PATH config to both profile and rc files ([#128](https://github.com/stellarlinkco/myclaude/issues/128))

### 🚀 Features


- add course module with dev, product-requirements and test-cases skills

- add hooks management to install.py

### 🚜 Refactor


- restructure codebase to internal/ directory with modular architecture

## [5.6.7] - 2026-01-17


### 💼 Other


- remove .sparv

### 📚 Documentation


- update 'Agent Hierarchy' model for frontend-ui-ux-engineer and document-writer in README ([#127](https://github.com/stellarlinkco/myclaude/issues/127))

- update mappings for frontend-ui-ux-engineer and document-writer in README ([#126](https://github.com/stellarlinkco/myclaude/issues/126))

### 🚀 Features


- add sparv module and interactive plugin manager

- add sparv enhanced rules v1.1

- add sparv skill to claude-plugin v1.1.0

- feat sparv skill

## [5.6.6] - 2026-01-16


### 🐛 Bug Fixes


- remove extraneous dash arg for opencode stdin mode ([#124](https://github.com/stellarlinkco/myclaude/issues/124))

### 💼 Other


- update readme

## [5.6.5] - 2026-01-16


### 🐛 Bug Fixes


- correct default models for oracle and librarian agents ([#120](https://github.com/stellarlinkco/myclaude/issues/120))

### 🚀 Features


- feat dev skill

## [5.6.4] - 2026-01-15


### 🐛 Bug Fixes


- filter codex 0.84.0 stderr noise logs ([#122](https://github.com/stellarlinkco/myclaude/issues/122))

- filter codex stderr noise logs

## [5.6.3] - 2026-01-14


### ⚙️ Miscellaneous Tasks


- bump codeagent-wrapper version to 5.6.3

### 🐛 Bug Fixes


- update version tests to match 5.6.3

- use config override for codex reasoning effort

## [5.6.2] - 2026-01-14


### 🐛 Bug Fixes


- propagate SkipPermissions to parallel tasks ([#113](https://github.com/stellarlinkco/myclaude/issues/113))

- add timeout for Windows process termination

- reject dash as workdir parameter ([#118](https://github.com/stellarlinkco/myclaude/issues/118))

### 📚 Documentation


- add OmO workflow to README and fix plugin marketplace structure

### 🚜 Refactor


- remove sisyphus agent and unused code

## [5.6.1] - 2026-01-13


### 🐛 Bug Fixes


- add sleep in fake script to prevent CI race condition

- fix gemini env load

- fix omo

### 🚀 Features


- add reasoning effort config for codex backend

## [5.6.0] - 2026-01-13


### 📚 Documentation


- update FAQ for default bypass/skip-permissions behavior

### 🚀 Features


- default to skip-permissions and bypass-sandbox

- add omo module for multi-agent orchestration

### 🚜 Refactor


- streamline agent documentation and remove sisyphus

## [5.5.0] - 2026-01-12


### 🐛 Bug Fixes


- 修复 Gemini init 事件 session_id 未提取的问题 ([#111](https://github.com/stellarlinkco/myclaude/issues/111))

- fix codeagent skill TaskOutput

### 💼 Other


- Merge branch 'master' of github.com:stellarlinkco/myclaude

- add test-cases skill

- add browser skill

### 🚀 Features


- add multi-agent support with yolo mode

## [5.4.4] - 2026-01-08


### 💼 Other


- 修复 Windows 后端退出：taskkill 结束进程树 + turn.completed 支持 ([#108](https://github.com/stellarlinkco/myclaude/issues/108))

## [5.4.3] - 2026-01-06


### 🐛 Bug Fixes


- support model parameter for all backends, auto-inject from settings ([#105](https://github.com/stellarlinkco/myclaude/issues/105))

### 📚 Documentation


- add FAQ Q5 for permission/sandbox env vars

### 🚀 Features


- feat skill-install install script and security scan

- add uninstall scripts with selective module removal

## [5.4.2] - 2025-12-31


### 🐛 Bug Fixes


- replace setx with reg add to avoid 1024-char PATH truncation ([#101](https://github.com/stellarlinkco/myclaude/issues/101))

## [5.4.1] - 2025-12-26


### 🐛 Bug Fixes


- 移除未知事件格式的日志噪声 ([#96](https://github.com/stellarlinkco/myclaude/issues/96))

- prevent duplicate PATH entries on reinstall ([#95](https://github.com/stellarlinkco/myclaude/issues/95))

### 📚 Documentation


- 添加 FAQ 常见问题章节

- update troubleshooting with idempotent PATH commands ([#95](https://github.com/stellarlinkco/myclaude/issues/95))

### 🚀 Features


- Add intelligent backend selection based on task complexity ([#61](https://github.com/stellarlinkco/myclaude/issues/61))

## [5.4.0] - 2025-12-24


### 🐛 Bug Fixes


- Minor issues #12 and #13 - ASCII mode and performance optimization

- code review fixes for PR #94 - all critical and major issues resolved

### 🚀 Features


- v5.4.0 structured execution report ([#94](https://github.com/stellarlinkco/myclaude/issues/94))

## [5.2.8] - 2025-12-22


### ⚙️ Miscellaneous Tasks


- simplify release workflow to use GitHub auto-generated notes

### 🐛 Bug Fixes


- correct settings.json filename and bump version to v5.2.8

## [5.2.7] - 2025-12-21


### ⚙️ Miscellaneous Tasks


- bump version to v5.2.7

### 🐛 Bug Fixes


- allow claude backend to read env from setting.json while preventing recursion ([#92](https://github.com/stellarlinkco/myclaude/issues/92))

- comprehensive security and quality improvements for PR #85 & #87 ([#90](https://github.com/stellarlinkco/myclaude/issues/90))

- Parser重复解析优化 + 严重bug修复 + PR #86兼容性 ([#88](https://github.com/stellarlinkco/myclaude/issues/88))

### 💼 Other


- Improve backend termination after message and extend timeout ([#86](https://github.com/stellarlinkco/myclaude/issues/86))

### 🚀 Features


- add millisecond-precision timestamps to all log entries ([#91](https://github.com/stellarlinkco/myclaude/issues/91))

## [5.2.6] - 2025-12-19


### 🐛 Bug Fixes


- filter noisy stderr output from gemini backend ([#83](https://github.com/stellarlinkco/myclaude/issues/83))

- 修復 wsl install.sh 格式問題 ([#78](https://github.com/stellarlinkco/myclaude/issues/78))

### 💼 Other


- update all readme

- BMADh和Requirements-Driven支持根据语义生成对应的文档 ([#82](https://github.com/stellarlinkco/myclaude/issues/82))

## [5.2.5] - 2025-12-17


### 🐛 Bug Fixes


- 修复多 backend 并行日志 PID 混乱并移除包装格式 ([#74](https://github.com/stellarlinkco/myclaude/issues/74)) ([#76](https://github.com/stellarlinkco/myclaude/issues/76))

- replace "Codex" to "codeagent" in dev-plan-generator subagent

- 修復 win python install.py

### 💼 Other


- Merge pull request #71 from aliceric27/master

- Merge branch 'stellarlinkco:master' into master

- Merge pull request #72 from changxvv/master

- update changelog

- update codeagent skill backend select

## [5.2.4] - 2025-12-16


### ⚙️ Miscellaneous Tasks


- integrate git-cliff for automated changelog generation

- bump version to 5.2.4

### 🐛 Bug Fixes


- 防止 Claude backend 无限递归调用

- isolate log files per task in parallel mode

### 💼 Other


- Merge pull request #70 from stellarlinkco/fix/prevent-codeagent-infinite-recursion

- Merge pull request #69 from stellarlinkco/myclaude-master-20251215-073053-338465000

- update CHANGELOG.md

- Merge pull request #65 from stellarlinkco/fix/issue-64-buffer-overflow

## [5.2.3] - 2025-12-15


### 🐛 Bug Fixes


- 修复 bufio.Scanner token too long 错误 ([#64](https://github.com/stellarlinkco/myclaude/issues/64))

### 💼 Other


- change version

### 🧪 Testing


- 同步测试中的版本号至 5.2.3

## [5.2.2] - 2025-12-13


### ⚙️ Miscellaneous Tasks


- Bump version and clean up documentation

### 🐛 Bug Fixes


- fix codeagent backend claude no auto

- fix install.py dev fail

### 🧪 Testing


- Fix tests for ClaudeBackend default --dangerously-skip-permissions

## [5.2.1] - 2025-12-13


### 🐛 Bug Fixes


- fix codeagent claude and gemini root dir

### 💼 Other


- update readme

## [5.2.0] - 2025-12-13


### ⚙️ Miscellaneous Tasks


- Update CHANGELOG and remove deprecated test files

### 🐛 Bug Fixes


- fix race condition in stdout parsing

- add worker limit cap and remove legacy alias

- use -r flag for gemini backend resume

- clarify module list shows default state not enabled

- use -r flag for claude backend resume

- remove binary artifacts and improve error messages

- 异常退出时显示最近错误信息

- op_run_command 实时流式输出

- 修复权限标志逻辑和版本号测试

- 重构信号处理逻辑避免重复 nil 检查

- 移除 .claude 配置文件验证步骤

- 修复并行执行启动横幅重复打印问题

- 修复master合并后的编译和测试问题

### 💼 Other


- Merge rc/5.2 into master: v5.2.0 release improvements

- Merge pull request #53 from stellarlinkco/rc/5.2

- remove docs

- remove docs

- add prototype prompt skill

- add prd skill

- update memory claude

- remove command gh flow

- update license

- Merge branch 'master' into rc/5.2

- Merge pull request #52 from stellarlinkco/fix/parallel-log-path-on-startup

### 📚 Documentation


- remove GitHub workflow related content

### 🚀 Features


- Complete skills system integration and config cleanup

- Improve release notes and installation scripts

- 添加终端日志输出和 verbose 模式

- 完整多后端支持与安全优化

- 替换 Codex 为 codeagent 并添加 UI 自动检测

### 🚜 Refactor


- 调整文件命名和技能定义

### 🧪 Testing


- 添加 ExtractRecentErrors 单元测试

## [5.1.4] - 2025-12-09


### 🐛 Bug Fixes


- 任务启动时立即返回日志文件路径以支持实时调试

## [5.1.3] - 2025-12-08


### 🐛 Bug Fixes


- resolve CI timing race in TestFakeCmdInfra

## [5.1.2] - 2025-12-08


### 🐛 Bug Fixes


- 修复channel同步竞态条件和死锁问题

### 💼 Other


- Merge pull request #51 from stellarlinkco/fix/channel-sync-race-conditions

- change codex-wrapper version

## [5.1.1] - 2025-12-08


### 🐛 Bug Fixes


- 增强日志清理的安全性和可靠性

- resolve data race on forceKillDelay with atomic operations

### 💼 Other


- Merge pull request #49 from stellarlinkco/freespace8/master

- resolve signal handling conflict preserving testability and Windows support

### 🧪 Testing


- 补充测试覆盖提升至 89.3%

## [5.1.0] - 2025-12-07


### 💼 Other


- Merge pull request #45 from Michaelxwb/master

- 修改windows安装说明

- 修改打包脚本

- 支持windows系统的安装

- Merge pull request #1 from Michaelxwb/feature-win

- 支持window

### 🚀 Features


- 添加启动时清理日志的功能和--cleanup标志支持

- implement enterprise workflow with multi-backend support

## [5.0.0] - 2025-12-05


### ⚙️ Miscellaneous Tasks


- clarify unit-test coverage levels in requirement questions

### 🐛 Bug Fixes


- defer startup log until args parsed

### 💼 Other


- Merge branch 'master' of github.com:stellarlinkco/myclaude

- Merge pull request #43 from gurdasnijor/smithery/add-badge

- Add Smithery badge

- Merge pull request #42 from freespace8/master

### 📚 Documentation


- rewrite documentation for v5.0 modular architecture

### 🚀 Features


- feat install.py

- implement modular installation system

### 🚜 Refactor


- remove deprecated plugin modules

## [4.8.2] - 2025-12-02


### 🐛 Bug Fixes


- skip signal test in CI environment

- make forceKillDelay testable to prevent signal test timeout

- correct Go version in go.mod from 1.25.3 to 1.21

- fix codex wrapper async log

- capture and include stderr in error messages

### 💼 Other


- Merge pull request #41 from stellarlinkco/fix-async-log

- remove test case 90

- optimize codex-wrapper

- Merge branch 'master' into fix-async-log

## [4.8.1] - 2025-12-01


### 🎨 Styling


- replace emoji with text labels

### 🐛 Bug Fixes


- improve --parallel parameter validation and docs

### 💼 Other


- remove codex-wrapper bin

## [4.8.0] - 2025-11-30


### 💼 Other


- update codex skill dependencies

## [4.7.3] - 2025-11-29


### 🐛 Bug Fixes


- 保留日志文件以便程序退出后调试并完善日志输出功能

### 💼 Other


- Merge pull request #34 from stellarlinkco/cce-worktree-master-20251129-111802-997076000

- update CLAUDE.md and codex skill

### 📚 Documentation


- improve codex skill parameter best practices

### 🚀 Features


- add session resume support and improve output format

- add parallel execution supp
... [TRUNCATED]
```

### File: config.json
```json
{
  "version": "1.0",
  "install_dir": "~/.claude",
  "log_file": "install.log",
  "modules": {
    "bmad": {
      "enabled": false,
      "description": "BMAD agile workflow with multi-agent orchestration",
      "operations": [
        {
          "type": "merge_dir",
          "source": "agents/bmad",
          "description": "Merge BMAD commands and agents"
        }
      ]
    },
    "requirements": {
      "enabled": false,
      "description": "Requirements-driven development workflow",
      "operations": [
        {
          "type": "merge_dir",
          "source": "agents/requirements",
          "description": "Merge requirements workflow commands and agents"
        }
      ]
    },
    "essentials": {
      "enabled": false,
      "description": "Core development commands and utilities",
      "operations": [
        {
          "type": "merge_dir",
          "source": "agents/development-essentials",
          "description": "Merge essential development commands"
        }
      ]
    },
    "omo": {
      "enabled": false,
      "description": "OmO multi-agent orchestration with Sisyphus coordinator",
      "agents": {
        "oracle": {
          "backend": "claude",
          "model": "claude-opus-4-5-20251101",
          "yolo": true
        },
        "librarian": {
          "backend": "claude",
          "model": "claude-sonnet-4-5-20250929",
          "yolo": true
        },
        "explore": {
          "backend": "opencode",
          "model": "opencode/grok-code"
        },
        "develop": {
          "backend": "codex",
          "model": "gpt-5.2",
          "reasoning": "xhigh",
          "yolo": true
        },
        "frontend-ui-ux-engineer": {
          "backend": "gemini",
          "model": "gemini-3-pro-preview"
        },
        "document-writer": {
          "backend": "gemini",
          "model": "gemini-3-flash-preview"
        }
      },
      "operations": [
        {
          "type": "copy_file",
          "source": "skills/omo/SKILL.md",
          "target": "skills/omo/SKILL.md",
          "description": "Install omo skill"
        },
        {
          "type": "copy_file",
          "source": "skills/omo/references/oracle.md",
          "target": "skills/omo/references/oracle.md",
          "description": "Install oracle agent prompt"
        },
        {
          "type": "copy_file",
          "source": "skills/omo/references/librarian.md",
          "target": "skills/omo/references/librarian.md",
          "description": "Install librarian agent prompt"
        },
        {
          "type": "copy_file",
          "source": "skills/omo/references/explore.md",
          "target": "skills/omo/references/explore.md",
          "description": "Install explore agent prompt"
        },
        {
          "type": "copy_file",
          "source": "skills/omo/references/frontend-ui-ux-engineer.md",
          "target": "skills/omo/references/frontend-ui-ux-engineer.md",
          "description": "Install frontend-ui-ux-engineer agent prompt"
        },
        {
          "type": "copy_file",
          "source": "skills/omo/references/document-writer.md",
          "target": "skills/omo/references/document-writer.md",
          "description": "Install document-writer agent prompt"
        },
        {
          "type": "copy_file",
          "source": "skills/omo/references/develop.md",
          "target": "skills/omo/references/develop.md",
          "description": "Install develop agent prompt"
        }
      ]
    },
    "sparv": {
      "enabled": false,
      "description": "SPARV workflow (Specify→Plan→Act→Review→Vault) with 10-point gate",
      "operations": [
        {
          "type": "copy_dir",
          "source": "skills/sparv",
          "target": "skills/sparv",
          "description": "Install sparv skill with all scripts and hooks"
        }
      ]
    },
    "do": {
      "enabled": true,
      "description": "5-phase feature development workflow with codeagent orchestration",
      "agents": {
        "develop": {
          "backend": "codex",
          "model": "gpt-4.1",
          "reasoning": "high",
          "yolo": true
        },
        "code-explorer": {
          "backend": "opencode",
          "model": ""
        },
        "code-architect": {
          "backend": "claude",
          "model": ""
        },
        "code-reviewer": {
          "backend": "claude",
          "model": ""
        }
      },
      "operations": [
        {
          "type": "copy_dir",
          "source": "skills/do",
          "target": "skills/do",
          "description": "Install do skill with hooks"
        }
      ]
    },
    "course": {
      "enabled": false,
      "description": "课程开发工作流，包含 dev、产品需求和测试用例技能",
      "operations": [
        {
          "type": "copy_dir",
          "source": "skills/dev",
          "target": "skills/dev",
          "description": "Install dev skill with agents"
        },
        {
          "type": "copy_file",
          "source": "skills/product-requirements/SKILL.md",
          "target": "skills/product-requirements/SKILL.md",
          "description": "Install product-requirements skill"
        },
        {
          "type": "copy_dir",
          "source": "skills/test-cases",
          "target": "skills/test-cases",
          "description": "Install test-cases skill with references"
        },
        {
          "type": "copy_file",
          "source": "skills/codeagent/SKILL.md",
          "target": "skills/codeagent/SKILL.md",
          "description": "Install codeagent skill"
        },
        {
          "type": "run_command",
          "command": "bash install.sh",
          "description": "Install codeagent-wrapper binary",
          "env": {
            "INSTALL_DIR": "${install_dir}"
          }
        }
      ]
    },
    "harness": {
      "enabled": false,
      "description": "Multi-session autonomous agent harness with progress checkpointing, failure recovery, task dependencies, and post-completion self-reflection",
      "operations": [
        {
          "type": "copy_dir",
          "source": "skills/harness",
          "target": "skills/harness",
          "description": "Install harness skill with hooks (Stop, SessionStart, TeammateIdle, SubagentStop, self-reflect)"
        }
      ]
    },
    "claudekit": {
      "enabled": false,
      "description": "ClaudeKit workflow: skills/do + global hooks (pre-bash, inject-spec, log-prompt)",
      "operations": [
        {
          "type": "copy_dir",
          "source": "skills/do",
          "target": "skills/do",
          "description": "Install do skill with 5-phase workflow"
        },
        {
          "type": "copy_dir",
          "source": "hooks",
          "target": "hooks",
          "description": "Install global hooks (pre-bash, inject-spec, log-prompt)"
        }
      ]
    }
  }
}

```

### File: config.schema.json
```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://github.com/stellarlinkco/myclaude/config.schema.json",
  "title": "Modular Installation Config",
  "type": "object",
  "additionalProperties": false,
  "required": ["version", "install_dir", "log_file", "modules"],
  "properties": {
    "version": {
      "type": "string",
      "pattern": "^[0-9]+\\.[0-9]+(\\.[0-9]+)?$"
    },
    "install_dir": {
      "type": "string",
      "minLength": 1,
      "description": "Target installation directory, supports ~/ expansion"
    },
    "log_file": {
      "type": "string",
      "minLength": 1
    },
    "modules": {
      "type": "object",
      "description": "可自定义的模块定义,每个模块名称可任意指定",
      "patternProperties": {
        "^[a-zA-Z0-9_-]+$": { "$ref": "#/$defs/module" }
      },
      "additionalProperties": false,
      "minProperties": 1
    }
  },
  "$defs": {
    "module": {
      "type": "object",
      "additionalProperties": false,
      "required": ["enabled", "description", "operations"],
      "properties": {
        "enabled": { "type": "boolean", "default": false },
        "description": { "type": "string", "minLength": 3 },
        "operations": {
          "type": "array",
          "minItems": 1,
          "items": { "$ref": "#/$defs/operation" }
        }
      }
    },
    "operation": {
      "oneOf": [
        { "$ref": "#/$defs/op_copy_dir" },
        { "$ref": "#/$defs/op_copy_file" },
        { "$ref": "#/$defs/op_merge_dir" },
        { "$ref": "#/$defs/op_merge_json" },
        { "$ref": "#/$defs/op_run_command" }
      ]
    },
    "common_operation_fields": {
      "type": "object",
      "properties": {
        "description": { "type": "string" }
      },
      "additionalProperties": true
    },
    "op_copy_dir": {
      "type": "object",
      "additionalProperties": false,
      "required": ["type", "source", "target"],
      "properties": {
        "type": { "const": "copy_dir" },
        "source": { "type": "string", "minLength": 1 },
        "target": { "type": "string", "minLength": 1 },
        "description": { "type": "string" }
      }
    },
    "op_copy_file": {
      "type": "object",
      "additionalProperties": false,
      "required": ["type", "source", "target"],
      "properties": {
        "type": { "const": "copy_file" },
        "source": { "type": "string", "minLength": 1 },
        "target": { "type": "string", "minLength": 1 },
        "description": { "type": "string" }
      }
    },
    "op_merge_dir": {
      "type": "object",
      "additionalProperties": false,
      "required": ["type", "source"],
      "properties": {
        "type": { "const": "merge_dir" },
        "source": { "type": "string", "minLength": 1 },
        "description": { "type": "string" }
      }
    },
    "op_merge_json": {
      "type": "object",
      "additionalProperties": false,
      "required": ["type", "source", "target"],
      "properties": {
        "type": { "const": "merge_json" },
        "source": { "type": "string", "minLength": 1 },
        "target": { "type": "string", "minLength": 1 },
        "merge_key": { "type": "string" },
        "description": { "type": "string" }
      }
    },
    "op_run_command": {
      "type": "object",
      "additionalProperties": false,
      "required": ["type", "command"],
      "properties": {
        "type": { "const": "run_command" },
        "command": { "type": "string", "minLength": 1 },
        "description": { "type": "string" },
        "env": {
          "type": "object",
          "additionalProperties": { "type": "string" }
        }
      }
    }
  }
}

```

### File: install.py
```py
#!/usr/bin/env python3
"""JSON-driven modular installer.

Keep it simple: validate config, expand paths, run three operation types,
and record what happened. Designed to be small, readable, and predictable.
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

try:
    import jsonschema
except ImportError:  # pragma: no cover
    jsonschema = None

DEFAULT_INSTALL_DIR = "~/.claude"
SETTINGS_FILE = "settings.json"
WRAPPER_REQUIRED_MODULES = {"do", "omo"}


def _ensure_list(ctx: Dict[str, Any], key: str) -> List[Any]:
    ctx.setdefault(key, [])
    return ctx[key]


def parse_args(argv: Optional[Iterable[str]] = None) -> argparse.Namespace:
    """Parse CLI arguments.

    The default install dir must remain "~/.claude" to match docs/tests.
    """

    parser = argparse.ArgumentParser(
        description="JSON-driven modular installation system"
    )
    parser.add_argument(
        "--install-dir",
        default=DEFAULT_INSTALL_DIR,
        help="Installation directory (defaults to ~/.claude)",
    )
    parser.add_argument(
        "--module",
        help="Comma-separated modules to install/uninstall, or 'all'",
    )
    parser.add_argument(
        "--config",
        default="config.json",
        help="Path to configuration file",
    )
    parser.add_argument(
        "--list-modules",
        action="store_true",
        help="List available modules and exit",
    )
    parser.add_argument(
        "--status",
        action="store_true",
        help="Show installation status of all modules",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="Uninstall specified modules",
    )
    parser.add_argument(
        "--update",
        action="store_true",
        help="Update already installed modules",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Force overwrite existing files",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output to terminal",
    )
    return parser.parse_args(argv)


def _load_json(path: Path) -> Any:
    try:
        with path.open("r", encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON in {path}: {exc}") from exc


def _save_json(path: Path, data: Any) -> None:
    """Save data to JSON file with proper formatting."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        json.dump(data, fh, indent=2, ensure_ascii=False)
        fh.write("\n")


# =============================================================================
# Hooks Management
# =============================================================================

def load_settings(ctx: Dict[str, Any]) -> Dict[str, Any]:
    """Load settings.json from install directory."""
    settings_path = ctx["install_dir"] / SETTINGS_FILE
    if settings_path.exists():
        try:
            return _load_json(settings_path)
        except (ValueError, FileNotFoundError):
            return {}
    return {}


def save_settings(ctx: Dict[str, Any], settings: Dict[str, Any]) -> None:
    """Save settings.json to install directory."""
    settings_path = ctx["install_dir"] / SETTINGS_FILE
    _save_json(settings_path, settings)


def find_module_hooks(module_name: str, cfg: Dict[str, Any], ctx: Dict[str, Any]) -> List[tuple]:
    """Find all hooks.json files for a module.

    Returns list of tuples (hooks_config, plugin_root_path).
    Searches in order for each copy_dir operation:
    1. {target_dir}/hooks/hooks.json (for skills with hooks subdirectory)
    2. {target_dir}/hooks.json (for hooks directory itself)
    """
    results = []
    seen_paths = set()

    # Check for hooks in operations (copy_dir targets)
    for op in cfg.get("operations", []):
        if op.get("type") == "copy_dir":
            target_dir = ctx["install_dir"] / op["target"]
            source_dir = ctx["config_dir"] / op["source"]

            # Check both target and source directories
            for base_dir, plugin_root in [(target_dir, str(target_dir)), (source_dir, str(target_dir))]:
                # First check {dir}/hooks/hooks.json (for skills)
                hooks_file = base_dir / "hooks" / "hooks.json"
                if hooks_file.exists() and str(hooks_file) not in seen_paths:
                    try:
                        results.append((_load_json(hooks_file), plugin_root))
                        seen_paths.add(str(hooks_file))
                    except (ValueError, FileNotFoundError):
                        pass

                # Then check {dir}/hooks.json (for hooks directory itself)
                hooks_file = base_dir / "hooks.json"
                if hooks_file.exists() and str(hooks_file) not in seen_paths:
                    try:
                        results.append((_load_json(hooks_file), plugin_root))
                        seen_paths.add(str(hooks_file))
                    except (ValueError, FileNotFoundError):
                        pass

    return results


def _create_hook_marker(module_name: str) -> str:
    """Create a marker to identify hooks from a specific module."""
    return f"__module:{module_name}__"


def _replace_hook_variables(obj: Any, plugin_root: str) -> Any:
    """Recursively replace ${CLAUDE_PLUGIN_ROOT} in hook config."""
    if isinstance(obj, str):
        return obj.replace("${CLAUDE_PLUGIN_ROOT}", plugin_root)
    elif isinstance(obj, dict):
        return {k: _replace_hook_variables(v, plugin_root) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [_replace_hook_variables(item, plugin_root) for item in obj]
    return obj


def merge_hooks_to_settings(module_name: str, hooks_config: Dict[str, Any], ctx: Dict[str, Any], plugin_root: str = "") -> None:
    """Merge module hooks into settings.json."""
    settings = load_settings(ctx)
    settings.setdefault("hooks", {})

    module_hooks = hooks_config.get("hooks", {})
    marker = _create_hook_marker(module_name)

    # Replace ${CLAUDE_PLUGIN_ROOT} with actual path
    if plugin_root:
        module_hooks = _replace_hook_variables(module_hooks, plugin_root)

    for hook_type, hook_entries in module_hooks.items():
        settings["hooks"].setdefault(hook_type, [])

        for entry in hook_entries:
            # Add marker to identify this hook's source module
            entry_copy = dict(entry)
            entry_copy["__module__"] = module_name

            # Check if already exists (avoid duplicates)
            exists = False
            for existing in settings["hooks"][hook_type]:
                if existing.get("__module__") == module_name:
                    # Same module, check if same hook
                    if _hooks_equal(existing, entry_copy):
                        exists = True
                        break

            if not exists:
                settings["hooks"][hook_type].append(entry_copy)

    save_settings(ctx, settings)
    write_log({"level": "INFO", "message": f"Merged hooks for module: {module_name}"}, ctx)


def unmerge_hooks_from_settings(module_name: str, ctx: Dict[str, Any]) -> None:
    """Remove module hooks from settings.json."""
    settings = load_settings(ctx)

    if "hooks" not in settings:
        return

    modified = False
    for hook_type in list(settings["hooks"].keys()):
        original_len = len(settings["hooks"][hook_type])
        settings["hooks"][hook_type] = [
            entry for entry in settings["hooks"][hook_type]
            if entry.get("__module__") != module_name
        ]
        if len(settings["hooks"][hook_type]) < original_len:
            modified = True

        # Remove empty hook type arrays
        if not settings["hooks"][hook_type]:
            del settings["hooks"][hook_type]

    if modified:
        save_settings(ctx, settings)
        write_log({"level": "INFO", "message": f"Removed hooks for module: {module_name}"}, ctx)


def merge_agents_to_models(module_name: str, agents: Dict[str, Any], ctx: Dict[str, Any]) -> None:
    """Merge module agent configs into ~/.codeagent/models.json."""
    models_path = Path.home() / ".codeagent" / "models.json"
    models_path.parent.mkdir(parents=True, exist_ok=True)

    if models_path.exists():
        with models_path.open("r", encoding="utf-8") as fh:
            models = json.load(fh)
    else:
        template = ctx["config_dir"] / "templates" / "models.json.example"
        if template.exists():
            with template.open("r", encoding="utf-8") as fh:
                models = json.load(fh)
            # Clear template agents so modules populate with __module__ tags
            models["agents"] = {}
        else:
            models = {
                "default_backend": "codex",
                "default_model": "gpt-4.1",
                "backends": {},
                "agents": {},
            }

    models.setdefault("agents", {})
    for agent_name, agent_cfg in agents.items():
        entry = dict(agent_cfg)
        entry["__module__"] = module_name

        existing = models["agents"].get(agent_name, {})
        if not existing or existing.get("__module__"):
            models["agents"][agent_name] = entry

    with models_path.open("w", encoding="utf-8") as fh:
        json.dump(models, fh, indent=2, ensure_ascii=False)

    write_log(
        {
            "level": "INFO",
            "message": (
                f"Merged {len(agents)} agent(s) from {module_name} "
                "into models.json"
            ),
        },
        ctx,
    )


def unmerge_agents_from_models(module_name: str, ctx: Dict[str, Any]) -> None:
    """Remove module's agent configs from ~/.codeagent/models.json.

    If another installed module also declares a removed agent, restore that
    module's version so shared agents (e.g. 'develop') are not lost.
    """
    models_path = Path.home() / ".codeagent" / "models.json"
    if not models_path.exists():
        return

    with models_path.open("r", encoding="utf-8") as fh:
        models = json.load(fh)

    agents = models.get("agents", {})
    to_remove = [
        name
        for name, cfg in agents.items()
        if isinstance(cfg, dict) and cfg.get("__module__") == module_name
    ]

    if not to_remove:
        return

    # Load config to find other modules that declare the same agents
    config_path = ctx["config_dir"] / "config.json"
    config = _load_json(config_path) if config_path.exists() else {}
    installed = load_installed_status(ctx).get("modules", {})

    for name in to_remove:
        del agents[name]
        # Check if another installed module also declares this agent
        for other_mod, other_status in installed.items():
            if other_mod == module_name:
                continue
            if other_status.get("status") != "success":
                continue
            other_cfg = config.get("modules", {}).get(other_mod, {})
            other_agents = other_cfg.get("agents", {})
            if name in other_agents:
                restored = dict(other_agents[name])
                restored["__module__"] = other_mod
                agents[name] = restored
                break

    with models_path.open("w", encoding="utf-8") as fh:
        json.dump(models, fh, indent=2, ensure_ascii=False)

    write_log(
        {
            "level": "INFO",
            "message": (
                f"Removed {len(to_remove)} agent(s) from {module_name} "
                "in models.json"
            ),
        },
        ctx,
    )


def _hooks_equal(hook1: Dict[str, Any], hook2: Dict[str, Any]) -> bool:
    """Compare two hooks ignoring the __module__ marker."""
    h1 = {k: v for k, v in hook1.items() if k != "__module__"}
    h2 = {k: v for k, v in hook2.items() if k != "__module__"}
    return h1 == h2


def load_config(path: str) -> Dict[str, Any]:
    """Load config and validate against JSON Schema.

    Schema is searched in the config directory first, then alongside this file.
    """

    config_path = Path(path).expanduser().resolve()
    config = _load_json(config_path)

    if jsonschema is None:
        print(
            "WARNING: python package 'jsonschema' is not installed; "
            "skipping config validation. To enable validation run:\n"
            "  python3 -m pip install jsonschema\n",
            file=sys.stderr,
        )

        if not isinstance(config, dict):
            raise ValueError(
                f"Config must be a dict, got {type(config).__name__}. "
                "Check your config.json syntax."
            )

        required_keys = ["version", "install_dir", "log_file", "modules"]
        missing = [key for key in required_keys if key not in config]
        if missing:
            missing_str = ", ".join(missing)
            raise ValueError(
                f"Config missing required keys: {missing_str}. "
                "Install jsonschema for better validation: "
                "python3 -m pip install jsonschema"
            )

        return config

    schema_candidates = [
        config_path.parent / "config.schema.json",
        Path(__file__).resolve().with_name("config.schema.json"),
    ]
    schema_path = next((p for p in schema_candidates if p.exists()), None)
    if schema_path is None:
        raise FileNotFoundError("config.schema.json not found")

    schema = _load_json(schema_path)
    try:
        jsonschema.validate(config, schema)
    except jsonschema.ValidationError as exc:
        raise ValueError(f"Config validation failed: {exc.message}") from exc

    return config


def resolve_paths(config: Dict[str, Any], args: argparse.Namespace) -> Dict[str, Any]:
    """Resolve all filesystem paths to absolute Path objects."""

    config_dir = Path(args.config).expanduser().resolve().parent

    if args.install_dir and args.install_dir != DEFAULT_INSTALL_DIR:
        install_dir_raw = args.install_dir
    elif config.get("install_dir"):
        install_dir_raw = config.get("install_dir")
    else:
        install_dir_raw = DEFAULT_INSTALL_DIR

    install_dir = Path(install_dir_raw).expanduser().resolve()

    log_file_raw = config.get("log_file", "install.log")
    log_file = Path(log_file_raw).expanduser()
    if not log_file.is_absolute():
        log_file = install_dir / log_file

    return {
        "install_dir": install_dir,
        "log_file": log_file,
        "status_file": install_dir / "installed_modules.json",
        "config_dir": config_dir,
        "force": bool(getattr(args, "force", False)),
        "verbose": bool(getattr(args, "verbose", False)),
        "app
... [TRUNCATED]
```

### File: install.sh
```sh
#!/bin/bash
set -e

if [ -z "${SKIP_WARNING:-}" ]; then
  echo "⚠️  WARNING: install.sh is LEGACY and will be removed in future versions."
  echo "Please use the new installation method:"
  echo "  npx github:stellarlinkco/myclaude"
  echo ""
  echo "Set SKIP_WARNING=1 to bypass this message"
  echo "Continuing with legacy installation in 5 seconds..."
  sleep 5
fi

# Detect platform
OS=$(uname -s | tr '[:upper:]' '[:lower:]')
ARCH=$(uname -m)

# Normalize architecture names
case "$ARCH" in
    x86_64) ARCH="amd64" ;;
    aarch64|arm64) ARCH="arm64" ;;
    *) echo "Unsupported architecture: $ARCH" >&2; exit 1 ;;
esac

# Build download URL
REPO="stellarlinkco/myclaude"
VERSION="${CODEAGENT_WRAPPER_VERSION:-latest}"
BINARY_NAME="codeagent-wrapper-${OS}-${ARCH}"
if [ "$VERSION" = "latest" ]; then
    URL="https://github.com/${REPO}/releases/latest/download/${BINARY_NAME}"
else
    URL="https://github.com/${REPO}/releases/download/${VERSION}/${BINARY_NAME}"
fi

echo "Downloading codeagent-wrapper from ${URL}..."
if ! curl -fsSL "$URL" -o /tmp/codeagent-wrapper; then
    echo "ERROR: failed to download binary" >&2
    exit 1
fi

INSTALL_DIR="${INSTALL_DIR:-$HOME/.claude}"
BIN_DIR="${INSTALL_DIR}/bin"
mkdir -p "$BIN_DIR"

mv /tmp/codeagent-wrapper "${BIN_DIR}/codeagent-wrapper"
chmod +x "${BIN_DIR}/codeagent-wrapper"

if "${BIN_DIR}/codeagent-wrapper" --version >/dev/null 2>&1; then
    echo "codeagent-wrapper installed successfully to ${BIN_DIR}/codeagent-wrapper"
else
    echo "ERROR: installation verification failed" >&2
    exit 1
fi

# Auto-add to shell config files with idempotency
if [[ ":${PATH}:" != *":${BIN_DIR}:"* ]]; then
    echo ""
    echo "WARNING: ${BIN_DIR} is not in your PATH"

    # Detect user's default shell (from $SHELL, not current script executor)
    USER_SHELL=$(basename "$SHELL")
    case "$USER_SHELL" in
        zsh)
            RC_FILE="$HOME/.zshrc"
            PROFILE_FILE="$HOME/.zprofile"
            ;;
        *)
            RC_FILE="$HOME/.bashrc"
            PROFILE_FILE="$HOME/.profile"
            ;;
    esac

    # Idempotent add: check if complete export statement already exists
    EXPORT_LINE="export PATH=\"${BIN_DIR}:\$PATH\""
    FILES_TO_UPDATE=("$RC_FILE" "$PROFILE_FILE")

    for FILE in "${FILES_TO_UPDATE[@]}"; do
        if [ -f "$FILE" ] && grep -qF "${EXPORT_LINE}" "$FILE" 2>/dev/null; then
            echo "  ${BIN_DIR} already in ${FILE}, skipping."
        else
            echo "  Adding to ${FILE}..."
            echo "" >> "$FILE"
            echo "# Added by myclaude installer" >> "$FILE"
            echo "${EXPORT_LINE}" >> "$FILE"
        fi
    done

    echo "  Done. Restart your shell or run:"
    echo "    source ${PROFILE_FILE}"
    echo "    source ${RC_FILE}"
    echo ""
fi

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
