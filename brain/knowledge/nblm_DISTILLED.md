---
id: nblm
type: knowledge
owner: OA_Triage
---
# nblm
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<div align="center">

  <img width="256" alt="logo" src="https://github.com/user-attachments/assets/37f0f882-65ca-436e-8053-3db8c18cac59" />

  # _nblm-rs_

  **Unofficial NotebookLM Enterprise API client**

  🦀 **Rust CLI**: Command-line tool for shell scripting and automation <br/>
  🐍 **Python SDK**: Python bindings for integration in Python applications

  [![Crates.io](https://img.shields.io/crates/v/nblm-cli.svg)](https://crates.io/crates/nblm-cli)
  [![Crates.io](https://img.shields.io/crates/d/nblm-cli.svg?color=orange&label=downloads)](https://crates.io/crates/nblm-cli)
  <br/>
  [![PyPI](https://img.shields.io/pypi/v/nblm.svg?color=blue)](https://pypi.org/project/nblm/)
  [![PyPI Downloads](https://static.pepy.tech/personalized-badge/nblm?period=total&units=INTERNATIONAL_SYSTEM&left_color=GRAY&right_color=BLUE&left_text=downloads)](https://pepy.tech/projects/nblm)
  [![Python versions](https://img.shields.io/pypi/pyversions/nblm.svg)](https://pypi.org/project/nblm/)
  [![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
  [![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
  [![mypy](https://img.shields.io/badge/mypy-checked-blue.svg)](https://mypy-lang.org/)
  <br/>
  [![DeepWiki](https://img.shields.io/badge/DeepWiki-K--dash%2Fnblm--rs-blue.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAyCAYAAAAnWDnqAAAAAXNSR0IArs4c6QAAA05JREFUaEPtmUtyEzEQhtWTQyQLHNak2AB7ZnyXZMEjXMGeK/AIi+QuHrMnbChYY7MIh8g01fJoopFb0uhhEqqcbWTp06/uv1saEDv4O3n3dV60RfP947Mm9/SQc0ICFQgzfc4CYZoTPAswgSJCCUJUnAAoRHOAUOcATwbmVLWdGoH//PB8mnKqScAhsD0kYP3j/Yt5LPQe2KvcXmGvRHcDnpxfL2zOYJ1mFwrryWTz0advv1Ut4CJgf5uhDuDj5eUcAUoahrdY/56ebRWeraTjMt/00Sh3UDtjgHtQNHwcRGOC98BJEAEymycmYcWwOprTgcB6VZ5JK5TAJ+fXGLBm3FDAmn6oPPjR4rKCAoJCal2eAiQp2x0vxTPB3ALO2CRkwmDy5WohzBDwSEFKRwPbknEggCPB/imwrycgxX2NzoMCHhPkDwqYMr9tRcP5qNrMZHkVnOjRMWwLCcr8ohBVb1OMjxLwGCvjTikrsBOiA6fNyCrm8V1rP93iVPpwaE+gO0SsWmPiXB+jikdf6SizrT5qKasx5j8ABbHpFTx+vFXp9EnYQmLx02h1QTTrl6eDqxLnGjporxl3NL3agEvXdT0WmEost648sQOYAeJS9Q7bfUVoMGnjo4AZdUMQku50McDcMWcBPvr0SzbTAFDfvJqwLzgxwATnCgnp4wDl6Aa+Ax283gghmj+vj7feE2KBBRMW3FzOpLOADl0Isb5587h/U4gGvkt5v60Z1VLG8BhYjbzRwyQZemwAd6cCR5/XFWLYZRIMpX39AR0tjaGGiGzLVyhse5C9RKC6ai42ppWPKiBagOvaYk8lO7DajerabOZP46Lby5wKjw1HCRx7p9sVMOWGzb/vA1hwiWc6jm3MvQDTogQkiqIhJV0nBQBTU+3okKCFDy9WwferkHjtxib7t3xIUQtHxnIwtx4mpg26/HfwVNVDb4oI9RHmx5WGelRVlrtiw43zboCLaxv46AZeB3IlTkwouebTr1y2NjSpHz68WNFjHvupy3q8TFn3Hos2IAk4Ju5dCo8B3wP7VPr/FGaKiG+T+v+TQqIrOqMTL1VdWV1DdmcbO8KXBz6esmYWYKPwDL5b5FA1a0hwapHiom0r/cKaoqr+27/XcrS5UwSMbQAAAABJRU5ErkJggg==)](https://deepwiki.com/K-dash/nblm-rs)
  [![codecov](https://codecov.io/gh/K-dash/nblm-rs/graph/badge.svg?token=OhxeTdnxTw)](https://codecov.io/gh/K-dash/nblm-rs)


  
</div>

> [!IMPORTANT]
> This project targets the **NotebookLM Enterprise API** only. Google hasn’t published an API for the consumer edition or general Google Workspace tenants as of 2025-10-25.

## Motivation

In September 2025, Google released the [NotebookLM Enterprise API](https://cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview), enabling programmatic access to NotebookLM features for the first time.

While you can interact with the API using simple `curl` commands, this approach has several limitations that this project addresses:

### Challenges with Direct API Calls

- **Authentication complexity**

  - **Problem**: Managing OAuth tokens, handling token refresh, and ensuring secure credential storage
  - **Solution**: Seamless `gcloud` CLI integration with automatic token caching and refresh

- **Manual request construction**

  - **Problem**: Writing JSON payloads by hand, managing resource names, and handling API versioning
  - **Solution**: Type-safe CLI flags and Python SDK with intelligent defaults and validation

- **Error handling**

  - **Problem**: Cryptic HTTP error codes without context or recovery suggestions
  - **Solution**: Clear, actionable error messages with automatic retries for transient failures

- **Repeated operations**

  - **Problem**: Writing boilerplate loops for fetch/add/delete sequences
  - **Solution**: Higher-level client helpers and CLI flags that wrap single API calls (with retries built in) so scripts stay concise

- **Output parsing**
  - **Problem**: Manual JSON parsing and extracting specific fields from responses
  - **Solution**: Structured response objects in the Python SDK and `--json` output in the CLI for easy integration with tools like `jq`

### Project Goals

This project provides production-ready tools that make the NotebookLM API accessible and reliable:

- **Rust CLI**: Fast, cross-platform binary for shell scripting and automation
- **Python SDK**: Idiomatic Python bindings for application integration
- **Type safety**: Compile-time checks prevent common API usage errors
- **Developer experience**: Intuitive commands and clear documentation

## Installation

### CLI

```bash
# macOS
brew tap k-dash/nblm https://github.com/K-dash/homebrew-nblm
brew install k-dash/nblm/nblm

# Linux (prebuilt binaries)
# Download from Releases page: https://github.com/K-dash/nblm-rs/releases

# From source
cargo install nblm-cli
```

### Python SDK

```bash
pip install nblm
# or
uv add nblm
```

> Prerequisite: a Google Cloud project with the NotebookLM Enterprise API enabled and either `gcloud auth login` or an OAuth token ready for `NBLM_ACCESS_TOKEN`.

For detailed installation instructions and troubleshooting, see the [Installation Guide](https://k-dash.github.io/nblm-rs/getting-started/installation/).

## Quick Start

### CLI

```bash
# 1. Authenticate
gcloud auth login

# 2. Set environment variables
export NBLM_PROJECT_NUMBER="123456789012"  # Get from GCP console
export NBLM_LOCATION="global"
export NBLM_ENDPOINT_LOCATION="global"

# 3. Create a notebook
nblm notebooks create --title "My Notebook"

# 4. Add a source
nblm sources add \
  --notebook-id YOUR_NOTEBOOK_ID \
  --web-url "https://example.com" \
  --web-name "Example"
```

### Python

```python
from nblm import NblmClient, GcloudTokenProvider, WebSource

# Initialize client
client = NblmClient(
    token_provider=GcloudTokenProvider(),
    project_number="123456789012"
)

# Create a notebook
notebook = client.create_notebook(title="My Notebook")

# Add sources
response = client.add_sources(
    notebook_id=notebook.notebook_id,
    web_sources=[WebSource(url="https://example.com", name="Example")]
)
```

## Features

> [!NOTE]
> The NotebookLM API is currently in **alpha**. Some features may not work as documented due to API limitations. See the [complete feature list](https://k-dash.github.io/nblm-rs/#features) in the documentation.

nblm-rs supports the following NotebookLM API operations:

- **Notebooks**: Create, list, and delete notebooks
- **Sources**: Add web URLs, text, videos (YouTube), Google Drive files, and upload files
- **Audio Overview**: Create and delete audio overviews
- **Sharing**: Share notebooks with users (CLI only, untested)

For detailed feature status and limitations, see the [Features documentation](https://k-dash.github.io/nblm-rs/#features).

## Documentation

**Complete guides and API references:**

📖 **[Full Documentation](https://k-dash.github.io/nblm-rs/)** - Complete guides, API references, and examples

- [Getting Started](https://k-dash.github.io/nblm-rs/getting-started/installation/) - Installation, authentication, configuration
- [CLI Reference](https://k-dash.github.io/nblm-rs/cli/) - All commands, options, and examples
- [Python SDK Reference](https://k-dash.github.io/nblm-rs/python/) - API reference and usage patterns

## Known API Issues

> [!NOTE]
> The NotebookLM API is currently in **alpha** and has several known limitations. See [API Limitations](https://k-dash.github.io/nblm-rs/api/limitations/) for details.

## Related Resources

- [NotebookLM API Documentation](https://cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview) - Official API documentation
- [NotebookLM API Reference](https://cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks) - API reference

## Contributing

Contributions are welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for development setup and guidelines.

## License

MIT

```

### File: python\README.md
```md
# nblm - Python SDK for NotebookLM Enterprise API

Python bindings for the NotebookLM Enterprise API, powered by Rust via PyO3.

> **Warning**: This project is not affiliated with, sponsored, or endorsed by Google. nblm-rs is an independent, unofficial tool. It is provided "as is" without any warranty.

## Installation

```bash
pip install nblm
```

Or with uv:

```bash
uv add nblm
```

**Requirements**: Python 3.14 or later

## Quick Start

```python
from nblm import NblmClient, GCloudTokenProvider

# Initialize client
client = NblmClient(
    token_provider=GCloudTokenProvider(),
    project_number="123456789012"
)

# Create a notebook
notebook = client.create_notebook("My Notebook")
print(f"Created: {notebook.title}")

# Add sources
from nblm import WebSource

client.add_sources(
    notebook_id=notebook.notebook_id,
    web_sources=[WebSource(url="https://example.com", name="Example")]
)

# Create audio overview
audio = client.create_audio_overview(notebook.notebook_id)
print(f"Audio status: {audio.status}")
```

## Features

- **Notebooks**: Create, list, and delete notebooks
- **Sources**: Add web, text, video sources; upload files; manage sources
- **Audio Overviews**: Create podcast-style discussions from notebook content
- **Type Safety**: Full type hints for IDE autocomplete and static analysis
- **Fast**: Powered by Rust for high performance

## Authentication

### gcloud CLI (Recommended)

```python
from nblm import NblmClient, GCloudTokenProvider

client = NblmClient(
    token_provider=GCloudTokenProvider(),
    project_number="123456789012"
)
```

### Environment Variable

```python
import os
from nblm import NblmClient, EnvTokenProvider

os.environ["NBLM_ACCESS_TOKEN"] = "your-access-token"

client = NblmClient(
    token_provider=EnvTokenProvider(),
    project_number="123456789012"
)
```

### OAuth2 (Read-only)

> **Experimental:** OAuth2 support currently requires setting `NBLM_PROFILE_EXPERIMENT=1`. Users must create an OAuth 2.0 **Desktop application** client ID in Google Cloud Console, including the client secret, before running this flow.

First, run the CLI once to complete the browser flow and store a refresh token:

```bash
export NBLM_OAUTH_CLIENT_ID="123-abc.apps.googleusercontent.com"
export NBLM_OAUTH_CLIENT_SECRET="your-desktop-client-secret"
export NBLM_PROFILE_EXPERIMENT=1
nblm --auth user-oauth --project-number 123456 notebooks list
```

Then reuse that token from Python without re-authenticating:

```python
from nblm import NblmClient

client = NblmClient.with_user_oauth(
    project_number=123456,
    location="us-central1",
)
```

You can also instantiate the provider directly:

```python
from nblm import UserOAuthProvider

provider = UserOAuthProvider.from_file(project_number=123456)
```

## Documentation

**Complete Python SDK documentation:**

- [Getting Started Guide](https://github.com/K-dash/nblm-rs/blob/main/docs/getting-started/installation.md)
- [Quickstart Tutorial](https://github.com/K-dash/nblm-rs/blob/main/docs/python/quickstart.md)
- [API Reference](https://github.com/K-dash/nblm-rs/blob/main/docs/python/api-reference.md)
- [Notebooks API](https://github.com/K-dash/nblm-rs/blob/main/docs/python/notebooks.md)
- [Sources API](https://github.com/K-dash/nblm-rs/blob/main/docs/python/sources.md)
- [Audio API](https://github.com/K-dash/nblm-rs/blob/main/docs/python/audio.md)
- [Error Handling](https://github.com/K-dash/nblm-rs/blob/main/docs/python/error-handling.md)

## Examples

### Create Notebook and Add Sources

```python
from nblm import NblmClient, GCloudTokenProvider, WebSource, TextSource

client = NblmClient(
    token_provider=GCloudTokenProvider(),
    project_number="123456789012"
)

# Create notebook
notebook = client.create_notebook("Research: Python Best Practices")

# Add sources
client.add_sources(
    notebook_id=notebook.notebook_id,
    web_sources=[
        WebSource(url="https://peps.python.org/pep-0008/", name="PEP 8"),
        WebSource(url="https://docs.python-guide.org/")
    ],
    text_sources=[
        TextSource(content="Focus on code quality", name="Notes")
    ]
)
```

### Upload Files

```python
# Upload a PDF
response = client.upload_source_file(
    notebook_id=notebook.notebook_id,
    path="/path/to/document.pdf",
    display_name="Research Paper"
)
print(f"Uploaded: {response.source_id}")
```

### Error Handling

```python
from nblm import NblmError

try:
    notebook = client.create_notebook("My Notebook")
except NblmError as e:
    print(f"Error: {e}")
```

## Type Hints

The library includes full type hints:

```python
from nblm import (
    NblmClient,
    Notebook,
    NotebookSource,
    AudioOverviewResponse,
    WebSource,
    TextSource,
    VideoSource,
)

# All operations are fully typed
client: NblmClient
notebook: Notebook = client.create_notebook("Title")
audio: AudioOverviewResponse = client.create_audio_overview("abc123")
```

## Supported Operations

| Category           | Operations                                        | Status        |
| ------------------ | ------------------------------------------------- | ------------- |
| **Notebooks**      | Create, list, delete                              | Available     |
| **Sources**        | Add (web, text, video), upload files, get, delete | Available     |
| **Audio Overview** | Create, delete                                    | Available     |
| **Sharing**        | Share with users                                  | Not available |

## Links

- [GitHub Repository](https://github.com/K-dash/nblm-rs)
- [Full Documentation](https://github.com/K-dash/nblm-rs/tree/main/docs)
- [CLI Tool](https://crates.io/crates/nblm-cli)
- [Issue Tracker](https://github.com/K-dash/nblm-rs/issues)

## Contributing

See [CONTRIBUTING.md](https://github.com/K-dash/nblm-rs/blob/main/CONTRIBUTING.md) for development setup and guidelines.

## License

MIT

```

### File: docs\cli\README.md
```md
# CLI Overview

Command-line interface for the NotebookLM Enterprise API.

## Command Structure

```bash
nblm [GLOBAL_OPTIONS] <COMMAND> [COMMAND_OPTIONS]
```

## Global Options

Options that can be used with any command:

| Option                           | Description                                 | Required | Default  |
| -------------------------------- | ------------------------------------------- | -------- | -------- |
| `--auth <METHOD>`                | Authentication method: `gcloud` or `env`    | Yes      | -        |
| `--project-number <NUMBER>`      | Google Cloud project number                 | Yes\*    | From env |
| `--location <LOCATION>`          | API location: `global`, `us`, or `eu`       | No       | `global` |
| `--endpoint-location <LOCATION>` | Endpoint location (must match `--location`) | No       | `global` |
| `--json`                         | Output in JSON format                       | No       | false    |
| `--debug-http`                   | Print raw HTTP responses to stderr          | No       | false    |
| `-h, --help`                     | Print help information                      | No       | -        |
| `-V, --version`                  | Print version information                   | No       | -        |

\*Can be set via `NBLM_PROJECT_NUMBER` environment variable.

## Commands

| Command     | Description                 | Documentation                |
| ----------- | --------------------------- | ---------------------------- |
| `doctor`    | Run environment diagnostics | [doctor.md](doctor.md)       |
| `auth`      | Manage authentication       | [auth.md](auth.md)           |
| `notebooks` | Manage notebooks            | [notebooks.md](notebooks.md) |
| `sources`   | Manage notebook sources     | [sources.md](sources.md)     |
| `audio`     | Manage audio overviews      | [audio.md](audio.md)         |
| `share`     | Share notebooks with users  | [share.md](share.md)         |

## Authentication

Two authentication methods are supported:

### gcloud CLI (Recommended)

```bash
gcloud auth login
nblm --auth gcloud notebooks recent
# or let environment variables fill in project details
nblm --auth gcloud --project-number "$NBLM_PROJECT_NUMBER" notebooks recent
```

### Environment Variable

```bash
export NBLM_ACCESS_TOKEN=$(gcloud auth print-access-token)
nblm --auth env notebooks recent
```

See [Authentication Guide](../getting-started/authentication.md) for details.

## Environment Variables

Reduce command verbosity by setting environment variables:

```bash
export NBLM_PROJECT_NUMBER="123456789012"
export NBLM_LOCATION="global"
export NBLM_ENDPOINT_LOCATION="global"

# Now you can omit these flags
nblm notebooks recent
```

### Raw HTTP Logging

Use the new `--debug-http` flag (or set `NBLM_DEBUG_HTTP=1`) to print the raw JSON payload returned by the API. Logged bodies may contain sensitive data, so enable this only on trusted machines.

## Output Formats

### Human-Readable (Default)

```bash
nblm notebooks recent
```

Output:

```
Title: My Notebook
Notebook ID: abc123
Updated: 2025-10-25T10:30:00Z
```

### JSON Format

```bash
nblm --json notebooks recent
```

Output:

```json
{
  "notebooks": [
    {
      "title": "My Notebook",
      "notebookId": "abc123",
      "updateTime": "2025-10-25T10:30:00Z"
    }
  ]
}
```

The `--json` flag can be placed anywhere in the command:

```bash
# All equivalent
nblm --json notebooks recent
nblm notebooks recent --json
```

## Error Handling

### Exit Codes

| Code | Description          |
| ---- | -------------------- |
| 0    | Success              |
| 1    | General error        |
| 2    | Authentication error |

### Automatic Retries

The CLI automatically retries transient failures (HTTP 429, 500, 502, 503, 504) with exponential backoff.

### Error Messages

Errors are printed to stderr in a human-readable format:

```bash
Error: Failed to create notebook
Cause: API returned 403 Forbidden
```

In JSON mode, errors are also in JSON format:

```json
{
  "error": "Failed to create notebook",
  "cause": "API returned 403 Forbidden"
}
```

## Getting Help

### General Help

```bash
nblm --help
```

### Command-Specific Help

```bash
nblm notebooks --help
nblm sources add --help
```

## Examples

### Quick Start

```bash
# Set up
export NBLM_PROJECT_NUMBER="123456789012"
gcloud auth login

# Create notebook
nblm notebooks create --title "My Notebook"

# List notebooks
nblm notebooks recent

# Add source
nblm sources add \
  --notebook-id abc123 \
  --web-url "https://example.com"
```

### JSON Output with jq

```bash
# Get all notebook titles
nblm --json notebooks recent | jq '.notebooks[].title'

# Get first notebook ID
nblm --json notebooks recent | jq -r '.notebooks[0].notebookId'

# Count notebooks
nblm --json notebooks recent | jq '.notebooks | length'
```

## Next Steps

- [Notebooks Commands](notebooks.md) - Notebook management
- [Sources Commands](sources.md) - Source management
- [Audio Commands](audio.md) - Audio overview operations
- [Auth Commands](auth.md) - Authentication management

```

### File: docs\python\README.md
```md
# Python SDK Overview

Python bindings for the NotebookLM Enterprise API, powered by Rust via PyO3.

## Features

- **Type-safe API**: Full type hints for IDE autocomplete and static analysis
- **Fast**: Powered by Rust for high performance
- **Easy to use**: Pythonic API with sensible defaults
- **Comprehensive**: Supports notebooks, sources, and audio overviews

## Supported Operations

| Category           | Operations                                        | Status        |
| ------------------ | ------------------------------------------------- | ------------- |
| **Notebooks**      | Create, list, delete                              | Available     |
| **Sources**        | Add (web, text, video), upload files, get, delete | Available     |
| **Audio Overview** | Create, delete                                    | Available     |
| **Sharing**        | Share with users                                  | Not available |

## Installation

```bash
pip install nblm
```

Or with uv:

```bash
uv add nblm
```

**Requirements**: Python 3.14 or later

## Quick Example

```python
from nblm import NblmClient, GcloudTokenProvider, WebSource

# Initialize client
client = NblmClient(
    token_provider=GcloudTokenProvider(),
    project_number="123456789012"
)

# Create notebook
notebook = client.create_notebook(title="My Notebook")

# Add sources
client.add_sources(
    notebook_id=notebook.notebook_id,
    web_sources=[WebSource(url="https://example.com", name="Example")]
)

# Create audio overview
audio = client.create_audio_overview(notebook.notebook_id)
print(f"Audio status: {audio.status}")
```

## Documentation

### Getting Started

- [Quickstart](quickstart.md) - Get started in 5 minutes
- [Authentication](../getting-started/authentication.md) - Set up authentication
- [Configuration](../getting-started/configuration.md) - Configure project and location

### API Reference

- [API Reference](api-reference.md) - Complete API documentation
- [Notebooks API](notebooks.md) - Notebook operations
- [Sources API](sources.md) - Source operations
- [Audio API](audio.md) - Audio overview operations
- [Error Handling](error-handling.md) - Exception handling

## Authentication Methods

```python
from nblm import (
    GcloudTokenProvider,  # Use gcloud CLI
    EnvTokenProvider,     # Use environment variable
    NblmClient
)

# Method 1: gcloud CLI (recommended)
provider = GcloudTokenProvider()

# Method 2: Environment variable
import os
os.environ["NBLM_ACCESS_TOKEN"] = "your-token"
provider = EnvTokenProvider()

# Create client
client = NblmClient(
    token_provider=provider,
    project_number="123456789012"
)
```

## Debugging HTTP Responses

Set `NBLM_DEBUG_HTTP=1` before importing `nblm` to print the raw JSON bodies returned by the API. The payload can include notebook contents, so only enable this in trusted environments.

```bash
export NBLM_DEBUG_HTTP=1
python monitor_api.py --debug-http
```

## Type Support

The SDK includes full type hints:

```python
from nblm import (
    NblmClient,
    Notebook,
    NotebookSource,
    AudioOverviewResponse,
    ListRecentlyViewedResponse,
    BatchCreateSourcesResponse,
    WebSource,
    TextSource,
    VideoSource,
)

# All operations are fully typed
client: NblmClient
notebook: Notebook = client.create_notebook(title="Title")
sources: BatchCreateSourcesResponse = client.add_sources(...)
audio: AudioOverviewResponse = client.create_audio_overview(...)
```

## Quick Start

```python
import nblm

# 1. Authenticate (opens browser)
nblm.login()

# 2. Initialize client (uses gcloud credentials by default)
client = nblm.NblmClient()

# 3. List recent notebooks
response = client.list_notebooks()
for notebook in response.notebooks:
    print(f"{notebook.title} ({notebook.notebook_id})")
```

## Error Handling

```python
from nblm import NblmClient, NblmError

try:
    notebook = client.create_notebook(title="My Notebook")
except NblmError as e:
    print(f"Error: {e}")
```

See [Error Handling](error-handling.md) for details.

## Performance

The Python SDK is powered by Rust, providing:

- **Fast execution**: Native code performance
- **Memory efficiency**: Rust's memory management
- **Thread safety**: Safe concurrent operations

## Limitations

- **Sharing operations**: Not currently supported
- **Google Drive sources**: Supported via `GoogleDriveSource`; the SDK validates Drive scope (`drive`/`drive.file`) and document access before ingesting, returning an error if the requirements are not met
- **Audio configuration**: API only accepts empty request (as of 2025-10-25)

## Next Steps

- [Quickstart](quickstart.md) - Start building with the Python SDK
- [API Reference](api-reference.md) - Explore all available methods
- [Examples](notebooks.md) - See practical examples

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: local
    hooks:
      - id: make-all
        name: Run 'cargo make all'
        entry: cargo make all
        language: system
        always_run: true
        pass_filenames: false

```

### File: CONTRIBUTING.md
```md
# Contributing to nblm-rs

Thank you for your interest in contributing to nblm-rs!

## Prerequisites

### Rust Development

- Rust 1.90.0 or later
- Task runner: [cargo-make](https://github.com/sagiegurari/cargo-make)

```bash
# Option 1: cargo-make (traditional)
cargo install cargo-make

# Option 2: makers (faster alternative)
cargo install makers
```

We rely on `cargo-make` for every task (locally and in CI), so please install it before running any project commands.

### Python Development

- Python 3.14
- [uv](https://docs.astral.sh/uv/) - Python package manager

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## Development Workflow

### 1. Fork and Clone

```bash
git clone https://github.com/yourusername/nblm-rs.git
cd nblm-rs
```

### 2. Initial Setup

After cloning the repository, run all checks to set up the development environment:

```bash
# Using cargo-make
cargo make all

# Or using makers
makers all
```

This command will:

- Install and set up [prek](https://github.com/j178/prek) (pre-commit hook manager)
- Run Rust formatting, linting, and tests
- Run Python formatting, linting, type checking, and build

> [!IMPORTANT]
> Run `makers all` or `cargo make all` after cloning to ensure your environment is properly configured.

### 3. Make Your Changes

Create a new branch for your changes:

```bash
git checkout -b feature/your-feature-name
```

### 4. Run All Checks

Before submitting a pull request, ensure that all checks pass:

```bash
# Using cargo-make
cargo make all

# Or using makers
makers all
```

This command automatically:

- Installs and sets up prek (if not already installed)
- Runs Rust formatting (`cargo fmt --all`)
- Runs Rust linting (`cargo clippy --all-targets --all-features -- -D warnings`)
- Runs Rust tests (`cargo test --all`)
- Runs Python formatting (`ruff format`)
- Runs Python linting (`ruff check --fix`)
- Runs Python type checking (`mypy`)
- Builds Python package (`maturin develop`)

> [!IMPORTANT]
> All pull requests must pass `cargo make all` or `makers all` before being merged.

#### Pre-commit Hooks

This project uses [prek](https://github.com/j178/prek) for pre-commit hooks. When you run `makers all`, prek is automatically installed and configured. The pre-commit hooks will run `cargo make all` and `cargo make py-all` automatically before each commit.

> [!IMPORTANT] > **Pre-commit hooks must pass before pushing.** If a hook fails, fix the issues and try committing again. You can manually run hooks with `prek run --all-files` to test before committing.

### 5. Additional Commands

#### Rust Commands

```bash
# Format code only
cargo make fmt    # or: makers fmt

# Run linter only
cargo make lint   # or: makers lint

# Run tests only
cargo make test   # or: makers test

# Run CI checks (used in GitHub Actions)
cargo make ci     # or: makers ci

# Generate coverage report
cargo make coverage   # or: makers coverage
```

#### Python Commands

```bash
# Format Python code
cargo make py-fmt           # or: makers py-fmt

# Check formatting (CI)
cargo make py-fmt-check     # or: makers py-fmt-check

# Lint Python code
cargo make py-lint          # or: makers py-lint

# Lint and fix
cargo make py-lint-fix      # or: makers py-lint-fix

# Type checking
cargo make py-type          # or: makers py-type

# Run Python tests
cargo make py-test          # or: makers py-test

# Build Python package with maturin
cargo make py-build         # or: makers py-build
```

### Adding New Tests

#### Rust Tests

When adding new Rust features:

1. Add unit tests in the same file as your implementation
2. Add integration tests in `crates/nblm-cli/tests/`
3. Use the test helpers in `crates/nblm-cli/tests/_helpers/`
4. Follow existing test patterns for consistency

#### Python Tests

When adding new Python features:

1. Add tests in `python/tests/` directory
2. Use pytest conventions and fixtures
3. Test files should be named `test_*.py`
4. Run tests with `cargo make py-test` or `makers py-test`

## Code Style

### Rust

- Follow Rust standard formatting (`cargo fmt`)
- Keep clippy warnings at zero (`cargo clippy`)
- Use meaningful variable and function names
- Add documentation comments for public APIs
- Document any API issues or limitations you discover

### Python

- Follow PEP 8 style guide (enforced by `ruff format`)
- Type hints are required for all public functions (`mypy`)
- Keep `ruff` linting warnings at zero
- Use descriptive variable and function names
- Add docstrings for public APIs

## Documenting API Issues

If you discover issues with the NotebookLM API:

1. Add comments in the code explaining the issue
2. Add warnings in CLI help text if it affects user experience
3. Document in README.md's "Known API Issues" section
4. Include verification date in your documentation

Example:

```rust
/// Delete notebooks.
///
/// # Known Issues (as of 2025-10-19)
///
/// Despite the API being named "batchDelete", it only accepts one notebook
/// at a time. This function works around this limitation by calling the API
/// sequentially.
```

## Pull Request Process

1. Ensure all relevant checks pass:
   - Run `cargo make all` or `makers all` (this includes all Rust and Python checks)
2. **Pre-commit hooks must pass** - The pre-commit hooks (managed by prek) will automatically run `cargo make all` and `cargo make py-all` before each commit. Make sure all hooks pass before pushing.
3. Update documentation if you've added new features
4. Add or update tests for your changes
5. Write clear commit messages
6. Reference any related issues in your PR description

> [!NOTE]
> If you need to manually run pre-commit hooks before committing, use `prek run --all-files`. To skip hooks temporarily (not recommended), use `git commit --no-verify`, but ensure all checks pass before pushing.

## Project Structure

```
nblm-rs/
├── crates/
│   ├── nblm-core/          # Core API client and models
│   ├── nblm-cli/           # CLI interface
│   └── nblm-python/        # Python bindings (PyO3)
├── python/                 # Python package (tests, config, generated .so)
├── .github/workflows/      # CI/CD workflows
├── docs/                   # Documentation
└── Makefile.toml           # cargo-make tasks
```

## Getting Help

- Check existing issues for similar problems
- Read the [NotebookLM API documentation](https://cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs)
- Ask questions in issue discussions

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

```

### File: renovate.json
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ],
  "timezone": "Asia/Tokyo",
  "schedule": [
    "every weekend"
  ]
}

```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
## Summary

<!-- Briefly describe what this pull request changes and why. -->

## Testing

- [ ] Pre-commit hooks passed (automatically checked on commit)

<!-- List any additional manual checks or scripts you ran. -->

## Additional Context

<!-- Optional: screenshots, linked issues, follow-up tasks, etc. -->

```

### File: docs\index.md
```md
# nblm-rs Documentation

Complete documentation for the NotebookLM Enterprise API client (CLI & Python SDK).

!!! important "Unofficial Project"
    This project is not affiliated with, sponsored, or endorsed by Google. nblm-rs is an independent, unofficial tool. It is provided "as is" without any warranty.

## Getting Started

**New to nblm-rs?** Start here:

- [Installation](getting-started/installation.md) - Install CLI or Python SDK
- [Authentication](getting-started/authentication.md) - Set up authentication with gcloud
- [Configuration](getting-started/configuration.md) - Project numbers, locations, environment variables

## Features

!!! note "API Status"
    The NotebookLM API is currently in **alpha**. Some features may not work as documented due to API limitations. See [API Limitations](api/limitations.md) for details.

### Notebooks

| Feature               | CLI | Python | Status  | Notes                                |
| --------------------- | --- | ------ | ------- | ------------------------------------ |
| Create notebook       | ✅  | ✅     | Working |                                      |
| List recent notebooks | ✅  | ✅     | Working | Pagination not implemented by API    |
| Delete notebook(s)    | ✅  | ✅     | Working | Sequential deletion (API limitation) |

### Sources

| Feature             | CLI | Python | Status  | Notes                       |
| ------------------- | --- | ------ | ------- | --------------------------- |
| Add web URL         | ✅  | ✅     | Working |                             |
| Add text content    | ✅  | ✅     | Working |                             |
| Add video (YouTube) | ✅  | ✅     | Working | Uses `youtubeUrl` field     |
| Add Google Drive    | ✅  | ✅     | Working | Requires Drive-enabled auth |
| Upload file         | ✅  | ✅     | Working |                             |
| Delete source(s)    | ✅  | ✅     | Working |                             |
| Get source by ID    | ✅  | ✅     | Working |                             |

### Audio Overview

| Feature               | CLI | Python | Status  | Notes                       |
| --------------------- | --- | ------ | ------- | --------------------------- |
| Create audio overview | ✅  | ✅     | Working | Config fields not supported |
| Delete audio overview | ✅  | ✅     | Working |                             |

### Sharing

| Feature        | CLI | Python | Status   | Notes                     |
| -------------- | --- | ------ | -------- | ------------------------- |
| Share notebook | ✅  | ❌     | Untested | Requires additional users |

## CLI Reference

Complete command-line interface documentation:

- [CLI Overview](cli/README.md) - Command structure and common options
- [Notebooks Commands](cli/notebooks.md) - Create, list, and delete notebooks
- [Sources Commands](cli/sources.md) - Add, upload, and manage sources
- [Audio Commands](cli/audio.md) - Create and delete audio overviews
- [Doctor Command](cli/doctor.md) - Run environment diagnostics

## Python SDK Reference

Python bindings documentation:

- [Python SDK Overview](python/README.md) - Installation and basic usage
- [Quickstart](python/quickstart.md) - Get started in 5 minutes
- [API Reference](python/api-reference.md) - All classes and methods
- [Source Management](python/sources.md) - Source operations in detail
- [Notebooks API](python/notebooks.md) - Notebook operations in detail
- [Audio API](python/audio.md) - Audio overview operations
- [Error Handling](python/error-handling.md) - Exception handling patterns

## Rust SDK

Rust library documentation:

- [Getting Started](rust/getting-started.md) - Rust SDK setup and usage

!!! note "Work in Progress"
    The Rust SDK is currently being refactored. The Getting Started guide will be updated once the new core APIs are finalized.

## Guides

Additional guides and tutorials:

- [Troubleshooting](guides/troubleshooting.md) - Common issues and solutions

## API Information

- [API Limitations](api/limitations.md) - Known limitations and workarounds
- [NotebookLM API Documentation](https://cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/overview) - Official API docs

## Contributing

- [Contributing Guide](https://github.com/K-dash/nblm-rs/blob/main/CONTRIBUTING.md) - Development setup and guidelines

---

!!! note
    The `investigation/` directory contains internal research notes and experiments with the NotebookLM API.

```

### File: python\manual_test.py
```py
#!/usr/bin/env python3
"""
Manual test script for nblm Python bindings

This script demonstrates notebook creation, retrieval, and deletion.
Run with: python manual_test.py
"""

import os
import sys
from pathlib import Path

from nblm import (
    AudioOverviewRequest,
    GcloudTokenProvider,
    NblmClient,
    NblmError,
    TextSource,
    VideoSource,
    WebSource,
)


def main() -> None:
    # Get project number from environment
    project_number = os.getenv("NBLM_PROJECT_NUMBER")
    if not project_number:
        print("Error: NBLM_PROJECT_NUMBER environment variable not set")
        sys.exit(1)

    location = os.getenv("NBLM_LOCATION", "global")
    endpoint_location = os.getenv("NBLM_ENDPOINT_LOCATION", "global")

    print(f"Project Number: {project_number}")
    print(f"Location: {location}")
    print(f"Endpoint Location: {endpoint_location}\n")

    # Initialize client with gcloud auth
    try:
        token_provider = GcloudTokenProvider()
        client = NblmClient(
            project_number=project_number,
            location=location,
            endpoint_location=endpoint_location,
            token_provider=token_provider,
        )
        print("✓ Client initialized\n")
    except NblmError as e:
        print(f"✗ Failed to initialize client: {e}")
        sys.exit(1)

    # Test 1: Create a notebook
    print("Test 1: Creating a notebook...")
    try:
        notebook = client.create_notebook(title="Python Test Notebook")
        print(f"✓ Notebook created: {notebook.name}")
        print(f"  Title: {notebook.title}\n")
    except NblmError as e:
        print(f"✗ Failed to create notebook: {e}\n")
        sys.exit(1)

    # Test 2: List recently viewed notebooks
    print("Test 2: Listing recently viewed notebooks...")
    try:
        response = client.list_recently_viewed()
        print(f"✓ Found {len(response.notebooks)} notebook(s)")
        for nb in response.notebooks[:3]:  # Show first 3
            print(f"  - {nb.title} ({nb.name})")
        print()
    except NblmError as e:
        print(f"✗ Failed to list notebooks: {e}\n")

    # Test 3: Add sources to the notebook
    print("Test 3: Adding sources to the notebook...")
    source_ids = []
    try:
        response = client.add_sources(
            notebook_id=notebook.notebook_id,
            web_sources=[
                WebSource(url="https://www.python.org/", name="Python Official Site"),
                WebSource(url="https://docs.python.org/"),
            ],
            text_sources=[
                TextSource(content="This is a test text content.", name="Test Note"),
            ],
            video_sources=[
                VideoSource(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
            ],
        )
        print(f"✓ Added sources (error_count: {response.error_count})")
        for source in response.sources:
            print(f"  - {source.name}")
            # Extract source ID from the source name (format: .../sources/SOURCE_ID)
            if source.name and "/sources/" in source.name:
                source_id = source.name.split("/sources/")[-1]
                source_ids.append(source_id)
        print()
    except NblmError as e:
        print(f"✗ Failed to add sources: {e}\n")

    # Test 4: Get source by ID
    print("Test 4: Getting source details...")
    if source_ids:
        # Get the first source that was added
        test_source_id = source_ids[0]
        try:
            source = client.get_source(
                notebook_id=notebook.notebook_id,
                source_id=test_source_id
            )
            print(f"✓ Retrieved source: {source.name}")
            print(f"  Title: {source.title}")
            if source.source_id and source.source_id.id:
                print(f"  Source ID: {source.source_id.id}")
            if source.metadata:
                if source.metadata.source_added_timestamp:
                    print(f"  Added: {source.metadata.source_added_timestamp}")
                if source.metadata.word_count:
                    print(f"  Word Count: {source.metadata.word_count}")
                if source.metadata.youtube_metadata:
                    youtube_meta = source.metadata.youtube_metadata
                    if youtube_meta.channel_name:
                        print(f"  YouTube Channel: {youtube_meta.channel_name}")
                    if youtube_meta.video_id:
                        print(f"  YouTube Video ID: {youtube_meta.video_id}")
            if source.settings and source.settings.status:
                print(f"  Status: {source.settings.status}")
            print()
        except NblmError as e:
            print(f"✗ Failed to get source: {e}\n")
    else:
        print("  No sources available to get details\n")

    # Test 5: Create audio overview
    print("Test 5: Creating audio overview...")
    try:
        # Create audio overview with empty request (current API requirement)
        audio_response = client.create_audio_overview(
            notebook_id=notebook.notebook_id,
            request=AudioOverviewRequest()
        )
        print(f"✓ Audio overview created:")
        
        # Debug information
        print(f"  [DEBUG] audio_overview_id: {audio_response.audio_overview_id}")
        print(f"  [DEBUG] name: {audio_response.name}")
        print(f"  [DEBUG] status: {audio_response.status}")
        print(f"  [DEBUG] generation_options: {audio_response.generation_options}")
        print(f"  [DEBUG] extra keys: {list(audio_response.extra.keys()) if hasattr(audio_response.extra, 'keys') else 'N/A'}")
        print(f"  [DEBUG] full repr: {repr(audio_response)}")
        
        # Original display
        if audio_response.audio_overview_id:
            print(f"  Audio Overview ID: {audio_response.audio_overview_id}")
        if audio_response.name:
            print(f"  Name: {audio_response.name}")
        if audio_response.status:
            print(f"  Status: {audio_response.status}")
        print()
        
        # Test deleting the audio overview
        print("Test 5b: Deleting audio overview...")
        try:
            client.delete_audio_overview(notebook_id=notebook.notebook_id)
            print("✓ Audio overview deleted successfully\n")
        except NblmError as e:
            print(f"✗ Failed to delete audio overview: {e}\n")
    except NblmError as e:
        print(f"✗ Failed to create audio overview: {e}\n")

    # Test 6: Upload a local file as a source (optional)
    upload_path = os.getenv("NBLM_UPLOAD_FILE")
    if upload_path:
        print("Test 5: Uploading file to the notebook...")
        path_obj = Path(upload_path)
        if not path_obj.exists() or not path_obj.is_file():
            print(f"✗ Upload path is not a file: {path_obj}")
        else:
            content_type = os.getenv("NBLM_UPLOAD_CONTENT_TYPE")
            display_name = os.getenv("NBLM_UPLOAD_DISPLAY_NAME")
            try:
                response = client.upload_source_file(
                    notebook_id=notebook.notebook_id,
                    path=path_obj,
                    content_type=content_type,
                    display_name=display_name,
                )

                source_id_obj = response.source_id
                if source_id_obj and source_id_obj.id:
                    print(f"✓ Uploaded source ID: {source_id_obj.id}")
                else:
                    print("✓ Upload accepted (source ID unavailable)")

                extra = getattr(response, "extra", {})
                if isinstance(extra, dict):
                    print(f"  Extra metadata keys: {len(extra)}\n")
                else:
                    print("  Extra metadata: <unavailable>\n")
            except NblmError as e:
                print(f"✗ Failed to upload file: {e}\n")
                print(f"Error type: {type(e).__name__}")
                print(f"Error message: {e}")
                print(f"Error details: {e.args}")
                import traceback
                traceback.print_exc()
    else:
        print(
            "Test 6 skipped: set NBLM_UPLOAD_FILE to exercise upload_source_file manually.\n"
        )

    # # Test 7: Delete the created notebook
    # print("Test 7: Deleting the test notebook...")
    # try:
    #     response = client.delete_notebooks([notebook.name])
    #     print(f"✓ Deleted {len(response.deleted_notebooks)} notebook(s)")
    #     for name in response.deleted_notebooks:
    #         print(f"  - {name}")
    #     if response.failed_notebooks:
    #         print(f"  Failed: {response.failed_notebooks}")
    #     print()
    # except NblmError as e:
    #     print(f"✗ Failed to delete notebook: {e}\n")

    print("All tests completed!")


if __name__ == "__main__":
    main()

```

### File: python\manual_test_env.py
```py
#!/usr/bin/env python3
"""
Manual test script for nblm Python bindings using EnvTokenProvider

This script demonstrates authentication using an environment variable token.
Run with: python manual_test_env.py

Prerequisites:
    export NBLM_ACCESS_TOKEN=$(gcloud auth print-access-token)
    export NBLM_PROJECT_NUMBER="your_project_number"
"""

import os
import sys
from nblm import NblmClient, EnvTokenProvider, NblmError


def main() -> None:
    # Get configuration from environment
    access_token = os.getenv("NBLM_ACCESS_TOKEN")
    if not access_token:
        print("Error: NBLM_ACCESS_TOKEN environment variable not set")
        print("Run: export NBLM_ACCESS_TOKEN=$(gcloud auth print-access-token)")
        sys.exit(1)

    project_number = os.getenv("NBLM_PROJECT_NUMBER")
    if not project_number:
        print("Error: NBLM_PROJECT_NUMBER environment variable not set")
        sys.exit(1)

    location = os.getenv("NBLM_LOCATION", "global")
    endpoint_location = os.getenv("NBLM_ENDPOINT_LOCATION", "global")

    print("=== EnvTokenProvider Test ===")
    print(f"Project Number: {project_number}")
    print(f"Location: {location}")
    print(f"Endpoint Location: {endpoint_location}")
    print(f"Token: {access_token[:20]}...\n")

    # Initialize client with environment token provider
    try:
        token_provider = EnvTokenProvider("NBLM_ACCESS_TOKEN")
        client = NblmClient(
            project_number=project_number,
            location=location,
            endpoint_location=endpoint_location,
            token_provider=token_provider,
        )
        print("✓ Client initialized with EnvTokenProvider\n")
    except NblmError as e:
        print(f"✗ Failed to initialize client: {e}")
        sys.exit(1)

    # Test: Create a notebook
    print("Test: Creating a notebook...")
    try:
        notebook = client.create_notebook(title="EnvToken Test Notebook")
        print(f"✓ Notebook created: {notebook.name}")
        print(f"  Title: {notebook.title}\n")
    except NblmError as e:
        print(f"✗ Failed to create notebook: {e}\n")
        sys.exit(1)

    # Test: List recently viewed notebooks
    print("Test: Listing recently viewed notebooks...")
    try:
        response = client.list_recently_viewed()
        print(f"✓ Found {len(response.notebooks)} notebook(s)")
        for nb in response.notebooks[:3]:  # Show first 3
            print(f"  - {nb.title} ({nb.name})")
        print()
    except NblmError as e:
        print(f"✗ Failed to list notebooks: {e}\n")

    # Test: Delete the created notebook
    print("Test: Deleting the test notebook...")
    try:
        response = client.delete_notebooks([notebook.name])
        print(f"✓ Deleted {len(response.deleted_notebooks)} notebook(s)")
        for name in response.deleted_notebooks:
            print(f"  - {name}")
        if response.failed_notebooks:
            print(f"  Failed: {response.failed_notebooks}")
        print()
    except NblmError as e:
        print(f"✗ Failed to delete notebook: {e}\n")

    print("All tests completed with EnvTokenProvider!")


if __name__ == "__main__":
    main()

```

### File: scripts\bump-version.sh
```sh
#!/usr/bin/env bash
set -euo pipefail

# Usage: ./scripts/bump-version.sh

# Fetch latest tags from remote
echo "Fetching latest tags from remote..."
git fetch --tags --quiet

# Get the latest tag version
LATEST_TAG=$(git tag -l 'v*' | sort -V | tail -n 1)
if [ -z "$LATEST_TAG" ]; then
  echo "No existing tags found."
  LATEST_VERSION="none"
else
  LATEST_VERSION="${LATEST_TAG#v}"
  echo "Current latest tag: ${LATEST_TAG} (${LATEST_VERSION})"
fi

# Prompt for new version
echo ""
read -p "Enter new version: " NEW_VERSION

if [ -z "$NEW_VERSION" ]; then
  echo "Error: Version cannot be empty"
  exit 1
fi

echo "Bumping version to ${NEW_VERSION}..."

# Rust crates
echo "Updating Rust crates..."
sed -i.bak "s/^version = \".*\"/version = \"${NEW_VERSION}\"/" Cargo.toml
sed -i.bak "s/^version = \".*\"/version = \"${NEW_VERSION}\"/" crates/nblm-core/Cargo.toml
sed -i.bak "s/^version = \".*\"/version = \"${NEW_VERSION}\"/" crates/nblm-cli/Cargo.toml
sed -i.bak "s/^version = \".*\"/version = \"${NEW_VERSION}\"/" crates/nblm-python/Cargo.toml

# Update nblm-core dependency version in nblm-cli
echo "Updating nblm-core dependency in nblm-cli..."
sed -i.bak "s/^nblm-core = { version = \"[^\"]*\"/nblm-core = { version = \"${NEW_VERSION}\"/" crates/nblm-cli/Cargo.toml

# Python package
echo "Updating Python package..."
sed -i.bak "s/^version = \".*\"/version = \"${NEW_VERSION}\"/" python/pyproject.toml
(cd python && uv sync)

# Clean up backup files
find . -name "*.bak" -delete

# Update Cargo.lock
echo "Updating Cargo.lock..."
cargo check --quiet

echo "✅ Version bumped to ${NEW_VERSION}"
echo ""
echo "Next steps:"
echo "  1. Review changes: git diff"
echo "  2. Commit: git add -A && git commit -m 'chore: bump version to ${NEW_VERSION}'"
echo "  3. Tag: git tag v${NEW_VERSION}"
echo "  4. Push: git push origin main && git push origin v${NEW_VERSION}"


```

### File: scripts\update_homebrew.sh
```sh
#!/usr/bin/env bash
# Updates the Homebrew tap Formula/nblm.rb and opens a PR via gh.
#
# Example usage:
#   ./scripts/update_homebrew.sh \
#     --version 0.3.0 \
#     --tap-dir ../homebrew-nblm

set -euo pipefail

usage() {
  cat <<'USAGE'
Usage: ./scripts/update_homebrew.sh \
  --version <version> \
  [--tap-dir <path>] \
  [--remote <remote>] \
  [--base-branch <branch>] \
  [--pr-branch <branch>] \
  [--no-pr]

The script fetches release assets from GitHub, calculates SHA256,
updates Formula/nblm.rb, commits, pushes, and opens a PR via gh.
USAGE
}

TAP_DIR="../homebrew-nblm"
REMOTE="origin"
BASE_BRANCH="main"
PR_BRANCH=""
CREATE_PR=1

VERSION=""

while [[ $# -gt 0 ]]; do
  case "$1" in
    --version)
      VERSION="$2"
      shift 2
      ;;
    --tap-dir)
      TAP_DIR="$2"
      shift 2
      ;;
    --remote)
      REMOTE="$2"
      shift 2
      ;;
    --base-branch)
      BASE_BRANCH="$2"
      shift 2
      ;;
    --pr-branch)
      PR_BRANCH="$2"
      shift 2
      ;;
    --no-pr)
      CREATE_PR=0
      shift 1
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage >&2
      exit 1
      ;;
  esac
done

if [[ -z "$VERSION" ]]; then
  echo "Error: --version is required" >&2
  usage >&2
  exit 1
fi

if [[ -z "$PR_BRANCH" ]]; then
  PR_BRANCH="update-nblm-v${VERSION}"
fi

for cmd in git gh python3; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Error: required command '$cmd' not found" >&2
    exit 1
  fi
done

if ! gh auth status >/dev/null 2>&1; then
  echo "Error: gh is not authenticated. Run 'gh auth login' first." >&2
  exit 1
fi

if [[ ! -d "$TAP_DIR/.git" ]]; then
  echo "Error: tap directory '$TAP_DIR' is not a git repository" >&2
  exit 1
fi

echo "Fetching release info for tag v${VERSION}..."
RELEASE_JSON=$(gh api "repos/K-dash/nblm-rs/releases/tags/v${VERSION}")

MAC_ARM_URL=$(echo "$RELEASE_JSON" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for asset in data.get('assets', []):
    if 'nblm-macos-aarch64.tar.gz' in asset['name']:
        print(asset['browser_download_url'])
        break
")

MAC_INTEL_URL=$(echo "$RELEASE_JSON" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for asset in data.get('assets', []):
    if 'nblm-macos-x86_64.tar.gz' in asset['name']:
        print(asset['browser_download_url'])
        break
")

if [[ -z "$MAC_ARM_URL" ]]; then
  echo "Error: could not find macOS ARM64 asset in release v${VERSION}" >&2
  exit 1
fi

if [[ -z "$MAC_INTEL_URL" ]]; then
  echo "Error: could not find macOS Intel asset in release v${VERSION}" >&2
  exit 1
fi

echo "Found ARM64 binary: $MAC_ARM_URL"
echo "Found Intel binary: $MAC_INTEL_URL"

TEMP_DIR=$(mktemp -d)
trap "rm -rf $TEMP_DIR" EXIT

echo "Downloading ARM64 binary..."
curl -sSL "$MAC_ARM_URL" -o "$TEMP_DIR/arm64.tar.gz"
MAC_ARM_SHA=$(shasum -a 256 "$TEMP_DIR/arm64.tar.gz" | awk '{print $1}')
echo "ARM64 SHA256: $MAC_ARM_SHA"

echo "Downloading Intel binary..."
curl -sSL "$MAC_INTEL_URL" -o "$TEMP_DIR/intel.tar.gz"
MAC_INTEL_SHA=$(shasum -a 256 "$TEMP_DIR/intel.tar.gz" | awk '{print $1}')
echo "Intel SHA256: $MAC_INTEL_SHA"

pushd "$TAP_DIR" >/dev/null

if [[ -n $(git status --porcelain) ]]; then
  echo "Error: tap repository has uncommitted changes. Commit or stash them first." >&2
  popd >/dev/null
  exit 1
fi

git fetch "$REMOTE" "$BASE_BRANCH" --quiet
git checkout "$BASE_BRANCH" >/dev/null
git pull --ff-only "$REMOTE" "$BASE_BRANCH"

if git rev-parse --verify --quiet "$PR_BRANCH" >/dev/null; then
  echo "Error: branch '$PR_BRANCH' already exists locally. Pick a different --pr-branch or delete it." >&2
  popd >/dev/null
  exit 1
fi

if git ls-remote --exit-code --heads "$REMOTE" "$PR_BRANCH" >/dev/null 2>&1; then
  echo "Error: branch '$PR_BRANCH' already exists on remote '$REMOTE'. Choose a different --pr-branch." >&2
  popd >/dev/null
  exit 1
fi

git checkout -b "$PR_BRANCH" "$REMOTE/$BASE_BRANCH" >/dev/null

FORMULA_PATH="Formula/nblm.rb"
if [[ ! -f "$FORMULA_PATH" ]]; then
  echo "Error: formula file '$FORMULA_PATH' not found" >&2
  popd >/dev/null
  exit 1
fi

export FORMULA_PATH VERSION MAC_ARM_URL MAC_ARM_SHA MAC_INTEL_URL MAC_INTEL_SHA

python3 <<'PYTHON'
import os
import pathlib
import re

formula_path = pathlib.Path(os.environ["FORMULA_PATH"])
text = formula_path.read_text()

version = os.environ["VERSION"]
mac_arm_url = os.environ["MAC_ARM_URL"]
mac_arm_sha = os.environ["MAC_ARM_SHA"]
mac_intel_url = os.environ["MAC_INTEL_URL"]
mac_intel_sha = os.environ["MAC_INTEL_SHA"]

lines = text.splitlines()

def with_indent(original_line: str, content: str) -> str:
    indent = re.match(r"^\s*", original_line).group(0)
    return f"{indent}{content}"

found_version = False
found_arm = False
found_intel = False

for idx, line in enumerate(lines):
    stripped = line.strip()
    if stripped.startswith("version ") and not found_version:
        lines[idx] = with_indent(line, f'version "{version}"')
        found_version = True
    elif "url " in stripped and "nblm-macos-aarch64" in stripped and not found_arm:
        lines[idx] = with_indent(line, f'url "{mac_arm_url}"')
        # find sha line that follows the url
        sha_idx = idx + 1
        while sha_idx < len(lines) and lines[sha_idx].strip() == "":
            sha_idx += 1
        if sha_idx >= len(lines) or not lines[sha_idx].strip().startswith("sha256"):
            raise SystemExit("Failed to locate sha256 line for macOS arm64 block")
        lines[sha_idx] = with_indent(lines[sha_idx], f'sha256 "{mac_arm_sha}"')
        found_arm = True
    elif "url " in stripped and "nblm-macos-x86_64" in stripped and not found_intel:
        lines[idx] = with_indent(line, f'url "{mac_intel_url}"')
        sha_idx = idx + 1
        while sha_idx < len(lines) and lines[sha_idx].strip() == "":
            sha_idx += 1
        if sha_idx >= len(lines) or not lines[sha_idx].strip().startswith("sha256"):
            raise SystemExit("Failed to locate sha256 line for macOS intel block")
        lines[sha_idx] = with_indent(lines[sha_idx], f'sha256 "{mac_intel_sha}"')
        found_intel = True


if not found_version:
    raise SystemExit("Failed to update version line")
if not found_arm:
    raise SystemExit("Failed to update macOS arm block")
if not found_intel:
    raise SystemExit("Failed to update macOS intel block")

updated_text = "\n".join(lines)
if text.endswith("\n"):
    updated_text += "\n"

formula_path.write_text(updated_text)
PYTHON

git add "$FORMULA_PATH"

if git diff --cached --quiet; then
  echo "Error: no changes detected after editing formula" >&2
  popd >/dev/null
  exit 1
fi

COMMIT_MSG="chore: update nblm formula to v${VERSION}"
git commit -m "$COMMIT_MSG"

git push -u "$REMOTE" "$PR_BRANCH"

if [[ "$CREATE_PR" -eq 1 ]]; then
  gh pr create \
    --base "$BASE_BRANCH" \
    --head "$PR_BRANCH" \
    --title "Update nblm formula to v${VERSION}" \
    --body "Update the nblm Homebrew formula to version v${VERSION}."
else
  echo "Skipping PR creation (--no-pr provided)."
fi

popd >/dev/null

echo "✅ Formula update complete"

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
