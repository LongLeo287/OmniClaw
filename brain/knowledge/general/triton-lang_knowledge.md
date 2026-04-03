---
id: triton-lang-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:23.054963
---

# KNOWLEDGE EXTRACT: triton-lang
> **Extracted on:** 2026-03-30 17:55:22
> **Source:** triton-lang

---

## File: `triton.md`
```markdown
# 📦 triton-lang/triton [🔖 PENDING/APPROVE]
🔗 https://github.com/triton-lang/triton
🌐 https://triton-lang.org/

## Meta
- **Stars:** ⭐ 18776 | **Forks:** 🍴 2706
- **Language:** MLIR | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Development repository for the Triton language and compiler

## README (trích đầu)
```

| **`Documentation`** | **`Nightly Wheels`** |
|-------------------- | -------------------- |
| [![Documentation](https://github.com/triton-lang/triton/actions/workflows/documentation.yml/badge.svg)](https://triton-lang.org/) | [![Wheels](https://github.com/triton-lang/triton/actions/workflows/wheels.yml/badge.svg)](https://github.com/triton-lang/triton/actions/workflows/wheels.yml) |

# Triton Conference 2025

![Triton Banner](https://github.com/user-attachments/assets/b4b6972a-857c-417f-bf2c-f16f38a358c0)

The 3rd Triton Developer Conference took place on October 21, 2025 at the Microsoft Silicon Valley Campus in Mountain View, California.

### Conference Materials

Conference recordings and materials are now available online:

- **Conference Videos:** [YouTube Playlist](https://www.youtube.com/playlist?list=PLc_vA1r0qoiQqCdWFDUDqI90oY5EjfGuO)
- **Conference Slides:** [Google Drive Folder](https://drive.google.com/drive/folders/1KB6tD3UM1J0_eUp-F-JSlGrargLBawIr)

For previous conference materials, see:
- [2024 Conference Materials](docs/meetups/dev_conference_2024.md)
- [2023 Conference Materials](docs/meetups/dev-meetup-2023.md)

# Triton

This is the development repository of Triton, a language and compiler for writing highly efficient custom Deep-Learning primitives. The aim of Triton is to provide an open-source environment to write fast code at higher productivity than CUDA, but also with higher flexibility than other existing DSLs.

The foundations of this project are described in the following MAPL2019 publication: [Triton: An Intermediate Language and Compiler for Tiled Neural Network Computations](http://www.eecs.harvard.edu/~htk/publication/2019-mapl-tillet-kung-cox.pdf). Please consider citing this work if you use Triton!

The [official documentation](https://triton-lang.org) contains installation instructions and tutorials.  See also these third-party [Triton puzzles](https://github.com/srush/Triton-Puzzles), which can all be run using the Triton interpreter -- no GPU required.

# Quick Installation

You can install the latest stable release of Triton from pip:

```shell
pip install triton
```

Binary wheels are available for CPython 3.10-3.14.

# Install from source

```shell
git clone https://github.com/triton-lang/triton.git
cd triton

pip install -r python/requirements.txt # build-time dependencies
pip install -e .
```

Or with a virtualenv:

```shell
git clone https://github.com/triton-lang/triton.git
cd triton

python -m venv .venv --prompt triton
source .venv/bin/activate

pip install -r python/requirements.txt # build-time dependencies
pip install -e .
```

# Building with a custom LLVM

Triton uses LLVM to generate code for GPUs and CPUs.  Normally, the Triton build
downloads a prebuilt LLVM, but you can also build and use LLVM from source.

LLVM does not have a stable API, so the Triton build will not work at an
arbitrary LLVM version.

For convenience, use the following command to build LLVM and install Triton with the c
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

