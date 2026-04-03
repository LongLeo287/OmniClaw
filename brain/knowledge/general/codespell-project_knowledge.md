---
id: codespell-project-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:08.211997
---

# KNOWLEDGE EXTRACT: codespell-project
> **Extracted on:** 2026-03-30 17:34:53
> **Source:** codespell-project

---

## File: `codespell.md`
```markdown
# 📦 codespell-project/codespell [🔖 PENDING/APPROVE]
🔗 https://github.com/codespell-project/codespell


## Meta
- **Stars:** ⭐ 2342 | **Forks:** 🍴 507
- **Language:** Python | **License:** GPL-2.0
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
check code for common misspellings

## README (trích đầu)
```
codespell
=========

Fix common misspellings in text files. It's designed primarily for checking
misspelled words in source code (backslash escapes are skipped), but it can be used with other files as well.
It does not check for word membership in a complete dictionary, but instead
looks for a set of common misspellings. Therefore it should catch errors like
"adn", but it will not catch "adnasdfasdf". This also means it shouldn't
generate false-positives when you use a niche term it doesn't know about.

Useful links
------------

* `GitHub project <https://github.com/codespell-project/codespell>`_

* `Repository <https://github.com/codespell-project/codespell>`_

* `Releases <https://github.com/codespell-project/codespell/releases>`_

Requirements
------------

Python 3.9 or above.

Installation
------------

You can use ``pip`` to install codespell with e.g.:

.. code-block:: sh

    pip install codespell

Usage
-----

Below are some simple usage examples to demonstrate how the tool works.
For exhaustive usage information, please check the output of ``codespell -h``.

Run codespell in all files of the current directory:

.. code-block:: sh

    codespell

Run codespell in specific files or directories (specified via their names or glob patterns):

.. code-block:: sh

    codespell some_file some_dir/ *.ext

Some noteworthy flags:

.. code-block:: sh

    codespell -w, --write-changes

The ``-w`` flag will actually implement the changes recommended by codespell. Running without the ``-w`` flag is the same as doing a dry run. It is recommended to run this with the ``-i`` or ``--interactive`` flag.

.. code-block:: sh

    codespell -I FILE, --ignore-words=FILE

The ``-I`` flag can be used for a list of certain words to allow that are in the codespell dictionaries. The format of the file is one word per line. Invoke using: ``codespell -I path/to/file.txt`` to execute codespell referencing said list of allowed words. See `Ignoring Words`_ for more details.

.. code-block:: sh

    codespell -L word1,word2,word3,word4

The ``-L`` flag can be used to allow certain words that are comma-separated placed immediately after it.  See `Ignoring Words`_ for more details.

.. code-block:: sh

    codespell -x FILE, --exclude-file=FILE

Ignore whole lines that match those in ``FILE``.  The lines in ``FILE`` should match the to-be-excluded lines exactly.

.. code-block:: sh

    codespell -S, --skip=

Comma-separated list of files to skip. It accepts globs as well.  Examples:

* to skip .eps & .txt files, invoke ``codespell --skip="*.eps,*.txt"``

* to skip directories, invoke ``codespell --skip="./src/3rd-Party,./src/Test"``


Useful commands:

.. code-block:: sh

    codespell -d -q 3 --skip="*.po,*.ts,./src/3rdParty,./src/Test"

List all typos found except translation files and some directories.
Display them without terminal colors and with a quiet level of 3.

.. code-block:: sh

    codespell -i 3 -w

Run interactive mode level 3 and write changes to file.

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

