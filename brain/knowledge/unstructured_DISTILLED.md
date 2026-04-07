---
id: unstructured
type: knowledge
owner: OA_Triage
---
# unstructured
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<h3 align="center">
  <img
    src="https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/img/unstructured_logo.png"
    height="200"
  >
</h3>

<div align="center">

  <a href="https://github.com/Unstructured-IO/unstructured/blob/main/LICENSE.md">![https://pypi.python.org/pypi/unstructured/](https://img.shields.io/pypi/l/unstructured.svg)</a>
  <a href="https://pypi.python.org/pypi/unstructured/">![https://pypi.python.org/pypi/unstructured/](https://img.shields.io/pypi/pyversions/unstructured.svg)</a>
  <a href="https://GitHub.com/unstructured-io/unstructured/graphs/contributors">![https://GitHub.com/unstructured-io/unstructured.js/graphs/contributors](https://img.shields.io/github/contributors/unstructured-io/unstructured)</a>
  <a href="https://github.com/Unstructured-IO/unstructured/blob/main/CODE_OF_CONDUCT.md">![code_of_conduct.md](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg) </a>
  <a href="https://GitHub.com/unstructured-io/unstructured/releases">![https://GitHub.com/unstructured-io/unstructured.js/releases](https://img.shields.io/github/release/unstructured-io/unstructured)</a>
  <a href="https://pypi.python.org/pypi/unstructured/">![https://github.com/Naereen/badges/](https://badgen.net/badge/Open%20Source%20%3F/Yes%21/blue?icon=github)</a>
  [![Downloads](https://static.pepy.tech/badge/unstructured)](https://pepy.tech/project/unstructured)
  [![Downloads](https://static.pepy.tech/badge/unstructured/month)](https://pepy.tech/project/unstructured)
  <a
   href="https://www.phorm.ai/query?projectId=34efc517-2201-4376-af43-40c4b9da3dc5">
	<img src="https://img.shields.io/badge/Phorm-Ask_AI-%23F2777A.svg?&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNSIgaGVpZ2h0PSI0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogIDxwYXRoIGQ9Ik00LjQzIDEuODgyYTEuNDQgMS40NCAwIDAgMS0uMDk4LjQyNmMtLjA1LjEyMy0uMTE1LjIzLS4xOTIuMzIyLS4wNzUuMDktLjE2LjE2NS0uMjU1LjIyNmExLjM1MyAxLjM1MyAwIDAgMS0uNTk1LjIxMmMtLjA5OS4wMTItLjE5Mi4wMTQtLjI3OS4wMDZsLTEuNTkzLS4xNHYtLjQwNmgxLjY1OGMuMDkuMDAxLjE3LS4xNjkuMjQ2LS4xOTFhLjYwMy42MDMgMCAwIDAgLjItLjEwNi41MjkuNTI5IDAgMCAwIC4xMzgtLjE3LjY1NC42NTQgMCAwIDAgLjA2NS0uMjRsLjAyOC0uMzJhLjkzLjkzIDAgMCAwLS4wMzYtLjI0OS41NjcuNTY3IDAgMCAwLS4xMDMtLjIuNTAyLjUwMiAwIDAgMC0uMTY4LS4xMzguNjA4LjYwOCAwIDAgMC0uMjQtLjA2N0wyLjQzNy43MjkgMS42MjUuNjcxYS4zMjIuMzIyIDAgMCAwLS4yMzIuMDU4LjM3NS4zNzUgMCAwIDAtLjExNi4yMzJsLS4xMTYgMS40NS0uMDU4LjY5Ny0uMDU4Ljc1NEwuNzA1IDRsLS4zNTctLjA3OUwuNjAyLjkwNkMuNjE3LjcyNi42NjMuNTc0LjczOS40NTRhLjk1OC45NTggMCAwIDEgLjI3NC0uMjg1Ljk3MS45NzEgMCAwIDEgLjMzNy0uMTRjLjExOS0uMDI2LjIyNy0uMDM0LjMyNS0uMDI2TDMuMjMyLjE2Yy4xNTkuMDE0LjMzNi4wMy40NTkuMDgyYTEuMTczIDEuMTczIDAgMCAxIC41NDUuNDQ3Yy4wNi4wOTQuMTA5LjE5Mi4xNDQuMjkzYTEuMzkyIDEuMzkyIDAgMCAxIC4wNzguNThsLS4wMjkuMzJaIiBmaWxsPSIjRjI3NzdBIi8+CiAgPHBhdGggZD0iTTQuMDgyIDIuMDA3YTEuNDU1IDEuNDU1IDAgMCAxLS4wOTguNDI3Yy0uMDUuMTI0LS4xMTQuMjMyLS4xOTIuMzI0YTEuMTMgMS4xMyAwIDAgMS0uMjU0LjIyNyAxLjM1MyAxLjM1MyAwIDAgMS0uNTk1LjIxNGMtLjEuMDEyLS4xOTMuMDE0LS4yOC4wMDZsLTEuNTYtLjEwOC4wMzQtLjQwNi4wMy0uMzQ4IDEuNTU5LjE1NGMuMDkgMCAuMTczLS4wMS4yNDgtLjAzM2EuNjAzLjYwMyAwIDAgMCAuMi0uMTA2LjUzMi41MzIgMCAwIDAgLjEzOS0uMTcyLjY2LjY2IDAgMCAwIC4wNjQtLjI0MWwuMDI5LS4zMjFhLjk0Ljk0IDAgMCAwLS4wMzYtLjI1LjU3LjU3IDAgMCAwLS4xMDMtLjIwMi41MDIuNTAyIDAgMCAwLS4xNjgtLjEzOC42MDUuNjA1IDAgMCAwLS4yNC0uMDY3TDEuMjczLjgyN2MtLjA5NC0uMDA4LS4xNjguMDEtLjIyMS4wNTUtLjA1My4wNDUtLjA4NC4xMTQtLjA5Mi4yMDZMLjcwNSA0IDAgMy45MzhsLjI1NS0yLjkxMUExLjAxIDEuMDEgMCAwIDEgLjM5My41NzIuOTYyLjk2MiAwIDAgMSAuNjY2LjI4NmEuOTcuOTcgMCAwIDEgLjMzOC0uMTRDMS4xMjIuMTIgMS4yMy4xMSAxLjMyOC4xMTlsMS41OTMuMTRjLjE2LjAxNC4zLjA0Ny40MjMuMWExLjE3IDEuMTcgMCAwIDEgLjU0NS40NDhjLjA2MS4wOTUuMTA5LjE5My4xNDQuMjk1YTEuNDA2IDEuNDA2IDAgMCAxIC4wNzcuNTgzbC0uMDI4LjMyMloiIGZpbGw9IndoaXRlIi8+CiAgPHBhdGggZD0iTTQuMDgyIDIuMDA3YTEuNDU1IDEuNDU1IDAgMCAxLS4wOTguNDI3Yy0uMDUuMTI0LS4xMTQuMjMyLS4xOTIuMzI0YTEuMTMgMS4xMyAwIDAgMS0uMjU0LjIyNyAxLjM1MyAxLjM1MyAwIDAgMS0uNTk1LjIxNGMtLjEuMDEyLS4xOTMuMDE0LS4yOC4wMDZsLTEuNTYtLjEwOC4wMzQtLjQwNi4wMy0uMzQ4IDEuNTU5LjE1NGMuMDkgMCAuMTczLS4wMS4yNDgtLjAzM2EuNjAzLjYwMyAwIDAgMCAuMi0uMTA2LjUzMi41MzIgMCAwIDAgLjEzOS0uMTcyLjY2LjY2IDAgMCAwIC4wNjQtLjI0MWwuMDI5LS4zMjFhLjk0Ljk0IDAgMCAwLS4wMzYtLjI1LjU3LjU3IDAgMCAwLS4xMDMtLjIwMi41MDIuNTAyIDAgMCAwLS4xNjgtLjEzOC42MDUuNjA1IDAgMCAwLS4yNC0uMDY3TDEuMjczLjgyN2MtLjA5NC0uMDA4LS4xNjguMDEtLjIyMS4wNTUtLjA1My4wNDUtLjA4NC4xMTQtLjA5Mi4yMDZMLjcwNSA0IDAgMy45MzhsLjI1NS0yLjkxMUExLjAxIDEuMDEgMCAwIDEgLjM5My41NzIuOTYyLjk2MiAwIDAgMSAuNjY2LjI4NmEuOTcuOTcgMCAwIDEgLjMzOC0uMTRDMS4xMjIuMTIgMS4yMy4xMSAxLjMyOC4xMTlsMS41OTMuMTRjLjE2LjAxNC4zLjA0Ny40MjMuMWExLjE3IDEuMTcgMCAwIDEgLjU0NS40NDhjLjA2MS4wOTUuMTA5LjE5My4xNDQuMjk1YTEuNDA2IDEuNDA2IDAgMCAxIC4wNzcuNTgzbC0uMDI4LjMyMloiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=" />
   </a>

</div>

<div>
  <p align="center">
  <a
  href="https://short.unstructured.io/pzw05l7">
    <img src="https://img.shields.io/badge/JOIN US ON SLACK-4A154B?style=for-the-badge&logo=slack&logoColor=white" />
  </a>
  <a href="https://www.linkedin.com/company/unstructuredio/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" />
  </a>
</div>

<h2 align="center">
  <p>Open-Source Pre-Processing Tools for Unstructured Data</p>
</h2>

The `unstructured` library provides open-source components for ingesting and pre-processing images and text documents, such as PDFs, HTML, Word docs, and [many more](https://docs.unstructured.io/open-source/core-functionality/partitioning). The use cases of `unstructured` revolve around streamlining and optimizing the data processing workflow for LLMs. `unstructured` modular functions and connectors form a cohesive system that simplifies data ingestion and pre-processing, making it adaptable to different platforms and efficient in transforming unstructured data into structured outputs.

## Try the Unstructured Platform Product

Ready to move your data processing pipeline to production, and take advantage of advanced features? Check out [Unstructured Platform](https://unstructured.io/enterprise). In addition to better processing performance, take advantage of chunking, embedding, and image and table enrichment generation, all from a low code UI or an API. [Request a demo](https://unstructured.io/contact) from our sales team to learn more about how to get started.

## :eight_pointed_black_star: Quick Start

There are several ways to use the `unstructured` library:
* [Run the library in a container](https://github.com/Unstructured-IO/unstructured#run-the-library-in-a-container) or
* Install the library
    1. [Install from PyPI](https://github.com/Unstructured-IO/unstructured#installing-the-library)
    2. [Install for local development](https://github.com/Unstructured-IO/unstructured#installation-instructions-for-local-development)
* For installation with `conda` on Windows system, please refer to the [documentation](https://unstructured-io.github.io/unstructured/installing.html#installation-with-conda-on-windows)

### Run the library in a container

The following instructions are intended to help you get up and running using Docker to interact with `unstructured`.
See [here](https://docs.docker.com/get-docker/) if you don't already have docker installed on your machine.

NOTE: we build multi-platform images to support both x86_64 and Apple silicon hardware. `docker pull` should download the corresponding image for your architecture, but you can specify with `--platform` (e.g. `--platform linux/amd64`) if needed.

We build Docker images for all pushes to `main`. We tag each image with the corresponding short commit hash (e.g. `fbc7a69`) and the application version (e.g. `0.5.5-dev1`). We also tag the most recent image with `latest`. To leverage this, `docker pull` from our image repository.

```bash
docker pull downloads.unstructured.io/unstructured-io/unstructured:latest
```

Once pulled, you can create a container from this image and shell to it.

```bash
# create the container
docker run -dt --name unstructured downloads.unstructured.io/unstructured-io/unstructured:latest

# this will drop you into a bash shell where the Docker image is running
docker exec -it unstructured bash
```

You can also build your own Docker image. Note that the base image is `wolfi-base`, which is
updated regularly. If you are building the image locally, it is possible `docker-build` could
fail due to upstream changes in `wolfi-base`.

If you only plan on parsing one type of data you can speed up building the image by commenting out some
of the packages/requirements necessary for other data types. See Dockerfile to know which lines are necessary
for your use case.

```bash
make docker-build

# this will drop you into a bash shell where the Docker image is running
make docker-start-bash
```

Once in the running container, you can try things directly in Python interpreter's interactive mode.
```bash
# this will drop you into a python console so you can run the below partition functions
python3

>>> from unstructured.partition.pdf import partition_pdf
>>> elements = partition_pdf(filename="example-docs/layout-parser-paper-fast.pdf")

>>> from unstructured.partition.text import partition_text
>>> elements = partition_text(filename="example-docs/fake-text.txt")
```

### Installing the library
Use the following instructions to get up and running with `unstructured` and test your
installation.

- Install the Python SDK to support all document types with `pip install "unstructured[all-docs]"`
  - For plain text files, HTML, XML, JSON and Emails that do not require any extra dependencies, you can run `pip install unstructured`
  - To process other doc types, you can install the extras required for those documents, such as `pip install "unstructured[docx,pptx]"`
- Install the following system dependencies if they are not already available on your system.
  Depending on what document types you're parsing, you may not need all of these.
    - `libmagic-dev` (filetype detection)
    - `poppler-utils` (images and PDFs)
    - `tesseract-ocr` (images and PDFs, install `tesseract-lang` for additional language support)
    - `libreoffice` (MS Office docs)
    - `pandoc` is bundled automatically via the `pypandoc-binary` Python package (no system install needed)

- For suggestions on how to install on the Windows and to learn about dependencies for other features, see the
  installation documentation [here](https://unstructured-io.github.io/unstructured/installing.html).

At this point, you should be able to run the following code:

```python
from unstructured.partition.auto import partition

elements = partition(filename="example-docs/eml/fake-email.eml")
print("\n\n".join([str(el) for el in elements]))
```

### Installation Instructions for Local Development

The following instructions are intended to help you get up and running with `unstructured`
locally if you are planning to contribute to the project.

This project uses [uv](https://docs.astral.sh/uv/) for dependency management. Install it first:

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Then install all dependencies (base, extras, dev, test, and lint groups):

```bash
make install
```

This runs `uv sync --locked --all-extras --all-groups`, which creates a virtual environment
and installs everything in one step. No need to manually create or activate a virtualenv.

To install only specific document-type extras:

```bash
uv sync --extra pdf
uv sync --extra csv --extra docx
```

To update the lock file after changing dependencies in `pyproject.toml`:

```bash
make lock
```

* Optional:
  * To install extras for processing images and PDFs locally, run `uv sync --extra pdf --extra image`.
  * For processing image files, `tesseract` is required. See [here](https://tesseract-ocr.github.io/tessdoc/Installation.html) for installation instructions.
  * For processing PDF files, `tesseract` and `poppler` are required. The [pdf2image docs](https://pdf2image.readthedocs.io/en/latest/installation.html) have instructions on installing `poppler` across various platforms.

Additionally, if you're planning to contribute to `unstructured`, we provide you an optional `pre-commit` configuration
file to ensure your code matches the formatting and linting standards used in `unstructured`.
If you'd prefer not to have code changes auto-tidied before every commit, you can use  `make check` to see
whether any linting or formatting changes should be applied, and `make tidy` to apply them.

If using the optional `pre-commit`, you'll just need to install the hooks with `pre-commit install` since the
`pre-commit` package is installed as part of `make install` mentioned above. Finally, if you decided to use `pre-commit`
you can also uninstall the hooks with `pre-commit uninstall`.

In addition to develop in your local OS we also provide a helper to use docker providing a development environment:

```bash
make docker-start-dev
```

This starts a docker container with your local repo mounted to `/mnt/local_unstructured`. This docker image allows you to develop without worrying about your OS's compatibility with the repo and its dependencies.

## :clap: Quick Tour

### Documentation
For more comprehensive documentation, visit https://docs.unstructured.io . You can also learn
more about our other products on the documentation page, including our SaaS API.

Here are a few pages from the [Open Source documentation page](https://docs.unstructured.io/open-source/introduction/overview)
that are helpful for new users to review:

- [Quick Start](https://docs.unstructured.io/open-source/introduction/quick-start)
- [Using the `unstructured` open source package](https://docs.unstructured.io/open-source/core-functionality/overview)
- [Connectors](https://docs.unstructured.io/open-source/ingest/overview)
- [Concepts](https://docs.unstructured.io/open-source/concepts/document-elements)
- [Integrations](https://docs.unstructured.io/open-source/integrations)


### PDF Document Parsing Example
The following examples show how to get started with the `unstructured` library. The easiest way to parse a document in unstructured is to use the `partition` function. If you use `partition` function, `unstructured` will detect the file type and route it to the appropriate file-specific partitioning function. If you are using the `partition` function, you may need to install additional dependencies per doc type.
For example, to install docx dependencies you need to run `pip install "unstructured[docx]"`.
See our  [installation guide](https://docs.unstructured.io/open-source/installation/full-installation) for more details.

```python
from unstructured.partition.auto import partition

elements = partition("example-docs/layout-parser-paper.pdf")
```

Run `print("\n\n".join([str(el) for el in elements]))` to get a string representation of the
output, which looks like:

```

LayoutParser : A Uniﬁed Toolkit for Deep Learning Based Document Image Analysis

Zejiang Shen 1 ( (cid:0) ), Ruochen Zhang 2 , Melissa Dell 3 , Benjamin Charles Ge
... [TRUNCATED]
```

### File: scripts\performance\README.md
```md
# Performance
This is a collection of tools helpful for inspecting and tracking performance of the Unstructured library.

The benchmarking script allows a user to track performance time to partitioning results against a fixed set of test documents and store those results with indication of architecture, instance type, and git hash, in S3.

The profiling script allows a user to inspect how time time and memory are spent across called functions when performing partitioning on a given document.

## Install
Benchmarking requires no additional dependencies and should work without any initial setup.
Profiling has a few dependencies which can be installed with:

```bash
pip install -r scripts/performance/requirements.txt
npm install -g speedscope
```

The second dependency `speedscope` provides a tool to view profiling results from `py-spy` locally. Alternatively you can also drop the profile result `*.speedscope` into https://www.speedscope.app/ to view the results online.

## Run
### Benchmark
Export / assign desired environment variable settings:
- DOCKER_TEST: Set to true to run benchmark inside a Docker container (default: false)
- NUM_ITERATIONS: Number of iterations for benchmark (e.g., 100) (default: 3)
- INSTANCE_TYPE: Type of benchmark instance (e.g., "c5.xlarge") (default: unspecified)
- PUBLISH_RESULTS: Set to true to publish results to S3 bucket (default: false)
-
Usage: `./scripts/performance/benchmark.sh`

### Profile

Export / assign desired environment variable settings:
- DOCKER_TEST: Set to true to run profiling inside a Docker container (default: false)

Usage:

**on Linux**: `./scripts/performance/profile.sh`

**on macOS**: `sudo -E ./scripts/performance/profile.sh`; `py-spy` requires su to run on macOS

- Run the script and choose the profiling mode: 'run' or 'view'.
- In the 'run' mode, you can profile custom files or select existing test files.
- In the 'view' mode, you can view previously generated profiling results.
- The script supports time profiling with cProfile and memory profiling with memray.
- Users can choose different visualization options such as flamegraphs, tables, trees, summaries, and statistics.
- Test documents are synced from an S3 bucket to a local directory before running the profiles

```

### File: scripts\performance\requirements.txt
```txt
flameprof>=0.4
memray>=1.7.0
snakeviz>=2.2.0
py-spy>=0.3.14

```

### File: .grype.yaml
```yaml
ignore:
  - vulnerability: CVE-2024-11053

```

### File: .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: "v4.3.0"
    hooks:
      - id: check-added-large-files
      - id: check-toml
      - id: check-yaml
      - id: check-json
      - id: check-xml
      - id: end-of-file-fixer
        exclude: \.json$
        files: \.py$
      - id: trailing-whitespace
      - id: mixed-line-ending

  - repo: https://github.com/psf/black
    rev: 24.2.0
    hooks:
      - id: black
        args: ["--line-length=100"]
        language_version: python3

  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.2.1
    hooks:
      - id: ruff
        args:
          ["--fix"]

  - repo: https://github.com/pycqa/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        language_version: python3

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
support@unstructured.io.
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

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
## Contributing to Unstructured

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](code_of_conduct.md)

👍🎉 First off, thank you for taking the time to contribute! 🎉👍

The following is a set of guidelines for contributing to the open source ecosystem of preprocessing pipeline APIs and supporting libraries hosted [here](https://github.com/Unstructured-IO).

This is meant to help the review process go smoothly, save the reviewer(s) time in catching common issues, and avoid submitting PRs that will be rejected by the CI.

In some cases it's convenient to put up a PR that's not ready for final review. This is fine (and under those circumstances it's not necessary to go through this checklist), but the PR should be put in draft mode so everyone knows it's not ready for review. 

### How to Contribute?

If you want to contribute, start working through the Unstructured codebase, navigate to the Github "issues" tab and start looking through interesting issues. If you are not sure of where to start, then start by trying one of the smaller/easier issues here i.e. issues with the "good first issue" label and then take a look at the issues with the "contributions welcome" label. These are issues that we believe are particularly well suited for outside contributions, often because we probably won't get to them right now. If you decide to start on an issue, leave a comment so that other people know that you're working on it. If you want to help out, but not alone, use the issue comment thread to coordinate.


## Pull-Request Checklist

The following is a list of tasks to be completed before submitting a pull request for final review.

### Before creating PR:

1. Follow coding best practices
    1. [ ] Make sure all new classes/functions/methods have docstrings.
    1. [ ] Make sure all new functions/methods have type hints (optional for tests).
    1. [ ] Make sure all new functions/methods have associated tests.
    1. [ ] Update `CHANGELOG.md` and `__version__.py` if the core code has changed
<br/><br/>
1. Ensure environment is consistent
    1. [ ] Update dependencies in `.in` files if needed (pay special attention to whether the current PR depends on changes to internal repos that are not packaged - if so the commit needs to be bumped).
    1. [ ] If dependencies have changed, recompile dependencies with `make pip-compile`.
    1. [ ] Make sure local virtual environment matches what CI will see - reinstall internal/external dependencies as needed.\
<sub>Follow the [virtualenv install instructions](https://github.com/Unstructured-IO/community#mac--homebrew) if you are unsure about working with virtual environments.
<br/><br/>    
1. Run tests and checks locally
    1. [ ] Run tests locally with `make test`. Some repositories have supplemental tests with targets like `make test-integration` or `make test-sample-docs`. If applicable, run these as well. Try to make sure all tests are passing before submitting the PR, unless you are submitting in draft mode.
    1. [ ] Run typing, linting, and formatting checks with `make check`. Some repositories have supplemental checks with targets like `make check-scripts` or `make check-notebooks`. If applicable, run these as well. Try to make sure all checks are passing before submitting the PR, unless you are submitting in draft mode.
<br/><br/>    
1. Ensure code is clean
    1. [ ] Remove all debugging artifacts.
    1. [ ] Remove commented out code. 
    1. [ ] For actual comments, note that our typical format is `# NOTE(<username>): <comment>`
    1. [ ] Double check everything has been committed and pushed, recommended that local feature branch is clean.
    
### PR Guidelines:

1. [ ] PR title should follow [conventional commit](https://www.conventionalcommits.org/en/v1.0.0/) standards.
      
1. [ ] PR description should give enough detail that the reviewer knows what they reviewing - sometimes a copy-paste of the added `CHANGELOG.md` items is enough, sometimes more detail is needed.

1. [ ] If applicable, add a testing section to the PR description that recommends steps a reviewer can take to verify the changes, e.g. a snippet of code they can run locally.

### License

Unstructured open source projects are licensed under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0).

Include a license at the top of new `setup.py` files:

- [Python license example](https://github.com/Unstructured-IO/unstructured/blob/main/setup.py)


## Conventions

For pull requests, our convention is to squash and merge. For PR titles, we use [conventional commit](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/#conventional-commits) messages. The format should look like 

- `<type>: <description>`.

For example, if the PR addresses a new feature, the PR title should look like: 

- `feat: Implements exciting new feature`. 

For feature branches, the naming convention is:

- `<username>/<description>`. 

For the commit above, coming from the user called `contributor` the branch name would look like: 

- `contributor/exciting-new-feature`.

Here is a list of some of the most common possible commit types:

- `feat` – a new feature is introduced with the changes
- `fix` – a bug fix has occurred
- `chore` – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
- `refactor` – refactored code that neither fixes a bug nor adds a feature
- `docs` – updates to documentation such as a the README or other markdown files

### Why should you write better commit messages?

By writing good commits, you are simply future-proofing yourself. You could save yourself and/or coworkers hours of digging around while troubleshooting by providing that helpful description 🙂. 

The extra time it takes to write a thoughtful commit message as a letter to your potential future self is extremely worthwhile. On large scale projects, documentation is imperative for maintenance.

Collaboration and communication are of utmost importance within engineering teams. The Git commit message is a prime example of this. I highly suggest setting up a convention for commit messages on your team if you do not already have one in place.


## Code of Conduct

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Enforcement

Please report unacceptable behavior to support@unstructured.io. All complaints will be reviewed and investigated and will result in a response that is deemed necessary and appropriate to the circumstances. The project team is obligated to maintain confidentiality with regard to the reporter of an incident. Further details of specific enforcement policies may be posted separately.

Project maintainers who do not follow or enforce the Code of Conduct in good faith may face temporary or permanent repercussions as determined by other members of the project's leadership.

Thank you! 🤗

The Unstructured Team


## Learn more

| Section | Description |
|-|-|
| [Company Website](https://unstructured.io) | Unstructured.io product and company info |
| [Documentation](https://docs.unstructured.io/) | Full API documentation |
| [Working with Pull Requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) | About pull requests |
| [Code of Conduct](https://www.contributor-covenant.org/version/1/4/code-of-conduct/) | Contributor Covenant Code Of Conduct |
| [Conventional Commits](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/) | How to write better git commit messages |
| [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) | Lightweight convention on top of commit messages |
| [First Contributions](https://github.com/firstcontributions/first-contributions/blob/main/README.md) | Beginners' guide to make their first contribution! |


## Contributing Guides

If you're stumped 😓, here are some good examples of contribution guidelines:

- The GitHub Docs [contribution guidelines](https://github.com/github/docs/blob/main/CONTRIBUTING.md).
- The Ruby on Rails [contribution guidelines](https://github.com/rails/rails/blob/main/CONTRIBUTING.md).
- The Open Government [contribution guidelines](https://github.com/opengovernment/opengovernment/blob/master/CONTRIBUTING.md).
- The MMOCR [contribution guidelines](https://mmocr.readthedocs.io/en/dev-1.x/notes/contribution_guide.html).
- The HuggingFace [contribution guidelines](https://huggingface2.notion.site/Contribution-Guide-19411c29298644df8e9656af45a7686d).

```

### File: LICENSE.md
```md
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2022 Unstructured Technologies, Inc

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

```

### File: scripts\check-licenses.sh
```sh
#!/usr/bin/env bash

set -euo pipefail

# Allowed license families (partial-match against the License metadata field).
# Covers the standard permissive + weak-copyleft licenses the project accepts.
# Build the semicolon-separated allowlist for --partial-match.
# Each entry is matched as a case-insensitive substring against the package's
# License metadata field. Order does not matter.
ALLOWED="Apache;\
BSD;\
MIT;\
ISC;\
MPL;\
Mozilla;\
LGPL;\
GNU Lesser General Public License;\
GNU Library or Lesser General Public License;\
GNU General Public License v2;\
PSF;\
Python Software Foundation;\
Unlicense;\
HPND;\
Historical Permission Notice and Disclaimer;\
CNRI-Python;\
Python-2.0"

# Packages whose license metadata is missing, non-standard, or proprietary but
# known-good for this project. Each has been manually verified against the
# upstream source repository.
IGNORED_PACKAGES=(
  # Metadata missing -- verified permissive on GitHub
  arro3-core     # MIT / Apache-2.0 (geoarrow/geoarrow-rs)
  chroma-hnswlib # Apache-2.0 (chroma-core/hnswlib)
  google-crc32c  # Apache-2.0 (googleapis/python-crc32c)
  iopath         # MIT (facebookresearch/iopath)
  pypdfium2      # BSD-3-Clause (PDFium/PDFium)
  sentencepiece  # Apache-2.0 (google/sentencepiece)
  voyageai       # MIT (voyage-ai/voyageai-python)

  # Permissive but non-standard classifier
  lmdb # OpenLDAP Public License (BSD-style, jnwatson/py-lmdb)
  pykx # KDB+ proprietary (KxSystems/pykx, transitive dep of kdbai-client)

  # NVIDIA CUDA runtime libs (proprietary, torch transitive dependencies)
  cuda-bindings
  nvidia-cublas-cu12
  nvidia-cuda-cupti-cu12
  nvidia-cuda-nvrtc-cu12
  nvidia-cuda-runtime-cu12
  nvidia-cudnn-cu12
  nvidia-cufft-cu12
  nvidia-cufile-cu12
  nvidia-curand-cu12
  nvidia-cusolver-cu12
  nvidia-cusparse-cu12
  nvidia-cusparselt-cu12
  nvidia-nccl-cu12
  nvidia-nvjitlink-cu12
  nvidia-nvshmem-cu12
  nvidia-nvtx-cu12
)

echo "Checking licenses for installed packages..."
uv run pip-licenses \
  --partial-match \
  --allow-only="$ALLOWED" \
  --ignore-packages "${IGNORED_PACKAGES[@]}"
EXIT_CODE=$?

if [ "$EXIT_CODE" -eq 0 ]; then
  echo "All dependencies have authorized licenses."
else
  echo "There are dependencies with unauthorized or unknown licenses."
  exit 1
fi

```

### File: scripts\check-new-release-version.sh
```sh
#!/usr/bin/env bash

set -eux

# Function to check if the current version is a non-dev version
function is_non_dev_version {
  local VERSION="$1"
  [[ "$VERSION" != *"-dev"* ]]
}

# Function to get the version from the current main branch
function get_main_branch_version {
  local VERSION
  git fetch origin main
  VERSION=$(git show origin/main:unstructured/__version__.py | grep -o -m 1 -E "(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-[a-zA-Z0-9.-]+)?")
  echo "$VERSION"
}

# Get the current version from the file
CURRENT_VERSION=$(grep -o -m 1 -E "(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(-dev[0-9]+)?" "unstructured/__version__.py")

# Check if the current version is a non-dev version and not matching the main version
if is_non_dev_version "$CURRENT_VERSION" && [ "$(get_main_branch_version)" != "$CURRENT_VERSION" ]; then
  echo "New release version: $CURRENT_VERSION"
fi

```

### File: scripts\collect_env.py
```py
import platform
import shutil
import subprocess

import pkg_resources

from unstructured.utils import dependency_exists


def command_exists(command):
    """
    Check if a command exists in the system

    Args:
        command (str): The command to check

    Returns:
        bool: True if command exists, False otherwise
    """
    return shutil.which(command) is not None


def get_python_version():
    """
    Get the current Python version

    Returns:
        str: The current Python version
    """
    return platform.python_version()


def get_os_version():
    """
    Get the current operating system version

    Returns:
        str: The current operating system version
    """
    return platform.platform()


def is_python_package_installed(package_name: str):
    """
    Check if a Python package is installed

    Args:
        package_name (str): The Python package to check

    Returns:
        bool: True if package is installed, False otherwise
    """
    result = subprocess.run(
        ["pip", "list"],
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    )

    return any(line.lower().startswith(package_name.lower()) for line in result.stdout.splitlines())


def is_brew_package_installed(package_name: str):
    """
    Check if a Homebrew package is installed

    Args:
        package_name (str): The package to check

    Returns:
        bool: True if package is installed, False otherwise
    """
    if not command_exists("brew"):
        return False

    result = subprocess.run(
        ["brew", "list"],
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    )

    for line in result.stdout.splitlines():
        if line.lower().startswith(package_name.lower()):
            return True

    result = subprocess.run(
        ["brew", "list", "--cask"],
        stdout=subprocess.PIPE,
        text=True,
        check=True,
    )

    return any(line.lower().startswith(package_name.lower()) for line in result.stdout.splitlines())


def get_python_package_version(package_name):
    """
    Get the version of a Python package

    Args:
        package_name (str): The Python package to check

    Returns:
        str: Version of the package, None if package is not installed
    """
    try:
        return pkg_resources.get_distribution(package_name).version
    except pkg_resources.DistributionNotFound:
        return None


def get_brew_package_version(package_name):
    """
    Get the version of a Homebrew package

    Args:
        package_name (str): The package to check

    Returns:
        str: Version of the package, None if package is not installed
    """
    if not command_exists("brew"):
        return None

    result = subprocess.run(
        ["brew", "info", package_name],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        text=True,
    )

    for line in result.stdout.splitlines():
        return line

    return None


def get_libmagic_version():
    """
    Get the version of libmagic

    Returns:
        str: Version of libmagic, None if libmagic is not installed
    """
    result = subprocess.run(
        ["file", "--version", "--headless"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    return result.stdout.strip()


def get_libreoffice_version():
    """
    Get the version of LibreOffice

    Returns:
        str: Version of LibreOffice, None if LibreOffice is not installed
    """
    result = subprocess.run(
        ["libreoffice", "--version", "--headless"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    return result.stdout.strip()


def main():
    """
    The main function to run all checks
    """
    print("OS version: ", get_os_version())
    print("Python version: ", get_python_version())

    if dependency_exists("unstructured"):
        print("unstructured version: ", get_python_package_version("unstructured"))
    else:
        print("unstructured is not installed")

    if dependency_exists("unstructured_inference"):
        print(
            "unstructured-inference version: ",
            get_python_package_version("unstructured-inference"),
        )
    else:
        print("unstructured-inference is not installed")

    if dependency_exists("pytesseract"):
        print(
            "pytesseract version: ",
            get_python_package_version("pytesseract"),
        )
    else:
        print("pytesseract is not installed")

    if dependency_exists("torch"):
        print("Torch version: ", get_python_package_version("torch"))
    else:
        print("Torch is not installed")

    if dependency_exists("detectron2"):
        print("Detectron2 version: ", get_python_package_version("detectron2"))
    else:
        print("Detectron2 is not installed")

    if is_python_package_installed("paddlepaddle") or is_python_package_installed(
        "paddleocr",
    ):
        print(
            "PaddleOCR version: ",
            get_python_package_version("paddlepaddle") or get_python_package_version("paddleocr"),
        )
    else:
        print("PaddleOCR is not installed")

    if is_brew_package_installed("libmagic"):
        print("Libmagic version: ", get_brew_package_version("libmagic"))
    else:
        libmagic_version = get_libmagic_version()
        if libmagic_version:
            print(f"Libmagic version: {libmagic_version}")
        else:
            print("Libmagic is not installed")

    if platform.system() != "Windows":
        if is_brew_package_installed("libreoffice"):
            print("LibreOffice version: ", get_brew_package_version("libreoffice"))
        else:
            libreoffice_version = get_libreoffice_version()
            if libreoffice_version:
                print("LibreOffice version: ", libreoffice_version)
            else:
                print("LibreOffice is not installed")


if __name__ == "__main__":
    main()

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
