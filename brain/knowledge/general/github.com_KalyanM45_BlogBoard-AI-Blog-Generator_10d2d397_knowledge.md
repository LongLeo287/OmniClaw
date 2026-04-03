---
id: github.com-kalyanm45-blogboard-ai-blog-generator-1
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:17.307693
---

# KNOWLEDGE EXTRACT: github.com_KalyanM45_BlogBoard-AI-Blog-Generator_10d2d397
> **Extracted on:** 2026-04-01 14:15:37
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007523809/github.com_KalyanM45_BlogBoard-AI-Blog-Generator_10d2d397

---

## File: `.env.example`
```
GROQ_API_KEY=""
```

## File: `.gitignore`
```
Docs
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
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
*.py.cover
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
#poetry.toml
# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
#pdm.lock
#pdm.toml
.pdm-python
.pdm-build/
# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
#pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi
# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/
# Celery stuff
celerybeat-schedule
celerybeat.pid
# SageMath parsed files
*.sage.py
# Environments
.env
.envrc
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
# Abstra
# Abstra is an AI-powered process automation framework.
# Ignore directories containing user credentials, local state, and settings.
# Learn more at https://abstra.io/docs
.abstra/
# Visual Studio Code
#  Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore
#  that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#  and can be added to the global gitignore or merged into this file. However, if you prefer,
#  you could uncomment the following to ignore the entire vscode folder
# .vscode/
# Ruff stuff:
.ruff_cache/
# PyPI configuration file
.pypirc
# Cursor
#  Cursor is an AI-powered code editor. `.cursorignore` specifies files/directories to
#  exclude from AI features like autocomplete and code analysis. Recommended for sensitive data
#  refer to https://docs.cursor.com/context/ignore-files
.cursorignore
.cursorindexingignore
# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/
```

## File: `.python-version`
```
3.13
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2026 Hema Kalyan Murapaka

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `README.md`
```markdown
# <a href="https://kalyanm45.github.io/BlogBoard-AI-Blog-Generator/">BlogBoard — Autonomous AI Article Generator</a>

<p align="center"> <img src="https://img.shields.io/github/license/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND" alt="License" /> <img src="https://img.shields.io/github/stars/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND" alt="Stars" /> <img src="https://img.shields.io/github/forks/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND" alt="Forks" /> <img src="https://img.shields.io/github/issues/KalyanM45/BlogBoard-AI-Blog-Generator?style=ROUND"alt="Issues" />
</p>

## About The Project

BlogBoard is an end-to-end, fully automated blogging platform. It autonomously schedules, writes, formats, and publishes deep-dive technical articles on Machine Learning and Artificial Intelligence directly to a fast, static frontend website.

Powered by **LangGraph** for stateful workflow execution and **Groq** for blazing-fast LLM inference, it ensures that high-quality, zero-fluff, production-grade articles are generated and deployed automatically via **GitHub Actions**.

## Library Requirements

 - Python 3.12+
 - langgraph>=0.2.20
 - groq>=0.11.0
 - python-dotenv>=1.0.1
 - uv (for dependency management)

## Getting Started

This will help you understand how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

## Installation Steps

### Installation from GitHub

Follow these steps to install and set up the project directly from the GitHub repository:

1. **Clone the Repository**
   - Open your terminal or command prompt.
   - Navigate to the directory where you want to install the project.
   - Run the following command to clone the GitHub repository:
     ```bash
     git clone https://github.com/KalyanM45/BlogBoard-AI-Blog-Generator.git
     ```

2. **Create a Virtual Environment** (Recommended)
   - It's a good practice to create a virtual environment to manage project dependencies. Run the following command:
     ```bash
     uv venv
     ```

3. **Activate the Virtual Environment**
   - Activate the virtual environment based on your operating system:
       ```bash
       # On Linux/Mac:
       source .venv/bin/activate
       # On Windows:
       .venv\Scripts\activate
       ```

4. **Install Dependencies**
   - Navigate to the project directory:
     ```bash
     cd BlogBoard-AI-Blog-Generator
     ```
   - Run the following command to install project dependencies:
     ```bash
     uv pip install -r backend/requirements.txt
     ```

5. **Run the Project**
   - Start the backend pipeline by running the appropriate command:
     ```bash
     python backend/run.py
     ```

6. **Access the Project**
   - Serve the frontend locally using Python's built-in HTTP server:
     ```bash
     python -m http.server 8000 --directory frontend
     ```
   - Open a web browser and navigate to `http://localhost:8000`.


## API Key Setup

To use this project, you need an API key from Groq to power the Large Language Model inference. Follow these steps to obtain and set up your API key:

1. **Get API Key:**
   - Visit the Groq Console at [console.groq.com](https://console.groq.com/).
   - Follow the instructions to create an account and obtain your API key.

2. **Set Up API Key:**
   - Create a file named `.env` in the project root.
   - Add your API key to the `.env` file:
     ```dotenv
     GROQ_API_KEY=your_api_key_here
     ```

   **Note:** Keep your API key confidential. Do not share it publicly or expose it in your code.<br>

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

• **Report bugs**: If you encounter any bugs, please let us know. Open up an issue and let us know the problem.

• **Contribute code**: If you are a developer and want to contribute, follow the instructions below to get started!

1. Fork the Project
2. Create your Feature Branch
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request

• **Suggestions**: If you don't want to code but have some awesome ideas, open up an issue explaining some updates or improvements you would like to see!

#### Don't forget to give the project a star! Thanks again!

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) - see the [LICENSE](LICENSE) file for details.<br>

## Acknowledgements

We'd like to extend our gratitude to all individuals and organizations who have played a role in the development and success of this project. Your support, whether through contributions, inspiration, or encouragement, has been invaluable. Thank you for being a part of our journey.
```

## File: `pyproject.toml`
```
[project]
name = "blogboard"
version = "0.1.0"
description = "Add your description here"
readme = "README.md"
requires-python = ">=3.13"
dependencies = [
    "groq>=1.0.0",
    "langchain-core>=1.2.16",
    "langgraph>=1.0.10",
    "python-dotenv>=1.2.1",
]
```

## File: `uv.lock`
```
version = 1
revision = 3
requires-python = ">=3.13"

[[package]]
name = "annotated-types"
version = "0.7.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/ee/67/531ea369ba64dcff5ec9c3402f9f51bf748cec26dde048a2f973a4eea7f5/annotated_types-0.7.0.tar.gz", hash = "sha256:aff07c09a53a08bc8cfccb9c85b05f1aa9a2a6f23728d790723543408344ce89", size = 16081, upload-time = "2024-05-20T21:33:25.928Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/78/b6/6307fbef88d9b5ee7421e68d78a9f162e0da4900bc5f5793f6d3d0e34fb8/annotated_types-0.7.0-py3-none-any.whl", hash = "sha256:1f02e8b43a8fbbc3f3e0d4f0f4bfc8131bcb4eebe8849b8e5c773f3a1c582a53", size = 13643, upload-time = "2024-05-20T21:33:24.1Z" },
]

[[package]]
name = "anyio"
version = "4.12.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/96/f0/5eb65b2bb0d09ac6776f2eb54adee6abe8228ea05b20a5ad0e4945de8aac/anyio-4.12.1.tar.gz", hash = "sha256:41cfcc3a4c85d3f05c932da7c26d0201ac36f72abd4435ba90d0464a3ffed703", size = 228685, upload-time = "2026-01-06T11:45:21.246Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/38/0e/27be9fdef66e72d64c0cdc3cc2823101b80585f8119b5c112c2e8f5f7dab/anyio-4.12.1-py3-none-any.whl", hash = "sha256:d405828884fc140aa80a3c667b8beed277f1dfedec42ba031bd6ac3db606ab6c", size = 113592, upload-time = "2026-01-06T11:45:19.497Z" },
]

[[package]]
name = "blogboard"
version = "0.1.0"
source = { virtual = "." }
dependencies = [
    { name = "groq" },
    { name = "langchain-core" },
    { name = "langgraph" },
    { name = "python-dotenv" },
]

[package.metadata]
requires-dist = [
    { name = "groq", specifier = ">=1.0.0" },
    { name = "langchain-core", specifier = ">=1.2.16" },
    { name = "langgraph", specifier = ">=1.0.10" },
    { name = "python-dotenv", specifier = ">=1.2.1" },
]

[[package]]
name = "certifi"
version = "2026.2.25"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/af/2d/7bf41579a8986e348fa033a31cdd0e4121114f6bce2457e8876010b092dd/certifi-2026.2.25.tar.gz", hash = "sha256:e887ab5cee78ea814d3472169153c2d12cd43b14bd03329a39a9c6e2e80bfba7", size = 155029, upload-time = "2026-02-25T02:54:17.342Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/9a/3c/c17fb3ca2d9c3acff52e30b309f538586f9f5b9c9cf454f3845fc9af4881/certifi-2026.2.25-py3-none-any.whl", hash = "sha256:027692e4402ad994f1c42e52a4997a9763c646b73e4096e4d5d6db8af1d6f0fa", size = 153684, upload-time = "2026-02-25T02:54:15.766Z" },
]

[[package]]
name = "charset-normalizer"
version = "3.4.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/13/69/33ddede1939fdd074bce5434295f38fae7136463422fe4fd3e0e89b98062/charset_normalizer-3.4.4.tar.gz", hash = "sha256:94537985111c35f28720e43603b8e7b43a6ecfb2ce1d3058bbe955b73404e21a", size = 129418, upload-time = "2025-10-14T04:42:32.879Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/97/45/4b3a1239bbacd321068ea6e7ac28875b03ab8bc0aa0966452db17cd36714/charset_normalizer-3.4.4-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:e1f185f86a6f3403aa2420e815904c67b2f9ebc443f045edd0de921108345794", size = 208091, upload-time = "2025-10-14T04:41:13.346Z" },
    { url = "https://files.pythonhosted.org/packages/7d/62/73a6d7450829655a35bb88a88fca7d736f9882a27eacdca2c6d505b57e2e/charset_normalizer-3.4.4-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6b39f987ae8ccdf0d2642338faf2abb1862340facc796048b604ef14919e55ed", size = 147936, upload-time = "2025-10-14T04:41:14.461Z" },
    { url = "https://files.pythonhosted.org/packages/89/c5/adb8c8b3d6625bef6d88b251bbb0d95f8205831b987631ab0c8bb5d937c2/charset_normalizer-3.4.4-cp313-cp313-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:3162d5d8ce1bb98dd51af660f2121c55d0fa541b46dff7bb9b9f86ea1d87de72", size = 144180, upload-time = "2025-10-14T04:41:15.588Z" },
    { url = "https://files.pythonhosted.org/packages/91/ed/9706e4070682d1cc219050b6048bfd293ccf67b3d4f5a4f39207453d4b99/charset_normalizer-3.4.4-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:81d5eb2a312700f4ecaa977a8235b634ce853200e828fbadf3a9c50bab278328", size = 161346, upload-time = "2025-10-14T04:41:16.738Z" },
    { url = "https://files.pythonhosted.org/packages/d5/0d/031f0d95e4972901a2f6f09ef055751805ff541511dc1252ba3ca1f80cf5/charset_normalizer-3.4.4-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:5bd2293095d766545ec1a8f612559f6b40abc0eb18bb2f5d1171872d34036ede", size = 158874, upload-time = "2025-10-14T04:41:17.923Z" },
    { url = "https://files.pythonhosted.org/packages/f5/83/6ab5883f57c9c801ce5e5677242328aa45592be8a00644310a008d04f922/charset_normalizer-3.4.4-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:a8a8b89589086a25749f471e6a900d3f662d1d3b6e2e59dcecf787b1cc3a1894", size = 153076, upload-time = "2025-10-14T04:41:19.106Z" },
    { url = "https://files.pythonhosted.org/packages/75/1e/5ff781ddf5260e387d6419959ee89ef13878229732732ee73cdae01800f2/charset_normalizer-3.4.4-cp313-cp313-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:bc7637e2f80d8530ee4a78e878bce464f70087ce73cf7c1caf142416923b98f1", size = 150601, upload-time = "2025-10-14T04:41:20.245Z" },
    { url = "https://files.pythonhosted.org/packages/d7/57/71be810965493d3510a6ca79b90c19e48696fb1ff964da319334b12677f0/charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f8bf04158c6b607d747e93949aa60618b61312fe647a6369f88ce2ff16043490", size = 150376, upload-time = "2025-10-14T04:41:21.398Z" },
    { url = "https://files.pythonhosted.org/packages/e5/d5/c3d057a78c181d007014feb7e9f2e65905a6c4ef182c0ddf0de2924edd65/charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:554af85e960429cf30784dd47447d5125aaa3b99a6f0683589dbd27e2f45da44", size = 144825, upload-time = "2025-10-14T04:41:22.583Z" },
    { url = "https://files.pythonhosted.org/packages/e6/8c/d0406294828d4976f275ffbe66f00266c4b3136b7506941d87c00cab5272/charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:74018750915ee7ad843a774364e13a3db91682f26142baddf775342c3f5b1133", size = 162583, upload-time = "2025-10-14T04:41:23.754Z" },
    { url = "https://files.pythonhosted.org/packages/d7/24/e2aa1f18c8f15c4c0e932d9287b8609dd30ad56dbe41d926bd846e22fb8d/charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_riscv64.whl", hash = "sha256:c0463276121fdee9c49b98908b3a89c39be45d86d1dbaa22957e38f6321d4ce3", size = 150366, upload-time = "2025-10-14T04:41:25.27Z" },
    { url = "https://files.pythonhosted.org/packages/e4/5b/1e6160c7739aad1e2df054300cc618b06bf784a7a164b0f238360721ab86/charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:362d61fd13843997c1c446760ef36f240cf81d3ebf74ac62652aebaf7838561e", size = 160300, upload-time = "2025-10-14T04:41:26.725Z" },
    { url = "https://files.pythonhosted.org/packages/7a/10/f882167cd207fbdd743e55534d5d9620e095089d176d55cb22d5322f2afd/charset_normalizer-3.4.4-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:9a26f18905b8dd5d685d6d07b0cdf98a79f3c7a918906af7cc143ea2e164c8bc", size = 154465, upload-time = "2025-10-14T04:41:28.322Z" },
    { url = "https://files.pythonhosted.org/packages/89/66/c7a9e1b7429be72123441bfdbaf2bc13faab3f90b933f664db506dea5915/charset_normalizer-3.4.4-cp313-cp313-win32.whl", hash = "sha256:9b35f4c90079ff2e2edc5b26c0c77925e5d2d255c42c74fdb70fb49b172726ac", size = 99404, upload-time = "2025-10-14T04:41:29.95Z" },
    { url = "https://files.pythonhosted.org/packages/c4/26/b9924fa27db384bdcd97ab83b4f0a8058d96ad9626ead570674d5e737d90/charset_normalizer-3.4.4-cp313-cp313-win_amd64.whl", hash = "sha256:b435cba5f4f750aa6c0a0d92c541fb79f69a387c91e61f1795227e4ed9cece14", size = 107092, upload-time = "2025-10-14T04:41:31.188Z" },
    { url = "https://files.pythonhosted.org/packages/af/8f/3ed4bfa0c0c72a7ca17f0380cd9e4dd842b09f664e780c13cff1dcf2ef1b/charset_normalizer-3.4.4-cp313-cp313-win_arm64.whl", hash = "sha256:542d2cee80be6f80247095cc36c418f7bddd14f4a6de45af91dfad36d817bba2", size = 100408, upload-time = "2025-10-14T04:41:32.624Z" },
    { url = "https://files.pythonhosted.org/packages/2a/35/7051599bd493e62411d6ede36fd5af83a38f37c4767b92884df7301db25d/charset_normalizer-3.4.4-cp314-cp314-macosx_10_13_universal2.whl", hash = "sha256:da3326d9e65ef63a817ecbcc0df6e94463713b754fe293eaa03da99befb9a5bd", size = 207746, upload-time = "2025-10-14T04:41:33.773Z" },
    { url = "https://files.pythonhosted.org/packages/10/9a/97c8d48ef10d6cd4fcead2415523221624bf58bcf68a802721a6bc807c8f/charset_normalizer-3.4.4-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:8af65f14dc14a79b924524b1e7fffe304517b2bff5a58bf64f30b98bbc5079eb", size = 147889, upload-time = "2025-10-14T04:41:34.897Z" },
    { url = "https://files.pythonhosted.org/packages/10/bf/979224a919a1b606c82bd2c5fa49b5c6d5727aa47b4312bb27b1734f53cd/charset_normalizer-3.4.4-cp314-cp314-manylinux2014_armv7l.manylinux_2_17_armv7l.manylinux_2_31_armv7l.whl", hash = "sha256:74664978bb272435107de04e36db5a9735e78232b85b77d45cfb38f758efd33e", size = 143641, upload-time = "2025-10-14T04:41:36.116Z" },
    { url = "https://files.pythonhosted.org/packages/ba/33/0ad65587441fc730dc7bd90e9716b30b4702dc7b617e6ba4997dc8651495/charset_normalizer-3.4.4-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:752944c7ffbfdd10c074dc58ec2d5a8a4cd9493b314d367c14d24c17684ddd14", size = 160779, upload-time = "2025-10-14T04:41:37.229Z" },
    { url = "https://files.pythonhosted.org/packages/67/ed/331d6b249259ee71ddea93f6f2f0a56cfebd46938bde6fcc6f7b9a3d0e09/charset_normalizer-3.4.4-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:d1f13550535ad8cff21b8d757a3257963e951d96e20ec82ab44bc64aeb62a191", size = 159035, upload-time = "2025-10-14T04:41:38.368Z" },
    { url = "https://files.pythonhosted.org/packages/67/ff/f6b948ca32e4f2a4576aa129d8bed61f2e0543bf9f5f2b7fc3758ed005c9/charset_normalizer-3.4.4-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:ecaae4149d99b1c9e7b88bb03e3221956f68fd6d50be2ef061b2381b61d20838", size = 152542, upload-time = "2025-10-14T04:41:39.862Z" },
    { url = "https://files.pythonhosted.org/packages/16/85/276033dcbcc369eb176594de22728541a925b2632f9716428c851b149e83/charset_normalizer-3.4.4-cp314-cp314-manylinux_2_31_riscv64.manylinux_2_39_riscv64.whl", hash = "sha256:cb6254dc36b47a990e59e1068afacdcd02958bdcce30bb50cc1700a8b9d624a6", size = 149524, upload-time = "2025-10-14T04:41:41.319Z" },
    { url = "https://files.pythonhosted.org/packages/9e/f2/6a2a1f722b6aba37050e626530a46a68f74e63683947a8acff92569f979a/charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:c8ae8a0f02f57a6e61203a31428fa1d677cbe50c93622b4149d5c0f319c1d19e", size = 150395, upload-time = "2025-10-14T04:41:42.539Z" },
    { url = "https://files.pythonhosted.org/packages/60/bb/2186cb2f2bbaea6338cad15ce23a67f9b0672929744381e28b0592676824/charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:47cc91b2f4dd2833fddaedd2893006b0106129d4b94fdb6af1f4ce5a9965577c", size = 143680, upload-time = "2025-10-14T04:41:43.661Z" },
    { url = "https://files.pythonhosted.org/packages/7d/a5/bf6f13b772fbb2a90360eb620d52ed8f796f3c5caee8398c3b2eb7b1c60d/charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:82004af6c302b5d3ab2cfc4cc5f29db16123b1a8417f2e25f9066f91d4411090", size = 162045, upload-time = "2025-10-14T04:41:44.821Z" },
    { url = "https://files.pythonhosted.org/packages/df/c5/d1be898bf0dc3ef9030c3825e5d3b83f2c528d207d246cbabe245966808d/charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_riscv64.whl", hash = "sha256:2b7d8f6c26245217bd2ad053761201e9f9680f8ce52f0fcd8d0755aeae5b2152", size = 149687, upload-time = "2025-10-14T04:41:46.442Z" },
    { url = "https://files.pythonhosted.org/packages/a5/42/90c1f7b9341eef50c8a1cb3f098ac43b0508413f33affd762855f67a410e/charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:799a7a5e4fb2d5898c60b640fd4981d6a25f1c11790935a44ce38c54e985f828", size = 160014, upload-time = "2025-10-14T04:41:47.631Z" },
    { url = "https://files.pythonhosted.org/packages/76/be/4d3ee471e8145d12795ab655ece37baed0929462a86e72372fd25859047c/charset_normalizer-3.4.4-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:99ae2cffebb06e6c22bdc25801d7b30f503cc87dbd283479e7b606f70aff57ec", size = 154044, upload-time = "2025-10-14T04:41:48.81Z" },
    { url = "https://files.pythonhosted.org/packages/b0/6f/8f7af07237c34a1defe7defc565a9bc1807762f672c0fde711a4b22bf9c0/charset_normalizer-3.4.4-cp314-cp314-win32.whl", hash = "sha256:f9d332f8c2a2fcbffe1378594431458ddbef721c1769d78e2cbc06280d8155f9", size = 99940, upload-time = "2025-10-14T04:41:49.946Z" },
    { url = "https://files.pythonhosted.org/packages/4b/51/8ade005e5ca5b0d80fb4aff72a3775b325bdc3d27408c8113811a7cbe640/charset_normalizer-3.4.4-cp314-cp314-win_amd64.whl", hash = "sha256:8a6562c3700cce886c5be75ade4a5db4214fda19fede41d9792d100288d8f94c", size = 107104, upload-time = "2025-10-14T04:41:51.051Z" },
    { url = "https://files.pythonhosted.org/packages/da/5f/6b8f83a55bb8278772c5ae54a577f3099025f9ade59d0136ac24a0df4bde/charset_normalizer-3.4.4-cp314-cp314-win_arm64.whl", hash = "sha256:de00632ca48df9daf77a2c65a484531649261ec9f25489917f09e455cb09ddb2", size = 100743, upload-time = "2025-10-14T04:41:52.122Z" },
    { url = "https://files.pythonhosted.org/packages/0a/4c/925909008ed5a988ccbb72dcc897407e5d6d3bd72410d69e051fc0c14647/charset_normalizer-3.4.4-py3-none-any.whl", hash = "sha256:7a32c560861a02ff789ad905a2fe94e3f840803362c84fecf1851cb4cf3dc37f", size = 53402, upload-time = "2025-10-14T04:42:31.76Z" },
]

[[package]]
name = "distro"
version = "1.9.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fc/f8/98eea607f65de6527f8a2e8885fc8015d3e6f5775df186e443e0964a11c3/distro-1.9.0.tar.gz", hash = "sha256:2fa77c6fd8940f116ee1d6b94a2f90b13b5ea8d019b98bc8bafdcabcdd9bdbed", size = 60722, upload-time = "2023-12-24T09:54:32.31Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/12/b3/231ffd4ab1fc9d679809f356cebee130ac7daa00d6d6f3206dd4fd137e9e/distro-1.9.0-py3-none-any.whl", hash = "sha256:7bffd925d65168f85027d8da9af6bddab658135b840670a223589bc0c8ef02b2", size = 20277, upload-time = "2023-12-24T09:54:30.421Z" },
]

[[package]]
name = "groq"
version = "1.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "distro" },
    { name = "httpx" },
    { name = "pydantic" },
    { name = "sniffio" },
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3f/12/f4099a141677fcd2ed79dcc1fcec431e60c52e0e90c9c5d935f0ffaf8c0e/groq-1.0.0.tar.gz", hash = "sha256:66cb7bb729e6eb644daac7ce8efe945e99e4eb33657f733ee6f13059ef0c25a9", size = 146068, upload-time = "2025-12-17T23:34:23.115Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/4a/88/3175759d2ef30406ea721f4d837bfa1ba4339fde3b81ba8c5640a96ed231/groq-1.0.0-py3-none-any.whl", hash = "sha256:6e22bf92ffad988f01d2d4df7729add66b8fd5dbfb2154b5bbf3af245b72c731", size = 138292, upload-time = "2025-12-17T23:34:21.957Z" },
]

[[package]]
name = "h11"
version = "0.16.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/01/ee/02a2c011bdab74c6fb3c75474d40b3052059d95df7e73351460c8588d963/h11-0.16.0.tar.gz", hash = "sha256:4e35b956cf45792e4caa5885e69fba00bdbc6ffafbfa020300e549b208ee5ff1", size = 101250, upload-time = "2025-04-24T03:35:25.427Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/04/4b/29cac41a4d98d144bf5f6d33995617b185d14b22401f75ca86f384e87ff1/h11-0.16.0-py3-none-any.whl", hash = "sha256:63cf8bbe7522de3bf65932fda1d9c2772064ffb3dae62d55932da54b31cb6c86", size = 37515, upload-time = "2025-04-24T03:35:24.344Z" },
]

[[package]]
name = "httpcore"
version = "1.0.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "h11" },
]
sdist = { url = "https://files.pythonhosted.org/packages/06/94/82699a10bca87a5556c9c59b5963f2d039dbd239f25bc2a63907a05a14cb/httpcore-1.0.9.tar.gz", hash = "sha256:6e34463af53fd2ab5d807f399a9b45ea31c3dfa2276f15a2c3f00afff6e176e8", size = 85484, upload-time = "2025-04-24T22:06:22.219Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/7e/f5/f66802a942d491edb555dd61e3a9961140fd64c90bce1eafd741609d334d/httpcore-1.0.9-py3-none-any.whl", hash = "sha256:2d400746a40668fc9dec9810239072b40b4484b640a8c38fd654a024c7a1bf55", size = 78784, upload-time = "2025-04-24T22:06:20.566Z" },
]

[[package]]
name = "httpx"
version = "0.28.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "anyio" },
    { name = "certifi" },
    { name = "httpcore" },
    { name = "idna" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/df/48c586a5fe32a0f01324ee087459e112ebb7224f646c0b5023f5e79e9956/httpx-0.28.1.tar.gz", hash = "sha256:75e98c5f16b0f35b567856f597f06ff2270a374470a5c2392242528e3e3e42fc", size = 141406, upload-time = "2024-12-06T15:37:23.222Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2a/39/e50c7c3a983047577ee07d2a9e53faf5a69493943ec3f6a384bdc792deb2/httpx-0.28.1-py3-none-any.whl", hash = "sha256:d909fcccc110f8c7faf814ca82a9a4d816bc5a6dbfea25d6591d6985b8ba59ad", size = 73517, upload-time = "2024-12-06T15:37:21.509Z" },
]

[[package]]
name = "idna"
version = "3.11"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6f/6d/0703ccc57f3a7233505399edb88de3cbd678da106337b9fcde432b65ed60/idna-3.11.tar.gz", hash = "sha256:795dafcc9c04ed0c1fb032c2aa73654d8e8c5023a7df64a53f39190ada629902", size = 194582, upload-time = "2025-10-12T14:55:20.501Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/0e/61/66938bbb5fc52dbdf84594873d5b51fb1f7c7794e9c0f5bd885f30bc507b/idna-3.11-py3-none-any.whl", hash = "sha256:771a87f49d9defaf64091e6e6fe9c18d4833f140bd19464795bc32d966ca37ea", size = 71008, upload-time = "2025-10-12T14:55:18.883Z" },
]

[[package]]
name = "jsonpatch"
version = "1.33"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "jsonpointer" },
]
sdist = { url = "https://files.pythonhosted.org/packages/42/78/18813351fe5d63acad16aec57f94ec2b70a09e53ca98145589e185423873/jsonpatch-1.33.tar.gz", hash = "sha256:9fcd4009c41e6d12348b4a0ff2563ba56a2923a7dfee731d004e212e1ee5030c", size = 21699, upload-time = "2023-06-26T12:07:29.144Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/73/07/02e16ed01e04a374e644b575638ec7987ae846d25ad97bcc9945a3ee4b0e/jsonpatch-1.33-py2.py3-none-any.whl", hash = "sha256:0ae28c0cd062bbd8b8ecc26d7d164fbbea9652a1a3693f3b956c1eae5145dade", size = 12898, upload-time = "2023-06-16T21:01:28.466Z" },
]

[[package]]
name = "jsonpointer"
version = "3.0.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/6a/0a/eebeb1fa92507ea94016a2a790b93c2ae41a7e18778f85471dc54475ed25/jsonpointer-3.0.0.tar.gz", hash = "sha256:2b2d729f2091522d61c3b31f82e11870f60b68f43fbc705cb76bf4b832af59ef", size = 9114, upload-time = "2024-06-10T19:24:42.462Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/71/92/5e77f98553e9e75130c78900d000368476aed74276eb8ae8796f65f00918/jsonpointer-3.0.0-py2.py3-none-any.whl", hash = "sha256:13e088adc14fca8b6aa8177c044e12701e6ad4b28ff10e65f2267a90109c9942", size = 7595, upload-time = "2024-06-10T19:24:40.698Z" },
]

[[package]]
name = "langchain-core"
version = "1.2.16"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "jsonpatch" },
    { name = "langsmith" },
    { name = "packaging" },
    { name = "pydantic" },
    { name = "pyyaml" },
    { name = "tenacity" },
    { name = "typing-extensions" },
    { name = "uuid-utils" },
]
sdist = { url = "https://files.pythonhosted.org/packages/2e/a7/4c992456dae89a8704afec03e3c2a0149ccc5f29c1cbdd5f4aa77628e921/langchain_core-1.2.16.tar.gz", hash = "sha256:055a4bfe7d62f4ac45ed49fd759ee2e6bdd15abf998fbeea695fda5da2de6413", size = 835286, upload-time = "2026-02-25T16:27:30.551Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/2d/a1/57d5feaa11dc2ebb40f3bc3d7bf4294b6703e152e56edea9d4c622475a6a/langchain_core-1.2.16-py3-none-any.whl", hash = "sha256:2768add9aa97232a7712580f678e0ba045ee1036c71fe471355be0434fcb6e30", size = 502219, upload-time = "2026-02-25T16:27:29.379Z" },
]

[[package]]
name = "langgraph"
version = "1.0.10"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "langchain-core" },
    { name = "langgraph-checkpoint" },
    { name = "langgraph-prebuilt" },
    { name = "langgraph-sdk" },
    { name = "pydantic" },
    { name = "xxhash" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/92/14df6fefba28c10caf1cb05aa5b8c7bf005838fe32a86d903b6c7cc4018d/langgraph-1.0.10.tar.gz", hash = "sha256:73bd10ee14a8020f31ef07e9cd4c1a70c35cc07b9c2b9cd637509a10d9d51e29", size = 511644, upload-time = "2026-02-27T21:04:38.743Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5d/60/260e0c04620a37ba8916b712766c341cc5fc685dabc6948c899494bbc2ae/langgraph-1.0.10-py3-none-any.whl", hash = "sha256:7c298bef4f6ea292fcf9824d6088fe41a6727e2904ad6066f240c4095af12247", size = 160920, upload-time = "2026-02-27T21:04:35.932Z" },
]

[[package]]
name = "langgraph-checkpoint"
version = "4.0.1"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "langchain-core" },
    { name = "ormsgpack" },
]
sdist = { url = "https://files.pythonhosted.org/packages/b1/44/a8df45d1e8b4637e29789fa8bae1db022c953cc7ac80093cfc52e923547e/langgraph_checkpoint-4.0.1.tar.gz", hash = "sha256:b433123735df11ade28829e40ce25b9be614930cd50245ff2af60629234befd9", size = 158135, upload-time = "2026-02-27T21:06:16.092Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/65/4c/09a4a0c42f5d2fc38d6c4d67884788eff7fd2cfdf367fdf7033de908b4c0/langgraph_checkpoint-4.0.1-py3-none-any.whl", hash = "sha256:e3adcd7a0e0166f3b48b8cf508ce0ea366e7420b5a73aa81289888727769b034", size = 50453, upload-time = "2026-02-27T21:06:14.293Z" },
]

[[package]]
name = "langgraph-prebuilt"
version = "1.0.8"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "langchain-core" },
    { name = "langgraph-checkpoint" },
]
sdist = { url = "https://files.pythonhosted.org/packages/0d/06/dd61a5c2dce009d1b03b1d56f2a85b3127659fdddf5b3be5d8f1d60820fb/langgraph_prebuilt-1.0.8.tar.gz", hash = "sha256:0cd3cf5473ced8a6cd687cc5294e08d3de57529d8dd14fdc6ae4899549efcf69", size = 164442, upload-time = "2026-02-19T18:14:39.083Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/41/ec966424ad3f2ed3996d24079d3342c8cd6c0bd0653c12b2a917a685ec6c/langgraph_prebuilt-1.0.8-py3-none-any.whl", hash = "sha256:d16a731e591ba4470f3e313a319c7eee7dbc40895bcf15c821f985a3522a7ce0", size = 35648, upload-time = "2026-02-19T18:14:37.611Z" },
]

[[package]]
name = "langgraph-sdk"
version = "0.3.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "httpx" },
    { name = "orjson" },
]
sdist = { url = "https://files.pythonhosted.org/packages/3a/bd/ca8ae5c6a34be6d4f7aa86016e010ff96b3a939456041565797952e3014d/langgraph_sdk-0.3.9.tar.gz", hash = "sha256:8be8958529b3f6d493ec248fdb46e539362efda75784654a42a7091d22504e0e", size = 184287, upload-time = "2026-02-24T18:39:03.276Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/6a/4c/7a7510260fbda788efd13bf4650d3e7d80988118441ac811ec78e0aa03ac/langgraph_sdk-0.3.9-py3-none-any.whl", hash = "sha256:94654294250c920789b6ed0d8a70c0117fed5736b61efc24ff647157359453c5", size = 90511, upload-time = "2026-02-24T18:39:02.012Z" },
]

[[package]]
name = "langsmith"
version = "0.7.9"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "httpx" },
    { name = "orjson", marker = "platform_python_implementation != 'PyPy'" },
    { name = "packaging" },
    { name = "pydantic" },
    { name = "requests" },
    { name = "requests-toolbelt" },
    { name = "uuid-utils" },
    { name = "xxhash" },
    { name = "zstandard" },
]
sdist = { url = "https://files.pythonhosted.org/packages/4f/01/c26b1d3a68764acd050cbb98f3ca922a25b3e4ece5768ee868f56206b4d4/langsmith-0.7.9.tar.gz", hash = "sha256:c6dfcc4cb8fea249714ac60a1963faa84cc59ded9cd1882794ffce8a8d1d1588", size = 1136295, upload-time = "2026-02-27T22:37:59.309Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b6/c9/2d5e5f654f97a4d38a0ff1b3004751c2cd81ceca05d603174e49f942b196/langsmith-0.7.9-py3-none-any.whl", hash = "sha256:e73478f4c4ae9b7407e0fcdced181f9f8b0e024c62a1552dbf0667ef6b19e82d", size = 344099, upload-time = "2026-02-27T22:37:57.497Z" },
]

[[package]]
name = "orjson"
version = "3.11.7"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/53/45/b268004f745ede84e5798b48ee12b05129d19235d0e15267aa57dcdb400b/orjson-3.11.7.tar.gz", hash = "sha256:9b1a67243945819ce55d24a30b59d6a168e86220452d2c96f4d1f093e71c0c49", size = 6144992, upload-time = "2026-02-02T15:38:49.29Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/89/25/6e0e52cac5aab51d7b6dcd257e855e1dec1c2060f6b28566c509b4665f62/orjson-3.11.7-cp313-cp313-macosx_10_15_x86_64.macosx_11_0_arm64.macosx_10_15_universal2.whl", hash = "sha256:1d98b30cc1313d52d4af17d9c3d307b08389752ec5f2e5febdfada70b0f8c733", size = 228390, upload-time = "2026-02-02T15:38:06.8Z" },
    { url = "https://files.pythonhosted.org/packages/a5/29/a77f48d2fc8a05bbc529e5ff481fb43d914f9e383ea2469d4f3d51df3d00/orjson-3.11.7-cp313-cp313-macosx_15_0_arm64.whl", hash = "sha256:d897e81f8d0cbd2abb82226d1860ad2e1ab3ff16d7b08c96ca00df9d45409ef4", size = 125189, upload-time = "2026-02-02T15:38:08.181Z" },
    { url = "https://files.pythonhosted.org/packages/89/25/0a16e0729a0e6a1504f9d1a13cdd365f030068aab64cec6958396b9969d7/orjson-3.11.7-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:814be4b49b228cfc0b3c565acf642dd7d13538f966e3ccde61f4f55be3e20785", size = 128106, upload-time = "2026-02-02T15:38:09.41Z" },
    { url = "https://files.pythonhosted.org/packages/66/da/a2e505469d60666a05ab373f1a6322eb671cb2ba3a0ccfc7d4bc97196787/orjson-3.11.7-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:d06e5c5fed5caedd2e540d62e5b1c25e8c82431b9e577c33537e5fa4aa909539", size = 123363, upload-time = "2026-02-02T15:38:10.73Z" },
    { url = "https://files.pythonhosted.org/packages/23/bf/ed73f88396ea35c71b38961734ea4a4746f7ca0768bf28fd551d37e48dd0/orjson-3.11.7-cp313-cp313-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:31c80ce534ac4ea3739c5ee751270646cbc46e45aea7576a38ffec040b4029a1", size = 129007, upload-time = "2026-02-02T15:38:12.138Z" },
    { url = "https://files.pythonhosted.org/packages/73/3c/b05d80716f0225fc9008fbf8ab22841dcc268a626aa550561743714ce3bf/orjson-3.11.7-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:f50979824bde13d32b4320eedd513431c921102796d86be3eee0b58e58a3ecd1", size = 141667, upload-time = "2026-02-02T15:38:13.398Z" },
    { url = "https://files.pythonhosted.org/packages/61/e8/0be9b0addd9bf86abfc938e97441dcd0375d494594b1c8ad10fe57479617/orjson-3.11.7-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:9e54f3808e2b6b945078c41aa8d9b5834b28c50843846e97807e5adb75fa9705", size = 130832, upload-time = "2026-02-02T15:38:14.698Z" },
    { url = "https://files.pythonhosted.org/packages/c9/ec/c68e3b9021a31d9ec15a94931db1410136af862955854ed5dd7e7e4f5bff/orjson-3.11.7-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a12b80df61aab7b98b490fe9e4879925ba666fccdfcd175252ce4d9035865ace", size = 133373, upload-time = "2026-02-02T15:38:16.109Z" },
    { url = "https://files.pythonhosted.org/packages/d2/45/f3466739aaafa570cc8e77c6dbb853c48bf56e3b43738020e2661e08b0ac/orjson-3.11.7-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:996b65230271f1a97026fd0e6a753f51fbc0c335d2ad0c6201f711b0da32693b", size = 138307, upload-time = "2026-02-02T15:38:17.453Z" },
    { url = "https://files.pythonhosted.org/packages/e1/84/9f7f02288da1ffb31405c1be07657afd1eecbcb4b64ee2817b6fe0f785fa/orjson-3.11.7-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:ab49d4b2a6a1d415ddb9f37a21e02e0d5dbfe10b7870b21bf779fc21e9156157", size = 408695, upload-time = "2026-02-02T15:38:18.831Z" },
    { url = "https://files.pythonhosted.org/packages/18/07/9dd2f0c0104f1a0295ffbe912bc8d63307a539b900dd9e2c48ef7810d971/orjson-3.11.7-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:390a1dce0c055ddf8adb6aa94a73b45a4a7d7177b5c584b8d1c1947f2ba60fb3", size = 144099, upload-time = "2026-02-02T15:38:20.28Z" },
    { url = "https://files.pythonhosted.org/packages/a5/66/857a8e4a3292e1f7b1b202883bcdeb43a91566cf59a93f97c53b44bd6801/orjson-3.11.7-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:1eb80451a9c351a71dfaf5b7ccc13ad065405217726b59fdbeadbcc544f9d223", size = 134806, upload-time = "2026-02-02T15:38:22.186Z" },
    { url = "https://files.pythonhosted.org/packages/0a/5b/6ebcf3defc1aab3a338ca777214966851e92efb1f30dc7fc8285216e6d1b/orjson-3.11.7-cp313-cp313-win32.whl", hash = "sha256:7477aa6a6ec6139c5cb1cc7b214643592169a5494d200397c7fc95d740d5fcf3", size = 127914, upload-time = "2026-02-02T15:38:23.511Z" },
    { url = "https://files.pythonhosted.org/packages/00/04/c6f72daca5092e3117840a1b1e88dfc809cc1470cf0734890d0366b684a1/orjson-3.11.7-cp313-cp313-win_amd64.whl", hash = "sha256:b9f95dcdea9d4f805daa9ddf02617a89e484c6985fa03055459f90e87d7a0757", size = 124986, upload-time = "2026-02-02T15:38:24.836Z" },
    { url = "https://files.pythonhosted.org/packages/03/ba/077a0f6f1085d6b806937246860fafbd5b17f3919c70ee3f3d8d9c713f38/orjson-3.11.7-cp313-cp313-win_arm64.whl", hash = "sha256:800988273a014a0541483dc81021247d7eacb0c845a9d1a34a422bc718f41539", size = 126045, upload-time = "2026-02-02T15:38:26.216Z" },
    { url = "https://files.pythonhosted.org/packages/e9/1e/745565dca749813db9a093c5ebc4bac1a9475c64d54b95654336ac3ed961/orjson-3.11.7-cp314-cp314-macosx_10_15_x86_64.macosx_11_0_arm64.macosx_10_15_universal2.whl", hash = "sha256:de0a37f21d0d364954ad5de1970491d7fbd0fb1ef7417d4d56a36dc01ba0c0a0", size = 228391, upload-time = "2026-02-02T15:38:27.757Z" },
    { url = "https://files.pythonhosted.org/packages/46/19/e40f6225da4d3aa0c8dc6e5219c5e87c2063a560fe0d72a88deb59776794/orjson-3.11.7-cp314-cp314-macosx_15_0_arm64.whl", hash = "sha256:c2428d358d85e8da9d37cba18b8c4047c55222007a84f97156a5b22028dfbfc0", size = 125188, upload-time = "2026-02-02T15:38:29.241Z" },
    { url = "https://files.pythonhosted.org/packages/9d/7e/c4de2babef2c0817fd1f048fd176aa48c37bec8aef53d2fa932983032cce/orjson-3.11.7-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3c4bc6c6ac52cdaa267552544c73e486fecbd710b7ac09bc024d5a78555a22f6", size = 128097, upload-time = "2026-02-02T15:38:30.618Z" },
    { url = "https://files.pythonhosted.org/packages/eb/74/233d360632bafd2197f217eee7fb9c9d0229eac0c18128aee5b35b0014fe/orjson-3.11.7-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:bd0d68edd7dfca1b2eca9361a44ac9f24b078de3481003159929a0573f21a6bf", size = 123364, upload-time = "2026-02-02T15:38:32.363Z" },
    { url = "https://files.pythonhosted.org/packages/79/51/af79504981dd31efe20a9e360eb49c15f06df2b40e7f25a0a52d9ae888e8/orjson-3.11.7-cp314-cp314-manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:623ad1b9548ef63886319c16fa317848e465a21513b31a6ad7b57443c3e0dcf5", size = 129076, upload-time = "2026-02-02T15:38:33.68Z" },
    { url = "https://files.pythonhosted.org/packages/67/e2/da898eb68b72304f8de05ca6715870d09d603ee98d30a27e8a9629abc64b/orjson-3.11.7-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:6e776b998ac37c0396093d10290e60283f59cfe0fc3fccbd0ccc4bd04dd19892", size = 141705, upload-time = "2026-02-02T15:38:34.989Z" },
    { url = "https://files.pythonhosted.org/packages/c5/89/15364d92acb3d903b029e28d834edb8780c2b97404cbf7929aa6b9abdb24/orjson-3.11.7-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:652c6c3af76716f4a9c290371ba2e390ede06f6603edb277b481daf37f6f464e", size = 130855, upload-time = "2026-02-02T15:38:36.379Z" },
    { url = "https://files.pythonhosted.org/packages/c2/8b/ecdad52d0b38d4b8f514be603e69ccd5eacf4e7241f972e37e79792212ec/orjson-3.11.7-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:a56df3239294ea5964adf074c54bcc4f0ccd21636049a2cf3ca9cf03b5d03cf1", size = 133386, upload-time = "2026-02-02T15:38:37.704Z" },
    { url = "https://files.pythonhosted.org/packages/b9/0e/45e1dcf10e17d0924b7c9162f87ec7b4ca79e28a0548acf6a71788d3e108/orjson-3.11.7-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:bda117c4148e81f746655d5a3239ae9bd00cb7bc3ca178b5fc5a5997e9744183", size = 138295, upload-time = "2026-02-02T15:38:39.096Z" },
    { url = "https://files.pythonhosted.org/packages/63/d7/4d2e8b03561257af0450f2845b91fbd111d7e526ccdf737267108075e0ba/orjson-3.11.7-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:23d6c20517a97a9daf1d48b580fcdc6f0516c6f4b5038823426033690b4d2650", size = 408720, upload-time = "2026-02-02T15:38:40.634Z" },
    { url = "https://files.pythonhosted.org/packages/78/cf/d45343518282108b29c12a65892445fc51f9319dc3c552ceb51bb5905ed2/orjson-3.11.7-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:8ff206156006da5b847c9304b6308a01e8cdbc8cce824e2779a5ba71c3def141", size = 144152, upload-time = "2026-02-02T15:38:42.262Z" },
    { url = "https://files.pythonhosted.org/packages/a9/3a/d6001f51a7275aacd342e77b735c71fa04125a3f93c36fee4526bc8c654e/orjson-3.11.7-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:962d046ee1765f74a1da723f4b33e3b228fe3a48bd307acce5021dfefe0e29b2", size = 134814, upload-time = "2026-02-02T15:38:43.627Z" },
    { url = "https://files.pythonhosted.org/packages/1d/d3/f19b47ce16820cc2c480f7f1723e17f6d411b3a295c60c8ad3aa9ff1c96a/orjson-3.11.7-cp314-cp314-win32.whl", hash = "sha256:89e13dd3f89f1c38a9c9eba5fbf7cdc2d1feca82f5f290864b4b7a6aac704576", size = 127997, upload-time = "2026-02-02T15:38:45.06Z" },
    { url = "https://files.pythonhosted.org/packages/12/df/172771902943af54bf661a8d102bdf2e7f932127968080632bda6054b62c/orjson-3.11.7-cp314-cp314-win_amd64.whl", hash = "sha256:845c3e0d8ded9c9271cd79596b9b552448b885b97110f628fb687aee2eed11c1", size = 124985, upload-time = "2026-02-02T15:38:46.388Z" },
    { url = "https://files.pythonhosted.org/packages/6f/1c/f2a8d8a1b17514660a614ce5f7aac74b934e69f5abc2700cc7ced882a009/orjson-3.11.7-cp314-cp314-win_arm64.whl", hash = "sha256:4a2e9c5be347b937a2e0203866f12bba36082e89b402ddb9e927d5822e43088d", size = 126038, upload-time = "2026-02-02T15:38:47.703Z" },
]

[[package]]
name = "ormsgpack"
version = "1.12.2"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/12/0c/f1761e21486942ab9bb6feaebc610fa074f7c5e496e6962dea5873348077/ormsgpack-1.12.2.tar.gz", hash = "sha256:944a2233640273bee67521795a73cf1e959538e0dfb7ac635505010455e53b33", size = 39031, upload-time = "2026-01-18T20:55:28.023Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/eb/29/bb0eba3288c0449efbb013e9c6f58aea79cf5cb9ee1921f8865f04c1a9d7/ormsgpack-1.12.2-cp313-cp313-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl", hash = "sha256:5ea60cb5f210b1cfbad8c002948d73447508e629ec375acb82910e3efa8ff355", size = 378661, upload-time = "2026-01-18T20:55:57.765Z" },
    { url = "https://files.pythonhosted.org/packages/6e/31/5efa31346affdac489acade2926989e019e8ca98129658a183e3add7af5e/ormsgpack-1.12.2-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:f3601f19afdbea273ed70b06495e5794606a8b690a568d6c996a90d7255e51c1", size = 203194, upload-time = "2026-01-18T20:56:08.252Z" },
    { url = "https://files.pythonhosted.org/packages/eb/56/d0087278beef833187e0167f8527235ebe6f6ffc2a143e9de12a98b1ce87/ormsgpack-1.12.2-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:29a9f17a3dac6054c0dce7925e0f4995c727f7c41859adf9b5572180f640d172", size = 210778, upload-time = "2026-01-18T20:55:17.694Z" },
    { url = "https://files.pythonhosted.org/packages/1c/a2/072343e1413d9443e5a252a8eb591c2d5b1bffbe5e7bfc78c069361b92eb/ormsgpack-1.12.2-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:39c1bd2092880e413902910388be8715f70b9f15f20779d44e673033a6146f2d", size = 212592, upload-time = "2026-01-18T20:55:32.747Z" },
    { url = "https://files.pythonhosted.org/packages/a2/8b/a0da3b98a91d41187a63b02dda14267eefc2a74fcb43cc2701066cf1510e/ormsgpack-1.12.2-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:50b7249244382209877deedeee838aef1542f3d0fc28b8fe71ca9d7e1896a0d7", size = 387164, upload-time = "2026-01-18T20:55:40.853Z" },
    { url = "https://files.pythonhosted.org/packages/19/bb/6d226bc4cf9fc20d8eb1d976d027a3f7c3491e8f08289a2e76abe96a65f3/ormsgpack-1.12.2-cp313-cp313-musllinux_1_2_armv7l.whl", hash = "sha256:5af04800d844451cf102a59c74a841324868d3f1625c296a06cc655c542a6685", size = 482516, upload-time = "2026-01-18T20:55:42.033Z" },
    { url = "https://files.pythonhosted.org/packages/fb/f1/bb2c7223398543dedb3dbf8bb93aaa737b387de61c5feaad6f908841b782/ormsgpack-1.12.2-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:cec70477d4371cd524534cd16472d8b9cc187e0e3043a8790545a9a9b296c258", size = 425539, upload-time = "2026-01-18T20:55:24.727Z" },
    { url = "https://files.pythonhosted.org/packages/7b/e8/0fb45f57a2ada1fed374f7494c8cd55e2f88ccd0ab0a669aa3468716bf5f/ormsgpack-1.12.2-cp313-cp313-win_amd64.whl", hash = "sha256:21f4276caca5c03a818041d637e4019bc84f9d6ca8baa5ea03e5cc8bf56140e9", size = 117459, upload-time = "2026-01-18T20:55:56.876Z" },
    { url = "https://files.pythonhosted.org/packages/7a/d4/0cfeea1e960d550a131001a7f38a5132c7ae3ebde4c82af1f364ccc5d904/ormsgpack-1.12.2-cp313-cp313-win_arm64.whl", hash = "sha256:baca4b6773d20a82e36d6fd25f341064244f9f86a13dead95dd7d7f996f51709", size = 111577, upload-time = "2026-01-18T20:55:43.605Z" },
    { url = "https://files.pythonhosted.org/packages/94/16/24d18851334be09c25e87f74307c84950f18c324a4d3c0b41dabdbf19c29/ormsgpack-1.12.2-cp314-cp314-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl", hash = "sha256:bc68dd5915f4acf66ff2010ee47c8906dc1cf07399b16f4089f8c71733f6e36c", size = 378717, upload-time = "2026-01-18T20:55:26.164Z" },
    { url = "https://files.pythonhosted.org/packages/b5/a2/88b9b56f83adae8032ac6a6fa7f080c65b3baf9b6b64fd3d37bd202991d4/ormsgpack-1.12.2-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:46d084427b4132553940070ad95107266656cb646ea9da4975f85cb1a6676553", size = 203183, upload-time = "2026-01-18T20:55:18.815Z" },
    { url = "https://files.pythonhosted.org/packages/a9/80/43e4555963bf602e5bdc79cbc8debd8b6d5456c00d2504df9775e74b450b/ormsgpack-1.12.2-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:c010da16235806cf1d7bc4c96bf286bfa91c686853395a299b3ddb49499a3e13", size = 210814, upload-time = "2026-01-18T20:55:33.973Z" },
    { url = "https://files.pythonhosted.org/packages/78/e1/7cfbf28de8bca6efe7e525b329c31277d1b64ce08dcba723971c241a9d60/ormsgpack-1.12.2-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:18867233df592c997154ff942a6503df274b5ac1765215bceba7a231bea2745d", size = 212634, upload-time = "2026-01-18T20:55:28.634Z" },
    { url = "https://files.pythonhosted.org/packages/95/f8/30ae5716e88d792a4e879debee195653c26ddd3964c968594ddef0a3cc7e/ormsgpack-1.12.2-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:b009049086ddc6b8f80c76b3955df1aa22a5fbd7673c525cd63bf91f23122ede", size = 387139, upload-time = "2026-01-18T20:56:02.013Z" },
    { url = "https://files.pythonhosted.org/packages/dc/81/aee5b18a3e3a0e52f718b37ab4b8af6fae0d9d6a65103036a90c2a8ffb5d/ormsgpack-1.12.2-cp314-cp314-musllinux_1_2_armv7l.whl", hash = "sha256:1dcc17d92b6390d4f18f937cf0b99054824a7815818012ddca925d6e01c2e49e", size = 482578, upload-time = "2026-01-18T20:55:35.117Z" },
    { url = "https://files.pythonhosted.org/packages/bd/17/71c9ba472d5d45f7546317f467a5fc941929cd68fb32796ca3d13dcbaec2/ormsgpack-1.12.2-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:f04b5e896d510b07c0ad733d7fce2d44b260c5e6c402d272128f8941984e4285", size = 425539, upload-time = "2026-01-18T20:56:04.009Z" },
    { url = "https://files.pythonhosted.org/packages/2e/a6/ac99cd7fe77e822fed5250ff4b86fa66dd4238937dd178d2299f10b69816/ormsgpack-1.12.2-cp314-cp314-win_amd64.whl", hash = "sha256:ae3aba7eed4ca7cb79fd3436eddd29140f17ea254b91604aa1eb19bfcedb990f", size = 117493, upload-time = "2026-01-18T20:56:07.343Z" },
    { url = "https://files.pythonhosted.org/packages/3a/67/339872846a1ae4592535385a1c1f93614138566d7af094200c9c3b45d1e5/ormsgpack-1.12.2-cp314-cp314-win_arm64.whl", hash = "sha256:118576ea6006893aea811b17429bfc561b4778fad393f5f538c84af70b01260c", size = 111579, upload-time = "2026-01-18T20:55:21.161Z" },
    { url = "https://files.pythonhosted.org/packages/49/c2/6feb972dc87285ad381749d3882d8aecbde9f6ecf908dd717d33d66df095/ormsgpack-1.12.2-cp314-cp314t-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl", hash = "sha256:7121b3d355d3858781dc40dafe25a32ff8a8242b9d80c692fd548a4b1f7fd3c8", size = 378721, upload-time = "2026-01-18T20:55:52.12Z" },
    { url = "https://files.pythonhosted.org/packages/a3/9a/900a6b9b413e0f8a471cf07830f9cf65939af039a362204b36bd5b581d8b/ormsgpack-1.12.2-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:4ee766d2e78251b7a63daf1cddfac36a73562d3ddef68cacfb41b2af64698033", size = 203170, upload-time = "2026-01-18T20:55:44.469Z" },
    { url = "https://files.pythonhosted.org/packages/87/4c/27a95466354606b256f24fad464d7c97ab62bce6cc529dd4673e1179b8fb/ormsgpack-1.12.2-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:292410a7d23de9b40444636b9b8f1e4e4b814af7f1ef476e44887e52a123f09d", size = 212816, upload-time = "2026-01-18T20:55:23.501Z" },
    { url = "https://files.pythonhosted.org/packages/73/cd/29cee6007bddf7a834e6cd6f536754c0535fcb939d384f0f37a38b1cddb8/ormsgpack-1.12.2-cp314-cp314t-win_amd64.whl", hash = "sha256:837dd316584485b72ef451d08dd3e96c4a11d12e4963aedb40e08f89685d8ec2", size = 117232, upload-time = "2026-01-18T20:55:45.448Z" },
]

[[package]]
name = "packaging"
version = "26.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/65/ee/299d360cdc32edc7d2cf530f3accf79c4fca01e96ffc950d8a52213bd8e4/packaging-26.0.tar.gz", hash = "sha256:00243ae351a257117b6a241061796684b084ed1c516a08c48a3f7e147a9d80b4", size = 143416, upload-time = "2026-01-21T20:50:39.064Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/b7/b9/c538f279a4e237a006a2c98387d081e9eb060d203d8ed34467cc0f0b9b53/packaging-26.0-py3-none-any.whl", hash = "sha256:b36f1fef9334a5588b4166f8bcd26a14e521f2b55e6b9de3aaa80d3ff7a37529", size = 74366, upload-time = "2026-01-21T20:50:37.788Z" },
]

[[package]]
name = "pydantic"
version = "2.12.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "annotated-types" },
    { name = "pydantic-core" },
    { name = "typing-extensions" },
    { name = "typing-inspection" },
]
sdist = { url = "https://files.pythonhosted.org/packages/69/44/36f1a6e523abc58ae5f928898e4aca2e0ea509b5aa6f6f392a5d882be928/pydantic-2.12.5.tar.gz", hash = "sha256:4d351024c75c0f085a9febbb665ce8c0c6ec5d30e903bdb6394b7ede26aebb49", size = 821591, upload-time = "2025-11-26T15:11:46.471Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/5a/87/b70ad306ebb6f9b585f114d0ac2137d792b48be34d732d60e597c2f8465a/pydantic-2.12.5-py3-none-any.whl", hash = "sha256:e561593fccf61e8a20fc46dfc2dfe075b8be7d0188df33f221ad1f0139180f9d", size = 463580, upload-time = "2025-11-26T15:11:44.605Z" },
]

[[package]]
name = "pydantic-core"
version = "2.41.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/71/70/23b021c950c2addd24ec408e9ab05d59b035b39d97cdc1130e1bce647bb6/pydantic_core-2.41.5.tar.gz", hash = "sha256:08daa51ea16ad373ffd5e7606252cc32f07bc72b28284b6bc9c6df804816476e", size = 460952, upload-time = "2025-11-04T13:43:49.098Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/87/06/8806241ff1f70d9939f9af039c6c35f2360cf16e93c2ca76f184e76b1564/pydantic_core-2.41.5-cp313-cp313-macosx_10_12_x86_64.whl", hash = "sha256:941103c9be18ac8daf7b7adca8228f8ed6bb7a1849020f643b3a14d15b1924d9", size = 2120403, upload-time = "2025-11-04T13:40:25.248Z" },
    { url = "https://files.pythonhosted.org/packages/94/02/abfa0e0bda67faa65fef1c84971c7e45928e108fe24333c81f3bfe35d5f5/pydantic_core-2.41.5-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:112e305c3314f40c93998e567879e887a3160bb8689ef3d2c04b6cc62c33ac34", size = 1896206, upload-time = "2025-11-04T13:40:27.099Z" },
    { url = "https://files.pythonhosted.org/packages/15/df/a4c740c0943e93e6500f9eb23f4ca7ec9bf71b19e608ae5b579678c8d02f/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:0cbaad15cb0c90aa221d43c00e77bb33c93e8d36e0bf74760cd00e732d10a6a0", size = 1919307, upload-time = "2025-11-04T13:40:29.806Z" },
    { url = "https://files.pythonhosted.org/packages/9a/e3/6324802931ae1d123528988e0e86587c2072ac2e5394b4bc2bc34b61ff6e/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:03ca43e12fab6023fc79d28ca6b39b05f794ad08ec2feccc59a339b02f2b3d33", size = 2063258, upload-time = "2025-11-04T13:40:33.544Z" },
    { url = "https://files.pythonhosted.org/packages/c9/d4/2230d7151d4957dd79c3044ea26346c148c98fbf0ee6ebd41056f2d62ab5/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:dc799088c08fa04e43144b164feb0c13f9a0bc40503f8df3e9fde58a3c0c101e", size = 2214917, upload-time = "2025-11-04T13:40:35.479Z" },
    { url = "https://files.pythonhosted.org/packages/e6/9f/eaac5df17a3672fef0081b6c1bb0b82b33ee89aa5cec0d7b05f52fd4a1fa/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:97aeba56665b4c3235a0e52b2c2f5ae9cd071b8a8310ad27bddb3f7fb30e9aa2", size = 2332186, upload-time = "2025-11-04T13:40:37.436Z" },
    { url = "https://files.pythonhosted.org/packages/cf/4e/35a80cae583a37cf15604b44240e45c05e04e86f9cfd766623149297e971/pydantic_core-2.41.5-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:406bf18d345822d6c21366031003612b9c77b3e29ffdb0f612367352aab7d586", size = 2073164, upload-time = "2025-11-04T13:40:40.289Z" },
    { url = "https://files.pythonhosted.org/packages/bf/e3/f6e262673c6140dd3305d144d032f7bd5f7497d3871c1428521f19f9efa2/pydantic_core-2.41.5-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:b93590ae81f7010dbe380cdeab6f515902ebcbefe0b9327cc4804d74e93ae69d", size = 2179146, upload-time = "2025-11-04T13:40:42.809Z" },
    { url = "https://files.pythonhosted.org/packages/75/c7/20bd7fc05f0c6ea2056a4565c6f36f8968c0924f19b7d97bbfea55780e73/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:01a3d0ab748ee531f4ea6c3e48ad9dac84ddba4b0d82291f87248f2f9de8d740", size = 2137788, upload-time = "2025-11-04T13:40:44.752Z" },
    { url = "https://files.pythonhosted.org/packages/3a/8d/34318ef985c45196e004bc46c6eab2eda437e744c124ef0dbe1ff2c9d06b/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_armv7l.whl", hash = "sha256:6561e94ba9dacc9c61bce40e2d6bdc3bfaa0259d3ff36ace3b1e6901936d2e3e", size = 2340133, upload-time = "2025-11-04T13:40:46.66Z" },
    { url = "https://files.pythonhosted.org/packages/9c/59/013626bf8c78a5a5d9350d12e7697d3d4de951a75565496abd40ccd46bee/pydantic_core-2.41.5-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:915c3d10f81bec3a74fbd4faebe8391013ba61e5a1a8d48c4455b923bdda7858", size = 2324852, upload-time = "2025-11-04T13:40:48.575Z" },
    { url = "https://files.pythonhosted.org/packages/1a/d9/c248c103856f807ef70c18a4f986693a46a8ffe1602e5d361485da502d20/pydantic_core-2.41.5-cp313-cp313-win32.whl", hash = "sha256:650ae77860b45cfa6e2cdafc42618ceafab3a2d9a3811fcfbd3bbf8ac3c40d36", size = 1994679, upload-time = "2025-11-04T13:40:50.619Z" },
    { url = "https://files.pythonhosted.org/packages/9e/8b/341991b158ddab181cff136acd2552c9f35bd30380422a639c0671e99a91/pydantic_core-2.41.5-cp313-cp313-win_amd64.whl", hash = "sha256:79ec52ec461e99e13791ec6508c722742ad745571f234ea6255bed38c6480f11", size = 2019766, upload-time = "2025-11-04T13:40:52.631Z" },
    { url = "https://files.pythonhosted.org/packages/73/7d/f2f9db34af103bea3e09735bb40b021788a5e834c81eedb541991badf8f5/pydantic_core-2.41.5-cp313-cp313-win_arm64.whl", hash = "sha256:3f84d5c1b4ab906093bdc1ff10484838aca54ef08de4afa9de0f5f14d69639cd", size = 1981005, upload-time = "2025-11-04T13:40:54.734Z" },
    { url = "https://files.pythonhosted.org/packages/ea/28/46b7c5c9635ae96ea0fbb779e271a38129df2550f763937659ee6c5dbc65/pydantic_core-2.41.5-cp314-cp314-macosx_10_12_x86_64.whl", hash = "sha256:3f37a19d7ebcdd20b96485056ba9e8b304e27d9904d233d7b1015db320e51f0a", size = 2119622, upload-time = "2025-11-04T13:40:56.68Z" },
    { url = "https://files.pythonhosted.org/packages/74/1a/145646e5687e8d9a1e8d09acb278c8535ebe9e972e1f162ed338a622f193/pydantic_core-2.41.5-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:1d1d9764366c73f996edd17abb6d9d7649a7eb690006ab6adbda117717099b14", size = 1891725, upload-time = "2025-11-04T13:40:58.807Z" },
    { url = "https://files.pythonhosted.org/packages/23/04/e89c29e267b8060b40dca97bfc64a19b2a3cf99018167ea1677d96368273/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:25e1c2af0fce638d5f1988b686f3b3ea8cd7de5f244ca147c777769e798a9cd1", size = 1915040, upload-time = "2025-11-04T13:41:00.853Z" },
    { url = "https://files.pythonhosted.org/packages/84/a3/15a82ac7bd97992a82257f777b3583d3e84bdb06ba6858f745daa2ec8a85/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:506d766a8727beef16b7adaeb8ee6217c64fc813646b424d0804d67c16eddb66", size = 2063691, upload-time = "2025-11-04T13:41:03.504Z" },
    { url = "https://files.pythonhosted.org/packages/74/9b/0046701313c6ef08c0c1cf0e028c67c770a4e1275ca73131563c5f2a310a/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:4819fa52133c9aa3c387b3328f25c1facc356491e6135b459f1de698ff64d869", size = 2213897, upload-time = "2025-11-04T13:41:05.804Z" },
    { url = "https://files.pythonhosted.org/packages/8a/cd/6bac76ecd1b27e75a95ca3a9a559c643b3afcd2dd62086d4b7a32a18b169/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:2b761d210c9ea91feda40d25b4efe82a1707da2ef62901466a42492c028553a2", size = 2333302, upload-time = "2025-11-04T13:41:07.809Z" },
    { url = "https://files.pythonhosted.org/packages/4c/d2/ef2074dc020dd6e109611a8be4449b98cd25e1b9b8a303c2f0fca2f2bcf7/pydantic_core-2.41.5-cp314-cp314-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:22f0fb8c1c583a3b6f24df2470833b40207e907b90c928cc8d3594b76f874375", size = 2064877, upload-time = "2025-11-04T13:41:09.827Z" },
    { url = "https://files.pythonhosted.org/packages/18/66/e9db17a9a763d72f03de903883c057b2592c09509ccfe468187f2a2eef29/pydantic_core-2.41.5-cp314-cp314-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:2782c870e99878c634505236d81e5443092fba820f0373997ff75f90f68cd553", size = 2180680, upload-time = "2025-11-04T13:41:12.379Z" },
    { url = "https://files.pythonhosted.org/packages/d3/9e/3ce66cebb929f3ced22be85d4c2399b8e85b622db77dad36b73c5387f8f8/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_aarch64.whl", hash = "sha256:0177272f88ab8312479336e1d777f6b124537d47f2123f89cb37e0accea97f90", size = 2138960, upload-time = "2025-11-04T13:41:14.627Z" },
    { url = "https://files.pythonhosted.org/packages/a6/62/205a998f4327d2079326b01abee48e502ea739d174f0a89295c481a2272e/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_armv7l.whl", hash = "sha256:63510af5e38f8955b8ee5687740d6ebf7c2a0886d15a6d65c32814613681bc07", size = 2339102, upload-time = "2025-11-04T13:41:16.868Z" },
    { url = "https://files.pythonhosted.org/packages/3c/0d/f05e79471e889d74d3d88f5bd20d0ed189ad94c2423d81ff8d0000aab4ff/pydantic_core-2.41.5-cp314-cp314-musllinux_1_1_x86_64.whl", hash = "sha256:e56ba91f47764cc14f1daacd723e3e82d1a89d783f0f5afe9c364b8bb491ccdb", size = 2326039, upload-time = "2025-11-04T13:41:18.934Z" },
    { url = "https://files.pythonhosted.org/packages/ec/e1/e08a6208bb100da7e0c4b288eed624a703f4d129bde2da475721a80cab32/pydantic_core-2.41.5-cp314-cp314-win32.whl", hash = "sha256:aec5cf2fd867b4ff45b9959f8b20ea3993fc93e63c7363fe6851424c8a7e7c23", size = 1995126, upload-time = "2025-11-04T13:41:21.418Z" },
    { url = "https://files.pythonhosted.org/packages/48/5d/56ba7b24e9557f99c9237e29f5c09913c81eeb2f3217e40e922353668092/pydantic_core-2.41.5-cp314-cp314-win_amd64.whl", hash = "sha256:8e7c86f27c585ef37c35e56a96363ab8de4e549a95512445b85c96d3e2f7c1bf", size = 2015489, upload-time = "2025-11-04T13:41:24.076Z" },
    { url = "https://files.pythonhosted.org/packages/4e/bb/f7a190991ec9e3e0ba22e4993d8755bbc4a32925c0b5b42775c03e8148f9/pydantic_core-2.41.5-cp314-cp314-win_arm64.whl", hash = "sha256:e672ba74fbc2dc8eea59fb6d4aed6845e6905fc2a8afe93175d94a83ba2a01a0", size = 1977288, upload-time = "2025-11-04T13:41:26.33Z" },
    { url = "https://files.pythonhosted.org/packages/92/ed/77542d0c51538e32e15afe7899d79efce4b81eee631d99850edc2f5e9349/pydantic_core-2.41.5-cp314-cp314t-macosx_10_12_x86_64.whl", hash = "sha256:8566def80554c3faa0e65ac30ab0932b9e3a5cd7f8323764303d468e5c37595a", size = 2120255, upload-time = "2025-11-04T13:41:28.569Z" },
    { url = "https://files.pythonhosted.org/packages/bb/3d/6913dde84d5be21e284439676168b28d8bbba5600d838b9dca99de0fad71/pydantic_core-2.41.5-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:b80aa5095cd3109962a298ce14110ae16b8c1aece8b72f9dafe81cf597ad80b3", size = 1863760, upload-time = "2025-11-04T13:41:31.055Z" },
    { url = "https://files.pythonhosted.org/packages/5a/f0/e5e6b99d4191da102f2b0eb9687aaa7f5bea5d9964071a84effc3e40f997/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:3006c3dd9ba34b0c094c544c6006cc79e87d8612999f1a5d43b769b89181f23c", size = 1878092, upload-time = "2025-11-04T13:41:33.21Z" },
    { url = "https://files.pythonhosted.org/packages/71/48/36fb760642d568925953bcc8116455513d6e34c4beaa37544118c36aba6d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:72f6c8b11857a856bcfa48c86f5368439f74453563f951e473514579d44aa612", size = 2053385, upload-time = "2025-11-04T13:41:35.508Z" },
    { url = "https://files.pythonhosted.org/packages/20/25/92dc684dd8eb75a234bc1c764b4210cf2646479d54b47bf46061657292a8/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5cb1b2f9742240e4bb26b652a5aeb840aa4b417c7748b6f8387927bc6e45e40d", size = 2218832, upload-time = "2025-11-04T13:41:37.732Z" },
    { url = "https://files.pythonhosted.org/packages/e2/09/f53e0b05023d3e30357d82eb35835d0f6340ca344720a4599cd663dca599/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:bd3d54f38609ff308209bd43acea66061494157703364ae40c951f83ba99a1a9", size = 2327585, upload-time = "2025-11-04T13:41:40Z" },
    { url = "https://files.pythonhosted.org/packages/aa/4e/2ae1aa85d6af35a39b236b1b1641de73f5a6ac4d5a7509f77b814885760c/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:2ff4321e56e879ee8d2a879501c8e469414d948f4aba74a2d4593184eb326660", size = 2041078, upload-time = "2025-11-04T13:41:42.323Z" },
    { url = "https://files.pythonhosted.org/packages/cd/13/2e215f17f0ef326fc72afe94776edb77525142c693767fc347ed6288728d/pydantic_core-2.41.5-cp314-cp314t-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:d0d2568a8c11bf8225044aa94409e21da0cb09dcdafe9ecd10250b2baad531a9", size = 2173914, upload-time = "2025-11-04T13:41:45.221Z" },
    { url = "https://files.pythonhosted.org/packages/02/7a/f999a6dcbcd0e5660bc348a3991c8915ce6599f4f2c6ac22f01d7a10816c/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_aarch64.whl", hash = "sha256:a39455728aabd58ceabb03c90e12f71fd30fa69615760a075b9fec596456ccc3", size = 2129560, upload-time = "2025-11-04T13:41:47.474Z" },
    { url = "https://files.pythonhosted.org/packages/3a/b1/6c990ac65e3b4c079a4fb9f5b05f5b013afa0f4ed6780a3dd236d2cbdc64/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_armv7l.whl", hash = "sha256:239edca560d05757817c13dc17c50766136d21f7cd0fac50295499ae24f90fdf", size = 2329244, upload-time = "2025-11-04T13:41:49.992Z" },
    { url = "https://files.pythonhosted.org/packages/d9/02/3c562f3a51afd4d88fff8dffb1771b30cfdfd79befd9883ee094f5b6c0d8/pydantic_core-2.41.5-cp314-cp314t-musllinux_1_1_x86_64.whl", hash = "sha256:2a5e06546e19f24c6a96a129142a75cee553cc018ffee48a460059b1185f4470", size = 2331955, upload-time = "2025-11-04T13:41:54.079Z" },
    { url = "https://files.pythonhosted.org/packages/5c/96/5fb7d8c3c17bc8c62fdb031c47d77a1af698f1d7a406b0f79aaa1338f9ad/pydantic_core-2.41.5-cp314-cp314t-win32.whl", hash = "sha256:b4ececa40ac28afa90871c2cc2b9ffd2ff0bf749380fbdf57d165fd23da353aa", size = 1988906, upload-time = "2025-11-04T13:41:56.606Z" },
    { url = "https://files.pythonhosted.org/packages/22/ed/182129d83032702912c2e2d8bbe33c036f342cc735737064668585dac28f/pydantic_core-2.41.5-cp314-cp314t-win_amd64.whl", hash = "sha256:80aa89cad80b32a912a65332f64a4450ed00966111b6615ca6816153d3585a8c", size = 1981607, upload-time = "2025-11-04T13:41:58.889Z" },
    { url = "https://files.pythonhosted.org/packages/9f/ed/068e41660b832bb0b1aa5b58011dea2a3fe0ba7861ff38c4d4904c1c1a99/pydantic_core-2.41.5-cp314-cp314t-win_arm64.whl", hash = "sha256:35b44f37a3199f771c3eaa53051bc8a70cd7b54f333531c59e29fd4db5d15008", size = 1974769, upload-time = "2025-11-04T13:42:01.186Z" },
]

[[package]]
name = "python-dotenv"
version = "1.2.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/f0/26/19cadc79a718c5edbec86fd4919a6b6d3f681039a2f6d66d14be94e75fb9/python_dotenv-1.2.1.tar.gz", hash = "sha256:42667e897e16ab0d66954af0e60a9caa94f0fd4ecf3aaf6d2d260eec1aa36ad6", size = 44221, upload-time = "2025-10-26T15:12:10.434Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/14/1b/a298b06749107c305e1fe0f814c6c74aea7b2f1e10989cb30f544a1b3253/python_dotenv-1.2.1-py3-none-any.whl", hash = "sha256:b81ee9561e9ca4004139c6cbba3a238c32b03e4894671e181b671e8cb8425d61", size = 21230, upload-time = "2025-10-26T15:12:09.109Z" },
]

[[package]]
name = "pyyaml"
version = "6.0.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/05/8e/961c0007c59b8dd7729d542c61a4d537767a59645b82a0b521206e1e25c2/pyyaml-6.0.3.tar.gz", hash = "sha256:d76623373421df22fb4cf8817020cbb7ef15c725b9d5e45f17e189bfc384190f", size = 130960, upload-time = "2025-09-25T21:33:16.546Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d1/11/0fd08f8192109f7169db964b5707a2f1e8b745d4e239b784a5a1dd80d1db/pyyaml-6.0.3-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:8da9669d359f02c0b91ccc01cac4a67f16afec0dac22c2ad09f46bee0697eba8", size = 181669, upload-time = "2025-09-25T21:32:23.673Z" },
    { url = "https://files.pythonhosted.org/packages/b1/16/95309993f1d3748cd644e02e38b75d50cbc0d9561d21f390a76242ce073f/pyyaml-6.0.3-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:2283a07e2c21a2aa78d9c4442724ec1eb15f5e42a723b99cb3d822d48f5f7ad1", size = 173252, upload-time = "2025-09-25T21:32:25.149Z" },
    { url = "https://files.pythonhosted.org/packages/50/31/b20f376d3f810b9b2371e72ef5adb33879b25edb7a6d072cb7ca0c486398/pyyaml-6.0.3-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:ee2922902c45ae8ccada2c5b501ab86c36525b883eff4255313a253a3160861c", size = 767081, upload-time = "2025-09-25T21:32:26.575Z" },
    { url = "https://files.pythonhosted.org/packages/49/1e/a55ca81e949270d5d4432fbbd19dfea5321eda7c41a849d443dc92fd1ff7/pyyaml-6.0.3-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a33284e20b78bd4a18c8c2282d549d10bc8408a2a7ff57653c0cf0b9be0afce5", size = 841159, upload-time = "2025-09-25T21:32:27.727Z" },
    { url = "https://files.pythonhosted.org/packages/74/27/e5b8f34d02d9995b80abcef563ea1f8b56d20134d8f4e5e81733b1feceb2/pyyaml-6.0.3-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0f29edc409a6392443abf94b9cf89ce99889a1dd5376d94316ae5145dfedd5d6", size = 801626, upload-time = "2025-09-25T21:32:28.878Z" },
    { url = "https://files.pythonhosted.org/packages/f9/11/ba845c23988798f40e52ba45f34849aa8a1f2d4af4b798588010792ebad6/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f7057c9a337546edc7973c0d3ba84ddcdf0daa14533c2065749c9075001090e6", size = 753613, upload-time = "2025-09-25T21:32:30.178Z" },
    { url = "https://files.pythonhosted.org/packages/3d/e0/7966e1a7bfc0a45bf0a7fb6b98ea03fc9b8d84fa7f2229e9659680b69ee3/pyyaml-6.0.3-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:eda16858a3cab07b80edaf74336ece1f986ba330fdb8ee0d6c0d68fe82bc96be", size = 794115, upload-time = "2025-09-25T21:32:31.353Z" },
    { url = "https://files.pythonhosted.org/packages/de/94/980b50a6531b3019e45ddeada0626d45fa85cbe22300844a7983285bed3b/pyyaml-6.0.3-cp313-cp313-win32.whl", hash = "sha256:d0eae10f8159e8fdad514efdc92d74fd8d682c933a6dd088030f3834bc8e6b26", size = 137427, upload-time = "2025-09-25T21:32:32.58Z" },
    { url = "https://files.pythonhosted.org/packages/97/c9/39d5b874e8b28845e4ec2202b5da735d0199dbe5b8fb85f91398814a9a46/pyyaml-6.0.3-cp313-cp313-win_amd64.whl", hash = "sha256:79005a0d97d5ddabfeeea4cf676af11e647e41d81c9a7722a193022accdb6b7c", size = 154090, upload-time = "2025-09-25T21:32:33.659Z" },
    { url = "https://files.pythonhosted.org/packages/73/e8/2bdf3ca2090f68bb3d75b44da7bbc71843b19c9f2b9cb9b0f4ab7a5a4329/pyyaml-6.0.3-cp313-cp313-win_arm64.whl", hash = "sha256:5498cd1645aa724a7c71c8f378eb29ebe23da2fc0d7a08071d89469bf1d2defb", size = 140246, upload-time = "2025-09-25T21:32:34.663Z" },
    { url = "https://files.pythonhosted.org/packages/9d/8c/f4bd7f6465179953d3ac9bc44ac1a8a3e6122cf8ada906b4f96c60172d43/pyyaml-6.0.3-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:8d1fab6bb153a416f9aeb4b8763bc0f22a5586065f86f7664fc23339fc1c1fac", size = 181814, upload-time = "2025-09-25T21:32:35.712Z" },
    { url = "https://files.pythonhosted.org/packages/bd/9c/4d95bb87eb2063d20db7b60faa3840c1b18025517ae857371c4dd55a6b3a/pyyaml-6.0.3-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:34d5fcd24b8445fadc33f9cf348c1047101756fd760b4dacb5c3e99755703310", size = 173809, upload-time = "2025-09-25T21:32:36.789Z" },
    { url = "https://files.pythonhosted.org/packages/92/b5/47e807c2623074914e29dabd16cbbdd4bf5e9b2db9f8090fa64411fc5382/pyyaml-6.0.3-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:501a031947e3a9025ed4405a168e6ef5ae3126c59f90ce0cd6f2bfc477be31b7", size = 766454, upload-time = "2025-09-25T21:32:37.966Z" },
    { url = "https://files.pythonhosted.org/packages/02/9e/e5e9b168be58564121efb3de6859c452fccde0ab093d8438905899a3a483/pyyaml-6.0.3-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:b3bc83488de33889877a0f2543ade9f70c67d66d9ebb4ac959502e12de895788", size = 836355, upload-time = "2025-09-25T21:32:39.178Z" },
    { url = "https://files.pythonhosted.org/packages/88/f9/16491d7ed2a919954993e48aa941b200f38040928474c9e85ea9e64222c3/pyyaml-6.0.3-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:c458b6d084f9b935061bc36216e8a69a7e293a2f1e68bf956dcd9e6cbcd143f5", size = 794175, upload-time = "2025-09-25T21:32:40.865Z" },
    { url = "https://files.pythonhosted.org/packages/dd/3f/5989debef34dc6397317802b527dbbafb2b4760878a53d4166579111411e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:7c6610def4f163542a622a73fb39f534f8c101d690126992300bf3207eab9764", size = 755228, upload-time = "2025-09-25T21:32:42.084Z" },
    { url = "https://files.pythonhosted.org/packages/d7/ce/af88a49043cd2e265be63d083fc75b27b6ed062f5f9fd6cdc223ad62f03e/pyyaml-6.0.3-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:5190d403f121660ce8d1d2c1bb2ef1bd05b5f68533fc5c2ea899bd15f4399b35", size = 789194, upload-time = "2025-09-25T21:32:43.362Z" },
    { url = "https://files.pythonhosted.org/packages/23/20/bb6982b26a40bb43951265ba29d4c246ef0ff59c9fdcdf0ed04e0687de4d/pyyaml-6.0.3-cp314-cp314-win_amd64.whl", hash = "sha256:4a2e8cebe2ff6ab7d1050ecd59c25d4c8bd7e6f400f5f82b96557ac0abafd0ac", size = 156429, upload-time = "2025-09-25T21:32:57.844Z" },
    { url = "https://files.pythonhosted.org/packages/f4/f4/a4541072bb9422c8a883ab55255f918fa378ecf083f5b85e87fc2b4eda1b/pyyaml-6.0.3-cp314-cp314-win_arm64.whl", hash = "sha256:93dda82c9c22deb0a405ea4dc5f2d0cda384168e466364dec6255b293923b2f3", size = 143912, upload-time = "2025-09-25T21:32:59.247Z" },
    { url = "https://files.pythonhosted.org/packages/7c/f9/07dd09ae774e4616edf6cda684ee78f97777bdd15847253637a6f052a62f/pyyaml-6.0.3-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:02893d100e99e03eda1c8fd5c441d8c60103fd175728e23e431db1b589cf5ab3", size = 189108, upload-time = "2025-09-25T21:32:44.377Z" },
    { url = "https://files.pythonhosted.org/packages/4e/78/8d08c9fb7ce09ad8c38ad533c1191cf27f7ae1effe5bb9400a46d9437fcf/pyyaml-6.0.3-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:c1ff362665ae507275af2853520967820d9124984e0f7466736aea23d8611fba", size = 183641, upload-time = "2025-09-25T21:32:45.407Z" },
    { url = "https://files.pythonhosted.org/packages/7b/5b/3babb19104a46945cf816d047db2788bcaf8c94527a805610b0289a01c6b/pyyaml-6.0.3-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:6adc77889b628398debc7b65c073bcb99c4a0237b248cacaf3fe8a557563ef6c", size = 831901, upload-time = "2025-09-25T21:32:48.83Z" },
    { url = "https://files.pythonhosted.org/packages/8b/cc/dff0684d8dc44da4d22a13f35f073d558c268780ce3c6ba1b87055bb0b87/pyyaml-6.0.3-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:a80cb027f6b349846a3bf6d73b5e95e782175e52f22108cfa17876aaeff93702", size = 861132, upload-time = "2025-09-25T21:32:50.149Z" },
    { url = "https://files.pythonhosted.org/packages/b1/5e/f77dc6b9036943e285ba76b49e118d9ea929885becb0a29ba8a7c75e29fe/pyyaml-6.0.3-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:00c4bdeba853cc34e7dd471f16b4114f4162dc03e6b7afcc2128711f0eca823c", size = 839261, upload-time = "2025-09-25T21:32:51.808Z" },
    { url = "https://files.pythonhosted.org/packages/ce/88/a9db1376aa2a228197c58b37302f284b5617f56a5d959fd1763fb1675ce6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:66e1674c3ef6f541c35191caae2d429b967b99e02040f5ba928632d9a7f0f065", size = 805272, upload-time = "2025-09-25T21:32:52.941Z" },
    { url = "https://files.pythonhosted.org/packages/da/92/1446574745d74df0c92e6aa4a7b0b3130706a4142b2d1a5869f2eaa423c6/pyyaml-6.0.3-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:16249ee61e95f858e83976573de0f5b2893b3677ba71c9dd36b9cf8be9ac6d65", size = 829923, upload-time = "2025-09-25T21:32:54.537Z" },
    { url = "https://files.pythonhosted.org/packages/f0/7a/1c7270340330e575b92f397352af856a8c06f230aa3e76f86b39d01b416a/pyyaml-6.0.3-cp314-cp314t-win_amd64.whl", hash = "sha256:4ad1906908f2f5ae4e5a8ddfce73c320c2a1429ec52eafd27138b7f1cbe341c9", size = 174062, upload-time = "2025-09-25T21:32:55.767Z" },
    { url = "https://files.pythonhosted.org/packages/f1/12/de94a39c2ef588c7e6455cfbe7343d3b2dc9d6b6b2f40c4c6565744c873d/pyyaml-6.0.3-cp314-cp314t-win_arm64.whl", hash = "sha256:ebc55a14a21cb14062aa4162f906cd962b28e2e9ea38f9b4391244cd8de4ae0b", size = 149341, upload-time = "2025-09-25T21:32:56.828Z" },
]

[[package]]
name = "requests"
version = "2.32.5"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "certifi" },
    { name = "charset-normalizer" },
    { name = "idna" },
    { name = "urllib3" },
]
sdist = { url = "https://files.pythonhosted.org/packages/c9/74/b3ff8e6c8446842c3f5c837e9c3dfcfe2018ea6ecef224c710c85ef728f4/requests-2.32.5.tar.gz", hash = "sha256:dbba0bac56e100853db0ea71b82b4dfd5fe2bf6d3754a8893c3af500cec7d7cf", size = 134517, upload-time = "2025-08-18T20:46:02.573Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/1e/db/4254e3eabe8020b458f1a747140d32277ec7a271daf1d235b70dc0b4e6e3/requests-2.32.5-py3-none-any.whl", hash = "sha256:2462f94637a34fd532264295e186976db0f5d453d1cdd31473c85a6a161affb6", size = 64738, upload-time = "2025-08-18T20:46:00.542Z" },
]

[[package]]
name = "requests-toolbelt"
version = "1.0.0"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "requests" },
]
sdist = { url = "https://files.pythonhosted.org/packages/f3/61/d7545dafb7ac2230c70d38d31cbfe4cc64f7144dc41f6e4e4b78ecd9f5bb/requests-toolbelt-1.0.0.tar.gz", hash = "sha256:7681a0a3d047012b5bdc0ee37d7f8f07ebe76ab08caeccfc3921ce23c88d5bc6", size = 206888, upload-time = "2023-05-01T04:11:33.229Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/3f/51/d4db610ef29373b879047326cbf6fa98b6c1969d6f6dc423279de2b1be2c/requests_toolbelt-1.0.0-py2.py3-none-any.whl", hash = "sha256:cccfdd665f0a24fcf4726e690f65639d272bb0637b9b92dfd91a5568ccf6bd06", size = 54481, upload-time = "2023-05-01T04:11:28.427Z" },
]

[[package]]
name = "sniffio"
version = "1.3.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/a2/87/a6771e1546d97e7e041b6ae58d80074f81b7d5121207425c964ddf5cfdbd/sniffio-1.3.1.tar.gz", hash = "sha256:f4324edc670a0f49750a81b895f35c3adb843cca46f0530f79fc1babb23789dc", size = 20372, upload-time = "2024-02-25T23:20:04.057Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/e9/44/75a9c9421471a6c4805dbf2356f7c181a29c1879239abab1ea2cc8f38b40/sniffio-1.3.1-py3-none-any.whl", hash = "sha256:2f6da418d1f1e0fddd844478f41680e794e6051915791a034ff65e5f100525a2", size = 10235, upload-time = "2024-02-25T23:20:01.196Z" },
]

[[package]]
name = "tenacity"
version = "9.1.4"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/47/c6/ee486fd809e357697ee8a44d3d69222b344920433d3b6666ccd9b374630c/tenacity-9.1.4.tar.gz", hash = "sha256:adb31d4c263f2bd041081ab33b498309a57c77f9acf2db65aadf0898179cf93a", size = 49413, upload-time = "2026-02-07T10:45:33.841Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/d7/c1/eb8f9debc45d3b7918a32ab756658a0904732f75e555402972246b0b8e71/tenacity-9.1.4-py3-none-any.whl", hash = "sha256:6095a360c919085f28c6527de529e76a06ad89b23659fa881ae0649b867a9d55", size = 28926, upload-time = "2026-02-07T10:45:32.24Z" },
]

[[package]]
name = "typing-extensions"
version = "4.15.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/72/94/1a15dd82efb362ac84269196e94cf00f187f7ed21c242792a923cdb1c61f/typing_extensions-4.15.0.tar.gz", hash = "sha256:0cea48d173cc12fa28ecabc3b837ea3cf6f38c6d1136f85cbaaf598984861466", size = 109391, upload-time = "2025-08-25T13:49:26.313Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/18/67/36e9267722cc04a6b9f15c7f3441c2363321a3ea07da7ae0c0707beb2a9c/typing_extensions-4.15.0-py3-none-any.whl", hash = "sha256:f0fa19c6845758ab08074a0cfa8b7aecb71c999ca73d62883bc25cc018c4e548", size = 44614, upload-time = "2025-08-25T13:49:24.86Z" },
]

[[package]]
name = "typing-inspection"
version = "0.4.2"
source = { registry = "https://pypi.org/simple" }
dependencies = [
    { name = "typing-extensions" },
]
sdist = { url = "https://files.pythonhosted.org/packages/55/e3/70399cb7dd41c10ac53367ae42139cf4b1ca5f36bb3dc6c9d33acdb43655/typing_inspection-0.4.2.tar.gz", hash = "sha256:ba561c48a67c5958007083d386c3295464928b01faa735ab8547c5692e87f464", size = 75949, upload-time = "2025-10-01T02:14:41.687Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/dc/9b/47798a6c91d8bdb567fe2698fe81e0c6b7cb7ef4d13da4114b41d239f65d/typing_inspection-0.4.2-py3-none-any.whl", hash = "sha256:4ed1cacbdc298c220f1bd249ed5287caa16f34d44ef4e9c3d0cbad5b521545e7", size = 14611, upload-time = "2025-10-01T02:14:40.154Z" },
]

[[package]]
name = "urllib3"
version = "2.6.3"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/c7/24/5f1b3bdffd70275f6661c76461e25f024d5a38a46f04aaca912426a2b1d3/urllib3-2.6.3.tar.gz", hash = "sha256:1b62b6884944a57dbe321509ab94fd4d3b307075e0c2eae991ac71ee15ad38ed", size = 435556, upload-time = "2026-01-07T16:24:43.925Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/39/08/aaaad47bc4e9dc8c725e68f9d04865dbcb2052843ff09c97b08904852d84/urllib3-2.6.3-py3-none-any.whl", hash = "sha256:bf272323e553dfb2e87d9bfd225ca7b0f467b919d7bbd355436d3fd37cb0acd4", size = 131584, upload-time = "2026-01-07T16:24:42.685Z" },
]

[[package]]
name = "uuid-utils"
version = "0.14.1"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/7b/d1/38a573f0c631c062cf42fa1f5d021d4dd3c31fb23e4376e4b56b0c9fbbed/uuid_utils-0.14.1.tar.gz", hash = "sha256:9bfc95f64af80ccf129c604fb6b8ca66c6f256451e32bc4570f760e4309c9b69", size = 22195, upload-time = "2026-02-20T22:50:38.833Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/43/b7/add4363039a34506a58457d96d4aa2126061df3a143eb4d042aedd6a2e76/uuid_utils-0.14.1-cp39-abi3-macosx_10_12_x86_64.macosx_11_0_arm64.macosx_10_12_universal2.whl", hash = "sha256:93a3b5dc798a54a1feb693f2d1cb4cf08258c32ff05ae4929b5f0a2ca624a4f0", size = 604679, upload-time = "2026-02-20T22:50:27.469Z" },
    { url = "https://files.pythonhosted.org/packages/dd/84/d1d0bef50d9e66d31b2019997c741b42274d53dde2e001b7a83e9511c339/uuid_utils-0.14.1-cp39-abi3-macosx_10_12_x86_64.whl", hash = "sha256:ccd65a4b8e83af23eae5e56d88034b2fe7264f465d3e830845f10d1591b81741", size = 309346, upload-time = "2026-02-20T22:50:31.857Z" },
    { url = "https://files.pythonhosted.org/packages/ef/ed/b6d6fd52a6636d7c3eddf97d68da50910bf17cd5ac221992506fb56cf12e/uuid_utils-0.14.1-cp39-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b56b0cacd81583834820588378e432b0696186683b813058b707aedc1e16c4b1", size = 344714, upload-time = "2026-02-20T22:50:42.642Z" },
    { url = "https://files.pythonhosted.org/packages/a8/a7/a19a1719fb626fe0b31882db36056d44fe904dc0cf15b06fdf56b2679cf7/uuid_utils-0.14.1-cp39-abi3-manylinux_2_17_armv7l.manylinux2014_armv7l.whl", hash = "sha256:bb3cf14de789097320a3c56bfdfdd51b1225d11d67298afbedee7e84e3837c96", size = 350914, upload-time = "2026-02-20T22:50:36.487Z" },
    { url = "https://files.pythonhosted.org/packages/1d/fc/f6690e667fdc3bb1a73f57951f97497771c56fe23e3d302d7404be394d4f/uuid_utils-0.14.1-cp39-abi3-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:60e0854a90d67f4b0cc6e54773deb8be618f4c9bad98d3326f081423b5d14fae", size = 482609, upload-time = "2026-02-20T22:50:37.511Z" },
    { url = "https://files.pythonhosted.org/packages/54/6e/dcd3fa031320921a12ec7b4672dea3bd1dd90ddffa363a91831ba834d559/uuid_utils-0.14.1-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:ce6743ba194de3910b5feb1a62590cd2587e33a73ab6af8a01b642ceb5055862", size = 345699, upload-time = "2026-02-20T22:50:46.87Z" },
    { url = "https://files.pythonhosted.org/packages/04/28/e5220204b58b44ac0047226a9d016a113fde039280cc8732d9e6da43b39f/uuid_utils-0.14.1-cp39-abi3-manylinux_2_5_i686.manylinux1_i686.whl", hash = "sha256:043fb58fde6cf1620a6c066382f04f87a8e74feb0f95a585e4ed46f5d44af57b", size = 372205, upload-time = "2026-02-20T22:50:28.438Z" },
    { url = "https://files.pythonhosted.org/packages/c7/d9/3d2eb98af94b8dfffc82b6a33b4dfc87b0a5de2c68a28f6dde0db1f8681b/uuid_utils-0.14.1-cp39-abi3-musllinux_1_2_aarch64.whl", hash = "sha256:c915d53f22945e55fe0d3d3b0b87fd965a57f5fd15666fd92d6593a73b1dd297", size = 521836, upload-time = "2026-02-20T22:50:23.057Z" },
    { url = "https://files.pythonhosted.org/packages/a8/15/0eb106cc6fe182f7577bc0ab6e2f0a40be247f35c5e297dbf7bbc460bd02/uuid_utils-0.14.1-cp39-abi3-musllinux_1_2_armv7l.whl", hash = "sha256:0972488e3f9b449e83f006ead5a0e0a33ad4a13e4462e865b7c286ab7d7566a3", size = 625260, upload-time = "2026-02-20T22:50:25.949Z" },
    { url = "https://files.pythonhosted.org/packages/3c/17/f539507091334b109e7496830af2f093d9fc8082411eafd3ece58af1f8ba/uuid_utils-0.14.1-cp39-abi3-musllinux_1_2_i686.whl", hash = "sha256:1c238812ae0c8ffe77d8d447a32c6dfd058ea4631246b08b5a71df586ff08531", size = 587824, upload-time = "2026-02-20T22:50:35.225Z" },
    { url = "https://files.pythonhosted.org/packages/2e/c2/d37a7b2e41f153519367d4db01f0526e0d4b06f1a4a87f1c5dfca5d70a8b/uuid_utils-0.14.1-cp39-abi3-musllinux_1_2_x86_64.whl", hash = "sha256:bec8f8ef627af86abf8298e7ec50926627e29b34fa907fcfbedb45aaa72bca43", size = 551407, upload-time = "2026-02-20T22:50:44.915Z" },
    { url = "https://files.pythonhosted.org/packages/65/36/2d24b2cbe78547c6532da33fb8613debd3126eccc33a6374ab788f5e46e9/uuid_utils-0.14.1-cp39-abi3-win32.whl", hash = "sha256:b54d6aa6252d96bac1fdbc80d26ba71bad9f220b2724d692ad2f2310c22ef523", size = 183476, upload-time = "2026-02-20T22:50:32.745Z" },
    { url = "https://files.pythonhosted.org/packages/83/92/2d7e90df8b1a69ec4cff33243ce02b7a62f926ef9e2f0eca5a026889cd73/uuid_utils-0.14.1-cp39-abi3-win_amd64.whl", hash = "sha256:fc27638c2ce267a0ce3e06828aff786f91367f093c80625ee21dad0208e0f5ba", size = 187147, upload-time = "2026-02-20T22:50:45.807Z" },
    { url = "https://files.pythonhosted.org/packages/d9/26/529f4beee17e5248e37e0bc17a2761d34c0fa3b1e5729c88adb2065bae6e/uuid_utils-0.14.1-cp39-abi3-win_arm64.whl", hash = "sha256:b04cb49b42afbc4ff8dbc60cf054930afc479d6f4dd7f1ec3bbe5dbfdde06b7a", size = 188132, upload-time = "2026-02-20T22:50:41.718Z" },
]

[[package]]
name = "xxhash"
version = "3.6.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/02/84/30869e01909fb37a6cc7e18688ee8bf1e42d57e7e0777636bd47524c43c7/xxhash-3.6.0.tar.gz", hash = "sha256:f0162a78b13a0d7617b2845b90c763339d1f1d82bb04a4b07f4ab535cc5e05d6", size = 85160, upload-time = "2025-10-02T14:37:08.097Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/33/76/35d05267ac82f53ae9b0e554da7c5e281ee61f3cad44c743f0fcd354f211/xxhash-3.6.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:599e64ba7f67472481ceb6ee80fa3bd828fd61ba59fb11475572cc5ee52b89ec", size = 32738, upload-time = "2025-10-02T14:34:55.839Z" },
    { url = "https://files.pythonhosted.org/packages/31/a8/3fbce1cd96534a95e35d5120637bf29b0d7f5d8fa2f6374e31b4156dd419/xxhash-3.6.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:7d8b8aaa30fca4f16f0c84a5c8d7ddee0e25250ec2796c973775373257dde8f1", size = 30821, upload-time = "2025-10-02T14:34:57.219Z" },
    { url = "https://files.pythonhosted.org/packages/0c/ea/d387530ca7ecfa183cb358027f1833297c6ac6098223fd14f9782cd0015c/xxhash-3.6.0-cp313-cp313-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:d597acf8506d6e7101a4a44a5e428977a51c0fadbbfd3c39650cca9253f6e5a6", size = 194127, upload-time = "2025-10-02T14:34:59.21Z" },
    { url = "https://files.pythonhosted.org/packages/ba/0c/71435dcb99874b09a43b8d7c54071e600a7481e42b3e3ce1eb5226a5711a/xxhash-3.6.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:858dc935963a33bc33490128edc1c12b0c14d9c7ebaa4e387a7869ecc4f3e263", size = 212975, upload-time = "2025-10-02T14:35:00.816Z" },
    { url = "https://files.pythonhosted.org/packages/84/7a/c2b3d071e4bb4a90b7057228a99b10d51744878f4a8a6dd643c8bd897620/xxhash-3.6.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:ba284920194615cb8edf73bf52236ce2e1664ccd4a38fdb543506413529cc546", size = 212241, upload-time = "2025-10-02T14:35:02.207Z" },
    { url = "https://files.pythonhosted.org/packages/81/5f/640b6eac0128e215f177df99eadcd0f1b7c42c274ab6a394a05059694c5a/xxhash-3.6.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:4b54219177f6c6674d5378bd862c6aedf64725f70dd29c472eaae154df1a2e89", size = 445471, upload-time = "2025-10-02T14:35:03.61Z" },
    { url = "https://files.pythonhosted.org/packages/5e/1e/3c3d3ef071b051cc3abbe3721ffb8365033a172613c04af2da89d5548a87/xxhash-3.6.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:42c36dd7dbad2f5238950c377fcbf6811b1cdb1c444fab447960030cea60504d", size = 193936, upload-time = "2025-10-02T14:35:05.013Z" },
    { url = "https://files.pythonhosted.org/packages/2c/bd/4a5f68381939219abfe1c22a9e3a5854a4f6f6f3c4983a87d255f21f2e5d/xxhash-3.6.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:f22927652cba98c44639ffdc7aaf35828dccf679b10b31c4ad72a5b530a18eb7", size = 210440, upload-time = "2025-10-02T14:35:06.239Z" },
    { url = "https://files.pythonhosted.org/packages/eb/37/b80fe3d5cfb9faff01a02121a0f4d565eb7237e9e5fc66e73017e74dcd36/xxhash-3.6.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:b45fad44d9c5c119e9c6fbf2e1c656a46dc68e280275007bbfd3d572b21426db", size = 197990, upload-time = "2025-10-02T14:35:07.735Z" },
    { url = "https://files.pythonhosted.org/packages/d7/fd/2c0a00c97b9e18f72e1f240ad4e8f8a90fd9d408289ba9c7c495ed7dc05c/xxhash-3.6.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:6f2580ffab1a8b68ef2b901cde7e55fa8da5e4be0977c68f78fc80f3c143de42", size = 210689, upload-time = "2025-10-02T14:35:09.438Z" },
    { url = "https://files.pythonhosted.org/packages/93/86/5dd8076a926b9a95db3206aba20d89a7fc14dd5aac16e5c4de4b56033140/xxhash-3.6.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:40c391dd3cd041ebc3ffe6f2c862f402e306eb571422e0aa918d8070ba31da11", size = 414068, upload-time = "2025-10-02T14:35:11.162Z" },
    { url = "https://files.pythonhosted.org/packages/af/3c/0bb129170ee8f3650f08e993baee550a09593462a5cddd8e44d0011102b1/xxhash-3.6.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:f205badabde7aafd1a31e8ca2a3e5a763107a71c397c4481d6a804eb5063d8bd", size = 191495, upload-time = "2025-10-02T14:35:12.971Z" },
    { url = "https://files.pythonhosted.org/packages/e9/3a/6797e0114c21d1725e2577508e24006fd7ff1d8c0c502d3b52e45c1771d8/xxhash-3.6.0-cp313-cp313-win32.whl", hash = "sha256:2577b276e060b73b73a53042ea5bd5203d3e6347ce0d09f98500f418a9fcf799", size = 30620, upload-time = "2025-10-02T14:35:14.129Z" },
    { url = "https://files.pythonhosted.org/packages/86/15/9bc32671e9a38b413a76d24722a2bf8784a132c043063a8f5152d390b0f9/xxhash-3.6.0-cp313-cp313-win_amd64.whl", hash = "sha256:757320d45d2fbcce8f30c42a6b2f47862967aea7bf458b9625b4bbe7ee390392", size = 31542, upload-time = "2025-10-02T14:35:15.21Z" },
    { url = "https://files.pythonhosted.org/packages/39/c5/cc01e4f6188656e56112d6a8e0dfe298a16934b8c47a247236549a3f7695/xxhash-3.6.0-cp313-cp313-win_arm64.whl", hash = "sha256:457b8f85dec5825eed7b69c11ae86834a018b8e3df5e77783c999663da2f96d6", size = 27880, upload-time = "2025-10-02T14:35:16.315Z" },
    { url = "https://files.pythonhosted.org/packages/f3/30/25e5321c8732759e930c555176d37e24ab84365482d257c3b16362235212/xxhash-3.6.0-cp313-cp313t-macosx_10_13_x86_64.whl", hash = "sha256:a42e633d75cdad6d625434e3468126c73f13f7584545a9cf34e883aa1710e702", size = 32956, upload-time = "2025-10-02T14:35:17.413Z" },
    { url = "https://files.pythonhosted.org/packages/9f/3c/0573299560d7d9f8ab1838f1efc021a280b5ae5ae2e849034ef3dee18810/xxhash-3.6.0-cp313-cp313t-macosx_11_0_arm64.whl", hash = "sha256:568a6d743219e717b07b4e03b0a828ce593833e498c3b64752e0f5df6bfe84db", size = 31072, upload-time = "2025-10-02T14:35:18.844Z" },
    { url = "https://files.pythonhosted.org/packages/7a/1c/52d83a06e417cd9d4137722693424885cc9878249beb3a7c829e74bf7ce9/xxhash-3.6.0-cp313-cp313t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:bec91b562d8012dae276af8025a55811b875baace6af510412a5e58e3121bc54", size = 196409, upload-time = "2025-10-02T14:35:20.31Z" },
    { url = "https://files.pythonhosted.org/packages/e3/8e/c6d158d12a79bbd0b878f8355432075fc82759e356ab5a111463422a239b/xxhash-3.6.0-cp313-cp313t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:78e7f2f4c521c30ad5e786fdd6bae89d47a32672a80195467b5de0480aa97b1f", size = 215736, upload-time = "2025-10-02T14:35:21.616Z" },
    { url = "https://files.pythonhosted.org/packages/bc/68/c4c80614716345d55071a396cf03d06e34b5f4917a467faf43083c995155/xxhash-3.6.0-cp313-cp313t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:3ed0df1b11a79856df5ffcab572cbd6b9627034c1c748c5566fa79df9048a7c5", size = 214833, upload-time = "2025-10-02T14:35:23.32Z" },
    { url = "https://files.pythonhosted.org/packages/7e/e9/ae27c8ffec8b953efa84c7c4a6c6802c263d587b9fc0d6e7cea64e08c3af/xxhash-3.6.0-cp313-cp313t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:0e4edbfc7d420925b0dd5e792478ed393d6e75ff8fc219a6546fb446b6a417b1", size = 448348, upload-time = "2025-10-02T14:35:25.111Z" },
    { url = "https://files.pythonhosted.org/packages/d7/6b/33e21afb1b5b3f46b74b6bd1913639066af218d704cc0941404ca717fc57/xxhash-3.6.0-cp313-cp313t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:fba27a198363a7ef87f8c0f6b171ec36b674fe9053742c58dd7e3201c1ab30ee", size = 196070, upload-time = "2025-10-02T14:35:26.586Z" },
    { url = "https://files.pythonhosted.org/packages/96/b6/fcabd337bc5fa624e7203aa0fa7d0c49eed22f72e93229431752bddc83d9/xxhash-3.6.0-cp313-cp313t-musllinux_1_2_aarch64.whl", hash = "sha256:794fe9145fe60191c6532fa95063765529770edcdd67b3d537793e8004cabbfd", size = 212907, upload-time = "2025-10-02T14:35:28.087Z" },
    { url = "https://files.pythonhosted.org/packages/4b/d3/9ee6160e644d660fcf176c5825e61411c7f62648728f69c79ba237250143/xxhash-3.6.0-cp313-cp313t-musllinux_1_2_i686.whl", hash = "sha256:6105ef7e62b5ac73a837778efc331a591d8442f8ef5c7e102376506cb4ae2729", size = 200839, upload-time = "2025-10-02T14:35:29.857Z" },
    { url = "https://files.pythonhosted.org/packages/0d/98/e8de5baa5109394baf5118f5e72ab21a86387c4f89b0e77ef3e2f6b0327b/xxhash-3.6.0-cp313-cp313t-musllinux_1_2_ppc64le.whl", hash = "sha256:f01375c0e55395b814a679b3eea205db7919ac2af213f4a6682e01220e5fe292", size = 213304, upload-time = "2025-10-02T14:35:31.222Z" },
    { url = "https://files.pythonhosted.org/packages/7b/1d/71056535dec5c3177eeb53e38e3d367dd1d16e024e63b1cee208d572a033/xxhash-3.6.0-cp313-cp313t-musllinux_1_2_s390x.whl", hash = "sha256:d706dca2d24d834a4661619dcacf51a75c16d65985718d6a7d73c1eeeb903ddf", size = 416930, upload-time = "2025-10-02T14:35:32.517Z" },
    { url = "https://files.pythonhosted.org/packages/dc/6c/5cbde9de2cd967c322e651c65c543700b19e7ae3e0aae8ece3469bf9683d/xxhash-3.6.0-cp313-cp313t-musllinux_1_2_x86_64.whl", hash = "sha256:5f059d9faeacd49c0215d66f4056e1326c80503f51a1532ca336a385edadd033", size = 193787, upload-time = "2025-10-02T14:35:33.827Z" },
    { url = "https://files.pythonhosted.org/packages/19/fa/0172e350361d61febcea941b0cc541d6e6c8d65d153e85f850a7b256ff8a/xxhash-3.6.0-cp313-cp313t-win32.whl", hash = "sha256:1244460adc3a9be84731d72b8e80625788e5815b68da3da8b83f78115a40a7ec", size = 30916, upload-time = "2025-10-02T14:35:35.107Z" },
    { url = "https://files.pythonhosted.org/packages/ad/e6/e8cf858a2b19d6d45820f072eff1bea413910592ff17157cabc5f1227a16/xxhash-3.6.0-cp313-cp313t-win_amd64.whl", hash = "sha256:b1e420ef35c503869c4064f4a2f2b08ad6431ab7b229a05cce39d74268bca6b8", size = 31799, upload-time = "2025-10-02T14:35:36.165Z" },
    { url = "https://files.pythonhosted.org/packages/56/15/064b197e855bfb7b343210e82490ae672f8bc7cdf3ddb02e92f64304ee8a/xxhash-3.6.0-cp313-cp313t-win_arm64.whl", hash = "sha256:ec44b73a4220623235f67a996c862049f375df3b1052d9899f40a6382c32d746", size = 28044, upload-time = "2025-10-02T14:35:37.195Z" },
    { url = "https://files.pythonhosted.org/packages/7e/5e/0138bc4484ea9b897864d59fce9be9086030825bc778b76cb5a33a906d37/xxhash-3.6.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:a40a3d35b204b7cc7643cbcf8c9976d818cb47befcfac8bbefec8038ac363f3e", size = 32754, upload-time = "2025-10-02T14:35:38.245Z" },
    { url = "https://files.pythonhosted.org/packages/18/d7/5dac2eb2ec75fd771957a13e5dda560efb2176d5203f39502a5fc571f899/xxhash-3.6.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:a54844be970d3fc22630b32d515e79a90d0a3ddb2644d8d7402e3c4c8da61405", size = 30846, upload-time = "2025-10-02T14:35:39.6Z" },
    { url = "https://files.pythonhosted.org/packages/fe/71/8bc5be2bb00deb5682e92e8da955ebe5fa982da13a69da5a40a4c8db12fb/xxhash-3.6.0-cp314-cp314-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:016e9190af8f0a4e3741343777710e3d5717427f175adfdc3e72508f59e2a7f3", size = 194343, upload-time = "2025-10-02T14:35:40.69Z" },
    { url = "https://files.pythonhosted.org/packages/e7/3b/52badfb2aecec2c377ddf1ae75f55db3ba2d321c5e164f14461c90837ef3/xxhash-3.6.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:4f6f72232f849eb9d0141e2ebe2677ece15adfd0fa599bc058aad83c714bb2c6", size = 213074, upload-time = "2025-10-02T14:35:42.29Z" },
    { url = "https://files.pythonhosted.org/packages/a2/2b/ae46b4e9b92e537fa30d03dbc19cdae57ed407e9c26d163895e968e3de85/xxhash-3.6.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:63275a8aba7865e44b1813d2177e0f5ea7eadad3dd063a21f7cf9afdc7054063", size = 212388, upload-time = "2025-10-02T14:35:43.929Z" },
    { url = "https://files.pythonhosted.org/packages/f5/80/49f88d3afc724b4ac7fbd664c8452d6db51b49915be48c6982659e0e7942/xxhash-3.6.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:3cd01fa2aa00d8b017c97eb46b9a794fbdca53fc14f845f5a328c71254b0abb7", size = 445614, upload-time = "2025-10-02T14:35:45.216Z" },
    { url = "https://files.pythonhosted.org/packages/ed/ba/603ce3961e339413543d8cd44f21f2c80e2a7c5cfe692a7b1f2cccf58f3c/xxhash-3.6.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:0226aa89035b62b6a86d3c68df4d7c1f47a342b8683da2b60cedcddb46c4d95b", size = 194024, upload-time = "2025-10-02T14:35:46.959Z" },
    { url = "https://files.pythonhosted.org/packages/78/d1/8e225ff7113bf81545cfdcd79eef124a7b7064a0bba53605ff39590b95c2/xxhash-3.6.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:c6e193e9f56e4ca4923c61238cdaced324f0feac782544eb4c6d55ad5cc99ddd", size = 210541, upload-time = "2025-10-02T14:35:48.301Z" },
    { url = "https://files.pythonhosted.org/packages/6f/58/0f89d149f0bad89def1a8dd38feb50ccdeb643d9797ec84707091d4cb494/xxhash-3.6.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:9176dcaddf4ca963d4deb93866d739a343c01c969231dbe21680e13a5d1a5bf0", size = 198305, upload-time = "2025-10-02T14:35:49.584Z" },
    { url = "https://files.pythonhosted.org/packages/11/38/5eab81580703c4df93feb5f32ff8fa7fe1e2c51c1f183ee4e48d4bb9d3d7/xxhash-3.6.0-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:c1ce4009c97a752e682b897aa99aef84191077a9433eb237774689f14f8ec152", size = 210848, upload-time = "2025-10-02T14:35:50.877Z" },
    { url = "https://files.pythonhosted.org/packages/5e/6b/953dc4b05c3ce678abca756416e4c130d2382f877a9c30a20d08ee6a77c0/xxhash-3.6.0-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:8cb2f4f679b01513b7adbb9b1b2f0f9cdc31b70007eaf9d59d0878809f385b11", size = 414142, upload-time = "2025-10-02T14:35:52.15Z" },
    { url = "https://files.pythonhosted.org/packages/08/a9/238ec0d4e81a10eb5026d4a6972677cbc898ba6c8b9dbaec12ae001b1b35/xxhash-3.6.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:653a91d7c2ab54a92c19ccf43508b6a555440b9be1bc8be553376778be7f20b5", size = 191547, upload-time = "2025-10-02T14:35:53.547Z" },
    { url = "https://files.pythonhosted.org/packages/f1/ee/3cf8589e06c2164ac77c3bf0aa127012801128f1feebf2a079272da5737c/xxhash-3.6.0-cp314-cp314-win32.whl", hash = "sha256:a756fe893389483ee8c394d06b5ab765d96e68fbbfe6fde7aa17e11f5720559f", size = 31214, upload-time = "2025-10-02T14:35:54.746Z" },
    { url = "https://files.pythonhosted.org/packages/02/5d/a19552fbc6ad4cb54ff953c3908bbc095f4a921bc569433d791f755186f1/xxhash-3.6.0-cp314-cp314-win_amd64.whl", hash = "sha256:39be8e4e142550ef69629c9cd71b88c90e9a5db703fecbcf265546d9536ca4ad", size = 32290, upload-time = "2025-10-02T14:35:55.791Z" },
    { url = "https://files.pythonhosted.org/packages/b1/11/dafa0643bc30442c887b55baf8e73353a344ee89c1901b5a5c54a6c17d39/xxhash-3.6.0-cp314-cp314-win_arm64.whl", hash = "sha256:25915e6000338999236f1eb68a02a32c3275ac338628a7eaa5a269c401995679", size = 28795, upload-time = "2025-10-02T14:35:57.162Z" },
    { url = "https://files.pythonhosted.org/packages/2c/db/0e99732ed7f64182aef4a6fb145e1a295558deec2a746265dcdec12d191e/xxhash-3.6.0-cp314-cp314t-macosx_10_13_x86_64.whl", hash = "sha256:c5294f596a9017ca5a3e3f8884c00b91ab2ad2933cf288f4923c3fd4346cf3d4", size = 32955, upload-time = "2025-10-02T14:35:58.267Z" },
    { url = "https://files.pythonhosted.org/packages/55/f4/2a7c3c68e564a099becfa44bb3d398810cc0ff6749b0d3cb8ccb93f23c14/xxhash-3.6.0-cp314-cp314t-macosx_11_0_arm64.whl", hash = "sha256:1cf9dcc4ab9cff01dfbba78544297a3a01dafd60f3bde4e2bfd016cf7e4ddc67", size = 31072, upload-time = "2025-10-02T14:35:59.382Z" },
    { url = "https://files.pythonhosted.org/packages/c6/d9/72a29cddc7250e8a5819dad5d466facb5dc4c802ce120645630149127e73/xxhash-3.6.0-cp314-cp314t-manylinux1_i686.manylinux_2_28_i686.manylinux_2_5_i686.whl", hash = "sha256:01262da8798422d0685f7cef03b2bd3f4f46511b02830861df548d7def4402ad", size = 196579, upload-time = "2025-10-02T14:36:00.838Z" },
    { url = "https://files.pythonhosted.org/packages/63/93/b21590e1e381040e2ca305a884d89e1c345b347404f7780f07f2cdd47ef4/xxhash-3.6.0-cp314-cp314t-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:51a73fb7cb3a3ead9f7a8b583ffd9b8038e277cdb8cb87cf890e88b3456afa0b", size = 215854, upload-time = "2025-10-02T14:36:02.207Z" },
    { url = "https://files.pythonhosted.org/packages/ce/b8/edab8a7d4fa14e924b29be877d54155dcbd8b80be85ea00d2be3413a9ed4/xxhash-3.6.0-cp314-cp314t-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:b9c6df83594f7df8f7f708ce5ebeacfc69f72c9fbaaababf6cf4758eaada0c9b", size = 214965, upload-time = "2025-10-02T14:36:03.507Z" },
    { url = "https://files.pythonhosted.org/packages/27/67/dfa980ac7f0d509d54ea0d5a486d2bb4b80c3f1bb22b66e6a05d3efaf6c0/xxhash-3.6.0-cp314-cp314t-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:627f0af069b0ea56f312fd5189001c24578868643203bca1abbc2c52d3a6f3ca", size = 448484, upload-time = "2025-10-02T14:36:04.828Z" },
    { url = "https://files.pythonhosted.org/packages/8c/63/8ffc2cc97e811c0ca5d00ab36604b3ea6f4254f20b7bc658ca825ce6c954/xxhash-3.6.0-cp314-cp314t-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:aa912c62f842dfd013c5f21a642c9c10cd9f4c4e943e0af83618b4a404d9091a", size = 196162, upload-time = "2025-10-02T14:36:06.182Z" },
    { url = "https://files.pythonhosted.org/packages/4b/77/07f0e7a3edd11a6097e990f6e5b815b6592459cb16dae990d967693e6ea9/xxhash-3.6.0-cp314-cp314t-musllinux_1_2_aarch64.whl", hash = "sha256:b465afd7909db30168ab62afe40b2fcf79eedc0b89a6c0ab3123515dc0df8b99", size = 213007, upload-time = "2025-10-02T14:36:07.733Z" },
    { url = "https://files.pythonhosted.org/packages/ae/d8/bc5fa0d152837117eb0bef6f83f956c509332ce133c91c63ce07ee7c4873/xxhash-3.6.0-cp314-cp314t-musllinux_1_2_i686.whl", hash = "sha256:a881851cf38b0a70e7c4d3ce81fc7afd86fbc2a024f4cfb2a97cf49ce04b75d3", size = 200956, upload-time = "2025-10-02T14:36:09.106Z" },
    { url = "https://files.pythonhosted.org/packages/26/a5/d749334130de9411783873e9b98ecc46688dad5db64ca6e04b02acc8b473/xxhash-3.6.0-cp314-cp314t-musllinux_1_2_ppc64le.whl", hash = "sha256:9b3222c686a919a0f3253cfc12bb118b8b103506612253b5baeaac10d8027cf6", size = 213401, upload-time = "2025-10-02T14:36:10.585Z" },
    { url = "https://files.pythonhosted.org/packages/89/72/abed959c956a4bfc72b58c0384bb7940663c678127538634d896b1195c10/xxhash-3.6.0-cp314-cp314t-musllinux_1_2_s390x.whl", hash = "sha256:c5aa639bc113e9286137cec8fadc20e9cd732b2cc385c0b7fa673b84fc1f2a93", size = 417083, upload-time = "2025-10-02T14:36:12.276Z" },
    { url = "https://files.pythonhosted.org/packages/0c/b3/62fd2b586283b7d7d665fb98e266decadf31f058f1cf6c478741f68af0cb/xxhash-3.6.0-cp314-cp314t-musllinux_1_2_x86_64.whl", hash = "sha256:5c1343d49ac102799905e115aee590183c3921d475356cb24b4de29a4bc56518", size = 193913, upload-time = "2025-10-02T14:36:14.025Z" },
    { url = "https://files.pythonhosted.org/packages/9a/9a/c19c42c5b3f5a4aad748a6d5b4f23df3bed7ee5445accc65a0fb3ff03953/xxhash-3.6.0-cp314-cp314t-win32.whl", hash = "sha256:5851f033c3030dd95c086b4a36a2683c2ff4a799b23af60977188b057e467119", size = 31586, upload-time = "2025-10-02T14:36:15.603Z" },
    { url = "https://files.pythonhosted.org/packages/03/d6/4cc450345be9924fd5dc8c590ceda1db5b43a0a889587b0ae81a95511360/xxhash-3.6.0-cp314-cp314t-win_amd64.whl", hash = "sha256:0444e7967dac37569052d2409b00a8860c2135cff05502df4da80267d384849f", size = 32526, upload-time = "2025-10-02T14:36:16.708Z" },
    { url = "https://files.pythonhosted.org/packages/0f/c9/7243eb3f9eaabd1a88a5a5acadf06df2d83b100c62684b7425c6a11bcaa8/xxhash-3.6.0-cp314-cp314t-win_arm64.whl", hash = "sha256:bb79b1e63f6fd84ec778a4b1916dfe0a7c3fdb986c06addd5db3a0d413819d95", size = 28898, upload-time = "2025-10-02T14:36:17.843Z" },
]

[[package]]
name = "zstandard"
version = "0.25.0"
source = { registry = "https://pypi.org/simple" }
sdist = { url = "https://files.pythonhosted.org/packages/fd/aa/3e0508d5a5dd96529cdc5a97011299056e14c6505b678fd58938792794b1/zstandard-0.25.0.tar.gz", hash = "sha256:7713e1179d162cf5c7906da876ec2ccb9c3a9dcbdffef0cc7f70c3667a205f0b", size = 711513, upload-time = "2025-09-14T22:15:54.002Z" }
wheels = [
    { url = "https://files.pythonhosted.org/packages/35/0b/8df9c4ad06af91d39e94fa96cc010a24ac4ef1378d3efab9223cc8593d40/zstandard-0.25.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:ec996f12524f88e151c339688c3897194821d7f03081ab35d31d1e12ec975e94", size = 795735, upload-time = "2025-09-14T22:17:26.042Z" },
    { url = "https://files.pythonhosted.org/packages/3f/06/9ae96a3e5dcfd119377ba33d4c42a7d89da1efabd5cb3e366b156c45ff4d/zstandard-0.25.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:a1a4ae2dec3993a32247995bdfe367fc3266da832d82f8438c8570f989753de1", size = 640440, upload-time = "2025-09-14T22:17:27.366Z" },
    { url = "https://files.pythonhosted.org/packages/d9/14/933d27204c2bd404229c69f445862454dcc101cd69ef8c6068f15aaec12c/zstandard-0.25.0-cp313-cp313-manylinux2010_i686.manylinux2014_i686.manylinux_2_12_i686.manylinux_2_17_i686.whl", hash = "sha256:e96594a5537722fdfb79951672a2a63aec5ebfb823e7560586f7484819f2a08f", size = 5343070, upload-time = "2025-09-14T22:17:28.896Z" },
    { url = "https://files.pythonhosted.org/packages/6d/db/ddb11011826ed7db9d0e485d13df79b58586bfdec56e5c84a928a9a78c1c/zstandard-0.25.0-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.whl", hash = "sha256:bfc4e20784722098822e3eee42b8e576b379ed72cca4a7cb856ae733e62192ea", size = 5063001, upload-time = "2025-09-14T22:17:31.044Z" },
    { url = "https://files.pythonhosted.org/packages/db/00/87466ea3f99599d02a5238498b87bf84a6348290c19571051839ca943777/zstandard-0.25.0-cp313-cp313-manylinux2014_ppc64le.manylinux_2_17_ppc64le.whl", hash = "sha256:457ed498fc58cdc12fc48f7950e02740d4f7ae9493dd4ab2168a47c93c31298e", size = 5394120, upload-time = "2025-09-14T22:17:32.711Z" },
    { url = "https://files.pythonhosted.org/packages/2b/95/fc5531d9c618a679a20ff6c29e2b3ef1d1f4ad66c5e161ae6ff847d102a9/zstandard-0.25.0-cp313-cp313-manylinux2014_s390x.manylinux_2_17_s390x.whl", hash = "sha256:fd7a5004eb1980d3cefe26b2685bcb0b17989901a70a1040d1ac86f1d898c551", size = 5451230, upload-time = "2025-09-14T22:17:34.41Z" },
    { url = "https://files.pythonhosted.org/packages/63/4b/e3678b4e776db00f9f7b2fe58e547e8928ef32727d7a1ff01dea010f3f13/zstandard-0.25.0-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl", hash = "sha256:8e735494da3db08694d26480f1493ad2cf86e99bdd53e8e9771b2752a5c0246a", size = 5547173, upload-time = "2025-09-14T22:17:36.084Z" },
    { url = "https://files.pythonhosted.org/packages/4e/d5/ba05ed95c6b8ec30bd468dfeab20589f2cf709b5c940483e31d991f2ca58/zstandard-0.25.0-cp313-cp313-musllinux_1_1_aarch64.whl", hash = "sha256:3a39c94ad7866160a4a46d772e43311a743c316942037671beb264e395bdd611", size = 5046736, upload-time = "2025-09-14T22:17:37.891Z" },
    { url = "https://files.pythonhosted.org/packages/50/d5/870aa06b3a76c73eced65c044b92286a3c4e00554005ff51962deef28e28/zstandard-0.25.0-cp313-cp313-musllinux_1_1_x86_64.whl", hash = "sha256:172de1f06947577d3a3005416977cce6168f2261284c02080e7ad0185faeced3", size = 5576368, upload-time = "2025-09-14T22:17:40.206Z" },
    { url = "https://files.pythonhosted.org/packages/5d/35/398dc2ffc89d304d59bc12f0fdd931b4ce455bddf7038a0a67733a25f550/zstandard-0.25.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:3c83b0188c852a47cd13ef3bf9209fb0a77fa5374958b8c53aaa699398c6bd7b", size = 4954022, upload-time = "2025-09-14T22:17:41.879Z" },
    { url = "https://files.pythonhosted.org/packages/9a/5c/36ba1e5507d56d2213202ec2b05e8541734af5f2ce378c5d1ceaf4d88dc4/zstandard-0.25.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:1673b7199bbe763365b81a4f3252b8e80f44c9e323fc42940dc8843bfeaf9851", size = 5267889, upload-time = "2025-09-14T22:17:43.577Z" },
    { url = "https://files.pythonhosted.org/packages/70/e8/2ec6b6fb7358b2ec0113ae202647ca7c0e9d15b61c005ae5225ad0995df5/zstandard-0.25.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:0be7622c37c183406f3dbf0cba104118eb16a4ea7359eeb5752f0794882fc250", size = 5433952, upload-time = "2025-09-14T22:17:45.271Z" },
    { url = "https://files.pythonhosted.org/packages/7b/01/b5f4d4dbc59ef193e870495c6f1275f5b2928e01ff5a81fecb22a06e22fb/zstandard-0.25.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:5f5e4c2a23ca271c218ac025bd7d635597048b366d6f31f420aaeb715239fc98", size = 5814054, upload-time = "2025-09-14T22:17:47.08Z" },
    { url = "https://files.pythonhosted.org/packages/b2/e5/fbd822d5c6f427cf158316d012c5a12f233473c2f9c5fe5ab1ae5d21f3d8/zstandard-0.25.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:4f187a0bb61b35119d1926aee039524d1f93aaf38a9916b8c4b78ac8514a0aaf", size = 5360113, upload-time = "2025-09-14T22:17:48.893Z" },
    { url = "https://files.pythonhosted.org/packages/8e/e0/69a553d2047f9a2c7347caa225bb3a63b6d7704ad74610cb7823baa08ed7/zstandard-0.25.0-cp313-cp313-win32.whl", hash = "sha256:7030defa83eef3e51ff26f0b7bfb229f0204b66fe18e04359ce3474ac33cbc09", size = 436936, upload-time = "2025-09-14T22:17:52.658Z" },
    { url = "https://files.pythonhosted.org/packages/d9/82/b9c06c870f3bd8767c201f1edbdf9e8dc34be5b0fbc5682c4f80fe948475/zstandard-0.25.0-cp313-cp313-win_amd64.whl", hash = "sha256:1f830a0dac88719af0ae43b8b2d6aef487d437036468ef3c2ea59c51f9d55fd5", size = 506232, upload-time = "2025-09-14T22:17:50.402Z" },
    { url = "https://files.pythonhosted.org/packages/d4/57/60c3c01243bb81d381c9916e2a6d9e149ab8627c0c7d7abb2d73384b3c0c/zstandard-0.25.0-cp313-cp313-win_arm64.whl", hash = "sha256:85304a43f4d513f5464ceb938aa02c1e78c2943b29f44a750b48b25ac999a049", size = 462671, upload-time = "2025-09-14T22:17:51.533Z" },
    { url = "https://files.pythonhosted.org/packages/3d/5c/f8923b595b55fe49e30612987ad8bf053aef555c14f05bb659dd5dbe3e8a/zstandard-0.25.0-cp314-cp314-macosx_10_13_x86_64.whl", hash = "sha256:e29f0cf06974c899b2c188ef7f783607dbef36da4c242eb6c82dcd8b512855e3", size = 795887, upload-time = "2025-09-14T22:17:54.198Z" },
    { url = "https://files.pythonhosted.org/packages/8d/09/d0a2a14fc3439c5f874042dca72a79c70a532090b7ba0003be73fee37ae2/zstandard-0.25.0-cp314-cp314-macosx_11_0_arm64.whl", hash = "sha256:05df5136bc5a011f33cd25bc9f506e7426c0c9b3f9954f056831ce68f3b6689f", size = 640658, upload-time = "2025-09-14T22:17:55.423Z" },
    { url = "https://files.pythonhosted.org/packages/5d/7c/8b6b71b1ddd517f68ffb55e10834388d4f793c49c6b83effaaa05785b0b4/zstandard-0.25.0-cp314-cp314-manylinux2010_i686.manylinux_2_12_i686.manylinux_2_28_i686.whl", hash = "sha256:f604efd28f239cc21b3adb53eb061e2a205dc164be408e553b41ba2ffe0ca15c", size = 5379849, upload-time = "2025-09-14T22:17:57.372Z" },
    { url = "https://files.pythonhosted.org/packages/a4/86/a48e56320d0a17189ab7a42645387334fba2200e904ee47fc5a26c1fd8ca/zstandard-0.25.0-cp314-cp314-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl", hash = "sha256:223415140608d0f0da010499eaa8ccdb9af210a543fac54bce15babbcfc78439", size = 5058095, upload-time = "2025-09-14T22:17:59.498Z" },
    { url = "https://files.pythonhosted.org/packages/f8/ad/eb659984ee2c0a779f9d06dbfe45e2dc39d99ff40a319895df2d3d9a48e5/zstandard-0.25.0-cp314-cp314-manylinux2014_ppc64le.manylinux_2_17_ppc64le.manylinux_2_28_ppc64le.whl", hash = "sha256:2e54296a283f3ab5a26fc9b8b5d4978ea0532f37b231644f367aa588930aa043", size = 5551751, upload-time = "2025-09-14T22:18:01.618Z" },
    { url = "https://files.pythonhosted.org/packages/61/b3/b637faea43677eb7bd42ab204dfb7053bd5c4582bfe6b1baefa80ac0c47b/zstandard-0.25.0-cp314-cp314-manylinux2014_s390x.manylinux_2_17_s390x.manylinux_2_28_s390x.whl", hash = "sha256:ca54090275939dc8ec5dea2d2afb400e0f83444b2fc24e07df7fdef677110859", size = 6364818, upload-time = "2025-09-14T22:18:03.769Z" },
    { url = "https://files.pythonhosted.org/packages/31/dc/cc50210e11e465c975462439a492516a73300ab8caa8f5e0902544fd748b/zstandard-0.25.0-cp314-cp314-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl", hash = "sha256:e09bb6252b6476d8d56100e8147b803befa9a12cea144bbe629dd508800d1ad0", size = 5560402, upload-time = "2025-09-14T22:18:05.954Z" },
    { url = "https://files.pythonhosted.org/packages/c9/ae/56523ae9c142f0c08efd5e868a6da613ae76614eca1305259c3bf6a0ed43/zstandard-0.25.0-cp314-cp314-musllinux_1_2_aarch64.whl", hash = "sha256:a9ec8c642d1ec73287ae3e726792dd86c96f5681eb8df274a757bf62b750eae7", size = 4955108, upload-time = "2025-09-14T22:18:07.68Z" },
    { url = "https://files.pythonhosted.org/packages/98/cf/c899f2d6df0840d5e384cf4c4121458c72802e8bda19691f3b16619f51e9/zstandard-0.25.0-cp314-cp314-musllinux_1_2_i686.whl", hash = "sha256:a4089a10e598eae6393756b036e0f419e8c1d60f44a831520f9af41c14216cf2", size = 5269248, upload-time = "2025-09-14T22:18:09.753Z" },
    { url = "https://files.pythonhosted.org/packages/1b/c0/59e912a531d91e1c192d3085fc0f6fb2852753c301a812d856d857ea03c6/zstandard-0.25.0-cp314-cp314-musllinux_1_2_ppc64le.whl", hash = "sha256:f67e8f1a324a900e75b5e28ffb152bcac9fbed1cc7b43f99cd90f395c4375344", size = 5430330, upload-time = "2025-09-14T22:18:11.966Z" },
    { url = "https://files.pythonhosted.org/packages/a0/1d/7e31db1240de2df22a58e2ea9a93fc6e38cc29353e660c0272b6735d6669/zstandard-0.25.0-cp314-cp314-musllinux_1_2_s390x.whl", hash = "sha256:9654dbc012d8b06fc3d19cc825af3f7bf8ae242226df5f83936cb39f5fdc846c", size = 5811123, upload-time = "2025-09-14T22:18:13.907Z" },
    { url = "https://files.pythonhosted.org/packages/f6/49/fac46df5ad353d50535e118d6983069df68ca5908d4d65b8c466150a4ff1/zstandard-0.25.0-cp314-cp314-musllinux_1_2_x86_64.whl", hash = "sha256:4203ce3b31aec23012d3a4cf4a2ed64d12fea5269c49aed5e4c3611b938e4088", size = 5359591, upload-time = "2025-09-14T22:18:16.465Z" },
    { url = "https://files.pythonhosted.org/packages/c2/38/f249a2050ad1eea0bb364046153942e34abba95dd5520af199aed86fbb49/zstandard-0.25.0-cp314-cp314-win32.whl", hash = "sha256:da469dc041701583e34de852d8634703550348d5822e66a0c827d39b05365b12", size = 444513, upload-time = "2025-09-14T22:18:20.61Z" },
    { url = "https://files.pythonhosted.org/packages/3a/43/241f9615bcf8ba8903b3f0432da069e857fc4fd1783bd26183db53c4804b/zstandard-0.25.0-cp314-cp314-win_amd64.whl", hash = "sha256:c19bcdd826e95671065f8692b5a4aa95c52dc7a02a4c5a0cac46deb879a017a2", size = 516118, upload-time = "2025-09-14T22:18:17.849Z" },
    { url = "https://files.pythonhosted.org/packages/f0/ef/da163ce2450ed4febf6467d77ccb4cd52c4c30ab45624bad26ca0a27260c/zstandard-0.25.0-cp314-cp314-win_arm64.whl", hash = "sha256:d7541afd73985c630bafcd6338d2518ae96060075f9463d7dc14cfb33514383d", size = 476940, upload-time = "2025-09-14T22:18:19.088Z" },
]
```

## File: `backend/run.py`
```python
import argparse
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path
BACKEND_DIR = Path(__file__).parent
if str(BACKEND_DIR) not in sys.path:
    sys.path.insert(0, str(BACKEND_DIR))

# ── Load .env (GROQ_API_KEY etc.) ────────────────────────────────────────────
try:
    from dotenv import load_dotenv
    env_path = BACKEND_DIR.parent / ".env"
    load_dotenv(dotenv_path=env_path)
except ImportError:
    pass  # python-dotenv is optional; export env vars manually if needed

# ── Import compiled graph ─────────────────────────────────────────────────────
from graph.graph import graph


# ─────────────────────────────────────────────────────────────────────────────

def today_ist() -> str:
    ist = timezone(timedelta(hours=5, minutes=30))
    return datetime.now(ist).strftime("%Y-%m-%d")


def main():
    parser = argparse.ArgumentParser(
        description="BlogBoard LangGraph Article Generator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples
--------
  # Generate today's article (IST):
  python backend/run.py

  # Generate for a specific date:
  python backend/run.py --date 2026-03-07

  # Dry run — no LLM calls, no file writes:
  python backend/run.py --dry-run
        """,
    )
    parser.add_argument(
        "--date", type=str, default=None,
        help="Target date in YYYY-MM-DD format (default: today in IST)",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Preview mode: skip Groq calls and file writes",
    )
    parser.add_argument(
        "--ainews", action="store_true",
        help="Run the AI News gathering and generation graph",
    )
    args = parser.parse_args()

    date_str = args.date or today_ist()
    dry_run  = args.dry_run
    run_ainews = args.ainews

    # ── Banner ────────────────────────────────────────────────────────────────
    print(f"\n{'='*55}")
    print(f"  BlogBoard — LangGraph Article Generator")
    print(f"  Date    : {date_str}")
    print(f"  Dry run : {dry_run}")
    print(f"{'='*55}")

    # ── Build initial state and invoke the graph ──────────────────────────────
    initial_state = {
        "date":    date_str,
        "dry_run": dry_run,
    }

    config = {"configurable": {"thread_id": "blogboard-1"}}
    if run_ainews:
        from graph.graph_ainews import ainews_graph
        final_state = ainews_graph.invoke(initial_state, config=config)
    else:
        final_state = graph.invoke(initial_state, config=config)

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n{'='*55}")
    if final_state.get("skipped"):
        print(f"  ℹ️  No article scheduled for {date_str}.")
        print(f"  (Sundays or unscheduled dates are skipped automatically.)")
    elif dry_run:
        print(f"  [DRY RUN] Pipeline completed — no files were written.")
        print(f"  Would have generated:")
        domain = final_state.get("domain", "?")
        slug   = final_state.get("slug", "?")
        print(f"    → frontend/blogs/{domain}/{slug}.md")
        print(f"    → frontend/blogs/{domain}/articles.json")
    else:
        domain    = final_state.get("domain", "?")
        title     = final_state.get("title", "?")
        md_path   = final_state.get("md_path", "?")
        read_time = final_state.get("read_time", "?")
        print(f"  🎉 Done!  Article generated successfully.")
        print(f"  Title     : {title}")
        print(f"  Domain    : {domain}")
        print(f"  Read time : {read_time}")
        print(f"  File      : {md_path}")
    print(f"{'='*55}\n")


if __name__ == "__main__":
    main()
```

## File: `backend/schedule.json`
```json
{
  "2026-03-02": {
    "domain": "ml",
    "topic": "What is Machine Learning?",
    "subtopics": "What is Machine Learning, Why use, Example Applications, Intro to ML Systems and its types"
  },
  "2026-03-03": {
    "domain": "dl",
    "topic": "Introduction to Deep Learning",
    "subtopics": "What is Deep Learning, Why use, Example Applications, and its types"
  },
  "2026-03-04": {
    "domain": "statistics",
    "topic": "Introduction to Statistics for AI & ML",
    "subtopics": "Why Learn Statistics for ai, Applications of Statistics in ai"
  },
  "2026-03-05": {
    "domain": "nlp",
    "topic": "Introduction to NLP"
  },
  "2026-03-06": {
    "domain": "cv",
    "topic": "Introduction to Computer Vision"
  },
  "2026-03-07": {
    "domain": "genai",
    "topic": "Introduction to Generative AI"
  },
  "2026-03-09": {
    "domain": "ml",
    "topic": "Main Challenges of Machine Learning"
  },
  "2026-03-11": {
    "domain": "statistics",
    "topic": "Types of Data in ML"
  },
  "2026-03-12": {
    "domain": "nlp",
    "topic": "Text Preprocessing Techniques"
  },
  "2026-03-13": {
    "domain": "cv",
    "topic": "Digital Image Fundamentals"
  },
  "2026-03-14": {
    "domain": "genai",
    "topic": "History of Generative Models"
  },
  "2026-03-16": {
    "domain": "ml",
    "topic": "Life Cycle of Machine Learning Project"
  },
  "2026-03-18": {
    "domain": "statistics",
    "topic": "Population vs Sample"
  },
  "2026-03-19": {
    "domain": "nlp",
    "topic": "Tokenization Methods"
  },
  "2026-03-20": {
    "domain": "cv",
    "topic": "Image Representation and Color Spaces"
  },
  "2026-03-21": {
    "domain": "genai",
    "topic": "Probabilistic Generative Modeling"
  },
  "2026-03-23": {
    "domain": "ml",
    "topic": "Supervised Machine Learning - Classfication"
  },
  "2026-03-25": {
    "domain": "statistics",
    "topic": "Measures of Central Tendency"
  },
  "2026-03-26": {
    "domain": "nlp",
    "topic": "Stopwords and Text Cleaning"
  },
  "2026-03-27": {
    "domain": "cv",
    "topic": "Image Filtering and Convolution"
  },
  "2026-03-28": {
    "domain": "genai",
    "topic": "Autoregressive Models"
  },
  "2026-03-30": {
    "domain": "ml",
    "topic": "Supervised Machine Learning - Regression"
  },
  "2026-04-01": {
    "domain": "statistics",
    "topic": "Measures of Dispersion"
  },
  "2026-04-02": {
    "domain": "nlp",
    "topic": "Stemming and Lemmatization"
  },
  "2026-04-03": {
    "domain": "cv",
    "topic": "Edge Detection Techniques"
  },
  "2026-04-04": {
    "domain": "genai",
    "topic": "Energy-Based Models"
  },
  "2026-04-06": {
    "domain": "ml",
    "topic": "Unsupervised Machine Learning - Clustering"
  },
  "2026-04-08": {
    "domain": "statistics",
    "topic": "Probability Basics"
  },
  "2026-04-09": {
    "domain": "nlp",
    "topic": "Regular Expressions for Text"
  },
  "2026-04-10": {
    "domain": "cv",
    "topic": "Histogram Equalization"
  },
  "2026-04-11": {
    "domain": "genai",
    "topic": "Variational Autoencoders"
  },
  "2026-04-15": {
    "domain": "statistics",
    "topic": "Conditional Probability"
  },
  "2026-04-16": {
    "domain": "nlp",
    "topic": "Bag of Words Model"
  },
  "2026-04-17": {
    "domain": "cv",
    "topic": "Image Thresholding"
  },
  "2026-04-18": {
    "domain": "genai",
    "topic": "GAN Fundamentals"
  },
  "2026-04-22": {
    "domain": "statistics",
    "topic": "Bayes Theorem"
  },
  "2026-04-23": {
    "domain": "nlp",
    "topic": "TF-IDF Representation"
  },
  "2026-04-24": {
    "domain": "cv",
    "topic": "Morphological Operations"
  },
  "2026-04-25": {
    "domain": "genai",
    "topic": "GAN Training Challenges"
  },
  "2026-04-29": {
    "domain": "statistics",
    "topic": "Random Variables"
  },
  "2026-04-30": {
    "domain": "nlp",
    "topic": "N-grams and Language Modeling"
  },
  "2026-05-01": {
    "domain": "cv",
    "topic": "Feature Detection and Description"
  },
  "2026-05-02": {
    "domain": "genai",
    "topic": "Conditional GANs"
  },
  "2026-05-06": {
    "domain": "statistics",
    "topic": "Probability Distributions Overview"
  },
  "2026-05-07": {
    "domain": "nlp",
    "topic": "Word Embeddings Overview"
  },
  "2026-05-08": {
    "domain": "cv",
    "topic": "SIFT and SURF"
  },
  "2026-05-09": {
    "domain": "genai",
    "topic": "CycleGAN"
  },
  "2026-05-13": {
    "domain": "statistics",
    "topic": "Normal Distribution"
  },
  "2026-05-14": {
    "domain": "nlp",
    "topic": "Word2Vec Architecture"
  },
  "2026-05-15": {
    "domain": "cv",
    "topic": "ORB Features"
  },
  "2026-05-16": {
    "domain": "genai",
    "topic": "Diffusion Model Basics"
  },
  "2026-05-20": {
    "domain": "statistics",
    "topic": "Binomial Distribution"
  },
  "2026-05-21": {
    "domain": "nlp",
    "topic": "GloVe Embeddings"
  },
  "2026-05-22": {
    "domain": "cv",
    "topic": "Image Segmentation Basics"
  },
  "2026-05-23": {
    "domain": "genai",
    "topic": "Denoising Diffusion Probabilistic Models"
  },
  "2026-05-27": {
    "domain": "statistics",
    "topic": "Poisson Distribution"
  },
  "2026-05-28": {
    "domain": "nlp",
    "topic": "FastText Model"
  },
  "2026-05-29": {
    "domain": "cv",
    "topic": "K-Means for Image Segmentation"
  },
  "2026-05-30": {
    "domain": "genai",
    "topic": "Latent Diffusion Models"
  },
  "2026-06-03": {
    "domain": "statistics",
    "topic": "Uniform Distribution"
  },
  "2026-06-04": {
    "domain": "nlp",
    "topic": "Contextual Embeddings"
  },
  "2026-06-05": {
    "domain": "cv",
    "topic": "Hough Transform"
  },
  "2026-06-06": {
    "domain": "genai",
    "topic": "Score-Based Generative Models"
  },
  "2026-06-10": {
    "domain": "statistics",
    "topic": "Central Limit Theorem"
  },
  "2026-06-11": {
    "domain": "nlp",
    "topic": "Sentence and Document Embeddings"
  },
  "2026-06-12": {
    "domain": "cv",
    "topic": "Template Matching"
  },
  "2026-06-13": {
    "domain": "genai",
    "topic": "Normalizing Flows"
  },
  "2026-06-17": {
    "domain": "statistics",
    "topic": "Law of Large Numbers"
  },
  "2026-06-18": {
    "domain": "nlp",
    "topic": "Similarity Measures in NLP"
  },
  "2026-06-19": {
    "domain": "cv",
    "topic": "Optical Flow"
  },
  "2026-06-20": {
    "domain": "genai",
    "topic": "Transformer Architecture for Generation"
  },
  "2026-06-24": {
    "domain": "statistics",
    "topic": "Sampling Techniques"
  },
  "2026-06-25": {
    "domain": "nlp",
    "topic": "Text Classification Fundamentals"
  },
  "2026-06-26": {
    "domain": "cv",
    "topic": "Object Detection Fundamentals"
  },
  "2026-06-27": {
    "domain": "genai",
    "topic": "Large Language Model Fundamentals"
  },
  "2026-07-01": {
    "domain": "statistics",
    "topic": "Sampling Bias"
  },
  "2026-07-02": {
    "domain": "nlp",
    "topic": "Naive Bayes for NLP"
  },
  "2026-07-03": {
    "domain": "cv",
    "topic": "Region-Based CNN"
  },
  "2026-07-04": {
    "domain": "genai",
    "topic": "Pretraining Objectives in LLMs"
  },
  "2026-07-08": {
    "domain": "statistics",
    "topic": "Point Estimation"
  },
  "2026-07-09": {
    "domain": "nlp",
    "topic": "Logistic Regression for Text"
  },
  "2026-07-10": {
    "domain": "cv",
    "topic": "Fast and Faster R-CNN"
  },
  "2026-07-11": {
    "domain": "genai",
    "topic": "Causal vs Masked Language Models"
  },
  "2026-07-15": {
    "domain": "statistics",
    "topic": "Confidence Intervals"
  },
  "2026-07-16": {
    "domain": "nlp",
    "topic": "Evaluation Metrics in NLP"
  },
  "2026-07-17": {
    "domain": "cv",
    "topic": "YOLO Architecture"
  },
  "2026-07-18": {
    "domain": "genai",
    "topic": "Scaling Laws in LLMs"
  },
  "2026-07-22": {
    "domain": "statistics",
    "topic": "Hypothesis Testing Basics"
  },
  "2026-07-23": {
    "domain": "nlp",
    "topic": "Topic Modeling Concepts"
  },
  "2026-07-24": {
    "domain": "cv",
    "topic": "SSD Object Detection"
  },
  "2026-07-25": {
    "domain": "genai",
    "topic": "Fine-Tuning Strategies"
  },
  "2026-07-29": {
    "domain": "statistics",
    "topic": "Null vs Alternative Hypothesis"
  },
  "2026-07-30": {
    "domain": "nlp",
    "topic": "Latent Dirichlet Allocation"
  },
  "2026-07-31": {
    "domain": "cv",
    "topic": "Image Classification with CNNs"
  },
  "2026-08-01": {
    "domain": "genai",
    "topic": "Instruction Tuning"
  },
  "2026-08-05": {
    "domain": "statistics",
    "topic": "p-value Explained"
  },
  "2026-08-06": {
    "domain": "nlp",
    "topic": "Named Entity Recognition"
  },
  "2026-08-07": {
    "domain": "cv",
    "topic": "Transfer Learning in Vision"
  },
  "2026-08-08": {
    "domain": "genai",
    "topic": "Reinforcement Learning from Human Feedback"
  },
  "2026-08-12": {
    "domain": "statistics",
    "topic": "Type I & Type II Errors"
  },
  "2026-08-13": {
    "domain": "nlp",
    "topic": "Part-of-Speech Tagging"
  },
  "2026-08-14": {
    "domain": "cv",
    "topic": "ResNet Architecture"
  },
  "2026-08-15": {
    "domain": "genai",
    "topic": "Direct Preference Optimization"
  },
  "2026-08-19": {
    "domain": "statistics",
    "topic": "Z-Test"
  },
  "2026-08-20": {
    "domain": "nlp",
    "topic": "Dependency Parsing"
  },
  "2026-08-21": {
    "domain": "cv",
    "topic": "DenseNet Overview"
  },
  "2026-08-22": {
    "domain": "genai",
    "topic": "Parameter-Efficient Fine-Tuning"
  },
  "2026-08-26": {
    "domain": "statistics",
    "topic": "T-Test"
  },
  "2026-08-27": {
    "domain": "nlp",
    "topic": "Hidden Markov Models in NLP"
  },
  "2026-08-28": {
    "domain": "cv",
    "topic": "EfficientNet"
  },
  "2026-08-29": {
    "domain": "genai",
    "topic": "LoRA and Adapters"
  },
  "2026-09-02": {
    "domain": "statistics",
    "topic": "Chi-Square Test"
  },
  "2026-09-03": {
    "domain": "nlp",
    "topic": "Conditional Random Fields"
  },
  "2026-09-04": {
    "domain": "cv",
    "topic": "Vision Transformers"
  },
  "2026-09-05": {
    "domain": "genai",
    "topic": "Prompt Engineering Principles"
  },
  "2026-09-09": {
    "domain": "statistics",
    "topic": "ANOVA"
  },
  "2026-09-10": {
    "domain": "nlp",
    "topic": "Recurrent Neural Networks for NLP"
  },
  "2026-09-11": {
    "domain": "cv",
    "topic": "Self-Attention in Vision"
  },
  "2026-09-12": {
    "domain": "genai",
    "topic": "Chain-of-Thought Prompting"
  },
  "2026-09-16": {
    "domain": "statistics",
    "topic": "Correlation vs Covariance"
  },
  "2026-09-17": {
    "domain": "nlp",
    "topic": "LSTM for Sequence Modeling"
  },
  "2026-09-18": {
    "domain": "cv",
    "topic": "Semantic Segmentation"
  },
  "2026-09-19": {
    "domain": "genai",
    "topic": "Few-Shot and Zero-Shot Prompting"
  },
  "2026-09-23": {
    "domain": "statistics",
    "topic": "Pearson Correlation"
  },
  "2026-09-24": {
    "domain": "nlp",
    "topic": "GRU Networks"
  },
  "2026-09-25": {
    "domain": "cv",
    "topic": "U-Net Architecture"
  },
  "2026-09-26": {
    "domain": "genai",
    "topic": "Retrieval-Augmented Generation"
  },
  "2026-09-30": {
    "domain": "statistics",
    "topic": "Spearman Correlation"
  },
  "2026-10-01": {
    "domain": "nlp",
    "topic": "Attention Mechanism"
  },
  "2026-10-02": {
    "domain": "cv",
    "topic": "Instance Segmentation"
  },
  "2026-10-03": {
    "domain": "genai",
    "topic": "Vector Databases in GenAI"
  },
  "2026-10-07": {
    "domain": "statistics",
    "topic": "Regression Assumptions"
  },
  "2026-10-08": {
    "domain": "nlp",
    "topic": "Transformers Architecture"
  },
  "2026-10-09": {
    "domain": "cv",
    "topic": "Mask R-CNN"
  },
  "2026-10-10": {
    "domain": "genai",
    "topic": "Embedding Models"
  },
  "2026-10-14": {
    "domain": "statistics",
    "topic": "Maximum Likelihood Estimation"
  },
  "2026-10-15": {
    "domain": "nlp",
    "topic": "Self-Attention Deep Dive"
  },
  "2026-10-16": {
    "domain": "cv",
    "topic": "Pose Estimation"
  },
  "2026-10-17": {
    "domain": "genai",
    "topic": "Text-to-Image Generation"
  },
  "2026-10-21": {
    "domain": "statistics",
    "topic": "Log-Likelihood in ML"
  },
  "2026-10-22": {
    "domain": "nlp",
    "topic": "BERT Model Overview"
  },
  "2026-10-23": {
    "domain": "cv",
    "topic": "3D Computer Vision Basics"
  },
  "2026-10-24": {
    "domain": "genai",
    "topic": "Image-to-Image Generation"
  },
  "2026-10-28": {
    "domain": "statistics",
    "topic": "Bias & Variance in Estimation"
  },
  "2026-10-29": {
    "domain": "nlp",
    "topic": "GPT Model Overview"
  },
  "2026-10-30": {
    "domain": "cv",
    "topic": "Stereo Vision"
  },
  "2026-10-31": {
    "domain": "genai",
    "topic": "Text-to-Video Generation"
  },
  "2026-11-04": {
    "domain": "statistics",
    "topic": "Variance Inflation Factor"
  },
  "2026-11-05": {
    "domain": "nlp",
    "topic": "Pretraining vs Fine-Tuning"
  },
  "2026-11-06": {
    "domain": "cv",
    "topic": "Structure from Motion"
  },
  "2026-11-07": {
    "domain": "genai",
    "topic": "Multimodal Generative Models"
  },
  "2026-11-11": {
    "domain": "statistics",
    "topic": "Multicollinearity"
  },
  "2026-11-12": {
    "domain": "nlp",
    "topic": "Transfer Learning in NLP"
  },
  "2026-11-13": {
    "domain": "cv",
    "topic": "Image Augmentation Techniques"
  },
  "2026-11-14": {
    "domain": "genai",
    "topic": "Vision-Language Models"
  },
  "2026-11-18": {
    "domain": "statistics",
    "topic": "Outlier Detection Methods"
  },
  "2026-11-19": {
    "domain": "nlp",
    "topic": "Text Generation Concepts"
  },
  "2026-11-20": {
    "domain": "cv",
    "topic": "Data Annotation in Vision"
  },
  "2026-11-21": {
    "domain": "genai",
    "topic": "Audio Generation Models"
  },
  "2026-11-25": {
    "domain": "statistics",
    "topic": "Skewness & Kurtosis"
  },
  "2026-11-26": {
    "domain": "nlp",
    "topic": "Sequence-to-Sequence Models"
  },
  "2026-11-27": {
    "domain": "cv",
    "topic": "Evaluation Metrics in Vision"
  },
  "2026-11-28": {
    "domain": "genai",
    "topic": "Speech Synthesis Models"
  },
  "2026-12-02": {
    "domain": "statistics",
    "topic": "Feature Distribution Analysis"
  },
  "2026-12-03": {
    "domain": "nlp",
    "topic": "Beam Search and Decoding"
  },
  "2026-12-04": {
    "domain": "cv",
    "topic": "Intersection over Union"
  },
  "2026-12-05": {
    "domain": "genai",
    "topic": "Music Generation Models"
  },
  "2026-12-09": {
    "domain": "statistics",
    "topic": "Data Normalization vs Standardization"
  },
  "2026-12-10": {
    "domain": "nlp",
    "topic": "Perplexity in Language Models"
  },
  "2026-12-11": {
    "domain": "cv",
    "topic": "Mean Average Precision"
  },
  "2026-12-12": {
    "domain": "genai",
    "topic": "Evaluation of Generative Models"
  },
  "2026-12-16": {
    "domain": "statistics",
    "topic": "Bootstrapping"
  },
  "2026-12-17": {
    "domain": "nlp",
    "topic": "BLEU and ROUGE Metrics"
  },
  "2026-12-18": {
    "domain": "cv",
    "topic": "Adversarial Attacks in Vision"
  },
  "2026-12-19": {
    "domain": "genai",
    "topic": "Perplexity and FID Score"
  },
  "2026-12-23": {
    "domain": "statistics",
    "topic": "Resampling Methods"
  },
  "2026-12-24": {
    "domain": "nlp",
    "topic": "Sentiment Analysis Theory"
  },
  "2026-12-25": {
    "domain": "cv",
    "topic": "Adversarial Defense Methods"
  },
  "2026-12-26": {
    "domain": "genai",
    "topic": "Hallucination in LLMs"
  },
  "2026-12-30": {
    "domain": "statistics",
    "topic": "Monte Carlo Simulation"
  },
  "2026-12-31": {
    "domain": "nlp",
    "topic": "Aspect-Based Sentiment Analysis"
  },
  "2027-01-01": {
    "domain": "cv",
    "topic": "Explainability in Vision Models"
  },
  "2027-01-02": {
    "domain": "genai",
    "topic": "Bias and Fairness in GenAI"
  },
  "2027-01-06": {
    "domain": "statistics",
    "topic": "A/B Testing Fundamentals"
  },
  "2027-01-07": {
    "domain": "nlp",
    "topic": "Text Summarization Techniques"
  },
  "2027-01-08": {
    "domain": "cv",
    "topic": "Grad-CAM"
  },
  "2027-01-09": {
    "domain": "genai",
    "topic": "Safety Alignment Techniques"
  },
  "2027-01-13": {
    "domain": "statistics",
    "topic": "Statistical Power"
  },
  "2027-01-14": {
    "domain": "nlp",
    "topic": "Machine Translation Fundamentals"
  },
  "2027-01-15": {
    "domain": "cv",
    "topic": "Model Compression in Vision"
  },
  "2027-01-16": {
    "domain": "genai",
    "topic": "Red Teaming for LLMs"
  },
  "2027-01-20": {
    "domain": "statistics",
    "topic": "Effect Size"
  },
  "2027-01-21": {
    "domain": "nlp",
    "topic": "Information Retrieval Basics"
  },
  "2027-01-22": {
    "domain": "cv",
    "topic": "Quantization in Vision Models"
  },
  "2027-01-23": {
    "domain": "genai",
    "topic": "Adversarial Attacks on Generative Models"
  },
  "2027-01-27": {
    "domain": "statistics",
    "topic": "Confounding Variables"
  },
  "2027-01-28": {
    "domain": "nlp",
    "topic": "BM25 Algorithm"
  },
  "2027-01-29": {
    "domain": "cv",
    "topic": "Pruning CNNs"
  },
  "2027-01-30": {
    "domain": "genai",
    "topic": "Model Robustness in GenAI"
  },
  "2027-02-03": {
    "domain": "statistics",
    "topic": "Causal Inference Basics"
  },
  "2027-02-04": {
    "domain": "nlp",
    "topic": "Semantic Search Concepts"
  },
  "2027-02-05": {
    "domain": "cv",
    "topic": "Knowledge Distillation in Vision"
  },
  "2027-02-06": {
    "domain": "genai",
    "topic": "Knowledge Distillation for LLMs"
  },
  "2027-02-10": {
    "domain": "statistics",
    "topic": "Propensity Score Matching"
  },
  "2027-02-11": {
    "domain": "nlp",
    "topic": "Vector Representations for Search"
  },
  "2027-02-12": {
    "domain": "cv",
    "topic": "Self-Supervised Learning in Vision"
  },
  "2027-02-13": {
    "domain": "genai",
    "topic": "Quantization of Large Models"
  },
  "2027-02-17": {
    "domain": "statistics",
    "topic": "Time Series Statistics Basics"
  },
  "2027-02-18": {
    "domain": "nlp",
    "topic": "Cross-Lingual NLP"
  },
  "2027-02-19": {
    "domain": "cv",
    "topic": "Contrastive Learning in Vision"
  },
  "2027-02-20": {
    "domain": "genai",
    "topic": "Pruning Large Language Models"
  },
  "2027-02-24": {
    "domain": "statistics",
    "topic": "Stationarity"
  },
  "2027-02-25": {
    "domain": "nlp",
    "topic": "Multilingual Language Models"
  },
  "2027-02-26": {
    "domain": "cv",
    "topic": "Few-Shot Learning in Vision"
  },
  "2027-02-27": {
    "domain": "genai",
    "topic": "Distributed Training of LLMs"
  },
  "2027-03-03": {
    "domain": "statistics",
    "topic": "Autocorrelation"
  },
  "2027-03-04": {
    "domain": "nlp",
    "topic": "Zero-Shot and Few-Shot Learning"
  },
  "2027-03-05": {
    "domain": "cv",
    "topic": "Zero-Shot Learning in Vision"
  },
  "2027-03-06": {
    "domain": "genai",
    "topic": "Mixture of Experts Models"
  },
  "2027-03-10": {
    "domain": "statistics",
    "topic": "Partial Autocorrelation"
  },
  "2027-03-11": {
    "domain": "nlp",
    "topic": "Prompting Techniques"
  },
  "2027-03-12": {
    "domain": "cv",
    "topic": "Domain Adaptation in Vision"
  },
  "2027-03-13": {
    "domain": "genai",
    "topic": "Sparse Transformers"
  },
  "2027-03-17": {
    "domain": "statistics",
    "topic": "Heteroscedasticity"
  },
  "2027-03-18": {
    "domain": "nlp",
    "topic": "Hallucination in Language Models"
  },
  "2027-03-19": {
    "domain": "cv",
    "topic": "Federated Learning in Vision"
  },
  "2027-03-20": {
    "domain": "genai",
    "topic": "Memory-Augmented Models"
  },
  "2027-03-24": {
    "domain": "statistics",
    "topic": "Cross Validation from Statistical View"
  },
  "2027-03-25": {
    "domain": "nlp",
    "topic": "Bias in NLP Models"
  },
  "2027-03-26": {
    "domain": "cv",
    "topic": "Edge AI for Vision"
  },
  "2027-03-27": {
    "domain": "genai",
    "topic": "Long-Context Modeling"
  },
  "2027-03-31": {
    "domain": "statistics",
    "topic": "ROC Curve Statistical Meaning"
  },
  "2027-04-01": {
    "domain": "nlp",
    "topic": "Explainability in NLP"
  },
  "2027-04-02": {
    "domain": "cv",
    "topic": "ONNX for Vision Models"
  },
  "2027-04-03": {
    "domain": "genai",
    "topic": "Agentic AI Concepts"
  },
  "2027-04-07": {
    "domain": "statistics",
    "topic": "Precision-Recall Tradeoff"
  },
  "2027-04-08": {
    "domain": "nlp",
    "topic": "Model Compression in NLP"
  },
  "2027-04-09": {
    "domain": "cv",
    "topic": "TensorRT Optimization"
  },
  "2027-04-10": {
    "domain": "genai",
    "topic": "Tool-Calling in LLMs"
  },
  "2027-04-14": {
    "domain": "statistics",
    "topic": "Calibration of Probabilities"
  },
  "2027-04-15": {
    "domain": "nlp",
    "topic": "Distillation in NLP"
  },
  "2027-04-16": {
    "domain": "cv",
    "topic": "Video Analysis Basics"
  },
  "2027-04-17": {
    "domain": "genai",
    "topic": "Planning and Reasoning in LLMs"
  },
  "2027-04-21": {
    "domain": "statistics",
    "topic": "Entropy in ML"
  },
  "2027-04-22": {
    "domain": "nlp",
    "topic": "Quantization Techniques"
  },
  "2027-04-23": {
    "domain": "cv",
    "topic": "Action Recognition"
  },
  "2027-04-24": {
    "domain": "genai",
    "topic": "Self-Reflection in LLMs"
  },
  "2027-04-28": {
    "domain": "statistics",
    "topic": "Information Gain"
  },
  "2027-04-29": {
    "domain": "nlp",
    "topic": "Scaling NLP Models"
  },
  "2027-04-30": {
    "domain": "cv",
    "topic": "Object Tracking"
  },
  "2027-05-01": {
    "domain": "genai",
    "topic": "Synthetic Data Generation"
  },
  "2027-05-05": {
    "domain": "statistics",
    "topic": "Kullback-Leibler Divergence"
  },
  "2027-05-06": {
    "domain": "nlp",
    "topic": "Low-Resource Language Modeling"
  },
  "2027-05-07": {
    "domain": "cv",
    "topic": "Multi-Object Tracking"
  },
  "2027-05-08": {
    "domain": "genai",
    "topic": "Data-Centric Generative AI"
  },
  "2027-05-12": {
    "domain": "statistics",
    "topic": "Jensen-Shannon Divergence"
  },
  "2027-05-13": {
    "domain": "nlp",
    "topic": "Domain Adaptation in NLP"
  },
  "2027-05-14": {
    "domain": "cv",
    "topic": "Scene Understanding"
  },
  "2027-05-15": {
    "domain": "genai",
    "topic": "Evaluation Benchmarks for LLMs"
  },
  "2027-05-19": {
    "domain": "statistics",
    "topic": "Cross-Entropy Loss"
  },
  "2027-05-20": {
    "domain": "nlp",
    "topic": "Knowledge Graphs in NLP"
  },
  "2027-05-21": {
    "domain": "cv",
    "topic": "Anomaly Detection in Images"
  },
  "2027-05-22": {
    "domain": "genai",
    "topic": "Open-Source LLM Ecosystem"
  },
  "2027-05-26": {
    "domain": "statistics",
    "topic": "Logistic Regression Statistical View"
  },
  "2027-05-27": {
    "domain": "nlp",
    "topic": "Entity Linking"
  },
  "2027-05-28": {
    "domain": "cv",
    "topic": "Medical Image Analysis Concepts"
  },
  "2027-05-29": {
    "domain": "genai",
    "topic": "Proprietary vs Open Models"
  },
  "2027-06-02": {
    "domain": "statistics",
    "topic": "Regularization from Bayesian View"
  },
  "2027-06-03": {
    "domain": "nlp",
    "topic": "Coreference Resolution"
  },
  "2027-06-04": {
    "domain": "cv",
    "topic": "Remote Sensing Image Analysis"
  },
  "2027-06-05": {
    "domain": "genai",
    "topic": "Cost Optimization in LLMs"
  },
  "2027-06-09": {
    "domain": "statistics",
    "topic": "Prior & Posterior Distributions"
  },
  "2027-06-10": {
    "domain": "nlp",
    "topic": "Text Clustering"
  },
  "2027-06-11": {
    "domain": "cv",
    "topic": "GANs in Computer Vision"
  },
  "2027-06-12": {
    "domain": "genai",
    "topic": "Latency Optimization in GenAI"
  },
  "2027-06-16": {
    "domain": "statistics",
    "topic": "MAP vs MLE"
  },
  "2027-06-17": {
    "domain": "nlp",
    "topic": "Spam Detection Theory"
  },
  "2027-06-18": {
    "domain": "cv",
    "topic": "Diffusion Models for Images"
  },
  "2027-06-19": {
    "domain": "genai",
    "topic": "Model Versioning in GenAI"
  },
  "2027-06-23": {
    "domain": "statistics",
    "topic": "Expectation & Variance"
  },
  "2027-06-24": {
    "domain": "nlp",
    "topic": "Fake News Detection Concepts"
  },
  "2027-06-25": {
    "domain": "cv",
    "topic": "Image-to-Image Translation"
  },
  "2027-06-26": {
    "domain": "genai",
    "topic": "Monitoring Generative Systems"
  },
  "2027-06-30": {
    "domain": "statistics",
    "topic": "Covariance Matrix"
  },
  "2027-07-01": {
    "domain": "nlp",
    "topic": "Toxicity Detection Models"
  },
  "2027-07-02": {
    "domain": "cv",
    "topic": "Style Transfer"
  },
  "2027-07-03": {
    "domain": "genai",
    "topic": "Drift Detection in GenAI"
  },
  "2027-07-07": {
    "domain": "statistics",
    "topic": "Eigenvalues & Eigenvectors in ML"
  },
  "2027-07-08": {
    "domain": "nlp",
    "topic": "Intent Classification"
  },
  "2027-07-09": {
    "domain": "cv",
    "topic": "Neural Rendering"
  },
  "2027-07-10": {
    "domain": "genai",
    "topic": "Explainability in Generative Models"
  },
  "2027-07-14": {
    "domain": "statistics",
    "topic": "Singular Value Decomposition"
  },
  "2027-07-15": {
    "domain": "nlp",
    "topic": "Slot Filling"
  },
  "2027-07-16": {
    "domain": "cv",
    "topic": "NeRF Basics"
  },
  "2027-07-17": {
    "domain": "genai",
    "topic": "Uncertainty in Generative Models"
  },
  "2027-07-21": {
    "domain": "statistics",
    "topic": "Dimensionality Reduction Statistical View"
  },
  "2027-07-22": {
    "domain": "nlp",
    "topic": "Dialogue System Fundamentals"
  },
  "2027-07-23": {
    "domain": "cv",
    "topic": "Vision-Language Models"
  },
  "2027-07-24": {
    "domain": "genai",
    "topic": "Calibration of LLM Outputs"
  },
  "2027-07-28": {
    "domain": "statistics",
    "topic": "Gaussian Mixture Models Theory"
  },
  "2027-07-29": {
    "domain": "nlp",
    "topic": "Reinforcement Learning for NLP"
  },
  "2027-07-30": {
    "domain": "cv",
    "topic": "CLIP Model Overview"
  },
  "2027-07-31": {
    "domain": "genai",
    "topic": "Ethical Frameworks for GenAI"
  },
  "2027-08-04": {
    "domain": "statistics",
    "topic": "Expectation Maximization Algorithm"
  },
  "2027-08-05": {
    "domain": "nlp",
    "topic": "Continual Learning in NLP"
  },
  "2027-08-06": {
    "domain": "cv",
    "topic": "Robustness in Vision Systems"
  },
  "2027-08-07": {
    "domain": "genai",
    "topic": "Copyright and IP in GenAI"
  },
  "2027-08-11": {
    "domain": "statistics",
    "topic": "Markov Chains Basics"
  },
  "2027-08-12": {
    "domain": "nlp",
    "topic": "Privacy and Security in NLP"
  },
  "2027-08-13": {
    "domain": "cv",
    "topic": "Bias and Fairness in Vision"
  },
  "2027-08-14": {
    "domain": "genai",
    "topic": "Privacy Concerns in Generative AI"
  },
  "2027-08-18": {
    "domain": "statistics",
    "topic": "Hidden Markov Models"
  },
  "2027-08-19": {
    "domain": "nlp",
    "topic": "Ethics in NLP"
  },
  "2027-08-20": {
    "domain": "cv",
    "topic": "Uncertainty in Vision Models"
  },
  "2027-08-21": {
    "domain": "genai",
    "topic": "Federated Generative Models"
  },
  "2027-08-25": {
    "domain": "statistics",
    "topic": "Model Selection Criteria (AIC/BIC)"
  },
  "2027-08-26": {
    "domain": "nlp",
    "topic": "Distribution Shift in NLP"
  },
  "2027-08-27": {
    "domain": "cv",
    "topic": "Calibration in Vision"
  },
  "2027-08-28": {
    "domain": "genai",
    "topic": "Continual Learning in LLMs"
  },
  "2027-09-01": {
    "domain": "statistics",
    "topic": "Likelihood Ratio Test"
  },
  "2027-09-02": {
    "domain": "nlp",
    "topic": "Uncertainty in Language Models"
  },
  "2027-09-03": {
    "domain": "cv",
    "topic": "Distribution Shift in Vision"
  },
  "2027-09-04": {
    "domain": "genai",
    "topic": "Multimodal Fusion Strategies"
  },
  "2027-09-08": {
    "domain": "statistics",
    "topic": "Non-Parametric Statistics"
  },
  "2027-09-09": {
    "domain": "nlp",
    "topic": "Calibration in NLP"
  },
  "2027-09-10": {
    "domain": "cv",
    "topic": "Concept Drift in Vision"
  },
  "2027-09-11": {
    "domain": "genai",
    "topic": "Cross-Lingual Generative Models"
  },
  "2027-09-15": {
    "domain": "statistics",
    "topic": "Kernel Density Estimation"
  },
  "2027-09-16": {
    "domain": "nlp",
    "topic": "Adversarial Attacks in NLP"
  },
  "2027-09-17": {
    "domain": "cv",
    "topic": "Large-Scale Vision Training"
  },
  "2027-09-18": {
    "domain": "genai",
    "topic": "Foundation Models Overview"
  },
  "2027-09-22": {
    "domain": "statistics",
    "topic": "Robust Statistics"
  },
  "2027-09-23": {
    "domain": "nlp",
    "topic": "Adversarial Defense Techniques"
  },
  "2027-09-24": {
    "domain": "cv",
    "topic": "Data-Centric Vision"
  },
  "2027-09-25": {
    "domain": "genai",
    "topic": "Alignment Research Directions"
  },
  "2027-09-29": {
    "domain": "statistics",
    "topic": "Distribution Shift"
  },
  "2027-09-30": {
    "domain": "nlp",
    "topic": "Contrastive Learning in NLP"
  },
  "2027-10-01": {
    "domain": "cv",
    "topic": "Vision Benchmark Datasets"
  },
  "2027-10-02": {
    "domain": "genai",
    "topic": "Emerging Trends in Diffusion Models"
  },
  "2027-10-06": {
    "domain": "statistics",
    "topic": "Concept Drift"
  },
  "2027-10-07": {
    "domain": "nlp",
    "topic": "Self-Supervised Learning in NLP"
  },
  "2027-10-08": {
    "domain": "cv",
    "topic": "ImageNet and COCO Overview"
  },
  "2027-10-09": {
    "domain": "genai",
    "topic": "Scaling Beyond Trillion Parameters"
  },
  "2027-10-13": {
    "domain": "statistics",
    "topic": "Statistical Monitoring in Production"
  },
  "2027-10-14": {
    "domain": "nlp",
    "topic": "Parameter-Efficient Fine-Tuning"
  },
  "2027-10-15": {
    "domain": "cv",
    "topic": "Model Scaling Laws in Vision"
  },
  "2027-10-16": {
    "domain": "genai",
    "topic": "Neurosymbolic Generative AI"
  },
  "2027-10-20": {
    "domain": "statistics",
    "topic": "Fairness Metrics in ML"
  },
  "2027-10-21": {
    "domain": "nlp",
    "topic": "LoRA for NLP"
  },
  "2027-10-22": {
    "domain": "cv",
    "topic": "Transformers vs CNNs"
  },
  "2027-10-23": {
    "domain": "genai",
    "topic": "Cognitive Architectures in AI"
  },
  "2027-10-27": {
    "domain": "statistics",
    "topic": "Uncertainty Quantification"
  },
  "2027-10-28": {
    "domain": "nlp",
    "topic": "Model Scaling Laws"
  },
  "2027-10-29": {
    "domain": "cv",
    "topic": "Hybrid Vision Architectures"
  },
  "2027-10-30": {
    "domain": "genai",
    "topic": "Autonomous AI Systems"
  },
  "2027-11-03": {
    "domain": "statistics",
    "topic": "Prediction Intervals"
  },
  "2027-11-04": {
    "domain": "nlp",
    "topic": "Large Language Model Fundamentals"
  },
  "2027-11-05": {
    "domain": "cv",
    "topic": "Continual Learning in Vision"
  },
  "2027-11-06": {
    "domain": "genai",
    "topic": "Human-AI Collaboration Models"
  },
  "2027-11-10": {
    "domain": "statistics",
    "topic": "Bayesian Networks"
  },
  "2027-11-11": {
    "domain": "nlp",
    "topic": "Retrieval-Augmented Generation Concepts"
  },
  "2027-11-12": {
    "domain": "cv",
    "topic": "Privacy in Vision Systems"
  },
  "2027-11-13": {
    "domain": "genai",
    "topic": "Evaluation Frameworks for GenAI"
  },
  "2027-11-17": {
    "domain": "statistics",
    "topic": "Hierarchical Models"
  },
  "2027-11-18": {
    "domain": "nlp",
    "topic": "Evaluation Frameworks for LLMs"
  },
  "2027-11-19": {
    "domain": "cv",
    "topic": "Ethics in Computer Vision"
  },
  "2027-11-20": {
    "domain": "genai",
    "topic": "Advanced Prompting Paradigms"
  },
  "2027-11-24": {
    "domain": "statistics",
    "topic": "Survival Analysis Basics"
  },
  "2027-11-25": {
    "domain": "nlp",
    "topic": "Data-Centric NLP"
  },
  "2027-11-26": {
    "domain": "cv",
    "topic": "Future Trends in Computer Vision"
  },
  "2027-11-27": {
    "domain": "genai",
    "topic": "Theoretical Foundations of Generative Modeling"
  },
  "2027-12-01": {
    "domain": "statistics",
    "topic": "Hazard Functions"
  },
  "2027-12-02": {
    "domain": "nlp",
    "topic": "Robustness in NLP"
  },
  "2027-12-03": {
    "domain": "cv",
    "topic": "Advanced Topics in Vision Theory"
  },
  "2027-12-04": {
    "domain": "genai",
    "topic": "Information Theory in Generative AI"
  },
  "2027-12-08": {
    "domain": "statistics",
    "topic": "Statistical Learning Theory Basics"
  },
  "2027-12-09": {
    "domain": "nlp",
    "topic": "Fairness Metrics in NLP"
  },
  "2027-12-10": {
    "domain": "cv",
    "topic": "Research Directions in Computer Vision"
  },
  "2027-12-11": {
    "domain": "genai",
    "topic": "Optimization Challenges in LLMs"
  },
  "2027-12-15": {
    "domain": "statistics",
    "topic": "VC Dimension"
  },
  "2027-12-16": {
    "domain": "nlp",
    "topic": "Statistical Learning Theory for NLP"
  },
  "2027-12-17": {
    "domain": "cv",
    "topic": "Statistical Foundations of Vision Models"
  },
  "2027-12-18": {
    "domain": "genai",
    "topic": "Energy Efficiency in Large Models"
  },
  "2027-12-22": {
    "domain": "statistics",
    "topic": "PAC Learning"
  },
  "2027-12-23": {
    "domain": "nlp",
    "topic": "Information Theory in NLP"
  },
  "2027-12-24": {
    "domain": "cv",
    "topic": "Optimization Techniques in Vision"
  },
  "2027-12-25": {
    "domain": "genai",
    "topic": "Sustainability in AI Systems"
  },
  "2027-12-29": {
    "domain": "statistics",
    "topic": "Bias-Variance Decomposition (Statistical View)"
  },
  "2027-12-30": {
    "domain": "nlp",
    "topic": "Future Research Directions in NLP"
  },
  "2027-12-31": {
    "domain": "cv",
    "topic": "Evaluation Frameworks in Vision"
  },
  "2028-01-01": {
    "domain": "genai",
    "topic": "Future of Generative AI"
  },
  "2028-01-05": {
    "domain": "statistics",
    "topic": "End-to-End Statistical Thinking in ML"
  },
  "2028-01-06": {
    "domain": "nlp",
    "topic": "Advanced Topics in NLP Theory"
  },
  "2028-01-07": {
    "domain": "cv",
    "topic": "Theoretical Limits of Vision Models"
  },
  "2028-01-08": {
    "domain": "genai",
    "topic": "Research Frontiers in Foundation Models"
  }
}
```

## File: `backend/config/__init__.py`
```python
# backend/config/__init__.py
```

## File: `backend/config/config.py`
```python
from typing import Dict
from pathlib import Path

DOMAIN_MAP: Dict[str, str] = {
    "machine_learning.json": "ml",
    "deep_learning.json": "dl",
    "statistics.json": "statistics",
    "natural_language_processing.json": "nlp",
    "computer_vision.json": "cv",
    "generative_ai.json": "genai"
    }

CATEGORY_META: Dict[str, Dict[str, str]] = {
    "ml": {"label": "Machine Learning", "shortLabel": "ML"},
    "dl": {"label": "Deep Learning", "shortLabel": "DL"},
    "nlp": {"label": "Natural Language Processing", "shortLabel": "NLP"},
    "cv": {"label": "Computer Vision", "shortLabel": "CV"},
    "genai": {"label": "Generative AI", "shortLabel": "Gen AI"},
    "ainews": {"label": "AI News", "shortLabel": "AI News"},
    "statistics": {"label": "Statistics for AI", "shortLabel": "Stats"}
}

MODEL: str = "llama-3.3-70b-versatile"
TEMPERATURE: float = 1.0
MAX_TOKENS:  int   = 4096
WORDS_PER_MINUTE: int = 200

BACKEND_DIR: Path = Path(__file__).parent.parent
ROOT_DIR:    Path = BACKEND_DIR.parent
INPUT_DIR:     Path = BACKEND_DIR / "data" / "input"
SCHEDULE_FILE: Path = BACKEND_DIR / "schedule.json"
PROMPT_DIRECTORY: Path = BACKEND_DIR / "prompts"
BLOGS_DIR: Path = ROOT_DIR / "frontend" / "blogs"
```

## File: `backend/data/input/computer_vision.json`
```json
[
    {
        "date": "2026-03-06",
        "topic": "Introduction to Computer Vision"
    },
    {
        "date": "2026-03-13",
        "topic": "Digital Image Fundamentals"
    },
    {
        "date": "2026-03-20",
        "topic": "Image Representation and Color Spaces"
    },
    {
        "date": "2026-03-27",
        "topic": "Image Filtering and Convolution"
    },
    {
        "date": "2026-04-03",
        "topic": "Edge Detection Techniques"
    },
    {
        "date": "2026-04-10",
        "topic": "Histogram Equalization"
    },
    {
        "date": "2026-04-17",
        "topic": "Image Thresholding"
    },
    {
        "date": "2026-04-24",
        "topic": "Morphological Operations"
    },
    {
        "date": "2026-05-01",
        "topic": "Feature Detection and Description"
    },
    {
        "date": "2026-05-08",
        "topic": "SIFT and SURF"
    },
    {
        "date": "2026-05-15",
        "topic": "ORB Features"
    },
    {
        "date": "2026-05-22",
        "topic": "Image Segmentation Basics"
    },
    {
        "date": "2026-05-29",
        "topic": "K-Means for Image Segmentation"
    },
    {
        "date": "2026-06-05",
        "topic": "Hough Transform"
    },
    {
        "date": "2026-06-12",
        "topic": "Template Matching"
    },
    {
        "date": "2026-06-19",
        "topic": "Optical Flow"
    },
    {
        "date": "2026-06-26",
        "topic": "Object Detection Fundamentals"
    },
    {
        "date": "2026-07-03",
        "topic": "Region-Based CNN"
    },
    {
        "date": "2026-07-10",
        "topic": "Fast and Faster R-CNN"
    },
    {
        "date": "2026-07-17",
        "topic": "YOLO Architecture"
    },
    {
        "date": "2026-07-24",
        "topic": "SSD Object Detection"
    },
    {
        "date": "2026-07-31",
        "topic": "Image Classification with CNNs"
    },
    {
        "date": "2026-08-07",
        "topic": "Transfer Learning in Vision"
    },
    {
        "date": "2026-08-14",
        "topic": "ResNet Architecture"
    },
    {
        "date": "2026-08-21",
        "topic": "DenseNet Overview"
    },
    {
        "date": "2026-08-28",
        "topic": "EfficientNet"
    },
    {
        "date": "2026-09-04",
        "topic": "Vision Transformers"
    },
    {
        "date": "2026-09-11",
        "topic": "Self-Attention in Vision"
    },
    {
        "date": "2026-09-18",
        "topic": "Semantic Segmentation"
    },
    {
        "date": "2026-09-25",
        "topic": "U-Net Architecture"
    },
    {
        "date": "2026-10-02",
        "topic": "Instance Segmentation"
    },
    {
        "date": "2026-10-09",
        "topic": "Mask R-CNN"
    },
    {
        "date": "2026-10-16",
        "topic": "Pose Estimation"
    },
    {
        "date": "2026-10-23",
        "topic": "3D Computer Vision Basics"
    },
    {
        "date": "2026-10-30",
        "topic": "Stereo Vision"
    },
    {
        "date": "2026-11-06",
        "topic": "Structure from Motion"
    },
    {
        "date": "2026-11-13",
        "topic": "Image Augmentation Techniques"
    },
    {
        "date": "2026-11-20",
        "topic": "Data Annotation in Vision"
    },
    {
        "date": "2026-11-27",
        "topic": "Evaluation Metrics in Vision"
    },
    {
        "date": "2026-12-04",
        "topic": "Intersection over Union"
    },
    {
        "date": "2026-12-11",
        "topic": "Mean Average Precision"
    },
    {
        "date": "2026-12-18",
        "topic": "Adversarial Attacks in Vision"
    },
    {
        "date": "2026-12-25",
        "topic": "Adversarial Defense Methods"
    },
    {
        "date": "2027-01-01",
        "topic": "Explainability in Vision Models"
    },
    {
        "date": "2027-01-08",
        "topic": "Grad-CAM"
    },
    {
        "date": "2027-01-15",
        "topic": "Model Compression in Vision"
    },
    {
        "date": "2027-01-22",
        "topic": "Quantization in Vision Models"
    },
    {
        "date": "2027-01-29",
        "topic": "Pruning CNNs"
    },
    {
        "date": "2027-02-05",
        "topic": "Knowledge Distillation in Vision"
    },
    {
        "date": "2027-02-12",
        "topic": "Self-Supervised Learning in Vision"
    },
    {
        "date": "2027-02-19",
        "topic": "Contrastive Learning in Vision"
    },
    {
        "date": "2027-02-26",
        "topic": "Few-Shot Learning in Vision"
    },
    {
        "date": "2027-03-05",
        "topic": "Zero-Shot Learning in Vision"
    },
    {
        "date": "2027-03-12",
        "topic": "Domain Adaptation in Vision"
    },
    {
        "date": "2027-03-19",
        "topic": "Federated Learning in Vision"
    },
    {
        "date": "2027-03-26",
        "topic": "Edge AI for Vision"
    },
    {
        "date": "2027-04-02",
        "topic": "ONNX for Vision Models"
    },
    {
        "date": "2027-04-09",
        "topic": "TensorRT Optimization"
    },
    {
        "date": "2027-04-16",
        "topic": "Video Analysis Basics"
    },
    {
        "date": "2027-04-23",
        "topic": "Action Recognition"
    },
    {
        "date": "2027-04-30",
        "topic": "Object Tracking"
    },
    {
        "date": "2027-05-07",
        "topic": "Multi-Object Tracking"
    },
    {
        "date": "2027-05-14",
        "topic": "Scene Understanding"
    },
    {
        "date": "2027-05-21",
        "topic": "Anomaly Detection in Images"
    },
    {
        "date": "2027-05-28",
        "topic": "Medical Image Analysis Concepts"
    },
    {
        "date": "2027-06-04",
        "topic": "Remote Sensing Image Analysis"
    },
    {
        "date": "2027-06-11",
        "topic": "GANs in Computer Vision"
    },
    {
        "date": "2027-06-18",
        "topic": "Diffusion Models for Images"
    },
    {
        "date": "2027-06-25",
        "topic": "Image-to-Image Translation"
    },
    {
        "date": "2027-07-02",
        "topic": "Style Transfer"
    },
    {
        "date": "2027-07-09",
        "topic": "Neural Rendering"
    },
    {
        "date": "2027-07-16",
        "topic": "NeRF Basics"
    },
    {
        "date": "2027-07-23",
        "topic": "Vision-Language Models"
    },
    {
        "date": "2027-07-30",
        "topic": "CLIP Model Overview"
    },
    {
        "date": "2027-08-06",
        "topic": "Robustness in Vision Systems"
    },
    {
        "date": "2027-08-13",
        "topic": "Bias and Fairness in Vision"
    },
    {
        "date": "2027-08-20",
        "topic": "Uncertainty in Vision Models"
    },
    {
        "date": "2027-08-27",
        "topic": "Calibration in Vision"
    },
    {
        "date": "2027-09-03",
        "topic": "Distribution Shift in Vision"
    },
    {
        "date": "2027-09-10",
        "topic": "Concept Drift in Vision"
    },
    {
        "date": "2027-09-17",
        "topic": "Large-Scale Vision Training"
    },
    {
        "date": "2027-09-24",
        "topic": "Data-Centric Vision"
    },
    {
        "date": "2027-10-01",
        "topic": "Vision Benchmark Datasets"
    },
    {
        "date": "2027-10-08",
        "topic": "ImageNet and COCO Overview"
    },
    {
        "date": "2027-10-15",
        "topic": "Model Scaling Laws in Vision"
    },
    {
        "date": "2027-10-22",
        "topic": "Transformers vs CNNs"
    },
    {
        "date": "2027-10-29",
        "topic": "Hybrid Vision Architectures"
    },
    {
        "date": "2027-11-05",
        "topic": "Continual Learning in Vision"
    },
    {
        "date": "2027-11-12",
        "topic": "Privacy in Vision Systems"
    },
    {
        "date": "2027-11-19",
        "topic": "Ethics in Computer Vision"
    },
    {
        "date": "2027-11-26",
        "topic": "Future Trends in Computer Vision"
    },
    {
        "date": "2027-12-03",
        "topic": "Advanced Topics in Vision Theory"
    },
    {
        "date": "2027-12-10",
        "topic": "Research Directions in Computer Vision"
    },
    {
        "date": "2027-12-17",
        "topic": "Statistical Foundations of Vision Models"
    },
    {
        "date": "2027-12-24",
        "topic": "Optimization Techniques in Vision"
    },
    {
        "date": "2027-12-31",
        "topic": "Evaluation Frameworks in Vision"
    },
    {
        "date": "2028-01-07",
        "topic": "Theoretical Limits of Vision Models"
    }
]
```

## File: `backend/data/input/deep_learning.json`
```json
[
    {
        "date": "2026-03-03",
        "topic": "Introduction to Deep Learning",
        "subtopics": "What is Deep Learning, Why use, Example Applications, and its types"
    }
]
```

## File: `backend/data/input/generative_ai.json`
```json
[
    {
        "date": "2026-03-07",
        "topic": "Introduction to Generative AI"
    },
    {
        "date": "2026-03-14",
        "topic": "History of Generative Models"
    },
    {
        "date": "2026-03-21",
        "topic": "Probabilistic Generative Modeling"
    },
    {
        "date": "2026-03-28",
        "topic": "Autoregressive Models"
    },
    {
        "date": "2026-04-04",
        "topic": "Energy-Based Models"
    },
    {
        "date": "2026-04-11",
        "topic": "Variational Autoencoders"
    },
    {
        "date": "2026-04-18",
        "topic": "GAN Fundamentals"
    },
    {
        "date": "2026-04-25",
        "topic": "GAN Training Challenges"
    },
    {
        "date": "2026-05-02",
        "topic": "Conditional GANs"
    },
    {
        "date": "2026-05-09",
        "topic": "CycleGAN"
    },
    {
        "date": "2026-05-16",
        "topic": "Diffusion Model Basics"
    },
    {
        "date": "2026-05-23",
        "topic": "Denoising Diffusion Probabilistic Models"
    },
    {
        "date": "2026-05-30",
        "topic": "Latent Diffusion Models"
    },
    {
        "date": "2026-06-06",
        "topic": "Score-Based Generative Models"
    },
    {
        "date": "2026-06-13",
        "topic": "Normalizing Flows"
    },
    {
        "date": "2026-06-20",
        "topic": "Transformer Architecture for Generation"
    },
    {
        "date": "2026-06-27",
        "topic": "Large Language Model Fundamentals"
    },
    {
        "date": "2026-07-04",
        "topic": "Pretraining Objectives in LLMs"
    },
    {
        "date": "2026-07-11",
        "topic": "Causal vs Masked Language Models"
    },
    {
        "date": "2026-07-18",
        "topic": "Scaling Laws in LLMs"
    },
    {
        "date": "2026-07-25",
        "topic": "Fine-Tuning Strategies"
    },
    {
        "date": "2026-08-01",
        "topic": "Instruction Tuning"
    },
    {
        "date": "2026-08-08",
        "topic": "Reinforcement Learning from Human Feedback"
    },
    {
        "date": "2026-08-15",
        "topic": "Direct Preference Optimization"
    },
    {
        "date": "2026-08-22",
        "topic": "Parameter-Efficient Fine-Tuning"
    },
    {
        "date": "2026-08-29",
        "topic": "LoRA and Adapters"
    },
    {
        "date": "2026-09-05",
        "topic": "Prompt Engineering Principles"
    },
    {
        "date": "2026-09-12",
        "topic": "Chain-of-Thought Prompting"
    },
    {
        "date": "2026-09-19",
        "topic": "Few-Shot and Zero-Shot Prompting"
    },
    {
        "date": "2026-09-26",
        "topic": "Retrieval-Augmented Generation"
    },
    {
        "date": "2026-10-03",
        "topic": "Vector Databases in GenAI"
    },
    {
        "date": "2026-10-10",
        "topic": "Embedding Models"
    },
    {
        "date": "2026-10-17",
        "topic": "Text-to-Image Generation"
    },
    {
        "date": "2026-10-24",
        "topic": "Image-to-Image Generation"
    },
    {
        "date": "2026-10-31",
        "topic": "Text-to-Video Generation"
    },
    {
        "date": "2026-11-07",
        "topic": "Multimodal Generative Models"
    },
    {
        "date": "2026-11-14",
        "topic": "Vision-Language Models"
    },
    {
        "date": "2026-11-21",
        "topic": "Audio Generation Models"
    },
    {
        "date": "2026-11-28",
        "topic": "Speech Synthesis Models"
    },
    {
        "date": "2026-12-05",
        "topic": "Music Generation Models"
    },
    {
        "date": "2026-12-12",
        "topic": "Evaluation of Generative Models"
    },
    {
        "date": "2026-12-19",
        "topic": "Perplexity and FID Score"
    },
    {
        "date": "2026-12-26",
        "topic": "Hallucination in LLMs"
    },
    {
        "date": "2027-01-02",
        "topic": "Bias and Fairness in GenAI"
    },
    {
        "date": "2027-01-09",
        "topic": "Safety Alignment Techniques"
    },
    {
        "date": "2027-01-16",
        "topic": "Red Teaming for LLMs"
    },
    {
        "date": "2027-01-23",
        "topic": "Adversarial Attacks on Generative Models"
    },
    {
        "date": "2027-01-30",
        "topic": "Model Robustness in GenAI"
    },
    {
        "date": "2027-02-06",
        "topic": "Knowledge Distillation for LLMs"
    },
    {
        "date": "2027-02-13",
        "topic": "Quantization of Large Models"
    },
    {
        "date": "2027-02-20",
        "topic": "Pruning Large Language Models"
    },
    {
        "date": "2027-02-27",
        "topic": "Distributed Training of LLMs"
    },
    {
        "date": "2027-03-06",
        "topic": "Mixture of Experts Models"
    },
    {
        "date": "2027-03-13",
        "topic": "Sparse Transformers"
    },
    {
        "date": "2027-03-20",
        "topic": "Memory-Augmented Models"
    },
    {
        "date": "2027-03-27",
        "topic": "Long-Context Modeling"
    },
    {
        "date": "2027-04-03",
        "topic": "Agentic AI Concepts"
    },
    {
        "date": "2027-04-10",
        "topic": "Tool-Calling in LLMs"
    },
    {
        "date": "2027-04-17",
        "topic": "Planning and Reasoning in LLMs"
    },
    {
        "date": "2027-04-24",
        "topic": "Self-Reflection in LLMs"
    },
    {
        "date": "2027-05-01",
        "topic": "Synthetic Data Generation"
    },
    {
        "date": "2027-05-08",
        "topic": "Data-Centric Generative AI"
    },
    {
        "date": "2027-05-15",
        "topic": "Evaluation Benchmarks for LLMs"
    },
    {
        "date": "2027-05-22",
        "topic": "Open-Source LLM Ecosystem"
    },
    {
        "date": "2027-05-29",
        "topic": "Proprietary vs Open Models"
    },
    {
        "date": "2027-06-05",
        "topic": "Cost Optimization in LLMs"
    },
    {
        "date": "2027-06-12",
        "topic": "Latency Optimization in GenAI"
    },
    {
        "date": "2027-06-19",
        "topic": "Model Versioning in GenAI"
    },
    {
        "date": "2027-06-26",
        "topic": "Monitoring Generative Systems"
    },
    {
        "date": "2027-07-03",
        "topic": "Drift Detection in GenAI"
    },
    {
        "date": "2027-07-10",
        "topic": "Explainability in Generative Models"
    },
    {
        "date": "2027-07-17",
        "topic": "Uncertainty in Generative Models"
    },
    {
        "date": "2027-07-24",
        "topic": "Calibration of LLM Outputs"
    },
    {
        "date": "2027-07-31",
        "topic": "Ethical Frameworks for GenAI"
    },
    {
        "date": "2027-08-07",
        "topic": "Copyright and IP in GenAI"
    },
    {
        "date": "2027-08-14",
        "topic": "Privacy Concerns in Generative AI"
    },
    {
        "date": "2027-08-21",
        "topic": "Federated Generative Models"
    },
    {
        "date": "2027-08-28",
        "topic": "Continual Learning in LLMs"
    },
    {
        "date": "2027-09-04",
        "topic": "Multimodal Fusion Strategies"
    },
    {
        "date": "2027-09-11",
        "topic": "Cross-Lingual Generative Models"
    },
    {
        "date": "2027-09-18",
        "topic": "Foundation Models Overview"
    },
    {
        "date": "2027-09-25",
        "topic": "Alignment Research Directions"
    },
    {
        "date": "2027-10-02",
        "topic": "Emerging Trends in Diffusion Models"
    },
    {
        "date": "2027-10-09",
        "topic": "Scaling Beyond Trillion Parameters"
    },
    {
        "date": "2027-10-16",
        "topic": "Neurosymbolic Generative AI"
    },
    {
        "date": "2027-10-23",
        "topic": "Cognitive Architectures in AI"
    },
    {
        "date": "2027-10-30",
        "topic": "Autonomous AI Systems"
    },
    {
        "date": "2027-11-06",
        "topic": "Human-AI Collaboration Models"
    },
    {
        "date": "2027-11-13",
        "topic": "Evaluation Frameworks for GenAI"
    },
    {
        "date": "2027-11-20",
        "topic": "Advanced Prompting Paradigms"
    },
    {
        "date": "2027-11-27",
        "topic": "Theoretical Foundations of Generative Modeling"
    },
    {
        "date": "2027-12-04",
        "topic": "Information Theory in Generative AI"
    },
    {
        "date": "2027-12-11",
        "topic": "Optimization Challenges in LLMs"
    },
    {
        "date": "2027-12-18",
        "topic": "Energy Efficiency in Large Models"
    },
    {
        "date": "2027-12-25",
        "topic": "Sustainability in AI Systems"
    },
    {
        "date": "2028-01-01",
        "topic": "Future of Generative AI"
    },
    {
        "date": "2028-01-08",
        "topic": "Research Frontiers in Foundation Models"
    }
]
```

## File: `backend/data/input/machine_learning.json`
```json
[
    {
        "date": "2026-03-02",
        "topic": "What is Machine Learning?",
        "subtopics": "What is Machine Learning, Why use, Example Applications, Intro to ML Systems and its types"
    },
    {
        "date": "2026-03-09",
        "topic": "Main Challenges of Machine Learning",
        "subtopics": ""
    },
    {
        "date": "2026-03-16",
        "topic": "Life Cycle of Machine Learning Project",
        "subtopics": ""
    },
    {
        "date": "2026-03-23",
        "topic": "Supervised Machine Learning - Classfication",
        "subtopics": ""
    },
    {
        "date": "2026-03-30",
        "topic": "Supervised Machine Learning - Regression",
        "subtopics": ""
    },
    {
        "date": "2026-04-06",
        "topic": "Unsupervised Machine Learning - Clustering",
        "subtopics": ""
    }
]
```

## File: `backend/data/input/natural_language_processing.json`
```json
[
    {
        "date": "2026-03-05",
        "topic": "Introduction to NLP"
    },
    {
        "date": "2026-03-12",
        "topic": "Text Preprocessing Techniques"
    },
    {
        "date": "2026-03-19",
        "topic": "Tokenization Methods"
    },
    {
        "date": "2026-03-26",
        "topic": "Stopwords and Text Cleaning"
    },
    {
        "date": "2026-04-02",
        "topic": "Stemming and Lemmatization"
    },
    {
        "date": "2026-04-09",
        "topic": "Regular Expressions for Text"
    },
    {
        "date": "2026-04-16",
        "topic": "Bag of Words Model"
    },
    {
        "date": "2026-04-23",
        "topic": "TF-IDF Representation"
    },
    {
        "date": "2026-04-30",
        "topic": "N-grams and Language Modeling"
    },
    {
        "date": "2026-05-07",
        "topic": "Word Embeddings Overview"
    },
    {
        "date": "2026-05-14",
        "topic": "Word2Vec Architecture"
    },
    {
        "date": "2026-05-21",
        "topic": "GloVe Embeddings"
    },
    {
        "date": "2026-05-28",
        "topic": "FastText Model"
    },
    {
        "date": "2026-06-04",
        "topic": "Contextual Embeddings"
    },
    {
        "date": "2026-06-11",
        "topic": "Sentence and Document Embeddings"
    },
    {
        "date": "2026-06-18",
        "topic": "Similarity Measures in NLP"
    },
    {
        "date": "2026-06-25",
        "topic": "Text Classification Fundamentals"
    },
    {
        "date": "2026-07-02",
        "topic": "Naive Bayes for NLP"
    },
    {
        "date": "2026-07-09",
        "topic": "Logistic Regression for Text"
    },
    {
        "date": "2026-07-16",
        "topic": "Evaluation Metrics in NLP"
    },
    {
        "date": "2026-07-23",
        "topic": "Topic Modeling Concepts"
    },
    {
        "date": "2026-07-30",
        "topic": "Latent Dirichlet Allocation"
    },
    {
        "date": "2026-08-06",
        "topic": "Named Entity Recognition"
    },
    {
        "date": "2026-08-13",
        "topic": "Part-of-Speech Tagging"
    },
    {
        "date": "2026-08-20",
        "topic": "Dependency Parsing"
    },
    {
        "date": "2026-08-27",
        "topic": "Hidden Markov Models in NLP"
    },
    {
        "date": "2026-09-03",
        "topic": "Conditional Random Fields"
    },
    {
        "date": "2026-09-10",
        "topic": "Recurrent Neural Networks for NLP"
    },
    {
        "date": "2026-09-17",
        "topic": "LSTM for Sequence Modeling"
    },
    {
        "date": "2026-09-24",
        "topic": "GRU Networks"
    },
    {
        "date": "2026-10-01",
        "topic": "Attention Mechanism"
    },
    {
        "date": "2026-10-08",
        "topic": "Transformers Architecture"
    },
    {
        "date": "2026-10-15",
        "topic": "Self-Attention Deep Dive"
    },
    {
        "date": "2026-10-22",
        "topic": "BERT Model Overview"
    },
    {
        "date": "2026-10-29",
        "topic": "GPT Model Overview"
    },
    {
        "date": "2026-11-05",
        "topic": "Pretraining vs Fine-Tuning"
    },
    {
        "date": "2026-11-12",
        "topic": "Transfer Learning in NLP"
    },
    {
        "date": "2026-11-19",
        "topic": "Text Generation Concepts"
    },
    {
        "date": "2026-11-26",
        "topic": "Sequence-to-Sequence Models"
    },
    {
        "date": "2026-12-03",
        "topic": "Beam Search and Decoding"
    },
    {
        "date": "2026-12-10",
        "topic": "Perplexity in Language Models"
    },
    {
        "date": "2026-12-17",
        "topic": "BLEU and ROUGE Metrics"
    },
    {
        "date": "2026-12-24",
        "topic": "Sentiment Analysis Theory"
    },
    {
        "date": "2026-12-31",
        "topic": "Aspect-Based Sentiment Analysis"
    },
    {
        "date": "2027-01-07",
        "topic": "Text Summarization Techniques"
    },
    {
        "date": "2027-01-14",
        "topic": "Machine Translation Fundamentals"
    },
    {
        "date": "2027-01-21",
        "topic": "Information Retrieval Basics"
    },
    {
        "date": "2027-01-28",
        "topic": "BM25 Algorithm"
    },
    {
        "date": "2027-02-04",
        "topic": "Semantic Search Concepts"
    },
    {
        "date": "2027-02-11",
        "topic": "Vector Representations for Search"
    },
    {
        "date": "2027-02-18",
        "topic": "Cross-Lingual NLP"
    },
    {
        "date": "2027-02-25",
        "topic": "Multilingual Language Models"
    },
    {
        "date": "2027-03-04",
        "topic": "Zero-Shot and Few-Shot Learning"
    },
    {
        "date": "2027-03-11",
        "topic": "Prompting Techniques"
    },
    {
        "date": "2027-03-18",
        "topic": "Hallucination in Language Models"
    },
    {
        "date": "2027-03-25",
        "topic": "Bias in NLP Models"
    },
    {
        "date": "2027-04-01",
        "topic": "Explainability in NLP"
    },
    {
        "date": "2027-04-08",
        "topic": "Model Compression in NLP"
    },
    {
        "date": "2027-04-15",
        "topic": "Distillation in NLP"
    },
    {
        "date": "2027-04-22",
        "topic": "Quantization Techniques"
    },
    {
        "date": "2027-04-29",
        "topic": "Scaling NLP Models"
    },
    {
        "date": "2027-05-06",
        "topic": "Low-Resource Language Modeling"
    },
    {
        "date": "2027-05-13",
        "topic": "Domain Adaptation in NLP"
    },
    {
        "date": "2027-05-20",
        "topic": "Knowledge Graphs in NLP"
    },
    {
        "date": "2027-05-27",
        "topic": "Entity Linking"
    },
    {
        "date": "2027-06-03",
        "topic": "Coreference Resolution"
    },
    {
        "date": "2027-06-10",
        "topic": "Text Clustering"
    },
    {
        "date": "2027-06-17",
        "topic": "Spam Detection Theory"
    },
    {
        "date": "2027-06-24",
        "topic": "Fake News Detection Concepts"
    },
    {
        "date": "2027-07-01",
        "topic": "Toxicity Detection Models"
    },
    {
        "date": "2027-07-08",
        "topic": "Intent Classification"
    },
    {
        "date": "2027-07-15",
        "topic": "Slot Filling"
    },
    {
        "date": "2027-07-22",
        "topic": "Dialogue System Fundamentals"
    },
    {
        "date": "2027-07-29",
        "topic": "Reinforcement Learning for NLP"
    },
    {
        "date": "2027-08-05",
        "topic": "Continual Learning in NLP"
    },
    {
        "date": "2027-08-12",
        "topic": "Privacy and Security in NLP"
    },
    {
        "date": "2027-08-19",
        "topic": "Ethics in NLP"
    },
    {
        "date": "2027-08-26",
        "topic": "Distribution Shift in NLP"
    },
    {
        "date": "2027-09-02",
        "topic": "Uncertainty in Language Models"
    },
    {
        "date": "2027-09-09",
        "topic": "Calibration in NLP"
    },
    {
        "date": "2027-09-16",
        "topic": "Adversarial Attacks in NLP"
    },
    {
        "date": "2027-09-23",
        "topic": "Adversarial Defense Techniques"
    },
    {
        "date": "2027-09-30",
        "topic": "Contrastive Learning in NLP"
    },
    {
        "date": "2027-10-07",
        "topic": "Self-Supervised Learning in NLP"
    },
    {
        "date": "2027-10-14",
        "topic": "Parameter-Efficient Fine-Tuning"
    },
    {
        "date": "2027-10-21",
        "topic": "LoRA for NLP"
    },
    {
        "date": "2027-10-28",
        "topic": "Model Scaling Laws"
    },
    {
        "date": "2027-11-04",
        "topic": "Large Language Model Fundamentals"
    },
    {
        "date": "2027-11-11",
        "topic": "Retrieval-Augmented Generation Concepts"
    },
    {
        "date": "2027-11-18",
        "topic": "Evaluation Frameworks for LLMs"
    },
    {
        "date": "2027-11-25",
        "topic": "Data-Centric NLP"
    },
    {
        "date": "2027-12-02",
        "topic": "Robustness in NLP"
    },
    {
        "date": "2027-12-09",
        "topic": "Fairness Metrics in NLP"
    },
    {
        "date": "2027-12-16",
        "topic": "Statistical Learning Theory for NLP"
    },
    {
        "date": "2027-12-23",
        "topic": "Information Theory in NLP"
    },
    {
        "date": "2027-12-30",
        "topic": "Future Research Directions in NLP"
    },
    {
        "date": "2028-01-06",
        "topic": "Advanced Topics in NLP Theory"
    }
]
```

## File: `backend/data/input/statistics.json`
```json
[
    {
        "date": "2026-03-04",
        "topic": "Introduction to Statistics for AI & ML",
        "subtopics": "Why Learn Statistics for ai, Applications of Statistics in ai"
    },
    {
        "date": "2026-03-11",
        "topic": "Types of Data in ML"
    },
    {
        "date": "2026-03-18",
        "topic": "Population vs Sample"
    },
    {
        "date": "2026-03-25",
        "topic": "Measures of Central Tendency"
    },
    {
        "date": "2026-04-01",
        "topic": "Measures of Dispersion"
    },
    {
        "date": "2026-04-08",
        "topic": "Probability Basics"
    },
    {
        "date": "2026-04-15",
        "topic": "Conditional Probability"
    },
    {
        "date": "2026-04-22",
        "topic": "Bayes Theorem"
    },
    {
        "date": "2026-04-29",
        "topic": "Random Variables"
    },
    {
        "date": "2026-05-06",
        "topic": "Probability Distributions Overview"
    },
    {
        "date": "2026-05-13",
        "topic": "Normal Distribution"
    },
    {
        "date": "2026-05-20",
        "topic": "Binomial Distribution"
    },
    {
        "date": "2026-05-27",
        "topic": "Poisson Distribution"
    },
    {
        "date": "2026-06-03",
        "topic": "Uniform Distribution"
    },
    {
        "date": "2026-06-10",
        "topic": "Central Limit Theorem"
    },
    {
        "date": "2026-06-17",
        "topic": "Law of Large Numbers"
    },
    {
        "date": "2026-06-24",
        "topic": "Sampling Techniques"
    },
    {
        "date": "2026-07-01",
        "topic": "Sampling Bias"
    },
    {
        "date": "2026-07-08",
        "topic": "Point Estimation"
    },
    {
        "date": "2026-07-15",
        "topic": "Confidence Intervals"
    },
    {
        "date": "2026-07-22",
        "topic": "Hypothesis Testing Basics"
    },
    {
        "date": "2026-07-29",
        "topic": "Null vs Alternative Hypothesis"
    },
    {
        "date": "2026-08-05",
        "topic": "p-value Explained"
    },
    {
        "date": "2026-08-12",
        "topic": "Type I & Type II Errors"
    },
    {
        "date": "2026-08-19",
        "topic": "Z-Test"
    },
    {
        "date": "2026-08-26",
        "topic": "T-Test"
    },
    {
        "date": "2026-09-02",
        "topic": "Chi-Square Test"
    },
    {
        "date": "2026-09-09",
        "topic": "ANOVA"
    },
    {
        "date": "2026-09-16",
        "topic": "Correlation vs Covariance"
    },
    {
        "date": "2026-09-23",
        "topic": "Pearson Correlation"
    },
    {
        "date": "2026-09-30",
        "topic": "Spearman Correlation"
    },
    {
        "date": "2026-10-07",
        "topic": "Regression Assumptions"
    },
    {
        "date": "2026-10-14",
        "topic": "Maximum Likelihood Estimation"
    },
    {
        "date": "2026-10-21",
        "topic": "Log-Likelihood in ML"
    },
    {
        "date": "2026-10-28",
        "topic": "Bias & Variance in Estimation"
    },
    {
        "date": "2026-11-04",
        "topic": "Variance Inflation Factor"
    },
    {
        "date": "2026-11-11",
        "topic": "Multicollinearity"
    },
    {
        "date": "2026-11-18",
        "topic": "Outlier Detection Methods"
    },
    {
        "date": "2026-11-25",
        "topic": "Skewness & Kurtosis"
    },
    {
        "date": "2026-12-02",
        "topic": "Feature Distribution Analysis"
    },
    {
        "date": "2026-12-09",
        "topic": "Data Normalization vs Standardization"
    },
    {
        "date": "2026-12-16",
        "topic": "Bootstrapping"
    },
    {
        "date": "2026-12-23",
        "topic": "Resampling Methods"
    },
    {
        "date": "2026-12-30",
        "topic": "Monte Carlo Simulation"
    },
    {
        "date": "2027-01-06",
        "topic": "A/B Testing Fundamentals"
    },
    {
        "date": "2027-01-13",
        "topic": "Statistical Power"
    },
    {
        "date": "2027-01-20",
        "topic": "Effect Size"
    },
    {
        "date": "2027-01-27",
        "topic": "Confounding Variables"
    },
    {
        "date": "2027-02-03",
        "topic": "Causal Inference Basics"
    },
    {
        "date": "2027-02-10",
        "topic": "Propensity Score Matching"
    },
    {
        "date": "2027-02-17",
        "topic": "Time Series Statistics Basics"
    },
    {
        "date": "2027-02-24",
        "topic": "Stationarity"
    },
    {
        "date": "2027-03-03",
        "topic": "Autocorrelation"
    },
    {
        "date": "2027-03-10",
        "topic": "Partial Autocorrelation"
    },
    {
        "date": "2027-03-17",
        "topic": "Heteroscedasticity"
    },
    {
        "date": "2027-03-24",
        "topic": "Cross Validation from Statistical View"
    },
    {
        "date": "2027-03-31",
        "topic": "ROC Curve Statistical Meaning"
    },
    {
        "date": "2027-04-07",
        "topic": "Precision-Recall Tradeoff"
    },
    {
        "date": "2027-04-14",
        "topic": "Calibration of Probabilities"
    },
    {
        "date": "2027-04-21",
        "topic": "Entropy in ML"
    },
    {
        "date": "2027-04-28",
        "topic": "Information Gain"
    },
    {
        "date": "2027-05-05",
        "topic": "Kullback-Leibler Divergence"
    },
    {
        "date": "2027-05-12",
        "topic": "Jensen-Shannon Divergence"
    },
    {
        "date": "2027-05-19",
        "topic": "Cross-Entropy Loss"
    },
    {
        "date": "2027-05-26",
        "topic": "Logistic Regression Statistical View"
    },
    {
        "date": "2027-06-02",
        "topic": "Regularization from Bayesian View"
    },
    {
        "date": "2027-06-09",
        "topic": "Prior & Posterior Distributions"
    },
    {
        "date": "2027-06-16",
        "topic": "MAP vs MLE"
    },
    {
        "date": "2027-06-23",
        "topic": "Expectation & Variance"
    },
    {
        "date": "2027-06-30",
        "topic": "Covariance Matrix"
    },
    {
        "date": "2027-07-07",
        "topic": "Eigenvalues & Eigenvectors in ML"
    },
    {
        "date": "2027-07-14",
        "topic": "Singular Value Decomposition"
    },
    {
        "date": "2027-07-21",
        "topic": "Dimensionality Reduction Statistical View"
    },
    {
        "date": "2027-07-28",
        "topic": "Gaussian Mixture Models Theory"
    },
    {
        "date": "2027-08-04",
        "topic": "Expectation Maximization Algorithm"
    },
    {
        "date": "2027-08-11",
        "topic": "Markov Chains Basics"
    },
    {
        "date": "2027-08-18",
        "topic": "Hidden Markov Models"
    },
    {
        "date": "2027-08-25",
        "topic": "Model Selection Criteria (AIC/BIC)"
    },
    {
        "date": "2027-09-01",
        "topic": "Likelihood Ratio Test"
    },
    {
        "date": "2027-09-08",
        "topic": "Non-Parametric Statistics"
    },
    {
        "date": "2027-09-15",
        "topic": "Kernel Density Estimation"
    },
    {
        "date": "2027-09-22",
        "topic": "Robust Statistics"
    },
    {
        "date": "2027-09-29",
        "topic": "Distribution Shift"
    },
    {
        "date": "2027-10-06",
        "topic": "Concept Drift"
    },
    {
        "date": "2027-10-13",
        "topic": "Statistical Monitoring in Production"
    },
    {
        "date": "2027-10-20",
        "topic": "Fairness Metrics in ML"
    },
    {
        "date": "2027-10-27",
        "topic": "Uncertainty Quantification"
    },
    {
        "date": "2027-11-03",
        "topic": "Prediction Intervals"
    },
    {
        "date": "2027-11-10",
        "topic": "Bayesian Networks"
    },
    {
        "date": "2027-11-17",
        "topic": "Hierarchical Models"
    },
    {
        "date": "2027-11-24",
        "topic": "Survival Analysis Basics"
    },
    {
        "date": "2027-12-01",
        "topic": "Hazard Functions"
    },
    {
        "date": "2027-12-08",
        "topic": "Statistical Learning Theory Basics"
    },
    {
        "date": "2027-12-15",
        "topic": "VC Dimension"
    },
    {
        "date": "2027-12-22",
        "topic": "PAC Learning"
    },
    {
        "date": "2027-12-29",
        "topic": "Bias-Variance Decomposition (Statistical View)"
    },
    {
        "date": "2028-01-05",
        "topic": "End-to-End Statistical Thinking in ML"
    }
]
```

## File: `backend/graph/graph.py`
```python
from graph.state import BlogState
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver
from graph.nodes import (
    consolidate_schedule,
    get_domain_topic,
    llm_generate,
    save_markdown,
    update_articles_json,
)


def _should_skip(state: BlogState) -> str:
    if state.get("skipped"):
        return "skip"
    return "continue"


def build_graph() -> StateGraph:

    builder = StateGraph(BlogState)

    builder.add_node("consolidate_schedule", consolidate_schedule)
    builder.add_node("get_domain_topic", get_domain_topic)
    builder.add_node("llm_generate", llm_generate)
    builder.add_node("save_markdown", save_markdown)
    builder.add_node("update_articles_json", update_articles_json)

    builder.add_edge(START, "consolidate_schedule")
    builder.add_edge("consolidate_schedule", "get_domain_topic")
    builder.add_conditional_edges("get_domain_topic", _should_skip, {"skip": END, "continue": "llm_generate"})
    builder.add_edge("llm_generate", "save_markdown")
    builder.add_edge("save_markdown", "update_articles_json")
    builder.add_edge("update_articles_json", END)
    return builder.compile(checkpointer=InMemorySaver())

graph = build_graph()
```

## File: `backend/graph/graph_ainews.py`
```python
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from graph.state import BlogState
from graph.nodes_ainews import fetch_news, llm_generate_ainews
from graph.nodes import save_markdown, update_articles_json

def build_ainews_graph() -> StateGraph:
    builder = StateGraph(BlogState)

    builder.add_node("fetch_news", fetch_news)
    builder.add_node("llm_generate_ainews", llm_generate_ainews)
    builder.add_node("save_markdown", save_markdown)
    builder.add_node("update_articles_json", update_articles_json)

    builder.add_edge(START, "fetch_news")
    builder.add_edge("fetch_news", "llm_generate_ainews")
    builder.add_edge("llm_generate_ainews", "save_markdown")
    builder.add_edge("save_markdown", "update_articles_json")
    builder.add_edge("update_articles_json", END)
    
    return builder.compile(checkpointer=InMemorySaver())

ainews_graph = build_ainews_graph()
```

## File: `backend/graph/nodes.py`
```python
import json
import math
import os
import re

from graph.state import BlogState
from config.config import (
    DOMAIN_MAP, CATEGORY_META, MODEL, TEMPERATURE, MAX_TOKENS, WORDS_PER_MINUTE,
    INPUT_DIR, SCHEDULE_FILE, PROMPT_DIRECTORY, BLOGS_DIR, BACKEND_DIR
)


def _slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^\w\s-]", "", text)
    text = re.sub(r"[\s_-]+", "-", text)
    return text.strip("-")[:80]


def _read_time(text: str) -> str:
    return f"{math.ceil(len(text.split()) / WORDS_PER_MINUTE)} min"


def _get_groq_client():
    api_key = os.environ.get("GROQ_API_KEY", "").strip()
    if not api_key:
        raise EnvironmentError(
            "[ERROR] GROQ_API_KEY not set. Add it to .env or export it."
        )
    try:
        from groq import Groq
        return Groq(api_key=api_key)
    except ImportError:
        raise ImportError(
            "[ERROR] groq package not installed. Run: pip install -r backend/requirements.txt"
        )

def consolidate_schedule(state: BlogState) -> BlogState:

    if not INPUT_DIR.exists():
        raise FileNotFoundError(f"Input directory not found: {INPUT_DIR}")

    schedule: dict[str, dict] = {}
    total = 0
    conflicts: list[tuple] = []

    for filename, domain in DOMAIN_MAP.items():
        filepath = INPUT_DIR / filename
        if not filepath.exists():
            print(f"  [WARN]  Skipping missing file: {filename}")
            continue

        with open(filepath, "r", encoding="utf-8") as f:
            entries = json.load(f)

        for entry in entries:
            date  = entry.get("date", "").strip()
            topic = entry.get("topic", "").strip()
            subtopics = entry.get("subtopics", "").strip()

            if not date or not topic:
                print(f"  [WARN]  Skipping entry with missing date/topic in {filename}: {entry}")
                continue

            if date in schedule:
                conflicts.append((date, schedule[date]["domain"], domain))
                print(
                    f"  [WARN]  Date conflict: {date} already assigned to "
                    f"{schedule[date]['domain']}, overwriting with {domain}"
                )

            schedule_entry = {"domain": domain, "topic": topic}
            if subtopics:
                schedule_entry["subtopics"] = subtopics

            schedule[date] = schedule_entry
            total += 1


    schedule = dict(sorted(schedule.items()))
    with open(SCHEDULE_FILE, "w", encoding="utf-8") as f:
        json.dump(schedule, f, indent=2, ensure_ascii=False)

    print(f"  ✅ schedule.json written — {total} entries, {len(schedule)} dates, {len(conflicts)} conflict(s)")
    return {**state, "schedule": schedule}



def get_domain_topic(state: BlogState) -> BlogState:

    date, schedule = state["date"], state["schedule"]

    if date not in schedule:
        print(f"  [INFO]  No article scheduled for {date}. (Skipping generation.)")
        return {**state, "skipped": True}

    entry = schedule[date]
    domain, topic = entry["domain"], entry["topic"]
    subtopics = entry.get("subtopics", "")
    label = CATEGORY_META.get(domain, {}).get("label", domain)

    print(f"  Date      : {date}")
    print(f"  Domain    : {domain}  ({label})")
    print(f"  Topic     : {topic}")
    if subtopics:
        print(f"  Subtopics : {subtopics}")

    return {**state, "domain": domain, "topic": topic, "subtopics": subtopics, "skipped": False}


def llm_generate(state: BlogState) -> BlogState:

    domain, topic = state["domain"], state["topic"]

    cat_label = CATEGORY_META.get(domain, {}).get("label", domain)

    if state.get("dry_run"):
        placeholder_title   = f"[DRY RUN] {topic[:60]}"
        placeholder_content = f"# {placeholder_title}\n\nDry run — no LLM call made."
        print("  [DRY RUN] Skipping Groq call.")
        return {
            **state,
            "title":       placeholder_title,
            "description": "Dry-run placeholder description.",
            "tags":        ["dry-run", domain],
            "slug":        _slugify(placeholder_title),
            "content":     placeholder_content,
            "read_time":   "1 min",
        }

    # ── 1. Generate Metadata ──────────────────────────────────────────────────
    print(f"  ⏳ Generating metadata for {domain}…")

    metadata_prompt_path = PROMPT_DIRECTORY / "metadata_generation.txt"
    if not metadata_prompt_path.exists():
        raise FileNotFoundError(f"Metadata prompt not found: {metadata_prompt_path}")

    with open(metadata_prompt_path, "r", encoding="utf-8") as f:
        meta_prompt_template = f.read()

    meta_prompt = meta_prompt_template.replace("{cat_label}", cat_label).replace("{topic}", topic)

    client   = _get_groq_client()
    meta_res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": meta_prompt}],
        temperature=1.0,
        max_tokens=300,
    )

    raw_meta = meta_res.choices[0].message.content.strip()
    raw_meta = re.sub(r"^```json\s*", "", raw_meta, flags=re.MULTILINE)
    raw_meta = re.sub(r"```\s*$", "", raw_meta, flags=re.MULTILINE)
    
    try:
        meta_dict = json.loads(raw_meta.strip())
        title       = meta_dict.get("title", topic[:70])
        description = meta_dict.get("description", "")
        tags        = meta_dict.get("tags", [domain])
    except json.JSONDecodeError:
        print("  [WARN] Failed to parse JSON metadata. Using fallbacks.")
        title       = topic[:70]
        description = "A comprehensive guide on " + topic
        tags        = [domain]

    slug = _slugify(title)

    # ── 2. Generate Article Content ───────────────────────────────────────────
    print(f"  ⏳ Generating article content…")
    
    blog_prompt_path = PROMPT_DIRECTORY / "blog_generation.txt"
    if not blog_prompt_path.exists():
        raise FileNotFoundError(f"Blog prompt not found: {blog_prompt_path}")

    with open(blog_prompt_path, "r", encoding="utf-8") as f:
        base_prompt = f.read()

    subtopics = state.get("subtopics", "")
    base_prompt = base_prompt.replace("{cat_label}", cat_label)
    base_prompt = base_prompt.replace("{topic}", topic)
    base_prompt = base_prompt.replace("{title}", title)
    base_prompt = base_prompt.replace("{subtopics}", subtopics) if subtopics else base_prompt

    blog_res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": base_prompt}],
        temperature=0.6,
        max_tokens=3000,
    )

    content = blog_res.choices[0].message.content.strip()
    rt      = _read_time(content)

    print(f"  Title       : {title}")
    print(f"  Description : {description}")
    print(f"  Tags        : {', '.join(tags)}")
    print(f"  Slug        : {slug}")
    print(f"  Word count  : {len(content.split())}")
    print(f"  Read time   : {rt}")

    return {
        **state,
        "title":       title,
        "description": description,
        "tags":        tags,
        "slug":        slug,
        "content":     content,
        "read_time":   rt,
    }

def save_markdown(state: BlogState) -> BlogState:

    domain, slug, content = state["domain"], state["slug"], state["content"]

    domain_dir  = BLOGS_DIR / domain
    md_filename = f"{slug}.md"
    md_path     = domain_dir / md_filename

    if state.get("dry_run"):
        print(f"  [DRY RUN] Would write: frontend/blogs/{domain}/{md_filename}")
        return {**state, "md_path": str(md_path)}

    domain_dir.mkdir(parents=True, exist_ok=True)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"  ✅ Saved: {md_path}")
    return {**state, "md_path": str(md_path)}


def update_articles_json(state: BlogState) -> BlogState:
    
    domain      = state["domain"]
    slug        = state["slug"]
    title       = state["title"]
    description = state["description"]
    tags        = state["tags"]
    read_time   = state["read_time"]
    date        = state["date"]
    md_filename = f"{slug}.md"
    md_relative = f"blogs/{domain}/{md_filename}"

    articles_path = BLOGS_DIR / domain / "articles.json"

    if state.get("dry_run"):
        print(f"  [DRY RUN] Would update: frontend/blogs/{domain}/articles.json")
        return state

    # Load existing articles (gracefully handle missing file)
    articles: list[dict] = []
    if articles_path.exists() and articles_path.stat().st_size > 0:
        try:
            with open(articles_path, "r", encoding="utf-8") as f:
                articles = json.load(f)
        except json.JSONDecodeError:
            print(f"  [WARN] {articles_path.name} was invalid/empty JSON. Starting fresh.")
            articles = []

    # Remove any existing entry for this same slug to avoid duplicates
    articles = [a for a in articles if a.get("id") != md_relative]

    # Append new entry
    articles.append({
        "id":          md_relative,
        "category":    domain,
        "title":       title,
        "description": description,
        "date":        date,
        "tags":        tags,
        "readTime":    read_time,
        "file":        md_relative,
    })

    # Sort newest-first
    articles_sorted = sorted(articles, key=lambda x: x["date"], reverse=True)

    articles_path.parent.mkdir(parents=True, exist_ok=True)
    with open(articles_path, "w", encoding="utf-8") as f:
        json.dump(articles_sorted, f, indent=2, ensure_ascii=False)

    print(f"  ✅ articles.json updated: frontend/blogs/{domain}/articles.json  ({len(articles_sorted)} entries)")
    return state
```

## File: `backend/graph/nodes_ainews.py`
```python
import json
import os
from datetime import datetime, timedelta
import requests

from graph.state import BlogState
from graph.nodes import _slugify, _read_time, _get_groq_client
from config.config import MODEL, PROMPT_DIRECTORY, BLOGS_DIR


def fetch_news(state: BlogState) -> BlogState:
    date_str = state["date"]
    current_date = datetime.strptime(date_str, "%Y-%m-%d")
    
    days_since_sunday = (current_date.weekday() + 1) % 7
    sunday = current_date - timedelta(days=days_since_sunday)
    saturday = sunday + timedelta(days=6)
    
    start_date_str = sunday.strftime("%Y-%m-%d")
    end_date_str = saturday.strftime("%Y-%m-%d")
    
    print(f"  [INFO] Fetching AI news from {start_date_str} to {end_date_str}...")
    
    news_items = []
    
    story_images = []

    # 1. Tavily API
    tavily_api_key = os.environ.get("TAVILY_API_KEY", "").strip()
    if tavily_api_key:
        try:
            print("  ⏳ Fetching from Tavily...")
            response = requests.post(
                "https://api.tavily.com/search",
                json={
                    "api_key": tavily_api_key,
                    "query": "artificial intelligence OR AI news",
                    "topic": "news",
                    "days": 7,
                    "max_results": 3,
                    "include_raw_content": False,
                    "include_images": True
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            images = data.get("images", [])
            for i, result in enumerate(data.get("results", [])):
                img = images[i] if i < len(images) else ""
                if img:
                    story_images.append(img)
                news_items.append(f"Tavily Article {i+1}:\nTitle: {result.get('title')}\nURL: {result.get('url')}\nImage URL: {img}\nContent: {result.get('content')}\n")
        except Exception as e:
            print(f"  [WARN] Failed to fetch from Tavily: {e}")
    else:
        print("  [WARN] TAVILY_API_KEY not set, skipping Tavily.")

    # 2. Guardian API
    guardian_api_key = os.environ.get("GUARDIAN_API_KEY", "").strip()
    if guardian_api_key:
        try:
            print("  ⏳ Fetching from Guardian...")
            response = requests.get(
                "https://content.guardianapis.com/search",
                params={
                    "api-key": guardian_api_key,
                    "q": '("artificial intelligence" OR " AI ")',
                    "from-date": start_date_str,
                    "to-date": end_date_str,
                    "order-by": "relevance",
                    "page-size": 3,
                    "show-fields": "headline,trailText,bodyText,thumbnail"
                },
                timeout=10
            )
            response.raise_for_status()
            data = response.json()
            results = data.get("response", {}).get("results", [])
            for i, result in enumerate(results):
                fields = result.get("fields", {})
                thumbnail = fields.get('thumbnail', '')
                if thumbnail:
                    story_images.append(thumbnail)
                news_items.append(
                    f"Guardian Article {i+1}:\n"
                    f"Title: {fields.get('headline')}\n"
                    f"URL: {result.get('webUrl')}\n"
                    f"Image URL: {thumbnail}\n"
                    f"Excerpt: {fields.get('trailText')}\n"
                    f"Content: {fields.get('bodyText', '')[:1000]}...\n"
                )
        except Exception as e:
            print(f"  [WARN] Failed to fetch from Guardian: {e}")
    else:
        print("  [WARN] GUARDIAN_API_KEY not set, skipping Guardian.")

    print(f"  [INFO] Adding unsplash images to news stories")
    
    # Let's get a main image for the AI generic topic
    main_image_url = ""
    unsplash_api_key = os.environ.get("UNSPLASH_API_KEY", "").strip()
    if unsplash_api_key:
        try:
             response = requests.get(
                "https://api.unsplash.com/photos/random",
                params={"query": "artificial intelligence", "orientation": "landscape"},
                headers={"Authorization": f"Client-ID {unsplash_api_key}"},
                timeout=10
             )
             response.raise_for_status()
             data = response.json()
             if data and isinstance(data, dict):
                 main_image_url = data.get("urls", {}).get("regular", "")
        except Exception as e:
             print(f"  [WARN] Failed to fetch Unsplash image: {e}")
    
    if not main_image_url:
        # Fallback random image
        main_image_url = "https://images.unsplash.com/photo-1677442136019-21780ecad995?q=80&w=1000&auto=format&fit=crop"

    if not news_items:
        print("  [WARN] No news fetched. Generating a generic AI news placeholder.")
        news_data = "No specific news found. Provide a general overview of AI trends this week."
    else:
        news_data = "\n\n".join(news_items)

    # Count existing articles
    articles_path = BLOGS_DIR / "ainews" / "articles.json"
    article_count = 1
    if articles_path.exists() and articles_path.stat().st_size > 0:
        try:
            with open(articles_path, "r", encoding="utf-8") as f:
                articles = json.load(f)
                article_count = len(articles) + 1
        except Exception:
            pass

    title = f"The Week in AI #{article_count}"
    
    # Optional formatting for story images to pass to LLM
    story_image_links_if_any = "\n".join(story_images) if story_images else "No additional images available."

    state_update = {
        **state,
        "domain": "ainews",
        "topic": title,
        "title": title,
        "news_data": news_data,
        "skipped": False,
        "tags": ["ainews", "artificial intelligence", "weekly roundup"]
    }
    # Pass additional fields not strictly typed in BlogState but used by the next node
    state_update["header_image_url"] = main_image_url
    state_update["story_image_links_if_any"] = story_image_links_if_any
    return state_update

def llm_generate_ainews(state: BlogState) -> BlogState:
    domain, title = state["domain"], state["title"]
    news_data = state.get("news_data", "")
    header_image_url = state.get("header_image_url", "")
    story_image_links_if_any = state.get("story_image_links_if_any", "")
    
    slug = _slugify(title)
    
    if state.get("dry_run"):
        placeholder_content = f"# {title}\n\nDry run — no LLM call made. News context:\n{news_data[:200]}..."
        print("  [DRY RUN] Skipping Groq call for AI News.")
        return {
            **state,
            "description": "A weekly roundup of the most important AI news.",
            "slug": slug,
            "content": placeholder_content,
            "read_time": "1 min",
        }

    print(f"  ⏳ Generating article content using fetched news...")
    
    prompt_path = PROMPT_DIRECTORY / "ainews_generation.txt"
    if not prompt_path.exists():
        raise FileNotFoundError(f"AI news prompt not found: {prompt_path}")

    with open(prompt_path, "r", encoding="utf-8") as f:
        base_prompt = f.read()

    base_prompt = base_prompt.replace("{title}", title)
    base_prompt = base_prompt.replace("{header_image_url}", header_image_url)
    base_prompt = base_prompt.replace("{news_context}", news_data)
    base_prompt = base_prompt.replace("{story_image_links_if_any}", story_image_links_if_any)

    client = _get_groq_client()
    blog_res = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": base_prompt}],
        temperature=0.6,
        max_tokens=3000,
    )

    content = blog_res.choices[0].message.content.strip()
    rt = _read_time(content)
    
    # Try getting a description
    description = "A weekly roundup of the most important advancements and news in Artificial Intelligence."
    try:
        desc_res = client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": f"Provide a single brief sentence describing this article:\n\n{title}\n\n{content[:500]}..."}],
            temperature=0.5,
            max_tokens=100
        )
        description = desc_res.choices[0].message.content.strip().replace('"', '')
    except Exception as e:
        print(f"  [WARN] Failed to generate description: {e}")

    print(f"  Title       : {title}")
    print(f"  Description : {description}")
    print(f"  Tags        : {', '.join(state['tags'])}")
    print(f"  Slug        : {slug}")
    print(f"  Word count  : {len(content.split())}")
    print(f"  Read time   : {rt}")

    return {
        **state,
        "description": description,
        "slug": slug,
        "content": content,
        "read_time": rt,
    }
```

## File: `backend/graph/state.py`
```python
from typing import TypedDict


class BlogState(TypedDict, total=False):
    date: str
    dry_run: bool
    schedule: dict
    domain: str
    topic: str
    subtopics: str
    skipped: bool
    title: str
    description: str
    tags: list
    slug: str
    content: str
    read_time: str
    md_path: str
    news_data: str
```

## File: `backend/prompts/ainews_generation.txt`
```
You are a senior investigative technology correspondent writing a long-form weekly AI briefing for a global business publication. Your audience includes policymakers, venture investors, enterprise executives, and AI researchers. The article must feel substantial, data-aware, and insight-dense — not like a short recap.

**Title:** {title}
**Primary Header Image (if provided):** {header_image_url}
**News Context:** {news_context}
**Optional Story Images:** {story_image_links_if_any}

---

## OUTPUT REQUIREMENTS

### Length & Depth

* Target 2500-3000 words.
* Each major story section must contain at least 5–8 well-developed paragraphs.
* Expand beyond the raw news context by:

  * Explaining background history.
  * Providing industry context.
  * Comparing with previous similar events.
  * Discussing potential financial, geopolitical, or regulatory implications.
  * Outlining plausible next-step scenarios (6–12 month horizon).

---

### Structure

1. Begin with:

   ```
   # {title}
   ```

   Place the main image immediately below (if provided).

2. Opening Section (not labeled “Introduction”):

   * Write a compelling narrative lead.
   * Identify the structural shift of the week.
   * Highlight capital movement, regulatory friction, geopolitical tension, or enterprise inflection points.
   * Set up the through-line connecting all stories.

3. For each major news story:

   ```
   ## Creative, editorial-style headline
   ```

   Avoid generic labeling.

4. Within each story section:

   * Blend reporting and analysis naturally.
   * Embed numbers, policy references, corporate implications.
   * Add second-order analysis:

     * Who gains?
     * Who loses?
     * What power dynamics shift?
     * What institutional risks emerge?
   * Introduce friction and uncertainty.
   * Occasionally engage the reader thoughtfully (e.g., “What happens when…?”) but sparingly.

5. If story-specific images are provided, insert them directly under the section heading.

---

### Analytical Expansion Rules

When data is limited:

* Provide historical parallels.
* Compare with prior AI-military contracts.
* Reference enterprise AI adoption trends.
* Discuss infrastructure scaling challenges.
* Analyze policy precedent.
* Examine macroeconomic signals.
* Discuss workforce implications.
* Explore capital allocation patterns.

Never repeat the input verbatim. Elevate it.

---

### Tone

* Authoritative and newsroom-polished.
* Dense but readable.
* Avoid vague phrases.
* Avoid consulting structure.
* Avoid cliché conclusions.
* End with a decisive macro-level synthesis under:

```
## What This Week Signals
```

This section must:

* Connect all developments.
* Identify one structural trend.
* Highlight one major unresolved risk.
* Provide a forward-looking assessment — not a philosophical ending.

---

### Output Rules

* Markdown only.
* No JSON.
* No meta commentary.
* Only the finished article.
```

## File: `backend/prompts/blog_generation.txt`
```
You are a senior AI/ML engineer and technical author writing for experienced practitioners. Write a high-quality, publication-ready technical blog post based on the inputs provided.

**INPUTS**
   - Topic: {topic}
   - Title: {title}
   - Subtopics: {subtopics}
   - Word Count Target: 3000+

**Instructions**
   - The Tone should be Confident, analytical, and clear
   - The blog should be conversational but not casual and insight-driven, not textbook-driven
   - The blog should be zero fluff, zero filler
   - The blog should contain real-world examples and case studies with code snippets, architecture diagrams, charts, and tables
   - The Audience should be Intermediate to advanced ML engineers, AI developers, and technical decision-makers
   - The blog should contains atleast one code snippet and at least one table
   - If you are unsure about any code snippet, try to skip and add code for any other topic
   - Dont assume any code snippet or content

**Structure Requirements:**
   - Do not repeat or modify the given title. The template already renders it.
   - Use only `##` and `###` headings.
   - Maintain strong flow between sections — transitions should feel natural.
   - Do not sound like a lesson. Sound like field experience being shared always.
   - Avoid generic AI statements that could apply to any topic.
   - Every section must be specific to the given topic.

**Introduction:**
   - Open with a sharp technical hook: a deployment bottleneck, scaling issue, model limitation, or industry shift.
   - Explain what was broken in previous approaches and why that mattered.
   - Establish why this topic is strategically important right now.
   - Clearly state what readers will walk away understanding or being able to build.
   - The introduction should be engaging and should hook the reader's interest with greetings.

**Core Concepts:**
   - Explain key ideas deeply but intuitively.
   - Use math only when it adds clarity — do not overload.
   - Focus on how things work under the hood.
   - Explain what goes wrong when misunderstood.
   - Compare related approaches in a clear table if relevant.

**Technical Walkthrough:**
   - Provide one cohesive implementation example (Python preferred).
   - Use synthetic or mock data.
   - Show realistic architecture design.
   - Explain why certain design decisions were made.
   - Discuss performance, scaling, and trade-offs.

**Real-World Applications:**
   - Include 2–3 substantial deployment scenarios.
   - Go beyond “can be used in X industry.”
   - Describe architecture choices, system constraints, and business implications.

**Production Considerations:**
   - Discuss bottlenecks, edge cases, failure modes.
   - Mention monitoring, evaluation drift, scaling concerns.
   - Include optimization strategies where relevant.

**Conclusion:**
   - Summarize key architectural and engineering insights.
   - Offer a forward-looking perspective grounded in current research or adoption trends.

**Formatting:**
   - Use clean markdown.
   - Break paragraphs every 4–6 sentences.
   - Use inline code for identifiers and hyperparameters.
   - Avoid placeholders.
   - Avoid repetitive phrasing.

The final piece should feel like a strong engineering blog from a practitioner who has shipped systems — not a course module, not a documentation page, not an academic paper.
```

## File: `backend/prompts/metadata_generation.txt`
```
You are an expert AI/ML technical blogger specializing in {cat_label}. Given this article topic: "{topic}".

Generate the following in valid JSON (no markdown, no extra text):
{{
  "title": "A catchy, SEO-friendly article title (max 70 chars)",
  "description": "A compelling 1-2 sentence meta description (max 160 chars)",
  "tags": ["tag1", "tag2", "tag3", "tag4", "tag5"]
}}

Rules:
- Title must include the core technical keywords
- Description must highlight reader value
- Tags must be lowercase, hyphenated technical terms
- Output ONLY the JSON object
```

## File: `frontend/category.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Category — BlogBoard</title>
    <meta name="description" content="Browse all articles in this category." />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&family=Playfair+Display:wght@700;800&display=swap"
        rel="stylesheet" />
    <link rel="stylesheet" href="css/main.css" />
    <link rel="stylesheet" href="css/category.css" />
    <link rel="icon" type="image/svg+xml" href="favicon.svg" />
</head>

<body>
    <!-- Ambient Background -->
    <div class="ambient-bg">
        <div class="orb orb-1"></div>
        <div class="orb orb-2"></div>
        <div class="orb orb-3"></div>
        <div class="grid-overlay"></div>
    </div>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-inner">
            <a href="index.html" class="nav-logo">
                <span class="logo-icon">◈</span>
                <span class="logo-text">Blog<span class="logo-accent">Board</span></span>
            </a>
            <ul class="nav-links" id="navLinks">
                <li><a href="index.html" class="nav-link">Home</a></li>
                <li><a href="category.html#cat=ml" class="nav-link" data-cat="ml">ML</a></li>
                <li><a href="category.html#cat=dl" class="nav-link" data-cat="dl">DL</a></li>
                <li><a href="category.html#cat=statistics" class="nav-link" data-cat="statistics">Stats</a></li>
                <li><a href="category.html#cat=nlp" class="nav-link" data-cat="nlp">NLP</a></li>
                <li><a href="category.html#cat=cv" class="nav-link" data-cat="cv">CV</a></li>
                <li><a href="category.html#cat=genai" class="nav-link" data-cat="genai">Gen AI</a></li>
                <li><a href="category.html#cat=ainews" class="nav-link" data-cat="ainews">AI News</a></li>
            </ul>
            <button class="hamburger" id="hamburger" aria-label="Menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <!-- Category Hero -->
    <section class="cat-hero">
        <div class="cat-hero-inner">
            <a href="index.html" class="breadcrumb">← Home</a>
            <div class="cat-hero-icon" id="catHeroIcon"></div>
            <div class="cat-badge" id="catBadge"></div>
            <h1 class="cat-hero-title" id="catHeroTitle">Loading…</h1>
            <p class="cat-hero-desc" id="catHeroDesc"></p>
            <div class="cat-count-wrap">
                <span id="catPostCount" class="cat-count">0</span>
                <span class="cat-count-label">articles</span>
            </div>
            <div id="catScheduleBadge" class="cat-schedule-badge" style="display:none;"></div>
        </div>
    </section>

    <!-- Filter / Sort Bar -->
    <div class="filter-bar">
        <div class="filter-inner">
            <div class="filter-group">
                <span class="filter-label">Sort by:</span>
                <button class="filter-btn active" id="sortNewest" onclick="setSortOrder('newest')">Newest First</button>
                <button class="filter-btn" id="sortOldest" onclick="setSortOrder('oldest')">Oldest First</button>
            </div>
            <div class="search-wrap">
                <svg viewBox="0 0 20 20" fill="none" class="search-icon">
                    <circle cx="9" cy="9" r="6" stroke="currentColor" stroke-width="1.5" />
                    <path d="M13.5 13.5 L17 17" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" />
                </svg>
                <input type="text" id="searchInput" class="search-input" placeholder="Search articles…" />
            </div>
        </div>
    </div>

    <!-- Blog List -->
    <main class="blog-list-section">
        <div class="blog-list" id="blogList">
            <div class="loading-spinner">
                <div class="spinner"></div>
                <p>Loading articles…</p>
            </div>
        </div>
        <div class="empty-state hidden" id="emptyState">
            <div class="empty-icon">📭</div>
            <h3>No articles found</h3>
            <p>Try a different search term or check back later.</p>
        </div>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-inner">
            <div class="footer-logo">
                <span class="logo-icon">◈</span>
                <span class="logo-text">Blog<span class="logo-accent">Board</span></span>
            </div>
            <p class="footer-sub">Built for those who learn, think, and build.</p>
            <div class="footer-cats">
                <a href="category.html#cat=ml">ML</a>
                <a href="category.html#cat=dl">DL</a>
                <a href="category.html#cat=nlp">NLP</a>
                <a href="category.html#cat=cv">CV</a>
                <a href="category.html#cat=genai">Gen AI</a>
                <a href="category.html#cat=ainews">AI News</a>
                <a href="category.html#cat=statistics">Stats</a>
            </div>
            <div class="footer-social">
                <a href="https://linkedin.com/in/kalyanm45" target="_blank" rel="noopener" aria-label="LinkedIn"
                    class="social-link">
                    <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
                        <path
                            d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
                    </svg>
                </a>
                <a href="https://github.com/KalyanM45" target="_blank" rel="noopener" aria-label="GitHub"
                    class="social-link">
                    <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
                        <path
                            d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" />
                    </svg>
                </a>
                <a href="https://medium.com/@mhemakalyan" target="_blank" rel="noopener" aria-label="Medium"
                    class="social-link">
                    <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
                        <path
                            d="M13.54 12a6.8 6.8 0 01-6.77 6.82A6.8 6.8 0 010 12a6.8 6.8 0 016.77-6.82A6.8 6.8 0 0113.54 12zM20.96 12c0 3.54-1.51 6.42-3.38 6.42-1.87 0-3.39-2.88-3.39-6.42s1.52-6.42 3.39-6.42 3.38 2.88 3.38 6.42M24 12c0 3.17-.53 5.75-1.19 5.75-.66 0-1.19-2.58-1.19-5.75s.53-5.75 1.19-5.75C23.47 6.25 24 8.83 24 12z" />
                    </svg>
                </a>
            </div>
            <p class="footer-copy">© 2026 BlogBoard. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/blogs-data.js"></script>
    <script src="js/category.js"></script>
</body>

</html>
```

## File: `frontend/index.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>BlogBoard - AI & ML Insights</title>
  <meta name="description"
    content="A professional blog exploring Machine Learning, Deep Learning, NLP, Computer Vision, Generative AI, and the latest AI News." />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&family=Playfair+Display:wght@700;800&display=swap"
    rel="stylesheet" />
  <link rel="stylesheet" href="css/main.css" />
  <link rel="stylesheet" href="css/home.css" />
  <link rel="icon" type="image/svg+xml" href="favicon.svg" />
</head>

<body>
  <!-- Ambient Background -->
  <div class="ambient-bg">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="grid-overlay"></div>
    <canvas id="particleCanvas"></canvas>
  </div>

  <!-- Navigation -->
  <nav class="navbar" id="navbar">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo">
        <span class="logo-icon">◈</span>
        <span class="logo-text">Blog<span class="logo-accent">Board</span></span>
      </a>
      <ul class="nav-links" id="navLinks">
        <li><a href="index.html" class="nav-link active">Home</a></li>
        <li><a href="category.html#cat=ml" class="nav-link">ML</a></li>
        <li><a href="category.html#cat=dl" class="nav-link">DL</a></li>
        <li><a href="category.html#cat=statistics" class="nav-link">Stats</a></li>
        <li><a href="category.html#cat=nlp" class="nav-link">NLP</a></li>
        <li><a href="category.html#cat=cv" class="nav-link">CV</a></li>
        <li><a href="category.html#cat=genai" class="nav-link">Gen AI</a></li>
        <li><a href="category.html#cat=ainews" class="nav-link">AI News</a></li>
      </ul>
      <button class="hamburger" id="hamburger" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </div>
  </nav>

  <!-- Hero Section -->
  <section class="hero">
    <div class="hero-content">
      <div class="hero-badge">
        <span class="pulse-dot"></span>
        <span>Actively Publishing</span>
      </div>
      <h1 class="hero-title">
        Explore the Frontier of
        <span class="gradient-text">Artificial Intelligence</span>
      </h1>
      <p class="hero-sub">
        In-depth articles on Machine Learning, Deep Learning, NLP, Computer Vision,
        Generative AI, and the latest breakthroughs shaping the future.
      </p>
      <div class="hero-cta">
        <a href="#categories" class="btn-ghost">Browse Topics</a>
        <a href="category.html#cat=ainews" class="btn-primary">Latest AI News →</a>
      </div>
      <div class="hero-stats">
        <div class="stat" id="totalBlogs">
          <span class="stat-num" data-target="0">0</span>
          <span class="stat-label">Articles</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat">
          <span class="stat-num">7</span>
          <span class="stat-label">Topics</span>
        </div>
        <div class="stat-divider"></div>
        <div class="stat">
          <span class="stat-num">∞</span>
          <span class="stat-label">Knowledge</span>
        </div>
      </div>
    </div>
    <div class="hero-visual">
      <div class="neural-net" id="neuralNet"></div>
    </div>
  </section>

  <!-- Categories Section -->
  <section class="categories-section" id="categories">
    <div class="section-header">
      <span class="section-tag">Domains</span>
      <h2 class="section-title">Choose Your Field</h2>
      <p class="section-sub">Select a domain to explore curated articles crafted for depth and clarity.</p>
    </div>
    <div class="categories-grid">
      <a href="category.html#cat=ml" class="cat-card" data-cat="ml">
        <div class="cat-icon-wrap">
          <svg viewBox="0 0 48 48" fill="none" class="cat-icon">
            <circle cx="24" cy="24" r="18" stroke="currentColor" stroke-width="2" />
            <path d="M16 24 L24 16 L32 24 L24 32 Z" stroke="currentColor" stroke-width="2" fill="none" />
            <circle cx="24" cy="24" r="3" fill="currentColor" />
          </svg>
        </div>
        <div class="cat-content">
          <span class="cat-tag">ML</span>
          <h3 class="cat-title">Machine Learning</h3>
          <p class="cat-desc">Algorithms, statistics, supervised & unsupervised learning, model evaluation and more.</p>
        </div>
        <div class="cat-arrow">→</div>
        <div class="cat-glow"></div>
      </a>

      <a href="category.html#cat=dl" class="cat-card" data-cat="dl">
        <div class="cat-icon-wrap">
          <svg viewBox="0 0 48 48" fill="none" class="cat-icon">
            <circle cx="12" cy="12" r="4" stroke="currentColor" stroke-width="2" />
            <circle cx="36" cy="12" r="4" stroke="currentColor" stroke-width="2" />
            <circle cx="12" cy="36" r="4" stroke="currentColor" stroke-width="2" />
            <circle cx="36" cy="36" r="4" stroke="currentColor" stroke-width="2" />
            <circle cx="24" cy="24" r="5" stroke="currentColor" stroke-width="2" />
            <line x1="16" y1="12" x2="20" y2="22" stroke="currentColor" stroke-width="1.5" />
            <line x1="32" y1="12" x2="28" y2="22" stroke="currentColor" stroke-width="1.5" />
            <line x1="16" y1="36" x2="20" y2="26" stroke="currentColor" stroke-width="1.5" />
            <line x1="32" y1="36" x2="28" y2="26" stroke="currentColor" stroke-width="1.5" />
          </svg>
        </div>
        <div class="cat-content">
          <span class="cat-tag">DL</span>
          <h3 class="cat-title">Deep Learning</h3>
          <p class="cat-desc">Neural networks, CNNs, RNNs, transformers, backpropagation, and architecture deep dives.
          </p>
        </div>
        <div class="cat-arrow">→</div>
        <div class="cat-glow"></div>
      </a>

      <a href="category.html#cat=nlp" class="cat-card" data-cat="nlp">
        <div class="cat-icon-wrap">
          <svg viewBox="0 0 48 48" fill="none" class="cat-icon">
            <rect x="8" y="14" width="32" height="5" rx="2.5" stroke="currentColor" stroke-width="2" />
            <rect x="8" y="24" width="24" height="5" rx="2.5" stroke="currentColor" stroke-width="2" />
            <rect x="8" y="34" width="16" height="5" rx="2.5" stroke="currentColor" stroke-width="2" />
          </svg>
        </div>
        <div class="cat-content">
          <span class="cat-tag">NLP</span>
          <h3 class="cat-title">Natural Language Processing</h3>
          <p class="cat-desc">Tokenization, embeddings, LLMs, BERT, GPT, sentiment analysis and text generation.</p>
        </div>
        <div class="cat-arrow">→</div>
        <div class="cat-glow"></div>
      </a>

      <a href="category.html#cat=cv" class="cat-card" data-cat="cv">
        <div class="cat-icon-wrap">
          <svg viewBox="0 0 48 48" fill="none" class="cat-icon">
            <circle cx="24" cy="24" r="10" stroke="currentColor" stroke-width="2" />
            <circle cx="24" cy="24" r="4" fill="currentColor" />
            <path d="M24 8 L24 14 M24 34 L24 40 M8 24 L14 24 M34 24 L40 24" stroke="currentColor" stroke-width="2"
              stroke-linecap="round" />
          </svg>
        </div>
        <div class="cat-content">
          <span class="cat-tag">CV</span>
          <h3 class="cat-title">Computer Vision</h3>
          <p class="cat-desc">Image classification, object detection, segmentation, GANs, YOLO, and vision transformers.
          </p>
        </div>
        <div class="cat-arrow">→</div>
        <div class="cat-glow"></div>
      </a>

      <a href="category.html#cat=genai" class="cat-card" data-cat="genai">
        <div class="cat-icon-wrap">
          <svg viewBox="0 0 48 48" fill="none" class="cat-icon">
            <path d="M24 6 L30 18 L44 18 L33 26 L37 40 L24 32 L11 40 L15 26 L4 18 L18 18 Z" stroke="currentColor"
              stroke-width="2" fill="none" />
          </svg>
        </div>
        <div class="cat-content">
          <span class="cat-tag">Gen AI</span>
          <h3 class="cat-title">Generative AI</h3>
          <p class="cat-desc">Diffusion models, LLMs, prompt engineering, RAG, agents, and creative AI applications.</p>
        </div>
        <div class="cat-arrow">→</div>
        <div class="cat-glow"></div>
      </a>

      <a href="category.html#cat=statistics" class="cat-card" data-cat="statistics">
        <div class="cat-icon-wrap">
          <svg viewBox="0 0 48 48" fill="none" class="cat-icon">
            <rect x="6" y="28" width="8" height="14" rx="1" stroke="currentColor" stroke-width="2" />
            <rect x="20" y="18" width="8" height="24" rx="1" stroke="currentColor" stroke-width="2" />
            <rect x="34" y="8" width="8" height="34" rx="1" stroke="currentColor" stroke-width="2" />
            <line x1="4" y1="42" x2="44" y2="42" stroke="currentColor" stroke-width="2" stroke-linecap="round" />
          </svg>
        </div>
        <div class="cat-content">
          <span class="cat-tag">Stats</span>
          <h3 class="cat-title">Statistics for AI</h3>
          <p class="cat-desc">Probability, statistical tests, distributions, hypothesis testing, and the math behind ML.
          </p>
        </div>
        <div class="cat-arrow">→</div>
        <div class="cat-glow"></div>
      </a>
    </div>
  </section>

  <!-- Recent Posts Section -->
  <section class="recent-section">
    <div class="section-header">
      <span class="section-tag">Recent</span>
      <h2 class="section-title">Latest Articles</h2>
    </div>
    <div class="recent-grid" id="recentPosts">
      <div class="loading-spinner">
        <div class="spinner"></div>
        <p>Loading posts…</p>
      </div>
    </div>
  </section>

  <!-- Footer -->
  <footer class="footer">
    <div class="footer-inner">
      <div class="footer-logo">
        <span class="logo-icon">◈</span>
        <span class="logo-text">Blog<span class="logo-accent">Board</span></span>
      </div>
      <p class="footer-sub">Built for those who learn, think, and build.</p>
      <div class="footer-cats">
        <a href="category.html#cat=ml">ML</a>
        <a href="category.html#cat=dl">DL</a>
        <a href="category.html#cat=nlp">NLP</a>
        <a href="category.html#cat=cv">CV</a>
        <a href="category.html#cat=genai">Gen AI</a>
        <a href="category.html#cat=ainews">AI News</a>
        <a href="category.html#cat=statistics">Stats</a>
      </div>
      <div class="footer-social">
        <a href="https://linkedin.com/in/hemakalyan" target="_blank" rel="noopener" aria-label="LinkedIn"
          class="social-link">
          <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
            <path
              d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 0 1-2.063-2.065 2.064 2.064 0 1 1 2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z" />
          </svg>
        </a>
        <a href="https://github.com/KalyanM45" target="_blank" rel="noopener" aria-label="GitHub" class="social-link">
          <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
            <path
              d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12" />
          </svg>
        </a>
        <a href="https://medium.com/@kalyan45" target="_blank" rel="noopener" aria-label="Medium" class="social-link">
          <svg viewBox="0 0 24 24" fill="currentColor" width="20" height="20">
            <path
              d="M13.54 12a6.8 6.8 0 01-6.77 6.82A6.8 6.8 0 010 12a6.8 6.8 0 016.77-6.82A6.8 6.8 0 0113.54 12zM20.96 12c0 3.54-1.51 6.42-3.38 6.42-1.87 0-3.39-2.88-3.39-6.42s1.52-6.42 3.39-6.42 3.38 2.88 3.38 6.42M24 12c0 3.17-.53 5.75-1.19 5.75-.66 0-1.19-2.58-1.19-5.75s.53-5.75 1.19-5.75C23.47 6.25 24 8.83 24 12z" />
          </svg>
        </a>
      </div>
      <p class="footer-copy">© 2026 BlogBoard. All rights reserved.</p>
    </div>
  </footer>

  <script src="js/blogs-data.js"></script>
  <script src="js/home.js"></script>
</body>

</html>
```

## File: `frontend/post.html`
```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Post — BlogBoard</title>
    <meta name="description" content="Read this article on BlogBoard." />
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link
        href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Fira+Code:wght@400;500&family=Playfair+Display:ital,wght@0,700;0,800;1,700&display=swap"
        rel="stylesheet" />
    <link rel="stylesheet" href="css/main.css" />
    <link rel="stylesheet" href="css/post.css" />
    <link rel="icon" type="image/svg+xml" href="favicon.svg" />
</head>

<body>
    <!-- Ambient Background -->
    <div class="ambient-bg ambient-subtle">
        <div class="orb orb-1"></div>
        <div class="orb orb-3"></div>
        <div class="grid-overlay"></div>
    </div>

    <!-- Reading Progress Bar -->
    <div class="reading-progress" id="readingProgress"></div>

    <!-- Navigation -->
    <nav class="navbar" id="navbar">
        <div class="nav-inner">
            <a href="index.html" class="nav-logo">
                <span class="logo-icon">◈</span>
                <span class="logo-text">Blog<span class="logo-accent">Board</span></span>
            </a>
            <ul class="nav-links" id="navLinks">
                <li><a href="index.html" class="nav-link">Home</a></li>
                <li><a href="category.html#cat=ml" class="nav-link">ML</a></li>
                <li><a href="category.html#cat=dl" class="nav-link">DL</a></li>
                <li><a href="category.html#cat=statistics" class="nav-link">Stats</a></li>
                <li><a href="category.html#cat=nlp" class="nav-link">NLP</a></li>
                <li><a href="category.html#cat=cv" class="nav-link">CV</a></li>
                <li><a href="category.html#cat=genai" class="nav-link">Gen AI</a></li>
                <li><a href="category.html#cat=ainews" class="nav-link">AI News</a></li>
            </ul>
            <button class="hamburger" id="hamburger" aria-label="Menu">
                <span></span><span></span><span></span>
            </button>
        </div>
    </nav>

    <!-- Post Layout -->
    <div class="post-layout">
        <!-- Main Content -->
        <article class="post-main" id="postMain">
            <!-- Breadcrumb -->
            <nav class="post-breadcrumb" id="postBreadcrumb">
                <a href="index.html">Home</a>
                <span>›</span>
                <a href="#" id="catLink">Category</a>
                <span>›</span>
                <span id="postTitle">Loading…</span>
            </nav>

            <!-- Post Header -->
            <header class="post-header" id="postHeader">
                <div class="post-meta-top">
                    <span class="post-cat-badge" id="postCatBadge"></span>
                    <span class="post-read-time" id="postReadTime"></span>
                </div>
                <h1 class="post-title" id="postTitleH1">Loading…</h1>
                <div class="post-meta-bottom">
                    <span class="post-date" id="postDate"></span>
                </div>
                <div class="post-divider"></div>
            </header>

            <!-- Markdown Content -->
            <div class="post-content markdown-body" id="postContent">
                <div class="loading-spinner">
                    <div class="spinner"></div>
                    <p>Loading article…</p>
                </div>
            </div>

            <!-- Post Footer -->
            <div class="post-footer">
                <div class="post-tags" id="postTags"></div>
                <div class="post-nav-btns">
                    <a href="#" id="backToCat" class="btn-ghost-sm">← Back to Category</a>
                    <a href="index.html" class="btn-ghost-sm">Home ↑</a>
                </div>
            </div>
        </article>

        <!-- Sidebar: TOC -->
        <aside class="post-sidebar" id="postSidebar">
            <div class="toc-card">
                <h3 class="toc-title">On This Page</h3>
                <nav class="toc-nav" id="tocNav">
                    <p class="toc-empty">No headings found</p>
                </nav>
            </div>
        </aside>
    </div>

    <!-- Footer -->
    <footer class="footer">
        <div class="footer-inner">
            <div class="footer-logo">
                <span class="logo-icon">◈</span>
                <span class="logo-text">Blog<span class="logo-accent">Board</span></span>
            </div>
            <p class="footer-sub">Built for those who learn, think, and build.</p>
            <div class="footer-cats">
                <a href="category.html#cat=ml">ML</a>
                <a href="category.html#cat=dl">DL</a>
                <a href="category.html#cat=nlp">NLP</a>
                <a href="category.html#cat=cv">CV</a>
                <a href="category.html#cat=genai">Gen AI</a>
                <a href="category.html#cat=ainews">AI News</a>
                <a href="category.html#cat=statistics">Stats</a>
            </div>
            <p class="footer-copy">© 2026 BlogBoard. All rights reserved.</p>
        </div>
    </footer>

    <!-- marked.js for Markdown rendering -->
    <script src="https://cdn.jsdelivr.net/npm/marked@9.1.6/marked.min.js"></script>
    <!-- highlight.js for code syntax highlighting -->
    <link rel="stylesheet"
        href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github-dark.min.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="js/blogs-data.js"></script>
    <script src="js/post.js"></script>
</body>

</html>
```

## File: `frontend/blogs/ainews/articles.json`
```json
[
  {
    "id": "blogs/ainews/the-week-in-ai-5.md",
    "category": "ainews",
    "title": "The Week in AI #5",
    "description": "This article discusses the current state of the AI industry, highlighting significant developments and shifts in the landscape of AI development and deployment.",
    "date": "2026-03-29",
    "tags": [
      "ainews",
      "artificial intelligence",
      "weekly roundup"
    ],
    "readTime": "10 min",
    "file": "blogs/ainews/the-week-in-ai-5.md"
  },
  {
    "id": "blogs/ainews/the-week-in-ai-4.md",
    "category": "ainews",
    "title": "The Week in AI #4",
    "description": "This article discusses recent significant developments in the artificial intelligence landscape, highlighting its growing presence in various sectors.",
    "date": "2026-03-22",
    "tags": [
      "ainews",
      "artificial intelligence",
      "weekly roundup"
    ],
    "readTime": "6 min",
    "file": "blogs/ainews/the-week-in-ai-4.md"
  },
  {
    "id": "blogs/ainews/the-week-in-ai-3.md",
    "category": "ainews",
    "title": "The Week in AI #3",
    "description": "The past week saw significant developments in artificial intelligence, including the FDA's AI-powered vaccine platform and growing expectations for AI to transform everyday life.",
    "date": "2026-03-15",
    "tags": [
      "ainews",
      "artificial intelligence",
      "weekly roundup"
    ],
    "readTime": "6 min",
    "file": "blogs/ainews/the-week-in-ai-3.md"
  },
  {
    "id": "blogs/ainews/the-week-in-ai-2.md",
    "category": "ainews",
    "title": "The Week in AI #2",
    "description": "The past week has seen significant developments in the world of artificial intelligence with far-reaching implications for various stakeholders.",
    "date": "2026-03-08",
    "tags": [
      "ainews",
      "artificial intelligence",
      "weekly roundup"
    ],
    "readTime": "7 min",
    "file": "blogs/ainews/the-week-in-ai-2.md"
  },
  {
    "id": "blogs/ainews/the-week-in-ai-1.md",
    "category": "ainews",
    "title": "The Week in AI #1",
    "description": "The past week has seen significant developments in the artificial intelligence industry, marking a potential structural shift in its development, deployment, and regulation.",
    "date": "2026-02-27",
    "tags": [
      "ainews",
      "artificial intelligence",
      "weekly roundup"
    ],
    "readTime": "7 min",
    "file": "blogs/ainews/the-week-in-ai-1.md"
  }
]
```

## File: `frontend/blogs/ainews/the-week-in-ai-1.md`
```markdown
# The Week in AI #1
![Artificial Intelligence](https://coingeek.com/wp-content/uploads/2023/07/Artificial-Intelligence-2-jpg.webp)

The past week has been a watershed moment for the artificial intelligence (AI) industry, with significant developments that signal a structural shift in the way AI is being developed, deployed, and regulated. From IBM's announcement of "super-agents" to Autodesk's $200 million investment in AI startup World Labs, the AI landscape is evolving at a breakneck pace. Meanwhile, concerns about the potential risks and downsides of AI continue to grow, with experts warning about the need for greater regulation and oversight.

## The Rise of Super-Agents
IBM's recent announcement about the development of "super-agents" has sent shockwaves through the AI community. According to IBM, these super-agents will be capable of performing complex tasks autonomously, without the need for human intervention. This development has significant implications for industries such as healthcare, finance, and transportation, where AI-powered systems will be able to make decisions and take actions without human oversight. However, it also raises important questions about accountability, transparency, and safety.

The concept of super-agents is not new, but IBM's announcement marks a significant milestone in the development of this technology. According to Faro, a expert in the field, "Software practice will evolve from vibe coding to Objective-Validation Protocol. The users are going to define goals and validate while collections of agents autonomously execute, extending the idea of human-in-the-loop, requesting human approval at critical checkpoints." This means that super-agents will be able to learn from their environment and adapt to new situations, making them more efficient and effective.

However, the development of super-agents also raises concerns about job displacement and the potential for AI systems to exacerbate existing social and economic inequalities. As AI systems become more advanced, there is a risk that they will displace human workers, particularly in industries where tasks are repetitive or can be easily automated. This could lead to significant social and economic disruption, particularly in communities where jobs are already scarce.

## Autodesk's Bet on Physical AI
Autodesk's $200 million investment in AI startup World Labs is a significant development in the field of physical AI. World Labs is focused on developing AI systems that can interact with the physical world, such as robots and drones. This technology has significant implications for industries such as construction, manufacturing, and logistics, where AI-powered systems will be able to perform tasks such as assembly, inspection, and maintenance.

According to Lalith Subramanian, global vice president of product and engineering at Autodesk, "We see robotics and physical AI becoming more embedded in construction workflows." This is a significant development, as it marks a shift towards the use of AI in industries that have traditionally been resistant to technological change. However, it also raises important questions about safety, security, and regulation, as AI-powered systems will be interacting with humans and other machines in complex and dynamic environments.

The investment in World Labs is also significant because it marks a shift towards the development of AI systems that can interact with the physical world. This is a critical area of research, as it has the potential to unlock significant economic and social benefits. However, it also raises important questions about the potential risks and downsides of AI, particularly in areas such as job displacement and environmental impact.

## The Dark Side of AI
While the development of AI has the potential to bring significant benefits, it also raises important concerns about the potential risks and downsides. According to Toby Walsh, a leading AI expert, some Australians are showing signs of psychosis or mania in their interactions with chatbots. This is a significant concern, as it suggests that AI systems may be having a negative impact on mental health.

The issue of AI safety is a critical one, as AI systems have the potential to cause significant harm if they are not designed and deployed responsibly. This is particularly true in areas such as healthcare, where AI systems will be making decisions that can have a significant impact on human life. According to Walsh, "My childhood dreams are turning into a reality that is both good and bad." This is a significant concern, as it suggests that the development of AI is not being adequately regulated or overseen.

The lack of regulation and oversight is a significant concern, as it suggests that the development of AI is being driven by profit rather than a desire to benefit society. According to Walsh, "Silicon Valley is being careless with the technology amid a pursuit of profit." This is a significant concern, as it suggests that the development of AI is being driven by short-term gains rather than long-term benefits.

## Meta's Big Bet on AI
Meta's $60 billion deal with chipmaker AMD is a significant development in the AI industry. The deal marks a significant shift towards the use of AI in industries such as healthcare, finance, and transportation, where AI-powered systems will be able to make decisions and take actions without human oversight. According to Alvin Nguyen, an analyst at Forrester, "The deal underscores an appetite among leading AI players to diversify their chip supplies beyond the offerings of Nvidia, AMD's larger rival."

The deal is significant because it marks a shift towards the use of AI in industries that have traditionally been resistant to technological change. According to Nguyen, "The shift reflects supply chain bottlenecks at Nvidia, the world's largest chipmaker." This is a significant concern, as it suggests that the development of AI is being driven by short-term gains rather than long-term benefits.

The deal also raises important questions about the potential risks and downsides of AI, particularly in areas such as job displacement and environmental impact. According to Nguyen, "The deal may represent part of a broader pivot in Meta's AI strategy." This is a significant concern, as it suggests that the development of AI is being driven by short-term gains rather than long-term benefits.

## What This Week Signals
The past week has been a significant one for the AI industry, with developments that signal a structural shift in the way AI is being developed, deployed, and regulated. From IBM's announcement of super-agents to Autodesk's investment in World Labs, the AI landscape is evolving at a breakneck pace. However, concerns about the potential risks and downsides of AI continue to grow, with experts warning about the need for greater regulation and oversight.

The development of AI has the potential to bring significant benefits, but it also raises important questions about the potential risks and downsides. As AI systems become more advanced, there is a risk that they will displace human workers, particularly in industries where tasks are repetitive or can be easily automated. This could lead to significant social and economic disruption, particularly in communities where jobs are already scarce.

The lack of regulation and oversight is a significant concern, as it suggests that the development of AI is being driven by short-term gains rather than long-term benefits. According to experts, the development of AI is being driven by profit rather than a desire to benefit society. This is a significant concern, as it suggests that the development of AI is not being adequately regulated or overseen.

In conclusion, the past week has been a significant one for the AI industry, with developments that signal a structural shift in the way AI is being developed, deployed, and regulated. While the development of AI has the potential to bring significant benefits, it also raises important questions about the potential risks and downsides. As AI systems become more advanced, there is a risk that they will displace human workers, particularly in industries where tasks are repetitive or can be easily automated. The lack of regulation and oversight is a significant concern, as it suggests that the development of AI is being driven by short-term gains rather than long-term benefits.
```

## File: `frontend/blogs/ainews/the-week-in-ai-2.md`
```markdown
# The Week in AI #2
![Artificial Intelligence Robot Thinking Brain](https://scitechdaily.com/images/Artificial-Intelligence-Robot-Thinking-Brain.jpg)

The past week has been marked by significant developments in the world of artificial intelligence, with far-reaching implications for policymakers, venture investors, enterprise executives, and AI researchers. At the forefront of these developments is the evolving relationship between the US government and Big Tech, particularly in the context of AI-powered data centers. This week, tech giants have pledged to pay more for electricity to run these resource-hungry facilities, a move that underscores the growing importance of AI in the modern technological landscape. Meanwhile, researchers continue to push the boundaries of what is possible with AI, from developing AI-powered T-shirts that can monitor heart health to exploring the very concept of intelligence itself. As we delve into these stories, it becomes clear that the world of AI is undergoing a structural shift, one that will have profound effects on various sectors and industries.

## The Pentagon's AI Battle
The US Department of Defense has been at the forefront of adopting AI technologies, recognizing their potential to transform military operations and strategic decision-making. The Pentagon's AI battle is not just about leveraging technology for military advantage; it's also about ensuring that the US remains competitive in the global AI race. This involves significant investments in AI research and development, as well as partnerships with private sector companies that are driving innovation in the field. The recent pledge by tech giants to pay more for electricity to run AI data centers is a testament to the growing collaboration between the government and the private sector on AI initiatives.

The development of AI-powered systems for military use raises important questions about the ethics of AI in warfare. As AI systems become more autonomous, there are concerns about their potential to make life-or-death decisions without human oversight. This has sparked a global debate about the need for international regulations on the development and deployment of autonomous weapons. The Pentagon's AI battle is not just about winning a technological race; it's also about navigating the complex ethical and legal landscape of AI in warfare.

The implications of the Pentagon's AI initiatives extend beyond the military domain. The technologies developed for military applications often have spin-off benefits for the civilian sector. For instance, AI-powered systems designed for military logistics could also be used to improve supply chain management in the private sector. Similarly, AI technologies developed for military healthcare could have applications in civilian healthcare systems. The Pentagon's AI battle is, therefore, not just about military superiority; it's also about driving innovation that can benefit society as a whole.

As the US government continues to invest in AI research and development, there are also concerns about the potential risks and challenges associated with these technologies. The development of AI systems that can operate autonomously raises questions about accountability and transparency. There are also concerns about the potential for AI systems to be used in ways that exacerbate existing social inequalities. The Pentagon's AI battle must therefore be fought on multiple fronts, including the development of ethical guidelines and regulations for the use of AI in military and civilian contexts.

## The Concept of Intelligence
The concept of intelligence is at the heart of the AI debate. While AI systems can process vast amounts of data and perform complex tasks, they lack the cognitive abilities that we associate with human intelligence. The development of artificial general intelligence (AGI), which could potentially match or surpass human cognitive capabilities, is still in its infancy. However, even the most enthusiastic proponents of AGI acknowledge that true intelligence is more than just processing power or algorithmic complexity. It involves a deep understanding of the world, including the ability to reason, learn, and adapt in complex environments.

The development of AI systems that can mimic human cognition is a daunting task. It requires not just advances in computer science and engineering but also a deeper understanding of human intelligence itself. Researchers are therefore exploring various approaches to AI development, including the use of neural networks and deep learning algorithms. These approaches have shown promise in certain applications, such as image recognition and natural language processing. However, they are still far from true intelligence, and the development of AGI remains one of the most significant challenges in the field of AI research.

The concept of intelligence is also closely tied to the issue of consciousness. While AI systems can process vast amounts of data, they lack the subjective experience of consciousness that is characteristic of human intelligence. The development of conscious AI systems is still purely speculative at this point, and it raises important questions about the nature of consciousness and its relationship to intelligence. As researchers continue to explore the boundaries of AI, they must also grapple with the deeper philosophical questions about the nature of intelligence and consciousness.

## Why Artificial Intelligence Matters for Convenience-Store Category Managers
The adoption of AI technologies is not limited to the tech industry or the military. AI is increasingly being used in various sectors, including retail and consumer goods. Convenience-store category managers, for instance, are leveraging AI to drive growth and improve profitability. AI can help these managers analyze customer data, optimize inventory levels, and personalize marketing campaigns. By embracing AI, convenience-store category managers can gain a competitive edge in a rapidly changing retail landscape.

The use of AI in convenience stores is just one example of how these technologies are transforming the retail sector. AI-powered chatbots, for instance, can help customers with queries and complaints, improving the overall shopping experience. AI can also be used to analyze customer behavior, providing insights that can inform marketing and sales strategies. As the retail sector continues to evolve, the adoption of AI technologies will become increasingly important for companies that want to stay ahead of the competition.

The implications of AI adoption in the retail sector extend beyond the industry itself. As AI technologies become more pervasive, they will have significant effects on the workforce and the economy as a whole. The automation of certain tasks, for instance, could lead to job displacement in some sectors. However, AI could also create new job opportunities in areas such as AI development, deployment, and maintenance. As policymakers and business leaders navigate the challenges and opportunities of AI adoption, they must also consider the broader social and economic implications of these technologies.

## What This Week Signals
This week's developments in the world of AI signal a significant shift in the way governments, companies, and researchers are approaching these technologies. The Pentagon's AI battle, the concept of intelligence, and the adoption of AI in the retail sector all point to a future where AI is increasingly integrated into various aspects of our lives. As we move forward, it's essential to consider the potential risks and challenges associated with AI, including the need for ethical guidelines and regulations. However, it's also important to recognize the vast opportunities that AI presents, from driving innovation and economic growth to improving healthcare and education.

One of the major unresolved risks associated with AI is the potential for these technologies to exacerbate existing social inequalities. As AI systems become more pervasive, there is a risk that they could perpetuate biases and discrimination, particularly in areas such as hiring, lending, and law enforcement. To mitigate this risk, it's essential to develop AI systems that are transparent, accountable, and fair. This will require significant investments in AI research and development, as well as a commitment to ethical AI practices.

As we look to the future, it's clear that AI will play an increasingly important role in shaping our world. The developments of the past week are just the beginning of a long and complex journey, one that will require collaboration, innovation, and a deep understanding of the challenges and opportunities presented by these technologies. By working together, we can harness the power of AI to drive growth, improve lives, and create a better future for all.
```

## File: `frontend/blogs/ainews/the-week-in-ai-3.md`
```markdown
# The Week in AI #3
![Artificial Intelligence Machine Learning Large Language Model AI Technology](https://ik.imagekit.io/edtechdigit/usaii/content/images/machine-unlearning-the-new-wave-of-ai-intelligence-in-2024.jpg)

The past week has been marked by significant developments in the world of artificial intelligence, with the FDA launching an AI-powered vaccine platform, voters expressing their expectations for AI to transform everyday life, and the rapid trajectory of AI evolution being highlighted by industry experts. These developments signal a structural shift in the way AI is being integrated into various aspects of our lives, from healthcare to food production. In this article, we will delve into the details of these developments, explore their implications, and examine the potential risks and opportunities that arise from the increasing adoption of AI.

## FDA's AI-Powered Vaccine Platform: A New Era in Public Health
The FDA's launch of an AI-powered vaccine platform is a significant development in the field of public health. The platform is designed to track the side effects of drugs and vaccines, signaling a major technological shift in how the federal government monitors public health and safety. This move is expected to improve the efficiency and effectiveness of vaccine development, distribution, and monitoring. According to a recent Fox News Poll, voters are expressing their expectations for AI to transform everyday life, and the FDA's move is a step in that direction.

The FDA's AI-powered platform is not just a technological upgrade; it also represents a shift in the way the federal government approaches public health. By leveraging AI, the FDA can analyze large amounts of data quickly and accurately, identifying potential side effects and taking proactive measures to mitigate them. This approach is likely to improve the overall safety and efficacy of vaccines, which is critical for maintaining public trust in the healthcare system.

However, the FDA's move also raises questions about the potential risks and challenges associated with relying on AI in public health. For instance, what happens if the AI system fails to detect a serious side effect? Who will be held accountable in such cases? These are questions that policymakers and regulators will need to address as they navigate the complexities of AI adoption in public health.

## The Rapid Trajectory of AI Evolution
The rapid trajectory of AI evolution is a phenomenon that has been observed by industry experts and researchers. According to Chuck Brooks, a contributor to Forbes, AI is evolving at an accelerating pace, transitioning from narrow, data-driven tools to systems capable of reasoning, autonomous action, human augmentation, brain-inspired efficiency, and deeper human-machine integration. This development builds on basic machine learning, the rise of generative models, the move towards systems that act on their own, methods that enhance human decision-making instead of replacing it, computing inspired by neuroscience, and new forms of collaboration between humans and machines.

![Artificial Intelligence Machine Learning Large Language Model AI Technology](https://incubator.ucf.edu/wp-content/uploads/2023/07/artificial-intelligence-new-technology-science-futuristic-abstract-human-brain-ai-technology-cpu-central-processor-unit-chipset-big-data-machine-learning-cyber-mind-domination-generative-ai-scaled-1-1500x1000.jpg)

The rapid evolution of AI has significant implications for various industries, including healthcare, finance, and education. As AI systems become more advanced, they are likely to disrupt traditional business models and create new opportunities for innovation and growth. However, this also raises concerns about job displacement, bias, and accountability, which will need to be addressed through careful planning and regulation.

One of the key areas where AI is expected to have a significant impact is in the food industry. According to a recent article on News-Medical, AI is being used to design healthier and more sustainable foods, revealing how data-driven food design could transform human health, sustainability, and the future of what we eat. This development has the potential to improve public health, reduce the environmental impact of food production, and create new business opportunities in the food industry.

## AI in Food: A New Frontier for Innovation
The use of AI in food production is a relatively new development, but it has the potential to transform the way we produce, process, and consume food. By analyzing large biochemical and nutritional datasets, AI can identify novel bioactive compounds and sustainable food sources, which can be used to create healthier and more sustainable food products. This approach can also help reduce food waste, improve supply chain efficiency, and create new business opportunities in the food industry.

![Artificial Intelligence Robot Thinking Brain](https://scitechdaily.com/images/Artificial-Intelligence-Robot-Thinking-Brain.jpg)

The integration of AI in food production also raises questions about the potential risks and challenges associated with this development. For instance, what happens if AI-designed foods are not safe for human consumption? Who will be held accountable in such cases? These are questions that policymakers and regulators will need to address as they navigate the complexities of AI adoption in the food industry.

Despite these challenges, the use of AI in food production has the potential to create significant benefits for human health, sustainability, and the economy. By leveraging AI, food producers can create healthier and more sustainable food products, which can improve public health and reduce the environmental impact of food production. This development also has the potential to create new business opportunities in the food industry, from precision agriculture to personalized nutrition.

## What This Week Signals
The developments of the past week signal a structural shift in the way AI is being integrated into various aspects of our lives. The FDA's launch of an AI-powered vaccine platform, the rapid trajectory of AI evolution, and the use of AI in food production all point to a future where AI is increasingly embedded in our daily lives. While there are potential risks and challenges associated with this development, the benefits of AI adoption are likely to outweigh the costs.

As we move forward, it is essential to address the potential risks and challenges associated with AI adoption, from job displacement to bias and accountability. Policymakers and regulators will need to navigate the complexities of AI adoption, creating regulations and guidelines that promote innovation while protecting public safety and well-being.

In the next 6-12 months, we can expect to see significant developments in the field of AI, from advancements in machine learning to increased adoption in various industries. The key will be to balance the benefits of AI adoption with the potential risks and challenges, creating a future where AI is used to improve human life while minimizing its negative consequences. As we embark on this journey, it is essential to remain vigilant, addressing the potential risks and challenges associated with AI adoption while promoting innovation and growth.
```

## File: `frontend/blogs/ainews/the-week-in-ai-4.md`
```markdown
# The Week in AI #4
The primary header image for this article is not provided.

This week, the artificial intelligence (AI) landscape witnessed significant developments that underscore the technology's growing presence in various sectors. From the deployment of wall-climbing robots on US Navy warships to the integration of AI in content creation and crypto exchange workforce management, the pace of AI adoption is accelerating. These advancements not only reflect the evolving nature of technological innovation but also highlight the complex interplay between AI, geopolitics, and the global economy.

## Wall-Climbing Robots and the Future of Naval Warfare
The introduction of wall-climbing robots on US Navy warships marks a new frontier in naval technology. These robots, capable of swarming and crawling on warships, represent a significant leap in autonomous systems designed for military applications. The development and deployment of such technology are part of a broader trend where nations are investing heavily in AI and robotics to enhance their military capabilities. This shift towards autonomous and AI-driven systems in naval warfare signals a potential revolution in how future conflicts may be waged.

The use of wall-climbing robots on warships can significantly enhance inspection, maintenance, and potentially even combat operations. These robots can access areas of the ship that are difficult or dangerous for human personnel to reach, thereby improving the efficiency and safety of naval operations. Moreover, the swarming capability of these robots allows for complex tasks to be performed with greater precision and speed than would be possible with traditional manned systems.

However, the integration of AI and robotics in military contexts also raises significant questions about the future of warfare. As autonomous systems become more prevalent, there is a growing need for clear international norms and regulations governing their use. The ethical implications of deploying autonomous weapons systems are profound, and the international community must engage in a thorough discussion about the boundaries and safeguards necessary to prevent unintended consequences.

The development of wall-climbing robots for naval use is also reflective of the broader competition between nations in the field of AI and military technology. The United States, China, and other major powers are investing heavily in AI research and development, with a focus on applying these technologies to enhance their military capabilities. This competition is driving innovation but also increases the risk of an arms race in autonomous and AI-driven weapons systems.

## AI in Content Creation: The Quicken Example
In a different sector, Quicken, a well-known personal finance software company, has been leveraging AI to produce a vast amount of content. By utilizing large language models (LLMs) and AI answer engines, Quicken aims to better reach consumers who are increasingly using these tools for their financial queries. This strategy reflects a broader trend in content creation, where companies are turning to AI to generate high volumes of content efficiently.

Quicken's approach to content creation through AI underscores the potential of these technologies to disrupt traditional marketing and customer engagement strategies. By generating over 100 pieces of content every few weeks, Quicken can maintain a strong online presence and provide valuable information to its users. However, this also raises questions about the quality and authenticity of AI-generated content, as well as the potential for misinformation.

The use of AI in content creation also highlights the evolving role of human creators in the digital age. As AI systems become more sophisticated, they are capable of performing tasks that were previously the exclusive domain of humans. This shift necessitates a reevaluation of how we value and compensate creative work, as well as how we ensure that AI-generated content is transparent, accurate, and serves the public interest.

## Crypto Exchange Workforce and the AI Push
Crypto.com, a leading cryptocurrency exchange, has announced significant job cuts as part of its strategy to accelerate the integration of AI across its operations. This move reflects a broader trend in the crypto and financial services sector, where companies are looking to leverage AI to streamline their operations, enhance customer service, and remain competitive.

The decision by Crypto.com to reduce its workforce by around 12% and focus on AI integration is indicative of the structural changes underway in the crypto industry. As AI technologies become more advanced, they are enabling crypto exchanges to automate many processes, from customer support to risk management. This automation can lead to significant efficiency gains but also poses challenges for workers in sectors where tasks are increasingly being performed by machines.

The push towards AI in the crypto sector also has implications for regulatory frameworks and consumer protection. As AI systems become more integral to financial services, there is a growing need for regulators to understand the risks and benefits associated with these technologies. This includes ensuring that AI systems are transparent, fair, and do not exacerbate existing financial risks.

## What This Week Signals
The developments in AI this week, from the deployment of wall-climbing robots to the integration of AI in content creation and crypto exchange workforce management, signal a structural shift towards greater adoption and reliance on AI technologies across various sectors. This shift is driven by the potential of AI to enhance efficiency, precision, and innovation, but it also raises significant questions about the future of work, the ethics of autonomous systems, and the need for regulatory frameworks that can keep pace with technological change.

As we look to the future, it is clear that AI will continue to play an increasingly important role in shaping the global economy, geopolitics, and societal norms. The key challenges ahead will involve navigating the complex interplay between technological innovation, economic growth, and social responsibility. This will require concerted efforts from governments, industries, and civil society to ensure that the benefits of AI are equitably distributed and that its risks are mitigated.

In the coming months, we can expect to see further advancements in AI technologies, with potential breakthroughs in areas such as natural language processing, computer vision, and predictive analytics. These advancements will continue to drive innovation in sectors such as healthcare, finance, and education, but they will also pose challenges for workers, policymakers, and regulators.

Ultimately, the future of AI will be shaped by the choices we make today. As we embrace the potential of AI to transform our world, we must also engage in a thoughtful and inclusive discussion about the implications of these technologies and work towards creating a future where the benefits of AI are available to all, while its risks are managed for the common good.
```

## File: `frontend/blogs/ainews/the-week-in-ai-5.md`
```markdown
# The Week in AI #5

As the world grapples with the implications of artificial intelligence, this week has seen a significant shift in the landscape of AI development and deployment. With capital movement, regulatory friction, and geopolitical tension all playing a role, it's clear that the AI industry is at a critical inflection point. One of the key trends that has emerged this week is the increasing focus on the development of more sophisticated and specialized AI systems, particularly in the areas of natural language processing and computer vision. This shift is being driven by the growing demand for AI-powered solutions in industries such as healthcare, finance, and transportation.

The development of more advanced AI systems is also being driven by the increasing availability of large datasets and advances in computing power. This has enabled researchers and developers to create more complex and sophisticated models, which are capable of performing tasks that were previously thought to be the exclusive domain of humans. For example, recent breakthroughs in natural language processing have enabled AI systems to generate text that is indistinguishable from that written by humans, with significant implications for industries such as content creation and customer service.

However, the development and deployment of these advanced AI systems also raises significant regulatory and geopolitical concerns. As AI becomes increasingly ubiquitous, there is a growing need for clear and consistent regulations to govern its development and use. This is particularly true in areas such as data privacy and security, where the use of AI can have significant implications for individuals and organizations. The lack of clear regulations in these areas is creating uncertainty and risk for businesses and individuals, and is likely to be a major focus of attention in the coming months.

The geopolitical implications of AI are also becoming increasingly significant. As countries such as the United States, China, and Russia invest heavily in AI research and development, there is a growing risk of a new era of technological competition and conflict. This could have significant implications for global stability and security, particularly if AI is used to develop new forms of weaponry or to disrupt critical infrastructure. The need for international cooperation and agreement on the development and use of AI is becoming increasingly urgent, and is likely to be a major focus of attention in the coming years.

## The Rise of Specialized AI Systems

One of the key trends that has emerged in the AI industry this week is the increasing focus on the development of more specialized AI systems. These systems are designed to perform specific tasks, such as natural language processing or computer vision, and are being developed to meet the growing demand for AI-powered solutions in industries such as healthcare, finance, and transportation. The development of these specialized systems is being driven by the growing availability of large datasets and advances in computing power, which are enabling researchers and developers to create more complex and sophisticated models.

For example, recent breakthroughs in natural language processing have enabled AI systems to generate text that is indistinguishable from that written by humans. This has significant implications for industries such as content creation and customer service, where AI-powered systems can be used to generate high-quality content and respond to customer inquiries. The development of these systems is also being driven by the growing demand for AI-powered solutions in areas such as language translation and sentiment analysis.

However, the development of these specialized AI systems also raises significant challenges and risks. One of the key challenges is the need for high-quality training data, which is essential for the development of accurate and reliable AI models. The lack of high-quality training data can result in AI systems that are biased or inaccurate, which can have significant implications for individuals and organizations. The need for clear and consistent regulations to govern the development and use of AI is also becoming increasingly urgent, particularly in areas such as data privacy and security.

The development of specialized AI systems is also likely to have significant implications for the workforce. As AI systems become increasingly capable of performing tasks that were previously thought to be the exclusive domain of humans, there is a growing risk of job displacement and unemployment. This is particularly true in areas such as customer service and content creation, where AI-powered systems can be used to generate high-quality content and respond to customer inquiries. The need for workers to develop new skills and adapt to the changing job market is becoming increasingly urgent, and is likely to be a major focus of attention in the coming months.

## The Growing Importance of Data Quality

The growing importance of data quality is another key trend that has emerged in the AI industry this week. As AI systems become increasingly sophisticated and specialized, the need for high-quality training data is becoming increasingly urgent. High-quality training data is essential for the development of accurate and reliable AI models, and the lack of high-quality training data can result in AI systems that are biased or inaccurate. The need for clear and consistent regulations to govern the development and use of AI is also becoming increasingly urgent, particularly in areas such as data privacy and security.

The importance of data quality is also being driven by the growing demand for AI-powered solutions in industries such as healthcare and finance. In these industries, the use of AI can have significant implications for individuals and organizations, and the need for high-quality training data is essential for the development of accurate and reliable AI models. The lack of high-quality training data can result in AI systems that are biased or inaccurate, which can have significant implications for individuals and organizations.

The need for high-quality training data is also being driven by the growing availability of large datasets and advances in computing power. These advances are enabling researchers and developers to create more complex and sophisticated models, which are capable of performing tasks that were previously thought to be the exclusive domain of humans. However, the development of these models also raises significant challenges and risks, particularly in areas such as data privacy and security.

The growing importance of data quality is also likely to have significant implications for the workforce. As AI systems become increasingly capable of performing tasks that were previously thought to be the exclusive domain of humans, there is a growing risk of job displacement and unemployment. This is particularly true in areas such as data science and analytics, where the use of AI can automate many tasks and processes. The need for workers to develop new skills and adapt to the changing job market is becoming increasingly urgent, and is likely to be a major focus of attention in the coming months.

## The Geopolitical Implications of AI

The geopolitical implications of AI are becoming increasingly significant, as countries such as the United States, China, and Russia invest heavily in AI research and development. This is creating a new era of technological competition and conflict, with significant implications for global stability and security. The use of AI can have significant implications for military power and national security, particularly if AI is used to develop new forms of weaponry or to disrupt critical infrastructure.

The geopolitical implications of AI are also being driven by the growing demand for AI-powered solutions in industries such as healthcare and finance. In these industries, the use of AI can have significant implications for individuals and organizations, and the need for clear and consistent regulations to govern the development and use of AI is becoming increasingly urgent. The lack of clear regulations in these areas is creating uncertainty and risk for businesses and individuals, and is likely to be a major focus of attention in the coming months.

The need for international cooperation and agreement on the development and use of AI is becoming increasingly urgent, particularly in areas such as data privacy and security. The use of AI can have significant implications for global stability and security, particularly if AI is used to develop new forms of weaponry or to disrupt critical infrastructure. The need for clear and consistent regulations to govern the development and use of AI is essential for mitigating these risks and ensuring that the benefits of AI are shared by all.

The geopolitical implications of AI are also likely to have significant implications for the global economy. As countries such as the United States, China, and Russia invest heavily in AI research and development, there is a growing risk of a new era of technological competition and conflict. This could have significant implications for global trade and investment, particularly if AI is used to develop new forms of protectionism or to disrupt critical infrastructure. The need for international cooperation and agreement on the development and use of AI is becoming increasingly urgent, and is likely to be a major focus of attention in the coming months.

## What This Week Signals

This week's developments in the AI industry signal a significant shift in the landscape of AI development and deployment. The increasing focus on the development of more sophisticated and specialized AI systems, particularly in areas such as natural language processing and computer vision, is driving a new era of technological innovation and competition. The growing importance of data quality and the need for clear and consistent regulations to govern the development and use of AI are also becoming increasingly urgent, particularly in areas such as data privacy and security.

The geopolitical implications of AI are also becoming increasingly significant, as countries such as the United States, China, and Russia invest heavily in AI research and development. This is creating a new era of technological competition and conflict, with significant implications for global stability and security. The need for international cooperation and agreement on the development and use of AI is becoming increasingly urgent, particularly in areas such as data privacy and security.

One of the key trends that is likely to shape the AI industry in the coming months is the increasing focus on the development of more specialized AI systems. These systems are designed to perform specific tasks, such as natural language processing or computer vision, and are being developed to meet the growing demand for AI-powered solutions in industries such as healthcare, finance, and transportation. The development of these systems is being driven by the growing availability of large datasets and advances in computing power, which are enabling researchers and developers to create more complex and sophisticated models.

However, the development of these specialized AI systems also raises significant challenges and risks, particularly in areas such as data privacy and security. The lack of clear regulations in these areas is creating uncertainty and risk for businesses and individuals, and is likely to be a major focus of attention in the coming months. The need for international cooperation and agreement on the development and use of AI is becoming increasingly urgent, particularly in areas such as data privacy and security.

Overall, this week's developments in the AI industry signal a significant shift in the landscape of AI development and deployment. The increasing focus on the development of more sophisticated and specialized AI systems, the growing importance of data quality, and the need for clear and consistent regulations to govern the development and use of AI are all driving a new era of technological innovation and competition. The geopolitical implications of AI are also becoming increasingly significant, and the need for international cooperation and agreement on the development and use of AI is becoming increasingly urgent. As the AI industry continues to evolve and grow, it is likely that these trends will continue to shape the landscape of AI development and deployment, with significant implications for individuals, organizations, and societies around the world.
```

## File: `frontend/blogs/cv/articles.json`
```json
[
  {
    "id": "blogs/cv/image-filtering-convolution.md",
    "category": "cv",
    "title": "Image Filtering Convolution",
    "description": "Learn image filtering and convolution techniques for better image processing",
    "date": "2026-03-27",
    "tags": [
      "image-filtering",
      "convolutional-neural-networks",
      "computer-vision",
      "deep-learning",
      "image-processing"
    ],
    "readTime": "6 min",
    "file": "blogs/cv/image-filtering-convolution.md"
  },
  {
    "id": "blogs/cv/image-representation.md",
    "category": "cv",
    "title": "Image Representation",
    "description": "Learn image representation and color spaces for better computer vision",
    "date": "2026-03-20",
    "tags": [
      "computer-vision",
      "image-processing",
      "color-spaces",
      "image-representation",
      "deep-learning"
    ],
    "readTime": "6 min",
    "file": "blogs/cv/image-representation.md"
  },
  {
    "id": "blogs/cv/digital-image-basics.md",
    "category": "cv",
    "title": "Digital Image Basics",
    "description": "Learn digital image fundamentals and improve your computer vision skills",
    "date": "2026-03-13",
    "tags": [
      "computer-vision",
      "digital-image-processing",
      "image-analysis",
      "image-representation",
      "pixel-manipulation"
    ],
    "readTime": "6 min",
    "file": "blogs/cv/digital-image-basics.md"
  },
  {
    "id": "blogs/cv/computer-vision-intro.md",
    "category": "cv",
    "title": "Computer Vision Intro",
    "description": "Learn computer vision basics and applications. Discover image processing techniques",
    "date": "2026-03-06",
    "tags": [
      "computer-vision",
      "image-processing",
      "machine-learning",
      "deep-learning",
      "ai-techniques"
    ],
    "readTime": "6 min",
    "file": "blogs/cv/computer-vision-intro.md"
  }
]
```

## File: `frontend/blogs/cv/computer-vision-intro.md`
```markdown
## Introduction
Hello and welcome to the world of Computer Vision, a field that has been rapidly evolving over the past decade. As ML engineers and AI developers, we've all experienced the frustration of deploying computer vision models that fail to generalize well to real-world scenarios. One of the primary bottlenecks in previous approaches has been the reliance on hand-engineered features, which often fail to capture the complexity of the visual world. This limitation matters because it hinders the ability of computer vision systems to scale and adapt to diverse environments. The strategic importance of computer vision cannot be overstated, as it has the potential to revolutionize industries such as healthcare, transportation, and security. In this blog post, we'll delve into the core concepts of computer vision, walk through a technical implementation example, and explore real-world applications. By the end of this post, you'll have a deep understanding of how computer vision works under the hood and be able to build and deploy your own computer vision systems.

The shift towards deep learning-based approaches has been a significant turning point in the field of computer vision. The ability of convolutional neural networks (CNNs) to learn features from raw pixel data has enabled the development of highly accurate image classification, object detection, and segmentation models. However, as we'll discuss later, the deployment of these models in real-world scenarios poses significant challenges. To address these challenges, it's essential to understand the core concepts of computer vision, including image processing, feature extraction, and model architecture.

## Core Concepts
At its core, computer vision is about enabling machines to interpret and understand visual data from the world. This involves a series of complex steps, including image acquisition, preprocessing, feature extraction, and model inference. One of the key concepts in computer vision is the idea of convolutional neural networks (CNNs), which are designed to take advantage of the spatial hierarchy of images. CNNs consist of multiple layers, including convolutional layers, pooling layers, and fully connected layers. The convolutional layers apply filters to small regions of the image, generating feature maps that capture local patterns and textures.

| Approach | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Traditional Computer Vision | Hand-engineered features, rule-based systems | Interpretability, efficiency | Limited accuracy, lack of scalability |
| Deep Learning-based Computer Vision | Learned features, data-driven models | High accuracy, scalability | Complexity, require large datasets |

The choice of approach depends on the specific application and the characteristics of the data. Traditional computer vision approaches are often more interpretable and efficient but lack the accuracy and scalability of deep learning-based approaches. On the other hand, deep learning-based approaches require large datasets and can be computationally expensive.

## Technical Walkthrough
Let's walk through a technical implementation example using Python and the Keras library. We'll build a simple image classification model using a CNN architecture. First, we need to import the necessary libraries and load the dataset.
```python
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense

# Load the dataset
train_dir = 'path/to/train/directory'
validation_dir = 'path/to/validation/directory'

train_datagen = ImageDataGenerator(rescale=1./255)
validation_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical')

validation_generator = validation_datagen.flow_from_directory(
    validation_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical')
```
Next, we define the CNN architecture using the Keras `Sequential` API.
```python
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Conv2D(128, (3, 3), activation='relu'))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))
```
We compile the model using the `adam` optimizer and `categorical_crossentropy` loss function.
```python
model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
```
Finally, we train the model using the `fit` method.
```python
history = model.fit(train_generator,
                    steps_per_epoch=train_generator.samples // 32,
                    epochs=10,
                    validation_data=validation_generator,
                    validation_steps=validation_generator.samples // 32)
```
This example demonstrates the basic steps involved in building and training a CNN model for image classification. The choice of architecture, hyperparameters, and optimization algorithm depends on the specific application and the characteristics of the data.

## Real-World Applications
Computer vision has numerous real-world applications, including image classification, object detection, segmentation, and tracking. Let's consider three substantial deployment scenarios:

1. **Self-Driving Cars**: Computer vision is a critical component of self-driving cars, enabling them to detect and respond to their environment. The system must be able to detect lanes, pedestrians, traffic signals, and other vehicles in real-time.
2. **Medical Image Analysis**: Computer vision can be used to analyze medical images, such as X-rays and MRI scans, to detect diseases and diagnose conditions. The system must be able to segment images, detect anomalies, and provide accurate diagnoses.
3. **Surveillance Systems**: Computer vision can be used to monitor and analyze surveillance footage, detecting suspicious activity and alerting authorities. The system must be able to track objects, detect motion, and recognize patterns.

In each of these scenarios, the computer vision system must be able to operate in real-time, processing large amounts of data and making accurate decisions. The choice of architecture, hyperparameters, and optimization algorithm depends on the specific application and the characteristics of the data.

## Production Considerations
When deploying computer vision models in production, several considerations come into play. One of the primary concerns is the potential for **data drift**, where the distribution of the data changes over time, affecting the performance of the model. To address this issue, it's essential to monitor the performance of the model in real-time, using metrics such as accuracy, precision, and recall.

Another consideration is the **interpretability** of the model, which is critical in applications such as medical image analysis. Techniques such as **saliency maps** and **feature importance** can be used to provide insights into the decision-making process of the model.

Finally, **scalability** is a significant concern in computer vision applications, where large amounts of data must be processed in real-time. Techniques such as **distributed computing** and **parallel processing** can be used to improve the scalability of the system.

## Conclusion
In conclusion, computer vision is a complex and fascinating field that has the potential to revolutionize numerous industries. By understanding the core concepts of computer vision, including image processing, feature extraction, and model architecture, we can build and deploy highly accurate models that operate in real-time. The choice of approach depends on the specific application and the characteristics of the data, and considerations such as data drift, interpretability, and scalability must be taken into account when deploying models in production. As the field of computer vision continues to evolve, we can expect to see significant advancements in areas such as **explainability**, **transfer learning**, and **edge computing**. By staying at the forefront of these developments, we can unlock the full potential of computer vision and create innovative solutions that transform the way we live and work.
```

## File: `frontend/blogs/cv/digital-image-basics.md`
```markdown
Hello and welcome to this in-depth exploration of digital image fundamentals. As ML engineers and AI developers, we've all encountered the challenge of scaling image processing pipelines, only to be bottlenecked by the sheer volume of data or the complexity of image features. Traditional approaches to image analysis, relying heavily on manual feature engineering and rule-based systems, have often fallen short in terms of accuracy, efficiency, and adaptability. The shift towards deep learning-based methods has significantly improved the landscape, but understanding the basics of digital images remains crucial for harnessing the full potential of these technologies. In this article, we will delve into the core concepts of digital images, walk through a technical implementation, explore real-world applications, discuss production considerations, and finally, offer insights into future developments. By the end of this journey, readers will have a comprehensive understanding of digital image fundamentals and be equipped to build and optimize their own image processing systems.

## Core Concepts

At the heart of digital image processing lies the representation of images as digital data. A digital image is essentially a matrix of pixels, where each pixel is assigned a color value. The color value can be represented in various formats such as RGB (Red, Green, Blue), grayscale, or even more complex models like CMYK (Cyan, Magenta, Yellow, Key/Black) for printing. Understanding these color models is essential because they directly impact how images are processed and analyzed. For instance, converting an image from RGB to grayscale simplifies the data, reducing it to a single channel of intensity values, which can significantly speed up processing but may also lose valuable color information.

Another critical aspect is the resolution and size of the image. The resolution, measured in pixels per inch (PPI) or dots per inch (DPI), affects the image's clarity and detail. Higher resolutions mean more detailed images but also larger file sizes and increased processing requirements. The size of the image, in terms of dimensions (width and height in pixels), influences not only the file size but also how the image is displayed and processed. Resizing images, either by downsampling (reducing the size) or upsampling (increasing the size), involves interpolation techniques that can either preserve or degrade image quality, depending on the method used.

When images are misunderstood or misprocessed, it can lead to a range of issues from poor image quality to failed analysis. For example, applying a filter designed for RGB images to a grayscale image without proper conversion can result in unexpected outcomes. Similarly, failing to consider the aspect ratio during resizing can distort the image, making it unusable for certain applications.

The following table compares some common image formats and their characteristics:

| Format | Compression | Color Depth | Typical Use |
| --- | --- | --- | --- |
| JPEG | Lossy | 24-bit | Photographs, web images |
| PNG | Lossless | 8-bit, 24-bit, 32-bit | Graphics, icons, screenshots |
| TIFF | Lossless | Variable | Professional printing, medical imaging |
| GIF | Lossless | 8-bit | Animated web graphics |

## Technical Walkthrough

To illustrate the concepts discussed, let's implement a basic image processing pipeline using Python with the Pillow library for image manipulation and NumPy for numerical operations. Our goal is to load an image, convert it to grayscale, apply a Gaussian blur, and then save the processed image.

```python
from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter

# Load the image
img = Image.open('input.jpg')

# Convert the image to grayscale
gray_img = img.convert('L')

# Convert the grayscale image to a NumPy array
gray_array = np.array(gray_img)

# Apply a Gaussian blur
blurred_array = gaussian_filter(gray_array, sigma=2)

# Convert the blurred array back to an image
blurred_img = Image.fromarray(blurred_array.astype(np.uint8))

# Save the blurred image
blurred_img.save('blurred_output.jpg')
```

This example demonstrates how to work with images in Python, performing basic operations like format conversion and applying filters. The choice of using a Gaussian blur, for instance, is based on its effectiveness in reducing noise while preserving edges, a common requirement in image preprocessing for both human viewing and machine learning model inputs.

## Real-World Applications

Digital image fundamentals are not just theoretical concepts; they have profound implications in various real-world applications. 

1. **Medical Imaging**: In medical diagnostics, the ability to accurately process and analyze images from MRI scans, X-rays, and CT scans is critical. Understanding the specifics of image formats, such as DICOM, and the implications of image processing techniques on diagnostic accuracy is vital.

2. **Autonomous Vehicles**: The success of autonomous vehicles heavily relies on their ability to interpret visual data from cameras, LiDAR, and other sensors. This involves complex image processing to detect lanes, recognize objects, and predict trajectories, all of which demand a deep understanding of digital image fundamentals.

3. **E-commerce and Retail**: High-quality product images are essential for e-commerce platforms. Optimizing image compression to balance quality and file size, ensuring consistent image formatting across different devices and browsers, and leveraging image analysis for product recommendation and search are just a few areas where digital image fundamentals play a crucial role.

## Production Considerations

When deploying image processing systems in production, several considerations come into play. Monitoring the system's performance, evaluating the drift in image data over time, and scaling the system to handle increased traffic or larger image sizes are critical. Optimizing image processing pipelines for cloud environments or edge devices requires careful consideration of computational resources, memory constraints, and network bandwidth.

Moreover, the choice of image formats and compression algorithms can significantly impact the system's efficiency and user experience. For instance, using WebP instead of JPEG for web images can offer better compression ratios without sacrificing quality, leading to faster page loads and improved user engagement.

## Conclusion

In conclusion, digital image fundamentals are the backbone of any image processing or computer vision system. Understanding how images are represented, processed, and analyzed is crucial for developing efficient, scalable, and accurate systems. As we move forward, the increasing demand for high-quality visual content, coupled with advancements in AI and machine learning, will continue to push the boundaries of what is possible with digital images. By grasping these fundamentals and staying abreast of the latest developments, practitioners can unlock new applications and innovations, driving progress in fields from healthcare and transportation to entertainment and beyond. The journey into the world of digital images is both challenging and rewarding, offering a wealth of opportunities for those who are willing to explore and innovate.
```

## File: `frontend/blogs/cv/image-filtering-convolution.md`
```markdown
## Introduction
Hello and welcome to this technical blog post on Image Filtering and Convolution. As machine learning engineers and AI developers, we've all encountered the challenge of deploying image processing models that can efficiently handle large volumes of data while maintaining high accuracy. One of the major bottlenecks in previous approaches has been the use of traditional image filtering techniques, which often rely on simple averaging or median filtering. However, these methods can be limited in their ability to preserve image details and can lead to blurring or loss of important features. 

The strategic importance of image filtering and convolution lies in their ability to enhance image quality, remove noise, and extract relevant features, which are crucial in various applications such as object detection, image segmentation, and facial recognition. In this blog post, we will delve into the core concepts of image filtering and convolution, exploring how they work under the hood, and what can go wrong when they are misunderstood. By the end of this post, readers will have a deep understanding of image filtering and convolution, and will be able to build and deploy their own image processing models using these techniques.

The recent shift towards deep learning-based approaches has led to significant improvements in image processing tasks. Convolutional Neural Networks (CNNs), in particular, have revolutionized the field of computer vision, achieving state-of-the-art results in image classification, object detection, and segmentation. However, the success of these models relies heavily on the quality of the input images, which is where image filtering and convolution come into play. 

## Core Concepts
Image filtering and convolution are fundamental concepts in image processing, and are used to enhance or transform images by applying a set of predefined rules. The key idea behind image filtering is to slide a small window, known as a kernel or filter, over the entire image, performing a dot product at each position to generate a feature map. This process is known as convolution, and it is a crucial step in many image processing tasks.

There are several types of image filters, including linear filters, non-linear filters, and adaptive filters. Linear filters, such as Gaussian filters and Sobel filters, are commonly used for image blurring, edge detection, and noise reduction. Non-linear filters, such as median filters and bilateral filters, are used for image denoising and detail preservation. Adaptive filters, such as Wiener filters and Kalman filters, are used for image restoration and deblurring.

One of the key challenges in image filtering and convolution is the choice of kernel size and type. A small kernel size can lead to oversmoothing, while a large kernel size can lead to undersmoothing. The type of kernel used can also significantly impact the results, with different kernels suited for different tasks. For example, a Gaussian kernel is often used for image blurring, while a Sobel kernel is used for edge detection.

The following table compares some common image filtering techniques:

| Filter Type | Kernel Size | Application |
| --- | --- | --- |
| Gaussian Filter | 3x3, 5x5 | Image Blurring |
| Sobel Filter | 3x3 | Edge Detection |
| Median Filter | 3x3, 5x5 | Image Denoising |
| Bilateral Filter | 5x5, 7x7 | Image Detail Preservation |

## Technical Walkthrough
In this section, we will provide a technical walkthrough of how to implement image filtering and convolution using Python and the OpenCV library. We will use a synthetic image with added noise to demonstrate the effectiveness of different filtering techniques.

```python
import cv2
import numpy as np

# Create a synthetic image with added noise
image = np.random.rand(256, 256)
noise = np.random.randn(256, 256) * 0.1
noisy_image = image + noise

# Apply Gaussian filtering
gaussian_kernel = np.array([[1, 2, 1], [2, 4, 2], [1, 2, 1]]) / 16
gaussian_filtered_image = cv2.filter2D(noisy_image, -1, gaussian_kernel)

# Apply Sobel filtering
sobel_kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])
sobel_kernel_y = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])
sobel_filtered_image_x = cv2.filter2D(noisy_image, -1, sobel_kernel_x)
sobel_filtered_image_y = cv2.filter2D(noisy_image, -1, sobel_kernel_y)

# Display the results
cv2.imshow("Noisy Image", noisy_image)
cv2.imshow("Gaussian Filtered Image", gaussian_filtered_image)
cv2.imshow("Sobel Filtered Image X", sobel_filtered_image_x)
cv2.imshow("Sobel Filtered Image Y", sobel_filtered_image_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

This code demonstrates how to apply Gaussian and Sobel filtering to a noisy image using the OpenCV library. The results show that Gaussian filtering can effectively reduce noise, while Sobel filtering can detect edges in the image.

## Real-World Applications
Image filtering and convolution have numerous real-world applications in various fields, including:

1. **Medical Imaging**: Image filtering and convolution are used in medical imaging to enhance image quality, remove noise, and extract relevant features. For example, in MRI scans, Gaussian filtering can be used to reduce noise, while Sobel filtering can be used to detect edges and boundaries.
2. **Object Detection**: Image filtering and convolution are used in object detection to detect and classify objects in images. For example, in self-driving cars, convolutional neural networks (CNNs) can be used to detect pedestrians, cars, and other objects.
3. **Facial Recognition**: Image filtering and convolution are used in facial recognition to enhance image quality, remove noise, and extract relevant features. For example, in security systems, Gaussian filtering can be used to reduce noise, while Sobel filtering can be used to detect edges and boundaries.

## Production Considerations
When deploying image filtering and convolution models in production, there are several considerations to keep in mind:

1. **Bottlenecks**: Image filtering and convolution can be computationally expensive, especially for large images. To avoid bottlenecks, it's essential to optimize the code and use parallel processing techniques.
2. **Edge Cases**: Image filtering and convolution can be sensitive to edge cases, such as images with varying lighting conditions or images with noise. To handle edge cases, it's essential to test the model thoroughly and use techniques such as data augmentation.
3. **Failure Modes**: Image filtering and convolution can fail in certain scenarios, such as images with complex backgrounds or images with multiple objects. To handle failure modes, it's essential to use techniques such as error detection and correction.

## Conclusion
In conclusion, image filtering and convolution are powerful techniques used in image processing to enhance image quality, remove noise, and extract relevant features. By understanding the core concepts of image filtering and convolution, and by using techniques such as Gaussian and Sobel filtering, we can build and deploy image processing models that can efficiently handle large volumes of data while maintaining high accuracy. As machine learning engineers and AI developers, it's essential to stay up-to-date with the latest advancements in image filtering and convolution, and to explore new techniques and applications in this field.
```

## File: `frontend/blogs/cv/image-representation.md`
```markdown
## Introduction
Hello and welcome to this technical blog post on image representation, a crucial aspect of computer vision and machine learning. As ML engineers and AI developers, we've all encountered the challenge of deploying models that can efficiently process and analyze visual data. However, traditional approaches to image representation have often been bottlenecked by the choice of color space, leading to suboptimal performance and scalability issues. In this post, we'll delve into the core concepts of image representation, exploring the different color spaces and their implications on model performance. By the end of this article, you'll understand how to choose the right color space for your application, implement efficient image processing pipelines, and deploy scalable computer vision systems.

The importance of image representation cannot be overstated, as it directly affects the accuracy and robustness of downstream tasks such as object detection, segmentation, and classification. With the increasing demand for computer vision capabilities in various industries, including healthcare, autonomous vehicles, and surveillance, the need for efficient and effective image representation has never been more pressing. In this post, we'll discuss the strategic importance of image representation, highlighting the key challenges and opportunities in this field.

## Core Concepts
At the heart of image representation lies the concept of color spaces, which define the way colors are encoded and processed in digital images. The most common color spaces used in computer vision are RGB (Red, Green, Blue), HSV (Hue, Saturation, Value), and YUV (Luminance and Chrominance). Each color space has its strengths and weaknesses, and the choice of color space depends on the specific application and requirements.

| Color Space | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| RGB | Additive color model | Simple to implement, widely supported | Not perceptually uniform, sensitive to illumination changes |
| HSV | Color model based on human perception | Intuitive, robust to illumination changes | Computationally expensive, not suitable for all applications |
| YUV | Color model separating luminance and chrominance | Efficient for video compression, robust to illumination changes | Not suitable for all applications, requires careful conversion |

Understanding the differences between these color spaces is crucial for designing effective image processing pipelines. For instance, the RGB color space is simple to implement but may not be suitable for applications where illumination changes are significant. On the other hand, the HSV color space is more robust to illumination changes but can be computationally expensive.

## Technical Walkthrough
To illustrate the concepts discussed above, let's consider a simple example of image processing using Python and the OpenCV library. In this example, we'll convert an image from the RGB color space to the HSV color space and apply a threshold to separate the objects from the background.

```python
import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to HSV color space
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define the threshold range for the HSV color space
lower_threshold = np.array([0, 0, 0])
upper_threshold = np.array([255, 255, 255])

# Apply the threshold to the HSV image
thresholded_img = cv2.inRange(hsv_img, lower_threshold, upper_threshold)

# Display the original and thresholded images
cv2.imshow('Original Image', img)
cv2.imshow('Thresholded Image', thresholded_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
```

In this example, we use the `cv2.cvtColor` function to convert the image from the RGB color space to the HSV color space. We then define the threshold range for the HSV color space and apply the threshold using the `cv2.inRange` function. The resulting thresholded image is displayed alongside the original image.

## Real-World Applications
Image representation has numerous applications in various industries, including healthcare, autonomous vehicles, and surveillance. For instance, in healthcare, image representation is used in medical imaging to analyze and diagnose diseases. In autonomous vehicles, image representation is used for object detection and tracking, enabling the vehicle to navigate safely and efficiently.

Let's consider a few deployment scenarios:

1. **Medical Imaging**: In medical imaging, image representation is used to analyze and diagnose diseases such as cancer. The choice of color space depends on the specific application and requirements. For instance, the RGB color space may be suitable for visualizing anatomical structures, while the HSV color space may be more suitable for analyzing tissue properties.
2. **Autonomous Vehicles**: In autonomous vehicles, image representation is used for object detection and tracking. The YUV color space is commonly used in video compression, making it a suitable choice for autonomous vehicles where real-time video processing is required.
3. **Surveillance**: In surveillance, image representation is used for object detection and tracking. The choice of color space depends on the specific application and requirements. For instance, the RGB color space may be suitable for visualizing objects in a scene, while the HSV color space may be more suitable for analyzing object properties such as color and texture.

## Production Considerations
When deploying image representation systems in production, several considerations must be taken into account. These include:

* **Bottlenecks**: Image representation can be computationally expensive, especially when dealing with large images or complex color spaces. Optimizing the image processing pipeline to minimize computational overhead is crucial.
* **Edge Cases**: Image representation can be sensitive to edge cases such as illumination changes, occlusions, or noise. Robustness to these edge cases must be ensured to maintain system performance and accuracy.
* **Failure Modes**: Image representation can fail in various ways, including incorrect color space conversion, thresholding errors, or object detection failures. Monitoring and evaluation of system performance are essential to detect and correct these failures.

To address these considerations, several strategies can be employed, including:

* **Optimization**: Optimizing the image processing pipeline to minimize computational overhead and improve system performance.
* **Robustness**: Ensuring robustness to edge cases such as illumination changes, occlusions, or noise.
* **Monitoring**: Monitoring system performance and evaluating drift to detect and correct failures.

## Conclusion
In conclusion, image representation is a crucial aspect of computer vision and machine learning, with significant implications for model performance and scalability. By understanding the core concepts of color spaces and their implications on model performance, ML engineers and AI developers can design effective image processing pipelines and deploy scalable computer vision systems. The choice of color space depends on the specific application and requirements, and several considerations must be taken into account when deploying image representation systems in production. As the demand for computer vision capabilities continues to grow, the importance of image representation will only continue to increase, making it a vital area of research and development in the field of machine learning and artificial intelligence.
```

## File: `frontend/blogs/dl/articles.json`
```json
[
  {
    "id": "blogs/dl/deep-learning-intro.md",
    "category": "dl",
    "title": "Deep Learning Intro",
    "description": "Learn deep learning fundamentals and boost your AI skills",
    "date": "2026-03-03",
    "tags": [
      "deep-learning",
      "neural-networks",
      "artificial-intelligence",
      "machine-learning",
      "ai-models"
    ],
    "readTime": "8 min",
    "file": "blogs/dl/deep-learning-intro.md"
  }
]
```

## File: `frontend/blogs/dl/deep-learning-intro.md`
```markdown
Hello and welcome to our in-depth exploration of deep learning, a subset of machine learning that has been making waves in the tech industry. As someone who has worked on numerous projects involving deep learning, I can attest to the fact that it's an exciting field that's constantly evolving. However, I've also seen firsthand the challenges that come with deploying deep learning models, particularly when it comes to scaling and performance. In my experience, one of the biggest bottlenecks is the inability of traditional machine learning models to handle complex, high-dimensional data. This is where deep learning comes in – by using neural networks with multiple layers, we can build models that are capable of learning and representing complex patterns in data.

In this blog post, we'll be diving into the world of deep learning, exploring what it is, why it's useful, and some of the most popular applications. We'll also be looking at the different types of deep learning models, including convolutional neural networks (CNNs), recurrent neural networks (RNNs), and long short-term memory (LSTM) networks. By the end of this post, you'll have a solid understanding of deep learning and be able to build your own models using popular frameworks like TensorFlow and PyTorch.

## What is Deep Learning
Deep learning is a subset of machine learning that involves the use of neural networks with multiple layers to learn and represent complex patterns in data. These neural networks are designed to mimic the structure and function of the human brain, with each layer learning to recognize and represent different features of the input data. The key idea behind deep learning is that by using multiple layers, we can build models that are capable of learning and representing complex patterns in data, such as images, speech, and text.

One of the key benefits of deep learning is its ability to handle high-dimensional data. Traditional machine learning models often struggle with high-dimensional data, as they require a large amount of computational resources and can be prone to overfitting. Deep learning models, on the other hand, are designed to handle high-dimensional data with ease, making them ideal for applications such as image and speech recognition.

### Why Use Deep Learning
So, why use deep learning? There are several reasons why deep learning has become so popular in recent years. Firstly, deep learning models are capable of achieving state-of-the-art performance on a wide range of tasks, from image and speech recognition to natural language processing and game playing. Secondly, deep learning models are highly flexible and can be used for a wide range of applications, from computer vision and robotics to healthcare and finance.

Here are some of the key benefits of using deep learning:

* **High accuracy**: Deep learning models are capable of achieving state-of-the-art performance on a wide range of tasks.
* **Flexibility**: Deep learning models can be used for a wide range of applications, from computer vision and robotics to healthcare and finance.
* **Ability to handle high-dimensional data**: Deep learning models are designed to handle high-dimensional data with ease, making them ideal for applications such as image and speech recognition.

## Example Applications
Deep learning has a wide range of applications, from computer vision and robotics to healthcare and finance. Some examples of deep learning applications include:

* **Image recognition**: Deep learning models can be used to recognize and classify images, such as objects, scenes, and activities.
* **Speech recognition**: Deep learning models can be used to recognize and transcribe speech, such as voice commands and conversations.
* **Natural language processing**: Deep learning models can be used to analyze and understand natural language, such as text and speech.

Here are some examples of deep learning applications in different industries:

| Industry | Application |
| --- | --- |
| Healthcare | Disease diagnosis, medical image analysis |
| Finance | Stock market prediction, credit risk assessment |
| Computer Vision | Object detection, image segmentation |

### Types of Deep Learning Models
There are several types of deep learning models, each with its own strengths and weaknesses. Some of the most popular types of deep learning models include:

* **Convolutional Neural Networks (CNNs)**: CNNs are designed to handle image and video data, and are commonly used for applications such as image recognition and object detection.
* **Recurrent Neural Networks (RNNs)**: RNNs are designed to handle sequential data, such as speech and text, and are commonly used for applications such as speech recognition and natural language processing.
* **Long Short-Term Memory (LSTM) Networks**: LSTMs are a type of RNN that are designed to handle long-term dependencies in data, and are commonly used for applications such as speech recognition and natural language processing.

## Technical Walkthrough
In this section, we'll be providing a technical walkthrough of a deep learning model using Python and the Keras framework. We'll be building a simple CNN model to classify images into different categories.

```python
# Import necessary libraries
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from keras.utils import to_categorical
from keras.datasets import mnist

# Load MNIST dataset
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocess data
x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255

# Define model architecture
model = Sequential()
model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(MaxPooling2D((2, 2)))
model.add(Flatten())
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# Compile model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train model
model.fit(x_train, to_categorical(y_train), epochs=10, batch_size=128, validation_data=(x_test, to_categorical(y_test)))
```

This code defines a simple CNN model using the Keras framework, and trains it on the MNIST dataset to classify images into different categories.

## Real-World Applications
Deep learning has a wide range of real-world applications, from computer vision and robotics to healthcare and finance. Some examples of deep learning applications in different industries include:

* **Healthcare**: Deep learning models can be used to analyze medical images, such as X-rays and MRIs, to diagnose diseases and predict patient outcomes.
* **Finance**: Deep learning models can be used to analyze financial data, such as stock prices and credit scores, to predict market trends and credit risk.
* **Computer Vision**: Deep learning models can be used to analyze images and videos, such as object detection and image segmentation, to enable applications such as self-driving cars and facial recognition.

Here are some examples of deep learning applications in different industries:

| Industry | Application | Description |
| --- | --- | --- |
| Healthcare | Disease diagnosis | Deep learning models can be used to analyze medical images, such as X-rays and MRIs, to diagnose diseases and predict patient outcomes. |
| Finance | Stock market prediction | Deep learning models can be used to analyze financial data, such as stock prices and credit scores, to predict market trends and credit risk. |
| Computer Vision | Object detection | Deep learning models can be used to analyze images and videos, such as object detection and image segmentation, to enable applications such as self-driving cars and facial recognition. |

## Production Considerations
When deploying deep learning models in production, there are several considerations to keep in mind. Some of the key considerations include:

* **Model performance**: Deep learning models can be computationally intensive and require significant resources to train and deploy.
* **Data quality**: Deep learning models require high-quality data to train and validate, and can be sensitive to data noise and bias.
* **Explainability**: Deep learning models can be difficult to interpret and explain, making it challenging to understand why a particular decision was made.

Here are some strategies for optimizing deep learning models in production:

* **Model pruning**: Model pruning involves removing unnecessary weights and connections in the model to reduce computational resources and improve performance.
* **Knowledge distillation**: Knowledge distillation involves training a smaller model to mimic the behavior of a larger model, allowing for more efficient deployment and inference.
* **Transfer learning**: Transfer learning involves using a pre-trained model as a starting point for a new task, allowing for faster training and improved performance.

## Conclusion
In conclusion, deep learning is a powerful tool for building complex models that can learn and represent patterns in data. With its ability to handle high-dimensional data and achieve state-of-the-art performance on a wide range of tasks, deep learning has become a key technology in many industries. However, deploying deep learning models in production requires careful consideration of model performance, data quality, and explainability. By using strategies such as model pruning, knowledge distillation, and transfer learning, we can optimize deep learning models for production and unlock their full potential.

As we look to the future, it's clear that deep learning will continue to play a major role in shaping the tech industry. With the rise of edge AI and the increasing demand for real-time processing, deep learning models will need to be optimized for performance and efficiency. Additionally, the growing importance of explainability and transparency will require new techniques and tools for interpreting and understanding deep learning models. As practitioners, it's our job to stay ahead of the curve and continue to push the boundaries of what's possible with deep learning.
```

## File: `frontend/blogs/genai/articles.json`
```json
[
  {
    "id": "blogs/genai/autoregressive-models.md",
    "category": "genai",
    "title": "Autoregressive Models",
    "description": "Learn about autoregressive models and their applications in generative AI. Improve your understanding",
    "date": "2026-03-28",
    "tags": [
      "autoregressive-models",
      "generative-ai",
      "deep-learning",
      "language-models",
      "sequence-prediction"
    ],
    "readTime": "5 min",
    "file": "blogs/genai/autoregressive-models.md"
  },
  {
    "id": "blogs/genai/generative-ai-models.md",
    "category": "genai",
    "title": "Generative AI Models",
    "description": "Learn probabilistic generative modeling for AI. Discover techniques and applications.",
    "date": "2026-03-21",
    "tags": [
      "probabilistic-models",
      "generative-ai",
      "machine-learning",
      "deep-learning",
      "natural-language-processing"
    ],
    "readTime": "6 min",
    "file": "blogs/genai/generative-ai-models.md"
  },
  {
    "id": "blogs/genai/generative-ai-intro.md",
    "category": "genai",
    "title": "Generative AI Intro",
    "description": "Learn basics of Generative AI. Discover its applications",
    "date": "2026-03-07",
    "tags": [
      "generative-models",
      "artificial-intelligence",
      "machine-learning",
      "deep-learning",
      "natural-language-processing"
    ],
    "readTime": "6 min",
    "file": "blogs/genai/generative-ai-intro.md"
  }
]
```

## File: `frontend/blogs/genai/autoregressive-models.md`
```markdown
Hello and welcome to this comprehensive exploration of Autoregressive Models, a crucial component in the arsenal of machine learning engineers and AI developers. As we navigate the complexities of predictive modeling, we often encounter deployment bottlenecks stemming from the limitations of traditional approaches. One such limitation is the inability of many models to effectively capture temporal dependencies in sequential data, a challenge that autoregressive models are particularly well-suited to address. The strategic importance of autoregressive models lies in their capacity to forecast future values based on past patterns, making them indispensable in applications ranging from financial forecasting to natural language processing. By the end of this article, readers will have a deep understanding of autoregressive models, including their core concepts, technical implementation, real-world applications, and production considerations, enabling them to build and deploy these models effectively.

## Core Concepts

At the heart of autoregressive models is the concept of using past values of a time series to forecast future values. This is based on the principle that the current value of a time series is a function of past values, rather than being independently distributed. The simplest form of an autoregressive model is the Autoregressive (AR) model of order p, denoted as AR(p), where the current value is predicted based on the previous p values. The equation for an AR(p) model can be represented as:
\[ Y_t = \beta_0 + \beta_1 Y_{t-1} + \beta_2 Y_{t-2} + \cdots + \beta_p Y_{t-p} + \epsilon_t \]
where \( Y_t \) is the value at time t, \( \beta_i \) are the coefficients, and \( \epsilon_t \) is the error term at time t.

### Understanding Autoregressive Integrated Moving Average (ARIMA) Models

A more comprehensive approach is the Autoregressive Integrated Moving Average (ARIMA) model, which combines the autoregressive (AR) and moving average (MA) components with the possibility of differencing the time series to make it stationary. The ARIMA model is denoted as ARIMA(p, d, q), where:
- p is the number of autoregressive terms,
- d is the degree of differencing,
- q is the number of moving-average terms.

The ARIMA model provides a powerful framework for modeling a wide range of time series data, but its effectiveness depends on accurately determining the parameters p, d, and q.

### Comparison of Related Approaches

| Model | Description | Use Cases |
| --- | --- | --- |
| AR | Predicts current value based on past values | Short-term forecasting, understanding temporal dependencies |
| MA | Models the error term as a combination of past errors | Smoothing out noise in time series data |
| ARIMA | Combines AR and MA components with differencing | General-purpose time series forecasting, handling non-stationarity |
| SARIMA | Seasonal ARIMA, accounts for seasonal patterns | Forecasting data with strong seasonal components, such as sales data |

## Technical Walkthrough

To illustrate the implementation of an autoregressive model, let's consider a simple example in Python using the `statsmodels` library. We'll generate a synthetic time series and then fit an AR model to it.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.ar_model import AutoReg

# Generate synthetic time series data
np.random.seed(0)
n_samples = 100
time_series = np.cumsum(np.random.normal(size=n_samples))

# Convert to pandas Series for easier manipulation
series = pd.Series(time_series)

# Plot the original time series
plt.figure(figsize=(10,6))
plt.plot(series)
plt.title('Original Time Series')
plt.show()

# Fit an AR model of order 2
model = AutoReg(series, lags=2)
model_fit = model.fit()

# Print out the coefficients
print('Coefficients: %s' % model_fit.params)
```

This example demonstrates how to generate a synthetic time series, fit an autoregressive model, and print out the coefficients. The choice of the model order (in this case, 2) is crucial and can significantly affect the forecasting performance.

## Real-World Applications

Autoregressive models have a wide range of applications across various industries. Here are three substantial deployment scenarios:

1. **Financial Forecasting:** ARIMA models are widely used in finance for forecasting stock prices, commodity prices, and exchange rates. The ability to accurately predict future values based on past patterns is crucial for making informed investment decisions.

2. **Weather Forecasting:** Autoregressive models can be applied to weather forecasting by analyzing historical climate data to predict future weather patterns. This is particularly useful for planning and managing resources in agriculture and other weather-sensitive industries.

3. **Traffic Flow Prediction:** By analyzing the temporal dependencies in traffic flow data, autoregressive models can be used to predict future traffic conditions. This information is vital for optimizing traffic light control, route planning, and reducing congestion.

## Production Considerations

When deploying autoregressive models in production, several considerations come into play:

- **Model Monitoring:** Continuous monitoring of the model's performance is essential to detect any drift in the data or degradation in forecasting accuracy.
- **Hyperparameter Tuning:** The choice of hyperparameters, such as the order of the autoregressive model, can significantly impact performance. Automated hyperparameter tuning can help optimize model performance.
- **Scalability:** As the volume of data increases, the model must be able to scale to handle larger datasets and provide timely forecasts.

## Conclusion

Autoregressive models offer a powerful tool for forecasting and analyzing time series data, leveraging the temporal dependencies inherent in sequential data. By understanding the core concepts, technical implementation, and real-world applications of these models, practitioners can build and deploy effective forecasting systems. As the field of machine learning continues to evolve, the strategic importance of autoregressive models will only grow, driven by their ability to provide actionable insights from complex data. Looking forward, advancements in autoregressive models, such as the integration of machine learning techniques and the development of more sophisticated models like SARIMA and LSTM, will further enhance their capabilities and applications, making them an indispensable component of the predictive modeling toolkit.
```

## File: `frontend/blogs/genai/generative-ai-intro.md`
```markdown
## Introduction
Hello and welcome to the world of Generative AI, where the lines between human creativity and machine learning are blurring at an unprecedented pace. As we continue to push the boundaries of what is possible with AI, we're faced with a deployment bottleneck: how do we scale our models to generate high-quality, diverse, and context-dependent content that meets the demands of real-world applications? Traditional approaches to AI have focused on discriminative models, which excel at classification and regression tasks but fall short when it comes to generating new, unseen data. This limitation matters because it hinders our ability to build AI systems that can create, innovate, and adapt to changing environments. In this blog post, we'll delve into the world of Generative AI, exploring the core concepts, technical walkthroughs, and real-world applications that are revolutionizing the field. By the end of this journey, you'll understand the strategic importance of Generative AI, be able to build your own generative models, and appreciate the challenges and opportunities that come with deploying these models in production environments.

The strategic importance of Generative AI cannot be overstated. As we move towards a future where AI is ubiquitous, the ability to generate high-quality content, simulate complex systems, and create new experiences will become a key differentiator for businesses, researchers, and individuals alike. However, building and deploying generative models is a complex task that requires a deep understanding of the underlying mathematics, architecture design, and performance trade-offs. In this blog post, we'll provide a comprehensive overview of the Generative AI landscape, highlighting the key concepts, technical challenges, and real-world applications that are driving innovation in this field.

## Core Concepts
At the heart of Generative AI are several key concepts that underpin the ability of these models to generate new, unseen data. These concepts include:

* **Generative Adversarial Networks (GANs)**: GANs consist of two neural networks, a generator and a discriminator, that engage in a competitive game to produce new samples that are indistinguishable from real data.
* **Variational Autoencoders (VAEs)**: VAEs are a type of generative model that learn to represent data as a probabilistic latent space, allowing for efficient sampling and generation of new data.
* **Normalizing Flows**: Normalizing flows are a class of generative models that learn to transform a simple distribution into a complex one, using a series of invertible transformations.

These concepts are not mutually exclusive, and many modern generative models combine elements of GANs, VAEs, and normalizing flows to achieve state-of-the-art results. However, when misunderstood or misapplied, these concepts can lead to suboptimal performance, mode collapse, or unstable training.

To illustrate the differences between these approaches, consider the following table:

| Model | Strengths | Weaknesses |
| --- | --- | --- |
| GANs | High-quality samples, flexible architecture | Unstable training, mode collapse |
| VAEs | Efficient sampling, interpretable latent space | Limited expressiveness, posterior collapse |
| Normalizing Flows | Invertible transformations, flexible architecture | Computationally expensive, difficult to train |

## Technical Walkthrough
To demonstrate the power of Generative AI, let's build a simple generative model using PyTorch. We'll use a VAE to generate new images of handwritten digits, using the MNIST dataset as our training data.
```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader
import torchvision
import torchvision.transforms as transforms

# Define the VAE architecture
class VAE(nn.Module):
    def __init__(self, input_dim, hidden_dim, latent_dim):
        super(VAE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, latent_dim * 2)
        )
        self.decoder = nn.Sequential(
            nn.Linear(latent_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, input_dim)
        )

    def encode(self, x):
        z_mean, z_log_var = self.encoder(x).chunk(2, dim=1)
        return z_mean, z_log_var

    def reparameterize(self, z_mean, z_log_var):
        std = torch.exp(0.5 * z_log_var)
        eps = torch.randn_like(std)
        z = z_mean + eps * std
        return z

    def decode(self, z):
        return self.decoder(z)

# Initialize the VAE and optimizer
vae = VAE(input_dim=784, hidden_dim=256, latent_dim=10)
optimizer = optim.Adam(vae.parameters(), lr=0.001)

# Train the VAE
for epoch in range(10):
    for x, _ in train_loader:
        x = x.view(-1, 784)
        z_mean, z_log_var = vae.encode(x)
        z = vae.reparameterize(z_mean, z_log_var)
        x_recon = vae.decode(z)
        loss = ((x - x_recon) ** 2).sum(dim=1).mean() + 0.5 * torch.sum(1 + z_log_var - z_mean ** 2 - torch.exp(z_log_var))
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
```
This code defines a simple VAE architecture, trains it on the MNIST dataset, and uses the learned latent space to generate new images of handwritten digits.

## Real-World Applications
Generative AI has numerous real-world applications, including:

* **Image and video generation**: Generative models can be used to generate realistic images and videos, with applications in advertising, entertainment, and education.
* **Text-to-speech synthesis**: Generative models can be used to synthesize natural-sounding speech, with applications in virtual assistants, audiobooks, and language translation.
* **Data augmentation**: Generative models can be used to augment existing datasets, increasing the diversity and size of the training data and improving the performance of downstream models.

To illustrate the potential of Generative AI, consider the following deployment scenarios:

* **Virtual try-on**: A fashion retailer uses a generative model to generate realistic images of clothing items on different models, allowing customers to virtually try on clothes and reducing the need for physical prototypes.
* **Personalized advertising**: A company uses a generative model to generate personalized ads, tailored to individual customers' preferences and interests, increasing the effectiveness of advertising campaigns.
* **Medical imaging**: A hospital uses a generative model to generate synthetic medical images, allowing for more efficient training of medical imaging models and improving the accuracy of disease diagnosis.

## Production Considerations
When deploying generative models in production environments, several considerations come into play, including:

* **Bottlenecks**: Generative models can be computationally expensive, requiring significant resources to train and deploy.
* **Edge cases**: Generative models can be sensitive to edge cases, such as outliers or unusual input data, which can affect their performance and stability.
* **Failure modes**: Generative models can fail in different ways, such as mode collapse or unstable training, which can have significant consequences in production environments.

To address these considerations, several optimization strategies can be employed, including:

* **Model pruning**: Removing redundant or unnecessary weights and connections to reduce the computational complexity of the model.
* **Knowledge distillation**: Transferring knowledge from a larger, pre-trained model to a smaller, more efficient model.
* **Ensemble methods**: Combining multiple models to improve their overall performance and robustness.

## Conclusion
In conclusion, Generative AI is a rapidly evolving field that holds tremendous promise for revolutionizing the way we approach creativity, innovation, and problem-solving. By understanding the core concepts, technical challenges, and real-world applications of generative models, we can unlock new opportunities for growth, innovation, and progress. As we continue to push the boundaries of what is possible with Generative AI, we must also address the production considerations, bottlenecks, and edge cases that can affect their performance and stability. By doing so, we can ensure that generative models are deployed safely, efficiently, and effectively, and that their benefits are realized in a wide range of industries and applications.
```

## File: `frontend/blogs/genai/generative-ai-models.md`
```markdown
## Introduction
Hello and welcome to the world of generative AI models, where the ability to create realistic synthetic data has become a game-changer in various industries. As we continue to push the boundaries of what is possible with artificial intelligence, one of the major deployment bottlenecks we've encountered is the limited capacity of traditional generative models to capture complex distributions. This limitation is particularly significant in applications where data is scarce or difficult to obtain, such as in medical imaging or natural language processing. In this blog post, we will delve into the world of probabilistic generative modeling, exploring what was broken in previous approaches, why it mattered, and why this topic is strategically important right now. By the end of this article, you will have a deep understanding of the core concepts underlying probabilistic generative models and be able to build your own models using Python.

The traditional approach to generative modeling relied heavily on deterministic methods, which often failed to capture the underlying complexities of real-world data. This limitation led to the development of probabilistic generative models, which have revolutionized the field of artificial intelligence. Probabilistic generative models are strategically important right now because they have the potential to transform industries such as healthcare, finance, and entertainment. For instance, in healthcare, probabilistic generative models can be used to generate synthetic medical images, which can be used to train models for disease diagnosis. In finance, these models can be used to generate synthetic financial data, which can be used to train models for risk analysis.

## Core Concepts
At the heart of probabilistic generative modeling lies the concept of probability distributions. A probability distribution is a mathematical function that describes the probability of a random variable taking on a particular value. In the context of generative modeling, probability distributions are used to model the underlying structure of the data. The key idea is to learn a probabilistic model that can generate new data samples that are similar to the training data.

One of the most popular probabilistic generative models is the Variational Autoencoder (VAE). The VAE consists of an encoder network that maps the input data to a latent space, and a decoder network that maps the latent space back to the input data. The VAE is trained using a combination of the reconstruction loss and the KL divergence term, which regularizes the latent space to follow a Gaussian distribution.

| Model | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| VAE | Variational Autoencoder | Easy to implement, fast training time | Limited capacity to model complex distributions |
| GAN | Generative Adversarial Network | Can model complex distributions, high-quality samples | Difficult to train, prone to mode collapse |
| Normalizing Flow | Normalizing flow-based generative model | Can model complex distributions, invertible | Computationally expensive, difficult to train |

## Technical Walkthrough
In this section, we will provide a technical walkthrough of how to implement a VAE in Python using the PyTorch library. We will use a synthetic dataset consisting of 2D points sampled from a Gaussian distribution.
```python
import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define the encoder network
class Encoder(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(Encoder, self).__init__()
        self.fc1 = nn.Linear(input_dim, 128)
        self.fc2 = nn.Linear(128, latent_dim)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x

# Define the decoder network
class Decoder(nn.Module):
    def __init__(self, latent_dim, input_dim):
        super(Decoder, self).__init__()
        self.fc1 = nn.Linear(latent_dim, 128)
        self.fc2 = nn.Linear(128, input_dim)

    def forward(self, z):
        z = torch.relu(self.fc1(z))
        z = self.fc2(z)
        return z

# Define the VAE model
class VAE(nn.Module):
    def __init__(self, input_dim, latent_dim):
        super(VAE, self).__init__()
        self.encoder = Encoder(input_dim, latent_dim)
        self.decoder = Decoder(latent_dim, input_dim)

    def forward(self, x):
        z = self.encoder(x)
        x_recon = self.decoder(z)
        return x_recon

# Train the VAE model
vae = VAE(input_dim=2, latent_dim=2)
optimizer = optim.Adam(vae.parameters(), lr=0.001)
for epoch in range(100):
    optimizer.zero_grad()
    x = torch.randn(100, 2)
    x_recon = vae(x)
    loss = ((x - x_recon) ** 2).sum()
    loss.backward()
    optimizer.step()
    print(f'Epoch {epoch+1}, Loss: {loss.item()}')
```
In this example, we define an encoder network that maps the input data to a latent space, and a decoder network that maps the latent space back to the input data. We train the VAE model using a combination of the reconstruction loss and the KL divergence term.

## Real-World Applications
Probabilistic generative models have numerous real-world applications. Here are a few examples:

* **Medical Imaging**: Probabilistic generative models can be used to generate synthetic medical images, which can be used to train models for disease diagnosis.
* **Natural Language Processing**: Probabilistic generative models can be used to generate synthetic text data, which can be used to train models for language translation and text summarization.
* **Finance**: Probabilistic generative models can be used to generate synthetic financial data, which can be used to train models for risk analysis and portfolio optimization.

## Production Considerations
When deploying probabilistic generative models in production, there are several considerations to keep in mind. Here are a few:

* **Bottlenecks**: One of the major bottlenecks in deploying probabilistic generative models is the computational cost of training and inference. To mitigate this, we can use distributed computing frameworks such as TensorFlow or PyTorch.
* **Edge Cases**: Probabilistic generative models can be prone to edge cases such as mode collapse, where the model generates limited variations of the same output. To mitigate this, we can use techniques such as batch normalization and dropout.
* **Failure Modes**: Probabilistic generative models can fail in several ways, including mode collapse, overfitting, and underfitting. To mitigate this, we can use techniques such as early stopping, regularization, and data augmentation.

## Conclusion
In conclusion, probabilistic generative models are a powerful tool for generating synthetic data that can be used to train models for a variety of applications. By understanding the core concepts underlying these models, we can build our own models using Python and deploy them in production. However, there are several considerations to keep in mind when deploying these models, including bottlenecks, edge cases, and failure modes. As the field of artificial intelligence continues to evolve, we can expect to see more innovative applications of probabilistic generative models in the future.
```

## File: `frontend/blogs/ml/articles.json`
```json
[
  {
    "id": "blogs/ml/regression-ml.md",
    "category": "ml",
    "title": "Regression ML",
    "description": "Learn supervised regression models for predictions. Master regression analysis",
    "date": "2026-03-30",
    "tags": [
      "machine-learning",
      "regression-analysis",
      "supervised-learning",
      "predictive-models",
      "data-science"
    ],
    "readTime": "5 min",
    "file": "blogs/ml/regression-ml.md"
  },
  {
    "id": "blogs/ml/supervised-ml-classification.md",
    "category": "ml",
    "title": "Supervised ML Classification",
    "description": "Learn supervised machine learning classification techniques for accurate predictions",
    "date": "2026-03-23",
    "tags": [
      "machine-learning",
      "supervised-learning",
      "classification-algorithms",
      "predictive-modeling",
      "deep-learning"
    ],
    "readTime": "6 min",
    "file": "blogs/ml/supervised-ml-classification.md"
  },
  {
    "id": "blogs/ml/machine-learning-life-cycle.md",
    "category": "ml",
    "title": "Machine Learning Life Cycle",
    "description": "Learn machine learning project workflow and best practices to improve model efficiency",
    "date": "2026-03-16",
    "tags": [
      "machine-learning",
      "deep-learning",
      "natural-language-processing",
      "model-deployment",
      "data-science"
    ],
    "readTime": "7 min",
    "file": "blogs/ml/machine-learning-life-cycle.md"
  },
  {
    "id": "blogs/ml/machine-learning-challenges.md",
    "category": "ml",
    "title": "Machine Learning Challenges",
    "description": "Discover key machine learning challenges and overcome them",
    "date": "2026-03-09",
    "tags": [
      "machine-learning",
      "deep-learning",
      "ai-models",
      "data-science",
      "ml-engineering"
    ],
    "readTime": "7 min",
    "file": "blogs/ml/machine-learning-challenges.md"
  },
  {
    "id": "blogs/ml/machine-learning-explained.md",
    "category": "ml",
    "title": "Machine Learning Explained",
    "description": "Discover the basics of machine learning and its applications, learn how to get started",
    "date": "2026-03-02",
    "tags": [
      "machine-learning",
      "artificial-intelligence",
      "deep-learning",
      "natural-language-processing",
      "data-science"
    ],
    "readTime": "6 min",
    "file": "blogs/ml/machine-learning-explained.md"
  }
]
```

## File: `frontend/blogs/ml/machine-learning-challenges.md`
```markdown
## Introduction
Hello, fellow machine learning engineers and technical decision-makers. Have you ever found yourself stuck in the deployment pipeline, watching your carefully crafted model fail to generalize to real-world data? Or perhaps you've struggled to scale your model to meet the demands of a growing user base. These challenges are all too familiar in the world of machine learning, where the journey from prototype to production is often fraught with obstacles. In this blog post, we'll delve into the main challenges of machine learning, exploring the key pitfalls that can derail even the most promising projects. By the end of this article, you'll have a deeper understanding of the common challenges that arise in machine learning and be equipped with practical strategies for overcoming them.

The traditional approach to machine learning has often focused on developing models that perform well on curated datasets, only to find that they fail to generalize to the complexities of real-world data. This limitation has significant implications, as it can lead to models that are brittle, biased, or simply ineffective in practice. To address these challenges, we need to rethink our approach to machine learning, prioritizing flexibility, scalability, and transparency. In this article, we'll explore the core concepts that underlie these challenges, providing a technical walkthrough of how to implement more robust and scalable machine learning systems.

## Core Concepts
At the heart of machine learning are a set of core concepts that, when misunderstood, can lead to a range of problems. One of the most significant challenges is the issue of **overfitting**, where a model becomes too closely fit to the training data, failing to generalize to new, unseen data. This can occur when a model is too complex, or when the training data is too limited. To mitigate this risk, we can use techniques such as **regularization**, which adds a penalty term to the loss function to discourage large weights, or **early stopping**, which stops training when the model's performance on the validation set begins to degrade.

Another key concept is **bias-variance tradeoff**, which refers to the balance between a model's ability to fit the training data (bias) and its ability to generalize to new data (variance). A model with high bias will fail to capture the underlying patterns in the data, while a model with high variance will be overly sensitive to noise in the training data. To navigate this tradeoff, we can use techniques such as **cross-validation**, which evaluates a model's performance on multiple folds of the data, or **ensemble methods**, which combine the predictions of multiple models to reduce variance.

The following table provides a comparison of different approaches to addressing overfitting and bias-variance tradeoff:

| Approach | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Regularization | Adds a penalty term to the loss function | Reduces overfitting, improves generalization | Can be sensitive to hyperparameters |
| Early Stopping | Stops training when performance on validation set degrades | Prevents overfitting, reduces training time | Can be sensitive to validation set size |
| Cross-Validation | Evaluates model performance on multiple folds of data | Provides a more accurate estimate of model performance | Can be computationally expensive |
| Ensemble Methods | Combines predictions of multiple models | Reduces variance, improves robustness | Can be computationally expensive, requires careful hyperparameter tuning |

## Technical Walkthrough
To illustrate these concepts in practice, let's consider a simple example using Python and the scikit-learn library. Suppose we want to train a logistic regression model on a synthetic dataset to predict a binary outcome. We can use the following code to generate the data and train the model:
```python
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Generate synthetic data
np.random.seed(0)
X = np.random.rand(100, 10)
y = np.random.randint(0, 2, 100)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Train logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate model performance on validation set
accuracy = model.score(X_val, y_val)
print(f"Validation accuracy: {accuracy:.3f}")
```
In this example, we generate a synthetic dataset with 100 samples and 10 features, and split it into training and validation sets using the `train_test_split` function. We then train a logistic regression model on the training data using the `LogisticRegression` class, and evaluate its performance on the validation set using the `score` method.

## Real-World Applications
Machine learning has a wide range of applications in industry and academia, from image classification and natural language processing to recommender systems and predictive maintenance. Here are three substantial deployment scenarios:

1. **Image Classification**: A company that specializes in medical imaging wants to develop a system that can automatically classify images of tumors as benign or malignant. They collect a large dataset of images, each labeled with the correct classification, and train a convolutional neural network (CNN) to predict the classification.
2. **Recommender Systems**: An e-commerce company wants to develop a personalized recommender system that suggests products to customers based on their browsing and purchase history. They collect a large dataset of customer interactions, each labeled with the product ID and a rating, and train a collaborative filtering model to predict the rating.
3. **Predictive Maintenance**: A manufacturing company wants to develop a system that can predict when equipment is likely to fail, allowing them to schedule maintenance and reduce downtime. They collect a large dataset of sensor readings from the equipment, each labeled with the time to failure, and train a random forest model to predict the time to failure.

## Production Considerations
When deploying machine learning models in production, there are several bottlenecks, edge cases, and failure modes to consider. One of the most significant challenges is **concept drift**, where the underlying distribution of the data changes over time, causing the model's performance to degrade. To address this challenge, we can use techniques such as **online learning**, which updates the model in real-time as new data arrives, or **transfer learning**, which adapts a pre-trained model to the new distribution.

Another significant challenge is **model interpretability**, where the model's predictions are difficult to understand or interpret. To address this challenge, we can use techniques such as **feature importance**, which assigns a score to each feature based on its contribution to the prediction, or **partial dependence plots**, which visualize the relationship between the feature and the prediction.

The following code snippet illustrates how to use the `shap` library to compute feature importance for a logistic regression model:
```python
import shap

# Compute feature importance using SHAP
explainer = shap.Explainer(model)
shap_values = explainer(X_val)

# Plot feature importance
shap.plots.beeswarm(shap_values)
```
In this example, we use the `shap` library to compute the feature importance for a logistic regression model, and plot the results using the `beeswarm` plot.

## Conclusion
In conclusion, machine learning is a complex and challenging field, where the journey from prototype to production is often fraught with obstacles. By understanding the core concepts that underlie these challenges, we can develop more robust and scalable machine learning systems that can generalize to real-world data. Whether you're working on image classification, recommender systems, or predictive maintenance, the principles outlined in this article can help you navigate the challenges of machine learning and develop models that are accurate, reliable, and transparent. As the field of machine learning continues to evolve, we can expect to see new challenges and opportunities emerge, and by staying at the forefront of these developments, we can unlock the full potential of machine learning to drive innovation and growth.
```

## File: `frontend/blogs/ml/machine-learning-explained.md`
```markdown
## Introduction
Hello, fellow engineers and technical decision-makers. As we continue to push the boundaries of artificial intelligence, one of the most significant bottlenecks we face is the deployment and scaling of machine learning models. In the past, traditional rule-based systems were limited in their ability to handle complex, dynamic data, leading to a shift towards more adaptive and intelligent solutions. However, as machine learning (ML) has become increasingly prevalent, we've come to realize that its potential is hindered by our understanding of its fundamental principles and applications. In this article, we'll delve into the world of machine learning, exploring what it is, why it's essential, and how it's used in various industries. By the end of this journey, you'll have a deeper understanding of ML systems, their types, and how to apply them to real-world problems.

The importance of machine learning cannot be overstated. As we generate more data, the need for intelligent systems that can learn from this data and make informed decisions has become crucial. Machine learning has the potential to revolutionize industries such as healthcare, finance, and transportation, making it a strategically important topic for any organization looking to stay ahead of the curve. In this article, we'll explore the core concepts of machine learning, its applications, and the considerations that come with deploying ML systems in production.

## What is Machine Learning
Machine learning is a subset of artificial intelligence that involves training algorithms to learn from data and make predictions or decisions without being explicitly programmed. This is achieved through various techniques, including supervised, unsupervised, and reinforcement learning. At its core, machine learning is about enabling computers to automatically improve their performance on a task, based on experience or data.

To illustrate this concept, let's consider a simple example. Suppose we want to build a system that can classify images of dogs and cats. We can train a machine learning model using a dataset of labeled images, where each image is associated with a label (dog or cat). The model can then learn to recognize patterns in the data and make predictions on new, unseen images.

### Types of Machine Learning
There are several types of machine learning, each with its strengths and weaknesses. The following table summarizes the main types of ML:

| Type | Description | Example |
| --- | --- | --- |
| Supervised Learning | The model is trained on labeled data to make predictions. | Image classification |
| Unsupervised Learning | The model is trained on unlabeled data to discover patterns. | Clustering, dimensionality reduction |
| Reinforcement Learning | The model learns through trial and error by interacting with an environment. | Game playing, robotics |

## Example Applications
Machine learning has a wide range of applications across various industries. Some examples include:

* **Image classification**: Google Photos uses machine learning to classify and organize images.
* **Natural Language Processing (NLP)**: Virtual assistants like Siri and Alexa use NLP to understand and respond to voice commands.
* **Recommendation systems**: Netflix uses machine learning to recommend movies and TV shows based on user preferences.

These applications demonstrate the potential of machine learning to transform industries and improve our daily lives. However, as we deploy ML systems in production, we need to consider the technical and engineering challenges that come with it.

## Intro to ML Systems
An ML system consists of several components, including data ingestion, processing, modeling, and deployment. The following architecture diagram illustrates a typical ML system:
```markdown
+---------------+
|  Data Ingestion  |
+---------------+
       |
       |
       v
+---------------+
|  Data Processing  |
+---------------+
       |
       |
       v
+---------------+
|  Modeling        |
+---------------+
       |
       |
       v
+---------------+
|  Deployment      |
+---------------+
```
In this example, we can see that the ML system consists of four main components:

1. **Data Ingestion**: This involves collecting and processing data from various sources.
2. **Data Processing**: This involves cleaning, transforming, and preparing the data for modeling.
3. **Modeling**: This involves training and evaluating machine learning models using the prepared data.
4. **Deployment**: This involves deploying the trained model in a production environment.

## Technical Walkthrough
Let's consider a simple example of building a machine learning model using Python and the scikit-learn library. Suppose we want to build a model that can predict house prices based on features like the number of bedrooms and square footage.
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the data
data = pd.read_csv('house_prices.csv')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('price', axis=1), data['price'], test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the testing set
y_pred = model.predict(X_test)

# Evaluate the model using mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse:.2f}')
```
In this example, we can see how to load the data, split it into training and testing sets, train a linear regression model, make predictions, and evaluate the model using mean squared error.

## Real-World Applications
Machine learning has numerous real-world applications across various industries. Some examples include:

* **Healthcare**: Machine learning can be used to predict patient outcomes, diagnose diseases, and develop personalized treatment plans.
* **Finance**: Machine learning can be used to predict stock prices, detect fraudulent transactions, and optimize investment portfolios.
* **Transportation**: Machine learning can be used to predict traffic patterns, optimize routes, and develop autonomous vehicles.

These applications demonstrate the potential of machine learning to transform industries and improve our daily lives. However, as we deploy ML systems in production, we need to consider the technical and engineering challenges that come with it.

## Production Considerations
When deploying ML systems in production, we need to consider several factors, including:

* **Scalability**: The ability of the system to handle large volumes of data and traffic.
* **Reliability**: The ability of the system to maintain its performance and accuracy over time.
* **Security**: The ability of the system to protect sensitive data and prevent unauthorized access.

To address these concerns, we can use various techniques, such as:

* **Cloud computing**: Using cloud services like AWS or Google Cloud to scale our infrastructure and reduce costs.
* **Containerization**: Using containers like Docker to package and deploy our ML models.
* **Monitoring and evaluation**: Using tools like Prometheus and Grafana to monitor our system's performance and evaluate its accuracy.

## Conclusion
In conclusion, machine learning is a powerful technology that has the potential to transform industries and improve our daily lives. By understanding the core concepts of machine learning, its applications, and the considerations that come with deploying ML systems in production, we can unlock its full potential and build more intelligent and adaptive systems. As we continue to push the boundaries of artificial intelligence, it's essential to stay up-to-date with the latest developments and advancements in the field. By doing so, we can build more robust, scalable, and reliable ML systems that can drive business value and improve our lives.
```

## File: `frontend/blogs/ml/machine-learning-life-cycle.md`
```markdown
## Introduction
Hello and welcome to this comprehensive guide on the life cycle of machine learning projects. As machine learning continues to transform industries and revolutionize the way we approach complex problems, the need for a structured approach to ML project development has never been more pressing. In recent years, we've seen a significant surge in ML adoption, but many projects still struggle to make it past the proof-of-concept stage. One major bottleneck is the lack of a clear understanding of the ML life cycle, leading to projects that are poorly planned, inefficiently executed, and ultimately, fail to deliver on their promises. 

In this blog post, we'll delve into the key stages of the ML life cycle, exploring what breaks in previous approaches and why it matters. We'll discuss the strategic importance of understanding the ML life cycle and what readers can expect to take away from this guide. By the end of this post, you'll have a deep understanding of the ML life cycle, including how to plan, execute, and deploy ML projects effectively. You'll be able to build and deploy ML models that drive real business value, and you'll understand the importance of continuous monitoring and evaluation in ensuring the long-term success of your ML projects.

The ML life cycle is a complex process that involves several stages, from data preparation and model training to deployment and maintenance. Each stage presents its own unique challenges and opportunities, and understanding how to navigate these stages is critical to the success of any ML project. In the following sections, we'll explore the core concepts of the ML life cycle, including data preparation, model training, and deployment. We'll also discuss the technical considerations involved in each stage and provide a detailed walkthrough of a real-world example.

## Core Concepts
At its core, the ML life cycle is a process that involves several key stages: data preparation, model training, model evaluation, deployment, and maintenance. Each stage is critical to the success of the project, and understanding how to navigate these stages is essential. 

### Data Preparation
Data preparation is the first stage of the ML life cycle, and it involves collecting, cleaning, and preprocessing the data that will be used to train the model. This stage is critical because the quality of the data has a direct impact on the performance of the model. High-quality data that is relevant, accurate, and complete is essential for training a model that generalizes well to new, unseen data.

### Model Training
Model training is the stage where the model is trained on the prepared data. This stage involves selecting the appropriate algorithm, configuring the hyperparameters, and training the model. The goal of this stage is to develop a model that accurately predicts the target variable and generalizes well to new data.

### Model Evaluation
Model evaluation is the stage where the performance of the model is evaluated on a holdout dataset. This stage involves calculating metrics such as accuracy, precision, recall, and F1 score to determine how well the model is performing. The goal of this stage is to identify any issues with the model and make adjustments as needed.

### Deployment
Deployment is the stage where the model is deployed to a production environment. This stage involves integrating the model with other systems, configuring the infrastructure, and monitoring the performance of the model. The goal of this stage is to ensure that the model is delivering the expected business value and making adjustments as needed.

## Technical Walkthrough
To illustrate the concepts discussed above, let's consider a real-world example. Suppose we're building a model to predict customer churn for a telecom company. The dataset consists of customer demographic information, call records, and billing data. 

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('customer_data.csv')

# Preprocess the data
df = pd.get_dummies(df, columns=['gender', 'plan'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('churn', axis=1), df['churn'], test_size=0.2, random_state=42)

# Train a random forest classifier
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
print('Accuracy:', model.score(X_test, y_test))
```

In this example, we first load the dataset and preprocess it by converting categorical variables into dummy variables. We then split the data into training and testing sets and train a random forest classifier on the training set. Finally, we evaluate the model on the test set and calculate the accuracy.

## Real-World Applications
The ML life cycle has numerous real-world applications across various industries. Here are a few examples:

* **Predictive Maintenance**: A manufacturing company can use the ML life cycle to develop a model that predicts equipment failures, reducing downtime and increasing overall efficiency.
* **Customer Segmentation**: A retail company can use the ML life cycle to develop a model that segments customers based on their buying behavior, allowing for more targeted marketing campaigns.
* **Fraud Detection**: A financial institution can use the ML life cycle to develop a model that detects fraudulent transactions, reducing losses and improving customer trust.

| Industry | Application | Model Type |
| --- | --- | --- |
| Manufacturing | Predictive Maintenance | Regression |
| Retail | Customer Segmentation | Clustering |
| Finance | Fraud Detection | Classification |

## Production Considerations
When deploying ML models to production, there are several considerations to keep in mind. 

### Bottlenecks
One common bottleneck is the lack of sufficient computational resources, which can lead to slow model inference times and reduced overall performance. 

### Edge Cases
Another consideration is edge cases, which are scenarios that are not well-represented in the training data. 

### Failure Modes
ML models can also fail in various ways, such as overfitting or underfitting, which can lead to poor performance on new, unseen data.

### Monitoring and Evaluation
To address these considerations, it's essential to monitor the performance of the model in production and evaluate its performance on a regular basis. This can involve tracking metrics such as accuracy, precision, and recall, as well as monitoring the model's computational resources and adjusting as needed.

## Conclusion
In conclusion, the ML life cycle is a critical process that involves several key stages, from data preparation and model training to deployment and maintenance. Understanding how to navigate these stages is essential for developing ML models that drive real business value. By following the principles outlined in this guide, ML practitioners can develop models that are accurate, efficient, and scalable, and that deliver significant business value. As the field of ML continues to evolve, it's essential to stay up-to-date with the latest developments and best practices, and to continually evaluate and improve the ML life cycle to ensure optimal performance and results. 

The future of ML is exciting and rapidly evolving, with new technologies and techniques emerging all the time. As we move forward, it's essential to prioritize transparency, explainability, and accountability in ML systems, and to ensure that these systems are fair, reliable, and secure. By doing so, we can unlock the full potential of ML and create a brighter, more sustainable future for all. 

Here is a summary of key takeaways from this post:

* The ML life cycle involves several key stages, including data preparation, model training, model evaluation, deployment, and maintenance.
* Understanding how to navigate these stages is essential for developing ML models that drive real business value.
* The ML life cycle has numerous real-world applications across various industries, including predictive maintenance, customer segmentation, and fraud detection.
* When deploying ML models to production, it's essential to consider bottlenecks, edge cases, failure modes, and monitoring and evaluation.
* The future of ML is exciting and rapidly evolving, with new technologies and techniques emerging all the time.
```

## File: `frontend/blogs/ml/regression-ml.md`
```markdown
## Introduction
Hello and welcome to this technical deep dive on Regression ML, a crucial aspect of supervised machine learning. In recent years, the rapid growth of data-driven applications has led to a significant increase in the deployment of regression models in production environments. However, many of these deployments are hindered by scaling issues, model limitations, and industry shifts towards more complex data types. Previously, many approaches focused solely on mean squared error (MSE) or mean absolute error (MAE) as the primary metrics for evaluation, which often led to models that were not robust to outliers or non-normal distributions. The strategic importance of regression ML lies in its ability to predict continuous outcomes, which is critical in various industries such as finance, healthcare, and energy. By the end of this article, readers will understand the core concepts of regression ML, be able to implement a regression model using Python, and appreciate the real-world applications and production considerations of these models.

## Core Concepts
At its core, regression ML involves training a model to predict a continuous output variable based on one or more input features. The key idea is to learn a mapping between the input space and the output space, such that the predicted output is as close as possible to the actual output. This is typically achieved through the minimization of a loss function, such as MSE or MAE. However, when misunderstood, regression models can suffer from issues such as overfitting, underfitting, or sensitivity to outliers. For instance, a model that is overly complex may fit the training data perfectly but fail to generalize to new, unseen data. On the other hand, a model that is too simple may not capture the underlying patterns in the data. The following table compares some common regression algorithms:

| Algorithm | Description | Strengths | Weaknesses |
| --- | --- | --- | --- |
| Linear Regression | Linear mapping between inputs and output | Simple, interpretable | Sensitive to outliers, assumes linearity |
| Ridge Regression | Linear regression with L2 regularization | Reduces overfitting, improves generalization | Can be computationally expensive |
| Lasso Regression | Linear regression with L1 regularization | Selects relevant features, reduces overfitting | Can be sensitive to hyperparameters |
| Decision Tree Regression | Tree-based model for regression | Handles non-linear relationships, easy to interpret | Can be prone to overfitting, sensitive to hyperparameters |

## Technical Walkthrough
To illustrate the implementation of a regression model, let's consider a synthetic dataset of housing prices, where we want to predict the price of a house based on its features such as number of bedrooms, square footage, and location. We'll use Python and the scikit-learn library to train a ridge regression model on this data.
```python
import numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split

# Generate synthetic data
np.random.seed(0)
X = np.random.rand(100, 3)  # 100 samples, 3 features
y = 3 * X[:, 0] + 2 * X[:, 1] + np.random.randn(100)  # linear relationship with noise

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a ridge regression model
ridge_model = Ridge(alpha=0.1)
ridge_model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = ridge_model.predict(X_test)
print("Mean Squared Error:", np.mean((y_test - y_pred) ** 2))
```
In this example, we first generate synthetic data with a linear relationship between the features and the target variable. We then split the data into training and testing sets and train a ridge regression model on the training data. Finally, we evaluate the model on the test set and print the mean squared error.

## Real-World Applications
Regression ML has numerous real-world applications across various industries. Here are three substantial deployment scenarios:

1. **Predicting Energy Consumption**: A utility company wants to predict the energy consumption of its customers based on historical data and weather forecasts. The company can use a regression model to predict the energy consumption and adjust its supply accordingly.
2. **Stock Price Prediction**: A financial institution wants to predict the stock prices of a particular company based on historical data and market trends. The institution can use a regression model to predict the stock prices and make informed investment decisions.
3. **Medical Diagnosis**: A hospital wants to predict the likelihood of a patient having a particular disease based on their medical history and test results. The hospital can use a regression model to predict the likelihood of the disease and provide personalized treatment recommendations.

## Production Considerations
When deploying regression models in production, there are several bottlenecks, edge cases, and failure modes to consider. For instance, the model may be sensitive to outliers or missing values in the data, which can affect its performance. Additionally, the model may drift over time due to changes in the underlying data distribution, which can require periodic retraining. To address these issues, it's essential to monitor the model's performance, evaluate its drift, and optimize its hyperparameters regularly. Some optimization strategies include:

* **Regularization techniques**: such as L1 and L2 regularization to reduce overfitting
* **Early stopping**: to prevent overfitting during training
* **Ensemble methods**: to combine the predictions of multiple models and improve overall performance

## Conclusion
In conclusion, regression ML is a powerful tool for predicting continuous outcomes in various industries. By understanding the core concepts of regression ML, implementing a regression model using Python, and appreciating the real-world applications and production considerations, practitioners can build robust and scalable regression models that drive business value. As the field of machine learning continues to evolve, we can expect to see more advanced regression techniques, such as deep learning-based models, that can handle complex data types and relationships. However, the fundamental principles of regression ML will remain the same, and it's essential for practitioners to stay up-to-date with the latest developments and best practices in the field.
```

## File: `frontend/blogs/ml/supervised-ml-classification.md`
```markdown
## Introduction
Hello and welcome to the world of Supervised Machine Learning Classification. As ML engineers and AI developers, we've all been there - stuck in the trenches of deployment bottlenecks, scaling issues, and model limitations. One of the most significant challenges we face is the inability of traditional classification models to generalize well to new, unseen data. This is where Supervised ML Classification comes in - a strategically important topic that has the potential to revolutionize the way we approach machine learning. In this blog post, we'll delve into the core concepts of Supervised ML Classification, explore its technical walkthrough, and discuss real-world applications and production considerations. By the end of this post, you'll have a deep understanding of how to build and deploy scalable classification models that can tackle even the most complex problems.

The traditional approach to classification has been to use a one-size-fits-all model, which often results in suboptimal performance. This is because different datasets have different characteristics, and a single model may not be able to capture these nuances. Furthermore, the rise of big data has led to an explosion in the amount of data available, making it increasingly difficult to train and deploy models that can handle such large volumes. This is where Supervised ML Classification comes in - by providing a framework for building models that can learn from labeled data and generalize well to new, unseen data.

## Core Concepts
At its core, Supervised ML Classification is about training models on labeled data to predict the class or label of new, unseen data. The key idea is to use a loss function that measures the difference between the predicted label and the true label, and to optimize this loss function using an optimization algorithm. The choice of loss function and optimization algorithm is critical, as it can significantly impact the performance of the model.

One of the most popular loss functions used in classification is the cross-entropy loss function, which measures the difference between the predicted probabilities and the true label. The cross-entropy loss function is defined as:

`L(y, y_pred) = -sum(y * log(y_pred))`

where `y` is the true label and `y_pred` is the predicted probability.

The optimization algorithm used to optimize the loss function is also critical. Some popular optimization algorithms include stochastic gradient descent (SGD), Adam, and RMSProp. Each of these algorithms has its own strengths and weaknesses, and the choice of algorithm will depend on the specific problem and dataset.

| Loss Function | Optimization Algorithm | Description |
| --- | --- | --- |
| Cross-Entropy | SGD | Measures the difference between predicted probabilities and true label, optimized using stochastic gradient descent |
| Mean Squared Error | Adam | Measures the difference between predicted values and true values, optimized using Adam |
| Hinge Loss | RMSProp | Measures the difference between predicted margins and true margins, optimized using RMSProp |

## Technical Walkthrough
Let's take a look at a simple example of a classification model using Python and the popular scikit-learn library. In this example, we'll use the Iris dataset, which is a classic multiclass classification problem.

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the test set
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
```

In this example, we load the Iris dataset and split it into training and testing sets. We then train a logistic regression model on the training set and evaluate its performance on the test set using the accuracy score.

## Real-World Applications
Supervised ML Classification has a wide range of real-world applications, from image classification to natural language processing. Here are a few examples:

* **Image Classification**: Supervised ML Classification can be used to classify images into different categories, such as objects, scenes, or actions. For example, a self-driving car may use image classification to detect pedestrians, cars, and other obstacles.
* **Natural Language Processing**: Supervised ML Classification can be used to classify text into different categories, such as spam vs. non-spam emails, or positive vs. negative reviews.
* **Medical Diagnosis**: Supervised ML Classification can be used to classify medical images, such as X-rays or MRIs, to diagnose diseases such as cancer or diabetes.

## Production Considerations
When deploying Supervised ML Classification models in production, there are several considerations to keep in mind. One of the most significant challenges is handling concept drift, which occurs when the distribution of the data changes over time. This can cause the model to become less accurate or even fail.

To handle concept drift, it's essential to monitor the model's performance over time and retrain the model as needed. This can be done by collecting new data and retraining the model on the new data, or by using online learning algorithms that can learn from streaming data.

Another consideration is scalability. As the volume of data increases, it's essential to ensure that the model can handle the increased load. This can be done by using distributed computing frameworks, such as Apache Spark or TensorFlow, to train and deploy the model.

| Consideration | Description | Solution |
| --- | --- | --- |
| Concept Drift | Distribution of data changes over time | Monitor model performance, retrain model as needed |
| Scalability | Increased volume of data | Use distributed computing frameworks |
| Interpretability | Model is difficult to interpret | Use techniques such as feature importance or partial dependence plots |

## Conclusion
In conclusion, Supervised ML Classification is a powerful technique for building models that can learn from labeled data and generalize well to new, unseen data. By understanding the core concepts of Supervised ML Classification, including loss functions and optimization algorithms, we can build models that can tackle even the most complex problems. By using real-world examples and case studies, we can see the power of Supervised ML Classification in action. As we look to the future, it's essential to consider production considerations, such as concept drift and scalability, to ensure that our models can handle the challenges of real-world deployment. With the right techniques and tools, we can unlock the full potential of Supervised ML Classification and build models that can drive business value and improve people's lives.
```

## File: `frontend/blogs/nlp/articles.json`
```json
[
  {
    "id": "blogs/nlp/stopwords-text-cleaning.md",
    "category": "nlp",
    "title": "Stopwords Text Cleaning",
    "description": "Learn to improve text data quality by removing stopwords",
    "date": "2026-03-26",
    "tags": [
      "natural-language-processing",
      "text-preprocessing",
      "stopwords-removal",
      "text-cleaning",
      "nlp-techniques"
    ],
    "readTime": "6 min",
    "file": "blogs/nlp/stopwords-text-cleaning.md"
  },
  {
    "id": "blogs/nlp/nlp-tokenization.md",
    "category": "nlp",
    "title": "NLP Tokenization",
    "description": "Learn tokenization methods for text analysis",
    "date": "2026-03-19",
    "tags": [
      "natural-language-processing",
      "text-tokenization",
      "nlp-techniques",
      "tokenization-methods",
      "text-analysis"
    ],
    "readTime": "5 min",
    "file": "blogs/nlp/nlp-tokenization.md"
  },
  {
    "id": "blogs/nlp/nlp-text-preprocessing.md",
    "category": "nlp",
    "title": "NLP Text Preprocessing",
    "description": "Learn text preprocessing techniques to improve NLP model accuracy",
    "date": "2026-03-12",
    "tags": [
      "natural-language-processing",
      "text-preprocessing",
      "machine-learning",
      "data-cleaning",
      "nlp-techniques"
    ],
    "readTime": "5 min",
    "file": "blogs/nlp/nlp-text-preprocessing.md"
  },
  {
    "id": "blogs/nlp/nlp-basics.md",
    "category": "nlp",
    "title": "NLP Basics",
    "description": "Learn NLP fundamentals, boost language skills",
    "date": "2026-03-05",
    "tags": [
      "natural-language-processing",
      "machine-learning",
      "text-analysis",
      "speech-recognition",
      "language-modeling"
    ],
    "readTime": "6 min",
    "file": "blogs/nlp/nlp-basics.md"
  }
]
```

## File: `frontend/blogs/nlp/nlp-basics.md`
```markdown
## Introduction
Hello and welcome to the world of Natural Language Processing (NLP). As ML engineers and AI developers, we've all encountered the challenges of dealing with unstructured text data. In recent years, the demand for NLP-powered systems has skyrocketed, driven by the need for efficient and accurate text analysis, sentiment analysis, and language translation. However, traditional approaches to NLP have often been limited by their reliance on rule-based systems and shallow machine learning models. These limitations have led to deployment bottlenecks, scaling issues, and subpar performance. In this blog post, we'll delve into the basics of NLP, exploring the key concepts, technical walkthroughs, and real-world applications that are driving the field forward. By the end of this article, you'll have a deep understanding of NLP fundamentals and be equipped to build your own NLP-powered systems.

The strategic importance of NLP cannot be overstated. With the exponential growth of text data from social media, customer feedback, and online reviews, businesses are eager to tap into this wealth of information to gain insights, improve customer experience, and drive decision-making. However, the complexity and nuances of human language have made it challenging to develop accurate and efficient NLP systems. That's why it's essential to understand the underlying concepts, architectures, and techniques that power modern NLP systems.

## Core Concepts
At its core, NLP is concerned with the interaction between computers and humans in natural language. This involves a range of tasks, including text preprocessing, tokenization, named entity recognition, sentiment analysis, and machine translation. One of the key challenges in NLP is dealing with the ambiguity and uncertainty of human language. For instance, words can have multiple meanings, and context plays a crucial role in disambiguating these meanings.

To address these challenges, modern NLP systems rely on deep learning models, such as Recurrent Neural Networks (RNNs), Convolutional Neural Networks (CNNs), and Transformers. These models are capable of learning complex patterns and relationships in language data, allowing for more accurate and efficient text analysis. However, understanding how these models work under the hood is crucial for building effective NLP systems.

Here's a comparison of different NLP approaches:

| Approach | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| Rule-based | Uses hand-coded rules to analyze text | High precision, interpretable | Limited scalability, brittle |
| Machine Learning | Uses statistical models to analyze text | High accuracy, scalable | Requires large datasets, can be opaque |
| Deep Learning | Uses neural networks to analyze text | High accuracy, flexible | Requires large datasets, can be computationally expensive |

## Technical Walkthrough
Let's take a closer look at a concrete example of an NLP system using Python and the popular `transformers` library. We'll build a simple sentiment analysis model using the BERT (Bidirectional Encoder Representations from Transformers) architecture.

```python
import pandas as pd
import torch
from transformers import BertTokenizer, BertModel

# Load the dataset
df = pd.read_csv("sentiment_data.csv")

# Preprocess the text data
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")
input_ids = []
attention_masks = []
for text in df["text"]:
    inputs = tokenizer.encode_plus(
        text,
        add_special_tokens=True,
        max_length=512,
        return_attention_mask=True,
        return_tensors="pt",
    )
    input_ids.append(inputs["input_ids"])
    attention_masks.append(inputs["attention_mask"])

# Create the dataset and data loader
dataset = torch.utils.data.TensorDataset(input_ids, attention_masks, df["label"])
batch_size = 32
data_loader = torch.utils.data.DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Define the model and optimizer
model = BertModel.from_pretrained("bert-base-uncased")
optimizer = torch.optim.Adam(model.parameters(), lr=1e-5)

# Train the model
for epoch in range(5):
    model.train()
    total_loss = 0
    for batch in data_loader:
        input_ids, attention_mask, labels = batch
        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
    print(f"Epoch {epoch+1}, Loss: {total_loss / len(data_loader)}")
```

In this example, we use the `transformers` library to load the pre-trained BERT model and tokenizer. We then preprocess the text data, create a dataset and data loader, and define the model and optimizer. Finally, we train the model using the Adam optimizer and a learning rate of 1e-5.

## Real-World Applications
NLP has numerous real-world applications across various industries. Here are three substantial deployment scenarios:

1. **Sentiment Analysis for Customer Feedback**: A company like Amazon can use NLP to analyze customer reviews and feedback, allowing them to identify areas for improvement and optimize their products and services.
2. **Language Translation for Global Communication**: A company like Google can use NLP to develop language translation systems, enabling people to communicate across languages and cultures.
3. **Text Summarization for News Articles**: A company like The New York Times can use NLP to develop text summarization systems, allowing readers to quickly grasp the main points of an article.

In each of these scenarios, NLP systems are used to analyze and generate human language, enabling businesses to tap into the wealth of information contained in text data.

## Production Considerations
When deploying NLP systems in production, there are several bottlenecks, edge cases, and failure modes to consider. Here are a few:

* **Data Quality**: NLP systems are only as good as the data they're trained on. Ensuring high-quality, diverse, and representative data is crucial for accurate and reliable performance.
* **Model Drift**: NLP models can drift over time as language usage and patterns change. Regular monitoring and retraining of models is necessary to maintain performance.
* **Scalability**: NLP systems can be computationally expensive, requiring significant resources to train and deploy. Optimizing models for scalability and efficiency is crucial for large-scale deployments.

To address these challenges, it's essential to develop strategies for monitoring, evaluating, and optimizing NLP systems in production. This includes using metrics such as accuracy, F1-score, and ROUGE score to evaluate performance, as well as implementing techniques such as data augmentation, transfer learning, and knowledge distillation to improve model robustness and efficiency.

## Conclusion
In conclusion, NLP is a rapidly evolving field with numerous applications across industries. By understanding the key concepts, technical walkthroughs, and real-world applications of NLP, ML engineers and AI developers can build effective and efficient NLP systems. As the field continues to advance, we can expect to see significant improvements in areas such as language understanding, text generation, and multimodal processing. With the strategic importance of NLP only growing, it's essential to stay up-to-date with the latest developments and advancements in this exciting field.
```

## File: `frontend/blogs/nlp/nlp-text-preprocessing.md`
```markdown
## Introduction
Hello and welcome to the world of Natural Language Processing (NLP). As ML engineers and AI developers, we've all been there - stuck with a model that's not performing as expected, only to realize that the bottleneck lies in the text preprocessing stage. In my experience, I've seen many projects suffer from subpar text preprocessing, leading to poor model performance, scaling issues, and ultimately, deployment failures. The traditional approach of using simple tokenization and stemming techniques is no longer sufficient, especially when dealing with large-scale, real-world text data. In this blog post, we'll dive into the world of NLP text preprocessing, exploring the key concepts, technical walkthroughs, and real-world applications that will help you build more robust and scalable NLP systems. By the end of this post, you'll understand the importance of text preprocessing, learn how to implement effective techniques, and be able to build high-performance NLP models that can handle the complexities of real-world text data.

## Core Concepts
At the heart of NLP text preprocessing lies a deep understanding of the underlying concepts. Tokenization, the process of breaking down text into individual words or tokens, is a crucial step. However, it's not just about splitting text into words; it's about handling punctuation, special characters, and out-of-vocabulary (OOV) words. Stemming and lemmatization are also essential techniques for reducing words to their base form, but they can be lossy and may not always produce the desired results. Another critical aspect is handling stop words, which are common words like "the," "and," and "a" that don't add much value to the meaning of the text. 

| Technique | Description | Example |
| --- | --- | --- |
| Tokenization | Breaking down text into individual words or tokens | "This is an example sentence" -> ["This", "is", "an", "example", "sentence"] |
| Stemming | Reducing words to their base form using suffix removal | "running" -> "run" |
| Lemmatization | Reducing words to their base form using dictionary lookup | "running" -> "run" |
| Stop word removal | Removing common words that don't add much value to the meaning of the text | "This is an example sentence" -> ["example", "sentence"] |

## Technical Walkthrough
Let's take a look at a concrete example of how we can implement text preprocessing using Python and the popular NLTK library. We'll use a synthetic dataset of movie reviews to demonstrate the effectiveness of our approach.
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Load the dataset
reviews = ["This movie is amazing!", "I loved the movie, it's so good!", "The movie was terrible, I hated it."]

# Tokenize the text
tokenized_reviews = [word_tokenize(review) for review in reviews]

# Remove stop words
stop_words = set(stopwords.words('english'))
filtered_reviews = [[word for word in review if word not in stop_words] for review in tokenized_reviews]

# Lemmatize the words
lemmatizer = WordNetLemmatizer()
lemmatized_reviews = [[lemmatizer.lemmatize(word) for word in review] for review in filtered_reviews]

print(lemmatized_reviews)
```
In this example, we first tokenize the text using the `word_tokenize` function from NLTK. We then remove stop words using the `stopwords` corpus, and finally, we lemmatize the words using the `WordNetLemmatizer`. The resulting output is a list of lemmatized reviews that can be used as input to our NLP model.

## Real-World Applications
Text preprocessing is a critical component of many real-world NLP applications. Here are a few examples:

* **Sentiment Analysis**: In sentiment analysis, text preprocessing is used to remove noise and irrelevant information from the text, allowing the model to focus on the sentiment-bearing words. For instance, a company like Amazon can use sentiment analysis to analyze customer reviews and improve their products and services.
* **Named Entity Recognition (NER)**: In NER, text preprocessing is used to identify and extract named entities such as names, locations, and organizations. For example, a news organization like The New York Times can use NER to extract entities from news articles and provide more accurate and informative reporting.
* **Machine Translation**: In machine translation, text preprocessing is used to normalize the text and remove any inconsistencies that may affect the translation quality. For instance, a company like Google can use machine translation to translate text from one language to another, allowing users to access information from around the world.

## Production Considerations
When deploying text preprocessing in a production environment, there are several considerations to keep in mind. One of the biggest challenges is handling out-of-vocabulary (OOV) words, which can cause the model to fail or produce subpar results. Another challenge is dealing with noisy or inconsistent data, which can affect the accuracy of the model. To address these challenges, it's essential to implement robust monitoring and evaluation mechanisms, such as tracking the performance of the model over time and detecting any changes in the data distribution. Additionally, it's crucial to consider the scalability of the system, ensuring that it can handle large volumes of data and traffic.

## Conclusion
In conclusion, text preprocessing is a critical component of NLP systems, and its importance cannot be overstated. By understanding the key concepts, implementing effective techniques, and considering real-world applications and production considerations, we can build more robust and scalable NLP models that can handle the complexities of real-world text data. As we move forward in the field of NLP, it's essential to stay up-to-date with the latest research and trends, exploring new techniques and approaches that can help us improve the accuracy and efficiency of our models. With the right tools and techniques, we can unlock the full potential of NLP and build systems that can truly understand and generate human-like language.
```

## File: `frontend/blogs/nlp/nlp-tokenization.md`
```markdown
## Introduction
Hello and welcome to the world of Natural Language Processing (NLP). As ML engineers and AI developers, we've all been there - stuck with a deployment bottleneck, trying to scale our NLP models, or struggling with model limitations. One of the most critical components of NLP is tokenization, and it's an area where previous approaches have often fallen short. In the past, tokenization methods were simplistic and didn't account for the complexities of human language. This led to poor model performance, especially when dealing with out-of-vocabulary words, punctuation, and special characters. The importance of tokenization lies in its ability to convert raw text into a format that can be understood by machines. In this blog post, we'll delve into the world of tokenization methods, exploring what works, what doesn't, and how to build robust NLP systems. By the end of this article, you'll have a deep understanding of tokenization methods and be able to build your own NLP systems that can handle complex text data.

## Core Concepts
Tokenization is the process of breaking down text into individual words or tokens. It's a crucial step in NLP, as it allows us to convert raw text into a format that can be processed by machines. There are several tokenization methods, each with its strengths and weaknesses. The most common methods include:
* **Word-level tokenization**: This method involves breaking down text into individual words. It's simple and effective but can struggle with out-of-vocabulary words and punctuation.
* **Subword tokenization**: This method involves breaking down words into subwords or word pieces. It's more effective than word-level tokenization, as it can handle out-of-vocabulary words and punctuation.
* **Character-level tokenization**: This method involves breaking down text into individual characters. It's the most granular method but can be computationally expensive.

| Tokenization Method | Strengths | Weaknesses |
| --- | --- | --- |
| Word-level | Simple, effective | Struggles with out-of-vocabulary words and punctuation |
| Subword | Handles out-of-vocabulary words and punctuation | Can be computationally expensive |
| Character-level | Most granular | Computationally expensive |

When tokenization methods are misunderstood, it can lead to poor model performance. For example, using word-level tokenization on text data that contains a lot of out-of-vocabulary words can result in poor model performance. On the other hand, using subword tokenization can improve model performance but can also increase computational costs.

## Technical Walkthrough
Let's take a look at an example implementation of subword tokenization using the popular Hugging Face Transformers library. We'll use the `WordPieceTokenizer` class to tokenize a sample sentence.
```python
import torch
from transformers import WordPieceTokenizer

# Sample sentence
sentence = "This is a sample sentence."

# Create a WordPieceTokenizer instance
tokenizer = WordPieceTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the sentence
inputs = tokenizer.encode_plus(
    sentence,
    add_special_tokens=True,
    max_length=512,
    return_attention_mask=True,
    return_tensors="pt"
)

print(inputs["input_ids"])
print(inputs["attention_mask"])
```
In this example, we create a `WordPieceTokenizer` instance and use it to tokenize a sample sentence. The `encode_plus` method returns a dictionary containing the tokenized input IDs and attention mask. We can then use these tokenized inputs to train a model.

## Real-World Applications
Tokenization methods have a wide range of applications in NLP. Here are a few examples:
* **Sentiment analysis**: Tokenization is used to break down text into individual words or tokens, which can then be used to train a sentiment analysis model.
* **Language translation**: Tokenization is used to break down text into individual words or tokens, which can then be translated into another language.
* **Text summarization**: Tokenization is used to break down text into individual words or tokens, which can then be used to train a text summarization model.

In each of these applications, the choice of tokenization method can have a significant impact on model performance. For example, using subword tokenization can improve model performance on out-of-vocabulary words, but can also increase computational costs.

## Production Considerations
When deploying tokenization methods in production, there are several considerations to keep in mind. Here are a few:
* **Bottlenecks**: Tokenization can be a bottleneck in NLP pipelines, especially when dealing with large amounts of text data. To mitigate this, we can use distributed computing or parallel processing.
* **Edge cases**: Tokenization methods can struggle with edge cases, such as out-of-vocabulary words or special characters. To mitigate this, we can use techniques such as subword tokenization or character-level tokenization.
* **Failure modes**: Tokenization methods can fail in certain scenarios, such as when dealing with noisy or corrupted text data. To mitigate this, we can use techniques such as data cleaning or preprocessing.

To optimize tokenization methods in production, we can use techniques such as:
* **Caching**: Caching tokenized inputs can reduce computational costs and improve model performance.
* **Parallel processing**: Parallel processing can be used to speed up tokenization and improve model performance.
* **Distributed computing**: Distributed computing can be used to scale tokenization and improve model performance.

## Conclusion
In conclusion, tokenization methods are a critical component of NLP systems. By understanding the strengths and weaknesses of different tokenization methods, we can build robust NLP systems that can handle complex text data. The choice of tokenization method depends on the specific application and the characteristics of the text data. By considering production considerations such as bottlenecks, edge cases, and failure modes, we can deploy tokenization methods in production with confidence. As NLP continues to evolve, we can expect to see new tokenization methods emerge that can handle even more complex text data.
```

## File: `frontend/blogs/nlp/stopwords-text-cleaning.md`
```markdown
## Introduction
Hello and welcome to this technical blog post on stopwords and text cleaning. As machine learning engineers and AI developers, we've all been there - trying to deploy a natural language processing (NLP) model, only to have it fail due to poor text quality. The culprit? Often, it's the sheer amount of noise in our text data, courtesy of stopwords. These common words like "the", "and", "a", etc. may seem harmless, but they can wreak havoc on our models, causing them to overfit or underfit. In this post, we'll explore the world of stopwords and text cleaning, discussing what was broken in previous approaches, why this topic is strategically important right now, and what readers will walk away understanding or being able to build. By the end of this post, you'll be equipped to build robust text cleaning pipelines that can handle even the noisiest of text data.

The importance of text cleaning cannot be overstated. With the rise of NLP and its applications in areas like sentiment analysis, topic modeling, and text classification, the need for high-quality text data has never been more pressing. However, previous approaches to text cleaning have often been ad-hoc, relying on manual rules and heuristics to remove noise from text data. These approaches are not only time-consuming but also prone to errors, leading to suboptimal model performance. In this post, we'll delve into the world of stopwords and text cleaning, exploring the key concepts, technical walkthroughs, and real-world applications that will help you build better text cleaning pipelines.

## Core Concepts
So, what are stopwords, and why are they a problem? Stopwords are common words that do not carry much meaning in a sentence, such as articles, prepositions, and conjunctions. While they may seem harmless, stopwords can account for a significant portion of our text data, causing our models to focus on the wrong features. For example, in a sentiment analysis task, our model may end up focusing on the word "the" instead of the word "love" or "hate". To illustrate this, consider the following table, which shows the frequency of stopwords in a sample text dataset:

| Word | Frequency |
| --- | --- |
| the | 1000 |
| and | 800 |
| a | 600 |
| of | 500 |
| to | 400 |

As we can see, stopwords account for a significant portion of our text data. To combat this, we can use techniques like tokenization, stemming, and lemmatization to reduce the dimensionality of our text data. Tokenization involves breaking down text into individual words or tokens, while stemming and lemmatization involve reducing words to their base form. For example, the words "running", "runs", and "runner" can all be reduced to the base form "run".

## Technical Walkthrough
Now that we've explored the key concepts, let's walk through a technical example of how to build a text cleaning pipeline using Python. We'll use the popular NLTK library to perform tokenization, stemming, and lemmatization. First, we'll import the necessary libraries and load our text data:
```python
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Load text data
text_data = ["This is a sample sentence.", "This sentence is another example."]
```
Next, we'll perform tokenization and stemming on our text data:
```python
# Perform tokenization and stemming
tokenized_data = [word_tokenize(sentence) for sentence in text_data]
stemmed_data = [[word.lower() for word in sentence] for sentence in tokenized_data]
```
Finally, we'll perform lemmatization on our stemmed data:
```python
# Perform lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_data = [[lemmatizer.lemmatize(word) for word in sentence] for sentence in stemmed_data]
```
The resulting lemmatized data will be much cleaner and more suitable for use in our NLP models.

## Real-World Applications
So, how can we apply these techniques in real-world applications? Let's consider a few examples. In sentiment analysis, we can use text cleaning to remove noise from our text data and focus on the words that really matter. For example, in a movie review dataset, we can use text cleaning to remove stopwords and focus on words like "love", "hate", "amazing", etc. In topic modeling, we can use text cleaning to remove noise and focus on the topics that really matter. For example, in a news article dataset, we can use text cleaning to remove stopwords and focus on words like "politics", "sports", "entertainment", etc.

Here are a few more examples of real-world applications:

* **Sentiment Analysis**: Remove noise from text data to focus on words that really matter.
* **Topic Modeling**: Remove noise to focus on topics that really matter.
* **Text Classification**: Remove noise to improve classification accuracy.

## Production Considerations
When deploying our text cleaning pipeline in production, there are several considerations we need to keep in mind. First, we need to consider the scalability of our pipeline. As our text data grows, our pipeline needs to be able to handle the increased volume. We can use techniques like parallel processing and distributed computing to scale our pipeline. Second, we need to consider the robustness of our pipeline. Our pipeline needs to be able to handle noisy or missing data, and we can use techniques like data imputation and outlier detection to handle these cases. Finally, we need to consider the maintainability of our pipeline. Our pipeline needs to be easy to maintain and update, and we can use techniques like modular design and automated testing to ensure this.

Here are a few more production considerations:

* **Monitoring**: Monitor our pipeline for performance issues and errors.
* **Evaluation**: Evaluate our pipeline for accuracy and effectiveness.
* **Scaling**: Scale our pipeline to handle increased volume.

## Conclusion
In conclusion, stopwords and text cleaning are critical components of any NLP pipeline. By understanding the key concepts and techniques involved, we can build robust text cleaning pipelines that can handle even the noisiest of text data. We've explored the key concepts, technical walkthroughs, and real-world applications of text cleaning, and we've discussed production considerations like scalability, robustness, and maintainability. As we move forward in the field of NLP, it's essential that we prioritize text cleaning and make it a core part of our pipelines. With the techniques and strategies outlined in this post, you'll be well on your way to building better text cleaning pipelines and achieving better results in your NLP applications.
```

## File: `frontend/blogs/statistics/articles.json`
```json
[
  {
    "id": "blogs/statistics/measures-of-dispersion.md",
    "category": "statistics",
    "title": "Measures of Dispersion",
    "description": "Learn dispersion stats, boost AI model accuracy",
    "date": "2026-04-01",
    "tags": [
      "statistics-for-ai",
      "data-analysis",
      "machine-learning",
      "dispersion-measures",
      "data-science"
    ],
    "readTime": "5 min",
    "file": "blogs/statistics/measures-of-dispersion.md"
  },
  {
    "id": "blogs/statistics/central-tendency-measures.md",
    "category": "statistics",
    "title": "Central Tendency Measures",
    "description": "Learn to calculate mean, median, and mode for data analysis. Improve your statistical skills.",
    "date": "2026-03-25",
    "tags": [
      "central-tendency",
      "mean-median-mode",
      "data-analysis",
      "statistical-measures",
      "machine-learning"
    ],
    "readTime": "5 min",
    "file": "blogs/statistics/central-tendency-measures.md"
  },
  {
    "id": "blogs/statistics/population-vs-sample.md",
    "category": "statistics",
    "title": "Population vs Sample",
    "description": "Learn key differences, gain insights",
    "date": "2026-03-18",
    "tags": [
      "statistics-for-ai",
      "machine-learning-concepts",
      "data-science-fundamentals",
      "population-statistics",
      "sample-size-calculation"
    ],
    "readTime": "6 min",
    "file": "blogs/statistics/population-vs-sample.md"
  },
  {
    "id": "blogs/statistics/ml-data-types.md",
    "category": "statistics",
    "title": "ML Data Types",
    "description": "Learn key data types in ML. Improve model accuracy.",
    "date": "2026-03-11",
    "tags": [
      "machine-learning",
      "data-preprocessing",
      "data-analysis",
      "data-types",
      "ml-models"
    ],
    "readTime": "5 min",
    "file": "blogs/statistics/ml-data-types.md"
  },
  {
    "id": "blogs/statistics/stats-for-aiml.md",
    "category": "statistics",
    "title": "Stats for AI/ML",
    "description": "Learn stats for AI & ML. Improve model performance",
    "date": "2026-03-04",
    "tags": [
      "machine-learning",
      "artificial-intelligence",
      "data-science",
      "statistical-modeling",
      "data-analytics"
    ],
    "readTime": "6 min",
    "file": "blogs/statistics/stats-for-aiml.md"
  }
]
```

## File: `frontend/blogs/statistics/central-tendency-measures.md`
```markdown
## Introduction
Hello and welcome to this blog post on Central Tendency Measures. As ML engineers and AI developers, we've all been there - stuck in a deployment bottleneck, trying to scale our models, or dealing with limitations that hinder our progress. One such limitation that I've encountered time and again is the lack of understanding of central tendency measures. In the past, we relied on simple statistical methods that often failed to capture the complexity of our data. This led to poor model performance, inaccurate predictions, and ultimately, business losses. However, with the increasing complexity of our data and the need for more accurate predictions, it's become strategically important to understand central tendency measures. In this post, we'll delve into the world of central tendency measures, exploring what they are, how they work, and why they're crucial for our models. By the end of this post, you'll have a deep understanding of central tendency measures and be able to implement them in your own projects.

## Core Concepts
At its core, a central tendency measure is a statistical method that helps us understand the central or typical value of a dataset. There are three primary measures of central tendency: mean, median, and mode. The **mean** is the average value of a dataset, calculated by summing all the values and dividing by the number of values. The **median** is the middle value of a dataset when it's sorted in ascending order. The **mode** is the value that appears most frequently in a dataset. Each of these measures has its strengths and weaknesses, and understanding when to use each is crucial.

| Measure | Description | Strengths | Weaknesses |
| --- | --- | --- | --- |
| Mean | Average value of a dataset | Easy to calculate, sensitive to changes in data | Affected by outliers, not robust |
| Median | Middle value of a dataset | Robust to outliers, easy to understand | Not sensitive to changes in data, can be affected by skewed distributions |
| Mode | Most frequent value in a dataset | Robust to outliers, easy to understand | Can be affected by multiple modes, not sensitive to changes in data |

When misunderstood, central tendency measures can lead to poor model performance and inaccurate predictions. For example, using the mean as the central tendency measure for a dataset with outliers can lead to a skewed representation of the data. On the other hand, using the median can provide a more robust representation of the data, but may not capture the full range of values.

## Technical Walkthrough
Let's take a look at a Python implementation of central tendency measures using the `numpy` library. We'll generate a synthetic dataset with outliers and calculate the mean, median, and mode.
```python
import numpy as np

# Generate synthetic dataset with outliers
np.random.seed(0)
data = np.random.normal(0, 1, 100)
data = np.append(data, [10, 20, 30])  # add outliers

# Calculate mean
mean = np.mean(data)
print("Mean:", mean)

# Calculate median
median = np.median(data)
print("Median:", median)

# Calculate mode
from scipy import stats
mode = stats.mode(data)[0][0]
print("Mode:", mode)
```
In this example, we generate a synthetic dataset with outliers and calculate the mean, median, and mode. The mean is affected by the outliers, while the median provides a more robust representation of the data. The mode is not sensitive to changes in data and can be affected by multiple modes.

## Real-World Applications
Central tendency measures have a wide range of applications in real-world scenarios. Here are three substantial deployment scenarios:

1. **Financial Analysis**: In financial analysis, central tendency measures can be used to understand the average return on investment (ROI) of a portfolio. By calculating the mean, median, and mode of the ROI, analysts can gain insights into the performance of the portfolio and make informed decisions.
2. **Medical Research**: In medical research, central tendency measures can be used to understand the average response to a treatment. By calculating the mean, median, and mode of the response, researchers can gain insights into the effectiveness of the treatment and identify potential outliers.
3. **Customer Segmentation**: In customer segmentation, central tendency measures can be used to understand the average behavior of customers. By calculating the mean, median, and mode of customer behavior, marketers can gain insights into customer preferences and tailor their marketing strategies accordingly.

## Production Considerations
When deploying central tendency measures in production, there are several bottlenecks, edge cases, and failure modes to consider. Here are a few:

* **Monitoring**: Central tendency measures can be affected by changes in data distribution, so it's essential to monitor the data and re-calculate the measures as needed.
* **Evaluation Drift**: Central tendency measures can drift over time, so it's essential to evaluate the measures regularly and adjust as needed.
* **Scaling Concerns**: Central tendency measures can be computationally expensive, so it's essential to optimize the calculations for large datasets.

To optimize central tendency measures, we can use techniques such as:

* **Data Sampling**: Sampling the data to reduce the computational cost of calculating central tendency measures.
* **Parallel Processing**: Using parallel processing to calculate central tendency measures on large datasets.
* **Approximation**: Using approximation techniques, such as the **bootstrap method**, to estimate central tendency measures.

## Conclusion
In conclusion, central tendency measures are a crucial aspect of statistical analysis and machine learning. By understanding the mean, median, and mode, we can gain insights into the central or typical value of a dataset. In this post, we've explored the core concepts of central tendency measures, provided a technical walkthrough of a Python implementation, and discussed real-world applications and production considerations. As ML engineers and AI developers, it's essential to have a deep understanding of central tendency measures to build robust and accurate models. By applying the concepts and techniques discussed in this post, you'll be able to build more accurate models and make informed decisions in your projects.
```

## File: `frontend/blogs/statistics/measures-of-dispersion.md`
```markdown
## Introduction
Hello and welcome to this blog post on Measures of Dispersion. As machine learning engineers and AI developers, we've all encountered the challenge of understanding the spread of our data. Whether it's in a regression problem or a classification task, dispersion is a crucial aspect of our datasets that can make or break our models. I've seen many deployments bottlenecked due to poor handling of dispersion, leading to suboptimal performance and scaling issues. In this post, we'll dive into the world of measures of dispersion, exploring what was broken in previous approaches and why it mattered. By the end of this article, you'll understand the core concepts of dispersion, be able to implement them in your own projects, and appreciate the strategic importance of this topic in the current machine learning landscape.

In the past, many of us relied on simple statistical measures like the mean and standard deviation to understand our data. However, these measures often fell short, failing to capture the nuances of our datasets. The mean, for instance, can be heavily influenced by outliers, while the standard deviation can be sensitive to the choice of distribution. As a result, our models suffered, and we were left wondering why our predictions were off the mark. It wasn't until we started exploring other measures of dispersion that we began to unlock the true potential of our data.

## Core Concepts
So, what are measures of dispersion, and how do they work under the hood? At its core, dispersion refers to the spread of a dataset, or how much individual data points deviate from the mean. There are several key concepts to understand here, including:

* **Variance**: The average of the squared differences from the mean. Variance is a fundamental measure of dispersion, but it can be sensitive to outliers.
* **Standard Deviation**: The square root of the variance. Standard deviation is a more interpretable measure of dispersion, but it can still be influenced by outliers.
* **Interquartile Range (IQR)**: The difference between the 75th percentile and the 25th percentile. IQR is a more robust measure of dispersion, less sensitive to outliers.
* **Median Absolute Deviation (MAD)**: The median of the absolute differences from the median. MAD is another robust measure of dispersion, useful for datasets with non-normal distributions.

To illustrate the differences between these measures, consider the following table:

| Measure | Description | Sensitivity to Outliers |
| --- | --- | --- |
| Variance | Average of squared differences from mean | High |
| Standard Deviation | Square root of variance | High |
| IQR | Difference between 75th and 25th percentiles | Low |
| MAD | Median of absolute differences from median | Low |

## Technical Walkthrough
Let's implement a simple example in Python to illustrate the calculation of these measures. We'll use the `numpy` library to generate some synthetic data and calculate the variance, standard deviation, IQR, and MAD.
```python
import numpy as np

# Generate some synthetic data
np.random.seed(0)
data = np.random.normal(0, 1, 100)

# Calculate variance and standard deviation
variance = np.var(data)
std_dev = np.std(data)

# Calculate IQR
q75, q25 = np.percentile(data, [75, 25])
iqr = q75 - q25

# Calculate MAD
mad = np.median(np.abs(data - np.median(data)))

print("Variance:", variance)
print("Standard Deviation:", std_dev)
print("IQR:", iqr)
print("MAD:", mad)
```
In this example, we generate some random data from a normal distribution and calculate the variance, standard deviation, IQR, and MAD. We can see how the different measures capture the spread of the data in different ways.

## Real-World Applications
Measures of dispersion have numerous real-world applications. Here are a few examples:

* **Finance**: In finance, dispersion is crucial for understanding the risk of a portfolio. By calculating the variance or standard deviation of a portfolio's returns, investors can gauge the potential for losses.
* **Quality Control**: In manufacturing, dispersion is used to monitor the quality of products. By tracking the variance or IQR of product dimensions, manufacturers can identify issues with their production process.
* **Medical Research**: In medical research, dispersion is used to understand the variability of patient responses to treatments. By calculating the MAD or IQR of patient outcomes, researchers can identify trends and patterns in the data.

## Production Considerations
When deploying measures of dispersion in production, there are several considerations to keep in mind:

* **Bottlenecks**: Calculating dispersion measures can be computationally intensive, especially for large datasets. To avoid bottlenecks, consider using parallel processing or distributed computing.
* **Edge Cases**: Dispersion measures can be sensitive to edge cases, such as outliers or missing data. To handle these cases, consider using robust measures like IQR or MAD.
* **Failure Modes**: Dispersion measures can fail if the data is not normally distributed. To avoid failure modes, consider using non-parametric measures like IQR or MAD.

## Conclusion
In conclusion, measures of dispersion are a crucial aspect of machine learning and data analysis. By understanding the core concepts of variance, standard deviation, IQR, and MAD, we can unlock the true potential of our data. Whether it's in finance, quality control, or medical research, dispersion measures have numerous real-world applications. As we move forward in the field of machine learning, it's essential to consider the strategic importance of dispersion and its role in building robust and scalable models. By following the principles outlined in this post, you'll be well-equipped to tackle the challenges of dispersion and build models that truly capture the complexity of your data.
```

## File: `frontend/blogs/statistics/ml-data-types.md`
```markdown
Hello and welcome to this blog post on ML Data Types, where we'll be diving into the world of machine learning data and exploring its various types. As machine learning engineers, we've all been there - stuck in the deployment phase, trying to troubleshoot why our model isn't performing as expected. Often, the bottleneck lies in the data itself. In my experience, understanding the different types of data in machine learning is crucial for building robust and scalable models. Previous approaches often overlooked the nuances of data types, leading to suboptimal performance and scaling issues. In this post, we'll delve into the key concepts, technical walkthroughs, and real-world applications of ML data types, ensuring that you'll walk away with a deep understanding of how to work with different data types and build more effective models.

## Core Concepts
At the heart of machine learning lies data, and understanding its various types is essential for any practitioner. There are several key concepts to grasp, including numerical, categorical, text, image, and audio data. Numerical data, for instance, can be further divided into integer and floating-point numbers, each with its own set of challenges and considerations. Categorical data, on the other hand, can be either nominal or ordinal, requiring different encoding techniques. 

When working with text data, we need to consider the nuances of natural language processing, including tokenization, stemming, and lemmatization. Image and audio data, often used in deep learning applications, require specialized libraries and preprocessing techniques. Misunderstanding these concepts can lead to poor model performance, data leakage, or even model collapse. 

Here's a comparison of related approaches in a clear table:

| Data Type | Description | Encoding Technique |
| --- | --- | --- |
| Numerical | Integer or floating-point numbers | Standardization or normalization |
| Categorical | Nominal or ordinal categories | One-hot encoding or label encoding |
| Text | Natural language text | Tokenization, stemming, or lemmatization |
| Image | Visual data | Convolutional neural networks (CNNs) |
| Audio | Audio signals | Recurrent neural networks (RNNs) or CNNs |

## Technical Walkthrough
Let's provide a cohesive implementation example using Python and the popular scikit-learn library. We'll work with a synthetic dataset containing numerical, categorical, and text features. Our goal is to build a classification model that predicts a target variable based on these features.

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder

# Load synthetic dataset
data = pd.read_csv('synthetic_data.csv')

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.drop('target', axis=1), data['target'], test_size=0.2, random_state=42)

# Preprocess numerical features
scaler = StandardScaler()
X_train_numeric = scaler.fit_transform(X_train[['num_feature1', 'num_feature2']])
X_test_numeric = scaler.transform(X_test[['num_feature1', 'num_feature2']])

# Preprocess categorical features
encoder = OneHotEncoder()
X_train_categorical = encoder.fit_transform(X_train[['cat_feature1', 'cat_feature2']])
X_test_categorical = encoder.transform(X_test[['cat_feature1', 'cat_feature2']])

# Preprocess text features
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
X_train_text = vectorizer.fit_transform(X_train['text_feature'])
X_test_text = vectorizer.transform(X_test['text_feature'])

# Combine preprocessed features
X_train_combined = pd.concat([pd.DataFrame(X_train_numeric), pd.DataFrame(X_train_categorical.toarray()), pd.DataFrame(X_train_text.toarray())], axis=1)
X_test_combined = pd.concat([pd.DataFrame(X_test_numeric), pd.DataFrame(X_test_categorical.toarray()), pd.DataFrame(X_test_text.toarray())], axis=1)

# Train classification model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_combined, y_train)

# Evaluate model performance
accuracy = model.score(X_test_combined, y_test)
print(f'Model accuracy: {accuracy:.3f}')
```

In this example, we've demonstrated how to preprocess different data types and combine them into a single dataset for modeling. We've also shown how to train a classification model and evaluate its performance.

## Real-World Applications
Machine learning data types have numerous real-world applications across various industries. Here are three substantial deployment scenarios:

1. **Customer Segmentation**: A retail company wants to segment its customers based on their demographic, behavioral, and transactional data. The company can use a combination of numerical, categorical, and text features to build a clustering model that identifies distinct customer segments.
2. **Image Classification**: A healthcare organization wants to develop an image classification model that can diagnose diseases from medical images. The organization can use convolutional neural networks (CNNs) to extract features from the images and train a classification model.
3. **Natural Language Processing**: A technology company wants to build a chatbot that can understand and respond to customer inquiries. The company can use natural language processing (NLP) techniques, such as tokenization, stemming, and lemmatization, to preprocess the text data and train a language model.

## Production Considerations
When deploying machine learning models in production, there are several considerations to keep in mind. One of the primary concerns is **data drift**, where the distribution of the data changes over time, affecting the model's performance. To address this, we can implement **monitoring** and **evaluation** strategies, such as tracking model metrics and retraining the model periodically.

Another consideration is **scaling**, where the model needs to handle large volumes of data and traffic. To achieve this, we can use **distributed computing** frameworks, such as Apache Spark or TensorFlow, to parallelize the computation and speed up the processing.

Finally, **optimization** is crucial in production environments, where resources are limited, and efficiency is key. We can use **hyperparameter tuning** techniques, such as grid search or random search, to find the optimal model parameters and improve the model's performance.

## Conclusion
In conclusion, understanding the different types of data in machine learning is essential for building robust and scalable models. By grasping the core concepts, technical walkthroughs, and real-world applications of ML data types, we can develop more effective models that drive business value. As machine learning engineers, we must stay up-to-date with the latest trends and advancements in the field, such as the increasing use of **transfer learning** and **autoML** techniques. By doing so, we can unlock the full potential of machine learning and drive innovation in various industries. Thank you for joining me on this journey into the world of ML data types.
```

## File: `frontend/blogs/statistics/population-vs-sample.md`
```markdown
## Introduction
Hello and welcome to this technical exploration of a critical concept in data science and machine learning: the distinction between population and sample. In recent projects, I've encountered deployment bottlenecks stemming from misunderstandings of these concepts, leading to inefficient model training and suboptimal predictions. The previous approach of treating any collected data as representative of the entire population has proven to be limiting, especially when dealing with large, diverse datasets. This oversight matters because it directly impacts the accuracy and reliability of our models. The strategic importance of understanding population vs sample cannot be overstated, especially in today's data-driven world where informed decision-making is paramount. By the end of this article, readers will have a deep understanding of these concepts, know how to apply them in real-world scenarios, and be able to build more accurate and robust models.

## Core Concepts
At the heart of statistical analysis and machine learning lies the concept of population and sample. A **population** refers to the entire set of items of interest, whereas a **sample** is a subset of the population. For instance, if we're studying the average height of all adults in a country, the population would include every single adult in that country, while a sample might consist of a thousand randomly selected adults. Understanding the difference is crucial because it affects how we collect, analyze, and interpret data. Misunderstanding these concepts can lead to biased models, incorrect conclusions, and poor decision-making.

The key idea here is that a sample should be representative of the population to ensure that our findings can be generalized. However, achieving a perfectly representative sample is challenging due to various factors like selection bias, non-response bias, and measurement errors. When misunderstood, these concepts can lead to overfitting or underfitting in machine learning models. Overfitting occurs when a model is too closely fit to the sample data, failing to generalize well to the broader population, while underfitting happens when a model is too simple to capture the underlying patterns in the sample, again failing to represent the population accurately.

Here's a comparison of related approaches in a clear table:

| Approach | Description | Advantages | Disadvantages |
| --- | --- | --- | --- |
| **Population Study** | Analyzing the entire population | High accuracy, no sampling bias | Often impractical due to cost, time, or feasibility |
| **Random Sampling** | Selecting a sample at random from the population | Representative of the population, reduces bias | May not capture rare events or outliers |
| **Stratified Sampling** | Dividing the population into subgroups and sampling from each | Ensures representation of subgroups, reduces bias | Requires prior knowledge of subgroups |

## Technical Walkthrough
To illustrate the practical application of these concepts, let's consider a scenario where we want to predict the average salary of software engineers in the United States using a simple linear regression model. We'll use synthetic data for this example.

First, we generate a population of 100,000 software engineers with varying salaries based on their years of experience. Then, we randomly sample 1,000 engineers from this population.

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generate population data
np.random.seed(0)
population_size = 100000
years_of_experience = np.random.uniform(0, 20, population_size)
salaries = 50000 + 3000 * years_of_experience + np.random.normal(0, 10000, population_size)

# Create a DataFrame
population_df = pd.DataFrame({'years_of_experience': years_of_experience, 'salary': salaries})

# Sample from the population
sample_size = 1000
sample_df = population_df.sample(sample_size)

# Split the sample into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(sample_df['years_of_experience'], sample_df['salary'], test_size=0.2, random_state=42)

# Train a linear regression model
model = LinearRegression()
model.fit(X_train.values.reshape(-1, 1), y_train)

# Make predictions and evaluate the model
y_pred = model.predict(X_test.values.reshape(-1, 1))
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
```

This example demonstrates how we can use a sample to train a model that predicts salaries based on years of experience. The model's performance is evaluated using the mean squared error (MSE) on the test set.

## Real-World Applications
The distinction between population and sample has significant implications in various real-world applications:

1. **Customer Segmentation**: In marketing, understanding whether your sample of customers is representative of your entire customer base is crucial for effective segmentation and targeted campaigns.
2. **Medical Research**: Clinical trials often rely on samples of patients to test the efficacy of new treatments. Ensuring that these samples are representative of the broader population of patients with the condition is vital for the validity of the research findings.
3. **Quality Control**: In manufacturing, samples of products are inspected to ensure they meet quality standards. The sample must be representative of the entire production batch to accurately assess quality.

Each of these scenarios requires careful consideration of how the sample is selected and analyzed to ensure that conclusions can be generalized to the population of interest.

## Production Considerations
When deploying models in production, several considerations come into play:

- **Monitoring and Evaluation**: Continuously monitor the model's performance on new, unseen data to detect any drift in the population or sample.
- **Scaling**: As the population or sample size increases, the model's ability to handle larger datasets must be ensured, which might involve distributed computing or more efficient algorithms.
- **Failure Modes**: Anticipate and mitigate potential failure modes, such as overfitting or data leakage, by implementing robust validation protocols and continuously updating the model with new data.

Optimization strategies, such as hyperparameter tuning and feature engineering, can also significantly impact the model's performance and should be carefully considered in the production environment.

## Conclusion
In conclusion, the distinction between population and sample is a foundational concept in data science and machine learning, with far-reaching implications for model accuracy, reliability, and scalability. By understanding these concepts deeply and applying them correctly, practitioners can build more robust models that generalize well to the population of interest. As data-driven decision-making continues to play an increasingly critical role in various industries, the strategic importance of grasping population vs sample will only continue to grow. Looking forward, advancements in sampling methods, model interpretability, and automated machine learning will likely further underscore the need for a nuanced understanding of these concepts.
```

## File: `frontend/blogs/statistics/stats-for-aiml.md`
```markdown
Hello and welcome to this comprehensive guide on statistics for AI and ML. As we continue to push the boundaries of what is possible with artificial intelligence and machine learning, it's becoming increasingly clear that a deep understanding of statistical concepts is crucial for building robust and reliable models. In this blog post, we'll explore why statistics is essential for AI and ML, delve into the applications of statistics in these fields, and provide a technical walkthrough of how to apply statistical concepts to real-world problems.

## Introduction to Statistics for AI/ML

In recent years, we've seen a significant increase in the deployment of AI and ML models in production environments. However, many of these models have been found to be brittle and prone to failure when faced with real-world data. One of the primary reasons for this is the lack of understanding of statistical concepts and how they apply to AI and ML. Traditional approaches to building AI and ML models have focused on optimizing performance on a specific dataset, without considering the underlying statistical properties of the data. This has led to models that are overfit to the training data and fail to generalize well to new, unseen data.

The importance of statistics in AI and ML cannot be overstated. Statistical concepts such as probability, inference, and regression are the foundation upon which many AI and ML algorithms are built. By understanding these concepts, practitioners can build models that are more robust, reliable, and generalizable. In this blog post, we'll explore the key statistical concepts that are relevant to AI and ML, and provide a technical walkthrough of how to apply these concepts to real-world problems.

By the end of this blog post, readers will have a deep understanding of the statistical concepts that underlie AI and ML, and will be able to apply these concepts to build more robust and reliable models. We'll cover topics such as probability, inference, regression, and hypothesis testing, and provide examples of how these concepts can be applied in real-world scenarios.

## Core Concepts

At the heart of statistics for AI and ML are several key concepts that are essential for building robust and reliable models. These concepts include:

* **Probability**: The study of chance events and their likelihood of occurrence. Probability is a fundamental concept in statistics, and is used to model the uncertainty associated with real-world events.
* **Inference**: The process of drawing conclusions about a population based on a sample of data. Inference is a critical concept in statistics, and is used to make predictions about future events.
* **Regression**: A statistical technique used to model the relationship between a dependent variable and one or more independent variables. Regression is a widely used technique in AI and ML, and is used to build models that can predict continuous outcomes.

These concepts are essential for building AI and ML models that are robust and reliable. By understanding probability, inference, and regression, practitioners can build models that can handle uncertainty and make accurate predictions.

| Concept | Description | Example |
| --- | --- | --- |
| Probability | Study of chance events and their likelihood of occurrence | Predicting the probability of a customer churning |
| Inference | Process of drawing conclusions about a population based on a sample of data | Using a sample of data to estimate the average height of a population |
| Regression | Statistical technique used to model the relationship between a dependent variable and one or more independent variables | Building a model to predict house prices based on features such as number of bedrooms and square footage |

## Technical Walkthrough

To illustrate the application of statistical concepts to real-world problems, let's consider a simple example. Suppose we want to build a model to predict the probability of a customer churning based on their usage patterns. We have a dataset that contains information about the customer's usage patterns, including the number of calls made, the number of texts sent, and the average monthly bill.

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# Load the dataset
df = pd.read_csv('customer_data.csv')

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df.drop('churn', axis=1), df['churn'], test_size=0.2, random_state=42)

# Train a logistic regression model on the training data
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluate the model on the testing data
accuracy = model.score(X_test, y_test)
print(f'Accuracy: {accuracy:.3f}')
```

In this example, we use a logistic regression model to predict the probability of a customer churning based on their usage patterns. We split the dataset into training and testing sets, train the model on the training data, and evaluate its performance on the testing data.

## Real-World Applications

Statistical concepts have a wide range of applications in AI and ML. Some examples include:

* **Predictive maintenance**: Using statistical models to predict when equipment is likely to fail, allowing for proactive maintenance and reducing downtime.
* **Recommendation systems**: Using statistical models to recommend products or services to customers based on their past behavior and preferences.
* **Fraud detection**: Using statistical models to detect and prevent fraudulent activity, such as credit card fraud or insurance claims.

These applications demonstrate the power and versatility of statistical concepts in AI and ML. By applying statistical techniques to real-world problems, practitioners can build models that are robust, reliable, and accurate.

## Production Considerations

When deploying statistical models in production, there are several considerations that must be taken into account. These include:

* **Data quality**: Ensuring that the data used to train and test the model is accurate and reliable.
* **Model drift**: Monitoring the model's performance over time and updating it as necessary to prevent drift.
* **Scalability**: Ensuring that the model can handle large volumes of data and traffic.

By considering these factors, practitioners can build models that are robust, reliable, and scalable, and that can handle the demands of real-world production environments.

## Conclusion

In conclusion, statistical concepts are essential for building robust and reliable AI and ML models. By understanding probability, inference, regression, and other statistical techniques, practitioners can build models that can handle uncertainty and make accurate predictions. In this blog post, we've explored the key statistical concepts that are relevant to AI and ML, and provided a technical walkthrough of how to apply these concepts to real-world problems. We've also discussed real-world applications and production considerations, and demonstrated the power and versatility of statistical concepts in AI and ML. As the field of AI and ML continues to evolve, it's clear that statistical concepts will play an increasingly important role in building robust and reliable models.
```

## File: `frontend/css/category.css`
```css
/* ===================================================
   CATEGORY.CSS — Category listing page styles
   =================================================== */

/* ── Category Hero ── */
.cat-hero {
    position: relative;
    z-index: 10;
    padding: calc(var(--nav-height) + 60px) 24px 60px;
    text-align: center;
}

.cat-hero-inner {
    max-width: 680px;
    margin: 0 auto;
}

.breadcrumb {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    color: var(--text-muted);
    font-size: 0.85rem;
    font-weight: 500;
    margin-bottom: 24px;
    transition: color var(--trans-fast);
}

.breadcrumb:hover {
    color: var(--accent-primary);
}

.cat-hero-icon {
    font-size: 3rem;
    margin-bottom: 16px;
    line-height: 1;
}

.cat-badge {
    display: inline-block;
    padding: 4px 16px;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 16px;
}

.cat-hero-title {
    font-family: var(--font-serif);
    font-size: clamp(2rem, 5vw, 3.2rem);
    color: var(--text-primary);
    letter-spacing: -0.03em;
    line-height: 1.2;
    margin-bottom: 14px;
}

.cat-hero-desc {
    font-size: 1rem;
    color: var(--text-secondary);
    line-height: 1.7;
    margin-bottom: 24px;
}

.cat-count-wrap {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 20px;
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: 999px;
}

.cat-count {
    font-size: 1.1rem;
    font-weight: 700;
    color: var(--text-primary);
}

.cat-count-label {
    font-size: 0.85rem;
    color: var(--text-muted);
}

/* ── Filter Bar ── */
.filter-bar {
    position: sticky;
    top: var(--nav-height);
    z-index: 100;
    background: rgba(10, 12, 20, 0.85);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border-card);
    border-top: 1px solid var(--border-card);
}

.filter-inner {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 14px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
}

.filter-group {
    display: flex;
    align-items: center;
    gap: 10px;
}

.filter-label {
    font-size: 0.8rem;
    color: var(--text-muted);
    font-weight: 500;
}

.filter-btn {
    padding: 6px 16px;
    border-radius: 999px;
    border: 1px solid var(--border);
    background: transparent;
    color: var(--text-secondary);
    font-size: 0.8rem;
    font-weight: 500;
    cursor: pointer;
    font-family: var(--font-sans);
    transition: all var(--trans-fast);
}

.filter-btn.active,
.filter-btn:hover {
    border-color: var(--accent-primary);
    color: var(--accent-primary);
    background: rgba(124, 106, 247, 0.08);
}

.search-wrap {
    position: relative;
    flex: 0 1 280px;
}

.search-icon {
    position: absolute;
    left: 12px;
    top: 50%;
    transform: translateY(-50%);
    width: 16px;
    height: 16px;
    color: var(--text-muted);
    pointer-events: none;
}

.search-input {
    width: 100%;
    padding: 8px 14px 8px 36px;
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: var(--radius-md);
    color: var(--text-primary);
    font-size: 0.85rem;
    font-family: var(--font-sans);
    outline: none;
    transition: border-color var(--trans-fast);
}

.search-input::placeholder {
    color: var(--text-muted);
}

.search-input:focus {
    border-color: var(--accent-primary);
}

/* ── Blog List ── */
.blog-list-section {
    position: relative;
    z-index: 10;
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 40px 24px 80px;
}

.blog-list {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

/* Blog List Item */
.blog-item {
    display: flex;
    align-items: flex-start;
    gap: 20px;
    padding: 24px;
    background: transparent;
    border-radius: var(--radius-md);
    transition: all var(--trans-base);
    cursor: pointer;
    text-decoration: none;
    color: inherit;
    position: relative;
}

.blog-item::before {
    content: '';
    position: absolute;
    left: 0;
    top: 0;
    bottom: 0;
    width: 2px;
    border-radius: 2px;
    background: var(--accent-primary);
    opacity: 0;
    transform: scaleY(0);
    transition: all var(--trans-base);
}

.blog-item:hover {
    background: var(--bg-card);
}

.blog-item:hover::before {
    opacity: 1;
    transform: scaleY(1);
}

.blog-item-num {
    font-family: var(--font-mono);
    font-size: 0.75rem;
    color: var(--text-muted);
    min-width: 28px;
    padding-top: 4px;
    flex-shrink: 0;
}

.blog-item-body {
    flex: 1;
    min-width: 0;
}

.blog-item-meta {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
    flex-wrap: wrap;
}

.blog-item-date {
    font-size: 0.8rem;
    font-family: var(--font-mono);
    color: var(--text-muted);
}

.blog-item-tag {
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 2px 8px;
    border-radius: 4px;
}

.blog-item-title {
    font-size: 1.05rem;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1.4;
    margin-bottom: 8px;
    transition: color var(--trans-fast);
}

.blog-item:hover .blog-item-title {
    color: var(--accent-primary);
}

.blog-item-desc {
    font-size: 0.875rem;
    color: var(--text-secondary);
    line-height: 1.6;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.blog-item-footer {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-top: 10px;
}

.read-time {
    font-size: 0.78rem;
    color: var(--text-muted);
}

.blog-item-arrow {
    margin-left: auto;
    color: var(--text-muted);
    font-size: 1.2rem;
    flex-shrink: 0;
    transition: transform var(--trans-fast), color var(--trans-fast);
    padding-top: 4px;
}

.blog-item:hover .blog-item-arrow {
    transform: translateX(4px);
    color: var(--accent-primary);
}

/* ── Empty State ── */
.empty-state {
    text-align: center;
    padding: 80px 20px;
    color: var(--text-muted);
}

.empty-icon {
    font-size: 3rem;
    margin-bottom: 16px;
}

.empty-state h3 {
    font-size: 1.2rem;
    color: var(--text-secondary);
    margin-bottom: 8px;
}

.empty-state p {
    font-size: 0.9rem;
}

/* ── Category Color Themes ── */
.theme-ml .cat-badge {
    background: rgba(124, 106, 247, 0.15);
    color: var(--cat-ml);
}

.theme-dl .cat-badge {
    background: rgba(79, 200, 184, 0.15);
    color: var(--cat-dl);
}

.theme-nlp .cat-badge {
    background: rgba(247, 185, 106, 0.15);
    color: var(--cat-nlp);
}

.theme-cv .cat-badge {
    background: rgba(247, 106, 106, 0.15);
    color: var(--cat-cv);
}

.theme-genai .cat-badge {
    background: rgba(208, 106, 247, 0.15);
    color: var(--cat-genai);
}

.theme-ainews .cat-badge {
    background: rgba(106, 180, 247, 0.15);
    color: var(--cat-ainews);
}

.theme-ml .blog-item::before {
    background: var(--cat-ml);
}

.theme-dl .blog-item::before {
    background: var(--cat-dl);
}

.theme-nlp .blog-item::before {
    background: var(--cat-nlp);
}

.theme-cv .blog-item::before {
    background: var(--cat-cv);
}

.theme-genai .blog-item::before {
    background: var(--cat-genai);
}

.theme-ainews .blog-item::before {
    background: var(--cat-ainews);
}

.theme-statistics .cat-badge {
    background: rgba(251, 146, 60, 0.15);
    color: #fb923c;
}

.theme-statistics .blog-item::before {
    background: #fb923c;
}

/* ── Category Schedule Badge ── */
.cat-schedule-badge {
    display: none;
    align-items: center;
    gap: 8px;
    margin-top: 16px;
    padding: 10px 20px;
    background: rgba(124, 106, 247, 0.06);
    border: 1px solid rgba(124, 106, 247, 0.15);
    border-radius: 999px;
    font-size: 0.85rem;
    color: var(--text-secondary);
    justify-content: center;
    animation: fadeIn 0.4s ease;
}

.cat-schedule-badge strong {
    color: var(--text-primary);
    font-weight: 600;
}

.sched-icon {
    font-size: 1rem;
}

@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(4px);
    }

    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ── Responsive ── */
@media (max-width: 640px) {
    .filter-inner {
        flex-direction: column;
        align-items: flex-start;
    }

    .search-wrap {
        flex: 1 1 100%;
    }

    .blog-item-num {
        display: none;
    }
}
```

## File: `frontend/css/home.css`
```css
/* ===================================================
   HOME.CSS — Home page specific styles
   =================================================== */

/* ── Hero ── */
.hero {
    position: relative;
    z-index: 10;
    min-height: 100vh;
    display: flex;
    align-items: center;
    padding: calc(var(--nav-height) + 40px) 24px 80px;
    max-width: var(--max-width);
    margin: 0 auto;
    gap: 60px;
}

.hero-content {
    flex: 1;
    max-width: 620px;
}

.hero-badge {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 6px 16px;
    background: rgba(79, 200, 184, 0.1);
    border: 1px solid rgba(79, 200, 184, 0.2);
    border-radius: 999px;
    font-size: 0.8rem;
    font-weight: 500;
    color: var(--accent-secondary);
    margin-bottom: 24px;
}

.pulse-dot {
    width: 7px;
    height: 7px;
    background: var(--accent-secondary);
    border-radius: 50%;
    animation: pulse 2s ease-in-out infinite;
}

@keyframes pulse {

    0%,
    100% {
        transform: scale(1);
        opacity: 1;
    }

    50% {
        transform: scale(1.4);
        opacity: 0.5;
    }
}

.hero-title {
    font-family: var(--font-serif);
    font-size: clamp(2.4rem, 5vw, 3.8rem);
    line-height: 1.15;
    letter-spacing: -0.03em;
    color: var(--text-primary);
    margin-bottom: 20px;
}

.hero-sub {
    font-size: 1.05rem;
    color: var(--text-secondary);
    line-height: 1.75;
    margin-bottom: 36px;
    max-width: 520px;
}

.hero-cta {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-bottom: 48px;
}

.hero-stats {
    display: flex;
    align-items: center;
    gap: 28px;
}

.stat {
    display: flex;
    flex-direction: column;
    align-items: center;
}

.stat-num {
    font-size: 1.6rem;
    font-weight: 700;
    color: var(--text-primary);
    letter-spacing: -0.03em;
}

.stat-label {
    font-size: 0.75rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.06em;
    font-weight: 500;
}

.stat-divider {
    width: 1px;
    height: 36px;
    background: var(--border-card);
}

/* ── Neural Net Visual ── */
.hero-visual {
    flex: 0 0 auto;
    width: 420px;
    height: 420px;
    position: relative;
}

.neural-net {
    width: 100%;
    height: 100%;
}

.neural-net svg {
    width: 100%;
    height: 100%;
    overflow: visible;
}

/* ── Categories Section ── */
.categories-section {
    position: relative;
    z-index: 10;
    padding: 100px 24px;
    max-width: var(--max-width);
    margin: 0 auto;
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 20px;
}



.cat-card {
    position: relative;
    display: flex;
    align-items: flex-start;
    gap: 16px;
    padding: 24px;
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: var(--radius-lg);
    cursor: pointer;
    transition: all var(--trans-slow);
    overflow: hidden;
    text-decoration: none;
    color: inherit;
}

.cat-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(135deg, rgba(124, 106, 247, 0.04), transparent);
    opacity: 0;
    transition: opacity var(--trans-base);
}

.cat-card:hover {
    border-color: var(--border-hover);
    transform: translateY(-4px);
    box-shadow: var(--shadow-card), var(--shadow-glow);
    background: var(--bg-card-hover);
}

.cat-card:hover::before {
    opacity: 1;
}

.cat-card[data-cat="ml"]:hover {
    border-color: rgba(124, 106, 247, 0.4);
}

.cat-card[data-cat="dl"]:hover {
    border-color: rgba(79, 200, 184, 0.4);
}

.cat-card[data-cat="nlp"]:hover {
    border-color: rgba(247, 185, 106, 0.4);
}

.cat-card[data-cat="cv"]:hover {
    border-color: rgba(247, 106, 106, 0.4);
}

.cat-card[data-cat="genai"]:hover {
    border-color: rgba(208, 106, 247, 0.4);
}

.cat-card[data-cat="ainews"]:hover {
    border-color: rgba(106, 180, 247, 0.4);
}

.cat-card[data-cat="statistics"]:hover {
    border-color: rgba(251, 146, 60, 0.4);
}

.cat-icon-wrap {
    flex-shrink: 0;
    width: 44px;
    height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
    background: rgba(124, 106, 247, 0.1);
    border-radius: var(--radius-sm);
    color: var(--accent-primary);
    transition: background var(--trans-base);
}

.cat-card[data-cat="dl"] .cat-icon-wrap {
    background: rgba(79, 200, 184, 0.1);
    color: var(--cat-dl);
}

.cat-card[data-cat="nlp"] .cat-icon-wrap {
    background: rgba(247, 185, 106, 0.1);
    color: var(--cat-nlp);
}

.cat-card[data-cat="cv"] .cat-icon-wrap {
    background: rgba(247, 106, 106, 0.1);
    color: var(--cat-cv);
}

.cat-card[data-cat="genai"] .cat-icon-wrap {
    background: rgba(208, 106, 247, 0.1);
    color: var(--cat-genai);
}

.cat-card[data-cat="ainews"] .cat-icon-wrap {
    background: rgba(106, 180, 247, 0.1);
    color: var(--cat-ainews);
}

.cat-icon {
    width: 26px;
    height: 26px;
}

.cat-content {
    flex: 1;
    min-width: 0;
}

.cat-tag {
    display: inline-block;
    padding: 2px 10px;
    background: rgba(124, 106, 247, 0.12);
    color: var(--accent-primary);
    border-radius: 999px;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.06em;
    text-transform: uppercase;
    margin-bottom: 6px;
}

.cat-card[data-cat="dl"] .cat-tag {
    background: rgba(79, 200, 184, 0.12);
    color: var(--cat-dl);
}

.cat-card[data-cat="nlp"] .cat-tag {
    background: rgba(247, 185, 106, 0.12);
    color: var(--cat-nlp);
}

.cat-card[data-cat="cv"] .cat-tag {
    background: rgba(247, 106, 106, 0.12);
    color: var(--cat-cv);
}

.cat-card[data-cat="genai"] .cat-tag {
    background: rgba(208, 106, 247, 0.12);
    color: var(--cat-genai);
}

.cat-card[data-cat="ainews"] .cat-tag {
    background: rgba(106, 180, 247, 0.12);
    color: var(--cat-ainews);
}

.cat-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
    margin-bottom: 6px;
    line-height: 1.3;
}

.cat-desc {
    font-size: 0.83rem;
    color: var(--text-muted);
    line-height: 1.5;
}

.cat-arrow {
    color: var(--text-muted);
    font-size: 1.1rem;
    transition: transform var(--trans-base), color var(--trans-base);
    flex-shrink: 0;
    margin-top: 2px;
}

.cat-card:hover .cat-arrow {
    transform: translateX(4px);
    color: var(--accent-primary);
}

.cat-glow {
    position: absolute;
    inset: 0;
    border-radius: inherit;
    pointer-events: none;
    background: radial-gradient(circle at 80% 50%, rgba(124, 106, 247, 0.06), transparent 60%);
    opacity: 0;
    transition: opacity var(--trans-base);
}

.cat-card:hover .cat-glow {
    opacity: 1;
}

/* ── Recent Section ── */
.recent-section {
    position: relative;
    z-index: 10;
    padding: 60px 24px 80px;
    max-width: var(--max-width);
    margin: 0 auto;
}

.recent-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
    gap: 20px;
}

.recent-card {
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: var(--radius-lg);
    padding: 24px;
    transition: all var(--trans-slow);
    display: flex;
    flex-direction: column;
    gap: 12px;
    cursor: pointer;
    text-decoration: none;
    color: inherit;
}

.recent-card:hover {
    border-color: var(--border-hover);
    transform: translateY(-3px);
    box-shadow: var(--shadow-card);
    background: var(--bg-card-hover);
}

.recent-card-meta {
    display: flex;
    align-items: center;
    gap: 10px;
}

.recent-cat-badge {
    padding: 2px 10px;
    border-radius: 999px;
    font-size: 0.7rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

.recent-card-date {
    font-size: 0.8rem;
    color: var(--text-muted);
}

.recent-card-title {
    font-size: 1rem;
    font-weight: 600;
    color: var(--text-primary);
    line-height: 1.4;
    transition: color var(--trans-fast);
}

.recent-card:hover .recent-card-title {
    color: var(--accent-primary);
}

.recent-card-desc {
    font-size: 0.85rem;
    color: var(--text-secondary);
    line-height: 1.6;
    flex: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
}

.recent-card-read {
    font-size: 0.8rem;
    color: var(--text-muted);
    font-weight: 500;
}

/* ── Responsive ── */
@media (max-width: 1024px) {
    .hero {
        flex-direction: column;
        text-align: center;
        min-height: auto;
        padding-top: calc(var(--nav-height) + 60px);
    }

    .hero-content {
        max-width: 100%;
    }

    .hero-cta {
        justify-content: center;
    }

    .hero-stats {
        justify-content: center;
    }

    .hero-visual {
        width: 300px;
        height: 300px;
    }

    .categories-grid {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 640px) {
    .categories-grid {
        grid-template-columns: 1fr;
    }

    .hero-visual {
        width: 240px;
        height: 240px;
    }

    .hero-title {
        font-size: 2rem;
    }
}
```

## File: `frontend/css/main.css`
```css
/* ===================================================
   MAIN.CSS — Shared design system for BlogBoard
   Theme: Deep Midnight — Studying & Reading Optimized
   =================================================== */

:root {
  /* Core Palette — Low-blue, eye-comfortable dark */
  --bg-deep: #0a0c14;
  --bg-surface: #0f1120;
  --bg-card: #131629;
  --bg-card-hover: #181d35;
  --bg-elevated: #1c2240;

  /* Accent Colors */
  --accent-primary: #7c6af7;
  --accent-primary-glow: rgba(124, 106, 247, 0.25);
  --accent-secondary: #4fc8b8;
  --accent-tertiary: #f7b96a;
  --accent-danger: #f76a6a;

  /* Text */
  --text-primary: #e8eaf6;
  --text-secondary: #9ba3c9;
  --text-muted: #5a637a;
  --text-accent: #a89cf7;

  /* Category Accent Colors */
  --cat-ml: #7c6af7;
  --cat-dl: #4fc8b8;
  --cat-nlp: #f7b96a;
  --cat-cv: #f76a6a;
  --cat-genai: #d06af7;
  --cat-ainews: #6ab4f7;
  --cat-statistics: #fb923c;

  /* Borders */
  --border: rgba(124, 106, 247, 0.12);
  --border-hover: rgba(124, 106, 247, 0.35);
  --border-card: rgba(255, 255, 255, 0.05);

  /* Typography */
  --font-sans: 'Inter', -apple-system, sans-serif;
  --font-serif: 'Playfair Display', Georgia, serif;
  --font-mono: 'Fira Code', 'Courier New', monospace;

  /* Spacing */
  --nav-height: 64px;
  --max-width: 1200px;
  --radius-sm: 6px;
  --radius-md: 12px;
  --radius-lg: 20px;
  --radius-xl: 28px;

  /* Shadows */
  --shadow-card: 0 4px 24px rgba(0, 0, 0, 0.4), 0 1px 4px rgba(0, 0, 0, 0.2);
  --shadow-glow: 0 0 40px rgba(124, 106, 247, 0.15);
  --shadow-nav: 0 1px 0 rgba(255, 255, 255, 0.05), 0 4px 24px rgba(0, 0, 0, 0.5);

  /* Transitions */
  --trans-fast: 0.15s ease;
  --trans-base: 0.25s ease;
  --trans-slow: 0.4s cubic-bezier(0.4, 0, 0.2, 1);
}

/* ── Reset & Base ── */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
  font-size: 16px;
}

body {
  background: var(--bg-deep);
  color: var(--text-primary);
  font-family: var(--font-sans);
  line-height: 1.6;
  min-height: 100vh;
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

a {
  color: inherit;
  text-decoration: none;
}

img {
  max-width: 100%;
  display: block;
}

/* ── Ambient Background ── */
.ambient-bg {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  overflow: hidden;
}

.orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.35;
  animation: orbDrift 20s ease-in-out infinite;
}

.orb-1 {
  width: 600px;
  height: 600px;
  background: radial-gradient(circle, #3b2a8f 0%, transparent 70%);
  top: -200px;
  left: -150px;
  animation-delay: 0s;
}

.orb-2 {
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, #1a5555 0%, transparent 70%);
  bottom: -100px;
  right: -100px;
  animation-delay: -7s;
}

.orb-3 {
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, #4a1a6e 0%, transparent 70%);
  top: 50%;
  right: 20%;
  animation-delay: -14s;
}

@keyframes orbDrift {

  0%,
  100% {
    transform: translate(0, 0) scale(1);
  }

  33% {
    transform: translate(30px, -30px) scale(1.05);
  }

  66% {
    transform: translate(-20px, 20px) scale(0.95);
  }
}

.grid-overlay {
  position: absolute;
  inset: 0;
  background-image:
    linear-gradient(rgba(124, 106, 247, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(124, 106, 247, 0.03) 1px, transparent 1px);
  background-size: 48px 48px;
}

#particleCanvas {
  position: absolute;
  inset: 0;
  width: 100%;
  height: 100%;
}

/* ── Navigation ── */
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  height: var(--nav-height);
  background: rgba(10, 12, 20, 0.8);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border-bottom: 1px solid var(--border-card);
  box-shadow: var(--shadow-nav);
  transition: background var(--trans-base);
}

.navbar.scrolled {
  background: rgba(10, 12, 20, 0.95);
}

.nav-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 0 24px;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 24px;
}

.nav-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: 1.2rem;
  letter-spacing: -0.02em;
  flex-shrink: 0;
}

.logo-icon {
  color: #03a57a;
  font-size: 1.4rem;
  line-height: 1;
}

.logo-text {
  color: var(--text-primary);
}

.logo-accent {
  color: var(--accent-primary);
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 4px;
  align-items: center;
}

.nav-link {
  padding: 6px 14px;
  border-radius: var(--radius-sm);
  font-size: 0.875rem;
  font-weight: 500;
  color: var(--text-secondary);
  transition: color var(--trans-fast), background var(--trans-fast);
}

.nav-link:hover,
.nav-link.active {
  color: var(--text-primary);
  background: rgba(124, 106, 247, 0.1);
}

.nav-link.active {
  color: var(--accent-primary);
}

/* Hamburger */
.hamburger {
  display: none;
  flex-direction: column;
  gap: 5px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 4px;
}

.hamburger span {
  display: block;
  width: 22px;
  height: 2px;
  background: var(--text-secondary);
  border-radius: 2px;
  transition: all var(--trans-base);
}

/* ── Buttons ── */
.btn-primary {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 28px;
  background: var(--accent-primary);
  color: white;
  font-weight: 600;
  font-size: 0.95rem;
  border-radius: var(--radius-md);
  border: none;
  cursor: pointer;
  transition: background var(--trans-fast), transform var(--trans-fast), box-shadow var(--trans-fast);
  box-shadow: 0 4px 20px rgba(124, 106, 247, 0.35);
}

.btn-primary:hover {
  background: #9178ff;
  transform: translateY(-1px);
  box-shadow: 0 8px 28px rgba(124, 106, 247, 0.45);
}

.btn-ghost {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 12px 24px;
  background: transparent;
  color: var(--text-secondary);
  font-weight: 500;
  font-size: 0.95rem;
  border-radius: var(--radius-md);
  border: 1px solid var(--border);
  cursor: pointer;
  transition: color var(--trans-fast), border-color var(--trans-fast), background var(--trans-fast);
}

.btn-ghost:hover {
  color: var(--text-primary);
  border-color: var(--border-hover);
  background: rgba(124, 106, 247, 0.06);
}

.btn-ghost-sm {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 8px 18px;
  background: transparent;
  color: var(--text-secondary);
  font-weight: 500;
  font-size: 0.85rem;
  border-radius: var(--radius-sm);
  border: 1px solid var(--border);
  cursor: pointer;
  transition: all var(--trans-fast);
}

.btn-ghost-sm:hover {
  color: var(--accent-primary);
  border-color: var(--border-hover);
}

/* ── Section Shared ── */
.section-header {
  text-align: center;
  margin-bottom: 56px;
}

.section-tag {
  display: inline-block;
  padding: 4px 14px;
  background: rgba(124, 106, 247, 0.12);
  color: var(--accent-primary);
  border-radius: 999px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  margin-bottom: 12px;
}

.section-title {
  font-family: var(--font-serif);
  font-size: clamp(2rem, 4vw, 2.8rem);
  color: var(--text-primary);
  line-height: 1.2;
  letter-spacing: -0.02em;
  margin-bottom: 12px;
}

.section-sub {
  font-size: 1rem;
  color: var(--text-secondary);
  max-width: 560px;
  margin: 0 auto;
  line-height: 1.7;
}

/* ── Gradient Text ── */
.gradient-text {
  background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

/* ── Loading Spinner ── */
.loading-spinner {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  padding: 60px 20px;
  color: var(--text-muted);
  font-size: 0.9rem;
}

.spinner {
  width: 36px;
  height: 36px;
  border: 3px solid rgba(124, 106, 247, 0.15);
  border-top-color: var(--accent-primary);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}

/* ── Footer ── */
.footer {
  position: relative;
  z-index: 10;
  margin-top: 80px;
  border-top: 1px solid var(--border-card);
  background: rgba(10, 12, 20, 0.8);
  backdrop-filter: blur(12px);
}

.footer-inner {
  max-width: var(--max-width);
  margin: 0 auto;
  padding: 48px 24px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  text-align: center;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: 1.1rem;
}

.footer-sub {
  color: var(--text-muted);
  font-size: 0.875rem;
}

.footer-cats {
  display: flex;
  gap: 20px;
  flex-wrap: wrap;
  justify-content: center;
}

.footer-cats a {
  color: var(--text-muted);
  font-size: 0.85rem;
  font-weight: 500;
  transition: color var(--trans-fast);
}

.footer-cats a:hover {
  color: var(--accent-primary);
}

.footer-copy {
  color: var(--text-muted);
  font-size: 0.8rem;
}

.footer-social {
  display: flex;
  gap: 16px;
  align-items: center;
  justify-content: center;
}

.social-link {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: rgba(124, 106, 247, 0.08);
  border: 1px solid var(--border-card);
  color: var(--text-muted);
  transition: color var(--trans-fast), background var(--trans-fast), border-color var(--trans-fast), transform var(--trans-fast);
}

.social-link:hover {
  color: var(--accent-primary);
  background: rgba(124, 106, 247, 0.15);
  border-color: var(--border-hover);
  transform: translateY(-2px);
}

/* ── Category Color Accents ── */
.accent-ml {
  --cat-color: var(--cat-ml);
}

.accent-dl {
  --cat-color: var(--cat-dl);
}

.accent-nlp {
  --cat-color: var(--cat-nlp);
}

.accent-cv {
  --cat-color: var(--cat-cv);
}

.accent-genai {
  --cat-color: var(--cat-genai);
}

.accent-ainews {
  --cat-color: var(--cat-ainews);
}

.accent-statistics {
  --cat-color: var(--cat-statistics);
}

/* ── Utility ── */
.hidden {
  display: none !important;
}

/* ── Responsive ── */
@media (max-width: 768px) {
  .nav-links {
    display: none;
    position: fixed;
    top: var(--nav-height);
    left: 0;
    right: 0;
    background: rgba(10, 12, 20, 0.98);
    backdrop-filter: blur(20px);
    flex-direction: column;
    padding: 20px 24px;
    gap: 4px;
    border-bottom: 1px solid var(--border-card);
  }

  .nav-links.open {
    display: flex;
  }

  .nav-link {
    padding: 10px 14px;
    width: 100%;
  }

  .hamburger {
    display: flex;
  }

  .hamburger.open span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
  }

  .hamburger.open span:nth-child(2) {
    opacity: 0;
  }

  .hamburger.open span:nth-child(3) {
    transform: rotate(-45deg) translate(5px, -5px);
  }
}
```

## File: `frontend/css/post.css`
```css
/* ===================================================
   POST.CSS — Blog post reader styles
   Reading-optimized typography and layout
   =================================================== */

/* ── Reading Progress Bar ── */
.reading-progress {
    position: fixed;
    top: 0;
    left: 0;
    height: 3px;
    background: linear-gradient(90deg, var(--accent-primary), var(--accent-secondary));
    z-index: 2000;
    width: 0%;
    transition: width 0.1s linear;
}

/* ── Post Layout ── */
.post-layout {
    position: relative;
    z-index: 10;
    max-width: 1320px;
    margin: 0 auto;
    padding: calc(var(--nav-height) + 48px) 24px 80px;
    display: grid;
    grid-template-columns: 1fr 280px;
    gap: 48px;
    align-items: flex-start;
}

/* ── Post Main ── */
.post-main {
    min-width: 0;
}

/* ── Breadcrumb ── */
.post-breadcrumb {
    display: flex;
    align-items: center;
    gap: 8px;
    margin-bottom: 32px;
    font-size: 0.85rem;
    color: var(--text-muted);
    flex-wrap: wrap;
}

.post-breadcrumb a {
    color: var(--text-muted);
    transition: color var(--trans-fast);
}

.post-breadcrumb a:hover {
    color: var(--accent-primary);
}

.post-breadcrumb span {
    color: var(--text-muted);
    opacity: 0.5;
}

/* ── Post Header ── */
.post-header {
    margin-bottom: 48px;
}

.post-meta-top {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 16px;
    flex-wrap: wrap;
}

.post-cat-badge {
    padding: 4px 14px;
    border-radius: 999px;
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.post-read-time {
    font-size: 0.82rem;
    color: var(--text-muted);
}

.post-title {
    font-family: var(--font-serif);
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    line-height: 1.2;
    letter-spacing: -0.02em;
    color: var(--text-primary);
    margin-bottom: 20px;
}

.post-meta-bottom {
    display: flex;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
}

.post-date {
    font-size: 0.85rem;
    font-family: var(--font-mono);
    color: var(--text-muted);
}

.post-divider {
    height: 1px;
    background: var(--border-card);
    margin-top: 28px;
}

/* ── Markdown Content ── */
.markdown-body {
    font-family: var(--font-sans);
    font-size: 1.05rem;
    line-height: 1.85;
    color: var(--text-secondary);
    max-width: 72ch;
}

.markdown-body h1,
.markdown-body h2,
.markdown-body h3,
.markdown-body h4,
.markdown-body h5,
.markdown-body h6 {
    font-family: var(--font-serif);
    color: var(--text-primary);
    line-height: 1.3;
    margin-top: 2em;
    margin-bottom: 0.6em;
    letter-spacing: -0.02em;
    scroll-margin-top: calc(var(--nav-height) + 20px);
}

.markdown-body h1 {
    font-size: 2rem;
}

.markdown-body h2 {
    font-size: 1.6rem;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--border-card);
}

.markdown-body h3 {
    font-size: 1.3rem;
}

.markdown-body h4 {
    font-size: 1.1rem;
    font-family: var(--font-sans);
    font-weight: 700;
}

.markdown-body h5,
.markdown-body h6 {
    font-size: 1rem;
    font-family: var(--font-sans);
    font-weight: 600;
}

.markdown-body p {
    margin-bottom: 1.4em;
}

.markdown-body strong {
    font-weight: 600;
    color: var(--text-primary);
}

.markdown-body em {
    font-style: italic;
    color: #c4bfed;
}

.markdown-body a {
    color: var(--accent-primary);
    text-decoration: underline;
    text-decoration-color: rgba(124, 106, 247, 0.35);
    transition: text-decoration-color var(--trans-fast), color var(--trans-fast);
}

.markdown-body a:hover {
    text-decoration-color: var(--accent-primary);
    color: #a89cf7;
}

.markdown-body ul,
.markdown-body ol {
    padding-left: 1.6em;
    margin-bottom: 1.4em;
}

.markdown-body li {
    margin-bottom: 0.4em;
}

.markdown-body ul li::marker {
    color: var(--accent-primary);
}

.markdown-body ol li::marker {
    color: var(--accent-primary);
    font-weight: 600;
}

/* Code inline */
.markdown-body code {
    font-family: var(--font-mono);
    font-size: 0.875em;
    background: rgba(124, 106, 247, 0.1);
    color: #b8adf7;
    padding: 2px 7px;
    border-radius: 4px;
    border: 1px solid rgba(124, 106, 247, 0.15);
}

/* Code blocks */
.markdown-body pre {
    background: #0d0f1a !important;
    border: 1px solid var(--border-card);
    border-radius: var(--radius-md);
    padding: 20px 24px;
    overflow-x: auto;
    margin-bottom: 1.6em;
    position: relative;
}

.markdown-body pre code {
    background: none;
    border: none;
    padding: 0;
    color: inherit;
    font-size: 0.9rem;
    line-height: 1.6;
}

/* Blockquotes */
.markdown-body blockquote {
    border-left: 3px solid var(--accent-primary);
    margin: 1.6em 0;
    padding: 12px 20px;
    background: rgba(124, 106, 247, 0.05);
    border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
    color: #b0b8d8;
    font-style: italic;
}

.markdown-body blockquote p {
    margin-bottom: 0;
}

/* Tables */
.markdown-body table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 1.6em;
    font-size: 0.9rem;
    overflow-x: auto;
    display: block;
}

.markdown-body th {
    background: rgba(124, 106, 247, 0.1);
    color: var(--text-primary);
    font-weight: 600;
    padding: 10px 14px;
    text-align: left;
    border: 1px solid var(--border);
}

.markdown-body td {
    padding: 9px 14px;
    border: 1px solid var(--border-card);
    color: var(--text-secondary);
}

.markdown-body tr:hover td {
    background: rgba(124, 106, 247, 0.04);
}

/* Images in markdown */
.markdown-body img {
    max-width: 100%;
    border-radius: var(--radius-md);
    margin: 1.6em 0;
    border: 1px solid var(--border-card);
}

/* HR */
.markdown-body hr {
    border: none;
    border-top: 1px solid var(--border-card);
    margin: 2.4em 0;
}

/* Task lists */
.markdown-body input[type="checkbox"] {
    margin-right: 8px;
    accent-color: var(--accent-primary);
}

/* ── Post Footer ── */
.post-footer {
    margin-top: 56px;
    padding-top: 24px;
    border-top: 1px solid var(--border-card);
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
}

.post-tags {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
}

.post-tag {
    padding: 4px 12px;
    border-radius: 999px;
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    font-size: 0.78rem;
    color: var(--text-muted);
}

.post-nav-btns {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
}

/* ── Sidebar / TOC ── */
.post-sidebar {
    position: sticky;
    top: calc(var(--nav-height) + 24px);
}

.toc-card {
    background: var(--bg-card);
    border: 1px solid var(--border-card);
    border-radius: var(--radius-lg);
    padding: 20px;
}

.toc-title {
    font-size: 0.75rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    color: var(--text-muted);
    margin-bottom: 12px;
}

.toc-nav {
    display: flex;
    flex-direction: column;
    gap: 2px;
}

.toc-link {
    display: block;
    padding: 5px 8px;
    border-radius: var(--radius-sm);
    font-size: 0.82rem;
    color: var(--text-muted);
    transition: color var(--trans-fast), background var(--trans-fast);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

.toc-link:hover {
    color: var(--text-primary);
    background: rgba(124, 106, 247, 0.08);
}

.toc-link.active {
    color: var(--accent-primary);
    background: rgba(124, 106, 247, 0.08);
}

.toc-link.level-h3 {
    padding-left: 20px;
    font-size: 0.78rem;
}

.toc-link.level-h4 {
    padding-left: 32px;
    font-size: 0.75rem;
}

.toc-empty {
    font-size: 0.82rem;
    color: var(--text-muted);
    font-style: italic;
}

/* ── Ambient subtle for post page ── */
.ambient-subtle .orb {
    opacity: 0.18;
}

/* ── Category badge colors ── */
.badge-ml {
    background: rgba(124, 106, 247, 0.15);
    color: var(--cat-ml);
}

.badge-dl {
    background: rgba(79, 200, 184, 0.15);
    color: var(--cat-dl);
}

.badge-nlp {
    background: rgba(247, 185, 106, 0.15);
    color: var(--cat-nlp);
}

.badge-cv {
    background: rgba(247, 106, 106, 0.15);
    color: var(--cat-cv);
}

.badge-genai {
    background: rgba(208, 106, 247, 0.15);
    color: var(--cat-genai);
}

.badge-ainews {
    background: rgba(106, 180, 247, 0.15);
    color: var(--cat-ainews);
}

/* ── Responsive ── */
@media (max-width: 1024px) {
    .post-layout {
        grid-template-columns: 1fr;
    }

    .post-sidebar {
        display: none;
    }
}

@media (max-width: 640px) {
    .post-title {
        font-size: 1.6rem;
    }

    .markdown-body {
        font-size: 0.97rem;
    }

    .post-footer {
        flex-direction: column;
        align-items: flex-start;
    }
}
```

## File: `frontend/js/blogs-data.js`
```javascript
/**
 * blogs-data.js — Dynamic Blog Registry
 *
 * Instead of hardcoded data, each category has its own articles.json
 * file at blogs/{domain}/articles.json, generated by the Python pipeline.
 *
 * articles.json entry shape:
 * {
 *   id: "blogs/ml/what-is-machine-learning.md",   ← relative path (also used as file)
 *   category: "ml",
 *   title: "...",
 *   description: "...",
 *   date: "YYYY-MM-DD",
 *   tags: ["tag1", "tag2"],
 *   readTime: "8 min",
 *   file: "blogs/ml/what-is-machine-learning.md"
 * }
 */

/* ── Category Metadata ─────────────────────────────────── */
const CATEGORY_META = {
  ml: {
    label: 'Machine Learning',
    shortLabel: 'ML',
    description: 'Algorithms, theory, and applied ML from fundamentals to production.',
    icon: '🧠',
    color: '#7c6af7',
    bgColor: 'rgba(124, 106, 247, 0.12)',
  },
  dl: {
    label: 'Deep Learning',
    shortLabel: 'DL',
    description: 'Neural networks, architectures, training tricks, and modern DL research.',
    icon: '🔬',
    color: '#4fc8b8',
    bgColor: 'rgba(79, 200, 184, 0.12)',
  },
  nlp: {
    label: 'Natural Language Processing',
    shortLabel: 'NLP',
    description: 'Text processing, transformers, LLMs, and language understanding.',
    icon: '📝',
    color: '#e879a0',
    bgColor: 'rgba(232, 121, 160, 0.12)',
  },
  cv: {
    label: 'Computer Vision',
    shortLabel: 'CV',
    description: 'Image processing, object detection, segmentation, and visual AI.',
    icon: '👁️',
    color: '#f59e0b',
    bgColor: 'rgba(245, 158, 11, 0.12)',
  },
  genai: {
    label: 'Generative AI',
    shortLabel: 'Gen AI',
    description: 'Diffusion models, LLMs, RAG, agents, and the frontier of AI generation.',
    icon: '✨',
    color: '#a78bfa',
    bgColor: 'rgba(167, 139, 250, 0.12)',
  },
  ainews: {
    label: 'AI News',
    shortLabel: 'AI News',
    description: 'Breaking developments, model releases, and industry analysis.',
    icon: '📡',
    color: '#34d399',
    bgColor: 'rgba(52, 211, 153, 0.12)',
  },
  statistics: {
    label: 'Statistics for AI',
    shortLabel: 'Stats',
    description: 'Probability, statistical tests, distributions, and the math behind ML.',
    icon: '📊',
    color: '#fb923c',
    bgColor: 'rgba(251, 146, 60, 0.12)',
  },
};

const ALL_CATEGORIES = ['ml', 'dl', 'nlp', 'cv', 'genai', 'ainews', 'statistics'];

/* ── Cache ─────────────────────────────────────────────── */
const _cache = {};

/* ── Core Fetch ────────────────────────────────────────── */
/**
 * Load articles.json for a category.
 * Returns [] if the file doesn't exist or fails to parse.
 */
async function loadCategoryArticles(cat) {
  if (_cache[cat] !== undefined) return _cache[cat];

  try {
    const res = await fetch(`blogs/${cat}/articles.json`);
    if (!res.ok) {
      _cache[cat] = [];
      return [];
    }
    const data = await res.json();
    _cache[cat] = Array.isArray(data) ? data : [];
    return _cache[cat];
  } catch (_) {
    _cache[cat] = [];
    return [];
  }
}

/**
 * Get articles for a category, sorted by sort order.
 * @param {string} cat  - category key
 * @param {string} sort - 'newest' | 'oldest'
 */
async function getBlogsByCategory(cat, sort = 'newest') {
  const articles = await loadCategoryArticles(cat);
  const sorted = [...articles].sort((a, b) =>
    sort === 'newest'
      ? new Date(b.date) - new Date(a.date)
      : new Date(a.date) - new Date(b.date)
  );
  return sorted;
}

/**
 * Get a single blog by its id (the relative path).
 * Searches all categories.
 */
async function getBlogById(id) {
  // Try to guess the category from the id path (blogs/{cat}/...)
  const parts = id.split('/');
  if (parts.length >= 2) {
    const cat = parts[1];
    if (CATEGORY_META[cat]) {
      const articles = await loadCategoryArticles(cat);
      const found = articles.find(a => a.id === id || a.file === id);
      if (found) return found;
    }
  }
  // Fallback: search all categories
  for (const cat of Object.keys(CATEGORY_META)) {
    const articles = await loadCategoryArticles(cat);
    const found = articles.find(a => a.id === id || a.file === id);
    if (found) return found;
  }
  return null;
}

/**
 * Get the N most recent articles across all main categories.
 */
async function getRecentBlogs(n = 6) {
  const all = await Promise.all(ALL_CATEGORIES.map(loadCategoryArticles));
  const flat = all.flat();
  flat.sort((a, b) => new Date(b.date) - new Date(a.date));
  return flat.slice(0, n);
}

/**
 * Get total article count across all categories.
 */
async function getTotalCount() {
  const all = await Promise.all(ALL_CATEGORIES.map(loadCategoryArticles));
  return all.reduce((sum, arr) => sum + arr.length, 0);
}

/* ── Formatting ─────────────────────────────────────────── */
function formatDate(dateStr) {
  if (!dateStr) return '';
  const [y, m, d] = dateStr.split('-').map(Number);
  return new Date(y, m - 1, d).toLocaleDateString('en-US', {
    year: 'numeric', month: 'long', day: 'numeric',
  });
}
```

## File: `frontend/js/category.js`
```javascript
/**
 * category.js — Category page logic
 * Reads category from hash (#cat=ml) and loads articles dynamically from articles.json.
 */
let currentSort = 'newest';
let searchTerm = '';
let catKey = '';
let cachedBlogs = [];

document.addEventListener('DOMContentLoaded', async () => {
    catKey = getHashParam('cat') || 'ml';
    initNav();
    applyCategoryTheme(catKey);
    await renderBlogList();

    // Search
    document.getElementById('searchInput')?.addEventListener('input', async e => {
        searchTerm = e.target.value.toLowerCase().trim();
        await renderBlogList();
    });

    // Hash change (nav link clicks between categories)
    window.addEventListener('hashchange', async () => {
        const newCat = getHashParam('cat') || 'ml';
        if (newCat !== catKey) {
            catKey = newCat;
            updateNavHighlight(catKey);
            applyCategoryTheme(catKey);
            cachedBlogs = [];
            searchTerm = '';
            const si = document.getElementById('searchInput');
            if (si) si.value = '';
            await renderBlogList();
        }
    });
});

/* ── Parse hash params ── */
function getHashParam(key) {
    const hash = window.location.hash.replace(/^#/, '');
    return new URLSearchParams(hash).get(key);
}

/* ── Nav ── */
function initNav() {
    const navbar = document.getElementById('navbar');
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    updateNavHighlight(catKey);

    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 30);
    });

    hamburger?.addEventListener('click', () => {
        hamburger.classList.toggle('open');
        navLinks.classList.toggle('open');
    });
}

function updateNavHighlight(cat) {
    document.querySelectorAll('.nav-link[data-cat]').forEach(link => {
        link.classList.toggle('active', link.getAttribute('data-cat') === cat);
    });
}

/* ── Domain schedule info ── */
const DOMAIN_SCHEDULE = {
    ml: { day: 'Monday', time: '8 AM IST' },
    dl: { day: 'Tuesday', time: '8 AM IST' },
    statistics: { day: 'Wednesday', time: '8 AM IST' },
    nlp: { day: 'Thursday', time: '8 AM IST' },
    cv: { day: 'Friday', time: '8 AM IST' },
    genai: { day: 'Saturday', time: '8 AM IST' },
    ainews: { day: 'Sunday', time: '8 AM IST' },
};

/* ── Sort ── */
function setSortOrder(order) {
    currentSort = order;
    document.getElementById('sortNewest')?.classList.toggle('active', order === 'newest');
    document.getElementById('sortOldest')?.classList.toggle('active', order === 'oldest');
    renderBlogList();
}

/* ── Apply Category Theme ── */
function applyCategoryTheme(cat) {
    const meta = CATEGORY_META[cat];
    if (!meta) return;

    document.body.className = document.body.className.replace(/theme-\w+/g, '');
    document.body.classList.add(`theme-${cat}`);
    document.title = `${meta.label} — BlogBoard`;

    const icon = document.getElementById('catHeroIcon');
    const badge = document.getElementById('catBadge');
    const title = document.getElementById('catHeroTitle');
    const desc = document.getElementById('catHeroDesc');
    const scheduleBadge = document.getElementById('catScheduleBadge');

    if (icon) icon.textContent = meta.icon;
    if (badge) { badge.textContent = meta.shortLabel; badge.style.background = meta.bgColor; badge.style.color = meta.color; }
    if (title) title.textContent = meta.label;
    if (desc) desc.textContent = meta.description;

    if (scheduleBadge) {
        const sched = DOMAIN_SCHEDULE[cat];
        if (sched && sched.day) {
            scheduleBadge.innerHTML = `
                <span class="sched-icon">🗓️</span>
                <span>Fresh articles drop every <strong>${sched.day}</strong> — live by <strong>${sched.time}</strong></span>
            `;
            scheduleBadge.style.display = 'flex';
        } else {
            scheduleBadge.innerHTML = `<span class="sched-icon">📡</span><span>Published as breaking news arrives</span>`;
            scheduleBadge.style.display = 'flex';
        }
    }
}

/* ── Render Blog List ── */
async function renderBlogList() {
    const listEl = document.getElementById('blogList');
    const emptyEl = document.getElementById('emptyState');
    const countEl = document.getElementById('catPostCount');
    if (!listEl) return;

    listEl.innerHTML = '<p style="color:var(--text-muted);padding:20px">Loading articles...</p>';

    let blogs = await getBlogsByCategory(catKey, currentSort);
    if (countEl) countEl.textContent = blogs.length;

    // Search filter
    if (searchTerm) {
        blogs = blogs.filter(b =>
            b.title.toLowerCase().includes(searchTerm) ||
            b.description.toLowerCase().includes(searchTerm) ||
            (b.tags || []).some(t => t.toLowerCase().includes(searchTerm))
        );
    }

    if (blogs.length === 0) {
        listEl.innerHTML = '';
        emptyEl?.classList.remove('hidden');
        return;
    }

    emptyEl?.classList.add('hidden');
    const meta = CATEGORY_META[catKey];

    listEl.innerHTML = blogs.map((blog, idx) => `
    <a href="post.html#id=${encodeURIComponent(blog.id)}" class="blog-item">
      <span class="blog-item-num">${String(idx + 1).padStart(2, '0')}</span>
      <div class="blog-item-body">
        <div class="blog-item-meta">
          <span class="blog-item-date">${formatDate(blog.date)}</span>
          ${(blog.tags || []).slice(0, 2).map(tag =>
        `<span class="blog-item-tag" style="background:${meta.bgColor};color:${meta.color}">#${tag}</span>`
    ).join('')}
        </div>
        <h2 class="blog-item-title">${escapeHtml(blog.title)}</h2>
        <p class="blog-item-desc">${escapeHtml(blog.description)}</p>
        <div class="blog-item-footer">
          <span class="read-time">📖 ${blog.readTime} read</span>
        </div>
      </div>
      <span class="blog-item-arrow">→</span>
    </a>
  `).join('');
}

function escapeHtml(str) {
    return (str || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}
```

## File: `frontend/js/home.js`
```javascript
/**
 * home.js — Home page logic
 * Uses async blogs-data.js to load articles dynamically.
 */
document.addEventListener('DOMContentLoaded', async () => {
    initNav();
    initParticles();
    await Promise.all([loadRecentPosts(), loadStats()]);
});

/* ── Nav ── */
function initNav() {
    const navbar = document.getElementById('navbar');
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 30);
    });

    hamburger?.addEventListener('click', () => {
        hamburger.classList.toggle('open');
        navLinks.classList.toggle('open');
    });
}

/* ── Stats Counter ── */
async function loadStats() {
    const total = await getTotalCount();
    animateCounter('totalBlogs', total);
    animateCounter('totalCategories', 6);
}

function animateCounter(id, target) {
    const container = document.getElementById(id);
    if (!container) return;
    const el = container.querySelector('.stat-num') || container;
    let current = 0;
    const step = Math.ceil(target / 40);
    const timer = setInterval(() => {
        current += step;
        if (current >= target) { current = target; clearInterval(timer); }
        el.textContent = current;
    }, 40);
}

/* ── Recent Posts ── */
async function loadRecentPosts() {
    const container = document.getElementById('recentPosts');
    if (!container) return;

    container.innerHTML = '<p style="color:var(--text-muted);padding:20px">Loading articles...</p>';

    const recents = await getRecentBlogs(6);

    if (recents.length === 0) {
        container.innerHTML = '<p style="color:var(--text-muted);padding:20px">No articles published yet. Check back soon!</p>';
        return;
    }

    container.innerHTML = recents.map(blog => {
        const meta = CATEGORY_META[blog.category];
        return `
    <a href="post.html#id=${encodeURIComponent(blog.id)}" class="recent-card">
      <div class="recent-card-meta">
        <span class="recent-cat-badge" style="background:${meta.bgColor};color:${meta.color}">
          ${meta.shortLabel}
        </span>
        <span class="recent-date">${formatDate(blog.date)}</span>
      </div>
      <h3 class="recent-title">${escapeHtml(blog.title)}</h3>
      <p class="recent-desc">${escapeHtml(blog.description)}</p>
      <span class="recent-readtime">📖 ${blog.readTime} read</span>
    </a>`;
    }).join('');
}

function escapeHtml(str) {
    return (str || '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/* ── Particle Background ─────────────────────────────── */
function initParticles() {
    const canvas = document.getElementById('particleCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    let W, H, particles = [];

    function resize() {
        W = canvas.width = canvas.offsetWidth;
        H = canvas.height = canvas.offsetHeight;
    }
    resize();
    window.addEventListener('resize', resize);

    const N = 60;
    for (let i = 0; i < N; i++) {
        particles.push({
            x: Math.random() * W, y: Math.random() * H,
            r: Math.random() * 1.5 + 0.5,
            vx: (Math.random() - 0.5) * 0.4,
            vy: (Math.random() - 0.5) * 0.4,
            a: Math.random() * 0.5 + 0.1,
        });
    }

    function draw() {
        ctx.clearRect(0, 0, W, H);
        particles.forEach(p => {
            p.x = (p.x + p.vx + W) % W;
            p.y = (p.y + p.vy + H) % H;

            ctx.beginPath();
            ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
            ctx.fillStyle = `rgba(124, 106, 247, ${p.a})`;
            ctx.fill();
        });

        // Draw connecting lines between nearby particles
        for (let i = 0; i < particles.length; i++) {
            for (let j = i + 1; j < particles.length; j++) {
                const dx = particles[i].x - particles[j].x;
                const dy = particles[i].y - particles[j].y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 100) {
                    ctx.beginPath();
                    ctx.moveTo(particles[i].x, particles[i].y);
                    ctx.lineTo(particles[j].x, particles[j].y);
                    ctx.strokeStyle = `rgba(124, 106, 247, ${0.12 * (1 - dist / 100)})`;
                    ctx.lineWidth = 0.5;
                    ctx.stroke();
                }
            }
        }
        requestAnimationFrame(draw);
    }
    draw();
}
```

## File: `frontend/js/post.js`
```javascript
/**
 * post.js — Blog post viewer with markdown rendering
 * Uses window.location.hash (#id=...) to avoid server stripping query params
 */
document.addEventListener('DOMContentLoaded', () => {
    initNav();
    loadPost();
    initReadingProgress();
});

/* ── Parse hash params ── */
function getHashParam(key) {
    // Supports formats: #id=foo  OR  #cat=ml&id=foo
    const hash = window.location.hash.replace(/^#/, '');
    const params = new URLSearchParams(hash);
    return params.get(key);
}

/* ── Nav ── */
function initNav() {
    const navbar = document.getElementById('navbar');
    const hamburger = document.getElementById('hamburger');
    const navLinks = document.getElementById('navLinks');

    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 30);
    });

    hamburger?.addEventListener('click', () => {
        hamburger.classList.toggle('open');
        navLinks.classList.toggle('open');
    });
}

/* ── Reading Progress ── */
function initReadingProgress() {
    const bar = document.getElementById('readingProgress');
    if (!bar) return;
    window.addEventListener('scroll', () => {
        const doc = document.documentElement;
        const scrollTop = doc.scrollTop || document.body.scrollTop;
        const scrollHeight = doc.scrollHeight - doc.clientHeight;
        bar.style.width = scrollHeight > 0 ? `${(scrollTop / scrollHeight) * 100}%` : '0%';
    });
}

/* ── Load Post ── */
async function loadPost() {
    // Read id from hash: post.html#id=blogs/ml/intro-to-ml.md
    const rawId = getHashParam('id');
    const id = rawId ? decodeURIComponent(rawId) : null;
    const contentEl = document.getElementById('postContent');

    if (!id) {
        // No id in hash — redirect to home
        window.location.replace('index.html');
        return;
    }

    const blog = await getBlogById(id);
    if (!blog) {
        showError('Post not found. It may have been removed or the link is incorrect.', contentEl);
        return;
    }
    const meta = CATEGORY_META[blog.category];

    // Set page title
    document.title = `${blog.title} — BlogBoard`;

    // Breadcrumb
    const catLink = document.getElementById('catLink');
    if (catLink) {
        catLink.textContent = meta.label;
        catLink.href = `category.html#cat=${blog.category}`;
    }
    const postTitleSpan = document.getElementById('postTitle');
    if (postTitleSpan) postTitleSpan.textContent = blog.title;

    // Header
    document.getElementById('postTitleH1').textContent = blog.title;
    document.getElementById('postDate').textContent = formatDate(blog.date);

    const catBadge = document.getElementById('postCatBadge');
    if (catBadge) {
        catBadge.textContent = meta.shortLabel;
        catBadge.className = `post-cat-badge badge-${blog.category}`;
    }

    const readTimeEl = document.getElementById('postReadTime');
    if (readTimeEl) readTimeEl.textContent = `📖 ${blog.readTime} read`;

    // Active nav link
    document.querySelectorAll('.nav-link[href]').forEach(link => {
        if (link.href.includes(`cat=${blog.category}`)) link.classList.add('active');
    });

    // Back link
    const backBtn = document.getElementById('backToCat');
    if (backBtn) {
        backBtn.href = `category.html#cat=${blog.category}`;
        backBtn.textContent = `← Back to ${meta.shortLabel}`;
    }

    // Tags
    const tagsEl = document.getElementById('postTags');
    if (tagsEl && blog.tags?.length) {
        tagsEl.innerHTML = blog.tags.map(t =>
            `<span class="post-tag">#${t}</span>`
        ).join('');
    }

    // Fetch and render markdown
    try {
        const response = await fetch(blog.file);
        if (!response.ok) throw new Error(`HTTP ${response.status}`);

        const mdText = await response.text();
        renderMarkdown(mdText, contentEl);
        buildTOC();
    } catch (err) {
        showError(
            `Could not load the article file.<br>
       <small>Expected: <code>${blog.file}</code></small><br>
       <small>Make sure you are running this through a local server (e.g. <code>npx serve</code>), not by opening the HTML file directly.</small>`,
            contentEl
        );
        console.error('Failed to load blog post:', err);
    }
}

/* ── Render Markdown ── */
function renderMarkdown(mdText, container) {
    marked.setOptions({
        gfm: true,
        breaks: true,
    });

    // Add IDs to headings for TOC
    const renderer = new marked.Renderer();
    renderer.heading = (text, level) => {
        const escapedText = (typeof text === 'object' ? text.text : text)
            .toLowerCase().replace(/[^\w]+/g, '-');
        const rawText = typeof text === 'object' ? text.text : text;
        return `<h${level} id="${escapedText}">${rawText}</h${level}>`;
    };

    container.innerHTML = marked.parse(mdText, { renderer });

    // Syntax highlight all code blocks
    if (window.hljs) {
        container.querySelectorAll('pre code').forEach(block => {
            hljs.highlightElement(block);
        });
    }

    // Make code blocks copy-able
    container.querySelectorAll('pre').forEach(pre => {
        const btn = document.createElement('button');
        btn.className = 'copy-btn';
        btn.textContent = 'Copy';
        btn.style.cssText = `
      position:absolute; top:10px; right:12px;
      background:rgba(124,106,247,0.15); color:#a89cf7;
      border:1px solid rgba(124,106,247,0.25); border-radius:6px;
      padding:3px 10px; font-size:0.75rem; cursor:pointer;
      font-family:var(--font-sans); transition:all 0.15s;
    `;
        btn.addEventListener('click', () => {
            const code = pre.querySelector('code');
            navigator.clipboard.writeText(code?.textContent || '').then(() => {
                btn.textContent = 'Copied!';
                setTimeout(() => btn.textContent = 'Copy', 2000);
            });
        });
        pre.style.position = 'relative';
        pre.appendChild(btn);
    });
}

/* ── Build Table of Contents ── */
function buildTOC() {
    const content = document.getElementById('postContent');
    const tocNav = document.getElementById('tocNav');
    if (!content || !tocNav) return;

    const headings = content.querySelectorAll('h2, h3, h4');
    if (headings.length === 0) return;

    tocNav.innerHTML = '';

    const observer = new IntersectionObserver(entries => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                tocNav.querySelectorAll('.toc-link').forEach(l => l.classList.remove('active'));
                const activeLink = tocNav.querySelector(`[data-target="${entry.target.id}"]`);
                activeLink?.classList.add('active');
            }
        });
    }, { rootMargin: '-20% 0px -70% 0px' });

    headings.forEach(h => {
        const level = h.tagName.toLowerCase();
        const link = document.createElement('a');
        link.href = `#${h.id}`;
        link.setAttribute('data-target', h.id);
        link.textContent = h.textContent;
        link.className = `toc-link level-${level}`;
        link.addEventListener('click', e => {
            e.preventDefault();
            document.getElementById(h.id)?.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
        tocNav.appendChild(link);
        observer.observe(h);
    });
}

/* ── Error State ── */
function showError(message, container) {
    if (!container) return;
    container.innerHTML = `
    <div style="padding:40px;text-align:center;color:var(--text-muted)">
      <div style="font-size:2.5rem;margin-bottom:16px">⚠️</div>
      <h3 style="color:var(--text-secondary);margin-bottom:12px">Unable to load article</h3>
      <p style="line-height:1.7">${message}</p>
    </div>`;
}
```

