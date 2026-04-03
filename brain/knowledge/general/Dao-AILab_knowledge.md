---
id: dao-ailab-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:16.250771
---

# KNOWLEDGE EXTRACT: Dao-AILab
> **Extracted on:** 2026-03-30 17:35:41
> **Source:** Dao-AILab

---

## File: `flash-attention.md`
```markdown
# 📦 Dao-AILab/flash-attention [🔖 PENDING/APPROVE]
🔗 https://github.com/Dao-AILab/flash-attention


## Meta
- **Stars:** ⭐ 22992 | **Forks:** 🍴 2555
- **Language:** Python | **License:** BSD-3-Clause
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Fast and memory-efficient exact attention

## README (trích đầu)
```
# FlashAttention
This repository provides the official implementation of FlashAttention and
FlashAttention-2 from the
following papers.

**FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness**  
Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, Christopher Ré  
Paper: https://arxiv.org/abs/2205.14135  
IEEE Spectrum [article](https://spectrum.ieee.org/mlperf-rankings-2022) about our submission to the MLPerf 2.0 benchmark using FlashAttention.
![FlashAttention](assets/flashattn_banner.jpg)

**FlashAttention-2: Faster Attention with Better Parallelism and Work Partitioning**  
Tri Dao

Paper: https://tridao.me/publications/flash2/flash2.pdf

![FlashAttention-2](assets/flashattention_logo.png)


## Usage

We've been very happy to see FlashAttention being widely adopted in such a short
time after its release. This [page](https://github.com/Dao-AILab/flash-attention/blob/main/usage.md)
contains a partial list of places where FlashAttention is being used.

FlashAttention and FlashAttention-2 are free to use and modify (see LICENSE).
Please cite and credit FlashAttention if you use it.


## FlashAttention-3 beta release
FlashAttention-3 is optimized for Hopper GPUs (e.g. H100). 

Blogpost: https://tridao.me/blog/2024/flash3/

Paper: https://tridao.me/publications/flash3/flash3.pdf

![FlashAttention-3 speedup on H100 80GB SXM5 with FP16](assets/flash3_fp16_fwd.png)

This is a beta release for testing / benchmarking before we integrate that with
the rest of the repo.

Currently released:
- FP16 / BF16 forward and backward, FP8 forward

Requirements: H100 / H800 GPU, CUDA >= 12.3.

We highly recommend CUDA 12.8 for best performance.

To install:
```sh
cd hopper
python setup.py install
```
To run the test:
```sh
export PYTHONPATH=$PWD
pytest -q -s test_flash_attn.py
```
Once the package is installed, you can import it as follows:
```python
import flash_attn_interface
flash_attn_interface.flash_attn_func()
```

## FlashAttention-4 (CuTeDSL)

FlashAttention-4 is written in CuTeDSL and optimized for Hopper and Blackwell GPUs (e.g. H100, B200).

To install:
```sh
pip install flash-attn-4
```

If you're on CUDA 13, we recommend installing with the `cu13` extra for best performance:
```sh
pip install "flash-attn-4[cu13]"
```

Once installed, you can use it as follows:
```python
from flash_attn.cute import flash_attn_func

out = flash_attn_func(q, k, v, causal=True)
```

## Installation and features
**Requirements:**
- CUDA toolkit or ROCm toolkit
- PyTorch 2.2 and above.
- `packaging` Python package (`pip install packaging`)
- `psutil` Python package (`pip install psutil`)
- `ninja` Python package (`pip install ninja`) *
- Linux. Might work for Windows starting v2.3.2 (we've seen a few positive [reports](https://github.com/Dao-AILab/flash-attention/issues/595)) but Windows compilation still requires more testing. If you have ideas on how to set up prebuilt CUDA wheels for Windows, please reach out via Github issue.

\* Make sure that `ninj
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

