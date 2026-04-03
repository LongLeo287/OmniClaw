---
id: babyagi-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:56.357234
---

# KNOWLEDGE EXTRACT: babyagi
> **Extracted on:** 2026-03-30 13:53:04
> **Source:** babyagi

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
brain/knowledge/docs_legacy/_build/

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

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/brain/knowledge/docs_legacy/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/#use-with-ide
.pdm.toml

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

# Custom ignores
funztionz.db
encryption_key.json
```

## File: `.replit`
```
entrypoint = "main.py"
modules = ["python-3.11"]

[nix]
channel = "stable-24_05"

[unitTest]
language = "python3"

[gitHubImport]
requiredFiles = [".replit", "replit.nix"]

[deployment]
run = ["python3", "main.py"]
deploymentTarget = "cloudrun"

[[ports]]
localPort = 5000
externalPort = 5000

[[ports]]
localPort = 8000
externalPort = 8000

[[ports]]
localPort = 8080
externalPort = 80
```

## File: `CNAME`
```
babyagi.org
```

## File: `CODE_READINESS_ANALYSIS.md`
```markdown
# BabyAGI Code Readiness Analysis

**Analysis Date:** January 2026
**Repository:** yoheinakajima/babyagi
**Verdict:** **NOT PRODUCTION READY**

---

## Executive Summary

BabyAGI is an experimental self-building autonomous agent framework built on a custom "functionz" function management system. **The author explicitly states this is not meant for production use**, and this analysis confirms that assessment. While the project demonstrates innovative ideas around self-building agents, it has significant issues that must be addressed before recommending it for general use.

### Quick Assessment

| Category | Score | Status |
|----------|-------|--------|
| Security | 2/10 | **Critical Issues** |
| Testing | 0/10 | **No Tests** |
| Documentation | 4.5/10 | **Moderate** |
| Error Handling | 6.5/10 | **Mixed** |
| Dependencies | 3/10 | **Poor** |
| Code Quality | 5/10 | **Experimental** |
| **Overall Readiness** | **3/10** | **Not Ready** |

---

## 1. Project Overview

### What is BabyAGI?

BabyAGI is an experimental framework for a self-building autonomous agent. The core philosophy is that "the optimal way to build a general autonomous agent is to build the simplest thing that can build itself."

**Key Components:**
- **Functionz Framework**: Core engine for storing, managing, and executing functions from a database
- **Flask Dashboard**: Web UI for function management, monitoring, and logs
- **REST API**: Endpoints for programmatic function management
- **Function Packs**: Pre-built function libraries (default, drafts, plugins)
- **Self-Building Agents**: Experimental features for AI-powered function generation

### Author's Own Assessment

From the README:
> *"This is a framework built by Yohei who has never held a job as a developer. The purpose of this repo is to share ideas and spark discussion and for experienced devs to play with. **Not meant for production use**. Use with caution."*

---

## 2. Critical Issues Requiring Immediate Attention

### 2.1 Security Vulnerabilities

#### CRITICAL: Arbitrary Code Execution (RCE)

**Location:** `babyagi/functionz/core/execution.py:44, 122`

The framework uses `exec()` to execute function code stored in the database without any sandboxing or validation:

```python
exec(function_version['code'], local_scope)
```

**Risk:** Anyone who can write to the database can execute arbitrary code on the host system.

#### CRITICAL: SQL Injection

**Location:** `babyagi/functionz/packs/drafts/user_db.py:251`

Raw SQL is constructed using f-strings:

```python
alter_stmt = f'ALTER TABLE {table_name} ADD COLUMN {new_column.name} {new_column.type}'
user_db.engine.execute(alter_stmt)
```

**Risk:** Complete database compromise through malicious table names.

#### CRITICAL: Encryption Key Exposure

**Location:** `babyagi/functionz/db/models.py:28`

The encryption key is printed to stdout/logs:

```python
print(f"Using encryption key: {ENCRYPTION_KEY}")
```

**Risk:** All encrypted secrets can be decrypted if logs are accessible.

#### HIGH: Secrets Injection Without Scoping

**Location:** `babyagi/functionz/core/execution.py:158-162`

ALL stored secret keys are injected into every function's execution scope:

```python
local_scope.update(secret_keys)  # All secrets available to any function
```

**Risk:** Any function can access all stored credentials.

### 2.2 No Test Coverage

**Finding:** Zero tests exist in the entire codebase.

- No `test_*.py` files
- No `tests/` directory
- No pytest, unittest, or any test framework configured
- No CI/CD pipeline

**Impact:** No automated verification that the code works correctly. Any change could introduce regressions without detection.

### 2.3 Dependency Management Chaos

**Finding:** Three conflicting dependency systems:

1. `requirements.txt` (pip)
2. `pyproject.toml` (Poetry)
3. `setup.py` (setuptools)

**Critical Problems:**
- `poetry.lock` only tracks 11 packages; core dependencies like SQLAlchemy, cryptography, scikit-learn are missing
- Four critical packages have NO version constraints: `cryptography`, `scikit-learn`, `litellm`, `openai`
- Version conflicts: setup.py says Python >=3.6, pyproject.toml says >=3.10.0,<3.12
- Package versions out of sync (setup.py: 0.1.2, pyproject.toml: 0.0.8)

---

## 3. Complete Issue Inventory

### Security Issues (16 found)

| Severity | Issue | Location |
|----------|-------|----------|
| CRITICAL | Arbitrary code execution via exec() | execution.py:44,122 |
| CRITICAL | SQL injection vulnerability | user_db.py:251 |
| CRITICAL | Encryption key printed to logs | models.py:28 |
| CRITICAL | Plaintext encryption key file | models.py:15-20 |
| HIGH | All secrets injected to all functions | execution.py:158-162 |
| HIGH | Unvalidated pip install of packages | execution.py:19 |
| HIGH | Insufficient input validation | execution.py:170-174 |
| HIGH | Weak secret storage mechanism | local_db.py:235-259 |
| MEDIUM | Debug logging of secret operations | local_db.py:236-244 |
| MEDIUM | Database file permissions unset | local_db.py:14 |
| MEDIUM | No CSRF protection | api/__init__.py |
| MEDIUM | No rate limiting | api/__init__.py |
| MEDIUM | Unvalidated dynamic imports | execution.py:32-35 |
| MEDIUM | Duplicate method definitions | local_db.py:235,248 |
| LOW | No timeout on code execution | execution.py:55-141 |
| LOW | No authentication on API/dashboard | Multiple files |

### Code Quality Issues

| Issue | Location | Impact |
|-------|----------|--------|
| Silent exception suppression | `__init__.py:122-123` | Errors hidden from users |
| print() instead of logging | Multiple files | Inconsistent logging |
| No custom exception classes | Entire codebase | Poor error semantics |
| Extensive DEBUG print statements | drafts/*.py | Development code in repo |

### Incomplete/Experimental Features

The `drafts/` directory contains experimental features explicitly marked as incomplete:

- `generate_function.py` - 674 lines with 26+ DEBUG statements
- `self_build.py` / `self_build2.py` - Self-building agent experiments
- `choose_or_create_function.py` - Function selection logic
- `react_agent.py` - ReAct agent implementation

From README: *"These draft features are experimental concepts and may not function as intended. They require significant improvements and should be used with caution."*

---

## 4. Documentation Assessment

### Strengths
- Well-structured README with clear quick start
- Good examples in `examples/` directory
- Progressive complexity from basic to advanced features
- Clear warnings about experimental status

### Gaps
- No API documentation (no OpenAPI/Swagger spec)
- Limited docstrings (56% coverage, but minimal Args/Returns)
- No architecture documentation
- No troubleshooting guide
- No generated documentation (Sphinx, MkDocs, etc.)

**Score: 4.5/10**

---

## 5. Error Handling Assessment

### Strengths
- No bare `except:` clauses - good practice
- Widespread try/except coverage in API layer
- Proper re-raising in critical execution paths
- Good logging in API/dashboard modules

### Weaknesses
- Silent exception suppression in `__init__.py` (lines 54-56, 122-123)
- Inconsistent use of print() vs logging module
- No custom exception classes
- Encryption failures silently return None

**Score: 6.5/10**

---

## 6. Architecture Assessment

### Strengths
- Clean modular structure (core, db, api, dashboard, packs)
- Separation of concerns between components
- Decorator-based registration pattern
- Versioning system for functions
- Trigger-based automation capability

### Concerns
- Global singleton pattern for Functionz instance
- Tight coupling between execution engine and database
- Dynamic `exec()` of database code is inherently risky
- No sandboxing or isolation of function execution

---

## 7. Recommendations for Production Readiness

### Must Fix Before Any Use

1. **Remove exec() or add sandboxing** - Consider using RestrictedPython or containerized execution
2. **Fix SQL injection** - Use parameterized queries exclusively
3. **Stop logging encryption key** - Remove the print statement immediately
4. **Add scope-based secret injection** - Only inject secrets required by each function
5. **Add authentication** - Protect API and dashboard endpoints
6. **Add test suite** - Minimum 80% coverage on core components

### Should Fix

6. **Consolidate dependency management** - Pick one system (recommend Poetry)
7. **Pin all dependencies** - Especially security-critical packages
8. **Replace print() with logging** - Consistent logging configuration
9. **Add custom exceptions** - Improve error semantics
10. **Add input validation** - Type and value validation on all inputs

### Nice to Have

11. **Add API documentation** - OpenAPI/Swagger specification
12. **Set up CI/CD** - Automated testing and security scanning
13. **Add execution timeouts** - Prevent infinite loops
14. **Add rate limiting** - Prevent abuse
15. **Document architecture** - Help contributors understand the system

---

## 8. Conclusion

**BabyAGI is an interesting experimental project that demonstrates innovative ideas about self-building autonomous agents.** However, it has critical security vulnerabilities, no tests, and dependency management issues that make it unsuitable for any production use or recommendation to others.

### Who Should Use This?

- **Researchers** exploring self-building agent concepts
- **Experienced developers** who can identify and work around the issues
- **Contributors** who want to help improve the framework

### Who Should NOT Use This?

- Anyone building production systems
- Developers who need reliable, tested code
- Projects that require security compliance
- Teams without security expertise to mitigate the risks

### Bottom Line

The author is transparent about the experimental nature of this project. **Respect that warning.** If you want to experiment with the concepts, understand that you're working with early-stage research code that has significant issues. If you need a production-ready agent framework, look elsewhere or contribute to making BabyAGI production-ready.

---

## Appendix: Files Reviewed

### Core Framework
- `babyagi/__init__.py` (140 lines)
- `babyagi/functionz/core/framework.py` (149 lines)
- `babyagi/functionz/core/execution.py` (254 lines)
- `babyagi/functionz/core/registration.py` (266 lines)

### Database Layer
- `babyagi/functionz/db/base_db.py` (62 lines)
- `babyagi/functionz/db/local_db.py` (259 lines)
- `babyagi/functionz/db/db_router.py` (301 lines)
- `babyagi/functionz/db/models.py` (~130 lines)

### API/Dashboard
- `babyagi/api/__init__.py` (158 lines)
- `babyagi/dashboard/__init__.py` (132 lines)

### Function Packs
- `babyagi/functionz/packs/default/*.py`
- `babyagi/functionz/packs/drafts/*.py`
- `babyagi/functionz/packs/plugins/*.py`

### Configuration
- `requirements.txt`
- `pyproject.toml`
- `setup.py`
- `poetry.lock`
- `README.md`
```

## File: `main.py`
```python
import babyagi
import os


app = babyagi.create_app('/dashboard')

# Add OpenAI key to enable automated descriptions and embedding of functions.
babyagi.add_key_wrapper('openai_api_key',os.environ['OPENAI_API_KEY'])


@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for BabyAGI dashboard."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

## File: `MANIFEST.in`
```
# Include the README and LICENSE
include README.md
include LICENSE

# Include all package directories and their contents
recursive-include babyagi *

# Include examples
recursive-include examples *

# Exclude specific sensitive or unwanted files
exclude encryption_key.json
exclude funztionz.db

# Exclude other unnecessary files
global-exclude *.pyc
global-exclude __pycache__/

# Exclude .git and .gitignore
global-exclude .git
global-exclude .gitignore

# Exclude .egg-info directory and files
global-exclude *.egg-info
global-exclude *.egg-info/*
```

## File: `pyproject.toml`
```
[tool.poetry]
name = "babyagi"
version = "0.0.8"
description = ""
authors = ["Your Name <you@example.com>"]

[tool.poetry.dependencies]
python = ">=3.10.0,<3.12"
db = "^0.1.1"
flask = "^3.0.3"
werkzeug = "^3.0.4"
setuptools = "^75.1.0"

[tool.pyright]
# https://github.com/microsoft/pyright/blob/main/brain/knowledge/docs_legacy/configuration.md
useLibraryCodeForTypes = true
exclude = [".cache"]

[tool.ruff]
# https://beta.ruff.rs/brain/knowledge/docs_legacy/configuration/
select = ['E', 'W', 'F', 'I', 'B', 'C4', 'ARG', 'SIM']
ignore = ['W291', 'W292', 'W293']

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

## File: `README.md`
```markdown
# BabyAGI

> [!NOTE]
> The original BabyAGI from March 2023 introduced task planning as a method for developing autonomous agents. This project has been archived and moved to the [babyagi_archive](https://github.com/yoheinakajima/babyagi_archive) repo (September 2024 snapshot).

> [!CAUTION]
> This is a framework built by Yohei who has never held a job as a developer. The purpose of this repo is to share ideas and spark discussion and for experienced devs to play with. Not meant for production use. Use with cautioun.

---

This newest BabyAGI is an experimental framework for a self-building autonomous agent. Earlier efforts to expand BabyAGI have made it clear that the optimal way to build a general autonomous agent is to build the simplest thing that can build itself.

Check out [this introductory X/Twitter thread](https://x.com/yoheinakajima/status/1840678823681282228) for a simple overview.

The core is a new function framework (**functionz**) for storing, managing, and executing functions from a database. It offers a graph-based structure for tracking imports, dependent functions, and authentication secrets, with automatic loading and comprehensive logging capabilities. Additionally, it comes with a dashboard for managing functions, running updates, and viewing logs.

## Table of Contents

- [Quick Start](#quick-start)
- [Basic Usage](#basic-usage)
- [Function Metadata](#function-metadata)
- [Function Loading](#function-loading)
- [Key Dependencies](#key-dependencies)
- [Execution Environment](#execution-environment)
  - [Log](#log)
- [Dashboard](#dashboard)
- [Pre-loaded Functions](#pre-loaded-functions)
- [Future/Draft Features](#futuredraft-features)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Quick Start

To quickly check out the dashboard and see how it works:

1. **Install BabyAGI:**

    ```bash
    pip install babyagi
    ```

2. **Import BabyAGI and load the dashboard:**

    ```python
    import babyagi

    if __name__ == "__main__":
        app = babyagi.create_app('/dashboard')
        app.run(host='0.0.0.0', port=8080)
    ```

3. **Navigate to the dashboard:**

    Open your browser and go to `http://localhost:8080/dashboard` to access the BabyAGI dashboard.
    
## Basic Usage

Start by importing `babyagi` and registering your functions. Here's how to register two functions, where one depends on the other:

```python
import babyagi

# Register a simple function
@babyagi.register_function()
def world():
    return "world"

# Register a function that depends on 'world'
@babyagi.register_function(dependencies=["world"])
def hello_world():
    x = world()
    return f"Hello {x}!"

# Execute the function
print(babyagi.hello_world())  # Output: Hello world!

if __name__ == "__main__":
    app = babyagi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
```

## Function Metadata

Functions can be registered with metadata to enhance their capabilities and manage their relationships. Here's a more comprehensive example of function metadata, showing logical usage of all fields:

```python
import babyagi

@babyagi.register_function(
    imports=["math"],
    dependencies=["circle_area"],
    key_dependencies=["openai_api_key"],
    metadata={
        "description": "Calculates the volume of a cylinder using the circle_area function."
    }
)
def cylinder_volume(radius, height):
    import math
    area = circle_area(radius)
    return area * height
```

**Available Metadata Fields:**

- `imports`: List of external libraries the function depends on.
- `dependencies`: List of other functions this function depends on.
- `key_dependencies`: List of secret keys required by the function.
- `metadata["description"]`: A description of what the function does.

## Function Loading

In addition to using `register_function`, you can use `load_function` to load plugins or draft packs of functions. BabyAGI comes with built-in function packs, or you can load your own packs by pointing to the file path.

You can find available function packs in `babyagi/functionz/packs`.

**Loading Custom Function Packs:**

```python
import babyagi

# Load your custom function pack
babyagi.load_functions("path/to/your/custom_functions.py")
```

This approach makes function building and management easier by organizing related functions into packs.

## Key Dependencies

You can store `key_dependencies` directly from your code or manage them via the dashboard.

**Storing Key Dependencies from Code:**

```python
import babyagi

# Add a secret key
babyagi.add_key_wrapper('openai_api_key', 'your_openai_api_key')
```

**Adding Key Dependencies via Dashboard:**

Navigate to the dashboard and use the **add_key_wrapper** feature to securely add your secret keys.

## Execution Environment

BabyAGI automatically loads essential function packs and manages their dependencies, ensuring a seamless execution environment. Additionally, it logs all activities, including the relationships between functions, to provide comprehensive tracking of function executions and dependencies.

### Log

BabyAGI implements a comprehensive logging system to track all function executions and their interactions. The logging mechanism ensures that every function call, including its inputs, outputs, execution time, and any errors, is recorded for monitoring and debugging purposes.

**Key Logging Features:**

- **Execution Tracking:** Logs when a function starts and finishes execution, including the function name, arguments, keyword arguments, and execution time.
  
- **Error Logging:** Captures and logs any errors that occur during function execution, providing detailed error messages for troubleshooting.

- **Dependency Management:** Automatically resolves and logs dependencies between functions, ensuring that all required functions and libraries are loaded before execution.

- **Trigger Logging:** Logs the execution of triggered functions, detailing which functions were triggered by others and their respective execution outcomes.

- **Comprehensive Records:** Maintains a history of all function executions, enabling users to review past activities, understand function relationships, and analyze performance metrics.

**How Triggers Work:**

Triggers are mechanisms that allow certain functions to be automatically executed in response to specific events or actions within the system. For example, when a function is added or updated, a trigger can initiate the generation of a description for that function.

Triggers enhance the autonomy of BabyAGI by enabling automated workflows and reducing the need for manual intervention. However, it's essential to manage triggers carefully to avoid unintended recursive executions or conflicts between dependent functions.

## Dashboard

The BabyAGI dashboard offers a user-friendly interface for managing functions, monitoring executions, and handling configurations. Key features include:

- **Function Management:** Register, deregister, and update functions directly from the dashboard.

- **Dependency Visualization:** View and manage dependencies between functions to understand their relationships.

- **Secret Key Management:** Add and manage secret keys securely through the dashboard interface.

- **Logging and Monitoring:** Access comprehensive logs of function executions, including inputs, outputs, and execution times.

- **Trigger Management:** Set up triggers to automate function executions based on specific events or conditions.

**Accessing the Dashboard:**

After running your application, navigate to `http://localhost:8080/dashboard` to access the BabyAGI dashboard.
## Pre-loaded Functions Summary

BabyAGI includes two pre-loaded function packs:

1. **Default Functions (`packs/default_functions.py`):**
   - **Function Execution:** Run, add, update, or retrieve functions and versions.
   - **Key Management:** Add and retrieve secret keys.
   - **Triggers:** Add triggers to execute functions based on others.
   - **Logs:** Retrieve logs with optional filters.

2. **AI Functions (`packs/ai_generator.py`):**
   - **AI Description & Embeddings:** Auto-generate descriptions and embeddings for functions.
   - **Function Selection:** Find or choose similar functions based on prompts.

## Running a Self-Building Agent

BabyAGI includes two experimental self-building agents, showcasing how the framework can help a self-building coding agent leverage existing functions to write new ones.

### 1. `process_user_input` in the `code_writing_functions` pack

This function first determines whether to use an existing function or generate new ones. If new functions are needed, it breaks them down into smaller reusable components and combines them into a final function.

Try this:

~~~python
import babyagi

babyagi.add_key_wrapper('openai_api_key', os.environ['OPENAI_API_KEY'])
babyagi.load_functions("drafts/code_writing_functions")

babyagi.process_user_input("Grab today's score from ESPN and email it to test@test.com")
~~~

When you run this, you will see the functions being generated in the shell and new functions will be available in the dashboard once completed.

### 2. `self_build` in the `self_build` pack

This function takes a user description and generates X distinct tasks that a user might ask an AI assistant. Each task is processed by `process_user_input`, creating new functions if no existing ones suffice.

Try this:

~~~python
import babyagi

babyagi.add_key_wrapper('openai_api_key', os.environ['OPENAI_API_KEY'])
babyagi.load_functions("drafts/code_writing_functions")
babyagi.load_functions("drafts/self_build")

babyagi.self_build("A sales person at an enterprise SaaS company.", 3)
~~~

This will generate 3 distinct tasks a salesperson might ask an AI assistant and create functions to handle those.

*The functions will be generated and stored in the dashboard, but note that the generated code is minimal and may need improvement.

![alt text](https://github.com/yoheinakajima/babyagi_staging/blob/main/self_build.png?raw=true)



**Warning:** These draft features are experimental concepts and may not function as intended. They require significant improvements and should be used with caution.


## Contributing

Contributions are greatly appreciatedly, but candidly I have not been great at managing PRs. Please be patient as things will move slow while I am working on this alone (on nights and weekends). I may start by building a small core crew before collaborating with a larger group.

If you are a dev, investor, friend of open-source and interesting supporting AI work I do, please fill [this form](https://forms.gle/UZLyT75HQULr8XNUA) (I have a few fun initiatives coming up!)

## License

BabyAGI is released under the MIT License. See the [LICENSE](LICENSE) file for more details.
```

## File: `requirements.txt`
```
Flask>=2.0.0
sqlalchemy>=1.4,<2.0
cryptography
scikit-learn
litellm
openai
```

## File: `setup.py`
```python
from setuptools import setup, find_packages
import os

# Read the long description from README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read requirements from requirements.txt
def parse_requirements(filename):
    with open(filename, "r") as f:
        lines = f.readlines()
    # Remove comments and empty lines
    return [line.strip() for line in lines if line.strip() and not line.startswith("#")]

setup(
    name="babyagi",  # Ensure this is the desired package name
    version="0.1.2",  # Update this version appropriately
    author="Yohei Nakajima",
    author_email="babyagi@untapped.vc",
    description="An experimental prototype framework for building self building autonomous agents.",
    long_description=  long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yoheinakajima/babyagi",  # Update if necessary
    packages=find_packages(),
    include_package_data=True,  # Include package data as specified in MANIFEST.in
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=parse_requirements("requirements.txt"),
    entry_points={
        'console_scripts': [
            'babyagi=babyagi.main:main',  # Example entry point
        ],
    },
    keywords="AGI, AI, Framework, Baby AGI",
    project_urls={  # Optional
        "Author": "https://x.com/yoheinakajima",
    },
)
```

## File: `babyagi/__init__.py`
```python
# babyagi/__init__.py

from flask import Flask, g
from .functionz.core.framework import Functionz
from .dashboard import create_dashboard
from .api import create_api_blueprint
import os
import importlib.util
import traceback
import sys

# Singleton instance of the functionz framework
_func_instance = Functionz()


def get_func_instance():
    return _func_instance

def create_app(dashboard_route='/dashboard'):
    app = Flask(__name__)

    # Remove leading slash if present to avoid double slashes
    if dashboard_route.startswith('/'):
        dashboard_route = dashboard_route[1:]

    # Create and register the dashboard blueprint with dashboard_route
    dashboard_blueprint = create_dashboard(_func_instance, dashboard_route)

    # Create and register the API blueprint
    api_blueprint = create_api_blueprint()

    # Register the blueprints
    app.register_blueprint(dashboard_blueprint, url_prefix=f'/{dashboard_route}')
    app.register_blueprint(api_blueprint)  # Mounted at '/api' as defined in the blueprint

    # Store the dashboard route for use in templates
    app.config['DASHBOARD_ROUTE'] = dashboard_route

    # Ensure the Functionz instance is accessible in the request context
    @app.before_request
    def set_functionz():
        g.functionz = _func_instance
        g.dashboard_route = dashboard_route  # Optional, if needed globally

    return app

# Function to register functions using the babyagi framework
def register_function(*args, **kwargs):
    def wrapper(func):
        try:
            _func_instance.register_function(*args, **kwargs)(func)
            setattr(sys.modules[__name__], func.__name__, func)
            #print(f"Function '{func.__name__}' registered successfully.")
        except Exception as e:
            print(f"Error registering function '{func.__name__}': {e}")
            traceback.print_exc()
        return func
    return wrapper

# Function to load additional function packs
def load_functions(pack_name_or_path):
    #print(f"Attempting to load function pack: {pack_name_or_path}")
    if os.path.exists(pack_name_or_path):
        try:
            spec = importlib.util.spec_from_file_location("custom_pack", pack_name_or_path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            #print(f"Custom pack loaded from {pack_name_or_path}")
        except Exception as e:
            #print(f"Failed to load custom pack from path '{pack_name_or_path}': {e}")
            traceback.print_exc()
    else:
        try:
            print(f"Assuming '{pack_name_or_path}' is an internal pack...")
            _func_instance.load_function_pack(pack_name_or_path)
            print(f"Internal pack '{pack_name_or_path}' loaded successfully.")
        except Exception as e:
            print(f"Failed to load internal pack '{pack_name_or_path}': {e}")
            traceback.print_exc()


def use_blueprints(app, dashboard_route='/dashboard'):
    """
    Registers the babyagi blueprints with the provided Flask app.

    Args:
        app (Flask): The Flask application instance.
        dashboard_route (str): The route prefix for the dashboard.
    """
    # Remove leading slash if present
    if dashboard_route.startswith('/'):
        dashboard_route = dashboard_route[1:]

    # Create blueprints
    dashboard_blueprint = create_dashboard(_func_instance, dashboard_route)
    api_blueprint = create_api_blueprint()

    # Register blueprints
    app.register_blueprint(dashboard_blueprint, url_prefix=f'/{dashboard_route}')
    app.register_blueprint(api_blueprint)  # Mounted at '/api' as defined in the blueprint

    # Store the dashboard route for use in templates
    app.config['DASHBOARD_ROUTE'] = dashboard_route

    # Ensure the Functionz instance is accessible in the request context
    @app.before_request
    def set_functionz():
        g.functionz = _func_instance
        g.dashboard_route = dashboard_route  # Optional, if needed globally


def __getattr__(name):
    """
    Dynamic attribute access for the babyagi module.
    If a function with the given name exists in the database,
    return a callable that executes the function via the executor.
    """
    try:
        if _func_instance.get_function(name):
            # Return a callable that executes the function via the executor
            return lambda *args, **kwargs: _func_instance.executor.execute(name, *args, **kwargs)
    except Exception as e:
        pass
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


# Auto-load default function packs when babyagi is imported
try:
    print("Attempting to load default function packs...")
    # Uncomment if needed
    _func_instance.load_function_pack('default/default_functions')
    _func_instance.load_function_pack('default/ai_functions')
    _func_instance.load_function_pack('default/os')
    _func_instance.load_function_pack('default/function_calling_chat')
except Exception as e:
    print(f"Error loading default function packs: {e}")
    traceback.print_exc()

print("babyagi/__init__.py loaded")
```

## File: `babyagi/api/__init__.py`
```python
# babyagi/api/__init__.py

from flask import Blueprint, jsonify, request, g
from datetime import datetime
from io import StringIO
import logging
import os
import sys
import importlib.util

logger = logging.getLogger(__name__)

def create_api_blueprint():
    api = Blueprint('api', __name__, url_prefix='/api')

    # Removed the before_request function since g.functionz is set in the main app

    @api.route('/functions')
    def get_functions():
        logger.debug("Accessing /api/functions route.")
        try:
            functions = g.functionz.get_all_functions()
            logger.debug(f"Retrieved {len(functions)} functions.")
            return jsonify(functions)
        except Exception as e:
            logger.error(f"Error in get_functions: {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500

    @api.route('/function/<function_name>')
    def get_function(function_name):
        logger.debug(f"Accessing /api/function/{function_name} route.")
        try:
            function = g.functionz.db.get_function(function_name)
            if not function:
                logger.warning(f"Function '{function_name}' not found.")
                return jsonify({"error": f"Function '{function_name}' not found."}), 404
            return jsonify(function)
        except Exception as e:
            logger.error(f"Error getting function {function_name}: {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500

    @api.route('/function/<function_name>', methods=['PUT'])
    def update_function(function_name):
        logger.debug(f"Accessing /api/function/{function_name} [PUT] route.")
        try:
            data = request.get_json()
            if not data or 'code' not in data:
                logger.warning("No 'code' provided in request data.")
                return jsonify({"error": "No 'code' provided in request data."}), 400
            g.functionz.update_function(function_name, code=data['code'])
            logger.info(f"Function '{function_name}' updated successfully.")
            return jsonify({"status": "success"})
        except Exception as e:
            logger.error(f"Error updating function {function_name}: {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500

    @api.route('/execute/<function_name>', methods=['POST'])
    def execute_function(function_name):
        logger.debug(f"Accessing /api/execute/{function_name} [POST] route.")
        try:
            params = request.get_json() or {}

            if function_name == 'execute_function_wrapper':
                # Special handling for execute_function_wrapper
                inner_function_name = params.pop('function_name', None)
                args = params.pop('args', [])
                kwargs = params.pop('kwargs', {})
                result = g.functionz.executor.execute(function_name, inner_function_name, *args, **kwargs)
            else:
                # Normal execution for other functions
                result = g.functionz.executor.execute(function_name, **params)

            logger.info(f"Function '{function_name}' executed successfully.")
            return jsonify(result)
        except Exception as e:
            logger.error(f"Error executing function {function_name}: {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500

    @api.route('/function/<function_name>/versions')
    def get_function_versions(function_name):
        logger.debug(f"Accessing /api/function/{function_name}/versions route.")
        try:
            versions = g.functionz.get_function_versions(function_name)
            logger.debug(f"Retrieved {len(versions)} versions for function '{function_name}'.")
            return jsonify(versions)
        except Exception as e:
            logger.error(f"Error getting versions for function {function_name}: {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500

    @api.route('/function/<function_name>/activate/<version>', methods=['POST'])
    def activate_function_version(function_name, version):
        logger.debug(f"Accessing /api/function/{function_name}/activate/{version} [POST] route.")
        try:
            g.functionz.activate_function_version(function_name, int(version))
            logger.info(f"Version {version} of function '{function_name}' activated successfully.")
            return jsonify({"status": "success"})
        except ValueError:
            logger.warning(f"Invalid version number provided: {version}")
            return jsonify({"error": "Invalid version number."}), 400
        except Exception as e:
            logger.error(f"Error activating version {version} for function {function_name}: {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500


    @api.route('/logs/<function_name>')
    @api.route('/logs', defaults={'function_name': None})
    def get_logs(function_name):
        logger.debug(f"Accessing /api/logs/{function_name if function_name else 'all'} route.")
        try:
            start_date_str = request.args.get('start_date')
            end_date_str = request.args.get('end_date')
            triggered_by_log_id_str = request.args.get('triggered_by_log_id')  # New filter
            start_date = datetime.fromisoformat(start_date_str) if start_date_str else None
            end_date = datetime.fromisoformat(end_date_str) if end_date_str else None
            triggered_by_log_id = int(triggered_by_log_id_str) if triggered_by_log_id_str else None  # Convert to int if provided

            logs = g.functionz.db.get_logs(function_name, start_date, end_date, triggered_by_log_id)
            if function_name:
                logger.debug(f"Retrieved {len(logs)} logs for function '{function_name}'.")
            else:
                logger.debug(f"Retrieved {len(logs)} logs for all functions.")
            return jsonify(logs)
        except ValueError:
            logger.warning("Invalid date format or triggered_by_log_id provided.")
            return jsonify({"error": "Invalid date format or triggered_by_log_id. Use ISO format for dates and integer for triggered_by_log_id."}), 400
        except Exception as e:
            logger.error(f"Error getting logs for function '{function_name}': {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500

    @api.route('/log_bundle/<int:log_id>')
    def get_log_bundle(log_id):
        logger.debug(f"Accessing /api/log_bundle/{log_id} route.")
        try:
            logs = g.functionz.db.get_log_bundle(log_id)
            return jsonify({'logs': logs})
        except Exception as e:
            logger.error(f"Error getting log bundle for log_id '{log_id}': {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500


    @api.route('/triggers/<function_name>', methods=['GET'])
    def get_triggers(function_name):
        logger.debug(f"Accessing /api/triggers/{function_name} [GET] route.")
        try:
            triggers = g.functionz.get_triggers_for_function(function_name)
            trigger_list = [
                getattr(trigger.triggering_function, 'name', 'any function')
                for trigger in triggers
            ]
            logger.debug(f"Retrieved {len(trigger_list)} triggers for function '{function_name}'.")
            return jsonify(trigger_list)
        except Exception as e:
            logger.error(f"Error getting triggers for function {function_name}: {str(e)}", exc_info=True)
            return jsonify({"error": str(e)}), 500


    logger.info("API blueprint created successfully.")
    return api
```

## File: `babyagi/dashboard/__init__.py`
```python
# babyagi/dashboard/__init__.py

from flask import Blueprint, render_template, g, send_from_directory
import logging
import os

logger = logging.getLogger(__name__)

def create_dashboard(func_instance, dashboard_route):
    if func_instance is None:
        raise ValueError("func_instance cannot be None")
    if dashboard_route is None:
        raise ValueError("dashboard_route cannot be None")

    dashboard = Blueprint('dashboard', __name__, 
                          template_folder='templates', 
                          static_folder='static',
                          static_url_path='/dashboard/static')

    logger.info("Creating dashboard blueprint...")

    @dashboard.before_request
    def before_request():
        """Set up the necessary context before each request."""
        g.functionz = func_instance
        g.dashboard_route = dashboard_route
        logger.debug("Set g.functionz and g.dashboard_route for the request context.")

    @dashboard.route('/')
    def dashboard_home():
        logger.info("Accessing dashboard home page.")
        try:
            logger.debug(f"Dashboard Route: {g.dashboard_route}")
            return render_template('index.html', dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in dashboard_home: {str(e)}", exc_info=True)
            return f"Error loading dashboard: {str(e)}", 500

    @dashboard.route('/function/<function_name>')
    def function_detail(function_name):
        logger.info(f"Accessing function detail for: {function_name}")
        try:
            function = g.functionz.db.get_function(function_name)
            if not function:
                logger.warning(f"Function '{function_name}' not found.")
                return f"Function '{function_name}' not found.", 404
            return render_template('function_details.html', function_name=function_name, dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in function_detail: {str(e)}", exc_info=True)
            return f"Error loading function detail: {str(e)}", 500

    @dashboard.route('/graph')
    def function_graph():
        logger.info("Accessing function relationship graph page.")
        try:
            return render_template('function_graph.html', dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in function_graph: {str(e)}", exc_info=True)
            return f"Error loading function graph: {str(e)}", 500

    @dashboard.route('/mermaid')
    def function_graph_mermaid():
        logger.info("Accessing mermaid function relationship graph page.")
        try:
            return render_template('function_graph_mermaid.html', dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in function_graph_mermaid: {str(e)}", exc_info=True)
            return f"Error loading mermaid function graph: {str(e)}", 500

    @dashboard.route('/3d')
    def function_graph_3d():
        logger.info("Accessing 3D function relationship graph page.")
        try:
            return render_template('function_graph_3d.html', dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in function_graph_3d: {str(e)}", exc_info=True)
            return f"Error loading 3D function graph: {str(e)}", 500

    @dashboard.route('/logs')
    def logs_dashboard():
        logger.info("Accessing logs dashboard.")
        try:
            return render_template('logs_dashboard.html', dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in logs_dashboard: {str(e)}", exc_info=True)
            return f"Error loading logs dashboard: {str(e)}", 500

    @dashboard.route('/log/<int:log_id>')
    def log_page(log_id):
        logger.info(f"Accessing log page for Log ID {log_id}.")
        try:
            return render_template(
                'log_page.html',
                log_id=log_id,
                dashboard_route=g.dashboard_route  # Pass the dashboard route if needed
            )
        except Exception as e:
            logger.error(f"Error in log_page for Log ID {log_id}: {str(e)}", exc_info=True)
            return f"Error loading log page for Log ID {log_id}: {str(e)}", 500
    
    @dashboard.route('/log_graph')
    def log_relationship_graph():
        logger.info("Accessing log relationship graph.")
        try:
            return render_template('log_relationship_graph.html', dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in log_relationship_graph: {str(e)}", exc_info=True)
            return f"Error loading log relationship graph: {str(e)}", 500

    @dashboard.route('/chat')
    def chat_page():
        logger.info("Accessing chat page.")
        try:
            return render_template('chat.html', dashboard_route=g.dashboard_route)
        except Exception as e:
            logger.error(f"Error in chat_page: {str(e)}", exc_info=True)
            return f"Error loading chat page: {str(e)}", 500
    
    @dashboard.route('/<path:filename>')
    def serve_static_files(filename):
        """Serve static files from the dashboard's static folder."""
        logger.debug(f"Serving static file: {filename}")
        try:
            return send_from_directory(dashboard.static_folder, filename)
        except Exception as e:
            logger.error(f"Error serving static file '{filename}': {str(e)}", exc_info=True)
            return "File not found.", 404

    logger.info("Dashboard blueprint created successfully.")
    return dashboard

logger.info("Dashboard __init__.py loaded successfully.")
```

## File: `babyagi/dashboard/static/css/style.css`
```css
/* static/css/style.css */

/* Global Variables */
:root {
    /* Color variables */
    --primary-color: #3498db;
    --secondary-color: #2c3e50;
    --background-color: #f0f4f8;
    --text-color: #333333;
    --border-color: #e0e0e0;
    --hover-color: #f8f9fa;
    --card-bg-color: #ffffff;
    --bg-color: #f0f4f8;
    --text-color: #333;
    --accent-color: #3498db;
    --hover-color: #f7fbfc;
    --card-bg: #ffffff;
}



/* Global Styles */
body, html {
    margin: 0;
    padding: 0;
    font-family: 'Inter', Arial, sans-serif;
    background-color: var(--background-color);
    color: var(--text-color);
    font-size: 12px;
    line-height: 1.4;
}

.container {
    width: 100%;
    max-width: 100%;
    padding: 20px;
    margin: 0 auto;
    box-sizing: border-box;
}


.details-container {
    width: 100%;
    max-width: 1600px;
    padding: 20px;
    margin: 0 auto;
    box-sizing: border-box;
}

/* Hide elements with 'mobile-only' class on screens wider than 768px */
@media (min-width: 768px) {
    .mobile-only {
        display: none;
    }
}

/* Hide elements with 'desktop-only' class on screens narrower than 768px */
@media (max-width: 767px) {
    .desktop-only {
        display: none;
    }
}


/* Headers */
h1 {
    color: var(--secondary-color);
    font-size: 1.5em;
    font-weight: 600;
    margin-bottom: 20px;
    text-align: left;
}

h1 small {
    font-size: 0.7em;
    font-weight: normal;
    margin-left: 10px;
}

h1 small a {
    color: var(--primary-color);
    text-decoration: none;
}

/* Navigation Menu Styles */
nav {
    background-color: var(--secondary-color);
    padding: 10px 0;
    margin-bottom: 20px;
}

nav ul {
    list-style-type: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: left;
    flex-wrap: wrap;
}

nav li {
    margin: 0 15px;
}

nav a {
    color: #ffffff;
    text-decoration: none;
    font-weight: 500;
    font-size: 14px;
}

nav a:hover {
    text-decoration: underline;
    color: var(--primary-color);
}

/* Breadcrumb Styles */
.breadcrumb {
    margin-bottom: 20px;
}

.breadcrumb a {
    color: var(--primary-color);
    text-decoration: none;
}

.breadcrumb a:hover {
    text-decoration: underline;
}



/* Search Bar Styles */
#searchInput {
    width: 100%;
    max-width: 1200px; /* Match the container's max-width */
    padding: 10px;
    margin-bottom: 20px;
    font-size: 14px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    box-sizing: border-box;
}

/* Table Styles */
table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    background-color: var(--card-bg-color);
    box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    table-layout: fixed;
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid var(--border-color);
    vertical-align: top;
}

td {
    word-wrap: break-word;
    overflow-wrap: break-word;
}

th {
    background-color: var(--secondary-color);
    color: white;
    font-weight: 500;
    white-space: nowrap;
    cursor: pointer;
}

th.sortable:hover {
    background-color: var(--primary-color);
}

tr:hover {
    background-color: var(--hover-color);
}

.function-name {
    color: var(--primary-color);
    font-weight: 500;
    text-decoration: none;
}

.function-name:hover {
    text-decoration: underline;
}

.function-link, .function-name {
    color: var(--primary-color);
    font-weight: 500;
    text-decoration: none;
}

.function-link:hover, .function-name:hover {
    text-decoration: underline;
}

.small-text {
    font-size: 0.92em;
    color: #666;
}

.params-list, .dependencies-list, .imports-list, .triggers-list {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

.params-list li, .dependencies-list li, .imports-list, .triggers-list li {
    margin-bottom: 2px;
}

/* Card Styles (for mobile view) */
.function-grid {
    display: none;
    grid-template-columns: 1fr;
    gap: 15px;
    padding: 10px;
}

.function-card {
    background-color: var(--background-color);
    border: 1px solid var(--border-color);
    border-radius: 4px;
    padding: 15px;
}

.function-meta {
    color: #666;
    margin-bottom: 10px;
}

.function-description {
    margin-bottom: 10px;
}

.params-title {
    font-weight: 500;
    margin-top: 8px;
    margin-bottom: 3px;
}

.log-info {
    display: flex;
    justify-content: space-between;
    color: #666;
    border-top: 1px solid var(--border-color);
    padding-top: 8px;
    margin-top: 8px;
}

/* Function Detail Page Styles */
.function-detail {
    background-color: var(--card-bg-color);
    padding: 20px;
    border-radius: 8px;
    margin-bottom: 20px;
}

.section-title {
    font-size: 1.2em;
    font-weight: bold;
    margin-top: 20px;
    margin-bottom: 10px;
    color: var(--primary-color);
}

.button {
    background-color: var(--primary-color);
    color: white;
    padding: 10px 15px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-size: 14px;
    margin-right: 10px;
}

.button:hover {
    background-color: var(--hover-color);
}

#functionLogs {
    max-height:600px;
    overflow-y:scroll;
}

.log-entry, .execution-result {
    background-color: #f8f9fa;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 12px;
    line-height: 1.4;
    overflow-x: auto;
}

.param-input {
    margin-bottom: 10px;
}

.param-input label {
    display: block;
    margin-bottom: 5px;
}

.param-input input, .param-input textarea {
    width: 100%;
    padding: 5px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
}

.breadcrumb {
    margin-bottom: 20px;
}

.breadcrumb a {
    color: var(--primary-color);
    text-decoration: none;
}

.breadcrumb a:hover {
    text-decoration: underline;
}

.two-column {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
}

.column {
    flex: 1;
    min-width: 300px;
}

.detail-item {
    background-color: #f8f9fa;
    padding: 10px;
    margin-bottom: 10px;
    border-radius: 4px;
    font-family: monospace;
    font-size: 12px;
    line-height: 1.4;
    overflow-x: auto;
}

.detail-label {
    display: inline-block;
    min-width: 120px;
    font-weight: bold;
    color: var(--primary-color);
    margin-right: 10px;
}

.detail-value {
    display: inline-block;
}

.detail-list {
    margin: 5px 0 5px 130px;
    padding-left: 20px;
}

.CodeMirror {
    font-size: 12px;
    border: 1px solid var(--border-color);
    border-radius: 4px;
    margin-bottom: 5px;
}

/* Version History */
.version-item {
    padding: 10px;
    border-bottom: 1px solid #ccc;
    background-color: #f8f9fa;
    margin-bottom: 5px;
    word-wrap: break-word;
    white-space: pre-wrap;
    max-height:600px;
}

.version-item.active {
    background-color: #e0f7fa;
}

.version-item pre {
    background-color: #f1f1f1;
    padding: 10px;
    border-radius: 4px;
    font-size: 12px;
    overflow-x: auto;
    white-space: pre-wrap;
    word-wrap: break-word;
    line-height: 1.4;
}

#toggleVersionHistory {
    margin-top: 10px;
}

#versionHistory {
    margin-top: 10px;
}

/* Media Queries */
@media (max-width: 768px) {
    /* Hide the table in mobile, show the card grid */
    table {
        display: none;
    }
    .function-grid {
        display: grid;
    }
    .two-column {
        flex-direction: column;
    }
    .container, #searchInput, .function-detail, .column, input, body {
        padding: 10px;
        max-width: 100%;
    }
    .param-input{
        margin:10px;
    }
}
```

## File: `babyagi/dashboard/static/js/dashboard.js`
```javascript
/* static/js/dashboard.js */

// Assume that dashboardRoute, apiFunctionsUrl, and apiLogsUrl are defined in the HTML template

let currentSort = { key: null, direction: 'asc' };
let allFunctions = []; // This will hold the functions data globally

function filterTable() {
    const input = document.getElementById("searchInput").value.toLowerCase();
    const table = document.getElementById("functionTable");
    const rows = table.getElementsByTagName("tr");
    const grid = document.getElementById("functionGrid");
    const cards = grid.getElementsByClassName("function-card");

    for (let i = 1; i < rows.length; i++) { // Start at 1 to skip header row
        let match = false;
        const cells = rows[i].getElementsByTagName("td");
        for (let j = 0; j < cells.length; j++) {
            if (cells[j].innerText.toLowerCase().includes(input)) {
                match = true;
                break;
            }
        }
        rows[i].style.display = match ? "" : "none";
    }

    // Filter cards for mobile view
    for (let i = 0; i < cards.length; i++) {
        if (cards[i].innerText.toLowerCase().includes(input)) {
            cards[i].style.display = "";
        } else {
            cards[i].style.display = "none";
        }
    }
}
function sortTable(key) {
    const direction = currentSort.key === key && currentSort.direction === 'asc' ? 'desc' : 'asc';
    currentSort = { key, direction };

    const sortedFunctions = [...allFunctions].sort((a, b) => {
        let valA, valB;
        if (key === 'name') {
            valA = a.name.toLowerCase();
            valB = b.name.toLowerCase();
        } else if (key === 'created_date') {
            valA = new Date(a.created_date);
            valB = new Date(b.created_date);
        } else if (key === 'total_logs') {
            valA = a.total_logs || 0;
            valB = b.total_logs || 0;
        } else if (key === 'last_log_date') {
            valA = new Date(a.last_log_date || 0);
            valB = new Date(b.last_log_date || 0);
        }

        if (direction === 'asc') return valA > valB ? 1 : -1;
        return valA < valB ? 1 : -1;
    });

    populateDashboard(sortedFunctions);
}

async function fetchLogs(functionName) {
    try {
        const response = await fetch(`${apiLogsUrl}${encodeURIComponent(functionName)}`);
        if (!response.ok) {
            throw new Error('Failed to fetch logs');
        }
        const logs = await response.json();
        return {
            total_logs: logs.length,
            last_log_date: logs.length > 0 ? logs[logs.length - 1].timestamp : null
        };
    } catch (error) {
        console.error(`Error fetching logs for ${functionName}:`, error);
        return { total_logs: 0, last_log_date: null };
    }
}

function updateLogsAsync(tasks) {
    const promises = tasks.map(([functionName, row]) => {
        return fetchLogs(functionName).then(({ total_logs, last_log_date }) => {
            const totalLogsCell = row.querySelector('.total-logs');
            const lastLogDateCell = row.querySelector('.last-log-date');
            totalLogsCell.textContent = total_logs;
            lastLogDateCell.textContent = last_log_date ? new Date(last_log_date).toLocaleDateString() : 'N/A';

            // Update function in allFunctions array
            const func = allFunctions.find(f => f.name === functionName);
            if (func) {
                func.total_logs = total_logs;
                func.last_log_date = last_log_date;
            }
        });
    });
    return Promise.all(promises);
}

async function populateDashboard(functions) {
    allFunctions = functions; // Store functions globally for sorting
    const tableBody = document.querySelector('#functionTable tbody');
    const grid = document.getElementById('functionGrid');
    const logTasks = [];

    tableBody.innerHTML = '';
    grid.innerHTML = '';

    for (const func of functions) {
        const row = document.createElement('tr');
        const description = func.metadata && func.metadata.description ? func.metadata.description : 'No description available';
        const createdDate = new Date(func.created_date).toLocaleDateString();

        row.innerHTML = `
            <td><a href="${dashboardRoute}/function/${encodeURIComponent(func.name)}" class="function-name">${func.name}</a></td>
            <td class="small-text">v${func.version}</td>
            <td>${description}</td>
            <td>${formatParams(func.input_parameters)}</td>
            <td>${formatParams(func.output_parameters)}</td>
            <td>${formatList(func.dependencies, 'dependencies-list', dashboardRoute)}</td>
            <td>${formatList(func.imports, 'imports-list')}</td>
            <td>${formatList(func.triggers, 'triggers-list', dashboardRoute)}</td>
            <td class="small-text">${createdDate}</td>
            <td class="small-text total-logs">Loading...</td>
            <td class="small-text last-log-date">Loading...</td>
        `;
        tableBody.appendChild(row);

        // Populate card view (for mobile)
        const card = document.createElement('div');
        card.className = 'function-card';
        card.innerHTML = `
            <a href="${dashboardRoute}function/${encodeURIComponent(func.name)}" class="function-name">${func.name}</a>
            <div class="function-meta">v${func.version} | Created: ${createdDate}</div>
            <div class="function-description">${description}</div>
            <div class="params-title">Input Parameters:</div>
            ${formatParams(func.input_parameters)}
            <div class="params-title">Output Parameters:</div>
            ${formatParams(func.output_parameters)}
            <div class="params-title">Dependencies:</div>
            ${formatList(func.dependencies, 'dependencies-list', dashboardRoute)}
            <div class="params-title">Imports:</div>
            ${formatList(func.imports, 'imports-list')}
            <div class="params-title">Triggers:</div>
            ${formatList(func.triggers, 'triggers-list', dashboardRoute)}
            <div class="log-info">
                <span>Total Logs: <span class="total-logs">Loading...</span></span>
                <span>Last Log: <span class="last-log-date">Loading...</span></span>
            </div>
        `;
        grid.appendChild(card);

        logTasks.push([func.name, row]);
    }

    updateLogsAsync(logTasks);
}

function formatParams(params) {
    if (!params || params.length === 0) {
        return '<span class="small-text"></span>';
    }
    return '<ul class="params-list">' + 
        params.map(param => `<li>${param.name}: <span class="small-text">${param.type}</span></li>`).join('') + 
        '</ul>';
}

function formatList(items, className, dashboardRoute) {
    if (!items || items.length === 0) {
        return '<span class="small-text">-</span>';
    }
    return '<ul class="' + className + '">' + 
        items.map(item => {
            if (className === 'dependencies-list' || className === 'triggers-list') {
                return `<li><a href="${dashboardRoute}/function/${encodeURIComponent(item)}" class="function-link">${item}</a></li>`;
            }
            return `<li>${item}</li>`;
        }).join('') + 
        '</ul>';
}

// Fetch functions data and populate the dashboard
async function fetchFunctionsAndPopulate() {
    try {
        const response = await fetch(apiFunctionsUrl);
        if (!response.ok) {
            throw new Error('Failed to fetch functions');
        }
        const data = await response.json();
        populateDashboard(data);
    } catch (error) {
        console.error('Error fetching functions:', error);
        document.querySelector('.container').innerHTML += `<p style="color: red;">Error loading functions. Please try refreshing the page.</p>`;
    }
}

// Call the function when the page loads
document.addEventListener('DOMContentLoaded', () => {
    fetchFunctionsAndPopulate();

    // Add event listener for search input
    const searchInput = document.getElementById("searchInput");
    searchInput.addEventListener('input', filterTable);
});
```

## File: `babyagi/dashboard/static/js/function_details.js`
```javascript
// At the top of function_details.js


// Ensure apiRoutes is defined
window.apiRoutes = window.apiRoutes || {};

// Helper function to get the API route
function getApiRoute(routeName, ...args) {
    if (typeof apiRoutes[routeName] === 'function') {
        return apiRoutes[routeName](...args);
    } else {
        return apiRoutes[routeName];
    }
}

window.getApiRoute = getApiRoute;

let functionData;
let codeEditor;

// Expose necessary functions to the global scope
window.loadFunctionDetails = loadFunctionDetails;
window.loadFunctionLogs = loadFunctionLogs;
window.initCodeEditor = initCodeEditor;
window.displayFunctionDetails = displayFunctionDetails;
window.createExecutionForm = createExecutionForm;
window.updateFunction = updateFunction;
window.executeFunction = executeFunction;
window.toggleVersionHistory = toggleVersionHistory;
window.loadFunctionVersions = loadFunctionVersions;
window.activateVersion = activateVersion;

function loadFunctionDetails() {
    fetch(getApiRoute('getFunction'))
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(data => {
            functionData = data;
            console.log("functionData",functionData)
            displayFunctionDetails();
            createExecutionForm();
            initCodeEditor();
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('functionDetails').innerHTML = `<p>Error loading function details: ${error.message}</p>`;
        });
}

function loadFunctionLogs() {
    fetch(getApiRoute('getLogs'))
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(logs => {
            let logsHtml = logs.map(log => `
                <div class="log-entry">
                    <strong>Timestamp:</strong> ${new Date(log.timestamp).toLocaleString()}<br>
                    <strong>Message:</strong> ${log.message}<br>
                    <strong>Params:</strong> ${JSON.stringify(log.params)}<br>
                    <strong>Output:</strong> ${JSON.stringify(log.output)}<br>
                    <strong>Time spent:</strong> ${log.time_spent} seconds
                </div>
            `).join('');
            document.getElementById('functionLogs').innerHTML = logsHtml;
        })
        .catch(error => {
            console.error('Error:', error);
            document.getElementById('functionLogs').innerHTML = `<p>Error loading logs: ${error.message}</p>`;
        });
}

function initCodeEditor() {
    const editorElement = document.getElementById('codeEditor'); // Example: Get the editor element

    // Check if the editor element exists
    if (!editorElement) {
        console.error("Code editor textarea not found!");
        return;
    }

    // Destroy the previous CodeMirror instance if it exists
    if (codeEditor) {
        codeEditor.toTextArea(); // Converts the editor back into a textarea
        codeEditor = null; // Clear the reference
    }

    // Initialize the new CodeMirror instance
    codeEditor = CodeMirror.fromTextArea(editorElement, {
        mode: "python",
        theme: "monokai",
        lineNumbers: true,
        indentUnit: 4,
        tabSize: 4,
        indentWithTabs: false,
        autofocus: true
    });
    console.log("initCodeEditor executing");
    console.log("window.functionData.code", functionData.code);
    console.log("window.functionData", functionData);

    // Set the current function code (if available)
    if (functionData && functionData.code) {
        codeEditor.setValue(functionData.code);
    } else {
        codeEditor.setValue(""); // Clear editor if no code
    }

    // Refresh CodeMirror to fix display issues
    setTimeout(() => {
        codeEditor.refresh();
    }, 200); // Short delay to ensure the editor is fully visible before refreshing
}



function displayFunctionDetails() {
    document.getElementById('functionName').textContent = functionData.name;

    let detailsHtml = `
        <div class="detail-item">
            <span class="detail-label">Version:</span>
            <span class="detail-value">${functionData.version}</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Created Date:</span>
            <span class="detail-value">${new Date(functionData.created_date).toLocaleString()}</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Description:</span>
            <span class="detail-value">${functionData.metadata.description || 'No description available'}</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Dependencies:</span>
            <span class="detail-value">$
                <span class="detail-value">
                  ${functionData.dependencies.length ? functionData.dependencies.map(dep => `
                    <a href="${dashboardRoute}/function/${encodeURIComponent(dep)}" class="function-name">${dep}</a>
                  `).join(', ') : 'None'}
                </span>

            </span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Imports:</span>
            <span class="detail-value">${functionData.imports ? functionData.imports.join(', ') : 'None'}</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Triggers:</span>
            <span class="detail-value">${functionData.triggers.join(', ') || 'None'}</span>
        </div>
        <div class="detail-item">
            <span class="detail-label">Input Parameters:</span>
            <ul class="detail-list">
                ${functionData.input_parameters.map(param => `<li>${param.name} (${param.type})</li>`).join('')}
            </ul>
        </div>
        <div class="detail-item">
            <span class="detail-label">Output Parameters:</span>
            <ul class="detail-list">
                ${functionData.output_parameters.map(param => `<li>${param.name} (${param.type})</li>`).join('')}
            </ul>
        </div>
    `;

    document.getElementById('functionDetails').innerHTML = detailsHtml;
}

function createExecutionForm() {
    let formHtml = '';
    if (functionData.name === 'execute_function_wrapper') {
        formHtml += `
            <div class="param-input">
                <label for="function_name">function_name (str):</label>
                <input type="text" id="function_name" name="function_name">
            </div>
            <div class="param-input">
                <label for="args">args (comma-separated values):</label>
                <input type="text" id="args" name="args">
            </div>
            <div class="param-input">
                <label for="kwargs">kwargs (JSON format):</label>
                <textarea id="kwargs" name="kwargs" rows="5" cols="50"></textarea>
            </div>
        `;
    } else {
        functionData.input_parameters.forEach(param => {
            if (param.type === 'json') {
                formHtml += `
                    <div class="param-input">
                        <label for="${param.name}">${param.name} (${param.type}):</label>
                        <textarea id="${param.name}" name="${param.name}" rows="5" cols="50"></textarea>
                    </div>
                `;
            } else {
                formHtml += `
                    <div class="param-input">
                        <label for="${param.name}">${param.name} (${param.type}):</label>
                        <input type="text" id="${param.name}" name="${param.name}">
                    </div>
                `;
            }
        });
    }
    document.getElementById('executionForm').innerHTML = formHtml;
}

function updateFunction() {
    const updatedCode = codeEditor.getValue();
    fetch(getApiRoute('updateFunction'), {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            code: updatedCode,
        }),
    })
    .then(response => response.json())
    .then(data => {
        alert('Function updated successfully');
        functionData.code = updatedCode;
        if (data.version) {
            functionData.version = data.version;
        }
        displayFunctionDetails();
    })
    .catch((error) => {
        console.error('Error:', error);
        alert('Error updating function');
    });
}

function executeFunction() {
    let params = {};
    if (functionData.name === 'execute_function_wrapper') {
        const functionNameInput = document.getElementById('function_name').value.trim();
        if (!functionNameInput) {
            alert('Function name is required.');
            return;
        }
        const args = document.getElementById('args').value ? 
            document.getElementById('args').value.split(',').map(arg => arg.trim()) : [];
        let kwargs = {};
        const kwargsValue = document.getElementById('kwargs').value.trim();
        if (kwargsValue) {
            try {
                kwargs = JSON.parse(kwargsValue);
            } catch (e) {
                alert('Invalid JSON input for kwargs. Please check your input.');
                return;
            }
        }
        params = {
            function_name: functionNameInput,
            args: args,
            kwargs: kwargs
        };
    } else {
        for (const param of functionData.input_parameters) {
            let value = document.getElementById(param.name).value.trim();

            // Skip empty inputs
            if (value === '') continue;

            try {
                switch (param.type) {
                    case 'int':
                        value = parseInt(value, 10);
                        if (isNaN(value)) throw new Error(`Invalid integer for ${param.name}`);
                        break;
                    case 'float':
                        value = parseFloat(value);
                        if (isNaN(value)) throw new Error(`Invalid float for ${param.name}`);
                        break;
                    case 'bool':
                        value = value.toLowerCase();
                        if (value !== 'true' && value !== 'false') throw new Error(`Invalid boolean for ${param.name}. Use 'true' or 'false'.`);
                        value = value === 'true';
                        break;
                    case 'date':
                        value = new Date(value);
                        if (isNaN(value.getTime())) throw new Error(`Invalid date for ${param.name}`);
                        break;
                    case 'list':
                        value = value.split(',').map(item => item.trim());
                        break;
                    case 'json':
                        value = JSON.parse(value);
                        break;
                }
                params[param.name] = value;
            } catch (error) {
                alert(`Error with parameter ${param.name}: ${error.message}`);
                return;
            }
        }
    }

    fetch(getApiRoute('executeFunction'), {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(params),
    })
    .then(response => {
        if (!response.ok) {
            return response.text().then(text => {
                throw new Error(text || response.statusText);
            });
        }
        return response.json();
    })
    .then(data => {
        document.getElementById('executionResult').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('executionResult').innerHTML = `<pre class="error">Error executing function: ${error.message}</pre>`;
    });
}

let isVersionHistoryVisible = false;

function toggleVersionHistory() {
    const versionHistory = document.getElementById('versionHistory');
    if (isVersionHistoryVisible) {
        versionHistory.style.display = 'none';
        document.getElementById('toggleVersionHistory').textContent = 'Show Versions';
    } else {
        loadFunctionVersions();
        versionHistory.style.display = 'block';
        document.getElementById('toggleVersionHistory').textContent = 'Hide Versions';
    }
    isVersionHistoryVisible = !isVersionHistoryVisible;
}

function loadFunctionVersions() {
    fetch(getApiRoute('getFunctionVersions'))
        .then(response => response.json())
        .then(versions => {
            const versionHistoryDiv = document.getElementById('versionHistory');
            let versionHtml = versions.map(version => `
                <div class="version-item ${version.is_active ? 'active' : ''}">
                    <strong>Version ${version.version}</strong> - Created: ${new Date(version.created_date).toLocaleString()}
                    <pre>${version.code}</pre>
                    <button class="button" onclick="activateVersion(${version.version})">Activate Version</button>
                </div>
            `).join('');
            versionHistoryDiv.innerHTML = versionHtml;
        })
        .catch(error => console.error('Error loading versions:', error));
}

function activateVersion(version) {
    const url = getApiRoute('activateVersion', version);
    fetch(url, {
        method: 'POST',
    })
    .then(response => response.json())
    .then(data => {
        alert('Version activated successfully');
        loadFunctionDetails();
        loadFunctionVersions();
    })
    .catch(error => console.error('Error activating version:', error));
}

window.addEventListener('load', function() {
    loadFunctionDetails();
    loadFunctionLogs();
});
```

## File: `babyagi/dashboard/static/js/function_graph.js`
```javascript
// function_graph.js
let cy;

document.addEventListener('DOMContentLoaded', () => {
    cy = cytoscape({
        container: document.getElementById('graph'),
        style: [
            {
                selector: 'node',
                style: {
                    'shape': 'rectangle',
                    'background-color': '#E6F2FF',
                    'label': 'data(id)',
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'text-wrap': 'wrap',
                    'text-max-width': '150px',
                    'width': 'label',
                    'height': 'label',
                    'padding': '12px',
                    'font-weight': 'bold',
                    'font-size': '16px',
                    'color': '#333333',
                    'text-outline-color': '#FFFFFF',
                    'text-outline-width': 1,
                    'cursor': 'pointer'
                }
            },
            {
                selector: 'node[type="import"]',
                style: {
                    'background-color': '#E6FFF2'
                }
            },
            {
                selector: 'node[type="trigger"]',
                style: {
                    'background-color': '#FFE6E6'
                }
            },
            {
                selector: 'node:hover',
                style: {
                    'background-opacity': 0.8
                }
            },
            {
                selector: 'edge',
                style: {
                    'width': 1,
                    'line-color': '#999999',
                    'target-arrow-color': '#999999',
                    'target-arrow-shape': 'triangle',
                    'curve-style': 'bezier',
                    'arrow-scale': 1.5
                }
            },
            {
                selector: 'edge[type="dependency"]',
                style: {
                    'width': 2
                }
            },
            {
                selector: 'edge[type="trigger"]',
                style: {
                    'line-style': 'dashed',
                    'label': 'trigger',
                    'font-size': '12px',
                    'text-rotation': 'autorotate',
                    'text-margin-y': -10
                }
            }
        ],
        layout: {
            name: 'cose',
            idealEdgeLength: 50,
            nodeOverlap: 20,
            refresh: 20,
            fit: true,
            padding: 30,
            randomize: false,
            componentSpacing: 80,
            nodeRepulsion: 450000,
            edgeElasticity: 100,
            nestingFactor: 5,
            gravity: 80,
            numIter: 1000,
            initialTemp: 200,
            coolingFactor: 0.95,
            minTemp: 1.0
        },
        wheelSensitivity: 0.2
    });

    fetch('/api/functions')
        .then(response => response.json())
        .then(data => {
            const elements = [];
            const imports = new Set();

            data.forEach(func => {
                elements.push({ data: { id: func.name, type: 'function' } });

                func.dependencies.forEach(dep => {
                    elements.push({ data: { id: dep, type: 'function' } });
                    elements.push({ data: { source: func.name, target: dep, type: 'dependency' } });
                });

                func.triggers.forEach(trigger => {
                    elements.push({ data: { id: trigger, type: 'trigger' } });
                    elements.push({ data: { source: func.name, target: trigger, type: 'trigger' } });
                });

                func.imports.forEach(imp => imports.add(imp));
            });

            imports.forEach(imp => {
                elements.push({ data: { id: imp, type: 'import' } });
            });

            data.forEach(func => {
                func.imports.forEach(imp => {
                    elements.push({ data: { source: func.name, target: imp, type: 'import' } });
                });
            });

            cy.add(elements);
            cy.layout({ name: 'cose' }).run();

            cy.fit(40);

            cy.zoom({
                level: cy.zoom() * 1.3,
                renderedPosition: { x: cy.width() / 2, y: cy.height() / 2 }
            });
        });

    cy.on('tap', 'node', function(evt) {
        const node = evt.target;
        if (node.data('type') === 'function' || node.data('type') === 'trigger') {
            showFunctionOverlay(node.id());
        }
    });

    cy.on('zoom pan', () => {
        closeOverlay();
    });
});

function showFunctionOverlay(functionName) {
    const overlay = document.getElementById('overlay');
    const content = document.getElementById('overlay-content');

    fetch(`/api/function/${functionName}`)
        .then(response => response.json())
        .then(data => {
            content.innerHTML = `
                <h3>${data.name}</h3>
                <div id="tab-buttons">
                    <button class="tab-button active" onclick="showTab('description', '${data.name}')">Description</button>
                    <button class="tab-button" onclick="showTab('code', '${data.name}')">Code</button>
                    <button class="tab-button" onclick="showTab('logs', '${data.name}')">Logs</button>
                </div>
                <div id="tab-content">
                    <div id="description-tab">
                        <p><strong>Description:</strong> ${data.metadata.description || 'No description available.'}</p>
                        <p><strong>Version:</strong> ${data.version}</p>
                    </div>
                    <div id="code-tab" style="display: none;"></div>
                    <div id="logs-tab" style="display: none;"></div>
                </div>
            `;

            const node = cy.$id(functionName);
            const renderedPosition = node.renderedPosition();

            overlay.style.left = `${renderedPosition.x + 10}px`;
            overlay.style.top = `${renderedPosition.y + 10}px`;
            overlay.style.display = 'block';
        });
}

function showTab(tabName, functionName) {
    const tabs = ['description', 'code', 'logs'];
    tabs.forEach(tab => {
        const tabElement = document.getElementById(`${tab}-tab`);
        const tabButton = document.querySelector(`button.tab-button:nth-child(${tabs.indexOf(tab) + 1})`);
        if (tab === tabName) {
            tabElement.style.display = 'block';
            tabButton.classList.add('active');
        } else {
            tabElement.style.display = 'none';
            tabButton.classList.remove('active');
        }
    });

    if (tabName === 'code' && document.getElementById('code-tab').innerHTML === '') {
        showCode(functionName);
    } else if (tabName === 'logs' && document.getElementById('logs-tab').innerHTML === '') {
        showLogs(functionName);
    }
}

function showCode(functionName) {
    fetch(`/api/function/${functionName}`)
        .then(response => response.json())
        .then(data => {
            const codeTab = document.getElementById('code-tab');
            codeTab.innerHTML = `
                <h4>Code:</h4>
                <pre><code>${data.code}</code></pre>
            `;
        });
}

function showLogs(functionName) {
    fetch(`/api/logs/${functionName}`)
        .then(response => response.json())
        .then(data => {
            const logsTab = document.getElementById('logs-tab');
            logsTab.innerHTML = `
                <h4>Logs:</h4>
                <pre>${JSON.stringify(data, null, 2)}</pre>
            `;
        });
}

function closeOverlay() {
    document.getElementById('overlay').style.display = 'none';
}
```

## File: `babyagi/dashboard/static/js/log_dashboard.js`
```javascript
let currentSort = { key: 'timestamp', direction: 'desc' }; // Set default sort to 'timestamp' descending
let allLogs = []; // Holds all fetched logs
let filteredLogs = []; // Holds logs after filtering
let rootLogs = []; // Holds the root logs after building the tree

// Fetch unique values for function names and log types to populate filter dropdowns
async function populateFilters() {
    try {
        const response = await fetch(apiLogsUrl);
        if (!response.ok) {
            throw new Error('Failed to fetch logs for filters');
        }
        let logs = await response.json();

        // **Sort logs by timestamp descending (most recent first)**
        logs.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));

        allLogs = logs;
        filteredLogs = logs;

        const functionFilter = document.getElementById('functionFilter');
        const logTypeFilter = document.getElementById('logTypeFilter');

        const uniqueFunctions = [...new Set(logs.map(log => log.function_name))].sort();
        uniqueFunctions.forEach(func => {
            const option = document.createElement('option');
            option.value = func;
            option.textContent = func;
            functionFilter.appendChild(option);
        });

        const uniqueLogTypes = [...new Set(logs.map(log => log.log_type))].sort();
        uniqueLogTypes.forEach(type => {
            const option = document.createElement('option');
            option.value = type;
            option.textContent = capitalizeFirstLetter(type);
            logTypeFilter.appendChild(option);
        });

        // Build the tree structure
        rootLogs = buildLogTree(filteredLogs);

        renderLogs();
    } catch (error) {
        console.error('Error populating filters:', error);
        alert('Failed to load logs for filters. Please try again later.');
    }
}

// Build log tree based on parent_log_id
function buildLogTree(logs) {
    const logsById = {};
    const rootLogs = [];

    // Initialize logsById mapping and add children array to each log
    logs.forEach(log => {
        log.children = [];
        logsById[log.id] = log;
    });

    // Build the tree
    logs.forEach(log => {
        if (log.parent_log_id !== null) {
            const parentLog = logsById[log.parent_log_id];
            if (parentLog) {
                parentLog.children.push(log);
            } else {
                // Parent log not found, treat as root
                rootLogs.push(log);
            }
        } else {
            rootLogs.push(log);
        }
    });

    return rootLogs;
}

// Render logs in table and grid formats
function renderLogs() {
    renderTable();
    renderGrid();
}

// Render Logs Table (Desktop View)
function renderTable() {
    const tableBody = document.querySelector('#logTable tbody');
    tableBody.innerHTML = '';

    rootLogs.forEach(log => {
        renderLogRow(tableBody, log, 0);
    });
}

// Recursive function to render each log row and its children
function renderLogRow(tableBody, log, depth, parentRowId) {
    const row = document.createElement('tr');
    const rowId = 'log-' + log.id;
    row.id = rowId;

    // If it's a child row, add a class to indicate it's a child
    if (parentRowId) {
        row.classList.add('child-of-log-' + parentRowId);
        row.style.display = 'none'; // Hide child rows by default
    }

    // Check if log has children
    const hasChildren = log.children && log.children.length > 0;

    // Create expand/collapse icon
    let toggleIcon = '';
    if (hasChildren) {
        toggleIcon = `<span class="toggle-icon" data-log-id="${log.id}" style="cursor:pointer;">[+]</span> `;
    }

    row.innerHTML = `
        <td><a href="${dashboardRoute}/log/${log.id}" class="function-link">${log.id}</a></td>
        <td><a href="${dashboardRoute}/function/${encodeURIComponent(log.function_name)}" class="function-link">${log.function_name}</a></td>
        <td style="padding-left:${depth * 20}px">${toggleIcon}${log.message}</td>
        <td>${new Date(log.timestamp).toLocaleString()}</td>
        <td>${capitalizeFirstLetter(log.log_type)}</td>
        <td>${log.time_spent ? log.time_spent.toFixed(3) : 'N/A'}</td>
        <td>${log.parent_log_id !== null ? log.parent_log_id : 'N/A'}</td>
        <td>${log.triggered_by_log_id !== null ? log.triggered_by_log_id : 'N/A'}</td>
    `;
    tableBody.appendChild(row);

    // Add event listener for toggle
    if (hasChildren) {
        row.querySelector('.toggle-icon').addEventListener('click', function() {
            toggleChildRows(log.id);
            // Update the icon
            const icon = this;
            if (icon.textContent === '[+]') {
                icon.textContent = '[-]';
            } else {
                icon.textContent = '[+]';
            }
        });
    }

    // Recursively render children
    if (hasChildren) {
        log.children.forEach(childLog => {
            renderLogRow(tableBody, childLog, depth + 1, log.id);
        });
    }
}

// Function to toggle child rows
function toggleChildRows(parentLogId) {
    const childRows = document.querySelectorAll('.child-of-log-' + parentLogId);

    childRows.forEach(row => {
        if (row.style.display === 'none') {
            row.style.display = '';
        } else {
            row.style.display = 'none';
            // Recursively hide any child rows
            const childLogId = row.id.replace('log-', '');
            toggleChildRows(childLogId);
            // Reset the toggle icon of child rows to '[+]'
            const toggleIcon = row.querySelector('.toggle-icon');
            if (toggleIcon) {
                toggleIcon.textContent = '[+]';
            }
        }
    });
}

// Render Logs Grid (Mobile View)
function renderGrid() {
    const logGrid = document.getElementById('logGrid');
    logGrid.innerHTML = '';

    rootLogs.forEach(log => {
        renderLogCard(logGrid, log, 0);
    });
}

// Recursive function to render log cards and their children
function renderLogCard(container, log, depth) {
    const card = document.createElement('div');
    card.className = 'log-card';
    card.style.marginLeft = (depth * 20) + 'px';

    card.innerHTML = `
        <h5>ID: <a href="${dashboardRoute}/log/${log.id}" class="function-link">${log.id}</a></h5>
        <div class="log-meta">Function: <a href="${dashboardRoute}/function/${encodeURIComponent(log.function_name)}">${log.function_name}</a> | ${new Date(log.timestamp).toLocaleString()}</div>
        <div class="log-details"><strong>Message:</strong> ${log.message}</div>
        <div class="log-details"><strong>Log Type:</strong> ${capitalizeFirstLetter(log.log_type)}</div>
        <div class="log-details"><strong>Time Spent:</strong> ${log.time_spent ? log.time_spent.toFixed(3) : 'N/A'} seconds</div>
        <div class="log-details"><strong>Parent Log ID:</strong> ${log.parent_log_id !== null ? log.parent_log_id : 'N/A'}</div>
        <div class="log-details"><strong>Triggered By Log ID:</strong> ${log.triggered_by_log_id !== null ? log.triggered_by_log_id : 'N/A'}</div>
    `;
    container.appendChild(card);

    // Recursively render children
    if (log.children && log.children.length > 0) {
        log.children.forEach(childLog => {
            renderLogCard(container, childLog, depth + 1);
        });
    }
}

// Capitalize the first letter of a string
function capitalizeFirstLetter(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

// Sort logs based on a key
function sortLogs(key) {
    if (currentSort.key === key) {
        currentSort.direction = currentSort.direction === 'asc' ? 'desc' : 'asc';
    } else {
        currentSort.key = key;
        currentSort.direction = 'asc';
    }

    // Sort root logs
    rootLogs.sort((a, b) => {
        let valA = a[key];
        let valB = b[key];

        // Handle null or undefined values
        if (valA === null || valA === undefined) valA = '';
        if (valB === null || valB === undefined) valB = '';

        // If sorting by timestamp, convert to Date
        if (key === 'timestamp') {
            valA = new Date(valA);
            valB = new Date(valB);
        }

        // If sorting by time_spent or IDs, ensure numerical comparison
        if (key === 'time_spent' || key === 'id' || key === 'parent_log_id' || key === 'triggered_by_log_id') {
            valA = Number(valA);
            valB = Number(valB);
        }

        if (valA > valB) return currentSort.direction === 'asc' ? 1 : -1;
        if (valA < valB) return currentSort.direction === 'asc' ? -1 : 1;
        return 0;
    });

    renderLogs();
}

// Apply Filters
function applyFilters() {
    const functionFilter = document.getElementById('functionFilter').value.toLowerCase();
    const logTypeFilter = document.getElementById('logTypeFilter').value.toLowerCase();
    const startDate = document.getElementById('startDate').value;
    const endDate = document.getElementById('endDate').value;

    // First, filter the logs
    filteredLogs = allLogs.filter(log => {
        let matchesFunction = true;
        let matchesLogType = true;
        let matchesStartDate = true;
        let matchesEndDate = true;

        if (functionFilter) {
            matchesFunction = log.function_name.toLowerCase().includes(functionFilter);
        }

        if (logTypeFilter) {
            matchesLogType = log.log_type.toLowerCase() === logTypeFilter;
        }

        if (startDate) {
            matchesStartDate = new Date(log.timestamp) >= new Date(startDate);
        }

        if (endDate) {
            // Add one day to endDate to include the entire end day
            const endDateObj = new Date(endDate);
            endDateObj.setDate(endDateObj.getDate() + 1);
            matchesEndDate = new Date(log.timestamp) < endDateObj;
        }

        return matchesFunction && matchesLogType && matchesStartDate && matchesEndDate;
    });

    // Rebuild the tree
    rootLogs = buildLogTree(filteredLogs);

    renderLogs();
}

// Reset Filters
function resetFilters() {
    document.getElementById('functionFilter').value = '';
    document.getElementById('logTypeFilter').value = '';
    document.getElementById('startDate').value = '';
    document.getElementById('endDate').value = '';
    filteredLogs = allLogs;

    // Rebuild the tree
    rootLogs = buildLogTree(filteredLogs);

    renderLogs();
}

// Initialize the logs dashboard
document.addEventListener('DOMContentLoaded', () => {
    populateFilters();
});
```

## File: `babyagi/dashboard/static/js/log_graph.js`
```javascript
document.addEventListener('DOMContentLoaded', () => {
    loadLogs();
});

async function loadLogs() {
    try {
        const response = await fetch(apiLogsUrl);
        if (!response.ok) {
            throw new Error('Failed to fetch logs');
        }
        const logs = await response.json();
        renderGraph(logs);
    } catch (error) {
        console.error('Error loading logs:', error);
        alert('Failed to load logs. Please try again later.');
    }
}

function renderGraph(logs) {
    // Process logs and build graph data
    const elements = logs.map(log => ({
        data: { id: log.id, label: log.function_name }
    }));

    // Add edges for relationships
    logs.forEach(log => {
        if (log.parent_log_id) {
            elements.push({
                data: {
                    id: `parent-${log.id}`,
                    source: log.parent_log_id,
                    target: log.id,
                    label: 'Parent'
                }
            });
        }
        if (log.triggered_by_log_id) {
            elements.push({
                data: {
                    id: `trigger-${log.id}`,
                    source: log.triggered_by_log_id,
                    target: log.id,
                    label: 'Triggered By'
                }
            });
        }
    });

    // Initialize Cytoscape graph
    var cy = cytoscape({
        container: document.getElementById('graph'),
        elements: elements,
        style: [
            {
                selector: 'node',
                style: {
                    'label': 'data(label)',
                    'background-color': '#666',
                    'text-valign': 'center',
                    'text-halign': 'center',
                    'color': '#fff',
                    'text-outline-width': 2,
                    'text-outline-color': '#666'
                }
            },
            {
                selector: 'edge',
                style: {
                    'width': 2,
                    'line-color': '#ccc',
                    'target-arrow-color': '#ccc',
                    'target-arrow-shape': 'triangle',
                    'curve-style': 'bezier'
                }
            }
        ],
        layout: {
            name: 'breadthfirst',
            directed: true,
            padding: 10
        }
    });

    // Add event listeners if needed
}
```

## File: `babyagi/dashboard/templates/base.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    {% block head %}
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}PythonFunc Dashboard{% endblock %}</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
    <!-- Include external CSS -->
    <link rel="stylesheet" href="{{ url_for('dashboard.static', filename='css/style.css') }}">
    {% endblock %}
</head>
<body>
    <!-- Include the navigation menu outside the container for styling purposes -->
    <nav>
        <ul>
            <li><a href="{{ url_for('dashboard.dashboard_home') }}">Home</a></li>
            <li><a href="{{ url_for('dashboard.function_graph') }}">Graph</a></li>
            <li><a href="{{ url_for('dashboard.function_graph_mermaid') }}">Mermaid Graph</a></li>
            <li><a href="{{ url_for('dashboard.function_graph_3d') }}">3D Graph</a></li>
            <li><a href="{{ url_for('dashboard.logs_dashboard') }}">Logs</a></li>
            <li><a href="{{ url_for('dashboard.chat_page') }}">Chat</a></li>
            <!--<li><a href="{{ url_for('dashboard.log_relationship_graph') }}">Log Graph</a></li>-->
        </ul>
    </nav>
    <div class="container">
        <!-- Breadcrumb -->
        {% block breadcrumb %}{% endblock %}
        <!-- Main content -->
        {% block content %}{% endblock %}
    </div>
    {% block scripts %}{% endblock %}
</body>
</html>
```

## File: `babyagi/dashboard/templates/chat.html`
```html
{% extends "base.html" %}
{% block title %}Chat Application{% endblock %}
{% block breadcrumb %}
    <div class="breadcrumb">
        <a href="{{ url_for('dashboard.dashboard_home') }}">Home</a> &gt; Chat
    </div>
{% endblock %}
{% block content %}
    <div class="header-container">
        <h1>Function-Enhanced Chat Application</h1>
        <!-- Additional header content can be added here -->
    </div>

    <div class="main-content">
        <!-- Function Selection Section -->
        <div class="function-selection">
            <h2>Select Available Functions</h2>
            <input type="text" id="searchBar" placeholder="Search functions..." class="search-bar">
            <div id="functionList" class="function-list">
                <!-- Function items will be populated here -->
            </div>
        </div>

        <!-- Chat Section -->
        <div class="chat-container">
            <!-- Available Functions Display -->
            <div id="availableFunctionsContainer" class="available-functions-container">
                <h3>Available Functions:</h3>
                <div id="availableFunctionsList" class="available-functions-list">
                    <!-- Selected functions will be displayed here -->
                </div>
            </div>

            <div id="chatWindow" class="chat-window">
                <!-- Chat messages will be displayed here -->
            </div>
            <div class="chat-input-container">
                <textarea id="userMessage" placeholder="Type your message here..." rows="2"></textarea>
                <button id="sendMessage" class="btn btn-success">Send</button>
            </div>
        </div>
    </div>

    <!-- Function Details Modal -->
    <div id="functionModal" class="modal">
        <div class="modal-content">
            <span class="close-button">&times;</span>
            <div id="modalContent">
                <!-- Function details will be displayed here -->
            </div>
        </div>
    </div>
{% endblock %}
{% block scripts %}
    <!-- Include Marked.js for Markdown parsing -->
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>

    <style>
        /* Basic Styles */
        .header-container {
            margin-bottom: 20px;
        }
        .main-content {
            display: flex;
            flex-direction: column;
        }
        .function-selection {
            margin-bottom: 20px;
            flex-shrink: 0;
        }
        .search-bar {
            width: 100%;
            padding: 5px;
            margin-bottom: 10px;
            box-sizing: border-box;
        }
        .function-list {
            overflow-y: auto;
            max-height: calc(100vh - 400px); /* Adjust based on header and other elements */
        }
        .function-item {
            border-bottom: 1px solid #ddd;
            padding: 5px 10px;
            cursor: pointer;
            display: flex;
            align-items: center;
            transition: background-color 0.2s;
            position: relative;
        }
        .function-item:hover {
            background-color: #f0f0f0;
        }
        .function-item.selected {
            background-color: #e0f7fa;
        }
        .function-name {
            flex: 1;
            font-weight: bold;
            text-decoration: none;
            color: inherit;
        }
        .add-button {
            margin-left: 5px;
        }
        .info-button {
            background: none;
            border: none;
            cursor: pointer;
            font-size: 16px;
            margin-left: 5px;
            position: relative;
        }
        .chat-container {
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 5px;
            flex: 1;
            display: flex;
            flex-direction: column;
            max-height: calc(100vh - 400px);
            margin-top: 20px; /* Added margin to separate from function list */
        }
        .chat-window {
            flex: 1;
            overflow-y: auto;
            margin-bottom: 10px;
            padding: 5px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        .chat-message {
            margin-bottom: 10px;
        }
        .chat-message.user {
            text-align: right;
        }
        .chat-message.assistant {
            text-align: left;
        }
        .chat-input-container {
            display: flex;
            margin-top: 10px;
            padding-bottom: 10px; /* Added padding at the bottom */
        }
        #userMessage {
            flex: 1;
            resize: none;
            padding: 5px;
        }
        #sendMessage {
            margin-left: 10px;
        }
        .available-functions-container {
            margin-bottom: 20px;
        }
        .available-functions-list {
            display: flex;
            flex-wrap: wrap;
        }
        .available-function-item {
            background-color: #e0f7fa;
            padding: 5px 10px;
            margin-right: 10px;
            margin-bottom: 10px;
            border-radius: 3px;
            position: relative;
            cursor: default;
        }
        .available-function-item .remove-function {
            position: absolute;
            top: 2px;
            right: 5px;
            cursor: pointer;
            font-weight: bold;
        }
        /* Modal Styles */
        .modal {
            display: none; /* Hidden by default */
            position: fixed;
            z-index: 1000; /* Sit on top */
            left: 0;
            top: 0;
            width: 100%; /* Full width */
            height: 100%; /* Full height */
            overflow: auto;
            background-color: rgba(0,0,0,0.5); /* Black w/ opacity */
        }
        .modal-content {
            background-color: #fefefe;
            margin: 5% auto; /* 15% from the top and centered */
            padding: 20px;
            border: 1px solid #888;
            width: 80%; /* Could be more or less, depending on screen size */
            max-height: 80%;
            overflow-y: auto;
            position: relative;
        }
        .close-button {
            color: #aaa;
            float: right;
            font-size: 28px;
            font-weight: bold;
            cursor: pointer;
            position: absolute;
            right: 10px;
            top: 5px;
        }
        .close-button:hover,
        .close-button:focus {
            color: black;
            text-decoration: none;
            cursor: pointer;
        }
        /* Responsive Layout */
        @media (min-width: 768px) {
            .main-content {
                flex-direction: row;
            }
            .function-selection {
                width: 25%;
                margin-right: 20px;
            }
            .chat-container {
                width: 75%;
                margin-top: 0; /* Remove top margin in row layout */
            }
        }
    </style>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const functionListContainer = document.getElementById('functionList');
            const chatWindow = document.getElementById('chatWindow');
            const userMessageInput = document.getElementById('userMessage');
            const sendMessageButton = document.getElementById('sendMessage');
            const searchBar = document.getElementById('searchBar');
            const modal = document.getElementById('functionModal');
            const modalContent = document.getElementById('modalContent');
            const closeButton = document.querySelector('.close-button');

            let availableFunctions = [];
            let allFunctions = [];
            let chatHistory = [
                // Optionally, you can initialize with system message if needed
                // { role: 'system', message: 'You are a helpful assistant.' }
            ];

            // Function to fetch available functions using /api/functions endpoint
            function fetchFunctions() {
                fetch("{{ url_for('api.get_functions') }}", {
                    method: 'GET',
                    headers: { 'Content-Type': 'application/json' }
                })
                .then(response => response.json())
                .then(data => {
                    allFunctions = data;
                    displayFunctions(allFunctions);
                })
                .catch(error => console.error('Error fetching functions:', error));
            }

            // Function to display functions as selectable items
            function displayFunctions(functions) {
                functionListContainer.innerHTML = '';
                functions.forEach(func => {
                    console.log(func);
                    const functionItem = document.createElement('div');
                    functionItem.className = 'function-item';
                    functionItem.dataset.name = func.name;
                    functionItem.dataset.description = func.description || '';
                    functionItem.dataset.details = JSON.stringify(func);

                    const functionName = document.createElement('a');
                    functionName.className = 'function-name';
                    functionName.textContent = func.name;
                    functionName.href = '/function/' + encodeURIComponent(func.name);

                    const addButton = document.createElement('button');
                    addButton.className = 'add-button';
                    addButton.textContent = 'Add';

                    // **New Code Starts Here**
                    // Check if the function is already in availableFunctions
                    if (availableFunctions.includes(func.name)) {
                        addButton.textContent = 'Remove';
                        addButton.classList.add('remove');
                    } else {
                        addButton.textContent = 'Add';
                        addButton.classList.remove('remove');
                    }
                    // **New Code Ends Here**

                    addButton.addEventListener('click', function(event) {
                        event.stopPropagation();
                        toggleFunctionSelection(func.name);
                        if (addButton.textContent === 'Add') {
                            addButton.textContent = 'Remove';
                            addButton.classList.add('remove');
                        } else {
                            addButton.textContent = 'Add';
                            addButton.classList.remove('remove');
                        }
                    });

                    const infoButton = document.createElement('button');
                    infoButton.className = 'info-button';
                    infoButton.innerHTML = 'ℹ️';

                    // Add click event listener to open modal with function details
                    infoButton.addEventListener('click', function(event) {
                        event.stopPropagation();
                        openModal(func);
                    });

                    functionItem.appendChild(functionName);
                    functionItem.appendChild(addButton);
                    functionItem.appendChild(infoButton);

                    functionListContainer.appendChild(functionItem);

                    // Add click event listener for selecting the function item
                    functionItem.addEventListener('click', function(event) {
                        // Avoid triggering when clicking on addButton or infoButton
                        if (event.target === addButton || event.target === infoButton || infoButton.contains(event.target)) {
                            return;
                        }
                        window.location.href = '/function/' + encodeURIComponent(func.name);
                    });
                });
            }


            // Function to open modal with function details
            function openModal(func) {
                // Assemble the detailed information
                let infoContent = `<h2>${func.name}</h2>`;
                infoContent += `<strong>Version:</strong> ${func.version || 'N/A'}<br>`;
                infoContent += `<strong>Created Date:</strong> ${func.created_date || 'N/A'}<br>`;
                infoContent += `<strong>Metadata:</strong> <pre>${JSON.stringify(func.metadata, null, 2) || '{}'}<pre><br>`;
                infoContent += `<strong>Dependencies:</strong> <pre>${JSON.stringify(func.dependencies, null, 2) || '[]'}<pre><br>`;
                infoContent += `<strong>Triggers:</strong> <pre>${JSON.stringify(func.triggers, null, 2) || '[]'}<pre><br>`;
                infoContent += `<strong>Input Parameters:</strong> <pre>${JSON.stringify(func.input_parameters, null, 2) || '[]'}<pre><br>`;
                infoContent += `<strong>Output Parameters:</strong> <pre>${JSON.stringify(func.output_parameters, null, 2) || '[]'}<pre><br>`;
                infoContent += `<strong>Code:</strong><pre>${func.code || 'N/A'}</pre>`;

                modalContent.innerHTML = infoContent;
                modal.style.display = 'block';
            }

            // Close the modal when the user clicks on the close button
            closeButton.addEventListener('click', function() {
                modal.style.display = 'none';
            });

            // Close the modal when the user clicks anywhere outside of the modal content
            window.addEventListener('click', function(event) {
                if (event.target === modal) {
                    modal.style.display = 'none';
                }
            });

            // Filter functions based on search input
            searchBar.addEventListener('input', function() {
                const query = this.value.toLowerCase();
                const filteredFunctions = allFunctions.filter(func =>
                    func.name.toLowerCase().includes(query) ||
                    (func.description && func.description.toLowerCase().includes(query))
                );
                displayFunctions(filteredFunctions);
            });

            // Toggle function selection
            function toggleFunctionSelection(functionName) {
                const index = availableFunctions.indexOf(functionName);
                if (index === -1) {
                    availableFunctions.push(functionName);
                    addFunctionToAvailableList(functionName);
                } else {
                    availableFunctions.splice(index, 1);
                    removeFunctionFromAvailableList(functionName);
                }
            }

            // Add function to available functions list in UI
            function addFunctionToAvailableList(functionName) {
                const availableFunctionsList = document.getElementById('availableFunctionsList');
                const functionItem = document.createElement('div');
                functionItem.className = 'available-function-item';
                functionItem.dataset.name = functionName;
                functionItem.textContent = functionName;

                const removeButton = document.createElement('span');
                removeButton.className = 'remove-function';
                removeButton.textContent = '×';

                removeButton.addEventListener('click', function() {
                    toggleFunctionSelection(functionName);
                    // Update the add button in the function list
                    const functionItems = document.querySelectorAll('.function-item');
                    functionItems.forEach(item => {
                        if (item.dataset.name === functionName) {
                            const addButton = item.querySelector('.add-button');
                            if (addButton) {
                                addButton.textContent = 'Add';
                                addButton.classList.remove('remove');
                            }
                        }
                    });
                });

                functionItem.appendChild(removeButton);
                availableFunctionsList.appendChild(functionItem);
            }

            // Remove function from available functions list in UI
            function removeFunctionFromAvailableList(functionName) {
                const availableFunctionsList = document.getElementById('availableFunctionsList');
                const functionItems = availableFunctionsList.querySelectorAll('.available-function-item');
                functionItems.forEach(item => {
                    if (item.dataset.name === functionName) {
                        availableFunctionsList.removeChild(item);
                    }
                });
            }

            // Send user message
            sendMessageButton.addEventListener('click', function() {
                const userMessage = userMessageInput.value.trim();
                if (userMessage === '') return;

                if (availableFunctions.length === 0) {
                    alert('Please select at least one function before sending a message.');
                    return;
                }

                // Display user message
                addMessageToChat('user', userMessage);

                // Clear input
                userMessageInput.value = '';

                // Prepare parameters
                const params = {
                    chat_history: chatHistory,
                    available_function_names: availableFunctions.join(', ')
                };

                fetch("{{ url_for('api.execute_function', function_name='chat_with_functions') }}", {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(params)
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Data received from server:', data);

                    let assistantResponse;

                    if (typeof data === 'string') {
                        assistantResponse = data;
                    } else if (data.message) {
                        assistantResponse = data.message;
                    } else {
                        assistantResponse = JSON.stringify(data);
                    }

                    // Display the assistant's response
                    addMessageToChat('assistant', assistantResponse);
                })
                .catch(error => {
                    console.error('Error:', error);
                    addMessageToChat('assistant', 'Error processing your request.');
                });
            });

            // Function to add message to chat window
            function addMessageToChat(role, message) {
                if (typeof message !== 'string') {
                    message = 'No message received.';
                }

                const messageElement = document.createElement('div');
                messageElement.className = `chat-message ${role}`;

                if (role === 'assistant') {
                    // Parse Markdown
                    messageElement.innerHTML = marked.parse(message);
                } else {
                    messageElement.textContent = message;
                }

                chatWindow.appendChild(messageElement);
                chatWindow.scrollTop = chatWindow.scrollHeight;

                // Save message to chat history
                chatHistory.push({ role: role, message: message });
            }

            // Initialize by fetching functions
            fetchFunctions();
        });
    </script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/function_details.html`
```html
{% extends "base.html" %}
{% block title %}Function Details: {{ function_name }}{% endblock %}
{% block head %}
    <link rel="stylesheet" href="{{ url_for('dashboard.static', filename='css/style.css') }}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/theme/monokai.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/mode/python/python.min.js"></script>
{% endblock %}
{% block breadcrumb %}
    <div class="breadcrumb">
        <a href="{{ url_for('dashboard.dashboard_home') }}">Home</a> &gt; <span id="functionName">{{ function_name }}</span>
    </div>
{% endblock %}
{% block content %}
    <h1>Function: <span id="functionName">{{ function_name }}</span></h1>

    <div class="two-column">
        <div class="column">
            <div class="function-detail">
                <div class="section-title">Execute Function</div>
                <div id="executionForm"></div>
                <button onclick="executeFunction()" class="button">Execute</button>
                <div id="executionResult" class="execution-result"></div>
            </div>
            <div class="function-detail">
                <div class="section-title">Details</div>
                <div id="functionDetails"></div>
                <div id="functionTriggers"></div>
            </div>
        </div>

        <div class="column">
            <div class="function-detail">
                <div class="section-title">Code</div>
                <textarea id="codeEditor"></textarea>
                <button onclick="updateFunction()" class="button">Update Function</button>
            </div>

            <div class="function-detail">
                <div class="section-title">Logs</div>
                <div id="functionLogs"></div>
            </div>

            <div class="function-detail">
                <div class="section-title">
                    Versions
                </div>
                <button class="button" id="toggleVersionHistory">Show Versions</button>
                <div id="versionHistory" class="version-history" style="display: none;"></div>
            </div>
        </div>
    </div>
{% endblock %}
{% block scripts %}
    <script>
        window.functionName = "{{ function_name }}";
        window.dashboardRoute = "{{ url_for('dashboard.dashboard_home') }}";
        const apiRoutes = {
            getFunction: "{{ url_for('api.get_function', function_name=function_name) }}",
            executeFunction: "{{ url_for('api.execute_function', function_name=function_name) }}",
            getLogs: "{{ url_for('api.get_logs', function_name=function_name) }}",
            getTriggers: "{{ url_for('api.get_triggers', function_name=function_name) }}",
            getFunctionVersions: "{{ url_for('api.get_function_versions', function_name=function_name) }}",
            activateVersion: "{{ url_for('api.activate_function_version', function_name=function_name, version='VERSION_PLACEHOLDER') }}",
            updateFunction: "{{ url_for('api.update_function', function_name=function_name) }}"
        };
    </script>
    <script src="{{ url_for('dashboard.static', filename='js/function_details.js') }}"></script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/function_graph.html`
```html
{% extends "base.html" %}
{% block title %}Function Relationship Graph{% endblock %}

{% block head %}
    {{ super() }}
    <!-- Include Cytoscape.js -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.21.1/cytoscape.min.js"></script>
    <!-- Include CodeMirror CSS and JS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/theme/monokai.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/codemirror.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/codemirror/5.62.0/mode/python/python.min.js"></script>
    <!-- Page-Specific Styles -->
    <style>
        #graph {
            width: 100%;
            height: calc(100vh - 160px); /* Adjust height considering nav and breadcrumb */
            background-color: var(--background-color);
        }

        .overlay {
            position: absolute;
            background: var(--card-bg-color);
            border: 1px solid var(--border-color);
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            z-index: 10;
            top: 10px;
            right: 10px;
            width: 400px;
            height: 90vh;
            overflow-y: auto;
            display: none;
        }

        .close-btn {
            position: absolute;
            top: 10px;
            right: 10px;
            font-size: 20px;
            cursor: pointer;
            color: var(--text-color);
        }

        .toggle-menu {
            display: flex;
            justify-content: space-around;
            margin-bottom: 20px;
        }

        .toggle-menu button {
            padding: 10px;
            cursor: pointer;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 4px;
        }

        .toggle-menu button:hover {
            background-color: var(--hover-color);
        }

        .card {
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 15px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            background-color: var(--card-bg-color);
        }

        .card-title {
            font-size: 1.2em;
            margin-bottom: 10px;
            color: var(--primary-color);
        }

        .card-content {
            display: none;
        }

        .card-content.active {
            display: block;
        }

        #tab-buttons {
            display: flex;
            margin-bottom: 10px;
        }

        .tab-button {
            padding: 5px 10px;
            margin-right: 5px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            border-radius: 3px;
            cursor: pointer;
        }

        .tab-button.active {
            background-color: #007bff;
            color: white;
            border-color: #0056b3;
        }

        #tab-content {
            border: 1px solid #ccc;
            padding: 10px;
            border-radius: 3px;
        }
    </style>
{% endblock %}

{% block breadcrumb %}
    <div class="breadcrumb">
        <a href="{{ url_for('dashboard.dashboard_home') }}">Home</a> &gt; Function Graph
    </div>
{% endblock %}

{% block content %}
    <h1>Function Relationship Graph</h1>
    <div id="graph"></div>

    <!-- Overlay for Function Details -->
    <div id="overlay" class="overlay">
        <span class="close-btn" onclick="closeOverlay()">×</span>
        <div id="overlay-content">
            <h2 id="functionName"></h2>
            <!-- Tab buttons -->
            <div id="tab-buttons">
                <button class="tab-button active" onclick="showTab('description')">Description</button>
                <button class="tab-button" onclick="showTab('code')">Code</button>
                <button class="tab-button" onclick="showTab('logs')">Logs</button>
                <button class="tab-button" onclick="showTab('execute')">Execute</button>
                <button class="tab-button" onclick="showTab('versions')">Versions</button>
            </div>
            <!-- Tab content -->
            <div id="tab-content">
                <div id="description-tab">
                    <div id="functionDetails"></div>
                    <div id="functionTriggers"></div>
                </div>
                <div id="code-tab" style="display: none;">
                    <textarea id="codeEditor"></textarea>
                    <button onclick="updateFunction()" class="button">Update Function</button>
                </div>
                <div id="logs-tab" style="display: none;">
                    <div id="functionLogs"></div>
                </div>
                <div id="execute-tab" style="display: none;">
                    <div id="executionForm"></div>
                    <button onclick="executeFunction()" class="button">Execute</button>
                    <div id="executionResult" class="execution-result"></div>
                </div>
                <div id="versions-tab" style="display: none;">
                    <button class="button" id="toggleVersionHistory">Show Versions</button>
                    <div id="versionHistory" class="version-history" style="display: none;"></div>
                </div>
            </div>
        </div>
    </div>
{% endblock %}

{% block scripts %}
    {{ super() }}
    <script>
        // Define dashboardRoute correctly without _external and _scheme
        window.dashboardRoute = "{{ url_for('dashboard.dashboard_home') }}";

        // Initialize Cytoscape graph
        let cy;
        document.addEventListener('DOMContentLoaded', () => {
            cy = cytoscape({
                container: document.getElementById('graph'),
                style: [
                    {
                        selector: 'node',
                        style: {
                            'shape': 'rectangle',
                            'background-color': '#E6F2FF',
                            'label': 'data(id)',
                            'text-valign': 'center',
                            'text-halign': 'center',
                            'text-wrap': 'wrap',
                            'text-max-width': '150px',
                            'width': 'label',
                            'height': 'label',
                            'padding': '12px',
                            'font-weight': 'bold',
                            'font-size': '16px',
                            'color': '#333333',
                            'text-outline-color': '#FFFFFF',
                            'text-outline-width': 1,
                            'cursor': 'pointer'
                        }
                    },
                    {
                        selector: 'node[type="import"]',
                        style: {
                            'background-color': '#E6FFF2'  // Light green for imports
                        }
                    },
                    {
                        selector: 'node[type="trigger"]',
                        style: {
                            'background-color': '#FFE6E6'  // Light red for triggers
                        }
                    },
                    {
                        selector: 'node:hover',
                        style: {
                            'background-opacity': 0.8
                        }
                    },
                    {
                        selector: 'edge',
                        style: {
                            'width': 1,
                            'line-color': '#999999',
                            'target-arrow-color': '#999999',
                            'target-arrow-shape': 'triangle',
                            'curve-style': 'bezier',
                            'arrow-scale': 1.5
                        }
                    },
                    {
                        selector: 'edge[type="dependency"]',
                        style: {
                            'width': 2
                        }
                    },
                    {
                        selector: 'edge[type="trigger"]',
                        style: {
                            'line-style': 'dashed',
                            'label': 'trigger',
                            'font-size': '12px',
                            'text-rotation': 'autorotate',
                            'text-margin-y': -10
                        }
                    }
                ],
                layout: {
                    name: 'cose',
                    idealEdgeLength: 50,
                    nodeOverlap: 20,
                    refresh: 20,
                    fit: true,
                    padding: 30,
                    randomize: false,
                    componentSpacing: 80,
                    nodeRepulsion: 450000,
                    edgeElasticity: 100,
                    nestingFactor: 5,
                    gravity: 80,
                    numIter: 1000,
                    initialTemp: 200,
                    coolingFactor: 0.95,
                    minTemp: 1.0
                },
                wheelSensitivity: 0.2
            });

            fetch('/api/functions')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to fetch functions');
                    }
                    return response.json();
                })
                .then(data => {
                    const elements = [];
                    const imports = new Set();

                    data.forEach(func => {
                        elements.push({ data: { id: func.name, type: 'function' } });

                        func.dependencies.forEach(dep => {
                            elements.push({ data: { id: dep, type: 'function' } });
                            elements.push({ data: { source: func.name, target: dep, type: 'dependency' } });
                        });

                        func.triggers.forEach(trigger => {
                            elements.push({ data: { id: trigger, type: 'trigger' } });
                            elements.push({ data: { source: func.name, target: trigger, type: 'trigger' } });
                        });

                        func.imports.forEach(imp => imports.add(imp));
                    });

                    imports.forEach(imp => {
                        elements.push({ data: { id: imp, type: 'import' } });
                    });

                    data.forEach(func => {
                        func.imports.forEach(imp => {
                            elements.push({ data: { source: func.name, target: imp, type: 'import' } });
                        });
                    });

                    cy.add(elements);
                    cy.layout({ name: 'cose' }).run();

                    // Zoom to fit with a bit of padding
                    cy.fit(40);

                    // Add a slight zoom in
                    cy.zoom({
                        level: cy.zoom() * 1.3,
                        renderedPosition: { x: cy.width() / 2, y: cy.height() / 2 }
                    });
                })
                .catch(error => {
                    console.error('Error fetching functions:', error);
                });

            cy.on('tap', 'node', function(evt) {
                const node = evt.target;
                if (node.data('type') === 'function') {
                    showFunctionOverlay(node.id());
                }
            });

            cy.on('zoom pan', () => {
                closeOverlay();
            });
        });

        // Initialize global variables and API routes
        window.functionName = null;
        window.apiRoutes = {}; // Initialize apiRoutes as an empty object
        window.functionDetailsJsLoaded = false; // Flag to check if function_details.js is loaded

        // Update apiRoutes based on the selected function
        window.updateApiRoutes = function(functionName) {
            window.apiRoutes = {
                getFunction: `/api/function/${functionName}`,
                updateFunction: `/api/function/${functionName}`,
                executeFunction: `/api/execute/${functionName}`,
                getLogs: `/api/logs/${functionName}`,
                getFunctionVersions: `/api/function/${functionName}/versions`,
                activateVersion: (version) => `/api/function/${functionName}/versions/${version}/activate`
            };
        };

        // Function to show the overlay with function details
        function showFunctionOverlay(functionName) {
            const overlay = document.getElementById('overlay');
            document.getElementById('functionName').textContent = functionName;

            // Set global functionName
            window.functionName = functionName;

            // Update apiRoutes with the current function name
            window.updateApiRoutes(functionName);

            overlay.style.display = 'block';

            // Fetch the function data from the API
            fetch(window.apiRoutes.getFunction)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to fetch function data');
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("Fetched function data:", data);

                    if (data.error) {
                        console.error("Error fetching function data:", data.error);
                        return;
                    }

                    // Set the global functionData to the fetched data
                    window.functionData = data;

                    // Check if function_details.js is loaded
                    if (!window.functionDetailsJsLoaded) {
                        var script = document.createElement('script');
                        script.src = "{{ url_for('dashboard.static', filename='js/function_details.js') }}";
                        script.onload = function() {
                            window.functionDetailsJsLoaded = true;

                            // Call the required functions after loading the script
                            window.loadFunctionDetails();
                            window.loadFunctionLogs();

                            // Initialize CodeMirror editor
                            window.initCodeEditor();

                            // Set up version history toggle
                            const toggleVersionHistoryBtn = document.getElementById('toggleVersionHistory');
                            if (toggleVersionHistoryBtn) {
                                toggleVersionHistoryBtn.onclick = window.toggleVersionHistory;
                            }

                            // Default to showing the Description tab
                            showTab('description');
                        };
                        document.head.appendChild(script);
                    } else {
                        // If function_details.js is already loaded, just call the necessary functions
                        window.loadFunctionDetails();
                        window.loadFunctionLogs();

                        // Initialize CodeMirror editor
                        if (typeof codeEditor === 'undefined' || !codeEditor) {
                            window.initCodeEditor();
                        } else {
                            codeEditor.setValue('');
                            codeEditor.toTextArea();
                            window.initCodeEditor();
                        }

                        // Set up version history toggle
                        const toggleVersionHistoryBtn = document.getElementById('toggleVersionHistory');
                        if (toggleVersionHistoryBtn) {
                            toggleVersionHistoryBtn.onclick = window.toggleVersionHistory;
                        }

                        // Default to showing the Description tab
                        showTab('description');
                    }
                })
                .catch(error => {
                    console.error('Error fetching function data:', error);
                });
        }

        // Function to handle tab switching
        function showTab(tabName) {
            const tabs = ['description', 'code', 'logs', 'execute', 'versions'];
            tabs.forEach(tab => {
                const tabElement = document.getElementById(`${tab}-tab`);
                const tabButton = document.querySelector(`button.tab-button:nth-child(${tabs.indexOf(tab) + 1})`);
                if (tab === tabName) {
                    tabElement.style.display = 'block';
                    tabButton.classList.add('active');
                } else {
                    tabElement.style.display = 'none';
                    tabButton.classList.remove('active');
                }
            });

            // Load content for specific tabs if needed
            if (tabName === 'code' && document.getElementById('code-tab').innerHTML === '') {
                window.initCodeEditor();
            } else if (tabName === 'logs' && document.getElementById('logs-tab').innerHTML === '') {
                window.loadFunctionLogs();
            } else if (tabName === 'execute' && document.getElementById('executionForm').innerHTML === '') {
                window.createExecutionForm();
            } else if (tabName === 'versions' && document.getElementById('versionHistory').innerHTML === '') {
                window.loadFunctionVersions();
            }
        }

        // Function to close the overlay
        function closeOverlay() {
            document.getElementById('overlay').style.display = 'none';
        }

        // Function to toggle card visibility (if needed)
        function toggleCard(cardId) {
            const allCards = document.querySelectorAll('.card .card-content');
            allCards.forEach(card => card.classList.remove('active'));

            const selectedCard = document.getElementById(cardId).querySelector('.card-content');
            selectedCard.classList.add('active');
        }

        // Override the executeFunction to ensure it uses POST method
        window.executeFunction = function() {
            let params = {};
            const form = document.getElementById('executionForm');
            const inputs = form.querySelectorAll('input, textarea');
            inputs.forEach(input => {
                params[input.name] = input.value;
            });

            fetch(apiRoutes.executeFunction, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(params),
            })
            .then(response => {
                if (!response.ok) {
                    return response.text().then(text => {
                        throw new Error(text || response.statusText);
                    });
                }
                return response.json();
            })
            .then(data => {
                document.getElementById('executionResult').innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
            })
            .catch((error) => {
                console.error('Error:', error);
                document.getElementById('executionResult').innerHTML = `<pre class="error">Error executing function: ${error.message}</pre>`;
            });
        };
    </script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/function_graph_3d.html`
```html
{% extends "base.html" %}
{% block title %}3D Function Relationship Graph{% endblock %}
{% block head %}
    {{ super() }}
    <style>
        body {
            margin: 0;
            overflow: hidden;
            font-family: 'Inter', Arial, sans-serif;
        }
        #3d-graph {
            width: 100%;
            height: 100vh;
        }
        .node-label {
            background-color: white;
            padding: 5px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            position: absolute;
            display: none;
            z-index: 1;
        }
    </style>
{% endblock %}
{% block breadcrumb %}
    <div class="breadcrumb">
        <a href="{{ url_for('dashboard.dashboard_home') }}">Home</a> &gt; 3D Graph
    </div>
{% endblock %}
{% block content %}
    <div id="3d-graph"></div>
    <div id="node-label" class="node-label"></div>
{% endblock %}
{% block scripts %}
    <!-- Include the 3D Force-Directed Graph and Three.js libraries -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
    <script src="https://unpkg.com/3d-force-graph"></script>

    <script>
        // Main script to generate 3D graph

        // Fetch the data for functions and dependencies (same structure as before)
        fetch('/api/functions')
            .then(response => response.json())
            .then(data => {
                const imports = new Set();

                // Prepare the nodes and links arrays for the 3D force-directed graph
                const nodes = [];
                const links = [];

                // Map function data to nodes and edges
                data.forEach(func => {
                    nodes.push({ id: func.name, group: 'function' });

                    func.dependencies.forEach(dep => {
                        links.push({ source: func.name, target: dep, type: 'dependency' });
                    });

                    func.triggers.forEach(trigger => {
                        links.push({ source: func.name, target: trigger, type: 'trigger' });
                    });

                    func.imports.forEach(imp => imports.add(imp));
                });

                imports.forEach(imp => {
                    nodes.push({ id: imp, group: 'import' });
                });

                data.forEach(func => {
                    func.imports.forEach(imp => {
                        links.push({ source: func.name, target: imp, type: 'import' });
                    });
                });

                // Create the 3D graph using 3D Force-Directed Graph
                const Graph = ForceGraph3D()
                    (document.getElementById('3d-graph'))
                    .graphData({ nodes, links })
                    .nodeLabel('id')
                    .nodeAutoColorBy('group')
                    .linkWidth(link => link.type === 'dependency' ? 2 : 1)
                    .linkDirectionalParticles(2)
                    .linkDirectionalParticleWidth(2)
                    .nodeThreeObject(node => {
                        // Create a custom 3D object for nodes using the correct version of THREE
                        const sphereGeometry = new THREE.SphereGeometry(8, 32, 32);
                        const material = new THREE.MeshBasicMaterial({ color: node.group === 'function' ? 0x44aa88 : 0xffcc00 });
                        return new THREE.Mesh(sphereGeometry, material);
                    })
                    .onNodeClick(node => {
                        // On node click, dynamically fetch and show more information
                        expandNode(node);
                    });

                // Function to expand a node and add more details dynamically
                function expandNode(node) {
                    // Fetch the details of the clicked node (function)
                    const url = '/api/functions/' + node.id;

                    fetch(url)
                        .then(response => response.json())
                        .then(funcData => {
                            // Handle function data here
                            // You can add more nodes or display details as needed
                        })
                        .catch(error => {
                            console.error('Error fetching function details:', error);
                        });
                }
            });
    </script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/function_graph_mermaid.html`
```html
{% extends "base.html" %}
{% block title %}Function Relationship Mermaid Graph{% endblock %}

{% block head %}
    {{ super() }}
    <!-- Include Mermaid.js as an ESM module -->
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';
        
        // Initialize Mermaid with desired configuration
        mermaid.initialize({
            startOnLoad: false, // We will manually initialize after graph is inserted
            theme: 'default',
            flowchart: {
                useMaxWidth: true,
                htmlLabels: true,
                fontFamily: 'Arial, sans-serif' // Use web-safe fonts to avoid CORS issues
            }
        });
    </script>
    <style>
        /* Additional styles specific to the function_graph_mermaid.html */
        #graph {
            width: 100%;
            height: calc(100vh - 160px); /* Adjust height considering nav and breadcrumb */
            background-color: var(--background-color);
            overflow: auto;
            padding: 20px;
        }

        /* Download Button Styles */
        #download-btn {
            position: fixed;
            top: 120px; /* Adjust based on your layout */
            right: 30px;
            padding: 10px 20px;
            background-color: var(--primary-color);
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            z-index: 1001; /* Ensure it's above the graph */
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }

        #download-btn:hover {
            background-color: var(--hover-color);
        }

        /* Responsive Adjustments */
        @media (max-width: 768px) {
            #download-btn {
                top: 100px;
                right: 20px;
                padding: 8px 16px;
            }
        }

        /* Optional: Enhance node hover effects */
        .mermaid .node rect {
            cursor: pointer;
        }

        .mermaid .node:hover rect {
            stroke: var(--primary-color);
            stroke-width: 2px;
        }
    </style>
{% endblock %}

{% block breadcrumb %}
    <div class="breadcrumb">
        <a href="{{ url_for('dashboard.dashboard_home') }}">Home</a> &gt; Mermaid Graph
    </div>
{% endblock %}

{% block content %}
    <h1>Function Relationship Mermaid Graph</h1>
    <div id="graph">
        <div class="mermaid">
            %% Mermaid graph will be injected here
        </div>
    </div>
    <!-- Download Button -->
    <!-- <button id="download-btn">Download Image</button>-->
{% endblock %}

{% block scripts %}
    {{ super() }}
    <script type="module">
        import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs';

        document.addEventListener('DOMContentLoaded', () => {
            fetch('/api/functions')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Failed to fetch functions');
                    }
                    return response.json();
                })
                .then(data => {
                    let mermaidGraph = 'graph TD\n';

                    const imports = new Set();
                    const wrappers = [];  // To store functions ending with _wrapper

                    // Process each function to build the graph
                    data.forEach(func => {
                        // Prepare input and output parameters
                        const inputs = Array.isArray(func.input_parameters) && func.input_parameters.length > 0
                            ? func.input_parameters.map(param => `${param.name}: ${param.type}`).join(', ')
                            : 'None';
                        const outputs = Array.isArray(func.output_parameters) && func.output_parameters.length > 0
                            ? func.output_parameters.map(param => `${param.name}: ${param.type}`).join(', ')
                            : 'None';

                        // Multiline label using <br/> for inputs and outputs, with function name in bold
                        const label = `<b>${func.name}</b><br/>Inputs: ${inputs}<br/>Outputs: ${outputs}`;

                        if (func.name.endsWith('_wrapper')) {
                            wrappers.push(func.name);  // Add _wrapper functions to this array
                        }

                        // Define node with HTML-like labels for better formatting
                        mermaidGraph += `    ${func.name}["${label}"]\n`;

                        // Add dependencies as edges
                        func.dependencies.forEach(dep => {
                            mermaidGraph += `    ${func.name} -->|Depends on| ${dep}\n`;
                        });

                        // Add triggers as dashed edges
                        func.triggers.forEach(trigger => {
                            mermaidGraph += `    ${func.name} -.->|Triggered by| ${trigger}\n`;
                        });

                        // Collect imports
                        if (Array.isArray(func.imports)) {
                            func.imports.forEach(imp => imports.add(imp));
                        }
                    });

                    // Define Imports subgraph
                    if (imports.size > 0) {
                        mermaidGraph += `    subgraph Imports\n`;
                        imports.forEach(imp => {
                            mermaidGraph += `        ${imp}["Import: ${imp}"]\n`;
                        });
                        mermaidGraph += `    end\n`;

                        // Link functions to imports
                        data.forEach(func => {
                            if (Array.isArray(func.imports)) {
                                func.imports.forEach(imp => {
                                    mermaidGraph += `    ${func.name} -->|Uses| ${imp}\n`;
                                });
                            }
                        });
                    }

                    // Define Wrapper_Functions subgraph if any
                    if (wrappers.length > 0) {
                        mermaidGraph += `    subgraph Wrapper_Functions\n`;
                        wrappers.forEach(wrapper => {
                            mermaidGraph += `        ${wrapper}["<b>${wrapper}</b>"]\n`;
                        });
                        mermaidGraph += `    end\n`;

                        // Link wrapper functions if necessary
                        // (Add any specific links related to wrapper functions here)
                    }

                    // Inject the graph into the Mermaid container
                    const graphContainer = document.querySelector('.mermaid');
                    graphContainer.innerHTML = mermaidGraph;

                    // Render the Mermaid graph
                    mermaid.init(undefined, graphContainer);

                    // Add click event listeners to nodes for interactivity
                    // Note: Mermaid does not provide built-in click events, so we need to add them manually
                    // This approach uses SVG elements generated by Mermaid
                    // Ensure that the graph has been rendered before adding event listeners

                    // Delay to ensure Mermaid has rendered the SVG
                    setTimeout(() => {
                        const nodes = graphContainer.querySelectorAll('.node');
                        nodes.forEach(node => {
                            node.style.cursor = 'pointer'; // Change cursor to pointer
                            node.addEventListener('click', () => {
                                // Extract function name from the label
                                const rawLabel = node.querySelector('text').innerHTML;
                                const functionName = rawLabel.split('<br/>')[0].replace('<b>', '').replace('</b>', '');
                                // Optional: Implement a click handler if needed
                                // For now, we'll just alert the function name
                                alert(`Function: ${functionName}`);
                            });
                        });
                    }, 500); // Adjust delay as necessary
                })
                .catch(error => {
                    console.error('Error fetching functions:', error);
                    document.getElementById('graph').innerHTML = `<p>Error loading graph: ${error.message}</p>`;
                });
        });

        // Download Image Functionality
        document.getElementById('download-btn').addEventListener('click', () => {
            const graphContainer = document.querySelector('.mermaid');
            const svg = graphContainer.querySelector('svg');

            if (!svg) {
                alert('Graph is not loaded yet.');
                return;
            }

            const serializer = new XMLSerializer();
            const svgString = serializer.serializeToString(svg);

            // Create a canvas to draw the SVG
            const canvas = document.createElement('canvas');
            const bbox = svg.getBBox();
            canvas.width = bbox.width;
            canvas.height = bbox.height;
            const ctx = canvas.getContext('2d');

            const img = new Image();
            const svgBlob = new Blob([svgString], {type: 'image/svg+xml;charset=utf-8'});
            const url = URL.createObjectURL(svgBlob);

            img.onload = () => {
                ctx.drawImage(img, 0, 0);
                URL.revokeObjectURL(url);

                // Create a PNG data URL
                const pngUrl = canvas.toDataURL('image/png');

                // Create a temporary link to trigger download
                const downloadLink = document.createElement('a');
                downloadLink.href = pngUrl;
                downloadLink.download = 'function_relationship_graph.png';
                document.body.appendChild(downloadLink);
                downloadLink.click();
                document.body.removeChild(downloadLink);
            };

            img.onerror = (error) => {
                console.error('Error loading SVG image for download:', error);
                alert('Failed to convert graph to image.');
            };

            img.src = url;
        });
    </script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/index.html`
```html
{% extends "base.html" %}
{% block title %}Function Dashboard{% endblock %}
{% block content %}
    <h1>Function Dashboard</h1>
    <input type="text" id="searchInput" placeholder="Search functions..." onkeyup="filterTable()">
    <table id="functionTable">
        <thead>
            <tr>
                <th class="sortable" onclick="sortTable('name')">Name</th>
                <th>Version</th>
                <th>Description</th>
                <th>Input Parameters</th>
                <th>Output Parameters</th>
                <th>Dependencies</th>
                <th>Imports</th>
                <th>Triggers</th>
                <th class="sortable" onclick="sortTable('created_date')">Created Date</th>
                <th class="sortable" onclick="sortTable('total_logs')">Total Logs</th>
                <th class="sortable" onclick="sortTable('last_log_date')">Last Log Date</th>
            </tr>
        </thead>
        <tbody>
            <!-- Function rows will be dynamically inserted here -->
        </tbody>
    </table>
    <div id="functionGrid" class="function-grid">
        <!-- Function cards will be dynamically inserted here for mobile view -->
    </div>
{% endblock %}
{% block scripts %}
    <script>
        const dashboardRoute = "{{ url_for('dashboard.dashboard_home') }}";
        const apiFunctionsUrl = "{{ url_for('api.get_functions') }}";
        const apiLogsUrl = "{{ url_for('api.get_logs', function_name='') }}"; // Base URL for logs
    </script>
    <!-- Include external JavaScript -->
    <script src="{{ url_for('dashboard.static', filename='js/dashboard.js') }}"></script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/logs_dashboard.html`
```html
{% extends "base.html" %}
{% block title %}Logs Dashboard{% endblock %}
{% block breadcrumb %}
    <div class="breadcrumb">
        <a href="{{ url_for('dashboard.dashboard_home') }}">Home</a> &gt; Logs
    </div>
{% endblock %}
{% block content %}
    <h1>Logs Dashboard</h1>

    <!-- Filter Section -->
    <div class="filter-container">
        <label class="filter-label" for="functionFilter">Function:</label>
        <select id="functionFilter" class="filter-select">
            <option value="">All</option>
            <!-- Dynamic options will be populated here -->
        </select>

        <label class="filter-label" for="logTypeFilter">Log Type:</label>
        <select id="logTypeFilter" class="filter-select">
            <option value="">All</option>
            <option value="info">Info</option>
            <option value="success">Success</option>
            <option value="error">Error</option>
            <!-- Add more log types if applicable -->
        </select>

        <label class="filter-label" for="dateFilter">Date Range:</label>
        <input type="date" id="startDate" class="filter-select">
        <input type="date" id="endDate" class="filter-select">

        <button class="btn btn-primary" onclick="applyFilters()">Apply Filters</button>
        <button class="btn btn-secondary" onclick="resetFilters()">Reset Filters</button>
    </div>

    <!-- Logs Table (Desktop View) -->
    <table id="logTable" class="table table-striped table-bordered desktop-only">
        <thead>
            <tr>
                <th class="sortable" onclick="sortLogs('id')">ID</th>
                <th class="sortable" onclick="sortLogs('function_name')">Function Name</th>
                <th class="sortable" onclick="sortLogs('message')">Message</th>
                <th class="sortable" onclick="sortLogs('timestamp')">Timestamp</th>
                <th class="sortable" onclick="sortLogs('log_type')">Log Type</th>
                <th class="sortable" onclick="sortLogs('time_spent')">Time Spent (s)</th>
                <th class="sortable" onclick="sortLogs('parent_log_id')">Parent Log ID</th>
                <th class="sortable" onclick="sortLogs('triggered_by_log_id')">Triggered By Log ID</th>
            </tr>
        </thead>
        <tbody>
            <!-- Log rows will be dynamically inserted here -->
        </tbody>
    </table>

    <!-- Logs Grid (Mobile View) -->
    <div id="logGrid" class="log-grid mobile-only">
        <!-- Log cards will be dynamically inserted here -->
    </div>
{% endblock %}
{% block scripts %}
    <script>
        const dashboardRoute = "{{ url_for('dashboard.dashboard_home') }}";
        const apiLogsUrl = "{{ url_for('api.get_logs') }}";
    </script>
    <!-- Include external JavaScript -->
    <script src="{{ url_for('dashboard.static', filename='js/log_dashboard.js') }}"></script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/log_page.html`
```html
{% extends "base.html" %}
{% block title %}Log Details{% endblock %}
{% block content %}
<h1>Log Details for Log ID {{ log_id }}</h1>

<!-- Container to display the logs -->
<div id="logContainer"></div>
{% endblock %}

{% block scripts %}
<style>
    /* CSS Styles */
    .log-entry {
        margin-left: 20px;
        border-left: 1px solid #ccc;
        padding-left: 10px;
        position: relative;
    }

    .log-entry::before {
        content: '';
        position: absolute;
        left: -1px;
        top: 0;
        bottom: 0;
        width: 1px;
        background: #ccc;
    }

    .log-header {
        font-weight: bold;
        display: flex;
        align-items: center;
    }

    .log-status {
        width: 12px;
        height: 12px;
        border-radius: 50%;
        margin-right: 10px;
    }

    .log-status-success {
        background-color: green;
    }

    .log-status-error {
        background-color: red;
    }

    .log-status-other {
        background-color: yellow;
    }

    .log-details {
        margin-top: 5px;
        display: none; /* Hidden by default */
        background-color: #f9f9f9;
        padding: 10px;
    }

    .toggle-button {
        color: blue;
        cursor: pointer;
        text-decoration: underline;
        margin-left: 10px;
    }

    pre {
        background-color: #f4f4f4;
        padding: 10px;
        overflow: auto;
    }
</style>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const logId = {{ log_id }};
        const apiLogBundleUrl = '/api/log_bundle/' + logId;

        fetch(apiLogBundleUrl)
        .then(response => {
            if (!response.ok) {
                throw new Error(`Error ${response.status}: ${response.statusText}`);
            }
            return response.json();
        })
        .then(data => {
            const logs = data.logs;
            if (!logs || logs.length === 0) {
                document.getElementById('logContainer').innerHTML = '<p>No logs found.</p>';
                return;
            }

            const logsById = {};
            logs.forEach(log => {
                log.children = [];
                logsById[log.id] = log;
            });

            // Build the tree by assigning children to their respective parents
            logs.forEach(log => {
                if (log.parent_log_id !== null && logsById[log.parent_log_id]) {
                    logsById[log.parent_log_id].children.push(log);
                }
            });
    
            // Identify all root logs (logs without a parent in the fetched bundle)
            const rootLogs = logs.filter(log => log.parent_log_id === null || !logsById[log.parent_log_id]);
    
            const logContainer = document.getElementById('logContainer');
            rootLogs.forEach(log => {
                renderLog(logContainer, log);
            });
        })
        .catch(error => {
            console.error('Error fetching log bundle:', error);
            document.getElementById('logContainer').innerHTML = `<p>Error loading log bundle: ${error.message}</p>`;
        });

        function renderLog(container, log, depth = 0) {
            const div = document.createElement('div');
            div.className = 'log-entry';
            div.style.marginLeft = (depth * 20) + 'px';

            const header = document.createElement('div');
            header.className = 'log-header';

            const statusDiv = document.createElement('div');
            statusDiv.className = 'log-status ' + getLogStatusClass(log.log_type);
            header.appendChild(statusDiv);

            const messageSpan = document.createElement('span');
            messageSpan.textContent = `${log.function_name}: ${log.message}`;

            const toggleButton = document.createElement('span');
            toggleButton.className = 'toggle-button';
            toggleButton.textContent = '[Show Details]';
            toggleButton.addEventListener('click', function() {
                if (detailsDiv.style.display === 'none') {
                    detailsDiv.style.display = 'block';
                    toggleButton.textContent = '[Hide Details]';
                } else {
                    detailsDiv.style.display = 'none';
                    toggleButton.textContent = '[Show Details]';
                }
            });

            header.appendChild(messageSpan);
            header.appendChild(toggleButton);
            div.appendChild(header);

            const detailsDiv = document.createElement('div');
            detailsDiv.className = 'log-details';

            // Handle null or undefined params/output
            const params = log.params ? JSON.stringify(log.params, null, 2) : 'N/A';
            const output = log.output ? JSON.stringify(log.output, null, 2) : 'N/A';

            detailsDiv.innerHTML = `
                <p><strong>ID:</strong> ${log.id}</p>
                <p><strong>Timestamp:</strong> ${new Date(log.timestamp).toLocaleString()}</p>
                <p><strong>Log Type:</strong> ${log.log_type}</p>
                <p><strong>Time Spent:</strong> ${log.time_spent ? log.time_spent.toFixed(3) + ' s' : 'N/A'}</p>
                <p><strong>Parent Log ID:</strong> ${log.parent_log_id !== null ? log.parent_log_id : 'N/A'}</p>
                <p><strong>Triggered By Log ID:</strong> ${log.triggered_by_log_id !== null ? log.triggered_by_log_id : 'N/A'}</p>
                <p><strong>Params:</strong></p>
                <pre>${params}</pre>
                <p><strong>Output:</strong></p>
                <pre>${output}</pre>
            `;

            div.appendChild(detailsDiv);

            container.appendChild(div);

            // Recursively render children
            if (log.children && log.children.length > 0) {
                log.children.forEach(childLog => {
                    renderLog(container, childLog, depth + 1);
                });
            }
        }

        function getLogStatusClass(logType) {
            switch (logType.toLowerCase()) {
                case 'success':
                    return 'log-status-success';
                case 'error':
                    return 'log-status-error';
                default:
                    return 'log-status-other';
            }
        }
    });
</script>
{% endblock %}
```

## File: `babyagi/dashboard/templates/log_relationship_graph.html`
```html
{% extends "base.html" %}
{% block title %}Log Relationship Graph{% endblock %}
{% block breadcrumb %}
    <div class="breadcrumb">
        <a href="{{ url_for('dashboard.dashboard_home') }}">Home</a> &gt; Log Graph
    </div>
{% endblock %}
{% block content %}
    <h1>Log Relationship Graph</h1>
    <div class="controls">
        <input type="text" id="functionName" placeholder="Function name (optional)">
        <input type="datetime-local" id="startDate" placeholder="Start date">
        <input type="datetime-local" id="endDate" placeholder="End date">
        <button onclick="loadLogs()">Load Logs</button>
    </div>
    <div id="graph"></div>
    <div class="legend">
        <div class="legend-item">
            <div class="legend-color" style="background-color: #3366cc;"></div>
            <span>Parent Relationship</span>
        </div>
        <div class="legend-item">
            <div class="legend-color" style="background-color: #dc3912; border-top: 2px dashed #dc3912;"></div>
            <span>Trigger Relationship</span>
        </div>
    </div>
    <div id="overlay" class="overlay">
        <div class="overlay-content">
            <span class="close-btn" onclick="closeOverlay()">&times;</span>
            <h2 id="logTitle"></h2>
            <pre id="logContent"></pre>
        </div>
    </div>
{% endblock %}
{% block scripts %}
    <script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.21.1/cytoscape.min.js"></script>
    <script>
        const apiLogsUrl = "{{ url_for('api.get_logs') }}";
    </script>
    <script src="{{ url_for('dashboard.static', filename='js/log_graph.js') }}"></script>
{% endblock %}
```

## File: `babyagi/functionz/__init__.py`
```python
from .core.framework import func

__all__ = ['func']
```

## File: `babyagi/functionz/core/execution.py`
```python
import subprocess
import sys
import importlib
import inspect
from typing import Any, Dict, List, Optional
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class FunctionExecutor:
    def __init__(self, python_func):
        self.python_func = python_func

    def _install_external_dependency(self, package_name: str, imp_name: str) -> Any:
        try:
            return importlib.import_module(imp_name)
        except ImportError:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
            return importlib.import_module(package_name)

    def _resolve_dependencies(self, function_version: Dict[str, Any], local_scope: Dict[str, Any],
                              parent_log_id: Optional[int], executed_functions: List[str],
                              visited: Optional[set] = None) -> None:
        if visited is None:
            visited = set()

        function_name = function_version['name']
        function_imports = self.python_func.db.get_function_imports(function_name)

        for imp in function_imports:
            lib_name = imp['lib'] if imp['lib'] else imp['name']
            if lib_name not in local_scope:
                module = self._install_external_dependency(lib_name, imp['name'])
                local_scope[imp['name']] = module

        for dep_name in function_version.get('dependencies', []):
            if dep_name not in local_scope and dep_name not in visited:
                visited.add(dep_name)
                dep_data = self.python_func.db.get_function(dep_name)
                if not dep_data:
                    raise ValueError(f"Dependency '{dep_name}' not found in the database.")
                self._resolve_dependencies(dep_data, local_scope, parent_log_id, executed_functions, visited)
                exec(dep_data['code'], local_scope)
                if dep_name in local_scope:
                    dep_func = local_scope[dep_name]
                    # Wrap the dependent function
                    local_scope[dep_name] = self._create_function_wrapper(dep_func, dep_name, parent_log_id, executed_functions)

    def _create_function_wrapper(self, func: callable, func_name: str, parent_log_id: int, executed_functions: List[str]):
        def wrapper(*args, **kwargs):
            return self.execute(func_name, *args, executed_functions=executed_functions, parent_log_id=parent_log_id, **kwargs)
        return wrapper

    def execute(
        self,
        function_name: str,
        *args,
        executed_functions: Optional[List[str]] = None,
        parent_log_id: Optional[int] = None,
        wrapper_log_id: Optional[int] = None,
        triggered_by_log_id: Optional[int] = None,
        **kwargs
    ) -> Any:
        start_time = datetime.now()
        executed_functions = executed_functions or []
        log_id = None
        bound_args = None
        output = None

        # Ensure wrapper_log_id is initialized
        wrapper_log_id = wrapper_log_id if wrapper_log_id is not None else None

        logger.info(f"Executing function: {function_name}")

        try:
            executed_functions.append(function_name)
            function_version = self.python_func.db.get_function(function_name)
            if not function_version:
                raise ValueError(f"Function '{function_name}' not found in the database.")

            # If the function being executed is the wrapper, create a special log entry and set wrapper_log_id
            if function_name == 'execute_function_wrapper':
                log_id = self._add_execution_log(
                    function_name,
                    start_time,
                    {},
                    None,
                    0,
                    parent_log_id,
                    triggered_by_log_id,
                    'started'
                )
                wrapper_log_id = log_id
            else:
                log_id = self._add_execution_log(
                    function_name,
                    start_time,
                    {},
                    None,
                    0,
                    wrapper_log_id if wrapper_log_id else parent_log_id,
                    triggered_by_log_id,
                    'started'
                )

            # Include 'datetime' in local_scope
            local_scope = {
                'func': self.python_func,
                'parent_log_id': log_id,
                'datetime': datetime  # Added datetime here
            }

            self._resolve_dependencies(
                function_version,
                local_scope,
                parent_log_id=log_id,
                executed_functions=executed_functions
            )
            self._inject_secret_keys(local_scope)

            exec(function_version['code'], local_scope)
            if function_name not in local_scope:
                raise ValueError(f"Failed to load function '{function_name}'.")

            func = local_scope[function_name]
            bound_args = self._bind_function_arguments(func, args, kwargs)
            self._validate_input_parameters(function_version, bound_args)

            params = bound_args.arguments
            self._update_execution_log_params(log_id, params)

            output = func(*bound_args.args, **bound_args.kwargs)
            end_time = datetime.now()
            time_spent = (end_time - start_time).total_seconds()

            self._update_execution_log(log_id, output, time_spent, 'success')

            # Check and execute triggers for the function
            self._execute_triggered_functions(function_name, output, executed_functions, log_id)
            return output

        except Exception as e:
            end_time = datetime.now()
            time_spent = (end_time - start_time).total_seconds()
            if log_id is not None:
                self._update_execution_log(log_id, None, time_spent, 'error', str(e))
            raise

    

    def _check_key_dependencies(self, function_version: Dict[str, Any]) -> None:
        if 'key_dependencies' in function_version.get('metadata', {}):
            for key_name in function_version['metadata']['key_dependencies']:
                if key_name not in self.python_func.db.get_all_secret_keys():
                    raise ValueError(f"Required secret key '{key_name}' not found for function '{function_version['name']}'")

    def _inject_secret_keys(self, local_scope: Dict[str, Any]) -> None:
        secret_keys = self.python_func.db.get_all_secret_keys()
        if secret_keys:
            logger.debug(f"Injecting secret keys: {list(secret_keys.keys())}")
            local_scope.update(secret_keys)

    def _bind_function_arguments(self, func: callable, args: tuple, kwargs: dict) -> inspect.BoundArguments:
        sig = inspect.signature(func)
        bound_args = sig.bind(*args, **kwargs)
        bound_args.apply_defaults()
        return bound_args

    def _validate_input_parameters(self, function_version: Dict[str, Any], bound_args: inspect.BoundArguments) -> None:
        input_params = function_version.get('input_parameters', [])
        for param in input_params:
            if param['name'] not in bound_args.arguments:
                raise ValueError(f"Missing required input parameter '{param['name']}' for function '{function_version['name']}'")

    def _add_execution_log(self, function_name: str, start_time: datetime, params: Dict[str, Any],
                           output: Any, time_spent: float, parent_log_id: Optional[int],
                           triggered_by_log_id: Optional[int], log_type: str, error_message: Optional[str] = None) -> int:
        if log_type == 'started':
            message = "Execution started."
        elif log_type == 'success':
            message = "Execution successful."
        else:
            message = f"Execution failed. Error: {error_message}"
        return self.python_func.db.add_log(
            function_name=function_name,
            message=message,
            timestamp=start_time,
            params=params,
            output=output,
            time_spent=time_spent,
            parent_log_id=parent_log_id,
            triggered_by_log_id=triggered_by_log_id,
            log_type=log_type
        )

    def _update_execution_log(self, log_id: int, output: Any, time_spent: float, log_type: str,
          error_message: Optional[str] = None):
        message = "Execution successful." if log_type == 'success' else f"Execution failed. Error: {error_message}"
        update_data = {
            'message': message,
            'log_type': log_type
        }
        if output is not None:
            update_data['output'] = output
        if time_spent is not None:
            update_data['time_spent'] = time_spent

            self.python_func.db.update_log(log_id=log_id, **update_data)


    def _update_execution_log_params(self, log_id: int, params: Dict[str, Any]) -> None:
        self.python_func.db.update_log(log_id=log_id, params=params)


    
    def _execute_triggered_functions(self, function_name: str, output: Any, executed_functions: List[str], log_id: int) -> None:
        triggered_function_names = self.python_func.db.get_triggers_for_function(function_name)
        logger.info(f"Functions triggered by {function_name}: {triggered_function_names}")

        for triggered_function_name in triggered_function_names:
            if triggered_function_name in executed_functions:
                logger.warning(f"Triggered function '{triggered_function_name}' already executed in this chain. Skipping to prevent recursion.")
                continue

            try:
                logger.info(f"Preparing to execute trigger: {triggered_function_name}")
                triggered_function = self.python_func.db.get_function(triggered_function_name)
                if triggered_function:
                    trigger_args, trigger_kwargs = self._prepare_trigger_arguments(triggered_function, output)
                    logger.info(f"Executing trigger {triggered_function_name} with args: {trigger_args} and kwargs: {trigger_kwargs}")

                    trigger_output = self.execute(
                        triggered_function_name,
                        *trigger_args,
                        executed_functions=executed_functions.copy(),
                        parent_log_id=log_id,
                        triggered_by_log_id=log_id,
                        **trigger_kwargs
                    )
                    logger.info(f"Trigger {triggered_function_name} execution completed. Output: {trigger_output}")
                else:
                    logger.error(f"Triggered function '{triggered_function_name}' not found in the database.")
            except Exception as e:
                logger.error(f"Error executing triggered function '{triggered_function_name}': {str(e)}")

    def _prepare_trigger_arguments(self, triggered_function: Dict[str, Any], output: Any) -> tuple:
        triggered_params = triggered_function.get('input_parameters', [])
        if triggered_params:
            # If the triggered function expects parameters, pass the output as the first parameter
            return (output,), {}
        else:
            # If the triggered function doesn't expect parameters, don't pass any
            return (), {}
```

## File: `babyagi/functionz/core/framework.py`
```python
# core/framework.py

import os
import sys
import importlib.util
from typing import Optional, List, Dict, Any
from datetime import datetime
import logging

from ..db.db_router import DBRouter
from .execution import FunctionExecutor
from .registration import FunctionRegistrar

logger = logging.getLogger(__name__)

class Functionz:
    def __init__(self, db_type='local', **db_kwargs):
        self.db = DBRouter(db_type, **db_kwargs)
        self.executor = FunctionExecutor(self)
        self.registrar = FunctionRegistrar(self)

    # Function execution
    def execute_function(self, function_name: str, *args, **kwargs):
        return self.executor.execute(function_name, *args, **kwargs)

    def __getattr__(self, name):
        if self.db.get_function(name):
            return lambda *args, **kwargs: self.executor.execute(name, *args, **kwargs)
        raise AttributeError(f"'PythonFunc' object has no attribute '{name}'")

    # Function management
    def get_function(self, name: str):
        return self.db.get_function(name)

    def get_function_versions(self, name: str):
        return self.db.get_function_versions(name)

    def get_all_functions(self) -> List[Dict[str, Any]]:
        return self.db.get_all_functions()

    def activate_function_version(self, name: str, version: int) -> None:
        self.db.activate_function_version(name, version)

    def get_function_imports(self, name: str):
        return self.db.get_function_imports(name)

    # Function registration (exposing registrar methods)
    def register_function(self, *args, **kwargs):
        return self.registrar.register_function(*args, **kwargs)

    def update_function(self, *args, **kwargs):
        return self.registrar.update_function(*args, **kwargs)

    def add_function(self, *args, **kwargs):
        return self.registrar.add_function(*args, **kwargs)

    # Key management
    def add_key(self, key_name: str, key_value: str) -> None:
        self.db.add_secret_key(key_name, key_value)

    def get_all_secret_keys(self, *args, **kwargs):
        return self.db.get_all_secret_keys(*args, **kwargs)

    # Import management
    def get_all_imports(self, *args, **kwargs):
        return self.db.get_all_imports(*args, **kwargs)

    # Function pack and file loading
    def load_function_pack(self, pack_name: str):
        packs_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'packs')
        pack_path = os.path.join(packs_dir, pack_name + '.py')

        if not os.path.exists(pack_path):
            logger.error(f"Function pack '{pack_name}' not found.")
            return

        self._load_module_from_path(pack_path, pack_name)

    def load_functions_from_file(self, file_path: str):
        if not os.path.exists(file_path):
            logger.error(f"File '{file_path}' not found.")
            return

        module_name = os.path.splitext(os.path.basename(file_path))[0]
        self._load_module_from_path(file_path, module_name)

    def _load_module_from_path(self, path: str, module_name: str):
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        module.func = self

        original_sys_path = sys.path[:]
        try:
            babyagi_root = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
            if babyagi_root not in sys.path:
                sys.path.insert(0, babyagi_root)

            spec.loader.exec_module(module)
            logger.info(f"Loaded module '{module_name}' from '{path}'")
        except Exception as e:
            logger.error(f"Error loading module '{module_name}' from '{path}': {str(e)}")
            import traceback
            logger.error(traceback.format_exc())
        finally:
            sys.path = original_sys_path

    # Trigger management
    def add_trigger(self, triggered_function_name, triggering_function_name=None):
        self.db.add_trigger(triggered_function_name, triggering_function_name)

    def get_triggers_for_function(self, function_name: str) -> List[str]:
        function_data = self.get_function(function_name)
        return function_data.get('triggers', []) if function_data else []

    # Logging and display
    def get_logs(self, function_name: Optional[str] = None,
                 start_date: Optional[datetime] = None,
                 end_date: Optional[datetime] = None) -> List[Dict[str, Any]]:
        return self.db.get_logs(function_name, start_date, end_date)

    def display(self):
        functions = self.db.get_all_functions()
        result = []

        for function in functions:
            function_info = [
                f"Function: {function['name']}",
                f"  Version: {function['version']}",
                f"  Created Date: {function['created_date']}",
                f"  Metadata: {function['metadata']}",
                f"  Dependencies: {function['dependencies']}",
                f"  Triggers: {function.get('triggers', [])}",
                "  Input Parameters:",
            ]
            for param in function['input_parameters']:
                function_info.append(f"    - {param['name']} ({param['type']})")

            function_info.append("  Output Parameters:")
            for param in function['output_parameters']:
                function_info.append(f"    - {param['name']} ({param['type']})")

            function_info.append(f"  Code:\n{function['code']}")
            function_info.append("---")

            result.append("\n".join(function_info))

        return "\n\n".join(result)

# Create the global 'func' instance
func = Functionz()
```

## File: `babyagi/functionz/core/registration.py`
```python
# core/registration.py

from .execution import FunctionExecutor
import inspect
import ast
from typing import Optional, List, Dict, Any, Union
import logging
import json

logger = logging.getLogger(__name__)

class FunctionRegistrar:
    def __init__(self, python_func):
        self.python_func = python_func

    def register_function(self, metadata: Optional[Dict[str, Any]] = None,
                          imports: Optional[List[str]] = None,
                          dependencies: Optional[List[str]] = None,
                          triggers: Optional[List[str]] = None,
                          key_dependencies: Optional[List[str]] = None):
        """Decorator to register a function."""
        def decorator(func):
            function_name = func.__name__
            source_lines = inspect.getsourcelines(func)[0]
            func_start = next(i for i, line in enumerate(source_lines) if line.strip().startswith('def '))
            function_code = ''.join(source_lines[func_start:]).strip()

            # Store metadata on the function object
            func.__pythonfunc_metadata__ = {
                'metadata': metadata or {},
                'imports': imports or [],
                'dependencies': dependencies or [],
                'triggers': triggers or [], 
                'key_dependencies': key_dependencies or []
            }

            self.add_function(function_name, metadata=metadata, code=function_code,
                              imports=imports, dependencies=dependencies, 
                              key_dependencies=key_dependencies, triggers=triggers)
            def wrapper(*args, **kwargs):
                return self.python_func.executor.execute(function_name, *args, **kwargs)
            return wrapper
        return decorator

    def parse_function_parameters(self, code: str):
        """
        Parse the input and output parameters of a given function code.
        """
        try:
            # Parse the source code into an AST
            tree = ast.parse(code)

            # Find the function definition node
            function_def = next(node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef))

            # Parse input parameters
            input_params = []
            for arg in function_def.args.args:
                param_type = 'Any'
                if arg.annotation:
                    param_type = ast.unparse(arg.annotation)
                input_params.append({'name': arg.arg, 'type': param_type})

            # Parse return statement to identify output parameters
            output_params = []
            returns = [node for node in ast.walk(function_def) if isinstance(node, ast.Return)]
            if returns:
                return_node = returns[0].value
                if isinstance(return_node, ast.Dict):
                    # If returning a dictionary, treat each key as an output parameter
                    for key in return_node.keys:
                        if isinstance(key, ast.Str):
                            output_params.append({'name': key.s, 'type': 'Any'})
                elif isinstance(return_node, (ast.Name, ast.Attribute)):
                    # If returning a single variable
                    output_params.append({'name': 'output', 'type': 'Any'})
                elif isinstance(return_node, ast.Str):
                    # If returning a string literal
                    output_params.append({'name': 'output', 'type': 'str'})
                else:
                    # For other types of returns, use a generic 'output' parameter
                    output_params.append({'name': 'output', 'type': 'Any'})

            return input_params, output_params
        except Exception as e:
            # print(f"Error parsing function parameters: {str(e)}")
            return [], []

    def parse_import(self, imp):
        try:
            #print("Attempt to parse the string as JSON")
            #print(imp.type())
            parsed = json.loads(imp)
            #print("Parsed string as JSON")
            return parsed
        except json.JSONDecodeError:
            print("Failed to parse the string as JSON")
            # If it fails, return the original string (it's a simple import)
            return imp

    # Register imports helper function
    def register_imports(self, imports):
        print(f"Registering imports: {imports}")
        if isinstance(imports, list):
            for imp in imports:
                self.process_single_import(imp)
        elif isinstance(imports, dict):
            self.process_single_import(imports)

    def process_single_import(self, imp):
        if isinstance(imp, str):
            self.python_func.db.add_import(imp, 'external', lib=None)
        elif isinstance(imp, dict):
            name = imp.get('name')
            lib = imp.get('lib')
            if name:
                self.python_func.db.add_import(name, 'external', lib=lib)
        else:
            print(f"Unsupported import format: {imp}")

    def process_imports(self, imports):
        import_names = []
        if imports:
            if isinstance(imports, list):
                for imp in imports:
                    if isinstance(imp, str):
                        import_names.append(imp)
                    elif isinstance(imp, dict):
                        import_name = imp.get('name')
                        if import_name:
                            import_names.append(import_name)
            elif isinstance(imports, dict):
                import_name = imports.get('name')
                if import_name:
                    import_names.append(import_name)
        return import_names

    def function_has_no_changes(self, name, code, metadata, import_names, dependencies, triggers):
        existing_function = self.python_func.db.get_function(name)
        if not existing_function:
            return False  # Function does not exist, so changes are needed

        existing_code = existing_function.get('code')
        existing_metadata = existing_function.get('metadata', {})
        existing_description = existing_metadata.get('description')
        existing_imports = existing_function.get('imports') or []
        existing_dependencies = existing_function.get('dependencies') or []
        existing_triggers = existing_function.get('triggers') or []

        new_description = metadata.get('description') if metadata else None

        if (existing_code == code and
            existing_description == new_description and
            set(existing_imports) == set(import_names) and
            set(existing_dependencies) == set(dependencies) and
            set(existing_triggers) == set(triggers)):
            return True  # No changes
        else:
            return False  # Changes detected

    def add_function(self, name: str, metadata: Optional[Dict[str, Any]] = None,
                    code: Optional[str] = None, imports: Optional[List[Union[str, Dict[str, str]]]] = None,
                    dependencies: Optional[List[str]] = None, triggers: Optional[List[str]] = None,
                    key_dependencies: Optional[List[str]] = None,
                    input_parameters: Optional[List[Dict[str, str]]] = None,
                    output_parameters: Optional[List[Dict[str, str]]] = None) -> None:

        if code:
            # Parse input and output parameters if not provided
            if input_parameters is None or output_parameters is None:
                parsed_input, parsed_output = self.parse_function_parameters(code)
                input_parameters = input_parameters or parsed_input
                output_parameters = output_parameters or parsed_output

        # Process imports
        import_names = self.process_imports(imports)

        # Ensure lists are not None
        dependencies = dependencies or []
        triggers = triggers or []

        # Check for changes
        if self.function_has_no_changes(name, code, metadata, import_names, dependencies, triggers):
            #print(f"Function {name} has no changes.")
            return

        # Register imports
        if imports:
            self.register_imports(imports)

        # Add or update the function in the database
        existing_function = self.python_func.db.get_function(name)
        if existing_function:
            # Function exists, update it
            self.python_func.db.update_function(
                name, code=code, metadata=metadata, dependencies=dependencies,
                input_parameters=input_parameters, output_parameters=output_parameters,
                imports=import_names, triggers=triggers
            )
        else:
            # Function does not exist, add it
            self.python_func.db.add_function(
                name, code=code, metadata=metadata, dependencies=dependencies,
                input_parameters=input_parameters, output_parameters=output_parameters,
                imports=import_names, triggers=triggers
            )

        if key_dependencies:
            print(f"Function {name} requires keys: {key_dependencies}")
            metadata = metadata or {}
            metadata['key_dependencies'] = key_dependencies

        if self.python_func.db.get_function('function_added_or_updated'):
            try:
                action = 'updated' if existing_function else 'added'
                self.python_func.executor.execute(function_name='function_added_or_updated', action=action, triggered_function_name=name)
            except Exception as e:
                logger.error(f"Error executing trigger function 'function_added_or_updated': {str(e)}")

    def update_function(self, name: str, code: Optional[str] = None, imports: Optional[List[Union[str, Dict[str, str]]]] = None,
                        metadata: Optional[Dict[str, Any]] = None,
                        dependencies: Optional[List[str]] = None,
                        triggers: Optional[List[str]] = None,
                        key_dependencies: Optional[List[str]] = None,
                        input_parameters: Optional[List[Dict[str, str]]] = None,
                        output_parameters: Optional[List[Dict[str, str]]] = None) -> None:

        if code:
            # Parse input and output parameters if not provided
            if input_parameters is None or output_parameters is None:
                parsed_input, parsed_output = self.parse_function_parameters(code)
                input_parameters = input_parameters or parsed_input
                output_parameters = output_parameters or parsed_output

        # Process imports
        import_names = self.process_imports(imports)

        # Ensure lists are not None
        dependencies = dependencies or []
        triggers = triggers or []

        # Check for changes
        if self.function_has_no_changes(name, code, metadata, import_names, dependencies, triggers):
            # print(f"Function {name} has no changes.")
            return

        # Update the function in the database
        self.python_func.db.update_function(
            name, code=code, metadata=metadata, dependencies=dependencies,
            input_parameters=input_parameters, output_parameters=output_parameters,
            imports=import_names, triggers=triggers
        )

        if key_dependencies:
            metadata = metadata or {}
            metadata['key_dependencies'] = key_dependencies

        # Register imports
        if imports:
            self.register_imports(imports)

        if self.python_func.db.get_function('function_added_or_updated'):
            try:
                self.python_func.executor.execute(function_name='function_added_or_updated', action='updated', triggered_function_name=name)
            except Exception as e:
                logger.error(f"Error executing trigger function 'function_added_or_updated': {str(e)}")
```

## File: `babyagi/functionz/db/base_db.py`
```python
from abc import ABC, abstractmethod
from typing import Optional, List, Dict, Any
from datetime import datetime

class BaseDB(ABC):
    # Function management
    @abstractmethod
    def add_function(self, name: str, code: str, metadata: Optional[Dict[str, Any]] = None,
                     dependencies: Optional[List[str]] = None,
                     input_parameters: Optional[List[Dict[str, Any]]] = None,
                     output_parameters: Optional[List[Dict[str, Any]]] = None) -> None:
        pass

    @abstractmethod
    def get_function(self, name: str) -> Optional[Dict[str, Any]]:
        pass

    @abstractmethod
    def get_all_functions(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def update_function(self, name: str, code: Optional[str] = None,
                        metadata: Optional[Dict[str, Any]] = None,
                        dependencies: Optional[List[str]] = None,
                        input_parameters: Optional[List[Dict[str, Any]]] = None,
                        output_parameters: Optional[List[Dict[str, Any]]] = None) -> None:
        pass

    @abstractmethod
    def remove_function(self, name: str) -> None:
        pass

    @abstractmethod
    def get_function_versions(self, name: str) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def activate_function_version(self, name: str, version: int) -> None:
        pass

    # Import management
    @abstractmethod
    def add_import(self, name: str, source: str, lib: Optional[str] = None) -> None:
        pass

    @abstractmethod
    def get_all_imports(self) -> List[Dict[str, Any]]:
        pass

    # Logging
    @abstractmethod
    def add_log(self, function_name: str, message: str, timestamp: datetime,
                params: Optional[Dict[str, Any]] = None,
                output: Optional[Any] = None,
                time_spent: Optional[float] = None) -> None:
        pass

    @abstractmethod
    def get_logs(self, function_name: Optional[str] = None,
                 start_date: Optional[datetime] = None,
                 end_date: Optional[datetime] = None) -> List[Dict[str, Any]]:
        pass
```

## File: `babyagi/functionz/db/db_router.py`
```python
from typing import List, Optional, Dict, Any
from contextlib import contextmanager
from datetime import datetime

from .local_db import LocalDB
from .base_db import BaseDB
from .models import Import, Function, FunctionVersion, Log

class ImportResult:
    def __init__(self, name: str, source: str):
        self.name = name
        self.source = source

class DBRouter(BaseDB):
    def __init__(self, db_type: str = 'local', **kwargs):
        if db_type == 'local':
            self.db = LocalDB(**kwargs)
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

    @contextmanager
    def session_scope(self):
        with self.db.session_scope() as session:
            yield session

    # Function management
    def add_function(self, name: str, code: str, metadata: Optional[Dict[str, Any]] = None, 
                     dependencies: Optional[List[str]] = None, 
                     triggers: Optional[List[str]] = None,
                     input_parameters: Optional[List[Dict[str, str]]] = None,
                     output_parameters: Optional[List[Dict[str, str]]] = None,
                     imports: Optional[List[str]] = None) -> None:
        with self.session_scope() as session:
            self.db.add_or_update_function(session, name, code, metadata, dependencies, triggers, input_parameters, output_parameters, imports)

    def update_function(self, name: str, code: Optional[str] = None, 
                        metadata: Optional[Dict[str, Any]] = None, 
                        dependencies: Optional[List[str]] = None,
                        triggers: Optional[List[str]] = None,
                        input_parameters: Optional[List[Dict[str, str]]] = None,
                        output_parameters: Optional[List[Dict[str, str]]] = None,
                        imports: Optional[List[str]] = None) -> None:
        with self.session_scope() as session:
            function = self.db.get_function(session, name)
            if function:
                active_version = self.db.get_active_version(session, function)
                self.db.add_or_update_function(
                    session, name, 
                    code if code is not None else active_version.code,
                    metadata or active_version.function_metadata,
                    dependencies, 
                    triggers if triggers is not None else active_version.triggers,
                    input_parameters or active_version.input_parameters,
                    output_parameters or active_version.output_parameters,
                    imports
                )

    def get_function(self, name: str) -> Optional[Dict[str, Any]]:
        with self.session_scope() as session:
            function = self.db.get_function(session, name)
            if function:
                active_version = self.db.get_active_version(session, function)
                if active_version:
                    return {
                        'name': function.name,
                        'version': active_version.version,
                        'code': active_version.code,
                        'metadata': active_version.function_metadata,
                        'dependencies': [dep.name for dep in active_version.dependencies],
                        'imports': [imp.name for imp in active_version.imports],
                        'created_date': active_version.created_date.isoformat(),
                        'input_parameters': active_version.input_parameters,
                        'output_parameters': active_version.output_parameters,
                        'triggers': active_version.triggers
                    }
            return None

    def get_all_functions(self) -> List[Dict[str, Any]]:
        with self.session_scope() as session:
            functions = self.db.get_all_functions(session)
            return [
                {
                    'name': function.name,
                    'version': active_version.version,
                    'code': active_version.code,
                    'metadata': active_version.function_metadata,
                    'dependencies': [dep.name for dep in active_version.dependencies],
                    'imports': [imp.name for imp in active_version.imports],
                    'created_date': active_version.created_date.isoformat(),
                    'input_parameters': active_version.input_parameters,
                    'output_parameters': active_version.output_parameters,
                    'triggers': active_version.triggers
                }
                for function in functions
                if (active_version := next((v for v in function.versions if v.is_active), None))
            ]

    def remove_function(self, name: str) -> None:
        with self.session_scope() as session:
            function = self.db.get_function(session, name)
            if function:
                session.delete(function)

    def get_function_versions(self, name: str) -> List[Dict[str, Any]]:
        with self.session_scope() as session:
            function = self.db.get_function(session, name)
            if function:
                return [
                    {
                        'version': v.version,
                        'code': v.code,
                        'metadata': v.function_metadata,
                        'is_active': v.is_active,
                        'dependencies': [dep.name for dep in v.dependencies],
                        'created_date': v.created_date.isoformat(),
                        'input_parameters': v.input_parameters,
                        'output_parameters': v.output_parameters,
                        'triggers': v.triggers
                    }
                    for v in function.versions
                ]
            return []

    def activate_function_version(self, name: str, version: int) -> None:
        with self.session_scope() as session:
            function = self.db.get_function(session, name)
            if function:
                for v in function.versions:
                    v.is_active = (v.version == version)

    # Import management
    def add_import(self, name: str, source: str, lib: Optional[str] = None) -> None:
        with self.session_scope() as session:
            self.db.add_import(session, name, source, lib)

    def get_all_imports(self) -> List[Dict[str, Any]]:
        with self.session_scope() as session:
            imports = session.query(Import).all()
            return [{"name": imp.name, "source": imp.source, "lib": imp.lib} for imp in imports]

    def get_function_imports(self, function_name: str) -> List[Dict[str, Any]]:
        with self.session_scope() as session:
            function = session.query(Function).filter_by(name=function_name).first()
            if function:
                imports = (session.query(Import)
                           .join(FunctionVersion.imports)
                           .filter(FunctionVersion.function_id == function.id)
                           .all())
                return [{"name": imp.name, "source": imp.source, "lib": imp.lib} for imp in imports]
            return []

    # Logging
    def add_log(self, function_name: str, message: str, timestamp: datetime, 
                params: Optional[Dict[str, Any]] = None, 
                output: Optional[Any] = None, 
                time_spent: Optional[float] = None, 
                parent_log_id: Optional[int] = None, 
                triggered_by_log_id: Optional[int] = None, 
                log_type: str = 'info') -> int:
        with self.session_scope() as session:
            return self.db.add_log(
                session=session,
                function_name=function_name,
                message=message,
                timestamp=timestamp,
                params=params,
                output=output,
                time_spent=time_spent,
                parent_log_id=parent_log_id,
                triggered_by_log_id=triggered_by_log_id,
                log_type=log_type
            )

    def update_log(self, log_id: int, **kwargs) -> None:
        with self.session_scope() as session:
            self.db.update_log(
                session=session,
                log_id=log_id,
                **kwargs
            )


    def update_log_params(self, log_id: int, params: Dict[str, Any]) -> None:
        with self.session_scope() as session:
            self.db.update_log_params(
                session=session,
                log_id=log_id,
                params=params
            )



    def get_logs(self, function_name: Optional[str] = None, 
                 start_date: Optional[datetime] = None, 
                 end_date: Optional[datetime] = None, 
                 triggered_by_log_id: Optional[int] = None) -> List[Dict[str, Any]]:
        with self.session_scope() as session:
            logs = self.db.get_logs(session, function_name, start_date, end_date, triggered_by_log_id)
            return [
                {
                    'id': log.id,
                    'function_name': log.function_name,
                    'message': log.message,
                    'timestamp': log.timestamp.isoformat(),
                    'params': log.params,
                    'output': log.output,
                    'time_spent': log.time_spent,
                    'parent_log_id': log.parent_log_id,
                    'triggered_by_log_id': log.triggered_by_log_id,
                    'log_type': log.log_type
                }
                for log in logs
            ]

    def get_log_bundle(self, log_id: int) -> List[Dict[str, Any]]:
        with self.session_scope() as session:
            logs_collected = {}

            def fetch_related_logs(current_log_id):
                if current_log_id in logs_collected:
                    return
                log = self.db.get_log(session, current_log_id)
                if log:
                    logs_collected[current_log_id] = log
                else:
                    logger.warning(f"Log ID {current_log_id} not found.")
                    return

                # Fetch parent log
                if log.parent_log_id:
                    fetch_related_logs(log.parent_log_id)

                    # Fetch sibling logs
                    sibling_logs = session.query(Log).filter(
                        Log.parent_log_id == log.parent_log_id,
                        Log.id != current_log_id
                    ).all()
                    for sibling in sibling_logs:
                        fetch_related_logs(sibling.id)

                # Fetch child logs
                child_logs = self.db.get_child_logs(session, current_log_id)
                for child in child_logs:
                    fetch_related_logs(child.id)

            fetch_related_logs(log_id)

            # Convert logs to dictionaries
            all_logs = [
                {
                    'id': log.id,
                    'function_name': log.function_name,
                    'message': log.message,
                    'timestamp': log.timestamp.isoformat(),
                    'params': log.params,
                    'output': log.output,
                    'time_spent': log.time_spent,
                    'parent_log_id': log.parent_log_id,
                    'triggered_by_log_id': log.triggered_by_log_id,
                    'log_type': log.log_type
                }
                for log in logs_collected.values()
            ]

            return all_logs


    
    # Secret key management
    def add_secret_key(self, key_name: str, key_value: str) -> None:
        with self.session_scope() as session:
            existing_key = self.db.get_secret_key(session, key_name)
            if existing_key:
                existing_key.value = key_value
            else:
                self.db.add_secret_key(session, key_name, key_value)

    def get_secret_key(self, key_name: str) -> Optional[str]:
        with self.session_scope() as session:
            secret_key = self.db.get_secret_key(session, key_name)
            return secret_key.value if secret_key else None

    def get_all_secret_keys(self) -> Dict[str, str]:
        with self.session_scope() as session:
            secret_keys = self.db.get_all_secret_keys(session)
            return {key.name: key.value for key in secret_keys if key.value is not None}

    # Trigger management
    def add_trigger(self, triggered_function_name: str, triggering_function_name: Optional[str] = None) -> None:
        with self.session_scope() as session:
            self.db.add_trigger(session, triggered_function_name, triggering_function_name)

    def get_triggers_for_function(self, function_name: str) -> List[str]:
        with self.session_scope() as session:
            all_functions = self.db.get_all_functions(session)
            triggered_functions = []
            for func in all_functions:
                active_version = self.db.get_active_version(session, func)
                if active_version and active_version.triggers:
                    if function_name in active_version.triggers:
                        triggered_functions.append(func.name)
            return triggered_functions
```

## File: `babyagi/functionz/db/local_db.py`
```python
# local_db.py

from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker, scoped_session, joinedload
from sqlalchemy.exc import SQLAlchemyError
from contextlib import contextmanager
from .models import Base, Function, FunctionVersion, Import, Log, SecretKey, fernet
import datetime



class LocalDB:
    def __init__(self, db_path='sqlite:///funztionz.db'):
        self.engine = create_engine(db_path)
        Base.metadata.create_all(self.engine)
        self.Session = scoped_session(sessionmaker(bind=self.engine))

    @contextmanager
    def session_scope(self):
        session = self.Session()
        try:
            yield session
            session.commit()
        except SQLAlchemyError as e:
            session.rollback()
            raise e
        finally:
            self.Session.remove()

    def serialize_for_json(self, obj):
        """
        Recursively convert datetime objects to ISO format strings within the given object.
        Handles dictionaries, lists, and individual datetime objects.
        """
        if isinstance(obj, dict):
            return {k: self.serialize_for_json(v) for k, v in obj.items()}
        elif isinstance(obj, list):
            return [self.serialize_for_json(element) for element in obj]
        elif isinstance(obj, datetime.datetime):
            return obj.isoformat()
        else:
            return obj


    def get_function(self, session, name):
        return session.query(Function).filter_by(name=name).first()

    def get_active_version(self, session, function):
        return session.query(FunctionVersion).filter_by(function_id=function.id, is_active=True).options(
            joinedload(FunctionVersion.dependencies)
        ).first()

    def get_all_functions(self, session):
        return session.query(Function).options(
            joinedload(Function.versions).joinedload(FunctionVersion.dependencies)
        ).all()

    def add_or_update_function(self, session, name, code, metadata, dependencies, triggers, input_parameters, output_parameters, imports=None):
        function = self.get_function(session, name)
        if not function:
            function = Function(name=name)
            session.add(function)
            session.flush()

        # Handle imports before creating the FunctionVersion
        import_objects = []
        if imports:
            for import_name in imports:
                imp = session.query(Import).filter_by(name=import_name).first()
                if not imp:
                    imp = Import(name=import_name, source='external')
                    session.add(imp)
                    session.flush()
                import_objects.append(imp)

        # Create the FunctionVersion instance, now including triggers as JSON
        version = FunctionVersion(
            function=function,
            version=len(function.versions) + 1,
            code=code,
            function_metadata=metadata or {},
            is_active=True,
            input_parameters=input_parameters or [],
            output_parameters=output_parameters or [],
            imports=import_objects,  # Pass the list of Import objects here
            triggers=triggers or []  # Store the triggers as JSON
        )
        session.add(version)

        # Handle dependencies
        if dependencies:
            for dep in dependencies:
                dep_func = self.get_function(session, dep)
                if dep_func:
                    version.dependencies.append(dep_func)

        # Deactivate previous versions
        for v in function.versions:
            if v != version:
                v.is_active = False


    def add_import(self, session, name, source, lib=None):
        existing_import = session.query(Import).filter_by(name=name).first()
        if not existing_import:
            new_import = Import(name=name, source=source, lib=lib)
            session.add(new_import)



    def add_log(self, session, function_name, message, timestamp, params, output, time_spent, parent_log_id=None, triggered_by_log_id=None, log_type='info'):
        if isinstance(timestamp, str):
            # Convert the string timestamp back to a datetime object
            timestamp = datetime.datetime.fromisoformat(timestamp)

        # Serialize params and output to ensure JSON serializability
        serialized_params = self.serialize_for_json(params) if params else None
        serialized_output = self.serialize_for_json(output) if output else None

        new_log = Log(
            function_name=function_name,
            message=message,
            timestamp=timestamp,
            params=serialized_params,
            output=serialized_output,
            time_spent=time_spent,
            parent_log_id=parent_log_id,
            triggered_by_log_id=triggered_by_log_id,
            log_type=log_type
        )
        session.add(new_log)
        session.flush()  # This ensures new_log.id is populated
        return new_log.id

    def update_log(self, session, log_id: int, **kwargs) -> None:
        # Fetch the log entry by id
        log_entry = session.query(Log).filter(Log.id == log_id).first()
        if log_entry:
            # Update only the fields provided in kwargs
            for key, value in kwargs.items():
                if hasattr(log_entry, key):
                    setattr(log_entry, key, value)
                else:
                    raise ValueError(f"Log has no attribute '{key}'")
            # No need to call session.commit(); it will be committed in the session scope
        else:
            raise ValueError(f"Log with id {log_id} not found.")



    def update_log_params(self, session, log_id: int, params) -> None:
        log_entry = session.query(Log).filter_by(id=log_id).one_or_none()
        if log_entry is None:
            raise ValueError(f"Log entry with id {log_id} not found.")

        log_entry.params = params
        session.commit()



    def get_log(self, session, log_id: int):
        """
        Fetches a single log entry by its ID.

        :param session: SQLAlchemy session object.
        :param log_id: The ID of the log to retrieve.
        :return: Log object if found, else None.
        """
        return session.query(Log).filter_by(id=log_id).first()

    def get_child_logs(self, session, parent_id: int):
        """
        Retrieves all child logs that have the given parent_log_id.

        :param session: SQLAlchemy session object.
        :param parent_id: The ID of the parent log.
        :return: List of Log objects.
        """
        return session.query(Log).filter_by(parent_log_id=parent_id).all()
    
    def get_logs(self, session, function_name=None, start_date=None, end_date=None, triggered_by_log_id=None):
        query = session.query(Log)

        if function_name:
            query = query.filter(Log.function_name == function_name)

        if start_date:
            query = query.filter(Log.timestamp >= start_date)

        if end_date:
            query = query.filter(Log.timestamp <= end_date)

        if triggered_by_log_id:
            query = query.filter(Log.triggered_by_log_id == triggered_by_log_id)

        return query.all()


    def get_log_bundle(self, session, log_id):
        logs_collected = {}

        def fetch_related_logs(current_log_id):
            if current_log_id in logs_collected:
                return
            log = session.query(Log).filter_by(id=current_log_id).one_or_none()
            if not log:
                return
            logs_collected[current_log_id] = log

            # Fetch parent log
            if log.parent_log_id:
                fetch_related_logs(log.parent_log_id)

                # Fetch sibling logs
                sibling_logs = session.query(Log).filter(
                    Log.parent_log_id == log.parent_log_id,
                    Log.id != current_log_id
                ).all()
                for sibling in sibling_logs:
                    if sibling.id not in logs_collected:
                        fetch_related_logs(sibling.id)

            # Fetch child logs
            child_logs = session.query(Log).filter_by(parent_log_id=current_log_id).all()
            for child in child_logs:
                if child.id not in logs_collected:
                    fetch_related_logs(child.id)

        fetch_related_logs(log_id)
        return list(logs_collected.values())




    def add_secret_key(self, session, function_id, key_name, key_value):
        print(f"Encrypting value for key '{key_name}'")
        try:
            encrypted_value = fernet.encrypt(key_value.encode())
            print(f"Value encrypted successfully for key '{key_name}'")
            secret_key = SecretKey(function_id=function_id, name=key_name, _encrypted_value=encrypted_value)
            session.add(secret_key)
            print(f"Secret key '{key_name}' added to session")
        except Exception as e:
            print(f"Error in add_secret_key: {str(e)}")
            raise

    
    def add_secret_key(self, session, key_name, key_value):
        encrypted_value = fernet.encrypt(key_value.encode())
        secret_key = SecretKey(name=key_name, _encrypted_value=encrypted_value)
        session.add(secret_key)

    def get_secret_key(self, session, key_name):
        return session.query(SecretKey).filter_by(name=key_name).first()

    
    def get_all_secret_keys(self, session):
        return session.query(SecretKey).all()

    
```

## File: `babyagi/functionz/db/models.py`
```python
# models.py

from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey, Boolean, Table, Float, LargeBinary
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from cryptography.fernet import Fernet
from cryptography.fernet import InvalidToken
from sqlalchemy.ext.hybrid import hybrid_property
import os
import json
from datetime import datetime

Base = declarative_base()

KEY_FILE = 'encryption_key.json'

def get_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'r') as f:
            return json.load(f)['key']
    else:
        key = Fernet.generate_key().decode()
        with open(KEY_FILE, 'w') as f:
            json.dump({'key': key}, f)
        return key

ENCRYPTION_KEY = get_or_create_key()
print(f"Using encryption key: {ENCRYPTION_KEY}")
fernet = Fernet(ENCRYPTION_KEY.encode())

# Association table for function dependencies (many-to-many between FunctionVersion and Function)
function_dependency = Table('function_dependency', Base.metadata,
    Column('function_version_id', Integer, ForeignKey('function_versions.id')),
    Column('dependency_id', Integer, ForeignKey('functions.id'))
)

# **Define function_version_imports association table here**
function_version_imports = Table('function_version_imports', Base.metadata,
    Column('function_version_id', Integer, ForeignKey('function_versions.id')),
    Column('import_id', Integer, ForeignKey('imports.id'))
)


class Function(Base):
    __tablename__ = 'functions'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    versions = relationship("FunctionVersion", back_populates="function", cascade="all, delete-orphan")

class FunctionVersion(Base):
    __tablename__ = 'function_versions'
    id = Column(Integer, primary_key=True)
    function_id = Column(Integer, ForeignKey('functions.id'))
    version = Column(Integer)
    code = Column(String)
    function_metadata = Column(JSON)
    is_active = Column(Boolean, default=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    input_parameters = Column(JSON)
    output_parameters = Column(JSON)
    function = relationship("Function", back_populates="versions")
    dependencies = relationship('Function', secondary=function_dependency,
                                primaryjoin=(function_dependency.c.function_version_id == id),
                                secondaryjoin=(function_dependency.c.dependency_id == Function.id))
    imports = relationship('Import', secondary=function_version_imports, back_populates='function_versions')
    triggers = Column(JSON, nullable=True)  # Store triggers as a JSON field



class Import(Base):
    __tablename__ = 'imports'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    lib = Column(String, nullable=True)
    source = Column(String)
    function_versions = relationship('FunctionVersion', secondary=function_version_imports, back_populates='imports')


class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    function_name = Column(String, nullable=False)
    message = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)
    params = Column(JSON, nullable=True)
    output = Column(JSON, nullable=True)
    time_spent = Column(Float, nullable=True)
    log_type = Column(String, nullable=False)

    # Parent Log Relationship
    parent_log_id = Column(Integer, ForeignKey('logs.id'), nullable=True)
    parent_log = relationship(
        'Log',
        remote_side=[id],
        backref='child_logs',
        foreign_keys=[parent_log_id]
    )

    # Triggered By Log Relationship
    triggered_by_log_id = Column(Integer, ForeignKey('logs.id'), nullable=True)
    triggered_by_log = relationship(
        'Log',
        remote_side=[id],
        backref='triggered_logs',
        foreign_keys=[triggered_by_log_id]
    )


class SecretKey(Base):
    __tablename__ = 'secret_keys'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)  # Make name unique
    _encrypted_value = Column(LargeBinary, nullable=False)

    @hybrid_property
    def value(self):
        if self._encrypted_value:
            try:
                return fernet.decrypt(self._encrypted_value).decode()
            except InvalidToken:
                print(f"Error decrypting value for key: {self.name}. The encryption key may have changed.")
                return None
        return None

    @value.setter
    def value(self, plaintext_value):
        if plaintext_value:
            self._encrypted_value = fernet.encrypt(plaintext_value.encode())
        else:
            self._encrypted_value = None

```

## File: `babyagi/functionz/packs/default/ai_functions.py`
```python
# packs/ai_generator.py

from functionz.core.framework import func

@func.register_function(
    metadata={"description": "GPT Call function using LiteLLm"},
    imports=["litellm"],
    key_dependencies=["openai_api_key"]
)
def gpt_call(prompt: str) -> str:
    from litellm import completion
    messages = [{"role": "user", "content": prompt}]
    response = completion(model="gpt-4o", messages=messages)
    return response['choices'][0]['message']['content']

@func.register_function(
    metadata={"description": "Generates a description for a function using LiteLLm"},
    dependencies=["gpt_call"]
)
def description_writer(function_code: str) -> str:
    prompt = (
        f"Provide a concise and clear description for the following Python function:\n\n"
        f"{function_code}\n\n"
        f"Description:"
    )
    description = func.gpt_call(prompt)
    return description

@func.register_function(
    metadata={"description": "Generates and updates descriptions for functions lacking one or having an empty description"},
    dependencies=["description_writer"],
    triggers=["function_added_or_updated"]
)
def ai_description_generator(function_name: str) -> None:
    print(f"Generating AI description for function: {function_name}")
    function = func.db.get_function(function_name)
    if not function:
        print(f"Function '{function_name}' not found in the database.")
        return

    description = function.get('metadata', {}).get('description', '').strip()
    function_code = function.get('code', '')

    if not description and function_code.strip():
        #print(f"Generating description for function '{function_name}'.")
        generated_description = func.description_writer(function_code)
        func.update_function(
            name=function_name,
            metadata={"description": generated_description}
        )
        print(f"Description for function '{function_name}' has been generated and updated.")
        return f"Description for function '{function_name}' has been generated and updated."
    elif not function_code.strip():
        print(f"Function '{function_name}' has no code to generate a description.")
        return f"Function '{function_name}' has no code to generate a description."
    else:
        print(f"Function '{function_name}' already has a non-empty description.")
        return f"Function '{function_name}' already has a non-empty description."

@func.register_function(
    metadata={"description": "Scans all functions and generates descriptions for those lacking one"},
    dependencies=["ai_description_generator"]
)
def generate_missing_descriptions() -> None:
    all_functions = func.db.get_all_functions()
    missing_description_functions = [
        func_info['name'] for func_info in all_functions
        if not func_info.get('metadata', {}).get('description')
    ]
    if not missing_description_functions:
        print("All functions already have descriptions.")
        return
    print(f"Found {len(missing_description_functions)} function(s) without descriptions. Generating descriptions...")
    for function_name in missing_description_functions:
        func.ai_description_generator(function_name)
    print("Description generation process completed.")


@func.register_function(
    metadata={"description": "Embeds an input using LiteLLM"},
    imports=["litellm"],
    key_dependencies=["openai_api_key"]
)
def embed_input(input_text: str, model: str = "text-embedding-ada-002", 
                encoding_format: str = "float", dimensions: int = None, 
                timeout: int = 600) -> list:
    from litellm import embedding
    import os

    # Set OpenAI API Key from environment variables
    os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

    # Prepare the embedding request with optional parameters
    embedding_params = {
        "model": model,
        "input": [input_text],
        "encoding_format": encoding_format,
        "timeout": timeout
    }

    if dimensions:
        embedding_params["dimensions"] = dimensions

    # Call the LiteLLM embedding function
    response = embedding(**embedding_params)

    # Return the embedding from the response
    return response['data'][0]['embedding']


@func.register_function(
    metadata={"description": "Embeds and updates a function's description if it exists"},
    dependencies=["embed_input"],
    imports=["os","csv"]
)
def embed_function_description(function: str) -> None:
    print(f"Embedding description for function: {function}")
    # Retrieve the function details from the database
    function_data = func.db.get_function(function)
    if not function_data:
        print(f"Function '{function}' not found in the database.")
        return

    description = function_data.get('metadata', {}).get('description', '').strip()
    if description:
        print(f"Embedding description for function '{function}'.")
        embedding = func.embed_input(description)

        # Check if 'function_embeddings.csv' exists, create it if not
        file_path = 'function_embeddings.csv'
        file_exists = os.path.isfile(file_path)

        # Create a list to store CSV data
        rows = []

        if file_exists:
            with open(file_path, mode='r') as file:
                reader = csv.reader(file)
                rows = list(reader)

        # Look for the function in the existing rows
        function_found = False
        for i, row in enumerate(rows):
            if row[0] == function:  # function column is the first column
                rows[i][1] = str(embedding)  # Update the embedding
                function_found = True
                print(f"Updated embedding for function '{function}'.")

        if not function_found:
            # Add a new row if the function is not found
            rows.append([function, str(embedding)])
            print(f"Added new function '{function}' with its embedding.")

        # Write back the data to the CSV file (create or update)
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)

        print(f"Embedding for function '{function}' has been saved.")
        return embedding
    else:
        print(f"Function '{function}' has no description to embed.")
        return f"Function '{function}' has no description to embed."



@func.register_function(
    metadata={"description": "Finds similar functions based on the provided description"},
    dependencies=["embed_input"],
    imports=["numpy", "csv", "sklearn","os"]
)
def find_similar_function(description: str, top_n: int = 3):
    import numpy as np
    from sklearn.metrics.pairwise import cosine_similarity
    # Step 1: Embed the input description
    #print(f"Embedding input description: {description}")
    input_embedding = func.embed_input(description)

    # Step 2: Load stored embeddings and descriptions from CSV
    file_path = 'function_embeddings.csv'
    stored_embeddings = []
    stored_functions = []

    if not os.path.isfile(file_path):
        print(f"No embeddings found in {file_path}.")
        return []

    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            stored_functions.append(row[0])
            stored_embeddings.append(np.fromstring(row[1].strip("[]"), sep=','))

    if not stored_embeddings:
        print("No embeddings stored.")
        return []

    # Step 3: Calculate cosine similarity between the input embedding and stored embeddings
    similarities = cosine_similarity([input_embedding], stored_embeddings)

    # Step 4: Sort stored functions by similarity
    sorted_indices = np.argsort(similarities[0])[::-1]  # Sort in descending order

    # Step 5: Return the top N most similar functions
    similar_functions = [stored_functions[i] for i in sorted_indices[:top_n]]

    print(f"Top {top_n} similar functions: {similar_functions}")
    return similar_functions


@func.register_function(
    metadata={"description": "Generates embeddings for functions missing from the CSV"},
    dependencies=["embed_function_description"],
    imports=["os", "csv"]
)
def generate_missing_embeddings() -> None:
    # Step 1: Retrieve all functions from the database
    all_functions = func.db.get_all_functions()
    all_function_names = [func_info['name'] for func_info in all_functions]

    # Step 2: Check if 'function_embeddings.csv' exists
    file_path = 'function_embeddings.csv'
    file_exists = os.path.isfile(file_path)

    # Read existing embeddings from CSV if the file exists
    embedded_functions = []
    if file_exists:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            embedded_functions = [row[0] for row in reader]  # First column is the function name

    # Step 3: Find functions without embeddings
    missing_embeddings = [func_name for func_name in all_function_names if func_name not in embedded_functions]

    if not missing_embeddings:
        print("All functions already have embeddings.")
        return

    print(f"Found {len(missing_embeddings)} function(s) without embeddings. Generating embeddings...")

    # Step 4: Embed the functions that are missing
    for function_name in missing_embeddings:
        print(f"Embedding function: {function_name}")
        func.embed_function_description(function_name)

    print("Embedding generation process completed.")



@func.register_function(
    metadata={"description": "Chooses a function to use"},
    dependencies=["get_all_functions","gpt_call"]
)
def choose_function(prompt: str) -> str:
    functions = func.get_all_functions()
    prompt = (
        f"Which functions are most relevant to the following input? It could be ones to use or look at as reference to build a new one:\n\n"
        f"{prompt}\n\n"
        f"Functions:{functions}"
    )
    choice = func.gpt_call(prompt)
    return {"functions":functions,"choice":choice}
```

## File: `babyagi/functionz/packs/default/default_functions.py`
```python
# packs/default_functions.py

from babyagi.functionz.core.framework import func
from datetime import datetime
from typing import Optional, Dict, Any, List

@func.register_function()
def execute_function_wrapper(function_name: str, *args, **kwargs):
    # Create an initial log for the wrapper
    wrapper_log_id = func.db.add_log(
        function_name="execute_function_wrapper",
        message="Wrapper execution started.",
        timestamp=datetime.now(),
        params={"function_name": function_name, "args": args, "kwargs": kwargs},
        output=None,
        time_spent=0,
        parent_log_id=None,
        triggered_by_log_id=None,
        log_type='started'
    )
    # Execute the function with the wrapper's log ID as the parent ID
    result = func.execute_function(function_name, *args, parent_log_id=wrapper_log_id, **kwargs)

    # Update the wrapper log after execution
    func.db.update_log(wrapper_log_id, output=result, log_type='success', message="Wrapper execution completed.")
    return result


@func.register_function(
    metadata={
        "description": "Dynamically adds a new function to the system with the provided code and metadata."
    },
    imports=["typing"]
)
def add_new_function(
    name: str,
    code: str,
    metadata: dict = None,
    imports: list = None,
    dependencies: list = None,
    key_dependencies: list = None,
    triggers: list = None
) -> bool:

    try:
        func.registrar.add_function(
            name=name,
            code=code,
            metadata=metadata,
            imports=imports,
            dependencies=dependencies,
            key_dependencies=key_dependencies,
            triggers=triggers
        )
        #print(f"Function '{name}' added successfully.")
        return True
    except Exception as e:
        print(f"Error adding function '{name}': {str(e)}")
        return False


@func.register_function()
def function_added_or_updated(action=None, triggered_function_name=None):
    """
    Triggered whenever a function is added or updated.
    """
    print(f"Function '{triggered_function_name}' has been {action}.")
    function_data = func.get_function(triggered_function_name) if triggered_function_name else None
    if function_data:
        return triggered_function_name
    else:
        print(f"Function '{triggered_function_name}' not found in the database.")
        return None

@func.register_function(
    metadata={"description": "Add a secret key to the database."},
    imports=["os"]
)
def add_key_wrapper(key_name: str, key_value: str):
    return func.add_key(key_name, key_value)

@func.register_function(metadata={"description": "Get all versions of a given function."})
def get_function_versions_wrapper(name: str):
    return func.get_function_versions(name)

@func.register_function()
def get_function_wrapper(name: str):
    return func.get_function(name)


@func.register_function(metadata={"description": "Get all versions of a given function."})
def get_all_functions_wrapper():
    return func.get_all_functions()

@func.register_function(metadata={"description": "Activate a specific version of a function."})
def activate_function_version_wrapper(name: str, version: int):
    return func.activate_function_version(name, version)

@func.register_function(metadata={"description": "Display all registered functions and their metadata."})
def display_functions_wrapper():
    return func.display()

@func.register_function(
    metadata={"description": "Get logs for a specific function, optionally filtered by date."},
    imports=['datetime']
                       )
def get_logs_wrapper(function_name: str = None, start_date: datetime = None,
                 end_date: datetime = None):
    return func.get_logs(function_name, start_date, end_date)

@func.register_function(metadata={"description": "Add a trigger that executes a specific function when another function is executed."})
def add_trigger_wrapper(triggered_function_name: str, triggering_function_name: Optional[str] = None):
    return func.add_trigger(triggered_function_name, triggering_function_name)


@func.register_function(metadata={"description": "Get all secret keys stored."})
def get_all_secret_keys():
    return func.get_all_secret_keys()


@func.register_function(metadata={"description": "Get all imports."})
def get_all_imports_wrapper():
    return func.get_all_imports()
```

## File: `babyagi/functionz/packs/default/function_calling_chat.py`
```python
from functionz.core.framework import func
import json
import litellm

# Assuming `func` is the registry from your framework
# and `execute_function_wrapper` is already registered in the database.

@func.register_function(
    metadata={
        "description": "A chat application that interacts with LiteLLM and executes selected functions from the database."
    },
    imports=["litellm", "json"],
    dependencies=["get_function_wrapper", "execute_function_wrapper"],
    key_dependencies=["OPENAI_API_KEY"]  # Ensure this key is set in your environment
)
def chat_with_functions(chat_history, available_function_names) -> str:
    def map_python_type_to_json(python_type: str) -> dict:
        """
        Maps Python type annotations to JSON Schema types.

        Args:
            python_type (str): The Python type as a string.

        Returns:
            dict: The corresponding JSON Schema type with additional details if necessary.
        """
        type_mapping = {
            "str": {"type": "string"},
            "int": {"type": "integer"},
            "float": {"type": "number"},
            "bool": {"type": "boolean"},
            "list": {"type": "array", "items": {"type": "string"}},  # Assuming list of strings
            "dict": {"type": "object"},
            "Any": {"type": "string"}  # Default to string for unsupported types
        }
        return type_mapping.get(python_type, {"type": "string"})

    # Enable verbose logging for LiteLLM
    litellm.set_verbose = True

    # Initialize chat context with system message
    chat_context = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

    # Validate and append chat history
    if not isinstance(chat_history, list):
        raise ValueError("chat_history must be a list of messages.")

    for message in chat_history:
        if not isinstance(message, dict):
            raise ValueError("Each message in chat_history must be a dictionary.")
        role = message.get('role')
        content = message.get('message')
        if role not in ['user', 'assistant', 'system']:
            raise ValueError("Message role must be 'user', 'assistant', or 'system'.")
        if not isinstance(content, str):
            raise ValueError("Message content must be a string.")
        chat_context.append({"role": role, "content": content})

    # Handle available_function_names input
    if isinstance(available_function_names, str):
        # Split the string by commas and strip whitespace
        available_function_names = [name.strip() for name in available_function_names.split(',') if name.strip()]
    elif isinstance(available_function_names, list):
        # Ensure all elements are strings and strip whitespace
        available_function_names = [name.strip() for name in available_function_names if isinstance(name, str) and name.strip()]
    else:
        raise ValueError("available_function_names must be a string or a list of strings.")

    if not available_function_names:
        raise ValueError("No valid function names provided in available_function_names.")

    # Fetch available functions from the database
    tools = []
    for func_name in available_function_names:
        # Retrieve function details using the get_function_wrapper
        function_data = get_function_wrapper(func_name)
        if function_data:
            # Construct the tool definition for LiteLLM
            tool = {
                "type": "function",
                "function": {
                    "name": function_data['name'],
                    "description": function_data['metadata']['description'],
                    "parameters": {
                        "type": "object",
                        "properties": {},
                        "required": []
                    },
                },
            }

            # Map input_parameters to the tool's parameters
            for param in function_data.get('input_parameters', []):
                # Convert Python types to JSON Schema types
                json_schema = map_python_type_to_json(param['type'])
                tool['function']['parameters']['properties'][param['name']] = {
                    **json_schema,
                    "description": param.get('description', '')
                }
                if param.get('required', False):
                    tool['function']['parameters']['required'].append(param['name'])

            tools.append(tool)
        else:
            # Handle the case where the function is not found
            raise ValueError(f"Function '{func_name}' not found in the database.")


    # Call LiteLLM's completion API with the user message and available tools
    response = litellm.completion(
        model="gpt-4-turbo",
        messages=chat_context,
        tools=tools,
        tool_choice="auto"
    )

    # Extract the message from the response
    response_message = response['choices'][0]['message']

    # Check if the model wants to call any functions
    tool_calls = response_message.get('tool_calls', [])

    # If there are function calls, execute them
    if tool_calls:
        # Append the assistant's message to the chat context
        chat_context.append(response_message)

        for tool_call in tool_calls:
            function_name = tool_call['function']['name']
            function_args = json.loads(tool_call['function']['arguments'])
            tool_call_id = tool_call['id']  # Extract the tool_call_id

            # Execute the function using execute_function_wrapper
            try:
                function_response = execute_function_wrapper(function_name, **function_args)
            except Exception as e:
                function_response = f"Error executing function '{function_name}': {str(e)}"

            # Ensure function_response is a string
            if not isinstance(function_response, str):
                function_response = json.dumps(function_response)

            # Append the function response to the chat context
            chat_context.append({
                "tool_call_id": tool_call_id,  # Include the tool_call_id
                "role": "tool",  # Use 'tool' as per LiteLLM's protocol
                "name": function_name,
                "content": function_response
            })

        # Call LiteLLM again with the updated context including function responses
        second_response = litellm.completion(
            model="gpt-4-turbo",
            messages=chat_context
        )

        # Extract and return the assistant's final response
        assistant_response = second_response['choices'][0]['message']['content']
        return assistant_response
    else:
        # If no functions are called, return the assistant's message directly
        assistant_response = response_message.get('content', '')
        return assistant_response
```

## File: `babyagi/functionz/packs/default/os.py`
```python
@func.register_function(
    metadata={"description": "Returns the current directory and recursively lists all files and folders, excluding hidden files, folders (those starting with a '.'), and the '__pycache__' folder. The output omits the current directory prefix from file paths for readability."},
    imports=["os"]
)
def get_full_directory_contents_cleaned():
    current_directory = os.getcwd()  # Get current working directory
    directory_structure = {}

    # Walk through the directory and its subdirectories
    for root, dirs, files in os.walk(current_directory):
        # Filter out hidden directories, '__pycache__', and hidden files
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        files = [f for f in files if not f.startswith('.')]

        # Remove the current directory path from the root
        relative_root = root.replace(current_directory, "").lstrip(os.sep)
        directory_structure[relative_root] = {
            "folders": dirs,
            "files": files
        }

    return {"current_directory": current_directory, "directory_structure": directory_structure}
```

## File: `babyagi/functionz/packs/drafts/choose_or_create_function.py`
```python
from functionz.core.framework import func

@func.register_function(
    metadata={"description": "Choose or create a function based on user input and execute it."},
    dependencies=[
        "display_functions_wrapper",
        "get_function_wrapper",
        "execute_function_wrapper",
        "generate_function_from_description"
    ],
    imports=[
        {"name": "litellm", "lib": "litellm"},
        {"name": "pydantic", "lib": "pydantic"},
        {"name": "typing", "lib": "typing"},
        {"name": "json", "lib": "json"},
    ]
)
def choose_or_create_function(user_input: str) -> dict:
    """
    Takes user input, compares against existing functions, decides whether to use an existing function or generate a new one, then executes the function with generated parameters.

    Args:
        user_input (str): The user's input or request.

    Returns:
        dict: A dictionary containing the result of the function execution, intermediate steps, and any relevant information.
    """
    from litellm import completion
    from pydantic import BaseModel, Field, ValidationError
    from typing import List, Optional, Dict, Any
    import json

    intermediate_steps = []

    # Step 1: Fetch existing functions
    try:
        existing_functions = display_functions_wrapper()
        print(f"[DEBUG] Existing Functions: {existing_functions}")
        intermediate_steps.append({"step": "Fetch Existing Functions", "content": existing_functions})
    except Exception as e:
        print(f"[ERROR] Failed to fetch existing functions: {e}")
        intermediate_steps.append({"step": "Error Fetching Existing Functions", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error fetching existing functions."}

    # Step 2: Use LLM to decide whether to use an existing function or generate a new one
    system_prompt = """
You are an assistant that helps decide whether an existing function can fulfill a user's request or if a new function needs to be created.

Please analyze the user's input and the list of available functions.

Return your decision in the following JSON format:

{
    "use_existing_function": true or false,
    "function_name": "name of the existing function" (if applicable),
    "function_description": "description of the function to generate" (if applicable)
}

Provide only the JSON response, without any additional text.
"""

    class FunctionDecision(BaseModel):
        use_existing_function: bool = Field(..., description="True if an existing function can be used; False if a new function needs to be generated.")
        function_name: Optional[str] = Field(None, description="Name of the existing function to use.")
        function_description: Optional[str] = Field(None, description="Description of the new function to generate.")

    decision_prompt = f"""
The user has provided the following input:
\"{user_input}\"

Available Functions:
{existing_functions}
"""

    try:
        decision_response = completion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": decision_prompt}
            ],
            response_format=FunctionDecision
        )
        print(f"[DEBUG] Decision Response: {decision_response}")
    except Exception as e:
        print(f"[ERROR] LLM call for FunctionDecision failed: {e}")
        intermediate_steps.append({"step": "Error in FunctionDecision LLM Call", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error during function decision analysis."}

    # Parse the response
    try:
        content = decision_response.choices[0].message.content
        print(f"[DEBUG] Raw Decision Content: {content}")
        decision_parsed = FunctionDecision.parse_raw(content)
        print(f"[DEBUG] Parsed FunctionDecision: {decision_parsed}")
        intermediate_steps.append({"step": "Function Decision", "content": decision_parsed.dict()})
    except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
        print(f"[ERROR] Parsing FunctionDecision response failed: {e}")
        intermediate_steps.append({"step": "Error Parsing FunctionDecision Response", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error parsing FunctionDecision response."}

    if decision_parsed.use_existing_function and decision_parsed.function_name:
        function_name = decision_parsed.function_name
        print(f"[INFO] Using existing function: {function_name}")
    elif not decision_parsed.use_existing_function and decision_parsed.function_description:
        # Generate the new function
        print(f"[INFO] Generating new function based on description.")
        gen_result = generate_function_from_description(decision_parsed.function_description)
        intermediate_steps.extend(gen_result.get("intermediate_steps", []))
        if not gen_result.get("added_to_database"):
            print(f"[ERROR] Failed to generate and add new function.")
            return {"intermediate_steps": intermediate_steps, "error": "# Error generating new function."}
        # Get the function name from the generated function code
        function_name = gen_result.get("function_name")
        if not function_name:
            # Extract function name from the code
            import re
            match = re.search(r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', gen_result.get("final_code", ""))
            if match:
                function_name = match.group(1)
                print(f"[INFO] Extracted function name: {function_name}")
            else:
                print(f"[ERROR] Function name not found in generated code.")
                return {"intermediate_steps": intermediate_steps, "error": "# Function name not found in generated code."}
    else:
        print(f"[ERROR] Invalid decision or missing information.")
        return {"intermediate_steps": intermediate_steps, "error": "# Invalid function decision."}

    # Step 3: Get the function code using get_function_wrapper
    try:
        function_info = get_function_wrapper(function_name)
        if not function_info:
            print(f"[ERROR] Function {function_name} not found.")
            intermediate_steps.append({"step": "Error Fetching Function", "content": f"Function {function_name} not found."})
            return {"intermediate_steps": intermediate_steps, "error": f"# Function {function_name} not found."}
        print(f"[DEBUG] Function Info: {function_info}")
        intermediate_steps.append({"step": "Fetch Function Info", "content": function_info})
    except Exception as e:
        print(f"[ERROR] Fetching function info failed: {e}")
        intermediate_steps.append({"step": "Error Fetching Function Info", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error fetching function info."}

    # Step 4: Use LLM to generate parameters for the function based on user input
    param_prompt = f"""
    The user has provided the following input:
    \"{user_input}\"

    The function to execute is:
    {function_info.get('code', '')}

    Generate a JSON object with a single key "parameters" that contains the parameters required by the function, filled in appropriately based on the user's input.

    Return only the JSON object, with no additional text.
    """

    try:
        # Define a Pydantic model with a fixed field "parameters"
        class FunctionParameters(BaseModel):
            parameters: Dict[str, Any]

            class Config:
                extra = 'forbid'  # This sets 'additionalProperties' to False

        param_response = completion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant that provides only JSON-formatted data, with no additional text."},
                {"role": "user", "content": param_prompt}
            ],
            response_format=FunctionParameters  # Keep the same parsing format
        )
        print(f"[DEBUG] Parameter Response: {param_response}")
    except Exception as e:
        print(f"[ERROR] LLM call for parameter generation failed: {e}")
        intermediate_steps.append({"step": "Error in Parameter Generation LLM Call", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error generating parameters."}

    # Parse the response using the Pydantic model
    try:
        content = param_response.choices[0].message.content
        print(f"[DEBUG] Raw Parameter Content: {content}")
        function_params_model = FunctionParameters.parse_raw(content)
        function_params = function_params_model.parameters  # Extract the parameters dictionary
        print(f"[DEBUG] Parsed Parameters: {function_params}")
        intermediate_steps.append({"step": "Generate Function Parameters", "content": function_params})
    except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
        print(f"[ERROR] Parsing parameters failed: {e}")
        intermediate_steps.append({"step": "Error Parsing Parameters", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error parsing function parameters."}

    # Step 5: Execute the function using execute_function_wrapper
    try:
        # Ensure that function_params is a dictionary
        if not isinstance(function_params, dict):
            raise TypeError("function_params must be a dictionary")
        execution_result = execute_function_wrapper(function_name, **function_params)
        print(f"[DEBUG] Execution Result: {execution_result}")
        intermediate_steps.append({"step": "Execute Function", "content": execution_result})
    except Exception as e:
        print(f"[ERROR] Function execution failed: {e}")
        intermediate_steps.append({"step": "Error Executing Function", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error executing function."}

    return {
        "intermediate_steps": intermediate_steps,
        "execution_result": execution_result
    }
```

## File: `babyagi/functionz/packs/drafts/code_writing_functions.py`
```python
from functionz.core.framework import func

@func.register_function(
  metadata={"description": "Checks if an existing function satisfies the user input"},
  dependencies=["gpt_call", "get_all_functions_wrapper"]
)
def check_existing_functions(user_input):
  import json

  while True:
      # Get all functions and their descriptions
      functions = get_all_functions_wrapper()
      function_descriptions = [
          {"name": f['name'], "description": f['metadata'].get('description', '')}
          for f in functions
      ]

      # Prepare the prompt
      prompt = f"""
You are an expert software assistant. The user has provided the following request:

"{user_input}"

Below is a list of available functions with their descriptions:

{function_descriptions}

Determine if any of the existing functions perfectly fulfill the user's request. If so, return the name of the function.

Provide your answer in the following JSON format:
{{
  "function_found": true or false,
  "function_name": "<name of the function if found, else null>"
}}

Examples:

Example 1:
User input: "Calculate the sum of two numbers"
Functions: [{{"name": "add_numbers", "description": "Adds two numbers"}}]
Response:
{{
  "function_found": true,
  "function_name": "add_numbers"
}}

Example 2:
User input: "Translate text to French"
Functions: [{{"name": "add_numbers", "description": "Adds two numbers"}}]
Response:
{{
  "function_found": false,
  "function_name": null
}}

Now, analyze the user's request and provide the JSON response.
"""

      response = gpt_call(prompt)

      # Try to parse the JSON response
      try:
          result = json.loads(response)
          if 'function_found' in result and isinstance(result['function_found'], bool) and \
             ('function_name' in result):
              return result
          else:
              raise ValueError("Invalid JSON structure")
      except Exception as e:
          # If parsing fails, retry
          continue

@func.register_function(
  metadata={"description": "Breaks down the user task into smaller functions"},
  dependencies=["gpt_call"]
)
def break_down_task(user_input):
  import json
  while True:
      # Prepare the prompt with detailed context
      prompt = f"""
You are an expert software assistant helping to break down a user's request into smaller functions for a microservice-inspired architecture. The system is designed to be modular, with each function being small and designed optimally for potential future reuse.

When breaking down the task, consider the following:

- Each function should be as small as possible and do one thing well.
- Use existing functions where possible. You have access to functions such as 'gpt_call', 'find_similar_function', and others in our function database.
- Functions can depend on each other. Use 'dependencies' to specify which functions a function relies on.
- Functions should include appropriate 'imports' if external libraries are needed.
- Provide the breakdown as a list of functions, where each function includes its 'name', 'description', 'input_parameters', 'output_parameters', 'dependencies', and 'code' (just a placeholder or brief description at this stage).
- Make sure descriptions are detailed so an engineer could build it to spec.
- Every sub function you create should be designed to be reusable by turning things into parameters, vs hardcoding them.

User request:

"{user_input}"

Provide your answer in JSON format as a list of functions. Each function should have the following structure:

{{
  "name": "function_name",
  "description": "Brief description of the function",
  "input_parameters": [{{"name": "param1", "type": "type1"}}, ...],
  "output_parameters": [{{"name": "output", "type": "type"}}, ...],
  "dependencies": ["dependency1", "dependency2", ...],
  "imports": ["import1", "import2", ...],
  "code": "Placeholder or brief description"
}}

Example:

[
  {{
      "name": "process_data",
      "description": "Processes input data",
      "input_parameters": [{{"name": "data", "type": "str"}}],
      "output_parameters": [{{"name": "processed_data", "type": "str"}}],
      "dependencies": [],
      "imports": [],
      "code": "Placeholder for process_data function"
  }},
  {{
      "name": "analyze_data",
      "description": "Analyzes processed data",
      "input_parameters": [{{"name": "processed_data", "type": "str"}}],
      "output_parameters": [{{"name": "analysis_result", "type": "str"}}],
      "dependencies": ["process_data"],
      "imports": [],
      "code": "Placeholder for analyze_data function"
  }}
]

Now, provide the breakdown for the user's request.
"""

      response = gpt_call(prompt)

      # Try to parse the JSON response
      try:
          functions = json.loads(response)
          # Basic validation of the structure
          if isinstance(functions, list) and all('name' in func and 'description' in func for func in functions):
              return functions
          else:
              raise ValueError("Invalid JSON structure")
      except Exception as e:
          # If parsing fails, retry
          continue

@func.register_function(
  metadata={"description": "Decides if imports or external APIs are needed"},
  dependencies=["gpt_call", "get_all_functions_wrapper"]
)
def decide_imports_and_apis(context):
  import json
  while True:
      # Get all available functions and their imports
      all_functions = get_all_functions_wrapper()
      existing_imports = set()
      for func in all_functions:
          existing_imports.update(func.get('imports', []))

      # Prepare the prompt
      prompt = f"""
You are an expert software assistant helping to decide what imports and external APIs are needed for a set of functions based on the context provided.

Context:

{context}

Existing standard Python imports:

{list(existing_imports)}

Determine the libraries (imports) and external APIs needed for these functions. Separate standard Python libraries from external libraries or APIs.

Provide your answer in the following JSON format:

{{
  "standard_imports": ["import1", "import2", ...],
  "external_imports": ["external_import1", "external_import2", ...],
  "external_apis": ["api1", "api2", ...],
  "documentation_needed": [
      {{"name": "external_import1", "type": "import" or "api"}},
      ...
  ]
}}

Note: 'documentation_needed' should include any external imports or APIs for which documentation should be looked up.

Example:

{{
  "standard_imports": ["os", "json"],
  "external_imports": ["requests"],
  "external_apis": ["SerpAPI"],
  "documentation_needed": [
      {{"name": "requests", "type": "import"}},
      {{"name": "SerpAPI", "type": "api"}}
  ]
}}

Now, analyze the context and provide the JSON response.
"""

      response = gpt_call(prompt)

      # Try to parse the JSON response
      try:
          result = json.loads(response)
          # Basic validation of the structure
          if all(key in result for key in ['standard_imports', 'external_imports', 'external_apis', 'documentation_needed']):
              return result
          else:
              raise ValueError("Invalid JSON structure")
      except Exception as e:
          # If parsing fails, retry
          continue

@func.register_function(
  metadata={"description": "Gets functions that depend on a given function"},
  dependencies=["get_all_functions_wrapper"]
)
def get_functions_that_depend_on(function_name):
  all_functions = get_all_functions_wrapper()
  dependent_functions = []
  for function in all_functions:
      if function_name in function.get('dependencies', []):
          dependent_functions.append(function['name'])
  return dependent_functions


@func.register_function(
    metadata={"description": "Generates the function code using LLM"},
    dependencies=["gpt_call", "get_function_wrapper", "get_functions_that_depend_on", "get_all_functions_wrapper"]
)
def generate_function_code(function, context):
    while True:

        print("\033[1;32mGenerating code for function: ", function["name"], "\033[0m")
        # Gather dependent functions and their code
        dependencies = function.get('dependencies', [])
        dependency_code = ''
        for dep in dependencies:
            dep_function = get_function_wrapper(dep)
            if dep_function:
                dependency_code += f"\n# Code for dependency function '{dep}':\n{dep_function['code']}\n"

        # Gather functions that depend on the same imports
        imports = function.get('imports', [])
        functions_with_same_imports = []
        all_functions = get_all_functions_wrapper()
        for func_with_imports in all_functions:
            if set(func_with_imports.get('imports', [])) & set(imports):
                functions_with_same_imports.append(func_with_imports)

        similar_imports_functions_code = ''
        for func_with_imports in functions_with_same_imports:
            similar_imports_functions_code += f"\n# Code for function '{func_with_imports['name']}' that uses similar imports:\n{func_with_imports['code']}\n"

        # Prepare the prompt
        prompt = f"""
You are an expert Python programmer. Your task is to write detailed and working code for the following function based on the context provided. Do not provide placeholder code, but rather do your best like you are the best senior engineer in the world and provide the best code possible. DO NOT PROVIDE PLACEHOLDER CODE.

Function details:

Name: {function['name']}
Description: {function['description']}
Input parameters: {function['input_parameters']}
Output parameters: {function['output_parameters']}
Dependencies: {function['dependencies']}
Imports: {function['imports']}

Overall context:

{context}

Dependency code:

{dependency_code}

Code from functions with similar imports:

{similar_imports_functions_code}

Please provide the function details in JSON format, following this structure:

{{
  "function_name": "<function_name>",
  "metadata": {{
    "description": "<function_description>",
    "input_parameters": {function['input_parameters']},
    "output_parameters": {function['output_parameters']}
  }},
  "code": "<function_code_as_string>",
  "imports": {function['imports']},
  "dependencies": {function['dependencies']},
  "key_dependencies": [],
  "triggers": []
}}

**Example JSON Output:**

{{
  "function_name": "example_function",
  "metadata": {{
    "description": "An example function.",
    "input_parameters": [{{"name": "param1", "type": "str"}}],
    "output_parameters": [{{"name": "result", "type": "str"}}]
  }},
  "code": "<complete function code goes here>",
  "imports": ["os"],
  "dependencies": [],
  "key_dependencies": [],
  "triggers": []
}}

Provide the JSON output only, without any additional text. Do not provide placeholder code, but write complete code that is ready to run and provide the expected output.

Now, please provide the JSON output for the function '{function['name']}'.
"""

        response = gpt_call(prompt)

        try:
            # Parse the JSON response
            import json
            function_data = json.loads(response)

            # Return the parsed function data
            return function_data
        except json.JSONDecodeError as e:
            # If parsing fails, retry
            print(f"JSON decoding error: {str(e)}")
            continue
        except Exception as e:
            print(f"Error processing function data: {str(e)}")
            return None


@func.register_function(
    metadata={"description": "Creates a new function if similar functions are not sufficient"},
    dependencies=["decide_imports_and_apis", "generate_function_code","add_new_function"]
)
def create_function(function, context):
    # Decide imports and APIs
    imports_and_apis = decide_imports_and_apis(context)
    function['imports'] = imports_and_apis.get('standard_imports', []) + imports_and_apis.get('external_imports', [])

    # Update context with imports and APIs
    context.update({'imports_and_apis': imports_and_apis})

    # Generate function code
    function_data = generate_function_code(function, context)

    if function_data:
        # Register the function using the parsed JSON data
        add_new_function(
            name=function_data['function_name'],
            code=function_data['code'],
            metadata=function_data['metadata'],
            imports=function_data.get('imports', []),
            dependencies=function_data.get('dependencies', []),
            key_dependencies=function_data.get('key_dependencies', []),
            triggers=function_data.get('triggers', [])
        )

        #print(f"Function '{function_data['function_name']}' registered successfully.")

        return {
            'name': function_data['function_name'],
            'code': function_data['code'],
            'metadata': function_data['metadata'],
            'imports': function_data.get('imports', []),
            'dependencies': function_data.get('dependencies', []),
            'key_dependencies': function_data.get('key_dependencies', []),
            'triggers': function_data.get('triggers', [])
        }
    else:
        print("Failed to generate function code.")
        return None



@func.register_function(
  metadata={"description": "Generates the required functions based on the breakdown"},
  dependencies=["find_similar_function", "create_function", "get_function_wrapper"]
)
def generate_functions(function_breakdown, context):
  for function in function_breakdown:
      function_name = function['name']
      # Find similar functions
      similar_functions = find_similar_function(function['description'])
      function_found = False
      for similar_function_name in similar_functions:
          similar_function = get_function_wrapper(similar_function_name)
          if similar_function and similar_function['metadata'].get('description', '') == function['description']:
              function_found = True
              break
      if not function_found:
          # Combine context for this function
          function_context = context.copy()
          function_context.update({'function': function})
          create_function(function, function_context)

@func.register_function(
  metadata={"description": "Runs the final function to produce the output for the user"},
  dependencies=["func"]
)
def run_final_function(function_name, *args, **kwargs):
  result = func.execute_function(function_name, *args, **kwargs)
  return result

@func.register_function(
    metadata={"description": "Extracts parameters from user input for a given function"},
    dependencies=["gpt_call", "get_function_wrapper"]
)
def extract_function_parameters(user_input, function_name):
    import json
    # Get the function code and parameters
    function = get_function_wrapper(function_name)
    if not function:
        print(f"Function '{function_name}' not found.")
        return None

    # Prepare the prompt to convert user input into function parameters
    while True:
        prompt = f"""
You are an expert assistant. The user wants to execute the following function:

Function code:
{function['code']}

Function description:
{function['metadata'].get('description', '')}

Function parameters:
{function['metadata'].get('input_parameters', [])}

The user has provided the following input:
"{user_input}"

Your task is to extract the required parameters from the user's input and provide them in JSON format that matches the function's parameters.

Provide your answer in the following JSON format:
{{
  "parameters": {{
    "param1": value1,
    "param2": value2,
    ...
  }}
}}

Ensure that the parameters match the function's required input parameters.

Examples:

Example 1:

Function code:
def add_numbers(a, b):
    return a + b

Function parameters:
[{{"name": "a", "type": "int"}}, {{"name": "b", "type": "int"}}]

User input: "Add 5 and 3"

Response:
{{
  "parameters": {{
    "a": 5,
    "b": 3
  }}
}}

Example 2:

Function code:
def greet_user(name):
    return f"Hello, {{name}}!"

Function parameters:
[{{"name": "name", "type": "str"}}]

User input: "Say hello to Alice"

Response:
{{
  "parameters": {{
    "name": "Alice"
  }}
}}

Now, using the function provided and the user's input, extract the parameters and provide the JSON response.
"""
        response = gpt_call(prompt)

        # Try to parse the JSON response
        try:
            result = json.loads(response)
            if 'parameters' in result and isinstance(result['parameters'], dict):
                return result['parameters']
            else:
                raise ValueError("Invalid JSON structure")
        except Exception as e:
            # If parsing fails, retry
            continue

@func.register_function(
    metadata={"description": "Main function to process user input and generate the required functions"},
    dependencies=["check_existing_functions", "break_down_task", "generate_functions", "run_final_function", "extract_function_parameters"]
)
def process_user_input(user_input):
    # First, check if an existing function satisfies the user input
    print("\033[1;95mProcessing user input: ", user_input, "\033[0m")
    result = check_existing_functions(user_input)
    if result['function_found']:
        function_name = result['function_name']
    else:
        # Break down the task into functions
        function_breakdown = break_down_task(user_input)
        # Context to be passed around
        context = {'user_input': user_input, 'function_breakdown': function_breakdown}
        # Generate the required functions
        generate_functions(function_breakdown, context)
        # Assume the main function is the first one in the breakdown
        function_name = function_breakdown[0]['name']

    # Extract parameters from user input for the function
    parameters = extract_function_parameters(user_input, function_name)
    if parameters is None:
        print("Failed to extract parameters from user input.")
        return None

    # Call the function with the parameters
    output = run_final_function(function_name, **parameters)
    return output


```

## File: `babyagi/functionz/packs/drafts/generate_function.py`
```python

from functionz.core.framework import func

# Function 1: Fetch existing functions
@func.register_function(
    metadata={"description": "Fetch existing functions using display_functions_wrapper."},
    dependencies=["display_functions_wrapper"],
    imports=[
        {"name": "json", "lib": "json"}
    ]
)
def fetch_existing_functions(description: str) -> dict:
    """
    Fetches existing functions and returns them along with the initial intermediate_steps.

    Args:
        description (str): User description of the function to generate.

    Returns:
        dict: A dictionary containing existing functions and intermediate steps.
    """
    intermediate_steps = []
    try:
        existing_functions = display_functions_wrapper()
        print(f"[DEBUG] Existing Functions: {existing_functions}")
        intermediate_steps.append({"step": "Fetch Existing Functions", "content": existing_functions})
        return {"existing_functions": existing_functions, "intermediate_steps": intermediate_steps}
    except Exception as e:
        print(f"[ERROR] Failed to fetch existing functions: {e}")
        intermediate_steps.append({"step": "Error Fetching Existing Functions", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error fetching existing functions."}

# Function 2: Analyze internal functions
@func.register_function(
    metadata={"description": "Analyze internal functions and identify reusable and reference functions."},
    dependencies=["litellm", "FunctionSuggestion"],
    imports=[
        {"name": "litellm", "lib": "litellm"},
        {"name": "pydantic", "lib": "pydantic"},
        {"name": "typing", "lib": "typing"},
        {"name": "json", "lib": "json"},
    ]
)
def analyze_internal_functions(description: str, existing_functions: str, intermediate_steps: list) -> dict:
    """
    Analyzes existing functions to identify reusable and reference functions.

    Args:
        description (str): User description of the function to generate.
        existing_functions (str): Existing functions obtained from the previous step.
        intermediate_steps (list): List of intermediate steps.

    Returns:
        dict: A dictionary containing updated intermediate steps, reusable_functions, and reference_functions.
    """
    from litellm import completion
    from pydantic import BaseModel, Field, ValidationError
    from typing import List
    import json

    # Define Pydantic model for parsing internal function responses
    class FunctionSuggestion(BaseModel):
        reusable_functions: List[str] = Field(default_factory=list)
        reference_functions: List[str] = Field(default_factory=list)

    # System prompt for code generation adhering to the functionz framework guidelines.
    system_prompt = """
    You are an AI designed to help developers write Python functions using the functionz framework. Every function you generate must adhere to the following rules:

    Function Registration: All functions must be registered with the functionz framework using the @babyagi.register_function() decorator. Each function can include metadata, dependencies, imports, and key dependencies.

    Basic Function Registration Example:

    def function_name(param1, param2):
        # function logic here
        return result

    Metadata and Dependencies: When writing functions, you may include optional metadata (such as descriptions) and dependencies. Dependencies can be other functions or secrets (API keys, etc.).

    Import Handling: Manage imports by specifying them in the decorator as dictionaries with 'name' and 'lib' keys. Include these imports within the function body.

    Secret Management: When using API keys or authentication secrets, reference the stored key with globals()['key_name'].

    Error Handling: Functions should handle errors gracefully, catching exceptions if necessary.

    General Guidelines: Use simple, clean, and readable code. Follow the structure and syntax of the functionz framework. Ensure proper function documentation via metadata.
    """

    display_prompt = f"""You are an assistant helping a developer build a function using the functionz framework.

    The user has provided the following function description: {description}

    The current available functions are listed below. Please specify if any of these functions can be used directly (for reuse), or if any should be referenced while building the new function. Return your response as structured JSON.

    Available Functions:
    {existing_functions}
    """

    # Step 2.1: Make the LLM call using JSON mode with Pydantic model
    try:
        display_response = completion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": display_prompt}
            ],
            response_format=FunctionSuggestion
        )
        print(f"[DEBUG] Display Response: {display_response}")
    except Exception as e:
        print(f"[ERROR] LLM call for FunctionSuggestion failed: {e}")
        intermediate_steps.append({"step": "Error in FunctionSuggestion LLM Call", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error during FunctionSuggestion analysis."}

    # Step 2.2: Access and parse the response
    try:
        content = display_response.choices[0].message.content
        print(f"[DEBUG] Raw Display Content: {content}")
        display_response_parsed = FunctionSuggestion.parse_raw(content)
        print(f"[DEBUG] Parsed FunctionSuggestion: {display_response_parsed}")
        intermediate_steps.append({"step": "Analyze Internal Functions", "content": display_response_parsed.dict()})
    except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
        print(f"[ERROR] Parsing FunctionSuggestion response failed: {e}")
        intermediate_steps.append({"step": "Error Parsing FunctionSuggestion Response", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error parsing FunctionSuggestion response."}

    reusable_functions = display_response_parsed.reusable_functions
    reference_functions = display_response_parsed.reference_functions
    print(f"[DEBUG] Reusable Functions: {reusable_functions}")
    print(f"[DEBUG] Reference Functions: {reference_functions}")

    return {
        "intermediate_steps": intermediate_steps,
        "reusable_functions": reusable_functions,
        "reference_functions": reference_functions
    }

# Function 3: Fetch function codes
@func.register_function(
    metadata={"description": "Fetch function codes for given function names using get_function_wrapper."},
    dependencies=["get_function_wrapper"],
    imports=[
        {"name": "json", "lib": "json"},
        {"name": "typing", "lib": "typing"},
    ]
)
def fetch_function_codes(function_names, intermediate_steps):
    """
    Fetches function codes for given function names.

    Args:
        function_names (List[str]): List of function names to fetch.
        intermediate_steps (list): List of intermediate steps.

    Returns:
        dict: A dictionary containing updated intermediate steps and function_codes.
    """
    from typing import List
    try:
        function_codes = {
            func_name: get_function_wrapper(func_name).get("code", "")
            for func_name in function_names
        }
        print(f"[DEBUG] Function Codes: {function_codes}")
        intermediate_steps.append({"step": "Fetch Function Codes", "content": function_codes})
        return {
            "intermediate_steps": intermediate_steps,
            "function_codes": function_codes
        }
    except Exception as e:
        print(f"[ERROR] Fetching function codes failed: {e}")
        intermediate_steps.append({"step": "Error Fetching Function Codes", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error fetching function codes."}

# Function 4: Determine required external APIs
@func.register_function(
    metadata={"description": "Determine required external APIs based on the user's function description."},
    dependencies=["litellm"],
    imports=[
        {"name": "litellm", "lib": "litellm"},
        {"name": "pydantic", "lib": "pydantic"},
        {"name": "typing", "lib": "typing"},
        {"name": "json", "lib": "json"},
    ]
)
def determine_required_external_apis(description: str, intermediate_steps: list) -> dict:
    """
    Determines required external APIs based on the user's function description.

    Args:
        description (str): User description of the function to generate.
        intermediate_steps (list): List of intermediate steps.

    Returns:
        dict: A dictionary containing updated intermediate steps and external_apis as a list of dictionaries.
    """
    from litellm import completion
    from pydantic import BaseModel, Field, ValidationError, validator
    from typing import List, Optional, Union
    import json

    # Define Pydantic models
    class Endpoint(BaseModel):
        method: Optional[str]
        url: str
        description: Optional[str] = None

    class APIDetails(BaseModel):
        api_name: str = Field(alias="name")  # Use alias to map 'name' to 'api_name'
        purpose: str
        endpoints: Optional[List[Union[Endpoint, str]]] = Field(default_factory=list)

        @validator("endpoints", pre=True, each_item=True)
        def convert_to_endpoint(cls, v):
            """Convert string URLs into Endpoint objects if necessary."""
            if isinstance(v, str):
                return Endpoint(url=v)  # Create an Endpoint object from a URL string
            return v

    class APIResponse(BaseModel):
        name: str
        purpose: str
        endpoints: List[Endpoint]

    # System prompt
    system_prompt = """
    [Your existing system prompt here]
    """

    prompt_for_apis = f"""You are an assistant analyzing function requirements.

    The user has provided the following function description: {description}.

    Identify if this function will require external APIs (including SDKs or libraries). If so, return a structured JSON with a list of external APIs, their purposes, and any relevant endpoints."""

    try:
        api_response = completion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt_for_apis}
            ],
            response_format=APIDetails
        )
        print(f"[DEBUG] API Response: {api_response}")
    except Exception as e:
        print(f"[ERROR] LLM call for APIResponse failed: {e}")
        intermediate_steps.append({"step": "Error in APIResponse LLM Call", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error during APIResponse analysis."}

    # Step 3.2: Access and parse the API response
    try:
        content = api_response.choices[0].message.content
        print(f"[DEBUG] Raw API Content: {content}")
        api_response_parsed = APIResponse.parse_raw(content)
        print(f"[DEBUG] Parsed APIResponse: {api_response_parsed}")
        intermediate_steps.append({"step": "Identify External API", "content": api_response_parsed.dict()})

        # Ensure external_apis is always a list
        external_apis = [api_response_parsed.dict()]  # Wrap in a list
    except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
        print(f"[ERROR] Parsing APIResponse failed: {e}")
        intermediate_steps.append({"step": "Error Parsing APIResponse", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error parsing APIResponse."}

    return {
        "intermediate_steps": intermediate_steps,
        "external_apis": external_apis  # Now a list of dicts
    }



# Function 5: Handle API documentation and extraction
@func.register_function(
    metadata={"description": "Search API documentation and extract relevant information."},
    dependencies=["serpapi_search_v2", "scrape_website", "litellm"],
    key_dependencies=["serpapi_api_key", "firecrawl_api_key"],
    imports=[
        {"name": "litellm", "lib": "litellm"},
        {"name": "pydantic", "lib": "pydantic"},
        {"name": "typing", "lib": "typing"},
        {"name": "json", "lib": "json"},
        {"name": "urllib", "lib": "urllib"},
    ]
)
def handle_api_documentation(api_name: str, description: str, intermediate_steps: list) -> dict:
    """
    Searches API documentation for a given API and extracts relevant information.

    Args:
        api_name (str): Name of the API to search for.
        description (str): User description of the function to generate.
        intermediate_steps (list): List of intermediate steps.

    Returns:
        dict: A dictionary containing updated intermediate steps and api_contexts.
    """
    from litellm import completion
    from pydantic import BaseModel, Field, ValidationError
    from typing import List
    import json
    from urllib.parse import urlparse

    # Define Pydantic models
    class URLSelection(BaseModel):
        selected_urls: List[str] = Field(default_factory=list)

    # Updated ExtractionInfo model with 'requires_more_info'
    class ExtractionInfo(BaseModel):
        relevant_info: str
        additional_urls: List[str] = Field(default_factory=list)
        requires_more_info: bool

    # System prompt
    system_prompt = """
    You are an AI designed to help developers write Python functions using the functionz framework. Every function you generate must adhere to the following rules:

    Function Registration: All functions must be registered with the functionz framework using the @babyagi.register_function() decorator. Each function can include metadata, dependencies, imports, and key dependencies.

    Basic Function Registration Example:

    def function_name(param1, param2):
        # function logic here
        return result

    Metadata and Dependencies: When writing functions, you may include optional metadata (such as descriptions) and dependencies. Dependencies can be other functions or secrets (API keys, etc.).

    Import Handling: Manage imports by specifying them in the decorator as dictionaries with 'name' and 'lib' keys. Include these imports within the function body.

    Secret Management: When using API keys or authentication secrets, reference the stored key with globals()['key_name'].

    Error Handling: Functions should handle errors gracefully, catching exceptions if necessary.

    General Guidelines: Use simple, clean, and readable code. Follow the structure and syntax of the functionz framework. Ensure proper function documentation via metadata.
    """

    # Function to check if a URL is valid
    def is_valid_url(url: str) -> bool:
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    # Function to chunk text
    def chunk_text(text: str, chunk_size: int = 100000, overlap: int = 10000) -> List[str]:
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            if end < len(text):
                # Find the last newline within the overlap
                last_newline = text.rfind('\n', end - overlap, end)
                if last_newline != -1:
                    end = last_newline + 1
            chunks.append(text[start:end])
            start = end - overlap
        return chunks

    search_query = f"{api_name} API documentation python"
    print(f"[DEBUG] Searching for API documentation with query: {search_query}")
    try:
        search_results = serpapi_search_v2(query=search_query)
        print(f"[DEBUG] Search Results for {api_name}: {search_results}")
        intermediate_steps.append({"step": f"Search API Documentation for {api_name}", "content": search_results})
    except Exception as e:
        print(f"[ERROR] serpapi_search_v2 failed for {api_name}: {e}")
        intermediate_steps.append({"step": f"Error Searching API Documentation for {api_name}", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error searching API documentation."}

    link_selection_prompt = f"""You are given the following search results for the query "{search_query}":
    {json.dumps(search_results)}

    Which links seem most relevant for obtaining Python API documentation? Return them as a structured JSON list of URLs."""

    try:
        link_selection_response = completion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": link_selection_prompt}
            ],
            response_format=URLSelection
        )
        print(f"[DEBUG] Link Selection Response for {api_name}: {link_selection_response}")
    except Exception as e:
        print(f"[ERROR] LLM call for URLSelection failed for {api_name}: {e}")
        intermediate_steps.append({"step": f"Error in URLSelection LLM Call for {api_name}", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error in URLSelection LLM call."}

    # Step 4.2: Access and parse the link selection response
    try:
        content = link_selection_response.choices[0].message.content
        print(f"[DEBUG] Raw Link Selection Content for {api_name}: {content}")
        link_selection_parsed = URLSelection.parse_raw(content)
        print(f"[DEBUG] Parsed URLSelection for {api_name}: {link_selection_parsed}")
        intermediate_steps.append({"step": f"Select Relevant URLs for {api_name}", "content": link_selection_parsed.dict()})
    except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
        print(f"[ERROR] Parsing URLSelection response for {api_name} failed: {e}")
        intermediate_steps.append({"step": f"Error Parsing URLSelection Response for {api_name}", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error parsing URLSelection response."}

    selected_urls = link_selection_parsed.selected_urls or []
    print(f"[DEBUG] Selected URLs for {api_name}: {selected_urls}")
    scraped_urls = set()
    api_scrape_info = {}
    api_contexts = []
    accumulated_info = ""  # To accumulate relevant info

    requires_more_info = True  # Initialize to True to start the loop

    # Step 5: Scrape and recursively explore additional URLs until no more info is needed
    while selected_urls and requires_more_info:
        current_url = selected_urls.pop(0)
        print(f"[DEBUG] Scraping URL: {current_url}")
        if current_url in scraped_urls or not is_valid_url(current_url):
            print(f"[DEBUG] URL already scraped or invalid: {current_url}")
            continue

        try:
            scrape_result = scrape_website(current_url)
            print(f"[DEBUG] Scrape Result for {current_url}: {scrape_result}")
        except Exception as e:
            print(f"[ERROR] scrape_website failed for {current_url}: {e}")
            intermediate_steps.append({"step": f"Error Scraping URL: {current_url}", "content": str(e)})
            continue  # Skip to the next URL

        scraped_urls.add(current_url)
        if not scrape_result.get("error"):
            api_scrape_info[current_url] = scrape_result
            intermediate_steps.append({"step": f"Scrape URL: {current_url}", "content": scrape_result})
        else:
            print(f"[WARN] Error in scrape_result for {current_url}: {scrape_result.get('error')}")
            intermediate_steps.append({"step": f"Scrape Error for URL: {current_url}", "content": scrape_result.get("error")})
            continue  # Skip to the next URL

        # Step 6: Use LLM to extract relevant info and decide if more info is needed
        extraction_prompt = f"""The user wants to create a function described as follows: {description}.
You have accumulated the following relevant API information so far:
{accumulated_info}

You have just scraped the following new API documentation:
{json.dumps(scrape_result)}

Based on the new information, extract any additional relevant API methods, endpoints, and usage patterns needed to implement the user's function. Indicate whether more information is required by setting 'requires_more_info' to true or false. If any other URLs should be scraped for further information, include them in the 'additional_urls' field."""

        # Chunk the extraction prompt if it's too long
        extraction_prompt_chunks = chunk_text(extraction_prompt)
        extraction_results = []

        for chunk in extraction_prompt_chunks:
            try:
                extraction_response = completion(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": chunk}
                    ],
                    response_format=ExtractionInfo
                )
                print(f"[DEBUG] Extraction Response: {extraction_response}")
                extraction_results.append(extraction_response)
            except Exception as e:
                print(f"[ERROR] LLM call for ExtractionInfo failed: {e}")
                intermediate_steps.append({"step": "Error in ExtractionInfo LLM Call", "content": str(e)})
                continue  # Skip to the next chunk

        # Combine extraction results
        combined_extraction = {
            "relevant_info": "",
            "additional_urls": [],
            "requires_more_info": False
        }
        for result in extraction_results:
            try:
                content = result.choices[0].message.content
                parsed_result = ExtractionInfo.parse_raw(content)
                combined_extraction["relevant_info"] += parsed_result.relevant_info + "\n"
                combined_extraction["additional_urls"].extend(parsed_result.additional_urls)
                if parsed_result.requires_more_info:
                    combined_extraction["requires_more_info"] = True
            except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
                print(f"[ERROR] Parsing ExtractionInfo response failed: {e}")
                intermediate_steps.append({"step": "Error Parsing ExtractionInfo Response", "content": str(e)})

        # Update accumulated info
        accumulated_info += combined_extraction["relevant_info"]
        print(f"[DEBUG] Updated Accumulated Info: {accumulated_info}")

        # Include extracted info in API contexts
        api_contexts.append(combined_extraction["relevant_info"])
        print(f"[DEBUG] Updated API Contexts: {api_contexts}")

        # Queue additional URLs for scraping
        new_urls = [url for url in combined_extraction["additional_urls"] if url not in scraped_urls and is_valid_url(url)]
        print(f"[DEBUG] New URLs to Scrape: {new_urls}")
        selected_urls.extend(new_urls)

        # Check if more information is required
        requires_more_info = combined_extraction["requires_more_info"]
        print(f"[DEBUG] Requires More Info: {requires_more_info}")

    return {
        "intermediate_steps": intermediate_steps,
        "api_contexts": api_contexts
    }


# Function 6: Generate final function code
@func.register_function(
    metadata={"description": "Generate the final function code using all gathered information."},
    dependencies=["litellm"],
    imports=[
        {"name": "litellm", "lib": "litellm"},
        {"name": "json", "lib": "json"},
        {"name": "typing", "lib": "typing"},
    ]
)
def generate_final_function_code(description: str, reusable_function_code: dict, reference_function_code: dict, api_contexts: list, intermediate_steps: list) -> dict:
    """
    Generates the final function code using all gathered information.

    Args:
        description (str): User description of the function to generate.
        reusable_function_code (dict): Codes of reusable functions.
        reference_function_code (dict): Codes of reference functions.
        api_contexts (list): List of API contexts.
        intermediate_steps (list): List of intermediate steps.

    Returns:
        dict: A dictionary containing updated intermediate steps and the combined final function details.
    """
    from litellm import completion
    from pydantic import BaseModel, Field, ValidationError
    from typing import Dict, Any, List, Optional
    import json

    # Define Pydantic model
    class GeneratedFunction(BaseModel):
        name: str
        code: str
        metadata: Optional[Dict[str, Any]] = Field(default_factory=dict)
        imports: Optional[List[Dict[str, str]]] = Field(default_factory=list)
        dependencies: List[str] = Field(default_factory=list)
        key_dependencies: List[str] = Field(default_factory=list)
        triggers: List[str] = Field(default_factory=list)

        class Config:
            extra = "forbid"

    # System prompt
    system_prompt = """
    You are an AI designed to help developers write Python functions using the functionz framework. Every function you generate must adhere to the following rules:

    Function Registration: All functions must be registered with the functionz framework using the @babyagi.register_function() decorator. Each function can include metadata, dependencies, imports, and key dependencies.

    Basic Function Registration Example:

    def function_name(param1, param2):
        # function logic here
        return result

    Metadata and Dependencies: When writing functions, you may include optional metadata (such as descriptions) and dependencies. Dependencies can be other functions or secrets (API keys, etc.).

    Import Handling: Manage imports by specifying them in the decorator as dictionaries with 'name' and 'lib' keys. Include these imports within the function body.

    Secret Management: When using API keys or authentication secrets, reference the stored key with globals()['key_name'].

    Error Handling: Functions should handle errors gracefully, catching exceptions if necessary.

    General Guidelines: Use simple, clean, and readable code. Follow the structure and syntax of the functionz framework. Ensure proper function documentation via metadata.
    """

    # Function to chunk text
    def chunk_text(text: str, chunk_size: int = 100000, overlap: int = 10000) -> List[str]:
        chunks = []
        start = 0
        while start < len(text):
            end = start + chunk_size
            if end < len(text):
                # Find the last newline within the overlap
                last_newline = text.rfind('\n', end - overlap, end)
                if last_newline != -1:
                    end = last_newline + 1
            chunks.append(text[start:end])
            start = end - overlap
        return chunks

    final_prompt = f"""{system_prompt}

    The user wants to create a function with the following description: {description}.

    You have the following internal reusable functions:
    {json.dumps(reusable_function_code)}

    You have the following internal reference functions:
    {json.dumps(reference_function_code)}

    You have the following context on the necessary external APIs and their usage:
    {json.dumps(api_contexts)}

    Generate a complete function using the functionz framework that adheres to the provided guidelines and utilizes the specified internal and external functions. Ensure the function is registered with the correct metadata, dependencies, and includes all relevant imports.

    Provide the function details in a structured format including:
    1. Function name
    2. Complete function code (do not the @babyagi.register_function decorator)
    3. Metadata (description)
    4. Imports
    5. Dependencies
    6. Key dependencies
    7. Triggers (if any)
    """

    # Chunk the final prompt if it's too long
    final_prompt_chunks = chunk_text(final_prompt)
    final_results = []

    for chunk in final_prompt_chunks:
        try:
            final_response = completion(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": chunk}
                ],
                response_format=GeneratedFunction
            )
            print(f"[DEBUG] Final Response: {final_response}")
            final_results.append(final_response)
        except Exception as e:
            print(f"[ERROR] LLM call for GeneratedFunction failed: {e}")
            intermediate_steps.append({"step": "Error in GeneratedFunction LLM Call", "content": str(e)})
            return {"intermediate_steps": intermediate_steps, "error": "# Error during GeneratedFunction generation."}

    # Combine final results
    combined_final = {
        "name": "",
        "code": "",
        "metadata": {},
        "imports": [],
        "dependencies": [],
        "key_dependencies": [],
        "triggers": []
    }
    for result in final_results:
        try:
            content = result.choices[0].message.content
            parsed_result = GeneratedFunction.parse_raw(content)
            if not combined_final["name"]:
                combined_final["name"] = parsed_result.name
            combined_final["code"] += parsed_result.code + "\n"
            if parsed_result.metadata:
                combined_final["metadata"].update(parsed_result.metadata or {})
            if parsed_result.imports:
                combined_final["imports"].extend(parsed_result.imports)
            if parsed_result.dependencies:
                combined_final["dependencies"].extend(parsed_result.dependencies)
            if parsed_result.key_dependencies:
                combined_final["key_dependencies"].extend(parsed_result.key_dependencies)
            if parsed_result.triggers:
                combined_final["triggers"].extend(parsed_result.triggers)

        except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
            print(f"[ERROR] Parsing GeneratedFunction response failed: {e}")
            intermediate_steps.append({"step": "Error Parsing GeneratedFunction Response", "content": str(e)})
            return {"intermediate_steps": intermediate_steps, "error": "# Error parsing GeneratedFunction response."}

    # Remove duplicates from lists
    combined_final["imports"] = list({json.dumps(imp): imp for imp in combined_final["imports"]}.values())
    combined_final["dependencies"] = list(set(combined_final["dependencies"]))
    combined_final["key_dependencies"] = list(set(combined_final["key_dependencies"]))
    combined_final["triggers"] = list(set(combined_final["triggers"]))

    print(f"[DEBUG] Combined Final GeneratedFunction: {combined_final}")
    intermediate_steps.append({"step": "Generate Final Function", "content": combined_final})

    return {
        "intermediate_steps": intermediate_steps,
        "combined_final": combined_final
    }

# Function 7: Add function to database
@func.register_function(
    metadata={"description": "Add the generated function to the database."},
    dependencies=["add_new_function"],
    imports=[
        {"name": "json", "lib": "json"},
    ]
)
def add_function_to_database(combined_final: dict, intermediate_steps: list) -> dict:
    """
    Adds the generated function to the database.

    Args:
        combined_final (dict): The combined final function details.
        intermediate_steps (list): List of intermediate steps.

    Returns:
        dict: A dictionary containing updated intermediate steps and the success status.
    """
    try:
        success = add_new_function(
            name=combined_final["name"],
            code=combined_final["code"],
            metadata=combined_final["metadata"],
            imports=combined_final["imports"],
            dependencies=combined_final["dependencies"],
            key_dependencies=combined_final["key_dependencies"],
            triggers=combined_final["triggers"]
        )
        intermediate_steps.append({"step": "Add Function to Database", "content": {"success": success}})
    except Exception as e:
        print(f"[ERROR] Failed to add function to database: {e}")
        intermediate_steps.append({"step": "Error Adding Function to Database", "content": str(e)})
        success = False

    return {
        "intermediate_steps": intermediate_steps,
        "success": success
    }

# Main Function: Orchestrate all steps
@func.register_function(
    metadata={"description": "Main function to generate a function from a description."},
    dependencies=[
        "fetch_existing_functions",
        "analyze_internal_functions",
        "fetch_function_codes",
        "determine_required_external_apis",
        "handle_api_documentation",
        "generate_final_function_code",
        "add_function_to_database"
    ],
    imports=[
        {"name": "json", "lib": "json"},
        {"name": "typing", "lib": "typing"},
    ]
)
def generate_function_from_description(description: str) -> dict:
    """
    Main function that generates a Python function based on a user-provided description.

    Args:
        description (str): User description of the function to generate.

    Returns:
        dict: A dictionary containing intermediate steps, the final generated function code, and whether it was successfully added to the database.
    """
    intermediate_steps = []

    # Step 1: Fetch existing functions
    result = fetch_existing_functions(description)
    if "error" in result:
        return {"intermediate_steps": result["intermediate_steps"], "final_code": result["error"], "added_to_database": False}
    existing_functions = result["existing_functions"]
    intermediate_steps.extend(result["intermediate_steps"])

    # Step 2: Analyze internal functions
    result = analyze_internal_functions(description, existing_functions, intermediate_steps)
    if "error" in result:
        return {"intermediate_steps": result["intermediate_steps"], "final_code": result["error"], "added_to_database": False}
    intermediate_steps = result["intermediate_steps"]
    reusable_functions = result["reusable_functions"]
    reference_functions = result["reference_functions"]

    # Step 3: Fetch function codes for reusable and reference functions
    reusable_function_code = {}
    if reusable_functions:
        result = fetch_function_codes(reusable_functions, intermediate_steps)
        if "error" in result:
            return {"intermediate_steps": result["intermediate_steps"], "final_code": result["error"], "added_to_database": False}
        intermediate_steps = result["intermediate_steps"]
        reusable_function_code = result["function_codes"]

    reference_function_code = {}
    if reference_functions:
        result = fetch_function_codes(reference_functions, intermediate_steps)
        if "error" in result:
            return {"intermediate_steps": result["intermediate_steps"], "final_code": result["error"], "added_to_database": False}
        intermediate_steps = result["intermediate_steps"]
        reference_function_code = result["function_codes"]

    # Step 4: Determine required external APIs
    result = determine_required_external_apis(description, intermediate_steps)
    if "error" in result:
        return {"intermediate_steps": result["intermediate_steps"], "final_code": result["error"], "added_to_database": False}
    intermediate_steps = result["intermediate_steps"]
    external_apis_dicts = result["external_apis"]

    # Ensure external_apis_dicts is a list
    if not isinstance(external_apis_dicts, list):
        external_apis_dicts = [external_apis_dicts]

    # Reconstruct APIResponse objects from dicts
    from typing import Optional, List
    from pydantic import BaseModel

    class Endpoint(BaseModel):
        method: Optional[str]
        url: str
        description: Optional[str] = None

    class APIResponse(BaseModel):
        name: str
        purpose: str
        endpoints: List[Endpoint]

    external_apis = []
    for api_dict in external_apis_dicts:
        api_response_parsed = APIResponse(**api_dict)
        external_apis.append(api_response_parsed)

    # Step 5: Handle API documentation and extract contexts
    api_contexts = []
    for api_response_parsed in external_apis:
        api_name = api_response_parsed.name
        result = handle_api_documentation(api_name, description, intermediate_steps)
        if "error" in result:
            return {"intermediate_steps": result["intermediate_steps"], "final_code": result["error"], "added_to_database": False}
        intermediate_steps = result["intermediate_steps"]
        api_contexts.extend(result["api_contexts"])

    # Step 6: Generate final function code
    result = generate_final_function_code(description, reusable_function_code, reference_function_code, api_contexts, intermediate_steps)
    if "error" in result:
        return {"intermediate_steps": result["intermediate_steps"], "final_code": result["error"], "added_to_database": False}
    intermediate_steps = result["intermediate_steps"]
    combined_final = result["combined_final"]

    # Step 7: Add function to database
    result = add_function_to_database(combined_final, intermediate_steps)
    intermediate_steps = result["intermediate_steps"]
    success = result["success"]

    return {
        "intermediate_steps": intermediate_steps,
        "final_code": combined_final["code"],
        "added_to_database": success
    }
```

## File: `babyagi/functionz/packs/drafts/react_agent.py`
```python
from functionz.core.framework import func

@func.register_function(
    metadata={
        "description": "An agent that takes an input, plans using LLM, executes actions using functions from display_functions_wrapper(), and continues until the task is complete using chain-of-thought techniques while providing detailed reasoning and function execution steps."
    },
    imports=["litellm", "json", "copy"],
    dependencies=["get_function_wrapper", "execute_function_wrapper", "get_all_functions_wrapper"],
    key_dependencies=["OPENAI_API_KEY"]
)
def react_agent(input_text) -> str:
    def map_python_type_to_json(python_type: str) -> dict:
        type_mapping = {
            "str": {"type": "string"},
            "int": {"type": "integer"},
            "float": {"type": "number"},
            "bool": {"type": "boolean"},
            "list": {"type": "array", "items": {"type": "string"}},
            "dict": {"type": "object"},
            "Any": {"type": "string"}
        }
        return type_mapping.get(python_type, {"type": "string"})

    try:
        # Enable verbose logging for LiteLLM
        litellm.set_verbose = True

        # Get available functions using get_all_functions_wrapper
        all_functions = get_all_functions_wrapper()

        # Extract function names from the structured data
        available_function_names = [func_info['name'] for func_info in all_functions]

        # Fetch available functions from the database
        tools = []
        for func_name in available_function_names:
            # Retrieve function details using get_function_wrapper
            function_data = get_function_wrapper(func_name)
            if function_data:
                # Construct the tool definition for LiteLLM
                tool = {
                    "type": "function",
                    "function": {
                        "name": function_data['name'],
                        "description": function_data['metadata'].get('description', ''),
                        "parameters": {
                            "type": "object",
                            "properties": {},
                            "required": []
                        },
                    },
                }

                # Map input_parameters to the tool's parameters
                for param in function_data.get('input_parameters', []):
                    json_schema = map_python_type_to_json(param['type'])
                    tool['function']['parameters']['properties'][param['name']] = {
                        **json_schema,
                        "description": param.get('description', '')
                    }
                    if param.get('required', False):
                        tool['function']['parameters']['required'].append(param['name'])

                tools.append(tool)
            else:
                raise ValueError(f"Function '{func_name}' not found in the database.")

        # Initialize function call history
        function_call_history = []

        # Initialize chat context with system message
        system_prompt = (
            "You are an AI assistant that uses a chain-of-thought reasoning process to solve tasks. "
            "Let's think step by step to solve the following problem. "
            "You have access to the following functions which you can use to complete the task. "
            "Explain your reasoning in detail, including any functions you use and their outputs. "
            "At the end of your reasoning, provide the final answer after 'Answer:'. "
            "Before finalizing, review your reasoning for any errors or inconsistencies. "
            "Avoid repeating function calls with the same arguments you've already tried. "
            "Here is the history of function calls you have made so far: {{function_call_history}}"
        )

        chat_context = [
            {"role": "system", "content": system_prompt.replace("{{function_call_history}}", "None")},
            {"role": "user", "content": input_text},
        ]

        # Initialize loop parameters
        max_iterations = 5
        iteration = 0

        full_reasoning_path = ""

        while iteration < max_iterations:
            iteration += 1

            # Update the system prompt with the current function call history
            if function_call_history:
                history_str = "\n".join([
                    f"- {call['function_name']} with arguments {call['arguments']} produced output: {call['output']}"
                    for call in function_call_history
                ])
            else:
                history_str = "None"

            chat_context[0]['content'] = system_prompt.replace("{{function_call_history}}", history_str)

            # Call LiteLLM's completion API with the chat context and tools
            response = litellm.completion(
                model="gpt-4-turbo",
                messages=chat_context,
                tools=tools,
                tool_choice="auto",
                max_tokens=1500,
                temperature=0.7
            )

            # Extract the message from the response
            response_message = response['choices'][0]['message']

            # Append the assistant's message to the chat context and full reasoning path
            chat_context.append(response_message)
            full_reasoning_path += f"\nIteration {iteration}:\n{response_message['content']}\n"

            # Check if the assistant wants to call any functions
            tool_calls = response_message.get('tool_calls', [])

            if tool_calls:
                for tool_call in tool_calls:
                    function_name = tool_call['function']['name']
                    function_args = json.loads(tool_call['function']['arguments'])
                    tool_call_id = tool_call['id']

                    # Check if this function call with these arguments has already been made
                    if any(
                        call['function_name'] == function_name and call['arguments'] == function_args
                        for call in function_call_history
                    ):
                        function_response = f"Function '{function_name}' with arguments {function_args} has already been called. Please try a different approach."
                    else:
                        # Execute the function using execute_function_wrapper
                        try:
                            function_output = execute_function_wrapper(function_name, **function_args)
                            function_call_history.append({
                                'function_name': function_name,
                                'arguments': function_args,
                                'output': function_output
                            })
                            function_response = f"Function '{function_name}' executed successfully with output: {function_output}"
                        except Exception as e:
                            function_response = f"Error executing function '{function_name}': {str(e)}"

                    # Ensure function_response is a string
                    if not isinstance(function_response, str):
                        function_response = json.dumps(function_response)

                    # Append the function response to the chat context and full reasoning path
                    chat_context.append({
                        "tool_call_id": tool_call_id,
                        "role": "tool",
                        "name": function_name,
                        "content": function_response
                    })
                    full_reasoning_path += f"Function Call: {function_name}\nArguments: {function_args}\nOutput: {function_response}\n"

                # Continue the loop to allow the assistant to process the function outputs
                continue
            else:
                # No function calls, assume task is complete
                break

        # Extract the final answer from the last assistant message
        final_answer = response_message['content'].split('Answer:')[-1].strip() if 'Answer:' in response_message['content'] else response_message['content']

        # Compile the full response including reasoning steps and function call history
        if function_call_history:
            function_calls_str = "\n".join([
                f"Function '{call['function_name']}' called with arguments {call['arguments']}, produced output: {call['output']}"
                for call in function_call_history
            ])
        else:
            function_calls_str = "No functions were called."

        full_response = (
            f"Full Reasoning Path:\n{full_reasoning_path}\n\n"
            f"Functions Used:\n{function_calls_str}\n\n"
            f"Final Answer:\n{final_answer}"
        )

        return full_response

    except Exception as e:
        return f"An error occurred: {str(e)}\n\nFull reasoning path so far:\n{full_reasoning_path}"
```

## File: `babyagi/functionz/packs/drafts/self_build.py`
```python
# self_build.py

from functionz.core.framework import func
import json

@func.register_function(
    metadata={"description": "Generates queries based on user description"},
    dependencies=["gpt_call"],
    imports=["json"]
)
def generate_queries(user_description, X=3, max_retries=3):
    """
    Generates X distinct queries that require action based on the user description using gpt_call. 

    Args:
        user_description (str): Description of the user or their needs.
        X (int, optional): Number of queries to generate. Defaults to 3.
        max_retries (int, optional): Maximum number of retries for generating valid queries. Defaults to 3.

    Returns:
        list: A list of generated queries.

    Raises:
        ValueError: If unable to generate valid queries within the retry limit.
    """
    prompt = f"""
You are an AI assistant. Based on the following user description, generate {X} distinct queries that such a user might ask:

User Description:
"{user_description}"

Provide the queries in JSON format as a list:

[
  "Query 1",
  "Query 2",
  ...
]

Ensure the queries are diverse, relevant to the user description, and represent realistic questions that this user might ask. Make requests that require action, such as using tools and APIs, which you should specify in the request. Based on the user description, guess what types of tools they use and specify them in the query.
"""

    errors = []  # To collect error messages from each attempt

    for attempt in range(1, max_retries + 1):
        response = gpt_call(prompt)
        try:
            queries = json.loads(response)
            if isinstance(queries, list) and len(queries) == X and all(isinstance(q, str) for q in queries):
                return queries
            else:
                error_message = (
                    f"Attempt {attempt}: Invalid JSON structure or incorrect number of queries. "
                    f"Expected {X} string queries, but received: {response}"
                )
                errors.append(error_message)
        except json.JSONDecodeError as e:
            error_message = (
                f"Attempt {attempt}: JSON decoding failed with error: {str(e)}. "
                f"Response received: {response}"
            )
            errors.append(error_message)
        except Exception as e:
            error_message = (
                f"Attempt {attempt}: An unexpected error occurred: {str(e)}. "
                f"Response received: {response}"
            )
            errors.append(error_message)

    # After all attempts, raise an error with all collected messages
    full_error_message = " | ".join(errors)
    raise ValueError(f"Failed to generate {X} valid queries after {max_retries} attempts. Errors: {full_error_message}")


@func.register_function(
    metadata={"description": "Processes generated queries based on user description"},
    dependencies=["generate_queries", "process_user_input"],
    imports=["json"]
)
def self_build(user_description, X=3):
    """
    Generates queries based on the user description and processes each query.

    Args:
        user_description (str): Description of the user or their needs.
        X (int, optional): Number of queries to generate and process. Defaults to 3.

    Returns:
        list: A list of dictionaries containing each query and its corresponding output.

    Raises:
        ValueError: If query generation fails.
    """
    try:

        print("\033[1;33mUser Description: ", user_description, "\033[0m")
        # Generate queries
        queries = generate_queries(user_description, X)
    except ValueError as e:
        # Log the error message for debugging
        print(f"Error in generate_queries: {str(e)}")
        return []

    print("\033[1;34mQueries generated by self_build: ", queries, "\033[0m")
    results = []
    for idx, query in enumerate(queries, start=1):
        try:
            output = process_user_input(query)
            results.append({'query': query, 'output': output})
        except Exception as e:
            # Log the error message for debugging
            print(f"Error processing query {idx} ('{query}'): {str(e)}")
            results.append({'query': query, 'output': None, 'error': str(e)})

    return results
```

## File: `babyagi/functionz/packs/drafts/self_build2.py`
```python
from functionz.core.framework import func

@func.register_function(
    metadata={
        "name": "generate_and_process_queries",
        "description": "Generates a specified number of synthetic queries based on a user description and processes each query using the choose_or_create_function.",
        "input_parameters": {
            "user_description": "A detailed description provided by the user.",
            "num_queries": "An integer specifying the number of synthetic queries to generate."
        },
        "output": "A dictionary containing the results of each processed query along with intermediate steps and any errors."
    },
    dependencies=[
        "choose_or_create_function",
        "litellm.completion",
    ],
    imports=[
        {"name": "litellm", "lib": "litellm"},
        {"name": "pydantic", "lib": "pydantic"},
        {"name": "typing", "lib": "typing"},
        {"name": "json", "lib": "json"},
    ]
)
def generate_and_process_queries(user_description: str, num_queries: int) -> dict:
    """
    Generates X synthetic queries based on the user description and processes each query
    using the choose_or_create_function.

    Args:
        user_description (str): The user's description to base synthetic queries on.
        num_queries (int): The number of synthetic queries to generate.

    Returns:
        dict: A dictionary containing the results of each query execution, intermediate steps, and any relevant information.
    """
    from litellm import completion
    from pydantic import BaseModel, Field, ValidationError
    from typing import List, Dict, Any
    import json

    intermediate_steps = []
    results = []

    # Step 1: Generate synthetic queries based on the user description
    system_prompt = """
You are an AI assistant specialized in generating relevant and distinct queries based on a given description.

Given a user description, generate a specified number of unique and diverse queries that a user might ask an AI assistant.
Ensure that the queries are varied and cover different aspects of the description.

Return your response in the following JSON format:

{
    "queries": [
        "First synthetic query.",
        "Second synthetic query.",
        ...
    ]
}

Provide only the JSON response, without any additional text.
"""

    class QueryGenerationResponse(BaseModel):
        queries: List[str] = Field(..., description="A list of generated synthetic queries.")

    generation_prompt = f"""
User Description:
\"\"\"{user_description}\"\"\"

Number of Queries to Generate:
{num_queries}
"""

    try:
        generation_response = completion(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": generation_prompt}
            ],
            response_format=QueryGenerationResponse
        )
        print(f"[DEBUG] Generation Response: {generation_response}")
    except Exception as e:
        print(f"[ERROR] LLM call for query generation failed: {e}")
        intermediate_steps.append({"step": "Error in Query Generation LLM Call", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error generating synthetic queries."}

    # Parse the response
    try:
        content = generation_response.choices[0].message.content
        print(f"[DEBUG] Raw Generation Content: {content}")
        generation_parsed = QueryGenerationResponse.parse_raw(content)
        print(f"[DEBUG] Parsed Query Generation: {generation_parsed}")
        intermediate_steps.append({"step": "Generate Synthetic Queries", "content": generation_parsed.dict()})
    except (ValidationError, IndexError, AttributeError, json.JSONDecodeError) as e:
        print(f"[ERROR] Parsing query generation response failed: {e}")
        intermediate_steps.append({"step": "Error Parsing Query Generation Response", "content": str(e)})
        return {"intermediate_steps": intermediate_steps, "error": "# Error parsing synthetic queries."}

    synthetic_queries = generation_parsed.queries

    if not synthetic_queries or len(synthetic_queries) != num_queries:
        print(f"[ERROR] Number of generated queries does not match the requested number.")
        intermediate_steps.append({
            "step": "Query Count Mismatch",
            "content": f"Requested: {num_queries}, Generated: {len(synthetic_queries)}"
        })
        return {
            "intermediate_steps": intermediate_steps,
            "error": "# The number of generated queries does not match the requested number."
        }

    # Step 2: Process each synthetic query using choose_or_create_function
    for idx, query in enumerate(synthetic_queries, start=1):
        intermediate_steps.append({"step": f"Processing Query {idx}", "content": query})
        try:
            # Assuming choose_or_create_function is accessible within the scope
            # If it's in a different module, you might need to import it accordingly
            query_result = choose_or_create_function(query)
            results.append({
                "query": query,
                "result": query_result.get("execution_result"),
                "intermediate_steps": query_result.get("intermediate_steps", [])
            })
            intermediate_steps.append({
                "step": f"Executed Query {idx}",
                "content": query_result.get("execution_result")
            })
        except Exception as e:
            print(f"[ERROR] Processing query {idx} failed: {e}")
            intermediate_steps.append({
                "step": f"Error Processing Query {idx}",
                "content": str(e)
            })
            results.append({
                "query": query,
                "error": f"# Error processing query: {e}"
            })

    return {
        "intermediate_steps": intermediate_steps,
        "results": results
    }
```

## File: `babyagi/functionz/packs/drafts/user_db.py`
```python
# packs/user_db.py

from PythonFunc.core.framework import func

@func.register_function(
    metadata={"description": "Base UserDB class for database operations."},
    imports=["sqlalchemy", "contextlib"]
)
def get_user_db_class():
    from sqlalchemy import create_engine, Column, Integer, String, MetaData
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy.orm import sessionmaker
    from contextlib import contextmanager
    from sqlalchemy.exc import SQLAlchemyError

    class UserDB:
        def __init__(self, db_url='sqlite:///user_db.sqlite'):
            self.engine = create_engine(db_url)
            self.Session = sessionmaker(bind=self.engine)
            self.metadata = MetaData()
            self.Base = declarative_base(metadata=self.metadata)

        @contextmanager
        def session_scope(self):
            session = self.Session()
            try:
                yield session
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                raise e
            finally:
                session.close()

    return UserDB.__name__  # Return the name of the class instead of the class itself

@func.register_function(
    metadata={"description": "Create a new database."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy"]
)
def create_database(db_name: str, db_type: str = 'sqlite', **kwargs):
    from sqlalchemy import create_engine, MetaData

    if db_type == 'sqlite':
        db_url = f'sqlite:///{db_name}.sqlite'
    elif db_type == 'postgresql':
        db_url = f'postgresql://{kwargs.get("user")}:{kwargs.get("password")}@{kwargs.get("host", "localhost")}:{kwargs.get("port", 5432)}/{db_name}'
    elif db_type == 'mysql':
        db_url = f'mysql+pymysql://{kwargs.get("user")}:{kwargs.get("password")}@{kwargs.get("host", "localhost")}:{kwargs.get("port", 3306)}/{db_name}'
    else:
        raise ValueError(f"Unsupported database type: {db_type}")

    UserDB_name = func.get_user_db_class()
    # Reconstruct the UserDB class
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })

    user_db = UserDB(db_url)  # Pass db_url here

    new_engine = create_engine(db_url)
    user_db.metadata.create_all(new_engine)
    return f"Database '{db_name}' created successfully."


@func.register_function(
    metadata={"description": "List all SQLite databases."},
    dependencies=["get_user_db_class"],
    imports=["os", "sqlalchemy"]
)
def list_databases():
    import os
    from sqlalchemy import create_engine, MetaData
    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })
    # This function doesn't actually use UserDB, but we include it for consistency
    return [f for f in os.listdir() if f.endswith('.sqlite')]

@func.register_function(
    metadata={"description": "Delete a database."},
    dependencies=["get_user_db_class"],
    imports=["os", "sqlalchemy"]
)
def delete_database(db_name: str, db_type: str = 'sqlite', **kwargs):
    import os
    from sqlalchemy import create_engine, MetaData
    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })
    # This function doesn't actually use UserDB, but we include it for consistency
    if db_type == 'sqlite':
        os.remove(f'{db_name}.sqlite')
        return f"Database '{db_name}' deleted successfully."
    else:
        raise NotImplementedError(f"Deleting {db_type} databases is not implemented yet.")

@func.register_function(
    metadata={"description": "Create a new table in the database."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy", "json"]  # Added 'json' to imports
)
def create_table(db_name: str, table_name: str, columns: str):
    from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, Boolean, DateTime, LargeBinary
    import json  # Imported json within the function


    try:
        columns = json.loads(columns)
        print("Parsed columns:", columns)  # Debugging statement
    except json.JSONDecodeError as e:
        return f"Invalid JSON for columns: {e}"

    def get_column_type(type_name):
        type_map = {
            'string': String,
            'integer': Integer,
            'float': Float,
            'boolean': Boolean,
            'datetime': DateTime,
            'binary': LargeBinary,
            'embedding': LargeBinary  # We'll use LargeBinary for embeddings
        }
        return type_map.get(type_name.lower(), String)  # Default to String if type not found

    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData(),
    })
    user_db = UserDB(f'sqlite:///{db_name}.sqlite')

    # Create the table
    table = Table(
        table_name,
        user_db.metadata,
        Column('id', Integer, primary_key=True),
        *(Column(col['name'], get_column_type(col['type'])) for col in columns)
    )

    # Create the table in the database
    table.create(user_db.engine, checkfirst=True)

    return f"Table '{table_name}' created successfully in database '{db_name}'."



@func.register_function(
    metadata={"description": "List all tables in a database."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy"]
)
def list_tables(db_name: str):
    from sqlalchemy import create_engine, MetaData
    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })
    user_db = UserDB(f'sqlite:///{db_name}.sqlite')
    user_db.metadata.reflect(user_db.engine)
    return [table.name for table in user_db.metadata.tables.values()]

@func.register_function(
    metadata={"description": "Get details of a specific table."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy"]
)
def get_table(db_name: str, table_name: str):
    from sqlalchemy import create_engine, MetaData, Table
    from sqlalchemy.exc import NoSuchTableError

    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })

    try:
        user_db = UserDB(f'sqlite:///{db_name}.sqlite')
        user_db.metadata.reflect(user_db.engine)

        if table_name in user_db.metadata.tables:
            table = Table(table_name, user_db.metadata, autoload_with=user_db.engine)
            return {
                "name": table.name,
                "columns": [{"name": column.name, "type": str(column.type)} for column in table.columns]
            }
        else:
            return f"Table '{table_name}' not found in database '{db_name}'."
    except NoSuchTableError:
        return f"Table '{table_name}' not found in database '{db_name}'."
    except Exception as e:
        return f"Error getting table details: {str(e)}"
        
@func.register_function(
    metadata={"description": "Update a table by adding new columns."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy", "json"]  # Added 'json' to imports
)
def update_table(db_name: str, table_name: str, new_columns: str):
    from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, Float, Boolean, DateTime, LargeBinary
    from sqlalchemy.schema import CreateTable
    import json  # Imported json within the function

    try:
        new_columns = json.loads(new_columns)
        print("Parsed columns:", new_columns)  # Debugging statement
    except json.JSONDecodeError as e:
        return f"Invalid JSON for columns: {e}"

    def get_column_type(type_name):
        type_map = {
            'string': String,
            'integer': Integer,
            'float': Float,
            'boolean': Boolean,
            'datetime': DateTime,
            'binary': LargeBinary,
            'embedding': LargeBinary  # We'll use LargeBinary for embeddings
        }
        return type_map.get(type_name.lower(), String)  # Default to String if type not found


    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })

    try:
        user_db = UserDB(f'sqlite:///{db_name}.sqlite')
        user_db.metadata.reflect(user_db.engine)

        if table_name not in user_db.metadata.tables:
            return f"Table '{table_name}' not found in database '{db_name}'."

        table = Table(table_name, user_db.metadata, autoload_with=user_db.engine)
        existing_columns = set(column.name for column in table.columns)

        for col in new_columns:
            if col['name'] not in existing_columns:
                new_column = Column(col['name'], get_column_type(col['type']))
                # Generate the SQL statement to add the new column
                alter_stmt = f'ALTER TABLE {table_name} ADD COLUMN {new_column.name} {new_column.type}'
                user_db.engine.execute(alter_stmt)

        # Refresh the table metadata
        user_db.metadata.clear()
        user_db.metadata.reflect(user_db.engine)

        return f"Table '{table_name}' updated successfully in database '{db_name}'."

    except Exception as e:
        return f"An error occurred while updating the table: {e}"


@func.register_function(
    metadata={"description": "Delete a table from the database."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy"]
)
def delete_table(db_name: str, table_name: str):
    from sqlalchemy import create_engine, MetaData, Table
    from sqlalchemy.exc import NoSuchTableError

    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })

    try:
        user_db = UserDB(f'sqlite:///{db_name}.sqlite')
        user_db.metadata.reflect(user_db.engine)

        if table_name in user_db.metadata.tables:
            table = Table(table_name, user_db.metadata, autoload_with=user_db.engine)
            table.drop(user_db.engine)
            user_db.metadata.remove(table)
            return f"Table '{table_name}' deleted successfully from database '{db_name}'."
        else:
            return f"Table '{table_name}' not found in database '{db_name}'."
    except NoSuchTableError:
        return f"Table '{table_name}' not found in database '{db_name}'."
    except Exception as e:
        return f"Error deleting table: {str(e)}"


@func.register_function(
    metadata={"description": "Create a new record in a table."},
    dependencies=["get_user_db_class", "convert_value"],
    imports=["sqlalchemy", "json"]
)
def create_record(db_name: str, table_name: str, data: list):
    from sqlalchemy import create_engine, MetaData, Table, String
    from sqlalchemy.orm import sessionmaker
    import json

    if not isinstance(data_dict, dict):
        return "Error: Data must be a JSON object"

    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })
    user_db = UserDB(f'sqlite:///{db_name}.sqlite')
    user_db.metadata.reflect(user_db.engine)
    table = Table(table_name, user_db.metadata, autoload_with=user_db.engine)
    Session = sessionmaker(bind=user_db.engine)

    # Get column types
    column_types = {c.name: c.type for c in table.columns}

    # Convert input data to appropriate types
    converted_data = {key: func.convert_value(value, column_types.get(key, String)) for key, value in data.items()}

    try:
        with Session() as session:
            ins = table.insert().values(**converted_data)
            session.execute(ins)
            session.commit()
        return f"Record created in table '{table_name}' of database '{db_name}'."
    except Exception as e:
        return f"Error creating record: {str(e)}"
        
def read_records(db_name: str, table_name: str, filters: dict = None):
    from sqlalchemy import create_engine, MetaData, Table
    from sqlalchemy.orm import sessionmaker
    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })
    user_db = UserDB(f'sqlite:///{db_name}.sqlite')
    user_db.metadata.reflect(user_db.engine)
    table = Table(table_name, user_db.metadata, autoload_with=user_db.engine)
    Session = sessionmaker(bind=user_db.engine)
    with Session() as session:
        query = session.query(table)
        if filters:
            query = query.filter_by(**filters)
        return [dict(row) for row in query.all()]

@func.register_function(
    metadata={"description": "Update a record in a table."},
    dependencies=["get_user_db_class", "convert_value"],
    imports=["sqlalchemy", "json"]
)
def update_record(db_name: str, table_name: str, record_id: int, data: json):
    from sqlalchemy import create_engine, MetaData, Table, String
    from sqlalchemy.orm import sessionmaker
    import json

    if not isinstance(data_dict, dict):
        return "Error: Data must be a JSON object"

    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })
    user_db = UserDB(f'sqlite:///{db_name}.sqlite')
    user_db.metadata.reflect(user_db.engine)
    table = Table(table_name, user_db.metadata, autoload_with=user_db.engine)
    Session = sessionmaker(bind=user_db.engine)

    # Get column types
    column_types = {c.name: c.type for c in table.columns}

    # Convert input data to appropriate types
    converted_data = {key: func.convert_value(value, column_types.get(key, String)) for key, value in data.items()}

    try:
        with Session() as session:
            update = table.update().where(table.c.id == record_id).values(**converted_data)
            result = session.execute(update)
            session.commit()
            if result.rowcount:
                return f"Record {record_id} in table '{table_name}' of database '{db_name}' updated successfully."
            return f"Record {record_id} not found in table '{table_name}' of database '{db_name}'."
    except Exception as e:
        return f"Error updating record: {str(e)}"

@func.register_function(
    metadata={"description": "Delete a record from a table."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy"]
)
def delete_record(db_name: str, table_name: str, record_id: int):
    from sqlalchemy import create_engine, MetaData, Table
    from sqlalchemy.orm import sessionmaker
    UserDB_name = func.get_user_db_class()
    UserDB = type(UserDB_name, (), {
        '__init__': lambda self, db_url: setattr(self, 'engine', create_engine(db_url)),
        'metadata': MetaData()
    })
    user_db = UserDB(f'sqlite:///{db_name}.sqlite')
    user_db.metadata.reflect(user_db.engine)
    table = Table(table_name, user_db.metadata, autoload_with=user_db.engine)
    Session = sessionmaker(bind=user_db.engine)
    with Session() as session:
        delete = table.delete().where(table.c.id == record_id)
        result = session.execute(delete)
        session.commit()
        if result.rowcount:
            return f"Record {record_id} in table '{table_name}' of database '{db_name}' deleted successfully."
        return f"Record {record_id} not found in table '{table_name}' of database '{db_name}'."


@func.register_function(
    metadata={"description": "Convert value to specified SQLAlchemy type"},
    imports=["sqlalchemy", "json", "datetime"]
)
def convert_value(value, target_type):
    from sqlalchemy import Boolean, DateTime, LargeBinary, Integer, Float
    import json
    from datetime import datetime

    if isinstance(value, str):
        if target_type == Boolean:
            return value.lower() in ('true', 'yes', '1', 'on')
        elif target_type == DateTime:
            return datetime.fromisoformat(value)
        elif target_type == LargeBinary:
            try:
                # Assume it's a JSON array for embeddings
                return json.dumps(json.loads(value)).encode('utf-8')
            except json.JSONDecodeError:
                # If not JSON, treat as regular binary data
                return value.encode('utf-8')
        elif target_type in (Integer, Float):
            return target_type(value)
    return value  # Return as-is for String or if already correct type

@func.register_function(
    metadata={"description": "Create a new table in the database."},
    dependencies=["get_user_db_class"],
    imports=["sqlalchemy"]
)
```

## File: `babyagi/functionz/packs/plugins/airtable.py`
```python
from functionz import func

# Initialize the Airtable Table instance
@func.register_function(
    metadata={"description": "Initialize Airtable table instance with access token, base ID, and table name."},
    key_dependencies=["airtable_access_token"],
    imports=["pyairtable"]
)
def init_airtable(base_id, table_name):
    """
    Initialize the Airtable Table instance.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :return: Airtable Table instance
    """
    api_token = globals()["airtable_access_token"]
    from pyairtable import Table
    return Table(api_token, base_id, table_name)


# Create a single record in a given Airtable table
@func.register_function(
    metadata={"description": "Create a new record in a specific Airtable table."},
    dependencies=["init_airtable"]
)
def create_record(base_id, table_name, record_data):
    """
    Create a new record in the specified Airtable table.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param record_data: Dictionary containing record fields and values
    :return: The newly created record
    """
    table = init_airtable(base_id, table_name)
    return table.create(record_data)


# Retrieve a single record by its ID
@func.register_function(
    metadata={"description": "Retrieve a specific record from Airtable using its record ID."},
    dependencies=["init_airtable"]
)
def get_record_by_id(base_id, table_name, record_id):
    """
    Retrieve a record by its unique ID from the specified Airtable table.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param record_id: Unique record ID in Airtable
    :return: The record data as a dictionary
    """
    table = init_airtable(base_id, table_name)
    return table.get(record_id)


# Update an existing record by its ID
@func.register_function(
    metadata={"description": "Update a record in Airtable using its ID and new field values."},
    dependencies=["init_airtable"]
)
def update_record(base_id, table_name, record_id, updated_fields):
    """
    Update a record in Airtable with new values for specified fields.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param record_id: Unique record ID in Airtable
    :param updated_fields: Dictionary with updated field values
    :return: The updated record data as a dictionary
    """
    table = init_airtable(base_id, table_name)
    return table.update(record_id, updated_fields)


# Delete a record by its ID
@func.register_function(
    metadata={"description": "Delete a specific record from an Airtable table."},
    dependencies=["init_airtable"]
)
def delete_record(base_id, table_name, record_id):
    """
    Delete a record from Airtable using its unique ID.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param record_id: Unique record ID in Airtable
    :return: Deletion confirmation message
    """
    table = init_airtable(base_id, table_name)
    return table.delete(record_id)


# Retrieve all records from a table
@func.register_function(
    metadata={"description": "Retrieve all records from a specific Airtable table."},
    dependencies=["init_airtable"]
)
def get_all_records(base_id, table_name, max_records=100, sort_by=None):
    """
    Get all records from the specified table, with optional sorting.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param max_records: Maximum number of records to retrieve
    :param sort_by: Optional list of fields to sort the records by
    :return: List of all records
    """
    table = init_airtable(base_id, table_name)
    return table.all(max_records=max_records, sort=sort_by)


# Upsert multiple records into a table based on unique fields
@func.register_function(
    metadata={"description": "Upsert (create or update) multiple records into a table using unique field identifiers."},
    dependencies=["init_airtable"]
)
def batch_upsert_records(base_id, table_name, records, key_fields):
    """
    Upsert multiple records into the specified table.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param records: List of records to be upserted
    :param key_fields: List of fields to use as unique keys
    :return: List of created or updated records
    """
    table = init_airtable(base_id, table_name)
    return table.batch_upsert(records, key_fields=key_fields)


# Batch create multiple records in a table
@func.register_function(
    metadata={"description": "Create multiple records in a table using batch operations."},
    dependencies=["init_airtable"]
)
def batch_create_records(base_id, table_name, records):
    """
    Create multiple records in the specified table.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param records: List of records to be created
    :return: List of created records
    """
    table = init_airtable(base_id, table_name)
    return table.batch_create(records)


# Batch delete multiple records from a table
@func.register_function(
    metadata={"description": "Delete multiple records in a table using batch operations."},
    dependencies=["init_airtable"]
)
def batch_delete_records(base_id, table_name, record_ids):
    """
    Batch delete records using their unique IDs.
    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param record_ids: List of record IDs to be deleted
    :return: Confirmation messages for deleted records
    """
    table = init_airtable(base_id, table_name)
    return table.batch_delete(record_ids)



from functionz import func

@func.register_function(
    metadata={"description": "Fetch a dynamic number of rows from Airtable based on a flexible search query."},
    dependencies=["init_airtable"],
    imports=["pyairtable"]
)
def get_dynamic_records(base_id, table_name, max_records=100, search_query=None, sort_by=None, fields=None, view=None, page_size=100):
    """
    Fetch a dynamic number of records from an Airtable table based on a custom query.

    :param base_id: ID of the Airtable base
    :param table_name: Name of the table within the base
    :param max_records: Maximum number of records to retrieve
    :param search_query: Dictionary of field-value pairs to match (e.g., {"Name": "Alice", "Age": 30})
    :param sort_by: List of fields to sort the records by (e.g., ["Name", "-Age"])
    :param fields: List of specific fields to retrieve (e.g., ["Name", "Age"])
    :param view: View ID or name to filter the records by
    :param page_size: Number of records per page request
    :return: List of matching records
    """
    from pyairtable.formulas import match
    table = init_airtable(base_id, table_name)

    # Construct a formula using the match function if search_query is provided
    formula = None
    if search_query:
        from pyairtable.formulas import match
        formula = match(search_query)

    # Use iterate to handle large datasets if max_records is set higher than page_size
    records = table.iterate(
        formula=formula,
        sort=sort_by,
        fields=fields,
        view=view,
        page_size=page_size,
        max_records=max_records
    )

    # Collect results from the generator into a list
    return list(records)

```

## File: `babyagi/functionz/packs/plugins/augie.py`
```python
from babyagi.functionz.core.framework import func

@func.register_function(
  metadata={"description": "Generate parameters for Augie creation using GPT."},
  dependencies=["gpt_call"]
)
def generate_augie_params(user_input, voice_id="29vD33N1CtxCmqQRPOHJ"):
  """
  This function generates JSON parameters for creating an Augie video.
  It uses GPT to structure the user input into the required format, keeping the default voice_id.

  Parameters:
  - user_input: The basic user input text.
  - voice_id: Default voice ID (not generated by GPT).

  Returns: A dictionary with the necessary parameters for creating the Augie video.
  """
  prompt = (
      "You are creating parameters for a video generation API request. "
      "The user has provided input text for the video content. Structure the input into the following JSON format:\n"
      "{\n"
      "  'name': '<brief title>',\n"
      "  'text': '<full video content text>',\n"
      "  'orientation': 'landscape' or 'portrait',\n"
      "  'make_video': true or false\n"
      "}\n"
      "Do not generate a voice ID, use the one provided by the API system."
  )

  gpt_output = gpt_call({"prompt": prompt, "user_input": user_input})

  # Parse GPT output and construct parameters
  params = gpt_output['text']  # Assuming gpt_call returns a structured response.
  params['voice_id'] = voice_id  # Set the default voice ID.

  return params


@func.register_function(
  metadata={"description": "Creates a video on Augie platform."},
  key_dependencies=["augie_api_key"],
  imports={"name": "requests", "lib": "requests"}
)
def create_augie(params):
  """Function to create a video on Augie platform with parameters."""
  API_KEY = globals()['augie_api_key']
  BASE_URL = 'https://beta.api.augie.studio/v1'

  headers = {
      'x-api-key': API_KEY,
      'Content-Type': 'application/json'
  }

  import requests
  response = requests.post(f'{BASE_URL}/augies', json=params, headers=headers)

  if response.status_code == 201:
      return response.json()  # Returns the creation response
  else:
      raise Exception(f"Failed to create Augie: {response.text}")


@func.register_function(
  metadata={"description": "Checks the status of the created video."},
  key_dependencies=["augie_api_key"],
  imports={"name": "requests", "lib": "requests"}
)
def get_augie_status(augie_id):
  """Function to check the status of an Augie video creation."""
  API_KEY = globals()['augie_api_key']
  BASE_URL = 'https://beta.api.augie.studio/v1'

  headers = {
      'x-api-key': API_KEY
  }

  import requests
  response = requests.get(f'{BASE_URL}/augies/{augie_id}/status', headers=headers)

  if response.status_code == 200:
      status_data = response.json()
      if status_data.get('status') == 'succeeded' and 'output' in status_data and 'video' in status_data['output']:
          return {"status": "completed", "video_url": status_data['output']['video']}
      else:
          return {"status": "processing"}
  else:
      raise Exception(f"Failed to get Augie status: {response.text}")


@func.register_function(
  metadata={"description": "Wrapper to create a video and keep checking its status until available."},
  dependencies=["generate_augie_params", "create_augie", "get_augie_status"],
  imports={"name": "time", "lib": "time"}
)
def create_and_wait_for_video(user_input, timeout=300, interval=10):
  """
  Wrapper function to create a video from user input and wait for it to be available.
  - user_input: Basic input from the user, processed by GPT.
  - timeout: The max time to wait (in seconds).
  - interval: Time between status checks (in seconds).
  """
  import time

  # Generate parameters using GPT
  params = generate_augie_params(user_input)

  # Create the video
  creation_response = create_augie(params)
  augie_id = creation_response.get('id')

  if not augie_id:
      raise Exception("Failed to retrieve Augie ID after creation.")

  # Wait and check the status periodically
  start_time = time.time()
  while time.time() - start_time < timeout:
      status_response = get_augie_status(augie_id)
      if status_response['status'] == 'completed':
          return status_response  # Return video URL if available
      time.sleep(interval)

  # Timeout reached, return failure
  raise TimeoutError(f"Video creation timed out after {timeout} seconds.")
```

## File: `babyagi/functionz/packs/plugins/e2b.py`
```python
import babyagi

@babyagi.register_function(
    metadata={"description": "Executes AI-generated Python code in a secure E2B sandbox."},
    imports=["e2b_code_interpreter"],
    key_dependencies=["e2b_api_key"]
)
def execute_code_in_sandbox(code: str):
    """
    This function initializes an E2B sandbox and executes AI-generated Python code within it.

    :param code: Python code to be executed.
    :return: Results and logs from the code execution.
    """
    from e2b_code_interpreter import CodeInterpreter
  
    with CodeInterpreter() as sandbox:
        # Execute the code in the sandbox
        execution = sandbox.notebook.exec_cell(code)

        # Handle execution errors
        if execution.error:
            return {"error": execution.error.name, "message": execution.error.value, "traceback": execution.error.traceback}

        # Gather results
        results = [{"text": result.text, "formats": result.formats()} for result in execution.results]
        logs = {"stdout": execution.logs.stdout, "stderr": execution.logs.stderr}

        return {"results": results, "logs": logs}


# Function 2: Chat with LLM (OpenAI) and parse response to execute in sandbox

@babyagi.register_function(
    metadata={"description": "Calls the OpenAI API (gpt-3.5-turbo) to generate code and execute it in an E2B sandbox."},
    imports=["litellm", "os"],
    key_dependencies=["openai_api_key"],
    dependencies=["execute_code_in_sandbox"]
)
def chat_with_llm_and_execute(user_message: str):
    """
    This function calls the OpenAI API (via litellm) to generate Python code based on the user's message,
    then executes that code in an E2B sandbox.

    :param user_message: The message to prompt the LLM with.
    :return: Results from the executed code and logs.
    """
    from litellm import completion
  
    # Load OpenAI API key from environment
    api_key = globals()['openai_api_key']

    # Define the message for the LLM
    messages = [{"role": "user", "content": user_message}]

    # Call the LLM using litellm completion method
    response = completion(model="gpt-3.5-turbo", messages=messages)
    llm_generated_code = response['choices'][0]['message']['content']

    # Execute the generated code in the E2B sandbox
    return execute_code_in_sandbox(llm_generated_code)


# Function 3: Save generated charts

@babyagi.register_function(
    metadata={"description": "Saves a base64-encoded PNG chart to a file."},
    imports=["base64"],
)
def save_chart(base64_png: str, filename: str = "chart.png"):
    """
    Saves a base64-encoded PNG chart to a file.

    :param base64_png: Base64-encoded PNG data.
    :param filename: The name of the file to save the chart.
    :return: The path to the saved chart.
    """
    png_data = base64.b64decode(base64_png)

    # Save the decoded PNG to a file
    with open(filename, "wb") as file:
        file.write(png_data)

    return f"Chart saved to {filename}"


# Function 4: Execute main flow (chat with LLM, run code, save chart if exists)

@babyagi.register_function(
    metadata={"description": "Main function to prompt LLM, execute code in E2B, and save any generated charts."},
    dependencies=["chat_with_llm_and_execute", "save_chart"]
)
def e2b_llm_to_chart(user_message: str):
    """
    The main workflow function: sends a message to the LLM, executes the generated code, and saves any charts.

    :param user_message: The user's input prompt for the LLM.
    :return: Final results and path to saved chart if applicable.
    """
    # Get code execution results and logs
    execution_results = chat_with_llm_and_execute(user_message)

    # Check if any chart (PNG) was generated
    if execution_results["results"]:
        for result in execution_results["results"]:
            if "png" in result["formats"]:
                # Save the chart if PNG format is present
                chart_filename = save_chart(result["formats"]["png"])
                return {"execution_results": execution_results, "chart_saved_to": chart_filename}

    return {"execution_results": execution_results}
```

## File: `babyagi/functionz/packs/plugins/firecrawl.py`
```python
# 1. Crawl a website and initiate a crawl job.
@func.register_function(
    metadata={"description": "Submits a crawl job for a website and returns a job ID."},
    key_dependencies=["firecrawl_api_key"],
    imports={"name":"firecrawl","lib":"firecrawl-py"}
)
def crawl_website(url: str, limit: int = 100, formats: list = ["markdown", "html"], poll_interval: int = 30):
    """
    Submits a crawl job for the given URL and returns the crawl job status and job ID.
    """
    from firecrawl import FirecrawlApp
    api_key = globals()['firecrawl_api_key']
    app = FirecrawlApp(api_key=api_key)

    try:
        crawl_status = app.crawl_url(
            url, 
            params={'limit': limit, 'scrapeOptions': {'formats': formats}},
            poll_interval=poll_interval
        )
        return crawl_status
    except Exception as e:
        return {"error": str(e)}


# 2. Check the status of a crawl job.
@func.register_function(
    metadata={"description": "Checks the status of an ongoing or completed crawl job by its job ID."},
    key_dependencies=["firecrawl_api_key"],
    imports={"name":"firecrawl","lib":"firecrawl-py"}
)
def check_crawl_status(crawl_id: str):
    """
    Checks the status of the crawl job and returns the job details including markdown and HTML data.
    """
    from firecrawl import FirecrawlApp
    api_key = globals()['firecrawl_api_key']
    app = FirecrawlApp(api_key=api_key)

    try:
        crawl_status = app.check_crawl_status(crawl_id)
        return crawl_status
    except Exception as e:
        return {"error": str(e)}


# 3. Scrape a single website URL for markdown and HTML data.
@func.register_function(
    metadata={"description": "Scrapes a single URL and returns markdown and HTML content."},
    key_dependencies=["firecrawl_api_key"],
    imports={"name":"firecrawl","lib":"firecrawl-py"}
)
def scrape_website(url: str, formats: list = ["markdown", "html"]):
    """
    Scrapes the given URL and returns the data (markdown, HTML, and metadata).
    """
    from firecrawl import FirecrawlApp
    api_key = globals()['firecrawl_api_key']
    app = FirecrawlApp(api_key=api_key)

    try:
        scrape_result = app.scrape_url(url, params={'formats': formats})
        return scrape_result
    except Exception as e:
        return {"error": str(e)}
```

## File: `babyagi/functionz/packs/plugins/harmonic.py`
```python
# Harmonic API Functions Pack for Functionz Framework


@func.register_function(
    metadata={"description": "Fetch a company's enrichment data using its identifier (URL or domain)."},
    key_dependencies=["harmonic_api_key"],
    imports=[{"name": "requests", "lib": "requests"}]
)
def harmonic_enrich_company(identifier):
    """
    Enrich a company using its URL, domain, or identifier.
    Returns the full response from Harmonic API.
    """
    api_key = globals()['harmonic_api_key']
    url = "https://api.harmonic.ai/companies"
    headers = {"accept": "application/json", "apikey": api_key}

    # Determine the appropriate parameter based on identifier type
    if identifier.startswith('http'):
        params = {"crunchbase_url": identifier} if 'crunchbase.com' in identifier else {"website_url": identifier}
    elif '.' in identifier and not identifier.startswith('http'):
        params = {"website_domain": identifier}
    else:
        url += f"/{identifier}"
        params = {}

    # Use POST if parameters are present, otherwise GET
    response = requests.post(url, headers=headers, params=params) if params else requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()


@func.register_function(
    metadata={"description": "Search for companies using a set of keywords."},
    key_dependencies=["harmonic_api_key"],
    imports=[{"name": "requests", "lib": "requests"}]
)
def harmonic_search_companies(keywords, include_ids_only=False):
    """
    Search for companies using keywords.
    Returns a list of companies and their metadata.
    """
    api_key = globals()['harmonic_api_key']
    url = "https://api.harmonic.ai/search/companies_by_keywords"
    headers = {"accept": "application/json", "apikey": api_key, "Content-Type": "application/json"}

    data = {"keywords": keywords, "include_ids_only": include_ids_only}
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    return response.json()


@func.register_function(
    metadata={"description": "Fetch detailed information about a person using their ID."},
    key_dependencies=["harmonic_api_key"],
    imports=[{"name": "requests", "lib": "requests"}]
)
def harmonic_enrich_person_by_id(person_id):
    """
    Retrieve detailed information about a person using their Harmonic ID.
    """
    api_key = globals()['harmonic_api_key']
    url = f"https://api.harmonic.ai/persons/{person_id}"
    headers = {"accept": "application/json", "apikey": api_key}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
```

## File: `babyagi/functionz/packs/plugins/payman.py`
```python
from babyagi.functionz.core.framework import func

# Store API keys (both test and real) from Replit secrets into the function database
@func.register_function(
    metadata={"description": "Store PayMan API keys (test and real) from Replit secrets into the function database"},
    imports=["os"]
)
def store_payman_api_keys():
    # Store test API key
    func.add_key('payman_test_api_key', os.environ['PAYMAN_TEST_API_KEY'])
    # Store real API key
    func.add_key('payman_api_key', os.environ['PAYMAN_API_KEY'])


# Create Task Function
@func.register_function(
    metadata={"description": "Create a task on PayMan platform (test by default, real if 'real_money' is True)"},
    key_dependencies=["payman_test_api_key", "payman_api_key"],
    imports=["requests"]
)
def create_task(title: str, description: str, payout: int, currency: str = "USD", category: str = "MARKETING", real_money: bool = False):
    if real_money:
        api_key = globals()['payman_api_key']
        base_url = "https://agent.payman.ai/api"
    else:
        api_key = globals()['payman_test_api_key']
        base_url = "https://agent-sandbox.payman.ai/api"

    headers = {
        "x-payman-api-secret": api_key,
        "Content-Type": "application/json",
        "Accept": "application/vnd.payman.v1+json"
    }
    payload = {
        "title": title,
        "description": description,
        "payout": payout,  # Payout in cents (e.g. 5000 for $50)
        "currency": currency,
        "category": category,
        "requiredSubmissions": 1,
        "submissionPolicy": "OPEN_SUBMISSIONS_ONE_PER_USER"
    }
    try:
        response = requests.post(f"{base_url}/tasks", headers=headers, json=payload)
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e)}


# Get Task by ID Function
@func.register_function(
    metadata={"description": "Get a task by its ID on PayMan platform (test by default, real if 'real_money' is True)"},
    key_dependencies=["payman_test_api_key", "payman_api_key"],
    imports=["requests"]
)
def get_task_by_id(task_id: str, real_money: bool = False):
    if real_money:
        api_key = globals()['payman_api_key']
        base_url = "https://agent.payman.ai/api"
    else:
        api_key = globals()['payman_test_api_key']
        base_url = "https://agent-sandbox.payman.ai/api"

    headers = {
        "x-payman-api-secret": api_key,
        "Content-Type": "application/json",
        "Accept": "application/vnd.payman.v1+json"
    }
    try:
        response = requests.get(f"{base_url}/tasks/{task_id}", headers=headers)
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e)}


# Get All Tasks Function
@func.register_function(
    metadata={"description": "Get all tasks for the current organization on PayMan platform (test by default, real if 'real_money' is True)"},
    key_dependencies=["payman_test_api_key", "payman_api_key"],
    imports=["requests"]
)
def get_all_tasks(page: int = 0, limit: int = 20, real_money: bool = False):
    if real_money:
        api_key = globals()['payman_api_key']
        base_url = "https://agent.payman.ai/api"
    else:
        api_key = globals()['payman_test_api_key']
        base_url = "https://agent-sandbox.payman.ai/api"

    headers = {
        "x-payman-api-secret": api_key,
        "Content-Type": "application/json",
        "Accept": "application/vnd.payman.v1+json"
    }
    params = {
        "page": page,
        "limit": limit
    }
    try:
        response = requests.get(f"{base_url}/tasks", headers=headers, params=params)
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e)}


@func.register_function(
    metadata={"description": "Get all submissions for a task on PayMan platform (test by default, real if 'real_money' is True)"},
    key_dependencies=["payman_test_api_key", "payman_api_key"],
    imports=["requests"]
)
def get_task_submissions(task_id: str, statuses: list = None, page: int = 0, limit: int = 20, real_money: bool = False):
    if real_money:
        api_key = globals()['payman_api_key']
        base_url = "https://agent.payman.ai/api"
    else:
        api_key = globals()['payman_test_api_key']
        base_url = "https://agent-sandbox.payman.ai/api"

    headers = {
        "x-payman-api-secret": api_key,
        "Content-Type": "application/json",
        "Accept": "application/vnd.payman.v1+json"
    }

    params = {
        "page": page,
        "limit": limit
    }

    if statuses:
        params["statuses"] = ",".join(statuses)

    try:
        response = requests.get(f"{base_url}/tasks/{task_id}/submissions", headers=headers, params=params)
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e)}

# Approve Task Submission Function
@func.register_function(
    metadata={"description": "Approve a task submission on PayMan platform (test by default, real if 'real_money' is True)"},
    key_dependencies=["payman_test_api_key", "payman_api_key"],
    imports=["requests"]
)
def approve_task_submission(submission_id: str, real_money: bool = False):
    if real_money:
        api_key = globals()['payman_api_key']
        base_url = "https://agent.payman.ai/api"
    else:
        api_key = globals()['payman_test_api_key']
        base_url = "https://agent-sandbox.payman.ai/api"

    headers = {
        "x-payman-api-secret": api_key,
        "Content-Type": "application/json",
        "Accept": "application/vnd.payman.v1+json"
    }
    try:
        response = requests.post(f"{base_url}/tasks/submissions/{submission_id}/approve", headers=headers)
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e)}


# Reject Task Submission Function
@func.register_function(
    metadata={"description": "Reject a task submission on PayMan platform (test by default, real if 'real_money' is True)"},
    key_dependencies=["payman_test_api_key", "payman_api_key"],
    imports=["requests"]
)
def reject_task_submission(submission_id: str, rejection_reason: str, real_money: bool = False):
    if real_money:
        api_key = globals()['payman_api_key']
        base_url = "https://agent.payman.ai/api"
    else:
        api_key = globals()['payman_test_api_key']
        base_url = "https://agent-sandbox.payman.ai/api"

    headers = {
        "x-payman-api-secret": api_key,
        "Content-Type": "application/json",
        "Accept": "application/vnd.payman.v1+json"
    }
    try:
        response = requests.post(f"{base_url}/tasks/submissions/{submission_id}/reject", headers=headers, json=rejection_reason)
        return response.json()
    except requests.exceptions.HTTPError as e:
        return {"error": str(e)}
```

## File: `babyagi/functionz/packs/plugins/serpapi.py`
```python
@func.register_function(
  metadata={
      "description": "Perform a search using the latest SerpApi Python client library with customizable parameters."
  },
  key_dependencies=["serpapi_api_key"],
  imports=["serpapi"]
)
def serpapi_search_v2(query: str, engine: str = "google", location: str = "United States", language: str = "en", country: str = "us", safe_search: bool = False, num_results: int = 10, start: int = 0, async_request: bool = False, output_format: str = "json"):
  """
  Perform a search using the SerpApi service with a flexible set of parameters.

  Args:
      query (str): The search query.
      engine (str): The search engine to use (e.g., 'google', 'bing'). Default is 'google'.
      location (str): The location to target the search. Default is 'United States'.
      language (str): UI language for the search. Default is 'en'.
      country (str): Country code for the search. Default is 'us'.
      safe_search (bool): Flag for SafeSearch filtering. Default is False.
      num_results (int): Number of search results to retrieve. Default is 10.
      start (int): Pagination offset. Default is 0.
      async_request (bool): Whether to make an asynchronous request. Default is False.
      output_format (str): Format of the output ('json' or 'html'). Default is 'json'.

  Returns:
      dict or str: The search results in the specified format.
  """
  # Import necessary modules and classes within function scope.

  # Get the API key from the global variables.
  api_key = globals().get("serpapi_api_key", "")
  if not api_key:
      raise ValueError("API key is missing. Please provide a valid SerpApi key.")

  # Initialize the SerpApi client.
  client = serpapi.Client(api_key=api_key)

  # Define the search parameters.
  params = {
      "q": query,
      "engine": engine,
      "location": location,
      "hl": language,
      "gl": country,
      "safe": "active" if safe_search else "off",
      "num": num_results,
      "start": start,
      "async": async_request,
      "output": output_format,
  }

  try:
      # Perform the search and get the results.
      search_results = client.search(**params)

      # Return the results in the specified format.
      if output_format == "json":
          return search_results.as_dict()
      elif output_format == "html":
          return search_results.get("raw_html", "No HTML content found.")
      else:
          raise ValueError("Invalid output format specified. Choose either 'json' or 'html'.")

  except requests.exceptions.HTTPError as e:
      # Handle potential SerpApi errors and HTTP errors.
      return {"error": str(e)}
```

## File: `babyagi/functionz/packs/plugins/voilanorbert.py`
```python
@func.register_function(
  metadata={"description": "Search for a contact by name and domain using VoilaNorbert's API."},
  key_dependencies=["voilanorbert_api_key"],
  imports=["requests", "time"]
)
def search_contact_by_name_domain(name, domain):
  """
  Searches for a contact by name and domain using the VoilaNorbert API.

  Args:
      name (str): Full name of the person to search.
      domain (str): Domain of the company the person works for.

  Returns:
      dict: The contact information if found, otherwise an appropriate message.
  """
  api_key = globals().get('voilanorbert_api_key')
  if not api_key:
      return {"error": "API key not found"}

  # Prepare the API request
  search_url = 'https://api.voilanorbert.com/2018-01-08/search/name'
  auth = ('any_string', api_key)
  data = {'name': name, 'domain': domain}

  try:
      # POST request to initiate search
      response = requests.post(search_url, auth=auth, data=data)
      if response.status_code == 402:
          return {"error": "No credits available for this search"}
      elif response.status_code != 200:
          return {"error": f"Failed to search contact: {response.json()}"}

      result = response.json()
      contact_id = result.get('id')

      # Polling to check if the email is found
      contact_url = f'https://api.voilanorbert.com/2018-01-08/contacts/{contact_id}'
      while True:
          contact_response = requests.get(contact_url, auth=auth)
          if contact_response.status_code == 200:
              contact_data = contact_response.json()
              if not contact_data['searching']:
                  if contact_data['email']:
                      return {
                          "email": contact_data['email']['email'],
                          "score": contact_data['email']['score']
                      }
                  return {"message": "Email not found!"}
          time.sleep(10)

  except requests.RequestException as e:
      return {"error": str(e)}


@func.register_function(
  metadata={"description": "Search for contacts by domain using VoilaNorbert's API."},
  key_dependencies=["voilanorbert_api_key"],
  imports=["requests"]
)
def search_contact_by_domain(domain):
  """
  Searches for contacts by domain using the VoilaNorbert API.

  Args:
      domain (str): The domain of the company to search for contacts.

  Returns:
      list: A list of found contacts with emails if available.
  """
  api_key = globals().get('voilanorbert_api_key')
  if not api_key:
      return {"error": "API key not found"}

  # Prepare the API request
  search_url = 'https://api.voilanorbert.com/2018-01-08/search/domain'
  auth = ('any_string', api_key)
  data = {'domain': domain}

  try:
      # POST request to initiate search
      response = requests.post(search_url, auth=auth, data=data)
      if response.status_code == 402:
          return {"error": "No credits available for this search"}
      elif response.status_code != 200:
          return {"error": f"Failed to search contacts: {response.json()}"}

      result = response.json()
      return result.get('result', [])

  except requests.RequestException as e:
      return {"error": str(e)}
```

## File: `babyagi/functionz/packs/plugins/wokelo.py`
```python
@func.register_function(
  metadata={"description": "Get an authentication token using the Wokelo API credentials."},
  key_dependencies=["wokelo_username", "wokelo_password"],
  imports=[{"name": "requests", "lib": "requests"}]
)
def get_auth_token():
  """Obtain an authentication token using Wokelo API credentials stored as secrets."""
  import requests
  BASE_URL = 'https://api.wokelo.ai'
  url = BASE_URL + '/auth/token'

  headers = {"Content-Type": "application/x-www-form-urlencoded"}
  data = {
      "client_id": "B5I07FeItrqH5V8ytQKNwHPDHeMQnGBheg7A6FAg",
      "client_secret": "JkVEP6FZhTkolz9vwkFSFAMVKLO0r9CnYU2RlGcRSzxZGZSkdSbSCed30VHg55IWU94F3sh0fTGUy8dTGslQZmcpCGvPhEUs9w3uobWa4ftXvsahriFCReRIxEUdd2f8",
      "grant_type": "password",
      "username": globals()['wokelo_username'],
      "password": globals()['wokelo_password'],
  }

  response = requests.post(url, headers=headers, data=data)

  if response.status_code == 200:
      # Successfully obtained token
      token_info = response.json()
      return token_info.get("access_token")
  else:
      return {"error": f"Failed to obtain token. Status code: {response.status_code}", "details": response.text}


@func.register_function(
  metadata={"description": "Create an industry snapshot report in Wokelo."},
  dependencies=["get_auth_token"],
  imports=[{"name": "requests", "lib": "requests"}]
)
def create_industry_snapshot(access_token: str, industry_name: str):
  """Initiate a new industry snapshot report."""
  import requests
  BASE_URL = 'https://api.wokelo.ai'
  url = f'{BASE_URL}/api/industry_primer/v3/start/'
  headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
  payload = {"industry": industry_name}

  response = requests.post(url, json=payload, headers=headers)
  if response.status_code == 200:
      return response.json().get('report_id')
  else:
      return {"error": "Failed to create industry snapshot.", "details": response.text}


@func.register_function(
  metadata={"description": "Check the status of an industry report using its report ID."},
  dependencies=["get_auth_token"],
  imports=[{"name": "requests", "lib": "requests"}]
)
def check_report_status(access_token: str, report_id: str):
  """Check the status of a generated report in Wokelo."""
  import requests
  BASE_URL = 'https://api.wokelo.ai'
  url = f'{BASE_URL}/api/assets/get_report_status/?report_id={report_id}'
  headers = {'Authorization': f'Bearer {access_token}'}

  response = requests.get(url, headers=headers)
  if response.status_code == 200:
      return response.json()
  else:
      return {"error": "Failed to check report status.", "details": response.text}


@func.register_function(
  metadata={"description": "Download the generated report from Wokelo."},
  dependencies=["get_auth_token"],
  imports=[{"name": "requests", "lib": "requests"}]
)
def download_report(access_token: str, report_id: str, file_type: str = 'pdf'):
  """Download a specific report in a given file format."""
  import requests
  BASE_URL = 'https://api.wokelo.ai'
  url = f'{BASE_URL}/api/assets/download_report/'
  headers = {'Authorization': f'Bearer {access_token}', 'Content-Type': 'application/json'}
  payload = {"file_type": file_type, "report_id": report_id}

  response = requests.post(url, json=payload, headers=headers)
  if response.status_code == 200:
      return response.content
  else:
      return {"error": "Failed to download report.", "details": response.text}


@func.register_function(
  metadata={"description": "Generate an industry report in Wokelo by tying all steps together."},
  dependencies=["get_auth_token", "create_industry_snapshot", "check_report_status", "download_report"],
  imports=[{"name": "time", "lib": "time"}]
)
def generate_industry_report(industry_name: str, file_type: str = 'pdf'):
  """
  Complete workflow for generating and downloading an industry report.

  Args:
      industry_name (str): The name of the industry to generate the report for.
      file_type (str): The format of the report file to be downloaded. Default is 'pdf'.

  Returns:
      str: File path of the downloaded report.
  """
  # Step 1: Get an authentication token.
  access_token = get_auth_token()
  if not isinstance(access_token, str):
      return access_token  # If there's an error, return the error message.

  # Step 2: Create an industry snapshot.
  report_id = create_industry_snapshot(access_token, industry_name)
  if not isinstance(report_id, str):
      return report_id  # If there's an error, return the error message.

  # Step 3: Check report status until it's ready.
  print(f"Initiated report creation. Waiting for the report (ID: {report_id}) to be exported.")
  while True:
      status_info = check_report_status(access_token, report_id)
      if 'status' in status_info and status_info['status'] == 'exported':
          print(f"Report is ready for download: {report_id}")
          break
      elif 'status' in status_info:
          print(f"Current report status: {status_info['status']}. Checking again in 30 seconds...")
      else:
          return status_info  # Error occurred.
      time.sleep(30)

  # Step 4: Download the report.
  report_content = download_report(access_token, report_id, file_type)
  if isinstance(report_content, dict) and 'error' in report_content:
      return report_content  # Return the error if download failed.

  # Step 5: Save the report locally.
  report_filename = f'report_{report_id}.{file_type}'
  with open(report_filename, 'wb') as report_file:
      report_file.write(report_content)

  return f"Report downloaded successfully: {report_filename}"
```

## File: `examples/custom_flask_example.py`
```python
#this is an example of how to use the babyagi framework in a custom flask app

from flask import Flask
import babyagi
from babyagi import register_function, load_functions

app = Flask(__name__)

# Use the babyagi blueprints
babyagi.use_blueprints(app, dashboard_route='/dashboard')

@register_function()
def integrated_function():
    return "Hello from integrated function!"

load_functions('plugins/firecrawl')

@app.route('/')
def home():
    return "Welcome to the main app. Visit /dashboard for BabyAGI dashboard."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

## File: `examples/custom_route_example.py`
```python
# this is an example of how to use babyagi with custom routes

from babyagi import create_app, register_function

app = create_app('/dashboard')

@register_function()
def another_custom_function():
    return "Hello from another custom function!"

@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for BabyAGI dashboard."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

## File: `examples/quickstart_example.py`
```python


import babyagi
import os


app = babyagi.create_app('/dashboard')

# Add OpenAI key to enable automated descriptions and embedding of functions.
babyagi.add_key_wrapper('openai_api_key',os.environ['OPENAI_API_KEY'])


@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for BabyAGI dashboard."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
```

## File: `examples/self_build_example.py`
```python
import babyagi
import os

# Add OpenAI key to enable automated descriptions and embedding of functions.
babyagi.add_key_wrapper('openai_api_key',os.environ['OPENAI_API_KEY'])

# Load below function packs to play with experimental self-building functions
babyagi.load_functions("drafts/code_writing_functions")
babyagi.load_functions("drafts/self_build")


babyagi.self_build("A growth marketer at an enterprise SaaS company.")

@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for BabyAGI dashboard."

if __name__ == "__main__":
    app = babyagi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
```

## File: `examples/simple_example.py`
```python
# this is a simple example of registering two functions into babyagi, executing the function stored in the database, and loading the dashboard

import babyagi
import os

# Add OpenAI key to enable automated descriptions and embedding of functions.
babyagi.add_key_wrapper('openai_api_key',os.environ['OPENAI_API_KEY'])

@babyagi.register_function()
def world():
    return "world"

@babyagi.register_function(dependencies=["world"])
def hello_world():
    x = world()
    return f"Hello {x}!"

print(hello_world())

@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for BabyAGI dashboard."

if __name__ == "__main__":
    app = babyagi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
```

## File: `examples/trigger_example.py`
```python
import babyagi

@babyagi.register_function()
def function_a():
    print("Result from function A")
    return "Result from function A"

@babyagi.register_function(triggers=['function_a'])
def function_b(input_data):
    print(f"Function B triggered with input: {input_data}")
    return f"Function B triggered with input: {input_data}"

function_a()

@app.route('/')
def home():
    return f"Welcome to the main app. Visit <a href=\"/dashboard\">/dashboard</a> for BabyAGI dashboard."

if __name__ == "__main__":
    app = babyagi.create_app('/dashboard')
    app.run(host='0.0.0.0', port=8080)
```

