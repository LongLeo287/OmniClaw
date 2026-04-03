---
id: recursive-decomposition-skill-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:08.209738
---

# KNOWLEDGE EXTRACT: recursive-decomposition-skill
> **Extracted on:** 2026-03-30 13:17:05
> **Source:** recursive-decomposition-skill

---

## File: `AGENTS.md`
```markdown
# Recursive Decomposition Skills Repository

This repository contains Claude Code plugins for handling long-context tasks through recursive decomposition strategies. It serves as a marketplace for distributing these skills.

## Repository Structure

```
.claude-plugin/
  marketplace.json          # Marketplace catalog - lists all plugins
plugins/
  recursive-decomposition/  # Plugin for recursive decomposition strategies
    .claude-plugin/
      plugin.json           # Plugin manifest
    skills/
      recursive-decomposition/
        SKILL.md            # Main skill file
        references/         # Supporting documentation
        examples/           # Walkthrough examples
    README.md
```

## Creating Claude Code Plugins

### Plugin Directory Structure

Each plugin follows this structure:

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json         # Required: Plugin manifest (only file in this dir)
├── skills/                 # Skill directories
│   └── skill-name/
│       ├── SKILL.md        # Required: Main skill file
│       ├── references/     # Optional: Supporting docs
│       └── scripts/        # Optional: Utility scripts
└── README.md               # Optional: Plugin documentation
```

### Plugin Manifest (`plugin.json`)

```json
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "Brief description of the plugin",
  "author": {
    "name": "Your Name",
    "email": "you@example.com"
  }
}
```

Required fields:
- `name`: Unique identifier in kebab-case

Optional fields:
- `version`: Semantic versioning (e.g., `"1.0.0"`)
- `description`: Brief explanation shown in plugin manager
- `author`: Object with `name` and optionally `email`

### Skill Files (`SKILL.md`)

Skills teach Claude how to perform specific tasks. Each skill has a `SKILL.md` file with YAML frontmatter:

```markdown
---
name: skill-name
description: What the skill does and when to use it. Claude uses this for auto-discovery.
---

# Skill Title

Skill content goes here...
```

**Frontmatter fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Skill identifier (lowercase, hyphens, max 64 chars) |
| `description` | Yes | When to use this skill (max 1024 chars) - crucial for auto-discovery |
| `allowed-tools` | No | Tools Claude can use without permission (e.g., `"Read, Grep, Bash(node:*)"`) |
| `version` | No | Skill version |
| `license` | No | License identifier |

**Best practices:**
- Keep `SKILL.md` under 500 lines
- Use `references/` subdirectory for detailed documentation
- Write descriptions that match what users naturally say
- Include keywords users would search for

### Supporting Files

Skills can include supporting files:

```
skills/my-skill/
├── SKILL.md                 # Main skill (required)
├── references/              # Detailed documentation
│   ├── setup.md
│   └── examples.md
└── scripts/                 # Utility scripts
    ├── fetch.js
    └── validate.js
```

Reference these in your SKILL.md:
```markdown
## References

Consult these resources as needed:
- ./references/setup.md -- Setup and configuration guide
- ./references/examples.md -- Usage examples
```

## Marketplace Configuration

The `.claude-plugin/marketplace.json` file catalogs all plugins:

```json
{
  "name": "marketplace-name",
  "owner": {
    "name": "Owner Name",
    "email": "owner@example.com"
  },
  "metadata": {
    "description": "Marketplace description"
  },
  "plugins": [
    {
      "name": "plugin-name",
      "source": "./plugins/plugin-name",
      "description": "What the plugin does."
    }
  ]
}
```

**Plugin entry fields:**
- `name` (required): Plugin identifier in kebab-case
- `source` (required): Relative path to plugin directory
- `description`: Brief description for the plugin list

## Adding a New Plugin

1. Create the plugin directory structure:
   ```bash
   mkdir -p plugins/my-plugin/.claude-plugin
   mkdir -p plugins/my-plugin/skills/my-skill
   ```

2. Create `plugins/my-plugin/.claude-plugin/plugin.json`:
   ```json
   {
     "name": "my-plugin",
     "version": "1.0.0",
     "description": "What the plugin does",
     "author": {
       "name": "Your Name",
       "email": "you@example.com"
     }
   }
   ```

3. Create `plugins/my-plugin/skills/my-skill/SKILL.md`:
   ```markdown
   ---
   name: my-skill
   description: When to use this skill and what it does.
   ---

   # My Skill

   Content...
   ```

4. Create `plugins/my-plugin/README.md`:
   ```markdown
   # My Plugin

   Brief description.

   ## License

   MIT
   ```

5. Add to `.claude-plugin/marketplace.json`:
   ```json
   {
     "name": "my-plugin",
     "source": "./plugins/my-plugin",
     "description": "What the plugin does."
   }
   ```

6. Add to `README.md` installation examples:
   ```
   /plugin install my-plugin
   ```

## Testing Plugins

Test plugins locally before publishing:

```bash
# Load plugin for testing
claude --plugin-dir ./plugins/recursive-decomposition

# Validate plugin structure
claude plugin validate ./plugins/recursive-decomposition
```

## User Installation

Users install plugins from this marketplace:

```bash
# Add the marketplace
/plugin marketplace add recursive-decomposition-skill

# Install a plugin
/plugin install recursive-decomposition
```

## Conventions in This Repo

- **Plugin names**: Use kebab-case (e.g., `recursive-decomposition`)
- **Skill names**: Use kebab-case (e.g., `recursive-decomposition`)
- **File names**: Use kebab-case for all files
- **License**: MIT for all plugins
- **README.md**: Include in each plugin with brief description and license
```

## File: `CLAUDE.md`
```markdown
AGENTS.md
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Recursive Decomposition Skills

We welcome contributions! This implementation of recursive decomposition strategies for Claude Code is open for improvements.

## Development Workflow

1.  **Fork & Clone**: Start by forking the repository.
2.  **Plugin Structure**: Understanding the `plugins/` directory layout.
3.  **Creating Skills**: Guidelines for writing `SKILL.md` files (clear triggers, concise instructions).

## Testing Changes

Before submitting, you **must** test your changes locally:

```bash
# Load the plugin from your local directory
claude --plugin-dir ./plugins/recursive-decomposition
```

- Verify that the skill triggers when appropriate (e.g., "analyze these 20 files").
- Verify that the decomposition strategy works as expected.

## Submission Guidelines

- **One Skill Per Pull Request**: Keep PRs focused.
- **Documentation**: Ensure `SKILL.md` frontmatter is correct.
- **Examples**: Provide a walkthrough in `examples/` if adding a complex new strategy.

## Code of Conduct

Be respectful and constructive.
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 MDL

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
<p align="center">
  <img src="assets/logo.png" alt="Recursive Decomposition Skill" width="200">
</p>

<h1 align="center">Recursive Decomposition Skill</h1>

<p align="center">
  <strong>Handle long-context tasks with Claude Code through recursive decomposition</strong>
</p>

<p align="center">
  <a href="#installation"><img src="https://img.shields.io/badge/Claude_Code-Plugin-blueviolet?style=flat-square" alt="Claude Code Plugin"></a>
  <a href="https://arxiv.org/abs/2512.24601"><img src="https://img.shields.io/badge/arXiv-2512.24601-b31b1b?style=flat-square" alt="arXiv Paper"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-green?style=flat-square" alt="MIT License"></a>
  <a href="https://agentskills.io"><img src="https://img.shields.io/badge/Format-Agent_Skills-orange?style=flat-square" alt="Agent Skills Format"></a>
</p>

<p align="center">
  <a href="#what-it-does">What It Does</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#how-it-works">How It Works</a> •
  <a href="#benchmarks">Benchmarks</a> •
  <a href="#acknowledgments">Acknowledgments</a>
</p>

---

## The Problem

When analyzing large codebases, processing many documents, or aggregating information across dozens of files, Claude's context window becomes a bottleneck. As context grows, **"context rot"** degrades performance:

- Missed details in long documents
- Decreased accuracy on information retrieval
- Hallucinated connections between distant content
- Degraded reasoning over large evidence sets

## The Solution

This skill implements **Recursive Language Model (RLM)** strategies from [Zhang, Kraska, and Khattab's 2025 research](https://arxiv.org/abs/2512.24601), enabling Claude Code to handle inputs **up to 2 orders of magnitude beyond normal context limits**.

Instead of cramming everything into context, Claude learns to:

1. **Filter** — Narrow search space before deep analysis
2. **Chunk** — Partition inputs strategically
3. **Recurse** — Spawn sub-agents for independent segments
4. **Verify** — Re-check answers on smaller, focused windows
5. **Synthesize** — Aggregate results programmatically

---

## What It Does

| Task Type | Without Skill | With Skill |
|-----------|---------------|------------|
| Analyze 100+ files | Context overflow / degraded results | Systematic coverage via decomposition |
| Multi-document QA | Missed information | Comprehensive extraction |
| Codebase-wide search | Manual iteration | Parallel sub-agent analysis |
| Information aggregation | Incomplete synthesis | Map-reduce pattern |

### Real Test Results

We tested on the [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook) (196 files, 356MB):

```
Task: "Find all Anthropic API calling patterns across the codebase"

Results:
├── Files scanned: 142
├── Files with API calls: 18
├── Patterns identified: 8 distinct patterns
├── Anti-patterns detected: 4
└── Output: Comprehensive report with file:line references
```

---

## Installation

### Via Claude Code Marketplace

```bash
# Add the marketplace
claude plugin marketplace add massimodeluisa/recursive-decomposition-skill

# Install the plugin
claude plugin install recursive-decomposition@recursive-decomposition
```

### From Local Clone

```bash
# Clone the repository
git clone https://github.com/massimodeluisa/recursive-decomposition-skill.git ~/recursive-decomposition-skill

# Add as local marketplace
claude plugin marketplace add ~/recursive-decomposition-skill

# Install the plugin
claude plugin install recursive-decomposition
```

### Manual Installation (Skills Directory)

```bash
# Copy skill directly to Claude's skills directory
cp -r plugins/recursive-decomposition/skills/recursive-decomposition ~/.claude/skills/
```

After installation, **restart Claude Code** for the skill to take effect.

### Updating

```bash
# Update marketplace index
claude plugin marketplace update

# Update the plugin
claude plugin update recursive-decomposition@recursive-decomposition
```

---

## Usage

The skill activates automatically when you describe tasks involving:

- Large-scale file analysis (`"analyze all files in..."`)
- Multi-document processing (`"aggregate information from..."`)
- Codebase-wide searches (`"find all occurrences across..."`)
- Long-context reasoning (`"summarize these 50 documents..."`)

### Example Prompts

```
"Analyze error handling patterns across this entire codebase"

"Find all TODO comments in the project and categorize by priority"

"What API endpoints are defined across all route files?"

"Summarize the key decisions from all meeting notes in /docs"

"Find security vulnerabilities across all Python files"
```

### Trigger Phrases

The skill recognizes these patterns:
- `"analyze all files"`
- `"process this large document"`
- `"aggregate information from"`
- `"search across the codebase"`
- Tasks involving 10+ files or 50k+ tokens

---

## When to Use

The skill is designed for **complex, long-context tasks**. Use it when:

- Analyzing 10+ files simultaneously
- Processing documents exceeding 50k tokens
- Performing codebase-wide pattern analysis
- Extracting information from multiple scattered sources
- Multi-hop reasoning requiring evidence synthesis

**When NOT to use:**

- Single file edits → Direct processing is faster
- Specific function lookup → Use Grep directly
- Tasks < 30k tokens → Overhead not worth it
- Time-critical operations → Latency matters more than completeness

---

## How It Works

### Decomposition Strategies

#### 1. Filter Before Deep Analysis
```
1000 files → Glob filter → 100 files
100 files  → Grep filter → 20 files
20 files   → Deep analysis
```
**Result:** 50x reduction before expensive processing

#### 2. Strategic Chunking
- **Uniform:** Split by line count or natural boundaries
- **Semantic:** Partition by logical units (functions, classes)
- **Keyword-based:** Group by shared characteristics

#### 3. Parallel Sub-Agents
```
Main Agent
├── Sub-Agent 1 (Batch A) ─┐
├── Sub-Agent 2 (Batch B) ─┼── Parallel
├── Sub-Agent 3 (Batch C) ─┘
└── Synthesize results
```

#### 4. Verification Pass
Re-check synthesized answers against focused evidence to catch context rot errors.

---

## Benchmarks

From the [RLM paper](https://arxiv.org/abs/2512.24601):

| Task | Direct Model | With RLM | Improvement |
|------|--------------|----------|-------------|
| Multi-hop QA (6-11M tokens) | 70% | 91% | **+21%** |
| Linear aggregation | Baseline | +28-33% | **Significant** |
| Quadratic reasoning | <0.1% | 58% | **Massive** |
| Context scaling | 2^14 tokens | 2^18 tokens | **16x** |

**Cost:** RLM approaches are ~3x cheaper than summarization baselines while achieving superior quality.

---

## Repository Structure

```
recursive-decomposition-skill/
├── .claude-plugin/
│   └── marketplace.json          # Marketplace manifest
├── plugins/
│   └── recursive-decomposition/
│       ├── .claude-plugin/
│       │   └── plugin.json       # Plugin manifest
│       ├── README.md             # Plugin documentation
│       └── skills/
│           └── recursive-decomposition/
│               ├── SKILL.md      # Core skill instructions
│               └── references/
│                   ├── rlm-strategies.md
│                   ├── cost-analysis.md
│                   ├── codebase-analysis.md
│                   └── document-aggregation.md
├── assets/
│   └── logo.png                  # Project logo
├── AGENTS.md                     # Agent-facing docs
├── CONTRIBUTING.md               # Contribution guidelines
├── LICENSE
└── README.md
```

---

## Skill Contents

| File | Purpose |
|------|---------|
| [`SKILL.md`](plugins/recursive-decomposition/skills/recursive-decomposition/SKILL.md) | Core decomposition strategies and patterns |
| [`references/rlm-strategies.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/rlm-strategies.md) | Detailed techniques from the RLM paper |
| [`references/cost-analysis.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/cost-analysis.md) | When to use recursive vs. direct approaches |
| [`references/codebase-analysis.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/codebase-analysis.md) | Full walkthrough: multi-file error handling analysis |
| [`references/document-aggregation.md`](plugins/recursive-decomposition/skills/recursive-decomposition/references/document-aggregation.md) | Full walkthrough: multi-document feature extraction |

---

## Acknowledgments

This skill is based on the **Recursive Language Models** research paper. Huge thanks to the authors for their groundbreaking work:

<table>
  <tr>
    <td align="center">
      <a href="https://x.com/a1zhang">
        <b>Alex L. Zhang</b>
      </a>
      <br>
      <a href="https://x.com/a1zhang">@a1zhang</a>
      <br>
      <sub>MIT CSAIL</sub>
    </td>
    <td align="center">
      <a href="https://x.com/tim_kraska">
        <b>Tim Kraska</b>
      </a>
      <br>
      <a href="https://x.com/tim_kraska">@tim_kraska</a>
      <br>
      <sub>MIT Professor</sub>
    </td>
    <td align="center">
      <a href="https://x.com/lateinteraction">
        <b>Omar Khattab</b>
      </a>
      <br>
      <a href="https://x.com/lateinteraction">@lateinteraction</a>
      <br>
      <sub>MIT CSAIL, Creator of DSPy</sub>
    </td>
  </tr>
</table>

### Paper

> **Recursive Language Models**
>
> *Alex L. Zhang, Tim Kraska, Omar Khattab*
>
> arXiv:2512.24601 • December 2025
>
> We propose Recursive Language Models (RLMs), an inference technique enabling LLMs to handle prompts up to two orders of magnitude beyond model context windows through programmatic decomposition and recursive self-invocation over prompt segments.

<p>
  <a href="https://arxiv.org/abs/2512.24601"><img src="https://img.shields.io/badge/arXiv-2512.24601-b31b1b?style=for-the-badge" alt="arXiv Paper"></a>
  <a href="https://arxiv.org/pdf/2512.24601"><img src="https://img.shields.io/badge/PDF-Download-blue?style=for-the-badge" alt="PDF Download"></a>
</p>

---

## References

- [Agent Skills Specification](https://agentskills.io/specification)
- [Claude Code Documentation](https://docs.anthropic.com/claude-code)

---

## Contributing

Contributions welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## Author

<p>
  <a href="https://x.com/massimodeluisa">
    <img src="https://img.shields.io/badge/X-@massimodeluisa-000000?style=flat-square&logo=x" alt="X (Twitter)">
  </a>
  <a href="https://github.com/massimodeluisa">
    <img src="https://img.shields.io/badge/GitHub-massimodeluisa-181717?style=flat-square&logo=github" alt="GitHub">
  </a>
</p>

**Massimo De Luisa** — [@massimodeluisa](https://x.com/massimodeluisa)

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---
```

## File: `plugins/recursive-decomposition/README.md`
```markdown
# Recursive Decomposition Plugin

A Claude Code plugin for handling long-context tasks through recursive decomposition strategies based on [Recursive Language Models (RLM) research](https://arxiv.org/abs/2512.24601) by Zhang, Kraska, and Khattab (2025).

## What This Plugin Does

This plugin enables Claude to handle tasks that exceed comfortable context limits (typically 30k+ tokens or 10+ files) by:

- **Filtering before deep analysis** - Narrowing search space systematically
- **Strategic chunking** - Partitioning inputs for parallel processing
- **Recursive sub-agents** - Spawning independent analysis tasks
- **Answer verification** - Re-checking synthesized results on focused windows
- **Programmatic synthesis** - Aggregating results without context overflow

**Real-world impact:** Handles inputs up to 2 orders of magnitude beyond normal context limits, with benchmarks showing 21-58% accuracy improvements on long-context tasks.

## When to Use

The skill automatically activates when Claude detects:

- Tasks involving 10+ files or 50k+ tokens
- Phrases like "analyze all files", "process this large document", "aggregate information from", "search across the codebase"
- Codebase-wide pattern analysis
- Multi-document information extraction
- Multi-hop questions requiring scattered evidence

## Skills Included

- **recursive-decomposition** - Core strategies for programmatic decomposition, chunking, filtering, and recursive self-invocation

## Installation

### From Marketplace

```bash
# Add this marketplace
/plugin marketplace add massimodeluisa/recursive-decomposition-skill

# Install the plugin
/plugin install recursive-decomposition
```

### Manual Installation

Copy this plugin directory to your Claude Code plugins directory:

```bash
cp -r plugins/recursive-decomposition ~/.claude/plugins/
```

## Usage Examples

```
"Find all error handling patterns across the entire codebase"
"Summarize all TODO comments and categorize by priority"
"What API endpoints are defined across all route files?"
"Analyze security vulnerabilities in all Python files"
```

The plugin handles the decomposition automatically - no special syntax required.

## Plugin Structure

```
recursive-decomposition/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
└── skills/
    └── recursive-decomposition/
        ├── SKILL.md             # Core decomposition strategies
        └── references/
            ├── rlm-strategies.md
            ├── cost-analysis.md
            ├── codebase-analysis.md
            └── document-aggregation.md
```

## Research Foundation

Based on "Recursive Language Models" (Zhang, Kraska, Khattab, 2025):
- arXiv: [2512.24601](https://arxiv.org/abs/2512.24601)
- Enables context scaling from 2^14 to 2^18 tokens (16x)
- ~3x more cost-effective than summarization baselines

## License

MIT - See [LICENSE](../../LICENSE)

## Author

Massimo De Luisa ([@massimodeluisa](https://x.com/massimodeluisa))
```

## File: `plugins/recursive-decomposition/skills/recursive-decomposition/SKILL.md`
```markdown
---
name: recursive-decomposition
description: Based on the Recursive Language Models (RLM) research by Zhang, Kraska, and Khattab (2025), this skill provides strategies for handling tasks that exceed comfortable context limits through programmatic decomposition and recursive self-invocation. Triggers on phrases like "analyze all files", "process this large document", "aggregate information from", "search across the codebase", or tasks involving 10+ files or 50k+ tokens.
---

# Recursive Decomposition Guidelines

## References

Consult these resources as needed:

- ./references/rlm-strategies.md -- Detailed decomposition patterns from the RLM paper
- ./references/cost-analysis.md -- When to apply recursive vs. direct approaches
- ./references/codebase-analysis.md -- Full walkthrough of codebase-wide analysis
- ./references/document-aggregation.md -- Multi-document information extraction

## Core Principles

**CRITICAL: Treat inputs as environmental variables, not immediate context.**

Most tasks fail when context is overloaded. Instead of loading entire contexts into the processing window, treat inputs as **environmental variables** accessible through code execution. Decompose problems recursively, process segments independently, and aggregate results programmatically.

**Progressive Disclosure**: Load information only when necessary. Start high-level to map the territory, then dive deep into specific areas.

### When Recursive Decomposition is Required

-   Tasks involving 10+ files
-   Input exceeding ~50k tokens where single-prompt context is insufficient
-   Multi-hop questions requiring evidence from multiple scattered sources
-   Codebase-wide pattern analysis or migration planning

### When Direct Processing Works

-   Small contexts (<30k tokens)
-   Single file analysis
-   Linear complexity tasks with manageable inputs

## Operational Rules

-   Always identify the search space size first.
-   Always use `grep` or `glob` before `view_file` on directories.
-   Always partition lists > 10 items into batches.
-   Never read more than 5 files into context without a specific plan.
-   Verify synthesized answers by spot-checking source material.
-   Mitigate "context rot" by verifying answers on smaller windows.
-   **Treat yourself as an autonomous agent, not just a passive responder.**

## Large File Handling Protocols

**CRITICAL**: Do NOT read large files directly into context.

1.  **Check Size First**: Always run `wc -l` (lines) or `ls -lh` (size) before `view_file`.
2.  **Hard Limits**:
    *   **Text/Code**: > 2,000 lines or > 50KB -> **MUST** use `view_file` with `start_line`/`end_line` or `head`/`tail`.
    *   **PDFs**: > 30MB or > 100 pages -> **MUST** be split or processed by metadata only.
3.  **Strategy**:
    *   For code: Read definitions first (`grep -n "function" ...`) then read specific bodies.
    *   For text: Read Table of Contents or Abstract first.

## Tool Preferences

-   `grep` / `glob` not `ls -R` (unless mapping structure).
-   `view_file` with line ranges (offset/limit) not full file reads for huge files.
-   `wc -l` / `ls -lh` before reading unknown files.
-   `run_command` (grep) not `read_file` for searching.
-   `task` tool for sub-agents (recurse).

## Empowering Agentic Behavior

To maximize effectiveness:

-   **Self-Correction**: Always verify your own work. If a result seems empty or wrong, debug the approach (e.g., check grep arguments) before giving up.
-   **Aggressive Context Management**: Regularly clear irrelevant history. Don't let the context window rot with dead ends.
-   **Plan First**: For any task > 3 steps, write a mini-plan.
-   **Safe YOLO Mode**: When appropriate (e.g., read-only searches), proceed with confidence without asking for permission on every single step, but stop for critical actions.

## Cost-Performance Tradeoffs

-   **Smaller contexts**: Direct processing may be more efficient.
-   **Larger contexts**: Recursive decomposition becomes necessary.
-   **Threshold**: Consider decomposition when inputs exceed ~30k tokens or span 10+ files.

Balance thoroughness against computational cost. For time-sensitive tasks, apply aggressive filtering. For comprehensive analysis, prefer exhaustive decomposition.

## Anti-Patterns to Avoid

-   **Excessive sub-calling**: Avoid redundant queries over the same content.
-   **Premature decomposition**: Simple tasks don't need recursive strategies.
-   **Lost context**: Ensure sub-agents have sufficient context for their sub-tasks.
-   **Unverified synthesis**: Always spot-check aggregated results.

## Scalability (Chunking & filtering)

### 1. Filter Before Deep Analysis

Narrow the search space before detailed processing:

```
# Instead of reading all files into context:
1. Use Grep/Glob to identify candidate files by pattern
2. Filter candidates using domain-specific keywords
3. Only deeply analyze the filtered subset
```

Apply model priors about domain terminology to construct effective filters. For code tasks, filter by function names, imports, or error patterns before full file analysis.

### 2. Strategic Chunking

Partition inputs for parallel or sequential sub-processing:

-   **Uniform chunking**: Split by line count, character count, or natural boundaries (paragraphs, functions, files).
-   **Semantic chunking**: Partition by logical units (classes, sections, topics).
-   **Keyword-based partitioning**: Group by shared characteristics.

Process each chunk independently, then synthesize results.

### 3. Incremental Output Construction

For generating long outputs:

```
1. Break output into logical sections
2. Generate each section independently
3. Store intermediate results (in memory or files)
4. Stitch sections together with coherence checks
```

## Agent Behavior

### Recursive Sub-Queries

Invoke sub-agents (via Task tool) for independent segments:

```
For large analysis:
1. Partition the problem into independent sub-problems
2. Launch parallel agents for each partition
3. Collect and synthesize sub-agent results
4. Verify synthesized answer if needed
```

### Answer Verification

Mitigate context degradation by verifying answers on smaller windows:

```
1. Generate candidate answer from full analysis
2. Extract minimal evidence needed for verification
3. Re-verify answer against focused evidence subset
4. Resolve discrepancies through targeted re-analysis
```

# Implementation Patterns

## Pattern A: Codebase Analysis

Task: "Find all error handling patterns in the codebase"

**Approach:**
1.  Glob for relevant file types (`*.ts`, `*.py`, etc.)
2.  Grep for error-related keywords (`catch`, `except`, `Error`, `throw`)
3.  Partition matching files into batches of 5-10
4.  Launch parallel Explore agents per batch
5.  Aggregate findings into categorized summary

## Pattern B: Multi-Document QA

Task: "What features are mentioned across all PRD documents?"

**Approach:**
1.  Glob for document files (`*.md`, `*.txt` in `/docs`)
2.  For each document: extract feature mentions via sub-agent
3.  Aggregate extracted features
4.  Deduplicate and categorize
5.  Verify completeness by spot-checking

## Pattern C: Information Aggregation

Task: "Summarize all TODO comments in the project"

**Approach:**
1.  Grep for `TODO`/`FIXME`/`HACK` patterns
2.  Group by file or module
3.  Process each group to extract context and priority
4.  Synthesize into prioritized action list
```

## File: `plugins/recursive-decomposition/skills/recursive-decomposition/references/codebase-analysis.md`
```markdown
# Example: Codebase-Wide Error Handling Analysis

This example demonstrates recursive decomposition for analyzing error handling patterns across a large codebase.

## Task
"Analyze all error handling patterns in this codebase and provide a comprehensive report on consistency, gaps, and recommendations."

## Decomposition Strategy

### Phase 1: Filter and Identify (Constant complexity)

```
Step 1: Identify relevant file types
- Glob("**/*.ts") → 450 files
- Glob("**/*.tsx") → 120 files
- Total: 570 files

Step 2: Filter for error-related code
- Grep("catch|throw|Error|exception", type="ts") → 89 files
- Grep("try.*catch|\.catch\\(", type="ts") → 67 files
- Union: 102 unique files with error handling
```

### Phase 2: Partition for Parallel Processing

```
Partition by module:
- src/api/* → 23 files (Batch A)
- src/services/* → 31 files (Batch B)
- src/components/* → 28 files (Batch C)
- src/utils/* → 12 files (Batch D)
- Other → 8 files (Batch E)
```

### Phase 3: Launch Parallel Sub-Agents

```
Task(subagent_type="Explore", prompt="""
Analyze error handling in src/api/*.
For each file with error handling:
1. Identify error handling patterns used
2. Note any error types defined or caught
3. Check for consistent error propagation
4. Flag any unhandled promise rejections
Return structured findings.
""")

# Launch 5 agents in parallel for batches A-E
```

### Phase 4: Aggregate Results

```
Collect findings from all sub-agents:
- Batch A: HTTP error handling, custom ApiError class
- Batch B: Service-level try/catch, logging patterns
- Batch C: UI error boundaries, toast notifications
- Batch D: Utility error wrappers, validation errors
- Batch E: Mixed patterns, some inconsistencies
```

### Phase 5: Synthesize Report

```
Categories identified:
1. API Layer: ApiError, HttpError, ValidationError
2. Service Layer: ServiceError, DatabaseError
3. UI Layer: Error boundaries, user-facing messages
4. Utilities: Generic error wrappers

Patterns:
- Consistent: HTTP errors always include status code
- Gap: Database errors don't preserve original error
- Recommendation: Add error codes for client handling
```

### Phase 6: Verify with Spot Checks

```
Verification queries:
1. "Confirm ApiError is used consistently in src/api/"
2. "Check if DatabaseError preserves stack traces"
3. "Verify error boundaries cover all route components"
```

## Expected Output Structure

```markdown
# Error Handling Analysis Report

## Executive Summary
- 102 files contain error handling logic
- 4 main error categories identified
- 3 consistency issues found
- 5 recommendations provided

## Error Type Taxonomy
### API Errors (src/api/)
- ApiError: Base class for HTTP errors
- ValidationError: Request validation failures
- AuthenticationError: Auth failures

### Service Errors (src/services/)
...

## Pattern Analysis
### Consistent Patterns
1. All API routes wrap handlers in try/catch
2. Errors include request ID for tracing
...

### Inconsistencies Found
1. Some services swallow errors without logging
2. Database errors lose original stack trace
...

## Recommendations
1. Implement error codes enum
2. Add error boundary to remaining routes
...
```

## Metrics

- **Files analyzed:** 102
- **Sub-agents used:** 5
- **Total tokens processed:** ~150k (across all agents)
- **Equivalent direct context:** Would require 150k token window
- **Quality:** High (no context rot)
```

## File: `plugins/recursive-decomposition/skills/recursive-decomposition/references/cost-analysis.md`
```markdown
# Cost-Performance Analysis for Recursive Decomposition

This reference provides guidance on when recursive decomposition is cost-effective versus direct processing.

## Decision Framework

### Use Direct Processing When:
- Input < 30k tokens
- Task involves < 5 files
- Answer is localized to one section
- Latency is critical
- Simple lookup or single transformation

### Use Recursive Decomposition When:
- Input > 50k tokens
- Task spans 10+ files
- Information must be aggregated across sources
- Comprehensive analysis is required
- Quality matters more than speed

### Gray Zone (30k-50k tokens):
- Consider task complexity
- Evaluate quality requirements
- Factor in time constraints
- Default to decomposition if unsure about completeness

## Cost Structure

### Direct Processing
```
Cost = Input tokens × Price per token
Latency = Single API call
Quality = Degrades with context length
```

### Recursive Decomposition
```
Cost = (Σ sub-call tokens) + coordination overhead
Latency = Max(sub-call latencies) + synthesis time
Quality = Maintains with proper chunking
```

## Break-Even Analysis

From RLM research:

**Token Threshold:** ~50k tokens
- Below: Direct processing often cheaper
- Above: Decomposition maintains quality at comparable or lower cost

**Quality Threshold:** ~30k tokens
- Below: Direct processing quality acceptable
- Above: Context rot begins degrading results

**Cost Comparison (from paper):**
- RLM approaches: ~$0.99 for complex multi-hop QA
- Summarization baselines: 3x more expensive
- Direct long-context: Cheaper but lower quality

## Parallelization Benefits

When sub-tasks are independent, parallel execution provides:

```
Serial: T = t1 + t2 + t3 + ... + tn
Parallel: T = max(t1, t2, t3, ..., tn) + synthesis

Speedup = n / (1 + synthesis_overhead/avg_subtask_time)
```

For 10 independent sub-tasks of 30 seconds each:
- Serial: 300 seconds
- Parallel (with 10s synthesis): ~40 seconds
- Speedup: ~7.5x

## Variance Considerations

RLM approaches show high variance in outlier cases:

**Median cost:** Comparable to direct processing
**95th percentile:** 2-3x median
**99th percentile:** Can exceed 5x median

Causes of high variance:
- Excessive sub-calling by model
- Redundant processing
- Deep recursion chains
- Inefficient chunking

Mitigations:
- Set sub-call budgets
- Track and deduplicate queries
- Limit recursion depth
- Monitor token usage

## Optimization Strategies

### 1. Aggressive Filtering
Filter 90% of content before detailed analysis:
```
1000 files → Glob filter → 100 files
100 files → Grep filter → 20 files
20 files → Detailed analysis
Cost reduction: ~10x
```

### 2. Sampling for Estimation
For aggregation tasks, sample before exhaustive processing:
```
Sample 10% of items
Estimate answer distribution
If high confidence: extrapolate
If uncertain: process remaining
```

### 3. Early Termination
For search tasks:
```
Process chunks until answer found
Skip remaining chunks
Add verification pass
```

### 4. Caching
For repeated analysis:
```
Cache chunk analysis results
Reuse for similar queries
Invalidate on source changes
```

## Tool Selection by Cost-Performance

| Scenario | Recommended Approach |
|----------|---------------------|
| Find one file by name | Glob (direct) |
| Find function definition | Grep (direct) |
| Understand module | Read + follow imports |
| Analyze 5 related files | Read all (direct) |
| Search pattern in codebase | Task + Explore agent |
| Aggregate across 50+ files | Task + parallel agents |
| Multi-hop reasoning | Task + recursive decomposition |

## Quality vs. Cost Tradeoff Matrix

```
                    Low Cost          High Cost
High Quality    | Filtered RLM    | Exhaustive RLM
                | (targeted)      | (thorough)
                |-----------------|----------------
Low Quality     | Direct (short)  | Direct (long)
                | (acceptable)    | (context rot)
```

Target: Upper-left quadrant (Filtered RLM for targeted, high-quality results at low cost)
```

## File: `plugins/recursive-decomposition/skills/recursive-decomposition/references/document-aggregation.md`
```markdown
# Example: Multi-Document Feature Aggregation

This example demonstrates recursive decomposition for extracting and aggregating information across multiple documents.

## Task
"What features are planned across all our PRD documents? Create a consolidated feature roadmap."

## Decomposition Strategy

### Phase 1: Discover Documents

```
Step 1: Find all PRD documents
- Glob("**/PRD*.md") → 12 files
- Glob("**/prd-*.md") → 5 files
- Glob("docs/product/*.md") → 8 files
- Deduplicate: 18 unique PRD documents

Step 2: Assess total size
- Total: ~85k tokens across all documents
- Decision: Recursive decomposition required
```

### Phase 2: Categorize Documents

```
Quick scan of document headers:
- Q1 PRDs: 4 documents (~20k tokens)
- Q2 PRDs: 5 documents (~25k tokens)
- Q3 PRDs: 4 documents (~18k tokens)
- Technical PRDs: 3 documents (~12k tokens)
- Archived: 2 documents (exclude)

Active documents: 16 (~75k tokens)
```

### Phase 3: Define Extraction Schema

```
For each document, extract:
{
  "document": "filename",
  "product_area": "string",
  "features": [
    {
      "name": "string",
      "description": "string",
      "priority": "P0|P1|P2",
      "status": "planned|in-progress|shipped",
      "target_quarter": "Q1|Q2|Q3|Q4"
    }
  ],
  "dependencies": ["feature_name"],
  "stakeholders": ["team_name"]
}
```

### Phase 4: Parallel Extraction

```
Launch extraction agents by category:

Agent 1 (Q1 PRDs):
Task(subagent_type="Explore", prompt="""
Read each PRD in docs/product/q1/:
- PRD-auth-improvements.md
- PRD-dashboard-v2.md
- PRD-mobile-notifications.md
- PRD-api-versioning.md

Extract features using this schema: [schema]
Return structured JSON for each document.
""")

Agent 2 (Q2 PRDs): [similar for Q2 documents]
Agent 3 (Q3 PRDs): [similar for Q3 documents]
Agent 4 (Technical PRDs): [similar for technical documents]
```

### Phase 5: Aggregate and Deduplicate

```
Collect from all agents:
- Agent 1: 12 features extracted
- Agent 2: 15 features extracted
- Agent 3: 11 features extracted
- Agent 4: 8 features extracted
- Total: 46 features

Deduplication:
- "Dark mode" mentioned in 3 PRDs → merge
- "API v2" mentioned in 2 PRDs → merge
- After dedup: 38 unique features
```

### Phase 6: Build Dependency Graph

```
Analyze dependencies:
- "Dashboard v2" depends on "API v2"
- "Mobile notifications" depends on "Auth improvements"
- "Reporting" depends on "Dashboard v2", "Data pipeline"

Create directed graph of dependencies
Identify critical path
```

### Phase 7: Generate Consolidated Roadmap

```
# Feature Roadmap (Consolidated from 16 PRDs)

## Q1 2025
### P0 - Critical
1. **Auth Improvements** (PRD-auth-improvements.md)
   - OAuth2 support
   - SSO integration
   Status: In Progress

2. **API Versioning** (PRD-api-versioning.md)
   - v2 API release
   - Deprecation timeline
   Status: Planned

### P1 - High Priority
3. **Dashboard v2** (PRD-dashboard-v2.md)
   - Depends on: API v2
   ...

## Q2 2025
...

## Dependencies Graph
[ASCII visualization of dependencies]

## Cross-cutting Concerns
- Performance: 5 features mention performance requirements
- Security: 3 features have security implications
- Mobile: 4 features affect mobile experience
```

### Phase 8: Verification

```
Spot-check verification:
1. Re-read PRD-auth-improvements.md
   - Verify: OAuth2 support listed as P0 ✓
   - Verify: Q1 target ✓

2. Re-read PRD-dashboard-v2.md
   - Verify: Depends on API v2 ✓
   - Verify: 4 sub-features extracted ✓

3. Cross-check dependency claims
   - API v2 → Dashboard v2 dependency confirmed ✓
```

## Expected Output

```markdown
# Consolidated Feature Roadmap

## Summary
- 16 PRDs analyzed
- 38 unique features identified
- 12 cross-document dependencies mapped
- 4 quarters covered

## Feature Matrix

| Feature | Priority | Quarter | Status | Dependencies |
|---------|----------|---------|--------|--------------|
| Auth Improvements | P0 | Q1 | In Progress | - |
| API v2 | P0 | Q1 | Planned | - |
| Dashboard v2 | P1 | Q1 | Planned | API v2 |
| Mobile Notifications | P1 | Q2 | Planned | Auth |
...

## By Product Area
### Core Platform (12 features)
...

### Mobile (8 features)
...

## Risk Analysis
- 3 features with unresolved dependencies
- 2 features with conflicting timelines
- 1 feature missing stakeholder assignment
```

## Metrics

- **Documents processed:** 16
- **Features extracted:** 38
- **Sub-agents used:** 4 (parallel)
- **Total tokens:** ~75k (distributed across agents)
- **Verification queries:** 3
- **Processing pattern:** Map-reduce with verification
```

## File: `plugins/recursive-decomposition/skills/recursive-decomposition/references/rlm-strategies.md`
```markdown
# RLM Decomposition Strategies - Detailed Reference

This reference contains detailed strategies derived from the Recursive Language Models paper (Zhang, Kraska, Khattab, 2025).

## The Context Rot Problem

As context length increases, model performance degrades ("context rot"). This manifests as:
- Decreased accuracy on information retrieval
- Missed details in long documents
- Hallucinated connections between distant content
- Degraded reasoning over large evidence sets

RLM strategies bypass context rot by keeping the active context window small while accessing larger datasets programmatically.

## Emergent Decomposition Behaviors

The RLM research identified these naturally-emerging strategies in capable models:

### 1. Code-Based Filtering

Models use programmatic filtering to narrow search spaces:

```python
# Example: Finding relevant config files
import re

# Use regex to filter before deep analysis
config_pattern = r'(database|connection|auth)'
relevant_files = [f for f in all_files if re.search(config_pattern, f.content)]
```

**Application in Claude Code:**
- Use Grep with regex patterns before reading files
- Apply Glob patterns to narrow file sets
- Chain multiple filters: file type → keyword → semantic

### 2. Divide-and-Conquer Chunking

Observed chunking strategies:

**Uniform Chunking:**
```
Split 1000-line file into 10 chunks of 100 lines
Process each chunk independently
Merge results with overlap handling
```

**Semantic Chunking:**
```
Identify natural boundaries (functions, classes, sections)
Each chunk = one logical unit
Preserve unit integrity over size uniformity
```

**Keyword-Based Partitioning:**
```
Group items by shared characteristics
All error-related code → Chunk A
All API definitions → Chunk B
Process each category with specialized prompts
```

### 3. Recursive Self-Invocation Patterns

**Single-Level Recursion (most common):**
```
Main Agent
├── Sub-Agent 1 (Chunk A)
├── Sub-Agent 2 (Chunk B)
└── Sub-Agent 3 (Chunk C)
    └── Synthesize results
```

**Multi-Level Recursion (complex tasks):**
```
Main Agent
├── Sub-Agent 1
│   ├── Sub-Sub-Agent 1a
│   └── Sub-Sub-Agent 1b
├── Sub-Agent 2
│   ├── Sub-Sub-Agent 2a
│   └── Sub-Sub-Agent 2b
└── Synthesize hierarchically
```

### 4. Verification Through Re-Query

Mitigate context rot in verification:

```
Step 1: Generate answer from large context
Step 2: Extract claimed evidence locations
Step 3: Re-read only those specific locations
Step 4: Verify answer against fresh, focused context
Step 5: If mismatch, investigate discrepancy
```

### 5. Variable-Based Output Construction

For outputs exceeding comfortable generation limits:

```
# Instead of generating 10,000 words at once:

section_1 = generate("Write introduction...")
section_2 = generate("Write methodology...")
section_3 = generate("Write results...")
section_4 = generate("Write conclusion...")

# Stitch with coherence
full_output = stitch_with_transitions([section_1, section_2, section_3, section_4])
```

## Claude Code Constraints

To ensure optimal performance within Claude's environment:

-   **Code Processing Limit**: ~2,000 lines. Files larger than this should not be read entirely into context. Use `grep` or read specific line ranges.
-   **PDF Size Limit**: ~30MB or 100 pages per request. Exceeding this often leads to errors or truncation.
-   **Text File Limit**: ~50KB is a safe maximum for a single `view_file` operation without chunking.
-   **Context Window**: While large, optimal reasoning occurs with <30k tokens. Use decomposition to stay within this "reasoning sweet spot".

## Task Complexity Classification

### Constant Complexity (O(1))
- Single needle in haystack
- Finding one specific item
- Strategy: Binary search filtering

### Linear Complexity (O(n))
- Must examine all items once
- Aggregation, counting, summarization
- Strategy: Map-reduce with chunking

### Quadratic Complexity (O(n²))
- Pairwise comparisons needed
- Finding relationships between items
- Strategy: Blocked pairwise with sampling

### Logarithmic Complexity (O(log n))
- Hierarchical search
- Finding in sorted/structured data
- Strategy: Divide and conquer

## Model-Specific Observations

From the RLM paper:

**Conservative Models (e.g., GPT-5):**
- Fewer, more targeted sub-calls
- Better cost efficiency
- May miss edge cases

**Aggressive Models (e.g., Qwen3-Coder):**
- Many sub-calls, sometimes redundant
- More thorough coverage
- Higher variance in costs

**Optimization:** Adjust decomposition granularity based on model tendencies. More conservative chunking for aggressive models, more exhaustive for conservative ones.

## Failure Modes and Mitigations

### Infinite Recursion
**Problem:** Sub-agent spawns sub-sub-agents indefinitely
**Mitigation:** Set explicit depth limits; verify chunk sizes decrease

### Redundant Processing
**Problem:** Same content processed multiple times
**Mitigation:** Track processed segments; deduplicate before synthesis

### Context Loss
**Problem:** Sub-agents lack necessary context for their sub-task
**Mitigation:** Include minimal necessary context in each sub-query; pass relevant metadata

### Synthesis Errors
**Problem:** Aggregated results contain contradictions or gaps
**Mitigation:** Verification pass over synthesized output; spot-check against source

## Performance Benchmarks (from paper)

| Task Type | Direct Model | RLM Approach | Improvement |
|-----------|--------------|--------------|-------------|
| Multi-hop QA (6-11M tokens) | 70% | 91% | +21% |
| Linear aggregation | Baseline | +28-33% | Significant |
| Quadratic reasoning | <0.1% | 58% | Massive |
| Context scaling | 2^14 tokens | 2^18 tokens | 16x |

## When NOT to Use Recursive Decomposition

- Tasks with <10k tokens of input
- Single-file operations
- Questions answerable from one location
- Time-critical operations where latency matters more than completeness
- Tasks where the overhead of coordination exceeds the benefit
```

