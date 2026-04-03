---
id: treeverse-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:23.028362
---

# KNOWLEDGE EXTRACT: treeverse
> **Extracted on:** 2026-03-30 17:55:22
> **Source:** treeverse

---

## File: `dvc.md`
```markdown
# 📦 treeverse/dvc [🔖 PENDING/APPROVE]
🔗 https://github.com/treeverse/dvc
🌐 https://dvc.org

## Meta
- **Stars:** ⭐ 15479 | **Forks:** 🍴 1289
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
🦉 Data Versioning and ML Experiments

## README (trích đầu)
```
|Banner|

`Website <https://dvc.org>`_
• `Docs <https://dvc.org/doc>`_
• `Blog <http://blog.dataversioncontrol.com>`_
• `Tutorial <https://dvc.org/doc/get-started>`_
• `Related Technologies <https://dvc.org/doc/user-guide/related-technologies>`_
• `How DVC works`_
• `VS Code Extension`_
• `Installation`_
• `Contributing`_
• `Community and Support`_

|CI| |Python Version| |Coverage| |VS Code| |DOI|

|PyPI| |PyPI Downloads| |Packages| |Brew| |Conda| |Choco| |Snap|

|

**Data Version Control** or **DVC** is a command line tool and `VS Code Extension`_ to help you develop reproducible machine learning projects:

#. **Version** your data and models.
   Store them in your cloud storage but keep their version info in your Git repo.

#. **Iterate** fast with lightweight pipelines.
   When you make changes, only run the steps impacted by those changes.

#. **Track** experiments in your local Git repo (no servers needed).

#. **Compare** any data, code, parameters, model, or performance plots.

#. **Share** experiments and automatically reproduce anyone's experiment.

Quick start
===========

    Please read our `Command Reference <https://dvc.org/doc/command-reference>`_ for a complete list.

A common CLI workflow includes:


+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Task                              | Terminal                                                                                           |
+===================================+====================================================================================================+
| Track data                        | | ``$ git add train.py params.yaml``                                                               |
|                                   | | ``$ dvc add images/``                                                                            |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Connect code and data             | | ``$ dvc stage add -n featurize -d images/ -o features/ python featurize.py``                     |
|                                   | | ``$ dvc stage add -n train -d features/ -d train.py -o model.p -M metrics.json python train.py`` |
+-----------------------------------+----------------------------------------------------------------------------------------------------+
| Make changes and experiment       | | ``$ dvc exp run -n exp-baseline``                                                                |
|                                   | | ``$ vi train.py``                                                                                |
|                                   | | ``$ dvc exp run -n exp-code-change``                                                             |
+-----------------------------------+----------------------------------------------------------
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

