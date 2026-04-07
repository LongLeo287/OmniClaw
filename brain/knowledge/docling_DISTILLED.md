---
id: docling
type: knowledge
owner: OA_Triage
---
# docling
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <a href="https://github.com/docling-project/docling">
    <img loading="lazy" alt="Docling" src="https://github.com/docling-project/docling/raw/main/docs/assets/docling_processing.png" width="100%"/>
  </a>
</p>

# Docling

<p align="center">
  <a href="https://trendshift.io/repositories/12132" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12132" alt="DS4SD%2Fdocling | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</p>

[![arXiv](https://img.shields.io/badge/arXiv-2408.09869-b31b1b.svg)](https://arxiv.org/abs/2408.09869)
[![Docs](https://img.shields.io/badge/docs-live-brightgreen)](https://docling-project.github.io/docling/)
[![PyPI version](https://img.shields.io/pypi/v/docling)](https://pypi.org/project/docling/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/docling)](https://pypi.org/project/docling/)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Pydantic v2](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/pydantic/pydantic/main/docs/badge/v2.json)](https://pydantic.dev)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![License MIT](https://img.shields.io/github/license/docling-project/docling)](https://opensource.org/licenses/MIT)
[![PyPI Downloads](https://static.pepy.tech/badge/docling/month)](https://pepy.tech/projects/docling)
[![Docling Actor](https://apify.com/actor-badge?actor=vancura/docling?fpr=docling)](https://apify.com/vancura/docling)
[![Chat with Dosu](https://dosu.dev/dosu-chat-badge.svg)](https://app.dosu.dev/097760a8-135e-4789-8234-90c8837d7f1c/ask?utm_source=github)
[![Discord](https://img.shields.io/discord/1399788921306746971?color=6A7EC2&logo=discord&logoColor=ffffff)](https://docling.ai/discord)
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/10101/badge)](https://www.bestpractices.dev/projects/10101)
[![LF AI & Data](https://img.shields.io/badge/LF%20AI%20%26%20Data-003778?logo=linuxfoundation&logoColor=fff&color=0094ff&labelColor=003778)](https://lfaidata.foundation/projects/)

Docling simplifies document processing, parsing diverse formats — including advanced PDF understanding — and providing seamless integrations with the gen AI ecosystem.

## Features

* 🗂️ Parsing of [multiple document formats][supported_formats] incl. PDF, DOCX, PPTX, XLSX, HTML, WAV, MP3, WebVTT, images (PNG, TIFF, JPEG, ...), LaTeX, plain text, and more
* 📑 Advanced PDF understanding incl. page layout, reading order, table structure, code, formulas, image classification, and more
* 🧬 Unified, expressive [DoclingDocument][docling_document] representation format
* ↪️ Various [export formats][supported_formats] and options, including Markdown, HTML, WebVTT, [DocTags](https://arxiv.org/abs/2503.11576) and lossless JSON
* 📜 Support of several application-specifc XML schemas incl. [USPTO](https://www.uspto.gov/patents) patents, [JATS](https://jats.nlm.nih.gov/) articles, and [XBRL](https://www.xbrl.org/) financial reports.
* 🔒 Local execution capabilities for sensitive data and air-gapped environments
* 🤖 Plug-and-play [integrations][integrations] incl. LangChain, LlamaIndex, Crew AI & Haystack for agentic AI
* 🔍 Extensive OCR support for scanned PDFs and images
* 👓 Support of several Visual Language Models ([GraniteDocling](https://huggingface.co/ibm-granite/granite-docling-258M))
* 🎙️ Audio support with Automatic Speech Recognition (ASR) models
* 🔌 Connect to any agent using the [MCP server](https://docling-project.github.io/docling/usage/mcp/)
* 💻 Simple and convenient CLI

### What's new
* 📤 Structured [information extraction][extraction] \[🧪 beta\]
* 📑 New layout model (**Heron**) by default, for faster PDF parsing
* 🔌 [MCP server](https://docling-project.github.io/docling/usage/mcp/) for agentic applications
* 💼 Parsing of XBRL (eXtensible Business Reporting Language) documents for financial reports
* 💬 Parsing of WebVTT (Web Video Text Tracks) files and export to WebVTT format
* 💬 Parsing of LaTeX files
* 📝 Parsing of plain-text files (`.txt`, `.text`) and Markdown supersets (`.qmd`, `.Rmd`)

### Coming soon

* 📝 Metadata extraction, including title, authors, references & language
* 📝 Chart understanding (Barchart, Piechart, LinePlot, etc)
* 📝 Complex chemistry understanding (Molecular structures)

## Installation

To use Docling, simply install `docling` from your package manager, e.g. pip:
```bash
pip install docling
```

> **Note:** Python 3.9 support was dropped in docling version 2.70.0. Please use Python 3.10 or higher.

Works on macOS, Linux and Windows environments. Both x86_64 and arm64 architectures.

More [detailed installation instructions](https://docling-project.github.io/docling/installation/) are available in the docs.

## Getting started

To convert individual documents with python, use `convert()`, for example:

```python
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "## Docling Technical Report[...]"
```

More [advanced usage options](https://docling-project.github.io/docling/usage/advanced_options/) are available in
the docs.

## CLI

Docling has a built-in CLI to run conversions.

```bash
docling https://arxiv.org/pdf/2206.01062
```

You can also use 🥚[GraniteDocling](https://huggingface.co/ibm-granite/granite-docling-258M) and other VLMs via Docling CLI:
```bash
docling --pipeline vlm --vlm-model granite_docling https://arxiv.org/pdf/2206.01062
```
This will use MLX acceleration on supported Apple Silicon hardware.

Read more [here](https://docling-project.github.io/docling/usage/)

## Documentation

Check out Docling's [documentation](https://docling-project.github.io/docling/), for details on
installation, usage, concepts, recipes, extensions, and more.

## Examples

Go hands-on with our [examples](https://docling-project.github.io/docling/examples/),
demonstrating how to address different application use cases with Docling.

## Integrations

To further accelerate your AI application development, check out Docling's native
[integrations](https://docling-project.github.io/docling/integrations/) with popular frameworks
and tools.

## Get help and support

Please feel free to connect with us using the [discussion section](https://github.com/docling-project/docling/discussions).

## Technical report

For more details on Docling's inner workings, check out the [Docling Technical Report](https://arxiv.org/abs/2408.09869).

## Contributing

Please read [Contributing to Docling](https://github.com/docling-project/docling/blob/main/CONTRIBUTING.md) for details.

## References

If you use Docling in your projects, please consider citing the following:

```bib
@techreport{Docling,
  author = {Deep Search Team},
  month = {8},
  title = {Docling Technical Report},
  url = {https://arxiv.org/abs/2408.09869},
  eprint = {2408.09869},
  doi = {10.48550/arXiv.2408.09869},
  version = {1.0.0},
  year = {2024}
}
```

## License

The Docling codebase is under MIT license.
For individual model usage, please refer to the model licenses found in the original packages.

## LF AI & Data

Docling is hosted as a project in the [LF AI & Data Foundation](https://lfaidata.foundation/projects/).

### IBM ❤️ Open Source AI

The project was started by the AI for knowledge team at IBM Research Zurich.

[supported_formats]: https://docling-project.github.io/docling/usage/supported_formats/
[docling_document]: https://docling-project.github.io/docling/concepts/docling_document/
[integrations]: https://docling-project.github.io/docling/integrations/
[extraction]: https://docling-project.github.io/docling/examples/extraction/

```

### File: .actor\README.md
```md
# Docling Actor on Apify

[![Docling Actor](https://apify.com/actor-badge?actor=vancura/docling?fpr=docling)](https://apify.com/vancura/docling)

This Actor (specification v1) wraps the [Docling project](https://github.com/docling-project/docling) to provide serverless document processing in the cloud. It can process complex documents (PDF, DOCX, images) and convert them into structured formats (Markdown, JSON, HTML, Text, or DocTags) with optional OCR support.

## What are Actors?

[Actors](https://docs.apify.com/platform/actors?fpr=docling) are serverless microservices running on the [Apify Platform](https://apify.com/?fpr=docling). They are based on the [Actor SDK](https://docs.apify.com/sdk/js?fpr=docling) and can be found in the [Apify Store](https://apify.com/store?fpr=docling). Learn more about Actors in the [Apify Whitepaper](https://whitepaper.actor?fpr=docling).

## Table of Contents

1. [Features](#features)
2. [Usage](#usage)
3. [Input Parameters](#input-parameters)
4. [Output](#output)
5. [Performance and Resources](#performance-and-resources)
6. [Troubleshooting](#troubleshooting)
7. [Local Development](#local-development)
8. [Architecture](#architecture)
9. [License](#license)
10. [Acknowledgments](#acknowledgments)
11. [Security Considerations](#security-considerations)

## Features

- Leverages the official docling-serve-cpu Docker image for efficient document processing
- Processes multiple document formats:
  - PDF documents (scanned or digital)
  - Microsoft Office files (DOCX, XLSX, PPTX)
  - Images (PNG, JPG, TIFF)
  - Other text-based formats
- Provides OCR capabilities for scanned documents
- Exports to multiple formats:
  - Markdown
  - JSON
  - HTML
  - Plain Text
  - DocTags (structured format)
- No local setup needed—just provide input via a simple JSON config

## Usage

### Using Apify Console

1. Go to the Apify Actor page.
2. Click "Run".
3. In the input form, fill in:
   - The URL of the document.
   - Output format (`md`, `json`, `html`, `text`, or `doctags`).
   - OCR boolean toggle.
4. The Actor will run and produce its outputs in the default key-value store under the key `OUTPUT`.

### Using Apify API

```bash
curl --request POST \
  --url "https://api.apify.com/v2/acts/vancura~docling/run" \
  --header 'Content-Type: application/json' \
  --header 'Authorization: Bearer YOUR_API_TOKEN' \
  --data '{
  "options": {
    "to_formats": ["md", "json", "html", "text", "doctags"]
  },
  "http_sources": [
    {"url": "https://vancura.dev/assets/actor-test/facial-hairstyles-and-filtering-facepiece-respirators.pdf"},
    {"url": "https://arxiv.org/pdf/2408.09869"}
  ]
}'
```

### Using Apify CLI

```bash
apify call vancura/docling --input='{
  "options": {
    "to_formats": ["md", "json", "html", "text", "doctags"]
  },
  "http_sources": [
    {"url": "https://vancura.dev/assets/actor-test/facial-hairstyles-and-filtering-facepiece-respirators.pdf"},
    {"url": "https://arxiv.org/pdf/2408.09869"}
  ]
}'
```

## Input Parameters

The Actor accepts a JSON schema matching the file `.actor/input_schema.json`. Below is a summary of the fields:

| Field          | Type    | Required | Default  | Description                                                                   |
|----------------|---------|----------|----------|-------------------------------------------------------------------------------|
| `http_sources` | object  | Yes      | None     | https://github.com/DS4SD/docling-serve?tab=readme-ov-file#url-endpoint        |
| `options`      | object  | No       | None     | https://github.com/DS4SD/docling-serve?tab=readme-ov-file#common-parameters   |

### Example Input

```json
{
  "options": {
    "to_formats": ["md", "json", "html", "text", "doctags"]
  },
  "http_sources": [
    {"url": "https://vancura.dev/assets/actor-test/facial-hairstyles-and-filtering-facepiece-respirators.pdf"},
    {"url": "https://arxiv.org/pdf/2408.09869"}
  ]
}
```

## Output

The Actor provides three types of outputs:

1. **Processed Documents in a ZIP** - The Actor will provide the direct URL to your result in the run log, looking like:

   ```text
   You can find your results at: 'https://api.apify.com/v2/key-value-stores/[YOUR_STORE_ID]/records/OUTPUT'
   ```

2. **Processing Log** - Available in the key-value store as `DOCLING_LOG`

3. **Dataset Record** - Contains processing metadata with:
   - Direct link to the processed output zip file
   - Processing status

You can access the results in several ways:

1. **Direct URL** (shown in Actor run logs):

```text
https://api.apify.com/v2/key-value-stores/[STORE_ID]/records/OUTPUT
```

2. **Programmatically** via Apify CLI:

```bash
apify key-value-stores get-value OUTPUT
```

3. **Dataset** - Check the "Dataset" tab in the Actor run details to see processing metadata

### Example Outputs

#### Markdown (md)

```markdown
# Document Title

## Section 1
Content of section 1...

## Section 2
Content of section 2...
```

#### JSON

```json
{
    "title": "Document Title",
    "sections": [
        {
            "level": 1,
            "title": "Section 1",
            "content": "Content of section 1..."
        }
    ]
}
```

#### HTML

```html
<h1>Document Title</h1>
<h2>Section 1</h2>
<p>Content of section 1...</p>
```

### Processing Logs (`DOCLING_LOG`)

The Actor maintains detailed processing logs including:

- API request and response details
- Processing steps and timing
- Error messages and stack traces
- Input validation results

Access logs via:

```bash
apify key-value-stores get-record DOCLING_LOG
```

## Performance and Resources

- **Docker Image Size**: ~4GB
- **Memory Requirements**:
  - Minimum: 2 GB RAM
  - Recommended: 4 GB RAM for large or complex documents
- **Processing Time**:
  - Simple documents: 15-30 seconds
  - Complex PDFs with OCR: 1-3 minutes
  - Large documents (100+ pages): 3-10 minutes

## Troubleshooting

Common issues and solutions:

1. **Document URL Not Accessible**
   - Ensure the URL is publicly accessible
   - Check if the document requires authentication
   - Verify the URL leads directly to the document

2. **OCR Processing Fails**
   - Verify the document is not password-protected
   - Check if the image quality is sufficient
   - Try processing with OCR disabled

3. **API Response Issues**
   - Check the logs for detailed error messages
   - Ensure the document format is supported
   - Verify the URL is correctly formatted

4. **Output Format Issues**
   - Verify the output format is supported
   - Check if the document structure is compatible
   - Review the `DOCLING_LOG` for specific errors

### Error Handling

The Actor implements comprehensive error handling:

- Detailed error messages in `DOCLING_LOG`
- Proper exit codes for different failure scenarios
- Automatic cleanup on failure
- Dataset records with processing status

## Local Development

If you wish to develop or modify this Actor locally:

1. Clone the repository.
2. Ensure Docker is installed.
3. The Actor files are located in the `.actor` directory:
   - `Dockerfile` - Defines the container environment
   - `actor.json` - Actor configuration and metadata
   - `actor.sh` - Main execution script that starts the docling-serve API and orchestrates document processing
   - `input_schema.json` - Input parameter definitions
   - `dataset_schema.json` - Dataset output format definition
   - `CHANGELOG.md` - Change log documenting all notable changes
   - `README.md` - This documentation
4. Run the Actor locally using:

   ```bash
   apify run
   ```

### Actor Structure

```text
.actor/
├── Dockerfile           # Container definition
├── actor.json           # Actor metadata
├── actor.sh             # Execution script (also starts docling-serve API)
├── input_schema.json    # Input parameters
├── dataset_schema.json  # Dataset output format definition
├── docling_processor.py # Python script for API communication
├── CHANGELOG.md         # Version history and changes
└── README.md            # This documentation
```

## Architecture

This Actor uses a lightweight architecture based on the official `quay.io/ds4sd/docling-serve-cpu` Docker image:

- **Base Image**: `quay.io/ds4sd/docling-serve-cpu:latest` (~4GB)
- **Multi-Stage Build**: Uses a multi-stage Docker build to include only necessary tools
- **API Communication**: Uses the RESTful API provided by docling-serve
- **Request Flow**:
  1. The actor script starts the docling-serve API on port 5001
  2. Performs health checks to ensure the API is running
  3. Processes the input parameters
  4. Creates a JSON payload for the docling-serve API with proper format:
     ```json
     {
       "options": {
         "to_formats": ["md"],
         "do_ocr": true
       },
       "http_sources": [{"url": "https://example.com/document.pdf"}]
     }
     ```
  5. Makes a POST request to the `/v1alpha/convert/source` endpoint
  6. Processes the response and stores it in the key-value store
- **Dependencies**:
  - Node.js for Apify CLI
  - Essential tools (curl, jq, etc.) copied from build stage
- **Security**: Runs as a non-root user for enhanced security

## License

This wrapper project is under the MIT License, matching the original Docling license. See [LICENSE](../LICENSE) for details.

## Acknowledgments

- [Docling](https://ds4sd.github.io/docling/) and [docling-serve-cpu](https://quay.io/repository/ds4sd/docling-serve-cpu) by IBM
- [Apify](https://apify.com/?fpr=docling) for the serverless actor environment

## Security Considerations

- Actor runs under a non-root user for enhanced security
- Input URLs are validated before processing
- Temporary files are securely managed and cleaned up
- Process isolation through Docker containerization
- Secure handling of processing artifacts

```

### File: .pre-commit-config.yaml
```yaml
fail_fast: true
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.11.5
    hooks:
      # Run the Ruff formatter.
      - id: ruff-format
        name: "Ruff formatter"
        args: [--config=pyproject.toml]
        files: '^(docling|tests|docs/examples).*\.(py|ipynb)$'
      # Run the Ruff linter.
      - id: ruff
        name: "Ruff linter"
        args: [--exit-non-zero-on-fix, --fix, --config=pyproject.toml]
        files: '^(docling|tests|docs/examples).*\.(py|ipynb)$'
  - repo: local
    hooks:
      - id: mypy
        name: MyPy
        entry: uv run --no-sync mypy docling
        pass_filenames: false
        language: system
        files: '\.py$'
  - repo: https://github.com/astral-sh/uv-pre-commit
    rev: 0.8.3
    hooks:
      - id: uv-lock

```

### File: CHANGELOG.md
```md
## [v2.84.0](https://github.com/docling-project/docling/releases/tag/v2.84.0) - 2026-04-01

### Feature

* Glm ocr ([#3146](https://github.com/docling-project/docling/issues/3146)) ([`a9265d8`](https://github.com/docling-project/docling/commit/a9265d854a195993d2e63bfc8c4bb2f76be7f9d9))
* Switch to the latest version of DocumentFigureClassifier model v2.5 ([#3171](https://github.com/docling-project/docling/issues/3171)) ([`d046390`](https://github.com/docling-project/docling/commit/d046390bf4bff2c538cb33eebb03dce56d122d37))
* Remove the deprecation of extraction ([#3220](https://github.com/docling-project/docling/issues/3220)) ([`e9a39e8`](https://github.com/docling-project/docling/commit/e9a39e872048f31b57402926ae3a40c05b7d24d0))

## [v2.83.0](https://github.com/docling-project/docling/releases/tag/v2.83.0) - 2026-03-31

### Feature

* Upgrade to transformers v5 ([#3200](https://github.com/docling-project/docling/issues/3200)) ([`d2c6357`](https://github.com/docling-project/docling/commit/d2c6357982d79629440919188d73bda18bc678c8))
* OCR model for remote KServe v2 API ([#3189](https://github.com/docling-project/docling/issues/3189)) ([`8522b00`](https://github.com/docling-project/docling/commit/8522b00146a2217760ad1944934926ed0e9f5d39))

### Fix

* **pdf:** Propagate hyperlinks to DoclingDocument text items ([#3131](https://github.com/docling-project/docling/issues/3131)) ([`524edcc`](https://github.com/docling-project/docling/commit/524edcce73869a87b6ccf73bc16324742bd36648))
* **xlsx:** Guard last-row bounds in Excel table scan ([#3197](https://github.com/docling-project/docling/issues/3197)) ([`85ac377`](https://github.com/docling-project/docling/commit/85ac3775148494e2767bbe17ce8d7a28a8baf6b6))
* Parse LaTeX macros in multicolumn/multirow table cells ([#3204](https://github.com/docling-project/docling/issues/3204)) ([`89c68f8`](https://github.com/docling-project/docling/commit/89c68f8ec373c6012c963a39ea70f5c122e0e779))
* Handle empty CSV file without crashing ([#3196](https://github.com/docling-project/docling/issues/3196)) ([`f283484`](https://github.com/docling-project/docling/commit/f2834848aeaa63ac51f4968e1665b6b8e77b90e4))

### Documentation

* Add line-based chunker documentation and examples ([#3210](https://github.com/docling-project/docling/issues/3210)) ([`3a64f41`](https://github.com/docling-project/docling/commit/3a64f41af86c90af71d6befe619f9f5a12a26e5f))

## [v2.82.0](https://github.com/docling-project/docling/releases/tag/v2.82.0) - 2026-03-25

### Feature

* Implementation of HTML backend with headless browser ([#2969](https://github.com/docling-project/docling/issues/2969)) ([`1c74a9b`](https://github.com/docling-project/docling/commit/1c74a9b9c7c2019b85abef8f0f94381a83b721df))

### Fix

* **omml:** Correct LaTeX output for fractions, math operators, and functions ([#3122](https://github.com/docling-project/docling/issues/3122)) ([`e36125b`](https://github.com/docling-project/docling/commit/e36125ba2ddfbe584fc752e6dc7ca0f0f8f58d87))
* Manage PDFium backend resource lifecycles to avoid SIGSEGV/SIGTRAP crashes ([#3180](https://github.com/docling-project/docling/issues/3180)) ([`a0fc3c9`](https://github.com/docling-project/docling/commit/a0fc3c9d731c29f896680b17fa6df5549e2dfc5d))
* **docx:** Split multiple OMML equations into separate formula items ([#3123](https://github.com/docling-project/docling/issues/3123)) ([`90d6dd4`](https://github.com/docling-project/docling/commit/90d6dd4e87d96167aced588249dcb2e0f47cd68f))
* Let user params override engine defaults in API VLM engine ([#3116](https://github.com/docling-project/docling/issues/3116)) ([`fdf5e20`](https://github.com/docling-project/docling/commit/fdf5e20ccd8ae85ea73effa6c743910ed295564d))
* **vlm:** Handle content_filter finish reason in API responses ([#3051](https://github.com/docling-project/docling/issues/3051)) ([`f0e3d1d`](https://github.com/docling-project/docling/commit/f0e3d1df2a086710d5c9629426595f5d54ed65aa))
* **cli:** Avoid generating images for non-image exports ([#3127](https://github.com/docling-project/docling/issues/3127)) ([`5473e07`](https://github.com/docling-project/docling/commit/5473e074505e0bd46985683800fa8f929fd53492))
* Honor picture description batching and scale options ([#3132](https://github.com/docling-project/docling/issues/3132)) ([`9abf0fd`](https://github.com/docling-project/docling/commit/9abf0fd3851429183debfb90e2a9f975c9654beb))

### Documentation

* Fix Erroneous vLLM VLM pipeline engine option params causing empty/bad responses ([#3167](https://github.com/docling-project/docling/issues/3167)) ([`fffd445`](https://github.com/docling-project/docling/commit/fffd4457892002f5668e3a37b3c7a79e36936405))

## [v2.81.0](https://github.com/docling-project/docling/releases/tag/v2.81.0) - 2026-03-20

### Feature

* Route plain-text and Quarto/R Markdown files to the Markdown backend ([#3161](https://github.com/docling-project/docling/issues/3161)) ([`96d7c7e`](https://github.com/docling-project/docling/commit/96d7c7ec79992d8dddedfafaaedb7f9bf6e14f40))

### Fix

* **docx:** Missing list items after numbered header (#2665) ([#2678](https://github.com/docling-project/docling/issues/2678)) ([`2f7c09e`](https://github.com/docling-project/docling/commit/2f7c09e0d8f07a5fa0aaf4f33bdfb1f71d3f3063))
* Avoid thread-unsafe close of pypdfium backend ([#3160](https://github.com/docling-project/docling/issues/3160)) ([`afb4bb6`](https://github.com/docling-project/docling/commit/afb4bb68023c5d8fb8dc5e39413a27678e642293))
* Handle external image relationships in MsWordDocumentBackend ([#3114](https://github.com/docling-project/docling/issues/3114)) ([`8ae0974`](https://github.com/docling-project/docling/commit/8ae0974a9d86a447f78e4950bc0a45d5eba31e98))
* Handle PermissionError for directory input on Windows CLI ([#3149](https://github.com/docling-project/docling/issues/3149)) ([`a39317a`](https://github.com/docling-project/docling/commit/a39317a147859c68bf8aef635276a23585725529))
* Avoid in-place mutation of pipeline options breaking cache key ([#3115](https://github.com/docling-project/docling/issues/3115)) ([`412af62`](https://github.com/docling-project/docling/commit/412af62135869978b7d22e1dd4ee2725623fad44))
* Preserve torch_dtype in get_engine_config and add it to CodeFormulaV2 ([#3117](https://github.com/docling-project/docling/issues/3117)) ([`53a5f80`](https://github.com/docling-project/docling/commit/53a5f80a43849d853d4e0598d3875e6aac2f88e0))
* Release image backend resources after frame extraction ([#3134](https://github.com/docling-project/docling/issues/3134)) ([`1e841eb`](https://github.com/docling-project/docling/commit/1e841ebcbd048fbfc11d63b4086539b7cd88bb77))

## [v2.80.0](https://github.com/docling-project/docling/releases/tag/v2.80.0) - 2026-03-14

### Feature

* Add the VllmCudaGraphMode ([#3125](https://github.com/docling-project/docling/issues/3125)) ([`f950679`](https://github.com/docling-project/docling/commit/f950679f60ab6b1a9b057e7131fc8c8334e6e62e))

## [v2.79.0](https://github.com/docling-project/docling/releases/tag/v2.79.0) - 2026-03-12

### Feature

* Add fact metadata and linkbase relationships for XBRL ([#3084](https://github.com/docling-project/docling/issues/3084)) ([`7952efe`](https://github.com/docling-project/docling/commit/7952efee2fcbae2a9c516d75acd8995c004fc949))

### Fix

* Use OCR cells with TableFormer v2 ([#3107](https://github.com/docling-project/docling/issues/3107)) ([`93f6fee`](https://github.com/docling-project/docling/commit/93f6feeabcef81b1f71a189458b0166af9db176c))
* Add self-consistency check in the table-structure model ([#3105](https://github.com/docling-project/docling/issues/3105)) ([`2a0e11f`](https://github.com/docling-project/docling/commit/2a0e11f762fc06e16597c5d3662bc47a500efefa))
* Correct typos in log messages and add missing error log ([#3097](https://github.com/docling-project/docling/issues/3097)) ([`198d0af`](https://github.com/docling-project/docling/commit/198d0af19b20424e118301d47d155e4b021e50a7))
* Don't force cast to float32 in API Kserve v2 inputs ([#3101](https://github.com/docling-project/docling/issues/3101)) ([`fef01f8`](https://github.com/docling-project/docling/commit/fef01f8c88ed827e6443f4f6fc25fa94571dcd41))

## [v2.78.0](https://github.com/docling-project/docling/releases/tag/v2.78.0) - 2026-03-10

### Feature

* Add support for TableFormer v2 ([#3013](https://github.com/docling-project/docling/issues/3013)) ([`4ccd1d4`](https://github.com/docling-project/docling/commit/4ccd1d465deb8d521c09e2da61b537a9236d6560))
* Add gRPC transport for KServe v2 API engine ([#3074](https://github.com/docling-project/docling/issues/3074)) ([`3d90778`](https://github.com/docling-project/docling/commit/3d90778e3e5762b16758e1c121f42890e32f0560))

### Fix

* **html:** Fix broken document tree and quadratic complexity in rich table cells ([#3025](https://github.com/docling-project/docling/issues/3025)) ([`80f75b8`](https://github.com/docling-project/docling/commit/80f75b8896a6b15c5422c56e9a423e4d2e6673cd))
* Loosen dependency for pandas3 ([#3095](https://github.com/docling-project/docling/issues/3095)) ([`5188180`](https://github.com/docling-project/docling/commit/5188180ea31dd90567140affc564ce2729b6e4a1))
* Add parse timeout to legacy LaTeX documents ([#3019](https://github.com/docling-project/docling/issues/3019)) ([`1192714`](https://github.com/docling-project/docling/commit/1192714b536ebb8117785b06ed85e7d203e0996d))
* **msword:** Skip GroupItem targets without comments attribute ([#3080](https://github.com/docling-project/docling/issues/3080)) ([`ee16285`](https://github.com/docling-project/docling/commit/ee16285651e5c2f963e051b1ee32b50a043191e2))

### Documentation

* Fix code in rag langchain chunker tokenizer ([#2993](https://github.com/docling-project/docling/issues/2993)) ([`d113e61`](https://github.com/docling-project/docling/commit/d113e611c445db6793fd94b3fee9c4109513d04a))
* Update code snippet to use modern pipeline options syntax ([#3087](https://github.com/docling-project/docling/issues/3087)) ([`95b759e`](https://github.com/docling-project/docling/commit/95b759e5199f1142fb66dc2088c0c36177c5c284))
* Set HuggingFaceEndpoint task for Mixtral examples ([#2945](https://github.com/docling-project/docling/issues/2945)) ([`5d3ac38`](https://github.com/docling-project/docling/commit/5d3ac38a65000cd39766f87557c685668224ad7f))

## [v2.77.0](https://github.com/docling-project/docling/releases/tag/v2.77.0) - 2026-03-06

### Feature

* Track vlm_inference time for mlx_model pipeline ([#3060](https://github.com/docling-project/docling/issues/3060)) ([`38c4bb2`](https://github.com/docling-project/docling/commit/38c4bb26e8e3a7797d1caec3f690a7c8d5d9a735))
* Add configurable graph_optimization_level for ONNX Runtime engines ([#3071](https://github.com/docling-project/docling/issues/3071)) ([`cfc6636`](https://github.com/docling-project/docling/commit/cfc6636a2a0e6b149dd51714d20e9b93f3f6463b))

### Fix

* **docx:** Preserve URL fragments and query params in hyperlinks ([#3050](https://github.com/docling-project/docling/issues/3050)) ([`cd9dd10`](https://github.com/docling-project/docling/commit/cd9dd10ccfe2a112af10ad135f8293d3bf845e1a))
* Detect Office Open XML formats from ZIP contents when filename has no extension ([#3073](https://github.com/docling-project/docling/issues/3073)) ([`56f06fe`](https://github.com/docling-project/docling/commit/56f06fe372e3bfda29c14d66de0a066afb4c79c0))
* **readingorder:** Assign FURNITURE content_layer to footer/header in container groups ([#3044](https://github.com/docling-project/docling/issues/3044)) ([`f7cb304`](https://github.com/docling-project/docling/commit/f7cb304daa7b7bfe49ba23b81d53fb16da4024af))
* **docx:** Handle list items immediately after numbered headings ([#3070](https://github.com/docling-project/docling/issues/3070)) ([`56eb127`](https://github.com/docling-project/docling/commit/56eb12782c804b7ec36145bf52c1e005839c816b))
* **rapidocr:** ORT thread configuration for RapidOCR backend ([#3062](https://github.com/docling-project/docling/issues/3062)) ([`68336c2`](https://github.com/docling-project/docling/commit/68336c2bda2b79f10759ad1587626c47500f4fb4))

### Documentation

* Add examples and fix docstring bug in DocumentConverter ([#3064](https://github.com/docling-project/docling/issues/3064)) ([`653940e`](https://github.com/docling-project/docling/commit/653940e0251e1bc5f311aded31690c64f42d9819))
* Add docstrings to PipelineOptions classes ([#3065](https://github.com/docling-project/docling/issues/3065)) ([`8b99085`](https://github.com/docling-project/docling/commit/8b990856cd48fec12c68d940e665d8187d349753))

## [v2.76.0](https://github.com/docling-project/docling/releases/tag/v2.76.0) - 2026-03-02

### Feature

* Export to WebVTT format ([#3036](https://github.com/docling-project/docling/issues/3036)) ([`d276e60`](https://github.com/docling-project/docling/commit/d276e6056106b6aa04fee65def96d3e10557d632))

### Fix

* **xlsx:** Handle OneCellAnchor images in Excel backend ([#3045](https://github.com/docling-project/docling/issues/3045)) ([`859c302`](https://github.com/docling-project/docling/commit/859c302310289c5bab45a6e160e7cc3b9c538343))
* Normalize Unicode ligatures in PDF text extraction ([#3057](https://github.com/docling-project/docling/issues/3057)) ([`6198e69`](https://github.com/docling-project/docling/commit/6198e69dec33d9c14b3be279b19924d73e5eb3fb))
* **ocr:** Update RapidOCR torch GPU config key ([#3049](https://github.com/docling-project/docling/issues/3049)) ([`477359b`](https://github.com/docling-project/docling/commit/477359b772039b9c9c0d31c9dabcd755abdeb560))
* Convert PIL images to RGB before picture description ([#3014](https://github.com/docling-project/docling/issues/3014)) ([`90ce93d`](https://github.com/docling-project/docling/commit/90ce93d8a095ea17040bd6a91ded0b463998bea9))
* **msword:** Use outlineLvl for heading levels and clamp to minimum 1 ([#2916](https://github.com/docling-project/docling/issues/2916)) ([`a3d2b4b`](https://github.com/docling-project/docling/commit/a3d2b4bcc07fc00fff3039ae2046ee69b7587ab2))

### Documentation

* Add metaxy integration ([#3058](https://github.com/docling-project/docling/issues/3058)) ([`7aacc6c`](https://github.com/docling-project/docling/commit/7aacc6c18da3e856babb0f06afd7c985774f118e))
* Removes merge conflict artifacts ([#3055](https://github.com/docling-project/docling/issues/3055)) ([`672125c`](https://github.com/docling-project/docling/commit/672125cd1bb5e22bb7a677f48157a55ca93f9ff6))
* Add audio & video processing guide ([#3038](https://github.com/docling-project/docling/issues/3038)) ([`1321b39`](https://github.com/docling-project/docling/commit/1321b39cd8203d5e1cd60191cc9e979c5b939f98))
* Add XBRL conversion example notebook and update feature listings ([#3039](https://github.com/docling-project/docling/issues/3039)) ([`1eb5c21`](https://github.com/docling-project/docling/commit/1eb5c21dabfed02bfe71cb7fc502d124562f1ba8))

## [v2.75.0](https://githu
... [TRUNCATED]
```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

This project adheres to the [Docling - Code of Conduct and Covenant](https://github.com/docling-project/community/blob/main/CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code.

```

### File: CONTRIBUTING.md
```md
## Contributing In General
Our project welcomes external contributions. If you have an itch, please feel
free to scratch it.

For more details on the contributing guidelines head to the Docling Project [community repository](https://github.com/docling-project/community).

## Developing

### Usage of uv

We use [uv](https://docs.astral.sh/uv/) as package and project manager.

#### Installation

To install `uv`, check the documentation on [Installing uv](https://docs.astral.sh/uv/getting-started/installation/).

#### Create an environment and sync it

You can use the `uv sync` to create a project virtual environment (if it does not already exist) and sync
the project's dependencies with the environment.

```bash
uv sync
```

#### Use a specific Python version (optional)

If you need to work with a specific version of Python, you can create a new virtual environment for that version
and run the sync command:

```bash
uv venv --python 3.12
uv sync
```

More detailed options are described on the [Using Python environments](https://docs.astral.sh/uv/pip/environments/) documentation.

#### Add a new dependency

Simply use the `uv add` command. The `pyproject.toml` and `uv.lock` files will be updated.

```bash
uv add [OPTIONS] <PACKAGES|--requirements <REQUIREMENTS>>
```

## Coding Style Guidelines

We use the following tools to enforce code style:

- [Ruff](https://docs.astral.sh/ruff/), as linter and code formatter
- [MyPy](https://mypy.readthedocs.io), as static type checker

A set of styling checks, as well as regression tests, are defined and managed through the [pre-commit](https://pre-commit.com/) framework.
To ensure that those scripts run automatically before a commit is finalized, install `pre-commit` on your local repository:

```bash
pre-commit install
```

To run the checks on-demand, run:

```bash
pre-commit run --all-files
```

Note: Checks like `Ruff` will "fail" if they modify files. This is because `pre-commit` doesn't like to see files modified by its hooks. In these cases, `git add` the modified files and `git commit` again.

## Tests

When submitting a new feature or fix, please consider adding a short test for it.

### Reference test documents

When a change improves the conversion results, multiple reference documents must be regenerated and reviewed.

The reference data can be regenerated with

```sh
DOCLING_GEN_TEST_DATA=1 uv run pytest
```

All PRs modifying the reference test data require a double review to guarantee we don't miss edge cases.


## Documentation

We use [MkDocs](https://www.mkdocs.org/) to write documentation.

To run the documentation server, run:

```bash
mkdocs serve
```

The server will be available at [http://localhost:8000](http://localhost:8000).

### Pushing Documentation to GitHub Pages

Run the following:

```bash
mkdocs gh-deploy
```
```

### File: MAINTAINERS.md
```md
# MAINTAINERS

- Christoph Auer - [@cau-git](https://github.com/cau-git)
- Michele Dolfi - [@dolfim-ibm](https://github.com/dolfim-ibm)
- Panos Vagenas - [@vagenas](https://github.com/vagenas)
- Peter Staar - [@PeterStaar-IBM](https://github.com/PeterStaar-IBM)

Maintainers can be contacted at [deepsearch-core@zurich.ibm.com](mailto:deepsearch-core@zurich.ibm.com).

```

### File: .actor\actor.json
```json
{
  "actorSpecification": 1,
  "name": "docling",
  "version": "1.0",
  "environmentVariables": {},
  "dockerFile": "./Dockerfile",
  "inputSchema": "./input_schema.json",
  "scripts": {
    "run": "./actor.sh"
  }
}

```

### File: .actor\actor.sh
```sh
#!/bin/bash

export PATH=$PATH:/build-files/node_modules/.bin

# Function to upload content to the key-value store
upload_to_kvs() {
    local content_file="$1"
    local key_name="$2"
    local content_type="$3"
    local description="$4"

    # Find the Apify CLI command
    find_apify_cmd
    local apify_cmd="$FOUND_APIFY_CMD"

    if [ -n "$apify_cmd" ]; then
        echo "Uploading $description to key-value store (key: $key_name)..."

        # Create a temporary home directory with write permissions
        setup_temp_environment

        # Use the --no-update-notifier flag if available
        if $apify_cmd --help | grep -q "\--no-update-notifier"; then
            if $apify_cmd --no-update-notifier actor:set-value "$key_name" --contentType "$content_type" < "$content_file"; then
                echo "Successfully uploaded $description to key-value store"
                local url="https://api.apify.com/v2/key-value-stores/${APIFY_DEFAULT_KEY_VALUE_STORE_ID}/records/$key_name"
                echo "$description available at: $url"
                cleanup_temp_environment
                return 0
            fi
        else
            # Fall back to regular command if flag isn't available
            if $apify_cmd actor:set-value "$key_name" --contentType "$content_type" < "$content_file"; then
                echo "Successfully uploaded $description to key-value store"
                local url="https://api.apify.com/v2/key-value-stores/${APIFY_DEFAULT_KEY_VALUE_STORE_ID}/records/$key_name"
                echo "$description available at: $url"
                cleanup_temp_environment
                return 0
            fi
        fi

        echo "ERROR: Failed to upload $description to key-value store"
        cleanup_temp_environment
        return 1
    else
        echo "ERROR: Apify CLI not found for $description upload"
        return 1
    fi
}

# Function to find Apify CLI command
find_apify_cmd() {
    FOUND_APIFY_CMD=""
    for cmd in "apify" "actor" "/usr/local/bin/apify" "/usr/bin/apify" "/opt/apify/cli/bin/apify"; do
        if command -v "$cmd" &> /dev/null; then
            FOUND_APIFY_CMD="$cmd"
            break
        fi
    done
}

# Function to set up temporary environment for Apify CLI
setup_temp_environment() {
    export TMPDIR="/tmp/apify-home-${RANDOM}"
    mkdir -p "$TMPDIR"
    export APIFY_DISABLE_VERSION_CHECK=1
    export NODE_OPTIONS="--no-warnings"
    export HOME="$TMPDIR"  # Override home directory to writable location
}

# Function to clean up temporary environment
cleanup_temp_environment() {
    rm -rf "$TMPDIR" 2>/dev/null || true
}

# Function to push data to Apify dataset
push_to_dataset() {
    # Example usage: push_to_dataset "$RESULT_URL" "$OUTPUT_SIZE" "zip"

    local result_url="$1"
    local size="$2"
    local format="$3"

    # Find Apify CLI command
    find_apify_cmd
    local apify_cmd="$FOUND_APIFY_CMD"

    if [ -n "$apify_cmd" ]; then
        echo "Adding record to dataset..."
        setup_temp_environment

        # Use the --no-update-notifier flag if available
        if $apify_cmd --help | grep -q "\--no-update-notifier"; then
            if $apify_cmd --no-update-notifier actor:push-data "{\"output_file\": \"${result_url}\", \"format\": \"${format}\", \"size\": \"${size}\", \"status\": \"success\"}"; then
                echo "Successfully added record to dataset"
            else
                echo "Warning: Failed to add record to dataset"
            fi
        else
            # Fall back to regular command
            if $apify_cmd actor:push-data "{\"output_file\": \"${result_url}\", \"format\": \"${format}\", \"size\": \"${size}\", \"status\": \"success\"}"; then
                echo "Successfully added record to dataset"
            else
                echo "Warning: Failed to add record to dataset"
            fi
        fi

        cleanup_temp_environment
    fi
}


# --- Setup logging and error handling ---

LOG_FILE="/tmp/docling.log"
touch "$LOG_FILE" || {
    echo "Fatal: Cannot create log file at $LOG_FILE"
    exit 1
}

# Log to both console and file
exec 1> >(tee -a "$LOG_FILE")
exec 2> >(tee -a "$LOG_FILE" >&2)

# Exit codes
readonly ERR_API_UNAVAILABLE=15
readonly ERR_INVALID_INPUT=16


# --- Debug environment ---

echo "Date: $(date)"
echo "Python version: $(python --version 2>&1)"
echo "Docling-serve path: $(which docling-serve 2>/dev/null || echo 'Not found')"
echo "Working directory: $(pwd)"

# --- Get input ---

echo "Getting Apify Actor Input"
INPUT=$(apify actor get-input 2>/dev/null)

# --- Setup tools ---

echo "Setting up tools..."
TOOLS_DIR="/tmp/docling-tools"
mkdir -p "$TOOLS_DIR"

# Copy tools if available
if [ -d "/build-files" ]; then
    echo "Copying tools from /build-files..."
    cp -r /build-files/* "$TOOLS_DIR/"
    export PATH="$TOOLS_DIR/bin:$PATH"
else
    echo "Warning: No build files directory found. Some tools may be unavailable."
fi

# Check OCR directories and ensure they're writable
echo "Checking OCR directory permissions..."
OCR_DIR="/opt/app-root/src/.EasyOCR"
if [ -d "$OCR_DIR" ]; then
    # Test if we can write to the directory
    if touch "$OCR_DIR/test_write" 2>/dev/null; then
        echo "[✓] OCR directory is writable"
        rm "$OCR_DIR/test_write"
    else
        echo "[✗] OCR directory is not writable, setting up alternative in /tmp"

        # Create alternative in /tmp (which is writable)
        mkdir -p "/tmp/.EasyOCR/user_network"
        export EASYOCR_MODULE_PATH="/tmp/.EasyOCR"
    fi
else
    echo "OCR directory not found, creating in /tmp"
    mkdir -p "/tmp/.EasyOCR/user_network"
    export EASYOCR_MODULE_PATH="/tmp/.EasyOCR"
fi


# --- Starting the API ---

echo "Starting docling-serve API..."

# Create a dedicated working directory in /tmp (writable)
API_DIR="/tmp/docling-api"
mkdir -p "$API_DIR"
cd "$API_DIR"
echo "API working directory: $(pwd)"

# Find docling-serve executable
DOCLING_SERVE_PATH=$(which docling-serve)
echo "Docling-serve executable: $DOCLING_SERVE_PATH"

# Start the API with minimal parameters to avoid any issues
echo "Starting docling-serve API..."
"$DOCLING_SERVE_PATH" run --host 0.0.0.0 --port 5001 > "$API_DIR/docling-serve.log" 2>&1 &
API_PID=$!
echo "Started docling-serve API with PID: $API_PID"

# A more reliable wait for API startup
echo "Waiting for API to initialize..."
MAX_TRIES=30
tries=0
started=false

while [ $tries -lt $MAX_TRIES ]; do
    tries=$((tries + 1))

    # Check if process is still running
    if ! ps -p $API_PID > /dev/null; then
        echo "ERROR: docling-serve API process terminated unexpectedly after $tries seconds"
        break
    fi

    # Check log for startup completion or errors
    if grep -q "Application startup complete" "$API_DIR/docling-serve.log" 2>/dev/null; then
        echo "[✓] API startup completed successfully after $tries seconds"
        started=true
        break
    fi

    if grep -q "Permission denied\|PermissionError" "$API_DIR/docling-serve.log" 2>/dev/null; then
        echo "ERROR: Permission errors detected in API startup"
        break
    fi

    # Sleep and check again
    sleep 1

    # Output a progress indicator every 5 seconds
    if [ $((tries % 5)) -eq 0 ]; then
        echo "Still waiting for API startup... ($tries/$MAX_TRIES seconds)"
    fi
done

# Show log content regardless of outcome
echo "docling-serve log output so far:"
tail -n 20 "$API_DIR/docling-serve.log"

# Verify the API is running
if ! ps -p $API_PID > /dev/null; then
    echo "ERROR: docling-serve API failed to start"
    if [ -f "$API_DIR/docling-serve.log" ]; then
        echo "Full log output:"
        cat "$API_DIR/docling-serve.log"
    fi
    exit $ERR_API_UNAVAILABLE
fi

if [ "$started" != "true" ]; then
    echo "WARNING: API process is running but startup completion was not detected"
    echo "Will attempt to continue anyway..."
fi

# Try to verify API is responding at this point
echo "Verifying API responsiveness..."
(python -c "
import sys, time, socket
for i in range(5):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex(('localhost', 5001))
        if result == 0:
            s.close()
            print('Port 5001 is open and accepting connections')
            sys.exit(0)
        s.close()
    except Exception as e:
        pass
    time.sleep(1)
print('Could not connect to API port after 5 attempts')
sys.exit(1)
" && echo "API verification succeeded") || echo "API verification failed, but continuing anyway"

# Define API endpoint
DOCLING_API_ENDPOINT="http://localhost:5001/v1alpha/convert/source"


# --- Processing document ---

echo "Starting document processing..."
echo "Reading input from Apify..."

echo "Input content:" >&2
echo "$INPUT" >&2  # Send the raw input to stderr for debugging
echo "$INPUT"      # Send the clean JSON to stdout for processing

# Create the request JSON

REQUEST_JSON=$(echo $INPUT | jq '.options += {"return_as_file": true}')

echo "Creating request JSON:" >&2
echo "$REQUEST_JSON" >&2
echo "$REQUEST_JSON" > "$API_DIR/request.json"


# Send the conversion request using our Python script
#echo "Sending conversion request to docling-serve API..."
#python "$TOOLS_DIR/docling_processor.py" \
#    --api-endpoint "$DOCLING_API_ENDPOINT" \
#    --request-json "$API_DIR/request.json" \
#    --output-dir "$API_DIR" \
#    --output-format "$OUTPUT_FORMAT"

echo "Curl the Docling API"
curl -s -H "content-type: application/json" -X POST --data-binary @$API_DIR/request.json -o $API_DIR/output.zip $DOCLING_API_ENDPOINT

CURL_EXIT_CODE=$?

# --- Check for various potential output files ---

echo "Checking for output files..."
if [ -f "$API_DIR/output.zip" ]; then
    echo "Conversion completed successfully! Output file found."

    # Get content from the converted file
    OUTPUT_SIZE=$(wc -c < "$API_DIR/output.zip")
    echo "Output file found with size: $OUTPUT_SIZE bytes"

    # Calculate the access URL for result display
    RESULT_URL="https://api.apify.com/v2/key-value-stores/${APIFY_DEFAULT_KEY_VALUE_STORE_ID}/records/OUTPUT"

    echo "=============================="
    echo "PROCESSING COMPLETE!"
    echo "Output size: ${OUTPUT_SIZE} bytes"
    echo "=============================="

    # Set the output content type based on format
    CONTENT_TYPE="application/zip"

    # Upload the document content using our function
    upload_to_kvs "$API_DIR/output.zip" "OUTPUT" "$CONTENT_TYPE" "Document content"

    # Only proceed with dataset record if document upload succeeded
    if [ $? -eq 0 ]; then
        echo "Your document is available at: ${RESULT_URL}"
        echo "=============================="

        # Push data to dataset
        push_to_dataset "$RESULT_URL" "$OUTPUT_SIZE" "zip"
    fi
else
    echo "ERROR: No converted output file found at $API_DIR/output.zip"

    # Create error metadata
    ERROR_METADATA="{\"status\":\"error\",\"error\":\"No converted output file found\",\"documentUrl\":\"$DOCUMENT_URL\"}"
    echo "$ERROR_METADATA" > "/tmp/actor-output/OUTPUT"
    chmod 644 "/tmp/actor-output/OUTPUT"

    echo "Error information has been saved to /tmp/actor-output/OUTPUT"
fi


# --- Verify output files for debugging ---

echo "=== Final Output Verification ==="
echo "Files in /tmp/actor-output:"
ls -la /tmp/actor-output/ 2>/dev/null || echo "Cannot list /tmp/actor-output/"

echo "All operations completed. The output should be available in the default key-value store."
echo "Content URL: ${RESULT_URL:-No URL available}"


# --- Cleanup function ---

cleanup() {
    echo "Running cleanup..."

    # Stop the API process
    if [ -n "$API_PID" ]; then
        echo "Stopping docling-serve API (PID: $API_PID)..."
        kill $API_PID 2>/dev/null || true
    fi

    # Export log file to KVS if it exists
    # DO THIS BEFORE REMOVING TOOLS DIRECTORY
    if [ -f "$LOG_FILE" ]; then
        if [ -s "$LOG_FILE" ]; then
            echo "Log file is not empty, pushing to key-value store (key: LOG)..."

            # Upload log using our function
            upload_to_kvs "$LOG_FILE" "LOG" "text/plain" "Log file"
        else
            echo "Warning: log file exists but is empty"
        fi
    else
        echo "Warning: No log file found"
    fi

    # Clean up temporary files AFTER log is uploaded
    echo "Cleaning up temporary files..."
    if [ -d "$API_DIR" ]; then
        echo "Removing API working directory: $API_DIR"
        rm -rf "$API_DIR" 2>/dev/null || echo "Warning: Failed to remove $API_DIR"
    fi

    if [ -d "$TOOLS_DIR" ]; then
        echo "Removing tools directory: $TOOLS_DIR"
        rm -rf "$TOOLS_DIR" 2>/dev/null || echo "Warning: Failed to remove $TOOLS_DIR"
    fi

    # Keep log file until the very end
    echo "Script execution completed at $(date)"
    echo "Actor execution completed"
}

# Register cleanup
trap cleanup EXIT

```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
