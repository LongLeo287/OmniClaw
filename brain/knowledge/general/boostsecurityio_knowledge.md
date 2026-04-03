---
id: boostsecurityio-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:18:59.095345
---

# KNOWLEDGE EXTRACT: boostsecurityio
> **Extracted on:** 2026-03-30 17:31:13
> **Source:** boostsecurityio

---

## File: `poutine.md`
```markdown
# 📦 boostsecurityio/poutine [🔖 PENDING/APPROVE]
🔗 https://github.com/boostsecurityio/poutine


## Meta
- **Stars:** ⭐ 392 | **Forks:** 🍴 30
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
boostsecurityio/poutine

## README (trích đầu)
```
[![OpenSSF Best Practices](https://www.bestpractices.dev/projects/8787/badge)](https://www.bestpractices.dev/projects/8787)
[![OpenSSF Scorecard](https://api.securityscorecards.dev/projects/github.com/boostsecurityio/poutine/badge)](https://securityscorecards.dev/viewer/?uri=github.com/boostsecurityio/poutine)
![build](https://github.com/boostsecurityio/poutine/actions/workflows/build_test.yml/badge.svg)
![CodeQL](https://github.com/boostsecurityio/poutine/actions/workflows/codeql.yml/badge.svg)
[![Go Reference](https://pkg.go.dev/badge/github.com/boostsecurityio/poutine/v4.svg)](https://pkg.go.dev/github.com/boostsecurityio/poutine)
[![Go Report Card](https://goreportcard.com/badge/github.com/boostsecurityio/poutine)](https://goreportcard.com/report/github.com/boostsecurityio/poutine)
[![SLSA 3](https://slsa.dev/images/gh-badge-level3.svg)](https://slsa.dev)

[![View site - GH Pages](https://img.shields.io/badge/View_site-GH_Pages-2ea44f?style=for-the-badge)](https://boostsecurityio.github.io/poutine/)

# `poutine`

Created by [BoostSecurity.io](https://boostsecurity.io), `poutine` is a security scanner that detects misconfigurations and vulnerabilities in the build pipelines of a repository. It supports parsing CI workflows from GitHub Actions and Gitlab CI/CD. When given an access token with read-level access, `poutine` can analyze all the repositories of an organization to quickly gain insights into the security posture of the organization's software supply chain.

<table>
<td>

![Finding raised by poutine about "Arbitrary Code Execution from Untrusted Code Changes"](https://github.com/boostsecurityio/poutine/assets/172889/ca031a4f-afd8-4e3f-9e66-a2502bd0379b)

</td>
</table>

See the [documentation](brain/knowledge/docs_legacy/content/en/rules) for a list of rules currently supported by `poutine`.

## Why `poutine`?

In French, the word "poutine", when not referring to the [dish](https://en.wikipedia.org/wiki/Poutine), can be used to mean "messy". Inspired by the complexity and intertwined dependencies of modern open-source projects, `poutine` reflects both a nod to our Montreal roots and the often messy, complex nature of securing software supply chains.

## Supported Platforms

- GitHub Actions
- Gitlab Pipelines
- Azure DevOps
- Pipelines As Code Tekton

## Getting Started

### Installation

To install `poutine`, download the latest release from the [releases page](https://github.com/boostsecurityio/poutine/releases) and add the binary to your $PATH. 

<!-- TODO: cosign verify instructions? -->

#### Homebrew
``` bash
brew install poutine
```

#### Docker
``` bash
docker run -e GH_TOKEN ghcr.io/boostsecurityio/poutine:latest
```

#### GitHub Actions
```yaml
...
jobs:
  poutine:
    runs-on: ubuntu-latest
    permissions:
      security-events: write
      contents: read
    steps:
    - uses: actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11 # v4.1.1
#################################################################################################
    - 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

