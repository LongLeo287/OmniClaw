---
id: materials
type: knowledge
owner: OA_Triage
---
# materials
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Materials Simulation Skills

[![CI](https://github.com/heshamfs/materials-simulation-skills/actions/workflows/ci.yml/badge.svg)](https://github.com/heshamfs/materials-simulation-skills/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)
[![Agent Skills](https://img.shields.io/badge/Agent_Skills-standard-orange.svg)](https://agentskills.io)
[![Python 3.10-3.12](https://img.shields.io/badge/Python-3.10--3.12-blue.svg)](https://www.python.org/)

**Open-source [Agent Skills](https://agentskills.io) for computational materials science and numerical simulation workflows.**

Give your AI coding agent domain expertise in numerical methods, simulation best practices, and scientific computing -- without re-explaining the same concepts every session. Skills are portable across Claude Code, Codex, Gemini CLI, Cursor, VS Code Copilot, and [20+ other compatible tools](https://agentskills.io).

---

## Table of Contents

- [The Problem](#the-problem)
- [The Solution](#the-solution)
- [What's Inside](#whats-inside)
  - [Core Numerical Skills](#core-numerical-skills-skillscore-numerical)
  - [Simulation Workflow Skills](#simulation-workflow-skills-skillssimulation-workflow)
  - [HPC Deployment Skills](#hpc-deployment-skills-skillshpc-deployment)
  - [Ontology Skills](#ontology-skills-skillsontology)
- [How Skills Work](#how-skills-work)
- [Security](#security)
- [Quick Start](#quick-start)
- [Adding Skills to Your Agent](#adding-skills-to-your-agent)
  - [Claude Code](#claude-code)
  - [Gemini CLI](#gemini-cli)
  - [OpenAI Codex](#openai-codex)
  - [VS Code / GitHub Copilot](#vs-code--github-copilot)
  - [Cursor](#cursor)
  - [Other Agents](#other-agents)
- [Repository Layout](#repository-layout)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

---

## The Problem

Simulation engineers repeat the same guidance to AI agents constantly: *"Check the CFL number before running," "Use Richardson extrapolation for grid convergence," "Exit code 2 means bad input."* General-purpose agents lack the domain knowledge to run reliable numerical simulations without heavy hand-holding.

## The Solution

This project packages that domain knowledge into **skills** -- structured folders of instructions, scripts, and references that agents discover automatically and load on demand. Each skill teaches an agent a specific simulation competency, backed by validated Python scripts that produce reproducible results.

```text
You: Check if dt=0.001 is stable for my advection problem with v=2.0 m/s and dx=0.01.

Agent: I'll use the numerical-stability skill to check this.
       [runs cfl_checker.py --dx 0.01 --dt 0.001 --velocity 2.0 --json]

       CFL number = 0.2 (limit: 1.0) -- stable.
       Recommended max dt = 0.005 with safety factor 1.0.
```

No prompt engineering. No copy-pasting formulas. The agent finds the right skill, runs the script, and interprets the results.

---

## What's Inside

**17 skills** | **67 scripts** | **932 tests** | **78 eval cases** | **312 assertions** | Cross-platform CI on Python 3.10-3.12

### Core Numerical Skills (`skills/core-numerical/`)

Foundational numerical methods and analysis tools.

| Skill | What it does |
|-------|-------------|
| `numerical-stability` | CFL/Fourier analysis, von Neumann stability, stiffness detection, matrix conditioning |
| `time-stepping` | Time integrator selection, adaptive step-size control, output scheduling |
| `mesh-generation` | Mesh quality metrics (aspect ratio, skewness, orthogonality), refinement guidance |
| `convergence-study` | Grid/time convergence analysis, Richardson extrapolation, GCI calculation |
| `numerical-integration` | Quadrature rule selection, error estimation, adaptive stepping |
| `differentiation-schemes` | Finite difference stencil generation, truncation error analysis, scheme comparison |
| `linear-solvers` | Iterative/direct solver selection, preconditioner advice, convergence diagnostics |
| `nonlinear-solvers` | Newton/quasi-Newton/fixed-point selection, globalization strategies, convergence diagnostics |

### Simulation Workflow Skills (`skills/simulation-workflow/`)

End-to-end simulation management and automation.

| Skill | What it does |
|-------|-------------|
| `simulation-validator` | Pre-flight checks, runtime log monitoring, post-flight validation |
| `parameter-optimization` | DOE sampling (LHS, factorial), optimizer selection, sensitivity analysis |
| `simulation-orchestrator` | Parameter sweeps, batch campaign management, result aggregation |
| `post-processing` | Field extraction, time series analysis, derived quantity computation |
| `performance-profiling` | Timing analysis, scaling studies, memory profiling, bottleneck detection |

### HPC Deployment Skills (`skills/hpc-deployment/`)

Deployment and job submission tooling for running simulations on HPC systems.

| Skill | What it does |
|-------|-------------|
| `slurm-job-script-generator` | Generate `sbatch` scripts, sanity-check resource requests, and standardize `#SBATCH` directives |

### Ontology Skills (`skills/ontology/`)

Materials science ontology understanding, mapping, and validation.

| Skill | What it does |
|-------|-------------|
| `ontology-explorer` | Parse OWL/XML ontologies, browse class hierarchies, look up properties, search concepts (CMSO, ASMO, OCDO ecosystem) |
| `ontology-mapper` | Map natural-language materials terms and crystal parameters to ontology classes and properties (CMSO, ASMO) |
| `ontology-validator` | Validate annotations against ontology constraints, check completeness, verify relationship domain/range |

---

## How Skills Work

Skills follow the open [Agent Skills standard](https://agentskills.io/specification). Each skill is a folder with three tiers of content, loaded progressively to keep context efficient:

```
skills/core-numerical/numerical-stability/
    SKILL.md              # Instructions + YAML metadata (loaded when skill triggers)
    scripts/              # Python CLI tools (executed for reproducible results)
        cfl_checker.py
        von_neumann_analyzer.py
        matrix_condition.py
        stiffness_detector.py
    references/           # Deep domain knowledge (loaded only when needed)
        stability_criteria.md
        common_pitfalls.md
        scheme_catalog.md
    evals/                # Evaluation suite per agentskills.io spec
        evals.json        # Test cases with prompts, assertions, expected outputs
    CHANGELOG.md          # Version history
```

1. **Discovery** -- The agent sees each skill's name and description at startup (~100 tokens per skill)
2. **Activation** -- When a task matches, the agent loads the full `SKILL.md` with decision guidance, workflows, and CLI examples
3. **Execution** -- Scripts run as subprocesses with `--json` output for structured, parseable results

All scripts are standalone CLI tools with `--help`, a pure-function core for testing, and consistent error handling (exit code 2 for bad input, 1 for runtime errors).

---

## Security

All skills are hardened against the [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/), with 75 dedicated security tests. Key safeguards:

- **No shell access by default** -- Skills use `allowed-tools: Read, Write, Grep, Glob` (no `Bash`), preventing the agent from executing arbitrary commands when processing untrusted data
- **Input validation at every boundary** -- Numeric parameters are bounds-checked and validated as finite; string inputs (parameter names, field names, term names) are validated against regex allowlists
- **Safe file loading** -- All JSON/CSV/NPY loaders enforce file size limits (100-500 MB) and structure validation (dict root required); `np.load()` uses `allow_pickle=False`
- **No `eval()`/`exec()`** -- Region condition parsing uses strict regex matching, never dynamic code execution
- **Prompt injection resistance** -- String values extracted from external files are truncated and stripped of control characters before surfacing to the agent; phase names from logs are sanitized
- **Command construction safety** -- `shlex.quote()` escapes paths interpolated into shell commands; command templates are validated against a shell-operator denylist
- **ReDoS prevention** -- User-supplied regex patterns are length-capped and checked for catastrophic backtracking constructs

Each skill documents its specific safeguards in a **Security** section within its `SKILL.md`, with standardized subsections for Input Validation, File Access, Tool Restrictions, and Safety Measures.

### Security Risk Tiers

Every skill is classified by its tool access surface:

| Tier | Criteria | Skills |
|------|----------|-------|
| **HIGH** | Has `Bash` (can execute scripts) | 9 skills — numerical-stability, time-stepping, convergence-study, differentiation-schemes, nonlinear-solvers, ontology-explorer, ontology-validator, simulation-validator, slurm-job-script-generator |
| **MEDIUM** | Has `Write` but no `Bash` | 7 skills — linear-solvers, mesh-generation, numerical-integration, parameter-optimization, performance-profiling, post-processing, simulation-orchestrator |
| **LOW** | Read/Grep/Glob only | 1 skill — ontology-mapper |

---

## Quality & Evaluation

Every skill includes an evaluation suite (`evals/evals.json`) following the [agentskills.io evaluation spec](https://agentskills.io/skill-creation/evaluating-skills). Each suite contains 4-5 test cases with realistic prompts, expected outputs, and verifiable assertions.

**Current metrics:** 78 eval test cases | 312 assertions | All 17 skills evaluated

The CI pipeline validates:
- SKILL.md frontmatter (name, description < 1024 chars, metadata block)
- Eval suite completeness (every skill has evals.json with ≥ 3 test cases)
- Security section presence (all skills must have `## Security`)
- Changelog existence (all skills must have CHANGELOG.md)

---

## Quick Start

### Install

```bash
git clone https://github.com/heshamfs/materials-simulation-skills.git
cd materials-simulation-skills
pip install -r requirements-dev.txt
```

### Run the test suite

```bash
python -m pytest tests/ -v --tb=short          # All 932 tests
python -m pytest tests/unit -v --tb=short       # Unit tests only
python -m pytest tests/integration -v           # Integration tests only
```

---

## Adding Skills to Your Agent

These skills follow the open [Agent Skills standard](https://agentskills.io) and work across 20+ AI coding tools. Choose your agent below.

### Claude Code

Copy individual skills (or the whole `skills/` tree) into your personal or project skills directory:

```bash
# Personal (available across all projects)
cp -r skills/core-numerical/numerical-stability ~/.claude/skills/numerical-stability

# Project-level (committed to version control)
cp -r skills/core-numerical/numerical-stability .claude/skills/numerical-stability
```

Or clone the whole repo and point Claude Code at it with `--add-dir`:

```bash
claude --add-dir /path/to/materials-simulation-skills/skills
```

Verify with: `What skills are available?` or type `/` to see skills in the autocomplete menu.

See the [Claude Code skills docs](https://code.claude.com/docs/en/skills) for more details.

### Gemini CLI

Install directly from the repo, or copy skills into your Gemini skills directory:

```bash
# User-scoped (available across all workspaces)
cp -r skills/core-numerical/numerical-stability ~/.gemini/skills/numerical-stability

# Workspace-scoped (project-specific)
cp -r skills/core-numerical/numerical-stability .gemini/skills/numerical-stability
```

Verify with: `gemini skills list`

See the [Gemini CLI skills docs](https://geminicli.com/docs/cli/skills/) for more details.

### OpenAI Codex

Copy skills into one of the Codex skills directories:

```bash
# User-scoped
cp -r skills/core-numerical/numerical-stability ~/.agents/skills/numerical-stability

# Repository-scoped
cp -r skills/core-numerical/numerical-stability .agents/skills/numerical-stability
```

Restart Codex after adding skills. Use `/skills` or `$` to invoke skills by name.

See the [Codex skills docs](https://developers.openai.com/codex/skills) for more details.

### VS Code / GitHub Copilot

Copy skills into your workspace or personal skills directory:

```bash
# Workspace (committed to version control)
cp -r skills/core-numerical/numerical-stability .github/skills/numerical-stability

# Personal (across all workspaces)
cp -r skills/core-numerical/numerical-stability ~/.copilot/skills/numerical-stability
```

Type `/skills` in the chat input to see and invoke available skills.

See the [VS Code skills docs](https://code.visualstudio.com/docs/copilot/customization/agent-skills) for more details.

### Cursor

Copy skills into a `skills/` directory at your project root:

```bash
cp -r skills/core-numerical/numerical-stability skills/numerical-stability
```

Cursor's MCP server auto-discovers skills from the `skills/` directory.

### Other Agents

Any agent that supports the [Agent Skills standard](https://agentskills.io) can use these skills. The general pattern:

1. Copy the skill directory (containing `SKILL.md`, `scripts/`, `references/`) into your agent's skills folder
2. The agent discovers the skill by its `name` and `description` in the YAML frontmatter
3. Mention the skill by name or ask a task that matches its description

```text
Use numerical-stability to check a proposed dt for my phase-field run.
```

The agent loads the skill's instructions, runs the appropriate scripts, and interprets the results.

---

## Repository Layout

```
skills/
    core-numerical/          # 8 skills: stability, solvers, meshing, convergence, ...
    simulation-workflow/     # 5 skills: validation, optimization, orchestration, ...
    hpc-deployment/          # 1 skill: SLURM job script generation
    ontology/                # 3 skills: ontology exploration, mapping, validation
    <each-skill>/
        SKILL.md             # Instructions + YAML frontmatter (with metadata block)
        scripts/             # Python CLI tools with --json output
        references/          # Domain knowledge documents
        evals/evals.json     # Evaluation suite (prompts, assertions)
        CHANGELOG.md         # Version history
tests/
    unit/                    # Pure-function tests via load_module()
    integration/             # Subprocess + JSON schema validation
    fixtures/                # Sample data files for CI smoke tests
.github/
    workflows/ci.yml         # Cross-platform CI + quality validation
    ISSUE_TEMPLATE/          # Bug reports, skill proposals
    PULL_REQUEST_TEMPLATE.md # PR checklist
```

---

## Contributing

We welcome contributions of all kinds -- new skills, bug fixes, documentation, and tests. The project is designed to grow from 17 skills across 4 categories into a broader collection spanning materials physics, ve
... [TRUNCATED]
```

### File: requirements.txt
```txt
# Core dependencies for materials-simulation-skills
# Install with: pip install -r requirements.txt

numpy>=1.21

```

### File: CONTRIBUTING.md
```md
# Contributing to Materials Simulation Skills

Thanks for your interest in contributing! This project provides open-source **Agent Skills** for computational materials science and numerical simulation workflows. Each skill is a structured folder (SKILL.md + scripts + references) that AI agents discover by name and load on demand.

Our goal is to grow from the current 17 skills across 4 categories to approximately **38 skills across 8 categories**, covering everything from core numerical methods to materials physics, HPC deployment, and robustness techniques. Every contribution -- whether a new skill, a bug fix, improved documentation, or better tests -- helps the community build more reliable simulation workflows.

All contributors are expected to follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).

---

## Ways to Contribute

| Contribution | Description | Difficulty |
|-------------|-------------|------------|
| Report a bug | File an issue using the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md) | Beginner |
| Fix a bug | Reproduce the issue, add a test, submit a fix | Beginner |
| Improve documentation | Fix typos, clarify SKILL.md sections, expand references | Beginner |
| Add tests | Increase coverage with unit, integration, or property tests | Intermediate |
| Propose a skill | Open a [skill proposal](.github/ISSUE_TEMPLATE/skill_proposal.md) issue | Intermediate |
| Implement a planned skill | Pick a skill from the [taxonomy](#skill-taxonomy--roadmap) and implement it | Advanced |
| Improve infrastructure | CI workflows, test utilities, cross-platform fixes | Advanced |

---

## Getting Started

### 1. Fork and Clone

```bash
git clone https://github.com/heshamfs/materials-simulation-skills.git
cd materials-simulation-skills
```

### 2. Set Up Your Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows
pip install -r requirements-dev.txt
```

### 3. Run Tests

```bash
python -m pytest tests/ -v --tb=short       # All tests
python -m pytest tests/unit -v --tb=short    # Unit tests only
python -m pytest tests/integration -v        # Integration tests only
```

### 4. Create a Branch

Use one of these naming conventions:

| Branch prefix | Use for |
|--------------|---------|
| `skill/name` | New skill (e.g. `skill/elasticity-mechanics`) |
| `fix/desc` | Bug fix (e.g. `fix/cfl-nan-handling`) |
| `docs/desc` | Documentation changes |
| `test/desc` | Test additions or improvements |
| `infra/desc` | CI, build, or tooling changes |

---

## Creating a New Skill

### Step 1: Directory Layout

Create the following structure under the appropriate category:

```
skills/{category}/{skill-name}/
    SKILL.md
    scripts/
        your_script.py
    references/
        domain_guide.md
```

The available categories are listed in the [Skill Taxonomy](#skill-taxonomy--roadmap) section.

**Naming rules** (per the [Agent Skills specification](https://agentskills.io/specification)):
- Lowercase letters, numbers, and hyphens only (e.g. `mesh-generation`, `cfl-checker`)
- Max 64 characters, no consecutive hyphens (`--`), cannot start or end with a hyphen
- The `name` field in SKILL.md frontmatter **must match** the directory name
- Must not contain reserved words (`anthropic`, `claude`)

### Step 2: Write SKILL.md

Every SKILL.md starts with YAML frontmatter and contains specific sections. Use this template:

```markdown
---
name: your-skill-name
description: >
  Describes what this skill does and when to use it. Write in third person.
  Include specific keywords that help agents identify relevant tasks.
  Example: "Compute CFL and Fourier numbers for explicit time-stepping schemes.
  Use when selecting time steps, diagnosing numerical blow-up, or checking
  stability criteria for advection-diffusion problems."
allowed-tools: Read, Bash, Write, Grep, Glob
# Optional fields:
# license: Apache-2.0
# compatibility: Requires numpy; designed for Claude Code or similar agents
# metadata:
#   author: your-name
#   version: "1.0"
---

# Your Skill Name

## Goal

What problem does this skill solve? One or two sentences.

## Requirements

- Python 3.8+
- NumPy
- List any other dependencies

## Inputs to Gather

| Input | Description | Example |
|-------|-------------|---------|
| `param_name` | What it represents | `1.0` |

## Decision Guidance

Help the agent choose between approaches. Use decision trees:

\```
Is condition A true?
+-- YES -> Approach 1
+-- NO  -> Approach 2
\```

## Script Outputs

| Script | Output Key | Description |
|--------|-----------|-------------|
| `your_script.py` | `results.metric` | What it means |

## Workflow

1. Gather inputs from the user
2. Run script with appropriate parameters
3. Interpret results and advise

## CLI Examples

\```bash
python skills/{category}/{skill-name}/scripts/your_script.py \
  --param 1.0 --json
\```

## Conversational Workflow Example

> **User**: I need help with [problem].
>
> **Agent**: I will use the your-skill-name skill. Let me gather some inputs...

## Error Handling

| Error | Cause | Resolution |
|-------|-------|------------|
| `ValueError: param must be positive` | Negative input | Use a positive value |

## Limitations

- Known limitation 1
- Known limitation 2

## References

- Author, "Title," Journal, Year. DOI: ...
- Relevant textbook or standard

## Version History

- v1 (YYYY-MM-DD): Initial implementation
```

**Notes:**
- The `description` in the frontmatter is critical -- agents use it to decide whether to load the skill. Always write in **third person** and describe both *what* the skill does and *when* to use it
- Keep SKILL.md body **under 500 lines**. The Agent Skills standard uses progressive disclosure: only `name` and `description` are loaded at startup (~100 tokens); the full SKILL.md body is loaded on activation; `references/` and `scripts/` are loaded only when needed
- Keep reference files **one level deep** from SKILL.md -- avoid chains where one reference points to another reference
- The `allowed-tools` field controls which tools the agent can use when the skill is active
- Always use **forward slashes** in file paths (`references/guide.md`), even on Windows

### Step 3: New Skill Checklist

Before submitting your PR, verify every item:

- [ ] Skill directory is under the correct category
- [ ] Directory name matches the `name` field in SKILL.md frontmatter
- [ ] Name follows conventions (lowercase, hyphens, max 64 chars, no reserved words)
- [ ] `SKILL.md` has YAML frontmatter with `name`, `description`, and `allowed-tools`
- [ ] Description is third-person and says both *what* the skill does and *when* to use it
- [ ] `SKILL.md` body is under 500 lines (detailed content goes in `references/`)
- [ ] `SKILL.md` contains all 12 sections (Goal through Version History)
- [ ] At least one script in `scripts/`
- [ ] Scripts use `argparse` with `--help` documentation
- [ ] Scripts support `--json` flag for structured output
- [ ] Scripts have a pure-function core (importable for testing)
- [ ] Scripts reject NaN/Inf inputs with `ValueError`
- [ ] Scripts use exit code 2 for validation errors, exit code 1 for runtime errors
- [ ] Unit tests in `tests/unit/test_{script_name}.py`
- [ ] Integration tests in `tests/integration/`
- [ ] Reference docs placed in `references/` directory
- [ ] Skill added to the top-level `README.md`
- [ ] All file paths use forward slashes (even on Windows)
- [ ] Reference files are one level deep from SKILL.md (no nested chains)
- [ ] All tests pass: `python -m pytest tests/ -v --tb=short`
- [ ] Scripts compile: `python -m py_compile scripts/your_script.py`
- [ ] (Optional) Validate with: `skills-ref validate ./skills/{category}/{skill-name}`

---

## Script Conventions

All scripts are standalone CLI tools. Follow this annotated template:

```python
#!/usr/bin/env python3
"""Short description of what this script computes."""

import argparse
import json
import math
import sys
from typing import Dict, Optional


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Describe the script purpose.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--param", type=float, required=True, help="Description")
    parser.add_argument("--json", action="store_true", help="Emit JSON output")
    return parser.parse_args()


def compute(param: float) -> Dict[str, object]:
    """Pure function: all logic here, no I/O. This is what tests import."""
    # Validate inputs
    if not math.isfinite(param):
        raise ValueError("param must be finite (no NaN or Inf)")
    if param <= 0:
        raise ValueError("param must be positive")

    # Compute results
    result_value = param * 2  # Replace with real logic

    return {
        "metric": result_value,
        "notes": [],
    }


def main() -> None:
    args = parse_args()
    try:
        result = compute(param=args.param)
    except ValueError as exc:
        if args.json:
            json.dump({"error": str(exc)}, sys.stdout)
            print()
        else:
            print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)

    if args.json:
        output = {
            "inputs": {"param": args.param},
            "results": result,
        }
        json.dump(output, sys.stdout, indent=2)
        print()
    else:
        print(f"Metric: {result['metric']}")


if __name__ == "__main__":
    main()
```

### Key Rules

- **NumPy only**: Scripts should only require `numpy`. Use `scipy` or `scikit-learn` only when truly necessary and document it
- **Exit codes**: Use `sys.exit(2)` for validation errors (bad input), `sys.exit(1)` for unexpected runtime errors
- **NaN/Inf rejection**: Always check `math.isfinite()` on numeric inputs before computation
- **JSON envelope**: When `--json` is active, output follows `{"inputs": {...}, "results": {...}}`; errors emit `{"error": "message"}`
- **Pure-function core**: The `compute()` function must be importable and testable without CLI parsing
- **No interactive input**: Scripts must work in non-interactive (subprocess) mode

---

## Testing Requirements

Tests live in `tests/` with this structure:

```
tests/
    unit/
        _utils.py           # load_module() helper
        test_your_script.py
    integration/
        _schema.py          # assert_schema() helper
        test_cli_your_skill.py
    fixtures/               # Sample data files for CI smoke tests
```

### Unit Tests

Unit tests import the pure-function core directly using `load_module()`:

```python
import unittest

from tests.unit._utils import load_module


class TestYourScript(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module(
            "your_script",
            "skills/{category}/{skill-name}/scripts/your_script.py",
        )

    def test_basic_case(self):
        result = self.mod.compute(param=1.0)
        self.assertAlmostEqual(result["metric"], 2.0, places=6)

    def test_validation_error(self):
        with self.assertRaises(ValueError):
            self.mod.compute(param=-1.0)

    def test_nan_rejection(self):
        with self.assertRaises(ValueError):
            self.mod.compute(param=float("nan"))

    def test_inf_rejection(self):
        with self.assertRaises(ValueError):
            self.mod.compute(param=float("inf"))
```

### Integration Tests

Integration tests run scripts as subprocesses and validate JSON output:

```python
import json
import subprocess
import sys
import unittest
from pathlib import Path

from tests.integration._schema import assert_schema

ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "skills" / "{category}" / "{skill-name}" / "scripts"


class TestCliYourSkill(unittest.TestCase):
    def run_cmd(self, args):
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_json_output(self):
        result = self.run_cmd([
            str(SCRIPTS / "your_script.py"),
            "--param", "1.0",
            "--json",
        ])
        self.assertEqual(result.returncode, 0)
        data = json.loads(result.stdout)
        assert_schema(data, {
            "inputs": {"param": float},
            "results": {"metric": (int, float)},
        })

    def test_validation_error_exit_code(self):
        result = self.run_cmd([
            str(SCRIPTS / "your_script.py"),
            "--param", "-1.0",
            "--json",
        ])
        self.assertEqual(result.returncode, 2)
        data = json.loads(result.stdout)
        self.assertIn("error", data)
```

### Property Tests (Optional but Encouraged)

Use `hypothesis` for property-based testing:

```python
import unittest

from hypothesis import given, settings
from hypothesis import strategies as st

from tests.unit._utils import load_module


class TestYourScriptProperties(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.mod = load_module(
            "your_script",
            "skills/{category}/{skill-name}/scripts/your_script.py",
        )

    @given(param=st.floats(min_value=0.001, max_value=1e6))
    @settings(max_examples=200)
    def test_output_always_positive(self, param):
        result = self.mod.compute(param=param)
        self.assertGreater(result["metric"], 0)
```

### Running Tests

```bash
# All tests
python -m pytest tests/ -v --tb=short

# Single test file
python -m pytest tests/unit/test_your_script.py -v

# Single test method
python -m pytest tests/unit/test_your_script.py::TestYourScript::test_basic_case -v

# With coverage (if installed)
python -m pytest tests/ --cov=skills --cov-report=term-missing
```

---

## Pull Request Guidelines

### Before Submitting

1. **One skill per PR** -- keep PRs focused and reviewable
2. **Link related issues** -- reference the skill proposal or bug report
3. **All CI checks must pass** -- the PR template includes a checklist
4. **Self-review your diff** -- read through your own changes before requesting review

### What Reviewers Check

- **SKILL.md completeness**: All 12 sections present with useful content
- **Script patterns**: argparse, `--json`, pure-function core, error handling
- **Test coverage**: Unit tests for core logic, integration tests for CLI, edge cases for invalid input
- **Cross-platform compatibility**: No OS-specific paths, commands, or assumptions
- **Documentation**: References in `references/`, README updated

### Review Process

1. A maintainer will review within a few days
2. Address feedback by pushing new commits (do not force-push during review)
3. Once approved, a maintainer will merge the PR

---

## Skill Taxonomy & Roadmap

The project is organized into categories. The first four categories are established with 17 skills; the remaining 
... [TRUNCATED]
```

### File: requirements-dev.txt
```txt
# Development dependencies for materials-simulation-skills
# Install with: pip install -r requirements-dev.txt

-r requirements.txt

# Testing
pytest>=7.0
pytest-cov>=4.0
hypothesis>=6.0

# Optional for advanced features
scipy>=1.7
scikit-learn>=1.0

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Summary

<!-- Brief description of the changes in this PR. -->

## Type of Change

- [ ] New skill
- [ ] Bug fix
- [ ] Documentation
- [ ] Tests
- [ ] CI / infrastructure

## Related Issues

<!-- Link related issues: Fixes #123, Closes #456, Related to #789 -->

---

## Checklist

### All PRs

- [ ] Tests pass locally (`python -m pytest tests/ -v --tb=short`)
- [ ] No new dependencies beyond numpy (or justified in PR description)
- [ ] Works cross-platform (no OS-specific paths, forward slashes only)
- [ ] Files use ASCII only (unless existing content requires Unicode)
- [ ] Lint passes (`python -m py_compile` on changed scripts)

### New Skill PRs

- [ ] Skill directory follows `skills/{category}/{skill-name}/` layout
- [ ] Directory name matches the `name` field in SKILL.md frontmatter
- [ ] Name follows conventions (lowercase, hyphens, max 64 chars, no reserved words)
- [ ] `SKILL.md` has YAML frontmatter (`name`, `description`, `allowed-tools`)
- [ ] Description is third-person, says what the skill does and when to use it
- [ ] `SKILL.md` body is under 500 lines (details go in `references/`)
- [ ] `SKILL.md` contains all required sections (Goal, Requirements, Inputs to Gather, Decision Guidance, Script Outputs, Workflow, CLI Examples, Conversational Workflow Example, Error Handling, Limitations, References, Version History)
- [ ] Scripts use `argparse` with `--help`
- [ ] Scripts support `--json` flag with `{"inputs": {...}, "results": {...}}` envelope
- [ ] Scripts have a pure-function core importable for testing
- [ ] Scripts reject NaN/Inf inputs with `ValueError`
- [ ] Scripts use exit code 2 for validation errors, 1 for runtime errors
- [ ] Unit tests added in `tests/unit/test_{script_name}.py`
- [ ] Integration tests added in `tests/integration/`
- [ ] Skill listed in top-level `README.md`
- [ ] Reference docs placed in `references/` (one level deep, no nested chains)
- [ ] Issue linked or skill proposal referenced

### Bug Fix PRs

- [ ] Reproducing test added before fix
- [ ] Fix verified against the reproducing test

```

### File: tests\__init__.py
```py


```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug Report
about: Report a bug in a skill script or test
title: "[Bug] "
labels: bug
---

## Skill / Script Affected

<!-- Which skill and script is this about? e.g. core-numerical/numerical-stability/scripts/cfl_checker.py -->

## Describe the Bug

<!-- A clear and concise description of what the bug is. -->

## Steps to Reproduce

```bash
# Paste the exact command or code that triggers the bug
python skills/core-numerical/numerical-stability/scripts/cfl_checker.py \
  --dx 0.1 --dt 0.01 --velocity 1.0 --json
```

## Expected Behavior

<!-- What you expected to happen. -->

## Actual Behavior

<!-- What actually happened. Include error messages or incorrect output. -->

## Environment

- **OS**: <!-- e.g. Ubuntu 22.04 / Windows 11 / macOS 14 -->
- **Python version**: <!-- e.g. 3.11.5 -->
- **NumPy version**: <!-- e.g. 1.26.0 -->
- **Commit or branch**: <!-- e.g. main @ abc1234 -->

## Additional Context

<!-- Any other context, screenshots, or log output. -->

```

### File: .github\ISSUE_TEMPLATE\skill_proposal.md
```md
---
name: Skill Proposal
about: Propose a new skill for the project
title: "[Skill Proposal] "
labels: skill-proposal, enhancement
---

## Skill Name

<!-- Use kebab-case, e.g. elasticity-mechanics -->

## Category

<!-- Check one: -->

- [ ] core-numerical
- [ ] simulation-workflow
- [ ] materials-physics
- [ ] verification-validation
- [ ] data-management
- [ ] hpc-deployment
- [ ] simulation-patterns
- [ ] robustness

## Description

<!-- One paragraph describing what this skill helps agents do. -->

## Use Cases

<!-- List 2-3 concrete scenarios where an agent would invoke this skill. -->

1.
2.
3.

## Proposed Scripts

| Script | Purpose | Key Inputs |
|--------|---------|------------|
| `script_name.py` | | |

## Domain Knowledge Required

<!-- What references/ docs would the skill need? Link textbooks, papers, or standards if applicable. -->

## Dependencies

- [x] NumPy only (preferred)
- [ ] Requires SciPy
- [ ] Requires scikit-learn
- [ ] Other: <!-- specify -->

## Prior Art

<!-- Are there existing tools, libraries, or papers that cover this domain? How would this skill differ? -->

## Implementation

- [ ] I would like to implement this skill myself
- [ ] I am looking for someone else to implement this

```

### File: tests\integration\test_cli_edge_cases.py
```py
import json
import subprocess
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "skills" / "core-numerical" / "numerical-stability" / "scripts"


class TestCliEdgeCases(unittest.TestCase):
    def run_cmd(self, args):
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_von_neumann_invalid_nk(self):
        cmd = [
            str(SCRIPTS / "von_neumann_analyzer.py"),
            "--coeffs",
            "0.5,0.5",
            "--nk",
            "1",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("nk must be > 1", result.stderr)

    def test_matrix_condition_non_finite(self):
        matrix_path = ROOT / "tests" / "integration" / "nan_matrix.txt"
        matrix_path.write_text("1 0\n0 nan\n")
        try:
            cmd = [
                str(SCRIPTS / "matrix_condition.py"),
                "--matrix",
                str(matrix_path),
            ]
            result = self.run_cmd(cmd)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("non-finite", result.stderr.lower())
        finally:
            matrix_path.unlink(missing_ok=True)

    def test_stiffness_detector_empty_eigs(self):
        cmd = [
            str(SCRIPTS / "stiffness_detector.py"),
            "--eigs=",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("eigs must be a comma-separated list", result.stderr)

    def test_cfl_invalid_dimensions(self):
        cmd = [
            str(SCRIPTS / "cfl_checker.py"),
            "--dx",
            "0.1",
            "--dt",
            "0.01",
            "--velocity",
            "1.0",
            "--dimensions",
            "0",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dimensions must be positive", result.stderr)

    def test_von_neumann_kmin_kmax(self):
        cmd = [
            str(SCRIPTS / "von_neumann_analyzer.py"),
            "--coeffs",
            "0.2,0.6,0.2",
            "--kmin",
            "1.0",
            "--kmax",
            "0.0",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("kmin must be < kmax", result.stderr)

    def test_matrix_condition_non_square(self):
        matrix_path = ROOT / "tests" / "integration" / "rect_matrix.txt"
        matrix_path.write_text("1 0 0\n0 1 0\n")
        try:
            cmd = [
                str(SCRIPTS / "matrix_condition.py"),
                "--matrix",
                str(matrix_path),
            ]
            result = self.run_cmd(cmd)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("matrix must be square", result.stderr.lower())
        finally:
            matrix_path.unlink(missing_ok=True)

    def test_matrix_condition_invalid_norm(self):
        matrix_path = ROOT / "tests" / "integration" / "square_matrix.txt"
        matrix_path.write_text("1 0\n0 2\n")
        try:
            cmd = [
                str(SCRIPTS / "matrix_condition.py"),
                "--matrix",
                str(matrix_path),
                "--norm",
                "bad",
            ]
            result = self.run_cmd(cmd)
            self.assertNotEqual(result.returncode, 0)
            self.assertIn("norm must be one of", result.stderr.lower())
        finally:
            matrix_path.unlink(missing_ok=True)

    def test_error_norm_missing_scale(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "error_norm.py"
            ),
            "--error",
            "0.1,0.2",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("solution or scale must be provided", result.stderr)

    def test_adaptive_step_negative_dt(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "adaptive_step_controller.py"
            ),
            "--dt",
            "-0.1",
            "--error-norm",
            "0.5",
            "--order",
            "2",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dt must be a positive finite number", result.stderr)

    def test_integrator_selector_invalid_dimension(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "integrator_selector.py"
            ),
            "--dimension",
            "0",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dimension must be positive", result.stderr)

    def test_imex_split_missing_terms(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "imex_split_planner.py"
            ),
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Provide at least one", result.stderr)

    def test_splitting_error_invalid_dt(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "splitting_error_estimator.py"
            ),
            "--dt",
            "0",
            "--commutator-norm",
            "1",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dt must be a positive finite number", result.stderr)

    def test_timestep_planner_invalid_dt(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "time-stepping"
                / "scripts"
                / "timestep_planner.py"
            ),
            "--dt-target",
            "-1",
            "--dt-limit",
            "1e-3",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dt_target", result.stderr)

    def test_output_schedule_invalid_interval(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "time-stepping"
                / "scripts"
                / "output_schedule.py"
            ),
            "--t-start",
            "0",
            "--t-end",
            "1",
            "--interval",
            "0",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("interval must be positive", result.stderr)

    def test_checkpoint_planner_invalid_runtime(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "time-stepping"
                / "scripts"
                / "checkpoint_planner.py"
            ),
            "--run-time",
            "0",
            "--checkpoint-cost",
            "10",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("run_time", result.stderr)

    def test_stencil_generator_invalid_order(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "differentiation-schemes"
                / "scripts"
                / "stencil_generator.py"
            ),
            "--order",
            "0",
            "--accuracy",
            "2",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("order must be positive", result.stderr)

    def test_scheme_selector_invalid_flags(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "differentiation-schemes"
                / "scripts"
                / "scheme_selector.py"
            ),
            "--smooth",
            "--discontinuous",
            "--order",
            "1",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("smooth and discontinuous", result.stderr)

    def test_truncation_error_invalid_dx(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "differentiation-schemes"
                / "scripts"
                / "truncation_error.py"
            ),
            "--dx",
            "0",
            "--accuracy",
            "2",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dx must be positive", result.stderr)

    def test_grid_sizing_invalid_length(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "mesh-generation"
                / "scripts"
                / "grid_sizing.py"
            ),
            "--length",
            "0",
            "--resolution",
            "10",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("length must be positive", result.stderr)

    def test_mesh_quality_invalid(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "mesh-generation"
                / "scripts"
                / "mesh_quality.py"
            ),
            "--dx",
            "0",
            "--dy",
            "1",
            "--dz",
            "1",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("must be a finite positive number", result.stderr)

    def test_preflight_invalid_config(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "simulation-validator"
                / "scripts"
                / "preflight_checker.py"
            ),
            "--config",
            "missing.json",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("Config not found", result.stderr)

    def test_runtime_monitor_invalid_log(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "simulation-validator"
                / "scripts"
                / "runtime_monitor.py"
            ),
            "--log",
            "missing.log",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)

    def test_result_validator_invalid_metrics(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "simulation-validator"
                / "scripts"
                / "result_validator.py"
            ),
            "--metrics",
            "missing.json",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)

    def test_failure_diagnoser_invalid_log(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "simulation-validator"
                / "scripts"
                / "failure_diagnoser.py"
            ),
            "--log",
            "missing.log",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)

    def test_doe_generator_invalid_budget(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "parameter-optimization"
                / "scripts"
                / "doe_generator.py"
            ),
            "--params",
            "2",
            "--budget",
            "0",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("budget must be positive", result.stderr)

    def test_optimizer_selector_invalid_dim(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "parameter-optimization"
                / "scripts"
                / "optimizer_selector.py"
            ),
            "--dim",
            "0",
            "--budget",
            "10",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("dim must be positive", result.stderr)

    def test_sensitivity_summary_invalid_names(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "parameter-optimization"
                / "scripts"
                / "sensitivity_summary.py"
            ),
            "--scores",
            "0.1,0.2",
            "--names",
            "a,b,c",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("names count", result.stderr)

    def test_surrogate_builder_invalid_model(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "simulation-workflow"
                / "parameter-optimization"
                / "scripts"
                / "surrogate_builder.py"
            ),
            "--x",
            "0,1",
            "--y",
            "1,2",
            "--model",
            "bad",
        ]
        result = self.run_cmd(cmd)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("--model", result.stderr)

    def test_linear_solver_invalid_size(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "linear-solvers"
                / "scripts"
                / "solver_selector.py"
            ),
            "--size",
            "0",
        ]
        result = self.run_cmd(cmd)
        self.as
... [TRUNCATED]
```

### File: tests\integration\test_cli_json_schema.py
```py
import json
import subprocess
import sys
import unittest
from pathlib import Path

from tests.integration._schema import assert_schema


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "skills" / "core-numerical" / "numerical-stability" / "scripts"


class TestCliJsonSchema(unittest.TestCase):
    def run_cmd(self, args):
        return subprocess.run(
            [sys.executable, *args],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

    def test_cfl_schema(self):
        cmd = [
            str(SCRIPTS / "cfl_checker.py"),
            "--dx",
            "0.1",
            "--dt",
            "0.01",
            "--velocity",
            "1.0",
            "--diffusivity",
            "0.1",
            "--reaction-rate",
            "2.0",
            "--dimensions",
            "2",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "dx": (int, float),
                    "dt": (int, float),
                    "velocity": (type(None), int, float),
                    "diffusivity": (type(None), int, float),
                    "reaction_rate": (type(None), int, float),
                    "dimensions": int,
                    "scheme": str,
                    "safety": (int, float),
                },
                "metrics": {
                    "cfl": (type(None), int, float),
                    "fourier": (type(None), int, float),
                    "reaction": (type(None), int, float),
                },
                "limits": {
                    "advection_limit": (int, float),
                    "diffusion_limit": (int, float),
                    "reaction_limit": (int, float),
                },
                "criteria_applied": [str],
                "recommended_dt": (type(None), int, float),
                "stable": (type(None), bool),
                "notes": [str],
            },
        )

    def test_von_neumann_schema(self):
        cmd = [
            str(SCRIPTS / "von_neumann_analyzer.py"),
            "--coeffs",
            "0.2,0.6,0.2",
            "--nk",
            "64",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "coeffs": [float],
                    "dx": (int, float),
                    "kmin": (int, float),
                    "kmax": (int, float),
                    "nk": int,
                    "offset": int,
                },
                "results": {
                    "max_amplification": (int, float),
                    "k_at_max": (int, float),
                    "stable": bool,
                    "warning": (type(None), str),
                },
            },
        )

    def test_matrix_condition_schema(self):
        matrix_path = ROOT / "tests" / "integration" / "schema_matrix.txt"
        matrix_path.write_text("1 0\n0 2\n")
        try:
            cmd = [
                str(SCRIPTS / "matrix_condition.py"),
                "--matrix",
                str(matrix_path),
                "--json",
            ]
            result = self.run_cmd(cmd)
            self.assertEqual(result.returncode, 0, result.stderr)
            payload = json.loads(result.stdout)
            assert_schema(
                payload,
                {
                    "inputs": {
                        "matrix": str,
                        "shape": [int],
                        "norm": str,
                        "symmetry_tol": (int, float),
                        "skip_eigs": bool,
                    },
                    "results": {
                        "condition_number": (int, float),
                        "eigenvalue_spread": (type(None), int, float),
                        "eigenvalue_min_abs": (type(None), int, float),
                        "eigenvalue_max_abs": (type(None), int, float),
                        "is_symmetric": bool,
                        "status": str,
                        "note": (type(None), str),
                    },
                },
            )
        finally:
            matrix_path.unlink(missing_ok=True)

    def test_stiffness_schema(self):
        cmd = [
            str(SCRIPTS / "stiffness_detector.py"),
            "--eigs=-1,-1000",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {"source": str, "threshold": (int, float)},
                "results": {
                    "stiffness_ratio": (int, float),
                    "stiff": bool,
                    "recommendation": str,
                    "nonzero_count": int,
                    "total_count": int,
                },
            },
        )

    def test_error_norm_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "error_norm.py"
            ),
            "--error",
            "0.1,0.2",
            "--solution",
            "1.0,2.0",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "error": [float],
                    "solution": (type(None), list),
                    "scale": (type(None), list),
                    "rtol": (int, float),
                    "atol": (int, float),
                    "norm": str,
                    "min_scale": (int, float),
                },
                "results": {
                    "error_norm": (int, float),
                    "max_component": (int, float),
                    "scale_min": (int, float),
                    "scale_max": (int, float),
                },
            },
        )

    def test_adaptive_step_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "adaptive_step_controller.py"
            ),
            "--dt",
            "0.1",
            "--error-norm",
            "0.5",
            "--order",
            "4",
            "--controller",
            "pi",
            "--prev-error",
            "0.6",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "dt": (int, float),
                    "error_norm": (int, float),
                    "order": int,
                    "accept_threshold": (int, float),
                    "safety": (int, float),
                    "min_factor": (int, float),
                    "max_factor": (int, float),
                    "controller": str,
                    "prev_error": (type(None), int, float),
                },
                "results": {
                    "accept": bool,
                    "dt_next": (int, float),
                    "factor": (int, float),
                    "controller_used": str,
                    "note": (type(None), str),
                },
            },
        )

    def test_integrator_selector_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "integrator_selector.py"
            ),
            "--stiff",
            "--jacobian-available",
            "--implicit-allowed",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "stiff": bool,
                    "oscillatory": bool,
                    "event_detection": bool,
                    "jacobian_available": bool,
                    "implicit_allowed": bool,
                    "accuracy": str,
                    "dimension": int,
                    "low_memory": bool,
                },
                "results": {
                    "recommended": [str],
                    "alternatives": [str],
                    "notes": [str],
                },
            },
        )

    def test_imex_split_planner_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "imex_split_planner.py"
            ),
            "--stiff-terms",
            "diffusion,elastic",
            "--nonstiff-terms",
            "reaction",
            "--coupling",
            "strong",
            "--accuracy",
            "high",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "stiff_terms": [str],
                    "nonstiff_terms": [str],
                    "coupling": str,
                    "accuracy": str,
                    "stiffness_ratio": (int, float),
                    "conservative": bool,
                },
                "results": {
                    "implicit_terms": [str],
                    "explicit_terms": [str],
                    "recommended_integrator": [str],
                    "splitting_strategy": str,
                    "notes": [str],
                },
            },
        )

    def test_splitting_error_estimator_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "numerical-integration"
                / "scripts"
                / "splitting_error_estimator.py"
            ),
            "--dt",
            "1e-3",
            "--scheme",
            "strang",
            "--commutator-norm",
            "100",
            "--target-error",
            "1e-6",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "dt": (int, float),
                    "scheme": str,
                    "commutator_norm": (int, float),
                    "target_error": (int, float),
                },
                "results": {
                    "scheme": str,
                    "order": int,
                    "error_estimate": (int, float),
                    "dt_effective": (int, float),
                    "substeps": int,
                },
            },
        )

    def test_timestep_planner_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "time-stepping"
                / "scripts"
                / "timestep_planner.py"
            ),
            "--dt-target",
            "1e-4",
            "--dt-limit",
            "2e-4",
            "--safety",
            "0.8",
            "--ramp-steps",
            "5",
            "--preview-steps",
            "3",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "dt_target": (int, float),
                    "dt_limit": (int, float),
                    "safety": (int, float),
                    "dt_min": (type(None), int, float),
                    "dt_max": (type(None), int, float),
                    "ramp_steps": int,
                    "ramp_kind": str,
                    "preview_steps": int,
                },
                "results": {
                    "dt_limit": (int, float),
                    "dt_recommended": (int, float),
                    "ramp_schedule": [float],
                    "notes": [str],
                },
            },
        )

    def test_output_schedule_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "time-stepping"
                / "scripts"
                / "output_schedule.py"
            ),
            "--t-start",
            "0",
            "--t-end",
            "1",
            "--interval",
            "0.2",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "t_start": (int, float),
                    "t_end": (int, float),
                    "interval": (int, float),
                    "max_outputs": int,
                },
                "results": {
                    "interval": (int, float),
                    "count": int,
                    "output_times": [float],
                },
            },
        )

    def test_checkpoint_planner_schema(self):
        cmd = [
            str(
                ROOT
                / "skills"
                / "core-numerical"
                / "time-stepping"
                / "scripts"
                / "checkpoint_planner.py"
            ),
            "--run-time",
            "36000",
            "--checkpoint-cost",
            "120",
            "--max-lost-time",
            "1800",
            "--json",
        ]
        result = self.run_cmd(cmd)
        self.assertEqual(result.returncode, 0, result.stderr)
        payload = json.loads(result.stdout)
        assert_schema(
            payload,
            {
                "inputs": {
                    "run_time": (int, float),
                    "checkpoint_cost": (int, float),
                    "max_lost_ti
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
