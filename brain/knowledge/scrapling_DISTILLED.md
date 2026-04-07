---
id: scrapling
type: knowledge
owner: OA_Triage
---
# scrapling
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
<!-- mcp-name: io.github.D4Vinci/Scrapling -->

<h1 align="center">
    <a href="https://scrapling.readthedocs.io">
        <picture>
          <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/docs/assets/cover_dark.svg?sanitize=true">
          <img alt="Scrapling Poster" src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/docs/assets/cover_light.svg?sanitize=true">
        </picture>
    </a>
    <br>
    <small>Effortless Web Scraping for the Modern Web</small>
</h1>

<p align="center">
    <a href="https://trendshift.io/repositories/14244" target="_blank"><img src="https://trendshift.io/api/badge/repositories/14244" alt="D4Vinci%2FScrapling | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
    <br/>
    <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_AR.md">العربيه</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_ES.md">Español</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_FR.md">Français</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_DE.md">Deutsch</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_CN.md">简体中文</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_JP.md">日本語</a> |  <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_RU.md">Русский</a> | <a href="https://github.com/D4Vinci/Scrapling/blob/main/docs/README_KR.md">한국어</a>
    <br/>
    <a href="https://github.com/D4Vinci/Scrapling/actions/workflows/tests.yml" alt="Tests">
        <img alt="Tests" src="https://github.com/D4Vinci/Scrapling/actions/workflows/tests.yml/badge.svg"></a>
    <a href="https://badge.fury.io/py/Scrapling" alt="PyPI version">
        <img alt="PyPI version" src="https://badge.fury.io/py/Scrapling.svg"></a>
    <a href="https://clickpy.clickhouse.com/dashboard/scrapling" rel="nofollow"><img src="https://img.shields.io/pypi/dm/scrapling" alt="PyPI package downloads"></a>
    <a href="https://github.com/D4Vinci/Scrapling/tree/main/agent-skill" alt="AI Agent Skill directory">
        <img alt="Static Badge" src="https://img.shields.io/badge/Skill-black?style=flat&label=Agent&link=https%3A%2F%2Fgithub.com%2FD4Vinci%2FScrapling%2Ftree%2Fmain%2Fagent-skill"></a>
    <a href="https://clawhub.ai/D4Vinci/scrapling-official" alt="OpenClaw Skill">
        <img alt="OpenClaw Skill" src="https://img.shields.io/badge/Clawhub-darkred?style=flat&label=OpenClaw&link=https%3A%2F%2Fclawhub.ai%2FD4Vinci%2Fscrapling-official"></a>
    <br/>
    <a href="https://discord.gg/EMgGbDceNQ" alt="Discord" target="_blank">
      <img alt="Discord" src="https://img.shields.io/discord/1360786381042880532?style=social&logo=discord&link=https%3A%2F%2Fdiscord.gg%2FEMgGbDceNQ">
    </a>
    <a href="https://x.com/Scrapling_dev" alt="X (formerly Twitter)">
      <img alt="X (formerly Twitter) Follow" src="https://img.shields.io/twitter/follow/Scrapling_dev?style=social&logo=x&link=https%3A%2F%2Fx.com%2FScrapling_dev">
    </a>
    <br/>
    <a href="https://pypi.org/project/scrapling/" alt="Supported Python versions">
        <img alt="Supported Python versions" src="https://img.shields.io/pypi/pyversions/scrapling.svg"></a>
</p>

<p align="center">
    <a href="https://scrapling.readthedocs.io/en/latest/parsing/selection.html"><strong>Selection methods</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/fetching/choosing.html"><strong>Fetchers</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/spiders/architecture.html"><strong>Spiders</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/spiders/proxy-blocking.html"><strong>Proxy Rotation</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/cli/overview.html"><strong>CLI</strong></a>
    &middot;
    <a href="https://scrapling.readthedocs.io/en/latest/ai/mcp-server.html"><strong>MCP</strong></a>
</p>

Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl.

Its parser learns from website changes and automatically relocates your elements when pages update. Its fetchers bypass anti-bot systems like Cloudflare Turnstile out of the box. And its spider framework lets you scale up to concurrent, multi-session crawls with pause/resume and automatic proxy rotation - all in a few lines of Python. One library, zero compromises.

Blazing fast crawls with real-time stats and streaming. Built by Web Scrapers for Web Scrapers and regular users, there's something for everyone.

```python
from scrapling.fetchers import Fetcher, AsyncFetcher, StealthyFetcher, DynamicFetcher
StealthyFetcher.adaptive = True
p = StealthyFetcher.fetch('https://example.com', headless=True, network_idle=True)  # Fetch website under the radar!
products = p.css('.product', auto_save=True)                                        # Scrape data that survives website design changes!
products = p.css('.product', adaptive=True)                                         # Later, if the website structure changes, pass `adaptive=True` to find them!
```
Or scale up to full crawls
```python
from scrapling.spiders import Spider, Response

class MySpider(Spider):
  name = "demo"
  start_urls = ["https://example.com/"]

  async def parse(self, response: Response):
      for item in response.css('.product'):
          yield {"title": item.css('h2::text').get()}

MySpider().start()
```

<p align="center">
    <a href="https://dataimpulse.com/?utm_source=scrapling&utm_medium=banner&utm_campaign=scrapling" target="_blank" style="display:flex; justify-content:center; padding:4px 0;">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/DataImpulse.png" alt="At DataImpulse, we specialize in developing custom proxy services for your business. Make requests from anywhere, collect data, and enjoy fast connections with our premium proxies." style="max-height:60px;">
    </a>
</p>

# Platinum Sponsors
<table>
  <tr>
    <td width="200">
      <a href="https://hypersolutions.co/?utm_source=github&utm_medium=readme&utm_campaign=scrapling" target="_blank" title="Bot Protection Bypass API for Akamai, DataDome, Incapsula & Kasada">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/HyperSolutions.png">
      </a>
    </td>
    <td> Scrapling handles Cloudflare Turnstile. For enterprise-grade protection, <a href="https://hypersolutions.co?utm_source=github&utm_medium=readme&utm_campaign=scrapling">
        <b>Hyper Solutions</b>
      </a> provides API endpoints that generate valid antibot tokens for <b>Akamai</b>, <b>DataDome</b>, <b>Kasada</b>, and <b>Incapsula</b>. Simple API calls, no browser automation required. </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://birdproxies.com/t/scrapling" target="_blank" title="At Bird Proxies, we eliminate your pains such as banned IPs, geo restriction, and high costs so you can focus on your work.">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/BirdProxies.jpg">
      </a>
    </td>
    <td>Hey, we built <a href="https://birdproxies.com/t/scrapling">
        <b>BirdProxies</b>
      </a> because proxies shouldn't be complicated or overpriced. Fast residential and ISP proxies in 195+ locations, fair pricing, and real support. <br />
      <b>Try our FlappyBird game on the landing page for free data!</b>
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://evomi.com?utm_source=github&utm_medium=banner&utm_campaign=d4vinci-scrapling" target="_blank" title="Evomi is your Swiss Quality Proxy Provider, starting at $0.49/GB">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/evomi.png">
      </a>
    </td>
    <td>
      <a href="https://evomi.com?utm_source=github&utm_medium=banner&utm_campaign=d4vinci-scrapling">
        <b>Evomi</b>
      </a>: residential proxies from $0.49/GB. Scraping browser with fully spoofed Chromium, residential IPs, auto CAPTCHA solving, and anti-bot bypass. </br>
      <b>Scraper API for hassle-free results. MCP and N8N integrations are available.</b>
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://tikhub.io/?utm_source=github.com/D4Vinci/Scrapling&utm_medium=marketing_social&utm_campaign=retargeting&utm_content=carousel_ad" target="_blank" title="Unlock the Power of Social Media Data & AI">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/TikHub.jpg">
      </a>
    </td>
    <td>
      <a href="https://tikhub.io/?utm_source=github.com/D4Vinci/Scrapling&utm_medium=marketing_social&utm_campaign=retargeting&utm_content=carousel_ad" target="_blank">TikHub.io</a> provides 900+ stable APIs across 16+ platforms including TikTok, X, YouTube & Instagram, with 40M+ datasets. <br /> Also offers <a href="https://ai.tikhub.io/?ref=KarimShoair" target="_blank">DISCOUNTED AI models</a> - Claude, GPT, GEMINI & more up to 71% off.
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://www.nsocks.com/?keyword=2p67aivg" target="_blank" title="Scalable Web Data Access for AI Applications">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/nsocks.png">
      </a>
    </td>
    <td>
    <a href="https://www.nsocks.com/?keyword=2p67aivg" target="_blank">Nsocks</a> provides fast Residential and ISP proxies for developers and scrapers. Global IP coverage, high anonymity, smart rotation, and reliable performance for automation and data extraction. Use <a href="https://www.xcrawl.com/?keyword=2p67aivg" target="_blank">Xcrawl</a> to simplify large-scale web crawling.
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://petrosky.io/d4vinci" target="_blank" title="PetroSky delivers cutting-edge VPS hosting.">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/petrosky.png">
      </a>
    </td>
    <td>
    Close your laptop. Your scrapers keep running. <br />
    <a href="https://petrosky.io/d4vinci" target="_blank">PetroSky VPS</a> - cloud servers built for nonstop automation. Windows and Linux machines with full control. From €6.99/mo.
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://substack.thewebscraping.club/p/scrapling-hands-on-guide?utm_source=github&utm_medium=repo&utm_campaign=scrapling" target="_blank" title="The #1 newsletter dedicated to Web Scraping">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/TWSC.png">
      </a>
    </td>
    <td>
    Read a full review of <a href="https://substack.thewebscraping.club/p/scrapling-hands-on-guide?utm_source=github&utm_medium=repo&utm_campaign=scrapling" target="_blank">Scrapling on The Web Scraping Club</a> (Nov 2025), the #1 newsletter dedicated to Web Scraping.
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="https://proxy-seller.com/?partner=CU9CAA5TBYFFT2" target="_blank" title="Proxy-Seller provides reliable proxy infrastructure for Web Scraping">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/ProxySeller.png">
      </a>
    </td>
    <td>
    <a href="https://proxy-seller.com/?partner=CU9CAA5TBYFFT2" target="_blank">Proxy-Seller</a> provides reliable proxy infrastructure for web scraping, offering IPv4, IPv6, ISP, Residential, and Mobile proxies with stable performance, broad geo coverage, and flexible plans for business-scale data collection.
    </td>
  </tr>
  <tr>
    <td width="200">
      <a href="http://mangoproxy.com/?utm_source=D4Vinci&utm_medium=GitHub&utm_campaign=D4Vinci" target="_blank" title="Proxies You Can Rely On: Residential, Server, and Mobile">
        <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/MangoProxy.png">
      </a>
    </td>
    <td>
    <a href="http://mangoproxy.com/?utm_source=D4Vinci&utm_medium=GitHub&utm_campaign=D4Vinci" target="_blank">Stable proxies</a> for scraping, automation, and multi-accounting. Clean IPs, fast response, and reliable performance under load. Built for scalable workflows.
    </td>
  </tr>
</table>

<i><sub>Do you want to show your ad here? Click [here](https://github.com/sponsors/D4Vinci/sponsorships?tier_id=586646)</sub></i>
# Sponsors 

<!-- sponsors -->


<a href="https://serpapi.com/?utm_source=scrapling" target="_blank" title="Scrape Google and other search engines with SerpApi"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/SerpApi.png"></a>
<a href="https://visit.decodo.com/Dy6W0b" target="_blank" title="Try the Most Efficient Residential Proxies for Free"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/decodo.png"></a>
<a href="https://hasdata.com/?utm_source=github&utm_medium=banner&utm_campaign=D4Vinci" target="_blank" title="The web scraping service that actually beats anti-bot systems!"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/hasdata.png"></a>
<a href="https://proxyempire.io/?ref=scrapling&utm_source=scrapling" target="_blank" title="Collect The Data Your Project Needs with the Best Residential Proxies"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/ProxyEmpire.png"></a>
<a href="https://www.webshare.io/?referral_code=48r2m2cd5uz1" target="_blank" title="The Most Reliable Proxy with Unparalleled Performance"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/webshare.png"></a>
<a href="https://browser.cash/?utm_source=D4Vinci&utm_medium=referral" target="_blank" title="Browser Automation & AI Browser Agent Platform"><img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/browserCash.png"></a>

<!-- /sponsors -->

<i><sub>Do you want to show your ad here? Click [here](https://github.com/sponsors/D4Vinci) and choose the tier that suites you!</sub></i>

---

## Key Features

### Spiders - A Full Crawling Framework
- 🕷️ **Scrapy-like Spider API**: Define spiders with `start_urls`, async `parse` callbacks, and `Request`/`Response` objects.
- ⚡ **Concurrent Crawling**: Configurable concurrency limits, per-domain throttling, and download delays.
- 🔄 **Multi-Session Support**: Unified interface for HTTP requests, and stealthy headless browsers in a single spider - route requests to different sessions by ID.
- 💾 **Pause & Resume**: Checkpoint-based crawl persistence. Press Ctrl+C for a graceful shutdown; restart to resume from where you left off.
- 📡 **Streaming Mode**: Stream scraped items as they arrive via `async for item in spider.stream()` with real-time stats - ideal for UI, pipelines, and long-running crawls.
- 🛡️ **Blocked Request Detection**: Automatic detection and retry of blocked requests with customizable logic.
- 📦 **Built-in Export**: Export results through hooks and your own pipeline or the built-in
... [TRUNCATED]
```

### File: agent-skill\README.md
```md
# Scrapling Agent Skill

The skill aligns with the [AgentSkill](https://agentskills.io/specification) specification, so it will be readable by [OpenClaw](https://github.com/openclaw/openclaw), [Claude Code](https://claude.com/product/claude-code), and other agentic tools. It encapsulates almost all of the documentation website's content in Markdown, so the agent doesn't have to guess anything.

It can be used to answer almost 90% of any questions you would have about scrapling. We tested it on [OpenClaw](https://github.com/openclaw/openclaw) and [Claude Code](https://claude.com/product/claude-code), but please open a [ticket](https://github.com/D4Vinci/Scrapling/issues/new/choose) if you faced any issues or use our [Discord server](https://discord.gg/EMgGbDceNQ).

## Installation

You can use this [direct URL](https://github.com/D4Vinci/Scrapling/raw/refs/heads/main/agent-skill/Scrapling-Skill.zip) to download the ZIP file of the skill directly. We will try to update this page with all available methods.

### Clawhub
If you are an [OpenClaw](https://github.com/openclaw/openclaw) and [Claude Code](https://claude.com/product/claude-code), you can install the skill using [Clawhub](https://docs.openclaw.ai/tools/clawhub) directly:
```bash
clawhub install scrapling-official
```

Or go to the [Clawhub](https://docs.openclaw.ai/tools/clawhub) page from [here](https://clawhub.ai/D4Vinci/scrapling-official).
```

### File: docs\requirements.txt
```txt
zensical>=0.0.30
mkdocstrings>=1.0.3
mkdocstrings-python>=2.0.3
griffe-inherited-docstrings>=1.1.3
griffe-runtime-objects>=0.3.1
griffe-sphinx>=0.2.1
black>=26.1.0
pngquant
```

### File: tests\requirements.txt
```txt
pytest>=2.8.0,<9
pytest-cov
playwright==1.58.0
werkzeug<3.0.0
pytest-httpbin==2.1.0
pytest-asyncio
httpbin~=0.10.0
pytest-xdist

```

### File: .pre-commit-config.yaml
```yaml
repos:
- repo: https://github.com/PyCQA/bandit
  rev: 1.9.0
  hooks:
  - id: bandit
    args: [-r, -c, .bandit.yml]
- repo: https://github.com/astral-sh/ruff-pre-commit
  # Ruff version.
  rev: v0.14.5
  hooks:
    # Run the linter.
    - id: ruff
      args: [ --fix ]
    # Run the formatter.
    - id: ruff-format
- repo: https://github.com/netromdk/vermin
  rev: v1.7.0
  hooks:
  - id: vermin
    args: ['-t=3.10-', '--violations', '--eval-annotations', '--no-tips']

```

### File: .readthedocs.yaml
```yaml
# See https://docs.readthedocs.com/platform/stable/intro/zensical.html for details
# Example: https://github.com/readthedocs/test-builds/tree/zensical

version: 2

build:
  os: ubuntu-24.04
  apt_packages:
    - pngquant
  tools:
    python: "3.13"
  jobs:
    install:
      - pip install -r docs/requirements.txt
      - pip install ".[all]"
    build:
      html:
        - zensical build
    post_build:
      - mkdir -p $READTHEDOCS_OUTPUT/html/
      - cp --recursive site/* $READTHEDOCS_OUTPUT/html/

```

### File: benchmarks.py
```py
import functools
import time
import timeit
from statistics import mean

import requests
from autoscraper import AutoScraper
from bs4 import BeautifulSoup
from lxml import etree, html
from mechanicalsoup import StatefulBrowser
from parsel import Selector
from pyquery import PyQuery as pq
from selectolax.parser import HTMLParser

from scrapling import Selector as ScraplingSelector

large_html = (
    "<html><body>" + '<div class="item">' * 5000 + "</div>" * 5000 + "</body></html>"
)


def benchmark(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        benchmark_name = func.__name__.replace("test_", "").replace("_", " ")
        print(f"-> {benchmark_name}", end=" ", flush=True)
        # Warm-up phase
        timeit.repeat(
            lambda: func(*args, **kwargs), number=2, repeat=2, globals=globals()
        )
        # Measure time (1 run, repeat 100 times, take average)
        times = timeit.repeat(
            lambda: func(*args, **kwargs),
            number=1,
            repeat=100,
            globals=globals(),
            timer=time.process_time,
        )
        min_time = round(mean(times) * 1000, 2)  # Convert to milliseconds
        print(f"average execution time: {min_time} ms")
        return min_time

    return wrapper


@benchmark
def test_lxml():
    return [
        e.text
        for e in etree.fromstring(
            large_html,
            # Scrapling and Parsel use the same parser inside, so this is just to make it fair
            parser=html.HTMLParser(recover=True, huge_tree=True),
        ).cssselect(".item")
    ]


@benchmark
def test_bs4_lxml():
    return [e.text for e in BeautifulSoup(large_html, "lxml").select(".item")]


@benchmark
def test_bs4_html5lib():
    return [e.text for e in BeautifulSoup(large_html, "html5lib").select(".item")]


@benchmark
def test_pyquery():
    return [e.text() for e in pq(large_html)(".item").items()]


@benchmark
def test_scrapling():
    # No need to do `.extract()` like parsel to extract text
    # Also, this is faster than `[t.text for t in Selector(large_html, adaptive=False).css('.item')]`
    # for obvious reasons, of course.
    return ScraplingSelector(large_html, adaptive=False).css(".item::text").getall()


@benchmark
def test_parsel():
    return Selector(text=large_html).css(".item::text").extract()


@benchmark
def test_mechanicalsoup():
    browser = StatefulBrowser()
    browser.open_fake_page(large_html)
    return [e.text for e in browser.page.select(".item")]


@benchmark
def test_selectolax():
    return [node.text() for node in HTMLParser(large_html).css(".item")]


def display(results):
    # Sort and display results
    sorted_results = sorted(results.items(), key=lambda x: x[1])  # Sort by time
    scrapling_time = results["Scrapling"]
    print("\nRanked Results (fastest to slowest):")
    print(f" i. {'Library tested':<18} | {'avg. time (ms)':<15} | vs Scrapling")
    print("-" * 50)
    for i, (test_name, test_time) in enumerate(sorted_results, 1):
        compare = round(test_time / scrapling_time, 3)
        print(f" {i}. {test_name:<18} | {str(test_time):<15} | {compare}")


@benchmark
def test_scrapling_text(request_html):
    return ScraplingSelector(request_html, adaptive=False).find_by_text("Tipping the Velvet", first_match=True, clean_match=False).find_similar(ignore_attributes=["title"])


@benchmark
def test_autoscraper(request_html):
    # autoscraper by default returns elements text
    return AutoScraper().build(html=request_html, wanted_list=["Tipping the Velvet"])


if __name__ == "__main__":
    print(
        " Benchmark: Speed of parsing and retrieving the text content of 5000 nested elements \n"
    )
    results1 = {
        "Raw Lxml": test_lxml(),
        "Parsel/Scrapy": test_parsel(),
        "Scrapling": test_scrapling(),
        "Selectolax": test_selectolax(),
        "PyQuery": test_pyquery(),
        "BS4 with Lxml": test_bs4_lxml(),
        "MechanicalSoup": test_mechanicalsoup(),
        "BS4 with html5lib": test_bs4_html5lib(),
    }

    display(results1)
    print("\n" + "=" * 25)
    req = requests.get("https://books.toscrape.com/index.html")
    print(
        " Benchmark: Speed of searching for an element by text content, and retrieving the text of similar elements\n"
    )
    results2 = {
        "Scrapling": test_scrapling_text(req.text),
        "AutoScraper": test_autoscraper(req.text),
    }
    display(results2)

```

### File: cleanup.py
```py
import shutil
from pathlib import Path


# Clean up after installing for local development
def clean():
    # Get the current directory
    base_dir = Path.cwd()

    # Directories and patterns to clean
    cleanup_patterns = [
        "build",
        "dist",
        "*.egg-info",
        "__pycache__",
        ".eggs",
        ".pytest_cache",
    ]

    # Clean directories
    for pattern in cleanup_patterns:
        for path in base_dir.glob(pattern):
            try:
                if path.is_dir():
                    shutil.rmtree(path)
                else:
                    path.unlink()
                print(f"Removed: {path}")
            except Exception as e:
                print(f"Could not remove {path}: {e}")

    # Remove compiled Python files
    for path in base_dir.rglob("*.py[co]"):
        try:
            path.unlink()
            print(f"Removed compiled file: {path}")
        except Exception as e:
            print(f"Could not remove {path}: {e}")


if __name__ == "__main__":
    clean()

```

### File: CODE_OF_CONDUCT.md
```md
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
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
reported to the community leaders responsible for enforcement at
karim.shoair@pm.me.
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

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

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
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
https://www.contributor-covenant.org/version/2/0/code_of_conduct.html.

Community Impact Guidelines were inspired by [Mozilla's code of conduct
enforcement ladder](https://github.com/mozilla/diversity).

[homepage]: https://www.contributor-covenant.org

For answers to common questions about this code of conduct, see the FAQ at
https://www.contributor-covenant.org/faq. Translations are available at
https://www.contributor-covenant.org/translations.

```

### File: CONTRIBUTING.md
```md
# Contributing to Scrapling

Thank you for your interest in contributing to Scrapling! 

Everybody is invited and welcome to contribute to Scrapling. 

Minor changes are more likely to be included promptly. Adding unit tests for new features or test cases for bugs you've fixed helps us ensure that the Pull Request (PR) is acceptable.

There are many ways to contribute to Scrapling. Here are some of them:

- Report bugs and request features using the [GitHub issues](https://github.com/D4Vinci/Scrapling/issues). Please follow the issue template to help us resolve your issue quickly.
- Blog about Scrapling. Tell the world how you’re using Scrapling. This will help newcomers with more examples and increase the Scrapling project's visibility.
- Join the [Discord community](https://discord.gg/EMgGbDceNQ) and share your ideas on how to improve Scrapling. We’re always open to suggestions.
- If you are not a developer, perhaps you would like to help with translating the [documentation](https://github.com/D4Vinci/Scrapling/tree/docs)?

## Making a Pull Request
To ensure that your PR gets accepted, please make sure that your PR is based on the latest changes from the dev branch and that it satisfies the following requirements:

- **The PR must be made against the [**dev**](https://github.com/D4Vinci/Scrapling/tree/dev) branch of Scrapling. Any PR made against the main branch will be rejected.**
- **The code should be passing all available tests. We use tox with GitHub's CI to run the current tests on all supported Python versions for every code-related commit.**
- **The code should be passing all code quality checks like `mypy` and `pyright`. We are using GitHub's CI to enforce code style checks as well.**
- **Make your changes, keep the code clean with an explanation of any part that might be vague, and remember to create a separate virtual environment for this project.**
- If you are adding a new feature, please add tests for it.
- If you are fixing a bug, please add code with the PR that reproduces the bug.
- Please follow the rules and coding style rules we explain below.


## Finding work

If you have decided to make a contribution to Scrapling, but you do not know what to contribute, here are some ways to find pending work:

- Check out the [contribution](https://github.com/D4Vinci/Scrapling/contribute) GitHub page, which lists open issues tagged as `good first issue`. These issues provide a good starting point.
- There are also the [help wanted](https://github.com/D4Vinci/Scrapling/issues?q=is%3Aissue%20label%3A%22help%20wanted%22%20state%3Aopen) issues, but know that some may require familiarity with the Scrapling code base first. You can also target any other issue, provided it is not tagged as `invalid`, `wontfix`, or similar tags.
- If you enjoy writing automated tests, you can work on increasing our test coverage. Currently, the test coverage is around 90–92%.
- Join the [Discord community](https://discord.gg/EMgGbDceNQ) and ask questions in the `#help` channel.

## Coding style
Please follow these coding conventions as we do when writing code for Scrapling:
- We use [pre-commit](https://pre-commit.com/) to automatically address simple code issues before every commit, so please install it and run `pre-commit install` to set it up. This will install hooks to run [ruff](https://docs.astral.sh/ruff/), [bandit](https://github.com/PyCQA/bandit), and [vermin](https://github.com/netromdk/vermin) on every commit. We are currently using a workflow to automatically run these tools on every PR, so if your code doesn't pass these checks, the PR will be rejected.
- We use type hints for better code clarity and [pyright](https://github.com/microsoft/pyright)/[mypy](https://github.com/python/mypy) for static type checking. If your code isn't acceptable by those tools, your PR won't pass the code quality rule.
- We use the conventional commit messages format as [here](https://gist.github.com/qoomon/5dfcdf8eec66a051ecd85625518cfd13#types), so for example, we use the following prefixes for commit messages:
   
   | Prefix      | When to use it           |
   |-------------|--------------------------|
   | `feat:`     | New feature added        |
   | `fix:`      | Bug fix                  |
   | `docs:`     | Documentation change/add |
   | `test:`     | Tests                    |
   | `refactor:` | Code refactoring         |
   | `chore:`    | Maintenance tasks        |
    
    Then include the details of the change in the commit message body/description.

   Example:
   ```
   feat: add `adaptive` for similar elements
   
   - Added find_similar() method
   - Implemented pattern matching
   - Added tests and documentation
   ```

> Please don’t put your name in the code you contribute; git provides enough metadata to identify the author of the code.

## Development

### Getting started

1. Fork the repository and clone your fork:
   ```bash
   git clone https://github.com/<your-username>/Scrapling.git
   cd Scrapling
   git checkout dev
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[all]"
   pip install -r tests/requirements.txt
   ```

3. Install browser dependencies:
   ```bash
   scrapling install
   ```

4. Set up pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

### Tips

Setting the scrapling logging level to `debug` makes it easier to know what's happening in the background.
```python
import logging
logging.getLogger("scrapling").setLevel(logging.DEBUG)
```
Bonus: You can install the beta of the upcoming update from the dev branch as follows
```commandline
pip3 install git+https://github.com/D4Vinci/Scrapling.git@dev
```

## Tests
Scrapling includes a comprehensive test suite that can be executed with pytest. However, first, you need to install all libraries and `pytest-plugins` listed in `tests/requirements.txt`. Then, running the tests will result in an output like this:
   ```bash
   $ pytest tests -n auto
   =============================== test session starts ===============================
   platform darwin -- Python 3.13.8, pytest-8.4.2, pluggy-1.6.0 -- /Users/<redacted>/.venv/bin/python3.13
   cachedir: .pytest_cache
   rootdir: /Users/<redacted>/scrapling
   configfile: pytest.ini
   plugins: asyncio-1.2.0, anyio-4.11.0, xdist-3.8.0, httpbin-2.1.0, cov-7.0.0
   asyncio: mode=Mode.STRICT, asyncio_default_fixture_loop_scope=function, asyncio_default_test_loop_scope=function
   10 workers [515 items]
   scheduling tests via LoadScheduling

   ...<shortened>...

   =============================== 271 passed in 52.68s ==============================
   ```
Here, `-n auto` runs tests in parallel across multiple processes to increase speed.

**Note:** You may need to run browser tests sequentially (`DynamicFetcher`/`StealthyFetcher`) to avoid conflicts. To run non-browser tests in parallel and browser tests separately:
```bash
# Non-browser tests (parallel)
pytest tests/ -k "not (DynamicFetcher or StealthyFetcher)" -n auto

# Browser tests (sequential)
pytest tests/ -k "DynamicFetcher or StealthyFetcher"
```

Bonus: You can also see the test coverage with the `pytest` plugin below
```bash
pytest --cov=scrapling tests/
```

## Building Documentation
Documentation is built using [Zensical](https://zensical.org/). You can build it locally using the following commands:
```bash
pip install zensical
pip install -r docs/requirements.txt
zensical build --clean  # Build the static site
zensical serve          # Local preview
```

```

### File: ROADMAP.md
```md
## TODOs
- [x] Add more tests and increase the code coverage.
- [x] Structure the tests folder in a better way.
- [x] Add more documentation.
- [x] Add the browsing ability.
- [x] Create detailed documentation for the 'readthedocs' website, preferably add GitHub action for deploying it.
- [ ] Create a Scrapy plugin/decorator to make it replace parsel in the response argument when needed.
- [x] Need to add more functionality to `AttributesHandler` and more navigation functions to `Selector` object (ex: functions similar to map, filter, and reduce functions but here pass it to the element and the function is executed on children, siblings, next elements, etc...)
- [x] Add `.filter` method to `Selectors` object and other similar methods.
- [ ] Add functionality to automatically detect pagination URLs
- [ ] Add the ability to auto-detect schemas in pages and manipulate them.
- [ ] Add `analyzer` ability that tries to learn about the page through meta-elements and return what it learned
- [ ] Add the ability to generate a regex from a group of elements (Like for all href attributes)
- 
```

### File: server.json
```json
{
  "$schema": "https://static.modelcontextprotocol.io/schemas/2025-12-11/server.schema.json",
  "name": "io.github.D4Vinci/Scrapling",
  "title": "Scrapling MCP Server",
  "description": "Web scraping with stealth HTTP, real browsers, and Cloudflare bypass. CSS selectors supported.",
  "websiteUrl": "https://scrapling.readthedocs.io/en/latest/ai/mcp-server.html",
  "repository": {
    "url": "https://github.com/D4Vinci/Scrapling",
    "source": "github"
  },
  "icons": [
    {
      "src": "https://raw.githubusercontent.com/D4Vinci/Scrapling/main/docs/assets/logo.png",
      "mimeType": "image/png"
    }
  ],
  "version": "0.4.3",
  "packages": [
    {
      "registryType": "pypi",
      "identifier": "scrapling",
      "version": "0.4.3",
      "runtimeHint": "uvx",
      "packageArguments": [
        {
          "type": "positional",
          "valueHint": "mcp",
          "isFixed": true
        }
      ],
      "transport": {
        "type": "stdio"
      }
    },
    {
      "registryType": "oci",
      "identifier": "ghcr.io/d4vinci/scrapling",
      "packageArguments": [
        {
          "type": "positional",
          "valueHint": "mcp",
          "isFixed": true
        }
      ],
      "transport": {
        "type": "stdio"
      }
    }
  ]
}
```

### File: .github\PULL_REQUEST_TEMPLATE.md
```md
<!--
  You are amazing! Thanks for contributing to Scrapling!
  Please, DO NOT DELETE ANY TEXT from this template! (unless instructed).
-->

## Proposed change
<!--
  Describe the big picture of your changes here to communicate to the maintainers why we should accept this pull request.
  If it fixes a bug or resolves a feature request, be sure to link to that issue in the additional information section.
-->


### Type of change:
<!--
  What type of change does your PR introduce to Scrapling?
  NOTE: Please, check at least 1 box!
  If your PR requires multiple boxes to be checked, you'll most likely need to
  split it into multiple PRs. This makes things easier and faster to code review.
-->



- [ ] Dependency upgrade
- [ ] Bugfix (non-breaking change which fixes an issue)
- [ ] New integration (thank you!)
- [ ] New feature (which adds functionality to an existing integration)
- [ ] Deprecation (breaking change to happen in the future)
- [ ] Breaking change (fix/feature causing existing functionality to break)
- [ ] Code quality improvements to existing code or addition of tests
- [ ] Add or change doctests? -- Note: Please avoid changing both code and tests in a single pull request.
- [ ] Documentation change?

### Additional information
<!--
  Details are important and help maintainers processing your PR.
  Please be sure to fill out additional details, if applicable.
-->

- This PR fixes or closes an issue: fixes #
- This PR is related to an issue: #
- Link to documentation pull request: **

### Checklist:
* [ ] I have read [CONTRIBUTING.md](https://github.com/D4Vinci/Scrapling/blob/main/CONTRIBUTING.md).
* [ ] This pull request is all my own work -- I have not plagiarized.
* [ ] I know that pull requests will not be merged if they fail the automated tests.
* [ ] All new Python files are placed inside an existing directory.
* [ ] All filenames are in all lowercase characters with no spaces or dashes.
* [ ] All functions and variable names follow Python naming conventions.
* [ ] All function parameters and return values are annotated with Python [type hints](https://docs.python.org/3/library/typing.html).
* [ ] All functions have doc-strings.

```

### File: docs\benchmarks.md
```md
# Performance Benchmarks

Scrapling isn't just powerful - it's also blazing fast. The following benchmarks compare Scrapling's parser with the latest versions of other popular libraries.

### Text Extraction Speed Test (5000 nested elements)

| # |      Library      | Time (ms) | vs Scrapling | 
|---|:-----------------:|:---------:|:------------:|
| 1 |     Scrapling     |   2.02    |     1.0x     |
| 2 |   Parsel/Scrapy   |   2.04    |     1.01     |
| 3 |     Raw Lxml      |   2.54    |    1.257     |
| 4 |      PyQuery      |   24.17   |     ~12x     |
| 5 |    Selectolax     |   82.63   |     ~41x     |
| 6 |  MechanicalSoup   |  1549.71  |   ~767.1x    |
| 7 |   BS4 with Lxml   |  1584.31  |   ~784.3x    |
| 8 | BS4 with html5lib |  3391.91  |   ~1679.1x   |


### Element Similarity & Text Search Performance

Scrapling's adaptive element finding capabilities significantly outperform alternatives:

| Library     | Time (ms) | vs Scrapling |
|-------------|:---------:|:------------:|
| Scrapling   |   2.39    |     1.0x     |
| AutoScraper |   12.45   |    5.209x    |

> All benchmarks represent averages of 100+ runs. See [benchmarks.py](https://github.com/D4Vinci/Scrapling/blob/main/benchmarks.py) for methodology.

```

### File: docs\donate.md
```md
I've been creating all of these projects in my spare time and have invested considerable resources & effort in providing them to the community for free. By becoming a sponsor, you'd be directly funding my coffee reserves, helping me fulfill my responsibilities, and enabling me to continuously update existing projects and potentially create new ones.

You can sponsor me directly through the [GitHub Sponsors program](https://github.com/sponsors/D4Vinci) or [Buy Me a Coffee](https://buymeacoffee.com/d4vinci).

Thank you, stay curious, and hack the planet! ❤️

## Advertisement
If you are looking to **advertise** your business to our target audience, check out the [available tiers](https://github.com/sponsors/D4Vinci):

### 1. [The Silver tier](https://github.com/sponsors/D4Vinci/sponsorships?tier_id=435495) ($100/month)
Perks:

1. Your logo will be featured at [the top of Scrapling's project page](https://github.com/D4Vinci/Scrapling?tab=readme-ov-file#sponsors).
2. The same logo will be featured at [the top of Scrapling's PyPI page](https://pypi.org/project/scrapling/) and [the top of Docker's image page](https://hub.docker.com/r/pyd4vinci/scrapling), the same way it was placed on the project's page.

### 2. [The Gold tier](https://github.com/sponsors/D4Vinci/sponsorships?tier_id=591422) ($200/month)
Perks:

1. Your logo will be featured at [the top of Scrapling's project page](https://github.com/D4Vinci/Scrapling?tab=readme-ov-file#sponsors).
2. The same logo will be featured at [the top of Scrapling's PyPI page](https://pypi.org/project/scrapling/) and [the top of Docker's image page](https://hub.docker.com/r/pyd4vinci/scrapling), the same way it was placed on the project's page.
3. Your logo will be featured as a top sponsor on [Scrapling's website](https://scrapling.readthedocs.io/en/latest/) main page.

### 3. [The Platinum tier](https://github.com/sponsors/D4Vinci/sponsorships?tier_id=586646) ($300/month)
Perks:

1. Your logo will have a special placement at [the very top of Scrapling's project page](https://github.com/D4Vinci/Scrapling?tab=readme-ov-file#platinum-sponsors) with a 25-word paragraph or less.
2. The same logo will be featured at [the PyPI page](https://pypi.org/project/scrapling/)/[the Docker page](https://hub.docker.com/r/pyd4vinci/scrapling), the same way it was placed on the project's page.
3. A special placement for your logo as a top sponsor on [Scrapling's website](https://scrapling.readthedocs.io/en/latest/) main page.
4. A partner role at our Discord server and an announcement on the Twitter page and the Discord server.
5. A Shoutout at the end of each Release notes.
```

### File: docs\index.md
```md
<style>
.md-typeset h1 {
  display: none;
}
[data-md-color-scheme="default"] .only-dark { display: none; }
[data-md-color-scheme="slate"] .only-light { display: none; }
</style>

<br/>
<div align="center">
    <a href="https://scrapling.readthedocs.io/en/latest/" alt="poster">
        <img alt="Scrapling" src="assets/cover_light.svg" class="only-light">
        <img alt="Scrapling" src="assets/cover_dark.svg" class="only-dark">
    </a>
</div>

<h2 align="center"><i>Effortless Web Scraping for the Modern Web</i></h2><br>

Scrapling is an adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl.

Its parser learns from website changes and automatically relocates your elements when pages update. Its fetchers bypass anti-bot systems like Cloudflare Turnstile out of the box. And its spider framework lets you scale up to concurrent, multi-session crawls with pause/resume and automatic proxy rotation - all in a few lines of Python. One library, zero compromises.

Blazing fast crawls with real-time stats and streaming. Built by Web Scrapers for Web Scrapers and regular users, there's something for everyone.

```python
from scrapling.fetchers import Fetcher, StealthyFetcher, DynamicFetcher
StealthyFetcher.adaptive = True
page = StealthyFetcher.fetch('https://example.com', headless=True, network_idle=True)  # Fetch website under the radar!
products = page.css('.product', auto_save=True)                                        # Scrape data that survives website design changes!
products = page.css('.product', adaptive=True)                                         # Later, if the website structure changes, pass `adaptive=True` to find them!
```
Or scale up to full crawls
```python
from scrapling.spiders import Spider, Response

class MySpider(Spider):
  name = "demo"
  start_urls = ["https://example.com/"]

  async def parse(self, response: Response):
      for item in response.css('.product'):
          yield {"title": item.css('h2::text').get()}

MySpider().start()
```

## Top Sponsors 

<style>
.ad {
    width:240px;
    height:100px;
}

</style>

<!-- sponsors -->
<div style="text-align: center;">
  <a href="https://hypersolutions.co/?utm_source=github&utm_medium=readme&utm_campaign=scrapling" target="_blank" title="Bot Protection Bypass API for Akamai, DataDome, Incapsula & Kasada">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/HyperSolutions.png" class="ad">
  </a>
  <a href="https://birdproxies.com/t/scrapling" target="_blank" title="At Bird Proxies, we eliminate your pains such as banned IPs, geo restriction, and high costs so you can focus on your work.">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/BirdProxies.jpg" class="ad">
  </a>
  <a href="https://evomi.com?utm_source=github&utm_medium=banner&utm_campaign=d4vinci-scrapling" target="_blank" title="Evomi is your Swiss Quality Proxy Provider, starting at $0.49/GB">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/evomi.png" class="ad">
  </a>
  <a href="https://tikhub.io/?utm_source=github.com/D4Vinci/Scrapling&utm_medium=marketing_social&utm_campaign=retargeting&utm_content=carousel_ad" target="_blank" title="Unlock the Power of Social Media Data & AI">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/TikHub.jpg" class="ad">
  </a>
  <a href="https://www.nsocks.com/?keyword=2p67aivg" target="_blank" title="Scalable Web Data Access for AI Applications">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/nsocks.png" class="ad">
  </a>
  <a href="https://petrosky.io/d4vinci" target="_blank" title="PetroSky delivers cutting-edge VPS hosting.">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/petrosky.png" class="ad">
  </a>
  <a href="https://substack.thewebscraping.club/p/scrapling-hands-on-guide?utm_source=github&utm_medium=repo&utm_campaign=scrapling" target="_blank" title="The #1 newsletter dedicated to Web Scraping">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/TWSC.png" class="ad">
  </a>
  <a href="https://proxy-seller.com/?partner=CU9CAA5TBYFFT2" target="_blank" title="Proxy-Seller provides reliable proxy infrastructure for Web Scraping">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/ProxySeller.png" class="ad">
  </a>
  <a href="http://mangoproxy.com/?utm_source=D4Vinci&utm_medium=GitHub&utm_campaign=D4Vinci" target="_blank" title="Proxies You Can Rely On: Residential, Server, and Mobile">
    <img src="https://raw.githubusercontent.com/D4Vinci/Scrapling/main/images/MangoProxy.png" class="ad">
  </a>
  <br />
  <br />
</div>
<!-- /sponsors -->

<i><sub>Do you want to show your ad here? Click [here](https://github.com/sponsors/D4Vinci), choose a plan, and enjoy the rest of the perks!</sub></i>

## Key Features

### Spiders - A Full Crawling Framework
- 🕷️ **Scrapy-like Spider API**: Define spiders with `start_urls`, async `parse` callbacks, and `Request`/`Response` objects.
- ⚡ **Concurrent Crawling**: Configurable concurrency limits, per-domain throttling, and download delays.
- 🔄 **Multi-Session Support**: Unified interface for HTTP requests, and stealthy headless browsers in a single spider - route requests to different sessions by ID.
- 💾 **Pause & Resume**: Checkpoint-based crawl persistence. Press Ctrl+C for a graceful shutdown; restart to resume from where you left off.
- 📡 **Streaming Mode**: Stream scraped items as they arrive via `async for item in spider.stream()` with real-time stats - ideal for UI, pipelines, and long-running crawls.
- 🛡️ **Blocked Request Detection**: Automatic detection and retry of blocked requests with customizable logic.
- 📦 **Built-in Export**: Export results through hooks and your own pipeline or the built-in JSON/JSONL with `result.items.to_json()` / `result.items.to_jsonl()` respectively.

### Advanced Websites Fetching with Session Support
- **HTTP Requests**: Fast and stealthy HTTP requests with the `Fetcher` class. Can impersonate browsers' TLS fingerprint, headers, and use HTTP/3.
- **Dynamic Loading**: Fetch dynamic websites with full browser automation through the `DynamicFetcher` class supporting Playwright's Chromium and Google's Chrome.
- **Anti-bot Bypass**: Advanced stealth capabilities with `StealthyFetcher` and fingerprint spoofing. Can easily bypass all types of Cloudflare's Turnstile/Interstitial with automation.
- **Session Management**: Persistent session support with `FetcherSession`, `StealthySession`, and `DynamicSession` classes for cookie and state management across requests.
- **Proxy Rotation**: Built-in `ProxyRotator` with cyclic or custom rotation strategies across all session types, plus per-request proxy overrides.
- **Domain Blocking**: Block requests to specific domains (and their subdomains) in browser-based fetchers.
- **Async Support**: Complete async support across all fetchers and dedicated async session classes.

### Adaptive Scraping & AI Integration
- 🔄 **Smart Element Tracking**: Relocate elements after website changes using intelligent similarity algorithms.
- 🎯 **Smart Flexible Selection**: CSS selectors, XPath selectors, filter-based search, text search, regex search, and more.
- 🔍 **Find Similar Elements**: Automatically locate elements similar to found elements.
- 🤖 **MCP Server to be used with AI**: Built-in MCP server for AI-assisted Web Scraping and data extraction. The MCP server features powerful, custom capabilities that leverage Scrapling to extract targeted content before passing it to the AI (Claude/Cursor/etc), thereby speeding up operations and reducing costs by minimizing token usage. ([demo video](https://www.youtube.com/watch?v=qyFk3ZNwOxE))

### High-Performance & battle-tested Architecture
- 🚀 **Lightning Fast**: Optimized performance outperforming most Python scraping libraries.
- 🔋 **Memory Efficient**: Optimized data structures and lazy loading for a minimal memory footprint.
- ⚡ **Fast JSON Serialization**: 10x faster than the standard library.
- 🏗️ **Battle tested**: Not only does Scrapling have 92% test coverage and full type hints coverage, but it has been used daily by hundreds of Web Scrapers over the past year.

### Developer/Web Scraper Friendly Experience
- 🎯 **Interactive Web Scraping Shell**: Optional built-in IPython shell with Scrapling integration, shortcuts, and new tools to speed up Web Scraping scripts development, like converting curl requests to Scrapling requests and viewing requests results in your browser.
- 🚀 **Use it directly from the Terminal**: Optionally, you can use Scrapling to scrape a URL without writing a single line of code!
- 🛠️ **Rich Navigation API**: Advanced DOM traversal with parent, sibling, and child navigation methods.
- 🧬 **Enhanced Text Processing**: Built-in regex, cleaning methods, and optimized string operations.
- 📝 **Auto Selector Generation**: Generate robust CSS/XPath selectors for any element.
- 🔌 **Familiar API**: Similar to Scrapy/BeautifulSoup with the same pseudo-elements used in Scrapy/Parsel.
- 📘 **Complete Type Coverage**: Full type hints for excellent IDE support and code completion. The entire codebase is automatically scanned with **PyRight** and **MyPy** with each change.
- 🔋 **Ready Docker image**: With each release, a Docker image containing all browsers is automatically built and pushed.


## Star History
Scrapling’s GitHub stars have grown steadily since its release (see chart below).

<div id="chartContainer">
  <a href="https://github.com/D4Vinci/Scrapling">
    <img id="chartImage" alt="Star History Chart" loading="lazy" src="https://api.star-history.com/svg?repos=D4Vinci/Scrapling&type=Date" height="400"/>
  </a>
</div>

<script>
const observer = new MutationObserver((mutations) => {
  mutations.forEach((mutation) => {
    if (mutation.attributeName === 'data-md-color-media') {
      const colorMedia = document.body.getAttribute('data-md-color-media');
      const isDarkScheme = document.body.getAttribute('data-md-color-scheme') === 'slate';
      const chartImg = document.querySelector('#chartImage');
      const baseUrl = 'https://api.star-history.com/svg?repos=D4Vinci/Scrapling&type=Date';
      
      if (colorMedia === '(prefers-color-scheme)' ? isDarkScheme : colorMedia.includes('dark')) {
        chartImg.src = `${baseUrl}&theme=dark`;
      } else {
        chartImg.src = baseUrl;
      }
    }
  });
});

observer.observe(document.body, {
  attributes: true,
  attributeFilter: ['data-md-color-media', 'data-md-color-scheme']
});
</script>


## Installation
Scrapling requires Python 3.10 or higher:

```bash
pip install scrapling
```

This installation only includes the parser engine and its dependencies, without any fetchers or commandline dependencies.

### Optional Dependencies

1. If you are going to use any of the extra features below, the fetchers, or their classes, you will need to install fetchers' dependencies and their browser dependencies as follows:
    ```bash
    pip install "scrapling[fetchers]"
    
    scrapling install           # normal install
    scrapling install  --force  # force reinstall
    ```

    This downloads all browsers, along with their system dependencies and fingerprint manipulation dependencies.

    Or you can install them from the code instead of running a command like this:
    ```python
    from scrapling.cli import install
    
    install([], standalone_mode=False)          # normal install
    install(["--force"], standalone_mode=False) # force reinstall
    ```

2. Extra features:


     - Install the MCP server feature:
       ```bash
       pip install "scrapling[ai]"
       ```
     - Install shell features (Web Scraping shell and the `extract` command): 
         ```bash
         pip install "scrapling[shell]"
         ```
     - Install everything: 
         ```bash
         pip install "scrapling[all]"
         ```
     Don't forget that you need to install the browser dependencies with `scrapling install` after any of these extras (if you didn't already)

### Docker
You can also install a Docker image with all extras and browsers with the following command from DockerHub:
```bash
docker pull pyd4vinci/scrapling
```
Or download it from the GitHub registry:
```bash
docker pull ghcr.io/d4vinci/scrapling:latest
```
This image is automatically built and pushed using GitHub Actions and the repository's main branch.

## How the documentation is organized
Scrapling has extensive documentation, so we try to follow the [Diátaxis documentation framework](https://diataxis.fr/).

## Support

If you like Scrapling and want to support its development:

- ⭐ Star the [GitHub repository](https://github.com/D4Vinci/Scrapling)
- 🚀 Follow us on [Twitter](https://x.com/Scrapling_dev) and join the [discord server](https://discord.gg/EMgGbDceNQ)
- 💝 Consider [sponsoring the project or buying me a coffee](donate.md) :wink:
- 🐛 Report bugs and suggest features through [GitHub Issues](https://github.com/D4Vinci/Scrapling/issues)

## License

This project is licensed under the BSD-3 License. See the [LICENSE](https://github.com/D4Vinci/Scrapling/blob/main/LICENSE) file for details.
```



> [!WARNING]
> Distillation threshold (50000 chars) reached. Truncating further files.
