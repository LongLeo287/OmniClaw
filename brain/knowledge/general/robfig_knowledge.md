---
id: robfig-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:09.824385
---

# KNOWLEDGE EXTRACT: robfig
> **Extracted on:** 2026-03-30 17:53:01
> **Source:** robfig

---

## File: `cron.md`
```markdown
# 📦 robfig/cron [🔖 PENDING/APPROVE]
🔗 https://github.com/robfig/cron


## Meta
- **Stars:** ⭐ 14096 | **Forks:** 🍴 1693
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
a cron library for go

## README (trích đầu)
```
[![GoDoc](http://godoc.org/github.com/robfig/cron?status.png)](http://godoc.org/github.com/robfig/cron)
[![Build Status](https://travis-ci.org/robfig/cron.svg?branch=master)](https://travis-ci.org/robfig/cron)

# cron

Cron V3 has been released!

To download the specific tagged release, run:
```bash
go get github.com/robfig/cron/v3@v3.0.0
```
Import it in your program as:
```go
import "github.com/robfig/cron/v3"
```
It requires Go 1.11 or later due to usage of Go Modules.

Refer to the documentation here:
http://godoc.org/github.com/robfig/cron

The rest of this document describes the the advances in v3 and a list of
breaking changes for users that wish to upgrade from an earlier version.

## Upgrading to v3 (June 2019)

cron v3 is a major upgrade to the library that addresses all outstanding bugs,
feature requests, and rough edges. It is based on a merge of master which
contains various fixes to issues found over the years and the v2 branch which
contains some backwards-incompatible features like the ability to remove cron
jobs. In addition, v3 adds support for Go Modules, cleans up rough edges like
the timezone support, and fixes a number of bugs.

New features:

- Support for Go modules. Callers must now import this library as
  `github.com/robfig/cron/v3`, instead of `gopkg.in/...`

- Fixed bugs:
  - 0f01e6b parser: fix combining of Dow and Dom (#70)
  - dbf3220 adjust times when rolling the clock forward to handle non-existent midnight (#157)
  - eeecf15 spec_test.go: ensure an error is returned on 0 increment (#144)
  - 70971dc cron.Entries(): update request for snapshot to include a reply channel (#97)
  - 1cba5e6 cron: fix: removing a job causes the next scheduled job to run too late (#206)

- Standard cron spec parsing by default (first field is "minute"), with an easy
  way to opt into the seconds field (quartz-compatible). Although, note that the
  year field (optional in Quartz) is not supported.

- Extensible, key/value logging via an interface that complies with
  the https://github.com/go-logr/logr project.

- The new Chain & JobWrapper types allow you to install "interceptors" to add
  cross-cutting behavior like the following:
  - Recover any panics from jobs
  - Delay a job's execution if the previous run hasn't completed yet
  - Skip a job's execution if the previous run hasn't completed yet
  - Log each job's invocations
  - Notification when jobs are completed

It is backwards incompatible with both v1 and v2. These updates are required:

- The v1 branch accepted an optional seconds field at the beginning of the cron
  spec. This is non-standard and has led to a lot of confusion. The new default
  parser conforms to the standard as described by [the Cron wikipedia page].

  UPDATING: To retain the old behavior, construct your Cron with a custom
  parser:
```go
// Seconds field, required
cron.New(cron.WithSeconds())

// Seconds field, optional
cron.New(cron.WithParser(cron.NewParser(
	cron.SecondOptional | cron.Minute | cron.H
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

