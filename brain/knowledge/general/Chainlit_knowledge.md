---
id: chainlit-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:00.586283
---

# KNOWLEDGE EXTRACT: Chainlit
> **Extracted on:** 2026-03-30 17:31:16
> **Source:** Chainlit

---

## File: `chainlit.md`
```markdown
# 📦 Chainlit/chainlit [🔖 PENDING/APPROVE]
🔗 https://github.com/Chainlit/chainlit
🌐 https://docs.chainlit.io

## Meta
- **Stars:** ⭐ 11812 | **Forks:** 🍴 1674
- **Language:** Python | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Build Conversational AI in minutes ⚡️

## README (trích đầu)
```
<h1 align="center">Welcome to Chainlit 👋</h1>

<p align="center">
<b>Build python production-ready conversational AI applications in minutes, not weeks ⚡️</b>

</p>
<p align="center">
   <a href="https://discord.gg/k73SQ3FyUh" target="_blank">
   <img src="https://img.shields.io/discord/1088038867602526210?logo=discord&labelColor=%20%235462eb&logoColor=%20%23f5f5f5&color=%20%235462eb"
      alt="chat on Discord"></a>
    <a href="https://twitter.com/chainlit_io" rel="nofollow"><img alt="Twitter" src="https://img.shields.io/twitter/url/https/twitter.com/chainlit_io.svg?style=social&label=Follow%20%40chainlit_io" style="max-width:100%;"></a>
    <a href="https://pypistats.org/packages/chainlit" rel="nofollow"><img alt="Downloads" src="https://img.shields.io/pypi/dm/chainlit" style="max-width:100%;"></a>
        <a href="https://github.com/chainlit/chainlit/graphs/contributors" rel="nofollow"><img alt="Contributors" src="https://img.shields.io/github/contributors/chainlit/chainlit" style="max-width:100%;"></a>
    <a href="https://github.com/Chainlit/chainlit/actions/workflows/ci.yaml" rel="nofollow"><img alt="CI" src="https://github.com/Chainlit/chainlit/actions/workflows/ci.yaml/badge.svg" style="max-width:100%;"></a>
</p>

> ⚠️ **Notice:** Chainlit is now community-maintained.
>
> As of May 1st 2025, the original Chainlit team has stepped back from active development. The project is maintained by @Chainlit/chainlit-maintainers under a formal Maintainer Agreement.
>
> Maintainers are responsible for code review, releases, and security.  
> Chainlit SAS provides no warranties on future updates.
>
> Want to help maintain? [Apply here →](https://docs.google.com/forms/d/e/1FAIpQLSf6CllNWnKBnDIoj0m-DnHU6b0dj8HYFGixKy-_qNi_rD4iNA/viewform)

<p align="center">
    <a href="https://chainlit.io"><b>Website</b></a>  •  
    <a href="https://docs.chainlit.io"><b>Documentation</b></a>  •  
    <a href="https://help.chainlit.io"><b>Chainlit Help</b></a>  •  
    <a href="https://github.com/Chainlit/cookbook"><b>Cookbook</b></a>
</p>

<p align="center">
    <a href="https://trendshift.io/repositories/6708" target="_blank"><img src="https://trendshift.io/api/badge/repositories/6708" alt="Chainlit%2Fchainlit | Trendshift" style="width: 250px; height: 45px;" width="250" height="45"/></a>
</p>

https://github.com/user-attachments/assets/b3738aba-55c0-42fa-ac00-6efd1ee0d148


## Installation

Open a terminal and run:

```sh
pip install chainlit
chainlit hello
```

If this opens the `hello app` in your browser, you're all set!

### Development version

The latest in-development version can be installed straight from GitHub with:

```sh
pip install git+https://github.com/Chainlit/chainlit.git#subdirectory=backend/
```

(Requires Node and pnpm installed on the system.)

## 🚀 Quickstart

### 🐍 Pure Python

Create a new file `demo.py` with the following code:

```python
import chainlit as cl


@cl.step(type="tool")
async def tool():
    # Fake tool
    await cl.sleep(2)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

