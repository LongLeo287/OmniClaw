---
id: github.com-wilfred-tree-sitter-elisp-e1d2dde4-know
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:44.222292
---

# KNOWLEDGE EXTRACT: github.com_Wilfred_tree-sitter-elisp_e1d2dde4
> **Extracted on:** 2026-04-01 09:34:31
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007520277/github.com_Wilfred_tree-sitter-elisp_e1d2dde4

---

## File: `.editorconfig`
```
root = true

[*]
charset = utf-8
end_of_line = lf
insert_final_newline = true
trim_trailing_whitespace = true

[*.{json,toml,yml,gyp}]
indent_style = space
indent_size = 2

[*.js]
indent_style = space
indent_size = 2

[*.rs]
indent_style = space
indent_size = 4

[*.{c,cc,h}]
indent_style = space
indent_size = 4

[*.{py,pyi}]
indent_style = space
indent_size = 4

[*.swift]
indent_style = space
indent_size = 4

[*.go]
indent_style = tab
indent_size = 8

[Makefile]
indent_style = tab
indent_size = 8
```

## File: `.gitattributes`
```
* text eol=lf

src/*.json linguist-generated
src/parser.c linguist-generated
src/tree_sitter/* linguist-generated

bindings/** linguist-generated
binding.gyp linguist-generated
setup.py linguist-generated
Makefile linguist-generated
Package.swift linguist-generated

# Zig bindings
build.zig linguist-generated
build.zig.zon linguist-generated
```

## File: `.gitignore`
```
# Rust artifacts
target/
Cargo.lock

# Node artifacts
build/
prebuilds/
node_modules/
package-lock.json

# Swift artifacts
.build/
Package.resolved

# Go artifacts
_obj/

# Python artifacts
.venv/
dist/
*.egg-info
*.whl

# C artifacts
*.a
*.so
*.so.*
*.dylib
*.dll
*.pc
*.exp
*.lib

# Zig artifacts
.zig-cache/
zig-cache/
zig-out/

# Example dirs
/examples/*/

# Grammar volatiles
*.wasm
*.obj
*.o

# Archives
*.tar.gz
*.tgz
*.zip
```

## File: `CHANGELOG.md`
```markdown
# v1.6.1 (released 15 November 2025)

Updated Rust bindings to use tree-sitter-language.

# v1.6.0 (released 15 November 2025)

Updated tree-sitter version, rebuild parser, and added
tree-sitter.json.

# v1.5.0 (released 18 June 2024)

Updated tree-sitter version and rebuilt parser.

# v1.4.0 (released 18 June 2024)

No functional changes, exercising the release process.

# v1.3 (released 3 June 2023)

Don't error on quoted forms that look like function definitions (such
as `'(defun foo)`).

# v1.2

Added some basic syntax highlighting support ("queries" in tree-sitter
terms).

Function definitions are now handled separately from other
s-expressions. Added highlighting and tags table queries for function
definitions.

Macros are also handled separately to other s-expressions. They are
treated the same as functions for highlighting and tags tables.

Special forms are now parsed and highlighted separately from
s-expressions.

Added highlighting for `nil` and `t`.

# v1.1

Added support for more special read syntax.

Added support for bytecode literals.

Linefeed characters (commonly used as section delimiters) are now treated
as whitespace rather than parse errors.

Fixed handling of string literals with newline escaping:

```
"foo\
bar"
```

Fixed handling escaped characters and non-ASCII character in symbols.

# v1.0

Initial release.
```

## File: `Cargo.toml`
```
[package]
name = "tree-sitter-elisp"
description = "Emacs Lisp tree-sitter grammar"
version = "1.7.0"
keywords = ["incremental", "parsing", "tree-sitter", "elisp"]
categories = ["parser-implementations", "parsing", "text-editors"]
authors = ["Wilfred Hughes <me@wilfred.me.uk>"]
repository = "https://github.com/Wilfred/tree-sitter-elisp"
edition = "2018"
license = "MIT"

build = "bindings/rust/build.rs"
include = [
  "bindings/rust/*",
  "grammar.js",
  "queries/*",
  "src/*",
  "tree-sitter.json",
  "/LICENSE",
]

[lib]
path = "bindings/rust/lib.rs"

[dependencies]
tree-sitter-language = "0.1"

[build-dependencies]
cc = "1.2"

[dev-dependencies]
tree-sitter = "0.25.10"
```

## File: `LICENSE`
```
MIT License

Copyright (c) 2021 Wilfred Hughes

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## File: `Makefile`
```
VERSION := 0.0.1

LANGUAGE_NAME := tree-sitter-elisp

# repository
SRC_DIR := src

PARSER_REPO_URL := $(shell git -C $(SRC_DIR) remote get-url origin 2>/dev/null)

ifeq ($(PARSER_URL),)
	PARSER_URL := $(subst .git,,$(PARSER_REPO_URL))
ifeq ($(shell echo $(PARSER_URL) | grep '^[a-z][-+.0-9a-z]*://'),)
	PARSER_URL := $(subst :,/,$(PARSER_URL))
	PARSER_URL := $(subst git@,https://,$(PARSER_URL))
endif
endif

TS ?= tree-sitter

# ABI versioning
SONAME_MAJOR := $(word 1,$(subst ., ,$(VERSION)))
SONAME_MINOR := $(word 2,$(subst ., ,$(VERSION)))

# install directory layout
PREFIX ?= /usr/local
INCLUDEDIR ?= $(PREFIX)/include
LIBDIR ?= $(PREFIX)/lib
PCLIBDIR ?= $(LIBDIR)/pkgconfig

# source/object files
PARSER := $(SRC_DIR)/parser.c
EXTRAS := $(filter-out $(PARSER),$(wildcard $(SRC_DIR)/*.c))
OBJS := $(patsubst %.c,%.o,$(PARSER) $(EXTRAS))

# flags
ARFLAGS ?= rcs
override CFLAGS += -I$(SRC_DIR) -std=c11 -fPIC

# OS-specific bits
ifeq ($(OS),Windows_NT)
	$(error "Windows is not supported")
else ifeq ($(shell uname),Darwin)
	SOEXT = dylib
	SOEXTVER_MAJOR = $(SONAME_MAJOR).dylib
	SOEXTVER = $(SONAME_MAJOR).$(SONAME_MINOR).dylib
	LINKSHARED := $(LINKSHARED)-dynamiclib -Wl,
	ifneq ($(ADDITIONAL_LIBS),)
	LINKSHARED := $(LINKSHARED)$(ADDITIONAL_LIBS),
	endif
	LINKSHARED := $(LINKSHARED)-install_name,$(LIBDIR)/lib$(LANGUAGE_NAME).$(SONAME_MAJOR).dylib,-rpath,@executable_path/../Frameworks
else
	SOEXT = so
	SOEXTVER_MAJOR = so.$(SONAME_MAJOR)
	SOEXTVER = so.$(SONAME_MAJOR).$(SONAME_MINOR)
	LINKSHARED := $(LINKSHARED)-shared -Wl,
	ifneq ($(ADDITIONAL_LIBS),)
	LINKSHARED := $(LINKSHARED)$(ADDITIONAL_LIBS)
	endif
	LINKSHARED := $(LINKSHARED)-soname,lib$(LANGUAGE_NAME).so.$(SONAME_MAJOR)
endif
ifneq ($(filter $(shell uname),FreeBSD NetBSD DragonFly),)
	PCLIBDIR := $(PREFIX)/libdata/pkgconfig
endif

all: lib$(LANGUAGE_NAME).a lib$(LANGUAGE_NAME).$(SOEXT) $(LANGUAGE_NAME).pc

lib$(LANGUAGE_NAME).a: $(OBJS)
	$(AR) $(ARFLAGS) $@ $^

lib$(LANGUAGE_NAME).$(SOEXT): $(OBJS)
	$(CC) $(LDFLAGS) $(LINKSHARED) $^ $(LDLIBS) -o $@
ifneq ($(STRIP),)
	$(STRIP) $@
endif

$(LANGUAGE_NAME).pc: bindings/c/$(LANGUAGE_NAME).pc.in
	sed  -e 's|@URL@|$(PARSER_URL)|' \
		-e 's|@VERSION@|$(VERSION)|' \
		-e 's|@LIBDIR@|$(LIBDIR)|' \
		-e 's|@INCLUDEDIR@|$(INCLUDEDIR)|' \
		-e 's|@REQUIRES@|$(REQUIRES)|' \
		-e 's|@ADDITIONAL_LIBS@|$(ADDITIONAL_LIBS)|' \
		-e 's|=$(PREFIX)|=$${prefix}|' \
		-e 's|@PREFIX@|$(PREFIX)|' $< > $@

$(PARSER): $(SRC_DIR)/grammar.json
	$(TS) generate --no-bindings $^

install: all
	install -d '$(DESTDIR)$(INCLUDEDIR)'/tree_sitter '$(DESTDIR)$(PCLIBDIR)' '$(DESTDIR)$(LIBDIR)'
	install -m644 bindings/c/$(LANGUAGE_NAME).h '$(DESTDIR)$(INCLUDEDIR)'/tree_sitter/$(LANGUAGE_NAME).h
	install -m644 $(LANGUAGE_NAME).pc '$(DESTDIR)$(PCLIBDIR)'/$(LANGUAGE_NAME).pc
	install -m644 lib$(LANGUAGE_NAME).a '$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).a
	install -m755 lib$(LANGUAGE_NAME).$(SOEXT) '$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).$(SOEXTVER)
	ln -sf lib$(LANGUAGE_NAME).$(SOEXTVER) '$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).$(SOEXTVER_MAJOR)
	ln -sf lib$(LANGUAGE_NAME).$(SOEXTVER_MAJOR) '$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).$(SOEXT)

uninstall:
	$(RM) '$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).a \
		'$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).$(SOEXTVER) \
		'$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).$(SOEXTVER_MAJOR) \
		'$(DESTDIR)$(LIBDIR)'/lib$(LANGUAGE_NAME).$(SOEXT) \
		'$(DESTDIR)$(INCLUDEDIR)'/tree_sitter/$(LANGUAGE_NAME).h \
		'$(DESTDIR)$(PCLIBDIR)'/$(LANGUAGE_NAME).pc

clean:
	$(RM) $(OBJS) $(LANGUAGE_NAME).pc lib$(LANGUAGE_NAME).a lib$(LANGUAGE_NAME).$(SOEXT)

test:
	$(TS) test

.PHONY: all install uninstall clean test
```

## File: `README.md`
```markdown
# Tree-sitter Grammar for Emacs Lisp

<a href="https://crates.io/crates/tree-sitter-elisp"><img src="https://img.shields.io/crates/v/tree-sitter-elisp.svg" alt="crates.io"></a>
<a href="https://www.npmjs.com/package/tree-sitter-elisp"><img src="https://img.shields.io/npm/v/tree-sitter-elisp" alt="npm"></a>

A tree-sitter grammar for elisp.

Syntax supported:

* Atoms (integers, floats, strings, characters, symbols)
* Lists (normal syntax `(a b)` and dotted `(a . b)`)
* Vectors
* Quoting and unquoting (`'`, `#'`, `` ` ``, `,`, `,@`)
* Some special read syntax (`$#`, `##`, `#("foo" 1 2 x)`)
* Bytecode literals (`#[1 2 3 4]`)
* Special forms (`let` etc)
* Comments

Limitations:

* Autoload cookies are treated as plain comments

## Limitations

Elisp is a lisp-2 with user-defined macros. A simple parser cannot
detect if e.g. `(foo (let ...))` is a function call with a `let`
expression argument, or a macro call where `let` means something else.

Currently tree-sitter-elisp treats everything as an s-expression. This
is accurate, but makes this package less useful for generating a
summary of file contents, or for syntax highlighting.

Emacs itself has more information that it can use. Emacs will
highlight macro calls based on which macros are defined in the current
instance. Some elisp packages also offer custom highlighting logic,
such as `dash-fontify-mode` in
[dash.el](https://github.com/magnars/dash.el).

## Developing

Check out the repo, then use `npm` to install dependencies.

```
$ npm install
```

You can then parse your favourite elisp files.

```
$ npm run parse ~/.emacs.d/init.el
```

The grammar itself is in
[grammar.js](https://github.com/Wilfred/tree-sitter-elisp/blob/main/grammar.js). You'll
need to regenerate the code after editing the grammar.

```
$ npm run generate
```

This project also contains a few tests.

```
$ npm test
```

You can also run this parser against your `.emacs.d` to confirm it can
parse everything.

```
$ npm run parse -- '/home/wilfred/.emacs.d/**/*.el' --quiet --stat
```

To regenerate the bindings, delete the previously generated files and
run the following.

```
$ npm run ts-init
```

## Why?

The best place to read and write elisp is of course Emacs.

However, there is a growing ecosystem of tools built on top of
tree-sitter, such as GitHub. This project should allow them to support
emacs lisp too.

## Related Projects

[tree-sitter-clojure](https://github.com/sogaiu/tree-sitter-clojure)
is another tree-sitter package for the lisp family. It's a useful
project to compare with, and [has notes discussing lisp-specific
challenges](https://github.com/sogaiu/tree-sitter-clojure/blob/master/doc/scope.md).

[language-emacs-lisp](https://github.com/Alhadis/language-emacs-lisp)
is a textmate grammar for elisp that's used for Atom and GitHub.
```

## File: `binding.gyp`
```
{
  "targets": [
    {
      "target_name": "tree_sitter_elisp_binding",
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except",
      ],
      "include_dirs": [
        "src",
      ],
      "sources": [
        "bindings/node/binding.cc",
        "src/parser.c",
        # NOTE: if your language has an external scanner, add it here.
      ],
      "conditions": [
        ["OS!='win'", {
          "cflags_c": [
            "-std=c11",
          ],
        }, { # OS == "win"
          "cflags_c": [
            "/std:c11",
            "/utf-8",
          ],
        }],
      ],
    }
  ]
}
```

## File: `grammar.js`
```javascript
const COMMENT = token(/;.*/);

const STRING = token(
  seq('"', repeat(choice(/[^"\\]/, seq("\\", /(.|\n)/))), '"')
);

// Symbols can contain any character when escaped:
// https://www.gnu.org/software/emacs/manual/html_node/elisp/Symbol-Type.html
// Most characters do not need escaping, but space and parentheses
// certainly do.
//
// Symbols also cannot start with ?.
const SYMBOL = token(
  /([^?# \n\s\f()\[\]'`,\\";]|\\.)([^# \n\s\f()\[\]'`,\\";]|\\.)*/
);

const ESCAPED_READER_SYMBOL = token(/\\(`|'|,)/);
const INTERNED_EMPTY_STRING = token("##");

const INTEGER_BASE10 = token(/[+-]?[0-9]+\.?/);
const INTEGER_WITH_BASE = token(/#([box]|[0-9][0-9]?r)[0-9a-zA-Z]/);

const FLOAT_WITH_DEC_POINT = token(/[+-]?[0-9]*\.[0-9]+/);
const FLOAT_WITH_EXPONENT = token(/[+-]?[0-9]+[eE][0-9]+/);
const FLOAT_WITH_BOTH = token(/[+-]?[0-9]*\.[0-9]+[eE][0-9]+/);
const FLOAT_INF = token(/-?1.0[eE]\+INF/);
const FLOAT_NAN = token(/-?0.0[eE]\+NaN/);

const CHAR = token(/\?(\\.|.)/);
const UNICODE_NAME_CHAR = token(/\?\\N\{[^}]+\}/);
const LOWER_CODE_POINT_CHAR = token(/\?\\u[0-9a-fA-F]{4}/);
const UPPER_CODE_POINT_CHAR = token(/\?\\U[0-9a-fA-F]{8}/);
const HEX_CHAR = token(/\?\\x[0-9a-fA-F]+/);
const OCTAL_CHAR = token(/\?\\[0-7]{1,3}/);

// E.g. ?\C-o or ?\^o or ?\C-\S-o
const KEY_CHAR = token(/\?(\\(([CMSHsA]-)|\^))+(\\;|.)/);
// E.g. ?\M-\123
const META_OCTAL_CHAR = token(/\?\\M-\\[0-9]{1,3}/);

// https://www.gnu.org/software/emacs/manual/html_node/elisp/Special-Read-Syntax.html
const BYTE_COMPILED_FILE_NAME = token("#$");

module.exports = grammar({
  name: "elisp",

  extras: ($) => [/(\s|\f)/, $.comment],

  rules: {
    source_file: ($) => repeat($._sexp),

    _sexp: ($) =>
      choice(
        $.special_form,
        $.function_definition,
        $.macro_definition,
        $.list,
        $.vector,
        $.hash_table,
        $.bytecode,
        $.string_text_properties,
        $._atom,
        $.quote,
        $.unquote_splice,
        $.unquote
      ),

    special_form: ($) =>
      seq(
        "(",
        choice(
          "and",
          "catch",
          "cond",
          "condition-case",
          "defconst",
          "defvar",
          "function",
          "if",
          "interactive",
          "lambda",
          "let",
          "let*",
          "or",
          "prog1",
          "prog2",
          "progn",
          "quote",
          "save-current-buffer",
          "save-excursion",
          "save-restriction",
          "setq",
          "setq-default",
          "unwind-protect",
          "while"
        ),
        repeat($._sexp),
        ")"
      ),

    function_definition: ($) =>
      prec(
        1,
        seq(
          "(",
          choice("defun", "defsubst"),
          field("name", $.symbol),
          optional(field("parameters", $._sexp)),
          optional(field("docstring", $.string)),
          repeat($._sexp),
          ")"
        )
      ),

    macro_definition: ($) =>
      prec(
        1,
        seq(
          "(",
          "defmacro",
          field("name", $.symbol),
          optional(field("parameters", $._sexp)),
          optional(field("docstring", $.string)),
          repeat($._sexp),
          ")"
        )
      ),

    _atom: ($) =>
      choice(
        $.float,
        $.integer,
        $.char,
        $.string,
        $.byte_compiled_file_name,
        $.symbol
      ),
    float: ($) =>
      choice(
        FLOAT_WITH_DEC_POINT,
        FLOAT_WITH_EXPONENT,
        FLOAT_WITH_BOTH,
        FLOAT_INF,
        FLOAT_NAN
      ),
    integer: ($) => choice(INTEGER_BASE10, INTEGER_WITH_BASE),
    char: ($) =>
      choice(
        CHAR,
        UNICODE_NAME_CHAR,
        LOWER_CODE_POINT_CHAR,
        UPPER_CODE_POINT_CHAR,
        HEX_CHAR,
        OCTAL_CHAR,
        KEY_CHAR,
        META_OCTAL_CHAR
      ),
    string: ($) => STRING,
    byte_compiled_file_name: ($) => BYTE_COMPILED_FILE_NAME,
    symbol: ($) =>
      choice(
        // Match nil and t separately so we can highlight them.
        "nil",
        "t",
        // We need to define these as separate tokens so we can handle
        // e.g '(defun) as a sexp. Without these, we just try
        // function_definition and produce a parse failure.
        "defun",
        "defsubst",
        "defmacro",
        ESCAPED_READER_SYMBOL,
        SYMBOL,
        INTERNED_EMPTY_STRING
      ),

    quote: ($) => seq(choice("#'", "'", "`"), $._sexp),
    unquote_splice: ($) => seq(",@", $._sexp),
    unquote: ($) => seq(",", $._sexp),

    dot: ($) => token("."),
    list: ($) => seq("(", choice(repeat($._sexp)), ")"),
    vector: ($) => seq("[", repeat($._sexp), "]"),
    bytecode: ($) => seq("#[", repeat($._sexp), "]"),

    string_text_properties: ($) => seq("#(", $.string, repeat($._sexp), ")"),

    hash_table: ($) => seq("#s(hash-table", repeat($._sexp), ")"),

    comment: ($) => COMMENT,
  },
});
```

## File: `package.json`
```json
{
  "name": "tree-sitter-elisp",
  "version": "1.7.0",
  "description": "tree-sitter grammar for Emacs Lisp",
  "main": "bindings/node",
  "types": "bindings/node",
  "keywords": [
    "parser",
    "lexer"
  ],
  "files": [
    "grammar.js",
    "binding.gyp",
    "prebuilds/**",
    "bindings/node/*",
    "queries/*",
    "src/**"
  ],
  "scripts": {
    "ts-init": "tree-sitter init --update",
    "generate": "tree-sitter generate",
    "highlight": "tree-sitter highlight",
    "parse": "tree-sitter parse",
    "test": "tree-sitter test",
    "install": "node-gyp-build",
    "prebuildify": "prebuildify --napi --strip"
  },
  "author": "Wilfred Hughes <me@wilfred.me.uk>",
  "repository": {
    "type": "git",
    "url": "git+https://github.com/Wilfred/tree-sitter-elisp.git"
  },
  "license": "MIT",
  "dependencies": {
    "node-addon-api": "^8.0.0",
    "node-gyp-build": "^4.8.4"
  },
  "peerDependencies": {
    "tree-sitter": "^0.25.0"
  },
  "peerDependenciesMeta": {
    "tree_sitter": {
      "optional": true
    }
  },
  "devDependencies": {
    "tree-sitter-cli": "^0.25.0",
    "prebuildify": "^6.0.0"
  },
  "tree-sitter": [
    {
      "scope": "source.emacs.lisp",
      "highlights": "queries/highlights.scm",
      "file-types": [
        "el"
      ]
    }
  ]
}
```

## File: `pyproject.toml`
```
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "tree-sitter-elisp"
description = "Elisp grammar for tree-sitter"
version = "0.0.1"
keywords = ["incremental", "parsing", "tree-sitter", "elisp"]
classifiers = [
  "Intended Audience :: Developers",
  "License :: OSI Approved :: MIT License",
  "Topic :: Software Development :: Compilers",
  "Topic :: Text Processing :: Linguistic",
  "Typing :: Typed"
]
requires-python = ">=3.8"
license.text = "MIT"
readme = "README.md"

[project.urls]
Homepage = "https://github.com/tree-sitter/tree-sitter-elisp"

[project.optional-dependencies]
core = ["tree-sitter~=0.21"]

[tool.cibuildwheel]
build = "cp38-*"
build-frontend = "build"
```

## File: `setup.py`
```python
from os import path
from sysconfig import get_config_var

from setuptools import Extension, find_packages, setup
from setuptools.command.build import build
from setuptools.command.build_ext import build_ext
from setuptools.command.egg_info import egg_info
from wheel.bdist_wheel import bdist_wheel


class Build(build):
    def run(self):
        if path.isdir("queries"):
            dest = path.join(self.build_lib, "tree_sitter_elisp", "queries")
            self.copy_tree("queries", dest)
        super().run()


class BuildExt(build_ext):
    def build_extension(self, ext: Extension):
        if self.compiler.compiler_type != "msvc":
            ext.extra_compile_args = ["-std=c11", "-fvisibility=hidden"]
        else:
            ext.extra_compile_args = ["/std:c11", "/utf-8"]
        if path.exists("src/scanner.c"):
            ext.sources.append("src/scanner.c")
        if ext.py_limited_api:
            ext.define_macros.append(("Py_LIMITED_API", "0x030A0000"))
        super().build_extension(ext)


class BdistWheel(bdist_wheel):
    def get_tag(self):
        python, abi, platform = super().get_tag()
        if python.startswith("cp"):
            python, abi = "cp310", "abi3"
        return python, abi, platform


class EggInfo(egg_info):
    def find_sources(self):
        super().find_sources()
        self.filelist.recursive_include("queries", "*.scm")
        self.filelist.include("src/tree_sitter/*.h")


setup(
    packages=find_packages("bindings/python"),
    package_dir={"": "bindings/python"},
    package_data={
        "tree_sitter_elisp": ["*.pyi", "py.typed"],
        "tree_sitter_elisp.queries": ["*.scm"],
    },
    ext_package="tree_sitter_elisp",
    ext_modules=[
        Extension(
            name="_binding",
            sources=[
                "bindings/python/tree_sitter_elisp/binding.c",
                "src/parser.c",
            ],
            define_macros=[
                ("PY_SSIZE_T_CLEAN", None),
                ("TREE_SITTER_HIDE_SYMBOLS", None),
            ],
            include_dirs=["src"],
            py_limited_api=not get_config_var("Py_GIL_DISABLED"),
        )
    ],
    cmdclass={
        "build": Build,
        "build_ext": BuildExt,
        "bdist_wheel": BdistWheel,
        "egg_info": EggInfo,
    },
    zip_safe=False
)
```

## File: `tree-sitter.json`
```json
{
  "$schema": "https://tree-sitter.github.io/tree-sitter/assets/schemas/config.schema.json",
  "grammars": [
    {
      "name": "elisp",
      "camelcase": "Elisp",
      "title": "Emacs Lisp",
      "scope": "source.elisp",
      "file-types": [
        "el",
        ".emacs"
      ],
      "injection-regex": "^elisp$",
      "highlights": "queries/highlights.scm",
      "class-name": "TreeSitterElisp"
    }
  ],
  "metadata": {
    "version": "1.7.0",
    "license": "MIT",
    "description": "Emacs Lisp",
    "authors": [
      {
        "name": "Wilfred Hughes",
        "email": "me@wilfred.me.uk",
        "url": "https://www.wilfred.me.uk/"
      }
    ],
    "links": {
      "repository": "https://github.com/Wilfred/tree-sitter-elisp/"
    }
  },
  "bindings": {
    "c": false,
    "go": false,
    "node": true,
    "python": true,
    "rust": true,
    "swift": false,
    "zig": false
  }
}
```

## File: `bindings/c/tree-sitter-elisp.h`
```c
#ifndef TREE_SITTER_ELISP_H_
#define TREE_SITTER_ELISP_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_elisp(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_ELISP_H_
```

## File: `bindings/c/tree-sitter-elisp.pc.in`
```
prefix=@PREFIX@
libdir=@LIBDIR@
includedir=@INCLUDEDIR@

Name: tree-sitter-elisp
Description: Elisp grammar for tree-sitter
URL: @URL@
Version: @VERSION@
Requires: @REQUIRES@
Libs: -L${libdir} @ADDITIONAL_LIBS@ -ltree-sitter-elisp
Cflags: -I${includedir}
```

## File: `bindings/go/binding.go`
```go
package tree_sitter_elisp

// #cgo CFLAGS: -std=c11 -fPIC
// #include "../../src/parser.c"
// // NOTE: if your language has an external scanner, add it here.
import "C"

import "unsafe"

// Get the tree-sitter Language for this grammar.
func Language() unsafe.Pointer {
	return unsafe.Pointer(C.tree_sitter_elisp())
}
```

## File: `bindings/go/binding_test.go`
```go
package tree_sitter_elisp_test

import (
	"testing"

	tree_sitter "github.com/smacker/go-tree-sitter"
	"github.com/tree-sitter/tree-sitter-elisp"
)

func TestCanLoadGrammar(t *testing.T) {
	language := tree_sitter.NewLanguage(tree_sitter_elisp.Language())
	if language == nil {
		t.Errorf("Error loading Elisp grammar")
	}
}
```

## File: `bindings/go/go.mod`
```
module github.com/tree-sitter/tree-sitter-elisp

go 1.22

require github.com/smacker/go-tree-sitter v0.0.0-20230720070738-0d0a9f78d8f8
```

## File: `bindings/node/binding.cc`
```
#include <napi.h>

typedef struct TSLanguage TSLanguage;

extern "C" TSLanguage *tree_sitter_elisp();

// "tree-sitter", "language" hashed with BLAKE2
const napi_type_tag LANGUAGE_TYPE_TAG = {
  0x8AF2E5212AD58ABF, 0xD5006CAD83ABBA16
};

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    exports["name"] = Napi::String::New(env, "elisp");
    auto language = Napi::External<TSLanguage>::New(env, tree_sitter_elisp());
    language.TypeTag(&LANGUAGE_TYPE_TAG);
    exports["language"] = language;
    return exports;
}

NODE_API_MODULE(tree_sitter_elisp_binding, Init)
```

## File: `bindings/node/binding_test.js`
```javascript
const assert = require("node:assert");
const { test } = require("node:test");

const Parser = require("tree-sitter");

test("can load grammar", () => {
  const parser = new Parser();
  assert.doesNotThrow(() => parser.setLanguage(require(".")));
});
```

## File: `bindings/node/index.d.ts`
```typescript
type BaseNode = {
  type: string;
  named: boolean;
};

type ChildNode = {
  multiple: boolean;
  required: boolean;
  types: BaseNode[];
};

type NodeInfo =
  | (BaseNode & {
      subtypes: BaseNode[];
    })
  | (BaseNode & {
      fields: { [name: string]: ChildNode };
      children: ChildNode[];
    });

type Language = {
  name: string;
  language: unknown;
  nodeTypeInfo: NodeInfo[];
};

declare const language: Language;
export = language;
```

## File: `bindings/node/index.js`
```javascript
const root = require("path").join(__dirname, "..", "..");

module.exports =
  typeof process.versions.bun === "string"
    // Support `bun build --compile` by being statically analyzable enough to find the .node file at build-time
    ? require(`../../prebuilds/${process.platform}-${process.arch}/tree-sitter-elisp.node`)
    : require("node-gyp-build")(root);

try {
  module.exports.nodeTypeInfo = require("../../src/node-types.json");
} catch (_) {}
```

## File: `bindings/python/tests/test_binding.py`
```python
from unittest import TestCase

from tree_sitter import Language, Parser
import tree_sitter_elisp


class TestLanguage(TestCase):
    def test_can_load_grammar(self):
        try:
            Parser(Language(tree_sitter_elisp.language()))
        except Exception:
            self.fail("Error loading Emacs Lisp grammar")
```

## File: `bindings/python/tree_sitter_elisp/__init__.py`
```python
"Elisp grammar for tree-sitter"

from ._binding import language

__all__ = ["language"]
```

## File: `bindings/python/tree_sitter_elisp/__init__.pyi`
```
def language() -> int: ...
```

## File: `bindings/python/tree_sitter_elisp/binding.c`
```c
#include <Python.h>

typedef struct TSLanguage TSLanguage;

TSLanguage *tree_sitter_elisp(void);

static PyObject* _binding_language(PyObject *self, PyObject *args) {
    return PyLong_FromVoidPtr(tree_sitter_elisp());
}

static struct PyModuleDef_Slot slots[] = {
#ifdef Py_GIL_DISABLED
    {Py_mod_gil, Py_MOD_GIL_NOT_USED},
#endif
    {0, NULL}
};

static PyMethodDef methods[] = {
    {"language", _binding_language, METH_NOARGS,
     "Get the tree-sitter language for this grammar."},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef module = {
    .m_base = PyModuleDef_HEAD_INIT,
    .m_name = "_binding",
    .m_doc = NULL,
    .m_size = 0,
    .m_methods = methods,
    .m_slots = slots,
};

PyMODINIT_FUNC PyInit__binding(void) {
    return PyModuleDef_Init(&module);
}
```

## File: `bindings/rust/build.rs`
```rust
fn main() {
    let src_dir = std::path::Path::new("src");

    let mut c_config = cc::Build::new();
    c_config.std("c11").include(src_dir);

    #[cfg(target_env = "msvc")]
    c_config.flag("-utf-8");

    let parser_path = src_dir.join("parser.c");
    c_config.file(&parser_path);
    println!("cargo:rerun-if-changed={}", parser_path.to_str().unwrap());

    let scanner_path = src_dir.join("scanner.c");
    if scanner_path.exists() {
        c_config.file(&scanner_path);
        println!("cargo:rerun-if-changed={}", scanner_path.to_str().unwrap());
    }

    c_config.compile("tree-sitter-elisp");
}
```

## File: `bindings/rust/lib.rs`
```rust
//! This crate provides Emacs Lisp language support for the [tree-sitter] parsing library.
//!
//! Typically, you will use the [`LANGUAGE`] constant to add this language to a
//! tree-sitter [`Parser`], and then use the parser to parse some code:
//!
//! ```
//! let code = r#"
//! "#;
//! let mut parser = tree_sitter::Parser::new();
//! let language = tree_sitter_elisp::LANGUAGE;
//! parser
//!     .set_language(&language.into())
//!     .expect("Error loading Emacs Lisp parser");
//! let tree = parser.parse(code, None).unwrap();
//! assert!(!tree.root_node().has_error());
//! ```
//!
//! [`Parser`]: https://docs.rs/tree-sitter/0.25.10/tree_sitter/struct.Parser.html
//! [tree-sitter]: https://tree-sitter.github.io/

use tree_sitter_language::LanguageFn;

extern "C" {
    fn tree_sitter_elisp() -> *const ();
}

/// The tree-sitter [`LanguageFn`] for this grammar.
pub const LANGUAGE: LanguageFn = unsafe { LanguageFn::from_raw(tree_sitter_elisp) };

/// The content of the [`node-types.json`] file for this grammar.
///
/// [`node-types.json`]: https://tree-sitter.github.io/tree-sitter/using-parsers/6-static-node-types
pub const NODE_TYPES: &str = include_str!("../../src/node-types.json");

// NOTE: uncomment these to include any queries that this grammar contains:

pub const HIGHLIGHTS_QUERY: &str = include_str!("../../queries/highlights.scm");
// pub const INJECTIONS_QUERY: &str = include_str!("../../queries/injections.scm");
// pub const LOCALS_QUERY: &str = include_str!("../../queries/locals.scm");
pub const TAGS_QUERY: &str = include_str!("../../queries/tags.scm");

#[cfg(test)]
mod tests {
    #[test]
    fn test_can_load_grammar() {
        let mut parser = tree_sitter::Parser::new();
        parser
            .set_language(&super::LANGUAGE.into())
            .expect("Error loading Emacs Lisp parser");
    }
}
```

## File: `bindings/swift/TreeSitterElisp/elisp.h`
```c
#ifndef TREE_SITTER_ELISP_H_
#define TREE_SITTER_ELISP_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_elisp(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_ELISP_H_
```

## File: `queries/highlights.scm`
```
;; Special forms
[
  "and"
  "catch"
  "cond"
  "condition-case"
  "defconst"
  "defvar"
  "function"
  "if"
  "interactive"
  "lambda"
  "let"
  "let*"
  "or"
  "prog1"
  "prog2"
  "progn"
  "quote"
  "save-current-buffer"
  "save-excursion"
  "save-restriction"
  "setq"
  "setq-default"
  "unwind-protect"
  "while"
] @keyword

;; Function definitions
[
 "defun"
 "defsubst"
 ] @keyword
(function_definition name: (symbol) @function)
(function_definition parameters: (list (symbol) @variable.parameter))
(function_definition docstring: (string) @comment)

;; Highlight macro definitions the same way as function definitions.
"defmacro" @keyword
(macro_definition name: (symbol) @function)
(macro_definition parameters: (list (symbol) @variable.parameter))
(macro_definition docstring: (string) @comment)

(comment) @comment

(integer) @number
(float) @number
(char) @number

(string) @string

[
  "("
  ")"
  "#["
  "["
  "]"
] @punctuation.bracket

[
  "`"
  "#'"
  "'"
  ","
  ",@"
] @operator

;; Highlight nil and t as constants, unlike other symbols
[
  "nil"
  "t"
] @constant.builtin
```

## File: `queries/tags.scm`
```
;; defun/defsubst
(function_definition name: (symbol) @name) @definition.function

;; Treat macros as function definitions for the sake of TAGS.
(macro_definition name: (symbol) @name) @definition.function
```

## File: `src/grammar.json`
```json
{
  "$schema": "https://tree-sitter.github.io/tree-sitter/assets/schemas/grammar.schema.json",
  "name": "elisp",
  "rules": {
    "source_file": {
      "type": "REPEAT",
      "content": {
        "type": "SYMBOL",
        "name": "_sexp"
      }
    },
    "_sexp": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "special_form"
        },
        {
          "type": "SYMBOL",
          "name": "function_definition"
        },
        {
          "type": "SYMBOL",
          "name": "macro_definition"
        },
        {
          "type": "SYMBOL",
          "name": "list"
        },
        {
          "type": "SYMBOL",
          "name": "vector"
        },
        {
          "type": "SYMBOL",
          "name": "hash_table"
        },
        {
          "type": "SYMBOL",
          "name": "bytecode"
        },
        {
          "type": "SYMBOL",
          "name": "string_text_properties"
        },
        {
          "type": "SYMBOL",
          "name": "_atom"
        },
        {
          "type": "SYMBOL",
          "name": "quote"
        },
        {
          "type": "SYMBOL",
          "name": "unquote_splice"
        },
        {
          "type": "SYMBOL",
          "name": "unquote"
        }
      ]
    },
    "special_form": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "and"
            },
            {
              "type": "STRING",
              "value": "catch"
            },
            {
              "type": "STRING",
              "value": "cond"
            },
            {
              "type": "STRING",
              "value": "condition-case"
            },
            {
              "type": "STRING",
              "value": "defconst"
            },
            {
              "type": "STRING",
              "value": "defvar"
            },
            {
              "type": "STRING",
              "value": "function"
            },
            {
              "type": "STRING",
              "value": "if"
            },
            {
              "type": "STRING",
              "value": "interactive"
            },
            {
              "type": "STRING",
              "value": "lambda"
            },
            {
              "type": "STRING",
              "value": "let"
            },
            {
              "type": "STRING",
              "value": "let*"
            },
            {
              "type": "STRING",
              "value": "or"
            },
            {
              "type": "STRING",
              "value": "prog1"
            },
            {
              "type": "STRING",
              "value": "prog2"
            },
            {
              "type": "STRING",
              "value": "progn"
            },
            {
              "type": "STRING",
              "value": "quote"
            },
            {
              "type": "STRING",
              "value": "save-current-buffer"
            },
            {
              "type": "STRING",
              "value": "save-excursion"
            },
            {
              "type": "STRING",
              "value": "save-restriction"
            },
            {
              "type": "STRING",
              "value": "setq"
            },
            {
              "type": "STRING",
              "value": "setq-default"
            },
            {
              "type": "STRING",
              "value": "unwind-protect"
            },
            {
              "type": "STRING",
              "value": "while"
            }
          ]
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_sexp"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "function_definition": {
      "type": "PREC",
      "value": 1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "("
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "defun"
              },
              {
                "type": "STRING",
                "value": "defsubst"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "name",
            "content": {
              "type": "SYMBOL",
              "name": "symbol"
            }
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "FIELD",
                "name": "parameters",
                "content": {
                  "type": "SYMBOL",
                  "name": "_sexp"
                }
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "FIELD",
                "name": "docstring",
                "content": {
                  "type": "SYMBOL",
                  "name": "string"
                }
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "_sexp"
            }
          },
          {
            "type": "STRING",
            "value": ")"
          }
        ]
      }
    },
    "macro_definition": {
      "type": "PREC",
      "value": 1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "("
          },
          {
            "type": "STRING",
            "value": "defmacro"
          },
          {
            "type": "FIELD",
            "name": "name",
            "content": {
              "type": "SYMBOL",
              "name": "symbol"
            }
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "FIELD",
                "name": "parameters",
                "content": {
                  "type": "SYMBOL",
                  "name": "_sexp"
                }
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "FIELD",
                "name": "docstring",
                "content": {
                  "type": "SYMBOL",
                  "name": "string"
                }
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "_sexp"
            }
          },
          {
            "type": "STRING",
            "value": ")"
          }
        ]
      }
    },
    "_atom": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "float"
        },
        {
          "type": "SYMBOL",
          "name": "integer"
        },
        {
          "type": "SYMBOL",
          "name": "char"
        },
        {
          "type": "SYMBOL",
          "name": "string"
        },
        {
          "type": "SYMBOL",
          "name": "byte_compiled_file_name"
        },
        {
          "type": "SYMBOL",
          "name": "symbol"
        }
      ]
    },
    "float": {
      "type": "CHOICE",
      "members": [
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "[+-]?[0-9]*\\.[0-9]+"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "[+-]?[0-9]+[eE][0-9]+"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "[+-]?[0-9]*\\.[0-9]+[eE][0-9]+"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "-?1.0[eE]\\+INF"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "-?0.0[eE]\\+NaN"
          }
        }
      ]
    },
    "integer": {
      "type": "CHOICE",
      "members": [
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "[+-]?[0-9]+\\.?"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "#([box]|[0-9][0-9]?r)[0-9a-zA-Z]"
          }
        }
      ]
    },
    "char": {
      "type": "CHOICE",
      "members": [
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?(\\\\.|.)"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?\\\\N\\{[^}]+\\}"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?\\\\u[0-9a-fA-F]{4}"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?\\\\U[0-9a-fA-F]{8}"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?\\\\x[0-9a-fA-F]+"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?\\\\[0-7]{1,3}"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?(\\\\(([CMSHsA]-)|\\^))+(\\\\;|.)"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\?\\\\M-\\\\[0-9]{1,3}"
          }
        }
      ]
    },
    "string": {
      "type": "TOKEN",
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "\""
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "PATTERN",
                  "value": "[^\"\\\\]"
                },
                {
                  "type": "SEQ",
                  "members": [
                    {
                      "type": "STRING",
                      "value": "\\"
                    },
                    {
                      "type": "PATTERN",
                      "value": "(.|\\n)"
                    }
                  ]
                }
              ]
            }
          },
          {
            "type": "STRING",
            "value": "\""
          }
        ]
      }
    },
    "byte_compiled_file_name": {
      "type": "TOKEN",
      "content": {
        "type": "STRING",
        "value": "#$"
      }
    },
    "symbol": {
      "type": "CHOICE",
      "members": [
        {
          "type": "STRING",
          "value": "nil"
        },
        {
          "type": "STRING",
          "value": "t"
        },
        {
          "type": "STRING",
          "value": "defun"
        },
        {
          "type": "STRING",
          "value": "defsubst"
        },
        {
          "type": "STRING",
          "value": "defmacro"
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "\\\\(`|'|,)"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "PATTERN",
            "value": "([^?# \\n\\s\\f()\\[\\]'`,\\\\\";]|\\\\.)([^# \\n\\s\\f()\\[\\]'`,\\\\\";]|\\\\.)*"
          }
        },
        {
          "type": "TOKEN",
          "content": {
            "type": "STRING",
            "value": "##"
          }
        }
      ]
    },
    "quote": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "#'"
            },
            {
              "type": "STRING",
              "value": "'"
            },
            {
              "type": "STRING",
              "value": "`"
            }
          ]
        },
        {
          "type": "SYMBOL",
          "name": "_sexp"
        }
      ]
    },
    "unquote_splice": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": ",@"
        },
        {
          "type": "SYMBOL",
          "name": "_sexp"
        }
      ]
    },
    "unquote": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": ","
        },
        {
          "type": "SYMBOL",
          "name": "_sexp"
        }
      ]
    },
    "dot": {
      "type": "TOKEN",
      "content": {
        "type": "STRING",
        "value": "."
      }
    },
    "list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "REPEAT",
              "content": {
                "type": "SYMBOL",
                "name": "_sexp"
              }
            }
          ]
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "vector": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_sexp"
          }
        },
        {
          "type": "STRING",
          "value": "]"
        }
      ]
    },
    "bytecode": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "#["
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_sexp"
          }
        },
        {
          "type": "STRING",
          "value": "]"
        }
      ]
    },
    "string_text_properties": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "#("
        },
        {
          "type": "SYMBOL",
          "name": "string"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_sexp"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "hash_table": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "#s(hash-table"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_sexp"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "comment": {
      "type": "TOKEN",
      "content": {
        "type": "PATTERN",
        "value": ";.*"
      }
    }
  },
  "extras": [
    {
      "type": "PATTERN",
      "value": "(\\s|\\f)"
    },
    {
      "type": "SYMBOL",
      "name": "comment"
    }
  ],
  "conflicts": [],
  "precedences": [],
  "externals": [],
  "inline": [],
  "supertypes": [],
  "reserved": {}
}
```

## File: `src/node-types.json`
```json
[
  {
    "type": "bytecode",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "char",
    "named": true,
    "fields": {}
  },
  {
    "type": "float",
    "named": true,
    "fields": {}
  },
  {
    "type": "function_definition",
    "named": true,
    "fields": {
      "docstring": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "string",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "symbol",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "byte_compiled_file_name",
            "named": true
          },
          {
            "type": "bytecode",
            "named": true
          },
          {
            "type": "char",
            "named": true
          },
          {
            "type": "float",
            "named": true
          },
          {
            "type": "function_definition",
            "named": true
          },
          {
            "type": "hash_table",
            "named": true
          },
          {
            "type": "integer",
            "named": true
          },
          {
            "type": "list",
            "named": true
          },
          {
            "type": "macro_definition",
            "named": true
          },
          {
            "type": "quote",
            "named": true
          },
          {
            "type": "special_form",
            "named": true
          },
          {
            "type": "string",
            "named": true
          },
          {
            "type": "string_text_properties",
            "named": true
          },
          {
            "type": "symbol",
            "named": true
          },
          {
            "type": "unquote",
            "named": true
          },
          {
            "type": "unquote_splice",
            "named": true
          },
          {
            "type": "vector",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "hash_table",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "integer",
    "named": true,
    "fields": {}
  },
  {
    "type": "list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "macro_definition",
    "named": true,
    "fields": {
      "docstring": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "string",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "symbol",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "byte_compiled_file_name",
            "named": true
          },
          {
            "type": "bytecode",
            "named": true
          },
          {
            "type": "char",
            "named": true
          },
          {
            "type": "float",
            "named": true
          },
          {
            "type": "function_definition",
            "named": true
          },
          {
            "type": "hash_table",
            "named": true
          },
          {
            "type": "integer",
            "named": true
          },
          {
            "type": "list",
            "named": true
          },
          {
            "type": "macro_definition",
            "named": true
          },
          {
            "type": "quote",
            "named": true
          },
          {
            "type": "special_form",
            "named": true
          },
          {
            "type": "string",
            "named": true
          },
          {
            "type": "string_text_properties",
            "named": true
          },
          {
            "type": "symbol",
            "named": true
          },
          {
            "type": "unquote",
            "named": true
          },
          {
            "type": "unquote_splice",
            "named": true
          },
          {
            "type": "vector",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "quote",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "source_file",
    "named": true,
    "root": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "special_form",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "string_text_properties",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "symbol",
    "named": true,
    "fields": {}
  },
  {
    "type": "unquote",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "unquote_splice",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "vector",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "byte_compiled_file_name",
          "named": true
        },
        {
          "type": "bytecode",
          "named": true
        },
        {
          "type": "char",
          "named": true
        },
        {
          "type": "float",
          "named": true
        },
        {
          "type": "function_definition",
          "named": true
        },
        {
          "type": "hash_table",
          "named": true
        },
        {
          "type": "integer",
          "named": true
        },
        {
          "type": "list",
          "named": true
        },
        {
          "type": "macro_definition",
          "named": true
        },
        {
          "type": "quote",
          "named": true
        },
        {
          "type": "special_form",
          "named": true
        },
        {
          "type": "string",
          "named": true
        },
        {
          "type": "string_text_properties",
          "named": true
        },
        {
          "type": "symbol",
          "named": true
        },
        {
          "type": "unquote",
          "named": true
        },
        {
          "type": "unquote_splice",
          "named": true
        },
        {
          "type": "vector",
          "named": true
        }
      ]
    }
  },
  {
    "type": "##",
    "named": false
  },
  {
    "type": "#'",
    "named": false
  },
  {
    "type": "#(",
    "named": false
  },
  {
    "type": "#[",
    "named": false
  },
  {
    "type": "#s(hash-table",
    "named": false
  },
  {
    "type": "'",
    "named": false
  },
  {
    "type": "(",
    "named": false
  },
  {
    "type": ")",
    "named": false
  },
  {
    "type": ",",
    "named": false
  },
  {
    "type": ",@",
    "named": false
  },
  {
    "type": "[",
    "named": false
  },
  {
    "type": "]",
    "named": false
  },
  {
    "type": "`",
    "named": false
  },
  {
    "type": "and",
    "named": false
  },
  {
    "type": "byte_compiled_file_name",
    "named": true
  },
  {
    "type": "catch",
    "named": false
  },
  {
    "type": "comment",
    "named": true,
    "extra": true
  },
  {
    "type": "cond",
    "named": false
  },
  {
    "type": "condition-case",
    "named": false
  },
  {
    "type": "defconst",
    "named": false
  },
  {
    "type": "defmacro",
    "named": false
  },
  {
    "type": "defsubst",
    "named": false
  },
  {
    "type": "defun",
    "named": false
  },
  {
    "type": "defvar",
    "named": false
  },
  {
    "type": "function",
    "named": false
  },
  {
    "type": "if",
    "named": false
  },
  {
    "type": "interactive",
    "named": false
  },
  {
    "type": "lambda",
    "named": false
  },
  {
    "type": "let",
    "named": false
  },
  {
    "type": "let*",
    "named": false
  },
  {
    "type": "nil",
    "named": false
  },
  {
    "type": "or",
    "named": false
  },
  {
    "type": "prog1",
    "named": false
  },
  {
    "type": "prog2",
    "named": false
  },
  {
    "type": "progn",
    "named": false
  },
  {
    "type": "quote",
    "named": false
  },
  {
    "type": "save-current-buffer",
    "named": false
  },
  {
    "type": "save-excursion",
    "named": false
  },
  {
    "type": "save-restriction",
    "named": false
  },
  {
    "type": "setq",
    "named": false
  },
  {
    "type": "setq-default",
    "named": false
  },
  {
    "type": "string",
    "named": true
  },
  {
    "type": "t",
    "named": false
  },
  {
    "type": "unwind-protect",
    "named": false
  },
  {
    "type": "while",
    "named": false
  }
]
```

## File: `src/parser.c`
```c
/* Automatically @generated by tree-sitter v0.25.10 */

#include "tree_sitter/parser.h"

#if defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic ignored "-Wmissing-field-initializers"
#endif

#define LANGUAGE_VERSION 15
#define STATE_COUNT 74
#define LARGE_STATE_COUNT 35
#define SYMBOL_COUNT 82
#define ALIAS_COUNT 0
#define TOKEN_COUNT 63
#define EXTERNAL_TOKEN_COUNT 0
#define FIELD_COUNT 3
#define MAX_ALIAS_SEQUENCE_LENGTH 7
#define MAX_RESERVED_WORD_SET_SIZE 0
#define PRODUCTION_ID_COUNT 5
#define SUPERTYPE_COUNT 0

enum ts_symbol_identifiers {
  anon_sym_LPAREN = 1,
  anon_sym_and = 2,
  anon_sym_catch = 3,
  anon_sym_cond = 4,
  anon_sym_condition_DASHcase = 5,
  anon_sym_defconst = 6,
  anon_sym_defvar = 7,
  anon_sym_function = 8,
  anon_sym_if = 9,
  anon_sym_interactive = 10,
  anon_sym_lambda = 11,
  anon_sym_let = 12,
  anon_sym_let_STAR = 13,
  anon_sym_or = 14,
  anon_sym_prog1 = 15,
  anon_sym_prog2 = 16,
  anon_sym_progn = 17,
  anon_sym_quote = 18,
  anon_sym_save_DASHcurrent_DASHbuffer = 19,
  anon_sym_save_DASHexcursion = 20,
  anon_sym_save_DASHrestriction = 21,
  anon_sym_setq = 22,
  anon_sym_setq_DASHdefault = 23,
  anon_sym_unwind_DASHprotect = 24,
  anon_sym_while = 25,
  anon_sym_RPAREN = 26,
  anon_sym_defun = 27,
  anon_sym_defsubst = 28,
  anon_sym_defmacro = 29,
  aux_sym_float_token1 = 30,
  aux_sym_float_token2 = 31,
  aux_sym_float_token3 = 32,
  aux_sym_float_token4 = 33,
  aux_sym_float_token5 = 34,
  aux_sym_integer_token1 = 35,
  aux_sym_integer_token2 = 36,
  aux_sym_char_token1 = 37,
  aux_sym_char_token2 = 38,
  aux_sym_char_token3 = 39,
  aux_sym_char_token4 = 40,
  aux_sym_char_token5 = 41,
  aux_sym_char_token6 = 42,
  aux_sym_char_token7 = 43,
  aux_sym_char_token8 = 44,
  sym_string = 45,
  sym_byte_compiled_file_name = 46,
  anon_sym_nil = 47,
  anon_sym_t = 48,
  aux_sym_symbol_token1 = 49,
  aux_sym_symbol_token2 = 50,
  anon_sym_POUND_POUND = 51,
  anon_sym_POUND_SQUOTE = 52,
  anon_sym_SQUOTE = 53,
  anon_sym_BQUOTE = 54,
  anon_sym_COMMA_AT = 55,
  anon_sym_COMMA = 56,
  anon_sym_LBRACK = 57,
  anon_sym_RBRACK = 58,
  anon_sym_POUND_LBRACK = 59,
  anon_sym_POUND_LPAREN = 60,
  anon_sym_POUNDs_LPARENhash_DASHtable = 61,
  sym_comment = 62,
  sym_source_file = 63,
  sym__sexp = 64,
  sym_special_form = 65,
  sym_function_definition = 66,
  sym_macro_definition = 67,
  sym__atom = 68,
  sym_float = 69,
  sym_integer = 70,
  sym_char = 71,
  sym_symbol = 72,
  sym_quote = 73,
  sym_unquote_splice = 74,
  sym_unquote = 75,
  sym_list = 76,
  sym_vector = 77,
  sym_bytecode = 78,
  sym_string_text_properties = 79,
  sym_hash_table = 80,
  aux_sym_source_file_repeat1 = 81,
};

static const char * const ts_symbol_names[] = {
  [ts_builtin_sym_end] = "end",
  [anon_sym_LPAREN] = "(",
  [anon_sym_and] = "and",
  [anon_sym_catch] = "catch",
  [anon_sym_cond] = "cond",
  [anon_sym_condition_DASHcase] = "condition-case",
  [anon_sym_defconst] = "defconst",
  [anon_sym_defvar] = "defvar",
  [anon_sym_function] = "function",
  [anon_sym_if] = "if",
  [anon_sym_interactive] = "interactive",
  [anon_sym_lambda] = "lambda",
  [anon_sym_let] = "let",
  [anon_sym_let_STAR] = "let*",
  [anon_sym_or] = "or",
  [anon_sym_prog1] = "prog1",
  [anon_sym_prog2] = "prog2",
  [anon_sym_progn] = "progn",
  [anon_sym_quote] = "quote",
  [anon_sym_save_DASHcurrent_DASHbuffer] = "save-current-buffer",
  [anon_sym_save_DASHexcursion] = "save-excursion",
  [anon_sym_save_DASHrestriction] = "save-restriction",
  [anon_sym_setq] = "setq",
  [anon_sym_setq_DASHdefault] = "setq-default",
  [anon_sym_unwind_DASHprotect] = "unwind-protect",
  [anon_sym_while] = "while",
  [anon_sym_RPAREN] = ")",
  [anon_sym_defun] = "defun",
  [anon_sym_defsubst] = "defsubst",
  [anon_sym_defmacro] = "defmacro",
  [aux_sym_float_token1] = "float_token1",
  [aux_sym_float_token2] = "float_token2",
  [aux_sym_float_token3] = "float_token3",
  [aux_sym_float_token4] = "float_token4",
  [aux_sym_float_token5] = "float_token5",
  [aux_sym_integer_token1] = "integer_token1",
  [aux_sym_integer_token2] = "integer_token2",
  [aux_sym_char_token1] = "char_token1",
  [aux_sym_char_token2] = "char_token2",
  [aux_sym_char_token3] = "char_token3",
  [aux_sym_char_token4] = "char_token4",
  [aux_sym_char_token5] = "char_token5",
  [aux_sym_char_token6] = "char_token6",
  [aux_sym_char_token7] = "char_token7",
  [aux_sym_char_token8] = "char_token8",
  [sym_string] = "string",
  [sym_byte_compiled_file_name] = "byte_compiled_file_name",
  [anon_sym_nil] = "nil",
  [anon_sym_t] = "t",
  [aux_sym_symbol_token1] = "symbol_token1",
  [aux_sym_symbol_token2] = "symbol_token2",
  [anon_sym_POUND_POUND] = "##",
  [anon_sym_POUND_SQUOTE] = "#'",
  [anon_sym_SQUOTE] = "'",
  [anon_sym_BQUOTE] = "`",
  [anon_sym_COMMA_AT] = ",@",
  [anon_sym_COMMA] = ",",
  [anon_sym_LBRACK] = "[",
  [anon_sym_RBRACK] = "]",
  [anon_sym_POUND_LBRACK] = "#[",
  [anon_sym_POUND_LPAREN] = "#(",
  [anon_sym_POUNDs_LPARENhash_DASHtable] = "#s(hash-table",
  [sym_comment] = "comment",
  [sym_source_file] = "source_file",
  [sym__sexp] = "_sexp",
  [sym_special_form] = "special_form",
  [sym_function_definition] = "function_definition",
  [sym_macro_definition] = "macro_definition",
  [sym__atom] = "_atom",
  [sym_float] = "float",
  [sym_integer] = "integer",
  [sym_char] = "char",
  [sym_symbol] = "symbol",
  [sym_quote] = "quote",
  [sym_unquote_splice] = "unquote_splice",
  [sym_unquote] = "unquote",
  [sym_list] = "list",
  [sym_vector] = "vector",
  [sym_bytecode] = "bytecode",
  [sym_string_text_properties] = "string_text_properties",
  [sym_hash_table] = "hash_table",
  [aux_sym_source_file_repeat1] = "source_file_repeat1",
};

static const TSSymbol ts_symbol_map[] = {
  [ts_builtin_sym_end] = ts_builtin_sym_end,
  [anon_sym_LPAREN] = anon_sym_LPAREN,
  [anon_sym_and] = anon_sym_and,
  [anon_sym_catch] = anon_sym_catch,
  [anon_sym_cond] = anon_sym_cond,
  [anon_sym_condition_DASHcase] = anon_sym_condition_DASHcase,
  [anon_sym_defconst] = anon_sym_defconst,
  [anon_sym_defvar] = anon_sym_defvar,
  [anon_sym_function] = anon_sym_function,
  [anon_sym_if] = anon_sym_if,
  [anon_sym_interactive] = anon_sym_interactive,
  [anon_sym_lambda] = anon_sym_lambda,
  [anon_sym_let] = anon_sym_let,
  [anon_sym_let_STAR] = anon_sym_let_STAR,
  [anon_sym_or] = anon_sym_or,
  [anon_sym_prog1] = anon_sym_prog1,
  [anon_sym_prog2] = anon_sym_prog2,
  [anon_sym_progn] = anon_sym_progn,
  [anon_sym_quote] = anon_sym_quote,
  [anon_sym_save_DASHcurrent_DASHbuffer] = anon_sym_save_DASHcurrent_DASHbuffer,
  [anon_sym_save_DASHexcursion] = anon_sym_save_DASHexcursion,
  [anon_sym_save_DASHrestriction] = anon_sym_save_DASHrestriction,
  [anon_sym_setq] = anon_sym_setq,
  [anon_sym_setq_DASHdefault] = anon_sym_setq_DASHdefault,
  [anon_sym_unwind_DASHprotect] = anon_sym_unwind_DASHprotect,
  [anon_sym_while] = anon_sym_while,
  [anon_sym_RPAREN] = anon_sym_RPAREN,
  [anon_sym_defun] = anon_sym_defun,
  [anon_sym_defsubst] = anon_sym_defsubst,
  [anon_sym_defmacro] = anon_sym_defmacro,
  [aux_sym_float_token1] = aux_sym_float_token1,
  [aux_sym_float_token2] = aux_sym_float_token2,
  [aux_sym_float_token3] = aux_sym_float_token3,
  [aux_sym_float_token4] = aux_sym_float_token4,
  [aux_sym_float_token5] = aux_sym_float_token5,
  [aux_sym_integer_token1] = aux_sym_integer_token1,
  [aux_sym_integer_token2] = aux_sym_integer_token2,
  [aux_sym_char_token1] = aux_sym_char_token1,
  [aux_sym_char_token2] = aux_sym_char_token2,
  [aux_sym_char_token3] = aux_sym_char_token3,
  [aux_sym_char_token4] = aux_sym_char_token4,
  [aux_sym_char_token5] = aux_sym_char_token5,
  [aux_sym_char_token6] = aux_sym_char_token6,
  [aux_sym_char_token7] = aux_sym_char_token7,
  [aux_sym_char_token8] = aux_sym_char_token8,
  [sym_string] = sym_string,
  [sym_byte_compiled_file_name] = sym_byte_compiled_file_name,
  [anon_sym_nil] = anon_sym_nil,
  [anon_sym_t] = anon_sym_t,
  [aux_sym_symbol_token1] = aux_sym_symbol_token1,
  [aux_sym_symbol_token2] = aux_sym_symbol_token2,
  [anon_sym_POUND_POUND] = anon_sym_POUND_POUND,
  [anon_sym_POUND_SQUOTE] = anon_sym_POUND_SQUOTE,
  [anon_sym_SQUOTE] = anon_sym_SQUOTE,
  [anon_sym_BQUOTE] = anon_sym_BQUOTE,
  [anon_sym_COMMA_AT] = anon_sym_COMMA_AT,
  [anon_sym_COMMA] = anon_sym_COMMA,
  [anon_sym_LBRACK] = anon_sym_LBRACK,
  [anon_sym_RBRACK] = anon_sym_RBRACK,
  [anon_sym_POUND_LBRACK] = anon_sym_POUND_LBRACK,
  [anon_sym_POUND_LPAREN] = anon_sym_POUND_LPAREN,
  [anon_sym_POUNDs_LPARENhash_DASHtable] = anon_sym_POUNDs_LPARENhash_DASHtable,
  [sym_comment] = sym_comment,
  [sym_source_file] = sym_source_file,
  [sym__sexp] = sym__sexp,
  [sym_special_form] = sym_special_form,
  [sym_function_definition] = sym_function_definition,
  [sym_macro_definition] = sym_macro_definition,
  [sym__atom] = sym__atom,
  [sym_float] = sym_float,
  [sym_integer] = sym_integer,
  [sym_char] = sym_char,
  [sym_symbol] = sym_symbol,
  [sym_quote] = sym_quote,
  [sym_unquote_splice] = sym_unquote_splice,
  [sym_unquote] = sym_unquote,
  [sym_list] = sym_list,
  [sym_vector] = sym_vector,
  [sym_bytecode] = sym_bytecode,
  [sym_string_text_properties] = sym_string_text_properties,
  [sym_hash_table] = sym_hash_table,
  [aux_sym_source_file_repeat1] = aux_sym_source_file_repeat1,
};

static const TSSymbolMetadata ts_symbol_metadata[] = {
  [ts_builtin_sym_end] = {
    .visible = false,
    .named = true,
  },
  [anon_sym_LPAREN] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_and] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_catch] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_cond] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_condition_DASHcase] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_defconst] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_defvar] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_function] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_if] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_interactive] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_lambda] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_let] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_let_STAR] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_or] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_prog1] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_prog2] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_progn] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_quote] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_save_DASHcurrent_DASHbuffer] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_save_DASHexcursion] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_save_DASHrestriction] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_setq] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_setq_DASHdefault] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_unwind_DASHprotect] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_while] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_RPAREN] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_defun] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_defsubst] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_defmacro] = {
    .visible = true,
    .named = false,
  },
  [aux_sym_float_token1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_float_token2] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_float_token3] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_float_token4] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_float_token5] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_integer_token1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_integer_token2] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token2] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token3] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token4] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token5] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token6] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token7] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_char_token8] = {
    .visible = false,
    .named = false,
  },
  [sym_string] = {
    .visible = true,
    .named = true,
  },
  [sym_byte_compiled_file_name] = {
    .visible = true,
    .named = true,
  },
  [anon_sym_nil] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_t] = {
    .visible = true,
    .named = false,
  },
  [aux_sym_symbol_token1] = {
    .visible = false,
    .named = false,
  },
  [aux_sym_symbol_token2] = {
    .visible = false,
    .named = false,
  },
  [anon_sym_POUND_POUND] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_POUND_SQUOTE] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_SQUOTE] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_BQUOTE] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_COMMA_AT] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_COMMA] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_LBRACK] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_RBRACK] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_POUND_LBRACK] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_POUND_LPAREN] = {
    .visible = true,
    .named = false,
  },
  [anon_sym_POUNDs_LPARENhash_DASHtable] = {
    .visible = true,
    .named = false,
  },
  [sym_comment] = {
    .visible = true,
    .named = true,
  },
  [sym_source_file] = {
    .visible = true,
    .named = true,
  },
  [sym__sexp] = {
    .visible = false,
    .named = true,
  },
  [sym_special_form] = {
    .visible = true,
    .named = true,
  },
  [sym_function_definition] = {
    .visible = true,
    .named = true,
  },
  [sym_macro_definition] = {
    .visible = true,
    .named = true,
  },
  [sym__atom] = {
    .visible = false,
    .named = true,
  },
  [sym_float] = {
    .visible = true,
    .named = true,
  },
  [sym_integer] = {
    .visible = true,
    .named = true,
  },
  [sym_char] = {
    .visible = true,
    .named = true,
  },
  [sym_symbol] = {
    .visible = true,
    .named = true,
  },
  [sym_quote] = {
    .visible = true,
    .named = true,
  },
  [sym_unquote_splice] = {
    .visible = true,
    .named = true,
  },
  [sym_unquote] = {
    .visible = true,
    .named = true,
  },
  [sym_list] = {
    .visible = true,
    .named = true,
  },
  [sym_vector] = {
    .visible = true,
    .named = true,
  },
  [sym_bytecode] = {
    .visible = true,
    .named = true,
  },
  [sym_string_text_properties] = {
    .visible = true,
    .named = true,
  },
  [sym_hash_table] = {
    .visible = true,
    .named = true,
  },
  [aux_sym_source_file_repeat1] = {
    .visible = false,
    .named = false,
  },
};

enum ts_field_identifiers {
  field_docstring = 1,
  field_name = 2,
  field_parameters = 3,
};

static const char * const ts_field_names[] = {
  [0] = NULL,
  [field_docstring] = "docstring",
  [field_name] = "name",
  [field_parameters] = "parameters",
};

static const TSMapSlice ts_field_map_slices[PRODUCTION_ID_COUNT] = {
  [1] = {.index = 0, .length = 1},
  [2] = {.index = 1, .length = 2},
  [3] = {.index = 3, .length = 2},
  [4] = {.index = 5, .length = 3},
};

static const TSFieldMapEntry ts_field_map_entries[] = {
  [0] =
    {field_name, 2},
  [1] =
    {field_docstring, 3},
    {field_name, 2},
  [3] =
    {field_name, 2},
    {field_parameters, 3},
  [5] =
    {field_docstring, 4},
    {field_name, 2},
    {field_parameters, 3},
};

static const TSSymbol ts_alias_sequences[PRODUCTION_ID_COUNT][MAX_ALIAS_SEQUENCE_LENGTH] = {
  [0] = {0},
};

static const uint16_t ts_non_terminal_alias_map[] = {
  0,
};

static const TSStateId ts_primary_state_ids[STATE_COUNT] = {
  [0] = 0,
  [1] = 1,
  [2] = 2,
  [3] = 3,
  [4] = 4,
  [5] = 5,
  [6] = 6,
  [7] = 7,
  [8] = 8,
  [9] = 9,
  [10] = 10,
  [11] = 11,
  [12] = 12,
  [13] = 13,
  [14] = 14,
  [15] = 15,
  [16] = 16,
  [17] = 17,
  [18] = 18,
  [19] = 19,
  [20] = 20,
  [21] = 21,
  [22] = 22,
  [23] = 23,
  [24] = 24,
  [25] = 25,
  [26] = 26,
  [27] = 27,
  [28] = 28,
  [29] = 29,
  [30] = 30,
  [31] = 31,
  [32] = 32,
  [33] = 33,
  [34] = 34,
  [35] = 35,
  [36] = 36,
  [37] = 37,
  [38] = 38,
  [39] = 39,
  [40] = 40,
  [41] = 41,
  [42] = 42,
  [43] = 43,
  [44] = 44,
  [45] = 45,
  [46] = 46,
  [47] = 47,
  [48] = 48,
  [49] = 49,
  [50] = 50,
  [51] = 51,
  [52] = 52,
  [53] = 53,
  [54] = 54,
  [55] = 55,
  [56] = 56,
  [57] = 57,
  [58] = 58,
  [59] = 59,
  [60] = 60,
  [61] = 61,
  [62] = 62,
  [63] = 63,
  [64] = 64,
  [65] = 65,
  [66] = 66,
  [67] = 67,
  [68] = 68,
  [69] = 69,
  [70] = 70,
  [71] = 71,
  [72] = 72,
  [73] = 73,
};

static const TSCharacterRange aux_sym_symbol_token2_character_set_2[] = {
  {0, 0x08}, {0x0e, 0x1f}, {'!', '!'}, {'$', '&'}, {'*', '+'}, {'-', ':'}, {'<', 'Z'}, {'\\', '\\'},
  {'^', '_'}, {'a', 0x10ffff},
};

static bool ts_lex(TSLexer *lexer, TSStateId state) {
  START_LEXER();
  eof = lexer->eof(lexer);
  switch (state) {
    case 0:
      if (eof) ADVANCE(51);
      ADVANCE_MAP(
        '"', 1,
        '#', 2,
        '\'', 290,
        '(', 52,
        ')', 77,
        '+', 141,
        ',', 293,
        '-', 140,
        '.', 284,
        '0', 92,
        '1', 98,
        ';', 299,
        '?', 17,
        '[', 294,
        '\\', 35,
        ']', 295,
        '`', 291,
        'a', 216,
        'c', 152,
        'd', 180,
        'f', 273,
        'i', 193,
        'l', 153,
        'n', 202,
        'o', 239,
        'p', 240,
        'q', 271,
        's', 154,
        't', 128,
        'u', 217,
        'w', 201,
      );
      if (('\t' <= lookahead && lookahead <= '\r') ||
          lookahead == ' ') SKIP(0);
      if (('2' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if (lookahead != 0) ADVANCE(287);
      END_STATE();
    case 1:
      if (lookahead == '"') ADVANCE(125);
      if (lookahead == '\\') ADVANCE(49);
      if (lookahead != 0) ADVANCE(1);
      END_STATE();
    case 2:
      ADVANCE_MAP(
        '#', 288,
        '$', 126,
        '\'', 289,
        '(', 297,
        '[', 296,
        's', 3,
        'b', 46,
        'o', 46,
        'x', 46,
      );
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(29);
      END_STATE();
    case 3:
      if (lookahead == '(') ADVANCE(25);
      END_STATE();
    case 4:
      if (lookahead == '+') ADVANCE(16);
      END_STATE();
    case 5:
      if (lookahead == '+') ADVANCE(13);
      END_STATE();
    case 6:
      if (lookahead == '-') ADVANCE(31);
      END_STATE();
    case 7:
      if (lookahead == '-') ADVANCE(18);
      END_STATE();
    case 8:
      if (lookahead == '0') ADVANCE(282);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(287);
      END_STATE();
    case 9:
      if (lookahead == '0') ADVANCE(33);
      END_STATE();
    case 10:
      if (lookahead == '0') ADVANCE(283);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(287);
      END_STATE();
    case 11:
      if (lookahead == '0') ADVANCE(34);
      END_STATE();
    case 12:
      if (lookahead == 'F') ADVANCE(88);
      END_STATE();
    case 13:
      if (lookahead == 'I') ADVANCE(14);
      END_STATE();
    case 14:
      if (lookahead == 'N') ADVANCE(12);
      END_STATE();
    case 15:
      if (lookahead == 'N') ADVANCE(90);
      END_STATE();
    case 16:
      if (lookahead == 'N') ADVANCE(22);
      END_STATE();
    case 17:
      if (lookahead == '\\') ADVANCE(106);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(103);
      END_STATE();
    case 18:
      if (lookahead == '\\') ADVANCE(120);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(119);
      END_STATE();
    case 19:
      if (lookahead == '\\') ADVANCE(121);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(119);
      END_STATE();
    case 20:
      if (lookahead == 'a') ADVANCE(30);
      END_STATE();
    case 21:
      if (lookahead == 'a') ADVANCE(23);
      END_STATE();
    case 22:
      if (lookahead == 'a') ADVANCE(15);
      END_STATE();
    case 23:
      if (lookahead == 'b') ADVANCE(27);
      END_STATE();
    case 24:
      if (lookahead == 'e') ADVANCE(298);
      END_STATE();
    case 25:
      if (lookahead == 'h') ADVANCE(20);
      END_STATE();
    case 26:
      if (lookahead == 'h') ADVANCE(6);
      END_STATE();
    case 27:
      if (lookahead == 'l') ADVANCE(24);
      END_STATE();
    case 28:
      if (lookahead == 'r') ADVANCE(46);
      END_STATE();
    case 29:
      if (lookahead == 'r') ADVANCE(46);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(28);
      END_STATE();
    case 30:
      if (lookahead == 's') ADVANCE(26);
      END_STATE();
    case 31:
      if (lookahead == 't') ADVANCE(21);
      END_STATE();
    case 32:
      if (lookahead == '}') ADVANCE(113);
      if (lookahead != 0) ADVANCE(32);
      END_STATE();
    case 33:
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(4);
      END_STATE();
    case 34:
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(5);
      END_STATE();
    case 35:
      if (lookahead == '\'' ||
          lookahead == ',' ||
          lookahead == '`') ADVANCE(129);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(287);
      END_STATE();
    case 36:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(114);
      END_STATE();
    case 37:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(115);
      END_STATE();
    case 38:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(36);
      END_STATE();
    case 39:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(37);
      END_STATE();
    case 40:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(38);
      END_STATE();
    case 41:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(39);
      END_STATE();
    case 42:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(41);
      END_STATE();
    case 43:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(42);
      END_STATE();
    case 44:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(43);
      END_STATE();
    case 45:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(44);
      END_STATE();
    case 46:
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'Z') ||
          ('a' <= lookahead && lookahead <= 'z')) ADVANCE(102);
      END_STATE();
    case 47:
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(287);
      END_STATE();
    case 48:
      if (lookahead != 0 &&
          lookahead != '}') ADVANCE(32);
      END_STATE();
    case 49:
      if (lookahead != 0) ADVANCE(1);
      END_STATE();
    case 50:
      if (eof) ADVANCE(51);
      ADVANCE_MAP(
        '"', 1,
        '#', 2,
        '\'', 290,
        '(', 52,
        ')', 77,
        '+', 141,
        ',', 293,
        '-', 140,
        '.', 284,
        '0', 92,
        '1', 98,
        ';', 299,
        '?', 17,
        '[', 294,
        '\\', 35,
        ']', 295,
        '`', 291,
        'd', 188,
        'n', 202,
        't', 128,
      );
      if (('\t' <= lookahead && lookahead <= '\r') ||
          lookahead == ' ') SKIP(50);
      if (('2' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if (lookahead != 0) ADVANCE(287);
      END_STATE();
    case 51:
      ACCEPT_TOKEN(ts_builtin_sym_end);
      END_STATE();
    case 52:
      ACCEPT_TOKEN(anon_sym_LPAREN);
      END_STATE();
    case 53:
      ACCEPT_TOKEN(anon_sym_and);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 54:
      ACCEPT_TOKEN(anon_sym_catch);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 55:
      ACCEPT_TOKEN(anon_sym_cond);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(269);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 56:
      ACCEPT_TOKEN(anon_sym_condition_DASHcase);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 57:
      ACCEPT_TOKEN(anon_sym_defconst);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 58:
      ACCEPT_TOKEN(anon_sym_defvar);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 59:
      ACCEPT_TOKEN(anon_sym_function);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 60:
      ACCEPT_TOKEN(anon_sym_if);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 61:
      ACCEPT_TOKEN(anon_sym_interactive);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 62:
      ACCEPT_TOKEN(anon_sym_lambda);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 63:
      ACCEPT_TOKEN(anon_sym_let);
      if (lookahead == '*') ADVANCE(64);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 64:
      ACCEPT_TOKEN(anon_sym_let_STAR);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 65:
      ACCEPT_TOKEN(anon_sym_or);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 66:
      ACCEPT_TOKEN(anon_sym_prog1);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 67:
      ACCEPT_TOKEN(anon_sym_prog2);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 68:
      ACCEPT_TOKEN(anon_sym_progn);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 69:
      ACCEPT_TOKEN(anon_sym_quote);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 70:
      ACCEPT_TOKEN(anon_sym_save_DASHcurrent_DASHbuffer);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 71:
      ACCEPT_TOKEN(anon_sym_save_DASHexcursion);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 72:
      ACCEPT_TOKEN(anon_sym_save_DASHrestriction);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 73:
      ACCEPT_TOKEN(anon_sym_setq);
      if (lookahead == '-') ADVANCE(179);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 74:
      ACCEPT_TOKEN(anon_sym_setq_DASHdefault);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 75:
      ACCEPT_TOKEN(anon_sym_unwind_DASHprotect);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 76:
      ACCEPT_TOKEN(anon_sym_while);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 77:
      ACCEPT_TOKEN(anon_sym_RPAREN);
      END_STATE();
    case 78:
      ACCEPT_TOKEN(anon_sym_defun);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 79:
      ACCEPT_TOKEN(anon_sym_defsubst);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 80:
      ACCEPT_TOKEN(anon_sym_defmacro);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 81:
      ACCEPT_TOKEN(aux_sym_float_token1);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(131);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(82);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 82:
      ACCEPT_TOKEN(aux_sym_float_token1);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(286);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(82);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 83:
      ACCEPT_TOKEN(aux_sym_float_token1);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(134);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(82);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 84:
      ACCEPT_TOKEN(aux_sym_float_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(132);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 85:
      ACCEPT_TOKEN(aux_sym_float_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(135);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 86:
      ACCEPT_TOKEN(aux_sym_float_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 87:
      ACCEPT_TOKEN(aux_sym_float_token3);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(87);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 88:
      ACCEPT_TOKEN(aux_sym_float_token4);
      END_STATE();
    case 89:
      ACCEPT_TOKEN(aux_sym_float_token4);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 90:
      ACCEPT_TOKEN(aux_sym_float_token5);
      END_STATE();
    case 91:
      ACCEPT_TOKEN(aux_sym_float_token5);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 92:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '.') ADVANCE(99);
      if (lookahead == '\\') ADVANCE(8);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(143);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(93);
      if (lookahead == '\t' ||
          (0x0b <= lookahead && lookahead <= '\r') ||
          lookahead == ' ' ||
          lookahead == '"' ||
          lookahead == '#' ||
          ('\'' <= lookahead && lookahead <= ')') ||
          lookahead == ',' ||
          lookahead == ';' ||
          ('[' <= lookahead && lookahead <= ']') ||
          lookahead == '`') ADVANCE(9);
      if (lookahead != 0 &&
          (lookahead < '\t' || '\r' < lookahead)) ADVANCE(142);
      END_STATE();
    case 93:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '.') ADVANCE(101);
      if (lookahead == '0') ADVANCE(96);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(285);
      if (('1' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 94:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '.') ADVANCE(101);
      if (lookahead == '0') ADVANCE(97);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(285);
      if (('1' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 95:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '.') ADVANCE(101);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(285);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 96:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '.') ADVANCE(101);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(130);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 97:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '.') ADVANCE(101);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(133);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 98:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '.') ADVANCE(100);
      if (lookahead == '\\') ADVANCE(10);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(145);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(94);
      if (lookahead == '\t' ||
          (0x0b <= lookahead && lookahead <= '\r') ||
          lookahead == ' ' ||
          lookahead == '"' ||
          lookahead == '#' ||
          ('\'' <= lookahead && lookahead <= ')') ||
          lookahead == ',' ||
          lookahead == ';' ||
          ('[' <= lookahead && lookahead <= ']') ||
          lookahead == '`') ADVANCE(11);
      if (lookahead != 0 &&
          (lookahead < '\t' || '\r' < lookahead)) ADVANCE(144);
      END_STATE();
    case 99:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '0') ADVANCE(81);
      if (lookahead == '\\') ADVANCE(47);
      if (('1' <= lookahead && lookahead <= '9')) ADVANCE(82);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 100:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '0') ADVANCE(83);
      if (lookahead == '\\') ADVANCE(47);
      if (('1' <= lookahead && lookahead <= '9')) ADVANCE(82);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 101:
      ACCEPT_TOKEN(aux_sym_integer_token1);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(82);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 102:
      ACCEPT_TOKEN(aux_sym_integer_token2);
      END_STATE();
    case 103:
      ACCEPT_TOKEN(aux_sym_char_token1);
      END_STATE();
    case 104:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (lookahead == '-') ADVANCE(19);
      END_STATE();
    case 105:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (lookahead == '-') ADVANCE(18);
      END_STATE();
    case 106:
      ACCEPT_TOKEN(aux_sym_char_token1);
      ADVANCE_MAP(
        'M', 104,
        'N', 108,
        'U', 110,
        '^', 107,
        'u', 112,
        'x', 111,
        'A', 105,
        'C', 105,
        'H', 105,
        'S', 105,
        's', 105,
      );
      if (('0' <= lookahead && lookahead <= '7')) ADVANCE(109);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(103);
      END_STATE();
    case 107:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (lookahead == '\\') ADVANCE(120);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(119);
      END_STATE();
    case 108:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (lookahead == '{') ADVANCE(48);
      END_STATE();
    case 109:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (('0' <= lookahead && lookahead <= '7')) ADVANCE(118);
      END_STATE();
    case 110:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(45);
      END_STATE();
    case 111:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(116);
      END_STATE();
    case 112:
      ACCEPT_TOKEN(aux_sym_char_token1);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(40);
      END_STATE();
    case 113:
      ACCEPT_TOKEN(aux_sym_char_token2);
      END_STATE();
    case 114:
      ACCEPT_TOKEN(aux_sym_char_token3);
      END_STATE();
    case 115:
      ACCEPT_TOKEN(aux_sym_char_token4);
      END_STATE();
    case 116:
      ACCEPT_TOKEN(aux_sym_char_token5);
      if (('0' <= lookahead && lookahead <= '9') ||
          ('A' <= lookahead && lookahead <= 'F') ||
          ('a' <= lookahead && lookahead <= 'f')) ADVANCE(116);
      END_STATE();
    case 117:
      ACCEPT_TOKEN(aux_sym_char_token6);
      END_STATE();
    case 118:
      ACCEPT_TOKEN(aux_sym_char_token6);
      if (('0' <= lookahead && lookahead <= '7')) ADVANCE(117);
      END_STATE();
    case 119:
      ACCEPT_TOKEN(aux_sym_char_token7);
      END_STATE();
    case 120:
      ACCEPT_TOKEN(aux_sym_char_token7);
      ADVANCE_MAP(
        ';', 119,
        '^', 18,
        'A', 7,
        'C', 7,
        'H', 7,
        'M', 7,
        'S', 7,
        's', 7,
      );
      END_STATE();
    case 121:
      ACCEPT_TOKEN(aux_sym_char_token7);
      ADVANCE_MAP(
        ';', 119,
        '^', 18,
        'A', 7,
        'C', 7,
        'H', 7,
        'M', 7,
        'S', 7,
        's', 7,
      );
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(124);
      END_STATE();
    case 122:
      ACCEPT_TOKEN(aux_sym_char_token8);
      END_STATE();
    case 123:
      ACCEPT_TOKEN(aux_sym_char_token8);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(122);
      END_STATE();
    case 124:
      ACCEPT_TOKEN(aux_sym_char_token8);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(123);
      END_STATE();
    case 125:
      ACCEPT_TOKEN(sym_string);
      END_STATE();
    case 126:
      ACCEPT_TOKEN(sym_byte_compiled_file_name);
      END_STATE();
    case 127:
      ACCEPT_TOKEN(anon_sym_nil);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 128:
      ACCEPT_TOKEN(anon_sym_t);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 129:
      ACCEPT_TOKEN(aux_sym_symbol_token1);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 130:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '+') ADVANCE(151);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 131:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '+') ADVANCE(151);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(87);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 132:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '+') ADVANCE(151);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 133:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '+') ADVANCE(148);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 134:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '+') ADVANCE(148);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(87);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 135:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '+') ADVANCE(148);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 136:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '-') ADVANCE(167);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 137:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '-') ADVANCE(237);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 138:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '-') ADVANCE(163);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 139:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '-') ADVANCE(170);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 140:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '.') ADVANCE(284);
      if (lookahead == '0') ADVANCE(92);
      if (lookahead == '1') ADVANCE(98);
      if (lookahead == '\\') ADVANCE(47);
      if (('2' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 141:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '.') ADVANCE(284);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(95);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 142:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '0') ADVANCE(282);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 143:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '0') ADVANCE(84);
      if (lookahead == '\\') ADVANCE(47);
      if (('1' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 144:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '0') ADVANCE(283);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 145:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '0') ADVANCE(85);
      if (lookahead == '\\') ADVANCE(47);
      if (('1' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 146:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '1') ADVANCE(66);
      if (lookahead == '2') ADVANCE(67);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(68);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 147:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == 'F') ADVANCE(89);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 148:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == 'I') ADVANCE(149);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 149:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == 'N') ADVANCE(147);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 150:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == 'N') ADVANCE(91);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 151:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == 'N') ADVANCE(157);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 152:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(255);
      if (lookahead == 'o') ADVANCE(223);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 153:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(214);
      if (lookahead == 'e') ADVANCE(256);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 154:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(278);
      if (lookahead == 'e') ADVANCE(257);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 155:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(62);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 156:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(168);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 157:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(150);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 158:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(252);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 159:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(241);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 160:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(275);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 161:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'a') ADVANCE(171);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 162:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'b') ADVANCE(178);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 163:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'b') ADVANCE(274);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 164:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'b') ADVANCE(251);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 165:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(200);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 166:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(230);
      if (lookahead == 'm') ADVANCE(156);
      if (lookahead == 's') ADVANCE(272);
      if (lookahead == 'u') ADVANCE(218);
      if (lookahead == 'v') ADVANCE(159);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 167:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(276);
      if (lookahead == 'e') ADVANCE(281);
      if (lookahead == 'r') ADVANCE(191);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 168:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(244);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 169:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(263);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 170:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(158);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 171:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(265);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 172:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(261);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 173:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(277);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 174:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'c') ADVANCE(270);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 175:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'd') ADVANCE(53);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 176:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'd') ADVANCE(55);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 177:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'd') ADVANCE(137);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 178:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'd') ADVANCE(155);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 179:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'd') ADVANCE(186);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 180:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(194);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 181:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(136);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 182:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(69);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 183:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(76);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 184:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(61);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 185:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(56);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 186:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(197);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 187:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(248);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 188:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(195);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 189:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(227);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 190:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(242);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 191:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(253);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 192:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'e') ADVANCE(172);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 193:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'f') ADVANCE(60);
      if (lookahead == 'n') ADVANCE(262);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 194:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'f') ADVANCE(166);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 195:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'f') ADVANCE(215);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 196:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'f') ADVANCE(198);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 197:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'f') ADVANCE(160);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 198:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'f') ADVANCE(190);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 199:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'g') ADVANCE(146);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 200:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'h') ADVANCE(54);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 201:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'h') ADVANCE(203);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 202:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(211);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 203:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(212);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 204:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(279);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 205:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(232);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 206:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(226);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 207:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(233);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 208:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(234);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 209:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(235);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 210:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'i') ADVANCE(174);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 211:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'l') ADVANCE(127);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 212:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'l') ADVANCE(183);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 213:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'l') ADVANCE(260);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 214:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'm') ADVANCE(162);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 215:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'm') ADVANCE(156);
      if (lookahead == 's') ADVANCE(272);
      if (lookahead == 'u') ADVANCE(218);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 216:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(175);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 217:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(280);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 218:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(78);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 219:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(250);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 220:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(59);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 221:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(71);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 222:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(72);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 223:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(176);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 224:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(169);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 225:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(139);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 226:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(177);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 227:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'n') ADVANCE(266);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 228:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(199);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 229:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(80);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 230:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(219);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 231:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(264);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 232:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(220);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 233:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(225);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 234:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(221);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 235:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(222);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 236:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'o') ADVANCE(267);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 237:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'p') ADVANCE(249);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 238:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'q') ADVANCE(73);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 239:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(65);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 240:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(228);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 241:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(58);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 242:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(70);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 243:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(254);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 244:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(229);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 245:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(210);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 246:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(189);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 247:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(246);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 248:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(161);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 249:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'r') ADVANCE(236);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 250:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 's') ADVANCE(258);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 251:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 's') ADVANCE(259);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 252:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 's') ADVANCE(185);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 253:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 's') ADVANCE(268);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 254:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 's') ADVANCE(208);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 255:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(165);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 256:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(63);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 257:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(238);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 258:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(57);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 259:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(79);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 260:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(74);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 261:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(75);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 262:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(187);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 263:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(205);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 264:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(182);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 265:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(204);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 266:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(138);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 267:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(192);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 268:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(245);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 269:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(207);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 270:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 't') ADVANCE(209);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 271:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'u') ADVANCE(231);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 272:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'u') ADVANCE(164);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 273:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'u') ADVANCE(224);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 274:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'u') ADVANCE(196);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 275:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'u') ADVANCE(213);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 276:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'u') ADVANCE(247);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 277:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'u') ADVANCE(243);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 278:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'v') ADVANCE(181);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 279:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'v') ADVANCE(184);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 280:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'w') ADVANCE(206);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 281:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'x') ADVANCE(173);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 282:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(132);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 283:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (lookahead == 'E' ||
          lookahead == 'e') ADVANCE(135);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 284:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(82);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 285:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(86);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 286:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if (('0' <= lookahead && lookahead <= '9')) ADVANCE(87);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 287:
      ACCEPT_TOKEN(aux_sym_symbol_token2);
      if (lookahead == '\\') ADVANCE(47);
      if ((!eof && set_contains(aux_sym_symbol_token2_character_set_2, 10, lookahead))) ADVANCE(287);
      END_STATE();
    case 288:
      ACCEPT_TOKEN(anon_sym_POUND_POUND);
      END_STATE();
    case 289:
      ACCEPT_TOKEN(anon_sym_POUND_SQUOTE);
      END_STATE();
    case 290:
      ACCEPT_TOKEN(anon_sym_SQUOTE);
      END_STATE();
    case 291:
      ACCEPT_TOKEN(anon_sym_BQUOTE);
      END_STATE();
    case 292:
      ACCEPT_TOKEN(anon_sym_COMMA_AT);
      END_STATE();
    case 293:
      ACCEPT_TOKEN(anon_sym_COMMA);
      if (lookahead == '@') ADVANCE(292);
      END_STATE();
    case 294:
      ACCEPT_TOKEN(anon_sym_LBRACK);
      END_STATE();
    case 295:
      ACCEPT_TOKEN(anon_sym_RBRACK);
      END_STATE();
    case 296:
      ACCEPT_TOKEN(anon_sym_POUND_LBRACK);
      END_STATE();
    case 297:
      ACCEPT_TOKEN(anon_sym_POUND_LPAREN);
      END_STATE();
    case 298:
      ACCEPT_TOKEN(anon_sym_POUNDs_LPARENhash_DASHtable);
      END_STATE();
    case 299:
      ACCEPT_TOKEN(sym_comment);
      if (lookahead != 0 &&
          lookahead != '\n') ADVANCE(299);
      END_STATE();
    default:
      return false;
  }
}

static const TSLexerMode ts_lex_modes[STATE_COUNT] = {
  [0] = {.lex_state = 0},
  [1] = {.lex_state = 50},
  [2] = {.lex_state = 0},
  [3] = {.lex_state = 50},
  [4] = {.lex_state = 50},
  [5] = {.lex_state = 50},
  [6] = {.lex_state = 50},
  [7] = {.lex_state = 50},
  [8] = {.lex_state = 50},
  [9] = {.lex_state = 50},
  [10] = {.lex_state = 50},
  [11] = {.lex_state = 50},
  [12] = {.lex_state = 50},
  [13] = {.lex_state = 50},
  [14] = {.lex_state = 50},
  [15] = {.lex_state = 50},
  [16] = {.lex_state = 50},
  [17] = {.lex_state = 50},
  [18] = {.lex_state = 50},
  [19] = {.lex_state = 50},
  [20] = {.lex_state = 50},
  [21] = {.lex_state = 50},
  [22] = {.lex_state = 50},
  [23] = {.lex_state = 50},
  [24] = {.lex_state = 50},
  [25] = {.lex_state = 50},
  [26] = {.lex_state = 50},
  [27] = {.lex_state = 50},
  [28] = {.lex_state = 50},
  [29] = {.lex_state = 50},
  [30] = {.lex_state = 50},
  [31] = {.lex_state = 50},
  [32] = {.lex_state = 50},
  [33] = {.lex_state = 50},
  [34] = {.lex_state = 50},
  [35] = {.lex_state = 50},
  [36] = {.lex_state = 50},
  [37] = {.lex_state = 50},
  [38] = {.lex_state = 50},
  [39] = {.lex_state = 50},
  [40] = {.lex_state = 50},
  [41] = {.lex_state = 50},
  [42] = {.lex_state = 50},
  [43] = {.lex_state = 50},
  [44] = {.lex_state = 50},
  [45] = {.lex_state = 50},
  [46] = {.lex_state = 50},
  [47] = {.lex_state = 50},
  [48] = {.lex_state = 50},
  [49] = {.lex_state = 50},
  [50] = {.lex_state = 50},
  [51] = {.lex_state = 50},
  [52] = {.lex_state = 50},
  [53] = {.lex_state = 50},
  [54] = {.lex_state = 50},
  [55] = {.lex_state = 50},
  [56] = {.lex_state = 50},
  [57] = {.lex_state = 50},
  [58] = {.lex_state = 50},
  [59] = {.lex_state = 50},
  [60] = {.lex_state = 50},
  [61] = {.lex_state = 50},
  [62] = {.lex_state = 50},
  [63] = {.lex_state = 50},
  [64] = {.lex_state = 50},
  [65] = {.lex_state = 50},
  [66] = {.lex_state = 50},
  [67] = {.lex_state = 50},
  [68] = {.lex_state = 50},
  [69] = {.lex_state = 50},
  [70] = {.lex_state = 50},
  [71] = {.lex_state = 50},
  [72] = {.lex_state = 0},
  [73] = {.lex_state = 0},
};

static const uint16_t ts_parse_table[LARGE_STATE_COUNT][SYMBOL_COUNT] = {
  [STATE(0)] = {
    [ts_builtin_sym_end] = ACTIONS(1),
    [anon_sym_LPAREN] = ACTIONS(1),
    [anon_sym_and] = ACTIONS(1),
    [anon_sym_catch] = ACTIONS(1),
    [anon_sym_cond] = ACTIONS(1),
    [anon_sym_condition_DASHcase] = ACTIONS(1),
    [anon_sym_defconst] = ACTIONS(1),
    [anon_sym_defvar] = ACTIONS(1),
    [anon_sym_function] = ACTIONS(1),
    [anon_sym_if] = ACTIONS(1),
    [anon_sym_interactive] = ACTIONS(1),
    [anon_sym_lambda] = ACTIONS(1),
    [anon_sym_let] = ACTIONS(1),
    [anon_sym_let_STAR] = ACTIONS(1),
    [anon_sym_or] = ACTIONS(1),
    [anon_sym_prog1] = ACTIONS(1),
    [anon_sym_prog2] = ACTIONS(1),
    [anon_sym_progn] = ACTIONS(1),
    [anon_sym_quote] = ACTIONS(1),
    [anon_sym_save_DASHcurrent_DASHbuffer] = ACTIONS(1),
    [anon_sym_save_DASHexcursion] = ACTIONS(1),
    [anon_sym_save_DASHrestriction] = ACTIONS(1),
    [anon_sym_setq] = ACTIONS(1),
    [anon_sym_setq_DASHdefault] = ACTIONS(1),
    [anon_sym_unwind_DASHprotect] = ACTIONS(1),
    [anon_sym_while] = ACTIONS(1),
    [anon_sym_RPAREN] = ACTIONS(1),
    [anon_sym_defun] = ACTIONS(1),
    [anon_sym_defsubst] = ACTIONS(1),
    [anon_sym_defmacro] = ACTIONS(1),
    [aux_sym_float_token1] = ACTIONS(1),
    [aux_sym_float_token2] = ACTIONS(1),
    [aux_sym_float_token3] = ACTIONS(1),
    [aux_sym_float_token4] = ACTIONS(1),
    [aux_sym_float_token5] = ACTIONS(1),
    [aux_sym_integer_token1] = ACTIONS(1),
    [aux_sym_integer_token2] = ACTIONS(1),
    [aux_sym_char_token1] = ACTIONS(1),
    [aux_sym_char_token2] = ACTIONS(1),
    [aux_sym_char_token3] = ACTIONS(1),
    [aux_sym_char_token4] = ACTIONS(1),
    [aux_sym_char_token5] = ACTIONS(1),
    [aux_sym_char_token6] = ACTIONS(1),
    [aux_sym_char_token7] = ACTIONS(1),
    [aux_sym_char_token8] = ACTIONS(1),
    [sym_string] = ACTIONS(1),
    [sym_byte_compiled_file_name] = ACTIONS(1),
    [anon_sym_nil] = ACTIONS(1),
    [anon_sym_t] = ACTIONS(1),
    [aux_sym_symbol_token1] = ACTIONS(1),
    [aux_sym_symbol_token2] = ACTIONS(1),
    [anon_sym_POUND_POUND] = ACTIONS(1),
    [anon_sym_POUND_SQUOTE] = ACTIONS(1),
    [anon_sym_SQUOTE] = ACTIONS(1),
    [anon_sym_BQUOTE] = ACTIONS(1),
    [anon_sym_COMMA_AT] = ACTIONS(1),
    [anon_sym_COMMA] = ACTIONS(1),
    [anon_sym_LBRACK] = ACTIONS(1),
    [anon_sym_RBRACK] = ACTIONS(1),
    [anon_sym_POUND_LBRACK] = ACTIONS(1),
    [anon_sym_POUND_LPAREN] = ACTIONS(1),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(1),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(1)] = {
    [sym_source_file] = STATE(72),
    [sym__sexp] = STATE(8),
    [sym_special_form] = STATE(8),
    [sym_function_definition] = STATE(8),
    [sym_macro_definition] = STATE(8),
    [sym__atom] = STATE(8),
    [sym_float] = STATE(8),
    [sym_integer] = STATE(8),
    [sym_char] = STATE(8),
    [sym_symbol] = STATE(8),
    [sym_quote] = STATE(8),
    [sym_unquote_splice] = STATE(8),
    [sym_unquote] = STATE(8),
    [sym_list] = STATE(8),
    [sym_vector] = STATE(8),
    [sym_bytecode] = STATE(8),
    [sym_string_text_properties] = STATE(8),
    [sym_hash_table] = STATE(8),
    [aux_sym_source_file_repeat1] = STATE(8),
    [ts_builtin_sym_end] = ACTIONS(5),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(21),
    [sym_byte_compiled_file_name] = ACTIONS(21),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(2)] = {
    [sym__sexp] = STATE(10),
    [sym_special_form] = STATE(10),
    [sym_function_definition] = STATE(10),
    [sym_macro_definition] = STATE(10),
    [sym__atom] = STATE(10),
    [sym_float] = STATE(10),
    [sym_integer] = STATE(10),
    [sym_char] = STATE(10),
    [sym_symbol] = STATE(10),
    [sym_quote] = STATE(10),
    [sym_unquote_splice] = STATE(10),
    [sym_unquote] = STATE(10),
    [sym_list] = STATE(10),
    [sym_vector] = STATE(10),
    [sym_bytecode] = STATE(10),
    [sym_string_text_properties] = STATE(10),
    [sym_hash_table] = STATE(10),
    [aux_sym_source_file_repeat1] = STATE(10),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_and] = ACTIONS(39),
    [anon_sym_catch] = ACTIONS(39),
    [anon_sym_cond] = ACTIONS(39),
    [anon_sym_condition_DASHcase] = ACTIONS(39),
    [anon_sym_defconst] = ACTIONS(39),
    [anon_sym_defvar] = ACTIONS(39),
    [anon_sym_function] = ACTIONS(39),
    [anon_sym_if] = ACTIONS(39),
    [anon_sym_interactive] = ACTIONS(39),
    [anon_sym_lambda] = ACTIONS(39),
    [anon_sym_let] = ACTIONS(39),
    [anon_sym_let_STAR] = ACTIONS(39),
    [anon_sym_or] = ACTIONS(39),
    [anon_sym_prog1] = ACTIONS(39),
    [anon_sym_prog2] = ACTIONS(39),
    [anon_sym_progn] = ACTIONS(39),
    [anon_sym_quote] = ACTIONS(39),
    [anon_sym_save_DASHcurrent_DASHbuffer] = ACTIONS(39),
    [anon_sym_save_DASHexcursion] = ACTIONS(39),
    [anon_sym_save_DASHrestriction] = ACTIONS(39),
    [anon_sym_setq] = ACTIONS(39),
    [anon_sym_setq_DASHdefault] = ACTIONS(39),
    [anon_sym_unwind_DASHprotect] = ACTIONS(39),
    [anon_sym_while] = ACTIONS(39),
    [anon_sym_RPAREN] = ACTIONS(41),
    [anon_sym_defun] = ACTIONS(43),
    [anon_sym_defsubst] = ACTIONS(43),
    [anon_sym_defmacro] = ACTIONS(45),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(47),
    [sym_byte_compiled_file_name] = ACTIONS(47),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(3)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [ts_builtin_sym_end] = ACTIONS(49),
    [anon_sym_LPAREN] = ACTIONS(51),
    [anon_sym_RPAREN] = ACTIONS(49),
    [anon_sym_defun] = ACTIONS(54),
    [anon_sym_defsubst] = ACTIONS(54),
    [anon_sym_defmacro] = ACTIONS(54),
    [aux_sym_float_token1] = ACTIONS(57),
    [aux_sym_float_token2] = ACTIONS(57),
    [aux_sym_float_token3] = ACTIONS(57),
    [aux_sym_float_token4] = ACTIONS(57),
    [aux_sym_float_token5] = ACTIONS(57),
    [aux_sym_integer_token1] = ACTIONS(60),
    [aux_sym_integer_token2] = ACTIONS(63),
    [aux_sym_char_token1] = ACTIONS(66),
    [aux_sym_char_token2] = ACTIONS(69),
    [aux_sym_char_token3] = ACTIONS(69),
    [aux_sym_char_token4] = ACTIONS(69),
    [aux_sym_char_token5] = ACTIONS(69),
    [aux_sym_char_token6] = ACTIONS(66),
    [aux_sym_char_token7] = ACTIONS(66),
    [aux_sym_char_token8] = ACTIONS(69),
    [sym_string] = ACTIONS(72),
    [sym_byte_compiled_file_name] = ACTIONS(72),
    [anon_sym_nil] = ACTIONS(54),
    [anon_sym_t] = ACTIONS(54),
    [aux_sym_symbol_token1] = ACTIONS(54),
    [aux_sym_symbol_token2] = ACTIONS(54),
    [anon_sym_POUND_POUND] = ACTIONS(75),
    [anon_sym_POUND_SQUOTE] = ACTIONS(78),
    [anon_sym_SQUOTE] = ACTIONS(78),
    [anon_sym_BQUOTE] = ACTIONS(78),
    [anon_sym_COMMA_AT] = ACTIONS(81),
    [anon_sym_COMMA] = ACTIONS(84),
    [anon_sym_LBRACK] = ACTIONS(87),
    [anon_sym_RBRACK] = ACTIONS(49),
    [anon_sym_POUND_LBRACK] = ACTIONS(90),
    [anon_sym_POUND_LPAREN] = ACTIONS(93),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(96),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(4)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(99),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(5)] = {
    [sym__sexp] = STATE(11),
    [sym_special_form] = STATE(11),
    [sym_function_definition] = STATE(11),
    [sym_macro_definition] = STATE(11),
    [sym__atom] = STATE(11),
    [sym_float] = STATE(11),
    [sym_integer] = STATE(11),
    [sym_char] = STATE(11),
    [sym_symbol] = STATE(11),
    [sym_quote] = STATE(11),
    [sym_unquote_splice] = STATE(11),
    [sym_unquote] = STATE(11),
    [sym_list] = STATE(11),
    [sym_vector] = STATE(11),
    [sym_bytecode] = STATE(11),
    [sym_string_text_properties] = STATE(11),
    [sym_hash_table] = STATE(11),
    [aux_sym_source_file_repeat1] = STATE(11),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(103),
    [sym_byte_compiled_file_name] = ACTIONS(103),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_RBRACK] = ACTIONS(105),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(6)] = {
    [sym__sexp] = STATE(12),
    [sym_special_form] = STATE(12),
    [sym_function_definition] = STATE(12),
    [sym_macro_definition] = STATE(12),
    [sym__atom] = STATE(12),
    [sym_float] = STATE(12),
    [sym_integer] = STATE(12),
    [sym_char] = STATE(12),
    [sym_symbol] = STATE(12),
    [sym_quote] = STATE(12),
    [sym_unquote_splice] = STATE(12),
    [sym_unquote] = STATE(12),
    [sym_list] = STATE(12),
    [sym_vector] = STATE(12),
    [sym_bytecode] = STATE(12),
    [sym_string_text_properties] = STATE(12),
    [sym_hash_table] = STATE(12),
    [aux_sym_source_file_repeat1] = STATE(12),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(107),
    [sym_byte_compiled_file_name] = ACTIONS(107),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_RBRACK] = ACTIONS(109),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(7)] = {
    [sym__sexp] = STATE(14),
    [sym_special_form] = STATE(14),
    [sym_function_definition] = STATE(14),
    [sym_macro_definition] = STATE(14),
    [sym__atom] = STATE(14),
    [sym_float] = STATE(14),
    [sym_integer] = STATE(14),
    [sym_char] = STATE(14),
    [sym_symbol] = STATE(14),
    [sym_quote] = STATE(14),
    [sym_unquote_splice] = STATE(14),
    [sym_unquote] = STATE(14),
    [sym_list] = STATE(14),
    [sym_vector] = STATE(14),
    [sym_bytecode] = STATE(14),
    [sym_string_text_properties] = STATE(14),
    [sym_hash_table] = STATE(14),
    [aux_sym_source_file_repeat1] = STATE(14),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(111),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(113),
    [sym_byte_compiled_file_name] = ACTIONS(113),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(8)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [ts_builtin_sym_end] = ACTIONS(115),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(9)] = {
    [sym__sexp] = STATE(16),
    [sym_special_form] = STATE(16),
    [sym_function_definition] = STATE(16),
    [sym_macro_definition] = STATE(16),
    [sym__atom] = STATE(16),
    [sym_float] = STATE(16),
    [sym_integer] = STATE(16),
    [sym_char] = STATE(16),
    [sym_symbol] = STATE(16),
    [sym_quote] = STATE(16),
    [sym_unquote_splice] = STATE(16),
    [sym_unquote] = STATE(16),
    [sym_list] = STATE(16),
    [sym_vector] = STATE(16),
    [sym_bytecode] = STATE(16),
    [sym_string_text_properties] = STATE(16),
    [sym_hash_table] = STATE(16),
    [aux_sym_source_file_repeat1] = STATE(16),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(117),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(119),
    [sym_byte_compiled_file_name] = ACTIONS(119),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(10)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(121),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(11)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_RBRACK] = ACTIONS(123),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(12)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_RBRACK] = ACTIONS(125),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(13)] = {
    [sym__sexp] = STATE(18),
    [sym_special_form] = STATE(18),
    [sym_function_definition] = STATE(18),
    [sym_macro_definition] = STATE(18),
    [sym__atom] = STATE(18),
    [sym_float] = STATE(18),
    [sym_integer] = STATE(18),
    [sym_char] = STATE(18),
    [sym_symbol] = STATE(18),
    [sym_quote] = STATE(18),
    [sym_unquote_splice] = STATE(18),
    [sym_unquote] = STATE(18),
    [sym_list] = STATE(18),
    [sym_vector] = STATE(18),
    [sym_bytecode] = STATE(18),
    [sym_string_text_properties] = STATE(18),
    [sym_hash_table] = STATE(18),
    [aux_sym_source_file_repeat1] = STATE(18),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(127),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(129),
    [sym_byte_compiled_file_name] = ACTIONS(129),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(14)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(131),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(15)] = {
    [sym__sexp] = STATE(20),
    [sym_special_form] = STATE(20),
    [sym_function_definition] = STATE(20),
    [sym_macro_definition] = STATE(20),
    [sym__atom] = STATE(20),
    [sym_float] = STATE(20),
    [sym_integer] = STATE(20),
    [sym_char] = STATE(20),
    [sym_symbol] = STATE(20),
    [sym_quote] = STATE(20),
    [sym_unquote_splice] = STATE(20),
    [sym_unquote] = STATE(20),
    [sym_list] = STATE(20),
    [sym_vector] = STATE(20),
    [sym_bytecode] = STATE(20),
    [sym_string_text_properties] = STATE(20),
    [sym_hash_table] = STATE(20),
    [aux_sym_source_file_repeat1] = STATE(21),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(133),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(135),
    [sym_byte_compiled_file_name] = ACTIONS(137),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(16)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(139),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(17)] = {
    [sym__sexp] = STATE(23),
    [sym_special_form] = STATE(23),
    [sym_function_definition] = STATE(23),
    [sym_macro_definition] = STATE(23),
    [sym__atom] = STATE(23),
    [sym_float] = STATE(23),
    [sym_integer] = STATE(23),
    [sym_char] = STATE(23),
    [sym_symbol] = STATE(23),
    [sym_quote] = STATE(23),
    [sym_unquote_splice] = STATE(23),
    [sym_unquote] = STATE(23),
    [sym_list] = STATE(23),
    [sym_vector] = STATE(23),
    [sym_bytecode] = STATE(23),
    [sym_string_text_properties] = STATE(23),
    [sym_hash_table] = STATE(23),
    [aux_sym_source_file_repeat1] = STATE(24),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(141),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(143),
    [sym_byte_compiled_file_name] = ACTIONS(145),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(18)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(147),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(19)] = {
    [sym__sexp] = STATE(25),
    [sym_special_form] = STATE(25),
    [sym_function_definition] = STATE(25),
    [sym_macro_definition] = STATE(25),
    [sym__atom] = STATE(25),
    [sym_float] = STATE(25),
    [sym_integer] = STATE(25),
    [sym_char] = STATE(25),
    [sym_symbol] = STATE(25),
    [sym_quote] = STATE(25),
    [sym_unquote_splice] = STATE(25),
    [sym_unquote] = STATE(25),
    [sym_list] = STATE(25),
    [sym_vector] = STATE(25),
    [sym_bytecode] = STATE(25),
    [sym_string_text_properties] = STATE(25),
    [sym_hash_table] = STATE(25),
    [aux_sym_source_file_repeat1] = STATE(25),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(149),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(151),
    [sym_byte_compiled_file_name] = ACTIONS(151),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(20)] = {
    [sym__sexp] = STATE(4),
    [sym_special_form] = STATE(4),
    [sym_function_definition] = STATE(4),
    [sym_macro_definition] = STATE(4),
    [sym__atom] = STATE(4),
    [sym_float] = STATE(4),
    [sym_integer] = STATE(4),
    [sym_char] = STATE(4),
    [sym_symbol] = STATE(4),
    [sym_quote] = STATE(4),
    [sym_unquote_splice] = STATE(4),
    [sym_unquote] = STATE(4),
    [sym_list] = STATE(4),
    [sym_vector] = STATE(4),
    [sym_bytecode] = STATE(4),
    [sym_string_text_properties] = STATE(4),
    [sym_hash_table] = STATE(4),
    [aux_sym_source_file_repeat1] = STATE(4),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(153),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(155),
    [sym_byte_compiled_file_name] = ACTIONS(157),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(21)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(159),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(22)] = {
    [sym__sexp] = STATE(28),
    [sym_special_form] = STATE(28),
    [sym_function_definition] = STATE(28),
    [sym_macro_definition] = STATE(28),
    [sym__atom] = STATE(28),
    [sym_float] = STATE(28),
    [sym_integer] = STATE(28),
    [sym_char] = STATE(28),
    [sym_symbol] = STATE(28),
    [sym_quote] = STATE(28),
    [sym_unquote_splice] = STATE(28),
    [sym_unquote] = STATE(28),
    [sym_list] = STATE(28),
    [sym_vector] = STATE(28),
    [sym_bytecode] = STATE(28),
    [sym_string_text_properties] = STATE(28),
    [sym_hash_table] = STATE(28),
    [aux_sym_source_file_repeat1] = STATE(28),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(161),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(163),
    [sym_byte_compiled_file_name] = ACTIONS(163),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(23)] = {
    [sym__sexp] = STATE(30),
    [sym_special_form] = STATE(30),
    [sym_function_definition] = STATE(30),
    [sym_macro_definition] = STATE(30),
    [sym__atom] = STATE(30),
    [sym_float] = STATE(30),
    [sym_integer] = STATE(30),
    [sym_char] = STATE(30),
    [sym_symbol] = STATE(30),
    [sym_quote] = STATE(30),
    [sym_unquote_splice] = STATE(30),
    [sym_unquote] = STATE(30),
    [sym_list] = STATE(30),
    [sym_vector] = STATE(30),
    [sym_bytecode] = STATE(30),
    [sym_string_text_properties] = STATE(30),
    [sym_hash_table] = STATE(30),
    [aux_sym_source_file_repeat1] = STATE(30),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(165),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(167),
    [sym_byte_compiled_file_name] = ACTIONS(169),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(24)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(171),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(25)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(173),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(26)] = {
    [sym__sexp] = STATE(29),
    [sym_special_form] = STATE(29),
    [sym_function_definition] = STATE(29),
    [sym_macro_definition] = STATE(29),
    [sym__atom] = STATE(29),
    [sym_float] = STATE(29),
    [sym_integer] = STATE(29),
    [sym_char] = STATE(29),
    [sym_symbol] = STATE(29),
    [sym_quote] = STATE(29),
    [sym_unquote_splice] = STATE(29),
    [sym_unquote] = STATE(29),
    [sym_list] = STATE(29),
    [sym_vector] = STATE(29),
    [sym_bytecode] = STATE(29),
    [sym_string_text_properties] = STATE(29),
    [sym_hash_table] = STATE(29),
    [aux_sym_source_file_repeat1] = STATE(29),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(175),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(177),
    [sym_byte_compiled_file_name] = ACTIONS(177),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(27)] = {
    [sym__sexp] = STATE(31),
    [sym_special_form] = STATE(31),
    [sym_function_definition] = STATE(31),
    [sym_macro_definition] = STATE(31),
    [sym__atom] = STATE(31),
    [sym_float] = STATE(31),
    [sym_integer] = STATE(31),
    [sym_char] = STATE(31),
    [sym_symbol] = STATE(31),
    [sym_quote] = STATE(31),
    [sym_unquote_splice] = STATE(31),
    [sym_unquote] = STATE(31),
    [sym_list] = STATE(31),
    [sym_vector] = STATE(31),
    [sym_bytecode] = STATE(31),
    [sym_string_text_properties] = STATE(31),
    [sym_hash_table] = STATE(31),
    [aux_sym_source_file_repeat1] = STATE(31),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(179),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(181),
    [sym_byte_compiled_file_name] = ACTIONS(181),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(28)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(183),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(29)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(185),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(30)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(187),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(31)] = {
    [sym__sexp] = STATE(3),
    [sym_special_form] = STATE(3),
    [sym_function_definition] = STATE(3),
    [sym_macro_definition] = STATE(3),
    [sym__atom] = STATE(3),
    [sym_float] = STATE(3),
    [sym_integer] = STATE(3),
    [sym_char] = STATE(3),
    [sym_symbol] = STATE(3),
    [sym_quote] = STATE(3),
    [sym_unquote_splice] = STATE(3),
    [sym_unquote] = STATE(3),
    [sym_list] = STATE(3),
    [sym_vector] = STATE(3),
    [sym_bytecode] = STATE(3),
    [sym_string_text_properties] = STATE(3),
    [sym_hash_table] = STATE(3),
    [aux_sym_source_file_repeat1] = STATE(3),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_RPAREN] = ACTIONS(189),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(101),
    [sym_byte_compiled_file_name] = ACTIONS(101),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(32)] = {
    [sym__sexp] = STATE(43),
    [sym_special_form] = STATE(43),
    [sym_function_definition] = STATE(43),
    [sym_macro_definition] = STATE(43),
    [sym__atom] = STATE(43),
    [sym_float] = STATE(43),
    [sym_integer] = STATE(43),
    [sym_char] = STATE(43),
    [sym_symbol] = STATE(43),
    [sym_quote] = STATE(43),
    [sym_unquote_splice] = STATE(43),
    [sym_unquote] = STATE(43),
    [sym_list] = STATE(43),
    [sym_vector] = STATE(43),
    [sym_bytecode] = STATE(43),
    [sym_string_text_properties] = STATE(43),
    [sym_hash_table] = STATE(43),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(191),
    [sym_byte_compiled_file_name] = ACTIONS(191),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(33)] = {
    [sym__sexp] = STATE(44),
    [sym_special_form] = STATE(44),
    [sym_function_definition] = STATE(44),
    [sym_macro_definition] = STATE(44),
    [sym__atom] = STATE(44),
    [sym_float] = STATE(44),
    [sym_integer] = STATE(44),
    [sym_char] = STATE(44),
    [sym_symbol] = STATE(44),
    [sym_quote] = STATE(44),
    [sym_unquote_splice] = STATE(44),
    [sym_unquote] = STATE(44),
    [sym_list] = STATE(44),
    [sym_vector] = STATE(44),
    [sym_bytecode] = STATE(44),
    [sym_string_text_properties] = STATE(44),
    [sym_hash_table] = STATE(44),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(193),
    [sym_byte_compiled_file_name] = ACTIONS(193),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
  [STATE(34)] = {
    [sym__sexp] = STATE(45),
    [sym_special_form] = STATE(45),
    [sym_function_definition] = STATE(45),
    [sym_macro_definition] = STATE(45),
    [sym__atom] = STATE(45),
    [sym_float] = STATE(45),
    [sym_integer] = STATE(45),
    [sym_char] = STATE(45),
    [sym_symbol] = STATE(45),
    [sym_quote] = STATE(45),
    [sym_unquote_splice] = STATE(45),
    [sym_unquote] = STATE(45),
    [sym_list] = STATE(45),
    [sym_vector] = STATE(45),
    [sym_bytecode] = STATE(45),
    [sym_string_text_properties] = STATE(45),
    [sym_hash_table] = STATE(45),
    [anon_sym_LPAREN] = ACTIONS(7),
    [anon_sym_defun] = ACTIONS(9),
    [anon_sym_defsubst] = ACTIONS(9),
    [anon_sym_defmacro] = ACTIONS(9),
    [aux_sym_float_token1] = ACTIONS(11),
    [aux_sym_float_token2] = ACTIONS(11),
    [aux_sym_float_token3] = ACTIONS(11),
    [aux_sym_float_token4] = ACTIONS(11),
    [aux_sym_float_token5] = ACTIONS(11),
    [aux_sym_integer_token1] = ACTIONS(13),
    [aux_sym_integer_token2] = ACTIONS(15),
    [aux_sym_char_token1] = ACTIONS(17),
    [aux_sym_char_token2] = ACTIONS(19),
    [aux_sym_char_token3] = ACTIONS(19),
    [aux_sym_char_token4] = ACTIONS(19),
    [aux_sym_char_token5] = ACTIONS(19),
    [aux_sym_char_token6] = ACTIONS(17),
    [aux_sym_char_token7] = ACTIONS(17),
    [aux_sym_char_token8] = ACTIONS(19),
    [sym_string] = ACTIONS(195),
    [sym_byte_compiled_file_name] = ACTIONS(195),
    [anon_sym_nil] = ACTIONS(9),
    [anon_sym_t] = ACTIONS(9),
    [aux_sym_symbol_token1] = ACTIONS(9),
    [aux_sym_symbol_token2] = ACTIONS(9),
    [anon_sym_POUND_POUND] = ACTIONS(23),
    [anon_sym_POUND_SQUOTE] = ACTIONS(25),
    [anon_sym_SQUOTE] = ACTIONS(25),
    [anon_sym_BQUOTE] = ACTIONS(25),
    [anon_sym_COMMA_AT] = ACTIONS(27),
    [anon_sym_COMMA] = ACTIONS(29),
    [anon_sym_LBRACK] = ACTIONS(31),
    [anon_sym_POUND_LBRACK] = ACTIONS(33),
    [anon_sym_POUND_LPAREN] = ACTIONS(35),
    [anon_sym_POUNDs_LPARENhash_DASHtable] = ACTIONS(37),
    [sym_comment] = ACTIONS(3),
  },
};

static const uint16_t ts_small_parse_table[] = {
  [0] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(199), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(197), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [46] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(203), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(201), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [92] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(207), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(205), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [138] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(211), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(209), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [184] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(215), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(213), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [230] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(219), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(217), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [276] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(223), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(221), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [322] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(227), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(225), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [368] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(231), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(229), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [414] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(235), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(233), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [460] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(239), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(237), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [506] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(243), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(241), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [552] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(247), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(245), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [598] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(251), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(249), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [644] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(255), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(253), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [690] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(259), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(257), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [736] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(263), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(261), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [782] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(267), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(265), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [828] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(271), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(269), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [874] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(275), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(273), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [920] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(279), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(277), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [966] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(283), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(281), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1012] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(287), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(285), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1058] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(291), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(289), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1104] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(295), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(293), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1150] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(299), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(297), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1196] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(303), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(301), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1242] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(307), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(305), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1288] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(311), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(309), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1334] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(315), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(313), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1380] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(319), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(317), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1426] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(323), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(321), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1472] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(327), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(325), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1518] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(331), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(329), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1564] = 3,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(335), 17,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
      anon_sym_COMMA,
    ACTIONS(333), 21,
      ts_builtin_sym_end,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_POUND,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_RBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1610] = 6,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(23), 1,
      anon_sym_POUND_POUND,
    STATE(17), 1,
      sym_symbol,
    ACTIONS(9), 7,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
    ACTIONS(215), 10,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_COMMA,
    ACTIONS(213), 18,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1661] = 6,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(23), 1,
      anon_sym_POUND_POUND,
    STATE(15), 1,
      sym_symbol,
    ACTIONS(9), 7,
      anon_sym_defun,
      anon_sym_defsubst,
      anon_sym_defmacro,
      anon_sym_nil,
      anon_sym_t,
      aux_sym_symbol_token1,
      aux_sym_symbol_token2,
    ACTIONS(215), 10,
      aux_sym_float_token1,
      aux_sym_float_token2,
      aux_sym_float_token3,
      aux_sym_float_token4,
      aux_sym_float_token5,
      aux_sym_integer_token1,
      aux_sym_char_token1,
      aux_sym_char_token6,
      aux_sym_char_token7,
      anon_sym_COMMA,
    ACTIONS(213), 18,
      anon_sym_LPAREN,
      anon_sym_RPAREN,
      aux_sym_integer_token2,
      aux_sym_char_token2,
      aux_sym_char_token3,
      aux_sym_char_token4,
      aux_sym_char_token5,
      aux_sym_char_token8,
      sym_string,
      sym_byte_compiled_file_name,
      anon_sym_POUND_SQUOTE,
      anon_sym_SQUOTE,
      anon_sym_BQUOTE,
      anon_sym_COMMA_AT,
      anon_sym_LBRACK,
      anon_sym_POUND_LBRACK,
      anon_sym_POUND_LPAREN,
      anon_sym_POUNDs_LPARENhash_DASHtable,
  [1712] = 2,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(337), 1,
      ts_builtin_sym_end,
  [1719] = 2,
    ACTIONS(3), 1,
      sym_comment,
    ACTIONS(339), 1,
      sym_string,
};

static const uint32_t ts_small_parse_table_map[] = {
  [SMALL_STATE(35)] = 0,
  [SMALL_STATE(36)] = 46,
  [SMALL_STATE(37)] = 92,
  [SMALL_STATE(38)] = 138,
  [SMALL_STATE(39)] = 184,
  [SMALL_STATE(40)] = 230,
  [SMALL_STATE(41)] = 276,
  [SMALL_STATE(42)] = 322,
  [SMALL_STATE(43)] = 368,
  [SMALL_STATE(44)] = 414,
  [SMALL_STATE(45)] = 460,
  [SMALL_STATE(46)] = 506,
  [SMALL_STATE(47)] = 552,
  [SMALL_STATE(48)] = 598,
  [SMALL_STATE(49)] = 644,
  [SMALL_STATE(50)] = 690,
  [SMALL_STATE(51)] = 736,
  [SMALL_STATE(52)] = 782,
  [SMALL_STATE(53)] = 828,
  [SMALL_STATE(54)] = 874,
  [SMALL_STATE(55)] = 920,
  [SMALL_STATE(56)] = 966,
  [SMALL_STATE(57)] = 1012,
  [SMALL_STATE(58)] = 1058,
  [SMALL_STATE(59)] = 1104,
  [SMALL_STATE(60)] = 1150,
  [SMALL_STATE(61)] = 1196,
  [SMALL_STATE(62)] = 1242,
  [SMALL_STATE(63)] = 1288,
  [SMALL_STATE(64)] = 1334,
  [SMALL_STATE(65)] = 1380,
  [SMALL_STATE(66)] = 1426,
  [SMALL_STATE(67)] = 1472,
  [SMALL_STATE(68)] = 1518,
  [SMALL_STATE(69)] = 1564,
  [SMALL_STATE(70)] = 1610,
  [SMALL_STATE(71)] = 1661,
  [SMALL_STATE(72)] = 1712,
  [SMALL_STATE(73)] = 1719,
};

static const TSParseActionEntry ts_parse_actions[] = {
  [0] = {.entry = {.count = 0, .reusable = false}},
  [1] = {.entry = {.count = 1, .reusable = false}}, RECOVER(),
  [3] = {.entry = {.count = 1, .reusable = true}}, SHIFT_EXTRA(),
  [5] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_source_file, 0, 0, 0),
  [7] = {.entry = {.count = 1, .reusable = true}}, SHIFT(2),
  [9] = {.entry = {.count = 1, .reusable = false}}, SHIFT(39),
  [11] = {.entry = {.count = 1, .reusable = false}}, SHIFT(51),
  [13] = {.entry = {.count = 1, .reusable = false}}, SHIFT(56),
  [15] = {.entry = {.count = 1, .reusable = true}}, SHIFT(56),
  [17] = {.entry = {.count = 1, .reusable = false}}, SHIFT(58),
  [19] = {.entry = {.count = 1, .reusable = true}}, SHIFT(58),
  [21] = {.entry = {.count = 1, .reusable = true}}, SHIFT(8),
  [23] = {.entry = {.count = 1, .reusable = true}}, SHIFT(39),
  [25] = {.entry = {.count = 1, .reusable = true}}, SHIFT(32),
  [27] = {.entry = {.count = 1, .reusable = true}}, SHIFT(33),
  [29] = {.entry = {.count = 1, .reusable = false}}, SHIFT(34),
  [31] = {.entry = {.count = 1, .reusable = true}}, SHIFT(5),
  [33] = {.entry = {.count = 1, .reusable = true}}, SHIFT(6),
  [35] = {.entry = {.count = 1, .reusable = true}}, SHIFT(73),
  [37] = {.entry = {.count = 1, .reusable = true}}, SHIFT(7),
  [39] = {.entry = {.count = 1, .reusable = false}}, SHIFT(9),
  [41] = {.entry = {.count = 1, .reusable = true}}, SHIFT(63),
  [43] = {.entry = {.count = 1, .reusable = false}}, SHIFT(71),
  [45] = {.entry = {.count = 1, .reusable = false}}, SHIFT(70),
  [47] = {.entry = {.count = 1, .reusable = true}}, SHIFT(10),
  [49] = {.entry = {.count = 1, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0),
  [51] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(2),
  [54] = {.entry = {.count = 2, .reusable = false}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(39),
  [57] = {.entry = {.count = 2, .reusable = false}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(51),
  [60] = {.entry = {.count = 2, .reusable = false}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(56),
  [63] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(56),
  [66] = {.entry = {.count = 2, .reusable = false}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(58),
  [69] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(58),
  [72] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(3),
  [75] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(39),
  [78] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(32),
  [81] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(33),
  [84] = {.entry = {.count = 2, .reusable = false}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(34),
  [87] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(5),
  [90] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(6),
  [93] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(73),
  [96] = {.entry = {.count = 2, .reusable = true}}, REDUCE(aux_sym_source_file_repeat1, 2, 0, 0), SHIFT_REPEAT(7),
  [99] = {.entry = {.count = 1, .reusable = true}}, SHIFT(35),
  [101] = {.entry = {.count = 1, .reusable = true}}, SHIFT(3),
  [103] = {.entry = {.count = 1, .reusable = true}}, SHIFT(11),
  [105] = {.entry = {.count = 1, .reusable = true}}, SHIFT(47),
  [107] = {.entry = {.count = 1, .reusable = true}}, SHIFT(12),
  [109] = {.entry = {.count = 1, .reusable = true}}, SHIFT(48),
  [111] = {.entry = {.count = 1, .reusable = true}}, SHIFT(53),
  [113] = {.entry = {.count = 1, .reusable = true}}, SHIFT(14),
  [115] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_source_file, 1, 0, 0),
  [117] = {.entry = {.count = 1, .reusable = true}}, SHIFT(59),
  [119] = {.entry = {.count = 1, .reusable = true}}, SHIFT(16),
  [121] = {.entry = {.count = 1, .reusable = true}}, SHIFT(50),
  [123] = {.entry = {.count = 1, .reusable = true}}, SHIFT(36),
  [125] = {.entry = {.count = 1, .reusable = true}}, SHIFT(37),
  [127] = {.entry = {.count = 1, .reusable = true}}, SHIFT(38),
  [129] = {.entry = {.count = 1, .reusable = true}}, SHIFT(18),
  [131] = {.entry = {.count = 1, .reusable = true}}, SHIFT(40),
  [133] = {.entry = {.count = 1, .reusable = true}}, SHIFT(42),
  [135] = {.entry = {.count = 1, .reusable = true}}, SHIFT(19),
  [137] = {.entry = {.count = 1, .reusable = true}}, SHIFT(20),
  [139] = {.entry = {.count = 1, .reusable = true}}, SHIFT(41),
  [141] = {.entry = {.count = 1, .reusable = true}}, SHIFT(46),
  [143] = {.entry = {.count = 1, .reusable = true}}, SHIFT(22),
  [145] = {.entry = {.count = 1, .reusable = true}}, SHIFT(23),
  [147] = {.entry = {.count = 1, .reusable = true}}, SHIFT(49),
  [149] = {.entry = {.count = 1, .reusable = true}}, SHIFT(69),
  [151] = {.entry = {.count = 1, .reusable = true}}, SHIFT(25),
  [153] = {.entry = {.count = 1, .reusable = true}}, SHIFT(52),
  [155] = {.entry = {.count = 1, .reusable = true}}, SHIFT(26),
  [157] = {.entry = {.count = 1, .reusable = true}}, SHIFT(4),
  [159] = {.entry = {.count = 1, .reusable = true}}, SHIFT(54),
  [161] = {.entry = {.count = 1, .reusable = true}}, SHIFT(55),
  [163] = {.entry = {.count = 1, .reusable = true}}, SHIFT(28),
  [165] = {.entry = {.count = 1, .reusable = true}}, SHIFT(57),
  [167] = {.entry = {.count = 1, .reusable = true}}, SHIFT(27),
  [169] = {.entry = {.count = 1, .reusable = true}}, SHIFT(30),
  [171] = {.entry = {.count = 1, .reusable = true}}, SHIFT(60),
  [173] = {.entry = {.count = 1, .reusable = true}}, SHIFT(61),
  [175] = {.entry = {.count = 1, .reusable = true}}, SHIFT(62),
  [177] = {.entry = {.count = 1, .reusable = true}}, SHIFT(29),
  [179] = {.entry = {.count = 1, .reusable = true}}, SHIFT(65),
  [181] = {.entry = {.count = 1, .reusable = true}}, SHIFT(31),
  [183] = {.entry = {.count = 1, .reusable = true}}, SHIFT(64),
  [185] = {.entry = {.count = 1, .reusable = true}}, SHIFT(67),
  [187] = {.entry = {.count = 1, .reusable = true}}, SHIFT(66),
  [189] = {.entry = {.count = 1, .reusable = true}}, SHIFT(68),
  [191] = {.entry = {.count = 1, .reusable = true}}, SHIFT(43),
  [193] = {.entry = {.count = 1, .reusable = true}}, SHIFT(44),
  [195] = {.entry = {.count = 1, .reusable = true}}, SHIFT(45),
  [197] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 6, 0, 3),
  [199] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 6, 0, 3),
  [201] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_vector, 3, 0, 0),
  [203] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_vector, 3, 0, 0),
  [205] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_bytecode, 3, 0, 0),
  [207] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_bytecode, 3, 0, 0),
  [209] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_string_text_properties, 3, 0, 0),
  [211] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_string_text_properties, 3, 0, 0),
  [213] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_symbol, 1, 0, 0),
  [215] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_symbol, 1, 0, 0),
  [217] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_hash_table, 3, 0, 0),
  [219] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_hash_table, 3, 0, 0),
  [221] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_special_form, 4, 0, 0),
  [223] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_special_form, 4, 0, 0),
  [225] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 4, 0, 1),
  [227] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 4, 0, 1),
  [229] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_quote, 2, 0, 0),
  [231] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_quote, 2, 0, 0),
  [233] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_unquote_splice, 2, 0, 0),
  [235] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_unquote_splice, 2, 0, 0),
  [237] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_unquote, 2, 0, 0),
  [239] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_unquote, 2, 0, 0),
  [241] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 4, 0, 1),
  [243] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 4, 0, 1),
  [245] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_vector, 2, 0, 0),
  [247] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_vector, 2, 0, 0),
  [249] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_bytecode, 2, 0, 0),
  [251] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_bytecode, 2, 0, 0),
  [253] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_string_text_properties, 4, 0, 0),
  [255] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_string_text_properties, 4, 0, 0),
  [257] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_list, 3, 0, 0),
  [259] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_list, 3, 0, 0),
  [261] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_float, 1, 0, 0),
  [263] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_float, 1, 0, 0),
  [265] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 5, 0, 3),
  [267] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 5, 0, 3),
  [269] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_hash_table, 2, 0, 0),
  [271] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_hash_table, 2, 0, 0),
  [273] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 5, 0, 1),
  [275] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 5, 0, 1),
  [277] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 5, 0, 2),
  [279] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 5, 0, 2),
  [281] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_integer, 1, 0, 0),
  [283] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_integer, 1, 0, 0),
  [285] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 5, 0, 3),
  [287] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 5, 0, 3),
  [289] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_char, 1, 0, 0),
  [291] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_char, 1, 0, 0),
  [293] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_special_form, 3, 0, 0),
  [295] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_special_form, 3, 0, 0),
  [297] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 5, 0, 1),
  [299] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 5, 0, 1),
  [301] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 6, 0, 2),
  [303] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 6, 0, 2),
  [305] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 6, 0, 4),
  [307] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 6, 0, 4),
  [309] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_list, 2, 0, 0),
  [311] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_list, 2, 0, 0),
  [313] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 6, 0, 2),
  [315] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 6, 0, 2),
  [317] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 6, 0, 4),
  [319] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 6, 0, 4),
  [321] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 6, 0, 3),
  [323] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 6, 0, 3),
  [325] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 7, 0, 4),
  [327] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 7, 0, 4),
  [329] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_macro_definition, 7, 0, 4),
  [331] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_macro_definition, 7, 0, 4),
  [333] = {.entry = {.count = 1, .reusable = true}}, REDUCE(sym_function_definition, 5, 0, 2),
  [335] = {.entry = {.count = 1, .reusable = false}}, REDUCE(sym_function_definition, 5, 0, 2),
  [337] = {.entry = {.count = 1, .reusable = true}},  ACCEPT_INPUT(),
  [339] = {.entry = {.count = 1, .reusable = true}}, SHIFT(13),
};

#ifdef __cplusplus
extern "C" {
#endif
#ifdef TREE_SITTER_HIDE_SYMBOLS
#define TS_PUBLIC
#elif defined(_WIN32)
#define TS_PUBLIC __declspec(dllexport)
#else
#define TS_PUBLIC __attribute__((visibility("default")))
#endif

TS_PUBLIC const TSLanguage *tree_sitter_elisp(void) {
  static const TSLanguage language = {
    .abi_version = LANGUAGE_VERSION,
    .symbol_count = SYMBOL_COUNT,
    .alias_count = ALIAS_COUNT,
    .token_count = TOKEN_COUNT,
    .external_token_count = EXTERNAL_TOKEN_COUNT,
    .state_count = STATE_COUNT,
    .large_state_count = LARGE_STATE_COUNT,
    .production_id_count = PRODUCTION_ID_COUNT,
    .supertype_count = SUPERTYPE_COUNT,
    .field_count = FIELD_COUNT,
    .max_alias_sequence_length = MAX_ALIAS_SEQUENCE_LENGTH,
    .parse_table = &ts_parse_table[0][0],
    .small_parse_table = ts_small_parse_table,
    .small_parse_table_map = ts_small_parse_table_map,
    .parse_actions = ts_parse_actions,
    .symbol_names = ts_symbol_names,
    .field_names = ts_field_names,
    .field_map_slices = ts_field_map_slices,
    .field_map_entries = ts_field_map_entries,
    .symbol_metadata = ts_symbol_metadata,
    .public_symbol_map = ts_symbol_map,
    .alias_map = ts_non_terminal_alias_map,
    .alias_sequences = &ts_alias_sequences[0][0],
    .lex_modes = (const void*)ts_lex_modes,
    .lex_fn = ts_lex,
    .primary_state_ids = ts_primary_state_ids,
    .name = "elisp",
    .max_reserved_word_set_size = 0,
    .metadata = {
      .major_version = 1,
      .minor_version = 6,
      .patch_version = 0,
    },
  };
  return &language;
}
#ifdef __cplusplus
}
#endif
```

## File: `src/tree_sitter/alloc.h`
```c
#ifndef TREE_SITTER_ALLOC_H_
#define TREE_SITTER_ALLOC_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>

// Allow clients to override allocation functions
#ifdef TREE_SITTER_REUSE_ALLOCATOR

extern void *(*ts_current_malloc)(size_t size);
extern void *(*ts_current_calloc)(size_t count, size_t size);
extern void *(*ts_current_realloc)(void *ptr, size_t size);
extern void (*ts_current_free)(void *ptr);

#ifndef ts_malloc
#define ts_malloc  ts_current_malloc
#endif
#ifndef ts_calloc
#define ts_calloc  ts_current_calloc
#endif
#ifndef ts_realloc
#define ts_realloc ts_current_realloc
#endif
#ifndef ts_free
#define ts_free    ts_current_free
#endif

#else

#ifndef ts_malloc
#define ts_malloc  malloc
#endif
#ifndef ts_calloc
#define ts_calloc  calloc
#endif
#ifndef ts_realloc
#define ts_realloc realloc
#endif
#ifndef ts_free
#define ts_free    free
#endif

#endif

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_ALLOC_H_
```

## File: `src/tree_sitter/array.h`
```c
#ifndef TREE_SITTER_ARRAY_H_
#define TREE_SITTER_ARRAY_H_

#ifdef __cplusplus
extern "C" {
#endif

#include "./alloc.h"

#include <assert.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

#ifdef _MSC_VER
#pragma warning(push)
#pragma warning(disable : 4101)
#elif defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wunused-variable"
#endif

#define Array(T)       \
  struct {             \
    T *contents;       \
    uint32_t size;     \
    uint32_t capacity; \
  }

/// Initialize an array.
#define array_init(self) \
  ((self)->size = 0, (self)->capacity = 0, (self)->contents = NULL)

/// Create an empty array.
#define array_new() \
  { NULL, 0, 0 }

/// Get a pointer to the element at a given `index` in the array.
#define array_get(self, _index) \
  (assert((uint32_t)(_index) < (self)->size), &(self)->contents[_index])

/// Get a pointer to the first element in the array.
#define array_front(self) array_get(self, 0)

/// Get a pointer to the last element in the array.
#define array_back(self) array_get(self, (self)->size - 1)

/// Clear the array, setting its size to zero. Note that this does not free any
/// memory allocated for the array's contents.
#define array_clear(self) ((self)->size = 0)

/// Reserve `new_capacity` elements of space in the array. If `new_capacity` is
/// less than the array's current capacity, this function has no effect.
#define array_reserve(self, new_capacity) \
  _array__reserve((Array *)(self), array_elem_size(self), new_capacity)

/// Free any memory allocated for this array. Note that this does not free any
/// memory allocated for the array's contents.
#define array_delete(self) _array__delete((Array *)(self))

/// Push a new `element` onto the end of the array.
#define array_push(self, element)                            \
  (_array__grow((Array *)(self), 1, array_elem_size(self)), \
   (self)->contents[(self)->size++] = (element))

/// Increase the array's size by `count` elements.
/// New elements are zero-initialized.
#define array_grow_by(self, count) \
  do { \
    if ((count) == 0) break; \
    _array__grow((Array *)(self), count, array_elem_size(self)); \
    memset((self)->contents + (self)->size, 0, (count) * array_elem_size(self)); \
    (self)->size += (count); \
  } while (0)

/// Append all elements from one array to the end of another.
#define array_push_all(self, other)                                       \
  array_extend((self), (other)->size, (other)->contents)

/// Append `count` elements to the end of the array, reading their values from the
/// `contents` pointer.
#define array_extend(self, count, contents)                    \
  _array__splice(                                               \
    (Array *)(self), array_elem_size(self), (self)->size, \
    0, count,  contents                                        \
  )

/// Remove `old_count` elements from the array starting at the given `index`. At
/// the same index, insert `new_count` new elements, reading their values from the
/// `new_contents` pointer.
#define array_splice(self, _index, old_count, new_count, new_contents)  \
  _array__splice(                                                       \
    (Array *)(self), array_elem_size(self), _index,                \
    old_count, new_count, new_contents                                 \
  )

/// Insert one `element` into the array at the given `index`.
#define array_insert(self, _index, element) \
  _array__splice((Array *)(self), array_elem_size(self), _index, 0, 1, &(element))

/// Remove one element from the array at the given `index`.
#define array_erase(self, _index) \
  _array__erase((Array *)(self), array_elem_size(self), _index)

/// Pop the last element off the array, returning the element by value.
#define array_pop(self) ((self)->contents[--(self)->size])

/// Assign the contents of one array to another, reallocating if necessary.
#define array_assign(self, other) \
  _array__assign((Array *)(self), (const Array *)(other), array_elem_size(self))

/// Swap one array with another
#define array_swap(self, other) \
  _array__swap((Array *)(self), (Array *)(other))

/// Get the size of the array contents
#define array_elem_size(self) (sizeof *(self)->contents)

/// Search a sorted array for a given `needle` value, using the given `compare`
/// callback to determine the order.
///
/// If an existing element is found to be equal to `needle`, then the `index`
/// out-parameter is set to the existing value's index, and the `exists`
/// out-parameter is set to true. Otherwise, `index` is set to an index where
/// `needle` should be inserted in order to preserve the sorting, and `exists`
/// is set to false.
#define array_search_sorted_with(self, compare, needle, _index, _exists) \
  _array__search_sorted(self, 0, compare, , needle, _index, _exists)

/// Search a sorted array for a given `needle` value, using integer comparisons
/// of a given struct field (specified with a leading dot) to determine the order.
///
/// See also `array_search_sorted_with`.
#define array_search_sorted_by(self, field, needle, _index, _exists) \
  _array__search_sorted(self, 0, _compare_int, field, needle, _index, _exists)

/// Insert a given `value` into a sorted array, using the given `compare`
/// callback to determine the order.
#define array_insert_sorted_with(self, compare, value) \
  do { \
    unsigned _index, _exists; \
    array_search_sorted_with(self, compare, &(value), &_index, &_exists); \
    if (!_exists) array_insert(self, _index, value); \
  } while (0)

/// Insert a given `value` into a sorted array, using integer comparisons of
/// a given struct field (specified with a leading dot) to determine the order.
///
/// See also `array_search_sorted_by`.
#define array_insert_sorted_by(self, field, value) \
  do { \
    unsigned _index, _exists; \
    array_search_sorted_by(self, field, (value) field, &_index, &_exists); \
    if (!_exists) array_insert(self, _index, value); \
  } while (0)

// Private

typedef Array(void) Array;

/// This is not what you're looking for, see `array_delete`.
static inline void _array__delete(Array *self) {
  if (self->contents) {
    ts_free(self->contents);
    self->contents = NULL;
    self->size = 0;
    self->capacity = 0;
  }
}

/// This is not what you're looking for, see `array_erase`.
static inline void _array__erase(Array *self, size_t element_size,
                                uint32_t index) {
  assert(index < self->size);
  char *contents = (char *)self->contents;
  memmove(contents + index * element_size, contents + (index + 1) * element_size,
          (self->size - index - 1) * element_size);
  self->size--;
}

/// This is not what you're looking for, see `array_reserve`.
static inline void _array__reserve(Array *self, size_t element_size, uint32_t new_capacity) {
  if (new_capacity > self->capacity) {
    if (self->contents) {
      self->contents = ts_realloc(self->contents, new_capacity * element_size);
    } else {
      self->contents = ts_malloc(new_capacity * element_size);
    }
    self->capacity = new_capacity;
  }
}

/// This is not what you're looking for, see `array_assign`.
static inline void _array__assign(Array *self, const Array *other, size_t element_size) {
  _array__reserve(self, element_size, other->size);
  self->size = other->size;
  memcpy(self->contents, other->contents, self->size * element_size);
}

/// This is not what you're looking for, see `array_swap`.
static inline void _array__swap(Array *self, Array *other) {
  Array swap = *other;
  *other = *self;
  *self = swap;
}

/// This is not what you're looking for, see `array_push` or `array_grow_by`.
static inline void _array__grow(Array *self, uint32_t count, size_t element_size) {
  uint32_t new_size = self->size + count;
  if (new_size > self->capacity) {
    uint32_t new_capacity = self->capacity * 2;
    if (new_capacity < 8) new_capacity = 8;
    if (new_capacity < new_size) new_capacity = new_size;
    _array__reserve(self, element_size, new_capacity);
  }
}

/// This is not what you're looking for, see `array_splice`.
static inline void _array__splice(Array *self, size_t element_size,
                                 uint32_t index, uint32_t old_count,
                                 uint32_t new_count, const void *elements) {
  uint32_t new_size = self->size + new_count - old_count;
  uint32_t old_end = index + old_count;
  uint32_t new_end = index + new_count;
  assert(old_end <= self->size);

  _array__reserve(self, element_size, new_size);

  char *contents = (char *)self->contents;
  if (self->size > old_end) {
    memmove(
      contents + new_end * element_size,
      contents + old_end * element_size,
      (self->size - old_end) * element_size
    );
  }
  if (new_count > 0) {
    if (elements) {
      memcpy(
        (contents + index * element_size),
        elements,
        new_count * element_size
      );
    } else {
      memset(
        (contents + index * element_size),
        0,
        new_count * element_size
      );
    }
  }
  self->size += new_count - old_count;
}

/// A binary search routine, based on Rust's `std::slice::binary_search_by`.
/// This is not what you're looking for, see `array_search_sorted_with` or `array_search_sorted_by`.
#define _array__search_sorted(self, start, compare, suffix, needle, _index, _exists) \
  do { \
    *(_index) = start; \
    *(_exists) = false; \
    uint32_t size = (self)->size - *(_index); \
    if (size == 0) break; \
    int comparison; \
    while (size > 1) { \
      uint32_t half_size = size / 2; \
      uint32_t mid_index = *(_index) + half_size; \
      comparison = compare(&((self)->contents[mid_index] suffix), (needle)); \
      if (comparison <= 0) *(_index) = mid_index; \
      size -= half_size; \
    } \
    comparison = compare(&((self)->contents[*(_index)] suffix), (needle)); \
    if (comparison == 0) *(_exists) = true; \
    else if (comparison < 0) *(_index) += 1; \
  } while (0)

/// Helper macro for the `_sorted_by` routines below. This takes the left (existing)
/// parameter by reference in order to work with the generic sorting function above.
#define _compare_int(a, b) ((int)*(a) - (int)(b))

#ifdef _MSC_VER
#pragma warning(pop)
#elif defined(__GNUC__) || defined(__clang__)
#pragma GCC diagnostic pop
#endif

#ifdef __cplusplus
}
#endif

#endif  // TREE_SITTER_ARRAY_H_
```

## File: `src/tree_sitter/parser.h`
```c
#ifndef TREE_SITTER_PARSER_H_
#define TREE_SITTER_PARSER_H_

#ifdef __cplusplus
extern "C" {
#endif

#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

#define ts_builtin_sym_error ((TSSymbol)-1)
#define ts_builtin_sym_end 0
#define TREE_SITTER_SERIALIZATION_BUFFER_SIZE 1024

#ifndef TREE_SITTER_API_H_
typedef uint16_t TSStateId;
typedef uint16_t TSSymbol;
typedef uint16_t TSFieldId;
typedef struct TSLanguage TSLanguage;
typedef struct TSLanguageMetadata {
  uint8_t major_version;
  uint8_t minor_version;
  uint8_t patch_version;
} TSLanguageMetadata;
#endif

typedef struct {
  TSFieldId field_id;
  uint8_t child_index;
  bool inherited;
} TSFieldMapEntry;

// Used to index the field and supertype maps.
typedef struct {
  uint16_t index;
  uint16_t length;
} TSMapSlice;

typedef struct {
  bool visible;
  bool named;
  bool supertype;
} TSSymbolMetadata;

typedef struct TSLexer TSLexer;

struct TSLexer {
  int32_t lookahead;
  TSSymbol result_symbol;
  void (*advance)(TSLexer *, bool);
  void (*mark_end)(TSLexer *);
  uint32_t (*get_column)(TSLexer *);
  bool (*is_at_included_range_start)(const TSLexer *);
  bool (*eof)(const TSLexer *);
  void (*log)(const TSLexer *, const char *, ...);
};

typedef enum {
  TSParseActionTypeShift,
  TSParseActionTypeReduce,
  TSParseActionTypeAccept,
  TSParseActionTypeRecover,
} TSParseActionType;

typedef union {
  struct {
    uint8_t type;
    TSStateId state;
    bool extra;
    bool repetition;
  } shift;
  struct {
    uint8_t type;
    uint8_t child_count;
    TSSymbol symbol;
    int16_t dynamic_precedence;
    uint16_t production_id;
  } reduce;
  uint8_t type;
} TSParseAction;

typedef struct {
  uint16_t lex_state;
  uint16_t external_lex_state;
} TSLexMode;

typedef struct {
  uint16_t lex_state;
  uint16_t external_lex_state;
  uint16_t reserved_word_set_id;
} TSLexerMode;

typedef union {
  TSParseAction action;
  struct {
    uint8_t count;
    bool reusable;
  } entry;
} TSParseActionEntry;

typedef struct {
  int32_t start;
  int32_t end;
} TSCharacterRange;

struct TSLanguage {
  uint32_t abi_version;
  uint32_t symbol_count;
  uint32_t alias_count;
  uint32_t token_count;
  uint32_t external_token_count;
  uint32_t state_count;
  uint32_t large_state_count;
  uint32_t production_id_count;
  uint32_t field_count;
  uint16_t max_alias_sequence_length;
  const uint16_t *parse_table;
  const uint16_t *small_parse_table;
  const uint32_t *small_parse_table_map;
  const TSParseActionEntry *parse_actions;
  const char * const *symbol_names;
  const char * const *field_names;
  const TSMapSlice *field_map_slices;
  const TSFieldMapEntry *field_map_entries;
  const TSSymbolMetadata *symbol_metadata;
  const TSSymbol *public_symbol_map;
  const uint16_t *alias_map;
  const TSSymbol *alias_sequences;
  const TSLexerMode *lex_modes;
  bool (*lex_fn)(TSLexer *, TSStateId);
  bool (*keyword_lex_fn)(TSLexer *, TSStateId);
  TSSymbol keyword_capture_token;
  struct {
    const bool *states;
    const TSSymbol *symbol_map;
    void *(*create)(void);
    void (*destroy)(void *);
    bool (*scan)(void *, TSLexer *, const bool *symbol_whitelist);
    unsigned (*serialize)(void *, char *);
    void (*deserialize)(void *, const char *, unsigned);
  } external_scanner;
  const TSStateId *primary_state_ids;
  const char *name;
  const TSSymbol *reserved_words;
  uint16_t max_reserved_word_set_size;
  uint32_t supertype_count;
  const TSSymbol *supertype_symbols;
  const TSMapSlice *supertype_map_slices;
  const TSSymbol *supertype_map_entries;
  TSLanguageMetadata metadata;
};

static inline bool set_contains(const TSCharacterRange *ranges, uint32_t len, int32_t lookahead) {
  uint32_t index = 0;
  uint32_t size = len - index;
  while (size > 1) {
    uint32_t half_size = size / 2;
    uint32_t mid_index = index + half_size;
    const TSCharacterRange *range = &ranges[mid_index];
    if (lookahead >= range->start && lookahead <= range->end) {
      return true;
    } else if (lookahead > range->end) {
      index = mid_index;
    }
    size -= half_size;
  }
  const TSCharacterRange *range = &ranges[index];
  return (lookahead >= range->start && lookahead <= range->end);
}

/*
 *  Lexer Macros
 */

#ifdef _MSC_VER
#define UNUSED __pragma(warning(suppress : 4101))
#else
#define UNUSED __attribute__((unused))
#endif

#define START_LEXER()           \
  bool result = false;          \
  bool skip = false;            \
  UNUSED                        \
  bool eof = false;             \
  int32_t lookahead;            \
  goto start;                   \
  next_state:                   \
  lexer->advance(lexer, skip);  \
  start:                        \
  skip = false;                 \
  lookahead = lexer->lookahead;

#define ADVANCE(state_value) \
  {                          \
    state = state_value;     \
    goto next_state;         \
  }

#define ADVANCE_MAP(...)                                              \
  {                                                                   \
    static const uint16_t map[] = { __VA_ARGS__ };                    \
    for (uint32_t i = 0; i < sizeof(map) / sizeof(map[0]); i += 2) {  \
      if (map[i] == lookahead) {                                      \
        state = map[i + 1];                                           \
        goto next_state;                                              \
      }                                                               \
    }                                                                 \
  }

#define SKIP(state_value) \
  {                       \
    skip = true;          \
    state = state_value;  \
    goto next_state;      \
  }

#define ACCEPT_TOKEN(symbol_value)     \
  result = true;                       \
  lexer->result_symbol = symbol_value; \
  lexer->mark_end(lexer);

#define END_STATE() return result;

/*
 *  Parse Table Macros
 */

#define SMALL_STATE(id) ((id) - LARGE_STATE_COUNT)

#define STATE(id) id

#define ACTIONS(id) id

#define SHIFT(state_value)            \
  {{                                  \
    .shift = {                        \
      .type = TSParseActionTypeShift, \
      .state = (state_value)          \
    }                                 \
  }}

#define SHIFT_REPEAT(state_value)     \
  {{                                  \
    .shift = {                        \
      .type = TSParseActionTypeShift, \
      .state = (state_value),         \
      .repetition = true              \
    }                                 \
  }}

#define SHIFT_EXTRA()                 \
  {{                                  \
    .shift = {                        \
      .type = TSParseActionTypeShift, \
      .extra = true                   \
    }                                 \
  }}

#define REDUCE(symbol_name, children, precedence, prod_id) \
  {{                                                       \
    .reduce = {                                            \
      .type = TSParseActionTypeReduce,                     \
      .symbol = symbol_name,                               \
      .child_count = children,                             \
      .dynamic_precedence = precedence,                    \
      .production_id = prod_id                             \
    },                                                     \
  }}

#define RECOVER()                    \
  {{                                 \
    .type = TSParseActionTypeRecover \
  }}

#define ACCEPT_INPUT()              \
  {{                                \
    .type = TSParseActionTypeAccept \
  }}

#ifdef __cplusplus
}
#endif

#endif  // TREE_SITTER_PARSER_H_
```

## File: `test/corpus/bytecode_literal.txt`
```
================================================================================
Bytecode literals
================================================================================

#[1 2 3 4]

--------------------------------------------------------------------------------

(source_file
  (bytecode
    (integer)
    (integer)
    (integer)
    (integer)))
```

## File: `test/corpus/characters.txt`
```
================================================================================
Characters
================================================================================

?x
?\\
?\(

?\C-i
?\M-i
?\M-\151
?\M-\C-i
?\^i
?\C-\M-\S-\H-\s-\A-i
?\C-\;

?\N{SNOWMAN}
?\N{U+61}
?\u0061
?\U00000061
?\x61
?\141

--------------------------------------------------------------------------------

(source_file
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char)
  (char))
```

## File: `test/corpus/escaped_quote.txt`
```
================================================================================
Escaped symbols
================================================================================

\x\y
\'
\`
\,
\+1
\(

--------------------------------------------------------------------------------

(source_file
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol))
```

## File: `test/corpus/extras.txt`
```
================================================================================
Whitespace and comments
================================================================================

foo
; comment

bar

--------------------------------------------------------------------------------

(source_file
  (symbol)
  (comment)
  (symbol))
```

## File: `test/corpus/floats.txt`
```
================================================================================
Float literals
================================================================================

1.0
-.1
3E5
1.0e+INF

--------------------------------------------------------------------------------

(source_file
  (float)
  (float)
  (float)
  (float))
```

## File: `test/corpus/function_definition.txt`
```
================================================================================
Function definition
================================================================================

(defun foo (x &optional y)
  "stuff"
  x)
(defsubst bar () nil)

(defun no-args nil 123)

`(defun ,x () ,@body)

'(defun 1)
'(defun)
'(defun foo)

--------------------------------------------------------------------------------

(source_file
  (function_definition
    (symbol)
    (list
      (symbol)
      (symbol)
      (symbol))
    (string)
    (symbol))
  (function_definition
    (symbol)
    (list)
    (symbol))
  (function_definition
    (symbol)
    (symbol)
    (integer))
  (quote
    (list
      (symbol)
      (unquote
        (symbol))
      (list)
      (unquote_splice
        (symbol))))
  (quote
    (list
      (symbol)
      (integer)))
  (quote
    (list
      (symbol)))
  (quote
    (function_definition
      (symbol))))
```

## File: `test/corpus/hash_table.txt`
```
================================================================================
Hash table read syntax
================================================================================

#s(hash-table 0)

--------------------------------------------------------------------------------

(source_file
  (hash_table
    (integer)))
```

## File: `test/corpus/integers.txt`
```
================================================================================
Integer literals
================================================================================

1
-1.
+1234

#x2603
#o23003
#b101010

--------------------------------------------------------------------------------

(source_file
  (integer)
  (integer)
  (integer)
  (integer)
  (integer)
  (integer)
  (integer)
  (integer)
  (integer))
```

## File: `test/corpus/lists.txt`
```
================================================================================
Lists
================================================================================

()
(foo (bar))
(1 2 . nil)
(foo .)

--------------------------------------------------------------------------------

(source_file
  (list)
  (list
    (symbol)
    (list
      (symbol)))
  (list
    (integer)
    (integer)
    (symbol)
    (symbol))
  (list
    (symbol)
    (symbol)))
```

## File: `test/corpus/macro_definition.txt`
```
================================================================================
Macro definition
================================================================================

(defmacro foo (x &optional y)
  "stuff"
  x)

--------------------------------------------------------------------------------

(source_file
  (macro_definition
    (symbol)
    (list
      (symbol)
      (symbol)
      (symbol))
    (string)
    (symbol)))
```

## File: `test/corpus/multiple_characters.txt`
```
================================================================================
Multiple characters without spaces (regression test)
================================================================================

?a?a
?a?\]

--------------------------------------------------------------------------------

(source_file
  (char)
  (char)
  (char)
  (char))
```

## File: `test/corpus/quote.txt`
```
================================================================================
Quotes
================================================================================

'foo
#'bar
'(x ,y ,@z)

--------------------------------------------------------------------------------

(source_file
  (quote
    (symbol))
  (quote
    (symbol))
  (quote
    (list
      (symbol)
      (unquote
        (symbol))
      (unquote_splice
        (symbol)))))
```

## File: `test/corpus/special.txt`
```
================================================================================
Special forms
================================================================================

(if x 1 2)
(while x y)

--------------------------------------------------------------------------------

(source_file
  (special_form
    (symbol)
    (integer)
    (integer))
  (special_form
    (symbol)
    (symbol)))
```

## File: `test/corpus/special_read_syntax.txt`
```
================================================================================
Special read syntax
================================================================================

#$

--------------------------------------------------------------------------------

(source_file
  (byte_compiled_file_name))
```

## File: `test/corpus/string_after_symbol.txt`
```
================================================================================
String after symbol (regression test)
================================================================================

foo"bar"

--------------------------------------------------------------------------------

(source_file
  (symbol)
  (string))
```

## File: `test/corpus/string_props.txt`
```
================================================================================
String text properties
================================================================================

#("foo" 0 1 (x y))

--------------------------------------------------------------------------------

(source_file
  (string_text_properties
    (string)
    (integer)
    (integer)
    (list
      (symbol)
      (symbol))))
```

## File: `test/corpus/strings.txt`
```
================================================================================
String literals
================================================================================

""
"simple"
"\""
"\\"
"\\ foo \\"

"
multiline
"

"\
foo"

--------------------------------------------------------------------------------

(source_file
  (string)
  (string)
  (string)
  (string)
  (string)
  (string)
  (string))
```

## File: `test/corpus/symbols.txt`
```
================================================================================
Symbols
================================================================================

foo-bar
foo/bar
foo?
=
~
$
>
λ
:foo
foo!
foo|bar
foo.bar
foo@bar
foo{bar}
%
&optional
&&
_
##
.foo
foo-★
1+
\1
nil

--------------------------------------------------------------------------------

(source_file
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol)
  (symbol))
```

## File: `test/highlight/functions.el`
```
(defun foo (x)
  ;; ^ keyword
  ;;   ^ function
  ;;        ^ variable.parameter
  "stuff"
  ;; ^ string
  x)
```

