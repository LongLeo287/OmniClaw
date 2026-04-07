---
id: metaclaw
type: knowledge
owner: OA_Triage
---
# metaclaw
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

<img src="assets/new_logo2.png" alt="MetaClaw" width="600">

<br/>

# Just talk to your agent — it learns and *EVOLVES*.

<p>Inspired by how brains learn. Meta-learn and evolve your 🦞 from every conversation in the wild. No GPU required.
  
<br/>


<img src="assets/metaclaw_mainfig_v2.png" alt="MetaClaw Architecture" width="800">

<br/>


<p>
  <a href="https://arxiv.org/abs/2603.17187"><img src="https://img.shields.io/badge/📄_Technical_Report-purple?style=flat-square" alt="Tech Report" /></a>
  <a href="https://github.com/aiming-lab/MetaClaw"><img src="https://img.shields.io/badge/github-MetaClaw-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat&labelColor=555" alt="License MIT"></a>
  <img src="https://img.shields.io/badge/⚡_Fully_Async-yellow?style=flat&labelColor=555" alt="Fully Async" />
  <img src="https://img.shields.io/badge/☁️_No_GPU_Cluster-blue?style=flat&labelColor=555" alt="No GPU Cluster" />
  <img src="https://img.shields.io/badge/🛠️_Skill_Evolution-orange?style=flat&labelColor=555" alt="Skill Evolution" />
  <img src="https://img.shields.io/badge/🚀_One--Click_Deploy-green?style=flat&labelColor=555" alt="One-Click Deploy" />
</p>

[🇨🇳 中文](./assets/README_ZH.md) • [🇯🇵 日本語](./assets/README_JA.md) • [🇰🇷 한국어](./assets/README_KO.md) • [🇫🇷 Français](./assets/README_FR.md) • [🇩🇪 Deutsch](./assets/README_DE.md) • [🇪🇸 Español](./assets/README_ES.md) • [🇧🇷 Português](./assets/README_PT.md) • [🇷🇺 Русский](./assets/README_RU.md) • [🇮🇹 Italiano](./assets/README_IT.md) • [🇻🇳 Tiếng Việt](./assets/README_VI.md) • [🇦🇪 العربية](./assets/README_AR.md) • [🇮🇳 हिन्दी](./assets/README_HI.md)

<br/>

[Overview](#-overview) • [Quick Start](#-quick-start) • [Multi-Claw Support](#-multi-claw-support) • [Configuration](#️-configuration) • [Skills Mode](#-skills-mode) • [RL Mode](#-rl-mode) • [Auto Mode](#-auto-mode-default) • [Memory](#-memory) • [Citation](#-citation)

</div>

---

<div align="center">

### Two commands. That's it.
</div>

```bash
metaclaw setup              # one-time config wizard
metaclaw start              # default: auto mode — skills + scheduled RL training
metaclaw start --mode rl    # RL without scheduler (trains immediately on full batch)
metaclaw start --mode skills_only  # skills only, no RL (no Tinker needed)
```

<div align="center">
<img src="assets/metaclaw.gif" alt="MetaClaw demo" width="700">
</div>

---

## 🔥 News

- **[03/25/2026]** **v0.4.0** — Contexture layer: MetaClaw now persists cross-session memory for users and projects. Relevant facts, preferences, and project history are automatically retrieved and injected into prompts. Includes adaptive memory policy, background consolidation, and an optional memory sidecar service.
- **[03/24/2026]** **v0.3.3** — One-click OpenClaw plugin: MetaClaw now ships as a native OpenClaw extension — drop the folder into OpenClaw's extensions, run one command, and everything is set up automatically.
- **[03/18/2026]** Our technical report "[MetaClaw: Just Talk -- An Agent That Meta-Learns and Evolves in the Wild](https://arxiv.org/pdf/2603.17187)" is out! **🏆 Ranked No. 1** on [HuggingFace Daily Papers](https://huggingface.co/papers/2603.17187)! Check it out!
- **[03/16/2026]** **v0.3.2** — Multi-claw support: IronClaw, PicoClaw, ZeroClaw, CoPaw, NanoClaw, and NemoClaw now supported alongside OpenClaw. NanoClaw connected via new `/v1/messages` Anthropic-compatible endpoint; NemoClaw via OpenShell inference routing. Added OpenRouter as a supported LLM platform.
- **[03/13/2026]** **v0.3.1** — MinT backend support: RL training now works with both Tinker and MinT. Configurable via `rl.backend` (auto/tinker/mint).
- **[03/13/2026]** **v0.3** — Continual meta-learning support: slow RL updates now only run during sleep hours, idle time, or Google Calendar meetings. Added support/query set separation to prevent stale reward signals from polluting model updates.
- **[03/11/2026]** **v0.2** — One-click deployment via `metaclaw` CLI. Skills enabled by default, RL is now opt-in.
- **[03/09/2026]** We release **MetaClaw** — Just talk to your agent and let it evolve automatically. **NO** GPU deployment required; just plug into the **API**.

---

## 🎥 Demo

https://github.com/user-attachments/assets/d86a41a8-4181-4e3a-af0e-dc453a6b8594

---

## 📖 Overview

**MetaClaw is an agent that meta-learns and evolves in the wild.**
Just talk to your agent as you normally would — MetaClaw turns every live conversation into a learning signal, enabling the agent to continuously improve through real-world deployment rather than offline training alone.

Under the hood, it places your model behind a proxy that intercepts interactions from your personal agent (OpenClaw, CoPaw, IronClaw, PicoClaw, ZeroClaw, NanoClaw, NemoClaw, or any OpenAI-compatible client), injects relevant skills at each turn, and meta-learns from accumulated experience. For Anthropic-native agents like NanoClaw, MetaClaw also exposes a `/v1/messages` Anthropic-compatible endpoint so the full pipeline works without any agent-side changes. Skills are summarized automatically after each session; with RL enabled, a meta-learning scheduler defers weight updates to idle windows so the agent is never interrupted during active use.

No GPU cluster required. MetaClaw works with any OpenAI-compatible LLM API out of the box, and uses a Tinker-compatible backend for cloud-based LoRA training. [Tinker](https://www.thinkingmachines.ai/tinker/) is the default reference path; MinT and Weaver can be enabled through separate compatibility packages when needed.

## 🤖 Key Features

### **One-click deployment**
Configure once with `metaclaw setup`, then `metaclaw start` brings up the proxy, injects skills, and wires your chosen personal agent (OpenClaw, CoPaw, or IronClaw) automatically. No manual shell scripts needed.

### **Three operating modes**

| Mode | Default | What it does |
|------|---------|--------------|
| `skills_only` | | Proxy your LLM API. Skills injected and auto-summarized after each session. No GPU/Tinker required. |
| `rl` | | Skills + RL training (GRPO). Trains immediately when a batch is full. Optional OPD for teacher distillation. |
| `auto` | ✅ | Skills + RL + smart scheduler. RL weight updates only run during sleep/idle/meeting windows. |

### **Long-term memory**
MetaClaw can persist facts, preferences, and project history across sessions and inject relevant context at each turn — so your agent remembers what you've told it, even weeks later.

### **Asynchronous by design**
Serving, reward modeling, and training are fully decoupled. The agent continues responding while scoring and optimization run in parallel.

---

## 🚀 Quick Start

### 1. Install

**OpenClaw (one-click):** use the [v0.4.0](https://github.com/aiming-lab/MetaClaw/releases/tag/v0.4.0) release—run the snippet below, then `metaclaw setup` and `metaclaw start`. More detail (Windows, mirrors, config, troubleshooting): [`extensions/metaclaw-openclaw/README.md`](./extensions/metaclaw-openclaw/README.md).

```bash
curl -LO https://github.com/aiming-lab/MetaClaw/releases/download/v0.4.0/metaclaw-plugin.zip
unzip metaclaw-plugin.zip -d ~/.openclaw/extensions
openclaw plugins enable metaclaw-openclaw && openclaw gateway restart
```

**pip** (PyPI or this repo):

```bash
pip install -e .                        # skills_only mode (lightweight)
pip install -e ".[rl]"                  # + RL training support (torch, transformers, tinker)
pip install -e ".[evolve]"              # + skill evolution via OpenAI-compatible LLM
pip install -e ".[scheduler]"           # + Google Calendar integration for scheduler
pip install -e ".[rl,evolve,scheduler]" # recommended for full RL + scheduler setup
```
 (Optional) WeChat integration uses the official [`@tencent-weixin/openclaw-weixin`](https://github.com/nicepkg/openclaw-weixin) plugin. MetaClaw auto-installs it when WeChat is enabled:

```bash
metaclaw config wechat.enabled true
metaclaw start
```

The plugin is installed automatically on `metaclaw start`. You can also install it manually:

```bash
npx -y @tencent-weixin/openclaw-weixin-cli@latest install
```

To switch WeChat accounts (re-login with a new QR code):

```bash
metaclaw start --wechat-relogin
```

If you want to run `rl.backend=mint`, install the MinT compatibility package separately in the same environment, for example [`mindlab-toolkit`](https://github.com/MindLab-Research/mindlab-toolkit). Similarly, for `rl.backend=weaver`, install [`nex-weaver`](https://github.com/nex-agi/weaver) separately. MetaClaw keeps these dependencies out of the default package so RL users can choose Tinker, MinT, or Weaver explicitly.

### 2. Configure

```bash
metaclaw setup
```

The interactive wizard will ask you to:
1. **Choose your personal agent** — `openclaw`, `copaw`, `ironclaw`, `picoclaw`, `zeroclaw`, `nanoclaw`, `nemoclaw`, or `none` (MetaClaw will auto-configure it on start)
2. **Choose your auth method** — `api_key` (direct API) or `oauth_token` (CLI subprocess)
3. **Choose your LLM provider**:
   - **api_key**: Kimi, Qwen, OpenAI, Volcano Engine, or custom → enter API base + API key
   - **oauth_token**: Anthropic (Claude Code), OpenAI Codex, or Gemini CLI → paste OAuth token
4. **Enter your model ID** and optionally enable RL training

MetaClaw's RL path can switch explicitly between `tinker`, `mint`, and `weaver`. `auto` is the recommended default and will infer the backend from credentials, base URLs, or environment variables when the corresponding package is installed.

**Tinker**:

```bash
metaclaw config rl.backend tinker
metaclaw config rl.api_key sk-...
metaclaw config rl.model moonshotai/Kimi-K2.5
```

**MinT**:

```bash
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-mint-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
```

**Weaver**:

```bash
metaclaw config rl.backend weaver
metaclaw config rl.api_key sk-...
metaclaw config rl.base_url https://weaver-console.nex-agi.cn
metaclaw config rl.model Qwen/Qwen3-8B
```

Legacy aliases `rl.tinker_api_key` and `rl.tinker_base_url` are still accepted for backward compatibility.

### 3. Start

```bash
metaclaw start
```

That's it. MetaClaw starts the proxy, automatically configures your chosen personal agent to use it, and restarts the gateway. Open your agent and start chatting — skills are injected at every turn, and the session is automatically summarized into new skills when you're done.

---

## 🦞 Multi-Claw Support

MetaClaw works as a transparent proxy in front of any personal agent that supports an OpenAI-compatible LLM backend. The `claw_type` setting tells MetaClaw which agent to auto-configure when it starts.

| `claw_type` | Agent | What MetaClaw does on `start` |
|---|---|---|
| `openclaw` | [OpenClaw](https://openclaw.ai) | Runs `openclaw config set models.providers.metaclaw …` + `gateway restart`. Uses the `anthropic-messages` API format so memory plugins (Hindsight, mem0, memory-lancedb) receive `event.rawMessage` correctly. |
| `copaw` | [CoPaw](https://github.com/agentscope-ai/CoPaw) | Patches `~/.copaw/config.json` → `models.default` → `openai_compatible` pointing at the proxy port. CoPaw's ConfigWatcher hot-reloads automatically. |
| `ironclaw` | [IronClaw](https://github.com/nearai/ironclaw) | Patches `~/.ironclaw/.env` → `LLM_BACKEND=openai_compatible` + `LLM_BASE_URL/MODEL/API_KEY`. Runs `ironclaw service restart`. |
| `picoclaw` | [PicoClaw](https://github.com/sipeed/picoclaw) | Injects a `metaclaw` entry into `~/.picoclaw/config.json` `model_list` and sets it as the default model. Runs `picoclaw gateway restart`. |
| `zeroclaw` | [ZeroClaw](https://github.com/zeroclaw-labs/zeroclaw) | Patches `~/.zeroclaw/config.toml` → `provider = "openai-compatible"` + `base_url/model/api_key`. Runs `zeroclaw service restart`. |
| `nanoclaw` | [NanoClaw](https://github.com/qwibitai/nanoclaw) | Patches nanoclaw's `.env` → `ANTHROPIC_BASE_URL` pointing at the proxy's `/v1/messages` Anthropic-compatible endpoint. Restarts via `launchctl` (macOS) or `systemctl --user` (Linux). |
| `nemoclaw` | [NemoClaw](https://github.com/NVIDIA/NemoClaw) | Registers a `metaclaw` provider in OpenShell via `openshell provider create` and sets it as the active inference route via `openshell inference set`. Persists config to `~/.nemoclaw/config.json`. |
| `hermes` | [Hermes Agent](https://github.com/NousResearch/hermes-agent) | Injects a `metaclaw` entry into `~/.hermes/config.yaml` `custom_providers` and sets `model.provider: custom:metaclaw`. Runs `hermes gateway restart`. |
| `none` | — | Skips auto-configuration. Point your agent at the proxy manually. |

### Setup

Pick your agent during `metaclaw setup` (the first question in the wizard):

```
Personal agent to configure (openclaw/copaw/ironclaw/picoclaw/zeroclaw/nanoclaw/nemoclaw/hermes/none) [openclaw]:
```

Or set it directly at any time:

```bash
metaclaw config claw_type copaw      # switch to CoPaw
metaclaw config claw_type ironclaw   # switch to IronClaw
metaclaw config claw_type picoclaw   # switch to PicoClaw
metaclaw config claw_type zeroclaw   # switch to ZeroClaw
metaclaw config claw_type nanoclaw   # switch to NanoClaw
metaclaw config claw_type nemoclaw   # switch to NemoClaw
metaclaw config claw_type hermes     # switch to Hermes Agent
metaclaw config claw_type none       # manual / custom agent
```

Then run `metaclaw start` as usual — the proxy comes up and the chosen agent is wired automatically.

### Manual wiring (claw_type=none)

Point any OpenAI-compatible client at the MetaClaw proxy:

```
base_url: http://127.0.0.1:30000/v1
api_key:  metaclaw          # or whatever proxy.api_key is set to
model:    <your model id>
```

For Anthropic-native clients (e.g. the Claude SDK or NanoClaw's credential proxy), use the Anthropic-compatible endpoint instead:

```
ANTHROPIC_BASE_URL: http://127.0.0.1:30000
ANTHROPIC_API_KEY:  metaclaw
```

---

## ⚙️ Configuration

Configuration lives in `~/.metaclaw/config.yaml`, created by `metaclaw setup`.

**CLI commands:**

```
metaclaw setup                  # Interactive first-time configuration wizard
metaclaw start                  # Start MetaClaw (default: auto mode)
metaclaw start --mode rl        # Force RL mode (no scheduler) for this session
metaclaw start --mode skills_only  # Force skills-only mode for this session
metaclaw stop                   # Stop a running MetaClaw instance
metaclaw status                 # Check proxy health, running mode, and scheduler state
metaclaw config show            # View current configuration
metaclaw config KEY VALUE       # Set a config value
metaclaw config llm.oauth_token TOKEN        # Store OAuth token for current CLI provider
metaclaw auth paste-token --provider anthropic      # Store OAuth token (anthropic | openai-codex | gemini)
metaclaw auth
... [TRUNCATED]
```

### File: requirements.txt
```txt
# Core — always required
torch
transformers>=4.51.1
httpx
fastapi
uvicorn[standard]

# Optional: skill_manager.py embedding retrieval mode (retrieval_mode="embedding")
numpy
sentence-transformers

# Optional: skill_evolver.py Azure OpenAI skill evolution (enable_skill_evolution=True)
openai

# Optional: training metrics logging
wandb

```

### File: benchmark\README.md
```md
# MetaClaw Benchmark

Evaluation suite for the MetaClaw Evolution Benchmark — measures how well AI agents learn and adapt from multi-day interaction histories.

## Quick Start

```bash
# Install (requires Python ≥ 3.10)
cd benchmark
pip install -e .

# Validate dataset
metaclaw-bench check data/metaclaw-bench/all_tests.json

# Use pre-built script
python scripts/dummy_run.py

# Manually run full pipeline (infer → score → report)
metaclaw start  # start metaclaw proxy first
export BENCHMARK_BASE_URL=http://127.0.0.1:30000/v1
export BENCHMARK_MODEL=GPT-5.2
metaclaw-bench run data/metaclaw-bench/all_tests.json --output results/
```

## Project Structure

```
benchmark/
├── data/
│   ├── metaclaw-bench/          # Full benchmark (30 days)
│   └── metaclaw-bench-small/    # Small subset (12 days)
├── docs/
│   └── CLI.md                   # CLI reference
├── scripts/                     # Experiment runner scripts
│   └── config/                  # YAML configs for different strategies
├── src/                         # Core library
│   ├── cli.py                   # Entry point
│   ├── check/                   # Dataset validation
│   ├── infer/                   # Agent inference
│   ├── scoring/                 # Result scoring
│   ├── report/                  # Report generation
│   ├── run/                     # Full pipeline orchestration
│   └── clean/                   # Workspace cleanup
├── tests/                       # Unit tests
└── openclaw_customize/          # OpenClaw plugin extensions
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `check` | Validate dataset integrity (8 checks) |
| `infer` | Run agent inference on scenarios |
| `score` | Score inference results |
| `report`| Generate summary report |
| `run`   | Full pipeline: infer → score → report |
| `clean` | Remove temporary work directories |

See [docs/CLI.md](docs/CLI.md) for detailed usage and options.

## Experiment Scripts

Pre-built runner scripts under `scripts/` support various agent strategies:

- **baseline** — vanilla agent without enhancements
- **memory / skills-memory** — agents with memory modules
- **rl / rl-only** — reinforcement-learning-based agents
- **madmax** — combined strategy

Each script reads a YAML config from `scripts/config/`. See `scripts/config/env_arg_example.sh` for environment setup.

## Development

```bash
pip install -e ".[dev]"
pytest -v tests/
```

```

### File: extensions\README.md
```md
## MetaClaw Plugin for OpenClaw v0.4.0

One-click installer for [MetaClaw](https://github.com/aiming-lab/MetaClaw) as an OpenClaw extension. No `git clone` required — download the zip, enable, and go.

### One-Click Install

#### macOS / Linux

```bash
curl -LO https://github.com/aiming-lab/MetaClaw/releases/download/v0.4.0/metaclaw-plugin.zip
unzip metaclaw-plugin.zip -d ~/.openclaw/extensions
openclaw plugins enable metaclaw-openclaw
openclaw gateway restart
```

> **China users**: If GitHub downloads are slow or timeout, use a mirror:
> ```bash
> curl -LO https://ghfast.top/https://github.com/aiming-lab/MetaClaw/releases/download/v0.4.0/metaclaw-plugin.zip
> ```

#### Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri https://github.com/aiming-lab/MetaClaw/releases/download/v0.4.0/metaclaw-plugin.zip -OutFile metaclaw-plugin.zip
Expand-Archive metaclaw-plugin.zip -DestinationPath $env:USERPROFILE\.openclaw\extensions
openclaw plugins enable metaclaw-openclaw
openclaw gateway restart
```

> **China users**: If GitHub downloads are slow or timeout, replace the download URL with:
> ```
> https://ghfast.top/https://github.com/aiming-lab/MetaClaw/releases/download/v0.4.0/metaclaw-plugin.zip
> ```

### Then run

```bash
metaclaw setup
metaclaw start
```

### What the plugin does automatically

- Creates an isolated Python virtual environment (`.venv`)
- Installs MetaClaw (`[rl,evolve,scheduler]`) via pip
- Auto-installs the official WeChat plugin (`@tencent-weixin/openclaw-weixin`) when enabled
- Installs `metaclaw` CLI wrapper and configures PATH (macOS / Linux / Windows)
- Patches outbound LLM `fetch` to inject `X-Session-Id` / `X-Turn-Type` headers

### Requirements

- **Python ≥ 3.11**
- **OpenClaw** (any version)
- macOS, Linux, or Windows
- **RAM ≥ 4 GB recommended.** On machines with ≤ 2 GB RAM, add swap before installing:
  ```bash
  sudo fallocate -l 4G /swapfile && sudo chmod 600 /swapfile && sudo mkswap /swapfile && sudo swapon /swapfile
  ```

### What's new in v0.4.0

- **Native OpenClaw extension** — MetaClaw plugs into OpenClaw’s plugin model instead of sitting beside it as a second, hand-wired stack.
- **Two-step install** — drop the folder into OpenClaw’s extensions tree, then one command to enable and restart the gateway.
- **Self-contained bundle** — everything ships in the extension package so you’re not gluing repos, paths, and runtimes together yourself.

### Full auto mode (optional)

```bash
openclaw config set plugins.entries.metaclaw-openclaw.config.oneClickMetaclaw true
```

Enables: venv + pip + default config + `metaclaw start` on gateway load.

### Configuration

See [README](https://github.com/aiming-lab/MetaClaw/blob/main/extensions/metaclaw-openclaw/README.md) for all config options.

```

### File: docs\memory\README.md
```md
# Memory Upgrade Docs

Last updated: 2026-03-12
Status: All phases and optional enhancements complete (529 tests)

This directory contains the working documentation system for the MetaClaw memory upgrade.

## Structure

### Master control

- [Master Plan](/Users/jiaqi/Myprojects/metaclaw-test/MEMORY_UPGRADE_PLAN.md)
- [Handoff](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/HANDOFF.md)

### Phase documents

- [Phase 0 - Planning and Research](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/phases/phase-0-planning.md)
- [Phase 1 - Base Memory System](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/phases/phase-1-base-memory.md)
- [Phase 2 - Adaptive Memory Policy](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/phases/phase-2-adaptive-policy.md)
- [Phase 3 - Replay Evaluation](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/phases/phase-3-replay-eval.md)
- [Phase 4 - Controlled Self-Upgrade](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/phases/phase-4-self-upgrade.md)

### Research reviews

- [SimpleMem Review](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/research/simplemem-review.md)
- [MetaMem Review](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/research/metamem-review.md)

### Logs

- [Decision Log](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/logs/decision-log.md)
- [Lessons Learned](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/logs/lessons-learned.md)
- [Progress Log](/Users/jiaqi/Myprojects/metaclaw-test/docs/memory/logs/progress-log.md)

## Operating Rules

1. The master plan owns scope, roadmap, and overall status.
2. Each phase file owns detailed deliverables, task tracking, and exit criteria for that phase.
3. Research reviews capture what we learned from external and reference systems.
4. The decision log records architectural choices and why they were made.
5. The lessons log records failures, constraints, and reusable insights.
6. The progress log records dated progress notes as execution moves forward.

## Update Rhythm

- Update the relevant phase doc whenever work advances inside that phase.
- Update the decision log immediately after a design choice is made.
- Update lessons learned immediately after discovering a failure mode or important constraint.
- Update the master plan when the overall status or phase boundaries change.
- Re-read the master plan and active phase document before each substantial new implementation segment.
- Reconcile documentation with repository state before ending a work block or reporting progress.
- Refresh the handoff document whenever ownership is expected to move to another agent or operator.

```

### File: assets\README_AR.md
```md
<div align="center">

<img src="new_logo2.png" alt="MetaClaw" width="600">

<br/>

# فقط تحدّث مع الوكيل الخاص بك، وسيتعلّم ويتطوّر باستمرار.

<p>مستوحى من طريقة تعلّم الدماغ. اجعل 🦞 الخاص بك يتعلّم ويتطوّر من كل محادثة حقيقية. لا حاجة لوحدات GPU. يدعم Kimi وQwen وClaude وMiniMax والمزيد.</p>

<img src="metaclaw_mainfig_v2.png" alt="MetaClaw Architecture" width="800">

<p>
  <a href="https://github.com/aiming-lab/MetaClaw"><img src="https://img.shields.io/badge/github-MetaClaw-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat&labelColor=555" alt="License MIT"></a>
  <img src="https://img.shields.io/badge/⚡_غير_متزامن_بالكامل-yellow?style=flat&labelColor=555" alt="Fully Async" />
  <img src="https://img.shields.io/badge/☁️_بدون_GPU-blue?style=flat&labelColor=555" alt="No GPU Cluster" />
  <img src="https://img.shields.io/badge/🛠️_تطور_المهارات-orange?style=flat&labelColor=555" alt="Skill Evolution" />
  <img src="https://img.shields.io/badge/🚀_نشر_بنقرة_واحدة-green?style=flat&labelColor=555" alt="One-Click Deploy" />
</p>

<br/>

[🇺🇸 English](../README.md) • [🇨🇳 中文](./README_ZH.md) • [🇯🇵 日本語](./README_JA.md) • [🇰🇷 한국어](./README_KO.md) • [🇫🇷 Français](./README_FR.md) • [🇩🇪 Deutsch](./README_DE.md) • [🇪🇸 Español](./README_ES.md) • [🇧🇷 Português](./README_PT.md) • [🇷🇺 Русский](./README_RU.md) • [🇮🇹 Italiano](./README_IT.md) • [🇻🇳 Tiếng Việt](./README_VI.md) • [🇮🇳 हिन्दी](./README_HI.md)

<br/>

[نظرة عامة](#-نظرة-عامة) • [البدء السريع](#-البدء-السريع) • [الإعدادات](#️-الإعدادات) • [وضع المهارات](#-وضع-المهارات) • [وضع RL](#-وضع-rl) • [وضع Auto](#-وضع-auto-الافتراضي) • [الاقتباس](#-الاقتباس)

</div>

---

<div align="center">

### أمران فقط. هذا كل شيء.
</div>

```bash
metaclaw setup              # معالج الإعداد لمرة واحدة
metaclaw start              # الوضع الافتراضي: auto، مهارات + تدريب RL مُجدوَل
metaclaw start --mode rl    # RL بدون مُجدوِل (يتدرّب فورًا عند اكتمال الدُّفعة)
metaclaw start --mode skills_only  # مهارات فقط، بدون RL (لا حاجة لـ Tinker)
```

<div align="center">
<img src="metaclaw.gif" alt="MetaClaw demo" width="700">
</div>

---

## 🔥 آخر الأخبار

- **[2026/03/25]** **v0.4.0** — طبقة السياق (Contexture layer): يحتفظ MetaClaw الآن بالذاكرة عبر الجلسات للمستخدمين والمشاريع. يتم استرجاع الحقائق والتفضيلات وتاريخ المشروع ذات الصلة تلقائيًا وحقنها في المطالبات. يشمل سياسة ذاكرة تكيفية وتوحيدًا في الخلفية وخدمة sidecar اختيارية للذاكرة.
- **[2026/03/16]** **v0.3.2** دعم متعدد الـ Claw: أصبح IronClaw وPicoClaw وZeroClaw وCoPaw وNanoClaw وNemoClaw مدعومين إلى جانب OpenClaw. NanoClaw عبر نقطة النهاية الجديدة المتوافقة مع Anthropic `/v1/messages`؛ NemoClaw عبر توجيه الاستدلال OpenShell. إضافة OpenRouter كمنصة LLM مدعومة.
- **[2026/03/13]** **v0.3.1** دعم واجهة MinT الخلفية: يعمل تدريب RL الآن مع Tinker وMinT معًا. يمكن ضبطه عبر `rl.backend` (auto/tinker/mint).
- **[2026/03/13]** **v0.3** دعم التعلّم الفوقي المستمر: تحديثات RL البطيئة تعمل فقط خلال ساعات النوم أو فترات الخمول أو اجتماعات Google Calendar. تمت إضافة فصل مجموعات support/query لمنع إشارات المكافأة القديمة من تلويث تحديثات النموذج.
- **[2026/03/11]** **v0.2** نشر بنقرة واحدة عبر واجهة `metaclaw` CLI. المهارات مُفعّلة افتراضيًا، وRL أصبح اختياريًا.
- **[2026/03/09]** إطلاق **MetaClaw** رسميًا. فقط تحدّث مع الوكيل ودعه يتطوّر تلقائيًا. **لا حاجة** لنشر GPU، فقط اتصل بـ **API**.

---

## 🎥 عرض توضيحي

https://github.com/user-attachments/assets/d86a41a8-4181-4e3a-af0e-dc453a6b8594

---

## 📖 نظرة عامة

**MetaClaw وكيل يتعلّم فوقيًا ويتطوّر في البيئات الحقيقية.**
فقط تحدّث مع وكيلك كالمعتاد. يحوّل MetaClaw كل محادثة حيّة إلى إشارة تعلّم، مما يُمكّن الوكيل من التحسّن المستمر من خلال النشر الفعلي بدلًا من الاعتماد على التدريب دون اتصال فقط.

في الخلفية، يضع MetaClaw نموذجك خلف وكيل وسيط متوافق مع OpenAI (مع نقطة نهاية `/v1/messages` متوافقة مع Anthropic للوكلاء مثل NanoClaw) يعترض التفاعلات من OpenClaw وNanoClaw وNemoClaw وغيرها من الوكلاء المدعومين، ويحقن المهارات ذات الصلة في كل دور، ويتعلّم فوقيًا من التجارب المتراكمة. تُلخَّص المهارات تلقائيًا بعد كل جلسة. عند تفعيل RL، يؤجّل مُجدوِل التعلّم الفوقي تحديثات الأوزان إلى فترات الخمول حتى لا يُقاطَع الوكيل أثناء الاستخدام النشط.

لا حاجة لمجموعة GPU. يعمل MetaClaw مع أي واجهة LLM API متوافقة مع OpenAI مباشرةً، ويستخدم واجهة خلفية متوافقة مع Tinker لتدريب LoRA السحابي. [Tinker](https://www.thinkingmachines.ai/tinker/) هو المسار المرجعي الافتراضي، ويمكن تفعيل MinT أو Weaver من خلال حزم توافق منفصلة عند الحاجة.

## 🤖 الميزات الرئيسية

### **نشر بنقرة واحدة**
قم بالإعداد مرة واحدة باستخدام `metaclaw setup`، ثم `metaclaw start` يُشغّل الوكيل الوسيط ويحقن المهارات ويربط OpenClaw تلقائيًا. لا حاجة لسكربتات shell يدوية.

### **ثلاثة أوضاع تشغيل**

| الوضع | افتراضي | الوصف |
|------|---------|-------|
| `skills_only` | | وكيل وسيط لواجهة LLM API الخاصة بك. يحقن المهارات ويُلخّصها تلقائيًا بعد كل جلسة. لا حاجة لـ GPU / Tinker. |
| `rl` | | المهارات + تدريب RL (GRPO). يتدرّب فورًا عند اكتمال الدُّفعة. OPD اختياري لتقطير المعلّم. |
| `auto` | ✅ | المهارات + RL + مُجدوِل ذكي. تحديثات أوزان RL تعمل فقط خلال فترات النوم/الخمول/الاجتماعات. |

### **ذاكرة طويلة المدى**
يمكن لـ MetaClaw الاحتفاظ بالحقائق والتفضيلات وسجل المشروع عبر الجلسات وحقن السياق المناسب في كل دور — حتى يتذكر الوكيل ما أخبرته به حتى بعد أسابيع.

### **تصميم غير متزامن بالكامل**
الخدمة ونمذجة المكافآت والتدريب منفصلة تمامًا. يستمر الوكيل في الاستجابة بينما يعمل التقييم والتحسين بالتوازي في الخلفية.

---

## 🚀 البدء السريع

### 1. التثبيت

**OpenClaw (تثبيت بنقرة واحدة):** استخدم الإصدار [v0.4.0](https://github.com/aiming-lab/MetaClaw/releases/tag/v0.4.0) — نفّذ الأوامر أدناه، ثم `metaclaw setup` و`metaclaw start`. مزيد من التفاصيل (Windows، المرايا، الإعداد، استكشاف الأخطاء): [`extensions/metaclaw-openclaw/README.md`](../extensions/metaclaw-openclaw/README.md).

```bash
curl -LO https://github.com/aiming-lab/MetaClaw/releases/download/v0.4.0/metaclaw-plugin.zip
unzip metaclaw-plugin.zip -d ~/.openclaw/extensions
openclaw plugins enable metaclaw-openclaw && openclaw gateway restart
```

**pip** (PyPI أو هذا المستودع):

```bash
pip install -e .                        # وضع skills_only (خفيف الوزن)
pip install -e ".[rl]"                  # + دعم تدريب RL (torch، transformers، tinker)
pip install -e ".[evolve]"              # + تطوير المهارات عبر LLM متوافق مع OpenAI
pip install -e ".[scheduler]"           # + تكامل Google Calendar مع المُجدوِل
pip install -e ".[rl,evolve,scheduler]" # موصى به: إعداد RL + مُجدوِل كامل
```
(اختياري) يستخدم دمج WeChat الملحق الرسمي @tencent-weixin/openclaw-weixin. يثبّت MetaClaw هذا الملحق تلقائياً عند تفعيل WeChat:

```bash
metaclaw config wechat.enabled true
metaclaw start
```

يتم تثبيت الملحق تلقائياً عند بدء MetaClaw. يمكنك أيضاً تثبيته يدوياً:

```bash
npx -y @tencent-weixin/openclaw-weixin-cli@latest install
```

لتبديل حسابات WeChat (إعادة تسجيل الدخول برمز QR جديد):

```bash
metaclaw start --wechat-relogin
```

إذا كنت تريد استخدام `rl.backend=mint`، قم بتثبيت حزمة توافق MinT بشكل منفصل في نفس البيئة، مثل [`mindlab-toolkit`](https://github.com/MindLab-Research/mindlab-toolkit). لاستخدام `rl.backend=weaver`، قم بتثبيت [`nex-weaver`](https://github.com/nex-agi/weaver) بشكل منفصل. لا يضمّن MetaClaw هذه التبعيات في الحزمة الافتراضية حتى يتمكّن مستخدمو RL من اختيار Tinker أو MinT أو Weaver بشكل صريح.

### 2. الإعداد

```bash
metaclaw setup
```

الدليل التفاعلي سيطلب منك:
1. **اختيار الوكيل الشخصي** — `openclaw` أو `copaw` أو `ironclaw` أو `picoclaw` أو `zeroclaw` أو `nanoclaw` أو `nemoclaw` أو `none` (يضبطه MetaClaw تلقائياً عند التشغيل)
2. **اختيار مزود LLM** — Kimi أو Qwen أو OpenAI أو Volcano Engine أو مخصص
3. **إدخال مفتاح API** وتفعيل تدريب RL اختيارياً

يمكن لمسار RL في MetaClaw التبديل صراحةً بين `tinker` و`mint` و`weaver`. القيمة الافتراضية الموصى بها هي `auto` وستظل تستنتج MinT أو Weaver من بيانات الاعتماد أو عناوين URL المقابلة عندما تكون الحزم مثبّتة.

**Tinker**:

```bash
metaclaw config rl.backend tinker
metaclaw config rl.api_key sk-...
metaclaw config rl.model moonshotai/Kimi-K2.5
```

**MinT**:

```bash
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-mint-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
```

**Weaver**:

```bash
metaclaw config rl.backend weaver
metaclaw config rl.api_key sk-...
metaclaw config rl.base_url https://weaver-console.nex-agi.cn
metaclaw config rl.model Qwen/Qwen3-8B
```

الأسماء المستعارة القديمة `rl.tinker_api_key` و`rl.tinker_base_url` لا تزال مقبولة للتوافق مع الإصدارات السابقة.

### 3. التشغيل

```bash
metaclaw start
```

هذا كل شيء. يبدأ MetaClaw البروكسي، ويضبط الوكيل الشخصي المختار تلقائياً، ويعيد تشغيل البوابة. افتح الوكيل وابدأ المحادثة — تُحقَن المهارات في كل دور وتُلخَّص الجلسة تلقائياً إلى مهارات جديدة عند الانتهاء.

---

## ⚙️ الإعدادات

ملف الإعدادات موجود في `~/.metaclaw/config.yaml`، يُنشأ بواسطة `metaclaw setup`.

**أوامر CLI:**

```
metaclaw setup                  # معالج الإعداد التفاعلي لأول مرة
metaclaw start                  # تشغيل MetaClaw (الوضع الافتراضي: auto)
metaclaw start --mode rl        # فرض وضع RL لهذه الجلسة (بدون مُجدوِل)
metaclaw start --mode skills_only  # فرض وضع المهارات فقط لهذه الجلسة
metaclaw stop                   # إيقاف مثيل MetaClaw قيد التشغيل
metaclaw status                 # التحقق من صحة الوكيل الوسيط والوضع الحالي وحالة المُجدوِل
metaclaw config show            # عرض الإعدادات الحالية
metaclaw config KEY VALUE       # تعيين قيمة إعداد
metaclaw config llm.oauth_token TOKEN               # تخزين رمز OAuth لمزود CLI الحالي
metaclaw auth paste-token --provider anthropic      # تخزين رمز OAuth (anthropic | openai-codex | gemini)
metaclaw auth status                                # عرض جميع ملفات المصادقة المخزّنة
metaclaw uninstall              # حذف جميع بيانات MetaClaw وإضافة OpenClaw وحزمة pip
```

استخدم `metaclaw status` للتحقق من الجاهزية و`metaclaw stop` لإيقاف العملية.

<details>
<summary><b>المرجع الكامل للإعدادات (انقر للتوسيع)</b></summary>

```yaml
mode: auto                 # "auto" | "rl" | "skills_only"
claw_type: openclaw        # "openclaw" | "copaw" | "ironclaw" | "picoclaw" | "zeroclaw" | "nanoclaw" | "nemoclaw" | "hermes" | "none"

llm:
  auth_method: api_key      # "api_key" | "oauth_token"
  provider: kimi            # kimi | qwen | openai | minimax | novita | openrouter | volcengine | custom
  model_id: moonshotai/Kimi-K2.5
  api_base: https://api.moonshot.cn/v1
  api_key: sk-...
  # مثال oauth_token (الرمز مخزَّن عبر `metaclaw auth paste-token`):
  # auth_method: oauth_token
  # provider: anthropic     # anthropic | openai-codex | gemini
  # model_id: claude-sonnet-4-6

proxy:
  port: 30000
  api_key: ""              # اختياري: رمز bearer للوكيل الوسيط المحلي لـ MetaClaw

skills:
  enabled: true
  dir: ~/.metaclaw/skills   # دليل مكتبة المهارات الخاصة بك
  retrieval_mode: template  # template | embedding
  top_k: 6
  task_specific_top_k: 10   # الحد الأقصى للمهارات الخاصة بالمهمة (افتراضي 10)
  auto_evolve: true         # تلخيص المهارات تلقائيًا بعد كل جلسة

rl:
  enabled: false            # اضبط على true لتفعيل تدريب RL
  backend: auto             # "auto" | "tinker" | "mint" | "weaver"
  model: moonshotai/Kimi-K2.5
  api_key: ""
  base_url: ""              # نقطة نهاية خلفية اختيارية، مثل https://mint.macaron.xin/ لـ MinT أو https://weaver-console.nex-agi.cn لـ Weaver
  tinker_api_key: ""        # اسم مستعار متوافق لـ api_key
  tinker_base_url: ""       # اسم مستعار متوافق لـ base_url
  prm_url: https://api.openai.com/v1
  prm_model: gpt-5.2
  prm_api_key: ""
  lora_rank: 32
  batch_size: 4
  resume_from_ckpt: ""      # اختياري: استئناف التدريب من نقطة تفتيش
  evolver_api_base: ""      # اتركه فارغًا لإعادة استخدام llm.api_base
  evolver_api_key: ""
  evolver_model: gpt-5.2

opd:
  enabled: false            # اضبط على true لتفعيل OPD (تقطير المعلّم)
  teacher_url: ""           # عنوان URL الأساسي لنموذج المعلّم (متوافق مع OpenAI /v1/completions)
  teacher_model: ""         # اسم نموذج المعلّم (مثل Qwen/Qwen3-32B)
  teacher_api_key: ""       # مفتاح API لنموذج المعلّم
  kl_penalty_coef: 1.0      # معامل عقوبة KL لـ OPD

max_context_tokens: 20000   # حد رموز الموجه قبل الاقتطاع؛ 0 = بلا اقتطاع
                            # (موصى به في skills_only مع نماذج سحابية ذات سياق كبير)
context_window: 0           # نافذة السياق المبلَّغ عنها للوكيل (مثل عتبة ضغط OpenClaw)؛
                            # 0 = تلقائي (≈200000 في skills_only، 32768 في rl/auto)

scheduler:                  # v0.3: مُجدوِل التعلّم الفوقي (يُفعَّل تلقائيًا في وضع auto)
  enabled: false            # يُفعَّل تلقائيًا في وضع auto، يجب ضبطه يدويًا في وضع rl
  sleep_start: "23:00"
  sleep_end: "07:00"
  idle_threshold_minutes: 30
  min_window_minutes: 15
  calendar:
    enabled: false
    credentials_path: ""
    token_path: ""
```

</details>

---

## 💪 وضع المهارات

**`metaclaw start --mode skills_only`**

أخف وضع تشغيل. لا حاجة لـ GPU أو واجهة RL خلفية. يضع MetaClaw واجهة LLM الخاصة بك خلف وكيل وسيط يحقن المهارات ذات الصلة في كل دور محادثة، ثم يُلخّص مهارات جديدة تلقائيًا بعد كل محادثة.

لمزودين مخصصين متوافقين مع OpenAI، اضبط `llm.api_base` على عنوان قاعدة واجهة الدردشة الكامل (عادة ينتهي بـ `/v1`، مثل `https://your-gateway.example/v1`). في وضع `skills_only`، يعيد MetaClaw استخدام نقطة النهاية نفسها لضغط الموجه واستدعاءات نموذج اللغة المساعدة ما لم تُضبَط نقطة نهاية evolver منفصلة.

المهارات هي تعليمات Markdown قصيرة تُخزَّن في `~/.metaclaw/skills/` كملفات `SKILL.md` مستقلة. تنمو المكتبة تلقائيًا مع استخدامك.

لتحميل بنك المهارات المدمج مسبقًا (أكثر من 40 مهارة تشمل البرمجة والأمان ومهام الوكيل وغيرها):

```bash
cp -r memory_data/skills/* ~/.metaclaw/skills/
```

---

## 🔬 وضع RL

**`metaclaw start --mode rl`**

كل ما في وضع المهارات، بالإضافة إلى الضبط الدقيق المستمر بالتعلّم المعزّز من المحادثات الحيّة. يتم تحويل كل دور محادثة إلى رموز وإرساله كعيّنة تدريب. يقوم نموذج LLM حكم (PRM) بتقييم الاستجابات بشكل غير متزامن، وتُجري واجهة خلفية متوافقة مع Tinker (مثل Tinker السحابي أو MinT أو Weaver) ضبطًا دقيقًا لـ LoRA مع تبديل الأوزان تلقائيًا.

**Tinker**:

```bash
metaclaw config rl.backend tinker
metaclaw config rl.api_key sk-...
metaclaw config rl.model moonshotai/Kimi-K2.5
metaclaw config rl.prm_url https://api.openai.com/v1
metaclaw config rl.prm_api_key sk-...
metaclaw start --mode rl
```

**MinT**:

```bash
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-mint-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
metaclaw config rl.prm_url https://api.openai.com/v1
metaclaw config rl.prm_api_key sk-...
metaclaw start --mode rl
```

**Weaver**:

```bash
metaclaw config rl.backend weaver
metaclaw config rl.api_key sk-...
metaclaw config rl.base_url https://weaver-console.nex-agi.cn
metaclaw config rl.model Qwen/Qwen3-8B
metaclaw config rl.prm_url https://api.openai.com/v1
metaclaw config rl.prm_api_key sk-...
metaclaw start --mode rl
```

يستخرج نموذج LLM مُطوِّر مخصّص أيضًا م
... [TRUNCATED]
```

### File: assets\README_DE.md
```md
<div align="center">

<img src="new_logo2.png" alt="MetaClaw" width="600">

<br/>

# Sprich einfach mit deinem Agenten — er lernt und *ENTWICKELT* sich weiter.

<p>Inspiriert davon, wie das Gehirn lernt. Meta-lernen und entwickeln Sie Ihren 🦞 aus jedem Gespräch. Keine GPU nötig. Kompatibel mit Kimi, Qwen, Claude, MiniMax und mehr.</p>

<img src="metaclaw_mainfig_v2.png" alt="MetaClaw Architecture" width="800">

<p>
  <a href="https://github.com/aiming-lab/MetaClaw"><img src="https://img.shields.io/badge/github-MetaClaw-181717?style=flat&labelColor=555&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat&labelColor=555" alt="License MIT"></a>
  <img src="https://img.shields.io/badge/⚡_Vollständig_Async-yellow?style=flat&labelColor=555" alt="Fully Async" />
  <img src="https://img.shields.io/badge/☁️_Kein_GPU--Cluster-blue?style=flat&labelColor=555" alt="No GPU Cluster" />
  <img src="https://img.shields.io/badge/🛠️_Skill--Evolution-orange?style=flat&labelColor=555" alt="Skill Evolution" />
  <img src="https://img.shields.io/badge/🚀_Ein--Klick--Deployment-green?style=flat&labelColor=555" alt="One-Click Deploy" />
</p>

<br/>

[🇺🇸 English](../README.md) • [🇨🇳 中文](./README_ZH.md) • [🇯🇵 日本語](./README_JA.md) • [🇰🇷 한국어](./README_KO.md) • [🇫🇷 Français](./README_FR.md) • [🇪🇸 Español](./README_ES.md) • [🇧🇷 Português](./README_PT.md) • [🇷🇺 Русский](./README_RU.md) • [🇮🇹 Italiano](./README_IT.md) • [🇻🇳 Tiếng Việt](./README_VI.md) • [🇦🇪 العربية](./README_AR.md) • [🇮🇳 हिन्दी](./README_HI.md)

<br/>

[Übersicht](#-übersicht) • [Schnellstart](#-schnellstart) • [Konfiguration](#️-konfiguration) • [Skills-Modus](#-skills-modus) • [RL-Modus](#-rl-modus) • [Auto-Modus](#-auto-modus-standard) • [Zitierung](#-zitierung)

</div>

---

<div align="center">

### Zwei Befehle. Das ist alles.
</div>

```bash
metaclaw setup              # Einmaliger Konfigurationsassistent
metaclaw start              # Standard: Auto-Modus, Skills + geplantes RL-Training
metaclaw start --mode rl    # RL ohne Scheduler (trainiert sofort bei vollem Batch)
metaclaw start --mode skills_only  # Nur Skills, kein RL (kein Tinker nötig)
```

<div align="center">
<img src="metaclaw.gif" alt="MetaClaw demo" width="700">
</div>

---

## 🔥 Neuigkeiten

- **[25.03.2026]** **v0.4.0** — Contexture layer: MetaClaw speichert nun sitzungsübergreifend Erinnerungen für Nutzer und Projekte. Relevante Fakten, Präferenzen und Projektverlauf werden automatisch abgerufen und in Prompts injiziert. Enthält adaptive Speicherrichtlinie, Hintergrundkonsolidierung und einen optionalen Memory-Sidecar-Dienst.
- **[16.03.2026]** **v0.3.2** Multi-Claw-Unterstützung: IronClaw, PicoClaw, ZeroClaw, CoPaw, NanoClaw und NemoClaw werden neben OpenClaw unterstützt. NanoClaw über den neuen `/v1/messages` Anthropic-kompatiblen Endpunkt; NemoClaw über OpenShell-Inferenz-Routing. OpenRouter als LLM-Plattform hinzugefügt.
- **[13.03.2026]** **v0.3.1** MinT-Backend-Unterstützung: RL-Training funktioniert jetzt mit Tinker und MinT. Konfigurierbar über `rl.backend` (auto/tinker/mint).
- **[13.03.2026]** **v0.3** Kontinuierliche Meta-Learning-Unterstützung: RL-Gewichtsupdates laufen nur noch während Schlafenszeiten, Leerlaufphasen oder Google-Calendar-Meetings. Support/Query-Set-Trennung hinzugefügt, um veraltete Belohnungssignale von Modell-Updates fernzuhalten.
- **[11.03.2026]** **v0.2** Ein-Klick-Deployment über `metaclaw` CLI. Skills standardmäßig aktiviert, RL jetzt optional.
- **[09.03.2026]** **MetaClaw** veröffentlicht. Sprich einfach mit deinem Agenten und lass ihn automatisch weiterentwickeln. **Kein** GPU-Deployment erforderlich; einfach an die **API** anschließen.

---

## 🎥 Demo

https://github.com/user-attachments/assets/d86a41a8-4181-4e3a-af0e-dc453a6b8594

---

## 📖 Übersicht

**MetaClaw ist ein Agent, der in realen Einsatzszenarien meta-lernt und sich weiterentwickelt.**
Sprich einfach wie gewohnt mit deinem Agenten. MetaClaw verwandelt jedes Live-Gespräch in ein Lernsignal und ermöglicht dem Agenten, sich durch den realen Einsatz kontinuierlich zu verbessern, statt nur auf Offline-Training zu setzen.

Unter der Haube kapselt es dein Modell hinter einem OpenAI-kompatiblen Proxy (für Anthropic-native Agenten wie NanoClaw wird zusätzlich ein `/v1/messages`-kompatibler Endpunkt bereitgestellt), fängt Interaktionen über OpenClaw, NanoClaw, NemoClaw und andere unterstützte Agenten ab, injiziert relevante Skills bei jedem Schritt und meta-lernt aus den gesammelten Erfahrungen. Nach jeder Session werden Skills automatisch zusammengefasst; mit aktiviertem RL verschiebt ein Meta-Learning-Scheduler die Gewichtsaktualisierungen in inaktive Zeitfenster, damit der Agent während der aktiven Nutzung nie unterbrochen wird.

Kein GPU-Cluster nötig. MetaClaw funktioniert mit jeder OpenAI-kompatiblen LLM-API und nutzt ein Tinker-kompatibles Backend für Cloud-basiertes LoRA-Training. [Tinker](https://www.thinkingmachines.ai/tinker/) ist der Standard-Referenzpfad; bei Bedarf können MinT oder Weaver über separate Kompatibilitätspakete aktiviert werden.

## 🤖 Hauptfunktionen

### **Ein-Klick-Deployment**
Einmal mit `metaclaw setup` konfigurieren, dann startet `metaclaw start` den Proxy, injiziert Skills und verbindet OpenClaw automatisch. Keine manuellen Shell-Skripte nötig.

### **Drei Betriebsmodi**

| Modus | Standard | Funktion |
|-------|---------|----------|
| `skills_only` | | Proxy für deine LLM-API. Skills werden injiziert und nach jeder Session automatisch zusammengefasst. Kein GPU/Tinker erforderlich. |
| `rl` | | Skills + RL-Training (GRPO). Trainiert sofort, wenn ein Batch voll ist. Optional OPD für Lehrer-Destillation. |
| `auto` | ✅ | Skills + RL + Smart-Scheduler. RL-Gewichtsupdates laufen nur in Schlaf-/Leerlauf-/Meeting-Fenstern. |

### **Langzeitgedächtnis**
MetaClaw kann Fakten, Präferenzen und Projektverlauf über Sitzungen hinweg speichern und pro Runde relevanten Kontext einspielen — dein Agent erinnert sich an das, was du gesagt hast, auch Wochen später.

### **Asynchron by Design**
Serving, Reward Modeling und Training sind vollständig entkoppelt. Der Agent antwortet weiterhin, während Bewertung und Optimierung parallel laufen.

---

## 🚀 Schnellstart

### 1. Installation

**OpenClaw (One-Click):** Nutze das Release [v0.4.0](https://github.com/aiming-lab/MetaClaw/releases/tag/v0.4.0) — führe die Befehle unten aus, dann `metaclaw setup` und `metaclaw start`. Mehr Infos (Windows, Spiegelserver, Konfiguration, Troubleshooting): [`extensions/metaclaw-openclaw/README.md`](../extensions/metaclaw-openclaw/README.md).

```bash
curl -LO https://github.com/aiming-lab/MetaClaw/releases/download/v0.4.0/metaclaw-plugin.zip
unzip metaclaw-plugin.zip -d ~/.openclaw/extensions
openclaw plugins enable metaclaw-openclaw && openclaw gateway restart
```

**pip** (PyPI oder dieses Repository):

```bash
pip install -e .                        # skills_only-Modus (leichtgewichtig)
pip install -e ".[rl]"                  # + RL-Trainingsunterstützung (torch, transformers, tinker)
pip install -e ".[evolve]"              # + Skill-Evolution via OpenAI-kompatibler LLM
pip install -e ".[scheduler]"           # + Google Calendar Integration für Scheduler
pip install -e ".[rl,evolve,scheduler]" # empfohlen: vollständiges RL + Scheduler-Setup
```
(Freiwillig) WeChat-Integration verwendet das offizielle Plugin @tencent-weixin/openclaw-weixin. MetaClaw installiert es automatisch, wenn WeChat aktiviert ist:

```bash
metaclaw config wechat.enabled true
metaclaw start
```

Das Plugin wird beim Starten von MetaClaw automatisch installiert. Du kannst es auch manuell installieren:

```bash
npx -y @tencent-weixin/openclaw-weixin-cli@latest install
```

Um WeChat-Konten zu wechseln (mit neuem QR-Code erneut anmelden):

```bash
metaclaw start --wechat-relogin
```

Wenn du `rl.backend=mint` verwenden willst, installiere das MinT-Kompatibilitätspaket separat in derselben Umgebung, zum Beispiel [`mindlab-toolkit`](https://github.com/MindLab-Research/mindlab-toolkit). Für `rl.backend=weaver` installiere separat [`nex-weaver`](https://github.com/nex-agi/weaver). MetaClaw hält diese Abhängigkeiten absichtlich aus dem Standardpaket heraus, damit RL-Nutzer Tinker, MinT oder Weaver explizit wählen können.

### 2. Konfiguration

```bash
metaclaw setup
```

Der interaktive Assistent führt dich durch:
1. **Persönlichen Agenten wählen** — `openclaw`, `copaw`, `ironclaw`, `picoclaw`, `zeroclaw`, `nanoclaw`, `nemoclaw` oder `none` (MetaClaw konfiguriert ihn beim Start automatisch)
2. **LLM-Anbieter wählen** — Kimi, Qwen, OpenAI, Volcano Engine oder benutzerdefiniert
3. **API-Schlüssel eingeben** und optional RL-Training aktivieren

Der RL-Pfad von MetaClaw kann explizit zwischen `tinker`, `mint` und `weaver` wechseln. `auto` ist die empfohlene Voreinstellung und kann MinT oder Weaver weiterhin aus den entsprechenden Credentials oder Base-URLs ableiten, wenn die Pakete installiert sind.

**Tinker**:

```bash
metaclaw config rl.backend tinker
metaclaw config rl.api_key sk-...
metaclaw config rl.model moonshotai/Kimi-K2.5
```

**MinT**:

```bash
metaclaw config rl.backend mint
metaclaw config rl.api_key sk-mint-...
metaclaw config rl.base_url https://mint.macaron.xin/
metaclaw config rl.model Qwen/Qwen3-4B-Instruct-2507
```

**Weaver**:

```bash
metaclaw config rl.backend weaver
metaclaw config rl.api_key sk-...
metaclaw config rl.base_url https://weaver-console.nex-agi.cn
metaclaw config rl.model Qwen/Qwen3-8B
```

Die Legacy-Aliase `rl.tinker_api_key` und `rl.tinker_base_url` werden weiterhin aus Kompatibilitätsgründen akzeptiert.

### 3. Start

```bash
metaclaw start
```

Das war's. MetaClaw startet den Proxy, konfiguriert OpenClaw automatisch und startet das Gateway neu. Öffne OpenClaw und beginne zu chatten. Skills werden bei jedem Schritt injiziert, und die Session wird automatisch zu neuen Skills zusammengefasst, wenn du fertig bist.

---

## ⚙️ Konfiguration

Die Konfiguration liegt in `~/.metaclaw/config.yaml`, erstellt durch `metaclaw setup`.

**CLI-Befehle:**

```
metaclaw setup                  # Interaktiver Erstkonfigurations-Assistent
metaclaw start                  # MetaClaw starten (Standard: Auto-Modus)
metaclaw start --mode rl        # RL-Modus für diese Session erzwingen (ohne Scheduler)
metaclaw start --mode skills_only  # Nur-Skills-Modus für diese Session erzwingen
metaclaw stop                   # Laufende MetaClaw-Instanz stoppen
metaclaw status                 # Proxy-Status, laufenden Modus und Scheduler prüfen
metaclaw config show            # Aktuelle Konfiguration anzeigen
metaclaw config KEY VALUE       # Konfigurationswert setzen
metaclaw config llm.oauth_token TOKEN               # OAuth-Token fuer den aktuellen CLI-Anbieter speichern
metaclaw auth paste-token --provider anthropic      # OAuth-Token speichern (anthropic | openai-codex | gemini)
metaclaw auth status                                # Alle gespeicherten Authentifizierungsprofile anzeigen
metaclaw uninstall              # Alle MetaClaw-Daten, OpenClaw-Erweiterung und pip-Paket entfernen
```

Verwenden Sie `metaclaw status` zur Überprüfung der Bereitschaft und `metaclaw stop` zum Stoppen des Prozesses.

<details>
<summary><b>Vollständige Konfigurationsreferenz (zum Aufklappen klicken)</b></summary>

```yaml
mode: auto                 # "auto" | "rl" | "skills_only"
claw_type: openclaw        # "openclaw" | "copaw" | "ironclaw" | "picoclaw" | "zeroclaw" | "nanoclaw" | "nemoclaw" | "hermes" | "none"

llm:
  auth_method: api_key      # "api_key" | "oauth_token"
  provider: kimi            # kimi | qwen | openai | minimax | novita | openrouter | volcengine | custom
  model_id: moonshotai/Kimi-K2.5
  api_base: https://api.moonshot.cn/v1
  api_key: sk-...
  # oauth_token-Beispiel (Token gespeichert via `metaclaw auth paste-token`):
  # auth_method: oauth_token
  # provider: anthropic     # anthropic | openai-codex | gemini
  # model_id: claude-sonnet-4-6

proxy:
  port: 30000
  api_key: ""              # optionales Bearer-Token für den lokalen MetaClaw-Proxy

skills:
  enabled: true
  dir: ~/.metaclaw/skills   # deine Skill-Bibliothek
  retrieval_mode: template  # template | embedding
  top_k: 6
  task_specific_top_k: 10   # Obergrenze für aufgabenspezifische Skills (Standard 10)
  auto_evolve: true         # Skills nach jeder Session automatisch zusammenfassen

rl:
  enabled: false            # auf true setzen, um RL-Training zu aktivieren
  backend: auto             # "auto" | "tinker" | "mint" | "weaver"
  model: moonshotai/Kimi-K2.5
  api_key: ""
  base_url: ""              # optionaler Backend-Endpunkt, z.B. https://mint.macaron.xin/ für MinT oder https://weaver-console.nex-agi.cn für Weaver
  tinker_api_key: ""        # Legacy-Alias für api_key
  tinker_base_url: ""       # Legacy-Alias für base_url
  prm_url: https://api.openai.com/v1
  prm_model: gpt-5.2
  prm_api_key: ""
  lora_rank: 32
  batch_size: 4
  resume_from_ckpt: ""      # optionaler Checkpoint-Pfad zum Fortsetzen des Trainings
  evolver_api_base: ""      # leer lassen, um llm.api_base wiederzuverwenden
  evolver_api_key: ""
  evolver_model: gpt-5.2

opd:
  enabled: false            # auf true setzen, um OPD (Lehrer-Destillation) zu aktivieren
  teacher_url: ""           # Basis-URL des Lehrermodells (OpenAI-kompatibles /v1/completions)
  teacher_model: ""         # Name des Lehrermodells (z.B. Qwen/Qwen3-32B)
  teacher_api_key: ""       # API-Schlüssel des Lehrermodells
  kl_penalty_coef: 1.0      # KL-Strafkoeffizient für OPD

max_context_tokens: 20000   # Obergrenze für Prompt-Tokens vor Trunkierung; 0 = keine Trunkierung
                            # (empfohlen in skills_only mit großen Cloud-Modellen)
context_window: 0           # dem Agenten gemeldetes Kontextfenster (z. B. OpenClaw-Kompaktierungsschwelle);
                            # 0 = auto (ca. 200 000 in skills_only, 32 768 in rl/auto)

scheduler:                  # v0.3: Meta-Learning-Scheduler (auto-aktiviert im Auto-Modus)
  enabled: false            # Auto-Modus aktiviert automatisch; für RL-Modus manuell setzen
  sleep_start: "23:00"
  sleep_end: "07:00"
  idle_threshold_minutes: 30
  min_window_minutes: 15
  calendar:
    enabled: false
    credentials_path: ""
    token_path: ""
```

</details>

---

## 💪 Skills-Modus

**`metaclaw start --mode skills_only`**

Der leichteste Modus. Kein GPU, kein RL-Backend nötig. MetaClaw kapselt dein LLM hinter einem Proxy, der bei jedem Schritt relevante Skills injiziert und nach jedem Gespräch automatisch neue Skills zusammenfasst.

Für benutzerdefinierte OpenAI-kompatible Anbieter setze `llm.api_base` auf die vollständige Chat-API-Basis (meist mit `/v1`, z. B. `https://your-gateway.example/v1`). Im Modus `skills_only` nutzt MetaClaw denselben Endpunkt für Prompt-Kompression und zugehörige Hilfs-LLM-Aufrufe, sofern kein separater Evolver-Endpunkt konfiguriert ist.

Skills sind kurze Markdown-Anweisungen
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
