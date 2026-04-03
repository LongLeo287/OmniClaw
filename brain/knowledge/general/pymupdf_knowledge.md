---
id: pymupdf-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:04.144895
---

# KNOWLEDGE EXTRACT: pymupdf
> **Extracted on:** 2026-03-30 17:51:31
> **Source:** pymupdf

---

## File: `PyMuPDF.md`
```markdown
# 📦 pymupdf/PyMuPDF [🔖 PENDING/APPROVE]
🔗 https://github.com/pymupdf/PyMuPDF
🌐 https://pymupdf.readthedocs.io

## Meta
- **Stars:** ⭐ 9322 | **Forks:** 🍴 699
- **Language:** Python | **License:** AGPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
PyMuPDF is a high performance Python library for data extraction, analysis, conversion & manipulation of PDF (and other) documents.

## README (trích đầu)
```
# PyMuPDF

**PyMuPDF** is a high performance **Python** library for data extraction, analysis, conversion & manipulation of [PDF (and other) documents](https://pymupdf.readthedocs.io/en/latest/the-basics.html#supported-file-types).

# Community
Join us on **Discord** here: [#pymupdf](https://discord.gg/TSpYGBW4eq)


# Installation

**PyMuPDF** requires **Python 3.10 or later**, install using **pip** with:

`pip install PyMuPDF`

There are **no mandatory** external dependencies. However, some [optional features](#pymupdf-optional-features) become available only if additional packages are installed.

You can also try without installing by visiting [PyMuPDF.io](https://pymupdf.io/#examples).


# Usage

Basic usage is as follows:

```python
import pymupdf # imports the pymupdf library
doc = pymupdf.open("example.pdf") # open a document
for page in doc: # iterate the document pages
  text = page.get_text() # get plain text encoded as UTF-8

```


# Documentation

Full documentation can be found on [pymupdf.readthedocs.io](https://pymupdf.readthedocs.io).



# <a id="pymupdf-optional-features"></a>Optional Features

* [fontTools](https://pypi.org/project/fonttools/) for creating font subsets.
* [pymupdf-fonts](https://pypi.org/project/pymupdf-fonts/) contains some nice fonts for your text output.
* [Tesseract-OCR](https://github.com/tesseract-ocr/tesseract) for optical character recognition in images and document pages.



# About

**PyMuPDF** adds **Python** bindings and abstractions to [MuPDF](https://mupdf.com/), a lightweight **PDF**, **XPS**, and **eBook** viewer, renderer, and toolkit. Both **PyMuPDF** and **MuPDF** are maintained and developed by [Artifex Software, Inc](https://artifex.com).

**PyMuPDF** was originally written by [Jorj X. McKie](mailto:jorj.x.mckie@outlook.de).


# License and Copyright

**PyMuPDF** is available under [open-source AGPL](https://www.gnu.org/licenses/agpl-3.0.html) and commercial license agreements. If you determine you cannot meet the requirements of the **AGPL**, please contact [Artifex](https://artifex.com/contact/pymupdf-inquiry.php) for more information regarding a commercial license.





```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

