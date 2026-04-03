---
id: camelot-dev-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.240330
---

# KNOWLEDGE EXTRACT: camelot-dev
> **Extracted on:** 2026-03-30 17:31:15
> **Source:** camelot-dev

---

## File: `camelot.md`
```markdown
# 📦 camelot-dev/camelot [🔖 PENDING/APPROVE]
🔗 https://github.com/camelot-dev/camelot
🌐 https://camelot-py.readthedocs.io

## Meta
- **Stars:** ⭐ 3659 | **Forks:** 🍴 536
- **Language:** Python | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Python library to extract tabular data from PDFs

## README (trích đầu)
```
<p align="center">
  <img src="https://raw.githubusercontent.com/camelot-dev/camelot/master/brain/knowledge/docs_legacy/_static/camelot.png" width="200">
</p>

# Camelot: PDF Table Extraction for Humans

[![tests](https://github.com/camelot-dev/camelot/actions/workflows/tests.yml/badge.svg)](https://github.com/camelot-dev/camelot/actions/workflows/tests.yml) [![Documentation Status](https://readthedocs.org/projects/camelot-py/badge/?version=master)](https://camelot-py.readthedocs.io/en/master/)
[![codecov.io](https://codecov.io/github/camelot-dev/camelot/badge.svg?branch=master&service=github)](https://codecov.io/github/camelot-dev/camelot?branch=master)
[![image](https://img.shields.io/pypi/v/camelot-py.svg)](https://pypi.org/project/camelot-py/) [![image](https://img.shields.io/pypi/l/camelot-py.svg)](https://pypi.org/project/camelot-py/) [![image](https://img.shields.io/pypi/pyversions/camelot-py.svg)](https://pypi.org/project/camelot-py/)

**Camelot** is a Python library that can help you extract tables from PDFs.

---

**Extract tables from PDFs in just a few lines of code:**

Try it yourself in our interactive quickstart notebook. [![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/camelot-dev/camelot/blob/master/examples/camelot-quickstart-notebook.ipynb)

Or check out a simple example using [this pdf](https://github.com/camelot-dev/camelot/blob/master/brain/knowledge/docs_legacy/_static/pdf/foo.pdf).

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

Ref
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

