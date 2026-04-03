---
id: claromes-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:19:02.121091
---

# KNOWLEDGE EXTRACT: claromes
> **Extracted on:** 2026-03-30 17:31:18
> **Source:** claromes

---

## File: `waybacktweets.md`
```markdown
# 📦 claromes/waybacktweets [🔖 PENDING/APPROVE]
🔗 https://github.com/claromes/waybacktweets
🌐 https://waybacktweets.claromes.com

## Meta
- **Stars:** ⭐ 182 | **Forks:** 🍴 46
- **Language:** Python | **License:** GPL-3.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Archived tweets from the Wayback Machine

## README (trích đầu)
```
# Wayback Tweets

[![PyPI](https://img.shields.io/pypi/v/waybacktweets)](https://pypi.org/project/waybacktweets) [![PyPI Downloads](https://static.pepy.tech/badge/waybacktweets)](https://pepy.tech/projects/waybacktweets)

Retrieves archived tweets CDX data from the Wayback Machine, performs necessary parsing (see [Field Options](https://waybacktweets.claromes.com/field_options)), and saves the data in HTML, for easy viewing of the tweets using the iframe tags, CSV, and JSON formats.

## Installation

It is compatible with Python versions 3.10 and above. [See installation options](https://waybacktweets.claromes.com/installation).

```shell
pipx install waybacktweets
```

## CLI

```shell
Usage:
  waybacktweets [OPTIONS] USERNAME
  USERNAME: The Twitter username without @

Options:
  -c, --collapse [urlkey|digest|timestamp:xx]
                                  Collapse results based on a field, or a
                                  substring of a field. XX in the timestamp
                                  value ranges from 1 to 14, comparing the
                                  first XX digits of the timestamp field. It
                                  is recommended to use from 4 onwards, to
                                  compare at least by years.
  -f, --from DATE                 Filtering by date range from this date.
                                  Format: YYYYmmdd
  -t, --to DATE                   Filtering by date range up to this date.
                                  Format: YYYYmmdd
  -l, --limit INTEGER             Query result limits.
  -rk, --resumption_key TEXT      Allows for a simple way to scroll through
                                  the results. Key to continue the query from
                                  the end of the previous query.
  -mt, --matchtype [exact|prefix|host|domain]
                                  Results matching a certain prefix, a certain
                                  host or all subdomains.
  -v, --verbose                   Shows the log.
  --version                       Show the version and exit.
  -h, --help                      Show this message and exit.

Examples:
  waybacktweets jack
  waybacktweets --from 20200305 --to 20231231 --limit 300 --verbose jack

Repository:
  https://github.com/claromes/waybacktweets

Documentation:
  https://waybacktweets.claromes.com
```

## Module

[![Open In Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1tnaM3rMWpoSHBZ4P_6iHFPjraWRQ3OGe?usp=sharing)

```python
from waybacktweets import WaybackTweets, TweetsParser, TweetsExporter

USERNAME = "jack"

api = WaybackTweets(USERNAME)
archived_tweets = api.get()

if archived_tweets:
    field_options = [
        "archived_urlkey",
        "archived_timestamp",
        "parsed_archived_timestamp",
        "archived_tweet_url",
        "parsed_archived_tweet_url",
        "original_tweet_url",
        "parsed_tweet_url",
        "available_tweet_tex
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

