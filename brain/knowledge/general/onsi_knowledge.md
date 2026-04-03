---
id: onsi-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:15.054920
---

# KNOWLEDGE EXTRACT: onsi
> **Extracted on:** 2026-03-30 17:49:54
> **Source:** onsi

---

## File: `ginkgo.md`
```markdown
# 📦 onsi/ginkgo [🔖 PENDING/APPROVE]
🔗 https://github.com/onsi/ginkgo
🌐 http://onsi.github.io/ginkgo/

## Meta
- **Stars:** ⭐ 8969 | **Forks:** 🍴 695
- **Language:** Go | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
A Modern Testing Framework for Go

## README (trích đầu)
```
![Ginkgo](https://onsi.github.io/ginkgo/images/ginkgo.png)

[![test](https://github.com/onsi/ginkgo/actions/workflows/test.yml/badge.svg?branch=master)](https://github.com/onsi/ginkgo/actions?query=workflow%3Atest+branch%3Amaster) | [Ginkgo Docs](https://onsi.github.io/ginkgo/)

---

# Ginkgo

Ginkgo is a mature testing framework for Go designed to help you write expressive specs.  Ginkgo builds on top of Go's `testing` foundation and is complemented by the [Gomega](https://github.com/onsi/gomega) matcher library.  Together, Ginkgo and Gomega let you express the intent behind your specs clearly:

```go
import (
    . "github.com/onsi/ginkgo/v2"
    . "github.com/onsi/gomega"
    ...
)

var _ = Describe("Checking books out of the library", Label("library"), func() {
    var library *libraries.Library
    var book *books.Book
    var valjean *users.User
    BeforeEach(func() {
        library = libraries.NewClient()
        book = &books.Book{
            Title: "Les Miserables",
            Author: "Victor Hugo",
        }
        valjean = users.NewUser("Jean Valjean")
    })

    When("the library has the book in question", func() {
        BeforeEach(func(ctx SpecContext) {
            Expect(library.Store(ctx, book)).To(Succeed())
        })

        Context("and the book is available", func() {
            It("lends it to the reader", func(ctx SpecContext) {
                Expect(valjean.Checkout(ctx, library, "Les Miserables")).To(Succeed())
                Expect(valjean.Books()).To(ContainElement(book))
                Expect(library.UserWithBook(ctx, book)).To(Equal(valjean))
            }, SpecTimeout(time.Second * 5))
        })

        Context("but the book has already been checked out", func() {
            var javert *users.User
            BeforeEach(func(ctx SpecContext) {
                javert = users.NewUser("Javert")
                Expect(javert.Checkout(ctx, library, "Les Miserables")).To(Succeed())
            })

            It("tells the user", func(ctx SpecContext) {
                err := valjean.Checkout(ctx, library, "Les Miserables")
                Expect(err).To(MatchError("Les Miserables is currently checked out"))
            }, SpecTimeout(time.Second * 5))

            It("lets the user place a hold and get notified later", func(ctx SpecContext) {
                Expect(valjean.Hold(ctx, library, "Les Miserables")).To(Succeed())
                Expect(valjean.Holds(ctx)).To(ContainElement(book))

                By("when Javert returns the book")
                Expect(javert.Return(ctx, library, book)).To(Succeed())

                By("it eventually informs Valjean")
                notification := "Les Miserables is ready for pick up"
                Eventually(ctx, valjean.Notifications).Should(ContainElement(notification))

                Expect(valjean.Checkout(ctx, library, "Les Miserables")).To(Succeed())
                Expect(valjean.Books(ctx)).To(ContainElement(book))
                Expect(valjea
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

