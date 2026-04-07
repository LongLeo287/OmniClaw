---
id: gitingest
type: knowledge
owner: OA_Triage
---
# gitingest
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Gitingest

[![Screenshot of Gitingest front page](https://raw.githubusercontent.com/coderamp-labs/gitingest/refs/heads/main/docs/frontpage.png)](https://gitingest.com)

<!-- Badges -->
<!-- markdownlint-disable MD033 -->
<p align="center">
  <!-- row 1 — install & compat -->
  <a href="https://pypi.org/project/gitingest"><img src="https://img.shields.io/pypi/v/gitingest.svg" alt="PyPI"></a>
  <a href="https://pypi.org/project/gitingest"><img src="https://img.shields.io/pypi/pyversions/gitingest.svg" alt="Python Versions"></a>
  <br>
  <!-- row 2 — quality & community -->
  <a href="https://github.com/coderamp-labs/gitingest/actions/workflows/ci.yml?query=branch%3Amain"><img src="https://github.com/coderamp-labs/gitingest/actions/workflows/ci.yml/badge.svg?branch=main" alt="CI"></a>

  <a href="https://github.com/astral-sh/ruff"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff"></a>
  <a href="https://scorecard.dev/viewer/?uri=github.com/coderamp-labs/gitingest"><img src="https://api.scorecard.dev/projects/github.com/coderamp-labs/gitingest/badge" alt="OpenSSF Scorecard"></a>
  <br>
  <a href="https://github.com/coderamp-labs/gitingest/blob/main/LICENSE"><img src="https://img.shields.io/github/license/coderamp-labs/gitingest.svg" alt="License"></a>
  <a href="https://pepy.tech/project/gitingest"><img src="https://pepy.tech/badge/gitingest" alt="Downloads"></a>
  <a href="https://github.com/coderamp-labs/gitingest"><img src="https://img.shields.io/github/stars/coderamp-labs/gitingest" alt="GitHub Stars"></a>
  <a href="https://discord.com/invite/zerRaGK9EC"><img src="https://img.shields.io/badge/Discord-Join_chat-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <br>
  <a href="https://trendshift.io/repositories/13519"><img src="https://trendshift.io/api/badge/repositories/13519" alt="Trendshift" height="50"></a>
</p>
<!-- markdownlint-enable MD033 -->

Turn any Git repository into a prompt-friendly text ingest for LLMs.

You can also replace `hub` with `ingest` in any GitHub URL to access the corresponding digest.

<!-- Extensions -->
[gitingest.com](https://gitingest.com) · [Chrome Extension](https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood) · [Firefox Add-on](https://addons.mozilla.org/firefox/addon/gitingest)

<!-- Languages -->
[Deutsch](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=de) |
[Español](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=es) |
[Français](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=fr) |
[日本語](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ja) |
[한국어](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ko) |
[Português](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=pt) |
[Русский](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=ru) |
[中文](https://www.readme-i18n.com/coderamp-labs/gitingest?lang=zh)

## 🚀 Features

- **Easy code context**: Get a text digest from a Git repository URL or a directory
- **Smart Formatting**: Optimized output format for LLM prompts
- **Statistics about**:
  - File and directory structure
  - Size of the extract
  - Token count
- **CLI tool**: Run it as a shell command
- **Python package**: Import it in your code

## 📚 Requirements

- Python 3.8+
- For private repositories: A GitHub Personal Access Token (PAT). [Generate your token **here**!](https://github.com/settings/tokens/new?description=gitingest&scopes=repo)

### 📦 Installation

Gitingest is available on [PyPI](https://pypi.org/project/gitingest/).
You can install it using `pip`:

```bash
pip install gitingest
```

or

```bash
pip install gitingest[server]
```

to include server dependencies for self-hosting.

However, it might be a good idea to use `pipx` to install it.
You can install `pipx` using your preferred package manager.

```bash
brew install pipx
apt install pipx
scoop install pipx
...
```

If you are using pipx for the first time, run:

```bash
pipx ensurepath
```

```bash
# install gitingest
pipx install gitingest
```

## 🧩 Browser Extension Usage

<!-- markdownlint-disable MD033 -->
<a href="https://chromewebstore.google.com/detail/adfjahbijlkjfoicpjkhjicpjpjfaood" target="_blank" title="Get Gitingest Extension from Chrome Web Store"><img height="48" src="https://github.com/user-attachments/assets/20a6e44b-fd46-4e6c-8ea6-aad436035753" alt="Available in the Chrome Web Store" /></a>
<a href="https://addons.mozilla.org/firefox/addon/gitingest" target="_blank" title="Get Gitingest Extension from Firefox Add-ons"><img height="48" src="https://github.com/user-attachments/assets/c0e99e6b-97cf-4af2-9737-099db7d3538b" alt="Get The Add-on for Firefox" /></a>
<a href="https://microsoftedge.microsoft.com/addons/detail/nfobhllgcekbmpifkjlopfdfdmljmipf" target="_blank" title="Get Gitingest Extension from Microsoft Edge Add-ons"><img height="48" src="https://github.com/user-attachments/assets/204157eb-4cae-4c0e-b2cb-db514419fd9e" alt="Get from the Edge Add-ons" /></a>
<!-- markdownlint-enable MD033 -->

The extension is open source at [lcandy2/gitingest-extension](https://github.com/lcandy2/gitingest-extension).

Issues and feature requests are welcome to the repo.

## 💡 Command line usage

The `gitingest` command line tool allows you to analyze codebases and create a text dump of their contents.

```bash
# Basic usage (writes to digest.txt by default)
gitingest /path/to/directory

# From URL
gitingest https://github.com/coderamp-labs/gitingest

# or from specific subdirectory
gitingest https://github.com/coderamp-labs/gitingest/tree/main/src/gitingest/utils
```

For private repositories, use the `--token/-t` option.

```bash
# Get your token from https://github.com/settings/personal-access-tokens
gitingest https://github.com/username/private-repo --token github_pat_...

# Or set it as an environment variable
export GITHUB_TOKEN=github_pat_...
gitingest https://github.com/username/private-repo

# Include repository submodules
gitingest https://github.com/username/repo-with-submodules --include-submodules
```

By default, files listed in `.gitignore` are skipped. Use `--include-gitignored` if you
need those files in the digest.

By default, the digest is written to a text file (`digest.txt`) in your current working directory. You can customize the output in two ways:

- Use `--output/-o <filename>` to write to a specific file.
- Use `--output/-o -` to output directly to `STDOUT` (useful for piping to other tools).

See more options and usage details with:

```bash
gitingest --help
```

## 🐍 Python package usage

```python
# Synchronous usage
from gitingest import ingest

summary, tree, content = ingest("path/to/directory")

# or from URL
summary, tree, content = ingest("https://github.com/coderamp-labs/gitingest")

# or from a specific subdirectory
summary, tree, content = ingest("https://github.com/coderamp-labs/gitingest/tree/main/src/gitingest/utils")
```

For private repositories, you can pass a token:

```python
# Using token parameter
summary, tree, content = ingest("https://github.com/username/private-repo", token="github_pat_...")

# Or set it as an environment variable
import os
os.environ["GITHUB_TOKEN"] = "github_pat_..."
summary, tree, content = ingest("https://github.com/username/private-repo")

# Include repository submodules
summary, tree, content = ingest("https://github.com/username/repo-with-submodules", include_submodules=True)
```

By default, this won't write a file but can be enabled with the `output` argument.

```python
# Asynchronous usage
from gitingest import ingest_async
import asyncio

result = asyncio.run(ingest_async("path/to/directory"))
```

### Jupyter notebook usage

```python
from gitingest import ingest_async

# Use await directly in Jupyter
summary, tree, content = await ingest_async("path/to/directory")

```

This is because Jupyter notebooks are asynchronous by default.

## 🐳 Self-host

### Using Docker

1. Build the image:

   ``` bash
   docker build -t gitingest .
   ```

2. Run the container:

   ``` bash
   docker run -d --name gitingest -p 8000:8000 gitingest
   ```

The application will be available at `http://localhost:8000`.

If you are hosting it on a domain, you can specify the allowed hostnames via env variable `ALLOWED_HOSTS`.

   ```bash
   # Default: "gitingest.com, *.gitingest.com, localhost, 127.0.0.1".
   ALLOWED_HOSTS="example.com, localhost, 127.0.0.1"
   ```

### Environment Variables

The application can be configured using the following environment variables:

- **ALLOWED_HOSTS**: Comma-separated list of allowed hostnames (default: "gitingest.com, *.gitingest.com, localhost, 127.0.0.1")
- **GITINGEST_METRICS_ENABLED**: Enable Prometheus metrics server (set to any value to enable)
- **GITINGEST_METRICS_HOST**: Host for the metrics server (default: "127.0.0.1")
- **GITINGEST_METRICS_PORT**: Port for the metrics server (default: "9090")
- **GITINGEST_SENTRY_ENABLED**: Enable Sentry error tracking (set to any value to enable)
- **GITINGEST_SENTRY_DSN**: Sentry DSN (required if Sentry is enabled)
- **GITINGEST_SENTRY_TRACES_SAMPLE_RATE**: Sampling rate for performance data (default: "1.0", range: 0.0-1.0)
- **GITINGEST_SENTRY_PROFILE_SESSION_SAMPLE_RATE**: Sampling rate for profile sessions (default: "1.0", range: 0.0-1.0)
- **GITINGEST_SENTRY_PROFILE_LIFECYCLE**: Profile lifecycle mode (default: "trace")
- **GITINGEST_SENTRY_SEND_DEFAULT_PII**: Send default personally identifiable information (default: "true")
- **S3_ALIAS_HOST**: Public URL/CDN for accessing S3 resources (default: "127.0.0.1:9000/gitingest-bucket")
- **S3_DIRECTORY_PREFIX**: Optional prefix for S3 file paths (if set, prefixes all S3 paths with this value)

### Using Docker Compose

The project includes a `compose.yml` file that allows you to easily run the application in both development and production environments.

#### Compose File Structure

The `compose.yml` file uses YAML anchoring with `&app-base` and `<<: *app-base` to define common configuration that is shared between services:

```yaml
# Common base configuration for all services
x-app-base: &app-base
  build:
    context: .
    dockerfile: Dockerfile
  ports:
    - "${APP_WEB_BIND:-8000}:8000"  # Main application port
    - "${GITINGEST_METRICS_HOST:-127.0.0.1}:${GITINGEST_METRICS_PORT:-9090}:9090"  # Metrics port
  # ... other common configurations
```

#### Services

The file defines three services:

1. **app**: Production service configuration
   - Uses the `prod` profile
   - Sets the Sentry environment to "production"
   - Configured for stable operation with `restart: unless-stopped`

2. **app-dev**: Development service configuration
   - Uses the `dev` profile
   - Enables debug mode
   - Mounts the source code for live development
   - Uses hot reloading for faster development

3. **minio**: S3-compatible object storage for development
   - Uses the `dev` profile (only available in development mode)
   - Provides S3-compatible storage for local development
   - Accessible via:
     - API: Port 9000 ([localhost:9000](http://localhost:9000))
     - Web Console: Port 9001 ([localhost:9001](http://localhost:9001))
   - Default admin credentials:
     - Username: `minioadmin`
     - Password: `minioadmin`
   - Configurable via environment variables:
     - `MINIO_ROOT_USER`: Custom admin username (default: minioadmin)
     - `MINIO_ROOT_PASSWORD`: Custom admin password (default: minioadmin)
   - Includes persistent storage via Docker volume
   - Auto-creates a bucket and application-specific credentials:
     - Bucket name: `gitingest-bucket` (configurable via `S3_BUCKET_NAME`)
     - Access key: `gitingest` (configurable via `S3_ACCESS_KEY`)
     - Secret key: `gitingest123` (configurable via `S3_SECRET_KEY`)
   - These credentials are automatically passed to the app-dev service via environment variables:
     - `S3_ENDPOINT`: URL of the MinIO server
     - `S3_ACCESS_KEY`: Access key for the S3 bucket
     - `S3_SECRET_KEY`: Secret key for the S3 bucket
     - `S3_BUCKET_NAME`: Name of the S3 bucket
     - `S3_REGION`: Region for the S3 bucket (default: us-east-1)
     - `S3_ALIAS_HOST`: Public URL/CDN for accessing S3 resources (default: "127.0.0.1:9000/gitingest-bucket")

#### Usage Examples

To run the application in development mode:

```bash
docker compose --profile dev up
```

To run the application in production mode:

```bash
docker compose --profile prod up -d
```

To build and run the application:

```bash
docker compose --profile prod build
docker compose --profile prod up -d
```

## 🤝 Contributing

### Non-technical ways to contribute

- **Create an Issue**: If you find a bug or have an idea for a new feature, please [create an issue](https://github.com/coderamp-labs/gitingest/issues/new) on GitHub. This will help us track and prioritize your request.
- **Spread the Word**: If you like Gitingest, please share it with your friends, colleagues, and on social media. This will help us grow the community and make Gitingest even better.
- **Use Gitingest**: The best feedback comes from real-world usage! If you encounter any issues or have ideas for improvement, please let us know by [creating an issue](https://github.com/coderamp-labs/gitingest/issues/new) on GitHub or by reaching out to us on [Discord](https://discord.com/invite/zerRaGK9EC).

### Technical ways to contribute

Gitingest aims to be friendly for first time contributors, with a simple Python and HTML codebase. If you need any help while working with the code, reach out to us on [Discord](https://discord.com/invite/zerRaGK9EC). For detailed instructions on how to make a pull request, see [CONTRIBUTING.md](./CONTRIBUTING.md).

## 🛠️ Stack

- [Tailwind CSS](https://tailwindcss.com) - Frontend
- [FastAPI](https://github.com/fastapi/fastapi) - Backend framework
- [Jinja2](https://jinja.palletsprojects.com) - HTML templating
- [tiktoken](https://github.com/openai/tiktoken) - Token estimation
- [posthog](https://github.com/PostHog/posthog) - Amazing analytics
- [Sentry](https://sentry.io) - Error tracking and performance monitoring

### Looking for a JavaScript/FileSystemNode package?

Check out the NPM alternative 📦 Repomix: <https://github.com/yamadashy/repomix>

## 🚀 Project Growth

[![Star History Chart](https://api.star-history.com/svg?repos=coderamp-labs/gitingest&type=Date)](https://star-history.com/#coderamp-labs/gitingest&Date)

```

### File: requirements.txt
```txt
boto3>=1.28.0  # AWS SDK for S3 support
click>=8.0.0
fastapi[standard]>=0.109.1  # Vulnerable to https://osv.dev/vulnerability/PYSEC-2024-38
httpx
loguru>=0.7.0
pathspec>=0.12.1
prometheus-client
pydantic
python-dotenv
sentry-sdk[fastapi]
slowapi
starlette>=0.40.0  # Vulnerable to https://osv.dev/vulnerability/GHSA-f96h-pmfr-66vw
tiktoken>=0.7.0  # Support for o200k_base encoding
uvicorn>=0.11.7  # Vulnerable to https://osv.dev/vulnerability/PYSEC-2020-150

```

### File: src\server\main.py
```py
"""Main module for the FastAPI application."""

from __future__ import annotations

import os
import threading
from pathlib import Path

import sentry_sdk
from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from slowapi.errors import RateLimitExceeded
from starlette.middleware.trustedhost import TrustedHostMiddleware

# Import logging configuration first to intercept all logging
from gitingest.utils.logging_config import get_logger
from server.metrics_server import start_metrics_server
from server.routers import dynamic, index, ingest
from server.server_config import get_version_info, templates
from server.server_utils import limiter, rate_limit_exception_handler

# Load environment variables from .env file
load_dotenv()

# Initialize logger for this module
logger = get_logger(__name__)

# Initialize Sentry SDK if enabled
if os.getenv("GITINGEST_SENTRY_ENABLED") is not None:
    sentry_dsn = os.getenv("GITINGEST_SENTRY_DSN")

    # Only initialize Sentry if DSN is provided
    if sentry_dsn:
        # Configure Sentry options from environment variables
        traces_sample_rate = float(os.getenv("GITINGEST_SENTRY_TRACES_SAMPLE_RATE", "1.0"))
        profile_session_sample_rate = float(os.getenv("GITINGEST_SENTRY_PROFILE_SESSION_SAMPLE_RATE", "1.0"))
        profile_lifecycle_raw = os.getenv("GITINGEST_SENTRY_PROFILE_LIFECYCLE", "trace")
        profile_lifecycle = profile_lifecycle_raw if profile_lifecycle_raw in ("manual", "trace") else "trace"
        send_default_pii = os.getenv("GITINGEST_SENTRY_SEND_DEFAULT_PII", "true").lower() == "true"
        sentry_environment = os.getenv("GITINGEST_SENTRY_ENVIRONMENT", "")

        sentry_sdk.init(
            dsn=sentry_dsn,
            # Add data like request headers and IP for users
            send_default_pii=send_default_pii,
            # Set traces_sample_rate to capture transactions for tracing
            traces_sample_rate=traces_sample_rate,
            # Set profile_session_sample_rate to profile sessions
            profile_session_sample_rate=profile_session_sample_rate,
            # Set profile_lifecycle to automatically run the profiler
            profile_lifecycle=profile_lifecycle,
            # Set environment name
            environment=sentry_environment,
        )

# Initialize the FastAPI application
app = FastAPI(docs_url=None, redoc_url=None)
app.state.limiter = limiter

# Register the custom exception handler for rate limits
app.add_exception_handler(RateLimitExceeded, rate_limit_exception_handler)

# Start metrics server in a separate thread if enabled
if os.getenv("GITINGEST_METRICS_ENABLED") is not None:
    metrics_host = os.getenv("GITINGEST_METRICS_HOST", "127.0.0.1")
    metrics_port = int(os.getenv("GITINGEST_METRICS_PORT", "9090"))
    metrics_thread = threading.Thread(
        target=start_metrics_server,
        args=(metrics_host, metrics_port),
        daemon=True,
    )
    metrics_thread.start()


# Mount static files dynamically to serve CSS, JS, and other static assets
static_dir = Path(__file__).parent.parent / "static"
app.mount("/static", StaticFiles(directory=static_dir), name="static")


# Fetch allowed hosts from the environment or use the default values
allowed_hosts = os.getenv("ALLOWED_HOSTS")
if allowed_hosts:
    allowed_hosts = allowed_hosts.split(",")
else:
    # Define the default allowed hosts for the application
    default_allowed_hosts = ["gitingest.com", "*.gitingest.com", "localhost", "127.0.0.1"]
    allowed_hosts = default_allowed_hosts

# Add middleware to enforce allowed hosts
app.add_middleware(TrustedHostMiddleware, allowed_hosts=allowed_hosts)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint to verify that the server is running.

    **Returns**

    - **dict[str, str]**: A JSON object with a "status" key indicating the server's health status.

    """
    return {"status": "healthy"}


@app.head("/", include_in_schema=False)
async def head_root() -> HTMLResponse:
    """Respond to HTTP HEAD requests for the root URL.

    **This endpoint mirrors the headers and status code of the index page**
    for HTTP HEAD requests, providing a lightweight way to check if the server
    is responding without downloading the full page content.

    **Returns**

    - **HTMLResponse**: An empty HTML response with appropriate headers

    """
    return HTMLResponse(content=None, headers={"content-type": "text/html; charset=utf-8"})


@app.get("/robots.txt", include_in_schema=False)
async def robots() -> FileResponse:
    """Serve the robots.txt file to guide search engine crawlers.

    **This endpoint serves the ``robots.txt`` file located in the static directory**
    to provide instructions to search engine crawlers about which parts of the site
    they should or should not index.

    **Returns**

    - **FileResponse**: The ``robots.txt`` file located in the static directory

    """
    return FileResponse("static/robots.txt")


@app.get("/llms.txt")
async def llm_txt() -> FileResponse:
    """Serve the llm.txt file to provide information about the site to LLMs.

    **This endpoint serves the ``llms.txt`` file located in the static directory**
    to provide information about the site to Large Language Models (LLMs)
    and other AI systems that may be crawling the site.

    **Returns**

    - **FileResponse**: The ``llms.txt`` file located in the static directory

    """
    return FileResponse("static/llms.txt")


@app.get("/docs", response_class=HTMLResponse, include_in_schema=False)
async def custom_swagger_ui(request: Request) -> HTMLResponse:
    """Serve custom Swagger UI documentation.

    **This endpoint serves a custom Swagger UI interface**
    for the API documentation, providing an interactive way to explore
    and test the available endpoints.

    **Parameters**

    - **request** (`Request`): The incoming HTTP request

    **Returns**

    - **HTMLResponse**: Custom Swagger UI documentation page

    """
    context = {"request": request}
    context.update(get_version_info())
    return templates.TemplateResponse("swagger_ui.jinja", context)


@app.get("/api", include_in_schema=True)
def openapi_json_get() -> JSONResponse:
    """Return the OpenAPI schema.

    **This endpoint returns the OpenAPI schema (openapi.json)**
    that describes the API structure, endpoints, and data models
    for documentation and client generation purposes.

    **Returns**

    - **JSONResponse**: The OpenAPI schema as JSON

    """
    return JSONResponse(app.openapi())


@app.api_route("/api", methods=["POST", "PUT", "DELETE", "OPTIONS", "HEAD"], include_in_schema=False)
@app.api_route("/api/", methods=["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD"], include_in_schema=False)
def openapi_json() -> JSONResponse:
    """Return the OpenAPI schema for various HTTP methods.

    **This endpoint returns the OpenAPI schema (openapi.json)**
    for multiple HTTP methods, providing API documentation
    for clients that may use different request methods.

    **Returns**

    - **JSONResponse**: The OpenAPI schema as JSON

    """
    return JSONResponse(app.openapi())


# Include routers for modular endpoints
app.include_router(index)
app.include_router(ingest)
app.include_router(dynamic)

```

### File: src\static\js\index.js
```js
function submitExample(repoName) {
    const input = document.getElementById('input_text');

    if (input) {
        input.value = repoName;
        input.focus();
    }
}

// Make it visible to inline onclick handlers
window.submitExample = submitExample;

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: check-added-large-files
        description: 'Prevent large files from being committed.'
        args: ['--maxkb=10000']

      - id: check-case-conflict
        description: 'Check for files that would conflict in case-insensitive filesystems.'

      - id: fix-byte-order-marker
        description: 'Remove utf-8 byte order marker.'

      - id: mixed-line-ending
        description: 'Replace mixed line ending.'

      - id: destroyed-symlinks
        description: 'Detect symlinks which are changed to regular files with a content of a path which that symlink was pointing to.'

      - id: check-ast
        description: 'Check for parseable syntax.'

      - id: end-of-file-fixer
        description: 'Ensure that a file is either empty, or ends with one newline.'

      - id: trailing-whitespace
        description: 'Trim trailing whitespace.'
        exclude: CHANGELOG.md

      - id: check-docstring-first
        description: 'Check a common error of defining a docstring after code.'

      - id: requirements-txt-fixer
        description: 'Sort entries in requirements.txt.'

  - repo: https://github.com/MarcoGorelli/absolufy-imports
    rev: v0.3.1
    hooks:
      - id: absolufy-imports
        description: 'Automatically convert relative imports to absolute. (Use `args: [--never]` to revert.)'

  - repo: https://github.com/asottile/pyupgrade
    rev: v3.20.0
    hooks:
      - id: pyupgrade
        description: 'Automatically upgrade syntax for newer versions.'
        args: [--py3-plus, --py36-plus]

  - repo: https://github.com/pre-commit/pygrep-hooks
    rev: v1.10.0
    hooks:
      - id: python-check-blanket-noqa
        description: 'Enforce that `# noqa` annotations always occur with specific codes.'

      - id: python-check-blanket-type-ignore
        description: 'Enforce that `# type: ignore` annotations always occur with specific codes.'

      - id: python-use-type-annotations
        description: 'Enforce that python3.6+ type annotations are used instead of type comments.'

  - repo: https://github.com/PyCQA/isort
    rev: 6.0.1
    hooks:
      - id: isort
        description: 'Sort imports alphabetically, and automatically separated into sections and by type.'

  - repo: https://github.com/pre-commit/mirrors-eslint
    rev: v9.30.1
    hooks:
      - id: eslint
        description: 'Lint javascript files.'
        files: \.js$
        args: [--max-warnings=0, --fix]
        additional_dependencies:
          [
            'eslint@9.30.1',
            '@eslint/js@9.30.1',
            'eslint-plugin-import@2.32.0',
            'globals@16.3.0',
          ]

  - repo: https://github.com/djlint/djLint
    rev: v1.36.4
    hooks:
      - id: djlint-reformat-jinja

  - repo: https://github.com/igorshubovych/markdownlint-cli
    rev: v0.45.0
    hooks:
      - id: markdownlint
        description: 'Lint markdown files.'
        args: ['--disable=line-length', '--ignore=CHANGELOG.md']

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.12.2
    hooks:
      - id: ruff-check
      - id: ruff-format

  - repo: https://github.com/jsh9/pydoclint
    rev: 0.6.7
    hooks:
      - id: pydoclint
        name: pydoclint for source
        args: [--style=numpy]
        files: ^src/

  - repo: https://github.com/pycqa/pylint
    rev: v3.3.7
    hooks:
      - id: pylint
        name: pylint for source
        files: ^src/
        additional_dependencies:
          [
            boto3>=1.28.0,
            click>=8.0.0,
            'fastapi[standard]>=0.109.1',
            gitpython>=3.1.0,
            httpx,
            loguru>=0.7.0,
            pathspec>=0.12.1,
            prometheus-client,
            pydantic,
            pytest-asyncio,
            pytest-mock,
            python-dotenv,
            'sentry-sdk[fastapi]',
            slowapi,
            starlette>=0.40.0,
            strenum; python_version < '3.11',
            tiktoken>=0.7.0,
            typing_extensions>= 4.0.0; python_version < '3.10',
            uvicorn>=0.11.7,
          ]

      - id: pylint
        name: pylint for tests
        files: ^tests/
        args:
          - --rcfile=tests/.pylintrc
        additional_dependencies:
          [
            boto3>=1.28.0,
            click>=8.0.0,
            'fastapi[standard]>=0.109.1',
            gitpython>=3.1.0,
            httpx,
            loguru>=0.7.0,
            pathspec>=0.12.1,
            prometheus-client,
            pydantic,
            pytest-asyncio,
            pytest-mock,
            python-dotenv,
            'sentry-sdk[fastapi]',
            slowapi,
            starlette>=0.40.0,
            strenum; python_version < '3.11',
            tiktoken>=0.7.0,
            typing_extensions>= 4.0.0; python_version < '3.10',
            uvicorn>=0.11.7,
          ]

  - repo: meta
    hooks:
      - id: check-hooks-apply
      - id: check-useless-excludes
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.16.3
    hooks:
      - id: gitleaks

```

### File: .release-please-manifest.json
```json
{".":"0.3.1"}

```

### File: CHANGELOG.md
```md
# Changelog

## [0.3.1](https://github.com/coderamp-labs/gitingest/compare/v0.3.0...v0.3.1) (2025-07-31)


### Bug Fixes

* make cache aware of subpaths ([#481](https://github.com/coderamp-labs/gitingest/issues/481)) ([8b59bef](https://github.com/coderamp-labs/gitingest/commit/8b59bef541f858ef44eba8fce6ace77df9dea01c))

## [0.3.0](https://github.com/coderamp-labs/gitingest/compare/v0.2.1...v0.3.0) (2025-07-30)


### Features

* **logging:** implement loguru ([#473](https://github.com/coderamp-labs/gitingest/issues/473)) ([d061b48](https://github.com/coderamp-labs/gitingest/commit/d061b4877a253ba3f0480d329f025427c7f70177))
* serve cached digest if available ([#462](https://github.com/coderamp-labs/gitingest/issues/462)) ([efe5a26](https://github.com/coderamp-labs/gitingest/commit/efe5a2686142b5ee4984061ebcec23c3bf3495d5))


### Bug Fixes

* handle network errors gracefully in token count estimation ([#437](https://github.com/coderamp-labs/gitingest/issues/437)) ([5fbb445](https://github.com/coderamp-labs/gitingest/commit/5fbb445cd8725e56972f43ec8b5e12cb299e9e83))
* improved server side cleanup after ingest ([#477](https://github.com/coderamp-labs/gitingest/issues/477)) ([2df0eb4](https://github.com/coderamp-labs/gitingest/commit/2df0eb43989731ae40a9dd82d310ff76a794a46d))


### Documentation

* **contributing:** update PR title guidelines to enforce convention ([#476](https://github.com/coderamp-labs/gitingest/issues/476)) ([d1f8a80](https://github.com/coderamp-labs/gitingest/commit/d1f8a80826ca38ec105a1878742fe351d4939d6e))

## [0.2.1](https://github.com/coderamp-labs/gitingest/compare/v0.2.0...v0.2.1) (2025-07-27)


### Bug Fixes

* remove logarithm conversion from the backend and correctly process max file size in kb ([#464](https://github.com/coderamp-labs/gitingest/issues/464)) ([932bfef](https://github.com/coderamp-labs/gitingest/commit/932bfef85db66704985c83f3f7c427756bd14023))

## [0.2.0](https://github.com/coderamp-labs/gitingest/compare/v0.1.5...v0.2.0) (2025-07-26)

### Features

* `include_submodules` option ([#313](https://github.com/coderamp-labs/gitingest/issues/313)) ([38c2317](https://github.com/coderamp-labs/gitingest/commit/38c23171a14556a2cdd05c0af8219f4dc789defd))
* add Tailwind CSS pipeline, tag-aware cloning & overhaul CI/CD ([#352](https://github.com/coderamp-labs/gitingest/issues/352)) ([b683e59](https://github.com/coderamp-labs/gitingest/commit/b683e59b5b1a31d27cc5c6ce8fb62da9b660613b))
* add Tailwind CSS pipeline, tag-aware cloning & overhaul CI/CD ([#352](https://github.com/coderamp-labs/gitingest/issues/352)) ([016817d](https://github.com/coderamp-labs/gitingest/commit/016817d5590c1412498b7532f6e854d20239c6be))
* **ci:** build Docker Image on PRs ([#382](https://github.com/coderamp-labs/gitingest/issues/382)) ([bc8cdb4](https://github.com/coderamp-labs/gitingest/commit/bc8cdb459482948c27e780b733ac7216d822529a))
* implement prometheus exporter ([#406](https://github.com/coderamp-labs/gitingest/issues/406)) ([1016f6e](https://github.com/coderamp-labs/gitingest/commit/1016f6ecb3b1b066d541d1eba1ddffec49b15f16))
* implement S3 integration for storing and retrieving digest files ([#427](https://github.com/coderamp-labs/gitingest/issues/427)) ([414e851](https://github.com/coderamp-labs/gitingest/commit/414e85189fb9055491530ba8c0665c798474451e))
* integrate Sentry for error tracking and performance monitoring ([#408](https://github.com/coderamp-labs/gitingest/issues/408)) ([590e55a](https://github.com/coderamp-labs/gitingest/commit/590e55a4d28a4f5c0beafbd12c525828fa79e221))
* Refactor backend to a rest api ([#346](https://github.com/coderamp-labs/gitingest/issues/346)) ([2b1f228](https://github.com/coderamp-labs/gitingest/commit/2b1f228ae1f6d1f7ee471794d258b13fcac25a96))
* **ui:** add inline PAT info tooltip inside token field ([#348](https://github.com/coderamp-labs/gitingest/issues/348)) ([2592303](https://github.com/coderamp-labs/gitingest/commit/25923037ea6cd2f8ef33a6cf1f0406c2b4f0c9b6))


### Bug Fixes

* enable metrics if env var is defined instead of being "True" ([#407](https://github.com/coderamp-labs/gitingest/issues/407)) ([fa2e192](https://github.com/coderamp-labs/gitingest/commit/fa2e192c05864c8db90bda877e9efb9b03caf098))
* fix docker container not launching ([#449](https://github.com/coderamp-labs/gitingest/issues/449)) ([998cea1](https://github.com/coderamp-labs/gitingest/commit/998cea15b4f79c5d6f840b5d3d916f83c8be3a07))
* frontend directory tree ([#363](https://github.com/coderamp-labs/gitingest/issues/363)) ([0fcf8a9](https://github.com/coderamp-labs/gitingest/commit/0fcf8a956f7ec8403a025177f998f92ddee96de0))
* gitignore and gitingestignore files are now correctly processed … ([#416](https://github.com/coderamp-labs/gitingest/issues/416)) ([74e503f](https://github.com/coderamp-labs/gitingest/commit/74e503fa1140feb74aa5350a32f0025c43097da1))
* Potential fix for code scanning alert no. 75: Uncontrolled data used in path expression ([#421](https://github.com/coderamp-labs/gitingest/issues/421)) ([9ceaf6c](https://github.com/coderamp-labs/gitingest/commit/9ceaf6cbbb0cdefbc79f78c5285406b9188b2d3d))
* reset pattern form when switching between include/exclude patterns ([#417](https://github.com/coderamp-labs/gitingest/issues/417)) ([7085e13](https://github.com/coderamp-labs/gitingest/commit/7085e138a74099b1df189b3bf9b8a333c8769380))
* temp files cleanup after ingest([#309](https://github.com/coderamp-labs/gitingest/issues/309)) ([e669e44](https://github.com/coderamp-labs/gitingest/commit/e669e444fa1e6130f3f22952dd81f0ca3fe08fa5))
* **ui:** update layout in PAT section to avoid overlaps & overflows ([#331](https://github.com/coderamp-labs/gitingest/issues/331)) ([b39ef54](https://github.com/coderamp-labs/gitingest/commit/b39ef5416c1f8a7993a8249161d2a898b7387595))
* **windows:** warn if Git long path support is disabled, do not fail ([b8e375f](https://github.com/coderamp-labs/gitingest/commit/b8e375f71cae7d980cf431396c4414a6dbd0588c))


### Documentation

* add GitHub Issue Form for bug reports ([#403](https://github.com/coderamp-labs/gitingest/issues/403)) ([4546449](https://github.com/coderamp-labs/gitingest/commit/4546449bbc1e4a7ad0950c4b831b8855a98628fd))
* add GitHub Issue Form for feature requests ([#404](https://github.com/coderamp-labs/gitingest/issues/404)) ([9b1fc58](https://github.com/coderamp-labs/gitingest/commit/9b1fc58900ae18a3416fe3cf9b5e301a65a8e9fd))
* Fix CLI help text accuracy ([#332](https://github.com/coderamp-labs/gitingest/issues/332)) ([fdcbc53](https://github.com/coderamp-labs/gitingest/commit/fdcbc53cadde6a5dc3c3626120df1935b63693b2))


### Code Refactoring

* centralize PAT validation, streamline repo checks & misc cleanup ([#349](https://github.com/coderamp-labs/gitingest/issues/349)) ([cea0edd](https://github.com/coderamp-labs/gitingest/commit/cea0eddce8c6846bc6271cb3a8d15320e103214c))
* centralize PAT validation, streamline repo checks & misc cleanup ([#349](https://github.com/coderamp-labs/gitingest/issues/349)) ([f8d397e](https://github.com/coderamp-labs/gitingest/commit/f8d397e66e3382d12f8a0ed05d291a39db830bda))

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
<romain@coderamp.io>.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org),
version 2.0, available at
<https://www.contributor-covenant.org/version/2/0/code_of_conduct.html>.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

For answers to common questions about this code of conduct, see the FAQ at
<https://www.contributor-covenant.org/faq>. Translations are available at
<https://www.contributor-covenant.org/translations>.

```

### File: CONTRIBUTING.md
```md
# Contributing to Gitingest

Thanks for your interest in contributing to **Gitingest** 🚀 Our goal is to keep the codebase friendly to first-time
contributors.
If you ever get stuck, reach out on [Discord](https://discord.com/invite/zerRaGK9EC).

---

## How to Contribute (non-technical)

- **Create an Issue** – found a bug or have a feature idea?
  [Open an issue](https://github.com/coderamp-labs/gitingest/issues/new).
- **Spread the Word** – tweet, blog, or tell a friend.
- **Use Gitingest** – real-world usage gives the best feedback. File issues or ping us
  on [Discord](https://discord.com/invite/zerRaGK9EC) with anything you notice.

---

## How to submit a Pull Request

> **Prerequisites**: The project uses **Python 3.9+** and `pre-commit` for development.

1. **Fork** the repository.

2. **Clone** your fork:

   ```bash
   git clone https://github.com/coderamp-labs/gitingest.git
   cd gitingest
   ```

3. **Set up the dev environment**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev,server]"
   pre-commit install
   ```

4. **Create a branch** for your changes:

   ```bash
   git checkout -b your-branch
   ```

5. **Make your changes** (and add tests when relevant).

6. **Stage** the changes:

   ```bash
   git add .
   ```

7. **Run the backend test suite**:

   ```bash
   pytest
   ```

8. *(Optional)* **Run `pre-commit` on all files** to check hooks without committing:

   ```bash
   pre-commit run --all-files
   ```

9. **Run the local server** to sanity-check:

    ```bash
    python -m server
    ```

   Open [http://localhost:8000](http://localhost:8000) to confirm everything works.

10. **Commit** (signed):

    ```bash
    git commit -S -m "Your commit message"
    ```

    If *pre-commit* complains, fix the problems and repeat **5 – 9**.

11. **Push** your branch:

    ```bash
    git push origin your-branch
    ```

12. **Open a pull request** on GitHub with a clear description.

    > **Important:** Pull request titles **must follow
    the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification**. This helps with
    changelogs and automated releases.

13. **Iterate** on any review feedback—update your branch and repeat **6 – 11** as needed.

*(Optional) Invite a maintainer to your branch for easier collaboration.*

```

### File: release-please-config.json
```json
{
  "$schema": "https://raw.githubusercontent.com/googleapis/release-please/main/schemas/config.json",
  "packages": {
    ".": {
      "release-type": "python",
      "bump-minor-pre-major": true
    }
  }
}

```

### File: renovate.json
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ]
}

```

### File: requirements-dev.txt
```txt
-r requirements.txt
eval-type-backport
pre-commit
pytest
pytest-asyncio
pytest-cov
pytest-mock

```

### File: SECURITY.md
```md
# Security Policy

## Reporting a Vulnerability

If you have discovered a vulnerability inside the project, report it privately at <romain@coderamp.io>. This way the maintainer can work on a proper fix without disclosing the problem to the public before it has been solved.

```

### File: tests\conftest.py
```py
"""Fixtures for tests.

This file provides shared fixtures for creating sample queries, a temporary directory structure, and a helper function
to write ``.ipynb`` notebooks for testing notebook utilities.
"""

from __future__ import annotations

import json
import sys
import uuid
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Dict
from unittest.mock import AsyncMock, MagicMock

import pytest

from gitingest.query_parser import IngestionQuery

if TYPE_CHECKING:
    from pytest_mock import MockerFixture

WriteNotebookFunc = Callable[[str, Dict[str, Any]], Path]

DEMO_URL = "https://github.com/user/repo"
LOCAL_REPO_PATH = "/tmp/repo"
DEMO_COMMIT = "deadbeefdeadbeefdeadbeefdeadbeefdeadbeef"


def get_ensure_git_installed_call_count() -> int:
    """Get the number of calls made by ensure_git_installed based on platform.

    On Windows, ensure_git_installed makes 2 calls:
    1. git --version
    2. git config core.longpaths

    On other platforms, it makes 1 call:
    1. git --version

    Returns
    -------
    int
        The number of calls made by ensure_git_installed

    """
    return 2 if sys.platform == "win32" else 1


@pytest.fixture
def sample_query() -> IngestionQuery:
    """Provide a default ``IngestionQuery`` object for use in tests.

    This fixture returns a ``IngestionQuery`` pre-populated with typical fields and some default ignore patterns.

    Returns
    -------
    IngestionQuery
        The sample ``IngestionQuery`` object.

    """
    return IngestionQuery(
        user_name="test_user",
        repo_name="test_repo",
        local_path=Path("/tmp/test_repo").resolve(),
        slug="test_user/test_repo",
        id=uuid.uuid4(),
        branch="main",
        max_file_size=1_000_000,
        ignore_patterns={"*.pyc", "__pycache__", ".git"},
    )


@pytest.fixture
def temp_directory(tmp_path: Path) -> Path:
    """Create a temporary directory structure for testing repository scanning.

    The structure includes:
    test_repo/
    ├── file1.txt
    ├── file2.py
    ├── src/
    │   ├── subfile1.txt
    │   ├── subfile2.py
    │   └── subdir/
    │       ├── file_subdir.txt
    │       └── file_subdir.py
    ├── dir1/
    │   └── file_dir1.txt
    └── dir2/
        └── file_dir2.txt

    Parameters
    ----------
    tmp_path : Path
        The temporary directory path provided by the ``tmp_path`` fixture.

    Returns
    -------
    Path
        The path to the created ``test_repo`` directory.

    """
    test_dir = tmp_path / "test_repo"
    test_dir.mkdir()

    # Root files
    (test_dir / "file1.txt").write_text("Hello World")
    (test_dir / "file2.py").write_text("print('Hello')")

    # src directory and its files
    src_dir = test_dir / "src"
    src_dir.mkdir()
    (src_dir / "subfile1.txt").write_text("Hello from src")
    (src_dir / "subfile2.py").write_text("print('Hello from src')")

    # src/subdir and its files
    subdir = src_dir / "subdir"
    subdir.mkdir()
    (subdir / "file_subdir.txt").write_text("Hello from subdir")
    (subdir / "file_subdir.py").write_text("print('Hello from subdir')")

    # dir1 and its file
    dir1 = test_dir / "dir1"
    dir1.mkdir()
    (dir1 / "file_dir1.txt").write_text("Hello from dir1")

    # dir2 and its file
    dir2 = test_dir / "dir2"
    dir2.mkdir()
    (dir2 / "file_dir2.txt").write_text("Hello from dir2")

    return test_dir


@pytest.fixture
def write_notebook(tmp_path: Path) -> WriteNotebookFunc:
    """Provide a helper function to write a ``.ipynb`` notebook file with the given content.

    Parameters
    ----------
    tmp_path : Path
        The temporary directory path provided by the ``tmp_path`` fixture.

    Returns
    -------
    WriteNotebookFunc
        A callable that accepts a filename and a dictionary (representing JSON notebook data), writes it to a
        ``.ipynb`` file, and returns the path to the file.

    """

    def _write_notebook(name: str, content: dict[str, Any]) -> Path:
        notebook_path = tmp_path / name
        with notebook_path.open(mode="w", encoding="utf-8") as f:
            json.dump(content, f)
        return notebook_path

    return _write_notebook


@pytest.fixture
def stub_resolve_sha(mocker: MockerFixture) -> dict[str, AsyncMock]:
    """Patch *both* async helpers that hit the network.

    Include this fixture *only* in tests that should stay offline.
    """
    head_mock = mocker.patch(
        "gitingest.utils.query_parser_utils._resolve_ref_to_sha",
        new_callable=mocker.AsyncMock,
        return_value=DEMO_COMMIT,
    )
    ref_mock = mocker.patch(
        "gitingest.utils.git_utils._resolve_ref_to_sha",
        new_callable=mocker.AsyncMock,
        return_value=DEMO_COMMIT,
    )
    # return whichever you want to assert on; here we return the dict
    return {"head": head_mock, "ref": ref_mock}


@pytest.fixture
def stub_branches(mocker: MockerFixture) -> Callable[[list[str]], None]:
    """Return a function that stubs git branch discovery to *branches*."""

    def _factory(branches: list[str]) -> None:
        # Patch the GitPython fetch function
        mocker.patch(
            "gitingest.utils.git_utils.fetch_remote_branches_or_tags",
            new_callable=AsyncMock,
            return_value=branches,
        )

        # Patch GitPython's ls_remote method to return the mocked output
        ls_remote_output = "\n".join(f"{DEMO_COMMIT[:12]}{i:02d}\trefs/heads/{b}" for i, b in enumerate(branches))
        mock_git_cmd = mocker.patch("git.Git")
        mock_git_cmd.return_value.ls_remote.return_value = ls_remote_output

        # Also patch the git module imports in our utils
        mocker.patch("gitingest.utils.git_utils.git.Git", return_value=mock_git_cmd.return_value)

    return _factory


@pytest.fixture
def repo_exists_true(mocker: MockerFixture) -> AsyncMock:
    """Patch ``gitingest.clone.check_repo_exists`` to always return ``True``."""
    return mocker.patch("gitingest.clone.check_repo_exists", return_value=True)


@pytest.fixture
def run_command_mock(mocker: MockerFixture) -> AsyncMock:
    """Patch ``gitingest.clone.run_command`` with an ``AsyncMock``.

    The mocked function returns a dummy process whose ``communicate`` method yields generic
    ``stdout`` / ``stderr`` bytes. Tests can still access / tweak the mock via the fixture argument.
    """
    mock = AsyncMock(side_effect=_fake_run_command)
    mocker.patch("gitingest.utils.git_utils.run_command", mock)

    # Mock GitPython components
    _setup_gitpython_mocks(mocker)

    return mock


@pytest.fixture
def gitpython_mocks(mocker: MockerFixture) -> dict[str, MagicMock]:
    """Provide comprehensive GitPython mocks for testing."""
    return _setup_gitpython_mocks(mocker)


def _setup_gitpython_mocks(mocker: MockerFixture) -> dict[str, MagicMock]:
    """Set up comprehensive GitPython mocks."""
    # Mock git.Git class
    mock_git_cmd = MagicMock()
    mock_git_cmd.version.return_value = "git version 2.34.1"
    mock_git_cmd.config.return_value = "true"
    mock_git_cmd.execute.return_value = f"{DEMO_COMMIT}\trefs/heads/main\n"
    mock_git_cmd.ls_remote.return_value = f"{DEMO_COMMIT}\trefs/heads/main\n"
    mock_git_cmd.clone.return_value = ""

    # Mock git.Repo class
    mock_repo = MagicMock()
    mock_repo.git = MagicMock()
    mock_repo.git.fetch = MagicMock()
    mock_repo.git.checkout = MagicMock()
    mock_repo.git.submodule = MagicMock()
    mock_repo.git.execute = MagicMock()
    mock_repo.git.config = MagicMock()
    mock_repo.git.sparse_checkout = MagicMock()

    # Mock git.Repo.clone_from
    mock_clone_from = MagicMock(return_value=mock_repo)

    git_git_mock = mocker.patch("git.Git", return_value=mock_git_cmd)
    git_repo_mock = mocker.patch("git.Repo", return_value=mock_repo)
    mocker.patch("git.Repo.clone_from", mock_clone_from)

    # Patch imports in our modules
    mocker.patch("gitingest.utils.git_utils.git.Git", return_value=mock_git_cmd)
    mocker.patch("gitingest.utils.git_utils.git.Repo", return_value=mock_repo)
    mocker.patch("gitingest.clone.git.Git", return_value=mock_git_cmd)
    mocker.patch("gitingest.clone.git.Repo", return_value=mock_repo)
    mocker.patch("gitingest.clone.git.Repo.clone_from", mock_clone_from)

    return {
        "git_cmd": mock_git_cmd,
        "repo": mock_repo,
        "clone_from": mock_clone_from,
        "git_git_mock": git_git_mock,
        "git_repo_mock": git_repo_mock,
    }


async def _fake_run_command(*args: str) -> tuple[bytes, bytes]:
    if "ls-remote" in args:
        # single match: <sha> <tab>refs/heads/main
        return (f"{DEMO_COMMIT}\trefs/heads/main\n".encode(), b"")
    return (b"output", b"error")

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
