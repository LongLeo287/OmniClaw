---
id: github.com-harehare-mq-python-a0620414-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:05.684260
---

# KNOWLEDGE EXTRACT: github.com_harehare_mq-python_a0620414
> **Extracted on:** 2026-04-01 09:30:43
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520230/github.com_harehare_mq-python_a0620414

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

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc
.DS_Store
```

## File: `.python-version`
```
3.11
```

## File: `Cargo.toml`
```
[package]
authors = ["Takahiro Sato <harehare1110@gmail.com>"]
categories = ["command-line-utilities", "text-processing"]
description = "Python bindings for mq Markdown processing"
edition = "2024"
homepage = "https://mqlang.org/"
keywords = ["markdown", "jq", "query"]
license = "MIT"
name = "mq-python"
publish = false
readme = "README.md"
repository = "https://github.com/harehare/mq"
version = "0.5.24"

[lib]
crate-type = ["cdylib"]
name = "mq"

[dependencies]
mq-lang = "0.5.24"
mq-markdown = "0.5.24"
pyo3 = {version = "0.28.2", features = ["extension-module", "abi3-py39"]}

```

## File: `README.md`
```markdown
<h1 align="center">mq-python</h1>

[![PyPI](https://img.shields.io/pypi/v/markdown-query.svg)](https://pypi.org/project/markdown-query/)

Python bindings for the mq Markdown processor.

## Installation

```bash
pip install markdown-query
```

## Usage

### Basic Usage

Use the `run` function to process Markdown with mq queries:

```python
import mq

# Extract all level 1 headings
result = mq.run(".h1", "# Hello World\n\n## Heading2\n\nText")
print(result.values)  # ['# Hello World']

# Extract all level 2 headings
result = mq.run(".h2", "# Main Title\n\n## Section A\n\n## Section B")
print(result.values)  # ['## Section A', '## Section B']

# Get all results as a single string
print(result.text)  # '## Section A\n## Section B'
```

### Filtering and Transforming

Use mq query syntax to filter and transform Markdown:

```python
import mq

markdown = """
# Product

## Features
Great features here.

## Installation
Install instructions.
"""

# Filter headings containing specific text
result = mq.run('.h2 | select(contains("Feature"))', markdown)
print(result.values)  # ['## Features']

# Extract list items
result = mq.run(".[]", "# List\n\n- Item 1\n- Item 2\n- Item 3")
print(result.values)  # ['- Item 1', '- Item 2', '- Item 3']

# Extract code blocks
result = mq.run(".code", "# Code\n\n```python\nprint('Hello')\n```")
print(result.values)  # ["```python\nprint('Hello')\n```"]
```

### Input Formats

mq supports multiple input formats:

```python
import mq

# Markdown (default)
options = mq.Options()
options.input_format = mq.InputFormat.MARKDOWN
result = mq.run(".h1", "# Heading", options)

# MDX (Markdown with JSX)
options = mq.Options()
options.input_format = mq.InputFormat.MDX
result = mq.run("select(is_mdx())", "# MDX\n\n<Component />", options)
print(result.values)  # ['<Component />']

# HTML
options = mq.Options()
options.input_format = mq.InputFormat.HTML
result = mq.run('select(contains("Hello"))', "<h1>Hello</h1><p>World</p>", options)
print(result.values)  # ['# Hello']

# Plain text
options = mq.Options()
options.input_format = mq.InputFormat.TEXT
result = mq.run('select(contains("2"))', "Line 1\nLine 2\nLine 3", options)
print(result.values)  # ['Line 2']
```

Available input formats:
- `InputFormat.MARKDOWN` - Standard Markdown (default)
- `InputFormat.MDX` - Markdown with JSX
- `InputFormat.HTML` - HTML content
- `InputFormat.TEXT` - Plain text
- `InputFormat.RAW` - Raw string input
- `InputFormat.NULL` - Null input

### Rendering Options

Customize the output rendering:

```python
import mq

options = mq.Options()
options.input_format = mq.InputFormat.MARKDOWN
options.list_style = mq.ListStyle.PLUS        # Use '+' for list items
options.link_title_style = mq.TitleSurroundStyle.SINGLE  # Use single quotes for link titles
options.link_url_style = mq.UrlSurroundStyle.ANGLE       # Use angle brackets for URLs

result = mq.run(".", markdown, options)
```

Available options:
- `ListStyle`: `DASH` (default), `PLUS`, `STAR`
- `TitleSurroundStyle`: `DOUBLE` (default), `SINGLE`, `PAREN`
- `UrlSurroundStyle`: `NONE` (default), `ANGLE`

### HTML to Markdown Conversion

Convert HTML to Markdown:

```python
import mq

html = "<h1>Hello World</h1><p>This is a <strong>test</strong>.</p>"
markdown = mq.html_to_markdown(html)
print(markdown)  # '# Hello World\n\nThis is a **test**.'

# With conversion options
options = mq.ConversionOptions()
options.extract_scripts_as_code_blocks = True  # Convert <script> tags to code blocks
options.generate_front_matter = True           # Generate front matter from metadata
options.use_title_as_h1 = True                 # Use <title> as h1 heading

markdown = mq.html_to_markdown(html, options)
```

### Working with Results

The `run` function returns an `MQResult` object:

```python
import mq

result = mq.run(".h", "# H1\n\n## H2\n\n### H3")

# Get the number of results
print(len(result))  # 3

# Access individual results by index
print(result[0].text)  # '# H1'

# Iterate over results
for value in result.values:
    print(value)

# Get all results as a single string
print(result.text)  # '# H1\n## H2\n### H3'

# Check if a value is in the result
print("# H1" in result.values)  # True
```

Each `MQValue` has the following properties:
- `text` - The string representation of the value
- `values` - For arrays, returns the list of values
- `markdown_type` - The type of Markdown element (e.g., `Heading`, `Code`, `List`)
- `is_array()` - Check if the value is an array
- `is_markdown()` - Check if the value is a Markdown element

### Error Handling

Invalid queries raise a `RuntimeError`:

```python
import mq

try:
    result = mq.run(".invalid!!!", "# Heading")
except RuntimeError as e:
    print(f"Query error: {e}")
```

## Development

### Building from Source

```bash
git clone https://github.com/harehare/mq
cd mq/crates/mq-python
pip install maturin
maturin develop
```

### Running Tests

```bash
pytest tests/
```
## Support

- 🐛 [Report bugs](https://github.com/harehare/mq/issues)
- 💡 [Request features](https://github.com/harehare/mq/issues)
- 📖 [Read the documentation](https://mqlang.org/book/)
- 📦 [PyPI package](https://pypi.org/project/markdown-query/)

## License

Licensed under the MIT License.
```

## File: `pyproject.toml`
```
[project]
authors = [
  {name = "harehare", email = "harehare1110@gmail.com"},
]
classifiers = [
  "Programming Language :: Rust",
  "Programming Language :: Python",
]
dependencies = []
description = "Python bindings for mq, a jq-like command-line tool for Markdown processing"
keywords = ["markdown", "jq", "command-line", "tool"]
license = {text = "MIT"}
name = "markdown-query"
readme = "README.md"
requires-python = ">=3.10"
version = "0.5.24"

[tool.maturin]
module-name = "mq.mq"
python-packages = ["mq"]
python-source = "src"

[build-system]
build-backend = "maturin"
requires = ["maturin>=1.0,<2.0"]

[dependency-groups]
dev = [
  "maturin>=1.0,<2.0",
  "pytest>=8.3.5",
]

[project.urls]
Documentation = "https://mqlang.org/book/"
Homepage = "https://mqlang.org/"
Issues = "https://github.com/harehare/mq/issues"
Repository = "https://github.com/harehare/mq.git"
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.10"

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
version = "1.2.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/09/35/2495c4ac46b980e4ca1f6ad6db102322ef3ad2410b79fdde159a4b0f3b92/exceptiongroup-1.2.2.tar.gz", hash = "sha256:47c2edf7c6738fafb49fd34290706d1a1a2f4d1c6df275526b62cbb4aa5393cc", size = 28883, upload-time = "2024-07-12T22:26:00.161Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/02/cc/b7e31358aac6ed1ef2bb790a9746ac2c69bcb3c8588b41616914eb106eaf/exceptiongroup-1.2.2-py3-none-any.whl", hash = "sha256:3111b9d131c238bec2f8f516e123e14ba243563fb135d3fe885990585aa7795b", size = 16453, upload-time = "2024-07-12T22:25:58.476Z" },
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
name = "markdown-query"
version = "0.5.24"
source = { editable = "." }

[package.dev-dependencies]
dev = [
    { name = "maturin" },
    { name = "pytest" },
]

[package.metadata]

[package.metadata.requires-dev]
dev = [
    { name = "maturin", specifier = ">=1.0,<2.0" },
    { name = "pytest", specifier = ">=8.3.5" },
]

[[package]]
name = "maturin"
version = "1.12.4"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/2f/a6/54e73f0ec0224488ae25196ce8b4df298cae613b099ad0c4f39dd7e3a8d2/maturin-1.12.4.tar.gz", hash = "sha256:06f6438be7e723aaf4b412fb34839854b540a1350f7614fadf5bd1db2b98d5f7", size = 262134, upload-time = "2026-02-21T10:24:25.64Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e1/cd/8285f37bf968b8485e3c7eb43349a5adbccfddfc487cd4327fb9104578cc/maturin-1.12.4-py3-none-linux_armv6l.whl", hash = "sha256:cf8a0eddef9ab8773bc823c77aed3de9a5c85fb760c86448048a79ef89794c81", size = 9758449, upload-time = "2026-02-21T10:24:35.382Z" },
    { url = "https://files.pythonhosted.org/packages/d9/91/f51191db83735f77bc988c8034730bb63b750a4a1a04f9c8cba10f44ad45/maturin-1.12.4-py3-none-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl", hash = "sha256:eba1bd1c1513d00fec75228da98622c68a9f50f9693aaa6fb7dacb244e7bbf26", size = 18938848, upload-time = "2026-02-21T10:24:10.701Z" },
    { url = "https://files.pythonhosted.org/packages/65/47/03c422adeac93b903354b322bba632754fdb134b27ace71b5603feba5906/maturin-1.12.4-py3-none-macosx_10_12_x86_64.whl", hash = "sha256:89749cfc0e6baf5517fa370729a98955552e42fefc406b95732d5c8e85bc90c0", size = 9791641, upload-time = "2026-02-21T10:24:21.72Z" },
    { url = "https://files.pythonhosted.org/packages/5e/30/dd78acf6afc48d358512b5ed928fd24e2bc6b68db69b1f6bba3ffd7bcaed/maturin-1.12.4-py3-none-manylinux_2_12_i686.manylinux2010_i686.musllinux_1_1_i686.whl", hash = "sha256:4d68664e5b81f282144a3b717a7e8593ec94ac87d7ae563a4c464e93d6cde877", size = 9811625, upload-time = "2026-02-21T10:24:08.152Z" },
    { url = "https://files.pythonhosted.org/packages/e3/9a/a6e358a18815ab090ef55187da0066df01a955c7c44a61fb83b127055f23/maturin-1.12.4-py3-none-manylinux_2_12_x86_64.manylinux2010_x86_64.musllinux_1_1_x86_64.whl", hash = "sha256:88e09e6c386b08974fab0c7e4c07d7c7c50a0ba63095d31e930d80568488e1be", size = 10255812, upload-time = "2026-02-21T10:24:15.117Z" },
    { url = "https://files.pythonhosted.org/packages/4a/c5/84dfcce1f3475237cba6e6201a1939980025afbb41c076aa5147b10ac202/maturin-1.12.4-py3-none-manylinux_2_17_aarch64.manylinux2014_aarch64.musllinux_1_1_aarch64.whl", hash = "sha256:5cc56481b0f360571587c35a1d960ce6d0a0258d49aebb6af98fff9db837c337", size = 9645462, upload-time = "2026-02-21T10:24:28.814Z" },
    { url = "https://files.pythonhosted.org/packages/de/82/0845fff86ea044028302db17bc611e9bfe1b7b2c992756162cbe71267df5/maturin-1.12.4-py3-none-manylinux_2_17_armv7l.manylinux2014_armv7l.musllinux_1_1_armv7l.whl", hash = "sha256:8fd7eb0c9bb017e98d81aa86a1d440b912fe4f7f219571035dd6ab330c82071c", size = 9593649, upload-time = "2026-02-21T10:24:33.376Z" },
    { url = "https://files.pythonhosted.org/packages/2b/14/6e8969cd48c7c8ea27d7638e572d46eeba9aa0cb370d3031eb6a3f10ff8d/maturin-1.12.4-py3-none-manylinux_2_17_ppc64le.manylinux2014_ppc64le.musllinux_1_1_ppc64le.whl", hash = "sha256:5bb07c349dd066277a61e017a6d6e0860cd54b7b33f8ead10b9e5a4ffb740a0a", size = 12681515, upload-time = "2026-02-21T10:24:31.097Z" },
    { url = "https://files.pythonhosted.org/packages/ac/8d/2ad86623dca3cfa394049f4220188dececa6e4cefd73ac1f1385fc79c876/maturin-1.12.4-py3-none-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:c21baaed066b5bec893db2d261bfe3b9da054d99c018326f0bdcf1dc4c3a1eb9", size = 10448453, upload-time = "2026-02-21T10:24:26.827Z" },
    { url = "https://files.pythonhosted.org/packages/9c/eb/c66e2d3272e74dd590ae81bb51590bd98c3cd4e3f6629d4e4218bd6a5c28/maturin-1.12.4-py3-none-manylinux_2_31_riscv64.musllinux_1_1_riscv64.whl", hash = "sha256:939c4c57efa8ea982a991ee3ccb3992364622e9cbd1ede922b5cfb0f652bf517", size = 9970879, upload-time = "2026-02-21T10:24:12.881Z" },
    { url = "https://files.pythonhosted.org/packages/38/a0/998f8063d67fa19639179af7e8ea46016ceaa12f85b9720a2e4846449f43/maturin-1.12.4-py3-none-win32.whl", hash = "sha256:d72f626616292cb3e283941f47835ffc608207ebd8f95f4c50523a6631ffcb2e", size = 8518146, upload-time = "2026-02-21T10:24:17.296Z" },
    { url = "https://files.pythonhosted.org/packages/69/14/6ceea315db6e47093442ec70c2d01bb011d69f5243de5fc0e6a5fab97513/maturin-1.12.4-py3-none-win_amd64.whl", hash = "sha256:ab32c5ff7579a549421cae03e6297d3b03d7b81fa2934e3bdf24a102d99eb378", size = 9863686, upload-time = "2026-02-21T10:24:19.35Z" },
    { url = "https://files.pythonhosted.org/packages/d4/28/73e14739c6f7605ff9b9d108726d3ff529d4f91a7838739b4dd0afd33ec1/maturin-1.12.4-py3-none-win_arm64.whl", hash = "sha256:b8c05d24209af50ed9ae9e5de473c84866b9676c637fcfad123ee57f4a9ed098", size = 8557843, upload-time = "2026-02-21T10:24:23.894Z" },
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
name = "pluggy"
version = "1.5.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/96/2d/02d4312c973c6050a18b314a5ad0b3210edb65a906f868e31c111dede4a6/pluggy-1.5.0.tar.gz", hash = "sha256:2cffa88e94fdc978c4c574f15f9e59b7f4201d439195c3715ca9e2486f1d0cf1", size = 67955, upload-time = "2024-04-20T21:34:42.531Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/88/5f/e351af9a41f866ac3f1fac4ca0613908d9a41741cfcf2228f4ad853b697d/pluggy-1.5.0-py3-none-any.whl", hash = "sha256:44e1ad92c8ca002de6377e165f3e0f1be63266ab4d554740532335b9d75ea669", size = 20556, upload-time = "2024-04-20T21:34:40.434Z" },
]

[[package]]
name = "pytest"
version = "8.3.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "colorama", marker = "sys_platform == 'win32'" },
    { name = "exceptiongroup", marker = "python_full_version < '3.11'" },
    { name = "iniconfig" },
    { name = "packaging" },
    { name = "pluggy" },
    { name = "tomli", marker = "python_full_version < '3.11'" },
]
sdist = { url = "https://files.pythonhosted.org/packages/ae/3c/c9d525a414d506893f0cd8a8d0de7706446213181570cdbd766691164e40/pytest-8.3.5.tar.gz", hash = "sha256:f4efe70cc14e511565ac476b57c279e12a855b11f48f212af1080ef2263d3845", size = 1450891, upload-time = "2025-03-02T12:54:54.503Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/30/3d/64ad57c803f1fa1e963a7946b6e0fea4a70df53c1a7fed304586539c2bac/pytest-8.3.5-py3-none-any.whl", hash = "sha256:c69214aa47deac29fad6c2a4f590b9c4a9fdb16a403176fe154b79c0b4d4d820", size = 343634, upload-time = "2025-03-02T12:54:52.069Z" },
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
    { url = "https://files.pythonhosted.org/packages/04/90/2ee5f2e0362cb8a0b6499dc44f4d7d48f8fff06d28ba46e6f1eaa61a1388/tomli-2.2.1-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:f4039b9cbc3048b2416cc57ab3bda989a6fcf9b36cf8937f01a6e731b64f80d7", size = 132708, upload-time = "2024-11-27T22:38:21.659Z" },
    { url = "https://files.pythonhosted.org/packages/c0/ec/46b4108816de6b385141f082ba99e315501ccd0a2ea23db4a100dd3990ea/tomli-2.2.1-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:286f0ca2ffeeb5b9bd4fcc8d6c330534323ec51b2f52da063b11c502da16f30c", size = 123582, upload-time = "2024-11-27T22:38:22.693Z" },
    { url = "https://files.pythonhosted.org/packages/a0/bd/b470466d0137b37b68d24556c38a0cc819e8febe392d5b199dcd7f578365/tomli-2.2.1-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:a92ef1a44547e894e2a17d24e7557a5e85a9e1d0048b0b5e7541f76c5032cb13", size = 232543, upload-time = "2024-11-27T22:38:24.367Z" },
    { url = "https://files.pythonhosted.org/packages/d9/e5/82e80ff3b751373f7cead2815bcbe2d51c895b3c990686741a8e56ec42ab/tomli-2.2.1-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:9316dc65bed1684c9a98ee68759ceaed29d229e985297003e494aa825ebb0281", size = 241691, upload-time = "2024-11-27T22:38:26.081Z" },
    { url = "https://files.pythonhosted.org/packages/05/7e/2a110bc2713557d6a1bfb06af23dd01e7dde52b6ee7dadc589868f9abfac/tomli-2.2.1-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e85e99945e688e32d5a35c1ff38ed0b3f41f43fad8df0bdf79f72b2ba7bc5272", size = 251170, upload-time = "2024-11-27T22:38:27.921Z" },
    { url = "https://files.pythonhosted.org/packages/64/7b/22d713946efe00e0adbcdfd6d1aa119ae03fd0b60ebed51ebb3fa9f5a2e5/tomli-2.2.1-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:ac065718db92ca818f8d6141b5f66369833d4a80a9d74435a268c52bdfa73140", size = 236530, upload-time = "2024-11-27T22:38:29.591Z" },
    { url = "https://files.pythonhosted.org/packages/38/31/3a76f67da4b0cf37b742ca76beaf819dca0ebef26d78fc794a576e08accf/tomli-2.2.1-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:d920f33822747519673ee656a4b6ac33e382eca9d331c87770faa3eef562aeb2", size = 258666, upload-time = "2024-11-27T22:38:30.639Z" },
    { url = "https://files.pythonhosted.org/packages/07/10/5af1293da642aded87e8a988753945d0cf7e00a9452d3911dd3bb354c9e2/tomli-2.2.1-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:a198f10c4d1b1375d7687bc25294306e551bf1abfa4eace6650070a5c1ae2744", size = 243954, upload-time = "2024-11-27T22:38:31.702Z" },
    { url = "https://files.pythonhosted.org/packages/5b/b9/1ed31d167be802da0fc95020d04cd27b7d7065cc6fbefdd2f9186f60d7bd/tomli-2.2.1-cp313-cp313-win32.whl", hash = "sha256:d3f5614314d758649ab2ab3a62d4f2004c825922f9e370b29416484086b264ec", size = 98724, upload-time = "2024-11-27T22:38:32.837Z" },
    { url = "https://files.pythonhosted.org/packages/c7/32/b0963458706accd9afcfeb867c0f9175a741bf7b19cd424230714d722198/tomli-2.2.1-cp313-cp313-win_amd64.whl", hash = "sha256:a38aa0308e754b0e3c67e344754dff64999ff9b513e691d0e786265c93583c69", size = 109383, upload-time = "2024-11-27T22:38:34.455Z" },
    { url = "https://files.pythonhosted.org/packages/6e/c2/61d3e0f47e2b74ef40a68b9e6ad5984f6241a942f7cd3bbfbdbd03861ea9/tomli-2.2.1-py3-none-any.whl", hash = "sha256:cb55c73c5f4408779d0cf3eef9f762b9c9f147a77de7b258bef0a5628adc85cc", size = 14257, upload-time = "2024-11-27T22:38:35.385Z" },
]
```

## File: `src/lib.rs`
```rust
//! Python bindings for the mq markdown processing library.
//!
//! This crate provides Python bindings for mq, allowing Python applications to
//! process markdown, MDX, and HTML using the mq query language.
//!
//! # Features
//!
//! - Process markdown, MDX, HTML, and plain text from Python
//! - Full mq query language support
//! - Multiple input and output format options
//! - Configurable rendering options
//! - Type-safe Python API using PyO3
//!
//! # Installation
//!
//! ```bash
//! pip install mq
//! ```
//!
//! # Python Usage
//!
//! Basic usage example:
//!
//! ```python
//! import mq
//!
//! # Process markdown with mq
//! result = mq.run('.h', '# Hello\n## World', mq.Options(input_format=mq.InputFormat.MARKDOWN))
//! for value in result.values:
//!     print(value)
//! ```
//!
//! Filter and transform markdown:
//!
//! ```python
//! import mq
//!
//! markdown = """
//! # Introduction
//! Some text here.
//!
//! ## Section 1
//! More content.
//!
//! ## Section 2
//! Even more content.
//! """
//!
//! # Get only level 2 headings
//! result = mq.run('.h | select(level == 2)', markdown)
//! for heading in result.values:
//!     print(heading)
//! ```
//!
//! # Input Formats
//!
//! Supported input formats:
//! - `InputFormat.MARKDOWN` - Standard markdown
//! - `InputFormat.MDX` - Markdown with JSX
//! - `InputFormat.HTML` - HTML content
//! - `InputFormat.TEXT` - Plain text
//! - `InputFormat.RAW` - Raw string input
//! - `InputFormat.NULL` - Null input
//!
//! # Configuration
//!
//! Customize rendering with options:
//!
//! ```python
//! import mq
//!
//! options = mq.Options()
//! options.input_format = mq.InputFormat.MARKDOWN
//! options.list_style = mq.ListStyle.PLUS
//! options.link_title_style = mq.TitleSurroundStyle.SINGLE
//!
//! result = mq.run('.', markdown, options)
//! ```
pub mod result;
pub mod value;

use pyo3::prelude::*;
use result::MQResult;
use value::MQValue;

#[pyclass(eq, eq_int, from_py_object)]
#[derive(Debug, Clone, Copy, PartialEq, Default)]
enum InputFormat {
    #[pyo3(name = "MARKDOWN")]
    #[default]
    Markdown,
    #[pyo3(name = "MDX")]
    Mdx,
    #[pyo3(name = "TEXT")]
    Text,
    #[pyo3(name = "HTML")]
    Html,
    #[pyo3(name = "RAW")]
    Raw,
    #[pyo3(name = "NULL")]
    Null,
}

#[pyclass(eq, eq_int, from_py_object)]
#[derive(Debug, Clone, Copy, PartialEq, Default)]
pub enum ListStyle {
    #[pyo3(name = "DASH")]
    #[default]
    Dash,
    #[pyo3(name = "PLUS")]
    Plus,
    #[pyo3(name = "STAR")]
    Star,
}

#[pyclass(eq, eq_int, from_py_object)]
#[derive(Debug, Clone, Copy, PartialEq, Default)]
pub enum TitleSurroundStyle {
    #[pyo3(name = "DOUBLE")]
    #[default]
    Double,
    #[pyo3(name = "SINGLE")]
    Single,
    #[pyo3(name = "PAREN")]
    PAREN,
}

#[pyclass(eq, eq_int, from_py_object)]
#[derive(Debug, Clone, Copy, PartialEq, Default)]
pub enum UrlSurroundStyle {
    #[pyo3(name = "ANGLE")]
    Angle,
    #[pyo3(name = "NONE")]
    #[default]
    None,
}

#[pyclass(eq, from_py_object)]
#[derive(Debug, Clone, Copy, PartialEq, Default)]
struct Options {
    #[pyo3(get, set)]
    input_format: Option<InputFormat>,
    #[pyo3(get, set)]
    list_style: Option<ListStyle>,
    #[pyo3(get, set)]
    link_title_style: Option<TitleSurroundStyle>,
    #[pyo3(get, set)]
    link_url_style: Option<UrlSurroundStyle>,
}

#[pymethods]
impl Options {
    #[new]
    pub fn new() -> Self {
        Self::default()
    }
}

#[pyclass(eq, from_py_object)]
#[derive(Debug, Clone, Copy, PartialEq, Default)]
struct ConversionOptions {
    #[pyo3(get, set)]
    extract_scripts_as_code_blocks: bool,
    #[pyo3(get, set)]
    generate_front_matter: bool,
    #[pyo3(get, set)]
    use_title_as_h1: bool,
}

#[pymethods]
impl ConversionOptions {
    #[new]
    pub fn new() -> Self {
        Self::default()
    }
}

#[pyfunction]
#[pyo3(signature = (code, content, options=None))]
fn run(code: &str, content: &str, options: Option<Options>) -> PyResult<MQResult> {
    let mut engine = mq_lang::DefaultEngine::default();
    engine.load_builtin_module();
    let options = options.unwrap_or_default();
    let input = match options.input_format.unwrap_or(InputFormat::Markdown) {
        InputFormat::Markdown => mq_lang::parse_markdown_input(content),
        InputFormat::Mdx => mq_lang::parse_mdx_input(content),
        InputFormat::Text => mq_lang::parse_text_input(content),
        InputFormat::Html => mq_lang::parse_html_input(content),
        InputFormat::Raw => Ok(mq_lang::raw_input(content)),
        InputFormat::Null => Ok(mq_lang::null_input()),
    }
    .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Error evaluating query: {}", e)))?;

    engine
        .eval(code, input.into_iter())
        .map(|values| MQResult {
            values: values.into_iter().map(Into::into).collect::<Vec<_>>(),
        })
        .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Error evaluating query: {}", e)))
}

#[pyfunction]
#[pyo3(signature = (content, options=None))]
fn html_to_markdown(content: &str, options: Option<ConversionOptions>) -> PyResult<String> {
    mq_markdown::convert_html_to_markdown(
        content,
        match options {
            Some(opts) => mq_markdown::ConversionOptions {
                extract_scripts_as_code_blocks: opts.extract_scripts_as_code_blocks,
                generate_front_matter: opts.generate_front_matter,
                use_title_as_h1: opts.use_title_as_h1,
            },
            None => mq_markdown::ConversionOptions::default(),
        },
    )
    .map_err(|e| PyErr::new::<pyo3::exceptions::PyRuntimeError, _>(format!("Error converting HTML to Markdown: {}", e)))
}

#[pymodule]
fn mq(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<InputFormat>()?;
    m.add_class::<ListStyle>()?;
    m.add_class::<UrlSurroundStyle>()?;
    m.add_class::<TitleSurroundStyle>()?;
    m.add_class::<Options>()?;
    m.add_class::<MQResult>()?;
    m.add_class::<MQValue>()?;
    m.add_class::<ConversionOptions>()?;
    m.add_function(wrap_pyfunction!(run, m)?)?;
    m.add_function(wrap_pyfunction!(html_to_markdown, m)?)?;
    Ok(())
}
```

## File: `src/result.rs`
```rust
use crate::value::MQValue;

use pyo3::prelude::*;

#[pyclass]
pub struct MQResult {
    pub values: Vec<MQValue>,
}

#[pymethods]
impl MQResult {
    #[getter]
    pub fn text(&self) -> String {
        self.values().join("\n")
    }

    #[getter]
    pub fn values(&self) -> Vec<String> {
        self.values
            .iter()
            .filter_map(|value| if value.__len__() == 0 { None } else { Some(value.text()) })
            .collect::<Vec<String>>()
    }

    pub fn __len__(&self) -> usize {
        self.values.len()
    }

    pub fn __contains__(&self, value: &MQValue) -> PyResult<bool> {
        Ok(self.values.iter().any(|v| v == value))
    }

    pub fn __getitem__(&self, idx: usize) -> PyResult<MQValue> {
        if idx < self.values.len() {
            Ok(self.values[idx].clone())
        } else {
            Err(pyo3::exceptions::PyIndexError::new_err(format!(
                "Index {} out of range for MQResult with length {}",
                idx,
                self.values.len()
            )))
        }
    }

    fn __repr__(&self) -> String {
        format!("MQResult({} items)", self.values.len())
    }

    fn __str__(&self) -> String {
        self.text()
    }

    fn __eq__(&self, other: &Self) -> bool {
        if self.values.len() != other.values.len() {
            return false;
        }

        self.values.iter().zip(other.values.iter()).all(|(a, b)| a.__eq__(b))
    }

    fn __ne__(&self, other: &Self) -> bool {
        !self.__eq__(other)
    }

    fn __lt__(&self, other: &Self) -> bool {
        if self.values.len() != other.values.len() {
            return self.values.len() < other.values.len();
        }

        self.values.iter().zip(other.values.iter()).all(|(a, b)| a.__lt__(b))
    }

    fn __gt__(&self, other: &Self) -> bool {
        if self.values.len() != other.values.len() {
            return self.values.len() > other.values.len();
        }

        self.values.iter().zip(other.values.iter()).all(|(a, b)| a.__gt__(b))
    }
}

impl From<Vec<MQValue>> for MQResult {
    fn from(values: Vec<MQValue>) -> Self {
        Self { values }
    }
}
```

## File: `src/value.rs`
```rust
use pyo3::pyclass;
use std::{collections::HashMap, fmt};

#[pyclass(from_py_object)]
#[derive(Debug, Clone)]
pub enum MQValue {
    Array { value: Vec<MQValue> },
    Dict { value: HashMap<String, MQValue> },
    Markdown { value: String, markdown_type: MarkdownType },
}

impl fmt::Display for MQValue {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        match self {
            MQValue::Array { value } => write!(
                f,
                "{}",
                value.iter().map(|val| val.text()).collect::<Vec<String>>().join("\n")
            ),
            MQValue::Dict { value } => write!(
                f,
                "{}",
                value
                    .iter()
                    .map(|(k, v)| format!("{}: {}", k, v.text()))
                    .collect::<Vec<String>>()
                    .join("\n")
            ),
            MQValue::Markdown { value, .. } => write!(f, "{}", value),
        }
    }
}

impl PartialEq for MQValue {
    fn eq(&self, other: &Self) -> bool {
        match (self, other) {
            (MQValue::Array { value: a }, MQValue::Array { value: b }) => a == b,
            (
                MQValue::Markdown {
                    value: a,
                    markdown_type: at,
                },
                MQValue::Markdown {
                    value: b,
                    markdown_type: bt,
                },
            ) => a == b && at == bt,
            _ => false,
        }
    }
}

#[pyclass(eq, eq_int, from_py_object)]
#[derive(Debug, Clone, Copy, PartialEq)]
pub enum MarkdownType {
    Blockquote,
    Break,
    Definition,
    Delete,
    Heading,
    Emphasis,
    Footnote,
    FootnoteRef,
    Html,
    Yaml,
    Toml,
    Image,
    ImageRef,
    CodeInline,
    MathInline,
    Link,
    LinkRef,
    Math,
    List,
    TableHeader,
    TableRow,
    TableCell,
    Code,
    Strong,
    HorizontalRule,
    MdxFlowExpression,
    MdxJsxFlowElement,
    MdxJsxTextElement,
    MdxTextExpression,
    MdxJsEsm,
    Text,
    Empty,
}

impl From<mq_lang::RuntimeValue> for MQValue {
    fn from(value: mq_lang::RuntimeValue) -> Self {
        match value {
            mq_lang::RuntimeValue::Array(arr) => MQValue::Array {
                value: arr.into_iter().map(|v| v.into()).collect(),
            },
            mq_lang::RuntimeValue::Dict(map) => MQValue::Dict {
                value: map.into_iter().map(|(k, v)| (k.as_str(), v.into())).collect(),
            },
            mq_lang::RuntimeValue::Markdown(node, _) => MQValue::Markdown {
                value: node.to_string(),
                markdown_type: node.into(),
            },
            mq_lang::RuntimeValue::String(s) => MQValue::Markdown {
                value: s,
                markdown_type: MarkdownType::Text,
            },
            mq_lang::RuntimeValue::Symbol(i) => MQValue::Markdown {
                value: i.as_str(),
                markdown_type: MarkdownType::Text,
            },
            mq_lang::RuntimeValue::Number(n) => MQValue::Markdown {
                value: n.to_string(),
                markdown_type: MarkdownType::Text,
            },
            mq_lang::RuntimeValue::Boolean(b) => MQValue::Markdown {
                value: b.to_string(),
                markdown_type: MarkdownType::Text,
            },
            mq_lang::RuntimeValue::Function(..)
            | mq_lang::RuntimeValue::NativeFunction(..)
            | mq_lang::RuntimeValue::Module(..)
            | mq_lang::RuntimeValue::Ast(..) => MQValue::Markdown {
                value: "".to_string(),
                markdown_type: MarkdownType::Empty,
            },
            mq_lang::RuntimeValue::None => MQValue::Markdown {
                value: "".to_string(),
                markdown_type: MarkdownType::Empty,
            },
        }
    }
}

impl From<mq_markdown::Node> for MarkdownType {
    fn from(node: mq_markdown::Node) -> Self {
        match node {
            mq_markdown::Node::Blockquote(_) => MarkdownType::Blockquote,
            mq_markdown::Node::Break(_) => MarkdownType::Break,
            mq_markdown::Node::Definition(_) => MarkdownType::Definition,
            mq_markdown::Node::Delete(_) => MarkdownType::Delete,
            mq_markdown::Node::Heading(_) => MarkdownType::Heading,
            mq_markdown::Node::Emphasis(_) => MarkdownType::Emphasis,
            mq_markdown::Node::Footnote(_) => MarkdownType::Footnote,
            mq_markdown::Node::FootnoteRef(_) => MarkdownType::FootnoteRef,
            mq_markdown::Node::Html(_) => MarkdownType::Html,
            mq_markdown::Node::Yaml(_) => MarkdownType::Yaml,
            mq_markdown::Node::Toml(_) => MarkdownType::Toml,
            mq_markdown::Node::Image(_) => MarkdownType::Image,
            mq_markdown::Node::ImageRef(_) => MarkdownType::ImageRef,
            mq_markdown::Node::CodeInline(_) => MarkdownType::CodeInline,
            mq_markdown::Node::MathInline(_) => MarkdownType::MathInline,
            mq_markdown::Node::Link(_) => MarkdownType::Link,
            mq_markdown::Node::LinkRef(_) => MarkdownType::LinkRef,
            mq_markdown::Node::Math(_) => MarkdownType::Math,
            mq_markdown::Node::List(_) => MarkdownType::List,
            mq_markdown::Node::TableAlign(_) => MarkdownType::TableHeader,
            mq_markdown::Node::TableRow(_) => MarkdownType::TableRow,
            mq_markdown::Node::TableCell(_) => MarkdownType::TableCell,
            mq_markdown::Node::Code(_) => MarkdownType::Code,
            mq_markdown::Node::Strong(_) => MarkdownType::Strong,
            mq_markdown::Node::HorizontalRule(_) => MarkdownType::HorizontalRule,
            mq_markdown::Node::MdxFlowExpression(_) => MarkdownType::MdxFlowExpression,
            mq_markdown::Node::MdxJsxFlowElement(_) => MarkdownType::MdxJsxFlowElement,
            mq_markdown::Node::MdxJsxTextElement(_) => MarkdownType::MdxJsxTextElement,
            mq_markdown::Node::MdxTextExpression(_) => MarkdownType::MdxTextExpression,
            mq_markdown::Node::MdxJsEsm(..) => MarkdownType::MdxJsEsm,
            mq_markdown::Node::Text(_) => MarkdownType::Text,
            _ => MarkdownType::Empty,
        }
    }
}

use pyo3::prelude::*;

#[pymethods]
impl MQValue {
    #[getter]
    pub fn text(&self) -> String {
        self.to_string()
    }

    #[getter]
    pub fn values(&self) -> Vec<Self> {
        match self {
            MQValue::Array { value } => value.clone(),
            a => vec![a.clone()],
        }
    }

    #[getter]
    pub fn markdown_type(&self) -> Option<MarkdownType> {
        match self {
            MQValue::Markdown { markdown_type, .. } => Some(*markdown_type),
            _ => None,
        }
    }

    pub fn is_array(&self) -> bool {
        matches!(self, MQValue::Array { .. })
    }

    pub fn is_markdown(&self) -> bool {
        matches!(self, MQValue::Markdown { .. })
    }

    pub fn __getitem__(&self, idx: usize) -> PyResult<MQValue> {
        let array = self.values();

        if idx < array.len() {
            Ok(array[idx].clone())
        } else {
            Err(pyo3::exceptions::PyIndexError::new_err(format!(
                "Index {} out of range for MQResult with length {}",
                idx,
                array.len()
            )))
        }
    }

    pub fn __str__(&self) -> String {
        self.text()
    }

    pub fn __repr__(&self) -> String {
        match self {
            MQValue::Array { value: arr } => format!(
                "MQValue::ARRAY([{}])",
                arr.iter().map(|v| v.__repr__()).collect::<Vec<_>>().join(", ")
            ),
            MQValue::Dict { value: map } => {
                format!(
                    "MQValue::MAP({})",
                    map.iter()
                        .map(|(k, v)| format!("\"{}\": {}", k, v.__repr__()))
                        .collect::<Vec<_>>()
                        .join(", ")
                )
            }
            MQValue::Markdown { value, markdown_type } => {
                format!("MQValue::Markdown(\"{}\", {:?})", value, markdown_type)
            }
        }
    }

    pub fn __bool__(&self) -> bool {
        match self {
            MQValue::Array { value } => !value.is_empty(),
            MQValue::Dict { value } => !value.is_empty(),
            MQValue::Markdown { value, .. } => !value.is_empty(),
        }
    }

    pub fn __len__(&self) -> usize {
        match self {
            MQValue::Array { value } => value.len(),
            MQValue::Dict { value } => value.len(),
            MQValue::Markdown { value, .. } => value.len(),
        }
    }

    pub fn __eq__(&self, other: &Self) -> bool {
        self == other
    }

    pub fn __ne__(&self, other: &Self) -> bool {
        !self.__eq__(other)
    }

    pub fn __lt__(&self, other: &Self) -> bool {
        match (self, other) {
            (MQValue::Array { value: a }, MQValue::Array { value: b }) => {
                if a.len() != b.len() {
                    a.len() < b.len()
                } else {
                    for (a_item, b_item) in a.iter().zip(b.iter()) {
                        if a_item != b_item {
                            return a_item.__lt__(b_item);
                        }
                    }
                    false
                }
            }
            (MQValue::Markdown { value: a, .. }, MQValue::Markdown { value: b, .. }) => a < b,
            _ => false,
        }
    }

    pub fn __gt__(&self, other: &Self) -> bool {
        match (self, other) {
            (MQValue::Array { value: a }, MQValue::Array { value: b }) => {
                if a.len() != b.len() {
                    a.len() > b.len()
                } else {
                    for (a_item, b_item) in a.iter().zip(b.iter()) {
                        if a_item != b_item {
                            return a_item.__gt__(b_item);
                        }
                    }
                    false
                }
            }
            (MQValue::Markdown { value: a, .. }, MQValue::Markdown { value: b, .. }) => a > b,
            _ => false,
        }
    }
}
```

## File: `src/mq/__init__.py`
```python
from .mq import *

__all__ = mq.__all__
```

## File: `src/mq/mq.pyi`
```
from typing import List, Optional
from enum import Enum

class InputFormat(Enum):
    """The format of the input document."""

    MARKDOWN: 1
    MDX: 2
    TEXT: 3
    HTML: 4
    RAW: 5
    NULL: 6

class ListStyle(Enum):
    """Style to use for markdown lists."""

    DASH: 1
    PLUS: 2
    STAR: 3

class TitleSurroundStyle(Enum):
    """Style for surrounding link titles."""

    DOUBLE: 1
    SINGLE: 2
    PAREN: 3

class UrlSurroundStyle(Enum):
    """Style for surrounding URLs."""

    ANGLE: 1
    NONE: 2

class Options:
    """Configuration options for mq processing."""

    def __init__(self) -> None: ...
    @property
    def input_format(self) -> InputFormat: ...
    @property
    def list_style(self) -> ListStyle: ...
    @property
    def link_title_style(self) -> TitleSurroundStyle: ...
    @property
    def link_url_style(self) -> UrlSurroundStyle: ...

class MarkdownType(Enum):
    """Types of Markdown elements."""

    Blockquote: int = 1
    Break: int = 2
    Definition: int = 3
    Delete: int = 4
    Heading: int = 5
    Emphasis: int = 6
    Footnote: int = 7
    FootnoteRef: int = 8
    Html: int = 9
    Yaml: int = 10
    Toml: int = 11
    Image: int = 12
    ImageRef: int = 13
    CodeInline: int = 14
    MathInline: int = 15
    Link: int = 16
    LinkRef: int = 17
    Math: int = 18
    List: int = 19
    TableHeader: int = 20
    TableRow: int = 21
    TableCell: int = 22
    Code: int = 23
    Strong: int = 24
    HorizontalRule: int = 25
    MdxFlowExpression: int = 26
    MdxJsxFlowElement: int = 27
    MdxJsxTextElement: int = 28
    MdxTextExpression: int = 29
    MdxJsEsm: int = 30
    Text: int = 31
    Empty: int = 32

class MQValue:
    """
    Represents a value in the mq query result.
    """

    @property
    def text(self) -> str:
        """
        Get the text representation of the value.

        Returns:
            str: The text representation of the value
        """

    @property
    def array(self) -> List["MQValue"]:
        """
        Get the value as an array.

        Returns:
            List[MQValue]: The value as an array of MQValue objects
        """

    @property
    def markdown_type(self) -> Optional[MarkdownType]:
        """
        Get the markdown type of the document.

        Returns:
            Optional[MarkdownType]: The markdown type of the document, or None if not applicable.
        """

    def is_array(self) -> bool:
        """
        Check if this value is an array.

        Returns:
            True if this value is an array, False otherwise
        """

    def is_markdown(self) -> bool:
        """
        Check if this value is a markdown node.

        Returns:
            True if this value is a markdown node, False otherwise
        """

    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __eq__(self, other: "MQValue") -> bool: ...
    def __ne__(self, other: "MQValue") -> bool: ...
    def __lt__(self, other: "MQValue") -> bool: ...
    def __gt__(self, other: "MQValue") -> bool: ...

class MQResult:
    """
    Result of a query execution.
    Attributes:
        values: A list of MQValue objects returned by the query
    """

    values: List[MQValue]

    @property
    def text(self) -> str:
        """
        Get the text representation of all values.

        Returns:
            Text representation of all values joined by newlines
        """

    @property
    def values(self) -> List[str]:
        """
        Get a list of non-empty text values as strings.

        This returns the text representations of all non-empty values
        in the result set.

        Returns:
            List of non-empty text values as strings
        """

    def __contains__(self, item: str) -> bool: ...
    def __getitem__(self, idx: int) -> MQValue: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: "MQResult") -> bool: ...
    def __ne__(self, other: "MQResult") -> bool: ...
    def __lt__(self, other: "MQResult") -> bool: ...
    def __gt__(self, other: "MQResult") -> bool: ...

# Function to run mq queries
def run(code: str, content: str, options: Optional[Options] = None) -> MQResult:
    """
    Run an mq query against markdown content with the specified options.

    This is the main entry point for processing markdown with mq from Python.
    It takes a query written in the mq query language, applies it to the provided
    markdown content, and returns the results.

    Args:
        code: The mq query string to run against the content
        content: The markdown content to process (or text depending on options)
        options: Configuration options for processing. If None, default options are used.

    Returns:
        MQResult object containing the query results

    Raises:
        RuntimeError: If there's an error parsing the markdown or evaluating the query

    Example:
        ```python
        import mq

        # Create query to extract all headings
        query = ".h1"

        # Markdown content
        content = "# Title\\n\\nSome content\\n\\n## Subtitle\\n\\nMore content"

        # Run the query
        result = mq.run(query, content)

        # Print the extracted headings
        print(result.text)
        # Output: "# Title\n## Subtitle"
        ```
    """
```

## File: `tests/test_mq.py`
```python
import pytest
import mq


@pytest.mark.parametrize(
    "code, content, expected",
    [
        (".h1", "# Hello World\n\n## Heading2\n\nText", ["# Hello World"]),
        (".h2", "# Hello World\n\n## Heading2\n\nText", ["## Heading2"]),
        (
            ".h2",
            "# Main Title\n\n## Heading2A\n\nText\n\n## Heading2B\n\nMore text",
            ["## Heading2A", "## Heading2B"],
        ),
        (
            '.h2 | select(contains("Feature"))',
            "# Product\n\n## Features\n\nText\n\n## Installation\n\nMore text",
            ["## Features"],
        ),
        (
            ".[]",
            "# List\n\n- Item 1\n- Item 2\n- Item 3",
            ["- Item 1", "- Item 2", "- Item 3"],
        ),
        (
            ".code",
            "# Code\n\n```python\nprint('Hello')\n```",
            ["```python\nprint('Hello')\n```"],
        ),
    ],
)
def test_mq_queries(code, content, expected):
    result = mq.run(code, content, None)
    assert result.values == expected


@pytest.mark.parametrize(
    "input_format, code, content, expected",
    [
        (
            mq.InputFormat.TEXT,
            'select(contains("2"))',
            "Line 1\nLine 2\nLine 3",
            ["Line 2"],
        ),
        (
            mq.InputFormat.MDX,
            "select(is_mdx())",
            "# MDX Content\n\n<Component />",
            ["<Component />"],
        ),
        (
            mq.InputFormat.HTML,
            'select(contains("Hello"))',
            "<h1>Hello</h1><p>World</p>",
            ["# Hello"],
        ),
    ],
)
def test_input_formats(input_format, code, content, expected):
    options = mq.Options()
    options.input_format = input_format

    result = mq.run(code, content, options)
    assert result.values == expected


def test_invalid_query():
    with pytest.raises(Exception) as exc_info:
        mq.run(".invalid_selector!!!", "# Heading", None)

    assert "Error evaluating query" in str(exc_info.value)


def test_html_to_markdown():
    html_content = "<h1>Hello World</h1><p>This is a <strong>test</strong>.</p>"
    expected_markdown = "# Hello World\n\nThis is a **test**."
    markdown = mq.html_to_markdown(html_content)
    assert markdown.strip() == expected_markdown
```

