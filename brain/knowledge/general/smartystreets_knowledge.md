---
id: smartystreets-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:15.816793
---

# KNOWLEDGE EXTRACT: smartystreets
> **Extracted on:** 2026-03-30 17:53:52
> **Source:** smartystreets

---

## File: `goconvey.md`
```markdown
# 📦 smartystreets/goconvey [🔖 PENDING/APPROVE]
🔗 https://github.com/smartystreets/goconvey
🌐 http://smartystreets.github.io/goconvey/

## Meta
- **Stars:** ⭐ 8417 | **Forks:** 🍴 558
- **Language:** Go | **License:** NOASSERTION
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Go testing in the browser. Integrates with `go test`. Write behavioral tests in Go.

## README (trích đầu)
```
# SMARTY DISCLAIMER: Subject to the terms of the associated license agreement, this software is freely available for your use. This software is FREE, AS IN PUPPIES, and is a gift. Enjoy your new responsibility. This means that while we may consider enhancement requests, we may or may not choose to entertain requests at our sole and absolute discretion.

GoConvey is awesome Go testing
==============================

[![Build Status](https://app.travis-ci.com/smartystreets/goconvey.svg?branch=master)](https://app.travis-ci.com/smartystreets/goconvey)
[![GoDoc](https://godoc.org/github.com/smartystreets/goconvey?status.svg)](http://godoc.org/github.com/smartystreets/goconvey)


Welcome to GoConvey, a yummy Go testing tool for gophers. Works with `go test`. Use it in the terminal or browser according to your viewing pleasure.

GoConvey supports the current versions of Go (see the official Go
[release policy](https://golang.org/doc/devel/release#policy)). Currently
this means Go 1.16 and Go 1.17 are supported.

**Features:**

- Directly integrates with `go test`
- Fully-automatic web UI (works with native Go tests, too)
- Huge suite of regression tests
- Shows test coverage
- Readable, colorized console output (understandable by any manager, IT or not)
- Test code generator
- Desktop notifications (optional)
- Immediately open problem lines in [Sublime Text](http://www.sublimetext.com) ([some assembly required](https://github.com/asuth/subl-handler))


You can ask questions about how to use GoConvey on [StackOverflow](http://stackoverflow.com/questions/ask?tags=goconvey,go&title=GoConvey%3A%20). Use the tags `go` and `goconvey`.

**Menu:**

- [Installation](#installation)
- [Quick start](#quick-start)
- [Documentation](#documentation)
- [Screenshots](#screenshots)
- [Contributors](#contributors)




Installation
------------

	$ go install github.com/smartystreets/goconvey

[Quick start](https://github.com/smartystreets/goconvey/wiki#get-going-in-25-seconds)
-----------

Make a test, for example:

```go
package package_name

import (
    "testing"
    . "github.com/smartystreets/goconvey/convey"
)

func TestSpec(t *testing.T) {

	// Only pass t into top-level Convey calls
	Convey("Given some integer with a starting value", t, func() {
		x := 1

		Convey("When the integer is incremented", func() {
			x++

			Convey("The value should be greater by one", func() {
				So(x, ShouldEqual, 2)
			})
		})
	})
}
```


#### [In the browser](https://github.com/smartystreets/goconvey/wiki/Web-UI)

Start up the GoConvey web server at your project's path:

	$ $GOPATH/bin/goconvey

Then watch the test results display in your browser at:

	http://localhost:8080


If the browser doesn't open automatically, please click [http://localhost:8080](http://localhost:8080) to open manually.

There you have it.
![](http://d79i1fxsrar4t.cloudfront.net/goconvey.co/gc-1-dark.png)
As long as GoConvey is running, test results will automatically update in your browser window.

![](ht
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

