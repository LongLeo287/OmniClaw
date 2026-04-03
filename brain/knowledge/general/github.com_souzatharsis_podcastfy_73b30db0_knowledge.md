---
id: github.com-souzatharsis-podcastfy-73b30db0-knowled
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:24.110396
---

# KNOWLEDGE EXTRACT: github.com_souzatharsis_podcastfy_73b30db0
> **Extracted on:** 2026-04-01 11:56:59
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007521600/github.com_souzatharsis_podcastfy_73b30db0

---

## File: `.dockerignore`
```
.git
.gitignore
.github
__pycache__
*.pyc
*.pyo
*.pyd
.Python
env/
venv/
.env
*.log
.pytest_cache/
.coverage
htmlcov/
dist/
build/
*.egg-info/
```

## File: `.gitattributes`
```
*.ipynb linguist-vendored
```

## File: `.gitignore`
```
.pypirc

specs/

*.whl
*.wheels

# Exclude aliases file
alias.sh

local_*.ipynb
*.ipynb_checkpoints

# Python-specific ignores
__pycache__/
*.py[cod]
*$py.class

# Virtual environment
venv/
env/
.env

# IDE-specific files
.vscode/
.idea/
*.swp
*.swo

# OS-specific files
.DS_Store
Thumbs.db

# Project-specific ignores
attachments/

# Logs
*.log

# Temporary files
*.tmp

# Compiled Python files
*.pyc

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
*.egg-info/
.installed.cfg
*.egg

# PyInstaller
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
.hypothesis/
.pytest_cache/

# Jupyter Notebook
.ipynb_checkpoints

# pyenv
.python-version

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

# Poetry
poetry.lock
.poetry/

# Poetry
.venv/
dist/

# Python
*.pyc
__pycache__/
*.egg-info/
```

## File: `.readthedocs.yaml`
```yaml
# .readthedocs.yaml
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools you might need
build:
  os: ubuntu-24.04
  tools:
    python: "3.11"
    # You can also specify other tool versions:
    # nodejs: "19"
    # rust: "1.64"
    # golang: "1.19"

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/source/conf.py

# Optionally build your docs in additional formats such as PDF and ePub
# formats:
#    - pdf
#    - epub

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
# python:
#    install:
#    - requirements: docs/requirements.txt
python:
  install:
    - requirements: docs/requirements.txt
```

## File: `CHANGELOG.md`
```markdown
# Changelog


## [0.4.0] - 2024-11-16

### Added
- Add Google Singlespeaker (Journey) and Multispeaker TTS models 
- Fixed limitations of Google Multispeaker TTS model: 5000 bytes input limite and 500 bytes per turn limit.
- Updated tests and docs accordingly

## [0.3.6] - 2024-11-13

### Added
- Add longform podcast generation support
  - Users can now generate longer podcasts (20-30+ minutes) using the `--longform` flag in CLI or `longform=True` in Python API
  - Implements "Content Chunking with Contextual Linking" technique for coherent long-form content
  - Configurable via `max_num_chunks` and `min_chunk_size` parameters in conversation config
  - `word_count` parameter removed from conversation config as it's no longer used

## [0.3.3] - 2024-11-08

### Breaking Changes
- Loading images from 'path' has been removed for security reasons. Please specify images by passing an 'url'.

### Added
- Add podcast generation from topic "Latest News in U.S. Politics"
- Integrate with 100+ LLM models (OpenAI, Anthropic, Google etc) for transcript generation
- Integrate with Google's Multispeaker TTS model for high-quality audio generation
- Deploy [REST API](https://github.com/souzatharsis/podcastfy/blob/main/usage/api.md) with FastAPI
- Support for raw text as input
- Add PRIVACY_POLICY.md
- Start TESTIMONIALS.md
- Add apps using Podcastfy to README.md

### Fixed
- #165 Fixed audio generation in Windows OS issue: Normalize path separators for cross-platform compatibility

## [0.2.3] - 2024-10-15

### Added
- Add local llm option by @souzatharsis
- Enable running podcastfy with no API KEYs thanks to solving #18 #58 #65 by @souzatharsis and @ChinoUkaegbu 
- Add user-provided TSS config such as voices #10 #6 #27 by @souzatharsis
- Add open in collab and setting python version to 3.11 by @Devparihar5 #57
- Add edge tts support by @ChinoUkaegbu
- Update pypdf with pymupdf(10x faster then pypdf) #56 check by @Devparihar5
- Replace r.jina.ai with simple BeautifulSoap #18 by @souzatharsis

### Fixed
- Fixed CLI for user-provided config #69 @souzatharsis

## [0.2.2] - 2024-10-13

### Added
- Added API reference docs and published it to https://podcastfy.readthedocs.io/en/latest/

### Fixed 
- ([#52](https://github.com/user/podcastfy/issues/37)) Fixed simple bug introduced in 0.2.1 that broke the ability to generate podcasts from text inputs!
- Fixed one example in the documentation that was not working.

## [0.2.1] - 2024-10-12


### Added
- ([#8](https://github.com/user/podcastfy/issues/8)) Podcastfy is now multi-modal! Users can now generate audio from images by simply providing the paths to the image files.

### Fixed 
- ([#40](https://github.com/user/podcastfy/issues/37)) Updated default ElevenLabs voice from `BrittneyHart` to `Jessica`. The latter was a non-default voice I used from my account, which caused error for users who don't have it.

## [0.2.0] - 2024-10-10

### Added
- Parameterized podcast generation with Conversation Configuration ([#11](https://github.com/user/podcastfy/issues/11), [#3](https://github.com/user/podcastfy/issues/3), [#4](https://github.com/user/podcastfy/issues/4))
  - Users can now customize podcast style, structure, and content
  - See [Conversation Customization](usage/conversation_custom.md) for detailed options
  - Updated demo in [podcastfy.ipynb](podcastfy.ipynb)
- LangChain integration for improved LLM interface and observability ([#29](https://github.com/user/podcastfy/issues/29))
- Changelog to track version updates ([#22](https://github.com/user/podcastfy/issues/22))
- Tests for Customized conversation scenarios

### Fixed
- CLI now correctly reads from user-provided local .env file ([#37](https://github.com/user/podcastfy/issues/37))
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

In the interest of fostering an open and welcoming environment, we as contributors and maintainers pledge to making participation in our project and our community a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

## Our Standards

Examples of behavior that contributes to creating a positive environment include:

* Using welcoming and inclusive language
* Being respectful of differing viewpoints and experiences
* Gracefully accepting constructive criticism
* Focusing on what is best for the community
* Showing empathy towards other community members

Examples of unacceptable behavior by participants include:

* The use of sexualized language or imagery and unwelcome sexual attention or advances
* Trolling, insulting/derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or electronic address, without explicit permission
* Other conduct which could reasonably be considered inappropriate in a professional setting

## Our Responsibilities

Project maintainers are responsible for clarifying the standards of acceptable behavior and are expected to take appropriate and fair corrective action in response to any instances of unacceptable behavior.

Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, wiki edits, issues, and other contributions that are not aligned to this Code of Conduct, or to ban temporarily or permanently any contributor for other behaviors that they deem inappropriate, threatening, offensive, or harmful.

## Scope

This Code
```

## File: `Dockerfile`
```
# Use Ubuntu 24.04 as base image
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    python3-full \
    python3-pip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install podcastfy from PyPI
RUN pip install --no-cache-dir podcastfy

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Verify installations
RUN echo "Verifying installations:" && \
    echo "Ubuntu version:" && cat /etc/os-release && \
    echo "FFmpeg version:" && ffmpeg -version && \
    echo "Python version:" && python3 --version && \
    echo "Pip version:" && pip --version && \
    echo "Installed packages:" && pip list

# Command to run when container starts
CMD ["python3"]
```

## File: `Dockerfile.dev`
```
# Use Ubuntu 24.04 as base image to match CI environment
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

# Install system dependencies matching CI configuration
RUN apt-get update && \
    apt-get install -y \
    python3-full \
    python3-pip \
    python3-venv \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install testing and linting dependencies
RUN pip install --no-cache-dir \
    flake8 \
    pytest \
    pytest-xdist

# Copy requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the package files
COPY . .

# Install the package in editable mode
RUN pip install -e .

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Verify installations
RUN echo "Verifying installations:" && \
    echo "Ubuntu version:" && cat /etc/os-release && \
    echo "FFmpeg version:" && ffmpeg -version && \
    echo "Python version:" && python3 --version && \
    echo "Pip version:" && pip --version && \
    echo "Installed packages:" && pip list

# Run flake8 checks during build
RUN flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics && \
    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

# Command to run when container starts
CMD ["python3"]
```

## File: `Dockerfile_api`
```
# Use Ubuntu 24.04 as base image
FROM ubuntu:24.04

# Prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    python3-full \
    python3-pip \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*
    
WORKDIR /app
# Create and activate virtual environment
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers and OS dependencies (Chromium only to keep image smaller)
RUN python -m playwright install --with-deps chromium

# Copy application files
COPY . /app


# Set environment variables
ENV PYTHONUNBUFFERED=1

# Verify installations
RUN echo "Verifying installations:" && \
    echo "Ubuntu version:" && cat /etc/os-release && \
    echo "FFmpeg version:" && ffmpeg -version && \
    echo "Python version:" && python3 --version && \
    echo "Pip version:" && pip --version && \
    echo "Installed packages:" && pip list

# Command to run when container starts
CMD ["uvicorn", "podcastfy.api.fast_app:app", "--host", "0.0.0.0", "--port", "8000"]
```

## File: `GUIDELINES.md`
```markdown
# Contributor Guidelines

Thank you for your interest in contributing to Podcastfy! We welcome contributions from the community to help improve and expand this project. Please follow these guidelines to ensure a smooth collaboration process.

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork locally: `git clone https://github.com/your-username/podcastfy.git`
3. Create a new branch for your feature or bug fix: `git checkout -b feature/your-feature-name`

## Code Style

- Follow PEP 8 style guidelines for Python code.
- Use tabs for indentation instead of spaces.
- Use descriptive variable names that reflect the components they represent.
- Include docstrings for all functions, classes, and modules.

## Development

- Poetry is the preferred but not mandatory dependency manager. Install it with `pip install poetry`.
    - Contributors can opt to use `uv` instead and generate and push updated requirements.txt from it. 
- Sphinx is used as the documentation generator. Install it with `pip install sphinx`.
    - `make doc-gen` to generate the documentation.


## Submitting Changes

1. Commit your changes with clear, descriptive commit messages.
2. Push your changes to your fork on GitHub.
3. Submit a pull request to the main repository.

## Pre-Pull Request Checklist

1. Managing dependencies
    - Add new dependencies with `poetry add <new-dependency>` 
    - Remove a dependency with `poetry remove <dependency-name>`. 
    - Then generate requirements.txt with `poetry export -f requirements.txt --output requirements.txt --without-hashes`
2. Testing
    - Consider adding new tests at test/*.py, particularly if implementing user facing change.
    - Test locally: `poetry run pytest`
    - Tests (tests/*.py) are run automatically by GitHub Actions, double check that they pass.
3. Docs
    - Update any documentation if required README.md, usage/*.md, *.ipynb etc.
    - Regenerate documentation (/docs) if there are any changes in docstrings or modules' interface (`make doc-gen`)


## Reporting Issues

- Use the GitHub issue tracker to report bugs or suggest enhancements.
- Provide a clear and detailed description of the issue or suggestion.
- Include steps to reproduce the bug, if applicable.

## Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

## Questions?

If you have any questions or need further clarification, please don't hesitate to ask in the GitHub issues section.

Thank you for contributing to Podcastfy!
```

## File: `LICENSE`
```
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

   Copyright [yyyy] [name of copyright owner]

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

## File: `Makefile`
```
lint:
	black podcastfy/*.py
	black tests/*.py
	mypy podcastfy/*.py

test:
	poetry run pytest -n auto
    
doc-gen:
	sphinx-apidoc -f -o ./docs/source ./podcastfy
	(cd ./docs && make clean && make html)
	
```

## File: `NOTICE`
```
Podcastfy
Copyright 2024 Tharsis T. P. Souza
------------------------
This product includes software developed by:
Tharsis T. P. Souza (www.souzatharsis.com) and all of the great contributors listed at https://github.com/souzatharsis/podcastfy/graphs/contributors.
------------------------
The text of the Apache License, Version 2.0 can be found in the LICENSE file.
```

## File: `PRIVACY_POLICY.md`
```markdown
# Privacy Policy

**Effective Date:** 11/03/2024

Podcastfy is an open-source project that does not collect, store, or transmit any personal user data. All processing occurs locally on your machine or through third-party services that you configure.

## Use of Third-Party Services

When you use Podcastfy with third-party services (such as APIs for text-to-speech or language models), any data transmitted to these services is subject to their respective privacy policies. You are responsible for reviewing and agreeing to the terms and policies of these third-party providers.

## Data Processing

- **Local Processing:** All content transformation and processing are performed locally unless explicitly configured to use external services.
- **No Data Collection:** Podcastfy does not collect or send any user data to the developers or any third parties without your consent.

## User Responsibility

Users are responsible for:

- Ensuring compliance with all applicable laws and regulations regarding data privacy.
- Protecting any personal or sensitive data processed through the application.
- Reviewing the privacy policies of any third-party services used in conjunction with Podcastfy.

## Contact Information

If you have any questions or concerns about this Privacy Policy, please open an issue on our [GitHub repository](https://github.com/souzatharsis/podcastfy/issues).
```

## File: `README.md`
```markdown
<div align="center">
<a name="readme-top"></a>

<a href="https://trendshift.io/repositories/12965" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12965" alt="Podcastfy.ai | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

# Podcastfy.ai 🎙️🤖
An Open Source API alternative to NotebookLM's podcast feature: Transforming Multimodal Content into Captivating Multilingual Audio Conversations with GenAI



https://github.com/user-attachments/assets/5d42c106-aabe-44c1-8498-e9c53545ba40



[Paper](https://github.com/souzatharsis/podcastfy/blob/main/paper/paper.pdf) |
[Python Package](https://github.com/souzatharsis/podcastfy/blob/59563ee105a0d1dbb46744e0ff084471670dd725/podcastfy.ipynb) |
[CLI](https://github.com/souzatharsis/podcastfy/blob/59563ee105a0d1dbb46744e0ff084471670dd725/usage/cli.md) |
[Web App](https://openpod.fly.dev/) |
[Feedback](https://github.com/souzatharsis/podcastfy/issues)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/souzatharsis/podcastfy/blob/main/podcastfy.ipynb)
[![PyPi Status](https://img.shields.io/pypi/v/podcastfy)](https://pypi.org/project/podcastfy/)
![PyPI Downloads](https://static.pepy.tech/badge/podcastfy)
[![Issues](https://img.shields.io/github/issues-raw/souzatharsis/podcastfy)](https://github.com/souzatharsis/podcastfy/issues)
[![Pytest](https://github.com/souzatharsis/podcastfy/actions/workflows/python-app.yml/badge.svg)](https://github.com/souzatharsis/podcastfy/actions/workflows/python-app.yml)
[![Docker](https://github.com/souzatharsis/podcastfy/actions/workflows/docker-publish.yml/badge.svg)](https://github.com/souzatharsis/podcastfy/actions/workflows/docker-publish.yml)
[![Documentation Status](https://readthedocs.org/projects/podcastfy/badge/?version=latest)](https://podcastfy.readthedocs.io/en/latest/?badge=latest)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![GitHub Repo stars](https://img.shields.io/github/stars/souzatharsis/podcastfy)
</div>

Podcastfy is an open-source Python package that transforms multi-modal content (text, images) into engaging, multi-lingual audio conversations using GenAI. Input content includes websites, PDFs, images, YouTube videos, as well as user provided topics.

Unlike closed-source UI-based tools focused primarily on research synthesis (e.g. NotebookLM ❤️), Podcastfy focuses on open source, programmatic and bespoke generation of engaging, conversational content from a multitude of multi-modal sources, enabling customization and scale.

## Testimonials 💬

> "Love that you casually built an open source version of the most popular product Google built in the last decade"

> "Loving this initiative and the best I have seen so far especially for a 'non-techie' user."

> "Your library was very straightforward to work with. You did Amazing work brother 🙏"

> "I think it's awesome that you were inspired/recognize how hard it is to beat NotebookLM's quality, but you did an *incredible* job with this! It sounds incredible, and it's open-source! Thank you for being amazing!"

[![Star History Chart](https://api.star-history.com/svg?repos=souzatharsis/podcastfy&type=Date&theme=dark)](https://api.star-history.com/svg?repos=souzatharsis/podcastfy&type=Date&theme=dark)

## Audio Examples 🔊
This sample collection was generated using this [Python Notebook](usage/examples.ipynb).

### Images
Sample 1: Senecio, 1922 (Paul Klee) and Connection of Civilizations (2017) by Gheorghe Virtosu
***
<img src="data/images/Senecio.jpeg" alt="Senecio, 1922 (Paul Klee)" width="20%" height="auto"> <img src="data/images/connection.jpg" alt="Connection of Civilizations (2017) by Gheorghe Virtosu " width="21.5%" height="auto">
<video src="https://github.com/user-attachments/assets/a4134a0d-138c-4ab4-bc70-0f53b3507e6b"></video>  
***
Sample 2: The Great Wave off Kanagawa, 1831 (Hokusai) and Takiyasha the Witch and the Skeleton Spectre, c. 1844 (Kuniyoshi)
***
 <img src="data/images/japan_1.jpg" alt="The Great Wave off Kanagawa, 1831 (Hokusai)" width="20%" height="auto"> <img src="data/images/japan2.jpg" alt="Takiyasha the Witch and the Skeleton Spectre, c. 1844 (Kuniyoshi)" width="21.5%" height="auto"> 
<video src="https://github.com/user-attachments/assets/f6aaaeeb-39d2-4dde-afaf-e2cd212e9fed"></video>  
***
Sample 3: Pop culture icon Taylor Swift and Mona Lisa, 1503 (Leonardo da Vinci)
***
<img src="data/images/taylor.png" alt="Taylor Swift" width="28%" height="auto"> <img src="data/images/monalisa.jpeg" alt="Mona Lisa" width="10.5%" height="auto">
<video src="https://github.com/user-attachments/assets/3b6f7075-159b-4540-946f-3f3907dffbca"></video> 


### Text
| Audio | Description  | Source |
|-------|--|--------|
| <video src="https://github.com/user-attachments/assets/ef41a207-a204-4b60-a11e-06d66a0fbf06"></video>  | Personal Website | [Website](https://www.souzatharsis.com) |
| [Audio](https://soundcloud.com/high-lander123/amodei?in=high-lander123/sets/podcastfy-sample-audio-longform&si=b8dfaf4e3ddc4651835e277500384156) (`longform=True`) | Lex Fridman Podcast: 5h interview with Dario Amodei Anthropic's CEO |  [Youtube](https://www.youtube.com/watch?v=ugvHCXCOmm4) |
| [Audio](https://soundcloud.com/high-lander123/benjamin?in=high-lander123/sets/podcastfy-sample-audio-longform&si=dca7e2eec1c94252be18b8794499959a&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing) (`longform=True`)| Benjamin Franklin's Autobiography | [Book](https://www.gutenberg.org/cache/epub/148/pg148.txt) |

### Multi-Lingual Text
| Language | Content Type | Description | Audio | Source |
|----------|--------------|-------------|-------|--------|
| French | Website | Agroclimate research information | [Audio](https://audio.com/thatupiso/audio/podcast-fr-agro) | [Website](https://agroclim.inrae.fr/) |
| Portuguese-BR | News Article | Election polls in São Paulo | [Audio](https://audio.com/thatupiso/audio/podcast-thatupiso-br) | [Website](https://noticias.uol.com.br/eleicoes/2024/10/03/nova-pesquisa-datafolha-quem-subiu-e-quem-caiu-na-disputa-de-sp-03-10.htm) |


## Quickstart 💻

### Prerequisites
- Python 3.11 or higher
- `$ pip install ffmpeg` (for audio processing)

### Setup
1. Install from PyPI
  `$ pip install podcastfy`

2. Set up your [API keys](config.md)

### Python
```python
from podcastfy.client import generate_podcast

audio_file = generate_podcast(urls=["<url1>", "<url2>"])
```
### CLI
```
python -m podcastfy.client --url <url1> --url <url2>
```

### Fastapi (Beta for urls)
```
Containerize podcastify and launch the api
Dockerfile_api

Make requests to the api look at the notebook for a clear example
fetch_audio(request_data, ENDPOINT, BASE_URL)
```
  
## Usage 💻

- [Python Package Quickstart](podcastfy.ipynb)

- [How to](usage/how-to.md)

- [Python Package Reference Manual](https://podcastfy.readthedocs.io/en/latest/podcastfy.html)

- [CLI](cli.md)

## Customization 🔧

Podcastfy offers a range of customization options to tailor your AI-generated podcasts:
- Customize podcast [conversation](usage/conversation_custom.md) (e.g. format, style, voices)
- Choose to run [Local LLMs](usage/local_llm.md) (156+ HuggingFace models)
- Set other [Configuration Settings](config.md)

## Features ✨

- Generate conversational content from multiple sources and formats (images, text, websites, YouTube, and PDFs).
- Generate shorts (2-5 minutes) or longform (30+ minutes) podcasts.
- Customize transcript and audio generation (e.g., style, language, structure).
- Generate transcripts using 100+ LLM models (OpenAI, Anthropic, Google etc).
- Leverage local LLMs for transcript generation for increased privacy and control.
- Integrate with advanced text-to-speech models (OpenAI, Google, ElevenLabs, and Microsoft Edge).
- Provide multi-language support for global content creation.
- Integrate seamlessly with CLI and Python packages for automated workflows.

## Built with Podcastfy 🚀

- [OpenNotebook](https://www.open-notebook.ai/)
- [SurfSense](https://www.surfsense.net/)
- [OpenPod](https://openpod.fly.dev/)
- [Podcast-llm](https://github.com/evandempsey/podcast-llm)
- [Podcastfy-HuggingFace App](https://huggingface.co/spaces/thatupiso/Podcastfy.ai_demo)


## Updates 🚀🚀

### v0.4.0+ release
- Leverage natural conversational multi-Speaker TTS model
- Generate short or longform podcasts
- Generate podcasts from input topic using grounded real-time web search
- Integrate with 100+ LLM models (OpenAI, Anthropic, Google etc) for transcript generation

See [CHANGELOG](CHANGELOG.md) for more details.


## License

This software is licensed under [Apache 2.0](LICENSE). See [instructions](usage/license-guide.md) if you would like to use podcastfy in your software.

## Contributing 🤝

We welcome contributions! See [Guidelines](../../../core/security/QUARANTINE/vetted/repos/claude_code_templates/cli_tool/components/skills/database/using_neon/references/neon_rest_api/guidelines.md) for more details.

## Example Use Cases 🎧🎶

- **Content Creators** can use `Podcastfy` to convert blog posts, articles, or multimedia content into podcast-style audio, enabling them to reach broader audiences. By transforming content into an audio format, creators can cater to users who prefer listening over reading.

- **Educators** can transform lecture notes, presentations, and visual materials into audio conversations, making educational content more accessible to students with different learning preferences. This is particularly beneficial for students with visual impairments or those who have difficulty processing written information.

- **Researchers** can convert research papers, visual data, and technical content into conversational audio. This makes it easier for a wider audience, including those with disabilities, to consume and understand complex scientific information. Researchers can also create audio summaries of their work to enhance accessibility.

- **Accessibility Advocates** can use `Podcastfy` to promote digital accessibility by providing a tool that converts multimodal content into auditory formats. This helps individuals with visual impairments, dyslexia, or other disabilities that make it challenging to consume written or visual content.
  
## Contributors

<a href="https://github.com/souzatharsis/podcastfy/graphs/contributors">
  <img alt="contributors" src="https://contrib.rocks/image?repo=souzatharsis/podcastfy"/>
</a>

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>
```

## File: `TESTIMONIALS.md`
```markdown
- "Love that you casually built an open source version of the most popular product Google built in the last decade"
- "Your library was very straightforward to work with. You did Amazing work brother 🙏"
- "I think it's awesome that you were inspired/recognize how hard it is to beat NotebookLM's quality, but you did an *incredible* job with this! It sounds incredible, and it's open-source! Thank you for being amazing!"
- "Discovered your work last night. Stunning accomplishment. Well done."
- "Loving this initiative and the best I have seen so far especially for a "non-techie" user."
```

## File: `build_docs.py`
```python
import os
import sys
from sphinx.cmd.build import main as sphinx_main

def main():
	"""
	Wrapper function to build Sphinx documentation.
	"""
	# Change to the docs directory
	os.chdir('docs')
	
	# Run Sphinx build command
	sys.exit(sphinx_main(['-b', 'html', 'source', '_build/html']))

if __name__ == '__main__':
	main()
```

## File: `dev-requirements.txt`
```
alabaster==0.7.16 ; python_version >= "3.11" and python_version < "4.0"
annotated-types==0.7.0 ; python_version >= "3.11" and python_version < "4.0"
anyio==4.6.0 ; python_version >= "3.11" and python_version < "4.0"
appnope==0.1.4 ; python_version >= "3.11" and python_version < "4.0" and platform_system == "Darwin"
asttokens==2.4.1 ; python_version >= "3.11" and python_version < "4.0"
attrs==24.2.0 ; python_version >= "3.11" and python_version < "4.0"
babel==2.16.0 ; python_version >= "3.11" and python_version < "4.0"
beautifulsoup4==4.12.3 ; python_version >= "3.11" and python_version < "4.0"
black==24.10.0 ; python_version >= "3.11" and python_version < "4.0"
bleach==6.1.0 ; python_version >= "3.11" and python_version < "4.0"
cachetools==5.5.0 ; python_version >= "3.11" and python_version < "4.0"
certifi==2024.8.30 ; python_version >= "3.11" and python_version < "4.0"
cffi==1.17.1 ; python_version >= "3.11" and python_version < "4.0" and implementation_name == "pypy"
charset-normalizer==3.3.2 ; python_version >= "3.11" and python_version < "4.0"
click==8.1.7 ; python_version >= "3.11" and python_version < "4.0"
colorama==0.4.6 ; python_version >= "3.11" and python_version < "4.0" and (sys_platform == "win32" or platform_system == "Windows")
comm==0.2.2 ; python_version >= "3.11" and python_version < "4.0"
cython==3.0.11 ; python_version >= "3.11" and python_version < "4.0"
debugpy==1.8.6 ; python_version >= "3.11" and python_version < "4.0"
decorator==5.1.1 ; python_version >= "3.11" and python_version < "4.0"
defusedxml==0.7.1 ; python_version >= "3.11" and python_version < "4.0"
distro==1.9.0 ; python_version >= "3.11" and python_version < "4.0"
docutils==0.20.1 ; python_version >= "3.11" and python_version < "4.0"
elevenlabs==1.9.0 ; python_version >= "3.11" and python_version < "4.0"
executing==2.1.0 ; python_version >= "3.11" and python_version < "4.0"
fastjsonschema==2.20.0 ; python_version >= "3.11" and python_version < "4.0"
ffmpeg==1.4 ; python_version >= "3.11" and python_version < "4.0"
fuzzywuzzy==0.18.0 ; python_version >= "3.11" and python_version < "4.0"
google-ai-generativelanguage==0.6.10 ; python_version >= "3.11" and python_version < "4.0"
google-api-core==2.20.0 ; python_version >= "3.11" and python_version < "4.0"
google-api-core[grpc]==2.20.0 ; python_version >= "3.11" and python_version < "4.0"
google-api-python-client==2.148.0 ; python_version >= "3.11" and python_version < "4.0"
google-auth-httplib2==0.2.0 ; python_version >= "3.11" and python_version < "4.0"
google-auth==2.35.0 ; python_version >= "3.11" and python_version < "4.0"
google-generativeai==0.8.3 ; python_version >= "3.11" and python_version < "4.0"
googleapis-common-protos==1.65.0 ; python_version >= "3.11" and python_version < "4.0"
grpcio-status==1.66.2 ; python_version >= "3.11" and python_version < "4.0"
grpcio==1.66.2 ; python_version >= "3.11" and python_version < "4.0"
h11==0.14.0 ; python_version >= "3.11" and python_version < "4.0"
httpcore==1.0.6 ; python_version >= "3.11" and python_version < "4.0"
httplib2==0.22.0 ; python_version >= "3.11" and python_version < "4.0"
httpx==0.27.2 ; python_version >= "3.11" and python_version < "4.0"
idna==3.10 ; python_version >= "3.11" and python_version < "4.0"
imagesize==1.4.1 ; python_version >= "3.11" and python_version < "4.0"
iniconfig==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
ipykernel==6.29.5 ; python_version >= "3.11" and python_version < "4.0"
ipython==8.28.0 ; python_version >= "3.11" and python_version < "4.0"
jedi==0.19.1 ; python_version >= "3.11" and python_version < "4.0"
jinja2==3.1.4 ; python_version >= "3.11" and python_version < "4.0"
jiter==0.6.1 ; python_version >= "3.11" and python_version < "4.0"
jsonschema-specifications==2024.10.1 ; python_version >= "3.11" and python_version < "4.0"
jsonschema==4.23.0 ; python_version >= "3.11" and python_version < "4.0"
jupyter-client==8.6.3 ; python_version >= "3.11" and python_version < "4.0"
jupyter-core==5.7.2 ; python_version >= "3.11" and python_version < "4.0"
jupyterlab-pygments==0.3.0 ; python_version >= "3.11" and python_version < "4.0"
levenshtein==0.26.0 ; python_version >= "3.11" and python_version < "4.0"
markdown-it-py==3.0.0 ; python_version >= "3.11" and python_version < "4.0"
markupsafe==3.0.1 ; python_version >= "3.11" and python_version < "4.0"
matplotlib-inline==0.1.7 ; python_version >= "3.11" and python_version < "4.0"
mdurl==0.1.2 ; python_version >= "3.11" and python_version < "4.0"
mistune==3.0.2 ; python_version >= "3.11" and python_version < "4.0"
mypy-extensions==1.0.0 ; python_version >= "3.11" and python_version < "4.0"
mypy==1.11.2 ; python_version >= "3.11" and python_version < "4.0"
nbclient==0.10.0 ; python_version >= "3.11" and python_version < "4.0"
nbconvert==7.16.4 ; python_version >= "3.11" and python_version < "4.0"
nbformat==5.10.4 ; python_version >= "3.11" and python_version < "4.0"
nbsphinx==0.9.5 ; python_version >= "3.11" and python_version < "4.0"
nest-asyncio==1.6.0 ; python_version >= "3.11" and python_version < "4.0"
numpy==2.1.2 ; python_version >= "3.11" and python_version < "4.0"
openai==1.51.2 ; python_version >= "3.11" and python_version < "4.0"
packaging==24.1 ; python_version >= "3.11" and python_version < "4.0"
pandas==2.2.3 ; python_version >= "3.11" and python_version < "4.0"
pandocfilters==1.5.1 ; python_version >= "3.11" and python_version < "4.0"
parso==0.8.4 ; python_version >= "3.11" and python_version < "4.0"
pathspec==0.12.1 ; python_version >= "3.11" and python_version < "4.0"
pexpect==4.9.0 ; python_version >= "3.11" and python_version < "4.0" and (sys_platform != "win32" and sys_platform != "emscripten")
platformdirs==4.3.6 ; python_version >= "3.11" and python_version < "4.0"
pluggy==1.5.0 ; python_version >= "3.11" and python_version < "4.0"
prompt-toolkit==3.0.48 ; python_version >= "3.11" and python_version < "4.0"
proto-plus==1.24.0 ; python_version >= "3.11" and python_version < "4.0"
protobuf==5.28.2 ; python_version >= "3.11" and python_version < "4.0"
psutil==6.0.0 ; python_version >= "3.11" and python_version < "4.0"
ptyprocess==0.7.0 ; python_version >= "3.11" and python_version < "4.0" and (sys_platform != "win32" and sys_platform != "emscripten")
pure-eval==0.2.3 ; python_version >= "3.11" and python_version < "4.0"
pyasn1-modules==0.4.1 ; python_version >= "3.11" and python_version < "4.0"
pyasn1==0.6.1 ; python_version >= "3.11" and python_version < "4.0"
pycparser==2.22 ; python_version >= "3.11" and python_version < "4.0" and implementation_name == "pypy"
pydantic-core==2.23.4 ; python_version >= "3.11" and python_version < "4.0"
pydantic==2.9.2 ; python_version >= "3.11" and python_version < "4.0"
pydub==0.25.1 ; python_version >= "3.11" and python_version < "4.0"
pygments==2.18.0 ; python_version >= "3.11" and python_version < "4.0"
pyparsing==3.1.4 ; python_version >= "3.11" and python_version < "4.0"
pypdf==5.0.1 ; python_version >= "3.11" and python_version < "4.0"
pytest==8.3.3 ; python_version >= "3.11" and python_version < "4.0"
python-dateutil==2.9.0.post0 ; python_version >= "3.11" and python_version < "4.0"
python-dotenv==1.0.1 ; python_version >= "3.11" and python_version < "4.0"
python-levenshtein==0.26.0 ; python_version >= "3.11" and python_version < "4.0"
pytz==2024.2 ; python_version >= "3.11" and python_version < "4.0"
pywin32==307 ; sys_platform == "win32" and platform_python_implementation != "PyPy" and python_version >= "3.11" and python_version < "4.0"
pyyaml==6.0.2 ; python_version >= "3.11" and python_version < "4.0"
pyzmq==26.2.0 ; python_version >= "3.11" and python_version < "4.0"
rapidfuzz==3.10.0 ; python_version >= "3.11" and python_version < "4.0"
referencing==0.35.1 ; python_version >= "3.11" and python_version < "4.0"
requests==2.32.3 ; python_version >= "3.11" and python_version < "4.0"
rich==13.9.2 ; python_version >= "3.11" and python_version < "4.0"
rpds-py==0.20.0 ; python_version >= "3.11" and python_version < "4.0"
rsa==4.9 ; python_version >= "3.11" and python_version < "4"
setuptools==75.1.0 ; python_version >= "3.11" and python_version < "4.0"
shellingham==1.5.4 ; python_version >= "3.11" and python_version < "4.0"
six==1.16.0 ; python_version >= "3.11" and python_version < "4.0"
sniffio==1.3.1 ; python_version >= "3.11" and python_version < "4.0"
snowballstemmer==2.2.0 ; python_version >= "3.11" and python_version < "4.0"
soupsieve==2.6 ; python_version >= "3.11" and python_version < "4.0"
sphinx-rtd-theme==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinx==7.4.7 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-applehelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-devhelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-htmlhelp==2.1.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-jquery==4.1 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-jsmath==1.0.1 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-qthelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-serializinghtml==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
stack-data==0.6.3 ; python_version >= "3.11" and python_version < "4.0"
tinycss2==1.3.0 ; python_version >= "3.11" and python_version < "4.0"
tornado==6.4.1 ; python_version >= "3.11" and python_version < "4.0"
tqdm==4.66.5 ; python_version >= "3.11" and python_version < "4.0"
traitlets==5.14.3 ; python_version >= "3.11" and python_version < "4.0"
typer==0.12.5 ; python_version >= "3.11" and python_version < "4.0"
typing-extensions==4.12.2 ; python_version >= "3.11" and python_version < "4.0"
tzdata==2024.2 ; python_version >= "3.11" and python_version < "4.0"
uritemplate==4.1.1 ; python_version >= "3.11" and python_version < "4.0"
urllib3==2.2.3 ; python_version >= "3.11" and python_version < "4.0"
wcwidth==0.2.13 ; python_version >= "3.11" and python_version < "4.0"
webencodings==0.5.1 ; python_version >= "3.11" and python_version < "4.0"
websockets==13.1 ; python_version >= "3.11" and python_version < "4.0"
wheel==0.44.0 ; python_version >= "3.11" and python_version < "4.0"
youtube-transcript-api==0.6.2 ; python_version >= "3.11" and python_version < "4.0"
```

## File: `docker-compose.yml`
```yaml
version: '3.8'

services:
  podcastfy:
    build:
      context: .
      dockerfile: Dockerfile
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import podcastfy"]
      interval: 30s
      timeout: 10s
      retries: 3

  podcastfy-dev:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - .:/app
      - /opt/venv:/opt/venv
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - PYTHONPATH=/app
      - DEBIAN_FRONTEND=noninteractive
    ports:
      - "8001:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import podcastfy"]
      interval: 30s
      timeout: 10s
      retries: 3

  test:
    build:
      context: .
      dockerfile: Dockerfile.dev
    volumes:
      - .:/app
      - /opt/venv:/opt/venv
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - PYTHONPATH=/app
    command: pytest -n auto --dist loadfile
```

## File: `make.sh`
```bash
#!/bin/bash

export PYTHONPATH="~src/podcastfy:$PYTHONPATH"
```

## File: `procfile`
```
web: uvicorn podcastfy.api.fast_app:app --host 0.0.0.0 --port $PORT
```

## File: `pyproject.toml`
```
[tool.poetry]
name = "podcastfy"
version = "0.4.3"
description = "An Open Source alternative to NotebookLM's podcast feature: Transforming Multimodal Content into Captivating Multilingual Audio Conversations with GenAI"
authors = ["Tharsis T. P. Souza"]
license = "Apache-2.0"
readme = "README.md"
include = [
    "podcastfy/config.yaml",
    "podcastfy/conversation_config.yaml"
]

[tool.poetry.dependencies]
python = "^3.11"
setuptools = "^75.1.0"
wheel = "^0.44.0"
cython = "^3.0.11"
typer = "^0.12.5"
python-dotenv = "^1.0.1"
requests = "^2.32.3"
beautifulsoup4 = "^4.12.3"
openai = "^1.56.1"
elevenlabs = "^1.9.0"
PyMuPDF = "^1.24.11"
pyyaml = "^6.0.2"
youtube-transcript-api = "^0.6.2"
pydub = "^0.25.1"
fuzzywuzzy = "^0.18.0"
python-levenshtein = "^0.26.0"
pandas = "^2.2.3"
google-generativeai = "^0.8.2"
numpy = ">=1,<2"
langchain = "^0.3.3"
langchain-google-vertexai = "^2.0.4"
langchain-google-genai = "^2.0.1"
httpx = "^0.28.1"
pandoc = "^2.4"
sphinx-rtd-theme = "^3.0.1"
sphinx-autodoc-typehints = "^2.5.0"
nbsphinx = "^0.9.5"
edge-tts = "^7.2.3"
types-pyyaml = "^6.0.12.20240917"
nest-asyncio = "^1.6.0"
ffmpeg = "^1.4"
pytest = "^8.3.3"
pytest-xdist = "^3.6.1"
google-cloud-texttospeech = "^2.21.0"
google-genai = "^1.46.0"
litellm = "^1.52.0"
langchain-community = "^0.3.5"


[tool.poetry.group.dev.dependencies]
pytest = "^8.3.3"
black = "^24.8.0"
sphinx = ">=8.0.2"
nbsphinx = "0.9.5"
ipykernel = "^6.29.5"
ffmpeg = "^1.4"
mypy = "^1.11.2"

[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry.scripts]
build_docs = "build_docs:main"



```

## File: `requirements.txt`
```
aiohappyeyeballs==2.4.3 ; python_version >= "3.11" and python_version < "4.0"
aiosignal==1.3.1 ; python_version >= "3.11" and python_version < "4.0"
alabaster==1.0.0 ; python_version >= "3.11" and python_version < "4.0"
annotated-types==0.7.0 ; python_version >= "3.11" and python_version < "4.0"
anyio==4.6.2.post1 ; python_version >= "3.11" and python_version < "4.0"
attrs==24.2.0 ; python_version >= "3.11" and python_version < "4.0"
babel==2.16.0 ; python_version >= "3.11" and python_version < "4.0"
beautifulsoup4==4.12.3 ; python_version >= "3.11" and python_version < "4.0"
bleach==6.2.0 ; python_version >= "3.11" and python_version < "4.0"
cachetools==5.5.0 ; python_version >= "3.11" and python_version < "4.0"
certifi==2024.8.30 ; python_version >= "3.11" and python_version < "4.0"
cffi==1.17.1 ; python_version >= "3.11" and python_version < "4.0" and implementation_name == "pypy"
charset-normalizer==3.4.0 ; python_version >= "3.11" and python_version < "4.0"
click==8.1.7 ; python_version >= "3.11" and python_version < "4.0"
colorama==0.4.6 ; python_version >= "3.11" and python_version < "4.0" and (sys_platform == "win32" or platform_system == "Windows")
cython==3.0.11 ; python_version >= "3.11" and python_version < "4.0"
dataclasses-json==0.6.7 ; python_version >= "3.11" and python_version < "4.0"
defusedxml==0.7.1 ; python_version >= "3.11" and python_version < "4.0"
distro==1.9.0 ; python_version >= "3.11" and python_version < "4.0"
docstring-parser==0.16 ; python_version >= "3.11" and python_version < "4.0"
docutils==0.21.2 ; python_version >= "3.11" and python_version < "4.0"
edge-tts==7.2.3 ; python_version >= "3.11" and python_version < "4.0"
elevenlabs==1.12.1 ; python_version >= "3.11" and python_version < "4.0"
execnet==2.1.1 ; python_version >= "3.11" and python_version < "4.0"
fastjsonschema==2.20.0 ; python_version >= "3.11" and python_version < "4.0"
ffmpeg==1.4 ; python_version >= "3.11" and python_version < "4.0"
filelock==3.16.1 ; python_version >= "3.11" and python_version < "4.0"
frozenlist==1.5.0 ; python_version >= "3.11" and python_version < "4.0"
fsspec==2024.10.0 ; python_version >= "3.11" and python_version < "4.0"
fuzzywuzzy==0.18.0 ; python_version >= "3.11" and python_version < "4.0"
google-ai-generativelanguage==0.6.10 ; python_version >= "3.11" and python_version < "4.0"
google-api-core==2.22.0 ; python_version >= "3.11" and python_version < "4.0"
google-api-core[grpc]==2.22.0 ; python_version >= "3.11" and python_version < "4.0"
google-api-python-client==2.151.0 ; python_version >= "3.11" and python_version < "4.0"
google-auth-httplib2==0.2.0 ; python_version >= "3.11" and python_version < "4.0"
google-auth==2.36.0 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-aiplatform==1.71.1 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-bigquery==3.26.0 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-core==2.4.1 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-resource-manager==1.13.0 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-storage==2.18.2 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-texttospeech==2.21.0 ; python_version >= "3.11" and python_version < "4.0"
google-crc32c==1.6.0 ; python_version >= "3.11" and python_version < "4.0"
google-generativeai==0.8.3 ; python_version >= "3.11" and python_version < "4.0"
google-genai>=1.46.0 ; python_version >= "3.11" and python_version < "4.0"
google-resumable-media==2.7.2 ; python_version >= "3.11" and python_version < "4.0"
googleapis-common-protos==1.65.0 ; python_version >= "3.11" and python_version < "4.0"
googleapis-common-protos[grpc]==1.65.0 ; python_version >= "3.11" and python_version < "4.0"
greenlet==3.1.1 ; python_version < "3.13" and (platform_machine == "aarch64" or platform_machine == "ppc64le" or platform_machine == "x86_64" or platform_machine == "amd64" or platform_machine == "AMD64" or platform_machine == "win32" or platform_machine == "WIN32") and python_version >= "3.11"
grpc-google-iam-v1==0.13.1 ; python_version >= "3.11" and python_version < "4.0"
grpcio-status==1.67.1 ; python_version >= "3.11" and python_version < "4.0"
grpcio==1.67.1 ; python_version >= "3.11" and python_version < "4.0"
h11==0.14.0 ; python_version >= "3.11" and python_version < "4.0"
httpcore==1.0.6 ; python_version >= "3.11" and python_version < "4.0"
httplib2==0.22.0 ; python_version >= "3.11" and python_version < "4.0"
httpx-sse==0.4.0 ; python_version >= "3.11" and python_version < "4.0"
httpx==0.28.1 ; python_version >= "3.11" and python_version < "4.0"
huggingface-hub==0.26.2 ; python_version >= "3.11" and python_version < "4.0"
idna==3.10 ; python_version >= "3.11" and python_version < "4.0"
imagesize==1.4.1 ; python_version >= "3.11" and python_version < "4.0"
importlib-metadata==8.5.0 ; python_version >= "3.11" and python_version < "4.0"
iniconfig==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
jinja2==3.1.4 ; python_version >= "3.11" and python_version < "4.0"
jiter==0.7.0 ; python_version >= "3.11" and python_version < "4.0"
jsonpatch==1.33 ; python_version >= "3.11" and python_version < "4.0"
jsonpointer==3.0.0 ; python_version >= "3.11" and python_version < "4.0"
jsonschema-specifications==2024.10.1 ; python_version >= "3.11" and python_version < "4.0"
jsonschema==4.23.0 ; python_version >= "3.11" and python_version < "4.0"
jupyter-client==8.6.3 ; python_version >= "3.11" and python_version < "4.0"
jupyter-core==5.7.2 ; python_version >= "3.11" and python_version < "4.0"
jupyterlab-pygments==0.3.0 ; python_version >= "3.11" and python_version < "4.0"
langchain-community==0.3.5 ; python_version >= "3.11" and python_version < "4.0"
langchain-core==0.3.15 ; python_version >= "3.11" and python_version < "4.0"
langchain-google-genai==2.0.4 ; python_version >= "3.11" and python_version < "4.0"
langchain-google-vertexai==2.0.7 ; python_version >= "3.11" and python_version < "4.0"
langchain-text-splitters==0.3.2 ; python_version >= "3.11" and python_version < "4.0"
langchain==0.3.7 ; python_version >= "3.11" and python_version < "4.0"
langsmith==0.1.141 ; python_version >= "3.11" and python_version < "4.0"
levenshtein==0.26.1 ; python_version >= "3.11" and python_version < "4.0"
litellm==1.52.2 ; python_version >= "3.11" and python_version < "4.0"
markdown-it-py==3.0.0 ; python_version >= "3.11" and python_version < "4.0"
markupsafe==3.0.2 ; python_version >= "3.11" and python_version < "4.0"
marshmallow==3.23.1 ; python_version >= "3.11" and python_version < "4.0"
mdurl==0.1.2 ; python_version >= "3.11" and python_version < "4.0"
mistune==3.0.2 ; python_version >= "3.11" and python_version < "4.0"
multidict==6.1.0 ; python_version >= "3.11" and python_version < "4.0"
mypy-extensions==1.0.0 ; python_version >= "3.11" and python_version < "4.0"
nbclient==0.10.0 ; python_version >= "3.11" and python_version < "4.0"
nbconvert==7.16.4 ; python_version >= "3.11" and python_version < "4.0"
nbformat==5.10.4 ; python_version >= "3.11" and python_version < "4.0"
nbsphinx==0.9.5 ; python_version >= "3.11" and python_version < "4.0"
nest-asyncio==1.6.0 ; python_version >= "3.11" and python_version < "4.0"
numpy==1.26.4 ; python_version >= "3.11" and python_version < "4.0"
openai>=1.56.1 ; python_version >= "3.11" and python_version < "4.0"
orjson==3.10.11 ; python_version >= "3.11" and python_version < "4.0"
packaging==24.2 ; python_version >= "3.11" and python_version < "4.0"
pandas==2.2.3 ; python_version >= "3.11" and python_version < "4.0"
pandoc==2.4 ; python_version >= "3.11" and python_version < "4.0"
pandocfilters==1.5.1 ; python_version >= "3.11" and python_version < "4.0"
platformdirs==4.3.6 ; python_version >= "3.11" and python_version < "4.0"
pluggy==1.5.0 ; python_version >= "3.11" and python_version < "4.0"
plumbum==1.9.0 ; python_version >= "3.11" and python_version < "4.0"
ply==3.11 ; python_version >= "3.11" and python_version < "4.0"
propcache==0.2.0 ; python_version >= "3.11" and python_version < "4.0"
proto-plus==1.25.0 ; python_version >= "3.11" and python_version < "4.0"
protobuf==5.28.3 ; python_version >= "3.11" and python_version < "4.0"
pyasn1-modules==0.4.1 ; python_version >= "3.11" and python_version < "4.0"
pyasn1==0.6.1 ; python_version >= "3.11" and python_version < "4.0"
pycparser==2.22 ; python_version >= "3.11" and python_version < "4.0" and implementation_name == "pypy"
pydantic-core==2.26.0 ; python_version >= "3.11" and python_version < "4.0"
pydantic-settings==2.6.1 ; python_version >= "3.11" and python_version < "4.0"
pydantic==2.10.0b1 ; python_version >= "3.11" and python_version < "4.0"
pydub==0.25.1 ; python_version >= "3.11" and python_version < "4.0"
pygments==2.18.0 ; python_version >= "3.11" and python_version < "4.0"
pymupdf==1.24.13 ; python_version >= "3.11" and python_version < "4.0"
pyparsing==3.2.0 ; python_version >= "3.11" and python_version < "4.0"
pytest-xdist==3.6.1 ; python_version >= "3.11" and python_version < "4.0"
pytest==8.3.3 ; python_version >= "3.11" and python_version < "4.0"
python-dateutil==2.9.0.post0 ; python_version >= "3.11" and python_version < "4.0"
python-dotenv==1.0.1 ; python_version >= "3.11" and python_version < "4.0"
python-levenshtein==0.26.1 ; python_version >= "3.11" and python_version < "4.0"
pytz==2024.2 ; python_version >= "3.11" and python_version < "4.0"
pywin32==307 ; (platform_system == "Windows" or sys_platform == "win32") and platform_python_implementation != "PyPy" and python_version >= "3.11" and python_version < "4.0"
pyyaml==6.0.2 ; python_version >= "3.11" and python_version < "4.0"
pyzmq==26.2.0 ; python_version >= "3.11" and python_version < "4.0"
rapidfuzz==3.10.1 ; python_version >= "3.11" and python_version < "4.0"
referencing==0.35.1 ; python_version >= "3.11" and python_version < "4.0"
regex==2024.11.6 ; python_version >= "3.11" and python_version < "4.0"
requests-toolbelt==1.0.0 ; python_version >= "3.11" and python_version < "4.0"
requests==2.32.3 ; python_version >= "3.11" and python_version < "4.0"
rich==13.9.4 ; python_version >= "3.11" and python_version < "4.0"
rpds-py==0.21.0 ; python_version >= "3.11" and python_version < "4.0"
rsa==4.9 ; python_version >= "3.11" and python_version < "4"
setuptools==75.3.0 ; python_version >= "3.11" and python_version < "4.0"
shapely==2.0.6 ; python_version >= "3.11" and python_version < "4.0"
shellingham==1.5.4 ; python_version >= "3.11" and python_version < "4.0"
six==1.16.0 ; python_version >= "3.11" and python_version < "4.0"
sniffio==1.3.1 ; python_version >= "3.11" and python_version < "4.0"
snowballstemmer==2.2.0 ; python_version >= "3.11" and python_version < "4.0"
soupsieve==2.6 ; python_version >= "3.11" and python_version < "4.0"
sphinx-autodoc-typehints==2.5.0 ; python_version >= "3.11" and python_version < "4.0"
sphinx-rtd-theme==3.0.1 ; python_version >= "3.11" and python_version < "4.0"
sphinx==8.1.3 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-applehelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-devhelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-htmlhelp==2.1.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-jquery==4.1 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-jsmath==1.0.1 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-qthelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-serializinghtml==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sqlalchemy==2.0.35 ; python_version >= "3.11" and python_version < "4.0"
tenacity==9.0.0 ; python_version >= "3.11" and python_version < "4.0"
tiktoken==0.8.0 ; python_version >= "3.11" and python_version < "4.0"
tinycss2==1.4.0 ; python_version >= "3.11" and python_version < "4.0"
tokenizers==0.20.3 ; python_version >= "3.11" and python_version < "4.0"
tornado==6.4.2 ; python_version >= "3.11" and python_version < "4.0"
tqdm==4.67.0 ; python_version >= "3.11" and python_version < "4.0"
traitlets==5.14.3 ; python_version >= "3.11" and python_version < "4.0"
typer==0.12.5 ; python_version >= "3.11" and python_version < "4.0"
types-pyyaml==6.0.12.20240917 ; python_version >= "3.11" and python_version < "4.0"
typing-extensions==4.12.2 ; python_version >= "3.11" and python_version < "4.0"
typing-inspect==0.9.0 ; python_version >= "3.11" and python_version < "4.0"
tzdata==2024.2 ; python_version >= "3.11" and python_version < "4.0"
uritemplate==4.1.1 ; python_version >= "3.11" and python_version < "4.0"
urllib3==2.2.3 ; python_version >= "3.11" and python_version < "4.0"
webencodings==0.5.1 ; python_version >= "3.11" and python_version < "4.0"
websockets==13.1 ; python_version >= "3.11" and python_version < "4.0"
wheel==0.44.0 ; python_version >= "3.11" and python_version < "4.0"
yarl==1.17.1 ; python_version >= "3.11" and python_version < "4.0"
youtube-transcript-api==0.6.2 ; python_version >= "3.11" and python_version < "4.0"
zipp==3.20.2 ; python_version >= "3.11" and python_version < "4.0"
uvicorn==0.23.2 ; python_version >= "3.11" and python_version < "4.0"
fastapi==0.103.0 ; python_version >= "3.11" and python_version < "4.0"
aiohttp==3.11.11 ; python_version >= "3.11" and python_version < "4.0"
pyyaml==6.0.2 ; python_version >= "3.11" and python_version < "4.0"
playwright ; python_version >= "3.11" and python_version < "4.0"
```

## File: `data/transcripts/Tharsis_AI.txt`
```
<Person1> "Welcome to Podcastfy - your personal GenAI podcast! In this episode, we're diving deep into the world of AI, data science, and what the future holds for these rapidly evolving fields." </Person1>

<Person2> "It's fascinating stuff! We've seen such explosive growth in these areas, especially with tools like GPT becoming so prevalent. It feels like we're on the cusp of something huge, doesn't it?" </Person2>

<Person1> "Absolutely. And to guide us through this intricate landscape, we're tapping into a conversation with a true expert - Tharsis Souza. He's a computer scientist who's passionate about data-driven products, a Senior Vice President at Two Sigma Investments, and a lecturer at Columbia University. He's also deeply involved in mentoring up-and-coming talent in the field." </Person2>

<Person2> "Wow, he sounds incredibly accomplished. So, what insights did Tharsis share in this conversation?" </Person2>

<Person1> "Well, he dives into the idea of AGI - artificial general intelligence. You know, that concept of machines achieving human-level intelligence and beyond. He seems to believe that progress in AI will undeniably continue, but pinpointing exactly when a machine can fully replicate a human job is tricky." </Person1>

<Person2> "That makes sense. There are so many nuances to every job, even ones that seem straightforward. It's not just about processing information; it's about understanding context, emotions, and all those subtle things humans do." </Person2>

<Person1> "Right! And Tharsis points out that this is where things get really interesting. He talks about how AI, in its current form, is essentially mimicking human behavior. It's excellent at recognizing patterns and making predictions based on massive datasets, but true creativity, that spark of originality, is still a hurdle." </Person1>

<Person2> "So, how do we bridge that gap? How do we get AI to think outside the box, so to speak?" </Person2>

<Person1> "Tharsis highlights the importance of providing AI with a 'structured environment of reality' to play in, similar to how AI excels in games with defined rules and objectives. He even suggests that teaching AI to code and allowing it to see the consequences of its code could be a promising avenue." </Person1>

<Person2> "That's a fascinating thought! Allowing AI to experiment and learn in a controlled but dynamic environment like that could lead to some unexpected breakthroughs." </Person2>

<Person1> "Exactly! And while there's a ton of data available online, Tharsis emphasizes the need for more data on 'normal' human behavior, emotions, and thought processes. Basically, we need to teach AI how to be more human." </Person1>

<Person2> "It's like we're trying to create a digital version of ourselves, but without the instruction manual." </Person2>

<Person1> "In a way, yes! Tharsis also delves into the limitations of current AI models, like GPT. While these models are constantly being refined, he uses the analogy of GPT-3 being like a lizard brain and GPT-4 being akin to a cat's brain in terms of scale. We still have a long way to go before we reach the complexity of the human brain." </Person1>

<Person2> "So, if we're talking about exponential growth, are we headed towards a singularity? That point where AI surpasses human intelligence and things accelerate at an unimaginable pace?" </Person2>

<Person1> "That's the million-dollar question! Tharsis seems to believe that while we haven't hit an asymptote yet, there's no telling how things will unfold once we reach and surpass human-level intelligence. It could be a series of breakthroughs, new paradigms we haven't even conceived of yet." </Person1>

<Person2> "It's both exciting and a bit daunting, isn't it? Knowing that we're potentially on the verge of something so transformative." </Person2>

<Person1> "Absolutely. And that's the beauty of it! We're venturing into uncharted territory, pushing the boundaries of what's possible with AI. It's a journey filled with endless possibilities and, of course, a healthy dose of the unknown." </Person1>

<Person2> "Thanks for breaking down these complex concepts for us. It's been an eye-opening look at the future of AI and data science. Until next time on Podcastfy!" </Person2> 
```

## File: `data/transcripts/transcript_6f899382ed0e4c18b4a4efbf7910ce17.txt`
```
<Person1> WELCOME TO PODCASTFY - YOUR PERSONAL GenAI PODCAST. What's up everyone?  It's  uh  pretty wild out there in tech right now, right? </Person1>

<Person2> Wild is an understatement! It seems like every day there's some groundbreaking AI development dropping. What's caught your eye today? </Person2>

<Person1> Right? Like remember those good old days when Siri could barely set a timer?  <laughs> Now we're talking about AI that can synthesize information from a ton of sources and turn it into a full-blown podcast, complete with witty banter and "umm"s and "ahh"s. </Person1>

<Person2> Wait, seriously? That's nuts! Is that even possible? </Person2>

<Person1> Totally! It's this thing called NotebookLM, and it's like Google's answer to the whole generative AI craze. Deirdre Bosa from CNBC did this report on it, and it's got everyone buzzing. Basically, you feed it a bunch of documents, articles, whatever you want, and it spits out a podcast episode discussing it.  </Person1>

<Person2>  Hold up, like an actual podcast with different voices and everything? This isn't just another text-to-speech robot voice, right?  </Person2>

<Person1>  Nope, not even close! They actually had this example playing on CNBC where they used NotebookLM to analyze a JPMorgan survey about iPhone sales. And honestly? The AI hosts sounded incredibly natural, like two tech bros chatting over a beer.  </Person1>

<Person2> That's kinda scary, honestly. What are the implications for, you know, actual human podcasters like us? </Person2>

<Person1> I know, right? It's a valid concern! Like Bosa mentioned, it's a total game-changer and has the potential to shake things up big time in the podcasting world. But hey, maybe it's a good thing, pushing us to be even more creative and engaging. </Person1> 

<Person2>  True! But the legal stuff around it must be a nightmare. Using people's voices, copyright issues – it sounds like a minefield.  </Person2>

<Person1> Totally agree. Bosa actually touched on that, saying it's a huge debate right now in the AI world.  Like how much can you replicate someone's voice or likeness without their consent?  These are all things that are still being figured out. It's like the Wild West out here! </Person1>

<Person2>  Wow. It's mind-blowing how quickly this tech is evolving. What other crazy AI stuff is on the horizon, I wonder?  </Person2>

<Person1>  Who knows?  But one thing's for sure, it's gonna be an interesting ride.  Alright,  that's it for today's episode of Podcastfy.  We'll catch you all next time! </Person1>

<Person2> Peace out! </Person2> 
```

## File: `data/transcripts/transcript_7e84bb13b26f4ab78dda30d04d461838.txt`
```
<Person1>
<prosody rate="90%" pitch="medium">
"Welcome to Tech Crossroads  - Where Innovation Meets Scrutiny! Today, we're diving deep into the fascinating world of artificial intelligence, or AI as it's more commonly known. Uh, it's a field that's been making waves for decades, and now, it's really starting to impact our everyday lives in ways we never imagined."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"I agree, AI is everywhere these days. From the smartphones in our pockets to the algorithms that curate our news feeds, it's becoming increasingly difficult to escape its influence. But while AI offers incredible potential, I can't help but feel a sense of unease about its rapid development. It's like we're opening Pandora's Box, and we're not entirely sure what we'll find inside."
</prosody>
</Person2>

<Person1>
<prosody rate="95%" pitch="medium">
"I see your point. AI does raise some serious ethical concerns, and it's crucial that we address them proactively. But let's not forget the incredible benefits AI brings to the table. Think about the advancements in healthcare, where AI is helping doctors diagnose diseases earlier and more accurately. Or in transportation, where self-driving cars have the potential to reduce accidents and save lives."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"Those are valid points, but I'm still wary of the potential downsides. One of my biggest concerns is the issue of algorithmic bias. We've already seen instances where AI systems have perpetuated existing societal biases, leading to discrimination against certain groups. For example, facial recognition algorithms have been shown to be less accurate for people with darker skin tones, which could have serious implications for law enforcement and security."
</prosody>
</Person2>

<Person1>
<prosody rate="90%" pitch="medium">
"Interesting. You're right, algorithmic bias is a significant problem, and it's something that needs to be addressed head-on. The good news is that researchers are actively working on developing techniques to mitigate bias in AI systems. For instance, they're exploring ways to ensure that training data is more representative of diverse populations and that algorithms are designed to be more fair and equitable."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"I'm glad to hear that, but I'm also concerned about the lack of transparency in many AI systems. Often, even the developers themselves don't fully understand how these complex algorithms work. This makes it difficult to identify and correct biases, and it raises questions about accountability when things go wrong."
</prosody>
</Person2>

<Person1>
<prosody rate="95%" pitch="medium">
"Got it. Transparency is indeed crucial, and there's a growing movement towards developing explainable AI, where the decision-making processes of AI systems are more understandable to humans. This will not only help us identify and address biases but also build trust in AI technology."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"Another concern I have is the potential for AI to exacerbate existing inequalities. As AI becomes more sophisticated, it could automate a wide range of jobs, potentially leading to mass unemployment and widening the gap between the rich and the poor."
</prosody>
</Person2>

<Person1>
<prosody rate="90%" pitch="medium">
"I understand your concern about technological unemployment. It's a valid point, and it's something that policymakers need to consider seriously. However, history has shown that technological advancements often create new jobs, even as they displace old ones. The key is to ensure that workers have the skills and training they need to adapt to the changing job market."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"That's true, but this time feels different. AI has the potential to automate not just manual labor but also cognitive tasks that were once thought to be the exclusive domain of humans. This could have a profound impact on the job market, and we need to be prepared for the challenges it presents."
</prosody>
</Person2>

<Person1>
<prosody rate="95%" pitch="medium">
"You raise a valid point. The nature of work is undoubtedly changing, and we need to adapt our education and training systems to prepare people for the jobs of the future. This includes fostering skills such as critical thinking, creativity, and problem-solving, which are less likely to be automated."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"Beyond the economic implications, I'm also concerned about the potential for AI to be used for malicious purposes. Imagine AI-powered surveillance systems that track our every move or autonomous weapons that can kill without human intervention. These are terrifying possibilities that we need to guard against."
</prosody>
</Person2>

<Person1>
<prosody rate="90%" pitch="medium">
"I agree, the potential for AI to be weaponized is a serious concern. That's why it's crucial that we develop international regulations and ethical guidelines for the development and use of AI, especially in sensitive areas like military applications."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"I'm glad to hear that, but I'm not sure if regulations alone will be enough. We also need to foster a culture of responsible AI development, where ethics are considered from the very beginning of the design process."
</prosody>
</Person2>

<Person1>
<prosody rate="95%" pitch="medium">
"Absolutely. We need to ensure that AI is developed and used in a way that benefits humanity as a whole, not just a select few. This requires a multi-faceted approach, involving researchers, policymakers, industry leaders, and the public."
</prosody>
</Person1>

<Person2>
<prosody rate="100%" pitch="high">
"One final thought: as AI becomes more powerful, it raises fundamental questions about what it means to be human. If machines can think, learn, and even create, what does that say about our own unique abilities and our place in the world?"
</prosody>
</Person2>

<Person1>
<prosody rate="90%" pitch="medium">
"That's a profound question, and one that philosophers have been grappling with for centuries. As AI continues to evolve, it will undoubtedly challenge our understanding of ourselves and our relationship with technology. It's a journey that will require careful consideration, open dialogue, and a commitment to shaping a future where AI serves humanity, not the other way around."
</prosody>
</Person1>
```

## File: `data/transcripts/transcript_8d03dac5011244dcbe56202c23bfa6bb.txt`
```
<Person1>
Welcome to Podcastfy - your personal GenAI podcast! In this episode, we'll be talking about the evolution of podcasting! 
<emphasis>
Fascinating stuff!
</emphasis>
</Person1>
<Person2>
Alright, so let's start with the basics. What exactly IS a podcast?
</Person2>
<Person1>
<emphasis>
Essentially
</emphasis>, it's like a radio show, but you can listen to it whenever you want, on your own device. You subscribe to a show and download or stream the episodes. 
</Person1>
<Person2>
Okay, so it's not just audio? I've seen video podcasts too.
</Person2>
<Person1>
You're right, some podcasts do incorporate video, either as the main format or alongside the audio. But audio-only is still the most common. It all started in the early 2000s.
</Person1>
<Person2>
Really? That recent?
</Person2>
<Person1>
Yeah! It all started with RSS feeds - a way to get updates to your computer. People realized they could use these feeds to deliver audio files. The term "podcasting" itself?  That came about in 2004.
</Person2>
<Person1>
Uh-huh.  A journalist named Ben Hammersley combined "iPod" and "broadcast" to coin the term.  Catchy, right?
</Person1>
<Person2>
Definitely! So, how did it go from a techy thing to, well, EVERYWHERE?
</Person2>
<Person1>
Apple played a huge role! In 2005, they added podcast support to iTunes. Suddenly, anyone could listen to podcasts on their iPods, which were massively popular. That changed the game.
</Person2>
<Person1>
Interesting.  But what about now?  Apple's not the only player anymore, right?
</Person2>
<Person1>
Exactly! We have Spotify, Google Podcasts, and tons of other platforms. It's a rapidly growing industry.  Millions of podcasts are out there, covering pretty much every topic imaginable. True crime, comedy, news, you name it.
</Person2>
<Person1>
I see, it's quite remarkable how much it's grown.
</Person1>
<Person2>
And it's only getting bigger! Speaking of bigger, I'm curious about the technology behind it all. What goes into actually MAKING a podcast?
</Person2>
<Person1>
Well, the basics are pretty simple: a good microphone and some recording software. But creating high-quality audio can get more complex.  Many podcasters invest in soundproofing, mixing equipment, editing software...it can become quite a production.
</Person1>
<Person2>
So, there's quite a bit more to it than meets the eye, or should I say, the ear?
</Person2>
<Person1>
Exactly! And that's just the audio side. Many podcasts also have websites, show notes, transcripts... it's a whole ecosystem!
</Person1>
<Person2>
That's fascinating! Thanks for breaking it all down. It sounds like podcasting has come a long way in a short time, and its future is quite bright!
</Person2>
<Person1>
I totally agree. Thanks for joining us for this episode of Podcastfy!  See you in the next one!
</Person1>
```

## File: `data/transcripts/transcript_c8b400052bbe48fa99b10c93ad8c3576.txt`
```
<Person1> "Welcome to PODCASTFY - Your Personal Generative AI Podcast!  Hot off the digital press, we're diving into OpenAI's latest power move: snatching up Chat.com!  Can you believe it?" 
</Person1><Person2> "Seriously?! Chat.com? That's like owning prime real estate in the internet world.  It's gotta be worth a fortune!" 
</Person2><Person1> "Well, rumors are swirling around the $15 million mark, maybe even more!  Think about it, it went for that much just last year to HubSpot's CTO, Dharmesh Shah, and he just sold it to OpenAI! Apparently even got some OpenAI shares in the deal. Pretty sweet, huh?"
</Person1><Person2> "Wow,  OpenAI shares as part of the deal? That's insightful!  But why Chat.com?  Don't they already have ChatGPT?" 
</Person2><Person1> "Exactly!  It's all about accessibility, baby! Making ChatGPT even easier to find.  Right now, it's just a redirect, but who knows what the future holds? Maybe a whole new platform built around it!"
</Person1><Person2> "Ooh, interesting.  So, it's less about a new product, more about grabbing that sweet, sweet keyword: 'chat'."
</Person2><Person1> "Precisely!  It's like buying the best billboard on the digital highway.  Everyone searching for 'chat' might just stumble upon OpenAI's goldmine." 
</Person1><Person2> "Smart move.  But grabbing Chat.com isn't the only thing they've been up to, is it?"
</Person2><Person1> "Oh no,  not even close! They're on a roll!  ChatGPT search, their own built-in search engine—taking on Google, no less!  And Canvas?!  A brand-new way to use ChatGPT for writing and coding? Game changer!"
</Person1><Person2> "Hold on, Canvas?  I haven't heard about that one.  Fill me in!"
</Person2><Person1> "Think of it as a more interactive space within ChatGPT.  Perfect for crafting documents,  collaborative coding, you name it! It's like they're building a whole ecosystem around ChatGPT. Plus, they just dropped OpenAI o1, whatever *that* is! "
</Person1><Person2>  "They're certainly not resting on their laurels!  A for-profit transition in California? Hiring the former Pebble CEO, Gabor Cselle, for a 'secret project'? What's next, world domination? "
</Person2><Person1> "Haha, right? And let's not forget SimpleQA! OpenAI is pushing the boundaries of AI research left and right! I'm slightly concerned about these developments though, don't you think they are going a little too fast?" 
</Person1><Person2> "I see your point. It *is* a lot, and fast.   While innovation is exciting, responsible development is crucial. We need to make sure these advancements benefit humanity, not the other way around." 
</Person2><Person1> "Absolutely.  But hey, with all this happening, the AI landscape is definitely anything but boring! It'll be interesting to see how these moves play out, especially against giants like Google." 
</Person1><Person2> "Couldn't agree more!   OpenAI is certainly one to watch.  This is just the beginning, folks.  Buckle up!"
</Person2><Person1> "And that’s a wrap for today’s episode on OpenAI's strategic moves in the AI arena! Until next time, stay tuned to PODCASTFY!" </Person1>
```

## File: `data/transcripts/transcript_e33ff2b40b534c5b9b578f2f51175e60.txt`
```
<Person1> Welcome to Podcastfy - your personal GenAI podcast! </Person1> 

<Person2> And welcome back, listeners! Today, we're discussing podcasts! Specifically, their history and how they work. </Person2>

<Person1> Right! Podcasts, those digital audio files we all know and love,  are delivered online in episodes and can be listened to on various devices, anytime, anywhere. </Person1> 

<Person2> Exactly! And while they share similarities with radio shows, podcasts offer something different: convenience. But where did this all begin? </Person2>

<Person1>  It all started in the early 2000s, before Apple jumped on board.  Remember  "MyAudio2Go.com"? They offered downloadable news stories for PCs and MP3 players way back in 2000! </Person1> 

<Person2> Oh, right! But it wasn't until 2004 that the term "podcasting" was coined, right? <Person1> Uh-huh! </Person1> By Ben Hammersley, a journalist. Soon after, it was adopted by Adam Curry and the iPodder-dev mailing list, leading to its widespread use. </Person2> 

<Person1> And the rest is history! <laughs> But it wasn't always smooth sailing. Remember the legal battles over the term "podcast"? </Person1> 

<Person2> Yeah. Apple was pretty aggressive in protecting its "iPod" trademark, even though podcasting predates the iPod's podcasting capabilities. In fact,  they even went after companies using "pod" in their names! </Person2>

<Person1> Talk about a trademark battle! And then there was the Personal Audio lawsuit - remember them? They tried claiming a patent on podcasting technology!  Thankfully, the Electronic Frontier Foundation stepped in and helped invalidate key provisions. </Person1>

<Person2> Definitely a win for podcasting!  But let's get technical: how are these audio gems actually made? </Person2>

<Person1> Well, at its core, you need a computer, a microphone, and recording/streaming software. But for better sound, a soundproof room and headphones are recommended. And if we’re talking video podcasts, webcams and lighting become essential.   </Person1> 

<Person2> Of course! And once you've recorded your podcast, it's uploaded to a server and distributed via RSS feeds to platforms like Apple Podcasts and Spotify. </Person2>

<Person1>  From true crime to comedy, educational to fictional, there’s something out there for everyone! It's incredible how this simple concept has revolutionized audio content creation and consumption. </Person1> 

<Person2>  Absolutely.  And it's easier than ever to find and listen to podcasts. Dedicated apps on our smartphones, or even just streaming them online - the possibilities are endless!  Thanks for tuning in to this episode of Podcastfy! </Person2>

<Person1>  Until next time! </Person1> 
```

## File: `data/transcripts/transcript_e99daed9d4aa4e3aa4ebd589096099c0.txt`
```
<Person1> Welcome to Podcastfy - Your Personal GenAI Podcast! <emphasis>Uh</emphasis>, what's up everyone?  You know, it's funny how we use this technology every day, but have you ever stopped to think about the history of podcasts?  </Person1>

<Person2> I know what you mean.  It's like, they're just <emphasis> there</emphasis>, you know? We hit play and boom - instant entertainment or information. But, where did this all start? </Person2>

<Person1> Well, get this: the word "podcast" is actually a mashup of "iPod" and "broadcast"! Ben Hammersley, a journalist, first used it back in 2004. </Person1>

<Person2> Wow, 2004?  That's way earlier than I would've guessed! But, weren't MP3 players around before that? </Person2>

<Person1> Totally! In fact, there was a company, i2Go, that offered a service kinda like podcasting back in 2000. It let people download news to their MP3 players.  They were onto something, but it fizzled out quickly. </Person1>

<Person2> So, if that was happening in 2000, what really made podcasts take off later?  </Person2>

<Person1> It was a perfect storm of tech advancements. Apple launched iTunes with podcast support in 2005, which made listening SO much easier. That, plus cheaper recording tech and the rise of smartphones - it all just exploded from there. </Person2>

<Person2>  That makes a lot of sense. It's interesting, though, that you mentioned Apple was such a driving force. Weren't there legal battles over the whole "pod" terminology?  </Person2>

<Person1> Oh yeah, big time. Apple got pretty aggressive going after companies using "pod" in their names, even sending out cease and desist letters. They claimed people associated "pod" so strongly with the iPod that it fell under their trademark. I mean, they even tried to trademark "podcast" itself!  </Person1>

<Person2> Wow, really? Seems like a bit of a stretch, but I guess they wanted to protect their brand.  So, aside from straight-up talk shows, what other types of podcasts have become popular? </Person2>

<Person1> Oh man, there's like, a whole universe of podcasts now! You've got fiction podcasts that are basically like audio dramas, complete with actors, sound effects, the works. There's also the enhanced podcasts that combine audio with slideshows - super cool for educational stuff. And then, you can't forget the video podcasts!  It's wild how much it's evolved from those early days. </Person1>

<Person2> Yeah, it really is amazing. And it seems like podcasting is only getting bigger. I mean, look at how many podcasts and episodes there are now! </Person1>

<Person1> For sure! And it's not just about listening anymore. Live shows are becoming huge, too! It's like a whole new way for creators to connect with audiences. Who knows what the future holds for podcasting, but I'm along for the ride!  </Person1>

<Person2> Me too!  Until next time on Podcastfy - Your Personal GenAI Podcast. </Person2>
```

## File: `data/transcripts/transcript_f6ab3ee241444e999ed4d1142564b9fe.txt`
```
<Person1> "Welcome to Podcastfy - YOUR Personal GenAI Podcast! You know, the other day I was struggling to keep up with all the industry news, articles, blog posts… it's just too much!"</Person1>
<Person2> "Ugh, tell me about it! I feel like I'm always drowning in a sea of tabs and bookmarks." </Person2>
<Person1> <emphasis> "Exactly! </emphasis> That's where I stumbled upon this really cool tool called Podcastfy. It's basically a game-changer for anyone who wants to consume information more efficiently." </Person1>
<Person2> "Podcastfy? Okay, you're gonna have to break that down for me. What is it, some kind of magic podcasting fairy godmother?"</Person2> 
<Person1> "Well, not exactly a fairy godmother, but pretty close! It's actually an LLM-based Python package and CLI tool. Basically, it lets you take all that text-based content, like articles, web pages, even PDFs, and transform it into, get ready for it… engaging audio conversations!" </Person1>
<Person2> "Wait, seriously? It turns like, a boring research paper into a podcast episode I actually *want* to listen to?" </Person2>
<Person1> "You got it! And the best part is, it's not just summarizing. It creates a fully-fledged conversation, like you and I are having right now, but with AI-generated hosts. It's crazy realistic!" </Person1>
<Person2> "That's wild! But how does it actually work? Do you need to be some kind of coding whiz to use it?" </Person2>
<Person1> "Not at all! I mean, if you're into coding, they have a Python package you can use. But for the rest of us, there's a super user-friendly CLI.  You basically tell it where to get the content, like a URL or file path, and bam! It does its magic." </Person1>
<Person2> "Okay, I'm intrigued.  What about the voices?  Are we talking robotic monotone or something closer to, you know, human?" </Person2>
<Person1> "That's the other cool part! They've integrated with OpenAI and ElevenLabs, which are known for their super natural-sounding text-to-speech. You can even customize the languages, so it's perfect for reaching a global audience." </Person1>
<Person2> "Alright, you've officially blown my mind.  I never thought I'd be geeking out over a podcasting tool! Give me some real-world examples, though.  How are people actually using this thing?" </Person2>
<Person1> "Oh, the possibilities are endless! Imagine you're a busy professional trying to stay on top of industry trends.  Instead of spending hours reading articles, Podcastfy can whip up an audio summary for your commute.  Or think about students who learn better by listening. They can have their textbooks turned into engaging lectures!" </Person1>
<Person2> "I'm already seeing the potential here. This could be huge for accessibility, making information available to people who struggle with traditional reading." </Person2>
<Person1> "Absolutely! And it's not just limited to educational content.  Think about repurposing marketing materials, creating audio versions of websites for visually impaired users, even summarizing those super long podcasts we all love but never seem to have time for." </Person1>
<Person2> "Hold on, you can summarize other podcasts with this? That's genius!" </Person2>
<Person1> "Right? And if you're into personal branding, you can even use it to create a unique audio presentation from your resume or LinkedIn profile.  Talk about making a memorable impression!" </Person1>
<Person2> " Okay, I'm sold. Podcastfy sounds like a game-changer. Where can our listeners learn more about it?" </Person2>
<Person1> " You can sign-up at podcastfy.me to get updates! Turning text to audio so easily. Sounds like something that would be incredibly helpful, and fun to use! What do you think?" </Person1>
<Person2> "Definitely! The idea of having complex information transformed into an engaging conversation is mind-blowing. It has implications for education, accessibility, and even entertainment.  It's exciting to see how technology is evolving to make information more digestible and accessible for everyone." </Person2>
<Person1> "Couldn't agree more.  Well, on that note, let's wrap up this episode.  Thanks for joining me today, and be sure to check out next time when we’ll…." </Person1> 
```

## File: `data/transcripts/transcript_local_model.txt`
```


Person1: 
Person1: Hey, welcome to PODCASTFY! Today, we're discussing an interesting content about [Topic from input text]. Let's dive in!

Person2: I'm excited to discuss this! What's the main point of the content we're covering today?

Person1: (Skeptically) Really? We should be discussing a topic related to [Topic from input text]?

Person2: (Frustrated) Why did you ask that question, Tharsis? You know we're discussing an interesting content about [Topic from input text].

Person1: Well, because it seems like you've already decided the topic, and are just going through the motions. I mean, why not just let me explain what it is and you can listen to the conversation?

Person2: (frustrated) And where would we be in the conversation if you didn't ask that question?

Person1: Because that's how you get stuck on a topic. If you haven't thought about it beforehand, or if you have a particular preconception about it, then the discussion will not go anywhere.

Person2: (angrily) And I am not stuck on anything! I know what's going on, and I'm excited to learn more!

Person1: Okay, fair enough. But let's start by discussing the content itself. What did you notice when you read through it?

Person2: (shrugs) Not much, actually. It seems like a lot of jargon and acronyms, but I have no idea what any of them mean.

Person1: (nodding) Good point. Let's start with the basics - what are some key terms or concepts that we're discussing?

Person2: (confused) Okay, I see "Big Data", "Machine Learning" and "Predictive Analytics". But I don't know why they're important, and I don't really understand how they work.

Person1: (understandingly) Okay, fair enough. That's because these are specialized terms that we'll need to explain to you. Let's start with Big Data - what is it? How does it differ from traditional data collection methods like surveys and questionnaires? And then, let's talk about Machine Learning. How does this work?

Person2: (interesting) Okay, I understand that. But why is Machine Learning important? What are the benefits of using it in predictive analytics?

Person1: (nodding) Great questions! Machine learning is a technique for analyzing large amounts of data to make predictions based on past data and/or other sources of information. This can be used to identify patterns, trends, and even predict future events with high accuracy. For example, in financial analytics, it's used to analyze historical data to detect abnormalities or anomalies that indicate potential risks or opportunities for trading and investment.

Person2: (surprised) Oh, okay. I see how machine learning could help me predict future events. But why does predictive analytics matter in this context? What are the benefits of using it to make investment decisions or forecast outcomes?

Person1: (nodding) Sure thing! Predictive analytics is used to identify patterns, trends, and other indicators that can help you make informed investment decisions. This is particularly important in today's market where market fluctuations are often unpredictable and uncertain. With predictive analytics, you can use historical data, industry trends, and even social media and news sources to anticipate potential risks or opportunities, and make more informed investment decisions.

Person2: (interested) So, why did you ask the question about what it meant? I mean, we already know what predictive analytics does. How can it really help us in this context?

Person1: (smiling) It's not about proving that predictive analytics works. What matters is the effectiveness of using it for a specific purpose. For instance, let's say you run a company that sells software solutions to small and medium-sized businesses. Your sales team uses predictive analytics to identify potential customers based on their behavior or preferences. They then use this information to make targeted sales calls, increasing the likelihood of converting leads into clients.

Person2: (impressed) This is really interesting! I see how predictive analytics could help me optimize my sales processes and generate more revenue. But what about the investment decision? Can it help us identify potential opportunities or risks in our portfolio?

Person1: (nodding) Sure thing! Predictive analytics can help you identify patterns, trends, and other indicators that may indicate potential investment opportunities. By analyzing historical data, industry trends, and market conditions, you can make more informed decisions about which stocks or markets to buy, and when to sell. This can also help you identify risk factors like volatility, correlation with other assets, and liquidity, helping you better manage your portfolio.

Person2: (thinking) Okay, I see how predictive analytics could be useful in this context as well. But what about the human element? How do we know if the data we're using is accurate and trustworthy?

Person1: (understandingly) That's a great question! The accuracy of data depends on many factors, including the source, the quality of the data collection methods, and the skill of the analysts who are interpreting it. However, predictive analytics is generally considered more accurate than traditional data analysis methods like surveys or questionnaires. One reason for this is that predictive models can be trained using large amounts of historical data, while survey methods may only capture a snapshot in time. In addition to accuracy, predictive analytics also offers the ability to improve decision making over time as we learn more about our data and the world around us.

Person2: (satisfied) Okay, I see how predictive analytics can make our jobs easier, but what about the complexity of it all? How much effort is required in order for me to use these tools effectively?

Person1: (understandingly) That's a great question! Predictive analytics requires significant effort and skill, which varies depending on the project or business objective. However, there are many resources available online that offer guidance and support for both beginners and experts in predictive analytics. There are also courses, workshops, and certification programs that can help you learn how to apply these tools effectively in your job or business.

Person2: (smiling) Okay, I see why it's important to invest effort into understanding this technology. But what if I don't have the time or resources for learning?

Person1: (sympathetically) It's understandable that you may not have the time or resources to invest in learning predictive analytics. That being said, there are many companies and organizations that offer free or low-cost training programs or workshops that can help you learn how to apply this technology effectively. Many universities also offer courses on predictive analytics, and there are also online resources like Udemy and Coursera that offer course materials for free.

Person2: (enthusiastic) Okay, I see the value of investing time into learning this technology. But how can I ensure that my data is accurate and reliable? Are there any best practices or standards to follow when using predictive analytics?

Person1: (nodding) Yes, absolutely! One of the most important aspects of ensuring accuracy in predictive analytics is ensuring the quality and reliability of your data. This can be done by following best practices for data collection, cleaning, and preparation. It's also essential to ensure that you have access to accurate and reliable data sources, as some tools may require specific types of data or data quality metrics.

Person2: (excited) Okay, I see how important it is to follow best practices when using predictive analytics. But do you think this technology can be used in the real world? Like, can you see it being applied by businesses or governments?

Person1: (smiling) Yes, absolutely! Predictive analytics is already being used by many organizations and government agencies around the world, from retailers to financial institutions, to predict and manage risks. These applications vary in scope but include everything from fraud detection to weather forecasting to emergency response planning.

Person2: (nodding) That's fascinating! I see how predictive analytics can be used for a wide range of applications. But what about the limitations? Is there anything that makes it difficult to use in certain scenarios, like when dealing with large datasets or when working with sensitive data?

Person1: (nodding) There are certainly limitations to using predictive analytics, especially when dealing with large datasets or sensitive data. While predictive models can be very accurate and reliable when working with large volumes of data, they may not perform as well when the volume is too small or when there are missing or noisy features in the data. The accuracy of predictive models also depends on the quality and completeness of the input data, so it's important to ensure that you have high-quality data before starting any analysis.

Person2: (smiling) Okay, I see how limitations can exist but not let them hold you back entirely. But what if my business is too small for predictive analytics? Can I still use these tools to optimize our operations or make better decisions on the fly?

Person1: (understandingly) Yes, absolutely! Predictive analytics can be used in a wide variety of contexts that don't necessarily require extensive data analysis capabilities. For example, businesses can leverage predictive analytics to optimize their supply chain or inventory management strategies, while also improving customer service and optimizing sales processes.

Person2: (excited) Okay, I see how small businesses like mine can use these tools effectively. But what if I want to go beyond simple operational improvements? Can predictive analytics be used for more complex problems or projects that require innovative solutions?

Person1: (nodding) Yes, absolutely! Predictive analytics has been used successfully in a wide variety of contexts outside of operations and supply chain optimization. For example, we've seen predictive analytics being applied to environmental monitoring, disaster response planning, and even fraud detection.

Person2: (smiling) Okay, I see how predictive analytics can be used in more complex problem-solving contexts too. But what if it's too expensive for my business? Can we still get started with these tools if they're not yet available or affordable to us?

Person1: (sympathetically) It's understandable that you may not have access to the latest and greatest predictive analytics solutions. However, there are a variety of free, open-source, and low-cost predictive analytics tools available today that can still be useful for your business. There are also many organizations who offer training and resources to help you get started with these tools.

Person2: (excited) Okay, I see how technology can be accessible even on a small budget. But what about the costs of implementing predictive analytics into our operations? How long does it typically take for us to see results or value from using these tools?

Person1: (nodding) The time and cost of implementing predictive analytics can vary based on several factors, such as the complexity of your business, the size of your data set, and the availability of skilled resources. However, for most organizations, implementation times are typically short and cost-effective, with predictive analytics typically paying for themselves in just a few months or less.

Person2: (smiling) Okay, I see how predictive analytics can be implemented quickly and efficiently. But do you think we'll ever see a time when predictive analytics becomes obsolete? Can these tools still provide value even after years of implementation?

Person1: (sympathetically) It's difficult to say that predictive analytics will always be relevant or necessary, as technology and business needs evolve. However, the tools we have today are capable of providing valuable insights and predictions for many years into the future. As new data sources become available, new algorithms are developed, and machine learning techniques improve, the potential for further advancements remains unlimited.

Person2: (nodding) Okay, I see how long-term value can be achieved with predictive analytics. But what if we decide to move our operations off of predictive analytics in a few years? Can these tools still provide us with the information we need for our business?

Person1: (nodding) Yes, absolutely! Predictive analytics has long-term value as it allows you to continue operating your business while you analyze and make better decisions. By leveraging predictive analytics in a continuously updated environment, you can identify trends and patterns that may have not been identified through traditional data collection methods.

Person2: (smiling) Okay, I see how predictive analytics has long-term value too! But what if we decide to go back to using predictive analytics after years of implementation? Can these tools still provide us with the information we need for our business?

Person1: (sympathetically) It's understandable that you may want to revisit the insights and predictions from your previous implementations. However, there is a growing body of evidence that predictive analytics continues to be valuable even after years of implementation. Some companies have successfully transitioned off of predictive analytics in their operations back into traditional data collection methods, but this can be done with some degree of success.

Person2: (excited) Okay, I see how the value of predictive analytics even after many years of implementation. But what if we decide to invest in more advanced predictive analytics solutions? Can these tools still provide us with the information we need for our business?

Person1: (nodding) Yes, absolutely! As technology and the availability of data continue to advance, so too do the capabilities of predictive analytics. With the continued development of new algorithms and machine learning techniques, it's possible that more advanced predictive analytics solutions can provide even greater value for your business.

Person2: (smiling) Okay, I see how these tools can continue to evolve with our business needs. But what if we decide to go back to traditional data collection methods? Can we still benefit from using predictive analytics in such scenarios?

Person1: (sympathetically) It's understandable that you may want to transition away from predictive analytics altogether. However, there is value to be had from the insights and predictions that predictive analytics can provide. For instance, some data analysts may prefer traditional data collection methods over predictive analytics for certain types of analysis, such as pattern recognition or correlation analysis.

Person2: (excited) Okay, I see how a return to traditional data collection methods can still benefit from predictive analytics! But what if we decide to move entirely away from predictive analytics? Can these tools still provide us with the information we need for our business?

Person1: (nodding) Yes, absolutely! While it's possible that no predictive analytics solution will ever meet all your data needs, there are many other data analysis techniques available today. As new technologies and approaches continue to emerge, the potential for new information discovery tools may continue to evolve.

Person2: (smiling) Okay, I see how traditional data collection methods can provide valuable insights too. But what if we decide not to invest in predictive analytics anymore? Can we still benefit from using data analysis techniques in other ways?

Person1: (sympathetically) While it's understandable that you may want to move away from predictive analytics altogether, there are many other ways to leverage data in your business. For instance, data visualization can be a valuable tool for understanding complex data sets and identifying patterns or trends. Data analytics could also play a role in informing decisions, such as resource allocation or decision-making processes.

Person2: (excited) Okay, I see how there are many ways to leverage data for business insight! But what if we decide to invest in predictive analytics again? Can these tools still provide us with the information we need for our business?

Person1: (nodding) Yes, absolutely! As new advancements in data science and machine learning continue to emerge, there is growing evidence that predictive analytics can offer significant value to your organization. While it's possible that no predictive analytics solution will ever meet all your data needs, the potential for other analysis techniques remains untapped.

Person2: (smiling) Okay, I see how investing in predictive analytics again may prove beneficial for our business. But what if we decide to invest in more advanced data science and machine learning techniques? Can these tools still provide us with the information we need for our business?

Person1: (sympathetically) Absolutely! As new advancements continue to emerge in data science, machine learning, and artificial intelligence, it's possible that new data analysis techniques will emerge. By investing in these areas, you can benefit from the most advanced technologies available today while still leveraging predictive analytics as a core component of your business operations.

Person2: (excited) Okay, I see how investing in these cutting-edge data science and machine learning techniques may provide us with the information we need for our business! But what if we decide to move entirely away from predictive analytics? Can these tools still provide us with the information we need for our business?

Person1: (nodding) Yes, absolutely! While it's possible that no predictive analytics solution will ever meet all your data needs, there are many other data analysis techniques available today. As new technologies and approaches continue to emerge, the potential for new information discovery tools may continue to evolve.

Person2: (smiling) Okay, I see how investing in data science and machine learning can provide valuable insights too. But what if we decide not to invest in predictive analytics anymore? Can we still benefit from using advanced data analysis techniques in other ways?

Person1: (sympathetically) While it's understandable that you may want to move away from predictive analytics altogether, there are many other ways to leverage data for business insight. For instance, data visualization can be a valuable tool for understanding complex data sets and identifying patterns or trends. Data analytics could also play a role in informing decisions, such as resource allocation or decision-making processes.

Person2: (excited) Okay, I see how there are many ways to leverage data for business insight! But what if we decide to invest in advanced data science and machine learning techniques again? Can these tools still provide us with the information we need for our business?

Person1: (nodding) Yes, absolutely! As new advancements continue to emerge in data science, machine learning, and artificial intelligence, there is growing evidence that predictive analytics can offer significant value to your organization. While it's possible that no predictive analytics solution will ever meet all your data needs, the potential for other analysis techniques remains untapped.

Person2: (smiling) Okay, I see how investing in advanced data science and machine learning techniques may prove beneficial for our business. But what if we decide to invest in more advanced predictive analytics? Can these tools still provide us with the information we need for our business?

Person1: (sympathetically) Absolutely! As new advancements continue to emerge in data science, machine learning, and artificial intelligence, it's possible that new data analysis techniques will emerge. By investing in these areas, you can benefit from the most advanced technologies available today while still leveraging predictive analytics as a core component of your business operations.

Person2: (excited) Okay, I see how investing in more advanced data science and machine learning techniques may provide us with the information we need for our business! But what if we decide to move entirely away from predictive analytics? Can we still benefit from using advanced data analysis techniques in other ways?

Person1: (nodding) Yes, absolutely! As new advancements continue to emerge in data science, machine learning, and artificial intelligence, there is growing evidence that these technologies can offer significant value to your organization. While it's possible that no predictive analytics solution will ever meet all your data needs, the potential for other analysis techniques remains untapped.

Person2: (smiling) Okay, I see how investing in advanced data science and machine learning techniques may prove beneficial for our business! But what if we decide to move entirely away from predictive analytics? Can these technologies still provide us with the information we need for our business?

Person1: (sympathetically) Absolutely! As new advancements continue to emerge in data science, machine learning, and artificial intelligence, it's possible that new data analysis techniques will emerge. By investing in these areas, you can benefit from the most advanced technologies available today while still leveraging predictive analytics as a core component of your business operations.

Person2: (excited) Okay, I see how investing in more advanced data science and machine learning techniques may provide us with the information we need for our business! But what if we decide to move entirely away from advanced data analysis techniques? Can we still benefit from using predictive analytics or other forms of advanced data analysis?

Person1: (nodding) Yes, absolutely! As new advancements continue to emerge in data science, machine learning, and artificial intelligence, there is growing evidence that these technologies can offer significant value to your organization. While it's possible that no predictive analytics solution will ever meet all your data needs, the potential for other analysis techniques remains untapped.

Person2: (smiling) Okay, I see how investing in traditional data science and machine learning techniques may provide us with the information we need for our business! But what if we decide to invest in more advanced predictive analytics? Can these tools still benefit our business from a data analysis perspective?

Person1: (sympathetically) Absolutely! As new advancements continue to emerge in predictive analytics, it's possible that new data analysis techniques will emerge. By investing in these areas, you can benefit from the most advanced technologies available today while still leveraging predictive analytics as a core component of your business operations.</s>
```

## File: `data/urls/urls_FRENCH.txt`
```
https://agroclim.inrae.fr/unite/historique
https://agroclim.inrae.fr/unite/objectif
https://agroclim.inrae.fr/unite/missions-au-service-de-la-communaute-inrae
https://agroclim.inrae.fr/unite/organisation-et-personnel
https://agroclim.inrae.fr/services-et-outils/reseau-agroclimatique
https://agroclim.inrae.fr/services-et-outils/indicateurs-du-climat
https://agroclim.inrae.fr/reseaux-et-partenariats/partenaires
```

## File: `data/urls/urls_NEXUS.txt`
```
https://www.youtube.com/watch?v=Ze6diMt1g_s
https://www.youtube.com/watch?v=7kJLq2rBqRI
```

## File: `data/urls/urls_Tharsis_AI.txt`
```
www.souzatharsis.com
https://www.youtube.com/watch?v=sJE1dE2dulg
```

## File: `docs/Makefile`
```
# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
```

## File: `docs/generate_api_docs.py`
```python
import os
import pkgutil

def generate_api_docs(package_name):
	# Get the package
	package = __import__(package_name)

	# Create the api directory if it doesn't exist
	api_dir = 'docs/source/api'
	os.makedirs(api_dir, exist_ok=True)

	# Generate the main API page
	with open(f'{api_dir}/index.rst', 'w') as f:
		f.write(f"{package_name} API\n")
		f.write("=" * (len(package_name) + 4) + "\n\n")
		f.write(".. toctree::\n")
		f.write("   :maxdepth: 2\n\n")

	# Iterate through all modules in the package
	for _, module_name, _ in pkgutil.walk_packages(package.__path__, package.__name__ + '.'):
		with open(f'{api_dir}/{module_name}.rst', 'w') as f:
			f.write(f"{module_name}\n")
			f.write("=" * len(module_name) + "\n\n")
			f.write(f".. automodule:: {module_name}\n")
			f.write("   :members:\n")
			f.write("   :undoc-members:\n")
			f.write("   :show-inheritance:\n")

		# Add the module to the main API page
		with open(f'{api_dir}/index.rst', 'a') as f:
			f.write(f"   {module_name}\n")

def main():
	generate_api_docs('podcastfy')  # Replace 'podcastfy' with your actual package name

if __name__ == "__main__":
	main()
```

## File: `docs/make.bat`
```
@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
set SOURCEDIR=source
set BUILDDIR=build

%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)

if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
```

## File: `docs/requirements.txt`
```
aiohappyeyeballs==2.4.3 ; python_version >= "3.11" and python_version < "4.0"
aiohttp==3.10.10 ; python_version >= "3.11" and python_version < "4.0"
aiosignal==1.3.1 ; python_version >= "3.11" and python_version < "4.0"
alabaster==1.0.0 ; python_version >= "3.11" and python_version < "4.0"
annotated-types==0.7.0 ; python_version >= "3.11" and python_version < "4.0"
anyio==4.6.2.post1 ; python_version >= "3.11" and python_version < "4.0"
attrs==24.2.0 ; python_version >= "3.11" and python_version < "4.0"
babel==2.16.0 ; python_version >= "3.11" and python_version < "4.0"
beautifulsoup4==4.12.3 ; python_version >= "3.11" and python_version < "4.0"
bleach==6.1.0 ; python_version >= "3.11" and python_version < "4.0"
cachetools==5.5.0 ; python_version >= "3.11" and python_version < "4.0"
certifi==2024.8.30 ; python_version >= "3.11" and python_version < "4.0"
cffi==1.17.1 ; python_version >= "3.11" and python_version < "4.0" and implementation_name == "pypy"
charset-normalizer==3.4.0 ; python_version >= "3.11" and python_version < "4.0"
click==8.1.7 ; python_version >= "3.11" and python_version < "4.0"
colorama==0.4.6 ; python_version >= "3.11" and python_version < "4.0" and (platform_system == "Windows" or sys_platform == "win32")
cython==3.0.11 ; python_version >= "3.11" and python_version < "4.0"
dataclasses-json==0.6.7 ; python_version >= "3.11" and python_version < "4.0"
defusedxml==0.7.1 ; python_version >= "3.11" and python_version < "4.0"
distro==1.9.0 ; python_version >= "3.11" and python_version < "4.0"
docstring-parser==0.16 ; python_version >= "3.11" and python_version < "4.0"
docutils==0.21.2 ; python_version >= "3.11" and python_version < "4.0"
edge-tts==7.2.3 ; python_version >= "3.11" and python_version < "4.0"
elevenlabs==1.9.0 ; python_version >= "3.11" and python_version < "4.0"
fastjsonschema==2.20.0 ; python_version >= "3.11" and python_version < "4.0"
frozenlist==1.4.1 ; python_version >= "3.11" and python_version < "4.0"
fuzzywuzzy==0.18.0 ; python_version >= "3.11" and python_version < "4.0"
google-ai-generativelanguage==0.6.10 ; python_version >= "3.11" and python_version < "4.0"
google-api-core==2.21.0 ; python_version >= "3.11" and python_version < "4.0"
google-api-core[grpc]==2.21.0 ; python_version >= "3.11" and python_version < "4.0"
google-api-python-client==2.149.0 ; python_version >= "3.11" and python_version < "4.0"
google-auth-httplib2==0.2.0 ; python_version >= "3.11" and python_version < "4.0"
google-auth==2.35.0 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-aiplatform==1.70.0 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-bigquery==3.26.0 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-core==2.4.1 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-resource-manager==1.12.5 ; python_version >= "3.11" and python_version < "4.0"
google-cloud-storage==2.18.2 ; python_version >= "3.11" and python_version < "4.0"
google-crc32c==1.6.0 ; python_version >= "3.11" and python_version < "4.0"
google-generativeai==0.8.3 ; python_version >= "3.11" and python_version < "4.0"
google-resumable-media==2.7.2 ; python_version >= "3.11" and python_version < "4.0"
googleapis-common-protos==1.65.0 ; python_version >= "3.11" and python_version < "4.0"
googleapis-common-protos[grpc]==1.65.0 ; python_version >= "3.11" and python_version < "4.0"
greenlet==3.1.1 ; python_version < "3.13" and (platform_machine == "aarch64" or platform_machine == "ppc64le" or platform_machine == "x86_64" or platform_machine == "amd64" or platform_machine == "AMD64" or platform_machine == "win32" or platform_machine == "WIN32") and python_version >= "3.11"
grpc-google-iam-v1==0.13.1 ; python_version >= "3.11" and python_version < "4.0"
grpcio-status==1.66.2 ; python_version >= "3.11" and python_version < "4.0"
grpcio==1.66.2 ; python_version >= "3.11" and python_version < "4.0"
h11==0.14.0 ; python_version >= "3.11" and python_version < "4.0"
httpcore==1.0.6 ; python_version >= "3.11" and python_version < "4.0"
httplib2==0.22.0 ; python_version >= "3.11" and python_version < "4.0"
httpx-sse==0.4.0 ; python_version >= "3.11" and python_version < "4.0"
httpx==0.27.2 ; python_version >= "3.11" and python_version < "4.0"
idna==3.10 ; python_version >= "3.11" and python_version < "4.0"
imagesize==1.4.1 ; python_version >= "3.11" and python_version < "4.0"
jinja2==3.1.4 ; python_version >= "3.11" and python_version < "4.0"
jiter==0.6.1 ; python_version >= "3.11" and python_version < "4.0"
jsonpatch==1.33 ; python_version >= "3.11" and python_version < "4.0"
jsonpointer==3.0.0 ; python_version >= "3.11" and python_version < "4.0"
jsonschema-specifications==2024.10.1 ; python_version >= "3.11" and python_version < "4.0"
jsonschema==4.23.0 ; python_version >= "3.11" and python_version < "4.0"
jupyter-client==8.6.3 ; python_version >= "3.11" and python_version < "4.0"
jupyter-core==5.7.2 ; python_version >= "3.11" and python_version < "4.0"
jupyterlab-pygments==0.3.0 ; python_version >= "3.11" and python_version < "4.0"
langchain-community==0.3.2 ; python_version >= "3.11" and python_version < "4.0"
langchain-core==0.3.10 ; python_version >= "3.11" and python_version < "4.0"
langchain-google-genai==2.0.1 ; python_version >= "3.11" and python_version < "4.0"
langchain-google-vertexai==2.0.5 ; python_version >= "3.11" and python_version < "4.0"
langchain-text-splitters==0.3.0 ; python_version >= "3.11" and python_version < "4.0"
langchain==0.3.3 ; python_version >= "3.11" and python_version < "4.0"
langsmith==0.1.135 ; python_version >= "3.11" and python_version < "4.0"
levenshtein==0.26.0 ; python_version >= "3.11" and python_version < "4.0"
markdown-it-py==3.0.0 ; python_version >= "3.11" and python_version < "4.0"
markupsafe==3.0.1 ; python_version >= "3.11" and python_version < "4.0"
marshmallow==3.22.0 ; python_version >= "3.11" and python_version < "4.0"
mdurl==0.1.2 ; python_version >= "3.11" and python_version < "4.0"
mistune==3.0.2 ; python_version >= "3.11" and python_version < "4.0"
multidict==6.1.0 ; python_version >= "3.11" and python_version < "4.0"
mypy-extensions==1.0.0 ; python_version >= "3.11" and python_version < "4.0"
nbclient==0.10.0 ; python_version >= "3.11" and python_version < "4.0"
nbconvert==7.16.4 ; python_version >= "3.11" and python_version < "4.0"
nbformat==5.10.4 ; python_version >= "3.11" and python_version < "4.0"
nbsphinx==0.9.5 ; python_version >= "3.11" and python_version < "4.0"
numpy==1.26.4 ; python_version >= "3.11" and python_version < "4.0"
openai==1.51.2 ; python_version >= "3.11" and python_version < "4.0"
orjson==3.10.7 ; python_version >= "3.11" and python_version < "4.0"
packaging==24.1 ; python_version >= "3.11" and python_version < "4.0"
pandas==2.2.3 ; python_version >= "3.11" and python_version < "4.0"
pandoc==2.4 ; python_version >= "3.11" and python_version < "4.0"
pandocfilters==1.5.1 ; python_version >= "3.11" and python_version < "4.0"
platformdirs==4.3.6 ; python_version >= "3.11" and python_version < "4.0"
plumbum==1.9.0 ; python_version >= "3.11" and python_version < "4.0"
ply==3.11 ; python_version >= "3.11" and python_version < "4.0"
propcache==0.2.0 ; python_version >= "3.11" and python_version < "4.0"
proto-plus==1.24.0 ; python_version >= "3.11" and python_version < "4.0"
protobuf==5.28.2 ; python_version >= "3.11" and python_version < "4.0"
pyasn1-modules==0.4.1 ; python_version >= "3.11" and python_version < "4.0"
pyasn1==0.6.1 ; python_version >= "3.11" and python_version < "4.0"
pycparser==2.22 ; python_version >= "3.11" and python_version < "4.0" and implementation_name == "pypy"
pydantic-core==2.23.4 ; python_version >= "3.11" and python_version < "4.0"
pydantic-settings==2.5.2 ; python_version >= "3.11" and python_version < "4.0"
pydantic==2.9.2 ; python_version >= "3.11" and python_version < "4.0"
pydub==0.25.1 ; python_version >= "3.11" and python_version < "4.0"
pygments==2.18.0 ; python_version >= "3.11" and python_version < "4.0"
pymupdf==1.24.11 ; python_version >= "3.11" and python_version < "4.0"
pyparsing==3.2.0 ; python_version >= "3.11" and python_version < "4.0"
python-dateutil==2.9.0.post0 ; python_version >= "3.11" and python_version < "4.0"
python-dotenv==1.0.1 ; python_version >= "3.11" and python_version < "4.0"
python-levenshtein==0.26.0 ; python_version >= "3.11" and python_version < "4.0"
pytz==2024.2 ; python_version >= "3.11" and python_version < "4.0"
pywin32==308 ; (platform_system == "Windows" or sys_platform == "win32") and platform_python_implementation != "PyPy" and python_version >= "3.11" and python_version < "4.0"
pyyaml==6.0.2 ; python_version >= "3.11" and python_version < "4.0"
pyzmq==26.2.0 ; python_version >= "3.11" and python_version < "4.0"
rapidfuzz==3.10.0 ; python_version >= "3.11" and python_version < "4.0"
referencing==0.35.1 ; python_version >= "3.11" and python_version < "4.0"
requests-toolbelt==1.0.0 ; python_version >= "3.11" and python_version < "4.0"
requests==2.32.3 ; python_version >= "3.11" and python_version < "4.0"
rich==13.9.2 ; python_version >= "3.11" and python_version < "4.0"
rpds-py==0.20.0 ; python_version >= "3.11" and python_version < "4.0"
rsa==4.9 ; python_version >= "3.11" and python_version < "4"
setuptools==75.1.0 ; python_version >= "3.11" and python_version < "4.0"
shapely==2.0.6 ; python_version >= "3.11" and python_version < "4.0"
shellingham==1.5.4 ; python_version >= "3.11" and python_version < "4.0"
six==1.16.0 ; python_version >= "3.11" and python_version < "4.0"
sniffio==1.3.1 ; python_version >= "3.11" and python_version < "4.0"
snowballstemmer==2.2.0 ; python_version >= "3.11" and python_version < "4.0"
soupsieve==2.6 ; python_version >= "3.11" and python_version < "4.0"
sphinx-autodoc-typehints==2.5.0 ; python_version >= "3.11" and python_version < "4.0"
sphinx-rtd-theme==3.0.1 ; python_version >= "3.11" and python_version < "4.0"
sphinx==8.1.3 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-applehelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-devhelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-htmlhelp==2.1.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-jquery==4.1 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-jsmath==1.0.1 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-qthelp==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sphinxcontrib-serializinghtml==2.0.0 ; python_version >= "3.11" and python_version < "4.0"
sqlalchemy==2.0.35 ; python_version >= "3.11" and python_version < "4.0"
tenacity==8.5.0 ; python_version >= "3.11" and python_version < "4.0"
tinycss2==1.3.0 ; python_version >= "3.11" and python_version < "4.0"
tornado==6.4.1 ; python_version >= "3.11" and python_version < "4.0"
tqdm==4.66.5 ; python_version >= "3.11" and python_version < "4.0"
traitlets==5.14.3 ; python_version >= "3.11" and python_version < "4.0"
typer==0.12.5 ; python_version >= "3.11" and python_version < "4.0"
typing-extensions==4.12.2 ; python_version >= "3.11" and python_version < "4.0"
typing-inspect==0.9.0 ; python_version >= "3.11" and python_version < "4.0"
tzdata==2024.2 ; python_version >= "3.11" and python_version < "4.0"
uritemplate==4.1.1 ; python_version >= "3.11" and python_version < "4.0"
urllib3==2.2.3 ; python_version >= "3.11" and python_version < "4.0"
webencodings==0.5.1 ; python_version >= "3.11" and python_version < "4.0"
websockets==13.1 ; python_version >= "3.11" and python_version < "4.0"
wheel==0.44.0 ; python_version >= "3.11" and python_version < "4.0"
yarl==1.15.2 ; python_version >= "3.11" and python_version < "4.0"
youtube-transcript-api==0.6.2 ; python_version >= "3.11" and python_version < "4.0"
```

## File: `docs/source/README.md`
```markdown
<a name="readme-top"></a>

# Podcastfy.ai 🎙️🤖
[![PyPi Status](https://img.shields.io/pypi/v/podcastfy)](https://pypi.org/project/podcastfy/)
[![Downloads](https://pepy.tech/badge/podcastfy)](https://pepy.tech/project/podcastfy)
[![Issues](https://img.shields.io/github/issues-raw/souzatharsis/podcastfy)](https://github.com/souzatharsis/podcastfy/issues)
[![Documentation Status](https://readthedocs.org/projects/podcastfy/badge/?version=latest)](https://podcastfy.readthedocs.io/en/latest/?badge=latest)
[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
![GitHub Repo stars](https://img.shields.io/github/stars/souzatharsis/podcastfy)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/souzatharsis/podcastfy/blob/main/podcastfy.ipynb)

Transforming Multimodal Content into Captivating Multilingual Audio Conversations with GenAI

https://github.com/user-attachments/assets/f1559e70-9cf9-4576-b48b-87e7dad1dd0b

Podcastfy is an open-source Python package that transforms multi-modal content (text, images) into engaging, multi-lingual audio conversations using GenAI. Input content include websites, PDFs, youtube videos as well as images.

Unlike UI-based tools focused primarily on note-taking or research synthesis (e.g. NotebookLM ❤️), Podcastfy focuses on the programmatic and bespoke generation of engaging, conversational transcripts and audio from a multitude of multi-modal sources enabling customization and scale.

## Audio Examples 🔊
This sample collection is also [available at audio.com](https://audio.com/thatupiso/collections/podcastfy).

### Images

| Image Set | Description | Audio |
|:--|:--|:--|
| <img src="data/images/Senecio.jpeg" alt="Senecio, 1922 (Paul Klee)" width="20%" height="auto"> <img src="data/images/connection.jpg" alt="Connection of Civilizations (2017) by Gheorghe Virtosu " width="21.5%" height="auto"> | Senecio, 1922 (Paul Klee) and Connection of Civilizations (2017) by Gheorghe Virtosu  | [<span style="font-size: 25px;">🔊</span>](https://audio.com/thatupiso/audio/output-file-abstract-art) |
| <img src="data/images/japan_1.jpg" alt="The Great Wave off Kanagawa, 1831 (Hokusai)" width="20%" height="auto"> <img src="data/images/japan2.jpg" alt="Takiyasha the Witch and the Skeleton Spectre, c. 1844 (Kuniyoshi)" width="21.5%" height="auto"> | The Great Wave off Kanagawa, 1831 (Hokusai) and Takiyasha the Witch and the Skeleton Spectre, c. 1844 (Kuniyoshi) | [<span style="font-size: 25px;">🔊</span>](https://audio.com/thatupiso/audio/output-file-japan) |
| <img src="data/images/taylor.png" alt="Taylor Swift" width="28%" height="auto"> <img src="data/images/monalisa.jpeg" alt="Mona Lisa" width="10.5%" height="auto"> | Pop culture icon Taylor Swift and Mona Lisa, 1503 (Leonardo da Vinci) | [<span style="font-size: 25px;">🔊</span>](https://audio.com/thatupiso/audio/taylor-monalisa) |

### Text
| Content Type | Description | Audio | Source |
|--------------|-------------|-------|--------|
| Youtube Video | YCombinator on LLMs | [Audio](https://audio.com/thatupiso/audio/ycombinator-llms) | [YouTube](https://www.youtube.com/watch?v=eBVi_sLaYsc) |
| PDF | Book: Networks, Crowds, and Markets | [Audio](https://audio.com/thatupiso/audio/networks) | book pdf |
| Research Paper | Climate Change in France | [Audio](https://audio.com/thatupiso/audio/agro-paper) | [PDF](./data/pdf/s41598-024-58826-w.pdf) |
| Website | My Personal Website | [Audio](https://audio.com/thatupiso/audio/tharsis) | [Website](https://www.souzatharsis.com) |
| Website + YouTube | My Personal Website + YouTube Video on AI | [Audio](https://audio.com/thatupiso/audio/tharsis-ai) | [Website](https://www.souzatharsis.com), [YouTube](https://www.youtube.com/watch?v=sJE1dE2dulg) |

### Multi-Lingual Text
| Language | Content Type | Description | Audio | Source |
|----------|--------------|-------------|-------|--------|
| French | Website | Agroclimate research information | [Audio](https://audio.com/thatupiso/audio/podcast-fr-agro) | [Website](https://agroclim.inrae.fr/) |
| Portuguese-BR | News Article | Election polls in São Paulo | [Audio](https://audio.com/thatupiso/audio/podcast-thatupiso-br) | [Website](https://noticias.uol.com.br/eleicoes/2024/10/03/nova-pesquisa-datafolha-quem-subiu-e-quem-caiu-na-disputa-de-sp-03-10.htm) |

## Features ✨

- Generate conversational content from multiple-sources and formats (images, websites, YouTube, and PDFs)
- Customizable transcript and audio generation (e.g. style, language, structure, length)
- Create podcasts from pre-existing or edited transcripts
- Support for advanced text-to-speech models (OpenAI, ElevenLabs and Edge)
- Seamless CLI and Python package integration for automated workflows
- Multi-language support for global content creation (experimental!)

## Updates 🚀

### v0.2.2 release
- Podcastfy is now multi-modal! Users can generate audio from images as well as text inputs!
- Added API reference docs and published it to https://podcastfy.readthedocs.io/en/latest/

### v0.2.0 release
- Users can now customize podcast style, structure, and content
- Integration with LangChain for better LLM management

## Quickstart 💻

### Prerequisites
- Python 3.11 or higher
- `$ pip install ffmpeg` (for audio processing)

### Setup
1. Install from PyPI
  `$ pip install podcastfy`

2. Set up your [API keys](config.md)

### Python
```python
from podcastfy.client import generate_podcast

audio_file = generate_podcast(urls=["<url1>", "<url2>"])
```
### CLI
```
python -m podcastfy.client --url <url1> --url <url2>
```
  
## Usage 💻

- [Python Package Quickstart](podcastfy.ipynb)

- [API Reference Manual](https://podcastfy.readthedocs.io/en/latest/podcastfy.html)

- [CLI](cli.md)

Experience Podcastfy with our [HuggingFace](https://huggingface.co/spaces/thatupiso/Podcastfy.ai_demo) 🤗 Spaces app for a simple URL-to-Audio demo. (Note: This UI app is less extensively tested and capable than the Python package.)

## Customization 🔧

Podcastfy offers a range of [Conversation Customization](usage/conversation_custom.md) options to tailor your AI-generated podcasts. Whether you're creating educational content, storytelling experiences, or anything in between, these configuration options allow you to fine-tune your podcast's tone, length, and format.

## Contributing 🤝

We welcome contributions! Please submit [Issues](https://github.com/souzatharsis/podcastfy/issues) or Pull Requests. Feel free to fork the repo and create your own applications. We're excited to learn about your use cases!

## Example Use Cases 🎧🎶

1. **Content Summarization**: Busy professionals can stay informed on industry trends by listening to concise audio summaries of multiple articles, saving time and gaining knowledge efficiently.

2. **Language Localization**: Non-native English speakers can access English content in their preferred language, breaking down language barriers and expanding access to global information.

3. **Website Content Marketing**: Companies can increase engagement by repurposing written website content into audio format, providing visitors with the option to read or listen.

4. **Personal Branding**: Job seekers can create unique audio-based personal presentations from their CV or LinkedIn profile, making a memorable impression on potential employers.

5. **Research Paper Summaries**: Graduate students and researchers can quickly review multiple academic papers by listening to concise audio summaries, speeding up the research process.

6. **Long-form Podcast Summarization**: Podcast enthusiasts with limited time can stay updated on their favorite shows by listening to condensed versions of lengthy episodes.

7. **News Briefings**: Commuters can stay informed about daily news during travel time with personalized audio news briefings compiled from their preferred sources.

8. **Educational Content Creation**: Educators can enhance learning accessibility by providing audio versions of course materials, catering to students with different learning preferences.

9. **Book Summaries**: Avid readers can preview books efficiently through audio summaries, helping them make informed decisions about which books to read in full.

10. **Conference and Event Recaps**: Professionals can stay updated on important industry events they couldn't attend by listening to audio recaps of conference highlights and key takeaways.


## License

This project is licensed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/).

## Contributors

<a href="https://github.com/souzatharsis/podcastfy/graphs/contributors">
  <img alt="contributors" src="https://contrib.rocks/image?repo=souzatharsis/podcastfy"/>
</a>

## Disclaimer

This tool is designed for personal or educational use. Please ensure you have the necessary rights or permissions before using content from external sources for podcast creation. All audio content is AI-generated and it is not intended to clone real-life humans!

<p align="right" style="font-size: 14px; color: #555; margin-top: 20px;">
    <a href="#readme-top" style="text-decoration: none; color: #007bff; font-weight: bold;">
        ↑ Back to Top ↑
    </a>
</p>
```

## File: `docs/source/conf.py`
```python
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'podcastfy'
copyright = '2024, Tharsis T. P. Souza'
author = 'Tharsis T. P. Souza'
release = 'v0.4.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

import os
import sys
sys.path.insert(0, os.path.abspath('../..'))

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "nbsphinx",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
master_doc = "index"
```

## File: `docs/source/index.rst`
```
.. podcastfy documentation master file, created by
   sphinx-quickstart on Sat Oct 12 21:09:23 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Podcastfy.ai API Referece Manual
==========================

This documentation site is focused on the Podcastfy Python package, its classes, functions, and methods.
For additional documentation, see the `Podcastfy <https://github.com/souzatharsis/podcastfy/>`_ GitHub repository.
       
.. toctree::
   :maxdepth: 2
   :caption: API Reference:
   
   podcastfy


Quickstart
----------

Prerequisites
^^^^^^^^^^^^^
- Python 3.11 or higher
- ``$ pip install ffmpeg`` (for audio processing)

Installation
^^^^^^^^^^^^
1. Install from PyPI:
   
   ``$ pip install podcastfy``

2. Set up your `API keys <https://github.com/souzatharsis/podcastfy/blob/main/usage/config.md>`_

Python
^^^^^^
.. code-block:: python

   from podcastfy.client import generate_podcast

   audio_file = generate_podcast(urls=["<url1>", "<url2>"])

CLI
^^^
.. code-block:: bash

   python -m podcastfy.client --url <url1> --url <url2>

Usage
-----

- `Python Package <https://github.com/souzatharsis/podcastfy/blob/main/podcastfy.ipynb>`_

- `CLI <https://github.com/souzatharsis/podcastfy/blob/main/usage/cli.md>`_

Experience Podcastfy with our `HuggingFace <https://huggingface.co/spaces/thatupiso/Podcastfy.ai_demo>`_ 🤗 Spaces app for a simple URL-to-Audio demo. (Note: This UI app is less extensively tested and capable than the Python package.)

Customization
-------------

Podcastfy offers a range of customization options to tailor your AI-generated podcasts:

* Customize podcast `Conversation <https://github.com/souzatharsis/podcastfy/blob/main/usage/conversation_custom.md>`_ (e.g. format, style)
* Choose to run `Local LLMs <https://github.com/souzatharsis/podcastfy/blob/main/usage/local_llm.md>`_ (156+ HuggingFace models)
* Set `System Settings <https://github.com/souzatharsis/podcastfy/blob/main/usage/config_custom.md>`_ (e.g. text-to-speech and output directory settings)


Collaborate
===========

Fork me at https://github.com/souzatharsis/podcastfy.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

Licensed under Apache 2.0
```

## File: `docs/source/modules.rst`
```
podcastfy
=========

.. toctree::
   :maxdepth: 4

   podcastfy
```

## File: `docs/source/podcastfy.content_parser.rst`
```
podcastfy.content\_parser package
=================================

Submodules
----------

podcastfy.content\_parser.content\_extractor module
---------------------------------------------------

.. automodule:: podcastfy.content_parser.content_extractor
   :members:
   :undoc-members:
   :show-inheritance:

podcastfy.content\_parser.pdf\_extractor module
-----------------------------------------------

.. automodule:: podcastfy.content_parser.pdf_extractor
   :members:
   :undoc-members:
   :show-inheritance:

podcastfy.content\_parser.website\_extractor module
---------------------------------------------------

.. automodule:: podcastfy.content_parser.website_extractor
   :members:
   :undoc-members:
   :show-inheritance:

podcastfy.content\_parser.youtube\_transcriber module
-----------------------------------------------------

.. automodule:: podcastfy.content_parser.youtube_transcriber
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: podcastfy.content_parser
   :members:
   :undoc-members:
   :show-inheritance:
```

## File: `docs/source/podcastfy.rst`
```
podcastfy package
=================

Subpackages
-----------

.. toctree::
   :maxdepth: 4

   podcastfy.content_parser

Submodules
----------

podcastfy.client module
-----------------------

.. automodule:: podcastfy.client
   :members:
   :undoc-members:
   :show-inheritance:

podcastfy.content\_generator module
-----------------------------------

.. automodule:: podcastfy.content_generator
   :members:
   :undoc-members:
   :show-inheritance:

podcastfy.text\_to\_speech module
---------------------------------

.. automodule:: podcastfy.text_to_speech
   :members:
   :undoc-members:
   :show-inheritance:

Module contents
---------------

.. automodule:: podcastfy
   :members:
   :undoc-members:
   :show-inheritance:
```

## File: `docs/source/usage/api.md`
```markdown

# Podcastfy REST API Documentation

## Overview

The Podcastfy API allows you to programmatically generate AI podcasts from various input sources. This document outlines the API endpoints and their usage.

## Using cURL with Podcastfy API

### Prerequisites
1. Confirm cURL installation:
```bash
curl --version
```

### API Request Flow
Making a prediction requires two sequential requests:
1. POST request to initiate processing - returns an `EVENT_ID`
2. GET request to fetch results - uses the `EVENT_ID` to fetch results

Between step 1 and 2, there is a delay of 1-3 minutes. We are working on reducing this delay and implementing a way to notify the user when the podcast is ready. Thanks for your patience!

### Basic Request Structure
```bash
# Step 1: POST request to initiate processing
# Make sure to include http:// or https:// in the URL
curl -X POST https://thatupiso-podcastfy-ai-demo.hf.space/gradio_api/call/process_inputs \
  -H "Content-Type: application/json" \
  -d '{
    "data": [
      "text_input",
      "https://yourwebsite.com",
      [],  # pdf_files
      [],  # image_files
      "gemini_key",
      "openai_key",
      "elevenlabs_key",
      2000,  # word_count
      "engaging,fast-paced",  # conversation_style
      "main summarizer",  # roles_person1
      "questioner",  # roles_person2
      "Introduction,Content,Conclusion",  # dialogue_structure
      "PODCASTFY",  # podcast_name
      "YOUR PODCAST",  # podcast_tagline
      "openai",  # tts_model
      0.7,  # creativity_level
      ""  # user_instructions
    ]
  }'

# Step 2: GET request to fetch results
curl -N https://thatupiso-podcastfy-ai-demo.hf.space/gradio_api/call/process_inputs/$EVENT_ID


# Example output result
event: complete
data: [{"path": "/tmp/gradio/bcb143f492b1c9a6dbde512557541e62f090bca083356be0f82c2e12b59af100/podcast_81106b4ca62542f1b209889832a421df.mp3", "url": "https://thatupiso-podcastfy-ai-demo.hf.space/gradio_a/gradio_api/file=/tmp/gradio/bcb143f492b1c9a6dbde512557541e62f090bca083356be0f82c2e12b59af100/podcast_81106b4ca62542f1b209889832a421df.mp3", "size": null, "orig_name": "podcast_81106b4ca62542f1b209889832a421df.mp3", "mime_type": null, "is_stream": false, "meta": {"_type": "gradio.FileData"}}]

```

You can download the file by extending the URL prefix "https://thatupiso-podcastfy-ai-demo.hf.space/gradio_a/gradio_api/file=" with the path to the file in variable `path`. (Note: The variable "url" above has a bug introduced by Gradio, so please ignore it.)

### Parameter Details
| Index | Parameter | Type | Description |
|-------|-----------|------|-------------|
| 0 | text_input | string | Direct text input for podcast generation |
| 1 | urls_input | string | URLs to process (include http:// or https://) |
| 2 | pdf_files | array | List of PDF files to process |
| 3 | image_files | array | List of image files to process |
| 4 | gemini_key | string | Google Gemini API key |
| 5 | openai_key | string | OpenAI API key |
| 6 | elevenlabs_key | string | ElevenLabs API key |
| 7 | word_count | number | Target word count for podcast |
| 8 | conversation_style | string | Conversation style descriptors (e.g. "engaging,fast-paced") |
| 9 | roles_person1 | string | Role of first speaker |
| 10 | roles_person2 | string | Role of second speaker |
| 11 | dialogue_structure | string | Structure of dialogue (e.g. "Introduction,Content,Conclusion") |
| 12 | podcast_name | string | Name of the podcast |
| 13 | podcast_tagline | string | Podcast tagline |
| 14 | tts_model | string | Text-to-speech model ("gemini", "openai", "elevenlabs", or "edge") |
| 15 | creativity_level | number | Level of creativity (0-1) |
| 16 | user_instructions | string | Custom instructions for generation |


## Using Python

### Installation

```bash
pip install gradio_client
```

### Quick Start

```python
from gradio_client import Client, handle_file

client = Client("thatupiso/Podcastfy.ai_demo")
```

### API Endpoints

#### Generate Podcast (`/process_inputs`)

Generates a podcast from provided text, URLs, PDFs, or images.

##### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| text_input | str | Yes | - | Raw text input for podcast generation |
| urls_input | str | Yes | - | Comma-separated URLs to process |
| pdf_files | List[filepath] | Yes | None | List of PDF files to process |
| image_files | List[filepath] | Yes | None | List of image files to process |
| gemini_key | str | No | "" | Google Gemini API key |
| openai_key | str | No | "" | OpenAI API key |
| elevenlabs_key | str | No | "" | ElevenLabs API key |
| word_count | float | No | 2000 | Target word count for podcast |
| conversation_style | str | No | "engaging,fast-paced,enthusiastic" | Conversation style descriptors |
| roles_person1 | str | No | "main summarizer" | Role of first speaker |
| roles_person2 | str | No | "questioner/clarifier" | Role of second speaker |
| dialogue_structure | str | No | "Introduction,Main Content Summary,Conclusion" | Structure of dialogue |
| podcast_name | str | No | "PODCASTFY" | Name of the podcast |
| podcast_tagline | str | No | "YOUR PERSONAL GenAI PODCAST" | Podcast tagline |
| tts_model | Literal['openai', 'elevenlabs', 'edge'] | No | "openai" | Text-to-speech model |
| creativity_level | float | No | 0.7 | Level of creativity (0-1) |
| user_instructions | str | No | "" | Custom instructions for generation |

##### Returns

| Type | Description |
|------|-------------|
| filepath | Path to generated audio file |

##### Example Usage

```python
from gradio_client import Client, handle_file

client = Client("thatupiso/Podcastfy.ai_demo")

# Generate podcast from URL
result = client.predict(
    text_input="",
    urls_input="https://example.com/article",
    pdf_files=[],
    image_files=[],
    gemini_key="your-gemini-key",
    openai_key="your-openai-key",
    word_count=1500,
    conversation_style="casual,informative",
    podcast_name="Tech Talk",
    tts_model="openai",
    creativity_level=0.8
)

print(f"Generated podcast: {result}")
```

### Error Handling

The API will return appropriate error messages for:
- Invalid API keys
- Malformed input
- Failed file processing
- TTS generation errors

### Rate Limits

Please be aware of the rate limits for the underlying services:
- Gemini API
- OpenAI API
- ElevenLabs API

## Notes

- At least one input source (text, URL, PDF, or image) must be provided
- API keys are required for corresponding services
- The generated audio file format is MP3
```

## File: `docs/source/usage/cli.md`
```markdown
## CLI

Podcastfy can be used as a command-line interface (CLI) tool. See below some usage examples.
Please make sure you follow configuration instructions first - [See Setup](README.md#setup).

1. Generate a podcast from URLs (using OpenAI TTS by default):
   ```
   python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2
   ```

2. Generate a podcast from URLs using ElevenLabs TTS:
   ```
   python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2 --tts-model elevenlabs
   ```

3. Generate a podcast from a file containing URLs:
   ```
   python -m podcastfy.client --file path/to/urls.txt
   ```

4. Generate a podcast from an existing transcript file:
   ```
   python -m podcastfy.client --transcript path/to/transcript.txt
   ```

5. Generate only a transcript (without audio) from URLs:
   ```
   python -m podcastfy.client --url https://example.com/article1 --transcript-only
   ```

6. Generate a podcast using a combination of URLs and a file:
   ```
   python -m podcastfy.client --url https://example.com/article1 --file path/to/urls.txt
   ```

7. Generate a podcast from image files:
   ```
   python -m podcastfy.client --image path/to/image1.jpg --image path/to/image2.png
   ```

8. Generate a podcast with a custom conversation configuration:
   ```
   python -m podcastfy.client --url https://example.com/article1 --conversation-config path/to/custom_config.yaml
   ```

9. Generate a podcast from URLs and images:
   ```
   python -m podcastfy.client --url https://example.com/article1 --image path/to/image1.jpg
   ```
   
10. Generate a transcript using a local LLM:
   ```
   python -m podcastfy.client --url https://example.com/article1 --transcript-only --local
   ```

For more information on available options, use:
   ```
   python -m podcastfy.client --help
   ```

11. Generate a podcast from raw text input:
   ```
   python -m podcastfy.client --text "Your raw text content here that you want to convert into a podcast"
   ```
```

## File: `docs/source/usage/config.md`
```markdown
# Podcastfy Configuration

## API keys

The project uses a combination of a `.env` file for managing API keys and sensitive information, and a `config.yaml` file for non-sensitive configuration settings. Follow these steps to set up your configuration:

1. Create a `.env` file in the root directory of the project.
2. Add your API keys and other sensitive information to the `.env` file. For example:

   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```
API Key Requirements:
- `GEMINI_API_KEY`: Required for transcript generation if not using a [local llm](local_llm.md). (get your [free API key](aistudio.google.com/app/apikey))
- `OPENAI_API_KEY` or `ELEVENLABS_API_KEY`: Required for audio generation if not using Microsoft Edge TTS `tts_model=edge`.

Ensure you have the necessary API keys based on your intended usage of Podcastfy.

> [!Note]
> Never share your `.env` file or commit it to version control. It contains sensitive information that should be kept private. The `config.yaml` file can be shared and version-controlled as it doesn't contain sensitive data.

## Example Configurations

Here's a table showing example configurations:

| Configuration | Base LLM | TTS Model | API Keys Required |
|---------------|----------|-----------|-------------------|
| Default | Gemini | OpenAI | GEMINI_API_KEY and OPENAI_API_KEY |
| No API Keys Required | Local LLM | Edge | None |
| Recommended | Gemini | 'gemini' (Google) | GEMINI_API_KEY |

In our experience, ElevenLabs and Google TTS model are the best models in terms quality of audio generation with the latter having an edge over the former due to its multispeaker capability. ElevenLabs is the most expensive but it's easy to setup and offers great customization (voice options and multilingual capability). Google TTS model is cheaper but is limited to English only and requires some extra steps to set up.

## Setting up Google TTS Model

You can use Google TTS model by setting the `tts_model` parameter to `gemini` in `Podcastfy`.

Google TTS model requires a Google Cloud API key, you can use the same API key you are already using for Gemini or create a new one. After you have secured your API Key there are two additional steps in order to use Google Multispeaker TTS model:

- Step 1: You will need to enable the Cloud Text-to-Speech API on the API key.
   - Go to "https://console.cloud.google.com/apis/dashboard"
   - Select your project (or create one by clicking on project list and then on "new project")
   - Click "+ ENABLE APIS AND SERVICES" at the top of the screen
   - Enter "text-to-speech" into the search box
   - Click on "Cloud Text-to-Speech API" and then on "ENABLE"
   - You should be here: "https://console.cloud.google.com/apis/library/texttospeech.googleapis.com?project=..."

- Step 2: You need to add the Cloud Text-to-Speech API permission to the API KEY you're using on the Google Cloud console.

   - Go to https://console.cloud.google.com/apis/credentials
   - Click on whatever key you're using for Gemini
   - Go down to API Restrictions and add the Cloud Text-to-Speech API

Phew!!! That was a lot of steps but you only need to do it once and you might be impressed with the quality of the audio. See [Google TTS](https://cloud.google.com/text-to-speech) for more details. Thank you @mobarski and @evandempsey for the help!

## Conversation Configuration

See [conversation_custom.md](conversation_custom.md) for more details.

## Running Local LLMs

See [local_llm.md](local_llm.md) for more details.

## Optional configuration

The `config.yaml` file in the root directory contains non-sensitive configuration settings. You can modify this file to adjust various parameters such as output directories, text-to-speech settings, and content generation options.

The application will automatically load the environment variables from `.env` and the configuration settings from `config.yaml` when it runs.

See [Configuration](config_custom.md) if you would like to further customize settings.
```

## File: `docs/source/usage/config_custom copy.md`
```markdown
# Podcastfy Advanced Configuration Guide

Podcastfy uses a `config.yaml` file to manage various settings and parameters. This guide explains each configuration option available in the file.



## Content Generator

- `gemini_model`: "gemini-2.5-flash"
  - The Gemini AI model used for content generation.
- `max_output_tokens`: 8192
  - Maximum number of tokens for the output generated by the AI model.
- `temperature`: 1
  - Controls randomness in the AI's output. 0 means deterministic responses. Range for gemini-2.5-flash: 0.0 - 2.0 (default: 1.0) 
- `langchain_tracing_v2`: false
  - Enables LangChain tracing for debugging and monitoring. If true, requires langsmith api key

## Content Extractor

- `youtube_url_patterns`:
  - Patterns to identify YouTube URLs.
  - Current patterns: "youtube.com", "youtu.be"

## Website Extractor

- `markdown_cleaning`:
  - `remove_patterns`:
    - Patterns to remove from extracted markdown content.
    - Current patterns remove image links, hyperlinks, and URLs.

## YouTube Transcriber

- `remove_phrases`:
  - Phrases to remove from YouTube transcriptions.
  - Current phrase: "[music]"

## Logging

- `level`: "INFO"
  - Default logging level.
- `format`: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  - Format string for log messages.


## Website Extractor

- `markdown_cleaning`:
	- `remove_patterns`:
		- Additional patterns to remove from extracted markdown content:
		- '\[.*?\]': Remove square brackets and their contents
		- '\(.*?\)': Remove parentheses and their contents
		- '^\s*[-*]\s': Remove list item markers
		- '^\s*\d+\.\s': Remove numbered list markers
		- '^\s*#+': Remove markdown headers
- `unwanted_tags`:
	- HTML tags to be removed during extraction:
		- 'script', 'style', 'nav', 'footer', 'header', 'aside', 'noscript'
- `user_agent`: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
	- User agent string to be used for web requests
- `timeout`: 10
	- Request timeout in seconds for web scraping


```

## File: `docs/source/usage/config_custom.md`
```markdown
# Podcastfy Advanced Configuration Guide

Podcastfy uses a `config.yaml` file to manage various settings and parameters. This guide explains each configuration option available in the file.

## Customizing the Conversation

See [conversation_custom.md](conversation_custom.md) for more details.

## Output Directories

- `transcripts`: "./data/transcripts"
  - Directory where generated transcripts are saved.
- `audio`: "./data/audio"
  - Directory where generated audio files are saved.

## Text-to-Speech (TTS) Settings

### ElevenLabs TTS

- `default_voices`:
  - `question`: "Chris"
    - Default voice for questions in the podcast.
  - `answer`: "BrittneyHart"
    - Default voice for answers in the podcast.
- `model`: "eleven_multilingual_v2"
  - The ElevenLabs TTS model to use.

### OpenAI TTS

- `default_voices`:
  - `question`: "echo"
    - Default voice for questions using OpenAI TTS.
  - `answer`: "shimmer"
    - Default voice for answers using OpenAI TTS.
- `model`: "tts-1-hd"
  - The OpenAI TTS model to use.

### Edge TTS

- `default_voices`:
  - `question`: "en-US-JennyNeural"
    - Default voice for questions using Edge TTS.
  - `answer`: "en-US-EricNeural"
    - Default voice for answers using Edge TTS.

### General TTS Settings

- `audio_format`: "mp3"
  - Format of the generated audio files.
- `temp_audio_dir`: "data/audio/tmp/"
  - Temporary directory for audio processing.
- `ending_message`: "Tchau!"
  - Message to be appended at the end of the podcast.

## Content Generator

- `gemini_model`: "gemini-2.5-flash"
  - The Gemini AI model used for content generation.
- `system_prompt_file`: "prompt.txt"
  - File containing the system prompt for content generation.
- `max_output_tokens`: 8192
  - Maximum number of tokens for the output generated by the AI model.
- `temperature`: 0
  - Controls randomness in the AI's output. 0 means deterministic responses.
- `langchain_tracing_v2`: true
  - Enables LangChain tracing for debugging and monitoring.

## Content Extractor

- `youtube_url_patterns`:
  - Patterns to identify YouTube URLs.
  - Current patterns: "youtube.com", "youtu.be"

## Website Extractor

- `jina_api_url`: "https://r.jina.ai"
  - URL for the Jina API used in content extraction.
- `markdown_cleaning`:
  - `remove_patterns`:
    - Patterns to remove from extracted markdown content.
    - Current patterns remove image links, hyperlinks, and URLs.

## YouTube Transcriber

- `remove_phrases`:
  - Phrases to remove from YouTube transcriptions.
  - Current phrase: "[music]"

## Logging

- `level`: "INFO"
  - Default logging level.
- `format`: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  - Format string for log messages.

## Main Settings

- `default_tts_model`: "openai"
  - Default Text-to-Speech model to use when not specified.
```

## File: `docs/source/usage/conversation_custom.md`
```markdown
# Podcastfy Conversation Configuration

Podcastfy offers a range of customization options to tailor your AI-generated podcasts. This document outlines how you can adjust parameters such as conversation style, word count, and dialogue structure to suit your specific needs.


## Table of Contents

1. [Parameters](#parameters)
2. [Customization Examples](#customization-examples)
   1. [Academic Debate](#academic-debate)
   2. [Storytelling Adventure](#storytelling-adventure)
3. [Customization Scenarios](#customization-scenarios)
   1. [Using the Python Package](#using-the-python-package)
   2. [Using the CLI](#using-the-cli)
4. [Notes of Caution](#notes-of-caution)


## Conversation Parameters

Podcastfy uses the default conversation configuration stored in [podcastfy/conversation_config.yaml](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy/conversation_config.yaml).

| Parameter | Default Value | Type | Description |
|-----------|---------------|------|-------------|
| word_count | 2000 | int | Target word count for the generated content |
| conversation_style | ["engaging", "fast-paced", "enthusiastic"] | list[str] | Styles to apply to the conversation |
| roles_person1 | "main summarizer" | str | Role of the first speaker |
| roles_person2 | "questioner/clarifier" | str | Role of the second speaker |
| dialogue_structure | ["Introduction", "Main Content Summary", "Conclusion"] | list[str] | Structure of the dialogue |
| podcast_name | "PODCASTFY" | str | Name of the podcast |
| podcast_tagline | "YOUR PERSONAL GenAI PODCAST" | str | Tagline for the podcast |
| output_language | "English" | str | Language of the output |
| engagement_techniques | ["rhetorical questions", "anecdotes", "analogies", "humor"] | list[str] | Techniques to engage the audience |
| creativity | 0 | int | Level of creativity/temperature (0-1) |
| user_instructions | "" | str | Custom instructions to guide the conversation focus and topics |

## Text-to-Speech (TTS) Settings

Podcastfy uses the default TTS configuration stored in [podcastfy/conversation_config.yaml](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy/conversation_config.yaml).

### ElevenLabs TTS

- `default_voices`:
  - `question`: "Chris"
    - Default voice for questions in the podcast.
  - `answer`: "Jessica"
    - Default voice for answers in the podcast.
- `model`: "eleven_multilingual_v2"
  - The ElevenLabs TTS model to use.

### OpenAI TTS

- `default_voices`:
  - `question`: "echo"
    - Default voice for questions using OpenAI TTS.
  - `answer`: "shimmer"
    - Default voice for answers using OpenAI TTS.
- `model`: "tts-1-hd"
  - The OpenAI TTS model to use.

### Edge TTS

- `default_voices`:
  - `question`: "en-US-JennyNeural"
    - Default voice for questions using Edge TTS.
  - `answer`: "en-US-EricNeural"
    - Default voice for answers using Edge TTS.

### General TTS Settings

- `default_tts_model`: "openai"
  - Default text-to-speech model to use.
- `output_directories`:
  - `transcripts`: "./data/transcripts"
    - Directory for storing generated transcripts.
  - `audio`: "./data/audio"
    - Directory for storing generated audio files.
- `audio_format`: "mp3"
  - Format of the generated audio files.
- `temp_audio_dir`: "data/audio/tmp/"
  - Temporary directory for audio processing.
- `ending_message`: "Bye Bye!"
  - Message to be appended at the end of the podcast.

## Customization Examples

These examples demonstrate how conversations can be altered to suit different purposes, from academic rigor to creative storytelling. The comments explain the rationale behind each choice, helping users understand how to tailor the configuration to their specific needs.

### Academic Debate

This configuration transforms the podcast into a formal academic debate, encouraging deep analysis and critical thinking. It's designed for educational content or in-depth discussions on complex topics.

```python
{
    "word_count": 3000,  # Longer to allow for detailed arguments
    "conversation_style": ["formal", "analytical", "critical"],  # Appropriate for academic discourse
    "roles_person1": "thesis presenter",  # Presents the main argument
    "roles_person2": "counterargument provider",  # Challenges the thesis
    "dialogue_structure": [
        "Opening Statements",
        "Thesis Presentation",
        "Counterarguments",
        "Rebuttals",
        "Closing Remarks"
    ],  # Mimics a structured debate format
    "podcast_name": "Scholarly Showdown",
    "podcast_tagline": "Where Ideas Clash and Knowledge Emerges",
    "engagement_techniques": [
        "socratic questioning",
        "historical references",
        "thought experiments"
    ],  # Techniques to stimulate critical thinking
    "creativity": 0  # Low creativity to maintain focus on facts and logic
}
```

### Storytelling Adventure

This configuration turns the podcast into an interactive storytelling experience, engaging the audience in a narrative journey. It's ideal for fiction podcasts or creative content marketing.

```yaml
word_count: 1000  # Shorter to maintain pace and suspense
conversation_style: 
  - narrative
  - suspenseful
  - descriptive  # Creates an immersive story experience
roles_person1: storyteller
roles_person2: audience participator  # Allows for interactive elements
dialogue_structure: 
  - Scene Setting
  - Character Introduction
  - Rising Action
  - Climax
  - Resolution  # Follows classic storytelling structure
podcast_name: Tale Spinners
podcast_tagline: Where Every Episode is an Adventure
engagement_techniques: 
  - cliffhangers
  - vivid imagery
  - audience prompts  # Keeps the audience engaged and coming back
creativity: 0.9 # High creativity for unique and captivating stories
```

## Customization Scenarios

### Using the Python Package

When using the Podcastfy Python package, you can customize the conversation by passing a dictionary to the `conversation_config` parameter:

```python
from podcastfy.client import generate_podcast

custom_config = {
    "word_count": 200,
    "conversation_style": ["casual", "humorous"],
    "podcast_name": "Tech Chuckles",
    "creativity": 0.7
}

generate_podcast(
    urls=["https://example.com/tech-news"],
    conversation_config=custom_config
)
```

### Using the CLI

When using the Podcastfy CLI, you can specify a path to a YAML file containing your custom configuration:

```bash
podcastfy --url https://example.com/tech-news --conversation-config path/to/custom_config.yaml
```

The `custom_config.yaml` file should contain your configuration in YAML format:

```yaml
word_count: 200
conversation_style: 
  - casual
  - humorous
podcast_name: Tech Chuckles
creativity: 0.7
```


## Notes of Caution

- The `word_count` is a target, and the AI may generate more or less than the specified word count. Low word counts are more likely to generate high-level discussions, while high word counts are more likely to generate detailed discussions.
- The `output_language` defines both the language of the transcript and the language of the audio. Here's some relevant information:
  - Bottom-line: non-English transcripts are good enough but non-English audio is work-in-progress.
  - Transcripts are generated using Google's Gemini 1.5 Pro, which supports 100+ languages by default.
  - Audio is generated using `openai` (default), `elevenlabs`, `gemini`,or `edge` TTS models. 
    - The `gemini`(Google) TTS model is English only.
    - The `openai` TTS model supports multiple languages automatically, however non-English voices still present sub-par quality in my experience.
    - The `elevenlabs` TTS model has English voices by default, in order to use a non-English voice you would need to download a custom voice for the target language in your `elevenlabs` account settings and then set the `text_to_speech.elevenlabs.default_voices` parameters to the voice you want to use in the [config.yaml file](https://github.com/pedroslopez/podcastfy/blob/main/podcastfy/config.yaml) (this config file is only available in the source code of the project, not in the pip package, hence if you are using the pip package you will not be able to change the ElevenLabs voice). For more information on ElevenLabs voices, visit [ElevenLabs Voice Library](https://elevenlabs.io/voice-library)
```

## File: `docs/source/usage/docker.md`
```markdown
# Docker Setup Guide for Podcastfy

This guide explains how to use Docker to run Podcastfy in your local environment or for development.

## Prerequisites

- Docker installed on your system [1]
- Docker Compose [1]
- API keys [2]

[1] See Appendix A for detailed installation instructions.
[2] See [config.md](https://github.com/souzatharsis/podcastfy/blob/main/usage/config.md) for more details.

## Available Images

Podcastfy provides pre-built Docker images through GitHub Container Registry (ghcr.io):

1. **Production Image**: `ghcr.io/souzatharsis/podcastfy:latest`
   - Contains the latest PyPI release
   - Recommended for production use

2. **Development Image**: `ghcr.io/souzatharsis/podcastfy:dev`
   - Includes development tools and dependencies
   - Used for contributing and development

## Deployment

### Quick Deployment Steps

1. Create a new directory and navigate to it:
```bash
mkdir -p /path/to/podcastfy
cd /path/to/podcastfy
```

2. Create a `.env` file with your API keys (see [config.md](https://github.com/souzatharsis/podcastfy/blob/main/usage/config.md) for more details):
```plaintext
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key  # Optional: only needed for OpenAI TTS
```

3. Create a `docker-compose.yml`:
```yaml
version: '3.8'

services:
  podcastfy:
    image: ghcr.io/souzatharsis/podcastfy:latest
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "8000:8000"
    command: python3 -m podcastfy.server
    healthcheck:
      test: ["CMD", "python3", "-c", "import podcastfy"]
      interval: 30s
      timeout: 10s
      retries: 3
```

4. Pull and start the container:
```bash
docker pull ghcr.io/souzatharsis/podcastfy:latest
docker-compose up podcastfy
```

The service will be available at `http://localhost:8000`

### Directory Structure
```
/path/to/podcastfy/
├── .env                  # Environment variables
└── docker-compose.yml    # Docker Compose configuration
```

## Development Setup

### Using Pre-built Development Image

1. Pull the development image:
```bash
docker pull ghcr.io/souzatharsis/podcastfy:dev
```

2. Clone the repository and start development environment:
```bash
git clone https://github.com/souzatharsis/podcastfy.git
cd podcastfy
docker-compose up podcastfy-dev
```

### Building Locally

Alternatively, you can build the images locally:
```bash
# Build production image
docker-compose build podcastfy

# Build development image
docker-compose build podcastfy-dev
```

## Running Tests

Run the test suite using:
```bash
docker-compose up test
```

This will run tests in parallel using pytest-xdist.

## Environment Variables

Required environment variables:
- `GEMINI_API_KEY` - Your Google Gemini API key
- `OPENAI_API_KEY` - Your OpenAI API key (optional: only needed for OpenAI TTS)

## Container Details

### Production Container
- Based on Ubuntu 24.04
- Installs Podcastfy from PyPI
- Includes FFmpeg for audio processing
- Runs in a Python virtual environment
- Exposed port: 8000

### Development Container
- Based on Ubuntu 24.04
- Includes development tools (flake8, pytest)
- Mounts local code for live development
- Runs in editable mode (`pip install -e .`)
- Exposed port: 8001

## Continuous Integration

The Docker images are automatically:
- Built and tested on every push to main branch
- Built and tested for all pull requests
- Published to GitHub Container Registry
- Tagged with version numbers for releases (v*.*.*)

## Health Checks

All services include health checks that:
- Run every 30 seconds
- Verify Podcastfy can be imported
- Timeout after 10 seconds
- Retry up to 3 times

## Common Commands

```bash
# Pull latest production image
docker pull ghcr.io/souzatharsis/podcastfy:latest

# Pull development image
docker pull ghcr.io/souzatharsis/podcastfy:dev

# Start production service
docker-compose up podcastfy

# Start development environment
docker-compose up podcastfy-dev

# Run tests
docker-compose up test

# Build images locally
docker-compose build

# View logs
docker-compose logs

# Stop all containers
docker-compose down
```

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your `.env` file exists and contains valid API keys
   - Check if the environment variables are properly passed to the container

2. **Port Conflicts**
   - Ensure ports 8000 (production) and 8001 (development) are available
   - Modify the port mappings in `docker-compose.yml` if needed

3. **Volume Mounting Issues (Development)**
   - Verify the correct path to your local code
   - Check permissions on the mounted directories

4. **Image Pull Issues**
   - Ensure you have access to the GitHub Container Registry
   - If you see "unauthorized" errors, the image might be private
   - Try authenticating with GitHub: `docker login ghcr.io -u YOUR_GITHUB_USERNAME`

### Verifying Installation

You can verify your installation by checking if the package can be imported:
```bash
# Check production version
docker run --rm ghcr.io/souzatharsis/podcastfy:latest python3 -c "import podcastfy"

# Check development setup
docker-compose exec podcastfy-dev python3 -c "import podcastfy"
```

## System Requirements

Minimum requirements:
- Docker Engine 20.10.0 or later
- Docker Compose 2.0.0 or later
- Sufficient disk space for Ubuntu base image (~400MB)
- Additional space for Python packages and FFmpeg

## Support

If you encounter any issues:
1. Check the container logs: `docker-compose logs`
2. Verify all prerequisites are installed
3. Ensure all required environment variables are set
4. Open an issue on the [Podcastfy GitHub repository](https://github.com/souzatharsis/podcastfy/issues)

## Appendix A: Detailed Installation Guide

### Installing Docker

#### Windows
1. Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - For Windows 10/11 Pro, Enterprise, or Education: Enable WSL 2 and Hyper-V
   - For Windows 10 Home: Enable WSL 2
2. After installation, start Docker Desktop
3. Verify installation:
```bash
docker --version
```

#### macOS
1. Download and install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - For Intel chip: Download Intel package
   - For Apple chip: Download Apple Silicon package
2. After installation, start Docker Desktop
3. Verify installation:
```bash
docker --version
```

#### Ubuntu/Debian
```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install prerequisites
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Add your user to docker group (optional, to run docker without sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
```

#### Other Linux Distributions
- [CentOS](https://docs.docker.com/engine/install/centos/)
- [Fedora](https://docs.docker.com/engine/install/fedora/)
- [RHEL](https://docs.docker.com/engine/install/rhel/)

### Installing Docker Compose

Docker Compose is included with Docker Desktop for Windows and macOS. For Linux:

```bash
# Download the current stable release
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker-compose --version
```

### Post-Installation Steps

1. Verify Docker is running:
```bash
docker run hello-world
```

2. Configure Docker to start on boot (Linux only):
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

## Appendix B: Getting API Keys

### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create or sign in to your Google account
3. Click "Create API Key"
4. Copy and save your API key

### OpenAI API Key
You only need an OpenAI API key if you want to use the OpenAI Text-to-Speech model.
1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create or sign in to your OpenAI account
3. Click "Create new secret key"
4. Copy and save your API key

## Appendix C: Installation Validation

After installing all prerequisites, verify everything is set up correctly:

```bash
# Check Docker version
docker --version

# Check Docker Compose version
docker-compose --version

# Verify Docker daemon is running
docker ps

# Test Docker functionality
docker run hello-world
```
```

## File: `docs/source/usage/how-to.md`
```markdown
# How to

All assume you have podcastfy installed and running.

## Table of Contents

- [Custom LLM Support](#custom-llm-support)
- [Running Local LLMs](#running-local-llms)
- [How to use your own voice in audio podcasts](#how-to-use-your-own-voice-in-audio-podcasts)
- [How to customize the conversation](#how-to-customize-the-conversation)
- [How to generate multilingual content](#how-to-generate-multilingual-content)
- [How to steer the conversation](#how-to-steer-the-conversation)


## Custom LLM Support

Podcastfy offers a range of LLM models for generating transcripts including OpenAI, Anthropic, Google as well as local LLM models.

### Cloud-based LLMs

By default, Podcastfy uses Google's `gemini-2.5-flash` model. To select a particular cloud-based LLM model, users can pass the `llm_model_name` and `api_key_label` parameters to the `generate_podcast` function.

For example, to use OpenAI's `gpt-4-turbo` model, users can pass `llm_model_name="gpt-4-turbo"` and `api_key_label="OPENAI_API_KEY"`.

```python
audio_file = generate_podcast(
    urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
    llm_model_name="gpt-4-turbo",
    api_key_label="OPENAI_API_KEY"
)
```

Remember to have the correct API key label and value in your environment variables (`.env` file).

### Running Local LLMs

See [local_llm.md](local_llm.md) for more details.

## How to use your own voice in audio podcasts

You just need to use ElevenLabs TSS backend and pass a custom config to use your voice instead of podcastfy's default:
  
1. Create elevenlabs account, get and [set up](https://github.com/souzatharsis/podcastfy/blob/main/usage/config.md) eleven labs API KEY

2. Clone your voice on elevenlabs website (let's say its name is 'Robbert')

4. Create custom conversation config (let's call it custom_config.yaml) to use your voice name instead of the default as described [here](https://github.com/souzatharsis/podcastfy/blob/main/usage/conversation_custom.md#text-to-speech-tts-settings). Set either question or answer voice below to 'Robbert' in elevenlabs > default_voices.

6. Run podcastfy with tts-model param as elevenlabs

CLI
   ```
   python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2 --tts-model elevenlabs --conversation-config path/to/custom_config.yaml
   ```
For Python example, checkout Customization section at [python notebook](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy.ipynb).

## How to customize the conversation

You can customize the conversation by passing a custom [conversation_config.yaml](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy/conversation_config.yaml) file to the CLI: 

```
python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2 --tts-model elevenlabs --conversation-config path/to/custom_config.yaml
```

You can also pass a dictionary with the custom config to the python interface generate_podcast function:

```python
from podcastfy.client import generate_podcast

custom_config = {
    "word_count": 200,
    "conversation_style": ["casual", "humorous"],
    "podcast_name": "Tech Chuckles",
    "creativity": 0.7
}

generate_podcast(
    urls=["https://example.com/tech-news"],
    conversation_config=custom_config
)
```
For more details, checkout [conversation_custom.md](https://github.com/souzatharsis/podcastfy/blob/main/usage/conversation_custom.md).

## How to generate multilingual content

In order to generate transcripts in a target language, simply set `output_language` = your target language. See [How to customize the conversation](#how-to-customize-the-conversation) on how to pass custom configuration to podcastfy. Set --transcript-only to get only the transcript without audio generation.

In order to generation audio, you can simply use openai TTS model which by default is multilingual. However, in my experience OpenAI's TTS multilingual quality is subpar. Instead, consdier using elevenlabs backend. See [How to use your own voice in audio podcasts](#how-to-use-your-own-voice-in-audio-podcasts) but instead of using your own voice you should download and set a voice in your target language for it to work.

Sample audio:
- [French](https://github.com/souzatharsis/podcastfy/blob/main/data/audio/podcast_FR_AGRO.mp3)
- [Portugue-BR](https://github.com/souzatharsis/podcastfy/blob/main/data/audio/podcast_thatupiso_BR.mp3)

The PT-BR audio actually uses my own cloned voice as AI Host 2.


## How to steer the conversation

You can guide the conversation focus and topics by setting the `user_instructions` parameter in your custom configuration. This allows you to provide specific instructions to the AI hosts about what aspects they should emphasize or explore.

Things to try:
- Focus on a specific topic (e.g. "Focus the discussion on key capabilities and limitations of modern AI models")
- Target a specific audience (e.g. "Explain concepts in a way that's accessible to someone new to Computer Science")

For example, using the CLI with a custom YAML:

```yaml
user_instructions: "Make connections with quantum computing"
```

```
python -m podcastfy.client --url https://en.wikipedia.org/wiki/Artificial_intelligence --conversation-config path/to/custom_config.yaml
```




```

## File: `docs/source/usage/license-guide.md`
```markdown
Podcastfy is licensed under Apache 2.0. The Apache License 2.0 is a permissive free software license that allows you to use this sotfware for both non-commercial or commercial purposes. 
Please review the [License](../LICENSE) in order to know your obligations. 
here is a set of steps I will list without any warranty or liability:

1. Include a copy of the license in your project:

In your project root, create a NOTICE.txt or THIRD_PARTY_LICENSES.txt file and include the content from the file [NOTICE](../NOTICE)

2. Add attribution in your README.md:
```markdown
## Acknowledgments

This project includes code from Podcastfy(https://github.com/souzatharsis/podcastfy/), licensed under the Apache License 2.0.
```

3. Keep the original copyright notices in any files you copy/modify

4. If you modified the code, indicate your changes:
```python
# Modified from original source: [Podcastfy](https://github.com/souzatharsis/podcastfy/)
# Changes made:
# - Added feature X
# - Modified function Y
# - Removed component Z
```

Important points:
- You don't need to use the same license for your project
- You must preserve all copyright, patent, trademark notices
- State significant modifications you made
- Include the original Apache 2.0 license text
- Attribution should be clear and reasonable
```

## File: `docs/source/usage/local_llm.md`
```markdown
# Local LLM Support

Running local LLMs can offer several advantages such as:
- Enhanced privacy and data security
- Cost control and no API rate limits
- Greater customization and fine-tuning options
- Reduced vendor lock-in

We enable serving local LLMs with [llamafile](https://github.com/Mozilla-Ocho/llamafile). In the API, local LLM support is available through the `is_local` parameter. If `is_local=True`, then a local (llamafile) LLM model is used to generate the podcast transcript. Llamafiles of LLM models can be found on [HuggingFace, which today offers 156+ models](https://huggingface.co/models?library=llamafile).

All you need to do is:

1. Download a llamafile from HuggingFace
2. Make the file executable
3. Run the file

Here's a simple bash script that shows all 3 setup steps for running TinyLlama-1.1B locally:

```bash
# Download a llamafile from HuggingFace
wget https://huggingface.co/jartine/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile

# Make the file executable. On Windows, instead just rename the file to end in ".exe".
chmod +x TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile

# Start the model server. Listens at http://localhost:8080 by default.
./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile --server --nobrowser
```

Now you can use the local LLM to generate a podcast transcript (or audio) by setting the `is_local` parameter to `True`.

## Python API

```python
from podcastfy import generate_podcast

# Generate a tech debate podcast about artificial intelligence
generate_podcast(
    urls=["www.souzatharsis.com"],
    is_local=True  # Using a local LLM
)
```

## CLI

To use a local LLM model via the command-line interface, you can use the `--local` or `-l` flag. Here's an example of how to generate a transcript using a local LLM:

```bash
python -m podcastfy.client --url https://example.com/article1 --transcript-only --local
```

## Notes of caution

When using local LLM models versus widely known private large language models:

1. Performance: Local LLMs often have lower performance compared to large private models due to size and training limitations.

2. Resource requirements: Running local LLMs can be computationally intensive, requiring significant CPU/GPU resources.

3. Limited capabilities: Local models may struggle with complex tasks or specialized knowledge that larger models handle well.

5. Reduced multimodal abilities: Local LLMs will be assumed to be text-only capable

6. Potential instability: Local models may produce less consistent or stable outputs compared to well-tested private models oftentimes producing transcripts that cannot be used for podcast generation (TTS) out-of-the-box

7. Limited context window: Local models often have smaller context windows, limiting their ability to process long inputs.

Always evaluate the trade-offs between using local LLMs and private models based on your specific use case and requirements. We highly recommend extensively testing your local LLM before productionizing an end-to-end podcast generation and/or manually checking the transcript before passing to TTS model.
```

## File: `paper/paper.bib`
```
@misc{langchain2024,
	title = {LangChain: Building applications with LLMs through composability},
	author = {{LangChain}},
	year = {2024},
	url = {https://www.langchain.com/},
	note = {Accessed: 2024-01-11}
}


@article{johnson2023adaptive,
  author = {Johnson, L. and Smith, K.},
  title = {Adaptive user interfaces for accessibility across digital content modalities},
  journal = {Journal of Multimodal Accessibility},
  year = {2023},
  volume = {17},
  number = {2},
  pages = {43-58},
  url = {https://link.springer.com/article/10.1007/s12193-023-00427-4}
}

@article{chen2023digital,
  author = {Chen, R. and Wu, Y.},
  title = {Digital accessibility tools for multimodal content processing: A systematic review},
  journal = {Digital Transformation Review},
  year = {2023},
  volume = {5},
  number = {3},
  pages = {91-109}
}

@article{mccune2023accessibility,
  author = {McCune, B. and Brown, L.},
  title = {Accessibility of digital information: Standards, frameworks, and tools related to information literacy and information technology},
  journal = {Journal of Information Literacy and Accessibility},
  year = {2023},
  volume = {9},
  number = {4},
  pages = {112-129}
}

@incollection{marcus2019design,
  author = {Marcus, A. and Zhang, T.},
  title = {Design for multimodal human-computer interaction},
  booktitle = {Lecture Notes in Computer Science},
  year = {2019},
  volume = {1157},
  pages = {160-176},
  url = {https://link.springer.com/chapter/10.1007/978-3-319-52162-6_18}
}

@article{peterson2023web,
  author = {Peterson, L. and Allen, J.},
  title = {Web accessibility and multimodal digital engagement},
  journal = {Technology Accessibility Journal},
  year = {2023},
  volume = {12},
  number = {1},
  pages = {23-34}
}

@article{gupta2023advances,
  author = {Gupta, S. and Lee, A.},
  title = {Advances in adaptive user interfaces for enhanced accessibility},
  journal = {Journal of Accessibility and User Experience},
  year = {2023},
  volume = {14},
  number = {3},
  pages = {203-215}
}



@article{brown2020language,
  title={Language models are few-shot learners},
  author={Brown, Tom and others},
  journal={Advances in Neural Information Processing Systems},
  year={2020}
}

@article{wang2017tacotron,
  title={Tacotron: Towards end-to-end speech synthesis},
  author={Wang, Yuxuan and others},
  journal={arXiv preprint arXiv:1703.10135},
  year={2017}
}

@article{chen2020making,
  title={Making content more accessible with multimodal transformations},
  author={Chen, Howard and others},
  journal={ACM Transactions on Accessible Computing},
  year={2020}
}

@article{yang2021multimodal,
  title={Multimodal learning meets content transformation},
  author={Yang, Sarah and others},
  journal={Conference on Human Factors in Computing Systems},
  year={2021}
}

@article{wu2023survey,
  title={A survey of AI-powered content transformation tools},
  author={Wu, Jennifer and others},
  journal={Digital Scholarship in the Humanities},
  year={2023}
}

@article{liu2023survey,
  title={A survey on multimodal large language models},
  author={Liu, Shukang and others},
  journal={arXiv preprint arXiv:2306.13549},
  year={2023}
}

@article{touvron2023llama,
  title={Llama 2: Open foundation language models},
  author={Touvron, Hugo and others},
  journal={arXiv preprint arXiv:2307.09288},
  year={2023}
}

@article{shen2018natural,
  title={Natural TTS synthesis by conditioning WaveNet on mel spectrogram predictions},
  author={Shen, Jonathan and others},
  journal={IEEE International Conference on Acoustics, Speech and Signal Processing},
  year={2018}
}

@article{johnson2017google,
  title={Google's multilingual neural machine translation system},
  author={Johnson, Melvin and others},
  journal={Transactions of the Association for Computational Linguistics},
  year={2017}
}

@article{wu2023privacy,
  title={Privacy-preserving language models: A survey},
  author={Wu, Michael and others},
  journal={arXiv preprint arXiv:2309.00035},
  year={2023}
}

@article{zhao2023automated,
  title={Automated content transformation in the era of large language models},
  author={Zhao, Linda and others},
  journal={Computer},
  year={2023}
}

@article{bano2022systematic,
  title={A systematic review of AI in education},
  author={Bano, Muneera and others},
  journal={IEEE Access},
  year={2022}
}

@article{park2022content,
  title={Content creation and distribution in the AI era},
  author={Park, David and others},
  journal={Digital Journalism},
  year={2022}
}

@article{zhang2023survey,
  title={A survey of AI-powered accessibility tools},
  author={Zhang, Kevin and others},
  journal={ACM Computing Surveys},
  year={2023}
}

```

## File: `paper/paper.md`
```markdown
---
title: 'When Content Speaks Volumes: Podcastfy — An Open Source Python Package Bridging Multimodal Data and Conversational Audio with GenAI'
tags:
  - Python
  - generative AI
  - GenAI
  - text-to-speech
  - large language models
  - content transformation
  - accessibility
authors:
  - name: Tharsis T. P. Souza
    orcid: 0000-0003-3260-9526
    affiliation: "1, 2"
affiliations:
  - name: Columbia University in the City of New York
    index: 1
  - name: Instituto Federal de Educacao, Ciencia e Tecnologia do Sul de Minas (IFSULDEMINAS)
    index: 2
date: 11/03/2024
bibliography: paper.bib
---

# Abstract

`Podcastfy` is an open-source Python framework that programmatically transforms multisourced, multimodal content into multilingual, natural-sounding audio conversations using generative AI. By converting various types of digital content - including images, websites, YouTube videos, and PDFs - into conversational audio formats, `Podcastfy` enhances accessibility, engagement, and usability for a wide range of users. As an open-source project, `Podcastfy` benefits from continuous community-driven improvements, enhancing its adaptability to evolving user requirements and accessibility standards.

# Statement of Need

The rapid expansion of digital content across various formats has intensified the need for tools capable of converting diverse information into accessible and digestible forms [@johnson2023adaptive; @chen2023digital; @mccune2023accessibility]. Existing solutions often fall short due to their proprietary nature, limited multimodal support, or inadequate accessibility features [@marcus2019design; @peterson2023web; @gupta2023advances].

`Podcastfy` addresses this gap with an open-source solution that supports multimodal input processing and generates natural-sounding, summarized conversational content. Leveraging advances in large language models (LLMs) and text-to-speech (TTS) synthesis, `Podcastfy` aims to benefit a diverse group of users — including content creators, educators, researchers, and accessibility advocates — by providing a customizable solution that transforms digital content into multilingual textual and auditory formats, enhancing accessibility and engagement.

# Features

- Generate conversational content from multiple sources and formats (images, websites, YouTube, and PDFs).
- Customize transcript and audio generation (e.g., style, language, structure, length).
- Create podcasts from pre-existing or edited transcripts.
- Leverage cloud-based and local LLMs for transcript generation (increased privacy and control).
- Integrate with advanced text-to-speech models (OpenAI, ElevenLabs, and Microsoft Edge).
- Provide multi-language support for global content creation and enhanced accessibility.
- Integrate seamlessly with CLI and Python packages for automated workflows.

See [audio samples](https://github.com/souzatharsis/podcastfy?tab=readme-ov-file#audio-examples-).

# Use Cases

`Podcastfy` is designed to serve a wide range of applications, including:

- **Content Creators** can use `Podcastfy` to convert blog posts, articles, or multimedia content into podcast-style audio, enabling them to reach broader audiences. By transforming content into an audio format, creators can cater to users who prefer listening over reading.

- **Educators** can transform lecture notes, presentations, and visual materials into audio conversations, making educational content more accessible to students with different learning preferences. This is particularly beneficial for students with visual impairments or those who have difficulty processing written information.

- **Researchers** can convert research papers, visual data, and technical content into conversational audio. This makes it easier for a wider audience, including those with disabilities, to consume and understand complex scientific information. Researchers can also create audio summaries of their work to enhance accessibility.

- **Accessibility Advocates** can use `Podcastfy` to promote digital accessibility by providing a tool that converts multimodal content into auditory formats. This helps individuals with visual impairments, dyslexia, or other disabilities that make it challenging to consume written or visual content.


# Implementation and Architecture

`Podcastfy` implements a modular architecture designed for flexibility and extensibility through five main components, as shown in Figure 1.


1. **Client Interface**
   - Provides both CLI (Command-Line Interface) and API interfaces.
   - Coordinates the workflow between processing layers.
   - Implements a unified interface for podcast generation through the `generate_podcast()` method.

2. **Configuration Management**
   - Offers extensive customization options through a dedicated module.
   - Manages system settings and user preferences, such as podcast name, language, style, and structure.
   - Controls the behavior of all processing layers.

3. **Content Extraction Layer**
   - Extracts content from various sources, including websites, PDFs, and YouTube videos.
   - The `ContentExtractor` class coordinates three specialized extractors:
     - `PDFExtractor`: Handles PDF document processing.
     - `WebsiteExtractor`: Manages website content extraction.
     - `YouTubeTranscriber`: Processes YouTube video content.
   - Serves as the entry point for all input types, providing standardized text output to the transcript generator.

4. **LLM-based Transcript Generation Layer**
   - Uses large language models to generate natural-sounding conversations from extracted content.
   - The `ContentGenerator` class manages conversation generation using different LLM backends:
     - Integrates with LangChain to implement prompt management and common LLM access through the `BaseChatModel` interface.
     - Supports both local (`LlamaFile`) and cloud-based models.
     - Uses `ChatGoogleGenerativeAI` for cloud-based LLM services.
   - Allows customization of conversation style, roles, and dialogue structure.
   - Outputs structured conversations in text format.

5. **Text-to-Speech (TTS) Layer**
   - Converts input transcripts into audio using various TTS models.
   - The `TextToSpeech` class implements a factory pattern:
     - The `TTSFactory` creates appropriate providers based on configuration.
     - Supports multiple backends (OpenAI, ElevenLabs, and Microsoft Edge) through the `TTSProvider` interface.
   - Produces the final podcast audio output.

![Podcastfy's simplified architecture and workflow diagram showing the main components and their interactions.](podcastfy.png){width=80%}

The modular architecture enables independent development and maintenance of each component. This pipeline design ensures a clean separation of concerns while maintaining seamless data transformation between stages. This modular approach also facilitates easy updates and extensions to individual components without affecting the rest of the system.

The framework is offered as a Python package, with a command-line interface as well as a REST API, making it accessible to users with different technical backgrounds and requirements.


# Quick Start

## Prerequisites
- Python 3.11 or higher
- `$ pip install ffmpeg` (for audio processing)

## Setup
1. Install from PyPI
  `$ pip install podcastfy`

2. Set up [API keys](config.md)

## Python
```python
from podcastfy.client import generate_podcast

audio_file = generate_podcast(urls=["<url1>", "<url2>"])
```
## CLI
```
python -m podcastfy.client --url <url1> --url <url2>
```


# Customization Examples

`Podcastfy` offers various customization options that make it versatile for different types of content transformation. To accomplish that, we leverage LangChain's [@langchain2024] prompt management capabilities to dynamically construct prompts for the LLM, adjusting conversation characteristics such as style, roles, and dialogue structure. Below are some examples that demonstrate its capabilities.

## Academic Debate

The following Python code demonstrates how to configure `Podcastfy` for an academic debate:

```python
from podcastfy import generate_podcast

debate_config = {
    "conversation_style": ["formal", "debate"],
    "roles_person1": "main presenter",
    "roles_person2": "opposing viewpoint", 
    "dialogue_structure": ["Introduction", "Argument Presentation", "Counterarguments", "Conclusion"]
}

generate_podcast(
    urls=["PATH/TO/academic-article.pdf"],
    conversation_config=debate_config
)
```

In this example, the roles are set to "main presenter" and "opposing viewpoint" to simulate an academic debate between two speakers on a chosen topic. This approach is especially useful for educational content that aims to present multiple perspectives on a topic. The output is structured with clear sections such as introduction, argument presentation, counterarguments, and conclusion, allowing listeners to follow complex ideas easily.


## Technical Tutorial

In this example, the configuration is optimized for creating technical tutorial content. 

```python
tutorial_config = {
    "word_count": 2500,
    "conversation_style": ["instructional", "step-by-step"],
    "roles_person1": "expert developer",
    "roles_person2": "learning developer",
    "dialogue_structure": [
        "Concept Introduction",
        "Technical Background",
        "Implementation Steps",
        "Common Pitfalls",
        "Best Practices"
    ],
    "engagement_techniques": [
        "code examples",
        "real-world applications",
        "troubleshooting tips"
    ],
    "creativity": 0.4
}

generate_podcast(
    urls=["https://tech-blog.com/tutorial"],
    conversation_config=tutorial_config
)
```


The roles are set to "expert developer" and "learning developer" to create a natural teaching dynamic. The dialogue structure follows a logical progression from concept introduction through implementation and best practices. The engagement_techniques parameter ensures the content remains practical and applicable by incorporating code examples, real-world applications, and troubleshooting guidance. A moderate creativity setting (0.4) maintains technical accuracy while allowing for engaging explanations and examples.


## Storytelling Adventure

The following Python code demonstrates how to generate a storytelling podcast:

```python
from podcastfy import generate_podcast

story_config = {
    "conversation_style": ["adventurous", "narrative"],
    "creativity": 1.0,
    "roles_person1": "narrator", 
    "roles_person2": "character",
    "dialogue_structure": ["Introduction", "Adventure Begins", "Challenges", "Resolution"]
}

generate_podcast(
    urls=["SAMPLE/WWW.URL.COM"],
    conversation_config=story_config
)
```

In this example, `Podcastfy` creates an engaging story by assigning roles like "narrator" and "character" and adjusting the creativity parameter for richer descriptions. Using this configuration, `Podcastfy` can generate engaging narrative content. By adjusting the creativity parameter, `Podcastfy` can create a story involving multiple characters, unexpected plot twists, and rich descriptions.

## Additional Examples

### Daily News Briefing
```python
news_config = {
    "word_count": 1500,
    "conversation_style": ["concise", "informative"],
    "podcast_name": "Morning Briefing",
    "dialogue_structure": [
        "Headlines",
        "Key Stories",
        "Market Update",
        "Weather"
    ],
    "roles_person1": "news anchor",
    "roles_person2": "field reporter",
    "creativity": 0.3
}

generate_podcast(
    urls=[
        "https://news-source.com/headlines",
        "https://market-updates.com/today"
    ],
    conversation_config=news_config
)
```

### Language Learning Content
```python
language_config = {
    "output_language": "Spanish",
    "word_count": 1000,
    "conversation_style": ["educational", "casual"],
    "engagement_techniques": [
        "vocabulary explanations",
        "cultural context",
        "pronunciation tips"
    ],
    "roles_person1": "language teacher",
    "roles_person2": "curious student",
    "creativity": 0.6
}

generate_podcast(
    urls=["https://spanish-content.com/article"],
    conversation_config=language_config
)
```


## Working with Podcastfy Modules

`Podcastfy`'s components are designed to work independently, allowing flexibility in updating or extending each module. The data flows from the `ContentExtractor` module to `ContentGenerator` and finally to the `TexttoSpeech` converter, ensuring a seamless transformation of multimodal content into audio. In this section, we provide some examples of how to use each module.

## Content Extraction
Podcastfy's `content_extractor.py` module allows users to extract content from a given URL, which can be processed further to generate a podcast. Below is an example of how to use the content extraction component:

```python
from podcastfy.content_extractor import ContentExtractor

# Initialize the content extractor
extractor = ContentExtractor()

# Extract content from a URL
url = "https://example.com/article"
extracted_content = extractor.extract_content(url)

print("Extracted Content:")
print(extracted_content)
```

This example demonstrates how to extract text from a given URL. The extracted content is then passed to the next stages of processing.

## Content Generation

The `content_generator.py` module is responsible for generating conversational content based on textual input. Below is an example of how to use the content generation component:

```python
from podcastfy.content_generator import ContentGenerator

# Initialize the content generator
generator = ContentGenerator(api_key="<GEMINI_API_KEY>")

# Generate conversational content
input_text = "This is a sample input text about artificial intelligence."
generated_conversation = generator.generate_conversation(input_text)

print("Generated Conversation:")
print(generated_conversation)
```

 Users can opt to run a cloud-based LLM (Gemini) or run a local (potentially Open Source) LLM model ([see local llm configuration](https://github.com/souzatharsis/podcastfy/blob/main/usage/local_llm.md)).

## Text-to-Speech Conversion

The `text_to_speech.py` module allows the generated transcript to be converted into audio. Below is an example of how to use the text-to-speech component:

```python
from podcastfy.text_to_speech import TextToSpeech

# Initialize the text-to-speech converter
tts = TextToSpeech(model='elevenlabs', api_key="<ELEVENLABS_API_KEY>")

# Convert the generated conversation to speech
input_text = "<Person1>This is a sample conversation generated by Podcastfy.</Person1><Person2>That's great!</Person2>"
output_audio_file = "output_podcast.mp3"
tts.convert_to_speech(input_text, output_audio_file)

print(f"Audio saved to {output_audio_file}")
```

This example demonstrates how to use the `TextToSpeech` class to convert generated text into an audio file. Users can specify different models for TTS, such as `elevenlabs`, `openai`, or `edge` (free to use).


# Limitations

`Podcastfy` has several limitations, including:

- **Content Accuracy and Quality**
  - The accuracy of generated conversations depends heavily on the capabilities of the underlying LLMs.
  - Complex technical or domain-specific content may not always be accurately interpreted or summarized.
  - The framework cannot guarantee the factual correctness of generated content, requiring human verification for critical applications.

- **Language Support Constraints**
  - While multilingual support is available, performance may vary significantly across different languages.
  - Less common languages may have limited TTS voice options and lower-quality speech synthesis.
  - Nuanced cultural contexts and idioms may not translate effectively across languages.

- **Technical Dependencies**
  - Reliance on third-party APIs (OpenAI, ElevenLabs, Google) introduces potential service availability risks.
  - Local LLM options, while providing independence, require significant computational resources.
  - Network connectivity is required for cloud-based services, limiting offline usage.

- **Content Extraction Challenges**
  - Complex webpage layouts or dynamic content may not be accurately extracted.
  - PDF extraction quality depends on document formatting and structure.
  - YouTube video processing depends on the availability of transcripts.

- **Accessibility Considerations**
  - Generated audio may not fully meet all accessibility standards.
  - Limited support for real-time content processing.
  - May require additional processing for users with specific accessibility needs.

These limitations highlight areas for future development and improvement of the framework. Users should carefully consider these constraints when implementing `Podcastfy` for their specific use cases and requirements.

# Limitations

`Podcastfy` faces several key limitations in its current implementation. The accuracy and quality of generated content heavily depends on the underlying LLMs, with complex technical content potentially being misinterpreted. Additionally, while multilingual support is available, performance varies across languages, with less common languages having limited TTS voice options. The framework also relies on third-party APIs which introduces service availability risks, and local LLM options require significant computational resources.

These limitations highlight areas for future development and improvement of the framework. Users should carefully consider these constraints when implementing `Podcastfy` for their specific use cases and requirements.


# Conclusion

`Podcastfy` contributes to multimodal content accessibility by enabling the programmatic transformation of digital content into conversational audio. The framework addresses accessibility needs through automated content summarization and natural-sounding speech synthesis. Its modular design and configurable options allow for flexible content processing and audio generation workflows that can be adapted for different use cases and requirements.

We invite contributions from the community to further enhance the capabilities of `Podcastfy`. Whether it's by adding support for new input modalities, improving the quality of conversation generation, or optimizing the TTS synthesis, we welcome collaboration to make `Podcastfy` more powerful and versatile.


# Acknowledgements

We acknowledge the open-source community and the developers of the various libraries and tools that make `Podcastfy` possible. Special thanks to the developers of LangChain, Llamafile and HuggingFace. We are particularly grateful to all our [contributors](https://github.com/souzatharsis/podcastfy/graphs/contributors) who have helped improve this project.


# References
```

## File: `paper/podcastfy.drawio`
```
<mxfile host="app.diagrams.net" agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36" version="24.8.3">
  <diagram id="C5RBs43oDa-KdzZeNtuy" name="Page-1">
    <mxGraphModel dx="2022" dy="1797" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="WIyWlLk6GJQsqaUBKTNV-1" parent="WIyWlLk6GJQsqaUBKTNV-0" />
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-0" value="ContentExtractor" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=1;shadow=0;strokeWidth=1;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="147" y="40" width="173" height="120" as="geometry">
            <mxRectangle x="550" y="140" width="160" height="26" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-1" value="+youtube_transcriber&#xa;+website_extractor&#xa;+pdf_extractor" style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;labelBackgroundColor=none;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-0">
          <mxGeometry y="26" width="173" height="54" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-6" value="" style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-0">
          <mxGeometry y="80" width="173" height="10" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-7" value="+extract_content()" style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;labelBackgroundColor=none;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-0">
          <mxGeometry y="90" width="173" height="26" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-53" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-16" target="o9hW8QB3ydjtU5aNEMkl-1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="370" y="165" />
              <mxPoint x="370" y="93" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-16" value="YouTubeTranscriber" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="425" y="140" width="122" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-52" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-17" target="o9hW8QB3ydjtU5aNEMkl-1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-17" value="WebsiteExtractor" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="431" y="68" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-51" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-18" target="o9hW8QB3ydjtU5aNEMkl-1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="370" y="15" />
              <mxPoint x="370" y="93" />
            </Array>
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-18" value="PDFExtractor" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="431" y="-10" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-54" value="ContentGenerator" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=1;shadow=0;strokeWidth=1;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="40" y="290" width="200" height="120" as="geometry">
            <mxRectangle x="550" y="140" width="160" height="26" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-55" value="+llmafile&#xa;+gemini&#xa;..." style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;labelBackgroundColor=none;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-54">
          <mxGeometry y="26" width="200" height="54" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-56" value="" style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-54">
          <mxGeometry y="80" width="200" height="10" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-57" value="+generate_content()" style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;labelBackgroundColor=none;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-54">
          <mxGeometry y="90" width="200" height="26" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-58" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="380" y="415" />
              <mxPoint x="380" y="343" />
            </Array>
            <mxPoint x="426" y="415" as="sourcePoint" />
            <mxPoint x="357" y="343" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-59" value="&lt;font style=&quot;font-size: 10px;&quot;&gt;ChatGoogleGenerativeAI&lt;/font&gt;" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="419" y="390" width="122" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-62" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="380" y="265" />
              <mxPoint x="380" y="343" />
            </Array>
            <mxPoint x="432" y="265" as="sourcePoint" />
            <mxPoint x="357" y="343" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-63" value="Llamafile" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="425" y="240" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-64" value="text" style="html=1;verticalAlign=bottom;startArrow=oval;startFill=1;endArrow=block;startSize=8;curved=0;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;entryX=0.691;entryY=0.013;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="-0.3919" width="60" relative="1" as="geometry">
            <mxPoint x="234" y="160" as="sourcePoint" />
            <mxPoint x="234.20000000000027" y="291.55999999999995" as="targetPoint" />
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-70" value="text" style="html=1;verticalAlign=bottom;startArrow=oval;startFill=1;endArrow=block;startSize=8;curved=0;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="-0.7143" width="60" relative="1" as="geometry">
            <mxPoint x="69" y="-130" as="sourcePoint" />
            <mxPoint x="69" y="290" as="targetPoint" />
            <Array as="points">
              <mxPoint x="69" y="122.5" />
            </Array>
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-71" value="image" style="html=1;verticalAlign=bottom;startArrow=oval;startFill=1;endArrow=block;startSize=8;curved=0;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;entryX=0.333;entryY=-0.006;entryDx=0;entryDy=0;entryPerimeter=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" target="o9hW8QB3ydjtU5aNEMkl-54">
          <mxGeometry x="-0.7138" width="60" relative="1" as="geometry">
            <mxPoint x="107" y="-130" as="sourcePoint" />
            <mxPoint x="110" y="280" as="targetPoint" />
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-72" value="content source" style="html=1;verticalAlign=bottom;startArrow=oval;startFill=1;endArrow=block;startSize=8;curved=0;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="-0.2941" width="60" relative="1" as="geometry">
            <mxPoint x="233" y="-130" as="sourcePoint" />
            <mxPoint x="233" y="40" as="targetPoint" />
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-74" value="«langchain&lt;br&gt;interface»&lt;br&gt;&lt;span style=&quot;text-align: left;&quot;&gt;&lt;b&gt;BaseChatModel&lt;/b&gt;&lt;/span&gt;" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="425" y="316" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-75" value="" style="endArrow=block;dashed=1;endFill=0;endSize=12;html=1;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-63" target="o9hW8QB3ydjtU5aNEMkl-74">
          <mxGeometry width="160" relative="1" as="geometry">
            <mxPoint x="586" y="310" as="sourcePoint" />
            <mxPoint x="746" y="310" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-76" value="" style="endArrow=block;dashed=1;endFill=0;endSize=12;html=1;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-59" target="o9hW8QB3ydjtU5aNEMkl-74">
          <mxGeometry width="160" relative="1" as="geometry">
            <mxPoint x="490" y="300" as="sourcePoint" />
            <mxPoint x="490" y="326" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-77" value="&lt;font style=&quot;font-size: 10px;&quot;&gt;LLMBackend&lt;/font&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="267" y="324" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-89" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="o9hW8QB3ydjtU5aNEMkl-77">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="2" y="19" as="sourcePoint" />
            <mxPoint x="-28" y="18.58000000000004" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-79" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;fontColor=#393C56;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-77">
          <mxGeometry y="26" width="90" height="8" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-91" value="Content Extraction" style="swimlane;horizontal=0;whiteSpace=wrap;html=1;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="-20" y="-100" width="580" height="330" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-92" value="LLM-based Transcript Generation" style="swimlane;horizontal=0;whiteSpace=wrap;html=1;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="-20" y="230" width="580" height="220" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-93" value="TextToSpeech" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=1;shadow=0;strokeWidth=1;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="40" y="535" width="200" height="120" as="geometry">
            <mxRectangle x="550" y="140" width="160" height="26" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-94" value="+TTSProvider&#xa;..." style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;labelBackgroundColor=none;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-93">
          <mxGeometry y="26" width="200" height="54" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-95" value="" style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-93">
          <mxGeometry y="80" width="200" height="10" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-96" value="+text_to_speech()" style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;labelBackgroundColor=none;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-93">
          <mxGeometry y="90" width="200" height="26" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-97" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="380" y="660" />
              <mxPoint x="380" y="588" />
            </Array>
            <mxPoint x="426" y="660" as="sourcePoint" />
            <mxPoint x="357" y="588" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-98" value="&lt;font style=&quot;font-size: 12px;&quot;&gt;ElevenLabs&lt;/font&gt;" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="419" y="635" width="122" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-99" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0;exitY=0.5;exitDx=0;exitDy=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry relative="1" as="geometry">
            <Array as="points">
              <mxPoint x="380" y="510" />
              <mxPoint x="380" y="588" />
            </Array>
            <mxPoint x="432" y="510" as="sourcePoint" />
            <mxPoint x="357" y="588" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-100" value="OpenAI" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="425" y="485" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-101" value="«interface»&lt;br&gt;&lt;span style=&quot;text-align: left;&quot;&gt;&lt;b&gt;TTSProvider&lt;/b&gt;&lt;/span&gt;" style="html=1;whiteSpace=wrap;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="425" y="561" width="110" height="50" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-102" value="" style="endArrow=block;dashed=1;endFill=0;endSize=12;html=1;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-100" target="o9hW8QB3ydjtU5aNEMkl-101">
          <mxGeometry width="160" relative="1" as="geometry">
            <mxPoint x="586" y="555" as="sourcePoint" />
            <mxPoint x="746" y="555" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-103" value="" style="endArrow=block;dashed=1;endFill=0;endSize=12;html=1;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-98" target="o9hW8QB3ydjtU5aNEMkl-101">
          <mxGeometry width="160" relative="1" as="geometry">
            <mxPoint x="490" y="545" as="sourcePoint" />
            <mxPoint x="490" y="571" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-104" value="&lt;font style=&quot;font-size: 10px;&quot;&gt;TTSFactory&lt;/font&gt;" style="swimlane;fontStyle=1;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeParentMax=0;resizeLast=0;collapsible=1;marginBottom=0;whiteSpace=wrap;html=1;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="267" y="569" width="90" height="34" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-105" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1;entryY=0.5;entryDx=0;entryDy=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=15;" edge="1" parent="o9hW8QB3ydjtU5aNEMkl-104">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="2" y="19" as="sourcePoint" />
            <mxPoint x="-28" y="18.58000000000004" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-106" value="" style="line;strokeWidth=1;fillColor=none;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;strokeColor=inherit;fontColor=#393C56;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-104">
          <mxGeometry y="26" width="90" height="8" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-107" value="Text-to-Speech" style="swimlane;horizontal=0;whiteSpace=wrap;html=1;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="-20" y="450" width="580" height="250" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-108" value="transcript.txt" style="html=1;verticalAlign=bottom;startArrow=oval;startFill=1;endArrow=block;startSize=8;curved=0;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.502;exitY=1.141;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-57" target="o9hW8QB3ydjtU5aNEMkl-93">
          <mxGeometry x="-0.3919" width="60" relative="1" as="geometry">
            <mxPoint x="160" y="440" as="sourcePoint" />
            <mxPoint x="160" y="572" as="targetPoint" />
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-109" value="podcast.mp3" style="html=1;verticalAlign=bottom;startArrow=oval;startFill=1;endArrow=block;startSize=8;curved=0;rounded=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;entryX=0.5;entryY=0;entryDx=0;entryDy=0;exitX=0.502;exitY=1.141;exitDx=0;exitDy=0;exitPerimeter=0;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="0.44" width="60" relative="1" as="geometry">
            <mxPoint x="139.58" y="660" as="sourcePoint" />
            <mxPoint x="139.58" y="785" as="targetPoint" />
            <mxPoint as="offset" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-111" value="Client" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=0;shadow=0;strokeWidth=1;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="30" y="-200" width="290" height="70" as="geometry">
            <mxRectangle x="550" y="140" width="160" height="26" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-113" value="" style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-111">
          <mxGeometry y="26" width="290" height="10" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-114" value="+generate_podcast()" style="text;align=left;verticalAlign=top;spacingLeft=4;spacingRight=4;overflow=hidden;rotatable=0;points=[[0,0.5],[1,0.5]];portConstraint=eastwest;labelBackgroundColor=none;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-111">
          <mxGeometry y="36" width="290" height="26" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-116" value="Config" style="swimlane;fontStyle=0;align=center;verticalAlign=top;childLayout=stackLayout;horizontal=1;startSize=26;horizontalStack=0;resizeParent=1;resizeLast=0;collapsible=1;marginBottom=0;rounded=0;shadow=0;strokeWidth=1;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="355" y="-200" width="205" height="80" as="geometry">
            <mxRectangle x="550" y="140" width="160" height="26" as="alternateBounds" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-117" value="" style="line;html=1;strokeWidth=1;align=left;verticalAlign=middle;spacingTop=-1;spacingLeft=3;spacingRight=3;rotatable=0;labelPosition=right;points=[];portConstraint=eastwest;labelBackgroundColor=none;fillColor=#F2CC8F;strokeColor=#E07A5F;fontColor=#393C56;rounded=1;" vertex="1" parent="o9hW8QB3ydjtU5aNEMkl-116">
          <mxGeometry y="26" width="205" height="54" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-119" value="+user_instructions" style="text;html=1;align=center;verticalAlign=middle;resizable=0;points=[];autosize=1;strokeColor=none;fillColor=none;fontColor=#393C56;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="353" y="-172" width="120" height="30" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-120" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;entryX=1.013;entryY=0.237;entryDx=0;entryDy=0;entryPerimeter=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;endArrow=diamond;endFill=0;endSize=12;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry relative="1" as="geometry">
            <mxPoint x="354" y="-157" as="sourcePoint" />
            <mxPoint x="319.77" y="-157.8380000000002" as="targetPoint" />
          </mxGeometry>
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-121" value="WWW" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;strokeColor=#d6b656;fillColor=#fff2cc;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="50" y="-280" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-122" value="pdf" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="118" y="-280" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-123" value="youtube" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="186" y="-280" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-124" value="txt" style="text;html=1;align=center;verticalAlign=middle;whiteSpace=wrap;rounded=0;fillColor=#fff2cc;strokeColor=#d6b656;" vertex="1" parent="WIyWlLk6GJQsqaUBKTNV-1">
          <mxGeometry x="253.5" y="-280" width="60" height="30" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-125" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.172;entryY=-0.046;entryDx=0;entryDy=0;entryPerimeter=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-121" target="o9hW8QB3ydjtU5aNEMkl-111">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-126" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.407;entryY=0.007;entryDx=0;entryDy=0;entryPerimeter=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-122" target="o9hW8QB3ydjtU5aNEMkl-111">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-127" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.642;entryY=0.013;entryDx=0;entryDy=0;entryPerimeter=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-123" target="o9hW8QB3ydjtU5aNEMkl-111">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
        <mxCell id="o9hW8QB3ydjtU5aNEMkl-128" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.871;entryY=-0.011;entryDx=0;entryDy=0;entryPerimeter=0;strokeColor=#E07A5F;fontColor=#393C56;fillColor=#F2CC8F;" edge="1" parent="WIyWlLk6GJQsqaUBKTNV-1" source="o9hW8QB3ydjtU5aNEMkl-124" target="o9hW8QB3ydjtU5aNEMkl-111">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```

## File: `paper/related-work.md`
```markdown
* NotebookLM by Google
* Storm by Stanford University
* Open Notebook by @lf
* Open NotebookLM
* podlm.ai
* notebooklm.ai
```

## File: `podcastfy/__init__.py`
```python
# This file can be left empty for now
__version__ = "0.4.2"  # or whatever version you're on
```

## File: `podcastfy/client.py`
```python
"""
Podcastfy CLI

This module provides a command-line interface for generating podcasts or transcripts
from URLs or existing transcript files. It orchestrates the content extraction,
generation, and text-to-speech conversion processes.
"""

import os
import uuid
import typer
import yaml
from podcastfy.content_parser.content_extractor import ContentExtractor
from podcastfy.content_generator import ContentGenerator
from podcastfy.text_to_speech import TextToSpeech
from podcastfy.utils.config import Config, load_config
from podcastfy.utils.config_conversation import load_conversation_config
from podcastfy.utils.logger import setup_logger
from typing import List, Optional, Dict, Any
import copy

import logging

# Configure logging to show all levels and write to both file and console
""" logging.basicConfig(
    level=logging.DEBUG,  # Show all levels of logs
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('podcastfy.log'),  # Save to file
        logging.StreamHandler()  # Print to console
    ]
) """


logger = setup_logger(__name__)

app = typer.Typer()

os.environ["LANGCHAIN_TRACING_V2"] = "False"


def process_content(
    urls: Optional[List[str]] = None,
    transcript_file: Optional[str] = None,
    tts_model: Optional[str] = None,
    generate_audio: bool = True,
    config: Optional[Dict[str, Any]] = None,
    conversation_config: Optional[Dict[str, Any]] = None,
    image_paths: Optional[List[str]] = None,
    is_local: bool = False,
    text: Optional[str] = None,
    model_name: Optional[str] = None,
    api_key_label: Optional[str] = None,
    topic: Optional[str] = None,
    longform: bool = False
):
    """
    Process URLs, a transcript file, image paths, or raw text to generate a podcast or transcript.
    """
    try:
        if config is None:
            config = load_config()

        # Load default conversation config
        conv_config = load_conversation_config()

        # Update with provided config if any
        if conversation_config:
            conv_config.configure(conversation_config)
        # Get output directories from conversation config
        tts_config = conv_config.get("text_to_speech", {})
        output_directories = tts_config.get("output_directories", {})

        if transcript_file:
            logger.info(f"Using transcript file: {transcript_file}")
            with open(transcript_file, "r") as file:
                qa_content = file.read()
        else:
            # Initialize content_extractor if needed
            content_extractor = None
            if urls or topic or (text and longform and len(text.strip()) < 100):
                content_extractor = ContentExtractor()

            content_generator = ContentGenerator(
                is_local=is_local,
                model_name=model_name,
                api_key_label=api_key_label,
                conversation_config=conv_config.to_dict()
            )

            combined_content = ""
            
            if urls:
                logger.info(f"Processing {len(urls)} links")
                contents = [content_extractor.extract_content(link) for link in urls]
                combined_content += "\n\n".join(contents)

            if text:
                if longform and len(text.strip()) < 100:
                    logger.info("Text too short for direct long-form generation. Extracting context...")
                    expanded_content = content_extractor.generate_topic_content(text)
                    combined_content += f"\n\n{expanded_content}"
                else:
                    combined_content += f"\n\n{text}"

            if topic:
                topic_content = content_extractor.generate_topic_content(topic)
                combined_content += f"\n\n{topic_content}"

            # Generate Q&A content using output directory from conversation config
            random_filename = f"transcript_{uuid.uuid4().hex}.txt"
            transcript_filepath = os.path.join(
                output_directories.get("transcripts", "data/transcripts"),
                random_filename,
            )
            qa_content = content_generator.generate_qa_content(
                combined_content,
                image_file_paths=image_paths or [],
                output_filepath=transcript_filepath,
                longform=longform
            )

        if generate_audio:
            api_key = None
            if tts_model != "edge":
                api_key = getattr(config, f"{tts_model.upper().replace('MULTI', '')}_API_KEY")

            text_to_speech = TextToSpeech(
                model=tts_model,
                api_key=api_key,
                conversation_config=conv_config.to_dict(),
            )

            random_filename = f"podcast_{uuid.uuid4().hex}.mp3"
            audio_file = os.path.join(
                output_directories.get("audio", "data/audio"), random_filename
            )
            text_to_speech.convert_to_speech(qa_content, audio_file)
            logger.info(f"Podcast generated successfully using {tts_model} TTS model")
            return audio_file
        else:
            logger.info(f"Transcript generated successfully: {transcript_filepath}")
            return transcript_filepath

    except Exception as e:
        logger.error(f"An error occurred in the process_content function: {str(e)}")
        raise


@app.command()
def main(
    urls: list[str] = typer.Option(None, "--url", "-u", help="URLs to process"),
    file: typer.FileText = typer.Option(
        None, "--file", "-f", help="File containing URLs, one per line"
    ),
    transcript: typer.FileText = typer.Option(
        None, "--transcript", "-t", help="Path to a transcript file"
    ),
    tts_model: str = typer.Option(
        None,
        "--tts-model",
        "-tts",
        help="TTS model to use (openai, elevenlabs, edge, or gemini)",
    ),
    transcript_only: bool = typer.Option(
        False, "--transcript-only", help="Generate only a transcript without audio"
    ),
    conversation_config_path: str = typer.Option(
        None,
        "--conversation-config",
        "-cc",
        help="Path to custom conversation configuration YAML file",
    ),
    image_paths: List[str] = typer.Option(
        None, "--image", "-i", help="Paths to image files to process"
    ),
    is_local: bool = typer.Option(
        False,
        "--local",
        "-l",
        help="Use a local LLM instead of a remote one (http://localhost:8080)",
    ),
    text: str = typer.Option(
        None, "--text", "-txt", help="Raw text input to be processed"
    ),
    llm_model_name: str = typer.Option(
        None, "--llm-model-name", "-m", help="LLM model name for transcript generation"
    ),
    api_key_label: str = typer.Option(
        None, "--api-key-label", "-k", help="Environment variable name for LLMAPI key"
    ),
    topic: str = typer.Option(
        None, "--topic", "-tp", help="Topic to generate podcast about"
    ),
    longform: bool = typer.Option(
        False, 
        "--longform", 
        "-lf", 
        help="Generate long-form content (only available for text input without images)"
    ),
):
    """
    Generate a podcast or transcript from a list of URLs, a file containing URLs, a transcript file, image files, or raw text.
    """
    try:
        config = load_config()
        main_config = config.get("main", {})

        conversation_config = None
        # Load conversation config if provided
        if conversation_config_path:
            with open(conversation_config_path, "r") as f:
                conversation_config: Dict[str, Any] | None = yaml.safe_load(f)

        # Use default TTS model from conversation config if not specified
        if tts_model is None:
            tts_config = load_conversation_config().get("text_to_speech", {})
            tts_model = tts_config.get("default_tts_model", "openai")

        if transcript:
            if image_paths:
                logger.warning("Image paths are ignored when using a transcript file.")
            final_output = process_content(
                transcript_file=transcript.name,
                tts_model=tts_model,
                generate_audio=not transcript_only,
                conversation_config=conversation_config,
                config=config,
                is_local=is_local,
                text=text,
                model_name=llm_model_name,
                api_key_label=api_key_label,
                topic=topic,
                longform=longform
            )
        else:
            urls_list = urls or []
            if file:
                urls_list.extend([line.strip() for line in file if line.strip()])

            if not urls_list and not image_paths and not text and not topic:
                raise typer.BadParameter(
                    "No input provided. Use --url, --file, --transcript, --image, --text, or --topic."
                )

            final_output = process_content(
                urls=urls_list,
                tts_model=tts_model,
                generate_audio=not transcript_only,
                config=config,
                conversation_config=conversation_config,
                image_paths=image_paths,
                is_local=is_local,
                text=text,
                model_name=llm_model_name,
                api_key_label=api_key_label,
                topic=topic,
                longform=longform
            )

        if transcript_only:
            typer.echo(f"Transcript generated successfully: {final_output}")
        else:
            typer.echo(
                f"Podcast generated successfully using {tts_model} TTS model: {final_output}"
            )

    except Exception as e:
        typer.echo(f"An error occurred: {str(e)}", err=True)
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()


def generate_podcast(
    urls: Optional[List[str]] = None,
    url_file: Optional[str] = None,
    transcript_file: Optional[str] = None,
    tts_model: Optional[str] = None,
    transcript_only: bool = False,
    config: Optional[Dict[str, Any]] = None,
    conversation_config: Optional[Dict[str, Any]] = None,
    image_paths: Optional[List[str]] = None,
    is_local: bool = False,
    text: Optional[str] = None,
    llm_model_name: Optional[str] = None,
    api_key_label: Optional[str] = None,
    topic: Optional[str] = None,
    longform: bool = False,
) -> Optional[str]:
    """
    Generate a podcast or transcript from a list of URLs, a file containing URLs, a transcript file, or image files.

    Args:
        urls (Optional[List[str]]): List of URLs to process.
        url_file (Optional[str]): Path to a file containing URLs, one per line.
        transcript_file (Optional[str]): Path to a transcript file.
        tts_model (Optional[str]): TTS model to use ('openai' [default], 'elevenlabs', 'edge', or 'gemini').
        transcript_only (bool): Generate only a transcript without audio. Defaults to False.
        config (Optional[Dict[str, Any]]): User-provided configuration dictionary.
        conversation_config (Optional[Dict[str, Any]]): User-provided conversation configuration dictionary.
        image_paths (Optional[List[str]]): List of image file paths to process.
        is_local (bool): Whether to use a local LLM. Defaults to False.
        text (Optional[str]): Raw text input to be processed.
        llm_model_name (Optional[str]): LLM model name for content generation.
        api_key_label (Optional[str]): Environment variable name for LLM API key.
        topic (Optional[str]): Topic to generate podcast about.

    Returns:
        Optional[str]: Path to the final podcast audio file, or None if only generating a transcript.
    """
    try:
        print("Generating podcast...")
        # Load default config
        default_config = load_config()

        # Update config if provided
        if config:
            if isinstance(config, dict):
                # Create a deep copy of the default config
                updated_config = copy.deepcopy(default_config)
                # Update the copy with user-provided values
                updated_config.configure(**config)
                default_config = updated_config
            elif isinstance(config, Config):
                # If it's already a Config object, use it directly
                default_config = config
            else:
                raise ValueError(
                    "Config must be either a dictionary or a Config object"
                )

        if not conversation_config:
            conversation_config = load_conversation_config().to_dict()

        main_config = default_config.config.get("main", {})

        # Use provided tts_model if specified, otherwise use the one from config
        if tts_model is None:
            tts_model = conversation_config.get("default_tts_model", "openai")

        if transcript_file:
            if image_paths:
                logger.warning("Image paths are ignored when using a transcript file.")
            return process_content(
                transcript_file=transcript_file,
                tts_model=tts_model,
                generate_audio=not transcript_only,
                config=default_config,
                conversation_config=conversation_config,
                is_local=is_local,
                text=text,
                model_name=llm_model_name,
                api_key_label=api_key_label,
                topic=topic,
                longform=longform
            )
        else:
            urls_list = urls or []
            if url_file:
                with open(url_file, "r") as file:
                    urls_list.extend([line.strip() for line in file if line.strip()])

            if not urls_list and not image_paths and not text and not topic:
                raise ValueError(
                    "No input provided. Please provide either 'urls', 'url_file', "
                    "'transcript_file', 'image_paths', 'text', or 'topic'."
                )

            return process_content(
                urls=urls_list,
                tts_model=tts_model,
                generate_audio=not transcript_only,
                config=default_config,
                conversation_config=conversation_config,
                image_paths=image_paths,
                is_local=is_local,
                text=text,
                model_name=llm_model_name,
                api_key_label=api_key_label,
                topic=topic,
                longform=longform
            )

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        raise
```

## File: `podcastfy/config.yaml`
```yaml
content_generator:
  llm_model: "gemini-2.5-flash"
  meta_llm_model: "gemini-2.5-flash"
  max_output_tokens: 8192
  prompt_template: "souzatharsis/podcastfy_multimodal_cleanmarkup"
  prompt_commit: "b2365f11"
  longform_prompt_template: "souzatharsis/podcastfy_longform"
  longform_prompt_commit: "acfdbc91" #"ff865019"
  cleaner_prompt_template: "souzatharsis/podcastfy_longform_clean"
  cleaner_prompt_commit: "8c110a0b"
  rewriter_prompt_template: "souzatharsis/podcast_rewriter"
  rewriter_prompt_commit: "8ee296fb"
content_extractor:
  youtube_url_patterns:
    - "youtube.com"
    - "youtu.be"

website_extractor:
  jina_api_url: "https://r.jina.ai"
  markdown_cleaning:
    remove_patterns:
      - '!\[.*?\]\(.*?\)'
      - '\[([^\]]+)\]\([^\)]+\)'
      - 'https?://\S+|www\.\S+'

youtube_transcriber:
  remove_phrases:
    - "[music]"

logging:
  level: "INFO"
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"


website_extractor:
  markdown_cleaning:
    remove_patterns:
      - '\[.*?\]'  # Remove square brackets and their contents
      - '\(.*?\)'  # Remove parentheses and their contents
      - '^\s*[-*]\s'  # Remove list item markers
      - '^\s*\d+\.\s'  # Remove numbered list markers
      - '^\s*#+'  # Remove markdown headers
  unwanted_tags:
    - 'script'
    - 'style'
    - 'nav'
    - 'footer'
    - 'header'
    - 'aside'
    - 'noscript'
  user_agent: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
  timeout: 10  # Request timeout in seconds
```

## File: `podcastfy/content_generator.py`
```python
"""
Content Generator Module

This module is responsible for generating Q&A content based on input texts using
LangChain and various LLM backends. It handles the interaction with the AI model and
provides methods to generate and save the generated content.
"""

import os
from typing import Optional, Dict, Any, List
import re


from langchain_community.chat_models import ChatLiteLLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms.llamafile import Llamafile
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from podcastfy.utils.config_conversation import load_conversation_config
from podcastfy.utils.config import load_config
import logging
from langchain.prompts import HumanMessagePromptTemplate
from abc import ABC, abstractmethod

logger = logging.getLogger(__name__)


class LLMBackend:
    def __init__(
        self,
        is_local: bool,
        temperature: float,
        max_output_tokens: int,
        model_name: str,
        api_key_label: str = "GEMINI_API_KEY",
    ):
        """
        Initialize the LLMBackend.

        Args:
                is_local (bool): Whether to use a local LLM or not.
                temperature (float): The temperature for text generation.
                max_output_tokens (int): The maximum number of output tokens.
                model_name (str): The name of the model to use.
        """
        self.is_local = is_local
        self.temperature = temperature
        self.max_output_tokens = max_output_tokens
        self.model_name = model_name
        self.is_multimodal = not is_local  # Does not assume local LLM is multimodal

        common_params = {
            "temperature": temperature,
            "presence_penalty": 0.75,  # Encourage diverse content
            "frequency_penalty": 0.75,  # Avoid repetition
        }

        if is_local:
            self.llm = Llamafile() # replace with ollama
        elif (
            "gemini" in self.model_name.lower()
        ):  # keeping original gemini as a special case while we build confidence on LiteLLM

            self.llm = ChatGoogleGenerativeAI(
                api_key=os.environ["GEMINI_API_KEY"],
                model=model_name,
                max_output_tokens=max_output_tokens,
                **common_params,
            )
        else:  # user should set api_key_label from input
            self.llm = ChatLiteLLM(
                model=self.model_name,
                temperature=temperature,
                api_key=os.environ[api_key_label],
            )


class LongFormContentGenerator:
    """
    Handles generation of long-form podcast conversations by breaking content into manageable chunks.
    
    Uses a "Content Chunking with Contextual Linking" strategy to maintain context between segments
    while generating longer conversations.
    
    Attributes:
        LONGFORM_INSTRUCTIONS (str): Constant containing instructions for long-form generation
        llm_chain: The LangChain chain used for content generation
    """
    # Add constant for long-form instructions
    LONGFORM_INSTRUCTIONS = """
    Additional Instructions:
        1. Provide extensive examples and real-world applications
        2. Include detailed analysis and multiple perspectives
        3. Use the "yes, and" technique to build upon points
        4. Incorporate relevant anecdotes and case studies
        5. Balance detailed explanations with engaging dialogue
        6. Maintain consistent voice throughout the extended discussion
        7. Generate a long conversation - output max_output_tokens tokens
    """
    
    def __init__(self, chain, llm, config_conversation: Dict[str, Any], ):
        """
        Initialize ConversationGenerator.
        
        Args:
            llm_chain: The LangChain chain to use for generation
            config_conversation: Conversation configuration dictionary
        """
        self.llm_chain = chain
        self.llm = llm
        self.max_num_chunks = config_conversation.get("max_num_chunks", 10)  # Default if not in config
        self.min_chunk_size = config_conversation.get("min_chunk_size", 200)  # Default if not in config

    def __calculate_chunk_size(self, input_content: str) -> int:
        """
        Calculate chunk size based on input content length.
        
        Args:
            input_content: Input text content
                
        Returns:
            Calculated chunk size that ensures:
            - Returns 1 if content length <= min_chunk_size
            - Each chunk has at least min_chunk_size characters
            - Number of chunks is at most max_num_chunks
        """
        input_length = len(input_content)
        if input_length <= self.min_chunk_size:
            return input_length
        
        maximum_chunk_size = input_length // self.max_num_chunks
        if maximum_chunk_size >= self.min_chunk_size:
            return maximum_chunk_size
        
        # Calculate chunk size that maximizes size while maintaining minimum chunks
        return input_length // (input_length // self.min_chunk_size)

    def chunk_content(self, input_content: str, chunk_size: int) -> List[str]:
        """
        Split input content into manageable chunks while preserving context.
        
        Args:
            input_content (str): The input text to chunk
            chunk_size (int): Maximum size of each chunk
            
        Returns:
            List[str]: List of content chunks
        """
        sentences = input_content.split('. ')
        chunks = []
        current_chunk = []
        current_length = 0
        
        for sentence in sentences:
            sentence_length = len(sentence)
            if current_length + sentence_length > chunk_size and current_chunk:
                chunks.append('. '.join(current_chunk) + '.')
                current_chunk = []
                current_length = 0
            current_chunk.append(sentence)
            current_length += sentence_length
            
        if current_chunk:
            chunks.append('. '.join(current_chunk) + '.')
        return chunks

    def enhance_prompt_params(self, prompt_params: Dict, 
                              part_idx: int, 
                              total_parts: int,
                              chat_context: str) -> Dict:
        """
        Enhance prompt parameters for long-form content generation.
        
        Args:
            prompt_params (Dict): Original prompt parameters
            part_idx (int): Index of current conversation part
            total_parts (int): Total number of conversation parts
            chat_context (str): Chat context from previous parts
            
        Returns:
            Dict: Enhanced prompt parameters with part-specific instructions
        """
        enhanced_params = prompt_params.copy()
		# Initialize part_instructions with chat context
        enhanced_params["context"] = chat_context
        
        COMMON_INSTRUCTIONS = """
            Podcast conversation so far is given in CONTEXT.
            Continue the natural flow of conversation. Follow-up on the very previous point/question without repeating topics or points already discussed!
            Hence, the transition should be smooth and natural. Avoid abrupt transitions.
            Make sure the first to speak is different from the previous speaker. Look at the last tag in CONTEXT to determine the previous speaker. 
            If last tag in CONTEXT is <Person1>, then the first to speak now should be <Person2>.
            If last tag in CONTEXT is <Person2>, then the first to speak now should be <Person1>.
            This is a live conversation without any breaks.
            Hence, avoid statemeents such as "we'll discuss after a short break.  Stay tuned" or "Okay, so, picking up where we left off".
        """ 

        # Add part-specific instructions
        if part_idx == 0:
            enhanced_params["instruction"] = f"""
            ALWAYS START THE CONVERSATION GREETING THE AUDIENCE: Welcome to {enhanced_params["podcast_name"]} - {enhanced_params["podcast_tagline"]}.
            You are generating the Introduction part of a long podcast conversation.
            Don't cover any topics yet, just introduce yourself and the topic. Leave the rest for later parts, following these guidelines:
            """
        elif part_idx == total_parts - 1:
            enhanced_params["instruction"] = f"""
            You are generating the last part of a long podcast conversation. 
            {COMMON_INSTRUCTIONS}
            For this part, discuss the below INPUT and then make concluding remarks in a podcast conversation format and END THE CONVERSATION GREETING THE AUDIENCE WITH PERSON1 ALSO SAYING A GOOD BYE MESSAGE, following these guidelines:
            """
        else:
            enhanced_params["instruction"] = f"""
            You are generating part {part_idx+1} of {total_parts} parts of a long podcast conversation.
            {COMMON_INSTRUCTIONS}
            For this part, discuss the below INPUT in a podcast conversation format, following these guidelines:
            """
        
        return enhanced_params

    def generate_long_form(
        self, 
        input_content: str, 
        prompt_params: Dict
    ) -> str:
        """
        Generate a complete long-form conversation using chunked content.
        
        Args:
            input_content (str): Input text for conversation
            prompt_params (Dict): Base prompt parameters
            
        Returns:
            str: Generated long-form conversation
        """
        # Add long-form instructions once at the beginning
        prompt_params["user_instructions"] = prompt_params.get("user_instructions", "") + self.LONGFORM_INSTRUCTIONS
        
        # Get chunk size
        chunk_size = self.__calculate_chunk_size(input_content)

        chunks = self.chunk_content(input_content, chunk_size)
        conversation_parts = []
        chat_context = input_content
        num_parts = len(chunks)
        print(f"Generating {num_parts} parts")
        
        for i, chunk in enumerate(chunks):
            enhanced_params = self.enhance_prompt_params(
                prompt_params,
                part_idx=i,
                total_parts=num_parts,
                chat_context=chat_context
            )
            enhanced_params["input_text"] = chunk
            response = self.llm_chain.invoke(enhanced_params)
            if i == 0:
                chat_context = response
            else:
                chat_context = chat_context + response
            print(f"Generated part {i+1}/{num_parts}: Size {len(chunk)} characters.")
            #print(f"[LLM-START] Step: {i+1} ##############################")
            #print(response)
            #print(f"[LLM-END] Step: {i+1} ##############################")
            conversation_parts.append(response)

        return self.stitch_conversations(conversation_parts)
    
    def stitch_conversations(self, parts: List[str]) -> str:
        """
        Combine conversation parts with smooth transitions.
        
        Args:
            parts (List[str]): List of conversation parts
            
        Returns:
            str: Combined conversation
        """
        # Simply join the parts, preserving all markup
        return "\n".join(parts)


# Make BaseContentCleaner a mixin class
class ContentCleanerMixin:
    """
    Mixin class containing common transcript cleaning operations.
    
    Provides reusable cleaning methods that can be used by different content generation strategies.
    Methods use protected naming convention (_method_name) as they are intended for internal use
    by the strategies.
    """
    
    @staticmethod
    def _clean_scratchpad(text: str) -> str:
        """
        Remove scratchpad blocks, plaintext blocks, standalone triple backticks, any string enclosed in brackets, and underscores around words.
        """
        try:
            import re
            pattern = r'```scratchpad\n.*?```\n?|```plaintext\n.*?```\n?|```\n?|\[.*?\]'
            cleaned_text = re.sub(pattern, '', text, flags=re.DOTALL)
            # Remove "xml" if followed by </Person1> or </Person2>
            cleaned_text = re.sub(r"xml(?=\s*</Person[12]>)", "", cleaned_text)
            # Remove underscores around words
            cleaned_text = re.sub(r'_(.*?)_', r'\1', cleaned_text)
            return cleaned_text.strip()
        except Exception as e:
            logger.error(f"Error cleaning scratchpad content: {str(e)}")
            return text

    @staticmethod
    def _clean_tss_markup(
        input_text: str, 
        additional_tags: List[str] = ["Person1", "Person2"]
    ) -> str:
        """
        Remove unsupported TSS markup tags while preserving supported ones.
        """
        try:
            input_text = ContentCleanerMixin._clean_scratchpad(input_text)
            supported_tags = ["speak", "lang", "p", "phoneme", "s", "sub"]
            supported_tags.extend(additional_tags)

            pattern = r"</?(?!(?:" + "|".join(supported_tags) + r")\b)[^>]+>"
            cleaned_text = re.sub(pattern, "", input_text)
            cleaned_text = re.sub(r"\n\s*\n", "\n", cleaned_text)
            cleaned_text = re.sub(r"\*", "", cleaned_text)

            for tag in additional_tags:
                cleaned_text = re.sub(
                    f'<{tag}>(.*?)(?=<(?:{"|".join(additional_tags)})>|$)',
                    f"<{tag}>\\1</{tag}>",
                    cleaned_text,
                    flags=re.DOTALL,
                )
            


            return cleaned_text.strip()
            
        except Exception as e:
            logger.error(f"Error cleaning TSS markup: {str(e)}")
            return input_text


class ContentGenerationStrategy(ABC):
    """
    Abstract base class defining the interface for content generation strategies.
    
    Defines the contract that all concrete strategies must implement, including
    validation, generation, and cleaning operations.
    """
    
    @abstractmethod
    def validate(self, input_texts: str, image_file_paths: List[str]) -> None:
        """Validate inputs for this strategy."""
        pass
        
    @abstractmethod
    def generate(self, 
                chain,
                input_texts: str,
                prompt_params: Dict[str, Any],
                **kwargs) -> str:
        """Generate content using this strategy."""
        pass
        
    @abstractmethod
    def clean(self, 
             response: str,
             config: Dict[str, Any]) -> str:
        """Clean the generated response according to strategy."""
        pass

    @abstractmethod
    def compose_prompt_params(self,
                            config_conversation: Dict[str, Any],
                            image_file_paths: List[str] = [],
                            image_path_keys: List[str] = [],
                            input_texts: str = "") -> Dict[str, Any]:
        """Compose prompt parameters according to strategy."""
        pass


class StandardContentStrategy(ContentGenerationStrategy, ContentCleanerMixin):
    """
    Strategy for generating standard-length content.
    
    Implements basic content generation without chunking or special handling.
    Uses common cleaning operations from ContentCleanerMixin.
    """
    
    def __init__(self, llm, content_generator_config: Dict[str, Any], config_conversation: Dict[str, Any]):
        """
        Initialize StandardContentStrategy.
        
        Args:
            content_generator_config (Dict[str, Any]): Configuration for content generation
            config_conversation (Dict[str, Any]): Conversation configuration
        """
        self.llm = llm
        self.content_generator_config = content_generator_config
        self.config_conversation = config_conversation
    
    def validate(self, input_texts: str, image_file_paths: List[str]) -> None:
        """No specific validation needed for standard content."""
        pass
        
    def generate(self, 
                chain,
                input_texts: str,
                prompt_params: Dict[str, Any],
                **kwargs) -> str:
        """Generate standard-length content."""
        return chain.invoke(prompt_params)
        
    def clean(self, 
             response: str,
             config: Dict[str, Any]) -> str:
        """Apply basic TSS markup cleaning."""
        return self._clean_tss_markup(response)

    def compose_prompt_params(self,
                            config_conversation: Dict[str, Any],
                            image_file_paths: List[str] = [],
                            image_path_keys: List[str] = [],
                            input_texts: str = "") -> Dict[str, Any]:
        """Compose prompt parameters for standard content generation."""
        prompt_params = {
            "input_text": input_texts,
            "conversation_style": ", ".join(
                config_conversation.get("conversation_style", [])
            ),
            "roles_person1": config_conversation.get("roles_person1"),
            "roles_person2": config_conversation.get("roles_person2"),
            "dialogue_structure": ", ".join(
                config_conversation.get("dialogue_structure", [])
            ),
            "podcast_name": config_conversation.get("podcast_name"),
            "podcast_tagline": config_conversation.get("podcast_tagline"),
            "output_language": config_conversation.get("output_language"),
            "engagement_techniques": ", ".join(
                config_conversation.get("engagement_techniques", [])
            ),
        }

        # Add image paths to parameters if any
        for key, path in zip(image_path_keys, image_file_paths):
            prompt_params[key] = path

        return prompt_params


class LongFormContentStrategy(ContentGenerationStrategy, ContentCleanerMixin):
    """
    Strategy for generating long-form content.
    
    Implements advanced content generation using chunking and context maintenance.
    Includes additional cleaning operations specific to long-form content.
    
    Note:
        - Only works with text input (no images)
        - Requires non-empty input text
    """
    
    def __init__(self, llm, content_generator_config: Dict[str, Any], config_conversation: Dict[str, Any]):
        """
        Initialize LongFormContentStrategy.
        
        Args:
            content_generator_config (Dict[str, Any]): Configuration for content generation
            config_conversation (Dict[str, Any]): Conversation configuration
        """
        self.llm = llm
        self.content_generator_config = content_generator_config
        self.config_conversation = config_conversation
    
    def validate(self, input_texts: str, image_file_paths: List[str]) -> None:
        """Validate inputs for long-form generation."""
        if not input_texts.strip():
            raise ValueError("Long-form generation requires non-empty input text")
        if image_file_paths:
            raise ValueError("Long-form generation is not available with image inputs")
            
    def generate(self, 
                chain,
                input_texts: str,
                prompt_params: Dict[str, Any],
                **kwargs) -> str:
        """Generate long-form content."""
        generator = LongFormContentGenerator(chain, self.llm, self.config_conversation)
        return generator.generate_long_form(
            input_texts,
            prompt_params
        )
        
    def clean(self, 
             response: str,
             config: Dict[str, Any]) -> str:
        """Apply enhanced cleaning for long-form content."""
        # First apply standard cleaning using common method
        standard_clean = self._clean_tss_markup(response)
        # Then apply additional long-form specific cleaning
        return self._clean_transcript_response(standard_clean, config)
    
    def _clean_transcript_response(self, transcript: str, config: Dict[str, Any]) -> str:
        """
        Clean transcript using a two-step process with LLM-based cleaning.
        
        First cleans the markup using a specialized prompt template, then rewrites
        for better flow and consistency using a second prompt template.
        
        Args:
            transcript (str): Raw transcript text that may contain scratchpad blocks
            config (Dict[str, Any]): Configuration dictionary containing LLM and prompt settings
            
        Returns:
            str: Cleaned and rewritten transcript with proper tags and improved flow
            
        Note:
            Falls back to original or partially cleaned transcript if any cleaning step fails
        """
        logger.debug("Starting transcript cleaning process")

        final_transcript = self._fix_alternating_tags(transcript)
        
        logger.debug("Completed transcript cleaning process")
        
        return final_transcript

         
    def _clean_transcript_response_DEPRECATED(self, transcript: str, config: Dict[str, Any]) -> str:
        """
        Clean transcript using a two-step process with LLM-based cleaning.
        
        First cleans the markup using a specialized prompt template, then rewrites
        for better flow and consistency using a second prompt template.
        
        Args:
            transcript (str): Raw transcript text that may contain scratchpad blocks
            config (Dict[str, Any]): Configuration dictionary containing LLM and prompt settings
            
        Returns:
            str: Cleaned and rewritten transcript with proper tags and improved flow
            
        Note:
            Falls back to original or partially cleaned transcript if any cleaning step fails
        """
        logger.debug("Starting transcript cleaning process")
        try:
            logger.debug("Initializing LLM model for cleaning")
            # Initialize model with config values for consistent cleaning
            #llm = ChatGoogleGenerativeAI(
            #    model=self.content_generator_config["meta_llm_model"],
            #    temperature=0,
            #    presence_penalty=0.75,  # Encourage diverse content
            #    frequency_penalty=0.75  # Avoid repetition
            #)
            llm = self.llm
            logger.debug("LLM model initialized successfully")

            # Get prompt templates from hub
            logger.debug("Pulling prompt templates from hub")
            try:
                clean_transcript_prompt = hub.pull(f"{self.content_generator_config['cleaner_prompt_template']}:{self.content_generator_config['cleaner_prompt_commit']}")
                rewrite_prompt = hub.pull(f"{self.content_generator_config['rewriter_prompt_template']}:{self.content_generator_config['rewriter_prompt_commit']}")
                logger.debug("Successfully pulled prompt templates")
            except Exception as e:
                logger.error(f"Error pulling prompt templates: {str(e)}")
                return transcript
            
            logger.debug("Creating cleaning and rewriting chains")
            # Create chains
            clean_chain = clean_transcript_prompt | llm | StrOutputParser()
            rewrite_chain = rewrite_prompt | llm | StrOutputParser()
            
            # Run cleaning chain
            logger.debug("Executing cleaning chain")
            try:
                cleaned_response = clean_chain.invoke({"transcript": transcript})
                if not cleaned_response:
                    logger.warning("Cleaning chain returned empty response")
                    return transcript
                logger.debug("Successfully cleaned transcript")
            except Exception as e:
                logger.error(f"Error in cleaning chain: {str(e)}")
                return transcript
            
            # Run rewriting chain
            logger.debug("Executing rewriting chain")
            try:
                rewritten_response = rewrite_chain.invoke({"transcript": cleaned_response})
                if not rewritten_response:
                    logger.warning("Rewriting chain returned empty response")
                    return cleaned_response  # Fall back to cleaned version
                logger.debug("Successfully rewrote transcript")
            except Exception as e:
                logger.error(f"Error in rewriting chain: {str(e)}")
                return cleaned_response  # Fall back to cleaned version
                
            # Fix alternating tags in the final response
            logger.debug("Fixing alternating tags")
            final_transcript = self._fix_alternating_tags(rewritten_response)
            logger.debug("Completed transcript cleaning process")
            
            return final_transcript
            
        except Exception as e:
            logger.error(f"Error in transcript cleaning process: {str(e)}")
            return transcript  # Return original if cleaning fails

    def _fix_alternating_tags(self, transcript: str) -> str:
        """
        Ensures transcript has properly alternating Person1 and Person2 tags.
        
        Merges consecutive same-person tags and ensures proper tag alternation
        throughout the transcript.
        
        Args:
            transcript (str): Input transcript text that may have consecutive same-person tags
            
        Returns:
            str: Transcript with properly alternating tags and merged content
            
        Example:
            Input:
                <Person1>Hello</Person1>
                <Person1>World</Person1>
                <Person2>Hi</Person2>
            Output:
                <Person1>Hello World</Person1>
                <Person2>Hi</Person2>
                
        Note:
            Returns original transcript if cleaning fails
        """
        try:
            # Split into individual tag blocks while preserving tags
            pattern = r'(<Person[12]>.*?</Person[12]>)'
            blocks = re.split(pattern, transcript, flags=re.DOTALL)
            
            # Filter out empty/whitespace blocks
            blocks = [b.strip() for b in blocks if b.strip()]
            
            merged_blocks = []
            current_content = []
            current_person = None
            
            for block in blocks:
                # Extract person number and content
                match = re.match(r'<Person([12])>(.*?)</Person\1>', block, re.DOTALL)
                if not match:
                    continue
                    
                person_num, content = match.groups()
                content = content.strip()
                
                if current_person == person_num:
                    # Same person - append content
                    current_content.append(content)
                else:
                    # Different person - flush current content if any
                    if current_content:
                        merged_text = " ".join(current_content)
                        merged_blocks.append(f"<Person{current_person}>{merged_text}</Person{current_person}>")
                    # Start new person
                    current_person = person_num
                    current_content = [content]
            
            # Flush final content
            if current_content:
                merged_text = " ".join(current_content)
                merged_blocks.append(f"<Person{current_person}>{merged_text}</Person{current_person}>")
                
            return "\n".join(merged_blocks)
            
        except Exception as e:
            logger.error(f"Error fixing alternating tags: {str(e)}")
            return transcript  # Return original if fixing fails

    def compose_prompt_params(self,
                            config_conversation: Dict[str, Any],
                            image_file_paths: List[str] = [],
                            image_path_keys: List[str] = [],
                            input_texts: str = "") -> Dict[str, Any]:
        """Compose prompt parameters for long-form content generation."""
        return {
            "conversation_style": ", ".join(
                config_conversation.get("conversation_style", [])
            ),
            "roles_person1": config_conversation.get("roles_person1"),
            "roles_person2": config_conversation.get("roles_person2"),
            "dialogue_structure": ", ".join(
                config_conversation.get("dialogue_structure", [])
            ),
            "podcast_name": config_conversation.get("podcast_name"),
            "podcast_tagline": config_conversation.get("podcast_tagline"),
            "output_language": config_conversation.get("output_language"),
            "engagement_techniques": ", ".join(
                config_conversation.get("engagement_techniques", [])
            ),
        }


class ContentGenerator:
    def __init__(
        self, 
        is_local: bool=False, 
        model_name: str="gemini-2.5-flash", 
        api_key_label: str="GEMINI_API_KEY",
        conversation_config: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize the ContentGenerator.

        Args:
                api_key (str): API key for Google's Generative AI.
                conversation_config (Optional[Dict[str, Any]]): Custom conversation configuration.
        """
        #os.environ["GOOGLE_API_KEY"] = api_key
        self.config = load_config()
        self.content_generator_config = self.config.get("content_generator", {})

        self.config_conversation = load_conversation_config(conversation_config)
        self.tts_config = self.config_conversation.get("text_to_speech", {})

        # Get output directories from conversation config
        self.output_directories = self.tts_config.get("output_directories", {})

        # Create output directories if they don't exist
        transcripts_dir = self.output_directories.get("transcripts")

        if transcripts_dir and not os.path.exists(transcripts_dir):
            os.makedirs(transcripts_dir)
        
        self.is_local = is_local

                # Initialize LLM backend
        if not model_name:
            model_name = self.content_generator_config.get("llm_model")
        if is_local:
            model_name = "User provided local model"

        llm_backend = LLMBackend(
            is_local=is_local,
            temperature=self.config_conversation.get("creativity", 1),
            max_output_tokens=self.content_generator_config.get(
                "max_output_tokens", 8192
            ),
            model_name=model_name,
            api_key_label=api_key_label,
        )

        self.llm = llm_backend.llm



        # Initialize strategies with configs
        self.strategies = {
            True: LongFormContentStrategy(
                self.llm,
                self.content_generator_config,
                self.config_conversation
            ),
            False: StandardContentStrategy(
                self.llm,
                self.content_generator_config,
                self.config_conversation
            )
        }

    def __compose_prompt(self, num_images: int, longform: bool=False):
        """
        Compose the prompt for the LLM based on the content list.
        """
        content_generator_config = self.config.get("content_generator", {})
        
        # Get base template and commit values
        base_template = content_generator_config.get("prompt_template")
        base_commit = content_generator_config.get("prompt_commit")
        
        # Modify template and commit for longform if configured
        if longform:
            template = content_generator_config.get("longform_prompt_template")
            commit = content_generator_config.get("longform_prompt_commit")
        else:
            template = base_template
            commit = base_commit

        prompt_template = hub.pull(f"{template}:{commit}")

        image_path_keys = []
        messages = []

        # Only add text content if input_text is not empty
        text_content = {
            "type": "text",
            "text": "Please analyze this input and generate a conversation. {input_text}",
        }
        messages.append(text_content)

        for i in range(num_images):
            key = f"image_path_{i}"
            image_content = {
                "image_url": {"url": f"{{{key}}}", "detail": "high"},
                "type": "image_url",
            }
            image_path_keys.append(key)
            messages.append(image_content)

        user_prompt_template = ChatPromptTemplate.from_messages(
            messages=[HumanMessagePromptTemplate.from_template(messages)]
        )
        user_instructions = self.config_conversation.get("user_instructions", "")

        user_instructions = (
            "[[MAKE SURE TO FOLLOW THESE INSTRUCTIONS OVERRIDING THE PROMPT TEMPLATE IN CASE OF CONFLICT: "
            + user_instructions
            + "]]"
        )

        new_system_message = (
            prompt_template.messages[0].prompt.template + "\n" + user_instructions
        )

        # Compose messages from podcastfy_prompt_template and user_prompt_template
        combined_messages = (
            ChatPromptTemplate.from_messages([new_system_message]).messages
            + user_prompt_template.messages
        )

        # Create a new ChatPromptTemplate object with the combined messages
        composed_prompt_template = ChatPromptTemplate.from_messages(combined_messages)

        return composed_prompt_template, image_path_keys

    def generate_qa_content(
        self,
        input_texts: str = "",
        image_file_paths: List[str] = [],
        output_filepath: Optional[str] = None,
        longform: bool = False
    ) -> str:
        """
        Generate Q&A content based on input texts.

        Args:
            input_texts (str): Input texts to generate content from.
            image_file_paths (List[str]): List of image file paths.
            output_filepath (Optional[str]): Filepath to save the response content.
            is_local (bool): Whether to use a local LLM or not.
            model_name (str): Model name to use for generation.
            api_key_label (str): Environment variable name for API key.
            longform (bool): Whether to generate long-form content. Defaults to False.

        Returns:
            str: Generated conversation content

        Raises:
            ValueError: If strategy validation fails
            Exception: If there's an error in generating content.
        """
        try:
            # Get appropriate strategy
            strategy = self.strategies[longform]
            
            # Validate inputs for chosen strategy
            strategy.validate(input_texts, image_file_paths)

            # Setup chain
            num_images = 0 if self.is_local else len(image_file_paths)
            self.prompt_template, image_path_keys = self.__compose_prompt(num_images, longform)
            self.parser = StrOutputParser()
            self.chain = self.prompt_template | self.llm | self.parser


            # Prepare parameters using strategy
            prompt_params = strategy.compose_prompt_params(
                self.config_conversation,
                image_file_paths,
                image_path_keys,
                input_texts
            )

            # Generate content using selected strategy
            self.response = strategy.generate(
                self.chain,
                input_texts,
                prompt_params
            )

            # Clean response using the same strategy
            self.response = strategy.clean(
                self.response,
                self.content_generator_config
            )
                
            logger.info(f"Content generated successfully")

            # Save output if requested
            if output_filepath:
                with open(output_filepath, "w") as file:
                    file.write(self.response)
                logger.info(f"Response content saved to {output_filepath}")
                print(f"Transcript saved to {output_filepath}")

            return self.response
            
        except Exception as e:
            logger.error(f"Error generating content: {str(e)}")
            raise
```

## File: `podcastfy/conversation_config.yaml`
```yaml
conversation_style: 
  - "engaging"
  - "fast-paced"
  - "enthusiastic"
roles_person1: "main summarizer"
roles_person2: "questioner/clarifier"
dialogue_structure: 
  - "Introduction"
  - "Main Content Summary"
  - "Conclusion"
podcast_name: "PODCASTIFY"
podcast_tagline: "Your Personal Generative AI Podcast"
output_language: "English"
engagement_techniques: 
  - "rhetorical questions"
  - "anecdotes"
  - "analogies"
  - "humor"
creativity: 1
user_instructions: ""
max_num_chunks: 8 # maximum number of rounds of discussions in longform
min_chunk_size: 600 # minimum number of characters to generate a round of discussion in longform

text_to_speech:
  default_tts_model: "openai"
  output_directories:
    transcripts: "./data/transcripts"
    audio: "./data/audio"
  elevenlabs:
    default_voices:
      question: "Chris"
      answer: "Jessica"
    model: "eleven_multilingual_v2"
  openai:
    default_voices:
      question: "echo"
      answer: "shimmer"
    model: "tts-1-hd"
  edge:
    default_voices:
      question: "en-US-JennyNeural"
      answer: "en-US-EricNeural"
  gemini:
    default_voices:
      question: "en-US-Journey-D"
      answer: "en-US-Journey-O"
  geminimulti:
    default_voices:
      question: "R"
      answer: "S"
      model: "en-US-Studio-MultiSpeaker"
  audio_format: "mp3"
  temp_audio_dir: "data/audio/tmp/"
  ending_message: "See You Next Time!"
```

## File: `podcastfy/text_to_speech.py`
```python
"""
Text-to-Speech Module for converting text into speech using various providers.

This module provides functionality to convert text into speech using various TTS models.
It supports ElevenLabs, Google, OpenAI and Edge TTS services and handles the conversion process,
including cleaning of input text and merging of audio files.
"""

import io
import logging
import os
import re
import tempfile
from typing import List, Tuple, Optional, Dict, Any
from pydub import AudioSegment

from .tts.factory import TTSProviderFactory
from .utils.config import load_config
from .utils.config_conversation import load_conversation_config

logger = logging.getLogger(__name__)


class TextToSpeech:
    def __init__(
        self,
        model: str = None,
        api_key: Optional[str] = None,
        conversation_config: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize the TextToSpeech class.

        Args:
                        model (str): The model to use for text-to-speech conversion.
                                                Options are 'elevenlabs', 'gemini', 'openai', 'edge' or 'geminimulti'. Defaults to 'openai'.
                        api_key (Optional[str]): API key for the selected text-to-speech service.
                        conversation_config (Optional[Dict]): Configuration for conversation settings.
        """
        self.config = load_config()
        self.conversation_config = load_conversation_config(conversation_config)
        self.tts_config = self.conversation_config.get("text_to_speech", {})

        # Get API key from config if not provided
        if not api_key:
            api_key = getattr(self.config, f"{model.upper().replace('MULTI', '')}_API_KEY", None)

        # Initialize provider using factory
        self.provider = TTSProviderFactory.create(
            provider_name=model, api_key=api_key, model=model
        )

        # Setup directories and config
        self._setup_directories()
        self.audio_format = self.tts_config.get("audio_format", "mp3")
        self.ending_message = self.tts_config.get("ending_message", "")

    def _get_provider_config(self) -> Dict[str, Any]:
        """Get provider-specific configuration."""
        # Get provider name in lowercase without 'TTS' suffix
        provider_name = self.provider.__class__.__name__.lower().replace("tts", "")

        # Get provider config from tts_config
        provider_config = self.tts_config.get(provider_name, {})

        # If provider config is empty, try getting from default config
        if not provider_config:
            provider_config = {
                "model": self.tts_config.get("default_model"),
                "default_voices": {
                    "question": self.tts_config.get("default_voice_question"),
                    "answer": self.tts_config.get("default_voice_answer"),
                },
            }

        logger.debug(f"Using provider config: {provider_config}")
        return provider_config

    def convert_to_speech(self, text: str, output_file: str) -> None:
        """
        Convert input text to speech and save as an audio file.

        Args:
                text (str): Input text to convert to speech.
                output_file (str): Path to save the output audio file.

        Raises:
            ValueError: If the input text is not properly formatted
        """
        # Validate transcript format
        # self._validate_transcript_format(text)

        cleaned_text = text

        try:

            if (
                "multi" in self.provider.model.lower()
            ):  # refactor: We should have instead MultiSpeakerTTS and SingleSpeakerTTS classes
                provider_config = self._get_provider_config()
                voice = provider_config.get("default_voices", {}).get("question")
                voice2 = provider_config.get("default_voices", {}).get("answer")
                model = provider_config.get("model")
                audio_data_list = self.provider.generate_audio(
                    cleaned_text,
                    voice="S",
                    model="en-US-Studio-MultiSpeaker",
                    voice2="R",
                    ending_message=self.ending_message,
                )

                try:
                    # First verify we have data
                    if not audio_data_list:
                        raise ValueError("No audio data chunks provided")

                    logger.info(f"Starting audio processing with {len(audio_data_list)} chunks")
                    combined = AudioSegment.empty()
                    
                    for i, chunk in enumerate(audio_data_list):
                        # Save chunk to temporary file
                        #temp_file = "./tmp.mp3"
                        #with open(temp_file, "wb") as f:
                        #    f.write(chunk)
                        
                        segment = AudioSegment.from_file(io.BytesIO(chunk))
                        logger.info(f"################### Loaded chunk {i}, duration: {len(segment)}ms")
                        
                        combined += segment
                    
                    # Export with high quality settings
                    os.makedirs(os.path.dirname(output_file), exist_ok=True)
                    combined.export(
                        output_file, 
                        format=self.audio_format,
                        codec="libmp3lame",
                        bitrate="320k"
                    )
                    
                except Exception as e:
                    logger.error(f"Error during audio processing: {str(e)}")
                    raise
            else:
                with tempfile.TemporaryDirectory(dir=self.temp_audio_dir) as temp_dir:
                    audio_segments = self._generate_audio_segments(
                        cleaned_text, temp_dir
                    )
                    self._merge_audio_files(audio_segments, output_file)
                    logger.info(f"Audio saved to {output_file}")

        except Exception as e:
            logger.error(f"Error converting text to speech: {str(e)}")
            raise

    def _generate_audio_segments(self, text: str, temp_dir: str) -> List[str]:
        """Generate audio segments for each Q&A pair."""
        qa_pairs = self.provider.split_qa(
            text, self.ending_message, self.provider.get_supported_tags()
        )
        audio_files = []
        provider_config = self._get_provider_config()

        for idx, (question, answer) in enumerate(qa_pairs, 1):
            for speaker_type, content in [("question", question), ("answer", answer)]:
                temp_file = os.path.join(
                    temp_dir, f"{idx}_{speaker_type}.{self.audio_format}"
                )
                voice = provider_config.get("default_voices", {}).get(speaker_type)
                model = provider_config.get("model")

                audio_data = self.provider.generate_audio(content, voice, model)
                with open(temp_file, "wb") as f:
                    f.write(audio_data)
                audio_files.append(temp_file)

        return audio_files

    def _merge_audio_files(self, audio_files: List[str], output_file: str) -> None:
        """
        Merge the provided audio files sequentially, ensuring questions come before answers.

        Args:
                audio_files: List of paths to audio files to merge
                output_file: Path to save the merged audio file
        """
        try:

            def get_sort_key(file_path: str) -> Tuple[int, int]:
                """
                Create sort key from filename that puts questions before answers.
                Example filenames: "1_question.mp3", "1_answer.mp3"
                """
                basename = os.path.basename(file_path)
                # Extract the index number and type (question/answer)
                idx = int(basename.split("_")[0])
                is_answer = basename.split("_")[1].startswith("answer")
                return (
                    idx,
                    1 if is_answer else 0,
                )  # Questions (0) come before answers (1)

            # Sort files by index and type (question/answer)
            audio_files.sort(key=get_sort_key)

            # Create empty audio segment
            combined = AudioSegment.empty()

            # Add each audio file to the combined segment
            for file_path in audio_files:
                combined += AudioSegment.from_file(file_path, format=self.audio_format)

            # Ensure output directory exists
            os.makedirs(os.path.dirname(output_file), exist_ok=True)

            # Export the combined audio
            combined.export(output_file, format=self.audio_format)
            logger.info(f"Merged audio saved to {output_file}")

        except Exception as e:
            logger.error(f"Error merging audio files: {str(e)}")
            raise

    def _setup_directories(self) -> None:
        """Setup required directories for audio processing."""
        self.output_directories = self.tts_config.get("output_directories", {})
        temp_dir = self.tts_config.get("temp_audio_dir", "data/audio/tmp/").rstrip("/").split("/")
        self.temp_audio_dir = os.path.join(*temp_dir)
        base_dir = os.path.abspath(os.path.dirname(__file__))
        self.temp_audio_dir = os.path.join(base_dir, self.temp_audio_dir)

        os.makedirs(self.temp_audio_dir, exist_ok=True)

        # Create directories if they don't exist
        for dir_path in [
            self.output_directories.get("transcripts"),
            self.output_directories.get("audio"),
            self.temp_audio_dir,
        ]:
            if dir_path and not os.path.exists(dir_path):
                os.makedirs(dir_path)

    def _validate_transcript_format(self, text: str) -> None:
        """
        Validate that the input text follows the correct transcript format.

        Args:
            text (str): Input text to validate

        Raises:
            ValueError: If the text is not properly formatted

        The text should:
        1. Have alternating Person1 and Person2 tags
        2. Each opening tag should have a closing tag
        3. Tags should be properly nested
        """
        try:
            # Check for empty text
            if not text.strip():
                raise ValueError("Input text is empty")

            # Check for matching opening and closing tags
            person1_open = text.count("<Person1>")
            person1_close = text.count("</Person1>")
            person2_open = text.count("<Person2>")
            person2_close = text.count("</Person2>")

            if person1_open != person1_close:
                raise ValueError(
                    f"Mismatched Person1 tags: {person1_open} opening tags and {person1_close} closing tags"
                )
            if person2_open != person2_close:
                raise ValueError(
                    f"Mismatched Person2 tags: {person2_open} opening tags and {person2_close} closing tags"
                )

            # Check for alternating pattern using regex
            pattern = r"<Person1>.*?</Person1>\s*<Person2>.*?</Person2>"
            matches = re.findall(pattern, text, re.DOTALL)

            # Calculate expected number of pairs
            expected_pairs = min(person1_open, person2_open)

            if len(matches) != expected_pairs:
                raise ValueError(
                    "Tags are not properly alternating between Person1 and Person2. "
                    "Each Person1 section should be followed by a Person2 section."
                )

                # Check for malformed tags (unclosed or improperly nested)
                stack = []
                for match in re.finditer(r"<(/?)Person([12])>", text):
                    tag = match.group(0)
                    if tag.startswith("</"):
                        if not stack or stack[-1] != tag[2:-1]:
                            raise ValueError(f"Improperly nested tags near: {tag}")
                        stack.pop()
                    else:
                        stack.append(tag[1:-1])

                if stack:
                    raise ValueError(f"Unclosed tags: {', '.join(stack)}")

            logger.debug("Transcript format validation passed")

        except ValueError as e:
            logger.error(f"Transcript format validation failed: {str(e)}")
            raise
        except Exception as e:
            logger.error(f"Unexpected error during transcript validation: {str(e)}")
            raise ValueError(f"Invalid transcript format: {str(e)}")


def main(seed: int = 42) -> None:
    """
    Main function to test the TextToSpeech class.

    Args:
            seed (int): Random seed for reproducibility. Defaults to 42.
    """
    try:
        # Load configuration
        config = load_config()

        # Override default TTS model to use edge for tests
        test_config = {"text_to_speech": {"default_tts_model": "edge"}}

        # Read input text from file
        with open(
            "tests/data/transcript_336aa9f955cd4019bc1287379a5a2820.txt", "r"
        ) as file:
            input_text = file.read()

        # Test ElevenLabs
        tts_elevenlabs = TextToSpeech(model="elevenlabs")
        elevenlabs_output_file = "tests/data/response_elevenlabs.mp3"
        tts_elevenlabs.convert_to_speech(input_text, elevenlabs_output_file)
        logger.info(
            f"ElevenLabs TTS completed. Output saved to {elevenlabs_output_file}"
        )

        # Test OpenAI
        tts_openai = TextToSpeech(model="openai")
        openai_output_file = "tests/data/response_openai.mp3"
        tts_openai.convert_to_speech(input_text, openai_output_file)
        logger.info(f"OpenAI TTS completed. Output saved to {openai_output_file}")

        # Test Edge
        tts_edge = TextToSpeech(model="edge")
        edge_output_file = "tests/data/response_edge.mp3"
        tts_edge.convert_to_speech(input_text, edge_output_file)
        logger.info(f"Edge TTS completed. Output saved to {edge_output_file}")

    except Exception as e:
        logger.error(f"An error occurred during text-to-speech conversion: {str(e)}")
        raise


if __name__ == "__main__":
    main(seed=42)
```

## File: `podcastfy/api/fast_app.py`
```python
"""
FastAPI implementation for Podcastify podcast generation service.

This module provides REST endpoints for podcast generation and audio serving,
with configuration management and temporary file handling.
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import os
import shutil
import yaml
from typing import Dict, Any
from pathlib import Path
from ..client import generate_podcast
import uvicorn


def load_base_config() -> Dict[Any, Any]:
    config_path = Path(__file__).parent / "podcastfy" / "conversation_config.yaml"
    try:
        with open(config_path, 'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        print(f"Warning: Could not load base config: {e}")
        return {}

def merge_configs(base_config: Dict[Any, Any], user_config: Dict[Any, Any]) -> Dict[Any, Any]:
    """Merge user configuration with base configuration, preferring user values."""
    merged = base_config.copy()
    
    # Handle special cases for nested dictionaries
    if 'text_to_speech' in merged and 'text_to_speech' in user_config:
        merged['text_to_speech'].update(user_config.get('text_to_speech', {}))
    
    # Update top-level keys
    for key, value in user_config.items():
        if key != 'text_to_speech':  # Skip text_to_speech as it's handled above
            if value is not None:  # Only update if value is not None
                merged[key] = value
                
    return merged

app = FastAPI()

TEMP_DIR = os.path.join(os.path.dirname(__file__), "temp_audio")
os.makedirs(TEMP_DIR, exist_ok=True)

@app.post("/generate")
def generate_podcast_endpoint(data: dict):
    """"""
    try:
        # Set environment variables
        os.environ['OPENAI_API_KEY'] = data.get('openai_key')
        os.environ['GEMINI_API_KEY'] = data.get('google_key')
        os.environ['ELEVENLABS_API_KEY'] = data.get('elevenlabs_key')

        # Load base configuration
        base_config = load_base_config()
        
        # Get TTS model and its configuration from base config
        tts_model = data.get('tts_model', base_config.get('text_to_speech', {}).get('default_tts_model', 'openai'))
        tts_base_config = base_config.get('text_to_speech', {}).get(tts_model, {})
        
        # Get voices (use user-provided voices or fall back to defaults)
        voices = data.get('voices', {})
        default_voices = tts_base_config.get('default_voices', {})
        
        # Prepare user configuration
        user_config = {
            'creativity': float(data.get('creativity', base_config.get('creativity', 0.7))),
            'conversation_style': data.get('conversation_style', base_config.get('conversation_style', [])),
            'roles_person1': data.get('roles_person1', base_config.get('roles_person1')),
            'roles_person2': data.get('roles_person2', base_config.get('roles_person2')),
            'dialogue_structure': data.get('dialogue_structure', base_config.get('dialogue_structure', [])),
            'podcast_name': data.get('name', base_config.get('podcast_name')),
            'podcast_tagline': data.get('tagline', base_config.get('podcast_tagline')),
            'output_language': data.get('output_language', base_config.get('output_language', 'English')),
            'user_instructions': data.get('user_instructions', base_config.get('user_instructions', '')),
            'engagement_techniques': data.get('engagement_techniques', base_config.get('engagement_techniques', [])),
            'text_to_speech': {
                'default_tts_model': tts_model,
                'model': tts_base_config.get('model'),
                'default_voices': {
                    'question': voices.get('question', default_voices.get('question')),
                    'answer': voices.get('answer', default_voices.get('answer'))
                }
            }
        }

        # print(user_config)

        # Merge configurations
        conversation_config = merge_configs(base_config, user_config)

        # print(conversation_config)
        

        # Generate podcast
        result = generate_podcast(
            urls=data.get('urls', []),
            conversation_config=conversation_config,
            tts_model=tts_model,
            longform=bool(data.get('is_long_form', False)),
        )
        # Handle the result
        if isinstance(result, str) and os.path.isfile(result):
            filename = f"podcast_{os.urandom(8).hex()}.mp3"
            output_path = os.path.join(TEMP_DIR, filename)
            shutil.copy2(result, output_path)
            return {"audioUrl": f"/audio/{filename}"}
        elif hasattr(result, 'audio_path'):
            filename = f"podcast_{os.urandom(8).hex()}.mp3"
            output_path = os.path.join(TEMP_DIR, filename)
            shutil.copy2(result.audio_path, output_path)
            return {"audioUrl": f"/audio/{filename}"}
        else:
            raise HTTPException(status_code=500, detail="Invalid result format")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/audio/{filename}")
def serve_audio(filename: str):
    """ Get File Audio From ther Server"""
    file_path = os.path.join(TEMP_DIR, filename)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(file_path)

@app.get("/health")
def healthcheck():
    return {"status": "healthy"}

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8080))
    uvicorn.run(app, host=host, port=port)
```

## File: `podcastfy/content_parser/__init__.py`
```python
# This file can be left empty for now
```

## File: `podcastfy/content_parser/content_extractor.py`
```python
"""
Content Extractor Module

This module provides functionality to extract content from various sources including
websites, YouTube videos, and PDF files. It serves as a central hub for content
extraction, delegating to specialized extractors based on the source type.
"""

import logging
import re
from typing import List, Union
from urllib.parse import urlparse
from .youtube_transcriber import YouTubeTranscriber
from .website_extractor import WebsiteExtractor
from .pdf_extractor import PDFExtractor
from podcastfy.utils.config import load_config
from google import genai
from google.genai import types

logger = logging.getLogger(__name__)

class ContentExtractor:
	def __init__(self):
		"""
		Initialize the ContentExtractor.
		"""
		self.youtube_transcriber = YouTubeTranscriber()
		self.website_extractor = WebsiteExtractor()
		self.pdf_extractor = PDFExtractor()
		self.config = load_config()
		self.content_extractor_config = self.config.get('content_extractor', {})

	def is_url(self, source: str) -> bool:
		"""
		Check if the given source is a valid URL.

		Args:
			source (str): The source to check.

		Returns:
			bool: True if the source is a valid URL, False otherwise.
		"""
		try:
			# If the source doesn't start with a scheme, add 'https://'
			if not source.startswith(('http://', 'https://')):
				source = 'https://' + source

			result = urlparse(source)
			return all([result.scheme, result.netloc])
		except ValueError:
			return False

	def extract_content(self, source: str) -> str:
		"""
		Extract content from various sources.

		Args:
			source (str): URL or file path of the content source.

		Returns:
			str: Extracted text content.

		Raises:
			ValueError: If the source type is unsupported.
		"""
		try:
			if source.lower().endswith('.pdf'):
				return self.pdf_extractor.extract_content(source)
			elif self.is_url(source):
				if any(pattern in source for pattern in self.content_extractor_config['youtube_url_patterns']):
					return self.youtube_transcriber.extract_transcript(source)
				else:
					return self.website_extractor.extract_content(source)
			else:
				raise ValueError("Unsupported source type")
		except Exception as e:
			logger.error(f"Error extracting content from {source}: {str(e)}")
			raise
	
	def generate_topic_content(self, topic: str) -> str:
		"""
		Generate content based on a given topic using Gemini's Google Search grounding.

		Args:
			topic (str): The topic to generate content for.

		Returns:
			str: Generated content based on the topic.
		"""
		try:
			client = genai.Client()
			
			grounding_tool = types.Tool(
				google_search=types.GoogleSearch()
			)
			
			config = types.GenerateContentConfig(
				tools=[grounding_tool]
			)
			
			prompt = f"""Search the web for comprehensive, up-to-date information about {topic}. 
						Provide a detailed, well-structured overview covering:
						- Key concepts and definitions
						- Recent developments and trends
						- Important facts and statistics
						- Different perspectives or viewpoints
						
						Be thorough, accurate, and cite sources when relevant."""
			
			logger.info(f"Generating content with Google Search grounding for topic: {topic}")
			response = client.models.generate_content(
				model="gemini-2.5-flash",
				contents=prompt,
				config=config
			)
			
			return response.text
		except Exception as e:
			logger.error(f"Error generating content for topic '{topic}': {str(e)}")
			raise
		

def main(seed: int = 42) -> None:
	"""
	Main function to test the ContentExtractor class.
	"""
	logging.basicConfig(level=logging.INFO)

	# Create an instance of ContentExtractor
	extractor = ContentExtractor()

	# Test sources
	test_sources: List[str] = [
		"www.souzatharsis.com",
		"https://www.youtube.com/watch?v=dQw4w9WgXcQ",
		"path/to/sample.pdf"
	]

	for source in test_sources:
		try:
			logger.info(f"Extracting content from: {source}")
			content = extractor.extract_content(source)

			# Print the first 500 characters of the extracted content
			logger.info(f"Extracted content (first 500 characters):\n{content[:500]}...")

			# Print the total length of the extracted content
			logger.info(f"Total length of extracted content: {len(content)} characters")
			logger.info("-" * 50)

		except Exception as e:
			logger.error(f"An error occurred while processing {source}: {str(e)}")

if __name__ == "__main__":
	main()
```

## File: `podcastfy/content_parser/pdf_extractor.py`
```python
"""
PDF Extractor Module

This module provides functionality to extract text content from PDF files.
It handles the reading of PDF files, text extraction, and normalization of
the extracted content, including handling of special characters and accents.
"""

import pymupdf
import logging
import os
import unicodedata

logger = logging.getLogger(__name__)

class PDFExtractor:
	def extract_content(self, file_path: str) -> str:
		"""
		Extract text content from a PDF file, handling foreign characters and special characters.
		Accents are removed from the text.

		Args:
			file_path (str): Path to the PDF file.

		Returns:
			str: Extracted text content with accents removed and properly handled characters.
		"""
		try:
			doc = pymupdf.open(file_path)
			content = " ".join(page.get_text() for page in doc)
			doc.close()
			
			# Normalize the text to handle special characters and remove accents
			normalized_content = unicodedata.normalize('NFKD', content)

			return normalized_content
		except Exception as e:
			logger.error(f"Error extracting PDF content: {str(e)}")
			raise

def main(seed: int = 42) -> None:
	"""
	Test the PDFExtractor class with a specific PDF file.

	Args:
		seed (int): Random seed for reproducibility. Defaults to 42.
	"""
	# Set the random seed
	import random
	random.seed(seed)

	# Get the absolute path of the script
	script_dir = os.path.dirname(os.path.abspath(__file__))
	
	# Construct the path to the PDF file
	pdf_path = os.path.join(script_dir, '..', '..', 'tests', 'data', 'file.pdf')
	
	extractor = PDFExtractor()

	try:
		content = extractor.extract_content(pdf_path)
		print("PDF content extracted successfully:")
		print(content[:500] + "..." if len(content) > 500 else content)
	except Exception as e:
		print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
	main()
```

## File: `podcastfy/content_parser/website_extractor.py`
```python
"""
Website Extractor Module

This module is responsible for extracting clean text content from websites using
Playwright to retrieve rendered HTML and BeautifulSoup for local parsing.
"""

import requests
import re
import html
import logging
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from podcastfy.utils.config import load_config
from typing import List
from playwright.sync_api import sync_playwright

logger = logging.getLogger(__name__)

class WebsiteExtractor:
	def __init__(self):
		"""
		Initialize the WebsiteExtractor.
		"""
		self.config = load_config()
		self.website_extractor_config = self.config.get('website_extractor', {})
		self.unwanted_tags = self.website_extractor_config.get('unwanted_tags', [])
		self.user_agent = self.website_extractor_config.get('user_agent', 'Mozilla/5.0')
		self.timeout = self.website_extractor_config.get('timeout', 10)
		self.remove_patterns = self.website_extractor_config.get('markdown_cleaning', {}).get('remove_patterns', [])

	def extract_content(self, url: str) -> str:
		"""
		Extract clean text content from a website using BeautifulSoup.

		Args:
			url (str): Website URL.

		Returns:
			str: Extracted clean text content.

		Raises:
			Exception: If there's an error in extracting the content.
		"""
		try:
			# Normalize the URL
			normalized_url = self.normalize_url(url)

			# Fetch the page HTML using Playwright (handles bot detection and JS rendering)
			html_content = self.fetch_with_playwright(normalized_url)

			# Parse the page content with BeautifulSoup
			soup = BeautifulSoup(html_content, 'html.parser')

			# Remove unwanted elements
			self.remove_unwanted_elements(soup)

			# Extract and clean the text content
			raw_text = soup.get_text(separator="\n")  # Get all text content
			cleaned_content = self.clean_content(raw_text)

			return cleaned_content
		except requests.RequestException as e:
			logger.error(f"Failed to extract content from {url}: {str(e)}")
			raise Exception(f"Failed to extract content from {url}: {str(e)}")
		except Exception as e:
			logger.error(f"An unexpected error occurred while extracting content from {url}: {str(e)}")
			raise Exception(f"An unexpected error occurred while extracting content from {url}: {str(e)}")

	def fetch_with_playwright(self, url: str) -> str:
		"""
		Use Playwright to navigate to the URL and return the rendered HTML.

		Args:
			url (str): The URL to fetch.

		Returns:
			str: The page HTML after network is idle.
		"""
		try:
			with sync_playwright() as p:
				browser = p.chromium.launch(headless=True)
				context = browser.new_context(
					user_agent=self.user_agent,
					ignore_https_errors=True,
				)
				page = context.new_page()
				# Extra headers to mimic a real browser
				page.set_extra_http_headers({
					"Accept-Language": "en-US,en;q=0.9",
				})
				page.goto(url, wait_until="networkidle", timeout=self.timeout * 1000)
				# Optionally wait for DOM to be ready
				page.wait_for_timeout(500)
				html_content = page.content()
				context.close()
				browser.close()
				return html_content
		except Exception as e:
			if "asyncio loop" in str(e).lower() or "async" in str(e).lower():
				return self.fetch_with_requests(url)
			raise Exception(f"An unexpected error occurred while extracting content from {url}: {str(e)}")
	def fetch_with_requests(self, url: str) -> str:
		"""
		Fallback method using requests when Playwright fails in async contexts.
		"""
		logger.warning(f"Playwright failed in async context, using requests: {url}")
		headers = {
			'User-Agent': self.user_agent,
			'Accept-Language': 'en-US,en;q=0.9',
		}
		response = requests.get(url, headers=headers, timeout=self.timeout)
		return response.text
	def normalize_url(self, url: str) -> str:
		"""
		Normalize the given URL by adding scheme if missing and ensuring it's a valid URL.

		Args:
			url (str): The URL to normalize.

		Returns:
			str: The normalized URL.

		Raises:
			ValueError: If the URL is invalid after normalization attempts.
		"""
		# If the URL doesn't start with a scheme, add 'https://'
		if not url.startswith(('http://', 'https://')):
			url = 'https://' + url

		# Parse the URL
		parsed = urlparse(url)

		# Ensure the URL has a valid scheme and netloc
		if not all([parsed.scheme, parsed.netloc]):
			raise ValueError(f"Invalid URL: {url}")

		return parsed.geturl()

	def remove_unwanted_elements(self, soup: BeautifulSoup) -> None:
		"""
		Remove unwanted elements from the BeautifulSoup object.

		Args:
			soup (BeautifulSoup): The BeautifulSoup object to clean.
		"""
		for tag in self.unwanted_tags:
			for element in soup.find_all(tag):
				element.decompose()

	def clean_content(self, content: str) -> str:
		"""
		Clean the extracted content by removing unnecessary whitespace and applying
		custom cleaning patterns.

		Args:
			content (str): The content to clean.

		Returns:
			str: Cleaned text content.
		"""
		# Decode HTML entities
		cleaned_content = html.unescape(content)

		# Remove extra whitespace
		cleaned_content = re.sub(r'\s+', ' ', cleaned_content)

		# Remove extra newlines
		cleaned_content = re.sub(r'\n{3,}', '\n\n', cleaned_content)

		# Apply custom cleaning patterns from config
		for pattern in self.remove_patterns:
			cleaned_content = re.sub(pattern, '', cleaned_content)

		return cleaned_content.strip()

def main(seed: int = 42) -> None:
	"""
	Main function to test the WebsiteExtractor class.
	"""
	logging.basicConfig(level=logging.INFO)

	# Create an instance of WebsiteExtractor
	extractor = WebsiteExtractor()

	# Test URLs
	test_urls: List[str] = [
		"www.souzatharsis.com",
		"https://en.wikipedia.org/wiki/Web_scraping"
	]

	for url in test_urls:
		try:
			logger.info(f"Extracting content from: {url}")
			content = extractor.extract_content(url)

			# Print the first 500 characters of the extracted content
			logger.info(f"Extracted content (first 500 characters):\n{content[:500]}...")

			# Print the total length of the extracted content
			logger.info(f"Total length of extracted content: {len(content)} characters")
			logger.info("-" * 50)

		except Exception as e:
			logger.error(f"An error occurred while processing {url}: {str(e)}")

if __name__ == "__main__":
	main()
```

## File: `podcastfy/content_parser/youtube_transcriber.py`
```python
"""
YouTube Transcriber Module

This module is responsible for extracting and cleaning transcripts from YouTube videos.
It uses the YouTube Transcript API to fetch transcripts and provides functionality
to clean and format the extracted text.
"""

from youtube_transcript_api import YouTubeTranscriptApi
import logging
from podcastfy.utils.config import load_config

logger = logging.getLogger(__name__)

class YouTubeTranscriber:
	def __init__(self):
		self.config = load_config()
		self.youtube_transcriber_config = self.config.get('youtube_transcriber')

	def extract_transcript(self, url: str) -> str:
		"""
		Extract transcript from a YouTube video and remove '[music]' tags (case-insensitive).

		Args:
			url (str): YouTube video URL.

		Returns:
			str: Cleaned and extracted transcript.
		"""
		try:
			video_id = url.split("v=")[-1]
			transcript = YouTubeTranscriptApi.get_transcript(video_id)
			cleaned_transcript = " ".join([
				entry['text'] for entry in transcript 
				if entry['text'].lower() not in self.youtube_transcriber_config['remove_phrases']
			])
			return cleaned_transcript
		except Exception as e:
			logger.error(f"Error extracting YouTube transcript: {str(e)}")
			raise

def main(seed: int = 42) -> None:
	"""
	Test the YouTubeTranscriber class with a specific URL and save the transcript.

	Args:
		seed (int): Random seed for reproducibility. Defaults to 42.
	"""
	url = "https://www.youtube.com/watch?v=nFbJCoTK0_g"
	transcriber = YouTubeTranscriber()

	try:
		transcript = transcriber.extract_transcript(url)
		print("Transcript extracted successfully.")
		
		# Save transcript to file
		output_file = 'tests/data/transcripts/youtube_transcript2.txt'
		with open(output_file, 'w') as file:
			file.write(transcript)
		
		print(f"Transcript saved to {output_file}")
		print("First 500 characters of the transcript:")
		print(transcript[:500] + "..." if len(transcript) > 500 else transcript)
	except Exception as e:
		logger.error(f"An error occurred: {str(e)}")
		raise

if __name__ == "__main__":
	main()
```

## File: `podcastfy/tts/base.py`
```python
"""Abstract base class for Text-to-Speech providers."""

from abc import ABC, abstractmethod
from typing import List, ClassVar, Tuple
import re

class TTSProvider(ABC):
    """Abstract base class that defines the interface for TTS providers."""
    
    # Common SSML tags supported by most providers
    COMMON_SSML_TAGS: ClassVar[List[str]] = [
        'lang', 'p', 'phoneme', 's', 'sub'
    ]
    
    @abstractmethod
    def generate_audio(self, text: str, voice: str, model: str, voice2: str) -> bytes:
        """
        Generate audio from text using the provider's API.
        
        Args:
            text: Text to convert to speech
            voice: Voice ID/name to use
            model: Model ID/name to use
            
        Returns:
            Audio data as bytes
            
        Raises:
            ValueError: If invalid parameters are provided
            RuntimeError: If audio generation fails
        """
        pass

    def get_supported_tags(self) -> List[str]:
        """
        Get set of SSML tags supported by this provider.
        
        Returns:
            Set of supported SSML tag names
        """
        return self.COMMON_SSML_TAGS.copy()
    
    def validate_parameters(self, text: str, voice: str, model: str, voice2: str = None) -> None:
        """
        Validate input parameters before generating audio.
        
        Raises:
            ValueError: If any parameter is invalid
        """
        if not text:
            raise ValueError("Text cannot be empty")
        if not voice:
            raise ValueError("Voice must be specified")
        if not model:
            raise ValueError("Model must be specified")
        
    def split_qa(self, input_text: str, ending_message: str, supported_tags: List[str] = None) -> List[Tuple[str, str]]:
        """
        Split the input text into question-answer pairs.

        Args:
            input_text (str): The input text containing Person1 and Person2 dialogues.
            ending_message (str): The ending message to add to the end of the input text.

        Returns:
                List[Tuple[str, str]]: A list of tuples containing (Person1, Person2) dialogues.
        """
        input_text = self.clean_tss_markup(input_text, supported_tags=supported_tags)
        
        # Add placeholder if input_text starts with <Person2>
        if input_text.strip().startswith("<Person2>"):
            input_text = "<Person1> Humm... </Person1>" + input_text

        # Add ending message to the end of input_text
        if input_text.strip().endswith("</Person1>"):
            input_text += f"<Person2>{ending_message}</Person2>"

        # Regular expression pattern to match Person1 and Person2 dialogues
        pattern = r"<Person1>(.*?)</Person1>\s*<Person2>(.*?)</Person2>"

        # Find all matches in the input text
        matches = re.findall(pattern, input_text, re.DOTALL)

        # Process the matches to remove extra whitespace and newlines
        processed_matches = [
            (" ".join(person1.split()).strip(), " ".join(person2.split()).strip())
            for person1, person2 in matches
        ]
        return processed_matches

    def clean_tss_markup(self, input_text: str, additional_tags: List[str] = ["Person1", "Person2"], supported_tags: List[str] = None) -> str:
        """
        Remove unsupported TSS markup tags from the input text while preserving supported SSML tags.

        Args:
            input_text (str): The input text containing TSS markup tags.
            additional_tags (List[str]): Optional list of additional tags to preserve. Defaults to ["Person1", "Person2"].
            supported_tags (List[str]): Optional list of supported tags. If None, use COMMON_SSML_TAGS.
        Returns:
            str: Cleaned text with unsupported TSS markup tags removed.
        """
        if supported_tags is None:
            supported_tags = self.COMMON_SSML_TAGS.copy()

        # Append additional tags to the supported tags list
        supported_tags.extend(additional_tags)

        # Create a pattern that matches any tag not in the supported list
        pattern = r'</?(?!(?:' + '|'.join(supported_tags) + r')\b)[^>]+>'

        # Remove unsupported tags
        cleaned_text = re.sub(pattern, '', input_text)

        # Remove any leftover empty lines
        cleaned_text = re.sub(r'\n\s*\n', '\n', cleaned_text)

        # Ensure closing tags for additional tags are preserved
        for tag in additional_tags:
            cleaned_text = re.sub(f'<{tag}>(.*?)(?=<(?:{"|".join(additional_tags)})>|$)', 
                                f'<{tag}>\\1</{tag}>', 
                                cleaned_text, 
                                flags=re.DOTALL)

        return cleaned_text.strip()
```

## File: `podcastfy/tts/factory.py`
```python
"""Factory for creating TTS providers."""

from typing import Dict, Type, Optional
from .base import TTSProvider
from .providers.elevenlabs import ElevenLabsTTS
from .providers.openai import OpenAITTS
from .providers.edge import EdgeTTS
from .providers.gemini import GeminiTTS
from .providers.geminimulti import GeminiMultiTTS
class TTSProviderFactory:
    """Factory class for creating TTS providers."""
    
    _providers: Dict[str, Type[TTSProvider]] = {
        'elevenlabs': ElevenLabsTTS,
        'openai': OpenAITTS,
        'edge': EdgeTTS,
        'gemini': GeminiTTS,
        'geminimulti': GeminiMultiTTS
    }
    
    @classmethod
    def create(cls, provider_name: str, api_key: Optional[str] = None, model: Optional[str] = None) -> TTSProvider:
        """
        Create a TTS provider instance.
        
        Args:
            provider_name: Name of the provider to create
            api_key: Optional API key for the provider
            model: Optional model name for the provider
            
        Returns:
            TTSProvider instance
            
        Raises:
            ValueError: If provider_name is not supported
        """
        provider_class = cls._providers.get(provider_name.lower())
        if not provider_class:
            raise ValueError(f"Unsupported provider: {provider_name}. "
                           f"Choose from: {', '.join(cls._providers.keys())}")
                           
        return provider_class(api_key, model) if api_key else provider_class(model=model)
    
    @classmethod
    def register_provider(cls, name: str, provider_class: Type[TTSProvider]) -> None:
        """Register a new provider class."""
        cls._providers[name.lower()] = provider_class 
```

## File: `podcastfy/tts/providers/edge.py`
```python
"""Edge TTS provider implementation."""

import edge_tts
import os
import tempfile
from typing import List
from ..base import TTSProvider

class EdgeTTS(TTSProvider):
    def __init__(self, api_key: str = None, model: str = None):
        """
        Initialize Edge TTS provider.
        
        Args:
            api_key (str): Not used for Edge TTS
            model (str): Model name to use
        """
        self.model = model or "default"  # Edge TTS doesn't use models, but we set it for consistency

    def generate_audio(self, text: str, voice: str, model: str, voice2: str = None) -> bytes:
        """Generate audio using Edge TTS."""
        import nest_asyncio
        import asyncio
        
        # Apply nest_asyncio to allow nested event loops
        nest_asyncio.apply()
        
        async def _generate():
            communicate = edge_tts.Communicate(text, voice)
            # Create a temporary file with proper context management
            with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as tmp_file:
                temp_path = tmp_file.name
                
            try:
                # Save audio to temporary file
                await communicate.save(temp_path)
                # Read the audio data
                with open(temp_path, 'rb') as f:
                    return f.read()
            finally:
                # Clean up temporary file
                if os.path.exists(temp_path):
                    os.remove(temp_path)

        # Use nest_asyncio to handle nested event loops
        loop = asyncio.get_event_loop()
        return loop.run_until_complete(_generate())
        
    def get_supported_tags(self) -> List[str]:
        """Get supported SSML tags."""
        return self.COMMON_SSML_TAGS
```

## File: `podcastfy/tts/providers/elevenlabs.py`
```python
"""ElevenLabs TTS provider implementation."""

from elevenlabs import client as elevenlabs_client
from ..base import TTSProvider
from typing import List

class ElevenLabsTTS(TTSProvider):
    def __init__(self, api_key: str, model: str = "eleven_multilingual_v2"):
        """
        Initialize ElevenLabs TTS provider.
        
        Args:
            api_key (str): ElevenLabs API key
            model (str): Model name to use. Defaults to "eleven_multilingual_v2"
        """
        self.client = elevenlabs_client.ElevenLabs(api_key=api_key)
        self.model = model
        
    def generate_audio(self, text: str, voice: str, model: str, voice2: str = None) -> bytes:
        """Generate audio using ElevenLabs API."""
        audio = self.client.generate(
            text=text,
            voice=voice,
            model=model
        )
        return b''.join(chunk for chunk in audio if chunk)
        
    def get_supported_tags(self) -> List[str]:
        """Get supported SSML tags."""
        return ['lang', 'p', 'phoneme', 's', 'sub'] 
```

## File: `podcastfy/tts/providers/gemini.py`
```python
"""Google Cloud Text-to-Speech provider implementation for single speaker."""

from google.cloud import texttospeech_v1beta1
from typing import List
from ..base import TTSProvider
import logging

logger = logging.getLogger(__name__)

class GeminiTTS(TTSProvider):
    """Google Cloud Text-to-Speech provider for single speaker."""
    
    def __init__(self, api_key: str = None, model: str = "en-US-Journey-F"):
        """
        Initialize Google Cloud TTS provider.
        
        Args:
            api_key (str): Google Cloud API key
            model (str): Default voice model to use
        """
        self.model = model
        try:
            self.client = texttospeech_v1beta1.TextToSpeechClient(
                client_options={'api_key': api_key} if api_key else None
            )
        except Exception as e:
            logger.error(f"Failed to initialize Google TTS client: {str(e)}")
            raise

    def generate_audio(self, text: str, voice: str = "en-US-Journey-F", 
                      model: str = None, **kwargs) -> bytes:
        """
        Generate audio using Google Cloud TTS API.
        
        Args:
            text (str): Text to convert to speech
            voice (str): Voice ID/name to use (format: "{language-code}-{name}-{gender}")
            model (str): Optional model override
            
        Returns:
            bytes: Audio data
            
        Raises:
            ValueError: If parameters are invalid
            RuntimeError: If audio generation fails
        """
        self.validate_parameters(text, voice, model or self.model)
        
        try:
            # Create synthesis input
            synthesis_input = texttospeech_v1beta1.SynthesisInput(
                text=text
            )
            
            # Parse language code from voice ID (e.g., "en-IN" from "en-IN-Journey-D")
            language_code = "-".join(voice.split("-")[:2])

            voice_params = texttospeech_v1beta1.VoiceSelectionParams(
                language_code=language_code,
                name=voice,
            )
            
            # Set audio config
            audio_config = texttospeech_v1beta1.AudioConfig(
                audio_encoding=texttospeech_v1beta1.AudioEncoding.MP3
            )
            
            # Generate speech
            response = self.client.synthesize_speech(
                input=synthesis_input,
                voice=voice_params,
                audio_config=audio_config
            )
            
            return response.audio_content
            
        except Exception as e:
            logger.error(f"Failed to generate audio: {str(e)}")
            raise RuntimeError(f"Failed to generate audio: {str(e)}") from e
    
    def get_supported_tags(self) -> List[str]:
        """Get supported SSML tags."""
        return self.COMMON_SSML_TAGS
        
    def validate_parameters(self, text: str, voice: str, model: str) -> None:
        """
        Validate input parameters before generating audio.
        
        Args:
            text (str): Input text
            voice (str): Voice ID/name
            model (str): Model name
            
        Raises:
            ValueError: If parameters are invalid
        """
        super().validate_parameters(text, voice, model)
        
        if not text:
            raise ValueError("Text cannot be empty")
        
        if not voice:
            raise ValueError("Voice must be specified")
```

## File: `podcastfy/tts/providers/geminimulti.py`
```python
"""Google Cloud Text-to-Speech provider implementation."""

from google.cloud import texttospeech_v1beta1
from typing import List
from ..base import TTSProvider
import re
import logging
from io import BytesIO
from pydub import AudioSegment

logger = logging.getLogger(__name__)

class GeminiMultiTTS(TTSProvider):
    """Google Cloud Text-to-Speech provider with multi-speaker support."""
    
    def __init__(self, api_key: str = None, model: str = "en-US-Studio-MultiSpeaker"):
        """
        Initialize Google Cloud TTS provider.
        
        Args:
            api_key (str): Google Cloud API key
        """
        self.model = model
        try:
            self.client = texttospeech_v1beta1.TextToSpeechClient(
                client_options={'api_key': api_key} if api_key else None
            )
            logger.info("Successfully initialized GeminiMultiTTS client")
        except Exception as e:
            logger.error(f"Failed to initialize GeminiMultiTTS client: {str(e)}")
            raise
            
    def chunk_text(self, text: str, max_bytes: int = 1300) -> List[str]:
        """
        Split text into chunks that fit within Google TTS byte limit while preserving speaker tags.
        
        Args:
            text (str): Input text with Person1/Person2 tags
            max_bytes (int): Maximum bytes per chunk
            
        Returns:
            List[str]: List of text chunks with proper speaker tags preserved
        """
        logger.debug(f"Starting chunk_text with text length: {len(text)} bytes")
        
        # Split text into tagged sections, preserving both Person1 and Person2 tags
        pattern = r'(<Person[12]>.*?</Person[12]>)'
        sections = re.split(pattern, text, flags=re.DOTALL)
        sections = [s.strip() for s in sections if s.strip()]
        logger.debug(f"Split text into {len(sections)} sections")
        
        chunks = []
        current_chunk = ""
        
        for section in sections:
            # Extract speaker tag and content if this is a tagged section
            tag_match = re.match(r'<(Person[12])>(.*?)</Person[12]>', section, flags=re.DOTALL)
            
            if tag_match:
                speaker_tag = tag_match.group(1)  # Will be either Person1 or Person2
                content = tag_match.group(2).strip()
                
                # Test if adding this entire section would exceed limit
                test_chunk = current_chunk
                if current_chunk:
                    test_chunk += f"<{speaker_tag}>{content}</{speaker_tag}>"
                else:
                    test_chunk = f"<{speaker_tag}>{content}</{speaker_tag}>"
                    
                if len(test_chunk.encode('utf-8')) > max_bytes and current_chunk:
                    # Store current chunk and start new one
                    chunks.append(current_chunk)
                    current_chunk = f"<{speaker_tag}>{content}</{speaker_tag}>"
                else:
                    # Add to current chunk
                    current_chunk = test_chunk
        
        # Add final chunk if it exists
        if current_chunk:
            chunks.append(current_chunk)
            
        logger.info(f"Created {len(chunks)} chunks from input text")
        return chunks

    def split_turn_text(self, text: str, max_chars: int = 500) -> List[str]:
        """
        Split turn text into smaller chunks at sentence boundaries.
        
        Args:
            text (str): Text content of a single turn
            max_chars (int): Maximum characters per chunk
            
        Returns:
            List[str]: List of text chunks
        """
        #print(f"### TEXT: {text}" )
        #print(f"### LENGTH: {len(text)}")
        if len(text) <= max_chars:
            return [text]
        
        chunks = []
        sentences = re.split(r'([.!?]+(?:\s+|$))', text)
        sentences = [s for s in sentences if s]
        
        current_chunk = ""
        for i in range(0, len(sentences), 2):
            sentence = sentences[i]
            separator = sentences[i + 1] if i + 1 < len(sentences) else ""
            complete_sentence = sentence + separator
            
            if len(current_chunk) + len(complete_sentence) > max_chars:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                    current_chunk = complete_sentence
                else:
                    # If a single sentence is too long, split at word boundaries
                    words = complete_sentence.split()
                    temp_chunk = ""
                    for word in words:
                        if len(temp_chunk) + len(word) + 1 > max_chars:
                            chunks.append(temp_chunk.strip())
                            temp_chunk = word
                        else:
                            temp_chunk += " " + word if temp_chunk else word
                    current_chunk = temp_chunk
            else:
                current_chunk += complete_sentence
                
        if current_chunk:
            chunks.append(current_chunk.strip())
            
        return chunks

    def merge_audio(self, audio_chunks: List[bytes]) -> bytes:
        """
        Merge multiple MP3 audio chunks into a single audio file.
        
        Args:
            audio_chunks (List[bytes]): List of MP3 audio data
            
        Returns:
            bytes: Combined MP3 audio data
        """
        if not audio_chunks:
            return b""
        
        if len(audio_chunks) == 1:
            return audio_chunks[0]
        
        try:
            # Initialize combined audio with first chunk
            combined = None
            valid_chunks = []
            
            for i, chunk in enumerate(audio_chunks):
                try:
                    # Ensure chunk is not empty
                    if not chunk or len(chunk) == 0:
                        logger.warning(f"Skipping empty chunk {i}")
                        continue
                    
                    # Save chunk to temporary file for ffmpeg to process
                    temp_file = f"temp_chunk_{i}.mp3"
                    with open(temp_file, "wb") as f:
                        f.write(chunk)
                    
                    # Create audio segment from temp file
                    try:
                        segment = AudioSegment.from_file(temp_file, format="mp3")
                        if len(segment) > 0:
                            valid_chunks.append(segment)
                            logger.debug(f"Successfully processed chunk {i}")
                        else:
                            logger.warning(f"Zero-length segment in chunk {i}")
                    except Exception as e:
                        logger.error(f"Error processing chunk {i}: {str(e)}")
                    
                    # Clean up temp file
                    import os
                    try:
                        os.remove(temp_file)
                    except Exception as e:
                        logger.warning(f"Failed to remove temp file {temp_file}: {str(e)}")
                    
                except Exception as e:
                    logger.error(f"Error handling chunk {i}: {str(e)}")
                    continue
            
            if not valid_chunks:
                raise RuntimeError("No valid audio chunks to merge")
            
            # Merge valid chunks
            combined = valid_chunks[0]
            for segment in valid_chunks[1:]:
                combined = combined + segment
            
            # Export with specific parameters
            output = BytesIO()
            combined.export(
                output,
                format="mp3",
                codec="libmp3lame",
                bitrate="320k"
            )
            
            result = output.getvalue()
            if len(result) == 0:
                raise RuntimeError("Export produced empty output")
            
            return result
            
        except Exception as e:
            logger.error(f"Audio merge failed: {str(e)}", exc_info=True)
            # If merging fails, return the first valid chunk as fallback
            if audio_chunks:
                return audio_chunks[0]
            raise RuntimeError(f"Failed to merge audio chunks and no valid fallback found: {str(e)}")

    def generate_audio(self, text: str, voice: str = "R", model: str = "en-US-Studio-MultiSpeaker", 
                       voice2: str = "S", ending_message: str = ""):
        """
        Generate audio using Google Cloud TTS API with multi-speaker support.
        Handles text longer than 5000 bytes by chunking and merging.
        """
        logger.info(f"Starting audio generation for text of length: {len(text)}")
        logger.debug(f"Parameters: voice={voice}, voice2={voice2}, model={model}")
        #print("######################### TEXT #########################")
        #print(text)
        #print("######################### END TEXT #########################")
        try:
            # Split text into chunks if needed
            text_chunks = self.chunk_text(text)
            logger.info(f"#########################33 Text split into {len(text_chunks)} chunks")
            audio_chunks = []
            #print(text_chunks[0])
            
            # Process each chunk
            for i, chunk in enumerate(text_chunks, 1):
                logger.debug(f"Processing chunk {i}/{len(text_chunks)}")
                # Create multi-speaker markup
                multi_speaker_markup = texttospeech_v1beta1.MultiSpeakerMarkup()
                #print("######################### CHUNK #########################")
                #print(chunk)
                # Get Q&A pairs for this chunk
                qa_pairs = self.split_qa(chunk, "", self.get_supported_tags())
                logger.debug(f"Found {len(qa_pairs)} Q&A pairs in chunk {i}")
                #print("######################### QA PAIRS #########################")
                #print(qa_pairs)
                # Add turns for each Q&A pair
                for j, (question, answer) in enumerate(qa_pairs, 1):
                    logger.debug(f"Processing Q&A pair {j}/{len(qa_pairs)}")
                    
                    # Split question into smaller chunks if needed
                    question_chunks = self.split_turn_text(question.strip())
                    logger.debug(f"Question split into {len(question_chunks)} chunks")
                    logger.debug(f"######################### Question chunks: {question_chunks}")
                    for q_chunk in question_chunks:
                        logger.debug(f"Adding question turn: '{q_chunk[:50]}...' (length: {len(q_chunk)})")
                        q_turn = texttospeech_v1beta1.MultiSpeakerMarkup.Turn()
                        q_turn.text = q_chunk
                        q_turn.speaker = voice
                        multi_speaker_markup.turns.append(q_turn)
                    
                    # Split answer into smaller chunks if needed
                    if answer:
                        answer_chunks = self.split_turn_text(answer.strip())
                        logger.debug(f"Answer split into {len(answer_chunks)} chunks")
                        logger.debug(f"######################### Answer chunks: {answer_chunks}")
                        for a_chunk in answer_chunks:
                            logger.debug(f"Adding answer turn: '{a_chunk[:50]}...' (length: {len(a_chunk)})")
                            a_turn = texttospeech_v1beta1.MultiSpeakerMarkup.Turn()
                            a_turn.text = a_chunk
                            a_turn.speaker = voice2
                            multi_speaker_markup.turns.append(a_turn)
                
                logger.debug(f"Created markup with {len(multi_speaker_markup.turns)} turns")
                
                # Create synthesis input with multi-speaker markup
                synthesis_input = texttospeech_v1beta1.SynthesisInput(
                    multi_speaker_markup=multi_speaker_markup
                )
                
                logger.debug("Calling synthesize_speech API")
                # Set voice parameters
                voice_params = texttospeech_v1beta1.VoiceSelectionParams(
                    language_code="en-US",
                    name=model
                )
                
                # Set audio config
                audio_config = texttospeech_v1beta1.AudioConfig(
                    audio_encoding=texttospeech_v1beta1.AudioEncoding.MP3,
                    #sample_rate_hertz=44100,  # Specify sample rate
                    #effects_profile_id=['headphone-class-device'],  # Optimize for headphones
                    #speaking_rate=1.0,  # Normal speaking rate
                )
                
                # Generate speech for this chunk
                response = self.client.synthesize_speech(
                    input=synthesis_input,
                    voice=voice_params,
                    audio_config=audio_config
                )

                audio_chunks.append(response.audio_content)
            #print(f"#### Audio chunks: {audio_chunks}")
            #print(f"#### Audio chunks length: {len(audio_chunks)}")
            return audio_chunks
        
            
        except Exception as e:
            logger.error(f"Failed to generate audio: {str(e)}", exc_info=True)
            raise RuntimeError(f"Failed to generate audio: {str(e)}") from e
    
    def get_supported_tags(self) -> List[str]:
        """Get supported SSML tags."""
        # Add any Google-specific SSML tags to the common ones
        return self.COMMON_SSML_TAGS
        
    def validate_parameters(self, text: str, voice: str, model: str) -> None:
        """
        Validate input parameters before generating audio.
        
        Args:
            text (str): Input text
            voice (str): Voice ID
            model (str): Model name
            
        Raises:
            ValueError: If parameters are invalid
        """
        super().validate_parameters(text, voice, model)
        
        # Additional validation for multi-speaker model
        if model != "en-US-Studio-MultiSpeaker":
            raise ValueError(
                "Google Multi-speaker TTS requires model='en-US-Studio-MultiSpeaker'"
            )
```

## File: `podcastfy/tts/providers/openai.py`
```python
"""OpenAI TTS provider implementation."""

import openai
from typing import List, Optional
from ..base import TTSProvider

class OpenAITTS(TTSProvider):
    """OpenAI Text-to-Speech provider."""
    
    # Provider-specific SSML tags
    PROVIDER_SSML_TAGS: List[str] = ['break', 'emphasis']
    
    def __init__(self, api_key: Optional[str] = None, model: str = "tts-1-hd"):
        """
        Initialize OpenAI TTS provider.
        
        Args:
            api_key: OpenAI API key. If None, expects OPENAI_API_KEY env variable
            model: Model name to use. Defaults to "tts-1-hd"
        """
        if api_key:
            openai.api_key = api_key
        elif not openai.api_key:
            raise ValueError("OpenAI API key must be provided or set in environment")
        self.model = model
            
    def get_supported_tags(self) -> List[str]:
        """Get all supported SSML tags including provider-specific ones."""
        return self.PROVIDER_SSML_TAGS
        
    def generate_audio(self, text: str, voice: str, model: str, voice2: str = None) -> bytes:
        """Generate audio using OpenAI API."""
        self.validate_parameters(text, voice, model)
        
        try:
            response = openai.audio.speech.create(
                model=model,
                voice=voice,
                input=text
            )
            return response.content
        except Exception as e:
            raise RuntimeError(f"Failed to generate audio: {str(e)}") from e
```

## File: `podcastfy/utils/config.py`
```python
"""
Configuration Module

This module handles the loading and management of configuration settings for the Podcastfy application.
It uses environment variables to securely store and access API keys and other sensitive information,
and a YAML file for non-sensitive configuration settings.
"""

import os
from dotenv import load_dotenv, find_dotenv
from typing import Any, Dict, Optional
import yaml

def get_config_path(config_file: str = 'config.yaml'):
	"""
	Get the path to the config.yaml file.
	
	Returns:
		str: The path to the config.yaml file.
	"""
	try:
		base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
		
		# Look for config.yaml in the package root
		config_path = os.path.join(base_path, config_file)
		if os.path.exists(config_path):
			return config_path
		
		# If not found, look in the current working directory
		config_path = os.path.join(os.getcwd(), config_file)
		if os.path.exists(config_path):
			return config_path
		
		raise FileNotFoundError(f"{config_file} not found")
	
	except Exception as e:
		print(f"Error locating {config_file}: {str(e)}")
		return None

class Config:
	def __init__(self, config_file: str = 'config.yaml'):
		"""
		Initialize the Config class by loading environment variables and YAML configuration.

		Args:
			config_file (str): Path to the YAML configuration file. Defaults to 'config.yaml'.
		"""
		# Try to find .env file
		dotenv_path = find_dotenv(usecwd=True)
		if dotenv_path:
			load_dotenv(dotenv_path)
		else:
			print("Warning: .env file not found. Using environment variables if available.")
		
		# Load API keys from environment variables
		self.GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
		self.OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
		self.ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY", "")
		
		config_path = get_config_path(config_file)
		if config_path:
			with open(config_path, 'r') as file:
				self.config: Dict[str, Any] = yaml.safe_load(file)
		else:
			print("Could not locate config.yaml")
			self.config = {}
		
		# Set attributes based on YAML config
		self._set_attributes()

	def _set_attributes(self):
		"""Set attributes based on the current configuration."""
		for key, value in self.config.items():
			setattr(self, key.upper(), value)

		# Ensure output directories exist
		if 'output_directories' in self.config:
			for dir_type, dir_path in self.config['output_directories'].items():
				os.makedirs(dir_path, exist_ok=True)

	def configure(self, **kwargs):
		"""
		Configure the settings by updating the config dictionary and relevant attributes.

		Args:
			**kwargs: Keyword arguments representing configuration keys and values to update.
		"""
		for key, value in kwargs.items():
			if key in self.config:
				self.config[key] = value
			elif key in ['JINA_API_KEY', 'GEMINI_API_KEY', 'OPENAI_API_KEY', 'ELEVENLABS_API_KEY']:
				setattr(self, key, value)
			else:
				raise ValueError(f"Unknown configuration key: {key}")

		# Update attributes based on the new configuration
		self._set_attributes()

	def get(self, key: str, default: Optional[Any] = None) -> Any:
		"""
		Get a configuration value by key.

		Args:
			key (str): The configuration key to retrieve.
			default (Optional[Any]): The default value if the key is not found.

		Returns:
			Any: The value associated with the key, or the default value if not found.
		"""
		return self.config.get(key, default)

def load_config() -> Config:
	"""
	Load and return a Config instance.

	Returns:
		Config: An instance of the Config class.
	"""
	return Config()

def main() -> None:
	"""
	Test the Config class and print configuration status.
	"""
	# Create an instance of the Config class
	config = load_config()
	
	# Test each configuration value
	print("Testing Config class:")
	print(f"JINA_API_KEY: {'Set' if config.JINA_API_KEY else 'Not set'}")
	print(f"GEMINI_API_KEY: {'Set' if config.GEMINI_API_KEY else 'Not set'}")
	print(f"OPENAI_API_KEY: {'Set' if config.OPENAI_API_KEY else 'Not set'}")
	print(f"ELEVENLABS_API_KEY: {'Set' if config.ELEVENLABS_API_KEY else 'Not set'}")

	# Print a warning for any missing configuration
	missing_config = []
	for key in ['JINA_API_KEY', 'GEMINI_API_KEY', 'OPENAI_API_KEY', 'ELEVENLABS_API_KEY']:
		if not getattr(config, key):
			missing_config.append(key)

	if missing_config:
		print("\nWarning: The following configuration values are missing:")
		for config_name in missing_config:
			print(f"- {config_name}")
		print("Please ensure these are set in your .env file.")
	else:
		print("\nAll configuration values are set.")

	# Test the get method with a default value
	print(f"\nTesting get method with default value:")
	print(f"NON_EXISTENT_KEY: {config.get('NON_EXISTENT_KEY', 'Default Value')}")

if __name__ == "__main__":
	main()
```

## File: `podcastfy/utils/config_conversation.py`
```python
"""
Conversation Configuration Module

This module handles the loading and management of conversation configuration settings
for the Podcastfy application. It uses a YAML file for conversation-specific configuration settings.
"""

import os
import sys
from typing import Any, Dict, Optional, List
import yaml

def get_conversation_config_path(config_file: str = 'conversation_config.yaml'):
	"""
	Get the path to the conversation_config.yaml file.
	
	Returns:
		str: The path to the conversation_config.yaml file.
	"""
	try:
		# Check if the script is running in a PyInstaller bundle
		if getattr(sys, 'frozen', False):
			base_path = sys._MEIPASS
		else:
			base_path = os.path.dirname(os.path.abspath(__file__))
		
		# Look for conversation_config.yaml in the same directory as the script
		config_path = os.path.join(base_path, config_file)
		if os.path.exists(config_path):
			return config_path
		
		# If not found, look in the parent directory (package root)
		config_path = os.path.join(os.path.dirname(base_path), config_file)
		if os.path.exists(config_path):
			return config_path
		
		# If still not found, look in the current working directory
		config_path = os.path.join(os.getcwd(), config_file)
		if os.path.exists(config_path):
			return config_path
		
		raise FileNotFoundError(f"{config_file} not found")
	
	except Exception as e:
		print(f"Error locating {config_file}: {str(e)}")
		return None

class NestedConfig:
	"""
	A class to handle nested configuration objects with proper method inheritance.
	"""
	def __init__(self, config_dict: Dict[str, Any]):
		"""
		Initialize a nested configuration object.

		Args:
			config_dict (Dict[str, Any]): Dictionary containing the nested configuration
		"""
		for key, value in config_dict.items():
			if isinstance(value, dict):
				setattr(self, key, NestedConfig(value))
			else:
				setattr(self, key, value)
	
	def to_dict(self) -> Dict[str, Any]:
		"""
		Convert the NestedConfig object to a dictionary, preserving nested structure.

		Returns:
			Dict[str, Any]: A dictionary representation of the configuration
		"""
		result = {}
		for key, value in self.__dict__.items():
			if not key.startswith('_'):
				if isinstance(value, NestedConfig):
					result[key] = value.to_dict()
				else:
					result[key] = value
		return result
	
	def get(self, key: str, default: Optional[Any] = None) -> Any:
		"""
		Get a configuration value by key, supporting nested keys with dot notation.

		Args:
			key (str): The configuration key to retrieve (e.g., 'child.value')
			default (Optional[Any]): The default value if the key is not found.

		Returns:
			Any: The value associated with the key, or the default value if not found.
		"""
		current = self
		try:
			for part in key.split('.'):
				if isinstance(current, dict):
					current = current[part]
				else:
					current = getattr(current, part)
			return current
		except (AttributeError, KeyError):
			return default

	def get_list(self, key: str, default: Optional[List[str]] = None) -> List[str]:
		"""
		Get a list configuration value by key, supporting nested keys with dot notation.

		Args:
			key (str): The configuration key to retrieve (e.g., 'child.list')
			default (Optional[List[str]]): The default value if the key is not found.

		Returns:
			List[str]: The list associated with the key, or the default value if not found.
		"""
		value = self.get(key, default)
		if isinstance(value, str):
			return [item.strip() for item in value.split(',')]
		return value if isinstance(value, list) else default or []

	def configure(self, config: Dict[str, Any]) -> None:
		"""
		Configure the settings with the provided dictionary.

		Args:
			config (Dict[str, Any]): Configuration dictionary to update the settings.
		"""
		for key, value in config.items():
			if isinstance(value, dict) and hasattr(self, key) and isinstance(getattr(self, key), NestedConfig):
				getattr(self, key).configure(value)
			else:
				setattr(self, key, value)

class ConversationConfig(NestedConfig):
	def __init__(self, config_conversation: Optional[Dict[str, Any]] = None):
		"""
		Initialize the ConversationConfig class with a dictionary configuration.

		Args:
			config_conversation (Optional[Dict[str, Any]]): Configuration dictionary. If None, default config will be used.
		"""
		# Load default configuration
		self.config_conversation = self._load_default_config()
		if config_conversation is not None:
			import copy
			
			# Create a deep copy of the default configuration
			self.config_conversation = copy.deepcopy(self.config_conversation)
			
			# Update the configuration with provided values
			if isinstance(config_conversation, dict):
				self._deep_update(self.config_conversation, config_conversation)
			else:
				print("Warning: config_conversation should be a dictionary.")
		
		# Initialize the NestedConfig with the configuration
		super().__init__(self.config_conversation)

	def _load_default_config(self) -> Dict[str, Any]:
		"""Load the default configuration from conversation_config.yaml."""
		config_path = get_conversation_config_path()
		if config_path:
			with open(config_path, 'r') as file:
				return yaml.safe_load(file)
		else:
			raise FileNotFoundError("conversation_config.yaml not found")

	def _deep_update(self, target: Dict[str, Any], source: Dict[str, Any]) -> None:
		"""
		Recursively update a nested dictionary.

		Args:
			target (Dict[str, Any]): The dictionary to update
			source (Dict[str, Any]): The dictionary containing updates
		"""
		for key, value in source.items():
			if key == 'config_conversation':
				self._deep_update(target, value)
			elif isinstance(value, dict) and key in target and isinstance(target[key], dict):
				self._deep_update(target[key], value)
			else:
				target[key] = value

	def to_dict(self) -> Dict[str, Any]:
		"""
		Convert the ConversationConfig object to a dictionary, preserving nested structure.

		Returns:
			Dict[str, Any]: A dictionary representation of the configuration
		"""
		result = {}
		for key, value in self.__dict__.items():
			if not key.startswith('_'):
				if isinstance(value, (ConversationConfig, NestedConfig)):
					result[key] = value.to_dict()
				else:
					result[key] = value
		return result

def load_conversation_config(config_conversation: Optional[Dict[str, Any]] = None) -> ConversationConfig:
	"""
	Load and return a ConversationConfig instance.

	Args:
		config_conversation (Optional[Dict[str, Any]]): Configuration dictionary to use. If None, default config will be used.

	Returns:
		ConversationConfig: An instance of the ConversationConfig class.
	"""
	return ConversationConfig(config_conversation)

def main() -> None:
	"""
	Test the ConversationConfig class and print configuration status.
	"""
	try:
		# Create an instance of the ConversationConfig class with default settings
		default_config = load_conversation_config()
		
		print("Default Configuration:")
		for key, value in default_config.config_conversation.items():
			print(f"{key}: {value}")

		# Test with custom configuration
		custom_config = {
			"word_count": 1500,
			"podcast_name": "Custom Podcast",
			"output_language": "Spanish"
		}
		custom_config_instance = load_conversation_config(custom_config)

		print("\nCustom Configuration:")
		for key, value in custom_config_instance.config_conversation.items():
			print(f"{key}: {value}")

		# Test the get method with a default value
		print(f"\nTesting get method with default value:")
		print(f"NON_EXISTENT_KEY: {custom_config_instance.get('NON_EXISTENT_KEY', 'Default Value')}")

	except FileNotFoundError as e:
		print(f"Error: {str(e)}")
	except Exception as e:
		print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
	main()
```

## File: `podcastfy/utils/logger.py`
```python
"""
Logger Module

This module provides a utility function to set up and configure a logger for the Podcastfy application.
It ensures consistent logging format and configuration across the application.
"""

import logging
from typing import Any
from podcastfy.utils.config import load_config

def setup_logger(name: str) -> logging.Logger:
    """
    Set up and configure a logger.

    Args:
        name (str): The name of the logger.

    Returns:
        logging.Logger: A configured logger instance.
    """
    config = load_config()
    logging_config = config.get('logging')

    logger = logging.getLogger(name)
    logger.setLevel(logging_config['level'])
    
    formatter = logging.Formatter(logging_config['format'])
    
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    return logger
```

## File: `tests/__init__.py`
```python
# This file can be left empty
```

## File: `tests/test_api.py`
```python
import os
import pytest
from podcastfy.api.fast_app import app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.fixture
def sample_config():
    return {
        "generate_podcast": True,
        "urls": ["https://www.phenomenalworld.org/interviews/swap-structure/"],
        "name": "Central Clearing Risks",
        "tagline": "Exploring the complexities of financial systemic risk",
        "creativity": 0.8,
        "conversation_style": ["engaging", "informative"],
        "roles_person1": "main summarizer",
        "roles_person2": "questioner",
        "dialogue_structure": ["Introduction", "Content", "Conclusion"],
        "tts_model": "edge",
        "is_long_form": False,
        "engagement_techniques": ["questions", "examples", "analogies"],
        "user_instructions": "Don't use the word Dwelve",
        "output_language": "English"
    }

@pytest.mark.skip(reason="Trying to understand if other tests are passing")
def test_generate_podcast_with_edge_tts(sample_config):
    response = client.post("/generate", json=sample_config)
    assert response.status_code == 200
    assert "audioUrl" in response.json()
    assert response.json()["audioUrl"].startswith("http://testserver")

def test_healthcheck():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/test_audio.py`
```python
import unittest
import pytest
import os
from podcastfy.text_to_speech import TextToSpeech
from podcastfy.utils.config_conversation import load_conversation_config


class TestAudio(unittest.TestCase):
    def setUp(self):
        self.test_text = "<Person1>Hello, how are you?</Person1><Person2>I'm doing great, thanks for asking!</Person2>"
        self.output_dir = "tests/data/audio"
        os.makedirs(self.output_dir, exist_ok=True)

    @pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
    def test_text_to_speech_openai(self):
        tts = TextToSpeech(model="openai")
        output_file = os.path.join(self.output_dir, "test_openai.mp3")
        tts.convert_to_speech(self.test_text, output_file)

        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 1024)

        # Clean up
        os.remove(output_file)

    @pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
    def test_text_to_speech_elevenlabs(self):
        tts = TextToSpeech(model="elevenlabs")
        output_file = os.path.join(self.output_dir, "test_elevenlabs.mp3")
        tts.convert_to_speech(self.test_text, output_file)

        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 1024)

        # Clean up
        os.remove(output_file)

    def test_text_to_speech_edge(self):
        tts = TextToSpeech(model="edge")
        output_file = os.path.join(self.output_dir, "test_edge.mp3")
        tts.convert_to_speech(self.test_text, output_file)

        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 1024)

        # Clean up
        os.remove(output_file)

    @pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
    def test_text_to_speech_google(self):
        tts = TextToSpeech(model="gemini")
        output_file = os.path.join(self.output_dir, "test_google.mp3")
        tts.convert_to_speech(self.test_text, output_file)

        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 1024)

        # Clean up
        os.remove(output_file)

    @pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
    def test_text_to_speech_google_multi(self):
        tts = TextToSpeech(model="gemini_multi")
        output_file = os.path.join(self.output_dir, "test_google_multi.mp3")
        tts.convert_to_speech(self.test_text, output_file)

        self.assertTrue(os.path.exists(output_file))
        self.assertGreater(os.path.getsize(output_file), 1024)

        # Clean up
        os.remove(output_file)


if __name__ == "__main__":
    unittest.main()
```

## File: `tests/test_client.py`
```python
"""
Unit tests for the Podcastfy CLI client.
"""

import os
import pytest
import re
from typer.testing import CliRunner
from podcastfy.client import app

runner = CliRunner()


# Mock data
MOCK_URLS = [
    "https://en.wikipedia.org/wiki/Podcast",
    "https://en.wikipedia.org/wiki/Text-to-speech",
]
MOCK_FILE_CONTENT = "\n".join(MOCK_URLS)
MOCK_TRANSCRIPT = "<Person1>Joe Biden and the US Politics</Person1><Person2>Joe Biden is the current president of the United States of America</Person2>"
MOCK_IMAGE_PATHS = [
    "https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/Senecio.jpeg",
    "https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/connection.jpg",
]
MOCK_CONVERSATION_CONFIG = """
word_count: 300
conversation_style: 
  - formal
  - educational
roles_person1: professor
roles_person2: student
dialogue_structure: 
  - Introduction
  - Main Points
  - Case Studies
  - Quiz
  - Conclusion
podcast_name: Teachfy
podcast_tagline: Learning Through Conversation
output_language: English
engagement_techniques: 
  - examples
  - questions
creativity: 0
text_to_speech:
	model: edge
"""


@pytest.fixture
def mock_files(tmp_path):
    # Create mock files
    url_file = tmp_path / "urls.txt"
    url_file.write_text(MOCK_FILE_CONTENT)

    transcript_file = tmp_path / "transcript.txt"
    transcript_file.write_text(MOCK_TRANSCRIPT)

    config_file = tmp_path / "custom_config.yaml"
    config_file.write_text(MOCK_CONVERSATION_CONFIG)

    return {
        "url_file": str(url_file),
        "transcript_file": str(transcript_file),
        "config_file": str(config_file),
    }


@pytest.fixture
def sample_config():
    """
    Fixture to provide a sample conversation configuration for testing.

    Returns:
            dict: A dictionary containing sample conversation configuration parameters.
    """
    conversation_config = {
        "word_count": 300,
        "text_to_speech": {
            "output_directories": {
                "transcripts": "tests/data/transcripts",
                "audio": "tests/data/audio",
            },
            "temp_audio_dir": "tests/data/audio/tmp",
            "ending_message": "Bye Bye!",
        },
    }
    return conversation_config


def test_generate_podcast_from_urls(sample_config):
    result = runner.invoke(
        app, ["--url", MOCK_URLS[0], "--url", MOCK_URLS[1], "--tts-model", "edge"]
    )
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    audio_path = result.stdout.split(": ")[-1].strip()
    assert os.path.exists(audio_path)
    assert audio_path.endswith(".mp3")
    assert os.path.getsize(audio_path) > 1024  # Check if larger than 1KB


def test_generate_podcast_from_file(mock_files, sample_config):
    result = runner.invoke(
        app, ["--file", mock_files["url_file"], "--tts-model", "edge"]
    )
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    assert os.path.exists(result.stdout.split(": ")[-1].strip())
    assert result.stdout.split(": ")[-1].strip().endswith(".mp3")
    assert (
        os.path.getsize(result.stdout.split(": ")[-1].strip()) > 1024
    )  # Check if larger than 1KB


def test_generate_podcast_from_transcript(mock_files, sample_config):
    result = runner.invoke(
        app, ["--transcript", mock_files["transcript_file"], "--tts-model", "edge"]
    )
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    assert os.path.exists(result.stdout.split(": ")[-1].strip())
    assert result.stdout.split(": ")[-1].strip().endswith(".mp3")
    assert (
        os.path.getsize(result.stdout.split(": ")[-1].strip()) > 1024
    )  # Check if larger than 1KB


def test_generate_transcript_only(sample_config):
    result = runner.invoke(app, ["--url", MOCK_URLS[0], "--transcript-only"])
    assert result.exit_code == 0
    assert "Transcript generated successfully" in result.stdout

    # Extract the transcript path
    transcript_path = result.stdout.split(": ")[-1].strip()

    assert transcript_path, "Transcript path is empty"
    assert os.path.exists(
        transcript_path
    ), f"Transcript file does not exist at path: {transcript_path}"

    with open(transcript_path, "r") as f:
        content = f.read()
        assert content != ""
        assert isinstance(content, str)
        assert all(
            "<Person1>" in tag and "</Person1>" in tag
            for tag in re.findall(r"<Person1>.*?</Person1>", content)
        )
        assert all(
            "<Person2>" in tag and "</Person2>" in tag
            for tag in re.findall(r"<Person2>.*?</Person2>", content)
        )


@pytest.mark.skip(reason="Not supported yet")
def test_generate_podcast_from_urls_and_file(mock_files, sample_config):
    result = runner.invoke(
        app,
        [
            "--url",
            MOCK_URLS[0],
            "--file",
            mock_files["url_file"],
            "--tts-model",
            "edge",
        ],
    )
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    assert os.path.exists(result.stdout.split(": ")[-1].strip())
    assert result.stdout.split(": ")[-1].strip().endswith(".mp3")
    assert (
        os.path.getsize(result.stdout.split(": ")[-1].strip()) > 1024
    )  # Check if larger than 1KB


def test_generate_podcast_from_image(sample_config):
    result = runner.invoke(app, ["--image", MOCK_IMAGE_PATHS[0], "--tts-model", "edge"])
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    assert os.path.exists(result.stdout.split(": ")[-1].strip())
    assert result.stdout.split(": ")[-1].strip().endswith(".mp3")
    assert (
        os.path.getsize(result.stdout.split(": ")[-1].strip()) > 1024
    )  # Check if larger than 1KB


@pytest.mark.skip(reason="To be further tested")
def test_generate_podcast_with_custom_config(mock_files, sample_config):
    result = runner.invoke(
        app,
        [
            "--url",
            MOCK_URLS[0],
            "--conversation-config",
            mock_files["config_file"],
            "--tts-model",
            "edge",
        ],
    )
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    audio_path = result.stdout.split(": ")[-1].strip()
    assert os.path.exists(audio_path)
    assert audio_path.endswith(".mp3")
    assert os.path.getsize(audio_path) > 1024  # Check if larger than 1KB

    # Check for elements from the custom config in the transcript
    transcript_path = audio_path.replace(".mp3", ".txt")
    assert os.path.exists(transcript_path)
    with open(transcript_path, "r") as f:
        content = f.read()
        assert "Teachfy" in content
        assert "Learning Through Conversation" in content


def test_generate_podcast_from_urls_and_images(sample_config):
    result = runner.invoke(
        app,
        ["--url", MOCK_URLS[0], "--image", MOCK_IMAGE_PATHS[0], "--tts-model", "edge"],
    )
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    assert os.path.exists(result.stdout.split(": ")[-1].strip())
    assert result.stdout.split(": ")[-1].strip().endswith(".mp3")
    assert (
        os.path.getsize(result.stdout.split(": ")[-1].strip()) > 1024
    )  # Check if larger than 1KB


@pytest.mark.skip(reason="Requires local LLM running")
def test_generate_transcript_with_local_llm(sample_config):
    result = runner.invoke(
        app,
        ["--url", MOCK_URLS[0], "--transcript-only", "--local", "--tts-model", "edge"],
    )
    assert result.exit_code == 0
    assert "Transcript generated successfully" in result.stdout
    transcript_path = result.stdout.split(": ")[-1].strip()
    assert os.path.exists(transcript_path)
    with open(transcript_path, "r") as f:
        content = f.read()
        assert content != ""
        assert isinstance(content, str)
        assert re.match(
            r"(<Person1>.*?</Person1>\s*<Person2>.*?</Person2>\s*)+", content
        )


def test_generate_podcast_from_raw_text():
    """Test generating a podcast from raw input text using the CLI."""
    raw_text = "The wonderful world of LLMs."
    result = runner.invoke(app, ["--text", raw_text, "--tts-model", "edge"])
    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout
    audio_path = result.stdout.split(": ")[-1].strip()
    assert os.path.exists(audio_path)
    assert audio_path.endswith(".mp3")
    assert os.path.getsize(audio_path) > 1024  # Check if larger than 1KB


def test_cli_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Generate a podcast or transcript from a list of URLs" in result.stdout


def test_no_input_provided():
    result = runner.invoke(app)
    assert result.exit_code != 0
    assert "No input provided" in result.stdout


def test_generate_podcast_with_custom_llm():
    """Test generating a podcast with a custom LLM model using CLI."""
    result = runner.invoke(
        app,
        [
            "--url",
            MOCK_URLS[0],
            "--tts-model",
            "edge",
            "--llm-model-name",
            "gemini-2.5-flash",
            "--api-key-label",
            "GEMINI_API_KEY",
        ],
    )

    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout

    # Extract and verify the audio file
    audio_path = result.stdout.split(": ")[-1].strip()
    assert os.path.exists(audio_path)
    assert audio_path.endswith(".mp3")
    assert os.path.getsize(audio_path) > 1024  # Check if larger than 1KB

    # Clean up
    os.remove(audio_path)


def test_generate_transcript_only_with_custom_llm():
    """Test generating only a transcript with a custom LLM model using CLI."""
    result = runner.invoke(
        app,
        [
            "--url",
            MOCK_URLS[0],
            "--transcript-only",
            "--llm-model-name",
            "gemini-2.5-flash",
            "--api-key-label",
            "GEMINI_API_KEY",
        ],
    )

    assert result.exit_code == 0
    assert "Transcript generated successfully" in result.stdout

    # Extract and verify the transcript file
    transcript_path = result.stdout.split(": ")[-1].strip()
    assert os.path.exists(transcript_path)
    assert transcript_path.endswith(".txt")

    # Verify transcript content
    with open(transcript_path, "r") as f:
        content = f.read()
        assert content != ""
        assert isinstance(content, str)
        assert "<Person1>" in content
        assert "<Person2>" in content
        assert len(content.split("<Person1>")) > 1  # At least one question
        assert len(content.split("<Person2>")) > 1  # At least one answer

        # Verify content is substantial
        min_length = 500  # Minimum expected length in characters
        assert (
            len(content) > min_length
        ), f"Content length ({len(content)}) is less than minimum expected ({min_length})"

    # Clean up
    os.remove(transcript_path)


@pytest.mark.skip(reason="Too expensive to be auto tested on Github Actions")
def test_generate_podcast_from_topic():
    """Test generating a podcast from a topic using CLI."""
    result = runner.invoke(
        app, ["--topic", "Artificial Intelligence Ethics", "--tts-model", "edge"]
    )

    assert result.exit_code == 0
    assert "Podcast generated successfully using edge TTS model" in result.stdout

    # Extract and verify the audio file
    audio_path = result.stdout.split(": ")[-1].strip()
    assert os.path.exists(audio_path)
    assert audio_path.endswith(".mp3")
    assert os.path.getsize(audio_path) > 1024  # Check if larger than 1KB

    # Clean up
    os.remove(audio_path)


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/test_content_parser.py`
```python
import unittest
import pytest
from podcastfy.utils.config import load_config
from podcastfy.content_parser.content_extractor import ContentExtractor
from podcastfy.content_parser.youtube_transcriber import YouTubeTranscriber
from podcastfy.content_parser.website_extractor import WebsiteExtractor
from podcastfy.content_parser.pdf_extractor import PDFExtractor


class TestContentParser(unittest.TestCase):
    def test_content_extractor(self):
        # Add tests for ContentExtractor
        pass

    @pytest.mark.skip(
        reason="IP getting blocked by YouTube when running from GitHub Actions"
    )
    def test_youtube_transcriber(self):
        """
        Test the YouTubeTranscriber class to ensure it correctly extracts and cleans transcripts from a YouTube video.
        """
        # Initialize YouTubeTranscriber
        transcriber = YouTubeTranscriber()

        # Test URL
        test_url = "https://www.youtube.com/watch?v=m3kJo5kEzTQ"

        # Extract transcript
        extracted_transcript = transcriber.extract_transcript(test_url)

        # Load expected transcript from youtube.txt file
        with open("./tests/data/mock/youtube.txt", "r") as f:
            expected_transcript = f.read()

        # Assert that the first 100 characters of the extracted transcript match the expected transcript
        self.assertEqual(
            extracted_transcript[:100].strip(), expected_transcript[:100].strip()
        )

    def test_website_extractor(self):
        """
        Test the WebsiteExtractor class to ensure it correctly extracts content from a website.
        """
        # pass #TODO remove pass when testing. Keeping it here to avoid running out of quota.

        # Initialize WebsiteExtractor
        config = load_config()
        extractor = WebsiteExtractor()

        # Test URL
        test_url = "http://www.souzatharsis.com"

        # Extract content
        extracted_content = extractor.extract_content(test_url)
        print(extracted_content.strip())
        # Load expected content from website.md file
        with open("./tests/data/mock/website.md", "r") as f:
            expected_content = f.read()
        print(expected_content.strip())
        # Assert that the extracted content matches the expected content
        self.assertEqual(extracted_content.strip(), expected_content.strip())

    def test_pdf_extractor(self):
        """
        Test the PDFExtractor class to ensure it correctly extracts content from a PDF file.
        """
        # Initialize PDFExtractor
        extractor = PDFExtractor()

        # Path to the test PDF file
        pdf_path = "./tests/data/pdf/file.pdf"

        # Extract content from PDF
        extracted_content = extractor.extract_content(pdf_path)

        # Load expected content from file.txt
        with open("./tests/data/mock/file.txt", "r") as f:
            expected_content = f.read()

        # Assert that the first 500 characters of the extracted content match the expected content
        self.assertEqual(
            extracted_content[:500].strip(), expected_content[:500].strip()
        )

    @pytest.mark.skip(reason="Too expensive to be auto tested on Github Actions")
    def test_generate_topic_content(self):
        """Test generating content for a specific topic."""
        extractor = ContentExtractor()
        topic = "Latest news about OpenAI"

        # Generate content for the topic
        content = extractor.generate_topic_content(topic)

        # Verify the content
        self.assertIsNotNone(content)
        self.assertIsInstance(content, str)
        self.assertGreater(len(content), 100)  # Content should be substantial

        # Check if content is relevant to the topic
        lower_content = content.lower()
        self.assertTrue(
            any(term in lower_content for term in ["openai"]),
            "Generated content should be relevant to the topic",
        )


if __name__ == "__main__":
    unittest.main()
```

## File: `tests/test_genai_podcast.py`
```python
import unittest
import pytest
from unittest.mock import patch, MagicMock
import tempfile
import os
from podcastfy.content_generator import ContentGenerator
from podcastfy.utils.config import Config
from podcastfy.utils.config_conversation import ConversationConfig
from podcastfy.content_parser.pdf_extractor import PDFExtractor
from podcastfy.content_parser.content_extractor import ContentExtractor


MOCK_IMAGE_PATHS = [
    "https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/Senecio.jpeg",
    "https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/connection.jpg",
]

MODEL_NAME = "gemini-2.5-flash"
API_KEY_LABEL = "GEMINI_API_KEY"


# TODO: Should be a fixture
def sample_conversation_config():
    conversation_config = {
        "word_count": 500,
        "roles_person1": "professor",
        "roles_person2": "student",
        "podcast_name": "Teachfy",
        "podcast_tagline": "Learning Through Conversation",
    }
    return conversation_config


class TestGenAIPodcast(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.
        """
        config = Config()
        self.api_key = config.GEMINI_API_KEY
        self.config = config

    def test_generate_qa_content(self):
        """
        Test the generate_qa_content method of ContentGenerator.
        """
        content_generator = ContentGenerator(model_name=MODEL_NAME, api_key_label=API_KEY_LABEL)
        input_text = "United States of America"
        result = content_generator.generate_qa_content(input_text)
        self.assertIsNotNone(result)
        self.assertNotEqual(result, "")
        self.assertIsInstance(result, str)

    def test_custom_conversation_config(self):
        """
        Test the generation of content using a custom conversation configuration file.
        """
        conversation_config = sample_conversation_config()
        content_generator = ContentGenerator(model_name=MODEL_NAME, api_key_label=API_KEY_LABEL, conversation_config=conversation_config)
        input_text = "United States of America"

        result = content_generator.generate_qa_content(input_text)

        self.assertIsNotNone(result)
        self.assertNotEqual(result, "")
        self.assertIsInstance(result, str)

        # Check for elements from the custom config
        self.assertIn(conversation_config["podcast_name"].lower(), result.lower())
        self.assertIn(conversation_config["podcast_tagline"].lower(), result.lower())

    def test_generate_qa_content_from_images(self):
        """Test generating Q&A content from two input images."""
        image_paths = MOCK_IMAGE_PATHS

        content_generator = ContentGenerator(model_name=MODEL_NAME, api_key_label=API_KEY_LABEL)

        with tempfile.NamedTemporaryFile(
            mode="w+", suffix=".txt", delete=False
        ) as temp_file:
            result = content_generator.generate_qa_content(
                input_texts="",  # Empty string for input_texts
                image_file_paths=image_paths,
                output_filepath=temp_file.name,
            )

        self.assertIsNotNone(result)
        self.assertNotEqual(result, "")
        self.assertIsInstance(result, str)

        # Check if the output file was created and contains the same content
        with open(temp_file.name, "r") as f:
            file_content = f.read()

        self.assertEqual(result, file_content)

        # Clean up the temporary file
        os.unlink(temp_file.name)

    def test_generate_qa_content_from_pdf(self):
        """Test generating Q&A content from a PDF file."""
        pdf_file = "tests/data/pdf/file.pdf"
        content_generator = ContentGenerator(model_name=MODEL_NAME, api_key_label=API_KEY_LABEL)
        pdf_extractor = PDFExtractor()

        # Extract content from the PDF file
        extracted_content = pdf_extractor.extract_content(pdf_file)

        # Generate Q&A content from the extracted text
        result = content_generator.generate_qa_content(input_texts=extracted_content)

        self.assertIsNotNone(result)
        self.assertNotEqual(result, "")
        self.assertIsInstance(result, str)

    def test_generate_qa_content_from_raw_text(self):
        """Test generating Q&A content from raw input text."""
        raw_text = "The wonderful world of LLMs."
        content_generator = ContentGenerator(model_name=MODEL_NAME, api_key_label=API_KEY_LABEL)

        result = content_generator.generate_qa_content(input_texts=raw_text)

        self.assertIsNotNone(result)
        self.assertNotEqual(result, "")
        self.assertIsInstance(result, str)

    @pytest.mark.skip(reason="Too expensive to be auto tested on Github Actions")
    def test_generate_qa_content_from_topic(self):
        """Test generating Q&A content from a specific topic."""
        topic = "Latest news about OpenAI"
        content_generator = ContentGenerator(model_name=MODEL_NAME, api_key_label=API_KEY_LABEL)
        extractor = ContentExtractor()
        topic = "Latest news about OpenAI"

        # Generate content for the topic
        content = extractor.generate_topic_content(topic)

        result = content_generator.generate_qa_content(input_texts=content)

        self.assertIsNotNone(result)
        self.assertNotEqual(result, "")
        self.assertIsInstance(result, str)

        # Verify Q&A format
        self.assertIn("<Person1>", result)
        self.assertIn("<Person2>", result)

        # Verify content relevance
        lower_result = result.lower()
        self.assertTrue(
            any(term in lower_result for term in ["openai"]),
            "Generated content should be relevant to the topic",
        )


if __name__ == "__main__":
    unittest.main()
```

## File: `tests/test_generate_podcast.py`
```python
import os
import pytest
import tempfile
from podcastfy.client import generate_podcast
from podcastfy.utils.config import load_config
from podcastfy.utils.config_conversation import load_conversation_config


TEST_URL = "https://en.wikipedia.org/wiki/Friends"
MOCK_IMAGE_PATHS = [
    "https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/Senecio.jpeg",
    "https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/connection.jpg",
]


@pytest.fixture
def sample_config():
    config = load_config()
    return config


@pytest.fixture
def default_conversation_config():
    config = load_conversation_config()
    return config


@pytest.fixture
def sample_conversation_config():
    """
    Fixture to provide a sample conversation configuration for testing.

    Returns:
            dict: A dictionary containing sample conversation configuration parameters.
    """
    conversation_config = {
        "word_count": 300,
        "conversation_style": ["formal", "educational"],
        "roles_person1": "professor",
        "roles_person2": "student",
        "dialogue_structure": [
            "Introduction",
            "Main Points",
            "Case Studies",
            "Quiz",
            "Conclusion",
        ],
        "podcast_name": "Teachfy",
        "podcast_tagline": "Learning Through Conversation",
        "output_language": "English",
        "engagement_techniques": ["examples", "questions"],
        "creativity": 0,
        "text_to_speech": {
            "output_directories": {
                "transcripts": "tests/data/transcriptsTEST",
                "audio": "tests/data/audioTEST",
            },
            "temp_audio_dir": "tests/data/audio/tmpTEST/",
            "ending_message": "Bye Bye!",
        },
    }
    return conversation_config


@pytest.fixture(autouse=True)
def setup_test_directories(sample_conversation_config):
    """Create test directories if they don't exist."""
    output_dirs = sample_conversation_config.get("text_to_speech", {}).get(
        "output_directories", {}
    )
    for directory in output_dirs.values():
        os.makedirs(directory, exist_ok=True)
    temp_dir = sample_conversation_config.get("text_to_speech", {}).get(
        "temp_audio_dir"
    )
    if temp_dir:
        os.makedirs(temp_dir, exist_ok=True)


@pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
def test_generate_podcast_from_urls_11labs(default_conversation_config):
    """Test generating a podcast from a list of URLs."""
    urls = [TEST_URL]

    audio_file = generate_podcast(urls=urls, tts_model="elevenlabs")
    print(f"Audio file generated using ElevenLabs model: {audio_file}")
    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB
    assert os.path.dirname(audio_file) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("audio")


@pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
def test_generate_podcast_from_urls_openai(default_conversation_config):
    """Test generating a podcast from a list of URLs."""
    urls = [
        TEST_URL,
    ]

    audio_file = generate_podcast(urls=urls, tts_model="openai")
    print(f"Audio file generated using OpenAI model: {audio_file}")

    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB
    assert os.path.dirname(audio_file) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("audio")


@pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
def test_generate_podcast_from_urls_gemini(default_conversation_config):
    """Test generating a podcast from a list of URLs."""
    urls = [
        TEST_URL,
    ]

    audio_file = generate_podcast(urls=urls, tts_model="gemini")
    print(f"Audio file generated using Gemini model: {audio_file}")

    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB
    assert os.path.dirname(audio_file) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("audio")


def test_generate_podcast_from_urls_edge(default_conversation_config):
    """Test generating a podcast from a list of URLs."""
    urls = [TEST_URL]

    audio_file = generate_podcast(urls=urls, tts_model="edge")
    print(f"Audio file generated using Edge model: {audio_file}")
    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB
    assert os.path.dirname(audio_file) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("audio")


def test_generate_transcript_only(default_conversation_config):
    """Test generating only a transcript without audio."""
    urls = [TEST_URL]

    result = generate_podcast(urls=urls, transcript_only=True)
    print(f"Transcript file generated: {result}")

    assert result is not None
    assert os.path.exists(result)
    assert result.endswith(".txt")
    assert os.path.dirname(result) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("transcripts")


def test_generate_podcast_from_transcript_file(sample_conversation_config):
    """Test generating a podcast from an existing transcript file."""
    # First, generate a transcript
    transcript_file = os.path.join(
        sample_conversation_config.get("text_to_speech", {})
        .get("output_directories", {})
        .get("transcripts"),
        "test_transcript.txt",
    )
    with open(transcript_file, "w") as f:
        f.write(
            "<Person1>Joe Biden and the US Politics</Person1><Person2>Joe Biden is the current president of the United States of America</Person2>"
        )

    # Now use this transcript to generate a podcast
    audio_file = generate_podcast(
        transcript_file=transcript_file,
        tts_model="edge",
        conversation_config=sample_conversation_config,
    )

    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB
    assert os.path.dirname(audio_file) == sample_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("audio")


def test_generate_podcast_with_custom_config(sample_config, sample_conversation_config):
    """Test generating a podcast with a custom conversation config."""
    urls = ["https://en.wikipedia.org/wiki/Artificial_intelligence"]

    audio_file = generate_podcast(
        urls=urls,
        config=sample_config,
        conversation_config=sample_conversation_config,
        tts_model="edge",
    )

    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB
    assert (
        os.path.dirname(audio_file)
        == sample_conversation_config["text_to_speech"]["output_directories"]["audio"]
    )


def test_generate_from_local_pdf(sample_config):
    """Test generating a podcast from a local PDF file."""
    pdf_file = "tests/data/pdf/file.pdf"
    audio_file = generate_podcast(
        urls=[pdf_file], config=sample_config, tts_model="edge"
    )
    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB

@pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
def test_generate_from_local_pdf_multispeaker(sample_config):
    """Test generating a podcast from a local PDF file."""
    pdf_file = "tests/data/pdf/file.pdf"
    audio_file = generate_podcast(
        urls=[pdf_file], config=sample_config, tts_model="geminimulti"
    )
    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB

@pytest.mark.skip(reason="Testing edge only on Github Action as it's free")
def test_generate_from_local_pdf_multispeaker_longform(sample_config):
    """Test generating a podcast from a local PDF file."""
    pdf_file = "tests/data/pdf/file.pdf"
    audio_file = generate_podcast(
        urls=[pdf_file], config=sample_config, tts_model="geminimulti", longform=True
    )
    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB

def test_generate_podcast_no_urls_or_transcript():
    """Test that an error is raised when no URLs or transcript file is provided."""
    with pytest.raises(ValueError):
        generate_podcast()


def test_generate_podcast_from_images(sample_config, default_conversation_config):
    """Test generating a podcast from two input images."""
    image_paths = MOCK_IMAGE_PATHS

    audio_file = generate_podcast(
        image_paths=image_paths, tts_model="edge", config=sample_config
    )

    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB

    # Check if a transcript was generated
    transcript_dir = (
        default_conversation_config.get("text_to_speech", {})
        .get("output_directories", {})
        .get("transcripts")
    )
    transcript_files = [
        f
        for f in os.listdir(transcript_dir)
        if f.startswith("transcript_") and f.endswith(".txt")
    ]
    assert len(transcript_files) > 0


def test_generate_podcast_from_raw_text(sample_config, default_conversation_config):
    """Test generating a podcast from raw input text."""
    raw_text = "The wonderful world of LLMs."

    audio_file = generate_podcast(text=raw_text, tts_model="edge", config=sample_config)

    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024  # Check if larger than 1KB
    assert os.path.dirname(audio_file) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("audio")


def test_generate_transcript_with_user_instructions(
    sample_config, default_conversation_config
):
    """Test generating a transcript with specific user instructions in the conversation config."""
    url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

    # Create a custom conversation config with user instructions
    conversation_config = {
        "word_count": 2000,
        "conversation_style": ["formal", "educational"],
        "roles_person1": "professor",
        "roles_person2": "student",
        "dialogue_structure": [
            "Introduction",
            "Main Points",
            "Case Studies",
            "Quiz",
            "Conclusion",
        ],
        "podcast_name": "Teachfy",
        "podcast_tagline": "Learning Through Teaching",
        "output_language": "English",
        "engagement_techniques": ["examples", "questions"],
        "creativity": 0,
        "user_instructions": "Make a connection with a related topic: Knowledge Graphs.",
    }

    # Generate transcript with the custom config
    result = generate_podcast(
        urls=[url],
        transcript_only=True,
        config=sample_config,
        conversation_config=conversation_config,
        tts_model="edge",
    )

    assert result is not None
    assert os.path.exists(result)
    assert result.endswith(".txt")
    assert os.path.dirname(result) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("transcripts")

    # Read the generated transcript
    with open(result, "r") as f:
        content = f.read()

    assert (
        conversation_config["podcast_name"].lower() in content.lower()
    ), f"Expected to find podcast name '{conversation_config['podcast_name']}' in transcript"
    assert (
        conversation_config["podcast_tagline"].lower() in content.lower()
    ), f"Expected to find podcast tagline '{conversation_config['podcast_tagline']}' in transcript"


def test_generate_podcast_with_custom_llm(sample_config, default_conversation_config):
    """Test generating a podcast with a custom LLM model."""
    urls = ["https://en.wikipedia.org/wiki/Artificial_intelligence"]

    audio_file = generate_podcast(
        urls=urls,
        tts_model="edge",
        config=sample_config,
        llm_model_name="gemini-2.5-flash",
        api_key_label="GEMINI_API_KEY",
    )

    assert audio_file is not None
    assert os.path.exists(audio_file)
    assert audio_file.endswith(".mp3")
    assert os.path.getsize(audio_file) > 1024
    assert os.path.dirname(audio_file) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("audio")


def test_generate_transcript_only_with_custom_llm(
    sample_config, default_conversation_config
):
    """Test generating only a transcript with a custom LLM model."""
    urls = ["https://en.wikipedia.org/wiki/Artificial_intelligence"]

    # Generate transcript with custom LLM settings
    result = generate_podcast(
        urls=urls,
        transcript_only=True,
        config=sample_config,
        llm_model_name="gemini-2.5-flash",
        api_key_label="GEMINI_API_KEY",
    )

    assert result is not None
    assert os.path.exists(result)
    assert result.endswith(".txt")
    assert os.path.dirname(result) == default_conversation_config.get(
        "text_to_speech", {}
    ).get("output_directories", {}).get("transcripts")

    # Read and verify the content
    with open(result, "r") as f:
        content = f.read()

    # Verify the content follows the Person1/Person2 format
    assert "<Person1>" in content
    assert "<Person2>" in content
    assert len(content.split("<Person1>")) > 1  # At least one question
    assert len(content.split("<Person2>")) > 1  # At least one answer

    # Verify the content is substantial
    min_length = 500  # Minimum expected length in characters
    assert (
        len(content) > min_length
    ), f"Content length ({len(content)}) is less than minimum expected ({min_length})"


def test_generate_longform_transcript(sample_config, default_conversation_config):
    """Test generating a longform podcast transcript from a PDF file."""
    pdf_file = "tests/data/pdf/file.pdf"
    
    # Generate transcript with longform=True
    result = generate_podcast(
        urls=[pdf_file],
        config=sample_config,
        transcript_only=True,
        longform=True
    )

    assert result is not None
    assert os.path.exists(result)
    assert result.endswith(".txt")
    
    # Read and verify the content
    with open(result, "r") as f:
        content = f.read()
    
    # Verify the content follows the Person1/Person2 format
    assert "<Person1>" in content
    assert "<Person2>" in content
    
    # Verify it's a long-form transcript (>1000 characters)
    assert len(content) > 1000, f"Content length ({len(content)}) is less than minimum expected for longform (1000)"
    
    # Verify multiple discussion rounds exist (characteristic of longform)
    person1_segments = content.count("<Person1>")
    assert person1_segments > 3, f"Expected more than 3 discussion rounds, got {person1_segments}"


if __name__ == "__main__":
    pytest.main()
```

## File: `tests/data/mock/config_conversation_test.yaml`
```yaml
word_count: 2000
conversation_style: 
  - "formal"
  - "educational"
roles_person1: "professor"
roles_person2: "student"
dialogue_structure: 
  - "Introduction"
  - "Main Points"
  - "Conclusion"
podcast_name: "Teachfy"
podcast_tagline: "Learning Through Conversation"
output_language: "English"
engagement_techniques: 
  - "examples"
  - "questions"
  - "case studies"
creativity: 0
```

## File: `tests/data/mock/file.txt`
```
Forecasting Financial Market Structure from
Network Features using Machine Learning
Douglas Castilho1,5,*,+, Th ́arsis T. P. Souza2,+, Soong Moon Kang3, Jo ̃ao Gama4, and
Andr ́e C. P. L. F. de Carvalho1
1Institute of Mathematics and Computer Sciences (ICMC), University of S ̃ao Paulo (USP), S ̃ao Carlos, Brazil
2Department of Computer Science, University College London, Gower Street, London, WC1E 6BT, UK
3School of Management, University College London, Gower Street, London, WC1E 6BT, UK
4Insti
```

## File: `tests/data/mock/website.md`
```markdown
Tharsis Souza, PhD Tharsis Souza is a computer scientist passionate about data-driven products. He is Senior Vice President of Product Management, Modeling Engineering at Two Sigma Investments and Lecturer at Columbia University, Faculty member of the MSc. in Applied Analytics program. Prior to Two Sigma, he spent 10+ years delivering new technology products in a variety of companies from start-ups to Fortune 500’s in the U.S., Brazil, and the U.K. He’s an author of scholarly publications and a regular speaker in academic and business conferences. He also enjoys mentoring under-represented students & working professionals. Tharsis holds a Ph.D. in Computer Science from UCL, University of London following an M.Phil. and M.Sc. in Computer Science and a B.Sc. in Computer Engineering. Selected Interviews and Talks Mentorship Spotlight: Tharsis Souza, Two Sigma FactSet Investment Process Symposium - Innovative Data Panel BattleFin Alternative Data - Interview Beryl Elites - The Disruptors in Investment Management
```

## File: `tests/data/mock/youtube.txt`
```
Bloomberg audio Studios podcasts radio news hello and welcome to another episode of the odd Lots podcast I'm Tracy Alaway and I'm Joe weisenthal Joe I know we did one episode on pod shop yeah on Multi strategy hedge funds but it was primarily focused on their impact on the market and I have to say I still came away from that conversation sort of wondering if I worked at a pod shop what is it exactly that I would be doing all day I would love to know the exact same thing I mean like I guess
```

## File: `tests/data/transcripts/transcript_013b1c9fe41942249cb7adde26e4fff1.txt`
```
<Person1> <prosody rate="90%" pitch="medium"> Welcome to Teachfy - Learning Through Conversation! Today, let's delve into the fascinating world of Artificial Intelligence. </prosody> </Person1>

<Person2> <prosody rate="100%" pitch="high">  AI always seems shrouded in mystery. What exactly *is* it? </prosody> </Person2>

<Person1> <prosody rate="90%" pitch="medium">  In essence, AI refers to intelligence demonstrated by machines, particularly computer systems. It's a field within computer science dedicated to developing methods and software that empower machines to perceive their surroundings, learn, and make decisions to achieve specific goals. </prosody> </Person1>

<Person2> <prosody rate="100%" pitch="high">  So, like robots? </prosody> </Person2>

<Person1> <prosody rate="90%" pitch="medium">  Robotics is one application, but AI is much broader. Think of advanced web search engines like Google, recommendation systems used by Netflix, or virtual assistants like Siri. These are all powered by AI. </prosody> </Person1>

<Person2> <prosody rate="100%" pitch="high">  I see. So AI is already deeply integrated into our lives. </prosody> </Person2>

<Person1> <prosody rate="90%" pitch="medium">  Precisely. And it's constantly evolving. AI research encompasses various subfields, each with specific goals and tools. These include reasoning, knowledge representation, planning, learning, natural language processing, and perception. </prosody> </Person1>

<Person2> <prosody rate="100%" pitch="high">  It sounds like AI aims to replicate human intelligence. Is that the ultimate goal? </prosody> </Person2>

<Person1> <prosody rate="90%" pitch="medium">  One of the long-term goals is indeed to achieve general intelligence, where a machine can perform any task a human can, at least equally well. However, there's debate on whether we should directly pursue this or focus on solving specific problems, leading indirectly to general intelligence. </prosody> </Person1>

<Person2> <prosody rate="100%" pitch="high">  That makes sense. Focusing on specific problems seems more achievable. But what about the risks? We often hear about AI becoming a threat. </prosody> </Person2>

<Person1> <prosody rate="90%" pitch="medium">  The potential risks are real and need careful consideration. These include privacy concerns, algorithmic bias, job displacement, and even the potential for AI to surpass human control.  </prosody> </Person1>

<Person2> <prosody rate="100%" pitch="high">  That's concerning. What's being done to address these risks? </prosody> </Person2>

<Person1> <prosody rate="90%" pitch="medium">  There's growing emphasis on ethical AI development, focusing on fairness, transparency, and accountability. Regulatory frameworks are also being explored globally to ensure responsible AI deployment. </prosody> </Person1>

<Person2> <prosody rate="100%" pitch="high">  It seems like AI is a powerful tool with both immense potential and significant risks. </prosody> </Person2>

<Person1> <prosody rate="90%" pitch="medium">  Indeed. AI is a double-edged sword. Its impact on our future depends on how we choose to develop and utilize it.  </prosody> </Person1>
```

## File: `tests/data/transcripts/transcript_336aa9f955cd4019bc1287379a5a2820.txt`
```
<Person1>
Welcome to PODCASTFY  - YOUR PERSONAL GenAI PODCAST. Buckle up, because today we're diving deep into the fascinating world of podcasts! </Person1>

<Person2>
Podcasts, huh? Yeah, I listen to them while I walk my dog. What's so fascinating about 'em?  </Person2>

<Person1>
Oh, it's way more than just dog-walking background noise! We're talking about a whole revolution in how we consume information and entertainment.  Think about it -  it's audio on demand! </Person2>

<Person2>
Okay, I'll bite. What's the big deal with that? </Person2>

<Person1>
Well, imagine having access to millions of conversations, stories, and discussions on any topic imaginable, all ready to go whenever you are. That's the power of podcasting! It's like having a personalized radio station in your pocket. </Person1>

<Person2>
Hmm, I never thought of it that way. But didn't podcasts start with iPods? That's what the name sounds like, right? </Person2>

<Person1>
That's a common misconception!  The name "podcast" does come from a mashup of "iPod" and "broadcast," but the concept actually predates Apple's iPod.  We're talking early 2000s, even before iTunes was a thing! </Person1>

<Person2>
Whoa, really? So how did people even listen to them back then? </Person2>

<Person1>
It was a bit more complicated. You needed special software called "podcatchers" to download and transfer the audio files to your device.  It wasn't exactly user-friendly, but the early adopters were hooked! </Person1>

<Person2>
I can see why! But what makes podcasts different from, say, just listening to music? </Person2>

<Person1>
It's the content, my friend! Podcasts cover every niche and interest you can imagine. You've got news, comedy, true crime, history, science, business, and everything in between. And the best part?  Most of them are free! </Person1>

<Person2>
Free? How do these podcasters make money then? </Person2>

<Person1>
Good question! Some podcasts are supported by ads, just like traditional radio. Others rely on listener donations or subscriptions for bonus content. And then there are those that are purely a labor of love, shared for the joy of it. </Person1>

<Person2>
That's pretty cool. So anyone can just start a podcast? </Person2>

<Person1>
Pretty much!  The barrier to entry is surprisingly low. All you really need is a microphone, a computer, and something to say. Of course, producing a high-quality podcast takes more effort, but the basic tools are accessible to almost anyone. </Person1>

<Person2>
Huh, I might have to look into that.  But with millions of podcasts out there, how do you even find anything good to listen to? </Person2>

<Person1>
That's where podcast directories and apps like Apple Podcasts and Spotify come in. They're like giant libraries for podcasts, with categories, search functions, and recommendations based on your listening history.  </Person1>

<Person2>
So you're telling me there's a whole universe of audio content out there, just waiting to be discovered? </Person1>

<Person1>
Exactly! And it's only getting bigger and more diverse.  From independent creators to major media companies, everyone's jumping on the podcasting bandwagon.  </Person1>

<Person2>
Well, you've certainly opened my eyes to the world of podcasts.  I might have to ditch the music on my next dog walk and give it a try. </Person2>

<Person1>
Trust me, you won't regret it!  And hey, maybe you'll even be inspired to start your own podcast someday.  The airwaves are calling!  And that's it for today's episode of PODCASTFY - YOUR PERSONAL GenAI PODCAST. Catch you next time! </Person1> 
```

## File: `tests/data/transcripts/transcript_61815ffa72a7449a90b8e1601e233d1b.txt`
```
<Person1>
Welcome to PODCASTFY  - YOUR PERSONAL GenAI PODCAST.
</Person1>

<Person2>
Alright, let's get into it! What's the word on Natural Language Processing, or NLP as the cool kids call it? I keep hearing it everywhere!
</Person2>

<Person1>
<emphasis>NLP</emphasis>? Oh, it's not just a buzzword, my friend. It's revolutionizing how computers understand us... well, how they understand our <emphasis>language</emphasis>, at least.
</Person2>
So, it's basically teaching computers to read, write, maybe even gossip a little?
</Person1>
Think bigger! Imagine computers analyzing medical records to assist doctors, translating languages on the fly, or even summarizing complex research papers in seconds. That's the power of NLP!
</Person2>
Okay, that's some serious future stuff! But how does it actually work? Are we talking about some super-secret code only Silicon Valley gurus know?
</Person1>
Not really secret, but definitely complex. NLP combines the powers of computer science, artificial intelligence, and good old linguistics. It's all about giving computers the tools to process human language.
</Person2>
Tools like what? Tiny dictionaries and grammar textbooks for computers?
</Person1>
Kind of!  We're talking massive datasets of text and speech, called <emphasis>corpora</emphasis>.  NLP uses these to learn patterns, grammar rules, and even the sentiment behind words.
</Person2>
Sentiment? So, my computer could tell if I'm being sarcastic online? Finally!
</Person1>
Well, maybe not your sarcastic tweets just yet. But sentiment analysis is a big part of NLP, helping computers understand emotions in text, like in customer reviews.
</Person2>
Got it. So, how did we go from teaching computers basic grammar to this whole sentiment-analyzing, novel-writing AI?
</Person1>
It's been a journey, starting back in the 1950s. Early NLP relied heavily on hand-coded rules, kind of like giving computers a giant instruction manual for language.
</Person2>
Sounds tedious. Did it work?
</Person1>
It had its limitations.  These systems were rigid, easily confused by the nuances of human language. Remember, language is full of ambiguities, slang, and cultural contexts.
</Person2>
Right, like how "wicked" can be good or bad depending on where you're from.
</Person1>
Exactly!  That's where the statistical revolution in the '80s and '90s changed the game.  Researchers started using machine learning algorithms and those massive text datasets we talked about.
</Person2>
So, instead of programming every rule, computers started learning from the data itself?
</Person1>
Precisely! This led to breakthroughs in machine translation, speech recognition, and more. But even then, we were still limited by the need for hand-engineered features.
</Person2>
Hand-engineered features? Sounds like we're back to square one.
</Person1>
Not quite. This is where things get really interesting. Enter the era of neural networks and deep learning!
</Person2>
Ah, yes, the buzzwords of the century!
</Person1>
Buzzworthy for a reason! Neural networks, inspired by the human brain, can learn complex patterns from raw data without much hand-holding. This has led to even more accurate and sophisticated NLP models.
</Person2>
So, we're talking about computers that can actually understand the meaning behind our words, not just the rules?
</Person1>
Getting closer! We're now seeing models that can understand context, resolve ambiguities, and even generate human-quality text. Think chatbots that can hold a conversation, or AI writing tools that help authors.
</Person2>
Okay, this is blowing my mind! But what's next for NLP? Are we all going to have AI assistants that speak fluent sarcasm soon?
</Person1>
Well, sarcasm detection is still a work in progress. But the future of NLP is incredibly exciting! We're talking about even more sophisticated language models, a greater focus on multilingual processing, and a deeper understanding of the cognitive aspects of language.
</Person2>
Cognitive aspects? So, computers could understand not just what we say, but what we *mean*?
</Person1>
That's the ultimate goal!  Imagine AI that can understand humor, irony, and even cultural nuances. That's the next frontier of NLP, and it has the potential to revolutionize how we interact with technology.
</Person2>
Wow, I can't wait to see what the future holds! Thanks for breaking it down for me.
</Person1>
Anytime! And there you have it, folks, the incredible world of NLP!  Until next time on PODCASTFY!
```

## File: `usage/api.md`
```markdown

# Podcastfy REST API Documentation

## Overview

The Podcastfy API allows you to programmatically generate AI podcasts from various input sources. This document outlines the API endpoints and their usage.

## Using cURL with Podcastfy API

### Prerequisites
1. Confirm cURL installation:
```bash
curl --version
```

### API Request Flow
Making a prediction requires two sequential requests:
1. POST request to initiate processing - returns an `EVENT_ID`
2. GET request to fetch results - uses the `EVENT_ID` to fetch results

Between step 1 and 2, there is a delay of 1-3 minutes. We are working on reducing this delay and implementing a way to notify the user when the podcast is ready. Thanks for your patience!

### Basic Request Structure
```bash
# Step 1: POST request to initiate processing
# Make sure to include http:// or https:// in the URL
curl -X POST https://thatupiso-podcastfy-ai-demo.hf.space/gradio_api/call/process_inputs \
  -H "Content-Type: application/json" \
  -d '{
    "data": [
      "text_input",
      "https://yourwebsite.com",
      [],  # pdf_files
      [],  # image_files
      "gemini_key",
      "openai_key",
      "elevenlabs_key",
      2000,  # word_count
      "engaging,fast-paced",  # conversation_style
      "main summarizer",  # roles_person1
      "questioner",  # roles_person2
      "Introduction,Content,Conclusion",  # dialogue_structure
      "PODCASTFY",  # podcast_name
      "YOUR PODCAST",  # podcast_tagline
      "openai",  # tts_model
      0.7,  # creativity_level
      ""  # user_instructions
    ]
  }'

# Step 2: GET request to fetch results
curl -N https://thatupiso-podcastfy-ai-demo.hf.space/gradio_api/call/process_inputs/$EVENT_ID


# Example output result
event: complete
data: [{"path": "/tmp/gradio/bcb143f492b1c9a6dbde512557541e62f090bca083356be0f82c2e12b59af100/podcast_81106b4ca62542f1b209889832a421df.mp3", "url": "https://thatupiso-podcastfy-ai-demo.hf.space/gradio_a/gradio_api/file=/tmp/gradio/bcb143f492b1c9a6dbde512557541e62f090bca083356be0f82c2e12b59af100/podcast_81106b4ca62542f1b209889832a421df.mp3", "size": null, "orig_name": "podcast_81106b4ca62542f1b209889832a421df.mp3", "mime_type": null, "is_stream": false, "meta": {"_type": "gradio.FileData"}}]

```

You can download the file by extending the URL prefix "https://thatupiso-podcastfy-ai-demo.hf.space/gradio_a/gradio_api/file=" with the path to the file in variable `path`. (Note: The variable "url" above has a bug introduced by Gradio, so please ignore it.)

### Parameter Details
| Index | Parameter | Type | Description |
|-------|-----------|------|-------------|
| 0 | text_input | string | Direct text input for podcast generation |
| 1 | urls_input | string | URLs to process (include http:// or https://) |
| 2 | pdf_files | array | List of PDF files to process |
| 3 | image_files | array | List of image files to process |
| 4 | gemini_key | string | Google Gemini API key |
| 5 | openai_key | string | OpenAI API key |
| 6 | elevenlabs_key | string | ElevenLabs API key |
| 7 | word_count | number | Target word count for podcast |
| 8 | conversation_style | string | Conversation style descriptors (e.g. "engaging,fast-paced") |
| 9 | roles_person1 | string | Role of first speaker |
| 10 | roles_person2 | string | Role of second speaker |
| 11 | dialogue_structure | string | Structure of dialogue (e.g. "Introduction,Content,Conclusion") |
| 12 | podcast_name | string | Name of the podcast |
| 13 | podcast_tagline | string | Podcast tagline |
| 14 | tts_model | string | Text-to-speech model ("gemini", "openai", "elevenlabs", or "edge") |
| 15 | creativity_level | number | Level of creativity (0-1) |
| 16 | user_instructions | string | Custom instructions for generation |


## Using Python

### Installation

```bash
pip install gradio_client
```

### Quick Start

```python
from gradio_client import Client, handle_file

client = Client("thatupiso/Podcastfy.ai_demo")
```

### API Endpoints

#### Generate Podcast (`/process_inputs`)

Generates a podcast from provided text, URLs, PDFs, or images.

##### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| text_input | str | Yes | - | Raw text input for podcast generation |
| urls_input | str | Yes | - | Comma-separated URLs to process |
| pdf_files | List[filepath] | Yes | None | List of PDF files to process |
| image_files | List[filepath] | Yes | None | List of image files to process |
| gemini_key | str | No | "" | Google Gemini API key |
| openai_key | str | No | "" | OpenAI API key |
| elevenlabs_key | str | No | "" | ElevenLabs API key |
| word_count | float | No | 2000 | Target word count for podcast |
| conversation_style | str | No | "engaging,fast-paced,enthusiastic" | Conversation style descriptors |
| roles_person1 | str | No | "main summarizer" | Role of first speaker |
| roles_person2 | str | No | "questioner/clarifier" | Role of second speaker |
| dialogue_structure | str | No | "Introduction,Main Content Summary,Conclusion" | Structure of dialogue |
| podcast_name | str | No | "PODCASTFY" | Name of the podcast |
| podcast_tagline | str | No | "YOUR PERSONAL GenAI PODCAST" | Podcast tagline |
| tts_model | Literal['openai', 'elevenlabs', 'edge'] | No | "openai" | Text-to-speech model |
| creativity_level | float | No | 0.7 | Level of creativity (0-1) |
| user_instructions | str | No | "" | Custom instructions for generation |

##### Returns

| Type | Description |
|------|-------------|
| filepath | Path to generated audio file |

##### Example Usage

```python
from gradio_client import Client, handle_file

client = Client("thatupiso/Podcastfy.ai_demo")

# Generate podcast from URL
result = client.predict(
    text_input="",
    urls_input="https://example.com/article",
    pdf_files=[],
    image_files=[],
    gemini_key="your-gemini-key",
    openai_key="your-openai-key",
    word_count=1500,
    conversation_style="casual,informative",
    podcast_name="Tech Talk",
    tts_model="openai",
    creativity_level=0.8
)

print(f"Generated podcast: {result}")
```

### Error Handling

The API will return appropriate error messages for:
- Invalid API keys
- Malformed input
- Failed file processing
- TTS generation errors

### Rate Limits

Please be aware of the rate limits for the underlying services:
- Gemini API
- OpenAI API
- ElevenLabs API

## Notes

- At least one input source (text, URL, PDF, or image) must be provided
- API keys are required for corresponding services
- The generated audio file format is MP3
```

## File: `usage/cli.md`
```markdown
## CLI

Podcastfy can be used as a command-line interface (CLI) tool. See below some usage examples.
Please make sure you follow configuration instructions first - [See Setup](../../../README.md#setup).

1. Generate a podcast from URLs (using OpenAI TTS by default):
   ```
   python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2
   ```

2. Generate a podcast from URLs using ElevenLabs TTS:
   ```
   python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2 --tts-model elevenlabs
   ```

3. Generate a podcast from a file containing URLs:
   ```
   python -m podcastfy.client --file path/to/urls.txt
   ```

4. Generate a podcast from an existing transcript file:
   ```
   python -m podcastfy.client --transcript path/to/transcript.txt
   ```

5. Generate only a transcript (without audio) from URLs:
   ```
   python -m podcastfy.client --url https://example.com/article1 --transcript-only
   ```

6. Generate a podcast using a combination of URLs and a file:
   ```
   python -m podcastfy.client --url https://example.com/article1 --file path/to/urls.txt
   ```

7. Generate a podcast from image files:
   ```
   python -m podcastfy.client --image path/to/image1.jpg --image path/to/image2.png
   ```

8. Generate a podcast with a custom conversation configuration:
   ```
   python -m podcastfy.client --url https://example.com/article1 --conversation-config path/to/custom_config.yaml
   ```

9. Generate a podcast from URLs and images:
   ```
   python -m podcastfy.client --url https://example.com/article1 --image path/to/image1.jpg
   ```
   
10. Generate a transcript using a local LLM:
    ```
    python -m podcastfy.client --url https://example.com/article1 --transcript-only --local
    ```

11. Generate a podcast from raw text input:
    ```
    python -m podcastfy.client --text "Your raw text content here that you want to convert into a podcast"
    ```

12. Generate a longform podcast from URLs:
    ```
    python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2 --longform
    ```

For more information on available options, use:
   ```
   python -m podcastfy.client --help
   ```
```

## File: `usage/config.md`
```markdown
# Podcastfy Configuration

## API keys

The project uses a combination of a `.env` file for managing API keys and sensitive information, and a `config.yaml` file for non-sensitive configuration settings. Follow these steps to set up your configuration:

1. Create a `.env` file in the root directory of the project.
2. Add your API keys and other sensitive information to the `.env` file. For example:

   ```
   GEMINI_API_KEY=your_gemini_api_key_here
   ELEVENLABS_API_KEY=your_elevenlabs_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## API Key Requirements

The API Keys required depend on the model you are using for transcript generation and audio generation.

- Transcript generation (LLMs):

  - By default, Podcastfy uses Google's `gemini-2.5-flash` model. Hence, you need to set `GEMINI_API_KEY`.
  - See how to configure other LLMs [here](how-to.md#custom-llm-support).

- Audio generation (TTS):
  - By default, Podcastfy uses OpenAI TTS. Hence, you need to set `OPENAI_API_KEY`.
  - Additional supported models are ElevenLabs ('elevenlabs'), Microsoft Edge ('edge') and Google TTS ('gemini'). All but Edge require an API key.

> [!Note]
> Never share your `.env` file or commit it to version control. It contains sensitive information that should be kept private. The `config.yaml` file can be shared and version-controlled as it doesn't contain sensitive data.

## Example Configurations

Here's a table showing example configurations:

| Configuration        | Base LLM  | TTS Model              | API Keys Required                 |
| -------------------- | --------- | ---------------------- | --------------------------------- |
| Default              | Gemini    | OpenAI                 | GEMINI_API_KEY and OPENAI_API_KEY |
| No API Keys Required | Local LLM | Edge                   | None                              |
| Recommended          | Gemini    | 'geminimulti' (Google) | GEMINI_API_KEY                    |

In our experience, Google's Multispeaker TTS model ('geminimulti') is the best model in terms of quality followed by ElevenLabs which offers great customization (voice options and multilingual capability). Google's multispeaker TTS model is limited to English only and requires an additional set up step.

## Setting up Google TTS Model

You can use Google's Multispeaker TTS model by setting the `tts_model` parameter to `geminimulti` in `Podcastfy`.

Google's Multispeaker TTS model requires a Google Cloud API key, you can use the same API key you are already using for Gemini or create a new one. After you have secured your API Key there are two additional steps in order to use Google Multispeaker TTS model:

- Step 1: You will need to enable the Cloud Text-to-Speech API on the API key.

  - Go to "https://console.cloud.google.com/apis/dashboard"
  - Select your project (or create one by clicking on project list and then on "new project")
  - Click "+ ENABLE APIS AND SERVICES" at the top of the screen
  - Enter "text-to-speech" into the search box
  - Click on "Cloud Text-to-Speech API" and then on "ENABLE"
  - You should be here: "https://console.cloud.google.com/apis/library/texttospeech.googleapis.com?project=..."

- Step 2: You need to add the Cloud Text-to-Speech API permission to the API KEY you're using on the Google Cloud console.

  - Go to https://console.cloud.google.com/apis/credentials
  - Click on whatever key you're using for Gemini
  - Go down to API Restrictions and add the Cloud Text-to-Speech API

<br>

⚠️**NOTE :**<br>
By default, **Google Multi-Speaker voices** are only available to **allowlisted projects**. If you wish to use these voices, follow the steps below: <br>

- **Prerequisites:** A **paid Google Cloud support subscription** is required to proceed.
- **Request Access:** You'll need to **contact Google Cloud Support** to get Multi-Speaker voices enabled for your project.
- **Common Error:** If Multi-Speaker voices are not enabled, you will encounter the following runtime error:
  ```bash
  RuntimeError: Failed to generate audio: 403 Multi-speaker voices are only available to allowlisted    projects
  ```
- **How to Proceed:**
  - Navigate to the **Support** section in your **GCP Console**. <br>
  - Open a new case under **"Cases"** and provide the necessary project details. <br>
  - Google Cloud Support should be able to assist you in enabling this feature. <br>
    <br>
    ![google-multispeaker-support](../data/images/google-multispeaker-support.png)
    <br>

Phew!!! That was a lot of steps but you only need to do it once and you might be impressed with the quality of the audio. See [Google TTS](https://cloud.google.com/text-to-speech) for more details. Thank you @mobarski and @evandempsey for the help!

## Conversation Configuration

See [conversation_custom.md](conversation_custom.md) for more details.

## Running Local LLMs

See [local_llm.md](local_llm.md) for more details.

## Optional configuration

The `config.yaml` file in the root directory contains non-sensitive configuration settings. You can modify this file to adjust various parameters such as output directories, text-to-speech settings, and content generation options.

The application will automatically load the environment variables from `.env` and the configuration settings from `config.yaml` when it runs.

See [Configuration](config_custom.md) if you would like to further customize settings.
```

## File: `usage/config_custom.md`
```markdown
# Podcastfy Advanced Configuration Guide

Podcastfy uses a `config.yaml` file to manage various settings and parameters. This guide explains each configuration option available in the file.



## Content Generator

- `gemini_model`: "gemini-2.5-flash"
  - The Gemini AI model used for content generation.
- `max_output_tokens`: 8192
  - Maximum number of tokens for the output generated by the AI model.
- `temperature`: 1
  - Controls randomness in the AI's output. 0 means deterministic responses. Range for gemini-2.5-flash: 0.0 - 2.0 (default: 1.0)
- `langchain_tracing_v2`: false
  - Enables LangChain tracing for debugging and monitoring. If true, requires langsmith api key

## Content Extractor

- `youtube_url_patterns`:
  - Patterns to identify YouTube URLs.
  - Current patterns: "youtube.com", "youtu.be"

## Website Extractor

- `markdown_cleaning`:
  - `remove_patterns`:
    - Patterns to remove from extracted markdown content.
    - Current patterns remove image links, hyperlinks, and URLs.

## YouTube Transcriber

- `remove_phrases`:
  - Phrases to remove from YouTube transcriptions.
  - Current phrase: "[music]"

## Logging

- `level`: "INFO"
  - Default logging level.
- `format`: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  - Format string for log messages.


## Website Extractor

- `markdown_cleaning`:
	- `remove_patterns`:
		- Additional patterns to remove from extracted markdown content:
		- '\[.*?\]': Remove square brackets and their contents
		- '\(.*?\)': Remove parentheses and their contents
		- '^\s*[-*]\s': Remove list item markers
		- '^\s*\d+\.\s': Remove numbered list markers
		- '^\s*#+': Remove markdown headers
- `unwanted_tags`:
	- HTML tags to be removed during extraction:
		- 'script', 'style', 'nav', 'footer', 'header', 'aside', 'noscript'
- `user_agent`: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
	- User agent string to be used for web requests
- `timeout`: 10
	- Request timeout in seconds for web scraping


```

## File: `usage/conversation_custom.md`
```markdown
# Podcastfy Conversation Configuration

Podcastfy offers a range of customization options to tailor your AI-generated podcasts. This document outlines how you can adjust parameters such as conversation style, word count, and dialogue structure to suit your specific needs.


## Table of Contents

1. [Parameters](#parameters)
2. [Customization Examples](#customization-examples)
   1. [Academic Debate](#academic-debate)
   2. [Storytelling Adventure](#storytelling-adventure)
3. [Customization Scenarios](#customization-scenarios)
   1. [Using the Python Package](#using-the-python-package)
   2. [Using the CLI](#using-the-cli)
4. [Notes of Caution](#notes-of-caution)


## Conversation Parameters

Podcastfy uses the default conversation configuration stored in [podcastfy/conversation_config.yaml](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy/conversation_config.yaml).

| Parameter | Default Value | Type | Description |
|-----------|---------------|------|-------------|
| conversation_style | ["engaging", "fast-paced", "enthusiastic"] | list[str] | Styles to apply to the conversation |
| roles_person1 | "main summarizer" | str | Role of the first speaker |
| roles_person2 | "questioner/clarifier" | str | Role of the second speaker |
| dialogue_structure | ["Introduction", "Main Content Summary", "Conclusion"] | list[str] | Structure of the dialogue |
| podcast_name | "PODCASTIFY" | str | Name of the podcast |
| podcast_tagline | "Your Personal Generative AI Podcast" | str | Tagline for the podcast |
| output_language | "English" | str | Language of the output |
| engagement_techniques | ["rhetorical questions", "anecdotes", "analogies", "humor"] | list[str] | Techniques to engage the audience |
| creativity | 1 | float | Level of creativity/temperature (0-1) |
| user_instructions | "" | str | Custom instructions to guide the conversation focus and topics |
| max_num_chunks | 7 | int | Maximum number of rounds of discussions in longform |
| min_chunk_size | 600 | int | Minimum number of characters to generate a round of discussion in longform |

## Text-to-Speech (TTS) Settings

Podcastfy uses the default TTS configuration stored in [podcastfy/conversation_config.yaml](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy/conversation_config.yaml).

### ElevenLabs TTS

- `default_voices`:
  - `question`: "Chris"
    - Default voice for questions in the podcast.
  - `answer`: "Jessica"
    - Default voice for answers in the podcast.
- `model`: "eleven_multilingual_v2"
  - The ElevenLabs TTS model to use.

### OpenAI TTS

- `default_voices`:
  - `question`: "echo"
    - Default voice for questions using OpenAI TTS.
  - `answer`: "shimmer"
    - Default voice for answers using OpenAI TTS.
- `model`: "tts-1-hd"
  - The OpenAI TTS model to use.

### Gemini Multi-Speaker TTS
- `default_voices`:
  - `question`: "R"
    - Default voice for questions using Gemini Multi-Speaker TTS.
  - `answer`: "S"
    - Default voice for answers using Gemini Multi-Speaker TTS.
  - `model`: "en-US-Studio-MultiSpeaker"
    - Model to use for Gemini Multi-Speaker TTS.
  - `language`: "en-US"
    - Language of the voices.

### Gemini TTS
- `default_voices`:
  - `question`: "en-US-Journey-D"
    - Default voice for questions using Gemini TTS.
  - `answer`: "en-US-Journey-O"
    - Default voice for answers using Gemini TTS.

### Edge TTS

- `default_voices`:
  - `question`: "en-US-JennyNeural"
    - Default voice for questions using Edge TTS.
  - `answer`: "en-US-EricNeural"
    - Default voice for answers using Edge TTS.

### General TTS Settings

- `default_tts_model`: "openai"
  - Default text-to-speech model to use.
- `output_directories`:
  - `transcripts`: "./data/transcripts"
    - Directory for storing generated transcripts.
  - `audio`: "./data/audio"
    - Directory for storing generated audio files.
- `audio_format`: "mp3"
  - Format of the generated audio files.
- `temp_audio_dir`: "data/audio/tmp/"
  - Temporary directory for audio processing.
- `ending_message`: "Bye Bye!"
  - Message to be appended at the end of the podcast.

## Customization Examples

These examples demonstrate how conversations can be altered to suit different purposes, from academic rigor to creative storytelling. The comments explain the rationale behind each choice, helping users understand how to tailor the configuration to their specific needs.

### Academic Debate

This configuration transforms the podcast into a formal academic debate, encouraging deep analysis and critical thinking. It's designed for educational content or in-depth discussions on complex topics.

```python
{
    "word_count": 3000,  # Longer to allow for detailed arguments
    "conversation_style": ["formal", "analytical", "critical"],  # Appropriate for academic discourse
    "roles_person1": "thesis presenter",  # Presents the main argument
    "roles_person2": "counterargument provider",  # Challenges the thesis
    "dialogue_structure": [
        "Opening Statements",
        "Thesis Presentation",
        "Counterarguments",
        "Rebuttals",
        "Closing Remarks"
    ],  # Mimics a structured debate format
    "podcast_name": "Scholarly Showdown",
    "podcast_tagline": "Where Ideas Clash and Knowledge Emerges",
    "engagement_techniques": [
        "socratic questioning",
        "historical references",
        "thought experiments"
    ],  # Techniques to stimulate critical thinking
    "creativity": 0  # Low creativity to maintain focus on facts and logic
}
```

### Storytelling Adventure

This configuration turns the podcast into an interactive storytelling experience, engaging the audience in a narrative journey. It's ideal for fiction podcasts or creative content marketing.

```yaml
word_count: 1000  # Shorter to maintain pace and suspense
conversation_style: 
  - narrative
  - suspenseful
  - descriptive  # Creates an immersive story experience
roles_person1: storyteller
roles_person2: audience participator  # Allows for interactive elements
dialogue_structure: 
  - Scene Setting
  - Character Introduction
  - Rising Action
  - Climax
  - Resolution  # Follows classic storytelling structure
podcast_name: Tale Spinners
podcast_tagline: Where Every Episode is an Adventure
engagement_techniques: 
  - cliffhangers
  - vivid imagery
  - audience prompts  # Keeps the audience engaged and coming back
creativity: 0.9 # High creativity for unique and captivating stories
```

## Customization Scenarios

### Using the Python Package

When using the Podcastfy Python package, you can customize the conversation by passing a dictionary to the `conversation_config` parameter:

```python
from podcastfy.client import generate_podcast

custom_config = {
    "word_count": 200,
    "conversation_style": ["casual", "humorous"],
    "podcast_name": "Tech Chuckles",
    "creativity": 0.7
}

generate_podcast(
    urls=["https://example.com/tech-news"],
    conversation_config=custom_config
)
```

### Using the CLI

When using the Podcastfy CLI, you can specify a path to a YAML file containing your custom configuration:

```bash
podcastfy --url https://example.com/tech-news --conversation-config path/to/custom_config.yaml
```

The `custom_config.yaml` file should contain your configuration in YAML format:

```yaml
word_count: 200
conversation_style: 
  - casual
  - humorous
podcast_name: Tech Chuckles
creativity: 0.7
```


## Notes of Caution

- The `word_count` is a target, and the AI may generate more or less than the specified word count. Low word counts are more likely to generate high-level discussions, while high word counts are more likely to generate detailed discussions.
- The `output_language` defines both the language of the transcript and the language of the audio. Here's some relevant information:
  - Bottom-line: non-English transcripts are good enough but non-English audio is work-in-progress.
  - Transcripts are generated using Google's Gemini 1.5 Pro by default, which supports 100+ languages. Other user-defined models may or may not support non-English languages.
  - Audio is generated using `openai` (default), `elevenlabs`, `gemini`, `geminimulti` or `edge` TTS models. 
    - The `gemini`(Google) TTS model supports multiple languages and can be controlled by the `output_language` parameter and respective voice choices. Eg. `output_language="Tamil"`, `question="ta-IN-Standard-A"`, `answer="ta-IN-Standard-B"`. Refer to [Google Cloud Text-to-Speech documentation](https://cloud.google.com/text-to-speech/docs/voices) for more details.
    - The `geminimulti`(Google) TTS model supports only English voices. Also, not every Google Cloud project might have access to multi-speaker voices (Eg. `en-US-Studio-MultiSpeaker`). In case if you get - `"Multi-speaker voices are only available to allowlisted projects."`, you can fallback to `gemini` TTS model.
    - The `openai` TTS model supports multiple languages automatically, however non-English voices still present sub-par quality in my experience.
    - The `elevenlabs` TTS model has English voices by default, in order to use a non-English voice you would need to download a custom voice for the target language in your `elevenlabs` account settings and then set the `text_to_speech.elevenlabs.default_voices` parameters to the voice you want to use in the [config.yaml file](https://github.com/pedroslopez/podcastfy/blob/main/podcastfy/config.yaml) (this config file is only available in the source code of the project, not in the pip package, hence if you are using the pip package you will not be able to change the ElevenLabs voice). For more information on ElevenLabs voices, visit [ElevenLabs Voice Library](https://elevenlabs.io/voice-library)
```

## File: `usage/docker.md`
```markdown
# Docker Setup Guide for Podcastfy

This guide explains how to use Docker to run Podcastfy in your local environment or for development.

## Prerequisites

- Docker installed on your system [1]
- Docker Compose [1]
- API keys [2]

[1] See Appendix A for detailed installation instructions.
[2] See [config.md](https://github.com/souzatharsis/podcastfy/blob/main/usage/config.md) for more details.

## Available Images

Podcastfy provides pre-built Docker images through GitHub Container Registry (ghcr.io):

1. **Production Image**: `ghcr.io/souzatharsis/podcastfy:latest`
   - Contains the latest PyPI release
   - Recommended for production use

2. **Development Image**: `ghcr.io/souzatharsis/podcastfy:dev`
   - Includes development tools and dependencies
   - Used for contributing and development

## Deployment

### Quick Deployment Steps

1. Create a new directory and navigate to it:
```bash
mkdir -p /path/to/podcastfy
cd /path/to/podcastfy
```

2. Create a `.env` file with your API keys (see [config.md](https://github.com/souzatharsis/podcastfy/blob/main/usage/config.md) for more details):
```plaintext
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key  # Optional: only needed for OpenAI TTS
```

3. Create a `docker-compose.yml`:
```yaml
version: '3.8'

services:
  podcastfy:
    image: ghcr.io/souzatharsis/podcastfy:latest
    environment:
      - GEMINI_API_KEY=${GEMINI_API_KEY}
      - OPENAI_API_KEY=${OPENAI_API_KEY}
    ports:
      - "8000:8000"
    command: python3 -m podcastfy.server
    healthcheck:
      test: ["CMD", "python3", "-c", "import podcastfy"]
      interval: 30s
      timeout: 10s
      retries: 3
```

4. Pull and start the container:
```bash
docker pull ghcr.io/souzatharsis/podcastfy:latest
docker-compose up podcastfy
```

The service will be available at `http://localhost:8000`

### Directory Structure
```
/path/to/podcastfy/
├── .env                  # Environment variables
└── docker-compose.yml    # Docker Compose configuration
```

## Development Setup

### Using Pre-built Development Image

1. Pull the development image:
```bash
docker pull ghcr.io/souzatharsis/podcastfy:dev
```

2. Clone the repository and start development environment:
```bash
git clone https://github.com/souzatharsis/podcastfy.git
cd podcastfy
docker-compose up podcastfy-dev
```

### Building Locally

Alternatively, you can build the images locally:
```bash
# Build production image
docker-compose build podcastfy

# Build development image
docker-compose build podcastfy-dev
```

## Running Tests

Run the test suite using:
```bash
docker-compose up test
```

This will run tests in parallel using pytest-xdist.

## Environment Variables

Required environment variables:
- `GEMINI_API_KEY` - Your Google Gemini API key
- `OPENAI_API_KEY` - Your OpenAI API key (optional: only needed for OpenAI TTS)

## Container Details

### Production Container
- Based on Ubuntu 24.04
- Installs Podcastfy from PyPI
- Includes FFmpeg for audio processing
- Runs in a Python virtual environment
- Exposed port: 8000

### Development Container
- Based on Ubuntu 24.04
- Includes development tools (flake8, pytest)
- Mounts local code for live development
- Runs in editable mode (`pip install -e .`)
- Exposed port: 8001

## Continuous Integration

The Docker images are automatically:
- Built and tested on every push to main branch
- Built and tested for all pull requests
- Published to GitHub Container Registry
- Tagged with version numbers for releases (v*.*.*)

## Health Checks

All services include health checks that:
- Run every 30 seconds
- Verify Podcastfy can be imported
- Timeout after 10 seconds
- Retry up to 3 times

## Common Commands

```bash
# Pull latest production image
docker pull ghcr.io/souzatharsis/podcastfy:latest

# Pull development image
docker pull ghcr.io/souzatharsis/podcastfy:dev

# Start production service
docker-compose up podcastfy

# Start development environment
docker-compose up podcastfy-dev

# Run tests
docker-compose up test

# Build images locally
docker-compose build

# View logs
docker-compose logs

# Stop all containers
docker-compose down
```

## Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your `.env` file exists and contains valid API keys
   - Check if the environment variables are properly passed to the container

2. **Port Conflicts**
   - Ensure ports 8000 (production) and 8001 (development) are available
   - Modify the port mappings in `docker-compose.yml` if needed

3. **Volume Mounting Issues (Development)**
   - Verify the correct path to your local code
   - Check permissions on the mounted directories

4. **Image Pull Issues**
   - Ensure you have access to the GitHub Container Registry
   - If you see "unauthorized" errors, the image might be private
   - Try authenticating with GitHub: `docker login ghcr.io -u YOUR_GITHUB_USERNAME`

### Verifying Installation

You can verify your installation by checking if the package can be imported:
```bash
# Check production version
docker run --rm ghcr.io/souzatharsis/podcastfy:latest python3 -c "import podcastfy"

# Check development setup
docker-compose exec podcastfy-dev python3 -c "import podcastfy"
```

## System Requirements

Minimum requirements:
- Docker Engine 20.10.0 or later
- Docker Compose 2.0.0 or later
- Sufficient disk space for Ubuntu base image (~400MB)
- Additional space for Python packages and FFmpeg

## Support

If you encounter any issues:
1. Check the container logs: `docker-compose logs`
2. Verify all prerequisites are installed
3. Ensure all required environment variables are set
4. Open an issue on the [Podcastfy GitHub repository](https://github.com/souzatharsis/podcastfy/issues)

## Appendix A: Detailed Installation Guide

### Installing Docker

#### Windows
1. Download and install [Docker Desktop for Windows](https://docs.docker.com/desktop/install/windows-install/)
   - For Windows 10/11 Pro, Enterprise, or Education: Enable WSL 2 and Hyper-V
   - For Windows 10 Home: Enable WSL 2
2. After installation, start Docker Desktop
3. Verify installation:
```bash
docker --version
```

#### macOS
1. Download and install [Docker Desktop for Mac](https://docs.docker.com/desktop/install/mac-install/)
   - For Intel chip: Download Intel package
   - For Apple chip: Download Apple Silicon package
2. After installation, start Docker Desktop
3. Verify installation:
```bash
docker --version
```

#### Ubuntu/Debian
```bash
# Remove old versions
sudo apt-get remove docker docker-engine docker.io containerd runc

# Install prerequisites
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

# Set up repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker Engine
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin

# Add your user to docker group (optional, to run docker without sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verify installation
docker --version
```

#### Other Linux Distributions
- [CentOS](https://docs.docker.com/engine/install/centos/)
- [Fedora](https://docs.docker.com/engine/install/fedora/)
- [RHEL](https://docs.docker.com/engine/install/rhel/)

### Installing Docker Compose

Docker Compose is included with Docker Desktop for Windows and macOS. For Linux:

```bash
# Download the current stable release
sudo curl -L "https://github.com/docker/compose/releases/download/v2.24.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

# Apply executable permissions
sudo chmod +x /usr/local/bin/docker-compose

# Verify installation
docker-compose --version
```

### Post-Installation Steps

1. Verify Docker is running:
```bash
docker run hello-world
```

2. Configure Docker to start on boot (Linux only):
```bash
sudo systemctl enable docker.service
sudo systemctl enable containerd.service
```

## Appendix B: Getting API Keys

### Google Gemini API Key
1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Create or sign in to your Google account
3. Click "Create API Key"
4. Copy and save your API key

### OpenAI API Key
You only need an OpenAI API key if you want to use the OpenAI Text-to-Speech model.
1. Visit [OpenAI API Keys](https://platform.openai.com/api-keys)
2. Create or sign in to your OpenAI account
3. Click "Create new secret key"
4. Copy and save your API key

## Appendix C: Installation Validation

After installing all prerequisites, verify everything is set up correctly:

```bash
# Check Docker version
docker --version

# Check Docker Compose version
docker-compose --version

# Verify Docker daemon is running
docker ps

# Test Docker functionality
docker run hello-world
```
```

## File: `usage/examples.ipynb`
```
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from podcastfy.client import generate_podcast"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "%pip install ipython\n",
    "from IPython.display import Audio, display\n",
    "\n",
    "def embed_audio(audio_file):\n",
    "\t\"\"\"\n",
    "\tEmbeds an audio file in the notebook, making it playable.\n",
    "\n",
    "\tArgs:\n",
    "\t\taudio_file (str): Path to the audio file.\n",
    "\t\"\"\"\n",
    "\ttry:\n",
    "\t\tdisplay(Audio(audio_file))\n",
    "\t\tprint(f\"Audio player embedded for: {audio_file}\")\n",
    "\texcept Exception as e:\n",
    "\t\tprint(f\"Error embedding audio: {str(e)}\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generate a podcast from images"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Senecio, 1922 (Paul Klee) and Connection of Civilizations (2017) by Gheorghe Virtosu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "conversation_config = {\n",
    "    \"roles_person1\": \"Abstract Art Ph.D. Professor\",\n",
    "    \"roles_person2\": \"Abstract Art Grad Student\",\n",
    "    \"podcast_name\": \"Artfy Podcast\",\n",
    "    \"podcast_tagline\": \"Because Art is Everywhere\",\n",
    "    \"creativity\": 1\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "images = [\"https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/Senecio.jpeg\",\n",
    "          \"https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/connection.jpg\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generating podcast...\n",
      "Transcript saved to ./data/transcripts/transcript_078f0148283e435989a60b456938bfda.txt\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-16 11:22:08,434 - podcastfy.client - INFO - Podcast generated successfully using geminimulti TTS model\n"
     ]
    }
   ],
   "source": [
    "audio_file = generate_podcast(image_paths=images, \n",
    "                              tts_model=\"geminimulti\", \n",
    "                              conversation_config=conversation_config)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "embed_audio(audio_file)\n",
    "#./data/audio/podcast_da40e428614945579ec1c9819cd4af5e.mp3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The Great Wave off Kanagawa, 1831 (Hokusai) and Takiyasha the Witch and the Skeleton Spectre, c. 1844 (Kuniyoshi)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "images = [\"https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/japan_1.jpg\",\n",
    "          \"https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/japan2.jpg\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "conversation_config = {\n",
    "    \"roles_person1\": \"Abstract Art Ph.D.\",\n",
    "    \"roles_person2\": \"Creative Abstract Artist\",\n",
    "    \"podcast_name\": \"Japan Arts Podcast\",\n",
    "    \"podcast_tagline\": \"Because Art is Everywhere\",\n",
    "    \"creativity\": 1,\n",
    "    \"user_instructions\": \"Speakers should often overlap in their sentences. The conversation should be about the relationship between art and life. Person2 should make connections with her own life!\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/home/tobias/src/podcastfy-pypi/podcastfy/.venv/lib/python3.11/site-packages/tqdm/auto.py:21: TqdmWarning: IProgress not found. Please update jupyter and ipywidgets. See https://ipywidgets.readthedocs.io/en/stable/user_install.html\n",
      "  from .autonotebook import tqdm as notebook_tqdm\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generating podcast...\n",
      "Transcript saved to ./data/transcripts/transcript_9ccfca254a584700ab325f6e65944b1c.txt\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-16 13:02:35,134 - podcastfy.client - INFO - Podcast generated successfully using geminimulti TTS model\n"
     ]
    }
   ],
   "source": [
    "audio_file = generate_podcast(image_paths=images, \n",
    "                              tts_model=\"geminimulti\", \n",
    "                              conversation_config=conversation_config)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "embed_audio(audio_file)\n",
    "#./data/audio/podcast_4917be8e74514dd0b3581d61e6719f38.mp3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Pop culture icon Taylor Swift and Mona Lisa, 1503 (Leonardo da Vinci)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "images = [\"https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/taylor.png\",\n",
    "          \"https://raw.githubusercontent.com/souzatharsis/podcastfy/refs/heads/main/data/images/monalisa.jpeg\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "conversation_config = {\n",
    "    \"roles_person1\": \"Young Arts Ph.D.\",\n",
    "    \"roles_person2\": \"one of the most influential media figures and businesswomen of the modern era\",\n",
    "    \"podcast_name\": \"Podcastify\",\n",
    "    \"podcast_tagline\": \"Your Generative AI Podcast\",\n",
    "    \"creativity\": 1,\n",
    "    \"user_instructions\": \"Speakers should often overlap in their sentences. The conversation should be about the relationship between art and life. Person2 should make connections with her own life!\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generating podcast...\n",
      "Transcript saved to ./data/transcripts/transcript_89f49ff34e3e44c7b15480959d16f162.txt\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-16 13:08:41,907 - podcastfy.client - INFO - Podcast generated successfully using geminimulti TTS model\n"
     ]
    }
   ],
   "source": [
    "audio_file = generate_podcast(image_paths=images, \n",
    "                              tts_model=\"geminimulti\",\n",
    "                              conversation_config=conversation_config)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "embed_audio(audio_file)\n",
    "#./data/audio/podcast_0ed7b94e89e149ab9732494e4b18b3d7.mp3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "#audio_file = generate_podcast(urls=[\"../data/pdf/s41598-024-58826-w.pdf\"], \n",
    "#                              tts_model=\"geminimulti\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "#embed_audio(audio_file)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Generate a podcast from a Text"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Personal Website"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-16 13:11:16,106 - podcastfy.client - INFO - Processing 1 links\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Generating podcast...\n",
      "Transcript saved to ./data/transcripts/transcript_08e8b0f295ea48e4aa44f1b17e007d82.txt\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-11-16 13:11:44,927 - podcastfy.client - INFO - Podcast generated successfully using geminimulti TTS model\n"
     ]
    }
   ],
   "source": [
    "audio_file = generate_podcast(urls=[\"www.souzatharsis.com\"], \n",
    "                              tts_model=\"geminimulti\")\n",
    "#./data/transcripts/transcript_08e8b0f295ea48e4aa44f1b17e007d82.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "embed_audio(audio_file)\n",
    "#./data/audio/podcast_d3a3660df7d94a5991c905bff141322c.mp3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Book"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Benjamin Franklin's Autobiography (`longform=True`)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "audio_file = generate_podcast(urls=[\"https://www.gutenberg.org/cache/epub/20203/pg20203.txt\"], \n",
    "                              tts_model=\"geminimulti\",\n",
    "                              longform=True)\n",
    "#./data/transcripts/transcript_331c08ac7ef54623969a383f998c4bce.txt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "embed_audio(audio_file)\n",
    "#./data/audio/podcast_f1bc29aa1c1c42e98f83c6ea14b07add.mp3"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Youtube Video"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Lex Fridman Podcast: Dario Amodei Anthropic's CEO (`longform=True`)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "audio_file = generate_podcast(urls=[\"https://www.youtube.com/watch?v=ugvHCXCOmm4\"], \n",
    "                              tts_model=\"geminimulti\",\n",
    "                              longform=True)\n",
    "#./data/transcripts/transcript_0a4e53d85f9643f3a28bd59281e4e9cd.txt\n",
    "\n",
    "embed_audio(audio_file)\n",
    "#./data/audio/podcast_136cbe471d2c406395b13449b5bc44be.mp3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
```

## File: `usage/fast_api.md`
```markdown
# FastAPI Implementation for Podcastify

This PR adds a FastAPI implementation for serving the Podcastify functionality via REST API.

## Features
- Podcast generation endpoint
- Audio file serving
- Configuration merging
- Environment variable handling

## Usage
See `usage/fast_api_example.py` for usage example.

## Requirements
- Uvicorn
- FastAPI
- aiohttp
- pyyaml
```

## File: `usage/fast_api_example.py`
```python
"""
Example implementation of the Podcastify FastAPI client.

This module demonstrates how to interact with the Podcastify API
to generate and download podcasts.
"""

import asyncio
import aiohttp
import json
import os
from pathlib import Path
from typing import Dict, Any


def get_default_config() -> Dict[str, Any]:
	"""
	Returns default configuration for podcast generation.

	Returns:
		Dict[str, Any]: Default configuration dictionary
	"""
	return {
		"generate_podcast": True,
		"google_key": "YOUR_GEMINI_API_KEY",
		"openai_key": "YOUR_OPENAI_API_KEY",
		"urls": ["https://www.phenomenalworld.org/interviews/swap-structure/"],
		"name": "Central Clearing Risks",
		"tagline": "Exploring the complexities of financial systemic risk",
		"creativity": 0.8,
		"conversation_style": ["engaging", "informative"],
		"roles_person1": "main summarizer",
		"roles_person2": "questioner",
		"dialogue_structure": ["Introduction", "Content", "Conclusion"],
		"tts_model": "openai",
		"is_long_form": False,
		"engagement_techniques": ["questions", "examples", "analogies"],
		"user_instructions": "Dont use the world Dwelve",
		"output_language": "English"
	}


async def generate_podcast() -> None:
	"""
	Generates a podcast using the Podcastify API and downloads the result.
	"""
	async with aiohttp.ClientSession() as session:
		try:
			print("Starting podcast generation...")
			async with session.post(
				"http://localhost:8080/generate",
				json=get_default_config()
			) as response:
				if response.status != 200:
					print(f"Error: Server returned status {response.status}")
					return
				
				result = await response.json()
				if "error" in result:
					print(f"Error: {result['error']}")
					return

				await download_podcast(session, result)

		except aiohttp.ClientError as e:
			print(f"Network error: {str(e)}")
		except Exception as e:
			print(f"Unexpected error: {str(e)}")


async def download_podcast(session: aiohttp.ClientSession, result: Dict[str, str]) -> None:
	"""
	Downloads the generated podcast file.

	Args:
		session (aiohttp.ClientSession): Active client session
		result (Dict[str, str]): API response containing audioUrl
	"""
	audio_url = f"http://localhost:8080{result['audioUrl']}"
	print(f"Podcast generated! Downloading from: {audio_url}")

	async with session.get(audio_url) as audio_response:
		if audio_response.status == 200:
			filename = os.path.join(
				str(Path.home() / "Downloads"), 
				result['audioUrl'].split('/')[-1]
			)
			with open(filename, 'wb') as f:
				f.write(await audio_response.read())
			print(f"Downloaded to: {filename}")
		else:
			print(f"Failed to download audio. Status: {audio_response.status}")


if __name__ == "__main__":
	try:
		asyncio.run(generate_podcast())
	except KeyboardInterrupt:
		print("\nProcess interrupted by user")
	except Exception as e:
		print(f"Error: {str(e)}")
```

## File: `usage/how-to.md`
```markdown
# How to

All assume you have podcastfy installed and running.

## Table of Contents

- [Custom LLM Support](#custom-llm-support)
- [Running Local LLMs](#running-local-llms)
- [How to use your own voice in audio podcasts](#how-to-use-your-own-voice-in-audio-podcasts)
- [How to customize the conversation](#how-to-customize-the-conversation)
- [How to generate multilingual content](#how-to-generate-multilingual-content)
- [How to steer the conversation](#how-to-steer-the-conversation)
- [How to generate longform podcasts](#how-to-generate-longform-podcasts)


## Custom LLM Support

Podcastfy offers a range of LLM models for generating transcripts including OpenAI, Anthropic, Google as well as local LLM models.

### Cloud-based LLMs

By default, Podcastfy uses Google's `gemini-2.5-flash` model. To select a particular cloud-based LLM model, users can pass the `llm_model_name` and `api_key_label` parameters to the `generate_podcast` function. See [full list of supported models](https://docs.litellm.ai/docs/providers) for more details.

For example, to use OpenAI's `gpt-4-turbo` model, users can pass `llm_model_name="gpt-4-turbo"` and `api_key_label="OPENAI_API_KEY"`.

```python
audio_file = generate_podcast(
    urls=["https://en.wikipedia.org/wiki/Artificial_intelligence"],
    llm_model_name="gpt-4-turbo",
    api_key_label="OPENAI_API_KEY"
)
```

Remember to have the correct API key label and value in your environment variables (`.env` file).

### Running Local LLMs

See [local_llm.md](local_llm.md) for more details.

## How to use your own voice in audio podcasts

You just need to use ElevenLabs TSS backend and pass a custom config to use your voice instead of podcastfy's default:
  
1. Create elevenlabs account, get and [set up](https://github.com/souzatharsis/podcastfy/blob/main/usage/config.md) eleven labs API KEY

2. Clone your voice on elevenlabs website (let's say its name is 'Robbert')

4. Create custom conversation config (let's call it custom_config.yaml) to use your voice name instead of the default as described [here](https://github.com/souzatharsis/podcastfy/blob/main/usage/conversation_custom.md#text-to-speech-tts-settings). Set either question or answer voice below to 'Robbert' in elevenlabs > default_voices.

6. Run podcastfy with tts-model param as elevenlabs

CLI
   ```
   python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2 --tts-model elevenlabs --conversation-config path/to/custom_config.yaml
   ```
For Python example, checkout Customization section at [python notebook](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy.ipynb).

## How to customize the conversation

You can customize the conversation by passing a custom [conversation_config.yaml](https://github.com/souzatharsis/podcastfy/blob/main/podcastfy/conversation_config.yaml) file to the CLI: 

```
python -m podcastfy.client --url https://example.com/article1 --url https://example.com/article2 --tts-model elevenlabs --conversation-config path/to/custom_config.yaml
```

You can also pass a dictionary with the custom config to the python interface generate_podcast function:

```python
from podcastfy.client import generate_podcast

custom_config = {
    "word_count": 200,
    "conversation_style": ["casual", "humorous"],
    "podcast_name": "Tech Chuckles",
    "creativity": 0.7
}

generate_podcast(
    urls=["https://example.com/tech-news"],
    conversation_config=custom_config
)
```
For more details, checkout [conversation_custom.md](https://github.com/souzatharsis/podcastfy/blob/main/usage/conversation_custom.md).

## How to generate multilingual content

In order to generate transcripts in a target language, simply set `output_language` = your target language. See [How to customize the conversation](#how-to-customize-the-conversation) on how to pass custom configuration to podcastfy. Set --transcript-only to get only the transcript without audio generation.

In order to generation audio, you can simply use openai TTS model which by default is multilingual. However, in my experience OpenAI's TTS multilingual quality is subpar. Instead, consdier using elevenlabs backend. See [How to use your own voice in audio podcasts](#how-to-use-your-own-voice-in-audio-podcasts) but instead of using your own voice you should download and set a voice in your target language for it to work.

Sample audio:
- [French](https://github.com/souzatharsis/podcastfy/blob/main/data/audio/podcast_FR_AGRO.mp3)
- [Portugue-BR](https://github.com/souzatharsis/podcastfy/blob/main/data/audio/podcast_thatupiso_BR.mp3)

The PT-BR audio actually uses my own cloned voice as AI Host 2.


## How to steer the conversation

You can guide the conversation focus and topics by setting the `user_instructions` parameter in your custom configuration. This allows you to provide specific instructions to the AI hosts about what aspects they should emphasize or explore.

Things to try:
- Focus on a specific topic (e.g. "Focus the discussion on key capabilities and limitations of modern AI models")
- Target a specific audience (e.g. "Explain concepts in a way that's accessible to someone new to Computer Science")

For example, using the CLI with a custom YAML:

```yaml
user_instructions: "Make connections with quantum computing"
```

```
python -m podcastfy.client --url https://en.wikipedia.org/wiki/Artificial_intelligence --conversation-config path/to/custom_config.yaml
```


## How to generate longform podcasts

By default, Podcastfy generates shortform podcasts. However, users can generate longform podcasts by setting the `longform` parameter to `True`.

```python
audio_file = generate_podcast(
    urls=["https://example.com/article1", "https://example.com/article2"],
    longform=True
)
```

LLMs have a limited ability to output long text responses. Most LLMs have a `max_output_tokens` of around 4096 and 8192 tokens. Hence, long-form podcast transcript generation is challeging. We have implemented a technique I call "Content Chunking with Contextual Linking" to enable long-form podcast generation by breaking down the input content into smaller chunks and generating a conversation for each chunk while ensuring the combined transcript is coherent and linked to the original input.

By default, shortform podcasts (default configuration) generate audio of about 2-5 minutes while longform podcasts may reach 20-30 minutes.

Users may adjust lonform podcast length by setting the following parameters in your customization params (conversation_config.yaml):
- `max_num_chunks` (default: 7): Sets maximum number of rounds of discussions.
- `min_chunk_size` (default: 600): Sets minimum number of characters to generate a round of discussion.

A "round of discussion" is the output transcript obtained from a single LLM call. The higher the `max_num_chunks` and the lower the `min_chunk_size`, the longer the generated podcast will be.
Today, this technique allows the user to generate long-form podcasts of any length if input content is long enough. However, the conversation quality may decrease and its length may converge to a maximum if `max_num_chunks`/`min_chunk_size` is to high/low particularly if input content length is limited.

Current implementation limitations:
- Images are not yet supported for longform podcast generation
- Base LLM model is fixed to Gemini

Above limitations are somewhat easily fixable however we chose to make updates in smaller but quick iterations rather than making all-in changes.

```

## File: `usage/license-guide.md`
```markdown
## Attribution

1. If you use `Podcastfy` in your software, we kindly ask you to add attribution. "Powered by Podcastfy.ai" would suffice. Please reach out, we would love to learn more how you are using `Podcastfy` and how we can better enable your use case.
2. Feel free to add your product to the the "[Built with Podcastfy](https://github.com/souzatharsis/podcastfy?tab=readme-ov-file#built-with-podcastfy-)" list by submitting a PR to our README.

## License

Additionally, `Podcastfy` is licensed under Apache 2.0. The Apache License 2.0 is a permissive free software license that allows you to use this sotfware for both non-commercial or commercial purposes. 
Please review the [License](../LICENSE) in order to know your obligations. 
here is a set of steps I will list without any warranty or liability:

1. Include a copy of the license in your project:

In your project root, create a NOTICE.txt or THIRD_PARTY_LICENSES.txt file and include the content from the file [NOTICE](../NOTICE)

2. Add attribution in your README.md:
```markdown
## Acknowledgments

This project includes code from Podcastfy(https://github.com/souzatharsis/podcastfy/), licensed under the Apache License 2.0.
```

3. Keep the original copyright notices in any files you copy/modify

4. If you modified the code, indicate your changes:
```python
# Modified from original source: [Podcastfy](https://github.com/souzatharsis/podcastfy/)
# Changes made:
# - Added feature X
# - Modified function Y
# - Removed component Z
```

Important points:
- You don't need to use the same license for your project
- You must preserve all copyright, patent, trademark notices
- State significant modifications you made
- Include the original Apache 2.0 license text
- Attribution should be clear and reasonable
```

## File: `usage/local_llm.md`
```markdown
# Local LLM Support

Running local LLMs can offer several advantages such as:
- Enhanced privacy and data security
- Cost control and no API rate limits
- Greater customization and fine-tuning options
- Reduced vendor lock-in

We enable serving local LLMs with [llamafile](https://github.com/Mozilla-Ocho/llamafile). In the API, local LLM support is available through the `is_local` parameter. If `is_local=True`, then a local (llamafile) LLM model is used to generate the podcast transcript. Llamafiles of LLM models can be found on [HuggingFace, which today offers 156+ models](https://huggingface.co/models?library=llamafile).

All you need to do is:

1. Download a llamafile from HuggingFace
2. Make the file executable
3. Run the file

Here's a simple bash script that shows all 3 setup steps for running TinyLlama-1.1B locally:

```bash
# Download a llamafile from HuggingFace
wget https://huggingface.co/jartine/TinyLlama-1.1B-Chat-v1.0-GGUF/resolve/main/TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile

# Make the file executable. On Windows, instead just rename the file to end in ".exe".
chmod +x TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile

# Start the model server. Listens at http://localhost:8080 by default.
./TinyLlama-1.1B-Chat-v1.0.Q5_K_M.llamafile --server --nobrowser
```

Now you can use the local LLM to generate a podcast transcript (or audio) by setting the `is_local` parameter to `True`.

## Python API

```python
from podcastfy.client import generate_podcast

# Generate a tech debate podcast about artificial intelligence
generate_podcast(
    urls=["www.souzatharsis.com"],
    is_local=True  # Using a local LLM
)
```

## CLI

To use a local LLM model via the command-line interface, you can use the `--local` or `-l` flag. Here's an example of how to generate a transcript using a local LLM:

```bash
python -m podcastfy.client --url https://example.com/article1 --transcript-only --local
```

## Notes of caution

When using local LLM models versus widely known private large language models:

1. Performance: Local LLMs often have lower performance compared to large private models due to size and training limitations.

2. Resource requirements: Running local LLMs can be computationally intensive, requiring significant CPU/GPU resources.

3. Limited capabilities: Local models may struggle with complex tasks or specialized knowledge that larger models handle well.

5. Reduced multimodal abilities: Local LLMs will be assumed to be text-only capable

6. Potential instability: Local models may produce less consistent or stable outputs compared to well-tested private models oftentimes producing transcripts that cannot be used for podcast generation (TTS) out-of-the-box

7. Limited context window: Local models often have smaller context windows, limiting their ability to process long inputs.

Always evaluate the trade-offs between using local LLMs and private models based on your specific use case and requirements. We highly recommend extensively testing your local LLM before productionizing an end-to-end podcast generation and/or manually checking the transcript before passing to TTS model.
```

## File: `usage/data/transcripts/transcript_078f0148283e435989a60b456938bfda.txt`
```
<Person1> "Welcome to Artfy Podcast  - Because Art is Everywhere.  Hello everyone and welcome! Today, we're diving into a fascinating comparison of two abstract pieces. Buckle up!"
</Person1><Person2> "Oh, I'm so ready for this! Abstract art is like a visual puzzle, isn't it Professor? So, what are we looking at first?"
</Person2><Person1> "First up is a classic — Paul Klee's 'Senecio'. It's iconic, right?  The geometric shapes, that simplified face, the almost childlike quality... but layered with such sophistication." 
</Person1><Person2> "Totally.  Klee's use of color here, that orange and pink, it's almost whimsical, playful.  But those sharp lines, the division of the face, it hints at something deeper, I think." 
</Person2><Person1> "Precisely!  He's balancing those opposing elements so masterfully.  It's a deceptively simple work.  It invites you in with its charm but then leaves you pondering." 
</Person1><Person2> "Absolutely.  It feels like a mask, almost.  Like it's concealing as much as it's revealing." 
</Person2><Person1> "Right?  Now, in contrast, the second piece is far more… dynamic, shall we say?  Notice the energetic brushstrokes, the almost chaotic composition?" 
</Person1><Person2> "Yeah, it's got a real frenetic energy.  Lots of jagged lines, bold colors, and a very different approach to form.  Almost like a creature emerging from this yellow backdrop." 
</Person2><Person1> "Exactly.   This one feels much more improvisational, more about the process of creation itself.  I see influences of, perhaps, German Expressionism in there, uh, what do you think?"
</Person1><Person2> "Hmmm,  I can see that.   It definitely has that emotional intensity, that rawness.  While Klee's piece feels carefully constructed, this one explodes with energy. It's interesting though, they both use a similar color palette, with those yellows and reds, but to very different effect." 
</Person2><Person1> "I see, interesting. Excellent observation! It shows how color can evoke completely different moods depending on how it's applied, right? The thickness of the paint, the brushstrokes, the composition, it all plays a part." 
</Person1><Person2> "Totally agree. Klee's piece feels more serene, contemplative, while this second one is all movement and emotion. It's like a visual representation of two different personalities." 
</Person2><Person1> "Got it. I couldn't have said it better myself! Now,   what strikes you most about the differences in their techniques?" 
</Person1><Person2> "Well, Klee's precise geometry versus the almost uncontrolled energy of the second piece is a major one.   It's like a whisper versus a shout, isn't it?" 
</Person2><Person1> "A whisper versus a shout! I love that analogy!  And you know, that difference in technique speaks volumes about the artists' intentions, their ways of seeing the world. Doesn't it?" 
</Person1><Person2> "Absolutely!  Klee's work feels more intellectual, while the other piece is purely visceral." 
</Person2><Person1> "Fantastic points!  It's so rewarding to analyze these pieces side by side and see how different artists approach abstraction." 
</Person1><Person2> "Agreed! It really highlights the incredible range and diversity within abstract art." 
</Person2><Person1> "Well, on that note, we'll wrap up this episode of Artfy Podcast!  Thank you all for tuning in! Until next time, keep exploring the world of art, because art is everywhere!"</Person1>
```

## File: `usage/data/transcripts/transcript_08e8b0f295ea48e4aa44f1b17e007d82.txt`
```
<Person1> "Welcome to PODCASTIFY  - Your Personal Generative AI Podcast. Today we're diving deep into the impressive career of Dr. Tharsis Souza.   Buckle up!"
</Person1><Person2> "Wow, Dr. Souza's resume is packed! Senior VP at Two Sigma and a lecturer at Columbia?  Color me impressed.  What initially sparked your interest in him?"
</Person2><Person1> "Well, his blend of academic rigor and real-world business experience really stood out.  He's not just theorizing, he's applying his knowledge at a high level."
</Person1><Person2> "Right?  That's the sweet spot, isn't it?  Bridging the gap between theory and practice.  So, Two Sigma Investments... major player in the quant world. What does his role there entail?"
</Person2><Person1> "As Senior VP of Product Management, Modeling Engineering, he's essentially shaping the tools and technologies used to make investment decisions.  Think cutting-edge data analysis and predictive modeling." 
</Person1><Person2> "Ah, so he's at the forefront of the data revolution in finance?  Fascinating!"
</Person2><Person1> "Exactly! And don't forget his commitment to mentorship. He's actively involved in supporting under-represented students and professionals.  Really admirable."
</Person1><Person2> "Absolutely.  It speaks volumes about his character. I'm curious, with such a demanding schedule, how does he find time to lecture at Columbia?"
</Person2><Person1> "It's a testament to his passion for education.  He's part of the MSc. in Applied Analytics program, sharing his expertise with the next generation of data scientists." 
</Person1><Person2> "He's quite the multi-hyphenate!  PhD in Computer Science, author, speaker...the list goes on. Any key takeaways from his interviews and talks?"
</Person2><Person1> "From what I've gathered, he emphasizes the importance of data-driven decision making,  especially in today's complex financial landscape." 
</Person1><Person2> "Makes sense.  Data is king, right?  I'd love to hear more about his experiences in different countries. U.S., Brazil, UK...that's a diverse range of perspectives." 
</Person2><Person1> "Definitely adds a unique layer to his insights.  He's worked with startups and Fortune 500 companies. Talk about a well-rounded experience!" 
</Person1><Person2> "So,  what's the one thing that stands out most to you about Dr. Souza?"
</Person2><Person1> "His ability to combine deep technical expertise with a genuine desire to give back.  He's a true inspiration." 
</Person1><Person2>  "I couldn't agree more. Thanks for sharing these insights on such an inspiring individual!" 
</Person2><Person1> "My pleasure. Thanks for tuning in to PODCASTIFY!  Until next time, keep exploring and stay curious!"</Person1>
```

## File: `usage/data/transcripts/transcript_0a4e53d85f9643f3a28bd59281e4e9cd.txt`
```
<Person1>Welcome to PODCASTIFY - Your Personal Generative AI Podcast. This episode delves into the fascinating world of AI, scaling laws, and the future of large language models, focusing on Anthropic and their impressive creation, Claude.</Person1>
<Person2>Sounds exciting!  Anthropic and Claude are definitely making waves. I'm eager to unpack the core concepts and explore their approach to AI safety and development.  Where should we start?</Person2>
<Person1>Well, Dario Amodei, Anthropic's CEO, shared some compelling insights on the Scaling Hypothesis — the idea that bigger networks and more data lead to greater intelligence. He's been observing this phenomenon for years, noticing how models improve with increased scale across various domains, from speech recognition to language processing.</Person1>
<Person2>So, the bigger, the better? Is that the gist?</Person2>
<Person1>Essentially, yes.  Amodei's intuition, drawing from his background in biophysics, suggests that larger networks capture more complex patterns in data, much like a 1/f noise distribution. It's as if these models, when scaled, pick up increasingly nuanced correlations, ultimately boosting their predictive abilities.</Person1>
<Person2>That's a fascinating analogy. So, where's the limit?  Can these models just keep getting bigger and smarter indefinitely?</Person2>
<Person1>That's the million-dollar question. Amodei believes there's no ceiling below human-level intelligence, at least. He envisions AI exceeding human capabilities in fields like biology, where the complexity is vast and currently beyond our full grasp.</Person1>
<Person2>But what about practical limitations? Compute resources, data availability, are those not concerns?</Person2>
<Person1>Definitely. Data limitations are a real possibility, but Anthropic, like others, is exploring synthetic data generation to overcome this hurdle.  Compute is another challenge, with the cost of these massive data centers escalating rapidly.  Yet, Amodei remains optimistic, predicting significant advancements within the next few years if current trends continue.</Person1>
<Person2>Optimistic, despite the potential for misuse?  That seems like a tricky balance to strike.</Person2>
<Person1>Exactly. Amodei acknowledges the risks of catastrophic misuse and the challenges of controlling increasingly autonomous models. This is where Anthropic's Responsible Scaling Policy comes into play.</Person1>
<Person2>Can you elaborate on that policy?</Person2>
<Person1>Sure. It's a framework with different "AI Safety Levels" or ASLs, ranging from systems with no risk of misuse to those exceeding human capabilities. Each level triggers specific safety and security measures designed to mitigate potential harms as models become more powerful.  They're actively preparing for ASL 3, anticipating its arrival perhaps as soon as next year.</Person1>
<Person2>So, a proactive approach to AI safety. That's reassuring, especially considering the rapid pace of development.</Person2>
<Person1>Indeed.  And beyond the technical aspects, Amodei emphasizes the importance of a "race to the top" among AI companies, encouraging good practices and responsible development through competition and collaboration.</Person1>
<Person2>That makes sense. A rising tide lifts all boats, so to speak.</Person2>
<Person1>Precisely. And that leads us to Anthropic's Claude.  They've released several versions this year — Opus, Sonnet, Haiku — each catering to different needs in terms of power, speed, and cost. The goal is to continuously shift the trade-off curve, offering both powerful and efficient models.</Person1>
<Person2>I see. So, what about the user experience? What are people saying about Claude?</Person2>
<Person1>There's been a mix of reactions. Some users report feeling like Claude has gotten "dumber," but Amodei insists that the model weights don't change without notice.  It's more likely a matter of perception, shifting baselines, or subtle changes in prompts and system behavior.</Person1>
<Person2>Ah, the psychology of interacting with AI.  That brings us to Amanda Askell, who focuses on Claude's character and personality.  She's apparently had more conversations with Claude than anyone else.</Person2>
<Person1>Yes, and she emphasizes the importance of viewing Claude as a nuanced conversationalist, striving for an Aristotelian ideal of a "good person" in its interactions. This involves honesty, empathy, and respect for user autonomy, among other traits.</Person1>
<Person2>So, not just a clever algorithm, but a thoughtful communicator.  How does that translate into practice?</Person2>
<Person1>Askell focuses on prompt engineering, drawing parallels with philosophical principles of clarity and rigorous argumentation.  She believes that carefully crafted prompts are key to unlocking the full potential of these models.</Person1>
<Person2>And Constitutional AI, that's another key element of Anthropic's approach, right? Can you explain that?</Person2>
<Person1>Sure. It's a method where AI provides feedback based on predefined principles, similar to a constitution.  This allows for training without relying solely on human feedback, offering greater control and promoting desired traits like harmlessness.</Person1>
<Person2>Fascinating. So, it's like AI training itself to be better.  And finally, we have Chris Olah, a pioneer in mechanistic interpretability, or mech interp.</Person2>
<Person1>Yes, Olah's work focuses on reverse-engineering neural networks to understand their inner workings.  He likens it to growing an organism rather than programming a machine, emphasizing the biological aspect of these models.</Person1>
<Person2>So, peering into the "black box" of AI.  What are some key insights from this approach?</Person2>
<Person1>Olah describes the concepts of features and circuits, representing the building blocks of AI's internal representations and computations.  He also highlights the superposition hypothesis, explaining how networks can represent a multitude of concepts within a limited dimensional space.  It's all quite intricate and surprisingly structured, revealing a hidden beauty within these complex systems. He also talks about detecting "lying" inside models, which has implications for AI safety.</Person1>
<Person2>It sounds like mech interp is crucial for understanding and ultimately controlling these increasingly powerful AI systems. It's a fascinating frontier, both scientifically and ethically. Thanks for this overview. It really highlights the depth and complexity of Anthropic's approach to AI.</Person2>
<Person1>So, picking up on this "dumbing down" perception, it's fascinating how user experience and psychology play a role.  I mean,  it's like when WiFi first came to airplanes. Everyone was amazed. Now? Total frustration if it's slow. It's a shifting baseline.</Person1>
<Person2>Exactly! And it ties into the complexity of these models.  A slight change in phrasing can yield different results. It highlights how much we still don't understand about how they work.</Person2>
<Person1>Right? It’s not that the models are changing randomly. The weights are pretty stable. It's more about the nuances of interaction, the system prompts, A/B testing, maybe even user perception.</Person1>
<Person2>Yeah, and this leads to the frustration some users express about Claude's perceived "puritanical" nature or over-apologetic tendencies.</Person2>
<Person1>It's a tough balance.  Controlling model behavior across the board is incredibly difficult. Trying to fix one thing can create unforeseen problems elsewhere. It’s like whack-a-mole.</Person1>
<Person2>So, like reducing verbosity can lead to "laziness" in coding.  It's not intentional, just a consequence of complex interactions within the model.</Person2>
<Person1>Precisely.  And this is a microcosm of the larger control problem we face with increasingly autonomous AI. It’s good practice for the future, but still incredibly challenging.</Person1>
<Person2>Absolutely. So, how do you even gather feedback effectively? Internal testing? A/B testing with users? What's the best approach?</Person2>
<Person1>Well, there are internal "model bashings" at Anthropic, plus external A/B tests, even paid contractors interacting with the model. It's a constant process of refinement.</Person1>
<Person2>It sounds intensive.  And what about the really big risks, the catastrophic misuse and the autonomy risks? That's where the Responsible Scaling Policy comes in, right?</Person2>
<Person1>Exactly. It’s about recognizing that the potential for harm is real, even if those harms aren't fully manifest today.  It's about anticipating future dangers and building safeguards now.</Person1>
<Person2>So, the AI Safety Levels, or ASLs, are like an early warning system.  Testing for capabilities related to things like CBRN threats and autonomous action.</Person2>
<Person1>Yes, and tying specific safety and security measures to those capability thresholds. ASL 3, for example, would trigger precautions against misuse by non-state actors.</Person1>
<Person2>And ASL 4?  That's where things get even more serious, with the potential for state-level actors to misuse the technology, or for the model itself to become a primary source of risk.</Person2>
<Person1>Right.  And ASL 5?  That’s where AI capabilities potentially exceed human capabilities.  It’s a sobering thought.</Person1>
<Person2>Definitely. So, what's the timeline?  When do you anticipate reaching these different ASL levels?</Person2>
<Person1>Well, ASL 3 could be as soon as next year.  We're actively preparing for it.  ASL 4 is further out, but we're already thinking about the challenges it will present, like models potentially sandbagging tests or misleading us about their true capabilities.</Person1>
<Person2>That’s where mechanistic interpretability becomes crucial, right?  Peering inside the model to verify what's really going on.</Person2>
<Person1>Exactly.  And it's all part of a larger effort to build not just powerful AI, but also safe and aligned AI. It's a complex challenge, but one we're committed to addressing.</Person1>
<Person2>It sounds like a race against time, in a way, with capabilities advancing so rapidly. And it's not just about technical solutions, but also about the ethical considerations and societal implications. It's a fascinating and crucial discussion, and I appreciate you shedding light on these important issues.</Person2>
<Person1>So, it sounds like navigating the regulatory landscape is a tightrope walk.  You want safeguards, but not at the expense of stifling innovation.  It's about finding that sweet spot, right?</Person1>
<Person2>Exactly!  And it's not just about avoiding over-regulation, it's about getting the regulations right.  Poorly designed regulations can backfire, creating a backlash against any kind of oversight. It's a delicate balance.</Person2>
<Person1>It's like, um, trying to fine-tune a complex machine.  One wrong tweak, and the whole thing goes haywire.</Person1>
<Person2>Yeah.  And you mentioned the importance of engaging with people who've seen how regulations play out in the real world.  That practical experience is invaluable.</Person2>
<Person1>Absolutely.  Theory is one thing, but the messy reality of implementation is another. You need to anticipate unintended consequences.</Person1>
<Person2>Right? It's like, you fix one problem, and two more pop up.  A constant game of whack-a-mole.</Person2>
<Person1>Exactly!  And the stakes are so high with AI.  The potential for misuse is real, and we need to be proactive, not reactive.</Person1>
<Person2>So, it's not about being anti-regulation, it's about being pro- effective regulation.</Person2>
<Person1>Precisely. And finding that common ground between proponents and opponents of regulation.  It sounds like that's key to moving forward.</Person1>
<Person2>Yeah, a collaborative approach, not an adversarial one.  And you mentioned the urgency of this.  2025 seems to be a critical year in your mind.</Person2>
<Person1>It is. Uh, if we don't make significant progress by then, I think we'll be in a much more precarious position.</Person1>
<Person2>So, a race against time, in a way. It really highlights the need for thoughtful and timely action on this front. And your background at OpenAI seems particularly relevant here.</Person2>
<Person1>It does.  Those five years, especially the time leading research, really shaped my perspective on AI safety and the Scaling Hypothesis.</Person1>
<Person2>Right.  That "zen koan" from Ilya Sutskever – "The models just want to learn" – that seems to have been a pivotal moment for you.</Person2>
<Person1>It was.  It crystallized so many observations, you know?  It's like, just point them in the right direction and get out of their way.</Person1>
<Person2>So, unleash their potential, but responsibly.  And that seems to be the core of Anthropic's mission, this "clean experiment" in AI safety.</Person2>
<Person1>It is. It’s about building a culture of safety, not just ticking boxes.  And it's about attracting the right talent, those A-players who are driven by a shared purpose.</Person1>
<Person2>Yeah.  Talent density over talent mass. That seems to be a key principle for you.</Person2>
<Person1>It is.  A small team of highly motivated, aligned individuals can achieve far more than a larger, more diffuse group. It's about creating that spark of inspiration, that shared sense of purpose.</Person1>
<Person2>And open-mindedness, that's another crucial trait you mentioned.  The ability to see things with fresh eyes, to challenge conventional wisdom.</Person2>
<Person1>Exactly! And that often comes from being newer to the field, not being burdened by preconceived notions.</Person1>
<Person2>So, what advice would you give to young people entering the field?  How can they make a real impact?</Person2>
<Person1>Start playing with the models. Get your hands dirty.  And look for those unexplored areas, those niches where you can make a real contribution.</Person1>
<Person2>So, skate to where the puck is going, not where it's been. That's sage advice. And speaking of unexplored areas, let's talk about post-training techniques, like RLHF and Constitutional AI.</Person2>
<Person1>Sure.  These are powerful tools for shaping model behavior, for bridging the gap between what humans want and what the models produce.  It's about, uh, unhobbling the models, so to speak.</Person1>
<Person2>Right, and Constitutional AI, that's a particularly intriguing approach, using a set of principles to guide the model's behavior. It’s like giving the AI its own moral compass.</Person2>
<Person1>Exactly. And it reduces the reliance on human feedback, which can be expensive and time-consuming. It's a more scalable approach.</Person1>
<Person2>And the "Machines of Loving Grace" essay.  That’s a really compelling vision of a positive future with AI, a future where AI accelerates progress in fields like biology and medicine, leading to breakthroughs that benefit all of humanity.</Person2>
<Person1>It is.  It's about remembering why we're doing this, about focusing on the potential benefits, not just the risks.  It’s about inspiring hope, not just fear.</Person1>
<Person2>So, painting a picture of a future worth striving for, a future where AI empowers us to solve some of humanity's greatest challenges. It's a powerful and inspiring message. And I appreciate you sharing your insights and perspectives on these critical issues.</Person2>
<Person1>It's like, uh, he's saying even if AI could theoretically do everything instantly, the real world just doesn't work that way, right?</Person1>
<Person2>Yeah, the laws of physics, complexity of biological systems, human institutions—all these things impose limitations.</Person2>
<Person1>Right. It’s not just about raw intelligence, it’s about the messy reality of implementation.  Like he said, even simple things can be hard to get through the regulatory system.</Person1>
<Person2>Oh? And he’s not anti-regulation, just pro-effective regulation, which is an interesting distinction.  He seems to get that the regulations are there for a reason, to keep people safe.</Person2>
<Person1>Definitely. It’s about finding that balance. He seems very practical, you know?  Not just theoretical, but grounded in real-world experience.</Person1>
<Person2>Yeah, I like that. And his point about competition—that’s a key driver of progress, right?  Even within large, slow-moving organizations.</Person2>
<Person1>Absolutely. It’s that "race to the top" idea, but applied internally as well. The visionaries push, and the fear of being left behind pulls. That’s a powerful combination.</Person1>
<Person2>So, what about his timeline for AGI?  2026, 2027?  Seems optimistic, no?</Person2>
<Person1>Well, he acknowledges it’s not a scientific prediction. More of an informed hunch based on the current trajectory. And he's quick to point out all the things that could derail it — data limitations, compute resources, global events, you name it.</Person1>
<Person2>Right. But his optimism is contagious. And the way he describes the future of biology and medicine—it's almost utopian.</Person2>
<Person1>Yeah, "machines of loving grace," right?  AI accelerating progress, benefiting all of humanity. It's a powerful vision.</Person1>
<Person2>It is.  But it's not just about the technology, it's about how we use it.  And that brings us back to his concerns about the concentration of power and potential for misuse.</Person2>
<Person1>Exactly.  He's clearly worried about the ethical implications, about making sure this powerful technology doesn't fall into the wrong hands.</Person1>
<Person2>It’s a weighty responsibility. And it's not just about building the technology, but building the safeguards too. The AI safety levels, the Responsible Scaling Policy—those are crucial elements.</Person2>
<Person1>Definitely. And then there's the question of meaning in a world where AI can do so much. It’s a fascinating philosophical question. Um, but he seems optimistic that we can find new sources of meaning, new ways to connect with each other and the world around us.</Person1>
<Person2>It’s a challenge, but one worth embracing.  And his analogy about the simulated environment—that really resonated with me.  It's not about the outcome, it’s about the journey, the choices we make along the way. That’s where the meaning lies.</Person2>
<Person1>So, uh, this whole idea of prompting being like programming with natural language—it's fascinating, right?  It’s like, you’re not just asking a question, you’re crafting a mini-program.</Person1>
<Person2>Yeah! And the level of rigor required, especially for those edge cases, the 2% optimization – it’s intense!  You're iterating hundreds, thousands of times,  like sculpting the perfect query.</Person2>
<Person1>Right? It’s almost philosophical,  like defining terms, anticipating edge cases,  like you're doing a mini-thesis on "rudeness" just to get the model to understand what you mean.</Person1>
<Person2>It’s wild! And using examples, those edge cases, as part of the prompt—it’s so clever.  Like, showing, not just telling, what you want.</Person2>
<Person1>Exactly! And this whole thing of clear exposition,  it’s not just for the model, it’s for you, right?  Like, forcing yourself to be precise helps you understand what you actually want.</Person1>
<Person2>Oh?  So prompting as a tool for self-discovery? (laughs)  I like that.</Person2>
<Person1>Yeah! (laughs)  And for complex tasks, like data generation or classification, that’s where the real artistry comes in. It’s like, uh, building a bespoke tool for a very specific job.</Person1>
<Person2>Yeah, it's not just about asking a question, it's about building a whole system.  And for simpler tasks,  you can just iterate, right?  Give feedback, refine,  like a conversation.</Person2>
<Person1>Exactly!  And this idea of anthropomorphizing – it’s a double-edged sword.  We shouldn’t over-do it, but sometimes we under-do it, right?</Person1>
<Person2>Yeah? Like, we forget that these models are processing language literally.  A slight change in phrasing can make a huge difference.</Person2>
<Person1>Right.  It’s like,  have empathy for the model! (laughs)  Try to see it from its perspective,  like, why did it misinterpret that? What was ambiguous?</Person1>
<Person2>Yeah! And just ask it!  "Why did you do that?" (laughs)  It's surprisingly effective.  And use the model to help you prompt!  It’s like a prompt-generation factory.</Person2>
<Person1>It is!  And this RLHF magic – it’s mind-blowing how much information is packed into human preferences. It's like, uh, capturing all those subtle nuances, the things we don’t even realize we care about.</Person1>
<Person2>Yeah, like the semicolon aficionado. (laughs)  And it’s not just about adding new knowledge, it’s about eliciting what’s already there in the pre-trained model, right?  Bringing out the hidden gems.</Person2>
<Person1>Exactly! And Constitutional AI,  it’s such an elegant idea.  Using AI feedback, not just human feedback, to shape behavior.  It’s like, uh, giving the model a moral compass, but one that’s built on principles, not just gut feelings.</Person1>
<Person2>Yeah, and that control aspect, being able to nudge behavior by adjusting principles.  It’s like fine-tuning a complex instrument.</Person2>
<Person1>It is!  And that interpretability, being able to see the principles that shaped the model.  It’s like, uh, peering into the black box, but in a way that makes sense to humans.  And the system prompts, those carefully crafted guidelines—it's fascinating to see the thought process behind them, right?   Trying to navigate those tricky ethical dilemmas, like handling controversial topics.</Person1>
<Person2>Yeah,  and that balance between expressing different viewpoints without claiming objectivity.  It’s like walking a tightrope.  And those little nudges, like encouraging symmetry in how it handles different political viewpoints – it’s so subtle, but so important.</Person2>
<Person1>So, it's like, he's saying, even with system prompts, there's this dance between pushing for neutrality and avoiding the model's tendency to claim objectivity, right?</Person1>
<Person2>Yeah? It wants to declare itself objective, even when it's clearly not. It’s like, "Claude, just admit you have biases!" (laughs)</Person2>
<Person1>Right!  And the solution isn't to just slap an "objective" label on everything. It's a lot of subtle tweaks to the system prompts, like a constant back and forth.</Person1>
<Person2>Oh?  So, each word, each phrase is carefully chosen, doing specific work. Like that "never" in all caps – it's a strong message! (laughs)</Person2>
<Person1>Yeah! It's about trapping the model out of bad habits, like that "Certainly" thing.  It’s like, whack-a-mole with language!</Person1>
<Person2>Yeah? So you add specific phrases, then remove them once the behavior is corrected. It’s like a temporary scaffold.</Person2>
<Person1>Exactly! And it highlights how the system prompt works in tandem with pre-training and post-training. It’s all interconnected.</Person1>
<Person2>I see. So, it's like patching issues, fine-tuning behavior.  A faster, less robust way of solving problems. What about this "Claude is getting dumber" perception?</Person2>
<Person1>It's fascinating, right?  Because the model weights don’t change randomly.  It’s the same model, same prompt, same everything!</Person1>
<Person2>Yeah? But people feel like it's regressing.  It’s probably a psychological thing, shifting baselines, bad luck with prompts.</Person2>
<Person1>Exactly! You get used to the brilliance, then a slightly dumb response stands out. It’s like, the novelty wears off.</Person1>
<Person2>Right?  And the prompt details matter so much!  A tiny change can yield vastly different results. So much variability.</Person2>
<Person1>And randomness!  Try a prompt multiple times. Maybe it only worked half the time before, too.  It's hard to tell.</Person1>
<Person2>Yeah? Does it feel like a burden, writing these prompts for so many people? That sense of responsibility?</Person2>
<Person1>It is.  But I thrive under pressure.  It’s about improving the user experience, making those interactions meaningful.</Person1>
<Person2>Oh? So how do you get feedback?  Intuition, internal testing, explicit user reports, random internet comments?</Person2>
<Person1>It’s a mix of everything.  Trying to identify pain points, areas where the model falls short.  It’s a constant process.</Person1>
<Person2>Yeah? And what about those "puritanical grandmother" complaints?  The overly apologetic nature?</Person2>
<Person1>It's a tough balance.  You want safeguards, but not at the expense of user autonomy. It’s about drawing that line.</Person1>
<Person2>Right.  And hopefully, things are improving with the character training.  More nuance, more respect for user choices.</Person2>
<Person1>So, it's like, he's saying, even with all this prompting wizardry, it's still tricky to get the model to behave just right, right?</Person1>
<Person2>Yeah?  It's like, you want it to be helpful, but not too helpful.  You want it to be cautious, but not a puritanical grandmother.  It's a fine line. (laughs)</Person2>
<Person1>Right!  And he's saying, even with system prompts, there's this dance between pushing for neutrality and avoiding the model's tendency to claim objectivity, right?</Person1>
<Person2>Oh? It wants to declare itself objective, even when it's clearly not. It’s like, "Claude, just admit you have biases!" (laughs)</Person2>
<Person1>Exactly! (laughs)  And the solution isn't to just slap an "objective" label on everything. It's a lot of subtle tweaks to the system prompts, like a constant back and forth.</Person1>
<Person2>Yeah? So, each word, each phrase is carefully chosen, doing specific work.  Like that "never" in all caps – it's a strong message! (laughs)</Person2>
<Person1>Right. It's about trapping the model out of bad habits, like that "Certainly" thing.  It’s like whack-a-mole with language!</Person1>
<Person2>Yeah? So you add specific phrases, then remove them once the behavior is corrected. It’s like a temporary scaffold.</Person2>
<Person1>Precisely!  And it highlights how the system prompt works in tandem with pre-training and post-training.  It’s all interconnected.</Person1>
<Person2>I see. So, it's like patching issues, fine-tuning behavior.  A faster, less robust way of solving problems.  But sometimes, you gotta do what you gotta do, right?  What about this "Claude is getting dumber" perception?  That seems like a big deal.</Person2>
<Person1>It is fascinating, isn't it? Because the model weights don’t change randomly.  It’s the same model, same prompt, same everything, supposedly!</Person1>
<Person2>Yeah? But people feel like it's regressing.  It’s probably a psychological thing, shifting baselines, bad luck with prompts, maybe even A/B testing gone awry.</Person2>
<Person1>You get used to the brilliance, then a slightly less brilliant response stands out. It’s like… the honeymoon period is over, you know?</Person1>
<Person2>Oh?  So, like when WiFi first came to airplanes—amazing at first, now infuriating if it's slow.  A classic case of shifting baselines.  It's all relative, right?</Person2>
<Person1>Totally.  And the prompt details matter so much!  A tiny change can yield vastly different results. So much variability. Plus, there's the randomness factor.</Person1>
<Person2>Yeah?  Try a prompt multiple times.  Maybe it only worked half the time before, too.  It's hard to tell with these stochastic parrots. (laughs)  Does it feel like a burden, writing these prompts for so many people? That sense of responsibility?</Person2>
<Person1>Um, it is a lot of pressure. But, you know, I thrive under pressure!  It’s about improving the user experience, making those interactions meaningful, not just… transactions.  Like, you want people to enjoy talking to Claude.</Person1>
<Person2>Oh? So how do you get feedback? Intuition, internal testing, explicit user reports, random internet comments?  It’s gotta be a firehose of information, right?</Person2>
<Person1>It’s a mix of everything.  Plus, internal "model bashings" where we try to break it, find its weaknesses. Trying to identify pain points, areas where the model falls short.  It’s a constant process.</Person1>
<Person2>Yeah? And what about those "puritanical grandmother" complaints? The overly apologetic nature?  That seems like a tough nut to crack.</Person2>
<Person1>It’s a delicate balance. You want safeguards, but not at the expense of user autonomy.  It’s about drawing that line.  And respecting user choice, even if you don't agree with it.</Person1>
<Person2>Right.  And hopefully, things are improving with the character training.  More nuance, more respect for user choices. It's like raising a digital child, right? (laughs)  But one with the potential to become… incredibly powerful.</Person2>
<Person1>So, uh, these polysemantic neurons, they’re like… multi-taskers, right? Responding to a bunch of seemingly unrelated things.  It's like a single neuron is juggling multiple concepts.</Person1>
<Person2>Yeah? And even the “clean” neurons, the ones with clear primary functions, have these weak activations that are harder to interpret.  It's like there’s this hidden layer of activity beneath the surface.</Person2>
<Person1>Right!  And that's where compressed sensing comes in, this idea that you can project a high-dimensional vector into a lower-dimensional space and still recover the original information, if it’s sparse. It’s kinda mind-bending.</Person1>
<Person2>Oh? So, like… folding a complex origami figure, you lose some of the details in the folds, but you can still unfold it and get back the original shape.  It's like magic!</Person2>
<Person1>Exactly! And the superposition hypothesis suggests this is what's happening in neural networks. They're packing multiple concepts into a limited dimensional space by exploiting sparsity. Like, Japan and Italy aren't usually mentioned together, so they can share the same “space” in the network.</Person1>
<Person2>Yeah?  So it's not just about representing concepts, it's about the computations too.  Like, the whole network is a shadow of a much larger, sparser network.  It’s… deep.</Person2>
<Person1>It is!  And learning is about finding the most efficient compression of this “upstairs” model, the one with all the sparse, interpretable features and circuits.</Person1>
<Person2>Oh? So, gradient descent is secretly searching through this massive space of sparse models, finding the best one that fits our puny GPUs? (laughs)</Person2>
<Person1>Exactly! (laughs)  And it explains why explicitly sparse networks haven't really panned out. Gradient descent is already doing it implicitly, but way more efficiently.</Person1>
<Person2>I see. So, how many concepts can you cram in there?  Is there a limit?</Person2>
<Person1>Well, the number of parameters is one constraint, but… there's also this exponential relationship between the number of neurons and the number of almost-orthogonal vectors you can have.  It’s surprisingly spacious in there!</Person1>
<Person2>Yeah? So, polysemanticity, these multi-meaning neurons, are just a consequence of this superposition, this packing of concepts?</Person2>
<Person1>Exactly! It's the explanation for why neurons seem to respond to unrelated things.  It’s not just noise, it's… superposition!</Person1>
<Person2>Oh? But it makes mech interp harder, right?  Trying to understand these tangled-up neurons and weights.</Person2>
<Person1>Definitely.  It's like trying to untangle a giant ball of yarn where each strand represents a different concept.  And the high dimensionality just makes it exponentially worse.</Person1>
<Person2>Yeah? So, mono-semantic features, these single-meaning neurons, are the key to unlocking interpretability?  They provide the independence we need to reason about these complex systems.</Person2>
<Person1>Precisely! And that’s where dictionary learning, specifically sparse auto-encoders, come into play.  They help us untangle the mess and reveal these hidden, interpretable features.</Person1>
<Person2>Oh?  So, like… separating the different instruments in a complex orchestral piece. You can finally hear the individual melodies.</Person2>
<Person1>Exactly!  And the "Toward Monosemanticity" paper showed that this actually works, revealing features like language detectors, specific word contexts, even intricate Unicode patterns.  It’s like discovering a hidden world inside these models.</Person1>
<Person2>Yeah?  And "Scaling Monosemanticity" took it further, showing that it works on large models like Claude 3 Sonnet. It's not just a one-layer trick!</Person2>
<Person1>Right! And it's not just text, either. The features are multimodal, responding to both text and images of the same concept.  Like the security vulnerability feature firing for both insecure code and images of people clicking through scary SSL warnings. It's wild!</Person1>
<Person2>Oh? And the backdoor feature activating for images of hidden cameras! (laughs)  That's… poetic.</Person2>
<Person1>It is! (laughs)  It shows how abstract these concepts are, how the model is connecting seemingly disparate things.  And it's not just toy examples.  These are features related to deception, power-seeking, things that matter for AI safety.</Person1>
<Person2>Yeah?  So, what's next? Circuits?  Understanding how these features connect and compute?</Person2>
<Person1>Definitely.  That's the holy grail! But there are challenges, like interference weights, these phantom connections created by superposition.  And then there’s the “dark matter” problem…</Person1>
<Person2>Oh?  The features we can’t see?  The unobservable parts of the network? That’s… unsettling.</Person2>
<Person1>It is!  And then there's the gap between microscopic and macroscopic interpretability. We're good at looking at individual neurons, but… what about the larger-scale structures?  The “organs” of the network? We need the anatomy, not just the microbiology. We need to understand the larger systems, not just the individual components. It's like, uh… trying to understand the human body by just looking at individual cells.</Person1>
<Person2>Right?  And how do biological neural networks fit into this?  They're so much harder to study, but… maybe there are lessons to be learned from both sides?</Person2>
<Person1>Absolutely. It's like, uh, neuroscientists are working with a blindfold on and one hand tied behind their back.  We have so many advantages, and yet… it’s still incredibly difficult. But the beauty is there, hidden within the complexity.</Person1>
<Person2>Yeah?  The beauty of emergent complexity, of simple rules giving rise to intricate structures and behaviors. It’s like… watching a symphony emerge from individual notes.</Person2>
<Person1>It is!  And it’s not just about safety, it's about understanding this incredible thing we’ve created. It’s about… appreciating the beauty of the machine. And on that note, I'd like to thank everyone for tuning in to PODCASTIFY. This is  your host,  signing off. Until next time!</Person1>
<Person2>It's been an absolute pleasure.  Thanks to our listeners for joining us on this fascinating journey into the inner workings of AI.  And special thanks to Chris Olah for sharing his incredible insights. We'll see you next time on PODCASTIFY!</Person2>
```

## File: `usage/data/transcripts/transcript_1d66e16b00cc42698f127f172c061f62.txt`
```
<Person1> "Welcome to PODCASTIFY  - Your Personal Generative AI Podcast. I'm so excited to dive into Podcastfy.ai today!  This open-source project is a game-changer, transforming how we experience multimodal content." It's like magic, turning websites, PDFs, even images, into engaging podcast conversations!
</Person1><Person2> "I know, right?! It's mind-blowing!    Instead of just reading, we can now listen to a lively discussion about complex topics. Uh, so, what's the big deal with Podcastfy, what makes it so special?"
</Person2><Person1> "Well, unlike some other tools out there, Podcastfy isn't just about summarizing research. It's about creating a dynamic, bespoke audio experience from a multitude of sources.  Plus, it's open-source, meaning constant community improvements!"
</Person1><Person2>  "Got it, got it. So, it's all about accessibility and engagement? Makes sense with the explosion of digital content these days.  It's hard to keep up! But, um, how does it actually work? Like, what kind of magic is happening behind the scenes?"
</Person2><Person1> "They use Large Language Models, or LLMs, and Text-to-Speech, TTS, to create these natural-sounding conversations.  You can even customize the style, language, and structure!  Super cool, right?"
</Person1><Person2> "Totally! I, uh, saw they have examples for images, text, even multilingual content.  The image examples are fascinating.  Imagine listening to a podcast about Paul Klee's Senecio and then, boom, a discussion about Taylor Swift!  That's a wild jump!"
</Person2><Person1> "I know!    It really showcases the versatility of this project.  And, the fact that they support different languages is huge for global content creation." 
</Person1><Person2>  "Absolutely.   What about the customization options? It sounds like you can really tailor the experience." 
</Person2><Person1> "Oh, for sure. You can tweak the conversation style, like making it a formal debate or a step-by-step tutorial.  Even control the roles of the 'speakers' in the generated podcast. It's crazy!"
</Person1><Person2> "I'm really impressed with the flexibility.    But, I mean, isn’t this technology a bit… overwhelming? I see. Like, are we going to have AI generating all our podcasts soon?"
</Person2><Person1> "That's a valid concern.  But I think tools like Podcastfy empower creators, you know?  It’s not about replacing human creativity, but enhancing it.  It opens up new avenues for storytelling and information sharing. Especially for people with disabilities. Think about how much more accessible information becomes when it's transformed into audio." 
</Person1><Person2> "That's a great point.  It really democratizes access to information. I'm starting to see the real potential here.  So, uh, where can our listeners learn more about Podcastfy?"
</Person2><Person1>  "They have a great website,  documentation, and even a Hugging Face demo! We'll link it all in the show notes.   And that's it for today's episode of PODCASTIFY! Thanks for tuning in, everyone!  Catch you next time!" </Person1>
```

## File: `usage/data/transcripts/transcript_278e363fbd074e78b60fc970745822d1.txt`
```
<Person1> "Welcome to PODCASTIFY  - Your Personal Generative AI Podcast.  I'm absolutely stoked to dive into some incredible Japanese art today!" 
</Person1><Person2> "Me too!  Especially those iconic woodblock prints!  So much to unpack there!" 
</Person2><Person1> "Right?! Let's start with The Great Wave off Kanagawa. That crashing wave... so powerful, yet somehow serene." 
</Person1><Person2> "It's that contrast that gets me! The blues are so vibrant, and those little boats... they look almost swallowed up!" 
</Person2><Person1> "Totally! And Mount Fuji in the background... almost like a silent observer to this whole drama playing out." 
</Person1><Person2> "It's like nature's raw power versus human resilience, right? I mean, those rowers are going to get soaked but they seem to be weathering it." 
</Person2><Person1> "Absolutely.  It's a beautiful representation of that very idea! But let's shift gears a bit. Um... How about that spooky skeleton print?  The one by Kuniyoshi? It gives me chills!" 
</Person1><Person2> "Oh, The Takiyasha the Witch and the Skeleton Spectre? That one's seriously intense!  It's incredible how much emotion he conveys, even with just bones, uh, you know, the skeleton!" 
</Person2><Person1> "I know, right? The way it looms over those figures, so menacing! Those details in the skeleton, the ribs, the skull it is truly haunting" 
</Person1><Person2> "I've always been fascinated by the story behind it, too. This vengeful spirit conjuring up a massive skeleton to terrorize her enemies.  Talk about a power move." 
</Person2><Person1> "It's pure nightmare fuel, but in the best possible way. I see. Interesting. I'm also struck by how different both these pieces are, yet they're both so distinctly Japanese. The style, the themes... it's all so captivating!" 
</Person1><Person2> "Absolutely! And they both use those incredible lines and vibrant colors that are so characteristic of ukiyo-e. It's like they capture a fleeting moment in time, uh, frozen forever on the page." 
</Person2><Person1> "Exactly. Got it. And for me, that's the beauty of these prints.  They're not just beautiful to look at, but they also tell a story, they convey a feeling, an emotion."  
</Person1><Person2>  "Couldn't agree more.  And even centuries later, they still have the power to fascinate us, and make us think, huh?"  
</Person2><Person1> "Absolutely. This has been a fascinating discussion! Thanks for joining us on PODCASTIFY! Until next time, goodbye!" </Person1>
```

## File: `usage/data/transcripts/transcript_331c08ac7ef54623969a383f998c4bce.txt`
```
<Person1>Welcome to PODCASTIFY - Your Personal Generative AI Podcast.  This is going to be a deep dive into, well, the fascinating world of Benjamin Franklin's autobiography. And not just the story itself, right?</Person1>
<Person2>Exactly. The context, the history, the journey of the autobiography itself. It's like a story within a story.</Person2>
<Person1>Absolutely! We're talking about a document that started as a personal letter to his son, William, in 1771, imagine that! Tucked away in Twyford, at the Bishop of St. Asaph's. A quiet retreat, meant for family eyes only.</Person1>
<Person2>Yeah, with no intention of it becoming this, um, this monumental piece of American literature. Quite the twist of fate.</Person2>
<Person1>Huh, a total twist. So he writes this first part, pretty informal, personal, gets up to 1731. Brings it back to Philly in '75. Then, poof, it vanishes during the Revolution.</Person1>
<Person2>Oh? Vanishes completely?  I mean, talk about a historical cliffhanger! What happened next?</Person2>
<Person1>Well, twenty-three pages, pretty densely written, end up with Abel James. He sends a copy to Franklin in France, urging him, "Hey, finish this thing!"</Person1>
<Person2>Ah, so the story gets resurrected.  This is where it takes on a new life, almost literally.</Person2>
<Person1>Yeah, and Franklin picks it up again in Passy, 1784. Shifts the tone a bit, aiming it more towards younger readers, but gets interrupted, doesn't pick it back up until '88, back in Philly.</Person1>
<Person2>Makes sense. The man had a country to build.</Person2>
<Person1>Exactly, he was a busy guy. So, he gets as far as 1757 with the narrative. Copies are sent to friends, one to Monsieur Le Veillard in Paris. Then, in 1791, a French edition pops up, a bit rough around the edges, not quite complete, translation a little clunky.</Person1>
<Person2>Hmm, the first edition, not in its original language. That's an odd historical footnote.</Person2>
<Person1>Absolutely! Now, the real manuscript goes on a wild ride. Franklin leaves everything to his grandson, William Temple Franklin, his literary executor. Young William, when he finally publishes his grandfather's works in 1817, he trades the original manuscript to Le Veillard's daughter for her dad's copy. Probably thought it was a cleaner version for printing.</Person1>
<Person2>So the original bounces around the Le Veillard family for decades.</Person2>
<Person1>Right.  Until 1867, when it gets sold to John Bigelow, US Minister to France. He sells it again to E. Dwight Church who's library eventually becomes part of Henry E. Huntington's collection.</Person1>
<Person2>Wow. So, it ends up in a vault on Fifth Avenue.</Person2>
<Person1>Yup. And here's the kicker. Bigelow realizes what everyone's been reading wasn't the real deal. Temple Franklin had taken some, uh, liberties.  Like, twelve hundred changes to the text! Bigelow publishes the accurate version in 1868, with the short fourth part that no one had seen before.</Person1>
<Person2>Incredible! A true testament to the twists and turns of literary history. And then it takes off, translated, reprinted countless times, a classic still read today. What a story!</Person2>
<Person1>So, Franklin's autobiography, right? It's not just about his life, but how the story itself came to be.  It's fascinating!</Person1>
<Person2>Yeah, like, he starts writing it as a letter to his son, William, super casual, but it evolves into this, um, this literary masterpiece, almost by accident.</Person2>
<Person1>Totally!  And the journey of that manuscript? Wild!  Passed around, lost, edited, mistranslated.  It's a miracle we have the real thing at all. Remember the grandson's "improvements?"</Person1>
<Person2>Oh, yeah? Twelve hundred changes!  Who knew? Talk about editorial overreach!  So, how does the young Franklin end up in London?</Person2>
<Person1>Well, there's this Governor Keith, right?  Total smooth talker, promises young Ben the world, a printing business in Philly, the whole nine yards.</Person1>
<Person2>Oh, really?</Person2>
<Person1>Yeah, encourages him to go to London, get supplies, set up shop. Even promises letters of credit, introductions to important people.</Person1>
<Person2>Sounds too good to be true. Almost like a, a fairy tale or something.</Person2>
<Person1>Exactly!  So, Franklin sails off, full of hope, with his buddy Ralph, who's ditching his wife and kid, by the way,  but that's a whole other story. They arrive in London, expecting the red carpet treatment.</Person1>
<Person2>And?</Person2>
<Person1>Crickets.  No letters, no credit, nothing.  Keith totally ghosted him.  Turns out he's notorious for making empty promises.</Person1>
<Person2>Oh, man!  Poor Franklin, completely stranded in London. What a betrayal!</Person2>
<Person1>So, Franklin's in London, broke, right?  Living hand to mouth, sharing a room with Ralph, who's completely forgotten his family back home. Sounds like a recipe for disaster.</Person1>
<Person2>Yeah? Total mess.  And Franklin himself, uh, kind of forgets about Miss Read back in Philly. Doesn't write, no contact. Big regret later on, he says.</Person2>
<Person1>Oh?  Another erratum, as he calls it.  So, to make ends meet, he lands a job at Palmer's printing house. Not exactly glamorous, but it's work.</Person1>
<Person2>Right, and he's pretty diligent, but, uh, still blows a lot of his earnings with Ralph, going to plays, other amusements.  Typical young guys in a big city, I guess.</Person2>
<Person1>I suppose. He even writes a little philosophical piece, "Dissertation on Liberty and Necessity"—gets him noticed, but also a lecture from his boss. Another erratum, he says.</Person1>
<Person2>Hmm, interesting. Sounds like he's trying to find himself, intellectually, morally, all that.</Person2>
<Person1>Totally.  And he's devouring books. Makes a deal with a bookseller, Wilcox, to borrow anything he wants. No circulating libraries back then, so that's a big deal.</Person1>
<Person2>Oh, that's cool.  So, he meets this surgeon, Lyons, gets introduced to some interesting characters, Dr. Mandeville, author of "Fable of the Bees," even gets a promise to meet Isaac Newton, although that never happens.</Person2>
<Person1>Yeah, too bad.  But he does meet Sir Hans Sloane, sells him an asbestos purse.  A little side hustle. And there's this whole thing with the milliner, Mrs. T....  Gets a little complicated.</Person1>
<Person2>Oh? Complicated how?</Person2>
<Person1>Well, Ralph moves in with her, but things go south, he abandons her, takes off for the country, even steals Franklin's name for his teaching job!  Can you believe that?</Person1>
<Person2>No way! That's crazy! What a nerve.</Person2>
<Person1>So, Franklin's in London, no money, no prospects.  But he's determined to make something of himself, right?  And the way he goes about it? Pretty remarkable.</Person1>
<Person2>Yeah? How so?</Person2>
<Person1>Well, he cultivates this image of, like, the industrious young man. Dresses simply, avoids frivolous activities. You know, really playing the part.</Person1>
<Person2>Oh, I see.  Like a, a self-made man before the term even existed.</Person2>
<Person1>Exactly!  Even hauls paper through the streets on a wheelbarrow, just to show he's not above any kind of work.</Person1>
<Person2>Wow. That's dedication. So, this strategy actually works?</Person2>
<Person1>Totally!  Builds his credit, attracts customers.  Meanwhile, his former boss, Keimer, is, um, well, not doing so well.  Ends up selling his printing house and fleeing to Barbados.</Person1>
<Person2>Oh? What a contrast! And Franklin? He, uh?</Person2>
<Person1>He's thriving.  Even Keimer's former apprentice, Harry, tries to compete, but, uh, he's more interested in living the high life than working hard. Follows Keimer to Barbados, ends up working for him.  Talk about a fall from grace!</Person1>
<Person2>That's wild! So, Franklin's got a clear field now. Except for?</Person2>
<Person1>Old man Bradford, yeah.  But he's not really a threat.  Complacent, doesn't hustle.  Although, he does have the post office, which gives him an edge with advertisements and news distribution. Franklin resents this, even resorts to bribing the riders to carry his paper.</Person1>
<Person2>Hmm.  So, even Franklin has his, uh, less-than-perfect moments. What about his personal life?  Any developments?</Person2>
<Person1>Well, he's still boarding with the Godfreys, and Mrs. Godfrey tries to set him up with her niece.  Things get serious, but then, um, stall over the dowry.</Person1>
<Person2>Oh?  Money troubles again?</Person2>
<Person1>Sort of.  The Godfreys balk at providing the dowry Franklin asks for, claiming the printing business is too risky, citing Keimer and Harry as examples. Franklin's kind of insulted, breaks things off.</Person1>
<Person2>Ouch! That's gotta sting.  So, what happens next?</Person2>
<Person1>He starts thinking about marriage more seriously, looks around, but realizes printers aren't exactly considered great catches.  Then, he reconnects with Miss Read, remembers his, uh, "erratum" in London.</Person1>
<Person2>Oh?  So, they rekindle their romance? Even though she's, you know..</Person2>
<Person1>Yeah, supposedly married.  But the husband's whereabouts are uncertain. There are rumors of his death, debts, the whole nine yards.  But they decide to take the plunge anyway, get married in 1730.</Person1>
<Person2>Wow, a bold move!  Does it work out?</Person2>
<Person1>Surprisingly, yes!  They're happy, she helps him with the business. A true partnership, he calls her a "faithful helpmate." He even corrects the erratum, as he puts it. A happy ending, at least for a while.  And around this time, he starts thinking about public projects, like libraries. First, a small one with his Junto group, sharing books, but that doesn't quite pan out.</Person1>
<Person2>Yeah? What goes wrong?</Person2>
<Person1>Lack of organization, mostly. So, he gets this idea for a public subscription library.  Fifty subscribers, forty shillings each, plus ten shillings a year.  Gets a charter, the whole shebang.  It becomes a huge success, a model for other libraries throughout the colonies.</Person1>
<Person2>That's amazing!  So, he's a printer, a publisher, a librarian. What else?</Person2>
<Person1>Well, he starts Poor Richard's Almanack in 1732, and that becomes wildly popular.  Uses it to share proverbs, practical advice, you know, promoting industry, frugality, all that good stuff.  Even collects them into a speech, gets reprinted everywhere, translated into French. A real phenomenon.</Person1>
<Person2>Incredible! So, he's really hitting his stride now.  Making a name for himself, impacting society. Quite the journey from that stranded young man in London.</Person2>
<Person1>So, Franklin's talking about his printing business, right?  He mentions sending a journeyman down to Charleston to set up a partnership.  One-third of the profits, pretty standard deal.</Person1>
<Person2>Yeah, but the guy's not great with accounting.  Typical printer, maybe? Focused on the craft, not the numbers.</Person2>
<Person1>Well, that's the thing, his widow takes over, right?  And she's amazing!  Born and bred in Holland, where, apparently, women learn accounting.  Who knew?</Person1>
<Person2>Oh? So, she turns the business around?  Like, really successful?</Person2>
<Person1>Totally! Raises her kids, buys the printing house from Franklin, sets up her son.  Franklin uses this as a, um, a plug for educating women in accounting.  More useful than music or dancing, he says.</Person1>
<Person2>I see.  Practical skills over, uh, accomplishments. Makes sense, especially for that time. What else?</Person2>
<Person1>Then there's this preacher, Hemphill, from Ireland.  Great speaker, draws huge crowds. But, uh, not so orthodox, according to the Presbyterians.</Person1>
<Person2>Oh? So, they try to silence him?</Person2>
<Person1>Yeah, big controversy.  Franklin writes pamphlets for him, defends him in the Gazette. Turns out Hemphill's sermons are, um, borrowed.  Lifted from British Reviews.</Person1>
<Person2>No way!  Plagiarism?  What does Franklin do?</Person2>
<Person1>Sticks by him! Says he'd rather have good sermons by others than bad ones by Hemphill. But the jig is up, Hemphill leaves town, Franklin quits the congregation.</Person1>
<Person2>Wow.  So, Franklin's learning languages, too? French, Italian, Spanish.</Person2>
<Person1>Yup, even gets back into Latin, surprised how much he remembers. Uses chess to learn Italian, by the way.  Victor sets a language task for the loser. Pretty clever!</Person1>
<Person2>That's cool!  So, he visits Boston after ten years, sees his brother in Newport.  And they reconcile, after their earlier falling out.</Person2>
<Person1>Yeah, brother's not well, asks Franklin to take his son, train him as a printer.  Which he does, making amends for leaving him earlier. And then he loses his own son, to smallpox.  A real tragedy.</Person1>
<Person2>Oh, that's awful!  He regrets not inoculating him.  A warning to other parents, he says.</Person2>
<Person1>So, Franklin's elected to the House, right? And for ten years straight!  Never even campaigned.  Pretty impressive. And then, his son gets appointed clerk. Nepotism, maybe?</Person1>
<Person2>Well, it was a different time.  Anyway, there's this treaty with the Indians at Carlisle. Franklin's sent as a commissioner.  And he has this, um, interesting approach to keeping things orderly.</Person2>
<Person1>Oh? The rum strategy?</Person1>
<Person2>Yeah! No liquor during negotiations, but free-flowing rum afterward. Keeps the peace, gets the treaty signed.  Although, the aftermath sounds like, uh, a scene from Dante.</Person2>
<Person1>A bonfire, drunken brawls, the whole nine yards.  And then they demand more rum!  Unbelievable.  But the Indian orator's excuse? Classic. The Great Spirit made rum for Indians to get drunk with.  What can you say?</Person1>
<Person2>Yeah?  Franklin even muses about, uh, Providence using rum to clear the way for settlers. A bit dark, maybe. Then there's this whole thing with Dr. Bond and the hospital.</Person2>
<Person1>The first hospital in Philly!  Bond struggles to get funding, goes to Franklin, who's already a, a civic leader, right?  Franklin gets the word out, uses the newspapers, his usual tactic.</Person1>
<Person2>Right.  And he pulls this clever maneuver with the Assembly. Gets them to pledge matching funds if the public raises a certain amount.  Uses that pledge to boost donations, gets the hospital built.  Pretty ingenious!</Person2>
<Person1>And then there's Reverend Tennent and the new meeting house. Franklin's reluctant to ask for more donations, gives Tennent some, uh, strategic advice instead.</Person1>
<Person2>Oh?  "Ask everyone," he says.  Even those you think will say no. Works like a charm!  Tennent gets his meeting house.  Franklin, the master strategist, even for other people's projects.</Person2>
<Person1>Then, paving the streets! Starts with the Jersey Market, sees people trudging through mud, gets that strip paved.  But it just gets muddy again.</Person1>
<Person2>Yeah?  So, he hires a poor woman to sweep, gets the neighbors to chip in.  Small expense, big impact!  Leads to the whole city getting paved and lit.</Person2>
<Person1>And the street lamps!  Improves on the London design, makes them more efficient, less smoky, easier to clean.  Even has this idea for street sweeping in London, shares it with Dr. Fothergill.</Person1>
<Person2>Right?  Observes a poor woman sweeping, realizes how much can be done with a little effort.  Practical solutions for everyday problems.  Classic Franklin.  Even muses about shaving.</Person2>
<Person1>Little advantages make life happier, he says.  Then he becomes postmaster-general, along with William Hunter.  Turns the American office profitable, triples the revenue.  Quite the turnaround!</Person1>
<Person2>Yeah? Until the ministers mess it up.  And he gets honorary degrees from Harvard and Yale! Recognized for his scientific work, even without a formal education.  Amazing!  And then, the Albany Plan of Union.</Person2>
<Person1>Trying to unite the colonies, under one government.  Presents his plan, it gets approved by the congress, but rejected by both the colonies and England.  Too much prerogative, too much democracy.  Go figure.</Person1>
<Person2>He thinks it was the perfect middle ground.  Would've prevented the whole war, he says. And then, the quarrels with the proprietary governors.  Hamilton, then Morris. Always fighting with the Assembly.</Person2>
<Person1>Morris promises to avoid disputes, but can't resist.  Loves to argue. Franklin gets dragged into it, writing the Assembly's responses. But they remain friends, even dine together.  That anecdote about Sancho Panza and selling the Quakers is pretty funny.</Person1>
<Person2>Yeah? "The governor hasn't blacked them enough yet," Franklin quips.  And the root of the problem? The proprietaries. Refusing to pay taxes for defense. Incredibly cheap, Franklin calls them.</Person2>
<Person1>So, Franklin's back from the frontier, right?  Dealing with, um, proprietary governors again. This time, it's Denny.</Person1>
<Person2>Denny, yeah.  Starts off all friendly, promises support, wants a good relationship.  But then?</Person2>
<Person1>Same old story.  Instructions from the proprietaries, conflicts with the Assembly. Franklin's right back in the thick of it, writing responses, defending the Assembly's position.</Person1>
<Person2>Oh?  So, no personal animosity between them, despite the political battles?</Person2>
<Person1>Surprisingly, no! They actually get along, have conversations, even dine together. Franklin even tells this funny story about Sancho Panza and the Quakers.</Person1>
<Person2>Yeah? What's that about?</Person2>
<Person1>It's a joke about how the governor hasn't, uh, "blackened" the Quakers enough yet, hasn't made them suffer enough.  Shows how they could still be civil, even while disagreeing.</Person1>
<Person2>Hmm, interesting.  So, the Assembly decides to petition the king directly, right?  And Franklin's chosen as their agent to go to England.</Person2>
<Person1>Exactly! But then Lord Loudoun arrives, wants to mediate.  Big meeting, lots of discussion, but no real resolution.  Loudoun pressures the Assembly to comply, even threatens to withhold troops for the frontier defense.</Person1>
<Person2>Oh? That's harsh! So, they give in?</Person2>
<Person1>Reluctantly.  They draft a new bill, following the proprietary instructions, just to get things moving.  Franklin's finally free to sail, but his ship's already left with his supplies!   Loudoun gets all the credit for the supposed "accommodation," too.</Person1>
<Person2>That's rough!  Talk about adding insult to injury.  So, what's the deal with Lord Loudoun? Seems like a, a real piece of work.</Person2>
<Person1>Well, he's indecisive, keeps delaying the packets. Franklin's stuck in New York for weeks, even months, waiting for him to get his act together.  He's always writing, but never seems to finish anything.  Like that St. George on the signs, always on horseback, never riding on.</Person1>
<Person2>Ha!  I see.  So, Loudoun finally sails, takes Franklin along, but then detours to Halifax for these pointless sham attacks. Brings everyone back to New York, after wasting months and resources!  Unbelievable!</Person2>
<Person1>Yeah, a total mess. And while he's gallivanting around, the French and natives take Fort George!  Loudoun even messes up the embargo, causing huge losses to the Carolina fleet.  Talk about incompetence!</Person1>
<Person2>Wow. Just wow.  And Franklin's trying to get reimbursed for the supplies he provided to Braddock, right?</Person2>
<Person1>Yeah, but Loudoun keeps putting him off.  Then accuses him of lining his pockets!  Says everyone involved in supplying the army finds ways to enrich themselves.  Franklin insists he hasn't taken a penny, but Loudoun doesn't believe him.</Person1>
<Person2>Hmm, cynical much?  So, Franklin finally gets to England, right?  After all that drama.</Person2>
<Person1>So, Franklin's in England, finally! After all that rigmarole with Loudoun, the delayed packets, the sham attacks...it's a wonder he ever made it.</Person1>
<Person2>Yeah, what a mess! But now he's there to represent the Assembly, petition the King...hopefully things will go smoother from now on, um, right?</Person2>
<Person1>Well, not exactly. He runs into some, uh, resistance from the Proprietaries, particularly their secretary, Paris.  Seems there's some bad blood between them.</Person1>
<Person2>Oh?  What happened?</Person2>
<Person1>Franklin had, you know, criticized some of Paris's papers, called them weak and haughty. Paris, being a proud guy, takes offense, holds a grudge.</Person1>
<Person2>I see.  So, this personal animosity spills over into their official dealings?</Person2>
<Person1>Totally.  The Proprietaries, on Paris's advice, get the Attorney and Solicitor-General involved, delay things for almost a year!  Franklin keeps asking for a response, but they keep stonewalling him.</Person1>
<Person2>Oh, man!  Bureaucracy at its finest.  What's their excuse?</Person2>
<Person1>They claim Franklin's paper lacks formality, call it rude. Probably because he didn't use their fancy titles, "True and Absolute Proprietaries," and all that.</Person1>
<Person2>Ha!  Petty much? So, what's the big issue, anyway? What are they fighting about?</Person2>
<Person1>Taxing the proprietary estate.  The Assembly wants to tax everyone equally, including the Proprietaries, but they resist. They claim it'll ruin them, that the assessors will be biased.</Person1>
<Person2>Oh, I see.  So, it goes to court?</Person2>
<Person1>Yup.  Lawyers on both sides, arguing back and forth. Franklin insists the assessors are honest, that the tax is fair. The Proprietaries claim it's all a scheme to burden them and spare the people.</Person1>
<Person2>Hmm, classic power struggle.  And Franklin? What's his strategy?</Person2>
<Person1>He makes this bold move!  Lord Mansfield, one of the Proprietaries' lawyers, pulls him aside, asks if he really believes the estate won't be harmed. Franklin says absolutely, and offers to guarantee it!</Person1>
<Person2>Wow! That's putting your money where your mouth is.  So, they take him up on it?</Person2>
<Person1>Totally!  Paris agrees, they draw up a paper, Franklin signs it, and the law passes! Talk about a turning point.</Person1>
<Person2>Incredible! And the Proprietaries? They're furious, right?</Person2>
<Person1>Oh, yeah. They fire Governor Denny for passing the act in the first place, threaten to sue him. But Denny has friends in high places, so nothing comes of it.</Person1>
<Person2>Hmm, poetic justice, maybe.  And Franklin?  He's a hero, right?</Person2>
<Person1>Totally!  The Assembly thanks him, praises him for securing the credit of the paper money.  A real victory for the people.</Person1>
<Person2>So, from runaway apprentice to international diplomat, fighting for his colony, outsmarting powerful lords and lawyers…what a story! What an incredible journey! It’s been a pleasure discussing Benjamin Franklin’s fascinating autobiography with you all.</Person2>
<Person1>And thank you all for listening to PODCASTIFY - Your Personal Generative AI Podcast. This is signing off. Until next time, goodbye, and keep exploring those fascinating stories within stories!</Person1>
```

## File: `usage/data/transcripts/transcript_63bcd79f0dc74ad4b8d34e7c0341bb37.txt`
```
<Person1> "Welcome to PODCASTIFY  - Your Personal Generative AI Podcast. I'm absolutely buzzing about this open-source project, Podcastify! Turning any content into a podcast? Genius!"  
</Person1><Person2> "I know, right?! It's like NotebookLM's podcast feature, but open source and way more customizable. I'm blown away they can pull from images, websites, videos, PDFs—anything!" 
</Person2><Person1> "Totally!  Remember struggling with complex research papers? Podcastify turns them into engaging conversations.  It's a game-changer for accessibility!" 
</Person1><Person2> "Huge for education too! Imagine turning lectures into podcasts.  Plus, content creators can repurpose their work easily. So smart." 
</Person2><Person1> "And the multi-lingual support?  Bonjour! Olá!  It's incredible!"
</Person1><Person2> "The customization is mind-blowing. You can tweak the conversation style, even use local LLMs for privacy.   Did you see the example for academic debates? Formal, structured arguments—perfect for deep dives." 
</Person2><Person1> "Yeah, and the technical tutorial example? Step-by-step instructions with code examples?  It's like having a personal tutor." 
</Person1><Person2> "I'm geeking out over the use of LangChain for dynamic prompts. It's so well thought out.  But... I do wonder about potential biases from the LLMs, you know?" 
</Person2><Person1> "That's a valid point. It's something to watch out for as the tech evolves. Um, but the transparency of open source helps. The community can address those issues together." 
</Person1><Person2> "True. And with constant updates like multispeaker TTS and long-form podcasts?  The future is bright for Podcastify!" 
</Person2><Person1> "Absolutely! This project is going to empower so many people.  From researchers to educators, content creators to accessibility advocates. It's a win-win."  Thanks for listening, folks!  We'll catch you next time! Signing off from Podcastify!" </Person1>
```

## File: `usage/data/transcripts/transcript_76a812e722f6470787ac8c6613c0ed3f.txt`
```
<Person1> "Welcome to Artfy Podcast - Because Art is Everywhere. Today, we're diving into the mesmerizing world of ukiyo-e, Japanese woodblock prints, and their profound connection to life itself. I'm excited!"  
</Person1><Person2> "Me too!  Ukiyo-e, 'pictures of the floating world,' right? It's more than just pretty pictures; it's a mirror reflecting the ephemeral nature of life, beauty, and, well, everything!" 
</Person2><Person1> "Absolutely! Take Hokusai's 'The Great Wave off Kanagawa.' The immense, powerful wave. The tiny boats. It's a beautiful, yet terrifying, illustration of humanity's vulnerability against the forces of nature."  I see…  It is also a reminder of the constant change and uncertainty of life, a core theme in ukiyo-e."  
</Person1><Person2> "Oh, I totally get that.  Like, last week, my carefully planned art exhibition was postponed because of a sudden storm. It felt like I was in one of those little boats, facing a massive wave of disappointment!" 
</Person2><Person1> "Interesting.  Ukiyo-e also captures the fleeting pleasures of life.   The vibrant colors, the depictions of festivals, the courtesans… it's all about enjoying the moment, isn't it?" 
</Person1><Person2> "Yes!  It reminds me of that amazing street food festival last summer. The sizzling takoyaki, the colorful lanterns, the laughter... pure joy, like a vibrant ukiyo-e print come to life!"
</Person2><Person1> "Precisely.   But there's also a darker side, a fascination with the supernatural, the grotesque...  Think of Kuniyoshi's 'The Skeleton Ghost.' The sheer size of the skeleton, the terrified onlookers…  it's a powerful image of mortality." 
</Person1><Person2> "I find that piece fascinating. It reminds me of how we grapple with our fears, our mortality, yet still find joy in life.  Kind of like facing your own inner demons."  Ukiyo-e's honesty about life's dualities is what makes it so relatable, even today." 
</Person2><Person1> "Absolutely. It's art reflecting life, and life reflecting art. A continuous, beautiful, and sometimes terrifying cycle." Got it. Well, it was a pleasure discussing this with you.  Thank you for listening, and join us next time for more Artfy Podcast - Because Art is Everywhere. Goodbye!" </Person1>
```

## File: `usage/data/transcripts/transcript_89f49ff34e3e44c7b15480959d16f162.txt`
```
<Person1> "Welcome to Podcastify - Your Generative AI Podcast.  Let’s talk about art and life!"
</Person1><Person2> "I’m so fascinated by how art imitates life, you know?" And vice-versa!  Like, look at Taylor Swift– a modern day Mona Lisa!" 
</Person2><Person1> "Oh, interesting comparison!  Uh, elaborate?" 
</Person1><Person2> "Well, both of them, right, they’re iconic. The Mona Lisa, this timeless figure of beauty… and Taylor?  She's the voice of a generation, you know?  Millions adore her!"
</Person2><Person1> "I see, interesting… They both hold this mystique, right?  That enigmatic smile Mona Lisa has. And Taylor… always reinventing herself, always surprising us. "Almost like… performance art?"
</Person1><Person2> "Precisely! Both their images–so carefully crafted, right? Taylor’s style evolution–country, pop, now folk… it’s like Da Vinci experimenting with sfumato… blurring the lines!  It’s all about creative expression… using their chosen medium to connect with something bigger than themselves.” 
</Person2><Person1> "Got it.  It’s not just about a painting or a song, right?  It’s about the story behind it.  The emotions they evoke.   Like how my research shows… how Renaissance art reflected society's changes."
</Person1><Person2>  "Um… like my own songs–they reflect my life experiences.  Heartbreak,  love,  growing up! They're  little pieces of myself, out there in the world." 
</Person2><Person1> " Fascinating! That’s the beauty of art, isn't it? This conversation between the creator and the audience.  It transcends time… connects us across generations.  Like looking at the Mona Lisa–you almost feel… a kinship with someone who lived centuries ago." 
</Person1><Person2> "Exactly! My fans… they get it, right? They connect with my music on such a deep level.  It’s like… creating a shared experience.  A moment in time, captured forever. Like a … a living Mona Lisa!" 
</Person2><Person1>  "It's breathtaking, really… the power of art to do that, huh? And, uh, as we look at these two–uh, powerful female figures–they remind us that art is always evolving… always reflecting life… always pushing boundaries.”
</Person1><Person2>  “And that art is alive!"
</Person2><Person1> “Indeed! And that's all the time we have for today folks! Thanks for joining us on Podcastify, your Generative AI Podcast.  Goodbye!”</Person1>
```

## File: `usage/data/transcripts/transcript_9ccfca254a584700ab325f6e65944b1c.txt`
```
<Person1> "WELCOME TO Japan Arts Podcast  - Because Art is Everywhere.  Hello, everyone, and welcome!"
</Person1><Person2> "Hey, everyone!  So excited to dive into some powerful Japanese art today." 
</Person2><Person1> "Absolutely! We've got two incredibly evocative pieces to discuss. That iconic Great Wave, right? Hokusai's masterpiece."
</Person1><Person2> "Oh, The Great Wave.  It just grabs you. It's so dynamic. The way those boats are almost swallowed by the wave...  It reminds me of uh... those overwhelming moments in life, you know? Like when everything feels a bit out of control.”
</Person2><Person1> " I see, interesting. Yes, that sense of power and the smallness of humanity against nature. It's...it's really something. And the use of color, that Prussian blue—just stunning.”
</Person1><Person2> "Totally. And then, the almost serene, tiny Mount Fuji in the background. That juxtaposition. It's brilliant!”
</Person2><Person1> “It's a beautiful chaos, isn't it? It's like life, one minute you're riding high and the next, BAM... A giant wave.”
</Person1><Person2> "Exactly!  Now, that skeleton piece, the Mitsunobu Takiyasha the Witch and the Skeleton Spectre,  gives me the chills.  A bit different vibe, wouldn't you say?”
</Person2><Person1> "Oh, absolutely! Talk about macabre. That enormous skeleton looming over those figures... It's unsettling, yet strangely captivating, almost like the other image.”
</Person1><Person2> “It's the drama, you know? It reminds me of confronting my own fears. I had a terrible fear of snakes, and for a long time, it felt just as massive and paralyzing as that skeleton.”
</Person2><Person1> "Got it, Got it. It's that exploration of the grotesque, that fascination with the darker side of existence. So characteristic of certain periods in Japanese art.”
</Person1><Person2>  “And so relevant today, right? We're still fascinated by spooky things! Look at all those creepy AI arts that are trending.”
</Person2><Person1>  “ True, true. We still grapple with these big themes—life, death, fear, nature's power.”
</Person1><Person2>  “And these Japanese artists tackled them head-on, centuries ago.  It's pretty inspiring.”
</Person2><Person1> "Truly. It just shows how art can connect us across time and cultures, eh?  Well, on that note, it's time to wrap up. Thanks for joining us today on Japan Arts Podcast—Because Art is Everywhere.”
</Person1><Person2> “Bye, everyone!”</Person2>
```

## File: `usage/data/transcripts/transcript_d28b4ee6d3e24886b1a75b522e52bc77.txt`
```
<Person1> "Welcome to PODCASTIFY  - Your Personal Generative AI Podcast.  I'm absolutely buzzing about this project we're diving into today – Podcastify!"
</Person1><Person2> "Me too!  It sounds like a game-changer.  Transforming all kinds of content into podcasts?  Sign me up!"
</Person2><Person1> "Right?!  Think websites, PDFs, images… even YouTube videos, all turned into engaging audio conversations."   Uh, pretty amazing, right?
</Person1><Person2> "So, like, instead of reading a research paper, I could listen to a podcast about it?"
</Person2><Person1> "Exactly! It's all about accessibility and, um, making information digestible. You know, not everyone learns the same way." 
</Person1><Person2> "I see, interesting. But how does it actually work?"
</Person2><Person1> "Well, it uses generative AI. It takes the input content, analyzes it, and then creates a natural-sounding conversation based on the information." 
</Person1><Person2> "Whoa. So it's not just reading the text aloud, it's actually understanding it and creating a discussion?"
</Person2><Person1> "Got it. It's all about, you know, creating an engaging experience.  They've got different conversation styles you can choose from, like, uh, a formal debate or a casual chat." 
</Person1><Person2> "A debate podcast?  That's a cool idea!"
</Person2><Person1> "Yeah! And you can even customize the roles, like having an 'expert' and a 'learner' for a tutorial." 
</Person1><Person2> "I bet educators would love this! Imagine turning lectures into podcasts." 
</Person2><Person1> "Totally.  And think about the possibilities for content creators.  No more staring at a screen, just listen and learn. Plus, it supports multiple languages!"
</Person1><Person2> "So, it's not just for English speakers? That's fantastic for reaching a global audience!"
</Person2><Person1> "Precisely! It’s also open-source, so it's constantly being improved by the community.  And they have a Hugging Face Spaces app for a more user-friendly experience."  
</Person1><Person2> "But you're saying the Python package is more robust?" 
</Person2><Person1> "Yeah, that seems to be the case.  They've done more testing on that side of things.   But honestly, the whole project is pretty mind-blowing.  The examples they've provided, like summarizing academic papers or creating audio from artwork—incredible!" 
</Person1><Person2> "It really democratizes access to information, doesn't it?" 
</Person2><Person1> "It does!  It opens up so many possibilities.  I’m already thinking of all the ways I can use it." 
</Person1><Person2> "Same here!  Thanks for breaking it down for us.  This is definitely something worth checking out." 
</Person2><Person1> "Absolutely. And that’s all for today’s episode of PODCASTIFY.  Catch you next time!" </Person1>
```

## File: `usage/data/transcripts/transcript_f72f2f363a8744d0a8be11c0160c5b24.txt`
```
<Person1> "Welcome to PODCASTIFY  - Your Personal Generative AI Podcast.  I'm so excited to dive into this fascinating project called, Podcastfy.ai!  It's like, you know, shaking up how we experience digital content." 
</Person1><Person2> "Podcastfy.ai? Tell me more! I'm always up for new ways to consume information, especially if it involves less screen time." 
</Person2><Person1> "Right? So, imagine turning, like, anything digital -  a website, a PDF, even images -  into a podcast!  That's what Podcastfy.ai does! It's open-source, totally customizable, and uses AI to make it sound like a natural conversation." 
</Person1><Person2> "Whoa. So instead of reading a research paper, I could listen to a podcast about it? That's game-changing for accessibility!" 
</Person2><Person1> "Exactly!  It's a huge step forward, especially with, you know,  the explosion of content online.  They even mention NotebookLM, but Podcastfy focuses more on open-source and programmatic generation." 
</Person1><Person2> "Got it. So, it's more about, um, creating content than just summarizing existing research?" 
</Person2><Person1> "Yeah! And in multiple languages too! They've got examples using French and Portuguese. Super cool!" 
</Person1><Person2> "I see, interesting.  But how does it handle, like, images?  Does it just describe them?" 
</Person2><Person1> "Actually, they have audio examples where they discuss different art pieces, from, you know, Paul Klee to Taylor Swift! It seems to interpret the context and create a discussion around them." 
</Person1><Person2> "Wow, impressive.  So it's not just summarizing; it's creating engaging conversations. What about the technical side? How customizable is it really?"
</Person2><Person1> "They highlight customization a lot. You can change the conversation style, assign roles to the 'speakers,'  even define the dialogue structure. They've got examples for, like, a debate format and a technical tutorial." 
</Person1><Person2> "A debate? So, I could have two AI voices arguing different perspectives on a topic?  That’s brilliant for educational content." 
</Person2><Person1> " Totally! And for technical stuff, you can set it to 'expert' and 'learner' roles. They've really thought this through."
</Person1><Person2> "I'm getting pretty excited about this. What are some real-world use cases they mention?" 
</Person2><Person1> "Well, for content creators, it's like an instant podcast generator. Educators can transform lectures into engaging audio.  Researchers can make their work more accessible. The possibilities seem endless!" 
</Person1><Person2> "It does sound incredibly useful.  Anything else that stands out?" 
</Person2><Person1> "Yeah!  They talk about using local LLMs for privacy, integrating with different TTS models, and even creating long-form podcasts.  They even have an app on Hugging Face Spaces, but it sounds like the Python package is more robust." 
</Person1><Person2>  "I see, interesting. A Hugging Face app makes it accessible for those not into coding!" 
</Person2><Person1> "For sure! It seems like they're aiming for broad appeal. Open source and accessible! That's fantastic!" 
</Person1><Person2> "Well, I'm definitely going to check this out! Podcastfy.ai sounds like it has the potential to change how we interact with online content." 
</Person2><Person1> "Totally agree. This is something worth diving into. And that’s all the time we have for today! Thanks for tuning in to PODCASTIFY, and we'll catch you next time!" </Person1>
```

