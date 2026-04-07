---
id: chroma
type: knowledge
owner: OA_Triage
---
# chroma
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
![Chroma](./docs/assets/chroma-wordmark-color.png#gh-light-mode-only)
![Chroma](./docs/assets/chroma-wordmark-white.png#gh-dark-mode-only)

<p align="center">
    <b>Chroma - the open-source data infrastructure for AI</b>. <br />
</p>

<p align="center">
  <a href="https://discord.gg/MMeYNTmh3x" target="_blank">
      <img src="https://img.shields.io/discord/1073293645303795742?cacheSeconds=3600" alt="Discord">
  </a> |
  <a href="https://github.com/chroma-core/chroma/blob/master/LICENSE" target="_blank">
      <img src="https://img.shields.io/badge/License-Apache_2.0-blue.svg" alt="License">
  </a> |
  <a href="https://docs.trychroma.com/" target="_blank">
      Docs
  </a> |
  <a href="https://www.trychroma.com/" target="_blank">
      Homepage
  </a>
</p>

```bash
pip install chromadb # python client
# for javascript, npm install chromadb!
# for client-server mode, chroma run --path /chroma_db_path
```

## Chroma Cloud

Our hosted service, Chroma Cloud, powers serverless vector, hybrid, and full-text search. It's extremely fast, cost-effective, scalable and painless. Create a DB and try it out in under 30 seconds with $5 of free credits.

[Get started with Chroma Cloud](https://trychroma.com/signup)

## API

The core API is only 4 functions (run our [💡 Google Colab](https://colab.research.google.com/drive/1QEzFyqnoFxq7LUGyP1vzR4iLt9PpCDXv?usp=sharing)):

```python
import chromadb
# setup Chroma in-memory, for easy prototyping. Can add persistence easily!
client = chromadb.Client()

# Create collection. get_collection, get_or_create_collection, delete_collection also available!
collection = client.create_collection("all-my-documents")

# Add docs to the collection. Can also update and delete. Row-based API coming soon!
collection.add(
    documents=["This is document1", "This is document2"], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
    ids=["doc1", "doc2"], # unique for each doc
)

# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2,
    # where={"metadata_field": "is_equal_to_this"}, # optional filter
    # where_document={"$contains":"search_string"}  # optional filter
)
```

Learn about all features on our [Docs](https://docs.trychroma.com)

## Get involved

Chroma is a rapidly developing project. We welcome PR contributors and ideas for how to improve the project.
- [Join the conversation on Discord](https://discord.com/invite/chromadb) - `#contributing` channel
- [Review the 🛣️ Roadmap and contribute your ideas](https://docs.trychroma.com/docs/overview/oss#roadmap)
- [Grab an issue and open a PR](https://github.com/chroma-core/chroma/issues) - [`Good first issue tag`](https://github.com/chroma-core/chroma/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22)
- [Read our contributing guide](https://docs.trychroma.com/docs/overview/oss#contributing)

**Release Cadence**
We currently release new tagged versions of the `pypi` and `npm` packages on Mondays. Hotfixes go out at any time during the week.

## License

[Apache 2.0](./LICENSE)

```

### File: requirements.txt
```txt
bcrypt>=4.0.1
graphlib_backport==1.0.3; python_version < '3.9'
grpcio>=1.58.0
httpx>=0.27.0
importlib-resources
jsonschema>=4.19.0
kubernetes>=28.1.0
mmh3>=4.0.1
numpy>=1.22.5
onnxruntime>=1.14.1
opentelemetry-api>=1.24.0
opentelemetry-exporter-otlp-proto-grpc>=1.24.0
opentelemetry-sdk>=1.24.0
orjson>=3.9.12
overrides>=7.3.1
pybase64>=1.4.1
pydantic>=2.0
pydantic-settings>=2.0
pypika>=0.48.9
PyYAML>=6.0.0
rich>=10.11.0
tenacity>=8.2.3
tokenizers>=0.13.2
tqdm>=4.65.0
typer>=0.9.0
typing_extensions>=4.5.0
uvicorn[standard]>=0.18.3

```

### File: examples\README.md
```md
## Examples

> Searching for community contributions! Join the [#contributing](https://discord.com/channels/1073293645303795742/1074711539724058635) Discord Channel to discuss.

This folder will contain an ever-growing set of examples.

The key with examples is that they should *always* work. The failure mode of examples folders is that they get quickly deprecated.

Examples are:
- Easy to maintain
- Easy to maintain examples are __simple__
- Use case examples are fine, technology is better

```
folder structure
- basic_functionality - notebooks with simple walkthroughs
- advanced_functionality - notebooks with advanced walkthroughs
- deployments - how to deploy places
- use_with - chroma + ___, where ___ can be langchain, nextjs, etc
- data - common data for examples
```

> 💡 Feel free to open a PR with an example you would like to see

### Basic Functionality
- [x] Examples of using different embedding models
- [x] Local persistance demo
- [x] Where filtering demo

### Advanced Functionality
- [ ] Clustering
- [ ] Projections
- [ ] Fine tuning

### Use With

#### LLM Application Code
- [ ] Langchain
- [ ] LlamaIndex
- [ ] Semantic Kernal

#### App Frameworks
- [ ] Streamlit
- [ ] Gradio
- [ ] Nextjs
- [ ] Rails
- [ ] FastAPI

#### Inference Services
- [ ] Brev.dev
- [ ] Banana.dev
- [ ] Modal

### LLM providers/services
- [ ] OpenAI
- [ ] Anthropic
- [ ] Cohere
- [ ] Google PaLM
- [ ] Hugging Face

***

### Inspiration
- The [OpenAI Cookbook](https://github.com/openai/openai-cookbook) gets a lot of things right

```

### File: docs\scripts\README.md
```md
# Documentation Generator Scripts

## Python Reference

Generate all split reference files into `docs/mintlify/reference/python/`:

```bash
uv run docs/scripts/generate_python_reference.py --output reference/python/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/python` and `/reference/python/index` redirect to `/reference/python/client`. The file `reference/python/where-filter.mdx` is maintained by hand (Python DSL only) and is not overwritten by the script.

## TypeScript Reference

Generate all split reference files into `docs/mintlify/reference/typescript/`:

```bash
bun run docs/scripts/generate_ts_reference.ts --output reference/typescript/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/typescript` and `/reference/typescript/index` redirect to `/reference/typescript/client`. The file `reference/typescript/where-filter.mdx` is maintained by hand (TypeScript DSL only) and is not overwritten by the script.

```

### File: .pre-commit-config.yaml
```yaml
exclude: 'chromadb/proto/(chroma_pb2|coordinator_pb2|logservice_pb2|chroma_pb2_grpc|coordinator_pb2_grpc|logservice_pb2_grpc)\.(py|pyi)' # Generated files
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.6.0
    hooks:
      - id: trailing-whitespace
        exclude: ".*\\.gen\\.ts$"
      - id: mixed-line-ending
      - id: end-of-file-fixer
        exclude: "go/migrations|.*\\.gen\\.ts$"
      - id: requirements-txt-fixer
      - id: check-yaml
        args: ["--allow-multiple-documents"]
        # Exclude Helm templates from YAML linting as they are not valid YAML
        exclude: "k8s/distributed-chroma/templates/"
      - id: check-xml
      - id: check-merge-conflict
      - id: check-case-conflict
      - id: check-docstring-first

  - repo: https://github.com/psf/black-pre-commit-mirror
    # https://github.com/psf/black/issues/2493
    rev: "23.3.0"
    hooks:
      - id: black

  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args:
          - "--extend-ignore=E203,E501,E503"
          - "--max-line-length=88"

  - repo: https://github.com/pre-commit/mirrors-mypy
    rev: "v1.10.0"
    hooks:
      - id: mypy
        args:
          [
            --strict,
            --ignore-missing-imports,
            --follow-imports=silent,
            --disable-error-code=type-abstract,
            --config-file=./pyproject.toml,
          ]
        additional_dependencies:
          [
            "pydantic",
            "overrides",
            "hypothesis",
            "pytest",
            "pypika",
            "numpy",
            "types-protobuf",
            "kubernetes",
          ]

  - repo: https://github.com/pre-commit/mirrors-prettier
    rev: "v3.1.0"
    hooks:
      - id: prettier
        files: "^clients/(js|new-js)/.+"
        exclude: "^clients/(js|new-js)/src/generated/.+|.*\\.gen\\.ts$"
        additional_dependencies:
          - prettier@2.8.7

```

### File: bandit.yaml
```yaml
# FILE: bandit.yaml
exclude_dirs: [ 'chromadb/test', 'bin', 'build', 'build', '.git', '.venv', 'venv', 'env','.github','examples','clients/js','.vscode' ]
tests: [ ]
skips: [ ]

```

### File: DEVELOP.md
```md
# Development Instructions

This project uses the testing, build and release standards specified
by the PyPA organization and documented at
<https://packaging.python.org>.

## Setup

Set up a virtual environment and install the project's requirements
and dev requirements:

```bash
python3 -m venv venv      # Only need to do this once
source venv/bin/activate  # Do this each time you use a new shell for the project
pip install -r requirements.txt
pip install -r requirements_dev.txt
pre-commit install # install the precommit hooks
```

Install protobuf:
for MacOS `brew install protobuf`

You can also install `chromadb` the `pypi` package locally and in editable mode with `pip install -e .`.

## Local dev setup for distributed chroma

We use tilt for providing local dev setup. Tilt is an open source project

### Requirement

- Docker
- Local Kubernetes cluster (Recommended: [OrbStack](https://orbstack.dev/) for mac, [Kind](https://kind.sigs.k8s.io/) for linux)
- [Tilt](https://docs.tilt.dev/)
- [Helm](https://helm.sh)

1. Start Kubernetes. If you're using OrbStack, navigate to `Kubernetes - Pods`, and select `Turn On`
2. Start a distributed Chroma cluster by running `tilt up` from the root of the repository.
3. Once done, it will expose Chroma on port 8000. You can also visit the Tilt dashboard UI at `http://localhost:10350/`.
4. To clean and remove all the resources created by Tilt, use `tilt down`.

## Testing

Unit tests are in the `/chromadb/test` directory.

To run unit tests using your current environment, run `pytest`.

Make sure to have `tilt up` running for these tests otherwise some distributed Chroma tests will fail.

## Manual Build

Make sure the following is only done in the virtual environment created in the [Setup](#setup) section above.

To manually build the rust codebase and bindings for type safety, run `maturin dev`.

To manually build a distribution, run `python -m build`.

The project's source and wheel distributions will be placed in the `dist` directory.

If you have `tilt up` running, saving changes to your files will automatically rebuild new binaries with your changes and deploy to the local cluster `tilt` has running.

## IDE Recommendations

If you are developing with VSCode or its derivatives (Windsurf/Cursor etc), make sure to install the `rust-analyzer` extension. It helps with auto-formatting, Intellisense and code navigation.

For debugging it is recommended to install the `CodeLLDB` extension.

You should be able to run and debug the rust tests by clicking on the 'Run Test' or 'Debug' button found above the test method definitions.

![rust-analyzer extension](https://github.com/user-attachments/assets/a7779e4d-9d64-4511-9271-b790bed7b68b)

## Setting breakpoints in Distributed Chroma

Debugging binaries in the Kubernetes pods that `tilt up` spins up is a bit more involved. Right now the only reliable way to set a breakpoint in this scenario is to log in to the pod, install lldb/gdb and set a breakpoint that way. For example after running `tilt up` you can set a breakpoint in the query-service-0 pod as follows:

```bash
kubectl exec -it query-service-0 -n chroma -- /bin/sh
apt-get update && apt-get install gdb
gdb
(gdb) b <relative_file_path>:<lineno>
```

## Manual Release

Not yet implemented.

## Versioning

This project uses PyPA's `setuptools_scm` module to determine the
version number for build artifacts, meaning the version number is
derived from Git rather than hardcoded in the repository. For full
details, see the
[documentation for setuptools_scm](https://github.com/pypa/setuptools_scm/).

In brief, version numbers are generated as follows:

- If the current git head is tagged, the version number is exactly the
  tag (e.g, `0.0.1`).
- If the current git head is a clean checkout, but is not tagged,
  the version number is a patch version increment of the most recent
  tag, plus `devN` where N is the number of commits since the most
  recent tag. For example, if there have been 5 commits since the
  `0.0.1` tag, the generated version will be `0.0.2-dev5`.
- If the current head is not a clean checkout, a `+dirty` local
  version will be appended to the version number. For example,
  `0.0.2-dev5+dirty`.

At any point, you can manually run `python -m setuptools_scm` to see
what version would be assigned given your current state.

## Continuous Integration

This project uses Github Actions to run unit tests automatically upon
every commit to the main branch. See the documentation for Github
Actions and the flow definitions in `.github/workflows` for details.

## Continuous Delivery

Not yet implemented.

```

### File: docs_DISTILLED.md
```md
---
id: docs
type: distilled_knowledge
---
# docs

## SWALLOW ENGINE DISTILLATION

### File: scripts\README.md
```md
# Documentation Generator Scripts

## Python Reference

Generate all split reference files into `docs/mintlify/reference/python/`:

```bash
uv run docs/scripts/generate_python_reference.py --output reference/python/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/python` and `/reference/python/index` redirect to `/reference/python/client`. The file `reference/python/where-filter.mdx` is maintained by hand (Python DSL only) and is not overwritten by the script.

## TypeScript Reference

Generate all split reference files into `docs/mintlify/reference/typescript/`:

```bash
bun run docs/scripts/generate_ts_reference.ts --output reference/typescript/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/typescript` and `/reference/typescript/index` redirect to `/reference/typescript/client`. The file `reference/typescript/where-filter.mdx` is maintained by hand (TypeScript DSL only) and is not overwritten by the script.

```

### File: scripts_DISTILLED.md
```md
---
id: scripts
type: distilled_knowledge
---
# scripts

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Documentation Generator Scripts

## Python Reference

Generate all split reference files into `docs/mintlify/reference/python/`:

```bash
uv run docs/scripts/generate_python_reference.py --output reference/python/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/python` and `/reference/python/index` redirect to `/reference/python/client`. The file `reference/python/where-filter.mdx` is maintained by hand (Python DSL only) and is not overwritten by the script.

## TypeScript Reference

Generate all split reference files into `docs/mintlify/reference/typescript/`:

```bash
bun run docs/scripts/generate_ts_reference.ts --output reference/typescript/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/typescript` and `/reference/typescript/index` redirect to `/reference/typescript/client`. The file `reference/typescript/where-filter.mdx` is maintained by hand (TypeScript DSL only) and is not overwritten by the script.

```

### File: generate_python_reference.py
```py
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "docstring-parser>=0.15",
#     "chromadb==1.5.0",
# ]
# ///
"""
Generate Python SDK reference documentation for Chroma.

Usage:
    uv run generate_python_reference.py --output reference/python/index.mdx

This script introspects the chromadb package and generates MDX documentation
with ParamField components for Mintlify.

To extend this script:
1. Add new sections to get_documentation_sections()
2. Add type simplifications to TYPE_SIMPLIFICATIONS
"""

from __future__ import annotations

import argparse
import inspect
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import (
    Any,
    Callable,
    Optional,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
)

from docstring_parser import parse as parse_docstring


# =============================================================================
# Configuration
# =============================================================================

TYPE_SIMPLIFICATIONS: dict[str, str] = {
    "ndarray": "Embedding",
    "Sequence[float]": "Embedding",
    "Sequence[int]": "Embedding",
    "List[Union[Sequence[float], Sequence[int]]]": "Embeddings",
    "Mapping[str, Union[str, int, float, bool, SparseVector, None]]": "Metadata",
    "List[Mapping[str, Union[str, int, float, bool, SparseVector, None]]]": "Metadatas",
}

TYPE_ALIASES: dict[str, str] = {
    "Union[str, List[str]]": "OneOrMany[str]",
    "Union[str, List[str], None]": "Optional[OneOrMany[str]]",
    "List[str]": "IDs",
    "Optional[List[str]]": "Optional[IDs]",
}


@dataclass
class SectionConfig:
    """Configuration for a documentation section."""

    title: str
    items: list[tuple[str, Any]] | list[str]
    source_class: Optional[type] = None
    render_mode: str = (
        "function"  # "function", "method", "class", "class_full", "type_alias"
    )
    output_file: str = "index"
    show_class_methods: bool = True


def get_documentation_sections() -> list[SectionConfig]:
    """Define all documentation sections with output_file for split generation."""
    import chromadb
    from chromadb.api import AdminAPI, ClientAPI
    from chromadb.api.models.Collection import Collection
    from chromadb.api.types import (
        BoolInvertedIndexConfig,
        Embedding,
        EmbeddingFunction,
        FloatInvertedIndexConfig,
        FtsIndexConfig,
        GetResult,
        HnswIndexConfig,
        IntInvertedIndexConfig,
        QueryResult,
        Schema,
        SearchResult,
        SparseEmbeddingFunction,
        SparseVectorIndexConfig,
        SpannIndexConfig,
        StringInvertedIndexConfig,
        VectorIndexConfig,
    )
    from chromadb.base_types import SparseVector
    from chromadb.execution.expression.operator import (
        GroupBy,
        Knn,
        Limit,
        MaxK,
        MinK,
        Rrf,
        Select,
    )
    from chromadb.execution.expression.plan import Search
    from chromadb.utils import embedding_functions as ef_module

    return [
        SectionConfig(
            title="Clients",
            render_mode="function",
            output_file="client",
            items=[
                ("EphemeralClient", chromadb.EphemeralClient),
                ("PersistentClient", chromadb.PersistentClient),
                ("HttpClient", chromadb.HttpClient),
                ("AsyncHttpClient", chromadb.AsyncHttpClient),
                ("CloudClient", chromadb.CloudClient),
                ("AdminClient", chromadb.AdminClient),
            ],
        ),
        SectionConfig(
            title="Client Methods",
            render_mode="method",
            source_class=ClientAPI,
            output_file="client",
            items=[
                "heartbeat",
                "list_collections",
                "count_collections",
                "create_collection",
                "get_collection",
                "get_or_create_collection",
                "delete_collection",
                "reset",
                "get_version",
                "get_settings",
                "get_max_batch_size",
            ],
        ),
        SectionConfig(
            title="Admin Client Methods",
            render_mode="method",
            source_class=AdminAPI,
            output_file="client",
            items=[
                "create_tenant",
                "get_tenant",
                "create_database",
                "get_database",
                "delete_database",
                "list_databases",
            ],
        ),
        SectionConfig(
            title="Collection Methods",
            render_mode="method",
            source_class=Collection,
            output_file="collection",
            items=[
                "count",
                "add",
                "get",
                "peek",
                "query",
                "modify",
                "update",
                "upsert",
                "delete",
            ],
        ),
        SectionConfig(
            title="Types",
            render_mode="class",
            output_file="collection",
            items=[
                ("GetResult", GetResult),
                ("QueryResult", QueryResult),
            ],
        ),
        SectionConfig(
            title="Embedding Function Base Classes",
            render_mode="class",
            output_file="embedding-functions",
            items=[
                ("EmbeddingFunction", EmbeddingFunction),
                ("SparseEmbeddingFunction", SparseEmbeddingFunction),
            ],
        ),
        SectionConfig(
            title="Registration",
            render_mode="function",
            output_file="embedding-functions",
            items=[
                ("register_embedding_function", ef_module.register_embedding_function),
                (
                    "register_sparse_embedding_function",
                    ef_module.register_sparse_embedding_function,
                ),
            ],
        ),
        SectionConfig(
            title="Types",
            render_mode="class",
            output_file="embedding-functions",
            items=[
                ("Embedding", Embedding),
                ("SparseVector", SparseVector),
            ],
        ),
        SectionConfig(
            title="Search",
            render_mode="class",
            output_file="search",
            items=[("Search", Search)],
        ),
        SectionConfig(
            title="Select",
            render_mode="class",
            output_file="search",
            items=[("Select", Select)],
        ),
        SectionConfig(
            title="Knn",
            render_mode="class",
            output_file="search",
            items=[("Knn", Knn)],
        ),
        SectionConfig(
            title="Rrf",
            render_mode="class",
            output_file="search",
            items=[("Rrf", Rrf)],
        ),
        SectionConfig(
            title="Group By",
            render_mode="class",
            output_file="search",
            items=[
                ("GroupBy", GroupBy),
                ("Limit", Limit),
                ("MinK", MinK),
                ("MaxK", MaxK),
            ],
        ),
        SectionConfig(
            title="SearchResult",
            render_mode="class",
            output_file="search",
            items=[("SearchResult", SearchResult)],
        ),
        SectionConfig(
            title="Schema",
            render_mode="class",
            output_file="schema",
            show_class_methods=False,
            items=[("Schema", Schema)],
        ),
        SectionConfig(
            title="Index configs",
            render_mode="class",
            output_file="schema",
            show_class_methods=False,
            items=[
                ("FtsIndexConfig", FtsIndexConfig),
                ("HnswIndexConfig", HnswIndexConfig),
                ("SpannIndexConfig", SpannIndexConfig),
                ("VectorIndexConfig", VectorIndexConfig),
                ("SparseVectorIndexConfig", SparseVectorIndexConfig),
                ("StringInvertedIndexConfig", StringInvertedIndexConfig),
                ("IntInvertedIndexConfig", IntInvertedIndexConfig),
                ("FloatInvertedIndexConfig", FloatInvertedIndexConfig),
                ("BoolInvertedIndexConfig", BoolInvertedIndexConfig),
            ],
        ),
    ]


# =============================================================================
# Data Model
# =============================================================================


@dataclass
class Param:
    """A parameter or property with type and optional description."""

    name: str
    type: str
    description: Optional[str] = None
    required: bool = False


@dataclass
class MethodDoc:
    """Documentation for a method."""

    name: str
    description: Optional[str] = None
    params: list[Param] = field(default_factory=list)
    returns: Optional[str] = None
    raises: list[str] = field(default_factory=list)
    is_async: bool = False


@dataclass
class FunctionDoc:
    """Documentation for a function."""

    name: str
    description: Optional[str] = None
    params: list[Param] = field(default_factory=list)
    returns: Optional[str] = None
    is_async: bool = False


@dataclass
class ClassDoc:
    """Documentation for a class."""

    name: str
    description: Optional[str] = None
    properties: list[Param] = field(default_factory=list)
    methods: list[MethodDoc] = field(default_factory=list)


# =============================================================================
# Type Formatting
# =============================================================================


def simplify_type(type_str: str) -> str:
    """Simplify complex type strings to more readable forms."""
    for pattern, replacement in TYPE_SIMPLIFICATIONS.items():
        if pattern in type_str:
            type_str = type_str.replace(pattern, replacement)

    for pattern, replacement in TYPE_ALIASES.items():
        if type_str == pattern:
            return replacement

    if "ForwardRef" in type_str:
        type_str = re.sub(r"ForwardRef\('(\w+)'\)", r"\1", type_str)

    if "Literal[" in type_str and type_str.count("Literal[") > 2:
        return "Where"

    if len(type_str) > 80:
        if "ndarray" in type_str.lower() or "embedding" in type_str.lower():
            return (
                "Optional[Embeddings]"
                if "List[" in type_str or "Union[" in type_str
                else "Optional[Embedding]"
            )
        if "Mapping" in type_str or "metadata" in type_str.lower():
            return (
                "Optional[Metadatas]" if "List[" in type_str else "Optional[Metadata]"
            )
        if "DataLoader" in type_str:
            return "Optional[DataLoader]"
        if "EmbeddingFunction" in type_str:
            return "Optional[EmbeddingFunction]"

    return type_str


def format_type(typ: Any) -> str:
    """Format a type annotation as a readable string."""
    if typ is None or typ is type(None):
        return "None"

    if isinstance(typ, str):
        return simplify_type(typ)

    origin = get_origin(typ)
    args = get_args(typ)

    if origin is Union:
        if len(args) == 2 and type(None) in args:
            inner = args[0] if args[1] is type(None) else args[1]
            return simplify_type(f"Optional[{format_type(inner)}]")
        return simplify_type(f"Union[{', '.join(format_type(a) for a in args)}]")

    if origin is not None:
        origin_name = getattr(origin, "__name__", str(origin))
        name_map = {"list": "List", "dict": "Dict", "tuple": "Tuple", "set": "Set"}
        origin_name = name_map.get(origin_name, origin_name)

        if args:
            return simplify_type(
                f"{origin_name}[{', '.join(format_type(a) for a in args)}]"
            )
        return origin_name

    if hasattr(typ, "__name__"):
        return cast(str, typ.__name__)

    return simplify_type(str(typ).replace("typing.", ""))


# =============================================================================
# Extraction
# =============================================================================


def _full_description(parsed: Any) -> Optional[str]:
    """Build full description from parsed docstring (s
... [TRUNCATED]
```

### File: examples_DISTILLED.md
```md
---
id: examples
type: distilled_knowledge
---
# examples

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
## Examples

> Searching for community contributions! Join the [#contributing](https://discord.com/channels/1073293645303795742/1074711539724058635) Discord Channel to discuss.

This folder will contain an ever-growing set of examples.

The key with examples is that they should *always* work. The failure mode of examples folders is that they get quickly deprecated.

Examples are:
- Easy to maintain
- Easy to maintain examples are __simple__
- Use case examples are fine, technology is better

```
folder structure
- basic_functionality - notebooks with simple walkthroughs
- advanced_functionality - notebooks with advanced walkthroughs
- deployments - how to deploy places
- use_with - chroma + ___, where ___ can be langchain, nextjs, etc
- data - common data for examples
```

> 💡 Feel free to open a PR with an example you would like to see

### Basic Functionality
- [x] Examples of using different embedding models
- [x] Local persistance demo
- [x] Where filtering demo

### Advanced Functionality
- [ ] Clustering
- [ ] Projections
- [ ] Fine tuning

### Use With

#### LLM Application Code
- [ ] Langchain
- [ ] LlamaIndex
- [ ] Semantic Kernal

#### App Frameworks
- [ ] Streamlit
- [ ] Gradio
- [ ] Nextjs
- [ ] Rails
- [ ] FastAPI

#### Inference Services
- [ ] Brev.dev
- [ ] Banana.dev
- [ ] Modal

### LLM providers/services
- [ ] OpenAI
- [ ] Anthropic
- [ ] Cohere
- [ ] Google PaLM
- [ ] Hugging Face

***

### Inspiration
- The [OpenAI Cookbook](https://github.com/openai/openai-cookbook) gets a lot of things right

```

### File: task_api_example.py
```py
#!/usr/bin/env python3
"""
Example: Using Chroma's Attached Functions API to process collections automatically

This demonstrates how to attach functions that automatically process
collections as new records are added.
"""

import chromadb
import time
from chromadb.api.functions import RECORD_COUNTER_FUNCTION

# Connect to Chroma server
client = chromadb.HttpClient(host="localhost", port=8000)
# ignore error if collection does not exist
try:
    client.delete_collection("my_documents_counts")
except Exception:
    pass
# Create or get a collection
collection = client.get_or_create_collection(
    name="my_document", metadata={"description": "Sample documents for task processing"}
)

# Add some sample documents
collection.add(
    ids=["doc1", "doc2", "doc3"],
    documents=[
        "The quick brown fox jumps over the lazy dog",
        "Machine learning is a subset of artificial intelligence",
        "Python is a popular programming language",
    ],
    metadatas=[{"source": "proverb"}, {"source": "tech"}, {"source": "tech"}],
)

print(f"✅ Created collection '{collection.name}' with {collection.count()} documents")

# Attach a function that counts records in the collection
# The 'record_counter' function processes each record and outputs {"count": N}
attached_fn = collection.attach_function(
    function=RECORD_COUNTER_FUNCTION,
    name="count_my_docs",
    output_collection="my_documents_counts",
    params=None,
)

print("✅ Function attached successfully!")
print(f"   Attached Function ID: {attached_fn.id}")
print(f"   Name: {attached_fn.name}")
print(f"   Function: {attached_fn.function_name}")
print(f"   Input collection: {collection.name}")
print(f"   Output collection: {attached_fn.output_collection}")

# The function will now run automatically when:
# 1. New documents are added to 'my_documents'
# 2. The number of new records >= min_records_for_invocation (default: 100)

print("\n" + "=" * 60)
print("Function is now attached and will run on new data!")
print("=" * 60)

time.sleep(10)

# Add more documents to trigger function execution
print("\nAdding more documents...")
collection.add(
    ids=["doc4", "doc5"],
    documents=["Chroma is a vector database", "Functions automate data processing"],
)

print(f"Collection now has {collection.count()} documents")

# Later, you can detach the function
print("\n" + "=" * 60)
input("Press Enter to detach the function...")

success = collection.detach_function(
    attached_fn.name,
    delete_output_collection=True,  # Also delete the output collection
)

if success:
    print("✅ Function detached successfully!")
else:
    print("❌ Failed to detach function")

```


```

### File: pull_request_template.md
```md
## Description of changes

_Summarize the changes made by this PR._

- Improvements & Bug fixes
  - ...
- New functionality
  - ...

## Test plan

_How are these changes tested?_

- [ ] Tests pass locally with `pytest` for python, `yarn test` for js, `cargo test` for rust

## Migration plan

_Are there any migrations, or any forwards/backwards compatibility changes needed in order to make sure this change deploys reliably?_

## Observability plan

_What is the plan to instrument and monitor this change?_

## Documentation Changes

_Are all docstrings for user-facing APIs updated if required? Do we need to make documentation changes in the [docs section](https://github.com/chroma-core/chroma/tree/main/docs/docs.trychroma.com)?_

```

### File: RELEASE_PROCESS.md
```md
## Release Process

This guide covers how to release chroma to PyPi

#### Increase the version number
1. Create a new PR for the release that upgrades the version in code. Name it `release/A.B.C` In [this file](https://github.com/chroma-core/chroma/blob/main/chromadb/__init__.py) update the __ version __. The commit comment (and hence PR title) should be `[RELEASE] A.B.C`
```
__version__ = "A.B.C"
```
2. On Github, add the "release" label to this PR
3. Once the PR checks pass, merge it. This will trigger Github Actions to release to PyPi, DockerHub, and the JS client. It may take a while before they complete.
4. Once the PR is merged and the Github Actions complete, tag your commit SHA with the release version
```
git tag A.B.C <SHA>
```
5. Push your tag to origin to create the release. This will trigger more Github Actions to perform the release.
```
git push origin A.B.C
```
6. On the right panel on Github, click on "Releases", and the new release should appear first. Make sure it is marked as "latest".

```

### File: requirements_dev.txt
```txt
black==23.3.0 # match what's in pyproject.toml
build
chroma-hnswlib==0.7.6
fastapi>=0.115.9
grpcio-tools==1.67.1 # Later version not compatible with protobuf 4.25.5
httpx
hypothesis==6.112.2 # TODO: Resolve breaking changes and bump version
hypothesis[numpy]==6.112.2 # TODO: Resolve breaking changes and bump version
maturin>=1.0
mmh3
mypy-protobuf
opentelemetry-instrumentation-fastapi>=0.41b0
pandas
pre-commit
protobuf==5.28.0 # Later version not compatible with opentelemetry 1.27.0
psutil
pytest
pytest-asyncio
pytest-rerunfailures
pytest-xdist
setuptools_scm
snowballstemmer
types-protobuf

```

### File: .github\DEVELOP.md
```md
GitHub *still* does not support organizing workflows into directories, so instead we use some notation:

- A workflow starting with `_` is a reusable workflow and should exclusively have a `workflow_call` trigger.
- Any other workflow is expected to have standard triggers (e.g. `push`, `pull_request`, etc.) and should not be called by other workflows.

All workflows should be prefixed by their language name, e.g. `python-test.yml`.

```

### File: docs\scripts_DISTILLED.md
```md
---
id: scripts
type: distilled_knowledge
---
# scripts

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Documentation Generator Scripts

## Python Reference

Generate all split reference files into `docs/mintlify/reference/python/`:

```bash
uv run docs/scripts/generate_python_reference.py --output reference/python/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/python` and `/reference/python/index` redirect to `/reference/python/client`. The file `reference/python/where-filter.mdx` is maintained by hand (Python DSL only) and is not overwritten by the script.

## TypeScript Reference

Generate all split reference files into `docs/mintlify/reference/typescript/`:

```bash
bun run docs/scripts/generate_ts_reference.ts --output reference/typescript/
```

This produces `client.mdx`, `collection.mdx`, `embedding-functions.mdx`, `search.mdx`, and `schema.mdx`. There is no index page; `/reference/typescript` and `/reference/typescript/index` redirect to `/reference/typescript/client`. The file `reference/typescript/where-filter.mdx` is maintained by hand (TypeScript DSL only) and is not overwritten by the script.

```

### File: generate_python_reference.py
```py
#!/usr/bin/env python3
# /// script
# requires-python = ">=3.9"
# dependencies = [
#     "docstring-parser>=0.15",
#     "chromadb==1.5.0",
# ]
# ///
"""
Generate Python SDK reference documentation for Chroma.

Usage:
    uv run generate_python_reference.py --output reference/python/index.mdx

This script introspects the chromadb package and generates MDX documentation
with ParamField components for Mintlify.

To extend this script:
1. Add new sections to get_documentation_sections()
2. Add type simplifications to TYPE_SIMPLIFICATIONS
"""

from __future__ import annotations

import argparse
import inspect
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import (
    Any,
    Callable,
    Optional,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
)

from docstring_parser import parse as parse_docstring


# =============================================================================
# Configuration
# =============================================================================

TYPE_SIMPLIFICATIONS: dict[str, str] = {
    "ndarray": "Embedding",
    "Sequence[float]": "Embedding",
    "Sequence[int]": "Embedding",
    "List[Union[Sequence[float], Sequence[int]]]": "Embeddings",
    "Mapping[str, Union[str, int, float, bool, SparseVector, None]]": "Metadata",
    "List[Mapping[str, Union[str, int, float, bool, SparseVector, None]]]": "Metadatas",
}

TYPE_ALIASES: dict[str, str] = {
    "Union[str, List[str]]": "OneOrMany[str]",
    "Union[str, List[str], None]": "Optional[OneOrMany[str]]",
    "List[str]": "IDs",
    "Optional[List[str]]": "Optional[IDs]",
}


@dataclass
class SectionConfig:
    """Configuration for a documentation section."""

    title: str
    items: list[tuple[str, Any]] | list[str]
    source_class: Optional[type] = None
    render_mode: str = (
        "function"  # "function", "method", "class", "class_full", "type_alias"
    )
    output_file: str = "index"
    show_class_methods: bool = True


def get_documentation_sections() -> list[SectionConfig]:
    """Define all documentation sections with output_file for split generation."""
    import chromadb
    from chromadb.api import AdminAPI, ClientAPI
    from chromadb.api.models.Collection import Collection
    from chromadb.api.types import (
        BoolInvertedIndexConfig,
        Embedding,
        EmbeddingFunction,
        FloatInvertedIndexConfig,
        FtsIndexConfig,
        GetResult,
        HnswIndexConfig,
        IntInvertedIndexConfig,
        QueryResult,
        Schema,
        SearchResult,
        SparseEmbeddingFunction,
        SparseVectorIndexConfig,
        SpannIndexConfig,
        StringInvertedIndexConfig,
        VectorIndexConfig,
    )
    from chromadb.base_types import SparseVector
    from chromadb.execution.expression.operator import (
        GroupBy,
        Knn,
        Limit,
        MaxK,
        MinK,
        Rrf,
        Select,
    )
    from chromadb.execution.expression.plan import Search
    from chromadb.utils import embedding_functions as ef_module

    return [
        SectionConfig(
            title="Clients",
            render_mode="function",
            output_file="client",
            items=[
                ("EphemeralClient", chromadb.EphemeralClient),
                ("PersistentClient", chromadb.PersistentClient),
                ("HttpClient", chromadb.HttpClient),
                ("AsyncHttpClient", chromadb.AsyncHttpClient),
                ("CloudClient", chromadb.CloudClient),
                ("AdminClient", chromadb.AdminClient),
            ],
        ),
        SectionConfig(
            title="Client Methods",
            render_mode="method",
            source_class=ClientAPI,
            output_file="client",
            items=[
                "heartbeat",
                "list_collections",
                "count_collections",
                "create_collection",
                "get_collection",
                "get_or_create_collection",
                "delete_collection",
                "reset",
                "get_version",
                "get_settings",
                "get_max_batch_size",
            ],
        ),
        SectionConfig(
            title="Admin Client Methods",
            render_mode="method",
            source_class=AdminAPI,
            output_file="client",
            items=[
                "create_tenant",
                "get_tenant",
                "create_database",
                "get_database",
                "delete_database",
                "list_databases",
            ],
        ),
        SectionConfig(
            title="Collection Methods",
            render_mode="method",
            source_class=Collection,
            output_file="collection",
            items=[
                "count",
                "add",
                "get",
                "peek",
                "query",
                "modify",
                "update",
                "upsert",
                "delete",
            ],
        ),
        SectionConfig(
            title="Types",
            render_mode="class",
            output_file="collection",
            items=[
                ("GetResult", GetResult),
                ("QueryResult", QueryResult),
            ],
        ),
        SectionConfig(
            title="Embedding Function Base Classes",
            render_mode="class",
            output_file="embedding-functions",
            items=[
                ("EmbeddingFunction", EmbeddingFunction),
                ("SparseEmbeddingFunction", SparseEmbeddingFunction),
            ],
        ),
        SectionConfig(
            title="Registration",
            render_mode="function",
            output_file="embedding-functions",
            items=[
                ("register_embedding_function", ef_module.register_embedding_function),
                (
                    "register_sparse_embedding_function",
                    ef_module.register_sparse_embedding_function,
                ),
            ],
        ),
        SectionConfig(
            title="Types",
            render_mode="class",
            output_file="embedding-functions",
            items=[
                ("Embedding", Embedding),
                ("SparseVector", SparseVector),
            ],
        ),
        SectionConfig(
            title="Search",
            render_mode="class",
            output_file="search",
            items=[("Search", Search)],
        ),
        SectionConfig(
            title="Select",
            render_mode="class",
            output_file="search",
            items=[("Select", Select)],
        ),
        SectionConfig(
            title="Knn",
            render_mode="class",
            output_file="search",
            items=[("Knn", Knn)],
        ),
        SectionConfig(
            title="Rrf",
            render_mode="class",
            output_file="search",
            items=[("Rrf", Rrf)],
        ),
        SectionConfig(
            title="Group By",
            render_mode="class",
            output_file="search",
            items=[
                ("GroupBy", GroupBy),
                ("Limit", Limit),
                ("MinK", MinK),
                ("MaxK", MaxK),
            ],
        ),
        SectionConfig(
            title="SearchResult",
            render_mode="class",
            output_file="search",
            items=[("SearchResult", SearchResult)],
        ),
        SectionConfig(
            title="Schema",
            render_mode="class",
            output_file="schema",
            show_class_methods=False,
            items=[("Schema", Schema)],
        ),
        SectionConfig(
            title="Index configs",
            render_mode="class",
            output_file="schema",
            show_class_methods=False,
            items=[
                ("FtsIndexConfig", FtsIndexConfig),
                ("HnswIndexConfig", HnswIndexConfig),
                ("SpannIndexConfig", SpannIndexConfig),
                ("VectorIndexConfig", VectorIndexConfig),
                ("SparseVectorIndexConfig", SparseVectorIndexConfig),
                ("StringInvertedIndexConfig", StringInvertedIndexConfig),
                ("IntInvertedIndexConfig", IntInvertedIndexConfig),
                ("FloatInvertedIndexConfig", FloatInvertedIndexConfig),
                ("BoolInvertedIndexConfig", BoolInvertedIndexConfig),
            ],
        ),
    ]


# =============================================================================
# Data Model
# =============================================================================


@dataclass
class Param:
    """A parameter or property with type and optional description."""

    name: str
    type: str
    description: Optional[str] = None
    required: bool = False


@dataclass
class MethodDoc:
    """Documentation for a method."""

    name: str
    description: Optional[str] = None
    params: list[Param] = field(default_factory=list)
    returns: Optional[str] = None
    raises: list[str] = field(default_factory=list)
    is_async: bool = False


@dataclass
class FunctionDoc:
    """Documentation for a function."""

    name: str
    description: Optional[str] = None
    params: list[Param] = field(default_factory=list)
    returns: Optional[str] = None
    is_async: bool = False


@dataclass
class ClassDoc:
    """Documentation for a class."""

    name: str
    description: Optional[str] = None
    properties: list[Param] = field(default_factory=list)
    methods: list[MethodDoc] = field(default_factory=list)


# =============================================================================
# Type Formatting
# =============================================================================


def simplify_type(type_str: str) -> str:
    """Simplify complex type strings to more readable forms."""
    for pattern, replacement in TYPE_SIMPLIFICATIONS.items():
        if pattern in type_str:
            type_str = type_str.replace(pattern, replacement)

    for pattern, replacement in TYPE_ALIASES.items():
        if type_str == pattern:
            return replacement

    if "ForwardRef" in type_str:
        type_str = re.sub(r"ForwardRef\('(\w+)'\)", r"\1", type_str)

    if "Literal[" in type_str and type_str.count("Literal[") > 2:
        return "Where"

    if len(type_str) > 80:
        if "ndarray" in type_str.lower() or "embedding" in type_str.lower():
            return (
                "Optional[Embeddings]"
                if "List[" in type_str or "Union[" in type_str
                else "Optional[Embedding]"
            )
        if "Mapping" in type_str or "metadata" in type_str.lower():
            return (
                "Optional[Metadatas]" if "List[" in type_str else "Optional[Metadata]"
            )
        if "DataLoader" in type_str:
            return "Optional[DataLoader]"
        if "EmbeddingFunction" in type_str:
            return "Optional[EmbeddingFunction]"

    return type_str


def format_type(typ: Any) -> str:
    """Format a type annotation as a readable string."""
    if typ is None or typ is type(None):
        return "None"

    if isinstance(typ, str):
        return simplify_type(typ)

    origin = get_origin(typ)
    args = get_args(typ)

    if origin is Union:
        if len(args) == 2 and type(None) in args:
            inner = args[0] if args[1] is type(None) else args[1]
            return simplify_type(f"Optional[{format_type(inner)}]")
        return simplify_type(f"Union[{', '.join(format_type(a) for a in args)}]")

    if origin is not None:
        origin_name = getattr(origin, "__name__", str(origin))
        name_map = {"list": "List", "dict": "Dict", "tuple": "Tuple", "set": "Set"}
        origin_name = name_map.get(origin_name, origin_name)

        if args:
            return simplify_type(
                f"{origin_name}[{', '.join(format_type(a) for a in args)}]"
            )
        return origin_name

    if hasattr(typ, "__name__"):
        return cast(str, typ.__name__)

    return simplify_type(str(typ).replace("typing.", ""))


# =============================================================================
# Extraction
# =============================================================================


def _full_description(parsed: Any) -> Optional[str]:
    """Build full description from parsed docstring (short + long, paragraphs preserved)."""
    parts = []
    if getattr(parsed, "short_description", None):
        parts.append(parsed.short_description)
    if getattr(parsed, "long_description", None):
        parts.append(parsed.long_description)
    if not parts:
        return None
    return "\n\n".join(parts).strip() or None


def extract_function(fn: Callable[..., Any], name: Optional[str] = None) -> FunctionDoc:
    """Extract documentation from a function."""
    fn_name = name or fn.__name__

    try:
        sig = inspect.signature(fn)
    except (ValueError, TypeError):
        sig = None

    try:
        type_hints = get_type_hints(fn)
    except Exception:
        type_hints = {}

    doc = inspect.getdoc(fn) or ""
    parsed = parse_docstring(doc)

    description = _full_description(parsed)

    param_descs = {p.arg_name: p.description for p in parsed.params}

    params = []
    if sig:
        for param_name, param in sig.parameters.items():
            if param_name in ("self", "cls"):
                continue

            param_type = type_hints.get(param_name, param.annotation)
            if param_type is inspect.Parameter.empty:
                param_type = "Any"

            params.append(
                Param(
                    name=
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
