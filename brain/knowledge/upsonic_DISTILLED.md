---
id: upsonic
type: knowledge
owner: OA_Triage
---
# upsonic
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

<img src="https://github.com/user-attachments/assets/fbe7219f-55bc-4748-ac4a-dd2fb2b8d9e5" width="600" />

# Upsonic

**Production-Ready AI Agent Framework with Safety First**

[![PyPI version](https://badge.fury.io/py/upsonic.svg)](https://badge.fury.io/py/upsonic)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENCE)
[![Python Version](https://img.shields.io/pypi/pyversions/upsonic.svg)](https://pypi.org/project/upsonic/)
[![GitHub stars](https://img.shields.io/github/stars/Upsonic/Upsonic.svg?style=social&label=Star)](https://github.com/Upsonic/Upsonic)
[![GitHub issues](https://img.shields.io/github/issues/Upsonic/Upsonic.svg)](https://github.com/Upsonic/Upsonic/issues)
[![Documentation](https://img.shields.io/badge/docs-upsonic.ai-brightgreen.svg)](https://docs.upsonic.ai)
[![Discord](https://img.shields.io/badge/Discord-Join%20Community-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/pmYDMSQHqY)

[Documentation](https://docs.upsonic.ai) • [Quickstart](https://docs.upsonic.ai/get-started/quickstart) • [Examples](https://docs.upsonic.ai/examples) • [Discord](https://discord.gg/pmYDMSQHqY)

</div>

---

## Overview

Upsonic is an open-source AI agent framework for building production-ready agents. It supports multiple AI providers (OpenAI, Anthropic, Azure, Bedrock) and includes built-in safety policies, OCR, memory, multi-agent coordination, and MCP tool integration.

## What Can You Build?

- **Document Analysis**: Extract and process text from images and PDFs
- **Customer Service Automation**: Agents with memory and session context
- **Financial Analysis**: Agents that analyze data, generate reports, and provide insights
- **Compliance Monitoring**: Enforce safety policies across all agent interactions
- **Research & Data Gathering**: Automate research workflows with multi-agent collaboration
- **Multi-Agent Workflows**: Orchestrate tasks across specialized agent teams

## Quick Start

### Installation

```bash
uv pip install upsonic
# pip install upsonic
```

### Basic Agent

```python
from upsonic import Agent, Task

agent = Agent(model="anthropic/claude-sonnet-4-5", name="Stock Analyst Agent")

task = Task(description="Analyze the current market trends")

agent.print_do(task)
```

### Agent with Tools

```python
from upsonic import Agent, Task
from upsonic.tools.common_tools import YFinanceTools

agent = Agent(model="anthropic/claude-sonnet-4-5", name="Stock Analyst Agent")

task = Task(
    description="Give me a summary about tesla stock with tesla car models",
    tools=[YFinanceTools()]
)

agent.print_do(task)
```

### Agent with Memory

```python
from upsonic import Agent, Task
from upsonic.storage import Memory, InMemoryStorage

memory = Memory(
    storage=InMemoryStorage(),
    session_id="session_001",
    full_session_memory=True
)

agent = Agent(model="anthropic/claude-sonnet-4-5", memory=memory)

task1 = Task(description="My name is John")
agent.print_do(task1)

task2 = Task(description="What is my name?")
agent.print_do(task2)  # Agent remembers: "Your name is John"
```

**Ready for more?** Check out the [Quickstart Guide](https://docs.upsonic.ai/get-started/quickstart) for additional examples including Knowledge Base and Team workflows.

## Key Features

- **Autonomous Agent**: An agent that can read, write, and execute code inside a sandboxed workspace, no tool setup required
- **Safety Engine**: Policy-based content filtering applied to user inputs, agent outputs, and tool interactions
- **OCR Support**: Unified interface for multiple OCR engines with PDF and image support
- **Memory Management**: Session memory and long-term storage with multiple backend options
- **Multi-Agent Teams**: Sequential and parallel agent coordination
- **Tool Integration**: MCP tools, custom tools, and human-in-the-loop workflows
- **Production Ready**: Monitoring, metrics, and enterprise deployment support

## Core Capabilities

### Autonomous Agent

`AutonomousAgent` extends `Agent` with built-in filesystem and shell tools, automatic session memory, and workspace sandboxing. Useful for coding assistants, DevOps automation, and any task that needs direct file or terminal access.

```python
from upsonic import AutonomousAgent, Task

agent = AutonomousAgent(
    model="anthropic/claude-sonnet-4-5",
    workspace="/path/to/project"
)

task = Task("Read the main.py file and add error handling to every function")
agent.print_do(task)
```

All file and shell operations are restricted to `workspace`. Path traversal and dangerous commands are blocked.

---

### Safety Engine

The Safety Engine applies policies at three points: user inputs, agent outputs, and tool interactions. Policies can block, anonymize, replace, or raise exceptions on matched content.

```python
from upsonic import Agent, Task
from upsonic.safety_engine.policies.pii_policies import PIIAnonymizePolicy

agent = Agent(
    model="anthropic/claude-sonnet-4-5",
    user_policy=PIIAnonymizePolicy,  # anonymizes PII before sending to the LLM
)

task = Task(
    description="My email is john.doe@example.com and phone is 555-1234. What are my email and phone?"
)

# PII is anonymized before reaching the LLM, then de-anonymized in the response
result = agent.do(task)
print(result)  # "Your email is john.doe@example.com and phone is 555-1234"
```

Pre-built policies cover PII, adult content, profanity, financial data, and more. Custom policies are also supported.

Learn more: [Safety Engine Documentation](https://docs.upsonic.ai/concepts/safety-engine/overview)

---

### OCR and Document Processing

Upsonic provides a unified OCR interface with a layered pipeline: Layer 0 handles document preparation (PDF to image conversion, preprocessing), Layer 1 runs the OCR engine.

```bash
uv pip install "upsonic[ocr]"
```

```python
from upsonic.ocr import OCR
from upsonic.ocr.layer_1.engines import EasyOCREngine

engine = EasyOCREngine(languages=["en"])
ocr = OCR(layer_1_ocr_engine=engine)

text = ocr.get_text("invoice.pdf")
print(text)
```

Supported engines: EasyOCR, RapidOCR, Tesseract, PaddleOCR, DeepSeek OCR, DeepSeek via Ollama.

Learn more: [OCR Documentation](https://docs.upsonic.ai/concepts/ocr/overview)

## Upsonic AgentOS

AgentOS is an optional deployment platform for running agents in production. It provides a Kubernetes-based runtime, metrics dashboard, and self-hosted deployment.

- **Kubernetes-based FastAPI Runtime**: Deploy agents as isolated, scalable microservices
- **Metrics Dashboard**: Track LLM costs, token usage, and performance per transaction
- **Self-Hosted**: Full control over your data and infrastructure
- **One-Click Deployment**: Automated deployment pipelines

<img width="3024" height="1590" alt="AgentOS Dashboard" src="https://github.com/user-attachments/assets/42fceaca-2dec-4496-ab67-4b9067caca42" />

## IDE Integration

Add Upsonic docs as a source in your coding tools:

**Cursor:** Settings → Indexing & Docs → Add `https://docs.upsonic.ai/llms-full.txt`

Also works with VSCode, Windsurf, and similar tools.

## Documentation and Resources

- **[Documentation](https://docs.upsonic.ai)** - Complete guides and API reference
- **[Quickstart Guide](https://docs.upsonic.ai/get-started/quickstart)** - Get started in 5 minutes
- **[Examples](https://docs.upsonic.ai/examples)** - Real-world examples and use cases
- **[API Reference](https://docs.upsonic.ai/reference)** - Detailed API documentation

## Community and Support

> **💬 [Join our Discord community!](https://discord.gg/pmYDMSQHqY)** — Ask questions, share what you're building, get help from the team, and connect with other developers using Upsonic.

- **[Discord](https://discord.gg/pmYDMSQHqY)** - Chat with the community and get real-time support
- **[Issue Tracker](https://github.com/Upsonic/Upsonic/issues)** - Report bugs and request features
- **[Changelog](https://docs.upsonic.ai/changelog)** - See what's new in each release

## License

Upsonic is released under the MIT License. See [LICENCE](LICENCE) for details.

## Contributing

We welcome contributions from the community! Please read our contributing guidelines and code of conduct before submitting pull requests.

---

**Learn more at [upsonic.ai](https://upsonic.ai)**

```

### File: benchmarks\README.md
```md
# Upsonic Framework Benchmarks

This directory contains benchmark projects for measuring the performance of various Upsonic Framework components.

## 🚀 Setup

### ⚡ Quick Start (with Makefile - Recommended)

```bash
cd benchmarks
make setup              # Virtual env + dependencies
cd .. && echo "OPENAI_API_KEY=sk-xxx" > .env && cd benchmarks
make run                # Run first benchmark
```

**For all Makefile commands:** `make help`  
**Detailed quick start:** [QUICKSTART.md](QUICKSTART.md)

### 📋 Manual Setup

```bash
cd benchmarks
uv venv
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

# Install dependencies
uv pip install pydantic python-dotenv pympler
uv pip install -e ..

# Create environment file
cd .. && echo "OPENAI_API_KEY=sk-xxx" > .env && cd benchmarks

# Run benchmark
python -m overhead_analysis.benchmark
```

---

## 📁 Available Benchmark Projects

### 1. Overhead Analysis (`overhead_analysis/`)

Three-way comparison: Direct LLM Call (minimal overhead) vs Agent (no prompt) vs Agent (with prompt).

**Measured Metrics:**
- Memory usage (object size in bytes)
- Execution speed (mean, median, stdev, min, max)
- Cost metrics (per iteration and total, including tokens)
- Sample outputs (actual responses from each approach)

**Run:**
```bash
python -m benchmarks.overhead_analysis.benchmark
python -m benchmarks.overhead_analysis.benchmark --all-tests
```

**Details:** [overhead_analysis/README.md](overhead_analysis/README.md)

---

## 🛠️ Common Utilities

### `utils.py` - Shared Profiling Tools

Common tools used by all benchmark projects:

- **MemoryProfiler**: Object size measurement, peak memory tracking
- **PerformanceProfiler**: Timing measurement, statistical analysis
- **BenchmarkReporter**: Report generation, JSON export, console output

**Usage:**
```python
from benchmarks.utils import MemoryProfiler, PerformanceProfiler

# Memory profiling
profiler = MemoryProfiler()
profiler.start_tracking()
# ... your code ...
current_mb, peak_mb = profiler.stop_tracking()

# Performance profiling
result, elapsed_ms = PerformanceProfiler.measure_time(operation)

# Multiple runs with statistics
metrics = PerformanceProfiler.measure_multiple_runs(operation, iterations=10)
```

---

## 🚀 Creating a New Benchmark Project

### 1. Directory Structure

```
benchmarks/
├── your_benchmark_name/
│   ├── __init__.py
│   ├── benchmark.py
│   ├── test_cases.py (optional)
│   ├── README.md
│   └── results/
│       └── .gitkeep
```

### 2. Example Template

```python
# your_benchmark_name/benchmark.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from benchmarks.utils import (
    MemoryProfiler,
    PerformanceProfiler,
    BenchmarkReporter
)

def run_benchmark():
    # Your benchmark logic here
    pass

if __name__ == "__main__":
    run_benchmark()
```

### 3. Best Practices

✅ **Use common utilities**: Use tools from `benchmarks.utils` module  
✅ **Save results**: Save in JSON format to `results/` directory  
✅ **Add README**: Explain how to run and what is measured  
✅ **Define test cases**: Create repeatable tests  
✅ **Statistical analysis**: Multiple runs, mean, median, stdev  

---

## 📊 Environment Setup

A `.env` file is required for all benchmarks:

```bash
# In main directory (Upsonic/.env)
OPENAI_API_KEY=sk-your-key-here
ANTHROPIC_API_KEY=sk-ant-your-key-here  # Optional
```

---

## 🎯 Future Benchmark Projects (Suggestions)

### Model Comparison (`model_comparison/`)
Performance comparison of different LLM providers:
- OpenAI vs Anthropic vs Google
- Speed, cost, quality metrics

### Tool Performance (`tool_performance/`)
Tool execution overhead analysis:
- Native functions vs MCP tools
- Tool orchestration performance

### Memory Backend (`memory_backend/`)
Performance comparison of different memory backends:
- SQLite vs PostgreSQL vs Redis
- Read/write speed, storage overhead

### Batch Processing (`batch_processing/`)
Parallel vs sequential execution analysis:
- Throughput metrics
- Resource utilization

### Streaming Performance (`streaming_performance/`)
Stream vs non-stream execution comparison:
- First token latency
- Total completion time

---

## 📈 Standard Metrics

Standard metrics used across all benchmark projects:

### Memory Metrics
- `shallow_size_bytes`: Size of the object itself
- `deep_size_bytes`: Total size including all references
- `peak_memory_mb`: Maximum memory usage
- `current_memory_mb`: Current memory usage

### Performance Metrics
- `init_time_ms`: Initialization time
- `execution_time_ms`: Execution time
- `total_time_ms`: Total time
- `mean_time_ms`: Average (multiple runs)
- `median_time_ms`: Median
- `stdev_time_ms`: Standard deviation
- `min_time_ms` / `max_time_ms`: Min/Max

### Cost Metrics
- `total_cost`: Total API cost in USD
- `total_input_token`: Total input tokens
- `total_output_token`: Total output tokens
- `cost_per_1k_tokens`: Cost per 1,000 tokens

---

## 🤝 Contributing

For new benchmark projects or improvements:

1. Create a new subdirectory
2. Use common utilities (`benchmarks.utils`)
3. Add README and documentation
4. Submit a pull request

---

## 📝 Notes

- **First run**: May be slower due to model loading
- **Network connection**: Required for LLM API calls
- **API costs**: Consider test iterations
- **Statistical significance**: At least 5 iterations recommended

---

## 📚 Resources

- [Upsonic Documentation](https://docs.upsonic.ai)
- [Direct LLM Call Guide](https://docs.upsonic.ai/concepts/direct-llm-call/overview)
- [Agent Guide](https://docs.upsonic.ai/concepts/agent)

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.5.14
    hooks:
      # Update the uv lockfile
      - id: uv-lock
        always_run: true

  - repo: https://github.com/astral-sh/uv-pre-commit
    # uv version.
    rev: 0.5.14
    hooks:
      - id: uv-sync
        always_run: true


  - repo: local
    hooks:
      - id: pytest
        name: pytest
        entry: uv run --all-extras pytest tests/unit_tests/
        language: python
        pass_filenames: false
        always_run: true
```

### File: CLAUDE.md
```md
# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Upsonic is a reliability-focused AI agent framework for building production-ready AI agents and digital workers. The framework provides advanced reliability features, MCP (Model Context Protocol) integration, and supports multiple AI providers (OpenAI, Anthropic, Azure, Bedrock).

## Core Architecture

### Key Components

- **Agent System**: Core agent implementation in `src/upsonic/agent/` with `Direct` class as the main agent interface
- **Task Management**: Task definitions and execution logic in `src/upsonic/tasks/`
- **Tools & MCP Integration**: Tool processing and external tool management in `src/upsonic/tools/`
- **Reliability Layer**: Advanced reliability features in `src/upsonic/reliability_layer/`
- **Safety Engine**: Content filtering and policy enforcement in `src/upsonic/safety_engine/`
- **Storage**: Multi-provider storage system in `src/upsonic/storage/` (In-Memory, JSON, SQLite, Redis, PostgreSQL, MongoDB)
- **Team/Multi-Agent**: Team coordination and delegation in `src/upsonic/team/`
- **Knowledge Base & RAG**: Document processing and retrieval in `src/upsonic/knowledge_base/` and `src/upsonic/rag/`

### Main Entry Points

- `Task`: Task definition and execution (`src/upsonic/tasks/tasks.py`)
- `Agent`/`Direct`: Main agent class (`src/upsonic/agent/agent.py`)
- `Team`: Multi-agent coordination (`src/upsonic/team/team.py`)
- `KnowledgeBase`: RAG and document management (`src/upsonic/knowledge_base/knowledge_base.py`)

## Development Commands

### Environment Setup
```bash
# Install dependencies with uv
uv sync

# Install with optional dependencies
uv sync --extra rag --extra storage
```

### Testing
```bash
# Run all tests
uv run pytest

# Run specific test directory
uv run pytest tests/rag/

# Run tests with coverage
uv run pytest --cov=src/upsonic
```

### Development Tools
```bash
# Type checking
uv run mypy src/

# Pre-commit hooks (runs automatically on commit)
pre-commit run --all-files

# Lock dependencies
uv lock
```

### Running Examples
```bash
# Run basic agent example
uv run test.py
```


If you get an error about the upsonic is module is not found just try

```python
uv pip uninstall upsonic && uv run 
```

## Model Providers and Configuration

The framework supports multiple AI providers through a unified interface:

- **OpenAI**: Set `OPENAI_API_KEY` environment variable
- **Anthropic**: Set `ANTHROPIC_API_KEY` environment variable  
- **Azure**: Configure Azure-specific credentials
- **AWS Bedrock**: Configure AWS credentials

Models are specified using the format `provider/model` (e.g., `openai/gpt-4o`, `anthropic/claude-3-sonnet`).

## Key Features to Understand

### Reliability Layer
Advanced reliability features including verifier agents, editor agents, and iterative quality improvement rounds for production-ready outputs.

### MCP Integration
Built-in support for Model Context Protocol tools - can integrate with hundreds of existing MCP servers from the ecosystem.

### Safety Engine
Policy-based content filtering and safety enforcement with configurable rules for sensitive content, adult content, crypto, and social media policies.

### Storage Abstraction
Unified storage interface supporting multiple backends for session management, memory persistence, and user profiles.

## Testing Structure

Tests are organized by functionality:
- `tests/` - Core functionality tests
- `tests/rag/` - RAG and chunking tests  
- `tests/safety_engine/` - Safety policy tests
- `tests/pricing/` - Cost calculation tests

Use pytest for all testing with async support enabled.

## Environment Variables

Key environment variables:
- `OPENAI_API_KEY`, `ANTHROPIC_API_KEY` - AI provider credentials
- `UPSONIC_TELEMETRY=False` - Disable telemetry collection
- Database connection strings for storage providers (Redis, PostgreSQL, etc.)

## File Organization

- Source code: `src/upsonic/`
- Tests: `tests/`
- Documentation: `README.md`, inline docstrings
- Configuration: `pyproject.toml`, `.pre-commit-config.yaml`, `pytest.ini`
- Dependencies: Managed by `uv` with `uv.lock`
```

### File: CONTRIBUTING.md
```md
# Contributing to Upsonic

Upsonic is an open-source AI Agent Framework. We welcome contributions that align with our standards.

## Development Setup

1. Clone the repository
2. Install `uv` if not already installed:
   ```bash
   pip install uv
   ```
3. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # Unix
   # or
   .venv\Scripts\activate     # Windows
   ```
4. Install the package in editable mode with dev dependencies:
   ```bash
   uv pip install -e ".[dev]"
   ```

For specific feature development, install the relevant optional dependencies:
```bash
uv pip install -e ".[vectordb,storage,models,embeddings,tools]"
```

## Running Tests

### Unit Tests
```bash
uv run --all-extras pytest tests/unit_tests -v
```

### Smoke Tests (requires Docker)
```bash
make smoke_tests
```

This will automatically start the required Docker services (Redis, PostgreSQL, MongoDB) before running tests.

### Running Specific Tests
```bash
uv run --all-extras pytest tests/unit_tests/tools/test_common_tools_duckduckgo.py -v
uv run --all-extras pytest tests/smoke_tests/memory -v
```

## Code Standards

### Sync/Async Pattern
Every function/method MUST have both synchronous and asynchronous versions:
```python
def process(data: str) -> Result:
    """Synchronous version."""
    ...

async def aprocess(data: str) -> Result:
    """Asynchronous version - prefix with 'a'."""
    ...
```

### Type Annotations
All code MUST have proper type annotations. No `Any` types unless absolutely necessary:
```python
def calculate_score(
    items: list[dict[str, float]],
    threshold: float = 0.5
) -> tuple[float, list[str]]:
    ...
```

### Standalone Functions
Functions must be self-contained and receive all dependencies as parameters:
```python
# ✅ Correct
def process_data(client: HttpClient, config: Config, data: str) -> Result:
    ...

# ❌ Wrong - relies on external state
def process_data(data: str) -> Result:
    client = get_global_client()  # Don't do this
    ...
```

## Extension Points

### Adding a VectorDB Provider

1. Create a new file in `src/upsonic/vectordb/providers/`:
   ```
   src/upsonic/vectordb/providers/your_provider.py
   ```

2. Implement the `VectorDBProvider` interface from `src/upsonic/vectordb/base.py`

3. Add dependencies to `pyproject.toml` under a new optional group:
   ```toml
   [project.optional-dependencies]
   your-provider = [
       "your-client-lib>=x.x.x",
   ]
   ```

4. Update the `vectordb` group to include your vector database

5. Add tests in `tests/smoke_tests/vectordb/`

Reference: `src/upsonic/vectordb/providers/chroma.py`

### Adding a Model Provider

1. Create a new file in `src/upsonic/models/`:
   ```
   src/upsonic/models/your_provider.py
   ```

2. Implement the required interface pattern (see existing providers)

3. Register in `src/upsonic/models/model_registry.py`

4. Add dependencies to `pyproject.toml` under a new optional group:
   ```toml
   [project.optional-dependencies]
   your-provider = [
       "your-client-lib>=x.x.x",
   ]
   ```

5. Update the `models` group to include your model provider

6. Add tests in `tests/unit_tests/` or `tests/smoke_tests/`

Reference: `src/upsonic/models/openai.py`, `src/upsonic/models/anthropic.py`

### Adding a Storage Provider

1. Create a new directory in `src/upsonic/storage/`:
   ```
   src/upsonic/storage/your_storage/
   ├── __init__.py
   ├── your_storage.py      # Sync implementation
   ├── async_your_storage.py # Async implementation
   ├── schemas.py
   └── utils.py
   ```

2. Implement the `BaseStorage` interface from `src/upsonic/storage/base.py`

3. Provide BOTH sync and async implementations

4. Add dependencies to `pyproject.toml`:
   ```toml
   [project.optional-dependencies]
   your-storage = [
       "your-client>=x.x.x",
   ]
   ```

5. Update the `storage` group to include your storage

6. Add tests in `tests/smoke_tests/memory/`

Reference: `src/upsonic/storage/postgres/`, `src/upsonic/storage/redis/`

### Adding a Tool

1. For common tools, add to `src/upsonic/tools/common_tools/`:
   ```
   src/upsonic/tools/common_tools/your_tool.py
   ```

2. For custom/integration tools, add to `src/upsonic/tools/custom_tools/`:
   ```
   src/upsonic/tools/custom_tools/your_tool.py
   ```

3. Follow the base tool pattern from `src/upsonic/tools/base.py`

4. Export in the appropriate `__init__.py`

5. Add tests in `tests/unit_tests/tools/`

6. Update the `tools` group to include your tool

Reference: `src/upsonic/tools/common_tools/duckduckgo.py`

## Pull Request Guidelines

1. **Keep PRs focused**: One feature or fix per PR
2. **Include tests**: All new code must have test coverage
3. **Follow type conventions**: Proper annotations
4. **Both sync/async**: Implement both versions for any new function
5. **Run tests locally**: Ensure all tests pass before submitting

## License

This project is licensed under the [MIT License](/LICENCE).

```

### File: benchmarks\QUICKSTART.md
```md
# Benchmark Quick Start Guide

Follow this guide to run benchmarks as quickly as possible.

## ⚡ Quick Start (3 Steps)

### 1. Setup
```bash
cd benchmarks
make setup
```

This command will:
- ✅ Create virtual environment
- ✅ Install all dependencies
- ✅ Install Upsonic in editable mode

### 2. API Key
Create a `.env` file in the root directory:
```bash
cd ..
echo "OPENAI_API_KEY=sk-your-key-here" > .env
cd benchmarks
```

### 3. Run
```bash
make run
```

That's it! 🎉

---

## 📚 Other Commands

### Show Test Cases
```bash
make list
```

### Run All Tests
```bash
make run-all  # Warning: May take 5+ minutes
```

### Run Specific Test
```bash
make run-math           # Math problem
make run-structured     # Structured output
make run-analysis       # Text analysis
```

### Custom Iteration Count
```bash
make run-iterations N=10  # 10 iterations
```

### Show Results
```bash
make results
```

### Environment Check
```bash
make test-env
```

Output:
```
✓ Virtual environment exists
✓ .env file exists
✓ Upsonic installed
```

---

## 🔧 Troubleshooting

### "Virtual environment not found"
```bash
make setup
```

### ".env file not found"
```bash
cd ..
nano .env  # Add OPENAI_API_KEY
cd benchmarks
```

### Dependency Error
```bash
make install
```

### Reset Everything
```bash
make clean-all
make setup
```

---

## 📊 Example Workflow

```bash
# Initial setup
cd benchmarks
make setup
cd .. && echo "OPENAI_API_KEY=sk-xxx" > .env && cd benchmarks

# Quick test
make list       # View test cases
make run        # Run simple test

# Detailed analysis
make run-all    # Run all tests

# View results
make results    # List JSON files
cat overhead_analysis/results/*.json | jq .  # View JSON content

# Cleanup
make clean      # Clear cache
```

---

## 🎯 Understanding Results

Benchmark results show:

**Detailed Comparison Table:**
- Speed Metrics: Mean, Median, Stdev, Min, Max (ms)
- Memory: Object size (bytes)
- Cost: Per iteration and total cost
- Token Usage: Mean and total token counts

**Three-Way Comparison:**
- Direct: Minimum overhead
- Agent (no prompt): Without system prompt
- Agent (with prompt): With default system prompt

**Sample Outputs:**
- Actual responses from each approach
- You can see quality differences

---

## 💡 Tips

1. **First run is slower**: Model loading, cache creation
2. **API cost**: Each test ~$0.00001-0.0001
3. **Iteration count**: More iterations = more reliable results
4. **Network connection required**: For LLM API calls

---

## 🆘 Help

To see all commands:
```bash
make help
```

For detailed documentation:
- `README.md` - Main README
- `SETUP.md` - Detailed setup
- `overhead_analysis/README.md` - Project specific


```

### File: benchmarks\SETUP.md
```md
# Benchmark Setup Guide

This guide contains the setup steps required to run Upsonic benchmarks.

## ✅ Quick Start

```bash
# 1. Navigate to benchmarks directory
cd /path/to/Upsonic/benchmarks

# 2. Create virtual environment (first time only)
uv venv

# 3. Activate it
source .venv/bin/activate  # Linux/Mac
# or
.venv\Scripts\activate  # Windows

# 4. Install dependencies (first time only)
uv pip install pydantic python-dotenv pympler anthropic
uv pip install -e ..

# 5. Create environment file (in main directory)
cd ..
echo "OPENAI_API_KEY=your-key-here" > .env
echo "ANTHROPIC_API_KEY=your-key-here" >> .env  # Optional

# 6. Run benchmark
cd benchmarks
python -m overhead_analysis.benchmark --list-tests
```

## 📦 Installed Packages

The virtual environment includes:

### Benchmark Specific
- `pydantic` - For structured output
- `python-dotenv` - Environment variables
- `pympler` - Deep memory profiling (optional)
- `anthropic` - Anthropic API client

### Framework
- `upsonic` - Main framework (editable mode)
- `openai` - LLM provider
- `rich` - Terminal UI
- And other dependencies...

## 🔧 Troubleshooting

### ImportError: No module named 'X'

```bash
# Check if virtual environment is active
which python  # Should show .venv/bin/python

# If not, activate it
source .venv/bin/activate

# Install package
uv pip install <package-name>
```

### ModuleNotFoundError: No module named 'upsonic'

```bash
# Install Upsonic in editable mode
uv pip install -e ..
```

### API Key error

```bash
# Create .env file in main directory
cd /path/to/Upsonic
echo "OPENAI_API_KEY=your-actual-key" > .env
```

### Anthropic API credit balance error

If you see "Your credit balance is too low to access the Anthropic API":

1. Go to [Anthropic Console](https://console.anthropic.com/)
2. Navigate to Billing section
3. Add credits to your account
4. Retry the benchmark

## 🎯 Every Time

Before running benchmarks:

```bash
cd benchmarks
source .venv/bin/activate  # Activate virtual env
python -m overhead_analysis.benchmark  # Run benchmark
```

## 📁 File Structure

```
benchmarks/
├── .venv/                  # Virtual environment (in gitignore)
├── .gitignore              # Python, venv, etc.
├── __init__.py
├── utils.py                # Shared utilities
├── README.md               # Main README
├── SETUP.md               # This file
├── Makefile               # Automation commands
│
└── overhead_analysis/      # First benchmark project
    ├── __init__.py
    ├── benchmark.py
    ├── test_cases.py
    ├── README.md
    └── results/
```

## 🚀 For New Benchmark Projects

```bash
# Virtual environment already exists, just activate it
source .venv/bin/activate

# Create new project directory
mkdir -p your_benchmark/results

# Write code and run
python -m your_benchmark.benchmark
```

## 💡 Tips

1. **Activate virtual env in every terminal session**
2. **For package updates**: `uv pip install --upgrade package-name`
3. **To see all packages**: `uv pip list`
4. **Benchmark results**: Stored in `overhead_analysis/results/` directory
   - JSON files contain raw data
   - Markdown files contain formatted reports with comparison table and sample outputs
5. **Using Makefile**: Run `make help` to see all available commands

## 🎨 Makefile Commands

```bash
make setup          # Create venv and install dependencies
make install        # Install dependencies only
make run            # Run default benchmark
make run-all        # Run all test cases
make run-compare    # Compare OpenAI and Anthropic models
make clean          # Clean Python cache
make clean-all      # Clean everything including venv
make help           # Show all commands
```

```

### File: benchmarks\utils.py
```py
"""
Benchmark utilities for memory and performance profiling.
"""

import sys
import time
import tracemalloc
import statistics
import platform
import json
from dataclasses import dataclass, asdict
from typing import Any, Dict, List, Optional, Callable
from datetime import datetime
from pathlib import Path


@dataclass
class MemoryMetrics:
    """Memory usage metrics."""
    shallow_size_bytes: int
    deep_size_bytes: int
    peak_memory_mb: float
    current_memory_mb: float
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class CostMetrics:
    """Cost and token usage metrics."""
    total_cost: float
    input_tokens: int
    output_tokens: int
    total_tokens: int
    cost_per_1k_tokens: float
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class PerformanceMetrics:
    """Performance timing metrics."""
    init_time_ms: float
    execution_time_ms: float
    total_time_ms: float
    iterations: int
    mean_time_ms: Optional[float] = None
    median_time_ms: Optional[float] = None
    stdev_time_ms: Optional[float] = None
    min_time_ms: Optional[float] = None
    max_time_ms: Optional[float] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class BenchmarkResult:
    """Complete benchmark result for a single approach."""
    name: str
    memory: MemoryMetrics
    performance: PerformanceMetrics
    cost: CostMetrics
    metadata: Dict[str, Any]
    sample_output: Optional[str] = None
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "memory": self.memory.to_dict(),
            "performance": self.performance.to_dict(),
            "cost": self.cost.to_dict(),
            "metadata": self.metadata,
            "sample_output": self.sample_output
        }


class MemoryProfiler:
    """Profile memory usage of objects and operations."""
    
    def __init__(self):
        self.current_memory = 0.0
        self.peak_memory = 0.0
    
    def start_tracking(self) -> None:
        """Start tracking memory allocations."""
        tracemalloc.start()
    
    def stop_tracking(self) -> tuple[float, float]:
        """Stop tracking and return (current_mb, peak_mb)."""
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        current_mb = current / (1024 * 1024)
        peak_mb = peak / (1024 * 1024)
        
        self.current_memory = current_mb
        self.peak_memory = peak_mb
        
        return current_mb, peak_mb
    
    @staticmethod
    def measure_object_size(obj: Any) -> tuple[int, int]:
        """
        Measure object size in bytes.
        
        Returns:
            tuple: (shallow_size, deep_size)
        """
        shallow_size = sys.getsizeof(obj)
        
        # Try to get deep size using pympler if available
        try:
            from pympler import asizeof
            deep_size = asizeof.asizeof(obj)
        except ImportError:
            # Fallback: use shallow size
            deep_size = shallow_size
        
        return shallow_size, deep_size
    
    def profile_operation(self, operation: Callable, *args, **kwargs) -> MemoryMetrics:
        """
        Profile memory usage of an operation.
        
        Args:
            operation: Callable to execute
            *args: Arguments for the callable
            **kwargs: Keyword arguments for the callable
            
        Returns:
            MemoryMetrics with memory usage information
        """
        self.start_tracking()
        
        result = operation(*args, **kwargs)
        
        current_mb, peak_mb = self.stop_tracking()
        
        shallow_size, deep_size = self.measure_object_size(result)
        
        return MemoryMetrics(
            shallow_size_bytes=shallow_size,
            deep_size_bytes=deep_size,
            peak_memory_mb=peak_mb,
            current_memory_mb=current_mb
        )


class PerformanceProfiler:
    """Profile execution time and performance metrics."""
    
    @staticmethod
    def measure_time(operation: Callable, *args, **kwargs) -> tuple[Any, float]:
        """
        Measure execution time of an operation.
        
        Returns:
            tuple: (result, elapsed_time_ms)
        """
        start = time.perf_counter()
        result = operation(*args, **kwargs)
        end = time.perf_counter()
        
        elapsed_ms = (end - start) * 1000
        return result, elapsed_ms
    
    @staticmethod
    def measure_multiple_runs(
        operation: Callable,
        iterations: int = 10,
        warmup: int = 1,
        *args,
        **kwargs
    ) -> PerformanceMetrics:
        """
        Measure performance across multiple runs with statistics.
        
        Args:
            operation: Callable to execute
            iterations: Number of iterations to run
            warmup: Number of warmup runs (not counted)
            *args: Arguments for the callable
            **kwargs: Keyword arguments for the callable
            
        Returns:
            PerformanceMetrics with detailed timing statistics
        """
        # Warmup runs
        for _ in range(warmup):
            operation(*args, **kwargs)
        
        # Actual measurement runs
        times = []
        for _ in range(iterations):
            _, elapsed = PerformanceProfiler.measure_time(operation, *args, **kwargs)
            times.append(elapsed)
        
        # Calculate statistics
        mean_time = statistics.mean(times)
        median_time = statistics.median(times)
        stdev_time = statistics.stdev(times) if len(times) > 1 else 0.0
        min_time = min(times)
        max_time = max(times)
        
        return PerformanceMetrics(
            init_time_ms=0.0,  # To be set separately if needed
            execution_time_ms=mean_time,
            total_time_ms=mean_time,
            iterations=iterations,
            mean_time_ms=mean_time,
            median_time_ms=median_time,
            stdev_time_ms=stdev_time,
            min_time_ms=min_time,
            max_time_ms=max_time
        )


class BenchmarkReporter:
    """Generate and save benchmark reports."""
    
    @staticmethod
    def get_system_info() -> Dict[str, Any]:
        """Get system information for the report."""
        return {
            "platform": platform.platform(),
            "python_version": platform.python_version(),
            "processor": platform.processor(),
            "machine": platform.machine(),
        }
    
    @staticmethod
    def create_comparison_report(
        results: List[BenchmarkResult],
        test_name: str,
        upsonic_version: str = "0.1.0"
    ) -> Dict[str, Any]:
        """
        Create a comprehensive comparison report.
        
        Args:
            results: List of BenchmarkResult objects
            test_name: Name of the test scenario
            upsonic_version: Version of Upsonic framework
            
        Returns:
            Dictionary with complete report
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "test_name": test_name,
            "upsonic_version": upsonic_version,
            "system_info": BenchmarkReporter.get_system_info(),
            "results": {result.name: result.to_dict() for result in results}
        }
        
        # Add comparison based on number of results
        direct_result = next((r for r in results if r.name == "Direct"), None)
        agent_no_prompt = next((r for r in results if "no prompt" in r.name), None)
        agent_with_prompt = next((r for r in results if "with prompt" in r.name), None)
        
        # Handle 3-way comparison (Direct, Agent no prompt, Agent with prompt)
        if len(results) == 3 and direct_result and agent_no_prompt and agent_with_prompt:
            comparisons = {}
            
            # Direct vs Agent (no prompt)
            comparisons["direct_vs_agent_no_prompt"] = BenchmarkReporter._create_pair_comparison(
                direct_result, agent_no_prompt, "Direct", "Agent (no prompt)"
            )
            
            # Direct vs Agent (with prompt)
            comparisons["direct_vs_agent_with_prompt"] = BenchmarkReporter._create_pair_comparison(
                direct_result, agent_with_prompt, "Direct", "Agent (with prompt)"
            )
            
            # Agent (no prompt) vs Agent (with prompt)
            comparisons["agent_no_prompt_vs_with_prompt"] = BenchmarkReporter._create_pair_comparison(
                agent_no_prompt, agent_with_prompt, "Agent (no prompt)", "Agent (with prompt)"
            )
            
            report["comparison"] = comparisons
            
        # Handle 2-way comparison (backward compatibility)
        elif len(results) == 2 and direct_result:
            agent_result = next((r for r in results if r.name != "Direct"), None)
            if agent_result:
                comparison = BenchmarkReporter._create_pair_comparison(
                    direct_result, agent_result, "Direct", agent_result.name
                )
                report["comparison"] = comparison
        
        return report
    
    @staticmethod
    def _add_pair_comparison_to_markdown(md_lines: List[str], comp: Dict[str, Any]) -> None:
        """Add a pair comparison section to markdown lines."""
        name_a = comp.get('name_a', 'A')
        name_b = comp.get('name_b', 'B')
        
        # Speed comparison
        speed_ratio = comp['speed_improvement_ratio']
        speed_diff = comp['faster_by_ms']
        
        md_lines.append(f"**⚡ Speed**")
        md_lines.append("")
        if speed_ratio > 1:
            md_lines.append(f"- {name_b} is **{speed_ratio:.2f}x slower** than {name_a}")
            md_lines.append(f"- {name_a} completes tasks **{abs(speed_diff):.2f} ms faster**")
        else:
            md_lines.append(f"- {name_b} is **{1/speed_ratio:.2f}x faster** than {name_a}")
            md_lines.append(f"- {name_b} completes tasks **{abs(speed_diff):.2f} ms faster**")
        md_lines.append("")
        
        # Memory comparison
        mem_ratio = comp['memory_overhead_ratio']
        mem_diff = comp['memory_overhead_mb']
        md_lines.append(f"**💾 Memory**")
        md_lines.append("")
        if mem_ratio > 1:
            md_lines.append(f"- {name_b} uses **{mem_ratio:.2f}x more memory** than {name_a}")
            md_lines.append(f"- Memory overhead: **{mem_diff:.2f} MB** ({mem_diff*1024:.2f} KB)")
        else:
            md_lines.append(f"- {name_b} uses **{mem_ratio:.2f}x less memory** than {name_a}")
            md_lines.append(f"- Memory saved: **{abs(mem_diff):.2f} MB** ({abs(mem_diff)*1024:.2f} KB)")
        md_lines.append("")
        
        # Cost comparison (if available)
        if "cost_ratio" in comp:
            cost_ratio = comp['cost_ratio']
            cost_diff = comp.get('cost_difference', 0.0)
            md_lines.append(f"**💰 Cost**")
            md_lines.append("")
            if cost_ratio > 1:
                md_lines.append(f"- {name_b} costs **{cost_ratio:.2f}x more** than {name_a}")
                md_lines.append(f"- Cost difference: **${cost_diff:.6f}**")
                md_lines.append(f"- {name_a} total cost: **${comp['cost_a']:.6f}**")
                md_lines.append(f"- {name_b} total cost: **${comp['cost_b']:.6f}**")
            else:
                md_lines.append(f"- {name_b} costs **{1/cost_ratio:.2f}x less** than {name_a}")
                md_lines.append(f"- Cost savings: **${abs(cost_diff):.6f}**")
                md_lines.append(f"- {name_a} total cost: **${comp['cost_a']:.6f}**")
                md_lines.append(f"- {name_b} total cost: **${comp['cost_b']:.6f}**")
            md_lines.append("")
    
    @staticmethod
    def _add_detailed_comparison_table(md_lines: List[str], report: Dict[str, Any]) -> None:
        """Add a detailed comparison table showing all three approaches side-by-side."""
        results = report["results"]
        
        # Extract the three results
        direct = results.get("Direct")
        agent_no = results.get("Agent (no prompt)")
        agent_with = results.get("Agent (with prompt)")
        
        if not (direct and agent_no and agent_with):
            return
        
        # Calculate mean values per iteration
        direct_perf = direct["performance"]
        agent_no_perf = agent_no["performance"]
        agent_with_perf = agent_with["performance"]
        
        direct_cost = direct["cost"]
        agent_no_cost = agent_no["cost"]
        agent_with_cost = agent_with["cost"]
        
        # Mean costs per iteration
        direct_mean_cost = direct_cost["total_cost"] / direct_perf["iterations"]
        agent_no_mean_cost = agent_no_cost["total_cost"] / agent_no_perf["iterations"]
        agent_with_mean_cost = agent_with_cost["total_cost"] / agent_with_perf["iterations"]
        
        # Mean tokens per iteration
        direct_mean_input = direct_cost["input_tokens"] / direct_perf["iterations"]
        agent_no_mean_input = agent_no_cost["input_tokens"] / agent_no_perf["iterations"]
        agent_with_mean_input = agent_with_cost["input_tokens"] / agent_with_perf["iterations"]
        
        direct_mean_output = direct_cost["output_tokens"] / direct_perf["iterations"]
        agent_no_mean_output = agent_no_cost["output_tokens"] / agent_no_perf["iterations"]
        agent_with_mean_output = agent_with_cost["output_tokens"] / agent_with_perf["iterations"]
        
        # Create markdown table
        md_lines.append("| Metric | Direct | Agent (No Prompt) | Agent (With Prompt) |")
        md_lines.append("|--------|--------|-------------------|---------------------|")
        
        # Speed metrics
        md_lines.append(f"| **Mean Time (ms)** | {direct_perf['mean_time_ms']:.2f} | {agent_no_perf['mean_time_ms']:.2f} | {agent_with_perf['mean_time_ms']:.2f} |")
        md_lines.append(f"| **Stdev Time (ms)** | {direct_perf['stdev_time_ms']:.2f} | {agent_no_perf['stdev_time_ms']:.2f} | {agent_with_perf['stdev_time_ms']:.2f} |")
        md_lines.append(f"| **Median Time (ms)** | {direct_perf['median_time_ms']:.2f} | {agent_no_perf['median_time_ms']:.2f} | {agent_with_perf['median_time_ms']:.2f} |")
        md_lines.append(f"| **Min Time (ms)** | {direct_perf['min_time_ms']:.2f} | {agent_no_perf['min_time_ms']:.2f} | {agent_with_perf['min_time_ms']:.2f} |")
        md_lines.append(f"| **Max Time (ms)** | {direct_perf['max_time_ms']:.2f} | {agent_no_perf['max_time_ms']:.2f} | {agent_with_perf['max_time_ms']:.2f} |")
        
        # Memory metrics
        md_lines.append(f"| **Memory (bytes)** | {direct['memory']['deep_size_bytes']:,} | {agent_no['memory']['deep_size_bytes']:,} | {agent_with['memory']['deep_size_bytes']:,} |")
        
        # Cost metrics
        md_lines.append(f"| **Mean Cost ($/iter)** | ${dir
... [TRUNCATED]
```

### File: benchmarks\__init__.py
```py
"""
Upsonic Framework Benchmarks

This package contains benchmark utilities and scripts to measure
the performance of different Upsonic components.

Available Benchmark Projects:
- overhead_analysis: Direct vs Agent performance comparison

Shared utilities are available in the utils module.
"""

__version__ = "0.1.0"

from .utils import (
    MemoryProfiler,
    PerformanceProfiler,
    BenchmarkResult,
    BenchmarkReporter,
    MemoryMetrics,
    PerformanceMetrics,
    CostMetrics
)

__all__ = [
    "MemoryProfiler",
    "PerformanceProfiler",
    "BenchmarkResult",
    "BenchmarkReporter",
    "MemoryMetrics",
    "PerformanceMetrics",
    "CostMetrics",
]


```

### File: notebooks\investment_full_report.md
```md
# Stock Analyst Report

# Comprehensive Market Analysis Report

## Company Overview

### Apple Inc. (AAPL)
- **Location:** Cupertino, CA, USA
- **Industry:** Consumer Electronics
- **Sector:** Technology
- **Website:** [apple.com](https://www.apple.com)
- **Business Summary:** Apple Inc. designs, manufactures, and markets a range of consumer electronics, software, and services. The company is known for products like the iPhone, Mac, iPad, and its wearables line, and operates services such as Apple Music, iCloud, and the App Store.

### Microsoft Corporation (MSFT)
- **Location:** Redmond, WA, USA
- **Industry:** Software - Infrastructure
- **Sector:** Technology
- **Website:** [microsoft.com](https://www.microsoft.com)
- **Business Summary:** Microsoft develops and licenses consumer and enterprise software products including Office, Windows, Azure cloud services, and more. They are also involved in the gaming industry with Xbox.

### Alphabet Inc. (GOOGL)
- **Location:** Mountain View, CA, USA
- **Industry:** Internet Content & Information
- **Sector:** Communication Services
- **Website:** [abc.xyz](https://abc.xyz)
- **Business Summary:** Alphabet Inc. operates as the parent company of Google, offering search, advertising services, and platforms like YouTube and Google Cloud, as well as ventures in AI, software, and hardware.

---

## Market Research 📊

### Apple Inc. (AAPL)
- **Market Cap:** $3.78 Trillion
- **52 Week Range:** $169.21 - $288.62
- **Avg. Daily Volume:** 44M
- **Positioning:** Leads in consumer electronics leveraging strong brand loyalty and ecosystem of products and services.
- **Industry Trends:** Rising demand for wearables, growth in digital services, and emphasis on sustainability and innovation.

### Microsoft Corporation (MSFT)
- **Market Cap:** $3.42 Trillion
- **52 Week Range:** $344.79 - $555.45
- **Avg. Daily Volume:** 23M
- **Positioning:** Strong in cloud services (Azure), enterprise solutions, and consumer segments with high-entry technological barriers and extensive post-sale support.
- **Industry Trends:** Cloud computing growth, cybersecurity demand, and evolving software subscription models.

### Alphabet Inc. (GOOGL)
- **Market Cap:** $3.99 Trillion
- **52 Week Range:** $140.53 - $340.49
- **Avg. Daily Volume:** 36M
- **Positioning:** Dominates digital advertising with significant investments in AI, cloud computing, and innovative ventures like Other Bets.
- **Industry Trends:** Digital transformation, AI integration, and advertising privacy concerns.

---

## Financial Analysis 💹

### Key Financial Ratios (Twelve Months Ended)

#### Apple Inc. (AAPL)
- **Trailing P/E:** 34.25
- **Forward P/E:** 27.92
- **Return on Equity (ROE):** 171.42%
- **Gross Margins:** 46.9%

#### Microsoft Corporation (MSFT)
- **Trailing P/E:** 32.68
- **Forward P/E:** 24.53
- **Return on Equity (ROE):** 32.24%
- **Gross Margins:** 68.76%

#### Alphabet Inc. (GOOGL)
- **Trailing P/E:** 32.58
- **Forward P/E:** 29.25
- **Return on Equity (ROE):** 35.45%
- **Gross Margins:** 59.17%

### Analyst Recommendations
- **Apple Inc.:** Buy
- **Microsoft Corporation:** Strong Buy
- **Alphabet Inc.:** Strong Buy

### Recent News Impact
- **Apple Inc.:** Investor interest as key figure Peter Thiel reinvests in Apple.
- **Microsoft Corporation:** Stabilizing performance amidst market slump, favored by tech investors.
- **Alphabet Inc.:** Investment community focused on its strong growth potential and tech diversification.

### Growth Catalysts
- **Apple Inc.:** New product releases, service expansion, and ecosystem engagement.
- **Microsoft Corporation:** Cloud services (Azure), AI integration, and enterprise solutions.
- **Alphabet Inc.:** Leadership in digital advertising, cloud computing, and innovation in AI technologies.

---

## Risk Assessment 🎯

### Market Risks
- **Economic Slowdowns:** Could affect consumer purchasing power and spending patterns impacting all three companies.
- **Technology Changes:** Rapid changes in technology may necessitate adaptation and could pose risks to all tech giants.

### Company-Specific Challenges
- **Apple Inc.:** Dependency on iPhone sales, supply chain vulnerabilities, and regulatory scrutiny.
- **Microsoft Corporation:** Intense competition in cloud infrastructure and regulatory challenges in cross-border data flow.
- **Alphabet Inc.:** Regulatory pressures from data privacy laws and antitrust lawsuits.

### Macroeconomic Factors
- **Interest Rates:** Rising interest rates could impact consumer and business spending patterns.
- **Currency Fluctuations:** Can affect international sales and revenues, particularly for global operations like Apple, Microsoft, and Alphabet.

### Potential Red Flags
- **Apple Inc.:** High valuation multiples relative to historical averages.
- **Microsoft Corporation:** Slowdowns in business process solutions amidst economic concerns.
- **Alphabet Inc.:** Ongoing scrutiny and legal battles pertaining to competition laws and data management practices.

--- 

> Note: This analysis is based on recent financial data, market trends, and industry dynamics as of the latest available data. All information is intended for educational purposes and should not be construed as financial advice.

# Research Analyst Report

# Investment Analysis and Company Ranking Report

## 1. Investment Analysis 🔍

### Apple Inc. (AAPL)

- **Valuation**: With a trailing P/E of 34.25 and forward P/E of 27.92, Apple's valuation appears high. However, its impressive ROE of 171.42% indicates strong profitability.
- **Competitive Advantages**: Apple has unparalleled brand loyalty and a robust ecosystem of products and services, fostering repeat customer engagement.
- **Market Positioning**: Apple remains a leader in consumer electronics with rising demand for its digital services and wearables.
- **Challenges**: The company faces risks from supply chain disruptions and regulatory scrutiny, especially regarding its App Store policies.

### Microsoft Corporation (MSFT)

- **Valuation**: The company's trailing P/E is 32.68, with a forward P/E of 24.53, implying some expected earnings growth.
- **Competitive Advantages**: Microsoft's strengths lie in Azure cloud services, its integrated software ecosystem, and enterprise solutions.
- **Market Positioning**: It holds a strong position in cloud computing, a segment poised for continued robust growth. It also has formidable barriers to entry due to its infrastructure and enterprise partnerships.
- **Challenges**: Regulatory concerns, especially in the international sphere, and competition in cloud services present ongoing challenges.

### Alphabet Inc. (GOOGL)

- **Valuation**: Alphabet's trailing P/E is 32.58 with a forward P/E of 29.25, suggesting slightly higher valuation expectations compared to its peers.
- **Competitive Advantages**: Dominance in digital advertising, and a strong push into AI and cloud computing underpin Alphabet's market position.
- **Market Positioning**: A leader in digital advertising and poised for growth through its adaptive AI technologies and cloud offerings.
- **Challenges**: Faces significant regulatory scrutiny and antitrust lawsuits, particularly concerning its advertising practices.

## 2. Risk Evaluation 📈

- **Economic Conditions**: All three companies are vulnerable to macroeconomic trends like interest rate changes and consumer spending patterns.
- **Technology Changes**: Rapid evolutions in technology require sustained innovation and adaptation.
- **Management Capability**: Each company has a strong management team with a proven track record in navigating industry challenges.

## 3. Company Ranking 🏆

### 1. Microsoft Corporation (MSFT) - **Strong Buy**
   - **Rationale**: Microsoft is positioned strongly due to its leadership in cloud computing through Azure, solid enterprise offerings, and resilient software subscription models. Its superior margins (68.76%) and reasonable valuation (forward P/E of 24.53) enhance its investment potential.
   - **Risk-Adjusted Return**: High due to its diversified product base and adaptability.
   - **Competitive Advantage**: Unique blend of enterprise solutions and consumer products with high-integrity technological integration.

### 2. Alphabet Inc. (GOOGL) - **Strong Buy**
   - **Rationale**: Alphabet's significant investment in AI and cloud, combined with its dominant position in digital advertising, offer substantial growth potential. It has a solid ROE of 35.45% and innovative ventures providing diversification.
   - **Risk-Adjusted Return**: Good, but regulatory risks are a considerable concern compared to peers.
   - **Competitive Advantage**: Leading capabilities in AI research and lucrative advertising platforms.

### 3. Apple Inc. (AAPL) - **Buy**
   - **Rationale**: Apple remains a pioneer in consumer electronics with significant brand loyalty and financial health, indicated by a superior ROE of 171.42%. Its strategically growing services segment promises sustainable growth.
   - **Risk-Adjusted Return**: Moderate, due to potential regulatory risks and high valuation relative to growth prospects.
   - **Competitive Advantage**: Strong ecosystem of interconnected products and services.

---

### Conclusion

Microsoft stands out due to its balanced valuation, growth potential, and strategic positioning in essential tech sectors like cloud services. Alphabet offers promising growth opportunities but faces more considerable regulatory risks. Apple continues to be a solid choice with its ecosystem strength but carries higher valuation risks. These rankings consider both potential returns and the corresponding risks for each company, aiming to provide a comprehensive overview for informed investment decisions.

# Investment Lead Report

# Portfolio Allocation Strategy and Investment Report

## 1. Portfolio Strategy 💼

### Allocation Strategy
- **Microsoft Corporation (MSFT):** Allocate 40% of the portfolio. Microsoft’s strong position in cloud computing and enterprise solutions, along with a reasonable valuation, provides the portfolio with growth potential and stability. The allocation reflects its top ranking and "Strong Buy" recommendation.
  
- **Alphabet Inc. (GOOGL):** Allocate 35% of the portfolio. Alphabet’s significant investments in AI and cloud computing, combined with its leading position in digital advertising, offer substantial growth prospects. However, the regulatory risks are factored into its slightly lower allocation compared to Microsoft.

- **Apple Inc. (AAPL):** Allocate 25% of the portfolio. Apple’s brand loyalty and ecosystem strength make it a reliable investment, though its high valuation and regulatory scrutiny suggest a more cautious approach in terms of allocation.

### Optimizing Risk-Reward Balance
- **Diversification:** By allocating the portfolio across Microsoft, Alphabet, and Apple, diversification is achieved within the tech sector, which helps mitigate risks associated with individual company challenges and market volatility.
  
- **Risk Management:** The higher allocation to companies with broad enterprise solutions like Microsoft helps cushion against sector-specific regulatory pressures that Alphabet might face.

### Investment Timeframes
- **Short-to-Medium Term (1-3 years):** Prioritize Microsoft and Alphabet for potential short-to-medium-term growth driven by cloud services and AI developments.
  
- **Long Term (3-5 years+):** Consider continued investment in all three companies, with potential shifts based on regulatory developments and technological advancements.

## 2. Investment Rationale 📝

### Microsoft Corporation (MSFT)
- **Reasoning:** Microsoft's leadership position in cloud computing via Azure and its robust enterprise product suite makes it an anchor for the portfolio. The balance of reasonable valuation and high margins supports long-term growth and resilience. 
- **Concerns:** Regulatory challenges are noted but mitigated by the company’s diversified income sources.
- **Growth Catalysts:** Expansion in cloud services and the growth of subscription-based models continue to drive revenue.

### Alphabet Inc. (GOOGL)
- **Reasoning:** Alphabet stands out for its dominance in digital advertising and innovation in AI technologies. Its focus on cloud services strengthens its market potential.
- **Concerns:** Significant regulatory risks, particularly around data privacy and advertising practices, pose challenges, but its innovation potential offers a strong counterbalance.
- **Growth Catalysts:** Investment in AI and growing cloud services platform are pivotal for future expansion.

### Apple Inc. (AAPL)
- **Reasoning:** Apple maintains a strong competitive edge through its ecosystem of products and its shift towards service-based revenue streams.
- **Concerns:** The high market valuation relative to peers and regulatory scrutiny present some risk. Its substantial ROE highlights financial health and profitability.
- **Growth Catalysts:** The services segment promises sustained revenue growth and profit margins.

## 3. Recommendation Delivery 📊

### Final Allocations
- **Microsoft Corporation (MSFT):** 40%
- **Alphabet Inc. (GOOGL):** 35%
- **Apple Inc. (AAPL):** 25%

### Investment Thesis
- **Microsoft Corporation:** Act as the core holding due to its strong market position in cloud computing and enterprise solutions.
- **Alphabet Inc.:** Growth driver with a secondary focus due to regulatory concerns.
- **Apple Inc.:** Steady performer with growth through services, albeit with careful attention to valuation risks.

### Actionable Insights
- Continuously monitor regulatory developments that may impact Alphabet, adjusting allocations if risks are realized.
- Keep abreast of technological innovations in cloud computing and how Microsoft and Alphabet are capitalizing on these.
- Watch for shifts in Apple's services segment that can provide longer-term revenue stability.

### Risk Considerations
- **Regulatory Landscapes:** Close monitoring of legal and regulatory changes affecting the tech sector is essential.
- **Economic Fluctuations:** Stay alert to macroeconomic indicators that could affect consumer technology spending and corporate investment.
- **Technological Change:** Swift adaptation and innovation by portfolio companies are crucial to mitigate risks from new entrants or tech disruptions.

Implement this strategy to achieve optimized risk-adjusted returns while adapting to market changes dynamically for sustained portfolio growth.

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
