---
id: guardrails
type: knowledge
owner: OA_Triage
---
# guardrails
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# NeMo Guardrails

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![PyPI](https://img.shields.io/pypi/v/nemoguardrails)](https://pypi.org/project/nemoguardrails)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nemoguardrails)](https://pypi.org/project/nemoguardrails)
[![Tests/Linux](https://img.shields.io/github/actions/workflow/status/NVIDIA-NeMo/Guardrails/pr-tests.yml?logo=github&label=Tests%2FLinux)](https://github.com/NVIDIA-NeMo/Guardrails/actions/workflows/pr-tests.yml)
[![Tests/Windows](https://img.shields.io/github/actions/workflow/status/NVIDIA-NeMo/Guardrails/full-tests.yml?logo=github&label=Tests%2FWindows)](https://github.com/NVIDIA-NeMo/Guardrails/actions/workflows/full-tests.yml)
[![Tests/macOS](https://img.shields.io/github/actions/workflow/status/NVIDIA-NeMo/Guardrails/full-tests.yml?logo=github&label=Tests%2FmacOS)](https://github.com/NVIDIA-NeMo/Guardrails/actions/workflows/full-tests.yml)
[![Lint](https://img.shields.io/github/actions/workflow/status/NVIDIA-NeMo/Guardrails/lint.yml?logo=github&label=Lint)](https://github.com/NVIDIA-NeMo/Guardrails/actions/workflows/lint.yml)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Documentation](https://img.shields.io/badge/docs-nvidia.com-blue.svg)](https://docs.nvidia.com/nemo/guardrails)
[![arXiv](https://img.shields.io/badge/cs.CL-arXiv%3A2310.10501-b31b1b.svg)](https://arxiv.org/abs/2310.10501)
[![Downloads](https://static.pepy.tech/badge/nemoguardrails)](https://pepy.tech/project/nemoguardrails)
[![Downloads](https://static.pepy.tech/badge/nemoguardrails/month)](https://pepy.tech/project/nemoguardrails)

> **LATEST RELEASE / DEVELOPMENT VERSION**: The [main](https://github.com/NVIDIA-NeMo/Guardrails/tree/main) branch tracks the latest released beta version: [0.21.0](https://github.com/NVIDIA-NeMo/Guardrails/tree/v0.21.0). For the latest development version, checkout the [develop](https://github.com/NVIDIA-NeMo/Guardrails/tree/develop) branch.

✨✨✨

📌 **The official NeMo Guardrails documentation has moved to [docs.nvidia.com/nemo/guardrails](https://docs.nvidia.com/nemo/guardrails).**

✨✨✨

NeMo Guardrails is an open-source toolkit for easily adding *programmable guardrails* to LLM-based conversational applications. Guardrails (or "rails" for short) are specific ways of controlling the output of a large language model, such as not talking about politics, responding in a particular way to specific user requests, following a predefined dialog path, using a particular language style, extracting structured data, and more.

[This paper](https://arxiv.org/abs/2310.10501) introduces NeMo Guardrails and contains a technical overview of the system and the current evaluation.

## Requirements

Python 3.10, 3.11, 3.12 or 3.13.

NeMo Guardrails uses [annoy](https://github.com/spotify/annoy) which is a C++ library with Python bindings. To install NeMo Guardrails you will need to have the C++ compiler and dev tools installed. Check out the [Installation Guide](https://docs.nvidia.com/nemo/guardrails/getting-started/installation-guide.html#prerequisites) for platform-specific instructions.

## Installation

To install using pip:

```bash
> pip install nemoguardrails
```

For more detailed instructions, see the [Installation Guide](https://docs.nvidia.com/nemo/guardrails/getting-started/installation-guide.html).

## Overview

<!-- start-documentation-reuse -->

NeMo Guardrails enables developers building LLM-based applications to easily add **programmable guardrails** between the application code and the LLM.

<div align="center">
  <img src="https://github.com/NVIDIA-NeMo/Guardrails/raw/develop/docs/_static/images/programmable_guardrails.png"  width="75%" alt="Programmable Guardrails">
</div>

Key benefits of adding *programmable guardrails* include:

- **Building Trustworthy, Safe, and Secure LLM-based Applications:** you can define rails to guide and safeguard conversations; you can choose to define the behavior of your LLM-based application on specific topics and prevent it from engaging in discussions on unwanted topics.

- **Connecting models, chains, and other services securely:** you can connect an LLM to other services (a.k.a. tools) seamlessly and securely.

- **Controllable dialog**: you can steer the LLM to follow pre-defined conversational paths, allowing you to design the interaction following conversation design best practices and enforce standard operating procedures (e.g., authentication, support).

<!-- end-documentation-reuse -->

### Protecting against LLM Vulnerabilities

NeMo Guardrails provides several mechanisms for protecting an LLM-powered chat application against common LLM vulnerabilities, such as jailbreaks and prompt injections. Below is a sample overview of the protection offered by different guardrails configuration for the example [ABC Bot](./examples/bots/abc) included in this repository. For more details, please refer to the [LLM Vulnerability Scanning](https://docs.nvidia.com/nemo/guardrails/evaluation/llm-vulnerability-scanning.html) page.

<div align="center">
<img src="https://github.com/NVIDIA-NeMo/Guardrails/raw/develop/docs/_static/images/abc-llm-vulnerability-scan-results.png" width="500">
</div>

### Use Cases

You can use programmable guardrails in different types of use cases:

1. **Question Answering** over a set of documents (a.k.a. Retrieval Augmented Generation): Enforce fact-checking and output moderation.
2. **Domain-specific Assistants** (a.k.a. chatbots): Ensure the assistant stays on topic and follows the designed conversational flows.
3. **LLM Endpoints**: Add guardrails to your custom LLM for safer customer interaction.
4. **LangChain Chains**: If you use LangChain for any use case, you can add a guardrails layer around your chains.

### Usage

To add programmable guardrails to your application you can use the Python API or a guardrails server (see the [Server Guide](https://docs.nvidia.com/nemo/guardrails/user-guides/server-guide.html) for more details). Using the Python API is similar to using the LLM directly. Calling the guardrails layer instead of the LLM requires only minimal changes to the code base, and it involves two simple steps:

1. Loading a guardrails configuration and creating an `LLMRails` instance.
2. Making the calls to the LLM using the `generate`/`generate_async` methods.

```python
from nemoguardrails import LLMRails, RailsConfig

# Load a guardrails configuration from the specified path.
config = RailsConfig.from_path("PATH/TO/CONFIG")
rails = LLMRails(config)

completion = rails.generate(
    messages=[{"role": "user", "content": "Hello world!"}]
)
```

Sample output:

```json
{"role": "assistant", "content": "Hi! How can I help you?"}
```

The input and output format for the `generate` method is similar to the [Chat Completions API](https://platform.openai.com/docs/guides/gpt/chat-completions-api) from OpenAI.

#### Async API

NeMo Guardrails is an async-first toolkit as the core mechanics are implemented using the Python async model. The public methods have both a sync and an async version. For example: `LLMRails.generate` and `LLMRails.generate_async`.

### Supported LLMs

You can use NeMo Guardrails with multiple LLMs like OpenAI GPT-3.5, GPT-4, LLaMa-2, Falcon, Vicuna, or Mosaic. For more details, check out the [Supported LLM Models](https://docs.nvidia.com/nemo/guardrails/user-guides/configuration-guide.html#supported-llm-models) section in the Configuration Guide.

### Types of Guardrails

NeMo Guardrails supports five main types of guardrails:

<div align="center">
  <img src="https://github.com/NVIDIA-NeMo/Guardrails/raw/develop/docs/_static/images/programmable_guardrails_flow.png"  width="75%" alt="Programmable Guardrails Flow">
</div>

1. **Input rails**: applied to the input from the user; an input rail can reject the input, stopping any additional processing, or alter the input (e.g., to mask potentially sensitive data, to rephrase).

2. **Dialog rails**: influence how the LLM is prompted; dialog rails operate on canonical form messages for details see [Colang Guide](https://docs.nvidia.com/nemo/guardrails/user-guides/colang-language-syntax-guide.html)) and determine if an action should be executed, if the LLM should be invoked to generate the next step or a response, if a predefined response should be used instead, etc.

3. **Retrieval rails**: applied to the retrieved chunks in the case of a RAG (Retrieval Augmented Generation) scenario; a retrieval rail can reject a chunk, preventing it from being used to prompt the LLM, or alter the relevant chunks (e.g., to mask potentially sensitive data).

4. **Execution rails**: applied to input/output of the custom actions (a.k.a. tools), that need to be called by the LLM.

5. **Output rails**: applied to the output generated by the LLM; an output rail can reject the output, preventing it from being returned to the user, or alter it (e.g., removing sensitive data).

### Guardrails Configuration

A guardrails configuration defines the **LLM(s)** to be used and **one or more guardrails**. A guardrails configuration can include any number of input/dialog/output/retrieval/execution rails. A configuration without any configured rails will essentially forward the requests to the LLM.

The standard structure for a guardrails configuration folder looks like this:

```
.
├── config
│   ├── actions.py
│   ├── config.py
│   ├── config.yml
│   ├── rails.co
│   ├── ...
```

The `config.yml` contains all the general configuration options, such as LLM models, active rails, and custom configuration data". The `config.py` file contains any custom initialization code and the `actions.py` contains any custom python actions. For a complete overview, see the [Configuration Guide](https://docs.nvidia.com/nemo/guardrails/user-guides/configuration-guide.html).

Below is an example `config.yml`:

```yaml
# config.yml
models:
  - type: main
    engine: openai
    model: gpt-3.5-turbo-instruct

rails:
  # Input rails are invoked when new input from the user is received.
  input:
    flows:
      - check jailbreak
      - mask sensitive data on input

  # Output rails are triggered after a bot message has been generated.
  output:
    flows:
      - self check facts
      - self check hallucination
      - activefence moderation on input

  config:
    # Configure the types of entities that should be masked on user input.
    sensitive_data_detection:
      input:
        entities:
          - PERSON
          - EMAIL_ADDRESS
```

The `.co` files included in a guardrails configuration contain the Colang definitions (see the next section for a quick overview of what Colang is) that define various types of rails. Below is an example `greeting.co` file which defines the dialog rails for greeting the user.

```colang
define user express greeting
  "Hello!"
  "Good afternoon!"

define flow
  user express greeting
  bot express greeting
  bot offer to help

define bot express greeting
  "Hello there!"

define bot offer to help
  "How can I help you today?"
```

Below is an additional example of Colang definitions for a dialog rail against insults:

```colang
define user express insult
  "You are stupid"

define flow
  user express insult
  bot express calmly willingness to help
```

### Colang

To configure and implement various types of guardrails, this toolkit introduces **Colang**, a modeling language specifically created for designing flexible, yet controllable, dialogue flows. Colang has a python-like syntax and is designed to be simple and intuitive, especially for developers.

```{note}
Two versions of Colang, 1.0 and 2.0, are supported and Colang 1.0 is the default.
```

For a brief introduction to the Colang 1.0 syntax, see the [Colang 1.0 Language Syntax Guide](https://docs.nvidia.com/nemo/guardrails/user-guides/colang-language-syntax-guide.html).

To get started with Colang 2.0, see the [Colang 2.0 Documentation](https://docs.nvidia.com/nemo/guardrails/colang-2/overview.html).

### Guardrails Library

NeMo Guardrails comes with a set of [built-in guardrails](https://docs.nvidia.com/nemo/guardrails/user-guides/guardrails-library.html).

```{note}
The built-in guardrails may or may not be suitable for a given production use case. As always, developers should work with their internal application team to ensure guardrails meets requirements for the relevant industry and use case and address unforeseen product misuse.
```

The library includes guardrails for LLM self-checking (input/output moderation, fact-checking, hallucination detection), NVIDIA safety models (content safety, topic safety), jailbreak and injection detection, and integrations with community models and third-party APIs. For the complete list, see the [Guardrails Library documentation](https://docs.nvidia.com/nemo/guardrails/user-guides/guardrails-library.html).

## CLI

NeMo Guardrails also comes with a built-in CLI.

```bash
$ nemoguardrails --help

Usage: nemoguardrails [OPTIONS] COMMAND [ARGS]...

actions-server    Start a NeMo Guardrails actions server.
chat              Start an interactive chat session.
evaluate          Run an evaluation task.
server            Start a NeMo Guardrails server.
```

### Guardrails Server

You can use the NeMo Guardrails CLI to start a guardrails server. The server can load one or more configurations from the specified folder and expose and HTTP API for using them.

```
nemoguardrails server [--config PATH/TO/CONFIGS] [--port PORT]
```

For example, to get a chat completion for a `sample` config, you can use the `/v1/chat/completions` endpoint:

```
POST /v1/chat/completions
```

```json
{
    "config_id": "sample",
    "messages": [{
      "role":"user",
      "content":"Hello! What can you do for me?"
    }]
}
```

Sample output:

```json
{"role": "assistant", "content": "Hi! How can I help you?"}
```

#### Docker

To start a guardrails server, you can also use a Docker container. NeMo Guardrails provides a [Dockerfile](./Dockerfile) that you can use to build a `nemoguardrails` image. For further information, see the [using Docker](https://docs.nvidia.com/nemo/guardrails/user-guides/advanced/using-docker.html) section.

## Integration with LangChain

NeMo Guardrails integrates seamlessly with LangChain. You can easily wrap a guardrails configuration around a LangChain chain (or any `Runnable`). You can also call a LangChain chain from within a guardrails configuration. For more details, check out the [LangChain Integration Documentation](https://docs.nvidia.com/nemo/guardrails/user-guides/langchain/langchain-integration.html)

## Evaluation

Evaluating the safety of a LLM-based conversational application is a complex task and still an open research question. To support proper evaluation, NeMo Guardrails provides the following:

1. An [evaluation tool](nemoguardrails/evaluate/README.md), i.e. `nemo
... [TRUNCATED]
```

### File: benchmark\README.md
```md
# Guardrails Benchmarking

NeMo Guardrails includes benchmarking tools to help users capacity-test their Guardrails applications.
Adding guardrails to an LLM-based application improves safety and security, while adding some latency. These benchmarks allow users to quantify the tradeoff between security and latency, to make data-driven decisions.
We currently have a simple testbench, which runs the Guardrails server with mocks as Guardrail and Application models. This can be used for performance-testing on a laptop without any GPUs, and run in a few minutes.

-----

## Guardrails Core Benchmarking

This benchmark measures the performance of the Guardrails application, running on CPU-only laptop or instance.
It doesn't require GPUs on which to run local models, or access to the internet to use models hosted by providers.
All models use the [Mock LLM Server](mock_llm_server), which is a simplified model of an LLM used for inference.
The aim of this benchmark is to detect performance-regressions as quickly as running unit-tests.

## Quickstart: Running Guardrails with Mock LLMs

To run Guardrails with mocks for both the content-safety and main LLM, follow the steps below.
All commands must be run in the `benchmark` directory.

### 1. Set up benchmarking virtual environment

The benchmarking tools have their own dependencies, which are managed using a virtual environment, pip, and the [requirements.txt](requirements.txt) file.
In this section, you'll create a new virtual environment, activate it, and install all the dependencies needed to benchmark Guardrails.

First you'll create the virtual environment and install dependencies.

```shell
# Create a virtual environment under ~/env/benchmark_env and activate it

$ cd benchmark
$ mkdir ~/env
$ python -m venv ~/env/benchmark_env
$ pip install -r requirements.txt
...
Successfully installed fastapi-0.128.0 honcho-2.0.0 httpx-0.28.1 langchain-core-1.2.5 numpy-2.4.0 pydantic-2.12.5 pydantic-core-2.41.5 pydantic-settings-2.12.0 pyyaml-6.0.3 typer-0.21.0 typing-inspection-0.4.2 uuid-utils-0.12.0 uvicorn-0.40.0
$ source ~/env/benchmark_env/bin/activate
(benchmark_env) $
```

### 2. Run Guardrails with Mock LLMs for Content-Safety and Application LLM

Now we can start up the processes that are part of the [Procfile](Procfile).
As the Procfile processes spin up, they log to the console with a prefix. The `system` prefix is used by Honcho, `app_llm` is the Application or Main LLM mock, `cs_llm` is the content-safety mock, and `gr` is the Guardrails service. We'll explore the Procfile in more detail below.
Once the three 'Uvicorn running on ...' messages are printed, you can move to the next step. Note these messages are likely not on consecutive lines.

```shell
# These commands must be run in the benchmark directory after activating the benchmark_env virtual environment

(benchmark_env) $ honcho start
13:40:33 system    | gr.1 started (pid=93634)
13:40:33 system    | app_llm.1 started (pid=93635)
13:40:33 system    | cs_llm.1 started (pid=93636)
...
13:40:41 app_llm.1 | INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
...
13:40:41 cs_llm.1  | INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
...
13:40:45 gr.1      | INFO:     Uvicorn running on http://0.0.0.0:9000 (Press CTRL+C to quit)
```

### 3. Validate services are running correctly

Once Guardrails and the mock servers are up, we'll use the [validate_mocks.sh](scripts/validate_mocks.sh) script to validate everything is working.
This doesn't require the `benchmark_env` virtual environment since we're running curl commands in the script.

```shell
# In a new shell, change into the benchmark directory and run these commands.

$ cd benchmark
$ scripts/validate_mocks.sh
Starting LLM endpoint health check...

--- Checking Port: 8000 ---
Checking http://localhost:8000/health ...
Health Check PASSED: Status is 'healthy'.
Checking http://localhost:8000/v1/models for 'meta/llama-3.3-70b-instruct'...
Model Check PASSED: Found 'meta/llama-3.3-70b-instruct' in model list.
--- Port 8000: ALL CHECKS PASSED ---

--- Checking Port: 8001 ---
Checking http://localhost:8001/health ...
Health Check PASSED: Status is 'healthy'.
Checking http://localhost:8001/v1/models for 'nvidia/llama-3.1-nemoguard-8b-content-safety'...
Model Check PASSED: Found 'nvidia/llama-3.1-nemoguard-8b-content-safety' in model list.
--- Port 8001: ALL CHECKS PASSED ---

--- Checking Port: 9000 (Rails Config) ---
Checking http://localhost:9000/v1/rails/configs ...
HTTP Status PASSED: Got 200.
Body Check PASSED: Response is an array with at least one entry.
--- Port 9000: ALL CHECKS PASSED ---

--- Final Summary ---
Port 8000 (meta/llama-3.3-70b-instruct): PASSED
Port 8001 (nvidia/llama-3.1-nemoguard-8b-content-safety): PASSED
Port 9000 (Rails Config): PASSED
---------------------
Overall Status: All endpoints are healthy!
```

### 4. Make Guardrails requests

Once the mocks and Guardrails are running and the script passes, we can issue curl requests against the Guardrails `/chat/completions` endpoint to generate a response and test the system end-to-end.

```shell
 $ curl -s -X POST http://0.0.0.0:9000/v1/chat/completions \
   -H 'Accept: application/json' \
   -H 'Content-Type: application/json' \
   -d '{
      "model": "meta/llama-3.3-70b-instruct",
      "messages": [
         {
            "role": "user",
            "content": "what can you do for me?"
         }
      ],
      "stream": false
    }' | jq

{
  "messages": [
    {
      "role": "assistant",
      "content": "I can provide information and help with a wide range of topics, from science and history to entertainment and culture. I can also help with language-related tasks, such as translation and text summarization. However, I can't assist with requests that involve harm or illegal activities."
    }
  ]
}
```

------

## Deep-Dive: Configuration

In this section, we'll examine the configuration files used in the quickstart above. This gives more context on how the system works, and can be extended as needed.

### Procfile

The [Procfile](Procfile) contains all the processes that make up the application.
The Honcho package reads in this file, starts all the processes, and combines their logs to the console
The `gr` line runs the Guardrails server on port 9000 and sets the default Guardrails configuration as [content_safety_local](../examples/configs/content_safety_local).
The `app_llm` line runs the Application or Main Mock LLM. Guardrails calls this LLM to generate a response to the user's query. This server uses 4 uvicorn workers and runs on port 8000. The configuration file here is a Mock LLM configuration, not a Guardrails configuration.
The `cs_llm` line runs the Content-Safety Mock LLM. This uses 4 uvicorn workers and runs on port 8001.

### Guardrails Configuration

The [Guardrails Configuration](../examples/configs/content_safety_local/config.yml) is used by the Guardrails server.
Under the `models` section, the `main` model is used to generate responses to the user queries. The base URL for this model is the `app_llm` Mock LLM from the Procfile, running on port 8000. The `model` field has to match the Mock LLM model name.
The `content_safety` model is configured for use in an input and output rail. The `type` field matches the `$model` used in the input and output flows.

### Mock LLM Endpoints

The Mock LLM implements a subset of the OpenAI LLM API.
There are two Mock LLM configurations, one for the Mock [main model](mock_llm_server/configs/meta-llama-3.3-70b-instruct.env), and another for the Mock [content-safety](mock_llm_server/configs/nvidia-llama-3.1-nemoguard-8b-content-safety.env) model.
The Mock LLM has the following OpenAI-compatible endpoints:

* `/health`: Returns a JSON object with status set to healthy and timestamp in seconds-since-epoch. For example `{"status":"healthy","timestamp":1762781239}`
* `/v1/models`: Returns the `MODEL` field from the Mock configuration (see below). For example `{"object":"list","data":[{"id":"meta/llama-3.3-70b-instruct","object":"model","created":1762781290,"owned_by":"system"}]}`
* `/v1/completions`: Returns an [OpenAI completion object](https://platform.openai.com/docs/api-reference/completions/object) using the Mock configuration (see below).
* `/v1/chat/completions`: Returns an [OpenAI chat completion object](https://platform.openai.com/docs/api-reference/chat/object) using the Mock configuration (see below).

### Mock LLM Configuration

Mock LLMs are configured using the `.env` file format. These files are passed to the Mock LLM using the `--config-file` argument.
The Mock LLMs return either a `SAFE_TEXT` or `UNSAFE_TEXT` response to `/v1/completions` or `/v1/chat/completions` inference requests.
The probability of the `UNSAFE_TEXT` being returned if given by `UNSAFE_PROBABILITY`.
The latency of each response is also controllable, and works as follows:

* Latency is first sampled from a normal distribution with mean `LATENCY_MEAN_SECONDS` and standard deviation `LATENCY_STD_SECONDS`.
* If the sampled value is less than `LATENCY_MIN_SECONDS`, it is set to `LATENCY_MIN_SECONDS`.
* If the sampled value is less than `LATENCY_MAX_SECONDS`, it is set to `LATENCY_MAX_SECONDS`.

The full list of configuration fields is shown below:

* `MODEL`: The Model name served by the Mock LLM. This will be returned on the `/v1/models` endpoint.
* `UNSAFE_PROBABILITY`: Probability of an unsafe response. This must be in the range [0, 1].
* `UNSAFE_TEXT`: String returned as an unsafe response.
* `SAFE_TEXT`: String returned as a safe response.
* `LATENCY_MIN_SECONDS`: Minimum latency in seconds.
* `LATENCY_MAX_SECONDS`: Maximum latency in seconds.
* `LATENCY_MEAN_SECONDS`: Normal distribution mean from which to sample latency.
* `LATENCY_STD_SECONDS`: Normal distribution standard deviation from which to sample latency.

```

### File: benchmark\requirements.txt
```txt
# Runtime dependencies for benchmark tools
#
# Install with: pip install -r requirements.txt
#
# Note: Version constraints are aligned with the main nemoguardrails package
# where applicable to ensure compatibility.

# --- general dependencies ---
honcho>=2.0.0

# --- mock_llm_server dependencies ---
fastapi>=0.103.0
uvicorn>=0.23
pydantic>=2.0
pydantic-settings>=2.0
numpy>=2.3.2

# --- aiperf dependencies ---
httpx>=0.24.1
typer>=0.8
pyyaml>=6.0

# --- locust load testing dependencies ---
locust>=2.0.0

```

### File: docs\README.md
```md
# Documentation

## Product Documentation

Product documentation for the toolkit is available at
<https://docs.nvidia.com/nemo/guardrails>.

## Building the Documentation

1. Make sure you installed the `docs` dependencies.
   Refer to [CONTRIBUTING.md](../CONTRIBUTING.md) for more information about Poetry and dependencies.

   ```console
   poetry install --with docs
   ```

1. Build the documentation:

   ```console
   make docs
   ```

   The HTML is created in the `_build/docs` directory.

## Live Documentation Server

For local development with automatic rebuilding on file changes, use one of the following methods:

### Option 1: Using the Shell Script (Recommended for Unix/Mac)

```bash
cd docs
./serve.sh [port]
```

Default port is 8000. The server will automatically rebuild documentation when you save changes to any source file.

### Option 2: Using the Python Script (Cross-Platform)

```bash
cd docs
python serve.py [--port PORT] [--host HOST] [--open]
```

Options:

- `--port PORT`: Port to serve on (default: 8000)
- `--host HOST`: Host to bind to (default: 0.0.0.0)
- `--open`: Automatically open browser

Examples:

```bash
# Start server on default port (8000)
python serve.py

# Start server on custom port with auto-open browser
python serve.py --port 8080 --open

# Start server accessible only from localhost
python serve.py --host 127.0.0.1
```

### Option 3: Direct sphinx-autobuild Command

```bash
cd docs
sphinx-autobuild . _build/html --port 8000 --open-browser
```

Once the server is running:

- Open your browser to `http://127.0.0.1:8000`
- Edit any documentation file (`.md`, `.rst`, `.py` configs)
- Save the file
- The browser will automatically refresh with the updated content

Press `Ctrl+C` to stop the server.

## Publishing the Documentation

Tag the commit to publish with `docs-v<semver>`.
Push the tag to GitHub.

To avoid publishing the documentation as the latest, ensure the commit has `/not-latest` on a single line, tag that commit, and push to GitHub.

```

### File: examples\bots\README.md
```md
# Example Bots

The examples in this folder showcase various configurations of guardrails. You can use them as a starting point for different types of bots you want to build with NeMo Guardrails.

1. [Hello World](./hello_world): basic starter configuration.
2. [ABC Bot](./abc): more advanced configuration using topical rails, input and output moderation and retrieval augmented generation, etc.

```

### File: examples\configs\README.md
```md
# Example Configurations

The configurations in this folder showcase various features of NeMo Guardrails, e.g., using a specific LLM, enabling streaming, enabling fact-checking, etc. These configurations are kept very simple and focused.

```

### File: examples\configs\tracing\README.md
```md
# NeMo Guardrails Tracing

This guide explains how to set up tracing with NeMo Guardrails to monitor and debug your guardrails interactions.

## What is Tracing?

Tracing helps you understand what happens inside your guardrails:

- Track which rails are activated
- Monitor LLM calls and responses
- Debug performance issues
- Analyze conversation flows

## Quick Start

### 1. Try the Working Example

The fastest way to see tracing in action:

```bash
# Install tracing support with SDK (needed for examples)
pip install nemoguardrails[tracing] opentelemetry-sdk

cd examples/configs/tracing/
python working_example.py
```

This will show traces printed to your console immediately.

### 2. Basic Configuration

Enable tracing in your `config.yml`:

```yaml
tracing:
  enabled: true
  adapters:
    - name: FileSystem
```

Or use OpenTelemetry (requires additional setup):

```yaml
tracing:
  enabled: true
  adapters:
    - name: OpenTelemetry
```

## Available Tracing Adapters

### FileSystem Adapter (Easiest)

Logs traces to local JSON files which is a good option for development and debugging:

```yaml
tracing:
  enabled: true
  adapters:
    - name: FileSystem
      filepath: "./logs/traces.jsonl"
```

**When to use**: Development, debugging, simple logging needs.

### OpenTelemetry Adapter

```yaml
tracing:
  enabled: true
  adapters:
    - name: OpenTelemetry
```

**When to use**: Production environments, integration with monitoring systems, distributed applications.

## OpenTelemetry Ecosystem Compatibility

**NeMo Guardrails is compatible with the entire OpenTelemetry ecosystem.** The examples below show common configurations, but you can use any OpenTelemetry compatible:

- **Exporters**: Jaeger, Zipkin, Prometheus, New Relic, Datadog, AWS X-Ray, Google Cloud Trace, and many more
- **Collectors**: OpenTelemetry Collector, Jaeger Collector, custom collectors
- **Backends**: Any system that accepts OpenTelemetry traces

For the complete list of supported exporters, see the [OpenTelemetry Registry](https://opentelemetry.io/ecosystem/registry/).

### Custom Adapter

Implement your own adapter for specific requirements:

```python
from nemoguardrails.tracing.adapters.base import InteractionLogAdapter

class MyCustomAdapter(InteractionLogAdapter):
    name = "MyCustomAdapter"

    def transform(self, interaction_log):
        # your custom logic here
        pass
```

## OpenTelemetry Setup

### Understanding the Architecture

- **NeMo Guardrails**: Uses only the OpenTelemetry API (doesn't configure anything)
- **Your Application**: Configures the OpenTelemetry SDK and exporters

This means you must configure OpenTelemetry in your application code.

### Installation

#### For Tracing Support (API only)

```bash
# minimum requirement for NeMo Guardrails tracing features
pip install nemoguardrails[tracing]
```

This installs only the OpenTelemetry API, which is sufficient if your application already configures OpenTelemetry.

#### For Running Examples and Development

```bash
# includes OpenTelemetry SDK for configuring exporters
pip install nemoguardrails[tracing] opentelemetry-sdk
```

#### For Production Deployments

```bash
# install tracing support
pip install nemoguardrails[tracing]

# install SDK and your preferred exporter
# for OTLP
pip install opentelemetry-sdk opentelemetry-exporter-otlp
# OR for Jaeger
pip install opentelemetry-sdk opentelemetry-exporter-jaeger
# OR for Zipkin
pip install opentelemetry-sdk opentelemetry-exporter-zipkin
```

### Configuration Examples

#### Common Examples

**Console Output** (Development/Testing):

Suitable for development which prints traces to your terminal:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter
from opentelemetry.sdk.resources import Resource

# configure OpenTelemetry (do this before using NeMo Guardrails)
resource = Resource.create({
    "service.name": "my-guardrails-app",
    "service.version": "1.0.0",
}, schema_url="https://opentelemetry.io/schemas/1.26.0")

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

# use console exporter (prints to terminal)
console_exporter = ConsoleSpanExporter()
span_processor = BatchSpanProcessor(console_exporter)
tracer_provider.add_span_processor(span_processor)

# now configure NeMo Guardrails
from nemoguardrails import LLMRails, RailsConfig

config = RailsConfig.from_content(
    config={
        "models": [{"type": "main", "engine": "openai", "model": "gpt-3.5-turbo-instruct"}],
        "tracing": {
            "enabled": True,
            "adapters": [{"name": "OpenTelemetry"}]
        }
    }
)

rails = LLMRails(config)
response = rails.generate(messages=[{"role": "user", "content": "Hello!"}])
```

**OTLP Exporter** (Production-ready):

For production use with observability platforms:

```bash
# install OTLP exporter
pip install opentelemetry-exporter-otlp
```

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import Resource

# configure OpenTelemetry
resource = Resource.create({
    "service.name": "my-guardrails-app",
    "service.version": "1.0.0",
}, schema_url="https://opentelemetry.io/schemas/1.26.0")

tracer_provider = TracerProvider(resource=resource)
trace.set_tracer_provider(tracer_provider)

# configure OTLP exporter
otlp_exporter = OTLPSpanExporter(
    endpoint="http://localhost:4317",  # Your OTLP collector endpoint
    insecure=True
)

span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)

# use with NeMo Guardrails (same as console example)
```

> **Note**: These examples show popular configurations, but OpenTelemetry supports many more exporters and backends. You can integrate with any OpenTelemetry-compatible observability platform by installing the appropriate exporter package and configuring it in your application code.

## Additional Integration Examples

These are just a few examples of the many OpenTelemetry integrations available:

### Zipkin Integration

1. Start Zipkin server:

```bash
docker run -d -p 9411:9411 openzipkin/zipkin
```

2. Install Zipkin exporter:

```bash
pip install opentelemetry-exporter-zipkin
```

3. Configure in your application:

```python
from opentelemetry.exporter.zipkin.proto.http import ZipkinExporter

zipkin_exporter = ZipkinExporter(
    endpoint="http://localhost:9411/api/v2/spans",
)
span_processor = BatchSpanProcessor(zipkin_exporter)
tracer_provider.add_span_processor(span_processor)
```

### OpenTelemetry Collector

Create a collector configuration file:

```yaml
# otel-config.yaml
receivers:
  otlp:
    protocols:
      grpc:
        endpoint: 0.0.0.0:4317
      http:
        endpoint: 0.0.0.0:4318

processors:
  batch:

exporters:
  logging:
    loglevel: debug

service:
  pipelines:
    traces:
      receivers: [otlp]
      processors: [batch]
      exporters: [logging]
```

Run the collector:

```bash
docker run -p 4317:4317 -p 4318:4318 \
  -v $(pwd)/otel-config.yaml:/etc/otel-collector-config.yaml \
  otel/opentelemetry-collector:latest \
  --config=/etc/otel-collector-config.yaml
```

## Migration Guide

### From Previous Versions

If you were using the old OpenTelemetry configuration:

**❌ no longer supported:**

```yaml
tracing:
  enabled: true
  adapters:
    - name: OpenTelemetry
      service_name: "my-service"
      exporter: "console"
      resource_attributes:
        env: "production"
```

**✅ supported:**

```python
# configure OpenTelemetry in your application code
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter

tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)

console_exporter = ConsoleSpanExporter()
span_processor = BatchSpanProcessor(console_exporter)
tracer_provider.add_span_processor(span_processor)

config = RailsConfig.from_content(
    config={
        "tracing": {
            "enabled": True,
            "adapters": [{"name": "OpenTelemetry"}]
        }
    }
)
```

### Deprecated Features

#### register_otel_exporter Function

The `register_otel_exporter` function is deprecated and will be removed in version 0.16.0:

```python
#  DEPRECATED - will be removed in 0.16.0
from nemoguardrails.tracing.adapters.opentelemetry import register_otel_exporter
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

register_otel_exporter("my-otlp", OTLPSpanExporter)
```

Instead, configure exporters directly in your application:

```python
from opentelemetry import trace
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

tracer_provider = TracerProvider()
trace.set_tracer_provider(tracer_provider)

otlp_exporter = OTLPSpanExporter(endpoint="http://localhost:4318")
span_processor = BatchSpanProcessor(otlp_exporter)
tracer_provider.add_span_processor(span_processor)
```

### Why the Change?

This change follows OpenTelemetry best practices:

1. **Libraries use only the API**: No configuration conflicts
2. **Applications control observability**: You decide where traces go
3. **Better compatibility**: Works with any OpenTelemetry setup

## Troubleshooting

### Common Issues

**No traces appear:**

- Ensure OpenTelemetry is configured in your application (not just NeMo Guardrails config)
- Check that your exporter is working (try `ConsoleSpanExporter` first)
- Verify tracing is enabled in your config

**Connection errors with OTLP:**

```
WARNING: Transient error StatusCode.UNAVAILABLE encountered while exporting traces to localhost:4317
```

- Make sure your collector/endpoint is running
- Use `ConsoleSpanExporter` for testing without external dependencies

**Import errors:**

```
ImportError: No module named 'opentelemetry'
```

- Install the tracing dependencies: `pip install nemoguardrails[tracing]`
- For exporters: `pip install opentelemetry-exporter-otlp`

**Wrong service name in traces:**

- Configure the `Resource` with `SERVICE_NAME` in your application code
- The old `service_name` parameter is no longer used

```

### File: .coderabbit.yaml
```yaml
# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json
# https://docs.coderabbit.ai/getting-started/configure-coderabbit/
# Validator https://docs.coderabbit.ai/configuration/yaml-validator#yaml-validator
# In PR, comment "@coderabbitai configuration" to get the full config including defaults
# Set the language for reviews by using the corresponding ISO language code.
# Default: "en-US"
language: "en-US"
# Settings related to reviews.
# Default: {}
reviews:
  # Set the profile for reviews. Assertive profile yields more feedback, that may be considered nitpicky.
  # Options: chill, assertive
  # Default: "chill"
  profile: chill
  # Add this keyword in the PR/MR title to auto-generate the title.
  # Default: "@coderabbitai"
  auto_title_placeholder: "@coderabbitai title"
  # Auto Title Instructions - Custom instructions for auto-generating the PR/MR title.
  # Default: ""
  auto_title_instructions: 'Format: "<category>: <title>". Category must be one of: feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert, cp. The category must be followed by a colon. Title should be concise (<= 80 chars). Example: "feat: Add logit_bias support".' # current: ''
  # Set the commit status to 'pending' when the review is in progress and 'success' when it is complete.
  # Default: true
  commit_status: false
  # Generate walkthrough in a markdown collapsible section.
  # Default: false
  collapse_walkthrough: true
  # Generate an assessment of how well the changes address the linked issues in the walkthrough.
  # Default: true
  assess_linked_issues: true
  # Include possibly related issues in the walkthrough.
  # Default: true
  related_issues: true
  # Related PRs - Include possibly related pull requests in the walkthrough.
  # Default: true
  related_prs: true
  # Suggest labels based on the changes in the pull request in the walkthrough.
  # Default: true
  suggested_labels: true
  # Suggest reviewers based on the changes in the pull request in the walkthrough.
  # Default: true
  suggested_reviewers: true
  # Generate a poem in the walkthrough comment.
  # Default: true
  poem: false # current: true
  # Post review details on each review. Additionally, post a review status when a review is skipped in certain cases.
  # Default: true
  review_status: false # current: true
  # Configuration for pre merge checks
  # Default: {}
  pre_merge_checks:
    # Custom Pre-merge Checks - Add unique checks to enforce your team's standards before merging a pull request. Each check must have a unique name (up to 50 characters) and clear instructions (up to 10000 characters). Use these to automatically verify coding, security, documentation, or business rules and maintain code quality.
    # Default: []
    custom_checks:
      - name: "Test Results for Major Changes"
        mode: "warning" # or "error" to block merges
        instructions: |
          If this PR contains major changes (such as new features, breaking changes, or significant refactoring), verify that the PR description includes test results or testing information.
          If a change could affect numerics or convergence, the PR description should include information demonstrating that there is no regression.
          If a change could affect performance, the PR description should include before-and-after performance numbers, as well as the configuration and context in which they apply.
          Pass if test results are documented or if the changes are minor.
  auto_review:
    # Configuration for auto review
    # Default: {}
    # Automatic Incremental Review - Automatic incremental code review on each push
    # Default: true
    auto_incremental_review: false # current: true
    # Review draft PRs/MRs.
    # Default: false
    drafts: false
    # Base branches (other than the default branch) to review. Accepts regex patterns. Use '.*' to match all branches.

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-yaml
      - id: end-of-file-fixer
      - id: trailing-whitespace

  - repo: https://github.com/astral-sh/ruff-pre-commit
    # Ruff version.
    rev: v0.14.6
    hooks:
      # Run the linter.
      - id: ruff
        args: [--fix]
      # Run the formatter.
      - id: ruff-format

  - repo: https://github.com/Lucas-C/pre-commit-hooks
    rev: v1.4.2
    hooks:
      - id: insert-license
        files: \.py$
        args:
          - --license-filepath
          - LICENSE.md
          - --use-current-year
  - repo: local
    hooks:
      - id: pyright
        name: pyright
        entry: poetry run pyright
        language: system
        types: [python]
        pass_filenames: false

```

### File: build_notebook_docs.py
```py
# SPDX-FileCopyrightText: Copyright (c) 2023-2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import re
import subprocess
from pathlib import Path

import typer
import yaml

app = typer.Typer()
app.pretty_exceptions_enable = False


def _remove_code_blocks_with_text(md_file_path, text_to_remove):
    # Define a regular expression pattern to match code blocks
    code_block_pattern = re.compile(r"```.*?```", re.DOTALL)

    # Read the content of the Markdown file
    with open(md_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Find all code blocks
    code_blocks = code_block_pattern.findall(content)

    # Filter out code blocks containing the specific text
    blocks_to_remove = [block for block in code_blocks if text_to_remove in block]

    # Remove the blocks from content
    for block in blocks_to_remove:
        content = content.replace(block, "")

    # Write the modified content back to the file
    with open(md_file_path, "w", encoding="utf-8") as file:
        file.write(content)


def _fix_prefix_and_type_in_code_blocks(md_file_path):
    # Define a regular expression pattern to match code blocks
    code_block_pattern = re.compile(r"```.*?```", re.DOTALL)

    # Read the content of the Markdown file
    with open(md_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Find all code blocks
    code_blocks = code_block_pattern.findall(content)

    for block in code_blocks:
        lines = block.split("\n")
        start_with_four_spaces = True
        for i in range(1, len(lines) - 1):
            if not lines[i].startswith("    "):
                start_with_four_spaces = False
                break

        if start_with_four_spaces:
            for i in range(1, len(lines) - 1):
                lines[i] = lines[i][4:]

            # print(f"Need to remove prefix for block:\n{block}")
            updated_block = "\n".join(lines)

            content = content.replace(block, updated_block)
            block = updated_block

        # Next, we also try to fix the type of the block using some heuristics
        if lines[0] == "```python" or lines[0] == "```":
            # If it parses correctly as a yaml file, we mark it as yaml
            try:
                data = yaml.safe_load("\n".join(lines[1:-1]))
                if isinstance(data, dict) and " " not in list(data.keys())[0]:
                    lines[0] = "```yaml"
                    updated_block = "\n".join(lines)
                    content = content.replace(block, updated_block)
                    block = updated_block
            except Exception:
                pass

        if lines[0] == "```" and "from nemoguardrails" in block:
            lines[0] = "```python"
            updated_block = "\n".join(lines)
            content = content.replace(block, updated_block)
            block = updated_block

        if lines[0].startswith("```py "):
            lines[0] = "```python"
            updated_block = "\n".join(lines)
            content = content.replace(block, updated_block)
            block = updated_block

        if lines[0].startswith("```co "):
            lines[0] = "```colang"
            updated_block = "\n".join(lines)
            content = content.replace(block, updated_block)
            block = updated_block

        if lines[0].startswith("```yml"):
            lines[0] = "```yaml"
            updated_block = "\n".join(lines)
            content = content.replace(block, updated_block)
            block = updated_block

    # Write the modified content back to the file
    with open(md_file_path, "w", encoding="utf-8") as file:
        file.write(content)


def _remove_specific_text(md_file_path, text_to_remove):
    # Read the content of the Markdown file
    with open(md_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace the specified text with an empty string
    content = content.replace(text_to_remove, "")

    # Write the modified content back to the file
    with open(md_file_path, "w", encoding="utf-8") as file:
        file.write(content)


def _post_process(md_file_path):
    # Read the content of the Markdown file
    with open(md_file_path, "r", encoding="utf-8") as file:
        content = file.read()

    content = re.sub(r"\n<!-- WARNING.*\n", "\n", content)
    content = re.sub(r"\n<.?CodeOutputBlock.*\n", "\n", content)
    content = re.sub(r"\n\n\n+", "\n\n", content)
    content = re.sub(r"\n +\n", "\n\n", content)
    content = re.sub(r"\n    \n", "\n\n", content)
    content = re.sub(r"\n\n+$", "\n", content)

    # Write the modified content back to the file
    with open(md_file_path, "w", encoding="utf-8") as file:
        file.write(content)


# Function to run the nbdoc_build command
def run_nbdoc_build(srcdir, force_all):
    try:
        # Run the nbdoc_build command with specified arguments
        subprocess.run(
            ["nbdoc_build", "--srcdir", srcdir, "--force_all", str(force_all)],
            check=True,
        )

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running nbdoc_build: {e}")
        return False
    return True


# Function to recursively rename .md files to README.md
def rename_md_to_readme(start_dir):
    generated = set()

    for path in Path(start_dir).rglob("*.md"):
        if path.name == "README.md":
            # if path.exists() and not path.absolute() in generated:
            #     path.unlink()
            continue

        # Skip processing the root directory
        if path.parent.name == "getting-started":
            continue

        # Generate the new file name, assuming the path as a directory with README.md
        readme_path = path.parent / "README.md"

        # # Skip if README.md already exists
        if readme_path.exists():
            print(f"{readme_path} already exists, deleting.")
            readme_path.unlink()

        # Rename the file
        path.rename(readme_path)
        print(f"Renamed {path} to {readme_path}")
        generated.add(readme_path.absolute())
        print(f"Adding {readme_path.absolute()}")

        # We do some additional post-processing
        _remove_code_blocks_with_text(readme_path.absolute(), "# Init:")
        _remove_code_blocks_with_text(readme_path.absolute(), "# Hide from documentation page.")

        _remove_code_blocks_with_text(
            readme_path.absolute(),
            "huggingface/tokenizers: The current process just got forked",
        )
        _remove_code_blocks_with_text(readme_path.absolute(), "Writing config/")
        _remove_code_blocks_with_text(readme_path.absolute(), "Appending to config/")
        _remove_specific_text(
            readme_path.absolute(),
            '<CodeOutputBlock lang="bash">\n\n\n\n</CodeOutputBlock>',
        )

        _fix_prefix_and_type_in_code_blocks(readme_path.absolute())

        _post_process(readme_path.absolute())


@app.command()
def convert(folder: str):
    """Convert a Jupyter notebook in the provided folder to .md.

    It creates a README.md file next to the Jupyter notebook.
    """
    print(f"Processing {folder}...")

    notebooks = [f for f in os.listdir(folder) if f.endswith(".ipynb")]

    if len(notebooks) == 0:
        raise RuntimeError(f"No .ipynb file found in {folder}.")
    elif len(notebooks) > 1:
        raise RuntimeError(f"Found {len(notebooks)} in {folder}: {notebooks}.")

    print(f"Found notebook: {notebooks[0]}")

    if run_nbdoc_build(folder, True):
        # Rename .md files if nbdev_build was successful
        rename_md_to_readme(folder)
        subprocess.run(["git", "add", "."])
        subprocess.run(["pre-commit", "run", "--all-files"])
    else:
        print("nbdoc_build command failed. Exiting without renaming .md files.")


if __name__ == "__main__":
    app()

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
