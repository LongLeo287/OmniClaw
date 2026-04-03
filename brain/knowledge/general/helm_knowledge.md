---
id: helm-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:51.652236
---

# KNOWLEDGE EXTRACT: helm
> **Extracted on:** 2026-03-30 17:38:05
> **Source:** helm

---

## File: `chart-testing.md`
```markdown
# 📦 helm/chart-testing [🔖 PENDING/APPROVE]
🔗 https://github.com/helm/chart-testing


## Meta
- **Stars:** ⭐ 1624 | **Forks:** 🍴 246
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
CLI tool for linting and testing Helm charts

## README (trích đầu)
```
# Chart Testing

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Go Report Card](https://goreportcard.com/badge/github.com/helm/chart-testing)](https://goreportcard.com/report/github.com/helm/chart-testing)
[![ci](https://github.com/helm/chart-testing/workflows/ci/badge.svg)](https://github.com/helm/chart-testing/actions/workflows/ci.yaml)

`ct` is the tool for testing Helm charts.
It is meant to be used for linting and testing pull requests.
It automatically detects charts changed against the target branch.

## Installation

### Prerequisites

It is recommended to use the provided Docker image which can be [found on Quay](https://quay.io/repository/helmpack/chart-testing).
It comes with all necessary tools installed.

* [Helm](http://helm.sh)
* [Git](https://git-scm.com) (2.17.0 or later)
* [Yamllint](https://github.com/adrienverge/yamllint)
* [Yamale](https://github.com/23andMe/Yamale)
* [Kubectl](https://kubernetes.io/docs/reference/kubectl/overview/)

### Binary Distribution

Download the release distribution for your OS from the Releases page:

https://github.com/helm/chart-testing/releases

Unpack the `ct` binary, add it to your PATH, and you are good to go!

### Docker Image

A Docker image is available at `quay.io/helmpack/chart-testing` with list of
available tags [here](https://quay.io/repository/helmpack/chart-testing?tab=tags).

### Homebrew

```console
$ brew install chart-testing
```

## Usage

See documentation for individual commands:

* [ct](doc/ct.md)
* [ct install](doc/ct_install.md)
* [ct lint](doc/ct_lint.md)
* [ct lint-and-install](doc/ct_lint-and-install.md)
* [ct list-changed](doc/ct_list-changed.md)
* [ct version](doc/ct_version.md)

For a more extensive how-to guide, please see:

* [charts-repo-actions-demo](https://github.com/helm/charts-repo-actions-demo)

## Configuration

`ct` is a command-line application.
All command-line flags can also be set via environment variables or config file.
Environment variables must be prefixed with `CT_`.
Underscores must be used instead of hyphens.

CLI flags, environment variables, and a config file can be mixed.
The following order of precedence applies:

1. CLI flags
1. Environment variables
1. Config file

Note that linting requires config file for [yamllint](https://github.com/adrienverge/yamllint) and [yamale](https://github.com/23andMe/Yamale).
If not specified, these files are search in the current directory, the `.ct` directory in current directory, `$HOME/.ct`, and `/etc/ct`, in that order.
Samples are provided in the [etc](etc) folder.

### Examples

The following example show various way of configuring the same thing:

#### CLI

#### Remote repo

With remote repo:

    ct install --remote upstream --chart-dirs stable,incubator --build-id pr-42

#### Local repo

If you have a chart in current directory and ct installed on the host then you can run:

    ct install --chart-dirs . --charts .

With docker 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

