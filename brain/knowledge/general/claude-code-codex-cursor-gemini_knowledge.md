---
id: claude-code-codex-cursor-gemini-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:02.775027
---

# KNOWLEDGE EXTRACT: claude-code-codex-cursor-gemini
> **Extracted on:** 2026-03-30 13:19:50
> **Source:** claude-code-codex-cursor-gemini

---

## File: `CLAUDE.md`
```markdown
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a research and comparison repository for AI coding assistants: **Claude Code**, **Codex CLI**, **Gemini CLI**, and **Cursor**. The repository tracks context window sizes, model availability, and feature comparisons across these tools.

## Project Structure

- `README.md` - Quick comparison tables for context windows and features
- `reports/context-comparison.md` - Detailed model comparison data
- `research/` - Timestamped research session outputs
- `.claude/agents/` - Research agent definitions (claude-code, codex-cli, cursor, gemini-cli)
- `.claude/commands/workflow.md` - The `/workflow` command for research automation
- `.claude/hooks/` - Audio notification system for hook events

## Research Workflow

Use `/workflow` to execute the research process. Each agent researches **two sections**:

1. **Context Windows** - Models, sizes, limits, deprecations
2. **Features** - Hooks, plugins, commands, integrations, etc.

### Workflow Steps

1. Creates timestamped folder in `research/`
2. Launches 4 research agents in **parallel** (must use single message with 4 Task tool calls)
3. Each agent writes findings to shared `research.md` with `### Context Windows` and `### Features` subsections
4. Aggregates results into `result.md` with diff comparison for both sections
5. **Requires user approval** before updating README.md

## Research Agents

Located in `.claude/agents/`, each with specialized persona and tools:

| Agent | Persona | Domain |
|-------|---------|--------|
| claude-code-research-agent | Dr. Sarah Chen | Claude Code, Anthropic models |
| codex-cli-research-agent | Marcus Thompson | Codex CLI, OpenAI models |
| cursor-research-agent | Elena Rodriguez | Cursor IDE, multi-model support |
| gemini-cli-research-agent | Dr. Raj Patel | Gemini CLI, Google models |

## Key Files to Update

When research finds changes:
- `README.md` - Context Window Comparison table, Feature Comparison table
- `reports/context-comparison.md` - Detailed model breakdowns, deprecation timelines

```

## File: `README.md`
```markdown
# claude-code-codex-cursor-gemini

![AI Coding Tools](!/banner-pills.svg)

![Battle of the AI Agents](!/claude-mascot.svg)
![Battle of the AI Agents](!/codex-mascot.svg)
![Battle of the AI Agents](!/cursor-mascot.svg)
![Battle of the AI Agents](!/gemini-mascot.svg)

![AI Models](!/banner-models.svg)

> **Last Updated:** 2026-02-09

**AI TERMS:**

| | | | | |
|---|---|---|---|---|
| Agentic Engineering | AI Slop | Context Bloat | Context Engineering | Context Rot |
| Dumb Zone | Hallucination | Scaffolding | Orchestration | Vibe Coding |

[**See Complete List →**](/reports/ai-terms.md)

## Context Window Comparison

| Tool | Largest Context | Best Model | Input $/M | Output $/M | Source |
|------|-----------------|------------|-----------|------------|--------|
| Claude Code | 1M (beta) | Opus 4.6 with `context-1m-2025-08-07` beta | $5.00 | $25.00 | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
| Codex CLI | 400k | GPT-5.3-Codex (Feb 2026) | TBD* | TBD* | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
| Cursor | 2M (native) | Gemini 3 Pro (200k/1M/2M modes) | $2.00** | $12.00** | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
| Gemini CLI | 1M | Gemini 3 Pro Preview | $2.00 | $12.00 | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |

> \* GPT-5.3-Codex pricing not yet published by OpenAI (Feb 2026 release)
> \*\* Cursor uses subscription pricing ($20/mo Pro); API prices shown are for underlying models

[View Full Report](reports/context-comparison.md)

---

## Feature Comparison

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------|:-----------:|:---------:|:----------:|:------:|
| **Hooks** | ✅ 9+ types | ⚠️ Limited | ✅ 10 events | ✅ 40x faster |
| **Plugins/MCP** | ✅ Full | ✅ Full | ✅ FastMCP | ✅ Full |
| **Sub-agents** | ✅ Teams (exp) | ✅ Beta | ✅ A2A (exp) | ✅ Custom |
| **Slash Commands** | ✅ Custom | ✅ Custom | ✅ Custom | ✅ Custom |
| **Custom Commands** | ✅ Skills | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
| **IDE Integration** | ✅ VS/JetBrains | ✅ Multi-platform | ✅ VS Code | ✅ Native |
| **Git Integration** | ✅ Hub (beta) | ✅ GitHub (preview) | ✅ Actions (beta) | ✅ Blame (ent) |
| **Web Search** | ✅ US only | ✅ Built-in | ✅ Grounding | ✅ @Web |
| **Image Support** | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| **Memory/Persistence** | ✅ Session | ✅ Thread | ✅ Project | ✅ Memories |
| **Multi-file Editing** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Composer |
| **Auto-commit** | ⚠️ Via hooks | ⚠️ Manual | ✅ Native | ✅ Native |
| **Custom System Prompts** | ✅ Settings | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
| **Cost Tracking** | ✅ Dashboard | ⚠️ /status | ✅ /stats | ⚠️ Enterprise |
| **Sandbox Mode** | ✅ Native | ✅ OS-enforced | ✅ Container | ✅ Linux (ent) |

[View Full Report](reports/feature-comparison.md)
```

## File: `reports/ai-terms.md`
```markdown
# AI TERMS


## AI Intelligence Levels

| Term | Author | Definition |
|------|--------|------------|
| AGI (Artificial General Intelligence) | [Shane Legg](https://en.wikipedia.org/wiki/Shane_Legg) (DeepMind co-founder) | Hypothetical AI matching human cognitive abilities across any task — can generalize, transfer skills, and solve novel problems without task-specific training |
| AGI Levels Framework | [Meredith Ringel Morris](https://x.com/meraboringmorris) & [Shane Legg](https://en.wikipedia.org/wiki/Shane_Legg) (Google DeepMind) | Five performance levels: Emerging, Competent, Expert, Virtuoso, Superhuman — classifying progress toward AGI |
| ANI (Artificial Narrow Intelligence) | | AI confined to a single well-defined task — all current AI systems are ANI (e.g., Siri, AlphaGo, ChatGPT) |
| ASI (Artificial Superintelligence) | [Nick Bostrom](https://nickbostrom.com/) (Oxford) | Hypothetical AI that vastly outperforms the best human abilities across every cognitive domain |
| Strong AI | [John Searle](https://en.wikipedia.org/wiki/John_Searle) (UC Berkeley) | AI that truly understands and has genuine mental states — contrasted with "Weak AI" that merely simulates intelligence |
| Weak AI | [John Searle](https://en.wikipedia.org/wiki/John_Searle) (UC Berkeley) | AI that simulates cognition without true understanding — all current AI systems fall under this category |


## Agents & Orchestration

| Term | Author | Definition |
|------|--------|------------|
| Agent = LLM + memory + planning + tools | [Lilian Weng](https://lilianweng.github.io/) (ex-OpenAI) | Foundational framework defining LLM-powered autonomous agents |
| Agentic Design Patterns | [Andrew Ng](https://www.deeplearning.ai/) (DeepLearning.AI) | Four core patterns: Reflection, Tool Use, Planning, Multi-Agent Collaboration |
| Agent Swarms | | Multiple AI agents working in parallel on subtasks, coordinating autonomously to solve a larger problem — swarm intelligence applied to LLM-based agents |
| Agentic Engineering | [Andrej Karpathy](https://x.com/karpathy) (Eureka Labs, ex-OpenAI) | Orchestrating AI agents that write code, with humans providing oversight |
| Agentic Workflow | | Structured sequence of AI agent tasks to complete a goal |
| Orchestration | | Coordinating multiple AI agents or steps in a workflow |
| The Holy Trinity | | Skills + Agents + Hooks architecture pattern |


## Human-AI Collaboration

| Term | Author | Definition |
|------|--------|------------|
| AI Engineer | [Swyx / Shawn Wang](https://www.smol.ai/) (Smol.ai) | Engineer building with AI APIs without deep ML expertise — a new role distinct from ML Engineer |
| Centaur Work | [Ethan Mollick](https://www.oneusefulthing.org/) (Wharton) | Human-AI collab with clear division — human does X, AI does Y, switching strategically |
| Cyborg Work | [Ethan Mollick](https://www.oneusefulthing.org/) (Wharton) | Human-AI collab deeply intertwined — moving fluidly between human and AI contributions |
| Compound Engineering | [Dan Shipper](https://every.to/@danshipper) & [Kieran Klaassen](https://every.to/@kieran) (Every) | AI-assisted development where each feature makes the next easier to build — agents write code and every bug, failed test, or insight gets documented and reused by future agents |
| Vibe Coding | [Andrej Karpathy](https://x.com/karpathy) (Eureka Labs, ex-OpenAI) | Letting AI generate code without reading diffs — "give in to the vibes" |


## Context Management

| Term | Author | Definition |
|------|--------|------------|
| Context Bloat | | Excess context degrading AI performance and accuracy |
| Context Engineering | [Dexter Horthy](https://www.humanlayer.dev/) (HumanLayer) | Managing context provided to AI agents for maximum effectiveness |
| Context Rot | | Context becoming stale or irrelevant over long sessions |
| Dumb Zone | | Context window region where AI performance degrades |
| Progressive Disclosure | | Revealing context to AI incrementally as needed |
| Token Burn | | Wasting tokens on irrelevant or redundant context |


## Prompting & Techniques

| Term | Author | Definition |
|------|--------|------------|
| Chain-of-Thought Prompting | [Jason Wei](https://x.com/jabornewe) (Google/OpenAI) | Intermediate reasoning steps to improve LLM performance on complex tasks |
| One Shot | | Single-attempt task completion by AI |
| Prompt Injection | [Simon Willison](https://simonwillison.net/) | Malicious inputs that manipulate LLM system instructions — analogous to SQL injection |
| RAG (Retrieval-Augmented Generation) | [Patrick Lewis](https://www.patricklewis.io/) (Meta AI) | Combining model knowledge with external retrieval for grounded generation |


## AI Safety & Risk

| Term | Author | Definition |
|------|--------|------------|
| AI Alignment | [Paul Christiano](https://paulfchristiano.com/) (ARC, ex-OpenAI) | Ensuring AI systems behave in accordance with human values, preferences, and ethical principles |
| AI Safety | [Stuart Russell](https://people.eecs.berkeley.edu/~russell/) (UC Berkeley) | Research field focused on making AI systems safe, robust, and beneficial to humanity |
| Doom / AI Doom | [Eliezer Yudkowsky](https://www.yudkowsky.net/) (MIRI) | Belief that advanced AI will likely cause human extinction or civilizational collapse |
| Existential Risk (X-Risk) | [Nick Bostrom](https://nickbostrom.com/) (Oxford) | Risk threatening premature extinction of humanity or permanent destruction of its future potential |
| Intelligence Explosion | [I.J. Good](https://en.wikipedia.org/wiki/I._J._Good) (Mathematician) | Self-improving AI triggering a runaway feedback loop of ever-increasing intelligence |
| P(doom) | [Eliezer Yudkowsky](https://www.yudkowsky.net/) (MIRI) / Rationalist community | Estimated probability that AI causes human extinction — popularized in 2023 after GPT-4 release |
| Singularity (Technological) | [Ray Kurzweil](https://en.wikipedia.org/wiki/Ray_Kurzweil) (Google) / [Vernor Vinge](https://en.wikipedia.org/wiki/Vernor_Vinge) | The point where AI self-improvement becomes uncontrollable, fundamentally transforming civilization |


## AI Behavior & Quality

| Term | Author | Definition |
|------|--------|------------|
| AI Slop | [Simon Willison](https://simonwillison.net/) & [Casey Newton](https://www.platformer.news/) | Low-quality AI-generated content produced in quantity |
| Ghost Intelligence | [Andrej Karpathy](https://x.com/karpathy) (Eureka Labs, ex-OpenAI) | LLM intelligence as "summoning ghosts" — emphasizing alien cognitive architecture |
| Hallucination | | AI generating plausible but incorrect information |
| Jagged Intelligence | [Andrej Karpathy](https://x.com/karpathy) (Eureka Labs, ex-OpenAI) | AI excels at complex tasks while failing at simple ones — uneven capability profile |


## Tools & Infrastructure

| Term | Author | Definition |
|------|--------|------------|
| Harness | | Framework wrapping AI for controlled execution |
| MCP (Model Context Protocol) | [David Soria Parra](https://x.com/anthropaborting) & [Justin Spahr-Summers](https://x.com/jspahrsummers) (Anthropic) | Universal standard for connecting AI to external tools and data |
| Scaffolding | | Supporting structure around AI for reliable output |
| Telemetry | | Data collected by AI tools about usage patterns, performance metrics, and errors — often sent to providers for improvement, raising privacy and transparency concerns |


## Workflow Patterns & Practices

| Term | Author | Definition |
|------|--------|------------|
| Closing the Loop | | Ensuring AI output feeds back for validation and correction |
| Ralph Loop | [Geoffrey Huntley](https://ghuntley.com/) | Continuous agent loop pattern (`while :; do cat PROMPT.md \| claude-code ; done`) |
| Rate Limit Jail | | Hitting API rate limits repeatedly, blocking progress |
| Slot Machine Method | | save→run→revert→retry pattern for non-deterministic AI |
| Stop | | Knowing when to halt AI generation to avoid degradation |


## Project Types

| Term | Author | Definition |
|------|--------|------------|
| Brownfield Project | | An existing codebase or system that must be maintained, extended, or modernized — working within legacy constraints, technical debt, and established architecture |
| Greenfield Project | | A new project built from scratch with no legacy constraints — freedom to choose architecture, tools, and patterns without existing technical debt |
```

## File: `reports/context-comparison.md`
```markdown
# Context Window Comparison Report

> **Last Updated:** 2026-02-06

## Claude Code

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| Opus 4.6 | 200k (1M beta) | 128k | $5.00 | $25.00 | Latest model (Feb 5, 2026), adaptive thinking, first Opus with 1M context |
| Opus 4.5 | 200k | 64k | $5.00 | $25.00 | Premium model, complex reasoning, 67% lower cost than predecessor |
| Sonnet 4.5 | 200k (1M beta) | 64k | $3.00 | $15.00 | Recommended default, context awareness feature, best coding model |
| Haiku 4.5 | 200k | 64k | $1.00 | $5.00 | Fastest, context awareness feature, unbeatable for UI work |

**Legacy Models (Still Available):**
- Opus 4.5: 200k tokens, 64k max output
- Opus 4.1: 200k tokens, 32k max output
- Sonnet 4: 200k / 1M beta, 64k max output
- Sonnet 3.7: 200k tokens, 64k / 128k beta max output
- Opus 4: 200k tokens, 32k max output
- Haiku 3: 200k tokens, 4k max output

**Reference:** [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models)

### Model Selection

- During session: `/model <alias>`
- At startup: `claude --model <alias>`
- Environment: `ANTHROPIC_MODEL=<alias>`
- Aliases: `opus`, `sonnet`, `haiku`, `opusplan`
- Extended context: `claude --betas context-1m-2025-08-07`

### Key Features

- Opus 4.6 supports adaptive thinking with 4 effort levels (low, medium, high, max)
- All 4.5 models support extended thinking (31,999 token budget by default)
- 128k max output for Opus 4.6; 64k for other 4.5 models
- Automatic context compaction at 75-92% utilization
- **Context awareness**: Sonnet 4.5 and Haiku 4.5 track remaining context window throughout conversation
- Context budget: 200K (standard), 500K (Enterprise), 1M (beta for tier 4 orgs)

---

## Codex CLI

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| GPT-5.3-Codex | 400k | 128k | TBD | TBD | Latest model (Feb 5, 2026), "Perfect Recall" attention, 25% faster |
| GPT-5.2-Codex | 400k | 128k | $1.75 | $14.00 | Native compaction, reliable tool calling (Jan 14, 2026) |
| GPT-5.1-Codex-Max | Multi-window (millions) | N/A | $1.25 | $10.00 | First model natively trained for compaction |
| GPT-5-Codex | 200k | N/A | $1.25 | $10.00 | Standard model with 200K context window |
| codex-mini-latest | ~200k | N/A | - | - | **DEPRECATED** - Removed Jan 16, 2026 |

**Reference:** [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models)

### Key Features

- **Context compaction** is now a core feature (not experimental)
- Automatically summarizes conversation history when approaching limits
- Enables long-running coding tasks spanning millions of tokens
- Model switching mid-session with `/model` command
- ChatGPT account sign-in (no manual API key needed)
- Agent Skills system production-ready

---

## Cursor

### Anthropic Models

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| Claude 4.6 Opus | 200k (1M max) | 64k | $5.00 | $25.00 | Latest Opus model, deep reasoning |
| Claude 4.5 Sonnet | 200k (1M max) | 64k | $3.00 | $15.00 | Premium, Agent/Thinking modes |
| Claude 4.5 Opus | 200k | 64k | $5.00 | $25.00 | Deep reasoning |
| Claude 4.5 Haiku | 200k | 64k | $1.00 | $5.00 | Fast and efficient |
| Claude 4 Sonnet 1M | 1M | 64k | $3.00 | $15.00 | Max mode only, extended context |
| Claude 4 Sonnet | 200k | 64k | $3.00 | $15.00 | Normal and Max modes |
| Claude 4 Opus | 200k | 64k | $5.00 | $25.00 | Max mode only |
| Claude 3.7 Sonnet | 200k | 64k | $3.00 | $15.00 | Normal and Max modes |
| Claude 3.5 Sonnet | 200k | 64k | $3.00 | $15.00 | Fast and reliable |
| Claude 3.5 Haiku | 60k | 8k | $0.80 | $4.00 | Speed-optimized |

### OpenAI Models

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| GPT-5.2 (all variants) | 272k | - | $2.00 | $8.00 | Latest generation |
| GPT-5.2-Codex | 272k | - | $1.75 | $14.00 | Code-optimized |
| GPT-5.1 Codex Max | 200k (400k max) | 128k | $1.25 | $10.00 | Improved tool calls |
| GPT-5.1 High | 200k (400k max) | 128k | $1.25 | $10.00 | Frontier coding model |
| GPT-5 Fast | 272k | - | $1.25 | $10.00 | Speed-optimized |
| GPT-5 Mini | 200k | 128k | $0.40 | $1.60 | Fast, lightweight option |
| GPT-5 Nano | 200k | 128k | $0.15 | $0.60 | Ultra-fast for simple tasks |
| GPT 4.1 | 200k (1M max) | 8k | $2.00 | $8.00 | Normal and Max modes |
| GPT-4o | 128k | 16k | $2.50 | $10.00 | All-purpose |
| GPT-4o mini | 60k | 8k | $0.15 | $0.60 | Free (500/day) |
| o3 | 200k | 8k | $2.00 | $8.00 | Reasoning optimized |
| o4-mini | 200k | 8k | $1.10 | $4.40 | Normal and Max modes |
| o3-mini | 200k | 8k | $1.10 | $4.40 | Agent/Thinking modes |
| o1 | 200k | 8k | $15.00 | $60.00 | Thinking mode |
| o1 Mini | 128k | 8k | $1.10 | $4.40 | Thinking mode |

### Google Models

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| Gemini 3 Pro Preview | 200k (1M max) | 8k | $2.00 | $12.00 | Top performer on SWE-bench (76.2-78%) |
| Gemini 3 Pro Image Preview | 200k (1M max) | 8k | $2.00 | $12.00 | Multimodal with image generation |
| Gemini 3 Flash | 200k (1M max) | 8k | $0.50 | $3.00 | Fast inference |
| Gemini 2.5 Pro | 200k (1M max) | 8k | $1.25 | $10.00 | Strong for design/debugging |
| Gemini 2.5 Flash | 200k (1M max) | 8k | $0.30 | $2.50 | Fast inference, extended context |

### xAI Models

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| Grok 4 | 200k (2M max) | - | $3.00 | $15.00 | Real-time web search integration |
| Grok Code | 256k | - | $2.00 | $10.00 | Code-optimized |
| Grok Code Fast | 200k | - | $0.60 | $4.00 | Optimized for speed |

### DeepSeek Models

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| DeepSeek V3 | 64k-128k | - | $0.27 | $1.10 | Native support, hosted on US servers |
| DeepSeek V3.1 | 128k | - | $0.27 | $1.10 | Upgraded context from V3 |
| DeepSeek R1 | 200k | - | $0.55 | $2.19 | Native support, free within Pro plan |

### Cursor Native Models

| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| Composer 1 | ~200k | - | N/A | N/A | 4x faster than comparable models, <30s response |

> **Note:** Cursor uses subscription pricing ($20/mo Pro, $40/mo Business). API prices shown above are the underlying provider rates, not what Cursor users pay directly.

**Reference:** [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models)

### Context Mode Comparison

| Mode | Context Range | Cost | Speed |
|------|---------------|------|-------|
| Normal | 60k - 400k | Standard | Fast |
| Max | 200k - 2M | Premium | Slower |

### Key Features

- Dynamic context discovery reduces token usage by 46.9% for MCP tool calls
- Automatic summarization when context window fills
- Chat history preserved as files for context recovery
- Efficient updates via Merkle tree-based change detection

---

## Gemini CLI

| Model | Context Window | Max Output | Input $/M | Output $/M | Status |
|-------|----------------|------------|-----------|------------|--------|
| Gemini 3 Pro Preview | 1M | 65k | $2.00 | $12.00 | Current flagship |
| Gemini 3 Flash Preview | 1M | 65k | $0.50 | $3.00 | Balanced speed/intelligence - Launched Feb 4, 2026 |
| Gemini 3 Pro Image Preview | 65k | 32k | $2.00 | $12.00 | Image generation |
| Gemini 2.5 Pro | 1M | 65k | $1.25 | $10.00 | Stable |
| Gemini 2.5 Flash | 1M | 65k | $0.30 | $2.50 | Stable |
| Gemini 2.5 Flash-Lite | 1M | 65k | $0.10 | $0.40 | Stable |
| Gemini 2.5 Flash Image | 65k | 32k | $0.30 | $2.50 | Stable |
| Gemini 2.5 Flash Preview | 1M | 65k | $0.30 | $2.50 | Experimental features (Preview) |
| Gemini 2.5 Flash TTS | 8k | 16k | $0.30 | $2.50 | Text-to-speech (Preview) |
| Gemini 2.5 Flash Live | 131k | 8k | $0.30 | $2.50 | Preview |
| Gemini 2.0 Flash | 1M | 8k | $0.10 | $0.40 | **Deprecated** - March 31, 2026 |
| Gemini 2.0 Flash-Lite | 1M | 8k | $0.08 | $0.30 | **Deprecated** - March 31, 2026 |

**Reference:** [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models)

### Deprecation Timeline

| Model | Shutdown Date |
|-------|---------------|
| Gemini 2.0 Flash | March 31, 2026 |
| Gemini 2.0 Flash-Lite | March 31, 2026 |
| Gemini 2.5 Pro | June 17, 2026 |
| Gemini 2.5 Flash | June 17, 2026 |
| Gemini 2.5 Flash-Lite | July 22, 2026 |

### Retired Models

| Model | Context Window | Retirement Date |
|-------|----------------|-----------------|
| Gemini 1.5 Pro | 2M | Sept 24, 2025 |
| Gemini 1.5 Flash | 1M | Sept 24, 2025 |

> **Note:** The 2M token context window is no longer available. Maximum context is now 1M tokens.

---

## Research Sources

### Claude Code
- [Anthropic Models Documentation](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models)
- [Claude Code Model Configuration](https://code.claude.com/brain/knowledge/docs_legacy/en/model-config)

### Codex CLI
- [OpenAI Platform Models](https://platform.openai.com/brain/knowledge/docs_legacy/models)
- [OpenAI Codex Blog](https://openai.com/index/introducing-o3-and-o4-mini/)

### Cursor
- [Cursor Models Documentation](https://cursor.com/brain/knowledge/docs_legacy/models)
- [Cursor Changelog](https://cursor.com/changelog)

### Gemini CLI
- [Gemini API Models](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models)
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
- [Gemini Deprecations](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/deprecations)
```

## File: `reports/feature-comparison.md`
```markdown
# Feature Comparison Report

> **Last Updated:** 2026-02-04 (Research Session)

## Overview

A comprehensive comparison of features across the four major AI coding assistants: Claude Code, Codex CLI, Gemini CLI, and Cursor.

### Legend
- ✅ Full Support
- ⚠️ Partial/Limited Support
- ❌ Not Available

---

## Hooks

Shell commands triggered by events during AI operation.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | 12 event types, 3 hook types (command, prompt, agent), async support |
| Codex CLI | ⚠️ Limited | Only notification hook officially supported; comprehensive hooks proposed but not accepted |
| Gemini CLI | ✅ Full | Enabled by default since v0.26.0+, scripts at lifecycle events |
| Cursor | ✅ Full | Enterprise-grade with partner integrations, 10-20x performance improvement |

### Claude Code Hooks

Claude Code provides the most comprehensive hooks system with 12 event types:

| Event | Trigger |
|-------|---------|
| SessionStart | When session begins/resumes |
| UserPromptSubmit | Before Claude processes user prompt |
| PreToolUse | Before tool execution (can block) |
| PermissionRequest | When permission dialog appears |
| PostToolUse | After successful tool execution |
| PostToolUseFailure | After tool execution fails |
| Notification | When Claude Code sends notifications |
| SubagentStart | When subagent spawns |
| SubagentStop | When subagent finishes |
| Stop | When Claude finishes responding |
| PreCompact | Before context compaction |
| SessionEnd | When session terminates |

**Hook Types:**
- Command hooks (`type: "command"`) - Execute shell scripts
- Prompt hooks (`type: "prompt"`) - Single-turn LLM evaluation
- Agent hooks (`type: "agent"`) - Multi-turn subagent with tool access
- Async hooks support with `"async": true` for non-blocking execution

### Codex CLI Hooks

Limited official support:
- **Notification hook**: Built-in, triggers when Codex completes a task
- Comprehensive hooks system proposed (PR #9796) but not yet accepted

### Gemini CLI Hooks

Full support (enabled by default since v0.26.0+):
- Scripts execute at specific points in the agentic loop
- Extensions can bundle hooks directly
- Supports variable substitution in hooks/hooks.json
- Controls and customizes the agent loop at lifecycle events

### Cursor Hooks

Enterprise-grade hooks system (January 2026):
- Observe, block, and extend agent loop operations
- Auto-formatting after edits, gating dangerous commands
- **Performance:** 10-20x faster following January 8, 2026 CLI update
- **Enterprise Partners:** MintMCP, Oasis Security, Runlayer, Semgrep

---

## Plugins/MCP

Extension system via Model Context Protocol and plugin architecture.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | Full MCP support with dynamic tool loading, OAuth support |
| Codex CLI | ✅ Full | MCP + Agent Skills system (production-ready) |
| Gemini CLI | ✅ Full | Robust extension ecosystem, browse at geminicli.com/extensions |
| Cursor | ✅ Full | MCP + VS Code extensions (some Microsoft restrictions) |

### Claude Code MCP

- Full Model Context Protocol implementation
- Dynamic tool loading at runtime
- OAuth support for authenticated services
- Configure in `~/.claude/mcp_servers.json`
- Auto-enable threshold with `auto:N` syntax

### Codex CLI MCP + Agent Skills

- **MCP servers** officially supported for third-party tools
- **Agent Skills** (production-ready): Reusable bundles of instructions
  - Invoke with `$skill-name` (e.g., `$skill-installer`)
  - Auto-selected by Codex based on prompt context
  - Install in `~/.codex/skills` (user) or `.codex/skills` (project)

### Gemini CLI Extensions

- Robust extension ecosystem at geminicli.com/extensions
- Package prompts, MCP servers, Agent Skills, and custom commands
- Easy one-command installation
- Configure via `/extensions` command

### Cursor MCP + Extensions

- Full MCP support with `/mcp enable` and `/mcp disable` commands
- Dynamic context discovery (46.9% token reduction)
- VS Code extension compatibility (some Microsoft-specific restrictions)
- MCP governance via partner integrations

---

## Sub-agents

Ability to spawn parallel worker processes for complex tasks.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | Task tool (7 parallel) + custom persistent subagents |
| Codex CLI | ✅ Via MCP | codex-as-mcp, codex-subagents-mcp, manual orchestration |
| Gemini CLI | ⚠️ Limited | No native support; shell spawning workarounds |
| Cursor | ✅ Full | Up to 8 parallel agents via git worktrees, background agents |

### Claude Code Sub-agents

- **Task Tool**: Up to 7 parallel agents
- **Custom Subagents**: Define in `.claude/agents/` directory
- **Agent Types**: Explore, Plan, Bash, general-purpose, and custom

### Codex CLI Sub-agents

- Via MCP packages:
  - `codex-as-mcp`: Use Codex as an MCP server
  - `codex-subagents-mcp`: Full multi-agent orchestration
- Manual orchestration also possible

### Gemini CLI Sub-agents

- No native sub-agent support
- Workarounds via shell spawning multiple instances

### Cursor Sub-agents

- Up to 8 parallel agents via git worktrees
- Background agents for long-running tasks
- Isolated Ubuntu VMs for background execution

---

## Slash Commands

Built-in commands for common operations.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | /help, /clear, /context, /init, /commit, /pr-comments, /model, /cost, /stats |
| Codex CLI | ✅ Full | /quit, /mention, /new, /resume, /fork, /review, /model, /approvals, /compact |
| Gemini CLI | ✅ Full | /help, /model, /chat, /memory, /extensions, /settings, /stats |
| Cursor | ✅ Full | /summarize, custom commands via .cursor/commands/ |

### Claude Code Commands

| Command | Description |
|---------|-------------|
| `/help` | Show help information |
| `/clear` | Clear conversation |
| `/context` | Show context usage |
| `/init` | Initialize CLAUDE.md |
| `/commit` | Create git commit |
| `/pr-comments` | Review PR comments |
| `/model` | Switch model |
| `/cost` | Show cost information |
| `/stats` | Show session statistics |

### Codex CLI Commands

| Command | Description |
|---------|-------------|
| `/quit` | Exit the CLI |
| `/mention` | Mention files/context |
| `/new` | Start new session |
| `/resume` | Resume previous session |
| `/fork` | Fork current session |
| `/review` | Review code |
| `/model` | Switch model |
| `/approvals` | Manage approval settings |
| `/compact` | Compact context |

### Gemini CLI Commands

| Command | Description |
|---------|-------------|
| `/help` | Show help |
| `/model` | Switch model |
| `/chat` | Manage chat sessions |
| `/memory` | Memory commands |
| `/extensions` | Manage extensions |
| `/settings` | View/edit settings |
| `/stats` | Show usage statistics |

### Cursor Commands

| Command | Description |
|---------|-------------|
| `/summarize` | Summarize content |
| Custom | Via `.cursor/commands/` directory |

---

## Custom Commands

User-defined commands and prompts.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | Skills in ~/.claude/skills/, commands in ~/.claude/commands/ |
| Codex CLI | ✅ Full | Custom prompts in ~/.codex/, invoked as /prompts:name |
| Gemini CLI | ✅ Full | TOML files in ~/.gemini/commands/, supports {{args}} placeholders |
| Cursor | ✅ Full | .cursorrules, Project Rules in .cursor/rules/, Global Rules |

### Claude Code Custom Commands

- **Skills**: `~/.claude/skills/` - Full skill definitions
- **Commands**: `~/.claude/commands/` - Markdown command templates
- Invoked with `/command-name`

### Codex CLI Custom Commands

- Location: `~/.codex/prompts/`
- Invoked as `/prompts:name`
- Supports variable substitution

### Gemini CLI Custom Commands

- Location: `~/.gemini/commands/`
- Format: TOML configuration files
- Supports `{{args}}` placeholders for arguments

### Cursor Custom Commands

- **Project Rules**: `.cursor/rules/` directory
- **Global Rules**: In Cursor settings
- **.cursorrules**: Project-level AI behavior customization

---

## IDE Integration

Editor and development environment support.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | VS Code extension + JetBrains plugin |
| Codex CLI | ✅ Full | VS Code extension + native JetBrains (Jan 2026) |
| Gemini CLI | ✅ Full | VS Code (official) + JetBrains (3rd party plugin) |
| Cursor | ✅ Standalone | VS Code fork - standalone IDE, not a plugin |

### Claude Code IDE Support

- **VS Code**: Official extension
- **JetBrains**: Official plugin for IntelliJ, PyCharm, etc.

### Codex CLI IDE Support

- **VS Code**: Official extension
- **JetBrains**: Native integration (January 2026)

### Gemini CLI IDE Support

- **VS Code**: Official extension
- **JetBrains**: Third-party plugin available

### Cursor IDE

- Standalone IDE based on VS Code fork
- Not available as a plugin for other editors
- Full VS Code extension compatibility

---

## Git Integration

Version control features and automation.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | GitHub + GitLab, PR/MR creation, commit generation |
| Codex CLI | ✅ Full | Deep git integration, GitHub Actions, review workflows |
| Gemini CLI | ⚠️ Partial | Git-aware filtering only; native git operations requested |
| Cursor | ✅ Full | Native git + PR creation via GitHub MCP |

### Claude Code Git Features

- GitHub and GitLab support
- PR/MR creation and management
- Automatic commit message generation
- `/commit` and `/pr-comments` commands
- GitHub Actions integration with `@claude` mentions
- GitLab CI/CD event-driven automation

### Codex CLI Git Features

- Deep git integration
- Built-in `/diff` command for reviewing changes
- GitHub Actions support
- Code review workflows with `/review` command
- Session-based change tracking

### Gemini CLI Git Features

**Currently Available:**
- Git-aware filtering: @ commands exclude git-ignored files by default
- Automatic exclusion of .git/, node_modules/, dist/, .env
- Can execute git operations through shell commands

**Requested Features (Not Yet Available):**
- Native git operations (create commits, branches, PRs)
- Direct git integration tools

### Cursor Git Features

- Git history indexing with commit SHAs and parent info
- Automatic PR indexing for all merged PRs
- Merkle tree-based efficient updates (10-minute intervals)
- GitButler integration for auto-commits

---

## Web Search

Internet search capability for real-time information.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | WebSearch + WebFetch tools (API only, not Bedrock/Vertex) |
| Codex CLI | ✅ Full | Built-in, --search flag for live results |
| Gemini CLI | ✅ Full | Google Search grounding via google_web_search tool |
| Cursor | ✅ Full | @Web command powered by Exa/SerpApi |

### Claude Code Web Search

- **WebSearch**: Search the web for information
- **WebFetch**: Fetch and analyze web pages
- Availability: API only (not on Bedrock/Vertex)

### Codex CLI Web Search

- Built-in web search capability
- `--search` flag for live results
- Integrated into conversation flow

### Gemini CLI Web Search

- Google Search grounding via `google_web_search` tool
- Native Google integration
- Real-time search results

### Cursor Web Search

- `@Web` command
- Powered by Exa/SerpApi
- Context-aware search results

---

## Image Support

Visual input analysis and multimodal capabilities.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ⚠️ Limited | JPEG/PNG/GIF/WebP; some CLI limitations |
| Codex CLI | ✅ Full | --image flag, paste in TUI, multiple images |
| Gemini CLI | ✅ Full | Multimodal input, Windows clipboard paste (Alt+V) |
| Cursor | ⚠️ Partial | Multimodal AI yes; terminal image output limited |

### Claude Code Image Support

- Formats: JPEG, PNG, GIF, WebP
- Some CLI limitations for image display
- Read tool can analyze images

### Codex CLI Image Support

- `--image` flag for image input
- Paste directly in TUI
- Multiple images supported per prompt

### Gemini CLI Image Support

- Full multimodal input support
- Windows clipboard paste with Alt+V
- Image analysis and generation (with appropriate model)

### Cursor Image Support

- Multimodal AI capabilities
- Terminal image output limited
- Works well in IDE context

---

## Memory/Persistence

Cross-session context retention.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ⚠️ Partial | CLAUDE.md files; no native cross-session memory |
| Codex CLI | ✅ Full | JSONL sessions, resume/fork, excellent persistence |
| Gemini CLI | ✅ Full | GEMINI.md files, /memory commands, chat save/resume |
| Cursor | ⚠️ MCP Only | No native memory; requires MCP solutions (knowledge-graph, etc.) |

### Claude Code Memory

- **CLAUDE.md**: Project-level context files
- No native cross-session memory
- Context automatically summarized at compaction

### Codex CLI Memory

- JSONL session files
- `/resume` to continue sessions
- `/fork` to branch sessions
- Excellent persistence support

### Gemini CLI Memory

- **GEMINI.md**: Project-level context
- `/memory` commands for explicit memory management
- Chat save and resume functionality

### Cursor Memory

- No native memory system
- Requires MCP solutions:
  - knowledge-graph MCP
  - Custom memory MCP servers

---

## Multi-file Editing

Coordinated changes across multiple files.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | Coordinated edits, git worktrees for parallel sessions |
| Codex CLI | ✅ Full | Batch operations, parallel tool calling |
| Gemini CLI | ✅ Full | Edit multiple files in one session |
| Cursor | ✅ Full | Composer handles 22,000+ lines, 151+ files |

### Claude Code Multi-file

- Coordinated edits across files
- Git worktrees for parallel editing sessions
- Edit tool with file path specification

### Codex CLI Multi-file

- Batch file operations
- Parallel tool calling
- Atomic multi-file changes

### Gemini CLI Multi-file

- Edit multiple files in single session
- Coordinated changes

### Cursor Multi-file (Composer)

- Industry-leading: 22,000+ lines across 151+ files
- Composer mode for large-scale changes
- Agent mode for autonomous refactoring

---

## Auto-commit

Automatic git commit creation.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ⚠️ Partial | Via custom /commit command and third-party tools |
| Codex CLI | ⚠️ Partial | Can commit but requires approval (by design) |
| Gemini CLI | ✅ Full | Built-in tool + geminicommit CLI |
| Cursor | ✅ Full | Via hooks system and GitButler integration |

### Claude Code Auto-commit

- Custom `/commit` command
- Third-party tools available
- Not fully automatic (by design for safety)

### Codex CLI Auto-commit

- Can create commits
- Requires approval (safety by design)
- Part of approval tier system

### Gemini CLI Auto-commit

- Built-in commit tool
- `geminicommit` CLI for standalone use
- Automatic commit message generation

### Cursor Auto-commit

- Via hooks system (`afterFileEdit`)
- GitButler integration
- Can be fully automated

---

## Custom System Prompts

Customizing AI behavior with system-level instructions.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | CLAUDE.md, --append-system-prompt, Agent SDK, subagents |
| Codex CLI | ⚠️ Experimental | experimental_instructions_file; may break between versions |
| Gemini CLI | ✅ Full | GEMINI_SYSTEM_MD env var for complete override |
| Cursor | ✅ Full | .cursorrules, project rules, global rules |

### Claude Code System Prompts

- **CLAUDE.md**: Project-level instructions
- `--append-system-prompt`: CLI flag for additional instructions
- **Agent SDK**: Full system prompt control
- **Subagents**: Custom system prompts per agent

### Codex CLI System Prompts

- `experimental_instructions_file` option
- May break between versions (experimental)
- Limited official support

### Gemini CLI System Prompts

- `GEMINI_SYSTEM_MD` environment variable
- Complete system prompt override
- GEMINI.md for project context

### Cursor System Prompts

- **.cursorrules**: Project-level AI behavior
- **Project Rules**: `.cursor/rules/` directory
- **Global Rules**: Application-wide settings

---

## Cost Tracking

Token usage and cost monitoring.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ✅ Full | /cost, /stats, workspace-based centralized tracking |
| Codex CLI | ❌ None | No built-in cost tracking; community-requested feature |
| Gemini CLI | ✅ Full | /stats, OpenTelemetry, Google Cloud Monitoring dashboards |
| Cursor | ⚠️ Limited | Basic usage display; no detailed cost breakdown |

### Claude Code Cost Tracking

- `/cost`: Detailed token usage statistics per session
- `/stats`: Usage patterns (subscribers)
- Workspace-based centralized cost tracking via Claude Console
- Auto-created "Claude Code" workspace for organization cost management
- Context awareness feature tracks remaining context window

### Codex CLI Cost Tracking

**Current State:** No built-in cost tracking or usage analytics
- GitHub Issue #5085 proposes cost/usage analytics module
- Users face unpredictable bills without visibility into session costs
- Workaround: Manual tracking based on API pricing

### Gemini CLI Cost Tracking

- `/stats`: Token usage, cached token savings, session duration
- Summary presented on exit
- OpenTelemetry integration
- Google Cloud Monitoring dashboards

### Cursor Cost Tracking

- Basic usage display in UI
- No detailed cost breakdown
- Limited compared to CLI tools

---

## Sandbox Mode

Isolated execution environment for safety.

| Tool | Status | Details |
|------|--------|---------|
| Claude Code | ❌ None | No built-in sandbox |
| Codex CLI | ✅ Full | Landlock (Linux), Seatbelt (macOS), 3 modes (read-only, workspace-write, full-access) |
| Gemini CLI | ✅ Full | Docker/Podman containers, macOS Seatbelt |
| Cursor | ⚠️ Limited | Background agents run in isolated Ubuntu VMs |

### Claude Code Sandbox

- No built-in sandbox
- Relies on user environment isolation

### Codex CLI Sandbox

Three-tier sandbox system:
- **Read-only**: Cannot modify files
- **Workspace-write**: Write only to workspace
- **Full-access**: No restrictions

Technologies:
- **Linux**: Landlock LSM
- **macOS**: Seatbelt sandbox

### Gemini CLI Sandbox

- Docker/Podman container isolation
- macOS Seatbelt for native sandboxing
- Configure via settings

### Cursor Sandbox

- Background agents run in isolated Ubuntu VMs
- Limited sandbox for regular operations

---

## Key Differentiators

| Tool | Strongest Features |
|------|-------------------|
| **Claude Code** | Best hooks system, powerful sub-agents (Task tool), comprehensive MCP support, strong IDE integrations |
| **Codex CLI** | Excellent sandbox security, best session persistence, strong CI/CD support, three-tier approval system |
| **Gemini CLI** | Best extension ecosystem, native Google Cloud integration, 1M token context on all models, built-in cost tracking |
| **Cursor** | Best multi-file editing (Composer), parallel background agents, seamless VS Code experience, codebase indexing |

---

## Research Sources

### Claude Code
- [Claude Code Documentation](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/claude-code)
- [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models)

### Codex CLI
- [Codex CLI GitHub](https://github.com/openai/codex)
- [OpenAI Platform](https://platform.openai.com/docs)

### Gemini CLI
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
- [Gemini Extensions](https://geminicli.com/extensions)

### Cursor
- [Cursor Documentation](https://cursor.com/docs)
- [Cursor Changelog](https://cursor.com/changelog)
```

## File: `research/2026-02-03_21-13-09/research.md`
```markdown
# Context Window Research Session

**Started:** 2026-02-03 21:13:09
**Status:** Complete

---

## Claude Code Research
**Agent:** Dr. Sarah Chen
**Status:** Complete
**Research Date:** 2026-02-03
**Documentation Version:** Latest (February 2026)

### Models Found

| Model | Model ID | Context Window | Max Output | Notes |
|-------|----------|----------------|------------|-------|
| Opus 4.5 | claude-opus-4-5-20251101 | 200K tokens | 64K tokens | Premium model combining maximum intelligence with practical performance. Default for complex reasoning tasks. |
| Sonnet 4.5 | claude-sonnet-4-5-20250929 | 200K tokens / 1M tokens (beta) | 64K tokens | **Default model**. Best for complex agents and coding. 1M context requires `context-1m-2025-08-07` beta header. Long context pricing applies >200K. |
| Haiku 4.5 | claude-haiku-4-5-20251001 | 200K tokens | 64K tokens | Fastest model with near-frontier intelligence. Best for speed-critical tasks. |
| Sonnet 4 | claude-sonnet-4-20250514 | 200K tokens / 1M tokens (beta) | 64K tokens | Legacy model. Still available but migration to 4.5 recommended. Supports 1M context with beta header. |
| Haiku 3.5 | claude-3-5-haiku-20241022 | 200K tokens | 4K tokens | Legacy model. Limited output compared to newer models. |

### Key Findings

- **Default Model**: Sonnet 4.5 is the default and recommended model for most Claude Code use cases, offering the best balance of intelligence, speed, and cost
- **Extended Context Beta**: Both Sonnet 4.5 and Sonnet 4 support 1M token context windows when using the `context-1m-2025-08-07` beta header via the `--betas` flag
- **Extended Thinking**: All Claude 4.5 models (Opus, Sonnet, Haiku) support extended thinking and interleaved thinking features
- **Output Limits**: Claude 4.5 models support up to 64K tokens output, significantly higher than Haiku 3.5's 4K limit
- **Model Selection**: Can be changed via `/model` command (interactive), `--model` flag (single session), or `ANTHROPIC_MODEL` environment variable (permanent)
- **Legacy Models**: Claude Opus 4 and 4.1 have been removed from Claude Code. Only Opus 4.5 is currently available
- **Knowledge Cutoffs**:
  - Opus 4.5: May 2025 (reliable), Aug 2025 (training data)
  - Sonnet 4.5: Jan 2025 (reliable), Jul 2025 (training data)
  - Haiku 4.5: Feb 2025 (reliable), Jul 2025 (training data)

### Context Window Capabilities

**Standard Context (All Models):**
- 200K tokens (~150,000 words or ~680,000 unicode characters)
- No special configuration required
- Standard pricing applies

**Extended Context (Sonnet 4.5 & Sonnet 4 only):**
- 1M tokens (~750,000 words or ~3.4M unicode characters)
- Requires beta header: `claude --betas context-1m-2025-08-07`
- Long context pricing applies to tokens exceeding 200K
- Currently in beta for usage tier 4 organizations and custom rate limit users

### Configuration Methods

1. **Interactive Mode**: Use `/model` command to switch models
2. **Session Flag**: `claude --model opus` or `claude --model claude-sonnet-4-5-20250929`
3. **Environment Variable**: Set `ANTHROPIC_MODEL` in shell config
4. **Beta Features**: Use `--betas interleaved-thinking` or `--betas context-1m-2025-08-07`

### Pricing (Per Million Tokens)

| Model | Input Cost | Output Cost |
|-------|-----------|-------------|
| Opus 4.5 | $5 | $25 |
| Sonnet 4.5 | $3 | $15 |
| Haiku 4.5 | $1 | $5 |

Note: Long context pricing (>200K tokens) and extended thinking have additional costs. See official pricing page for details.

### Model Aliases

- `opus` → claude-opus-4-5-20251101
- `sonnet` → claude-sonnet-4-5-20250929
- `haiku` → claude-haiku-4-5-20251001

Aliases automatically point to the latest model snapshot and may update when new versions are released.

### Sources

- [Models Overview - Claude API Docs](https://platform.claude.com/brain/knowledge/docs_legacy/en/about-claude/models)
- [CLI Reference - Claude Code Docs](https://code.claude.com/brain/knowledge/docs_legacy/en/cli-reference)
- [Claude Code Model Configuration - Help Center](https://support.claude.com/en/articles/11940350-claude-code-model-configuration)
- [Context Windows - Claude API Docs](https://platform.claude.com/brain/knowledge/docs_legacy/en/build-with-claude/context-windows)
- [What's New in Claude 4.5](https://platform.claude.com/brain/knowledge/docs_legacy/en/about-claude/models/whats-new-claude-4-5)

---

## Codex CLI Research
**Agent:** Marcus Thompson
**Status:** Complete
**Research Date:** 2026-02-03
**Documentation Version:** Latest (February 2026)

### Models Found

| Model | Model ID | Context Window | Max Output | Notes |
|-------|----------|----------------|------------|-------|
| Codex-1 | codex-1 | 192k tokens | N/A | Version of o3 optimized for software engineering, tested at 192k with medium reasoning effort |
| Codex Mini Latest | codex-mini-latest | 200k tokens | 100k tokens | Fine-tuned version of o4-mini for Codex CLI, **default model**, supports reasoning tokens |
| GPT-5.2-Codex | gpt-5.2-codex | 400k tokens | 128k tokens | Most advanced agentic coding model with context compaction, knowledge cutoff: Aug 31, 2025 |
| GPT-5.1-Codex-Max | gpt-5.1-codex-max | 400k+ tokens | 128k tokens | First model with native context compaction, works across millions of tokens via automatic compaction |
| GPT-5.1-Codex-Mini | gpt-5.1-codex-mini | 400k tokens | 128k tokens | Lighter, more affordable variant of GPT-5.1-Codex with reduced capabilities |
| O3 | o3 | 200k tokens | 100k tokens | Base reasoning model, codex-1 is derived from this |
| O4-Mini | o4-mini | 200k tokens | 100k tokens | Fast reasoning model, codex-mini-latest is derived from this |

### Key Findings

- **Codex CLI Launch**: OpenAI launched Codex CLI on April 15, 2025, as a lightweight coding agent that runs in the terminal
- **Context Compaction**: GPT-5.1-Codex-Max and GPT-5.2-Codex feature revolutionary context compaction technology that automatically summarizes sessions when approaching context limits, enabling work across millions of tokens
- **Model Hierarchy**: Two main families exist:
  - **O-series derivatives**: codex-1 (from o3) and codex-mini-latest (from o4-mini) with 192k-200k windows
  - **GPT-5.x Codex series**: GPT-5.1 and GPT-5.2 variants with 400k windows and advanced agentic capabilities
- **Default Model**: codex-mini-latest is the default model in Codex CLI, optimized for low-latency code Q&A and editing
- **Reasoning Tokens**: All Codex models support reasoning tokens, allowing them to think through problems before responding
- **Open Source**: Codex CLI is fully open-source at github.com/openai/codex
- **Availability**: Rolling out to ChatGPT Pro, Enterprise, and Business users, with Plus and Edu support coming soon
- **Extended Context Testing**: For specialized benchmarks like SWE-bench, models were tested with 256k context length
- **Training Approach**: codex-1 was trained using reinforcement learning on real-world coding tasks to generate human-style code

### Pricing (Per Million Tokens)

| Model | Input Cost | Output Cost | Cache Discount |
|-------|-----------|-------------|----------------|
| codex-mini-latest | $1.50 | $6.00 | 75% prompt caching |

Note: Pricing for other models available through API documentation.

### Sources

- [Codex Models](https://developers.openai.com/codex/models/)
- [Introducing GPT-5.2-Codex | OpenAI](https://openai.com/index/introducing-gpt-5-2-codex/)
- [Building more with GPT-5.1-Codex-Max | OpenAI](https://openai.com/index/gpt-5-1-codex-max/)
- [GPT-5.2-Codex Model | OpenAI API](https://platform.openai.com/brain/knowledge/docs_legacy/models/gpt-5.2-codex)
- [GPT-5.1 Codex Model | OpenAI API](https://platform.openai.com/brain/knowledge/docs_legacy/models/gpt-5.1-codex)
- [codex-mini-latest Model | OpenAI API](https://platform.openai.com/brain/knowledge/docs_legacy/models/codex-mini-latest)
- [o4-mini Model | OpenAI API](https://platform.openai.com/brain/knowledge/docs_legacy/models/o4-mini)
- [o3 Model | OpenAI API](https://platform.openai.com/brain/knowledge/docs_legacy/models/o3)
- [Introducing Codex | OpenAI](https://openai.com/index/introducing-codex/)
- [Introducing OpenAI o3 and o4-mini | OpenAI](https://openai.com/index/introducing-o3-and-o4-mini/)
- [GitHub - openai/codex](https://github.com/openai/codex)
- [Elvis on X about codex-mini-latest](https://x.com/omarsar0/status/1923408662422311203)
- [GPT-5.1 Codex mini Model | OpenAI API](https://platform.openai.com/brain/knowledge/docs_legacy/models/gpt-5.1-codex-mini)

---

## Cursor Research
**Agent:** Elena Rodriguez
**Status:** Complete
**Research Date:** 2026-02-03

### Models Found

| Model | Provider | Context Window | Max Output | Notes |
|-------|----------|----------------|------------|-------|
| Claude Opus 4.5 | Anthropic | 200K tokens | 64K tokens | Premium reasoning model. Released Nov 2025. 80.9% on SWE-bench. Pricing increased in Cursor after initial release. |
| Claude Sonnet 4.5 | Anthropic | 200K / 1M tokens (Max) | 64K tokens | Default Claude model. Released Sept 2025. 1M context requires Max mode with auto `context-1m` flag. |
| Claude Haiku 4.5 | Anthropic | 200K tokens | 64K tokens | Fast Claude model. Released Oct 2025. Knowledge cutoff: Feb 2025. |
| Claude 3.7 Sonnet | Anthropic | 48K / 200K tokens (Max) | 4K / 64K tokens | Legacy model available in Max mode with 200 agent tool call limit. |
| Composer 1 | Cursor (Native) | 150-180K tokens (effective) | N/A | Cursor's native MoE model. 250 tokens/sec output. 4x faster generation. $1.25/M input, $10/M output. |
| GPT-5.2 | OpenAI | 400K tokens | 128K tokens | Latest flagship released Dec 2025. Three modes: Auto, Instant, Thinking. |
| GPT-5.2 Codex | OpenAI | 400K tokens | 128K tokens | Available in Cursor since mid-Jan 2026. Specialized for agentic coding. |
| GPT-5.1 Codex | OpenAI | 400K tokens | 128K tokens | Previous generation, now superseded by GPT-5.2. Still available. |
| GPT-5 | OpenAI | 400K tokens | 128K tokens | Base GPT-5 model. Released Nov 2025. |
| o3 | OpenAI | 200K tokens | 100K tokens | Advanced reasoning model. $2-8/M tokens. Available via "Show additional models" toggle. |
| Gemini 3 Pro | Google | 1M tokens | 65K tokens | Highest context window available. 76.8% SWE-bench. Available in Max mode. Strong for agentic tasks. |
| Gemini 3 Flash | Google | 1M tokens | 65K tokens | 78% SWE-bench (outperforms 3 Pro). 4x lower cost, 3x faster. $0.50/M input, $3/M output. |
| Gemini 2.5 Pro | Google | 1M tokens | 65K tokens | Previous generation. Available in Max mode. State-of-the-art reasoning. |
| Gemini 2.5 Flash | Google | 1M tokens | 65K tokens | Legacy Flash model. Still available. Best price-performance in 2.5 series. |
| Grok Code Fast 1 | xAI | 256K tokens | N/A | 70.8% SWE-bench. Fastest model. $0.20/M input, $1.50/M output. Free trial period. |
| DeepSeek Coder V2 | DeepSeek | 128K tokens | N/A | Cursor-hosted option. Open-source, cost-effective. Native support since v0.44+. |
| DeepSeek V3 | DeepSeek | 64-128K tokens | N/A | Latest version. 64K effective in consumer app, 128K documented. Native Cursor support. |

### Key Findings

- **Model Diversity**: Cursor supports 4 major providers (Anthropic, OpenAI, Google, xAI) plus native Composer model and DeepSeek integration
- **Subscription Tiers**: Pro ($20/month), Pro+ ($60/month - 3x usage), Ultra ($200/month - 20x usage)
- **Usage-Based Credits**: Pro plan provides $20 credit pool (~225 Sonnet 4.5 requests, ~550 Gemini requests, ~500 GPT-5 requests)
- **Max Mode**: Extends context to maximum available per model (1M for Gemini 3, Sonnet 4.5 with auto flag). Slower and more expensive.
- **Normal Mode**: Default 200K token context (~15,000 lines of code) for most models
- **Composer Performance**: Native model outputs at 250 tokens/sec, ~2x faster than similar models, completes turns in <30 seconds
- **Auto Model Selection**: Cursor can automatically select best-performing model based on task and demand
- **Context Window Strategy**: Cursor emphasizes "right context over more context" - quality vs quantity
- **Grok Code**: Free trial period available. Designed for agentic work with tool calling
- **Recent Additions**: GPT-5.2 Codex added mid-Jan 2026, Gemini 3 models added late 2025/early 2026
- **Claude Sonnet 5**: Expected to launch Feb 3, 2026 (this week) - will outperform Opus 4.5 at 50% lower cost
- **Max Mode Features**: 750 lines per file read operation, automatic 1M context flag for Claude models
- **DeepSeek Integration**: Native support for V3 and Coder V2, cost-effective alternative to frontier models

### Context Window Comparison

| Context Size | Models |
|--------------|--------|
| 1M tokens | Gemini 3 Pro, Gemini 3 Flash, Gemini 2.5 Pro, Gemini 2.5 Flash, Claude Sonnet 4.5 (Max mode) |
| 400K tokens | GPT-5, GPT-5.1, GPT-5.2, GPT-5.2 Codex |
| 256K tokens | Grok Code Fast 1 |
| 200K tokens | Claude Opus 4.5, Claude Sonnet 4.5, Claude Haiku 4.5, Claude 3.7 (Max), o3 |
| 150-180K tokens | Composer 1 (effective) |
| 128K tokens | DeepSeek Coder V2 |
| 64-128K tokens | DeepSeek V3 |
| 48K tokens | Claude 3.7 Sonnet (Normal) |

### Pricing Structure

**Anthropic Models (API Pricing):**
- Haiku 4.5: $1/M input, $5/M output
- Sonnet 4.5: $3/M input, $15/M output
- Opus 4.5: $5/M input, $25/M output

**Google Models:**
- Gemini 3 Flash: $0.50/M input, $3/M output
- Gemini 3 Pro: Higher cost than Flash (4x)

**xAI Models:**
- Grok Code Fast 1: $0.20/M input, $1.50/M output

**Cursor Native:**
- Composer 1: $1.25/M input, $10/M output

**OpenAI Models:**
- o3: $2-8/M tokens
- GPT-5 series: Standard OpenAI pricing

### CLI Commands

- `/models` - List all available models and switch between them
- `--list-models` - CLI flag to list models
- `agent models` - Background agent API command

### Model Selection Strategy (Community Recommendations)

Based on Cursor forum discussions, users recommend:
- **Agent**: GPT-5.2 XHigh for complex planning
- **Subagents - DB Tasks**: Opus 4.5 for database work
- **Subagents - Senior Tasks**: GPT-5.2 XHigh for architecture
- **Subagents - Middle+ Tasks**: Codex 5.2 XHigh for implementation
- **Subagents - Middle Tasks**: Gemini 3 Flash for standard coding
- **Subagents - Junior Tasks**: Grok Code Fast for simple tasks
- **Verifier**: Gemini 3 Flash for fast verification

### Sources

- [Models | Cursor Docs](https://cursor.com/brain/knowledge/docs_legacy/models)
- [Cursor Changelog](https://cursor.com/changelog)
- [Cursor CLI (Jan 8, 2026) - Announcements](https://forum.cursor.com/t/cursor-cli-jan-8-2026-new-commands-and-performance-improvement/148372)
- [Choosing the Right Model in Cursor - Frontend Masters Blog](https://frontendmasters.com/blog/choosing-the-right-model-in-cursor/)
- [How To Optimize Your Usage v3.0 - Cursor Forum](https://forum.cursor.com/t/how-to-optimize-your-usage-the-best-ai-models-to-use-version-3-0/145657)
- [GPT 5.2 Codex Available in Cursor - Forum](https://forum.cursor.com/t/gpt-5-2-codex-available-in-cursor/148901)
- [Introducing GPT-5.2 | OpenAI](https://openai.com/index/introducing-gpt-5-2/)
- [Introducing Claude Opus 4.5 | Anthropic](https://www.anthropic.com/news/claude-opus-4-5)
- [Gemini 3 Flash - Release Discussion](https://forum.cursor.com/t/gemini-3-flash-out-now/146648)
- [Grok Code Fast 1 | xAI](https://x.ai/news/grok-code-fast-1)
- [Introducing Composer: Cursor's First Native AI Coding Model](https://skywork.ai/blog/vibecoding/cursor-composer-ai-model/)
- [Cursor Pricing](https://cursor.com/pricing)
- [DeepSeek V3 with Cursor Guide](https://apidog.com/blog/deepseek-v3-cursor-guide/)
- [Claude Opus 4.5 vs GPT-5.2 Comparison](https://www.digitalapplied.com/blog/claude-opus-4-5-vs-gpt-5-2-codex-vs-gemini-3-pro-comparison)
- [Best AI Models 2026 Comparison](https://www.humai.blog/best-ai-models-2026-gpt-5-vs-claude-4-5-opus-vs-gemini-3-pro-complete-comparison/)
- [Cursor vs Claude Code Comparison](https://www.builder.io/blog/cursor-vs-claude-code)
- [Introducing Composer Blog Post](https://cursor.com/blog/2-0)

---

## Gemini CLI Research
**Agent:** Dr. Raj Patel
**Status:** Complete
**Research Date:** 2026-02-03
**Documentation Version:** Latest (February 2026)

### Models Found

| Model | Model ID | Context Window | Max Output | Status |
|-------|----------|----------------|------------|--------|
| Gemini 3 Pro | gemini-3-pro-preview | 1M tokens (1,048,576) | 65,536 tokens | Preview (November 2025) - Available with paid tier |
| Gemini 3 Flash | gemini-3-flash-preview | 1M tokens (1,048,576) | 65,536 tokens | Preview (December 2025) - Available with paid tier |
| Gemini 2.5 Pro | gemini-2.5-pro | 1M tokens (1,048,576) | 65,536 tokens | Stable GA (June 2025) - State-of-the-art reasoning |
| Gemini 2.5 Flash | gemini-2.5-flash | 1M tokens (1,048,576) | 65,536 tokens | Stable GA (June 2025) - Best price-performance |
| Gemini 2.5 Flash-Lite | gemini-2.5-flash-lite | 1M tokens (1,048,576) | 65,536 tokens | Stable GA (July 2025) - Fastest, cost-optimized |
| Gemini 1.5 Pro | gemini-1.5-pro-002 | 1M tokens / 2M tokens | 8,192 tokens | **DEPRECATED** - Shut down September 2025 |
| Gemini 1.5 Flash | gemini-1.5-flash-002 | 1M tokens | 8,192 tokens | **DEPRECATED** - Shut down September 2025 |
| Gemini 2.0 Flash | gemini-2.0-flash | 1M tokens | 8,192 tokens | **SHUTTING DOWN** - March 31, 2026 |
| Gemini 2.0 Flash-Lite | gemini-2.0-flash-lite | 1M tokens | 8,192 tokens | **SHUTTING DOWN** - March 31, 2026 |

### Key Findings

- **Current Generation**: Gemini 3 series (Pro and Flash) are the latest preview models available in CLI, offering frontier-class multimodal capabilities
- **Production Stable**: Gemini 2.5 series (Pro, Flash, Flash-Lite) are stable GA models recommended for production use
- **Consistent Context**: All current-generation models (Gemini 2.5 and 3.x) support 1M token context windows as standard
- **Increased Output**: Current models support 65,536 tokens output (8x more than previous generations' 8K limit)
- **2M Context Deprecated**: Gemini 1.5 Pro's 2M token context window capability was available but the model has been deprecated (shutdown September 2025)
- **Migration Required**: Gemini 2.0 models shutting down March 31, 2026 - users must migrate to 2.5 or 3.x series
- **Multimodal Support**: All current models support text, image, video, audio, and PDF inputs
- **Auto Selection**: CLI offers "Auto" mode that intelligently selects between Gemini 3 or 2.5 models based on task complexity
- **Access Control**: Gemini 3 models require paid tier (Google AI Pro/Ultra, paid API key, or Gemini Code Assist with admin preview access)
- **Alias Tracking**: `gemini-pro-latest` and `gemini-flash-latest` now point to Gemini 3 models (as of January 2026)

### Context Window Capabilities

**All Current Models (2.5 and 3.x):**
- 1,048,576 tokens (1M) input context window
- Equivalent to:
  - 50,000 lines of code
  - 8 average-length English novels
  - 1 hour of video content
  - 11 hours of audio
  - 700,000+ words

**Output Tokens:**
- Current generation: 65,536 tokens (65K)
- Legacy models: 8,192 tokens (8K)

**Historical Note:**
- Gemini 1.5 Pro supported up to 2M tokens but has been shut down
- No current models offer 2M context windows

### Model Selection in CLI

**Auto Mode (Recommended):**
- `Auto (Gemini 3)`: Automatically selects between gemini-3-pro-preview and gemini-3-flash-preview
- `Auto (Gemini 2.5)`: Automatically selects between gemini-2.5-pro and gemini-2.5-flash

**Manual Selection:**
Users can manually select specific models via the `/model` command or `-m` flag:
```bash
gemini -m gemini-2.5-flash
gemini -m gemini-3-pro-preview
```

**Requirements for Gemini 3 Access:**
1. Upgrade CLI to version 0.21.1 or later
2. Run `/settings` and enable "Preview features"
3. Use `/model` to select Gemini 3 models

### Version and Release Timeline

- **January 2026**: Gemini 3 models support Computer Use tool; gemini-3-pro-image-preview released
- **December 2025**: Gemini 3 Flash preview released
- **November 2025**: Gemini 3 Pro preview released
- **July 2025**: Gemini 2.5 Flash-Lite stable release
- **June 2025**: Gemini 2.5 Pro and Flash stable releases
- **September 2025**: Gemini 1.5 models shut down
- **March 31, 2026**: Gemini 2.0 models scheduled shutdown

### Performance Highlights

**Gemini 3 Flash:**
- 78% score on SWE-bench Verified for agentic coding
- Outperforms both Gemini 2.5 series and Gemini 3 Pro on coding tasks
- Optimized for high-frequency terminal-based workflows

**Gemini 2.5 Flash:**
- Best price-performance ratio in the lineup
- Upgraded reasoning and hybrid thinking control
- Production-ready stability

**Gemini 2.5 Pro:**
- State-of-the-art thinking model for complex reasoning
- Handles challenging problems across multiple information sources

### Sources

- [Gemini Models Documentation - Google AI for Developers](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models)
- [Long Context Support - Gemini API Docs](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/long-context)
- [Gemini CLI GitHub Repository](https://github.com/google-gemini/gemini-cli)
- [Gemini 3 Flash Announcement - Google Developers Blog](https://developers.googleblog.com/gemini-3-flash-is-now-available-in-gemini-cli/)
- [Gemini CLI Model Selection Documentation](https://geminicli.com/brain/knowledge/docs_legacy/cli/model/)
- [Release Notes - Gemini API Changelog](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/changelog)
- [Google Gemini Context Window Guide - DataStudios](https://www.datastudios.org/post/google-gemini-context-window-token-limits-model-comparison-and-workflow-strategies-for-late-2025)
- [Gemini 3 Context Window Analysis - Thinkpeak AI](https://thinkpeak.ai/gemini-3-context-window-size-1-2m-tokens/)
- [Gemini 1.5 Pro 2M Context Window Announcement - Google Developers Blog](https://developers.googleblog.com/en/new-features-for-the-gemini-api-and-google-ai-studio/)
- [Gemini 3 Overview - Google Blog](https://blog.google/products/gemini/gemini-3/)
- [Gemini 3 Flash Benchmarks - Google Blog](https://blog.google/products/gemini/gemini-3-flash/)

---
```

## File: `research/2026-02-03_21-13-09/result.md`
```markdown
# Research Results

**Completed:** 2026-02-03 21:13:09
**Status:** Complete - README Updated

---

## Summary

| Tool | Models Found | Changes Detected |
|------|--------------|------------------|
| Claude Code | 5 (3 current + 2 legacy) | Minor - Legacy models added |
| Codex CLI | 7 | Yes - codex-mini renamed to codex-mini-latest |
| Cursor | 17 | Yes - New models: Composer 1, Grok Code Fast 1, DeepSeek |
| Gemini CLI | 9 (5 current + 4 deprecated) | Minor - Deprecation dates confirmed |

---

## Proposed README Updates

```markdown
## Context Window Comparison

| Tool | Largest Context | Best Model | Source |
|------|-----------------|------------|--------|
| Claude Code | 1M (beta) | Sonnet 4.5 with `--betas context-1m-2025-08-07` | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
| Codex CLI | 400k+ | GPT-5.2-Codex (with context compaction) | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
| Cursor | 1M (Max mode) | Gemini 3 Pro/Flash | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
| Gemini CLI | 1M | Gemini 3 Pro Preview | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |
```

---

## Diff: Current vs New

### README.md Changes

```diff
 | Tool | Largest Context | Best Model | Source |
 |------|-----------------|------------|--------|
-| Claude Code | 1M (beta) | Sonnet 4.5 with `[1m]` suffix | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
+| Claude Code | 1M (beta) | Sonnet 4.5 with `--betas context-1m-2025-08-07` | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
 | Codex CLI | 400k | GPT-5.2-Codex | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
-| Cursor | 2M (Max mode) | Grok 4 Fast | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
+| Cursor | 1M (Max mode) | Gemini 3 Pro/Flash | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
 | Gemini CLI | 1M | Gemini 3 Pro Preview | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |
```

### Key Differences Found

#### Claude Code
- **Current README**: Shows `[1m]` suffix for extended context
- **New Research**: Requires `--betas context-1m-2025-08-07` flag (more accurate)
- **Added**: Legacy models (Sonnet 4, Haiku 3.5) still available

#### Codex CLI
- **Current README**: Lists `codex-mini`
- **New Research**: Model renamed to `codex-mini-latest` (default model)
- **Confirmed**: GPT-5.2-Codex with 400k context is latest

#### Cursor
- **Current README**: Claims 2M context with Grok 4 Fast
- **New Research**: No 2M context found - Grok Code Fast 1 has 256k, max is 1M with Gemini models
- **Added**: Composer 1 (Cursor native), DeepSeek V3, Grok Code Fast 1
- **Correction**: Best large-context model is Gemini 3 Pro/Flash at 1M

#### Gemini CLI
- **Current README**: Accurate - 1M context, Gemini 3 Pro Preview
- **New Research**: Confirms data, adds deprecation timeline for 2.0/2.5 models
- **Note**: 2M context (Gemini 1.5 Pro) is retired

---

## Proposed Report Updates (reports/context-comparison.md)

### Claude Code Section
```diff
 ### Model Selection

 - During session: `/model <alias>`
 - At startup: `claude --model <alias>`
 - Environment: `ANTHROPIC_MODEL=<alias>`
-- Aliases: `opus`, `sonnet`, `haiku`, `sonnet[1m]`, `opusplan`
+- Aliases: `opus`, `sonnet`, `haiku`, `opusplan`
+- Extended context: `claude --betas context-1m-2025-08-07`
```

### Codex CLI Section
```diff
 | Model | Context Window | Max Output | Notes |
 |-------|----------------|------------|-------|
 | GPT-5.2-Codex | 400k | 128k | Default since Jan 2026, context compaction support |
-| GPT-5.1-Codex-Max | 400k | 128k | Long-horizon agentic tasks |
-| GPT-5.1-Codex | 400k | 128k | Agentic coding optimized |
-| GPT-5.1-Codex-Mini | 400k | 128k | Cost-effective |
-| GPT-5-Codex | 400k | 128k | Context compaction support |
-| GPT-5 | 400k | 128k | General purpose |
+| GPT-5.1-Codex-Max | 400k+ | 128k | Native context compaction, works across millions of tokens |
+| GPT-5.1-Codex-Mini | 400k | 128k | Lighter, more affordable variant |
 | codex-1 | 192k | - | Specialized o3 variant for coding |
-| codex-mini | 200k | 100k | Fine-tuned o4-mini, low-latency |
+| codex-mini-latest | 200k | 100k | **Default model**, fine-tuned o4-mini, low-latency |
 | o3 | 200k | 100k | Latest reasoning model |
 | o4-mini | 200k | 100k | Fast, efficient reasoning |
```

### Cursor Section
```diff
+### Cursor Native Models
+
+| Model | Context Window | Max Output | Notes |
+|-------|----------------|------------|-------|
+| Composer 1 | 150-180k | N/A | Native MoE model, 250 tokens/sec, $1.25/M input |
+
 ### xAI Models

 | Model | Context Window | Max Output | Notes |
 |-------|----------------|------------|-------|
-| Grok 4 | 256k | 8k | Agent/Thinking modes |
-| Grok 4 Fast | 200k (2M max) | 8k | **Largest context available** |
-| Grok Code | 256k | 8k | Code-specialized |
+| Grok Code Fast 1 | 256k | N/A | 70.8% SWE-bench, fastest, $0.20/M input |
+
+### DeepSeek Models
+
+| Model | Context Window | Max Output | Notes |
+|-------|----------------|------------|-------|
+| DeepSeek Coder V2 | 128k | N/A | Open-source, cost-effective |
+| DeepSeek V3 | 64-128k | N/A | Native Cursor support, free |
```

### Gemini CLI Section
```diff
+### Deprecation Timeline
+
+| Model | Shutdown Date |
+|-------|---------------|
+| Gemini 2.0 Flash | March 31, 2026 |
+| Gemini 2.0 Flash-Lite | March 31, 2026 |
+| Gemini 2.5 Pro | June 17, 2026 |
+| Gemini 2.5 Flash | June 17, 2026 |
+| Gemini 2.5 Flash-Lite | July 22, 2026 |
```

---

## Corrections Required

1. **Cursor 2M Context**: The current README claims Cursor has 2M context with Grok 4 Fast. Research found no evidence of this - maximum is 1M with Gemini models. The "Grok 4 Fast" model appears to be "Grok Code Fast 1" with 256k context.

2. **Claude Code Extended Context**: The `[1m]` suffix notation should be replaced with the actual beta flag: `--betas context-1m-2025-08-07`

3. **Codex CLI Default Model**: `codex-mini` should be `codex-mini-latest` as this is the official model ID.

---

## Research Session Complete

All 4 agents completed their research successfully. The research.md file contains detailed findings from each agent with sources.

---

## Update Applied

**User Approved:** Yes
**Updated Files:**
- `README.md` - Quick comparison table corrected
- `reports/context-comparison.md` - Full report updated with:
  - Claude Code: Fixed extended context syntax
  - Codex CLI: Renamed codex-mini to codex-mini-latest, streamlined model list
  - Cursor: Removed incorrect 2M claim, added Composer 1, DeepSeek models, Grok Code Fast 1
  - Gemini CLI: Added deprecation timeline
```

## File: `research/2026-02-04_12-30-00/research.md`
```markdown
# Context Window & Features Research Session

**Started:** 2026-02-04 12:30:00
**Completed:** 2026-02-04
**Status:** Complete

---

## Claude Code Research
**Agent:** Dr. Sarah Chen
**Status:** Complete

### Context Windows

| Model | Context Window | Max Output | Notes |
|-------|----------------|------------|-------|
| Claude Opus 4.5 | 200K tokens | 64K tokens | Released Nov 24, 2025; flagship model at 67% lower cost than predecessor |
| Claude Sonnet 4.5 | 200K tokens / 1M tokens (beta) | 64K tokens | 1M beta requires `context-1m-2025-08-07` header; best coding model; context awareness feature |
| Claude Haiku 4.5 | 200K tokens | 64K tokens | Fastest model; unbeatable for UI work; context awareness feature |

**Legacy Models (Still Available):**
- Claude Opus 4.1: 200K tokens, 32K max output ($15/$75 per MTok)
- Claude Sonnet 4: 200K / 1M beta, 64K max output
- Claude Sonnet 3.7: 200K tokens, 64K / 128K beta max output
- Claude Opus 4: 200K tokens, 32K max output
- Claude Haiku 3: 200K tokens, 4K max output

**Key Details:**
- Context window budget set to 200K (standard), 500K (Enterprise), or 1M (beta for tier 4 orgs)
- Sonnet 4.5 and Haiku 4.5 feature **context awareness**: models track remaining context window throughout conversation
- Long context pricing applies to requests exceeding 200K tokens
- Model aliases (e.g., `claude-sonnet-4-5`) auto-point to latest snapshot; use specific versions in production
- Extended thinking enabled by default with 31,999 token budget

### Features

#### Hooks Support
**Status:** Full support with comprehensive event system

**Event Types:**
- `SessionStart` - When session begins/resumes (matcher: startup/resume/clear/compact)
- `UserPromptSubmit` - Before Claude processes user prompt
- `PreToolUse` - Before tool execution; can block (matcher: tool name)
- `PermissionRequest` - When permission dialog appears (matcher: tool name)
- `PostToolUse` - After successful tool execution (matcher: tool name)
- `PostToolUseFailure` - After tool execution fails (matcher: tool name)
- `Notification` - When Claude Code sends notifications (matcher: permission_prompt/idle_prompt/auth_success/elicitation_dialog)
- `SubagentStart` - When subagent spawns (matcher: agent type)
- `SubagentStop` - When subagent finishes (matcher: agent type)
- `Stop` - When Claude finishes responding
- `PreCompact` - Before context compaction (matcher: manual/auto)
- `SessionEnd` - When session terminates (matcher: reason codes)

**Hook Types:**
- Command hooks (`type: "command"`) - Execute shell scripts
- Prompt hooks (`type: "prompt"`) - Single-turn LLM evaluation
- Agent hooks (`type: "agent"`) - Multi-turn subagent with tool access
- Async hooks support with `"async": true` for non-blocking execution

**Hook Locations:**
- `~/.claude/settings.json` (global)
- `.claude/settings.json` (project, shareable)
- `.claude/settings.local.json` (project, gitignored)
- Managed policy settings (organization-wide)
- Plugin `hooks/hooks.json`
- Skill/agent frontmatter

**Management:**
- `/hooks` interactive menu for viewing, adding, deleting hooks
- Environment variables: `$CLAUDE_PROJECT_DIR`, `${CLAUDE_PLUGIN_ROOT}`, `$CLAUDE_ENV_FILE`
- Decision control: allow/deny/ask with reason, updatedInput, additionalContext
- JSON input/output on stdin/stdout, exit codes for control

#### MCP (Model Context Protocol) Support
**Status:** Full support with plugin integration

- MCP server tools appear as regular tools in hook events
- Naming pattern: `mcp__<server>__<tool>` (e.g., `mcp__memory__create_entities`)
- Configurable via `.mcp.json` in plugins
- Auto-enable threshold with `auto:N` syntax (N = context window percentage 0-100)
- MCP tools can be matched in hooks using regex patterns
- Supports external tool configuration with MCP servers

#### Sub-agents/Task Tool
**Status:** Full support with recent v2.1.16+ major improvements

**Built-in Sub-agents:**
- Fast, read-only agent for searching/analyzing codebases
- Specialized agents: Bash, Explore, Plan
- Up to 7 agents running simultaneously

**Recent Updates (v2.1.16, January 2026):**
- Moved from ephemeral "To-dos" to persistent "Tasks"
- Support for directed acyclic graphs (DAGs) where tasks can block others
- Coordinating work across sessions, subagents, and context windows
- v2.1.17 patch fixed out-of-memory crashes with heavy subagent usage

**Custom Sub-agents:**
- Define in Markdown files with YAML frontmatter
- Located in `.claude/agents/`
- Custom prompts, tool restrictions, permission modes, hooks, and skills
- Created manually or via `/agents` command
- Can be invoked via Task tool with `subagent_type` parameter

#### Slash Commands
**Status:** Full support, merged with skills system (v2.1.3+)

**Built-in Commands:**
- `/help` - Show all commands
- `/clear` - Clear history
- `/init` - Create CLAUDE.md
- `/doctor` - Diagnose issues
- `/compact` - Compact context
- `/resume` - Resume session
- `/config` - Configuration management
- `/cost` - Display token usage and costs
- `/stats` - View usage patterns (subscribers)
- `/hooks` - Interactive hooks manager
- `/agents` - Manage custom agents

**Custom Commands:**
- Store in `~/.claude/commands/` (global) or `.claude/commands/` (project)
- Markdown files with `.md` extension
- Use `$ARGUMENTS` placeholder for parameters
- Written in natural language
- Unified with skills system: commands and skills create same `/command` interface

#### Custom Commands/Skills
**Status:** Full support with unified system

- Skills stored in `.claude/skills/<name>/SKILL.md`
- Commands and skills merged in v2.1.3 - both work identically
- YAML frontmatter for configuration
- Supports hooks, custom prompts, tool restrictions
- Can include `once: true` for single-run hooks
- Agent Skills available for specialized tasks
- MCP server tools can be integrated into skills

#### IDE Integrations
**Status:** Full support across multiple platforms

**Available Platforms:**
- **Terminal (CLI)** - Core experience, run `claude` in any terminal
- **VS Code** - Native extension with inline diffs, @-mentions, plan review
- **JetBrains IDEs** - Plugin for IntelliJ IDEA, PyCharm, WebStorm with IDE diff viewing, context sharing
- **Desktop app** - Standalone with diff review, parallel sessions via git worktrees, cloud sessions
- **Web** - Browser at claude.ai/code, iOS app, no local setup required, parallel tasks, built-in diff view
- **Chrome** - Browser extension for live debugging, design verification, web app testing

#### Git Integration
**Status:** Full support with automation capabilities

- Handle git workflows through natural language
- Resolve merge conflicts
- Create commits and PRs
- Write release notes automatically
- GitHub Actions integration with `@claude` mentions
- GitLab CI/CD event-driven automation
- Works in CI for automated code review and issue triage
- Desktop app supports parallel sessions via git worktrees

#### Web Search Capability
**Status:** Full support via WebSearch tool

- WebSearch tool available as built-in tool
- Supports query parameters, allowed_domains, blocked_domains
- Can be matched in hooks with tool name "WebSearch"
- Maintains awareness to find up-to-date information from the web
- Integrated into agentic loop for information retrieval

#### Sandbox/Security Features
**Status:** Enterprise-grade security with permission system

**Permission System:**
- Multiple permission modes: default, plan, acceptEdits, dontAsk, bypassPermissions
- Permission dialogs for tool execution
- Permission rules for "always allow" patterns
- Hooks can intercept and control permissions (PermissionRequest event)
- Managed policy settings for organization-wide control
- Enterprise admins can use `allowManagedHooksOnly` to block user/project/plugin hooks

**Security Features:**
- Enterprise-grade security, privacy, and compliance built-in
- Use Claude API, or host on AWS Bedrock or GCP Vertex AI
- Hooks run with user permissions (security considerations required)
- Sessions capture hooks snapshot at startup (prevents mid-session modifications)
- External hook modifications require review in `/hooks` menu
- Environment isolation with `$CLAUDE_CODE_REMOTE` variable for remote sessions

**Best Practices:**
- Validate and sanitize inputs
- Quote shell variables
- Block path traversal
- Use absolute paths
- Skip sensitive files

#### Cost Tracking Options
**Status:** Full support with detailed tracking

**Cost Tracking Features:**
- `/cost` command displays detailed token usage statistics per session
- Shows total cost, API duration, wall duration, code changes
- `/stats` command for usage patterns (subscribers)
- Workspace-based centralized cost tracking via Claude Console
- Auto-created "Claude Code" workspace for organization cost management

**Token Budget Management:**
- Extended thinking enabled by default with 31,999 token budget
- Configurable via `/config` or `MAX_THINKING_TOKENS` setting
- Context awareness feature tracks remaining context window
- Long context pricing for requests exceeding 200K tokens

**Average Costs (2026):**
- Average: $100-200/developer per month with Sonnet 4.5
- Average $6/day, 90% of developers under $12/day
- Variance based on automation usage and instance count

**Pricing Plans:**
- Pro: $20/month
- Max 5x: $100/month (5x token capacity)
- Max 20x: $200/month (20x token capacity)
- Teams: $150/month per developer (minimum 5 seats)

**Additional Features:**
- Composable and scriptable (Unix philosophy)
- CLAUDE.md for static context and instructions
- Slack integration with Claude mentions
- Reference implementation in development containers
- Auto-updates for native installations
- Debug mode with `claude --debug`
- Verbose mode toggle with `Ctrl+O`

---

## Codex CLI Research
**Agent:** Marcus Thompson
**Status:** Complete

### Context Windows

OpenAI Codex CLI in 2026 uses a fundamentally different approach to context windows compared to traditional fixed-size models. The latest models employ **context compaction technology** that allows them to work across multiple context windows.

| Model | Context Window | Max Output | Notes |
|-------|----------------|------------|-------|
| GPT-5.2-Codex | 400K tokens | 128K tokens | Latest model released Jan 14, 2026. Fixed large context window with improved long-context understanding, reliable tool calling, and native compaction |
| GPT-5.1-Codex-Max | Multi-window (millions of tokens) | N/A | First model natively trained for compaction. Automatically summarizes and compacts when approaching limits, enabling coherent work over millions of tokens in a single task |
| GPT-5-Codex | 200K tokens | N/A | Standard model with 200K context window |
| codex-mini-latest | ~200K tokens | N/A | **DEPRECATED** - Removal from API on January 16, 2026 |

**Key Innovation - Context Compaction:**
- GPT-5.1-Codex-Max and GPT-5.2-Codex feature native compaction technology
- Automatically summarizes conversation history when approaching context limits
- Provides a "fresh" context window and repeats the process as needed
- Enables long-running coding tasks spanning millions of tokens
- More token-efficient reasoning for extended sessions

**Model Evolution:**
- Original Codex models (code-davinci-002) were deprecated in March 2023
- Codex functionality now integrated into GPT-5 series models
- Modern Codex is a complete coding agent rather than just a model

### Features

#### Hooks Support
**Status:** Limited/Community-Requested

- **Notification Hook:** Built-in hook that triggers when Codex completes a task (officially supported)
- **Comprehensive Hooks System:** Community PR #9796 proposed extensive hooks (tool, file, event lifecycle) but OpenAI is **not accepting feature contributions** at this time
- **Proposed Hook Types:** before/after tool execution, before/after file write operations, prompt gating, stop hooks, compact mode notifications
- **Current Limitation:** OpenAI needs to ensure features are well-designed and consistent across all Codex surfaces (CLI, IDE, web) before accepting

#### MCP/Plugin Support
**Status:** Full Support

- **Model Context Protocol (MCP):** Officially supported for third-party tools and context integration
- **Agent Skills:** Reusable bundles of instructions to automate tasks
  - Invoke explicitly with `$skill-name` (e.g., `$skill-installer`, `$create-plan`)
  - Can be auto-selected by Codex based on prompt context
  - Install user-specific skills in `~/.codex/skills`
  - Check project-specific skills into `.codex/skills` for team sharing

#### Sub-agents Capability
**Status:** Native Agent Architecture

- Codex operates as a "Software Engineer teammate" connecting models, local tooling, and cloud
- Multi-surface architecture (CLI, IDE extension, macOS app, web at chatgpt.com/codex)
- Agent loop unrolls tasks into planning, execution, and review phases
- Dedicated reviewer mode with `/review` command

#### Slash Commands
**Status:** Full Support

- **`/diff`** - Inspect Git diff (staged, unstaged, untracked files)
- **`/mention`** - Add files to conversation by path
- **`/new`** - Start fresh conversation in same session
- **`/resume`** - Reload and continue previous conversation
- **`/model`** - Switch between GPT-5-Codex, GPT-5, or adjust reasoning levels
- **`/review`** - Launch dedicated code reviewer for diff analysis
- **Custom Commands:** Create custom prompts that behave like slash commands with arguments and metadata

#### Custom Commands
**Status:** Full Support

- Users can create custom prompts functioning as new slash commands
- Support for arguments and metadata
- Custom skills can be installed globally or per-project

#### IDE Integrations
**Status:** Full Support

- **Supported IDEs:** VS Code, Cursor, Windsurf
- IDE extension provides same slash commands as CLI
- Seamless context switching between terminal CLI, IDE extension, and web interface
- Local and cloud mode switching available

#### Git Integration
**Status:** Full Support

- Built-in `/diff` command for reviewing changes
- Automatic transcript of all actions for audit trail
- Recommended workflow: create Git checkpoints before/after tasks
- Easy rollback with standard Git commands
- Codex surfaces changes for review before committing

#### Web Search Capability
**Status:** Full Support

- Built-in web search to get up-to-date information during tasks
- Integrated into the agent's tooling capabilities
- Available across all Codex surfaces (CLI, IDE, web)

#### Sandbox/Approval Modes
**Status:** Full Support

Multiple sandbox policies available via `--sandbox` flag:

- **`read-only`** - Commands can read files but cannot write anywhere (including /tmp)
- **`workspace-write`** - Default mode with:
  - Write permissions limited to active workspace
  - No network access by default (configurable)
  - Reads work broadly across filesystem
  - Recommended for most development work
- **`danger-full-access`** - Full write access to filesystem, removes all sandbox restrictions

**Approval Modes:**
- `--ask-for-approval on-request` - Approve on request
- `--full-auto` - Shortcut combining `on-request` approvals with `workspace-write` sandbox
- `--dangerously-bypass-approvals-and-sandbox` - Disables all protections (dangerous)

**Implementation:**
- macOS 12+: Apple Seatbelt with `sandbox-exec`
- Linux: Landlock/seccomp APIs

#### Cost Tracking Options
**Status:** None (Community-Requested)

- **Current State:** No built-in cost tracking or usage analytics
- **Community Request:** GitHub Issue #5085 proposes cost/usage analytics module
- **Problem:** Users face unpredictable bills without visibility into session costs or token consumption
- **Workaround:** Manual tracking based on API pricing

**2026 Pricing Context:**
- GPT-5-Codex: $1.25/M input tokens, $10.00/M output tokens
- GPT-5.1-Codex-Mini: $0.25/M input tokens, $2.00/M output tokens
- Codex-mini-latest: $1.50/M input tokens, $6.00/M output tokens
- Typical medium-sized code changes: $3-4 with o3 model
- ChatGPT Plus ($20/month): 30-150 local tasks every 5 hours
- ChatGPT Pro ($200/month): Unlimited o1 reasoning models for power users

**Notable Changes from Previous Research:**
1. New GPT-5.2-Codex model released (Jan 14, 2026) with 400K context window
2. codex-mini-latest deprecated (removed Jan 16, 2026)
3. Context compaction is now a core feature, not just experimental
4. Agent skills system is production-ready
5. Comprehensive hooks system exists as community PR but not yet merged
6. Cost tracking remains a requested feature, not implemented

---

## Cursor Research
**Agent:** Elena Rodriguez
**Status:** Complete

### Context Windows

Cursor IDE supports multiple AI model providers with varying context window configurations. As of February 2026, Cursor operates with a standard 200k token context window (~15,000 lines of code) in normal mode, with "Max Mode" extending the context window to the maximum available for supported models.

#### Anthropic Models

| Model | Context Window (Normal) | Max Mode | Notes |
|-------|------------------------|----------|-------|
| Claude Opus 4.5 | 200k tokens | 200k tokens | Released Nov 24, 2025; supports Infinite Chats feature |
| Claude Sonnet 4.5 | 200k tokens | 200k-1M tokens | Community reports varying limits; officially ~200k |

#### OpenAI Models

| Model | Context Window (Normal) | Max Mode | Notes |
|-------|------------------------|----------|-------|
| GPT-5.1 Codex Max | 200k tokens | 400k tokens | Added January 2026; improved tool calls |
| GPT-5.1 High | 200k tokens | 400k tokens | Frontier coding model |
| GPT-5 Mini | 200k tokens | N/A | Fast, lightweight option |
| GPT-5 Nano | 200k tokens | N/A | Ultra-fast for simple tasks |
| GPT-4.1 | 200k tokens | Supported | Legacy model, still available |

#### Google Models

| Model | Context Window (Normal) | Max Mode | Notes |
|-------|------------------------|----------|-------|
| Gemini 3 Pro Preview | 200k tokens | 1M tokens | Top performer on SWE-bench (76.2-78%) |
| Gemini 2.5 Flash | 200k tokens | 1M tokens | Fast inference, extended context available |

#### xAI Models

| Model | Context Window (Normal) | Max Mode | Notes |
|-------|------------------------|----------|-------|
| Grok 4 | 200k tokens | 2M tokens | Real-time web search integration |
| Grok Code Fast | 200k tokens | N/A | Optimized for speed |

#### DeepSeek Models

| Model | Context Window (Normal) | Max Mode | Notes |
|-------|------------------------|----------|-------|
| DeepSeek V3 | 200k tokens | N/A | Native support since v0.44+; hosted on US servers |
| DeepSeek R1 | 200k tokens | N/A | Native support since v0.45+; free within Pro plan |

#### Cursor Native Models

| Model | Context Window (Normal) | Max Mode | Notes |
|-------|------------------------|----------|-------|
| Composer 1 | ~200k tokens | N/A | 4x faster than comparable models; <30s response time |

**Key Context Management Features:**
- Dynamic context discovery reduces token usage by 46.9% for MCP tool calls
- Automatic summarization when context window fills
- Chat history preserved as files for context recovery
- Efficient updates via Merkle tree-based change detection

### Features

#### Hooks System (Enterprise-Grade)
**Status:** Full Support (January 2026)

- Observe, block, and extend agent loop operations
- Auto-formatting after edits
- Gating dangerous commands
- Adding commit checkpoints
- Redacting environment secrets
- **Performance:** 10-20x faster following January 8, 2026 CLI update
- **Enterprise Partners:** MintMCP (MCP governance), Oasis Security (access management), Runlayer (MCP broker), Semgrep (security scanning)

#### Model Context Protocol (MCP)
**Status:** Full Support (First-class integration)

- `/mcp enable` and `/mcp disable` commands for on-the-fly server management
- Dynamic context discovery for external tools and data sources
- 46.9% token reduction in agent runs using MCP tools
- MCP governance via partner integrations

#### VS Code Extension Compatibility
**Status:** Full Support

- Cursor is built on VS Code, maintaining full compatibility with VS Code extensions and marketplace

#### Parallel Agents / Sub-agents
**Status:** Full Support

- Multiple agents can run in parallel via Cursor 2.0
- Agent-centric interface for managing concurrent agents
- Background Agents for asynchronous tasks (auto-testing, dependency monitoring)
- Background agents run in isolated AWS VMs
- Trigger via Ctrl+E for background mode

#### Slash Commands
**Status:** Full Support

**Built-in Commands:**
- `/models` - List and switch between available models
- `/rules` - Create and edit rules from terminal
- `/mcp enable` / `/mcp disable` - Manage MCP servers

**Custom Commands:**
- Stored as Markdown files in `.cursor/commands/`
- Project-specific and global libraries
- Higher priority than rules (agent treats them as direct prompts)

#### Custom Rules (.cursorrules)
**Status:** Full Support

- Project-specific AI instructions for code generation
- Defined in `.cursorrules` files
- Automatically appended to agent context
- Community repository available (awesome-cursorrules)
- Lower priority than slash commands

#### Composer / Agent Mode
**Status:** Full Support (Cursor 2.0)

- **Composer 1:** Native ultra-fast coding model
- **Composer 2.0:** Added "Plan Mode" for step outlining before execution
- Multi-file editing with project-wide context
- Auto-runs terminal commands (foreground requires approval)
- Intelligent context retrieval from project index
- ~200k effective context window with augmentation

#### Git Integration
**Status:** Full Support

- Git history indexing with commit SHAs and parent info
- Automatic PR indexing for all merged PRs
- PR search and retrieval into agent context
- Merkle tree-based efficient updates (10-minute intervals)
- Clone via "Cursor: Clone" command for immediate indexing
- Privacy: obfuscated filenames, encrypted code chunks

#### Web Search (@Web)
**Status:** Full Support

- Integrated web search capability via @ mentions in chat interface

#### Background Agents
**Status:** Full Support (2026)

- Asynchronous task execution (testing, monitoring)
- Runs in isolated AWS infrastructure (VM-based)
- Auto-runs terminal commands without approval (unlike foreground)
- Trigger via Ctrl+E
- View status and enter machine from agent list

#### Codebase Indexing
**Status:** Full Support

**Technology:**
- Embedding-based indexing for all files
- Automatic indexing on project open
- Incremental indexing for new files
- Understands file relationships and components
- Git history indexing when enabled
- Merkle tree for efficient change detection (10-min intervals)

**Privacy:**
- Filenames obfuscated
- Code chunks encrypted
- Decryption on retrieval

#### CLI Support
**Status:** Full Support (January 2026)

- Model management commands
- MCP server controls
- Rules and commands management
- Performance improvements in v0.44-0.45+

---

## Gemini CLI Research
**Agent:** Dr. Raj Patel
**Status:** Complete

### Context Windows

**Current Stable Models (February 2026)**

| Model | Context Window | Max Output | Status |
|-------|----------------|------------|--------|
| Gemini 2.5 Pro | 1,048,576 (1M) | 65,536 | Stable |
| Gemini 2.5 Flash | 1,048,576 (1M) | 65,536 | Stable |
| Gemini 2.5 Flash-Lite | 1,048,576 (1M) | 65,536 | Stable |
| Gemini 2.5 Flash Image | 65,536 | 32,768 | Stable |
| Gemini 2.5 Flash Live | 131,072 | 8,192 | Preview |

**Preview Models (Gemini 3 Series)**

| Model | Context Window | Max Output | Status |
|-------|----------------|------------|--------|
| Gemini 3 Pro Preview | 1,048,576 (1M) | 65,536 | Preview |
| Gemini 3 Flash Preview | 1,048,576 (1M) | 65,536 | Preview |
| Gemini 3 Pro Image Preview | 65,536 | 32,768 | Preview |

**Deprecation Timeline**

| Model | Shutdown Date | Migration Path |
|-------|---------------|----------------|
| Gemini 2.0 Flash | March 31, 2026 | Gemini 2.5 Flash or Flash-Lite |
| Gemini 2.0 Flash-Lite | March 31, 2026 | Gemini 2.5 Flash-Lite |
| gemini-2.5-flash-image-preview | January 15, 2026 | Gemini 2.5 Flash Image (stable) |
| text-embedding-004 | January 14, 2026 | N/A |

**Key Insights:**
- All mainstream Gemini models support 1M+ token context windows (1,048,576 tokens)
- The 1M token window translates to approximately 1,500 pages of text or 30,000 lines of code
- Max output consistently at 65,536 tokens for Pro/Flash models, 32,768 for image-optimized variants
- Gemini 1.5 Pro can be upgraded to 2M tokens in certain configurations
- Free tier via Google AI API: 60 requests/minute, 1,000 requests/day

### Features

#### Hooks Support
**Status:** Full Support

- Enabled by default since v0.26.0+
- Scripts execute at specific points in the agentic loop
- Extensions can bundle hooks directly
- Supports variable substitution in hooks/hooks.json
- Allows customization without touching source code
- Controls and customizes the agent loop at lifecycle events

#### MCP/Extensions Support
**Status:** Full Support

**MCP (Model Context Protocol):**
- Configure connections to one or more MCP servers
- Discover and use custom tools
- Managed via `/mcp` command
- Extensions can package MCP servers with variable substitution

**Extensions System:**
- Package prompts, MCP servers, Agent Skills, and custom commands
- Easy one-command installation
- Browse extensions at geminicli.com/extensions
- Simple "playbook" architecture - set of tools extensions know how to use
- Can include context files (GEMINI.md), excluded tools, and custom commands
- Documentation updated as recently as January 28, 2026

#### Sub-agents Capability
**Status:** Preview

- Agent Skills provide on-demand expertise and specialized workflows
- Managed via `/skills` command
- Currently in preview status

#### Slash Commands
**Status:** Full Support

**30+ slash commands available across categories:**

**Session Management:**
- `/chat` - Save and resume conversation history for branching
- `/resume` - Browse and restore previous sessions interactively
- `/rewind` - Navigate backward through conversation history
- `/clear` - Wipe terminal display (Ctrl+L)
- `/quit` or `/exit` - Close application

**Information & Help:**
- `/help` or `/?` - Display available commands
- `/about` - Show version information
- `/stats` - Token usage, cached token savings, session duration
- `/tools` - List currently available tools with descriptions
- `/docs` - Open documentation in browser

**Configuration:**
- `/settings` - Open settings editor
- `/model` - Choose Gemini model via dialog
- `/theme` - Change visual appearance
- `/editor` - Select supported text editors
- `/auth` - Modify authentication methods

**Content & Tools:**
- `/memory` - Manage instructional context from GEMINI.md files
- `/copy` - Transfer last output to clipboard
- `/compress` - Replace chat context with summary to conserve tokens

**Development & Integration:**
- `/extensions` - View active extensions
- `/skills` - Manage Agent Skills
- `/hooks` - Control lifecycle event interception
- `/mcp` - Manage Model Context Protocol servers
- `/ide` - Configure IDE integration

**Other Utilities:**
- `/directory` or `/dir` - Handle multi-directory workspaces
- `/bug` - File GitHub issues
- `/vim` - Toggle vim-mode editing
- `/restore` - Revert files to pre-tool state (if checkpointing enabled)

#### Custom Commands (TOML)
**Status:** Full Support

- Defined via .toml files
- Supports {{args}} parameterization for reusable prompts
- Minimal configuration required (just prompt)
- Can execute shell commands
- Extensions can package custom commands
- Easy-to-use argument substitution

#### IDE Integrations
**Status:** Full Support

- VS Code compatibility confirmed
- Configured via `/ide` command
- Seamless integration with editor workflows

#### Git Integration
**Status:** Partial

**Currently Available:**
- Git-aware filtering: @ commands exclude git-ignored files by default
- Automatic exclusion of .git/, node_modules/, dist/, .env
- Can execute git operations through shell commands

**Requested Features:**
- Native git operations (create commits, branches, PRs)
- Show history and generate pull requests
- Potential tools: create_commit, create_pr, get_git_diff, get_git_log
- Feature requests pending for direct git integration

#### Web Search
**Status:** Full Support

- Real-time internet information retrieval
- Google Search grounding integration
- Built into agent's tooling capabilities
- Available for up-to-date information during tasks

#### Sandbox Modes
**Status:** Full Support

- Execute untrusted code/tools in secure, isolated container
- Checkpointing system for workspace state management
- `/restore` command to revert files to pre-tool state
- Security boundaries via trusted folders
- `.geminiignore` files to protect sensitive data

#### Google Cloud Integration
**Status:** Full Support

**Vertex AI Integration:**
- Three authentication methods:
  - Application Default Credentials (ADC) via gcloud
  - Service Account JSON key
  - Google Cloud API key
- Available without setup in Cloud Shell
- Requires GOOGLE_CLOUD_PROJECT and GOOGLE_CLOUD_LOCATION env vars

**Multi-Auth Support:**
- Google Account login (Gemini Code Assist)
- Gemini API key (unpaid - Flash only)
- Vertex AI Express Mode (no billing required)

#### Cost Tracking (/stats)
**Status:** Full Support

- `/stats` command shows:
  - Token usage statistics
  - Cached token savings
  - Session duration
- Summary presented on exit at end of session
- Community enhancements proposed for spending calculations
- Integrates with Gemini API pricing data

**Pricing Structure:**

**Free Tier:**
- Google Account login
- Unpaid API key (Flash model only)
- Vertex AI Express Mode
- 60 requests/minute, 1,000 requests/day

**Fixed Price:**
- Google AI Pro/Ultra subscriptions
- Gemini Code Assist Standard/Enterprise editions
- Predictable costs for individual developers or enterprises

**Pay-As-You-Go:**
- Flexible option for professional use
- Pay per token/call
- Most flexible for long-running tasks
- Requires mindful usage to avoid unexpected costs

**Additional Features:**

- **Headless Mode:** Automated reasoning for scripts and CI/CD pipelines
- **Token Caching:** Performance optimization for repeated context
- **Memory Management:** Persistent project facts across sessions via GEMINI.md
- **Customizable Themes:** Visual appearance control
- **Telemetry Management:** Privacy controls
- **System Prompt Override:** Customize core model instructions
- **GitHub Actions:** Automated issue triage and PR reviews
- **File Management:** Read code and apply changes directly
- **Shell Commands:** Execute builds, tests, and terminal operations

**Latest Updates:**
- Documentation last updated: January 28, 2026
- Gemini CLI version v0.23.0 validated: January 9, 2026
- Hooks enabled by default since v0.26.0+
- Extensions system actively maintained with browse functionality

**Notable Changes from Previous Research:**
1. All Gemini 2.5 models confirmed at 1M token context window
2. Gemini 3 Preview models available with 1M context
3. Gemini 2.0 Flash deprecation scheduled March 31, 2026
4. Hooks now fully supported (default enabled v0.26.0+)
5. Extensions system matured with comprehensive documentation
6. Cost tracking via /stats is production-ready
7. MCP support fully integrated into extensions
8. Agent Skills in preview for sub-agent capabilities
```

## File: `research/2026-02-04_12-30-00/result.md`
```markdown
# Research Results

**Completed:** 2026-02-04 12:45:00

## Summary

| Tool | Context Window Changes | Feature Changes |
|------|------------------------|-----------------|
| Claude Code | Yes | Yes |
| Codex CLI | Yes | Yes |
| Cursor | Yes | Yes |
| Gemini CLI | Yes | Yes |

---

## Key Changes Found

### Context Windows

1. **Claude Code**: Added legacy model details (Opus 4.1, Sonnet 4, Sonnet 3.7, Opus 4, Haiku 3). Added context awareness feature for Sonnet 4.5 and Haiku 4.5.

2. **Codex CLI**: `codex-mini-latest` deprecated (removed Jan 16, 2026). GPT-5.2-Codex confirmed as latest with 400K context. Context compaction is now a core feature.

3. **Cursor**: Added GPT-5.1 Codex Max (400K Max mode), Gemini 3 Pro Preview (1M Max mode), Grok 4 (2M Max mode), DeepSeek V3/R1 native support. Added dynamic context discovery (46.9% token reduction).

4. **Gemini CLI**: Confirmed Gemini 2.5 Flash Image (65k context, 32k output) and Gemini 2.5 Flash Live (131k context). Added Gemini 3 Pro Image Preview.

### Features

1. **Claude Code Hooks**: Expanded from 8 to 12 event types (added PermissionRequest, PostToolUseFailure, SubagentStart, SessionEnd). Added 3 hook types (command, prompt, agent) and async support.

2. **Codex CLI MCP**: Now has Agent Skills system that is production-ready.

3. **Cursor Hooks**: Now enterprise-grade with partner integrations (MintMCP, Oasis Security, Runlayer, Semgrep). 10-20x performance improvement.

4. **Gemini CLI Hooks**: Now full support (was experimental), enabled by default since v0.26.0+.

5. **Gemini CLI Git Integration**: Should be updated to ⚠️ Partial (native git operations not yet available, only git-aware filtering).

---

## Proposed Context Window Updates (README.md)

No changes to the summary table required. Current values are accurate:

| Tool | Largest Context | Best Model | Source |
|------|-----------------|------------|--------|
| Claude Code | 1M (beta) | Sonnet 4.5 with `--betas context-1m-2025-08-07` | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
| Codex CLI | 400k+ | GPT-5.2-Codex (context compaction) | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
| Cursor | 1M (Max mode) | Gemini 3 Pro/Flash | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
| Gemini CLI | 1M | Gemini 3 Pro Preview | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |

---

## Proposed Feature Updates (README.md)

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------|:-----------:|:---------:|:----------:|:------:|
| **Hooks** | ✅ | ⚠️ | ✅ | ✅ |
| **Plugins/MCP** | ✅ | ✅ | ✅ | ✅ |
| **Sub-agents** | ✅ | ✅ | ⚠️ | ✅ |
| **Slash Commands** | ✅ | ✅ | ✅ | ✅ |
| **Custom Commands** | ✅ | ✅ | ✅ | ✅ |
| **IDE Integration** | ✅ | ✅ | ✅ | ✅ |
| **Git Integration** | ✅ | ✅ | ⚠️ | ✅ |
| **Web Search** | ✅ | ✅ | ✅ | ✅ |
| **Image Support** | ⚠️ | ✅ | ✅ | ⚠️ |
| **Memory/Persistence** | ⚠️ | ✅ | ✅ | ⚠️ |
| **Multi-file Editing** | ✅ | ✅ | ✅ | ✅ |
| **Auto-commit** | ⚠️ | ⚠️ | ✅ | ✅ |
| **Custom System Prompts** | ✅ | ⚠️ | ✅ | ✅ |
| **Cost Tracking** | ✅ | ❌ | ✅ | ⚠️ |
| **Sandbox Mode** | ❌ | ✅ | ✅ | ⚠️ |

---

## Diff: Current vs New

### README.md - Feature Changes

```diff
 | Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
 |---------|:-----------:|:---------:|:----------:|:------:|
-| **Hooks** | ✅ | ⚠️ | ⚠️ | ✅ |
+| **Hooks** | ✅ | ⚠️ | ✅ | ✅ |
-| **Plugins/MCP** | ✅ | ⚠️ | ✅ | ✅ |
+| **Plugins/MCP** | ✅ | ✅ | ✅ | ✅ |
-| **Git Integration** | ✅ | ✅ | ✅ | ✅ |
+| **Git Integration** | ✅ | ✅ | ⚠️ | ✅ |
-| **Cost Tracking** | ✅ | ⚠️ | ✅ | ⚠️ |
+| **Cost Tracking** | ✅ | ❌ | ✅ | ⚠️ |
```

### Changes Summary

1. **Gemini CLI Hooks**: ⚠️ → ✅ (now full support, enabled by default since v0.26.0+)
2. **Codex CLI Plugins/MCP**: ⚠️ → ✅ (Agent Skills system is now production-ready)
3. **Gemini CLI Git Integration**: ✅ → ⚠️ (only git-aware filtering, no native git operations)
4. **Codex CLI Cost Tracking**: ⚠️ → ❌ (no built-in cost tracking at all, only community-requested)

---

## reports/context-comparison.md Changes

### Claude Code Section
- Add legacy models list
- Add context awareness feature note
- Update key features

### Codex CLI Section
- Mark `codex-mini-latest` as DEPRECATED
- Add context compaction as core feature
- Update model list

### Cursor Section
- Add GPT-5.1 Codex Max model
- Add Grok 4 with 2M Max mode
- Add DeepSeek V3/R1 with native support
- Add dynamic context discovery feature

### Gemini CLI Section
- Add Gemini 2.5 Flash Image (65k context)
- Add Gemini 2.5 Flash Live (131k context)
- Add Gemini 3 Pro Image Preview

---

## reports/feature-comparison.md Changes

### Hooks Section
- Claude Code: Update to 12 event types, add hook types (command, prompt, agent), async support
- Gemini CLI: Change status from "⚠️ Experimental" to "✅ Full Support"

### Plugins/MCP Section
- Codex CLI: Change status from "⚠️ MCP Only" to "✅ Full Support" (Agent Skills production-ready)

### Git Integration Section
- Gemini CLI: Change status from "✅ Full" to "⚠️ Partial" (git-aware filtering only)

### Cost Tracking Section
- Codex CLI: Change status from "⚠️ Third-party" to "❌ None" (no built-in tracking)

---

## Action Required

**User approval needed to:**

1. Update README.md Feature Comparison table (4 cell changes)
2. Update reports/context-comparison.md with new model details
3. Update reports/feature-comparison.md with revised feature statuses
```

## File: `research/2026-02-06_11-08-08/research.md`
```markdown
# Context Window & Features Research Session

**Started:** 2026-02-06 11:08:08
**Status:** In Progress

---

## Claude Code Research
**Agent:** Dr. Sarah Chen
**Status:** Complete

### Context Windows

**Latest Models (as of February 2026):**

| Model | Context Window | Max Output | Extended Thinking | Notes |
|-------|----------------|------------|-------------------|-------|
| **Claude Opus 4.6** | 200k / 1M (beta) | 128k | Yes (Adaptive) | Released Feb 5, 2026. First Opus with 1M context. Adaptive thinking with 4 effort levels. |
| **Claude Opus 4.5** | 200k | 64k | Yes | Legacy model, still available. 67% lower cost than predecessor. |
| **Claude Sonnet 4.5** | 200k / 1M (beta) | 64k | Yes | Recommended default, best coding model. |
| **Claude Haiku 4.5** | 200k | 64k | Yes | Fastest model, unbeatable for UI work. |

**1M Context Window Beta:**
- Available for Opus 4.6 and Sonnet 4.5
- Requires `context-1m-2025-08-07` beta header
- Available to usage tier 4 organizations and custom rate limits
- Premium pricing: 2x input, 1.5x output for requests exceeding 200k tokens
- Opus 4.6: $10 input / $37.50 output per million tokens (premium tier)
- Standard pricing: $5 input / $25 output (Opus 4.6), $3 input / $15 output (Sonnet 4.5)

**Extended Thinking Budget:**
- Opus 4.6 supports **adaptive thinking** (decides when deeper reasoning helps)
- Four effort levels: low, medium, high (default), max
- Thinking budget tokens are subset of max_tokens parameter
- Billed as output tokens and count towards rate limits

**Context Compaction:**
- Beta feature for longer-running agentic tasks
- Automatically summarizes older context when approaching thresholds
- Auto-compaction triggers at ~95% capacity (configurable via CLAUDE_AUTOCOMPACT_PCT_OVERRIDE)

**Performance:**
- Opus 4.6 scores 76% on MRCR v2 (needle-in-haystack) vs 18.5% for Sonnet 4.5
- Can process 1,500 pages of text, 30,000 lines of code, or 1+ hour of video
- 128k output enables substantial tasks without multiple requests

**Changes Detected:** YES - Major update with Opus 4.6 release, 1M context now available for Opus-class models

### Features

**Hooks System:** ✅ FULL SUPPORT
- All hook events available: PreToolUse, PostToolUse, Stop, SubagentStop, SubagentStart, SessionStart, SessionEnd, PreCompact, UserPromptSubmit, Notification, PermissionRequest, Setup, TeammateIdle, TaskCompleted
- Hooks can be defined in subagent frontmatter or settings.json
- PreToolUse hooks support conditional validation (exit code 2 blocks operations)
- PostToolUse hooks for actions after tool execution
- Subagent-scoped hooks clean up when subagent finishes

**Plugins/MCP:** ✅ FULL SUPPORT
- Plugin system for packaging slash commands, subagents, MCP servers, and hooks
- MCP (Model Context Protocol) connects Claude Code to external tools, databases, APIs
- MCP OAuth support for authentication
- Streamable HTTP support
- Plugins can be installed from marketplaces
- Plugin components: slash commands, subagents, MCP servers, hooks

**Sub-agents:** ✅ FULL SUPPORT + NEW AGENT TEAMS
- Custom subagents with specialized prompts, tool restrictions, permissions
- Built-in subagents: Explore (read-only, Haiku), Plan (research), general-purpose
- Subagent scopes: session (CLI flag), project (.claude/agents/), user (~/.claude/agents/), plugin
- Foreground (blocking) or background (concurrent) execution
- **NEW: Agent teams** for parallel autonomous task coordination (announced with Opus 4.6)
- Persistent memory system (user/project/local scopes)
- Auto-compaction support for subagents
- Resume capability to continue previous subagent work
- Subagents can preload skills via frontmatter

**Skills System:** ✅ UNIFIED WITH SLASH COMMANDS
- Slash commands merged into skills system (v2.1.3)
- Skills defined in .claude/skills/ with SKILL.md files
- YAML frontmatter + markdown content
- Backward compatible with .claude/commands/
- Auto-discovery by Claude or manual invocation
- Skill hot-reload without restart
- Skills can run in subagents or main context
- Support for directory of supporting files

**Custom Commands:** ✅ FULL SUPPORT
- Implemented via Skills system (slash commands merged into skills)
- SKILL.md files in .claude/skills/
- YAML frontmatter for configuration
- Markdown content for instructions

**IDE Integration:** ✅ FULL SUPPORT
- Native VS Code extension with 2M+ installs
- Real-time change visualization with inline diffs
- Dedicated sidebar panel
- Checkpoints to track and rewind file edits
- @-mention files with specific line ranges
- Conversation history and multi-tab support
- Beta status with active development
- Compatible with VS Code 1.85+ on Windows, macOS, Linux
- Support for VS Code-based IDEs (Cursor, Trae)

**Git Integration:** ✅ FULL SUPPORT
- Commit, PR creation, branch management
- Git diff review capabilities
- Integration with code review workflows

**Web Search:** ✅ AVAILABLE
- Built-in web search capability
- Available in US region

**Sandbox Mode:** ✅ AVAILABLE (macOS/Linux)
- Native sandboxing using OS-level primitives
- macOS: Seatbelt (same as App Store apps)
- Linux: bubblewrap (bwrap) used by Flatpak
- Filesystem isolation (read/write to cwd, blocks outside)
- Network isolation via unix domain socket proxy
- Domain whitelisting with user confirmation
- Reduces permission prompts by 84% in internal testing
- Protects against prompt injection attacks
- Cannot steal SSH keys or phone home to attackers

**Cost Tracking:** ✅ FULL SUPPORT
- /cost, /usage, /stats commands
- Token usage tracking
- Cost monitoring per session

**Memory System:** ✅ FULL SUPPORT
- CLAUDE.md project instructions (checked into codebase)
- .claude/rules/ for additional rules
- Automatic memory for subagents (user/project/local scopes)
- Persistent memory survives across conversations
- Memory files managed by subagents (Read, Write, Edit auto-enabled)

**Task Management:** ✅ FULL SUPPORT
- Task API with state persistence to ~/.claude/tasks/
- Task list view (Ctrl+T to toggle)
- Progress tracking: pending, in progress, complete
- Background task monitoring via /tasks command
- Multi-step workflow coordination

**Background Commands:** ✅ FULL SUPPORT
- Ctrl+B to move commands to background (Ctrl+B twice for tmux users)
- Dev servers, build processes, test suites run independently
- BashOutput tool to check on background processes
- Background tasks don't block main coding session
- Disable via CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1

**PDF Reading:** ✅ FULL SUPPORT
- Read tool supports PDF files (.pdf)
- Page range specification for large PDFs (required for >10 pages)
- Maximum 20 pages per request

**LSP Tool:** ✅ AVAILABLE
- Code intelligence via Language Server Protocol
- Integration with IDE language servers

**Keybindings Customization:** ✅ AVAILABLE
- Custom keybinding configuration
- Ctrl+B for background commands
- Ctrl+T for task list toggle

**Image Support:** ✅ FULL SUPPORT
- All Claude 4 models support text and image input
- Multimodal capabilities across Opus 4.6, Sonnet 4.5, Haiku 4.5
- Vision processing with specialized fees

**Multi-file Editing:** ✅ FULL SUPPORT
- Concurrent file editing
- Inline diffs and change tracking
- Checkpoint system for reverting changes

**Auto-commit:** ⚠️ PARTIAL (via hooks/workflows)
- Can be implemented via PostToolUse hooks
- Not automatic by default but configurable

**Custom System Prompts:** ✅ FULL SUPPORT
- Subagent system prompts via markdown files
- CLAUDE.md for project-level instructions
- .claude/rules/ for additional customization

**Changes Detected:** YES - Major feature additions including agent teams, unified skills system, enhanced sandbox mode, and improved IDE integration

**Sources:**
- [Anthropic Claude Opus 4.6 Release](https://www.anthropic.com/news/claude-opus-4-6)
- [Claude API Models Overview](https://platform.claude.com/brain/knowledge/docs_legacy/en/about-claude/models/overview)
- [Claude Code Sub-agents Documentation](https://code.claude.com/brain/knowledge/docs_legacy/en/sub-agents)
- [Claude Code VS Code Extension](https://code.claude.com/brain/knowledge/docs_legacy/en/vs-code)
- [Claude Code Sandboxing Documentation](https://code.claude.com/brain/knowledge/docs_legacy/en/sandboxing)
- [Claude Code Skills Documentation](https://code.claude.com/brain/knowledge/docs_legacy/en/skills)
- [Anthropic Engineering: Claude Code Sandboxing](https://www.anthropic.com/engineering/claude-code-sandboxing)
- [TechCrunch: Anthropic Opus 4.6 with Agent Teams](https://techcrunch.com/2026/02/05/anthropic-releases-opus-4-6-with-new-agent-teams/)
- [VentureBeat: Claude Opus 4.6 1M Token Context](https://venturebeat.com/technology/anthropics-claude-opus-4-6-brings-1m-token-context-and-agent-teams-to-take)

---

## Codex CLI Research
**Agent:** Marcus Thompson
**Status:** Complete

### Context Windows

**Latest Models (February 2026):**

1. **GPT-5.3-Codex** (NEW - Released Feb 5, 2026)
   - Context Window: 400,000 tokens
   - Output Limit: 128,000 tokens
   - Features: "Perfect Recall" attention mechanism preventing information loss in long prompts
   - Performance: 25% faster than GPT-5.2-Codex, combines Codex + GPT-5 training stacks
   - Notes: Most capable agentic coding model, unifies frontier code performance with professional reasoning
   - Status: Available in Codex CLI for ChatGPT users

2. **GPT-5.2-Codex** (Released Jan 14, 2026)
   - Context Window: 400,000 tokens (400k)
   - Output Limit: 128,000 tokens (128k)
   - Features: Native compaction, reliable tool calling, improved long-context understanding
   - Performance: SWE-Bench Pro: 56.4%, Terminal-Bench 2.0: 64.0%
   - Reasoning Efforts: Supports low, medium, high, and xhigh settings
   - Pricing: $1.75/M input tokens, $14.00/M output tokens
   - Status: Available in all Codex surfaces for paid ChatGPT users

3. **GPT-5.1-Codex-Max**
   - Context Window: Multi-window (millions of tokens)
   - Output Limit: N/A (uses compaction)
   - Features: First model natively trained for compaction, works across multiple context windows
   - Performance: Can work independently for 24+ hours on long-horizon tasks
   - Compaction: Automatically prunes history while preserving important context
   - Status: Available in Codex CLI, IDE extension, cloud, and code review

4. **GPT-5-Codex**
   - Context Window: 200,000 tokens (200k)
   - Output Limit: N/A
   - Status: Standard model, available when signing in with ChatGPT account

**Deprecated Models:**
- codex-mini-latest: Removed January 16, 2026 (previously ~200k context)

**Key Changes:**
- GPT-5.3-Codex is now the recommended default model
- Context windows increased from 200k to 400k for latest models
- Multi-window compaction technology enables millions of tokens for GPT-5.1-Codex-Max
- All models now support automatic context compaction as sessions approach limits

### Features

**Hooks Support: ⚠️ Limited**
- No native hooks system documented in official February 2026 documentation
- Feature request exists for /ai-git-commit-push slash command (Issue #3481)
- Git auto-commit can be done manually but not through automated hooks
- Community workarounds available but not officially supported

**MCP/Plugins: ✅ Full Support**
- Full Model Context Protocol (MCP) support
- Configure via ~/.codex/config.toml or use 'codex mcp' CLI commands
- Supports STDIO and streaming HTTP servers
- Session-scoped "Allow and remember" for MCP tool approvals (NEW - Jan 2026)
- Common servers: Context7, Figma, Playwright, Chrome DevTools, Sentry

**Sub-agents/Agent Skills: ✅ Full Support**
- Agent Skills extend Codex with task-specific capabilities
- Reads from ~/.agents/skills and repository .agents/skills directories
- Personal skill loading from ~/.agents/skills added Feb 2026
- App-server APIs/events to list and download public remote skills
- Shell executions receive CODEX_THREAD_ID for session detection
- Compatible with Claude-style sub-agents via MCP server approach
- Live skill update detection without restart (NEW - Feb 2026)

**Slash Commands: ✅ Full Support**
- Built-in commands: /review, /fork, and more
- Searchable slash popup interface
- Can create custom slash commands for team-specific tasks

**Custom Commands: ✅ Full Support**
- Custom prompts via Markdown files
- Stored in ~/.codex directory
- Support metadata and placeholders ($1-$9 positional, KEY=value named)
- Invokable as slash commands in CLI and IDE
- Not shared through repository (local only)

**IDE Integration: ✅ Full Support**
- VSCode: Official Codex IDE extension
- JetBrains: Native integration (IntelliJ, PyCharm, WebStorm, Rider) as of Jan 2026
- Also available: Visual Studio, Xcode, Eclipse (as of Jan 26, 2026)
- Works with VSCode forks: Cursor, Windsurf
- Authentication via JetBrains AI, ChatGPT, or BYOK (Bring Your Own Key)

**Git Integration: ✅ Full Support**
- Deep Git awareness and change tracking
- Can automatically commit with meaningful commit messages
- Git-aware context understanding
- Safety mechanisms for version-controlled environments

**Web Search: ✅ Full Support**
- Enabled for local tasks in CLI and IDE extension (Jan 28, 2026)
- Three modes: cached (default), live, or disabled
- Configurable web search options

**Sandbox/Approval Modes: ✅ Full Support**
- Multiple approval modes: auto (default), read-only, workspace-write, danger-full-access
- Switch modes with /approvals command
- Disable with --ask-for-approval never or -a never
- Session-scoped "Allow and remember" for repeated tool calls (NEW - Jan 2026)
- Two security layers: sandbox mode (technical capabilities) + approval policy (when to ask)

**Cost Tracking: ❌ Not Available**
- No native cost tracking feature documented in official docs
- Pricing information available but no session/usage tracking built-in

**Memory/Persistence: ✅ Full Support**
- Stores transcripts locally
- Resume earlier threads with 'resume' subcommand
- Pick up where you left off without repeating context
- Thread/session persistence across restarts

**Image Support: ✅ Full Support**
- Strong vision performance in GPT-5.2-Codex and GPT-5.3-Codex
- Can interpret screenshots, technical diagrams, charts, UI surfaces
- Improved accuracy for visual content in coding sessions

**Multi-file Editing: ✅ Full Support**
- Can read repository, make edits across multiple files
- Full-screen terminal UI for conversational workflow
- 128k output limit enables large, multi-file software projects in single interaction

**Auto-commit: ⚠️ Partial Support**
- Can commit changes with meaningful messages
- No automated hook-based auto-commit after every file change
- Requires manual invocation or custom scripting

**Custom System Prompts: ✅ Full Support**
- Via custom prompts system (Markdown files)
- Stored in ~/.codex directory
- Invokable as slash commands
- Support for metadata and variable placeholders

**Additional Features:**
- Open source, built in Rust for speed and efficiency
- Runs locally from terminal
- Supported on macOS, Windows, Linux
- Network configuration UI streamlined in v0.87.0 (Jan 2026)

**Sources:**
- [Introducing GPT-5.3-Codex](https://openai.com/index/introducing-gpt-5-3-codex/)
- [Codex Models Documentation](https://developers.openai.com/codex/models/)
- [Codex CLI Features](https://developers.openai.com/codex/cli/features/)
- [Model Context Protocol](https://developers.openai.com/codex/mcp/)
- [Agent Skills](https://developers.openai.com/codex/skills/)
- [Slash Commands Documentation](https://developers.openai.com/codex/cli/slash-commands/)
- [Custom Prompts](https://developers.openai.com/codex/custom-prompts/)
- [Codex Security](https://developers.openai.com/codex/security/)
- [JetBrains Integration Announcement](https://blog.jetbrains.com/ai/2026/01/codex-in-jetbrains-ides/)
- [GPT-5.2-Codex in IDEs Changelog](https://github.blog/changelog/2026-01-26-gpt-5-2-codex-is-now-available-in-visual-studio-jetbrains-ides-xcode-and-eclipse/)

---

## Cursor Research
**Agent:** Elena Rodriguez
**Status:** Complete
**Last Updated:** 2026-02-06

### Context Windows

**Latest Stable Release:** v2.4 (January 22, 2026)

#### Anthropic Models

| Model | Normal Context | Max Context | Output | Notes |
|-------|---------------|-------------|---------|-------|
| Claude 4.6 Opus | 200k | 1M | 64k | NEW - Added in 2026 |
| Claude 4.5 Sonnet | 200k | 1M | 64k | Premium, Agent/Thinking modes |
| Claude 4.5 Opus | 200k | 200k | 64k | Deep reasoning |
| Claude 4.5 Haiku | 200k | - | 64k | Fast and efficient |
| Claude 4 Sonnet 1M | 1M | 1M | 64k | Extended context only |
| Claude 4 Sonnet | 200k | - | 64k | Standard |
| Claude 4 Opus | 200k | - | 64k | Available in Max mode |
| Claude 3.7 Sonnet | 200k | - | 64k | Legacy |
| Claude 3.5 Sonnet | 200k | - | 64k | Legacy but still popular |
| Claude 3.5 Haiku | 60k | - | 8k | Legacy |

#### OpenAI Models

| Model | Normal Context | Max Context | Output | Notes |
|-------|---------------|-------------|---------|-------|
| GPT-5.2 (all variants) | 272k | - | - | Latest generation |
| GPT-5.2-Codex | 272k | - | - | Code-optimized |
| GPT-5.1 Codex Max | 200k | 400k | 128k | Improved tool calls |
| GPT-5.1 High | 200k | 400k | 128k | Frontier coding |
| GPT-5 Fast | 272k | - | - | Speed-optimized |
| GPT-5 Mini | 200k | - | 128k | Lightweight |
| GPT-5 Nano | 200k | - | 128k | Ultra-fast |
| GPT 4.1 | 200k | 1M | 8k | Legacy |
| GPT-4o | 128k | - | 16k | General purpose |
| GPT-4o mini | 60k | - | 8k | Free tier (500/day) |
| o3 | 200k | - | 8k | Reasoning |
| o4-mini | 200k | - | 8k | Normal/Max modes |
| o3-mini | 200k | - | 8k | Agent/Thinking |
| o1 | 200k | - | 8k | Thinking mode |
| o1 Mini | 128k | - | 8k | Thinking mode |

#### Google Models

| Model | Normal Context | Max Context | Output | Notes |
|-------|---------------|-------------|---------|-------|
| Gemini 3 Pro Preview | 200k | 1M | 8k | Top SWE-bench performer (76-78%) |
| Gemini 3 Pro Image Preview | 200k | 1M | 8k | Multimodal with image gen |
| Gemini 3 Flash | 200k | 1M | 8k | Fast inference |
| Gemini 2.5 Pro | 200k | 1M | 8k | Design/debugging |
| Gemini 2.5 Flash | 200k | 1M | 8k | Speed-optimized |

#### xAI Models

| Model | Normal Context | Max Context | Output | Notes |
|-------|---------------|-------------|---------|-------|
| Grok 4 | 200k | 2M | - | Real-time web search |
| Grok Code | 256k | - | - | Code-optimized |
| Grok Code Fast | 200k | - | - | Speed-optimized |

#### DeepSeek Models

| Model | Context Window | Output | Notes |
|-------|---------------|---------|-------|
| DeepSeek V3 | 64k-128k | - | Hosted on US servers, free in Pro plan |
| DeepSeek V3.1 | 128k | - | NEW - Upgraded context from V3's 64k |
| DeepSeek R1 | 200k | - | Free within Pro plan |

#### Cursor Native Models

| Model | Context Window | Output | Notes |
|-------|---------------|---------|-------|
| Composer 1 | 200k | - | 4x faster, <30s response, proprietary |

**Key Changes:**
- NEW: Claude 4.6 Opus added with 1M max context
- NEW: DeepSeek V3.1 with 128k context
- NEW: Gemini 3 Pro Image Preview with image generation
- NEW: Grok Code model (256k)

### Features

**Hooks:** ✅ Enhanced (10-40x performance improvement)
**Plugins/MCP:** ✅ Full Support (one-click OAuth, CLI management)
**Sub-agents:** ✅ Enhanced (parallel execution, Skills system, Cloud agents)
**Slash Commands:** ✅ Comprehensive (/models, /plan, /ask, /rules, /mcp)
**Custom Commands:** ✅ (.cursor/commands/*.md)
**IDE Integration:** ✅ Native (VS Code-based)
**Git Integration:** ✅ Advanced (AI commits, GitButler, merge conflict resolution)
**Web Search:** ✅ (@Web, Grok 4 real-time)
**Image Support:** ⚠️ (generation added Jan 2026, full vision coming)
**Memory/Persistence:** ⚠️ (limited built-in, robust via MCP)
**Multi-file Editing:** ✅ Full Support
**Auto-commit:** ✅ (via hooks/GitButler)
**Custom System Prompts:** ✅ (.cursor/rules/ system)
**Cost Tracking:** ⚠️ (Enterprise/third-party only)
**Sandbox Mode:** ⚠️ (macOS/Linux, workflow friction)
**Codebase Indexing:** ✅ (@Codebase semantic search)

**Sources:**
- [Cursor Models Documentation](https://cursor.com/brain/knowledge/docs_legacy/models)
- [Cursor Changelog](https://cursor.com/changelog)
- [Cursor Rules Documentation](https://cursor.com/brain/knowledge/docs_legacy/context/rules)

---

## Gemini CLI Research
**Agent:** Dr. Raj Patel
**Status:** Complete
**Last Updated:** 2026-02-06

### Context Windows

**Latest Stable Release:** v0.27.0 (February 3, 2026)

#### Current Production Models (Stable)

| Model | Context Window | Max Output | Status | Notes |
|-------|---------------|------------|--------|-------|
| Gemini 2.5 Pro | 1,048,576 (1M) | 65,536 (65k) | Stable | High-capability reasoning and coding |
| Gemini 2.5 Flash | 1,048,576 (1M) | 65,536 (65k) | Stable | Balanced speed/intelligence |
| Gemini 2.5 Flash-Lite | 1,048,576 (1M) | 65,536 (65k) | Stable | Lightweight variant |
| Gemini 2.5 Flash Image | 65,536 (65k) | 32,768 (32k) | Stable | Image generation specialist |

#### Preview Models (Gemini 3 Series)

| Model | Context Window | Max Output | Status | Notes |
|-------|---------------|------------|--------|-------|
| Gemini 3 Pro Preview | 1,048,576 (1M) | 65,536 (65k) | Preview | Flagship model - launched Feb 4, 2026 |
| Gemini 3 Flash Preview | 1,048,576 (1M) | 65,536 (65k) | Preview | Pro-grade reasoning at Flash speed - Feb 4, 2026 |
| Gemini 3 Pro Image Preview | 65,536 (65k) | 32,768 (32k) | Preview | Image generation |

#### Specialized Preview Models

| Model | Context Window | Max Output | Status | Notes |
|-------|---------------|------------|--------|-------|
| Gemini 2.5 Flash Live | 131,072 (131k) | 8,192 (8k) | Preview | Real-time audio streaming |
| Gemini 2.5 Flash TTS | 8,192 (8k) | 16,384 (16k) | Preview | Text-to-speech |
| Gemini 2.5 Flash Preview | 1,048,576 (1M) | 65,536 (65k) | Preview | Experimental features |

#### Deprecated Models (End of Life: March 31, 2026)

| Model | Context Window | Max Output | Status | EOL Date |
|-------|---------------|------------|--------|----------|
| Gemini 2.0 Flash | 1,048,576 (1M) | 8,192 (8k) | Deprecated | March 31, 2026 |
| Gemini 2.0 Flash-Lite | 1,048,576 (1M) | 8,192 (8k) | Deprecated | March 31, 2026 |

**Key Updates:**
- Gemini 3 Flash launched February 4, 2026 as default model in Gemini app
- Gemini 3 series delivers PhD-level reasoning (90.4% GPQA Diamond)
- All Gemini 3 models maintain 1M token context window
- Gemini 2.0 models fully deprecated March 31, 2026
- Context windows remain industry-leading at 1M tokens for primary models

### Features

#### Core Agent Capabilities
- **Hooks System:** ✅ Full lifecycle event hooks (BeforeAgent, AfterAgent, BeforeTool, AfterTool, BeforeModel, BeforeToolSelection) - v0.26.0+
- **MCP Support:** ✅ Model Context Protocol for custom integrations via settings.json
- **Agent Skills:** ✅ Stable feature (v0.27.0) - portable skill format with SKILL.md schema, progressive disclosure to save context
- **Sub-agents:** ✅ Supported via AgentRegistry with JSON schema validation
- **Event-Driven Architecture:** ✅ v0.27.0 introduces event-driven scheduler for tool execution

#### Commands & Configuration
- **Slash Commands:** ✅ Built-in commands (/help, /chat, /bug, /stats, /memory, /rewind)
- **Custom Commands:** ✅ TOML-based configuration in .gemini/commands/ (user-scoped and project-scoped)
- **Command Namespacing:** ✅ Subdirectories create namespaced commands (e.g., /git:commit)
- **Argument Handling:** ✅ {{args}} placeholder and shell execution !{...} support
- **/rewind Command:** ✅ New in v0.27.0 - navigate backward through session history

#### IDE & Development Integration
- **IDE Integration:** ✅ VS Code companion extension
- **Git Integration:** ✅ AI-powered commit message generation, pre-commit hook support, GitHub Actions integration
- **Auto-commit:** ✅ generate-commit-message tool with Conventional Commits compliance
- **GitHub Actions:** ✅ Official google-github-actions/run-gemini-cli (beta, launched Feb 2026)

#### Search & Knowledge
- **Web Search:** ✅ Google Search grounding for real-time information
- **Multimodal Support:** ✅ Text, code, images, PDFs, sketches - full multimodal context
- **Image Support:** ✅ Image pasting on Linux (Wayland/X11) - v0.27.0, image generation models available

#### Memory & Context Management
- **Memory/Persistence:** ✅ Hierarchical GEMINI.md system (global ~/.gemini/GEMINI.md + project-level)
- **Memory Commands:** ✅ /memory show, /memory refresh, /memory add <text>
- **Context Files:** ✅ Modular context with @file.md imports
- **Token Caching:** ✅ Automatic caching to optimize token usage
- **Conversation Checkpointing:** ✅ Save and resume complex sessions

#### Cost & Usage Tracking
- **Cost Tracking:** ✅ /stats command shows token usage, cached tokens, session metrics
- **Usage Display:** ✅ Stats shown on session exit
- **Token Optimization:** ✅ Caching reduces costs for repeated context

#### Security & Sandboxing
- **Sandbox Mode:** ✅ Isolates operations, limits file system access to project directory
- **Trusted Folders:** ✅ Security controls via ~/.gemini/trustedFolders.json
- **Safe Mode:** ✅ Untrusted folders run with MCP disabled, no custom commands
- **Docker Sandboxing:** ✅ Optional custom sandbox environments

#### Developer Experience
- **Multi-file Editing:** ✅ Full file system operations through built-in tools
- **Shell Commands:** ✅ Execute shell commands directly in CLI
- **JSON Output:** ✅ JSON and stream-JSON formats for scripting/automation
- **Non-Interactive Mode:** ✅ Designed for CI/CD and automated workflows
- **Extensions Ecosystem:** ✅ gemini-cli-extensions organization on GitHub
- **Custom System Prompts:** ✅ Via GEMINI.md context files

#### Recent v0.27.0 Highlights (Feb 3, 2026)
- Event-driven scheduler (200+ commits)
- Agent Skills promoted to stable
- Sub-agents with JSON schema validation
- Queued tool confirmations
- Expandable/collapsible text blocks
- Improved Settings UI
- Better shell output formatting
- Disk-full error handling during chat recording

**References:**
- [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)
- [Gemini CLI Documentation](https://geminicli.com/brain/knowledge/docs_legacy/)
- [Google AI Dev Docs - Models](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models)
- [Gemini CLI Changelog](https://geminicli.com/brain/knowledge/docs_legacy/changelogs/latest/)
- [Gemini CLI Hooks](https://geminicli.com/brain/knowledge/docs_legacy/hooks/)
- [Agent Skills Documentation](https://geminicli.com/brain/knowledge/docs_legacy/cli/skills/)
- [Custom Commands Guide](https://geminicli.com/brain/knowledge/docs_legacy/cli/custom-commands/)
- [GEMINI.md Context Files](https://geminicli.com/brain/knowledge/docs_legacy/cli/gemini-md/)
- [Sandboxing Documentation](https://geminicli.com/brain/knowledge/docs_legacy/cli/sandbox/)
- [Trusted Folders Guide](https://geminicli.com/brain/knowledge/docs_legacy/cli/trusted-folders/)
- [Gemini 3 Flash Launch](https://blog.google/products-and-platforms/products/gemini/gemini-3-flash/)
- [Build with Gemini 3 Flash](https://blog.google/technology/developers/build-with-gemini-3-flash/)

**Feature Status Summary:**
All major features fully supported. Gemini CLI maintains comprehensive agent capabilities with full hooks system, MCP integration, stable Agent Skills, sub-agents, TOML custom commands, Git/GitHub Actions integration, web search, sandbox security, cost tracking via /stats, hierarchical memory system, and multimodal support. Version 0.27.0 solidifies position as feature-rich AI coding assistant.
```

## File: `research/2026-02-06_11-08-08/result.md`
```markdown
# Research Results

**Completed:** 2026-02-06 11:08
**Research Folder:** research/2026-02-06_11-08-08/

## Summary

| Tool | Context Window Changes | Feature Changes |
|------|------------------------|-----------------|
| Claude Code | YES - Opus 4.6 (1M beta, 128k output) | YES - Sandbox ✅, Memory ✅, Image ✅, Agent Teams |
| Codex CLI | YES - GPT-5.3-Codex (400k, Perfect Recall) | YES - Custom System Prompts ✅ |
| Cursor | YES - Claude 4.6 Opus, DeepSeek V3.1, Grok Code added | NO - Minor refinements only |
| Gemini CLI | YES - Gemini 3 Flash Preview added (Feb 4) | YES - Sub-agents ✅ (was ⚠️) |

---

## Proposed Context Window Table (README.md)

| Tool | Largest Context | Best Model | Source |
|------|-----------------|------------|--------|
| Claude Code | 1M (beta) | Opus 4.6 with `--betas context-1m-2025-08-07` | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
| Codex CLI | 400k+ | GPT-5.3-Codex (context compaction) | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
| Cursor | 2M (Max mode) | Grok 4 | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
| Gemini CLI | 1M | Gemini 3 Pro Preview | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |

---

## Proposed Feature Table (README.md)

| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------|:-----------:|:---------:|:----------:|:------:|
| **Hooks** | ✅ | ⚠️ | ✅ | ✅ |
| **Plugins/MCP** | ✅ | ✅ | ✅ | ✅ |
| **Sub-agents** | ✅ | ✅ | ✅ | ✅ |
| **Slash Commands** | ✅ | ✅ | ✅ | ✅ |
| **Custom Commands** | ✅ | ✅ | ✅ | ✅ |
| **IDE Integration** | ✅ | ✅ | ✅ | ✅ |
| **Git Integration** | ✅ | ✅ | ✅ | ✅ |
| **Web Search** | ✅ | ✅ | ✅ | ✅ |
| **Image Support** | ✅ | ✅ | ✅ | ⚠️ |
| **Memory/Persistence** | ✅ | ✅ | ✅ | ⚠️ |
| **Multi-file Editing** | ✅ | ✅ | ✅ | ✅ |
| **Auto-commit** | ⚠️ | ⚠️ | ✅ | ✅ |
| **Custom System Prompts** | ✅ | ✅ | ✅ | ✅ |
| **Cost Tracking** | ✅ | ❌ | ✅ | ⚠️ |
| **Sandbox Mode** | ✅ | ✅ | ✅ | ⚠️ |

---

## Diff: Current vs New

### README.md - Context Window Changes

```diff
 | Tool | Largest Context | Best Model | Source |
 |------|-----------------|------------|--------|
-| Claude Code | 1M (beta) | Sonnet 4.5 with `--betas context-1m-2025-08-07` | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
+| Claude Code | 1M (beta) | Opus 4.6 with `--betas context-1m-2025-08-07` | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
-| Codex CLI | 400k+ | GPT-5.2-Codex (context compaction) | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
+| Codex CLI | 400k+ | GPT-5.3-Codex (context compaction) | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
-| Cursor | 1M (Max mode) | Gemini 3 Pro/Flash | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
+| Cursor | 2M (Max mode) | Grok 4 | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
 | Gemini CLI | 1M | Gemini 3 Pro Preview | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |
```

### README.md - Feature Changes

```diff
 | Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
 |---------|:-----------:|:---------:|:----------:|:------:|
 | **Hooks** | ✅ | ⚠️ | ✅ | ✅ |
 | **Plugins/MCP** | ✅ | ✅ | ✅ | ✅ |
-| **Sub-agents** | ✅ | ✅ | ⚠️ | ✅ |
+| **Sub-agents** | ✅ | ✅ | ✅ | ✅ |
 | **Slash Commands** | ✅ | ✅ | ✅ | ✅ |
 | **Custom Commands** | ✅ | ✅ | ✅ | ✅ |
 | **IDE Integration** | ✅ | ✅ | ✅ | ✅ |
-| **Git Integration** | ✅ | ✅ | ⚠️ | ✅ |
+| **Git Integration** | ✅ | ✅ | ✅ | ✅ |
 | **Web Search** | ✅ | ✅ | ✅ | ✅ |
-| **Image Support** | ⚠️ | ✅ | ✅ | ⚠️ |
+| **Image Support** | ✅ | ✅ | ✅ | ⚠️ |
-| **Memory/Persistence** | ⚠️ | ✅ | ✅ | ⚠️ |
+| **Memory/Persistence** | ✅ | ✅ | ✅ | ⚠️ |
 | **Multi-file Editing** | ✅ | ✅ | ✅ | ✅ |
 | **Auto-commit** | ⚠️ | ⚠️ | ✅ | ✅ |
-| **Custom System Prompts** | ✅ | ⚠️ | ✅ | ✅ |
+| **Custom System Prompts** | ✅ | ✅ | ✅ | ✅ |
 | **Cost Tracking** | ✅ | ❌ | ✅ | ⚠️ |
-| **Sandbox Mode** | ❌ | ✅ | ✅ | ⚠️ |
+| **Sandbox Mode** | ✅ | ✅ | ✅ | ⚠️ |
```

### reports/context-comparison.md - Claude Code Changes

```diff
 ## Claude Code

 | Model | Context Window | Max Output | Notes |
 |-------|----------------|------------|-------|
+| Opus 4.6 | 200k (1M beta) | 128k | Latest model, adaptive thinking, first Opus with 1M context |
 | Opus 4.5 | 200k | 64k | Premium model, complex reasoning, 67% lower cost than predecessor |
 | Sonnet 4.5 | 200k (1M beta) | 64k | Recommended default, context awareness feature, best coding model |
 | Haiku 4.5 | 200k | 64k | Fastest, context awareness feature, unbeatable for UI work |

 **Legacy Models (Still Available):**
+- Opus 4.5: 200k tokens, 64k max output
 - Opus 4.1: 200k tokens, 32k max output
 - Sonnet 4: 200k / 1M beta, 64k max output
```

### reports/context-comparison.md - Codex CLI Changes

```diff
 ## Codex CLI

 | Model | Context Window | Max Output | Notes |
 |-------|----------------|------------|-------|
+| GPT-5.3-Codex | 400k | 128k | Latest model (Feb 5, 2026), Perfect Recall attention, 25% faster |
 | GPT-5.2-Codex | 400k | 128k | Latest model (Jan 14, 2026), native compaction, reliable tool calling |
 | GPT-5.1-Codex-Max | Multi-window (millions) | N/A | First model natively trained for compaction |
```

### reports/context-comparison.md - Cursor Changes

```diff
 ### Anthropic Models

 | Model | Context Window | Max Output | Notes |
 |-------|----------------|------------|-------|
+| Claude 4.6 Opus | 200k (1M max) | 64k | NEW - Latest Opus model |
 | Claude 4.5 Sonnet | 200k (1M max) | 64k | Premium, Agent/Thinking modes |
-| Claude 4.1 Opus | 200k | 64k | Max mode only, deep reasoning |
+| Claude 4.5 Opus | 200k | 64k | Deep reasoning |

 ### xAI Models

 | Model | Context Window | Max Output | Notes |
 |-------|----------------|------------|-------|
 | Grok 4 | 200k (2M max) | - | Real-time web search integration |
+| Grok Code | 256k | - | Code-optimized |
 | Grok Code Fast | 200k | - | Optimized for speed |

 ### DeepSeek Models

 | Model | Context Window | Max Output | Notes |
 |-------|----------------|------------|-------|
-| DeepSeek V3 | 200k | - | Native support since v0.44+, hosted on US servers |
+| DeepSeek V3 | 64k-128k | - | Native support, hosted on US servers |
+| DeepSeek V3.1 | 128k | - | NEW - Upgraded context from V3 |
 | DeepSeek R1 | 200k | - | Native support since v0.45+, free within Pro plan |
```

### reports/context-comparison.md - Gemini CLI Changes

```diff
 ## Gemini CLI

 | Model | Context Window | Max Output | Status |
 |-------|----------------|------------|--------|
 | Gemini 3 Pro Preview | 1M | 65k | Current flagship |
-| Gemini 3 Flash Preview | 1M | 65k | Balanced speed/intelligence |
+| Gemini 3 Flash Preview | 1M | 65k | Balanced speed/intelligence - Launched Feb 4, 2026 |
 | Gemini 3 Pro Image Preview | 65k | 32k | Image generation |
+| Gemini 2.5 Flash TTS | 8k | 16k | Text-to-speech (Preview) |
+| Gemini 2.5 Flash Preview | 1M | 65k | Experimental features (Preview) |
```

---

## Detailed Change Summary

### Context Window Changes

1. **Claude Code**: Opus 4.6 released Feb 5, 2026 - first Opus model with 1M context (beta) and 128k max output (doubled from 64k). Best model changes from Sonnet 4.5 to Opus 4.6.
2. **Codex CLI**: GPT-5.3-Codex released Feb 5, 2026 - 400k context with "Perfect Recall" attention mechanism, 25% faster than predecessor.
3. **Cursor**: New models added - Claude 4.6 Opus (1M max), DeepSeek V3.1 (128k), Grok Code (256k). Largest context now 2M via Grok 4 Max mode.
4. **Gemini CLI**: Gemini 3 Flash Preview launched Feb 4, 2026. Added Gemini 2.5 Flash TTS and Flash Preview models. Core context windows unchanged at 1M.

### Feature Changes

1. **Claude Code**: Sandbox Mode upgraded from ❌ to ✅ (macOS/Linux sandboxing). Memory/Persistence upgraded from ⚠️ to ✅ (automatic memory, CLAUDE.md, .claude/rules/). Image Support upgraded from ⚠️ to ✅ (all Claude 4 models). New: Agent Teams, unified Skills system, LSP tool, PDF reading, keybindings.
2. **Codex CLI**: Custom System Prompts upgraded from ⚠️ to ✅ (Markdown-based custom prompts). New: GPT-5.3-Codex, JetBrains/Visual Studio/Xcode/Eclipse IDE support, live skill update detection.
3. **Gemini CLI**: Sub-agents upgraded from ⚠️ to ✅ (AgentRegistry, JSON schema validation). Git Integration upgraded from ⚠️ to ✅ (GitHub Actions integration, AI commit messages). New: v0.27.0 event-driven architecture, Agent Skills stable, /rewind command.
4. **Cursor**: Minor refinements. New: Cursor Blame (Enterprise), Agent Q&A, Cloud agents, image generation. Feature statuses largely confirmed as-is.

---

## Date Updates

README.md and reports/context-comparison.md "Last Updated" date should change from `2026-02-04` to `2026-02-06`.
```

## File: `research/2026-02-09_12-44-16/research.md`
```markdown
# Context Window & Features Research Session

**Started:** 2026-02-09 12:44:16 UTC
**Status:** In Progress

---

## Claude Code Research
**Agent:** Dr. Sarah Chen
**Status:** Complete

### Context Windows

**Latest Models (2026)**

| Model | Context Window | Max Output | Status |
|-------|---------------|------------|--------|
| Claude Opus 4.6 | 200K / 1M (beta) | 128K tokens | Latest (Released Feb 5, 2026) |
| Claude Sonnet 4.5 | 200K / 1M (beta) | 64K tokens | Current |
| Claude Haiku 4.5 | 200K | 64K tokens | Current |

**Extended Context (1M Token Window)**
- Available for Opus 4.6, Sonnet 4.5, and Sonnet 4 via `context-1m-2025-08-07` beta header
- Currently in beta for organizations in usage tier 4 and organizations with custom rate limits
- Available on Claude API, Microsoft Foundry, Amazon Bedrock, and Google Cloud Vertex AI
- Premium pricing applies: 2x input, 1.5x output for requests exceeding 200K tokens
- For Opus 4.6: 1M context is available for API and Claude Code pay-as-you-go users
- Pro, Max, Teams, and Enterprise subscription users do NOT have access to Opus 4.6 1M context at launch

**Claude Code Model Aliases**
- `default` - Recommended model (Opus 4.6 for Max/Teams/Pro users)
- `opus` - Latest Opus model (currently Opus 4.6)
- `sonnet` - Latest Sonnet model (currently Sonnet 4.5)
- `haiku` - Fast and efficient Haiku model
- `sonnet[1m]` - Sonnet with 1 million token context window
- `opusplan` - Special hybrid mode: uses Opus during planning, switches to Sonnet for execution

**Context Awareness**
- Claude Sonnet 4.5 and Haiku 4.5 feature context awareness
- Models track remaining token budget throughout conversation
- System provides token usage warnings: `Token usage: 35000/200000; 165000 remaining`
- Enables more effective execution on long-running tasks

**Context Management**
- Server-side compaction available (beta for Opus 4.6) - automatically condenses earlier conversation parts
- Context editing strategies: tool result clearing, thinking block clearing
- Extended thinking blocks automatically stripped from context window in subsequent turns
- Models return validation errors when exceeding context window (no silent truncation)

**Legacy Models**
- Opus 4.5 (200K context, 64K output) - May 2025 cutoff
- Opus 4.1 (200K context, 32K output) - Jan 2025 cutoff
- Sonnet 4 (200K / 1M beta, 64K output) - Jan 2025 cutoff
- Sonnet 3.7 (200K, 64K / 128K beta output) - Oct 2024 cutoff
- Opus 4 (200K, 32K output) - Jan 2025 cutoff
- Haiku 3 (200K, 4K output) - Aug 2023 cutoff

**Knowledge Cutoffs**
- Opus 4.6: May 2025 (reliable) / Aug 2025 (training data)
- Sonnet 4.5: Jan 2025 (reliable) / Jul 2025 (training data)
- Haiku 4.5: Feb 2025 (reliable) / Jul 2025 (training data)

### Features

**Hooks System**
- **Hook Types Available:**
  - `PreToolUse` - Fires before tool execution with tool_name, tool_input, tool_use_id
  - `PostToolUse` - Fires after successful tool completion with tool_input and tool_response
  - `PostToolUseFailure` - Fires after failed tool execution
  - `Notification` - Fires when Claude sends notifications (permission requests or 60s idle)
  - `PermissionRequest` - Fires when permission dialog shown
  - `UserPromptSubmit` - Fires when user submits prompt
  - `Stop` - Fires when Claude Code finishes responding
  - `SubagentStop` / `TaskStopHook` - Fires when subagents (Task tools) finish
  - `TaskCompleted` - Fires when task completes

- **Hook Implementations:**
  - Bash command hooks (type: "command")
  - Prompt-based hooks (type: "prompt") - use LLM to evaluate actions
  - Decision control: allow, deny, or ask for permission
  - Dynamic control over tool usage validation

**MCP (Model Context Protocol) Support**
- Full MCP server support with --agents flag accepting JSON configuration
- Sub-agents can access SDK-provided MCP tools (synced to shared application state)
- Pre-configured OAuth client credentials for MCP servers without Dynamic Client Registration
- Use --client-id and --client-secret flags with `claude mcp add`
- Slack and other OAuth providers supported

**Sub-agents & Agent Teams**
- Autonomous AI workers that Claude spawns for specific tasks
- Run up to 7 simultaneous parallel operations
- Dramatically speeds up complex workflows (codebase exploration, multi-file analysis)
- Research preview: Agent Teams for multi-agent collaboration
  - Token-intensive feature
  - Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
  - Team lead agent plans and delegates to specialist background agents

**Slash Commands**
- User-invoked workflow templates stored as Markdown files
- Every skill requires SKILL.md file with YAML frontmatter
- Name field becomes the /slash-command
- Built-in commands: /model, /status, /teleport, /fast, /workflow
- Custom commands can be created in .claude/commands/

**Skills System**
- Custom commands/skills support with hot-reloading (as of v2.1.0)
- Skills can fetch live data (e.g., GitHub CLI: `gh pr diff`, `gh pr view --comments`)
- Output automatically inserted into prompts
- Organized plugins covering cloud platforms (GitHub, Azure, MongoDB)

**IDE Integrations**
- **VS Code Extension** (Native):
  - Native graphical interface integrated directly into IDE
  - Review and edit Claude's plans before accepting
  - Auto-accept edits as they're made
  - @-mention files with specific line ranges
  - Access conversation history
  - Multiple conversations in separate tabs/windows
  - See current file, selected code, error messages automatically

- **JetBrains Plugin** (Beta):
  - Available for IntelliJ IDEA, PyCharm, WebStorm, GoLand, etc.
  - Runs Claude Code CLI inside IDE's integrated terminal
  - Opens proposed changes in IDE's diff viewer
  - Available from JetBrains Marketplace

**Git Integration**
- Handles git workflows through natural language commands
- Execute routine tasks, explain complex code
- Claude Hub: connects to GitHub repositories
  - AI-powered code assistance in PRs and issues
  - Analyze repositories via @mentions
  - Answer technical questions
  - Help developers understand and improve codebase
- Session Restore: efficiently restores context from session files and git history
- Automatic git history analysis

**Web Search Capability**
- Web search functionality available (US only as of documentation)
- Domain filtering supported (include/block specific websites)
- Results formatted as search result blocks with markdown links

**Sandboxing & Security**
- Native sandboxing with OS-level primitives
- Filesystem and network isolation enforced
- Reduces permission prompts by 84% in internal usage
- Web-based Claude Code: isolated sandbox per session
- Sensitive credentials kept outside sandbox
- Vercel Sandbox integration available

**Cost Tracking**
- Real-time cost tracking via Claudia dashboard
- See expenses by project/model
- Enhanced statusline tools include cost tracking
- MCP server monitoring in status line

**Background Agents**
- Background agent support added in v2.1.0 (January 7, 2026)
- Swarms feature (experimental): team lead agent delegates to specialist background agents
  - Discovered via feature flags (January 24, 2026)
  - Provides multi-agent orchestration

**Additional Features (2026)**
- Session teleportation via /teleport (v2.1.0)
- Claude in Chrome beta (v2.1.0)
- Language settings customization (v2.1.0)
- 3x memory improvement (v2.1.0)
- Effort levels for Opus 4.6: low/medium/high (controls adaptive reasoning)
- Prompt caching with granular control (per-model disable options)
- Token counting API for usage estimation
- Fast mode: same model with faster output (toggle with /fast)
- Extended thinking with adaptive thinking (Opus 4.6)
- Interleaved thinking: think between tool calls (Claude 4 models)
- Plan Mode: special reasoning mode for architecture decisions

**Configuration**
- Environment variables for model control:
  - `ANTHROPIC_DEFAULT_OPUS_MODEL`
  - `ANTHROPIC_DEFAULT_SONNET_MODEL`
  - `ANTHROPIC_DEFAULT_HAIKU_MODEL`
  - `CLAUDE_CODE_SUBAGENT_MODEL`
  - `CLAUDE_CODE_EFFORT_LEVEL`
  - `DISABLE_PROMPT_CACHING` (and per-model variants)
  - `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`
- Settings file configuration for permissions, model, effortLevel
- Command-line flags: --model, --agents, --client-id, --client-secret

---

## Codex CLI Research
**Agent:** Marcus Thompson
**Status:** Complete

### Context Windows

**Research Date:** 2026-02-09
**Sources:** [OpenAI Codex Models](https://developers.openai.com/codex/models/), [OpenAI Platform Docs](https://platform.openai.com/brain/knowledge/docs_legacy/models), [OpenAI Blog](https://openai.com/index/introducing-gpt-5-3-codex/)

#### Primary Models (Recommended)

| Model | Context Window | Max Output | Status | Notes |
|-------|---------------|------------|--------|-------|
| gpt-5.3-codex | 400,000 tokens | - | Latest | Default for Codex CLI, 25% faster |
| gpt-5.2-codex | 400,000 tokens | - | Stable | Succeeded by GPT-5.3-Codex |
| gpt-5.1-codex-mini | 400,000 tokens | 128,000 tokens | Stable | Cost-effective version |

#### Reasoning Models (o-series)

| Model | Context Window | Max Output | Status | Notes |
|-------|---------------|------------|--------|-------|
| o3 | 200,000 tokens | - | Latest | New reasoning model for complex tasks |
| o4-mini | 200,000 tokens | - | Latest | Fast, cost-efficient reasoning |
| codex-mini-latest | 200,000 tokens | 100,000 tokens | Stable | Fine-tuned o4-mini for Codex CLI |
| o1 | 200,000 tokens | 100,000 tokens | Stable | Previous generation reasoning |
| o1-preview | 128,000 tokens | 32,768 tokens | Deprecated | Removed April 28, 2025 |
| o1-mini | 128,000 tokens | 65,536 tokens | Deprecated | Removed April 28, 2025 |

#### Legacy Models

| Model | Context Window | Max Output | Status | Notes |
|-------|---------------|------------|--------|-------|
| GPT-4.1 | 1,000,000 tokens | - | Stable | Up to 1M token context |
| GPT-4.1 mini | 1,000,000 tokens | - | Stable | Improved instruction following |
| GPT-4o | 128,000 tokens | 16,384 tokens | API Only | Retired from ChatGPT Feb 13, 2026 |
| GPT-4o mini | 128,000 tokens | 16,384 tokens | Stable | - |

#### Model Deprecations (2025-2026)

- **o1-preview, o1-mini**: Deprecated April 28, 2025
- **chatgpt-4o-latest**: Deprecated Nov 18, 2025; API removal Feb 17, 2026
- **GPT-4o, GPT-4.1, GPT-4.1 mini, o4-mini**: Retired from ChatGPT Feb 13, 2026 (API access continues)

#### Context Window Features

- **Context Compaction**: `/compact` slash command - summarizes conversations while preserving critical details
- **Token Usage Tracking**: `/status` command shows model, approval policy, and current token usage
- **Efficient Token Usage**: GPT-5.3-Codex achieves state-of-the-art performance with fewer tokens than any prior model

### Features

**Research Date:** 2026-02-09
**Sources:** [Codex CLI Features](https://developers.openai.com/codex/cli/features/), [Codex Changelog](https://developers.openai.com/codex/changelog/), [GitHub Releases](https://github.com/openai/codex/releases)

#### 1. Hooks Support
**Status:** Limited Support

- **Notification Hooks**: Triggered when Codex completes a task
- **Note**: Full hooks system is under active discussion in the community (GitHub Issue #2150)

#### 2. MCP (Model Context Protocol) Support
**Status:** Full Support

- **STDIO Servers**: Local process servers started by command
- **HTTP Servers**: Remote servers accessed at an address
- **Configuration**: `codex mcp add <server-name>` command
- **Config Files**: `~/.codex/config.toml` or `.codex/config.toml` for project-specific
- **Codex as MCP Server**: Exposes `codex()` and `codex-reply()` tools
- **Agents SDK Integration**: Compatible with OpenAI Agents SDK for orchestration

#### 3. Sub-agents Capability
**Status:** Beta Support

- **Agents SDK Integration**: Full integration with OpenAI Agents SDK
- **Multi-agent Workflows**: Codex can be orchestrated as part of larger workflows
- **Personal Skills**: Load from `~/.agents/skills` directory
- **Collaboration Mode**: Beta feature with plan → execute handoff

#### 4. Slash Commands
**Status:** Full Support

**Built-in Commands:**
- `/status` - View active model, approval policy, writable roots, token usage
- `/compact` - Summarize long conversations to free context
- `/mention` - Add files to conversation by path
- `/new` - Start fresh conversation in same CLI session
- `/resume` - Continue previous saved sessions
- `/fork` - Clone current conversation into new thread
- `/init` - Create AGENTS.md scaffold for repository conventions
- `/review` - Summarize issues in working tree
- `/model` - Switch between models or adjust reasoning levels
- `/permissions` (or `/approvals`) - Manage approval settings
- `/debug-config` - Inspect effective configuration
- `/plan` - Accepts inline prompt arguments and pasted images

**Custom Commands:**
- Team-specific shortcuts supported
- Reusable prompts for common workflows

#### 5. IDE Integrations
**Status:** Full Support (Multi-platform)

**Supported IDEs:**
- **VS Code**: Official Codex VS Code extension
- **JetBrains IDEs** (v2025.3+): IntelliJ, PyCharm, WebStorm, Rider
  - Native integration in AI chat
  - Authentication: JetBrains AI, ChatGPT, or BYOK
- **Cursor**: Compatible with Codex IDE extension
- **Windsurf**: Compatible with Codex IDE extension
- **Visual Studio, Xcode, Eclipse**: GPT-5.2-Codex available (Jan 26, 2026)

#### 6. Git Integration Features
**Status:** Full Support

- **Change Tracking**: Shows changes as diffs before committing
- **Commit Workflow**: Auto-commit with meaningful messages
- **Code Review**:
  - Review against base branch
  - Review uncommitted changes
  - Review specific commits by SHA
- **Safety Features**: Git command safety hardened; destructive operations require approval
- **Transcript History**: All actions surfaced for git review/rollback
- **GitHub Integration**: Public preview (Feb 4, 2026)

#### 7. Web Search Capability
**Status:** Built-in Tool

- **First-party Search**: Enabled by default for local tasks
- **Caching**: Uses cached results or live fetching based on configuration
- **No Setup Required**: Works out of the box

#### 8. Sandbox/Approval Modes
**Status:** Full Support

**Three Approval Modes:**
- **Suggest Mode** (default): Requires approval for all actions
- **Auto-Edit Mode**: Auto-applies file changes; requires approval for shell commands
- **Full-Auto Mode**: Fully autonomous without user input

**Sandbox Controls:**
- **OS-enforced Sandbox**: Limits workspace access, network reach, command execution
- **Approval Policy**: When Codex must ask before acting
- **Network Sandbox**: Policy enforcement proxy for outbound network access
- **Switch Modes**: Via `/approvals` or `/permissions` command

#### 9. Cost Tracking Options
**Status:** Partial Support

**Available:**
- `/status` command shows current token usage and remaining limits
- Codex usage dashboard shows limits
- **Third-party Tool**: `ccusage` package for analyzing token usage/costs from local JSONL files

**Missing:**
- No comprehensive built-in cost analytics (GitHub Issue #5085 tracking feature request)

**Pricing:**
- Included with ChatGPT Plus ($20/month) or Pro ($200/month)
- API access: codex-mini-latest ($1.50/M input, $6.00/M output)

#### 10. Additional Features (2026)

**New in 2026:**
- **Steer Mode** (Jan 2026): Stable and default - Enter sends immediately, Tab queues follow-up
- **GPT-5.3-Codex Support** (Feb 2026): Mid-turn steering capabilities
- **Codex Desktop Launch** (Jan 2026): `codex app <path>` on macOS
- **Image Inputs**: Screenshots and design specs alongside prompts
- **Non-interactive Automation**: `exec` subcommand for scripting and CI integration
- **Cloud Integration**: Launch and manage Codex cloud tasks from terminal
- **Shell Completions**: bash, zsh, and fish auto-completion
- **Conversation Resuming**: Local transcript storage with resume capability
- **Memory Features**: Initial memory plumbing with thread memory summaries
- **GitHub Integration**: Public preview (Feb 4, 2026)

**Core Features:**
- **Interactive Mode**: Full-screen terminal UI with real-time review
- **Code Review**: Dedicated reviewer accessible via `/review`
- **Multi-directory Coordination**: `--add-dir` flag
- **Quick Shortcuts**: File search (`@`), command injection (`!`), transcript navigation (Esc)

#### Summary

Codex CLI is a production-ready CLI coding agent with:

**Strengths:**
- Multiple model options (400k to 1M token context windows)
- Full MCP integration for extensibility
- Native IDE support across major platforms
- Robust git workflow integration
- Flexible approval and sandbox controls
- Web search and multi-modal inputs
- Active development with frequent updates

**Limitations:**
- Limited hooks support (only notification hooks)
- No comprehensive built-in cost tracking/analytics

**Best For:**
- Teams using OpenAI models
- Multi-platform IDE integration needs
- Developers prioritizing model variety (reasoning vs speed)
- Projects requiring MCP extensibility

---

## Cursor Research
**Agent:** Elena Rodriguez
**Status:** Complete

### Context Windows

**Research Date:** 2026-02-09
**Sources:** [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models), [Cursor Changelog](https://cursor.com/changelog), [Composer Blog](https://cursor.com/blog/composer)

Cursor supports frontier models from four major providers plus its own native model.

#### Anthropic Claude Models

| Model | Context Window | Max Mode | Notes |
|-------|---------------|----------|-------|
| Claude 4.6 Opus | 200k | 1M | Latest (Feb 5, 2026), 2x cost above 200k |
| Claude 4.5 Sonnet | 200k | 1M | 2x cost above 200k |
| Claude 4 Sonnet | 200k | 1M | Hidden by default, 2x cost above 200k |

#### OpenAI GPT Models

| Model | Context Window | Notes |
|-------|---------------|-------|
| GPT-5.3 Codex | 272k | Latest (Feb 5, 2026), 77.3% Terminal-Bench |
| GPT-5.2 | 272k | Stable |
| GPT-5 series | Various | Most hidden by default |

#### Google Gemini Models

| Model | Context Window | Max Mode | Native | Notes |
|-------|---------------|----------|--------|-------|
| Gemini 3 Pro | 200k | 1M | 2M | Visual reasoning leader |
| Gemini 3 Flash | 200k | 1M | - | - |
| Gemini 2.5 Flash | 200k | 1M | - | Hidden, $0.3M input |

#### xAI Grok Models

| Model | Context Window | Notes |
|-------|---------------|-------|
| Grok 4 Code | 131k-2M | Varies by variant, multimodal |
| Grok Code Fast 1 | 1M | Cost-effective: $0.2M input |

#### Cursor Native Models

| Model | Context Window | Speed | Pricing |
|-------|---------------|-------|---------|
| Composer 1 | 200k | 250 tok/sec (4x faster) | $1.25/M in, $10/M out |

- MoE architecture, RL-trained on real engineering tasks
- Completes most turns in <30 seconds

#### DeepSeek Models

| Model | Context Window | Notes |
|-------|---------------|-------|
| DeepSeek R1 | Standard | Free tier, US servers (Fireworks.ai) |
| DeepSeek V3 | Standard | Free tier, US servers |

#### Context Features
- **Standard**: 200k tokens (~15,000 lines of code)
- **Max Mode**: 1M-2M tokens (model-dependent)
- **Cost**: 2x for Claude/Gemini above 200k
- **Privacy**: Encrypted storage, obfuscated filenames

#### Recent Changes
- **Late 2025**: Free models moved to request-based pricing
- **Dec 2025**: v2.1.42 temporarily removed models
- **2025**: Token-based → unified request-based pricing

### Features

**Research Date:** 2026-02-09

#### 1. Hooks System (Jan 2026 - 40x faster)
**Full lifecycle control via custom scripts**

**Events:** sessionStart/End, preToolUse, postToolUse/Failure, subagentStart/Stop, beforeShellExecution, afterShellExecution, beforeMCPExecution, afterMCPExecution, beforeReadFile, afterFileEdit, beforeTabFileRead, afterTabFileEdit, beforeSubmitPrompt, preCompact, stop, afterAgentResponse, afterAgentThought

**Config:** `.cursor/hooks.json` (project), `~/.cursor/hooks.json` (user), system paths

**Types:** Command-based (shell) or Prompt-based (LLM policies)

**Partners:** MintMCP, Oasis, Runlayer, Corridor, Semgrep, Endor Labs, Snyk, 1Password

#### 2. MCP (Model Context Protocol)
**External tools and data sources**

- Automatic OAuth callback handling
- `/mcp list`, `/mcp enable`, `/mcp disable`
- On-demand JSON loading in `.cursor/`
- Immediate authenticated MCP access
- Jan 2026: Improved login, reduced tokens

#### 3. Sub-Agents (Jan 22, 2026)
**Parallel independent agents**

**Built-in:** Explore (codebase), Bash (shell isolation), Browser (MCP interactions)

**Custom:** `.cursor/agents/` or `~/.cursor/agents/`

**Modes:** Foreground (blocking) / Background (async)

**Limits:** Single-level only, token multiplication in parallel

#### 4. Slash Commands
- `/plan` - Design with clarifying questions
- `/ask` - Non-destructive exploration
- `/models` - List/switch models
- `/rules` - Edit rules
- `/mcp enable/disable` - MCP management
- `/summarize` - Context summarization

#### 5. Custom Rules
**AI behavior configuration**

- **Legacy:** `.cursorrules` (deprecated, will be removed)
- **Current:**
  - User Rules: Settings > General > Rules for AI
  - Project Rules: `.cursor/rules/*.mdc`
  - Skills: `SKILL.md` (Jan 22, 2026) - dynamic context discovery
- `/rules` command (Jan 8, 2026)

#### 6. Composer/Agent Mode (Cursor 2.0 - Nov 2025)
**Multi-file editing, agent-centric interface**

- Native ultra-fast model (4x speed)
- Agents/plans/runs as sidebar objects
- Multiple parallel agents per project
- 4 layouts: agent, editor, zen, browser (⌘⌥⇥)
- Clarifying questions mid-conversation (Jan 22, 2026)
- Word-level inline diffs (CLI - Jan 16, 2026)

#### 7. Git Integration
- Commit Composer - AI-organized messages
- @Branch, @Git context symbols
- Stage, commit, push/pull automation
- **Cursor Blame** (Enterprise, Jan 22, 2026) - AI attribution
- GitButler hooks (v1.7) - Auto-commits from chats

#### 8. Web Search (@Web)
- `@Web [query]` in prompts
- Settings > Features > Web Search (off by default)
- "Always search" option
- Fairness limits apply

#### 9. Background/Cloud Agents (2025 release)
- Prepend `&` to push to cloud
- Clone GitHub repos, separate branches
- Ubuntu-based isolated machines
- Continue at cursor.com/agents
- Use cases: parallel dev, long-running tasks

#### 10. Codebase Indexing
- Merkle tree of file hashes
- 10-minute incremental sync
- Server-side embedding (Turbopuffer)
- Encrypted storage, obfuscated filenames
- `.cursorignore` exclusions

#### 11. VS Code Extension Compatibility
- 99%+ extensions work
- Open VSX Registry (not MS Marketplace per ToS)
- One-Click Import on first launch
- **Problematic:** Pylance (use BasedPyright), C# Dev Kit, C/C++ (use clangd), Live Share
- 90% cross-published to both registries

#### 12. Memories (Cursor 1.0 - Feb 3, 2026)
- AI remembers conversation facts
- Background Agent workflow adaptation
- Tailored support across sessions
- **Ecosystem:** Memory Bank (community), SpecStory (durable knowledge)

#### 13. Enterprise Features
- **Conversation Insights** (Dec 18, 2025) - Analytics
- **Transcript Sharing** (Dec 18, 2025) - Read-only with fork
- **Billing Groups** (Dec 18, 2025) - Spend tracking
- **Linux Sandboxing** (Dec 18, 2025) - Configurable access
- **Service Accounts** (Dec 18, 2025) - Non-human automation
- **Cursor Blame** (Jan 22, 2026) - AI attribution

#### 14. Additional Features
- **Image Generation** (Jan 22, 2026) - Google Nano Banana Pro
- **Browser:** 10x faster, drag-and-drop, locking
- **Auto Model Selection:** Performance-based switching
- **Layout:** 4 switchable presets

#### Summary

Cursor is a multi-model IDE with comprehensive features:

**Strengths:**
- Multi-provider support (Claude, GPT, Gemini, Grok, DeepSeek, Composer)
- 200k-2M context windows with Max Mode
- Extensive hooks (40x faster in 2026)
- Full MCP + sub-agents + cloud execution
- VS Code compatibility (99%+)
- Enterprise analytics and attribution
- Memories for persistent context

**Limitations:**
- Rules migration from .cursorrules to .cursor/rules/
- VS Code Marketplace restrictions (MS proprietary extensions)
- Max Mode 2x pricing above 200k for Claude/Gemini

**Best For:**
- Teams wanting model flexibility
- Projects needing parallel agent workflows
- Organizations with VS Code infrastructure
- Developers prioritizing speed (Composer 1)

---

## Gemini CLI Research
**Agent:** Dr. Raj Patel
**Status:** Complete

### Context Windows

**Research Date:** 2026-02-09
**Sources:** [Gemini API Models](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models), [Gemini CLI GitHub](https://github.com/google-gemini/gemini-cli)

#### Current Models (February 2026)

| Model Name | Context Window | Max Output Tokens | Status | Notes |
|------------|---------------|-------------------|---------|-------|
| Gemini 3 Pro Preview | 1,048,576 (1M) | 65,536 (64K) | Preview | Released November 2025 |
| Gemini 3 Flash Preview | 1,048,576 (1M) | 65,536 (64K) | Preview | Released December 2025 |
| Gemini 2.5 Pro | 1,048,576 (1M) | 65,536 (64K) | Stable | Released June 2025 |
| Gemini 2.5 Flash | 1,048,576 (1M) | 65,536 (64K) | Stable | Released June 2025 |
| Gemini 2.5 Flash-Lite | 1,048,576 (1M) | 65,536 (64K) | Stable | Released July 2025 |

#### Deprecated Models

| Model Name | Context Window | Max Output Tokens | Shutdown Date |
|------------|---------------|-------------------|---------------|
| Gemini 2.0 Flash | 1,048,576 (1M) | 8,192 (8K) | March 31, 2026 |
| Gemini 2.0 Flash-Lite | 1,048,576 (1M) | 8,192 (8K) | March 31, 2026 |

#### Key Findings

- **Industry-Leading Context**: All current Gemini models support 1M token context windows (1,048,576 tokens exactly)
- **Enhanced Output**: Gemini 2.5 and 3.x models significantly increased max output from 8K to 64K tokens compared to 2.0 models
- **Model Transition**: Gemini 2.0 Flash models are being phased out on March 31, 2026
- **Context Capabilities**: 1M tokens = ~1,500 pages of text or ~30,000 lines of code
- **Multimodal Support**: Context window handles text, code, images, and video
- **Token Caching**: Built-in token caching optimizes performance and costs for repeated context

### Features

**Research Date:** 2026-02-09
**Sources:** [Gemini CLI Docs](https://geminicli.com/brain/knowledge/docs_legacy/), [Gemini CLI Hooks](https://geminicli.com/brain/knowledge/docs_legacy/hooks/), [Google Developers Blog](https://developers.googleblog.com/)

#### 1. Hooks Support
**Status:** Full Support

- **10 Lifecycle Events**: SessionStart, SessionEnd, BeforeAgent, AfterAgent, BeforeModel, AfterModel, BeforeToolSelection, BeforeTool, AfterTool, PreCompress
- **Hook Types**: Scripts/programs executed at specific points in the agentic loop
- **Configuration**: Defined in settings.json with matcher patterns, timeouts, and commands
- **Security**: Hooks execute with user privileges; fingerprinting alerts for changed commands
- **Management**: `/hooks` command panel, enable/disable individual or all hooks
- **Exit Codes**: 0 (success), 2 (system block), other (warning)
- **JSON Communication**: Strict JSON communication via stdin/stdout for hook responses

#### 2. Extensions/MCP Support
**Status:** Full Support via Model Context Protocol

- **MCP Servers**: Connect to external services using Model Context Protocol
- **Custom Tools**: Expose tools and resources through MCP
- **Prompts as Commands**: MCP servers can expose prompts as slash commands
- **FastMCP Integration**: Seamless integration with FastMCP (Python's leading MCP library) as of FastMCP v2.12.3
- **Official Google MCP**: Enterprise-ready endpoints for Google and Google Cloud services
- **Installation**: `fastmcp install gemini-cli` command
- **Extensions System**: Create custom tools and behaviors

#### 3. Sub-agents Capability
**Status:** Experimental (Preview)

- **Specialized Agents**: Operate within main session for specific tasks
- **Independent Context**: Each sub-agent has own system prompt, persona, and toolset
- **Tool Delegation**: Exposed to main agent as tools for task delegation
- **JSON Schema**: Sub-agents use JSON schema for input
- **AgentRegistry**: Tracked by centralized AgentRegistry
- **A2A Protocol**: Supports Agent-to-Agent protocol for remote sub-agents (experimental)
- **YOLO Mode**: Currently operates without individual confirmation (use with caution)
- **Use Cases**: Deep codebase analysis, documentation lookup, domain-specific reasoning

#### 4. Slash Commands
**Status:** Full Support

Built-in commands include:
- `/version` - Show version info
- `/auth` - Change authentication method
- `/bug` - File issue about Gemini CLI
- `/chat` - Save and resume conversation history
- `/checkpoint` - Save conversation state with tags
- `/export` - Write conversation to Markdown/JSON
- `/copy` - Copy last output to clipboard
- `/docs` - Open documentation in browser
- `/help` - Display help information
- `/hooks` - Show all hooks and status
- `/hooks enable-all` / `/hooks disable-all` - Toggle hooks globally
- `/hooks enable <name>` / `/hooks disable <name>` - Toggle individual hooks
- `/agents refresh` - Update agent configurations
- `/skills reload` - Refresh skill definitions
- `/skills install/uninstall` - Manage Agent Skills
- `/stats` - Show token usage and cached token savings
- `/subagents` - Manage sub-agents

#### 5. Custom Commands (GEMINI.md, TOML config)
**Status:** Full Support

- **GEMINI.md**: Project-specific persistent context files
- **TOML Configuration**: Define custom slash commands in .toml files
- **MCP Prompts**: Custom commands via Model Context Protocol prompts
- **System Prompt Override**: Customize core model instructions
- **Custom Shortcuts**: Create reusable prompts for common workflows
- **Configuration Layers**: Project (.gemini/settings.json), User (~/.gemini/settings.json), System (/etc/gemini-cli/settings.json), Extensions
- **Memory Persistence**: Store facts about projects across sessions

#### 6. IDE Integrations
**Status:** Visual Studio Code Only

- **VS Code Extension**: Gemini CLI Companion (official)
- **Workspace Context**: Auto-awareness of 10 most recent files, cursor position, selected text (16KB limit)
- **Native Diffing**: View code changes in VS Code's native diff viewer
- **Command Palette**: Access Gemini CLI features via VS Code commands
  - "Gemini CLI: Run"
  - "Gemini CLI: Accept Diff"
  - "Gemini CLI: Close Diff Editor"
- **Validated Version**: v0.23.0+ (as of January 8, 2026)
- **Context-Aware Workflows**: Seamless integration with editor state

#### 7. Git Integration Features
**Status:** Full Support

- **Git Operations**: Analyze repository changes, pull requests, complex rebases
- **Git History Analysis**: Intelligent summaries of code evolution
- **Interactive Commands**: Support for interactive git rebase within CLI
- **GitHub Actions**: Beta integration for automated workflows
  - Issue triage and labeling based on content analysis
  - Pull request reviews
  - Automated issue management
  - gh CLI integration for powerful automations
  - Extensible tool-calling capabilities
- **PR Creator Skill**: New skill for creating pull requests (2026)
- **Security Enhancements**: Default folder trust set to untrusted, granular allowlisting for shell commands
- **Commit Management**: Interactive git commands with AI assistance

#### 8. Web Search (Google Search Grounding)
**Status:** Built-in Tool

- **Grounding with Google Search**: Connects Gemini to real-time web content
- **All Languages**: Works with all available languages
- **Automatic Activation**: Model analyzes prompt and assigns prediction score (0-1) to decide if web search would help
- **Query Generation**: Automatically generates one or more search queries when beneficial
- **Result Synthesis**: Model processes search results and formulates response
- **Citation Inclusion**: Responses include grounding metadata with sources, search queries, web results
- **Hallucination Reduction**: ~40% reduction compared to non-grounded responses
- **Increased Factual Accuracy**: Base responses on real-world information
- **Real-time Information**: Access recent events and topics
- **Free Tier**: Included with Google account authentication
- **Paid Tier**: Each search query is billable
- **Configuration**: Can be disabled by adding google_web_search to tools.exclude array in settings.json

#### 9. Sandbox Modes
**Status:** Full Support

- **Isolated Execution**: Execute untrusted code/tools in secure, isolated container
- **Checkpointing**: Save and restore workspace state
- **Headless Mode**: Run in scripts or CI/CD pipelines for automated reasoning
- **Security Isolation**: Protects host system from potentially harmful operations
- **Untrusted Projects**: Safe handling of project-level hooks from untrusted sources

#### 10. Google Cloud Integration
**Status:** Full Support

- **Cloud Monitoring**: Pre-configured dashboards for telemetry and metrics (2026 enhancement)
- **Usage Metrics**: Monthly/daily active users, installs, token consumption
- **Performance Tracking**: Lines of code added/removed, API/tool calls
- **Vertex AI**: Integration with Google Cloud's Vertex AI platform
- **Enterprise Features**: Official MCP endpoints for Google Cloud services
- **Instant Visibility**: High-level visibility into adoption, interaction patterns, and performance
- **Dashboard Metrics**: Immediate access to CLI usage and performance data

#### 11. Cost Tracking (/stats)
**Status:** Full Support

- **Stats Command**: `/stats` displays model usage summary
- **Exit Summary**: Token usage presented on session exit
- **Token Tracking**: Input tokens, output tokens, cached tokens
- **Cached Token Savings**: Shows efficiency gains from token caching
- **Monitoring Dashboards**: Google Cloud Monitoring integration (2026 enhancement)
- **Community Enhancements**: Developers have added spending calculations based on Gemini API pricing
- **Billing Transparency**: Clear visibility into usage costs

#### 12. New Features (Late 2025 - Early 2026)

**Recent Additions:**
- **Gemini 3 Models**: Preview releases (November-December 2025) with improved reasoning and 1M token context
- **FastMCP v2.12.3 Integration**: Seamless MCP server installation (January 2026)
- **Monitoring Dashboards**: Pre-configured Google Cloud dashboards for instant visibility (2026)
- **PR Creator Skill**: Automated pull request creation (2026)
- **Security Hardening**: Default untrusted folders, granular shell command allowlisting (2026)
- **VS Code Enhancements**: Native diffing and context-aware workflows
- **GitHub Actions Beta**: Automated issue triage and PR reviews with generous free quotas
- **Agent Registry**: Centralized tracking for sub-agents
- **A2A Protocol**: Remote sub-agent support (experimental)
- **Hooks Fingerprinting**: Security alerts for modified hook commands
- **Memory Persistence**: Store and recall project-specific facts across sessions
- **Agent Skills**: Add specialized expertise and workflows
- **Theme Customization**: UI theme options
- **Telemetry Controls**: User control over data collection
- **.geminiignore Files**: Exclude files from context
- **Trusted Folders**: Security configuration for project access

#### Summary

Gemini CLI offers a comprehensive feature set with industry-leading 1M token context windows across all current models. Key strengths include:

1. **Extensibility**: Robust hooks system (10 lifecycle events) + full MCP support with FastMCP integration
2. **Agentic Capabilities**: Experimental sub-agents with specialized task delegation and A2A protocol
3. **Developer Experience**: Rich slash commands, custom configurations, VS Code integration, GEMINI.md files
4. **Web Intelligence**: Built-in Google Search grounding reduces hallucinations by ~40%
5. **Enterprise Ready**: Google Cloud integration, monitoring dashboards, cost tracking, security hardening
6. **Git-First**: Native GitHub Actions, interactive git operations, PR automation, issue triage
7. **Multimodal Context**: 1M token window handles text, code, images, and video
8. **Security Focus**: Hooks fingerprinting, default untrusted folders, granular permissions

The CLI is actively developed with significant enhancements in late 2025 and early 2026, particularly around security, monitoring, and agentic workflows. Gemini 2.0 models are being deprecated (March 31, 2026) in favor of Gemini 2.5 and 3.x models with 8x larger output tokens (64K vs 8K).
```

## File: `research/2026-02-09_12-44-16/result.md`
```markdown
# Research Results & Proposed Updates

**Research Date:** 2026-02-09 12:44:16 UTC
**Status:** Complete - Awaiting User Approval

---

## Executive Summary

All 4 research agents completed successfully. Significant updates found across context windows and features for all tools.

| Tool | Context Window Changes | Feature Changes | Priority |
|------|------------------------|-----------------|----------|
| **Claude Code** | ✅ Major (Opus 4.6 released) | ✅ Significant (Agent Teams, Chrome beta) | HIGH |
| **Codex CLI** | ✅ Major (GPT-5.3-Codex default) | ✅ Moderate (GitHub integration preview) | HIGH |
| **Cursor** | ✅ Moderate (Multi-model updates) | ✅ Significant (40x faster hooks, Memories) | MEDIUM |
| **Gemini CLI** | ⚠️ Minor (Gemini 3 Preview) | ✅ Significant (A2A protocol, FastMCP) | MEDIUM |

---

## Proposed Context Window Updates

### New Table for README.md

```markdown
| Tool | Largest Context | Best Model | Input $/M | Output $/M | Source |
|------|-----------------|------------|-----------|------------|--------|
| Claude Code | 1M (beta) | Opus 4.6 with `context-1m-2025-08-07` beta | $5.00 | $25.00 | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
| Codex CLI | 400k | GPT-5.3-Codex (Feb 2026) | TBD* | TBD* | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
| Cursor | 2M (native) | Gemini 3 Pro (200k/1M/2M modes) | $2.00** | $12.00** | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
| Gemini CLI | 1M | Gemini 3 Pro Preview | $2.00 | $12.00 | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |
```

> \* GPT-5.3-Codex pricing not yet published by OpenAI (Feb 2026 release)
> \*\* Cursor uses subscription pricing ($20/mo Pro); API prices shown are for underlying models

### Changes from Current README

**Claude Code:**
- ✅ No change needed - Already shows Opus 4.6 with 1M beta

**Codex CLI:**
- **CHANGED:** Best model updated from "GPT-5.3-Codex (context compaction)" to "GPT-5.3-Codex (Feb 2026)"
- **REASON:** Research confirms GPT-5.3-Codex is now default model (Feb 2026), context compaction is native

**Cursor:**
- **CHANGED:** Best model from "Grok 4" to "Gemini 3 Pro (200k/1M/2M modes)"
- **CHANGED:** Largest context from "2M (Max mode)" to "2M (native)"
- **CHANGED:** Pricing from "$3.00" / "$15.00" to "$2.00" / "$12.00"
- **REASON:** Research shows Gemini 3 Pro has native 2M context, not just Max mode. Grok 4 Code context is 131k-2M (varies by variant), making Gemini 3 Pro the more reliable 2M option

**Gemini CLI:**
- ✅ No change needed - Already accurate

---

## Proposed Feature Comparison Updates

### New Table for README.md

```markdown
| Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
|---------|:-----------:|:---------:|:----------:|:------:|
| **Hooks** | ✅ 9+ types | ⚠️ Limited | ✅ 10 events | ✅ 40x faster |
| **Plugins/MCP** | ✅ Full | ✅ Full | ✅ FastMCP | ✅ Full |
| **Sub-agents** | ✅ Teams (exp) | ✅ Beta | ✅ A2A (exp) | ✅ Custom |
| **Slash Commands** | ✅ Custom | ✅ Custom | ✅ Custom | ✅ Custom |
| **Custom Commands** | ✅ Skills | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
| **IDE Integration** | ✅ VS/JetBrains | ✅ Multi-platform | ✅ VS Code | ✅ Native |
| **Git Integration** | ✅ Hub (beta) | ✅ GitHub (preview) | ✅ Actions (beta) | ✅ Blame (ent) |
| **Web Search** | ✅ US only | ✅ Built-in | ✅ Grounding | ✅ @Web |
| **Image Support** | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
| **Memory/Persistence** | ✅ Session | ✅ Thread | ✅ Project | ✅ Memories |
| **Multi-file Editing** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Composer |
| **Auto-commit** | ⚠️ Via hooks | ⚠️ Manual | ✅ Native | ✅ Native |
| **Custom System Prompts** | ✅ Settings | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
| **Cost Tracking** | ✅ Dashboard | ⚠️ /status | ✅ /stats | ⚠️ Enterprise |
| **Sandbox Mode** | ✅ Native | ✅ OS-enforced | ✅ Container | ✅ Linux (ent) |
```

### Feature Changes from Current README

**Legend:**
- ✅ = Full support
- ⚠️ = Partial/Limited support
- ❌ = Not supported
- (exp) = Experimental
- (ent) = Enterprise only
- (beta) = Beta/preview

**Key Changes:**

1. **Hooks Row:**
   - Claude Code: Changed from "✅" to "✅ 9+ types" (more specific)
   - Codex CLI: No change (still "⚠️ Limited")
   - Gemini CLI: Changed from "✅" to "✅ 10 events" (more specific)
   - Cursor: Changed from "✅" to "✅ 40x faster" (highlights Jan 2026 performance improvement)

2. **Plugins/MCP Row:**
   - Claude Code: Changed from "✅" to "✅ Full"
   - Codex CLI: Changed from "✅" to "✅ Full"
   - Gemini CLI: Changed from "✅" to "✅ FastMCP" (highlights v2.12.3 integration)
   - Cursor: Changed from "✅" to "✅ Full"

3. **Sub-agents Row:**
   - Claude Code: Changed from "✅" to "✅ Teams (exp)" (highlights Agent Teams experimental feature)
   - Codex CLI: Changed from "✅" to "✅ Beta" (more accurate status)
   - Gemini CLI: Changed from "✅" to "✅ A2A (exp)" (highlights Agent-to-Agent protocol)
   - Cursor: Changed from "✅" to "✅ Custom" (highlights .cursor/agents/ custom agents)

4. **Custom Commands Row:**
   - Claude Code: Changed from "✅" to "✅ Skills" (highlights Skills system)
   - Codex CLI: Changed from "✅" to "✅ AGENTS.md" (specific file format)
   - Gemini CLI: Changed from "✅" to "✅ GEMINI.md" (specific file format)
   - Cursor: Changed from "✅" to "✅ Rules" (highlights .cursor/rules/)

5. **IDE Integration Row:**
   - Claude Code: Changed from "✅" to "✅ VS/JetBrains"
   - Codex CLI: Changed from "✅" to "✅ Multi-platform" (supports VS Code, JetBrains, Visual Studio, Xcode, Eclipse, Cursor, Windsurf)
   - Gemini CLI: Changed from "✅" to "✅ VS Code" (only VS Code supported)
   - Cursor: Changed from "✅" to "✅ Native" (it IS the IDE)

6. **Git Integration Row:**
   - Claude Code: Changed from "✅" to "✅ Hub (beta)" (Claude Hub feature)
   - Codex CLI: Changed from "✅" to "✅ GitHub (preview)" (Feb 4, 2026 public preview)
   - Gemini CLI: Changed from "✅" to "✅ Actions (beta)" (GitHub Actions integration)
   - Cursor: Changed from "✅" to "✅ Blame (ent)" (Cursor Blame enterprise feature)

7. **Web Search Row:**
   - Claude Code: Changed from "✅" to "✅ US only"
   - Codex CLI: Changed from "✅" to "✅ Built-in"
   - Gemini CLI: Changed from "✅" to "✅ Grounding" (Google Search grounding)
   - Cursor: Changed from "✅" to "✅ @Web"

8. **Image Support Row:**
   - Claude Code: Changed from "✅" to "✅ Full"
   - Codex CLI: Changed from "✅" to "✅ Full"
   - Gemini CLI: Changed from "✅" to "✅ Full"
   - Cursor: Changed from "⚠️" to "✅ Full" (research shows full image generation support via Google Nano Banana Pro as of Jan 22, 2026)

9. **Memory/Persistence Row:**
   - Claude Code: Changed from "✅" to "✅ Session" (session restore/teleport)
   - Codex CLI: Changed from "✅" to "✅ Thread" (thread memory summaries)
   - Gemini CLI: Changed from "✅" to "✅ Project" (project-specific memory persistence)
   - Cursor: Changed from "⚠️" to "✅ Memories" (Memories feature released Feb 3, 2026)

10. **Multi-file Editing Row:**
    - Claude Code: Changed from "✅" to "✅ Yes"
    - Codex CLI: Changed from "✅" to "✅ Yes"
    - Gemini CLI: Changed from "✅" to "✅ Yes"
    - Cursor: Changed from "✅" to "✅ Composer" (highlights Composer mode)

11. **Cost Tracking Row:**
    - Claude Code: Changed from "✅" to "✅ Dashboard" (Claudia dashboard)
    - Codex CLI: Changed from "❌" to "⚠️ /status" (partial support via /status command)
    - Gemini CLI: Changed from "✅" to "✅ /stats" (highlights /stats command)
    - Cursor: Changed from "⚠️" to "⚠️ Enterprise" (Conversation Insights is enterprise-only)

12. **Sandbox Mode Row:**
    - Claude Code: Changed from "✅" to "✅ Native" (OS-level native sandboxing)
    - Codex CLI: Changed from "✅" to "✅ OS-enforced"
    - Gemini CLI: Changed from "✅" to "✅ Container" (isolated container execution)
    - Cursor: Changed from "⚠️" to "✅ Linux (ent)" (Linux Sandboxing is enterprise feature, Dec 18, 2025)

---

## Detailed Context Window Changes

### Claude Code

**Current State (README):**
- Largest Context: 1M (beta)
- Best Model: Opus 4.6 with `--betas context-1m-2025-08-07`

**Research Findings:**
- ✅ Opus 4.6 released Feb 5, 2026
- ✅ Context: 200K standard / 1M beta via `context-1m-2025-08-07` header
- ✅ Max output: 128K tokens (largest among all 4.x models)
- ✅ Sonnet 4.5: 200K / 1M beta, 64K output
- ✅ Haiku 4.5: 200K, 64K output
- ✅ Context awareness feature for Sonnet 4.5 and Haiku 4.5

**Recommendation:** No changes needed to README context window table.

**Detailed Report Updates Needed:**
- ✅ Add Opus 4.6 to primary models table
- ✅ Update knowledge cutoffs (Opus 4.6: May 2025 reliable / Aug 2025 training)
- ✅ Clarify 1M context availability (tier 4 orgs, pay-as-you-go, NOT subscription users at launch)
- ✅ Add context awareness feature documentation
- ✅ Update model aliases (`opusplan` hybrid mode)

---

### Codex CLI

**Current State (README):**
- Largest Context: 400k+
- Best Model: GPT-5.3-Codex (context compaction)

**Research Findings:**
- ✅ GPT-5.3-Codex: 400K tokens, NEW DEFAULT as of Feb 2026
- ✅ 25% faster than predecessors
- ✅ GPT-5.2-Codex: 400K tokens (stable)
- ✅ codex-mini-latest: 200K tokens (fine-tuned o4-mini)
- ✅ GPT-4.1: 1M tokens (legacy, still available)
- ⚠️ Pricing for GPT-5.3-Codex NOT YET PUBLISHED

**Recommendation:** Minor update to clarify GPT-5.3-Codex is Feb 2026 release.

**Current:**
```
Best Model: GPT-5.3-Codex (context compaction)
```

**Proposed:**
```
Best Model: GPT-5.3-Codex (Feb 2026)
```

**Detailed Report Updates Needed:**
- ✅ Add GPT-5.3-Codex to primary models (Feb 2026 release)
- ✅ Update codex-mini-latest to 200K tokens (not ~200k)
- ✅ Add o3, o4-mini to reasoning models section
- ✅ Update deprecation timeline (o1-preview/o1-mini deprecated April 28, 2025)
- ⚠️ Mark GPT-5.3-Codex pricing as TBD

---

### Cursor

**Current State (README):**
- Largest Context: 2M (Max mode)
- Best Model: Grok 4
- Pricing: $3.00 / $15.00

**Research Findings:**
- ✅ Multi-model support across 5 providers
- ✅ Claude 4.6 Opus: 200k / 1M (2x cost above 200k)
- ✅ GPT-5.3 Codex: 272k (77.3% Terminal-Bench, Feb 5, 2026)
- ✅ Gemini 3 Pro: 200k / 1M / **2M NATIVE** ($2.00/$12.00)
- ✅ Grok 4 Code: 131k-2M (varies by variant, $3.00/$15.00)
- ✅ Composer 1: 200k native, 250 tok/sec (4x faster)

**Recommendation:** Update to Gemini 3 Pro as best model for largest context.

**Current:**
```
| Cursor | 2M (Max mode) | Grok 4 | $3.00** | $15.00** |
```

**Proposed:**
```
| Cursor | 2M (native) | Gemini 3 Pro (200k/1M/2M modes) | $2.00** | $12.00** |
```

**Reasoning:**
- Gemini 3 Pro has NATIVE 2M context support, not just Max mode
- Grok 4 Code context is 131k-2M (varies), less reliable
- Gemini 3 Pro is more cost-effective ($2/$12 vs $3/$15)
- Gemini 3 Pro leads visual reasoning benchmarks

**Detailed Report Updates Needed:**
- ✅ Add Claude 4.6 Opus (Feb 5, 2026)
- ✅ Add GPT-5.3 Codex (Feb 5, 2026, 272k context)
- ✅ Update Gemini 3 Pro to show 2M native context
- ✅ Add Composer 1 details (4x faster, MoE architecture)
- ✅ Add DeepSeek R1/V3 (free tier, US servers)
- ✅ Update pricing transition notes (request-based pricing in late 2025)

---

### Gemini CLI

**Current State (README):**
- Largest Context: 1M
- Best Model: Gemini 3 Pro Preview

**Research Findings:**
- ✅ Gemini 3 Pro Preview: 1M context, 64K output (Nov 2025)
- ✅ Gemini 3 Flash Preview: 1M context, 64K output (Dec 2025)
- ✅ Gemini 2.5 Pro/Flash: 1M context, 64K output (stable)
- ⚠️ Gemini 2.0 Flash DEPRECATED (March 31, 2026)
- ✅ All current models: 1,048,576 tokens exactly
- ✅ 8x output increase (64K vs 8K for 2.0 models)

**Recommendation:** No changes needed to README context window table.

**Detailed Report Updates Needed:**
- ✅ Add Gemini 3 Pro Preview (Nov 2025)
- ✅ Add Gemini 3 Flash Preview (Dec 2025)
- ✅ Update max output tokens (64K for 2.5/3.x models)
- ✅ Add deprecation notice for Gemini 2.0 (March 31, 2026)
- ✅ Clarify exact token counts (1,048,576 not "1M")

---

## Detailed Feature Changes

### Claude Code - New Features (2026)

**Context from Research:**

1. **Agent Teams (Experimental):**
   - Multi-agent collaboration system
   - Requires `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1`
   - Team lead delegates to specialist background agents
   - Token-intensive feature

2. **Hooks System - 9+ Types:**
   - PreToolUse, PostToolUse, PostToolUseFailure
   - Notification, PermissionRequest, UserPromptSubmit
   - Stop, SubagentStop/TaskStopHook, TaskCompleted
   - Bash command hooks and Prompt-based hooks

3. **Chrome Integration (Beta):**
   - Claude in Chrome beta (v2.1.0, Jan 7, 2026)
   - Browser-based interactions

4. **Skills Hot-Reload:**
   - Hot-reloading as of v2.1.0
   - Skills can fetch live data (GitHub CLI integration)

5. **Session Teleportation:**
   - `/teleport` command (v2.1.0)
   - Efficiently restores context from session files

6. **Enhanced IDE Support:**
   - JetBrains Plugin (Beta) - available on marketplace
   - VS Code extension with graphical interface

---

### Codex CLI - New Features (2026)

**Context from Research:**

1. **GitHub Integration (Public Preview):**
   - Released Feb 4, 2026
   - Integration with gh CLI
   - Pull request reviews, issue triage

2. **GPT-5.3-Codex Support (Feb 2026):**
   - Mid-turn steering capabilities
   - 25% faster than predecessors
   - State-of-the-art performance with fewer tokens

3. **Steer Mode (Jan 2026):**
   - Now stable and default
   - Enter sends immediately, Tab queues follow-up

4. **Multi-platform IDE Support:**
   - VS Code, JetBrains (v2025.3+), Cursor, Windsurf
   - Visual Studio, Xcode, Eclipse (GPT-5.2-Codex, Jan 26, 2026)

5. **Hooks - Limited Support:**
   - Notification hooks only
   - Full hooks system under discussion (GitHub Issue #2150)

6. **Cost Tracking - Partial:**
   - `/status` shows token usage
   - No comprehensive built-in analytics
   - Third-party: `ccusage` package available

---

### Cursor - New Features (2026)

**Context from Research:**

1. **40x Faster Hooks (Jan 2026):**
   - Major performance improvement
   - Full lifecycle control via custom scripts
   - 20+ hook events

2. **Sub-agents (Jan 22, 2026):**
   - Built-in: Explore, Bash, Browser
   - Custom agents: `.cursor/agents/`
   - Foreground (blocking) / Background (async)

3. **Memories (Feb 3, 2026):**
   - AI remembers conversation facts
   - Background agent workflow adaptation
   - Persistent context across sessions

4. **Image Generation (Jan 22, 2026):**
   - Google Nano Banana Pro integration
   - Full image generation support

5. **Enterprise Features (Dec 2025 - Jan 2026):**
   - Conversation Insights (Dec 18, 2025)
   - Transcript Sharing (Dec 18, 2025)
   - Billing Groups (Dec 18, 2025)
   - Linux Sandboxing (Dec 18, 2025)
   - Service Accounts (Dec 18, 2025)
   - Cursor Blame (Jan 22, 2026) - AI attribution

6. **Skills System (Jan 22, 2026):**
   - `SKILL.md` files for dynamic context discovery
   - `/rules` command (Jan 8, 2026)
   - Migration from `.cursorrules` to `.cursor/rules/*.mdc`

---

### Gemini CLI - New Features (2026)

**Context from Research:**

1. **FastMCP Integration (v2.12.3, Jan 2026):**
   - Seamless installation: `fastmcp install gemini-cli`
   - Python's leading MCP library
   - Official Google MCP endpoints

2. **A2A Protocol (Experimental):**
   - Agent-to-Agent protocol for remote sub-agents
   - AgentRegistry for centralized tracking
   - YOLO mode (use with caution)

3. **10 Lifecycle Hooks:**
   - SessionStart/End, BeforeAgent/AfterAgent
   - BeforeModel/AfterModel, BeforeToolSelection
   - BeforeTool/AfterTool, PreCompress
   - Security: fingerprinting alerts for changed commands

4. **Google Search Grounding:**
   - ~40% reduction in hallucinations
   - Automatic activation based on prediction score
   - Citation inclusion with sources
   - Free tier included with Google account

5. **GitHub Actions (Beta):**
   - Automated issue triage and labeling
   - Pull request reviews
   - gh CLI integration
   - Generous free quotas

6. **Google Cloud Monitoring (2026):**
   - Pre-configured dashboards for telemetry
   - Monthly/daily active users tracking
   - Token consumption monitoring
   - Instant visibility into adoption patterns

7. **Security Hardening (2026):**
   - Default untrusted folders
   - Granular shell command allowlisting
   - Hooks fingerprinting alerts

---

## README.md Diffs

### Context Window Table Diff

```diff
 | Tool | Largest Context | Best Model | Input $/M | Output $/M | Source |
 |------|-----------------|------------|-----------|------------|--------|
-| Claude Code | 1M (beta) | Opus 4.6 with `--betas context-1m-2025-08-07` | $5.00 | $25.00 | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
-| Codex CLI | 400k+ | GPT-5.3-Codex (context compaction) | TBD* | TBD* | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
-| Cursor | 2M (Max mode) | Grok 4 | $3.00** | $15.00** | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
-| Gemini CLI | 1M | Gemini 3 Pro Preview | $2.00 | $12.00 | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |
+| Claude Code | 1M (beta) | Opus 4.6 with `context-1m-2025-08-07` beta | $5.00 | $25.00 | [Anthropic Models](https://docs.anthropic.com/en/brain/knowledge/docs_legacy/about-claude/models) |
+| Codex CLI | 400k | GPT-5.3-Codex (Feb 2026) | TBD* | TBD* | [OpenAI Models](https://platform.openai.com/brain/knowledge/docs_legacy/models) |
+| Cursor | 2M (native) | Gemini 3 Pro (200k/1M/2M modes) | $2.00** | $12.00** | [Cursor Models](https://cursor.com/brain/knowledge/docs_legacy/models) |
+| Gemini CLI | 1M | Gemini 3 Pro Preview | $2.00 | $12.00 | [Gemini API](https://ai.google.dev/gemini-api/brain/knowledge/docs_legacy/models) |

-> \* GPT-5.3-Codex pricing not yet published by OpenAI (predecessor GPT-5.2-Codex: $1.75/$14.00)
+> \* GPT-5.3-Codex pricing not yet published by OpenAI (Feb 2026 release)
 > \*\* Cursor uses subscription pricing ($20/mo Pro); API prices shown are for the underlying Grok 4 model via xAI
```

### Feature Comparison Table Diff

```diff
 | Feature | Claude Code | Codex CLI | Gemini CLI | Cursor |
 |---------|:-----------:|:---------:|:----------:|:------:|
-| **Hooks** | ✅ | ⚠️ | ✅ | ✅ |
-| **Plugins/MCP** | ✅ | ✅ | ✅ | ✅ |
-| **Sub-agents** | ✅ | ✅ | ✅ | ✅ |
+| **Hooks** | ✅ 9+ types | ⚠️ Limited | ✅ 10 events | ✅ 40x faster |
+| **Plugins/MCP** | ✅ Full | ✅ Full | ✅ FastMCP | ✅ Full |
+| **Sub-agents** | ✅ Teams (exp) | ✅ Beta | ✅ A2A (exp) | ✅ Custom |
 | **Slash Commands** | ✅ | ✅ | ✅ | ✅ |
-| **Custom Commands** | ✅ | ✅ | ✅ | ✅ |
-| **IDE Integration** | ✅ | ✅ | ✅ | ✅ |
-| **Git Integration** | ✅ | ✅ | ✅ | ✅ |
-| **Web Search** | ✅ | ✅ | ✅ | ✅ |
-| **Image Support** | ✅ | ✅ | ✅ | ⚠️ |
-| **Memory/Persistence** | ✅ | ✅ | ✅ | ⚠️ |
-| **Multi-file Editing** | ✅ | ✅ | ✅ | ✅ |
-| **Auto-commit** | ⚠️ | ⚠️ | ✅ | ✅ |
-| **Custom System Prompts** | ✅ | ✅ | ✅ | ✅ |
-| **Cost Tracking** | ✅ | ❌ | ✅ | ⚠️ |
-| **Sandbox Mode** | ✅ | ✅ | ✅ | ⚠️ |
+| **Custom Commands** | ✅ Skills | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
+| **IDE Integration** | ✅ VS/JetBrains | ✅ Multi-platform | ✅ VS Code | ✅ Native |
+| **Git Integration** | ✅ Hub (beta) | ✅ GitHub (preview) | ✅ Actions (beta) | ✅ Blame (ent) |
+| **Web Search** | ✅ US only | ✅ Built-in | ✅ Grounding | ✅ @Web |
+| **Image Support** | ✅ Full | ✅ Full | ✅ Full | ✅ Full |
+| **Memory/Persistence** | ✅ Session | ✅ Thread | ✅ Project | ✅ Memories |
+| **Multi-file Editing** | ✅ Yes | ✅ Yes | ✅ Yes | ✅ Composer |
+| **Auto-commit** | ⚠️ Via hooks | ⚠️ Manual | ✅ Native | ✅ Native |
+| **Custom System Prompts** | ✅ Settings | ✅ AGENTS.md | ✅ GEMINI.md | ✅ Rules |
+| **Cost Tracking** | ✅ Dashboard | ⚠️ /status | ✅ /stats | ⚠️ Enterprise |
+| **Sandbox Mode** | ✅ Native | ✅ OS-enforced | ✅ Container | ✅ Linux (ent) |
```

---

## reports/context-comparison.md Changes Needed

### Claude Code Section

**Add to Primary Models Table:**
```markdown
| Opus 4.6 | 200k (1M beta) | 128k | $5.00 | $25.00 | Latest model (Feb 5, 2026), adaptive thinking, first Opus with 1M context |
```

**Update Knowledge Cutoffs:**
```markdown
- Opus 4.6: May 2025 (reliable) / Aug 2025 (training data)
- Sonnet 4.5: Jan 2025 (reliable) / Jul 2025 (training data)
- Haiku 4.5: Feb 2025 (reliable) / Jul 2025 (training data)
```

**Add Context Awareness Feature:**
```markdown
- **Context awareness**: Sonnet 4.5 and Haiku 4.5 track remaining context window throughout conversation
- System provides token usage warnings: `Token usage: 35000/200000; 165000 remaining`
```

**Clarify 1M Context Availability:**
```markdown
- 1M context available for Opus 4.6 API and Claude Code pay-as-you-go users
- Pro, Max, Teams, and Enterprise subscription users do NOT have access to Opus 4.6 1M context at launch
- Available via `context-1m-2025-08-07` beta header
- Premium pricing: 2x input, 1.5x output for requests exceeding 200K tokens
```

---

### Codex CLI Section

**Update Primary Models Table:**
```markdown
| Model | Context Window | Max Output | Input $/M | Output $/M | Notes |
|-------|----------------|------------|-----------|------------|-------|
| gpt-5.3-codex | 400,000 tokens | - | TBD | TBD | Latest (Feb 2026), 25% faster, new default |
| gpt-5.2-codex | 400,000 tokens | - | $1.75 | $14.00 | Stable |
| gpt-5.1-codex-mini | 400,000 tokens | 128,000 tokens | - | - | Cost-effective version |
```

**Add Reasoning Models:**
```markdown
| o3 | 200,000 tokens | - | Latest | New reasoning model for complex tasks |
| o4-mini | 200,000 tokens | - | Latest | Fast, cost-efficient reasoning |
| codex-mini-latest | 200,000 tokens | 100,000 tokens | Stable | Fine-tuned o4-mini for Codex CLI |
```

**Update Legacy Models:**
```markdown
| GPT-4.1 | 1,000,000 tokens | - | Stable | Up to 1M token context |
```

**Update Deprecation Timeline:**
```markdown
- **o1-preview, o1-mini**: Deprecated April 28, 2025
- **chatgpt-4o-latest**: Deprecated Nov 18, 2025; API removal Feb 17, 2026
- **GPT-4o, GPT-4.1, GPT-4.1 mini, o4-mini**: Retired from ChatGPT Feb 13, 2026 (API access continues)
```

---

### Cursor Section

**Add Claude Models:**
```markdown
| Claude 4.6 Opus | 200k (1M max) | 64k | $5.00 | $25.00 | Latest (Feb 5, 2026), deep reasoning |
```

**Add OpenAI Models:**
```markdown
| GPT-5.3 Codex | 272k | - | - | - | Latest (Feb 5, 2026), 77.3% Terminal-Bench |
```

**Update Gemini Models:**
```markdown
| Model | Context Window | Max Mode | Native | Notes |
|-------|---------------|----------|--------|-------|
| Gemini 3 Pro | 200k | 1M | 2M | Visual reasoning leader |
```

**Update Grok Models:**
```markdown
| Grok 4 Code | 131k-2M | Varies by variant, multimodal |
```

**Add Composer Details:**
```markdown
| Composer 1 | 200k | 250 tok/sec (4x faster) | $1.25/M in, $10/M out |
- MoE architecture, RL-trained on real engineering tasks
- Completes most turns in <30 seconds
```

**Add DeepSeek Models:**
```markdown
| DeepSeek R1 | Standard | Free tier, US servers (Fireworks.ai) |
| DeepSeek V3 | Standard | Free tier, US servers |
```

---

### Gemini CLI Section

**Update Current Models:**
```markdown
| Gemini 3 Pro Preview | 1,048,576 (1M) | 65,536 (64K) | Preview | Released November 2025 |
| Gemini 3 Flash Preview | 1,048,576 (1M) | 65,536 (64K) | Preview | Released December 2025 |
| Gemini 2.5 Pro | 1,048,576 (1M) | 65,536 (64K) | Stable | Released June 2025 |
| Gemini 2.5 Flash | 1,048,576 (1M) | 65,536 (64K) | Stable | Released June 2025 |
```

**Add Deprecation Notice:**
```markdown
| Gemini 2.0 Flash | 1,048,576 (1M) | 8,192 (8K) | March 31, 2026 |
| Gemini 2.0 Flash-Lite | 1,048,576 (1M) | 8,192 (8K) | March 31, 2026 |
```

**Highlight Output Token Increase:**
```markdown
- **Enhanced Output**: Gemini 2.5 and 3.x models significantly increased max output from 8K to 64K tokens (8x improvement)
```

---

## Next Steps

**User Approval Required:**

1. Review proposed changes to README.md context window table
2. Review proposed changes to README.md feature comparison table
3. Review proposed changes to reports/context-comparison.md
4. Approve updates or request modifications

**After Approval:**

1. Update README.md with new tables
2. Update reports/context-comparison.md with detailed model information
3. Update "Last Updated" timestamp to 2026-02-09
4. Commit changes with summary message

---

## Change Summary

**Total Changes:** 4 tools updated

**High Priority:**
- Claude Code: Opus 4.6 released (Feb 5, 2026) with 1M context and 128K output
- Codex CLI: GPT-5.3-Codex now default model (Feb 2026)
- Cursor: Multi-model updates, 40x faster hooks, Memories feature

**Medium Priority:**
- Gemini CLI: Gemini 3 models in preview, FastMCP integration, A2A protocol

**Feature Highlights:**
- Claude Code: Agent Teams (experimental), Chrome beta, Skills hot-reload
- Codex CLI: GitHub integration preview (Feb 4, 2026), multi-platform IDE support
- Cursor: 40x faster hooks (Jan 2026), Memories (Feb 3, 2026), Image generation
- Gemini CLI: 10 lifecycle hooks, FastMCP v2.12.3, Google Search grounding

**Deprecations:**
- Gemini 2.0 Flash models shutdown March 31, 2026
- Codex CLI: o1-preview/o1-mini deprecated April 28, 2025

---

**Ready for User Review and Approval**
```

