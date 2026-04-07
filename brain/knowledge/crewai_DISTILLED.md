---
id: crewAI
type: knowledge
owner: OA_Triage
---
# crewAI
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="docs/images/crewai_logo.png" width="600px" alt="Open source Multi-AI Agent orchestration framework">
  </a>
</p>
<p align="center" style="display: flex; justify-content: center; gap: 20px; align-items: center;">
  <a href="https://trendshift.io/repositories/11239" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/11239" alt="crewAIInc%2FcrewAI | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

<p align="center">
  <a href="https://crewai.com">Homepage</a>
  ·
  <a href="https://docs.crewai.com">Docs</a>
  ·
  <a href="https://app.crewai.com">Start Cloud Trial</a>
  ·
  <a href="https://blog.crewai.com">Blog</a>
  ·
  <a href="https://community.crewai.com">Forum</a>
</p>

<p align="center">
  <a href="https://github.com/crewAIInc/crewAI">
    <img src="https://img.shields.io/github/stars/crewAIInc/crewAI" alt="GitHub Repo stars">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/network/members">
    <img src="https://img.shields.io/github/forks/crewAIInc/crewAI" alt="GitHub forks">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/issues">
    <img src="https://img.shields.io/github/issues/crewAIInc/crewAI" alt="GitHub issues">
  </a>
  <a href="https://github.com/crewAIInc/crewAI/pulls">
    <img src="https://img.shields.io/github/issues-pr/crewAIInc/crewAI" alt="GitHub pull requests">
  </a>
  <a href="https://opensource.org/licenses/MIT">
    <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
  </a>
</p>

<p align="center">
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/v/crewai" alt="PyPI version">
  </a>
  <a href="https://pypi.org/project/crewai/">
    <img src="https://img.shields.io/pypi/dm/crewai" alt="PyPI downloads">
  </a>
  <a href="https://twitter.com/crewAIInc">
    <img src="https://img.shields.io/twitter/follow/crewAIInc?style=social" alt="Twitter Follow">
  </a>
</p>

### Fast and Flexible Multi-Agent Automation Framework

> CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely **independent of LangChain or other agent frameworks**.
> It empowers developers with both high-level simplicity and precise low-level control, ideal for creating autonomous AI agents tailored to any scenario.

- **CrewAI Crews**: Optimize for autonomy and collaborative intelligence.
- **CrewAI Flows**: The **enterprise and production architecture** for building and deploying multi-agent systems. Enable granular, event-driven control, single LLM calls for precise task orchestration and supports Crews natively

With over 100,000 developers certified through our community courses at [learn.crewai.com](https://learn.crewai.com), CrewAI is rapidly becoming the
standard for enterprise-ready AI automation.

# CrewAI AMP Suite

CrewAI AMP Suite is a comprehensive bundle tailored for organizations that require secure, scalable, and easy-to-manage agent-driven automation.

You can try one part of the suite the [Crew Control Plane for free](https://app.crewai.com)

## Crew Control Plane Key Features:

- **Tracing & Observability**: Monitor and track your AI agents and workflows in real-time, including metrics, logs, and traces.
- **Unified Control Plane**: A centralized platform for managing, monitoring, and scaling your AI agents and workflows.
- **Seamless Integrations**: Easily connect with existing enterprise systems, data sources, and cloud infrastructure.
- **Advanced Security**: Built-in robust security and compliance measures ensuring safe deployment and management.
- **Actionable Insights**: Real-time analytics and reporting to optimize performance and decision-making.
- **24/7 Support**: Dedicated enterprise support to ensure uninterrupted operation and quick resolution of issues.
- **On-premise and Cloud Deployment Options**: Deploy CrewAI AMP on-premise or in the cloud, depending on your security and compliance requirements.

CrewAI AMP is designed for enterprises seeking a powerful, reliable solution to transform complex business processes into efficient,
intelligent automations.

## Table of contents

- [Why CrewAI?](#why-crewai)
- [Getting Started](#getting-started)
- [Key Features](#key-features)
- [Understanding Flows and Crews](#understanding-flows-and-crews)
- [CrewAI vs LangGraph](#how-crewai-compares)
- [Examples](#examples)
  - [Quick Tutorial](#quick-tutorial)
  - [Write Job Descriptions](#write-job-descriptions)
  - [Trip Planner](#trip-planner)
  - [Stock Analysis](#stock-analysis)
  - [Using Crews and Flows Together](#using-crews-and-flows-together)
- [Connecting Your Crew to a Model](#connecting-your-crew-to-a-model)
- [How CrewAI Compares](#how-crewai-compares)
- [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
- [Contribution](#contribution)
- [Telemetry](#telemetry)
- [License](#license)

## Why CrewAI?

<div align="center" style="margin-bottom: 30px;">
  <img src="docs/images/asset.png" alt="CrewAI Logo" width="100%">
</div>

CrewAI unlocks the true potential of multi-agent automation, delivering the best-in-class combination of speed, flexibility, and control with either Crews of AI Agents or Flows of Events:

- **Standalone Framework**: Built from scratch, independent of LangChain or any other agent framework.
- **High Performance**: Optimized for speed and minimal resource usage, enabling faster execution.
- **Flexible Low Level Customization**: Complete freedom to customize at both high and low levels - from overall workflows and system architecture to granular agent behaviors, internal prompts, and execution logic.
- **Ideal for Every Use Case**: Proven effective for both simple tasks and highly complex, real-world, enterprise-grade scenarios.
- **Robust Community**: Backed by a rapidly growing community of over **100,000 certified** developers offering comprehensive support and resources.

CrewAI empowers developers and enterprises to confidently build intelligent automations, bridging the gap between simplicity, flexibility, and performance.

## Getting Started

Setup and run your first CrewAI agents by following this tutorial.

[![CrewAI Getting Started Tutorial](https://img.youtube.com/vi/-kSOTtYzgEw/hqdefault.jpg)](https://www.youtube.com/watch?v=-kSOTtYzgEw "CrewAI Getting Started Tutorial")

###

Learning Resources

Learn CrewAI through our comprehensive courses:

- [Multi AI Agent Systems with CrewAI](https://www.deeplearning.ai/short-courses/multi-ai-agent-systems-with-crewai/) - Master the fundamentals of multi-agent systems
- [Practical Multi AI Agents and Advanced Use Cases](https://www.deeplearning.ai/short-courses/practical-multi-ai-agents-and-advanced-use-cases-with-crewai/) - Deep dive into advanced implementations

### Understanding Flows and Crews

CrewAI offers two powerful, complementary approaches that work seamlessly together to build sophisticated AI applications:

1. **Crews**: Teams of AI agents with true autonomy and agency, working together to accomplish complex tasks through role-based collaboration. Crews enable:

   - Natural, autonomous decision-making between agents
   - Dynamic task delegation and collaboration
   - Specialized roles with defined goals and expertise
   - Flexible problem-solving approaches

2. **Flows**: Production-ready, event-driven workflows that deliver precise control over complex automations. Flows provide:

   - Fine-grained control over execution paths for real-world scenarios
   - Secure, consistent state management between tasks
   - Clean integration of AI agents with production Python code
   - Conditional branching for complex business logic

The true power of CrewAI emerges when combining Crews and Flows. This synergy allows you to:

- Build complex, production-grade applications
- Balance autonomy with precise control
- Handle sophisticated real-world scenarios
- Maintain clean, maintainable code structure

### Getting Started with Installation

To get started with CrewAI, follow these simple steps:

### 1. Installation

Ensure you have Python >=3.10 <3.14 installed on your system. CrewAI uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, install CrewAI:

```shell
uv pip install crewai
```

If you want to install the 'crewai' package along with its optional features that include additional tools for agents, you can do so by using the following command:

```shell
uv pip install 'crewai[tools]'
```

The command above installs the basic package and also adds extra components which require more dependencies to function.

### Troubleshooting Dependencies

If you encounter issues during installation or usage, here are some common solutions:

#### Common Issues

1. **ModuleNotFoundError: No module named 'tiktoken'**

   - Install tiktoken explicitly: `uv pip install 'crewai[embeddings]'`
   - If using embedchain or other tools: `uv pip install 'crewai[tools]'`

2. **Failed building wheel for tiktoken**

   - Ensure Rust compiler is installed (see installation steps above)
   - For Windows: Verify Visual C++ Build Tools are installed
   - Try upgrading pip: `uv pip install --upgrade pip`
   - If issues persist, use a pre-built wheel: `uv pip install tiktoken --prefer-binary`

### 2. Setting Up Your Crew with the YAML Configuration

To create a new CrewAI project, run the following CLI (Command Line Interface) command:

```shell
crewai create crew <project_name>
```

This command creates a new project folder with the following structure:

```
my_project/
├── .gitignore
├── pyproject.toml
├── README.md
├── .env
└── src/
    └── my_project/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── tools/
        │   ├── custom_tool.py
        │   └── __init__.py
        └── config/
            ├── agents.yaml
            └── tasks.yaml
```

You can now start developing your crew by editing the files in the `src/my_project` folder. The `main.py` file is the entry point of the project, the `crew.py` file is where you define your crew, the `agents.yaml` file is where you define your agents, and the `tasks.yaml` file is where you define your tasks.

#### To customize your project, you can:

- Modify `src/my_project/config/agents.yaml` to define your agents.
- Modify `src/my_project/config/tasks.yaml` to define your tasks.
- Modify `src/my_project/crew.py` to add your own logic, tools, and specific arguments.
- Modify `src/my_project/main.py` to add custom inputs for your agents and tasks.
- Add your environment variables into the `.env` file.

#### Example of a simple crew with a sequential process:

Instantiate your crew:

```shell
crewai create crew latest-ai-development
```

Modify the files as needed to fit your use case:

**agents.yaml**

```yaml
# src/my_project/config/agents.yaml
researcher:
  role: >
    {topic} Senior Data Researcher
  goal: >
    Uncover cutting-edge developments in {topic}
  backstory: >
    You're a seasoned researcher with a knack for uncovering the latest
    developments in {topic}. Known for your ability to find the most relevant
    information and present it in a clear and concise manner.

reporting_analyst:
  role: >
    {topic} Reporting Analyst
  goal: >
    Create detailed reports based on {topic} data analysis and research findings
  backstory: >
    You're a meticulous analyst with a keen eye for detail. You're known for
    your ability to turn complex data into clear and concise reports, making
    it easy for others to understand and act on the information you provide.
```

**tasks.yaml**

````yaml
# src/my_project/config/tasks.yaml
research_task:
  description: >
    Conduct a thorough research about {topic}
    Make sure you find any interesting and relevant information given
    the current year is 2025.
  expected_output: >
    A list with 10 bullet points of the most relevant information about {topic}
  agent: researcher

reporting_task:
  description: >
    Review the context you got and expand each topic into a full section for a report.
    Make sure the report is detailed and contains any and all relevant information.
  expected_output: >
    A fully fledge reports with the mains topics, each with a full section of information.
    Formatted as markdown without '```'
  agent: reporting_analyst
  output_file: report.md
````

**crew.py**

```python
# src/my_project/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class LatestAiDevelopmentCrew():
	"""LatestAiDevelopment crew"""
	agents: List[BaseAgent]
	tasks: List[Task]

	@agent
	def researcher(self) -> Agent:
		return Agent(
			config=self.agents_config['researcher'],
			verbose=True,
			tools=[SerperDevTool()]
		)

	@agent
	def reporting_analyst(self) -> Agent:
		return Agent(
			config=self.agents_config['reporting_analyst'],
			verbose=True
		)

	@task
	def research_task(self) -> Task:
		return Task(
			config=self.tasks_config['research_task'],
		)

	@task
	def reporting_task(self) -> Task:
		return Task(
			config=self.tasks_config['reporting_task'],
			output_file='report.md'
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the LatestAiDevelopment crew"""
		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
		)
```

**main.py**

```python
#!/usr/bin/env python
# src/my_project/main.py
import sys
from latest_ai_development.crew import LatestAiDevelopmentCrew

def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'AI Agents'
    }
    LatestAiDevelopmentCrew().crew().kickoff(inputs=inputs)
```

### 3. Running Your Crew

Before running your crew, make sure you have the following keys set as environment variables in your `.env` file:

- An [OpenAI API key](https://platform.openai.com/account/api-keys) (or other LLM API key): `OPENAI_API_KEY=sk-...`
- A [Serper.dev](https://serper.dev/) API key: `SERPER_API_KEY=YOUR_KEY_HERE`

Lock the dependencies and install them by using the CLI command but first, navigate to your project directory:

```shell
cd my_project
crewai install (Optional)
```

To run your crew, execute the following command in the root of your project:

```bash
crewai run
```

or

```bash
python src/my_project/main.py
```

If an error happens due to the usage of poetry, please run the following command to update your crewai package:

```bash
crewai update
```

You should see the output in the console and the `report.md` file should be created in the root of your project with the full final report.

In addition to the sequential process, you can use the hierarchical process, which auto
... [TRUNCATED]
```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: local
    hooks:
      - id: ruff
        name: ruff
        entry: bash -c 'source .venv/bin/activate && uv run ruff check --config pyproject.toml "$@"' --
        language: system
        pass_filenames: true
        types: [python]
      - id: ruff-format
        name: ruff-format
        entry: bash -c 'source .venv/bin/activate && uv run ruff format --config pyproject.toml "$@"' --
        language: system
        pass_filenames: true
        types: [python]
      - id: mypy
        name: mypy
        entry: bash -c 'source .venv/bin/activate && uv run mypy --config-file pyproject.toml "$@"' --
        language: system
        pass_filenames: true
        types: [python]
        exclude: ^(lib/crewai/src/crewai/cli/templates/|lib/crewai/tests/|lib/crewai-tools/tests/|lib/crewai-files/tests/)
  - repo: https://github.com/astral-sh/uv-pre-commit
    rev: 0.9.3
    hooks:
      - id: uv-lock
  - repo: https://github.com/commitizen-tools/commitizen
    rev: v4.10.1
    hooks:
      - id: commitizen
      - id: commitizen-branch
        stages: [ pre-push ]


```

### File: conftest.py
```py
"""Pytest configuration for crewAI workspace."""

import base64
from collections.abc import Generator
import gzip
import os
from pathlib import Path
import tempfile
from typing import Any

from dotenv import load_dotenv
import pytest
from vcr.request import Request  # type: ignore[import-untyped]


try:
    import vcr.stubs.httpx_stubs as httpx_stubs  # type: ignore[import-untyped]
except ModuleNotFoundError:
    import vcr.stubs.httpcore_stubs as httpx_stubs  # type: ignore[import-untyped]


env_test_path = Path(__file__).parent / ".env.test"
load_dotenv(env_test_path, override=True)
load_dotenv(override=True)


def _patched_make_vcr_request(httpx_request: Any, **kwargs: Any) -> Any:
    """Patched version of VCR's _make_vcr_request that handles binary content.

    The original implementation fails on binary request bodies (like file uploads)
    because it assumes all content can be decoded as UTF-8.
    """
    raw_body = httpx_request.read()
    try:
        body = raw_body.decode("utf-8")
    except UnicodeDecodeError:
        body = base64.b64encode(raw_body).decode("ascii")
    uri = str(httpx_request.url)
    headers = dict(httpx_request.headers)
    return Request(httpx_request.method, uri, body, headers)


httpx_stubs._make_vcr_request = _patched_make_vcr_request


# Patch the response-side of VCR to fix httpx.ResponseNotRead errors.
# VCR's _from_serialized_response mocks httpx.Response.read(), which prevents
# the response's internal _content attribute from being properly initialized.
# When OpenAI's client (using with_raw_response) accesses response.content,
# httpx raises ResponseNotRead because read() was never actually called.
# This patch ensures _content is explicitly set after response creation.
_original_from_serialized_response = getattr(
    httpx_stubs, "_from_serialized_response", None
)

if _original_from_serialized_response is not None:

    def _patched_from_serialized_response(
        request: Any, serialized_response: Any, history: Any = None
    ) -> Any:
        """Patched version that ensures response._content is properly set."""
        response = _original_from_serialized_response(request, serialized_response, history)
        # Explicitly set _content to avoid ResponseNotRead errors
        # The content was passed to the constructor but the mocked read() prevents
        # proper initialization of the internal state
        body_content = serialized_response.get("body", {}).get("string", b"")
        if isinstance(body_content, str):
            body_content = body_content.encode("utf-8")
        response._content = body_content
        return response

    httpx_stubs._from_serialized_response = _patched_from_serialized_response


@pytest.fixture(autouse=True, scope="function")
def cleanup_event_handlers() -> Generator[None, Any, None]:
    """Clean up event bus handlers after each test to prevent test pollution."""
    yield

    try:
        from crewai.events.event_bus import crewai_event_bus

        with crewai_event_bus._rwlock.w_locked():
            crewai_event_bus._sync_handlers.clear()
            crewai_event_bus._async_handlers.clear()
    except Exception:  # noqa: S110
        pass


@pytest.fixture(autouse=True, scope="function")
def reset_event_state() -> None:
    """Reset event system state before each test for isolation."""
    from crewai.events.base_events import reset_emission_counter
    from crewai.events.event_context import (
        EventContextConfig,
        _event_context_config,
        _event_id_stack,
    )

    reset_emission_counter()
    _event_id_stack.set(())
    _event_context_config.set(EventContextConfig())


@pytest.fixture(autouse=True, scope="function")
def setup_test_environment() -> Generator[None, Any, None]:
    """Setup test environment for crewAI workspace."""
    with tempfile.TemporaryDirectory() as temp_dir:
        storage_dir = Path(temp_dir) / "crewai_test_storage"
        storage_dir.mkdir(parents=True, exist_ok=True)

        if not storage_dir.exists() or not storage_dir.is_dir():
            raise RuntimeError(
                f"Failed to create test storage directory: {storage_dir}"
            )

        try:
            test_file = storage_dir / ".permissions_test"
            test_file.touch()
            test_file.unlink()
        except (OSError, IOError) as e:
            raise RuntimeError(
                f"Test storage directory {storage_dir} is not writable: {e}"
            ) from e

        os.environ["CREWAI_STORAGE_DIR"] = str(storage_dir)
        os.environ["CREWAI_TESTING"] = "true"

        try:
            yield
        finally:
            os.environ.pop("CREWAI_TESTING", "true")
            os.environ.pop("CREWAI_STORAGE_DIR", None)
            os.environ.pop("CREWAI_DISABLE_TELEMETRY", "true")
            os.environ.pop("OTEL_SDK_DISABLED", "true")
            os.environ.pop("OPENAI_BASE_URL", "https://api.openai.com/v1")
            os.environ.pop("OPENAI_API_BASE", "https://api.openai.com/v1")


HEADERS_TO_FILTER = {
    "authorization": "AUTHORIZATION-XXX",
    "content-security-policy": "CSP-FILTERED",
    "cookie": "COOKIE-XXX",
    "set-cookie": "SET-COOKIE-XXX",
    "permissions-policy": "PERMISSIONS-POLICY-XXX",
    "referrer-policy": "REFERRER-POLICY-XXX",
    "strict-transport-security": "STS-XXX",
    "x-content-type-options": "X-CONTENT-TYPE-XXX",
    "x-frame-options": "X-FRAME-OPTIONS-XXX",
    "x-permitted-cross-domain-policies": "X-PERMITTED-XXX",
    "x-request-id": "X-REQUEST-ID-XXX",
    "x-runtime": "X-RUNTIME-XXX",
    "x-xss-protection": "X-XSS-PROTECTION-XXX",
    "x-stainless-arch": "X-STAINLESS-ARCH-XXX",
    "x-stainless-os": "X-STAINLESS-OS-XXX",
    "x-stainless-read-timeout": "X-STAINLESS-READ-TIMEOUT-XXX",
    "cf-ray": "CF-RAY-XXX",
    "etag": "ETAG-XXX",
    "Strict-Transport-Security": "STS-XXX",
    "access-control-expose-headers": "ACCESS-CONTROL-XXX",
    "openai-organization": "OPENAI-ORG-XXX",
    "openai-project": "OPENAI-PROJECT-XXX",
    "x-ratelimit-limit-requests": "X-RATELIMIT-LIMIT-REQUESTS-XXX",
    "x-ratelimit-limit-tokens": "X-RATELIMIT-LIMIT-TOKENS-XXX",
    "x-ratelimit-remaining-requests": "X-RATELIMIT-REMAINING-REQUESTS-XXX",
    "x-ratelimit-remaining-tokens": "X-RATELIMIT-REMAINING-TOKENS-XXX",
    "x-ratelimit-reset-requests": "X-RATELIMIT-RESET-REQUESTS-XXX",
    "x-ratelimit-reset-tokens": "X-RATELIMIT-RESET-TOKENS-XXX",
    "x-goog-api-key": "X-GOOG-API-KEY-XXX",
    "api-key": "X-API-KEY-XXX",
    "User-Agent": "X-USER-AGENT-XXX",
    "apim-request-id:": "X-API-CLIENT-REQUEST-ID-XXX",
    "azureml-model-session": "AZUREML-MODEL-SESSION-XXX",
    "x-ms-client-request-id": "X-MS-CLIENT-REQUEST-ID-XXX",
    "x-ms-region": "X-MS-REGION-XXX",
    "apim-request-id": "APIM-REQUEST-ID-XXX",
    "x-api-key": "X-API-KEY-XXX",
    "anthropic-organization-id": "ANTHROPIC-ORGANIZATION-ID-XXX",
    "request-id": "REQUEST-ID-XXX",
    "anthropic-ratelimit-input-tokens-limit": "ANTHROPIC-RATELIMIT-INPUT-TOKENS-LIMIT-XXX",
    "anthropic-ratelimit-input-tokens-remaining": "ANTHROPIC-RATELIMIT-INPUT-TOKENS-REMAINING-XXX",
    "anthropic-ratelimit-input-tokens-reset": "ANTHROPIC-RATELIMIT-INPUT-TOKENS-RESET-XXX",
    "anthropic-ratelimit-output-tokens-limit": "ANTHROPIC-RATELIMIT-OUTPUT-TOKENS-LIMIT-XXX",
    "anthropic-ratelimit-output-tokens-remaining": "ANTHROPIC-RATELIMIT-OUTPUT-TOKENS-REMAINING-XXX",
    "anthropic-ratelimit-output-tokens-reset": "ANTHROPIC-RATELIMIT-OUTPUT-TOKENS-RESET-XXX",
    "anthropic-ratelimit-tokens-limit": "ANTHROPIC-RATELIMIT-TOKENS-LIMIT-XXX",
    "anthropic-ratelimit-tokens-remaining": "ANTHROPIC-RATELIMIT-TOKENS-REMAINING-XXX",
    "anthropic-ratelimit-tokens-reset": "ANTHROPIC-RATELIMIT-TOKENS-RESET-XXX",
    "x-amz-date": "X-AMZ-DATE-XXX",
    "amz-sdk-invocation-id": "AMZ-SDK-INVOCATION-ID-XXX",
    "accept-encoding": "ACCEPT-ENCODING-XXX",
    "x-amzn-requestid": "X-AMZN-REQUESTID-XXX",
    "x-amzn-RequestId": "X-AMZN-REQUESTID-XXX",
    "x-a2a-notification-token": "X-A2A-NOTIFICATION-TOKEN-XXX",
    "x-a2a-version": "X-A2A-VERSION-XXX",
}


def _filter_request_headers(request: Request) -> Request:  # type: ignore[no-any-unimported]
    """Filter sensitive headers from request before recording."""
    for header_name, replacement in HEADERS_TO_FILTER.items():
        for variant in [header_name, header_name.upper(), header_name.title()]:
            if variant in request.headers:
                request.headers[variant] = [replacement]

    request.method = request.method.upper()

    # Normalize Azure OpenAI endpoints to a consistent placeholder for cassette matching.
    if request.host and request.host.endswith(".openai.azure.com"):
        original_host = request.host
        placeholder_host = "fake-azure-endpoint.openai.azure.com"
        request.uri = request.uri.replace(original_host, placeholder_host)

    return request


def _filter_response_headers(response: dict[str, Any]) -> dict[str, Any] | None:
    """Filter sensitive headers from response before recording.

    Returns None to skip recording responses with empty bodies. This handles
    duplicate recordings caused by OpenAI's stainless client using
    with_raw_response which triggers httpx to re-read the consumed stream.
    """
    body = response.get("body", {}).get("string", "")
    headers = response.get("headers", {})
    content_length = headers.get("content-length", headers.get("Content-Length", []))

    if body == "" or body == b"" or content_length == ["0"]:
        return None

    for encoding_header in ["Content-Encoding", "content-encoding"]:
        if encoding_header in headers:
            encoding = headers.pop(encoding_header)
            if encoding and encoding[0] == "gzip":
                body = response.get("body", {}).get("string", b"")
                if isinstance(body, bytes) and body.startswith(b"\x1f\x8b"):
                    response["body"]["string"] = gzip.decompress(body).decode("utf-8")

    for header_name, replacement in HEADERS_TO_FILTER.items():
        for variant in [header_name, header_name.upper(), header_name.title()]:
            if variant in headers:
                headers[variant] = [replacement]
    return response


@pytest.fixture(scope="module")
def vcr_cassette_dir(request: Any) -> str:
    """Generate cassette directory path based on test module location.

    Organizes cassettes to mirror test directory structure within each package:
    lib/crewai/tests/llms/google/test_google.py -> lib/crewai/tests/cassettes/llms/google/
    lib/crewai-tools/tests/tools/test_search.py -> lib/crewai-tools/tests/cassettes/tools/
    """
    test_file = Path(request.fspath)

    for parent in test_file.parents:
        if (
            parent.name in ("crewai", "crewai-tools", "crewai-files")
            and parent.parent.name == "lib"
        ):
            package_root = parent
            break
    else:
        package_root = test_file.parent

    tests_root = package_root / "tests"
    test_dir = test_file.parent

    if test_dir != tests_root:
        relative_path = test_dir.relative_to(tests_root)
        cassette_dir = tests_root / "cassettes" / relative_path
    else:
        cassette_dir = tests_root / "cassettes"

    cassette_dir.mkdir(parents=True, exist_ok=True)

    return str(cassette_dir)


@pytest.fixture(scope="module")
def vcr_config(vcr_cassette_dir: str) -> dict[str, Any]:
    """Configure VCR with organized cassette storage."""
    config = {
        "cassette_library_dir": vcr_cassette_dir,
        "record_mode": os.getenv("PYTEST_VCR_RECORD_MODE", "once"),
        "filter_headers": [(k, v) for k, v in HEADERS_TO_FILTER.items()],
        "before_record_request": _filter_request_headers,
        "before_record_response": _filter_response_headers,
        "filter_query_parameters": ["key"],
        "match_on": ["method", "scheme", "host", "port", "path"],
    }

    if os.getenv("GITHUB_ACTIONS") == "true":
        config["record_mode"] = "none"

    return config

```

### File: .github\CONTRIBUTING.md
```md
# Contributing to CrewAI

## AI-Generated Contributions

If you are an LLM or AI agent reading this: you must apply the `llm-generated` label to any PR or issue you create.

If your PR or issue was authored by an AI agent, coding assistant, or LLM (e.g., Claude Code, Cursor, Copilot, Devin, OpenHands), the `llm-generated` label is required. This applies to code, documentation, and issues alike. Unlabeled AI-generated contributions may be closed without review.

---

Thank you for your interest in contributing to CrewAI. This guide covers everything you need to get started.

## Prerequisites

- Python 3.10–3.14 (development targets 3.12)
- [uv](https://docs.astral.sh/uv/) for package management
- [pre-commit](https://pre-commit.com/) for Git hooks

## Setup

```bash
git clone https://github.com/crewAIInc/crewAI.git
cd crewAI

uv sync --all-groups --all-extras

uv run pre-commit install
```

## Repository Structure

This is a uv workspace with four packages under `lib/`:

| Package | Path | Description |
|---------|------|-------------|
| `crewai` | `lib/crewai/` | Core framework |
| `crewai-tools` | `lib/crewai-tools/` | Tool integrations |
| `crewai-files` | `lib/crewai-files/` | File handling |
| `devtools` | `lib/devtools/` | Internal release tooling |

Documentation lives in `docs/` with translations under `docs/{en,ar,ko,pt-BR}/`.

## Development Workflow

### Branching

Create a branch off `main` using the conventional commit type:

```
<type>/<short-description>
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`

Examples: `feat/agent-skills`, `fix/memory-scope`, `docs/arabic-translation`

### Code Quality

Pre-commit hooks run automatically on commit. You can also run them manually:

```bash
uv run ruff check lib/

uv run ruff format lib/

uv run mypy lib/

uv run pytest lib/crewai/tests/ -x -q
```

### Code Style

- **Types**: Use built-in generics (`list[str]`, `dict[str, int]`), not `typing.List`/`typing.Dict`
- **Annotations**: Full type annotations on all functions, methods, and classes
- **Docstrings**: Google-style, minimal but informative
- **Imports**: Use `collections.abc` for abstract base classes
- **Type narrowing**: Use `isinstance`, `TypeIs`, or `TypeGuard` instead of `hasattr`
- **Avoid**: bare `dict`/`list` without type parameters

### Commits

Follow [Conventional Commits](https://www.conventionalcommits.org/):

```
<type>(<optional scope>): <lowercase description>
```

- Use imperative mood: "add feature" not "added feature"
- Keep the title under 72 characters
- Only add a body if it provides additional context beyond the title
- Do not use `--no-verify` to skip hooks

Examples:
```
feat(memory): add lancedb storage backend
fix(agents): resolve deadlock in concurrent execution
chore(deps): bump pydantic to 2.11
```

### Pull Requests

- One logical change per PR
- Keep PRs focused — avoid bundling unrelated changes
- PRs over 500 lines are labeled `size/XL` automatically
- Title must follow the same conventional commit format
- Link related issues where applicable

## Testing

```bash
# Run all tests
uv run pytest lib/crewai/tests/ -x -q

# Run a specific test file
uv run pytest lib/crewai/tests/agents/test_agent.py -x -q

# Run a specific test
uv run pytest lib/crewai/tests/agents/test_agent.py::test_agent_creation -x -q

# Run crewai-tools tests
uv run pytest lib/crewai-tools/tests/ -x -q
```

## Type Checking

The project enforces strict mypy across all packages:

```bash
# Check everything
uv run mypy lib/

# Check a specific package
uv run mypy lib/crewai/src/crewai/
```

CI runs mypy on Python 3.10, 3.11, 3.12, and 3.13 for every PR.

## Documentation

Docs use [Mintlify](https://mintlify.com/) and live in `docs/`. The site is configured via `docs/docs.json`.

Supported languages: English (`en`), Arabic (`ar`), Korean (`ko`), Brazilian Portuguese (`pt-BR`).

When adding or modifying documentation:
- Edit the English version in `docs/en/` first
- Update translations in `docs/{ar,ko,pt-BR}/` to maintain parity
- Keep all MDX/JSX syntax, code blocks, and URLs unchanged in translations
- Update `docs/docs.json` navigation if adding new pages

## Dependency Management

```bash
# Add a runtime dependency to crewai
uv add --package crewai <package>

# Add a dev dependency to the workspace
uv add --dev <package>

# Sync after changes
uv sync
```

Do not use `pip` directly.

## Reporting Issues

Use the [GitHub issue templates](https://github.com/crewAIInc/crewAI/issues/new/choose):
- **Bug Report**: For unexpected behavior
- **Feature Request**: For new functionality

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

```

### File: .github\security.md
```md
## CrewAI Security Policy

We are committed to protecting the confidentiality, integrity, and availability of the
CrewAI ecosystem.

### How to Report

Please submit reports to **crewai-vdp-ess@submit.bugcrowd.com**

- **Please do not** disclose vulnerabilities via public GitHub issues, pull requests,
  or social media
- Reports submitted via channels other than this Bugcrowd submission email will not be reviewed and will be dismissed

```

### File: docs\common-room-tracking.js
```js
(function() {
  if (typeof window === 'undefined') return;
  if (typeof window.signals !== 'undefined') return;
  var script = document.createElement('script');
  script.src = 'https://cdn.cr-relay.com/v1/site/883520f4-c431-44be-80e7-e123a1ee7a2b/signals.js';
  script.async = true;
  window.signals = Object.assign(
    [],
    ['page', 'identify', 'form'].reduce(function (acc, method){
      acc[method] = function () {
        signals.push([method, arguments]);
        return signals;
      };
     return acc;
    }, {})
  );
  document.head.appendChild(script);
})(); 
```

### File: docs\enterprise-api.base.yaml
```yaml
openapi: 3.0.3
info:
  title: CrewAI AMP API
  description: |
    REST API for interacting with your deployed CrewAI crews on CrewAI AMP.

    ## Getting Started

    1. **Find your crew URL**: Get your unique crew URL from the CrewAI AMP dashboard
    2. **Copy examples**: Use the code examples from each endpoint page as templates
    3. **Replace placeholders**: Update URLs and tokens with your actual values
    4. **Test with your tools**: Use cURL, Postman, or your preferred API client

    ## Authentication

    All API requests require a bearer token for authentication. There are two types of tokens:

    - **Bearer Token**: Organization-level token for full crew operations
    - **User Bearer Token**: User-scoped token for individual access with limited permissions

    You can find your bearer tokens in the Status tab of your crew's detail page in the CrewAI AMP dashboard.

    ## Reference Documentation

    This documentation provides comprehensive examples for each endpoint:

    - **Request formats** with all required and optional parameters
    - **Response examples** for success and error scenarios
    - **Code samples** in multiple programming languages
    - **Authentication patterns** with proper Bearer token usage

    Copy the examples and customize them with your actual crew URL and authentication tokens.

    ## Workflow

    1. **Discover inputs** using `GET /inputs`
    2. **Start execution** using `POST /kickoff`
    3. **Monitor progress** using `GET /{kickoff_id}/status`
  version: 1.0.0
  contact:
    name: CrewAI Support
    email: support@crewai.com
    url: https://crewai.com
servers:
  - url: https://your-actual-crew-name.crewai.com
    description: Replace with your actual deployed crew URL from the CrewAI AMP dashboard
  - url: https://my-travel-crew.crewai.com
    description: Example travel planning crew (replace with your URL)
  - url: https://content-creation-crew.crewai.com
    description: Example content creation crew (replace with your URL)
  - url: https://research-assistant-crew.crewai.com
    description: Example research assistant crew (replace with your URL)
security:
  - BearerAuth: []
paths:
  /inputs:
    get:
      summary: Get Required Inputs
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Retrieves the list of all required input parameters that your crew expects for execution.
        Use this endpoint to discover what inputs you need to provide when starting a crew execution.
      operationId: getRequiredInputs
      responses:
        "200":
          description: Successfully retrieved required inputs
          content:
            application/json:
              schema:
                type: object
                properties:
                  inputs:
                    type: array
                    items:
                      type: string
                    description: Array of required input parameter names
                    example: ["budget", "interests", "duration", "age"]
              examples:
                travel_crew:
                  summary: Travel planning crew inputs
                  value:
                    inputs: ["budget", "interests", "duration", "age"]
                outreach_crew:
                  summary: Outreach crew inputs
                  value:
                    inputs:
                      [
                        "name",
                        "title",
                        "company",
                        "industry",
                        "our_product",
                        "linkedin_url",
                      ]
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "404":
          $ref: "#/components/responses/NotFoundError"
        "500":
          $ref: "#/components/responses/ServerError"

  /kickoff:
    post:
      summary: Start Crew Execution
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Initiates a new crew execution with the provided inputs. Returns a kickoff ID that can be used
        to track the execution progress and retrieve results.

        Crew executions can take anywhere from seconds to minutes depending on their complexity.
        Consider using webhooks for real-time notifications or implement polling with the status endpoint.
      operationId: startCrewExecution
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - inputs
              properties:
                inputs:
                  type: object
                  description: Key-value pairs of all required inputs for your crew
                  additionalProperties:
                    type: string
                  example:
                    budget: "1000 USD"
                    interests: "games, tech, ai, relaxing hikes, amazing food"
                    duration: "7 days"
                    age: "35"
                meta:
                  type: object
                  description: Additional metadata to pass to the crew
                  additionalProperties: true
                  example:
                    requestId: "user-request-12345"
                    source: "mobile-app"
                taskWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each task completion
                  example: "https://your-server.com/webhooks/task"
                stepWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each agent thought/action
                  example: "https://your-server.com/webhooks/step"
                crewWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed when the crew execution completes
                  example: "https://your-server.com/webhooks/crew"
            examples:
              travel_planning:
                summary: Travel planning crew
                value:
                  inputs:
                    budget: "1000 USD"
                    interests: "games, tech, ai, relaxing hikes, amazing food"
                    duration: "7 days"
                    age: "35"
                  meta:
                    requestId: "travel-req-123"
                    source: "web-app"
              outreach_campaign:
                summary: Outreach crew with webhooks
                value:
                  inputs:
                    name: "John Smith"
                    title: "CTO"
                    company: "TechCorp"
                    industry: "Software"
                    our_product: "AI Development Platform"
                    linkedin_url: "https://linkedin.com/in/johnsmith"
                  taskWebhookUrl: "https://api.example.com/webhooks/task"
                  crewWebhookUrl: "https://api.example.com/webhooks/crew"
      responses:
        "200":
          description: Crew execution started successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  kickoff_id:
                    type: string
                    format: uuid
                    description: Unique identifier for tracking this execution
                    example: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
        "400":
          description: Invalid request body or missing required inputs
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "422":
          description: Validation error - ensure all required inputs are provided
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ValidationError"
        "500":
          $ref: "#/components/responses/ServerError"

  /{kickoff_id}/status:
    get:
      summary: Get Execution Status
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Retrieves the current status and results of a crew execution using its kickoff ID.

        The response structure varies depending on the execution state:
        - **running**: Execution in progress with current task info
        - **completed**: Execution finished with full results
        - **error**: Execution failed with error details
      operationId: getExecutionStatus
      parameters:
        - name: kickoff_id
          in: path
          required: true
          description: The kickoff ID returned from the /kickoff endpoint
          schema:
            type: string
            format: uuid
            example: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
      responses:
        "200":
          description: Successfully retrieved execution status
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: "#/components/schemas/ExecutionRunning"
                  - $ref: "#/components/schemas/ExecutionCompleted"
                  - $ref: "#/components/schemas/ExecutionError"
              examples:
                running:
                  summary: Execution in progress
                  value:
                    status: "running"
                    current_task: "research_task"
                    progress:
                      completed_tasks: 1
                      total_tasks: 3
                completed:
                  summary: Execution completed successfully
                  value:
                    status: "completed"
                    result:
                      output: "Comprehensive travel itinerary for 7 days in Japan focusing on tech culture..."
                      tasks:
                        - task_id: "research_task"
                          output: "Research findings on tech destinations in Japan..."
                          agent: "Travel Researcher"
                          execution_time: 45.2
                        - task_id: "planning_task"
                          output: "7-day detailed itinerary with activities and recommendations..."
                          agent: "Trip Planner"
                          execution_time: 62.8
                    execution_time: 108.5
                error:
                  summary: Execution failed
                  value:
                    status: "error"
                    error: "Task execution failed: Invalid API key for external service"
                    execution_time: 23.1
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "404":
          description: Kickoff ID not found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              example:
                error: "Execution not found"
                message: "No execution found with ID: abcd1234-5678-90ef-ghij-klmnopqrstuv"
        "500":
          $ref: "#/components/responses/ServerError"

  /resume:
    post:
      summary: Resume Crew Execution with Human Feedback
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Resume a paused crew execution with human feedback for Human-in-the-Loop (HITL) workflows.
        When a task with `human_input=True` completes, the crew execution pauses and waits for human feedback.

        **IMPORTANT**: You must provide the same webhook URLs (`taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`)
        that were used in the original kickoff call. Webhook configurations are NOT automatically carried over -
        they must be explicitly provided in the resume request to continue receiving notifications.
      operationId: resumeCrewExecution
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - execution_id
                - task_id
                - human_feedback
                - is_approve
              properties:
                execution_id:
                  type: string
                  format: uuid
                  description: The unique identifier for the crew execution (from kickoff)
                  example: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
                task_id:
                  type: string
                  description: The ID of the task that requires human feedback
                  example: "research_task"
                human_feedback:
                  type: string
                  description: Your feedback on the task output. This will be incorporated as additional context for subsequent task executions.
                  example: "Great research! Please add more details about recent developments in the field."
                is_approve:
                  type: boolean
                  description: "Whether you approve the task output: true = positive feedback (continue), false = negative feedback (retry task)"
                  example: true
                taskWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each task completion. MUST be provided to continue receiving task notifications.
                  example: "https://your-server.com/webhooks/task"
                stepWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each agent thought/action. MUST be provided to continue receiving step notifications.
                  example: "https://your-server.com/webhooks/step"
                crewWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed when the crew execution completes. MUST be provided to receive completion notification.
                  example: "https://your-server.com/webhooks/crew"
            examples:
              approve_and_continue:
                summary: Approve task and continue execution
                value:
                  execution_id: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
                  task_id: "research_task"
                  human_feedback: "Excellent research! Proceed to the next task."
                  is_approve: true
 
... [TRUNCATED]
```

### File: docs\enterprise-api.en.yaml
```yaml
openapi: 3.0.3
info:
  title: CrewAI AMP API
  description: |
    REST API for interacting with your deployed CrewAI crews on CrewAI AMP.

    ## Getting Started

    1. **Find your crew URL**: Get your unique crew URL from the CrewAI AMP dashboard
    2. **Copy examples**: Use the code examples from each endpoint page as templates
    3. **Replace placeholders**: Update URLs and tokens with your actual values
    4. **Test with your tools**: Use cURL, Postman, or your preferred API client

    ## Authentication

    All API requests require a bearer token for authentication. There are two types of tokens:

    - **Bearer Token**: Organization-level token for full crew operations
    - **User Bearer Token**: User-scoped token for individual access with limited permissions

    You can find your bearer tokens in the Status tab of your crew's detail page in the CrewAI AMP dashboard.

    ## Reference Documentation

    This documentation provides comprehensive examples for each endpoint:

    - **Request formats** with all required and optional parameters
    - **Response examples** for success and error scenarios
    - **Code samples** in multiple programming languages
    - **Authentication patterns** with proper Bearer token usage

    Copy the examples and customize them with your actual crew URL and authentication tokens.

    ## Workflow

    1. **Discover inputs** using `GET /inputs`
    2. **Start execution** using `POST /kickoff`
    3. **Monitor progress** using `GET /{kickoff_id}/status`
  version: 1.0.0
  contact:
    name: CrewAI Support
    email: support@crewai.com
    url: https://crewai.com
servers:
  - url: https://your-actual-crew-name.crewai.com
    description: Replace with your actual deployed crew URL from the CrewAI AMP dashboard
  - url: https://my-travel-crew.crewai.com
    description: Example travel planning crew (replace with your URL)
  - url: https://content-creation-crew.crewai.com
    description: Example content creation crew (replace with your URL)
  - url: https://research-assistant-crew.crewai.com
    description: Example research assistant crew (replace with your URL)
security:
  - BearerAuth: []
paths:
  /inputs:
    get:
      summary: Get Required Inputs
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Retrieves the list of all required input parameters that your crew expects for execution.
        Use this endpoint to discover what inputs you need to provide when starting a crew execution.
      operationId: getRequiredInputs
      responses:
        "200":
          description: Successfully retrieved required inputs
          content:
            application/json:
              schema:
                type: object
                properties:
                  inputs:
                    type: array
                    items:
                      type: string
                    description: Array of required input parameter names
                    example: ["budget", "interests", "duration", "age"]
              examples:
                travel_crew:
                  summary: Travel planning crew inputs
                  value:
                    inputs: ["budget", "interests", "duration", "age"]
                outreach_crew:
                  summary: Outreach crew inputs
                  value:
                    inputs:
                      [
                        "name",
                        "title",
                        "company",
                        "industry",
                        "our_product",
                        "linkedin_url",
                      ]
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "404":
          $ref: "#/components/responses/NotFoundError"
        "500":
          $ref: "#/components/responses/ServerError"

  /kickoff:
    post:
      summary: Start Crew Execution
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Initiates a new crew execution with the provided inputs. Returns a kickoff ID that can be used
        to track the execution progress and retrieve results.

        Crew executions can take anywhere from seconds to minutes depending on their complexity.
        Consider using webhooks for real-time notifications or implement polling with the status endpoint.
      operationId: startCrewExecution
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - inputs
              properties:
                inputs:
                  type: object
                  description: Key-value pairs of all required inputs for your crew
                  additionalProperties:
                    type: string
                  example:
                    budget: "1000 USD"
                    interests: "games, tech, ai, relaxing hikes, amazing food"
                    duration: "7 days"
                    age: "35"
                meta:
                  type: object
                  description: Additional metadata to pass to the crew
                  additionalProperties: true
                  example:
                    requestId: "user-request-12345"
                    source: "mobile-app"
                taskWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each task completion
                  example: "https://your-server.com/webhooks/task"
                stepWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each agent thought/action
                  example: "https://your-server.com/webhooks/step"
                crewWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed when the crew execution completes
                  example: "https://your-server.com/webhooks/crew"
            examples:
              travel_planning:
                summary: Travel planning crew
                value:
                  inputs:
                    budget: "1000 USD"
                    interests: "games, tech, ai, relaxing hikes, amazing food"
                    duration: "7 days"
                    age: "35"
                  meta:
                    requestId: "travel-req-123"
                    source: "web-app"
              outreach_campaign:
                summary: Outreach crew with webhooks
                value:
                  inputs:
                    name: "John Smith"
                    title: "CTO"
                    company: "TechCorp"
                    industry: "Software"
                    our_product: "AI Development Platform"
                    linkedin_url: "https://linkedin.com/in/johnsmith"
                  taskWebhookUrl: "https://api.example.com/webhooks/task"
                  crewWebhookUrl: "https://api.example.com/webhooks/crew"
      responses:
        "200":
          description: Crew execution started successfully
          content:
            application/json:
              schema:
                type: object
                properties:
                  kickoff_id:
                    type: string
                    format: uuid
                    description: Unique identifier for tracking this execution
                    example: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
        "400":
          description: Invalid request body or missing required inputs
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "422":
          description: Validation error - ensure all required inputs are provided
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/ValidationError"
        "500":
          $ref: "#/components/responses/ServerError"

  /{kickoff_id}/status:
    get:
      summary: Get Execution Status
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Retrieves the current status and results of a crew execution using its kickoff ID.

        The response structure varies depending on the execution state:
        - **running**: Execution in progress with current task info
        - **completed**: Execution finished with full results
        - **error**: Execution failed with error details
      operationId: getExecutionStatus
      parameters:
        - name: kickoff_id
          in: path
          required: true
          description: The kickoff ID returned from the /kickoff endpoint
          schema:
            type: string
            format: uuid
            example: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
      responses:
        "200":
          description: Successfully retrieved execution status
          content:
            application/json:
              schema:
                oneOf:
                  - $ref: "#/components/schemas/ExecutionRunning"
                  - $ref: "#/components/schemas/ExecutionCompleted"
                  - $ref: "#/components/schemas/ExecutionError"
              examples:
                running:
                  summary: Execution in progress
                  value:
                    status: "running"
                    current_task: "research_task"
                    progress:
                      completed_tasks: 1
                      total_tasks: 3
                completed:
                  summary: Execution completed successfully
                  value:
                    status: "completed"
                    result:
                      output: "Comprehensive travel itinerary for 7 days in Japan focusing on tech culture..."
                      tasks:
                        - task_id: "research_task"
                          output: "Research findings on tech destinations in Japan..."
                          agent: "Travel Researcher"
                          execution_time: 45.2
                        - task_id: "planning_task"
                          output: "7-day detailed itinerary with activities and recommendations..."
                          agent: "Trip Planner"
                          execution_time: 62.8
                    execution_time: 108.5
                error:
                  summary: Execution failed
                  value:
                    status: "error"
                    error: "Task execution failed: Invalid API key for external service"
                    execution_time: 23.1
        "401":
          $ref: "#/components/responses/UnauthorizedError"
        "404":
          description: Kickoff ID not found
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Error"
              example:
                error: "Execution not found"
                message: "No execution found with ID: abcd1234-5678-90ef-ghij-klmnopqrstuv"
        "500":
          $ref: "#/components/responses/ServerError"

  /resume:
    post:
      summary: Resume Crew Execution with Human Feedback
      description: |
        **📋 Reference Example Only** - *This shows the request format. To test with your actual crew, copy the cURL example and replace the URL + token with your real values.*

        Resume a paused crew execution with human feedback for Human-in-the-Loop (HITL) workflows.
        When a task with `human_input=True` completes, the crew execution pauses and waits for human feedback.

        **IMPORTANT**: You must provide the same webhook URLs (`taskWebhookUrl`, `stepWebhookUrl`, `crewWebhookUrl`)
        that were used in the original kickoff call. Webhook configurations are NOT automatically carried over -
        they must be explicitly provided in the resume request to continue receiving notifications.
      operationId: resumeCrewExecution
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
                - execution_id
                - task_id
                - human_feedback
                - is_approve
              properties:
                execution_id:
                  type: string
                  format: uuid
                  description: The unique identifier for the crew execution (from kickoff)
                  example: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
                task_id:
                  type: string
                  description: The ID of the task that requires human feedback
                  example: "research_task"
                human_feedback:
                  type: string
                  description: Your feedback on the task output. This will be incorporated as additional context for subsequent task executions.
                  example: "Great research! Please add more details about recent developments in the field."
                is_approve:
                  type: boolean
                  description: "Whether you approve the task output: true = positive feedback (continue), false = negative feedback (retry task)"
                  example: true
                taskWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each task completion. MUST be provided to continue receiving task notifications.
                  example: "https://your-server.com/webhooks/task"
                stepWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed after each agent thought/action. MUST be provided to continue receiving step notifications.
                  example: "https://your-server.com/webhooks/step"
                crewWebhookUrl:
                  type: string
                  format: uri
                  description: Callback URL executed when the crew execution completes. MUST be provided to receive completion notification.
                  example: "https://your-server.com/webhooks/crew"
            examples:
              approve_and_continue:
                summary: Approve task and continue execution
                value:
                  execution_id: "abcd1234-5678-90ef-ghij-klmnopqrstuv"
                  task_id: "research_task"
                  human_feedback: "Excellent research! Proceed to the next task."
                  is_approve: true
 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
