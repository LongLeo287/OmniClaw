---
id: mattn-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:06.954482
---

# KNOWLEDGE EXTRACT: mattn
> **Extracted on:** 2026-03-30 17:42:05
> **Source:** mattn

---

## File: `go-colorable.md`
```markdown
# 📦 mattn/go-colorable [🔖 PENDING/APPROVE]
🔗 https://github.com/mattn/go-colorable
🌐 http://godoc.org/github.com/mattn/go-colorable

## Meta
- **Stars:** ⭐ 805 | **Forks:** 🍴 96
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-02-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# go-colorable

[![Build Status](https://github.com/mattn/go-colorable/workflows/test/badge.svg)](https://github.com/mattn/go-colorable/actions?query=workflow%3Atest)
[![Codecov](https://codecov.io/gh/mattn/go-colorable/branch/master/graph/badge.svg)](https://codecov.io/gh/mattn/go-colorable)
[![GoDoc](https://godoc.org/github.com/mattn/go-colorable?status.svg)](http://godoc.org/github.com/mattn/go-colorable)
[![Go Report Card](https://goreportcard.com/badge/mattn/go-colorable)](https://goreportcard.com/report/mattn/go-colorable)

Colorable writer for windows.

For example, most of logger packages doesn't show colors on windows. (I know we can do it with ansicon. But I don't want.)
This package is possible to handle escape sequence for ansi color on windows.

## Too Bad!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/bad.png)


## So Good!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/good.png)

## Usage

```go
logrus.SetFormatter(&logrus.TextFormatter{ForceColors: true})
logrus.SetOutput(colorable.NewColorableStdout())

logrus.Info("succeeded")
logrus.Warn("not correct")
logrus.Error("something error")
logrus.Fatal("panic")
```

You can compile above code on non-windows OSs.

## Installation

```
$ go get github.com/mattn/go-colorable
```

# License

MIT

# Author

Yasuhiro Matsumoto (a.k.a mattn)

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `go-isatty.md`
```markdown
# 📦 mattn/go-isatty [🔖 PENDING/APPROVE]
🔗 https://github.com/mattn/go-isatty
🌐 http://godoc.org/github.com/mattn/go-isatty

## Meta
- **Stars:** ⭐ 895 | **Forks:** 🍴 114
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-18
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
(No description)

## README (trích đầu)
```
# go-isatty

[![Godoc Reference](https://godoc.org/github.com/mattn/go-isatty?status.svg)](http://godoc.org/github.com/mattn/go-isatty)
[![Codecov](https://codecov.io/gh/mattn/go-isatty/branch/master/graph/badge.svg)](https://codecov.io/gh/mattn/go-isatty)
[![Coverage Status](https://coveralls.io/repos/github/mattn/go-isatty/badge.svg?branch=master)](https://coveralls.io/github/mattn/go-isatty?branch=master)
[![Go Report Card](https://goreportcard.com/badge/mattn/go-isatty)](https://goreportcard.com/report/mattn/go-isatty)

isatty for golang

## Usage

```go
package main

import (
	"fmt"
	"github.com/mattn/go-isatty"
	"os"
)

func main() {
	if isatty.IsTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Terminal")
	} else if isatty.IsCygwinTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Cygwin/MSYS2 Terminal")
	} else {
		fmt.Println("Is Not Terminal")
	}
}
```

## Installation

```
$ go get github.com/mattn/go-isatty
```

## License

MIT

## Author

Yasuhiro Matsumoto (a.k.a mattn)

## Thanks

* k-takata: base idea for IsCygwinTerminal

    https://github.com/k-takata/go-iscygpty

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `go-sqlite3.md`
```markdown
# 📦 mattn/go-sqlite3 [🔖 PENDING/APPROVE]
🔗 https://github.com/mattn/go-sqlite3
🌐 http://mattn.github.io/go-sqlite3

## Meta
- **Stars:** ⭐ 9026 | **Forks:** 🍴 1160
- **Language:** C | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
sqlite3 driver for go using database/sql

## README (trích đầu)
```
go-sqlite3
==========

[![Go Reference](https://pkg.go.dev/badge/github.com/mattn/go-sqlite3.svg)](https://pkg.go.dev/github.com/mattn/go-sqlite3)
[![GitHub Actions](https://github.com/mattn/go-sqlite3/workflows/Go/badge.svg)](https://github.com/mattn/go-sqlite3/actions?query=workflow%3AGo)
[![Financial Contributors on Open Collective](https://opencollective.com/mattn-go-sqlite3/all/badge.svg?label=financial+contributors)](https://opencollective.com/mattn-go-sqlite3) 
[![codecov](https://codecov.io/gh/mattn/go-sqlite3/branch/master/graph/badge.svg)](https://codecov.io/gh/mattn/go-sqlite3)
[![Go Report Card](https://goreportcard.com/badge/github.com/mattn/go-sqlite3)](https://goreportcard.com/report/github.com/mattn/go-sqlite3)

Latest stable version is v1.14 or later, not v2.

~~**NOTE:** The increase to v2 was an accident. There were no major changes or features.~~

# Description

A sqlite3 driver that conforms to the built-in database/sql interface.

Supported Golang version: See [.github/workflows/go.yaml](./.github/workflows/go.yaml).

This package follows the official [Golang Release Policy](https://golang.org/doc/devel/release.html#policy).

### Overview

- [go-sqlite3](#go-sqlite3)
- [Description](#description)
    - [Overview](#overview)
- [Installation](#installation)
- [API Reference](#api-reference)
- [Connection String](#connection-string)
  - [DSN Examples](#dsn-examples)
- [Features](#features)
    - [Usage](#usage)
    - [Feature / Extension List](#feature--extension-list)
- [Compilation](#compilation)
  - [Android](#android)
- [ARM](#arm)
- [Cross Compile](#cross-compile)
- [Compiling](#compiling)
  - [Linux](#linux)
    - [Alpine](#alpine)
    - [Fedora](#fedora)
    - [Ubuntu](#ubuntu)
  - [macOS](#mac-osx)
  - [Windows](#windows)
  - [Errors](#errors)
- [User Authentication](#user-authentication)
  - [Compile](#compile)
  - [Usage](#usage-1)
    - [Create protected database](#create-protected-database)
    - [Password Encoding](#password-encoding)
      - [Available Encoders](#available-encoders)
    - [Restrictions](#restrictions)
    - [Support](#support)
    - [User Management](#user-management)
      - [SQL](#sql)
        - [Examples](#examples)
      - [*SQLiteConn](#sqliteconn)
    - [Attached database](#attached-database)
- [Extensions](#extensions)
  - [Spatialite](#spatialite)
- [FAQ](#faq)
- [License](#license)
- [Author](#author)

# Installation

This package can be installed with the `go get` command:

    go get github.com/mattn/go-sqlite3

_go-sqlite3_ is *cgo* package.
If you want to build your app using go-sqlite3, you need gcc.

***Important: because this is a `CGO` enabled package, you are required to set the environment variable `CGO_ENABLED=1` and have a `gcc` compiler present within your path.***

# API Reference

API documentation can be found [here](http://godoc.org/github.com/mattn/go-sqlite3).

Examples can be found under the [examples](./_example) directory.

# Connection String

When creating a new SQ
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

