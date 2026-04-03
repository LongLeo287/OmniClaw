---
id: github.com-tree-sitter-tree-sitter-c-sharp-6cc4c73
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:30.128176
---

# KNOWLEDGE EXTRACT: github.com_tree-sitter_tree-sitter-c-sharp_6cc4c738
> **Extracted on:** 2026-04-01 16:52:38
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007525388/github.com_tree-sitter_tree-sitter-c-sharp_6cc4c738

---

## File: `.editorconfig`
```
root = true

[*]
charset = utf-8

[*.{json,toml,yml,gyp}]
indent_style = space
indent_size = 2

[*.js]
indent_style = space
indent_size = 2

[*.scm]
indent_style = space
indent_size = 2

[*.{c,cc,h}]
indent_style = space
indent_size = 4

[*.rs]
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

[parser.c]
indent_size = 2

[{alloc,array,parser}.h]
indent_size = 2
```

## File: `.gitattributes`
```
* text=auto eol=lf

# Generated source files
src/*.json linguist-generated
src/parser.c linguist-generated
src/tree_sitter/* linguist-generated

# C bindings
bindings/c/* linguist-generated
CMakeLists.txt linguist-generated
Makefile linguist-generated

# Rust bindings
bindings/rust/* linguist-generated
Cargo.toml linguist-generated
Cargo.lock linguist-generated

# Node.js bindings
bindings/node/* linguist-generated
binding.gyp linguist-generated
package.json linguist-generated
package-lock.json linguist-generated

# Python bindings
bindings/python/** linguist-generated
setup.py linguist-generated
pyproject.toml linguist-generated

# Go bindings
bindings/go/* linguist-generated
go.mod linguist-generated
go.sum linguist-generated

# Swift bindings
bindings/swift/** linguist-generated
Package.swift linguist-generated
Package.resolved linguist-generated
```

## File: `.gitignore`
```
# Rust artifacts
target/

# Node artifacts
build/
prebuilds/
node_modules/

# Swift artifacts
.build/

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
parser.exp
parser.lib

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

.claude/
```

## File: `CMakeLists.txt`
```
cmake_minimum_required(VERSION 3.13)

project(tree-sitter-c-sharp
        VERSION "0.23.1"
        DESCRIPTION "C# grammar for tree-sitter"
        HOMEPAGE_URL "https://github.com/tree-sitter/tree-sitter-c-sharp"
        LANGUAGES C)

option(BUILD_SHARED_LIBS "Build using shared libraries" ON)
option(TREE_SITTER_REUSE_ALLOCATOR "Reuse the library allocator" OFF)

set(TREE_SITTER_ABI_VERSION 14 CACHE STRING "Tree-sitter ABI version")
if(NOT ${TREE_SITTER_ABI_VERSION} MATCHES "^[0-9]+$")
    unset(TREE_SITTER_ABI_VERSION CACHE)
    message(FATAL_ERROR "TREE_SITTER_ABI_VERSION must be an integer")
endif()

find_program(TREE_SITTER_CLI tree-sitter DOC "Tree-sitter CLI")

add_custom_command(OUTPUT "${CMAKE_CURRENT_SOURCE_DIR}/src/parser.c"
                   DEPENDS "${CMAKE_CURRENT_SOURCE_DIR}/src/grammar.json"
                   COMMAND "${TREE_SITTER_CLI}" generate src/grammar.json
                            --abi=${TREE_SITTER_ABI_VERSION}
                   WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
                   COMMENT "Generating parser.c")

add_library(tree-sitter-c-sharp src/parser.c)
if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/src/scanner.c)
  target_sources(tree-sitter-c-sharp PRIVATE src/scanner.c)
endif()
target_include_directories(tree-sitter-c-sharp PRIVATE src)

target_compile_definitions(tree-sitter-c-sharp PRIVATE
                           $<$<BOOL:${TREE_SITTER_REUSE_ALLOCATOR}>:TREE_SITTER_REUSE_ALLOCATOR>
                           $<$<CONFIG:Debug>:TREE_SITTER_DEBUG>)

set_target_properties(tree-sitter-c-sharp
                      PROPERTIES
                      C_STANDARD 11
                      POSITION_INDEPENDENT_CODE ON
                      SOVERSION "${TREE_SITTER_ABI_VERSION}.${PROJECT_VERSION_MAJOR}"
                      DEFINE_SYMBOL "")

configure_file(bindings/c/tree-sitter-c-sharp.pc.in
               "${CMAKE_CURRENT_BINARY_DIR}/tree-sitter-c-sharp.pc" @ONLY)

include(GNUInstallDirs)

install(FILES bindings/c/tree-sitter-c-sharp.h
        DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/tree_sitter")
install(FILES "${CMAKE_CURRENT_BINARY_DIR}/tree-sitter-c-sharp.pc"
        DESTINATION "${CMAKE_INSTALL_DATAROOTDIR}/pkgconfig")
install(TARGETS tree-sitter-c-sharp
        LIBRARY DESTINATION "${CMAKE_INSTALL_LIBDIR}")

add_custom_target(ts-test "${TREE_SITTER_CLI}" test
                  WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}"
                  COMMENT "tree-sitter test")
```

## File: `Cargo.toml`
```
[package]
name = "tree-sitter-c-sharp"
description = "C# grammar for tree-sitter"
version = "0.23.1"
authors = [
  "Max Brunsfeld <maxbrunsfeld@gmail.com>",
  "Amaan Qureshi <amaanq12@gmail.com>",
]
license = "MIT"
readme = "README.md"
keywords = ["incremental", "parsing", "tree-sitter", "c-sharp"]
categories = ["parsing", "text-editors"]
repository = "https://github.com/tree-sitter/tree-sitter-c-sharp"
edition = "2021"
autoexamples = false

build = "bindings/rust/build.rs"
include = ["LICENSE", "bindings/rust/*", "grammar.js", "queries/*", "src/*", "tree-sitter.json"]

[lib]
path = "bindings/rust/lib.rs"

[dependencies]
tree-sitter-language = "0.1"

[build-dependencies]
cc = "1.1"

[dev-dependencies]
tree-sitter = "0.25"
```

## File: `LICENSE`
```
The MIT License (MIT)

Copyright (c) 2014-2023 Max Brunsfeld, Damien Guard, Amaan Qureshi, and contributors.

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
ifeq ($(OS),Windows_NT)
$(error Windows is not supported)
endif

LANGUAGE_NAME := tree-sitter-c-sharp
HOMEPAGE_URL := https://github.com/tree-sitter/tree-sitter-c-sharp
VERSION := 0.23.1

# repository
SRC_DIR := src

TS ?= tree-sitter

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

# ABI versioning
SONAME_MAJOR = $(shell sed -n 's/\#define LANGUAGE_VERSION //p' $(PARSER))
SONAME_MINOR = $(word 1,$(subst ., ,$(VERSION)))

# OS-specific bits
ifeq ($(shell uname),Darwin)
	SOEXT = dylib
	SOEXTVER_MAJOR = $(SONAME_MAJOR).$(SOEXT)
	SOEXTVER = $(SONAME_MAJOR).$(SONAME_MINOR).$(SOEXT)
	LINKSHARED = -dynamiclib -Wl,-install_name,$(LIBDIR)/lib$(LANGUAGE_NAME).$(SOEXTVER),-rpath,@executable_path/../Frameworks
else
	SOEXT = so
	SOEXTVER_MAJOR = $(SOEXT).$(SONAME_MAJOR)
	SOEXTVER = $(SOEXT).$(SONAME_MAJOR).$(SONAME_MINOR)
	LINKSHARED = -shared -Wl,-soname,lib$(LANGUAGE_NAME).$(SOEXTVER)
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
	sed -e 's|@PROJECT_VERSION@|$(VERSION)|' \
		-e 's|@CMAKE_INSTALL_LIBDIR@|$(LIBDIR:$(PREFIX)/%=%)|' \
		-e 's|@CMAKE_INSTALL_INCLUDEDIR@|$(INCLUDEDIR:$(PREFIX)/%=%)|' \
		-e 's|@PROJECT_DESCRIPTION@|$(DESCRIPTION)|' \
		-e 's|@PROJECT_HOMEPAGE_URL@|$(HOMEPAGE_URL)|' \
		-e 's|@CMAKE_INSTALL_PREFIX@|$(PREFIX)|' $< > $@

$(PARSER): $(SRC_DIR)/grammar.json
	$(TS) generate $^

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

## File: `Package.swift`
```
// swift-tools-version:5.3
import PackageDescription

let package = Package(
    name: "TreeSitterCSharp",
    products: [
        .library(name: "TreeSitterCSharp", targets: ["TreeSitterCSharp"]),
    ],
    dependencies: [
        .package(url: "https://github.com/ChimeHQ/SwiftTreeSitter", from: "0.9.0"),
    ],
    targets: [
        .target(
            name: "TreeSitterCSharp",
            dependencies: [],
            path: ".",
            sources: [
                "src/parser.c",
                "src/scanner.c",
            ],
            resources: [
                .copy("queries")
            ],
            publicHeadersPath: "bindings/swift",
            cSettings: [.headerSearchPath("src")]
        ),
        .testTarget(
            name: "TreeSitterCSharpTests",
            dependencies: [
                "SwiftTreeSitter",
                "TreeSitterCSharp",
            ],
            path: "bindings/swift/TreeSitterCSharpTests"
        )
    ],
    cLanguageStandard: .c11
)
```

## File: `README.md`
```markdown
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

## File: `binding.gyp`
```
{
  "targets": [
    {
      "target_name": "tree_sitter_c_sharp_binding",
      "dependencies": [
        "<!(node -p \"require('node-addon-api').targets\"):node_addon_api_except",
      ],
      "include_dirs": [
        "src",
      ],
      "sources": [
        "bindings/node/binding.cc",
        "src/parser.c",
        "src/scanner.c",
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

## File: `eslint.config.mjs`
```
import treesitter from 'eslint-config-treesitter';

export default [
  ...treesitter,
];
```

## File: `go.mod`
```
module github.com/tree-sitter/tree-sitter-c-sharp

go 1.22

require github.com/tree-sitter/go-tree-sitter v0.24.0

require github.com/mattn/go-pointer v0.0.1 // indirect
```

## File: `go.sum`
```
github.com/davecgh/go-spew v1.1.1 h1:vj9j/u1bqnvCEfJOwUhtlOARqs3+rkHYY13jYWTU97c=
github.com/davecgh/go-spew v1.1.1/go.mod h1:J7Y8YcW2NihsgmVo/mv3lAwl/skON4iLHjSsI+c5H38=
github.com/mattn/go-pointer v0.0.1 h1:n+XhsuGeVO6MEAp7xyEukFINEa+Quek5psIR/ylA6o0=
github.com/mattn/go-pointer v0.0.1/go.mod h1:2zXcozF6qYGgmsG+SeTZz3oAbFLdD3OWqnUbNvJZAlc=
github.com/pmezard/go-difflib v1.0.0 h1:4DBwDE0NGyQoBHbLQYPwSUPoCMWR5BEzIk/f1lZbAQM=
github.com/pmezard/go-difflib v1.0.0/go.mod h1:iKH77koFhYxTK1pcRnkKkqfTogsbg7gZNVY4sRDYZ/4=
github.com/stretchr/testify v1.9.0 h1:HtqpIVDClZ4nwg75+f6Lvsy/wHu+3BoSGCbBAcpTsTg=
github.com/stretchr/testify v1.9.0/go.mod h1:r2ic/lqez/lEtzL7wO/rwa5dbSLXVDPFyf8C91i36aY=
github.com/tree-sitter/go-tree-sitter v0.24.0 h1:kRZb6aBNfcI/u0Qh8XEt3zjNVnmxTisDBN+kXK0xRYQ=
github.com/tree-sitter/go-tree-sitter v0.24.0/go.mod h1:x681iFVoLMEwOSIHA1chaLkXlroXEN7WY+VHGFaoDbk=
github.com/tree-sitter/tree-sitter-c v0.21.5-0.20240818205408-927da1f210eb h1:A8425heRM8mylnv4H58FPUiH+aYivyitre0PzxrfmWs=
github.com/tree-sitter/tree-sitter-c v0.21.5-0.20240818205408-927da1f210eb/go.mod h1:dOF6gtQiF9UwNh995T5OphYmtIypkjsp3ap7r9AN/iA=
github.com/tree-sitter/tree-sitter-cpp v0.22.4-0.20240818224355-b1a4e2b25148 h1:AfFPZwtwGN01BW1jDdqBVqscTwetvMpydqYZz57RSlc=
github.com/tree-sitter/tree-sitter-cpp v0.22.4-0.20240818224355-b1a4e2b25148/go.mod h1:Bh6U3viD57rFXRYIQ+kmiYtr+1Bx0AceypDLJJSyi9s=
github.com/tree-sitter/tree-sitter-embedded-template v0.21.1-0.20240819044651-ffbf64942c33 h1:TwqSV3qLp3tKSqirGLRHnjFk9Tc2oy57LIl+FQ4GjI4=
github.com/tree-sitter/tree-sitter-embedded-template v0.21.1-0.20240819044651-ffbf64942c33/go.mod h1:CvCKCt3v04Ufos1zZnNCelBDeCGRpPucaN8QczoUsN4=
github.com/tree-sitter/tree-sitter-go v0.21.3-0.20240818010209-8c0f0e7a6012 h1:Xvxck3tE5FW7F7bTS97iNM2ADMyCMJztVqn5HYKdJGo=
github.com/tree-sitter/tree-sitter-go v0.21.3-0.20240818010209-8c0f0e7a6012/go.mod h1:T40D0O1cPvUU/+AmiXVXy1cncYQT6wem4Z0g4SfAYvY=
github.com/tree-sitter/tree-sitter-html v0.20.5-0.20240818004741-d11201a263d0 h1:c46K6uh5Dz00zJeU9BfjXdb8I+E4RkUdfnWJpQADXFo=
github.com/tree-sitter/tree-sitter-html v0.20.5-0.20240818004741-d11201a263d0/go.mod h1:hcNt/kOJHcIcuMvouE7LJcYdeFUFbVpBJ6d4wmOA+tU=
github.com/tree-sitter/tree-sitter-java v0.21.1-0.20240824015150-576d8097e495 h1:jrt4qbJVEFs4H93/ITxygHc6u0TGqAkkate7TQ4wFSA=
github.com/tree-sitter/tree-sitter-java v0.21.1-0.20240824015150-576d8097e495/go.mod h1:oyaR7fLnRV0hT9z6qwE9GkaeTom/hTDwK3H2idcOJFc=
github.com/tree-sitter/tree-sitter-javascript v0.21.5-0.20240818005344-15887341e5b5 h1:om4X9AVg3asL8gxNJDcz4e/Wp+VpQj1PY3uJXKr6EOg=
github.com/tree-sitter/tree-sitter-javascript v0.21.5-0.20240818005344-15887341e5b5/go.mod h1:nNqgPoV/h9uYWk6kYEFdEAhNVOacpfpRW5SFmdaP4tU=
github.com/tree-sitter/tree-sitter-json v0.21.1-0.20240818005659-bdd69eb8c8a5 h1:pfV3G3k7NCKqKk8THBmyuh2zA33lgYHS3GVrzRR8ry4=
github.com/tree-sitter/tree-sitter-json v0.21.1-0.20240818005659-bdd69eb8c8a5/go.mod h1:GbMKRjLfk0H+PI7nLi1Sx5lHf5wCpLz9al8tQYSxpEk=
github.com/tree-sitter/tree-sitter-php v0.22.9-0.20240819002312-a552625b56c1 h1:ZXZMDwE+IhUtGug4Brv6NjJWUU3rfkZBKpemf6RY8/g=
github.com/tree-sitter/tree-sitter-php v0.22.9-0.20240819002312-a552625b56c1/go.mod h1:UKCLuYnJ312Mei+3cyTmGOHzn0YAnaPRECgJmHtzrqs=
github.com/tree-sitter/tree-sitter-python v0.21.1-0.20240818005537-55a9b8a4fbfb h1:EXEM82lFM7JjJb6qiKZXkpIDaCcbV2obNn82ghwj9lw=
github.com/tree-sitter/tree-sitter-python v0.21.1-0.20240818005537-55a9b8a4fbfb/go.mod h1:lXCF1nGG5Dr4J3BTS0ObN4xJCCICiSu/b+Xe/VqMV7g=
github.com/tree-sitter/tree-sitter-ruby v0.21.1-0.20240818211811-7dbc1e2d0e2d h1:fcYCvoXdcP1uRQYXqJHRy6Hec+uKScQdKVtMwK9JeCI=
github.com/tree-sitter/tree-sitter-ruby v0.21.1-0.20240818211811-7dbc1e2d0e2d/go.mod h1:T1nShQ4v5AJtozZ8YyAS4uzUtDAJj/iv4YfwXSbUHzg=
github.com/tree-sitter/tree-sitter-rust v0.21.3-0.20240818005432-2b43eafe6447 h1:o9alBu1J/WjrcTKEthYtXmdkDc5OVXD+PqlvnEZ0Lzc=
github.com/tree-sitter/tree-sitter-rust v0.21.3-0.20240818005432-2b43eafe6447/go.mod h1:1Oh95COkkTn6Ezp0vcMbvfhRP5gLeqqljR0BYnBzWvc=
gopkg.in/yaml.v3 v3.0.1 h1:fxVm/GzAzEWqLHuvctI91KS9hhNmmWOoWu0XTYJS7CA=
gopkg.in/yaml.v3 v3.0.1/go.mod h1:K4uyk7z7BCEPqu6E+C64Yfv1cQ7kz7rIZviUmN+EgEM=
```

## File: `grammar.js`
```javascript
/**
 * @file C# grammar for tree-sitter
 * @author Max Brunsfeld <maxbrunsfeld@gmail.com>
 * @author Damien Guard <damieng@gmail.com>
 * @author Amaan Qureshi <amaanq12@gmail.com>
 * @license MIT
 */

/// <reference types="tree-sitter-cli/dsl" />
// @ts-check

const PREC = {
  GENERIC: 19,
  DOT: 18,
  INVOCATION: 18,
  POSTFIX: 18,
  PREFIX: 17,
  UNARY: 17,
  CAST: 17,
  RANGE: 16,
  SWITCH: 15,
  WITH: 14,
  MULT: 13,
  ADD: 12,
  SHIFT: 11,
  REL: 10,
  EQUAL: 9,
  AND: 8,
  XOR: 7,
  OR: 6,
  LOGICAL_AND: 5,
  LOGICAL_OR: 4,
  COALESCING: 3,
  CONDITIONAL: 2,
  ASSIGN: 1,
  SELECT: 0,
};

const decimalDigitSequence = /([0-9][0-9_]*[0-9]|[0-9])/;

const stringEncoding = /(u|U)8/;

export default grammar({
  name: 'c_sharp',

  conflicts: $ => [
    [$._simple_name, $.generic_name],
    [$._simple_name, $.type_parameter],
    [$._simple_name, $.subpattern],

    [$.tuple_element, $.type_pattern],
    [$.tuple_element, $.using_variable_declarator],
    [$.tuple_element, $.declaration_expression],

    [$.tuple_pattern, $.parameter],
    [$.tuple_pattern, $._simple_name],

    [$.lvalue_expression, $._name],
    [$.parameter, $.lvalue_expression],

    [$.type, $.attribute],
    [$.type, $.nullable_type],
    [$.type, $.nullable_type, $.array_creation_expression],
    [$.type, $._array_base_type],
    [$.type, $._array_base_type, $.array_creation_expression],
    [$.type, $.array_creation_expression],
    [$.type, $._pointer_base_type],

    [$.qualified_name, $.member_access_expression],
    [$.qualified_name, $.explicit_interface_specifier],

    [$._array_base_type, $.stackalloc_expression],

    [$.constant_pattern, $.non_lvalue_expression],
    [$.constant_pattern, $._expression_statement_expression],
    [$.constant_pattern, $.lvalue_expression],
    [$.constant_pattern, $._name],
    [$.constant_pattern, $.lvalue_expression, $._name],

    [$.type, $._name_invocation_pattern, $.recursive_pattern],
    [$.attribute, $.type, $._name_invocation_pattern, $.recursive_pattern],

    [$.parenthesized_pattern, $._parenthesized_pattern_with_designation],

    [$._reserved_identifier, $.modifier],
    [$._reserved_identifier, $.scoped_type],
    [$._reserved_identifier, $.implicit_type],
    [$._reserved_identifier, $.from_clause],
    [$._reserved_identifier, $.implicit_type, $.var_pattern],
    [$._reserved_identifier, $.type_parameter_constraint],
    [$._reserved_identifier, $.parameter, $.scoped_type],
    [$._reserved_identifier, $.parameter],
    [$._simple_name, $.parameter],
    [$.tuple_element, $.parameter, $.declaration_expression],
    [$.parameter, $.tuple_element],

    [$.event_declaration, $.variable_declarator],

    [$.base_list],
    [$.using_directive, $.modifier],
    [$.using_directive],

    [$._constructor_declaration_initializer, $._simple_name],
  ],

  externals: $ => [
    $._optional_semi,
    $.interpolation_regular_start,
    $.interpolation_verbatim_start,
    $.interpolation_raw_start,
    $.interpolation_start_quote,
    $.interpolation_end_quote,
    $.interpolation_open_brace,
    $.interpolation_close_brace,
    $.interpolation_string_content,
    $.raw_string_start,
    $.raw_string_end,
    $.raw_string_content,
  ],

  extras: $ => [
    /[\s\u00A0\uFEFF\u3000]+/,
    $.comment,
    $.preproc_region,
    $.preproc_endregion,
    $.preproc_line,
    $.preproc_pragma,
    $.preproc_nullable,
    $.preproc_error,
    $.preproc_warning,
    $.preproc_define,
    $.preproc_undef,
  ],

  inline: $ => [
    $._namespace_member_declaration,
    $._object_creation_type,
    $._nullable_base_type,
    $._parameter_type_with_modifiers,
    $._top_level_item_no_statement,
  ],

  precedences: $ => [
    [$._anonymous_object_member_declarator, $._simple_name],
    [$.block, $.initializer_expression],
  ],

  supertypes: $ => [
    $.declaration,
    $.expression,
    $.non_lvalue_expression,
    $.lvalue_expression,
    $.literal,
    $.statement,
    $.type,
    $.type_declaration,
    $.pattern,
  ],

  word: $ => $._identifier_token,

  rules: {
    compilation_unit: $ => seq(
      optional($.shebang_directive),
      repeat($._top_level_item),
    ),

    _top_level_item: $ => prec(2, choice(
      $._top_level_item_no_statement,
      $.global_statement,
    )),

    _top_level_item_no_statement: $ => choice(
      $.extern_alias_directive,
      $.using_directive,
      $.global_attribute,
      alias($.preproc_if_in_top_level, $.preproc_if),
      $._namespace_member_declaration,
      $.file_scoped_namespace_declaration,
    ),

    global_statement: $ => prec(1, $.statement),

    extern_alias_directive: $ => seq('extern', 'alias', field('name', $.identifier), ';'),

    using_directive: $ => seq(
      optional('global'),
      'using',
      choice(
        seq(
          optional('unsafe'),
          field('name', $.identifier),
          '=',
          $.type,
        ),
        seq(
          repeat(choice('static', 'unsafe')),
          $._name,
        ),
      ),
      ';',
    ),

    global_attribute: $ => seq(
      '[',
      choice('assembly', 'module'),
      ':',
      commaSep1($.attribute),
      optional(','),
      ']',
    ),

    attribute: $ => seq(
      field('name', $._name),
      optional($.attribute_argument_list),
    ),

    attribute_argument_list: $ => prec(-1, seq(
      '(',
      commaSep($.attribute_argument),
      ')',
    )),

    attribute_argument: $ => prec(-1, seq(
      optional(prec(1, seq(field('name', $.identifier), choice(':', '=')))),
      $.expression,
    )),

    attribute_list: $ => seq(
      '[',
      optional($.attribute_target_specifier),
      commaSep1($.attribute),
      optional(','),
      ']',
    ),

    _attribute_list: $ => choice($.attribute_list, $.preproc_if_in_attribute_list),

    attribute_target_specifier: _ => seq(
      choice('field', 'event', 'method', 'param', 'property', 'return', 'type', 'typevar'),
      ':',
    ),

    _namespace_member_declaration: $ => choice(
      $.namespace_declaration,
      $.type_declaration,
    ),

    namespace_declaration: $ => seq(
      'namespace',
      field('name', $._name),
      field('body', $.declaration_list),
      $._optional_semi,
    ),

    file_scoped_namespace_declaration: $ => seq(
      'namespace',
      field('name', $._name),
      ';',
    ),

    type_declaration: $ => choice(
      $.class_declaration,
      $.struct_declaration,
      $.enum_declaration,
      $.interface_declaration,
      $.delegate_declaration,
      $.record_declaration,
    ),

    class_declaration: $ => seq(
      $._class_declaration_initializer,
      $._declaration_list_body,
    ),

    _class_declaration_initializer: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      'class',
      field('name', $.identifier),
      repeat(choice($.type_parameter_list, $.parameter_list, $.base_list)),
      repeat($.type_parameter_constraints_clause),
    ),

    struct_declaration: $ => seq(
      $._struct_declaration_initializer,
      $._declaration_list_body,
    ),

    _struct_declaration_initializer: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      optional('ref'),
      'struct',
      field('name', $.identifier),
      repeat(choice($.type_parameter_list, $.parameter_list, $.base_list)),
      repeat($.type_parameter_constraints_clause),
    ),

    enum_declaration: $ => seq(
      $._enum_declaration_initializer,
      choice(
        seq(field('body', $.enum_member_declaration_list), $._optional_semi),
        ';',
      ),
    ),

    _enum_declaration_initializer: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      'enum',
      field('name', $.identifier),
      optional($.base_list),
    ),

    enum_member_declaration_list: $ => seq(
      '{',
      commaSep(choice(
        $.enum_member_declaration,
        alias($.preproc_if_in_enum_member_declaration, $.preproc_if),
      )),
      optional(','),
      '}',
    ),

    enum_member_declaration: $ => seq(
      repeat($._attribute_list),
      field('name', $.identifier),
      optional(seq('=', field('value', $.expression))),
    ),

    interface_declaration: $ => seq(
      $._interface_declaration_initializer,
      $._declaration_list_body,
    ),

    _interface_declaration_initializer: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      'interface',
      field('name', $.identifier),
      field('type_parameters', optional($.type_parameter_list)),
      optional($.base_list),
      repeat($.type_parameter_constraints_clause),
    ),

    delegate_declaration: $ => seq(
      $._delegate_declaration_initializer,
      repeat($.type_parameter_constraints_clause),
      ';',
    ),

    _delegate_declaration_initializer: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      'delegate',
      field('type', $.type),
      field('name', $.identifier),
      field('type_parameters', optional($.type_parameter_list)),
      field('parameters', $.parameter_list),
    ),

    record_declaration: $ => seq(
      $._record_declaration_initializer,
      $._declaration_list_body,
    ),

    _record_declaration_initializer: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      'record',
      optional(choice('class', 'struct')),
      field('name', $.identifier),
      repeat(choice($.type_parameter_list, $.parameter_list)),
      optional(alias($.record_base, $.base_list)),
      repeat($.type_parameter_constraints_clause),
    ),

    record_base: $ => choice(
      seq(':', commaSep1($._name)),
      seq(':', $.primary_constructor_base_type, optional(seq(',', commaSep1($._name)))),
    ),

    _declaration_list_body: $ => choice(
      seq(field('body', $.declaration_list), $._optional_semi),
      ';',
    ),

    primary_constructor_base_type: $ => seq(
      field('type', $._name),
      $.argument_list,
    ),

    modifier: _ => prec.right(choice(
      'abstract',
      'async',
      'const',
      'extern',
      'file',
      'fixed',
      'internal',
      'new',
      'override',
      'partial',
      'private',
      'protected',
      'public',
      'readonly',
      'required',
      // 'ref',     // `ref` as a modifier can only be used on struct declarations. Other than that it's a ref type or a ref parameter in a declaration.
      // 'scoped',  // `scoped` is either part of a scoped type or a scoped parameter. Both of which are handled outside of `modifier`.
      'sealed',
      'static',
      'unsafe',
      'virtual',
      'volatile',

    )),

    type_parameter_list: $ => seq('<', commaSep1($.type_parameter), '>'),

    type_parameter: $ => seq(
      repeat($._attribute_list),
      optional(choice('in', 'out')),
      field('name', $.identifier),
    ),

    base_list: $ => seq(':', commaSep1(seq($.type, optional($.argument_list)))),

    type_parameter_constraints_clause: $ => seq(
      'where',
      $.identifier,
      ':',
      commaSep1($.type_parameter_constraint),
    ),

    type_parameter_constraint: $ => choice(
      seq('class', optional('?')),
      'struct',
      'notnull',
      'unmanaged',
      $.constructor_constraint,
      field('type', $.type),
    ),

    constructor_constraint: _ => seq('new', '(', ')'),

    operator_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      field('type', $.type),
      optional($.explicit_interface_specifier),
      'operator',
      optional('checked'),
      field('operator', choice(
        '!',
        '~',
        '++',
        '--',
        'true',
        'false',
        '+', '-',
        '*', '/',
        '%', '^',
        '|', '&',
        '<<', '>>', '>>>',
        '==', '!=',
        '>', '<',
        '>=', '<=',
      )),
      field('parameters', $.parameter_list),
      $._function_body,
    ),

    conversion_operator_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      choice(
        'implicit',
        'explicit',
      ),
      repeat1(choice( // Intentionally structured this way for grammar size
        $.explicit_interface_specifier,
        'operator',
        'checked',
      )),
      field('type', $.type),
      field('parameters', $.parameter_list),
      $._function_body,
    ),

    declaration_list: $ => seq(
      '{',
      repeat($.declaration),
      '}',
    ),

    declaration: $ => choice(
      $.class_declaration,
      $.struct_declaration,
      $.enum_declaration,
      $.delegate_declaration,
      $.field_declaration,
      $.method_declaration,
      $.event_declaration,
      $.event_field_declaration,
      $.record_declaration,
      $.constructor_declaration,
      $.destructor_declaration,
      $.indexer_declaration,
      $.interface_declaration,
      $.namespace_declaration,
      $.operator_declaration,
      $.conversion_operator_declaration,
      $.property_declaration,
      $.using_directive,
      $.preproc_if,
    ),

    field_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      $.variable_declaration,
      ';',
    ),

    constructor_declaration: $ => seq(
      $._constructor_declaration_initializer,
      $._function_body,
    ),

    _constructor_declaration_initializer: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      field('name', $.identifier),
      field('parameters', $.parameter_list),
      optional($.constructor_initializer),
    ),

    destructor_declaration: $ => seq(
      repeat($._attribute_list),
      optional('extern'),
      '~',
      field('name', $.identifier),
      field('parameters', $.parameter_list),
      $._function_body,
    ),

    method_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      field('returns', $.type),
      optional($.explicit_interface_specifier),
      field('name', $.identifier),
      field('type_parameters', optional($.type_parameter_list)),
      field('parameters', $.parameter_list),
      repeat($.type_parameter_constraints_clause),
      $._function_body,
    ),

    event_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      'event',
      field('type', $.type),
      optional($.explicit_interface_specifier),
      field('name', $.identifier),
      choice(
        field('accessors', $.accessor_list),
        ';',
      ),
    ),

    event_field_declaration: $ => prec.dynamic(1, seq(
      repeat($._attribute_list),
      repeat($.modifier),
      'event',
      $.variable_declaration,
      ';',
    )),

    accessor_list: $ => seq(
      '{',
      repeat($.accessor_declaration),
      '}',
    ),

    accessor_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      field('name', choice('get', 'set', 'add', 'remove', 'init', $.identifier)),
      $._function_body,
    ),

    indexer_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      field('type', $.type),
      optional($.explicit_interface_specifier),
      'this',
      field('parameters', $.bracketed_parameter_list),
      choice(
        field('accessors', $.accessor_list),
        seq(field('value', $.arrow_expression_clause), ';'),
      ),
    ),

    bracketed_parameter_list: $ => seq(
      '[',
      sep(choice($.parameter, $._parameter_array), ','),
      ']',
    ),

    property_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      field('type', $.type),
      optional($.explicit_interface_specifier),
      field('name', $.identifier),
      choice(
        seq(
          field('accessors', $.accessor_list),
          optional(seq('=', field('value', $.expression), ';')),
        ),
        seq(
          field('value', $.arrow_expression_clause),
          ';',
        ),
      ),
    ),

    explicit_interface_specifier: $ => prec(PREC.DOT, seq(
      $._name,
      '.',
    )),

    parameter_list: $ => seq(
      '(',
      sep(choice($.parameter, $._parameter_array), ','),
      ')',
    ),

    _parameter_type_with_modifiers: $ => seq(
      repeat(prec.left(alias(
        choice('this', 'scoped', 'ref', 'out', 'in', 'readonly'),
        $.modifier,
      ))),
      field('type', $.type),
    ),

    parameter: $ => seq(
      repeat($._attribute_list),
      optional($._parameter_type_with_modifiers),
      field('name', $.identifier),
      optional(seq('=', $.expression)),
    ),

    _parameter_array: $ => seq(
      repeat($._attribute_list),
      'params',
      field('type', $.type),
      field('name', $.identifier),
    ),

    constructor_initializer: $ => seq(
      ':',
      choice('base', 'this'),
      $.argument_list,
    ),

    argument_list: $ => seq('(', commaSep($.argument), ')'),

    tuple_pattern: $ => seq(
      '(',
      commaSep1(choice(
        field('name', $.identifier),
        $.discard,
        $.tuple_pattern,
      )),
      ')',
    ),

    argument: $ => prec(1, seq(
      optional(seq(field('name', $.identifier), ':')),
      optional(choice('ref', 'out', 'in')),
      choice(
        $.expression,
        $.declaration_expression,
      ),
    )),

    block: $ => seq('{', repeat($.statement), '}'),

    arrow_expression_clause: $ => seq('=>', $.expression),

    _function_body: $ => choice(
      field('body', $.block),
      seq(field('body', $.arrow_expression_clause), ';'),
      ';',
    ),

    variable_declaration: $ => seq(
      field('type', $.type),
      commaSep1($.variable_declarator),
    ),

    using_variable_declaration: $ => seq(
      field('type', $.type),
      commaSep1(alias($.using_variable_declarator, $.variable_declarator)),
    ),

    variable_declarator: $ => seq(
      choice(field('name', $.identifier), $.tuple_pattern),
      optional($.bracketed_argument_list),
      optional(seq('=', $.expression)),
    ),

    using_variable_declarator: $ => seq(
      field('name', $.identifier),
      optional(seq('=', $.expression)),
    ),

    bracketed_argument_list: $ => seq(
      '[',
      commaSep1($.argument),
      optional(','),
      ']',
    ),

    qualified_identifier: $ => sep1($.identifier, '.'),

    _name: $ => choice(
      $.alias_qualified_name,
      $.qualified_name,
      $._simple_name,
    ),

    alias_qualified_name: $ => seq(
      field('alias', $.identifier),
      '::',
      field('name', $._simple_name),
    ),

    _simple_name: $ => choice(
      $.identifier,
      $.generic_name,
    ),

    qualified_name: $ => prec(PREC.DOT, seq(
      field('qualifier', $._name),
      '.',
      field('name', $._simple_name),
    )),

    generic_name: $ => seq($.identifier, $.type_argument_list),

    type_argument_list: $ => seq(
      '<',
      choice(
        repeat(','),
        commaSep1($.type),
      ),
      '>',
    ),

    type: $ => choice(
      $.implicit_type,
      $.array_type,
      $._name,
      $.nullable_type,
      $.pointer_type,
      $.function_pointer_type,
      $.predefined_type,
      $.tuple_type,
      $.ref_type,
      $.scoped_type,
    ),

    implicit_type: _ => prec.dynamic(1, 'var'),

    array_type: $ => seq(
      field('type', $._array_base_type),
      field('rank', $.array_rank_specifier),
    ),

    _array_base_type: $ => choice(
      $.array_type,
      $._name,
      $.nullable_type,
      $.pointer_type,
      $.function_pointer_type,
      $.predefined_type,
      $.tuple_type,
    ),

    array_rank_specifier: $ => seq(
      '[',
      commaSep(optional($.expression)),
      ']',
    ),

    nullable_type: $ => seq(field('type', $._nullable_base_type), '?'),

    _nullable_base_type: $ => choice(
      $.array_type,
      $._name,
      $.predefined_type,
      $.tuple_type,
    ),

    pointer_type: $ => seq(field('type', $._pointer_base_type), '*'),

    _pointer_base_type: $ => choice(
      $._name,
      $.nullable_type,
      $.pointer_type,
      $.function_pointer_type,
      $.predefined_type,
      $.tuple_type,
    ),

    function_pointer_type: $ => seq(
      'delegate',
      '*',
      optional($.calling_convention),
      '<',
      repeat(seq($.function_pointer_parameter, ',')),
      field('returns', $.type),
      '>',
    ),

    calling_convention: $ => choice(
      'managed',
      seq(
        'unmanaged',
        optional(seq(
          '[',
          commaSep1(choice(
            'Cdecl',
            'Stdcall',
            'Thiscall',
            'Fastcall',
            $.identifier,
          )),
          ']',
        )),
      ),
    ),

    function_pointer_parameter: $ => seq(
      optional(choice('ref', 'out', 'in')),
      field('type', $._ref_base_type),
    ),

    predefined_type: _ => token(choice(
      'bool',
      'byte',
      'char',
      'decimal',
      'double',
      'float',
      'int',
      'long',
      'object',
      'sbyte',
      'short',
      'string',
      'uint',
      'ulong',
      'ushort',
      'nint',
      'nuint',
      'void',
    )),

    ref_type: $ => seq(
      'ref',
      optional('readonly'),
      field('type', $.type),
    ),

    _ref_base_type: $ => choice(
      $.implicit_type,
      $._name,
      $.nullable_type,
      $.array_type,
      $.pointer_type,
      $.function_pointer_type,
      $.predefined_type,
      $.tuple_type,
    ),

    scoped_type: $ => seq(
      'scoped',
      field('type', $._scoped_base_type),
    ),

    _scoped_base_type: $ => choice(
      $._name,
      $.ref_type,
    ),

    tuple_type: $ => seq(
      '(',
      commaSep2($.tuple_element),
      ')',
    ),

    tuple_element: $ => seq(
      field('type', $.type),
      field('name', optional($.identifier)),
    ),

    statement: $ => prec(1, choice(
      $.block,
      $.break_statement,
      $.checked_statement,
      $.continue_statement,
      $.do_statement,
      $.empty_statement,
      $.expression_statement,
      $.fixed_statement,
      $.for_statement,
      $.return_statement,
      $.lock_statement,
      $.yield_statement,
      $.switch_statement,
      $.throw_statement,
      $.try_statement,
      $.unsafe_statement,
      $.using_statement,
      $.foreach_statement,
      $.goto_statement,
      $.labeled_statement,
      $.if_statement,
      $.while_statement,
      $.local_declaration_statement,
      $.local_function_statement,
      alias($.preproc_if_in_top_level, $.preproc_if),
    )),

    break_statement: _ => seq('break', ';'),

    checked_statement: $ => seq(choice('checked', 'unchecked'), $.block),

    continue_statement: _ => seq('continue', ';'),

    do_statement: $ => seq(
      'do',
      field('body', $.statement),
      'while',
      '(',
      field('condition', $.expression),
      ')',
      ';',
    ),

    empty_statement: _ => ';',

    expression_statement: $ => seq($._expression_statement_expression, ';'),

    fixed_statement: $ => seq('fixed', '(', $.variable_declaration, ')', $.statement),

    for_statement: $ => seq(
      'for',
      $._for_statement_conditions,
      field('body', $.statement),
    ),

    _for_statement_conditions: $ => seq(
      '(',
      field('initializer', optional(
        choice($.variable_declaration, commaSep1($.expression)),
      )),
      ';',
      field('condition', optional($.expression)),
      ';',
      field('update', optional(commaSep1($.expression))),
      ')',
    ),

    return_statement: $ => seq('return', optional($.expression), ';'),

    lock_statement: $ => seq('lock', '(', $.expression, ')', $.statement),

    yield_statement: $ => seq(
      'yield',
      choice(
        seq('return', $.expression),
        'break',
      ),
      ';',
    ),

    switch_statement: $ => seq(
      'switch',
      choice(
        seq(
          '(',
          field('value', $.expression),
          ')',
        ),
        field('value', $.tuple_expression),
      ),
      field('body', $.switch_body),
    ),

    switch_body: $ => seq('{', repeat($.switch_section), '}'),

    switch_section: $ => prec.left(seq(
      choice(
        seq(
          'case',
          choice(
            $.expression,
            seq($.pattern, optional($.when_clause)),
          ),
        ),
        'default',
      ),
      ':',
      repeat($.statement),
    )),

    throw_statement: $ => seq('throw', optional($.expression), ';'),

    try_statement: $ => seq(
      'try',
      field('body', $.block),
      repeat($.catch_clause),
      optional($.finally_clause),
    ),

    catch_clause: $ => seq(
      'catch',
      repeat(choice($.catch_declaration, $.catch_filter_clause)),
      field('body', $.block),
    ),

    catch_declaration: $ => seq(
      '(',
      field('type', $.type),
      optional(field('name', $.identifier)),
      ')',
    ),

    catch_filter_clause: $ => seq('when', '(', $.expression, ')'),

    finally_clause: $ => seq('finally', $.block),

    unsafe_statement: $ => seq('unsafe', $.block),

    using_statement: $ => seq(
      optional('await'),
      'using',
      '(',
      choice(
        alias($.using_variable_declaration, $.variable_declaration),
        $.expression,
      ),
      ')',
      field('body', $.statement),
    ),

    foreach_statement: $ => seq(
      $._foreach_statement_initializer,
      field('body', $.statement),
    ),

    _foreach_statement_initializer: $ => seq(
      optional('await'),
      'foreach',
      '(',
      choice(
        seq(
          field('type', $.type),
          field('left', choice($.identifier, $.tuple_pattern)),
        ),
        field('left', $.expression),
      ),
      'in',
      field('right', $.expression),
      ')',
    ),

    goto_statement: $ => seq(
      'goto',
      optional(choice('case', 'default')),
      optional($.expression),
      ';',
    ),

    labeled_statement: $ => seq(
      $.identifier,
      ':',
      $.statement,
    ),

    if_statement: $ => prec.right(seq(
      'if',
      '(',
      field('condition', $.expression),
      ')',
      field('consequence', $.statement),
      optional(seq(
        'else',
        field('alternative', $.statement),
      )),
    )),

    while_statement: $ => seq(
      'while',
      '(',
      field('condition', $.expression),
      ')',
      field('body', $.statement),
    ),

    local_declaration_statement: $ => seq(
      optional('await'),
      optional('using'),
      repeat($.modifier),
      $.variable_declaration,
      ';',
    ),

    local_function_statement: $ => seq(
      $._local_function_declaration,
      repeat($.type_parameter_constraints_clause),
      $._function_body,
    ),

    _local_function_declaration: $ => seq(
      repeat($._attribute_list),
      repeat($.modifier),
      field('type', $.type),
      field('name', $.identifier),
      field('type_parameters', optional($.type_parameter_list)),
      field('parameters', $.parameter_list),
    ),

    pattern: $ => choice(
      $.constant_pattern,
      $.declaration_pattern,
      $.discard,
      $.recursive_pattern,
      $.var_pattern,
      $.negated_pattern,
      // This must come before plain parenthesized_pattern to create GLR conflict
      prec.dynamic(1, alias($._parenthesized_pattern_with_designation, $.recursive_pattern)),
      $.parenthesized_pattern,
      $.relational_pattern,
      $.or_pattern,
      $.and_pattern,
      $.list_pattern,
      $.type_pattern,
    ),

    // Uses '(' pattern ')' to create direct conflict with parenthesized_pattern
    _parenthesized_pattern_with_designation: $ => seq(
      '(',
      $.pattern,
      ')',
      $._variable_designation,
    ),

    constant_pattern: $ => choice(
      $.binary_expression,
      $.default_expression,
      $.interpolated_string_expression,
      $.parenthesized_expression,
      $.postfix_unary_expression,
      $.prefix_unary_expression,
      $.sizeof_expression,
      $.tuple_expression,
      $.typeof_expression,
      $.member_access_expression,
      alias($._name_invocation_pattern, $.invocation_expression),
      alias($._complex_invocation_expression, $.invocation_expression),
      $.cast_expression,
      $._simple_name,
      $.literal,
    ),

    // Invocation with name - creates conflict with recursive_pattern's Name(positional_pattern_clause)
    _name_invocation_pattern: $ => seq(
      field('function', $._name),
      field('arguments', $.argument_list),
    ),

    // Invocation where function is not a simple name
    _complex_invocation_expression: $ => prec(PREC.INVOCATION, seq(
      field('function', choice(
        $.member_access_expression,
        $.element_access_expression,
        $.invocation_expression,
        $.parenthesized_expression,
        $.conditional_access_expression,
        $.cast_expression,
      )),
      field('arguments', $.argument_list),
    )),

    discard: _ => '_',

    parenthesized_pattern: $ => seq('(', $.pattern, ')'),

    var_pattern: $ => seq('var', $._variable_designation),

    type_pattern: $ => prec.right(field('type', $.type)),

    list_pattern: $ => prec.right(seq(
      '[',
      optional(seq(
        commaSep1(choice($.pattern, '..')),
        optional(','),
      )),
      ']',
      optional($._variable_designation),
    )),

    recursive_pattern: $ => prec.left(choice(
      // name followed by positional pattern WITH variable designation
      prec.dynamic(1, seq(
        field('type', $._name),
        $.positional_pattern_clause,
        optional($.property_pattern_clause),
        $._variable_designation,
      )),
      // name followed by positional pattern WITHOUT variable designation
      prec.dynamic(-1, seq(
        field('type', $._name),
        $.positional_pattern_clause,
        optional($.property_pattern_clause),
      )),
      // positional pattern with variable designation (no type prefix)
      prec.dynamic(1, seq(
        $.positional_pattern_clause,
        $._variable_designation,
      )),
      // positional pattern without variable designation (no type prefix)
      $.positional_pattern_clause,
      // other type followed by pattern clauses (type is required here to avoid ambiguity)
      seq(
        field('type', $.type),
        choice(
          seq(
            $.positional_pattern_clause,
            optional($.property_pattern_clause),
          ),
          $.property_pattern_clause,
        ),
        optional($._variable_designation),
      ),
      // no type, just pattern clauses (no variable designation to avoid conflict with above)
      seq(
        choice(
          seq(
            $.positional_pattern_clause,
            $.property_pattern_clause,
          ),
          $.property_pattern_clause,
        ),
        optional($._variable_designation),
      ),
    )),

    positional_pattern_clause: $ => prec(1, seq(
      '(',
      optional(commaSep($.subpattern)),
      ')',
    )),

    property_pattern_clause: $ => prec(1, seq(
      '{',
      commaSep($.subpattern),
      optional(','),
      '}',
    )),

    subpattern: $ => prec.right(seq(
      optional(
        choice(
          seq($.expression, ':'),
          seq($.identifier, ':'),
        ),
      ),
      $.pattern,
    )),

    relational_pattern: $ => choice(
      seq('<', $.expression),
      seq('<=', $.expression),
      seq('>', $.expression),
      seq('>=', $.expression),
    ),

    negated_pattern: $ => seq('not', $.pattern),

    and_pattern: $ => prec.left(PREC.AND, seq(
      field('left', $.pattern),
      field('operator', 'and'),
      field('right', $.pattern),
    )),

    or_pattern: $ => prec.left(PREC.OR, seq(
      field('left', $.pattern),
      field('operator', 'or'),
      field('right', $.pattern),
    )),

    declaration_pattern: $ => seq(
      field('type', $.type),
      $._variable_designation,
    ),

    _variable_designation: $ => prec(1, choice(
      $.discard,
      $.parenthesized_variable_designation,
      field('name', $.identifier),
    )),

    parenthesized_variable_designation: $ => seq(
      '(',
      commaSep($._variable_designation),
      ')',
    ),

    expression: $ => choice(
      $.non_lvalue_expression,
      $.lvalue_expression,
    ),

    non_lvalue_expression: $ => choice(
      'base',
      $.binary_expression,
      $.interpolated_string_expression,
      $.conditional_expression,
      $.conditional_access_expression,
      $.literal,
      $._expression_statement_expression,
      $.is_expression,
      $.is_pattern_expression,
      $.as_expression,
      $.cast_expression,
      $.checked_expression,
      $.switch_expression,
      $.throw_expression,
      $.default_expression,
      $.lambda_expression,
      $.with_expression,
      $.sizeof_expression,
      $.typeof_expression,
      $.makeref_expression,
      $.ref_expression,
      $.reftype_expression,
      $.refvalue_expression,
      $.stackalloc_expression,
      $.range_expression,
      $.array_creation_expression,
      $.anonymous_method_expression,
      $.anonymous_object_creation_expression,
      $.implicit_array_creation_expression,
      $.implicit_object_creation_expression,
      $.implicit_stackalloc_expression,
      $.initializer_expression,
      $.query_expression,
      alias($.preproc_if_in_expression, $.preproc_if),
    ),

    lvalue_expression: $ => choice(
      'this',
      $.member_access_expression,
      $.tuple_expression,
      $._simple_name,
      $.element_access_expression,
      alias($.bracketed_argument_list, $.element_binding_expression),
      alias($._pointer_indirection_expression, $.prefix_unary_expression),
      alias($._parenthesized_lvalue_expression, $.parenthesized_expression),
    ),

    // Covers error CS0201: Only assignment, call, increment, decrement, await, and new object expressions can be used as a statement
    _expression_statement_expression: $ => choice(
      $.assignment_expression,
      $.invocation_expression,
      $.postfix_unary_expression,
      $.prefix_unary_expression,
      $.await_expression,
      $.object_creation_expression,
      $.parenthesized_expression,
    ),

    assignment_expression: $ => seq(
      field('left', $.lvalue_expression),
      field('operator',
        choice(
          '=',
          '+=',
          '-=',
          '*=',
          '/=',
          '%=',
          '&=',
          '^=',
          '|=',
          '<<=',
          '>>=',
          '>>>=',
          '??=',
        ),
      ),
      field('right', $.expression),
    ),

    binary_expression: $ => choice(
      ...[
        ['&&', PREC.LOGICAL_AND],
        ['||', PREC.LOGICAL_OR],
        ['>>', PREC.SHIFT],
        ['>>>', PREC.SHIFT],
        ['<<', PREC.SHIFT],
        ['&', PREC.AND],
        ['^', PREC.XOR],
        ['|', PREC.OR],
        ['+', PREC.ADD],
        ['-', PREC.ADD],
        ['*', PREC.MULT],
        ['/', PREC.MULT],
        ['%', PREC.MULT],
        ['<', PREC.REL],
        ['<=', PREC.REL],
        ['==', PREC.EQUAL],
        ['!=', PREC.EQUAL],
        ['>=', PREC.REL],
        ['>', PREC.REL],
      ].map(([operator, precedence]) =>
        prec.left(precedence, seq(
          field('left', $.expression),
          // @ts-ignore
          field('operator', operator),
          field('right', $.expression),
        )),
      ),
      prec.right(PREC.COALESCING, seq(
        field('left', $.expression),
        field('operator', '??'),
        field('right', $.expression),
      )),
    ),

    postfix_unary_expression: $ => prec(PREC.POSTFIX, seq(
      $.expression,
      choice('++', '--', '!'),
    )),

    prefix_unary_expression: $ => prec(PREC.UNARY, seq(
      choice('++', '--', '+', '-', '!', '~', '&', '^'),
      $.expression,
    )),

    _pointer_indirection_expression: $ => prec.right(PREC.UNARY, seq(
      '*',
      $.lvalue_expression,
    )),

    query_expression: $ => seq($.from_clause, $._query_body),

    from_clause: $ => seq(
      'from',
      optional(field('type', $.type)),
      field('name', $.identifier),
      'in',
      $.expression,
    ),

    _query_body: $ => prec.right(sep1(
      seq(
        repeat($._query_clause),
        $._select_or_group_clause,
      ),
      seq('into', $.identifier),
    )),

    _query_clause: $ => choice(
      $.from_clause,
      $.join_clause,
      $.let_clause,
      $.order_by_clause,
      $.where_clause,
    ),

    join_clause: $ => seq(
      'join',
      $._join_header,
      $._join_body,
      optional($.join_into_clause),
    ),

    _join_header: $ => seq(optional(field('type', $.type)), $.identifier, 'in', $.expression),

    _join_body: $ => seq('on', $.expression, 'equals', $.expression),

    join_into_clause: $ => seq('into', $.identifier),

    let_clause: $ => seq(
      'let',
      $.identifier,
      '=',
      $.expression,
    ),

    order_by_clause: $ => seq(
      'orderby',
      commaSep1($._ordering),
    ),

    _ordering: $ => seq(
      $.expression,
      optional(choice('ascending', 'descending')),
    ),

    where_clause: $ => seq('where', $.expression),

    _select_or_group_clause: $ => choice(
      $.group_clause,
      $.select_clause,
    ),

    group_clause: $ => seq('group', $.expression, 'by', $.expression),

    select_clause: $ => seq('select', $.expression),

    conditional_expression: $ => prec.right(PREC.CONDITIONAL, seq(
      field('condition', $.expression),
      '?',
      field('consequence', $.expression),
      ':',
      field('alternative', $.expression),
    )),

    conditional_access_expression: $ => prec.right(PREC.CONDITIONAL, seq(
      field('condition', $.expression),
      '?',
      choice(
        $.member_binding_expression,
        alias($.bracketed_argument_list, $.element_binding_expression),
      ),
    )),

    as_expression: $ => prec(PREC.REL, seq(
      field('left', $.expression),
      field('operator', 'as'),
      field('right', $.type),
    )),

    is_expression: $ => prec(PREC.REL, seq(
      field('left', $.expression),
      field('operator', 'is'),
      field('right', $.type),
    )),

    is_pattern_expression: $ => prec(PREC.REL, seq(
      field('expression', $.expression),
      'is',
      field('pattern', $.pattern),
    )),

    cast_expression: $ => prec(PREC.CAST, prec.dynamic(1, seq( // higher than invocation, lower than binary
      '(',
      field('type', $.type),
      ')',
      field('value', $.expression),
    ))),

    checked_expression: $ => seq(
      choice('checked', 'unchecked'),
      '(',
      $.expression,
      ')',
    ),

    invocation_expression: $ => prec(PREC.INVOCATION, seq(
      field('function', $.expression),
      field('arguments', $.argument_list),
    )),

    switch_expression: $ => prec(PREC.SWITCH, seq(
      $.expression,
      'switch',
      $._switch_expression_body,
    )),
    _switch_expression_body: $ => seq(
      '{',
      commaSep($.switch_expression_arm),
      optional(','),
      '}',
    ),


    switch_expression_arm: $ => seq(
      $.pattern,
      optional($.when_clause),
      '=>',
      $.expression,
    ),

    when_clause: $ => seq('when', $.expression),

    await_expression: $ => prec.right(PREC.UNARY, seq(
      'await',
      $.expression,
    )),

    throw_expression: $ => seq('throw', $.expression),

    element_access_expression: $ => prec(PREC.POSTFIX, seq(
      field('expression', $.expression),
      field('subscript', $.bracketed_argument_list),
    )),

    interpolated_string_expression: $ => choice(
      seq(
        alias($.interpolation_regular_start, $.interpolation_start),
        alias($.interpolation_start_quote, '"'),
        repeat($._interpolated_string_content),
        alias($.interpolation_end_quote, '"'),
      ),
      seq(
        alias($.interpolation_verbatim_start, $.interpolation_start),
        alias($.interpolation_start_quote, '"'),
        repeat($._interpolated_verbatim_string_content),
        alias($.interpolation_end_quote, '"'),
      ),
      seq(
        alias($.interpolation_raw_start, $.interpolation_start),
        alias($.interpolation_start_quote, $.interpolation_quote),
        repeat($._interpolated_raw_string_content),
        alias($.interpolation_end_quote, $.interpolation_quote),
      ),
    ),

    _interpolated_string_content: $ => choice(
      alias($.interpolation_string_content, $.string_content),
      $.escape_sequence,
      $.interpolation,
    ),

    _interpolated_verbatim_string_content: $ => choice(
      alias($.interpolation_string_content, $.string_content),
      $.interpolation,
    ),

    _interpolated_raw_string_content: $ => choice(
      alias($.interpolation_string_content, $.string_content),
      $.interpolation,
    ),

    interpolation: $ => seq(
      alias($.interpolation_open_brace, $.interpolation_brace),
      $.expression,
      optional($.interpolation_alignment_clause),
      optional($.interpolation_format_clause),
      alias($.interpolation_close_brace, $.interpolation_brace),
    ),

    interpolation_alignment_clause: $ => seq(',', $.expression),

    interpolation_format_clause: _ => seq(':', /[^}"]+/),

    member_access_expression: $ => prec(PREC.DOT, seq(
      field('expression', choice($.expression, $.predefined_type, $._name)),
      choice('.', '->'),
      field('name', $._simple_name),
    )),

    member_binding_expression: $ => seq(
      '.',
      field('name', $._simple_name),
    ),

    object_creation_expression: $ => prec.right(seq(
      'new',
      field('type', $.type),
      field('arguments', optional($.argument_list)),
      field('initializer', optional($.initializer_expression)),
    )),

    // inline
    _object_creation_type: $ => choice(
      $._name,
      $.nullable_type,
      $.predefined_type,
    ),

    parenthesized_expression: $ => seq(
      '(',
      $.non_lvalue_expression,
      ')',
    ),

    _parenthesized_lvalue_expression: $ => seq('(', $.lvalue_expression, ')'),

    lambda_expression: $ => prec(-1, seq(
      $._lambda_expression_init,
      '=>',
      field('body', choice($.block, $.expression)),
    )),

    _lambda_expression_init: $ => prec(-1, seq(
      repeat($._attribute_list),
      repeat(prec(-1, alias(choice('static', 'async'), $.modifier))),
      optional(field('type', $.type)),
      field('parameters', $._lambda_parameters),
    ),
    ),

    _lambda_parameters: $ => prec(-1, choice(
      $.parameter_list,
      alias($.identifier, $.implicit_parameter),
    )),

    array_creation_expression: $ => prec.dynamic(PREC.UNARY, seq(
      'new',
      field('type', $.array_type),
      optional($.initializer_expression),
    )),

    anonymous_method_expression: $ => seq(
      repeat(prec(-1, alias(choice('static', 'async'), $.modifier))),
      'delegate',
      optional(field('parameters', $.parameter_list)),
      $.block,
    ),

    anonymous_object_creation_expression: $ => seq(
      'new',
      '{',
      commaSep($._anonymous_object_member_declarator),
      optional(','),
      '}',
    ),

    _anonymous_object_member_declarator: $ => choice(
      seq($.identifier, '=', $.expression),
      $.expression,
    ),

    implicit_array_creation_expression: $ => seq(
      'new',
      '[',
      repeat(','),
      ']',
      $.initializer_expression,
    ),

    implicit_object_creation_expression: $ => prec.right(seq(
      'new',
      $.argument_list,
      optional($.initializer_expression),
    )),

    implicit_stackalloc_expression: $ => seq(
      'stackalloc',
      '[',
      ']',
      $.initializer_expression,
    ),

    initializer_expression: $ => seq(
      '{',
      commaSep($.expression),
      optional(','),
      '}',
    ),

    declaration_expression: $ => prec.dynamic(1, seq(
      field('type', $.type),
      field('name', $.identifier),
    )),

    default_expression: $ => prec.right(seq(
      'default',
      optional(seq(
        '(',
        field('type', $.type),
        ')',
      )),
    )),

    with_expression: $ => prec.left(PREC.WITH, seq(
      $.expression,
      'with',
      $._with_body,
    )),
    _with_body: $ => seq(
      '{',
      commaSep($.with_initializer),
      optional(','),
      '}',
    ),

    with_initializer: $ => seq($.identifier, '=', $.expression),

    sizeof_expression: $ => seq(
      'sizeof',
      '(',
      field('type', $.type),
      ')',
    ),

    typeof_expression: $ => seq(
      'typeof',
      '(',
      field('type', $.type),
      ')',
    ),

    makeref_expression: $ => seq(
      '__makeref',
      '(',
      $.expression,
      ')',
    ),

    ref_expression: $ => seq('ref', $.expression),

    reftype_expression: $ => seq(
      '__reftype',
      '(',
      $.expression,
      ')',
    ),

    refvalue_expression: $ => seq(
      '__refvalue',
      '(',
      field('value', $.expression),
      ',',
      field('type', $.type),
      ')',
    ),

    stackalloc_expression: $ => prec.left(seq(
      'stackalloc',
      field('type', $.array_type),
      optional($.initializer_expression),
    )),

    range_expression: $ => prec.right(PREC.RANGE, seq(
      optional($.expression),
      '..',
      optional($.expression),
    )),

    tuple_expression: $ => seq(
      '(',
      commaSep2($.argument),
      ')',
    ),

    literal: $ => choice(
      $.null_literal,
      $.character_literal,
      $.integer_literal,
      $.real_literal,
      $.boolean_literal,
      $.string_literal,
      $.verbatim_string_literal,
      $.raw_string_literal,
    ),

    null_literal: _ => 'null',

    character_literal: $ => seq(
      '\'',
      choice($.character_literal_content, $.escape_sequence),
      '\'',
    ),

    character_literal_content: $ => token.immediate(/[^'\\]/),

    integer_literal: _ => token(seq(
      choice(
        decimalDigitSequence, // Decimal
        (/0[xX][0-9a-fA-F_]*[0-9a-fA-F]+/), // Hex
        (/0[bB][01_]*[01]+/), // Binary
      ),
      optional(/([uU][lL]?|[lL][uU]?)/),
    )),

    real_literal: _ => {
      const suffix = /[fFdDmM]/;
      const exponent = /[eE][+-]?[0-9][0-9_]*/;
      return token(choice(
        seq(
          decimalDigitSequence,
          '.',
          decimalDigitSequence,
          optional(exponent),
          optional(suffix),
        ),
        seq(
          '.',
          decimalDigitSequence,
          optional(exponent),
          optional(suffix),
        ),
        seq(
          decimalDigitSequence,
          exponent,
          optional(suffix),
        ),
        seq(
          decimalDigitSequence,
          suffix,
        ),
      ));
    },

    string_literal: $ => seq(
      '"',
      repeat(choice(
        $.string_literal_content,
        $.escape_sequence,
      )),
      '"',
      optional($.string_literal_encoding),
    ),

    string_literal_content: _ => token.immediate(prec(1, /[^"\\\n]+/)),

    escape_sequence: _ => token(choice(
      /\\x[0-9a-fA-F]{1,4}/,
      /\\u[0-9a-fA-F]{4}/,
      /\\U[0-9a-fA-F]{8}/,
      /\\[abefnrtv'\"\\\?0]/,
    )),

    string_literal_encoding: _ => token.immediate(stringEncoding),

    verbatim_string_literal: _ => token(seq(
      '@"',
      repeat(choice(
        /[^"]/,
        '""',
      )),
      '"',
      optional(stringEncoding),
    )),

    raw_string_literal: $ => seq(
      $.raw_string_start,
      $.raw_string_content,
      $.raw_string_end,
      optional(stringEncoding),
    ),

    boolean_literal: _ => choice('true', 'false'),

    _identifier_token: _ => token(seq(optional('@'), /(\p{XID_Start}|_|\\u[0-9A-Fa-f]{4}|\\U[0-9A-Fa-f]{8})(\p{XID_Continue}|\\u[0-9A-Fa-f]{4}|\\U[0-9A-Fa-f]{8})*/)),
    identifier: $ => choice(
      $._identifier_token,
      $._reserved_identifier,
    ),

    _reserved_identifier: _ => choice(
      'alias',
      'ascending',
      'by',
      'descending',
      'equals',
      'file',
      'from',
      'global',
      'group',
      'into',
      'join',
      'let',
      'notnull',
      'on',
      'orderby',
      'scoped',
      'select',
      'unmanaged',
      'var',
      'when',
      'where',
      'yield',
    ),

    // Preprocessor

    ...preprocIf('', $ => $.declaration),
    ...preprocIf('_in_top_level', $ => choice($._top_level_item_no_statement, $.statement)),
    ...preprocIf('_in_expression', $ => $.expression, -2, false),
    ...preprocIf('_in_enum_member_declaration', $ => $.enum_member_declaration, 0, false),
    ...preprocIf('_in_attribute_list', $ => $.attribute_list, -1, false),

    preproc_arg: _ => token(prec(-1, /\S([^/\n]|\/[^*]|\\\r?\n)*/)),
    preproc_directive: _ => /#[ \t]*[a-zA-Z0-9]\w*/,

    _preproc_expression: $ => choice(
      $.identifier,
      $.boolean_literal,
      $.integer_literal,
      $.character_literal,
      alias($.preproc_unary_expression, $.unary_expression),
      alias($.preproc_binary_expression, $.binary_expression),
      alias($.preproc_parenthesized_expression, $.parenthesized_expression),
    ),

    preproc_parenthesized_expression: $ => seq(
      '(',
      $._preproc_expression,
      ')',
    ),

    preproc_unary_expression: $ => prec.left(PREC.UNARY, seq(
      field('operator', '!'),
      field('argument', $._preproc_expression),
    )),

    preproc_binary_expression: $ => {
      const table = [
        ['||', PREC.LOGICAL_OR],
        ['&&', PREC.LOGICAL_AND],
        ['==', PREC.EQUAL],
        ['!=', PREC.EQUAL],
      ];

      return choice(...table.map(([operator, precedence]) => {
        return prec.left(precedence, seq(
          field('left', $._preproc_expression),
          // @ts-ignore
          field('operator', operator),
          field('right', $._preproc_expression),
        ));
      }));
    },

    preproc_region: $ => seq(
      preprocessor('region'),
      optional(field('content', $.preproc_arg)),
      /\n/,
    ),

    preproc_endregion: $ => seq(
      preprocessor('endregion'),
      optional(field('content', $.preproc_arg)),
      /\n/,
    ),

    preproc_line: $ => seq(
      preprocessor('line'),
      choice(
        'default',
        'hidden',
        seq($.integer_literal, optional($.string_literal)),
        seq(
          '(', $.integer_literal, ',', $.integer_literal, ')',
          '-',
          '(', $.integer_literal, ',', $.integer_literal, ')',
          optional($.integer_literal),
          $.string_literal,
        ),
      ),
      /\n/,
    ),

    preproc_pragma: $ => seq(
      preprocessor('pragma'),
      choice(
        seq('warning',
          choice('disable', 'restore'),
          commaSep(
            choice(
              $.identifier,
              $.integer_literal,
            ))),
        seq('checksum', $.string_literal, $.string_literal, $.string_literal),
      ),
      /\n/,
    ),

    preproc_nullable: _ => seq(
      preprocessor('nullable'),
      choice('enable', 'disable', 'restore'),
      optional(choice('annotations', 'warnings')),
      /\n/,
    ),

    preproc_error: $ => seq(
      preprocessor('error'),
      $.preproc_arg,
      /\n/,
    ),

    preproc_warning: $ => seq(
      preprocessor('warning'),
      $.preproc_arg,
      /\n/,
    ),

    preproc_define: $ => seq(
      preprocessor('define'),
      $.preproc_arg,
      /\n/,
    ),

    preproc_undef: $ => seq(
      preprocessor('undef'),
      $.preproc_arg,
      /\n/,
    ),

    shebang_directive: _ => token(seq('#!', /.*/)),

    comment: _ => token(choice(
      seq('//', /[^\n\r]*/),
      seq(
        '/*',
        /[^*]*\*+([^/*][^*]*\*+)*/,
        '/',
      ),
    )),
  },
});

/**
 * Creates a preprocessor regex rule
 *
 * @param {RegExp | Rule | string} command
 *
 * @returns {AliasRule}
 */
function preprocessor(command) {
  return alias(new RegExp('#[ \t]*' + command), '#' + command);
}

/**
 *
 * @param {string} suffix
 *
 * @param {RuleBuilder<string>} content
 *
 * @param {number} precedence
 *
 * @param {boolean} rep
 *
 * @returns {RuleBuilders<string, string>}
 */
function preprocIf(suffix, content, precedence = 0, rep = true) {
  /**
   *
   * @param {GrammarSymbols<string>} $
   *
   * @returns {ChoiceRule}
   */
  function alternativeBlock($) {
    return choice(
      suffix ? alias($['preproc_else' + suffix], $.preproc_else) : $.preproc_else,
      suffix ? alias($['preproc_elif' + suffix], $.preproc_elif) : $.preproc_elif,
    );
  }

  return {
    ['preproc_if' + suffix]: $ => prec(precedence, seq(
      preprocessor('if'),
      field('condition', $._preproc_expression),
      /\n/,
      rep ? repeat(content($)) : optional(content($)),
      field('alternative', optional(alternativeBlock($))),
      preprocessor('endif'),
    )),

    ['preproc_else' + suffix]: $ => prec(precedence, seq(
      preprocessor('else'),
      rep ? repeat(content($)) : optional(content($)),
    )),

    ['preproc_elif' + suffix]: $ => prec(precedence, seq(
      preprocessor('elif'),
      field('condition', $._preproc_expression),
      /\n/,
      rep ? repeat(content($)) : optional(content($)),
      field('alternative', optional(alternativeBlock($))),
    )),
  };
}

/**
 * Creates a rule to match one or more of the rules separated by a comma
 *
 * @param {Rule} rule
 *
 * @returns {SeqRule}
 */
function commaSep1(rule) {
  return seq(rule, repeat(seq(',', rule)));
}

/**
 * Creates a rule to match two or more of the rules separated by a comma
 *
 * @param {Rule} rule
 *
 * @returns {SeqRule}
 */
function commaSep2(rule) {
  return seq(rule, repeat1(seq(',', rule)));
}

/**
 * Creates a rule to optionally match one or more of the rules separated by a comma
 *
 * @param {Rule} rule
 *
 * @returns {ChoiceRule}
 */
function commaSep(rule) {
  return optional(commaSep1(rule));
}

/**
 * Creates a rule to match one or more of the rules separated by `separator`
 *
 * @param {RuleOrLiteral} rule
 *
 * @param {RuleOrLiteral} separator
 *
 * @returns {SeqRule}
 */
function sep1(rule, separator) {
  return seq(rule, repeat(seq(separator, rule)));
}

/**
 * Creates a rule to optionally match one or more of the rules separated by `separator`
 *
 * @param {RuleOrLiteral} rule
 *
 * @param {RuleOrLiteral} separator
 *
 * @returns {ChoiceRule}
 */
function sep(rule, separator) {
  return optional(sep1(rule, separator));
}
```

## File: `package.json`
```json
{
  "name": "tree-sitter-c-sharp",
  "version": "0.23.1",
  "description": "C# grammar for tree-sitter",
  "type": "module",
  "repository": "https://github.com/tree-sitter/tree-sitter-c-sharp",
  "license": "MIT",
  "author": {
    "name": "Max Brunsfeld",
    "email": "maxbrunsfeld@gmail.com"
  },
  "maintainers": [
    {
      "name": "Amaan Qureshi",
      "email": "amaanq12@gmail.com"
    },
    {
      "name": "Damien Guard",
      "email": "damieng@gmail.com"
    }
  ],
  "main": "bindings/node",
  "types": "bindings/node",
  "keywords": [
    "incremental",
    "parsing",
    "tree-sitter",
    "c-sharp"
  ],
  "files": [
    "grammar.js",
    "tree-sitter.json",
    "binding.gyp",
    "prebuilds/**",
    "bindings/node/*",
    "queries/*",
    "src/**",
    "*.wasm"
  ],
  "dependencies": {
    "node-addon-api": "^8.2.2",
    "node-gyp-build": "^4.8.4"
  },
  "devDependencies": {
    "eslint": "^9.15.0",
    "eslint-config-treesitter": "^1.0.2",
    "prebuildify": "^6.0.1",
    "tree-sitter": "^0.25.0",
    "tree-sitter-cli": "^0.26.5"
  },
  "peerDependencies": {
    "tree-sitter": "^0.25.0"
  },
  "peerDependenciesMeta": {
    "tree-sitter": {
      "optional": true
    }
  },
  "scripts": {
    "install": "node-gyp-build",
    "lint": "eslint grammar.js",
    "prestart": "tree-sitter build --wasm",
    "start": "tree-sitter playground",
    "test": "node --test bindings/node/*_test.js"
  }
}
```

## File: `pyproject.toml`
```
[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "tree-sitter-c-sharp"
description = "C# grammar for tree-sitter"
version = "0.23.1"
keywords = ["incremental", "parsing", "tree-sitter", "c-sharp"]
classifiers = [
  "Intended Audience :: Developers",
  "License :: OSI Approved :: MIT License",
  "Topic :: Software Development :: Compilers",
  "Topic :: Text Processing :: Linguistic",
  "Typing :: Typed",
]
authors = [
  { name = "Max Brunsfeld", email = "maxbrunsfeld@gmail.com" },
  { name = "Amaan Qureshi", email = "amaanq12@gmail.com" },
]
requires-python = ">=3.9"
license.text = "MIT"
readme = "README.md"

[project.urls]
Homepage = "https://github.com/tree-sitter/tree-sitter-c-sharp"

[project.optional-dependencies]
core = ["tree-sitter~=0.22"]

[tool.cibuildwheel]
build = "cp39-*"
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
            dest = path.join(self.build_lib, "tree_sitter_c-sharp", "queries")
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
        "tree_sitter_c_sharp": ["*.pyi", "py.typed"],
        "tree_sitter_c_sharp.queries": ["*.scm"],
    },
    ext_package="tree_sitter_c_sharp",
    ext_modules=[
        Extension(
            name="_binding",
            sources=[
                "bindings/python/tree_sitter_c_sharp/binding.c",
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
  "grammars": [
    {
      "name": "c-sharp",
      "camelcase": "CSharp",
      "scope": "source.cs",
      "path": ".",
      "file-types": [
        "cs"
      ],
      "highlights": [
        "queries/highlights.scm"
      ],
      "tags": [
        "queries/tags.scm"
      ],
      "injection-regex": "cs"
    }
  ],
  "metadata": {
    "version": "0.23.1",
    "license": "MIT",
    "description": "C# grammar for tree-sitter",
    "authors": [
      {
        "name": "Max Brunsfeld",
        "email": "maxbrunsfeld@gmail.com"
      },
      {
        "name": "Amaan Qureshi",
        "email": "amaanq12@gmail.com"
      },
      {
        "name": "Damien Guard",
        "email": "damieng@gmail.com"
      }
    ],
    "links": {
      "repository": "https://github.com/tree-sitter/tree-sitter-c-sharp"
    }
  },
  "bindings": {
    "c": true,
    "go": true,
    "node": true,
    "python": true,
    "rust": true,
    "swift": true
  }
}
```

## File: `bindings/c/tree-sitter-c-sharp.h`
```c
#ifndef TREE_SITTER_C_SHARP_H_
#define TREE_SITTER_C_SHARP_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_c_sharp(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_C_SHARP_H_
```

## File: `bindings/c/tree-sitter-c-sharp.pc.in`
```
prefix=@CMAKE_INSTALL_PREFIX@
libdir=${prefix}/@CMAKE_INSTALL_LIBDIR@
includedir=${prefix}/@CMAKE_INSTALL_INCLUDEDIR@

Name: tree-sitter-c-sharp
Description: @PROJECT_DESCRIPTION@
URL: @PROJECT_HOMEPAGE_URL@
Version: @PROJECT_VERSION@
Libs: -L${libdir} -ltree-sitter-c-sharp
Cflags: -I${includedir}
```

## File: `bindings/go/binding.go`
```go
package tree_sitter_c_sharp

// #cgo CFLAGS: -std=c11 -fPIC
// #include "../../src/parser.c"
// #if __has_include("../../src/scanner.c")
// #include "../../src/scanner.c"
// #endif
import "C"

import "unsafe"

// Get the tree-sitter Language for this grammar.
func Language() unsafe.Pointer {
	return unsafe.Pointer(C.tree_sitter_c_sharp())
}
```

## File: `bindings/go/binding_test.go`
```go
package tree_sitter_c_sharp_test

import (
	"testing"

	tree_sitter "github.com/tree-sitter/go-tree-sitter"
	tree_sitter_c_sharp "github.com/tree-sitter/tree-sitter-c-sharp/bindings/go"
)

func TestCanLoadGrammar(t *testing.T) {
	language := tree_sitter.NewLanguage(tree_sitter_c_sharp.Language())
	if language == nil {
		t.Errorf("Error loading CSharp grammar")
	}
}
```

## File: `bindings/node/binding.cc`
```
#include <napi.h>

typedef struct TSLanguage TSLanguage;

extern "C" TSLanguage *tree_sitter_c_sharp();

// "tree-sitter", "language" hashed with BLAKE2
const napi_type_tag LANGUAGE_TYPE_TAG = {
    0x8AF2E5212AD58ABF, 0xD5006CAD83ABBA16
};

Napi::Object Init(Napi::Env env, Napi::Object exports) {
    auto language = Napi::External<TSLanguage>::New(env, tree_sitter_c_sharp());
    language.TypeTag(&LANGUAGE_TYPE_TAG);
    exports["language"] = language;
    return exports;
}

NODE_API_MODULE(tree_sitter_c_sharp_binding, Init)
```

## File: `bindings/node/binding_test.js`
```javascript
import assert from "node:assert";
import { test } from "node:test";
import Parser from "tree-sitter";

test("can load grammar", () => {
  const parser = new Parser();
  assert.doesNotReject(async () => {
    const { default: language } = await import("./index.js");
    parser.setLanguage(language);
  });
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

/**
 * The tree-sitter language object for this grammar.
 *
 * @see {@linkcode https://tree-sitter.github.io/node-tree-sitter/interfaces/Parser.Language.html Parser.Language}
 *
 * @example
 * import Parser from "tree-sitter";
 * import CSharp from "tree-sitter-c-sharp";
 *
 * const parser = new Parser();
 * parser.setLanguage(CSharp);
 */
declare const binding: {
  /**
   * The inner language object.
   * @private
   */
  language: unknown;

  /**
   * The content of the `node-types.json` file for this grammar.
   *
   * @see {@linkplain https://tree-sitter.github.io/tree-sitter/using-parsers/6-static-node-types Static Node Types}
   */
  nodeTypeInfo: NodeInfo[];

  /** The syntax highlighting query for this grammar. */
  HIGHLIGHTS_QUERY?: string;

  /** The language injection query for this grammar. */
  INJECTIONS_QUERY?: string;

  /** The local variable query for this grammar. */
  LOCALS_QUERY?: string;

  /** The symbol tagging query for this grammar. */
  TAGS_QUERY?: string;
};

export default binding;
```

## File: `bindings/node/index.js`
```javascript
import { readFileSync } from "node:fs";
import { fileURLToPath } from "node:url";

const root = fileURLToPath(new URL("../..", import.meta.url));

const binding = typeof process.versions.bun === "string"
  // Support `bun build --compile` by being statically analyzable enough to find the .node file at build-time
  ? await import(`${root}/prebuilds/${process.platform}-${process.arch}/tree-sitter-c-sharp.node`)
  : (await import("node-gyp-build")).default(root);

try {
  const nodeTypes = await import(`${root}/src/node-types.json`, { with: { type: "json" } });
  binding.nodeTypeInfo = nodeTypes.default;
} catch { }

const queries = [
  ["HIGHLIGHTS_QUERY", `${root}/queries/highlights.scm`],
  ["INJECTIONS_QUERY", `${root}/queries/injections.scm`],
  ["LOCALS_QUERY", `${root}/queries/locals.scm`],
  ["TAGS_QUERY", `${root}/queries/tags.scm`],
];

for (const [prop, path] of queries) {
  Object.defineProperty(binding, prop, {
    configurable: true,
    enumerable: true,
    get() {
      delete binding[prop];
      try {
        binding[prop] = readFileSync(path, "utf8");
      } catch { }
      return binding[prop];
    }
  });
}

export default binding;
```

## File: `bindings/python/tests/test_binding.py`
```python
from unittest import TestCase

from tree_sitter import Language, Parser
import tree_sitter_c_sharp


class TestLanguage(TestCase):
    def test_can_load_grammar(self):
        try:
            Parser(Language(tree_sitter_c_sharp.language()))
        except Exception:
            self.fail("Error loading CSharp grammar")
```

## File: `bindings/python/tree_sitter_c_sharp/__init__.py`
```python
"""C# grammar for tree-sitter"""

from importlib.resources import files as _files

from ._binding import language


def _get_query(name, file):
    try:
        query = _files(f"{__package__}") / file
        globals()[name] = query.read_text()
    except FileNotFoundError:
        globals()[name] = None
    return globals()[name]


def __getattr__(name):
    if name == "HIGHLIGHTS_QUERY":
        return _get_query("HIGHLIGHTS_QUERY", "queries/highlights.scm")
    if name == "INJECTIONS_QUERY":
        return _get_query("INJECTIONS_QUERY", "queries/injections.scm")
    if name == "LOCALS_QUERY":
        return _get_query("LOCALS_QUERY", "queries/locals.scm")
    if name == "TAGS_QUERY":
        return _get_query("TAGS_QUERY", "queries/tags.scm")

    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")


__all__ = [
    "language",
    "HIGHLIGHTS_QUERY",
    "INJECTIONS_QUERY",
    "LOCALS_QUERY",
    "TAGS_QUERY",
]


def __dir__():
    return sorted(__all__ + [
        "__all__", "__builtins__", "__cached__", "__doc__", "__file__",
        "__loader__", "__name__", "__package__", "__path__", "__spec__",
    ])
```

## File: `bindings/python/tree_sitter_c_sharp/__init__.pyi`
```
from typing import Final
from typing_extensions import CapsuleType

HIGHLIGHTS_QUERY: Final[str] | None
"""The syntax highlighting query for this grammar."""

INJECTIONS_QUERY: Final[str] | None
"""The language injection query for this grammar."""

LOCALS_QUERY: Final[str] | None
"""The local variable query for this grammar."""

TAGS_QUERY: Final[str] | None
"""The symbol tagging query for this grammar."""

def language() -> CapsuleType:
    """The tree-sitter language function for this grammar."""
```

## File: `bindings/python/tree_sitter_c_sharp/binding.c`
```c
#include <Python.h>

typedef struct TSLanguage TSLanguage;

TSLanguage *tree_sitter_c_sharp(void);

static PyObject* _binding_language(PyObject *Py_UNUSED(self), PyObject *Py_UNUSED(args)) {
    return PyCapsule_New(tree_sitter_c_sharp(), "tree_sitter.Language", NULL);
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

    if std::env::var("TARGET").unwrap() == "wasm32-unknown-unknown" {
        let Ok(wasm_headers) = std::env::var("DEP_TREE_SITTER_LANGUAGE_WASM_HEADERS") else {
            panic!("Environment variable DEP_TREE_SITTER_LANGUAGE_WASM_HEADERS must be set by the language crate");
        };
        let Ok(wasm_src) =
            std::env::var("DEP_TREE_SITTER_LANGUAGE_WASM_SRC").map(std::path::PathBuf::from)
        else {
            panic!("Environment variable DEP_TREE_SITTER_LANGUAGE_WASM_SRC must be set by the language crate");
        };

        c_config.include(&wasm_headers);
        c_config.files([
            wasm_src.join("stdio.c"),
            wasm_src.join("stdlib.c"),
            wasm_src.join("string.c"),
        ]);
    }

    let parser_path = src_dir.join("parser.c");
    c_config.file(&parser_path);
    println!("cargo:rerun-if-changed={}", parser_path.to_str().unwrap());

    let scanner_path = src_dir.join("scanner.c");
    if scanner_path.exists() {
        c_config.file(&scanner_path);
        println!("cargo:rerun-if-changed={}", scanner_path.to_str().unwrap());
    }

    c_config.compile("tree-sitter-c-sharp");

    println!("cargo:rustc-check-cfg=cfg(with_highlights_query)");
    if !"queries/highlights.scm".is_empty() && std::path::Path::new("queries/highlights.scm").exists() {
        println!("cargo:rustc-cfg=with_highlights_query");
    }
    println!("cargo:rustc-check-cfg=cfg(with_injections_query)");
    if !"queries/injections.scm".is_empty() && std::path::Path::new("queries/injections.scm").exists() {
        println!("cargo:rustc-cfg=with_injections_query");
    }
    println!("cargo:rustc-check-cfg=cfg(with_locals_query)");
    if !"queries/locals.scm".is_empty() && std::path::Path::new("queries/locals.scm").exists() {
        println!("cargo:rustc-cfg=with_locals_query");
    }
    println!("cargo:rustc-check-cfg=cfg(with_tags_query)");
    if !"queries/tags.scm".is_empty() && std::path::Path::new("queries/tags.scm").exists() {
        println!("cargo:rustc-cfg=with_tags_query");
    }
}
```

## File: `bindings/rust/lib.rs`
```rust
//! This crate provides CSharp language support for the [tree-sitter] parsing library.
//!
//! Typically, you will use the [`LANGUAGE`] constant to add this language to a
//! tree-sitter [`Parser`], and then use the parser to parse some code:
//!
//! ```
//! let code = r#"
//! "#;
//! let mut parser = tree_sitter::Parser::new();
//! let language = tree_sitter_c_sharp::LANGUAGE;
//! parser
//!     .set_language(&language.into())
//!     .expect("Error loading CSharp parser");
//! let tree = parser.parse(code, None).unwrap();
//! assert!(!tree.root_node().has_error());
//! ```
//!
//! [`Parser`]: https://docs.rs/tree-sitter/0.26.3/tree_sitter/struct.Parser.html
//! [tree-sitter]: https://tree-sitter.github.io/

use tree_sitter_language::LanguageFn;

extern "C" {
    fn tree_sitter_c_sharp() -> *const ();
}

/// The tree-sitter [`LanguageFn`] for this grammar.
pub const LANGUAGE: LanguageFn = unsafe { LanguageFn::from_raw(tree_sitter_c_sharp) };

/// The content of the [`node-types.json`] file for this grammar.
///
/// [`node-types.json`]: https://tree-sitter.github.io/tree-sitter/using-parsers/6-static-node-types
pub const NODE_TYPES: &str = include_str!("../../src/node-types.json");

#[cfg(with_highlights_query)]
/// The syntax highlighting query for this grammar.
pub const HIGHLIGHTS_QUERY: &str = include_str!("../../queries/highlights.scm");

#[cfg(with_injections_query)]
/// The language injection query for this grammar.
pub const INJECTIONS_QUERY: &str = include_str!("../../queries/injections.scm");

#[cfg(with_locals_query)]
/// The local variable query for this grammar.
pub const LOCALS_QUERY: &str = include_str!("../../queries/locals.scm");

#[cfg(with_tags_query)]
/// The symbol tagging query for this grammar.
pub const TAGS_QUERY: &str = include_str!("../../queries/tags.scm");

#[cfg(test)]
mod tests {
    #[test]
    fn test_can_load_grammar() {
        let mut parser = tree_sitter::Parser::new();
        parser
            .set_language(&super::LANGUAGE.into())
            .expect("Error loading CSharp parser");
    }
}
```

## File: `bindings/swift/TreeSitterCSharp/c-sharp.h`
```c
#ifndef TREE_SITTER_C_SHARP_H_
#define TREE_SITTER_C_SHARP_H_

typedef struct TSLanguage TSLanguage;

#ifdef __cplusplus
extern "C" {
#endif

const TSLanguage *tree_sitter_c_sharp(void);

#ifdef __cplusplus
}
#endif

#endif // TREE_SITTER_C_SHARP_H_
```

## File: `bindings/swift/TreeSitterCSharpTests/TreeSitterCSharpTests.swift`
```
import XCTest
import SwiftTreeSitter
import TreeSitterCSharp

final class TreeSitterCSharpTests: XCTestCase {
    func testCanLoadGrammar() throws {
        let parser = Parser()
        let language = Language(language: tree_sitter_c_sharp())
        XCTAssertNoThrow(try parser.setLanguage(language),
                         "Error loading CSharp grammar")
    }
}
```

## File: `queries/highlights.scm`
```
(identifier) @variable

;; Methods

(method_declaration name: (identifier) @function)
(local_function_statement name: (identifier) @function)

;; Types

(interface_declaration name: (identifier) @type)
(class_declaration name: (identifier) @type)
(enum_declaration name: (identifier) @type)
(struct_declaration (identifier) @type)
(record_declaration (identifier) @type)
(namespace_declaration name: (identifier) @module)

(generic_name (identifier) @type)
(type_parameter (identifier) @property.definition)
(parameter type: (identifier) @type)
(type_argument_list (identifier) @type)
(as_expression right: (identifier) @type)
(is_expression right: (identifier) @type)

(constructor_declaration name: (identifier) @constructor)
(destructor_declaration name: (identifier) @constructor)

(_ type: (identifier) @type)

(base_list (identifier) @type)

(predefined_type) @type.builtin

;; Enum
(enum_member_declaration (identifier) @property.definition)

;; Literals

[
  (real_literal)
  (integer_literal)
] @number

[
  (character_literal)
  (string_literal)
  (raw_string_literal)
  (verbatim_string_literal)
  (interpolated_string_expression)
  (interpolation_start)
  (interpolation_quote)
 ] @string

(escape_sequence) @string.escape

[
  (boolean_literal)
  (null_literal)
] @constant.builtin

;; Comments

(comment) @comment

;; Tokens

[
  ";"
  "."
  ","
] @punctuation.delimiter

[
  "--"
  "-"
  "-="
  "&"
  "&="
  "&&"
  "+"
  "++"
  "+="
  "<"
  "<="
  "<<"
  "<<="
  "="
  "=="
  "!"
  "!="
  "=>"
  ">"
  ">="
  ">>"
  ">>="
  ">>>"
  ">>>="
  "|"
  "|="
  "||"
  "?"
  "??"
  "??="
  "^"
  "^="
  "~"
  "*"
  "*="
  "/"
  "/="
  "%"
  "%="
  ":"
] @operator

[
  "("
  ")"
  "["
  "]"
  "{"
  "}"
  (interpolation_brace)
]  @punctuation.bracket

;; Keywords

[
  (modifier)
  "this"
  (implicit_type)
] @keyword

[
  "add"
  "alias"
  "as"
  "base"
  "break"
  "case"
  "catch"
  "checked"
  "class"
  "continue"
  "default"
  "delegate"
  "do"
  "else"
  "enum"
  "event"
  "explicit"
  "extern"
  "finally"
  "for"
  "foreach"
  "global"
  "goto"
  "if"
  "implicit"
  "interface"
  "is"
  "lock"
  "namespace"
  "notnull"
  "operator"
  "params"
  "return"
  "remove"
  "sizeof"
  "stackalloc"
  "static"
  "struct"
  "switch"
  "throw"
  "try"
  "typeof"
  "unchecked"
  "using"
  "while"
  "new"
  "await"
  "in"
  "yield"
  "get"
  "set"
  "when"
  "out"
  "ref"
  "from"
  "where"
  "select"
  "record"
  "init"
  "with"
  "let"
] @keyword

;; Attribute

(attribute name: (identifier) @attribute)

;; Parameters

(parameter
  name: (identifier) @variable.parameter)

;; Type constraints

(type_parameter_constraints_clause (identifier) @property.definition)

;; Method calls

(invocation_expression (member_access_expression name: (identifier) @function))
```

## File: `queries/tags.scm`
```
(class_declaration name: (identifier) @name) @definition.class

(class_declaration (base_list (_) @name)) @reference.class

(interface_declaration name: (identifier) @name) @definition.interface

(interface_declaration (base_list (_) @name)) @reference.interface

(method_declaration name: (identifier) @name) @definition.method

(object_creation_expression type: (identifier) @name) @reference.class

(type_parameter_constraints_clause (identifier) @name) @reference.class

(type_parameter_constraint (type type: (identifier) @name)) @reference.class

(variable_declaration type: (identifier) @name) @reference.class

(invocation_expression function: (member_access_expression name: (identifier) @name)) @reference.send

(namespace_declaration name: (identifier) @name) @definition.module

(namespace_declaration name: (identifier) @name) @module
```

## File: `src/grammar.json`
```json
{
  "$schema": "https://tree-sitter.github.io/tree-sitter/assets/schemas/grammar.schema.json",
  "name": "c_sharp",
  "word": "_identifier_token",
  "rules": {
    "compilation_unit": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "shebang_directive"
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
            "name": "_top_level_item"
          }
        }
      ]
    },
    "_top_level_item": {
      "type": "PREC",
      "value": 2,
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "SYMBOL",
            "name": "_top_level_item_no_statement"
          },
          {
            "type": "SYMBOL",
            "name": "global_statement"
          }
        ]
      }
    },
    "_top_level_item_no_statement": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "extern_alias_directive"
        },
        {
          "type": "SYMBOL",
          "name": "using_directive"
        },
        {
          "type": "SYMBOL",
          "name": "global_attribute"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "preproc_if_in_top_level"
          },
          "named": true,
          "value": "preproc_if"
        },
        {
          "type": "SYMBOL",
          "name": "_namespace_member_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "file_scoped_namespace_declaration"
        }
      ]
    },
    "global_statement": {
      "type": "PREC",
      "value": 1,
      "content": {
        "type": "SYMBOL",
        "name": "statement"
      }
    },
    "extern_alias_directive": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "extern"
        },
        {
          "type": "STRING",
          "value": "alias"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "using_directive": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "global"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "using"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "STRING",
                      "value": "unsafe"
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                },
                {
                  "type": "FIELD",
                  "name": "name",
                  "content": {
                    "type": "SYMBOL",
                    "name": "identifier"
                  }
                },
                {
                  "type": "STRING",
                  "value": "="
                },
                {
                  "type": "SYMBOL",
                  "name": "type"
                }
              ]
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "CHOICE",
                    "members": [
                      {
                        "type": "STRING",
                        "value": "static"
                      },
                      {
                        "type": "STRING",
                        "value": "unsafe"
                      }
                    ]
                  }
                },
                {
                  "type": "SYMBOL",
                  "name": "_name"
                }
              ]
            }
          ]
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "global_attribute": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "assembly"
            },
            {
              "type": "STRING",
              "value": "module"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ":"
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "attribute"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "attribute"
                  }
                ]
              }
            }
          ]
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "]"
        }
      ]
    },
    "attribute": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "_name"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "attribute_argument_list"
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "attribute_argument_list": {
      "type": "PREC",
      "value": -1,
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
                "type": "SEQ",
                "members": [
                  {
                    "type": "SYMBOL",
                    "name": "attribute_argument"
                  },
                  {
                    "type": "REPEAT",
                    "content": {
                      "type": "SEQ",
                      "members": [
                        {
                          "type": "STRING",
                          "value": ","
                        },
                        {
                          "type": "SYMBOL",
                          "name": "attribute_argument"
                        }
                      ]
                    }
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "STRING",
            "value": ")"
          }
        ]
      }
    },
    "attribute_argument": {
      "type": "PREC",
      "value": -1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "PREC",
                "value": 1,
                "content": {
                  "type": "SEQ",
                  "members": [
                    {
                      "type": "FIELD",
                      "name": "name",
                      "content": {
                        "type": "SYMBOL",
                        "name": "identifier"
                      }
                    },
                    {
                      "type": "CHOICE",
                      "members": [
                        {
                          "type": "STRING",
                          "value": ":"
                        },
                        {
                          "type": "STRING",
                          "value": "="
                        }
                      ]
                    }
                  ]
                }
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "SYMBOL",
            "name": "expression"
          }
        ]
      }
    },
    "attribute_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "attribute_target_specifier"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "attribute"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "attribute"
                  }
                ]
              }
            }
          ]
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "]"
        }
      ]
    },
    "_attribute_list": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "attribute_list"
        },
        {
          "type": "SYMBOL",
          "name": "preproc_if_in_attribute_list"
        }
      ]
    },
    "attribute_target_specifier": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "field"
            },
            {
              "type": "STRING",
              "value": "event"
            },
            {
              "type": "STRING",
              "value": "method"
            },
            {
              "type": "STRING",
              "value": "param"
            },
            {
              "type": "STRING",
              "value": "property"
            },
            {
              "type": "STRING",
              "value": "return"
            },
            {
              "type": "STRING",
              "value": "type"
            },
            {
              "type": "STRING",
              "value": "typevar"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ":"
        }
      ]
    },
    "_namespace_member_declaration": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "namespace_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "type_declaration"
        }
      ]
    },
    "namespace_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "namespace"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "_name"
          }
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "declaration_list"
          }
        },
        {
          "type": "SYMBOL",
          "name": "_optional_semi"
        }
      ]
    },
    "file_scoped_namespace_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "namespace"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "_name"
          }
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "type_declaration": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "class_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "struct_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "enum_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "interface_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "delegate_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "record_declaration"
        }
      ]
    },
    "class_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_class_declaration_initializer"
        },
        {
          "type": "SYMBOL",
          "name": "_declaration_list_body"
        }
      ]
    },
    "_class_declaration_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "STRING",
          "value": "class"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "type_parameter_list"
              },
              {
                "type": "SYMBOL",
                "name": "parameter_list"
              },
              {
                "type": "SYMBOL",
                "name": "base_list"
              }
            ]
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "type_parameter_constraints_clause"
          }
        }
      ]
    },
    "struct_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_struct_declaration_initializer"
        },
        {
          "type": "SYMBOL",
          "name": "_declaration_list_body"
        }
      ]
    },
    "_struct_declaration_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "ref"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "struct"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "type_parameter_list"
              },
              {
                "type": "SYMBOL",
                "name": "parameter_list"
              },
              {
                "type": "SYMBOL",
                "name": "base_list"
              }
            ]
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "type_parameter_constraints_clause"
          }
        }
      ]
    },
    "enum_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_enum_declaration_initializer"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "FIELD",
                  "name": "body",
                  "content": {
                    "type": "SYMBOL",
                    "name": "enum_member_declaration_list"
                  }
                },
                {
                  "type": "SYMBOL",
                  "name": "_optional_semi"
                }
              ]
            },
            {
              "type": "STRING",
              "value": ";"
            }
          ]
        }
      ]
    },
    "_enum_declaration_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "STRING",
          "value": "enum"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "base_list"
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "enum_member_declaration_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "enum_member_declaration"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_if_in_enum_member_declaration"
                      },
                      "named": true,
                      "value": "preproc_if"
                    }
                  ]
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "CHOICE",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "enum_member_declaration"
                          },
                          {
                            "type": "ALIAS",
                            "content": {
                              "type": "SYMBOL",
                              "name": "preproc_if_in_enum_member_declaration"
                            },
                            "named": true,
                            "value": "preproc_if"
                          }
                        ]
                      }
                    ]
                  }
                }
              ]
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
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "enum_member_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "="
                },
                {
                  "type": "FIELD",
                  "name": "value",
                  "content": {
                    "type": "SYMBOL",
                    "name": "expression"
                  }
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "interface_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_interface_declaration_initializer"
        },
        {
          "type": "SYMBOL",
          "name": "_declaration_list_body"
        }
      ]
    },
    "_interface_declaration_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "STRING",
          "value": "interface"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type_parameters",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "type_parameter_list"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "base_list"
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
            "name": "type_parameter_constraints_clause"
          }
        }
      ]
    },
    "delegate_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_delegate_declaration_initializer"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "type_parameter_constraints_clause"
          }
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "_delegate_declaration_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "STRING",
          "value": "delegate"
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type_parameters",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "type_parameter_list"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "parameter_list"
          }
        }
      ]
    },
    "record_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_record_declaration_initializer"
        },
        {
          "type": "SYMBOL",
          "name": "_declaration_list_body"
        }
      ]
    },
    "_record_declaration_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "STRING",
          "value": "record"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "STRING",
                  "value": "class"
                },
                {
                  "type": "STRING",
                  "value": "struct"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "type_parameter_list"
              },
              {
                "type": "SYMBOL",
                "name": "parameter_list"
              }
            ]
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "record_base"
              },
              "named": true,
              "value": "base_list"
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
            "name": "type_parameter_constraints_clause"
          }
        }
      ]
    },
    "record_base": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": ":"
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "_name"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "_name"
                      }
                    ]
                  }
                }
              ]
            }
          ]
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": ":"
            },
            {
              "type": "SYMBOL",
              "name": "primary_constructor_base_type"
            },
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SEQ",
                  "members": [
                    {
                      "type": "STRING",
                      "value": ","
                    },
                    {
                      "type": "SEQ",
                      "members": [
                        {
                          "type": "SYMBOL",
                          "name": "_name"
                        },
                        {
                          "type": "REPEAT",
                          "content": {
                            "type": "SEQ",
                            "members": [
                              {
                                "type": "STRING",
                                "value": ","
                              },
                              {
                                "type": "SYMBOL",
                                "name": "_name"
                              }
                            ]
                          }
                        }
                      ]
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          ]
        }
      ]
    },
    "_declaration_list_body": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SEQ",
          "members": [
            {
              "type": "FIELD",
              "name": "body",
              "content": {
                "type": "SYMBOL",
                "name": "declaration_list"
              }
            },
            {
              "type": "SYMBOL",
              "name": "_optional_semi"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "primary_constructor_base_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "_name"
          }
        },
        {
          "type": "SYMBOL",
          "name": "argument_list"
        }
      ]
    },
    "modifier": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "STRING",
            "value": "abstract"
          },
          {
            "type": "STRING",
            "value": "async"
          },
          {
            "type": "STRING",
            "value": "const"
          },
          {
            "type": "STRING",
            "value": "extern"
          },
          {
            "type": "STRING",
            "value": "file"
          },
          {
            "type": "STRING",
            "value": "fixed"
          },
          {
            "type": "STRING",
            "value": "internal"
          },
          {
            "type": "STRING",
            "value": "new"
          },
          {
            "type": "STRING",
            "value": "override"
          },
          {
            "type": "STRING",
            "value": "partial"
          },
          {
            "type": "STRING",
            "value": "private"
          },
          {
            "type": "STRING",
            "value": "protected"
          },
          {
            "type": "STRING",
            "value": "public"
          },
          {
            "type": "STRING",
            "value": "readonly"
          },
          {
            "type": "STRING",
            "value": "required"
          },
          {
            "type": "STRING",
            "value": "sealed"
          },
          {
            "type": "STRING",
            "value": "static"
          },
          {
            "type": "STRING",
            "value": "unsafe"
          },
          {
            "type": "STRING",
            "value": "virtual"
          },
          {
            "type": "STRING",
            "value": "volatile"
          }
        ]
      }
    },
    "type_parameter_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "<"
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "type_parameter"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "type_parameter"
                  }
                ]
              }
            }
          ]
        },
        {
          "type": "STRING",
          "value": ">"
        }
      ]
    },
    "type_parameter": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "STRING",
                  "value": "in"
                },
                {
                  "type": "STRING",
                  "value": "out"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        }
      ]
    },
    "base_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": ":"
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "type"
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "argument_list"
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                }
              ]
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "type"
                      },
                      {
                        "type": "CHOICE",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "argument_list"
                          },
                          {
                            "type": "BLANK"
                          }
                        ]
                      }
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "type_parameter_constraints_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "where"
        },
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "STRING",
          "value": ":"
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "type_parameter_constraint"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "type_parameter_constraint"
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "type_parameter_constraint": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": "class"
            },
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "STRING",
                  "value": "?"
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          ]
        },
        {
          "type": "STRING",
          "value": "struct"
        },
        {
          "type": "STRING",
          "value": "notnull"
        },
        {
          "type": "STRING",
          "value": "unmanaged"
        },
        {
          "type": "SYMBOL",
          "name": "constructor_constraint"
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        }
      ]
    },
    "constructor_constraint": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "new"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "operator_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "explicit_interface_specifier"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "operator"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "checked"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "operator",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "!"
              },
              {
                "type": "STRING",
                "value": "~"
              },
              {
                "type": "STRING",
                "value": "++"
              },
              {
                "type": "STRING",
                "value": "--"
              },
              {
                "type": "STRING",
                "value": "true"
              },
              {
                "type": "STRING",
                "value": "false"
              },
              {
                "type": "STRING",
                "value": "+"
              },
              {
                "type": "STRING",
                "value": "-"
              },
              {
                "type": "STRING",
                "value": "*"
              },
              {
                "type": "STRING",
                "value": "/"
              },
              {
                "type": "STRING",
                "value": "%"
              },
              {
                "type": "STRING",
                "value": "^"
              },
              {
                "type": "STRING",
                "value": "|"
              },
              {
                "type": "STRING",
                "value": "&"
              },
              {
                "type": "STRING",
                "value": "<<"
              },
              {
                "type": "STRING",
                "value": ">>"
              },
              {
                "type": "STRING",
                "value": ">>>"
              },
              {
                "type": "STRING",
                "value": "=="
              },
              {
                "type": "STRING",
                "value": "!="
              },
              {
                "type": "STRING",
                "value": ">"
              },
              {
                "type": "STRING",
                "value": "<"
              },
              {
                "type": "STRING",
                "value": ">="
              },
              {
                "type": "STRING",
                "value": "<="
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "parameter_list"
          }
        },
        {
          "type": "SYMBOL",
          "name": "_function_body"
        }
      ]
    },
    "conversion_operator_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "implicit"
            },
            {
              "type": "STRING",
              "value": "explicit"
            }
          ]
        },
        {
          "type": "REPEAT1",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "explicit_interface_specifier"
              },
              {
                "type": "STRING",
                "value": "operator"
              },
              {
                "type": "STRING",
                "value": "checked"
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "parameter_list"
          }
        },
        {
          "type": "SYMBOL",
          "name": "_function_body"
        }
      ]
    },
    "declaration_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "declaration"
          }
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "declaration": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "class_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "struct_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "enum_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "delegate_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "field_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "method_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "event_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "event_field_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "record_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "constructor_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "destructor_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "indexer_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "interface_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "namespace_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "operator_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "conversion_operator_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "property_declaration"
        },
        {
          "type": "SYMBOL",
          "name": "using_directive"
        },
        {
          "type": "SYMBOL",
          "name": "preproc_if"
        }
      ]
    },
    "field_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "SYMBOL",
          "name": "variable_declaration"
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "constructor_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_constructor_declaration_initializer"
        },
        {
          "type": "SYMBOL",
          "name": "_function_body"
        }
      ]
    },
    "_constructor_declaration_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "parameter_list"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "constructor_initializer"
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "destructor_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "extern"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "~"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "parameter_list"
          }
        },
        {
          "type": "SYMBOL",
          "name": "_function_body"
        }
      ]
    },
    "method_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "FIELD",
          "name": "returns",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "explicit_interface_specifier"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type_parameters",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "type_parameter_list"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "parameter_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "type_parameter_constraints_clause"
          }
        },
        {
          "type": "SYMBOL",
          "name": "_function_body"
        }
      ]
    },
    "event_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "STRING",
          "value": "event"
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "explicit_interface_specifier"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "accessors",
              "content": {
                "type": "SYMBOL",
                "name": "accessor_list"
              }
            },
            {
              "type": "STRING",
              "value": ";"
            }
          ]
        }
      ]
    },
    "event_field_declaration": {
      "type": "PREC_DYNAMIC",
      "value": 1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "_attribute_list"
            }
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "modifier"
            }
          },
          {
            "type": "STRING",
            "value": "event"
          },
          {
            "type": "SYMBOL",
            "name": "variable_declaration"
          },
          {
            "type": "STRING",
            "value": ";"
          }
        ]
      }
    },
    "accessor_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "accessor_declaration"
          }
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "accessor_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "get"
              },
              {
                "type": "STRING",
                "value": "set"
              },
              {
                "type": "STRING",
                "value": "add"
              },
              {
                "type": "STRING",
                "value": "remove"
              },
              {
                "type": "STRING",
                "value": "init"
              },
              {
                "type": "SYMBOL",
                "name": "identifier"
              }
            ]
          }
        },
        {
          "type": "SYMBOL",
          "name": "_function_body"
        }
      ]
    },
    "indexer_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "explicit_interface_specifier"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "this"
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "bracketed_parameter_list"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "accessors",
              "content": {
                "type": "SYMBOL",
                "name": "accessor_list"
              }
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "FIELD",
                  "name": "value",
                  "content": {
                    "type": "SYMBOL",
                    "name": "arrow_expression_clause"
                  }
                },
                {
                  "type": "STRING",
                  "value": ";"
                }
              ]
            }
          ]
        }
      ]
    },
    "bracketed_parameter_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "parameter"
                    },
                    {
                      "type": "SYMBOL",
                      "name": "_parameter_array"
                    }
                  ]
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "CHOICE",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "parameter"
                          },
                          {
                            "type": "SYMBOL",
                            "name": "_parameter_array"
                          }
                        ]
                      }
                    ]
                  }
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "]"
        }
      ]
    },
    "property_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "explicit_interface_specifier"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "FIELD",
                  "name": "accessors",
                  "content": {
                    "type": "SYMBOL",
                    "name": "accessor_list"
                  }
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SEQ",
                      "members": [
                        {
                          "type": "STRING",
                          "value": "="
                        },
                        {
                          "type": "FIELD",
                          "name": "value",
                          "content": {
                            "type": "SYMBOL",
                            "name": "expression"
                          }
                        },
                        {
                          "type": "STRING",
                          "value": ";"
                        }
                      ]
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                }
              ]
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "FIELD",
                  "name": "value",
                  "content": {
                    "type": "SYMBOL",
                    "name": "arrow_expression_clause"
                  }
                },
                {
                  "type": "STRING",
                  "value": ";"
                }
              ]
            }
          ]
        }
      ]
    },
    "explicit_interface_specifier": {
      "type": "PREC",
      "value": 18,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "SYMBOL",
            "name": "_name"
          },
          {
            "type": "STRING",
            "value": "."
          }
        ]
      }
    },
    "parameter_list": {
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
              "type": "SEQ",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "parameter"
                    },
                    {
                      "type": "SYMBOL",
                      "name": "_parameter_array"
                    }
                  ]
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "CHOICE",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "parameter"
                          },
                          {
                            "type": "SYMBOL",
                            "name": "_parameter_array"
                          }
                        ]
                      }
                    ]
                  }
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "_parameter_type_with_modifiers": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "PREC_LEFT",
            "value": 0,
            "content": {
              "type": "ALIAS",
              "content": {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "STRING",
                    "value": "this"
                  },
                  {
                    "type": "STRING",
                    "value": "scoped"
                  },
                  {
                    "type": "STRING",
                    "value": "ref"
                  },
                  {
                    "type": "STRING",
                    "value": "out"
                  },
                  {
                    "type": "STRING",
                    "value": "in"
                  },
                  {
                    "type": "STRING",
                    "value": "readonly"
                  }
                ]
              },
              "named": true,
              "value": "modifier"
            }
          }
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        }
      ]
    },
    "parameter": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "_parameter_type_with_modifiers"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "="
                },
                {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "_parameter_array": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "STRING",
          "value": "params"
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        }
      ]
    },
    "constructor_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": ":"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "base"
            },
            {
              "type": "STRING",
              "value": "this"
            }
          ]
        },
        {
          "type": "SYMBOL",
          "name": "argument_list"
        }
      ]
    },
    "argument_list": {
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
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "argument"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "argument"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "tuple_pattern": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "FIELD",
                  "name": "name",
                  "content": {
                    "type": "SYMBOL",
                    "name": "identifier"
                  }
                },
                {
                  "type": "SYMBOL",
                  "name": "discard"
                },
                {
                  "type": "SYMBOL",
                  "name": "tuple_pattern"
                }
              ]
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "CHOICE",
                    "members": [
                      {
                        "type": "FIELD",
                        "name": "name",
                        "content": {
                          "type": "SYMBOL",
                          "name": "identifier"
                        }
                      },
                      {
                        "type": "SYMBOL",
                        "name": "discard"
                      },
                      {
                        "type": "SYMBOL",
                        "name": "tuple_pattern"
                      }
                    ]
                  }
                ]
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
    "argument": {
      "type": "PREC",
      "value": 1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SEQ",
                "members": [
                  {
                    "type": "FIELD",
                    "name": "name",
                    "content": {
                      "type": "SYMBOL",
                      "name": "identifier"
                    }
                  },
                  {
                    "type": "STRING",
                    "value": ":"
                  }
                ]
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
                "type": "CHOICE",
                "members": [
                  {
                    "type": "STRING",
                    "value": "ref"
                  },
                  {
                    "type": "STRING",
                    "value": "out"
                  },
                  {
                    "type": "STRING",
                    "value": "in"
                  }
                ]
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
                "type": "SYMBOL",
                "name": "expression"
              },
              {
                "type": "SYMBOL",
                "name": "declaration_expression"
              }
            ]
          }
        ]
      }
    },
    "block": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "statement"
          }
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "arrow_expression_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "=>"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "_function_body": {
      "type": "CHOICE",
      "members": [
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "block"
          }
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "FIELD",
              "name": "body",
              "content": {
                "type": "SYMBOL",
                "name": "arrow_expression_clause"
              }
            },
            {
              "type": "STRING",
              "value": ";"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "variable_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "variable_declarator"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "variable_declarator"
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "using_variable_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "using_variable_declarator"
              },
              "named": true,
              "value": "variable_declarator"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "ALIAS",
                    "content": {
                      "type": "SYMBOL",
                      "name": "using_variable_declarator"
                    },
                    "named": true,
                    "value": "variable_declarator"
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "variable_declarator": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "name",
              "content": {
                "type": "SYMBOL",
                "name": "identifier"
              }
            },
            {
              "type": "SYMBOL",
              "name": "tuple_pattern"
            }
          ]
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "bracketed_argument_list"
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
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "="
                },
                {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "using_variable_declarator": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "="
                },
                {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "bracketed_argument_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "argument"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "argument"
                  }
                ]
              }
            }
          ]
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "]"
        }
      ]
    },
    "qualified_identifier": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "STRING",
                "value": "."
              },
              {
                "type": "SYMBOL",
                "name": "identifier"
              }
            ]
          }
        }
      ]
    },
    "_name": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "alias_qualified_name"
        },
        {
          "type": "SYMBOL",
          "name": "qualified_name"
        },
        {
          "type": "SYMBOL",
          "name": "_simple_name"
        }
      ]
    },
    "alias_qualified_name": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "alias",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "STRING",
          "value": "::"
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "_simple_name"
          }
        }
      ]
    },
    "_simple_name": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "SYMBOL",
          "name": "generic_name"
        }
      ]
    },
    "qualified_name": {
      "type": "PREC",
      "value": 18,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "qualifier",
            "content": {
              "type": "SYMBOL",
              "name": "_name"
            }
          },
          {
            "type": "STRING",
            "value": "."
          },
          {
            "type": "FIELD",
            "name": "name",
            "content": {
              "type": "SYMBOL",
              "name": "_simple_name"
            }
          }
        ]
      }
    },
    "generic_name": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "SYMBOL",
          "name": "type_argument_list"
        }
      ]
    },
    "type_argument_list": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "<"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "REPEAT",
              "content": {
                "type": "STRING",
                "value": ","
              }
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "type"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "type"
                      }
                    ]
                  }
                }
              ]
            }
          ]
        },
        {
          "type": "STRING",
          "value": ">"
        }
      ]
    },
    "type": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "implicit_type"
        },
        {
          "type": "SYMBOL",
          "name": "array_type"
        },
        {
          "type": "SYMBOL",
          "name": "_name"
        },
        {
          "type": "SYMBOL",
          "name": "nullable_type"
        },
        {
          "type": "SYMBOL",
          "name": "pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "function_pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "predefined_type"
        },
        {
          "type": "SYMBOL",
          "name": "tuple_type"
        },
        {
          "type": "SYMBOL",
          "name": "ref_type"
        },
        {
          "type": "SYMBOL",
          "name": "scoped_type"
        }
      ]
    },
    "implicit_type": {
      "type": "PREC_DYNAMIC",
      "value": 1,
      "content": {
        "type": "STRING",
        "value": "var"
      }
    },
    "array_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "_array_base_type"
          }
        },
        {
          "type": "FIELD",
          "name": "rank",
          "content": {
            "type": "SYMBOL",
            "name": "array_rank_specifier"
          }
        }
      ]
    },
    "_array_base_type": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "array_type"
        },
        {
          "type": "SYMBOL",
          "name": "_name"
        },
        {
          "type": "SYMBOL",
          "name": "nullable_type"
        },
        {
          "type": "SYMBOL",
          "name": "pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "function_pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "predefined_type"
        },
        {
          "type": "SYMBOL",
          "name": "tuple_type"
        }
      ]
    },
    "array_rank_specifier": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "expression"
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "CHOICE",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "expression"
                          },
                          {
                            "type": "BLANK"
                          }
                        ]
                      }
                    ]
                  }
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "]"
        }
      ]
    },
    "nullable_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "_nullable_base_type"
          }
        },
        {
          "type": "STRING",
          "value": "?"
        }
      ]
    },
    "_nullable_base_type": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "array_type"
        },
        {
          "type": "SYMBOL",
          "name": "_name"
        },
        {
          "type": "SYMBOL",
          "name": "predefined_type"
        },
        {
          "type": "SYMBOL",
          "name": "tuple_type"
        }
      ]
    },
    "pointer_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "_pointer_base_type"
          }
        },
        {
          "type": "STRING",
          "value": "*"
        }
      ]
    },
    "_pointer_base_type": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_name"
        },
        {
          "type": "SYMBOL",
          "name": "nullable_type"
        },
        {
          "type": "SYMBOL",
          "name": "pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "function_pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "predefined_type"
        },
        {
          "type": "SYMBOL",
          "name": "tuple_type"
        }
      ]
    },
    "function_pointer_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "delegate"
        },
        {
          "type": "STRING",
          "value": "*"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "calling_convention"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "<"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "SYMBOL",
                "name": "function_pointer_parameter"
              },
              {
                "type": "STRING",
                "value": ","
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "returns",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "STRING",
          "value": ">"
        }
      ]
    },
    "calling_convention": {
      "type": "CHOICE",
      "members": [
        {
          "type": "STRING",
          "value": "managed"
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": "unmanaged"
            },
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SEQ",
                  "members": [
                    {
                      "type": "STRING",
                      "value": "["
                    },
                    {
                      "type": "SEQ",
                      "members": [
                        {
                          "type": "CHOICE",
                          "members": [
                            {
                              "type": "STRING",
                              "value": "Cdecl"
                            },
                            {
                              "type": "STRING",
                              "value": "Stdcall"
                            },
                            {
                              "type": "STRING",
                              "value": "Thiscall"
                            },
                            {
                              "type": "STRING",
                              "value": "Fastcall"
                            },
                            {
                              "type": "SYMBOL",
                              "name": "identifier"
                            }
                          ]
                        },
                        {
                          "type": "REPEAT",
                          "content": {
                            "type": "SEQ",
                            "members": [
                              {
                                "type": "STRING",
                                "value": ","
                              },
                              {
                                "type": "CHOICE",
                                "members": [
                                  {
                                    "type": "STRING",
                                    "value": "Cdecl"
                                  },
                                  {
                                    "type": "STRING",
                                    "value": "Stdcall"
                                  },
                                  {
                                    "type": "STRING",
                                    "value": "Thiscall"
                                  },
                                  {
                                    "type": "STRING",
                                    "value": "Fastcall"
                                  },
                                  {
                                    "type": "SYMBOL",
                                    "name": "identifier"
                                  }
                                ]
                              }
                            ]
                          }
                        }
                      ]
                    },
                    {
                      "type": "STRING",
                      "value": "]"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          ]
        }
      ]
    },
    "function_pointer_parameter": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "STRING",
                  "value": "ref"
                },
                {
                  "type": "STRING",
                  "value": "out"
                },
                {
                  "type": "STRING",
                  "value": "in"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "_ref_base_type"
          }
        }
      ]
    },
    "predefined_type": {
      "type": "TOKEN",
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "STRING",
            "value": "bool"
          },
          {
            "type": "STRING",
            "value": "byte"
          },
          {
            "type": "STRING",
            "value": "char"
          },
          {
            "type": "STRING",
            "value": "decimal"
          },
          {
            "type": "STRING",
            "value": "double"
          },
          {
            "type": "STRING",
            "value": "float"
          },
          {
            "type": "STRING",
            "value": "int"
          },
          {
            "type": "STRING",
            "value": "long"
          },
          {
            "type": "STRING",
            "value": "object"
          },
          {
            "type": "STRING",
            "value": "sbyte"
          },
          {
            "type": "STRING",
            "value": "short"
          },
          {
            "type": "STRING",
            "value": "string"
          },
          {
            "type": "STRING",
            "value": "uint"
          },
          {
            "type": "STRING",
            "value": "ulong"
          },
          {
            "type": "STRING",
            "value": "ushort"
          },
          {
            "type": "STRING",
            "value": "nint"
          },
          {
            "type": "STRING",
            "value": "nuint"
          },
          {
            "type": "STRING",
            "value": "void"
          }
        ]
      }
    },
    "ref_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "ref"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "readonly"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        }
      ]
    },
    "_ref_base_type": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "implicit_type"
        },
        {
          "type": "SYMBOL",
          "name": "_name"
        },
        {
          "type": "SYMBOL",
          "name": "nullable_type"
        },
        {
          "type": "SYMBOL",
          "name": "array_type"
        },
        {
          "type": "SYMBOL",
          "name": "pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "function_pointer_type"
        },
        {
          "type": "SYMBOL",
          "name": "predefined_type"
        },
        {
          "type": "SYMBOL",
          "name": "tuple_type"
        }
      ]
    },
    "scoped_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "scoped"
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "_scoped_base_type"
          }
        }
      ]
    },
    "_scoped_base_type": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_name"
        },
        {
          "type": "SYMBOL",
          "name": "ref_type"
        }
      ]
    },
    "tuple_type": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "tuple_element"
            },
            {
              "type": "REPEAT1",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "tuple_element"
                  }
                ]
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
    "tuple_element": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "identifier"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        }
      ]
    },
    "statement": {
      "type": "PREC",
      "value": 1,
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "SYMBOL",
            "name": "block"
          },
          {
            "type": "SYMBOL",
            "name": "break_statement"
          },
          {
            "type": "SYMBOL",
            "name": "checked_statement"
          },
          {
            "type": "SYMBOL",
            "name": "continue_statement"
          },
          {
            "type": "SYMBOL",
            "name": "do_statement"
          },
          {
            "type": "SYMBOL",
            "name": "empty_statement"
          },
          {
            "type": "SYMBOL",
            "name": "expression_statement"
          },
          {
            "type": "SYMBOL",
            "name": "fixed_statement"
          },
          {
            "type": "SYMBOL",
            "name": "for_statement"
          },
          {
            "type": "SYMBOL",
            "name": "return_statement"
          },
          {
            "type": "SYMBOL",
            "name": "lock_statement"
          },
          {
            "type": "SYMBOL",
            "name": "yield_statement"
          },
          {
            "type": "SYMBOL",
            "name": "switch_statement"
          },
          {
            "type": "SYMBOL",
            "name": "throw_statement"
          },
          {
            "type": "SYMBOL",
            "name": "try_statement"
          },
          {
            "type": "SYMBOL",
            "name": "unsafe_statement"
          },
          {
            "type": "SYMBOL",
            "name": "using_statement"
          },
          {
            "type": "SYMBOL",
            "name": "foreach_statement"
          },
          {
            "type": "SYMBOL",
            "name": "goto_statement"
          },
          {
            "type": "SYMBOL",
            "name": "labeled_statement"
          },
          {
            "type": "SYMBOL",
            "name": "if_statement"
          },
          {
            "type": "SYMBOL",
            "name": "while_statement"
          },
          {
            "type": "SYMBOL",
            "name": "local_declaration_statement"
          },
          {
            "type": "SYMBOL",
            "name": "local_function_statement"
          },
          {
            "type": "ALIAS",
            "content": {
              "type": "SYMBOL",
              "name": "preproc_if_in_top_level"
            },
            "named": true,
            "value": "preproc_if"
          }
        ]
      }
    },
    "break_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "break"
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "checked_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "checked"
            },
            {
              "type": "STRING",
              "value": "unchecked"
            }
          ]
        },
        {
          "type": "SYMBOL",
          "name": "block"
        }
      ]
    },
    "continue_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "continue"
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "do_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "do"
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "statement"
          }
        },
        {
          "type": "STRING",
          "value": "while"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "FIELD",
          "name": "condition",
          "content": {
            "type": "SYMBOL",
            "name": "expression"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "empty_statement": {
      "type": "STRING",
      "value": ";"
    },
    "expression_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_expression_statement_expression"
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "fixed_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "fixed"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "variable_declaration"
        },
        {
          "type": "STRING",
          "value": ")"
        },
        {
          "type": "SYMBOL",
          "name": "statement"
        }
      ]
    },
    "for_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "for"
        },
        {
          "type": "SYMBOL",
          "name": "_for_statement_conditions"
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "statement"
          }
        }
      ]
    },
    "_for_statement_conditions": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "FIELD",
          "name": "initializer",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "SYMBOL",
                    "name": "variable_declaration"
                  },
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "expression"
                      },
                      {
                        "type": "REPEAT",
                        "content": {
                          "type": "SEQ",
                          "members": [
                            {
                              "type": "STRING",
                              "value": ","
                            },
                            {
                              "type": "SYMBOL",
                              "name": "expression"
                            }
                          ]
                        }
                      }
                    ]
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          }
        },
        {
          "type": "STRING",
          "value": ";"
        },
        {
          "type": "FIELD",
          "name": "condition",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "expression"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        },
        {
          "type": "STRING",
          "value": ";"
        },
        {
          "type": "FIELD",
          "name": "update",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SEQ",
                "members": [
                  {
                    "type": "SYMBOL",
                    "name": "expression"
                  },
                  {
                    "type": "REPEAT",
                    "content": {
                      "type": "SEQ",
                      "members": [
                        {
                          "type": "STRING",
                          "value": ","
                        },
                        {
                          "type": "SYMBOL",
                          "name": "expression"
                        }
                      ]
                    }
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "return_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "return"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "expression"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "lock_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "lock"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "STRING",
          "value": ")"
        },
        {
          "type": "SYMBOL",
          "name": "statement"
        }
      ]
    },
    "yield_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "yield"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "return"
                },
                {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              ]
            },
            {
              "type": "STRING",
              "value": "break"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "switch_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "switch"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "("
                },
                {
                  "type": "FIELD",
                  "name": "value",
                  "content": {
                    "type": "SYMBOL",
                    "name": "expression"
                  }
                },
                {
                  "type": "STRING",
                  "value": ")"
                }
              ]
            },
            {
              "type": "FIELD",
              "name": "value",
              "content": {
                "type": "SYMBOL",
                "name": "tuple_expression"
              }
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "switch_body"
          }
        }
      ]
    },
    "switch_body": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "switch_section"
          }
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "switch_section": {
      "type": "PREC_LEFT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": "case"
                  },
                  {
                    "type": "CHOICE",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "expression"
                      },
                      {
                        "type": "SEQ",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "pattern"
                          },
                          {
                            "type": "CHOICE",
                            "members": [
                              {
                                "type": "SYMBOL",
                                "name": "when_clause"
                              },
                              {
                                "type": "BLANK"
                              }
                            ]
                          }
                        ]
                      }
                    ]
                  }
                ]
              },
              {
                "type": "STRING",
                "value": "default"
              }
            ]
          },
          {
            "type": "STRING",
            "value": ":"
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "statement"
            }
          }
        ]
      }
    },
    "throw_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "throw"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "expression"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "try_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "try"
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "block"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "catch_clause"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "finally_clause"
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "catch_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "catch"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "catch_declaration"
              },
              {
                "type": "SYMBOL",
                "name": "catch_filter_clause"
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "block"
          }
        }
      ]
    },
    "catch_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "name",
              "content": {
                "type": "SYMBOL",
                "name": "identifier"
              }
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "catch_filter_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "when"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "finally_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "finally"
        },
        {
          "type": "SYMBOL",
          "name": "block"
        }
      ]
    },
    "unsafe_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "unsafe"
        },
        {
          "type": "SYMBOL",
          "name": "block"
        }
      ]
    },
    "using_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "await"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "using"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "using_variable_declaration"
              },
              "named": true,
              "value": "variable_declaration"
            },
            {
              "type": "SYMBOL",
              "name": "expression"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ")"
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "statement"
          }
        }
      ]
    },
    "foreach_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_foreach_statement_initializer"
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "statement"
          }
        }
      ]
    },
    "_foreach_statement_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "await"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "foreach"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "FIELD",
                  "name": "type",
                  "content": {
                    "type": "SYMBOL",
                    "name": "type"
                  }
                },
                {
                  "type": "FIELD",
                  "name": "left",
                  "content": {
                    "type": "CHOICE",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "identifier"
                      },
                      {
                        "type": "SYMBOL",
                        "name": "tuple_pattern"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "type": "FIELD",
              "name": "left",
              "content": {
                "type": "SYMBOL",
                "name": "expression"
              }
            }
          ]
        },
        {
          "type": "STRING",
          "value": "in"
        },
        {
          "type": "FIELD",
          "name": "right",
          "content": {
            "type": "SYMBOL",
            "name": "expression"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "goto_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "goto"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "STRING",
                  "value": "case"
                },
                {
                  "type": "STRING",
                  "value": "default"
                }
              ]
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
              "type": "SYMBOL",
              "name": "expression"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "labeled_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "STRING",
          "value": ":"
        },
        {
          "type": "SYMBOL",
          "name": "statement"
        }
      ]
    },
    "if_statement": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "if"
          },
          {
            "type": "STRING",
            "value": "("
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "STRING",
            "value": ")"
          },
          {
            "type": "FIELD",
            "name": "consequence",
            "content": {
              "type": "SYMBOL",
              "name": "statement"
            }
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": "else"
                  },
                  {
                    "type": "FIELD",
                    "name": "alternative",
                    "content": {
                      "type": "SYMBOL",
                      "name": "statement"
                    }
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "while_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "while"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "FIELD",
          "name": "condition",
          "content": {
            "type": "SYMBOL",
            "name": "expression"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        },
        {
          "type": "FIELD",
          "name": "body",
          "content": {
            "type": "SYMBOL",
            "name": "statement"
          }
        }
      ]
    },
    "local_declaration_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "await"
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
              "type": "STRING",
              "value": "using"
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
            "name": "modifier"
          }
        },
        {
          "type": "SYMBOL",
          "name": "variable_declaration"
        },
        {
          "type": "STRING",
          "value": ";"
        }
      ]
    },
    "local_function_statement": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_local_function_declaration"
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "type_parameter_constraints_clause"
          }
        },
        {
          "type": "SYMBOL",
          "name": "_function_body"
        }
      ]
    },
    "_local_function_declaration": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "_attribute_list"
          }
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "SYMBOL",
            "name": "modifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "FIELD",
          "name": "type_parameters",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "type_parameter_list"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "parameters",
          "content": {
            "type": "SYMBOL",
            "name": "parameter_list"
          }
        }
      ]
    },
    "pattern": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "constant_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "declaration_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "discard"
        },
        {
          "type": "SYMBOL",
          "name": "recursive_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "var_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "negated_pattern"
        },
        {
          "type": "PREC_DYNAMIC",
          "value": 1,
          "content": {
            "type": "ALIAS",
            "content": {
              "type": "SYMBOL",
              "name": "_parenthesized_pattern_with_designation"
            },
            "named": true,
            "value": "recursive_pattern"
          }
        },
        {
          "type": "SYMBOL",
          "name": "parenthesized_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "relational_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "or_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "and_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "list_pattern"
        },
        {
          "type": "SYMBOL",
          "name": "type_pattern"
        }
      ]
    },
    "_parenthesized_pattern_with_designation": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "pattern"
        },
        {
          "type": "STRING",
          "value": ")"
        },
        {
          "type": "SYMBOL",
          "name": "_variable_designation"
        }
      ]
    },
    "constant_pattern": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "binary_expression"
        },
        {
          "type": "SYMBOL",
          "name": "default_expression"
        },
        {
          "type": "SYMBOL",
          "name": "interpolated_string_expression"
        },
        {
          "type": "SYMBOL",
          "name": "parenthesized_expression"
        },
        {
          "type": "SYMBOL",
          "name": "postfix_unary_expression"
        },
        {
          "type": "SYMBOL",
          "name": "prefix_unary_expression"
        },
        {
          "type": "SYMBOL",
          "name": "sizeof_expression"
        },
        {
          "type": "SYMBOL",
          "name": "tuple_expression"
        },
        {
          "type": "SYMBOL",
          "name": "typeof_expression"
        },
        {
          "type": "SYMBOL",
          "name": "member_access_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "_name_invocation_pattern"
          },
          "named": true,
          "value": "invocation_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "_complex_invocation_expression"
          },
          "named": true,
          "value": "invocation_expression"
        },
        {
          "type": "SYMBOL",
          "name": "cast_expression"
        },
        {
          "type": "SYMBOL",
          "name": "_simple_name"
        },
        {
          "type": "SYMBOL",
          "name": "literal"
        }
      ]
    },
    "_name_invocation_pattern": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "function",
          "content": {
            "type": "SYMBOL",
            "name": "_name"
          }
        },
        {
          "type": "FIELD",
          "name": "arguments",
          "content": {
            "type": "SYMBOL",
            "name": "argument_list"
          }
        }
      ]
    },
    "_complex_invocation_expression": {
      "type": "PREC",
      "value": 18,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "function",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "member_access_expression"
                },
                {
                  "type": "SYMBOL",
                  "name": "element_access_expression"
                },
                {
                  "type": "SYMBOL",
                  "name": "invocation_expression"
                },
                {
                  "type": "SYMBOL",
                  "name": "parenthesized_expression"
                },
                {
                  "type": "SYMBOL",
                  "name": "conditional_access_expression"
                },
                {
                  "type": "SYMBOL",
                  "name": "cast_expression"
                }
              ]
            }
          },
          {
            "type": "FIELD",
            "name": "arguments",
            "content": {
              "type": "SYMBOL",
              "name": "argument_list"
            }
          }
        ]
      }
    },
    "discard": {
      "type": "STRING",
      "value": "_"
    },
    "parenthesized_pattern": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "pattern"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "var_pattern": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "var"
        },
        {
          "type": "SYMBOL",
          "name": "_variable_designation"
        }
      ]
    },
    "type_pattern": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "FIELD",
        "name": "type",
        "content": {
          "type": "SYMBOL",
          "name": "type"
        }
      }
    },
    "list_pattern": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "["
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SEQ",
                "members": [
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "CHOICE",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "pattern"
                          },
                          {
                            "type": "STRING",
                            "value": ".."
                          }
                        ]
                      },
                      {
                        "type": "REPEAT",
                        "content": {
                          "type": "SEQ",
                          "members": [
                            {
                              "type": "STRING",
                              "value": ","
                            },
                            {
                              "type": "CHOICE",
                              "members": [
                                {
                                  "type": "SYMBOL",
                                  "name": "pattern"
                                },
                                {
                                  "type": "STRING",
                                  "value": ".."
                                }
                              ]
                            }
                          ]
                        }
                      }
                    ]
                  },
                  {
                    "type": "CHOICE",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "BLANK"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "STRING",
            "value": "]"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "_variable_designation"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "recursive_pattern": {
      "type": "PREC_LEFT",
      "value": 0,
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "PREC_DYNAMIC",
            "value": 1,
            "content": {
              "type": "SEQ",
              "members": [
                {
                  "type": "FIELD",
                  "name": "type",
                  "content": {
                    "type": "SYMBOL",
                    "name": "_name"
                  }
                },
                {
                  "type": "SYMBOL",
                  "name": "positional_pattern_clause"
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "property_pattern_clause"
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                },
                {
                  "type": "SYMBOL",
                  "name": "_variable_designation"
                }
              ]
            }
          },
          {
            "type": "PREC_DYNAMIC",
            "value": -1,
            "content": {
              "type": "SEQ",
              "members": [
                {
                  "type": "FIELD",
                  "name": "type",
                  "content": {
                    "type": "SYMBOL",
                    "name": "_name"
                  }
                },
                {
                  "type": "SYMBOL",
                  "name": "positional_pattern_clause"
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "property_pattern_clause"
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                }
              ]
            }
          },
          {
            "type": "PREC_DYNAMIC",
            "value": 1,
            "content": {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "positional_pattern_clause"
                },
                {
                  "type": "SYMBOL",
                  "name": "_variable_designation"
                }
              ]
            }
          },
          {
            "type": "SYMBOL",
            "name": "positional_pattern_clause"
          },
          {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "type",
                "content": {
                  "type": "SYMBOL",
                  "name": "type"
                }
              },
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "positional_pattern_clause"
                      },
                      {
                        "type": "CHOICE",
                        "members": [
                          {
                            "type": "SYMBOL",
                            "name": "property_pattern_clause"
                          },
                          {
                            "type": "BLANK"
                          }
                        ]
                      }
                    ]
                  },
                  {
                    "type": "SYMBOL",
                    "name": "property_pattern_clause"
                  }
                ]
              },
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "SYMBOL",
                    "name": "_variable_designation"
                  },
                  {
                    "type": "BLANK"
                  }
                ]
              }
            ]
          },
          {
            "type": "SEQ",
            "members": [
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "positional_pattern_clause"
                      },
                      {
                        "type": "SYMBOL",
                        "name": "property_pattern_clause"
                      }
                    ]
                  },
                  {
                    "type": "SYMBOL",
                    "name": "property_pattern_clause"
                  }
                ]
              },
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "SYMBOL",
                    "name": "_variable_designation"
                  },
                  {
                    "type": "BLANK"
                  }
                ]
              }
            ]
          }
        ]
      }
    },
    "positional_pattern_clause": {
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
                "type": "CHOICE",
                "members": [
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "subpattern"
                      },
                      {
                        "type": "REPEAT",
                        "content": {
                          "type": "SEQ",
                          "members": [
                            {
                              "type": "STRING",
                              "value": ","
                            },
                            {
                              "type": "SYMBOL",
                              "name": "subpattern"
                            }
                          ]
                        }
                      }
                    ]
                  },
                  {
                    "type": "BLANK"
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "STRING",
            "value": ")"
          }
        ]
      }
    },
    "property_pattern_clause": {
      "type": "PREC",
      "value": 1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "{"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SEQ",
                "members": [
                  {
                    "type": "SYMBOL",
                    "name": "subpattern"
                  },
                  {
                    "type": "REPEAT",
                    "content": {
                      "type": "SEQ",
                      "members": [
                        {
                          "type": "STRING",
                          "value": ","
                        },
                        {
                          "type": "SYMBOL",
                          "name": "subpattern"
                        }
                      ]
                    }
                  }
                ]
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
                "type": "STRING",
                "value": ","
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "STRING",
            "value": "}"
          }
        ]
      }
    },
    "subpattern": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "expression"
                      },
                      {
                        "type": "STRING",
                        "value": ":"
                      }
                    ]
                  },
                  {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "SYMBOL",
                        "name": "identifier"
                      },
                      {
                        "type": "STRING",
                        "value": ":"
                      }
                    ]
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "SYMBOL",
            "name": "pattern"
          }
        ]
      }
    },
    "relational_pattern": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": "<"
            },
            {
              "type": "SYMBOL",
              "name": "expression"
            }
          ]
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": "<="
            },
            {
              "type": "SYMBOL",
              "name": "expression"
            }
          ]
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": ">"
            },
            {
              "type": "SYMBOL",
              "name": "expression"
            }
          ]
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": ">="
            },
            {
              "type": "SYMBOL",
              "name": "expression"
            }
          ]
        }
      ]
    },
    "negated_pattern": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "not"
        },
        {
          "type": "SYMBOL",
          "name": "pattern"
        }
      ]
    },
    "and_pattern": {
      "type": "PREC_LEFT",
      "value": 8,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "left",
            "content": {
              "type": "SYMBOL",
              "name": "pattern"
            }
          },
          {
            "type": "FIELD",
            "name": "operator",
            "content": {
              "type": "STRING",
              "value": "and"
            }
          },
          {
            "type": "FIELD",
            "name": "right",
            "content": {
              "type": "SYMBOL",
              "name": "pattern"
            }
          }
        ]
      }
    },
    "or_pattern": {
      "type": "PREC_LEFT",
      "value": 6,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "left",
            "content": {
              "type": "SYMBOL",
              "name": "pattern"
            }
          },
          {
            "type": "FIELD",
            "name": "operator",
            "content": {
              "type": "STRING",
              "value": "or"
            }
          },
          {
            "type": "FIELD",
            "name": "right",
            "content": {
              "type": "SYMBOL",
              "name": "pattern"
            }
          }
        ]
      }
    },
    "declaration_pattern": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "SYMBOL",
          "name": "_variable_designation"
        }
      ]
    },
    "_variable_designation": {
      "type": "PREC",
      "value": 1,
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "SYMBOL",
            "name": "discard"
          },
          {
            "type": "SYMBOL",
            "name": "parenthesized_variable_designation"
          },
          {
            "type": "FIELD",
            "name": "name",
            "content": {
              "type": "SYMBOL",
              "name": "identifier"
            }
          }
        ]
      }
    },
    "parenthesized_variable_designation": {
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
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "_variable_designation"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "_variable_designation"
                      }
                    ]
                  }
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "non_lvalue_expression"
        },
        {
          "type": "SYMBOL",
          "name": "lvalue_expression"
        }
      ]
    },
    "non_lvalue_expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "STRING",
          "value": "base"
        },
        {
          "type": "SYMBOL",
          "name": "binary_expression"
        },
        {
          "type": "SYMBOL",
          "name": "interpolated_string_expression"
        },
        {
          "type": "SYMBOL",
          "name": "conditional_expression"
        },
        {
          "type": "SYMBOL",
          "name": "conditional_access_expression"
        },
        {
          "type": "SYMBOL",
          "name": "literal"
        },
        {
          "type": "SYMBOL",
          "name": "_expression_statement_expression"
        },
        {
          "type": "SYMBOL",
          "name": "is_expression"
        },
        {
          "type": "SYMBOL",
          "name": "is_pattern_expression"
        },
        {
          "type": "SYMBOL",
          "name": "as_expression"
        },
        {
          "type": "SYMBOL",
          "name": "cast_expression"
        },
        {
          "type": "SYMBOL",
          "name": "checked_expression"
        },
        {
          "type": "SYMBOL",
          "name": "switch_expression"
        },
        {
          "type": "SYMBOL",
          "name": "throw_expression"
        },
        {
          "type": "SYMBOL",
          "name": "default_expression"
        },
        {
          "type": "SYMBOL",
          "name": "lambda_expression"
        },
        {
          "type": "SYMBOL",
          "name": "with_expression"
        },
        {
          "type": "SYMBOL",
          "name": "sizeof_expression"
        },
        {
          "type": "SYMBOL",
          "name": "typeof_expression"
        },
        {
          "type": "SYMBOL",
          "name": "makeref_expression"
        },
        {
          "type": "SYMBOL",
          "name": "ref_expression"
        },
        {
          "type": "SYMBOL",
          "name": "reftype_expression"
        },
        {
          "type": "SYMBOL",
          "name": "refvalue_expression"
        },
        {
          "type": "SYMBOL",
          "name": "stackalloc_expression"
        },
        {
          "type": "SYMBOL",
          "name": "range_expression"
        },
        {
          "type": "SYMBOL",
          "name": "array_creation_expression"
        },
        {
          "type": "SYMBOL",
          "name": "anonymous_method_expression"
        },
        {
          "type": "SYMBOL",
          "name": "anonymous_object_creation_expression"
        },
        {
          "type": "SYMBOL",
          "name": "implicit_array_creation_expression"
        },
        {
          "type": "SYMBOL",
          "name": "implicit_object_creation_expression"
        },
        {
          "type": "SYMBOL",
          "name": "implicit_stackalloc_expression"
        },
        {
          "type": "SYMBOL",
          "name": "initializer_expression"
        },
        {
          "type": "SYMBOL",
          "name": "query_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "preproc_if_in_expression"
          },
          "named": true,
          "value": "preproc_if"
        }
      ]
    },
    "lvalue_expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "STRING",
          "value": "this"
        },
        {
          "type": "SYMBOL",
          "name": "member_access_expression"
        },
        {
          "type": "SYMBOL",
          "name": "tuple_expression"
        },
        {
          "type": "SYMBOL",
          "name": "_simple_name"
        },
        {
          "type": "SYMBOL",
          "name": "element_access_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "bracketed_argument_list"
          },
          "named": true,
          "value": "element_binding_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "_pointer_indirection_expression"
          },
          "named": true,
          "value": "prefix_unary_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "_parenthesized_lvalue_expression"
          },
          "named": true,
          "value": "parenthesized_expression"
        }
      ]
    },
    "_expression_statement_expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "assignment_expression"
        },
        {
          "type": "SYMBOL",
          "name": "invocation_expression"
        },
        {
          "type": "SYMBOL",
          "name": "postfix_unary_expression"
        },
        {
          "type": "SYMBOL",
          "name": "prefix_unary_expression"
        },
        {
          "type": "SYMBOL",
          "name": "await_expression"
        },
        {
          "type": "SYMBOL",
          "name": "object_creation_expression"
        },
        {
          "type": "SYMBOL",
          "name": "parenthesized_expression"
        }
      ]
    },
    "assignment_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "FIELD",
          "name": "left",
          "content": {
            "type": "SYMBOL",
            "name": "lvalue_expression"
          }
        },
        {
          "type": "FIELD",
          "name": "operator",
          "content": {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "="
              },
              {
                "type": "STRING",
                "value": "+="
              },
              {
                "type": "STRING",
                "value": "-="
              },
              {
                "type": "STRING",
                "value": "*="
              },
              {
                "type": "STRING",
                "value": "/="
              },
              {
                "type": "STRING",
                "value": "%="
              },
              {
                "type": "STRING",
                "value": "&="
              },
              {
                "type": "STRING",
                "value": "^="
              },
              {
                "type": "STRING",
                "value": "|="
              },
              {
                "type": "STRING",
                "value": "<<="
              },
              {
                "type": "STRING",
                "value": ">>="
              },
              {
                "type": "STRING",
                "value": ">>>="
              },
              {
                "type": "STRING",
                "value": "??="
              }
            ]
          }
        },
        {
          "type": "FIELD",
          "name": "right",
          "content": {
            "type": "SYMBOL",
            "name": "expression"
          }
        }
      ]
    },
    "binary_expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "PREC_LEFT",
          "value": 5,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "&&"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 4,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "||"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 11,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": ">>"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 11,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": ">>>"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 11,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "<<"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 8,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "&"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 7,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "^"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 6,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "|"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 12,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "+"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 12,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "-"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 13,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "*"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 13,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "/"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 13,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "%"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 10,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "<"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 10,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "<="
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 9,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "=="
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 9,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "!="
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 10,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": ">="
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 10,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": ">"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_RIGHT",
          "value": 3,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "??"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              }
            ]
          }
        }
      ]
    },
    "postfix_unary_expression": {
      "type": "PREC",
      "value": 18,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "SYMBOL",
            "name": "expression"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "++"
              },
              {
                "type": "STRING",
                "value": "--"
              },
              {
                "type": "STRING",
                "value": "!"
              }
            ]
          }
        ]
      }
    },
    "prefix_unary_expression": {
      "type": "PREC",
      "value": 17,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "++"
              },
              {
                "type": "STRING",
                "value": "--"
              },
              {
                "type": "STRING",
                "value": "+"
              },
              {
                "type": "STRING",
                "value": "-"
              },
              {
                "type": "STRING",
                "value": "!"
              },
              {
                "type": "STRING",
                "value": "~"
              },
              {
                "type": "STRING",
                "value": "&"
              },
              {
                "type": "STRING",
                "value": "^"
              }
            ]
          },
          {
            "type": "SYMBOL",
            "name": "expression"
          }
        ]
      }
    },
    "_pointer_indirection_expression": {
      "type": "PREC_RIGHT",
      "value": 17,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "*"
          },
          {
            "type": "SYMBOL",
            "name": "lvalue_expression"
          }
        ]
      }
    },
    "query_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "from_clause"
        },
        {
          "type": "SYMBOL",
          "name": "_query_body"
        }
      ]
    },
    "from_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "from"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "type",
              "content": {
                "type": "SYMBOL",
                "name": "type"
              }
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "identifier"
          }
        },
        {
          "type": "STRING",
          "value": "in"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "_query_body": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "SEQ",
            "members": [
              {
                "type": "REPEAT",
                "content": {
                  "type": "SYMBOL",
                  "name": "_query_clause"
                }
              },
              {
                "type": "SYMBOL",
                "name": "_select_or_group_clause"
              }
            ]
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SEQ",
              "members": [
                {
                  "type": "SEQ",
                  "members": [
                    {
                      "type": "STRING",
                      "value": "into"
                    },
                    {
                      "type": "SYMBOL",
                      "name": "identifier"
                    }
                  ]
                },
                {
                  "type": "SEQ",
                  "members": [
                    {
                      "type": "REPEAT",
                      "content": {
                        "type": "SYMBOL",
                        "name": "_query_clause"
                      }
                    },
                    {
                      "type": "SYMBOL",
                      "name": "_select_or_group_clause"
                    }
                  ]
                }
              ]
            }
          }
        ]
      }
    },
    "_query_clause": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "from_clause"
        },
        {
          "type": "SYMBOL",
          "name": "join_clause"
        },
        {
          "type": "SYMBOL",
          "name": "let_clause"
        },
        {
          "type": "SYMBOL",
          "name": "order_by_clause"
        },
        {
          "type": "SYMBOL",
          "name": "where_clause"
        }
      ]
    },
    "join_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "join"
        },
        {
          "type": "SYMBOL",
          "name": "_join_header"
        },
        {
          "type": "SYMBOL",
          "name": "_join_body"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "join_into_clause"
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "_join_header": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "type",
              "content": {
                "type": "SYMBOL",
                "name": "type"
              }
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "STRING",
          "value": "in"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "_join_body": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "on"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "STRING",
          "value": "equals"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "join_into_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "into"
        },
        {
          "type": "SYMBOL",
          "name": "identifier"
        }
      ]
    },
    "let_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "let"
        },
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "STRING",
          "value": "="
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "order_by_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "orderby"
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "_ordering"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "_ordering"
                  }
                ]
              }
            }
          ]
        }
      ]
    },
    "_ordering": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "STRING",
                  "value": "ascending"
                },
                {
                  "type": "STRING",
                  "value": "descending"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "where_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "where"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "_select_or_group_clause": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "group_clause"
        },
        {
          "type": "SYMBOL",
          "name": "select_clause"
        }
      ]
    },
    "group_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "group"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "STRING",
          "value": "by"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "select_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "select"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "conditional_expression": {
      "type": "PREC_RIGHT",
      "value": 2,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "STRING",
            "value": "?"
          },
          {
            "type": "FIELD",
            "name": "consequence",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "STRING",
            "value": ":"
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          }
        ]
      }
    },
    "conditional_access_expression": {
      "type": "PREC_RIGHT",
      "value": 2,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "STRING",
            "value": "?"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "member_binding_expression"
              },
              {
                "type": "ALIAS",
                "content": {
                  "type": "SYMBOL",
                  "name": "bracketed_argument_list"
                },
                "named": true,
                "value": "element_binding_expression"
              }
            ]
          }
        ]
      }
    },
    "as_expression": {
      "type": "PREC",
      "value": 10,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "left",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "FIELD",
            "name": "operator",
            "content": {
              "type": "STRING",
              "value": "as"
            }
          },
          {
            "type": "FIELD",
            "name": "right",
            "content": {
              "type": "SYMBOL",
              "name": "type"
            }
          }
        ]
      }
    },
    "is_expression": {
      "type": "PREC",
      "value": 10,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "left",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "FIELD",
            "name": "operator",
            "content": {
              "type": "STRING",
              "value": "is"
            }
          },
          {
            "type": "FIELD",
            "name": "right",
            "content": {
              "type": "SYMBOL",
              "name": "type"
            }
          }
        ]
      }
    },
    "is_pattern_expression": {
      "type": "PREC",
      "value": 10,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "expression",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "STRING",
            "value": "is"
          },
          {
            "type": "FIELD",
            "name": "pattern",
            "content": {
              "type": "SYMBOL",
              "name": "pattern"
            }
          }
        ]
      }
    },
    "cast_expression": {
      "type": "PREC",
      "value": 17,
      "content": {
        "type": "PREC_DYNAMIC",
        "value": 1,
        "content": {
          "type": "SEQ",
          "members": [
            {
              "type": "STRING",
              "value": "("
            },
            {
              "type": "FIELD",
              "name": "type",
              "content": {
                "type": "SYMBOL",
                "name": "type"
              }
            },
            {
              "type": "STRING",
              "value": ")"
            },
            {
              "type": "FIELD",
              "name": "value",
              "content": {
                "type": "SYMBOL",
                "name": "expression"
              }
            }
          ]
        }
      }
    },
    "checked_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "checked"
            },
            {
              "type": "STRING",
              "value": "unchecked"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "invocation_expression": {
      "type": "PREC",
      "value": 18,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "function",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "FIELD",
            "name": "arguments",
            "content": {
              "type": "SYMBOL",
              "name": "argument_list"
            }
          }
        ]
      }
    },
    "switch_expression": {
      "type": "PREC",
      "value": 15,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "SYMBOL",
            "name": "expression"
          },
          {
            "type": "STRING",
            "value": "switch"
          },
          {
            "type": "SYMBOL",
            "name": "_switch_expression_body"
          }
        ]
      }
    },
    "_switch_expression_body": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "switch_expression_arm"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "switch_expression_arm"
                      }
                    ]
                  }
                }
              ]
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
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "switch_expression_arm": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "pattern"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "when_clause"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "=>"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "when_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "when"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "await_expression": {
      "type": "PREC_RIGHT",
      "value": 17,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "await"
          },
          {
            "type": "SYMBOL",
            "name": "expression"
          }
        ]
      }
    },
    "throw_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "throw"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "element_access_expression": {
      "type": "PREC",
      "value": 18,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "expression",
            "content": {
              "type": "SYMBOL",
              "name": "expression"
            }
          },
          {
            "type": "FIELD",
            "name": "subscript",
            "content": {
              "type": "SYMBOL",
              "name": "bracketed_argument_list"
            }
          }
        ]
      }
    },
    "interpolated_string_expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SEQ",
          "members": [
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_regular_start"
              },
              "named": true,
              "value": "interpolation_start"
            },
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_start_quote"
              },
              "named": false,
              "value": "\""
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SYMBOL",
                "name": "_interpolated_string_content"
              }
            },
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_end_quote"
              },
              "named": false,
              "value": "\""
            }
          ]
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_verbatim_start"
              },
              "named": true,
              "value": "interpolation_start"
            },
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_start_quote"
              },
              "named": false,
              "value": "\""
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SYMBOL",
                "name": "_interpolated_verbatim_string_content"
              }
            },
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_end_quote"
              },
              "named": false,
              "value": "\""
            }
          ]
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_raw_start"
              },
              "named": true,
              "value": "interpolation_start"
            },
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_start_quote"
              },
              "named": true,
              "value": "interpolation_quote"
            },
            {
              "type": "REPEAT",
              "content": {
                "type": "SYMBOL",
                "name": "_interpolated_raw_string_content"
              }
            },
            {
              "type": "ALIAS",
              "content": {
                "type": "SYMBOL",
                "name": "interpolation_end_quote"
              },
              "named": true,
              "value": "interpolation_quote"
            }
          ]
        }
      ]
    },
    "_interpolated_string_content": {
      "type": "CHOICE",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "interpolation_string_content"
          },
          "named": true,
          "value": "string_content"
        },
        {
          "type": "SYMBOL",
          "name": "escape_sequence"
        },
        {
          "type": "SYMBOL",
          "name": "interpolation"
        }
      ]
    },
    "_interpolated_verbatim_string_content": {
      "type": "CHOICE",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "interpolation_string_content"
          },
          "named": true,
          "value": "string_content"
        },
        {
          "type": "SYMBOL",
          "name": "interpolation"
        }
      ]
    },
    "_interpolated_raw_string_content": {
      "type": "CHOICE",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "interpolation_string_content"
          },
          "named": true,
          "value": "string_content"
        },
        {
          "type": "SYMBOL",
          "name": "interpolation"
        }
      ]
    },
    "interpolation": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "interpolation_open_brace"
          },
          "named": true,
          "value": "interpolation_brace"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "interpolation_alignment_clause"
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
              "type": "SYMBOL",
              "name": "interpolation_format_clause"
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "interpolation_close_brace"
          },
          "named": true,
          "value": "interpolation_brace"
        }
      ]
    },
    "interpolation_alignment_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": ","
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "interpolation_format_clause": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": ":"
        },
        {
          "type": "PATTERN",
          "value": "[^}\"]+"
        }
      ]
    },
    "member_access_expression": {
      "type": "PREC",
      "value": 18,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "expression",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "expression"
                },
                {
                  "type": "SYMBOL",
                  "name": "predefined_type"
                },
                {
                  "type": "SYMBOL",
                  "name": "_name"
                }
              ]
            }
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "."
              },
              {
                "type": "STRING",
                "value": "->"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "name",
            "content": {
              "type": "SYMBOL",
              "name": "_simple_name"
            }
          }
        ]
      }
    },
    "member_binding_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "."
        },
        {
          "type": "FIELD",
          "name": "name",
          "content": {
            "type": "SYMBOL",
            "name": "_simple_name"
          }
        }
      ]
    },
    "object_creation_expression": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "new"
          },
          {
            "type": "FIELD",
            "name": "type",
            "content": {
              "type": "SYMBOL",
              "name": "type"
            }
          },
          {
            "type": "FIELD",
            "name": "arguments",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "argument_list"
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          },
          {
            "type": "FIELD",
            "name": "initializer",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "initializer_expression"
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          }
        ]
      }
    },
    "_object_creation_type": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_name"
        },
        {
          "type": "SYMBOL",
          "name": "nullable_type"
        },
        {
          "type": "SYMBOL",
          "name": "predefined_type"
        }
      ]
    },
    "parenthesized_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "non_lvalue_expression"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "_parenthesized_lvalue_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "lvalue_expression"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "lambda_expression": {
      "type": "PREC",
      "value": -1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "SYMBOL",
            "name": "_lambda_expression_init"
          },
          {
            "type": "STRING",
            "value": "=>"
          },
          {
            "type": "FIELD",
            "name": "body",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "block"
                },
                {
                  "type": "SYMBOL",
                  "name": "expression"
                }
              ]
            }
          }
        ]
      }
    },
    "_lambda_expression_init": {
      "type": "PREC",
      "value": -1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "_attribute_list"
            }
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "PREC",
              "value": -1,
              "content": {
                "type": "ALIAS",
                "content": {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "STRING",
                      "value": "static"
                    },
                    {
                      "type": "STRING",
                      "value": "async"
                    }
                  ]
                },
                "named": true,
                "value": "modifier"
              }
            }
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "FIELD",
                "name": "type",
                "content": {
                  "type": "SYMBOL",
                  "name": "type"
                }
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "parameters",
            "content": {
              "type": "SYMBOL",
              "name": "_lambda_parameters"
            }
          }
        ]
      }
    },
    "_lambda_parameters": {
      "type": "PREC",
      "value": -1,
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "SYMBOL",
            "name": "parameter_list"
          },
          {
            "type": "ALIAS",
            "content": {
              "type": "SYMBOL",
              "name": "identifier"
            },
            "named": true,
            "value": "implicit_parameter"
          }
        ]
      }
    },
    "array_creation_expression": {
      "type": "PREC_DYNAMIC",
      "value": 17,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "new"
          },
          {
            "type": "FIELD",
            "name": "type",
            "content": {
              "type": "SYMBOL",
              "name": "array_type"
            }
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "initializer_expression"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "anonymous_method_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "REPEAT",
          "content": {
            "type": "PREC",
            "value": -1,
            "content": {
              "type": "ALIAS",
              "content": {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "STRING",
                    "value": "static"
                  },
                  {
                    "type": "STRING",
                    "value": "async"
                  }
                ]
              },
              "named": true,
              "value": "modifier"
            }
          }
        },
        {
          "type": "STRING",
          "value": "delegate"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "parameters",
              "content": {
                "type": "SYMBOL",
                "name": "parameter_list"
              }
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "SYMBOL",
          "name": "block"
        }
      ]
    },
    "anonymous_object_creation_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "new"
        },
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "_anonymous_object_member_declarator"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "_anonymous_object_member_declarator"
                      }
                    ]
                  }
                }
              ]
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
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "_anonymous_object_member_declarator": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "identifier"
            },
            {
              "type": "STRING",
              "value": "="
            },
            {
              "type": "SYMBOL",
              "name": "expression"
            }
          ]
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "implicit_array_creation_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "new"
        },
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "REPEAT",
          "content": {
            "type": "STRING",
            "value": ","
          }
        },
        {
          "type": "STRING",
          "value": "]"
        },
        {
          "type": "SYMBOL",
          "name": "initializer_expression"
        }
      ]
    },
    "implicit_object_creation_expression": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "new"
          },
          {
            "type": "SYMBOL",
            "name": "argument_list"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "initializer_expression"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "implicit_stackalloc_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "stackalloc"
        },
        {
          "type": "STRING",
          "value": "["
        },
        {
          "type": "STRING",
          "value": "]"
        },
        {
          "type": "SYMBOL",
          "name": "initializer_expression"
        }
      ]
    },
    "initializer_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "expression"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "expression"
                      }
                    ]
                  }
                }
              ]
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
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "declaration_expression": {
      "type": "PREC_DYNAMIC",
      "value": 1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "type",
            "content": {
              "type": "SYMBOL",
              "name": "type"
            }
          },
          {
            "type": "FIELD",
            "name": "name",
            "content": {
              "type": "SYMBOL",
              "name": "identifier"
            }
          }
        ]
      }
    },
    "default_expression": {
      "type": "PREC_RIGHT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "default"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": "("
                  },
                  {
                    "type": "FIELD",
                    "name": "type",
                    "content": {
                      "type": "SYMBOL",
                      "name": "type"
                    }
                  },
                  {
                    "type": "STRING",
                    "value": ")"
                  }
                ]
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "with_expression": {
      "type": "PREC_LEFT",
      "value": 14,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "SYMBOL",
            "name": "expression"
          },
          {
            "type": "STRING",
            "value": "with"
          },
          {
            "type": "SYMBOL",
            "name": "_with_body"
          }
        ]
      }
    },
    "_with_body": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "{"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "with_initializer"
                },
                {
                  "type": "REPEAT",
                  "content": {
                    "type": "SEQ",
                    "members": [
                      {
                        "type": "STRING",
                        "value": ","
                      },
                      {
                        "type": "SYMBOL",
                        "name": "with_initializer"
                      }
                    ]
                  }
                }
              ]
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
              "type": "STRING",
              "value": ","
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "}"
        }
      ]
    },
    "with_initializer": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "STRING",
          "value": "="
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "sizeof_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "sizeof"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "typeof_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "typeof"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "makeref_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "__makeref"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "ref_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "ref"
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        }
      ]
    },
    "reftype_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "__reftype"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "expression"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "refvalue_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "__refvalue"
        },
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "FIELD",
          "name": "value",
          "content": {
            "type": "SYMBOL",
            "name": "expression"
          }
        },
        {
          "type": "STRING",
          "value": ","
        },
        {
          "type": "FIELD",
          "name": "type",
          "content": {
            "type": "SYMBOL",
            "name": "type"
          }
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "stackalloc_expression": {
      "type": "PREC_LEFT",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "stackalloc"
          },
          {
            "type": "FIELD",
            "name": "type",
            "content": {
              "type": "SYMBOL",
              "name": "array_type"
            }
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "initializer_expression"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "range_expression": {
      "type": "PREC_RIGHT",
      "value": 16,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "expression"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "STRING",
            "value": ".."
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "expression"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "tuple_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SEQ",
          "members": [
            {
              "type": "SYMBOL",
              "name": "argument"
            },
            {
              "type": "REPEAT1",
              "content": {
                "type": "SEQ",
                "members": [
                  {
                    "type": "STRING",
                    "value": ","
                  },
                  {
                    "type": "SYMBOL",
                    "name": "argument"
                  }
                ]
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
    "literal": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "null_literal"
        },
        {
          "type": "SYMBOL",
          "name": "character_literal"
        },
        {
          "type": "SYMBOL",
          "name": "integer_literal"
        },
        {
          "type": "SYMBOL",
          "name": "real_literal"
        },
        {
          "type": "SYMBOL",
          "name": "boolean_literal"
        },
        {
          "type": "SYMBOL",
          "name": "string_literal"
        },
        {
          "type": "SYMBOL",
          "name": "verbatim_string_literal"
        },
        {
          "type": "SYMBOL",
          "name": "raw_string_literal"
        }
      ]
    },
    "null_literal": {
      "type": "STRING",
      "value": "null"
    },
    "character_literal": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "'"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "character_literal_content"
            },
            {
              "type": "SYMBOL",
              "name": "escape_sequence"
            }
          ]
        },
        {
          "type": "STRING",
          "value": "'"
        }
      ]
    },
    "character_literal_content": {
      "type": "IMMEDIATE_TOKEN",
      "content": {
        "type": "PATTERN",
        "value": "[^'\\\\]"
      }
    },
    "integer_literal": {
      "type": "TOKEN",
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "PATTERN",
                "value": "([0-9][0-9_]*[0-9]|[0-9])"
              },
              {
                "type": "PATTERN",
                "value": "0[xX][0-9a-fA-F_]*[0-9a-fA-F]+"
              },
              {
                "type": "PATTERN",
                "value": "0[bB][01_]*[01]+"
              }
            ]
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "PATTERN",
                "value": "([uU][lL]?|[lL][uU]?)"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "real_literal": {
      "type": "TOKEN",
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "SEQ",
            "members": [
              {
                "type": "PATTERN",
                "value": "([0-9][0-9_]*[0-9]|[0-9])"
              },
              {
                "type": "STRING",
                "value": "."
              },
              {
                "type": "PATTERN",
                "value": "([0-9][0-9_]*[0-9]|[0-9])"
              },
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "PATTERN",
                    "value": "[eE][+-]?[0-9][0-9_]*"
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
                    "type": "PATTERN",
                    "value": "[fFdDmM]"
                  },
                  {
                    "type": "BLANK"
                  }
                ]
              }
            ]
          },
          {
            "type": "SEQ",
            "members": [
              {
                "type": "STRING",
                "value": "."
              },
              {
                "type": "PATTERN",
                "value": "([0-9][0-9_]*[0-9]|[0-9])"
              },
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "PATTERN",
                    "value": "[eE][+-]?[0-9][0-9_]*"
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
                    "type": "PATTERN",
                    "value": "[fFdDmM]"
                  },
                  {
                    "type": "BLANK"
                  }
                ]
              }
            ]
          },
          {
            "type": "SEQ",
            "members": [
              {
                "type": "PATTERN",
                "value": "([0-9][0-9_]*[0-9]|[0-9])"
              },
              {
                "type": "PATTERN",
                "value": "[eE][+-]?[0-9][0-9_]*"
              },
              {
                "type": "CHOICE",
                "members": [
                  {
                    "type": "PATTERN",
                    "value": "[fFdDmM]"
                  },
                  {
                    "type": "BLANK"
                  }
                ]
              }
            ]
          },
          {
            "type": "SEQ",
            "members": [
              {
                "type": "PATTERN",
                "value": "([0-9][0-9_]*[0-9]|[0-9])"
              },
              {
                "type": "PATTERN",
                "value": "[fFdDmM]"
              }
            ]
          }
        ]
      }
    },
    "string_literal": {
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
                "type": "SYMBOL",
                "name": "string_literal_content"
              },
              {
                "type": "SYMBOL",
                "name": "escape_sequence"
              }
            ]
          }
        },
        {
          "type": "STRING",
          "value": "\""
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SYMBOL",
              "name": "string_literal_encoding"
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "string_literal_content": {
      "type": "IMMEDIATE_TOKEN",
      "content": {
        "type": "PREC",
        "value": 1,
        "content": {
          "type": "PATTERN",
          "value": "[^\"\\\\\\n]+"
        }
      }
    },
    "escape_sequence": {
      "type": "TOKEN",
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "PATTERN",
            "value": "\\\\x[0-9a-fA-F]{1,4}"
          },
          {
            "type": "PATTERN",
            "value": "\\\\u[0-9a-fA-F]{4}"
          },
          {
            "type": "PATTERN",
            "value": "\\\\U[0-9a-fA-F]{8}"
          },
          {
            "type": "PATTERN",
            "value": "\\\\[abefnrtv'\\\"\\\\\\?0]"
          }
        ]
      }
    },
    "string_literal_encoding": {
      "type": "IMMEDIATE_TOKEN",
      "content": {
        "type": "PATTERN",
        "value": "(u|U)8"
      }
    },
    "verbatim_string_literal": {
      "type": "TOKEN",
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "@\""
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "PATTERN",
                  "value": "[^\"]"
                },
                {
                  "type": "STRING",
                  "value": "\"\""
                }
              ]
            }
          },
          {
            "type": "STRING",
            "value": "\""
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "PATTERN",
                "value": "(u|U)8"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "raw_string_literal": {
      "type": "SEQ",
      "members": [
        {
          "type": "SYMBOL",
          "name": "raw_string_start"
        },
        {
          "type": "SYMBOL",
          "name": "raw_string_content"
        },
        {
          "type": "SYMBOL",
          "name": "raw_string_end"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "PATTERN",
              "value": "(u|U)8"
            },
            {
              "type": "BLANK"
            }
          ]
        }
      ]
    },
    "boolean_literal": {
      "type": "CHOICE",
      "members": [
        {
          "type": "STRING",
          "value": "true"
        },
        {
          "type": "STRING",
          "value": "false"
        }
      ]
    },
    "_identifier_token": {
      "type": "TOKEN",
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "STRING",
                "value": "@"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "PATTERN",
            "value": "(\\p{XID_Start}|_|\\\\u[0-9A-Fa-f]{4}|\\\\U[0-9A-Fa-f]{8})(\\p{XID_Continue}|\\\\u[0-9A-Fa-f]{4}|\\\\U[0-9A-Fa-f]{8})*"
          }
        ]
      }
    },
    "identifier": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "_identifier_token"
        },
        {
          "type": "SYMBOL",
          "name": "_reserved_identifier"
        }
      ]
    },
    "_reserved_identifier": {
      "type": "CHOICE",
      "members": [
        {
          "type": "STRING",
          "value": "alias"
        },
        {
          "type": "STRING",
          "value": "ascending"
        },
        {
          "type": "STRING",
          "value": "by"
        },
        {
          "type": "STRING",
          "value": "descending"
        },
        {
          "type": "STRING",
          "value": "equals"
        },
        {
          "type": "STRING",
          "value": "file"
        },
        {
          "type": "STRING",
          "value": "from"
        },
        {
          "type": "STRING",
          "value": "global"
        },
        {
          "type": "STRING",
          "value": "group"
        },
        {
          "type": "STRING",
          "value": "into"
        },
        {
          "type": "STRING",
          "value": "join"
        },
        {
          "type": "STRING",
          "value": "let"
        },
        {
          "type": "STRING",
          "value": "notnull"
        },
        {
          "type": "STRING",
          "value": "on"
        },
        {
          "type": "STRING",
          "value": "orderby"
        },
        {
          "type": "STRING",
          "value": "scoped"
        },
        {
          "type": "STRING",
          "value": "select"
        },
        {
          "type": "STRING",
          "value": "unmanaged"
        },
        {
          "type": "STRING",
          "value": "var"
        },
        {
          "type": "STRING",
          "value": "when"
        },
        {
          "type": "STRING",
          "value": "where"
        },
        {
          "type": "STRING",
          "value": "yield"
        }
      ]
    },
    "preproc_if": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*if"
            },
            "named": false,
            "value": "#if"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "declaration"
            }
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "preproc_else"
                    },
                    {
                      "type": "SYMBOL",
                      "name": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          },
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*endif"
            },
            "named": false,
            "value": "#endif"
          }
        ]
      }
    },
    "preproc_else": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*else"
            },
            "named": false,
            "value": "#else"
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "declaration"
            }
          }
        ]
      }
    },
    "preproc_elif": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*elif"
            },
            "named": false,
            "value": "#elif"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "SYMBOL",
              "name": "declaration"
            }
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "preproc_else"
                    },
                    {
                      "type": "SYMBOL",
                      "name": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          }
        ]
      }
    },
    "preproc_if_in_top_level": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*if"
            },
            "named": false,
            "value": "#if"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "_top_level_item_no_statement"
                },
                {
                  "type": "SYMBOL",
                  "name": "statement"
                }
              ]
            }
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_top_level"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_top_level"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          },
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*endif"
            },
            "named": false,
            "value": "#endif"
          }
        ]
      }
    },
    "preproc_else_in_top_level": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*else"
            },
            "named": false,
            "value": "#else"
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "_top_level_item_no_statement"
                },
                {
                  "type": "SYMBOL",
                  "name": "statement"
                }
              ]
            }
          }
        ]
      }
    },
    "preproc_elif_in_top_level": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*elif"
            },
            "named": false,
            "value": "#elif"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "REPEAT",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "_top_level_item_no_statement"
                },
                {
                  "type": "SYMBOL",
                  "name": "statement"
                }
              ]
            }
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_top_level"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_top_level"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          }
        ]
      }
    },
    "preproc_if_in_expression": {
      "type": "PREC",
      "value": -2,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*if"
            },
            "named": false,
            "value": "#if"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "expression"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_expression"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_expression"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          },
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*endif"
            },
            "named": false,
            "value": "#endif"
          }
        ]
      }
    },
    "preproc_else_in_expression": {
      "type": "PREC",
      "value": -2,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*else"
            },
            "named": false,
            "value": "#else"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "expression"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "preproc_elif_in_expression": {
      "type": "PREC",
      "value": -2,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*elif"
            },
            "named": false,
            "value": "#elif"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "expression"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_expression"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_expression"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          }
        ]
      }
    },
    "preproc_if_in_enum_member_declaration": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*if"
            },
            "named": false,
            "value": "#if"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "enum_member_declaration"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_enum_member_declaration"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_enum_member_declaration"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          },
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*endif"
            },
            "named": false,
            "value": "#endif"
          }
        ]
      }
    },
    "preproc_else_in_enum_member_declaration": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*else"
            },
            "named": false,
            "value": "#else"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "enum_member_declaration"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "preproc_elif_in_enum_member_declaration": {
      "type": "PREC",
      "value": 0,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*elif"
            },
            "named": false,
            "value": "#elif"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "enum_member_declaration"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_enum_member_declaration"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_enum_member_declaration"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          }
        ]
      }
    },
    "preproc_if_in_attribute_list": {
      "type": "PREC",
      "value": -1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*if"
            },
            "named": false,
            "value": "#if"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "attribute_list"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_attribute_list"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_attribute_list"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          },
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*endif"
            },
            "named": false,
            "value": "#endif"
          }
        ]
      }
    },
    "preproc_else_in_attribute_list": {
      "type": "PREC",
      "value": -1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*else"
            },
            "named": false,
            "value": "#else"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "attribute_list"
              },
              {
                "type": "BLANK"
              }
            ]
          }
        ]
      }
    },
    "preproc_elif_in_attribute_list": {
      "type": "PREC",
      "value": -1,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "ALIAS",
            "content": {
              "type": "PATTERN",
              "value": "#[ \t]*elif"
            },
            "named": false,
            "value": "#elif"
          },
          {
            "type": "FIELD",
            "name": "condition",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          },
          {
            "type": "PATTERN",
            "value": "\\n"
          },
          {
            "type": "CHOICE",
            "members": [
              {
                "type": "SYMBOL",
                "name": "attribute_list"
              },
              {
                "type": "BLANK"
              }
            ]
          },
          {
            "type": "FIELD",
            "name": "alternative",
            "content": {
              "type": "CHOICE",
              "members": [
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_else_in_attribute_list"
                      },
                      "named": true,
                      "value": "preproc_else"
                    },
                    {
                      "type": "ALIAS",
                      "content": {
                        "type": "SYMBOL",
                        "name": "preproc_elif_in_attribute_list"
                      },
                      "named": true,
                      "value": "preproc_elif"
                    }
                  ]
                },
                {
                  "type": "BLANK"
                }
              ]
            }
          }
        ]
      }
    },
    "preproc_arg": {
      "type": "TOKEN",
      "content": {
        "type": "PREC",
        "value": -1,
        "content": {
          "type": "PATTERN",
          "value": "\\S([^/\\n]|\\/[^*]|\\\\\\r?\\n)*"
        }
      }
    },
    "preproc_directive": {
      "type": "PATTERN",
      "value": "#[ \\t]*[a-zA-Z0-9]\\w*"
    },
    "_preproc_expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "SYMBOL",
          "name": "identifier"
        },
        {
          "type": "SYMBOL",
          "name": "boolean_literal"
        },
        {
          "type": "SYMBOL",
          "name": "integer_literal"
        },
        {
          "type": "SYMBOL",
          "name": "character_literal"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "preproc_unary_expression"
          },
          "named": true,
          "value": "unary_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "preproc_binary_expression"
          },
          "named": true,
          "value": "binary_expression"
        },
        {
          "type": "ALIAS",
          "content": {
            "type": "SYMBOL",
            "name": "preproc_parenthesized_expression"
          },
          "named": true,
          "value": "parenthesized_expression"
        }
      ]
    },
    "preproc_parenthesized_expression": {
      "type": "SEQ",
      "members": [
        {
          "type": "STRING",
          "value": "("
        },
        {
          "type": "SYMBOL",
          "name": "_preproc_expression"
        },
        {
          "type": "STRING",
          "value": ")"
        }
      ]
    },
    "preproc_unary_expression": {
      "type": "PREC_LEFT",
      "value": 17,
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "FIELD",
            "name": "operator",
            "content": {
              "type": "STRING",
              "value": "!"
            }
          },
          {
            "type": "FIELD",
            "name": "argument",
            "content": {
              "type": "SYMBOL",
              "name": "_preproc_expression"
            }
          }
        ]
      }
    },
    "preproc_binary_expression": {
      "type": "CHOICE",
      "members": [
        {
          "type": "PREC_LEFT",
          "value": 4,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "||"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 5,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "&&"
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 9,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "=="
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              }
            ]
          }
        },
        {
          "type": "PREC_LEFT",
          "value": 9,
          "content": {
            "type": "SEQ",
            "members": [
              {
                "type": "FIELD",
                "name": "left",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              },
              {
                "type": "FIELD",
                "name": "operator",
                "content": {
                  "type": "STRING",
                  "value": "!="
                }
              },
              {
                "type": "FIELD",
                "name": "right",
                "content": {
                  "type": "SYMBOL",
                  "name": "_preproc_expression"
                }
              }
            ]
          }
        }
      ]
    },
    "preproc_region": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*region"
          },
          "named": false,
          "value": "#region"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "content",
              "content": {
                "type": "SYMBOL",
                "name": "preproc_arg"
              }
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_endregion": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*endregion"
          },
          "named": false,
          "value": "#endregion"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "FIELD",
              "name": "content",
              "content": {
                "type": "SYMBOL",
                "name": "preproc_arg"
              }
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_line": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*line"
          },
          "named": false,
          "value": "#line"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "default"
            },
            {
              "type": "STRING",
              "value": "hidden"
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "SYMBOL",
                  "name": "integer_literal"
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "string_literal"
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                }
              ]
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "("
                },
                {
                  "type": "SYMBOL",
                  "name": "integer_literal"
                },
                {
                  "type": "STRING",
                  "value": ","
                },
                {
                  "type": "SYMBOL",
                  "name": "integer_literal"
                },
                {
                  "type": "STRING",
                  "value": ")"
                },
                {
                  "type": "STRING",
                  "value": "-"
                },
                {
                  "type": "STRING",
                  "value": "("
                },
                {
                  "type": "SYMBOL",
                  "name": "integer_literal"
                },
                {
                  "type": "STRING",
                  "value": ","
                },
                {
                  "type": "SYMBOL",
                  "name": "integer_literal"
                },
                {
                  "type": "STRING",
                  "value": ")"
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SYMBOL",
                      "name": "integer_literal"
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                },
                {
                  "type": "SYMBOL",
                  "name": "string_literal"
                }
              ]
            }
          ]
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_pragma": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*pragma"
          },
          "named": false,
          "value": "#pragma"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "warning"
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "STRING",
                      "value": "disable"
                    },
                    {
                      "type": "STRING",
                      "value": "restore"
                    }
                  ]
                },
                {
                  "type": "CHOICE",
                  "members": [
                    {
                      "type": "SEQ",
                      "members": [
                        {
                          "type": "CHOICE",
                          "members": [
                            {
                              "type": "SYMBOL",
                              "name": "identifier"
                            },
                            {
                              "type": "SYMBOL",
                              "name": "integer_literal"
                            }
                          ]
                        },
                        {
                          "type": "REPEAT",
                          "content": {
                            "type": "SEQ",
                            "members": [
                              {
                                "type": "STRING",
                                "value": ","
                              },
                              {
                                "type": "CHOICE",
                                "members": [
                                  {
                                    "type": "SYMBOL",
                                    "name": "identifier"
                                  },
                                  {
                                    "type": "SYMBOL",
                                    "name": "integer_literal"
                                  }
                                ]
                              }
                            ]
                          }
                        }
                      ]
                    },
                    {
                      "type": "BLANK"
                    }
                  ]
                }
              ]
            },
            {
              "type": "SEQ",
              "members": [
                {
                  "type": "STRING",
                  "value": "checksum"
                },
                {
                  "type": "SYMBOL",
                  "name": "string_literal"
                },
                {
                  "type": "SYMBOL",
                  "name": "string_literal"
                },
                {
                  "type": "SYMBOL",
                  "name": "string_literal"
                }
              ]
            }
          ]
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_nullable": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*nullable"
          },
          "named": false,
          "value": "#nullable"
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "STRING",
              "value": "enable"
            },
            {
              "type": "STRING",
              "value": "disable"
            },
            {
              "type": "STRING",
              "value": "restore"
            }
          ]
        },
        {
          "type": "CHOICE",
          "members": [
            {
              "type": "CHOICE",
              "members": [
                {
                  "type": "STRING",
                  "value": "annotations"
                },
                {
                  "type": "STRING",
                  "value": "warnings"
                }
              ]
            },
            {
              "type": "BLANK"
            }
          ]
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_error": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*error"
          },
          "named": false,
          "value": "#error"
        },
        {
          "type": "SYMBOL",
          "name": "preproc_arg"
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_warning": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*warning"
          },
          "named": false,
          "value": "#warning"
        },
        {
          "type": "SYMBOL",
          "name": "preproc_arg"
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_define": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*define"
          },
          "named": false,
          "value": "#define"
        },
        {
          "type": "SYMBOL",
          "name": "preproc_arg"
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "preproc_undef": {
      "type": "SEQ",
      "members": [
        {
          "type": "ALIAS",
          "content": {
            "type": "PATTERN",
            "value": "#[ \t]*undef"
          },
          "named": false,
          "value": "#undef"
        },
        {
          "type": "SYMBOL",
          "name": "preproc_arg"
        },
        {
          "type": "PATTERN",
          "value": "\\n"
        }
      ]
    },
    "shebang_directive": {
      "type": "TOKEN",
      "content": {
        "type": "SEQ",
        "members": [
          {
            "type": "STRING",
            "value": "#!"
          },
          {
            "type": "PATTERN",
            "value": ".*"
          }
        ]
      }
    },
    "comment": {
      "type": "TOKEN",
      "content": {
        "type": "CHOICE",
        "members": [
          {
            "type": "SEQ",
            "members": [
              {
                "type": "STRING",
                "value": "//"
              },
              {
                "type": "PATTERN",
                "value": "[^\\n\\r]*"
              }
            ]
          },
          {
            "type": "SEQ",
            "members": [
              {
                "type": "STRING",
                "value": "/*"
              },
              {
                "type": "PATTERN",
                "value": "[^*]*\\*+([^/*][^*]*\\*+)*"
              },
              {
                "type": "STRING",
                "value": "/"
              }
            ]
          }
        ]
      }
    }
  },
  "extras": [
    {
      "type": "PATTERN",
      "value": "[\\s\\u00A0\\uFEFF\\u3000]+"
    },
    {
      "type": "SYMBOL",
      "name": "comment"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_region"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_endregion"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_line"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_pragma"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_nullable"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_error"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_warning"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_define"
    },
    {
      "type": "SYMBOL",
      "name": "preproc_undef"
    }
  ],
  "conflicts": [
    [
      "_simple_name",
      "generic_name"
    ],
    [
      "_simple_name",
      "type_parameter"
    ],
    [
      "_simple_name",
      "subpattern"
    ],
    [
      "tuple_element",
      "type_pattern"
    ],
    [
      "tuple_element",
      "using_variable_declarator"
    ],
    [
      "tuple_element",
      "declaration_expression"
    ],
    [
      "tuple_pattern",
      "parameter"
    ],
    [
      "tuple_pattern",
      "_simple_name"
    ],
    [
      "lvalue_expression",
      "_name"
    ],
    [
      "parameter",
      "lvalue_expression"
    ],
    [
      "type",
      "attribute"
    ],
    [
      "type",
      "nullable_type"
    ],
    [
      "type",
      "nullable_type",
      "array_creation_expression"
    ],
    [
      "type",
      "_array_base_type"
    ],
    [
      "type",
      "_array_base_type",
      "array_creation_expression"
    ],
    [
      "type",
      "array_creation_expression"
    ],
    [
      "type",
      "_pointer_base_type"
    ],
    [
      "qualified_name",
      "member_access_expression"
    ],
    [
      "qualified_name",
      "explicit_interface_specifier"
    ],
    [
      "_array_base_type",
      "stackalloc_expression"
    ],
    [
      "constant_pattern",
      "non_lvalue_expression"
    ],
    [
      "constant_pattern",
      "_expression_statement_expression"
    ],
    [
      "constant_pattern",
      "lvalue_expression"
    ],
    [
      "constant_pattern",
      "_name"
    ],
    [
      "constant_pattern",
      "lvalue_expression",
      "_name"
    ],
    [
      "type",
      "_name_invocation_pattern",
      "recursive_pattern"
    ],
    [
      "attribute",
      "type",
      "_name_invocation_pattern",
      "recursive_pattern"
    ],
    [
      "parenthesized_pattern",
      "_parenthesized_pattern_with_designation"
    ],
    [
      "_reserved_identifier",
      "modifier"
    ],
    [
      "_reserved_identifier",
      "scoped_type"
    ],
    [
      "_reserved_identifier",
      "implicit_type"
    ],
    [
      "_reserved_identifier",
      "from_clause"
    ],
    [
      "_reserved_identifier",
      "implicit_type",
      "var_pattern"
    ],
    [
      "_reserved_identifier",
      "type_parameter_constraint"
    ],
    [
      "_reserved_identifier",
      "parameter",
      "scoped_type"
    ],
    [
      "_reserved_identifier",
      "parameter"
    ],
    [
      "_simple_name",
      "parameter"
    ],
    [
      "tuple_element",
      "parameter",
      "declaration_expression"
    ],
    [
      "parameter",
      "tuple_element"
    ],
    [
      "event_declaration",
      "variable_declarator"
    ],
    [
      "base_list"
    ],
    [
      "using_directive",
      "modifier"
    ],
    [
      "using_directive"
    ],
    [
      "_constructor_declaration_initializer",
      "_simple_name"
    ]
  ],
  "precedences": [
    [
      {
        "type": "SYMBOL",
        "name": "_anonymous_object_member_declarator"
      },
      {
        "type": "SYMBOL",
        "name": "_simple_name"
      }
    ],
    [
      {
        "type": "SYMBOL",
        "name": "block"
      },
      {
        "type": "SYMBOL",
        "name": "initializer_expression"
      }
    ]
  ],
  "externals": [
    {
      "type": "SYMBOL",
      "name": "_optional_semi"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_regular_start"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_verbatim_start"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_raw_start"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_start_quote"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_end_quote"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_open_brace"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_close_brace"
    },
    {
      "type": "SYMBOL",
      "name": "interpolation_string_content"
    },
    {
      "type": "SYMBOL",
      "name": "raw_string_start"
    },
    {
      "type": "SYMBOL",
      "name": "raw_string_end"
    },
    {
      "type": "SYMBOL",
      "name": "raw_string_content"
    }
  ],
  "inline": [
    "_namespace_member_declaration",
    "_object_creation_type",
    "_nullable_base_type",
    "_parameter_type_with_modifiers",
    "_top_level_item_no_statement"
  ],
  "supertypes": [
    "declaration",
    "expression",
    "non_lvalue_expression",
    "lvalue_expression",
    "literal",
    "statement",
    "type",
    "type_declaration",
    "pattern"
  ],
  "reserved": {}
}
```

## File: `src/node-types.json`
```json
[
  {
    "type": "declaration",
    "named": true,
    "subtypes": [
      {
        "type": "class_declaration",
        "named": true
      },
      {
        "type": "constructor_declaration",
        "named": true
      },
      {
        "type": "conversion_operator_declaration",
        "named": true
      },
      {
        "type": "delegate_declaration",
        "named": true
      },
      {
        "type": "destructor_declaration",
        "named": true
      },
      {
        "type": "enum_declaration",
        "named": true
      },
      {
        "type": "event_declaration",
        "named": true
      },
      {
        "type": "event_field_declaration",
        "named": true
      },
      {
        "type": "field_declaration",
        "named": true
      },
      {
        "type": "indexer_declaration",
        "named": true
      },
      {
        "type": "interface_declaration",
        "named": true
      },
      {
        "type": "method_declaration",
        "named": true
      },
      {
        "type": "namespace_declaration",
        "named": true
      },
      {
        "type": "operator_declaration",
        "named": true
      },
      {
        "type": "preproc_if",
        "named": true
      },
      {
        "type": "property_declaration",
        "named": true
      },
      {
        "type": "record_declaration",
        "named": true
      },
      {
        "type": "struct_declaration",
        "named": true
      },
      {
        "type": "using_directive",
        "named": true
      }
    ]
  },
  {
    "type": "expression",
    "named": true,
    "subtypes": [
      {
        "type": "lvalue_expression",
        "named": true
      },
      {
        "type": "non_lvalue_expression",
        "named": true
      }
    ]
  },
  {
    "type": "literal",
    "named": true,
    "subtypes": [
      {
        "type": "boolean_literal",
        "named": true
      },
      {
        "type": "character_literal",
        "named": true
      },
      {
        "type": "integer_literal",
        "named": true
      },
      {
        "type": "null_literal",
        "named": true
      },
      {
        "type": "raw_string_literal",
        "named": true
      },
      {
        "type": "real_literal",
        "named": true
      },
      {
        "type": "string_literal",
        "named": true
      },
      {
        "type": "verbatim_string_literal",
        "named": true
      }
    ]
  },
  {
    "type": "lvalue_expression",
    "named": true,
    "subtypes": [
      {
        "type": "element_access_expression",
        "named": true
      },
      {
        "type": "element_binding_expression",
        "named": true
      },
      {
        "type": "generic_name",
        "named": true
      },
      {
        "type": "identifier",
        "named": true
      },
      {
        "type": "member_access_expression",
        "named": true
      },
      {
        "type": "parenthesized_expression",
        "named": true
      },
      {
        "type": "prefix_unary_expression",
        "named": true
      },
      {
        "type": "this",
        "named": false
      },
      {
        "type": "tuple_expression",
        "named": true
      }
    ]
  },
  {
    "type": "non_lvalue_expression",
    "named": true,
    "subtypes": [
      {
        "type": "anonymous_method_expression",
        "named": true
      },
      {
        "type": "anonymous_object_creation_expression",
        "named": true
      },
      {
        "type": "array_creation_expression",
        "named": true
      },
      {
        "type": "as_expression",
        "named": true
      },
      {
        "type": "assignment_expression",
        "named": true
      },
      {
        "type": "await_expression",
        "named": true
      },
      {
        "type": "base",
        "named": false
      },
      {
        "type": "binary_expression",
        "named": true
      },
      {
        "type": "cast_expression",
        "named": true
      },
      {
        "type": "checked_expression",
        "named": true
      },
      {
        "type": "conditional_access_expression",
        "named": true
      },
      {
        "type": "conditional_expression",
        "named": true
      },
      {
        "type": "default_expression",
        "named": true
      },
      {
        "type": "implicit_array_creation_expression",
        "named": true
      },
      {
        "type": "implicit_object_creation_expression",
        "named": true
      },
      {
        "type": "implicit_stackalloc_expression",
        "named": true
      },
      {
        "type": "initializer_expression",
        "named": true
      },
      {
        "type": "interpolated_string_expression",
        "named": true
      },
      {
        "type": "invocation_expression",
        "named": true
      },
      {
        "type": "is_expression",
        "named": true
      },
      {
        "type": "is_pattern_expression",
        "named": true
      },
      {
        "type": "lambda_expression",
        "named": true
      },
      {
        "type": "literal",
        "named": true
      },
      {
        "type": "makeref_expression",
        "named": true
      },
      {
        "type": "object_creation_expression",
        "named": true
      },
      {
        "type": "parenthesized_expression",
        "named": true
      },
      {
        "type": "postfix_unary_expression",
        "named": true
      },
      {
        "type": "prefix_unary_expression",
        "named": true
      },
      {
        "type": "preproc_if",
        "named": true
      },
      {
        "type": "query_expression",
        "named": true
      },
      {
        "type": "range_expression",
        "named": true
      },
      {
        "type": "ref_expression",
        "named": true
      },
      {
        "type": "reftype_expression",
        "named": true
      },
      {
        "type": "refvalue_expression",
        "named": true
      },
      {
        "type": "sizeof_expression",
        "named": true
      },
      {
        "type": "stackalloc_expression",
        "named": true
      },
      {
        "type": "switch_expression",
        "named": true
      },
      {
        "type": "throw_expression",
        "named": true
      },
      {
        "type": "typeof_expression",
        "named": true
      },
      {
        "type": "with_expression",
        "named": true
      }
    ]
  },
  {
    "type": "pattern",
    "named": true,
    "subtypes": [
      {
        "type": "and_pattern",
        "named": true
      },
      {
        "type": "constant_pattern",
        "named": true
      },
      {
        "type": "declaration_pattern",
        "named": true
      },
      {
        "type": "discard",
        "named": true
      },
      {
        "type": "list_pattern",
        "named": true
      },
      {
        "type": "negated_pattern",
        "named": true
      },
      {
        "type": "or_pattern",
        "named": true
      },
      {
        "type": "parenthesized_pattern",
        "named": true
      },
      {
        "type": "recursive_pattern",
        "named": true
      },
      {
        "type": "relational_pattern",
        "named": true
      },
      {
        "type": "type_pattern",
        "named": true
      },
      {
        "type": "var_pattern",
        "named": true
      }
    ]
  },
  {
    "type": "statement",
    "named": true,
    "subtypes": [
      {
        "type": "block",
        "named": true
      },
      {
        "type": "break_statement",
        "named": true
      },
      {
        "type": "checked_statement",
        "named": true
      },
      {
        "type": "continue_statement",
        "named": true
      },
      {
        "type": "do_statement",
        "named": true
      },
      {
        "type": "empty_statement",
        "named": true
      },
      {
        "type": "expression_statement",
        "named": true
      },
      {
        "type": "fixed_statement",
        "named": true
      },
      {
        "type": "for_statement",
        "named": true
      },
      {
        "type": "foreach_statement",
        "named": true
      },
      {
        "type": "goto_statement",
        "named": true
      },
      {
        "type": "if_statement",
        "named": true
      },
      {
        "type": "labeled_statement",
        "named": true
      },
      {
        "type": "local_declaration_statement",
        "named": true
      },
      {
        "type": "local_function_statement",
        "named": true
      },
      {
        "type": "lock_statement",
        "named": true
      },
      {
        "type": "preproc_if",
        "named": true
      },
      {
        "type": "return_statement",
        "named": true
      },
      {
        "type": "switch_statement",
        "named": true
      },
      {
        "type": "throw_statement",
        "named": true
      },
      {
        "type": "try_statement",
        "named": true
      },
      {
        "type": "unsafe_statement",
        "named": true
      },
      {
        "type": "using_statement",
        "named": true
      },
      {
        "type": "while_statement",
        "named": true
      },
      {
        "type": "yield_statement",
        "named": true
      }
    ]
  },
  {
    "type": "type",
    "named": true,
    "subtypes": [
      {
        "type": "alias_qualified_name",
        "named": true
      },
      {
        "type": "array_type",
        "named": true
      },
      {
        "type": "function_pointer_type",
        "named": true
      },
      {
        "type": "generic_name",
        "named": true
      },
      {
        "type": "identifier",
        "named": true
      },
      {
        "type": "implicit_type",
        "named": true
      },
      {
        "type": "nullable_type",
        "named": true
      },
      {
        "type": "pointer_type",
        "named": true
      },
      {
        "type": "predefined_type",
        "named": true
      },
      {
        "type": "qualified_name",
        "named": true
      },
      {
        "type": "ref_type",
        "named": true
      },
      {
        "type": "scoped_type",
        "named": true
      },
      {
        "type": "tuple_type",
        "named": true
      }
    ]
  },
  {
    "type": "type_declaration",
    "named": true,
    "subtypes": [
      {
        "type": "class_declaration",
        "named": true
      },
      {
        "type": "delegate_declaration",
        "named": true
      },
      {
        "type": "enum_declaration",
        "named": true
      },
      {
        "type": "interface_declaration",
        "named": true
      },
      {
        "type": "record_declaration",
        "named": true
      },
      {
        "type": "struct_declaration",
        "named": true
      }
    ]
  },
  {
    "type": "accessor_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "block",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "add",
            "named": false
          },
          {
            "type": "get",
            "named": false
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "init",
            "named": false
          },
          {
            "type": "remove",
            "named": false
          },
          {
            "type": "set",
            "named": false
          }
        ]
      }
    },
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "accessor_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "accessor_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "alias_qualified_name",
    "named": true,
    "fields": {
      "alias": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "and_pattern",
    "named": true,
    "fields": {
      "left": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "pattern",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "and",
            "named": false
          }
        ]
      },
      "right": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "pattern",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "anonymous_method_expression",
    "named": true,
    "fields": {
      "parameters": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "parameter_list",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "block",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        }
      ]
    }
  },
  {
    "type": "anonymous_object_creation_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        }
      ]
    }
  },
  {
    "type": "argument",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "declaration_expression",
          "named": true
        },
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "argument_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "argument",
          "named": true
        }
      ]
    }
  },
  {
    "type": "array_creation_expression",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "array_type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "initializer_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "array_rank_specifier",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "array_type",
    "named": true,
    "fields": {
      "rank": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "array_rank_specifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "array_type",
            "named": true
          },
          {
            "type": "function_pointer_type",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "nullable_type",
            "named": true
          },
          {
            "type": "pointer_type",
            "named": true
          },
          {
            "type": "predefined_type",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          },
          {
            "type": "tuple_type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "arrow_expression_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "as_expression",
    "named": true,
    "fields": {
      "left": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "as",
            "named": false
          }
        ]
      },
      "right": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "assignment_expression",
    "named": true,
    "fields": {
      "left": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "lvalue_expression",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "%=",
            "named": false
          },
          {
            "type": "&=",
            "named": false
          },
          {
            "type": "*=",
            "named": false
          },
          {
            "type": "+=",
            "named": false
          },
          {
            "type": "-=",
            "named": false
          },
          {
            "type": "/=",
            "named": false
          },
          {
            "type": "<<=",
            "named": false
          },
          {
            "type": "=",
            "named": false
          },
          {
            "type": ">>=",
            "named": false
          },
          {
            "type": ">>>=",
            "named": false
          },
          {
            "type": "??=",
            "named": false
          },
          {
            "type": "^=",
            "named": false
          },
          {
            "type": "|=",
            "named": false
          }
        ]
      },
      "right": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "attribute",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "attribute_argument_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "attribute_argument",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "attribute_argument_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "attribute_argument",
          "named": true
        }
      ]
    }
  },
  {
    "type": "attribute_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "attribute",
          "named": true
        },
        {
          "type": "attribute_target_specifier",
          "named": true
        }
      ]
    }
  },
  {
    "type": "attribute_target_specifier",
    "named": true,
    "fields": {}
  },
  {
    "type": "await_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "base_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "argument_list",
          "named": true
        },
        {
          "type": "primary_constructor_base_type",
          "named": true
        },
        {
          "type": "type",
          "named": true
        }
      ]
    }
  },
  {
    "type": "binary_expression",
    "named": true,
    "fields": {
      "left": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "binary_expression",
            "named": true
          },
          {
            "type": "boolean_literal",
            "named": true
          },
          {
            "type": "character_literal",
            "named": true
          },
          {
            "type": "expression",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "integer_literal",
            "named": true
          },
          {
            "type": "parenthesized_expression",
            "named": true
          },
          {
            "type": "unary_expression",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "!=",
            "named": false
          },
          {
            "type": "%",
            "named": false
          },
          {
            "type": "&",
            "named": false
          },
          {
            "type": "&&",
            "named": false
          },
          {
            "type": "*",
            "named": false
          },
          {
            "type": "+",
            "named": false
          },
          {
            "type": "-",
            "named": false
          },
          {
            "type": "/",
            "named": false
          },
          {
            "type": "<",
            "named": false
          },
          {
            "type": "<<",
            "named": false
          },
          {
            "type": "<=",
            "named": false
          },
          {
            "type": "==",
            "named": false
          },
          {
            "type": ">",
            "named": false
          },
          {
            "type": ">=",
            "named": false
          },
          {
            "type": ">>",
            "named": false
          },
          {
            "type": ">>>",
            "named": false
          },
          {
            "type": "??",
            "named": false
          },
          {
            "type": "^",
            "named": false
          },
          {
            "type": "|",
            "named": false
          },
          {
            "type": "||",
            "named": false
          }
        ]
      },
      "right": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "binary_expression",
            "named": true
          },
          {
            "type": "boolean_literal",
            "named": true
          },
          {
            "type": "character_literal",
            "named": true
          },
          {
            "type": "expression",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "integer_literal",
            "named": true
          },
          {
            "type": "parenthesized_expression",
            "named": true
          },
          {
            "type": "unary_expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "block",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "statement",
          "named": true
        }
      ]
    }
  },
  {
    "type": "boolean_literal",
    "named": true,
    "fields": {}
  },
  {
    "type": "bracketed_argument_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "argument",
          "named": true
        }
      ]
    }
  },
  {
    "type": "bracketed_parameter_list",
    "named": true,
    "fields": {
      "name": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": "type",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "parameter",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "break_statement",
    "named": true,
    "fields": {}
  },
  {
    "type": "calling_convention",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "identifier",
          "named": true
        }
      ]
    }
  },
  {
    "type": "cast_expression",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      },
      "value": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "catch_clause",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "block",
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
          "type": "catch_declaration",
          "named": true
        },
        {
          "type": "catch_filter_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "catch_declaration",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "catch_filter_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "character_literal",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "character_literal_content",
          "named": true
        },
        {
          "type": "escape_sequence",
          "named": true
        }
      ]
    }
  },
  {
    "type": "checked_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "checked_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "block",
          "named": true
        }
      ]
    }
  },
  {
    "type": "class_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "declaration_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "base_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "parameter_list",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "type_parameter_constraints_clause",
          "named": true
        },
        {
          "type": "type_parameter_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "compilation_unit",
    "named": true,
    "root": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "extern_alias_directive",
          "named": true
        },
        {
          "type": "file_scoped_namespace_declaration",
          "named": true
        },
        {
          "type": "global_attribute",
          "named": true
        },
        {
          "type": "global_statement",
          "named": true
        },
        {
          "type": "namespace_declaration",
          "named": true
        },
        {
          "type": "preproc_if",
          "named": true
        },
        {
          "type": "shebang_directive",
          "named": true
        },
        {
          "type": "type_declaration",
          "named": true
        },
        {
          "type": "using_directive",
          "named": true
        }
      ]
    }
  },
  {
    "type": "conditional_access_expression",
    "named": true,
    "fields": {
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "element_binding_expression",
          "named": true
        },
        {
          "type": "member_binding_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "conditional_expression",
    "named": true,
    "fields": {
      "alternative": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "consequence": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "constant_pattern",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "binary_expression",
          "named": true
        },
        {
          "type": "cast_expression",
          "named": true
        },
        {
          "type": "default_expression",
          "named": true
        },
        {
          "type": "generic_name",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "interpolated_string_expression",
          "named": true
        },
        {
          "type": "invocation_expression",
          "named": true
        },
        {
          "type": "literal",
          "named": true
        },
        {
          "type": "member_access_expression",
          "named": true
        },
        {
          "type": "parenthesized_expression",
          "named": true
        },
        {
          "type": "postfix_unary_expression",
          "named": true
        },
        {
          "type": "prefix_unary_expression",
          "named": true
        },
        {
          "type": "sizeof_expression",
          "named": true
        },
        {
          "type": "tuple_expression",
          "named": true
        },
        {
          "type": "typeof_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "constructor_constraint",
    "named": true,
    "fields": {}
  },
  {
    "type": "constructor_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "block",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "parameter_list",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "constructor_initializer",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "constructor_initializer",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "argument_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "continue_statement",
    "named": true,
    "fields": {}
  },
  {
    "type": "conversion_operator_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "block",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "parameter_list",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "explicit_interface_specifier",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "declaration_expression",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "declaration_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "declaration_pattern",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "discard",
          "named": true
        },
        {
          "type": "parenthesized_variable_designation",
          "named": true
        }
      ]
    }
  },
  {
    "type": "default_expression",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "delegate_declaration",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "parameter_list",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      },
      "type_parameters": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type_parameter_list",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "type_parameter_constraints_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "destructor_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "block",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "parameter_list",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "do_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "statement",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "element_access_expression",
    "named": true,
    "fields": {
      "expression": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "subscript": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "bracketed_argument_list",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "element_binding_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "argument",
          "named": true
        }
      ]
    }
  },
  {
    "type": "empty_statement",
    "named": true,
    "fields": {}
  },
  {
    "type": "enum_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "enum_member_declaration_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "base_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "enum_member_declaration",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "value": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "expression",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "enum_member_declaration_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "enum_member_declaration",
          "named": true
        },
        {
          "type": "preproc_if",
          "named": true
        }
      ]
    }
  },
  {
    "type": "event_declaration",
    "named": true,
    "fields": {
      "accessors": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "accessor_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "explicit_interface_specifier",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "event_field_declaration",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "variable_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "explicit_interface_specifier",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "alias_qualified_name",
          "named": true
        },
        {
          "type": "generic_name",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "qualified_name",
          "named": true
        }
      ]
    }
  },
  {
    "type": "expression_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "assignment_expression",
          "named": true
        },
        {
          "type": "await_expression",
          "named": true
        },
        {
          "type": "invocation_expression",
          "named": true
        },
        {
          "type": "object_creation_expression",
          "named": true
        },
        {
          "type": "parenthesized_expression",
          "named": true
        },
        {
          "type": "postfix_unary_expression",
          "named": true
        },
        {
          "type": "prefix_unary_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "extern_alias_directive",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "field_declaration",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "variable_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "file_scoped_namespace_declaration",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "finally_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "block",
          "named": true
        }
      ]
    }
  },
  {
    "type": "fixed_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "statement",
          "named": true
        },
        {
          "type": "variable_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "for_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "statement",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "initializer": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": ",",
            "named": false
          },
          {
            "type": "expression",
            "named": true
          },
          {
            "type": "variable_declaration",
            "named": true
          }
        ]
      },
      "update": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": ",",
            "named": false
          },
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "foreach_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "statement",
            "named": true
          }
        ]
      },
      "left": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "tuple_pattern",
            "named": true
          }
        ]
      },
      "right": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "from_clause",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "function_pointer_parameter",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "array_type",
            "named": true
          },
          {
            "type": "function_pointer_type",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "implicit_type",
            "named": true
          },
          {
            "type": "nullable_type",
            "named": true
          },
          {
            "type": "pointer_type",
            "named": true
          },
          {
            "type": "predefined_type",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          },
          {
            "type": "tuple_type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "function_pointer_type",
    "named": true,
    "fields": {
      "returns": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
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
          "type": "calling_convention",
          "named": true
        },
        {
          "type": "function_pointer_parameter",
          "named": true
        }
      ]
    }
  },
  {
    "type": "generic_name",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "type_argument_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "global_attribute",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "attribute",
          "named": true
        }
      ]
    }
  },
  {
    "type": "global_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "statement",
          "named": true
        }
      ]
    }
  },
  {
    "type": "goto_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "group_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "identifier",
    "named": true,
    "fields": {}
  },
  {
    "type": "if_statement",
    "named": true,
    "fields": {
      "alternative": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "statement",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "consequence": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "statement",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "implicit_array_creation_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "initializer_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "implicit_object_creation_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "argument_list",
          "named": true
        },
        {
          "type": "initializer_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "implicit_parameter",
    "named": true,
    "fields": {}
  },
  {
    "type": "implicit_stackalloc_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "initializer_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "implicit_type",
    "named": true,
    "fields": {}
  },
  {
    "type": "indexer_declaration",
    "named": true,
    "fields": {
      "accessors": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "accessor_list",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "bracketed_parameter_list",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      },
      "value": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "explicit_interface_specifier",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "initializer_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "interface_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "declaration_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type_parameters": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type_parameter_list",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "base_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "type_parameter_constraints_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "interpolated_string_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "escape_sequence",
          "named": true
        },
        {
          "type": "interpolation",
          "named": true
        },
        {
          "type": "interpolation_quote",
          "named": true
        },
        {
          "type": "interpolation_start",
          "named": true
        },
        {
          "type": "string_content",
          "named": true
        }
      ]
    }
  },
  {
    "type": "interpolation",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "interpolation_alignment_clause",
          "named": true
        },
        {
          "type": "interpolation_brace",
          "named": true
        },
        {
          "type": "interpolation_format_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "interpolation_alignment_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "interpolation_format_clause",
    "named": true,
    "fields": {}
  },
  {
    "type": "invocation_expression",
    "named": true,
    "fields": {
      "arguments": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "argument_list",
            "named": true
          }
        ]
      },
      "function": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "cast_expression",
            "named": true
          },
          {
            "type": "conditional_access_expression",
            "named": true
          },
          {
            "type": "element_access_expression",
            "named": true
          },
          {
            "type": "expression",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "invocation_expression",
            "named": true
          },
          {
            "type": "member_access_expression",
            "named": true
          },
          {
            "type": "parenthesized_expression",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "is_expression",
    "named": true,
    "fields": {
      "left": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "is",
            "named": false
          }
        ]
      },
      "right": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "is_pattern_expression",
    "named": true,
    "fields": {
      "expression": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "pattern": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "pattern",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "join_clause",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "join_into_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "join_into_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "identifier",
          "named": true
        }
      ]
    }
  },
  {
    "type": "labeled_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "statement",
          "named": true
        }
      ]
    }
  },
  {
    "type": "lambda_expression",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "block",
            "named": true
          },
          {
            "type": "expression",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "implicit_parameter",
            "named": true
          },
          {
            "type": "parameter_list",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "let_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        }
      ]
    }
  },
  {
    "type": "list_pattern",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
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
          "type": "parenthesized_variable_designation",
          "named": true
        },
        {
          "type": "pattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "local_declaration_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "variable_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "local_function_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "block",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "parameter_list",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      },
      "type_parameters": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type_parameter_list",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "type_parameter_constraints_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "lock_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "statement",
          "named": true
        }
      ]
    }
  },
  {
    "type": "makeref_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "member_access_expression",
    "named": true,
    "fields": {
      "expression": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "expression",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "predefined_type",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "member_binding_expression",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "method_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "block",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "parameter_list",
            "named": true
          }
        ]
      },
      "returns": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      },
      "type_parameters": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type_parameter_list",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "explicit_interface_specifier",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "type_parameter_constraints_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "modifier",
    "named": true,
    "fields": {}
  },
  {
    "type": "namespace_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "declaration_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "negated_pattern",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "pattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "nullable_type",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "array_type",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "predefined_type",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          },
          {
            "type": "tuple_type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "object_creation_expression",
    "named": true,
    "fields": {
      "arguments": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "argument_list",
            "named": true
          }
        ]
      },
      "initializer": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "initializer_expression",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "operator_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "block",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "!",
            "named": false
          },
          {
            "type": "!=",
            "named": false
          },
          {
            "type": "%",
            "named": false
          },
          {
            "type": "&",
            "named": false
          },
          {
            "type": "*",
            "named": false
          },
          {
            "type": "+",
            "named": false
          },
          {
            "type": "++",
            "named": false
          },
          {
            "type": "-",
            "named": false
          },
          {
            "type": "--",
            "named": false
          },
          {
            "type": "/",
            "named": false
          },
          {
            "type": "<",
            "named": false
          },
          {
            "type": "<<",
            "named": false
          },
          {
            "type": "<=",
            "named": false
          },
          {
            "type": "==",
            "named": false
          },
          {
            "type": ">",
            "named": false
          },
          {
            "type": ">=",
            "named": false
          },
          {
            "type": ">>",
            "named": false
          },
          {
            "type": ">>>",
            "named": false
          },
          {
            "type": "^",
            "named": false
          },
          {
            "type": "false",
            "named": false
          },
          {
            "type": "true",
            "named": false
          },
          {
            "type": "|",
            "named": false
          },
          {
            "type": "~",
            "named": false
          }
        ]
      },
      "parameters": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "parameter_list",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "explicit_interface_specifier",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "or_pattern",
    "named": true,
    "fields": {
      "left": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "pattern",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "or",
            "named": false
          }
        ]
      },
      "right": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "pattern",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "order_by_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "parameter",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "parameter_list",
    "named": true,
    "fields": {
      "name": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": "type",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "parameter",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "parenthesized_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "boolean_literal",
          "named": true
        },
        {
          "type": "character_literal",
          "named": true
        },
        {
          "type": "integer_literal",
          "named": true
        },
        {
          "type": "lvalue_expression",
          "named": true
        },
        {
          "type": "non_lvalue_expression",
          "named": true
        },
        {
          "type": "unary_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "parenthesized_pattern",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "pattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "parenthesized_variable_designation",
    "named": true,
    "fields": {
      "name": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": "identifier",
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
          "type": "discard",
          "named": true
        },
        {
          "type": "parenthesized_variable_designation",
          "named": true
        }
      ]
    }
  },
  {
    "type": "pointer_type",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "function_pointer_type",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "nullable_type",
            "named": true
          },
          {
            "type": "pointer_type",
            "named": true
          },
          {
            "type": "predefined_type",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          },
          {
            "type": "tuple_type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "positional_pattern_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "subpattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "postfix_unary_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "prefix_unary_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_define",
    "named": true,
    "extra": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "preproc_arg",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_elif",
    "named": true,
    "fields": {
      "alternative": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "preproc_elif",
            "named": true
          },
          {
            "type": "preproc_else",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "binary_expression",
            "named": true
          },
          {
            "type": "boolean_literal",
            "named": true
          },
          {
            "type": "character_literal",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "integer_literal",
            "named": true
          },
          {
            "type": "parenthesized_expression",
            "named": true
          },
          {
            "type": "unary_expression",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "declaration",
          "named": true
        },
        {
          "type": "enum_member_declaration",
          "named": true
        },
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "extern_alias_directive",
          "named": true
        },
        {
          "type": "file_scoped_namespace_declaration",
          "named": true
        },
        {
          "type": "global_attribute",
          "named": true
        },
        {
          "type": "statement",
          "named": true
        },
        {
          "type": "type_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_else",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "declaration",
          "named": true
        },
        {
          "type": "enum_member_declaration",
          "named": true
        },
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "extern_alias_directive",
          "named": true
        },
        {
          "type": "file_scoped_namespace_declaration",
          "named": true
        },
        {
          "type": "global_attribute",
          "named": true
        },
        {
          "type": "statement",
          "named": true
        },
        {
          "type": "type_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_endregion",
    "named": true,
    "extra": true,
    "fields": {
      "content": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "preproc_arg",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "preproc_error",
    "named": true,
    "extra": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "preproc_arg",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_if",
    "named": true,
    "fields": {
      "alternative": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "preproc_elif",
            "named": true
          },
          {
            "type": "preproc_else",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "binary_expression",
            "named": true
          },
          {
            "type": "boolean_literal",
            "named": true
          },
          {
            "type": "character_literal",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "integer_literal",
            "named": true
          },
          {
            "type": "parenthesized_expression",
            "named": true
          },
          {
            "type": "unary_expression",
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
          "type": "declaration",
          "named": true
        },
        {
          "type": "enum_member_declaration",
          "named": true
        },
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "extern_alias_directive",
          "named": true
        },
        {
          "type": "file_scoped_namespace_declaration",
          "named": true
        },
        {
          "type": "global_attribute",
          "named": true
        },
        {
          "type": "statement",
          "named": true
        },
        {
          "type": "type_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_if_in_attribute_list",
    "named": true,
    "fields": {
      "alternative": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "preproc_elif",
            "named": true
          },
          {
            "type": "preproc_else",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "binary_expression",
            "named": true
          },
          {
            "type": "boolean_literal",
            "named": true
          },
          {
            "type": "character_literal",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "integer_literal",
            "named": true
          },
          {
            "type": "parenthesized_expression",
            "named": true
          },
          {
            "type": "unary_expression",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_line",
    "named": true,
    "extra": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "integer_literal",
          "named": true
        },
        {
          "type": "string_literal",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_nullable",
    "named": true,
    "extra": true,
    "fields": {}
  },
  {
    "type": "preproc_pragma",
    "named": true,
    "extra": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "integer_literal",
          "named": true
        },
        {
          "type": "string_literal",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_region",
    "named": true,
    "extra": true,
    "fields": {
      "content": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "preproc_arg",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "preproc_undef",
    "named": true,
    "extra": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "preproc_arg",
          "named": true
        }
      ]
    }
  },
  {
    "type": "preproc_warning",
    "named": true,
    "extra": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "preproc_arg",
          "named": true
        }
      ]
    }
  },
  {
    "type": "primary_constructor_base_type",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "argument_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "property_declaration",
    "named": true,
    "fields": {
      "accessors": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "accessor_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      },
      "value": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "arrow_expression_clause",
            "named": true
          },
          {
            "type": "expression",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "explicit_interface_specifier",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "property_pattern_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "subpattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "qualified_name",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "qualifier": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "query_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "from_clause",
          "named": true
        },
        {
          "type": "group_clause",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "join_clause",
          "named": true
        },
        {
          "type": "let_clause",
          "named": true
        },
        {
          "type": "order_by_clause",
          "named": true
        },
        {
          "type": "select_clause",
          "named": true
        },
        {
          "type": "where_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "range_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "raw_string_literal",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "raw_string_content",
          "named": true
        },
        {
          "type": "raw_string_end",
          "named": true
        },
        {
          "type": "raw_string_start",
          "named": true
        }
      ]
    }
  },
  {
    "type": "record_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "declaration_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "base_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "parameter_list",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "type_parameter_constraints_clause",
          "named": true
        },
        {
          "type": "type_parameter_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "recursive_pattern",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "parenthesized_variable_designation",
          "named": true
        },
        {
          "type": "pattern",
          "named": true
        },
        {
          "type": "positional_pattern_clause",
          "named": true
        },
        {
          "type": "property_pattern_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "ref_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "ref_type",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "reftype_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "refvalue_expression",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      },
      "value": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "relational_pattern",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "return_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "scoped_type",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "alias_qualified_name",
            "named": true
          },
          {
            "type": "generic_name",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "qualified_name",
            "named": true
          },
          {
            "type": "ref_type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "select_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "sizeof_expression",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "stackalloc_expression",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "array_type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "initializer_expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "string_literal",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "escape_sequence",
          "named": true
        },
        {
          "type": "string_literal_content",
          "named": true
        },
        {
          "type": "string_literal_encoding",
          "named": true
        }
      ]
    }
  },
  {
    "type": "struct_declaration",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "declaration_list",
            "named": true
          }
        ]
      },
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "base_list",
          "named": true
        },
        {
          "type": "modifier",
          "named": true
        },
        {
          "type": "parameter_list",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        },
        {
          "type": "type_parameter_constraints_clause",
          "named": true
        },
        {
          "type": "type_parameter_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "subpattern",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "pattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "switch_body",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "switch_section",
          "named": true
        }
      ]
    }
  },
  {
    "type": "switch_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "switch_expression_arm",
          "named": true
        }
      ]
    }
  },
  {
    "type": "switch_expression_arm",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "pattern",
          "named": true
        },
        {
          "type": "when_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "switch_section",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "pattern",
          "named": true
        },
        {
          "type": "statement",
          "named": true
        },
        {
          "type": "when_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "switch_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "switch_body",
            "named": true
          }
        ]
      },
      "value": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          },
          {
            "type": "tuple_expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "throw_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "throw_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "try_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "block",
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
          "type": "catch_clause",
          "named": true
        },
        {
          "type": "finally_clause",
          "named": true
        }
      ]
    }
  },
  {
    "type": "tuple_element",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      },
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "tuple_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "argument",
          "named": true
        }
      ]
    }
  },
  {
    "type": "tuple_pattern",
    "named": true,
    "fields": {
      "name": {
        "multiple": true,
        "required": false,
        "types": [
          {
            "type": "identifier",
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
          "type": "discard",
          "named": true
        },
        {
          "type": "tuple_pattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "tuple_type",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "tuple_element",
          "named": true
        }
      ]
    }
  },
  {
    "type": "type_argument_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": false,
      "types": [
        {
          "type": "type",
          "named": true
        }
      ]
    }
  },
  {
    "type": "type_parameter",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "identifier",
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
          "type": "attribute_list",
          "named": true
        },
        {
          "type": "preproc_if_in_attribute_list",
          "named": true
        }
      ]
    }
  },
  {
    "type": "type_parameter_constraint",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "constructor_constraint",
          "named": true
        }
      ]
    }
  },
  {
    "type": "type_parameter_constraints_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "identifier",
          "named": true
        },
        {
          "type": "type_parameter_constraint",
          "named": true
        }
      ]
    }
  },
  {
    "type": "type_parameter_list",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "type_parameter",
          "named": true
        }
      ]
    }
  },
  {
    "type": "type_pattern",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "typeof_expression",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "unary_expression",
    "named": true,
    "fields": {
      "argument": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "binary_expression",
            "named": true
          },
          {
            "type": "boolean_literal",
            "named": true
          },
          {
            "type": "character_literal",
            "named": true
          },
          {
            "type": "identifier",
            "named": true
          },
          {
            "type": "integer_literal",
            "named": true
          },
          {
            "type": "parenthesized_expression",
            "named": true
          },
          {
            "type": "unary_expression",
            "named": true
          }
        ]
      },
      "operator": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "!",
            "named": false
          }
        ]
      }
    }
  },
  {
    "type": "unsafe_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "block",
          "named": true
        }
      ]
    }
  },
  {
    "type": "using_directive",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "type",
          "named": true
        }
      ]
    }
  },
  {
    "type": "using_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "statement",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "variable_declaration",
          "named": true
        }
      ]
    }
  },
  {
    "type": "var_pattern",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "discard",
          "named": true
        },
        {
          "type": "parenthesized_variable_designation",
          "named": true
        }
      ]
    }
  },
  {
    "type": "variable_declaration",
    "named": true,
    "fields": {
      "type": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "type",
            "named": true
          }
        ]
      }
    },
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "variable_declarator",
          "named": true
        }
      ]
    }
  },
  {
    "type": "variable_declarator",
    "named": true,
    "fields": {
      "name": {
        "multiple": false,
        "required": false,
        "types": [
          {
            "type": "identifier",
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
          "type": "bracketed_argument_list",
          "named": true
        },
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "tuple_pattern",
          "named": true
        }
      ]
    }
  },
  {
    "type": "when_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "where_clause",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "while_statement",
    "named": true,
    "fields": {
      "body": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "statement",
            "named": true
          }
        ]
      },
      "condition": {
        "multiple": false,
        "required": true,
        "types": [
          {
            "type": "expression",
            "named": true
          }
        ]
      }
    }
  },
  {
    "type": "with_expression",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "with_initializer",
          "named": true
        }
      ]
    }
  },
  {
    "type": "with_initializer",
    "named": true,
    "fields": {},
    "children": {
      "multiple": true,
      "required": true,
      "types": [
        {
          "type": "expression",
          "named": true
        },
        {
          "type": "identifier",
          "named": true
        }
      ]
    }
  },
  {
    "type": "yield_statement",
    "named": true,
    "fields": {},
    "children": {
      "multiple": false,
      "required": false,
      "types": [
        {
          "type": "expression",
          "named": true
        }
      ]
    }
  },
  {
    "type": "!",
    "named": false
  },
  {
    "type": "!=",
    "named": false
  },
  {
    "type": "\"",
    "named": false
  },
  {
    "type": "#define",
    "named": false
  },
  {
    "type": "#elif",
    "named": false
  },
  {
    "type": "#else",
    "named": false
  },
  {
    "type": "#endif",
    "named": false
  },
  {
    "type": "#endregion",
    "named": false
  },
  {
    "type": "#error",
    "named": false
  },
  {
    "type": "#if",
    "named": false
  },
  {
    "type": "#line",
    "named": false
  },
  {
    "type": "#nullable",
    "named": false
  },
  {
    "type": "#pragma",
    "named": false
  },
  {
    "type": "#region",
    "named": false
  },
  {
    "type": "#undef",
    "named": false
  },
  {
    "type": "#warning",
    "named": false
  },
  {
    "type": "%",
    "named": false
  },
  {
    "type": "%=",
    "named": false
  },
  {
    "type": "&",
    "named": false
  },
  {
    "type": "&&",
    "named": false
  },
  {
    "type": "&=",
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
    "type": "*",
    "named": false
  },
  {
    "type": "*=",
    "named": false
  },
  {
    "type": "+",
    "named": false
  },
  {
    "type": "++",
    "named": false
  },
  {
    "type": "+=",
    "named": false
  },
  {
    "type": ",",
    "named": false
  },
  {
    "type": "-",
    "named": false
  },
  {
    "type": "--",
    "named": false
  },
  {
    "type": "-=",
    "named": false
  },
  {
    "type": "->",
    "named": false
  },
  {
    "type": ".",
    "named": false
  },
  {
    "type": "..",
    "named": false
  },
  {
    "type": "/",
    "named": false
  },
  {
    "type": "/=",
    "named": false
  },
  {
    "type": ":",
    "named": false
  },
  {
    "type": "::",
    "named": false
  },
  {
    "type": ";",
    "named": false
  },
  {
    "type": "<",
    "named": false
  },
  {
    "type": "<<",
    "named": false
  },
  {
    "type": "<<=",
    "named": false
  },
  {
    "type": "<=",
    "named": false
  },
  {
    "type": "=",
    "named": false
  },
  {
    "type": "==",
    "named": false
  },
  {
    "type": "=>",
    "named": false
  },
  {
    "type": ">",
    "named": false
  },
  {
    "type": ">=",
    "named": false
  },
  {
    "type": ">>",
    "named": false
  },
  {
    "type": ">>=",
    "named": false
  },
  {
    "type": ">>>",
    "named": false
  },
  {
    "type": ">>>=",
    "named": false
  },
  {
    "type": "?",
    "named": false
  },
  {
    "type": "??",
    "named": false
  },
  {
    "type": "??=",
    "named": false
  },
  {
    "type": "Cdecl",
    "named": false
  },
  {
    "type": "Fastcall",
    "named": false
  },
  {
    "type": "Stdcall",
    "named": false
  },
  {
    "type": "Thiscall",
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
    "type": "^",
    "named": false
  },
  {
    "type": "^=",
    "named": false
  },
  {
    "type": "__makeref",
    "named": false
  },
  {
    "type": "__reftype",
    "named": false
  },
  {
    "type": "__refvalue",
    "named": false
  },
  {
    "type": "abstract",
    "named": false
  },
  {
    "type": "add",
    "named": false
  },
  {
    "type": "alias",
    "named": false
  },
  {
    "type": "and",
    "named": false
  },
  {
    "type": "annotations",
    "named": false
  },
  {
    "type": "as",
    "named": false
  },
  {
    "type": "ascending",
    "named": false
  },
  {
    "type": "assembly",
    "named": false
  },
  {
    "type": "async",
    "named": false
  },
  {
    "type": "await",
    "named": false
  },
  {
    "type": "base",
    "named": false
  },
  {
    "type": "break",
    "named": false
  },
  {
    "type": "by",
    "named": false
  },
  {
    "type": "case",
    "named": false
  },
  {
    "type": "catch",
    "named": false
  },
  {
    "type": "character_literal_content",
    "named": true
  },
  {
    "type": "checked",
    "named": false
  },
  {
    "type": "checksum",
    "named": false
  },
  {
    "type": "class",
    "named": false
  },
  {
    "type": "comment",
    "named": true,
    "extra": true
  },
  {
    "type": "const",
    "named": false
  },
  {
    "type": "continue",
    "named": false
  },
  {
    "type": "default",
    "named": false
  },
  {
    "type": "delegate",
    "named": false
  },
  {
    "type": "descending",
    "named": false
  },
  {
    "type": "disable",
    "named": false
  },
  {
    "type": "discard",
    "named": true
  },
  {
    "type": "do",
    "named": false
  },
  {
    "type": "else",
    "named": false
  },
  {
    "type": "enable",
    "named": false
  },
  {
    "type": "enum",
    "named": false
  },
  {
    "type": "equals",
    "named": false
  },
  {
    "type": "escape_sequence",
    "named": true
  },
  {
    "type": "event",
    "named": false
  },
  {
    "type": "explicit",
    "named": false
  },
  {
    "type": "extern",
    "named": false
  },
  {
    "type": "false",
    "named": false
  },
  {
    "type": "field",
    "named": false
  },
  {
    "type": "file",
    "named": false
  },
  {
    "type": "finally",
    "named": false
  },
  {
    "type": "fixed",
    "named": false
  },
  {
    "type": "for",
    "named": false
  },
  {
    "type": "foreach",
    "named": false
  },
  {
    "type": "from",
    "named": false
  },
  {
    "type": "get",
    "named": false
  },
  {
    "type": "global",
    "named": false
  },
  {
    "type": "goto",
    "named": false
  },
  {
    "type": "group",
    "named": false
  },
  {
    "type": "hidden",
    "named": false
  },
  {
    "type": "if",
    "named": false
  },
  {
    "type": "implicit",
    "named": false
  },
  {
    "type": "in",
    "named": false
  },
  {
    "type": "init",
    "named": false
  },
  {
    "type": "integer_literal",
    "named": true
  },
  {
    "type": "interface",
    "named": false
  },
  {
    "type": "internal",
    "named": false
  },
  {
    "type": "interpolation_brace",
    "named": true
  },
  {
    "type": "interpolation_quote",
    "named": true
  },
  {
    "type": "interpolation_start",
    "named": true
  },
  {
    "type": "into",
    "named": false
  },
  {
    "type": "is",
    "named": false
  },
  {
    "type": "join",
    "named": false
  },
  {
    "type": "let",
    "named": false
  },
  {
    "type": "lock",
    "named": false
  },
  {
    "type": "managed",
    "named": false
  },
  {
    "type": "method",
    "named": false
  },
  {
    "type": "module",
    "named": false
  },
  {
    "type": "namespace",
    "named": false
  },
  {
    "type": "new",
    "named": false
  },
  {
    "type": "not",
    "named": false
  },
  {
    "type": "notnull",
    "named": false
  },
  {
    "type": "null_literal",
    "named": true
  },
  {
    "type": "on",
    "named": false
  },
  {
    "type": "operator",
    "named": false
  },
  {
    "type": "or",
    "named": false
  },
  {
    "type": "orderby",
    "named": false
  },
  {
    "type": "out",
    "named": false
  },
  {
    "type": "override",
    "named": false
  },
  {
    "type": "param",
    "named": false
  },
  {
    "type": "params",
    "named": false
  },
  {
    "type": "partial",
    "named": false
  },
  {
    "type": "predefined_type",
    "named": true
  },
  {
    "type": "preproc_arg",
    "named": true
  },
  {
    "type": "private",
    "named": false
  },
  {
    "type": "property",
    "named": false
  },
  {
    "type": "protected",
    "named": false
  },
  {
    "type": "public",
    "named": false
  },
  {
    "type": "raw_string_content",
    "named": true
  },
  {
    "type": "raw_string_end",
    "named": true
  },
  {
    "type": "raw_string_start",
    "named": true
  },
  {
    "type": "readonly",
    "named": false
  },
  {
    "type": "real_literal",
    "named": true
  },
  {
    "type": "record",
    "named": false
  },
  {
    "type": "ref",
    "named": false
  },
  {
    "type": "remove",
    "named": false
  },
  {
    "type": "required",
    "named": false
  },
  {
    "type": "restore",
    "named": false
  },
  {
    "type": "return",
    "named": false
  },
  {
    "type": "scoped",
    "named": false
  },
  {
    "type": "sealed",
    "named": false
  },
  {
    "type": "select",
    "named": false
  },
  {
    "type": "set",
    "named": false
  },
  {
    "type": "shebang_directive",
    "named": true
  },
  {
    "type": "sizeof",
    "named": false
  },
  {
    "type": "stackalloc",
    "named": false
  },
  {
    "type": "static",
    "named": false
  },
  {
    "type": "string_content",
    "named": true
  },
  {
    "type": "string_literal_content",
    "named": true
  },
  {
    "type": "string_literal_encoding",
    "named": true
  },
  {
    "type": "struct",
    "named": false
  },
  {
    "type": "switch",
    "named": false
  },
  {
    "type": "this",
    "named": false
  },
  {
    "type": "throw",
    "named": false
  },
  {
    "type": "true",
    "named": false
  },
  {
    "type": "try",
    "named": false
  },
  {
    "type": "type",
    "named": false
  },
  {
    "type": "typeof",
    "named": false
  },
  {
    "type": "typevar",
    "named": false
  },
  {
    "type": "unchecked",
    "named": false
  },
  {
    "type": "unmanaged",
    "named": false
  },
  {
    "type": "unsafe",
    "named": false
  },
  {
    "type": "using",
    "named": false
  },
  {
    "type": "var",
    "named": false
  },
  {
    "type": "verbatim_string_literal",
    "named": true
  },
  {
    "type": "virtual",
    "named": false
  },
  {
    "type": "volatile",
    "named": false
  },
  {
    "type": "warning",
    "named": false
  },
  {
    "type": "warnings",
    "named": false
  },
  {
    "type": "when",
    "named": false
  },
  {
    "type": "where",
    "named": false
  },
  {
    "type": "while",
    "named": false
  },
  {
    "type": "with",
    "named": false
  },
  {
    "type": "yield",
    "named": false
  },
  {
    "type": "{",
    "named": false
  },
  {
    "type": "|",
    "named": false
  },
  {
    "type": "|=",
    "named": false
  },
  {
    "type": "||",
    "named": false
  },
  {
    "type": "}",
    "named": false
  },
  {
    "type": "~",
    "named": false
  }
]
```

## File: `src/scanner.c`
```c
#include "tree_sitter/alloc.h"
#include "tree_sitter/array.h"
#include "tree_sitter/parser.h"

#include <wctype.h>

enum TokenType {
    OPT_SEMI,
    INTERPOLATION_REGULAR_START,
    INTERPOLATION_VERBATIM_START,
    INTERPOLATION_RAW_START,
    INTERPOLATION_START_QUOTE,
    INTERPOLATION_END_QUOTE,
    INTERPOLATION_OPEN_BRACE,
    INTERPOLATION_CLOSE_BRACE,
    INTERPOLATION_STRING_CONTENT,
    RAW_STRING_START,
    RAW_STRING_END,
    RAW_STRING_CONTENT,
};

typedef enum {
    REGULAR = 1 << 0,
    VERBATIM = 1 << 1,
    RAW = 1 << 2,
} StringType;

typedef struct {
    uint8_t dollar_count;
    uint8_t open_brace_count;
    uint8_t quote_count;
    StringType string_type;
} Interpolation;

static inline bool is_regular(Interpolation *interpolation) { return interpolation->string_type & REGULAR; }

static inline bool is_verbatim(Interpolation *interpolation) { return interpolation->string_type & VERBATIM; }

static inline bool is_raw(Interpolation *interpolation) { return interpolation->string_type & RAW; }

typedef struct {
    uint8_t quote_count;
    Array(Interpolation) interpolation_stack;
} Scanner;

static inline void advance(TSLexer *lexer) { lexer->advance(lexer, false); }

static inline void skip(TSLexer *lexer) { lexer->advance(lexer, true); }

void *tree_sitter_c_sharp_external_scanner_create() {
    Scanner *scanner = ts_calloc(1, sizeof(Scanner));
    array_init(&scanner->interpolation_stack);
    return scanner;
}

void tree_sitter_c_sharp_external_scanner_destroy(void *payload) {
    Scanner *scanner = (Scanner *)payload;
    array_delete(&scanner->interpolation_stack);
    ts_free(scanner);
}

unsigned tree_sitter_c_sharp_external_scanner_serialize(void *payload, char *buffer) {
    Scanner *scanner = (Scanner *)payload;

    if (scanner->interpolation_stack.size * 4 + 2 > TREE_SITTER_SERIALIZATION_BUFFER_SIZE) {
        return 0;
    }

    unsigned size = 0;

    buffer[size++] = (char)scanner->quote_count;
    buffer[size++] = (char)scanner->interpolation_stack.size;

    for (unsigned i = 0; i < scanner->interpolation_stack.size; i++) {
        Interpolation interpolation = scanner->interpolation_stack.contents[i];
        buffer[size++] = (char)interpolation.dollar_count;
        buffer[size++] = (char)interpolation.open_brace_count;
        buffer[size++] = (char)interpolation.quote_count;
        buffer[size++] = (char)interpolation.string_type;
    }

    return size;
}

void tree_sitter_c_sharp_external_scanner_deserialize(void *payload, const char *buffer, unsigned length) {
    Scanner *scanner = (Scanner *)payload;

    scanner->quote_count = 0;
    array_clear(&scanner->interpolation_stack);
    unsigned size = 0;

    if (length > 0) {
        scanner->quote_count = (unsigned char)buffer[size++];
        scanner->interpolation_stack.size = (unsigned char)buffer[size++];
        array_reserve(&scanner->interpolation_stack, scanner->interpolation_stack.size);

        for (unsigned i = 0; i < scanner->interpolation_stack.size; i++) {
            Interpolation interpolation = {0};
            interpolation.dollar_count = buffer[size++];
            interpolation.open_brace_count = buffer[size++];
            interpolation.quote_count = buffer[size++];
            interpolation.string_type = (unsigned char)buffer[size++];
            scanner->interpolation_stack.contents[i] = interpolation;
        }
    }

    assert(size == length);
}

bool tree_sitter_c_sharp_external_scanner_scan(void *payload, TSLexer *lexer, const bool *valid_symbols) {
    Scanner *scanner = (Scanner *)payload;

    uint8_t brace_advanced = 0;
    uint8_t quote_count = 0;
    bool did_advance = false;

    // error recovery, gives better trees this way
    if (valid_symbols[OPT_SEMI] && valid_symbols[INTERPOLATION_REGULAR_START]) {
        return false;
    }

    if (valid_symbols[OPT_SEMI]) {
        lexer->result_symbol = OPT_SEMI;
        if (lexer->lookahead == ';') {
            advance(lexer);
        }
        return true;
    }

    if (valid_symbols[RAW_STRING_START]) {
        while (iswspace(lexer->lookahead)) {
            skip(lexer);
        }

        if (lexer->lookahead == '"') {
            while (lexer->lookahead == '"') {
                advance(lexer);
                quote_count++;
            }

            if (quote_count >= 3) {
                lexer->result_symbol = RAW_STRING_START;
                scanner->quote_count = quote_count;
                return true;
            }
        }
    }

    if (valid_symbols[RAW_STRING_END] && lexer->lookahead == '"') {
        while (lexer->lookahead == '"') {
            advance(lexer);
            quote_count++;
        }

        if (quote_count == scanner->quote_count) {
            lexer->result_symbol = RAW_STRING_END;
            scanner->quote_count = 0;
            return true;
        }

        did_advance = quote_count > 0;
    }

    if (valid_symbols[RAW_STRING_CONTENT]) {
        while (lexer->lookahead) {
            if (lexer->lookahead == '"') {
                lexer->mark_end(lexer);
                quote_count = 0;

                while (lexer->lookahead == '"') {
                    advance(lexer);
                    quote_count++;
                }

                if (quote_count == scanner->quote_count) {
                    lexer->result_symbol = RAW_STRING_CONTENT;
                    return true;
                }
            }
            advance(lexer);
            did_advance = true;
        }
        lexer->mark_end(lexer);
        lexer->result_symbol = RAW_STRING_CONTENT;
        return true;
    }

    if (valid_symbols[INTERPOLATION_REGULAR_START] || valid_symbols[INTERPOLATION_VERBATIM_START] ||
        valid_symbols[INTERPOLATION_RAW_START]) {
        while (iswspace(lexer->lookahead)) {
            skip(lexer);
        }

        uint8_t dollar_advanced = 0;

        bool is_verbatim = false;

        if (lexer->lookahead == '@') {
            is_verbatim = true;
            advance(lexer);
        }

        while (lexer->lookahead == '$' && quote_count == 0) {
            advance(lexer);
            dollar_advanced++;
        }

        if (dollar_advanced > 0 && (lexer->lookahead == '"' || lexer->lookahead == '@')) {
            lexer->result_symbol = INTERPOLATION_REGULAR_START;
            Interpolation interpolation = {
                .dollar_count = dollar_advanced,
                .open_brace_count = 0,
                .quote_count = 0,
                .string_type = 0,
            };

            if (is_verbatim || lexer->lookahead == '@') {
                if (lexer->lookahead == '@') {
                    advance(lexer);
                    is_verbatim = true;
                }
                lexer->result_symbol = INTERPOLATION_VERBATIM_START;
                interpolation.string_type = VERBATIM;
            }

            lexer->mark_end(lexer);
            advance(lexer);

            if (lexer->lookahead == '"' && !is_verbatim) {
                advance(lexer);
                if (lexer->lookahead == '"') {
                    lexer->result_symbol = INTERPOLATION_RAW_START;
                    interpolation.string_type |= RAW;
                    array_push(&scanner->interpolation_stack, interpolation);
                }
                // If we find 1 or 3 quotes, we push an interpolation.
                // If there's only two quotes, that's just an empty string
            } else {
                interpolation.string_type |= REGULAR;
                array_push(&scanner->interpolation_stack, interpolation);
            }

            return true;
        }
    }

    if (valid_symbols[INTERPOLATION_START_QUOTE] && scanner->interpolation_stack.size > 0) {
        Interpolation *current_interpolation = array_back(&scanner->interpolation_stack);

        if (is_verbatim(current_interpolation) || is_regular(current_interpolation)) {
            if (lexer->lookahead == '"') {
                advance(lexer);
                current_interpolation->quote_count++;
            }
        } else {
            while (lexer->lookahead == '"') {
                advance(lexer);
                current_interpolation->quote_count++;
            }
        }

        lexer->result_symbol = INTERPOLATION_START_QUOTE;
        return current_interpolation->quote_count > 0;
    }

    if (valid_symbols[INTERPOLATION_END_QUOTE] && scanner->interpolation_stack.size > 0) {
        Interpolation *current_interpolation = array_back(&scanner->interpolation_stack);

        while (lexer->lookahead == '"') {
            advance(lexer);
            quote_count++;
        }

        if (quote_count == current_interpolation->quote_count) {
            lexer->result_symbol = INTERPOLATION_END_QUOTE;
            array_pop(&scanner->interpolation_stack);
            return true;
        }

        did_advance = quote_count > 0;
    }

    if (valid_symbols[INTERPOLATION_OPEN_BRACE] && scanner->interpolation_stack.size > 0) {
        Interpolation *current_interpolation = array_back(&scanner->interpolation_stack);

        while (lexer->lookahead == '{' && brace_advanced < current_interpolation->dollar_count) {
            advance(lexer);
            brace_advanced++;
        }

        if (brace_advanced > 0 && brace_advanced == current_interpolation->dollar_count &&
            (brace_advanced == 0 || lexer->lookahead != '{')) {
            current_interpolation->open_brace_count = brace_advanced;
            lexer->result_symbol = INTERPOLATION_OPEN_BRACE;
            return true;
        }
    }

    if (valid_symbols[INTERPOLATION_CLOSE_BRACE] && scanner->interpolation_stack.size > 0) {
        uint8_t brace_advanced = 0;
        Interpolation *current_interpolation = array_back(&scanner->interpolation_stack);

        while (iswspace(lexer->lookahead)) {
            advance(lexer);
        }

        while (lexer->lookahead == '}') {
            advance(lexer);
            brace_advanced++;

            if (brace_advanced == current_interpolation->open_brace_count) {
                current_interpolation->open_brace_count = 0;
                lexer->result_symbol = INTERPOLATION_CLOSE_BRACE;
                return true;
            }
        }

        return false;
    }

    if (valid_symbols[INTERPOLATION_STRING_CONTENT] && scanner->interpolation_stack.size > 0) {
        lexer->result_symbol = INTERPOLATION_STRING_CONTENT;
        Interpolation *current_interpolation = array_back(&scanner->interpolation_stack);

        while (lexer->lookahead) {
            // top-down approach, first see if it's raw
            if (is_raw(current_interpolation)) {
                if (lexer->lookahead == '"') {
                    lexer->mark_end(lexer);
                    advance(lexer);
                    if (lexer->lookahead == '"') {
                        advance(lexer);
                        uint8_t quote_advanced = 2;
                        while (lexer->lookahead == '"') {
                            quote_advanced++;
                            advance(lexer);
                        }
                        if (quote_advanced == current_interpolation->quote_count) {
                            return did_advance;
                        }
                    }
                }

                if (lexer->lookahead == '{') {
                    lexer->mark_end(lexer);

                    while (lexer->lookahead == '{' && brace_advanced < current_interpolation->open_brace_count) {
                        advance(lexer);
                        brace_advanced++;
                    }

                    if (brace_advanced == current_interpolation->open_brace_count &&
                        (brace_advanced == 0 || lexer->lookahead != '{')) {
                        return did_advance;
                    }
                }
            }

            // then verbatim, since it could be verbatim + raw, but run the raw branch first
            else if (is_verbatim(current_interpolation)) {
                if (lexer->lookahead == '"') {
                    lexer->mark_end(lexer);
                    advance(lexer);
                    if (lexer->lookahead == '"') {
                        advance(lexer);
                        continue;
                    }
                    return did_advance;
                }

                if (lexer->lookahead == '{') {
                    lexer->mark_end(lexer);

                    while (lexer->lookahead == '{' && brace_advanced < current_interpolation->open_brace_count) {
                        advance(lexer);
                        brace_advanced++;
                    }

                    if (brace_advanced == current_interpolation->open_brace_count &&
                        (brace_advanced == 0 || lexer->lookahead != '{')) {
                        return did_advance;
                    }
                }
            }

            // finally regular
            else if (is_regular(current_interpolation)) {
                if (lexer->lookahead == '\\' || lexer->lookahead == '\n' || lexer->lookahead == '"') {
                    lexer->mark_end(lexer);
                    return did_advance;
                }

                if (lexer->lookahead == '{') {
                    lexer->mark_end(lexer);

                    while (lexer->lookahead == '{' && brace_advanced < current_interpolation->open_brace_count) {
                        advance(lexer);
                        brace_advanced++;
                    }

                    if (brace_advanced == current_interpolation->open_brace_count &&
                        (brace_advanced == 0 || lexer->lookahead != '{')) { // if we're in a brace we're not allowed to
                                                                            // collect more than the open_brace_count
                        return did_advance;
                    }
                }
            }

            if (lexer->lookahead != '{') {
                brace_advanced = 0;
            }
            advance(lexer);
            did_advance = true;
        }

        lexer->mark_end(lexer);
        return did_advance;
    }

    return false;
}
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
#define array_reserve(self, new_capacity)        \
  ((self)->contents = _array__reserve(           \
    (void *)(self)->contents, &(self)->capacity, \
    array_elem_size(self), new_capacity)         \
  )

/// Free any memory allocated for this array. Note that this does not free any
/// memory allocated for the array's contents.
#define array_delete(self) _array__delete((self), (void *)(self)->contents, sizeof(*self))

/// Push a new `element` onto the end of the array.
#define array_push(self, element)                                 \
  do {                                                            \
    (self)->contents = _array__grow(                              \
      (void *)(self)->contents, (self)->size, &(self)->capacity,  \
      1, array_elem_size(self)                                    \
    );                                                            \
   (self)->contents[(self)->size++] = (element);                  \
  } while(0)

/// Increase the array's size by `count` elements.
/// New elements are zero-initialized.
#define array_grow_by(self, count)                                               \
  do {                                                                           \
    if ((count) == 0) break;                                                     \
    (self)->contents = _array__grow(                                             \
      (self)->contents, (self)->size, &(self)->capacity,                         \
      count, array_elem_size(self)                                               \
    );                                                                           \
    memset((self)->contents + (self)->size, 0, (count) * array_elem_size(self)); \
    (self)->size += (count);                                                     \
  } while (0)

/// Append all elements from one array to the end of another.
#define array_push_all(self, other) \
  array_extend((self), (other)->size, (other)->contents)

/// Append `count` elements to the end of the array, reading their values from the
/// `contents` pointer.
#define array_extend(self, count, other_contents)                 \
  (self)->contents = _array__splice(                              \
    (void*)(self)->contents, &(self)->size, &(self)->capacity,    \
    array_elem_size(self), (self)->size, 0, count, other_contents \
  )

/// Remove `old_count` elements from the array starting at the given `index`. At
/// the same index, insert `new_count` new elements, reading their values from the
/// `new_contents` pointer.
#define array_splice(self, _index, old_count, new_count, new_contents) \
  (self)->contents = _array__splice(                                   \
    (void *)(self)->contents, &(self)->size, &(self)->capacity,        \
    array_elem_size(self), _index, old_count, new_count, new_contents  \
  )

/// Insert one `element` into the array at the given `index`.
#define array_insert(self, _index, element)                     \
  (self)->contents = _array__splice(                            \
    (void *)(self)->contents, &(self)->size, &(self)->capacity, \
    array_elem_size(self), _index, 0, 1, &(element)             \
  )

/// Remove one element from the array at the given `index`.
#define array_erase(self, _index) \
  _array__erase((void *)(self)->contents, &(self)->size, array_elem_size(self), _index)

/// Pop the last element off the array, returning the element by value.
#define array_pop(self) ((self)->contents[--(self)->size])

/// Assign the contents of one array to another, reallocating if necessary.
#define array_assign(self, other)                                   \
  (self)->contents = _array__assign(                                \
    (void *)(self)->contents, &(self)->size, &(self)->capacity,     \
    (const void *)(other)->contents, (other)->size, array_elem_size(self) \
  )

/// Swap one array with another
#define array_swap(self, other)                                     \
  do {                                                              \
    struct Swap swapped_contents = _array__swap(                    \
      (void *)(self)->contents, &(self)->size, &(self)->capacity,   \
      (void *)(other)->contents, &(other)->size, &(other)->capacity \
    );                                                              \
    (self)->contents = swapped_contents.self_contents;              \
    (other)->contents = swapped_contents.other_contents;            \
  } while (0)

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

// Pointers to individual `Array` fields (rather than the entire `Array` itself)
// are passed to the various `_array__*` functions below to address strict aliasing
// violations that arises when the _entire_ `Array` struct is passed as `Array(void)*`.
//
// The `Array` type itself was not altered as a solution in order to avoid breakage
// with existing consumers (in particular, parsers with external scanners).

/// This is not what you're looking for, see `array_delete`.
static inline void _array__delete(void *self, void *contents, size_t self_size) {
  if (contents) ts_free(contents);
  if (self) memset(self, 0, self_size);
}

/// This is not what you're looking for, see `array_erase`.
static inline void _array__erase(void* self_contents, uint32_t *size,
                                size_t element_size, uint32_t index) {
  assert(index < *size);
  char *contents = (char *)self_contents;
  memmove(contents + index * element_size, contents + (index + 1) * element_size,
          (*size - index - 1) * element_size);
  (*size)--;
}

/// This is not what you're looking for, see `array_reserve`.
static inline void *_array__reserve(void *contents, uint32_t *capacity,
                                  size_t element_size, uint32_t new_capacity) {
  void *new_contents = contents;
  if (new_capacity > *capacity) {
    if (contents) {
      new_contents = ts_realloc(contents, new_capacity * element_size);
    } else {
      new_contents = ts_malloc(new_capacity * element_size);
    }
    *capacity = new_capacity;
  }
  return new_contents;
}

/// This is not what you're looking for, see `array_assign`.
static inline void *_array__assign(void* self_contents, uint32_t *self_size, uint32_t *self_capacity,
                                 const void *other_contents, uint32_t other_size, size_t element_size) {
  void *new_contents = _array__reserve(self_contents, self_capacity, element_size, other_size);
  *self_size = other_size;
  memcpy(new_contents, other_contents, *self_size * element_size);
  return new_contents;
}

struct Swap {
  void *self_contents;
  void *other_contents;
};

/// This is not what you're looking for, see `array_swap`.
// static inline void _array__swap(Array *self, Array *other) {
static inline struct Swap _array__swap(void *self_contents, uint32_t *self_size, uint32_t *self_capacity,
                               void *other_contents, uint32_t *other_size, uint32_t *other_capacity) {
  void *new_self_contents = other_contents;
  uint32_t new_self_size = *other_size;
  uint32_t new_self_capacity = *other_capacity;

  void *new_other_contents = self_contents;
  *other_size = *self_size;
  *other_capacity = *self_capacity;

  *self_size = new_self_size;
  *self_capacity = new_self_capacity;

  struct Swap out = {
    .self_contents = new_self_contents,
    .other_contents = new_other_contents,
  };
  return out;
}

/// This is not what you're looking for, see `array_push` or `array_grow_by`.
static inline void *_array__grow(void *contents, uint32_t size, uint32_t *capacity,
                               uint32_t count, size_t element_size) {
  void *new_contents = contents;
  uint32_t new_size = size + count;
  if (new_size > *capacity) {
    uint32_t new_capacity = *capacity * 2;
    if (new_capacity < 8) new_capacity = 8;
    if (new_capacity < new_size) new_capacity = new_size;
    new_contents = _array__reserve(contents, capacity, element_size, new_capacity);
  }
  return new_contents;
}

/// This is not what you're looking for, see `array_splice`.
static inline void *_array__splice(void *self_contents, uint32_t *size, uint32_t *capacity,
                                 size_t element_size,
                                 uint32_t index, uint32_t old_count,
                                 uint32_t new_count, const void *elements) {
  uint32_t new_size = *size + new_count - old_count;
  uint32_t old_end = index + old_count;
  uint32_t new_end = index + new_count;
  assert(old_end <= *size);

  void *new_contents = _array__reserve(self_contents, capacity, element_size, new_size);

  char *contents = (char *)new_contents;
  if (*size > old_end) {
    memmove(
      contents + new_end * element_size,
      contents + old_end * element_size,
      (*size - old_end) * element_size
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
  *size += new_count - old_count;

  return new_contents;
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

## File: `test/corpus/attributes.txt`
```
================================================================================
Attribute targets
================================================================================

[assembly: Single]
[module: A, C()]

--------------------------------------------------------------------------------

(compilation_unit
  (global_attribute
    (attribute
      name: (identifier)))
  (global_attribute
    (attribute
      name: (identifier))
    (attribute
      name: (identifier)
      (attribute_argument_list))))


================================================================================
Attributes
================================================================================

[A(B.C)]
class D {}

[NS.A(B.C)]
class D {}

[One][Two]
[Three]
class A { }

[A,B()][C]
struct A { }

class Zzz {
  [A,B()][C]
  public int Z;
}

class Methods {
  [ValidatedContract]
  int Method1() { return 0; }

  [method: ValidatedContract]
  int Method2() { return 0; }

  [return: ValidatedContract]
  int Method3() { return 0; }
}

[Single]
enum A { B, C }

class Zzz {
  [A,B()][C]
  public event EventHandler SomeEvent { add { } remove { } }
}

class Class<[A, B][C()]T1> {
  void Method<[E] [F, G(1)] T2>() {
  }
}

class Zzz {
  public event EventHandler SomeEvent {
    [A,B()][C] add { }
    [A,B()][C] remove { }
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    (attribute_list
      (attribute
        name: (identifier)
        (attribute_argument_list
          (attribute_argument
            (member_access_expression
              expression: (identifier)
              name: (identifier))))))
    name: (identifier)
    body: (declaration_list))
  (class_declaration
    (attribute_list
      (attribute
        name: (qualified_name
          qualifier: (identifier)
          name: (identifier))
        (attribute_argument_list
          (attribute_argument
            (member_access_expression
              expression: (identifier)
              name: (identifier))))))
    name: (identifier)
    body: (declaration_list))
  (class_declaration
    (attribute_list
      (attribute
        name: (identifier)))
    (attribute_list
      (attribute
        name: (identifier)))
    (attribute_list
      (attribute
        name: (identifier)))
    name: (identifier)
    body: (declaration_list))
  (struct_declaration
    (attribute_list
      (attribute
        name: (identifier))
      (attribute
        name: (identifier)
        (attribute_argument_list)))
    (attribute_list
      (attribute
        name: (identifier)))
    name: (identifier)
    body: (declaration_list))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (field_declaration
        (attribute_list
          (attribute
            name: (identifier))
          (attribute
            name: (identifier)
            (attribute_argument_list)))
        (attribute_list
          (attribute
            name: (identifier)))
        (modifier)
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        (attribute_list
          (attribute
            name: (identifier)))
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement
            (integer_literal))))
      (method_declaration
        (attribute_list
          (attribute_target_specifier)
          (attribute
            name: (identifier)))
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement
            (integer_literal))))
      (method_declaration
        (attribute_list
          (attribute_target_specifier)
          (attribute
            name: (identifier)))
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement
            (integer_literal))))))
  (enum_declaration
    (attribute_list
      (attribute
        name: (identifier)))
    name: (identifier)
    body: (enum_member_declaration_list
      (enum_member_declaration
        name: (identifier))
      (enum_member_declaration
        name: (identifier))))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (event_declaration
        (attribute_list
          (attribute
            name: (identifier))
          (attribute
            name: (identifier)
            (attribute_argument_list)))
        (attribute_list
          (attribute
            name: (identifier)))
        (modifier)
        type: (identifier)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (block))
          (accessor_declaration
            body: (block))))))
  (class_declaration
    name: (identifier)
    (type_parameter_list
      (type_parameter
        (attribute_list
          (attribute
            name: (identifier))
          (attribute
            name: (identifier)))
        (attribute_list
          (attribute
            name: (identifier)
            (attribute_argument_list)))
        name: (identifier)))
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        type_parameters: (type_parameter_list
          (type_parameter
            (attribute_list
              (attribute
                name: (identifier)))
            (attribute_list
              (attribute
                name: (identifier))
              (attribute
                name: (identifier)
                (attribute_argument_list
                  (attribute_argument
                    (integer_literal)))))
            name: (identifier)))
        parameters: (parameter_list)
        body: (block))))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (event_declaration
        (modifier)
        type: (identifier)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            (attribute_list
              (attribute
                name: (identifier))
              (attribute
                name: (identifier)
                (attribute_argument_list)))
            (attribute_list
              (attribute
                name: (identifier)))
            body: (block))
          (accessor_declaration
            (attribute_list
              (attribute
                name: (identifier))
              (attribute
                name: (identifier)
                (attribute_argument_list)))
            (attribute_list
              (attribute
                name: (identifier)))
            body: (block)))))))

================================================================================
Attribute targets (non-global)
================================================================================

[type: Obsolete]
class A<[typevar: B] TC>
{
  [field:JsonIgnore]
  [property: JsonIgnore]
  public int D { get; set; }

  [method: Obsolete]
  [return: MaybeNull]
  public void E([param: AllowNull] int f) { }

  [event: Obsolete]
  public event EventHandler OnG;
}

---

(compilation_unit
  (class_declaration
    (attribute_list
      (attribute_target_specifier)
      (attribute
        (identifier)))
    (identifier)
    (type_parameter_list
      (type_parameter
        (attribute_list
          (attribute_target_specifier)
          (attribute
            (identifier)))
        (identifier)))
    (declaration_list
      (property_declaration
        (attribute_list
          (attribute_target_specifier)
          (attribute
            (identifier)))
        (attribute_list
          (attribute_target_specifier)
          (attribute
            (identifier)))
        (modifier)
        (predefined_type)
        (identifier)
        (accessor_list
          (accessor_declaration)
          (accessor_declaration)))
      (method_declaration
        (attribute_list
          (attribute_target_specifier)
          (attribute
            (identifier)))
        (attribute_list
          (attribute_target_specifier)
          (attribute
            (identifier)))
        (modifier)
        (predefined_type)
        (identifier)
        (parameter_list
          (parameter
            (attribute_list
              (attribute_target_specifier)
              (attribute
                (identifier)))
            (predefined_type)
            (identifier)))
        (block))
      (event_field_declaration
        (attribute_list
          (attribute_target_specifier)
          (attribute
            (identifier)))
        (modifier)
        (variable_declaration
          (identifier)
          (variable_declarator
            (identifier)))))))


================================================================================
Attribute quirks
================================================================================

[Theory,]
void A() { }

[Theory<About,Life>]
void A() { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      (attribute_list
        (attribute
          name: (identifier)))
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block)))
  (global_statement
    (local_function_statement
      (attribute_list
        (attribute
          name: (generic_name
            (identifier)
            (type_argument_list
              (identifier)
              (identifier)))))
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block))))

================================================================================
Lambda with attribute
================================================================================

var greeting = [Hello] () => Console.WriteLine("hello");

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (lambda_expression
            (attribute_list
              (attribute
                name: (identifier)))
            parameters: (parameter_list)
            body: (invocation_expression
              function: (member_access_expression
                expression: (identifier)
                name: (identifier))
              arguments: (argument_list
                (argument
                  (string_literal
                    (string_literal_content)))))))))))

================================================================================
Attribute named arguments with colon
================================================================================

[RegularExpression(pattern: "/.+", ErrorMessage = "The Callback Path Must start with a forward slash '/' followed by one or more characters")]
class Validator { }

[Route(Name: "default", Template = "/api/{id}")]
[Obsolete(message: "Use NewMethod instead", error: true)]
class Example { }

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    (attribute_list
      (attribute
        name: (identifier)
        (attribute_argument_list
          (attribute_argument
            name: (identifier)
            (string_literal
              (string_literal_content)))
          (attribute_argument
            name: (identifier)
            (string_literal
              (string_literal_content))))))
    name: (identifier)
    body: (declaration_list))
  (class_declaration
    (attribute_list
      (attribute
        name: (identifier)
        (attribute_argument_list
          (attribute_argument
            name: (identifier)
            (string_literal
              (string_literal_content)))
          (attribute_argument
            name: (identifier)
            (string_literal
              (string_literal_content))))))
    (attribute_list
      (attribute
        name: (identifier)
        (attribute_argument_list
          (attribute_argument
            name: (identifier)
            (string_literal
              (string_literal_content)))
          (attribute_argument
            name: (identifier)
            (boolean_literal)))))
    name: (identifier)
    body: (declaration_list)))
```

## File: `test/corpus/classes.txt`
```
================================================================================
Class Definitions
================================================================================

public class F {}

public class F : object, IAlpha, IOmega { }

public partial class F<T> {}

internal class F<in T1, out T2> {}

public class F<T> where T:struct {}

public class F<T> where T:unmanaged {}

public class F<T> where T:class?, notnull, Mine? {}

public class F<T> where T: new() {}

public class F<T> where T: I, new() {}

private class F<T1,T2> where T1 : I1, I2, new() where T2 : I2 { }

class Foo {
  public Foo() {}

  // expression bodied constructor
  public Foo(string name) => Name = name;

  // static constructor
  static Foo() {}
  static extern Foo() {}
  extern static Foo() {}

  // extern destructor
  extern ~Foo() {}

  // expression bodied destructor
  ~Foo() => DoSomething();

  // constants
  private const int a = 1;
  const string b = $"hello";

  // indexer
  public bool this[int index] {
    get { return a; }
    set { a = value; }
  }

  // expression bodied indexer
  public bool this[int index] => a[index];

  public string this[int index]
  {
    get => a[index];
    set => a[index] = value;
  }

  public int this[params string[] arguments] {
    get { return 1; }
  }

  B.C d() {
    return null;
  }
}

class Bar(int a, int b) {
  int add() {
    return a + b;
  }
}

// unicode class name
class Ωµ {
  B.C d() {
    return null;
  }
}

// file scoped class
file class A {}

class Baz(int a, int b) : Bar(a, b) { }

public class NoBody;

private class NoBodyPrimary(int a, int b);

public class NoBodyPrimaryWithBase(int x) : Base(x);

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    (modifier)
    name: (identifier)
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (base_list
      (predefined_type)
      (identifier)
      (identifier))
    body: (declaration_list))
  (class_declaration
    (modifier)
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier))
      (type_parameter
        name: (identifier)))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint)
      (type_parameter_constraint)
      (type_parameter_constraint
        type: (nullable_type
          type: (identifier))))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        (constructor_constraint)))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier))
      (type_parameter_constraint
        (constructor_constraint)))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier))
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier))
      (type_parameter_constraint
        type: (identifier))
      (type_parameter_constraint
        (constructor_constraint)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier)))
    body: (declaration_list))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (constructor_declaration
        (modifier)
        name: (identifier)
        parameters: (parameter_list)
        body: (block))
      (comment)
      (constructor_declaration
        (modifier)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        body: (arrow_expression_clause
          (assignment_expression
            left: (identifier)
            right: (identifier))))
      (comment)
      (constructor_declaration
        (modifier)
        name: (identifier)
        parameters: (parameter_list)
        body: (block))
      (constructor_declaration
        (modifier)
        (modifier)
        name: (identifier)
        parameters: (parameter_list)
        body: (block))
      (constructor_declaration
        (modifier)
        (modifier)
        name: (identifier)
        parameters: (parameter_list)
        body: (block))
      (comment)
      (destructor_declaration
        name: (identifier)
        parameters: (parameter_list)
        body: (block))
      (comment)
      (destructor_declaration
        name: (identifier)
        parameters: (parameter_list)
        body: (arrow_expression_clause
          (invocation_expression
            function: (identifier)
            arguments: (argument_list))))
      (comment)
      (field_declaration
        (modifier)
        (modifier)
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier)
            (integer_literal))))
      (field_declaration
        (modifier)
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier)
            (interpolated_string_expression
              (interpolation_start)
              (string_content)))))
      (comment)
      (indexer_declaration
        (modifier)
        type: (predefined_type)
        parameters: (bracketed_parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        accessors: (accessor_list
          (accessor_declaration
            body: (block
              (return_statement
                (identifier))))
          (accessor_declaration
            body: (block
              (expression_statement
                (assignment_expression
                  left: (identifier)
                  right: (identifier)))))))
      (comment)
      (indexer_declaration
        (modifier)
        type: (predefined_type)
        parameters: (bracketed_parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        value: (arrow_expression_clause
          (element_access_expression
            expression: (identifier)
            subscript: (bracketed_argument_list
              (argument
                (identifier))))))
      (indexer_declaration
        (modifier)
        type: (predefined_type)
        parameters: (bracketed_parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        accessors: (accessor_list
          (accessor_declaration
            body: (arrow_expression_clause
              (element_access_expression
                expression: (identifier)
                subscript: (bracketed_argument_list
                  (argument
                    (identifier))))))
          (accessor_declaration
            body: (arrow_expression_clause
              (assignment_expression
                left: (element_access_expression
                  expression: (identifier)
                  subscript: (bracketed_argument_list
                    (argument
                      (identifier))))
                right: (identifier))))))
      (indexer_declaration
        (modifier)
        type: (predefined_type)
        parameters: (bracketed_parameter_list
          type: (array_type
            type: (predefined_type)
            rank: (array_rank_specifier))
          name: (identifier))
        accessors: (accessor_list
          (accessor_declaration
            body: (block
              (return_statement
                (integer_literal))))))
      (method_declaration
        returns: (qualified_name
          qualifier: (identifier)
          name: (identifier))
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement
            (null_literal))))))
  (class_declaration
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier)))
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))))
  (comment)
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (qualified_name
          qualifier: (identifier)
          name: (identifier))
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement
            (null_literal))))))
  (comment)
  (class_declaration
    (modifier)
    name: (identifier)
    body: (declaration_list))
  (class_declaration
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier)))
    (base_list
      (identifier)
      (argument_list
        (argument
          (identifier))
        (argument
          (identifier))))
    body: (declaration_list))
  (class_declaration
    (modifier)
    name: (identifier)
  )
  (class_declaration
    (modifier)
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier)))
  )
  (class_declaration
    (modifier)
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier)))
    (base_list
      (identifier)
      (argument_list
        (argument
          (identifier))))))

```

## File: `test/corpus/contextual-keywords.txt`
```
================================================================================
From keyword can be a variable
================================================================================

var a = Assert.Range(from, to);

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (invocation_expression
            function: (member_access_expression
              expression: (identifier)
              name: (identifier))
            arguments: (argument_list
              (argument
                (identifier))
              (argument
                (identifier)))))))))

================================================================================
File keyword in invocation
================================================================================

file.Method(1, 2);

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (invocation_expression
        function: (member_access_expression
          expression: (identifier)
          name: (identifier))
        arguments: (argument_list
          (argument
            (integer_literal))
          (argument
            (integer_literal)))))))

================================================================================
File contextual keyword
================================================================================

void file() { }
void m(file p) { }
void m(int file) { }
void m()
{
    file v = null;
    int file = file;

    file();
    m(file);

    var x = file + 1;
}

file class file { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (identifier)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (predefined_type)
            (variable_declarator
              name: (identifier)
              (identifier))))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list)))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (binary_expression
                left: (identifier)
                right: (integer_literal))))))))
  (class_declaration
    (modifier)
    name: (identifier)
    body: (declaration_list)))

================================================================================
Scoped contextual keyword
================================================================================

void scoped() { }
void m(scoped p) { }
void m(scoped ref int p) { }
void m(scoped ref scoped p) { }
void m(int scoped) { }
void m()
{
    scoped v = null;
    scoped ref int v = null;
    scoped ref scoped v = null;
    int scoped = null;

    scoped();
    m(scoped);

    var x = scoped + 1;
    var l = scoped => null;
    var l = (scoped i) => null;
    var l = (scoped, i) => null;
    var l = scoped (int i, int j) => null;
}

class scoped { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (identifier)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          (modifier)
          (modifier)
          type: (predefined_type)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          (modifier)
          (modifier)
          type: (identifier)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (scoped_type
              type: (ref_type
                type: (predefined_type)))
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (scoped_type
              type: (ref_type
                type: (identifier)))
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (predefined_type)
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list)))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (binary_expression
                left: (identifier)
                right: (integer_literal)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                parameters: (implicit_parameter)
                body: (null_literal)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                parameters: (parameter_list
                  (parameter
                    type: (identifier)
                    name: (identifier)))
                body: (null_literal)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                parameters: (parameter_list
                  (parameter
                    name: (identifier))
                  (parameter
                    name: (identifier)))
                body: (null_literal)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                type: (identifier)
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier))
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                body: (null_literal))))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list)))

================================================================================
Set contextual keyword
================================================================================

void set() { }
void m(set p) { }
void m(int set) { }
void m()
{
    set v = null;
    int set = set;

    set();
    m(set);

    var x = set + 1;
}

class set { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (identifier)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (predefined_type)
            (variable_declarator
              name: (identifier)
              (identifier))))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list)))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (binary_expression
                left: (identifier)
                right: (integer_literal))))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list)))

================================================================================
Var contextual keyword
================================================================================

void var() { }
void m(var p) { }
void m(int var) { }
void m()
{
    var v = null;
    int var = var;
    var var = 1;

    var();
    m(var);

    var x = var + 1;
}

class var { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (implicit_type)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (predefined_type)
            (variable_declarator
              name: (identifier)
              (identifier))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (integer_literal))))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list)))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (binary_expression
                left: (identifier)
                right: (integer_literal))))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list)))

================================================================================
Nameof contextual keyword
================================================================================

void nameof() { }
void m(nameof p) { }
void m(int nameof) { }
void m()
{
    nameof v = null;
    int nameof = nameof;

    nameof();
    nameof(a, b);
    m(nameof);

    var x = nameof + 1;
}

class nameof { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (identifier)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier)))
      body: (block)))
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (null_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (predefined_type)
            (variable_declarator
              name: (identifier)
              (identifier))))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list)))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier))
              (argument
                (identifier)))))
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (binary_expression
                left: (identifier)
                right: (integer_literal))))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list)))
```

## File: `test/corpus/enums.txt`
```
================================================================================
global enum with one option
================================================================================

enum A: byte { One, Two = 2, Three = 0x03 }

enum NoBody;

--------------------------------------------------------------------------------

(compilation_unit
  (enum_declaration
    name: (identifier)
    (base_list
      (predefined_type))
    body: (enum_member_declaration_list
      (enum_member_declaration
        name: (identifier))
      (enum_member_declaration
        name: (identifier)
        value: (integer_literal))
      (enum_member_declaration
        name: (identifier)
        value: (integer_literal))))
(enum_declaration
  name: (identifier)))
```

## File: `test/corpus/expressions.txt`
```
================================================================================
Assignment to Prefix Unary Expressions
================================================================================

a = +a;
a = -a;
a = !a;
a = ~a;
a = ++a;
a = --a;
a = a++;
a = a--;
a = a!;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (prefix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (prefix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (prefix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (prefix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (prefix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (prefix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (postfix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (postfix_unary_expression
          (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (postfix_unary_expression
          (identifier))))))

================================================================================
Assignment to Binary Expressions
================================================================================

a = a + a;
a = a - a;
a = a * a;
a = a / a;
a = a % a;
a = a & a;
a = a | a;
a = a ^ a;
a = a >> a;
a = a << a;
a = a >>> a;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier))))))

================================================================================
Assignment to Binary Equality Expressions
================================================================================

a = a == b;
a = a != b;
a = a < b;
a = a <= b;
a = a > b;
a = a >= b;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (identifier)
          right: (identifier))))))

================================================================================
Assignment Binary Expressions
================================================================================

a += a;
a -= a;
a *= a;
a /= a;
a %= a;
a++;
a--;
a <<= a;
a >>= a;
a >>>= a;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier))))
  (global_statement
    (expression_statement
      (postfix_unary_expression
        (identifier))))
  (global_statement
    (expression_statement
      (postfix_unary_expression
        (identifier))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (identifier)))))

================================================================================
Assignment LValue types
================================================================================

a = 1;
a.b = 1;
a[b] = 1;
(a, b) = (1, 2);
(var a, b) = (1, 2);
var x = new A
{
  a = 1,
  [b] = 1
};
(a) = 1;
*p = 0;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (integer_literal))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (member_access_expression
          expression: (identifier)
          name: (identifier))
        right: (integer_literal))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (element_access_expression
          expression: (identifier)
          subscript: (bracketed_argument_list
            (argument
              (identifier))))
        right: (integer_literal))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (tuple_expression
          (argument
            (identifier))
          (argument
            (identifier)))
        right: (tuple_expression
          (argument
            (integer_literal))
          (argument
            (integer_literal))))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (tuple_expression
          (argument
            (declaration_expression
              type: (implicit_type)
              name: (identifier)))
          (argument
            (identifier)))
        right: (tuple_expression
          (argument
            (integer_literal))
          (argument
            (integer_literal))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (object_creation_expression
            type: (identifier)
            initializer: (initializer_expression
              (assignment_expression
                left: (identifier)
                right: (integer_literal))
              (assignment_expression
                left: (element_binding_expression
                  (argument
                    (identifier)))
                right: (integer_literal))))))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (parenthesized_expression
          (identifier))
        right: (integer_literal))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (prefix_unary_expression
          (identifier))
        right: (integer_literal)))))

================================================================================
Ternary Expression
================================================================================

class Foo {
  void Test() {
    var y = x ? "foo" : "bar";
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (conditional_expression
                  condition: (identifier)
                  consequence: (string_literal
                    (string_literal_content))
                  alternative: (string_literal
                    (string_literal_content)))))))))))

================================================================================
Binary Expressions
================================================================================

class Foo {
  void Test() {
    var b = x == y;
    var i = 1 + 2;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (binary_expression
                  left: (identifier)
                  right: (identifier)))))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (binary_expression
                  left: (integer_literal)
                  right: (integer_literal))))))))))

================================================================================
Ternary expressions is type
================================================================================

var t = x is int
  ? a
  : b;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_expression
            condition: (is_expression
              left: (identifier)
              right: (predefined_type))
            consequence: (identifier)
            alternative: (identifier)))))))

================================================================================
Ternary expressions is nullable type
================================================================================

var u = x is int?
  ? a
  : b;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_expression
            condition: (is_expression
              left: (identifier)
              right: (nullable_type
                type: (predefined_type)))
            consequence: (identifier)
            alternative: (identifier)))))))

================================================================================
Prefix-Unary Expressions
================================================================================

class Foo {
  void Test() {
    ++x;
    --y;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (expression_statement
            (prefix_unary_expression
              (identifier)))
          (expression_statement
            (prefix_unary_expression
              (identifier))))))))

================================================================================
Cast expressions
================================================================================

void Test() {
  a = (B)c + (C)d;
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (assignment_expression
            left: (identifier)
            right: (binary_expression
              left: (cast_expression
                type: (identifier)
                value: (identifier))
              right: (cast_expression
                type: (identifier)
                value: (identifier)))))))))

================================================================================
Cast expression of array access
================================================================================

b = (float)a[0];

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (cast_expression
          type: (predefined_type)
          value: (element_access_expression
            expression: (identifier)
            subscript: (bracketed_argument_list
              (argument
                (integer_literal)))))))))

================================================================================
Cast with parenthesized expression
================================================================================

var o = (A.A)(a.a.a);
var o = (Int32)(1);
var o = (Int32)(1);
var o = (Int32)((1));

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (cast_expression
            type: (qualified_name
              qualifier: (identifier)
              name: (identifier))
            value: (parenthesized_expression
              (member_access_expression
                expression: (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                name: (identifier))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (cast_expression
            type: (identifier)
            value: (parenthesized_expression
              (integer_literal)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (cast_expression
            type: (identifier)
            value: (parenthesized_expression
              (integer_literal)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (cast_expression
            type: (identifier)
            value: (parenthesized_expression
              (parenthesized_expression
                (integer_literal)))))))))

================================================================================
Precedence of unary prefix operator and element access
================================================================================

b = +a[0];

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (prefix_unary_expression
          (element_access_expression
            expression: (identifier)
            subscript: (bracketed_argument_list
              (argument
                (integer_literal)))))))))

================================================================================
Precedence of switch_expression and binary_expression
================================================================================

b = 2 * a switch
{
    1 => 1,
    _ => 0,
};

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (integer_literal)
          right: (switch_expression
            (identifier)
            (switch_expression_arm
              (constant_pattern
                (integer_literal))
              (integer_literal))
            (switch_expression_arm
              (discard)
              (integer_literal))))))))

================================================================================
Anonymous object creation with empty body
================================================================================

void b() {
  var x = new {
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_object_creation_expression))))))))

================================================================================
Target-type object creation
================================================================================

void b() {
  Friend friend = new("hi");
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (implicit_object_creation_expression
                (argument_list
                  (argument
                    (string_literal
                      (string_literal_content))))))))))))

================================================================================
Anonymous object creation with single unnamed
================================================================================

void b() {
  var x = new {
    args
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_object_creation_expression
                (identifier)))))))))

================================================================================
Anonymous object creation with single named
================================================================================

void b() {
  var x = new {
    test = "This"
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_object_creation_expression
                (identifier)
                (string_literal
                  (string_literal_content))))))))))

================================================================================
Checked expressions
================================================================================

void b() {
  var three = checked(1 + 2);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (checked_expression
                (binary_expression
                  left: (integer_literal)
                  right: (integer_literal))))))))))

================================================================================
Object creation expressions
================================================================================

void b() {
  new C.D(1, "hi");
  a = new E
  {
    Foo = bar,
  };

  b = new E(1);

  c = new E(1) { };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (object_creation_expression
            type: (qualified_name
              qualifier: (identifier)
              name: (identifier))
            arguments: (argument_list
              (argument
                (integer_literal))
              (argument
                (string_literal
                  (string_literal_content))))))
        (expression_statement
          (assignment_expression
            left: (identifier)
            right: (object_creation_expression
              type: (identifier)
              initializer: (initializer_expression
                (assignment_expression
                  left: (identifier)
                  right: (identifier))))))
        (expression_statement
          (assignment_expression
            left: (identifier)
            right: (object_creation_expression
              type: (identifier)
              arguments: (argument_list
                (argument
                  (integer_literal))))))
        (expression_statement
          (assignment_expression
            left: (identifier)
            right: (object_creation_expression
              type: (identifier)
              arguments: (argument_list
                (argument
                  (integer_literal)))
              initializer: (initializer_expression))))))))

================================================================================
Named parameters in constructors
================================================================================

void b() {
  var z = new C(a: 1, b: "hi");
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (object_creation_expression
                type: (identifier)
                arguments: (argument_list
                  (argument
                    name: (identifier)
                    (integer_literal))
                  (argument
                    name: (identifier)
                    (string_literal
                      (string_literal_content))))))))))))

================================================================================
Named parameters in method calls
================================================================================

void b() {
  z = A.B(a: 1, b: "hi");
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (assignment_expression
            left: (identifier)
            right: (invocation_expression
              function: (member_access_expression
                expression: (identifier)
                name: (identifier))
              arguments: (argument_list
                (argument
                  name: (identifier)
                  (integer_literal))
                (argument
                  name: (identifier)
                  (string_literal
                    (string_literal_content)))))))))))

================================================================================
Named parameters using contextually reserved words
================================================================================

void b() {
  resultNode = B(from: 1, into: "hi");
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (assignment_expression
            left: (identifier)
            right: (invocation_expression
              function: (identifier)
              arguments: (argument_list
                (argument
                  name: (identifier)
                  (integer_literal))
                (argument
                  name: (identifier)
                  (string_literal
                    (string_literal_content)))))))))))

================================================================================
Anonymous method expressions
================================================================================

void a() {
  var d = delegate(int a) {
    return a;
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_method_expression
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                (block
                  (return_statement
                    (identifier)))))))))))

================================================================================
Anonymous method expression with discard parameters
================================================================================

void a() {
  var d = delegate(int _, int _) {
    return a;
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_method_expression
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier))
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                (block
                  (return_statement
                    (identifier)))))))))))

================================================================================
Anonymous method expression with modifiers
================================================================================

void m() {
  var a = static delegate(int a) { return a; };
  var b = async delegate(int a) { return a; };
  var c = async static delegate(int a) { return a; };
  var d = static async delegate(int a) { return a; };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_method_expression
                (modifier)
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                (block
                  (return_statement
                    (identifier)))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_method_expression
                (modifier)
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                (block
                  (return_statement
                    (identifier)))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_method_expression
                (modifier)
                (modifier)
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                (block
                  (return_statement
                    (identifier)))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (anonymous_method_expression
                (modifier)
                (modifier)
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                (block
                  (return_statement
                    (identifier)))))))))))

================================================================================
Lambda expressions
================================================================================

void a() {
  var l = x => x + 1;
  var l = (A a, B b) => { return a.c(b); };
  var l = RetType (A a, B b) => { return 1; };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                parameters: (implicit_parameter)
                body: (binary_expression
                  left: (identifier)
                  right: (integer_literal))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                parameters: (parameter_list
                  (parameter
                    type: (identifier)
                    name: (identifier))
                  (parameter
                    type: (identifier)
                    name: (identifier)))
                body: (block
                  (return_statement
                    (invocation_expression
                      function: (member_access_expression
                        expression: (identifier)
                        name: (identifier))
                      arguments: (argument_list
                        (argument
                          (identifier))))))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                type: (identifier)
                parameters: (parameter_list
                  (parameter
                    type: (identifier)
                    name: (identifier))
                  (parameter
                    type: (identifier)
                    name: (identifier)))
                body: (block
                  (return_statement
                    (integer_literal)))))))))))

================================================================================
Async Lambda
================================================================================

void a()
{
    Do(async () => {});
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (lambda_expression
                  (modifier)
                  parameters: (parameter_list)
                  body: (block))))))))))

================================================================================
Lambda expression with modifiers
================================================================================

void a() {
  var lam = static x => x + 1;
  var bda = async x => x + 1;
  var syn = async static x => x + 1;
  var txt = static async x => x + 1;
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                (modifier)
                parameters: (implicit_parameter)
                body: (binary_expression
                  left: (identifier)
                  right: (integer_literal))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                (modifier)
                parameters: (implicit_parameter)
                body: (binary_expression
                  left: (identifier)
                  right: (integer_literal))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                (modifier)
                (modifier)
                parameters: (implicit_parameter)
                body: (binary_expression
                  left: (identifier)
                  right: (integer_literal))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                (modifier)
                (modifier)
                parameters: (implicit_parameter)
                body: (binary_expression
                  left: (identifier)
                  right: (integer_literal))))))))))

================================================================================
Lambda expression with discard parameters
================================================================================

void a() {
  var lam = (_, _) => 0;
  var bda = (int _, int _) => 0;
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                parameters: (parameter_list
                  (parameter
                    name: (identifier))
                  (parameter
                    name: (identifier)))
                body: (integer_literal)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (lambda_expression
                parameters: (parameter_list
                  (parameter
                    type: (predefined_type)
                    name: (identifier))
                  (parameter
                    type: (predefined_type)
                    name: (identifier)))
                body: (integer_literal)))))))))

================================================================================
Lambda expression with ref modifier
================================================================================

MyIntDelegate a = (ref int i) => i + 1;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (lambda_expression
            parameters: (parameter_list
              (parameter
                type: (ref_type
                  type: (predefined_type))
                name: (identifier)))
            body: (binary_expression
              left: (identifier)
              right: (integer_literal))))))))

================================================================================
Invocation expressions
================================================================================

void a() {
  b(c, in d, out e, ref f, out var g);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier))
              (argument
                (identifier))
              (argument
                (identifier))
              (argument
                (identifier))
              (argument
                (declaration_expression
                  type: (implicit_type)
                  name: (identifier))))))))))

================================================================================
Tuple expressions
================================================================================

void a() {
  b = (c, d: "e");
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (assignment_expression
            left: (identifier)
            right: (tuple_expression
              (argument
                (identifier))
              (argument
                name: (identifier)
                (string_literal
                  (string_literal_content))))))))))

================================================================================
Implicit array creation
================================================================================

void b() {
  var z = new [] { 1, 2, 3 };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (implicit_array_creation_expression
                (initializer_expression
                  (integer_literal)
                  (integer_literal)
                  (integer_literal))))))))))

================================================================================
Implicit multi array creation
================================================================================

void b() {
  var z = new [,] { { 1, 1 }, { 2, 2 }, { 3, 3 } };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (implicit_array_creation_expression
                (initializer_expression
                  (initializer_expression
                    (integer_literal)
                    (integer_literal))
                  (initializer_expression
                    (integer_literal)
                    (integer_literal))
                  (initializer_expression
                    (integer_literal)
                    (integer_literal)))))))))))

================================================================================
Stackalloc implicit array
================================================================================

void b() {
  var z = stackalloc [] { 1, 2, 3 };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (implicit_stackalloc_expression
                (initializer_expression
                  (integer_literal)
                  (integer_literal)
                  (integer_literal))))))))))

================================================================================
Stackalloc explicit array
================================================================================

void b() {
  var z = stackalloc int[] { 1, 2, 3 };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (stackalloc_expression
                type: (array_type
                  type: (predefined_type)
                  rank: (array_rank_specifier))
                (initializer_expression
                  (integer_literal)
                  (integer_literal)
                  (integer_literal))))))))))

================================================================================
Explicit array creation
================================================================================

void b() {
  var z = new int[3] { 1, 2, 3 };
  var b = new byte[,] { { 1, 2 }, { 2, 3 } };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (array_creation_expression
                type: (array_type
                  type: (predefined_type)
                  rank: (array_rank_specifier
                    (integer_literal)))
                (initializer_expression
                  (integer_literal)
                  (integer_literal)
                  (integer_literal))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (array_creation_expression
                type: (array_type
                  type: (predefined_type)
                  rank: (array_rank_specifier))
                (initializer_expression
                  (initializer_expression
                    (integer_literal)
                    (integer_literal))
                  (initializer_expression
                    (integer_literal)
                    (integer_literal)))))))))))

================================================================================
Explicit multi array creation
================================================================================

void b() {
  var z = new int[3,2] { { 1, 1 }, { 2, 2 }, { 3, 3 } };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (array_creation_expression
                type: (array_type
                  type: (predefined_type)
                  rank: (array_rank_specifier
                    (integer_literal)
                    (integer_literal)))
                (initializer_expression
                  (initializer_expression
                    (integer_literal)
                    (integer_literal))
                  (initializer_expression
                    (integer_literal)
                    (integer_literal))
                  (initializer_expression
                    (integer_literal)
                    (integer_literal)))))))))))

================================================================================
Array of named tuple
================================================================================

void a() {
  var z = new (string b, string c)[3];
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (array_creation_expression
                type: (array_type
                  type: (tuple_type
                    (tuple_element
                      type: (predefined_type)
                      name: (identifier))
                    (tuple_element
                      type: (predefined_type)
                      name: (identifier)))
                  rank: (array_rank_specifier
                    (integer_literal)))))))))))

================================================================================
Makeref
================================================================================

void b() {
  var gp = __makeref(g);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (makeref_expression
                (identifier)))))))))

================================================================================
Postfix unary
================================================================================

void b() {
  a--;
  a++;
  var b=a!;
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (postfix_unary_expression
            (identifier)))
        (expression_statement
          (postfix_unary_expression
            (identifier)))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (postfix_unary_expression
                (identifier)))))))))

================================================================================
__reftype
================================================================================

void b() {
  var z = __reftype(g);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (reftype_expression
                (identifier)))))))))

================================================================================
__refvalue
================================================================================

void b() {
  var z = __refvalue(g, int);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (refvalue_expression
                value: (identifier)
                type: (predefined_type)))))))))

================================================================================
sizeof
================================================================================

void b() {
  var z = sizeof(int);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (sizeof_expression
                type: (predefined_type)))))))))

================================================================================
typeof
================================================================================

void b() {
  var y = typeof(int);
  var z = typeof(List<string>.Enumerator);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (typeof_expression
                type: (predefined_type)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (typeof_expression
                type: (qualified_name
                  qualifier: (generic_name
                    (identifier)
                    (type_argument_list
                      (predefined_type)))
                  name: (identifier))))))))))

================================================================================
switch expression
================================================================================

void b() {
  var r = operation switch {
      1 => "one",
      2 => "two",
      _ => "more"
  };

  var t = obj.Parent.Parent switch {
    A(S.G) { Parent: A { Parent: B baseProperty } } => baseProperty.Type,
    _ => null,
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (switch_expression
                (identifier)
                (switch_expression_arm
                  (constant_pattern
                    (integer_literal))
                  (string_literal
                    (string_literal_content)))
                (switch_expression_arm
                  (constant_pattern
                    (integer_literal))
                  (string_literal
                    (string_literal_content)))
                (switch_expression_arm
                  (discard)
                  (string_literal
                    (string_literal_content)))))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (switch_expression
                (member_access_expression
                  expression: (member_access_expression
                    expression: (identifier)
                    name: (identifier))
                  name: (identifier))
                (switch_expression_arm
                  (recursive_pattern
                    type: (identifier)
                    (positional_pattern_clause
                      (subpattern
                        (constant_pattern
                          (member_access_expression
                            expression: (identifier)
                            name: (identifier)))))
                    (property_pattern_clause
                      (subpattern
                        (identifier)
                        (recursive_pattern
                          type: (identifier)
                          (property_pattern_clause
                            (subpattern
                              (identifier)
                              (declaration_pattern
                                type: (identifier)
                                name: (identifier))))))))
                  (member_access_expression
                    expression: (identifier)
                    name: (identifier)))
                (switch_expression_arm
                  (discard)
                  (null_literal))))))))))

================================================================================
switch expression with trailing comma
================================================================================

void b() {
  var r = operation switch {
      1 => "one",
      2 => "two",
      _ => "more",
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (switch_expression
                (identifier)
                (switch_expression_arm
                  (constant_pattern
                    (integer_literal))
                  (string_literal
                    (string_literal_content)))
                (switch_expression_arm
                  (constant_pattern
                    (integer_literal))
                  (string_literal
                    (string_literal_content)))
                (switch_expression_arm
                  (discard)
                  (string_literal
                    (string_literal_content)))))))))))

================================================================================
switch expression return
================================================================================

string b(Object operation) =>
  operation switch {
      1 => "one",
      _ => "more",
  };

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (identifier)
          name: (identifier)))
      body: (arrow_expression_clause
        (switch_expression
          (identifier)
          (switch_expression_arm
            (constant_pattern
              (integer_literal))
            (string_literal
              (string_literal_content)))
          (switch_expression_arm
            (discard)
            (string_literal
              (string_literal_content))))))))

================================================================================
switch expression with patterns
================================================================================

string b(Object operation) =>
  operation switch {
      Declaration d => "declaration",
      Simple => "simple (constant)",
      { } => "nothing",
      var z => "var",
      null => "constant",
      int => "type"
  };

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (identifier)
          name: (identifier)))
      body: (arrow_expression_clause
        (switch_expression
          (identifier)
          (switch_expression_arm
            (declaration_pattern
              type: (identifier)
              name: (identifier))
            (string_literal
              (string_literal_content)))
          (switch_expression_arm
            (constant_pattern
              (identifier))
            (string_literal
              (string_literal_content)))
          (switch_expression_arm
            (recursive_pattern
              (property_pattern_clause))
            (string_literal
              (string_literal_content)))
          (switch_expression_arm
            (declaration_pattern
              type: (implicit_type)
              name: (identifier))
            (string_literal
              (string_literal_content)))
          (switch_expression_arm
            (constant_pattern
              (null_literal))
            (string_literal
              (string_literal_content)))
          (switch_expression_arm
            (type_pattern
              type: (predefined_type))
            (string_literal
              (string_literal_content))))))))

================================================================================
await Expression
================================================================================

class Foo {
  void Test() {
    await x;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (expression_statement
            (await_expression
              (identifier))))))))

================================================================================
throw expression
================================================================================

class Foo {
  void Test() {
    x = x ?? throw y;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (expression_statement
            (assignment_expression
              left: (identifier)
              right: (binary_expression
                left: (identifier)
                right: (throw_expression
                  (identifier))))))))))

================================================================================
Pecedence with OR and XOR
================================================================================

b = 4 | 5 ^ 6;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (assignment_expression
        left: (identifier)
        right: (binary_expression
          left: (integer_literal)
          right: (binary_expression
            left: (integer_literal)
            right: (integer_literal)))))))

================================================================================
range expressions full
================================================================================

class Foo {
  void Test() {
    var a = b[1..4];
    var c = 1..^4;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (element_access_expression
                  expression: (identifier)
                  subscript: (bracketed_argument_list
                    (argument
                      (range_expression
                        (integer_literal)
                        (integer_literal))))))))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (range_expression
                  (integer_literal)
                  (prefix_unary_expression
                    (integer_literal)))))))))))

================================================================================
range expressions partial
================================================================================

class Foo {
  void Test() {
    var a = b[..4];
    var c = ^1..;
    var d = b[..];
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (element_access_expression
                  expression: (identifier)
                  subscript: (bracketed_argument_list
                    (argument
                      (range_expression
                        (integer_literal))))))))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (range_expression
                  (prefix_unary_expression
                    (integer_literal))))))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (element_access_expression
                  expression: (identifier)
                  subscript: (bracketed_argument_list
                    (argument
                      (range_expression))))))))))))

================================================================================
cast expression
================================================================================

class Foo {
  void Test() {
    x = (int) y;
      }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (expression_statement
            (assignment_expression
              left: (identifier)
              right: (cast_expression
                type: (predefined_type)
                value: (identifier)))))))))

================================================================================
Generic type name no type args
================================================================================

var d = typeof(Dictionary<,>);
var t = typeof(Tuple<,,,>);

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (typeof_expression
            type: (generic_name
              (identifier)
              (type_argument_list)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (typeof_expression
            type: (generic_name
              (identifier)
              (type_argument_list))))))))

================================================================================
default expression
================================================================================

var a = default(int);
int b = default;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (default_expression
            type: (predefined_type))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (default_expression))))))

================================================================================
Ref local declaration and ref expression
================================================================================

ref VeryLargeStruct reflocal = ref veryLargeStruct;
ref var elementRef = ref arr[0];

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (ref_type
          type: (identifier))
        (variable_declarator
          name: (identifier)
          (ref_expression
            (identifier))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (ref_type
          type: (implicit_type))
        (variable_declarator
          name: (identifier)
          (ref_expression
            (element_access_expression
              expression: (identifier)
              subscript: (bracketed_argument_list
                (argument
                  (integer_literal))))))))))

================================================================================
Element binding expression
================================================================================

var x = new Dictionary<string,int> { ["a"] = 65 };

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (object_creation_expression
            type: (generic_name
              (identifier)
              (type_argument_list
                (predefined_type)
                (predefined_type)))
            initializer: (initializer_expression
              (assignment_expression
                left: (element_binding_expression
                  (argument
                    (string_literal
                      (string_literal_content))))
                right: (integer_literal)))))))))

================================================================================
Member access expression (methods)
================================================================================

void Test(int value) {
  value.ToString();
  double.IsInfinity(value);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier)))
      body: (block
        (expression_statement
          (invocation_expression
            function: (member_access_expression
              expression: (identifier)
              name: (identifier))
            arguments: (argument_list)))
        (expression_statement
          (invocation_expression
            function: (member_access_expression
              expression: (predefined_type)
              name: (identifier))
            arguments: (argument_list
              (argument
                (identifier)))))))))

================================================================================
Member access expression (properties)
================================================================================

void Test(int value) {
  var x = string.Empty;
  var z = B<int>.Something;
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier)))
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (member_access_expression
                expression: (predefined_type)
                name: (identifier)))))
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (member_access_expression
                expression: (generic_name
                  (identifier)
                  (type_argument_list
                    (predefined_type)))
                name: (identifier)))))))))

================================================================================
is expression
================================================================================

var b = s is string;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_expression
            left: (identifier)
            right: (predefined_type)))))))

================================================================================
is pattern
================================================================================

var b = s is string s2;
var c = s is "test";
var a = 1 is int.MaxValue;
var d = a is nameof(a);
var e = a is (int)b;
var f = b is A { E: C(S.C) bb } ? bb : null;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (declaration_pattern
              type: (predefined_type)
              name: (identifier)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (constant_pattern
              (string_literal
                (string_literal_content))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (integer_literal)
            pattern: (constant_pattern
              (member_access_expression
                expression: (predefined_type)
                name: (identifier))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (constant_pattern
              (invocation_expression
                function: (identifier)
                arguments: (argument_list
                  (argument
                    (identifier))))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (constant_pattern
              (cast_expression
                type: (predefined_type)
                value: (identifier))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_expression
            condition: (is_pattern_expression
              expression: (identifier)
              pattern: (recursive_pattern
                type: (identifier)
                (property_pattern_clause
                  (subpattern
                    (identifier)
                    (recursive_pattern
                      type: (identifier)
                      (positional_pattern_clause
                        (subpattern
                          (type_pattern
                            type: (qualified_name
                              qualifier: (identifier)
                              name: (identifier)))))
                      name: (identifier))))))
            consequence: (identifier)
            alternative: (null_literal)))))))

================================================================================
Precedence between is operator and conditional_expression
================================================================================

int a = 1 is Object ? 1 : 2;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (conditional_expression
            condition: (is_pattern_expression
              expression: (integer_literal)
              pattern: (constant_pattern
                (identifier)))
            consequence: (integer_literal)
            alternative: (integer_literal)))))))

================================================================================
Precedence between is operator and as operator
================================================================================

//var a = new object() is null as Object == false; // this parses with wrong precedence
var a = new object() is null as Object;
var b = true == 1 as int? is int;

--------------------------------------------------------------------------------

(compilation_unit
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (as_expression
            left: (is_pattern_expression
              expression: (object_creation_expression
                type: (predefined_type)
                arguments: (argument_list))
              pattern: (constant_pattern
                (null_literal)))
            right: (identifier))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (binary_expression
            left: (boolean_literal)
            right: (is_expression
              left: (as_expression
                left: (integer_literal)
                right: (nullable_type
                  type: (predefined_type)))
              right: (predefined_type))))))))

================================================================================
Discard pattern
================================================================================

void Do() {
  DateTime.TryParse(dateString, out _);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (expression_statement
          (invocation_expression
            function: (member_access_expression
              expression: (identifier)
              name: (identifier))
            arguments: (argument_list
              (argument
                (identifier))
              (argument
                (identifier)))))))))

================================================================================
Null-forgiving operator
================================================================================

var x = name!.Length;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (member_access_expression
            expression: (postfix_unary_expression
              (identifier))
            name: (identifier)))))))

================================================================================
Negated pattern
================================================================================

var x = name is not null;
if (a is not B { E: C(S.E) x }) {}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (negated_pattern
              (constant_pattern
                (null_literal))))))))
  (global_statement
    (if_statement
      condition: (is_pattern_expression
        expression: (identifier)
        pattern: (negated_pattern
          (recursive_pattern
            type: (identifier)
            (property_pattern_clause
              (subpattern
                (identifier)
                (recursive_pattern
                  type: (identifier)
                  (positional_pattern_clause
                    (subpattern
                      (type_pattern
                        type: (qualified_name
                          qualifier: (identifier)
                          name: (identifier)))))
                  name: (identifier)))))))
      consequence: (block))))

================================================================================
Parenthesized pattern
================================================================================

var x = name is (var a);

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (parenthesized_pattern
              (declaration_pattern
                type: (implicit_type)
                name: (identifier)))))))))

================================================================================
Pattern Combinators and relational pattern
================================================================================

var x = c is < '0' or >= 'A' and <= 'Z';

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (or_pattern
              left: (relational_pattern
                (character_literal
                  (character_literal_content)))
              right: (and_pattern
                left: (relational_pattern
                  (character_literal
                    (character_literal_content)))
                right: (relational_pattern
                  (character_literal
                    (character_literal_content)))))))))))

================================================================================
Precedence of prefix_unary_expression and invocation_expression
================================================================================

var x = !this.Call();

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (prefix_unary_expression
            (invocation_expression
              function: (member_access_expression
                name: (identifier))
              arguments: (argument_list))))))))

================================================================================
Property patterns
================================================================================

var x = operand is ILiteralOperation { ConstantValue: { HasValue: true, Value: null } };
var x = operand is ILiteralOperation { ConstantValue.HasValue: true, ConstantValue.Value: null};

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (recursive_pattern
              type: (identifier)
              (property_pattern_clause
                (subpattern
                  (identifier)
                  (recursive_pattern
                    (property_pattern_clause
                      (subpattern
                        (identifier)
                        (constant_pattern
                          (boolean_literal)))
                      (subpattern
                        (identifier)
                        (constant_pattern
                          (null_literal)))))))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (recursive_pattern
              type: (identifier)
              (property_pattern_clause
                (subpattern
                  (member_access_expression
                    expression: (identifier)
                    name: (identifier))
                  (constant_pattern
                    (boolean_literal)))
                (subpattern
                  (member_access_expression
                    expression: (identifier)
                    name: (identifier))
                  (constant_pattern
                    (null_literal)))))))))))

================================================================================
Positional patterns
================================================================================

var a = p is var (x, y);
var c = p is (var x, var y) { x: 0 };

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (invocation_expression
            function: (is_expression
              left: (identifier)
              right: (implicit_type))
            arguments: (argument_list
              (argument
                (identifier))
              (argument
                (identifier))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (recursive_pattern
              (positional_pattern_clause
                (subpattern
                  (declaration_pattern
                    type: (implicit_type)
                    name: (identifier)))
                (subpattern
                  (declaration_pattern
                    type: (implicit_type)
                    name: (identifier))))
              (property_pattern_clause
                (subpattern
                  (identifier)
                  (constant_pattern
                    (integer_literal)))))))))))

================================================================================
Recursive patterns with variable designation (issue #282)
================================================================================

var x = expr is R(E.A) v0;
var y = expr is R(E.A or E.B) v1;
var z = expr is (E.A or E.B) v2;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (recursive_pattern
              type: (identifier)
              (positional_pattern_clause
                (subpattern
                  (type_pattern
                    type: (qualified_name
                      qualifier: (identifier)
                      name: (identifier)))))
              name: (identifier)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (recursive_pattern
              type: (identifier)
              (positional_pattern_clause
                (subpattern
                  (or_pattern
                    left: (type_pattern
                      type: (qualified_name
                        qualifier: (identifier)
                        name: (identifier)))
                    right: (constant_pattern
                      (member_access_expression
                        expression: (identifier)
                        name: (identifier))))))
              name: (identifier)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (recursive_pattern
              (or_pattern
                left: (constant_pattern
                  (member_access_expression
                    expression: (identifier)
                    name: (identifier)))
                right: (constant_pattern
                  (member_access_expression
                    expression: (identifier)
                    name: (identifier))))
              name: (identifier))))))))

================================================================================
Type patterns
================================================================================

var b = o is int or string; //is_pattern_expression with type_pattern
var c = o is int; //is_expression with type

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (or_pattern
              left: (type_pattern
                type: (predefined_type))
              right: (type_pattern
                type: (predefined_type))))))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_expression
            left: (identifier)
            right: (predefined_type))))))
  (comment))

================================================================================
List patterns
================================================================================

var a = p is [1,2,x,] and [] or [2,..];
if (aa is [(name: A.B), ..]) { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (is_pattern_expression
            expression: (identifier)
            pattern: (or_pattern
              left: (and_pattern
                left: (list_pattern
                  (constant_pattern
                    (integer_literal))
                  (constant_pattern
                    (integer_literal))
                  (constant_pattern
                    (identifier)))
                right: (list_pattern))
              right: (list_pattern
                (constant_pattern
                  (integer_literal)))))))))
  (global_statement
    (if_statement
      condition: (is_pattern_expression
        expression: (identifier)
        pattern: (list_pattern
          (recursive_pattern
            (positional_pattern_clause
              (subpattern
                (identifier)
                (constant_pattern
                  (member_access_expression
                    expression: (identifier)
                    name: (identifier))))))))
      consequence: (block))))

================================================================================
Conditional expression with member accesses
================================================================================

var a = b ? c.A + d.A : e.A + f.A;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_expression
            condition: (identifier)
            consequence: (binary_expression
              left: (member_access_expression
                expression: (identifier)
                name: (identifier))
              right: (member_access_expression
                expression: (identifier)
                name: (identifier)))
            alternative: (binary_expression
              left: (member_access_expression
                expression: (identifier)
                name: (identifier))
              right: (member_access_expression
                expression: (identifier)
                name: (identifier)))))))))

================================================================================
Conditional access expression
================================================================================

var a = b?.Something;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_access_expression
            condition: (identifier)
            (member_binding_expression
              name: (identifier))))))))

================================================================================
Conditional access to element (should be implicit_element_access)
================================================================================

var x = dict?["a"];

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_access_expression
            condition: (identifier)
            (element_binding_expression
              (argument
                (string_literal
                  (string_literal_content))))))))))

================================================================================
Conditional access expression with member binding
================================================================================

if (a?.B != 1) { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (if_statement
      condition: (binary_expression
        left: (conditional_access_expression
          condition: (identifier)
          (member_binding_expression
            name: (identifier)))
        right: (integer_literal))
      consequence: (block))))

================================================================================
Conditional access expression with simple member access
================================================================================

if ((p as Person[])?[0]._Age != 1) { }

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (if_statement
      condition: (binary_expression
        left: (member_access_expression
          expression: (conditional_access_expression
            condition: (parenthesized_expression
              (as_expression
                left: (identifier)
                right: (array_type
                  type: (identifier)
                  rank: (array_rank_specifier))))
            (element_binding_expression
              (argument
                (integer_literal))))
          name: (identifier))
        right: (integer_literal))
      consequence: (block))))

================================================================================
Null-coalescing operator is right-associative
================================================================================

var a = b ?? c ?? d;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (binary_expression
            left: (identifier)
            right: (binary_expression
              left: (identifier)
              right: (identifier))))))))

================================================================================
Precedence between null-coalescing operator and conditional OR
================================================================================

var a = b ?? c || d ?? e;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (binary_expression
            left: (identifier)
            right: (binary_expression
              left: (binary_expression
                left: (identifier)
                right: (identifier))
              right: (identifier))))))))

================================================================================
Precedence between null-coalescing operator and conditional operator
================================================================================

var a = b ?? c ? d ?? e : f ?? g;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_expression
            condition: (binary_expression
              left: (identifier)
              right: (identifier))
            consequence: (binary_expression
              left: (identifier)
              right: (identifier))
            alternative: (binary_expression
              left: (identifier)
              right: (identifier))))))))

================================================================================
Precedence between range and switch
================================================================================

var a = 3..4 switch
{
    _ => true
};

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (switch_expression
            (range_expression
              (integer_literal)
              (integer_literal))
            (switch_expression_arm
              (discard)
              (boolean_literal))))))))

================================================================================
Precedence between unary and switch
================================================================================

var a = -3 switch
{
    _ => true
};

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (switch_expression
            (prefix_unary_expression
              (integer_literal))
            (switch_expression_arm
              (discard)
              (boolean_literal))))))))

================================================================================
Precedence between range and as operator
================================================================================

var a = 3..4 as Range;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (as_expression
            left: (range_expression
              (integer_literal)
              (integer_literal))
            right: (identifier)))))))

================================================================================
Precedence between is and comparison operators
================================================================================

var allowedValuesList = someObj is null
    ? default
    : new object();

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (conditional_expression
            condition: (is_pattern_expression
              expression: (identifier)
              pattern: (constant_pattern
                (null_literal)))
            consequence: (default_expression)
            alternative: (object_creation_expression
              type: (predefined_type)
              arguments: (argument_list))))))))

================================================================================
Nameof expressions
================================================================================

var x = nameof(A);
var x = nameof(A<B>);
var x = nameof(A.B);

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (identifier))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (generic_name
                  (identifier)
                  (type_argument_list
                    (identifier))))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (invocation_expression
            function: (identifier)
            arguments: (argument_list
              (argument
                (member_access_expression
                  expression: (identifier)
                  name: (identifier))))))))))

================================================================================
Generic invocation expression
================================================================================

MyFunction<A,B>(1);

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (expression_statement
      (invocation_expression
        function: (generic_name
          (identifier)
          (type_argument_list
            (identifier)
            (identifier)))
        arguments: (argument_list
          (argument
            (integer_literal)))))))

================================================================================
Dereference versus logical and
================================================================================

bool c = (a) && b;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (cast_expression
            type: (identifier)
            value: (prefix_unary_expression
              (prefix_unary_expression
                (identifier)))))))))

================================================================================
With expression typical basic form
================================================================================

void A() {
  var newFriend = friend with { LastName = "Edwards" };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (with_expression
                (identifier)
                (with_initializer
                  (identifier)
                  (string_literal
                    (string_literal_content)))))))))))

================================================================================
With expression using expressions
================================================================================

void A() {
  var friend = GetAFriend() with {
      ForeName = RandomFirstName(),
      LastName = RandomLastName()
  };
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (with_expression
                (invocation_expression
                  function: (identifier)
                  arguments: (argument_list))
                (with_initializer
                  (identifier)
                  (invocation_expression
                    function: (identifier)
                    arguments: (argument_list)))
                (with_initializer
                  (identifier)
                  (invocation_expression
                    function: (identifier)
                    arguments: (argument_list)))))))))))

================================================================================
Precedence between with and cast
================================================================================

var x = (Point) p1 with {X = 3};

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (with_expression
            (cast_expression
              type: (identifier)
              value: (identifier))
            (with_initializer
              (identifier)
              (integer_literal))))))))

================================================================================
Precedence between with and switch
================================================================================

var x = p1 with {X = 3} switch { _ => 3 };

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (switch_expression
            (with_expression
              (identifier)
              (with_initializer
                (identifier)
                (integer_literal)))
            (switch_expression_arm
              (discard)
              (integer_literal))))))))

================================================================================
Precedence between with and equals
================================================================================

var x = p1 with {X = 3} == p1 with {X = 4};

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (binary_expression
            left: (with_expression
              (identifier)
              (with_initializer
                (identifier)
                (integer_literal)))
            right: (with_expression
              (identifier)
              (with_initializer
                (identifier)
                (integer_literal)))))))))

================================================================================
Associativity of with expression
================================================================================

var x = p1 with {X = 3} with {X = 4} with {X = 5};

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (with_expression
            (with_expression
              (with_expression
                (identifier)
                (with_initializer
                  (identifier)
                  (integer_literal)))
              (with_initializer
                (identifier)
                (integer_literal)))
            (with_initializer
              (identifier)
              (integer_literal))))))))

================================================================================
Array with trailing comma
================================================================================

var x = [ y, ];

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        (implicit_type)
        (variable_declarator
          (identifier)
          (element_binding_expression
            (argument
              (identifier))))))))
```

## File: `test/corpus/identifiers.txt`
```
================================================================================
Identifiers
================================================================================

int x = y;

// keyword names
int @var = @const;

// contextual keyword names
int nint = 0;
int nuint = 0;

// unicode identifiers
int under_score = 0;
int with1number = 0;
int varæble = 0;
int Переменная = 0;
int first‿letter = 0;
int ග්‍රහලෝකය = 0;
int _كوكبxxx = 0;

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (identifier)))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (identifier)))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal))))))
```

## File: `test/corpus/interfaces.txt`
```
================================================================================
Interfaces
================================================================================

public interface IOne: ITwo, IThree {
  byte Get { get; }
  char Set { set; }
  uint GetSet { get; set; }
  long SetGet { set; get; }

  void Nothing();
  int Output();
  void Input(string a);
  int InputOutput(string a);
};

// generic
private interface IOne<T1> : ITwo { }

// constraint
private interface IOne<T1> : ITwo where T1:T2 { }

private interface IOne<T1, T3> : ITwo where T1:T2 where T3:new() { }

namespace A {
  interface IOne : ITwo {
    event EventHandler<T> SomeEvent;

  bool this[int index] { get; set; }
  }
}


interface MyDefault {
  void Log(string message) {
    Console.WriteLine(message);
  }
}

public interface IGetNext<T> where T : IGetNext<T>
{
    static abstract T operator ++(T other);
}

private interface NoBody;

--------------------------------------------------------------------------------

(compilation_unit
  (interface_declaration
    (modifier)
    name: (identifier)
    (base_list
      (identifier)
      (identifier))
    body: (declaration_list
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier))))))
  (comment)
  (interface_declaration
    (modifier)
    name: (identifier)
    type_parameters: (type_parameter_list
      (type_parameter
        name: (identifier)))
    (base_list
      (identifier))
    body: (declaration_list))
  (comment)
  (interface_declaration
    (modifier)
    name: (identifier)
    type_parameters: (type_parameter_list
      (type_parameter
        name: (identifier)))
    (base_list
      (identifier))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier)))
    body: (declaration_list))
  (interface_declaration
    (modifier)
    name: (identifier)
    type_parameters: (type_parameter_list
      (type_parameter
        name: (identifier))
      (type_parameter
        name: (identifier)))
    (base_list
      (identifier))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        (constructor_constraint)))
    body: (declaration_list))
  (namespace_declaration
    name: (identifier)
    body: (declaration_list
      (interface_declaration
        name: (identifier)
        (base_list
          (identifier))
        body: (declaration_list
          (event_field_declaration
            (variable_declaration
              type: (generic_name
                (identifier)
                (type_argument_list
                  (identifier)))
              (variable_declarator
                name: (identifier))))
          (indexer_declaration
            type: (predefined_type)
            parameters: (bracketed_parameter_list
              (parameter
                type: (predefined_type)
                name: (identifier)))
            accessors: (accessor_list
              (accessor_declaration)
              (accessor_declaration)))))))
  (interface_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        body: (block
          (expression_statement
            (invocation_expression
              function: (member_access_expression
                expression: (identifier)
                name: (identifier))
              arguments: (argument_list
                (argument
                  (identifier)))))))))
  (interface_declaration
    (modifier)
    name: (identifier)
    type_parameters: (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (generic_name
          (identifier)
          (type_argument_list
            (identifier)))))
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))))))
  (interface_declaration
    (modifier)
    name: (identifier)))

```

## File: `test/corpus/literals.txt`
```
================================================================================
Literals
================================================================================

// integer

const int dec = 1_2;
const long hex = 0xf_1l;
const long hex2 = 0Xffff;
const long hex3 = 0x_0_f;
const UInt64 dec = 1uL;
const UInt16 bin = 0b0100_100;
const UInt16 bin2 = 0B01010__10;
const long bin3 = 0b_0_10;

// boolean

const bool t = true, u = false;

// char

const char c = 'a';
const char esc = '\n';
const char hex = '\xf09a';
const char hex2 = '\x9';
const char uni16 = '\ua0bf';
const char uni32 = '\UA0BFf9ca';

// real

const float s = 012.23F;
const float e = 1e6f;
const Single en = 0e-1f;
const Single ep = 1_1e+12f;
const double d = 0.9_9d;
const double e = .4_9d;
const decimal m = 0_1_2.9m;
const Decimal m2 = 102.349M;

// string

String e = "";
string s = "a";
string m = "abc";
string esc = "ab\"\t";
string hex = "ab\x22r";
string hex2 = "\x22r\x00";
string u16 = "\ub0d0ok";
string u32 = "\uF1D20ff0test";
string ve = @"";
string v = @"abcde\ef";
string quotes = @"<TestClass xmlns=""http://example.com/omg"" xmlns:i=""http://www.w3.org/2001/XMLSchema-instance""></TestClass>";
String e = @"This
is
a
multi-line";
string s = "//\n//";
string s = "\u0065/* \u0065 */\u0065";
string s = @"/* comment */";

// utf-8 string

var a = "lower"u8;
var b = "upper"U8;
var c = @"lower"u8;
var d = @"upper"U8;

string s = $"This contains {
  abc
} a newline";

// interpolated string

string s = $"hello";
string esc = $"ab\"\t";
string double = $"{{nope}}";
string s = $"\u0065/* \u0065 */\u0065";

string s = $"hello {name}, how are you?";
string s = $"hello {name:0.00}, how are you?";
string s = $"hello {name,25}, how are you?";
string s = $@"hello {name}, how are you?";
string s = $@"hello {name:g}, how are you?";
string s = $@"hello {name,-10}, how are you?";

string s = $@"hello";
string s = @$"hello";

var s = $@"Another
multiple
line";

string s = $@"
class A
{{
    bool Method(int value)
    {{
        return value  is  {operatorText}  3  or  {operatorText}  5;
    }}
}}
";
string s = $@"{a}/* comment */{a}";
var x = $@"/* {world} */";

// raw string

var x = """Hello""";
var x = """
  Hello
  """;
var x = """
  ""Hello"" "there"
  """u8;

var x = $"""The point "{X}, {Y}" is
         ""{Math.Sqrt(X * X + Y * Y)}"" from the origin
         """;

var x = $"{{";

var x = $"""{bar}""";

var x = """"baz"""";

var x = $""""
    [||]
    """
"""";

var x = $@" ""hi"" ";
var x = @$"""Hello"" {world}!";

var s = $$"""
{{ $" { 1 } " }}
""";

--------------------------------------------------------------------------------

(compilation_unit
  (comment)
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (comment)
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (boolean_literal))
        (variable_declarator
          name: (identifier)
          (boolean_literal)))))
  (comment)
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (character_literal
            (character_literal_content))))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (character_literal
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (character_literal
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (character_literal
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (character_literal
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (character_literal
            (escape_sequence))))))
  (comment)
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (global_statement
    (local_declaration_statement
      (modifier)
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (real_literal)))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (string_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content)
            (escape_sequence)
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content)
            (escape_sequence)
            (string_literal_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (escape_sequence)
            (string_literal_content)
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (escape_sequence)
            (string_literal_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (escape_sequence)
            (string_literal_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (verbatim_string_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (verbatim_string_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (verbatim_string_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (identifier)
        (variable_declarator
          name: (identifier)
          (verbatim_string_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content)
            (escape_sequence)
            (string_literal_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (escape_sequence)
            (string_literal_content)
            (escape_sequence)
            (string_literal_content)
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (verbatim_string_literal)))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content)
            (string_literal_encoding))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content)
            (string_literal_encoding))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (verbatim_string_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (verbatim_string_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content))))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (escape_sequence)
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (escape_sequence)
            (string_content)
            (escape_sequence)
            (string_content)
            (escape_sequence))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_format_clause)
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_alignment_clause
                (integer_literal))
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_format_clause)
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_alignment_clause
                (prefix_unary_expression
                  (integer_literal)))
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (string_content)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content))))))
  (comment)
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (raw_string_literal
            (raw_string_start)
            (raw_string_content)
            (raw_string_end))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (raw_string_literal
            (raw_string_start)
            (raw_string_content)
            (raw_string_end))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (raw_string_literal
            (raw_string_start)
            (raw_string_content)
            (raw_string_end))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (interpolation_quote)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content)
            (interpolation
              (interpolation_brace)
              (invocation_expression
                function: (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                arguments: (argument_list
                  (argument
                    (binary_expression
                      left: (binary_expression
                        left: (identifier)
                        right: (identifier))
                      right: (binary_expression
                        left: (identifier)
                        right: (identifier))))))
              (interpolation_brace))
            (string_content)
            (interpolation_quote))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (interpolation_quote)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (interpolation_quote))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (raw_string_literal
            (raw_string_start)
            (raw_string_content)
            (raw_string_end))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (interpolation_quote)
            (string_content)
            (interpolation_quote))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (string_content)
            (interpolation
              (interpolation_brace)
              (identifier)
              (interpolation_brace))
            (string_content))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (interpolated_string_expression
            (interpolation_start)
            (interpolation_quote)
            (string_content)
            (interpolation
              (interpolation_brace)
              (interpolated_string_expression
                (interpolation_start)
                (string_content)
                (interpolation
                  (interpolation_brace)
                  (integer_literal)
                  (interpolation_brace))
                (string_content))
              (interpolation_brace))
            (string_content)
            (interpolation_quote)))))))
```

## File: `test/corpus/preprocessor.txt`
```
================================================================================
If, elif and else directives
================================================================================

#if WIN32
  string os = "Win32";
#elif MACOS
  string os = "MacOS";
#else
  string os = "Unknown";
#endif

--------------------------------------------------------------------------------

(compilation_unit
  (preproc_if
    condition: (identifier)
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (string_literal
            (string_literal_content)))))
    alternative: (preproc_elif
      condition: (identifier)
      (local_declaration_statement
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier)
            (string_literal
              (string_literal_content)))))
      alternative: (preproc_else
        (local_declaration_statement
          (variable_declaration
            type: (predefined_type)
            (variable_declarator
              name: (identifier)
              (string_literal
                (string_literal_content)))))))))

================================================================================
If conditions
================================================================================

#if !MACOS
#endif

#if WIN32==true
#endif

#if !MACOS!=false
#endif

#if A && B || C
#endif

#if (A)
#endif

#if (A || B)
#endif

#if (A && B) || C
#endif

--------------------------------------------------------------------------------

(compilation_unit
  (preproc_if
    condition: (unary_expression
      argument: (identifier)))
  (preproc_if
    condition: (binary_expression
      left: (identifier)
      right: (boolean_literal)))
  (preproc_if
    condition: (binary_expression
      left: (unary_expression
        argument: (identifier))
      right: (boolean_literal)))
  (preproc_if
    condition: (binary_expression
      left: (binary_expression
        left: (identifier)
        right: (identifier))
      right: (identifier)))
  (preproc_if
    condition: (parenthesized_expression
      (identifier)))
  (preproc_if
    condition: (parenthesized_expression
      (binary_expression
        left: (identifier)
        right: (identifier))))
  (preproc_if
    condition: (binary_expression
      left: (parenthesized_expression
        (binary_expression
          left: (identifier)
          right: (identifier)))
      right: (identifier))))

================================================================================
Define and undefine directives
================================================================================

#define SOMETHING
#undef BAD

--------------------------------------------------------------------------------

(compilation_unit
  (preproc_define
    (preproc_arg))
  (preproc_undef
    (preproc_arg)))

================================================================================
Line directives
================================================================================

class Of1879 {
  void AMethod() {
#line 2001 "A Space" // Comment
#line hidden
#line default
#line (1, 1) - (1, 3) 1 "a.cs"
#line (2, 1) - (2, 3) "a.cs"
# line 2001 "A Space"
#  line hidden
#    line default
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (preproc_line
            (integer_literal)
            (string_literal
              (string_literal_content))
            (comment))
          (preproc_line)
          (preproc_line)
          (preproc_line
            (integer_literal)
            (integer_literal)
            (integer_literal)
            (integer_literal)
            (integer_literal)
            (string_literal
              (string_literal_content)))
          (preproc_line
            (integer_literal)
            (integer_literal)
            (integer_literal)
            (integer_literal)
            (string_literal
              (string_literal_content)))
          (preproc_line
            (integer_literal)
            (string_literal
              (string_literal_content)))
          (preproc_line)
          (preproc_line))))))

================================================================================
Directives not in strings or comments
================================================================================

class Of1879 {
  void AMethod() {
    var s = @"Only a string
    #if NOPE
";
    /* Only a comment
    #if NOPE
    */
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (verbatim_string_literal))))
          (comment))))))

================================================================================
Shebang directive
================================================================================

#!/usr/bin/env scriptcs

--------------------------------------------------------------------------------

(compilation_unit
  (shebang_directive))
```

## File: `test/corpus/query-syntax.txt`
```
================================================================================
Query from select
================================================================================

var x = from a in source select a.B() ? c : c * 2;

var x = from a in source select somevar = a;

var x = from a in source select new { Name = a.B };

var x = from a in source
  where a.B == "A"
  select new { Name = a.B };

var x = from a in source
  orderby a.A descending
  orderby a.C ascending
  orderby 1
  select a;

var x = from a in source
  let z = new { a.A, a.B }
  select z;

var x = from a in sourceA
  join b in sourceB on a.FK equals b.PK
  select new { A.A, B.B };

var x = from a in sourceA
  from b in sourceB
  where a.FK == b.FK
  select new { A.A, B.B };

var x = from a in sourceA
  group a by a.Country into g
  select new { Country = g.Key, Population = g.Sum(p => p.Population) };


--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (select_clause
              (conditional_expression
                condition: (invocation_expression
                  function: (member_access_expression
                    expression: (identifier)
                    name: (identifier))
                  arguments: (argument_list))
                consequence: (identifier)
                alternative: (binary_expression
                  left: (identifier)
                  right: (integer_literal)))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (select_clause
              (assignment_expression
                left: (identifier)
                right: (identifier))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (select_clause
              (anonymous_object_creation_expression
                (identifier)
                (member_access_expression
                  expression: (identifier)
                  name: (identifier)))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (where_clause
              (binary_expression
                left: (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                right: (string_literal
                  (string_literal_content))))
            (select_clause
              (anonymous_object_creation_expression
                (identifier)
                (member_access_expression
                  expression: (identifier)
                  name: (identifier)))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (order_by_clause
              (member_access_expression
                expression: (identifier)
                name: (identifier)))
            (order_by_clause
              (member_access_expression
                expression: (identifier)
                name: (identifier)))
            (order_by_clause
              (integer_literal))
            (select_clause
              (identifier)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (let_clause
              (identifier)
              (anonymous_object_creation_expression
                (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                (member_access_expression
                  expression: (identifier)
                  name: (identifier))))
            (select_clause
              (identifier)))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (join_clause
              (identifier)
              (identifier)
              (member_access_expression
                expression: (identifier)
                name: (identifier))
              (member_access_expression
                expression: (identifier)
                name: (identifier)))
            (select_clause
              (anonymous_object_creation_expression
                (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                (member_access_expression
                  expression: (identifier)
                  name: (identifier)))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (from_clause
              name: (identifier)
              (identifier))
            (where_clause
              (binary_expression
                left: (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                right: (member_access_expression
                  expression: (identifier)
                  name: (identifier))))
            (select_clause
              (anonymous_object_creation_expression
                (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                (member_access_expression
                  expression: (identifier)
                  name: (identifier)))))))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (query_expression
            (from_clause
              name: (identifier)
              (identifier))
            (group_clause
              (identifier)
              (member_access_expression
                expression: (identifier)
                name: (identifier)))
            (identifier)
            (select_clause
              (anonymous_object_creation_expression
                (identifier)
                (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                (identifier)
                (invocation_expression
                  function: (member_access_expression
                    expression: (identifier)
                    name: (identifier))
                  arguments: (argument_list
                    (argument
                      (lambda_expression
                        parameters: (implicit_parameter)
                        body: (member_access_expression
                          expression: (identifier)
                          name: (identifier))))))))))))))
```

## File: `test/corpus/records.txt`
```
================================================================================
Basic record declaration
================================================================================

record F {
  int Age { get; init; }
}

record struct F {
  int Age { get; init; }
}

record class F {
  int Age { get; init; }
}

public record F<T> where T:struct {}

public record F<T> where T: new() {}

public record A : ISomething { }

[Test]
private record F<T1,T2> where T1 : I1, I2, new() where T2 : I2 { }

record Person(string FirstName, string LastName);

record Teacher(string FirstName, string LastName, string Subject) : Person(FirstName, LastName);

record Teacher(string FirstName, string LastName, string Subject) : Person(FirstName, LastName), Ns.I1, I2;

record Teacher() : Entity<Person>(), I1;

public record Person { };

public record struct Person2 { };

record NoBody;

--------------------------------------------------------------------------------

(compilation_unit
  (record_declaration
    name: (identifier)
    body: (declaration_list
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))))
  (record_declaration
    name: (identifier)
    body: (declaration_list
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))))
  (record_declaration
    name: (identifier)
    body: (declaration_list
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))))
  (record_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint))
    body: (declaration_list))
  (record_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        (constructor_constraint)))
    body: (declaration_list))
  (record_declaration
    (modifier)
    name: (identifier)
    (base_list
      (identifier))
    body: (declaration_list))
  (record_declaration
    (attribute_list
      (attribute
        name: (identifier)))
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier))
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier))
      (type_parameter_constraint
        type: (identifier))
      (type_parameter_constraint
        (constructor_constraint)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier)))
    body: (declaration_list))
  (record_declaration
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier))))
  (record_declaration
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier)))
    (base_list
      (primary_constructor_base_type
        type: (identifier)
        (argument_list
          (argument
            (identifier))
          (argument
            (identifier))))))
  (record_declaration
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier))
      (parameter
        type: (predefined_type)
        name: (identifier)))
    (base_list
      (primary_constructor_base_type
        type: (identifier)
        (argument_list
          (argument
            (identifier))
          (argument
            (identifier))))
      (qualified_name
        qualifier: (identifier)
        name: (identifier))
      (identifier)))
  (record_declaration
    name: (identifier)
    (parameter_list)
    (base_list
      (primary_constructor_base_type
        type: (generic_name
          (identifier)
          (type_argument_list
            (identifier)))
        (argument_list))
      (identifier)))
  (record_declaration
    (modifier)
    name: (identifier)
    body: (declaration_list))
  (record_declaration
    (modifier)
    name: (identifier)
    body: (declaration_list))
  (record_declaration
    name: (identifier)))
```

## File: `test/corpus/source-file-structure.txt`
```
================================================================================
Using directives, extern alias, and namespace declarations
================================================================================

global using A;
global using static A.B;

using A;
using B.C;
using global::E.F;
using G = H.I;
using static J.K;

using Point = (int x, int y);

extern alias A;

namespace Foo {
  using A;
}

namespace A {
  namespace B.C.D {
  }

  namespace E.F {
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (using_directive
    (identifier))
  (using_directive
    (qualified_name
      (identifier)
      (identifier)))
  (using_directive
    (identifier))
  (using_directive
    (qualified_name
      (identifier)
      (identifier)))
  (using_directive
    (qualified_name
      (alias_qualified_name
        (identifier)
        (identifier))
      (identifier)))
  (using_directive
    (identifier)
    (qualified_name
      (identifier)
      (identifier)))
  (using_directive
    (qualified_name
      (identifier)
      (identifier)))
  (using_directive
    (identifier)
    (tuple_type
      (tuple_element
        (predefined_type)
        (identifier))
      (tuple_element
        (predefined_type)
        (identifier))))
  (extern_alias_directive
    (identifier))
  (namespace_declaration
    (identifier)
    (declaration_list
      (using_directive
        (identifier))))
  (namespace_declaration
    (identifier)
    (declaration_list
      (namespace_declaration
        (qualified_name
          (qualified_name
            (identifier)
            (identifier))
          (identifier))
        (declaration_list))
      (namespace_declaration
        (qualified_name
          (identifier)
          (identifier))
        (declaration_list)))))

================================================================================
File scoped namespaces
================================================================================

namespace A;

class B {
}

--------------------------------------------------------------------------------

(compilation_unit
  (file_scoped_namespace_declaration
    name: (identifier))
  (class_declaration
    name: (identifier)
    body: (declaration_list)))

================================================================================
Delegates
================================================================================

public delegate int Global(ref char a = '\n');
public delegate ref int Global(ref char a = '\n');
public delegate ref readonly int Global(ref char a = '\n');

delegate void A<T>() where T:class;

delegate void A(params int [] test);

class Z {
  delegate void Zed();
}

--------------------------------------------------------------------------------

(compilation_unit
  (delegate_declaration
    (modifier)
    type: (predefined_type)
    name: (identifier)
    parameters: (parameter_list
      (parameter
        (modifier)
        type: (predefined_type)
        name: (identifier)
        (character_literal
          (escape_sequence)))))
  (delegate_declaration
    (modifier)
    type: (ref_type
      type: (predefined_type))
    name: (identifier)
    parameters: (parameter_list
      (parameter
        (modifier)
        type: (predefined_type)
        name: (identifier)
        (character_literal
          (escape_sequence)))))
  (delegate_declaration
    (modifier)
    type: (ref_type
      type: (predefined_type))
    name: (identifier)
    parameters: (parameter_list
      (parameter
        (modifier)
        type: (predefined_type)
        name: (identifier)
        (character_literal
          (escape_sequence)))))
  (delegate_declaration
    type: (predefined_type)
    name: (identifier)
    type_parameters: (type_parameter_list
      (type_parameter
        name: (identifier)))
    parameters: (parameter_list)
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint)))
  (delegate_declaration
    type: (predefined_type)
    name: (identifier)
    parameters: (parameter_list
      type: (array_type
        type: (predefined_type)
        rank: (array_rank_specifier))
      name: (identifier)))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (delegate_declaration
        type: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)))))
```

## File: `test/corpus/statements.txt`
```
================================================================================
Common statements
================================================================================

(string a, bool b) c = default;
A<B> a = null;
int x = 0;
(x, int y) = point;
var result = list.Select(c => (c.f1, c.f2)).Where(t => t.f2 == 1);

class A {
  int Sample() {
    return 1;
  }

  void Sample2() {
    return;
  }

  void Sample3() {
    while (true) break;
    while (false) continue;
  }

  void Sample4() {
    throw;
    throw ex;
  }

  void Sample5() {
    do { } while (true);
  }

  void Sample6() {
    goto end;
    end:
      return;
  }

  int Sample7() {
    if (true) return 1;
    else return 0;
  }

  int Sample8() {
    switch (1) {
      case 1:
      case 2:
        return 1;
      default:
        return 0;
    }
  }

  M(out (int a, int b) c);

  void M() {
    (bool a, bool b) M2() {
      return (true, false);
    }
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (tuple_type
          (tuple_element
            type: (predefined_type)
            name: (identifier))
          (tuple_element
            type: (predefined_type)
            name: (identifier)))
        (variable_declarator
          name: (identifier)
          (default_expression)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (generic_name
          (identifier)
          (type_argument_list
            (identifier)))
        (variable_declarator
          name: (identifier)
          (null_literal)))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (predefined_type)
        (variable_declarator
          name: (identifier)
          (integer_literal)))))
  (global_statement
    (expression_statement
      (assignment_expression
        left: (tuple_expression
          (argument
            (identifier))
          (argument
            (declaration_expression
              type: (predefined_type)
              name: (identifier))))
        right: (identifier))))
  (global_statement
    (local_declaration_statement
      (variable_declaration
        type: (implicit_type)
        (variable_declarator
          name: (identifier)
          (invocation_expression
            function: (member_access_expression
              expression: (invocation_expression
                function: (member_access_expression
                  expression: (identifier)
                  name: (identifier))
                arguments: (argument_list
                  (argument
                    (lambda_expression
                      parameters: (implicit_parameter)
                      body: (tuple_expression
                        (argument
                          (member_access_expression
                            expression: (identifier)
                            name: (identifier)))
                        (argument
                          (member_access_expression
                            expression: (identifier)
                            name: (identifier))))))))
              name: (identifier))
            arguments: (argument_list
              (argument
                (lambda_expression
                  parameters: (implicit_parameter)
                  body: (binary_expression
                    left: (member_access_expression
                      expression: (identifier)
                      name: (identifier))
                    right: (integer_literal))))))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement
            (integer_literal))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (return_statement)))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (while_statement
            condition: (boolean_literal)
            body: (break_statement))
          (while_statement
            condition: (boolean_literal)
            body: (continue_statement))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (throw_statement)
          (throw_statement
            (identifier))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (do_statement
            body: (block)
            condition: (boolean_literal))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (goto_statement
            (identifier))
          (labeled_statement
            (identifier)
            (return_statement))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (if_statement
            condition: (boolean_literal)
            consequence: (return_statement
              (integer_literal))
            alternative: (return_statement
              (integer_literal)))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (switch_statement
            value: (integer_literal)
            body: (switch_body
              (switch_section
                (constant_pattern
                  (integer_literal)))
              (switch_section
                (constant_pattern
                  (integer_literal))
                (return_statement
                  (integer_literal)))
              (switch_section
                (return_statement
                  (integer_literal)))))))
      (constructor_declaration
        name: (identifier)
        parameters: (parameter_list
          (parameter
            (modifier)
            type: (tuple_type
              (tuple_element
                type: (predefined_type)
                name: (identifier))
              (tuple_element
                type: (predefined_type)
                name: (identifier)))
            name: (identifier))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (local_function_statement
            type: (tuple_type
              (tuple_element
                type: (predefined_type)
                name: (identifier))
              (tuple_element
                type: (predefined_type)
                name: (identifier)))
            name: (identifier)
            parameters: (parameter_list)
            body: (block
              (return_statement
                (tuple_expression
                  (argument
                    (boolean_literal))
                  (argument
                    (boolean_literal)))))))))))

================================================================================
Switch statements
================================================================================

int Sample9(int a) {
  switch (a, a) {
    case (1, 1):
      return 1;
    default:
      return 0;
  }

  switch (A, B) {
      case (_, _) when !c:
        break;
  }

  switch (A) {
      case {Length: 2} when !c:
        break;
  }

  int i = 123;
  switch (i)
  {
      case int when i < 5:
          break;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      (predefined_type)
      (identifier)
      (parameter_list
        (parameter
          (predefined_type)
          (identifier)))
      (block
        (switch_statement
          (tuple_expression
            (argument
              (identifier))
            (argument
              (identifier)))
          (switch_body
            (switch_section
              (constant_pattern
                (tuple_expression
                  (argument
                    (integer_literal))
                  (argument
                    (integer_literal))))
              (return_statement
                (integer_literal)))
            (switch_section
              (return_statement
                (integer_literal)))))
        (switch_statement
          (tuple_expression
            (argument
              (identifier))
            (argument
              (identifier)))
          (switch_body
            (switch_section
              (recursive_pattern
                (positional_pattern_clause
                  (subpattern
                    (discard))
                  (subpattern
                    (discard))))
              (when_clause
                (prefix_unary_expression
                  (identifier)))
              (break_statement))))
        (switch_statement
          (identifier)
          (switch_body
            (switch_section
              (recursive_pattern
                (property_pattern_clause
                  (subpattern
                    (identifier)
                    (constant_pattern
                      (integer_literal)))))
              (when_clause
                (prefix_unary_expression
                  (identifier)))
              (break_statement))))
        (local_declaration_statement
          (variable_declaration
            (predefined_type)
            (variable_declarator
              (identifier)
              (integer_literal))))
        (switch_statement
          (identifier)
          (switch_body
            (switch_section
              (type_pattern
                (predefined_type))
              (when_clause
                (binary_expression
                  (identifier)
                  (integer_literal)))
              (break_statement))))))))

================================================================================
Try catch finally statements
================================================================================

class A {
  void Sample() {
    try {
    } finally {
    }

    try {
    } catch (Exception ex) {
    }

    try {
    } catch (Exception ex) {
    } finally {
    }

    try {
    } catch (Exception ex) {
    } catch (OtherException ex) {
    }

    try {
    } catch (Exception ex) when (a == 1) {
    }
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (try_statement
            body: (block)
            (finally_clause
              (block)))
          (try_statement
            body: (block)
            (catch_clause
              (catch_declaration
                type: (identifier)
                name: (identifier))
              body: (block)))
          (try_statement
            body: (block)
            (catch_clause
              (catch_declaration
                type: (identifier)
                name: (identifier))
              body: (block))
            (finally_clause
              (block)))
          (try_statement
            body: (block)
            (catch_clause
              (catch_declaration
                type: (identifier)
                name: (identifier))
              body: (block))
            (catch_clause
              (catch_declaration
                type: (identifier)
                name: (identifier))
              body: (block)))
          (try_statement
            body: (block)
            (catch_clause
              (catch_declaration
                type: (identifier)
                name: (identifier))
              (catch_filter_clause
                (binary_expression
                  left: (identifier)
                  right: (integer_literal)))
              body: (block))))))))

================================================================================
Checked, unchecked, locked, & yield statements
================================================================================

class A {
  void Sample() {
    checked {
      return;
    }

    unchecked {
      return;
    }

    lock (this) {
      return;
    }

    yield return 1;
    yield break;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (checked_statement
            (block
              (return_statement)))
          (checked_statement
            (block
              (return_statement)))
          (lock_statement
            (block
              (return_statement)))
          (yield_statement
            (integer_literal))
          (yield_statement))))))

================================================================================
Initializers
================================================================================

class A {
  void Sample() {
    int a;
    int a = 1, b = 2;
    const int a = 1;
    const int a = 1, b = 2;
    ref var value = ref data[i];
    var g = args[0].Length;

    numbers ??= new List<int>();
    b = obj ?? a == 0;

    person = new Person(null!, null!);

    MyClass myVar = MyFunction<MyOtherClass>("MyArg");
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (local_declaration_statement
            (variable_declaration
              type: (predefined_type)
              (variable_declarator
                name: (identifier))))
          (local_declaration_statement
            (variable_declaration
              type: (predefined_type)
              (variable_declarator
                name: (identifier)
                (integer_literal))
              (variable_declarator
                name: (identifier)
                (integer_literal))))
          (local_declaration_statement
            (modifier)
            (variable_declaration
              type: (predefined_type)
              (variable_declarator
                name: (identifier)
                (integer_literal))))
          (local_declaration_statement
            (modifier)
            (variable_declaration
              type: (predefined_type)
              (variable_declarator
                name: (identifier)
                (integer_literal))
              (variable_declarator
                name: (identifier)
                (integer_literal))))
          (local_declaration_statement
            (variable_declaration
              type: (ref_type
                type: (implicit_type))
              (variable_declarator
                name: (identifier)
                (ref_expression
                  (element_access_expression
                    expression: (identifier)
                    subscript: (bracketed_argument_list
                      (argument
                        (identifier))))))))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (member_access_expression
                  expression: (element_access_expression
                    expression: (identifier)
                    subscript: (bracketed_argument_list
                      (argument
                        (integer_literal))))
                  name: (identifier)))))
          (expression_statement
            (assignment_expression
              left: (identifier)
              right: (object_creation_expression
                type: (generic_name
                  (identifier)
                  (type_argument_list
                    (predefined_type)))
                arguments: (argument_list))))
          (expression_statement
            (assignment_expression
              left: (identifier)
              right: (binary_expression
                left: (identifier)
                right: (binary_expression
                  left: (identifier)
                  right: (integer_literal)))))
          (expression_statement
            (assignment_expression
              left: (identifier)
              right: (object_creation_expression
                type: (identifier)
                arguments: (argument_list
                  (argument
                    (postfix_unary_expression
                      (null_literal)))
                  (argument
                    (postfix_unary_expression
                      (null_literal)))))))
          (local_declaration_statement
            (variable_declaration
              type: (identifier)
              (variable_declarator
                name: (identifier)
                (invocation_expression
                  function: (generic_name
                    (identifier)
                    (type_argument_list
                      (identifier)))
                  arguments: (argument_list
                    (argument
                      (string_literal
                        (string_literal_content)))))))))))))

================================================================================
Using statements
================================================================================

class A {
  void Sample() {
    using (var a = b) {
      return;
    }

    using (Stream a = File.OpenRead("a"), b = new BinaryReader(a)) {
      return;
    }

    using var a = new A();

    using (Object a = b) {
      return;
    }

    using (this) {
      return;
    }
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (using_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (identifier)))
            body: (block
              (return_statement)))
          (using_statement
            (variable_declaration
              type: (identifier)
              (variable_declarator
                name: (identifier)
                (invocation_expression
                  function: (member_access_expression
                    expression: (identifier)
                    name: (identifier))
                  arguments: (argument_list
                    (argument
                      (string_literal
                        (string_literal_content))))))
              (variable_declarator
                name: (identifier)
                (object_creation_expression
                  type: (identifier)
                  arguments: (argument_list
                    (argument
                      (identifier))))))
            body: (block
              (return_statement)))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                name: (identifier)
                (object_creation_expression
                  type: (identifier)
                  arguments: (argument_list)))))
          (using_statement
            (variable_declaration
              type: (identifier)
              (variable_declarator
                name: (identifier)
                (identifier)))
            body: (block
              (return_statement)))
          (using_statement
            body: (block
              (return_statement))))))))

================================================================================
Loops
================================================================================

class A {
  void Sample() {
    foreach(int x in y)
      z += x;

    foreach(x in y)
      z += x;

    foreach(var (x, y) in z)
      q += x;

    for(int x = 0; x < 100; x++) {
      z += x;
    }

    for(;;) {
    }
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (foreach_statement
            type: (predefined_type)
            left: (identifier)
            right: (identifier)
            body: (expression_statement
              (assignment_expression
                left: (identifier)
                right: (identifier))))
          (foreach_statement
            left: (identifier)
            right: (identifier)
            body: (expression_statement
              (assignment_expression
                left: (identifier)
                right: (identifier))))
          (foreach_statement
            type: (implicit_type)
            left: (tuple_pattern
              name: (identifier)
              name: (identifier))
            right: (identifier)
            body: (expression_statement
              (assignment_expression
                left: (identifier)
                right: (identifier))))
          (for_statement
            initializer: (variable_declaration
              type: (predefined_type)
              (variable_declarator
                name: (identifier)
                (integer_literal)))
            condition: (binary_expression
              left: (identifier)
              right: (integer_literal))
            update: (postfix_unary_expression
              (identifier))
            body: (block
              (expression_statement
                (assignment_expression
                  left: (identifier)
                  right: (identifier)))))
          (for_statement
            body: (block)))))))

================================================================================
Unsafe & fixed statements
================================================================================

class A {
  void Sample() {
    unsafe { x = y; }
    fixed (double p = arr) { }
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (unsafe_statement
            (block
              (expression_statement
                (assignment_expression
                  left: (identifier)
                  right: (identifier)))))
          (fixed_statement
            (variable_declaration
              type: (predefined_type)
              (variable_declarator
                name: (identifier)
                (identifier)))
            (block)))))))

================================================================================
Deconstruction
================================================================================

class A {
  void Sample() {
    (var a, var b) = c;
    var (a, b) = c;
    (a, b, _) = c;
    (_, b) = c;
    var (a, _) = c;
    var (a, (b, _)) = c;
  }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list)
        body: (block
          (expression_statement
            (assignment_expression
              left: (tuple_expression
                (argument
                  (declaration_expression
                    type: (implicit_type)
                    name: (identifier)))
                (argument
                  (declaration_expression
                    type: (implicit_type)
                    name: (identifier))))
              right: (identifier)))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                (tuple_pattern
                  name: (identifier)
                  name: (identifier))
                (identifier))))
          (expression_statement
            (assignment_expression
              left: (tuple_expression
                (argument
                  (identifier))
                (argument
                  (identifier))
                (argument
                  (identifier)))
              right: (identifier)))
          (expression_statement
            (assignment_expression
              left: (tuple_expression
                (argument
                  (identifier))
                (argument
                  (identifier)))
              right: (identifier)))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                (tuple_pattern
                  name: (identifier)
                  (discard))
                (identifier))))
          (local_declaration_statement
            (variable_declaration
              type: (implicit_type)
              (variable_declarator
                (tuple_pattern
                  name: (identifier)
                  (tuple_pattern
                    name: (identifier)
                    (discard)))
                (identifier)))))))))

================================================================================
Function with contextually reserved identifiers
================================================================================

async void Sample() {
  var var = "";
  int partial = from;
  A into = select;
  R await = get;
  T set = let + yield + group + add + alias + ascending + notnull + descending + equals;
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      (modifier)
      type: (predefined_type)
      name: (identifier)
      parameters: (parameter_list)
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (implicit_type)
            (variable_declarator
              name: (identifier)
              (string_literal))))
        (local_declaration_statement
          (variable_declaration
            type: (predefined_type)
            (variable_declarator
              name: (identifier)
              (identifier))))
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (identifier))))
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (identifier))))
        (local_declaration_statement
          (variable_declaration
            type: (identifier)
            (variable_declarator
              name: (identifier)
              (binary_expression
                left: (binary_expression
                  left: (binary_expression
                    left: (binary_expression
                      left: (binary_expression
                        left: (binary_expression
                          left: (binary_expression
                            left: (binary_expression
                              left: (identifier)
                              right: (identifier))
                            right: (identifier))
                          right: (identifier))
                        right: (identifier))
                      right: (identifier))
                    right: (identifier))
                  right: (identifier))
                right: (identifier)))))))))

================================================================================
Function conditional ref expression
================================================================================

ref T Choice(bool condition, ref T a, ref T b)
{
  ref var r = ref (condition ? ref a: ref b);
}

--------------------------------------------------------------------------------

(compilation_unit
  (global_statement
    (local_function_statement
      type: (ref_type
        type: (identifier))
      name: (identifier)
      parameters: (parameter_list
        (parameter
          type: (predefined_type)
          name: (identifier))
        (parameter
          (modifier)
          type: (identifier)
          name: (identifier))
        (parameter
          (modifier)
          type: (identifier)
          name: (identifier)))
      body: (block
        (local_declaration_statement
          (variable_declaration
            type: (ref_type
              type: (implicit_type))
            (variable_declarator
              name: (identifier)
              (ref_expression
                (parenthesized_expression
                  (conditional_expression
                    condition: (identifier)
                    consequence: (ref_expression
                      (identifier))
                    alternative: (ref_expression
                      (identifier))))))))))))
```

## File: `test/corpus/structs.txt`
```
================================================================================
Struct with a type parameter struct constraint
================================================================================

public struct F<T> where T:struct {}

public struct F<T> where T: new() {}

readonly public struct A : ISomething { }

private struct F<T1,T2> where T1 : I1, I2, new() where T2 : I2 { }

ref struct Test { }

struct NoBody;

private struct NoBodyWithPrimary(int g);
--------------------------------------------------------------------------------

(compilation_unit
  (struct_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint))
    body: (declaration_list))
  (struct_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        (constructor_constraint)))
    body: (declaration_list))
  (struct_declaration
    (modifier)
    (modifier)
    name: (identifier)
    (base_list
      (identifier))
    body: (declaration_list))
  (struct_declaration
    (modifier)
    name: (identifier)
    (type_parameter_list
      (type_parameter
        name: (identifier))
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier))
      (type_parameter_constraint
        type: (identifier))
      (type_parameter_constraint
        (constructor_constraint)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (identifier)))
    body: (declaration_list))
  (struct_declaration
    name: (identifier)
    body: (declaration_list))
  (struct_declaration
    name: (identifier))
  (struct_declaration
    (modifier)
    name: (identifier)
    (parameter_list
      (parameter
        type: (predefined_type)
        name: (identifier)))))
```

## File: `test/corpus/type-events.txt`
```
================================================================================
Class event declarations
================================================================================

class A {
  public event EventHandler<T> SomeEvent { add { } remove { } }
}

struct A {
  public event EventHandler<T> SomeEvent { add { } remove { } }
}

class A {
  public event EventHandler SomeEvent { add => addSomething(); remove => removeSomething(); }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (event_declaration
        (modifier)
        type: (generic_name
          (identifier)
          (type_argument_list
            (identifier)))
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (block))
          (accessor_declaration
            body: (block))))))
  (struct_declaration
    name: (identifier)
    body: (declaration_list
      (event_declaration
        (modifier)
        type: (generic_name
          (identifier)
          (type_argument_list
            (identifier)))
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (block))
          (accessor_declaration
            body: (block))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (event_declaration
        (modifier)
        type: (identifier)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (arrow_expression_clause
              (invocation_expression
                function: (identifier)
                arguments: (argument_list))))
          (accessor_declaration
            body: (arrow_expression_clause
              (invocation_expression
                function: (identifier)
                arguments: (argument_list)))))))))
```

## File: `test/corpus/type-fields.txt`
```
================================================================================
Class field declarations
================================================================================

class A {
  public readonly int _B;
  Int64 D_e_f, g;
  Tuple<char, Nullable<int>> z;

  public readonly int? i;
  private Byte? b;

  public readonly int* i;
  private Byte* b;
  private void* c;

  // Function pointer equivalent without calling convention
  delegate*<string, int> a;
  delegate*<delegate*<in string, int>, delegate*<ref string, ref readonly int>> b;

  // Function pointer equivalent with calling convention
  delegate* managed<string, int> c;
  delegate*<delegate* unmanaged[MyCallConv, YourCallConv]<string, int>, delegate*<string, int>> d;

  ref readonly Point Origin => ref origin;
  ref readonly Point* Origin;
  ref readonly Point[] Origin;
  ref readonly Point? Origin;

  (int, string str) a;
  (B b, C c, D d) a;

  nint a;
  nuint b;

  public required int B;
}

struct A {
  private readonly int c_;
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (field_declaration
        (modifier)
        (modifier)
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (identifier)
          (variable_declarator
            name: (identifier))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (generic_name
            (identifier)
            (type_argument_list
              (predefined_type)
              (generic_name
                (identifier)
                (type_argument_list
                  (predefined_type)))))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (modifier)
        (modifier)
        (variable_declaration
          type: (nullable_type
            type: (predefined_type))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (modifier)
        (variable_declaration
          type: (nullable_type
            type: (identifier))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (modifier)
        (modifier)
        (variable_declaration
          type: (pointer_type
            type: (predefined_type))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (modifier)
        (variable_declaration
          type: (pointer_type
            type: (identifier))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (modifier)
        (variable_declaration
          type: (pointer_type
            type: (predefined_type))
          (variable_declarator
            name: (identifier))))
      (comment)
      (field_declaration
        (variable_declaration
          type: (function_pointer_type
            (function_pointer_parameter
              type: (predefined_type))
            returns: (predefined_type))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (function_pointer_type
            (function_pointer_parameter
              type: (function_pointer_type
                (function_pointer_parameter
                  type: (predefined_type))
                returns: (predefined_type)))
            returns: (function_pointer_type
              (function_pointer_parameter
                type: (predefined_type))
              returns: (ref_type
                type: (predefined_type))))
          (variable_declarator
            name: (identifier))))
      (comment)
      (field_declaration
        (variable_declaration
          type: (function_pointer_type
            (calling_convention)
            (function_pointer_parameter
              type: (predefined_type))
            returns: (predefined_type))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (function_pointer_type
            (function_pointer_parameter
              type: (function_pointer_type
                (calling_convention
                  (identifier)
                  (identifier))
                (function_pointer_parameter
                  type: (predefined_type))
                returns: (predefined_type)))
            returns: (function_pointer_type
              (function_pointer_parameter
                type: (predefined_type))
              returns: (predefined_type)))
          (variable_declarator
            name: (identifier))))
      (property_declaration
        type: (ref_type
          type: (identifier))
        name: (identifier)
        value: (arrow_expression_clause
          (ref_expression
            (identifier))))
      (field_declaration
        (variable_declaration
          type: (ref_type
            type: (pointer_type
              type: (identifier)))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (ref_type
            type: (array_type
              type: (identifier)
              rank: (array_rank_specifier)))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (ref_type
            type: (nullable_type
              type: (identifier)))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (tuple_type
            (tuple_element
              type: (predefined_type))
            (tuple_element
              type: (predefined_type)
              name: (identifier)))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (tuple_type
            (tuple_element
              type: (identifier)
              name: (identifier))
            (tuple_element
              type: (identifier)
              name: (identifier))
            (tuple_element
              type: (identifier)
              name: (identifier)))
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier))))
      (field_declaration
        (modifier)
        (modifier)
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier))))))
  (struct_declaration
    name: (identifier)
    body: (declaration_list
      (field_declaration
        (modifier)
        (modifier)
        (variable_declaration
          type: (predefined_type)
          (variable_declarator
            name: (identifier)))))))
```

## File: `test/corpus/type-methods.txt`
```
================================================================================
Class method with single parameter
================================================================================

class A {
  private int GetBack(int b) {
    return b;
  }

  void Accept<T>(T accept) {
  }

  void Accept<T>(T accept) where T: new() {
  }

  void Accept<T1, T2>(T1 accept, T2 from)
    where T1: new()
    where T2: T1, new() {
  }

  void HasAnOut(out int a) {
  }

  void HasAnIn(in int a) {
  }

  void HasARef(ref int a) {
  }

  void M(this ref int a) { }
  void M(this scoped ref int a) { }

  void Keywords(int from, string partial) {
  }

  void Default(int a = 5) {
  }

  static int Static(int b) {
    return b;
  }

  public readonly double Add => x + y;

  DIn dIn = (ref readonly int p) => { };

  public int Zero(params int[]? ints) => 0;
}

class A : ISomething {
  int ISomething.GetBack(int b) {
    return b;
  }
}

ref struct S {
    void M(scoped ref System.Span<int> p) {
        scoped ref System.Span<int> i = ref p;
        scoped System.Span<int> j = p;
    }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        (modifier)
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        type_parameters: (type_parameter_list
          (type_parameter
            name: (identifier)))
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        type_parameters: (type_parameter_list
          (type_parameter
            name: (identifier)))
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        (type_parameter_constraints_clause
          (identifier)
          (type_parameter_constraint
            (constructor_constraint)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        type_parameters: (type_parameter_list
          (type_parameter
            name: (identifier))
          (type_parameter
            name: (identifier)))
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        (type_parameter_constraints_clause
          (identifier)
          (type_parameter_constraint
            (constructor_constraint)))
        (type_parameter_constraints_clause
          (identifier)
          (type_parameter_constraint
            type: (identifier))
          (type_parameter_constraint
            (constructor_constraint)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            (modifier)
            type: (predefined_type)
            name: (identifier)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            (modifier)
            type: (predefined_type)
            name: (identifier)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            (modifier)
            type: (predefined_type)
            name: (identifier)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            (modifier)
            (modifier)
            type: (predefined_type)
            name: (identifier)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            (modifier)
            (modifier)
            (modifier)
            type: (predefined_type)
            name: (identifier)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier))
          (parameter
            type: (predefined_type)
            name: (identifier)))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)
            (integer_literal)))
        body: (block))
      (method_declaration
        (modifier)
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (property_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        name: (identifier)
        value: (arrow_expression_clause
          (binary_expression
            left: (identifier)
            right: (identifier))))
      (field_declaration
        (variable_declaration
          type: (identifier)
          (variable_declarator
            name: (identifier)
            (lambda_expression
              parameters: (parameter_list
                (parameter
                  (modifier)
                  (modifier)
                  type: (predefined_type)
                  name: (identifier)))
              body: (block)))))
      (method_declaration
        (modifier)
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          type: (nullable_type
            type: (array_type
              type: (predefined_type)
              rank: (array_rank_specifier)))
          name: (identifier))
        body: (arrow_expression_clause
          (integer_literal)))))
  (class_declaration
    name: (identifier)
    (base_list
      (identifier))
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        (explicit_interface_specifier
          (identifier))
        name: (identifier)
        parameters: (parameter_list
          (parameter
            type: (predefined_type)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))))
  (struct_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          (parameter
            (modifier)
            (modifier)
            type: (qualified_name
              qualifier: (identifier)
              name: (generic_name
                (identifier)
                (type_argument_list
                  (predefined_type))))
            name: (identifier)))
        body: (block
          (local_declaration_statement
            (variable_declaration
              type: (scoped_type
                type: (ref_type
                  type: (qualified_name
                    qualifier: (identifier)
                    name: (generic_name
                      (identifier)
                      (type_argument_list
                        (predefined_type))))))
              (variable_declarator
                name: (identifier)
                (ref_expression
                  (identifier)))))
          (local_declaration_statement
            (variable_declaration
              type: (scoped_type
                type: (qualified_name
                  qualifier: (identifier)
                  name: (generic_name
                    (identifier)
                    (type_argument_list
                      (predefined_type)))))
              (variable_declarator
                name: (identifier)
                (identifier)))))))))

================================================================================
C# 13 params collections
================================================================================

class C {
  void M1(params int[] args) { }
  void M2(params Span<int> items) { }
  void M3(params IEnumerable<string> values) { }
  void M4(params List<double> numbers) { }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          type: (array_type
            type: (predefined_type)
            rank: (array_rank_specifier))
          name: (identifier))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          type: (generic_name
            (identifier)
            (type_argument_list
              (predefined_type)))
          name: (identifier))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          type: (generic_name
            (identifier)
            (type_argument_list
              (predefined_type)))
          name: (identifier))
        body: (block))
      (method_declaration
        returns: (predefined_type)
        name: (identifier)
        parameters: (parameter_list
          type: (generic_name
            (identifier)
            (type_argument_list
              (predefined_type)))
          name: (identifier))
        body: (block)))))
```

## File: `test/corpus/type-operators.txt`
```
================================================================================
Operator declarations
================================================================================

class A
{
  [SomeAttribute]
  public static int operator +(A a) { return 0; }

  public static int operator +(A a, A b) { return 0; }

  int operator -(A a) { return 0; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (attribute_list
          (attribute
            name: (identifier)))
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (integer_literal))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (integer_literal))))
      (operator_declaration
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (integer_literal)))))))

================================================================================
boolean operator declarations
================================================================================

class A
{
  public static bool operator true(A a) { return true; }
  bool operator false(A a) { return false; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (boolean_literal))))
      (operator_declaration
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (boolean_literal)))))))

================================================================================
conversion operator declaration
================================================================================

class A
{
  public static implicit operator int (A a) { return 0; }
  explicit operator int (A a) { return 0; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (integer_literal))))
      (conversion_operator_declaration
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (integer_literal)))))))

================================================================================
conversion operator with expression body
================================================================================

class A
{
  public static implicit operator int (A a) => 0;
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (integer_literal))))))

================================================================================
extern operators
================================================================================

class A
{
  public static extern int operator + (A a);
  public static extern bool operator <(A a, A b);
  public static explicit operator int (A a);
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))))
      (operator_declaration
        (modifier)
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier))))
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))))))

================================================================================
Class conversion operators with expression body
================================================================================

class A
{
  public static extern int operator + (A a) => 0;
  public static extern bool operator <(A a, A b) => true;
  public static explicit operator int (A a) => 0;
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (integer_literal)))
      (operator_declaration
        (modifier)
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (boolean_literal)))
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (integer_literal))))))

================================================================================
Unary operator overloads
================================================================================

class A
{
  public static A operator +(A a) { return a; }
  public static A operator -(A a) { return a; }
  public static A operator !(A a) { return a; }
  public static A operator ~(A a) { return a; }
  public static A operator ++(A a) { return a; }
  public static A operator --(A a) { return a; }
  public static bool operator true (A a) { return true; }
  public static bool operator false(A a) { return true; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (identifier))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (boolean_literal))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (boolean_literal)))))))

================================================================================
Binary unpaired operator overloads
================================================================================

class A
{
  public static A operator +(A a, A b) { return a == b; }
  public static A operator -(A a, A b) { return a != b; }
  public static A operator *(A a, A b) { return a < b; }
  public static A operator /(A a, A b) { return a <= b; }
  public static A operator %(A a, A b) { return a > b; }
  public static A operator &(A a, A b) { return a >= b; }
  public static A operator |(A a, A b) { return a >= b; }
  public static A operator ^(A a, A b) { return a >= b; }
  public static A operator <<(A a, A b) { return a >= b; }
  public static A operator >>(A a, A b) { return a >= b; }
  public static A operator >>>(A a, A b) { return a >= b; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier))))))))

================================================================================
Binary paired operator overloads
================================================================================

class A
{
  public static A operator ==(A a, A b) { return a == b; }
  public static A operator !=(A a, A b) { return a != b; }
  public static A operator <(A a, A b) { return a < b; }
  public static A operator <=(A a, A b) { return a <= b; }
  public static A operator >(A a, A b) { return a > b; }
  public static A operator >=(A a, A b) { return a >= b; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier)))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (binary_expression
              left: (identifier)
              right: (identifier))))))))

================================================================================
Explicit operator overloads
================================================================================

interface I
{
  static abstract int operator +(I i, I j);
}

public class C : I
{
  static int I.operator +(I i, I j) { return 1; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (interface_declaration
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier))))))
  (class_declaration
    (modifier)
    name: (identifier)
    (base_list
      (identifier))
    body: (declaration_list
      (operator_declaration
        (modifier)
        type: (predefined_type)
        (explicit_interface_specifier
          (identifier))
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (block
          (return_statement
            (integer_literal)))))))

================================================================================
Checked operators
================================================================================

public class C
{
  public static int operator checked +(C i, C j) => throw null;
  public static int operator +(C i, C j) => throw null;

  public static explicit operator checked int(C c) => throw null;
  public static explicit operator int(C c) => throw null;
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    (modifier)
    name: (identifier)
    body: (declaration_list
      (operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (throw_expression
            (null_literal))))
      (operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (throw_expression
            (null_literal))))
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (throw_expression
            (null_literal))))
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (throw_expression
            (null_literal)))))))

================================================================================
Explicit conversion operator overloads
================================================================================

public interface I<T> where T : I<T>
{
  static abstract explicit operator T(C c);
  static abstract explicit operator checked T(C c);
}

public class C : I<C>
{
  static explicit I<C>.operator C(C c) => throw null;
  static explicit I<C>.operator checked C(C c) => throw null;
}

--------------------------------------------------------------------------------

(compilation_unit
  (interface_declaration
    (modifier)
    name: (identifier)
    type_parameters: (type_parameter_list
      (type_parameter
        name: (identifier)))
    (type_parameter_constraints_clause
      (identifier)
      (type_parameter_constraint
        type: (generic_name
          (identifier)
          (type_argument_list
            (identifier)))))
    body: (declaration_list
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))))
      (conversion_operator_declaration
        (modifier)
        (modifier)
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier))))))
  (class_declaration
    (modifier)
    name: (identifier)
    (base_list
      (generic_name
        (identifier)
        (type_argument_list
          (identifier))))
    body: (declaration_list
      (conversion_operator_declaration
        (modifier)
        (explicit_interface_specifier
          (generic_name
            (identifier)
            (type_argument_list
              (identifier))))
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (throw_expression
            (null_literal))))
      (conversion_operator_declaration
        (modifier)
        (explicit_interface_specifier
          (generic_name
            (identifier)
            (type_argument_list
              (identifier))))
        type: (identifier)
        parameters: (parameter_list
          (parameter
            type: (identifier)
            name: (identifier)))
        body: (arrow_expression_clause
          (throw_expression
            (null_literal)))))))
```

## File: `test/corpus/type-properties.txt`
```
================================================================================
Class with bodyless properties
================================================================================

class Foo {
  byte Get { get; }
  char Set { set; }
  uint GetSet { get; set; }
  long SetGet { set; get; }

  public string FirstName { get; init; }

  byte Get { get { return 0xFF; } }
  char Set { set { x = value; } }
}

class Foo {
  uint GetSet {
    get { return x; }
    set { x = value; }
  }
  long SetGet {
    set { x = value; }
    get { return x; }
  }

  byte Get { get; } = 0x00;
  uint GetSet { get; set; } = 1;
  long SetGet { set; get; } = 2;
}

class Foo: IFoo {
  byte IFoo.Get { get; }
  public required int B { get; set; }
}

--------------------------------------------------------------------------------

(compilation_unit
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))
      (property_declaration
        (modifier)
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration)))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (block
              (return_statement
                (integer_literal))))))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (block
              (expression_statement
                (assignment_expression
                  left: (identifier)
                  right: (identifier)))))))))
  (class_declaration
    name: (identifier)
    body: (declaration_list
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (block
              (return_statement
                (identifier))))
          (accessor_declaration
            body: (block
              (expression_statement
                (assignment_expression
                  left: (identifier)
                  right: (identifier)))))))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration
            body: (block
              (expression_statement
                (assignment_expression
                  left: (identifier)
                  right: (identifier)))))
          (accessor_declaration
            body: (block
              (return_statement
                (identifier))))))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration))
        value: (integer_literal))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration))
        value: (integer_literal))
      (property_declaration
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration))
        value: (integer_literal))))
  (class_declaration
    name: (identifier)
    (base_list
      (identifier))
    body: (declaration_list
      (property_declaration
        type: (predefined_type)
        (explicit_interface_specifier
          (identifier))
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)))
      (property_declaration
        (modifier)
        (modifier)
        type: (predefined_type)
        name: (identifier)
        accessors: (accessor_list
          (accessor_declaration)
          (accessor_declaration))))))
```

## File: `test/highlight/baseline.cs`
```csharp
extern alias A;
//            ^ punctuation.delimiter

using System;
// <- keyword
//          ^ punctuation.delimiter
using global::System.Collections.Generic;
// <- keyword
//                  ^ punctuation.delimiter
//                              ^ punctuation.delimiter
//                                      ^ punctuation.delimiter
using static System.Console;
// <- keyword
//                 ^ punctuation.delimiter
//                         ^ punctuation.delimiter
using X = System.Console;
// <- keyword
//      ^ operator
//              ^ punctuation.delimiter
//                      ^ punctuation.delimiter
global using A;
// <- keyword
//     ^ keyword
//            ^ punctuation.delimiter
global using static A.B;
// <- keyword
//     ^ keyword
//                   ^ punctuation.delimiter
//                     ^ punctuation.delimiter

namespace Namespace
// <- keyword
//        ^ module
{
// <- punctuation.bracket
    using A;
    // <- keyword
    //     ^ punctuation.delimiter

    internal delegate void A(params int[] test);
    // <- keyword
    //       ^ keyword
    //                ^ type.builtin
    //                      ^ punctuation.bracket
    //                       ^ keyword
    //                              ^ type.builtin
    //                                 ^ punctuation.bracket
    //                                        ^ punctuation.bracket
    public struct F<T> where T : struct { }
    // <- keyword
    //     ^ keyword
    //            ^ type
    //             ^ operator
    //              ^ property.definition
    //               ^ operator
    //                 ^ keyword
    //                       ^ property.definition
    //                         ^ operator
    //                           ^ keyword
    //                                  ^ punctuation.bracket
    //                                    ^ punctuation.bracket

    record struct F
    // <- keyword
    //     ^ keyword
    //            ^ type
    {
    // <- punctuation.bracket
        int Age { get; init; }
        // <- type.builtin
        //  ^ variable
        //      ^ punctuation.bracket
        //        ^ keyword
        //           ^ punctuation.delimiter
        //             ^ keyword
        //                 ^ punctuation.delimiter
        //                   ^ punctuation.bracket
    }
    // <- punctuation.bracket

    [Nice]
    // <- punctuation.bracket
     // <- attribute
    //   ^ punctuation.bracket
    private record F<T1, T2> where T1 : I1, I2, new() where T2 : I2 { }
    // <- keyword
    //      ^ keyword
    //             ^ type
    //              ^ operator
    //               ^ property.definition
    //                 ^ punctuation.delimiter
    //                   ^ property.definition
    //                     ^ operator
    //                       ^ keyword
    //                             ^ property.definition
    //                                ^ operator
    //                                  ^ type
    //                                    ^ punctuation.delimiter
    //                                      ^ type
    //                                        ^ punctuation.delimiter
    //                                          ^ keyword
    //                                             ^ punctuation.bracket
    //                                                ^ keyword
    //                                                      ^ property.definition
    //                                                         ^ operator
    //                                                           ^ type
    //                                                              ^ punctuation.bracket
    //                                                                ^ punctuation.bracket

    record Teacher(string FirstName, string LastName, string Subject) : Person(FirstName, LastName);
    // <- keyword
    //     ^ type
    //            ^ punctuation.bracket
    //             ^ type.builtin
    //                    ^ variable.parameter
    //                             ^ punctuation.delimiter
    //                               ^ type.builtin
    //                                      ^ variable.parameter
    //                                              ^ punctuation.delimiter
    //                                                ^ type.builtin
    //                                                       ^ variable.parameter
    //                                                              ^ punctuation.bracket
    //                                                                ^ operator
    //                                                                        ^ punctuation.bracket
    //                                                                                  ^ punctuation.delimiter
    //                                                                                            ^ punctuation.bracket

    enum B { Ten = 10, Twenty = 20 }
    // <- keyword
    //   ^ type
    //     ^ punctuation.bracket
    //       ^ property.definition
    //           ^ operator
    //             ^ number
    //               ^ punctuation.delimiter
    //                 ^ property.definition
    //                        ^ operator
    //                          ^ number
    //                             ^ punctuation.bracket

    public class F : object, IAlpha, IOmega { }
    // <- keyword
    //     ^ keyword
    //           ^ type
    //             ^ operator
    //               ^ type.builtin
    //                     ^ punctuation.delimiter
    //                       ^ type
    //                             ^ punctuation.delimiter
    //                               ^ type
    //                                      ^ punctuation.bracket
    //                                        ^ punctuation.bracket

    public partial class Class<in TParam> where TParam : class?, notnull, F?
    // <- keyword
    //     ^ keyword
    //             ^ keyword
    //                   ^ type
    //                        ^ operator
    //                         ^ keyword
    //                            ^ property.definition
    //                                  ^ operator
    //                                    ^ keyword
    //                                          ^ property.definition
    //                                                 ^ operator
    //                                                   ^ keyword
    //                                                        ^ operator
    //                                                           ^ keyword
    //                                                                  ^ punctuation.delimiter
    //                                                                    ^ type
    //                                                                     ^ operator
    {
    // <- punctuation.bracket
        public event EventHandler<T> SomeEvent { add { } remove { } }
        // <- keyword
        //     ^ keyword
        //           ^ type
        //                       ^ operator
        //                        ^ type
        //                         ^ operator
        //                                     ^ punctuation.bracket
        //                                       ^ keyword
        //                                           ^ punctuation.bracket
        //                                             ^ punctuation.bracket
        //                                               ^ keyword
        //                                                      ^ punctuation.bracket
        //                                                        ^ punctuation.bracket
        //                                                          ^ punctuation.bracket
        public readonly int _B;
        // <- keyword
        //     ^ keyword
        //              ^ type.builtin
        //                  ^ variable
        //                   ^ variable
        //                    ^ punctuation.delimiter
        Int64 D_e_f, g;
        // <- type
        //    ^ variable
        //     ^ variable
        //      ^ variable
        //       ^ variable
        //        ^ variable
        //         ^ punctuation.delimiter
        //           ^ variable
        //            ^ punctuation.delimiter
        Tuple<char, Nullable<int>> z;
        // <- type
        //   ^ operator
        //    ^ type.builtin
        //        ^ punctuation.delimiter
        //          ^ type
        //                  ^ operator
        //                   ^ type.builtin
        //                      ^ operator
        //                         ^ variable
        //                          ^ punctuation.delimiter

        [SomeAttribute]
        // <- punctuation.bracket
         // <- attribute
        //            ^ punctuation.bracket
        public static int operator +(A a) { return 0; }
        // <- keyword
        //     ^ keyword
        //            ^ type.builtin
        //                ^ keyword
        //                         ^ operator
        //                           ^ type
        //                             ^ variable.parameter
        //                              ^ punctuation.bracket
        //                                ^ punctuation.bracket
        //                                  ^ keyword
        //                                         ^ number
        //                                          ^ punctuation.delimiter
        //                                            ^ punctuation.bracket

        uint GetSet { get; set; }
        // <- type.builtin
        //   ^ variable
        //          ^ punctuation.bracket
        //            ^ keyword
        //               ^ punctuation.delimiter
        //                 ^ keyword
        //                    ^ punctuation.delimiter
        //                      ^ punctuation.bracket

        static extern Foo() { }
        // <- keyword
        //     ^ keyword
        //            ^ constructor
        //               ^ punctuation.bracket
        //                  ^ punctuation.bracket
        //                    ^ punctuation.bracket

        extern ~Class() { }
        //     ^ operator
        //      ^ constructor
        //           ^ punctuation.bracket
        //              ^ punctuation.bracket
        //                ^ punctuation.bracket

        public void Method()
        // <- keyword
        //     ^ type.builtin
        //          ^ function
        //                ^ punctuation.bracket
        {
        // <- punctuation.bracket
            const int dec = 1_2;
            // <- keyword
            //    ^ type.builtin
            //        ^ variable
            //            ^ operator
            //              ^ number
            //               ^ number
            //                ^ number
            //                 ^ punctuation.delimiter
            const long hex = 0xf_1l;
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //             ^ operator
            //               ^ number
            //                  ^ number
            //                   ^ number
            //                     ^ punctuation.delimiter
            const long hex2 = 0Xffff;
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //              ^ operator
            //                ^ number
            //                      ^ punctuation.delimiter
            const long hex3 = 0x_0_f;
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //              ^ operator
            //                ^ number
            //                  ^ number
            //                   ^ number
            //                    ^ number
            //                     ^ number
            //                      ^ punctuation.delimiter
            const UInt64 dec = 1uL;
            // <- keyword
            //    ^ type
            //           ^ variable
            //               ^ operator
            //                 ^ number
            //                    ^ punctuation.delimiter
            const UInt16 bin = 0b0100_100;
            // <- keyword
            //    ^ type
            //           ^ variable
            //               ^ operator
            //                 ^ number
            //                       ^ number
            //                        ^ number
            //                           ^ punctuation.delimiter
            const UInt16 bin2 = 0B01010__10;
            // <- keyword
            //    ^ type
            //           ^ variable
            //                ^ operator
            //                  ^ number
            //                         ^ number
            //                           ^ number
            //                             ^ punctuation.delimiter
            const long bin3 = 0b_0_10;
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //              ^ operator
            //                ^ number
            //                  ^ number
            //                   ^ number
            //                    ^ number
            //                     ^ number
            //                       ^ punctuation.delimiter

            const bool t = true, u = false;
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //           ^ operator
            //             ^ constant.builtin
            //                 ^ punctuation.delimiter
            //                   ^ variable
            //                     ^ operator
            //                       ^ constant.builtin
            //                            ^ punctuation.delimiter

            const char c = 'a';
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //           ^ operator
            //             ^ string
            //              ^ string
            //               ^ string
            const char esc = '\n';
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //             ^ operator
            //                ^ string.escape
            //                  ^ string
            const char hex = '\xf09a';
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //             ^ operator
            //               ^ string
            //                 ^ string.escape
            //                      ^ string
            const char uni16 = '\ua0bf';
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //               ^ operator
            //                 ^ string
            //                   ^ string.escape
            //                        ^ string
            const char uni32 = '\UA0BFf9ca';
            // <- keyword
            //    ^ type.builtin
            //         ^ variable
            //               ^ operator
            //                 ^ string
            //                   ^ string.escape
            //                            ^ string

            const float s = 012.23F;
            // <- keyword
            //    ^ type.builtin
            //          ^ variable
            //            ^ operator
            //              ^ number
            //                 ^ number
            //                  ^ number
            //                     ^ punctuation.delimiter
            const float e = 1e6f;
            // <- keyword
            //    ^ type.builtin
            //          ^ variable
            //            ^ operator
            //              ^ number
            //                  ^ punctuation.delimiter
            const Single en = 0e-1f;
            // <- keyword
            //    ^ type
            //           ^ variable
            //              ^ operator
            //                ^ number
            //                  ^ number
            //                   ^ number
            //                     ^ punctuation.delimiter
            const Single ep = 1_1e+12f;
            // <- keyword
            //    ^ type
            //           ^ variable
            //              ^ operator
            //                ^ number
            //                 ^ number
            //                  ^ number
            //                    ^ number
            //                     ^ number
            //                        ^ punctuation.delimiter
            const double d = 0.9_9d;
            // <- keyword
            //    ^ type.builtin
            //           ^ variable
            //             ^ operator
            //               ^ number
            //                ^ number
            //                 ^ number
            //                  ^ number
            //                   ^ number
            //                     ^ punctuation.delimiter
            const double e = .4_9d;
            // <- keyword
            //    ^ type.builtin
            //           ^ variable
            //             ^ operator
            //               ^ number
            //                ^ number
            //                 ^ number
            //                  ^ number
            //                    ^ punctuation.delimiter
            const decimal m = 0_1_2.9m;
            // <- keyword
            //    ^ type.builtin
            //            ^ variable
            //              ^ operator
            //                ^ number
            //                 ^ number
            //                  ^ number
            //                   ^ number
            //                    ^ number
            //                     ^ number
            //                      ^ number
            //                        ^ punctuation.delimiter
            const Decimal m2 = 102.349M;
            // <- keyword
            //    ^ type
            //            ^ variable
            //               ^ operator
            //                 ^ number
            //                    ^ number
            //                     ^ number
            //                         ^ punctuation.delimiter

            const string x = null;
            // <- keyword
            //    ^ type.builtin
            //           ^ variable
            //             ^ operator
            //               ^ constant.builtin
            //                   ^ punctuation.delimiter

            String e = "";
            // <- type
            //     ^ variable
            //       ^ operator
            //         ^ string
            string s = "a";
            // <- type.builtin
            //     ^ variable
            //       ^ operator
            //         ^ string
            //          ^ string
            //           ^ string
            string m = "abc";
            // <- type.builtin
            //     ^ variable
            //       ^ operator
            //         ^ string
            //          ^ string
            //             ^ string
            string esc = "ab\"\t";
            // <- type.builtin
            //     ^ variable
            //         ^ operator
            //           ^ string
            //            ^ string
            //              ^ string.escape
            //                 ^ string.escape
            //                  ^ string
            string hex = "ab\x22r";
            // <- type.builtin
            //     ^ variable
            //         ^ operator
            //           ^ string
            //            ^ string
            //              ^ string.escape
            //               ^ string.escape
            //                   ^ string

            int @var = @const;
            // <- type.builtin
            //  ^ variable
            //   ^ variable
            //       ^ operator
            //               ^ punctuation.delimiter


            var x = $"""The point {X}, {Y} is {Math.Sqrt(X * X + Y * Y)} from the origin""";
            // <- keyword
            //  ^ variable
            //    ^ operator
            //                    ^ punctuation.bracket
            //                      ^ punctuation.bracket
            //                         ^ punctuation.bracket
            //                           ^ punctuation.bracket
            //                                ^ punctuation.bracket
            //                                     ^ punctuation.delimiter
            //                                          ^ punctuation.bracket
            //                                           ^ variable
            //                                             ^ operator
            //                                               ^ variable
            //                                                 ^ operator
            //                                                   ^ variable
            //                                                     ^ operator
            //                                                       ^ variable
            //                                                        ^ punctuation.bracket

            List<int> numbers = new() { 5, 4, 1, 3, 9, 8, 6, 7, 2, 0 };
            // <- type
            //  ^ operator
            //   ^ type.builtin
            //      ^ operator
            //        ^ variable
            //                ^ operator
            //                  ^ keyword
            //                     ^ punctuation.bracket
            //                        ^ punctuation.bracket
            //                          ^ number
            //                           ^ punctuation.delimiter
            //                             ^ number
            //                              ^ punctuation.delimiter
            //                                ^ number
            //                                 ^ punctuation.delimiter
            //                                   ^ number
            //                                    ^ punctuation.delimiter
            //                                      ^ number
            //                                       ^ punctuation.delimiter
            //                                         ^ number
            //                                          ^ punctuation.delimiter
            //                                            ^ number
            //                                             ^ punctuation.delimiter
            //                                               ^ number
            //                                                ^ punctuation.delimiter
            //                                                  ^ number
            //                                                   ^ punctuation.delimiter
            //                                                     ^ number
            //                                                       ^ punctuation.bracket

            var query =
            // <- keyword
            //  ^ variable
            //        ^ operator
                from num in numbers
                // <- keyword
                //   ^ variable
                //       ^ keyword
                //          ^ variable
                where num < 3 || num > 7
                // <- keyword
                //    ^ variable
                //        ^ operator
                //          ^ number
                //            ^ operator
                //               ^ variable
                //                   ^ operator
                //                     ^ number
                orderby num ascending
                select num;
                // <- keyword
                //     ^ variable
                //        ^ punctuation.delimiter

            var u = x is int?
            // <- keyword
            //  ^ variable
            //    ^ operator
            //        ^ keyword
            //           ^ type.builtin
            //              ^ operator
                ? a
                // <- operator
                //^ variable
                : b;
                // <- operator
                //^ variable
                // ^ punctuation.delimiter
            a = (B)c + (C)d;
            // <- variable
            //^ operator
            //  ^ punctuation.bracket
            //   ^ type
            //    ^ punctuation.bracket
            //     ^ variable
            //       ^ operator
            //         ^ punctuation.bracket
            //          ^ type
            //           ^ punctuation.bracket
            //            ^ variable
            //             ^ punctuation.delimiter
            b = (float)a[0];
            // <- variable
            //^ operator
            //  ^ punctuation.bracket
            //   ^ type.builtin
            //        ^ punctuation.bracket
            //          ^ punctuation.bracket
            //           ^ number
            //            ^ punctuation.bracket
            var x = new
            // <- keyword
            //  ^ variable
            //    ^ operator
            //      ^ keyword
            {
            // <- punctuation.bracket
            };
            // <- punctuation.bracket
            var three = checked(1 + 2);
            // <- keyword
            //  ^ variable
            //        ^ operator
            //          ^ keyword
            //                 ^ punctuation.bracket
            //                  ^ number
            //                    ^ operator
            //                      ^ number
            //                       ^ punctuation.bracket
            var d = delegate (int a)
            // <- keyword
            //  ^ variable
            //    ^ operator
            //      ^ keyword
            //               ^ punctuation.bracket
            //                ^ type.builtin
            //                    ^ variable.parameter
            //                     ^ punctuation.bracket
            {
            // <- punctuation.bracket
                return a;
                // <- keyword
                //     ^ variable
                //      ^ punctuation.delimiter
            };
            // <- punctuation.bracket

            var l = (A a, B b) => { return a.c(b); };
            // <- keyword
            //  ^ variable
            //    ^ operator
            //      ^ punctuation.bracket
            //       ^ type
            //         ^ variable.parameter
            //          ^ punctuation.delimiter
            //            ^ type
            //              ^ variable.parameter
            //               ^ punctuation.bracket
            //                 ^ operator
            //                    ^ punctuation.bracket
            //                      ^ keyword
            //                             ^ variable
            //                              ^ punctuation.delimiter
            //                               ^ function
            //                                ^ punctuation.bracket
            //                                 ^ variable
            //                                  ^ punctuation.bracket
            //                                     ^ punctuation.bracket

            int Add(int left, int right) => a + b;
            // <- type.builtin
            //  ^ function
            //      ^ type.builtin
            //          ^ variable.parameter
            //                 ^ type.builtin
            //                     ^ variable.parameter
            //                            ^ operator
            //                                ^ operator

            Do(async () => { });
            //^ punctuation.bracket
            // ^ keyword
            //       ^ punctuation.bracket
            //          ^ operator
            //             ^ punctuation.bracket
            //               ^ punctuation.bracket

            var gp = __makeref(g);
            // <- keyword
            //  ^ variable
            //     ^ operator
            //                ^ punctuation.bracket
            //                  ^ punctuation.bracket

            var z = typeof(List<string>.Enumerator);
            // <- keyword
            //  ^ variable
            //    ^ operator
            //      ^ keyword
            //            ^ punctuation.bracket
            //             ^ type
            //                 ^ operator
            //                  ^ type.builtin
            //                        ^ operator
            //                                    ^ punctuation.bracket

            ref VeryLargeStruct reflocal = ref veryLargeStruct;
            // <- keyword
            //                  ^ variable
            //                           ^ operator
            //                             ^ keyword
            //                                                ^ punctuation.delimiter
            ref var elementRef = ref arr[0];
            // <- keyword
            //  ^ keyword
            //      ^ variable
            //                 ^ operator
            //                   ^ keyword
            //                          ^ punctuation.bracket
            //                           ^ number
            //                            ^ punctuation.bracket

            var x = name is (var a);
            // <- keyword
            //  ^ variable
            //    ^ operator
            //           ^ keyword
            //              ^ punctuation.bracket
            //                    ^ punctuation.bracket
            var x = c is < '0' or >= 'A' and <= 'Z';
            // <- keyword
            //  ^ variable
            //    ^ operator
            //        ^ keyword
            //           ^ operator
            //             ^ string
            //              ^ string
            //               ^ string
            //                       ^ string
            //                        ^ string
            //                         ^ string
            //                                  ^ string
            //                                   ^ string
            //                                    ^ string
            var x = !this.Call();
            // <- keyword
            //  ^ variable
            //    ^ operator
            //      ^ operator
            //       ^ keyword
            //           ^ punctuation.delimiter
            //                ^ punctuation.bracket

        }
        // <- punctuation.bracket

        void Sample()
        // <- type.builtin
        //         ^ punctuation.bracket
        {
        // <- punctuation.bracket
            while (true) break;
            // <- keyword
            //    ^ punctuation.bracket
            //     ^ constant.builtin
            //         ^ punctuation.bracket
            //           ^ keyword
            //                ^ punctuation.delimiter
            throw ex;
            // <- keyword
            //      ^ punctuation.delimiter
            do { } while (a);
            // <- keyword
            // ^ punctuation.bracket
            //   ^ punctuation.bracket
            //     ^ keyword
            //           ^ punctuation.bracket
            //             ^ punctuation.bracket
            goto end;
            // <- keyword
            //      ^ punctuation.delimiter
        end:
        // ^ operator
            return;
            // <- keyword
            //    ^ punctuation.delimiter
            if (true) return 1;
            // <- keyword
            // ^ punctuation.bracket
            //  ^ constant.builtin
            //      ^ punctuation.bracket
            //        ^ keyword
            //               ^ number
            //                ^ punctuation.delimiter
            else return 0;
            // <- keyword
            //   ^ keyword
            //          ^ number
            //           ^ punctuation.delimiter

            (string a, bool b) c = default;
            // <- punctuation.bracket
             // <- type.builtin
            //       ^ punctuation.delimiter
            //         ^ type.builtin
            //               ^ punctuation.bracket
            //                 ^ variable
            //                   ^ operator
            //                     ^ keyword
            //                            ^ punctuation.delimiter
            switch (a, a)
            // <- keyword
            //     ^ punctuation.bracket
            //       ^ punctuation.delimiter
            //          ^ punctuation.bracket
            {
            // <- punctuation.bracket
                case (1, 1):
                // <- keyword
                //   ^ punctuation.bracket
                //    ^ number
                //     ^ punctuation.delimiter
                //       ^ number
                //        ^ punctuation.bracket
                    return 1;
                    // <- keyword
                    //     ^ number
                    //      ^ punctuation.delimiter
                default:
                // <- keyword
                //     ^ operator
                    return 0;
                    // <- keyword
                    //     ^ number
                    //      ^ punctuation.delimiter
            }
            // <- punctuation.bracket

            lock (this)
            // <- keyword
            //   ^ punctuation.bracket
            //    ^ keyword
            //        ^ punctuation.bracket
            {
            // <- punctuation.bracket
                return;
                // <- keyword
                //    ^ punctuation.delimiter
            }
            // <- punctuation.bracket

            yield return 1;
            // <- keyword
            //    ^ keyword
            //           ^ number
            //            ^ punctuation.delimiter

            using (Stream a = File.OpenRead("a"), b = new BinaryReader(a))
            // <- keyword
            //    ^ punctuation.bracket
            //     ^ type
            //            ^ variable
            //              ^ operator
            //                    ^ punctuation.delimiter
            //                             ^ punctuation.bracket
            //                               ^ string
            //                                ^ string
            //                                    ^ variable
            //                                      ^ operator
            //                                        ^ keyword
            //                                                        ^ punctuation.bracket
            //                                                          ^ punctuation.bracket
            {
            // <- punctuation.bracket
                return;
                // <- keyword
                //    ^ punctuation.delimiter
            }
            // <- punctuation.bracket

            foreach (var (x, y) in z)
            // <- keyword
            //      ^ punctuation.bracket
            //       ^ keyword
            //           ^ punctuation.bracket
            //             ^ punctuation.delimiter
            //                ^ punctuation.bracket
            //                  ^ keyword
            //                      ^ punctuation.bracket
                q += x;
                // <- variable
                //^ operator
                //   ^ variable
                //    ^ punctuation.delimiter

            for (int x = 0; x < 100; x++)
            // <- keyword
            //  ^ punctuation.bracket
            //   ^ type.builtin
            //       ^ variable
            //         ^ operator
            //           ^ number
            //            ^ punctuation.delimiter
            //              ^ variable
            //                ^ operator
            //                  ^ number
            //                     ^ punctuation.delimiter
            //                       ^ variable
            //                        ^ operator
            {
            // <- punctuation.bracket
                z += x;
                // <- variable
                //^ operator
                //   ^ variable
                //    ^ punctuation.delimiter
            }
            // <- punctuation.bracket

            dynamic dyn = "";
            // <- type
            //      ^ variable
            //          ^ operator
            //            ^ string
        }
        // <- punctuation.bracket

        string b(Object operation) =>
        // <- type.builtin
        //      ^ punctuation.bracket
        //       ^ type
        //              ^ variable.parameter
        //                       ^ punctuation.bracket
        //                         ^ operator
            operation switch
            // <- variable
            //        ^ keyword
            {
            // <- punctuation.bracket
                1 => "one",
                // <- number
                //^ operator
                //   ^ string
                //    ^ string
                //       ^ string
                _ => "more",
                //^ operator
                //   ^ string
                //    ^ string
                //        ^ string
            };
            // <- punctuation.bracket
    }
    // <- punctuation.bracket

}
// <- punctuation.bracket
```

## File: `test/highlight/operators.cs`
```csharp
using Namespace;

class C
{
    void M()
    {
        // unary
        a = +a;
        //  ^ operator
        a = -a;
        //  ^ operator
        a = !a;
        //  ^ operator
        a = ~a;
        //  ^ operator
        a = ++a;
        //  ^ operator
        a = --a;
        //  ^ operator
        a = a++;
        //   ^ operator
        a = a--;
        //   ^ operator
        a = a!;
        //   ^ operator
        a = a++;
        //   ^ operator
        a = a--;
        //   ^ operator

        // binary
        a = a + a;
        //    ^ operator
        a = a - a;
        //    ^ operator
        a = a * a;
        //    ^ operator
        a = a / a;
        //    ^ operator
        a = a % a;
        //    ^ operator
        a = a & a;
        //    ^ operator
        a = a | a;
        //    ^ operator
        a = a ^ a;
        //    ^ operator
        a = a >> a;
        //    ^ operator
        a = a << a;
        //    ^ operator
        a = a >>> a;
        //    ^ operator

        a = a == b;
        //    ^ operator
        a = a != b;
        //    ^ operator
        a = a < b;
        //    ^ operator
        a = a <= b;
        //    ^ operator
        a = a > b;
        //    ^ operator
        a = a >= b;
        //    ^ operator

        // assignment binary
        a += a;
        //^ operator
        a -= a;
        //^ operator
        a *= a;
        //^ operator
        a /= a;
        //^ operator
        a %= a;
        //^ operator
        a <<= a;
        //^ operator
        a >>= a;
        //^ operator
        a >>>= a;
        //^ operator

        // ternary
        string y = x ? "foo" : "bar";
        //           ^ operator
        //                   ^ operator

        // misc
        var l = (int i) => i;
        //              ^ operator
    }
}
```

## File: `test/highlight/types.cs`
```csharp
class A : B, C
//    ^ type
//        ^ type
//           ^ type
{
    public void M()
    {
        int a;
        // <- type.builtin
        var a;
        // <- keyword

        int? a;
        // <- type.builtin
        // ^ operator
        A? a;
        // <- type
         // <- operator

        int* a;
        // <- type.builtin
        // ^ operator
        A* a;
        // <- type
         // <- operator

        ref A* a;
        // <- keyword
        //  ^ type
        //   ^ operator

        var a = x is int;
        //           ^ type.builtin
        var a = x is A;
        //           ^

        var a = x as int;
        //           ^ type.builtin
        var a = x as A;
        //           ^ type

        var a = (int)x;
        //       ^ type.builtin
        var a = (A)x;
        //       ^ type

        A<int, A> a = new A<int, A>();
        // <- type
        //^ type.builtin
        //     ^ type
        //                ^ type
        //                  ^ type.builtin
        //                       ^ type
    }
}

record A(int a, B b) : B(), I;
//     ^ type
//       ^ type.builtin
//              ^ type
//                     ^ type
//                          ^ type

record A : B, I;
//     ^ type
//         ^ type
//            ^ type
```

## File: `test/highlight/var.cs`
```csharp
class var
//     ^ type
{
    void M()
    {
        var var = new var();
        // <- keyword
        //   ^ variable
    }
}
```

## File: `test/highlight/variableDeclarations.cs`
```csharp
class A
{
    public void M()
    {
        foreach (int i in new[] { 1 })
        //           ^ variable
        {
            int j = i;
            //  ^ variable
        }

        var x = from a in sourceA
        //           ^ variable
        //                ^ variable
                join b in sourceB on a.FK equals b.PK
        //           ^ variable
        //                ^ variable
                group a by a.X into g
        //            ^ variable
        //                          ^ variable
                orderby g ascending
        //              ^ variable
                select new { A.A, B.B };
    }
}
```

## File: `test/queries/identifiers.cs`
```csharp
namespace World
{
    class Hello {
        static void Main(string []args)
        {
            Hello x = new Hello();
            System.Console.WriteLine("Hello, world.");
        }
    }

    interface Blah {

    }
}
```

## File: `tools/highlight-test-generator/.gitignore`
```
bin/
obj/
```

## File: `tools/highlight-test-generator/Generator.cs`
```csharp
using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;

if (args.Length != 1)
{
    Console.WriteLine("Add the path to the file as an argument. The path needs to be fully qualified and point to an existing file in [REPO ROOT]/test/highlight.");
    return;
}

var filePath = args[0];

// Some basic tests on the path, so that we have a chance:
if (!filePath.Contains("/test/highlight/") ||
    !filePath.EndsWith(".cs") ||
    !File.Exists(filePath) ||
    !Path.IsPathFullyQualified(filePath))
{
    Console.WriteLine("The file needs to exist in [REPO ROOT]/test/highlight, and the path needs to be fully qualified.");
    return;
}

// Random variable name prefix, so that we don't accidentally replace something in the file:
var idPrefix = "a" + new Random(filePath.GetHashCode()).NextInt64(10000000) + "_";

var originalLines = File.ReadAllLines(filePath);


/// <summary>
/// Adds tree-sitter highlighting comments to the input file.
/// Comments start with either `// <-` or `// ^`, depending on the position of the hiughlighted token.
/// For highlight category, a unique random identifier is used.
/// </summary>
void AddCommentsToFile()
{
    var newLines = new List<string>();
    var index = 0;

    foreach (var line in originalLines)
    {
        newLines.Add(line);

        var leadingWhitespaces = line[..^line.TrimStart().Length];
        var first = true;

        var position = leadingWhitespaces.Length;
        while (position < line.Length)
        {
            var ch = line[position];

            bool HandleToken(Func<char, bool> isOfType)
            {
                if (!isOfType(ch))
                {
                    return false;
                }

                var variable = $"{idPrefix}{index++}";
                if (first)
                {
                    newLines.Add($"{leadingWhitespaces}// <- {variable}");
                    first = false;
                }
                else
                {
                    var spacesLength = position - leadingWhitespaces.Length - 2;
                    if (spacesLength < 0)
                    {
                        // Handle case when the first two characters need different highlight categories:
                        // Shift // by one space to the right.
                        newLines.Add($"{leadingWhitespaces} // <- {variable}");
                    }
                    else
                    {
                        var spaces = new string(' ', position - leadingWhitespaces.Length - 2);
                        newLines.Add($"{leadingWhitespaces}//{spaces}^ {variable}");
                    }
                }

                while (position < line.Length && isOfType(line[position]))
                {
                    position++;
                }

                return true;
            }

            // The below char methods are not exactly what we need for token parsing, but good enough.
            // For example
            // - `_abc` is an identifier, but has both letter and punctuation characters.
            // - string literals are parsed pretty badly, considering they can have all sorts of characters, even spaces, on which we split.
            if (!HandleToken(char.IsLetterOrDigit) &&
                !HandleToken(c => char.IsPunctuation(c) || char.IsSymbol(c)))
            {
                position++;
            }
        }
    }

    File.WriteAllLines(filePath, newLines.ToArray());
}

string GetHighlighterOutput()
{
    var process = new Process
    {
        StartInfo = new ProcessStartInfo
        {
            FileName = "tree-sitter",
            Arguments = $"test --filter skip-all-corpus-tests",
            UseShellExecute = false,
            RedirectStandardOutput = true,
            WorkingDirectory = Path.GetFullPath(Path.Combine(filePath, "..", "..", "..")),

        }
    };
    process.Start();
    var output = process.StandardOutput.ReadToEnd();
    process.WaitForExit();

    return output;
}

var regexWithHighlight = new Regex($@"Failure - row: \d+, column: \d+, expected highlight '{idPrefix}(\d+)', actual highlights: '(.*)'", RegexOptions.Compiled);
var regexWithNone = new Regex($@"Failure - row: \d+, column: \d+, expected highlight '{idPrefix}(\d+)', actual highlights: none.", RegexOptions.Compiled);

/// <summary>
/// Runs the tree-sitter test command, and tries to find a single highlighting failure.
/// If a failure is found, the category is extracted from the output, and the corresponding variable is replaced with the category.
/// </summary>
bool FindAndFixHighlightFailure()
{
    Console.Write(".");
    var output = GetHighlighterOutput();

    if (output.IndexOf("✗") != output.LastIndexOf("✗"))
    {
        Console.WriteLine("\nThe tree-sitter test execution identified multiple files with failed highlighting. Aborting.");
        File.WriteAllLines(filePath, originalLines);
        Environment.Exit(1);
    }

    var match = regexWithHighlight.Match(output);
    if (match.Success && match.Groups.Count == 3)
    {
        // Highlight found for position, so replace with expected category.
        var variableCat = $"{idPrefix}{match.Groups[1].Captures[0].Value}";
        var category = match.Groups[2].Captures[0].Value;
        File.WriteAllText(filePath, File.ReadAllText(filePath).Replace(variableCat + "\n", category + "\n"));
        return true;
    }

    match = regexWithNone.Match(output);
    if (!match.Success || match.Groups.Count != 2)
    {
        // Couldn't match any of the expected patterns.
        return false;
    }

    // No highlight found for position, so remove entire line.
    var variableNone = $"{idPrefix}{match.Groups[1].Captures[0].Value}";
    var lines = File.ReadAllLines(filePath).Where(line => !line.EndsWith(variableNone)).ToArray();
    File.WriteAllLines(filePath, lines);
    return true;
}

AddCommentsToFile();

Console.WriteLine("Calling tree-sitter highlighter several times. This might take a while.");
while (FindAndFixHighlightFailure())
{ }
Console.WriteLine("");
Console.WriteLine("Done modifying the input file. It may require some manual cleanup.");

```

## File: `tools/highlight-test-generator/Generator.csproj`
```
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <OutputType>Exe</OutputType>
    <TargetFramework>net6.0</TargetFramework>
  </PropertyGroup>
</Project>
```

## File: `tools/highlight-test-generator/run-generator`
```
#!/bin/bash

ROOT="$(git rev-parse --show-toplevel)"
echo $ROOT/tools/highlight-test-generator/Generator.csproj
dotnet run --project $ROOT/tools/highlight-test-generator/Generator.csproj $1
```

