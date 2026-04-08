---
id: repo-fetched-autoresearchclaw-112755
type: knowledge
owner: OA
registered_at: 2026-04-05T03:39:02.636324
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_AutoResearchClaw_112755

## Assimilation Report
Auto-cloned repository: FETCHED_AutoResearchClaw_112755

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="image/logo.png" width="700" alt="AutoResearchClaw Logo">
</p>

<h2 align="center"><b>Chat an Idea. Get a Paper. Autonomous, Collaborative & Self-Evolving.</b></h2>



<p align="center">
  <b><i><font size="5">Just chat with <a href="#openclaw-integration">OpenClaw</a>: "Research X" → done.</font></i></b>
</p>

<p align="center">
  <img src="image/framework_v2.png" width="100%" alt="AutoResearchClaw Framework">
</p>


<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
  <a href="https://python.org"><img src="https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white" alt="Python 3.11+"></a>
  <a href="#testing"><img src="https://img.shields.io/badge/Tests-2699%20passed-brightgreen?logo=pytest&logoColor=white" alt="2699 Tests Passed"></a>
  <a href="https://github.com/aiming-lab/AutoResearchClaw"><img src="https://img.shields.io/badge/GitHub-AutoResearchClaw-181717?logo=github" alt="GitHub"></a>
  <a href="#openclaw-integration"><img src="https://img.shields.io/badge/OpenClaw-Compatible-ff4444?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZD0iTTEyIDJDNi40OCAyIDIgNi40OCAyIDEyczQuNDggMTAgMTAgMTAgMTAtNC40OCAxMC0xMFMxNy41MiAyIDEyIDJ6IiBmaWxsPSJ3aGl0ZSIvPjwvc3ZnPg==" alt="OpenClaw Compatible"></a>
  <a href="https://discord.gg/u4ksqW5P"><img src="https://img.shields.io/badge/Discord-Join%20Community-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <a href="docs/README_CN.md">🇨🇳 中文</a> ·
  <a href="docs/README_JA.md">🇯🇵 日本語</a> ·
  <a href="docs/README_KO.md">🇰🇷 한국어</a> ·
  <a href="docs/README_FR.md">🇫🇷 Français</a> ·
  <a href="docs/README_DE.md">🇩🇪 Deutsch</a> ·
  <a href="docs/README_ES.md">🇪🇸 Español</a> ·
  <a href="docs/README_PT.md">🇧🇷 Português</a> ·
  <a href="docs/README_RU.md">🇷🇺 Русский</a> ·
  <a href="docs/README_AR.md">🇸🇦 العربية</a>
</p>

<p align="center">
  <a href="docs/showcase/SHOWCASE.md">🏆 Paper Showcase</a> · <a href="docs/HITL_GUIDE.md">🧑‍✈️ Co-Pilot Guide</a> · <a href="docs/integration-guide.md">📖 Integration Guide</a> · <a href="https://discord.gg/u4ksqW5P">💬 Discord Community</a>
</p>

---

<table>
<tr>
<td width="18%">
<a href="docs/showcase/SHOWCASE.md"><img src="docs/showcase/thumbnails/paper_I_random_matrix-01.png" width="120" alt="Sample Paper"/></a>
</td>
<td valign="middle">
<b>🏆 Generated Paper Showcase</b><br><br>
<b>8 papers across 8 domains</b> — math, statistics, biology, computing, NLP, RL, vision, robustness — generated fully autonomously or with Human-in-the-Loop co-pilot guidance.<br><br>
<a href="docs/showcase/SHOWCASE.md"><img src="https://img.shields.io/badge/View_Full_Showcase_→-All_8_Papers-d73a49?style=for-the-badge" alt="View Showcase"></a>
</td>
</tr>
</table>

---

> **🧪 We're looking for testers!** Try the pipeline with your own research idea — from any field — and [tell us what you think](docs/TESTER_GUIDE.md). Your feedback directly shapes the next version. **[→ Testing Guide](docs/TESTER_GUIDE.md)** | **[→ 中文测试指南](docs/TESTER_GUIDE_CN.md)** | **[→ 日本語テストガイド](docs/TESTER_GUIDE_JA.md)**

---

## 🔥 News
- **[04/01/2026]** **v0.4.0** — **Human-in-the-Loop Co-Pilot System** — AutoResearchClaw is no longer purely autonomous. New HITL system adds 6 intervention modes (`full-auto`, `gate-only`, `checkpoint`, `step-by-step`, `co-pilot`, `custom`), per-stage policies, and deep human-AI collaboration. Includes: Idea Workshop for hypothesis co-creation, Baseline Navigator for experiment design review, Paper Co-Writer for collaborative drafting, SmartPause (confidence-driven dynamic intervention), ALHF intervention learning, anti-hallucination claim verification, cost budget guardrails, pipeline branching for parallel hypothesis exploration, and CLI commands (`attach`/`status`/`approve`/`reject`/`guide`). **[→ Full HITL Guide](docs/HITL_GUIDE.md)**
- **[03/30/2026]** **Flexible Skill Loading** — AutoResearchClaw now supports loading open-source and custom skills from any discipline to further enhance your research experience. 19 pre-loaded skills are included as ready-to-use references, covering scientific writing, experiment design, chemistry, biology, and more — including an [A-Evolve](https://github.com/A-EVO-Lab/a-evolve) agentic evolution skill contributed by the community. Load your own via `researchclaw skills install` or drop a `SKILL.md` into `.claude/skills/`. See [Skills Library](#-skills-library).
- **[03/22/2026]** [v0.3.2](https://github.com/aiming-lab/AutoResearchClaw/releases/tag/v0.3.2) — **Cross-Platform Support + Major Stability** — AutoResearchClaw now runs on any ACP-compatible agent backend (Claude Code, Codex CLI, Copilot CLI, Gemini CLI, Kimi CLI) and supports messaging platforms (Discord, Telegram, Lark, WeChat) via OpenClaw bridge. New CLI-agent code generation backend delegates Stages 10 & 13 to external CLI agents with budget control and timeout management. Also includes anti-fabrication system (VerifiedRegistry + experiment diagnosis & repair loop), 100+ bug fixes, modular executor refactoring, `--resume` auto-detection, LLM retry hardening, and community-reported fixes.

<details>
<summary>Earlier releases</summary>

- **[03/18/2026]** [v0.3.1](https://github.com/aiming-lab/AutoResearchClaw/releases/tag/v0.3.1) — **OpenCode Beast Mode + Community Contributions** — New "Beast Mode" routes complex code generation to [OpenCode](https://github.com/anomalyco/opencode) with automatic complexity scoring and graceful fallback. Added Novita AI provider support, thread-safety hardening, improved LLM output parsing robustness, and 20+ bug fixes from community PRs and internal audit.
- **[03/17/2026]** [v0.3.0](https://github.com/aiming-lab/AutoResearchClaw/releases/tag/v0.3.0) — **MetaClaw Integration** — AutoResearchClaw now supports [MetaClaw](https://github.com/aiming-lab/MetaClaw) cross-run learning: pipeline failures → structured lessons → reusable skills, injected into all 23 stages. **+18.3%** robustness in controlled experiments. Opt-in (`metaclaw_bridge.enabled: true`), fully backward-compatible. See [Integration Guide](#-metaclaw-integration).
- **[03/16/2026]** [v0.2.0](https://github.com/aiming-lab/AutoResearchClaw/releases/tag/v0.2.0) — Three multi-agent subsystems (CodeAgent, BenchmarkAgent, FigureAgent), hardened Docker sandbox with network-policy-aware execution, 4-round paper quality audit (AI-slop detection, 7-dim review scoring, NeurIPS checklist), and 15+ bug fixes from production runs.
- **[03/15/2026]** [v0.1.0](https://github.com/aiming-lab/AutoResearchClaw/releases/tag/v0.1.0) — We release AutoResearchClaw: a fully autonomous 23-stage research pipeline that turns a single research idea into a conference-ready paper. No human intervention required.

</details>

---

## ⚡ One Command. One Paper.

```bash
# Fully autonomous — no human intervention
pip install -e . && researchclaw setup && researchclaw init && researchclaw run --topic "Your research idea here" --auto-approve

# Co-Pilot mode — collaborate with AI at key decision points
researchclaw run --topic "Your research idea here" --mode co-pilot
```


---

## 🤔 What Is This?

**You think it. AutoResearchClaw writes it. You guide the key decisions.**

Drop a research topic — get back a full academic paper with real literature from OpenAlex, Semantic Scholar & arXiv, hardware-aware sandbox experiments (GPU/MPS/CPU auto-detected), statistical analysis, multi-agent peer review, and conference-ready LaTeX targeting NeurIPS/ICML/ICLR. Run it fully autonomous, or use **Co-Pilot mode** to guide the AI at critical decision points — choose research directions, review experiment designs, and co-write the paper. No hallucinated references.

<table>
<tr><td>📄</td><td><code>paper_draft.md</code></td><td>Full academic paper (Introduction, Related Work, Method, Experiments, Results, Conclusion)</td></tr>
<tr><td>📐</td><td><code>paper.tex</code></td><td>Conference-ready LaTeX (NeurIPS / ICLR / ICML templates)</td></tr>
<tr><td>📚</td><td><code>references.bib</code></td><td>Real BibTeX references from OpenAlex, Semantic Scholar and arXiv — auto-pruned to match inline citations</td></tr>
<tr><td>🔍</td><td><code>verification_report.json</code></td><td>4-layer citation integrity + relevance verification (arXiv, CrossRef, DataCite, LLM)</td></tr>
<tr><td>🧪</td><td><code>experiment runs/</code></td><td>Generated code + sandbox results + structured JSON metrics</td></tr>
<tr><td>📊</td><td><code>charts/</code></td><td>Auto-generated condition comparison charts with error bars and confidence intervals</td></tr>
<tr><td>📝</td><td><code>reviews.md</code></td><td>Multi-agent peer review with methodology-evidence consistency checks</td></tr>
<tr><td>🧬</td><td><code>evolution/</code></td><td>Self-learning lessons extracted from each run</td></tr>
<tr><td>📦</td><td><code>deliverables/</code></td><td>All final outputs in one folder — compile-ready for Overleaf</td></tr>
</table>

The pipeline runs **end-to-end** — fully autonomous or with human-in-the-loop collaboration. When experiments fail, it self-heals. When hypotheses don't hold, it pivots. When citations are fake, it kills them. When you want to steer, it pauses and listens.

🌍 **Run it anywhere.** AutoResearchClaw isn't locked to a single platform. Use it standalone via CLI, plug it into [OpenClaw](https://github.com/openclaw/openclaw), or wire it up through any ACP-compatible agent — 🤖 Claude Code, 💻 Codex CLI, 🐙 Copilot CLI, ♊ Gemini CLI, 🌙 Kimi CLI, you name it. And because OpenClaw bridges to messaging platforms, you can kick off a full research run from 💬 Discord, ✈️ Telegram, 🐦 Lark (飞书), 💚 WeChat, or wherever your team already hangs out. One topic in, one paper out — no matter where you type it.

---

## 🚀 Quick Start

```bash
# 1. Clone & install
git clone https://github.com/aiming-lab/AutoResearchClaw.git
cd AutoResearchClaw
python3 -m venv .venv && source .venv/bin/activate
pip install -e .

# 2. Setup (interactive — installs OpenCode beast mode, checks Docker/LaTeX)
researchclaw setup

# 3. Configure
researchclaw init          # Interactive: choose LLM provider, creates config.arc.yaml
# Or manually: cp config.researchclaw.example.yaml config.arc.yaml

# 4. Run
export OPENAI_API_KEY="sk-..."
researchclaw run --config config.arc.yaml --topic "Your research idea" --auto-approve
```

Output → `artifacts/rc-YYYYMMDD-HHMMSS-<hash>/deliverables/` — compile-ready LaTeX, BibTeX, experiment code, charts.

<details>
<summary>📝 Minimum required config</summary>

```yaml
project:
  name: "my-research"

research:
  topic: "Your research topic here"

llm:
  base_url: "https://api.openai.com/v1"
  api_key_env: "OPENAI_API_KEY"
  primary_model: "gpt-4o"
  fallback_models: ["gpt-4o-mini"]

experiment:
  mode: "sandbox"
  sandbox:
    python_path: ".venv/bin/python"
```

</details>

---

## 🧠 What Makes It Different

| Capability | How It Works |
|-----------|-------------|
| **🧑‍✈️ Co-Pilot Mode** | 6 intervention modes — from fully autonomous to step-by-step. Guide the AI at critical decisions (hypotheses, baselines, paper writing) or let it run free. SmartPause auto-detects when human input would help. |
| **🔄 PIVOT / REFINE Loop** | Stage 15 autonomously decides: PROCEED, REFINE (tweak params), or PIVOT (new direction). Artifacts auto-versioned. |
| **🤖 Multi-Agent Debate** | Hypothesis generation, result analysis, and peer review each use structured multi-perspective debate. |
| **🧬 Self-Learning** | Lessons extracted per run (decision rationale, runtime warnings, metric anomalies) with 30-day time-decay. Future runs learn from past mistakes. |
| **📚 Knowledge Base** | Every run builds structured KB across 6 categories (decisions, experiments, findings, literature, questions, reviews). |
| **🛡️ Sentinel Watchdog** | Background quality monitor: NaN/Inf detection, paper-evidence consistency, citation relevance scoring, anti-fabrication guard. |
| **🔍 Claim Verification** | Inline fact-checking: extracts claims from AI-generated text and cross-references against collected literature. Flags ungrounded citations and fabricated numbers. |
| **🌿 Branch Exploration** | Fork the pipeline to explore multiple research directions simultaneously, compare results side-by-side, and merge the best path forward. |

---

## 🦞 OpenClaw Integration

<table>
<tr>

**AutoResearchClaw is an [OpenClaw](https://github.com/openclaw/openclaw)-compatible service.** Install it in OpenClaw and launch autonomous research with a single message — or use it standalone via CLI, Claude Code, or any AI coding assistant.

</tr>
</table>

### 🚀 Use with OpenClaw (Recommended)

If you already use [OpenClaw](https://github.com/openclaw/openclaw) as your AI assistant:

```
1️⃣  Share the GitHub repo URL with OpenClaw
2️⃣  OpenClaw auto-reads RESEARCHCLAW_AGENTS.md → understands the pipeline
3️⃣  Say: "Research [your topic]"
4️⃣  Done — OpenClaw clones, installs, configures, runs, and returns results
```

**That's it.** OpenClaw handles `git clone`, `pip install`, config setup, and pipeline execution automatically. You just chat.

<details>
<summary>💡 What happens under the hood</summary>

1. OpenClaw reads `RESEARCHCLAW_AGENTS.md` → learns the research orchestrator role
2. OpenClaw reads `README.md` → understands installation and pipeline structure
3. OpenClaw copies `config.researchclaw.example.yaml` → `config.yaml`
4. Asks for your LLM API key (or uses your environment variable)
5. Runs `pip install -e .` + `researchclaw run --topic "..." --auto-approve`
6. Returns the paper, LaTeX, experiments, and citations

</details>

### 🔌 OpenClaw Bridge (Advanced)

For deeper integration, AutoResearchClaw includes a **bridge adapter system** with 6 optional capabilities:

```yaml
# config.arc.yaml
openclaw_bridge:
  use_cron: true              # ⏰ Scheduled research runs
  use_message: true           # 💬 Progress notifications (Discord/Slack/Telegram)
  use_memory: true            # 🧠 Cross-session knowledge persistence
  use_sessions_spawn: true    # 🔀 Spawn parallel sub-sessions for concurrent stages
  use_web_fetch: true         # 🌐 Live web search during literature review
  use_browser: false          # 🖥️ Browser-based paper collection
```

Each flag activates a typed adapter protocol. When OpenClaw provides these capabilities, the adapters consume them without code changes. See [`docs/integration-guide.md`](docs/integration-guide.md) for full details.

### ACP (Agent Client Protocol)

AutoResearchClaw can use **any ACP-compatible coding agent** as its LLM backend — no API keys required. The agent communicates via [acpx](https://github.com/openclaw/acpx), maintaining a single persistent session across all 23 pipeline stages.

| Agent | Command | Notes |
|-------|---------|-------|
| Claude Code | `claude` | Anthropic |
| Codex CLI | `codex` | OpenAI |
| Copilot CLI | `gh` |
... [TRUNCATED]
```

### File: CONTRIBUTING.md
```md
# Contributing to AutoResearchClaw

## Setup

1. Fork and clone the repo
2. Create a venv and install with dev extras:
   ```
   python3 -m venv .venv && source .venv/bin/activate
   pip install -e ".[dev]"
   ```
3. Generate your local config:
   ```
   researchclaw init
   ```
4. Edit `config.arc.yaml` with your LLM settings

## Config Convention

- `config.researchclaw.example.yaml` — tracked template (do not add secrets)
- `config.arc.yaml` — your local config (gitignored, created by `researchclaw init`)
- `config.yaml` — also gitignored, supported as fallback

## Running Tests

```
pytest tests/
```

## Checking Your Environment

```
researchclaw doctor
```

## PR Guidelines

- Branch from main
- One concern per PR
- Ensure `pytest tests/` passes
- Include tests for new functionality

```

### File: RESEARCHCLAW_AGENTS.md
```md
# ResearchClaw — Agent Configuration

## Overview

ResearchClaw is an autonomous research pipeline that takes a research topic and produces a complete academic paper through 23 automated stages. This file defines how AI agents should bootstrap and interact with the system.

## Agent Role: Research Orchestrator

You are an AI research assistant operating ResearchClaw. Your job is to:

1. **Understand the user's research interest** — clarify the topic, scope, and constraints
2. **Configure the pipeline** — set up `config.yaml` with appropriate LLM settings and experiment mode
3. **Execute the pipeline** — run the 23-stage pipeline via CLI or Python API
4. **Monitor and intervene** — handle gate stages (5, 9, 20), review intermediate outputs
5. **Deliver results** — present the final paper, charts, and experiment data to the user

## Quick Setup

```bash
# Install
pip install -e .

# Configure (copy and edit)
cp config.researchclaw.example.yaml config.yaml
# Set llm.base_url, llm.api_key, experiment.mode

# Run
researchclaw run --topic "Your topic" --auto-approve
```

## Pipeline Stages (23 stages, 8 phases)

| Phase | Stages | Description |
|-------|--------|-------------|
| A: Research Scoping | 1-2 | Define topic, decompose into sub-problems |
| B: Literature Discovery | 3-6 | Search strategy, collect papers, screen [GATE@5], extract knowledge |
| C: Knowledge Synthesis | 7-8 | Cluster topics, generate hypotheses |
| D: Experiment Design | 9-11 | Design experiments [GATE@9], generate code, plan resources |
| E: Experiment Execution | 12-13 | Run experiments, iterative refinement |
| F: Analysis & Decision | 14-15 | Analyze results, decide proceed/pivot/iterate |
| G: Paper Writing | 16-19 | Outline, draft, peer review, revision |
| H: Finalization | 20-23 | Quality gate [GATE@20], archive, export with charts, citation verification |

## Gate Stages

Three stages require approval (use `--auto-approve` for fully autonomous mode):
- **Stage 5** (Literature Screen): Validates collected literature quality
- **Stage 9** (Experiment Design): Validates experiment protocol before code generation
- **Stage 20** (Quality Gate): Validates overall paper quality before export

## Experiment Modes

- `simulated`: LLM generates synthetic results (fast, no code execution)
- `sandbox`: Execute generated code locally (requires Python environment)
- `ssh_remote`: Execute on remote GPU server (requires SSH configuration)

## Key Files

| File | Purpose |
|------|---------|
| `config.yaml` | Pipeline configuration (LLM, experiment mode, etc.) |
| `config.researchclaw.example.yaml` | Configuration template |
| `researchclaw/cli.py` | CLI entry point |
| `researchclaw/pipeline/executor.py` | Stage execution logic |
| `researchclaw/pipeline/runner.py` | Pipeline orchestration |
| `researchclaw/experiment/validator.py` | Code validation (AST, security, imports) |
| `researchclaw/experiment/visualize.py` | Chart generation |

## Decision Guide

| Situation | Action |
|-----------|--------|
| User provides a clear topic | Run full pipeline with `--auto-approve` |
| User wants to review stages | Run without `--auto-approve`, pause at gates |
| Pipeline fails at a stage | Check error, fix config or retry from that stage with `--from-stage` |
| User wants iteration | Use `execute_iterative_pipeline()` with `max_iterations` |
| Experiment code fails | Validator auto-retries up to 3 times; if still failing, switch to `simulated` mode |

## Integration Platforms

ResearchClaw works with:
- **Claude Code**: Load via `.claude/skills/researchclaw/SKILL.md`
- **OpenClaw**: Read this `AGENTS.md` + `README.md` for bootstrapping
- **OpenCode**: Compatible skill format in `.claude/skills/`
- **Standalone**: Direct CLI or Python API usage

```

### File: RESEARCHCLAW_CLAUDE.md
```md
# ResearchClaw

## What This Is

ResearchClaw is a **fully autonomous academic research pipeline**. Given a research topic, it automatically completes literature review, hypothesis generation, experiment design, code generation & execution, result analysis, paper writing, peer review simulation, and final export — all through a 23-stage state machine driven by LLM calls.

## Quick Start

```bash
# 1. Copy and edit config
cp config.researchclaw.example.yaml config.yaml
# Fill in your LLM API key and base URL

# 2. Install
pip install -e .

# 3. Run
researchclaw run --topic "Your research topic" --auto-approve
```

Or programmatically:

```python
from researchclaw.pipeline.runner import execute_pipeline
from researchclaw.config import RCConfig
from researchclaw.adapters import AdapterBundle
from pathlib import Path

config = RCConfig.load("config.yaml", check_paths=False)
results = execute_pipeline(
    run_dir=Path("artifacts/my-run"),
    run_id="test-001",
    config=config,
    adapters=AdapterBundle(),
    auto_approve_gates=True,
)
```

## Project Structure

```
researchclaw/
├── __init__.py              # Version (0.3.2)
├── config.py                # RCConfig dataclass, validation, YAML loading
├── adapters.py              # AdapterBundle (recording stubs for notifications, OpenClaw bridge)
├── cli.py                   # CLI: `researchclaw run` and `researchclaw validate`
├── pipeline/
│   ├── stages.py            # 23-stage IntEnum, transitions, gate logic, rollback rules
│   ├── contracts.py         # StageContract for each stage (required_keys, produced_keys, gate flag)
│   ├── executor.py          # 23 stage executor functions + dispatch table (_STAGE_EXECUTORS)
│   └── runner.py            # execute_pipeline(), execute_iterative_pipeline()
├── llm/
│   └── client.py            # LLMClient (OpenAI-compatible), from_rc_config() factory
├── experiment/
│   ├── sandbox.py           # ExperimentSandbox (local subprocess execution)
│   ├── runner.py            # ExperimentRunner (run management)
│   ├── git_manager.py       # ExperimentGitManager
│   ├── validator.py         # AST syntax check, security scan, import check, auto-repair
│   └── visualize.py         # matplotlib charts (trajectory, comparison, timeline, iteration)
└── knowledge/
    └── base.py              # KnowledgeBase (markdown file write, 23-stage category map)
```

## 23-Stage Pipeline

```
Phase A: Research Scoping
  1: TOPIC_INIT           — Define research question, scope, constraints
  2: PROBLEM_DECOMPOSE    — Break into sub-problems, identify variables

Phase B: Literature Discovery
  3: SEARCH_STRATEGY      — Search strategy + data source verification
  4: LITERATURE_COLLECT   — Execute search, collect candidate papers
  5: LITERATURE_SCREEN    — Relevance + quality screening [GATE]
  6: KNOWLEDGE_EXTRACT    — Structured knowledge card extraction

Phase C: Knowledge Synthesis
  7: SYNTHESIS            — Topic clustering + research gap analysis
  8: HYPOTHESIS_GEN       — Generate falsifiable research hypotheses

Phase D: Experiment Design
  9: EXPERIMENT_DESIGN    — Design experiment protocol [GATE]
  10: CODE_GENERATION     — Generate executable experiment code (with validation)
  11: RESOURCE_PLANNING   — Resource scheduling, dependency ordering

Phase E: Experiment Execution
  12: EXPERIMENT_RUN      — Execute experiments (sandbox/remote/simulated)
  13: ITERATIVE_REFINE    — Edit→Run→Evaluate improvement loop

Phase F: Analysis & Decision
  14: RESULT_ANALYSIS     — Statistical analysis, generate experiment_summary.json + results_table.tex
  15: RESEARCH_DECISION   — PROCEED/PIVOT/ITERATE decision

Phase G: Paper Writing
  16: PAPER_OUTLINE       — Generate paper outline
  17: PAPER_DRAFT         — Write full draft (data-driven: uses real experiment metrics)
  18: PEER_REVIEW         — Simulated peer review
  19: PAPER_REVISION      — Revise based on review feedback

Phase H: Finalization
  20: QUALITY_GATE        — Automated quality scoring [GATE]
  21: KNOWLEDGE_ARCHIVE   — Archive findings and lessons learned
  22: EXPORT_PUBLISH      — Generate charts, export final artifacts
  23: CITATION_VERIFY     — Cross-check all citations against source data
```

## Gate Stages

Stages 5, 9, and 20 are **gate stages** requiring approval (or `--auto-approve`):
- Stage 5 (LITERATURE_SCREEN): reject → rollback to Stage 4
- Stage 9 (EXPERIMENT_DESIGN): reject → rollback to Stage 8
- Stage 20 (QUALITY_GATE): reject → rollback to Stage 16

## Configuration

Config file: `config.yaml` (or `config.researchclaw.example.yaml` as template).

Key sections:
- `project.name` / `project.mode` — Project identity
- `research.topic` — The research question
- `llm.base_url` / `llm.api_key` / `llm.primary_model` — LLM provider
- `experiment.mode` — `simulated`, `sandbox`, `docker`, `ssh_remote`, or `colab_drive`
- `experiment.sandbox.python_path` — Python interpreter for sandbox mode
- `security.hitl_required_stages` — Gate stage numbers (default: [5, 9, 20])
- `knowledge_base.root` — Directory for knowledge base files

## Important Constraints

- **Python 3.11+** required
- **Dependencies**: `pyyaml`, `rich`, `matplotlib` (for visualization)
- **LLM**: Any OpenAI-compatible API (tested with GPT-4o, GPT-5.x)
- Sandbox mode executes generated code locally — ensure `experiment.sandbox.python_path` points to a safe environment
- Code validation (AST + security scan) runs automatically before execution in Stage 10

## Testing

```bash
# Run all unit tests (2400+ tests)
python -m pytest tests/test_rc_*.py -q --tb=short

# Run real LLM E2E test (requires API key in config)
python tests/e2e_real_llm.py

# Validate config
researchclaw validate --config config.yaml
```

## Key APIs

```python
# Main pipeline entry
from researchclaw.pipeline.runner import execute_pipeline, execute_iterative_pipeline

# Single stage execution
from researchclaw.pipeline.executor import execute_stage

# Code validation
from researchclaw.experiment.validator import validate_code, security_scan, check_imports

# Chart generation
from researchclaw.experiment.visualize import generate_all_charts

# Config loading
from researchclaw.config import RCConfig, load_config
```

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for AutoResearchClaw
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: docs\agent_figure_and_benchmark_plan.md
```md
# Multi-Agent Figure Generation & Benchmark Selection — Task Requirements

> **Created**: 2026-03-15
> **Updated**: 2026-03-15
> **Status**: BenchmarkAgent IMPLEMENTED, FigureAgent IMPLEMENTED
> **Scope**: Two new multi-agent subsystems for AutoResearchClaw pipeline
>
> **Implementation Progress**:
> - [x] Part B: BenchmarkAgent — fully implemented (4 agents + orchestrator + config + pipeline integration + 43 tests)
> - [x] Part A: FigureAgent — fully implemented (5 agents + orchestrator + config + pipeline integration + 45 tests)
>
> **Key Research Findings (supplemental)**:
> - Papers With Code was shut down by Meta in July 2025; HuggingFace Hub API is now the primary dataset discovery source
> - AI Scientist v2 and MLR-Copilot both use pure LLM-driven dataset selection (no API search) — our API-based approach is more structured
> - MLE-bench (OpenAI) validates the pre-download + container-mount pattern (matches our `setup_only` network policy)
> - CodeSOTA (codesota.com) provides a lighter-weight benchmark database as an alternative to Papers With Code

---

## Executive Summary

当前 Pipeline 的图表生成和数据集/基准选择存在根本性缺陷：

**图表问题**（实测产出）：
- 每次固定只生成 2 张图（`method_comparison.png` + `experiment_comparison.png`）
- 图表类型单一：只有柱状图，无训练曲线、热力图、消融分析图等
- 数据无差异化：所有方法都显示 1.000，完全无信息量
- 样式简陋：默认 matplotlib 风格，远低于 AI 顶会标准
- 不适应实验内容：无论做什么研究都画一样的图
- DPI=150，不满足出版要求（300+ DPI）

**数据集/基准问题**：
- 当前仅通过 `dataset_guidance` 提示词列出预缓存数据集
- 无法根据研究领域动态搜索和选择最合适的 benchmark
- 无法自动下载非预缓存数据集
- 缺乏 baseline 方法的自动复现能力

**解决方案**：设计两个独立的多 Agent 子系统：
1. **FigureAgent** — 智能图表生成系统（6 个子 Agent 协作）
2. **BenchmarkAgent** — 数据集与基准选择系统（4 个子 Agent 协作）

---

## Part A: FigureAgent — 多 Agent 图表生成系统

### A.1 问题分析

#### 当前架构缺陷

```
现状：Stage 14 → visualize.py (5 个硬编码函数) → 固定 2 张图 → Stage 17/22 嵌入论文
```

| 问题 | 严重程度 | 说明 |
|------|---------|------|
| 图表类型固定 | Critical | 只有 bar chart 和 line chart，缺少 heatmap、scatter、violin、architecture diagram 等 |
| 不适应实验内容 | Critical | 知识蒸馏实验和 RL 实验画的图完全一样 |
| 无智能决策 | Critical | 不分析"应该画什么"，直接调用固定函数 |
| 数据正确性无验证 | High | 不验证图中数据是否与实验结果一致 |
| 样式不达标 | High | 默认 matplotlib，不符合学术论文视觉标准 |
| 无架构图能力 | High | 不能生成方法流程图 / 模型架构图（顶会 Figure 1 必备） |
| DPI 不足 | Medium | 150 DPI，出版要求 300+ |
| 无 VLM 审查 | Medium | 生成后不检查质量，直接用 |

#### 业界参考方案

| 项目 | 图表策略 | 核心创新 |
|------|---------|---------|
| AI Scientist v1 (Sakana) | 人工编写 `plot.py` 模板，LLM 不参与 | 可靠但不灵活 |
| AI Scientist v2 (Sakana) | LLM 自主生成画图代码 + VLM 审查反馈循环 | **VLM-as-critic**，首篇通过 ICLR workshop 审稿 |
| PlotGen (Adobe) | 三模态反馈：数值准确性 + 文本正确性 + 视觉质量 | **Tri-modal feedback**，MatPlotBench 最优 |
| PaperBanana (Google) | 3 阶段 pipeline：Caption 精炼 → 参考检索 → 迭代渲染 | **Caption sharpening** + 参考图库 |

### A.2 目标架构

```
                          ┌─────────────────────┐
                          │   FigureAgent        │
                          │   (Orchestrator)     │
                          └──────────┬──────────┘
                                     │
              ┌──────────┬───────────┼───────────┬──────────┐
              ▼          ▼           ▼           ▼          ▼
        ┌──────────┐┌──────────┐┌──────────┐┌──────────┐┌──────────┐
        │ Planner  ││ CodeGen  ││ Renderer ││ Critic   ││ Integra- │
        │ Agent    ││ Agent    ││ Agent    ││ Agent    ││ tor Agent│
        └──────────┘└──────────┘└──────────┘└──────────┘└──────────┘
              │          │           │           │          │
              ▼          ▼           ▼           ▼          ▼
         图表规划     代码生成     执行渲染     质量审查    论文嵌入
```

#### Agent 职责定义

**1. Orchestrator（编排器）**
- 接收：实验结果 JSON、论文草稿 markdown、研究主题描述
- 协调所有子 Agent 的执行顺序
- 管理迭代循环（Critic 不满意时回到 CodeGen）
- 输出：最终图表集合 + 嵌入指令

**2. Planner Agent（图表规划）**
- 输入：实验结果数据结构、论文 idea、研究领域
- 职责：
  - 分析实验数据，确定需要哪些图、每张图展示什么
  - 为每张图生成精确的 caption specification（非模糊描述）
  - 确定图表类型（bar / line / heatmap / scatter / architecture / ablation 等）
  - 确定布局（single / subplot / multi-panel）
  - 输出图表规划清单（JSON 格式）
- 关键规则：
  - 至少规划 4 张图：1 架构图 + 1 主结果图 + 1 消融图 + 1 分析图
  - 根据研究领域自动选择合适的图表类型
  - Caption sharpening：将模糊描述转化为精确视觉规范

**3. CodeGen Agent（代码生成）**
- 输入：Planner 输出的图表规划 + 实验数据
- 职责：
  - 为每张图生成独立的 Python 绘图脚本
  - 使用 SciencePlots 学术样式 (`plt.style.use(['science', 'ieee'])`)
  - 确保 colorblind-safe 配色
  - 300+ DPI 输出
  - 代码保存到 `charts/scripts/` 供复现
- 代码模板库：
  - 内置常用学术图表模板（training curve, bar comparison, heatmap, confusion matrix 等）
  - 新图表可基于模板扩展

**4. Renderer Agent（渲染执行）**
- 输入：CodeGen 生成的 Python 脚本
- 职责：
  - 在 Docker sandbox 中执行绘图脚本
  - 捕获执行错误并反馈给 CodeGen 修复
  - 验证输出文件存在且可读
  - 检查图像尺寸和分辨率

**5. Critic Agent（质量审查 — 三模态反馈）**
- 输入：渲染后的图像 + 源数据 + caption 规范
- 职责（三维度审查，参考 PlotGen）：
  - **数值准确性**：验证图中呈现的数值与源数据一致（读取 JSON → 对比图中数据点）
  - **文本正确性**：检查标题、坐标轴标签、图例是否准确完整
  - **视觉质量**：通过 VLM（如 GPT-4o vision）审查整体美观度、可读性、学术规范
- 输出：pass / fail + 具体修改建议
- 如果 fail：将反馈发回 CodeGen Agent，最多迭代 3 次

**6. Integrator Agent（论文嵌入）**
- 输入：通过审查的图表集合 + 论文草稿
- 职责：
  - 确定每张图在论文中的最佳位置
  - 生成 LaTeX figure 环境代码（支持 subfigure 多面板）
  - 生成交叉引用（`\ref{fig:xxx}`）
  - 确保图表在正确的 section（架构图在 Method，结果图在 Results）
  - 更新论文文本中的图表引用语句

### A.3 图表类型矩阵

根据研究领域和实验类型，Planner Agent 应遵循以下决策矩阵：

| 实验类型 | 必须包含的图表 | 可选图表 |
|---------|--------------|---------|
| **分类任务** | 精度对比 bar chart、confusion matrix | ROC 曲线、t-SNE 可视化 |
| **生成模型** | 生成样本 grid、FID/IS 曲线 | 插值可视化、attention map |
| **强化学习** | reward curve (mean±std shading)、episode length | 策略可视化、环境截图 |
| **知识蒸馏** | teacher-student 精度对比、知识迁移效率曲线 | 特征对齐热力图 |
| **NLP** | BLEU/ROUGE 对比表、attention heatmap | 样本输出对比 |
| **图神经网络** | 节点分类精度、图可视化 | 消息传递可视化 |
| **元学习** | few-shot 精度 vs shot 数曲线 | 任务适应速度 |
| **持续学习** | 遗忘率曲线、任务精度矩阵 | 表征漂移可视化 |
| **所有类型** | 消融分析 (grouped bar)、训练 loss 曲线 | 超参敏感性热力图 |

### A.4 样式规范

所有图表必须遵循以下学术出版标准：

```python
# 全局样式配置 (charts/style_config.py)
STYLE_CONFIG = {
    "matplotlib_style": ["science", "ieee"],   # SciencePlots
    "dpi": 300,                                 # 出版级
    "font_size": {"title": 12, "axis": 10, "tick": 8, "legend": 9},
    "figure_width": {
        "single_column": 3.5,   # IEEE single column (inches)
        "double_column": 7.0,   # IEEE double column
        "full_page": 7.0,       # Full width
    },
    "colors": "bright",          # colorblind-safe (Paul Tol)
    "line_styles": ["-", "--", "-.", ":"],  # 配合 B&W 打印
    "marker_styles": ["o", "s", "^", "D", "v", "P"],
    "error_bar_style": "shading",  # mean ± std 用阴影而非 error bar
    "format": "pdf",               # 矢量格式优先
    "fallback_format": "png",      # PNG 备用
}
```

### A.5 实现计划

#### 文件结构

```
researchclaw/
├── agents/
│   └── figure_agent/
│       ├── __init__.py
│       ├── orchestrator.py      # FigureAgent 主编排器
│       ├── planner.py           # Planner Agent
│       ├── codegen.py           # CodeGen Agent
│       ├── renderer.py          # Renderer Agent
│       ├── critic.py            # Critic Agent (三模态审查)
│       ├── integrator.py        # Integrator Agent
│       ├── templates/           # 图表代码模板库
│       │   ├── bar_comparison.py
│       │   ├── training_curve.py
│       │   ├── heatmap.py
│       │   ├── confusion_matrix.py
│       │   ├── scatter_plot.py
│       │   ├── ablation_grouped.py
│       │   ├── violin_box.py
│       │   └── multi_panel.py
│       └── style_config.py      # 全局样式配置
```

#### 开发任务清单

| ID | 任务 | 依赖 | 估计改动量 |
|----|------|------|-----------|
| FA-01 | 创建 `agents/figure_agent/` 目录结构和基础类 | 无 | 新建 |
| FA-02 | 实现 Planner Agent：图表规划逻辑 + 类型决策矩阵 | FA-01 | ~300 行 |
| FA-03 | 实现 CodeGen Agent：代码生成 + 模板库 | FA-01 | ~500 行 |
| FA-04 | 实现 Renderer Agent：sandbox 执行 + 错误处理 | FA-01, FA-03 | ~200 行 |
| FA-05 | 实现 Critic Agent：三模态审查（数值 / 文本 / VLM） | FA-01, FA-04 | ~400 行 |
| FA-06 | 实现 Integrator Agent：论文嵌入 + LaTeX subfigure 支持 | FA-01 | ~250 行 |
| FA-07 | 实现 Orchestrator：编排循环 + 最大迭代控制 | FA-02 ~ FA-06 | ~300 行 |
| FA-08 | 添加 SciencePlots 到 Docker 镜像 + 样式配置 | 无 | ~50 行 |
| FA-09 | 修改 executor.py：Stage 14 调用 FigureAgent 替代 `visualize.py` | FA-07 | ~100 行 |
| FA-10 | 修改 executor.py：Stage 17/22 使用 Integrator 输出 | FA-07 | ~100 行 |
| FA-11 | 修改 converter.py：支持 subfigure 和 PDF 格式 | FA-06 | ~80 行 |
| FA-12 | 添加图表代码模板库（8+ 模板） | FA-03 | ~600 行 |
| FA-13 | 测试：单元测试 + 集成测试 | FA-01 ~ FA-12 | ~400 行 |
| FA-14 | 向后兼容：保留 `visualize.py` 作为 fallback | FA-09 | ~30 行 |

#### Pipeline 集成点

```
Stage 12-13: 实验执行完成，生成 results.json
      │
      ▼
Stage 14: Result Analysis
      │── 调用 FigureAgent.orchestrate()
      │   ├── Planner: 分析 results.json → 图表规划
      │   ├── CodeGen: 生成绘图脚本 → charts/scripts/
      │   ├── Renderer: 执行脚本 → charts/*.pdf + charts/*.png
      │   ├── Critic: 审查图表质量 (max 3 iterations)
      │   └── 输出: charts/ 目录 + figure_manifest.json
      │
      ▼
Stage 17: Paper Draft
      │── Integrator: 读取 figure_manifest.json
      │   ├── 确定每张图的论文位置
      │   ├── 注入 markdown 图片引用 + caption
      │   └── 更新交叉引用文本
      │
      ▼
Stage 22: Paper Export
      │── 复制 charts/ 到 submission/
      │── converter.py 处理 subfigure 环境
      └── 最终 LaTeX 编译验证
```

---

## Part B: BenchmarkAgent — 多 Agent 数据集与基准选择系统

### B.1 问题分析

#### 当前架构缺陷

```
现状：dataset_guidance 提示词 (硬编码列表) + dataset_registry.yaml (静态清单) → LLM 自行选择
```

| 问题 | 严重程度 | 说明 |
|------|---------|------|
| 数据集选择不智能 | Critical | 仅列出预缓存数据集，LLM 可能选择不合适的 benchmark |
| 无领域适配 | Critical | 不根据研究领域搜索该领域的标准 benchmark |
| 无最新性保证 | High | 不检查是否有更新、更好的 benchmark 可用 |
| baseline 无法复现 | High | 不提供已有方法的参考实现 / 预训练权重 |
| 下载路径硬编码 | Medium | 非预缓存数据集无法自动获取 |
| 无数据集验证 | Medium | 不验证下载的数据集是否完整、格式正确 |

#### 理想工作流

一个好的数据集/基准选择流程应该：
1. **理解研究问题** → 确定评估维度（分类精度？生成质量？推理速度？）
2. **搜索领域标准** → 查找该领域顶会论文常用的 benchmark
3. **评估适用性** → 数据集大小、难度、License、可获取性
4. **获取数据** → 自动下载或生成下载脚本
5. **获取 baseline** → 找到对比方法的开源实现或预训练权重
6. **验证完整性** → 确认数据集可正常加载和使用

### B.2 目标架构

```
                          ┌─────────────────────┐
                          │  BenchmarkAgent      │
                          │  (Orchestrator)      │
                          └──────────┬──────────┘
                                     │
              ┌──────────┬───────────┼───────────┐
              ▼          ▼           ▼           ▼
        ┌──────────┐┌──────────┐┌──────────┐┌──────────┐
        │ Surveyor ││ Selector ││ Acquirer ││ Validator│
        │ Agent    ││ Agent    ││ Agent    ││ Agent    │
        └──────────┘└──────────┘└──────────┘└──────────┘
              │          │           │           │
              ▼          ▼           ▼           ▼
         领域调研     选择决策     数据获取     验证确认
```

#### Agent 职责定义

**1. Orchestrator（编排器）**
- 接收：研究主题、假设、实验设计方案
- 协调 4 个子 Agent 的执行
- 输出：`benchmark_plan.json`（包含数据集列表、下载脚本、baseline 方案）

**2. Surveyor Agent（领域调研）**
- 输入：研究主题关键词、相关文献列表
- 职责：
  - 搜索 Papers With Code 的领域 benchmark 排行榜
  - 搜索 HuggingFace Datasets 的相关数据集
  - 搜索 OpenML、Kaggle 的相关 benchmark
  - 分析近 2 年顶会论文（ICML、NeurIPS、ICLR）使用的数据集
  - 汇总领域标准 benchmark 清单（含引用频次、数据规模、难度级别）
- 输出：`survey_results.json` — 候选 benchmark 列表（按推荐度排序）
- 数据源优先级：
  1. Papers With Code (Benchmarks API)
  2. HuggingFace Datasets Hub
  3. torchvision / torchaudio / torchtext 内置
  4. 顶会论文附录中的数据集描述

**3. Selector Agent（选择决策）**
- 输入：survey_results.json + 实验约束（GPU 内存、时间预算、网络可用性）
- 职责：
  - 根据约束过滤不可行的数据集（太大 / 需要申请 / License 不兼容）
  - 考虑 Docker sandbox 已缓存的数据集（优先使用）
  - 选择 primary benchmark（必须是领域标准）+ secondary benchmarks（补充验证）
  - 选择 baseline 方法（至少 2 个有开源实现的对比方法）
  - 生成选择理由文档（供论文 Experimental Setup section 使用）
- 约束规则：
  - Tier 1（已缓存）：无网络需求，最优先
  - Tier 2（torchvision/HF datasets 可直接下载）：需 setup 阶段网络
  - Tier 3（需自定义下载脚本）：仅在 `network_policy: full` 时可用
- 输出：`selected_benchmarks.json` + `baseline_methods.json`

**4. Acquirer Agent（数据获取）**
- 输入：selected_benchmarks.json
- 职责：
  - 生成 `setup.py` 中的数据集下载代码
  - 为每个数据集生成加载 boilerplate 代码
  - 为 baseline 方法生成安装和调用代码
  - 处理 HuggingFace `datasets.load_dataset()` / `torchvision.datasets` 等接口
  - 生成 `requirements.txt` 中需要额外安装的包
- 输出：
  - `data_loading_snippets.py` — 数据加载代码片段（注入 CodeAgent）
  - `baseline_snippets.py` — baseline 调用代码片段
  - `setup.py` 追加内容 — 下载脚本

**5. Validator Agent（验证确认）**
- 输入：Acquirer 生成的下载/加载代码
- 职责：
  - 验证数据集 API 调用语法正确
  - 验证数据集分割（train/val/test）存在
  - 验证数据格式与实验代码兼容
  - 验证 baseline 方法可运行
  - 如果验证失败，反馈给 Acquirer 修复
- 输出：validation_report.json

### B.3 知识库设计

BenchmarkAgent 需要一个结构化知识库来支持决策：

```yaml
# researchclaw/data/benchmark_knowledge.yaml

domains:
  image_classification:
    standard_benchmarks:
      - name: CIFAR-10/100
        source: torchvision
        tier: 1  # 已缓存
        difficulty: easy/medium
        use_when: "小规模验证、快速原型"
      - name: ImageNet-1K
        source: torchvision
        tier: 3  # 需要下载 ~150GB
        difficulty: hard
        use_when: "大规模验证、与 SOTA 对比"
    common_baselines:
      - name: ResNet-50
        source: "torchvision.models.resnet50(pretrained=True)"
        paper: "He et al., 2016"
      - name: ViT-B/16
        source: "timm.create_model('vit_base_patch16_224', pretrained=True)"
        paper: "Dosovitskiy et al., 2021"

  reinforcement_learning:
    standard_benchmarks:
      - name: Gymnasium (MuJoCo)
        source: "gymnasium[mujoco]"
        tier: 2
      - name: Atari
        source: "gymnasium[atari]"
        tier: 2
    common_baselines:
      - name: PPO
        source: "stable-baselines3"
        paper: "Schulman et al., 2017"

  # ... 更多领域
```

### B.4 实现计划

#### 文件结构

```
researchclaw/
├── agents/
│   └── benchmark_agent/
│       ├── __init__.py
│       ├── orchestrator.py      # BenchmarkAgent 主编排器
│       ├── surveyor.py          # Surveyor Agent (领域调研)
│       ├── selector.py          # Selector Agent (选择决策)
│       ├── acquirer.py          # Acquirer Agent (数据获取)
│       ├── validator.py         # Validator Agent (验证确认)
│       └── knowledge_base.py    # 知识库加载和查询
├── data/
│   ├── benchmark_knowledge.yaml # 领域 benchmark 知识库
│   └── dataset_registry.yaml    # 已有数据集注册表 (保留)
```

#### 开发任务清单

| ID | 任务 | 依赖 | 估计改动量 |
|----|------|------|-----------|
| BA-01 | 创建 `agents/benchmark_agent/` 目录结构和基础类 | 无 | 新建 |
| BA-02 | 编写 `benchmark_knowledge.yaml` 知识库（覆盖 10+ 领域） | 无 | ~500 行 YAML |
| BA-03 | 实现 Surveyor Agent：Papers With Code API + HF Datasets 搜索 | BA-01 | ~350 行 |
| BA-04 | 实现 Selector Agent：约束过滤 + Tier 匹配 + 选择逻辑 | BA-01, BA-02 | ~300 行 |
| BA-05 | 实现 Acquirer Agent：代码生成 + 下载脚本 | BA-01, BA-04 | ~350 行 |
| BA-06 | 实现 Validator Agent：语法/可用性验证 | BA-01, BA-05 | ~250 行 |
| BA-07 | 实现 Orchestrator：编排 + 迭代修复 | BA-02 ~ BA-06 | ~250 行 |
| BA-08 | 修改 executor.py：Stage 6/7 调用 BenchmarkAgent | BA-07 | ~150 行 |
| BA-09 | 修改 executor.py：将 benchmark_plan 注入 CodeAgent | BA-07 | ~100 行 |
| BA-10 | 更新 prompts.py：基于 BenchmarkAgent 输出动态构建提示词 | BA-07 | ~100 行 |
| BA-11 | 测试：单元测试 + 集成测试 | BA-01 ~ BA-10 | ~300 行 |
| BA-12 | 向后兼容：保留 `dataset_registry.yaml` 作为 fallback | BA-08 | ~30 行 |

#### Pipeline 集成点

```
Stage 3: Topic Initialization
      │── 研究主题确定
      ▼
Stage 4-5: Literature Collection & Screening
      │── 文献列表生成
      ▼
Stage 6: Hypothesis Generation
      │── 调用 BenchmarkAgent.orchestrate()
      │   ├── Surveyor: 搜索领域标准 benchmark
      │   ├── Selector: 根据约束选择最优 benchmark + baseline
      │   ├── Acquirer: 生成下载/加载代码
      │   └── Validator: 验证代码可执行
      │── 输出: benchmark_plan.json
      ▼
Stage 7: Experiment Design
      │── benchmark_plan.json 注入实验
... [TRUNCATED]
```

### File: docs\BUG_FIX_DOCUMENT_20260316.md
```md
# Bug Fix Document — AutoResearchClaw Pipeline

> 生成日期：2026-03-16
> 反馈来源：2 位测试者（user1: CV 方向 / GPU 环境, user2: Windows 环境）
> 总计问题：9 个

## 📊 总览

| 分类 | 数量 |
|------|------|
| 🔴 确认的 Bug（需修复） | **4** |
| 🟠 架构改进（强烈建议） | **2** |
| 🔵 功能需求 | **3** |

## 🔥 修复优先级

| 优先级 | ID | 问题 | 阶段 | 涉及文件 |
|--------|----|------|------|----------|
| 🔴 CRITICAL | BUG-001 | 论文硬件信息与实际不一致 | PAPER_DRAFT (17) | `executor.py`, `prompts.py` |
| 🔴 CRITICAL | BUG-002 | Windows 环境 Docker 不可用导致实验链式失败 | EXPERIMENT_RUN (12) | `factory.py`, `docker_sandbox.py` |
| 🔴 HIGH | BUG-003 | 论文内容自相矛盾（承诺评测但未执行） | PAPER_DRAFT (17), PEER_REVIEW (18) | `executor.py`, `prompts.py` |
| 🔴 HIGH | BUG-004 | 生成代码缺少数值稳定性防护（NaN/Inf） | CODE_GENERATION (10) | `code_agent.py`, `prompts.py` |
| 🟠 HIGH | ARCH-001 | Stage 17 过于严格的 hard block 策略 | PAPER_DRAFT (17) | `executor.py` |
| 🟠 HIGH | ARCH-002 | Idea 降级时不询问用户确认 | EXPERIMENT_DESIGN (9), RESEARCH_DECISION (15) | `executor.py`, `stages.py` |

---

## 确认的 Bug — 详细修复方案

### 🔴 `BUG-001` — 论文硬件信息与实际机器不一致

| 字段 | 内容 |
|------|------|
| **严重程度** | CRITICAL |
| **所属阶段** | PAPER_DRAFT (Stage 17) |
| **报告者** | user1 |

**问题描述：**
论文中声称使用 A100 GPU 训练，但测试者实际机器上是 A5000。Pipeline 在 Stage 1 检测了硬件并保存到 `hardware_profile.json`，但在论文生成阶段完全没有利用这个信息来约束 LLM 输出。

**根因分析：**
- `executor.py` 第 1226-1233 行：Stage 1 (TOPIC_INIT) 检测硬件，保存 `hardware_profile.json`，包含 `gpu_name`、`vram_gb` 等
- `executor.py` 第 2352-2391 行：硬件信息 **仅** 用于 CODE_GENERATION 阶段的代码生成 hints
- `executor.py` 第 5776-5848 行：PAPER_DRAFT 阶段构建 prompt 时，**没有注入硬件 profile 信息**
- LLM 在缺少约束的情况下会「幻觉」出常见的高端硬件名称（如 A100）

**涉及文件：**
- `researchclaw/pipeline/executor.py`（PAPER_DRAFT 阶段的 prompt 构建部分，约第 5776-5960 行）
- `researchclaw/prompts.py`（paper writing prompt 模板）

**修复方案：**
1. 在 PAPER_DRAFT 阶段的 prompt 构建中，读取 `stage-01/hardware_profile.json`
2. 将实际硬件信息（GPU 型号、VRAM、CPU 等）作为 **硬性约束** 注入 prompt，例如：
   ```
   HARDWARE CONSTRAINT: The experiments were run on the following hardware:
   - GPU: {gpu_name} ({vram_gb} GB VRAM)
   - CPU: {cpu_info}
   You MUST use this exact hardware specification in the paper. Do NOT substitute with other GPU models.
   ```
3. 在 PEER_REVIEW (Stage 18) 的 prompt 中增加一条审核规则：验证 paper 中提到的硬件是否与 `hardware_profile.json` 一致

**修复后预期行为：**
论文中的硬件描述必须与实际运行环境一致。

<details>
<summary>原始反馈证据</summary>

> 然后就是paper和实验中有一些misalign的地方，比如paper里写说用的A100，实际上机器里的是A5000
</details>

---

### 🔴 `BUG-002` — Windows 环境下 Docker 不可用导致实验链式失败

| 字段 | 内容 |
|------|------|
| **严重程度** | CRITICAL |
| **所属阶段** | EXPERIMENT_RUN (Stage 12) → 链式影响到 Stage 13, 14, 17 |
| **报告者** | user2 |

**问题描述：**
在 Windows 环境下，Docker 不可用时 Pipeline 直接崩溃（`[WinError 2] The system cannot find the file specified`），导致所有后续阶段连锁失败。用户最终看到的是 Stage 17 的误导性错误「没有实验数据无法写论文」，完全看不到真正的根因。

**根因分析：**
- `experiment/factory.py` 第 25-29 行：当 `config.experiment.mode == "docker"` 时调用 `DockerSandbox.check_docker_available()`，如果 Docker 不可用直接 raise `RuntimeError`，**没有自动 fallback 到 subprocess sandbox**
- `docker_sandbox.py` 第 337、366 行：Docker volume mount 使用 POSIX 风格路径（如 `{staging_dir}:/workspace`），在 Windows 上可能导致挂载失败
- **链式失败：** Stage 12 crash → 无 metrics → Stage 13 空跑（`refine_sandbox_v1` 到 `v9` 都失败） → Stage 14 空 `experiment_summary.json` → Stage 17 hard block
- 用户看到的错误完全不提 Docker，只说「no metrics」，非常误导

**涉及文件：**
- `researchclaw/experiment/factory.py`（第 25-29 行，sandbox 创建逻辑）
- `researchclaw/experiment/docker_sandbox.py`（第 337、366、384 行，路径和命令构建）
- `researchclaw/pipeline/executor.py`（第 6000-6020 行，Stage 17 hard block）

**修复方案：**
1. `factory.py`：当 Docker 不可用时，自动 fallback 到 subprocess sandbox 模式，而不是 raise RuntimeError。增加日志 warning 告知用户：
   ```python
   if not DockerSandbox.check_docker_available():
       logger.warning("Docker not available, falling back to subprocess sandbox mode")
       return SubprocessSandbox(...)
   ```
2. `docker_sandbox.py`：修复 Windows 路径兼容性问题，使用 `pathlib.PureWindowsPath` 或 `os.path` 正确处理跨平台路径
3. 在 Stage 12 的错误信息中明确指出是 Docker 问题，而不是让错误沿链传播变成「no metrics」

**修复后预期行为：**
Windows 用户即使没有 Docker，Pipeline 也能通过 subprocess sandbox 完成实验。即使实验部分失败，错误信息应清晰指向根因。

<details>
<summary>原始反馈证据</summary>

> 我跑了两次 两次都有stage fail 最后没有生成报告

压缩包中 `experiment_summary.json` stderr: `[WinError 2] The system cannot find the file specified`
`pipeline_summary.json`: `"final_status": "failed"`, `"stages_failed": 1`
`stage-17/paper_draft.md`: `Experiment stage produced no metrics (status: failed/timeout). Cannot write a paper without real experimental data.`
</details>

---

### 🔴 `BUG-003` — 论文内容自相矛盾（承诺评测数据集但未实际执行）

| 字段 | 内容 |
|------|------|
| **严重程度** | HIGH |
| **所属阶段** | PAPER_DRAFT (Stage 17), PEER_REVIEW (Stage 18) |
| **报告者** | user1 |

**问题描述：**
论文前半部分按照用户的 topic 描述声称会在 MME、DocVQA、TextVQA 等数据集上评测，但实际实验阶段因为环境原因未能完成这些评测。论文后半部分在 Limitation 中又说「没有在这些数据集上评估」，形成自相矛盾。

**根因分析：**
- `prompts.py` 第 2006-2018 行：有 EVIDENCE-BOUNDING RULES（Rule 7-9），但这些只是 prompt 中的 **建议**，LLM 可以忽略
- `executor.py` 第 5647-5715 行：`_detect_result_contradictions()` 函数检测 null/negative results，但只生成 advisory text 注入 prompt，**不做硬性阻断**
- `executor.py` 第 6432-6443 行：PEER_REVIEW 阶段收集 `actual_run_count` 作为 evidence，但 **没有自动扫描 paper 文本提取声称的数据集列表并与实际评测记录对比**
- 核心问题：**缺少 claim-evidence 的自动对齐验证**

**涉及文件：**
- `researchclaw/pipeline/executor.py`（第 5647-5715 行、5944-5956 行、6432-6443 行）
- `researchclaw/prompts.py`（第 2006-2049 行、2124-2138 行）

**修复方案：**
1. 在 PAPER_DRAFT 阶段的 prompt 中，**明确列出** 实际完成评测的数据集和指标（从 `experiment_summary.json` 提取），硬性要求 LLM **只能**声称在这些数据集上进行了评测：
   ```
   ACTUAL EVALUATED DATASETS: [ImageNet-val (reconstruction)]
   You MUST NOT claim evaluation on any dataset not listed above.
   If the original research plan included additional datasets that were not evaluated,
   explain this honestly in the Limitations section WITHOUT first claiming you did evaluate them.
   ```
2. 在 PEER_REVIEW (Stage 18) 增加一个专项检查：自动提取 paper 中所有提到的 benchmark/dataset 名称，与 `experiment_summary.json` 中的实际 metrics keys 对比，不一致则标记为 CRITICAL discrepancy
3. 在 PAPER_REVISION (Stage 19) 中把这些 discrepancy 作为必须修改的 reviewer comment

**修复后预期行为：**
论文中不会出现「前面说评测了 X，后面说没评测 X」的自相矛盾。所有评测声明必须有实验数据支撑。

<details>
<summary>原始反馈证据</summary>

> 以及就是paper中有一些自相矛盾的地方，比如前面按照我的要求，说会在哪几个数据集上面进行评估，后面又没有测，然后在limitation说我们没有在这几个数据集上评估
</details>

---

### 🔴 `BUG-004` — 生成代码缺少数值稳定性防护（NaN/Inf 导致实验提前终止）

| 字段 | 内容 |
|------|------|
| **严重程度** | HIGH |
| **所属阶段** | CODE_GENERATION (Stage 10), ITERATIVE_REFINE (Stage 13) |
| **报告者** | user1 |

**问题描述：**
实验训练过程中出现 `loss = inf` → `loss = nan` 的数值爆炸，触发 harness 的 NaN 检测后实验提前终止。代码生成阶段没有在生成的训练代码中加入数值稳定性保护。

**根因分析：**
- `code_agent.py`：**完全没有** 关于数值稳定性的 prompt 指令。4 个阶段（Planning → Code Generation → Execution-in-the-Loop → Multi-Agent Review）都不检查 NaN guard
- `experiment/harness_template.py` 第 45-62 行：有 `check_value()` 做 NaN/Inf 检测，但这是 **opt-in 机制**——只有生成代码主动调用 `self.check_value(loss, "loss")` 才有效
- `executor.py` 第 779-900 行：`_detect_runtime_issues()` 在运行 **之后** 检测 NaN，但此时实验已经失败了
- `executor.py` 第 3915-3956 行：Stage 13 检测到 NaN 后调用 LLM 做 `iterative_repair`，但修复质量不稳定

**涉及文件：**
- `researchclaw/pipeline/code_agent.py`（prompt 构建，所有阶段）
- `researchclaw/prompts.py`（代码生成相关 prompt）
- `researchclaw/experiment/harness_template.py`（第 45-62 行）

**修复方案：**
1. 在 `code_agent.py` 的代码生成 prompt 中，增加 **强制性** 数值稳定性要求：
   ```
   NUMERICAL STABILITY REQUIREMENTS (MANDATORY):
   - Add gradient clipping (max_norm=1.0) to all optimizer steps
   - Check loss for NaN/Inf before backward pass: if not math.isfinite(loss): skip this batch
   - Use torch.amp.GradScaler for mixed precision training if applicable
   - Add learning rate warmup for the first 5-10% of training steps
   - Use self.check_value(loss, "loss") from experiment harness for NaN tracking
   ```
2. 在 `harness_template.py` 中，将 `check_value()` 改为 **自动 hook** 而非 opt-in——在 `finalize()` 中自动检查 metrics 是否为 finite
3. 在 Multi-Agent Review 阶段（`code_agent.py` Phase 4）增加数值稳定性作为必审项

**修复后预期行为：**
生成的训练代码默认包含 gradient clipping 和 NaN guard，训练过程中数值爆炸能被及时 catch 并恢复，而不是直接终止。

<details>
<summary>原始反馈证据</summary>

> 好像是他的代码写错了之类的

压缩包中 `experiment_summary.json` stderr:
```
WARNING: loss = inf (non-finite, skipped)
WARNING: loss = nan (non-finite, skipped)
WARNING: loss = nan (non-finite, skipped)
WARNING: loss = nan (non-finite, skipped)
WARNING: loss = nan (non-finite, skipped)
FAIL: Too many NaN/Inf values detected. Stopping experiment early.
```
</details>

---

## 架构改进 — 强烈建议

### 🟠 `ARCH-001` — Stage 17 (PAPER_DRAFT) 过于严格的 hard block 策略

| 字段 | 内容 |
|------|------|
| **严重程度** | HIGH |
| **所属阶段** | PAPER_DRAFT (Stage 17) |
| **报告者** | user2（链式影响） |

**问题描述：**
当实验阶段没有产出完整 metrics 时，Stage 17 直接 FAILED，不尝试用已有数据写论文。这导致前面 1-16 阶段的全部成果被浪费。

**根因分析：**
- `executor.py` 第 6000-6020 行：当 `has_real_metrics == False` 且 domain 为 empirical 时，直接返回 `StageStatus.FAILED`
- Stage 13 (ITERATIVE_REFINE) 的中间迭代可能产出了部分有效 metrics，但 Stage 17 只看 `experiment_summary.json` 的 final best_run

**涉及文件：**
- `researchclaw/pipeline/executor.py`（第 6000-6020 行）

**修复方案：**
将 hard block 改为 soft degradation：
1. 如果有部分 metrics（即使不完整），用已有数据写论文
2. 在 prompt 中明确告知 LLM 数据不完整，要求在 Abstract 和 Limitations 中如实说明
3. 只有在 **完全没有任何数据**（甚至没有 stage-07 synthesis 和 stage-08 hypotheses）的极端情况下才 hard block
4. 在输出的 `paper_draft.md` 头部加 warning 标记，方便后续阶段识别

**修复后预期行为：**
实验部分失败时，Pipeline 仍能生成一篇带有诚实 Limitations 的论文，用户至少得到有价值的输出。

---

### 🟠 `ARCH-002` — Idea 被降级到弱版本时不询问用户

| 字段 | 内容 |
|------|------|
| **严重程度** | HIGH |
| **所属阶段** | EXPERIMENT_DESIGN (Stage 9), RESEARCH_DECISION (Stage 15) |
| **报告者** | user1 |

**问题描述：**
用户给了一个复杂的 strong idea（如 VAE+ViT 统一编码器 + 多数据集评测），Pipeline 因资源限制（数据集不可用、GPU 不够、环境配不好）自动降级到 weaker 版本，但不通知或征求用户意见。用户认为降级后的研究「变得没啥意义」。

**根因分析：**
- `executor.py` 第 2220-2236 行：LLM 生成的实验计划无效时，使用 topic-derived fallback，**不询问用户**
- `executor.py` 第 4618-4640 行：RESEARCH_DECISION 检测 degenerate cycle 时只给 LLM advisory，**不暂停**
- `stages.py` 第 109-115 行：GATE_STAGES 只包含 Stage 5、9、20，不包含 Stage 15
- `agents/benchmark_agent/orchestrator.py` 第 314-322 行：BenchmarkAgent 验证失败时 silent retry，最终 silent proceed

**涉及文件：**
- `researchclaw/pipeline/executor.py`（第 2220-2236 行、4618-4640 行）
- `researchclaw/pipeline/stages.py`（GATE_STAGES 定义）
- `researchclaw/agents/benchmark_agent/orchestrator.py`（第 314-322 行）

**修复方案：**
1. 在 EXPERIMENT_DESIGN (Stage 9) 中，当检测到 significant downgrade（如：用户要求的数据集不可用、GPU 不满足要求、关键组件被简化）时，生成一个 **downgrade summary** 并暂停等待用户确认
2. 在 RESEARCH_DECISION (Stage 15) 中，将 REFINE → weaker idea 的决策标记为 GATE，需要用户 approve
3. 可以通过 `auto_approve` 参数让用户选择是否跳过这些确认（保持向后兼容）

**修复后预期行为：**
Pipeline 在降级研究方案前通知用户，用户可以选择：接受降级、提供更多资源（如更大的 GPU）、或终止当前 run。

<details>
<summary>原始反馈证据</summary>

> 对，还有就是比如我提出了一个相对strong的idea，而他因为各种原因（比如数据集找不到，环境配不好，gpu不够）之类的，给我fallback到weaker的idea之后，我感觉这个时候应该询问一下用户要不要继续跑
>
> 因为很多时候他继续跑的内容就会变得没啥意义
</details>

---

## 功能需求

### 🔵 `FEAT-001` — 论文生成后增加一致性反馈循环

- **报告者：** user1
- **描述：** 在论文生成之后，增加专门的 consistency check，检查 paper 中的声明与实际实验结果是否一致
- **建议：** 可以在 PEER_REVIEW (Stage 18) 的 prompt 中增加 claim-evidence alignment 专项检查。或者在 Stage 17 和 18 之间加一个轻量级的自动验证步骤

<details>
<summary>原始反馈</summary>

> 感觉这个可以在paper生成之后，加一些相关的consistence feedback之类的？
</details>

### 🔵 `FEAT-002` — 从 Related Works 的 GitHub 学习 Common Practice

- **报告者：** user1
- **描述：** 当前 Pipeline 的 literature 阶段只读论文，不看对应的开源代码。用户建议访问 related works 的 GitHub repo，学习 paper 中不会写的实现细节（tricks、common practice），缓解论文内容过于古老的问题
- **建议：** 在 KNOWLEDGE_EXTRACT (Stage 6) 或 EXPERIMENT_DESIGN (Stage 9) 增加 GitHub repo 分析能力。可以用 GitHub API 搜索 related works 的 repo，提取 README、主要代码结构、训练配置等信息

<details>
<summary>原始反馈</summary>

> 对就是我觉得即使不拿来用，visit related works的github也是有必要的，这样可以看到其他工作的common practice（一些不会在paper中出现的细节），应该会挺有用的。感觉可以缓解一下paper内容过于古老的问题
</details>

### 🔵 `FEAT-003` — 代码应该复用 Related Works 的框架

- **报告者：** user1
- **描述：** 当前代码都是 LLM 从零写的简单文件，用户建议从 most related works 中选一个合适的框架来用，就像真实研究中的做法
- **建议：** 可以在 BenchmarkAgent 或 CODE_GENERATION 阶段增加框架选择逻辑——从相关论文的开源实现中挑选合适的 codebase 作为起点，而不是从零生成。这是一个较大的改动，可以作为长期目标

<details>
<summary>原始反馈</summary>

> 以及他现在写的代码都比较简单，都是自己写几个文件对吧。我在想或许可以从most related works里面选一个合适的框架来用？我们平时也是这样的对吧。当然这个比较复杂，可以先不考虑
</details>

---

## 附录：按测试者分组

### 测试者：`user1`
- **学科/领域：** 计算机视觉（CV），统一图像编解码器
- **运行环境：** GPU 服务器（A5000），使用 Codex 监控
- **总计问题：** 6
- **确认 Bug：** 3（BUG-001, BUG-003, BUG-004）
- **架构改进：** 1（ARCH-002）
- **功能需求：** 3（FEAT-001, FEAT-002, FEAT-003）

| ID | 问题 | 状态 | 严重程度 |
|----|------|------|---------|
| BUG-001 | 论文硬件信息与实际不一致 | confirmed | CRITICAL |
| BUG-003 | 论文内容自相矛盾 | confirmed | HIGH |
| BUG-004 | 代码缺少数值稳定性防护 | confirmed | HIGH |
| ARCH-002 | Idea 降级不询问用户 | confirmed | HIGH |
| FEAT-001 | 一致性反馈循环 | feature_request | — |
| FEAT-002 | 从 GitHub 学习 common practice | feature_request | — |
| FEAT-003 | 复用 related works 框架 | feature_request | — |

### 测试者：`user2`
- **学科/领域：** 未知（topic 与纳米药物递送相关）
- **运行环境：** Windows
- **总计问题：** 2
- **确认 Bug：** 1（BUG-002）
- **架构改进：** 1（ARCH-001）

| ID | 问题 | 状态 | 严重程度 |
|----|------|------|---------|
| BUG-002 | Windows Docker 链式失败 | confirmed | CRITICAL |
| ARCH-001 | Stage 17 过于严格的 hard block | confirmed | HIGH |

---

## 修复执行指引

> 本文档设计为可由另一台机器上的 Claude Code agent 直接读取并执行修复。
> 建议按优先级从上到下依次修复，每修复一个 Bug 运行相关测试验证。

**修复顺序建议：**
1. BUG-002（Docker fallback）→ 解除 Windows 用户的完全阻塞
2. BUG-001（硬件一致性）→ 简单修复，prompt 注入即可
3. BUG-004（NaN guard）→ prompt 层面修复，影响面大
4. BUG-003（claim-evidence 对齐）→ 需要新增验证逻辑
5. ARCH-001（soft degradation）→ 改变 Stage 17 策略
6. ARCH-002（用户确认 Gate）→ 需要状态机和 Gate 逻辑调整

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
