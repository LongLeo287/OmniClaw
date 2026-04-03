---
id: mission202-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:29:08.793533
---

# KNOWLEDGE EXTRACT: mission202
> **Extracted on:** 2026-03-30 17:42:52
> **Source:** mission202

---

## File: `Stringly.Typed.md`
```markdown
# 📦 mission202/Stringly.Typed [🔖 PENDING/APPROVE]
🔗 https://github.com/mission202/Stringly.Typed
🌐 https://www.nuget.org/packages/Stringly.Typed/

## Meta
- **Stars:** ⭐ 47 | **Forks:** 🍴 4
- **Language:** C# | **License:** MIT
- **Last updated:** 2024-08-04
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Making it easier to convert strings to/from .NET types.

## README (trích đầu)
```
# Stringly.Typed

> Quick, painless conversion of .NET Types <> Strings.

## The Problem

`String` is everywhere - often being a top-level input to most pieces of code.

- User input.
- JSON data (e.g. configuration files).
- QueryString values.
- Database records/documents.
- Console input.

We then take this `string`, and "pass it on" to service layers, which then do their own type-checking/validation, but (for some reason) end up passing the `string` on to other systems. The "validation" logic is duplicated, refactoring is hard, bugs and "WTF's" ensue.

**This is referred to as being "[Stringly Typed](https://blog.codinghorror.com/new-programming-jargon/)"**:

> A riff on strongly typed. Used to describe an implementation that needlessly relies on strings when programmer & refactor friendly options are available.
> 
> For example:
>
> * Method parameters that take strings when other more appropriate types should be used.
> * On the occasion that a string is required in a method call (e.g. network service), the string is then passed and used throughout the rest of the call graph without first converting it to a more suitable internal representation (e.g. parse it and create an enum, then you have strong typing throughout the rest of your codebase).
> * Message passing without using typed messages etc.

For example:

```cs
public Data GetData(string recordId) {
    int result = -1;
    if (!int.TryParse(recordId, out result))
        throw new ArgumentException(nameof(recordId));

    // Now we can get to code the business cares about...
}
```

Our lives would have been so much easier if we had just written:

```cs
public Data GetData(int recordId) {
    // Living the good life! :)
}
```

We see this ALL the time, particularly with things like `int`, `Guid`, `MailAddress`, Postal/ZIP Codes, anything-that-is-a-thing-that-can't-be-empty, and so on.

**It's really just a specific form of ["Primitive Obsession"](https://sourcemaking.com/refactoring/smells/primitive-obsession).**

**You're losing the power (and safety) of a typed system. Validation logic is duplicated, and you get FUGLY code.**

Enter `Stringly.Typed`.

****

## The Solution

> If we can _easily_ define what a "valid" `string` for our type, we can really clean up our codebase.

`Stringly.Typed` made of a few parts:

1. Support for `Stringly<T>`, working with anything that has a `TryParse` method (e.g. primitives, `Guid`, `DateTime`, `IPAddress` - [knock yourself out](https://www.google.co.uk/search?q=.net+tryparse+site%3Ahttps%3A%2F%2Fmsdn.microsoft.com%2Fen-us)).
1. Support for `Stringly<Uri>`, parsing absolute `Uri`'s (e.g. from configuration files).
1. A generic type (`Stringly<T>`) that implements `implicit` operators so you can seamlessly move to/from `String`.
1. A base class that enables quick `Regex` matching.
1. A non-generic `Stringly` base class to make it easy to define "just a string that conforms to a specific format".

## Getting Started

> **Note:** You can see NUnit 
```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

