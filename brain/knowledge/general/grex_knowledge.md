---
id: grex-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:28:49.477273
---

# KNOWLEDGE EXTRACT: grex
> **Extracted on:** 2026-03-30 17:38:02
> **Source:** grex

---

## File: `.editorconfig`
```
# Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Editor configuration, see http://editorconfig.org
root = true

[*.rs]
charset = utf-8
indent_style = space
indent_size = 4
insert_final_newline = true
trim_trailing_whitespace = false
max_line_length = 100

[*.md]
max_line_length = off
trim_trailing_whitespace = false
```

## File: `.gitignore`
```
# Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

/pkg/
/target/
**/*.rs.bk

.idea
.project
.c9/
*.launch
.settings/
.metadata/
.venv
*.sublime-workspace
bin/
tmp/
out/
*.iml
*.ipr
*.iws
*.bak
*.tmp
*.class
*.html
.buildpath
.classpath
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json

.DS_Store
Thumbs.db
$RECYCLE.BIN/
._*
.AppleDouble
.LSOverride
*.lnk
Desktop.ini
ehthumbs.db

*.proptest-regressions
```

## File: `Cargo.toml`
```
#
# Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

[package]
name = "grex"
version = "1.4.6"
authors = ["Peter M. Stahl <pemistahl@gmail.com>"]
description = """
grex generates regular expressions from user-provided test cases.
"""
homepage = "https://github.com/pemistahl/grex"
repository = "https://github.com/pemistahl/grex"
documentation = "https://docs.rs/grex"
license = "Apache-2.0"
readme = "README.md"
edition = "2021"
categories = ["command-line-utilities", "parsing"]
keywords = ["pattern", "regex", "regexp"]

[lib]
crate-type = ["cdylib", "rlib"]

[dependencies]
itertools = "0.14.0"
ndarray = "0.17.1"
petgraph = {version = "0.8.3", default-features = false, features = ["stable_graph"]}
regex = "1.12.2"
unicode-general-category = "1.1.0"
unicode-segmentation = "1.12.0"

[target.'cfg(not(target_family = "wasm"))'.dependencies]
clap = {version = "4.5.53", features = ["derive", "wrap_help"], optional = true}
pyo3 = {version = "0.27.1", optional = true}

[target.'cfg(target_family = "wasm")'.dependencies]
wasm-bindgen = "0.2.105"

[dev-dependencies]
indoc = "2.0.7"
rstest = "0.26.1"

[target.'cfg(not(target_family = "wasm"))'.dev-dependencies]
assert_cmd = "2.1.1"
criterion = "0.7.0"
predicates = "3.1.3"
proptest = "1.9.0"
tempfile = "3.23.0"

[target.'cfg(target_family = "wasm")'.dev-dependencies]
wasm-bindgen-test = "0.3.55"

[features]
default = ["cli"]
cli = ["clap"]
python = ["pyo3"]

[[bench]]
name = "benchmark"
harness = false

[profile.bench]
debug = true
```

## File: `demo.tape`
```
# demo.gif created with https://github.com/charmbracelet/vhs on macOS 13 (Ventura)

Require grex
Output demo.gif

Set Shell zsh
Set Theme "Whimsy"
Set Width 1200
Set Height 850
Set TypingSpeed 150ms

Type "grex -c 'regexes are awesome' 'regexes are awful'"
Sleep 3s
Enter
Sleep 10s

Up
Left 42
Type " --verbose"
Sleep 3s
Enter
Sleep 15s
Type "clear"
Enter

Type "grex -c haha HAHAHA"
Sleep 3s
Enter
Sleep 10s

Up
Left 12
Type " --repetitions"
Sleep 3s
Enter
Sleep 10s

Up
Left 12
Type " --verbose"
Sleep 3s
Enter
Sleep 15s

Up
Left 12
Type " --ignore-case"
Sleep 3s
Enter
Sleep 15s
```

## File: `grex.pyi`
```
#
# Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import List


class RegExpBuilder:
    """This class builds regular expressions from user-provided test cases."""

    @classmethod
    def from_test_cases(cls, test_cases: List[str]) -> "RegExpBuilder":
        """Specify the test cases to build the regular expression from.

        The test cases need not be sorted because `RegExpBuilder` sorts them internally.

        Args:
            test_cases (list[str]): The list of test cases

        Raises:
            ValueError: if `test_cases` is empty
        """

    def with_conversion_of_digits(self) -> "RegExpBuilder":
        """Convert any Unicode decimal digit to character class `\d`.

        This method takes precedence over `with_conversion_of_words` if both are set.
        Decimal digits are converted to `\d`, the remaining word characters to `\w`.

        This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
        Decimal digits are converted to `\d`, the remaining non-whitespace characters to `\S`.
        """

    def with_conversion_of_non_digits(self) -> "RegExpBuilder":
        """Convert any character which is not a Unicode decimal digit to character class `\D`.

        This method takes precedence over `with_conversion_of_non_words` if both are set.
        Non-digits which are also non-word characters are converted to `\D`.

        This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
        Non-digits which are also non-space characters are converted to `\D`.
        """

    def with_conversion_of_whitespace(self) -> "RegExpBuilder":
        """Convert any Unicode whitespace character to character class `\s`.

        This method takes precedence over `with_conversion_of_non_digits` if both are set.
        Whitespace characters are converted to `\s`, the remaining non-digit characters to `\D`.

        This method takes precedence over `with_conversion_of_non_words` if both are set.
        Whitespace characters are converted to `\s`, the remaining non-word characters to `\W`.
        """

    def with_conversion_of_non_whitespace(self) -> "RegExpBuilder":
        """Convert any character which is not a Unicode whitespace character to character class `\S`."""

    def with_conversion_of_words(self) -> "RegExpBuilder":
        """Convert any Unicode word character to character class `\w`.

        This method takes precedence over `with_conversion_of_non_digits` if both are set.
        Word characters are converted to `\w`, the remaining non-digit characters to `\D`.

        This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
        Word characters are converted to `\w`, the remaining non-space characters to `\S`.
        """

    def with_conversion_of_non_words(self) -> "RegExpBuilder":
        """Convert any character which is not a Unicode word character to character class `\W`.

        This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
        Non-words which are also non-space characters are converted to `\W`.
        """

    def with_conversion_of_repetitions(self) -> "RegExpBuilder":
        """Detect repeated non-overlapping substrings and to convert them to `{min,max}` quantifier notation."""

    def with_case_insensitive_matching(self) -> "RegExpBuilder":
        """Enable case-insensitive matching of test cases so that letters match both upper and lower case."""

    def with_capturing_groups(self) -> "RegExpBuilder":
        """Replace non-capturing groups with capturing ones."""

    def with_minimum_repetitions(self, quantity: int) -> "RegExpBuilder":
        """Specify the minimum quantity of substring repetitions to be converted
        if `with_conversion_of_repetitions` is set.

        If the quantity is not explicitly set with this method, a default value of 1 will be used.

        Args:
            quantity (int): The minimum quantity of substring repetitions

        Raises:
            ValueError: if `quantity` is zero
        """

    def with_minimum_substring_length(self, length: int) -> "RegExpBuilder":
        """Specify the minimum length a repeated substring must have in order
        to be converted if `with_conversion_of_repetitions` is set.

        If the length is not explicitly set with this method, a default value of 1 will be used.

        Args:
            length (int): The minimum substring length

        Raises:
            ValueError: if `length` is zero
        """

    def with_escaping_of_non_ascii_chars(self, use_surrogate_pairs: bool) -> "RegExpBuilder":
        """Convert non-ASCII characters to unicode escape sequences.

        The parameter `use_surrogate_pairs` specifies whether to convert astral
        code planes (range `U+010000` to `U+10FFFF`) to surrogate pairs.

        Args:
            use_surrogate_pairs (bool): Whether to convert astral code planes to surrogate pairs
        """

    def with_verbose_mode(self) -> "RegExpBuilder":
        """ Produce a nicer looking regular expression in verbose mode."""

    def without_start_anchor(self) -> "RegExpBuilder":
        """Remove the caret anchor '^' from the resulting regular expression,
        thereby allowing to match the test cases also when they do not occur
        at the start of a string.
        """

    def without_end_anchor(self) -> "RegExpBuilder":
        """Remove the dollar sign anchor '$' from the resulting regular expression,
        thereby allowing to match the test cases also when they do not occur
        at the end of a string.
        """

    def without_anchors(self) -> "RegExpBuilder":
        """Remove the caret and dollar sign anchors from the resulting regular expression,
        thereby allowing to match the test cases also when they occur within a larger
        string that contains other content as well.
        """

    def build(self) -> str:
        """Build the actual regular expression using the previously given settings."""
```

## File: `LICENSE`
```
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright [yyyy] [name of copyright owner]

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
```

## File: `pyproject.toml`
```
[project]
name = "grex"
version = "1.0.2"
authors = [{name = "Peter M. Stahl", email = "pemistahl@gmail.com"}]
description = "grex generates regular expressions from user-provided test cases."
readme = "README_PYPI.md"
requires-python = ">=3.12"
license = {file = "LICENSE"}
keywords = ["pattern", "regex", "regexp"]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "Intended Audience :: Information Technology",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3.12",
    "Programming Language :: Python :: 3.13",
    "Programming Language :: Python :: 3.14",
    "Programming Language :: Rust",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: Text Processing"
]

[project.urls]
homepage = "https://github.com/pemistahl/grex"
repository = "https://github.com/pemistahl/grex"

[project.optional-dependencies]
test = ["pytest == 9.0.1"]

[tool.maturin]
no-default-features = true
features = ["pyo3/extension-module", "pyo3/generate-import-lib", "python"]

[build-system]
requires = ["maturin>=1.1,<2.0"]
build-backend = "maturin"

```

## File: `README.md`
```markdown
<div align="center">

  ![grex](https://raw.githubusercontent.com/pemistahl/grex/main/logo.png)

  <br>

  [![rust build status](https://github.com/pemistahl/grex/actions/workflows/rust-build.yml/badge.svg)](https://github.com/pemistahl/grex/actions/workflows/rust-build.yml)
  [![python build status](https://github.com/pemistahl/grex/actions/workflows/python-build.yml/badge.svg)](https://github.com/pemistahl/grex/actions/workflows/python-build.yml)
  [![docs.rs](https://docs.rs/grex/badge.svg)](https://docs.rs/grex)
  [![codecov](https://codecov.io/gh/pemistahl/grex/branch/main/graph/badge.svg)](https://codecov.io/gh/pemistahl/grex)
  [![dependency status](https://deps.rs/crate/grex/1.4.6/status.svg)](https://deps.rs/crate/grex/1.4.6)
  [![demo](https://img.shields.io/badge/-Demo%20Website-orange?logo=HTML5&labelColor=white)](https://pemistahl.github.io/grex-js/)
  
  [![downloads](https://img.shields.io/crates/d/grex.svg)](https://crates.io/crates/grex)
  [![crates.io](https://img.shields.io/crates/v/grex.svg)](https://crates.io/crates/grex)
  [![lib.rs](https://img.shields.io/badge/lib.rs-v1.4.6-blue)](https://lib.rs/crates/grex)
  ![supported Python versions](https://img.shields.io/badge/Python-%3E%3D%203.12-blue?logo=Python&logoColor=yellow)
  [![pypi](https://img.shields.io/badge/PYPI-v1.0.2-blue?logo=PyPI&logoColor=yellow)](https://pypi.org/project/grex)
  [![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)

  [![Linux 64-bit Download](https://img.shields.io/badge/Linux%2064bit%20Download-v1.4.6-blue?logo=Linux)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-x86_64-unknown-linux-musl.tar.gz)
  [![Linux ARM64 Download](https://img.shields.io/badge/Linux%20ARM64%20Download-v1.4.6-blue?logo=Linux)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-aarch64-unknown-linux-musl.tar.gz)  
  
  [![MacOS 64-bit Download](https://img.shields.io/badge/macOS%2064bit%20Download-v1.4.6-blue?logo=Apple)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-x86_64-apple-darwin.tar.gz)
  [![MacOS ARM64 Download](https://img.shields.io/badge/macOS%20ARM64%20Download-v1.4.6-blue?logo=Apple)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-aarch64-apple-darwin.tar.gz)
  
  [![Windows 64-bit Download](https://img.shields.io/badge/Windows%2064bit%20Download-v1.4.6-blue?logo=Windows)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-x86_64-pc-windows-msvc.zip)
  [![Windows ARM64 Download](https://img.shields.io/badge/Windows%20ARM64%20Download-v1.4.6-blue?logo=Windows)](https://github.com/pemistahl/grex/releases/download/v1.4.6/grex-v1.4.6-aarch64-pc-windows-msvc.zip)
</div>

<br>

![grex demo](https://raw.githubusercontent.com/pemistahl/grex/main/demo.gif)

<br>

## 1. What does this tool do?

*grex* is a library as well as a command-line utility that is meant to simplify the often 
complicated and tedious task of creating regular expressions. It does so by automatically 
generating a single regular expression from user-provided test cases. The resulting
expression is guaranteed to match the test cases which it was generated from.

This project has started as a Rust port of the JavaScript tool 
[*regexgen*](https://github.com/devongovett/regexgen) written by 
[Devon Govett](https://github.com/devongovett). Although a lot of further useful features 
could be added to it, its development was apparently ceased several years ago. The plan 
is now to add these new features to *grex* as Rust really shines when it comes to 
command-line tools. *grex* offers all features that *regexgen* provides, and more.

The philosophy of this project is to generate the most specific regular expression 
possible by default which exactly matches the given input only and nothing else. 
With the use of command-line flags (in the CLI tool) or preprocessing methods 
(in the library), more generalized expressions can be created.

The produced expressions are [Perl-compatible regular expressions](https://www.pcre.org) which are also 
compatible with the regular expression parser in Rust's [*regex* crate](https://crates.io/crates/regex).
Other regular expression parsers or respective libraries from other programming languages 
have not been tested so far, but they ought to be mostly compatible as well.

## 2. Do I still need to learn to write regexes then?

**Definitely, yes!** Using the standard settings, *grex* produces a regular expression that is guaranteed
to match only the test cases given as input and nothing else. 
This has been verified by [property tests](https://github.com/pemistahl/grex/blob/main/tests/property_tests.rs).
However, if the conversion to shorthand character classes such as `\w` is enabled, the resulting regex matches
a much wider scope of test cases. Knowledge about the consequences of this conversion is essential for finding
a correct regular expression for your business domain.

*grex* uses an algorithm that tries to find the shortest possible regex for the given test cases.
Very often though, the resulting expression is still longer or more complex than it needs to be.
In such cases, a more compact or elegant regex can be created only by hand.
Also, every regular expression engine has different built-in optimizations. *grex* does not know anything
about those and therefore cannot optimize its regexes for a specific engine.

**So, please learn how to write regular expressions!** The currently best use case for *grex* is to find
an initial correct regex which should be inspected by hand if further optimizations are possible.  

## 3. Current Features
- literals
- character classes
- detection of common prefixes and suffixes
- detection of repeated substrings and conversion to `{min,max}` quantifier notation
- alternation using `|` operator
- optionality using `?` quantifier
- escaping of non-ascii characters, with optional conversion of astral code points to surrogate pairs
- case-sensitive or case-insensitive matching
- capturing or non-capturing groups
- optional anchors `^` and `$`
- fully compliant to [Unicode Standard 16.0](https://unicode.org/versions/Unicode15.0.0)
- fully compatible with [*regex* crate 1.11.0+](https://crates.io/crates/regex)
- correctly handles graphemes consisting of multiple Unicode symbols
- reads input strings from the command-line or from a file
- produces more readable expressions indented on multiple using optional verbose mode 
- optional syntax highlighting for nicer output in supported terminals

## 4. How to install?

### 4.1 The command-line tool

You can download the self-contained executable for your platform above and put it in a place of your choice. 
Alternatively, pre-compiled 64-Bit binaries are available within the package managers [Scoop](https://scoop.sh) 
(for Windows), [Homebrew](https://brew.sh) (for macOS and Linux), [MacPorts](https://www.macports.org) (for macOS), and [Huber](https://github.com/innobead/huber) (for macOS, Linux and Windows). 
[Raúl Piracés](https://github.com/piraces) has contributed a [Chocolatey Windows package](https://community.chocolatey.org/packages/grex).

*grex* is also hosted on [crates.io](https://crates.io/crates/grex), 
the official Rust package registry. If you are a Rust developer and already have the Rust 
toolchain installed, you can install by compiling from source using 
[*cargo*](https://doc.rust-lang.org/cargo/), the Rust package manager.
So the summary of your installation options is:

```
( brew | cargo | choco | huber | port | scoop ) install grex
```

### 4.2 The library

In order to use *grex* as a library, simply add it as a dependency to your `Cargo.toml` file:

```toml
[dependencies]
grex = { version = "1.4.6", default-features = false }
```

The dependency *clap* is only needed for the command-line tool.
By disabling the default features, the download and compilation of clap is prevented for the library.

## 5. How to use?

Detailed explanations of the available settings are provided in the [library section](#52-the-library).
All settings can be freely combined with each other.

### 5.1 The command-line tool

Test cases are passed either directly (`grex a b c`) or from a file (`grex -f test_cases.txt`).
*grex* is able to receive its input from Unix pipelines as well, e.g. `cat test_cases.txt | grex -`.

The following table shows all available flags and options:

```
$ grex -h

grex 1.4.6
© 2019-today Peter M. Stahl <pemistahl@gmail.com>
Licensed under the Apache License, Version 2.0
Downloadable from https://crates.io/crates/grex
Source code at https://github.com/pemistahl/grex

grex generates regular expressions from user-provided test cases.

Usage: grex [OPTIONS] {INPUT...|--file <FILE>}

Input:
  [INPUT]...         One or more test cases separated by blank space
  -f, --file <FILE>  Reads test cases on separate lines from a file

Digit Options:
  -d, --digits      Converts any Unicode decimal digit to \d
  -D, --non-digits  Converts any character which is not a Unicode decimal digit to \D

Whitespace Options:
  -s, --spaces      Converts any Unicode whitespace character to \s
  -S, --non-spaces  Converts any character which is not a Unicode whitespace character to \S

Word Options:
  -w, --words      Converts any Unicode word character to \w
  -W, --non-words  Converts any character which is not a Unicode word character to \W

Escaping Options:
  -e, --escape           Replaces all non-ASCII characters with unicode escape sequences
      --with-surrogates  Converts astral code points to surrogate pairs if --escape is set

Repetition Options:
  -r, --repetitions
          Detects repeated non-overlapping substrings and converts them to {min,max} quantifier
          notation
      --min-repetitions <QUANTITY>
          Specifies the minimum quantity of substring repetitions to be converted if --repetitions
          is set [default: 1]
      --min-substring-length <LENGTH>
          Specifies the minimum length a repeated substring must have in order to be converted if
          --repetitions is set [default: 1]

Anchor Options:
      --no-start-anchor  Removes the caret anchor `^` from the resulting regular expression
      --no-end-anchor    Removes the dollar sign anchor `$` from the resulting regular expression
      --no-anchors       Removes the caret and dollar sign anchors from the resulting regular
                         expression

Display Options:
  -x, --verbose   Produces a nicer-looking regular expression in verbose mode
  -c, --colorize  Provides syntax highlighting for the resulting regular expression

Miscellaneous Options:
  -i, --ignore-case     Performs case-insensitive matching, letters match both upper and lower case
  -g, --capture-groups  Replaces non-capturing groups with capturing ones
  -h, --help            Prints help information
  -v, --version         Prints version information

 
```

### 5.2 The library

#### 5.2.1 Default settings

Test cases are passed either from a collection via [`RegExpBuilder::from()`](https://docs.rs/grex/1.4.6/grex/struct.RegExpBuilder.html#method.from) 
or from a file via [`RegExpBuilder::from_file()`](https://docs.rs/grex/1.4.6/grex/struct.RegExpBuilder.html#method.from_file).
If read from a file, each test case must be on a separate line. Lines may be ended with either a newline `\n` or a carriage
return with a line feed `\r\n`.

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["a", "aa", "aaa"]).build();
assert_eq!(regexp, "^a(?:aa?)?$");
```

#### 5.2.2 Convert to character classes

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["a", "aa", "123"])
    .with_conversion_of_digits()
    .with_conversion_of_words()
    .build();
assert_eq!(regexp, "^(\\d\\d\\d|\\w(?:\\w)?)$");
```

#### 5.2.3 Convert repeated substrings

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["aa", "bcbc", "defdefdef"])
    .with_conversion_of_repetitions()
    .build();
assert_eq!(regexp, "^(?:a{2}|(?:bc){2}|(?:def){3})$");
```

By default, *grex* converts each substring this way which is at least a single character long 
and which is subsequently repeated at least once. You can customize these two parameters if you like.

In the following example, the test case `aa` is not converted to `a{2}` because the repeated substring 
`a` has a length of 1, but the minimum substring length has been set to 2.

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["aa", "bcbc", "defdefdef"])
    .with_conversion_of_repetitions()
    .with_minimum_substring_length(2)
    .build();
assert_eq!(regexp, "^(?:aa|(?:bc){2}|(?:def){3})$");
```

Setting a minimum number of 2 repetitions in the next example, only the test case `defdefdef` will be
converted because it is the only one that is repeated twice.

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["aa", "bcbc", "defdefdef"])
    .with_conversion_of_repetitions()
    .with_minimum_repetitions(2)
    .build();
assert_eq!(regexp, "^(?:bcbc|aa|(?:def){3})$");
```

#### 5.2.4 Escape non-ascii characters

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["You smell like 💩."])
    .with_escaping_of_non_ascii_chars(false)
    .build();
assert_eq!(regexp, "^You smell like \\u{1f4a9}\\.$");
```

Old versions of JavaScript do not support unicode escape sequences for the astral code planes 
(range `U+010000` to `U+10FFFF`). In order to support these symbols in JavaScript regular 
expressions, the conversion to surrogate pairs is necessary. More information on that matter 
can be found [here](https://mathiasbynens.be/notes/javascript-unicode).

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["You smell like 💩."])
    .with_escaped_non_ascii_chars(true)
    .build();
assert_eq!(regexp, "^You smell like \\u{d83d}\\u{dca9}\\.$");
```

#### 5.2.5 Case-insensitive matching

The regular expressions that *grex* generates are case-sensitive by default.
Case-insensitive matching can be enabled like so:

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["big", "BIGGER"])
    .with_case_insensitive_matching()
    .build();
assert_eq!(regexp, "(?i)^big(?:ger)?$");
```

#### 5.2.6 Capturing Groups

Non-capturing groups are used by default. 
Extending the previous example, you can switch to capturing groups instead.

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["big", "BIGGER"])
    .with_case_insensitive_matching()
    .with_capturing_groups()
    .build();
assert_eq!(regexp, "(?i)^big(ger)?$");
```

#### 5.2.7 Verbose mode

If you find the generated regular expression hard to read, you can enable verbose mode.
The expression is then put on multiple lines and indented to make it more pleasant to the eyes.

```rust
use grex::RegExpBuilder;
use indoc::indoc;

let regexp = RegExpBuilder::from(&["a", "b", "bcd"])
    .with_verbose_mode()
    .build();

assert_eq!(regexp, indoc!(
    r#"
    (?x)
    ^
      (?:
        b
        (?:
          cd
        )?
        |
        a
      )
    $"#
));
```

#### 5.2.8 Disable anchors

By default, the anchors `^` and `$` are put around every generated regular expression in order
to ensure that it matches only the test cases given as input. Often enough, however, it is
desired to use the generated pattern as part of a larger one. For this purpose, the anchors
can be disabled, either separately or both of them.

```rust
use grex::RegExpBuilder;

let regexp = RegExpBuilder::from(&["a", "aa", "aaa"])
    .without_anchors()
    .build();
assert_eq!(regexp, "a(?:aa?)?");
```

### 5.3 Examples

The following examples show the various supported regex syntax features:

```shell
$ grex a b c
^[a-c]$

$ grex a c d e f
^[ac-f]$

$ grex a b x de
^(?:de|[abx])$

$ grex abc bc
^a?bc$

$ grex a b bc
^(?:bc?|a)$

$ grex [a-z]
^\[a\-z\]$

$ grex -r b ba baa baaa
^b(?:a{1,3})?$

$ grex -r b ba baa baaaa
^b(?:a{1,2}|a{4})?$

$ grex y̆ a z
^(?:y̆|[az])$
Note: 
Grapheme y̆ consists of two Unicode symbols:
U+0079 (Latin Small Letter Y)
U+0306 (Combining Breve)

$ grex "I ♥ cake" "I ♥ cookies"
^I ♥ c(?:ookies|ake)$
Note:
Input containing blank space must be 
surrounded by quotation marks.
```

The string `"I ♥♥♥ 36 and ٣ and 💩💩."` serves as input for the following examples using the command-line notation:

```shell
$ grex <INPUT>
^I ♥♥♥ 36 and ٣ and 💩💩\.$

$ grex -e <INPUT>
^I \u{2665}\u{2665}\u{2665} 36 and \u{663} and \u{1f4a9}\u{1f4a9}\.$

$ grex -e --with-surrogates <INPUT>
^I \u{2665}\u{2665}\u{2665} 36 and \u{663} and \u{d83d}\u{dca9}\u{d83d}\u{dca9}\.$

$ grex -d <INPUT>
^I ♥♥♥ \d\d and \d and 💩💩\.$

$ grex -s <INPUT>
^I\s♥♥♥\s36\sand\s٣\sand\s💩💩\.$

$ grex -w <INPUT>
^\w ♥♥♥ \w\w \w\w\w \w \w\w\w 💩💩\.$

$ grex -D <INPUT>
^\D\D\D\D\D\D36\D\D\D\D\D٣\D\D\D\D\D\D\D\D$

$ grex -S <INPUT>
^\S \S\S\S \S\S \S\S\S \S \S\S\S \S\S\S$

$ grex -dsw <INPUT>
^\w\s♥♥♥\s\d\d\s\w\w\w\s\d\s\w\w\w\s💩💩\.$

$ grex -dswW <INPUT>
^\w\s\W\W\W\s\d\d\s\w\w\w\s\d\s\w\w\w\s\W\W\W$

$ grex -r <INPUT>
^I ♥{3} 36 and ٣ and 💩{2}\.$

$ grex -er <INPUT>
^I \u{2665}{3} 36 and \u{663} and \u{1f4a9}{2}\.$

$ grex -er --with-surrogates <INPUT>
^I \u{2665}{3} 36 and \u{663} and (?:\u{d83d}\u{dca9}){2}\.$

$ grex -dgr <INPUT>
^I ♥{3} \d(\d and ){2}💩{2}\.$

$ grex -rs <INPUT>
^I\s♥{3}\s36\sand\s٣\sand\s💩{2}\.$

$ grex -rw <INPUT>
^\w ♥{3} \w(?:\w \w{3} ){2}💩{2}\.$

$ grex -Dr <INPUT>
^\D{6}36\D{5}٣\D{8}$

$ grex -rS <INPUT>
^\S \S(?:\S{2} ){2}\S{3} \S \S{3} \S{3}$

$ grex -rW <INPUT>
^I\W{5}36\Wand\W٣\Wand\W{4}$

$ grex -drsw <INPUT>
^\w\s♥{3}\s\d(?:\d\s\w{3}\s){2}💩{2}\.$

$ grex -drswW <INPUT>
^\w\s\W{3}\s\d(?:\d\s\w{3}\s){2}\W{3}$
```                                                                                                                            

## 6. How to build?

In order to build the source code yourself, you need the 
[stable Rust toolchain](https://www.rust-lang.org/tools/install) installed on your machine 
so that [*cargo*](https://doc.rust-lang.org/cargo/), the Rust package manager is available.
**Please note**: Rust >= 1.70.0 is required to build the CLI. For the library part, Rust < 1.70.0 is sufficient.

```shell
git clone https://github.com/pemistahl/grex.git
cd grex
cargo build
```

The source code is accompanied by an extensive test suite consisting of unit tests, integration 
tests and property tests. For running them, simply say:

```shell
cargo test
```

Benchmarks measuring the performance of several settings can be run with:

```shell
cargo bench
```

## 7. Python extension module

With the help of [PyO3](https://github.com/PyO3/pyo3) and
[Maturin](https://github.com/PyO3/maturin), the library has been compiled to a
Python extension module so that it can be used within any Python software as well.
It is available in the [Python Package Index](https://pypi.org/project/grex) and can 
be installed with:

```shell
pip install grex
```

To build the Python extension module yourself, create a virtual environment and install 
[Maturin](https://github.com/PyO3/maturin).

```shell
python -m venv /path/to/virtual/environment
source /path/to/virtual/environment/bin/activate
pip install maturin
maturin build
```

The Python library contains a single class named `RegExpBuilder` that can be imported like so:

```python
from grex import RegExpBuilder
```

## 8. WebAssembly support

This library can be compiled to [WebAssembly (WASM)](https://webassembly.org) which allows to use *grex*
in any JavaScript-based project, be it in the browser or in the back end running on [Node.js](https://nodejs.org).

The easiest way to compile is to use [`wasm-pack`](https://rustwasm.github.io/wasm-pack). After the installation,
you can, for instance, build the library with the web target so that it can be directly used in the browser:

    wasm-pack build --target web

This creates a directory named `pkg` on the top-level of this repository, containing the compiled wasm files
and JavaScript and TypeScript bindings. In an HTML file, you can then call *grex* like the following, for instance:

```html
<script type="module">
    import init, { RegExpBuilder } from "./pkg/grex.js";

    init().then(_ => {
        alert(RegExpBuilder.from(["hello", "world"]).build());
    });
</script>
```

There are also some integration tests available both for Node.js and for the browsers Chrome, Firefox and Safari.
To run them, simply say:

    wasm-pack test --node --headless --chrome --firefox --safari

If the tests fail to start in Safari, you need to enable Safari's web driver first by running:

    sudo safaridriver --enable

The output of `wasm-pack` will be hosted in a [separate repository](https://github.com/pemistahl/grex-js) which
allows to add further JavaScript-related configuration, tests and documentation. *grex* will then be added to the
[npm registry](https://www.npmjs.com) as well, allowing for an easy download and installation within every JavaScript
or TypeScript project.

There is a [demo website](https://pemistahl.github.io/grex-js/) available where you can give grex a try.

![demo website](https://raw.githubusercontent.com/pemistahl/grex/main/website.jpg)

## 9. How does it work?

1. A [deterministic finite automaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton) (DFA) 
is created from the input strings.

2. The number of states and transitions between states in the DFA is reduced by applying 
[Hopcroft's DFA minimization algorithm](https://en.wikipedia.org/wiki/DFA_minimization#Hopcroft.27s_algorithm).

3. The minimized DFA is expressed as a system of linear equations which are solved with 
[Brzozowski's algebraic method](http://cs.stackexchange.com/questions/2016/how-to-convert-finite-automata-to-regular-expressions#2392), 
resulting in the final regular expression.

## 10. What's next for version 1.5.0?

Take a look at the [planned issues](https://github.com/pemistahl/grex/milestone/5).

## 11. Contributions

In case you want to contribute something to *grex*, I encourage you to do so.
Do you have ideas for cool features? Or have you found any bugs so far? 
Feel free to open an issue or send a pull request. It's very much appreciated. :-)
```

## File: `README_PYPI.md`
```markdown
<div align="center">

![grex](https://raw.githubusercontent.com/pemistahl/grex/main/logo.png)

<br>

[![build status](https://github.com/pemistahl/grex/actions/workflows/python-build.yml/badge.svg)](https://github.com/pemistahl/grex/actions/workflows/python-build.yml)
[![codecov](https://codecov.io/gh/pemistahl/grex/branch/main/graph/badge.svg)](https://codecov.io/gh/pemistahl/grex)
[![demo](https://img.shields.io/badge/-Demo%20Website-orange?logo=HTML5&labelColor=white)](https://pemistahl.github.io/grex-js/)
![supported Python versions](https://img.shields.io/badge/Python-%3E%3D%203.12-blue?logo=Python&logoColor=yellow)
[![pypi](https://img.shields.io/badge/PYPI-v1.0.2-blue?logo=PyPI&logoColor=yellow)](https://pypi.org/project/grex)
[![license](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0)
</div>

<br>

## 1. What does this library do?

*grex* is a library that is meant to simplify the often complicated and tedious
task of creating regular expressions. It does so by automatically generating a
single regular expression from user-provided test cases. The resulting
expression is guaranteed to match the test cases which it was generated from.

This project has started as a [Rust port](https://github.com/pemistahl/grex) of
the JavaScript tool [*regexgen*](https://github.com/devongovett/regexgen)
written by [Devon Govett](https://github.com/devongovett). Although a lot of
further useful features could be added to it, its development was apparently
ceased several years ago. The Rust library offers new features and extended
Unicode support. With the help of [PyO3](https://github.com/PyO3/pyo3) and 
[Maturin](https://github.com/PyO3/maturin), the library has been compiled to a 
Python extension module so that it can be used within any Python software as well.

The philosophy of this project is to generate the most specific regular expression
possible by default which exactly matches the given input only and nothing else.
With the use of preprocessing methods, more generalized expressions can be created.

The produced expressions are [Perl-compatible regular expressions](https://www.pcre.org) which are also
compatible with the [regular expression module](https://docs.python.org/3/library/re.html) in Python's 
standard library.

There is a [demo website](https://pemistahl.github.io/grex-js/) available where you can give grex a try.

![demo website](https://raw.githubusercontent.com/pemistahl/grex/main/website.jpg)

## 2. Do I still need to learn to write regexes then?

**Definitely, yes!** Using the standard settings, *grex* produces a regular expression that is guaranteed
to match only the test cases given as input and nothing else. However, if the conversion to shorthand
character classes such as `\w` is enabled, the resulting regex matches a much wider scope of test cases.
Knowledge about the consequences of this conversion is essential for finding a correct regular expression
for your business domain.

*grex* uses an algorithm that tries to find the shortest possible regex for the given test cases.
Very often though, the resulting expression is still longer or more complex than it needs to be.
In such cases, a more compact or elegant regex can be created only by hand.
Also, every regular expression engine has different built-in optimizations. *grex* does not know anything
about those and therefore cannot optimize its regexes for a specific engine.

**So, please learn how to write regular expressions!** The currently best use case for *grex* is to find
an initial correct regex which should be inspected by hand if further optimizations are possible.

## 3. Current Features

- literals
- character classes
- detection of common prefixes and suffixes
- detection of repeated substrings and conversion to `{min,max}` quantifier notation
- alternation using `|` operator
- optionality using `?` quantifier
- escaping of non-ascii characters, with optional conversion of astral code points to surrogate pairs
- case-sensitive or case-insensitive matching
- capturing or non-capturing groups
- optional anchors `^` and `$`
- fully compliant to [Unicode Standard 16.0](https://unicode.org/versions/Unicode16.0.0)
- correctly handles graphemes consisting of multiple Unicode symbols
- produces more readable expressions indented on multiple using optional verbose mode
- optional syntax highlighting for nicer output in supported terminals

## 4. How to install?

*grex* is available in the [Python Package Index](https://pypi.org/project/grex) and can be installed with:

```
pip install grex
```

The current version 1.0.2 corresponds to the latest version 1.4.6 of the Rust
library and command-line tool.

## 5. How to use?

This library contains a single class named `RegExpBuilder` that can be imported like so:

```python
from grex import RegExpBuilder
```

### 5.1 Default settings

```python
pattern = RegExpBuilder.from_test_cases(["a", "aa", "aaa"]).build()
assert pattern == "^a(?:aa?)?$"
```

### 5.2 Convert to character classes

```python
pattern = (RegExpBuilder.from_test_cases(["a", "aa", "123"])
    .with_conversion_of_digits()
    .with_conversion_of_words()
    .build())
assert pattern == "^(?:\\d\\d\\d|\\w(?:\\w)?)$"
```

### 5.3 Convert repeated substrings

```python
pattern = (RegExpBuilder.from_test_cases(["aa", "bcbc", "defdefdef"])
    .with_conversion_of_repetitions()
    .build())
assert pattern == "^(?:a{2}|(?:bc){2}|(?:def){3})$"
```

By default, *grex* converts each substring this way which is at least a single character long
and which is subsequently repeated at least once. You can customize these two parameters if you like.

In the following example, the test case `aa` is not converted to `a{2}` because the repeated substring
`a` has a length of 1, but the minimum substring length has been set to 2.

```python
pattern = (RegExpBuilder.from_test_cases(["aa", "bcbc", "defdefdef"])
    .with_conversion_of_repetitions()
    .with_minimum_substring_length(2)
    .build())
assert pattern == "^(?:aa|(?:bc){2}|(?:def){3})$"
```

Setting a minimum number of 2 repetitions in the next example, only the test case `defdefdef` will be
converted because it is the only one that is repeated twice.

```python
pattern = (RegExpBuilder.from_test_cases(["aa", "bcbc", "defdefdef"])
    .with_conversion_of_repetitions()
    .with_minimum_repetitions(2)
    .build())
assert pattern == "^(?:bcbc|aa|(?:def){3})$"
```

### 5.4 Escape non-ascii characters

```python
pattern = (RegExpBuilder.from_test_cases(["You smell like 💩."])
    .with_escaping_of_non_ascii_chars(use_surrogate_pairs=False)
    .build())
assert pattern == "^You smell like \\U0001f4a9\\.$"
```

Old versions of JavaScript do not support unicode escape sequences for the astral code planes
(range `U+010000` to `U+10FFFF`). In order to support these symbols in JavaScript regular
expressions, the conversion to surrogate pairs is necessary. More information on that matter
can be found [here](https://mathiasbynens.be/notes/javascript-unicode).

```python
pattern = (RegExpBuilder.from_test_cases(["You smell like 💩."])
    .with_escaping_of_non_ascii_chars(use_surrogate_pairs=True)
    .build())
assert pattern == "^You smell like \\ud83d\\udca9\\.$"
```

### 5.5 Case-insensitive matching

The regular expressions that *grex* generates are case-sensitive by default.
Case-insensitive matching can be enabled like so:

```python
pattern = (RegExpBuilder.from_test_cases(["big", "BIGGER"])
    .with_case_insensitive_matching()
    .build())
assert pattern == "(?i)^big(?:ger)?$"
```

### 5.6 Capturing Groups

Non-capturing groups are used by default.
Extending the previous example, you can switch to capturing groups instead.

```python
pattern = (RegExpBuilder.from_test_cases(["big", "BIGGER"])
    .with_case_insensitive_matching()
    .with_capturing_groups()
    .build())
assert pattern == "(?i)^big(ger)?$"
```

### 5.7 Verbose mode

If you find the generated regular expression hard to read, you can enable verbose mode.
The expression is then put on multiple lines and indented to make it more pleasant to the eyes.

```python
import inspect

pattern = (RegExpBuilder.from_test_cases(["a", "b", "bcd"])
    .with_verbose_mode()
    .build())

assert pattern == inspect.cleandoc("""
    (?x)
    ^
      (?:
        b
        (?:
          cd
        )?
        |
        a
      )
    $
    """
)
```

### 5.8 Disable anchors

By default, the anchors `^` and `$` are put around every generated regular expression in order
to ensure that it matches only the test cases given as input. Often enough, however, it is
desired to use the generated pattern as part of a larger one. For this purpose, the anchors
can be disabled, either separately or both of them.

```python
pattern = (RegExpBuilder.from_test_cases(["a", "aa", "aaa"])
    .without_anchors()
    .build())
assert pattern == "a(?:aa?)?"
```

## 6. How to build?

In order to build the source code yourself, you need the
[stable Rust toolchain](https://www.rust-lang.org/tools/install) installed on your machine
so that [*cargo*](https://doc.rust-lang.org/cargo/), the Rust package manager is available.

```shell
git clone https://github.com/pemistahl/grex.git
cd grex
cargo build
```

To build the Python extension module, create a virtual environment and install [Maturin](https://github.com/PyO3/maturin).

```shell
python -m venv /path/to/virtual/environment
source /path/to/virtual/environment/bin/activate
pip install maturin
maturin build
```

The Rust source code is accompanied by an extensive test suite consisting of unit tests, integration
tests and property tests. For running them, simply say:

```shell
cargo test
```

Additional Python tests can be run after installing pytest which is an optional dependency:

```shell
maturin develop --extras=test
pytest tests/python/test_grex.py
```
```

## File: `RELEASE_NOTES.md`
```markdown
## grex 1.4.6 (released on 14 Nov 2025)

### Improvements
- All characters from the current Unicode standard 16.0 are now fully supported.

### Changes

- The unmaintained unic-* dependencies have been replaced by @jqnatividad. (#337)
- All other dependencies have been updated to their latest versions.
- Support for Python 3.14 has been added.
- Support for Python < 3.12 has been dropped.

## grex 1.4.5 (released on 06 Mar 2024)

### Improvements

- Type stubs for the Python bindings are now available, allowing better static code 
  analysis, better code completion in supported IDEs and easier understanding of the library's API.
- The code for creating regular expressions in verbose mode has been simplified and is more performant now.
- ARM64 binaries are now provided for every major platform (Linux, macOs, Windows).

### Bug Fixes

- For a small set of special characters, *grex* produced incorrect regular expressions when
  the case-insensitivity feature was enabled. This has been fixed.

### Changes
- All dependencies have been updated to their latest versions.

## grex 1.4.4 (released on 24 Aug 2023)

### Bug Fixes
- The Python release workflow was incorrect as it produced too many wheels for upload.
  This has been fixed.

## grex 1.4.3 (released on 24 Aug 2023)

### Features
- Python bindings are now available for the library. Use grex within any Python software. (#172)

### Changes
- All dependencies have been updated to their latest versions.

## grex 1.4.2 (released on 26 Jul 2023)

### Improvements
- All characters from the current Unicode standard 15.0 are now fully supported. (#128)
- A proper exit code is now returned if the provided user input cannot be handled by the CLI.
  Big thanks to @spenserblack for the respective pull request. (#165)

### Changes
- It is not possible anymore to call `RegExpBuilder.with_syntax_highlighting()` in the library
  as it only makes sense for the CLI.
- The dependency `atty` has been removed in favor of `std::io::IsTerminal` in Rust >= 1.70.0.
  As a result, Rust >= 1.70.0 is now needed to compile the CLI. 
- All remaining dependencies have been updated to their latest versions.

### Bug Fixes
- Several bugs have been fixed that caused incorrect expressions to be generated in rare cases.

## grex 1.4.1 (released on 21 Oct 2022)

### Changes
- `clap` has been updated to version 4.0. The help output by `grex -h` now looks a little different.

### Bug Fixes
- A bug in the grapheme segmentation was fixed that caused test cases which contain backslashes to produce
  incorrect regular expressions.

## grex 1.4.0 (released on 26 Jul 2022)

### Features
- The library can now be compiled to WebAssembly and be used in any JavaScript project. (#82)
- The supported character set for regular expression generation has been updated to the current Unicode Standard 14.0.
- `structopt` has been replaced with `clap` providing much nicer help output for the command-line tool.

### Improvements
- The regular expression generation performance has been significantly improved, especially for generating very long
  expressions from a large set of test cases. This has been accomplished by reducing the number of memory allocations,
  removing deprecated code and applying several minor optimizations.

### Bug Fixes
- Several bugs have been fixed that caused incorrect expressions to be generated in rare cases.

## grex 1.3.0 (released on 15 Sep 2021)

### Features
- anchors can now be disabled so that the generated expression can be used as part of a larger one (#30)
- the command-line tool can now be used within Unix pipelines (#45)

### Changes
- Additional methods have been added to `RegExpBuilder` in order to replace the enum `Feature` and make the library API more consistent. (#47)

### Bug Fixes
- Under rare circumstances, the conversion of repetitions did not work. This has been fixed. (#36)

## grex 1.2.0 (released on 28 Mar 2021)

### Features
- verbose mode is now supported with the `--verbose` flag to produce regular expressions which are easier to read (#17)

## grex 1.1.0 (released on 17 Apr 2020)

### Features
- case-insensitive matching regexes are now supported with the `--ignore-case` command-line flag or with `Feature::CaseInsensitivity` in the library (#23)
- non-capturing groups are now the default; capturing groups can be enabled with the `--capture-groups` command-line flag or with `Feature::CapturingGroup` in the library (#15)
- a lower bound for the conversion of repeated substrings can now be set by specifying `--min-repetitions` and `--min-substring-length` or using the library methods `RegExpBuilder.with_minimum_repetitions()` and `RegExpBuilder.with_minimum_substring_length()` (#10)
- test cases can now be passed from a file within the library as well using `RegExpBuilder::from_file()` (#13)

### Changes

- the rules for the conversion of test cases to shorthand character classes have been updated to be compliant to the newest Unicode Standard 13.0 (#21)
- the dependency on the unmaintained linked-list crate has been removed (#24)

### Bug Fixes

- test cases starting with a hyphen are now correctly parsed on the command-line (#12)
- the common substring detection algorithm now uses optionality expressions where possible instead of redundant union operations (#22)

### Test Coverage
- new unit tests, integration tests and property tests have been added

## grex 1.0.0 (released on 02 Feb 2020)

### Features
- conversion to character classes `\d`, `\D`, `\s`, `\S`, `\w`, `\W` is now supported
- repetition detection now works with arbitrarily nested expressions. Input strings such as `aaabaaab` which were previously converted to `^(aaab){2}$` are now converted to `^(a{3}b){2}$`.
- optional syntax highlighting for the produced regular expressions can now be enabled using the `--colorize` command-line flag or with the library method `RegExpBuilder.with_syntax_highlighting()`

### Test Coverage
- new unit tests, integration tests and property tests have been added

## grex 0.3.2 (released on 12 Jan 2020)

### Test Coverage
- new property tests have been added that revealed new bugs

### Bug Fixes
- entire rewrite of the repetition detection algorithm
- the former algorithm produced wrong regular expressions or even panicked for certain test cases

## grex 0.3.1 (released on 06 Jan 2020)

### Test Coverage
- property tests have been added using the [proptest](https://crates.io/crates/proptest) crate 
- big thanks go to [Christophe Biocca](https://github.com/christophebiocca) for pointing me to the concept of property tests in the first place and for writing an initial implementation of these tests

### Bug Fixes
- some regular expression specific characters were not escaped correctly in the generated expression
- expressions consisting of a single alternation such as `^(abc|xyz)$` were missing the outer parentheses. This caused an erroneous match of strings such as `abc123` or `456xyz` because of precedence rules.
- the created DFA was wrong for repetition conversion in some corner cases. The input `a, aa, aaa, aaaa, aaab` previously returned the expression `^a{1,4}b?$` which erroneously matches `aaaab`. Now the correct expression `^(a{3}b|a{1,4})$` is returned.

### Documentation
- some minor documentation updates

## grex 0.3.0 (released on 24 Dec 2019)

### Features
- *grex* is now also available as a library
- escaping of non-ascii characters is now supported with the `-e` flag
- astral code points can be converted to surrogate with the `--with-surrogates` flag
- repeated non-overlapping substrings can be converted to `{min,max}` quantifier notation using the `-r` flag

### Bug Fixes
- many many many bug fixes :-O

## grex 0.2.0 (released on 20 Oct 2019)

### Features
- character classes are now supported
- input strings can now be read from a text file

### Changes
- unicode characters are not escaped anymore by default
- the performance of the DFA minimization algorithm has been improved for large DFAs
- regular expressions are now always surrounded by anchors `^` and `$`

### Bug Fixes
- fixed a bug that caused a panic when giving an empty string as input

## grex 0.1.0 (released on 06 Oct 2019)

This is the very first release of *grex*. It aims at simplifying the construction of regular expressions based on matching example input.

### Features
- literals
- detection of common prefixes and suffixes
- alternation using `|` operator
- optionality using `?` quantifier
- concatenation of all of the former
```

## File: `requirements.txt`
```
maturin == 1.10.1
pytest == 9.0.1
```

## File: `benches/benchmark.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use criterion::{criterion_group, criterion_main, Criterion};
use grex::RegExpBuilder;
use itertools::Itertools;
use std::fs::File;
use std::io::Read;

fn load_test_cases() -> Vec<String> {
    let mut f = File::open("./benches/testcases.txt").expect("Test cases could not be loaded");
    let mut s = String::new();
    f.read_to_string(&mut s).unwrap();
    s.split("\n")
        .map(|test_case| test_case.to_string())
        .collect_vec()
}

fn benchmark_grex_with_default_settings(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with default settings", |bencher| {
        bencher.iter(|| RegExpBuilder::from(&test_cases).build())
    });
}

fn benchmark_grex_with_conversion_of_repetitions(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with conversion of repetitions", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .build()
        })
    });
}

fn benchmark_grex_with_conversion_of_digits(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with conversion of digits", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .build()
        })
    });
}

fn benchmark_grex_with_conversion_of_non_digits(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with conversion of non-digits", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_digits()
                .build()
        })
    });
}

fn benchmark_grex_with_conversion_of_words(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with conversion of words", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_conversion_of_words()
                .build()
        })
    });
}

fn benchmark_grex_with_conversion_of_non_words(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with conversion of non-words", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_words()
                .build()
        })
    });
}

fn benchmark_grex_with_conversion_of_whitespace(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with conversion of whitespace", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .build()
        })
    });
}

fn benchmark_grex_with_conversion_of_non_whitespace(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with conversion of non-whitespace", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_whitespace()
                .build()
        })
    });
}

fn benchmark_grex_with_case_insensitive_matching(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with case-insensitive matching", |bencher| {
        bencher.iter(|| {
            RegExpBuilder::from(&test_cases)
                .with_case_insensitive_matching()
                .build()
        })
    });
}

fn benchmark_grex_with_verbose_mode(c: &mut Criterion) {
    let test_cases = load_test_cases();
    c.bench_function("grex with verbose mode", |bencher| {
        bencher.iter(|| RegExpBuilder::from(&test_cases).with_verbose_mode().build())
    });
}

criterion_group!(
    benches,
    benchmark_grex_with_default_settings,
    benchmark_grex_with_conversion_of_repetitions,
    benchmark_grex_with_conversion_of_digits,
    benchmark_grex_with_conversion_of_non_digits,
    benchmark_grex_with_conversion_of_words,
    benchmark_grex_with_conversion_of_non_words,
    benchmark_grex_with_conversion_of_whitespace,
    benchmark_grex_with_conversion_of_non_whitespace,
    benchmark_grex_with_case_insensitive_matching,
    benchmark_grex_with_verbose_mode
);

criterion_main!(benches);
```

## File: `benches/testcases.txt`
```
Rocket Sled
Elysian Heirloom
Kaleb's Favor
Blazing Renegade
Flash Fire
Silence
Talir's Favored
Timekeeper
Oasis Sanctuary
Rolant's Favor
Mantle of Justice
Eilyn's Favor
Thunderbird
Primal Incarnation
Vampire Bat
Vara's Favor
Devouring Shadow
Seat of Order
Seat of Fury
Seat of Impulse
Seat of Vengeance
Seat of Glory
Seat of Progress
Seat of Chaos
Seat of Mystery
Seat of Cunning
Seat of Wisdom
Firebomb
Grenadin
Iron Sword
Magmahound
Wisp
Rhinarc
Sentinel
Owl
Gemblade
Frog
Snowball
Pig
Serpent Hatchling
Carnosaur
Stormdancer
Illusionary Dragon
Spiteling
Vengeful Gargoyle
Muertis, Pale Rider
Occi, Pale Rider
Sangu, Pale Rider
Volan, Pale Rider
Direwood Beast
```

## File: `src/builder.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::config::RegExpConfig;
use crate::regexp::RegExp;
use itertools::Itertools;
use std::io::ErrorKind;
use std::path::PathBuf;

pub(crate) const MISSING_TEST_CASES_MESSAGE: &str =
    "No test cases have been provided for regular expression generation";

pub(crate) const MINIMUM_REPETITIONS_MESSAGE: &str =
    "Quantity of minimum repetitions must be greater than zero";

pub(crate) const MINIMUM_SUBSTRING_LENGTH_MESSAGE: &str =
    "Minimum substring length must be greater than zero";

/// This struct builds regular expressions from user-provided test cases.
#[derive(Clone)]
#[cfg_attr(feature = "python", pyo3::prelude::pyclass)]
pub struct RegExpBuilder {
    pub(crate) test_cases: Vec<String>,
    pub(crate) config: RegExpConfig,
}

impl RegExpBuilder {
    /// Specifies the test cases to build the regular expression from.
    ///
    /// The test cases need not be sorted because `RegExpBuilder` sorts them internally.
    ///
    /// ⚠ Panics if `test_cases` is empty.
    pub fn from<T: Clone + Into<String>>(test_cases: &[T]) -> Self {
        if test_cases.is_empty() {
            panic!("{}", MISSING_TEST_CASES_MESSAGE);
        }
        Self {
            test_cases: test_cases.iter().cloned().map(|it| it.into()).collect_vec(),
            config: RegExpConfig::new(),
        }
    }

    /// Specifies a text file containing test cases to build the regular expression from.
    ///
    /// The test cases need not be sorted because `RegExpBuilder` sorts them internally.
    ///
    /// Each test case needs to be on a separate line.
    /// Lines may be ended with either a newline (`\n`) or
    /// a carriage return with a line feed (`\r\n`).
    /// The final line ending is optional.
    ///
    /// ⚠ Panics if:
    /// - the file cannot be found
    /// - the file's encoding is not valid UTF-8 data
    /// - the file cannot be opened because of conflicting permissions
    pub fn from_file<T: Into<PathBuf>>(file_path: T) -> Self {
        match std::fs::read_to_string(file_path.into()) {
            Ok(file_content) => Self {
                test_cases: file_content.lines().map(|it| it.to_string()).collect_vec(),
                config: RegExpConfig::new(),
            },
            Err(error) => match error.kind() {
                ErrorKind::NotFound => panic!("The specified file could not be found"),
                ErrorKind::InvalidData => {
                    panic!("The specified file's encoding is not valid UTF-8")
                }
                ErrorKind::PermissionDenied => {
                    panic!("Permission denied: The specified file could not be opened")
                }
                _ => panic!("{}", error),
            },
        }
    }

    /// Converts any Unicode decimal digit to character class `\d`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_words`](Self::with_conversion_of_words) if both are set.
    /// Decimal digits are converted to `\d`, the remaining word characters to `\w`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_whitespace`](Self::with_conversion_of_non_whitespace) if both are set.
    /// Decimal digits are converted to `\d`, the remaining non-whitespace characters to `\S`.
    pub fn with_conversion_of_digits(&mut self) -> &mut Self {
        self.config.is_digit_converted = true;
        self
    }

    /// Converts any character which is not a Unicode decimal digit to character class `\D`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_words`](Self::with_conversion_of_non_words) if both are set.
    /// Non-digits which are also non-word characters are converted to `\D`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_whitespace`](Self::with_conversion_of_non_whitespace) if both are set.
    /// Non-digits which are also non-space characters are converted to `\D`.
    pub fn with_conversion_of_non_digits(&mut self) -> &mut Self {
        self.config.is_non_digit_converted = true;
        self
    }

    /// Converts any Unicode whitespace character to character class `\s`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_digits`](Self::with_conversion_of_non_digits) if both are set.
    /// Whitespace characters are converted to `\s`, the remaining non-digit characters to `\D`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_words`](Self::with_conversion_of_non_words) if both are set.
    /// Whitespace characters are converted to `\s`, the remaining non-word characters to `\W`.
    pub fn with_conversion_of_whitespace(&mut self) -> &mut Self {
        self.config.is_space_converted = true;
        self
    }

    /// Converts any character which is not a Unicode whitespace character to character class `\S`.
    pub fn with_conversion_of_non_whitespace(&mut self) -> &mut Self {
        self.config.is_non_space_converted = true;
        self
    }

    /// Converts any Unicode word character to character class `\w`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_digits`](Self::with_conversion_of_non_digits) if both are set.
    /// Word characters are converted to `\w`, the remaining non-digit characters to `\D`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_whitespace`](Self::with_conversion_of_non_whitespace) if both are set.
    /// Word characters are converted to `\w`, the remaining non-space characters to `\S`.
    pub fn with_conversion_of_words(&mut self) -> &mut Self {
        self.config.is_word_converted = true;
        self
    }

    /// Converts any character which is not a Unicode word character to character class `\W`.
    ///
    /// This method takes precedence over
    /// [`with_conversion_of_non_whitespace`](Self::with_conversion_of_non_whitespace) if both are set.
    /// Non-words which are also non-space characters are converted to `\W`.
    pub fn with_conversion_of_non_words(&mut self) -> &mut Self {
        self.config.is_non_word_converted = true;
        self
    }

    /// Detects repeated non-overlapping substrings and
    /// to convert them to `{min,max}` quantifier notation.
    pub fn with_conversion_of_repetitions(&mut self) -> &mut Self {
        self.config.is_repetition_converted = true;
        self
    }

    /// Enables case-insensitive matching of test cases
    /// so that letters match both upper and lower case.
    pub fn with_case_insensitive_matching(&mut self) -> &mut Self {
        self.config.is_case_insensitive_matching = true;
        self
    }

    /// Replaces non-capturing groups with capturing ones.
    pub fn with_capturing_groups(&mut self) -> &mut Self {
        self.config.is_capturing_group_enabled = true;
        self
    }

    /// Specifies the minimum quantity of substring repetitions to be converted if
    /// [`with_conversion_of_repetitions`](Self::with_conversion_of_repetitions) is set.
    ///
    /// If the quantity is not explicitly set with this method, a default value of 1 will be used.
    ///
    /// ⚠ Panics if `quantity` is zero.
    pub fn with_minimum_repetitions(&mut self, quantity: u32) -> &mut Self {
        if quantity == 0 {
            panic!("{}", MINIMUM_REPETITIONS_MESSAGE);
        }
        self.config.minimum_repetitions = quantity;
        self
    }

    /// Specifies the minimum length a repeated substring must have in order to be converted if
    /// [`with_conversion_of_repetitions`](Self::with_conversion_of_repetitions) is set.
    ///
    /// If the length is not explicitly set with this method, a default value of 1 will be used.
    ///
    /// ⚠ Panics if `length` is zero.
    pub fn with_minimum_substring_length(&mut self, length: u32) -> &mut Self {
        if length == 0 {
            panic!("{}", MINIMUM_SUBSTRING_LENGTH_MESSAGE);
        }
        self.config.minimum_substring_length = length;
        self
    }

    /// Converts non-ASCII characters to unicode escape sequences.
    /// The parameter `use_surrogate_pairs` specifies whether to convert astral code planes
    /// (range `U+010000` to `U+10FFFF`) to surrogate pairs.
    pub fn with_escaping_of_non_ascii_chars(&mut self, use_surrogate_pairs: bool) -> &mut Self {
        self.config.is_non_ascii_char_escaped = true;
        self.config.is_astral_code_point_converted_to_surrogate = use_surrogate_pairs;
        self
    }

    /// Produces a nicer looking regular expression in verbose mode.
    pub fn with_verbose_mode(&mut self) -> &mut Self {
        self.config.is_verbose_mode_enabled = true;
        self
    }

    /// Removes the caret anchor '^' from the resulting regular
    /// expression, thereby allowing to match the test cases also when they do not occur
    /// at the start of a string.
    pub fn without_start_anchor(&mut self) -> &mut Self {
        self.config.is_start_anchor_disabled = true;
        self
    }

    /// Removes the dollar sign anchor '$' from the resulting regular
    /// expression, thereby allowing to match the test cases also when they do not occur
    /// at the end of a string.
    pub fn without_end_anchor(&mut self) -> &mut Self {
        self.config.is_end_anchor_disabled = true;
        self
    }

    /// Removes the caret and dollar sign anchors from the resulting
    /// regular expression, thereby allowing to match the test cases also when they occur
    /// within a larger string that contains other content as well.
    pub fn without_anchors(&mut self) -> &mut Self {
        self.config.is_start_anchor_disabled = true;
        self.config.is_end_anchor_disabled = true;
        self
    }

    /// Provides syntax highlighting for the resulting regular expression.
    ///
    /// ⚠ This method may only be used if the resulting regular expression is meant to
    /// be printed to the console. The regex string representation returned from enabling
    /// this setting cannot be fed into the [*regex*](https://crates.io/crates/regex) crate.
    #[cfg(feature = "cli")]
    #[doc(hidden)]
    pub fn with_syntax_highlighting(&mut self) -> &mut Self {
        self.config.is_output_colorized = true;
        self
    }

    /// Builds the actual regular expression using the previously given settings.
    pub fn build(&mut self) -> String {
        RegExp::from(&mut self.test_cases, &self.config).to_string()
    }
}
```

## File: `src/char_range.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/// A lightweight replacement for unic_char_range::CharRange
/// Represents a closed range of Unicode characters
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub(crate) struct CharRange {
    start: char,
    end: char,
}

impl CharRange {
    /// Creates a closed character range from start to end (inclusive)
    pub(crate) fn closed(start: char, end: char) -> Self {
        Self { start, end }
    }

    /// Checks if the given character is within this range
    pub(crate) fn contains(&self, c: char) -> bool {
        c >= self.start && c <= self.end
    }

    /// Returns an iterator over all valid Unicode scalar values
    /// This includes U+0000 to U+D7FF and U+E000 to U+10FFFF
    /// (excludes surrogate code points U+D800 to U+DFFF)
    pub(crate) fn all() -> CharRangeIter {
        CharRangeIter {
            current: '\0',
            done: false,
        }
    }
}

/// Iterator over all valid Unicode scalar values
pub(crate) struct CharRangeIter {
    current: char,
    done: bool,
}

impl Iterator for CharRangeIter {
    type Item = char;

    fn next(&mut self) -> Option<Self::Item> {
        if self.done {
            return None;
        }

        let result = self.current;

        // Get the next valid Unicode scalar value
        let mut next_code_point = self.current as u32 + 1;

        // Skip over surrogate code points (U+D800 to U+DFFF) and find next valid char
        loop {
            if next_code_point > 0x10FFFF {
                // We've reached the end of valid Unicode code points
                self.done = true;
                break;
            }

            match char::from_u32(next_code_point) {
                Some(next_char) => {
                    self.current = next_char;
                    break;
                }
                None => {
                    // Invalid code point (likely surrogate), skip to next
                    next_code_point += 1;
                }
            }
        }

        Some(result)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_char_range_contains() {
        let range = CharRange::closed('a', 'z');
        assert!(range.contains('a'));
        assert!(range.contains('m'));
        assert!(range.contains('z'));
        assert!(!range.contains('A'));
        assert!(!range.contains('0'));
    }

    #[test]
    fn test_char_range_all() {
        let all_chars: Vec<char> = CharRange::all().take(10).collect();
        assert_eq!(all_chars[0], '\0');
        assert_eq!(all_chars.len(), 10);
    }

    #[test]
    fn test_char_range_all_count() {
        // Valid Unicode scalar values: 0x110000 total code points - 0x800 surrogates = 0x10F800
        let count = CharRange::all().count();
        assert_eq!(count, 0x10F800);
    }
}
```

## File: `src/cluster.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::char_range::CharRange;
use crate::config::RegExpConfig;
use crate::grapheme::Grapheme;
use crate::unicode_tables::{DECIMAL_NUMBER, WHITE_SPACE, WORD};
use itertools::Itertools;
use std::cmp::Ordering;
use std::collections::HashMap;
use std::ops::Range;
use std::sync::LazyLock;
use unicode_general_category::GeneralCategory as GC;
use unicode_segmentation::UnicodeSegmentation;

#[derive(Clone, Debug, Eq, PartialEq)]
pub(crate) struct GraphemeCluster<'a> {
    graphemes: Vec<Grapheme>,
    config: &'a RegExpConfig,
}

impl<'a> GraphemeCluster<'a> {
    pub(crate) fn from(s: &str, config: &'a RegExpConfig) -> Self {
        Self {
            graphemes: UnicodeSegmentation::graphemes(s, true)
                .flat_map(|it| {
                    let contains_backslash = it.chars().count() == 2 && it.contains('\\');
                    let contains_combining_mark_or_unassigned_chars = it.chars().any(|c| {
                        let category = unicode_general_category::get_general_category(c);
                        matches!(
                            category,
                            // Mark categories
                            GC::NonspacingMark | GC::SpacingMark | GC::EnclosingMark |
                            // Other categories
                            GC::Control | GC::Format | GC::Surrogate | GC::PrivateUse | GC::Unassigned
                        )
                    });

                    if contains_backslash || contains_combining_mark_or_unassigned_chars {
                        it.chars()
                            .map(|c| {
                                Grapheme::from(
                                    &c.to_string(),
                                    config.is_capturing_group_enabled,
                                    config.is_output_colorized,
                                    config.is_verbose_mode_enabled,
                                )
                            })
                            .collect_vec()
                    } else {
                        vec![Grapheme::from(
                            it,
                            config.is_capturing_group_enabled,
                            config.is_output_colorized,
                            config.is_verbose_mode_enabled,
                        )]
                    }
                })
                .collect_vec(),
            config,
        }
    }

    pub(crate) fn from_graphemes(graphemes: Vec<Grapheme>, config: &'a RegExpConfig) -> Self {
        Self { graphemes, config }
    }

    pub(crate) fn new(grapheme: Grapheme, config: &'a RegExpConfig) -> Self {
        Self {
            graphemes: vec![grapheme],
            config,
        }
    }

    pub(crate) fn convert_to_char_classes(&mut self) {
        let is_digit_converted = self.config.is_digit_converted;
        let is_non_digit_converted = self.config.is_non_digit_converted;
        let is_space_converted = self.config.is_space_converted;
        let is_non_space_converted = self.config.is_non_space_converted;
        let is_word_converted = self.config.is_word_converted;
        let is_non_word_converted = self.config.is_non_word_converted;

        for grapheme in self.graphemes.iter_mut() {
            grapheme.chars = grapheme
                .chars
                .iter()
                .map(|it| {
                    it.chars()
                        .map(|c| {
                            if is_digit_converted && is_digit(c) {
                                "\\d".to_string()
                            } else if is_word_converted && is_word(c) {
                                "\\w".to_string()
                            } else if is_space_converted && is_space(c) {
                                "\\s".to_string()
                            } else if is_non_digit_converted && !is_digit(c) {
                                "\\D".to_string()
                            } else if is_non_word_converted && !is_word(c) {
                                "\\W".to_string()
                            } else if is_non_space_converted && !is_space(c) {
                                "\\S".to_string()
                            } else {
                                c.to_string()
                            }
                        })
                        .join("")
                })
                .collect_vec();
        }
    }

    pub(crate) fn convert_repetitions(&mut self) {
        let mut repetitions = vec![];
        convert_repetitions(self.graphemes(), repetitions.as_mut(), self.config);
        if !repetitions.is_empty() {
            self.graphemes = repetitions;
        }
    }

    pub(crate) fn merge(
        first: &GraphemeCluster,
        second: &GraphemeCluster,
        config: &'a RegExpConfig,
    ) -> Self {
        let mut graphemes = vec![];
        graphemes.extend_from_slice(&first.graphemes);
        graphemes.extend_from_slice(&second.graphemes);
        Self { graphemes, config }
    }

    pub(crate) fn graphemes(&self) -> &Vec<Grapheme> {
        &self.graphemes
    }

    pub(crate) fn graphemes_mut(&mut self) -> &mut Vec<Grapheme> {
        &mut self.graphemes
    }

    pub(crate) fn size(&self) -> usize {
        self.graphemes.len()
    }

    pub(crate) fn char_count(&self, is_non_ascii_char_escaped: bool) -> usize {
        self.graphemes
            .iter()
            .map(|it| it.char_count(is_non_ascii_char_escaped))
            .sum()
    }

    pub(crate) fn is_empty(&self) -> bool {
        self.graphemes.is_empty()
    }
}

fn is_digit(c: char) -> bool {
    static VALID_NUMERIC_CHARS: LazyLock<Vec<CharRange>> =
        LazyLock::new(|| convert_chars_to_range(DECIMAL_NUMBER));
    VALID_NUMERIC_CHARS.iter().any(|range| range.contains(c))
}

fn is_word(c: char) -> bool {
    static VALID_ALPHANUMERIC_CHARS: LazyLock<Vec<CharRange>> =
        LazyLock::new(|| convert_chars_to_range(WORD));
    VALID_ALPHANUMERIC_CHARS
        .iter()
        .any(|range| range.contains(c))
}

fn is_space(c: char) -> bool {
    static VALID_SPACE_CHARS: LazyLock<Vec<CharRange>> =
        LazyLock::new(|| convert_chars_to_range(WHITE_SPACE));
    VALID_SPACE_CHARS.iter().any(|range| range.contains(c))
}

fn convert_repetitions(
    graphemes: &[Grapheme],
    repetitions: &mut Vec<Grapheme>,
    config: &RegExpConfig,
) {
    let repeated_substrings = collect_repeated_substrings(graphemes);
    let ranges_of_repetitions = create_ranges_of_repetitions(repeated_substrings, config);
    let coalesced_repetitions = coalesce_repetitions(ranges_of_repetitions);
    replace_graphemes_with_repetitions(coalesced_repetitions, graphemes, repetitions, config)
}

fn collect_repeated_substrings(graphemes: &[Grapheme]) -> HashMap<Vec<String>, Vec<usize>> {
    let mut map = HashMap::new();

    for i in 0..graphemes.len() {
        let suffix = &graphemes[i..];
        for j in 1..=graphemes.len() / 2 {
            if suffix.len() >= j {
                let prefix = suffix[..j].iter().map(|it| it.value()).collect_vec();
                let indices = map.entry(prefix).or_insert_with(Vec::new);
                indices.push(i);
            }
        }
    }
    map
}

fn create_ranges_of_repetitions(
    repeated_substrings: HashMap<Vec<String>, Vec<usize>>,
    config: &RegExpConfig,
) -> Vec<(Range<usize>, Vec<String>)> {
    let mut repetitions = Vec::<(Range<usize>, Vec<String>)>::new();

    for (prefix_length, group) in &repeated_substrings
        .iter()
        .filter(|&(prefix, indices)| {
            indices
                .iter()
                .tuple_windows()
                .all(|(first, second)| (second - first) >= prefix.len())
        })
        .sorted_by_key(|&(prefix, _)| prefix.len())
        .rev()
        .chunk_by(|&(prefix, _)| prefix.len())
    {
        for (prefix, indices) in group.sorted_by_key(|&(_, indices)| indices[0]) {
            indices
                .iter()
                .map(|it| *it..it + prefix_length)
                .coalesce(|x, y| {
                    if x.end == y.start {
                        Ok(x.start..y.end)
                    } else {
                        Err((x, y))
                    }
                })
                .filter(|range| {
                    let count = ((range.end - range.start) / prefix_length) as u32;
                    count > config.minimum_repetitions
                })
                .for_each(|range| repetitions.push((range, prefix.clone())));
        }
    }
    repetitions
}

fn coalesce_repetitions(
    ranges_of_repetitions: Vec<(Range<usize>, Vec<String>)>,
) -> Vec<(Range<usize>, Vec<String>)> {
    ranges_of_repetitions
        .iter()
        .sorted_by(|&(first_range, _), &(second_range, _)| {
            match second_range.end.cmp(&first_range.end) {
                Ordering::Equal => first_range.start.cmp(&second_range.start),
                other => other,
            }
        })
        .coalesce(|first_tup, second_tup| {
            let first_range = &first_tup.0;
            let second_range = &second_tup.0;

            if (first_range.contains(&second_range.start)
                || first_range.contains(&second_range.end))
                && second_range.end != first_range.start
            {
                Ok(first_tup)
            } else {
                Err((first_tup, second_tup))
            }
        })
        .map(|(range, substr)| (range.clone(), substr.clone()))
        .collect_vec()
}

fn replace_graphemes_with_repetitions(
    coalesced_repetitions: Vec<(Range<usize>, Vec<String>)>,
    graphemes: &[Grapheme],
    repetitions: &mut Vec<Grapheme>,
    config: &RegExpConfig,
) {
    if coalesced_repetitions.is_empty() {
        return;
    }

    for grapheme in graphemes {
        repetitions.push(grapheme.clone());
    }

    for (range, substr) in coalesced_repetitions.iter() {
        if range.end > repetitions.len() {
            break;
        }

        let count = ((range.end - range.start) / substr.len()) as u32;

        if substr.len() < config.minimum_substring_length as usize {
            continue;
        }

        repetitions.splice(
            range.clone(),
            [Grapheme::new(
                substr.clone(),
                count,
                count,
                config.is_capturing_group_enabled,
                config.is_output_colorized,
                config.is_verbose_mode_enabled,
            )]
            .iter()
            .cloned(),
        );
    }

    for new_grapheme in repetitions.iter_mut() {
        convert_repetitions(
            &new_grapheme
                .chars
                .iter()
                .map(|it| {
                    Grapheme::from(
                        it,
                        config.is_capturing_group_enabled,
                        config.is_output_colorized,
                        config.is_verbose_mode_enabled,
                    )
                })
                .collect_vec(),
            new_grapheme.repetitions.as_mut(),
            config,
        );
    }
}

fn convert_chars_to_range(chars: &[(char, char)]) -> Vec<CharRange> {
    chars
        .iter()
        .map(|&(start, end)| CharRange::closed(start, end))
        .collect_vec()
}
```

## File: `src/component.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::quantifier::Quantifier;
use std::fmt::{Display, Formatter, Result};

pub(crate) enum Component {
    CapturedLeftParenthesis,
    CapturedParenthesizedExpression(String, bool, bool),
    Caret(bool),
    CharClass(String),
    DollarSign(bool),
    Hyphen,
    IgnoreCaseFlag,
    IgnoreCaseAndVerboseModeFlag,
    LeftBracket,
    Pipe,
    Quantifier(Quantifier, bool),
    Repetition(u32, bool),
    RepetitionRange(u32, u32, bool),
    RightBracket,
    RightParenthesis,
    UncapturedLeftParenthesis,
    UncapturedParenthesizedExpression(String, bool, bool),
    VerboseModeFlag,
}

impl Component {
    pub(crate) fn to_repr(&self, is_output_colorized: bool) -> String {
        match is_output_colorized {
            true => self.to_colored_string(false),
            false => self.to_string(),
        }
    }

    pub(crate) fn to_colored_string(&self, is_escaped: bool) -> String {
        match self {
            Component::CapturedLeftParenthesis => Self::green_bold(&self.to_string(), is_escaped),
            Component::CapturedParenthesizedExpression(
                expr,
                is_verbose_mode_enabled,
                has_final_line_break,
            ) => {
                if *is_verbose_mode_enabled {
                    if *has_final_line_break {
                        format!(
                            "\n{}\n{}\n{}\n",
                            Component::CapturedLeftParenthesis.to_colored_string(is_escaped),
                            expr,
                            Component::RightParenthesis.to_colored_string(is_escaped)
                        )
                    } else {
                        format!(
                            "\n{}\n{}\n{}",
                            Component::CapturedLeftParenthesis.to_colored_string(is_escaped),
                            expr,
                            Component::RightParenthesis.to_colored_string(is_escaped)
                        )
                    }
                } else {
                    format!(
                        "{}{}{}",
                        Component::CapturedLeftParenthesis.to_colored_string(is_escaped),
                        expr,
                        Component::RightParenthesis.to_colored_string(is_escaped)
                    )
                }
            }
            Component::Caret(is_verbose_mode_enabled) => {
                if *is_verbose_mode_enabled {
                    format!(
                        "{}\n",
                        Self::yellow_bold(&Component::Caret(false).to_string(), is_escaped)
                    )
                } else {
                    Self::yellow_bold(&self.to_string(), is_escaped)
                }
            }
            Component::CharClass(value) => Self::black_on_bright_yellow(value, is_escaped),
            Component::DollarSign(is_verbose_mode_enabled) => {
                if *is_verbose_mode_enabled {
                    format!(
                        "\n{}",
                        Self::yellow_bold(&Component::DollarSign(false).to_string(), is_escaped)
                    )
                } else {
                    Self::yellow_bold(&self.to_string(), is_escaped)
                }
            }
            Component::Hyphen => Self::cyan_bold(&self.to_string(), is_escaped),
            Component::IgnoreCaseFlag => {
                Self::bright_yellow_on_black(&self.to_string(), is_escaped)
            }
            Component::IgnoreCaseAndVerboseModeFlag => {
                format!("{}\n", Self::bright_yellow_on_black("(?ix)", is_escaped))
            }
            Component::LeftBracket => Self::cyan_bold(&self.to_string(), is_escaped),
            Component::Pipe => Self::red_bold(&self.to_string(), is_escaped),
            Component::Quantifier(quantifier, is_verbose_mode_enabled) => {
                if *is_verbose_mode_enabled {
                    format!(
                        "{}\n",
                        Self::purple_bold(&quantifier.to_string(), is_escaped)
                    )
                } else {
                    Self::purple_bold(&self.to_string(), is_escaped)
                }
            }
            Component::Repetition(num, is_verbose_mode_enabled) => {
                if *is_verbose_mode_enabled {
                    format!(
                        "{}\n",
                        Self::white_on_bright_blue(
                            &Component::Repetition(*num, false).to_string(),
                            is_escaped
                        )
                    )
                } else {
                    Self::white_on_bright_blue(&self.to_string(), is_escaped)
                }
            }
            Component::RepetitionRange(min, max, is_verbose_mode_enabled) => {
                if *is_verbose_mode_enabled {
                    format!(
                        "{}\n",
                        Self::white_on_bright_blue(
                            &Component::RepetitionRange(*min, *max, false).to_string(),
                            is_escaped
                        )
                    )
                } else {
                    Self::white_on_bright_blue(&self.to_string(), is_escaped)
                }
            }
            Component::RightBracket => Self::cyan_bold(&self.to_string(), is_escaped),
            Component::RightParenthesis => Self::green_bold(&self.to_string(), is_escaped),
            Component::UncapturedLeftParenthesis => Self::green_bold(&self.to_string(), is_escaped),
            Component::UncapturedParenthesizedExpression(
                expr,
                is_verbose_mode_enabled,
                has_final_line_break,
            ) => {
                if *is_verbose_mode_enabled {
                    if *has_final_line_break {
                        format!(
                            "\n{}\n{}\n{}\n",
                            Component::UncapturedLeftParenthesis.to_colored_string(is_escaped),
                            expr,
                            Component::RightParenthesis.to_colored_string(is_escaped)
                        )
                    } else {
                        format!(
                            "\n{}\n{}\n{}",
                            Component::UncapturedLeftParenthesis.to_colored_string(is_escaped),
                            expr,
                            Component::RightParenthesis.to_colored_string(is_escaped)
                        )
                    }
                } else {
                    format!(
                        "{}{}{}",
                        Component::UncapturedLeftParenthesis.to_colored_string(is_escaped),
                        expr,
                        Component::RightParenthesis.to_colored_string(is_escaped)
                    )
                }
            }
            Component::VerboseModeFlag => {
                format!("{}\n", Self::bright_yellow_on_black("(?x)", is_escaped))
            }
        }
    }

    fn black_on_bright_yellow(value: &str, is_escaped: bool) -> String {
        Self::color_code("103;30", value, is_escaped)
    }

    fn bright_yellow_on_black(value: &str, is_escaped: bool) -> String {
        Self::color_code("40;93", value, is_escaped)
    }

    fn cyan_bold(value: &str, is_escaped: bool) -> String {
        Self::color_code("1;36", value, is_escaped)
    }

    fn green_bold(value: &str, is_escaped: bool) -> String {
        Self::color_code("1;32", value, is_escaped)
    }

    fn purple_bold(value: &str, is_escaped: bool) -> String {
        Self::color_code("1;35", value, is_escaped)
    }

    fn red_bold(value: &str, is_escaped: bool) -> String {
        Self::color_code("1;31", value, is_escaped)
    }

    fn white_on_bright_blue(value: &str, is_escaped: bool) -> String {
        Self::color_code("104;37", value, is_escaped)
    }

    fn yellow_bold(value: &str, is_escaped: bool) -> String {
        Self::color_code("1;33", value, is_escaped)
    }

    fn color_code(code: &str, value: &str, is_escaped: bool) -> String {
        if is_escaped {
            format!("\u{1b}\\[{}m\\{}\u{1b}\\[0m", code, value)
        } else {
            format!("\u{1b}[{}m{}\u{1b}[0m", code, value)
        }
    }
}

impl Display for Component {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        write!(
            f,
            "{}",
            match self {
                Component::CapturedLeftParenthesis => "(".to_string(),
                Component::CapturedParenthesizedExpression(
                    expr,
                    is_verbose_mode_enabled,
                    has_final_line_break,
                ) =>
                    if *is_verbose_mode_enabled {
                        if *has_final_line_break {
                            format!(
                                "\n{}\n{}\n{}\n",
                                Component::CapturedLeftParenthesis,
                                expr,
                                Component::RightParenthesis
                            )
                        } else {
                            format!(
                                "\n{}\n{}\n{}",
                                Component::CapturedLeftParenthesis,
                                expr,
                                Component::RightParenthesis
                            )
                        }
                    } else {
                        format!(
                            "{}{}{}",
                            Component::CapturedLeftParenthesis,
                            expr,
                            Component::RightParenthesis
                        )
                    },
                Component::Caret(is_verbose_mode_enabled) =>
                    if *is_verbose_mode_enabled {
                        "^\n".to_string()
                    } else {
                        "^".to_string()
                    },
                Component::CharClass(value) => value.clone(),
                Component::DollarSign(is_verbose_mode_enabled) =>
                    if *is_verbose_mode_enabled {
                        "\n$".to_string()
                    } else {
                        "$".to_string()
                    },
                Component::Hyphen => "-".to_string(),
                Component::IgnoreCaseFlag => "(?i)".to_string(),
                Component::IgnoreCaseAndVerboseModeFlag => "(?ix)\n".to_string(),
                Component::LeftBracket => "[".to_string(),
                Component::Pipe => "|".to_string(),
                Component::Quantifier(quantifier, is_verbose_mode_enabled) =>
                    if *is_verbose_mode_enabled {
                        format!("{}\n", quantifier)
                    } else {
                        quantifier.to_string()
                    },
                Component::Repetition(num, is_verbose_mode_enabled) => {
                    if *num == 0 && *is_verbose_mode_enabled {
                        "{\\d+\\}\n".to_string()
                    } else if *num == 0 {
                        "{\\d+\\}".to_string()
                    } else if *is_verbose_mode_enabled {
                        format!("{{{}}}\n", num)
                    } else {
                        format!("{{{}}}", num)
                    }
                }
                Component::RepetitionRange(min, max, is_verbose_mode_enabled) => {
                    if *min == 0 && *max == 0 && *is_verbose_mode_enabled {
                        "{\\d+,\\d+\\}\n".to_string()
                    } else if *min == 0 && *max == 0 {
                        "{\\d+,\\d+\\}".to_string()
                    } else if *is_verbose_mode_enabled {
                        format!("{{{},{}}}\n", min, max)
                    } else {
                        format!("{{{},{}}}", min, max)
                    }
                }
                Component::RightBracket => "]".to_string(),
                Component::RightParenthesis => ")".to_string(),
                Component::UncapturedLeftParenthesis => "(?:".to_string(),
                Component::UncapturedParenthesizedExpression(
                    expr,
                    is_verbose_mode_enabled,
                    has_final_line_break,
                ) => {
                    if *is_verbose_mode_enabled {
                        if *has_final_line_break {
                            format!(
                                "\n{}\n{}\n{}\n",
                                Component::UncapturedLeftParenthesis,
                                expr,
                                Component::RightParenthesis
                            )
                        } else {
                            format!(
                                "\n{}\n{}\n{}",
                                Component::UncapturedLeftParenthesis,
                                expr,
                                Component::RightParenthesis
                            )
                        }
                    } else {
                        format!(
                            "{}{}{}",
                            Component::UncapturedLeftParenthesis,
                            expr,
                            Component::RightParenthesis
                        )
                    }
                }
                Component::VerboseModeFlag => "(?x)\n".to_string(),
            }
        )
    }
}
```

## File: `src/config.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#[derive(Clone, Debug, Hash, Ord, PartialOrd, Eq, PartialEq)]
pub(crate) struct RegExpConfig {
    pub(crate) minimum_repetitions: u32,
    pub(crate) minimum_substring_length: u32,
    pub(crate) is_digit_converted: bool,
    pub(crate) is_non_digit_converted: bool,
    pub(crate) is_space_converted: bool,
    pub(crate) is_non_space_converted: bool,
    pub(crate) is_word_converted: bool,
    pub(crate) is_non_word_converted: bool,
    pub(crate) is_repetition_converted: bool,
    pub(crate) is_case_insensitive_matching: bool,
    pub(crate) is_capturing_group_enabled: bool,
    pub(crate) is_non_ascii_char_escaped: bool,
    pub(crate) is_astral_code_point_converted_to_surrogate: bool,
    pub(crate) is_verbose_mode_enabled: bool,
    pub(crate) is_start_anchor_disabled: bool,
    pub(crate) is_end_anchor_disabled: bool,
    pub(crate) is_output_colorized: bool,
}

impl RegExpConfig {
    pub(crate) fn new() -> Self {
        Self {
            minimum_repetitions: 1,
            minimum_substring_length: 1,
            is_digit_converted: false,
            is_non_digit_converted: false,
            is_space_converted: false,
            is_non_space_converted: false,
            is_word_converted: false,
            is_non_word_converted: false,
            is_repetition_converted: false,
            is_case_insensitive_matching: false,
            is_capturing_group_enabled: false,
            is_non_ascii_char_escaped: false,
            is_astral_code_point_converted_to_surrogate: false,
            is_verbose_mode_enabled: false,
            is_start_anchor_disabled: false,
            is_end_anchor_disabled: false,
            is_output_colorized: false,
        }
    }

    pub(crate) fn is_char_class_feature_enabled(&self) -> bool {
        self.is_digit_converted
            || self.is_non_digit_converted
            || self.is_space_converted
            || self.is_non_space_converted
            || self.is_word_converted
            || self.is_non_word_converted
            || self.is_case_insensitive_matching
            || self.is_capturing_group_enabled
    }
}
```

## File: `src/dfa.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::cluster::GraphemeCluster;
use crate::config::RegExpConfig;
use crate::grapheme::Grapheme;
use itertools::Itertools;
use petgraph::graph::NodeIndex;
use petgraph::stable_graph::{Edges, StableGraph};
use petgraph::visit::Dfs;
use petgraph::{Directed, Direction};
use std::cmp::{max, min};
use std::collections::{BTreeSet, HashMap, HashSet};

type State = NodeIndex<u32>;
type StateLabel = String;
type EdgeLabel = Grapheme;

pub(crate) struct Dfa<'a> {
    alphabet: BTreeSet<Grapheme>,
    graph: StableGraph<StateLabel, EdgeLabel>,
    initial_state: State,
    final_state_indices: HashSet<usize>,
    config: &'a RegExpConfig,
}

impl<'a> Dfa<'a> {
    pub(crate) fn from(
        grapheme_clusters: &[GraphemeCluster],
        is_minimized: bool,
        config: &'a RegExpConfig,
    ) -> Self {
        let mut dfa = Self::new(config);
        for cluster in grapheme_clusters {
            dfa.insert(cluster);
        }
        if is_minimized {
            dfa.minimize();
        }
        dfa
    }

    pub(crate) fn state_count(&self) -> usize {
        self.graph.node_count()
    }

    pub(crate) fn states_in_depth_first_order(&self) -> Vec<State> {
        let mut depth_first_search = Dfs::new(&self.graph, self.initial_state);
        let mut states = vec![];
        while let Some(state) = depth_first_search.next(&self.graph) {
            states.push(state);
        }
        states
    }

    pub(crate) fn outgoing_edges(&self, state: State) -> Edges<'_, Grapheme, Directed> {
        self.graph.edges_directed(state, Direction::Outgoing)
    }

    pub(crate) fn is_final_state(&self, state: State) -> bool {
        self.final_state_indices.contains(&state.index())
    }

    fn new(config: &'a RegExpConfig) -> Self {
        let mut graph = StableGraph::new();
        let initial_state = graph.add_node("".to_string());
        Self {
            alphabet: BTreeSet::new(),
            graph,
            initial_state,
            final_state_indices: HashSet::new(),
            config,
        }
    }

    fn insert(&mut self, cluster: &GraphemeCluster) {
        let mut current_state = self.initial_state;

        for grapheme in cluster.graphemes() {
            self.alphabet.insert(grapheme.clone());
            current_state = self.return_next_state(current_state, grapheme);
        }
        self.final_state_indices.insert(current_state.index());
    }

    fn return_next_state(&mut self, current_state: State, edge_label: &Grapheme) -> State {
        match self.find_next_state(current_state, edge_label) {
            Some(next_state) => next_state,
            None => self.add_new_state(current_state, edge_label),
        }
    }

    fn find_next_state(&mut self, current_state: State, grapheme: &Grapheme) -> Option<State> {
        for next_state in self.graph.neighbors(current_state) {
            let edge_idx = self.graph.find_edge(current_state, next_state).unwrap();
            let current_grapheme = self.graph.edge_weight(edge_idx).unwrap();

            if current_grapheme.value() != grapheme.value() {
                continue;
            }

            if current_grapheme.maximum() == grapheme.maximum() - 1 {
                let min = min(current_grapheme.minimum(), grapheme.minimum());
                let max = max(current_grapheme.maximum(), grapheme.maximum());
                let new_grapheme = Grapheme::new(
                    grapheme.chars().clone(),
                    min,
                    max,
                    self.config.is_capturing_group_enabled,
                    self.config.is_output_colorized,
                    self.config.is_verbose_mode_enabled,
                );
                self.graph
                    .update_edge(current_state, next_state, new_grapheme);
                return Some(next_state);
            } else if current_grapheme.maximum() == grapheme.maximum() {
                return Some(next_state);
            }
        }
        None
    }

    fn add_new_state(&mut self, current_state: State, edge_label: &Grapheme) -> State {
        let next_state = self.graph.add_node("".to_string());
        self.graph
            .add_edge(current_state, next_state, edge_label.clone());
        next_state
    }

    #[allow(clippy::many_single_char_names)]
    fn minimize(&mut self) {
        let mut p = self.get_initial_partition();
        let mut w = p.iter().cloned().collect_vec();

        while !w.is_empty() {
            let a = w.drain(0..1).next().unwrap();

            for edge_label in self.alphabet.iter() {
                let x = self.get_parent_states(&a, edge_label);
                let mut replacements = vec![];
                let mut is_replacement_needed = true;
                let mut start_idx = 0;

                while is_replacement_needed {
                    for (idx, y) in p.iter().enumerate().skip(start_idx) {
                        if x.intersection(y).count() == 0 || y.difference(&x).count() == 0 {
                            is_replacement_needed = false;
                            continue;
                        }

                        let i = x.intersection(y).copied().collect::<HashSet<State>>();
                        let d = y.difference(&x).copied().collect::<HashSet<State>>();

                        is_replacement_needed = true;
                        start_idx = idx;

                        replacements.push((y.clone(), i, d));

                        break;
                    }

                    if is_replacement_needed {
                        let (_, i, d) = replacements.last().unwrap();

                        p.remove(start_idx);
                        p.insert(start_idx, i.clone());
                        p.insert(start_idx + 1, d.clone());
                    }
                }

                for (y, i, d) in replacements {
                    if w.contains(&y) {
                        let idx = w.iter().position(|it| it == &y).unwrap();
                        w.remove(idx);
                        w.push(i);
                        w.push(d);
                    } else if i.len() <= d.len() {
                        w.push(i);
                    } else {
                        w.push(d);
                    }
                }
            }
        }

        self.recreate_graph(p.iter().filter(|&it| !it.is_empty()).collect_vec());
    }

    fn get_initial_partition(&self) -> Vec<HashSet<State>> {
        let (final_states, non_final_states): (HashSet<State>, HashSet<State>) = self
            .graph
            .node_indices()
            .partition(|&state| !self.final_state_indices.contains(&state.index()));

        vec![final_states, non_final_states]
    }

    fn get_parent_states(&self, a: &HashSet<State>, label: &Grapheme) -> HashSet<State> {
        let mut x = HashSet::new();

        for &state in a {
            let direct_parent_states = self.graph.neighbors_directed(state, Direction::Incoming);
            for parent_state in direct_parent_states {
                let edge = self.graph.find_edge(parent_state, state).unwrap();
                let grapheme = self.graph.edge_weight(edge).unwrap();
                if grapheme.value() == label.value()
                    && (grapheme.maximum() == label.maximum()
                        || grapheme.minimum() == label.minimum())
                {
                    x.insert(parent_state);
                    break;
                }
            }
        }
        x
    }

    fn recreate_graph(&mut self, p: Vec<&HashSet<State>>) {
        let mut graph = StableGraph::<StateLabel, EdgeLabel>::new();
        let mut final_state_indices = HashSet::new();
        let mut state_mappings = HashMap::new();
        let mut new_initial_state: Option<NodeIndex> = None;

        for equivalence_class in p.iter() {
            let new_state = graph.add_node("".to_string());

            for old_state in equivalence_class.iter() {
                if self.initial_state == *old_state {
                    new_initial_state = Some(new_state);
                }
                state_mappings.insert(*old_state, new_state);
            }
        }

        for equivalence_class in p.iter() {
            let old_source_state = *equivalence_class.iter().next().unwrap();
            let new_source_state = state_mappings.get(&old_source_state).unwrap();

            for old_target_state in self.graph.neighbors(old_source_state) {
                let edge = self
                    .graph
                    .find_edge(old_source_state, old_target_state)
                    .unwrap();

                let grapheme = self.graph.edge_weight(edge).unwrap().clone();
                let new_target_state = state_mappings.get(&old_target_state).unwrap();

                graph.add_edge(*new_source_state, *new_target_state, grapheme.clone());

                if self.final_state_indices.contains(&old_target_state.index()) {
                    final_state_indices.insert(new_target_state.index());
                }
            }
        }
        self.initial_state = new_initial_state.unwrap();
        self.final_state_indices = final_state_indices;
        self.graph = graph;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_state_count() {
        let config = RegExpConfig::new();
        let mut dfa = Dfa::new(&config);
        assert_eq!(dfa.state_count(), 1);

        dfa.insert(&GraphemeCluster::from("abcd", &RegExpConfig::new()));
        assert_eq!(dfa.state_count(), 5);
    }

    #[test]
    fn test_is_final_state() {
        let config = RegExpConfig::new();
        let dfa = Dfa::from(
            &[GraphemeCluster::from("abcd", &RegExpConfig::new())],
            true,
            &config,
        );

        let intermediate_state = State::new(3);
        assert_eq!(dfa.is_final_state(intermediate_state), false);

        let final_state = State::new(4);
        assert_eq!(dfa.is_final_state(final_state), true);
    }

    #[test]
    fn test_outgoing_edges() {
        let config = RegExpConfig::new();
        let dfa = Dfa::from(
            &[
                GraphemeCluster::from("abcd", &RegExpConfig::new()),
                GraphemeCluster::from("abxd", &RegExpConfig::new()),
            ],
            true,
            &config,
        );
        let state = State::new(2);
        let mut edges = dfa.outgoing_edges(state);

        let first_edge = edges.next();
        assert!(first_edge.is_some());
        assert_eq!(
            first_edge.unwrap().weight(),
            &Grapheme::from("c", false, false, false)
        );

        let second_edge = edges.next();
        assert!(second_edge.is_some());
        assert_eq!(
            second_edge.unwrap().weight(),
            &Grapheme::from("x", false, false, false)
        );

        let third_edge = edges.next();
        assert!(third_edge.is_none());
    }

    #[test]
    fn test_states_in_depth_first_order() {
        let config = RegExpConfig::new();
        let dfa = Dfa::from(
            &[
                GraphemeCluster::from("abcd", &RegExpConfig::new()),
                GraphemeCluster::from("axyz", &RegExpConfig::new()),
            ],
            true,
            &config,
        );
        let states = dfa.states_in_depth_first_order();
        assert_eq!(states.len(), 7);

        let first_state = states.get(0).unwrap();
        let mut edges = dfa.outgoing_edges(*first_state);
        assert_eq!(
            edges.next().unwrap().weight(),
            &Grapheme::from("a", false, false, false)
        );
        assert!(edges.next().is_none());

        let second_state = states.get(1).unwrap();
        edges = dfa.outgoing_edges(*second_state);
        assert_eq!(
            edges.next().unwrap().weight(),
            &Grapheme::from("b", false, false, false)
        );
        assert_eq!(
            edges.next().unwrap().weight(),
            &Grapheme::from("x", false, false, false)
        );
        assert!(edges.next().is_none());

        let third_state = states.get(2).unwrap();
        edges = dfa.outgoing_edges(*third_state);
        assert_eq!(
            edges.next().unwrap().weight(),
            &Grapheme::from("y", false, false, false)
        );
        assert!(edges.next().is_none());

        let fourth_state = states.get(3).unwrap();
        edges = dfa.outgoing_edges(*fourth_state);
        assert_eq!(
            edges.next().unwrap().weight(),
            &Grapheme::from("z", false, false, false)
        );
        assert!(edges.next().is_none());

        let fifth_state = states.get(4).unwrap();
        edges = dfa.outgoing_edges(*fifth_state);
        assert!(edges.next().is_none());

        let sixth_state = states.get(5).unwrap();
        edges = dfa.outgoing_edges(*sixth_state);
        assert_eq!(
            edges.next().unwrap().weight(),
            &Grapheme::from("c", false, false, false)
        );
        assert!(edges.next().is_none());

        let seventh_state = states.get(6).unwrap();
        edges = dfa.outgoing_edges(*seventh_state);
        assert_eq!(
            edges.next().unwrap().weight(),
            &Grapheme::from("d", false, false, false)
        );
        assert!(edges.next().is_none());
    }

    #[test]
    fn test_minimization_algorithm() {
        let config = RegExpConfig::new();
        let mut dfa = Dfa::new(&config);
        assert_eq!(dfa.graph.node_count(), 1);
        assert_eq!(dfa.graph.edge_count(), 0);

        dfa.insert(&GraphemeCluster::from("abcd", &RegExpConfig::new()));
        assert_eq!(dfa.graph.node_count(), 5);
        assert_eq!(dfa.graph.edge_count(), 4);

        dfa.insert(&GraphemeCluster::from("abxd", &RegExpConfig::new()));
        assert_eq!(dfa.graph.node_count(), 7);
        assert_eq!(dfa.graph.edge_count(), 6);

        dfa.minimize();
        assert_eq!(dfa.graph.node_count(), 5);
        assert_eq!(dfa.graph.edge_count(), 5);
    }

    #[test]
    fn test_dfa_constructor() {
        let config = RegExpConfig::new();
        let dfa = Dfa::from(
            &[
                GraphemeCluster::from("abcd", &RegExpConfig::new()),
                GraphemeCluster::from("abxd", &RegExpConfig::new()),
            ],
            true,
            &config,
        );
        assert_eq!(dfa.graph.node_count(), 5);
        assert_eq!(dfa.graph.edge_count(), 5);
    }
}
```

## File: `src/expression.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::cluster::GraphemeCluster;
use crate::config::RegExpConfig;
use crate::dfa::Dfa;
use crate::grapheme::Grapheme;
use crate::quantifier::Quantifier;
use crate::substring::Substring;
use itertools::EitherOrBoth::Both;
use itertools::Itertools;
use ndarray::{Array1, Array2};
use petgraph::prelude::EdgeRef;
use std::cmp::Reverse;
use std::collections::BTreeSet;

#[derive(Clone, Debug, Eq, PartialEq)]
pub(crate) enum Expression<'a> {
    Alternation(Vec<Expression<'a>>, bool, bool, bool),
    CharacterClass(BTreeSet<char>, bool),
    Concatenation(Box<Expression<'a>>, Box<Expression<'a>>, bool, bool, bool),
    Literal(GraphemeCluster<'a>, bool, bool),
    Repetition(Box<Expression<'a>>, Quantifier, bool, bool, bool),
}

impl<'a> Expression<'a> {
    pub(crate) fn from(dfa: Dfa, config: &'a RegExpConfig) -> Self {
        let states = dfa.states_in_depth_first_order();
        let state_count = dfa.state_count();

        let mut a = Array2::<Option<Expression>>::default((state_count, state_count));
        let mut b = Array1::<Option<Expression>>::default(state_count);

        for (i, state) in states.iter().enumerate() {
            if dfa.is_final_state(*state) {
                b[i] = Some(Expression::new_literal(
                    GraphemeCluster::from("", config),
                    config,
                ));
            }

            for edge in dfa.outgoing_edges(*state) {
                let literal = Expression::new_literal(
                    GraphemeCluster::new(edge.weight().clone(), config),
                    config,
                );
                let j = states.iter().position(|&it| it == edge.target()).unwrap();

                a[(i, j)] = if a[(i, j)].is_some() {
                    Self::union(&a[(i, j)], &Some(literal), config)
                } else {
                    Some(literal)
                }
            }
        }

        for n in (0..state_count).rev() {
            if a[(n, n)].is_some() {
                b[n] = Self::concatenate(
                    &Self::repeat_zero_or_more_times(&a[(n, n)], config),
                    &b[n],
                    config,
                );
                for j in 0..n {
                    a[(n, j)] = Self::concatenate(
                        &Self::repeat_zero_or_more_times(&a[(n, n)], config),
                        &a[(n, j)],
                        config,
                    );
                }
            }

            for i in 0..n {
                if a[(i, n)].is_some() {
                    b[i] =
                        Self::union(&b[i], &Self::concatenate(&a[(i, n)], &b[n], config), config);
                    for j in 0..n {
                        a[(i, j)] = Self::union(
                            &a[(i, j)],
                            &Self::concatenate(&a[(i, n)], &a[(n, j)], config),
                            config,
                        );
                    }
                }
            }
        }

        if !b.is_empty() && b[0].is_some() {
            b[0].as_ref().unwrap().clone()
        } else {
            Expression::new_literal(GraphemeCluster::from("", config), config)
        }
    }

    pub(crate) fn new_alternation(exprs: Vec<Expression<'a>>, config: &RegExpConfig) -> Self {
        let mut options: Vec<Expression> = vec![];
        Self::flatten_alternations(&mut options, exprs);
        options.sort_by_key(|option| Reverse(option.len()));
        Expression::Alternation(
            options,
            config.is_capturing_group_enabled,
            config.is_output_colorized,
            config.is_verbose_mode_enabled,
        )
    }

    fn new_character_class(
        first_char_set: BTreeSet<char>,
        second_char_set: BTreeSet<char>,
        config: &RegExpConfig,
    ) -> Self {
        let union_set = first_char_set.union(&second_char_set).copied().collect();
        Expression::CharacterClass(union_set, config.is_output_colorized)
    }

    fn new_concatenation(
        expr1: Expression<'a>,
        expr2: Expression<'a>,
        config: &RegExpConfig,
    ) -> Self {
        Expression::Concatenation(
            Box::from(expr1),
            Box::from(expr2),
            config.is_capturing_group_enabled,
            config.is_output_colorized,
            config.is_verbose_mode_enabled,
        )
    }

    pub(crate) fn new_literal(cluster: GraphemeCluster<'a>, config: &RegExpConfig) -> Self {
        Expression::Literal(
            cluster,
            config.is_non_ascii_char_escaped,
            config.is_astral_code_point_converted_to_surrogate,
        )
    }

    fn new_repetition(expr: Expression<'a>, quantifier: Quantifier, config: &RegExpConfig) -> Self {
        Expression::Repetition(
            Box::from(expr),
            quantifier,
            config.is_capturing_group_enabled,
            config.is_output_colorized,
            config.is_verbose_mode_enabled,
        )
    }

    fn is_empty(&self) -> bool {
        match self {
            Expression::Literal(cluster, _, _) => cluster.is_empty(),
            _ => false,
        }
    }

    pub(crate) fn is_single_codepoint(&self) -> bool {
        match self {
            Expression::CharacterClass(_, _) => true,
            Expression::Literal(cluster, is_non_ascii_char_escaped, _) => {
                cluster.char_count(*is_non_ascii_char_escaped) == 1
                    && cluster.graphemes().first().unwrap().maximum() == 1
            }
            _ => false,
        }
    }

    fn len(&self) -> usize {
        match self {
            Expression::Alternation(options, _, _, _) => options.first().unwrap().len(),
            Expression::CharacterClass(_, _) => 1,
            Expression::Concatenation(expr1, expr2, _, _, _) => expr1.len() + expr2.len(),
            Expression::Literal(cluster, _, _) => cluster.size(),
            Expression::Repetition(expr, _, _, _, _) => expr.len(),
        }
    }

    pub(crate) fn precedence(&self) -> u8 {
        match self {
            Expression::Alternation(_, _, _, _) | Expression::CharacterClass(_, _) => 1,
            Expression::Concatenation(_, _, _, _, _) | Expression::Literal(_, _, _) => 2,
            Expression::Repetition(_, _, _, _, _) => 3,
        }
    }

    pub(crate) fn remove_substring(&mut self, substring: &Substring, length: usize) {
        match self {
            Expression::Concatenation(expr1, expr2, _, _, _) => match substring {
                Substring::Prefix => {
                    if let Expression::Literal(_, _, _) = **expr1 {
                        expr1.remove_substring(substring, length)
                    }
                }
                Substring::Suffix => {
                    if let Expression::Literal(_, _, _) = **expr2 {
                        expr2.remove_substring(substring, length)
                    }
                }
            },
            Expression::Literal(cluster, _, _) => match substring {
                Substring::Prefix => {
                    cluster.graphemes_mut().drain(..length);
                }
                Substring::Suffix => {
                    let graphemes = cluster.graphemes_mut();
                    graphemes.drain(graphemes.len() - length..);
                }
            },
            _ => (),
        }
    }

    pub(crate) fn value(&self, substring: Option<&Substring>) -> Option<Vec<Grapheme>> {
        match self {
            Expression::Concatenation(expr1, expr2, _, _, _) => match substring {
                Some(value) => match value {
                    Substring::Prefix => expr1.value(None),
                    Substring::Suffix => expr2.value(None),
                },
                None => None,
            },
            Expression::Literal(cluster, _, _) => Some(cluster.graphemes().clone()),
            _ => None,
        }
    }

    fn repeat_zero_or_more_times(
        expr: &Option<Expression<'a>>,
        config: &'a RegExpConfig,
    ) -> Option<Expression<'a>> {
        expr.as_ref()
            .map(|value| Expression::new_repetition(value.clone(), Quantifier::KleeneStar, config))
    }

    fn concatenate(
        a: &Option<Expression<'a>>,
        b: &Option<Expression<'a>>,
        config: &'a RegExpConfig,
    ) -> Option<Expression<'a>> {
        if a.is_none() || b.is_none() {
            return None;
        }

        let expr1 = a.as_ref().unwrap();
        let expr2 = b.as_ref().unwrap();

        if expr1.is_empty() {
            return b.clone();
        }
        if expr2.is_empty() {
            return a.clone();
        }

        if let (Expression::Literal(graphemes_a, _, _), Expression::Literal(graphemes_b, _, _)) =
            (&expr1, &expr2)
        {
            return Some(Expression::new_literal(
                GraphemeCluster::merge(graphemes_a, graphemes_b, config),
                config,
            ));
        }

        if let (
            Expression::Literal(graphemes_a, _, _),
            Expression::Concatenation(first, second, _, _, _),
        ) = (&expr1, &expr2)
        {
            if let Expression::Literal(graphemes_first, _, _) = &**first {
                let literal = Expression::new_literal(
                    GraphemeCluster::merge(graphemes_a, graphemes_first, config),
                    config,
                );
                return Some(Expression::new_concatenation(
                    literal,
                    *second.clone(),
                    config,
                ));
            }
        }

        if let (
            Expression::Literal(graphemes_b, _, _),
            Expression::Concatenation(first, second, _, _, _),
        ) = (&expr2, &expr1)
        {
            if let Expression::Literal(graphemes_second, _, _) = &**second {
                let literal = Expression::new_literal(
                    GraphemeCluster::merge(graphemes_second, graphemes_b, config),
                    config,
                );
                return Some(Expression::new_concatenation(
                    *first.clone(),
                    literal,
                    config,
                ));
            }
        }

        Some(Expression::new_concatenation(
            expr1.clone(),
            expr2.clone(),
            config,
        ))
    }

    fn union(
        a: &Option<Expression<'a>>,
        b: &Option<Expression<'a>>,
        config: &'a RegExpConfig,
    ) -> Option<Expression<'a>> {
        if let (Some(mut expr1), Some(mut expr2)) = (a.clone(), b.clone()) {
            if expr1 != expr2 {
                let common_prefix =
                    Self::remove_common_substring(&mut expr1, &mut expr2, Substring::Prefix);
                let common_suffix =
                    Self::remove_common_substring(&mut expr1, &mut expr2, Substring::Suffix);

                let mut result = if expr1.is_empty() {
                    Some(Expression::new_repetition(
                        expr2.clone(),
                        Quantifier::QuestionMark,
                        config,
                    ))
                } else if expr2.is_empty() {
                    Some(Expression::new_repetition(
                        expr1.clone(),
                        Quantifier::QuestionMark,
                        config,
                    ))
                } else {
                    None
                };

                if result.is_none() {
                    if let Expression::Repetition(expr, quantifier, _, _, _) = &expr1 {
                        if quantifier == &Quantifier::QuestionMark {
                            let alternation = Expression::new_alternation(
                                vec![*expr.clone(), expr2.clone()],
                                config,
                            );
                            result = Some(Expression::new_repetition(
                                alternation,
                                Quantifier::QuestionMark,
                                config,
                            ));
                        }
                    }
                }

                if result.is_none() {
                    if let Expression::Repetition(expr, quantifier, _, _, _) = &expr2 {
                        if quantifier == &Quantifier::QuestionMark {
                            let alternation = Expression::new_alternation(
                                vec![expr1.clone(), *expr.clone()],
                                config,
                            );
                            result = Some(Expression::new_repetition(
                                alternation,
                                Quantifier::QuestionMark,
                                config,
                            ));
                        }
                    }
                }

                if result.is_none() && expr1.is_single_codepoint() && expr2.is_single_codepoint() {
                    let first_char_set = Self::extract_character_set(expr1.clone());
                    let second_char_set = Self::extract_character_set(expr2.clone());
                    result = Some(Expression::new_character_class(
                        first_char_set,
                        second_char_set,
                        config,
                    ));
                }

                if result.is_none() {
                    result = Some(Expression::new_alternation(vec![expr1, expr2], config));
                }

                if let Some(prefix) = common_prefix {
                    result = Some(Expression::new_concatenation(
                        Expression::new_literal(
                            GraphemeCluster::from_graphemes(prefix, config),
                            config,
                        ),
                        result.unwrap(),
                        config,
                    ));
                }

                if let Some(suffix) = common_suffix {
                    result = Some(Expression::new_concatenation(
                        result.unwrap(),
                        Expression::new_literal(
                            GraphemeCluster::from_graphemes(suffix, config),
                            config,
                        ),
                        config,
                    ));
                }

                result
            } else if a.is_some() {
                a.clone()
            } else if b.is_some() {
                b.clone()
            } else {
                None
            }
        } else if a.is_some() {
            a.clone()
        } else if b.is_some() {
            b.clone()
        } else {
            None
        }
    }

    fn flatten_alternations(
        flattened_options: &mut Vec<Expression<'a>>,
        current_options: Vec<Expression<'a>>,
    ) {
        for option in current_options {
            if let Expression::Alternation(expr_options, _, _, _) = option {
                Self::flatten_alternations(flattened_options, expr_options);
            } else {
                flattened_options.push(option);
            }
        }
    }

    fn extract_character_set(expr: Expression) -> BTreeSet<char> {
        match expr {
            Expression::Literal(cluster, _, _) => {
                let single_char = cluster
                    .graphemes()
                    .first()
                    .unwrap()
                    .value()
                    .chars()
                    .next()
                    .unwrap();
                btreeset![single_char]
            }
            Expression::CharacterClass(char_set, _) => char_set,
            _ => BTreeSet::new(),
        }
    }

    fn remove_common_substring(
        a: &mut Expression,
        b: &mut Expression,
        substring: Substring,
    ) -> Option<Vec<Grapheme>> {
        let common_substring = Self::find_common_substring(a, b, &substring);
        if let Some(value) = &common_substring {
            a.remove_substring(&substring, value.len());
            b.remove_substring(&substring, value.len());
        }
        common_substring
    }

    fn find_common_substring(
        a: &Expression,
        b: &Expression,
        substring: &Substring,
    ) -> Option<Vec<Grapheme>> {
        let mut graphemes_a = a.value(Some(substring)).unwrap_or_default();
        let mut graphemes_b = b.value(Some(substring)).unwrap_or_default();
        let mut common_graphemes = vec![];

        if let Substring::Suffix = substring {
            graphemes_a.reverse();
            graphemes_b.reverse();
        }

        for pair in graphemes_a.iter().zip_longest(graphemes_b.iter()) {
            match pair {
                Both(grapheme_a, grapheme_b) => {
                    if grapheme_a == grapheme_b {
                        common_graphemes.push(grapheme_a.clone());
                    } else {
                        break;
                    }
                }
                _ => break,
            }
        }

        if let Substring::Suffix = substring {
            common_graphemes.reverse();
        }

        if common_graphemes.is_empty() {
            None
        } else {
            Some(common_graphemes)
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn ensure_correct_string_representation_of_alternation_1() {
        let config = RegExpConfig::new();
        let literal1 = Expression::new_literal(GraphemeCluster::from("abc", &config), &config);
        let literal2 = Expression::new_literal(GraphemeCluster::from("def", &config), &config);
        let alternation = Expression::new_alternation(vec![literal1, literal2], &config);
        assert_eq!(alternation.to_string(), "abc|def");
    }

    #[test]
    fn ensure_correct_string_representation_of_alternation_2() {
        let config = RegExpConfig::new();
        let literal1 = Expression::new_literal(GraphemeCluster::from("a", &config), &config);
        let literal2 = Expression::new_literal(GraphemeCluster::from("ab", &config), &config);
        let literal3 = Expression::new_literal(GraphemeCluster::from("abc", &config), &config);
        let alternation = Expression::new_alternation(vec![literal1, literal2, literal3], &config);
        assert_eq!(alternation.to_string(), "abc|ab|a");
    }

    #[test]
    fn ensure_correct_string_representation_of_character_class_1() {
        let config = RegExpConfig::new();
        let char_class = Expression::new_character_class(btreeset!['a'], btreeset!['b'], &config);
        assert_eq!(char_class.to_string(), "[ab]");
    }

    #[test]
    fn ensure_correct_string_representation_of_character_class_2() {
        let config = RegExpConfig::new();
        let char_class =
            Expression::new_character_class(btreeset!['a', 'b'], btreeset!['c'], &config);
        assert_eq!(char_class.to_string(), "[a-c]");
    }

    #[test]
    fn ensure_correct_string_representation_of_concatenation_1() {
        let config = RegExpConfig::new();
        let literal1 = Expression::new_literal(GraphemeCluster::from("abc", &config), &config);
        let literal2 = Expression::new_literal(GraphemeCluster::from("def", &config), &config);
        let concatenation = Expression::new_concatenation(literal1, literal2, &config);
        assert_eq!(concatenation.to_string(), "abcdef");
    }

    #[test]
    fn ensure_correct_string_representation_of_concatenation_2() {
        let config = RegExpConfig::new();
        let literal1 = Expression::new_literal(GraphemeCluster::from("abc", &config), &config);
        let literal2 = Expression::new_literal(GraphemeCluster::from("def", &config), &config);
        let repetition = Expression::new_repetition(literal1, Quantifier::KleeneStar, &config);
        let concatenation = Expression::new_concatenation(repetition, literal2, &config);
        assert_eq!(concatenation.to_string(), "(?:abc)*def");
    }

    #[test]
    fn ensure_correct_removal_of_prefix_in_literal() {
        let config = RegExpConfig::new();
        let mut literal =
            Expression::new_literal(GraphemeCluster::from("abcdef", &config), &config);
        assert_eq!(
            literal.value(None),
            Some(
                vec!["a", "b", "c", "d", "e", "f"]
                    .iter()
                    .map(|&it| Grapheme::from(
                        it,
                        config.is_capturing_group_enabled,
                        config.is_output_colorized,
                        config.is_verbose_mode_enabled
                    ))
                    .collect_vec()
            )
        );

        literal.remove_substring(&Substring::Prefix, 2);
        assert_eq!(
            literal.value(None),
            Some(
                vec!["c", "d", "e", "f"]
                    .iter()
                    .map(|&it| Grapheme::from(
                        it,
                        config.is_capturing_group_enabled,
                        config.is_output_colorized,
                        config.is_verbose_mode_enabled
                    ))
                    .collect_vec()
            )
        );
    }

    #[test]
    fn ensure_correct_removal_of_suffix_in_literal() {
        let config = RegExpConfig::new();
        let mut literal =
            Expression::new_literal(GraphemeCluster::from("abcdef", &config), &config);
        assert_eq!(
            literal.value(None),
            Some(
                vec!["a", "b", "c", "d", "e", "f"]
                    .iter()
                    .map(|&it| Grapheme::from(
                        it,
                        config.is_capturing_group_enabled,
                        config.is_output_colorized,
                        config.is_verbose_mode_enabled
                    ))
                    .collect_vec()
            )
        );

        literal.remove_substring(&Substring::Suffix, 2);
        assert_eq!(
            literal.value(None),
            Some(
                vec!["a", "b", "c", "d"]
                    .iter()
                    .map(|&it| Grapheme::from(
                        it,
                        config.is_capturing_group_enabled,
                        config.is_output_colorized,
                        config.is_verbose_mode_enabled
                    ))
                    .collect_vec()
            )
        );
    }

    #[test]
    fn ensure_correct_string_representation_of_repetition_1() {
        let config = RegExpConfig::new();
        let literal = Expression::new_literal(GraphemeCluster::from("abc", &config), &config);
        let repetition = Expression::new_repetition(literal, Quantifier::KleeneStar, &config);
        assert_eq!(repetition.to_string(), "(?:abc)*");
    }

    #[test]
    fn ensure_correct_string_representation_of_repetition_2() {
        let config = RegExpConfig::new();
        let literal = Expression::new_literal(GraphemeCluster::from("a", &config), &config);
        let repetition = Expression::new_repetition(literal, Quantifier::QuestionMark, &config);
        assert_eq!(repetition.to_string(), "a?");
    }
}
```

## File: `src/format.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::char_range::CharRange;
use crate::cluster::GraphemeCluster;
use crate::component::Component;
use crate::expression::Expression;
use crate::quantifier::Quantifier;
use itertools::Itertools;
use std::collections::BTreeSet;
use std::fmt::{Display, Formatter, Result};

impl Display for Expression<'_> {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        match self {
            Expression::Alternation(
                options,
                is_capturing_group_enabled,
                is_output_colorized,
                is_verbose_mode_enabled,
            ) => format_alternation(
                f,
                self,
                options,
                *is_capturing_group_enabled,
                *is_output_colorized,
                *is_verbose_mode_enabled,
            ),
            Expression::CharacterClass(char_set, is_output_colorized) => {
                format_character_class(f, char_set, *is_output_colorized)
            }
            Expression::Concatenation(
                expr1,
                expr2,
                is_capturing_group_enabled,
                is_output_colorized,
                is_verbose_mode_enabled,
            ) => format_concatenation(
                f,
                self,
                expr1,
                expr2,
                *is_capturing_group_enabled,
                *is_output_colorized,
                *is_verbose_mode_enabled,
            ),
            Expression::Literal(
                cluster,
                is_non_ascii_char_escaped,
                is_astral_code_point_converted_to_surrogate,
            ) => format_literal(
                f,
                cluster,
                *is_non_ascii_char_escaped,
                *is_astral_code_point_converted_to_surrogate,
            ),
            Expression::Repetition(
                expr,
                quantifier,
                is_capturing_group_enabled,
                is_output_colorized,
                is_verbose_mode_enabled,
            ) => format_repetition(
                f,
                self,
                expr,
                quantifier,
                *is_capturing_group_enabled,
                *is_output_colorized,
                *is_verbose_mode_enabled,
            ),
        }
    }
}

fn get_codepoint_position(c: char) -> usize {
    CharRange::all().position(|it| it == c).unwrap()
}

fn format_alternation(
    f: &mut Formatter<'_>,
    expr: &Expression,
    options: &[Expression],
    is_capturing_group_enabled: bool,
    is_output_colorized: bool,
    is_verbose_mode_enabled: bool,
) -> Result {
    let pipe_component = Component::Pipe.to_repr(is_output_colorized);
    let disjunction_operator = if is_verbose_mode_enabled {
        format!("\n{}\n", pipe_component)
    } else {
        pipe_component
    };
    let alternation_str = options
        .iter()
        .map(|option| {
            if option.precedence() < expr.precedence() && !option.is_single_codepoint() {
                if is_capturing_group_enabled {
                    Component::CapturedParenthesizedExpression(
                        option.to_string(),
                        is_verbose_mode_enabled,
                        true,
                    )
                    .to_repr(is_output_colorized)
                } else {
                    Component::UncapturedParenthesizedExpression(
                        option.to_string(),
                        is_verbose_mode_enabled,
                        true,
                    )
                    .to_repr(is_output_colorized)
                }
            } else {
                format!("{}", option)
            }
        })
        .join(&disjunction_operator);

    write!(f, "{}", alternation_str)
}

fn format_character_class(
    f: &mut Formatter<'_>,
    char_set: &BTreeSet<char>,
    is_output_colorized: bool,
) -> Result {
    let chars_to_escape = ['[', ']', '\\', '-', '^', '$'];
    let escaped_char_set = char_set
        .iter()
        .map(|c| {
            if chars_to_escape.contains(c) {
                format!("{}{}", "\\", c)
            } else if c == &'\n' {
                "\\n".to_string()
            } else if c == &'\r' {
                "\\r".to_string()
            } else if c == &'\t' {
                "\\t".to_string()
            } else {
                c.to_string()
            }
        })
        .collect_vec();
    let char_positions = char_set
        .iter()
        .map(|&it| get_codepoint_position(it))
        .collect_vec();

    let mut subsets = vec![];
    let mut subset = vec![];

    for ((first_c, first_pos), (second_c, second_pos)) in
        escaped_char_set.iter().zip(char_positions).tuple_windows()
    {
        if subset.is_empty() {
            subset.push(first_c);
        }
        if second_pos == first_pos + 1 {
            subset.push(second_c);
        } else {
            subsets.push(subset);
            subset = vec![second_c];
        }
    }

    subsets.push(subset);

    let mut char_class_strs = vec![];

    for subset in subsets.iter() {
        if subset.len() <= 2 {
            for c in subset.iter() {
                char_class_strs.push((*c).to_string());
            }
        } else {
            char_class_strs.push(format!(
                "{}{}{}",
                subset.first().unwrap(),
                Component::Hyphen.to_repr(is_output_colorized),
                subset.last().unwrap()
            ));
        }
    }

    write!(
        f,
        "{}{}{}",
        Component::LeftBracket.to_repr(is_output_colorized),
        char_class_strs.join(""),
        Component::RightBracket.to_repr(is_output_colorized)
    )
}

fn format_concatenation(
    f: &mut Formatter<'_>,
    expr: &Expression,
    expr1: &Expression,
    expr2: &Expression,
    is_capturing_group_enabled: bool,
    is_output_colorized: bool,
    is_verbose_mode_enabled: bool,
) -> Result {
    let expr_strs = [expr1, expr2]
        .iter()
        .map(|&it| {
            if it.precedence() < expr.precedence() && !it.is_single_codepoint() {
                if is_capturing_group_enabled {
                    Component::CapturedParenthesizedExpression(
                        it.to_string(),
                        is_verbose_mode_enabled,
                        true,
                    )
                    .to_repr(is_output_colorized)
                } else {
                    Component::UncapturedParenthesizedExpression(
                        it.to_string(),
                        is_verbose_mode_enabled,
                        true,
                    )
                    .to_repr(is_output_colorized)
                }
            } else {
                format!("{}", it)
            }
        })
        .collect_vec();

    write!(
        f,
        "{}{}",
        expr_strs.first().unwrap(),
        expr_strs.last().unwrap()
    )
}

fn format_literal(
    f: &mut Formatter<'_>,
    cluster: &GraphemeCluster,
    is_non_ascii_char_escaped: bool,
    is_astral_code_point_converted_to_surrogate: bool,
) -> Result {
    let literal_str = cluster
        .graphemes()
        .iter()
        .cloned()
        .map(|mut grapheme| {
            if grapheme.has_repetitions() {
                grapheme
                    .repetitions_mut()
                    .iter_mut()
                    .for_each(|repeated_grapheme| {
                        repeated_grapheme.escape_regexp_symbols(
                            is_non_ascii_char_escaped,
                            is_astral_code_point_converted_to_surrogate,
                        );
                    });
            } else {
                grapheme.escape_regexp_symbols(
                    is_non_ascii_char_escaped,
                    is_astral_code_point_converted_to_surrogate,
                );
            }
            grapheme.to_string()
        })
        .join("");

    write!(f, "{}", literal_str)
}

fn format_repetition(
    f: &mut Formatter<'_>,
    expr: &Expression,
    expr1: &Expression,
    quantifier: &Quantifier,
    is_capturing_group_enabled: bool,
    is_output_colorized: bool,
    is_verbose_mode_enabled: bool,
) -> Result {
    if expr1.precedence() < expr.precedence() && !expr1.is_single_codepoint() {
        if is_capturing_group_enabled {
            write!(
                f,
                "{}{}",
                Component::CapturedParenthesizedExpression(
                    expr1.to_string(),
                    is_verbose_mode_enabled,
                    false
                )
                .to_repr(is_output_colorized),
                Component::Quantifier(quantifier.clone(), is_verbose_mode_enabled)
                    .to_repr(is_output_colorized)
            )
        } else {
            write!(
                f,
                "{}{}",
                Component::UncapturedParenthesizedExpression(
                    expr1.to_string(),
                    is_verbose_mode_enabled,
                    false
                )
                .to_repr(is_output_colorized),
                Component::Quantifier(quantifier.clone(), is_verbose_mode_enabled)
                    .to_repr(is_output_colorized)
            )
        }
    } else {
        write!(
            f,
            "{}{}",
            expr1,
            Component::Quantifier(quantifier.clone(), is_verbose_mode_enabled)
                .to_repr(is_output_colorized)
        )
    }
}
```

## File: `src/grapheme.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::component::Component;
use itertools::Itertools;
use std::fmt::{Display, Formatter, Result};

const CHARS_TO_ESCAPE: [&str; 14] = [
    "(", ")", "[", "]", "{", "}", "+", "*", "-", ".", "?", "|", "^", "$",
];

const CHAR_CLASSES: [&str; 6] = ["\\d", "\\s", "\\w", "\\D", "\\S", "\\W"];

#[derive(Clone, Debug, Hash, Ord, PartialOrd, Eq, PartialEq)]
pub(crate) struct Grapheme {
    pub(crate) chars: Vec<String>,
    pub(crate) repetitions: Vec<Grapheme>,
    min: u32,
    max: u32,
    is_capturing_group_enabled: bool,
    is_output_colorized: bool,
    is_verbose_mode_enabled: bool,
}

impl Grapheme {
    pub(crate) fn from(
        s: &str,
        is_capturing_group_enabled: bool,
        is_output_colorized: bool,
        is_verbose_mode_enabled: bool,
    ) -> Self {
        Self {
            chars: vec![s.to_string()],
            repetitions: vec![],
            min: 1,
            max: 1,
            is_capturing_group_enabled,
            is_output_colorized,
            is_verbose_mode_enabled,
        }
    }

    pub(crate) fn new(
        chars: Vec<String>,
        min: u32,
        max: u32,
        is_capturing_group_enabled: bool,
        is_output_colorized: bool,
        is_verbose_mode_enabled: bool,
    ) -> Self {
        Self {
            chars,
            repetitions: vec![],
            min,
            max,
            is_capturing_group_enabled,
            is_output_colorized,
            is_verbose_mode_enabled,
        }
    }

    pub(crate) fn value(&self) -> String {
        self.chars.join("")
    }

    pub(crate) fn chars(&self) -> &Vec<String> {
        &self.chars
    }

    pub(crate) fn chars_mut(&mut self) -> &mut Vec<String> {
        &mut self.chars
    }

    pub(crate) fn has_repetitions(&self) -> bool {
        !self.repetitions.is_empty()
    }

    pub(crate) fn repetitions_mut(&mut self) -> &mut Vec<Grapheme> {
        &mut self.repetitions
    }

    pub(crate) fn minimum(&self) -> u32 {
        self.min
    }

    pub(crate) fn maximum(&self) -> u32 {
        self.max
    }

    pub(crate) fn char_count(&self, is_non_ascii_char_escaped: bool) -> usize {
        if is_non_ascii_char_escaped {
            self.chars
                .iter()
                .map(|it| it.chars().map(|c| self.escape(c, false)).join(""))
                .join("")
                .chars()
                .count()
        } else {
            self.chars.iter().map(|it| it.chars().count()).sum()
        }
    }

    pub(crate) fn escape_non_ascii_chars(&mut self, use_surrogate_pairs: bool) {
        self.chars = self
            .chars
            .iter()
            .map(|it| {
                it.chars()
                    .map(|c| self.escape(c, use_surrogate_pairs))
                    .join("")
            })
            .collect_vec();
    }

    pub(crate) fn escape_regexp_symbols(
        &mut self,
        is_non_ascii_char_escaped: bool,
        is_astral_code_point_converted_to_surrogate: bool,
    ) {
        let characters = self.chars_mut();

        #[allow(clippy::needless_range_loop)]
        for i in 0..characters.len() {
            let mut character = characters[i].clone();

            for char_to_escape in CHARS_TO_ESCAPE.iter() {
                character =
                    character.replace(char_to_escape, &format!("{}{}", "\\", char_to_escape));
            }

            character = character
                .replace('\n', "\\n")
                .replace('\r', "\\r")
                .replace('\t', "\\t");

            if character == "\\" {
                character = "\\\\".to_string();
            }

            characters[i] = character;
        }

        if is_non_ascii_char_escaped {
            self.escape_non_ascii_chars(is_astral_code_point_converted_to_surrogate);
        }
    }

    fn escape(&self, c: char, use_surrogate_pairs: bool) -> String {
        if c.is_ascii() {
            c.to_string()
        } else if use_surrogate_pairs && ('\u{10000}'..'\u{10ffff}').contains(&c) {
            self.convert_to_surrogate_pair(c)
        } else {
            c.escape_unicode().to_string()
        }
    }

    fn convert_to_surrogate_pair(&self, c: char) -> String {
        c.encode_utf16(&mut [0; 2])
            .iter()
            .map(|it| format!("\\u{{{:x}}}", it))
            .join("")
    }
}

impl Display for Grapheme {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        let is_single_char = self.char_count(false) == 1
            || (self.chars.len() == 1 && self.chars[0].matches('\\').count() == 1);
        let is_range = self.min < self.max;
        let is_repetition = self.min > 1;
        let mut value = if self.repetitions.is_empty() {
            self.value()
        } else {
            self.repetitions.iter().map(|it| it.to_string()).join("")
        };
        value = Component::CharClass(value.clone())
            .to_repr(self.is_output_colorized && CHAR_CLASSES.contains(&&*value));

        if !is_range && is_repetition && is_single_char {
            write!(
                f,
                "{}{}",
                value,
                Component::Repetition(self.min, false).to_repr(self.is_output_colorized)
            )
        } else if !is_range && is_repetition && !is_single_char {
            write!(
                f,
                "{}{}",
                if self.is_capturing_group_enabled {
                    Component::CapturedParenthesizedExpression(
                        value,
                        self.is_verbose_mode_enabled,
                        false,
                    )
                    .to_repr(self.is_output_colorized)
                } else {
                    Component::UncapturedParenthesizedExpression(
                        value,
                        self.is_verbose_mode_enabled,
                        false,
                    )
                    .to_repr(self.is_output_colorized)
                },
                Component::Repetition(self.min, self.is_verbose_mode_enabled)
                    .to_repr(self.is_output_colorized)
            )
        } else if is_range && is_single_char {
            write!(
                f,
                "{}{}",
                value,
                Component::RepetitionRange(self.min, self.max, false)
                    .to_repr(self.is_output_colorized)
            )
        } else if is_range && !is_single_char {
            write!(
                f,
                "{}{}",
                if self.is_capturing_group_enabled {
                    Component::CapturedParenthesizedExpression(
                        value,
                        self.is_verbose_mode_enabled,
                        false,
                    )
                    .to_repr(self.is_output_colorized)
                } else {
                    Component::UncapturedParenthesizedExpression(
                        value,
                        self.is_verbose_mode_enabled,
                        false,
                    )
                    .to_repr(self.is_output_colorized)
                },
                Component::RepetitionRange(self.min, self.max, self.is_verbose_mode_enabled)
                    .to_repr(self.is_output_colorized)
            )
        } else {
            write!(f, "{}", value)
        }
    }
}
```

## File: `src/lib.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

//! ## 1. What does this tool do?
//!
//! *grex* is a library as well as a command-line utility that is meant to simplify the often
//! complicated and tedious task of creating regular expressions. It does so by automatically
//! generating a single regular expression from user-provided test cases. The resulting
//! expression is guaranteed to match the test cases which it was generated from.
//!
//! This project has started as a Rust port of the JavaScript tool
//! [*regexgen*](https://github.com/devongovett/regexgen) written by
//! [Devon Govett](https://github.com/devongovett). Although a lot of further useful features
//! could be added to it, its development was apparently ceased several years ago. The plan
//! is now to add these new features to *grex* as Rust really shines when it comes to
//! command-line tools. *grex* offers all features that *regexgen* provides, and more.
//!
//! The philosophy of this project is to generate the most specific regular expression
//! possible by default which exactly matches the given input only and nothing else.
//! With the use of command-line flags (in the CLI tool) or preprocessing methods
//! (in the library), more generalized expressions can be created.
//!
//! The produced expressions are [Perl-compatible regular expressions](https://www.pcre.org)
//! which are also compatible with the regular expression parser in Rust's
//! [*regex crate*](https://crates.io/crates/regex).
//! Other regular expression parsers or respective libraries from other programming languages
//! have not been tested so far, but they ought to be mostly compatible as well.
//!
//! ## 2. Do I still need to learn to write regexes then?
//!
//! **Definitely, yes!** Using the standard settings, *grex* produces a regular expression that
//! is guaranteed to match only the test cases given as input and nothing else. This has been
//! verified by [property tests](https://github.com/pemistahl/grex/blob/main/tests/property_tests.rs).
//! However, if the conversion to shorthand character classes such as `\w` is enabled, the
//! resulting regex matches a much wider scope of test cases. Knowledge about the consequences of
//! this conversion is essential for finding a correct regular expression for your business domain.
//!
//! *grex* uses an algorithm that tries to find the shortest possible regex for the given test cases.
//! Very often though, the resulting expression is still longer or more complex than it needs to be.
//! In such cases, a more compact or elegant regex can be created only by hand.
//! Also, every regular expression engine has different built-in optimizations.
//! *grex* does not know anything about those and therefore cannot optimize its regexes
//! for a specific engine.
//!
//! **So, please learn how to write regular expressions!** The currently best use case for *grex*
//! is to find an initial correct regex which should be inspected by hand if further optimizations
//! are possible.
//!
//! ## 3. Current features
//!
//! - literals
//! - character classes
//! - detection of common prefixes and suffixes
//! - detection of repeated substrings and conversion to `{min,max}` quantifier notation
//! - alternation using `|` operator
//! - optionality using `?` quantifier
//! - escaping of non-ascii characters, with optional conversion of astral code points to surrogate pairs
//! - case-sensitive or case-insensitive matching
//! - capturing or non-capturing groups
//! - optional anchors `^` and `$`
//! - fully compliant to [Unicode Standard 15.0](https://unicode.org/versions/Unicode15.0.0)
//! - fully compatible with [*regex* crate 1.9.0+](https://crates.io/crates/regex)
//! - correctly handles graphemes consisting of multiple Unicode symbols
//! - reads input strings from the command-line or from a file
//! - produces more readable expressions indented on multiple using optional verbose mode
//!
//! ## 4. How to use?
//!
//! The code snippets below show how to use the public api.
//!
//! For [more detailed examples](https://github.com/pemistahl/grex/tree/main#53-examples), please
//! take a look at the project's readme file on GitHub.
//!
//! ### 4.1 Default settings
//!
//! Test cases are passed either from a collection via [`RegExpBuilder::from()`]
//! or from a file via [`RegExpBuilder::from_file()`].
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["a", "aa", "aaa"]).build();
//! assert_eq!(regexp, "^a(?:aa?)?$");
//! ```
//!
//! ### 4.2 Convert to character classes
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["a", "aa", "123"])
//!     .with_conversion_of_digits()
//!     .with_conversion_of_words()
//!     .build();
//! assert_eq!(regexp, "^(?:\\d\\d\\d|\\w(?:\\w)?)$");
//! ```
//!
//! ### 4.3 Convert repeated substrings
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["aa", "bcbc", "defdefdef"])
//!     .with_conversion_of_repetitions()
//!     .build();
//! assert_eq!(regexp, "^(?:a{2}|(?:bc){2}|(?:def){3})$");
//! ```
//!
//! By default, *grex* converts each substring this way which is at least a single character long
//! and which is subsequently repeated at least once. You can customize these two parameters
//! if you like.
//!
//! In the following example, the test case `aa` is not converted to `a{2}` because the repeated
//! substring `a` has a length of 1, but the minimum substring length has been set to 2.
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["aa", "bcbc", "defdefdef"])
//!     .with_conversion_of_repetitions()
//!     .with_minimum_substring_length(2)
//!     .build();
//! assert_eq!(regexp, "^(?:aa|(?:bc){2}|(?:def){3})$");
//! ```
//!
//! Setting a minimum number of 2 repetitions in the next example, only the test case `defdefdef`
//! will be converted because it is the only one that is repeated twice.
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["aa", "bcbc", "defdefdef"])
//!     .with_conversion_of_repetitions()
//!     .with_minimum_repetitions(2)
//!     .build();
//! assert_eq!(regexp, "^(?:bcbc|aa|(?:def){3})$");
//! ```
//!
//! ### 4.4 Escape non-ascii characters
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["You smell like 💩."])
//!     .with_escaping_of_non_ascii_chars(false)
//!     .build();
//! assert_eq!(regexp, "^You smell like \\u{1f4a9}\\.$");
//! ```
//!
//! Old versions of JavaScript do not support unicode escape sequences for
//! the astral code planes (range `U+010000` to `U+10FFFF`). In order to
//! support these symbols in JavaScript regular expressions, the conversion
//! to surrogate pairs is necessary. More information on that matter can be
//! found [here](https://mathiasbynens.be/notes/javascript-unicode).
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["You smell like 💩."])
//!     .with_escaping_of_non_ascii_chars(true)
//!     .build();
//! assert_eq!(regexp, "^You smell like \\u{d83d}\\u{dca9}\\.$");
//! ```
//!
//! ### 4.5 Case-insensitive matching
//!
//! The regular expressions that *grex* generates are case-sensitive by default.
//! Case-insensitive matching can be enabled like so:
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["big", "BIGGER"])
//!     .with_case_insensitive_matching()
//!     .build();
//! assert_eq!(regexp, "(?i)^big(?:ger)?$");
//! ```
//!
//! ### 4.6 Capturing Groups
//!
//! Non-capturing groups are used by default.
//! Extending the previous example, you can switch to capturing groups instead.
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["big", "BIGGER"])
//!     .with_case_insensitive_matching()
//!     .with_capturing_groups()
//!     .build();
//! assert_eq!(regexp, "(?i)^big(ger)?$");
//! ```
//!
//! ### 4.7 Verbose mode
//!
//! If you find the generated regular expression hard to read, you can enable verbose mode.
//! The expression is then put on multiple lines and indented to make it more pleasant to the eyes.
//!
//! ```
//! use grex::RegExpBuilder;
//! use indoc::indoc;
//!
//! let regexp = RegExpBuilder::from(&["a", "b", "bcd"])
//!     .with_verbose_mode()
//!     .build();
//!
//! assert_eq!(regexp, indoc!(
//!     r#"
//!     (?x)
//!     ^
//!       (?:
//!         b
//!         (?:
//!           cd
//!         )?
//!         |
//!         a
//!       )
//!     $"#
//! ));
//! ```
//!
//! ### 4.8 Disable anchors
//!
//! By default, the anchors `^` and `$` are put around every generated regular expression in order
//! to ensure that it matches only the test cases given as input. Often enough, however, it is
//! desired to use the generated pattern as part of a larger one. For this purpose, the anchors
//! can be disabled, either separately or both of them.
//!
//! ```
//! use grex::RegExpBuilder;
//!
//! let regexp = RegExpBuilder::from(&["a", "aa", "aaa"])
//!     .without_anchors()
//!     .build();
//! assert_eq!(regexp, "a(?:aa?)?");
//! ```
//!
//! ### 5. How does it work?
//!
//! 1. A [deterministic finite automaton](https://en.wikipedia.org/wiki/Deterministic_finite_automaton) (DFA)
//!    is created from the input strings.
//!
//! 2. The number of states and transitions between states in the DFA is reduced by applying
//!    [Hopcroft's DFA minimization algorithm](https://en.wikipedia.org/wiki/DFA_minimization#Hopcroft.27s_algorithm).
//!
//! 3. The minimized DFA is expressed as a system of linear equations which are solved with
//!    [Brzozowski's algebraic method](http://cs.stackexchange.com/questions/2016/how-to-convert-finite-automata-to-regular-expressions#2392),
//!    resulting in the final regular expression.

#[macro_use]
mod macros;

mod builder;
mod char_range;
mod cluster;
mod component;
mod config;
mod dfa;
mod expression;
mod format;
mod grapheme;
mod quantifier;
mod regexp;
mod substring;
mod unicode_tables;

#[cfg(feature = "python")]
mod python;

#[cfg(target_family = "wasm")]
mod wasm;

pub use builder::RegExpBuilder;

#[cfg(target_family = "wasm")]
pub use wasm::RegExpBuilder as WasmRegExpBuilder;
```

## File: `src/macros.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

macro_rules! btreeset {
    ( $( $value: expr ),* ) => {{
        let mut set = std::collections::BTreeSet::new();
        $( set.insert($value); )*
        set
    }};
}
```

## File: `src/main.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#[cfg(not(target_family = "wasm"))]
mod cli {
    use clap::ArgAction;
    use clap::Parser;
    use grex::RegExpBuilder;
    use itertools::Itertools;
    use std::io::{stdin, BufRead, Error, ErrorKind, IsTerminal, Read};
    use std::path::PathBuf;

    #[derive(Parser)]
    #[command(
        author = "© 2019-today Peter M. Stahl <pemistahl@gmail.com>",
        about = "Licensed under the Apache License, Version 2.0\n\
                 Downloadable from https://crates.io/crates/grex\n\
                 Source code at https://github.com/pemistahl/grex\n\n\
                 grex generates regular expressions from user-provided test cases.",
        version,
        override_usage = "grex [OPTIONS] {INPUT...|--file <FILE>}",
        help_template = "{name} {version}\n{author}\n{about}\n\n{usage-heading} {usage}\n\n{all-args}",
        disable_help_flag = true,
        disable_version_flag = true
    )]
    pub(crate) struct Cli {
        // --------------------
        // INPUT
        // --------------------
        /// One or more test cases separated by blank space
        ///
        /// Use a hyphen `-` to read test cases from standard input.
        ///
        /// Conflicts with --file.
        #[arg(
            value_name = "INPUT",
            allow_hyphen_values = true,
            required_unless_present = "file",
            conflicts_with = "file",
            help_heading = "Input",
            display_order = 1
        )]
        input: Vec<String>,

        /// Reads test cases on separate lines from a file.
        ///
        /// Lines may be ended with either a newline `\n` or a carriage return with a line feed `\r\n`.
        /// The final line ending is optional.
        ///
        /// Use a hyphen `-` to read the filename from standard input.
        ///
        /// Conflicts with INPUT...
        #[arg(
            name = "file",
            value_name = "FILE",
            short,
            long,
            required_unless_present = "input",
            help_heading = "Input",
            display_order = 2
        )]
        file_path: Option<PathBuf>,

        // --------------------
        // DIGIT OPTIONS
        // --------------------
        /// Converts any Unicode decimal digit to \d.
        ///
        /// Takes precedence over --words if both are set.
        /// Decimal digits are converted to \d, remaining word characters to \w.
        ///
        /// Takes precedence over --non-spaces if both are set.
        /// Decimal digits are converted to \d, remaining non-space characters to \S.
        #[arg(name = "digits", short, long, help_heading = "Digit Options")]
        is_digit_converted: bool,

        /// Converts any character which is not a Unicode decimal digit to \D.
        ///
        /// Takes precedence over --non-words if both are set.
        /// Non-digits which are also non-word characters are converted to \D.
        ///
        /// Takes precedence over --non-spaces if both are set.
        /// Non-digits which are also non-space characters are converted to \D.
        #[arg(name = "non-digits", short = 'D', long, help_heading = "Digit Options")]
        is_non_digit_converted: bool,

        // --------------------
        // WHITESPACE OPTIONS
        // --------------------
        /// Converts any Unicode whitespace character to \s.
        ///
        /// Takes precedence over --non-digits if both are set.
        /// Whitespace is converted to \s, remaining non-digits to \D.
        ///
        /// Takes precedence over --non-words if both are set.
        /// Whitespace is converted to \s, remaining non-word characters to \W.
        #[arg(name = "spaces", short, long, help_heading = "Whitespace Options")]
        is_space_converted: bool,

        /// Converts any character which is not a Unicode whitespace character to \S
        #[arg(
            name = "non-spaces",
            short = 'S',
            long,
            help_heading = "Whitespace Options"
        )]
        is_non_space_converted: bool,

        // --------------------
        // WORD OPTIONS
        // --------------------
        /// Converts any Unicode word character to \w.
        ///
        /// Takes precedence over --non-digits if both are set.
        /// Word characters are converted to \w, remaining non-digits to \D.
        ///
        /// Takes precedence over --non-spaces if both are set.
        /// Word characters are converted to \w, remaining non-whitespace to \S.
        #[arg(name = "words", short, long, help_heading = "Word Options")]
        is_word_converted: bool,

        /// Converts any character which is not a Unicode word character to \W.
        ///
        /// Takes precedence over --non-spaces if both are set.
        /// Non-word characters which are also non-whitespace are converted to \W.
        #[arg(name = "non-words", short = 'W', long, help_heading = "Word Options")]
        is_non_word_converted: bool,

        // --------------------
        // ESCAPING OPTIONS
        // --------------------
        /// Replaces all non-ASCII characters with unicode escape sequences.
        #[arg(name = "escape", short, long, help_heading = "Escaping Options")]
        is_non_ascii_char_escaped: bool,

        /// Converts astral code points to surrogate pairs if --escape is set.
        #[arg(
            name = "with-surrogates",
            long,
            requires = "escape",
            help_heading = "Escaping Options"
        )]
        is_astral_code_point_converted_to_surrogate: bool,

        // --------------------
        // REPETITION OPTIONS
        // --------------------
        /// Detects repeated non-overlapping substrings and converts them to {min,max} quantifier notation.
        #[arg(
            name = "repetitions",
            short,
            long,
            help_heading = "Repetition Options",
            display_order = 1
        )]
        is_repetition_converted: bool,

        /// Specifies the minimum quantity of substring repetitions to be converted if --repetitions is set.
        #[arg(
            name = "min-repetitions",
            value_name = "QUANTITY",
            long,
            default_value_t = 1,
            value_parser = repetition_options_parser,
            help_heading = "Repetition Options"
        )]
        minimum_repetitions: u32,

        /// Specifies the minimum length a repeated substring must have
        /// in order to be converted if --repetitions is set.
        #[arg(
            name = "min-substring-length",
            value_name = "LENGTH",
            long,
            default_value_t = 1,
            value_parser = repetition_options_parser,
            help_heading = "Repetition Options"
        )]
        minimum_substring_length: u32,

        // --------------------
        // ANCHOR OPTIONS
        // --------------------
        /// Removes the caret anchor `^` from the resulting regular expression.
        ///
        /// By default, the caret anchor is added to every generated regular expression
        /// which guarantees that the expression matches the test cases
        /// given as input only at the start of a string.
        ///
        /// This flag removes the anchor, thereby allowing to match the test cases
        /// also when they do not occur at the start of a string.
        #[arg(name = "no-start-anchor", long, help_heading = "Anchor Options")]
        is_caret_anchor_disabled: bool,

        /// Removes the dollar sign anchor `$` from the resulting regular expression.
        ///
        /// By default, the dollar sign anchor is added to every generated regular expression
        /// which guarantees that the expression matches the test cases given as input
        /// only at the end of a string.
        ///
        /// This flag removes the anchor, thereby allowing to match the test cases
        /// also when they do not occur at the end of a string.
        #[arg(name = "no-end-anchor", long, help_heading = "Anchor Options")]
        is_dollar_sign_anchor_disabled: bool,

        /// Removes the caret and dollar sign anchors from the resulting regular expression.
        ///
        /// By default, anchors are added to every generated regular expression
        /// which guarantees that the expression exactly matches only the test cases given as input
        /// and nothing else.
        ///
        /// This flag removes the anchors, thereby allowing to match the test cases
        /// also when they occur within a larger string that contains other content as well.
        #[arg(name = "no-anchors", long, help_heading = "Anchor Options")]
        are_anchors_disabled: bool,

        // --------------------
        // DISPLAY OPTIONS
        // --------------------
        /// Produces a nicer-looking regular expression in verbose mode.
        #[arg(
            name = "verbose",
            short = 'x',
            long,
            help_heading = "Display Options",
            display_order = 1
        )]
        is_verbose_mode_enabled: bool,

        /// Provides syntax highlighting for the resulting regular expression.
        #[arg(name = "colorize", short, long, help_heading = "Display Options")]
        is_output_colorized: bool,

        // ---------------------
        // MISCELLANEOUS OPTIONS
        // ---------------------
        /// Performs case-insensitive matching, letters match both upper and lower case.
        #[arg(
            name = "ignore-case",
            short,
            long,
            help_heading = "Miscellaneous Options",
            display_order = 1
        )]
        is_case_ignored: bool,

        /// Replaces non-capturing groups with capturing ones.
        #[arg(
            name = "capture-groups",
            short = 'g',
            long,
            help_heading = "Miscellaneous Options",
            display_order = 2
        )]
        is_group_captured: bool,

        /// Prints help information
        #[arg(
            name = "help",
            short = 'h',
            long,
            action = ArgAction::Help,
            help_heading = "Miscellaneous Options",
            display_order = 3
        )]
        help: Option<String>,

        /// Prints version information
        #[arg(
            name = "version",
            short = 'v',
            long,
            action = ArgAction::Version,
            help_heading = "Miscellaneous Options",
            display_order = 4
        )]
        version: Option<String>,
    }

    pub(crate) fn obtain_input(cli: &Cli) -> Result<Vec<String>, Error> {
        let is_stdin_available = !stdin().is_terminal();

        if !cli.input.is_empty() {
            let is_single_item = cli.input.len() == 1;
            let is_hyphen = cli.input.first().unwrap() == "-";

            if is_single_item && is_hyphen && is_stdin_available {
                Ok(stdin()
                    .lock()
                    .lines()
                    .map(|line| line.unwrap())
                    .collect_vec())
            } else {
                Ok(cli.input.clone())
            }
        } else if let Some(file_path) = &cli.file_path {
            let is_hyphen = file_path.as_os_str() == "-";
            let path = if is_hyphen && is_stdin_available {
                let mut stdin_file_path = String::new();
                stdin().read_to_string(&mut stdin_file_path)?;
                PathBuf::from(stdin_file_path.trim())
            } else {
                file_path.to_path_buf()
            };
            match std::fs::read_to_string(path) {
                Ok(file_content) => Ok(file_content.lines().map(|it| it.to_string()).collect_vec()),
                Err(error) => Err(error),
            }
        } else {
            Err(Error::new(
                ErrorKind::InvalidInput,
                "error: no valid input could be found whatsoever",
            ))
        }
    }

    pub(crate) fn handle_input(
        cli: &Cli,
        input: Result<Vec<String>, Error>,
    ) -> Result<(), Box<dyn std::error::Error>> {
        match input {
            Ok(test_cases) => {
                let mut builder = RegExpBuilder::from(&test_cases);

                if cli.is_digit_converted {
                    builder.with_conversion_of_digits();
                }

                if cli.is_non_digit_converted {
                    builder.with_conversion_of_non_digits();
                }

                if cli.is_space_converted {
                    builder.with_conversion_of_whitespace();
                }

                if cli.is_non_space_converted {
                    builder.with_conversion_of_non_whitespace();
                }

                if cli.is_word_converted {
                    builder.with_conversion_of_words();
                }

                if cli.is_non_word_converted {
                    builder.with_conversion_of_non_words();
                }

                if cli.is_repetition_converted {
                    builder.with_conversion_of_repetitions();
                }

                if cli.is_case_ignored {
                    builder.with_case_insensitive_matching();
                }

                if cli.is_group_captured {
                    builder.with_capturing_groups();
                }

                if cli.is_non_ascii_char_escaped {
                    builder.with_escaping_of_non_ascii_chars(
                        cli.is_astral_code_point_converted_to_surrogate,
                    );
                }

                if cli.is_verbose_mode_enabled {
                    builder.with_verbose_mode();
                }

                if cli.is_caret_anchor_disabled {
                    builder.without_start_anchor();
                }

                if cli.is_dollar_sign_anchor_disabled {
                    builder.without_end_anchor();
                }

                if cli.are_anchors_disabled {
                    builder.without_anchors();
                }

                if cli.is_output_colorized {
                    builder.with_syntax_highlighting();
                }

                builder
                    .with_minimum_repetitions(cli.minimum_repetitions)
                    .with_minimum_substring_length(cli.minimum_substring_length);

                let regexp = builder.build();

                println!("{}", regexp);
                Ok(())
            }
            Err(error) => match error.kind() {
                ErrorKind::NotFound => Err("error: the specified file could not be found".into()),
                ErrorKind::InvalidData => {
                    Err("error: the specified file's encoding is not valid UTF-8".into())
                }
                ErrorKind::PermissionDenied => {
                    Err("permission denied: the specified file could not be opened".into())
                }
                _ => Err(format!("error: {}", error).into()),
            },
        }
    }

    fn repetition_options_parser(value: &str) -> Result<u32, String> {
        match value.parse::<u32>() {
            Ok(parsed_value) => {
                if parsed_value > 0 {
                    Ok(parsed_value)
                } else {
                    Err(String::from("Value must not be zero"))
                }
            }
            Err(_) => Err(String::from("Value is not a valid unsigned integer")),
        }
    }
}

#[cfg(not(target_family = "wasm"))]
fn main() {
    use clap::Parser;
    let cli = cli::Cli::parse();
    if let Err(e) = cli::handle_input(&cli, cli::obtain_input(&cli)) {
        eprintln!("{}", e);
        std::process::exit(1);
    }
}

#[cfg(target_family = "wasm")]
fn main() {}
```

## File: `src/python.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::builder::{
    RegExpBuilder, MINIMUM_REPETITIONS_MESSAGE, MINIMUM_SUBSTRING_LENGTH_MESSAGE,
    MISSING_TEST_CASES_MESSAGE,
};
use crate::config::RegExpConfig;
use pyo3::exceptions::PyValueError;
use pyo3::prelude::*;
use pyo3::types::PyType;
use regex::{Captures, Regex};
use std::sync::LazyLock;

#[pymodule]
fn grex(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<RegExpBuilder>()?;
    Ok(())
}

#[pymethods]
impl RegExpBuilder {
    #[new]
    fn new(test_cases: Vec<String>) -> PyResult<Self> {
        if test_cases.is_empty() {
            Err(PyValueError::new_err(MISSING_TEST_CASES_MESSAGE))
        } else {
            Ok(Self {
                test_cases,
                config: RegExpConfig::new(),
            })
        }
    }

    /// Specify the test cases to build the regular expression from.
    ///
    /// The test cases need not be sorted because `RegExpBuilder` sorts them internally.
    ///
    /// Args:
    ///     test_cases (list[str]): The list of test cases
    ///
    /// Raises:
    ///     ValueError: if `test_cases` is empty
    #[classmethod]
    fn from_test_cases(_cls: &Bound<PyType>, test_cases: Vec<String>) -> PyResult<Self> {
        Self::new(test_cases)
    }

    /// Convert any Unicode decimal digit to character class `\d`.
    ///
    /// This method takes precedence over `with_conversion_of_words` if both are set.
    /// Decimal digits are converted to `\d`, the remaining word characters to `\w`.
    ///
    /// This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
    /// Decimal digits are converted to `\d`, the remaining non-whitespace characters to `\S`.
    #[pyo3(name = "with_conversion_of_digits")]
    fn py_with_conversion_of_digits(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_digit_converted = true;
        self_
    }

    /// Convert any character which is not a Unicode decimal digit to character class `\D`.
    ///
    /// This method takes precedence over `with_conversion_of_non_words` if both are set.
    /// Non-digits which are also non-word characters are converted to `\D`.
    ///
    /// This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
    /// Non-digits which are also non-space characters are converted to `\D`.
    #[pyo3(name = "with_conversion_of_non_digits")]
    fn py_with_conversion_of_non_digits(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_non_digit_converted = true;
        self_
    }

    /// Convert any Unicode whitespace character to character class `\s`.
    ///
    /// This method takes precedence over `with_conversion_of_non_digits` if both are set.
    /// Whitespace characters are converted to `\s`, the remaining non-digit characters to `\D`.
    ///
    /// This method takes precedence over `with_conversion_of_non_words` if both are set.
    /// Whitespace characters are converted to `\s`, the remaining non-word characters to `\W`.
    #[pyo3(name = "with_conversion_of_whitespace")]
    fn py_with_conversion_of_whitespace(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_space_converted = true;
        self_
    }

    /// Convert any character which is not a Unicode whitespace character to character class `\S`.
    #[pyo3(name = "with_conversion_of_non_whitespace")]
    fn py_with_conversion_of_non_whitespace(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_non_space_converted = true;
        self_
    }

    /// Convert any Unicode word character to character class `\w`.
    ///
    /// This method takes precedence over `with_conversion_of_non_digits` if both are set.
    /// Word characters are converted to `\w`, the remaining non-digit characters to `\D`.
    ///
    /// This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
    /// Word characters are converted to `\w`, the remaining non-space characters to `\S`.
    #[pyo3(name = "with_conversion_of_words")]
    fn py_with_conversion_of_words(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_word_converted = true;
        self_
    }

    /// Convert any character which is not a Unicode word character to character class `\W`.
    ///
    /// This method takes precedence over `with_conversion_of_non_whitespace` if both are set.
    /// Non-words which are also non-space characters are converted to `\W`.
    #[pyo3(name = "with_conversion_of_non_words")]
    fn py_with_conversion_of_non_words(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_non_word_converted = true;
        self_
    }

    /// Detect repeated non-overlapping substrings and convert them to `{min,max}` quantifier notation.
    #[pyo3(name = "with_conversion_of_repetitions")]
    fn py_with_conversion_of_repetitions(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_repetition_converted = true;
        self_
    }

    /// Enable case-insensitive matching of test cases so that letters match both upper and lower case.
    #[pyo3(name = "with_case_insensitive_matching")]
    fn py_with_case_insensitive_matching(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_case_insensitive_matching = true;
        self_
    }

    /// Replace non-capturing groups by capturing ones.
    #[pyo3(name = "with_capturing_groups")]
    fn py_with_capturing_groups(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_capturing_group_enabled = true;
        self_
    }

    /// Specify the minimum quantity of substring repetitions to be converted if `with_conversion_of_repetitions` is set.
    ///
    /// If the quantity is not explicitly set with this method, a default value of 1 will be used.
    ///
    /// Args:
    ///     quantity (int): The minimum quantity of substring repetitions
    ///
    /// Raises:
    ///     ValueError: if `quantity` is zero
    #[pyo3(name = "with_minimum_repetitions")]
    fn py_with_minimum_repetitions(
        mut self_: PyRefMut<Self>,
        quantity: i32,
    ) -> PyResult<PyRefMut<Self>> {
        if quantity <= 0 {
            Err(PyValueError::new_err(MINIMUM_REPETITIONS_MESSAGE))
        } else {
            self_.config.minimum_repetitions = quantity as u32;
            Ok(self_)
        }
    }

    /// Specify the minimum length a repeated substring must have in order to be converted if `with_conversion_of_repetitions` is set.
    ///
    /// If the length is not explicitly set with this method, a default value of 1 will be used.
    ///
    /// Args:
    ///     length (int): The minimum substring length
    ///
    /// Raises:
    ///     ValueError: if `length` is zero
    #[pyo3(name = "with_minimum_substring_length")]
    fn py_with_minimum_substring_length(
        mut self_: PyRefMut<Self>,
        length: i32,
    ) -> PyResult<PyRefMut<Self>> {
        if length <= 0 {
            Err(PyValueError::new_err(MINIMUM_SUBSTRING_LENGTH_MESSAGE))
        } else {
            self_.config.minimum_substring_length = length as u32;
            Ok(self_)
        }
    }

    /// Convert non-ASCII characters to unicode escape sequences.
    ///
    /// The parameter `use_surrogate_pairs` specifies whether to convert astral code planes
    /// (range `U+010000` to `U+10FFFF`) to surrogate pairs.
    ///
    /// Args:
    ///     use_surrogate_pairs (bool): Whether to convert astral code planes to surrogate pairs
    #[pyo3(name = "with_escaping_of_non_ascii_chars")]
    fn py_with_escaping_of_non_ascii_chars(
        mut self_: PyRefMut<Self>,
        use_surrogate_pairs: bool,
    ) -> PyRefMut<Self> {
        self_.config.is_non_ascii_char_escaped = true;
        self_.config.is_astral_code_point_converted_to_surrogate = use_surrogate_pairs;
        self_
    }

    /// Produce a nicer looking regular expression in verbose mode.
    #[pyo3(name = "with_verbose_mode")]
    fn py_with_verbose_mode(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_verbose_mode_enabled = true;
        self_
    }

    /// Remove the caret anchor '^' from the resulting regular expression, thereby allowing to
    /// match the test cases also when they do not occur at the start of a string.
    #[pyo3(name = "without_start_anchor")]
    fn py_without_start_anchor(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_start_anchor_disabled = true;
        self_
    }

    /// Remove the dollar sign anchor '$' from the resulting regular expression, thereby allowing
    /// to match the test cases also when they do not occur at the end of a string.
    #[pyo3(name = "without_end_anchor")]
    fn py_without_end_anchor(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_end_anchor_disabled = true;
        self_
    }

    /// Remove the caret and dollar sign anchors from the resulting regular expression, thereby
    /// allowing to match the test cases also when they occur within a larger string that contains
    /// other content as well.
    #[pyo3(name = "without_anchors")]
    fn py_without_anchors(mut self_: PyRefMut<Self>) -> PyRefMut<Self> {
        self_.config.is_start_anchor_disabled = true;
        self_.config.is_end_anchor_disabled = true;
        self_
    }

    /// Build the actual regular expression using the previously given settings.
    #[pyo3(name = "build")]
    fn py_build(&mut self) -> String {
        let regexp = self.build();
        if self.config.is_non_ascii_char_escaped {
            replace_unicode_escape_sequences(regexp)
        } else {
            regexp
        }
    }
}

/// Replaces Rust Unicode escape sequences with Python Unicode escape sequences.
fn replace_unicode_escape_sequences(regexp: String) -> String {
    static FOUR_CHARS_ESCAPE_SEQUENCE: LazyLock<Regex> =
        LazyLock::new(|| Regex::new(r"\\u\{([0-9a-f]{4})\}").unwrap());

    static FIVE_CHARS_ESCAPE_SEQUENCE: LazyLock<Regex> =
        LazyLock::new(|| Regex::new(r"\\u\{([0-9a-f]{5})\}").unwrap());

    let mut replacement = FOUR_CHARS_ESCAPE_SEQUENCE
        .replace_all(&regexp, |caps: &Captures| format!("\\u{}", &caps[1]))
        .to_string();

    replacement = FIVE_CHARS_ESCAPE_SEQUENCE
        .replace_all(&replacement, |caps: &Captures| {
            format!("\\U000{}", &caps[1])
        })
        .to_string();

    replacement
}
```

## File: `src/quantifier.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use std::fmt::{Display, Formatter, Result};

#[derive(Clone, Debug, Eq, PartialEq)]
pub(crate) enum Quantifier {
    KleeneStar,
    QuestionMark,
}

impl Display for Quantifier {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        write!(
            f,
            "{}",
            match self {
                Quantifier::KleeneStar => '*',
                Quantifier::QuestionMark => '?',
            }
        )
    }
}
```

## File: `src/regexp.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

use crate::cluster::GraphemeCluster;
use crate::component::Component;
use crate::config::RegExpConfig;
use crate::dfa::Dfa;
use crate::expression::Expression;
use itertools::Itertools;
use regex::Regex;
use std::cmp::Ordering;
use std::fmt::{Display, Formatter, Result};

pub(crate) struct RegExp<'a> {
    ast: Expression<'a>,
    config: &'a RegExpConfig,
}

impl<'a> RegExp<'a> {
    pub(crate) fn from(test_cases: &'a mut Vec<String>, config: &'a RegExpConfig) -> Self {
        if config.is_case_insensitive_matching {
            Self::convert_for_case_insensitive_matching(test_cases);
        }
        Self::sort(test_cases);
        let grapheme_clusters = Self::grapheme_clusters(test_cases, config);
        let mut dfa = Dfa::from(&grapheme_clusters, true, config);
        let mut ast = Expression::from(dfa, config);

        if config.is_start_anchor_disabled && config.is_end_anchor_disabled {
            let mut regex = Self::convert_expr_to_regex(&ast, config);

            if config.is_verbose_mode_enabled {
                // Remove line breaks before checking matches, otherwise check will be incorrect.
                regex = Regex::new(&regex.to_string().replace('\n', "")).unwrap();
            }

            if !Self::is_each_test_case_matched_after_rotating_alternations(
                &regex, &mut ast, test_cases,
            ) {
                dfa = Dfa::from(&grapheme_clusters, false, config);
                ast = Expression::from(dfa, config);
                regex = Self::convert_expr_to_regex(&ast, config);

                if !Self::regex_matches_all_test_cases(&regex, test_cases) {
                    let mut exprs = vec![];
                    for cluster in grapheme_clusters {
                        let literal = Expression::new_literal(cluster, config);
                        exprs.push(literal);
                    }
                    ast = Expression::new_alternation(exprs, config);
                }
            }
        }

        Self { ast, config }
    }

    fn convert_for_case_insensitive_matching(test_cases: &mut Vec<String>) {
        // Convert only those test cases to lowercase if
        // they keep their original number of characters.
        // Otherwise, "İ" -> "i\u{307}" would not match "İ".
        *test_cases = test_cases
            .iter()
            .map(|it| {
                let lower_test_case = it.to_lowercase();
                if lower_test_case.chars().count() == it.chars().count() {
                    lower_test_case
                } else {
                    it.to_string()
                }
            })
            .collect_vec();
    }

    fn convert_expr_to_regex(expr: &Expression, config: &RegExpConfig) -> Regex {
        if config.is_output_colorized {
            let color_replace_regex = Regex::new("\u{1b}\\[(?:\\d+;\\d+|0)m").unwrap();
            Regex::new(&color_replace_regex.replace_all(&expr.to_string(), "")).unwrap()
        } else {
            Regex::new(&expr.to_string()).unwrap()
        }
    }

    fn regex_matches_all_test_cases(regex: &Regex, test_cases: &[String]) -> bool {
        test_cases
            .iter()
            .all(|test_case| regex.find_iter(test_case).count() == 1)
    }

    fn sort(test_cases: &mut Vec<String>) {
        test_cases.sort();
        test_cases.dedup();
        test_cases.sort_by(|a, b| match a.len().cmp(&b.len()) {
            Ordering::Equal => a.cmp(b),
            other => other,
        });
    }

    fn grapheme_clusters(
        test_cases: &'a [String],
        config: &'a RegExpConfig,
    ) -> Vec<GraphemeCluster<'a>> {
        let mut clusters = test_cases
            .iter()
            .map(|it| GraphemeCluster::from(it, config))
            .collect_vec();

        if config.is_char_class_feature_enabled() {
            for cluster in clusters.iter_mut() {
                cluster.convert_to_char_classes();
            }
        }

        if config.is_repetition_converted {
            for cluster in clusters.iter_mut() {
                cluster.convert_repetitions();
            }
        }

        clusters
    }

    fn is_each_test_case_matched_after_rotating_alternations(
        regex: &Regex,
        expr: &mut Expression,
        test_cases: &[String],
    ) -> bool {
        for _ in 1..test_cases.len() {
            if Self::regex_matches_all_test_cases(regex, test_cases) {
                return true;
            } else if let Expression::Alternation(options, _, _, _) = expr {
                options.rotate_right(1);
            } else if let Expression::Concatenation(first, second, _, _, _) = expr {
                let a: &mut Expression = first;
                let b: &mut Expression = second;

                if let Expression::Alternation(options, _, _, _) = a {
                    options.rotate_right(1);
                } else if let Expression::Alternation(options, _, _, _) = b {
                    options.rotate_right(1);
                }
            }
        }
        false
    }
}

impl Display for RegExp<'_> {
    fn fmt(&self, f: &mut Formatter<'_>) -> Result {
        let flag =
            if self.config.is_case_insensitive_matching && self.config.is_verbose_mode_enabled {
                Component::IgnoreCaseAndVerboseModeFlag.to_repr(self.config.is_output_colorized)
            } else if self.config.is_case_insensitive_matching {
                Component::IgnoreCaseFlag.to_repr(self.config.is_output_colorized)
            } else if self.config.is_verbose_mode_enabled {
                Component::VerboseModeFlag.to_repr(self.config.is_output_colorized)
            } else {
                String::new()
            };

        let caret = if self.config.is_start_anchor_disabled {
            String::new()
        } else {
            Component::Caret(self.config.is_verbose_mode_enabled)
                .to_repr(self.config.is_output_colorized)
        };

        let dollar_sign = if self.config.is_end_anchor_disabled {
            String::new()
        } else {
            Component::DollarSign(self.config.is_verbose_mode_enabled)
                .to_repr(self.config.is_output_colorized)
        };

        let mut regexp = match self.ast {
            Expression::Alternation(_, _, _, _) => {
                format!(
                    "{}{}{}{}",
                    flag,
                    caret,
                    if self.config.is_capturing_group_enabled {
                        Component::CapturedParenthesizedExpression(
                            self.ast.to_string(),
                            self.config.is_verbose_mode_enabled,
                            false,
                        )
                        .to_repr(self.config.is_output_colorized)
                    } else {
                        Component::UncapturedParenthesizedExpression(
                            self.ast.to_string(),
                            self.config.is_verbose_mode_enabled,
                            false,
                        )
                        .to_repr(self.config.is_output_colorized)
                    },
                    dollar_sign
                )
            }
            _ => {
                format!("{}{}{}{}", flag, caret, self.ast, dollar_sign)
            }
        };

        regexp = regexp
            .replace('\u{b}', "\\v") // U+000B Line Tabulation
            .replace('\u{c}', "\\f"); // U+000C Form Feed

        if self.config.is_verbose_mode_enabled {
            regexp = regexp
                .replace('#', "\\#")
                .replace(
                    [
                        ' ', ' ', ' ', ' ', ' ', ' ', ' ', '\u{85}', '\u{a0}', '\u{1680}',
                        '\u{2000}', '\u{2001}', '\u{2002}', '\u{2003}', '\u{2004}', '\u{2005}',
                        '\u{2006}', '\u{2007}', '\u{2008}', '\u{2009}', '\u{200a}', '\u{2028}',
                        '\u{2029}', '\u{202f}', '\u{205f}', '\u{3000}',
                    ],
                    "\\s",
                )
                .replace(' ', "\\ ");
        }

        write!(
            f,
            "{}",
            if self.config.is_verbose_mode_enabled {
                indent_regexp(regexp, self.config)
            } else {
                regexp
            }
        )
    }
}

fn indent_regexp(regexp: String, config: &RegExpConfig) -> String {
    let mut indented_regexp = vec![];
    let mut nesting_level = 0;

    for (i, line) in regexp.lines().enumerate() {
        if i == 1 && config.is_start_anchor_disabled {
            nesting_level += 1;
        }
        if line.is_empty() {
            continue;
        }

        let is_colored_line = line.starts_with("\u{1b}[");

        if nesting_level > 0
            && ((is_colored_line && (line.contains('$') || line.contains(')')))
                || (line == "$" || line.starts_with(')')))
        {
            nesting_level -= 1;
        }

        let indentation = "  ".repeat(nesting_level);
        indented_regexp.push(format!("{indentation}{line}"));

        if (is_colored_line && (line.contains('^') || (i > 0 && line.contains('('))))
            || (line == "^" || (i > 0 && line.starts_with('(')))
        {
            nesting_level += 1;
        }
    }

    indented_regexp.join("\n")
}
```

## File: `src/substring.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

pub(crate) enum Substring {
    Prefix,
    Suffix,
}
```

## File: `src/wasm.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#![allow(non_snake_case)]

use crate::builder::{
    RegExpBuilder as Builder, MINIMUM_REPETITIONS_MESSAGE, MINIMUM_SUBSTRING_LENGTH_MESSAGE,
    MISSING_TEST_CASES_MESSAGE,
};
use itertools::Itertools;
use wasm_bindgen::prelude::*;

/// This class builds regular expressions from user-provided test cases.
#[wasm_bindgen]
#[derive(Clone)]
pub struct RegExpBuilder {
    builder: Builder,
}

#[wasm_bindgen]
impl RegExpBuilder {
    /// Specifies the test cases to build the regular expression from.
    ///
    /// The test cases need not be sorted because `RegExpBuilder` sorts them internally.
    ///
    /// ⚠ Throws an error if `testCases` is empty.
    pub fn from(testCases: Box<[JsValue]>) -> Result<RegExpBuilder, JsValue> {
        let strs = testCases
            .iter()
            .filter_map(|it| it.as_string())
            .collect_vec();

        if strs.is_empty() {
            return Err(JsValue::from(MISSING_TEST_CASES_MESSAGE));
        }
        Ok(RegExpBuilder {
            builder: Builder::from(&strs),
        })
    }

    /// Tells `RegExpBuilder` to convert any Unicode decimal digit to character class `\d`.
    ///
    /// This method takes precedence over `withConversionOfWords` if both are set.
    /// Decimal digits are converted to `\d`, the remaining word characters to `\w`.
    ///
    /// This method takes precedence over `withConversionOfWhitespace` if both are set.
    /// Decimal digits are converted to `\d`, the remaining non-whitespace characters to `\S`.
    pub fn withConversionOfDigits(&mut self) -> RegExpBuilder {
        self.builder.config.is_digit_converted = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to convert any character which is not
    /// a Unicode decimal digit to character class `\D`.
    ///
    /// This method takes precedence over `withConversionOfNonWords` if both are set.
    /// Non-digits which are also non-word characters are converted to `\D`.
    ///
    /// This method takes precedence over `withConversionOfNonWhitespace` if both are set.
    /// Non-digits which are also non-space characters are converted to `\D`.
    pub fn withConversionOfNonDigits(&mut self) -> RegExpBuilder {
        self.builder.config.is_non_digit_converted = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to convert any Unicode whitespace character to character class `\s`.
    ///
    /// This method takes precedence over `withConversionOfNonDigits` if both are set.
    /// Whitespace characters are converted to `\s`, the remaining non-digit characters to `\D`.
    ///
    /// This method takes precedence over `withConversionOfNonWords` if both are set.
    /// Whitespace characters are converted to `\s`, the remaining non-word characters to `\W`.
    pub fn withConversionOfWhitespace(&mut self) -> RegExpBuilder {
        self.builder.config.is_space_converted = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to convert any character which is not
    /// a Unicode whitespace character to character class `\S`.
    pub fn withConversionOfNonWhitespace(&mut self) -> RegExpBuilder {
        self.builder.config.is_non_space_converted = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to convert any Unicode word character to character class `\w`.
    ///
    /// This method takes precedence over `withConversionOfNonDigits` if both are set.
    /// Word characters are converted to `\w`, the remaining non-digit characters to `\D`.
    ///
    /// This method takes precedence over `withConversionOfNonWhitespace` if both are set.
    /// Word characters are converted to `\w`, the remaining non-space characters to `\S`.
    pub fn withConversionOfWords(&mut self) -> RegExpBuilder {
        self.builder.config.is_word_converted = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to convert any character which is not
    /// a Unicode word character to character class `\W`.
    ///
    /// This method takes precedence over `withConversionOfNonWhitespace` if both are set.
    /// Non-words which are also non-space characters are converted to `\W`.
    pub fn withConversionOfNonWords(&mut self) -> RegExpBuilder {
        self.builder.config.is_non_word_converted = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to detect repeated non-overlapping substrings and
    /// to convert them to `{min,max}` quantifier notation.
    pub fn withConversionOfRepetitions(&mut self) -> RegExpBuilder {
        self.builder.config.is_repetition_converted = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to enable case-insensitive matching of test cases
    /// so that letters match both upper and lower case.
    pub fn withCaseInsensitiveMatching(&mut self) -> RegExpBuilder {
        self.builder.config.is_case_insensitive_matching = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to replace non-capturing groups by capturing ones.
    pub fn withCapturingGroups(&mut self) -> RegExpBuilder {
        self.builder.config.is_capturing_group_enabled = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to convert non-ASCII characters to unicode escape sequences.
    /// The parameter `useSurrogatePairs` specifies whether to convert astral code planes
    /// (range `U+010000` to `U+10FFFF`) to surrogate pairs.
    pub fn withEscapingOfNonAsciiChars(&mut self, useSurrogatePairs: bool) -> RegExpBuilder {
        self.builder.config.is_non_ascii_char_escaped = true;
        self.builder
            .config
            .is_astral_code_point_converted_to_surrogate = useSurrogatePairs;
        self.clone()
    }

    /// Tells `RegExpBuilder` to produce a nicer looking regular expression in verbose mode.
    pub fn withVerboseMode(&mut self) -> RegExpBuilder {
        self.builder.config.is_verbose_mode_enabled = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to remove the caret anchor '^' from the resulting regular
    /// expression, thereby allowing to match the test cases also when they do not occur
    /// at the start of a string.
    pub fn withoutStartAnchor(&mut self) -> RegExpBuilder {
        self.builder.config.is_start_anchor_disabled = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to remove the dollar sign anchor '$' from the resulting regular
    /// expression, thereby allowing to match the test cases also when they do not occur
    /// at the end of a string.
    pub fn withoutEndAnchor(&mut self) -> RegExpBuilder {
        self.builder.config.is_end_anchor_disabled = true;
        self.clone()
    }

    /// Tells `RegExpBuilder` to remove the caret and dollar sign anchors from the resulting
    /// regular expression, thereby allowing to match the test cases also when they occur
    /// within a larger string that contains other content as well.
    pub fn withoutAnchors(&mut self) -> RegExpBuilder {
        self.builder.config.is_start_anchor_disabled = true;
        self.builder.config.is_end_anchor_disabled = true;
        self.clone()
    }

    /// Specifies the minimum quantity of substring repetitions to be converted
    /// if `withConversionOfRepetitions` is set.
    ///
    /// If the quantity is not explicitly set with this method, a default value of 1 will be used.
    ///
    /// ⚠ Throws an error if `quantity` is zero.
    pub fn withMinimumRepetitions(&mut self, quantity: u32) -> Result<RegExpBuilder, JsValue> {
        if quantity < 1 {
            return Err(JsValue::from(MINIMUM_REPETITIONS_MESSAGE));
        }
        self.builder.config.minimum_repetitions = quantity;
        Ok(self.clone())
    }

    /// Specifies the minimum length a repeated substring must have in order to be converted
    /// if `withConversionOfRepetitions` is set.
    ///
    /// If the length is not explicitly set with this method, a default value of 1 will be used.
    ///
    /// ⚠ Throws an error if `length` is zero.
    pub fn withMinimumSubstringLength(&mut self, length: u32) -> Result<RegExpBuilder, JsValue> {
        if length < 1 {
            return Err(JsValue::from(MINIMUM_SUBSTRING_LENGTH_MESSAGE));
        }
        self.builder.config.minimum_substring_length = length;
        Ok(self.clone())
    }

    /// Builds the actual regular expression using the previously given settings.
    pub fn build(&mut self) -> String {
        self.builder.build()
    }
}
```

## File: `src/unicode_tables/decimal.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// DO NOT EDIT THIS FILE. IT WAS AUTOMATICALLY GENERATED BY:
//
//   ucd-generate general-category ucd-16.0.0 --chars --include decimalnumber
//
// Unicode version: 16.0.0.
//
// ucd-generate 0.3.1 is available on crates.io.

pub const DECIMAL_NUMBER: &[(char, char)] = &[
    ('0', '9'),
    ('٠', '٩'),
    ('۰', '۹'),
    ('߀', '߉'),
    ('०', '९'),
    ('০', '৯'),
    ('੦', '੯'),
    ('૦', '૯'),
    ('୦', '୯'),
    ('௦', '௯'),
    ('౦', '౯'),
    ('೦', '೯'),
    ('൦', '൯'),
    ('෦', '෯'),
    ('๐', '๙'),
    ('໐', '໙'),
    ('༠', '༩'),
    ('၀', '၉'),
    ('႐', '႙'),
    ('០', '៩'),
    ('᠐', '᠙'),
    ('᥆', '᥏'),
    ('᧐', '᧙'),
    ('᪀', '᪉'),
    ('᪐', '᪙'),
    ('᭐', '᭙'),
    ('᮰', '᮹'),
    ('᱀', '᱉'),
    ('᱐', '᱙'),
    ('꘠', '꘩'),
    ('꣐', '꣙'),
    ('꤀', '꤉'),
    ('꧐', '꧙'),
    ('꧰', '꧹'),
    ('꩐', '꩙'),
    ('꯰', '꯹'),
    ('０', '９'),
    ('𐒠', '𐒩'),
    ('𐴰', '𐴹'),
    ('𐵀', '𐵉'),
    ('𑁦', '𑁯'),
    ('𑃰', '𑃹'),
    ('𑄶', '𑄿'),
    ('𑇐', '𑇙'),
    ('𑋰', '𑋹'),
    ('𑑐', '𑑙'),
    ('𑓐', '𑓙'),
    ('𑙐', '𑙙'),
    ('𑛀', '𑛉'),
    ('𑛐', '𑛣'),
    ('𑜰', '𑜹'),
    ('𑣠', '𑣩'),
    ('𑥐', '𑥙'),
    ('𑯰', '𑯹'),
    ('𑱐', '𑱙'),
    ('𑵐', '𑵙'),
    ('𑶠', '𑶩'),
    ('𑽐', '𑽙'),
    ('𖄰', '𖄹'),
    ('𖩠', '𖩩'),
    ('𖫀', '𖫉'),
    ('𖭐', '𖭙'),
    ('𖵰', '𖵹'),
    ('𜳰', '𜳹'),
    ('𝟎', '𝟿'),
    ('𞅀', '𞅉'),
    ('𞋰', '𞋹'),
    ('𞓰', '𞓹'),
    ('𞗱', '𞗺'),
    ('𞥐', '𞥙'),
    ('🯰', '🯹'),
];
```

## File: `src/unicode_tables/mod.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

mod decimal;
mod space;
mod word;

pub use decimal::DECIMAL_NUMBER;
pub use space::WHITE_SPACE;
pub use word::WORD;
```

## File: `src/unicode_tables/space.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// DO NOT EDIT THIS FILE. IT WAS AUTOMATICALLY GENERATED BY:
//
//   ucd-generate property-bool ucd-16.0.0 --chars --include whitespace
//
// Unicode version: 16.0.0.
//
// ucd-generate 0.3.1 is available on crates.io.

pub const WHITE_SPACE: &[(char, char)] = &[
    ('\t', '\r'),
    (' ', ' '),
    ('\u{85}', '\u{85}'),
    ('\u{a0}', '\u{a0}'),
    ('\u{1680}', '\u{1680}'),
    ('\u{2000}', '\u{200a}'),
    ('\u{2028}', '\u{2029}'),
    ('\u{202f}', '\u{202f}'),
    ('\u{205f}', '\u{205f}'),
    ('\u{3000}', '\u{3000}'),
];
```

## File: `src/unicode_tables/word.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

// DO NOT EDIT THIS FILE. IT WAS AUTOMATICALLY GENERATED BY:
//
//   ucd-generate perl-word ucd-16.0.0 --chars
//
// Unicode version: 16.0.0.
//
// ucd-generate 0.3.1 is available on crates.io.

pub const WORD: &[(char, char)] = &[
    ('0', '9'),
    ('A', 'Z'),
    ('_', '_'),
    ('a', 'z'),
    ('ª', 'ª'),
    ('µ', 'µ'),
    ('º', 'º'),
    ('À', 'Ö'),
    ('Ø', 'ö'),
    ('ø', 'ˁ'),
    ('ˆ', 'ˑ'),
    ('ˠ', 'ˤ'),
    ('ˬ', 'ˬ'),
    ('ˮ', 'ˮ'),
    ('\u{300}', 'ʹ'),
    ('Ͷ', 'ͷ'),
    ('ͺ', 'ͽ'),
    ('Ϳ', 'Ϳ'),
    ('Ά', 'Ά'),
    ('Έ', 'Ί'),
    ('Ό', 'Ό'),
    ('Ύ', 'Ρ'),
    ('Σ', 'ϵ'),
    ('Ϸ', 'ҁ'),
    ('\u{483}', 'ԯ'),
    ('Ա', 'Ֆ'),
    ('ՙ', 'ՙ'),
    ('ՠ', 'ֈ'),
    ('\u{591}', '\u{5bd}'),
    ('\u{5bf}', '\u{5bf}'),
    ('\u{5c1}', '\u{5c2}'),
    ('\u{5c4}', '\u{5c5}'),
    ('\u{5c7}', '\u{5c7}'),
    ('א', 'ת'),
    ('ׯ', 'ײ'),
    ('\u{610}', '\u{61a}'),
    ('ؠ', '٩'),
    ('ٮ', 'ۓ'),
    ('ە', '\u{6dc}'),
    ('\u{6df}', '\u{6e8}'),
    ('\u{6ea}', 'ۼ'),
    ('ۿ', 'ۿ'),
    ('ܐ', '\u{74a}'),
    ('ݍ', 'ޱ'),
    ('߀', 'ߵ'),
    ('ߺ', 'ߺ'),
    ('\u{7fd}', '\u{7fd}'),
    ('ࠀ', '\u{82d}'),
    ('ࡀ', '\u{85b}'),
    ('ࡠ', 'ࡪ'),
    ('ࡰ', 'ࢇ'),
    ('ࢉ', 'ࢎ'),
    ('\u{897}', '\u{8e1}'),
    ('\u{8e3}', '\u{963}'),
    ('०', '९'),
    ('ॱ', 'ঃ'),
    ('অ', 'ঌ'),
    ('এ', 'ঐ'),
    ('ও', 'ন'),
    ('প', 'র'),
    ('ল', 'ল'),
    ('শ', 'হ'),
    ('\u{9bc}', '\u{9c4}'),
    ('ে', 'ৈ'),
    ('ো', 'ৎ'),
    ('\u{9d7}', '\u{9d7}'),
    ('ড়', 'ঢ়'),
    ('য়', '\u{9e3}'),
    ('০', 'ৱ'),
    ('ৼ', 'ৼ'),
    ('\u{9fe}', '\u{9fe}'),
    ('\u{a01}', 'ਃ'),
    ('ਅ', 'ਊ'),
    ('ਏ', 'ਐ'),
    ('ਓ', 'ਨ'),
    ('ਪ', 'ਰ'),
    ('ਲ', 'ਲ਼'),
    ('ਵ', 'ਸ਼'),
    ('ਸ', 'ਹ'),
    ('\u{a3c}', '\u{a3c}'),
    ('ਾ', '\u{a42}'),
    ('\u{a47}', '\u{a48}'),
    ('\u{a4b}', '\u{a4d}'),
    ('\u{a51}', '\u{a51}'),
    ('ਖ਼', 'ੜ'),
    ('ਫ਼', 'ਫ਼'),
    ('੦', '\u{a75}'),
    ('\u{a81}', 'ઃ'),
    ('અ', 'ઍ'),
    ('એ', 'ઑ'),
    ('ઓ', 'ન'),
    ('પ', 'ર'),
    ('લ', 'ળ'),
    ('વ', 'હ'),
    ('\u{abc}', '\u{ac5}'),
    ('\u{ac7}', 'ૉ'),
    ('ો', '\u{acd}'),
    ('ૐ', 'ૐ'),
    ('ૠ', '\u{ae3}'),
    ('૦', '૯'),
    ('ૹ', '\u{aff}'),
    ('\u{b01}', 'ଃ'),
    ('ଅ', 'ଌ'),
    ('ଏ', 'ଐ'),
    ('ଓ', 'ନ'),
    ('ପ', 'ର'),
    ('ଲ', 'ଳ'),
    ('ଵ', 'ହ'),
    ('\u{b3c}', '\u{b44}'),
    ('େ', 'ୈ'),
    ('ୋ', '\u{b4d}'),
    ('\u{b55}', '\u{b57}'),
    ('ଡ଼', 'ଢ଼'),
    ('ୟ', '\u{b63}'),
    ('୦', '୯'),
    ('ୱ', 'ୱ'),
    ('\u{b82}', 'ஃ'),
    ('அ', 'ஊ'),
    ('எ', 'ஐ'),
    ('ஒ', 'க'),
    ('ங', 'ச'),
    ('ஜ', 'ஜ'),
    ('ஞ', 'ட'),
    ('ண', 'த'),
    ('ந', 'ப'),
    ('ம', 'ஹ'),
    ('\u{bbe}', 'ூ'),
    ('ெ', 'ை'),
    ('ொ', '\u{bcd}'),
    ('ௐ', 'ௐ'),
    ('\u{bd7}', '\u{bd7}'),
    ('௦', '௯'),
    ('\u{c00}', 'ఌ'),
    ('ఎ', 'ఐ'),
    ('ఒ', 'న'),
    ('ప', 'హ'),
    ('\u{c3c}', 'ౄ'),
    ('\u{c46}', '\u{c48}'),
    ('\u{c4a}', '\u{c4d}'),
    ('\u{c55}', '\u{c56}'),
    ('ౘ', 'ౚ'),
    ('ౝ', 'ౝ'),
    ('ౠ', '\u{c63}'),
    ('౦', '౯'),
    ('ಀ', 'ಃ'),
    ('ಅ', 'ಌ'),
    ('ಎ', 'ಐ'),
    ('ಒ', 'ನ'),
    ('ಪ', 'ಳ'),
    ('ವ', 'ಹ'),
    ('\u{cbc}', 'ೄ'),
    ('\u{cc6}', '\u{cc8}'),
    ('\u{cca}', '\u{ccd}'),
    ('\u{cd5}', '\u{cd6}'),
    ('ೝ', 'ೞ'),
    ('ೠ', '\u{ce3}'),
    ('೦', '೯'),
    ('ೱ', 'ೳ'),
    ('\u{d00}', 'ഌ'),
    ('എ', 'ഐ'),
    ('ഒ', '\u{d44}'),
    ('െ', 'ൈ'),
    ('ൊ', 'ൎ'),
    ('ൔ', '\u{d57}'),
    ('ൟ', '\u{d63}'),
    ('൦', '൯'),
    ('ൺ', 'ൿ'),
    ('\u{d81}', 'ඃ'),
    ('අ', 'ඖ'),
    ('ක', 'න'),
    ('ඳ', 'ර'),
    ('ල', 'ල'),
    ('ව', 'ෆ'),
    ('\u{dca}', '\u{dca}'),
    ('\u{dcf}', '\u{dd4}'),
    ('\u{dd6}', '\u{dd6}'),
    ('ෘ', '\u{ddf}'),
    ('෦', '෯'),
    ('ෲ', 'ෳ'),
    ('ก', '\u{e3a}'),
    ('เ', '\u{e4e}'),
    ('๐', '๙'),
    ('ກ', 'ຂ'),
    ('ຄ', 'ຄ'),
    ('ຆ', 'ຊ'),
    ('ຌ', 'ຣ'),
    ('ລ', 'ລ'),
    ('ວ', 'ຽ'),
    ('ເ', 'ໄ'),
    ('ໆ', 'ໆ'),
    ('\u{ec8}', '\u{ece}'),
    ('໐', '໙'),
    ('ໜ', 'ໟ'),
    ('ༀ', 'ༀ'),
    ('\u{f18}', '\u{f19}'),
    ('༠', '༩'),
    ('\u{f35}', '\u{f35}'),
    ('\u{f37}', '\u{f37}'),
    ('\u{f39}', '\u{f39}'),
    ('༾', 'ཇ'),
    ('ཉ', 'ཬ'),
    ('\u{f71}', '\u{f84}'),
    ('\u{f86}', '\u{f97}'),
    ('\u{f99}', '\u{fbc}'),
    ('\u{fc6}', '\u{fc6}'),
    ('က', '၉'),
    ('ၐ', '\u{109d}'),
    ('Ⴀ', 'Ⴥ'),
    ('Ⴧ', 'Ⴧ'),
    ('Ⴭ', 'Ⴭ'),
    ('ა', 'ჺ'),
    ('ჼ', 'ቈ'),
    ('ቊ', 'ቍ'),
    ('ቐ', 'ቖ'),
    ('ቘ', 'ቘ'),
    ('ቚ', 'ቝ'),
    ('በ', 'ኈ'),
    ('ኊ', 'ኍ'),
    ('ነ', 'ኰ'),
    ('ኲ', 'ኵ'),
    ('ኸ', 'ኾ'),
    ('ዀ', 'ዀ'),
    ('ዂ', 'ዅ'),
    ('ወ', 'ዖ'),
    ('ዘ', 'ጐ'),
    ('ጒ', 'ጕ'),
    ('ጘ', 'ፚ'),
    ('\u{135d}', '\u{135f}'),
    ('ᎀ', 'ᎏ'),
    ('Ꭰ', 'Ᏽ'),
    ('ᏸ', 'ᏽ'),
    ('ᐁ', 'ᙬ'),
    ('ᙯ', 'ᙿ'),
    ('ᚁ', 'ᚚ'),
    ('ᚠ', 'ᛪ'),
    ('ᛮ', 'ᛸ'),
    ('ᜀ', '\u{1715}'),
    ('ᜟ', '\u{1734}'),
    ('ᝀ', '\u{1753}'),
    ('ᝠ', 'ᝬ'),
    ('ᝮ', 'ᝰ'),
    ('\u{1772}', '\u{1773}'),
    ('ក', '\u{17d3}'),
    ('ៗ', 'ៗ'),
    ('ៜ', '\u{17dd}'),
    ('០', '៩'),
    ('\u{180b}', '\u{180d}'),
    ('\u{180f}', '᠙'),
    ('ᠠ', 'ᡸ'),
    ('ᢀ', 'ᢪ'),
    ('ᢰ', 'ᣵ'),
    ('ᤀ', 'ᤞ'),
    ('\u{1920}', 'ᤫ'),
    ('ᤰ', '\u{193b}'),
    ('᥆', 'ᥭ'),
    ('ᥰ', 'ᥴ'),
    ('ᦀ', 'ᦫ'),
    ('ᦰ', 'ᧉ'),
    ('᧐', '᧙'),
    ('ᨀ', '\u{1a1b}'),
    ('ᨠ', '\u{1a5e}'),
    ('\u{1a60}', '\u{1a7c}'),
    ('\u{1a7f}', '᪉'),
    ('᪐', '᪙'),
    ('ᪧ', 'ᪧ'),
    ('\u{1ab0}', '\u{1ace}'),
    ('\u{1b00}', 'ᭌ'),
    ('᭐', '᭙'),
    ('\u{1b6b}', '\u{1b73}'),
    ('\u{1b80}', '\u{1bf3}'),
    ('ᰀ', '\u{1c37}'),
    ('᱀', '᱉'),
    ('ᱍ', 'ᱽ'),
    ('ᲀ', 'ᲊ'),
    ('Ა', 'Ჺ'),
    ('Ჽ', 'Ჿ'),
    ('\u{1cd0}', '\u{1cd2}'),
    ('\u{1cd4}', 'ᳺ'),
    ('ᴀ', 'ἕ'),
    ('Ἐ', 'Ἕ'),
    ('ἠ', 'ὅ'),
    ('Ὀ', 'Ὅ'),
    ('ὐ', 'ὗ'),
    ('Ὑ', 'Ὑ'),
    ('Ὓ', 'Ὓ'),
    ('Ὕ', 'Ὕ'),
    ('Ὗ', 'ώ'),
    ('ᾀ', 'ᾴ'),
    ('ᾶ', 'ᾼ'),
    ('ι', 'ι'),
    ('ῂ', 'ῄ'),
    ('ῆ', 'ῌ'),
    ('ῐ', 'ΐ'),
    ('ῖ', 'Ί'),
    ('ῠ', 'Ῥ'),
    ('ῲ', 'ῴ'),
    ('ῶ', 'ῼ'),
    ('\u{200c}', '\u{200d}'),
    ('‿', '⁀'),
    ('⁔', '⁔'),
    ('ⁱ', 'ⁱ'),
    ('ⁿ', 'ⁿ'),
    ('ₐ', 'ₜ'),
    ('\u{20d0}', '\u{20f0}'),
    ('ℂ', 'ℂ'),
    ('ℇ', 'ℇ'),
    ('ℊ', 'ℓ'),
    ('ℕ', 'ℕ'),
    ('ℙ', 'ℝ'),
    ('ℤ', 'ℤ'),
    ('Ω', 'Ω'),
    ('ℨ', 'ℨ'),
    ('K', 'ℭ'),
    ('ℯ', 'ℹ'),
    ('ℼ', 'ℿ'),
    ('ⅅ', 'ⅉ'),
    ('ⅎ', 'ⅎ'),
    ('Ⅰ', 'ↈ'),
    ('Ⓐ', 'ⓩ'),
    ('Ⰰ', 'ⳤ'),
    ('Ⳬ', 'ⳳ'),
    ('ⴀ', 'ⴥ'),
    ('ⴧ', 'ⴧ'),
    ('ⴭ', 'ⴭ'),
    ('ⴰ', 'ⵧ'),
    ('ⵯ', 'ⵯ'),
    ('\u{2d7f}', 'ⶖ'),
    ('ⶠ', 'ⶦ'),
    ('ⶨ', 'ⶮ'),
    ('ⶰ', 'ⶶ'),
    ('ⶸ', 'ⶾ'),
    ('ⷀ', 'ⷆ'),
    ('ⷈ', 'ⷎ'),
    ('ⷐ', 'ⷖ'),
    ('ⷘ', 'ⷞ'),
    ('\u{2de0}', '\u{2dff}'),
    ('ⸯ', 'ⸯ'),
    ('々', '〇'),
    ('〡', '\u{302f}'),
    ('〱', '〵'),
    ('〸', '〼'),
    ('ぁ', 'ゖ'),
    ('\u{3099}', '\u{309a}'),
    ('ゝ', 'ゟ'),
    ('ァ', 'ヺ'),
    ('ー', 'ヿ'),
    ('ㄅ', 'ㄯ'),
    ('ㄱ', 'ㆎ'),
    ('ㆠ', 'ㆿ'),
    ('ㇰ', 'ㇿ'),
    ('㐀', '䶿'),
    ('一', 'ꒌ'),
    ('ꓐ', 'ꓽ'),
    ('ꔀ', 'ꘌ'),
    ('ꘐ', 'ꘫ'),
    ('Ꙁ', '\u{a672}'),
    ('\u{a674}', '\u{a67d}'),
    ('ꙿ', '\u{a6f1}'),
    ('ꜗ', 'ꜟ'),
    ('Ꜣ', 'ꞈ'),
    ('Ꞌ', 'ꟍ'),
    ('Ꟑ', 'ꟑ'),
    ('ꟓ', 'ꟓ'),
    ('ꟕ', 'Ƛ'),
    ('ꟲ', 'ꠧ'),
    ('\u{a82c}', '\u{a82c}'),
    ('ꡀ', 'ꡳ'),
    ('ꢀ', '\u{a8c5}'),
    ('꣐', '꣙'),
    ('\u{a8e0}', 'ꣷ'),
    ('ꣻ', 'ꣻ'),
    ('ꣽ', '\u{a92d}'),
    ('ꤰ', '\u{a953}'),
    ('ꥠ', 'ꥼ'),
    ('\u{a980}', '\u{a9c0}'),
    ('ꧏ', '꧙'),
    ('ꧠ', 'ꧾ'),
    ('ꨀ', '\u{aa36}'),
    ('ꩀ', 'ꩍ'),
    ('꩐', '꩙'),
    ('ꩠ', 'ꩶ'),
    ('ꩺ', 'ꫂ'),
    ('ꫛ', 'ꫝ'),
    ('ꫠ', 'ꫯ'),
    ('ꫲ', '\u{aaf6}'),
    ('ꬁ', 'ꬆ'),
    ('ꬉ', 'ꬎ'),
    ('ꬑ', 'ꬖ'),
    ('ꬠ', 'ꬦ'),
    ('ꬨ', 'ꬮ'),
    ('ꬰ', 'ꭚ'),
    ('ꭜ', 'ꭩ'),
    ('ꭰ', 'ꯪ'),
    ('꯬', '\u{abed}'),
    ('꯰', '꯹'),
    ('가', '힣'),
    ('ힰ', 'ퟆ'),
    ('ퟋ', 'ퟻ'),
    ('豈', '舘'),
    ('並', '龎'),
    ('ﬀ', 'ﬆ'),
    ('ﬓ', 'ﬗ'),
    ('יִ', 'ﬨ'),
    ('שׁ', 'זּ'),
    ('טּ', 'לּ'),
    ('מּ', 'מּ'),
    ('נּ', 'סּ'),
    ('ףּ', 'פּ'),
    ('צּ', 'ﮱ'),
    ('ﯓ', 'ﴽ'),
    ('ﵐ', 'ﶏ'),
    ('ﶒ', 'ﷇ'),
    ('ﷰ', 'ﷻ'),
    ('\u{fe00}', '\u{fe0f}'),
    ('\u{fe20}', '\u{fe2f}'),
    ('︳', '︴'),
    ('﹍', '﹏'),
    ('ﹰ', 'ﹴ'),
    ('ﹶ', 'ﻼ'),
    ('０', '９'),
    ('Ａ', 'Ｚ'),
    ('＿', '＿'),
    ('ａ', 'ｚ'),
    ('ｦ', 'ﾾ'),
    ('ￂ', 'ￇ'),
    ('ￊ', 'ￏ'),
    ('ￒ', 'ￗ'),
    ('ￚ', 'ￜ'),
    ('𐀀', '𐀋'),
    ('𐀍', '𐀦'),
    ('𐀨', '𐀺'),
    ('𐀼', '𐀽'),
    ('𐀿', '𐁍'),
    ('𐁐', '𐁝'),
    ('𐂀', '𐃺'),
    ('𐅀', '𐅴'),
    ('\u{101fd}', '\u{101fd}'),
    ('𐊀', '𐊜'),
    ('𐊠', '𐋐'),
    ('\u{102e0}', '\u{102e0}'),
    ('𐌀', '𐌟'),
    ('𐌭', '𐍊'),
    ('𐍐', '\u{1037a}'),
    ('𐎀', '𐎝'),
    ('𐎠', '𐏃'),
    ('𐏈', '𐏏'),
    ('𐏑', '𐏕'),
    ('𐐀', '𐒝'),
    ('𐒠', '𐒩'),
    ('𐒰', '𐓓'),
    ('𐓘', '𐓻'),
    ('𐔀', '𐔧'),
    ('𐔰', '𐕣'),
    ('𐕰', '𐕺'),
    ('𐕼', '𐖊'),
    ('𐖌', '𐖒'),
    ('𐖔', '𐖕'),
    ('𐖗', '𐖡'),
    ('𐖣', '𐖱'),
    ('𐖳', '𐖹'),
    ('𐖻', '𐖼'),
    ('𐗀', '𐗳'),
    ('𐘀', '𐜶'),
    ('𐝀', '𐝕'),
    ('𐝠', '𐝧'),
    ('𐞀', '𐞅'),
    ('𐞇', '𐞰'),
    ('𐞲', '𐞺'),
    ('𐠀', '𐠅'),
    ('𐠈', '𐠈'),
    ('𐠊', '𐠵'),
    ('𐠷', '𐠸'),
    ('𐠼', '𐠼'),
    ('𐠿', '𐡕'),
    ('𐡠', '𐡶'),
    ('𐢀', '𐢞'),
    ('𐣠', '𐣲'),
    ('𐣴', '𐣵'),
    ('𐤀', '𐤕'),
    ('𐤠', '𐤹'),
    ('𐦀', '𐦷'),
    ('𐦾', '𐦿'),
    ('𐨀', '\u{10a03}'),
    ('\u{10a05}', '\u{10a06}'),
    ('\u{10a0c}', '𐨓'),
    ('𐨕', '𐨗'),
    ('𐨙', '𐨵'),
    ('\u{10a38}', '\u{10a3a}'),
    ('\u{10a3f}', '\u{10a3f}'),
    ('𐩠', '𐩼'),
    ('𐪀', '𐪜'),
    ('𐫀', '𐫇'),
    ('𐫉', '\u{10ae6}'),
    ('𐬀', '𐬵'),
    ('𐭀', '𐭕'),
    ('𐭠', '𐭲'),
    ('𐮀', '𐮑'),
    ('𐰀', '𐱈'),
    ('𐲀', '𐲲'),
    ('𐳀', '𐳲'),
    ('𐴀', '\u{10d27}'),
    ('𐴰', '𐴹'),
    ('𐵀', '𐵥'),
    ('\u{10d69}', '\u{10d6d}'),
    ('𐵯', '𐶅'),
    ('𐺀', '𐺩'),
    ('\u{10eab}', '\u{10eac}'),
    ('𐺰', '𐺱'),
    ('𐻂', '𐻄'),
    ('\u{10efc}', '𐼜'),
    ('𐼧', '𐼧'),
    ('𐼰', '\u{10f50}'),
    ('𐽰', '\u{10f85}'),
    ('𐾰', '𐿄'),
    ('𐿠', '𐿶'),
    ('𑀀', '\u{11046}'),
    ('𑁦', '𑁵'),
    ('\u{1107f}', '\u{110ba}'),
    ('\u{110c2}', '\u{110c2}'),
    ('𑃐', '𑃨'),
    ('𑃰', '𑃹'),
    ('\u{11100}', '\u{11134}'),
    ('𑄶', '𑄿'),
    ('𑅄', '𑅇'),
    ('𑅐', '\u{11173}'),
    ('𑅶', '𑅶'),
    ('\u{11180}', '𑇄'),
    ('\u{111c9}', '\u{111cc}'),
    ('𑇎', '𑇚'),
    ('𑇜', '𑇜'),
    ('𑈀', '𑈑'),
    ('𑈓', '\u{11237}'),
    ('\u{1123e}', '\u{11241}'),
    ('𑊀', '𑊆'),
    ('𑊈', '𑊈'),
    ('𑊊', '𑊍'),
    ('𑊏', '𑊝'),
    ('𑊟', '𑊨'),
    ('𑊰', '\u{112ea}'),
    ('𑋰', '𑋹'),
    ('\u{11300}', '𑌃'),
    ('𑌅', '𑌌'),
    ('𑌏', '𑌐'),
    ('𑌓', '𑌨'),
    ('𑌪', '𑌰'),
    ('𑌲', '𑌳'),
    ('𑌵', '𑌹'),
    ('\u{1133b}', '𑍄'),
    ('𑍇', '𑍈'),
    ('𑍋', '\u{1134d}'),
    ('𑍐', '𑍐'),
    ('\u{11357}', '\u{11357}'),
    ('𑍝', '𑍣'),
    ('\u{11366}', '\u{1136c}'),
    ('\u{11370}', '\u{11374}'),
    ('𑎀', '𑎉'),
    ('𑎋', '𑎋'),
    ('𑎎', '𑎎'),
    ('𑎐', '𑎵'),
    ('𑎷', '\u{113c0}'),
    ('\u{113c2}', '\u{113c2}'),
    ('\u{113c5}', '\u{113c5}'),
    ('\u{113c7}', '𑏊'),
    ('𑏌', '𑏓'),
    ('\u{113e1}', '\u{113e2}'),
    ('𑐀', '𑑊'),
    ('𑑐', '𑑙'),
    ('\u{1145e}', '𑑡'),
    ('𑒀', '𑓅'),
    ('𑓇', '𑓇'),
    ('𑓐', '𑓙'),
    ('𑖀', '\u{115b5}'),
    ('𑖸', '\u{115c0}'),
    ('𑗘', '\u{115dd}'),
    ('𑘀', '\u{11640}'),
    ('𑙄', '𑙄'),
    ('𑙐', '𑙙'),
    ('𑚀', '𑚸'),
    ('𑛀', '𑛉'),
    ('𑛐', '𑛣'),
    ('𑜀', '𑜚'),
    ('\u{1171d}', '\u{1172b}'),
    ('𑜰', '𑜹'),
    ('𑝀', '𑝆'),
    ('𑠀', '\u{1183a}'),
    ('𑢠', '𑣩'),
    ('𑣿', '𑤆'),
    ('𑤉', '𑤉'),
    ('𑤌', '𑤓'),
    ('𑤕', '𑤖'),
    ('𑤘', '𑤵'),
    ('𑤷', '𑤸'),
    ('\u{1193b}', '\u{11943}'),
    ('𑥐', '𑥙'),
    ('𑦠', '𑦧'),
    ('𑦪', '\u{119d7}'),
    ('\u{119da}', '𑧡'),
    ('𑧣', '𑧤'),
    ('𑨀', '\u{11a3e}'),
    ('\u{11a47}', '\u{11a47}'),
    ('𑩐', '\u{11a99}'),
    ('𑪝', '𑪝'),
    ('𑪰', '𑫸'),
    ('𑯀', '𑯠'),
    ('𑯰', '𑯹'),
    ('𑰀', '𑰈'),
    ('𑰊', '\u{11c36}'),
    ('\u{11c38}', '𑱀'),
    ('𑱐', '𑱙'),
    ('𑱲', '𑲏'),
    ('\u{11c92}', '\u{11ca7}'),
    ('𑲩', '\u{11cb6}'),
    ('𑴀', '𑴆'),
    ('𑴈', '𑴉'),
    ('𑴋', '\u{11d36}'),
    ('\u{11d3a}', '\u{11d3a}'),
    ('\u{11d3c}', '\u{11d3d}'),
    ('\u{11d3f}', '\u{11d47}'),
    ('𑵐', '𑵙'),
    ('𑵠', '𑵥'),
    ('𑵧', '𑵨'),
    ('𑵪', '𑶎'),
    ('\u{11d90}', '\u{11d91}'),
    ('𑶓', '𑶘'),
    ('𑶠', '𑶩'),
    ('𑻠', '𑻶'),
    ('\u{11f00}', '𑼐'),
    ('𑼒', '\u{11f3a}'),
    ('𑼾', '\u{11f42}'),
    ('𑽐', '\u{11f5a}'),
    ('𑾰', '𑾰'),
    ('𒀀', '𒎙'),
    ('𒐀', '𒑮'),
    ('𒒀', '𒕃'),
    ('𒾐', '𒿰'),
    ('𓀀', '𓐯'),
    ('\u{13440}', '\u{13455}'),
    ('𓑠', '𔏺'),
    ('𔐀', '𔙆'),
    ('𖄀', '𖄹'),
    ('𖠀', '𖨸'),
    ('𖩀', '𖩞'),
    ('𖩠', '𖩩'),
    ('𖩰', '𖪾'),
    ('𖫀', '𖫉'),
    ('𖫐', '𖫭'),
    ('\u{16af0}', '\u{16af4}'),
    ('𖬀', '\u{16b36}'),
    ('𖭀', '𖭃'),
    ('𖭐', '𖭙'),
    ('𖭣', '𖭷'),
    ('𖭽', '𖮏'),
    ('𖵀', '𖵬'),
    ('𖵰', '𖵹'),
    ('𖹀', '𖹿'),
    ('𖼀', '𖽊'),
    ('\u{16f4f}', '𖾇'),
    ('\u{16f8f}', '𖾟'),
    ('𖿠', '𖿡'),
    ('𖿣', '\u{16fe4}'),
    ('\u{16ff0}', '\u{16ff1}'),
    ('𗀀', '𘟷'),
    ('𘠀', '𘳕'),
    ('𘳿', '𘴈'),
    ('𚿰', '𚿳'),
    ('𚿵', '𚿻'),
    ('𚿽', '𚿾'),
    ('𛀀', '𛄢'),
    ('𛄲', '𛄲'),
    ('𛅐', '𛅒'),
    ('𛅕', '𛅕'),
    ('𛅤', '𛅧'),
    ('𛅰', '𛋻'),
    ('𛰀', '𛱪'),
    ('𛱰', '𛱼'),
    ('𛲀', '𛲈'),
    ('𛲐', '𛲙'),
    ('\u{1bc9d}', '\u{1bc9e}'),
    ('𜳰', '𜳹'),
    ('\u{1cf00}', '\u{1cf2d}'),
    ('\u{1cf30}', '\u{1cf46}'),
    ('\u{1d165}', '\u{1d169}'),
    ('\u{1d16d}', '\u{1d172}'),
    ('\u{1d17b}', '\u{1d182}'),
    ('\u{1d185}', '\u{1d18b}'),
    ('\u{1d1aa}', '\u{1d1ad}'),
    ('\u{1d242}', '\u{1d244}'),
    ('𝐀', '𝑔'),
    ('𝑖', '𝒜'),
    ('𝒞', '𝒟'),
    ('𝒢', '𝒢'),
    ('𝒥', '𝒦'),
    ('𝒩', '𝒬'),
    ('𝒮', '𝒹'),
    ('𝒻', '𝒻'),
    ('𝒽', '𝓃'),
    ('𝓅', '𝔅'),
    ('𝔇', '𝔊'),
    ('𝔍', '𝔔'),
    ('𝔖', '𝔜'),
    ('𝔞', '𝔹'),
    ('𝔻', '𝔾'),
    ('𝕀', '𝕄'),
    ('𝕆', '𝕆'),
    ('𝕊', '𝕐'),
    ('𝕒', '𝚥'),
    ('𝚨', '𝛀'),
    ('𝛂', '𝛚'),
    ('𝛜', '𝛺'),
    ('𝛼', '𝜔'),
    ('𝜖', '𝜴'),
    ('𝜶', '𝝎'),
    ('𝝐', '𝝮'),
    ('𝝰', '𝞈'),
    ('𝞊', '𝞨'),
    ('𝞪', '𝟂'),
    ('𝟄', '𝟋'),
    ('𝟎', '𝟿'),
    ('\u{1da00}', '\u{1da36}'),
    ('\u{1da3b}', '\u{1da6c}'),
    ('\u{1da75}', '\u{1da75}'),
    ('\u{1da84}', '\u{1da84}'),
    ('\u{1da9b}', '\u{1da9f}'),
    ('\u{1daa1}', '\u{1daaf}'),
    ('𝼀', '𝼞'),
    ('𝼥', '𝼪'),
    ('\u{1e000}', '\u{1e006}'),
    ('\u{1e008}', '\u{1e018}'),
    ('\u{1e01b}', '\u{1e021}'),
    ('\u{1e023}', '\u{1e024}'),
    ('\u{1e026}', '\u{1e02a}'),
    ('𞀰', '𞁭'),
    ('\u{1e08f}', '\u{1e08f}'),
    ('𞄀', '𞄬'),
    ('\u{1e130}', '𞄽'),
    ('𞅀', '𞅉'),
    ('𞅎', '𞅎'),
    ('𞊐', '\u{1e2ae}'),
    ('𞋀', '𞋹'),
    ('𞓐', '𞓹'),
    ('𞗐', '𞗺'),
    ('𞟠', '𞟦'),
    ('𞟨', '𞟫'),
    ('𞟭', '𞟮'),
    ('𞟰', '𞟾'),
    ('𞠀', '𞣄'),
    ('\u{1e8d0}', '\u{1e8d6}'),
    ('𞤀', '𞥋'),
    ('𞥐', '𞥙'),
    ('𞸀', '𞸃'),
    ('𞸅', '𞸟'),
    ('𞸡', '𞸢'),
    ('𞸤', '𞸤'),
    ('𞸧', '𞸧'),
    ('𞸩', '𞸲'),
    ('𞸴', '𞸷'),
    ('𞸹', '𞸹'),
    ('𞸻', '𞸻'),
    ('𞹂', '𞹂'),
    ('𞹇', '𞹇'),
    ('𞹉', '𞹉'),
    ('𞹋', '𞹋'),
    ('𞹍', '𞹏'),
    ('𞹑', '𞹒'),
    ('𞹔', '𞹔'),
    ('𞹗', '𞹗'),
    ('𞹙', '𞹙'),
    ('𞹛', '𞹛'),
    ('𞹝', '𞹝'),
    ('𞹟', '𞹟'),
    ('𞹡', '𞹢'),
    ('𞹤', '𞹤'),
    ('𞹧', '𞹪'),
    ('𞹬', '𞹲'),
    ('𞹴', '𞹷'),
    ('𞹹', '𞹼'),
    ('𞹾', '𞹾'),
    ('𞺀', '𞺉'),
    ('𞺋', '𞺛'),
    ('𞺡', '𞺣'),
    ('𞺥', '𞺩'),
    ('𞺫', '𞺻'),
    ('🄰', '🅉'),
    ('🅐', '🅩'),
    ('🅰', '🆉'),
    ('🯰', '🯹'),
    ('𠀀', '𪛟'),
    ('𪜀', '𫜹'),
    ('𫝀', '𫠝'),
    ('𫠠', '𬺡'),
    ('𬺰', '𮯠'),
    ('𮯰', '𮹝'),
    ('丽', '𪘀'),
    ('𰀀', '𱍊'),
    ('𱍐', '𲎯'),
    ('\u{e0100}', '\u{e01ef}'),
];
```

## File: `tests/cli_integration_tests.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#![cfg(not(target_family = "wasm"))]

use assert_cmd::{cargo_bin, Command};
use indoc::indoc;
use predicates::prelude::*;
use std::io::Write;
use tempfile::NamedTempFile;

const TEST_CASE: &str = "I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩.";

mod no_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&[TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩\\.$\n"));
        }

        #[test]
        fn succeeds_with_ignore_case_option() {
            let mut grex = init_command();
            grex.args(&["--ignore-case", "Ä@Ö€Ü", "ä@ö€ü", "Ä@ö€Ü", "ä@Ö€ü"]);
            grex.assert()
                .success()
                .stdout(predicate::eq("(?i)^ä@ö€ü$\n"));
        }

        #[test]
        fn succeeds_with_leading_hyphen() {
            let mut grex = init_command();
            grex.args(&["-a", "b", "c"]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^(?:\\-a|[bc])$\n"));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I   \\u{2665}\\u{2665}\\u{2665} 36 and \\u{663} and y\\u{306}y\\u{306} and \\u{1f4a9}\\u{1f4a9}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I   \\u{2665}\\u{2665}\\u{2665} 36 and \\u{663} and y\\u{306}y\\u{306} and \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ \ \ ♥♥♥\ 36\ and\ ٣\ and\ y̆y̆\ and\ 💩💩\.
                $
                "#,
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ \ \ \u{2665}\u{2665}\u{2665}\ 36\ and\ \u{663}\ and\ y\u{306}y\u{306}\ and\ \u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--escape", "--with-surrogates", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ \ \ \u{2665}\u{2665}\u{2665}\ 36\ and\ \u{663}\ and\ y\u{306}y\u{306}\ and\ \u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_file_input() {
            let mut file = NamedTempFile::new().unwrap();
            writeln!(file, "a\nb\\n\n\nc\näöü\n♥").unwrap();

            let mut grex = init_command();
            grex.args(&["-f", file.path().to_str().unwrap()]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^(?:b\\\\n|äöü|[ac♥])$\n"));
        }

        #[test]
        fn succeeds_with_test_cases_from_stdin() {
            let mut grex = init_command();
            grex.write_stdin("a\nb\\n\n\nc\näöü\n♥")
                .arg("-")
                .assert()
                .stdout(predicate::eq("^(?:b\\\\n|äöü|[ac♥])$\n"));
        }

        #[test]
        fn succeeds_with_file_from_stdin() {
            let mut file = NamedTempFile::new().unwrap();
            writeln!(file, "a\nb\\n\n\nc\näöü\n♥").unwrap();

            let mut grex = init_command();
            grex.write_stdin(file.path().to_str().unwrap())
                .args(&["-f", "-"])
                .assert()
                .stdout(predicate::eq("^(?:b\\\\n|äöü|[ac♥])$\n"));
        }

        #[test]
        fn fails_with_surrogate_but_without_escape_option() {
            let mut grex = init_command();
            grex.args(&["--with-surrogates", TEST_CASE]);
            grex.assert().failure().stderr(predicate::str::contains(
                "required arguments were not provided",
            ));
        }

        #[test]
        fn fails_without_arguments() {
            let mut grex = init_command();
            grex.assert().failure().stderr(predicate::str::contains(
                "required arguments were not provided",
            ));
        }

        #[test]
        fn fails_when_file_name_is_not_provided() {
            let mut grex = init_command();
            grex.arg("-f");
            grex.assert().failure().stderr(predicate::str::contains(
                "a value is required for '--file <FILE>' but none was supplied",
            ));
        }

        #[test]
        fn fails_when_file_does_not_exist() {
            let mut grex = init_command();
            grex.args(&["-f", "/path/to/non-existing/file"]);
            grex.assert()
                .failure()
                .stdout(predicate::str::is_empty())
                .stderr(predicate::eq(
                    "error: the specified file could not be found\n",
                ));
        }

        #[test]
        fn fails_with_first_file_input_and_then_direct_input() {
            let mut grex = init_command();
            grex.args(&["-f", "/path/to/some/file", TEST_CASE]);
            grex.assert().failure().stderr(predicate::str::contains(
                "the argument '--file <FILE>' cannot be used with '[INPUT]...'",
            ));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I {3}♥{3} 36 and ٣ and (?:y̆){2} and 💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_ignore_case_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--ignore-case", "ÄÖÜäöü@Ö€", "äöüÄöÜ@ö€"]);
            grex.assert()
                .success()
                .stdout(predicate::eq("(?i)^(?:äöü){2}@ö€$\n"));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I {3}\\u{2665}{3} 36 and \\u{663} and (?:y\\u{306}){2} and \\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I {3}\\u{2665}{3} 36 and \\u{663} and (?:y\\u{306}){2} and (?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ {3}♥{3}\ 36\ and\ ٣\ and\ 
                  (?:
                    y̆
                  ){2}
                  \ and\ 💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ {3}\u{2665}{3}\ 36\ and\ \u{663}\ and\ 
                  (?:
                    y\u{306}
                  ){2}
                  \ and\ \u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ {3}\u{2665}{3}\ 36\ and\ \u{663}\ and\ 
                  (?:
                    y\u{306}
                  ){2}
                  \ and\ 
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_increased_minimum_repetitions() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--min-repetitions", "2", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^I {3}♥{3} 36 and ٣ and y̆y̆ and 💩💩\\.$\n"));
        }

        #[test]
        fn succeeds_with_increased_minimum_substring_length() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--min-substring-length", "2", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I   ♥♥♥ 36 and ٣ and (?:y̆){2} and 💩💩\\.$\n",
            ));
        }

        #[test]
        fn fails_with_minimum_repetitions_equal_to_zero() {
            let mut grex = init_command();
            grex.args(&["--min-repetitions", "0", TEST_CASE]);
            grex.assert()
                .failure()
                .stderr(predicate::str::contains("Value must not be zero"));
        }

        #[test]
        fn fails_with_minimum_repetitions_equal_to_invalid_value() {
            let mut grex = init_command();
            grex.args(&["--min-repetitions", "§!$", TEST_CASE]);
            grex.assert().failure().stderr(predicate::str::contains(
                "Value is not a valid unsigned integer",
            ));
        }

        #[test]
        fn fails_with_minimum_substring_length_equal_to_zero() {
            let mut grex = init_command();
            grex.args(&["--min-substring-length", "0", TEST_CASE]);
            grex.assert()
                .failure()
                .stderr(predicate::str::contains("Value must not be zero"));
        }

        #[test]
        fn fails_with_minimum_substring_length_equal_to_invalid_value() {
            let mut grex = init_command();
            grex.args(&["--min-substring-length", "§!$", TEST_CASE]);
            grex.assert().failure().stderr(predicate::str::contains(
                "Value is not a valid unsigned integer",
            ));
        }
    }
}

mod digit_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--digits", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I   ♥♥♥ \\d\\d and \\d and y̆y̆ and 💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I   \\u{2665}\\u{2665}\\u{2665} \\d\\d and \\d and y\\u{306}y\\u{306} and \\u{1f4a9}\\u{1f4a9}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I   \\u{2665}\\u{2665}\\u{2665} \\d\\d and \\d and y\\u{306}y\\u{306} and \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ \ \ ♥♥♥\ \d\d\ and\ \d\ and\ y̆y̆\ and\ 💩💩\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ \ \ \u{2665}\u{2665}\u{2665}\ \d\d\ and\ \d\ and\ y\u{306}y\u{306}\ and\ \u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ \ \ \u{2665}\u{2665}\u{2665}\ \d\d\ and\ \d\ and\ y\u{306}y\u{306}\ and\ \u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_capturing_groups_option() {
            let mut grex = init_command();
            grex.args(&["--capture-groups", "abc", "def"]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^(abc|def)$\n"));
        }

        #[test]
        fn succeeds_with_syntax_highlighting() {
            let mut grex = init_command();
            grex.args(&["--colorize", "abc", "def"]);
            grex.assert()
                .success()
                .stdout(predicate::eq("\u{1b}[1;33m^\u{1b}[0m\u{1b}[1;32m(?:\u{1b}[0mabc\u{1b}[1;31m|\u{1b}[0mdef\u{1b}[1;32m)\u{1b}[0m\u{1b}[1;33m$\u{1b}[0m\n"));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--digits", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I {3}♥{3} \\d(?:\\d and ){2}(?:y̆){2} and 💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--digits", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I {3}\\u{2665}{3} \\d(?:\\d and ){2}(?:y\\u{306}){2} and \\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I {3}\\u{2665}{3} \\d(?:\\d and ){2}(?:y\\u{306}){2} and (?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--digits", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ {3}♥{3}\ \d
                  (?:
                    \d\ and\ 
                  ){2}
                  (?:
                    y̆
                  ){2}
                  \ and\ 💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ {3}\u{2665}{3}\ \d
                  (?:
                    \d\ and\ 
                  ){2}
                  (?:
                    y\u{306}
                  ){2}
                  \ and\ \u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ {3}\u{2665}{3}\ \d
                  (?:
                    \d\ and\ 
                  ){2}
                  (?:
                    y\u{306}
                  ){2}
                  \ and\ 
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_increased_minimum_repetitions() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--min-repetitions",
                "2",
                "--digits",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I {3}♥{3} \\d\\d and \\d and y̆y̆ and 💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_increased_minimum_substring_length() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--min-substring-length",
                "2",
                "--digits",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I   ♥♥♥ \\d(?:\\d and ){2}(?:y̆){2} and 💩💩\\.$\n",
            ));
        }
    }
}

mod space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s\\s\\s♥♥♥\\s36\\sand\\s٣\\sand\\sy̆y̆\\sand\\s💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s36\\sand\\s\\u{663}\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{1f4a9}\\u{1f4a9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--spaces", "--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s36\\sand\\s\\u{663}\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s\s\s♥♥♥\s36\sand\s٣\sand\sy̆y̆\sand\s💩💩\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--spaces", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s\s\s\u{2665}\u{2665}\u{2665}\s36\sand\s\u{663}\sand\sy\u{306}y\u{306}\sand\s\u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s\s\s\u{2665}\u{2665}\u{2665}\s36\sand\s\u{663}\sand\sy\u{306}y\u{306}\sand\s\u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s{3}♥{3}\\s36\\sand\\s٣\\sand\\s(?:y̆){2}\\sand\\s💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s{3}\\u{2665}{3}\\s36\\sand\\s\\u{663}\\sand\\s(?:y\\u{306}){2}\\sand\\s\\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s{3}\\u{2665}{3}\\s36\\sand\\s\\u{663}\\sand\\s(?:y\\u{306}){2}\\sand\\s(?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s{3}♥{3}\s36\sand\s٣\sand\s
                  (?:
                    y̆
                  ){2}
                  \sand\s💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s{3}\u{2665}{3}\s36\sand\s\u{663}\sand\s
                  (?:
                    y\u{306}
                  ){2}
                  \sand\s\u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s{3}\u{2665}{3}\s36\sand\s\u{663}\sand\s
                  (?:
                    y\u{306}
                  ){2}
                  \sand\s
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }
    }
}

mod word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w   ♥♥♥ \\w\\w \\w\\w\\w \\w \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w 💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\w\\w \\w\\w\\w \\w \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{1f4a9}\\u{1f4a9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\w\\w \\w\\w\\w \\w \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ \ \ ♥♥♥\ \w\w\ \w\w\w\ \w\ \w\w\w\ \w\w\w\w\ \w\w\w\ 💩💩\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ \ \ \u{2665}\u{2665}\u{2665}\ \w\w\ \w\w\w\ \w\ \w\w\w\ \w\w\w\w\ \w\w\w\ \u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ \ \ \u{2665}\u{2665}\u{2665}\ \w\w\ \w\w\w\ \w\ \w\w\w\ \w\w\w\w\ \w\w\w\ \u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w {3}♥{3} \\w{2}(?: \\w{3} \\w){2}(?:\\w{3} ){2}💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w {3}\\u{2665}{3} \\w{2}(?: \\w{3} \\w){2}(?:\\w{3} ){2}\\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w {3}\\u{2665}{3} \\w{2}(?: \\w{3} \\w){2}(?:\\w{3} ){2}(?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ {3}♥{3}\ \w{2}
                  (?:
                    \ \w{3}\ \w
                  ){2}
                  (?:
                    \w{3}\ 
                  ){2}
                  💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ {3}\u{2665}{3}\ \w{2}
                  (?:
                    \ \w{3}\ \w
                  ){2}
                  (?:
                    \w{3}\ 
                  ){2}
                  \u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ {3}\u{2665}{3}\ \w{2}
                  (?:
                    \ \w{3}\ \w
                  ){2}
                  (?:
                    \w{3}\ 
                  ){2}
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }
    }
}

mod digit_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--digits", "--spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s\\s\\s♥♥♥\\s\\d\\d\\sand\\s\\d\\sand\\sy̆y̆\\sand\\s💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\sand\\s\\d\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{1f4a9}\\u{1f4a9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\sand\\s\\d\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s\s\s♥♥♥\s\d\d\sand\s\d\sand\sy̆y̆\sand\s💩💩\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--spaces", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s\s\s\u{2665}\u{2665}\u{2665}\s\d\d\sand\s\d\sand\sy\u{306}y\u{306}\sand\s\u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s\s\s\u{2665}\u{2665}\u{2665}\s\d\d\sand\s\d\sand\sy\u{306}y\u{306}\sand\s\u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--digits", "--spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s{3}♥{3}\\s\\d(?:\\d\\sand\\s){2}(?:y̆){2}\\sand\\s💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--spaces",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\sand\\s){2}(?:y\\u{306}){2}\\sand\\s\\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\sand\\s){2}(?:y\\u{306}){2}\\sand\\s(?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--spaces",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s{3}♥{3}\s\d
                  (?:
                    \d\sand\s
                  ){2}
                  (?:
                    y̆
                  ){2}
                  \sand\s💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s{3}\u{2665}{3}\s\d
                  (?:
                    \d\sand\s
                  ){2}
                  (?:
                    y\u{306}
                  ){2}
                  \sand\s\u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\s{3}\u{2665}{3}\s\d
                  (?:
                    \d\sand\s
                  ){2}
                  (?:
                    y\u{306}
                  ){2}
                  \sand\s
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }
    }
}

mod digit_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--digits", "--words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w   ♥♥♥ \\d\\d \\w\\w\\w \\d \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w 💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\d\\d \\w\\w\\w \\d \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{1f4a9}\\u{1f4a9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\d\\d \\w\\w\\w \\d \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ \ \ ♥♥♥\ \d\d\ \w\w\w\ \d\ \w\w\w\ \w\w\w\w\ \w\w\w\ 💩💩\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--words", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ \ \ \u{2665}\u{2665}\u{2665}\ \d\d\ \w\w\w\ \d\ \w\w\w\ \w\w\w\w\ \w\w\w\ \u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ \ \ \u{2665}\u{2665}\u{2665}\ \d\d\ \w\w\w\ \d\ \w\w\w\ \w\w\w\w\ \w\w\w\ \u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--digits", "--words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w {3}♥{3} \\d(?:\\d \\w{3} ){2}\\w(?:\\w{3} ){2}💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w {3}\\u{2665}{3} \\d(?:\\d \\w{3} ){2}\\w(?:\\w{3} ){2}\\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w {3}\\u{2665}{3} \\d(?:\\d \\w{3} ){2}\\w(?:\\w{3} ){2}(?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ {3}♥{3}\ \d
                  (?:
                    \d\ \w{3}\ 
                  ){2}
                  \w
                  (?:
                    \w{3}\ 
                  ){2}
                  💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ {3}\u{2665}{3}\ \d
                  (?:
                    \d\ \w{3}\ 
                  ){2}
                  \w
                  (?:
                    \w{3}\ 
                  ){2}
                  \u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\ {3}\u{2665}{3}\ \d
                  (?:
                    \d\ \w{3}\ 
                  ){2}
                  \w
                  (?:
                    \w{3}\ 
                  ){2}
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }
    }
}

mod space_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--words", "--spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s\\s\\s♥♥♥\\s\\w\\w\\s\\w\\w\\w\\s\\w\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\w\\w\\s\\w\\w\\w\\s\\w\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{1f4a9}\\u{1f4a9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\w\\w\\s\\w\\w\\w\\s\\w\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s\s\s♥♥♥\s\w\w\s\w\w\w\s\w\s\w\w\w\s\w\w\w\w\s\w\w\w\s💩💩\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--spaces", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s\s\s\u{2665}\u{2665}\u{2665}\s\w\w\s\w\w\w\s\w\s\w\w\w\s\w\w\w\w\s\w\w\w\s\u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s\s\s\u{2665}\u{2665}\u{2665}\s\w\w\s\w\w\w\s\w\s\w\w\w\s\w\w\w\w\s\w\w\w\s\u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--words", "--spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s{3}♥{3}\\s\\w{2}(?:\\s\\w{3}\\s\\w){2}(?:\\w{3}\\s){2}💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--spaces",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s{3}\\u{2665}{3}\\s\\w{2}(?:\\s\\w{3}\\s\\w){2}(?:\\w{3}\\s){2}\\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s{3}\\u{2665}{3}\\s\\w{2}(?:\\s\\w{3}\\s\\w){2}(?:\\w{3}\\s){2}(?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--spaces",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s{3}♥{3}\s\w{2}
                  (?:
                    \s\w{3}\s\w
                  ){2}
                  (?:
                    \w{3}\s
                  ){2}
                  💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s{3}\u{2665}{3}\s\w{2}
                  (?:
                    \s\w{3}\s\w
                  ){2}
                  (?:
                    \w{3}\s
                  ){2}
                  \u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s{3}\u{2665}{3}\s\w{2}
                  (?:
                    \s\w{3}\s\w
                  ){2}
                  (?:
                    \w{3}\s
                  ){2}
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }
    }
}

mod digit_space_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--digits", "--words", "--spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s\\s\\s♥♥♥\\s\\d\\d\\s\\w\\w\\w\\s\\d\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s💩💩\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--words", "--spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\s\\w\\w\\w\\s\\d\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{1f4a9}\\u{1f4a9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\s\\w\\w\\w\\s\\d\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$\n"
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--words", "--spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s\s\s♥♥♥\s\d\d\s\w\w\w\s\d\s\w\w\w\s\w\w\w\w\s\w\w\w\s💩💩\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--words",
                "--spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s\s\s\u{2665}\u{2665}\u{2665}\s\d\d\s\w\w\w\s\d\s\w\w\w\s\w\w\w\w\s\w\w\w\s\u{1f4a9}\u{1f4a9}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s\s\s\u{2665}\u{2665}\u{2665}\s\d\d\s\w\w\w\s\d\s\w\w\w\s\w\w\w\w\s\w\w\w\s\u{d83d}\u{dca9}\u{d83d}\u{dca9}\.
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--spaces",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s{3}♥{3}\\s\\d(?:\\d\\s\\w{3}\\s){2}\\w(?:\\w{3}\\s){2}💩{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--spaces",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\s\\w{3}\\s){2}\\w(?:\\w{3}\\s){2}\\u{1f4a9}{2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\s\\w{3}\\s){2}\\w(?:\\w{3}\\s){2}(?:\\u{d83d}\\u{dca9}){2}\\.$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--spaces",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s{3}♥{3}\s\d
                  (?:
                    \d\s\w{3}\s
                  ){2}
                  \w
                  (?:
                    \w{3}\s
                  ){2}
                  💩{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s{3}\u{2665}{3}\s\d
                  (?:
                    \d\s\w{3}\s
                  ){2}
                  \w
                  (?:
                    \w{3}\s
                  ){2}
                  \u{1f4a9}{2}\.
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--words",
                "--spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\s{3}\u{2665}{3}\s\d
                  (?:
                    \d\s\w{3}\s
                  ){2}
                  \w
                  (?:
                    \w{3}\s
                  ){2}
                  (?:
                    \u{d83d}\u{dca9}
                  ){2}
                  \.
                $
                "#
            )));
        }
    }
}

mod non_digit_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--non-digits", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D٣\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D\\u{663}\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D\\u{663}\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D36\D\D\D\D\D٣\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D36\D\D\D\D\D\u{663}\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D36\D\D\D\D\D\u{663}\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-digits", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}36\\D{5}٣\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-digits", "--escape", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}36\\D{5}\\u{663}\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}36\\D{5}\\u{663}\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-digits", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}36\D{5}٣\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}36\D{5}\u{663}\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}36\D{5}\u{663}\D{17}
                $
                "#
            )));
        }
    }
}

mod non_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S   \\S\\S\\S \\S\\S \\S\\S\\S \\S \\S\\S\\S \\S\\S\\S\\S \\S\\S\\S \\S\\S\\S$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S   \\S\\S\\S \\S\\S \\S\\S\\S \\S \\S\\S\\S \\S\\S\\S\\S \\S\\S\\S \\S\\S\\S$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", "--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S   \\S\\S\\S \\S\\S \\S\\S\\S \\S \\S\\S\\S \\S\\S\\S\\S \\S\\S\\S \\S\\S\\S$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\ \ \ \S\S\S\ \S\S\ \S\S\S\ \S\ \S\S\S\ \S\S\S\S\ \S\S\S\ \S\S\S
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\ \ \ \S\S\S\ \S\S\ \S\S\S\ \S\ \S\S\S\ \S\S\S\S\ \S\S\S\ \S\S\S
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\ \ \ \S\S\S\ \S\S\ \S\S\S\ \S\ \S\S\S\ \S\S\S\S\ \S\S\S\ \S\S\S
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S {3}\\S(?:\\S{2} ){2}\\S{3} (?:\\S(?: \\S{3}){2}){2}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S {3}\\S(?:\\S{2} ){2}\\S{3} (?:\\S(?: \\S{3}){2}){2}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S {3}\\S(?:\\S{2} ){2}\\S{3} (?:\\S(?: \\S{3}){2}){2}$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\ {3}\S
                  (?:
                    \S{2}\ 
                  ){2}
                  \S{3}\ 
                  (?:
                    \S
                    (?:
                      \ \S{3}
                    ){2}
                  ){2}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\ {3}\S
                  (?:
                    \S{2}\ 
                  ){2}
                  \S{3}\ 
                  (?:
                    \S
                    (?:
                      \ \S{3}
                    ){2}
                  ){2}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\ {3}\S
                  (?:
                    \S{2}\ 
                  ){2}
                  \S{3}\ 
                  (?:
                    \S
                    (?:
                      \ \S{3}
                    ){2}
                  ){2}
                $
                "#
            )));
        }
    }
}

mod non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\W\\W\\W\\W\\W\\W\\W36\\Wand\\W٣\\Wand\\Wy̆y̆\\Wand\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--non-words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\W\\W\\W\\W\\W\\W\\W36\\Wand\\W\\u{663}\\Wand\\Wy\\u{306}y\\u{306}\\Wand\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&["--non-words", "--escape", "--with-surrogates", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\W\\W\\W\\W\\W\\W\\W36\\Wand\\W\\u{663}\\Wand\\Wy\\u{306}y\\u{306}\\Wand\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\W\W\W\W\W\W\W36\Wand\W٣\Wand\Wy̆y̆\Wand\W\W\W\W
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-words", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\W\W\W\W\W\W\W36\Wand\W\u{663}\Wand\Wy\u{306}y\u{306}\Wand\W\W\W\W
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\W\W\W\W\W\W\W36\Wand\W\u{663}\Wand\Wy\u{306}y\u{306}\Wand\W\W\W\W
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\W{7}36\\Wand\\W٣\\Wand\\W(?:y̆){2}\\Wand\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\W{7}36\\Wand\\W\\u{663}\\Wand\\W(?:y\\u{306}){2}\\Wand\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^I\\W{7}36\\Wand\\W\\u{663}\\Wand\\W(?:y\\u{306}){2}\\Wand\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\W{7}36\Wand\W٣\Wand\W
                  (?:
                    y̆
                  ){2}
                  \Wand\W{4}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\W{7}36\Wand\W\u{663}\Wand\W
                  (?:
                    y\u{306}
                  ){2}
                  \Wand\W{4}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\W{7}36\Wand\W\u{663}\Wand\W
                  (?:
                    y\u{306}
                  ){2}
                  \Wand\W{4}
                $
                "#
            )));
        }
    }
}

mod non_digit_non_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--non-spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--non-spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--non-spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\S\S\D\D\D\D\D\S\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\S\S\D\D\D\D\D\S\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\S\S\D\D\D\D\D\S\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-digits", "--non-spaces", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\S{2}\\D{5}\\S\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\S{2}\\D{5}\\S\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\S{2}\\D{5}\\S\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\S{2}\D{5}\S\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\S{2}\D{5}\S\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\S{2}\D{5}\S\D{17}
                $
                "#
            )));
        }
    }
}

mod non_digit_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D٣\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--non-words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D\\u{663}\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D\\u{663}\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--non-words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D36\D\D\D\D\D٣\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D36\D\D\D\D\D\u{663}\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D36\D\D\D\D\D\u{663}\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-digits", "--non-words", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}36\\D{5}٣\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-words",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}36\\D{5}\\u{663}\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}36\\D{5}\\u{663}\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-words",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}36\D{5}٣\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}36\D{5}\u{663}\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}36\D{5}\u{663}\D{17}
                $
                "#
            )));
        }
    }
}

mod non_space_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", "--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\W\\W\\W\\W\\W\\W\\W\\S\\S\\W\\S\\S\\S\\W\\S\\W\\S\\S\\S\\W\\S\\S\\S\\S\\W\\S\\S\\S\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", "--non-words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\W\\W\\W\\W\\W\\W\\W\\S\\S\\W\\S\\S\\S\\W\\S\\W\\S\\S\\S\\W\\S\\S\\S\\S\\W\\S\\S\\S\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\W\\W\\W\\W\\W\\W\\W\\S\\S\\W\\S\\S\\S\\W\\S\\W\\S\\S\\S\\W\\S\\S\\S\\S\\W\\S\\S\\S\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--non-spaces", "--non-words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\W\W\W\W\W\W\W\S\S\W\S\S\S\W\S\W\S\S\S\W\S\S\S\S\W\S\S\S\W\W\W\W
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-spaces",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\W\W\W\W\W\W\W\S\S\W\S\S\S\W\S\W\S\S\S\W\S\S\S\S\W\S\S\S\W\W\W\W
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\W\W\W\W\W\W\W\S\S\W\S\S\S\W\S\W\S\S\S\W\S\S\S\S\W\S\S\S\W\W\W\W
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--non-spaces", "--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\W{7}\\S(?:\\S\\W\\S{3}\\W){2}\\S{4}\\W\\S{3}\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--non-words",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\W{7}\\S(?:\\S\\W\\S{3}\\W){2}\\S{4}\\W\\S{3}\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\W{7}\\S(?:\\S\\W\\S{3}\\W){2}\\S{4}\\W\\S{3}\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--non-words",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\W{7}\S
                  (?:
                    \S\W\S{3}\W
                  ){2}
                  \S{4}\W\S{3}\W{4}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\W{7}\S
                  (?:
                    \S\W\S{3}\W
                  ){2}
                  \S{4}\W\S{3}\W{4}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\W{7}\S
                  (?:
                    \S\W\S{3}\W
                  ){2}
                  \S{4}\W\S{3}\W{4}
                $
                "#
            )));
        }
    }
}

mod non_digit_non_space_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--non-digits", "--non-spaces", "--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\S\S\D\D\D\D\D\S\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\S\S\D\D\D\D\D\S\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\S\S\D\D\D\D\D\S\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--non-words",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\S{2}\\D{5}\\S\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\S{2}\\D{5}\\S\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\S{2}\\D{5}\\S\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\S{2}\D{5}\S\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\S{2}\D{5}\S\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--non-digits",
                "--non-spaces",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\S{2}\D{5}\S\D{17}
                $
                "#
            )));
        }
    }
}

mod digit_non_digit_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--digits", "--non-digits", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\d\\d\\D\\D\\D\\D\\D\\d\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--non-digits", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\d\\d\\D\\D\\D\\D\\D\\d\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--non-digits",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\d\\d\\D\\D\\D\\D\\D\\d\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--digits", "--non-digits", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\d\d\D\D\D\D\D\d\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--non-digits",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\d\d\D\D\D\D\D\d\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--digits",
                "--non-digits",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D\D\D\D\D\D\D\D\d\d\D\D\D\D\D\d\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D\D
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--digits", "--non-digits", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\d{2}\\D{5}\\d\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--non-digits",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\d{2}\\D{5}\\d\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--non-digits",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^\\D{8}\\d{2}\\D{5}\\d\\D{17}$\n"));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--non-digits",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\d{2}\D{5}\d\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--non-digits",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\d{2}\D{5}\d\D{17}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--digits",
                "--non-digits",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \D{8}\d{2}\D{5}\d\D{17}
                $
                "#
            )));
        }
    }
}

mod space_non_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--spaces", "--non-spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\s\\s\\s\\S\\S\\S\\s\\S\\S\\s\\S\\S\\S\\s\\S\\s\\S\\S\\S\\s\\S\\S\\S\\S\\s\\S\\S\\S\\s\\S\\S\\S$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--spaces", "--non-spaces", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\s\\s\\s\\S\\S\\S\\s\\S\\S\\s\\S\\S\\S\\s\\S\\s\\S\\S\\S\\s\\S\\S\\S\\S\\s\\S\\S\\S\\s\\S\\S\\S$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--spaces",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\s\\s\\s\\S\\S\\S\\s\\S\\S\\s\\S\\S\\S\\s\\S\\s\\S\\S\\S\\s\\S\\S\\S\\S\\s\\S\\S\\S\\s\\S\\S\\S$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--spaces", "--non-spaces", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\s\s\s\S\S\S\s\S\S\s\S\S\S\s\S\s\S\S\S\s\S\S\S\S\s\S\S\S\s\S\S\S
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--spaces",
                "--non-spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\s\s\s\S\S\S\s\S\S\s\S\S\S\s\S\s\S\S\S\s\S\S\S\S\s\S\S\S\s\S\S\S
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--spaces",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\s\s\s\S\S\S\s\S\S\s\S\S\S\s\S\s\S\S\S\s\S\S\S\S\s\S\S\S\s\S\S\S
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--spaces", "--non-spaces", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\s{3}\\S(?:\\S{2}\\s){2}\\S{3}\\s(?:\\S(?:\\s\\S{3}){2}){2}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--non-spaces",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\s{3}\\S(?:\\S{2}\\s){2}\\S{3}\\s(?:\\S(?:\\s\\S{3}){2}){2}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\S\\s{3}\\S(?:\\S{2}\\s){2}\\S{3}\\s(?:\\S(?:\\s\\S{3}){2}){2}$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--non-spaces",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\s{3}\S
                  (?:
                    \S{2}\s
                  ){2}
                  \S{3}\s
                  (?:
                    \S
                    (?:
                      \s\S{3}
                    ){2}
                  ){2}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--non-spaces",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\s{3}\S
                  (?:
                    \S{2}\s
                  ){2}
                  \S{3}\s
                  (?:
                    \S
                    (?:
                      \s\S{3}
                    ){2}
                  ){2}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--spaces",
                "--non-spaces",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \S\s{3}\S
                  (?:
                    \S{2}\s
                  ){2}
                  \S{3}\s
                  (?:
                    \S
                    (?:
                      \s\S{3}
                    ){2}
                  ){2}
                $
                "#
            )));
        }
    }
}

mod word_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--words", "--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\W\\W\\W\\W\\W\\W\\W\\w\\w\\W\\w\\w\\w\\W\\w\\W\\w\\w\\w\\W\\w\\w\\w\\w\\W\\w\\w\\w\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--non-words", "--escape", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\W\\W\\W\\W\\W\\W\\W\\w\\w\\W\\w\\w\\w\\W\\w\\W\\w\\w\\w\\W\\w\\w\\w\\w\\W\\w\\w\\w\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--words",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\W\\W\\W\\W\\W\\W\\W\\w\\w\\W\\w\\w\\w\\W\\w\\W\\w\\w\\w\\W\\w\\w\\w\\w\\W\\w\\w\\w\\W\\W\\W\\W$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--non-words", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\W\W\W\W\W\W\W\w\w\W\w\w\w\W\w\W\w\w\w\W\w\w\w\w\W\w\w\w\W\W\W\W
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&["--words", "--non-words", "--escape", "--verbose", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\W\W\W\W\W\W\W\w\w\W\w\w\w\W\w\W\w\w\w\W\w\w\w\w\W\w\w\w\W\W\W\W
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--words",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\W\W\W\W\W\W\W\w\w\W\w\w\w\W\w\W\w\w\w\W\w\w\w\w\W\w\w\w\W\W\W\W
                $
                "#
            )));
        }
    }

    mod repetition {
        use super::*;

        #[test]
        fn succeeds() {
            let mut grex = init_command();
            grex.args(&["--repetitions", "--words", "--non-words", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\W{7}\\w(?:\\w\\W\\w{3}\\W){2}\\w{4}\\W\\w{3}\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--non-words",
                "--escape",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\W{7}\\w(?:\\w\\W\\w{3}\\W){2}\\w{4}\\W\\w{3}\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--non-words",
                "--escape",
                "--with-surrogates",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(
                "^\\w\\W{7}\\w(?:\\w\\W\\w{3}\\W){2}\\w{4}\\W\\w{3}\\W{4}$\n",
            ));
        }

        #[test]
        fn succeeds_with_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--non-words",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\W{7}\w
                  (?:
                    \w\W\w{3}\W
                  ){2}
                  \w{4}\W\w{3}\W{4}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--non-words",
                "--escape",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\W{7}\w
                  (?:
                    \w\W\w{3}\W
                  ){2}
                  \w{4}\W\w{3}\W{4}
                $
                "#
            )));
        }

        #[test]
        fn succeeds_with_escape_and_surrogate_and_verbose_mode_option() {
            let mut grex = init_command();
            grex.args(&[
                "--repetitions",
                "--words",
                "--non-words",
                "--escape",
                "--with-surrogates",
                "--verbose",
                TEST_CASE,
            ]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  \w\W{7}\w
                  (?:
                    \w\W\w{3}\W
                  ){2}
                  \w{4}\W\w{3}\W{4}
                $
                "#
            )));
        }
    }
}

mod anchor_conversion {
    use super::*;

    mod no_verbose {
        use super::*;

        #[test]
        fn succeeds_with_no_start_anchor_option() {
            let mut grex = init_command();
            grex.args(&["--no-start-anchor", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩\\.$\n"));
        }

        #[test]
        fn succeeds_with_no_end_anchor_option() {
            let mut grex = init_command();
            grex.args(&["--no-end-anchor", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("^I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩\\.\n"));
        }

        #[test]
        fn succeeds_with_no_anchors_option() {
            let mut grex = init_command();
            grex.args(&["--no-anchors", TEST_CASE]);
            grex.assert()
                .success()
                .stdout(predicate::eq("I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩\\.\n"));
        }
    }

    mod verbose {
        use super::*;

        #[test]
        fn succeeds_with_verbose_mode_and_no_start_anchor_option() {
            let mut grex = init_command();
            grex.args(&["--verbose", "--no-start-anchor", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                  I\ \ \ ♥♥♥\ 36\ and\ ٣\ and\ y̆y̆\ and\ 💩💩\.
                $
                "#,
            )));
        }

        #[test]
        fn succeeds_with_verbose_mode_and_no_end_anchor_option() {
            let mut grex = init_command();
            grex.args(&["--verbose", "--no-end-anchor", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                ^
                  I\ \ \ ♥♥♥\ 36\ and\ ٣\ and\ y̆y̆\ and\ 💩💩\.
                "#,
            )));
        }

        #[test]
        fn succeeds_with_verbose_mode_and_no_anchors_option() {
            let mut grex = init_command();
            grex.args(&["--verbose", "--no-anchors", TEST_CASE]);
            grex.assert().success().stdout(predicate::eq(indoc!(
                r#"
                (?x)
                  I\ \ \ ♥♥♥\ 36\ and\ ٣\ and\ y̆y̆\ and\ 💩💩\.
                "#,
            )));
        }
    }
}

fn init_command() -> Command {
    Command::new(cargo_bin!())
}
```

## File: `tests/lib_integration_tests.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#![cfg(not(target_family = "wasm"))]

use grex::RegExpBuilder;
use indoc::indoc;
use regex::Regex;
use rstest::rstest;
use std::io::Write;
use tempfile::NamedTempFile;

mod no_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec![""], "^$"),
            case(vec![" "], "^ $"),
            case(vec!["   "], "^   $"),
            case(vec!["["], "^\\[$"),
            case(vec!["a", "("], "^[(a]$"),
            case(vec!["a", "\n"], "^[\\na]$"),
            case(vec!["a", "["], "^[\\[a]$"),
            case(vec!["a", "-", "c", "!"], "^[!\\-ac]$"),
            case(vec!["a", "b"], "^[ab]$"),
            case(vec!["a", "b", "c"], "^[a-c]$"),
            case(vec!["a", "c", "d", "e", "f"], "^[ac-f]$"),
            case(vec!["a", "b", "x", "d", "e"], "^[abdex]$"),
            case(vec!["a", "b", "x", "de"], "^(?:de|[abx])$"),
            case(vec!["a", "b", "c", "x", "d", "e"], "^[a-ex]$"),
            case(vec!["a", "b", "c", "x", "de"], "^(?:de|[a-cx])$"),
            case(vec!["a", "b", "c", "d", "e", "f", "o", "x", "y", "z"], "^[a-fox-z]$"),
            case(vec!["a", "b", "d", "e", "f", "o", "x", "y", "z"], "^[abd-fox-z]$"),
            case(vec!["1", "2"], "^[12]$"),
            case(vec!["1", "2", "3"], "^[1-3]$"),
            case(vec!["1", "3", "4", "5", "6"], "^[13-6]$"),
            case(vec!["1", "2", "8", "4", "5"], "^[12458]$"),
            case(vec!["1", "2", "8", "45"], "^(?:45|[128])$"),
            case(vec!["1", "2", "3", "8", "4", "5"], "^[1-58]$"),
            case(vec!["1", "2", "3", "8", "45"], "^(?:45|[1-38])$"),
            case(vec!["1", "2", "3", "5", "7", "8", "9"], "^[1-357-9]$"),
            case(vec!["a", "b", "bc"], "^(?:bc?|a)$"),
            case(vec!["a", "b", "bcd"], "^(?:b(?:cd)?|a)$"),
            case(vec!["a", "ab", "abc"], "^a(?:bc?)?$"),
            case(vec!["ac", "bc"], "^[ab]c$"),
            case(vec!["ab", "ac"], "^a[bc]$"),
            case(vec!["bc", "abc"], "^a?bc$"),
            case(vec!["ac", "abc"], "^ab?c$"),
            case(vec!["abc", "abxyc"], "^ab(?:xy)?c$"),
            case(vec!["ab", "abc"], "^abc?$"),
            case(vec!["abx", "cdx"], "^(?:ab|cd)x$"),
            case(vec!["abd", "acd"], "^a[bc]d$"),
            case(vec!["abc", "abcd"], "^abcd?$"),
            case(vec!["abc", "abcde"], "^abc(?:de)?$"),
            case(vec!["ade", "abcde"], "^a(?:bc)?de$"),
            case(vec!["abcxy", "adexy"], "^a(?:bc|de)xy$"),
            case(vec!["axy", "abcxy", "adexy"], "^a(?:(?:bc)?|de)xy$"), // goal: "^a(bc|de)?xy$"
            case(vec!["abcxy", "abcw", "efgh"], "^(?:abc(?:xy|w)|efgh)$"),
            case(vec!["abcxy", "efgh", "abcw"], "^(?:abc(?:xy|w)|efgh)$"),
            case(vec!["efgh", "abcxy", "abcw"], "^(?:abc(?:xy|w)|efgh)$"),
            case(vec!["abxy", "cxy", "efgh"], "^(?:(?:ab|c)xy|efgh)$"),
            case(vec!["abxy", "efgh", "cxy"], "^(?:(?:ab|c)xy|efgh)$"),
            case(vec!["efgh", "abxy", "cxy"], "^(?:(?:ab|c)xy|efgh)$"),
            case(vec!["aaacaac", "aac"], "^aa(?:acaa)?c$"),
            case(vec!["a", "ä", "o", "ö", "u", "ü"], "^[aouäöü]$"),
            case(vec!["y̆", "a", "z"], "^(?:y̆|[az])$"), // goal: "^[az]|y\\u{306}$"
            case(vec!["a", "b\n", "c"], "^(?:b\\n|[ac])$"),
            case(vec!["a", "b\\n", "c"], "^(?:b\\\\n|[ac])$"),
            case(vec!["[a-z]", "(d,e,f)"], "^(?:\\(d,e,f\\)|\\[a\\-z\\])$"),
            case(vec!["3.5", "4.5", "4,5"], "^(?:3\\.5|4[,.]5)$"),
            case(vec!["\u{b}"], "^\\v$"), // U+000B Line Tabulation
            case(vec!["\\u{b}"], "^\\\\u\\{b\\}$"),
            case(vec!["\u{c}"], "^\\f$"), // U+000C Form Feed
            case(vec!["\\u{c}"], "^\\\\u\\{c\\}$"),
            case(vec!["\u{200b}"], "^​$"),
            case(vec!["I ♥ cake"], "^I ♥ cake$"),
            case(vec!["I \u{2665} cake"], "^I ♥ cake$"),
            case(vec!["I \\u{2665} cake"], "^I \\\\u\\{2665\\} cake$"),
            case(vec!["I \\u2665 cake"], "^I \\\\u2665 cake$"),
            case(vec!["My ♥ is yours.", "My 💩 is yours."], "^My [♥💩] is yours\\.$"),
            case(vec!["[\u{c3e}"], "^\\[\u{c3e}$"),
            case(vec!["\\\u{10376}"], "^\\\\\u{10376}$"),
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩\\.$"),
            case(vec!["\u{890}\0"], "^\u{890}\0$"),
            case(vec!["\u{890}\\0"], "^\u{890}\\\\0$"),
            case(vec!["\u{890}\\\0"], "^\u{890}\\\\\0$"),
            case(vec!["\u{890}\\\\0"], "^\u{890}\\\\\\\\0$"),
            case(vec!["\\𑇂"], "^\\\\𑇂$"),
            case(vec!["𑇂\\"], "^𑇂\\\\$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases).build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["İ"], "(?i)^İ$"),
            case(vec!["ABC", "abc", "AbC", "aBc"], "(?i)^abc$"),
            case(vec!["ABC", "zBC", "abc", "AbC", "aBc"], "(?i)^[az]bc$"),
            case(vec!["Ä@Ö€Ü", "ä@ö€ü", "Ä@ö€Ü", "ä@Ö€ü"], "(?i)^ä@ö€ü$"),
        )]
        fn succeeds_with_ignore_case_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_case_insensitive_matching()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["My ♥ and 💩 is yours."], "^My \\u{2665} and \\u{1f4a9} is yours\\.$"),
            case(vec!["My ♥ is yours.", "My 💩 is yours."], "^My (?:\\u{2665}|\\u{1f4a9}) is yours\\.$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I   \\u{2665}\\u{2665}\\u{2665} 36 and \\u{663} and y\\u{306}y\\u{306} and \\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["My ♥ and 💩 is yours."], "^My \\u{2665} and \\u{d83d}\\u{dca9} is yours\\.$"),
            case(vec!["My ♥ is yours.", "My 💩 is yours."], "^My (?:\\u{2665}|\\u{d83d}\\u{dca9}) is yours\\.$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I   \\u{2665}\\u{2665}\\u{2665} 36 and \\u{663} and y\\u{306}y\\u{306} and \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["a", "b", "bc"], "^(bc?|a)$"),
            case(vec!["a", "b", "bcd"], "^(b(cd)?|a)$"),
            case(vec!["a", "ab", "abc"], "^a(bc?)?$"),
            case(vec!["efgh", "abcxy", "abcw"], "^(abc(xy|w)|efgh)$"),
        )]
        fn succeeds_with_capturing_groups_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_capturing_groups()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec![""], indoc!(
                r#"
                (?x)
                ^
                $"#
            )),
            case(vec![" "], indoc!(
                r#"
                (?x)
                ^
                  \ 
                $"#
            )),
            case(vec!["   "], indoc!(
                r#"
                (?x)
                ^
                  \ \ \ 
                $"#
            )),
            case(vec!["\u{200b}"], indoc!(
                r#"
                (?x)
                ^
                  ​
                $"#
            )),
            case(vec!["a", "b", "c"], indoc!(
                r#"
                (?x)
                ^
                  [a-c]
                $"#
            )),
            case(vec!["a", "b", "bc"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    bc?
                    |
                    a
                  )
                $"#
            )),
            case(vec!["a", "ab", "abc"], indoc!(
                r#"
                (?x)
                ^
                  a
                  (?:
                    bc?
                  )?
                $"#
            )),
            case(vec!["a", "b", "bcd"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    b
                    (?:
                      cd
                    )?
                    |
                    a
                  )
                $"#
            )),
            case(vec!["a", "b", "x", "de"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    de
                    |
                    [abx]
                  )
                $"#
            )),
            case(vec!["[a-z]", "(d,e,f)"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    \(d,e,f\)
                    |
                    \[a\-z\]
                  )
                $"#
            )),
            case(vec!["3.5", "4.5", "4,5"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    3\.5
                    |
                    4[,.]5
                  )
                $"#
            )),
            case(vec!["Ga", "G)"], indoc!(
                r#"
                (?x)
                ^
                  G[)a]
                $"#
            )),
            case(vec!["aG", ")G"], indoc!(
                r#"
                (?x)
                ^
                  [)a]G
                $"#
            )),
            case(vec!["Ga", "G)", "G("], indoc!(
                r#"
                (?x)
                ^
                  G[()a]
                $"#
            )),
            case(vec!["aG", ")G", "(G"], indoc!(
                r#"
                (?x)
                ^
                  [()a]G
                $"#
            )),
            case(vec!["aaacaac", "aac"], indoc!(
                r#"
                (?x)
                ^
                  aa
                  (?:
                    acaa
                  )?
                  c
                $"#
            )),
        )]
        fn succeeds_with_verbose_mode_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases).with_verbose_mode().build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["İ"], indoc!(
                r#"
                (?ix)
                ^
                  İ
                $"#
            )),
            case(vec!["ABC", "abc", "AbC", "aBc"], indoc!(
                r#"
                (?ix)
                ^
                  abc
                $"#
            )),
            case(vec!["ABC", "zBC", "abc", "AbC", "aBc"], indoc!(
                r#"
                (?ix)
                ^
                  [az]bc
                $"#
            )),
            case(vec!["Ä@Ö€Ü", "ä@ö€ü", "Ä@ö€Ü", "ä@Ö€ü"], indoc!(
                r#"
                (?ix)
                ^
                  ä@ö€ü
                $"#
            ))
        )]
        fn succeeds_with_ignore_case_and_verbose_mode_option(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_case_insensitive_matching()
                .with_verbose_mode()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[test]
        fn succeeds_with_file_input() {
            let mut file = NamedTempFile::new().unwrap();
            writeln!(file, "a\nb\nc\r\nxyz").unwrap();

            let expected_output = "^(?:xyz|[a-c])$";
            let test_cases = vec!["a", "b", "c", "xyz"];

            let regexp = RegExpBuilder::from_file(file.path()).build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec![""], "^$"),
            case(vec![" "], "^ $"),
            case(vec!["   "], "^ {3}$"),
            case(vec!["a"], "^a$"),
            case(vec!["aa"], "^a{2}$"),
            case(vec!["aaa"], "^a{3}$"),
            case(vec!["aaa aaa"], "^a{3} a{3}$"),
            case(vec!["ababab ababab"], "^(?:ab){3} (?:ab){3}$"),
            case(vec!["ababab  ababab"], "^(?:ab){3} {2}(?:ab){3}$"),
            case(vec!["a ababab ababab"], "^a(?: (?:ab){3}){2}$"),
            case(vec!["ababab ababab a"], "^a(?:b(?:ab){2} a){2}$"),
            case(vec!["ababababab abab ababab"], "^ababab(?:(?:ab){2} ){2}(?:ab){3}$"),
            case(vec!["a", "aa"], "^a{1,2}$"),
            case(vec!["aaa", "a", "aa"], "^a{1,3}$"),
            case(vec!["aaaa", "a", "aa"], "^(?:a{1,2}|a{4})$"),
            case(vec!["a", "aa", "aaa", "aaaa", "aaab"], "^(?:a{3}b|a{1,4})$"),
            case(vec!["baabaaaaaabb"], "^ba{2}ba{6}b{2}$"),
            case(vec!["aabbaabbaaa"], "^(?:a{2}b{2}){2}a{3}$"),
            case(vec!["aabbaa"], "^a{2}b{2}a{2}$"),
            case(vec!["aabbabb"], "^a(?:ab{2}){2}$"),
            case(vec!["ababab"], "^(?:ab){3}$"),
            case(vec!["abababa"], "^a(?:ba){3}$"),
            case(vec!["aababab"], "^a(?:ab){3}$"),
            case(vec!["abababaa"], "^(?:ab){3}a{2}$"),
            case(vec!["aaaaaabbbbb"], "^a{6}b{5}$"),
            case(vec!["aabaababab"], "^a{2}ba(?:ab){3}$"),
            case(vec!["aaaaaaabbbbbba"], "^a{7}b{6}a$"),
            case(vec!["abaaaabaaba"], "^abaaa(?:aba){2}$"),
            case(vec!["bbaababb"], "^b{2}a{2}bab{2}$"),
            case(vec!["b", "ba"], "^ba?$"),
            case(vec!["b", "ba", "baa"], "^b(?:a{1,2})?$"),
            case(vec!["b", "ba", "baaa", "baa"], "^b(?:a{1,3})?$"),
            case(vec!["b", "ba", "baaaa", "baa"], "^b(?:a{1,2}|a{4})?$"),
            case(vec!["axy", "abcxyxy", "adexy"], "^a(?:(?:de)?xy|bc(?:xy){2})$"),
            case(vec!["xy̆y̆y̆y̆z"], "^x(?:y̆){4}z$"),
            case(vec!["xy̆y̆z", "xy̆y̆y̆z"], "^x(?:y̆){2,3}z$"),
            case(vec!["xy̆y̆z", "xy̆y̆y̆y̆z"], "^x(?:(?:y̆){2}|(?:y̆){4})z$"),
            case(vec!["zyxx", "yxx"], "^z?yx{2}$"),
            case(vec!["zyxx", "yxx", "yxxx"], "^(?:zyx{2}|yx{2,3})$"),
            case(vec!["zyxxx", "yxx", "yxxx"], "^(?:zyx{3}|yx{2,3})$"),
            case(vec!["a", "b\n\n", "c"], "^(?:b\\n{2}|[ac])$"),
            case(vec!["a", "b\nb\nb", "c"], "^(?:b(?:\\nb){2}|[ac])$"),
            case(vec!["a", "b\nx\nx", "c"], "^(?:b(?:\\nx){2}|[ac])$"),
            case(vec!["a", "b\n\t\n\t", "c"], "^(?:b(?:\\n\\t){2}|[ac])$"),
            case(vec!["a", "b\n", "b\n\n", "b\n\n\n", "c"], "^(?:b\\n{1,3}|[ac])$"),
            case(vec!["4.5", "3.55"], "^(?:4\\.5|3\\.5{2})$"),
            case(vec!["4.5", "4.55"], "^4\\.5{1,2}$"),
            case(vec!["4.5", "4.55", "3.5"], "^(?:3\\.5|4\\.5{1,2})$"),
            case(vec!["4.5", "44.5", "44.55", "4.55"], "^4{1,2}\\.5{1,2}$"),
            case(vec!["I ♥♥ cake"], "^I ♥{2} cake$"),
            case(vec!["I ♥ cake", "I ♥♥ cake"], "^I ♥{1,2} cake$"),
            case(vec!["I \u{2665}\u{2665} cake"], "^I ♥{2} cake$"),
            case(vec!["I \\u{2665} cake"], "^I \\\\u\\{26{2}5\\} cake$"),
            case(vec!["I \\u{2665}\\u{2665} cake"], "^I (?:\\\\u\\{26{2}5\\}){2} cake$"),
            case(vec!["I \\u2665\\u2665 cake"], "^I (?:\\\\u26{2}5){2} cake$"),
            case(vec!["My ♥♥♥ is yours.", "My 💩💩 is yours."], "^My (?:💩{2}|♥{3}) is yours\\.$"),
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^I {3}♥{3} 36 and ٣ and (?:y̆){2} and 💩{2}\\.$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["İ", "İİ"], "(?i)^İ{1,2}$"),
            case(vec!["AAAAB", "aaaab", "AaAaB", "aAaAB"], "(?i)^a{4}b$"),
            case(vec!["ÄÖÜäöü@Ö€", "äöüÄöÜ@ö€"], "(?i)^(?:äöü){2}@ö€$"),
        )]
        fn succeeds_with_ignore_case_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_case_insensitive_matching()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["My ♥♥♥ and 💩💩 is yours."], "^My \\u{2665}{3} and \\u{1f4a9}{2} is yours\\.$"),
            case(vec!["My ♥♥♥ is yours.", "My 💩💩 is yours."], "^My (?:\\u{1f4a9}{2}|\\u{2665}{3}) is yours\\.$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I {3}\\u{2665}{3} 36 and \\u{663} and (?:y\\u{306}){2} and \\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["My ♥♥♥ and 💩💩 is yours."], "^My \\u{2665}{3} and (?:\\u{d83d}\\u{dca9}){2} is yours\\.$"),
            case(vec!["My ♥♥♥ is yours.", "My 💩💩 is yours."], "^My (?:(?:\\u{d83d}\\u{dca9}){2}|\\u{2665}{3}) is yours\\.$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I {3}\\u{2665}{3} 36 and \\u{663} and (?:y\\u{306}){2} and (?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["   "], indoc!(
                r#"
                (?x)
                ^
                  \ {3}
                $"#
            )),
            case(vec!["aa"], indoc!(
                r#"
                (?x)
                ^
                  a{2}
                $"#
            )),
            case(vec!["aaa", "a", "aa"], indoc!(
                r#"
                (?x)
                ^
                  a{1,3}
                $"#
            )),
            case(vec!["aaaa", "a", "aa"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    a{1,2}
                    |
                    a{4}
                  )
                $"#
            )),
            case(vec!["ababab"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    ab
                  ){3}
                $"#
            )),
            case(vec!["abababa"], indoc!(
                r#"
                (?x)
                ^
                  a
                  (?:
                    ba
                  ){3}
                $"#
            )),
            case(vec!["abababaa"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    ab
                  ){3}
                  a{2}
                $"#
            )),
            case(vec!["aabaababab"], indoc!(
                r#"
                (?x)
                ^
                  a{2}ba
                  (?:
                    ab
                  ){3}
                $"#
            )),
            case(vec!["abaaaabaaba"], indoc!(
                r#"
                (?x)
                ^
                  abaaa
                  (?:
                    aba
                  ){2}
                $"#
            )),
            case(vec!["xy̆y̆z", "xy̆y̆y̆y̆z"], indoc!(
                r#"
                (?x)
                ^
                  x
                  (?:
                    (?:
                      y̆
                    ){2}
                    |
                    (?:
                      y̆
                    ){4}
                  )
                  z
                $"#
            )),
            case(vec!["a", "b\n\t\n\t", "c"], indoc!(
                r#"
                (?x)
                ^
                  (?:
                    b
                    (?:
                      \n\t
                    ){2}
                    |
                    [ac]
                  )
                $"#
            )),
            case(vec!["My ♥♥♥ is yours.", "My 💩💩 is yours."], indoc!(
                r#"
                (?x)
                ^
                  My\ 
                  (?:
                    💩{2}
                    |
                    ♥{3}
                  )
                  \ is\ yours\.
                $"#
            ))
        )]
        fn succeeds_with_verbose_mode_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_verbose_mode()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec![""], "^$"),
            case(vec![" "], "^ $"),
            case(vec!["   "], "^   $"),
            case(vec!["    "], "^ {4}$"),
            case(vec!["      "], "^ {6}$"),
            case(vec!["a"], "^a$"),
            case(vec!["aa"], "^aa$"),
            case(vec!["aaa"], "^aaa$"),
            case(vec!["aaaa"], "^a{4}$"),
            case(vec!["aaaaa"], "^a{5}$"),
            case(vec!["ababababab abab ababab"], "^(?:ab){5} abab ababab$"),
            case(vec!["aabbaaaabbbabbbbba"], "^aabba{4}bbbab{5}a$"),
            case(vec!["baabaaaaaabb"], "^baaba{6}bb$"),
            case(vec!["ababab"], "^ababab$"),
            case(vec!["abababab"], "^(?:ab){4}$"),
            case(vec!["abababa"], "^abababa$"),
            case(vec!["ababababa"], "^a(?:ba){4}$"),
            case(vec!["aababab"], "^aababab$"),
            case(vec!["aabababab"], "^a(?:ab){4}$"),
            case(vec!["xy̆y̆z", "xy̆y̆y̆y̆z"], "^x(?:y̆y̆|(?:y̆){4})z$"),
            case(vec!["aaa", "a", "aa"], "^a(?:aa?)?$"),
            case(vec!["a", "aa", "aaa", "aaaa"], "^(?:aaa|aa?|a{4})$"),
            case(vec!["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], "^(?:aaa|aa?|a{4,6})$")
        )]
        fn succeeds_with_increased_minimum_repetitions(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_minimum_repetitions(3)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["aaa"], "^aaa$"),
            case(vec!["ababab"], "^ababab$"),
            case(vec!["abcabcabc"], "^(?:abc){3}$"),
            case(vec!["abcabcabc", "dede"], "^(?:dede|(?:abc){3})$"),
            case(vec!["abcabcabc", "defgdefg"], "^(?:(?:defg){2}|(?:abc){3})$"),
            case(vec!["ababababab abab ababab"], "^ababab(?:abab ){2}ababab$")
        )]
        fn succeeds_with_increased_minimum_substring_length(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_minimum_substring_length(3)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["abababab"], "^abababab$"),
            case(vec!["abcabcabc"], "^abcabcabc$"),
            case(vec!["abcabcabcabc"], "^(?:abc){4}$"),
            case(vec!["aaaaaaaaaaaa"], "^aaaaaaaaaaaa$"),
            case(vec!["abababab", "abcabcabcabc"], "^(?:abababab|(?:abc){4})$"),
            case(vec!["ababababab abab ababab"], "^ababababab abab ababab$")
        )]
        fn succeeds_with_increased_minimum_repetitions_and_substring_length(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_minimum_repetitions(3)
                .with_minimum_substring_length(3)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod digit_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec![""], "^$"),
            case(vec!["a"], "^a$"),
            case(vec!["1"], "^\\d$"),
            case(vec!["-1"], "^\\-\\d$"),
            case(vec!["12"], "^\\d\\d$"),
            case(vec!["1", "2"], "^\\d$"),
            case(vec!["1", "23"], "^\\d(?:\\d)?$"),
            case(vec!["1", "234"], "^\\d(?:\\d\\d)?$"),
            case(vec!["8", "234"], "^\\d(?:\\d\\d)?$"),
            case(vec!["890", "34"], "^\\d\\d(?:\\d)?$"),
            case(vec!["abc123"], "^abc\\d\\d\\d$"),
            case(vec!["a1b2c3"], "^a\\db\\dc\\d$"),
            case(vec!["abc", "123"], "^(?:\\d\\d\\d|abc)$"),
            case(vec!["١", "٣", "٥"], "^\\d$"), // Arabic digits: ١ = 1, ٣ = 3, ٥ = 5
            case(vec!["١٣٥"], "^\\d\\d\\d$"),
            case(vec!["a٣3", "b5٥"], "^[ab]\\d\\d$"),
            case(vec!["I ♥ 123"], "^I ♥ \\d\\d\\d$"),
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^I   ♥♥♥ \\d\\d and \\d and y̆y̆ and 💩💩\\.$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I   \\u{2665}\\u{2665}\\u{2665} \\d\\d and \\d and y\\u{306}y\\u{306} and \\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I   \\u{2665}\\u{2665}\\u{2665} \\d\\d and \\d and y\\u{306}y\\u{306} and \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I {3}♥{3} \\d(?:\\d and ){2}(?:y̆){2} and 💩{2}\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I {3}\\u{2665}{3} \\d(?:\\d and ){2}(?:y\\u{306}){2} and \\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I {3}\\u{2665}{3} \\d(?:\\d and ){2}(?:y\\u{306}){2} and (?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["1"], "^\\d$"),
            case(vec!["12"], "^\\d\\d$"),
            case(vec!["123"], "^\\d{3}$"),
            case(vec!["1", "12", "123"], "^(?:\\d\\d|\\d|\\d{3})$"),
            case(vec!["12", "123", "1234"], "^(?:\\d\\d|\\d{3,4})$"),
            case(vec!["123", "1234", "12345"], "^\\d{3,5}$"),
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^I {3}♥{3} \\d\\d and \\d and y̆y̆ and 💩💩\\.$")
        )]
        fn succeeds_with_increased_minimum_repetitions(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_minimum_repetitions(2)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec![""], "^$"),
            case(vec![" "], "^\\s$"),
            case(vec!["   "], "^\\s\\s\\s$"),
            case(vec!["\n"], "^\\s$"),
            case(vec!["\u{c}"], "^\\s$"), // form feed \f
            case(vec!["\u{b}"], "^\\s$"), // vertical tab \v
            case(vec!["\n", "\r"], "^\\s$"),
            case(vec!["\n\t", "\r"], "^\\s(?:\\s)?$"),
            case(vec!["a"], "^a$"),
            case(vec!["1"], "^1$"),
            case(vec!["I ♥ 123"], "^I\\s♥\\s123$"),
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^I\\s\\s\\s♥♥♥\\s36\\sand\\s٣\\sand\\sy̆y̆\\sand\\s💩💩\\.$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s36\\sand\\s\\u{663}\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s36\\sand\\s\\u{663}\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}♥{3}\\s36\\sand\\s٣\\sand\\s(?:y̆){2}\\sand\\s💩{2}\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}\\u{2665}{3}\\s36\\sand\\s\\u{663}\\sand\\s(?:y\\u{306}){2}\\sand\\s\\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}\\u{2665}{3}\\s36\\sand\\s\\u{663}\\sand\\s(?:y\\u{306}){2}\\sand\\s(?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec![" "], "^\\s$"),
            case(vec!["  "], "^\\s\\s$"),
            case(vec!["   "], "^\\s{3}$"),
            case(vec![" ", "  ", "   "], "^(?:\\s\\s|\\s|\\s{3})$"),
            case(vec!["  ", "   ", "    "], "^(?:\\s\\s|\\s{3,4})$"),
            case(vec!["   ", "    ", "     "], "^\\s{3,5}$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}♥{3}\\s36\\sand\\s٣\\sand\\sy\u{306}y\u{306}\\sand\\s💩💩\\.$"
            )
        )]
        fn succeeds_with_increased_minimum_repetitions(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .with_minimum_repetitions(2)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec![""], "^$"),
            case(vec![" "], "^ $"),
            case(vec!["a"], "^\\w$"),
            case(vec!["1"], "^\\w$"),
            case(vec!["-1"], "^\\-\\w$"),
            case(vec!["1", "2"], "^\\w$"),
            case(vec!["ä", "ß"], "^\\w$"),
            case(vec!["abc", "1234"], "^\\w\\w\\w(?:\\w)?$"),
            case(vec!["١", "٣", "٥"], "^\\w$"), // Arabic digits: ١ = 1, ٣ = 3, ٥ = 5
            case(vec!["١٣٥"], "^\\w\\w\\w$"),
            case(vec!["a٣3", "b5٥"], "^\\w\\w\\w$"),
            case(vec!["I ♥ 123"], "^\\w ♥ \\w\\w\\w$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w   ♥♥♥ \\w\\w \\w\\w\\w \\w \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w 💩💩\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\w\\w \\w\\w\\w \\w \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\w\\w \\w\\w\\w \\w \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w {3}♥{3} \\w{2}(?: \\w{3} \\w){2}(?:\\w{3} ){2}💩{2}\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w {3}\\u{2665}{3} \\w{2}(?: \\w{3} \\w){2}(?:\\w{3} ){2}\\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w {3}\\u{2665}{3} \\w{2}(?: \\w{3} \\w){2}(?:\\w{3} ){2}(?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["a"], "^\\w$"),
            case(vec!["ab"], "^\\w\\w$"),
            case(vec!["abc"], "^\\w{3}$"),
            case(vec!["a", "ab", "abc"], "^(?:\\w\\w|\\w|\\w{3})$"),
            case(vec!["ab", "abc", "abcd"], "^(?:\\w\\w|\\w{3,4})$"),
            case(vec!["abc", "abcd", "abcde"], "^\\w{3,5}$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w {3}♥{3} \\w\\w \\w{3} \\w \\w{3} \\w{4} \\w{3} 💩💩\\.$"
            )
        )]
        fn succeeds_with_increased_minimum_repetitions(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_words()
                .with_minimum_repetitions(2)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod digit_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s\\s\\s♥♥♥\\s\\d\\d\\sand\\s\\d\\sand\\sy̆y̆\\sand\\s💩💩\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\sand\\s\\d\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\sand\\s\\d\\sand\\sy\\u{306}y\\u{306}\\sand\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}♥{3}\\s\\d(?:\\d\\sand\\s){2}(?:y̆){2}\\sand\\s💩{2}\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\sand\\s){2}(?:y\\u{306}){2}\\sand\\s\\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\sand\\s){2}(?:y\\u{306}){2}\\sand\\s(?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["1\n"], "^\\d\\s$"),
            case(vec!["1\n1\n"], "^\\d\\s\\d\\s$"),
            case(vec!["1\n1\n1\n"], "^(?:\\d\\s){3}$"),
            case(vec!["1\n", "1\n1\n", "1\n1\n1\n"], "^(?:\\d\\s\\d\\s|\\d\\s|(?:\\d\\s){3})$"),
            case(vec!["1\n1\n", "1\n1\n1\n", "1\n1\n1\n1\n"], "^(?:\\d\\s\\d\\s|(?:\\d\\s){3,4})$"),
            case(vec!["1\n1\n1\n", "1\n1\n1\n1\n", "1\n1\n1\n1\n1\n"], "^(?:\\d\\s){3,5}$"),
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\s{3}♥{3}\\s\\d\\d\\sand\\s\\d\\sand\\sy̆y̆\\sand\\s💩💩\\.$"
            )
        )]
        fn succeeds_with_increased_minimum_repetitions(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_minimum_repetitions(2)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["1\n1\n"], "^1\\n1\\n$"),
            case(vec!["1\n\n1\n\n"], "^(?:1\\n\\n){2}$")
        )]
        fn succeeds_with_increased_minimum_substring_length(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_minimum_substring_length(3)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["1\n1\n"], "^1\\n1\\n$"),
            case(vec!["1\n1\n1\n"], "^1\\n1\\n1\\n$"),
            case(vec!["1\n\n1\n\n"], "^1\\n\\n1\\n\\n$"),
            case(vec!["1\n\n1\n\n1\n\n"], "^(?:1\\n\\n){3}$")
        )]
        fn succeeds_with_increased_minimum_repetitions_and_substring_length(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_minimum_repetitions(2)
                .with_minimum_substring_length(3)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod digit_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w   ♥♥♥ \\d\\d \\w\\w\\w \\d \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w 💩💩\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\d\\d \\w\\w\\w \\d \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w   \\u{2665}\\u{2665}\\u{2665} \\d\\d \\w\\w\\w \\d \\w\\w\\w \\w\\w\\w\\w \\w\\w\\w \\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w {3}♥{3} \\d(?:\\d \\w{3} ){2}\\w(?:\\w{3} ){2}💩{2}\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w {3}\\u{2665}{3} \\d(?:\\d \\w{3} ){2}\\w(?:\\w{3} ){2}\\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w {3}\\u{2665}{3} \\d(?:\\d \\w{3} ){2}\\w(?:\\w{3} ){2}(?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }
}

mod space_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s\\s\\s♥♥♥\\s\\w\\w\\s\\w\\w\\w\\s\\w\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s💩💩\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\w\\w\\s\\w\\w\\w\\s\\w\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\w\\w\\s\\w\\w\\w\\s\\w\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s{3}♥{3}\\s\\w{2}(?:\\s\\w{3}\\s\\w){2}(?:\\w{3}\\s){2}💩{2}\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s{3}\\u{2665}{3}\\s\\w{2}(?:\\s\\w{3}\\s\\w){2}(?:\\w{3}\\s){2}\\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s{3}\\u{2665}{3}\\s\\w{2}(?:\\s\\w{3}\\s\\w){2}(?:\\w{3}\\s){2}(?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }
}

mod digit_space_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s\\s\\s♥♥♥\\s\\d\\d\\s\\w\\w\\w\\s\\d\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s💩💩\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\s\\w\\w\\w\\s\\d\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{1f4a9}\\u{1f4a9}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s\\s\\s\\u{2665}\\u{2665}\\u{2665}\\s\\d\\d\\s\\w\\w\\w\\s\\d\\s\\w\\w\\w\\s\\w\\w\\w\\w\\s\\w\\w\\w\\s\\u{d83d}\\u{dca9}\\u{d83d}\\u{dca9}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s{3}♥{3}\\s\\d(?:\\d\\s\\w{3}\\s){2}\\w(?:\\w{3}\\s){2}💩{2}\\.$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\s\\w{3}\\s){2}\\w(?:\\w{3}\\s){2}\\u{1f4a9}{2}\\.$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\s{3}\\u{2665}{3}\\s\\d(?:\\d\\s\\w{3}\\s){2}\\w(?:\\w{3}\\s){2}(?:\\u{d83d}\\u{dca9}){2}\\.$"
            )
        )]
        fn succeeds_with_escape_and_surrogate_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_whitespace()
                .with_conversion_of_words()
                .with_escaping_of_non_ascii_chars(true)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
        }
    }
}

mod non_digit_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D٣\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_digits()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D\\u{663}\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_digits()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^\\D{8}36\\D{5}٣\\D{17}$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_digits()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^\\D{8}36\\D{5}\\u{663}\\D{17}$")
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_digits()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod non_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\S   \\S\\S\\S \\S\\S \\S\\S\\S \\S \\S\\S\\S \\S\\S\\S\\S \\S\\S\\S \\S\\S\\S$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\S {3}\\S(?:\\S{2} ){2}\\S{3} (?:\\S(?: \\S{3}){2}){2}$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\W\\W\\W\\W\\W\\W\\W36\\Wand\\W٣\\Wand\\Wy̆y̆\\Wand\\W\\W\\W\\W$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\W\\W\\W\\W\\W\\W\\W36\\Wand\\W\\u{663}\\Wand\\Wy\\u{306}y\\u{306}\\Wand\\W\\W\\W\\W$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\W{7}36\\Wand\\W٣\\Wand\\W(?:y̆){2}\\Wand\\W{4}$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^I\\W{7}36\\Wand\\W\\u{663}\\Wand\\W(?:y\\u{306}){2}\\Wand\\W{4}$"
            )
        )]
        fn succeeds_with_escape_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_words()
                .with_escaping_of_non_ascii_chars(false)
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod non_digit_non_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_digits()
                .with_conversion_of_non_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^\\D{8}\\S{2}\\D{5}\\S\\D{17}$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_digits()
                .with_conversion_of_non_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod non_digit_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\D\\D\\D\\D\\D\\D\\D\\D36\\D\\D\\D\\D\\D٣\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_digits()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^\\D{8}36\\D{5}٣\\D{17}$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_digits()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod non_space_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\S\\W\\W\\W\\W\\W\\W\\W\\S\\S\\W\\S\\S\\S\\W\\S\\W\\S\\S\\S\\W\\S\\S\\S\\S\\W\\S\\S\\S\\W\\W\\W\\W$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_whitespace()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\S\\W{7}\\S(?:\\S\\W\\S{3}\\W){2}\\S{4}\\W\\S{3}\\W{4}$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_whitespace()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod non_digit_non_space_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\S\\S\\D\\D\\D\\D\\D\\S\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_non_digits()
                .with_conversion_of_non_whitespace()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^\\D{8}\\S{2}\\D{5}\\S\\D{17}$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_non_digits()
                .with_conversion_of_non_whitespace()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod digit_non_digit_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\D\\D\\D\\D\\D\\D\\D\\D\\d\\d\\D\\D\\D\\D\\D\\d\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D\\D$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_digits()
                .with_conversion_of_non_digits()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."], "^\\D{8}\\d{2}\\D{5}\\d\\D{17}$")
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_digits()
                .with_conversion_of_non_digits()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod space_non_space_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\S\\s\\s\\s\\S\\S\\S\\s\\S\\S\\s\\S\\S\\S\\s\\S\\s\\S\\S\\S\\s\\S\\S\\S\\S\\s\\S\\S\\S\\s\\S\\S\\S$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_whitespace()
                .with_conversion_of_non_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\S\\s{3}\\S(?:\\S{2}\\s){2}\\S{3}\\s(?:\\S(?:\\s\\S{3}){2}){2}$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_whitespace()
                .with_conversion_of_non_whitespace()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod word_non_word_conversion {
    use super::*;

    mod no_repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\W\\W\\W\\W\\W\\W\\W\\w\\w\\W\\w\\w\\w\\W\\w\\W\\w\\w\\w\\W\\w\\w\\w\\w\\W\\w\\w\\w\\W\\W\\W\\W$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_words()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod repetition {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(
                vec!["I   ♥♥♥ 36 and ٣ and y̆y̆ and 💩💩."],
                "^\\w\\W{7}\\w(?:\\w\\W\\w{3}\\W){2}\\w{4}\\W\\w{3}\\W{4}$"
            )
        )]
        fn succeeds(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_conversion_of_repetitions()
                .with_conversion_of_words()
                .with_conversion_of_non_words()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

mod anchor_conversion {
    use super::*;

    mod no_verbose {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec!["aaacaac", "aac"], "aa(?:acaa)?c$"),
            case(vec!["My ♥♥♥ and 💩💩 is yours."], "My ♥♥♥ and 💩💩 is yours\\.$"),
        )]
        fn succeeds_without_start_anchor_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .without_start_anchor()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["aaacaac", "aac"], "^aa(?:acaa)?c"),
            case(vec!["My ♥♥♥ and 💩💩 is yours."], "^My ♥♥♥ and 💩💩 is yours\\."),
        )]
        fn succeeds_without_end_anchor_option(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases)
                .without_end_anchor()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["bab", "b", "cb", "bba"], "(?:b(?:ba|ab)?|cb)"),
            case(vec!["a", "aba", "baaa", "aaab"], "(?:baaa|a(?:aab|ba)?)"),
            case(vec!["a", "abab", "bbb", "aaac"], "(?:a(?:bab|aac)?|bbb)"),
            case(vec!["aaacaac", "aac"], "aa(?:acaa)?c"),
            case(vec!["My ♥♥♥ and 💩💩 is yours."], "My ♥♥♥ and 💩💩 is yours\\."),
            case(
                // https://github.com/pemistahl/grex/issues/31
                vec!["agbhd", "eibcd", "egbcd", "fbjbf", "agbh", "eibc", "egbc", "ebc", "fbc", "cd", "f", "c", "abcd", "ebcd", "fbcd"],
                "(?:a(?:gbhd?|bcd)|e(?:ibcd?|gbcd?|bcd?)|f(?:b(?:jbf|cd?))?|cd?)"
            )
        )]
        fn succeeds_without_anchors(test_cases: Vec<&str>, expected_output: &str) {
            let regexp = RegExpBuilder::from(&test_cases).without_anchors().build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }

    mod verbose {
        use super::*;

        #[rstest(test_cases, expected_output,
            case(vec!["My ♥♥♥ and 💩💩 is yours."], indoc!(
                r#"
                (?x)
                  My\ ♥♥♥\ and\ 💩💩\ is\ yours\.
                $"#
            ))
        )]
        fn succeeds_with_verbose_mode_and_without_start_anchor_option(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_verbose_mode()
                .without_start_anchor()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["My ♥♥♥ and 💩💩 is yours."], indoc!(
                r#"
                (?x)
                ^
                  My\ ♥♥♥\ and\ 💩💩\ is\ yours\."#
            ))
        )]
        fn succeeds_with_verbose_mode_and_without_end_anchor_option(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_verbose_mode()
                .without_end_anchor()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }

        #[rstest(test_cases, expected_output,
            case(vec!["aaacaac", "aac"], indoc!(
                r#"
                (?x)
                  aa
                  (?:
                    acaa
                  )?
                  c"#
            )),
            case(vec!["My ♥♥♥ and 💩💩 is yours."], indoc!(
                r#"
                (?x)
                  My\ ♥♥♥\ and\ 💩💩\ is\ yours\."#
            ))
        )]
        fn succeeds_with_verbose_mode_and_without_anchors_option(
            test_cases: Vec<&str>,
            expected_output: &str,
        ) {
            let regexp = RegExpBuilder::from(&test_cases)
                .with_verbose_mode()
                .without_anchors()
                .build();
            assert_that_regexp_is_correct(regexp, expected_output, &test_cases);
            assert_that_regexp_matches_test_cases(expected_output, test_cases);
        }
    }
}

fn assert_that_regexp_is_correct(regexp: String, expected_output: &str, test_cases: &[&str]) {
    assert_eq!(
        regexp, expected_output,
        "\n\ninput: {:?}\nexpected: {}\nactual: {}\n\n",
        test_cases, expected_output, regexp
    );
}

fn assert_that_regexp_matches_test_cases(expected_output: &str, test_cases: Vec<&str>) {
    let regexp = Regex::new(expected_output).unwrap();
    for test_case in test_cases {
        let substrings = regexp
            .find_iter(test_case)
            .map(|m| m.as_str())
            .collect::<Vec<_>>();

        assert_eq!(
            substrings.len(),
            1,
            "expression '{}' does not match test case '{}' entirely but {} of its substrings: {:?}",
            expected_output,
            test_case,
            substrings.len(),
            substrings
        );
    }
}
```

## File: `tests/property_tests.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#![cfg(not(target_family = "wasm"))]

use grex::RegExpBuilder;
use proptest::prelude::*;
use regex::{Error, Regex, RegexBuilder};

proptest! {
    #![proptest_config(ProptestConfig::with_cases(500))]

    #[test]
    fn valid_regexes_with_default_settings(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec).build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_case_insensitive_matching(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_case_insensitive_matching()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_case_insensitive_matching_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_case_insensitive_matching()
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_escape_sequences(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_escaping_of_non_ascii_chars(false)
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_escape_sequences_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_escaping_of_non_ascii_chars(false)
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_digits(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_digits()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_digits_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_digits()
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_non_digits(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_digits()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_non_digits_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_digits()
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_whitespace(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_whitespace()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_whitespace_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_whitespace()
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_non_whitespace(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_whitespace()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_non_whitespace_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_whitespace()
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_words(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_words()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_words_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_words()
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_non_words(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_words()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_non_words_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_words()
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_repetitions(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5),
        minimum_repetitions in 1..100u32,
        minimum_substring_length in 1..100u32
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_repetitions()
            .with_minimum_repetitions(minimum_repetitions)
            .with_minimum_substring_length(minimum_substring_length)
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn valid_regexes_with_conversion_of_repetitions_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5),
        minimum_repetitions in 1..100u32,
        minimum_substring_length in 1..100u32
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_repetitions()
            .with_minimum_repetitions(minimum_repetitions)
            .with_minimum_substring_length(minimum_substring_length)
            .with_verbose_mode()
            .build();
        prop_assert!(compile_regexp(&regexp).is_ok());
    }

    #[test]
    fn matching_regexes_with_default_settings(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec).build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_case_insensitive_matching(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_case_insensitive_matching()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_case_insensitive_matching_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_case_insensitive_matching()
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_escape_sequences(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_escaping_of_non_ascii_chars(false)
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_escape_sequences_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_escaping_of_non_ascii_chars(false)
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_digits(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_digits()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_digits_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_digits()
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_non_digits(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_digits()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_non_digits_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_digits()
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_whitespace(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_whitespace()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_whitespace_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_whitespace()
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_non_whitespace(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_whitespace()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_non_whitespace_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_whitespace()
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_words(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_words()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_words_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_words()
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_non_words(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_words()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_non_words_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_non_words()
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_repetitions(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5),
        minimum_repetitions in 1..100u32,
        minimum_substring_length in 1..100u32
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_repetitions()
            .with_minimum_repetitions(minimum_repetitions)
            .with_minimum_substring_length(minimum_substring_length)
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_with_conversion_of_repetitions_and_verbose_mode(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5),
        minimum_repetitions in 1..100u32,
        minimum_substring_length in 1..100u32
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec)
            .with_conversion_of_repetitions()
            .with_minimum_repetitions(minimum_repetitions)
            .with_minimum_substring_length(minimum_substring_length)
            .with_verbose_mode()
            .build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            prop_assert!(test_cases.iter().all(|test_case| compiled_regexp.is_match(test_case)));
        }
    }

    #[test]
    fn matching_regexes_without_start_anchor(
        test_cases in prop::collection::hash_set("[A-C]{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec).without_start_anchor().build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            for test_case in test_cases_vec {
                let substrings = compiled_regexp.find_iter(&test_case).map(|m| m.as_str()).collect::<Vec<_>>();
                prop_assert_eq!(
                    substrings.len(),
                    1,
                    "expression '{}' does not match test case '{}' entirely but {} of its substrings: {:?}",
                    regexp,
                    test_case,
                    substrings.len(),
                    substrings
                );
            }
        }
    }

    #[test]
    fn matching_regexes_without_end_anchor(
        test_cases in prop::collection::hash_set("[A-C]{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec).without_end_anchor().build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            for test_case in test_cases_vec {
                let substrings = compiled_regexp.find_iter(&test_case).map(|m| m.as_str()).collect::<Vec<_>>();
                prop_assert_eq!(
                    substrings.len(),
                    1,
                    "expression '{}' does not match test case '{}' entirely but {} of its substrings: {:?}",
                    regexp,
                    test_case,
                    substrings.len(),
                    substrings
                );
            }
        }
    }

    #[test]
    fn matching_regexes_without_anchors(
        test_cases in prop::collection::hash_set("[A-C]{1,10}", 1..=5)
    ) {
        let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
        let regexp = RegExpBuilder::from(&test_cases_vec).without_anchors().build();
        if let Ok(compiled_regexp) = compile_regexp(&regexp) {
            for test_case in test_cases_vec {
                let substrings = compiled_regexp.find_iter(&test_case).map(|m| m.as_str()).collect::<Vec<_>>();
                prop_assert_eq!(
                    substrings.len(),
                    1,
                    "expression '{}' does not match test case '{}' entirely but {} of its substrings: {:?}",
                    regexp,
                    test_case,
                    substrings.len(),
                    substrings
                );
            }
        }
    }

    #[test]
    fn regexes_not_matching_other_strings_with_default_settings(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5),
        other_strings in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        if test_cases.is_disjoint(&other_strings) {
            let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
            let regexp = RegExpBuilder::from(&test_cases_vec).build();
            if let Ok(compiled_regexp) = compile_regexp(&regexp) {
                prop_assert!(other_strings.iter().all(|other_string| !compiled_regexp.is_match(other_string)));
            }
        }
    }

    #[test]
    fn regexes_not_matching_other_strings_with_escape_sequences(
        test_cases in prop::collection::hash_set(".{1,10}", 1..=5),
        other_strings in prop::collection::hash_set(".{1,10}", 1..=5)
    ) {
        if test_cases.is_disjoint(&other_strings) {
            let test_cases_vec = test_cases.iter().cloned().collect::<Vec<_>>();
            let regexp = RegExpBuilder::from(&test_cases_vec)
                .with_escaping_of_non_ascii_chars(false)
                .build();
            if let Ok(compiled_regexp) = compile_regexp(&regexp) {
                prop_assert!(other_strings.iter().all(|other_string| !compiled_regexp.is_match(other_string)));
            }
        }
    }
}

fn compile_regexp(regexp: &str) -> Result<Regex, Error> {
    RegexBuilder::new(regexp).size_limit(20000000).build()
}
```

## File: `tests/wasm_browser_tests.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#![cfg(target_family = "wasm")]

use grex::WasmRegExpBuilder;
use indoc::indoc;
use wasm_bindgen::JsValue;
use wasm_bindgen_test::*;

wasm_bindgen_test::wasm_bindgen_test_configure!(run_in_browser);

#[wasm_bindgen_test]
fn assert_regexpbuilder_succeeds() {
    let test_cases = Box::new([JsValue::from("hello"), JsValue::from("world")]);
    let builder = WasmRegExpBuilder::from(test_cases);
    assert!(builder.is_ok());
    let regexp = builder.unwrap().build();
    assert_eq!(regexp, "^(?:hello|world)$");
}

#[wasm_bindgen_test]
fn assert_regexpbuilder_fails() {
    let builder = WasmRegExpBuilder::from(Box::new([]));
    assert_eq!(
        builder.err(),
        Some(JsValue::from(
            "No test cases have been provided for regular expression generation"
        ))
    );
}

#[wasm_bindgen_test]
fn test_conversion_of_digits() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfDigits()
        .build();
    assert_eq!(regexp, "^(?:abc  |\\d\\d\\d)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_non_digits() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfNonDigits()
        .build();
    assert_eq!(regexp, "^(?:\\D\\D\\D\\D\\D|123)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_whitespace() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfWhitespace()
        .build();
    assert_eq!(regexp, "^(?:abc\\s\\s|123)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_non_whitespace() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfNonWhitespace()
        .build();
    assert_eq!(regexp, "^\\S\\S\\S(?:  )?$");
}

#[wasm_bindgen_test]
fn test_conversion_of_words() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfWords()
        .build();
    assert_eq!(regexp, "^\\w\\w\\w(?:  )?$");
}

#[wasm_bindgen_test]
fn test_conversion_of_non_words() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfNonWords()
        .build();
    assert_eq!(regexp, "^(?:abc\\W\\W|123)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_repetitions() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfRepetitions()
        .build();
    assert_eq!(regexp, "^(?:abc {2}|123)$");
}

#[wasm_bindgen_test]
fn test_case_insensitive_matching() {
    let test_cases = Box::new([
        JsValue::from("ABC"),
        JsValue::from("abc  "),
        JsValue::from("123"),
    ]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withCaseInsensitiveMatching()
        .build();
    assert_eq!(regexp, "(?i)^(?:abc(?:  )?|123)$");
}

#[wasm_bindgen_test]
fn test_capturing_groups() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withCapturingGroups()
        .build();
    assert_eq!(regexp, "^(abc  |123)$");
}

#[wasm_bindgen_test]
fn test_escaping_of_non_ascii_chars() {
    let test_cases = Box::new([
        JsValue::from("abc  "),
        JsValue::from("123"),
        JsValue::from("♥"),
    ]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withEscapingOfNonAsciiChars(false)
        .build();
    assert_eq!(regexp, "^(?:abc  |123|\\u{2665})$");
}

#[wasm_bindgen_test]
fn test_verbose_mode() {
    let test_cases = Box::new([
        JsValue::from("abc  "),
        JsValue::from("123"),
        JsValue::from("♥"),
    ]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withVerboseMode()
        .build();
    assert_eq!(
        regexp,
        indoc!(
            r#"
            (?x)
            ^
              (?:
                abc\ \ 
                |
                123
                |
                ♥
              )
            $"#
        )
    );
}

#[wasm_bindgen_test]
fn test_without_start_anchor() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withoutStartAnchor()
        .build();
    assert_eq!(regexp, "(?:abc  |123)$");
}

#[wasm_bindgen_test]
fn test_without_end_anchor() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withoutEndAnchor()
        .build();
    assert_eq!(regexp, "^(?:abc  |123)");
}

#[wasm_bindgen_test]
fn test_without_anchors() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withoutAnchors()
        .build();
    assert_eq!(regexp, "(?:abc  |123)");
}

#[wasm_bindgen_test]
fn test_minimum_repetitions() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let builder = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withMinimumRepetitions(0);
    assert_eq!(
        builder.err(),
        Some(JsValue::from(
            "Quantity of minimum repetitions must be greater than zero"
        ))
    );
}

#[wasm_bindgen_test]
fn test_minimum_substring_length() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let builder = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withMinimumSubstringLength(0);
    assert_eq!(
        builder.err(),
        Some(JsValue::from(
            "Minimum substring length must be greater than zero"
        ))
    );
}
```

## File: `tests/wasm_node_tests.rs`
```rust
/*
 * Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#![cfg(target_family = "wasm")]

use grex::WasmRegExpBuilder;
use indoc::indoc;
use wasm_bindgen::JsValue;
use wasm_bindgen_test::*;

#[wasm_bindgen_test]
fn assert_regexpbuilder_succeeds() {
    let test_cases = Box::new([JsValue::from("hello"), JsValue::from("world")]);
    let builder = WasmRegExpBuilder::from(test_cases);
    assert!(builder.is_ok());
    let regexp = builder.unwrap().build();
    assert_eq!(regexp, "^(?:hello|world)$");
}

#[wasm_bindgen_test]
fn assert_regexpbuilder_fails() {
    let builder = WasmRegExpBuilder::from(Box::new([]));
    assert_eq!(
        builder.err(),
        Some(JsValue::from(
            "No test cases have been provided for regular expression generation"
        ))
    );
}

#[wasm_bindgen_test]
fn test_conversion_of_digits() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfDigits()
        .build();
    assert_eq!(regexp, "^(?:abc  |\\d\\d\\d)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_non_digits() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfNonDigits()
        .build();
    assert_eq!(regexp, "^(?:\\D\\D\\D\\D\\D|123)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_whitespace() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfWhitespace()
        .build();
    assert_eq!(regexp, "^(?:abc\\s\\s|123)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_non_whitespace() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfNonWhitespace()
        .build();
    assert_eq!(regexp, "^\\S\\S\\S(?:  )?$");
}

#[wasm_bindgen_test]
fn test_conversion_of_words() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfWords()
        .build();
    assert_eq!(regexp, "^\\w\\w\\w(?:  )?$");
}

#[wasm_bindgen_test]
fn test_conversion_of_non_words() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfNonWords()
        .build();
    assert_eq!(regexp, "^(?:abc\\W\\W|123)$");
}

#[wasm_bindgen_test]
fn test_conversion_of_repetitions() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withConversionOfRepetitions()
        .build();
    assert_eq!(regexp, "^(?:abc {2}|123)$");
}

#[wasm_bindgen_test]
fn test_case_insensitive_matching() {
    let test_cases = Box::new([
        JsValue::from("ABC"),
        JsValue::from("abc  "),
        JsValue::from("123"),
    ]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withCaseInsensitiveMatching()
        .build();
    assert_eq!(regexp, "(?i)^(?:abc(?:  )?|123)$");
}

#[wasm_bindgen_test]
fn test_capturing_groups() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withCapturingGroups()
        .build();
    assert_eq!(regexp, "^(abc  |123)$");
}

#[wasm_bindgen_test]
fn test_escaping_of_non_ascii_chars() {
    let test_cases = Box::new([
        JsValue::from("abc  "),
        JsValue::from("123"),
        JsValue::from("♥"),
    ]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withEscapingOfNonAsciiChars(false)
        .build();
    assert_eq!(regexp, "^(?:abc  |123|\\u{2665})$");
}

#[wasm_bindgen_test]
fn test_verbose_mode() {
    let test_cases = Box::new([
        JsValue::from("abc  "),
        JsValue::from("123"),
        JsValue::from("♥"),
    ]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withVerboseMode()
        .build();
    assert_eq!(
        regexp,
        indoc!(
            r#"
            (?x)
            ^
              (?:
                abc\ \ 
                |
                123
                |
                ♥
              )
            $"#
        )
    );
}

#[wasm_bindgen_test]
fn test_without_start_anchor() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withoutStartAnchor()
        .build();
    assert_eq!(regexp, "(?:abc  |123)$");
}

#[wasm_bindgen_test]
fn test_without_end_anchor() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withoutEndAnchor()
        .build();
    assert_eq!(regexp, "^(?:abc  |123)");
}

#[wasm_bindgen_test]
fn test_without_anchors() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let regexp = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withoutAnchors()
        .build();
    assert_eq!(regexp, "(?:abc  |123)");
}

#[wasm_bindgen_test]
fn test_minimum_repetitions() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let builder = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withMinimumRepetitions(0);
    assert_eq!(
        builder.err(),
        Some(JsValue::from(
            "Quantity of minimum repetitions must be greater than zero"
        ))
    );
}

#[wasm_bindgen_test]
fn test_minimum_substring_length() {
    let test_cases = Box::new([JsValue::from("abc  "), JsValue::from("123")]);
    let builder = WasmRegExpBuilder::from(test_cases)
        .unwrap()
        .withMinimumSubstringLength(0);
    assert_eq!(
        builder.err(),
        Some(JsValue::from(
            "Minimum substring length must be greater than zero"
        ))
    );
}
```

## File: `tests/python/test_grex.py`
```python
#
# Copyright © 2019-today Peter M. Stahl pemistahl@gmail.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import inspect
import pytest
import re

from grex import RegExpBuilder


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["abc", "abd", "abe"], "^ab[c-e]$"),
    ]
)
def test_default_settings(test_cases, expected_pattern):
    pattern = RegExpBuilder.from_test_cases(test_cases).build()
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["My ♥ and 💩 is yours."], "^My \\u2665 and \\U0001f4a9 is yours\\.$"),
    ]
)
def test_escaping(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_escaping_of_non_ascii_chars(use_surrogate_pairs=False)
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["My ♥ and 💩 is yours."], "^My \\u2665 and \\ud83d\\udca9 is yours\\.$"),
    ]
)
def test_escaping_with_surrogate_pairs(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_escaping_of_non_ascii_chars(use_surrogate_pairs=True)
               .build())
    assert pattern == expected_pattern
    # module re does not support matching surrogate pairs


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["efgh", "abcxy", "abcw"], "^(abc(xy|w)|efgh)$"),
    ]
)
def test_capturing_groups(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_capturing_groups()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["efgh", "abcxy", "abcw"], "(?:abc(?:xy|w)|efgh)"),
    ]
)
def test_without_anchors(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .without_anchors()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["ABC", "zBC", "abc", "AbC", "aBc"], "(?i)^[az]bc$"),
    ]
)
def test_case_insensitive_matching(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_case_insensitive_matching()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(
            ["[a-z]", "(d,e,f)"],
            inspect.cleandoc("""
                (?x)
                ^
                  (?:
                    \\(d,e,f\\)
                    |
                    \\[a\\-z\\]
                  )
                $
                """)
        ),
    ]
)
def test_verbose_mode(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_verbose_mode()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(
            ["Ä@Ö€Ü", "ä@ö€ü", "Ä@ö€Ü", "ä@Ö€ü"],
            inspect.cleandoc("""
                (?ix)
                ^
                  ä@ö€ü
                $
                """)
        )
    ]
)
def test_case_insensitive_matching_and_verbose_mode(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_case_insensitive_matching()
               .with_verbose_mode()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["a", "b\nx\nx", "c"], "^(?:b(?:\\nx){2}|[ac])$"),
    ]
)
def test_conversion_of_repetitions(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_repetitions()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["My ♥♥♥ and 💩💩 is yours."], "^My \\u2665{3} and \\U0001f4a9{2} is yours\\.$"),
    ]
)
def test_escaping_and_conversion_of_repetitions(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_escaping_of_non_ascii_chars(use_surrogate_pairs=False)
               .with_conversion_of_repetitions()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["a1b2c3"], "^a\\db\\dc\\d$"),
    ]
)
def test_conversion_of_digits(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_digits()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["a1b2c3"], "^\\D1\\D2\\D3$"),
    ]
)
def test_conversion_of_non_digits(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_non_digits()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["\n\t", "\r"], "^\\s(?:\\s)?$"),
    ]
)
def test_conversion_of_whitespace(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_whitespace()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["a1 b2 c3"], "^\\S\\S \\S\\S \\S\\S$"),
    ]
)
def test_conversion_of_non_whitespace(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_non_whitespace()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["abc", "1234"], "^\\w\\w\\w(?:\\w)?$"),
    ]
)
def test_conversion_of_words(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_words()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["abc 1234"], "^abc\\W1234$"),
    ]
)
def test_conversion_of_non_words(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_non_words()
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["aababab"], "^aababab$"),
        pytest.param(["aabababab"], "^a(?:ab){4}$")
    ]
)
def test_minimum_repetitions(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_repetitions()
               .with_minimum_repetitions(3)
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


@pytest.mark.parametrize(
    "test_cases,expected_pattern",
    [
        pytest.param(["ababab"], "^ababab$"),
        pytest.param(["abcabcabc"], "^(?:abc){3}$")
    ]
)
def test_minimum_substring_length(test_cases, expected_pattern):
    pattern = (RegExpBuilder.from_test_cases(test_cases)
               .with_conversion_of_repetitions()
               .with_minimum_substring_length(3)
               .build())
    assert pattern == expected_pattern
    for test_case in test_cases:
        assert re.match(pattern, test_case)


def test_error_for_empty_test_cases():
    with pytest.raises(ValueError) as exception_info:
        RegExpBuilder.from_test_cases([])
    assert (
        exception_info.value.args[0] ==
        "No test cases have been provided for regular expression generation"
    )


def test_error_for_invalid_minimum_repetitions():
    with pytest.raises(ValueError) as exception_info:
        RegExpBuilder.from_test_cases(["abcd"]).with_minimum_repetitions(-4)
    assert (
        exception_info.value.args[0] ==
        "Quantity of minimum repetitions must be greater than zero"
    )


def test_error_for_invalid_minimum_substring_length():
    with pytest.raises(ValueError) as exception_info:
        RegExpBuilder.from_test_cases(["abcd"]).with_minimum_substring_length(-2)
    assert (
        exception_info.value.args[0] ==
        "Minimum substring length must be greater than zero"
    )
```

