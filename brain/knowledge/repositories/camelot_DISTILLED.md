---
id: repo-fetched-camelot-151552
type: knowledge
owner: OA
registered_at: 2026-04-05T04:04:10.423411
tags: ["auto-cloned", "oa-assimilated"]
---

# FETCHED_camelot_151552

## Assimilation Report
Auto-cloned repository: FETCHED_camelot_151552

## Application for OmniClaw
No structural integration blueprint provided.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<p align="center">
  <img src="https://raw.githubusercontent.com/camelot-dev/camelot/master/docs/_static/camelot.png" width="200">
</p>

# Camelot: PDF Table Extraction for Humans

[![tests](https://github.com/camelot-dev/camelot/actions/workflows/tests.yml/badge.svg)](https://github.com/camelot-dev/camelot/actions/workflows/tests.yml) [![Documentation Status](https://readthedocs.org/projects/camelot-py/badge/?version=master)](https://camelot-py.readthedocs.io/en/master/)
[![codecov.io](https://codecov.io/github/camelot-dev/camelot/badge.svg?branch=master&service=github)](https://codecov.io/github/camelot-dev/camelot?branch=master)
[![image](https://img.shields.io/pypi/v/camelot-py.svg)](https://pypi.org/project/camelot-py/) [![image](https://img.shields.io/pypi/l/camelot-py.svg)](https://pypi.org/project/camelot-py/) [![image](https://img.shields.io/pypi/pyversions/camelot-py.svg)](https://pypi.org/project/camelot-py/)

**Camelot** is a Python library that can help you extract tables from PDFs.

---

**Extract tables from PDFs in just a few lines of code:**

Try it yourself in our interactive quickstart notebook. [![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camelot-dev/camelot/blob/master/examples/camelot-quickstart-notebook.ipynb)

Or check out a simple example using [this pdf](https://github.com/camelot-dev/camelot/blob/master/docs/_static/pdf/foo.pdf).

<pre>
>>> import camelot
>>> tables = camelot.read_pdf('foo.pdf')
>>> tables
&lt;TableList n=1&gt;
>>> tables.export('foo.csv', f='csv', compress=True) # json, excel, html, markdown, sqlite
>>> tables[0]
&lt;Table shape=(7, 7)&gt;
>>> tables[0].parsing_report
{
    'accuracy': 99.02,
    'whitespace': 12.24,
    'order': 1,
    'page': 1
}
>>> tables[0].to_csv('foo.csv') # to_json, to_excel, to_html, to_markdown, to_sqlite
>>> tables[0].df # get a pandas DataFrame!
</pre>

| Cycle Name | KI (1/km) | Distance (mi) | Percent Fuel Savings |                 |                 |                |
| ---------- | --------- | ------------- | -------------------- | --------------- | --------------- | -------------- |
|            |           |               | Improved Speed       | Decreased Accel | Eliminate Stops | Decreased Idle |
| 2012_2     | 3.30      | 1.3           | 5.9%                 | 9.5%            | 29.2%           | 17.4%          |
| 2145_1     | 0.68      | 11.2          | 2.4%                 | 0.1%            | 9.5%            | 2.7%           |
| 4234_1     | 0.59      | 58.7          | 8.5%                 | 1.3%            | 8.5%            | 3.3%           |
| 2032_2     | 0.17      | 57.8          | 21.7%                | 0.3%            | 2.7%            | 1.2%           |
| 4171_1     | 0.07      | 173.9         | 58.1%                | 1.6%            | 2.1%            | 0.5%           |

Camelot also comes packaged with a [command-line interface](https://camelot-py.readthedocs.io/en/latest/user/cli.html)!

Refer to the [QuickStart Guide](https://github.com/camelot-dev/camelot/blob/master/docs/user/quickstart.rst#quickstart) to quickly get started with Camelot, extract tables from PDFs and explore some basic options.

**Tip:** Visit the `parser-comparison-notebook` to get an overview of all the packed parsers and their features. [![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camelot-dev/camelot/blob/master/examples/parser-comparison-notebook.ipynb)

**Note:** Camelot only works with text-based PDFs and not scanned documents. (As Tabula [explains](https://github.com/tabulapdf/tabula#why-tabula), "If you can click and drag to select text in your table in a PDF viewer, then your PDF is text-based".)

You can check out some frequently asked questions [here](https://camelot-py.readthedocs.io/en/latest/user/faq.html).

## Why Camelot?

- **Configurability**: Camelot gives you control over the table extraction process with [tweakable settings](https://camelot-py.readthedocs.io/en/latest/user/advanced.html).
- **Metrics**: You can discard bad tables based on metrics like accuracy and whitespace, without having to manually look at each table.
- **Output**: Each table is extracted into a **pandas DataFrame**, which seamlessly integrates into [ETL and data analysis workflows](https://gist.github.com/vinayak-mehta/e5949f7c2410a0e12f25d3682dc9e873). You can also export tables to multiple formats, which include CSV, JSON, Excel, HTML, Markdown, and Sqlite.

See [comparison with similar libraries and tools](https://github.com/camelot-dev/camelot/wiki/Comparison-with-other-PDF-Table-Extraction-libraries-and-tools).

## Installation

### Using conda

The easiest way to install Camelot is with [conda](https://conda.io/docs/), which is a package manager and environment management system for the [Anaconda](http://docs.continuum.io/anaconda/) distribution.

```bash
conda install -c conda-forge camelot-py
```

### Using pip

You can also use pip to install Camelot:

```bash
pip install "camelot-py"
```

Note that [additional dependencies](https://camelot-py.readthedocs.io/en/latest/user/install-deps.html) may be required if you want to use the non-default backend [ghostscript](https://www.ghostscript.com/).

### From the source code

```bash
git clone https://github.com/camelot-dev/camelot.git
```

and install using pip:

```
cd camelot
pip install "."
```

Note that [additional dependencies](https://camelot-py.readthedocs.io/en/latest/user/install-deps.html) may be required if you want to use the non-default backend [ghostscript](https://www.ghostscript.com/).

## Documentation

The documentation is available at [http://camelot-py.readthedocs.io/](http://camelot-py.readthedocs.io/).

## Wrappers

- [camelot-php](https://github.com/randomstate/camelot-php) provides a [PHP](https://www.php.net/) wrapper on Camelot.

## Related projects

- [camelot-sharp](https://github.com/BobLd/camelot-sharp) provides a C sharp implementation of Camelot.

## Contributing

The [Contributor's Guide](https://camelot-py.readthedocs.io/en/latest/dev/contributing.html) has detailed information about contributing issues, documentation, code, and tests.

## Versioning

Camelot uses [Semantic Versioning](https://semver.org/). For the available versions, see the tags on this repository. For the changelog, you can check out the [releases](https://github.com/camelot-dev/camelot/releases) page.

## License

This project is licensed under the MIT License, see the [LICENSE](https://github.com/camelot-dev/camelot/blob/master/LICENSE) file for details.

The documentation theme is licensed under a seperate BSD-like License, see the [LICENSE](https://github.com/camelot-dev/camelot/blob/master/docs/_themes/LICENSE) file for details.

```

### File: requirements.txt
```txt
Using Python 3.10.18 environment at .nox/safety

```

### File: docs\requirements.txt
```txt
sphinx==9.0.4
sphinx-book-theme>=1.0.1
sphinx-click==6.2.0
myst_parser==4.0.0
ghostscript==0.8.1
opencv-python-headless==4.12.0.88
matplotlib==3.10.8
accessible-pygments==0.0.5
pydata-sphinx-theme==0.16.1
sphinx-copybutton==0.5.2
sphinx-prompt==1.10.2

```

### File: CODE_OF_CONDUCT.md
```md
Be cordial or be on your way. --Kenneth Reitz

https://kennethreitz.org/essays/2013/01/27/be-cordial-or-be-on-your-way

# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, caste, color, religion, or sexual
identity and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

- Demonstrating empathy and kindness toward other people
- Being respectful of differing opinions, viewpoints, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
- Focusing on what is best not just for us as individuals, but for the overall
  community

Examples of unacceptable behavior include:

- The use of sexualized language or imagery, and sexual attention or advances of
  any kind
- Trolling, insulting or derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information, such as a physical or email address,
  without their explicit permission
- Other conduct which could reasonably be considered inappropriate in a
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
https://github.com/camelot-dev/camelot/issues .
reported to the community leaders responsible for enforcement at
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

**Community Impact**: A violation through a single incident or series of
actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or permanent
ban.

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
standards, including sustained inappropriate behavior, harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within the
community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.1, available at
[https://www.contributor-covenant.org/version/2/1/code_of_conduct.html][v2.1].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][mozilla coc].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][faq]. Translations are available at
[https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.1]: https://www.contributor-covenant.org/version/2/1/code_of_conduct.html
[mozilla coc]: https://github.com/mozilla/diversity
[faq]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations

```

### File: VETTING_REPORT.md
```md
---
title: Auto Vetting Report for camelot
date: 2026-04-05
analyst: civ_vetting_pipeline
status: AUTO_VETTED
---

# Auto-Vetted Repository
This repository was automatically swept and vetted by the batch processor. Only documentation remains.

```

### File: .github\ISSUE_TEMPLATE\bug_report.md
```md
---
name: Bug report
about: Please follow this template to submit bug reports.
title: ""
labels: bug
assignees: ""
---

<!-- Please read the filing issues section of the contributor's guide first: https://camelot-py.readthedocs.io/en/latest/dev/contributing.html#filing-issues -->

**Describe the bug**

<!-- A clear and concise description of what the bug is. -->

**Steps to reproduce the bug**

<!-- Steps used to install `camelot`:
1. Add step here (you can add more steps too) -->

<!-- Steps to be used to reproduce behavior:
1. Add step here (you can add more steps too) -->

**Expected behavior**

<!-- A clear and concise description of what you expected to happen. -->

**Code**

<!-- Add the camelot code snippet that you used. -->

```

# add your code here
```

**PDF**

<!-- Add the PDF file that you want to extract tables from. -->

**Screenshots**

<!-- If applicable, add screenshots to help explain your problem. -->

**Environment**

- OS: [e.g. macOS]
- Python version:
- Numpy version:
- OpenCV version:
- Ghostscript version:
- camelot version:

**Additional context**

<!-- Add any other context about the problem here. -->

```

### File: .github\workflows\constraints.txt
```txt
lockfile<0.13.0,>=0.12.2
pip==25.0.1
nox==2025.11.12
virtualenv==20.36.1

```

