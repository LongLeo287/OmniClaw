---
id: tree-sitter-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:31:23.016877
---

# KNOWLEDGE EXTRACT: tree-sitter
> **Extracted on:** 2026-03-30 17:55:21
> **Source:** tree-sitter

---

## File: `tree-sitter-c-sharp.md`
```markdown
# 📦 tree-sitter/tree-sitter-c-sharp [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-c-sharp


## Meta
- **Stars:** ⭐ 289 | **Forks:** 🍴 91
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
C# Grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-c-sharp

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-c-sharp/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-c-sharp)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-c-sharp)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-c-sharp)

C# grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter) based upon the Roslyn grammar with changes in order to:

- Deal with differences between the parsing technologies
- Work around some bugs in that grammar
- Handle `#if`, `#else`, `#elif`, `#endif` blocks
- Support syntax highlighting/parsing of fragments
- Simplify the output tree
- Reduce parser state count and complexity
- Be in-line with tree-sitter's convention where applicable

### Status

Comprehensive supports C# 1 through 13.0 with the following exception:

- [ ] `async`, `var` and `await` cannot be used as identifiers everywhere they are valid

### References

- [Official C# 8 Draft Language Spec](https://github.com/dotnet/csharpstandard/tree/draft-v8/standard) provides chapters that formally define the language grammar.
- [Roslyn C# language grammar export](https://github.com/dotnet/roslyn/blob/master/src/Compilers/CSharp/Portable/Generated/CSharp.Generated.g4)
- [SharpLab](https://sharplab.io) (web-based syntax tree playground based on Roslyn)

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-c-sharp/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-c-sharp?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-c-sharp?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-c-sharp?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-c.md`
```markdown
# 📦 tree-sitter/tree-sitter-c [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-c


## Meta
- **Stars:** ⭐ 355 | **Forks:** 🍴 183
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
C grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-c

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-c/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-c)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-c)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-c)

C grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).
Adapted from [this C99 grammar](http://slps.github.io/zoo/c/iso-9899-tc3.html).

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-c/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-c?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-c?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-c?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-cpp.md`
```markdown
# 📦 tree-sitter/tree-sitter-cpp [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-cpp


## Meta
- **Stars:** ⭐ 407 | **Forks:** 🍴 156
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
C++ grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-cpp

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-cpp/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-cpp)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-cpp)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-cpp)

C++ grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

## References

- [Hyperlinked C++ BNF Grammar](http://www.nongnu.org/hcb/)
- [EBNF Syntax: C++](http://www.externsoft.ch/download/cpp-iso.html)

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-cpp/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-cpp?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-cpp?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-cpp?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-go.md`
```markdown
# 📦 tree-sitter/tree-sitter-go [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-go


## Meta
- **Stars:** ⭐ 402 | **Forks:** 🍴 86
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-14
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Go grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-go

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-go/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-go)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-go)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-go)

[Go](https://go.dev/ref/spec) grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-go/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-go?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-go?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-go?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-java.md`
```markdown
# 📦 tree-sitter/tree-sitter-java [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-java


## Meta
- **Stars:** ⭐ 252 | **Forks:** 🍴 136
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-20
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Java grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-java

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-java/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-java)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-java)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-java)

Java grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-java/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-java?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-java?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-java?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-javascript.md`
```markdown
# 📦 tree-sitter/tree-sitter-javascript [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-javascript


## Meta
- **Stars:** ⭐ 468 | **Forks:** 🍴 176
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-18
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Javascript grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-javascript

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-javascript/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-javascript)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-javascript)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-javascript)

JavaScript and JSX grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

This grammar intends to be a close approximation of the [ECMAScript](https://ecma-international.org/publications-and-standards/standards/ecma-262/)
specification, with some extensions to support JSX syntax. We try to support the
latest version of the spec, though it is possible that some very new features may
not be supported yet.

References

- [The ESTree Spec](https://github.com/estree/estree)
- [The ECMAScript 2025 Spec](https://tc39.es/ecma262/2025/)

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-javascript/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-javascript?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-javascript?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-javascript?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-ocaml.md`
```markdown
# 📦 tree-sitter/tree-sitter-ocaml [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-ocaml


## Meta
- **Stars:** ⭐ 93 | **Forks:** 🍴 34
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-24
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
OCaml grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-ocaml

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-ocaml/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-ocaml)
[![crates][crates]](https://crates.io/crates/tree-sitter-ocaml)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-ocaml/)

OCaml grammar for [tree-sitter][].

This module defines grammars for implementations (`.ml`) interfaces (`.mli`) and types. Require them as follows:

```js
require('tree-sitter-ocaml').ocaml;
require('tree-sitter-ocaml').ocaml_interface;
require('tree-sitter-ocaml').ocaml_type;
```

References

- [OCaml language reference](https://ocaml.org/manual/language.html)
- [OCaml language extensions](https://ocaml.org/manual/extn.html)
- [OCaml lexer](https://github.com/ocaml/ocaml/blob/trunk/parsing/lexer.mll)
- [OCaml parser](https://github.com/ocaml/ocaml/blob/trunk/parsing/parser.mly)

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-ocaml/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-ocaml?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-ocaml?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-ocaml?logo=pypi&logoColor=white&label=PyPI
[tree-sitter]: https://tree-sitter.github.io/tree-sitter/

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-php.md`
```markdown
# 📦 tree-sitter/tree-sitter-php [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-php


## Meta
- **Stars:** ⭐ 214 | **Forks:** 🍴 71
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
PHP grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-php

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-php/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-php)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-php)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-php)

PHP grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-php/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-php?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-php?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-php?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-python.md`
```markdown
# 📦 tree-sitter/tree-sitter-python [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-python


## Meta
- **Stars:** ⭐ 534 | **Forks:** 🍴 217
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-21
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Python grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-python

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-python/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-python)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-python)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-python/)

Python grammar for [tree-sitter][].

[tree-sitter]: https://github.com/tree-sitter/tree-sitter

## References

- [Python 2 Grammar](https://docs.python.org/2/reference/grammar.html)
- [Python 3 Grammar](https://docs.python.org/3/reference/grammar.html)

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-python/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-python?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-python?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-python?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-ql.md`
```markdown
# 📦 tree-sitter/tree-sitter-ql [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-ql


## Meta
- **Stars:** ⭐ 35 | **Forks:** 🍴 17
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-26
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
tree-sitter grammar for the CodeQL language

## README (trích đầu)
```
# tree-sitter-ql

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-ql/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-ql)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-ql)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-ql/)

tree-sitter grammar for GitHub CodeQL ([Language Spec](https://codeql.github.com/docs/ql-language-reference/ql-language-specification/))

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-ql/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-ql?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-ql?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-ql?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-ruby.md`
```markdown
# 📦 tree-sitter/tree-sitter-ruby [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-ruby


## Meta
- **Stars:** ⭐ 226 | **Forks:** 🍴 74
- **Language:** C | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Ruby grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-ruby

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-ruby/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-ruby)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-ruby)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-ruby)

Ruby grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

#### References

- [AST Format of the Whitequark parser](https://github.com/whitequark/parser/blob/master/doc/AST_FORMAT.md)

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-ruby/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-ruby?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-ruby?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-ruby?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-rust.md`
```markdown
# 📦 tree-sitter/tree-sitter-rust [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-rust


## Meta
- **Stars:** ⭐ 487 | **Forks:** 🍴 137
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-25
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
Rust grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-rust

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-rust/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-rust)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-rust)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-rust)

Rust grammar for [tree-sitter](https://github.com/tree-sitter/tree-sitter).

## Features

- **Speed** — When initially parsing a file, `tree-sitter-rust` takes around two to three times
  as long as rustc's hand-written parser.

  ```sh
  $ wc -l examples/ast.rs
    2157 examples/ast.rs

  $ rustc -Z unpretty=ast-tree -Z time-passes examples/ast.rs | head -n0
    time:   0.002; rss:   55MB ->   60MB (   +5MB)  parse_crate

  $ tree-sitter parse examples/ast.rs --quiet --time
    examples/ast.rs    6.48 ms        9908 bytes/ms
  ```

  But if you _edit_ the file after parsing it, tree-sitter can generally _update_
  the previous existing syntax tree to reflect your edit in less than a millisecond,
  thanks to its incremental parsing system.

## References

- [The Rust Reference](https://doc.rust-lang.org/reference/) — While Rust does
  not have a specification, the reference tries to describe its working in detail.
  It tends to be out of date.
- [Keywords](https://doc.rust-lang.org/stable/book/appendix-01-keywords.html) and
  [Operators and Symbols](https://doc.rust-lang.org/stable/book/appendix-02-operators.html).

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-rust/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-rust?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-rust?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-rust?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

## File: `tree-sitter-typescript.md`
```markdown
# 📦 tree-sitter/tree-sitter-typescript [🔖 PENDING/APPROVE]
🔗 https://github.com/tree-sitter/tree-sitter-typescript


## Meta
- **Stars:** ⭐ 501 | **Forks:** 🍴 155
- **Language:** JavaScript | **License:** MIT
- **Last updated:** 2026-03-23
- **Status trong AI OS:** 🔖 PENDING/APPROVE

## Description:
TypeScript grammar for tree-sitter

## README (trích đầu)
```
# tree-sitter-typescript

[![CI][ci]](https://github.com/tree-sitter/tree-sitter-typescript/actions/workflows/ci.yml)
[![discord][discord]](https://discord.gg/w7nTvsVJhm)
[![matrix][matrix]](https://matrix.to/#/#tree-sitter-chat:matrix.org)
[![crates][crates]](https://crates.io/crates/tree-sitter-typescript)
[![npm][npm]](https://www.npmjs.com/package/tree-sitter-typescript)
[![pypi][pypi]](https://pypi.org/project/tree-sitter-typescript)

TypeScript and TSX grammars for [tree-sitter][].

Because TSX and TypeScript are actually two different dialects, this module defines two grammars. Require them as follows:

```js
require("tree-sitter-typescript").typescript; // TypeScript grammar
require("tree-sitter-typescript").tsx; // TSX grammar
```

For Javascript files with [flow] type annotations you can use the `tsx` parser.

[tree-sitter]: https://github.com/tree-sitter/tree-sitter
[flow]: https://flow.org/en/

References

- [TypeScript Language Spec](https://github.com/microsoft/TypeScript/blob/30cb20434a6b117e007a4959b2a7c16489f86069/doc/spec-ARCHIVED.md)

[ci]: https://img.shields.io/github/actions/workflow/status/tree-sitter/tree-sitter-typescript/ci.yml?logo=github&label=CI
[discord]: https://img.shields.io/discord/1063097320771698699?logo=discord&label=discord
[matrix]: https://img.shields.io/matrix/tree-sitter-chat%3Amatrix.org?logo=matrix&label=matrix
[npm]: https://img.shields.io/npm/v/tree-sitter-typescript?logo=npm
[crates]: https://img.shields.io/crates/v/tree-sitter-typescript?logo=rust
[pypi]: https://img.shields.io/pypi/v/tree-sitter-typescript?logo=pypi&logoColor=ffd242

```

---
*Ingested: 2026-03-27 | Source: GitHub API | Owner: Dept 07 Knowledge*
```

