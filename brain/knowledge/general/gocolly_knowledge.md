---
id: gocolly-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:48.531488
---

# KNOWLEDGE EXTRACT: gocolly
> **Extracted on:** 2026-03-30 17:37:59
> **Source:** gocolly

---

## File: `colly.md`
```markdown
# 📦 gocolly/colly [🔖 PENDING/APPROVE]
🔗 https://github.com/gocolly/colly
🌐 https://go-colly.org/

## Meta
- **Stars:** ⭐ 25184 | **Forks:** 🍴 1839
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Elegant Scraper and Crawler Framework for Golang

## README (trích đầu)
```
# Colly

Lightning Fast and Elegant Scraping Framework for Gophers

Colly provides a clean interface to write any kind of crawler/scraper/spider.

With Colly you can easily extract structured data from websites, which can be used for a wide range of applications, like data mining, data processing or archiving.

[![GoDoc](https://godoc.org/github.com/gocolly/colly?status.svg)](https://pkg.go.dev/github.com/gocolly/colly/v2)
[![Backers on Open Collective](https://opencollective.com/colly/backers/badge.svg)](#backers) [![Sponsors on Open Collective](https://opencollective.com/colly/sponsors/badge.svg)](#sponsors) [![build status](https://github.com/gocolly/colly/actions/workflows/ci.yml/badge.svg)](https://github.com/gocolly/colly/actions/workflows/ci.yml)
[![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/gocolly/colly)
[![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://github.com/gocolly/colly/tree/master/_examples)
[![Code Coverage](https://img.shields.io/codecov/c/github/gocolly/colly/master.svg)](https://codecov.io/github/gocolly/colly?branch=master)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2Fgocolly%2Fcolly.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2Fgocolly%2Fcolly?ref=badge_shield)
[![Twitter URL](https://img.shields.io/badge/twitter-follow-green.svg)](https://twitter.com/gocolly)


## Features

-   Clean API
-   Fast (>1k request/sec on a single core)
-   Manages request delays and maximum concurrency per domain
-   Automatic cookie and session handling
-   Sync/async/parallel scraping
-   Caching
-   Automatic encoding of non-unicode responses
-   Robots.txt support
-   Distributed scraping
-   Configuration via environment variables
-   Extensions

## Example

```go

import (
	"fmt"

	"github.com/gocolly/colly/v2"
)

func main() {
	c := colly.NewCollector()

	// Find and visit all links
	c.OnHTML("a[href]", func(e *colly.HTMLElement) {
		e.Request.Visit(e.Attr("href"))
	})

	c.OnRequest(func(r *colly.Request) {
		fmt.Println("Visiting", r.URL)
	})

	c.Visit("http://go-colly.org/")
}
```

See [examples folder](https://github.com/gocolly/colly/tree/master/_examples) for more detailed examples.

## Installation

`go get github.com/gocolly/colly/v2`


## Bugs

Bugs or suggestions? Visit the [issue tracker](https://github.com/gocolly/colly/issues) or join `#colly` on freenode

## Other Projects Using Colly

Below is a list of public, open source projects that use Colly:

-   [greenpeace/check-my-pages](https://github.com/greenpeace/check-my-pages) Scraping script to test the Spanish Greenpeace web archive.
-   [altsab/gowap](https://github.com/altsab/gowap) Wappalyzer implementation in Go.
-   [jesuiscamille/goquotes](https://github.com/jesuiscamille/goquotes) A quotes scraper, making your day a little better!
-   [jivesearch/jivesearch](https://github.com/jivesearch
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

