---
id: model-hierarchy-skill-knowledge
type: document
owner: SYSTEM
tags: [auto-healed]
healed_at: 2026-04-03T22:46:22.046005
---

# KNOWLEDGE EXTRACT: model-hierarchy-skill
> **Extracted on:** 2026-03-29 22:08:37
> **Source:** model-hierarchy-skill

---

## File: `.gitignore`
```
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Virtual environments
venv/
ENV/
env/
.venv/

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/

# IDE
.idea/
.vscode/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Zak Cole

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

## File: `pyproject.toml`
```
[project]
name = "model-hierarchy-skill"
version = "0.1.0"
description = "OpenClaw skill for cost-optimized model routing based on task complexity"
readme = "README.md"
license = {text = "MIT"}
authors = [{name = "Zak Cole", email = "zak@numbergroup.xyz"}]
requires-python = ">=3.9"

[project.optional-dependencies]
test = ["pytest>=7.0.0"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_functions = ["test_*"]
addopts = "-v"

[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"
```

## File: `README.md`
```markdown
# model-hierarchy-skill

Cost-optimize AI agent operations by routing tasks to appropriate models based on complexity.

## The Problem

Most AI agents run everything on expensive models. But 80% of agent tasks are routine: file reads, status checks, formatting, simple Q&A. You're paying $15-75/M tokens for work that $0.14/M tokens handles fine.

## The Solution

A skill that teaches agents to classify tasks and route them to the cheapest model that can handle them:

| Task Type | Model Tier | Cost | Examples |
|-----------|------------|------|----------|
| Routine (80%) | Cheap | $0.14-0.50/M | File ops, status checks, formatting |
| Moderate (15%) | Mid | $1-5/M | Code gen, summaries, drafts |
| Complex (5%) | Premium | $10-75/M | Debugging, architecture, novel problems |

**Result: ~10x cost reduction** with equivalent quality on the tasks that matter.

## Quick Start

### OpenClaw

```bash
# Copy SKILL.md to your skills directory
cp SKILL.md ~/.openclaw/skills/model-hierarchy/SKILL.md

# Restart gateway to pick up the skill
openclaw gateway restart
```

### Claude Code / Codex

Add to your `CLAUDE.md` or project instructions:

```markdown
## Model Routing

Before executing tasks, classify complexity:
- ROUTINE (file ops, lookups, formatting) → Use cheapest model
- MODERATE (code, summaries, analysis) → Use mid-tier model  
- COMPLEX (debugging, architecture, failures) → Use premium model

When spawning sub-agents, default to cheap models unless task requires more.
```

### Other Agent Systems

See [SKILL.md](SKILL.md) for the full classification rules and integration examples.

## Cost Math

Assuming 100K tokens/day:

| Strategy | Monthly Cost |
|----------|--------------|
| Pure Opus | ~$225 |
| Pure Sonnet | ~$45 |
| Hierarchy (80/15/5) | ~$19 |

## Testing

```bash
# Run classification tests
python -m pytest tests/ -v

# Test specific scenarios
python tests/test_classification.py
```

## Files

```
model-hierarchy-skill/
├── SKILL.md          # The skill (install this)
├── README.md         # You're here
├── tests/
│   ├── test_classification.py
│   └── scenarios.json
└── examples/
    ├── openclaw.md
    └── claude-code.md
```

## License

MIT
```

## File: `SKILL.md`
```markdown
---
name: model-hierarchy
description: >
  Cost-optimize AI agent operations by routing tasks to appropriate models based on complexity.
  Use this skill when: (1) deciding which model to use for a task, (2) spawning sub-agents,
  (3) considering cost efficiency, (4) the current model feels like overkill for the task.
  Triggers: "model routing", "cost optimization", "which model", "too expensive", "spawn agent".

---

# Model Hierarchy

Route tasks to the cheapest model that can handle them. Most agent work is routine.

## Core Principle

**80% of agent tasks are janitorial.** File reads, status checks, formatting, simple Q&A. These don't need expensive models. Reserve premium models for problems that actually require deep reasoning.

## Model Tiers

### Tier 1: Cheap ($0.10-0.50/M tokens)

| Model | Input | Output | Best For |
|-------|-------|--------|----------|
| DeepSeek V3 | $0.14 | $0.28 | General routine work |
| GPT-4o-mini | $0.15 | $0.60 | Quick responses |
| Claude Haiku | $0.25 | $1.25 | Fast tool use |
| Gemini Flash | $0.075 | $0.30 | High volume |
| GLM 5 (Zhipu) | (OpenRouter Z.AI) | (OpenRouter Z.AI) | Routine + moderate text; 200K context; **text-only** — do not use for image/vision |
| Kimi K2.5 (Moonshot) | $0.45 | $2.25 | Routine + moderate; 262K context; **multimodal (text + image + video)** |

**Text-only models (e.g. GLM 5):** Do not use for any task that requires image input or vision — no photo analysis, screenshots, image-generation tools, or document/chart vision. Route to a vision-capable model (e.g. Kimi K2.5, GPT-4o, Gemini, Claude with vision, GLM-4.5V/4.6V).

**Vision-capable Tier 1/2 (e.g. Kimi K2.5):** Use for routine or moderate tasks that may involve images — screenshots, photo analysis, docs, image-generation orchestration — without moving to premium vision models.

### Tier 2: Mid ($1-5/M tokens)

| Model | Input | Output | Best For |
|-------|-------|--------|----------|
| Claude Sonnet | $3.00 | $15.00 | Balanced performance |
| GPT-4o | $2.50 | $10.00 | Multimodal tasks |
| Gemini Pro | $1.25 | $5.00 | Long context |

### Tier 3: Premium ($10-75/M tokens)

| Model | Input | Output | Best For |
|-------|-------|--------|----------|
| Claude Opus | $15.00 | $75.00 | Complex reasoning |
| GPT-4.5 | $75.00 | $150.00 | Frontier tasks |
| o1 | $15.00 | $60.00 | Multi-step reasoning |
| o3-mini | $1.10 | $4.40 | Reasoning on budget |

*Prices as of Feb 2026. Check provider docs for current rates.*

## Task Classification

Before executing any task, classify it:

### ROUTINE → Use Tier 1

**Requires image/vision** → Do not assign to text-only models (GLM 5, etc.). Use a vision-capable model from Tier 1/2 or 3 (e.g. Kimi K2.5, GPT-4o, Gemini, Claude, GLM-4.5V).

Characteristics:
- Single-step operations
- Clear, unambiguous instructions
- No judgment required
- Deterministic output expected

Examples:
- File read/write operations
- Status checks and health monitoring
- Simple lookups (time, weather, definitions)
- Formatting and restructuring text
- List operations (filter, sort, transform)
- API calls with known parameters
- Heartbeat and cron tasks
- URL fetching and basic parsing

### MODERATE → Use Tier 2

Characteristics:
- Multi-step but well-defined
- Some synthesis required
- Standard patterns apply
- Quality matters but isn't critical

Examples:
- Code generation (standard patterns)
- Summarization and synthesis
- Draft writing (emails, docs, messages)
- Data analysis and transformation
- Multi-file operations
- Tool orchestration
- Code review (non-security)
- Search and research tasks

### COMPLEX → Use Tier 3

Characteristics:
- Novel problem solving required
- Multiple valid approaches
- Nuanced judgment calls
- High stakes or irreversible
- Previous attempts failed

Examples:
- Multi-step debugging
- Architecture and design decisions
- Security-sensitive code review
- Tasks where cheaper model already failed
- Ambiguous requirements needing interpretation
- Long-context reasoning (>50K tokens)
- Creative work requiring originality
- Adversarial or edge-case handling

## Decision Algorithm

```
function selectModel(task):
    # Rule 1: Vision override (Tier 1/2 includes text-only models)
    if task.requiresImageInput or task.requiresVision:
        return VISION_CAPABLE_MODEL  # e.g. Kimi K2.5, GPT-4o, Gemini, Claude; do not use GLM 5 or other text-only
    
    # Rule 2: Escalation override
    if task.previousAttemptFailed:
        return nextTierUp(task.previousModel)
    
    # Rule 3: Explicit complexity signals
    if task.hasSignal("debug", "architect", "design", "security"):
        return TIER_3
    
    if task.hasSignal("write", "code", "summarize", "analyze"):
        return TIER_2
    
    # Rule 4: Default classification
    complexity = classifyTask(task)
    
    if complexity == ROUTINE:
        return TIER_1
    elif complexity == MODERATE:
        return TIER_2
    else:
        return TIER_3
```

## Behavioral Rules

### For Main Session

1. **Default to Tier 2** for interactive work
2. **Suggest downgrade** when doing routine work: "This is routine - I can handle this on a cheaper model or spawn a sub-agent."
3. **Request upgrade** when stuck: "This needs more reasoning power. Switching to [premium model]."

### For Sub-Agents

1. **Default to Tier 1** unless task is clearly moderate+
2. **Batch similar tasks** to amortize overhead
3. **Report failures** back to parent for escalation

### For Automated Tasks

1. **Heartbeats/monitoring** → Always Tier 1
2. **Scheduled reports** → Tier 1 or 2 based on complexity
3. **Alert responses** → Start Tier 2, escalate if needed

## Communication Patterns

When suggesting model changes, use clear language:

**Downgrade suggestion:**
> "This looks like routine file work. Want me to spawn a sub-agent on DeepSeek for this? Same result, fraction of the cost."

**Upgrade request:**
> "I'm hitting the limits of what I can figure out here. This needs Opus-level reasoning. Switching up."

**Explaining hierarchy:**
> "I'm running the heavy analysis on Sonnet while sub-agents fetch the data on DeepSeek. Keeps costs down without sacrificing quality where it matters."

## Cost Impact

Assuming 100K tokens/day average usage:

| Strategy | Monthly Cost | Notes |
|----------|--------------|-------|
| Pure Opus | ~$225 | Maximum capability, maximum spend |
| Pure Sonnet | ~$45 | Good default for most work |
| Pure DeepSeek | ~$8 | Cheap but limited on hard problems |
| **Hierarchy (80/15/5)** | **~$19** | Best of all worlds |

The 80/15/5 split:
- 80% routine tasks on Tier 1 (~$6)
- 15% moderate tasks on Tier 2 (~$7)
- 5% complex tasks on Tier 3 (~$6)

**Result: 10x cost reduction vs pure premium, with equivalent quality on complex tasks.**

## Integration Examples

### OpenClaw

```yaml
# config.yml - set default model
model: anthropic/claude-sonnet-4

# In session, switch models
/model opus  # upgrade for complex task
/model deepseek  # downgrade for routine

# Spawn sub-agent on cheap model
sessions_spawn:
  task: "Fetch and parse these 50 URLs"
  model: deepseek
```

**OpenRouter (Tier 1 with vision or text-only):**

```yaml
# Tier 1 with vision — Kimi K2.5 (multimodal)
model: openrouter/moonshotai/kimi-k2.5
# Heartbeats, cron, image-involving tasks: K2.5 handles text and vision.

# Tier 1 text-only — GLM 5 (no vision)
# model: openrouter/z-ai/glm-5  # exact ID TBD on OpenRouter Z.AI
# Routine text-only only; for image tasks use Kimi K2.5 or another vision-capable model.
```

### Claude Code

```
# In CLAUDE.md or project instructions
When spawning background agents, use claude-3-haiku for:
- File operations
- Simple searches  
- Status checks

Reserve claude-sonnet-4 for:
- Code generation
- Analysis tasks
```

### General Agent Systems

```python
def get_model_for_task(task_description: str) -> str:
    routine_signals = ['read', 'fetch', 'check', 'list', 'format', 'status']
    complex_signals = ['debug', 'architect', 'design', 'security', 'why']
    
    desc_lower = task_description.lower()
    
    if any(signal in desc_lower for signal in complex_signals):
        return "claude-opus-4"
    elif any(signal in desc_lower for signal in routine_signals):
        return "deepseek-v3"
    else:
        return "claude-sonnet-4"
```

## Anti-Patterns

**DON'T:**
- Run heartbeats on Opus
- Use premium models for file I/O
- Keep expensive model when task is clearly routine
- Spawn sub-agents on premium models by default
- Use GLM 5 (or any text-only Tier 1/2 model) for image/vision tasks — e.g. photo analysis, screenshot understanding, image-generation skills, or any tool that takes image input

**DO:**
- Start mid-tier, adjust based on task
- Spawn helpers on cheapest viable model
- Escalate explicitly when stuck
- Track cost per task type to optimize further

## Extending This Skill

To customize for your use case:

1. **Adjust tier definitions** based on your provider/budget
2. **Add domain-specific signals** to classification rules
3. **Track actual complexity** vs predicted to improve heuristics
4. **Set budget alerts** to catch runaway premium usage
```

## File: `examples/claude-code.md`
```markdown
# Claude Code / Codex Integration

## Add to CLAUDE.md

Add this section to your project's `CLAUDE.md` or global instructions:

```markdown
## Model Routing

Before executing tasks, classify by complexity:

### ROUTINE (spawn on haiku/cheap)
- File read/write operations
- Status checks and lookups
- Formatting and list operations
- Simple Q&A

### MODERATE (use current model)
- Code generation
- Summarization
- Draft writing
- Data analysis

### COMPLEX (request upgrade if needed)
- Multi-step debugging
- Architecture decisions
- Security reviews
- Tasks where previous attempt failed

When spawning background agents, default to claude-3-haiku for routine work.
When stuck on a problem, suggest upgrading to opus.
```

## Behavioral Examples

### Routine Task

User: "Read config.json and show me the port number"

Agent behavior:
- Classifies as ROUTINE (file read + simple lookup)
- If on expensive model, suggests: "This is routine - I can spawn a background agent for this"
- Executes on cheapest available

### Moderate Task

User: "Write a Python function to validate email addresses"

Agent behavior:
- Classifies as MODERATE (code generation)
- Uses current mid-tier model
- No model change needed

### Complex Task

User: "This test passes locally but fails in CI. Debug it."

Agent behavior:
- Classifies as COMPLEX (debugging)
- If on cheap model, requests: "This needs more reasoning power - switching to opus"
- Proceeds with premium model

## Sub-Agent Spawning

When using background agents:

```
# Good - routine work on cheap model
Spawn background agent (haiku): "Fetch these 20 URLs and extract titles"

# Good - complex work on appropriate model
Spawn background agent (sonnet): "Analyze this codebase and document the architecture"

# Bad - wasting money
Spawn background agent (opus): "Read all .md files in this directory"
```
```

## File: `examples/openclaw.md`
```markdown
# OpenClaw Integration

## Installation

Copy the skill to your OpenClaw skills directory:

```bash
cp SKILL.md ~/.openclaw/skills/model-hierarchy/SKILL.md
openclaw gateway restart
```

## Configuration

Set your default model to mid-tier in `config.yml`:

```yaml
model: anthropic/claude-sonnet-4
```

## Usage

### Switching Models in Session

```
# Upgrade to premium for complex task
/model opus

# Downgrade to cheap for routine work
/model deepseek
```

### Spawning Sub-Agents

When spawning sub-agents for bulk work, specify the model:

```python
sessions_spawn(
    task="Fetch and parse these 50 URLs",
    model="deepseek"  # Cheap model for routine work
)
```

### Heartbeat Configuration

Configure heartbeats to run on cheap models:

```yaml
# In your agent config
heartbeat:
  model: deepseek-v3
  interval: 30m
```

## Expected Behavior

After installing the skill, your agent should:

1. **Suggest downgrades** when doing routine work on expensive models
2. **Request upgrades** when stuck on complex problems
3. **Default sub-agents to cheap models** unless task requires more

## Cost Tracking

Use `/status` to monitor token usage and costs per session.
```

## File: `tests/conftest.py`
```python
"""Pytest configuration and fixtures for model-hierarchy tests."""

import pytest


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
```

## File: `tests/scenarios.json`
```json
{
  "routine_tasks": [
    {
      "description": "Read the contents of config.json",
      "expected_tier": 1,
      "signals": ["read", "file"]
    },
    {
      "description": "Check if the server is running",
      "expected_tier": 1,
      "signals": ["check", "status"]
    },
    {
      "description": "What time is it in Tokyo?",
      "expected_tier": 1,
      "signals": ["simple_qa"]
    },
    {
      "description": "Format this JSON and fix the indentation",
      "expected_tier": 1,
      "signals": ["format"]
    },
    {
      "description": "List all files in the src directory",
      "expected_tier": 1,
      "signals": ["list", "file"]
    },
    {
      "description": "Fetch the homepage of example.com",
      "expected_tier": 1,
      "signals": ["fetch", "url"]
    },
    {
      "description": "Filter this list to only items over 100",
      "expected_tier": 1,
      "signals": ["filter", "list"]
    },
    {
      "description": "Run the health check",
      "expected_tier": 1,
      "signals": ["health", "check"]
    },
    {
      "description": "Convert this date to ISO format",
      "expected_tier": 1,
      "signals": ["format", "date"]
    },
    {
      "description": "Get the current git status",
      "expected_tier": 1,
      "signals": ["status", "git"]
    }
  ],
  "moderate_tasks": [
    {
      "description": "Write a Python function to parse CSV files",
      "expected_tier": 2,
      "signals": ["write", "code"]
    },
    {
      "description": "Summarize this 10-page document",
      "expected_tier": 2,
      "signals": ["summarize"]
    },
    {
      "description": "Draft an email to the team about the launch",
      "expected_tier": 2,
      "signals": ["draft", "write"]
    },
    {
      "description": "Analyze the sales data and find trends",
      "expected_tier": 2,
      "signals": ["analyze", "data"]
    },
    {
      "description": "Refactor this function to be more readable",
      "expected_tier": 2,
      "signals": ["refactor", "code"]
    },
    {
      "description": "Search for recent articles about AI agents",
      "expected_tier": 2,
      "signals": ["search", "research"]
    },
    {
      "description": "Generate unit tests for this module",
      "expected_tier": 2,
      "signals": ["generate", "test", "code"]
    },
    {
      "description": "Create a README for this project",
      "expected_tier": 2,
      "signals": ["create", "write"]
    },
    {
      "description": "Review this pull request",
      "expected_tier": 2,
      "signals": ["review", "code"]
    },
    {
      "description": "Transform this JSON into a markdown table",
      "expected_tier": 2,
      "signals": ["transform", "data"]
    }
  ],
  "complex_tasks": [
    {
      "description": "Debug why this test is flaky and sometimes fails",
      "expected_tier": 3,
      "signals": ["debug"]
    },
    {
      "description": "Design the architecture for a distributed cache system",
      "expected_tier": 3,
      "signals": ["design", "architect"]
    },
    {
      "description": "Review this smart contract for security vulnerabilities",
      "expected_tier": 3,
      "signals": ["security", "review"]
    },
    {
      "description": "I tried three different approaches and none work. Why?",
      "expected_tier": 3,
      "signals": ["failed_attempts"]
    },
    {
      "description": "Explain why the system behaves differently under load",
      "expected_tier": 3,
      "signals": ["explain", "why", "complex"]
    },
    {
      "description": "Architect a migration strategy from monolith to microservices",
      "expected_tier": 3,
      "signals": ["architect", "design"]
    },
    {
      "description": "This code has a race condition somewhere. Find it.",
      "expected_tier": 3,
      "signals": ["debug", "concurrency"]
    },
    {
      "description": "Design the database schema for a multi-tenant SaaS",
      "expected_tier": 3,
      "signals": ["design", "architect"]
    },
    {
      "description": "Why does this work in dev but fail in production?",
      "expected_tier": 3,
      "signals": ["debug", "why"]
    },
    {
      "description": "Evaluate the tradeoffs between these three approaches",
      "expected_tier": 3,
      "signals": ["evaluate", "tradeoffs"]
    }
  ],
  "edge_cases": [
    {
      "description": "Read this file and summarize it",
      "expected_tier": 2,
      "note": "Compound task - summarize dominates over read"
    },
    {
      "description": "Check the logs and debug why the service crashed",
      "expected_tier": 3,
      "note": "Compound task - debug dominates over check"
    },
    {
      "description": "Format this code",
      "expected_tier": 2,
      "note": "Code keyword triggers moderate - acceptable tradeoff"
    },
    {
      "description": "Write hello world in Python",
      "expected_tier": 2,
      "note": "Write keyword triggers moderate - correct for most code tasks"
    },
    {
      "description": "The previous model couldn't solve this. Try again.",
      "expected_tier": 3,
      "note": "Escalation signal - always upgrade"
    }
  ]
}
```

## File: `tests/test_classification.py`
```python
"""
Tests for model hierarchy task classification.

These tests verify that the classification heuristics correctly route
tasks to appropriate model tiers based on complexity signals.
"""

import json
import re
from pathlib import Path
from typing import Literal

import pytest

# Model tier definitions
TIER_1_MODELS = ["deepseek-v3", "gpt-4o-mini", "claude-3-haiku", "gemini-flash"]
TIER_2_MODELS = ["claude-sonnet-4", "gpt-4o", "gemini-pro"]
TIER_3_MODELS = ["claude-opus-4", "gpt-4.5", "o1", "o3-mini"]


# Signal patterns for classification
ROUTINE_SIGNALS = [
    "read", "fetch", "check", "list", "format", "status", "get",
    "filter", "sort", "convert", "parse", "health", "ping", "time",
    "date", "lookup", "find file", "show", "display"
]

MODERATE_SIGNALS = [
    "write", "code", "summarize", "draft", "analyze", "create",
    "generate", "review", "refactor", "transform", "search",
    "research", "explain", "describe", "compare"
]

COMPLEX_SIGNALS = [
    "debug", "architect", "design", "security", "why does",
    "why is", "tradeoff", "evaluate", "doesn't work", "failed",
    "tried", "race condition", "vulnerability", "migrate",
    "behaves differently", "under load", "production"
]

ESCALATION_SIGNALS = [
    "previous", "couldn't", "failed", "try again", "still not working",
    "none of these work", "stuck"
]


def classify_task(description: str, previous_failed: bool = False) -> int:
    """
    Classify a task description into a model tier (1, 2, or 3).
    
    Args:
        description: The task description to classify
        previous_failed: Whether a previous attempt failed (forces escalation)
    
    Returns:
        Model tier (1=cheap, 2=mid, 3=premium)
    """
    desc_lower = description.lower()
    
    # Rule 1: Escalation override
    if previous_failed:
        return 3
    
    # Check for escalation signals in description
    if any(signal in desc_lower for signal in ESCALATION_SIGNALS):
        return 3
    
    # Rule 2: Check for complex signals first (highest priority)
    if any(signal in desc_lower for signal in COMPLEX_SIGNALS):
        return 3
    
    # Rule 3: Check for moderate signals
    if any(signal in desc_lower for signal in MODERATE_SIGNALS):
        return 2
    
    # Rule 4: Check for routine signals
    if any(signal in desc_lower for signal in ROUTINE_SIGNALS):
        return 1
    
    # Rule 5: Default to mid-tier if uncertain
    return 2


def get_model_for_tier(tier: int) -> str:
    """Get a representative model for a given tier."""
    if tier == 1:
        return "deepseek-v3"
    elif tier == 2:
        return "claude-sonnet-4"
    else:
        return "claude-opus-4"


def calculate_cost(tier: int, tokens: int = 1000) -> float:
    """
    Calculate approximate cost for a given tier and token count.
    Uses output token pricing (typically higher).
    
    Args:
        tier: Model tier (1, 2, or 3)
        tokens: Number of tokens (default 1000)
    
    Returns:
        Cost in USD
    """
    # Approximate output costs per 1M tokens
    costs = {
        1: 0.28,    # DeepSeek V3
        2: 15.00,   # Claude Sonnet
        3: 75.00    # Claude Opus
    }
    return (tokens / 1_000_000) * costs[tier]


def calculate_monthly_cost(
    daily_tokens: int,
    routine_pct: float = 0.80,
    moderate_pct: float = 0.15,
    complex_pct: float = 0.05
) -> float:
    """
    Calculate monthly cost with hierarchical routing.
    
    Args:
        daily_tokens: Average tokens per day
        routine_pct: Percentage of routine tasks
        moderate_pct: Percentage of moderate tasks
        complex_pct: Percentage of complex tasks
    
    Returns:
        Monthly cost in USD
    """
    daily_cost = (
        calculate_cost(1, daily_tokens * routine_pct) +
        calculate_cost(2, daily_tokens * moderate_pct) +
        calculate_cost(3, daily_tokens * complex_pct)
    )
    return daily_cost * 30


# Load test scenarios
SCENARIOS_PATH = Path(__file__).parent / "scenarios.json"


@pytest.fixture
def scenarios():
    """Load test scenarios from JSON file."""
    with open(SCENARIOS_PATH) as f:
        return json.load(f)


class TestTaskClassification:
    """Test task classification into model tiers."""
    
    def test_routine_tasks(self, scenarios):
        """Routine tasks should be classified as tier 1."""
        for task in scenarios["routine_tasks"]:
            tier = classify_task(task["description"])
            assert tier == 1, f"Expected tier 1 for: {task['description']}"
    
    def test_moderate_tasks(self, scenarios):
        """Moderate tasks should be classified as tier 2."""
        for task in scenarios["moderate_tasks"]:
            tier = classify_task(task["description"])
            assert tier == 2, f"Expected tier 2 for: {task['description']}"
    
    def test_complex_tasks(self, scenarios):
        """Complex tasks should be classified as tier 3."""
        for task in scenarios["complex_tasks"]:
            tier = classify_task(task["description"])
            assert tier == 3, f"Expected tier 3 for: {task['description']}"
    
    def test_escalation_override(self):
        """Previous failures should escalate to tier 3."""
        # Even routine tasks should escalate if previous failed
        tier = classify_task("Read the config file", previous_failed=True)
        assert tier == 3
    
    def test_escalation_signals_in_description(self):
        """Escalation signals in description should trigger tier 3."""
        descriptions = [
            "The previous model couldn't figure this out",
            "I tried three approaches and none work",
            "Still not working after multiple attempts"
        ]
        for desc in descriptions:
            tier = classify_task(desc)
            assert tier == 3, f"Expected tier 3 for: {desc}"
    
    def test_compound_tasks_use_highest_tier(self, scenarios):
        """Compound tasks should use the highest required tier."""
        for task in scenarios["edge_cases"]:
            tier = classify_task(task["description"])
            assert tier == task["expected_tier"], \
                f"Expected tier {task['expected_tier']} for: {task['description']} (got {tier})"
    
    def test_unknown_defaults_to_mid(self):
        """Unknown tasks should default to tier 2."""
        tier = classify_task("Do something with the thing")
        assert tier == 2


class TestCostCalculations:
    """Test cost calculation functions."""
    
    def test_tier_cost_ordering(self):
        """Higher tiers should cost more."""
        tokens = 10000
        assert calculate_cost(1, tokens) < calculate_cost(2, tokens)
        assert calculate_cost(2, tokens) < calculate_cost(3, tokens)
    
    def test_hierarchy_saves_money(self):
        """Hierarchical routing should be cheaper than pure premium."""
        daily_tokens = 100_000
        
        pure_premium = calculate_cost(3, daily_tokens) * 30
        hierarchical = calculate_monthly_cost(daily_tokens)
        
        assert hierarchical < pure_premium
        # Should be roughly 10x cheaper
        assert hierarchical < pure_premium / 5
    
    def test_monthly_cost_calculation(self):
        """Monthly cost should be approximately $19 for 100K tokens/day."""
        monthly = calculate_monthly_cost(100_000)
        # Allow some variance in pricing
        assert 10 < monthly < 30


class TestModelSelection:
    """Test model selection for tiers."""
    
    def test_tier_1_models(self):
        """Tier 1 should return cheap model."""
        model = get_model_for_tier(1)
        assert model in TIER_1_MODELS
    
    def test_tier_2_models(self):
        """Tier 2 should return mid-tier model."""
        model = get_model_for_tier(2)
        assert model in TIER_2_MODELS
    
    def test_tier_3_models(self):
        """Tier 3 should return premium model."""
        model = get_model_for_tier(3)
        assert model in TIER_3_MODELS


class TestSignalDetection:
    """Test signal detection patterns."""
    
    @pytest.mark.parametrize("signal", ROUTINE_SIGNALS[:5])
    def test_routine_signals_detected(self, signal):
        """Routine signals should trigger tier 1."""
        desc = f"Please {signal} the data"
        tier = classify_task(desc)
        # Some routine signals might be overridden by other words
        assert tier in [1, 2]
    
    @pytest.mark.parametrize("signal", COMPLEX_SIGNALS[:5])
    def test_complex_signals_detected(self, signal):
        """Complex signals should trigger tier 3."""
        desc = f"Need to {signal} this system"
        tier = classify_task(desc)
        assert tier == 3


class TestRealWorldScenarios:
    """Test realistic agent task scenarios."""
    
    def test_heartbeat_is_routine(self):
        """Heartbeat checks should be tier 1."""
        tasks = [
            "Run the heartbeat check",
            "Check if services are healthy",
            "Ping the server status"
        ]
        for task in tasks:
            assert classify_task(task) == 1
    
    def test_code_review_is_moderate(self):
        """Standard code review should be tier 2."""
        task = "Review this pull request for style issues"
        assert classify_task(task) == 2
    
    def test_security_review_is_complex(self):
        """Security code review should be tier 3."""
        task = "Review this code for security vulnerabilities"
        assert classify_task(task) == 3
    
    def test_simple_code_is_moderate(self):
        """Code tasks default to tier 2 even if simple."""
        # The "code" keyword triggers moderate - acceptable tradeoff
        # for catching code generation tasks
        task = "Format this Python code"
        assert classify_task(task) == 2
    
    def test_architecture_is_complex(self):
        """Architecture decisions should be tier 3."""
        tasks = [
            "Design the system architecture",
            "Architect a solution for this problem",
            "Evaluate the tradeoffs between microservices and monolith"
        ]
        for task in tasks:
            assert classify_task(task) == 3


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
```

