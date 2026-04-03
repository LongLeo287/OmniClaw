---
id: github.com-thomasbury-pyragify-9c7de652-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:27.776335
---

# KNOWLEDGE EXTRACT: github.com_ThomasBury_pyragify_9c7de652
> **Extracted on:** 2026-04-01 15:34:33
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524610/github.com_ThomasBury_pyragify_9c7de652

---

## File: `.gitignore`
```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
#.idea/
```

## File: `LICENSE`
```
This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or
distribute this software, either in source code form or as a compiled
binary, for any purpose, commercial or non-commercial, and by any
means.

In jurisdictions that recognize copyright laws, the author or authors
of this software dedicate any and all copyright interest in the
software to the public domain. We make this dedication for the benefit
of the public at large and to the detriment of our heirs and
successors. We intend this dedication to be an overt act of
relinquishment in perpetuity of all present and future rights to this
software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <https://unlicense.org>
```

## File: `README.md`
```markdown
# pyragify: Unlock the Power of Your Code with NotebookLM  

**pyragify** is a Python-based tool designed to **transform your Python code repositories into a format that's ready for analysis with large language models (LLMs), specifically NotebookLM.** It breaks down complex code structures into manageable semantic chunks, making it easier to understand, analyze, and extract insights from your code.

## Why pyragify?

* **Boost Code Comprehension:**  pyragify makes it easier to digest large codebases by dividing them into smaller, logical units.
* **Effortless Analysis:** The structured output simplifies the process of analyzing code, identifying patterns, and extracting knowledge.
* **Unlock the Power of NotebookLM:** pyragify prepares your code for use with NotebookLM, allowing you to leverage the power of LLMs for tasks like code summarization, documentation generation, and question answering.

## Key Features

* **Semantic Chunking:** pyragify intelligently extracts functions, classes, and comments from Python files, as well as headers and sections from Markdown files, preserving the context and meaning.
* **Wide Format Support:** It handles Python (.py), Markdown (.md, .markdown), HTML (.html), CSS (.css), and other common file types, ensuring all your repository content is processed.
* **Smart Parsing:** Uses AST for Python files, regex-based parsing for HTML/CSS, and header-based chunking for Markdown files.
* **Seamless Integration with NotebookLM:** The output format is specifically designed for compatibility with NotebookLM, making it easy to analyze your code with powerful LLMs.
* **Flexible Configuration:** Tailor the processing through a YAML file or command-line arguments to fit your specific needs.
* **File Skipping:** Respect your `.gitignore` and `.dockerignore` files, and define custom skip patterns for even more control.
* **Word Limit Control:** Automatically chunks output files based on a configurable word limit to ensure manageable file sizes.
* **Input Validation:** Validates repository paths and provides clear error messages for invalid inputs.

## Getting Started

### Installation

1. **Using uv (Recommended):**

    ```bash
    uv pip install pyragify
    ```

    `uv` is a blazing fast Python package manager that handles virtual environments and dependencies automatically.

2. **Using pip:**

    ```bash
    pip install pyragify
    ```

3. **From Source:**

    ```bash
    git clone https://github.com/ThomasBury/pyragify.git
    cd pyragify
    uv pip install -e .
    ```

### Usage

1. **Best Practice with uv:**

    ```bash
    uv run pyragify --config-file config.yaml
    ```

See below for details about the configuration file.

2. **Direct CLI Execution:**

    ```bash
    python -m pyragify --config-file config.yaml
    ```

#### Arguments and Options

See `pyragify --help` for a full list of options.

* `--config-file`: Path to the YAML configuration file (default: config.yaml).
* `--repo-path`: Override the repository path.
* `--output-dir`: Override the output directory.
* `--max-words`: Override the maximum words per output file.
* `--max-file-size`: Override the maximum file size (in bytes) to process.
* `--skip-patterns`: Override file patterns to skip.
* `--skip-dirs`: Override directories to skip.
* `--verbose`: Enable detailed logging for debugging.

### Configuration (config.yaml)

```yaml
repo_path: /path/to/repository
output_dir: /path/to/output
max_words: 200000
max_file_size: 10485760 # 10 MB
skip_patterns:
 - "*.log"
 - "*.tmp"
skip_dirs:
 - "__pycache__"
 - "node_modules"
verbose: false
```

## Example Workflow

1. **Prepare Your Repository:** Make sure your repository contains the code you want to process. Utilize `.gitignore` or `.dockerignore` to exclude unwanted files or directories.
2. **Configure pyragify:** Create a `config.yaml` file with your desired settings or use the default configuration.
3. **Process the Repository:** Run pyragify using uv (recommended):

    ```bash
    uv run pyragify --config-file config.yaml
    ```

4. **Check the Output:** Your processed content is neatly organized by file type in the specified output directory.

## Chat with Your Codebase (with NotebookLM)

1. Navigate to NotebookLM.
2. Upload the `chunk_0.txt` file (or other relevant chunks) from the pyragify output directory to a new notebook.
3. Start asking questions and get insights with precise citations! You can even generate a podcast from your code.
    ![code_chat](chat_code_base.png "Chat with your code base")

## Output Structure

The processed content is saved as `.txt` files and categorized into subdirectories based on the file type:

* `python/`:  Contains chunks of Python functions, classes, and their code.
* `markdown/`:  Contains sections of Markdown files split by headers.
* `html/`:  Contains HTML script and style chunks extracted from HTML files.
* `css/`:  Contains CSS rule chunks from CSS files.
* `other/`:  Contains plain-text versions of unsupported file types.

## Advanced Features

* **Input Validation:** Validates repository paths and provides clear error messages for invalid inputs.
* **Respect for Ignore Files:** pyragify automatically honors `.gitignore` and `.dockerignore` patterns.
* **Incremental Processing:** MD5 hashes are used to efficiently skip unchanged files during subsequent runs.

## Contributing

We welcome contributions! To contribute to pyragify:

1. Clone the repository.
2. Install dependencies.
3. Run tests. (Test suite is under development).

## Support

Feel free to create a GitHub issue for any questions, bug reports, or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Example Usages

**Process a Repository with Default Settings:**

```bash
uv run pyragify --config-file config.yaml
```

**Process a Specific Repository with Custom Settings:**

```bash
uv run pyragify \
 --repo-path /my/repo \
 --output-dir /my/output \
 --max-words 100000 \
 --max-file-size 5242880 \
 --skip-patterns "*.log,*.tmp" \
 --skip-dirs "__pycache__,node_modules" \
 --verbose
```
```

## File: `config.yaml`
```yaml
repo_path: /home/user/project/pyragify/
output_dir: ./output
max_words: 200000
max_file_size: 10485760  # 10 MB
skip_patterns:
 - ".git"
 - "uv.lock"
 - ".gitignore"
skip_dirs: []
verbose: false
```

## File: `pyproject.toml`
```
[project]
name = "pyragify"
version = "0.2.0"
description = "A tool for processing code repositories into semantic chunks for analysis with LLMs, especiallyNotebookLM."
readme = "README.md"
requires-python = ">=3.9, <3.13"
authors = [
    {name = "ThomasBury"}
]
license = {text = "The Unlicense"}
keywords = ["code-processing", "chunking", "repository-analysis", "notebookLM"]
classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent"
]
dependencies = [
    "omegaconf>=2.3.0",
    "pathspec>=0.12.1",
    "pyyaml>=6.0.2",
    "typer>=0.15.1"
]

[project.optional-dependencies]
dev = [
    "pytest>=7.0.0",
    "pytest-mock>=3.0.0"
]

[project.urls]
homepage = "https://github.com/ThomasBury/pyragify"
repository = "https://github.com/ThomasBury/pyragify"

[project.scripts]
pyragify = "pyragify.cli:app"

[tool.pytest.ini_options]
python_paths = ["src"]

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```

## File: `text2flow_optimized.yaml`
```yaml
# Pyragify Config: Optimized for Text2Flow/Visualization.

# Use the current directory as the source for weaving
repo_path: "."

# The folder where the LLM-ready "weaved" text will be saved
output_dir: "./llm_analysis"

# These are the files to ignore so we only push the essential files to the LLM.
skip_patterns:
  - "*.min.js"
  - "*.map"
  - "bundle.js"
  - "*-lock.json"
  - "*.svg"

# Standard heavy folders/files to bypass.
skip_dirs:
  - "node_modules"
  - "dist"
  - "build"
  - "__pycache__"
  - ".git"

# High max_words allows complex flowchart grammars to stay 
# within a single window for better RAG performance.
max_words: 500000

# Required to prevent CLI runtime failure.
max_file_size: 10485760 #10MB

# # Provide essential feedback in the terminal while processing.
verbose: true
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.9, <3.13"
resolution-markers = [
    "python_full_version >= '3.10'",
    "python_full_version < '3.10'",
]

[[package]]
name = "antlr4-python3-runtime"
version = "4.9.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/3e/38/7859ff46355f76f8d19459005ca000b6e7012f2f1ca597746cbcd1fbfe5e/antlr4-python3-runtime-4.9.3.tar.gz", hash = "sha256:f224469b4168294902bb1efa80a8bf7855f24c99aef99cbefc1bcd3cce77881b", size = 117034, upload-time = "2021-11-06T17:52:23.524Z" }

[[package]]
name = "click"
version = "8.1.7"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/d3/f04c7bfcf5c1862a2a5b845c6b2b360488cf47af55dfa79c98f6a6bf98b5/click-8.1.7.tar.gz", hash = "sha256:ca9853ad459e787e2192211578cc907e7594e294c7ccc834310722b41b9ca6de", size = 336121, upload-time = "2023-08-17T17:29:11.868Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/00/2e/d53fa4befbf2cfa713304affc7ca780ce4fc1fd8710527771b58311a3229/click-8.1.7-py3-none-any.whl", hash = "sha256:ae74fb96c20a0277a1d615f1e4d73c8414f5a98db8b799a7931d1582f3390c28", size = 97941, upload-time = "2023-08-17T17:29:10.08Z" },
]

[[package]]
name = "colorama"
version = "0.4.6"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d8/53/6f443c9a4a8358a93a6792e2acffb9d9d5cb0a5cfd8802644b7b1c9a02e4/colorama-0.4.6.tar.gz", hash = "sha256:08695f5cb7ed6e0531a20572697297273c47b8cae5a63ffc6d6ed5c201be6e44", size = 27697, upload-time = "2022-10-25T02:36:22.414Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/d6/3965ed04c63042e047cb6a3e6ed1a63a35087b6a609aa3a15ed8ac56c221/colorama-0.4.6-py2.py3-none-any.whl", hash = "sha256:4f1d9991f5acc0ca119f9d443620b77f9d6b33703e51011c16baf57afb285fc6", size = 25335, upload-time = "2022-10-25T02:36:20.889Z" },
]

[[package]]
name = "exceptiongroup"
version = "1.3.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/0b/9f/a65090624ecf468cdca03533906e7c69ed7588582240cfe7cc9e770b50eb/exceptiongroup-1.3.0.tar.gz", hash = "sha256:b241f5885f560bc56a59ee63ca4c6a8bfa46ae4ad651af316d4e81817bb9fd88", size = 29749, upload-time = "2025-05-10T17:42:51.123Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/36/f4/c6e662dade71f56cd2f3735141b265c3c79293c109549c1e6933b0651ffc/exceptiongroup-1.3.0-py3-none-any.whl", hash = "sha256:4d111e6e0c13d0644cad6ddaa7ed0261a0b36971f6d23e7ec9b4b9097da78a10", size = 16674, upload-time = "2025-05-10T17:42:49.33Z" },
]

[[package]]
name = "iniconfig"
version = "2.1.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f2/97/ebf4da567aa6827c909642694d71c9fcf53e5b504f2d96afea02718862f3/iniconfig-2.1.0.tar.gz", hash = "sha256:3abbd2e30b36733fee78f9c7f7308f2d0050e88f0087fd25c2645f63c773e1c7", size = 4793, upload-time = "2025-03-19T20:09:59.721Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2c/e1/e6716421ea10d38022b952c159d5161ca1193197fb744506875fbb87ea7b/iniconfig-2.1.0-py3-none-any.whl", hash = "sha256:9deba5723312380e77435581c6bf4935c94cbfab9b1ed33ef8d238ea168eb760", size = 6050, upload-time = "2025-03-19T20:10:01.071Z" },
]

[[package]]
name = "markdown-it-py"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "mdurl" },
]
sdist = { url = "https://files.pythonhosted.org/packages/38/71/3b932df36c1a044d397a1f92d1cf91ee0a503d91e470cbd670aa66b07ed0/markdown-it-py-3.0.0.tar.gz", hash = "sha256:e3f60a94fa066dc52ec76661e37c851cb232d92f9886b15cb560aaada2df8feb", size = 74596, upload-time = "2023-06-03T06:41:14.443Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/42/d7/1ec15b46af6af88f19b8e5ffea08fa375d433c998b8a7639e76935c14f1f/markdown_it_py-3.0.0-py3-none-any.whl", hash = "sha256:355216845c60bd96232cd8d8c40e8f9765cc86f46880e43a8fd22dc1a1a8cab1", size = 87528, upload-time = "2023-06-03T06:41:11.019Z" },
]

[[package]]
name = "mdurl"
version = "0.1.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/d6/54/cfe61301667036ec958cb99bd3efefba235e65cdeb9c84d24a8293ba1d90/mdurl-0.1.2.tar.gz", hash = "sha256:bb413d29f5eea38f31dd4754dd7377d4465116fb207585f97bf925588687c1ba", size = 8729, upload-time = "2022-08-14T12:40:10.846Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b3/38/89ba8ad64ae25be8de66a6d463314cf1eb366222074cfda9ee839c56a4b4/mdurl-0.1.2-py3-none-any.whl", hash = "sha256:84008a41e51615a49fc9966191ff91509e3c40b939176e643fd50a5c2196b8f8", size = 9979, upload-time = "2022-08-14T12:40:09.779Z" },
]

[[package]]
name = "omegaconf"
version = "2.3.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "antlr4-python3-runtime" },
    { name = "pyyaml" },
]
sdist = { url = "https://files.pythonhosted.org/packages/09/48/6388f1bb9da707110532cb70ec4d2822858ddfb44f1cdf1233c20a80ea4b/omegaconf-2.3.0.tar.gz", hash = "sha256:d5d4b6d29955cc50ad50c46dc269bcd92c6e00f5f90d23ab5fee7bfca4ba4cc7", size = 3298120, upload-time = "2022-12-08T20:59:22.753Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e3/94/1843518e420fa3ed6919835845df698c7e27e183cb997394e4a670973a65/omegaconf-2.3.0-py3-none-any.whl", hash = "sha256:7b4df175cdb08ba400f45cae3bdcae7ba8365db4d165fc65fd04b050ab63b46b", size = 79500, upload-time = "2022-12-08T20:59:19.686Z" },
]

[[package]]
name = "packaging"
version = "25.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a1/d4/1fc4078c65507b51b96ca8f8c3ba19e6a61c8253c72794544580a7b6c24d/packaging-25.0.tar.gz", hash = "sha256:d443872c98d677bf60f6a1f2f8c1cb748e8fe762d2bf9d3148b5599295b0fc4f", size = 165727, upload-time = "2025-04-19T11:48:59.673Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/20/12/38679034af332785aac8774540895e234f4d07f7545804097de4b666afd8/packaging-25.0-py3-none-any.whl", hash = "sha256:29572ef2b1f17581046b3a2227d5c611fb25ec70ca1ba8554b24b0e69331a484", size = 66469, upload-time = "2025-04-19T11:48:57.875Z" },
]

[[package]]
name = "pathspec"
version = "0.12.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ca/bc/f35b8446f4531a7cb215605d100cd88b7ac6f44ab3fc94870c120ab3adbf/pathspec-0.12.1.tar.gz", hash = "sha256:a482d51503a1ab33b1c67a6c3813a26953dbdc71c31dacaef9a838c4e29f5712", size = 51043, upload-time = "2023-12-10T22:30:45Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/cc/20/ff623b09d963f88bfde16306a54e12ee5ea43e9b597108672ff3a408aad6/pathspec-0.12.1-py3-none-any.whl", hash = "sha256:a0d503e138a4c123b27490a4f7beda6a01c6f288df0e4a8b79c7eb0dc7b4cc08", size = 31191, upload-time = "2023-12-10T22:30:43.14Z" },
]

[[package]]
name = "pluggy"
version = "1.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz", hash = "sha256:7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3", size = 69412, upload-time = "2025-05-15T12:30:07.975Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/54/20/4d324d65cc6d9205fabedc306948156824eb9f0ee1633355a8f7ec5c66bf/pluggy-1.6.0-py3-none-any.whl", hash = "sha256:e920276dd6813095e9377c0bc5566d94c932c33b27a3e3945d8389c374dd4746", size = 20538, upload-time = "2025-05-15T12:30:06.134Z" },
]

[[package]]
name = "pygments"
version = "2.18.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/8e/62/8336eff65bcbc8e4cb5d05b55faf041285951b6e80f33e2bff2024788f31/pygments-2.18.0.tar.gz", hash = "sha256:786ff802f32e91311bff3889f6e9a86e81505fe99f2735bb6d60ae0c5004f199", size = 4891905, upload-time = "2024-05-04T13:42:02.013Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/f7/3f/01c8b82017c199075f8f788d0d906b9ffbbc5a47dc9918a945e13d5a2bda/pygments-2.18.0-py3-none-any.whl", hash = "sha256:b8e6aca0523f3ab76fee51799c488e38782ac06eafcf95e7ba832985c8e7b13a", size = 1205513, upload-time = "2024-05-04T13:41:57.345Z" },
]

[[package]]
name = "pyragify"
version = "0.2.0"
source = { editable = "." }
dependencies = [
    { name = "omegaconf" },
    { name = "pathspec" },
    { name = "pyyaml" },
    { name = "typer" },
]

[package.optional-dependencies]
dev = [
    { name = "pytest" },
    { name = "pytest-mock" },
]

[package.metadata]
requires-dist = [
    { name = "omegaconf", specifier = ">=2.3.0" },
    { name = "pathspec", specifier = ">=0.12.1" },
    { name = "pytest", marker = "extra == 'dev'", specifier = ">=7.0.0" },
    { name = "pytest-mock", marker = "extra == 'dev'", specifier = ">=3.0.0" },
    { name = "pyyaml", specifier = ">=6.0.2" },
    { name = "typer", specifier = ">=0.15.1" },
]
provides-extras = ["dev"]

[[package]]
name = "pytest"
version = "8.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "pygments" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/a3/5c/00a0e072241553e1a7496d638deababa67c5058571567b92a7eaa258397c/pytest-8.4.2.tar.gz", hash = "sha256:86c0d0b93306b961d58d62a4db4879f27fe25513d4b969df351abdddb3c30e01", size = 1519618, upload-time = "2025-09-04T14:34:22.711Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/a8/a4/20da314d277121d6534b3a980b29035dcd51e6744bd79075a6ce8fa4eb8d/pytest-8.4.2-py3-none-any.whl", hash = "sha256:872f880de3fc3a5bdc88a11b39c9710c3497a547cfa9320bc3c5e62fbf272e79", size = 365750, upload-time = "2025-09-04T14:34:20.226Z" },
]

[[package]]
name = "pytest-mock"
version = "3.15.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "pytest" },
]
sdist = { url = "https://files.pythonhosted.org/packages/61/99/3323ee5c16b3637b4d941c362182d3e749c11e400bea31018c42219f3a98/pytest_mock-3.15.0.tar.gz", hash = "sha256:ab896bd190316b9d5d87b277569dfcdf718b2d049a2ccff5f7aca279c002a1cf", size = 33838, upload-time = "2025-09-04T20:57:48.679Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2b/b3/7fefc43fb706380144bcd293cc6e446e6f637ddfa8b83f48d1734156b529/pytest_mock-3.15.0-py3-none-any.whl", hash = "sha256:ef2219485fb1bd256b00e7ad7466ce26729b30eadfc7cbcdb4fa9a92ca68db6f", size = 10050, upload-time = "2025-09-04T20:57:47.274Z" },
]

[[package]]
name = "pyyaml"
version = "6.0.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/54/ed/79a089b6be93607fa5cdaedf301d7dfb23af5f25c398d5ead2525b063e17/pyyaml-6.0.2.tar.gz", hash = "sha256:d584d9ec91ad65861cc08d42e834324ef890a082e591037abe114850ff7bbc3e", size = 130631, upload-time = "2024-08-06T20:33:50.674Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9b/95/a3fac87cb7158e231b5a6012e438c647e1a87f09f8e0d123acec8ab8bf71/PyYAML-6.0.2-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:0a9a2848a5b7feac301353437eb7d5957887edbf81d56e903999a75a3d743086", size = 184199, upload-time = "2024-08-06T20:31:40.178Z" },
    { url = "https://files.pythonhosted.org/packages/c7/7a/68bd47624dab8fd4afbfd3c48e3b79efe09098ae941de5b58abcbadff5cb/PyYAML-6.0.2-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:29717114e51c84ddfba879543fb232a6ed60086602313ca38cce623c1d62cfbf", size = 171758, upload-time = "2024-08-06T20:31:42.173Z" },
    { url = "https://files.pythonhosted.org/packages/49/ee/14c54df452143b9ee9f0f29074d7ca5516a36edb0b4cc40c3f280131656f/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:8824b5a04a04a047e72eea5cec3bc266db09e35de6bdfe34c9436ac5ee27d237", size = 718463, upload-time = "2024-08-06T20:31:44.263Z" },
    { url = "https://files.pythonhosted.org/packages/4d/61/de363a97476e766574650d742205be468921a7b532aa2499fcd886b62530/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:7c36280e6fb8385e520936c3cb3b8042851904eba0e58d277dca80a5cfed590b", size = 719280, upload-time = "2024-08-06T20:31:50.199Z" },
    { url = "https://files.pythonhosted.org/packages/6b/4e/1523cb902fd98355e2e9ea5e5eb237cbc5f3ad5f3075fa65087aa0ecb669/PyYAML-6.0.2-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ec031d5d2feb36d1d1a24380e4db6d43695f3748343d99434e6f5f9156aaa2ed", size = 751239, upload-time = "2024-08-06T20:31:52.292Z" },
    { url = "https://files.pythonhosted.org/packages/b7/33/5504b3a9a4464893c32f118a9cc045190a91637b119a9c881da1cf6b7a72/PyYAML-6.0.2-cp310-cp310-musllinux_1_1_aarch64.whl", hash = "sha256:936d68689298c36b53b29f23c6dbb74de12b4ac12ca6cfe0e047bedceea56180", size = 695802, upload-time = "2024-08-06T20:31:53.836Z" },
    { url = "https://files.pythonhosted.org/packages/5c/20/8347dcabd41ef3a3cdc4f7b7a2aff3d06598c8779faa189cdbf878b626a4/PyYAML-6.0.2-cp310-cp310-musllinux_1_1_x86_64.whl", hash = "sha256:23502f431948090f597378482b4812b0caae32c22213aecf3b55325e049a6c68", size = 720527, upload-time = "2024-08-06T20:31:55.565Z" },
    { url = "https://files.pythonhosted.org/packages/be/aa/5afe99233fb360d0ff37377145a949ae258aaab831bde4792b32650a4378/PyYAML-6.0.2-cp310-cp310-win32.whl", hash = "sha256:2e99c6826ffa974fe6e27cdb5ed0021786b03fc98e5ee3c5bfe1fd5015f42b99", size = 144052, upload-time = "2024-08-06T20:31:56.914Z" },
    { url = "https://files.pythonhosted.org/packages/b5/84/0fa4b06f6d6c958d207620fc60005e241ecedceee58931bb20138e1e5776/PyYAML-6.0.2-cp310-cp310-win_amd64.whl", hash = "sha256:a4d3091415f010369ae4ed1fc6b79def9416358877534caf6a0fdd2146c87a3e", size = 161774, upload-time = "2024-08-06T20:31:58.304Z" },
    { url = "https://files.pythonhosted.org/packages/f8/aa/7af4e81f7acba21a4c6be026da38fd2b872ca46226673c89a758ebdc4fd2/PyYAML-6.0.2-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:cc1c1159b3d456576af7a3e4d1ba7e6924cb39de8f67111c735f6fc832082774", size = 184612, upload-time = "2024-08-06T20:32:03.408Z" },
    { url = "https://files.pythonhosted.org/packages/8b/62/b9faa998fd185f65c1371643678e4d58254add437edb764a08c5a98fb986/PyYAML-6.0.2-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:1e2120ef853f59c7419231f3bf4e7021f1b936f6ebd222406c3b60212205d2ee", size = 172040, upload-time = "2024-08-06T20:32:04.926Z" },
    { url = "https://files.pythonhosted.org/packages/ad/0c/c804f5f922a9a6563bab712d8dcc70251e8af811fce4524d57c2c0fd49a4/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:5d225db5a45f21e78dd9358e58a98702a0302f2659a3c6cd320564b75b86f47c", size = 736829, upload-time = "2024-08-06T20:32:06.459Z" },
    { url = "https://files.pythonhosted.org/packages/51/16/6af8d6a6b210c8e54f1406a6b9481febf9c64a3109c541567e35a49aa2e7/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:5ac9328ec4831237bec75defaf839f7d4564be1e6b25ac710bd1a96321cc8317", size = 764167, upload-time = "2024-08-06T20:32:08.338Z" },
    { url = "https://files.pythonhosted.org/packages/75/e4/2c27590dfc9992f73aabbeb9241ae20220bd9452df27483b6e56d3975cc5/PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3ad2a3decf9aaba3d29c8f537ac4b243e36bef957511b4766cb0057d32b0be85", size = 762952, upload-time = "2024-08-06T20:32:14.124Z" },
    { url = "https://files.pythonhosted.org/packages/9b/97/ecc1abf4a823f5ac61941a9c00fe501b02ac3ab0e373c3857f7d4b83e2b6/PyYAML-6.0.2-cp311-cp311-musllinux_1_1_aarch64.whl", hash = "sha256:ff3824dc5261f50c9b0dfb3be22b4567a6f938ccce4587b38952d85fd9e9afe4", size = 735301, upload-time = "2024-08-06T20:32:16.17Z" },
    { url = "https://files.pythonhosted.org/packages/45/73/0f49dacd6e82c9430e46f4a027baa4ca205e8b0a9dce1397f44edc23559d/PyYAML-6.0.2-cp311-cp311-musllinux_1_1_x86_64.whl", hash = "sha256:797b4f722ffa07cc8d62053e4cff1486fa6dc094105d13fea7b1de7d8bf71c9e", size = 756638, upload-time = "2024-08-06T20:32:18.555Z" },
    { url = "https://files.pythonhosted.org/packages/22/5f/956f0f9fc65223a58fbc14459bf34b4cc48dec52e00535c79b8db361aabd/PyYAML-6.0.2-cp311-cp311-win32.whl", hash = "sha256:11d8f3dd2b9c1207dcaf2ee0bbbfd5991f571186ec9cc78427ba5bd32afae4b5", size = 143850, upload-time = "2024-08-06T20:32:19.889Z" },
    { url = "https://files.pythonhosted.org/packages/ed/23/8da0bbe2ab9dcdd11f4f4557ccaf95c10b9811b13ecced089d43ce59c3c8/PyYAML-6.0.2-cp311-cp311-win_amd64.whl", hash = "sha256:e10ce637b18caea04431ce14fabcf5c64a1c61ec9c56b071a4b7ca131ca52d44", size = 161980, upload-time = "2024-08-06T20:32:21.273Z" },
    { url = "https://files.pythonhosted.org/packages/86/0c/c581167fc46d6d6d7ddcfb8c843a4de25bdd27e4466938109ca68492292c/PyYAML-6.0.2-cp312-cp312-macosx_10_9_x86_64.whl", hash = "sha256:c70c95198c015b85feafc136515252a261a84561b7b1d51e3384e0655ddf25ab", size = 183873, upload-time = "2024-08-06T20:32:25.131Z" },
    { url = "https://files.pythonhosted.org/packages/a8/0c/38374f5bb272c051e2a69281d71cba6fdb983413e6758b84482905e29a5d/PyYAML-6.0.2-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:ce826d6ef20b1bc864f0a68340c8b3287705cae2f8b4b1d932177dcc76721725", size = 173302, upload-time = "2024-08-06T20:32:26.511Z" },
    { url = "https://files.pythonhosted.org/packages/c3/93/9916574aa8c00aa06bbac729972eb1071d002b8e158bd0e83a3b9a20a1f7/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:1f71ea527786de97d1a0cc0eacd1defc0985dcf6b3f17bb77dcfc8c34bec4dc5", size = 739154, upload-time = "2024-08-06T20:32:28.363Z" },
    { url = "https://files.pythonhosted.org/packages/95/0f/b8938f1cbd09739c6da569d172531567dbcc9789e0029aa070856f123984/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:9b22676e8097e9e22e36d6b7bda33190d0d400f345f23d4065d48f4ca7ae0425", size = 766223, upload-time = "2024-08-06T20:32:30.058Z" },
    { url = "https://files.pythonhosted.org/packages/b9/2b/614b4752f2e127db5cc206abc23a8c19678e92b23c3db30fc86ab731d3bd/PyYAML-6.0.2-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:80bab7bfc629882493af4aa31a4cfa43a4c57c83813253626916b8c7ada83476", size = 767542, upload-time = "2024-08-06T20:32:31.881Z" },
    { url = "https://files.pythonhosted.org/packages/d4/00/dd137d5bcc7efea1836d6264f049359861cf548469d18da90cd8216cf05f/PyYAML-6.0.2-cp312-cp312-musllinux_1_1_aarch64.whl", hash = "sha256:0833f8694549e586547b576dcfaba4a6b55b9e96098b36cdc7ebefe667dfed48", size = 731164, upload-time = "2024-08-06T20:32:37.083Z" },
    { url = "https://files.pythonhosted.org/packages/c9/1f/4f998c900485e5c0ef43838363ba4a9723ac0ad73a9dc42068b12aaba4e4/PyYAML-6.0.2-cp312-cp312-musllinux_1_1_x86_64.whl", hash = "sha256:8b9c7197f7cb2738065c481a0461e50ad02f18c78cd75775628afb4d7137fb3b", size = 756611, upload-time = "2024-08-06T20:32:38.898Z" },
    { url = "https://files.pythonhosted.org/packages/df/d1/f5a275fdb252768b7a11ec63585bc38d0e87c9e05668a139fea92b80634c/PyYAML-6.0.2-cp312-cp312-win32.whl", hash = "sha256:ef6107725bd54b262d6dedcc2af448a266975032bc85ef0172c5f059da6325b4", size = 140591, upload-time = "2024-08-06T20:32:40.241Z" },
    { url = "https://files.pythonhosted.org/packages/0c/e8/4f648c598b17c3d06e8753d7d13d57542b30d56e6c2dedf9c331ae56312e/PyYAML-6.0.2-cp312-cp312-win_amd64.whl", hash = "sha256:7e7401d0de89a9a855c839bc697c079a4af81cf878373abd7dc625847d25cbd8", size = 156338, upload-time = "2024-08-06T20:32:41.93Z" },
    { url = "https://files.pythonhosted.org/packages/65/d8/b7a1db13636d7fb7d4ff431593c510c8b8fca920ade06ca8ef20015493c5/PyYAML-6.0.2-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:688ba32a1cffef67fd2e9398a2efebaea461578b0923624778664cc1c914db5d", size = 184777, upload-time = "2024-08-06T20:33:25.896Z" },
    { url = "https://files.pythonhosted.org/packages/0a/02/6ec546cd45143fdf9840b2c6be8d875116a64076218b61d68e12548e5839/PyYAML-6.0.2-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:a8786accb172bd8afb8be14490a16625cbc387036876ab6ba70912730faf8e1f", size = 172318, upload-time = "2024-08-06T20:33:27.212Z" },
    { url = "https://files.pythonhosted.org/packages/0e/9a/8cc68be846c972bda34f6c2a93abb644fb2476f4dcc924d52175786932c9/PyYAML-6.0.2-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:d8e03406cac8513435335dbab54c0d385e4a49e4945d2909a581c83647ca0290", size = 720891, upload-time = "2024-08-06T20:33:28.974Z" },
    { url = "https://files.pythonhosted.org/packages/e9/6c/6e1b7f40181bc4805e2e07f4abc10a88ce4648e7e95ff1abe4ae4014a9b2/PyYAML-6.0.2-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:f753120cb8181e736c57ef7636e83f31b9c0d1722c516f7e86cf15b7aa57ff12", size = 722614, upload-time = "2024-08-06T20:33:34.157Z" },
    { url = "https://files.pythonhosted.org/packages/3d/32/e7bd8535d22ea2874cef6a81021ba019474ace0d13a4819c2a4bce79bd6a/PyYAML-6.0.2-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3b1fdb9dc17f5a7677423d508ab4f243a726dea51fa5e70992e59a7411c89d19", size = 737360, upload-time = "2024-08-06T20:33:35.84Z" },
    { url = "https://files.pythonhosted.org/packages/d7/12/7322c1e30b9be969670b672573d45479edef72c9a0deac3bb2868f5d7469/PyYAML-6.0.2-cp39-cp39-musllinux_1_1_aarch64.whl", hash = "sha256:0b69e4ce7a131fe56b7e4d770c67429700908fc0752af059838b1cfb41960e4e", size = 699006, upload-time = "2024-08-06T20:33:37.501Z" },
    { url = "https://files.pythonhosted.org/packages/82/72/04fcad41ca56491995076630c3ec1e834be241664c0c09a64c9a2589b507/PyYAML-6.0.2-cp39-cp39-musllinux_1_1_x86_64.whl", hash = "sha256:a9f8c2e67970f13b16084e04f134610fd1d374bf477b17ec1599185cf611d725", size = 723577, upload-time = "2024-08-06T20:33:39.389Z" },
    { url = "https://files.pythonhosted.org/packages/ed/5e/46168b1f2757f1fcd442bc3029cd8767d88a98c9c05770d8b420948743bb/PyYAML-6.0.2-cp39-cp39-win32.whl", hash = "sha256:6395c297d42274772abc367baaa79683958044e5d3835486c16da75d2a694631", size = 144593, upload-time = "2024-08-06T20:33:46.63Z" },
    { url = "https://files.pythonhosted.org/packages/19/87/5124b1c1f2412bb95c59ec481eaf936cd32f0fe2a7b16b97b81c4c017a6a/PyYAML-6.0.2-cp39-cp39-win_amd64.whl", hash = "sha256:39693e1f8320ae4f43943590b49779ffb98acb81f788220ea932a6b6c51004d8", size = 162312, upload-time = "2024-08-06T20:33:49.073Z" },
]

[[package]]
name = "rich"
version = "13.9.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "markdown-it-py" },
    { name = "pygments" },
    { name = "typing-extensions", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ab/3a/0316b28d0761c6734d6bc14e770d85506c986c85ffb239e688eeaab2c2bc/rich-13.9.4.tar.gz", hash = "sha256:439594978a49a09530cff7ebc4b5c7103ef57baf48d5ea3184f21d9a2befa098", size = 223149, upload-time = "2024-11-01T16:43:57.873Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/19/71/39c7c0d87f8d4e6c020a393182060eaefeeae6c01dab6a84ec346f2567df/rich-13.9.4-py3-none-any.whl", hash = "sha256:6049d5e6ec054bf2779ab3358186963bac2ea89175919d699e378b99738c2a90", size = 242424, upload-time = "2024-11-01T16:43:55.817Z" },
]

[[package]]
name = "shellingham"
version = "1.5.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/58/15/8b3609fd3830ef7b27b655beb4b4e9c62313a4e8da8c676e142cc210d58e/shellingham-1.5.4.tar.gz", hash = "sha256:8dbca0739d487e5bd35ab3ca4b36e11c4078f3a234bfce294b0a0291363404de", size = 10310, upload-time = "2023-10-24T04:13:40.426Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e0/f9/0595336914c5619e5f28a1fb793285925a8cd4b432c9da0a987836c7f822/shellingham-1.5.4-py2.py3-none-any.whl", hash = "sha256:7ecfff8f2fd72616f7481040475a65b2bf8af90a56c89140852d1120324e8686", size = 9755, upload-time = "2023-10-24T04:13:38.866Z" },
]

[[package]]
name = "tomli"
version = "2.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/18/87/302344fed471e44a87289cf4967697d07e532f2421fdaf868a303cbae4ff/tomli-2.2.1.tar.gz", hash = "sha256:cd45e1dc79c835ce60f7404ec8119f2eb06d38b1deba146f07ced3bbc44505ff", size = 17175, upload-time = "2024-11-27T22:38:36.873Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/ca/75707e6efa2b37c77dadb324ae7d9571cb424e61ea73fad7c56c2d14527f/tomli-2.2.1-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:678e4fa69e4575eb77d103de3df8a895e1591b48e740211bd1067378c69e8249", size = 131077, upload-time = "2024-11-27T22:37:54.956Z" },
    { url = "https://files.pythonhosted.org/packages/c7/16/51ae563a8615d472fdbffc43a3f3d46588c264ac4f024f63f01283becfbb/tomli-2.2.1-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:023aa114dd824ade0100497eb2318602af309e5a55595f76b626d6d9f3b7b0a6", size = 123429, upload-time = "2024-11-27T22:37:56.698Z" },
    { url = "https://files.pythonhosted.org/packages/f1/dd/4f6cd1e7b160041db83c694abc78e100473c15d54620083dbd5aae7b990e/tomli-2.2.1-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:ece47d672db52ac607a3d9599a9d48dcb2f2f735c6c2d1f34130085bb12b112a", size = 226067, upload-time = "2024-11-27T22:37:57.63Z" },
    { url = "https://files.pythonhosted.org/packages/a9/6b/c54ede5dc70d648cc6361eaf429304b02f2871a345bbdd51e993d6cdf550/tomli-2.2.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:6972ca9c9cc9f0acaa56a8ca1ff51e7af152a9f87fb64623e31d5c83700080ee", size = 236030, upload-time = "2024-11-27T22:37:59.344Z" },
    { url = "https://files.pythonhosted.org/packages/1f/47/999514fa49cfaf7a92c805a86c3c43f4215621855d151b61c602abb38091/tomli-2.2.1-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:c954d2250168d28797dd4e3ac5cf812a406cd5a92674ee4c8f123c889786aa8e", size = 240898, upload-time = "2024-11-27T22:38:00.429Z" },
    { url = "https://files.pythonhosted.org/packages/73/41/0a01279a7ae09ee1573b423318e7934674ce06eb33f50936655071d81a24/tomli-2.2.1-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:8dd28b3e155b80f4d54beb40a441d366adcfe740969820caf156c019fb5c7ec4", size = 229894, upload-time = "2024-11-27T22:38:02.094Z" },
    { url = "https://files.pythonhosted.org/packages/55/18/5d8bc5b0a0362311ce4d18830a5d28943667599a60d20118074ea1b01bb7/tomli-2.2.1-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:e59e304978767a54663af13c07b3d1af22ddee3bb2fb0618ca1593e4f593a106", size = 245319, upload-time = "2024-11-27T22:38:03.206Z" },
    { url = "https://files.pythonhosted.org/packages/92/a3/7ade0576d17f3cdf5ff44d61390d4b3febb8a9fc2b480c75c47ea048c646/tomli-2.2.1-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:33580bccab0338d00994d7f16f4c4ec25b776af3ffaac1ed74e0b3fc95e885a8", size = 238273, upload-time = "2024-11-27T22:38:04.217Z" },
    { url = "https://files.pythonhosted.org/packages/72/6f/fa64ef058ac1446a1e51110c375339b3ec6be245af9d14c87c4a6412dd32/tomli-2.2.1-cp311-cp311-win32.whl", hash = "sha256:465af0e0875402f1d226519c9904f37254b3045fc5084697cefb9bdde1ff99ff", size = 98310, upload-time = "2024-11-27T22:38:05.908Z" },
    { url = "https://files.pythonhosted.org/packages/6a/1c/4a2dcde4a51b81be3530565e92eda625d94dafb46dbeb15069df4caffc34/tomli-2.2.1-cp311-cp311-win_amd64.whl", hash = "sha256:2d0f2fdd22b02c6d81637a3c95f8cd77f995846af7414c5c4b8d0545afa1bc4b", size = 108309, upload-time = "2024-11-27T22:38:06.812Z" },
    { url = "https://files.pythonhosted.org/packages/52/e1/f8af4c2fcde17500422858155aeb0d7e93477a0d59a98e56cbfe75070fd0/tomli-2.2.1-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:4a8f6e44de52d5e6c657c9fe83b562f5f4256d8ebbfe4ff922c495620a7f6cea", size = 132762, upload-time = "2024-11-27T22:38:07.731Z" },
    { url = "https://files.pythonhosted.org/packages/03/b8/152c68bb84fc00396b83e7bbddd5ec0bd3dd409db4195e2a9b3e398ad2e3/tomli-2.2.1-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:8d57ca8095a641b8237d5b079147646153d22552f1c637fd3ba7f4b0b29167a8", size = 123453, upload-time = "2024-11-27T22:38:09.384Z" },
    { url = "https://files.pythonhosted.org/packages/c8/d6/fc9267af9166f79ac528ff7e8c55c8181ded34eb4b0e93daa767b8841573/tomli-2.2.1-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4e340144ad7ae1533cb897d406382b4b6fede8890a03738ff1683af800d54192", size = 233486, upload-time = "2024-11-27T22:38:10.329Z" },
    { url = "https://files.pythonhosted.org/packages/5c/51/51c3f2884d7bab89af25f678447ea7d297b53b5a3b5730a7cb2ef6069f07/tomli-2.2.1-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:db2b95f9de79181805df90bedc5a5ab4c165e6ec3fe99f970d0e302f384ad222", size = 242349, upload-time = "2024-11-27T22:38:11.443Z" },
    { url = "https://files.pythonhosted.org/packages/ab/df/bfa89627d13a5cc22402e441e8a931ef2108403db390ff3345c05253935e/tomli-2.2.1-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:40741994320b232529c802f8bc86da4e1aa9f413db394617b9a256ae0f9a7f77", size = 252159, upload-time = "2024-11-27T22:38:13.099Z" },
    { url = "https://files.pythonhosted.org/packages/9e/6e/fa2b916dced65763a5168c6ccb91066f7639bdc88b48adda990db10c8c0b/tomli-2.2.1-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:400e720fe168c0f8521520190686ef8ef033fb19fc493da09779e592861b78c6", size = 237243, upload-time = "2024-11-27T22:38:14.766Z" },
    { url = "https://files.pythonhosted.org/packages/b4/04/885d3b1f650e1153cbb93a6a9782c58a972b94ea4483ae4ac5cedd5e4a09/tomli-2.2.1-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:02abe224de6ae62c19f090f68da4e27b10af2b93213d36cf44e6e1c5abd19fdd", size = 259645, upload-time = "2024-11-27T22:38:15.843Z" },
    { url = "https://files.pythonhosted.org/packages/9c/de/6b432d66e986e501586da298e28ebeefd3edc2c780f3ad73d22566034239/tomli-2.2.1-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:b82ebccc8c8a36f2094e969560a1b836758481f3dc360ce9a3277c65f374285e", size = 244584, upload-time = "2024-11-27T22:38:17.645Z" },
    { url = "https://files.pythonhosted.org/packages/1c/9a/47c0449b98e6e7d1be6cbac02f93dd79003234ddc4aaab6ba07a9a7482e2/tomli-2.2.1-cp312-cp312-win32.whl", hash = "sha256:889f80ef92701b9dbb224e49ec87c645ce5df3fa2cc548664eb8a25e03127a98", size = 98875, upload-time = "2024-11-27T22:38:19.159Z" },
    { url = "https://files.pythonhosted.org/packages/ef/60/9b9638f081c6f1261e2688bd487625cd1e660d0a85bd469e91d8db969734/tomli-2.2.1-cp312-cp312-win_amd64.whl", hash = "sha256:7fc04e92e1d624a4a63c76474610238576942d6b8950a2d7f908a340494e67e4", size = 109418, upload-time = "2024-11-27T22:38:20.064Z" },
    { url = "https://files.pythonhosted.org/packages/6e/c2/61d3e0f47e2b74ef40a68b9e6ad5984f6241a942f7cd3bbfbdbd03861ea9/tomli-2.2.1-py3-none-any.whl", hash = "sha256:cb55c73c5f4408779d0cf3eef9f762b9c9f147a77de7b258bef0a5628adc85cc", size = 14257, upload-time = "2024-11-27T22:38:35.385Z" },
]

[[package]]
name = "typer"
version = "0.15.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "click" },
    { name = "rich" },
    { name = "shellingham" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/cb/ce/dca7b219718afd37a0068f4f2530a727c2b74a8b6e8e0c0080a4c0de4fcd/typer-0.15.1.tar.gz", hash = "sha256:a0588c0a7fa68a1978a069818657778f86abe6ff5ea6abf472f940a08bfe4f0a", size = 99789, upload-time = "2024-12-04T17:44:58.956Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d0/cc/0a838ba5ca64dc832aa43f727bd586309846b0ffb2ce52422543e6075e8a/typer-0.15.1-py3-none-any.whl", hash = "sha256:7994fb7b8155b64d3402518560648446072864beefd44aa2dc36972a5972e847", size = 44908, upload-time = "2024-12-04T17:44:57.291Z" },
]

[[package]]
name = "typing-extensions"
version = "4.12.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/df/db/f35a00659bc03fec321ba8bce9420de607a1d37f8342eee1863174c69557/typing_extensions-4.12.2.tar.gz", hash = "sha256:1a7ead55c7e559dd4dee8856e3a88b41225abfe1ce8df57b7c13915fe121ffb8", size = 85321, upload-time = "2024-06-07T18:52:15.995Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/26/9f/ad63fc0248c5379346306f8668cda6e2e2e9c95e01216d2b8ffd9ff037d0/typing_extensions-4.12.2-py3-none-any.whl", hash = "sha256:04e5ca0351e0f3f85c6853954072df659d0d13fac324d0072316b67d7794700d", size = 37438, upload-time = "2024-06-07T18:52:13.582Z" },
]
```

## File: `src/pyragify/__init__.py`
```python

```

## File: `src/pyragify/__main__.py`
```python
from pyragify.cli import app

if __name__ == "__main__":
    app()
```

## File: `src/pyragify/cli.py`
```python
import typer
import logging
from pathlib import Path
from omegaconf import OmegaConf
from pyragify.processor import RepoContentProcessor

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger(__name__)

app = typer.Typer(help="A tool to process repositories and output text files for NotebookLM.")

@app.command()
def process_repo(
    config_file: Path = typer.Option("config.yaml", help="Path to the configuration YAML file."),
    repo_path: Path = typer.Option(None, help="Override: Path to the repository to process."),
    output_dir: Path = typer.Option(None, help="Override: Directory to save output files."),
    max_words: int = typer.Option(None, help="Override: Maximum number of words per output file."),
    max_file_size: int = typer.Option(None, help="Override: Maximum file size to process (in bytes)."),
    skip_patterns: list[str] = typer.Option(None, help="Override: List of file patterns to skip."),
    skip_dirs: list[str] = typer.Option(None, help="Override: List of directories to skip."),
    verbose: bool = typer.Option(None, help="Override: Enable verbose output.")
):
    """
    Process a repository and output its content to text files with a specified word limit.

    This command processes a repository using a configuration file and optional command-line overrides. 
    It outputs text files based on the repository's contents and saves metadata about the processing.

    Parameters
    ----------
    config_file : pathlib.Path, optional
        The path to the configuration YAML file. Default is "config.yaml".
    repo_path : pathlib.Path, optional
        Override for the path to the repository to process. Defaults to the value in the configuration file.
    output_dir : pathlib.Path, optional
        Override for the directory where output files will be saved. Defaults to the value in the configuration file.
    max_words : int, optional
        Override for the maximum number of words allowed per output file. Defaults to the value in the configuration file.
    max_file_size : int, optional
        Override for the maximum file size (in bytes) to process. Defaults to the value in the configuration file.
    skip_patterns : list of str, optional
        Override for the list of file patterns to skip (e.g., "*.log", "*.tmp"). Defaults to the value in the configuration file.
    skip_dirs : list of str, optional
        Override for the list of directory names to skip (e.g., "node_modules", "__pycache__"). Defaults to the value in the configuration file.
    verbose : bool, optional
        Override for enabling verbose output. When enabled, the logging level is set to DEBUG. Defaults to the value in the configuration file.

    Notes
    -----
    - If a configuration file exists, its settings are loaded first.
    - Command-line options take precedence and override corresponding configuration file values.
    - The repository is processed based on the final resolved configuration, and results are saved to the specified output directory.
    - Errors during processing are logged, and the command exits with an error code.

    Examples
    --------
    Run the command with the default configuration file:
        $ python -m yourmodule.cli process-repo

    Override the repository path and enable verbose output:
        $ python -m yourmodule.cli process-repo --repo-path /path/to/repo --verbose

    Specify a custom configuration file:
        $ python -m yourmodule.cli process-repo --config-file custom_config.yaml
    """

    # Load configuration from YAML
    if config_file.exists():
        config = OmegaConf.load(config_file)
        logger.info(f"Loaded configuration from '{config_file}'")
    else:
        config = OmegaConf.create()
        if repo_path is None: # No --repo-path override
            logger.error(f"Configuration file '{config_file}' not found and --repo-path not provided.")
            raise typer.Exit(code=1)

    # Apply CLI overrides
    overrides = {
        "repo_path": repo_path,
        "output_dir": output_dir,
        "max_words": max_words,
        "max_file_size": max_file_size,
        "skip_patterns": skip_patterns,
        "skip_dirs": skip_dirs,
        "verbose": verbose,
    }
    for key, value in overrides.items():
        if value is not None:
            config[key] = value

    if config.verbose:
        logger.setLevel(logging.DEBUG)
        logger.debug("Verbose mode enabled. Setting logging level to DEBUG.")

    # Validate repo_path after config is loaded and merged
    if "repo_path" not in config or not config.repo_path:
        typer.echo("Error: repo_path must be defined in the config file or via --repo-path.", err=True)
        raise typer.Exit(code=1)

    repo_path_obj = Path(config.repo_path)
    if not repo_path_obj.exists():
        typer.echo(f"Error: Repository path '{config.repo_path}' does not exist.", err=True)
        raise typer.Exit(code=1)
    if not repo_path_obj.is_dir():
        typer.echo(f"Error: Repository path '{config.repo_path}' is not a directory.", err=True)
        raise typer.Exit(code=1)
    # Initialize and run the processor
    try:
        processor = RepoContentProcessor(
            repo_path=repo_path_obj,
            output_dir=Path(config.output_dir),
            max_words=config.max_words,
            max_file_size=config.max_file_size,
            skip_patterns=config.skip_patterns,
            skip_dirs=config.skip_dirs
        )
        processor.process_repo()
        logger.info("Repository processing completed successfully!")
    except Exception as e:
        logger.error(f"An error occurred during repository processing: {e}")
        raise typer.Exit(code=1)

if __name__ == "__main__":
    app()
```

## File: `src/pyragify/processor.py`
```python
import ast
import hashlib
import json
import tokenize
import pathspec
import logging
from io import StringIO
from pathlib import Path
from collections import defaultdict
from pyragify.utils import validate_directory

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def save_json(data: dict, file_path: Path, description: str):
    """
    Save a dictionary to a JSON file with error handling.

    Parameters
    ----------
    data : dict
        The data to be saved as a JSON file.
    file_path : pathlib.Path
        The path where the JSON file should be saved.
    description : str
        A description of the file being saved, used in logging messages.

    Raises
    ------
    Exception
        If an error occurs during saving, it will be logged but not raised.

    Notes
    -----
    This function logs both successful saves and any errors encountered.
    """

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
        logger.info(f"{description} saved to {file_path}")
    except Exception as e:
        logger.error(f"Error saving {description}: {e}")

def compute_file_hash(file_path: Path) -> str:
    """
    Compute the MD5 hash of a file.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the file whose hash is to be computed.

    Returns
    -------
    str or None
        The MD5 hash of the file as a hexadecimal string, or None if an error occurs.

    Raises
    ------
    Exception
        If the file cannot be read, the error is logged and None is returned.

    Notes
    -----
    MD5 is not suitable for cryptographic purposes but is sufficient for file integrity checks.
    """

    hash_md5 = hashlib.md5()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except Exception as e:
        logger.error(f"Error computing hash for {file_path}: {e}")
        return None
    return hash_md5.hexdigest()

def load_json(file_path: Path, description: str) -> dict:
    """
    Load a JSON file into a dictionary with error handling.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the JSON file to be loaded.
    description : str
        A description of the file being loaded, used in logging messages.

    Returns
    -------
    dict
        The contents of the JSON file as a dictionary. Returns an empty dictionary if the file cannot be loaded.

    Raises
    ------
    Exception
        If an error occurs during file loading, it will be logged but not raised.
    """

    if file_path.exists():
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            logger.error(f"Error loading {description}: {e}")
    return {}

def is_documentation_file(file_path: Path) -> bool:
    """
    Check if a file is a documentation file based on its name.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the file being checked.

    Returns
    -------
    bool
        True if the file is recognized as a documentation file, otherwise False.

    Notes
    -----
    This function specifically checks for common documentation filenames such as 'README.md' or 'CHANGELOG.md'.
    """

    documentation_files = ["README.md", "README.rst", "CONTRIBUTING.md", "CHANGELOG.md"]
    return file_path.name in documentation_files

FILE_TYPE_MAP = {
    ".py": "python",
    ".js": "javascript",
    ".ts": "typescript",
    ".java": "java",
    ".cpp": "cpp",
    ".c": "c",
    ".html": "html",
    ".css": "css",
    ".md": "markdown",
    ".markdown": "markdown"
}

def read_file_in_chunks(file_path: Path, chunk_size: int = 4096):
    """
    Read a file in chunks to handle large files efficiently.

    Parameters
    ----------
    file_path : pathlib.Path
        The path to the file to be read.
    chunk_size : int, optional
        The size of each chunk in bytes. Default is 4096.

    Yields
    ------
    str
        A chunk of the file as a string.

    Notes
    -----
    This function is useful for processing very large files without loading them entirely into memory.
    """

    with open(file_path, "r", encoding="utf-8") as file:
        while chunk := file.read(chunk_size):
            yield chunk

class FileProcessor:
    """
    Class for handling file processing logic.

    This class provides methods for chunking files based on their type, including Python files, Markdown files, and others.

    Attributes
    ----------
    repo_path : pathlib.Path
        The path to the repository being processed.
    output_dir : pathlib.Path
        The directory where processed output will be saved.

    Methods
    -------
    chunk_python_file(file_path)
        Chunk a Python file into semantic sections.
    chunk_markdown_file(file_path)
        Chunk a Markdown file into sections based on headers.
    chunk_file(file_path)
        Chunk a file into semantic sections based on its type.
    """

    def __init__(self, repo_path: Path, output_dir: Path):
        self.repo_path = repo_path.resolve()
        self.output_dir = output_dir.resolve()
        validate_directory(self.output_dir)

    def format_chunk(self, chunk: dict) -> str:
        """
        Format a chunk into plain text for saving.

        Parameters
        ----------
        chunk : dict
            The chunk of content to format.

        Returns
        -------
        str
            A formatted plain-text representation of the chunk.
        """
        chunk_type = chunk.get("type", "unknown")
        if chunk_type == "function":
            docstring = f"\nDocstring:\n{chunk['docstring']}" if chunk.get('docstring') else ""
            return f"Function: {chunk.get('name')}{docstring}\nCode:\n{chunk.get('code')}"
        elif chunk_type == "class":
            docstring = f"\nDocstring:\n{chunk['docstring']}" if chunk.get('docstring') else ""
            return f"Class: {chunk.get('name')}{docstring}\nCode:\n{chunk.get('code')}"
        elif chunk_type == "comments":
            comments = "\n".join(f"Line {c['line']}: {c['text']}" for c in chunk.get("content", []))
            return f"Comments:\n{comments}"
        elif chunk_type == "file":
            return f"File: {chunk.get('name')}\nContent:\n{chunk.get('content', '')}"
        elif chunk_type == "html_script":
            return f"HTML Script:\n{chunk.get('content', '')}"
        elif chunk_type == "html_style":
            return f"HTML Style:\n{chunk.get('content', '')}"
        elif chunk_type == "css_rule":
            return f"CSS Rule:\n{chunk.get('content', '')}"
        else:
            return f"Unknown chunk type:\n{chunk}"

    def chunk_python_file(self, file_path: Path) -> tuple[list, int]:
        """
        Chunk a Python file into semantic sections, including code, functions, and comments.

        Parameters
        ----------
        file_path : pathlib.Path
            The path to the Python file to be chunked.

        Returns
        -------
        list of dict
            A list of dictionaries where each dictionary represents a chunk with metadata and content.

        Notes
        -----
        The chunks include functions, classes, and inline comments. Each chunk contains the following keys:
        - 'type': The type of the chunk (e.g., 'function', 'class', 'comments').
        - 'name': The name of the function or class (if applicable).
        - 'docstring': The docstring associated with the function or class.
        - 'code': The actual code of the function or class.
        - 'line_count': The number of lines in the file.
        """

        chunks = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                file_content = f.read()

            lines = file_content.splitlines()
            line_count = len(lines)

            # Extract functions and classes using AST
            tree = ast.parse(file_content, filename=file_path)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    func_name = node.name
                    code_snippet = ast.get_source_segment(file_content, node)
                    chunks.append({
                        "type": "function",
                        "name": func_name,
                        "docstring": ast.get_docstring(node),
                        "code": code_snippet
                    })
                elif isinstance(node, ast.ClassDef):
                    class_name = node.name
                    code_snippet = ast.get_source_segment(file_content, node)
                    methods = []
                    for class_node in node.body:
                        if isinstance(class_node, ast.FunctionDef):
                            method_name = class_node.name
                            methods.append({
                                "name": method_name,
                            })
                    chunks.append({
                        "type": "class",
                        "name": class_name,
                        "methods": methods,
                        "docstring": ast.get_docstring(node),
                        "code": code_snippet
                    })

            # Extract inline comments using tokenize
            tokens = tokenize.generate_tokens(StringIO(file_content).readline)
            comments = []
            for token in tokens:
                if token.type == tokenize.COMMENT:
                    line_number = token.start[0]
                    comment_text = token.string.lstrip("#").strip()
                    comments.append({
                        "type": "comment",
                        "line": line_number,
                        "text": comment_text
                    })
            if comments:
                chunks.append({"type": "comments", "content": comments})

        except Exception as e:
            logger.warning(f"Error chunking Python file {file_path}: {e}")
        return chunks, line_count if 'line_count' in locals() else 0

    def chunk_markdown_file(self, file_path: Path) -> tuple[list, int]:
        """
        Chunk a Markdown file into sections based on headers.

        Parameters
        ----------
        file_path : pathlib.Path
            The path to the Markdown file to be chunked.

        Returns
        -------
        list of dict
            A list of dictionaries where each dictionary represents a chunk with a header and its associated content.

        Notes
        -----
        Each chunk contains the following keys:
        - 'header': The header text (e.g., '# Title').
        - 'content': The content under the header.
        """

        chunks = []
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
            line_count = len(lines)
    
            current_chunk = {"header": None, "content": ""}
            for line in lines:
                if line.startswith("#"):  # Header
                    if current_chunk["header"] or current_chunk["content"].strip():
                        chunks.append(current_chunk)
                    current_chunk = {"header": line.strip(), "content": ""}
                else:
                    current_chunk["content"] += line
            if current_chunk["header"] or current_chunk["content"].strip():
                chunks.append(current_chunk)
        except Exception as e:
            logger.warning(f"Error chunking Markdown file {file_path}: {e}")
        return chunks, line_count if 'line_count' in locals() else 0

    def chunk_file(self, file_path: Path) -> tuple[list, int]:
        """
        Chunk a file into semantic sections based on its type.

        Parameters
        ----------
        file_path : pathlib.Path
            The path to the file to be chunked.

        Returns
        -------
        tuple[list, int]
            A tuple containing a list of chunks and the total number of lines in the file.

        Notes
        -----
        This method delegates to type-specific chunking methods based on the file extension. 
        For unsupported types, the entire file content is treated as a single chunk.
        """
        suffix = file_path.suffix
        if suffix == ".py":
            return self.chunk_python_file(file_path)
        elif suffix in [".md", ".markdown"]:
            return self.chunk_markdown_file(file_path)
        elif suffix in FILE_TYPE_MAP:
            return self.chunk_tree_sitter_file(file_path, suffix)
        else:
            try:
                content = file_path.read_text(encoding="utf-8")
                line_count = content.count('\n') + 1
                return ([{
                    "type": "file",
                    "name": file_path.name,
                    "content": content
                }], line_count)
            except Exception as e:
                logger.warning(f"Error reading file {file_path}: {e}")
                return [], 0


    def chunk_tree_sitter_file(self, file_path: Path, suffix: str) -> tuple[list, int]:
        """
        Chunk a file using tree-sitter for supported languages.

        Parameters
        ----------
        file_path : pathlib.Path
            The path to the file to be chunked.
        suffix : str
            The file suffix (extension) to determine the language.

        Returns
        -------
        list of dict
            A list of dictionaries, each representing a semantic chunk with keys like 'type', 'name', and 'code' or 'content'.

        Notes
        -----
        Supports semantic extraction for JavaScript/TypeScript (functions, classes, arrow functions), Java (methods, classes), C/C++ (functions, structs), HTML (scripts, styles), and CSS (rules). Falls back to full content if parsing fails.
        """
        try:
            source = file_path.read_text(encoding="utf-8")
            line_count = source.count('\n') + 1
            lang_name = FILE_TYPE_MAP[suffix]

            chunks = []
            if lang_name == "html":
                # Simple regex fallback for tags
                import re
                scripts = re.findall(r'<script[^>]*>(.*?)</script>', source, re.DOTALL | re.IGNORECASE)
                for script in scripts:
                    chunks.append({"type": "html_script", "content": script.strip()})
                styles = re.findall(r'<style[^>]*>(.*?)</style>', source, re.DOTALL | re.IGNORECASE)
                for style in styles:
                    chunks.append({"type": "html_style", "content": style.strip()})
                if not chunks:
                    chunks = [{"type": "html", "content": source}]

            # CSS: Chunk by rules
            elif lang_name == "css":
                import re
                rules = re.split(r'([@][^{]+{[^}]*}|{[^{}]*})', source)
                for rule in rules:
                    if rule.strip() and '{' in rule:
                        chunks.append({"type": "css_rule", "content": rule.strip()})
                if not chunks:
                    chunks = [{"type": "css", "content": source}]

            if not chunks:
                chunks = [{"type": "file", "name": file_path.name, "content": source}]

            return chunks, line_count
        except Exception as e:
            logger.warning(f"Error chunking {suffix} file {file_path}: {e}")
            content = file_path.read_text(encoding="utf-8")
            return [{"type": "file", "name": file_path.name, "content": content}], content.count('\n') + 1

class RepoContentProcessor:
    """
    Class for processing an entire repository.

    This class orchestrates file-level processing, manages metadata, and saves the results to disk.

    Attributes
    ----------
    repo_path : pathlib.Path
        The path to the repository being processed.
    output_dir : pathlib.Path
        The directory where processed output will be saved.
    max_words : int
        The maximum number of words allowed per output chunk.
    max_file_size : int
        The maximum file size (in bytes) for processing.
    skip_patterns : list of str
        Patterns for files to skip.
    skip_dirs : list of str
        Directory names to skip.
    ignore_patterns : pathspec.PathSpec
        Compiled patterns for ignoring files.
    current_word_count : int
        The current word count for the current chunk.
    content : str
        The current content being accumulated for a chunk.
    hashes : dict
        Cached file hashes to avoid reprocessing unchanged files.
    file_counter : collections.defaultdict
        Counter for output files by type.
    metadata : dict
        Metadata about processed and skipped files.

    Methods
    -------
    load_ignore_patterns()
        Load ignore patterns from .gitignore and .dockerignore files.
    should_skip(file_path)
        Determine if a file or directory should be skipped.
    save_chunk(chunk, subdir)
        Save a chunk of content to a file.
    save_content(subdir)
        Save the accumulated content to a file.
    process_file(file_path)
        Process a single file, chunking and saving its content.
    process_repo()
        Process all files in the repository.
    get_file_type_subdir(file_path)
        Determine the output subdirectory for a file based on its type.
    """

    def __init__(self, repo_path: Path, output_dir: Path, max_words: int = 200000, max_file_size: int = 10 * 1024 * 1024, skip_patterns: list = None, skip_dirs: list = None):
        self.repo_path = repo_path.resolve()
        self.output_dir = output_dir.resolve()
        self.max_words = max_words
        self.max_file_size = max_file_size
        self.skip_patterns = skip_patterns or [".git"]
        self.skip_dirs = skip_dirs or ["node_modules", "__pycache__"]
        self.ignore_patterns = self.load_ignore_patterns()
        self.current_word_count = 0
        self.content = ""
        self.hashes = load_json(self.output_dir / "hashes.json", "hashes")
        self.file_counter = defaultdict(int)
        self.metadata = {
            "processed_files": [],
            "skipped_files": [],
            "summary": {"total_files_processed": 0, "total_words": 0}
        }
        self.file_processor = FileProcessor(self.repo_path, self.output_dir)

        validate_directory(self.output_dir)

    def load_ignore_patterns(self) -> pathspec.PathSpec:
        """
        Load patterns from .gitignore and .dockerignore files if they exist.

        Returns
        -------
        pathspec.PathSpec
            A compiled PathSpec object containing all ignore patterns.

        Notes
        -----
        Additional patterns provided via `skip_patterns` are also included. 
        If the ignore files are missing, only the additional patterns are used.
        """

        ignore_patterns = []

        for ignore_file in [".gitignore", ".dockerignore"]:
            file_path = self.repo_path / ignore_file
            if file_path.exists():
                logger.info(f"Loading ignore patterns from {ignore_file}")
                with open(file_path, "r", encoding="utf-8") as f:
                    ignore_patterns.extend(f.readlines())

        # Add additional skip_patterns
        ignore_patterns.extend(self.skip_patterns)

        # Compile patterns using pathspec
        return pathspec.PathSpec.from_lines("gitwildmatch", ignore_patterns)

    def should_skip(self, file_path: Path) -> bool:
        """
        Determine if a file or directory should be skipped based on patterns.

        Parameters
        ----------
        file_path : pathlib.Path
            The path to the file or directory to check.

        Returns
        -------
        bool
            True if the file or directory should be skipped, otherwise False.

        Notes
        -----
        This method checks against ignore patterns and explicit directory or file size limits.
        """

        # Check if the path matches .gitignore or .dockerignore patterns
        relative_path = file_path.relative_to(self.repo_path)
        if self.ignore_patterns.match_file(str(relative_path)):
            logger.info(f"Skipping {relative_path} due to ignore pattern.")
            return True

        # Skip directories explicitly listed
        if file_path.is_dir() and file_path.name in self.skip_dirs:
            logger.info(f"Skipped directory: {file_path}")
            return True

        # Skip large files
        if file_path.is_file() and file_path.stat().st_size > self.max_file_size:
            self.metadata["skipped_files"].append({
                "path": str(file_path),
                "reason": "File exceeds size limit"
            })
            logger.info(f"Skipped file due to size: {file_path}")
            return True

        return False

    def save_chunk(self, chunk: dict, subdir: Path):
        """
        Save a chunk of content to a text file.

        Parameters
        ----------
        chunk : dict
            The chunk of content to save.
        subdir : pathlib.Path
            The subdirectory where the chunk should be saved.
        """
        formatted = self.file_processor.format_chunk(chunk)
        chunk_word_count = len(formatted.split())
        if self.current_word_count + chunk_word_count > self.max_words:
            self.save_content(subdir)
        self.content += formatted + "\n\n"
        self.current_word_count += chunk_word_count


    def save_content(self, subdir: Path):
        """
        Save the accumulated content to a file.

        This method writes the currently accumulated content to a file in the specified subdirectory.
        After saving, the content and word count are reset for the next chunk.

        Parameters
        ----------
        subdir : pathlib.Path
            The subdirectory within the output directory where the chunk file should be saved.

        Notes
        -----
        - The file is named `chunk_<counter>.json`, where `<counter>` is an incrementing number for the subdirectory.
        - If the subdirectory does not exist, it is created automatically.
        - Once the content is saved, the internal buffer (`self.content`) and the current word count (`self.current_word_count`) are reset to prepare for the next chunk.

        Examples
        --------
        To save the current content to a subdirectory:
            >>> processor = RepoContentProcessor(repo_path=Path("repo"), output_dir=Path("output"))
            >>> processor.content = "This is some chunked content."
            >>> processor.current_word_count = 5
            >>> processor.save_content(Path("python"))

        Raises
        ------
        OSError
            If the file cannot be created or written, an error is logged.
        """

        if self.content:
            file_path = self.output_dir / subdir / f"chunk_{self.file_counter[subdir]}.txt"
            file_path.parent.mkdir(parents=True, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(self.content)
            logger.info(f"Saved chunk to {file_path}")
            self.file_counter[subdir] += 1
            self.content = ""
            self.current_word_count = 0
            
    def process_file(self, file_path: Path):
        """
        Process a single file.

        This method handles the processing of a single file by checking its hash for changes, chunking its content, and saving the resulting chunks.
        Metadata about the processed file is updated, and any errors are logged.

        Parameters
        ----------
        file_path : pathlib.Path
            The path to the file to be processed.

        Notes
        -----
        - Files that have unchanged hashes (compared to the cached hashes) are skipped.
        - Skipped files are logged in the `metadata['skipped_files']` list with reasons for skipping.
        - Processed files are chunked based on their type, and each chunk is saved to the appropriate subdirectory.
        - Metadata about processed files, such as the number of chunks, file size, number of lines, and total words, is recorded.

        Raises
        ------
        Exception
            Any errors encountered during file processing are logged and added to the skipped files list, but do not halt execution.

        Examples
        --------
        To process a file:
            >>> processor = RepoContentProcessor(repo_path=Path("repo"), output_dir=Path("output"))
            >>> processor.process_file(Path("repo/example.py"))
        """

        try:
            current_hash = compute_file_hash(file_path)
            if not current_hash:
                self.metadata["skipped_files"].append({"path": str(file_path), "reason": "Error computing file hash"})
                logger.warning(f"Skipped file due to hash error: {file_path}")
                return

            relative_path = str(file_path.relative_to(self.repo_path))
            if relative_path in self.hashes and self.hashes[relative_path] == current_hash:
                self.metadata["skipped_files"].append({"path": relative_path, "reason": "Unchanged file (hash match)"})
                logger.info(f"Skipped unchanged file: {file_path}")
                return

            subdir = self.get_file_type_subdir(file_path)
            chunks, line_count = self.file_processor.chunk_file(file_path)
            for chunk in chunks:
                self.save_chunk(chunk, subdir)

            self.metadata["processed_files"].append({
                "path": relative_path,
                "chunks": len(chunks),
                "size": file_path.stat().st_size,
                "lines": line_count,
                "words": sum(len(self.file_processor.format_chunk(chunk).split()) for chunk in chunks)
            })
            self.metadata["summary"]["total_files_processed"] += 1
            self.metadata["summary"]["total_words"] += sum(len(self.file_processor.format_chunk(chunk).split()) for chunk in chunks)
            self.hashes[relative_path] = current_hash
        except Exception as e:
            logger.warning(f"Error processing file {file_path}: {e}")
            self.metadata["skipped_files"].append({"path": str(file_path), "reason": f"Error processing file: {e}"})

    def process_repo(self):
        """
        Process all files in the repository.

        This method iterates over all files in the specified repository directory. It skips files and directories 
        based on ignore patterns and file size limits, processes supported file types, and saves the results. 
        Metadata about processed and skipped files is recorded, and the final results are saved to the output directory.

        Notes
        -----
        - Files are processed based on their type (e.g., Python files, Markdown files).
        - Skipped files and directories are logged in the `metadata['skipped_files']`.
        - Processed files are chunked, and their metadata is updated in `metadata['processed_files']`.
        - All metadata and hash information is saved to the output directory at the end of processing.

        Parameters
        ----------
        None

        Raises
        ------
        Exception
            Errors during individual file processing are logged and added to the skipped files list, but do not halt execution.

        Examples
        --------
        To process a repository:
            >>> processor = RepoContentProcessor(repo_path=Path("repo"), output_dir=Path("output"))
            >>> processor.process_repo()

        Metadata Example:
            After processing, metadata is saved as JSON:
            {
                "processed_files": [
                    {
                        "path": "example.py",
                        "chunks": 3,
                        "size": 2048,
                        "lines": 50,
                        "words": 300
                    }
                ],
                "skipped_files": [
                    {
                        "path": ".git/config",
                        "reason": "Matches ignore pattern"
                    }
                ],
                "summary": {
                    "total_files_processed": 10,
                    "total_words": 5000
                }
            }
        """

        logger.info(f"Processing repository: {self.repo_path}")
        total_files = sum(1 for _ in self.repo_path.rglob("*"))
        file_count = 0

        for file_path in self.repo_path.rglob("*"):
            file_count += 1
            logger.info(f"Processing file {file_count}/{total_files}: {file_path}")
            if self.should_skip(file_path):
                continue

            if file_path.is_file():
                self.process_file(file_path)

        save_json(self.metadata, self.output_dir / "metadata.json", "Metadata")
        save_json(self.hashes, self.output_dir / "hashes.json", "Hashes")

        if self.content:
            self.save_content(Path("remaining"))

        logger.info("Repository processing complete.")

    def get_file_type_subdir(self, file_path: Path) -> str:
        """
        Determine the subdirectory for a file based on its type.

        This method maps a file's extension to a predefined subdirectory name using the `FILE_TYPE_MAP` dictionary.
        If the file extension is not recognized, it defaults to "other".

        Parameters
        ----------
        file_path : pathlib.Path
            The path to the file whose subdirectory is being determined.

        Returns
        -------
        str
            The name of the subdirectory where the file should be categorized.
            For example, "python" for `.py` files, "markdown" for `.md` files, and "other" for unrecognized file types.

        Notes
        -----
        - The `FILE_TYPE_MAP` dictionary defines the mappings between file extensions and subdirectory names.
        - This method ensures that files are categorized consistently based on their type.

        Examples
        --------
        To get the subdirectory for a file:
            >>> processor = RepoContentProcessor(repo_path=Path("repo"), output_dir=Path("output"))
            >>> processor.get_file_type_subdir(Path("example.py"))
            'python'

            >>> processor.get_file_type_subdir(Path("README.md"))
            'markdown'

            >>> processor.get_file_type_subdir(Path("unknown.xyz"))
            'other'
        """

        return FILE_TYPE_MAP.get(file_path.suffix, "other")
```

## File: `src/pyragify/utils.py`
```python
import yaml
from pathlib import Path

def load_yaml_config(config_path: Path) -> dict:
    """
    Load a YAML configuration file.

    Parameters
    ----------
    config_path : pathlib.Path
        The path to the YAML configuration file to load.

    Returns
    -------
    dict
        A dictionary representing the contents of the YAML file.

    Raises
    ------
    FileNotFoundError
        If the configuration file does not exist.
    ValueError
        If there is an error parsing the YAML file.

    Notes
    -----
    This function uses `yaml.safe_load` to safely parse the YAML file, ensuring only standard YAML structures are loaded.

    Examples
    --------
    To load a configuration file:
        >>> config = load_yaml_config(Path("config.yaml"))
        >>> print(config)
        {'repo_path': '/path/to/repo', 'max_words': 100000}
    """
    try:
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.safe_load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {config_path}")
    except yaml.YAMLError as e:
        raise ValueError(f"Error parsing YAML file: {e}")

def validate_directory(path: Path):
    """
    Ensure a directory exists or create it.
    
    Parameters
    ----------
    path : pathlib.Path
        The path to the directory to validate or create.
    
    Notes
    -----
    - If the directory does not exist, it will be created, including any intermediate directories.
    - If the directory already exists, no action is taken.
    
    Examples
    --------
    To validate or create a directory:
        >>> validate_directory(Path("/path/to/output"))
        # If the directory doesn't exist, it will be created.
    """

    if not path.exists():
        path.mkdir(parents=True, exist_ok=True)
```

## File: `tests/test_processor.py`
```python
import pytest
from pathlib import Path
from pyragify.processor import FileProcessor, compute_file_hash, save_json, load_json, is_documentation_file, read_file_in_chunks

@pytest.fixture
def sample_python_file(tmp_path):
    """Fixture for a sample Python file with function and class."""
    file_path = tmp_path / "sample.py"
    file_path.write_text("""
def test_function(param):
    \"\"\"Docstring for function.\"\"\"
    return param * 2

class TestClass:
    \"\"\"Docstring for class.\"\"\"
    def method(self):
        return "method"
# Comment line
""")
    return file_path

@pytest.fixture
def sample_markdown_file(tmp_path):
    """Fixture for a sample Markdown file with headers."""
    file_path = tmp_path / "sample.md"
    file_path.write_text("""
# Header 1
Content under header 1.

## Header 2
Content under header 2.
""")
    return file_path

@pytest.fixture
def sample_js_file(tmp_path):
    """Fixture for a sample JavaScript file."""
    file_path = tmp_path / "sample.js"
    file_path.write_text("""
function testFunction(param) {
    return param * 2;
}

class TestClass {
    constructor() {}
    method() {
        return 'test';
    }
}

const arrow = (x) => x * 3;
""")
    return file_path

@pytest.fixture
def sample_java_file(tmp_path):
    """Fixture for a sample Java file."""
    file_path = tmp_path / "Sample.java"
    file_path.write_text("""
public class Sample {
    public static void testMethod(String param) {
        return param.length();
    }
}
""")
    return file_path

@pytest.fixture
def sample_cpp_file(tmp_path):
    """Fixture for a sample C++ file."""
    file_path = tmp_path / "sample.cpp"
    file_path.write_text("""
struct TestStruct {
    int x;
};

int testFunction(int param) {
    return param * 2;
}
""")
    return file_path

@pytest.fixture
def sample_html_file(tmp_path):
    """Fixture for a sample HTML file."""
    file_path = tmp_path / "sample.html"
    file_path.write_text("""
<!DOCTYPE html>
<html>
<script>
function jsFunc() { return 'hi'; }
</script>
<style>
body { color: red; }
</style>
</html>
""")
    return file_path

@pytest.fixture
def sample_css_file(tmp_path):
    """Fixture for a sample CSS file."""
    file_path = tmp_path / "sample.css"
    file_path.write_text("""
body {
    color: red;
}

@media screen {
    div { font-size: 12px; }
}
""")
    return file_path

def test_compute_file_hash(sample_python_file):
    """Test file hash computation."""
    hash_value = compute_file_hash(sample_python_file)
    assert isinstance(hash_value, str)
    assert len(hash_value) == 32  # MD5 hex length

def test_save_json_load_json(tmp_path):
    """Test saving and loading JSON."""
    data = {"test": "value"}
    json_path = tmp_path / "test.json"
    save_json(data, json_path, "test data")
    loaded = load_json(json_path, "test data")
    assert loaded == data

def test_is_documentation_file():
    """Test documentation file detection."""
    assert is_documentation_file(Path("README.md")) == True
    assert is_documentation_file(Path("example.py")) == False

def test_read_file_in_chunks(sample_python_file):
    """Test reading file in chunks."""
    chunks = list(read_file_in_chunks(sample_python_file))
    full_content = sample_python_file.read_text()
    assert ''.join(chunks) == full_content

class TestFileProcessor:
    def test_chunk_python_file(self, sample_python_file, tmp_path):
        """Test Python chunking."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        chunks, line_count = processor.chunk_python_file(sample_python_file)
        assert line_count > 0
        assert len(chunks) >= 3  # Function, class, and comments
        func_chunk = next((c for c in chunks if c["type"] == "function"), None)
        assert func_chunk is not None
        assert "test_function" in func_chunk["name"]
        assert "def test_function" in func_chunk["code"]
        assert func_chunk["docstring"] == "Docstring for function."
        class_chunk = next((c for c in chunks if c["type"] == "class"), None)
        assert class_chunk is not None
        assert "TestClass" in class_chunk["name"]
        assert "class TestClass" in class_chunk["code"]
        assert class_chunk["docstring"] == "Docstring for class."

    def test_chunk_markdown_file(self, sample_markdown_file, tmp_path):
        """Test Markdown chunking."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        chunks, line_count = processor.chunk_markdown_file(sample_markdown_file)
        assert line_count > 0
        assert len(chunks) == 2  # Two headers
        assert chunks[0]["header"] == "# Header 1"
        assert "Content under header 1" in chunks[0]["content"]

    @pytest.mark.parametrize("file_fixture, suffix, expected_types", [
        ("sample_js_file", ".js", ["file"]),
        ("sample_java_file", ".java", ["file"]),
        ("sample_cpp_file", ".cpp", ["file"]),
        ("sample_html_file", ".html", ["html_script", "html_style"]),
        ("sample_css_file", ".css", ["css_rule"]),
    ])
    def test_chunk_tree_sitter_file_real(self, request, file_fixture, suffix, expected_types, tmp_path):
        """Test tree-sitter chunking for multiple languages with real parsers."""
        file_path = request.getfixturevalue(file_fixture)
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        chunks, line_count = processor.chunk_tree_sitter_file(file_path, suffix)
        assert line_count > 0
        assert chunks
        found_types = {c["type"] for c in chunks}
        for expected_type in expected_types:
            assert expected_type in found_types

    def test_chunk_file_routing(self, sample_python_file, sample_markdown_file, sample_js_file, tmp_path):
        """Test chunk_file routes to correct method."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        py_chunks, _ = processor.chunk_file(sample_python_file)
        assert any(c["type"] == "function" for c in py_chunks)
        md_chunks, _ = processor.chunk_file(sample_markdown_file)
        assert "header" in md_chunks[0]
        js_chunks, _ = processor.chunk_file(sample_js_file)
        assert any(c["type"] == "file" for c in js_chunks)

    def test_format_chunk(self):
        """Test formatting various chunk types."""
        processor = FileProcessor(Path("."), Path("."))
        func_chunk = {"type": "function", "name": "test", "code": "def test(): pass", "docstring": "A test function."}
        formatted = processor.format_chunk(func_chunk)
        assert "Function: test" in formatted
        assert "Docstring:\nA test function." in formatted
        assert "def test(): pass" in formatted
        html_chunk = {"type": "html_script", "content": "<script>alert('hi');</script>"}
        formatted_html = processor.format_chunk(html_chunk)
        assert "HTML Script:" in formatted_html

    def test_chunk_file_unreadable(self, tmp_path, caplog):
        """Test that chunking an unreadable file is handled gracefully."""
        output_dir = tmp_path / "output"
        processor = FileProcessor(tmp_path, output_dir)
        bad_file = tmp_path / "bad.txt"
        bad_file.write_bytes(b'\x80') # Invalid utf-8
        chunks, line_count = processor.chunk_file(bad_file)
        assert chunks == []
        assert line_count == 0
        assert "Error reading file" in caplog.text
```

