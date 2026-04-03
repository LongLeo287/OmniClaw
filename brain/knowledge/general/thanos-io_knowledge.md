---
id: thanos-io-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:21.898392
---

# KNOWLEDGE EXTRACT: thanos-io
> **Extracted on:** 2026-03-30 17:54:16
> **Source:** thanos-io

---

## File: `objstore.md`
```markdown
# 📦 thanos-io/objstore [🔖 PENDING/APPROVE]
🔗 https://github.com/thanos-io/objstore


## Meta
- **Stars:** ⭐ 178 | **Forks:** 🍴 109
- **Language:** Go | **License:** Apache-2.0
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Go module providing unified interface and efficient clients to work with various object storage providers until like GCS, S3, Azure, SWIFT, COS and more. 

## README (trích đầu)
```
<p align="center"><img src="Thanos-logo_fullmedium.png" alt="Thanos Logo"></p>

[![Latest Release](https://img.shields.io/github/release/thanos-io/objstore.svg?style=flat-square)](https://github.com/thanos-io/objstore/releases/latest) [![Slack](https://img.shields.io/badge/join%20slack-%23thanos-brightgreen.svg)](https://slack.cncf.io/)

[![Go Report Card](https://goreportcard.com/badge/github.com/thanos-io/objstore)](https://goreportcard.com/report/github.com/thanos-io/objstore) [![Go Code reference](https://img.shields.io/badge/code%20reference-go.dev-darkblue.svg)](https://pkg.go.dev/github.com/thanos-io/objstore?tab=subdirectories)

[![Tests](https://github.com/thanos-io/objstore/workflows/Test/badge.svg)](https://github.com/thanos-io/objstore/actions?query=workflow%3Atest)

# Thanos Object Storage Client

`objstore` is a Go module providing unified interface and efficient clients to work with various object storage providers.

Features:

* Ability to perform common operations with clear contract against most popular object storages.
* High focus on efficiency and reliability required for distributed databases on object storages.
* Optional built-in YAML based configuration definition for consistent configuration.
* Optional Prometheus metric instrumentation for bucket operations.

> This moduile is battle-tested and used on high scale production by projects like Thanos, Loki, Cortex, Mimir, Tempo, Parca and more.

## Contributing

Contributions are very welcome! See our [CONTRIBUTING.md](https://github.com/thanos-io/thanos/blob/main/CONTRIBUTING.md) for more information.

## Community

Thanos is an open source project and we value and welcome new contributors and members of the community. Here are ways to get in touch with the community:

* Slack: [#thanos](https://slack.cncf.io/)
* Issue Tracker: [GitHub Issues](https://github.com/thanos-io/thanos/issues)

## Adopters

See [`Adopters List`](https://github.com/thanos-io/thanos/blob/main/website/data/adopters.yml.

## Background

This library was initially developed as a Thanos [`objstore` package](https://github.com/thanos-io/thanos/tree/79ab7c65cb4b66b9dcc4fa537cb43b00cc65066c/pkg/objstore). Thanos uses object storage as primary storage for metrics and metadata related to them. This package ended up being used by other projects like Cortex, Loki, Mimir, Tempo, Parca and more.

Given reusability, Thanos community promoted this package to standalone Go module with smaller amount of dependencies.

## Maintainers

See [MAINTAINERS.md](https://github.com/thanos-io/thanos/blob/main/MAINTAINERS.md)

### How to use `objstore`

The core this module is the [`Bucket` interface](objstore.go):

```go mdox-exec="sed -n '55,73p' objstore.go"
// Bucket provides read and write access to an object storage bucket.
// NOTE: We assume strong consistency for write-read flow.
type Bucket interface {
	io.Closer
	BucketReader

	Provider() ObjProvider

	// Upload the contents of the reader as an object into the buck
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

