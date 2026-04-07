---
id: fastapi
type: knowledge
owner: OA_Triage
---
# fastapi
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <a href="https://fastapi.tiangolo.com"><img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI"></a>
</p>
<p align="center">
    <em>FastAPI framework, high performance, easy to learn, fast to code, ready for production</em>
</p>
<p align="center">
<a href="https://github.com/fastapi/fastapi/actions?query=workflow%3ATest+event%3Apush+branch%3Amaster">
    <img src="https://github.com/fastapi/fastapi/actions/workflows/test.yml/badge.svg?event=push&branch=master" alt="Test">
</a>
<a href="https://coverage-badge.samuelcolvin.workers.dev/redirect/fastapi/fastapi">
    <img src="https://coverage-badge.samuelcolvin.workers.dev/fastapi/fastapi.svg" alt="Coverage">
</a>
<a href="https://pypi.org/project/fastapi">
    <img src="https://img.shields.io/pypi/v/fastapi?color=%2334D058&label=pypi%20package" alt="Package version">
</a>
<a href="https://pypi.org/project/fastapi">
    <img src="https://img.shields.io/pypi/pyversions/fastapi.svg?color=%2334D058" alt="Supported Python versions">
</a>
</p>

---

**Documentation**: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)

**Source Code**: [https://github.com/fastapi/fastapi](https://github.com/fastapi/fastapi)

---

FastAPI is a modern, fast (high-performance), web framework for building APIs with Python based on standard Python type hints.

The key features are:

* **Fast**: Very high performance, on par with **NodeJS** and **Go** (thanks to Starlette and Pydantic). [One of the fastest Python frameworks available](#performance).
* **Fast to code**: Increase the speed to develop features by about 200% to 300%. *
* **Fewer bugs**: Reduce about 40% of human (developer) induced errors. *
* **Intuitive**: Great editor support. <dfn title="also known as auto-complete, autocompletion, IntelliSense">Completion</dfn> everywhere. Less time debugging.
* **Easy**: Designed to be easy to use and learn. Less time reading docs.
* **Short**: Minimize code duplication. Multiple features from each parameter declaration. Fewer bugs.
* **Robust**: Get production-ready code. With automatic interactive documentation.
* **Standards-based**: Based on (and fully compatible with) the open standards for APIs: [OpenAPI](https://github.com/OAI/OpenAPI-Specification) (previously known as Swagger) and [JSON Schema](https://json-schema.org/).

<small>* estimation based on tests conducted by an internal development team, building production applications.</small>

## Sponsors

<!-- sponsors -->
### Keystone Sponsor

<a href="https://fastapicloud.com" target="_blank" title="FastAPI Cloud. By the same team behind FastAPI. You code. We Cloud."><img src="https://fastapi.tiangolo.com/img/sponsors/fastapicloud.png"></a>

### Gold and Silver Sponsors

<a href="https://blockbee.io?ref=fastapi" target="_blank" title="BlockBee Cryptocurrency Payment Gateway"><img src="https://fastapi.tiangolo.com/img/sponsors/blockbee.png"></a>
<a href="https://github.com/scalar/scalar/?utm_source=fastapi&utm_medium=website&utm_campaign=main-badge" target="_blank" title="Scalar: Beautiful Open-Source API References from Swagger/OpenAPI files"><img src="https://fastapi.tiangolo.com/img/sponsors/scalar.svg"></a>
<a href="https://www.propelauth.com/?utm_source=fastapi&utm_campaign=1223&utm_medium=mainbadge" target="_blank" title="Auth, user management and more for your B2B product"><img src="https://fastapi.tiangolo.com/img/sponsors/propelauth.png"></a>
<a href="https://zuplo.link/fastapi-gh" target="_blank" title="Zuplo: Deploy, Secure, Document, and Monetize your FastAPI"><img src="https://fastapi.tiangolo.com/img/sponsors/zuplo.png"></a>
<a href="https://liblab.com?utm_source=fastapi" target="_blank" title="liblab - Generate SDKs from FastAPI"><img src="https://fastapi.tiangolo.com/img/sponsors/liblab.png"></a>
<a href="https://docs.render.com/deploy-fastapi?utm_source=deploydoc&utm_medium=referral&utm_campaign=fastapi" target="_blank" title="Deploy & scale any full-stack web app on Render. Focus on building apps, not infra."><img src="https://fastapi.tiangolo.com/img/sponsors/render.svg"></a>
<a href="https://www.coderabbit.ai/?utm_source=fastapi&utm_medium=badge&utm_campaign=fastapi" target="_blank" title="Cut Code Review Time & Bugs in Half with CodeRabbit"><img src="https://fastapi.tiangolo.com/img/sponsors/coderabbit.png"></a>
<a href="https://subtotal.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=open-source" target="_blank" title="The Gold Standard in Retail Account Linking"><img src="https://fastapi.tiangolo.com/img/sponsors/subtotal.svg"></a>
<a href="https://docs.railway.com/guides/fastapi?utm_medium=integration&utm_source=docs&utm_campaign=fastapi" target="_blank" title="Deploy enterprise applications at startup speed"><img src="https://fastapi.tiangolo.com/img/sponsors/railway.png"></a>
<a href="https://serpapi.com/?utm_source=fastapi_website" target="_blank" title="SerpApi: Web Search API"><img src="https://fastapi.tiangolo.com/img/sponsors/serpapi.png"></a>
<a href="https://www.greptile.com/?utm_source=fastapi&utm_medium=sponsorship&utm_campaign=fastapi_sponsor_page" target="_blank" title="Greptile: The AI Code Reviewer"><img src="https://fastapi.tiangolo.com/img/sponsors/greptile.png"></a>
<a href="https://databento.com/?utm_source=fastapi&utm_medium=sponsor&utm_content=display" target="_blank" title="Pay as you go for market data"><img src="https://fastapi.tiangolo.com/img/sponsors/databento.svg"></a>
<a href="https://speakeasy.com/editor?utm_source=fastapi+repo&utm_medium=github+sponsorship" target="_blank" title="SDKs for your API | Speakeasy"><img src="https://fastapi.tiangolo.com/img/sponsors/speakeasy.png"></a>
<a href="https://www.svix.com/" target="_blank" title="Svix - Webhooks as a service"><img src="https://fastapi.tiangolo.com/img/sponsors/svix.svg"></a>
<a href="https://www.stainlessapi.com/?utm_source=fastapi&utm_medium=referral" target="_blank" title="Stainless | Generate best-in-class SDKs"><img src="https://fastapi.tiangolo.com/img/sponsors/stainless.png"></a>
<a href="https://www.permit.io/blog/implement-authorization-in-fastapi?utm_source=github&utm_medium=referral&utm_campaign=fastapi" target="_blank" title="Fine-Grained Authorization for FastAPI"><img src="https://fastapi.tiangolo.com/img/sponsors/permit.png"></a>
<a href="https://www.interviewpal.com/?utm_source=fastapi&utm_medium=open-source&utm_campaign=dev-hiring" target="_blank" title="InterviewPal - AI Interview Coach for Engineers and Devs"><img src="https://fastapi.tiangolo.com/img/sponsors/interviewpal.png"></a>
<a href="https://dribia.com/en/" target="_blank" title="Dribia - Data Science within your reach"><img src="https://fastapi.tiangolo.com/img/sponsors/dribia.png"></a>

<!-- /sponsors -->

[Other sponsors](https://fastapi.tiangolo.com/fastapi-people/#sponsors)

## Opinions

"_[...] I'm using **FastAPI** a ton these days. [...] I'm actually planning to use it for all of my team's **ML services at Microsoft**. Some of them are getting integrated into the core **Windows** product and some **Office** products._"

<div style="text-align: right; margin-right: 10%;">Kabir Khan - <strong>Microsoft</strong> <a href="https://github.com/fastapi/fastapi/pull/26"><small>(ref)</small></a></div>

---

"_We adopted the **FastAPI** library to spawn a **REST** server that can be queried to obtain **predictions**. [for Ludwig]_"

<div style="text-align: right; margin-right: 10%;">Piero Molino, Yaroslav Dudin, and Sai Sumanth Miryala - <strong>Uber</strong> <a href="https://eng.uber.com/ludwig-v0-2/"><small>(ref)</small></a></div>

---

"_**Netflix** is pleased to announce the open-source release of our **crisis management** orchestration framework: **Dispatch**! [built with **FastAPI**]_"

<div style="text-align: right; margin-right: 10%;">Kevin Glisson, Marc Vilanova, Forest Monsen - <strong>Netflix</strong> <a href="https://netflixtechblog.com/introducing-dispatch-da4b8a2a8072"><small>(ref)</small></a></div>

---

"_I’m over the moon excited about **FastAPI**. It’s so fun!_"

<div style="text-align: right; margin-right: 10%;">Brian Okken - <strong>[Python Bytes](https://pythonbytes.fm/episodes/show/123/time-to-right-the-py-wrongs?time_in_sec=855) podcast host</strong> <a href="https://x.com/brianokken/status/1112220079972728832"><small>(ref)</small></a></div>

---

"_Honestly, what you've built looks super solid and polished. In many ways, it's what I wanted **Hug** to be - it's really inspiring to see someone build that._"

<div style="text-align: right; margin-right: 10%;">Timothy Crosley - <strong>[Hug](https://github.com/hugapi/hug) creator</strong> <a href="https://news.ycombinator.com/item?id=19455465"><small>(ref)</small></a></div>

---

"_If you're looking to learn one **modern framework** for building REST APIs, check out **FastAPI** [...] It's fast, easy to use and easy to learn [...]_"

"_We've switched over to **FastAPI** for our **APIs** [...] I think you'll like it [...]_"

<div style="text-align: right; margin-right: 10%;">Ines Montani - Matthew Honnibal - <strong>[Explosion AI](https://explosion.ai) founders - [spaCy](https://spacy.io) creators</strong> <a href="https://x.com/_inesmontani/status/1144173225322143744"><small>(ref)</small></a> - <a href="https://x.com/honnibal/status/1144031421859655680"><small>(ref)</small></a></div>

---

"_If anyone is looking to build a production Python API, I would highly recommend **FastAPI**. It is **beautifully designed**, **simple to use** and **highly scalable**, it has become a **key component** in our API first development strategy and is driving many automations and services such as our Virtual TAC Engineer._"

<div style="text-align: right; margin-right: 10%;">Deon Pillsbury - <strong>Cisco</strong> <a href="https://www.linkedin.com/posts/deonpillsbury_cisco-cx-python-activity-6963242628536487936-trAp/"><small>(ref)</small></a></div>

---

## FastAPI mini documentary

There's a [FastAPI mini documentary](https://www.youtube.com/watch?v=mpR8ngthqiE) released at the end of 2025, you can watch it online:

<a href="https://www.youtube.com/watch?v=mpR8ngthqiE"><img src="https://fastapi.tiangolo.com/img/fastapi-documentary.jpg" alt="FastAPI Mini Documentary"></a>

## **Typer**, the FastAPI of CLIs

<a href="https://typer.tiangolo.com"><img src="https://typer.tiangolo.com/img/logo-margin/logo-margin-vector.svg" style="width: 20%;"></a>

If you are building a <abbr title="Command Line Interface">CLI</abbr> app to be used in the terminal instead of a web API, check out [**Typer**](https://typer.tiangolo.com/).

**Typer** is FastAPI's little sibling. And it's intended to be the **FastAPI of CLIs**. ⌨️ 🚀

## Requirements

FastAPI stands on the shoulders of giants:

* [Starlette](https://www.starlette.dev/) for the web parts.
* [Pydantic](https://docs.pydantic.dev/) for the data parts.

## Installation

Create and activate a [virtual environment](https://fastapi.tiangolo.com/virtual-environments/) and then install FastAPI:

<div class="termy">

```console
$ pip install "fastapi[standard]"

---> 100%
```

</div>

**Note**: Make sure you put `"fastapi[standard]"` in quotes to ensure it works in all terminals.

## Example

### Create it

Create a file `main.py` with:

```Python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

<details markdown="1">
<summary>Or use <code>async def</code>...</summary>

If your code uses `async` / `await`, use `async def`:

```Python hl_lines="7  12"
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

**Note**:

If you don't know, check the _"In a hurry?"_ section about [`async` and `await` in the docs](https://fastapi.tiangolo.com/async/#in-a-hurry).

</details>

### Run it

Run the server with:

<div class="termy">

```console
$ fastapi dev

 ╭────────── FastAPI CLI - Development mode ───────────╮
 │                                                     │
 │  Serving at: http://127.0.0.1:8000                  │
 │                                                     │
 │  API docs: http://127.0.0.1:8000/docs               │
 │                                                     │
 │  Running in development mode, for production use:   │
 │                                                     │
 │  fastapi run                                        │
 │                                                     │
 ╰─────────────────────────────────────────────────────╯

INFO:     Will watch for changes in these directories: ['/home/user/code/awesomeapp']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [2248755] using WatchFiles
INFO:     Started server process [2248757]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

</div>

<details markdown="1">
<summary>About the command <code>fastapi dev</code>...</summary>

The command `fastapi dev` reads your `main.py` file automatically, detects the **FastAPI** app in it, and starts a server using [Uvicorn](https://www.uvicorn.dev).

By default, `fastapi dev` will start with auto-reload enabled for local development.

You can read more about it in the [FastAPI CLI docs](https://fastapi.tiangolo.com/fastapi-cli/).

</details>

### Check it

Open your browser at [http://127.0.0.1:8000/items/5?q=somequery](http://127.0.0.1:8000/items/5?q=somequery).

You will see the JSON response as:

```JSON
{"item_id": 5, "q": "somequery"}
```

You already created an API that:

* Receives HTTP requests in the _paths_ `/` and `/items/{item_id}`.
* Both _paths_ take `GET` <em>operations</em> (also known as HTTP _methods_).
* The _path_ `/items/{item_id}` has a _path parameter_ `item_id` that should be an `int`.
* The _path_ `/items/{item_id}` has an optional `str` _query parameter_ `q`.

### Interactive API docs

Now go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

You will see the automatic interactive API documentation (provided by [Swagger UI](https://github.com/swagger-api/swagger-ui)):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### Alternative API docs

And now, go to [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc).

You will see the alternative automatic documentation (provided by [ReDoc](https://github.com/Rebilly/ReDoc)):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)

## Example upgrade

Now modify the file `main.py` to receive a body from a `PUT` request.

Declare the body using standard Python types, thanks to Pydantic.

```Python hl_lines="2  7-10 23-25"
from fastapi import FastAPI
from pydantic import Bas
... [TRUNCATED]
```

### File: tests\main.py
```py
import http

from fastapi import FastAPI, Path, Query

external_docs = {
    "description": "External API documentation.",
    "url": "https://docs.example.com/api-general",
}

app = FastAPI(openapi_external_docs=external_docs)


@app.api_route("/api_route")
def non_operation():
    return {"message": "Hello World"}


def non_decorated_route():
    return {"message": "Hello World"}


app.add_api_route("/non_decorated_route", non_decorated_route)


@app.get("/text")
def get_text():
    return "Hello World"


@app.get("/path/{item_id}")
def get_id(item_id):
    return item_id


@app.get("/path/str/{item_id}")
def get_str_id(item_id: str):
    return item_id


@app.get("/path/int/{item_id}")
def get_int_id(item_id: int):
    return item_id


@app.get("/path/float/{item_id}")
def get_float_id(item_id: float):
    return item_id


@app.get("/path/bool/{item_id}")
def get_bool_id(item_id: bool):
    return item_id


@app.get("/path/param/{item_id}")
def get_path_param_id(item_id: str | None = Path()):
    return item_id


@app.get("/path/param-minlength/{item_id}")
def get_path_param_min_length(item_id: str = Path(min_length=3)):
    return item_id


@app.get("/path/param-maxlength/{item_id}")
def get_path_param_max_length(item_id: str = Path(max_length=3)):
    return item_id


@app.get("/path/param-min_maxlength/{item_id}")
def get_path_param_min_max_length(item_id: str = Path(max_length=3, min_length=2)):
    return item_id


@app.get("/path/param-gt/{item_id}")
def get_path_param_gt(item_id: float = Path(gt=3)):
    return item_id


@app.get("/path/param-gt0/{item_id}")
def get_path_param_gt0(item_id: float = Path(gt=0)):
    return item_id


@app.get("/path/param-ge/{item_id}")
def get_path_param_ge(item_id: float = Path(ge=3)):
    return item_id


@app.get("/path/param-lt/{item_id}")
def get_path_param_lt(item_id: float = Path(lt=3)):
    return item_id


@app.get("/path/param-lt0/{item_id}")
def get_path_param_lt0(item_id: float = Path(lt=0)):
    return item_id


@app.get("/path/param-le/{item_id}")
def get_path_param_le(item_id: float = Path(le=3)):
    return item_id


@app.get("/path/param-lt-gt/{item_id}")
def get_path_param_lt_gt(item_id: float = Path(lt=3, gt=1)):
    return item_id


@app.get("/path/param-le-ge/{item_id}")
def get_path_param_le_ge(item_id: float = Path(le=3, ge=1)):
    return item_id


@app.get("/path/param-lt-int/{item_id}")
def get_path_param_lt_int(item_id: int = Path(lt=3)):
    return item_id


@app.get("/path/param-gt-int/{item_id}")
def get_path_param_gt_int(item_id: int = Path(gt=3)):
    return item_id


@app.get("/path/param-le-int/{item_id}")
def get_path_param_le_int(item_id: int = Path(le=3)):
    return item_id


@app.get("/path/param-ge-int/{item_id}")
def get_path_param_ge_int(item_id: int = Path(ge=3)):
    return item_id


@app.get("/path/param-lt-gt-int/{item_id}")
def get_path_param_lt_gt_int(item_id: int = Path(lt=3, gt=1)):
    return item_id


@app.get("/path/param-le-ge-int/{item_id}")
def get_path_param_le_ge_int(item_id: int = Path(le=3, ge=1)):
    return item_id


@app.get("/query")
def get_query(query):
    return f"foo bar {query}"


@app.get("/query/optional")
def get_query_optional(query=None):
    if query is None:
        return "foo bar"
    return f"foo bar {query}"


@app.get("/query/int")
def get_query_type(query: int):
    return f"foo bar {query}"


@app.get("/query/int/optional")
def get_query_type_optional(query: int | None = None):
    if query is None:
        return "foo bar"
    return f"foo bar {query}"


@app.get("/query/int/default")
def get_query_type_int_default(query: int = 10):
    return f"foo bar {query}"


@app.get("/query/param")
def get_query_param(query=Query(default=None)):
    if query is None:
        return "foo bar"
    return f"foo bar {query}"


@app.get("/query/param-required")
def get_query_param_required(query=Query()):
    return f"foo bar {query}"


@app.get("/query/param-required/int")
def get_query_param_required_type(query: int = Query()):
    return f"foo bar {query}"


@app.get("/enum-status-code", status_code=http.HTTPStatus.CREATED)
def get_enum_status_code():
    return "foo bar"


@app.get("/query/frozenset")
def get_query_type_frozenset(query: frozenset[int] = Query(...)):
    return ",".join(map(str, sorted(query)))


@app.get("/query/list")
def get_query_list(device_ids: list[int] = Query()) -> list[int]:
    return device_ids


@app.get("/query/list-default")
def get_query_list_default(device_ids: list[int] = Query(default=[])) -> list[int]:
    return device_ids

```

### File: .pre-commit-config.yaml
```yaml
# See https://pre-commit.com for more information
# See https://pre-commit.com/hooks.html for more hooks
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v6.0.0
    hooks:
      - id: check-added-large-files
        args: ['--maxkb=750']
        exclude: ^uv.lock$
      - id: check-toml
      - id: check-yaml
        args:
        - --unsafe
      - id: end-of-file-fixer
      - id: trailing-whitespace

  - repo: local
    hooks:
      - id: local-ruff-check
        name: ruff check
        entry: uv run ruff check --force-exclude --fix --exit-non-zero-on-fix
        require_serial: true
        language: unsupported
        types: [python]

      - id: local-ruff-format
        name: ruff format
        entry: uv run ruff format --force-exclude --exit-non-zero-on-format
        require_serial: true
        language: unsupported
        types: [python]

      - id: local-mypy
        name: mypy check
        entry: uv run mypy fastapi
        require_serial: true
        language: unsupported
        pass_filenames: false

      - id: local-ty
        name: ty check
        entry: uv run ty check fastapi
        require_serial: true
        language: unsupported
        pass_filenames: false

      - id: add-permalinks-pages
        language: unsupported
        name: add-permalinks-pages
        entry: uv run ./scripts/docs.py add-permalinks-pages
        args:
          - --update-existing
        files: ^docs/en/docs/.*\.md$

      - id: generate-readme
        language: unsupported
        name: generate README.md from index.md
        entry: uv run ./scripts/docs.py generate-readme
        files: ^docs/en/docs/index\.md|docs/en/data/sponsors\.yml|scripts/docs\.py$
        pass_filenames: false

      - id: update-languages
        language: unsupported
        name: update languages
        entry: uv run ./scripts/docs.py update-languages
        files: ^docs/.*|scripts/docs\.py$
        pass_filenames: false

      - id: ensure-non-translated
        language: unsupported
        name: ensure non-translated files are not modified
        entry: uv run ./scripts/docs.py ensure-non-translated
        files: ^docs/(?!en/).*|^scripts/docs\.py$
        pass_filenames: false

      - id: fix-translations
        language: unsupported
        name: fix translations
        entry: uv run ./scripts/translation_fixer.py fix-pages
        files: ^docs/(?!en/).*/docs/.*\.md$

      - id: add-release-date
        language: unsupported
        name: add date to latest release header
        entry: uv run python scripts/add_latest_release_date.py
        files: ^docs/en/docs/release-notes\.md$
        pass_filenames: false

```

### File: CONTRIBUTING.md
```md
Please read the [Development - Contributing](https://fastapi.tiangolo.com/contributing/) guidelines in the documentation site.

```

### File: SECURITY.md
```md
# Security Policy

Security is very important for FastAPI and its community. 🔒

Learn more about it below. 👇

## Versions

The latest version of FastAPI is supported.

You are encouraged to [write tests](https://fastapi.tiangolo.com/tutorial/testing/) for your application and update your FastAPI version frequently after ensuring that your tests are passing. This way you will benefit from the latest features, bug fixes, and **security fixes**.

You can learn more about [FastAPI versions and how to pin and upgrade them](https://fastapi.tiangolo.com/deployment/versions/) for your project in the docs.

## Reporting a Vulnerability

If you think you found a vulnerability, and even if you are not sure about it, please report it right away by sending an email to: security@tiangolo.com. Please try to be as explicit as possible, describing all the steps and example code to reproduce the security issue.

I (the author, [@tiangolo](https://x.com/tiangolo)) will review it thoroughly and get back to you.

## Public Discussions

Please restrain from publicly discussing a potential security vulnerability. 🙊

It's better to discuss privately and try to find a solution first, to limit the potential impact as much as possible.

---

Thanks for your help!

The FastAPI community and I thank you for that. 🙇

```

### File: docs\missing-translation.md
```md
/// warning

This page hasn’t been translated into your language yet. 🌍

We’re currently switching to an automated translation system 🤖, which will help keep all translations complete and up to date.

Learn more: [Contributing - Translations](https://fastapi.tiangolo.com/contributing/#translations){.internal-link target=_blank}

///

```

### File: scripts\add_latest_release_date.py
```py
"""Check release-notes.md and add today's date to the latest release header if missing."""

import re
import sys
from datetime import date

RELEASE_NOTES_FILE = "docs/en/docs/release-notes.md"
RELEASE_HEADER_PATTERN = re.compile(r"^## (\d+\.\d+\.\d+)\s*(\(.*\))?\s*$")


def main() -> None:
    with open(RELEASE_NOTES_FILE) as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        match = RELEASE_HEADER_PATTERN.match(line)
        if not match:
            continue

        version = match.group(1)
        date_part = match.group(2)

        if date_part:
            print(f"Latest release {version} already has a date: {date_part}")
            sys.exit(0)

        today = date.today().isoformat()
        lines[i] = f"## {version} ({today})\n"
        print(f"Added date: {version} ({today})")

        with open(RELEASE_NOTES_FILE, "w") as f:
            f.writelines(lines)
        sys.exit(0)

    print("No release header found")
    sys.exit(1)


if __name__ == "__main__":
    main()

```

### File: scripts\contributors.py
```py
import logging
import secrets
import subprocess
from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any

import httpx
import yaml
from github import Github
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings

github_graphql_url = "https://api.github.com/graphql"


prs_query = """
query Q($after: String) {
  repository(name: "fastapi", owner: "fastapi") {
    pullRequests(first: 100, after: $after) {
      edges {
        cursor
        node {
          number
          labels(first: 100) {
            nodes {
              name
            }
          }
          author {
            login
            avatarUrl
            url
          }
          title
          createdAt
          lastEditedAt
          updatedAt
          state
          reviews(first:100) {
            nodes {
              author {
                login
                avatarUrl
                url
              }
              state
            }
          }
        }
      }
    }
  }
}
"""


class Author(BaseModel):
    login: str
    avatarUrl: str
    url: str


class LabelNode(BaseModel):
    name: str


class Labels(BaseModel):
    nodes: list[LabelNode]


class ReviewNode(BaseModel):
    author: Author | None = None
    state: str


class Reviews(BaseModel):
    nodes: list[ReviewNode]


class PullRequestNode(BaseModel):
    number: int
    labels: Labels
    author: Author | None = None
    title: str
    createdAt: datetime
    lastEditedAt: datetime | None = None
    updatedAt: datetime | None = None
    state: str
    reviews: Reviews


class PullRequestEdge(BaseModel):
    cursor: str
    node: PullRequestNode


class PullRequests(BaseModel):
    edges: list[PullRequestEdge]


class PRsRepository(BaseModel):
    pullRequests: PullRequests


class PRsResponseData(BaseModel):
    repository: PRsRepository


class PRsResponse(BaseModel):
    data: PRsResponseData


class Settings(BaseSettings):
    github_token: SecretStr
    github_repository: str
    httpx_timeout: int = 30


def get_graphql_response(
    *,
    settings: Settings,
    query: str,
    after: str | None = None,
) -> dict[str, Any]:
    headers = {"Authorization": f"token {settings.github_token.get_secret_value()}"}
    variables = {"after": after}
    response = httpx.post(
        github_graphql_url,
        headers=headers,
        timeout=settings.httpx_timeout,
        json={"query": query, "variables": variables, "operationName": "Q"},
    )
    if response.status_code != 200:
        logging.error(f"Response was not 200, after: {after}")
        logging.error(response.text)
        raise RuntimeError(response.text)
    data = response.json()
    if "errors" in data:
        logging.error(f"Errors in response, after: {after}")
        logging.error(data["errors"])
        logging.error(response.text)
        raise RuntimeError(response.text)
    return data


def get_graphql_pr_edges(
    *, settings: Settings, after: str | None = None
) -> list[PullRequestEdge]:
    data = get_graphql_response(settings=settings, query=prs_query, after=after)
    graphql_response = PRsResponse.model_validate(data)
    return graphql_response.data.repository.pullRequests.edges


def get_pr_nodes(settings: Settings) -> list[PullRequestNode]:
    pr_nodes: list[PullRequestNode] = []
    pr_edges = get_graphql_pr_edges(settings=settings)

    while pr_edges:
        for edge in pr_edges:
            pr_nodes.append(edge.node)
        last_edge = pr_edges[-1]
        pr_edges = get_graphql_pr_edges(settings=settings, after=last_edge.cursor)
    return pr_nodes


class ContributorsResults(BaseModel):
    contributors: Counter[str]
    translation_reviewers: Counter[str]
    translators: Counter[str]
    authors: dict[str, Author]


def get_contributors(pr_nodes: list[PullRequestNode]) -> ContributorsResults:
    contributors = Counter[str]()
    translation_reviewers = Counter[str]()
    translators = Counter[str]()
    authors: dict[str, Author] = {}

    for pr in pr_nodes:
        if pr.author:
            authors[pr.author.login] = pr.author
        is_lang = False
        for label in pr.labels.nodes:
            if label.name == "lang-all":
                is_lang = True
                break
        for review in pr.reviews.nodes:
            if review.author:
                authors[review.author.login] = review.author
                if is_lang:
                    translation_reviewers[review.author.login] += 1
        if pr.state == "MERGED" and pr.author:
            if is_lang:
                translators[pr.author.login] += 1
            else:
                contributors[pr.author.login] += 1
    return ContributorsResults(
        contributors=contributors,
        translation_reviewers=translation_reviewers,
        translators=translators,
        authors=authors,
    )


def get_users_to_write(
    *,
    counter: Counter[str],
    authors: dict[str, Author],
    min_count: int = 2,
) -> dict[str, Any]:
    users: dict[str, Any] = {}
    for user, count in counter.most_common():
        if count >= min_count:
            author = authors[user]
            users[user] = {
                "login": user,
                "count": count,
                "avatarUrl": author.avatarUrl,
                "url": author.url,
            }
    return users


def update_content(*, content_path: Path, new_content: Any) -> bool:
    old_content = content_path.read_text(encoding="utf-8")

    new_content = yaml.dump(new_content, sort_keys=False, width=200, allow_unicode=True)
    if old_content == new_content:
        logging.info(f"The content hasn't changed for {content_path}")
        return False
    content_path.write_text(new_content, encoding="utf-8")
    logging.info(f"Updated {content_path}")
    return True


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    settings = Settings()
    logging.info(f"Using config: {settings.model_dump_json()}")
    g = Github(settings.github_token.get_secret_value())
    repo = g.get_repo(settings.github_repository)

    pr_nodes = get_pr_nodes(settings=settings)
    contributors_results = get_contributors(pr_nodes=pr_nodes)
    authors = contributors_results.authors

    top_contributors = get_users_to_write(
        counter=contributors_results.contributors,
        authors=authors,
    )

    top_translators = get_users_to_write(
        counter=contributors_results.translators,
        authors=authors,
    )
    top_translations_reviewers = get_users_to_write(
        counter=contributors_results.translation_reviewers,
        authors=authors,
    )

    # For local development
    # contributors_path = Path("../docs/en/data/contributors.yml")
    contributors_path = Path("./docs/en/data/contributors.yml")
    # translators_path = Path("../docs/en/data/translators.yml")
    translators_path = Path("./docs/en/data/translators.yml")
    # translation_reviewers_path = Path("../docs/en/data/translation_reviewers.yml")
    translation_reviewers_path = Path("./docs/en/data/translation_reviewers.yml")

    updated = [
        update_content(content_path=contributors_path, new_content=top_contributors),
        update_content(content_path=translators_path, new_content=top_translators),
        update_content(
            content_path=translation_reviewers_path,
            new_content=top_translations_reviewers,
        ),
    ]

    if not any(updated):
        logging.info("The data hasn't changed, finishing.")
        return

    logging.info("Setting up GitHub Actions git user")
    subprocess.run(["git", "config", "user.name", "github-actions[bot]"], check=True)
    subprocess.run(
        ["git", "config", "user.email", "github-actions[bot]@users.noreply.github.com"],
        check=True,
    )
    branch_name = f"fastapi-people-contributors-{secrets.token_hex(4)}"
    logging.info(f"Creating a new branch {branch_name}")
    subprocess.run(["git", "checkout", "-b", branch_name], check=True)
    logging.info("Adding updated file")
    subprocess.run(
        [
            "git",
            "add",
            str(contributors_path),
            str(translators_path),
            str(translation_reviewers_path),
        ],
        check=True,
    )
    logging.info("Committing updated file")
    message = "👥 Update FastAPI People - Contributors and Translators"
    subprocess.run(["git", "commit", "-m", message], check=True)
    logging.info("Pushing branch")
    subprocess.run(["git", "push", "origin", branch_name], check=True)
    logging.info("Creating PR")
    pr = repo.create_pull(title=message, body=message, base="master", head=branch_name)
    logging.info(f"Created PR: {pr.number}")
    logging.info("Finished")


if __name__ == "__main__":
    main()

```

### File: scripts\coverage.sh
```sh
#!/usr/bin/env bash

set -e
set -x

coverage combine
coverage report
coverage html

```

### File: scripts\deploy_docs_status.py
```py
import logging
import re
from typing import Literal

from github import Auth, Github
from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    github_repository: str
    github_token: SecretStr
    deploy_url: str | None = None
    commit_sha: str
    run_id: int
    state: Literal["pending", "success", "error"] = "pending"


class LinkData(BaseModel):
    previous_link: str
    preview_link: str
    en_link: str | None = None


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    settings = Settings()

    logging.info(f"Using config: {settings.model_dump_json()}")
    g = Github(auth=Auth.Token(settings.github_token.get_secret_value()))
    repo = g.get_repo(settings.github_repository)
    use_pr = next(
        (pr for pr in repo.get_pulls() if pr.head.sha == settings.commit_sha), None
    )
    if not use_pr:
        logging.error(f"No PR found for hash: {settings.commit_sha}")
        return
    commits = list(use_pr.get_commits())
    current_commit = [c for c in commits if c.sha == settings.commit_sha][0]
    run_url = f"https://github.com/{settings.github_repository}/actions/runs/{settings.run_id}"
    if settings.state == "pending":
        current_commit.create_status(
            state="pending",
            description="Deploying Docs",
            context="deploy-docs",
            target_url=run_url,
        )
        logging.info("No deploy URL available yet")
        return
    if settings.state == "error":
        current_commit.create_status(
            state="error",
            description="Error Deploying Docs",
            context="deploy-docs",
            target_url=run_url,
        )
        logging.info("Error deploying docs")
        return
    assert settings.state == "success"
    if not settings.deploy_url:
        current_commit.create_status(
            state="success",
            description="No Docs Changes",
            context="deploy-docs",
            target_url=run_url,
        )
        logging.info("No docs changes found")
        return
    assert settings.deploy_url
    current_commit.create_status(
        state="success",
        description="Docs Deployed",
        context="deploy-docs",
        target_url=run_url,
    )

    files = list(use_pr.get_files())
    docs_files = [f for f in files if f.filename.startswith("docs/")]

    deploy_url = settings.deploy_url.rstrip("/")
    lang_links: dict[str, list[LinkData]] = {}
    for f in docs_files:
        match = re.match(r"docs/([^/]+)/docs/(.*)", f.filename)
        if not match:
            continue
        lang = match.group(1)
        path = match.group(2)
        if path.endswith("index.md"):
            path = path.replace("index.md", "")
        else:
            path = path.replace(".md", "/")
        en_path = path
        if lang == "en":
            use_path = en_path
        else:
            use_path = f"{lang}/{path}"
        link = LinkData(
            previous_link=f"https://fastapi.tiangolo.com/{use_path}",
            preview_link=f"{deploy_url}/{use_path}",
        )
        if lang != "en":
            link.en_link = f"https://fastapi.tiangolo.com/{en_path}"
        lang_links.setdefault(lang, []).append(link)

    links: list[LinkData] = []
    en_links = lang_links.get("en", [])
    en_links.sort(key=lambda x: x.preview_link)
    links.extend(en_links)

    langs = list(lang_links.keys())
    langs.sort()
    for lang in langs:
        if lang == "en":
            continue
        current_lang_links = lang_links[lang]
        current_lang_links.sort(key=lambda x: x.preview_link)
        links.extend(current_lang_links)

    header = "## 📝 Docs preview"
    message = header
    message += f"\n\nLast commit {settings.commit_sha} at: {deploy_url}"

    if links:
        message += "\n\n### Modified Pages\n\n"
        for link in links:
            message += f"* {link.preview_link}"
            message += f" - ([before]({link.previous_link}))"
            if link.en_link:
                message += f" - ([English]({link.en_link}))"
            message += "\n"

    print(message)
    issue = use_pr.as_issue()
    comments = list(issue.get_comments())
    for comment in comments:
        if (
            comment.body.startswith(header)
            and comment.user.login == "github-actions[bot]"
        ):
            comment.edit(message)
            break
    else:
        issue.create_comment(message)

    logging.info("Finished")


if __name__ == "__main__":
    main()

```

### File: scripts\docs.py
```py
import json
import logging
import os
import re
import shutil
import subprocess
from html.parser import HTMLParser
from http.server import HTTPServer, SimpleHTTPRequestHandler
from multiprocessing import Pool
from pathlib import Path
from typing import Any

import mkdocs.utils
import typer
import yaml
from jinja2 import Template
from ruff.__main__ import find_ruff_bin
from slugify import slugify as py_slugify

logging.basicConfig(level=logging.INFO)

SUPPORTED_LANGS = {
    "de",
    "en",
    "es",
    "fr",
    "ja",
    "ko",
    "pt",
    "ru",
    "tr",
    "uk",
    "zh",
    "zh-hant",
}


app = typer.Typer()

mkdocs_name = "mkdocs.yml"

missing_translation_snippet = """
{!../../docs/missing-translation.md!}
"""

non_translated_sections = (
    f"reference{os.sep}",
    "release-notes.md",
    "fastapi-people.md",
    "external-links.md",
    "newsletter.md",
    "management-tasks.md",
    "management.md",
    "contributing.md",
)

docs_path = Path("docs")
en_docs_path = Path("docs/en")
en_config_path: Path = en_docs_path / mkdocs_name
site_path = Path("site").absolute()
build_site_path = Path("site_build").absolute()

header_pattern = re.compile(r"^(#{1,6}) (.+?)(?:\s*\{\s*(#.*)\s*\})?\s*$")
header_with_permalink_pattern = re.compile(r"^(#{1,6}) (.+?)(\s*\{\s*#.*\s*\})\s*$")
code_block3_pattern = re.compile(r"^\s*```")
code_block4_pattern = re.compile(r"^\s*````")


# Pattern to match markdown links: [text](url) → text
md_link_pattern = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def strip_markdown_links(text: str) -> str:
    """Replace markdown links with just their visible text."""
    return md_link_pattern.sub(r"\1", text)


class VisibleTextExtractor(HTMLParser):
    """Extract visible text from a string with HTML tags."""

    def __init__(self):
        super().__init__()
        self.text_parts = []

    def handle_data(self, data):
        self.text_parts.append(data)

    def extract_visible_text(self, html: str) -> str:
        self.reset()
        self.text_parts = []
        self.feed(html)
        return "".join(self.text_parts).strip()


def slugify(text: str) -> str:
    return py_slugify(
        text,
        replacements=[
            ("`", ""),  # `dict`s -> dicts
            ("'s", "s"),  # it's -> its
            ("'t", "t"),  # don't -> dont
            ("**", ""),  # **FastAPI**s -> FastAPIs
        ],
    )


def get_en_config() -> dict[str, Any]:
    return mkdocs.utils.yaml_load(en_config_path.read_text(encoding="utf-8"))


def get_lang_paths() -> list[Path]:
    return sorted(docs_path.iterdir())


def lang_callback(lang: str | None) -> str | None:
    if lang is None:
        return None
    lang = lang.lower()
    return lang


def complete_existing_lang(incomplete: str):
    lang_path: Path
    for lang_path in get_lang_paths():
        if lang_path.is_dir() and lang_path.name.startswith(incomplete):
            yield lang_path.name


@app.callback()
def callback() -> None:
    # For MacOS with Cairo
    os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = "/opt/homebrew/lib"


@app.command()
def new_lang(lang: str = typer.Argument(..., callback=lang_callback)):
    """
    Generate a new docs translation directory for the language LANG.
    """
    new_path: Path = Path("docs") / lang
    if new_path.exists():
        typer.echo(f"The language was already created: {lang}")
        raise typer.Abort()
    new_path.mkdir()
    new_config_path: Path = Path(new_path) / mkdocs_name
    new_config_path.write_text("INHERIT: ../en/mkdocs.yml\n", encoding="utf-8")
    new_llm_prompt_path: Path = new_path / "llm-prompt.md"
    new_llm_prompt_path.write_text("", encoding="utf-8")
    print(f"Successfully initialized: {new_path}")
    update_languages()


@app.command()
def build_lang(
    lang: str = typer.Argument(
        ..., callback=lang_callback, autocompletion=complete_existing_lang
    ),
) -> None:
    """
    Build the docs for a language.
    """
    lang_path: Path = Path("docs") / lang
    if not lang_path.is_dir():
        typer.echo(f"The language translation doesn't seem to exist yet: {lang}")
        raise typer.Abort()
    typer.echo(f"Building docs for: {lang}")
    build_site_dist_path = build_site_path / lang
    if lang == "en":
        dist_path = site_path
        # Don't remove en dist_path as it might already contain other languages.
        # When running build_all(), that function already removes site_path.
        # All this is only relevant locally, on GitHub Actions all this is done through
        # artifacts and multiple workflows, so it doesn't matter if directories are
        # removed or not.
    else:
        dist_path = site_path / lang
        shutil.rmtree(dist_path, ignore_errors=True)
    current_dir = os.getcwd()
    os.chdir(lang_path)
    shutil.rmtree(build_site_dist_path, ignore_errors=True)
    subprocess.run(["mkdocs", "build", "--site-dir", build_site_dist_path], check=True)
    shutil.copytree(build_site_dist_path, dist_path, dirs_exist_ok=True)
    os.chdir(current_dir)
    typer.secho(f"Successfully built docs for: {lang}", color=typer.colors.GREEN)


index_sponsors_template = """
### Keystone Sponsor

{% for sponsor in sponsors.keystone -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}"></a>
{% endfor %}
### Gold and Silver Sponsors

{% for sponsor in sponsors.gold -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}"></a>
{% endfor -%}
{%- for sponsor in sponsors.silver -%}
<a href="{{ sponsor.url }}" target="_blank" title="{{ sponsor.title }}"><img src="{{ sponsor.img }}"></a>
{% endfor %}

"""


def remove_header_permalinks(content: str):
    lines: list[str] = []
    for line in content.split("\n"):
        match = header_with_permalink_pattern.match(line)
        if match:
            hashes, title, *_ = match.groups()
            line = f"{hashes} {title}"
        lines.append(line)
    return "\n".join(lines)


def generate_readme_content() -> str:
    en_index = en_docs_path / "docs" / "index.md"
    content = en_index.read_text("utf-8")
    content = remove_header_permalinks(content)  # remove permalinks from headers
    match_pre = re.search(r"</style>\n\n", content)
    match_start = re.search(r"<!-- sponsors -->", content)
    match_end = re.search(r"<!-- /sponsors -->", content)
    sponsors_data_path = en_docs_path / "data" / "sponsors.yml"
    sponsors = mkdocs.utils.yaml_load(sponsors_data_path.read_text(encoding="utf-8"))
    if not (match_start and match_end):
        raise RuntimeError("Couldn't auto-generate sponsors section")
    if not match_pre:
        raise RuntimeError("Couldn't find pre section (<style>) in index.md")
    frontmatter_end = match_pre.end()
    pre_end = match_start.end()
    post_start = match_end.start()
    template = Template(index_sponsors_template)
    message = template.render(sponsors=sponsors)
    pre_content = content[frontmatter_end:pre_end]
    post_content = content[post_start:]
    new_content = pre_content + message + post_content
    # Remove content between <!-- only-mkdocs --> and <!-- /only-mkdocs -->
    new_content = re.sub(
        r"<!-- only-mkdocs -->.*?<!-- /only-mkdocs -->",
        "",
        new_content,
        flags=re.DOTALL,
    )
    return new_content


@app.command()
def generate_readme() -> None:
    """
    Generate README.md content from main index.md
    """
    readme_path = Path("README.md")
    old_content = readme_path.read_text("utf-8")
    new_content = generate_readme_content()
    if new_content != old_content:
        print("README.md outdated from the latest index.md")
        print("Updating README.md")
        readme_path.write_text(new_content, encoding="utf-8")
        raise typer.Exit(1)
    print("README.md is up to date ✅")


@app.command()
def build_all() -> None:
    """
    Build mkdocs site for en, and then build each language inside, end result is located
    at directory ./site/ with each language inside.
    """
    update_languages()
    shutil.rmtree(site_path, ignore_errors=True)
    langs = [
        lang.name
        for lang in get_lang_paths()
        if (lang.is_dir() and lang.name in SUPPORTED_LANGS)
    ]
    cpu_count = os.cpu_count() or 1
    process_pool_size = cpu_count * 4
    typer.echo(f"Using process pool size: {process_pool_size}")
    with Pool(process_pool_size) as p:
        p.map(build_lang, langs)


@app.command()
def update_languages() -> None:
    """
    Update the mkdocs.yml file Languages section including all the available languages.
    """
    old_config = get_en_config()
    updated_config = get_updated_config_content()
    if old_config != updated_config:
        print("docs/en/mkdocs.yml outdated")
        print("Updating docs/en/mkdocs.yml")
        en_config_path.write_text(
            yaml.dump(updated_config, sort_keys=False, width=200, allow_unicode=True),
            encoding="utf-8",
        )
        raise typer.Exit(1)
    print("docs/en/mkdocs.yml is up to date ✅")


@app.command()
def serve() -> None:
    """
    A quick server to preview a built site with translations.

    For development, prefer the command live (or just mkdocs serve).

    This is here only to preview a site with translations already built.

    Make sure you run the build-all command first.
    """
    typer.echo("Warning: this is a very simple server.")
    typer.echo("For development, use the command live instead.")
    typer.echo("This is here only to preview a site with translations already built.")
    typer.echo("Make sure you run the build-all command first.")
    os.chdir("site")
    server_address = ("", 8008)
    server = HTTPServer(server_address, SimpleHTTPRequestHandler)
    typer.echo("Serving at: http://127.0.0.1:8008")
    server.serve_forever()


@app.command()
def live(
    lang: str = typer.Argument(
        None, callback=lang_callback, autocompletion=complete_existing_lang
    ),
    dirty: bool = False,
) -> None:
    """
    Serve with livereload a docs site for a specific language.

    This only shows the actual translated files, not the placeholders created with
    build-all.

    Takes an optional LANG argument with the name of the language to serve, by default
    en.
    """
    # Enable line numbers during local development to make it easier to highlight
    if lang is None:
        lang = "en"
    lang_path: Path = docs_path / lang
    # Enable line numbers during local development to make it easier to highlight
    args = ["mkdocs", "serve", "--dev-addr", "127.0.0.1:8008"]
    if dirty:
        args.append("--dirty")
    subprocess.run(
        args, env={**os.environ, "LINENUMS": "true"}, cwd=lang_path, check=True
    )


def get_updated_config_content() -> dict[str, Any]:
    config = get_en_config()
    languages = [{"en": "/"}]
    new_alternate: list[dict[str, str]] = []
    # Language names sourced from https://quickref.me/iso-639-1
    # Contributors may wish to update or change these, e.g. to fix capitalization.
    language_names_path = Path(__file__).parent / "../docs/language_names.yml"
    local_language_names: dict[str, str] = mkdocs.utils.yaml_load(
        language_names_path.read_text(encoding="utf-8")
    )
    for lang_path in get_lang_paths():
        if lang_path.name in {"en", "em"} or not lang_path.is_dir():
            continue
        if lang_path.name not in SUPPORTED_LANGS:
            # Skip languages that are not yet ready
            continue
        code = lang_path.name
        languages.append({code: f"/{code}/"})
    for lang_dict in languages:
        code = list(lang_dict.keys())[0]
        url = lang_dict[code]
        if code not in local_language_names:
            print(
                f"Missing language name for: {code}, "
                "update it in docs/language_names.yml"
            )
            raise typer.Abort()
        use_name = f"{code} - {local_language_names[code]}"
        new_alternate.append({"link": url, "name": use_name})
    config["extra"]["alternate"] = new_alternate
    return config


@app.command()
def ensure_non_translated() -> None:
    """
    Ensure there are no files in the non translatable pages.
    """
    print("Ensuring no non translated pages")
    lang_paths = get_lang_paths()
    error_paths = []
    for lang in lang_paths:
        if lang.name == "en":
            continue
        for non_translatable in non_translated_sections:
            non_translatable_path = lang / "docs" / non_translatable
            if non_translatable_path.exists():
                error_paths.append(non_translatable_path)
    if error_paths:
        print("Non-translated pages found, removing them:")
        for error_path in error_paths:
            print(error_path)
            if error_path.is_file():
                error_path.unlink()
            else:
                shutil.rmtree(error_path)
        raise typer.Exit(1)
    print("No non-translated pages found ✅")


@app.command()
def langs_json():
    langs = []
    for lang_path in get_lang_paths():
        if lang_path.is_dir() and lang_path.name in SUPPORTED_LANGS:
            langs.append(lang_path.name)
    print(json.dumps(langs))


@app.command()
def generate_docs_src_versions_for_file(file_path: Path) -> None:
    target_versions = ["py39", "py310"]
    full_path_str = str(file_path)
    for target_version in target_versions:
        if f"_{target_version}" in full_path_str:
            logging.info(
                f"Skipping {file_path}, already a version file for {target_version}"
            )
            return
    base_content = file_path.read_text(encoding="utf-8")
    previous_content = {base_content}
    for target_version in target_versions:
        version_result = subprocess.run(
            [
                find_ruff_bin(),
                "check",
                "--target-version",
                target_version,
                "--fix",
                "--unsafe-fixes",
                "-",
            ],
            input=base_content.encode("utf-8"),
            capture_output=True,
        )
        content_target = version_result.stdout.decode("utf-8")
        format_result = subprocess.run(
            [find_ruff_bin(), "format", "-"],
            input=content_target.encode("utf-8"),
            capture_output=True,
        )
        content_format = format_result.stdout.decode("utf-8")
        if content_format in previous_content:
            continue
        previous_content.add(content_format)
        # Determine where the version label should go: in the parent directory
        # name or in the file name, matching the source structure.
        label_in_parent = False
        for v in target_versions:
            if f"_{v}" in file_path.parent.name:
                label_in_parent = True
                break
        if label_in_parent:
            parent_name = file_path.parent.name
            for v in target_versions:
                
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
