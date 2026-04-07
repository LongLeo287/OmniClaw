---
id: trafilatura
type: knowledge
owner: OA_Triage
---
# trafilatura
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
# Trafilatura: Discover and Extract Text Data on the Web

<br/>

<img alt="Trafilatura Logo" src="https://raw.githubusercontent.com/adbar/trafilatura/master/docs/trafilatura-logo.png" align="center" width="60%"/>

<br/>

[![Python package](https://img.shields.io/pypi/v/trafilatura.svg)](https://pypi.python.org/pypi/trafilatura)
[![Python versions](https://img.shields.io/pypi/pyversions/trafilatura.svg)](https://pypi.python.org/pypi/trafilatura)
[![Documentation Status](https://readthedocs.org/projects/trafilatura/badge/?version=latest)](http://trafilatura.readthedocs.org/en/latest/?badge=latest)
[![Code Coverage](https://img.shields.io/codecov/c/github/adbar/trafilatura.svg)](https://codecov.io/gh/adbar/trafilatura)
[![Downloads](https://static.pepy.tech/badge/trafilatura/month)](https://pepy.tech/project/trafilatura)
[![Reference DOI: 10.18653/v1/2021.acl-demo.15](https://img.shields.io/badge/DOI-10.18653%2Fv1%2F2021.acl--demo.15-blue)](https://aclanthology.org/2021.acl-demo.15/)

<br/>

<img alt="Demo as GIF image" src="https://raw.githubusercontent.com/adbar/trafilatura/master/docs/trafilatura-demo.gif" align="center" width="80%"/>

<br/>


## Introduction

Trafilatura is a cutting-edge **Python package and command-line tool**
designed to **gather text on the Web and simplify the process of turning
raw HTML into structured, meaningful data**. It includes all necessary
discovery and text processing components to perform **web crawling,
downloads, scraping, and extraction** of main texts, metadata and
comments. It aims at staying **handy and modular**: no database is
required, the output can be converted to commonly used formats.

Going from HTML bulk to essential parts can alleviate many problems
related to text quality, by **focusing on the actual content**,
**avoiding the noise** caused by recurring elements like headers and footers
and by **making sense of the data and metadata** with selected information.
The extractor strikes a balance between limiting noise (precision) and
including all valid parts (recall). It is **robust and reasonably fast**.

Trafilatura is [widely used](https://trafilatura.readthedocs.io/en/latest/used-by.html)
and integrated into [thousands of projects](https://github.com/adbar/trafilatura/network/dependents)
by companies like HuggingFace, IBM, and Microsoft Research as well as institutions like
the Allen Institute, Stanford, the Tokyo Institute of Technology, and
the University of Munich.


### Features

- Advanced web crawling and text discovery:
   - Support for sitemaps (TXT, XML) and feeds (ATOM, JSON, RSS)
   - Smart crawling and URL management (filtering and deduplication)

- Parallel processing of online and offline input:
   - Live URLs, efficient and polite processing of download queues
   - Previously downloaded HTML files and parsed HTML trees

- Robust and configurable extraction of key elements:
   - Main text (common patterns and generic algorithms like jusText and readability)
   - Metadata (title, author, date, site name, categories and tags)
   - Formatting and structure: paragraphs, titles, lists, quotes, code, line breaks, in-line text formatting
   - Optional elements: comments, links, images, tables

- Multiple output formats:
   - TXT and Markdown
   - CSV
   - JSON
   - HTML, XML and [XML-TEI](https://tei-c.org/)

- Optional add-ons:
   - Language detection on extracted content
   - Speed optimizations

- Actively maintained with support from the open-source community:
   - Regular updates, feature additions, and optimizations
   - Comprehensive documentation


### Evaluation and alternatives

Trafilatura consistently outperforms other open-source libraries in text
extraction benchmarks, showcasing its efficiency and accuracy in
extracting web content. The extractor tries to strike a balance between
limiting noise and including all valid parts.

For more information see the [benchmark section](https://trafilatura.readthedocs.io/en/latest/evaluation.html)
and the [evaluation readme](https://github.com/adbar/trafilatura/blob/master/tests/README.rst)
to run the evaluation with the latest data and packages.


#### Other evaluations:

- Most efficient open-source library in *ScrapingHub*'s [article extraction benchmark](https://github.com/scrapinghub/article-extraction-benchmark)
- Best overall tool according to [Bien choisir son outil d'extraction de contenu à partir du Web](https://hal.archives-ouvertes.fr/hal-02768510v3/document)
  (Lejeune & Barbaresi 2020)
- Best single tool by ROUGE-LSum Mean F1 Page Scores in [An Empirical Comparison of Web Content Extraction Algorithms](https://webis.de/downloads/publications/papers/bevendorff_2023b.pdf)
  (Bevendorff et al. 2023)


## Usage and documentation

[Getting started with Trafilatura](https://trafilatura.readthedocs.io/en/latest/quickstart.html)
is straightforward. For more information and detailed guides, visit
[Trafilatura's documentation](https://trafilatura.readthedocs.io/):

- [Installation](https://trafilatura.readthedocs.io/en/latest/installation.html)
- Usage:
  [On the command-line](https://trafilatura.readthedocs.io/en/latest/usage-cli.html),
  [With Python](https://trafilatura.readthedocs.io/en/latest/usage-python.html),
  [With R](https://trafilatura.readthedocs.io/en/latest/usage-r.html)
- [Core Python functions](https://trafilatura.readthedocs.io/en/latest/corefunctions.html)
- Interactive Python Notebook: [Trafilatura Overview](docs/Trafilatura_Overview.ipynb)
- [Tutorials and use cases](https://trafilatura.readthedocs.io/en/latest/tutorials.html)

Youtube playlist with video tutorials in several languages:

- [Web scraping tutorials and how-tos](https://www.youtube.com/watch?v=8GkiOM17t0Q&list=PL-pKWbySIRGMgxXQOtGIz1-nbfYLvqrci)


## License

This package is distributed under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

Versions prior to v1.8.0 are under GPLv3+ license.


### Contributing

Contributions of all kinds are welcome. Visit the [Contributing
page](https://github.com/adbar/trafilatura/blob/master/CONTRIBUTING.md)
for more information. Bug reports can be filed on the [dedicated issue
page](https://github.com/adbar/trafilatura/issues).

Many thanks to the
[contributors](https://github.com/adbar/trafilatura/graphs/contributors)
who extended the docs or submitted bug reports, features and bugfixes!


## Context

This work started as a PhD project at the crossroads of linguistics and
NLP, this expertise has been instrumental in shaping Trafilatura over
the years. Initially launched to create text databases for research purposes
at the Berlin-Brandenburg Academy of Sciences (DWDS and ZDL units),
this package continues to be maintained but its future depends on community support.

**If you value this software or depend on it for your product, consider
sponsoring it and contributing to its codebase**. Your support
[on GitHub](https://github.com/sponsors/adbar) or [ko-fi.com](https://ko-fi.com/adbarbaresi)
will help maintain and enhance this popular package.

*Trafilatura* is an Italian word for [wire
drawing](https://en.wikipedia.org/wiki/Wire_drawing) symbolizing the
refinement and conversion process. It is also the way shapes of pasta
are formed.

### Author

Reach out via ia the software repository or the [contact
page](https://adrien.barbaresi.eu/) for inquiries, collaborations, or
feedback. See also social networks for the latest updates.

-   Barbaresi, A. [Trafilatura: A Web Scraping Library and Command-Line
    Tool for Text Discovery and
    Extraction](https://aclanthology.org/2021.acl-demo.15/), Proceedings
    of ACL/IJCNLP 2021: System Demonstrations, 2021, p. 122-131.
-   Barbaresi, A. "[Generic Web Content Extraction with Open-Source
    Software](https://hal.archives-ouvertes.fr/hal-02447264/document)",
    Proceedings of KONVENS 2019, Kaleidoscope Abstracts, 2019.
-   Barbaresi, A. "[Efficient construction of metadata-enhanced web
    corpora](https://hal.archives-ouvertes.fr/hal-01371704v2/document)",
    Proceedings of the [10th Web as Corpus Workshop
    (WAC-X)](https://www.sigwac.org.uk/wiki/WAC-X), 2016.


### Citing Trafilatura

Trafilatura is widely used in the academic domain, chiefly for data
acquisition. Here is how to cite it:

[![Reference DOI: 10.18653/v1/2021.acl-demo.15](https://img.shields.io/badge/DOI-10.18653%2Fv1%2F2021.acl--demo.15-blue)](https://aclanthology.org/2021.acl-demo.15/)
[![Zenodo archive DOI: 10.5281/zenodo.3460969](https://zenodo.org/badge/DOI/10.5281/zenodo.3460969.svg)](https://doi.org/10.5281/zenodo.3460969)

``` shell
@inproceedings{barbaresi-2021-trafilatura,
  title = {{Trafilatura: A Web Scraping Library and Command-Line Tool for Text Discovery and Extraction}},
  author = "Barbaresi, Adrien",
  booktitle = "Proceedings of the Joint Conference of the 59th Annual Meeting of the Association for Computational Linguistics and the 11th International Joint Conference on Natural Language Processing: System Demonstrations",
  pages = "122--131",
  publisher = "Association for Computational Linguistics",
  url = "https://aclanthology.org/2021.acl-demo.15",
  year = 2021,
}
```


### Software ecosystem

Jointly developed plugins and additional packages also contribute to the
field of web data extraction and analysis:

<img alt="Software ecosystem" src="https://raw.githubusercontent.com/adbar/htmldate/master/docs/software-ecosystem.png" align="center" width="65%"/>

Corresponding posts can be found on [Bits of
Language](https://adrien.barbaresi.eu/blog/tag/trafilatura.html).

Impressive, you have reached the end of the page: Thank you for your
interest!

```

### File: docs\requirements.txt
```txt
# with version specifier
sphinx>=8.1.3
pydata-sphinx-theme>=0.16.1
docutils>=0.21.2
sphinx-sitemap>=2.6.0

# without version specifier
trafilatura

```

### File: .readthedocs.yaml
```yaml
# Read the Docs configuration file for Sphinx projects
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the OS, Python version and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"
    # You can also specify other tool versions:
    # nodejs: "20"
    # rust: "1.70"
    # golang: "1.20"

# Build documentation in the "docs/" directory with Sphinx
sphinx:
  configuration: docs/conf.py
  # You can configure Sphinx to use a different builder, for instance use the dirhtml builder for simpler URLs
  # builder: "dirhtml"
  # Fail on all warnings to avoid broken references
  # fail_on_warning: true

# Optionally build your docs in additional formats such as PDF and ePub
# formats:
#    - pdf
#    - epub

# Optional but recommended, declare the Python requirements required
# to build your documentation
# See https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
python:
  install:
    - requirements: docs/requirements.txt

```

### File: CONTRIBUTING.md
```md
## How to contribute


If you value this software or depend on it for your product,
consider sponsoring it and contributing to its codebase.
Your support will help ensure the sustainability and growth of the project.

There are many ways to contribute:

  * Sponsor the project: Show your appreciation [on GitHub](https://github.com/sponsors/adbar) or [ko-fi.com](https://ko-fi.com/adbarbaresi).
  * Find bugs and submit bug reports: Help making Trafilatura an even more robust tool.
  * Write code: Fix bugs or add new features by writing [pull requests](https://docs.github.com/en/pull-requests) with a list of what you have done.
  * Improve the documentation: Write tutorials and guides, correct mistakes, or translate existing content.
  * Submit feature requests: Share your feedback and suggestions.


Here are some important resources:

  * [List of currently open issues](https://github.com/adbar/trafilatura/issues) (no pretention to exhaustivity!)
  * [How to contribute to open source](https://opensource.guide/how-to-contribute/)

A special thanks to all the [contributors](https://github.com/adbar/trafilatura/graphs/contributors) who have played a part in Trafilatura.


## Testing and evaluating the code

Here is how you can run the tests and code quality checks. Pull requests will only be accepted if the changes are tested and if they there are no errors. 

- Install the necessary packages with `pip install trafilatura[dev]`
- Run `pytest` from trafilatura's directory, or select a particular test suite, for example `realworld_tests.py`, and run `pytest realworld_tests.py` or simply `python3 realworld_tests.py`
- Run `mypy` on the directory: `mypy trafilatura/`

If you work on text extraction it is useful to check if performance is equal or better on the benchmark.

See the [tests Readme](tests/README.rst) for more information.


For further questions you can use [GitHub issues](https://github.com/adbar/trafilatura/issues) and discussion pages, or [E-Mail](https://adrien.barbaresi.eu/).

Thanks,

Adrien

```

### File: HISTORY.md
```md
## History / Changelog


## 2.0.0

Breaking changes:
- Python 3.6 and 3.7 deprecated (#709)
- `bare_extraction()`:
   - now returns an instance of the `Document` class by default
   - `as_dict` deprecation warning → use `.as_dict()` method on return value (#730)
- `bare_extraction()` and `extract()`: `no_fallback` deprecation warning → use `fast` instead (#730)
- downloads: remove `decode` argument in `fetch_url()` → use `fetch_response` instead (#724)
- deprecated graphical user interface now removed (#713)
- extraction: move `max_tree_size` parameter to `settings.cfg` (#742)
- use type hinting (#721, #723, #748)
- see [Python](https://trafilatura.readthedocs.io/en/latest/usage-python.html#deprecations) and [CLI](https://trafilatura.readthedocs.io/en/latest/usage-cli.html#deprecations) deprecations in the docs

Fixes:
- set `options.source` before raising error on empty doc tree by @dmoklaf (#707)
- robust encoding in `options.source` (#717)
- more robust mapping for conversion to HTML (#721)
- CLI downloads: use all information in settings file (#734)
- downloads: cleaner urllib3 code (#736)
- refine table markdown output by @unsleepy22 (#752)
- extraction fix: images in text nodes by @unsleepy22 (#757)

Metadata:
- more robust URL extraction (#710)

Command-line interface:
- CLI: print URLs early for feeds and sitemaps with `--list` with @gremid (#744)
- CLI: add 126 exit code for high error ratio (#747)

Maintenance:
- remove already deprecated functions and args (#716)
- add type hints (#723, #728)
- setup: use `pyproject.toml` file (#715)
- simplify code (#708, #709, #727)
- better debug messages in `main_extractor` (#714)
- evaluation: review data, update packages, add magic_html (#731)
- setup: explicit exports through `__all__` (#740)
- tests: extend coverage (#753)

Documentation:
- fix link in `docs/index.html` by @nzw0301 (#711)
- remove docs from published packages (#743)
- update docs (#745)


## 1.12.2

- downloads: add support for SOCKS proxies with @gremid (#682)
- extraction fix: ValueError in table spans (#685)
- spider: `prune_xpath` parameter added by @felipehertzer (#684)
- spider: relax strict parameter for link extraction (#687)
- sitemaps: `max_sitemaps` parameter added by @felipehertzer (#690)
- maintenance: make compression libraries optional (#691)
- metadata: review and lint code (#694)


### 1.12.1

Navigation:
- spider: restrict search to sections containing URL path (#673)
- crawler: add parameter class and types, **breaking change** for undocumented functions (#675)
- maintenance: simplify link discovery and extend tests (#674)
- CLI: review code, add types and tests (#677)

Bugfixes:
- fix `AttributeError` in element deletion (#668)
- fix `MemoryError` in table header columns (#665)

Docs:
- docs: fix variable name for extract_metadata in quickstart by @jpigla in #678


### 1.12.0

Breaking change:
- enforce fixed list of output formats, deprecate `-out` on the CLI (#647)

Faster, more accurate extraction:
- review link and structure checks (#653)
- improve justext fallback (#652)
- baseline: prevent LXML error in JSON-LD (#643), do not use as backup extraction (#646)
- review XPaths for undesirable content (#645)

Bugfixes and maintenance:
- CLI fix: markdown format should trigger `include_formatting` (#649)
- images fix: use a length threshold on src attribute (#654)
- XML-TEI: replace RelaxNG by DTD, remove pickle, and update (#655)
- formatting & markdown fix: add newlines (#656)
- table fix: prevent `MemoryError` & `ValueError` during conversion to text (#658)

Documentation:
- update `crawls.rst`: `known` is an unexpected argument, by @tommytyc in #638


### 1.11.0

Breaking change:
- metadata now skipped by default (#613), to trigger inclusion in all output formats:
   - `with_metadata=True` (Python)
   - `--with-metadata` (CLI)

Extraction:
- add HTML as output format (#614)
- better and faster baseline extraction (#619)
- better handling of HTML/XML elements (#628)
- XPath rules added with @felipehertzer (#540)
- fix: avoid faulty readability_lxml content (#635)

Evaluation:
- new scripts and data with @LydiaKoerber (#606, #615)
- additional data with @swetepete (#197)

Maintenance:
- docs extended and updated, added page on deduplication (#618)
- review code, add tests and types in part of the submodules (#620, #623, #624, #625)


### 1.10.0

Breaking changes:
- raise errors on deprecated CLI and function arguments (#581)
- regroup classes and functions linked to deduplication (#582)
``trafilatura.hashing`` → ``trafilatura.deduplication``

Extraction:
- port of is_probably_readerable from readability.js by @zirkelc in #587
- Markdown table fixes by @naktinis in #601
- fix list spacing in TXT output (#598)
- CLI fixes: file processing options, mtime, and tests (#605)
- CLI fix: read standard input as binary (#607)

Downloads:
- fix deflate and add optional zstd to accepted encodings (#594)
- spider fix: use internal download utilities for robots.txt (#590)

Maintenance:
- add author XPaths (#567)
- update justext and lxml dependencies (#593)
- simplify code: unique function for length tests (#591)

Docs:
- fix typos by @RainRat in #603


### 1.9.0

Extraction:
- add markdown as explicit output (#550)
- improve recall preset (#571)
- speedup for readability-lxml (#547)
- add global options object for extraction and use it in CLI (#552)
- fix: better encoding detection (#548)
- recall: fix for lists inside tables with @mikhainin (#534)
- add symbol to preserve vertical spacing in Markdown (#499)
- fix: table cell separators in non-XML output (#563)
- slightly better accuracy and execution speed overall

Metadata:
- add file creation date (date extraction, JSON & XML-TEI) (#561)
- fix: empty content in meta tag by @felipehertzer (#545)

Maintenance:
- restructure and simplify code (#543, #556)
- CLI & downloads: revamp and use global options (#565)
- eval: review code, add guidelines and small benchmark (#542)
- fix: raise error if config file does not exist (#554)
- deprecate `process_record()` (#549)
- docs: convert readme to markdown and update info (#564, #578)


### 1.8.1

Maintenance:
- Pin LXML to prevent broken dependency (#535)

Extraction:
- Improve extraction accuracy for major news outlets (#530)
- Fix formatting by correcting order of element generation and space handling with @dlwh (#528)
- Fix: prevent tail insertion before children in nested elements by @knit-bee (#536)


### 1.8.0

Extraction:
- Better precision by @felipehertzer (#509, #520)
- Code formatting in TXT/Markdown output added (#498)
- Improved CSV output (#496)
- LXML: compile XPath expressions (#504)
- Overall speedup about +5%

Downloads and Navigation:
- More robust scans with `is_live_page()` (#501)
- Better sitemap start and safeguards (#503, #506)
- Fix for headers in response object (#513)

Maintenance:
- License changed to Apache 2.0
- `Response` class: convenience functions added (#497)
- `lxml.html.Cleaner` removed (#491)
- CLI fixes: parallel cores and processing (#524)


### 1.7.0

Extraction:
- improved `html2txt()` function

Downloads:
- add advanced `fetch_response()` function
→ pending deprecation for `fetch_url(decode=False)`

Maintenance:
- support for LXML v5+ (#484 by @knit-bee, #485)
- update [htmldate](https://github.com/adbar/htmldate/releases/tag/v1.7.0)


### 1.6.4

Maintenance:
- MacOS: fix setup, update htmldate and add tests (#460)
- drop invalid XML element attributes with @vbarbaresi in #462
- remove cyclic imports (#458)

Navigation:
- introduce `MAX_REDIRECTS` config setting and fix urllib3 redirect handling by @vbarbaresi in #461
- improve feed detection (#457)

Documentation:
- enhancements to documentation and testing with @Maddesea in #456


### 1.6.3

Extraction:
- preserve space in certain elements with @idoshamun (#429)
- optional list of xPaths to prune by @HeLehm (#414)

Metadata:
- more precise date extraction (see [htmldate](https://github.com/adbar/htmldate/releases/tag/v1.6.0))
- new `htmldate` extensive search parameter in config (#434)
- changes in URLs: normalization, trackers removed (see [courlan](https://github.com/adbar/courlan/releases/tag/v0.9.5))

Navigation:
- reviewed code for feeds (#443)
- new config option: external URLs for feeds/sitemaps (#441)

Documentation:
- update, add page on text embeddings with @tonyyanga (#428, #435, #447)
- fix quickstart by @sashkab (#419)


### 1.6.2

Extraction:
- more lenient HTML parsing (#370)
- improved code block support with @idoshamun (#372, #401)
- conversion of relative links to absolute by @feltcat (#377)
- remove use of signal from core functions (#384)

Metadata:
- JSON-LD fix for sitenames by @felipehertzer (#383)

Command-line interface:
- more robust batch processing (#381)
- added `--probe` option to CLI to check for extractable content (#378, #392)

Maintenance:
- simplified code (#408)
- support for Python 3.12
- pinned LXML version for MacOS (#393)
- updated dependencies and parameters (notably `htmldate` and `courlan`)
- code cleaning by @marksmayo (#406)


### 1.6.1

Extraction:
- minor fixes: tables in figures (#301), headings (#354) and lists (#318)

Metadata:
- simplify and fully test JSON parsing code, with @felipehertzer (#352, #368)
- authors, JSON and unicode fixes by @felipehertzer in #365
- fix for authors without `additionalName` by @awwitecki in #363

Navigation:
- reviewed link processing in feeds and sitemaps (#340, #350)
- more robust spider (#359)
- updated underlying courlan package (#360)


### 1.6.0

Extraction:
- new content hashes and default file names (#314)
- fix deprecation warning with @sdondley in #321
- fix for metadata image by @andremacola in #328
- fix potential unicode issue in third-party extraction with @Korben00 in #331 
- review logging levels (#347)

Command-line interface:
- more efficient sitemap processing (#326)
- more efficient downloads (#338)
- fix for single URL processing (#324) and URL blacklisting (#339)

Navigation:
- additional safety check on domain similarity for feeds and sitemaps
- new function ``is_live test()`` using HTTP HEAD request (#327)
- code parts supported by new courlan version

Maintenance:
- allow ``urllib3`` version 2.0+
- minor code simplification and fixes


### 1.5.0

Extraction:
- fixes for metadata extraction with @felipehertzer (#295, #296),  @andremacola (#282, #310), and @edkrueger (#303)
- pagetype and image urls added to metadata by @andremacola (#282, #310)
- add as_dict method to Document class with @edkrueger in #306
- XML output fix with @knit-bee in #315
- various smaller fixes: lists (#309), XPaths, metadata hardening

Navigation:
- transfer URL management to courlan.UrlStore (#232, #312)
- fixes for spider module

Maintenance:
- simplify code and extend tests
- underlying packages htmldate and courlan, update setup and docs


### 1.4.1

Extraction:
- XML output improvements with @knit-bee (#273, #274)
- extraction bugs fixed (#263, #266), more robust HTML doctype parsing
- adjust thresholds for link density in paragraphs

Metadata:
- improved title and sitename detection (#284)
- faster author, categories, domain name, and tags extraction
- fixes to author emoji regexes by @felipehertzer (#269)

Command-line interface:
- review argument consistency and add deprecation warnings (#261)

Setup:
- make download timeout configurable (#263)
- updated dependencies, use of faust-cchardet for Python 3.11


### 1.4.0

Impact on extraction and output format:
- better extraction (#233, #243 & #250 with @knit-bee, #246 with @mrienstra, #258)
- XML: preserve list type as attribute (#229)
- XML TEI: better conformity with @knit-bee (#238, #242, #253, #254)
- faster text cleaning and shorter code (#237 with @deedy5, #245)
- metadata: add language when detector is activated (#224)
- metadata: extend fallbacks and test coverage for json_metadata functions by @felipehertzer (#235)
- TXT: change markdown formatting of headers by @LaundroMat (#257)

Smaller changes in convenience functions:
- add function to clear caches (#219)
- CLI: change exit code if download fails (#223)
- settings: use "\n" for multiple user agents by @k-sareen (#241)

Updates:
- docs updated (and #244 by @dsgibbons)
- package dependencies updated


### 1.3.0
- fast and robust `html2txt()` function added (#221)
- more robust parsing (#228)
- fixed bugs in metadata extraction, with @felipehertzer in #213 & #226 
- extraction about 10-20% faster, slightly better recall
- partial fixes for memory leaks (#216)
- docs extended and updated (#217, #225)
- prepared deprecation of old `process_record()` function
- more stable processing with updated dependencies


### 1.2.2
- more efficient rules for extraction
- metadata: further attributes used (with @felipehertzer)
- better baseline extraction
- issues fixed: #202, #204, #205
- evaluation updated


### 1.2.1
- ``--precision`` and ``--recall`` arguments added to the CLI
- better text cleaning: paywalls and comments
- improvements for Chinese websites (with @glacierck & @immortal-autumn): #186, #187, #188
- further bugs fixed: #189, #192 (with @felipehertzer), #200
- efficiency: faster module loading and improved RAM footprint


### 1.2.0
- efficiency: replaced module readability-lxml by trimmed fork
- bug fixed: (#179, #180, #183, #184)
- improved baseline extraction
- cleaner metadata (with @felipehertzer)


### 1.1.0
- encodings: better detection, output NFC-normalized Unicode
- maintenance and performance: more efficient code
- bugs fixed (#119, #136, #147, #160, #161, #162, #164, #167 and others)
- prepare compatibility with upcoming Python 3.11
- changed default settings
- extended documentation


### 1.0.0
- compress HTML backup files & seamlessly open .gz files
- support JSON web feeds
- graphical user interface integrated into main package
- faster downloads: reviewed backoff, compressed data
- optional modules: downloads with `pycurl`, language identification with `py3langid`
- bugs fixed (#111, #125, #132, #136, #140)
- minor optimizations and fixes by @vbarbaresi in [#124](https://github.com/adbar/trafilatura/pull/124) & [#130](https://github.com/adbar/trafilatura/pull/130)
- fixed array with single or multiples entries on json extractor by @felipehertzer in [#143](https://github.com/adbar/trafilatura/pull/143)
- code base refactored with @sourcery-ai [#121](https://github.com/adbar/trafilatura/pull/121), improved and optimized for Python 3.6+
- drop support for Python 3.5


### 0.9.3
- better, faster encoding detection: replaced `chardet` with `charset_normalizer`
- faster execution: updated `justext` to 3.0
- better extraction of sub-elements in tables (#78, #90)
- more robust web feed parsing
- further defined precision- and recall-oriented settings
- license extraction in footers (#118)


### 0.9.2
- first precision- and recall-oriented presets defined
- improvements in authorship extraction (thanks @felipehertzer)
- requesting TXT output with formatting now results in Markdown format
- bu
... [TRUNCATED]
```

### File: docs\conf.py
```py
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#

import os
import sys

sys.path.insert(0, os.path.abspath('.'))

import trafilatura

# -- Project information -----------------------------------------------------

project = 'Trafilatura'
copyright = '2025, Adrien Barbaresi'
html_show_sphinx = False
author = 'Adrien Barbaresi'
version = trafilatura.__version__


# -- General configuration ---------------------------------------------------

# The master toctree document.
master_doc = 'index'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# The short X.Y version.
version = trafilatura.__version__
# The full version, including alpha/beta/rc tags.
release = trafilatura.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'en'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_sitemap'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
add_module_names = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'pydata_sphinx_theme' # 'furo' # 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.

## pydata options
html_theme_options = {
  "github_url": "https://github.com/adbar/trafilatura",
  "external_links": [
      {"name": "Blog", "url": "https://adrien.barbaresi.eu/blog/tag/trafilatura.html"},
  ],
  "navigation_with_keys": False,
#  "use_edit_page_button": True,
#  "navigation_depth": 3,
#  "show_toc_level": 3,
}
html_theme_options["analytics"] = {
  "google_analytics_id": "G-K3R5QCVDF1",
  "analytics_anonymize_ip": True,
}

html_logo = "trafilatura-logo.png"


html_context = {
    # "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "adbar",
    "github_repo": "trafilatura",
    "github_version": "master",
    "doc_path": "docs",
}


## furo options
#html_theme_options = {
#    "announcement": "<em>Important</em> announcement!",
#}

## alabaster theme
#html_theme_options = {
#    "description": "Web scraping tool for text discovery and retrieval",
#    "show_powered_by": False,
#    "github_button": False,
#    "github_user": "adbar",
#    "github_repo": "trafilatura",
#    "github_count": True,
#    "github_banner": False,
#    "show_related": False,
#    "sidebar_collapse": True,
#    "extra_nav_links": {'test': 'https://example.org'},
#    "note_bg": "#FFF59C",
#}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

html_baseurl = 'https://trafilatura.readthedocs.io/'
sitemap_url_scheme = "{lang}latest/{link}"

html_extra_path = ['robots.txt']

```

### File: docs\robots.txt
```txt
User-agent: *

Sitemap: https://trafilatura.readthedocs.io/en/latest/sitemap.xml

```

### File: tests\baseline_tests.py
```py
"""
Unit tests for baseline functions of the trafilatura library.
"""

from lxml import html
from trafilatura import baseline, html2txt


def test_baseline():
    # Empty input
    result = baseline(b'')
    assert isinstance(result, tuple) and len(result) == 3
    assert result[0].tag == 'body'
    assert result[1] == ''
    assert result[2] == 0

    result = baseline('')
    assert isinstance(result, tuple) and len(result) == 3
    assert result[0].tag == 'body'
    assert result[1] == ''
    assert result[2] == 0

    # Invalid HTML
    _, result, _ = baseline(b'<invalid html>')
    assert result == ''

    tests = [
        '<html><body><article>' + 'The article consists of this text.'*10 + '</article></body></html>',
        '<html><body><article><b>The article consists of this text.</b></article></body></html>',
        '<html><body><quote>This is only a quote but it is better than nothing.</quote></body></html>',
    ]
    for doc in tests:
        _, result, _ = baseline(doc)
        assert result is not None

    # Invalid JSON
    filecontent = b'''
        <html>
            <body>
                <script type="application/ld+json">
                    {"articleBody": "This is the article body, it has to be long enough to fool the length threshold which is set at len 100."  # invalid JSON
                </script>
            </body>
        </html>
    '''
    _, result, _ = baseline(filecontent)
    assert result == ''

    # JSON OK
    filecontent = b'''
        <html>
            <body>
                <script type="application/ld+json">
                    {
                        "@type": "Article",
                        "articleBody": "This is the article body, it has to be long enough to fool the length threshold which is set at len 100."
                    }
                </script>
            </body>
        </html>
    '''
    _, result, _ = baseline(filecontent)
    assert len(result) > 100

    # JSON malformed
    filecontent = br'''
        <html>
            <body>
                <script type="application/ld+json">
                    {
                        "@type": "Article",
                        "articleBody": "<p>This is the article body, it has to be long enough to fool the length threshold which is set at len 100.<\/p>"
                    }
                </script>
            </body>
        </html>
    '''
    _, result, _ = baseline(filecontent)
    assert result == ''

    # Real-world examples
    my_document = r'<html><body><script type="application/ld+json">{"description":"In letzter Zeit kam man am Begriff \"Hygge\", was so viel wie \"angenehm\" oder \"gemütlich\" bedeutet, ja nicht vorbei. Jetzt macht ihm ein neuer Glücks-Trend ...","image":[{"name":"Mit der Ikigai-Methode wirst du glücklicher","url":"https:\/\/image.brigitte.de\/10973004\/uncropped-0-0\/7d00b2658fd0a3b19e1b161f4657cc20\/Xw\/ikigai--1-.jpg","width":"2048","height":"1366","@type":"ImageObject"},{"name":"Mit der Ikigai-Methode wirst du glücklicher","url":"https:\/\/image.brigitte.de\/10973004\/16x9-1280-720\/bf947c7c24167d7c0adae0be10942d57\/Uf\/ikigai--1-.jpg","width":"1280","height":"720","@type":"ImageObject"},{"name":"Mit der Ikigai-Methode wirst du glücklicher","url":"https:\/\/image.brigitte.de\/10973004\/16x9-938-528\/bf947c7c24167d7c0adae0be10942d57\/JK\/ikigai--1-.jpg","width":"938","height":"528","@type":"ImageObject"},{"name":"Mit der Ikigai-Methode wirst du glücklicher","url":"https:\/\/image.brigitte.de\/10973004\/large1x1-622-622\/f5544b7d67e1be04f7729b130e7e0485\/KN\/ikigai--1-.jpg","width":"622","height":"622","@type":"ImageObject"}],"mainEntityOfPage":{"@id":"https:\/\/www.brigitte.de\/liebe\/persoenlichkeit\/ikigai-macht-dich-sofort-gluecklicher--10972896.html","@type":"WebPage"},"headline":"Ikigai macht dich sofort glücklicher!","datePublished":"2019-06-19T14:29:08+0000","dateModified":"2019-06-19T14:29:10+0000","author":{"name":"BRIGITTE.de","@type":"Organization"},"publisher":{"name":"BRIGITTE.de","logo":{"url":"https:\/\/image.brigitte.de\/11476842\/uncropped-0-0\/f19537e97b9189bf0f25ce924168bedb\/kK\/bri-logo-schema-org.png","width":"167","height":"60","@type":"ImageObject"},"@type":"Organization"},"articleBody":"In letzter Zeit kam man am Begriff \"Hygge\" (\"gemütlich\" oder \"angenehm\") nicht vorbei. Jetzt macht ihm ein neuer Glücks-Trend Konkurrenz: \"Ikigai\". Bist du glücklich? Schwierige Frage, nicht wahr? Viele von uns müssen da erst mal überlegen.","@type":"NewsArticle"}</script></body></html>'
    _, result, _  = baseline(my_document)
    assert result.startswith('In letzter Zeit kam man') and result.endswith('erst mal überlegen.')

    my_document = "<html><body><div>   Document body...   </div><script> console.log('Hello world') </script></body></html>"
    _, result, _ = baseline(my_document)
    assert result == 'Document body...'


def test_html2txt():
    mydoc = "<html><body>Here is the body text</body></html>"
    assert html2txt(mydoc) == "Here is the body text"
    assert html2txt(html.fromstring(mydoc)) == "Here is the body text"
    assert html2txt("") == ""
    assert html2txt("123") == ""
    assert html2txt("<html></html>") == ""
    assert html2txt("<html><body/></html>") == ""
    assert html2txt("<html><body><style>font-size: 8pt</style><p>ABC</p></body></html>") == "ABC"


if __name__ == '__main__':
    test_baseline()
    test_html2txt()

```

### File: tests\cli_tests.py
```py
"""
Unit tests for the command-line interface.
"""

import io
import logging
import os
import re
import subprocess
import sys

from contextlib import redirect_stdout
from datetime import datetime
from os import path
from tempfile import gettempdir
from unittest.mock import patch

import pytest

from courlan import UrlStore

from trafilatura import cli, cli_utils, spider, settings
from trafilatura.downloads import add_to_compressed_dict, fetch_url
from trafilatura.utils import LANGID_FLAG

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
RESOURCES_DIR = path.join(path.abspath(path.dirname(__file__)), "resources")

settings.MAX_FILES_PER_DIRECTORY = 1


def test_parser():
    """test argument parsing for the command-line interface"""
    testargs = ["", "-fvv", "--xmltei", "--no-tables", "-u", "https://www.example.org"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    assert args.fast is True
    assert args.verbose == 2
    assert args.no_tables is False
    assert args.xmltei is True
    assert args.URL == "https://www.example.org"
    args = cli.map_args(args)
    assert args.output_format == "xmltei"
    testargs = ["", "--output-format", "csv", "--no-tables", "-u", "https://www.example.org"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    assert args.fast is False
    assert args.verbose == 0
    assert args.output_format == "csv"
    assert args.no_tables is False
    # test args mapping
    testargs = ["", "--markdown"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    args = cli.map_args(args)
    assert args.output_format == "markdown"
    testargs = ["", "--xml", "--no-comments", "--precision", "--recall"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    args = cli.map_args(args)
    assert args.output_format == "xml" and args.no_comments is False
    # combination possible (?)
    assert args.precision is True and args.recall is True
    args.xml, args.csv = False, True
    args = cli.map_args(args)
    assert args.output_format == "csv"
    args.csv, args.json = False, True
    args = cli.map_args(args)
    assert args.output_format == "json"
    testargs = ["", "--only-with-metadata"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    args = cli.map_args(args)
    assert args.only_with_metadata is True
    # process_args
    args.input_dir = "/dev/null"
    args.verbose = 1
    args.blacklist = path.join(RESOURCES_DIR, "list-discard.txt")
    cli.process_args(args)
    assert len(args.blacklist) == 3
    # filter
    testargs = [
        "",
        "-i",
        "resources/list-discard.txt",
        "--url-filter",
        "test1",
        "test2",
        "-vvv",
    ]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    assert args.input_file == "resources/list-discard.txt"
    assert args.url_filter == ["test1", "test2"]
    args.input_file = path.join(RESOURCES_DIR, "list-discard.txt")
    args.blacklist = path.join(RESOURCES_DIR, "list-discard.txt")
    f = io.StringIO()
    with redirect_stdout(f):
        cli.process_args(args)
    assert len(f.getvalue()) == 0
    # input directory
    testargs = ["", "--input-dir", "resources/test/"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    f = io.StringIO()
    with redirect_stdout(f):
        cli.process_args(args)
    assert len(f.getvalue()) == 0
    # version
    testargs = ["", "--version"]
    with pytest.raises(SystemExit) as e, redirect_stdout(f):
        with patch.object(sys, "argv", testargs):
            args = cli.parse_args(testargs)
    assert e.type == SystemExit
    assert e.value.code == 0
    assert re.match(
        r"Trafilatura [0-9]\.[0-9]+\.[0-9] - Python [0-9]\.[0-9]+\.[0-9]", f.getvalue()
    )


def test_climain(capfd):
    """test arguments and main CLI entrypoint"""
    # exit status required: 0
    # Windows platforms
    if os.name == "nt":
        trafilatura_bin = path.join(sys.prefix, "Scripts", "trafilatura")
    # other platforms
    else:
        trafilatura_bin = "trafilatura"
    # help display
    assert subprocess.run([trafilatura_bin, "--help"], check=True).returncode == 0
    # piped input
    empty_input = b"<html><body><article>" + b"<p>ABC</p>"*100 + b"</article></body></html>"
    result = subprocess.run([trafilatura_bin], input=empty_input, check=True)
    assert result.returncode == 0
    captured = capfd.readouterr()
    assert captured.out.strip().endswith("ABC")
    # input directory walking and processing
    env = os.environ.copy()
    if os.name == "nt":
        # Force encoding to utf-8 for Windows (seem to be a problem only in GitHub Actions)
        env["PYTHONIOENCODING"] = "utf-8"
    assert (
        subprocess.run(
            [trafilatura_bin, "--input-dir", RESOURCES_DIR], env=env, check=True
        ).returncode
        == 0
    )
    # compressed file
    with open(path.join(RESOURCES_DIR, "webpage.html.gz"), "rb") as inputf:
        compressed_input = inputf.read()
    assert subprocess.run([trafilatura_bin], input=compressed_input, check=True).returncode == 0
    captured = capfd.readouterr()
    assert captured.out.strip().endswith("in deep-red West Virginia.")


def test_input_type():
    """test input type errors"""
    testfile = "docs/trafilatura-demo.gif"
    testargs = ["", "-u", "http"]
    with patch.object(sys, "argv", testargs):
        assert cli.main() is None
    testargs = ["", "-v"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    with open(testfile, "rb") as f:
        teststring = f.read(1024)
    assert cli.examine(teststring, args) is None
    assert cli.examine([1, 2, 3], args) is None
    testfile = "docs/usage.rst"
    with open(testfile, "r", encoding="utf-8") as f:
        teststring = f.read()
    assert cli.examine(teststring, args) is None
    # test file list
    assert 10 <= len(list(cli_utils.generate_filelist(RESOURCES_DIR))) <= 21


def test_sysoutput():
    """test command-line output with respect to CLI arguments"""
    testargs = ["", "--csv", "-o", "/root/forbidden/"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    filepath, destdir = cli_utils.determine_output_path(args, args.output_dir, "")
    assert len(filepath) >= 10 and filepath.endswith(".csv")
    assert destdir == "/root/forbidden/"
    # doesn't work the same on Windows
    if os.name != "nt":
        assert cli_utils.check_outputdir_status(args.output_dir) is False
    else:
        assert cli_utils.check_outputdir_status(args.output_dir) is True
    testargs = ["", "--xml", "-o", "/tmp/you-touch-my-tralala"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    assert cli_utils.check_outputdir_status(args.output_dir) is True
    # test fileslug for name
    filepath, destdir = cli_utils.determine_output_path(
        args, args.output_dir, "", new_filename="AAZZ"
    )
    assert filepath.endswith("AAZZ.xml")
    # test json output
    args2 = args
    args2.xml, args2.json = False, True
    args2 = cli.map_args(args2)
    filepath2, destdir2 = cli_utils.determine_output_path(
        args, args.output_dir, "", new_filename="AAZZ"
    )
    assert filepath2.endswith("AAZZ.json")
    assert "you-touch-my-tralala" in destdir2
    # test directory counter
    # doesn't work the same on Windows
    if os.name != "nt":
        assert cli_utils.determine_counter_dir("testdir", 0) == "testdir/1"
    else:
        assert cli_utils.determine_counter_dir("testdir", 0) == "testdir\\1"
    # test file writing
    testargs = ["", "--markdown", "-o", "/dev/null/", "-b", "/dev/null/"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    result = "DADIDA"
    cli_utils.write_result(result, args)
    args.output_dir = gettempdir()
    args.backup_dir = None
    cli_utils.write_result(result, args)
    # process with backup directory and no counter
    options = settings.args_to_extractor(args)
    assert options.format == "markdown" and options.formatting is True
    assert cli_utils.process_result("DADIDA", args, -1, options) == -1

    # with counter
    with open(
        path.join(RESOURCES_DIR, "httpbin_sample.html"), "r", encoding="utf-8"
    ) as f:
        teststring = f.read()
    assert cli_utils.process_result(teststring, args, 1, options) == 2

    # test keeping dir structure
    testargs = ["", "-i", "myinputdir/", "-o", "test/", "--keep-dirs"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    filepath, destdir = cli_utils.determine_output_path(args, "testfile.txt", "")
    assert filepath == "test/testfile.txt"
    # test hash as output file name
    assert args.keep_dirs is True
    args.keep_dirs = False
    filepath, destdir = cli_utils.determine_output_path(args, "testfile.txt", "")
    assert filepath == "test/uOHdo6wKo4IK0pkL.txt"


def test_download():
    """test page download and command-line interface"""
    assert cli_utils._define_exit_code([], 0) == 0
    assert cli_utils._define_exit_code(["a"], 1) == 126
    assert cli_utils._define_exit_code(["a"], 2) == 1

    testargs = ["", "-v"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    assert cli.examine(None, args) is None
    assert cli.examine(" ", args) is None
    assert cli.examine("0" * int(10e7), args) is None
    # url = 'https://httpbun.org/status/200'
    # teststring = fetch_url(url)
    # assert teststring is None  # too small
    # assert cli.examine(teststring, args, url) is None
    # url = 'https://httpbun.org/links/2/2'
    # teststring = fetch_url(url)
    # assert teststring is not None
    # assert cli.examine(teststring, args, url) is None
    url = "https://httpbun.com/html"
    teststring = fetch_url(url)
    assert teststring is not None
    assert cli.examine(teststring, args, url) is not None
    # test exit code for faulty URLs
    testargs = ["", "-u", "https://1234.yz/"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    with pytest.raises(SystemExit) as e:
        cli.process_args(args)
    assert e.type == SystemExit and e.value.code == 126


# @patch('trafilatura.settings.MAX_FILES_PER_DIRECTORY', 1)
def test_cli_pipeline():
    """test command-line processing pipeline"""
    # Force encoding to utf-8 for Windows in future processes spawned by multiprocessing.Pool
    os.environ["PYTHONIOENCODING"] = "utf-8"

    # test URL listing
    testargs = ["", "--list"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    assert cli_utils.url_processing_pipeline(args, UrlStore()) is False

    # test inputlist + blacklist
    testargs = ["", "-i", path.join(RESOURCES_DIR, "list-process.txt")]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    my_urls = cli_utils.load_input_urls(args)
    assert my_urls is not None and len(my_urls) == 3
    testargs = [
        "",
        "-i",
        path.join(RESOURCES_DIR, "list-process.txt"),
        "--blacklist",
        path.join(RESOURCES_DIR, "list-discard.txt"),
        "--archived",
    ]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    assert args.blacklist is not None
    # test backoff between domain requests
    url_store = add_to_compressed_dict(my_urls, args.blacklist, None, None)
    reftime = datetime.now()
    cli_utils.url_processing_pipeline(args, url_store)
    delta = (datetime.now() - reftime).total_seconds()
    assert delta > 2
    # test blacklist and empty dict
    args.blacklist = cli_utils.load_blacklist(args.blacklist)
    assert len(args.blacklist) == 3
    url_store = add_to_compressed_dict(my_urls, args.blacklist, None, None)
    cli_utils.url_processing_pipeline(args, url_store)
    # test backup
    testargs = ["", "--backup-dir", "/tmp/"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    cli_utils.archive_html("00Test", args)
    # test date-based exclusion
    testargs = ["", "--output-format", "xml", "--only-with-metadata"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    with open(
        path.join(RESOURCES_DIR, "httpbin_sample.html"), "r", encoding="utf-8"
    ) as f:
        teststring = f.read()
    assert cli.examine(teststring, args) is None
    testargs = ["", "--output-format", "xml", "--only-with-metadata", "--precision"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    with open(
        path.join(RESOURCES_DIR, "httpbin_sample.html"), "r", encoding="utf-8"
    ) as f:
        teststring = f.read()
    assert cli.examine(teststring, args) is None
    # test JSON output
    testargs = ["", "--output-format", "json", "--recall"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    with open(
        path.join(RESOURCES_DIR, "httpbin_sample.html"), "r", encoding="utf-8"
    ) as f:
        teststring = f.read()
    assert cli.examine(teststring, args) is not None
    # sitemaps: tested in --explore
    testargs = [
        "",
        "--sitemap",
        "https://sitemaps.org/sitemap.xml",
        "--list",
        "--parallel",
        "1",
    ]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    f = io.StringIO()
    with redirect_stdout(f):
        cli.process_args(args)
    assert f.getvalue().strip().endswith("https://www.sitemaps.org/zh_TW/terms.html")
    # CLI options
    testargs = ["", "--links", "--images"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    with open(
        path.join(RESOURCES_DIR, "http_sample.html"), "r", encoding="utf-8"
    ) as f:
        teststring = f.read()
    result = cli.examine(teststring, args)
    assert "[link](testlink.html)" in result and "test.jpg" in result
    # HTML format as option
    testargs = ["", "--html"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    result = cli.examine(teststring, args)
    assert result.startswith("<html") and result.endswith("</html>")


def test_file_processing():
    "Test file processing pipeline on actual directories."
    backup = settings.MAX_FILES_PER_DIRECTORY
    settings.MAX_FILES_PER_DIRECTORY = 0

    # dry-run file processing pipeline
    testargs = ["", "--parallel", "1", "--input-dir", "/dev/null"]
    with patch.object(sys, "argv", testargs):
        args = cli.parse_args(testargs)
    cli_utils.file_processing_pipeline(args)
    # file processing pipeline on resources/
    args.input_dir = RESOURCES_DIR
    cli_utils.file_processing_pipeline(args)
    # test manually
    for 
... [TRUNCATED]
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
