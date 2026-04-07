---
id: ragas
type: knowledge
owner: OA_Triage
---
# ragas
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h1 align="center">
  <img style="vertical-align:middle" height="200"
  src="https://raw.githubusercontent.com/vibrantlabsai/ragas/main/docs/_static/imgs/logo.png">
</h1>
<p align="center">
  <i>Supercharge Your LLM Application Evaluations 🚀</i>
</p>

<p align="center">
    <a href="https://github.com/vibrantlabsai/ragas/releases">
        <img alt="Latest release" src="https://img.shields.io/github/release/vibrantlabsai/ragas.svg">
    </a>
    <a href="https://www.python.org/">
        <img alt="Made with Python" src="https://img.shields.io/badge/Made%20with-Python-1f425f.svg?color=purple">
    </a>
    <a href="https://github.com/vibrantlabsai/ragas/blob/master/LICENSE">
        <img alt="License Apache-2.0" src="https://img.shields.io/github/license/vibrantlabsai/ragas.svg?color=green">
    </a>
    <a href="https://pypi.org/project/ragas/">
        <img alt="Ragas Downloads per month" src="https://static.pepy.tech/badge/ragas/month">
    </a>
    <a href="https://discord.gg/5djav8GGNZ">
        <img alt="Join Ragas community on Discord" src="https://img.shields.io/discord/1119637219561451644">
    </a>
    <a target="_blank" href="https://deepwiki.com/vibrantlabsai/ragas">
      <img 
        src="https://devin.ai/assets/deepwiki-badge.png" 
        alt="Ask DeepWiki.com" 
        height="20" 
      />
    </a>
</p>

<h4 align="center">
    <p>
        <a href="https://docs.ragas.io/">Documentation</a> |
        <a href="#fire-quickstart">Quick start</a> |
        <a href="https://discord.gg/5djav8GGNZ">Join Discord</a> |
        <a href="https://blog.ragas.io/">Blog</a> |
        <a href="https://newsletter.ragas.io/">NewsLetter</a> |
        <a href="https://www.ragas.io/careers">Careers</a>
    <p>
</h4>

Objective metrics, intelligent test generation, and data-driven insights for LLM apps

Ragas is your ultimate toolkit for evaluating and optimizing Large Language Model (LLM) applications. Say goodbye to time-consuming, subjective assessments and hello to data-driven, efficient evaluation workflows.
Don't have a test dataset ready? We also do production-aligned test set generation.

## Key Features

- 🎯 Objective Metrics: Evaluate your LLM applications with precision using both LLM-based and traditional metrics.
- 🧪 Test Data Generation: Automatically create comprehensive test datasets covering a wide range of scenarios.
- 🔗 Seamless Integrations: Works flawlessly with popular LLM frameworks like LangChain and major observability tools.
- 📊 Build feedback loops: Leverage production data to continually improve your LLM applications.

## :shield: Installation

Pypi:

```bash
pip install ragas
```

Alternatively, from source:

```bash
pip install git+https://github.com/vibrantlabsai/ragas
```

## :fire: Quickstart

### Clone a Complete Example Project

The fastest way to get started is to use the `ragas quickstart` command:

```bash
# List available templates
ragas quickstart

# Create a RAG evaluation project
ragas quickstart rag_eval

# Specify where you want to create it.
ragas quickstart rag_eval -o ./my-project
```

Available templates:
- `rag_eval` - Evaluate RAG systems

Coming Soon:
- `agent_evals` - Evaluate AI agents
- `benchmark_llm` - Benchmark and compare LLMs
- `prompt_evals` - Evaluate prompt variations
- `workflow_eval` - Evaluate complex workflows

### Evaluate your LLM App

`ragas` comes with pre-built metrics for common evaluation tasks. For example, Aspect Critique evaluates any aspect of your output using `DiscreteMetric`:

```python
import asyncio
from openai import AsyncOpenAI
from ragas.metrics import DiscreteMetric
from ragas.llms import llm_factory

# Setup your LLM
client = AsyncOpenAI()
llm = llm_factory("gpt-4o", client=client)

# Create a custom aspect evaluator
metric = DiscreteMetric(
    name="summary_accuracy",
    allowed_values=["accurate", "inaccurate"],
    prompt="""Evaluate if the summary is accurate and captures key information.

Response: {response}

Answer with only 'accurate' or 'inaccurate'."""
)

# Score your application's output
async def main():
    score = await metric.ascore(
        llm=llm,
        response="The summary of the text is..."
    )
    print(f"Score: {score.value}")  # 'accurate' or 'inaccurate'
    print(f"Reason: {score.reason}")


if __name__ == "__main__":
    asyncio.run(main())
```

> **Note**: Make sure your `OPENAI_API_KEY` environment variable is set.

Find the complete [Quickstart Guide](https://docs.ragas.io/en/latest/getstarted/quickstart)

## Want help in improving your AI application using evals?

In the past 2 years, we have seen and helped improve many AI applications using evals. If you want help with improving and scaling up your AI application using evals.

🔗 Book a [slot](https://cal.com/team/vibrantlabs/app) or drop us a line: [founders@vibrantlabs.com](mailto:founders@vibrantlabs.com).

## 🫂 Community

If you want to get more involved with Ragas, check out our [discord server](https://discord.gg/5qGUJ6mh7C). It's a fun community where we geek out about LLM, Retrieval, Production issues, and more.

## Contributors

```yml
+----------------------------------------------------------------------------+
|     +----------------------------------------------------------------+     |
|     | Developers: Those who built with `ragas`.                      |     |
|     | (You have `import ragas` somewhere in your project)            |     |
|     |     +----------------------------------------------------+     |     |
|     |     | Contributors: Those who make `ragas` better.       |     |     |
|     |     | (You make PR to this repo)                         |     |     |
|     |     +----------------------------------------------------+     |     |
|     +----------------------------------------------------------------+     |
+----------------------------------------------------------------------------+
```

We welcome contributions from the community! Whether it's bug fixes, feature additions, or documentation improvements, your input is valuable.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

## 🔍 Open Analytics

At Ragas, we believe in transparency. We collect minimal, anonymized usage data to improve our product and guide our development efforts.

✅ No personal or company-identifying information

✅ Open-source data collection [code](./src/ragas/_analytics.py)

✅ Publicly available aggregated [data](https://github.com/vibrantlabsai/ragas/issues/49)

To opt-out, set the `RAGAS_DO_NOT_TRACK` environment variable to `true`.

### Cite Us

```
@misc{ragas2024,
  author       = {VibrantLabs},
  title        = {Ragas: Supercharge Your LLM Application Evaluations},
  year         = {2024},
  howpublished = {\url{https://github.com/vibrantlabsai/ragas}},
}
```

```

### File: examples\README.md
```md
# Ragas Examples

Official examples demonstrating how to use Ragas for evaluating different types of AI applications including RAG systems, agents, prompts, workflows, and LLM benchmarking. These examples might be unstable and are subject to change.

## Installation

### From PyPI (after release)
```bash
pip install "ragas[examples]"
```

### Local Development
Install both main ragas and examples packages in editable mode:

```bash
cd /path/to/ragas
uv pip install -e . -e ./examples
```

Or using regular pip:
```bash
cd /path/to/ragas  
pip install -e . -e ./examples
```

## Available Examples

- **`ragas_examples.agent_evals`** - Agent evaluation examples
- **`ragas_examples.benchmark_llm`** - LLM benchmarking and comparison examples  
- **`ragas_examples.prompt_evals`** - Prompt evaluation examples
- **`ragas_examples.rag_eval`** - RAG system evaluation examples
- **`ragas_examples.workflow_eval`** - Workflow evaluation examples

## Usage

### Set Environment Variables

Most examples require API keys to be set:

```bash
export OPENAI_API_KEY=your_key_here
```

For Google Drive examples, also install the gdrive extra:
```bash
pip install "ragas[examples,gdrive]"
```

### Running Examples as Modules

After installation, you can run examples directly:

```bash
# Run benchmark LLM prompt example
python -m ragas_examples.benchmark_llm.prompt

# Run benchmark LLM evaluation
python -m ragas_examples.benchmark_llm.evals

# Run other examples
python -m ragas_examples.rag_eval.evals
python -m ragas_examples.agent_evals.evals
python -m ragas_examples.prompt_evals.evals
python -m ragas_examples.workflow_eval.evals
```

## Release process

- The examples package is versioned independently using Git tags with prefix `examples-v` (e.g., `examples-v0.1.0`).
- Publishing is handled by the GitHub Actions workflow `publish-examples.yml`, which builds from `examples/` and publishes to PyPI when such a tag is pushed.

### Release Commands

To create and push a new release:

```bash
# Create and push a new tag (replace X.Y.Z with actual version)
git tag examples-vX.Y.Z
git push origin examples-vX.Y.Z

# Example:
git tag examples-v0.1.0
git push origin examples-v0.1.0
```

## Local Development & Testing


## Local Development & Testing

### Verify Installation
```bash

# Test module execution
python -m ragas_examples.benchmark_llm.prompt --help
```

```

### File: .pre-commit-config.yaml
```yaml
# Pre-commit configuration for entire ragas monorepo
# Install with: make install && pre-commit install
repos:
  - repo: local
    hooks:
      - id: monorepo-ci
        name: Run complete monorepo CI pipeline
        entry: make run-ci-format-check
        language: system
        pass_filenames: false
        always_run: true
        stages: [pre-commit]
        verbose: true

```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Ragas is an evaluation toolkit for Large Language Model (LLM) applications. It provides objective metrics for evaluating LLM applications, test data generation capabilities, and integrations with popular LLM frameworks.

The repository contains:

1. **Ragas Library** - The main evaluation toolkit including experimental features (in `src/ragas/` directory)
   - Core evaluation metrics and test generation
   - Experimental features available at `ragas.experimental`

## Development Environment Setup

### Installation

Choose the appropriate installation based on your needs:

```bash
# RECOMMENDED: Minimal dev setup (79 packages - fast)
make install-minimal

# FULL: Complete dev environment (383 packages - comprehensive)  
make install

# OR manual installation:
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

# Minimal dev setup (uses [project.optional-dependencies].dev-minimal)
uv pip install -e ".[dev-minimal]"

# Full dev setup (uses [dependency-groups].dev)
uv sync --group dev
```

### Installation Methods Explained

- **Minimal setup**: Uses `uv pip install` with optional dependencies for selective installation
- **Full setup**: Uses `uv sync` with dependency groups for comprehensive environment management
- **No naming conflicts**: `dev-minimal` vs `dev` clearly distinguish the two approaches

### Workspace Structure

The project uses a UV workspace configuration for managing multiple packages:

```bash
# Install
uv sync

# Install examples separately
uv sync --package ragas-examples

# Build specific workspace package
uv build --package ragas-examples
```

**Workspace Members:**
- `ragas` (main package) - Located in `src/ragas/`
- `ragas-examples` (examples package) - Located in `examples/`

The workspace ensures consistent dependency versions across packages and enables editable installs of workspace members.

## Common Commands

### Commands (from root directory)

```bash
# Setup and installation  
make install-minimal # Minimal dev setup (79 packages - recommended)
make install        # Full dev environment (383 packages - complete)

# Code quality
make format         # Format and lint all code
make type           # Type check all code
make check          # Quick health check (format + type, no tests)

# Testing
make test           # Run all unit tests
make test-e2e       # Run end-to-end tests

# CI/Build
make run-ci         # Run complete CI pipeline
make clean          # Clean all generated files

# Documentation
make build-docs     # Build all documentation
make serve-docs     # Serve documentation locally

# Benchmarks
make benchmarks     # Run performance benchmarks
make benchmarks-docker # Run benchmarks in Docker
```

### Testing

```bash
# Run all tests (from root)
make test

# Run specific test (using pytest -k flag)
make test k="test_name"

# Run end-to-end tests
make test-e2e

# Direct pytest commands for more control
uv run pytest tests/unit -k "test_name"
uv run pytest tests/unit -v
```

### Documentation

```bash
# Build all documentation (from root)
make build-docs

# Serve documentation locally
make serve-docs
```

### Benchmarks

```bash
# Run all benchmarks locally
make benchmarks

# Run benchmarks in Docker
make benchmarks-docker
```

## Project Architecture

The repository has the following structure:

```sh
/                          # Main ragas project
├── src/ragas/             # Source code including experimental features
│   └── experimental/      # Experimental features
├── tests/                 # All tests (core + experimental)
│   └── experimental/      # Experimental tests
├── examples/              # Example code
├── pyproject.toml         # Build config
├── docs/                  # Documentation
├── scripts/               # Build/CI scripts
├── Makefile               # Build commands
└── README.md              # Repository overview
```

### Ragas Core Components

The Ragas core library provides metrics, test data generation and evaluation functionality for LLM applications:

1. **Metrics** - Various metrics for evaluating LLM applications including:

   - AspectCritic
   - AnswerCorrectness
   - ContextPrecision
   - ContextRecall
   - Faithfulness
   - and many more

2. **Test Data Generation** - Automatic creation of test datasets for LLM applications

3. **Integrations** - Integrations with popular LLM frameworks like LangChain, LlamaIndex, and observability tools

### Experimental Components

The experimental features are now integrated into the main ragas package:

1. **Experimental features** are available at `ragas.experimental`
2. **Dataset and Experiment management** - Enhanced data handling for experiments
3. **Advanced metrics** - Extended metric capabilities
4. **Backend support** - Multiple storage backends (CSV, JSONL, Google Drive, in-memory)

To use experimental features:

```python
from ragas import Dataset
from ragas import experiment
from ragas.backends import get_registry
```

## Debugging Logs

To view debug logs for any module:

```python
import logging

# Configure logging for a specific module (example with analytics)
analytics_logger = logging.getLogger('ragas._analytics')
analytics_logger.setLevel(logging.DEBUG)

# Create a console handler and set its level
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# Create a formatter and add it to the handler
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Add the handler to the logger
analytics_logger.addHandler(console_handler)
```

## Memories

- whenever you create such docs put in in /\_experiments because that is gitignored and you can use it as a scratchpad or tmp directory for storing these
- always use uv to run python and python related commandline tools like isort, ruff, pyright etc. This is because we are using uv to manage the .venv and dependencies.
- The project uses two distinct dependency management approaches:
  - **Minimal setup**: `[project.optional-dependencies].dev-minimal` for fast development (79 packages)
  - **Full setup**: `[dependency-groups].dev` for comprehensive development (383 packages)
- Use `make install-minimal` for most development tasks, `make install` for full ML stack work
- if the user asks you to save a plan, save it into the plan/ directory with an appropriate file name.

```

### File: CODE_OF_CONDUCT.md
```md
# Code of Conduct

## Our Commitment

We are committed to providing a welcoming and inclusive environment for all people, regardless of age, body size, caste, disability, ethnicity, gender identity and expression, level of experience, family status, gender, immigration status, level of expertise, national origin, personal appearance, political belief, race, religion, sexual identity and orientation, socioeconomic status, tribe, and veteran status.

We expect all participants in the Ragas community—whether contributing code, providing feedback, reporting issues, participating in discussions, attending events, or engaging in any other capacity—to embody the values of respect, inclusion, and professionalism.

## Our Standards

Examples of behaviour that contributes to creating a positive environment include:

- Using welcoming and inclusive language
- Being respectful of differing opinions, viewpoints, and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members
- Being patient and understanding with newcomers
- Giving credit to others' work and contributions
- Asking clarifying questions rather than making assumptions

Examples of unacceptable behaviour include:

- Harassment, intimidation, or discrimination of any kind
- Unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Publishing others' private information without explicit permission (doxing)
- Gatekeeping—deliberately excluding or discouraging participation
- Deliberate disinformation or misinformation
- Other conduct which could reasonably be considered inappropriate in a professional setting
- Sustained disruption of discussions or project activities, including:
  - Spam, off-topic posts, or repeated low-effort comments in issues or discussions
  - Duplicate issues or discussions that have already been reported
  - Cross-posting the same issue or question across multiple channels without justification
  - Deliberately posting controversial or unrelated content to distract from ongoing discussions
- Threats of violence or violent language directed at another person

## Scope

This Code of Conduct applies to all spaces managed by the Ragas project, including:

- GitHub repositories (issues, pull requests, discussions, and code reviews)
- Official communication channels (Discord, Slack, mailing lists, forums)
- Official events and conferences organised by Ragas maintainers
- Any official online or offline event, conference, or gathering representing Ragas

This Code of Conduct also applies to conduct outside of these spaces if it demonstrates a pattern of harassment or is reasonably perceived as affecting the safety or well-being of community members.

The Code of Conduct applies equally to all participants, including maintainers, contributors, sponsors, and community members.

## Reporting Violations

If you experience or witness behaviour that violates this Code of Conduct, please report it by emailing **support@ragas.io**. Include as much detail as you're comfortable sharing, including:

- What happened
- Who was involved
- When it occurred
- Any relevant links or context
- Any witnesses (optional)

All reports will be treated confidentially. We will not disclose the identity of the reporter without their consent, except as necessary for investigation and response.

If the violation involves a member of the Code of Conduct committee, or if you're not comfortable reporting directly to that address, please reach out to a project maintainer directly through alternative means.

## Enforcement

The Ragas project maintainers are responsible for clarifying standards of acceptable behaviour and will take appropriate action in response to violations of this Code of Conduct.

### Our Commitment to Enforcement

We recognise that:

- Not all violations are equally severe
- Context matters
- People can learn and grow
- The goal is to maintain a healthy, inclusive community

### Enforcement Guidelines

The following are examples of how we may respond to violations. Responses will be proportionate to the severity and pattern of behaviour:

1. **Warning**: For minor or first-time violations, a private message explaining the issue and its impact, with an expectation to change behaviour.

2. **Temporary Suspension**: For more serious or repeated violations, temporary removal from community spaces (ranging from hours to weeks) to allow for reflection and de-escalation.

3. **Permanent Removal**: For severe, repeated, or unresolved violations, permanent removal from the project and its community spaces.

4. **Law Enforcement**: In cases involving illegal activity or threats of violence, we may involve law enforcement.

The maintainers may also take action to address behaviour even if no formal complaint has been filed, if they reasonably believe it violates this Code of Conduct.

## Consequences for Violations

Anyone who violates this Code of Conduct may face consequences determined by the Ragas maintainers, including:

- Editing or deletion of comments or contributions
- Removal from the project repository or community spaces
- Temporary or permanent ban from participating in Ragas spaces
- Public acknowledgment of the violation (at the discretion of the reporter and maintainers)

## Appeal Process

If you believe you have been unfairly sanctioned under this Code of Conduct, you may appeal by sending a detailed explanation to **support@ragas.io**. The appeal will be reviewed by a different set of maintainers when possible, and a decision will be communicated to you within a reasonable timeframe.

## Attribution

This Code of Conduct is adapted from the Contributor Covenant (https://www.contributor-covenant.org/), and incorporates best practices from codes of conduct in the Python community and other leading open source projects.

## Questions?

If you have questions about this Code of Conduct or how it applies to a specific situation, please reach out to the maintainers at **support@ragas.io** or through a project maintainer you trust.

---

**Last Updated**: November 2024

We appreciate your participation in making Ragas a welcoming and inclusive community for everyone.

```

### File: CONTRIBUTING.md
```md
# Development Guide for Ragas Monorepo

This comprehensive guide covers development workflows for the Ragas monorepo, designed for both human developers and AI agents.

## Quick Start (for Developers)

```bash
# 1. Clone and enter the repository
git clone https://github.com/vibrantlabsai/ragas.git

# 2. Install uv (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 3. Choose your installation type:

# RECOMMENDED: Minimal dev setup (fast)
make install-minimal

# FULL: Complete dev environment (comprehensive)
make install

# 4. Verify everything works
make check

# 5. Start developing!
make help  # See all available commands
```

## Quick Start (for AI Agents)

AI agents working with this codebase should use these standardized commands:

```bash
# Essential commands for AI development
make help           # See all available targets
make install-minimal # Minimal dev setup (fast)
make install        # Full environment (modern uv sync)
make check          # Quick health check (format + type)
make test           # Run all tests
make run-ci         # Full CI pipeline locally

# Individual development tasks
make format         # Format and lint all code
make type           # Type check all code
make clean          # Clean generated files
```

**Key Points for AI Agents:**
- Always use `make` commands rather than direct tool invocation
- Use `uv run` prefix for any direct Python tool usage
- Check `make help` for the complete command reference
- The CI pipeline uses the same commands as local development

## Monorepo Architecture

This repository is organized as a single project with integrated experimental features:

```sh
/                              # Main ragas project
├── src/ragas/                 # Main source code
│   └── experimental/          # Experimental features
├── tests/                     # Tests (unit, e2e, benchmarks)
│   └── experimental/          # Experimental tests
├── examples/                  # Example code
├── pyproject.toml             # Dependencies and configuration
├── docs/                      # Documentation
├── .github/workflows/         # CI/CD pipeline
├── Makefile                   # Build commands
└── CLAUDE.md                  # AI assistant instructions
```

### Project Components
- **Ragas Core**: The main evaluation toolkit for LLM applications (in `src/ragas/`)
- **Ragas Experimental**: Advanced features integrated at `src/ragas/experimental/`
- **Infrastructure**: Single CI/CD, documentation, and build system

### Examples Package (ragas-examples)
- Lives under `examples/` as an installable package `ragas-examples`
- Published independently to PyPI via GitHub Actions workflow `publish-examples.yml`
- Versioning via Git tags with prefix `examples-v` (e.g., `examples-v0.1.0`)
- Local development: `uv pip install -e . -e ./examples`
- Run examples: `python -m ragas_examples.benchmark_llm.prompt`

## Development Environment Setup

### Prerequisites
- Python 3.9+ 
- [uv](https://docs.astral.sh/uv/) (recommended) or pip
- Git

### Setup Process

#### Option 1: Using Make (Recommended)
```bash
# Recommended: Minimal dev setup
make install-minimal

# Full: Complete environment
make install
```

#### Option 2: Manual Setup
```bash
# Install uv if not available
curl -LsSf https://astral.sh/uv/install.sh | sh

# Minimal dev: Core + essential dev tools
uv pip install -e ".[dev-minimal]"

# Full dev: Everything (uses modern uv sync)
uv sync --group dev
```

#### Which Option to Choose?

**Use `make install-minimal` if you're:**
- Contributing to ragas development
- Need testing and linting tools
- Want fast CI/CD builds
- Working on code quality, docs, or basic features

**Use `make install` if you're:**
- Working on ML features requiring the full stack
- Need observability tools (Phoenix, MLflow)
- Developing with notebooks and advanced integrations
- Want the complete development environment

#### Installation Methods Explained

- **`install-minimal`**: Uses `uv pip install -e ".[dev-minimal]"` for selective minimal dev dependencies
- **`install`**: Uses `uv sync --group dev` for complete modern dependency management

### Verification
```bash
make check  # Runs format + type checking
make test   # Runs all tests
```

## Available Commands Reference

Run `make help` to see all targets. Here are the essential commands:

### Setup & Installation
- `make install-minimal` - Install minimal dev setup (recommended)
- `make install` - Install full environment with uv sync (complete)

### Code Quality
- `make format` - Format and lint all code (includes unused import cleanup)
- `make type` - Type check all code
- `make check` - Quick health check (format + type, no tests)

### Testing
- `make test` - Run all unit tests
- `make test-e2e` - Run end-to-end tests
- `make benchmarks` - Run performance benchmarks
- `make benchmarks-docker` - Run benchmarks in Docker

### CI/Build
- `make run-ci` - Run complete CI pipeline locally
- `make clean` - Clean all generated files

### Documentation
- `make build-docs` - Build all documentation
- `make build-docs-pdf` - Build documentation with PDF export (requires WeasyPrint)
- `make serve-docs` - Serve documentation locally
- See `docs/community/pdf_export.md` for PDF export details and limitations

## Development Workflows

### Daily Development
```bash
# 1. Start your work
git checkout -b feature/your-feature

# 2. Make changes to code

# 3. Check your work
make check           # Format and type check
make test            # Run tests

# 4. Commit and push
git add .
git commit -m "feat: your feature description"
git push origin feature/your-feature
```

### Before Submitting PR
```bash
make run-ci          # Run full CI pipeline
# Ensure all checks pass before creating PR
```

#### Development Workflow
```bash
# Use the Makefile for all development
make help           # See available commands
make format         # Format all code (core + experimental)
make type           # Type check all code
make test           # Run all tests (core + experimental)
make check          # Quick format + type check
make run-ci         # Run full CI pipeline

# Or use direct commands for specific tasks
uv run pytest tests/unit          # Run core unit tests
uv run pytest tests/unit  # Run unit tests
uv run pyright src               # Type check source code
```

## Testing Strategy

### Test Types
1. **Unit Tests**: Fast, isolated tests for individual components
2. **End-to-End Tests**: Integration tests for complete workflows
3. **Benchmarks**: Performance tests for evaluation metrics

### Running Tests
```bash
# All tests
make test

# Specific test categories
uv run pytest tests/unit
uv run pytest tests/e2e

# With coverage or specific options
uv run pytest tests/unit -k "test_name"
```

### Test Organization
- **Unit Tests**: `tests/unit/`
- **End-to-End Tests**: `tests/e2e/`
- **Benchmarks**: `tests/benchmarks/`

## Code Quality & CI/CD

### Code Quality Pipeline
The `make format` command runs:
1. **isort**: Import sorting
2. **ruff format**: Code formatting
3. **ruff --fix-only**: Auto-fix issues (including unused imports)
4. **ruff check**: Final linting validation

### Type Checking
```bash
make type  # Type check all code with pyright
```

### CI/CD Pipeline
Our GitHub Actions CI runs:
1. **Dependency Installation**: Using uv for consistent environments
2. **Code Quality Checks**: Format and type validation
3. **Testing**: Unit and integration tests across Python 3.9-3.12
4. **Multi-OS Testing**: Ubuntu, macOS, Windows

### Local CI Simulation
```bash
make run-ci  # Runs: format + type + test
```

## Project Guidelines

### Ragas Project
- **Language**: Python with type hints
- **Testing**: pytest with nbmake for notebook tests
- **Style**: Google-style docstrings
- **Architecture**: Modular metrics and evaluation framework with experimental features
- **Dependencies**: All defined in `pyproject.toml`

### Adding Dependencies
- **All features**: Add to `pyproject.toml`
- **Always**: Test with `make install` and `make test`

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Reinstall in development mode
make install
```

#### Test Failures
```bash
# Run specific failing test
uv run pytest tests/unit/test_specific.py -v

# Check experimental test dependencies
uv run pytest tests/unit --collect-only
```

#### Formatting Issues
```bash
# Fix formatting
make format

# Check specific files
uv run ruff check path/to/file.py --fix
```

#### CI Failures
```bash
# Run the same checks locally
make run-ci

# Individual checks
make format  # Must pass
make type    # Must pass  
make test    # Must pass
```

### Development Environment Issues

#### uv Not Found
```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
# or use pip: pip install uv
```

#### Dependency Conflicts
```bash
# Clean install
make clean
make install
```

### Getting Help
- **Documentation**: Check `CLAUDE.md` for AI assistant guidance
- **Commands**: Run `make help` for all available targets
- **Issues**: Check existing GitHub issues or create a new one

## Contributing Guidelines

### Pull Request Process
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Develop** using the workflows above
4. **Test** thoroughly: `make run-ci`
5. **Submit** a pull request with clear description

### Commit Message Format
```
feat: add new evaluation metric
fix: resolve import error in experimental
docs: update development guide
test: add unit tests for metric base
```

### Code Review Checklist
- [ ] All tests pass (`make test`)
- [ ] Code is formatted (`make format`)
- [ ] Type checking passes (`make type`)
- [ ] Documentation is updated
- [ ] Appropriate tests are included

## AI Agent Best Practices

### Recommended Workflow for AI Agents
1. **Understand the task**: Read relevant documentation and code
2. **Plan the approach**: Identify which project(s) need changes
3. **Use standardized commands**: Always prefer `make` targets
4. **Test incrementally**: Use `make check` frequently during development
5. **Validate thoroughly**: Run `make run-ci` before completing

### Command Patterns for AI Agents
```bash
# Always start with understanding the current state
make help
ls -la  # Check current directory structure

# For code changes
make format  # After making changes
make test    # Verify functionality

# For project-specific work
make help                       # See available commands

# For investigation
uv run pytest --collect-only  # See available tests
uv run ruff check --no-fix    # Check issues without fixing
```

### File Modification Guidelines
- **Prefer editing** existing files over creating new ones
- **Use project conventions** (check similar files for patterns)
- **Update tests** when modifying functionality
- **Follow existing code style** (enforced by `make format`)

---
#### Python 3.13 on macOS ARM: NumPy fails to install (builds from source)

- Symptom: `make install` attempts to build `numpy==2.0.x` from source on Python 3.13 (no prebuilt wheel), failing with C/C++ errors.
- Status: Ragas CI supports Python 3.9–3.12. Python 3.13 is not officially supported yet.

Workarounds:
1) Recommended: use Python 3.12
```bash
uv python install 3.12
rm -rf .venv
uv venv -p 3.12
make install
```

2) Stay on 3.13 (best effort):
- Install minimal first, then add extras as needed:
```bash
rm -rf .venv
uv venv -p 3.13
make install-minimal
uv pip install "ragas[tracing,gdrive,ai-frameworks]"
```
- Or force a newer NumPy wheel:
```bash
uv pip install "numpy>=2.1" --only-binary=:all:
```
If conflicts pin NumPy to 2.0.x, temporarily set `numpy>=2.1` in `pyproject.toml` and run `uv sync --group dev`.

**Happy coding! 🚀**

For additional context and instructions specific to AI assistants, see [CLAUDE.md](./CLAUDE.md).
```

### File: SECURITY.md
```md
# Security Policy

## Reporting Security Issues

We take the security of RAGAS seriously. If you discover a security vulnerability in this project, please report it to us privately. **Do not report security vulnerabilities through public GitHub issues, discussions, or pull requests.**

To report a vulnerability, please email us at founders@vibrantlabs.com. While not all details are mandatory, providing as much information as possible will assist us in effectively triaging and addressing the issue. Please include:

- **Type of Issue**: (e.g., buffer overflow, SQL injection, cross-site scripting)
- **Affected Versions**: List the versions of RAGAS impacted by this vulnerability.
- **Affected Files**: Full paths of source files related to the issue.
- **Location in Code**: The location of the affected source code (tag/branch/commit or direct URL).
- **Configuration Details**: Any special configuration required to reproduce the issue.
- **Environment**: (e.g., Linux / Windows / macOS)
- **Reproduction Steps**: Step-by-step instructions to reproduce the issue.
- **Proof-of-Concept or Exploit Code**: (if possible)
- **Impact Assessment**: Description of the issue's impact and how an attacker might exploit it.
- **Mitigation Suggestions**: If possible, offer suggestions or patches to mitigate the issue.

This information will help us triage and address your report more quickly.

## Supported Versions

The following versions of RAGAS are currently being supported with security updates.

| Version | Supported |
| --- | --- |
| 0.3.x   | :white_check_mark: |
| 0.2.x   | :x: |
| 0.1.x   | :x: |
| < 0.1.x | :x: |

## Security Update Policy

Upon receiving a security report, we will:

1. Acknowledge receipt within 48 hours.
2. Investigate and verify the issue.
3. Develop a fix and prepare a release.
4. Coordinate with the reporter to validate the fix.
5. Release the fix and update all affected parties.

We aim to address critical issues within 7 days of disclosure.

## Preferred Languages

We prefer all communications to be in English.

## Policy

We follow the principle of [Coordinated Vulnerability Disclosure.](https://en.wikipedia.org/wiki/Coordinated_vulnerability_disclosure)

## Acknowledgments

We appreciate the efforts of security researchers and users who report vulnerabilities to us. Your contributions help improve the security of RAGAS.

## References

For more information on security reporting and policies, you may refer to:

- [GitHub's Guide to Reporting Security Vulnerabilities](https://docs.github.com/en/code-security/security-advisories/guidelines-for-reporting-and-writing-about-security-vulnerabilities)
- [Open Source Security Foundation (OpenSSF) Best Practices](https://bestpractices.coreinfrastructure.org/)

---

*This policy is subject to change without notice. Please refer to the latest version in our repository.*

```

### File: .cursor\worktrees.json
```json
{
  "setup-worktree": [
    "cp $ROOT_WORKTREE_PATH/.env .env",
    "make install-minimal",
    "make check"
  ]
}

```

### File: .github\pull_request_template.md
```md
## Issue Link / Problem Description
<!-- Link to related issue or describe the problem this PR solves -->
- Fixes #[issue_number]
- OR describe the issue: What problem does this solve? How can it be replicated?

## Changes Made
<!-- Describe what you changed and why -->
- 
- 
- 

## Testing
<!-- Describe how this should be tested -->
### How to Test
- [ ] Automated tests added/updated
- [ ] Manual testing steps:
  1. 
  2. 
  3. 

## References
<!-- Link to related issues, discussions, forums, or external resources -->
- Related issues: 
- Documentation: 
- External references: 

## Screenshots/Examples (if applicable)
<!-- Add screenshots or code examples showing the change -->

---
<!-- 
Thank you for contributing to Ragas! 
Please fill out the sections above as completely as possible.
The more information you provide, the faster your PR can be reviewed and merged.
-->

```

### File: docs\alfred.py
```py
from __future__ import annotations

import argparse
import asyncio
import os
import typing as t
from collections import namedtuple

from langchain.prompts import ChatPromptTemplate
from langchain_core.language_models.chat_models import BaseChatModel
from langchain_openai.chat_models import ChatOpenAI
from tqdm.asyncio import tqdm

File = namedtuple("File", "name content")


def get_files(path: str, ext: str) -> list:
    return [os.path.join(path, f) for f in os.listdir(path) if f.endswith(ext)]


def load_docs(path: str) -> t.List[File]:
    files = [*get_files(path, ".md")]
    docs = []
    for file in files:
        with open(file, "r") as f:
            print("fixing: ", file)
            docs.append(File(file, f.read()))
    return docs


async def fix_doc_with_llm(doc: File, llm: BaseChatModel) -> File:
    prompt = """\
fix the following grammar and spelling mistakes in the following text. 
Please keep the markdown format intact when reformating it. 
Do not make any change to the parts of text that are for formating or additional metadata for the core text in markdown.
The target audience for this is developers so keep the tone serious and to the point without any marketing terms. 
The output text should me in .md format. 

text: {text}
"""
    fix_docs_prompt = ChatPromptTemplate.from_messages(
        [
            (prompt),
        ]
    )
    # get output
    fixed_doc = await llm.ainvoke(fix_docs_prompt.format_messages(text=doc.content))
    return File(doc.name, fixed_doc.content)


async def main(docs: t.List[File], llm: BaseChatModel):
    fix_doc_routines = [fix_doc_with_llm(doc, llm) for doc in docs]
    return await tqdm.gather(*fix_doc_routines)


if __name__ == "__main__":
    """
    Helpful assistant for documentation review and more (hopefully in the future).
    """
    # Create an argument parser
    parser = argparse.ArgumentParser(
        description="Helpful assistant for documentation review."
    )
    parser.add_argument("-d", "--directory", help="Directory to run the script against")
    args = parser.parse_args()
    directory = args.directory
    docs = load_docs(directory)
    gpt4 = ChatOpenAI(model="gpt-4")
    fix_docs = asyncio.run(main(docs, gpt4))
    for doc in fix_docs:
        with open(doc.name, "w") as f:
            f.write(doc.content)

```

### File: docs\index.md
```md
# ✨ Introduction

Ragas is a library that helps you move from "vibe checks" to systematic evaluation loops for your AI applications. It provides tools to supercharge the evaluation of Large Language Model (LLM) applications, enabling you to evaluate your LLM applications with ease and confidence.

## Why Ragas?

Traditional evaluation metrics don't capture what matters for LLM applications. Manual evaluation doesn't scale. Ragas solves this by combining **LLM-driven metrics** with **systematic experimentation** to create a continuous improvement loop.

### Key Features

- **Experiments-first approach**: Evaluate changes consistently with `experiments`. Make changes, run evaluations, observe results, and iterate to improve your LLM application.

- **Ragas Metrics**: Create custom metrics tailored to your specific use case with simple decorators or use our library of [available metrics](./concepts/metrics/available_metrics/index.md). Learn more about [metrics in Ragas](./concepts/metrics/overview/index.md).

- **Easy to integrate**: Built-in dataset management, result tracking, and integration with popular frameworks like LangChain, LlamaIndex, and more.

<div class="grid cards" markdown>
- 🚀 **Get Started**

    Start evaluating in 5 minutes with our quickstart guide.

    [:octicons-arrow-right-24: Get Started](getstarted/quickstart.md)

- 📚 **Core Concepts**

    Understand experiments, metrics, and datasets—the building blocks of effective evaluation.

    [:octicons-arrow-right-24: Core Concepts](./concepts/index.md)

- 🛠️ **How-to Guides**

    Integrate Ragas into your workflow with practical guides for specific use cases.

    [:octicons-arrow-right-24: How-to Guides](./howtos/index.md)

- 📖 **References**

    API documentation and technical details for diving deeper.

    [:octicons-arrow-right-24: References](./references/index.md)

</div>


## Want help improving your AI application using evals?

In the past 2 years, we have seen and helped improve many AI applications using evals.

We are compressing this knowledge into a product to replace vibe checks with eval loops so that you can focus on building great AI applications.

If you want help with improving and scaling up your AI application using evals, 🔗 Book a [slot](https://bit.ly/3EBYq4J) or drop us a line: [founders@vibrantlabs.com](mailto:founders@vibrantlabs.com).


```

### File: docs\ipynb_to_md.py
```py
import datetime
import os
import subprocess


def convert_ipynb_to_md(ipynb_file):
    # Change this line to add an underscore
    md_file = "_" + os.path.splitext(os.path.basename(ipynb_file))[0] + ".md"
    md_path = os.path.join(os.path.dirname(ipynb_file), md_file)
    try:
        subprocess.run(
            [
                "jupyter",
                "nbconvert",
                "--to",
                "markdown",
                ipynb_file,
                "--output",
                md_file,
            ],
            check=True,
        )
        print(f"Converted {ipynb_file} to {md_path}")
    except subprocess.CalledProcessError as e:
        print(f"Error converting {ipynb_file}: {e}")
    except FileNotFoundError:
        print(
            "Error: jupyter nbconvert not found. Please install it using 'pip install nbconvert'."
        )


def get_last_modified_time(file_path):
    return datetime.datetime.fromtimestamp(os.path.getmtime(file_path))


def find_and_convert_ipynb_files(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".ipynb"):
                ipynb_file = os.path.join(root, file)
                # Change this line to add an underscore
                md_file = "_" + os.path.splitext(file)[0] + ".md"
                md_path = os.path.join(root, md_file)

                ipynb_modified = get_last_modified_time(ipynb_file)
                md_modified = (
                    get_last_modified_time(md_path)
                    if os.path.exists(md_path)
                    else datetime.datetime.min
                )

                if ipynb_modified > md_modified:
                    print(f"Converting {ipynb_file} (modified: {ipynb_modified})")
                    convert_ipynb_to_md(ipynb_file)
                else:
                    print(f"Skipping {ipynb_file} (not modified since last conversion)")


def get_valid_directory(use_default=False):
    DEFAULT_DIRECTORY = "./docs/"

    if os.environ.get("MKDOCS_CI") or use_default:
        directory = DEFAULT_DIRECTORY
    else:
        directory = input(
            f"Enter the directory path to search for .ipynb files (default: {DEFAULT_DIRECTORY}): "
        ).strip()

    if directory == "":
        directory = DEFAULT_DIRECTORY

    return os.path.abspath(directory) if os.path.isdir(directory) else DEFAULT_DIRECTORY


if __name__ == "__main__":
    target_directory = get_valid_directory()
    print(f"Searching for .ipynb files in: {target_directory}")
    find_and_convert_ipynb_files(target_directory)
    print("Conversion process completed.")

if __name__ == "<run_path>":
    target_directory = get_valid_directory(use_default=True)
    find_and_convert_ipynb_files(target_directory)

```

### File: docs\quoted_spans_metric.md
```md
## `QuotedSpansAlignment`

**What:** A metric that measures the fraction of quoted spans in a model's answer
that appear verbatim in the retrieved sources.  The score is in the range
[0, 1], where 1.0 indicates every quoted span is supported by evidence and 0.0
indicates no quoted spans are found in the sources.

**Why:** Users place extra trust in exact quotes.  When a model quotes facts
that aren't present in its evidence, it undermines reliability.  This metric
helps catch cases of citation drift where quoted phrases in the answer are
unsupported.

## Modern Collections API (Recommended)

```python
from ragas.metrics.collections import QuotedSpansAlignment

metric = QuotedSpansAlignment()

result = await metric.ascore(
    response='The study found that "machine learning improves accuracy".',
    retrieved_contexts=["Machine learning improves accuracy by 15%."]
)
print(f"Score: {result.value}")  # 1.0
print(f"Reason: {result.reason}")  # "Matched 1/1 quoted spans"
```

**Parameters:**

- `name`: The metric name (default: "quoted_spans_alignment")
- `casefold`: Whether to normalize text by lower-casing before matching (default: True)
- `min_span_words`: Minimum number of words in a quoted span (default: 3)

**Input:**

- `response: str` – the model's response containing quoted spans
- `retrieved_contexts: List[str]` – list of source passages to check against

**Output:** A `MetricResult` with:

- `value`: Score in [0, 1]
- `reason`: Description of matched/total spans

**Notes:**

- The implementation normalizes text by collapsing whitespace and lower‑casing.
- Spans shorter than three words are ignored by default; adjust `min_span_words` to change this.
- If no quoted spans are found in the response, the score is 1.0 (nothing to verify).

---

## Legacy API (Deprecated)

> **Warning:** The legacy `quoted_spans_alignment` function is deprecated.
> Please use `QuotedSpansAlignment` from `ragas.metrics.collections` instead.

**Input shape:**

- `answers: List[str]` – list of model answers (length N)
- `sources: List[List[str]]` – list (length N) of lists of source passages

**Output:** A dictionary containing:

```python
{
  "citation_alignment_quoted_spans": float,  # score in [0,1]
  "matched": float,                          # number of spans found in sources
  "total": float                            # total number of spans considered
}
```

**Notes:**

- If no quoted spans are found across all answers, the score is defined as 0.0 with
  `total = 0`.
  
```

### File: examples\gdrive_append_example.py
```py
"""Example showing how to append data to an existing Google Drive dataset.

This demonstrates the proper pattern for adding data to existing datasets
while preserving the existing records.
"""

from pydantic import BaseModel

from ragas.dataset import Dataset


# Example data model
class EvaluationRecord(BaseModel):
    question: str
    answer: str
    context: str
    score: float
    feedback: str


def append_to_existing_dataset():
    """Example of appending to an existing dataset."""

    folder_id = "folder_id_here"  # Replace with your actual Google Drive folder ID

    # Option 1: Load existing dataset and add more data
    print("=== Appending to Existing Dataset ===")

    try:
        # Try to load existing dataset
        dataset = Dataset.load(
            name="evaluation_results",
            backend="gdrive",
            data_model=EvaluationRecord,
            folder_id=folder_id,
            credentials_path="credentials.json",
            token_path="token.json",
        )
        print(f"Loaded existing dataset with {len(dataset)} records")

    except FileNotFoundError:
        # Dataset doesn't exist, create a new one
        print("Dataset doesn't exist, creating new one")
        dataset = Dataset(
            name="evaluation_results",
            backend="gdrive",
            data_model=EvaluationRecord,
            folder_id=folder_id,
            credentials_path="credentials.json",
            token_path="token.json",
        )

    # Show existing records
    print("Existing records:")
    for i, record in enumerate(dataset):
        print(
            f"  {i + 1}. {record['question'] if isinstance(record, dict) else record.question}"
        )

    # Add new records
    new_records = [
        EvaluationRecord(
            question="What is the largest planet in our solar system?",
            answer="Jupiter",
            context="Solar system knowledge question.",
            score=0.9,
            feedback="Correct answer",
        ),
        EvaluationRecord(
            question="Who painted the Mona Lisa?",
            answer="Leonardo da Vinci",
            context="Art history question.",
            score=1.0,
            feedback="Perfect answer",
        ),
    ]

    # Append new records
    for record in new_records:
        dataset.append(record)

    print(f"\nAdded {len(new_records)} new records")

    # Save the updated dataset (this replaces the sheet with all records)
    dataset.save()
    print(f"Saved updated dataset with {len(dataset)} total records")

    # Verify by listing all records
    print("\nAll records in dataset:")
    for i, record in enumerate(dataset):
        print(
            f"  {i + 1}. {record['question'] if isinstance(record, dict) else record.question} -> {record['answer'] if isinstance(record, dict) else record.answer}"
        )

    return dataset


def create_multiple_datasets():
    """Example of creating separate datasets instead of appending."""

    folder_id = "folder_id_here"  # Replace with your actual Google Drive folder ID

    print("\n=== Creating Multiple Datasets ===")

    # Create different datasets for different evaluation runs
    datasets = {}

    for run_name, data in [
        (
            "basic_qa",
            [
                EvaluationRecord(
                    question="What is 1+1?",
                    answer="Two",
                    context="Basic math",
                    score=1.0,
                    feedback="Correct",
                )
            ],
        ),
        (
            "advanced_qa",
            [
                EvaluationRecord(
                    question="Explain quantum entanglement",
                    answer="Quantum entanglement is a phenomenon...",
                    context="Advanced physics",
                    score=0.8,
                    feedback="Good explanation",
                )
            ],
        ),
    ]:
        dataset = Dataset(
            name=f"evaluation_{run_name}",
            backend="gdrive",
            data_model=EvaluationRecord,
            folder_id=folder_id,
            credentials_path="credentials.json",
            token_path="token.json",
        )

        for record in data:
            dataset.append(record)

        dataset.save()
        datasets[run_name] = dataset
        print(f"Created dataset '{run_name}' with {len(dataset)} records")

    # List all datasets
    available_datasets = list(datasets.values())[0].backend.list_datasets()
    print(f"\nAll available datasets: {available_datasets}")

    return datasets


if __name__ == "__main__":
    try:
        # Method 1: Append to existing dataset
        dataset = append_to_existing_dataset()

        # Method 2: Create separate datasets
        datasets = create_multiple_datasets()

        print("\n✅ Append operations completed successfully!")
        print("\nKey points:")
        print(
            "- dataset.save() replaces the entire sheet (this is the intended behavior)"
        )
        print("- To append: load existing data, add new records, then save")
        print("- For different evaluation runs, consider separate datasets")

    except Exception as e:
        print(f"Error: {e}")
        import traceback

        traceback.print_exc()

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
