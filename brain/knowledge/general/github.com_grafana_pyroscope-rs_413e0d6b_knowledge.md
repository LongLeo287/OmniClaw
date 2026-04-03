---
id: github.com-grafana-pyroscope-rs-413e0d6b-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:04.537220
---

# KNOWLEDGE EXTRACT: github.com_grafana_pyroscope-rs_413e0d6b
> **Extracted on:** 2026-04-01 15:40:51
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007524680/github.com_grafana_pyroscope-rs_413e0d6b

---

## File: `.dockerignore`
```
**/target/
**/pkg/
**/dist/
**/build/
**/*egg-info*/
**/**/Makefile
*.so*
*.gem
```

## File: `.gitignore`
```
build/
dist/

.venv/
.env/

.idea/
/target/
**/*.rs.bk
.cache
.DS_Store

flamegraph.svg
perf.data
perf.data.*
```

## File: `.tool-versions`
```
ruby 4.0.1
```

## File: `CHANGELOG.md`
```markdown
# v2.0.0

## Breaking Changes
- `Backend::report()` now returns `ReportBatch` instead of `Vec<Report>` ([#437](https://github.com/grafana/pyroscope-rs/pull/437), [#447](https://github.com/grafana/pyroscope-rs/pull/447))
- New `ReportData` enum replaces the plain `Vec<Report>` in `ReportBatch`, supporting both structured reports (`ReportData::Reports`) and pre-encoded pprof bytes (`ReportData::RawPprof`) ([#447](https://github.com/grafana/pyroscope-rs/pull/447))
- Minimum supported Rust version bumped from 1.64 to 1.66

## New Features
- **Jemalloc memory profiling backend** — new `backend-jemalloc` feature flag enables heap profiling via `jemalloc_pprof`. Use `pyroscope::backend::jemalloc::jemalloc_backend()` to get started ([#378](https://github.com/grafana/pyroscope-rs/pull/378))
- **`ReportBatch` type** — backends now return a `ReportBatch` with a `profile_type` field (e.g. `"process_cpu"`, `"memory"`), enabling multi-profile support ([#437](https://github.com/grafana/pyroscope-rs/pull/437))

## Dependencies
- Updated `pprof` (pprof-pyroscope-fork) to v0.1500.3 ([#407](https://github.com/grafana/pyroscope-rs/pull/407))
- Updated `object` crate to 0.38 ([#430](https://github.com/grafana/pyroscope-rs/pull/430))
- Disabled py-spy default features to exclude CLI dependencies ([#418](https://github.com/grafana/pyroscope-rs/pull/418))
- Added `jemalloc_pprof` 0.8 and `tokio` 1 as workspace dependencies

# v1.0.0
## Breaking Changes
- Removed `auth_token` from Python and Ruby FFI bindings and related code
- Removed `detect_subprocesses` from Python and Ruby configs
- Config constructor now requires app/spy identity and sample rate inputs
- Removed support for collapsed format
- Removed global tags from ruleset

## New Features
- Integrated pprof-rs backend into main crate behind optional `backend-pprof-rs` feature
- Switched to push API (from `/ingest` to `/push`)
- Generated push API protos
- Added `ThreadId` type
- Added `rustls-no-provider` TLS feature

## Bug Fixes / Improvements
- Unified signal logic
- Report cleanup functions
- Optimized ruleset
- Removed obscure thread id hash check
- Ruby: inline thread_id crate; remove detect_subprocess
- Dependency updates (reqwest 0.13, prost 0.14, thiserror 2.0, serde_json 1.0.115, uuid 1.20, libflate 2.1)

# v0.5.4
## New Features
- Add report transfromation function which allows changing the report before
  sending it to the Pyroscope Server.
- Add Gzip support.

## Bug Fixes
- Use URL Builder. ([786c89b](https://github.com/pyroscope-io/pyroscope-rs/commit/786c89bb99839c45778410012a6da60267d395df))

# v0.5.3
## New Features
- Add BackendConfig to make reporting of pid, thread_id and thread_name
  optional. 
- Backends can add a suffix to the "application_name"

## Bug Fixes
- **main**: fixed an obsecure bug when counting stacktraces ([Abid Omar](https://github.com/pyroscope-io/pyroscope-rs/commit/bdecaa13aeae3ce7d4c3d97f88bdd104ec35e7c5))

# v0.5.2
## New features
- Authentication Token support

## API Changes
- use rust-tls instead of openssl

# v0.5.1
## API Changes
- Backend shutdown bug
- Docs update

# v0.5.0
## API Changes
- New API for building, starting and stopping the profiling agent.
- Backend supports reporting multiple threads.
- Tagging within local thread-scope

# v0.4.0
## API Changes
- Backend now support passing a configuration struct.
- TimerSignal enum
- pprof-rs backend is split into a different package. It has to be imported manually.

## What's Changed
* fix: avoid binding two unrelated vars to the same type by @drahnr in https://github.com/pyroscope-io/pyroscope-rs/pull/18
* avoid almost all unwraps by @drahnr in https://github.com/pyroscope-io/pyroscope-rs/pull/14
* use more features of `thiserror` by @drahnr in https://github.com/pyroscope-io/pyroscope-rs/pull/11
* introduce LOG_TAGs, avoid repetitive prefixes by @drahnr in https://github.com/pyroscope-io/pyroscope-rs/pull/10
* allow configurable accumulation_cycle by @drahnr in https://github.com/pyroscope-io/pyroscope-rs/pull/21
* Add CI Targets by @omarabid in https://github.com/pyroscope-io/pyroscope-rs/pull/22
* 0.4.0 release by @omarabid in https://github.com/pyroscope-io/pyroscope-rs/pull/23

## New Contributors
* @drahnr made their first contribution in https://github.com/pyroscope-io/pyroscope-rs/pull/18

**Full Changelog**: https://github.com/pyroscope-io/pyroscope-rs/compare/0.3.1...lib-0.4.0

# v0.3.1
Minor release with bug fixes.

## Bug Fixes
- **session**: avoid breaking SessionManager if request fails ([Abid Omar](https://github.com/pyroscope-io/pyroscope-rs/commit/1254bcc9a3b0d76b7adbeb82ba21f33b875c0b39))
- **typo**: variable name typo ([Abid Omar](https://github.com/pyroscope-io/pyroscope-rs/commit/0d8caffbe7855bec8158333dba2923cd07286a5f))
- **pprof**: fix #12 ([Abid Omar](https://github.com/pyroscope-io/pyroscope-rs/commit/936d3d99a2cc82812bc8251fd2fbf8152a87d4cb))
- **copyright**: fix #13 ([Abid Omar](https://github.com/pyroscope-io/pyroscope-rs/commit/b8eaf13137810df932e1b70e33b3ad3e25b65ece))

## Code Refactoring
- **option**: replace unwrap for various Options ([Abid Omar](https://github.com/pyroscope-io/pyroscope-rs/commit/3fd4e794d74523855c66f65c0b7fc8ff9dfe4604))
- **time**: add get_time_range ([Abid Omar](https://github.com/pyroscope-io/pyroscope-rs/commit/a6d4dbcef494b2bfe8016a817201499937cf3528))

# v0.3.0
First stable release

# v0.0.2-alpha
Second beta release

# v0.0.1-alpha
Initial beta release
```

## File: `CLAUDE.md`
```markdown
# pyroscope-rs

# Generated Files

Files in `kit/python_offsets_types/src/` (e.g. `py314.rs`, `py313.rs`) are **generated by `kit/python_offsets/gen_debug_offsets.sh`** using bindgen. **Never edit these files manually.** To update them, re-run the generator:

```bash
cd kit/python_offsets
./gen_debug_offsets.sh v3.14.0 py314
```

# Build & Packaging

When adding new workspace crates or source directories needed for Rust compilation, update ALL of these:
- `MANIFEST.in` — include Cargo.toml and source files so Python sdist contains them
- `docker/wheel.Dockerfile` — ADD the directory for Python manylinux wheel builds
- `docker/wheel-musllinux.Dockerfile` — ADD the directory for Python musllinux wheel builds
- `docker/gem.Dockerfile` — ADD the directory for Ruby gem builds

All three Dockerfiles and the MANIFEST.in must stay in sync with workspace members in the root `Cargo.toml`.

# Pre-Commit Checks

Before committing, always run:

```bash
cargo fmt --all
cargo clippy --all-targets --all-features -- -D warnings
for manifest in kit/*/Cargo.toml; do
    cargo test --manifest-path "$manifest"
done
```

All must pass with no errors before creating a commit.
```

## File: `CODEOWNERS`
```
* @grafana/pyroscope-rs @grafana/pyroscope-team
```

## File: `CODE_OF_CONDUCT.md`
```markdown
# Contributor Covenant Code of Conduct

## Our Pledge

We as members, contributors, and leaders pledge to make participation in our
community a harassment-free experience for everyone, regardless of age, body
size, visible or invisible disability, ethnicity, sex characteristics, gender
identity and expression, level of experience, education, socio-economic status,
nationality, personal appearance, race, religion, or sexual identity
and orientation.

We pledge to act and interact in ways that contribute to an open, welcoming,
diverse, inclusive, and healthy community.

## Our Standards

Examples of behavior that contributes to a positive environment for our
community include:

* Demonstrating empathy and kindness toward other people
* Being respectful of differing opinions, viewpoints, and experiences
* Giving and gracefully accepting constructive feedback
* Accepting responsibility and apologizing to those affected by our mistakes,
  and learning from the experience
* Focusing on what is best not just for us as individuals, but for the
  overall community

Examples of unacceptable behavior include:

* The use of sexualized language or imagery, and sexual attention or
  advances of any kind
* Trolling, insulting or derogatory comments, and personal or political attacks
* Public or private harassment
* Publishing others' private information, such as a physical or email
  address, without their explicit permission
* Other conduct which could reasonably be considered inappropriate in a
  professional setting

## Enforcement Responsibilities

Community leaders are responsible for clarifying and enforcing our standards of
acceptable behavior and will take appropriate and fair corrective action in
response to any behavior that they deem inappropriate, threatening, offensive,
or harmful.

Community leaders have the right and responsibility to remove, edit, or reject
comments, commits, code, wiki edits, issues, and other contributions that are
not aligned to this Code of Conduct, and will communicate reasons for moderation
decisions when appropriate.

## Scope

This Code of Conduct applies within all community spaces, and also applies when
an individual is officially representing the community in public spaces.
Examples of representing our community include using an official e-mail address,
posting via an official social media account, or acting as an appointed
representative at an online or offline event.

## Enforcement

Instances of abusive, harassing, or otherwise unacceptable behavior may be
reported to the community leaders responsible for enforcement at
conduct@pyroscope.io.
All complaints will be reviewed and investigated promptly and fairly.

All community leaders are obligated to respect the privacy and security of the
reporter of any incident.

## Enforcement Guidelines

Community leaders will follow these Community Impact Guidelines in determining
the consequences for any action they deem in violation of this Code of Conduct:

### 1. Correction

**Community Impact**: Use of inappropriate language or other behavior deemed
unprofessional or unwelcome in the community.

**Consequence**: A private, written warning from community leaders, providing
clarity around the nature of the violation and an explanation of why the
behavior was inappropriate. A public apology may be requested.

### 2. Warning

**Community Impact**: A violation through a single incident or series
of actions.

**Consequence**: A warning with consequences for continued behavior. No
interaction with the people involved, including unsolicited interaction with
those enforcing the Code of Conduct, for a specified period of time. This
includes avoiding interactions in community spaces as well as external channels
like social media. Violating these terms may lead to a temporary or
permanent ban.

### 3. Temporary Ban

**Community Impact**: A serious violation of community standards, including
sustained inappropriate behavior.

**Consequence**: A temporary ban from any sort of interaction or public
communication with the community for a specified period of time. No public or
private interaction with the people involved, including unsolicited interaction
with those enforcing the Code of Conduct, is allowed during this period.
Violating these terms may lead to a permanent ban.

### 4. Permanent Ban

**Community Impact**: Demonstrating a pattern of violation of community
standards, including sustained inappropriate behavior,  harassment of an
individual, or aggression toward or disparagement of classes of individuals.

**Consequence**: A permanent ban from any sort of public interaction within
the community.

## Attribution

This Code of Conduct is adapted from the [Contributor Covenant][homepage],
version 2.0, available at
[https://www.contributor-covenant.org/version/2/0/code_of_conduct.html][v2.0].

Community Impact Guidelines were inspired by
[Mozilla's code of conduct enforcement ladder][Mozilla CoC].

For answers to common questions about this code of conduct, see the FAQ at
[https://www.contributor-covenant.org/faq][FAQ]. Translations are available
at [https://www.contributor-covenant.org/translations][translations].

[homepage]: https://www.contributor-covenant.org
[v2.0]: https://www.contributor-covenant.org/version/2/0/code_of_conduct.html
[Mozilla CoC]: https://github.com/mozilla/diversity
[FAQ]: https://www.contributor-covenant.org/faq
[translations]: https://www.contributor-covenant.org/translations
```

## File: `CONTRIBUTING.md`
```markdown
# Contributing to Pyroscope

Thank you for your interest in contributing to Pyroscope! We welcome all people who want to contribute in a healthy and constructive manner within our community. To help us create a safe and positive community experience for all, we require all participants to adhere to the [Code of Conduct](CODE_OF_CONDUCT.md).

This document is a guide to help you through the process of contributing to Pyroscope.

## Where do I start

* Set up your [development environment](https://pyroscope.io/docs/developer-guide).
* Read the [style guides](https://pyroscope.io/docs/style-guide) we use.
* Check out the list of [good first issues](https://github.com/pyroscope-io/pyroscope/issues?q=is%3Aissue+is%3Aopen+label%3A%22good+first+issue%22).

## Maintainers

This package is maintained by [@grafana/pyroscope-rs](https://github.com/orgs/grafana/teams/pyroscope-rs).
Mention this team on issues or PRs for feedback.
```

## File: `Cargo.toml`
```
[package]
name = "pyroscope"
description = """
Pyroscope Profiler Agent for continuous profiling of Rust, Python and Ruby applications.
"""
keywords = ["pyroscope", "profiler", "profiling", "pprof"]
authors = ["Abid Omar <contact@omarabid.com>"]
version = "2.0.0"
edition = "2021"
license = "Apache-2.0"
homepage = "https://pyroscope.io/docs/rust"
documentation  = "https://docs.rs/pyroscope"
repository = "https://github.com/pyroscope-io/pyroscope-rs"
readme = "README.md"
autobins = false
autoexamples = true
autotests = true
autobenches = true
rust-version = "1.66"

[workspace]
members = [
    "pyroscope_ffi/ruby/ext/rbspy",
    "pyroscope_ffi/python/rust",
    "kit/kindasafe",
    "kit/kindasafe_init",
    "kit/sighandler",
    "kit/pyroscope_ingest",
    "kit/pprof_enc",
    "kit/notlibc",
    "kit/python_offsets",
    "kit/python_offsets_types",
    "kit/python_unwind",
    "kit/coredump",
    "kit/sig_ring",
    "kit/pysignalprof",
    "kit/pysignalprof_capi",
]

[workspace.dependencies]
thiserror = "2.0.12"
log = "0.4"
names = { version = "0.14.0", default-features = false }
reqwest = { version = "0.13", features = ["blocking", "query"], default-features = false }
uuid = { version = "1.20.0", features = ["v4"] }
url = "2.2.2"
libflate = "2.1.0"
libc = "^0.2.124"
prost = "0.14"
serde_json = "1.0.115"
jemalloc_pprof = { version = "0.8", features = ["symbolize"]}
tokio = { version = "1", features = ["rt"]}
pprof = { package = "pprof-pyroscope-fork", version = "0.1500.2", features = ["framehop", "framehop-unwinder"] }
lazy_static = "1.5.0"
assert_matches = "=1.5.0"
claims = "=0.8.0"
pretty_env_logger = "0.5.0"
rbspy = { version = "0.44" }
remoteprocess = "0.5.0"
anyhow = "1.0"
flate2 = "1.1"
py-spy = { git = "https://github.com/grafana/py-spy", rev = "5f1661d", default-features = false }




[dependencies]
thiserror = { workspace = true }
log = { workspace = true }
names = { workspace = true }
reqwest = { workspace = true }
uuid = { workspace = true }
url = { workspace = true }
libflate = { workspace = true }
libc = { workspace = true }
prost = { workspace = true }
serde_json = { workspace = true }
pprof = { workspace = true, optional = true }
lazy_static = { workspace = true }
jemalloc_pprof = { workspace = true, optional = true  }

[dev-dependencies]
assert_matches = { workspace = true }
claims = { workspace = true }
tikv-jemallocator = { version = "0.6", features = ["profiling"] }
env_logger = "0.11"

[[example]]
name = "jemalloc"
required-features = ["backend-jemalloc"]

[features]
default = ["rustls-tls"]
rustls-tls = ["reqwest/rustls"]
native-tls = ["reqwest/native-tls"]
native-tls-vendored = ["reqwest/native-tls-vendored"]
rustls-no-provider = ["reqwest/rustls-no-provider"]
backend-pprof-rs = ["dep:pprof"]
backend-jemalloc = ["dep:jemalloc_pprof"]

[profile.dev]
opt-level=0
debug = true
rpath = false
lto = false
debug-assertions = true
codegen-units = 4

[profile.release]
opt-level=3
debug = false
strip = "symbols"
rpath = false
lto = true
debug-assertions = false
codegen-units = 1

[profile.test]
opt-level = 1
debug = true
rpath = false
lto = false
debug-assertions = true
codegen-units = 4

[profile.bench]
opt-level = 3
debug = false
rpath = false
lto = true
debug-assertions = false
codegen-units = 1
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

   Copyright 2022 Pyroscope

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

## File: `MANIFEST.in`
```
include Cargo.toml
include Cargo.lock
include pyroscope_ffi/python/rust/Cargo.toml
include pyroscope_ffi/ruby/ext/rbspy/Cargo.toml
recursive-include src *.rs
recursive-include pyroscope_ffi/python/rust/src/ *.rs
recursive-include pyroscope_ffi/ruby/ext/rbspy/src/ *.rs
recursive-include kit/ *.rs
recursive-include kit/ Cargo.toml
recursive-include examples/ *.rs
```

## File: `Makefile`
```

COMMIT = $(shell git rev-parse --short HEAD)
DOCKER_EXTRA ?=
DOCKER_BUILDKIT=1
BUMP ?= fix



.PHONY: lib/test
lib/test:
	cargo  test --manifest-path Cargo.toml

.PHONY: pprofrs/test
pprofrs/test:
	cargo  test --manifest-path Cargo.toml --features backend-pprof-rs


.PHONY: ffikit/test
ffikit/test:
	cargo  test --manifest-path pyroscope_ffi/ffikit/Cargo.toml

.PHONY: test
test: pprofrs/test  lib/test ffikit/test


.PHONY: rust/fmt
rust/fmt:
	cargo fmt --all


.PHONY: rust/fmt/check
rust/fmt/check:
	cargo fmt --all --check


.PHONY: ruby/version/bump
ruby/version/bump:
	BUMP=$(BUMP) bash ci/bump_ffi_version.sh ruby


.PHONY: python/version/bump
python/version/bump:
	BUMP=$(BUMP) bash ci/bump_ffi_version.sh python


.PHONY: ffi/python/header
ffi/python/header:
	cd pyroscope_ffi/python/rust && cbindgen --config cbindgen.toml --output include/pyroscope_ffi.h


.PHONY: ffi/python/cffi
ffi/python/cffi:
	python pyroscope_ffi/python/scripts/tests/compile_ffi.py


.PHONY: ffi/ruby/header
ffi/ruby/header:
	cd pyroscope_ffi/ruby/ext/rbspy && cbindgen --config cbindgen.toml --output include/rbspy.h


include ffi.mk
```

## File: `README.md`
```markdown
## Pyroscope Profiler

**Pyroscope Profiler for Rust. Profile your Rust applications.**

[![license](https://img.shields.io/badge/license-Apache2.0-blue.svg)](LICENSE) 
[![Crate](https://img.shields.io/crates/v/pyroscope.svg)](https://crates.io/crates/pyroscope)


### Major Contributors

We'd like to give a big thank you to the following contributors who have made significant contributions to this project:

* [Abid Omar](https://github.com/omarabid)
* [Anatoly Korniltsev](https://github.com/korniltsev)
* [Bernhard Schuster](https://github.com/drahnr)


### License

Pyroscope is distributed under the Apache License (Version 2.0).

See [LICENSE](LICENSE) for details.
```

## File: `ffi.mk`
```

MANYLINUX_PREFIX=pyroscope/rust_builder
MANYLINUX_VERSION=4
BUILD_ARCH_AMD=manylinux2014_x86_64
BUILD_ARCH_ARM=manylinux2014_aarch64

.phony: wheel/linux/amd64
wheel/linux/amd64:
	docker buildx build \
		--build-arg=PLATFORM=x86_64 \
	 	--platform=linux/amd64 \
	 	--output=. \
	 	-f docker/wheel.Dockerfile \
	 	.

.phony: wheel/linux/arm64
wheel/linux/arm64:
	docker buildx build \
		--build-arg=PLATFORM=aarch64 \
	 	--platform=linux/arm64 \
	 	--output=. \
	 	-f docker/wheel.Dockerfile \
	 	.

.phony: wheel/musllinux/amd64
wheel/musllinux/amd64:
	docker buildx build \
		--build-arg=PLATFORM=x86_64 \
	 	--platform=linux/amd64 \
	 	--output=. \
	 	-f docker/wheel-musllinux.Dockerfile \
	 	.

.phony: wheel/musllinux/arm64
wheel/musllinux/arm64:
	docker buildx build \
		--build-arg=PLATFORM=aarch64 \
	 	--platform=linux/arm64 \
	 	--output=. \
	 	-f docker/wheel-musllinux.Dockerfile \
	 	.

.phony: wheel/mac/amd64
wheel/mac/amd64:
	MACOSX_DEPLOYMENT_TARGET=11.0 CARGO_BUILD_TARGET=x86_64-apple-darwin python -m build --wheel
	wheel tags --platform-tag macosx_11_0_x86_64 --remove dist/*.whl

.phony: wheel/mac/arm64
wheel/mac/arm64:
	MACOSX_DEPLOYMENT_TARGET=11.0 CARGO_BUILD_TARGET=aarch64-apple-darwin python -m build --wheel
	wheel tags --platform-tag macosx_11_0_arm64 --remove dist/*.whl


.phony: gem/linux/amd64
gem/linux/amd64:
	docker buildx build \
		--build-arg=PLATFORM=x86_64 \
		--build-arg="TARGET_TASK=x86_64_linux:gem" \
		--output=pyroscope_ffi/ruby \
	 	--platform=linux/amd64 \
	 	-f docker/gem.Dockerfile \
	 	.

.phony: gem/linux/arm64
gem/linux/arm64:
	docker buildx build  \
		--build-arg=PLATFORM=aarch64 \
		--build-arg="TARGET_TASK=aarch64_linux:gem" \
		--output=pyroscope_ffi/ruby \
		--platform=linux/arm64 \
		-f docker/gem.Dockerfile \
	 	.

.phony: gem/mac/amd64
gem/mac/amd64:
	cd pyroscope_ffi/ruby && \
		bundle && \
		RUST_TARGET=x86_64-apple-darwin rake rbspy_install && \
		RUST_TARGET=x86_64-apple-darwin rake x86_64_darwin:gem

.phony: gem/mac/arm64
gem/mac/arm64:
	cd pyroscope_ffi/ruby && \
		bundle && \
		RUST_TARGET=aarch64-apple-darwin rake rbspy_install && \
		RUST_TARGET=aarch64-apple-darwin rake arm64_darwin:gem
```

## File: `pyproject.toml`
```
[project]
name = "pyroscope-io"
version = "1.0.4" # x-release-please-version
description = "Pyroscope Python integration"
authors = [
    {name = "Tolya Korniltsev",email = "anatoly.korniltsev@grafana.com"}
]
license-files = [ "LICENSE" ]
license = "Apache-2.0"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "cffi (>=2.0.0,<3.0.0)",
]
maintainers = [
    {name = "Tolyan Korniltsev", email = "anatoly.korniltsev@grafana.com"},
]
classifiers = [
    "Intended Audience :: Developers",
    "Operating System :: MacOS",
    "Operating System :: POSIX",
    "Operating System :: Unix",
    "Programming Language :: Python",
    "Topic :: Software Development",
    "Topic :: Software Development :: Debuggers",
    "Topic :: Utilities",
]

[tool.setuptools.packages]
find = { where = ["pyroscope_ffi/python/python/"] }

[tool.distutils.bdist_wheel]
py_limited_api = "cp310"


[build-system]
requires = [
    "setuptools (>=82.0.0,<83.0.0)",
    "setuptools-rust (>=1.12.0,<2.0.0)",
    "cffi (>=2.0.0,<3.0.0)",
]


build-backend = "setuptools.build_meta"
```

## File: `renovate.json`
```json
{
  "$schema": "https://docs.renovatebot.com/renovate-schema.json",
  "extends": [
    "config:recommended"
  ],
  "packageRules": [
    {
      "matchDepNames": [
        "openssl/openssl"
      ],
      "separateMinorPatch": true
    },
    {
      "matchDepNames": [
        "openssl/openssl"
      ],
      "matchUpdateTypes": [
        "major",
        "minor"
      ],
      "enabled": false
    }
  ],
  "customManagers": [
    {
      "customType": "regex",
      "managerFilePatterns": [
        "/^docker/.*\\.Dockerfile$/"
      ],
      "matchStrings": [
        "ARG OPENSSL_VERSION=(?<currentValue>[\\d.]+)"
      ],
      "depNameTemplate": "openssl/openssl",
      "datasourceTemplate": "github-releases",
      "extractVersionTemplate": "^openssl-(?<version>.*)$"
    }
  ]
}
```

## File: `setup.py`
```python
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    rust_extensions=[
        RustExtension(
            "pyroscope_python_extension.pyroscope_python_extension",
            path="pyroscope_ffi/python/rust/Cargo.toml",
            binding=Binding.NoBinding,
            cargo_manifest_args=["--locked"],
        )
    ],
)
```

## File: `ci/bump_ffi_version.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

lang="${1:-}"
bump_part="${BUMP:-fix}"

if [[ -z "$lang" ]]; then
  echo "Usage: BUMP=<major|minor|fix> $0 <ruby|python>" >&2
  exit 1
fi

bump_semver() {
  local current="$1"
  local major minor patch

  major="$(echo "$current" | cut -d. -f1)"
  minor="$(echo "$current" | cut -d. -f2)"
  patch="$(echo "$current" | cut -d. -f3)"

  case "$bump_part" in
    major)
      major=$((major + 1))
      minor=0
      patch=0
      ;;
    minor)
      minor=$((minor + 1))
      patch=0
      ;;
    fix)
      patch=$((patch + 1))
      ;;
    *)
      echo "Invalid bump type '$bump_part'. Use major, minor, or fix." >&2
      exit 1
      ;;
  esac

  echo "$major.$minor.$patch"
}

case "$lang" in
  ruby)
    ruby_current="$(sed -n "s/.*VERSION = '\([0-9]*\.[0-9]*\.[0-9]*\)'.*/\1/p" pyroscope_ffi/ruby/lib/pyroscope/version.rb)"
    ruby_new="$(bump_semver "$ruby_current")"
    sed -i -E "s/(VERSION = ')[0-9]+\.[0-9]+\.[0-9]+('\\.freeze)/\1$ruby_new\2/" pyroscope_ffi/ruby/lib/pyroscope/version.rb
    sed -i -E "0,/^version = \"[0-9]+\.[0-9]+\.[0-9]+\"/s//version = \"$ruby_new\"/" pyroscope_ffi/ruby/ext/rbspy/Cargo.toml
    cargo update --package ffiruby
    echo "Ruby versions bumped: gem/rust cargo $ruby_current -> $ruby_new"
    ;;
  python)
    python_current="$(sed -n 's/^version = "\([0-9]*\.[0-9]*\.[0-9]*\)"/\1/p' pyproject.toml)"
    python_new="$(bump_semver "$python_current")"
    sed -i -E "s/^(version = \")[0-9]+\.[0-9]+\.[0-9]+(\")/\1$python_new\2/" pyproject.toml
    sed -i -E "0,/^version = \"[0-9]+\.[0-9]+\.[0-9]+\"/s//version = \"$python_new\"/" pyroscope_ffi/python/rust/Cargo.toml
    cargo update --package pyroscope_python_extension
    echo "Python versions bumped: package/rust cargo $python_current -> $python_new"
    ;;
  *)
    echo "Invalid language '$lang'. Use ruby or python." >&2
    exit 1
    ;;
esac
```

## File: `ci/check-kindasafe-versions.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

kindasafe_version=$(awk -F'=' '/^version[[:space:]]*=/{gsub(/[[:space:]"]/, "", $2); print $2; exit}' kit/kindasafe/Cargo.toml)
kindasafe_init_version=$(awk -F'=' '/^version[[:space:]]*=/{gsub(/[[:space:]"]/, "", $2); print $2; exit}' kit/kindasafe_init/Cargo.toml)

if [[ -z "$kindasafe_version" || -z "$kindasafe_init_version" ]]; then
  echo "failed to read one or more version values"
  exit 1
fi

if [[ "$kindasafe_version" != "$kindasafe_init_version" ]]; then
  echo "kindasafe version mismatch: kindasafe=$kindasafe_version kindasafe_init=$kindasafe_init_version"
  exit 1
fi

echo "kindasafe versions are in sync: $kindasafe_version"
```

## File: `ci/check-spy-versions.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

py_cfg_version=$(awk -F'=' '/^version[[:space:]]*=/{sub(/#.*/, "", $2); gsub(/[[:space:]"]/, "", $2); print $2; exit}' pyproject.toml)
rb_version=$(sed -nE "s/.*VERSION = '([^']+)'.*/\1/p" pyroscope_ffi/ruby/lib/pyroscope/version.rb)

py_rust_version=$(awk -F'=' '/^version[[:space:]]*=/{gsub(/[[:space:]"]/, "", $2); print $2; exit}' pyroscope_ffi/python/rust/Cargo.toml)
rb_rust_version=$(awk -F'=' '/^version[[:space:]]*=/{gsub(/[[:space:]"]/, "", $2); print $2; exit}' pyroscope_ffi/ruby/ext/rbspy/Cargo.toml)

if [[ -z "$py_cfg_version" || -z "$rb_version" || -z "$py_rust_version" || -z "$rb_rust_version" ]]; then
  echo "failed to read one or more version values"
  exit 1
fi

if [[ "$py_cfg_version" != "$py_rust_version" ]]; then
  echo "pyspy version mismatch: pyproject.toml=$py_cfg_version cargo=$py_rust_version"
  exit 1
fi

if [[ "$rb_version" != "$rb_rust_version" ]]; then
  echo "rbspy version mismatch: version.rb=$rb_version cargo=$rb_rust_version"
  exit 1
fi

echo "spy versions are in sync"
```

## File: `ci/check-tag-version.sh`
```bash
#!/usr/bin/env bash
set -euo pipefail

# Verifies that a release tag matches the corresponding Cargo package version.
#
# Usage: ./ci/check-tag-version.sh <tag>
#
# Supported tag formats:
#   lib-X.Y.Z       → checks root Cargo.toml (pyroscope crate)
#   python-X.Y.Z    → checks pyroscope_ffi/python/rust/Cargo.toml
#   ruby-X.Y.Z      → checks pyroscope_ffi/ruby/ext/rbspy/Cargo.toml
#   kindasafe-X.Y.Z → checks kit/kindasafe/Cargo.toml

cd "$(dirname "$0")/.."

TAG="${1:-}"
if [[ -z "$TAG" ]]; then
  echo "Usage: $0 <tag>"
  exit 1
fi

extract_cargo_version() {
  awk -F'=' '/^version[[:space:]]*=/{gsub(/[[:space:]"]/, "", $2); print $2; exit}' "$1"
}

if [[ "$TAG" =~ ^lib-(.+)$ ]]; then
  tag_version="${BASH_REMATCH[1]}"
  cargo_file="Cargo.toml"
elif [[ "$TAG" =~ ^python-(.+)$ ]]; then
  tag_version="${BASH_REMATCH[1]}"
  cargo_file="pyroscope_ffi/python/rust/Cargo.toml"
elif [[ "$TAG" =~ ^ruby-(.+)$ ]]; then
  tag_version="${BASH_REMATCH[1]}"
  cargo_file="pyroscope_ffi/ruby/ext/rbspy/Cargo.toml"
elif [[ "$TAG" =~ ^kindasafe-(.+)$ ]]; then
  tag_version="${BASH_REMATCH[1]}"
  cargo_file="kit/kindasafe/Cargo.toml"
else
  echo "Unknown tag format: $TAG"
  echo "Expected one of: lib-X.Y.Z, python-X.Y.Z, ruby-X.Y.Z, kindasafe-X.Y.Z"
  exit 1
fi

cargo_version=$(extract_cargo_version "$cargo_file")

if [[ -z "$cargo_version" ]]; then
  echo "Failed to read version from $cargo_file"
  exit 1
fi

if [[ "$tag_version" != "$cargo_version" ]]; then
  echo "Version mismatch: tag=$tag_version, $cargo_file=$cargo_version"
  exit 1
fi

echo "OK: tag $TAG matches $cargo_file version $cargo_version"
```

## File: `docker/Makefile`
```
PREFIX ?= pyroscope/rust_builder
CLI_BUILDER_VERSION ?= 3
MANYLINUX_VERSION ?= 4

.PHONY: push_x86_64
push_x86_64:
	docker buildx build --platform linux/amd64 -t $(PREFIX)_manylinux2014_x86_64:$(MANYLINUX_VERSION) -f Dockerfile.manylinux2014_x86_64 --push .

.PHONY: push_aarch64
push_aarch64:
	docker buildx build --platform linux/arm64 -t $(PREFIX)_manylinux2014_aarch64:$(MANYLINUX_VERSION) -f Dockerfile.manylinux2014_aarch64 --push .


.PHONY: push_cli_builder
push_cli_builder:
	docker buildx build --platform linux/amd64,linux/arm64 -t $(PREFIX)_cli:$(CLI_BUILDER_VERSION) -f Dockerfile.cli_builder --push .

```

## File: `docker/Readme.txt`
```
These dockerfile.manylinux* images do few things:

1. rust toolchain, libunwind, deps were downloaded and installed on every build in manylinux.sh
now they are installed once at image creation time
```

## File: `docker/gem.Dockerfile`
```
ARG PLATFORM=x86_64
FROM quay.io/pypa/manylinux2014_${PLATFORM} AS builder
ARG OPENSSL_VERSION=3.5.5

ENV RUST_VERSION=1.88
RUN curl https://static.rust-lang.org/rustup/dist/$(arch)-unknown-linux-musl/rustup-init -o ./rustup-init \
    && chmod +x ./rustup-init \
    && ./rustup-init  -y --default-toolchain=${RUST_VERSION} --default-host=$(arch)-unknown-linux-gnu
ENV PATH=/root/.cargo/bin:$PATH
RUN yum -y install gcc libffi-devel perl-core wget gcc-c++ glibc-devel make

# Build OpenSSL from source
RUN curl -fsSL "https://github.com/openssl/openssl/releases/download/openssl-${OPENSSL_VERSION}/openssl-${OPENSSL_VERSION}.tar.gz" \
    -o /tmp/openssl.tar.gz \
    && tar xzf /tmp/openssl.tar.gz -C /tmp \
    && cd /tmp/openssl-${OPENSSL_VERSION} \
    && ./config no-shared no-tests --prefix=/usr/local/openssl \
    && make -j$(nproc) \
    && make install_sw \
    && ln -sf /usr/local/openssl/lib64 /usr/local/openssl/lib || true \
    && cd / \
    && rm -rf /tmp/openssl*

ENV OPENSSL_DIR=/usr/local/openssl
ENV OPENSSL_STATIC=1

WORKDIR /pyroscope-rs

ADD rustfmt.toml \
    Cargo.toml \
    Cargo.lock \
    ./

ADD src src
ADD kit/ kit/
ADD examples/ examples/
ADD pyroscope_ffi/ pyroscope_ffi/
# TODO --frozen
RUN --mount=type=cache,target=/root/.cargo/registry cargo build -p ffiruby --release

FROM ruby:4.0@sha256:66302616aabd939350e9bd7bc31ccad5ef993a5ba5e93f0cc029bb82e80a8d3b AS builder-gem
WORKDIR /gem
ADD pyroscope_ffi/ruby /gem/

RUN bundle install

COPY --from=builder /pyroscope-rs/target/release/librbspy.so lib/rbspy/rbspy.so
ARG TARGET_TASK
RUN rake ${TARGET_TASK}

FROM scratch
COPY --from=builder-gem /gem/pkg/ /pkg/
```

## File: `docker/wheel-musllinux.Dockerfile`
```
# syntax=docker/dockerfile:1.22@sha256:4a43a54dd1fedceb30ba47e76cfcf2b47304f4161c0caeac2db1c61804ea3c91
ARG PLATFORM=x86_64
FROM quay.io/pypa/musllinux_1_2_${PLATFORM} AS builder
ARG OPENSSL_VERSION=3.5.5

RUN apk add --no-cache gcc musl-dev libffi-dev make perl linux-headers

# Build OpenSSL from source
RUN curl -fsSL "https://github.com/openssl/openssl/releases/download/openssl-${OPENSSL_VERSION}/openssl-${OPENSSL_VERSION}.tar.gz" \
    -o /tmp/openssl.tar.gz \
    && tar xzf /tmp/openssl.tar.gz -C /tmp \
    && cd /tmp/openssl-${OPENSSL_VERSION} \
    && ./config no-shared no-tests --prefix=/usr/local/openssl \
    && make -j$(nproc) \
    && make install_sw \
    && ln -sf /usr/local/openssl/lib64 /usr/local/openssl/lib || true \
    && cd / \
    && rm -rf /tmp/openssl*

ENV OPENSSL_DIR=/usr/local/openssl
ENV OPENSSL_STATIC=1

RUN adduser -D builder \
    && mkdir -p /pyroscope-rs \
    && chown builder:builder /pyroscope-rs

USER builder
RUN test "$(id -u)" = "1000" || { echo "ERROR: builder uid is $(id -u), expected 1000"; exit 1; }

ENV RUST_VERSION=1.88
RUN curl https://static.rust-lang.org/rustup/dist/$(arch)-unknown-linux-musl/rustup-init -o /tmp/rustup-init \
    && chmod +x /tmp/rustup-init \
    && /tmp/rustup-init -y --default-toolchain=${RUST_VERSION} --default-host=$(arch)-unknown-linux-musl \
    && rm /tmp/rustup-init
ENV PATH=/home/builder/.cargo/bin:$PATH

WORKDIR /pyroscope-rs

RUN /opt/python/cp310-cp310/bin/python -m pip install --user build

ADD --chown=builder:builder pyproject.toml \
    setup.py \
    rustfmt.toml \
    Cargo.toml \
    Cargo.lock \
    ./

ADD --chown=builder:builder src src
ADD --chown=builder:builder kit/ kit/
ADD --chown=builder:builder examples/ examples/
ADD --chown=builder:builder pyroscope_ffi/ pyroscope_ffi/

RUN --mount=type=cache,target=/home/builder/.cargo/registry,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/builder/.cargo/git,uid=1000,gid=1000 \
    /opt/python/cp310-cp310/bin/python -m build --wheel

RUN auditwheel repair dist/*.whl --wheel-dir dist-repaired/

FROM scratch
COPY --from=builder  /pyroscope-rs/dist-repaired dist/
```

## File: `docker/wheel.Dockerfile`
```
# syntax=docker/dockerfile:1.22@sha256:4a43a54dd1fedceb30ba47e76cfcf2b47304f4161c0caeac2db1c61804ea3c91
ARG PLATFORM=x86_64
FROM quay.io/pypa/manylinux2014_${PLATFORM} AS builder
ARG OPENSSL_VERSION=3.5.5

RUN yum -y install gcc libffi-devel perl-core glibc-devel make

# Build OpenSSL from source
RUN curl -fsSL "https://github.com/openssl/openssl/releases/download/openssl-${OPENSSL_VERSION}/openssl-${OPENSSL_VERSION}.tar.gz" \
    -o /tmp/openssl.tar.gz \
    && tar xzf /tmp/openssl.tar.gz -C /tmp \
    && cd /tmp/openssl-${OPENSSL_VERSION} \
    && ./config no-shared no-tests --prefix=/usr/local/openssl \
    && make -j$(nproc) \
    && make install_sw \
    && ln -sf /usr/local/openssl/lib64 /usr/local/openssl/lib || true \
    && cd / \
    && rm -rf /tmp/openssl*

ENV OPENSSL_DIR=/usr/local/openssl
ENV OPENSSL_STATIC=1

RUN useradd -m builder \
    && mkdir -p /pyroscope-rs \
    && chown builder:builder /pyroscope-rs

USER builder
RUN test "$(id -u)" = "1000" || { echo "ERROR: builder uid is $(id -u), expected 1000"; exit 1; }

ENV RUST_VERSION=1.88
RUN curl https://static.rust-lang.org/rustup/dist/$(arch)-unknown-linux-musl/rustup-init -o /tmp/rustup-init \
    && chmod +x /tmp/rustup-init \
    && /tmp/rustup-init -y --default-toolchain=${RUST_VERSION} --default-host=$(arch)-unknown-linux-gnu \
    && rm /tmp/rustup-init
ENV PATH=/home/builder/.cargo/bin:$PATH

WORKDIR /pyroscope-rs

RUN /opt/python/cp310-cp310/bin/python -m pip install --user build

ADD --chown=builder:builder pyproject.toml \
    setup.py \
    rustfmt.toml \
    Cargo.toml \
    Cargo.lock \
    ./

ADD --chown=builder:builder src src
ADD --chown=builder:builder kit/ kit/
ADD --chown=builder:builder examples/ examples/
ADD --chown=builder:builder pyroscope_ffi/ pyroscope_ffi/

RUN --mount=type=cache,target=/home/builder/.cargo/registry,uid=1000,gid=1000 \
    --mount=type=cache,target=/home/builder/.cargo/git,uid=1000,gid=1000 \
    /opt/python/cp310-cp310/bin/python -m build --wheel

RUN auditwheel repair dist/*.whl --wheel-dir dist-repaired/

FROM scratch
COPY --from=builder  /pyroscope-rs/dist-repaired dist/
```

## File: `examples/jemalloc.rs`
```rust
//! Jemalloc memory profiling example.
//!
//! This example demonstrates how to use the jemalloc backend for memory profiling.
//! It requires jemalloc to be configured as the global allocator with profiling enabled.
//!
//! # Requirements
//!
//! Add these dependencies to your Cargo.toml:
//!
//! ```toml
//! [dependencies]
//! pyroscope = { version = "2.0.0", features = ["backend-jemalloc"] }
//! tikv-jemallocator = { version = "0.6", features = ["profiling"] }
//! ```
//!
//! # Running
//!
//! ```sh
//! # Enable jemalloc profiling via environment variable
//! _RJEM_MALLOC_CONF=prof:true,prof_active:true,lg_prof_sample:19 \
//!     cargo run --example jemalloc --features backend-jemalloc
//! ```

use pyroscope::backend::jemalloc::jemalloc_backend;
use pyroscope::pyroscope::PyroscopeAgentBuilder;
use std::time::Duration;

// Configure jemalloc as the global allocator.
// Profiling must also be enabled at runtime via MALLOC_CONF or _RJEM_MALLOC_CONF.
#[global_allocator]
static ALLOC: tikv_jemallocator::Jemalloc = tikv_jemallocator::Jemalloc;

fn main() -> Result<(), Box<dyn std::error::Error>> {
    env_logger::init();

    let agent = PyroscopeAgentBuilder::new(
        "http://localhost:4040",
        "example.jemalloc",
        100,
        "pyroscope-rs",
        env!("CARGO_PKG_VERSION"),
        jemalloc_backend(),
    )
    .tags(vec![("env", "dev")])
    .build()?;

    let agent_running = agent.start()?;

    // Simulate heavy allocations for 30 seconds.
    let start = std::time::Instant::now();
    let mut iteration = 0u64;
    while start.elapsed() < Duration::from_secs(30) {
        // Allocate vectors of varying sizes (1KB to 1MB).
        for i in 0..100 {
            let size = 1024 * (1 + (iteration as usize + i) % 1024);
            let v: Vec<u8> = vec![0u8; size];
            std::hint::black_box(&v);
        }
        iteration += 1;
    }
    eprintln!("Completed {} iterations", iteration);

    let agent_ready = agent_running.stop()?;
    agent_ready.shutdown();

    Ok(())
}
```

## File: `kit/coredump/Cargo.toml`
```
[package]
name = "coredump"
version = "0.1.0"
edition = "2024"
publish = false

[dependencies]
object = { version = "0.38", default-features = false, features = ["read", "elf"] }
memmap2 = "0.9"

[dev-dependencies]
anyhow = "=1.0.102"
libc = "=0.2.182"
```

## File: `kit/coredump/src/lib.rs`
```rust
mod memory;
mod notes;

use object::elf;
use object::endian::LittleEndian;
use object::read::elf::FileHeader as _;

/// A PT_LOAD segment from the core file, used for virtual address resolution.
#[derive(Debug, Clone)]
pub struct Segment {
    pub vaddr: u64,
    pub memsz: u64,
    pub file_offset: u64,
    pub filesz: u64,
}

/// A memory mapping entry parsed from the NT_FILE note.
#[derive(Debug, Clone)]
pub struct Mapping {
    pub vaddr: u64,
    pub length: u64,
    pub flags: u32,
    pub file_offset: u64,
    pub path: Option<String>,
}

/// Thread register state parsed from NT_PRSTATUS.
#[derive(Debug, Clone)]
pub struct ThreadInfo {
    /// Light Weight Process ID (thread ID).
    pub lwp: u32,
    /// General purpose registers (raw bytes, x86_64: 27 × 8 = 216 bytes).
    pub gp_regs: Vec<u8>,
    /// Thread pointer base (TLS base). On x86_64 this is fs_base.
    pub tp_base: u64,
}

/// An opened and parsed ELF core file.
pub struct Coredump {
    data: memmap2::Mmap,
    pub mappings: Vec<Mapping>,
    pub threads: Vec<ThreadInfo>,
    segments: Vec<Segment>,
}

/// Errors that can occur when opening or reading a coredump.
#[derive(Debug)]
pub enum CoredumpError {
    Io(std::io::Error),
    ElfParse(String),
    NotCoreFile,
    InvalidNote(&'static str),
    AddressNotMapped(u64),
    ReadOutOfBounds { addr: u64, len: usize },
}

impl std::fmt::Display for CoredumpError {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        match self {
            CoredumpError::Io(e) => write!(f, "I/O error: {e}"),
            CoredumpError::ElfParse(msg) => write!(f, "ELF parse error: {msg}"),
            CoredumpError::NotCoreFile => write!(f, "not an ELF core file"),
            CoredumpError::InvalidNote(msg) => write!(f, "invalid note: {msg}"),
            CoredumpError::AddressNotMapped(addr) => {
                write!(f, "address 0x{addr:x} not mapped in coredump")
            }
            CoredumpError::ReadOutOfBounds { addr, len } => {
                write!(f, "read of {len} bytes at 0x{addr:x} out of bounds")
            }
        }
    }
}

impl std::error::Error for CoredumpError {}

impl From<std::io::Error> for CoredumpError {
    fn from(e: std::io::Error) -> Self {
        CoredumpError::Io(e)
    }
}

impl Coredump {
    /// Open and parse an ELF core file at the given path.
    pub fn open(path: &str) -> Result<Self, CoredumpError> {
        let file = std::fs::File::open(path)?;
        // SAFETY: the file is a read-only coredump; we never write through the mapping.
        let data = unsafe { memmap2::Mmap::map(&file) }?;
        Self::parse(data)
    }

    fn parse(data: memmap2::Mmap) -> Result<Self, CoredumpError> {
        let endian = LittleEndian;

        let header = elf::FileHeader64::<LittleEndian>::parse(&*data)
            .map_err(|e| CoredumpError::ElfParse(e.to_string()))?;

        if header.e_type(endian) != elf::ET_CORE {
            return Err(CoredumpError::NotCoreFile);
        }

        let program_headers = header
            .program_headers(endian, &*data)
            .map_err(|e| CoredumpError::ElfParse(e.to_string()))?;

        let segments = memory::collect_segments(endian, program_headers);
        let (mappings, threads) = notes::parse_notes(endian, program_headers, &data)?;

        Ok(Coredump {
            data,
            mappings,
            threads,
            segments,
        })
    }

    /// Read bytes from the coredump at the given virtual address.
    pub fn read(&self, addr: u64, buf: &mut [u8]) -> Result<(), CoredumpError> {
        memory::read(&self.data, &self.segments, addr, buf)
    }

    /// Read a little-endian u64 from the coredump at the given virtual address.
    pub fn read_u64(&self, addr: u64) -> Result<u64, CoredumpError> {
        let mut buf = [0u8; 8];
        self.read(addr, &mut buf)?;
        Ok(u64::from_le_bytes(buf))
    }

    /// Read a little-endian u32 from the coredump at the given virtual address.
    pub fn read_u32(&self, addr: u64) -> Result<u32, CoredumpError> {
        let mut buf = [0u8; 4];
        self.read(addr, &mut buf)?;
        Ok(u32::from_le_bytes(buf))
    }
}
```

## File: `kit/coredump/src/memory.rs`
```rust
use object::endian::LittleEndian;
use object::read::elf::ProgramHeader as _;

use crate::{CoredumpError, Segment};

pub fn collect_segments(
    endian: LittleEndian,
    program_headers: &[object::elf::ProgramHeader64<LittleEndian>],
) -> Vec<Segment> {
    program_headers
        .iter()
        .filter(|ph| ph.p_type(endian) == object::elf::PT_LOAD)
        .map(|ph| Segment {
            vaddr: ph.p_vaddr(endian),
            memsz: ph.p_memsz(endian),
            file_offset: ph.p_offset(endian),
            filesz: ph.p_filesz(endian),
        })
        .collect()
}

pub fn read(
    data: &[u8],
    segments: &[Segment],
    addr: u64,
    buf: &mut [u8],
) -> Result<(), CoredumpError> {
    let len = buf.len() as u64;
    for seg in segments {
        if addr >= seg.vaddr && addr.saturating_add(len) <= seg.vaddr.saturating_add(seg.memsz) {
            let seg_rel = addr - seg.vaddr;
            if seg_rel + len > seg.filesz {
                return Err(CoredumpError::ReadOutOfBounds {
                    addr,
                    len: buf.len(),
                });
            }
            let file_pos = seg.file_offset + seg_rel;
            let file_end = file_pos + len;
            if file_end as usize > data.len() {
                return Err(CoredumpError::ReadOutOfBounds {
                    addr,
                    len: buf.len(),
                });
            }
            buf.copy_from_slice(&data[file_pos as usize..file_end as usize]);
            return Ok(());
        }
    }
    Err(CoredumpError::AddressNotMapped(addr))
}
```

## File: `kit/coredump/src/notes.rs`
```rust
use object::elf;
use object::endian::LittleEndian;
use object::read::elf::ProgramHeader as _;

use crate::{CoredumpError, Mapping, ThreadInfo};

pub fn parse_notes(
    endian: LittleEndian,
    program_headers: &[elf::ProgramHeader64<LittleEndian>],
    data: &[u8],
) -> Result<(Vec<Mapping>, Vec<ThreadInfo>), CoredumpError> {
    let mut mappings = Vec::new();
    let mut threads = Vec::new();

    for ph in program_headers {
        let Some(mut iter) = ph
            .notes(endian, data)
            .map_err(|e| CoredumpError::ElfParse(e.to_string()))?
        else {
            continue;
        };

        while let Some(note) = iter
            .next()
            .map_err(|e| CoredumpError::ElfParse(e.to_string()))?
        {
            let name = note.name();
            let n_type = note.n_type(endian);
            let desc = note.desc();

            if name == elf::ELF_NOTE_CORE {
                match n_type {
                    elf::NT_PRSTATUS => {
                        parse_prstatus(desc, &mut threads)?;
                    }
                    elf::NT_FILE => {
                        mappings = parse_nt_file(desc)?;
                    }
                    _ => {}
                }
            }
        }
    }

    Ok((mappings, threads))
}

// x86_64 prstatus layout constants (from `pahole elf_prstatus`).
const PRSTATUS_SIZE_X86_64: usize = 336;
const LWP_OFFSET: usize = 32;
const GPREGS_OFFSET: usize = 112;
const GPREGS_SIZE: usize = 216; // 27 registers × 8 bytes
const FS_BASE_REG_INDEX: usize = 21;

fn parse_prstatus(desc: &[u8], threads: &mut Vec<ThreadInfo>) -> Result<(), CoredumpError> {
    if desc.len() < PRSTATUS_SIZE_X86_64 {
        return Err(CoredumpError::InvalidNote(
            "NT_PRSTATUS too short for x86_64",
        ));
    }

    let lwp = u32::from_le_bytes(desc[LWP_OFFSET..LWP_OFFSET + 4].try_into().unwrap());

    let gp_regs = desc[GPREGS_OFFSET..GPREGS_OFFSET + GPREGS_SIZE].to_vec();

    let fs_base_offset = FS_BASE_REG_INDEX * 8;
    let tp_base = u64::from_le_bytes(
        gp_regs[fs_base_offset..fs_base_offset + 8]
            .try_into()
            .unwrap(),
    );

    threads.push(ThreadInfo {
        lwp,
        gp_regs,
        tp_base,
    });
    Ok(())
}

const ENTRY_SIZE: usize = 24; // start(8) + end(8) + file_offset_pages(8)

fn parse_nt_file(desc: &[u8]) -> Result<Vec<Mapping>, CoredumpError> {
    if desc.len() < 16 {
        return Err(CoredumpError::InvalidNote("NT_FILE too short for header"));
    }

    let num_files = u64::from_le_bytes(desc[0..8].try_into().unwrap()) as usize;
    let page_size = u64::from_le_bytes(desc[8..16].try_into().unwrap());

    let entries_end = 16 + num_files * ENTRY_SIZE;
    if desc.len() < entries_end {
        return Err(CoredumpError::InvalidNote("NT_FILE truncated entries"));
    }

    struct Entry {
        start: u64,
        end: u64,
        file_offset_pages: u64,
    }

    let mut entries = Vec::with_capacity(num_files);
    for i in 0..num_files {
        let base = 16 + i * ENTRY_SIZE;
        let start = u64::from_le_bytes(desc[base..base + 8].try_into().unwrap());
        let end = u64::from_le_bytes(desc[base + 8..base + 16].try_into().unwrap());
        let file_offset_pages = u64::from_le_bytes(desc[base + 16..base + 24].try_into().unwrap());
        entries.push(Entry {
            start,
            end,
            file_offset_pages,
        });
    }

    let mut names_slice = &desc[entries_end..];
    let mut mappings = Vec::with_capacity(num_files);
    for entry in &entries {
        let null_pos =
            names_slice
                .iter()
                .position(|&b| b == 0)
                .ok_or(CoredumpError::InvalidNote(
                    "NT_FILE filename missing null terminator",
                ))?;
        let path = if null_pos > 0 {
            Some(String::from_utf8_lossy(&names_slice[..null_pos]).into_owned())
        } else {
            None
        };
        names_slice = &names_slice[null_pos + 1..];
        mappings.push(Mapping {
            vaddr: entry.start,
            length: entry.end - entry.start,
            flags: 0,
            file_offset: entry.file_offset_pages * page_size,
            path,
        });
    }
    Ok(mappings)
}
```

## File: `kit/coredump/tests/integration.rs`
```rust
#[test]
fn error_on_nonexistent_file() {
    let result = coredump::Coredump::open("/tmp/nonexistent-core-file-38493729");
    assert!(result.is_err());
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
mod coredump_read {
    use anyhow::{Result, anyhow};
    use std::path::PathBuf;
    use std::process::Command;

    const C_SOURCE: &str = r#"
#include <stdint.h>
#include <stdlib.h>
#include <string.h>

/* Known magic value in an initialized global. */
volatile uint64_t MAGIC = 0xDEADBEEFCAFEBABEULL;

/* A small struct to verify multi-field reads. */
struct TestData {
    uint32_t a;
    uint32_t b;
    uint64_t c;
};
volatile struct TestData DATA = { 0x11223344, 0x55667788, 0xAAAABBBBCCCCDDDDULL };

int main(void) {
    /* Touch the volatiles so the compiler cannot optimise them away. */
    uint64_t sink = MAGIC + DATA.a;
    (void)sink;
    abort();
    return 0;
}
"#;

    /// Find the virtual address of a named symbol in a non-PIE ELF binary.
    fn symbol_addr(elf_path: &str, name: &str) -> Result<u64> {
        let data = std::fs::read(elf_path)?;
        let obj = object::File::parse(&*data).map_err(|e| anyhow!("ELF parse: {e}"))?;
        use object::Object as _;
        use object::ObjectSymbol as _;
        for sym in obj.symbols() {
            if sym.name() == Ok(name) {
                return Ok(sym.address());
            }
        }
        Err(anyhow!("symbol '{name}' not found"))
    }

    /// Build the C helper, run it to produce a coredump, return (binary_path, core_path).
    fn build_and_dump(tmp: &std::path::Path) -> Result<(String, String)> {
        let src = tmp.join("crashme.c");
        let bin = tmp.join("crashme");
        let core = tmp.join("core");

        std::fs::write(&src, C_SOURCE)?;

        // Compile as non-PIE so symbol addresses are absolute.
        let cc = Command::new("gcc")
            .args([
                "-o",
                bin.to_str().unwrap(),
                src.to_str().unwrap(),
                "-no-pie",
                "-static",
            ])
            .output()?;
        if !cc.status.success() {
            return Err(anyhow!(
                "gcc failed: {}",
                String::from_utf8_lossy(&cc.stderr)
            ));
        }

        // Run the binary with coredumps enabled.
        // kernel.core_pattern may point elsewhere, so use a wrapper that
        // sets the core size and uses SIGSYS to control the pattern via
        // /proc/self — but the simplest portable approach is:
        //   1. set core_pattern via /proc/sys if possible (needs root)
        //   2. or just rely on kernel.core_pattern and search for the file
        //
        // Instead, we use gdb to generate the coredump at a known path,
        // which works reliably regardless of kernel.core_pattern.
        let gdb = Command::new("gdb")
            .args([
                "--batch",
                "-ex",
                "run",
                "-ex",
                &format!("generate-core-file {}", core.display()),
                "-ex",
                "quit",
                bin.to_str().unwrap(),
            ])
            .output()?;
        if !core.exists() {
            return Err(anyhow!(
                "gdb did not produce a core file.\nstdout: {}\nstderr: {}",
                String::from_utf8_lossy(&gdb.stdout),
                String::from_utf8_lossy(&gdb.stderr),
            ));
        }

        Ok((
            bin.to_str().unwrap().to_owned(),
            core.to_str().unwrap().to_owned(),
        ))
    }

    #[test]
    fn read_known_values_from_coredump() -> Result<()> {
        let tmp = tempdir()?;
        let (bin, core_path) = build_and_dump(&tmp)?;

        let core = coredump::Coredump::open(&core_path)?;

        // Sanity: the coredump has at least one thread and one mapping.
        assert!(!core.threads.is_empty(), "expected at least one thread");
        assert!(!core.mappings.is_empty(), "expected at least one mapping");

        // Look up symbol addresses from the static binary.
        let magic_addr = symbol_addr(&bin, "MAGIC")?;
        let data_addr = symbol_addr(&bin, "DATA")?;

        // Read MAGIC (u64).
        let magic_val = core.read_u64(magic_addr)?;
        assert_eq!(
            magic_val, 0xDEADBEEFCAFEBABE,
            "MAGIC mismatch: got 0x{magic_val:016x}"
        );

        // Read DATA.a (u32 at offset 0).
        let a = core.read_u32(data_addr)?;
        assert_eq!(a, 0x11223344, "DATA.a mismatch: got 0x{a:08x}");

        // Read DATA.b (u32 at offset 4).
        let b = core.read_u32(data_addr + 4)?;
        assert_eq!(b, 0x55667788, "DATA.b mismatch: got 0x{b:08x}");

        // Read DATA.c (u64 at offset 8).
        let c = core.read_u64(data_addr + 8)?;
        assert_eq!(c, 0xAAAABBBBCCCCDDDD, "DATA.c mismatch: got 0x{c:016x}");

        // Verify that reading an unmapped address fails.
        let bad = core.read_u64(0xDEAD_0000_0000);
        assert!(bad.is_err(), "reading unmapped address should fail");

        // Verify thread info has a non-zero tp_base (TLS base) and lwp.
        let t = &core.threads[0];
        assert_ne!(t.lwp, 0, "thread LWP should be non-zero");

        Ok(())
    }

    fn tempdir() -> Result<PathBuf> {
        let dir = std::env::temp_dir().join(format!("coredump-test-{}", std::process::id()));
        std::fs::create_dir_all(&dir)?;
        Ok(dir)
    }
}
```

## File: `kit/kindasafe/Cargo.toml`
```
[package]
name = "kindasafe"
version = "0.1.0"
edition = "2024"
description = "Signal-safe memory reading for x86_64 and aarch64 using naked functions and crash recovery"
license = "Apache-2.0"
repository = "https://github.com/grafana/pyroscope-rs"
keywords = ["memory", "signal-safe", "no_std", "profiler"]
categories = ["no-std", "os::unix-apis"]
readme = "README.md"

[dependencies]

[dev-dependencies]
anyhow = "=1.0.102"
libc = "=0.2.182"
kindasafe_init = { path = "../kindasafe_init" }
```

## File: `kit/kindasafe/README.md`
```markdown
# kindasafe

Signal-safe memory reading for x86_64 and aarch64 on Linux.

Uses naked assembly functions to read memory, with crash recovery via SIGSEGV/SIGBUS signal handlers. When a read faults, the signal handler adjusts the program counter to skip past the faulting instruction and reports the error instead of crashing.

This is a `no_std` crate providing the core read primitives. Use [`kindasafe_init`](https://crates.io/crates/kindasafe_init) to install the required signal handlers.

## Usage

```rust
// First, initialize the signal handlers (requires kindasafe_init)
kindasafe_init::init().expect("failed to init");

// Read a u64 from a potentially-invalid address
let value = kindasafe::u64(some_address);
match value {
    Ok(v) => println!("read: {v:#x}"),
    Err(e) => println!("fault: signal {}", e.signal),
}
```

## Supported architectures

- x86_64
- aarch64

## License

Apache-2.0
```

## File: `kit/kindasafe/src/lib.rs`
```rust
#![no_std]

#[derive(Debug, PartialEq)]
pub struct ReadMemError {
    pub signal: u64,
}

pub type Ptr = u64;

pub fn u64(at: Ptr) -> Result<Ptr, ReadMemError> {
    let res = arch::u64(at);
    if res.signal == 0 {
        Ok(res.value)
    } else {
        Err(ReadMemError { signal: res.signal })
    }
}

pub fn slice(buf: &mut [u8], at: Ptr) -> Result<(), ReadMemError> {
    let res = arch::slice(buf.as_ptr(), at, buf.len() as u64);
    if res.signal == 0 {
        Ok(())
    } else {
        Err(ReadMemError { signal: res.signal })
    }
}

pub fn str(buf: &mut [u8], at: Ptr) -> Result<&str, ReadMemError> {
    if at == 0 {
        return Ok("");
    }
    let res = arch::slice(buf.as_ptr(), at, buf.len() as u64);
    if res.signal != 0 {
        return Err(ReadMemError { signal: res.signal });
    }
    for i in 0..buf.len() {
        if buf[i] == 0 {
            let v = &buf[..i];
            return match core::str::from_utf8(v) {
                Ok(v) => Ok(v),
                Err(_) => Err(ReadMemError { signal: 228 }), //todo
            };
        }
    }
    Err(ReadMemError { signal: 229 }) //todo
}

pub fn crash_points() -> CrashPoints {
    arch::crash_points()
}

#[derive(Copy, Clone)]
pub struct CrashPoint {
    pub pc: usize,
    pub signal_reg: Reg,
    pub skip: usize,
}
const CRASH_POINTS_COUNT: usize = 2;

#[derive(Copy, Clone)]
pub struct CrashPoints {
    pub crash_points: [CrashPoint; CRASH_POINTS_COUNT],
}

#[cfg(target_arch = "x86_64")]
#[derive(Debug, Copy, Clone, PartialEq, Eq)]
pub enum Reg {
    Rax,
    Rdx,
}

#[cfg(target_arch = "aarch64")]
#[derive(Debug, Copy, Clone, PartialEq, Eq)]
pub enum Reg {
    X0,
    X1,
}

#[cfg(target_arch = "x86_64")]
pub mod arch {

    #[repr(C)]
    pub struct U64Res {
        pub value: u64,
        pub signal: u64,
    }

    #[unsafe(naked)]
    pub extern "sysv64" fn u64(_at: u64) -> U64Res {
        core::arch::naked_asm!(
            "mov rax, [rdi]", // 00010000 	48 8B 07 	mov 	rax, qword ptr [rdi]
            "xor edx, edx",   // 00010003 	31 D2 	xor 	edx, edx
            "ret",            // 00010005 	C3 	ret
        )
    }

    #[repr(C)]
    pub struct VecResult {
        pub signal: u64,
    }

    #[unsafe(naked)]
    pub extern "sysv64" fn slice(
        _dst: *const u8, // rdi
        _src: u64,       // rsi
        _n: u64,         // rdx
    ) -> VecResult {
        core::arch::naked_asm!(
            "mov ecx, edx", // 00010000 	89 D1 	mov 	ecx, edx
            "rep movsb",    // 00010002 	F3 A4 	rep movsb 	byte ptr [rdi], byte ptr [rsi]
            "xor eax, eax", // 00010004 	31 C0 	xor 	eax, eax
            "ret",          // 00010006 	C3 	ret
        )
    }

    pub fn crash_points() -> crate::CrashPoints {
        crate::CrashPoints {
            crash_points: [
                crate::CrashPoint {
                    pc: u64 as *const () as usize,
                    signal_reg: crate::Reg::Rdx,
                    skip: 5,
                },
                crate::CrashPoint {
                    pc: slice as *const () as usize + 2, // +2 for 89 D1 	mov 	ecx, edx
                    signal_reg: crate::Reg::Rax,
                    skip: 4,
                },
            ],
        }
    }
}

#[cfg(target_arch = "aarch64")]
pub mod arch {

    #[repr(C)]
    pub struct U64Res {
        pub value: u64,
        pub signal: u64,
    }

    #[unsafe(naked)]
    pub extern "C" fn u64(_at: u64) -> U64Res {
        core::arch::naked_asm!(
            "ldr x0, [x0]", // offset 0: load 64-bit value from address in x0
            "mov x1, #0",   // offset 4: signal = 0 (success)
            "ret",          // offset 8
        )
    }

    #[repr(C)]
    pub struct VecResult {
        pub signal: u64,
    }

    #[unsafe(naked)]
    pub extern "C" fn slice(
        _dst: *const u8, // x0
        _src: u64,       // x1
        _n: u64,         // x2
    ) -> VecResult {
        core::arch::naked_asm!(
            "cbz x2, 2f", // offset 0: skip if n==0
            "1:",
            "ldrb w3, [x1], #1", // offset 4: load byte from src, post-increment
            "strb w3, [x0], #1", // offset 8: store byte to dst, post-increment
            "subs x2, x2, #1",   // offset 12: decrement counter
            "b.ne 1b",           // offset 16: loop if not zero
            "2:",
            "mov x0, #0", // offset 20: signal = 0 (success)
            "ret",        // offset 24
        )
    }

    pub fn crash_points() -> crate::CrashPoints {
        crate::CrashPoints {
            crash_points: [
                crate::CrashPoint {
                    pc: u64 as *const () as usize,
                    signal_reg: crate::Reg::X1,
                    skip: 8, // skip ldr + mov to land on ret
                },
                crate::CrashPoint {
                    pc: slice as *const () as usize + 4, // +4 for cbz
                    signal_reg: crate::Reg::X0,
                    skip: 20, // skip ldrb + strb + subs + b.ne + mov to land on ret
                },
            ],
        }
    }
}
```

## File: `kit/kindasafe/tests/fallback.rs`
```rust
#[test]
fn test_fallback() {
    //todo
}
```

## File: `kit/kindasafe/tests/positive.rs`
```rust
use anyhow::anyhow;
use kindasafe::ReadMemError;

use anyhow::Result;
use kindasafe::{Ptr, slice, u64};

// On macOS, accessing a PROT_NONE mmap page delivers SIGBUS;
// on Linux it delivers SIGSEGV.
#[cfg(target_os = "linux")]
const PROT_NONE_SIGNAL: u64 = libc::SIGSEGV as u64;
#[cfg(target_os = "macos")]
const PROT_NONE_SIGNAL: u64 = libc::SIGBUS as u64;

#[test]
fn test_init() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    Ok(())
}

#[test]
fn u64_aligned() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;

    let x: Vec<u8> = vec![0xca, 0xfe, 0xba, 0xbe, 0xde, 0xad, 0xbe, 0xef];
    let x_ptr = x.as_ptr() as Ptr;

    let i = u64(x_ptr).map_err(|err| anyhow!("read mem error {err:?}"))?;
    assert_eq!(i, 0xefbeaddebebafeca);
    Ok(())
}

#[test]
fn u64_unaligned() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;

    let x: Vec<u8> = vec![0xca, 0xfe, 0xba, 0xbe, 0xde, 0xad, 0xbe, 0xef, 0x00];
    let x_ptr = x.as_ptr() as Ptr + 1;
    let i = u64(x_ptr).map_err(|err| anyhow!("read mem error {err:?}"))?;
    assert_eq!(i, 0xefbeaddebebafe);
    Ok(())
}

#[test]
fn u64_sigsegv() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    trigger_sigsegv(|p| {
        assert_eq!(
            u64(p),
            Err(ReadMemError {
                signal: PROT_NONE_SIGNAL
            })
        );
    });
    Ok(())
}

#[test]
fn u64_sigbus() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    trigger_sigbus(|p| {
        assert_eq!(
            u64(p),
            Err(ReadMemError {
                signal: libc::SIGBUS as u64
            })
        );
    });
    Ok(())
}

#[test]
fn u64_unaligned_page_boundary() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;

    trigger_sigsegv_page_boundary(|p, ps| {
        let boundary = ps as u64;
        assert_eq!(u64(p), Ok(0x6161616161616161));
        assert_eq!(u64(p + boundary - 0x8), Ok(0x6161616161616161));
        assert_eq!(
            u64(p + boundary - 0x7),
            Err(ReadMemError {
                signal: PROT_NONE_SIGNAL
            })
        );
        assert_eq!(
            u64(p + boundary),
            Err(ReadMemError {
                signal: PROT_NONE_SIGNAL
            })
        );
    });
    Ok(())
}

#[test]
fn vec_aligned() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    let mut buf = vec![0u8; 8];
    let x: Vec<u8> = vec![0xca, 0xfe, 0xba, 0xbe, 0xde, 0xad, 0xbe, 0xef];
    slice(&mut buf, x.as_ptr() as Ptr).map_err(|err| anyhow!("read mem error {err:?}"))?;
    assert_eq!(buf, x.clone());
    Ok(())
}

#[test]
fn vec_unaligned() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    let mut buf = vec![0u8; 8];
    let x: Vec<u8> = vec![0xca, 0xfe, 0xba, 0xbe, 0xde, 0xad, 0xbe, 0xef, 0xcc];
    let x_ptr = x.as_ptr() as Ptr + 1;
    slice(&mut buf[0..7], x_ptr).map_err(|err| anyhow!("read mem error {err:?}"))?;
    let expected: Vec<u8> = vec![0xfe, 0xba, 0xbe, 0xde, 0xad, 0xbe, 0xef, 0];
    assert_eq!(buf, expected);
    Ok(())
}

#[test]
fn vec_sigsegv() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    trigger_sigsegv(|p| {
        let mut buf = [0u8; 8];
        assert_eq!(
            slice(&mut buf, p as Ptr),
            Err(ReadMemError {
                signal: PROT_NONE_SIGNAL
            })
        );
    });
    Ok(())
}

#[test]
fn vec_sigbus() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;
    trigger_sigbus(|p| {
        let mut buf = [0u8; 8];
        let res = slice(&mut buf, p as Ptr);
        assert_eq!(
            res,
            Err(ReadMemError {
                signal: libc::SIGBUS as u64
            })
        );
    });
    Ok(())
}
#[test]
fn vec_sigsegv_page_boundary() -> Result<(), anyhow::Error> {
    kindasafe_init::init().map_err(|err| anyhow!("{:?}", err))?;

    trigger_sigsegv_page_boundary(|p, ps| {
        let boundary = ps as u64;
        let mut buf = [0u8; 16];
        assert_eq!(
            slice(&mut buf, (p + boundary - 8) as Ptr),
            Err(ReadMemError {
                signal: PROT_NONE_SIGNAL
            })
        );
        assert_eq!(
            buf,
            vec![
                0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x61, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0,
                0x0
            ]
            .as_slice()
        );
    });
    Ok(())
}

fn page_size() -> usize {
    let ps = unsafe { libc::sysconf(libc::_SC_PAGESIZE) };
    assert!(ps > 0, "sysconf(_SC_PAGESIZE) failed");
    ps as usize
}

fn trigger_sigsegv_page_boundary<F>(mut cb: F)
where
    F: FnMut(Ptr, usize),
{
    let ps = page_size();
    let map_size = 2 * ps;
    unsafe {
        let x_ptr = libc::mmap(
            std::ptr::null_mut::<libc::c_void>(),
            map_size,
            libc::PROT_NONE,
            libc::MAP_PRIVATE | libc::MAP_ANON,
            -1,
            0,
        );
        assert_ne!(libc::MAP_FAILED, x_ptr, "mmap failed");
        let x_ptr = x_ptr as usize;
        let ret = libc::mprotect(
            x_ptr as *mut libc::c_void,
            ps,
            libc::PROT_READ | libc::PROT_WRITE,
        );
        assert_eq!(ret, 0, "mprotect failed");
        libc::memset(x_ptr as *mut libc::c_void, 0x61, ps);

        cb(x_ptr as Ptr, ps);

        libc::munmap(x_ptr as *mut libc::c_void, map_size);
    }
}

pub fn trigger_sigbus<F>(mut cb: F)
where
    F: FnMut(u64),
{
    unsafe {
        let f = libc::tmpfile();
        let m = libc::mmap(
            std::ptr::null_mut::<libc::c_void>(),
            4,
            libc::PROT_WRITE,
            libc::MAP_PRIVATE,
            libc::fileno(f),
            0,
        );
        let m = m as *mut i32;
        cb(m as u64);

        libc::munmap(m as *mut libc::c_void, 4);
        libc::fclose(f);
    };
}

pub fn trigger_sigsegv<F>(mut cb: F)
where
    F: FnMut(u64),
{
    unsafe {
        let m = libc::mmap(
            std::ptr::null_mut::<libc::c_void>(),
            4,
            libc::PROT_NONE,
            libc::MAP_PRIVATE | libc::MAP_ANON,
            -1,
            0,
        );
        assert_ne!(libc::MAP_FAILED, m);
        let m = m as *mut i32;
        cb(m as u64);

        libc::munmap(m as *mut libc::c_void, 4);
    };
}
```

## File: `kit/kindasafe_init/Cargo.toml`
```
[package]
name = "kindasafe_init"
version = "0.1.0"
edition = "2024"
description = "Signal handler initialization for the kindasafe signal-safe memory reading library"
license = "Apache-2.0"
repository = "https://github.com/grafana/pyroscope-rs"
keywords = ["memory", "signal-safe", "profiler"]
categories = ["os::unix-apis"]
readme = "README.md"

[dependencies]
kindasafe = { path = "../kindasafe", version = "0.1.0" }
libc = { version = "0.2.182" }
spin = { version = "0.10.0" }

[dev-dependencies]
anyhow = "=1.0.102"
```

## File: `kit/kindasafe_init/README.md`
```markdown
# kindasafe_init

Signal handler initialization for the [kindasafe](https://crates.io/crates/kindasafe) signal-safe memory reading library.

Installs SIGSEGV and SIGBUS signal handlers that enable `kindasafe` to recover from memory access faults instead of crashing. Preserves any previously installed signal handlers as fallbacks.

## Usage

```rust
kindasafe_init::init().expect("failed to initialize kindasafe");

// Now kindasafe reads will recover from faults
let result = kindasafe::u64(some_address);
```

## License

Apache-2.0
```

## File: `kit/kindasafe_init/src/lib.rs`
```rust
#[derive(Debug, PartialEq, Clone)]
pub enum InitError {
    InstallSignalHandlersFailed,
    SanityCheckFailed,
}

// todo think how to have less static mut
static mut FALLBACK_SIGSEGV: libc::sigaction = unsafe { std::mem::zeroed() };
static mut FALLBACK_SIGBUS: libc::sigaction = unsafe { std::mem::zeroed() };

static INIT_LOCK: spin::Mutex<Option<Result<(), InitError>>> = spin::Mutex::new(None);

pub fn is_initialized() -> Option<Result<(), InitError>> {
    let g = INIT_LOCK.lock();
    g.clone()
}
pub fn init() -> Result<(), InitError> {
    let mut g = INIT_LOCK.lock();
    if let Some(prev) = g.clone() {
        return prev;
    }

    let res = init_locked();
    *g = Some(res.clone());
    res
}

pub fn init_locked() -> Result<(), InitError> {
    unsafe {
        FALLBACK_SIGSEGV = new_signal_handler(libc::SIGSEGV, crash_handler)
            .map_err(|_| InitError::InstallSignalHandlersFailed)?;
        FALLBACK_SIGBUS = new_signal_handler(libc::SIGBUS, crash_handler)
            .map_err(|_| InitError::InstallSignalHandlersFailed)?;
    }
    Ok(())
}

/// # Safety
/// `data` must be a valid pointer to `libc::ucontext_t`.
#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
unsafe fn crash_handler(sig: libc::c_int, info: *mut libc::siginfo_t, data: *mut libc::c_void) {
    unsafe {
        let ctx: *mut libc::ucontext_t = data as *mut libc::ucontext_t;
        let pc = (*ctx).uc_mcontext.gregs[libc::REG_RIP as usize] as usize;
        for x in kindasafe::crash_points().crash_points {
            if x.pc == pc {
                (*ctx).uc_mcontext.gregs[libc::REG_RIP as usize] = (pc + x.skip) as libc::greg_t;
                let reg_idx = match x.signal_reg {
                    kindasafe::Reg::Rax => libc::REG_RAX as usize,
                    kindasafe::Reg::Rdx => libc::REG_RDX as usize,
                };
                (*ctx).uc_mcontext.gregs[reg_idx] = sig as u64 as libc::greg_t;
                return;
            }
        }
        fallback(sig, info, data);
    }
}

/// # Safety
/// `data` must be a valid pointer to `libc::ucontext_t`.
#[cfg(all(target_arch = "x86_64", target_os = "macos"))]
unsafe fn crash_handler(sig: libc::c_int, info: *mut libc::siginfo_t, data: *mut libc::c_void) {
    unsafe {
        let ctx: *mut libc::ucontext_t = data as *mut libc::ucontext_t;
        let mctx = (*ctx).uc_mcontext;
        let ss = &mut (*mctx).__ss;
        let pc = ss.__rip as usize;
        for x in kindasafe::crash_points().crash_points {
            if x.pc == pc {
                ss.__rip = (pc + x.skip) as u64;
                match x.signal_reg {
                    kindasafe::Reg::Rax => ss.__rax = sig as u64,
                    kindasafe::Reg::Rdx => ss.__rdx = sig as u64,
                };
                return;
            }
        }
        fallback(sig, info, data);
    }
}

/// # Safety
/// `data` must be a valid pointer to `libc::ucontext_t`.
#[cfg(all(target_arch = "aarch64", target_os = "linux"))]
unsafe fn crash_handler(sig: libc::c_int, info: *mut libc::siginfo_t, data: *mut libc::c_void) {
    unsafe {
        let ctx: *mut libc::ucontext_t = data as *mut libc::ucontext_t;
        let pc = (*ctx).uc_mcontext.pc as usize;
        for x in kindasafe::crash_points().crash_points {
            if x.pc == pc {
                (*ctx).uc_mcontext.pc = (pc + x.skip) as u64;
                // libc provides no named constants for aarch64 register indices;
                // mcontext_t.regs is [u64; 31] where index matches register number.
                let reg_idx = match x.signal_reg {
                    kindasafe::Reg::X0 => 0,
                    kindasafe::Reg::X1 => 1,
                };
                (*ctx).uc_mcontext.regs[reg_idx] = sig as u64;
                return;
            }
        }
        fallback(sig, info, data);
    }
}

/// # Safety
/// `data` must be a valid pointer to `libc::ucontext_t`.
#[cfg(all(target_arch = "aarch64", target_os = "macos"))]
unsafe fn crash_handler(sig: libc::c_int, info: *mut libc::siginfo_t, data: *mut libc::c_void) {
    unsafe {
        let ctx: *mut libc::ucontext_t = data as *mut libc::ucontext_t;
        let mctx = (*ctx).uc_mcontext;
        let pc = (*mctx).__ss.__pc as usize;
        for x in kindasafe::crash_points().crash_points {
            if x.pc == pc {
                (*mctx).__ss.__pc = (pc + x.skip) as u64;
                // libc provides no named constants for aarch64 register indices;
                // __darwin_arm_thread_state64.__x is [u64; 29] where index matches register number.
                let reg_idx = match x.signal_reg {
                    kindasafe::Reg::X0 => 0,
                    kindasafe::Reg::X1 => 1,
                };
                (*mctx).__ss.__x[reg_idx] = sig as u64;
                return;
            }
        }
        fallback(sig, info, data);
    }
}

fn call_fallback(
    sig: libc::c_int,
    info: *mut libc::siginfo_t,
    data: *mut libc::c_void,
    fallback: libc::sigaction,
) {
    if fallback.sa_sigaction == 0 {
        restore_default_ignal_handler(sig);
    } else {
        let handler = unsafe {
            std::mem::transmute::<
                usize,
                extern "C" fn(libc::c_int, *mut libc::siginfo_t, *mut libc::c_void),
            >(fallback.sa_sigaction)
        };
        handler(sig, info, data);
    }
}
unsafe fn fallback(sig: libc::c_int, info: *mut libc::siginfo_t, data: *mut libc::c_void) {
    if sig == libc::SIGSEGV {
        call_fallback(sig, info, data, unsafe { FALLBACK_SIGSEGV });
        return;
    }
    if sig == libc::SIGBUS {
        call_fallback(sig, info, data, unsafe { FALLBACK_SIGBUS });
    }
}

fn new_signal_handler(
    signal: libc::c_int,
    handler: unsafe fn(sig: libc::c_int, info: *mut libc::siginfo_t, data: *mut libc::c_void),
) -> Result<libc::sigaction, ()> {
    unsafe {
        let mut old: libc::sigaction = std::mem::zeroed();
        if libc::sigaction(signal, std::ptr::null_mut(), &mut old) != 0 {
            return Err(());
        }
        let mut new: libc::sigaction = old;
        new.sa_sigaction = handler as usize;
        new.sa_flags |= libc::SA_RESTART | libc::SA_SIGINFO;
        if libc::sigaction(signal, &new, &mut old) != 0 {
            return Err(());
        }
        Ok(old)
    }
}

pub fn restore_default_ignal_handler(sig: libc::c_int) {
    let action: libc::sigaction = unsafe { std::mem::zeroed() };
    unsafe { libc::sigaction(sig, &action, std::ptr::null_mut()) };
}

/// Sanity check that kindasafe crash recovery is working.
///
/// Maps a PROT_NONE page, attempts to read it via `kindasafe::u64`,
/// and verifies the read returns an error (SIGSEGV) instead of crashing.
/// Unmaps the page before returning.
///
/// Returns `Ok(())` if the sanity check passes, `Err(SanityCheckFailed)` if
/// the read unexpectedly succeeded (meaning crash recovery is broken).
pub fn sanity_check() -> Result<(), InitError> {
    unsafe {
        let page = libc::mmap(
            std::ptr::null_mut(),
            4096,
            libc::PROT_NONE,
            libc::MAP_PRIVATE | libc::MAP_ANON,
            -1,
            0,
        );
        if page == libc::MAP_FAILED {
            return Err(InitError::SanityCheckFailed);
        }
        let addr = page as u64;
        let result = kindasafe::u64(addr);
        libc::munmap(page, 4096);
        match result {
            Err(_) => Ok(()),
            Ok(_) => Err(InitError::SanityCheckFailed),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_init_idempotent() {
        assert!(init().is_ok());
        assert!(init().is_ok());
        assert!(is_initialized().is_some());
        assert_eq!(is_initialized(), Some(Ok(())));
    }

    #[test]
    fn test_sanity_check() {
        assert!(init().is_ok());
        assert!(sanity_check().is_ok());
    }
}
```

## File: `kit/notlibc/Cargo.toml`
```
[package]
name = "notlibc"
version = "0.1.0"
edition = "2024"
publish = false

[features]
default = []
debug-print = []

[dependencies]
spin = { version = "0.10.0" }

[dev-dependencies]
libc = "=0.2.182"
anyhow = "=1.0.102"
```

## File: `kit/notlibc/src/auxv.rs`
```rust
//! Read entries from the ELF auxiliary vector via `/proc/self/auxv`.
//!
//! Uses only inline-assembly syscalls (SYS_openat, SYS_read, SYS_close) so
//! it is safe to call from a signal handler and requires no libc.

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
mod imp {
    use crate::mmap::check;
    use crate::syscall::{syscall1, syscall3, syscall4};
    use crate::syscall_nr::x86_64::{SYS_CLOSE, SYS_OPENAT, SYS_READ};

    // ── openat constants ───────────────────────────────────────────────────────
    const AT_FDCWD: usize = (-100_isize) as usize;
    const O_RDONLY: usize = 0;

    // ── ELF auxiliary vector entry types ──────────────────────────────────────
    const AT_NULL: usize = 0;

    /// Scan `/proc/self/auxv` for the entry with the given `tag` and return
    /// its value, or `None` if the file cannot be read or the tag is absent.
    pub fn getauxval(tag: usize) -> Option<usize> {
        const PATH: &[u8] = b"/proc/self/auxv\0";

        let fd = unsafe {
            check(syscall4(
                SYS_OPENAT,
                AT_FDCWD,
                PATH.as_ptr() as usize,
                O_RDONLY,
                0, // mode — unused without O_CREAT
            ))
            .ok()?
        };

        // Each auxv entry is a (type, value) pair of native `usize` words.
        // A stack buffer of 64 entries (1 024 bytes on 64-bit) comfortably
        // covers the ~20 entries the Linux kernel typically produces.
        const BUF_ENTRIES: usize = 64;
        const ENTRY_SIZE: usize = core::mem::size_of::<usize>() * 2;
        const BUF_BYTES: usize = BUF_ENTRIES * ENTRY_SIZE;

        let mut buf = [0u8; BUF_BYTES];
        let mut result: Option<usize> = None;

        'outer: loop {
            let n = unsafe {
                check(syscall3(
                    SYS_READ,
                    fd as usize,
                    buf.as_mut_ptr() as usize,
                    BUF_BYTES,
                ))
            };
            let n = match n {
                Ok(0) | Err(_) => break,
                Ok(n) => n as usize,
            };

            let available = &buf[..n];
            let mut i = 0usize;
            while i + ENTRY_SIZE <= available.len() {
                // Decode a (type, value) pair from little-endian bytes.
                // `usize::from_le_bytes` is used so the code compiles in
                // `no_std` without any byte-order helpers.
                const WORD: usize = core::mem::size_of::<usize>();
                let mut a_bytes = [0u8; WORD];
                let mut v_bytes = [0u8; WORD];
                a_bytes.copy_from_slice(&available[i..i + WORD]);
                v_bytes.copy_from_slice(&available[i + WORD..i + 2 * WORD]);
                let a_type = usize::from_le_bytes(a_bytes);
                let a_val = usize::from_le_bytes(v_bytes);
                i += ENTRY_SIZE;

                if a_type == AT_NULL {
                    break 'outer;
                }
                if a_type == tag {
                    result = Some(a_val);
                    break 'outer;
                }
            }
        }

        unsafe { syscall1(SYS_CLOSE, fd as usize) };
        result
    }
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
pub use imp::getauxval;
```

## File: `kit/notlibc/src/debug.rs`
```rust
//! Debug output helpers using raw syscalls.
//!
//! Output is gated behind the `debug-print` Cargo feature (disabled by default).

#[cfg(all(feature = "debug-print", target_arch = "x86_64", target_os = "linux"))]
use crate::syscall_nr::x86_64::SYS_WRITE;

#[cfg(feature = "debug-print")]
const STDOUT: usize = 1;

/// Write a string to stdout followed by a newline.
///
/// This is a no-op unless the `debug-print` feature is enabled.
#[cfg(feature = "debug-print")]
#[inline(always)]
pub fn puts(s: &str) {
    writes(s);
    writes("\n");
}

/// Write a string to stdout followed by a newline.
///
/// This is a no-op unless the `debug-print` feature is enabled.
#[cfg(not(feature = "debug-print"))]
#[inline(always)]
pub fn puts(_s: &str) {}

/// Write a string to stdout without a trailing newline.
///
/// This is a no-op unless the `debug-print` feature is enabled.
#[cfg(feature = "debug-print")]
#[inline(always)]
pub fn writes(s: &str) {
    unsafe {
        crate::syscall::syscall3(SYS_WRITE, STDOUT, s.as_ptr() as usize, s.len());
    }
}

/// Write a string to stdout without a trailing newline.
///
/// This is a no-op unless the `debug-print` feature is enabled.
#[cfg(not(feature = "debug-print"))]
#[inline(always)]
pub fn writes(_s: &str) {}

/// Write a `usize` value as lowercase hex digits to stdout.
///
/// No `0x` prefix is emitted; callers should use `writes("0x")` before this
/// if the prefix is desired.
///
/// This is a no-op unless the `debug-print` feature is enabled.
#[cfg(feature = "debug-print")]
#[inline(always)]
pub fn write_hex(v: usize) {
    const HEX: &[u8] = b"0123456789abcdef";
    unsafe {
        let mut buf = [0u8; 16];
        let mut i = 16usize;
        let mut n = v;
        loop {
            i -= 1;
            buf[i] = HEX[n & 0xf];
            n >>= 4;
            if n == 0 {
                break;
            }
        }
        crate::syscall::syscall3(SYS_WRITE, STDOUT, buf.as_ptr().add(i) as usize, 16 - i);
    }
}

/// Write a `usize` value as lowercase hex digits to stdout.
///
/// No `0x` prefix is emitted; callers should use `writes("0x")` before this
/// if the prefix is desired.
///
/// This is a no-op unless the `debug-print` feature is enabled.
#[cfg(not(feature = "debug-print"))]
#[inline(always)]
pub fn write_hex(_v: usize) {}
```

## File: `kit/notlibc/src/errno_guard.rs`
```rust

```

## File: `kit/notlibc/src/eventfd.rs`
```rust
//! Signal-safe eventfd and epoll-based multi-fd waiter.
//!
//! # Platform support
//! The implementation uses inline-asm syscalls and is therefore only available
//! on `x86_64`/Linux.  On other targets the public types exist but every
//! constructor returns an `Err` at runtime, keeping downstream code
//! unconditionally compilable.

/// Error type: the raw positive errno value returned by the kernel.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub struct Error(pub i32);

impl core::fmt::Display for Error {
    fn fmt(&self, f: &mut core::fmt::Formatter<'_>) -> core::fmt::Result {
        write!(f, "errno {}", self.0)
    }
}

// ── platform-specific syscall numbers & constants ─────────────────────────────

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
use crate::syscall_nr::x86_64::{
    SYS_CLOSE, SYS_EPOLL_CREATE1, SYS_EPOLL_CTL, SYS_EPOLL_WAIT, SYS_EVENTFD2, SYS_WRITE,
};

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
mod flags {
    /// `EFD_NONBLOCK | EFD_SEMAPHORE`
    pub const EFD_FLAGS: usize = 0x800 | 0x1;
    /// `EPOLL_CTL_ADD`
    pub const EPOLL_CTL_ADD: usize = 1;
    /// `EPOLLIN`
    pub const EPOLLIN: u32 = 0x0000_0001;
}

// ── epoll_event layout (x86_64, packed) ──────────────────────────────────────

/// Mirror of `struct epoll_event` on x86_64 Linux (packed, 12 bytes).
/// `data` is the full 8-byte union; we use only the `u64` interpretation.
#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
#[repr(C, packed)]
struct EpollEvent {
    events: u32,
    data: u64,
}

// ── raw fd helpers ────────────────────────────────────────────────────────────

/// Close a raw file descriptor. Errors are ignored.
fn close_fd(fd: i32) {
    #[cfg(all(target_arch = "x86_64", target_os = "linux"))]
    unsafe {
        crate::syscall::syscall1(SYS_CLOSE, fd as usize);
    }
    #[cfg(not(all(target_arch = "x86_64", target_os = "linux")))]
    let _ = fd;
}

// ── EventFd ───────────────────────────────────────────────────────────────────

/// A non-blocking, semaphore-mode Linux eventfd.
///
/// Owns the file descriptor; closes it on `Drop`.
pub struct EventFd {
    fd: i32,
}

impl EventFd {
    /// Create a new `EventFd`.
    ///
    /// Uses `SYS_eventfd2` with `EFD_NONBLOCK | EFD_SEMAPHORE`.
    pub fn new() -> Result<Self, Error> {
        #[cfg(all(target_arch = "x86_64", target_os = "linux"))]
        {
            let ret = unsafe { crate::syscall::syscall2(SYS_EVENTFD2, 0, flags::EFD_FLAGS) };
            if ret >= 0 {
                Ok(Self { fd: ret as i32 })
            } else {
                Err(Error((-ret) as i32))
            }
        }
        #[cfg(not(all(target_arch = "x86_64", target_os = "linux")))]
        Err(Error(38)) // ENOSYS
    }

    /// Return the underlying file descriptor.
    ///
    /// The fd remains owned by this `EventFd`; do not close it externally.
    pub fn as_fd(&self) -> i32 {
        self.fd
    }

    /// Write 1 to the eventfd counter.
    ///
    /// Signal-safe: uses a direct `SYS_write` syscall; errors are ignored
    /// because there is nothing meaningful to do in a signal-handler context.
    pub fn notify(&self) {
        #[cfg(all(target_arch = "x86_64", target_os = "linux"))]
        {
            let val: u64 = 1;
            // SAFETY: `val` lives on the stack for the duration of the syscall.
            unsafe {
                crate::syscall::syscall3(
                    SYS_WRITE,
                    self.fd as usize,
                    &val as *const u64 as usize,
                    8,
                );
            }
        }
    }
}

impl Drop for EventFd {
    fn drop(&mut self) {
        close_fd(self.fd);
    }
}

// ── EventSet ──────────────────────────────────────────────────────────────────

/// Capacity of an `EventSet` — the maximum number of `EventFd`s it can hold.
pub const EVENT_SET_CAPACITY: usize = 64;

/// Waits on up to [`EVENT_SET_CAPACITY`] `EventFd`s simultaneously using epoll.
///
/// After construction, register individual `EventFd`s with [`EventSet::add`].
/// Call [`EventSet::wait`] to block until at least one fires; it returns the
/// **index** (0-based, in registration order) of the first notified fd.
///
/// Owns the epoll file descriptor; closes it on `Drop`.
pub struct EventSet {
    epfd: i32,
    /// fds registered in order; index into this slice == the index returned by `wait`.
    fds: [i32; EVENT_SET_CAPACITY],
    len: usize,
}

impl EventSet {
    /// Create an empty `EventSet`.
    pub fn new() -> Result<Self, Error> {
        #[cfg(all(target_arch = "x86_64", target_os = "linux"))]
        {
            // epoll_create1(0) — no special flags needed
            let ret = unsafe { crate::syscall::syscall1(SYS_EPOLL_CREATE1, 0) };
            if ret >= 0 {
                Ok(Self {
                    epfd: ret as i32,
                    fds: [-1; EVENT_SET_CAPACITY],
                    len: 0,
                })
            } else {
                Err(Error((-ret) as i32))
            }
        }
        #[cfg(not(all(target_arch = "x86_64", target_os = "linux")))]
        Err(Error(38)) // ENOSYS
    }

    /// Register an `EventFd` with this set.
    ///
    /// Returns the 0-based index assigned to this fd, which is the value
    /// [`EventSet::wait`] will return when this fd fires.
    ///
    /// Returns `Err` if the set is full or the `epoll_ctl` syscall fails.
    pub fn add(&mut self, efd: &EventFd) -> Result<usize, Error> {
        if self.len >= EVENT_SET_CAPACITY {
            return Err(Error(28)); // ENOSPC
        }
        let idx = self.len;

        #[cfg(all(target_arch = "x86_64", target_os = "linux"))]
        {
            let mut ev = EpollEvent {
                events: flags::EPOLLIN,
                // Store the registration index in the epoll data so we can
                // recover it without a secondary lookup in `wait`.
                data: idx as u64,
            };
            let ret = unsafe {
                crate::syscall::syscall4(
                    SYS_EPOLL_CTL,
                    self.epfd as usize,
                    flags::EPOLL_CTL_ADD,
                    efd.fd as usize,
                    &mut ev as *mut EpollEvent as usize,
                )
            };
            if ret < 0 {
                return Err(Error((-ret) as i32));
            }
        }
        #[cfg(not(all(target_arch = "x86_64", target_os = "linux")))]
        {
            let _ = efd;
            return Err(Error(38)); // ENOSYS
        }

        self.fds[idx] = efd.fd;
        self.len += 1;
        Ok(idx)
    }

    /// Block until at least one registered `EventFd` is notified.
    ///
    /// Returns the **index** (as given by [`EventSet::add`]) of the first
    /// fd that became ready.  If multiple fds fired simultaneously only the
    /// first one (in epoll's internal ordering) is reported; the others remain
    /// pending for the next call.
    ///
    /// `timeout_ms` is passed directly to `epoll_wait`:
    /// - `-1` → block indefinitely
    /// - `0` → non-blocking poll
    /// - `n > 0` → wait up to `n` milliseconds
    pub fn wait(&self, timeout_ms: i32) -> Result<usize, Error> {
        #[cfg(all(target_arch = "x86_64", target_os = "linux"))]
        {
            let mut ev = EpollEvent { events: 0, data: 0 };
            loop {
                let ret = unsafe {
                    crate::syscall::syscall4(
                        SYS_EPOLL_WAIT,
                        self.epfd as usize,
                        &mut ev as *mut EpollEvent as usize,
                        1, // max_events = 1
                        timeout_ms as usize,
                    )
                };
                if ret > 0 {
                    return Ok(ev.data as usize);
                } else if ret == 0 {
                    return Err(Error(110)); // ETIMEDOUT
                } else {
                    let errno = (-ret) as i32;
                    if errno == 4 {
                        // EINTR — restart the syscall
                        continue;
                    }
                    return Err(Error(errno));
                }
            }
        }
        #[cfg(not(all(target_arch = "x86_64", target_os = "linux")))]
        {
            let _ = timeout_ms;
            Err(Error(38)) // ENOSYS
        }
    }
}

impl Drop for EventSet {
    fn drop(&mut self) {
        if self.epfd >= 0 {
            close_fd(self.epfd);
        }
    }
}
```

## File: `kit/notlibc/src/lib.rs`
```rust
#![no_std]

pub mod auxv;
pub mod debug;
mod errno_guard;
pub mod mmap;
mod syscall;
pub mod syscall_nr;

pub use spin::Mutex;

pub type ShardMutex<T> = spin::Mutex<T>;

pub mod eventfd;
pub use eventfd::{EVENT_SET_CAPACITY, EventFd, EventSet};

/// Return the caller's Linux thread ID via raw `SYS_gettid` syscall.
///
/// Async-signal-safe: uses inline assembly, no libc.
#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
pub fn gettid() -> u32 {
    unsafe { syscall::syscall1(syscall_nr::x86_64::SYS_GETTID, 0) as u32 }
}
```

## File: `kit/notlibc/src/mmap.rs`
```rust
//! Anonymous memory mapping via inline assembly syscalls — no libc.
//!
//! Structural design follows memmap2's unix.rs (MmapInner / Mmap / MmapMut),
//! with every libc call replaced by a call into `crate::syscall`.
//!
//! Only anonymous private mappings are supported (the use-case for
//! signal-handler–safe scratch buffers).  File-backed maps are out of scope.

/// Convert a raw kernel `isize` return value into `Result`.
/// Negative values encode `-errno`; non-negative values are success.
/// Not architecture-specific: the sign convention is the same on all
/// Linux targets.
#[inline]
pub(crate) fn check(ret: isize) -> Result<isize, i32> {
    if ret < 0 { Err((-ret) as i32) } else { Ok(ret) }
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
mod imp {
    use core::ops::{Deref, DerefMut};
    use core::sync::atomic::{AtomicUsize, Ordering};

    use super::check;
    use crate::auxv::getauxval;
    use crate::syscall::{syscall2, syscall3, syscall6};
    use crate::syscall_nr::x86_64::{SYS_MMAP, SYS_MPROTECT, SYS_MUNMAP};

    // ── mmap prot / flags constants (Linux x86_64) ─────────────────────────────
    const PROT_READ: usize = 1;
    const PROT_WRITE: usize = 2;
    const PROT_EXEC: usize = 4;
    const MAP_PRIVATE: usize = 0x02;
    const MAP_ANONYMOUS: usize = 0x20;

    // ── ELF auxiliary vector entry type for page size ──────────────────────────
    const AT_PAGESZ: usize = 6;

    // ── page size (cached, same pattern as memmap2) ────────────────────────────

    pub fn page_size() -> usize {
        static PAGE_SIZE: AtomicUsize = AtomicUsize::new(0);
        match PAGE_SIZE.load(Ordering::Relaxed) {
            0 => {
                let ps = getauxval(AT_PAGESZ).unwrap_or(4096);
                PAGE_SIZE.store(ps, Ordering::Relaxed);
                ps
            }
            ps => ps,
        }
    }

    // ── MmapInner (mirrors memmap2's MmapInner) ───────────────────────────────
    //
    // Memory layout (same as memmap2):
    //
    //   mmap_base_ptr ──► [page-aligned kernel mapping start]
    //                          │  offset bytes (ignored prefix for file maps)
    //   self.ptr      ──►      └─► [slice start, = mmap_base_ptr for anon maps]
    //
    // For anonymous maps offset is always 0, so self.ptr == mmap_base_ptr.

    struct MmapInner {
        ptr: *mut u8, // start of the user-visible slice (page-aligned for anon)
        len: usize,   // length of the user-visible slice
    }

    impl MmapInner {
        /// Create an anonymous private mapping with the given `prot` flags.
        fn map_anon(len: usize, prot: usize) -> Result<Self, i32> {
            // Mirror memmap2: Rust slices cannot exceed isize::MAX.
            // On 64-bit this is never a practical issue, but keep the guard
            // for correctness on 32-bit (where `usize` == `u32`).
            if core::mem::size_of::<usize>() < 8 && len > isize::MAX as usize {
                return Err(22); // EINVAL
            }
            // mmap(2) rejects len=0 with EINVAL.  Map at least 1 byte so we
            // always obtain a valid kernel mapping; the public slice length
            // stays `len` (possibly 0) so the caller sees an empty slice.
            let map_len = len.max(1);
            let ptr = unsafe {
                check(syscall6(
                    SYS_MMAP,
                    0,                           // addr  = NULL → kernel chooses
                    map_len,                     // length
                    prot,                        // prot
                    MAP_PRIVATE | MAP_ANONYMOUS, // flags
                    usize::MAX,                  // fd = -1  (usize::MAX == -1 as usize)
                    0,                           // offset = 0
                ))? as usize
            };
            Ok(MmapInner {
                ptr: ptr as *mut u8,
                len,
            })
        }

        /// Returns `(page_aligned_base, map_len)` for munmap / mprotect.
        ///
        /// Identical to memmap2's `as_mmap_params()`: the kernel mapping starts
        /// at the page-aligned address below `self.ptr`; for anonymous maps the
        /// offset is always zero so this reduces to `(self.ptr, self.len.max(1))`.
        fn mmap_base_and_len(&self) -> (*mut u8, usize) {
            let offset = self.ptr as usize % page_size();
            let base = unsafe { self.ptr.sub(offset) };
            let map_len = (self.len + offset).max(1);
            (base, map_len)
        }

        fn mprotect(&mut self, prot: usize) -> Result<isize, i32> {
            let (base, map_len) = self.mmap_base_and_len();
            check(unsafe { syscall3(SYS_MPROTECT, base as usize, map_len, prot) })
        }

        #[inline]
        pub fn ptr(&self) -> *const u8 {
            self.ptr
        }

        #[inline]
        pub fn mut_ptr(&mut self) -> *mut u8 {
            self.ptr
        }

        #[inline]
        pub fn len(&self) -> usize {
            self.len
        }
    }

    impl Drop for MmapInner {
        fn drop(&mut self) {
            let (base, map_len) = self.mmap_base_and_len();
            // Errors are ignored in Drop — same rationale as memmap2:
            // there is no meaningful way to report them here.
            let _ = check(unsafe { syscall2(SYS_MUNMAP, base as usize, map_len) });
        }
    }

    // SAFETY: the mapped memory is not tied to any thread-local state.
    unsafe impl Send for MmapInner {}
    unsafe impl Sync for MmapInner {}

    // ── Public RAII types ──────────────────────────────────────────────────────

    /// An immutable (PROT_READ) anonymous memory map.
    ///
    /// Derefs to `&[u8]`.  The mapping is unmapped when dropped.
    pub struct Mmap {
        inner: MmapInner,
    }

    impl Mmap {
        /// Create a read-only anonymous mapping of `len` bytes.
        pub fn map_anon(len: usize) -> Result<Self, i32> {
            MmapInner::map_anon(len, PROT_READ).map(|inner| Mmap { inner })
        }

        /// Transition to a mutable mapping via `mprotect(PROT_READ | PROT_WRITE)`.
        pub fn make_mut(mut self) -> Result<MmapMut, i32> {
            self.inner.mprotect(PROT_READ | PROT_WRITE)?;
            Ok(MmapMut { inner: self.inner })
        }
    }

    impl Deref for Mmap {
        type Target = [u8];
        #[inline]
        fn deref(&self) -> &[u8] {
            unsafe { core::slice::from_raw_parts(self.inner.ptr(), self.inner.len()) }
        }
    }

    /// A mutable (PROT_READ | PROT_WRITE) anonymous memory map.
    ///
    /// Derefs to `&mut [u8]`.  The mapping is unmapped when dropped.
    pub struct MmapMut {
        inner: MmapInner,
    }

    impl MmapMut {
        /// Create a read-write anonymous mapping of `len` bytes.
        pub fn map_anon(len: usize) -> Result<Self, i32> {
            MmapInner::map_anon(len, PROT_READ | PROT_WRITE).map(|inner| MmapMut { inner })
        }

        /// Transition to a read-only mapping via `mprotect(PROT_READ)`.
        pub fn make_read_only(mut self) -> Result<Mmap, i32> {
            self.inner.mprotect(PROT_READ)?;
            Ok(Mmap { inner: self.inner })
        }

        /// Transition to a read+execute mapping via `mprotect(PROT_READ | PROT_EXEC)`.
        pub fn make_exec(mut self) -> Result<Mmap, i32> {
            self.inner.mprotect(PROT_READ | PROT_EXEC)?;
            Ok(Mmap { inner: self.inner })
        }

        #[inline]
        pub fn as_ptr(&self) -> *const u8 {
            self.inner.ptr()
        }

        #[inline]
        pub fn as_mut_ptr(&mut self) -> *mut u8 {
            self.inner.mut_ptr()
        }
    }

    impl Deref for MmapMut {
        type Target = [u8];
        #[inline]
        fn deref(&self) -> &[u8] {
            unsafe { core::slice::from_raw_parts(self.inner.ptr(), self.inner.len()) }
        }
    }

    impl DerefMut for MmapMut {
        #[inline]
        fn deref_mut(&mut self) -> &mut [u8] {
            unsafe { core::slice::from_raw_parts_mut(self.inner.mut_ptr(), self.inner.len()) }
        }
    }
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
pub use imp::{Mmap, MmapMut, page_size};
```

## File: `kit/notlibc/src/syscall.rs`
```rust
//! Raw inline-assembly Linux syscall helpers for x86-64.
//!
//! Each function issues the `syscall` instruction with the given arguments and
//! returns the kernel's raw return value (negative → errno on error).
//! All are marked `unsafe`; callers are responsible for argument validity.

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
#[inline(always)]
pub(crate) unsafe fn syscall1(nr: usize, a0: usize) -> isize {
    let ret: isize;
    unsafe {
        core::arch::asm!(
            "syscall",
            inlateout("rax") nr => ret,
            in("rdi") a0,
            lateout("rcx") _,
            lateout("r11") _,
            options(nostack, preserves_flags),
        );
    }
    ret
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
#[inline(always)]
pub(crate) unsafe fn syscall2(nr: usize, a0: usize, a1: usize) -> isize {
    let ret: isize;
    unsafe {
        core::arch::asm!(
            "syscall",
            inlateout("rax") nr => ret,
            in("rdi") a0,
            in("rsi") a1,
            lateout("rcx") _,
            lateout("r11") _,
            options(nostack, preserves_flags),
        );
    }
    ret
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
#[inline(always)]
pub(crate) unsafe fn syscall3(nr: usize, a0: usize, a1: usize, a2: usize) -> isize {
    let ret: isize;
    unsafe {
        core::arch::asm!(
            "syscall",
            inlateout("rax") nr => ret,
            in("rdi") a0,
            in("rsi") a1,
            in("rdx") a2,
            lateout("rcx") _,
            lateout("r11") _,
            options(nostack, preserves_flags),
        );
    }
    ret
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
#[inline(always)]
pub(crate) unsafe fn syscall4(nr: usize, a0: usize, a1: usize, a2: usize, a3: usize) -> isize {
    let ret: isize;
    unsafe {
        core::arch::asm!(
            "syscall",
            inlateout("rax") nr => ret,
            in("rdi") a0,
            in("rsi") a1,
            in("rdx") a2,
            in("r10") a3,
            lateout("rcx") _,
            lateout("r11") _,
            options(nostack, preserves_flags),
        );
    }
    ret
}

#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
#[inline(always)]
pub(crate) unsafe fn syscall6(
    nr: usize,
    a0: usize,
    a1: usize,
    a2: usize,
    a3: usize,
    a4: usize,
    a5: usize,
) -> isize {
    let ret: isize;
    unsafe {
        core::arch::asm!(
            "syscall",
            inlateout("rax") nr => ret,
            in("rdi") a0,
            in("rsi") a1,
            in("rdx") a2,
            in("r10") a3,
            in("r8")  a4,
            in("r9")  a5,
            lateout("rcx") _,
            lateout("r11") _,
            options(nostack, preserves_flags),
        );
    }
    ret
}
```

## File: `kit/notlibc/src/syscall_nr.rs`
```rust
//! Linux syscall numbers for each supported architecture.
//!
//! Add a new `#[cfg(target_arch = "…")]` block when porting to a new arch.

#[cfg(target_arch = "x86_64")]
pub mod x86_64 {
    pub const SYS_READ: usize = 0;
    pub const SYS_WRITE: usize = 1;
    pub const SYS_CLOSE: usize = 3;
    pub const SYS_MMAP: usize = 9;
    pub const SYS_MPROTECT: usize = 10;
    pub const SYS_MUNMAP: usize = 11;
    pub const SYS_GETTID: usize = 186;
    pub const SYS_EPOLL_WAIT: usize = 232;
    pub const SYS_EPOLL_CTL: usize = 233;
    pub const SYS_OPENAT: usize = 257;
    pub const SYS_EVENTFD2: usize = 290;
    pub const SYS_EPOLL_CREATE1: usize = 291;
}
```

## File: `kit/notlibc/tests/eventfd.rs`
```rust
//! Integration tests for `notlibc::eventfd`.
//!
//! libc is used only in the test harness for draining fds and verifying
//! counts; production code uses no libc.

#![cfg(all(target_arch = "x86_64", target_os = "linux"))]

use notlibc::eventfd::{EventFd, EventSet};
use std::sync::Arc;
use std::thread;

// ── helpers ───────────────────────────────────────────────────────────────────

/// Drain one unit from a semaphore-mode eventfd.
/// Returns the value read (always 1 for semaphore mode) or the negative errno.
fn drain_one(fd: i32) -> i64 {
    let mut buf: u64 = 0;
    let ret = unsafe { libc::read(fd, &mut buf as *mut u64 as *mut libc::c_void, 8) };
    if ret < 0 {
        let errno = unsafe { *libc::__errno_location() };
        -(errno as i64)
    } else {
        buf as i64
    }
}

// ── EventFd tests ─────────────────────────────────────────────────────────────

#[test]
fn create_returns_valid_fd() {
    let efd = EventFd::new().expect("EventFd::new should succeed");
    assert!(efd.as_fd() >= 0, "fd must be non-negative");
    // Drop closes the fd automatically.
}

#[test]
fn notify_once_drain_reads_one() {
    let efd = EventFd::new().expect("EventFd::new");
    efd.notify();
    assert_eq!(drain_one(efd.as_fd()), 1);
}

#[test]
fn notify_twice_drain_twice_accumulates() {
    let efd = EventFd::new().expect("EventFd::new");
    efd.notify();
    efd.notify();
    // Semaphore mode: each read decrements by 1 and returns 1.
    assert_eq!(drain_one(efd.as_fd()), 1);
    assert_eq!(drain_one(efd.as_fd()), 1);
}

#[test]
fn non_blocking_second_read_returns_eagain() {
    let efd = EventFd::new().expect("EventFd::new");
    efd.notify();
    let _ = drain_one(efd.as_fd()); // drain the one notification
    let ret = drain_one(efd.as_fd()); // should be EAGAIN
    assert_eq!(
        ret,
        -(libc::EAGAIN as i64),
        "empty non-blocking eventfd should return EAGAIN, got {ret}"
    );
}

// ── EventSet tests ────────────────────────────────────────────────────────────

#[test]
fn event_set_single_fd_wait() {
    let efd = EventFd::new().expect("EventFd::new");
    let mut set = EventSet::new().expect("EventSet::new");
    let idx = set.add(&efd).expect("EventSet::add");
    assert_eq!(idx, 0);

    efd.notify();
    let fired = set.wait(-1).expect("EventSet::wait");
    assert_eq!(fired, 0);
}

#[test]
fn event_set_identifies_which_fd_fired() {
    // Register 4 eventfds; notify only the third one (index 2).
    let efds: Vec<EventFd> = (0..4).map(|_| EventFd::new().unwrap()).collect();
    let mut set = EventSet::new().unwrap();
    for efd in &efds {
        set.add(efd).unwrap();
    }

    efds[2].notify();
    let fired = set.wait(-1).unwrap();
    assert_eq!(fired, 2, "expected index 2 to fire");
}

#[test]
fn event_set_16_threads_one_reader() {
    const N: usize = 16;

    // Create 16 eventfds and an EventSet.
    let efds: Vec<Arc<EventFd>> = (0..N).map(|_| Arc::new(EventFd::new().unwrap())).collect();
    let mut set = EventSet::new().unwrap();
    for efd in &efds {
        set.add(efd).unwrap();
    }

    // Notify from thread 7.
    let notifier = Arc::clone(&efds[7]);
    let handle = thread::spawn(move || {
        notifier.notify();
    });

    let fired = set.wait(-1).unwrap();
    handle.join().unwrap();

    assert_eq!(fired, 7, "thread 7 should have fired index 7, got {fired}");
}

#[test]
fn event_set_all_16_threads_notify_wait_sees_at_least_one() {
    const N: usize = 16;

    let efds: Vec<Arc<EventFd>> = (0..N).map(|_| Arc::new(EventFd::new().unwrap())).collect();
    let mut set = EventSet::new().unwrap();
    for efd in &efds {
        set.add(efd).unwrap();
    }

    // All 16 threads notify simultaneously.
    let handles: Vec<_> = efds
        .iter()
        .map(|efd| {
            let efd = Arc::clone(efd);
            thread::spawn(move || efd.notify())
        })
        .collect();

    // Wait should return as soon as any one fires.
    let fired = set.wait(-1).unwrap();
    assert!(fired < N, "fired index {fired} out of range");

    for h in handles {
        h.join().unwrap();
    }
}
```

## File: `kit/notlibc/tests/lock.rs`
```rust
#[test]
fn mutex_new_lock_mutate_release() {
    let m = notlibc::Mutex::new(0u32);
    {
        let mut guard = m.lock();
        *guard = 42;
    }
    let guard = m.lock();
    assert_eq!(*guard, 42);
}

#[test]
fn shard_mutex_alias_usable() {
    let m: notlibc::ShardMutex<u32> = notlibc::ShardMutex::new(0u32);
    {
        let mut guard = m.lock();
        *guard = 7;
    }
    assert_eq!(*m.lock(), 7);
}
```

## File: `kit/notlibc/tests/mmap.rs`
```rust
#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
mod tests {
    use notlibc::mmap::{Mmap, MmapMut, page_size};

    #[test]
    fn page_size_is_power_of_two() {
        let ps = page_size();
        assert!(ps > 0);
        assert!(ps.is_power_of_two(), "page_size={ps} is not a power of two");
    }

    #[test]
    fn page_size_matches_libc() {
        // Verify that our AT_PAGESZ-based reading returns the same value as
        // the libc sysconf(_SC_PAGESIZE) call.
        let libc_ps = unsafe { libc::sysconf(libc::_SC_PAGESIZE) } as usize;
        assert_eq!(
            page_size(),
            libc_ps,
            "page_size() differs from libc sysconf"
        );
    }

    #[test]
    fn mmap_mut_write_read() {
        let mut map = MmapMut::map_anon(page_size()).expect("MmapMut::map_anon");
        assert_eq!(map.len(), page_size());

        let pattern: &[u8] = b"hello sig_safety";
        map[..pattern.len()].copy_from_slice(pattern);
        assert_eq!(&map[..pattern.len()], pattern);
    } // <-- Drop unmaps

    #[test]
    fn mmap_mut_drop_unmaps() {
        // Allocate and immediately drop — should not crash or leak.
        let map = MmapMut::map_anon(page_size()).expect("MmapMut::map_anon");
        drop(map);
    }

    #[test]
    fn make_read_only_transition() {
        let mut map = MmapMut::map_anon(page_size()).expect("MmapMut::map_anon");
        map[0] = 42;
        let ro: Mmap = map.make_read_only().expect("make_read_only");
        assert_eq!(ro[0], 42);
        // Deref to &[u8] works.
        assert_eq!(ro.len(), page_size());
    }

    #[test]
    fn make_read_only_then_make_mut() {
        let map = MmapMut::map_anon(page_size()).expect("MmapMut::map_anon");
        let ro = map.make_read_only().expect("make_read_only");
        let mut rw = ro.make_mut().expect("make_mut");
        rw[0] = 0xff;
        assert_eq!(rw[0], 0xff);
    }

    #[test]
    fn make_exec_transition() {
        // We just verify the mprotect succeeds; actually executing the mapping
        // is out of scope for this test.
        let map = MmapMut::map_anon(page_size()).expect("MmapMut::map_anon");
        map.make_exec().expect("make_exec");
    }

    #[test]
    fn zero_len_mapping_is_empty() {
        // memmap2 allows zero-length maps; we follow the same convention.
        let map = MmapMut::map_anon(0).expect("MmapMut::map_anon(0)");
        assert_eq!(map.len(), 0);
        assert!(map.is_empty());
    }

    #[test]
    fn multi_page_allocation() {
        let size = page_size() * 4;
        let mut map = MmapMut::map_anon(size).expect("MmapMut::map_anon 4 pages");
        // Write to first and last byte of every page.
        for i in 0..4usize {
            let base = i * page_size();
            map[base] = i as u8;
            map[base + page_size() - 1] = (i + 10) as u8;
        }
        for i in 0..4usize {
            let base = i * page_size();
            assert_eq!(map[base], i as u8);
            assert_eq!(map[base + page_size() - 1], (i + 10) as u8);
        }
    }
}
```

## File: `kit/notlibc/tests/syscall_nr.rs`
```rust
/// Verify that every constant in `syscall_nr::x86_64` matches the value
/// exported by the `libc` crate.  This catches copy-paste errors and makes
/// future arch additions easier to validate.
#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
mod x86_64 {
    use notlibc::syscall_nr::x86_64;

    #[test]
    fn syscall_numbers_match_libc() {
        assert_eq!(x86_64::SYS_READ, libc::SYS_read as usize);
        assert_eq!(x86_64::SYS_WRITE, libc::SYS_write as usize);
        assert_eq!(x86_64::SYS_CLOSE, libc::SYS_close as usize);
        assert_eq!(x86_64::SYS_MMAP, libc::SYS_mmap as usize);
        assert_eq!(x86_64::SYS_MPROTECT, libc::SYS_mprotect as usize);
        assert_eq!(x86_64::SYS_MUNMAP, libc::SYS_munmap as usize);
        assert_eq!(x86_64::SYS_EPOLL_WAIT, libc::SYS_epoll_wait as usize);
        assert_eq!(x86_64::SYS_EPOLL_CTL, libc::SYS_epoll_ctl as usize);
        assert_eq!(x86_64::SYS_OPENAT, libc::SYS_openat as usize);
        assert_eq!(x86_64::SYS_EVENTFD2, libc::SYS_eventfd2 as usize);
        assert_eq!(x86_64::SYS_EPOLL_CREATE1, libc::SYS_epoll_create1 as usize);
    }
}
```

## File: `kit/pprof_enc/Cargo.toml`
```
[package]
name = "pprof_enc"
version = "0.1.0"
edition = "2024"
publish = false

[dependencies]
prost = { workspace = true }
```

## File: `kit/pprof_enc/src/lib.rs`
```rust
// Minimal pprof protobuf encoder.
//
// Defines pprof message structs inline using prost derive macros (no .proto file).
// Encodes to protobuf bytes with prost.

use std::collections::HashMap;

use prost::Message;

// ---------------------------------------------------------------------------
// Pprof protobuf message types (inline, matching google/pprof profile.proto)
// ---------------------------------------------------------------------------

#[derive(Clone, PartialEq, Message)]
pub struct Profile {
    /// A description of the samples associated with each Sample.value.
    #[prost(message, repeated, tag = "1")]
    pub sample_type: Vec<ValueType>,
    /// The set of samples recorded in this profile.
    #[prost(message, repeated, tag = "2")]
    pub sample: Vec<Sample>,
    /// All locations referenced by this profile.
    #[prost(message, repeated, tag = "4")]
    pub location: Vec<Location>,
    /// All functions referenced by this profile.
    #[prost(message, repeated, tag = "5")]
    pub function: Vec<Function>,
    /// A common table for strings referenced by various messages.
    /// Index 0 must always be "".
    #[prost(string, repeated, tag = "6")]
    pub string_table: Vec<String>,
    /// Time of collection (approximate), as nanoseconds past the Unix epoch.
    #[prost(int64, tag = "9")]
    pub time_nanos: i64,
    /// Duration of the profile, if a duration makes sense, in nanoseconds.
    #[prost(int64, tag = "10")]
    pub duration_nanos: i64,
    /// The kind of events between sampled occurrences.
    #[prost(message, optional, tag = "11")]
    pub period_type: Option<ValueType>,
    /// The number of events between sampled occurrences.
    #[prost(int64, tag = "12")]
    pub period: i64,
}

#[derive(Clone, PartialEq, Message)]
pub struct ValueType {
    /// Index into string_table for the type name (e.g. "cpu").
    #[prost(int64, tag = "1")]
    pub r#type: i64,
    /// Index into string_table for the unit (e.g. "nanoseconds").
    #[prost(int64, tag = "2")]
    pub unit: i64,
}

#[derive(Clone, PartialEq, Message)]
pub struct Sample {
    /// The IDs of the location (frame) for this sample, from leaf to root.
    #[prost(uint64, repeated, tag = "1")]
    pub location_id: Vec<u64>,
    /// The type-specific measurement values for this sample.
    #[prost(int64, repeated, tag = "2")]
    pub value: Vec<i64>,
}

#[derive(Clone, PartialEq, Message)]
pub struct Location {
    /// Unique nonzero id for this location.
    #[prost(uint64, tag = "1")]
    pub id: u64,
    /// The set of inlined functions at this location.
    #[prost(message, repeated, tag = "4")]
    pub line: Vec<Line>,
}

#[derive(Clone, PartialEq, Message)]
pub struct Line {
    /// Index into Profile.function for the function executed at this line.
    #[prost(uint64, tag = "1")]
    pub function_id: u64,
    /// Line number in source code.
    #[prost(int64, tag = "2")]
    pub line: i64,
}

#[derive(Clone, PartialEq, Message)]
pub struct Function {
    /// Unique nonzero id for this function.
    #[prost(uint64, tag = "1")]
    pub id: u64,
    /// Index into string_table for the name of the function.
    #[prost(int64, tag = "2")]
    pub name: i64,
    /// Index into string_table for the source file containing the function.
    #[prost(int64, tag = "4")]
    pub filename: i64,
    /// Line number in source file of start of function.
    #[prost(int64, tag = "5")]
    pub start_line: i64,
}

// ---------------------------------------------------------------------------
// String table with deduplication
// ---------------------------------------------------------------------------

struct StringTable {
    strings: Vec<String>,
    index: HashMap<String, i64>,
}

impl StringTable {
    fn new() -> Self {
        // Index 0 must always be "" per spec.
        let mut st = StringTable {
            strings: Vec::new(),
            index: HashMap::new(),
        };
        st.intern("");
        st
    }

    fn intern(&mut self, s: &str) -> i64 {
        if let Some(&idx) = self.index.get(s) {
            return idx;
        }
        let idx = self.strings.len() as i64;
        self.strings.push(s.to_owned());
        self.index.insert(s.to_owned(), idx);
        idx
    }
}

// ---------------------------------------------------------------------------
// Frame — a single symbolized stack frame
// ---------------------------------------------------------------------------

pub struct Frame<'a> {
    pub function_name: &'a str,
    pub filename: &'a str,
    pub first_line: i64,
}

// ---------------------------------------------------------------------------
// ProfileBuilder — accumulates samples and produces an encoded profile
// ---------------------------------------------------------------------------

pub struct ProfileBuilder {
    st: StringTable,
    functions: Vec<Function>,
    /// Map from (name_idx, filename_idx, start_line) → function id (1-based)
    func_index: HashMap<(i64, i64, i64), u64>,
    locations: Vec<Location>,
    /// Map from function id → location id (1-based); one location per function
    loc_index: HashMap<u64, u64>,
    samples: Vec<Sample>,
    /// Map from location_id sequence → index into self.samples (for merging)
    sample_index: HashMap<Vec<u64>, usize>,
    time_nanos: i64,
    duration_nanos: i64,
    period: i64,
}

impl ProfileBuilder {
    /// Create a new builder.
    ///
    /// * `time_nanos`     — profile start time (Unix epoch nanoseconds)
    /// * `duration_nanos` — duration covered by this profile in nanoseconds
    /// * `period`         — sampling period in nanoseconds (e.g. 10_000_000 for 10 ms)
    pub fn new(time_nanos: i64, duration_nanos: i64, period: i64) -> Self {
        ProfileBuilder {
            st: StringTable::new(),
            functions: Vec::new(),
            func_index: HashMap::new(),
            locations: Vec::new(),
            loc_index: HashMap::new(),
            samples: Vec::new(),
            sample_index: HashMap::new(),
            time_nanos,
            duration_nanos,
            period,
        }
    }

    /// Add a sample consisting of a symbolized stack and a hit count.
    ///
    /// Frames should be ordered leaf-first (innermost frame first).
    /// The value stored is `count * period` (CPU nanoseconds).
    /// If an identical stack (same location_id sequence) was already added,
    /// the values are merged (summed) instead of creating a duplicate sample.
    pub fn add_sample(&mut self, frames: &[Frame<'_>], count: i64) {
        let mut location_ids: Vec<u64> = Vec::with_capacity(frames.len());
        for frame in frames {
            let func_id = self.intern_function(frame);
            let loc_id = self.intern_location(func_id, frame.first_line);
            location_ids.push(loc_id);
        }
        let value = count * self.period;
        if let Some(&idx) = self.sample_index.get(&location_ids) {
            self.samples[idx].value[0] += value;
        } else {
            let idx = self.samples.len();
            self.samples.push(Sample {
                location_id: location_ids.clone(),
                value: vec![value],
            });
            self.sample_index.insert(location_ids, idx);
        }
    }

    /// Reset all accumulated state so the builder can be reused for the next
    /// profile window. Keeps the allocated capacity for efficiency.
    pub fn reset(&mut self, time_nanos: i64, duration_nanos: i64) {
        self.st = StringTable::new();
        self.functions.clear();
        self.func_index.clear();
        self.locations.clear();
        self.loc_index.clear();
        self.samples.clear();
        self.sample_index.clear();
        self.time_nanos = time_nanos;
        self.duration_nanos = duration_nanos;
    }

    /// Return the number of accumulated samples (unique stacks).
    pub fn len(&self) -> usize {
        self.samples.len()
    }

    /// Return true if no samples have been accumulated.
    pub fn is_empty(&self) -> bool {
        self.samples.is_empty()
    }

    fn intern_function(&mut self, frame: &Frame<'_>) -> u64 {
        let name_idx = self.st.intern(frame.function_name);
        let filename_idx = self.st.intern(frame.filename);
        let start_line = frame.first_line;
        let key = (name_idx, filename_idx, start_line);
        if let Some(&id) = self.func_index.get(&key) {
            return id;
        }
        let id = (self.functions.len() + 1) as u64;
        self.functions.push(Function {
            id,
            name: name_idx,
            filename: filename_idx,
            start_line,
        });
        self.func_index.insert(key, id);
        id
    }

    fn intern_location(&mut self, func_id: u64, line: i64) -> u64 {
        if let Some(&id) = self.loc_index.get(&func_id) {
            return id;
        }
        let id = (self.locations.len() + 1) as u64;
        self.locations.push(Location {
            id,
            line: vec![Line {
                function_id: func_id,
                line,
            }],
        });
        self.loc_index.insert(func_id, id);
        id
    }

    /// Encode the profile to protobuf bytes.
    pub fn encode(&mut self) -> Vec<u8> {
        let cpu_type_idx = self.st.intern("cpu");
        let nanos_idx = self.st.intern("nanoseconds");
        let value_type = ValueType {
            r#type: cpu_type_idx,
            unit: nanos_idx,
        };

        let profile = Profile {
            sample_type: vec![value_type.clone()],
            sample: core::mem::take(&mut self.samples),
            location: core::mem::take(&mut self.locations),
            function: core::mem::take(&mut self.functions),
            string_table: core::mem::take(&mut self.st.strings),
            time_nanos: self.time_nanos,
            duration_nanos: self.duration_nanos,
            period_type: Some(value_type),
            period: self.period,
        };

        profile.encode_to_vec()
    }
}

// ---------------------------------------------------------------------------
// Tests
// ---------------------------------------------------------------------------

#[cfg(test)]
mod tests {
    use super::*;

    fn make_frame<'a>(name: &'a str, file: &'a str, line: i64) -> Frame<'a> {
        Frame {
            function_name: name,
            filename: file,
            first_line: line,
        }
    }

    #[test]
    fn string_table_starts_with_empty() {
        let mut st = StringTable::new();
        assert_eq!(st.strings[0], "");
        assert_eq!(st.intern(""), 0);
    }

    #[test]
    fn string_table_deduplicates() {
        let mut st = StringTable::new();
        let a = st.intern("hello");
        let b = st.intern("hello");
        assert_eq!(a, b);
        assert_eq!(st.strings.len(), 2); // "" and "hello"
    }

    #[test]
    fn encode_empty_profile_is_valid_protobuf() {
        let mut builder = ProfileBuilder::new(0, 15_000_000_000, 10_000_000);
        let bytes = builder.encode();
        assert!(!bytes.is_empty());
        let profile = Profile::decode(bytes.as_slice()).unwrap();
        assert_eq!(profile.string_table[0], "");
    }

    #[test]
    fn encode_single_sample() {
        let mut builder = ProfileBuilder::new(1_000_000_000, 15_000_000_000, 10_000_000);
        let frames = vec![
            make_frame("leaf_fn", "leaf.rs", 10),
            make_frame("root_fn", "root.rs", 1),
        ];
        builder.add_sample(&frames, 3);
        let bytes = builder.encode();

        let profile = Profile::decode(bytes.as_slice()).unwrap();

        // string_table[0] must be ""
        assert_eq!(profile.string_table[0], "");

        // One sample with value = count * period = 3 * 10_000_000
        assert_eq!(profile.sample.len(), 1);
        assert_eq!(profile.sample[0].value, vec![30_000_000i64]);
        assert_eq!(profile.sample[0].location_id.len(), 2);

        // Two locations, two functions
        assert_eq!(profile.location.len(), 2);
        assert_eq!(profile.function.len(), 2);

        // period and period_type
        assert_eq!(profile.period, 10_000_000);
        assert!(profile.period_type.is_some());

        // time / duration
        assert_eq!(profile.time_nanos, 1_000_000_000);
        assert_eq!(profile.duration_nanos, 15_000_000_000);
    }

    #[test]
    fn merges_identical_stacks() {
        let mut builder = ProfileBuilder::new(0, 15_000_000_000, 10_000_000);
        let frames = vec![make_frame("main", "main.rs", 1)];
        builder.add_sample(&frames, 1);
        builder.add_sample(&frames, 2);
        let bytes = builder.encode();

        let profile = Profile::decode(bytes.as_slice()).unwrap();
        assert_eq!(profile.function.len(), 1);
        assert_eq!(profile.location.len(), 1);
        // Identical stacks are merged into one sample with summed value.
        assert_eq!(profile.sample.len(), 1);
        assert_eq!(profile.sample[0].value, vec![(1 + 2) * 10_000_000i64]);
    }
}
```

## File: `kit/pyroscope_ingest/Cargo.toml`
```
[package]
name = "pyroscope_ingest"
version = "0.1.0"
edition = "2021"
publish = false

[dependencies]
ureq = "3"
anyhow = "1.0"
prost = { workspace = true }
uuid = { workspace = true }
flate2 = { workspace = true }

[dev-dependencies]
mockito = "1"
```

## File: `kit/pyroscope_ingest/src/lib.rs`
```rust
mod push;

use std::io::Write as _;
use std::time::Duration;

use anyhow::Result;
use flate2::write::GzEncoder;
use flate2::Compression;
use prost::Message;
use push::{LabelPair, PushRequest, RawProfileSeries, RawSample};

/// Send a pprof profile to the Pyroscope push API.
///
/// - `base_url`: e.g. `"http://localhost:4040"`
/// - `app_name`: application name; sent as `service_name` label
/// - `pprof`: raw (uncompressed) pprof protobuf bytes
/// - `_from`: profile start time (Unix seconds) — unused by push API, kept for caller compat
/// - `_until`: profile end time (Unix seconds) — unused by push API, kept for caller compat
///
/// Errors are returned but do not retry — callers should log and discard on failure.
pub fn send(
    base_url: &str,
    app_name: &str,
    tags: &[(&str, &str)],
    pprof: &[u8],
    _from: u64,
    _until: u64,
) -> Result<()> {
    let mut labels = vec![
        LabelPair {
            name: "service_name".to_string(),
            value: app_name.to_string(),
        },
        LabelPair {
            name: "__name__".to_string(),
            value: "process_cpu".to_string(),
        },
    ];
    for &(k, v) in tags {
        labels.push(LabelPair {
            name: k.to_string(),
            value: v.to_string(),
        });
    }
    let req = PushRequest {
        series: vec![RawProfileSeries {
            labels,
            samples: vec![RawSample {
                raw_profile: pprof.to_vec(),
                id: uuid::Uuid::new_v4().to_string(),
            }],
        }],
    };

    let proto_bytes = req.encode_to_vec();

    let mut gz = GzEncoder::new(Vec::new(), Compression::default());
    gz.write_all(&proto_bytes)?;
    let body = gz.finish()?;

    let url = format!(
        "{}/push.v1.PusherService/Push",
        base_url.trim_end_matches('/')
    );
    let agent = ureq::Agent::config_builder()
        .timeout_global(Some(Duration::from_secs(10)))
        .build()
        .new_agent();
    agent
        .post(&url)
        .header("Content-Type", "application/proto")
        .header("Content-Encoding", "gzip")
        .send(&body)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_send_happy_path() {
        let mut server = mockito::Server::new();
        let mock = server
            .mock("POST", "/push.v1.PusherService/Push")
            .with_status(200)
            .create();

        let result = send(&server.url(), "myapp", &[], b"fakepprof", 1000, 2000);
        assert!(result.is_ok(), "expected Ok, got: {:?}", result);
        mock.assert();
    }

    #[test]
    fn test_send_server_error() {
        let mut server = mockito::Server::new();
        let _mock = server
            .mock("POST", "/push.v1.PusherService/Push")
            .with_status(500)
            .create();

        let result = send(&server.url(), "myapp", &[], b"fakepprof", 1000, 2000);
        assert!(result.is_err(), "expected Err on 500, got Ok");
    }

    #[test]
    fn test_send_headers_and_body() {
        let mut server = mockito::Server::new();
        let mock = server
            .mock("POST", "/push.v1.PusherService/Push")
            .match_header("content-type", "application/proto")
            .match_header("content-encoding", "gzip")
            .match_body(mockito::Matcher::Any)
            .with_status(200)
            .create();

        let result = send(&server.url(), "myapp", &[], b"\x0a\x0b", 100, 200);
        assert!(result.is_ok(), "expected Ok, got: {:?}", result);
        mock.assert();
    }

    #[test]
    fn test_send_includes_tags_as_labels() {
        let mut server = mockito::Server::new();
        let mock = server
            .mock("POST", "/push.v1.PusherService/Push")
            .match_header("content-type", "application/proto")
            .match_header("content-encoding", "gzip")
            .with_status(200)
            .create();

        let tags = vec![("env", "prod"), ("region", "us-east")];
        let result = send(&server.url(), "myapp", &tags, b"fakepprof", 100, 200);
        assert!(result.is_ok(), "expected Ok, got: {:?}", result);
        mock.assert();
    }

    #[test]
    fn test_push_request_contains_tags() {
        let tags = vec![("env", "prod"), ("canary", "abc123")];

        let mut labels = vec![
            LabelPair {
                name: "service_name".to_string(),
                value: "myapp".to_string(),
            },
            LabelPair {
                name: "__name__".to_string(),
                value: "process_cpu".to_string(),
            },
        ];
        for &(k, v) in &tags {
            labels.push(LabelPair {
                name: k.to_string(),
                value: v.to_string(),
            });
        }

        assert_eq!(labels.len(), 4);
        assert_eq!(labels[2].name, "env");
        assert_eq!(labels[2].value, "prod");
        assert_eq!(labels[3].name, "canary");
        assert_eq!(labels[3].value, "abc123");
    }
}
```

## File: `kit/pyroscope_ingest/src/push.rs`
```rust
// Push API protobuf types, copied from src/encode/gen/push.rs and src/encode/gen/types.rs.
// These match the Pyroscope push.v1.PusherService/Push protobuf schema.

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct PushRequest {
    #[prost(message, repeated, tag = "1")]
    pub series: ::prost::alloc::vec::Vec<RawProfileSeries>,
}

#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RawProfileSeries {
    #[prost(message, repeated, tag = "1")]
    pub labels: ::prost::alloc::vec::Vec<LabelPair>,
    #[prost(message, repeated, tag = "2")]
    pub samples: ::prost::alloc::vec::Vec<RawSample>,
}

#[derive(Clone, PartialEq, Eq, Hash, ::prost::Message)]
pub struct RawSample {
    #[prost(bytes = "vec", tag = "1")]
    pub raw_profile: ::prost::alloc::vec::Vec<u8>,
    #[prost(string, tag = "2")]
    pub id: ::prost::alloc::string::String,
}

#[derive(Clone, PartialEq, Eq, Hash, ::prost::Message)]
pub struct LabelPair {
    #[prost(string, tag = "1")]
    pub name: ::prost::alloc::string::String,
    #[prost(string, tag = "2")]
    pub value: ::prost::alloc::string::String,
}
```

## File: `kit/pysignalprof/Cargo.toml`
```
[package]
name = "pysignalprof"
version = "0.1.0"
edition = "2024"
publish = false

[features]
default = []
debug-print = ["notlibc/debug-print", "python_unwind/debug-print"]

[dependencies]
kindasafe_init = { path = "../kindasafe_init" }
kindasafe = { path = "../kindasafe" }
python_offsets = { path = "../python_offsets" }
python_offsets_types = { path = "../python_offsets_types" }
python_unwind = { path = "../python_unwind" }
sig_ring = { path = "../sig_ring" }
sighandler = { path = "../sighandler" }
notlibc = { path = "../notlibc" }
bbqueue = "0.5"
libc = { version = "0.2.182" }
pprof_enc = { path = "../pprof_enc" }
pyroscope_ingest = { path = "../pyroscope_ingest" }
```

## File: `kit/pysignalprof/design.md`
```markdown
# Signal-Based CPU Profiler for Python — Unified Design Document

## Preface: Review of Prior Proposals

This document synthesizes the best ideas from three prior design proposals (designs/2.md, 3.md, 4.md), the hackathon-profiler prototype, and reference profiler implementations (async-profiler 3.0, gperftools, pprof-rs, Go 1.26 runtime). Each proposal was reviewed for correctness, completeness, and practicality. Key issues found:

**Proposal 2** ("The Detailed One"): Best overall structure and technical depth. Correct frame_owner handling (skips only CSTACK frames). Good sharding design. Issues: reads `co_code_adaptive` per frame in the handler unnecessarily; errno save/restore via libc calls; over-engineered TimerBackend trait.

**Proposal 3** ("The Practical One"): Good errno save/restore awareness, practical reset protocol using sigprocmask. Issues: fixed-size 4KB ring buffer entries (wasteful); wrong frame_owner handling (stops at generators); no sharding (single global SpinMutex); fragile TLS access via autoTSSkey formula; errno save/restore calls __errno_location() which is itself a libc function.

**Proposal 4** ("The Modular One"): Most decomposed crate structure; raw syscall wrappers; double-buffer idea for hash map reset. Issues: wrong frame_owner handling; redundant nanolibc vs libc; too many crates without clear benefit.

**Common errors**: Proposals 3 and 4 incorrectly stop frame walking at generator frames (owner != 0). Only `FRAME_OWNED_BY_CSTACK` (3) should be skipped — generators (1) and frame-object-backed frames (2) contain valid Python frames. None properly address the 3.14 `_PyInterpreterFrame` layout changes from 3.13.

---

## Table of Contents

1. [Goals and Non-Goals](#1-goals-and-non-goals)
2. [Architecture Overview](#2-architecture-overview)
3. [Crate Layout](#3-crate-layout)
4. [OS APIs and Syscalls](#4-os-apis-and-syscalls)
5. [Initialization and Discovery](#5-initialization-and-discovery)
6. [Signal Handler](#6-signal-handler)
7. [Python Stack Unwinding](#7-python-stack-unwinding)
8. [Async-Signal-Safe Primitives](#8-async-signal-safe-primitives)
9. [Collection: Per-Shard SPSC Queue (bbqueue)](#9-collection-per-shard-spsc-queue-kitsig_ring)
10. [Reader Thread and Periodic Flush](#10-reader-thread-and-periodic-flush)
11. [Symbolication](#11-symbolication)
12. [Pprof Generation](#12-pprof-generation)
13. [Pyroscope Ingestion](#13-pyroscope-ingestion)
14. [Shared Library Interface](#14-shared-library-interface)
15. [Concurrency Model](#15-concurrency-model)
16. [Memory Management](#16-memory-management)
17. [Error Handling](#17-error-handling)
18. [Future Work](#18-future-work)
19. [Appendix: CPython 3.14 Structures](#appendix-cpython-314-structures)

---

## 1. Goals and Non-Goals

### Goals

- **In-process, signal-based CPU profiler** for CPython, written in Rust.
- **`setitimer(ITIMER_PROF)` + `SIGPROF`** delivering a signal every **10ms of CPU time** (100 Hz). Design allows migration to per-thread `timer_create(CLOCK_THREAD_CPUTIME_ID)` later.
- **Fully async-signal-safe signal handler**: no malloc/free, **no libc function calls whatsoever**, no /proc reads, no syscalls beyond `gettid`. All code executing in signal handler context must be `#![no_std]` and must not depend on `libc` — use raw syscall wrappers or inline assembly instead. Memory is pre-allocated via raw `mmap` syscall. Spinlocks (from the `spin` crate) are try-lock only in the handler; full lock is used by the reader thread during dump.
- **Per-shard SPSC queue** (`kit/sig_ring`) for passing raw stack traces from signal handler to reader thread, built on the [`bbqueue`](https://github.com/jamesmunns/bbqueue) BipBuffer crate (`#![no_std]`, lockless, battle-tested in embedded/interrupt contexts). The handler requests a contiguous write grant, fills it with a variable-length record, and commits. Every N samples the handler notifies the reader thread via an `eventfd`. The reader also drains all queues on every 15s flush.
- **No CPython API calls, no linking against libpython** — discover everything by inspecting process memory as a debugger would. Read `/proc/self/maps`, parse ELF, use `_Py_DebugOffsets` from `_PyRuntime`.
- **Python 3.14 initially** — all offsets in a separate structure. Use `_Py_DebugOffsets` introspection to read as many offsets as possible; hardcode only what cannot be read.
- **Minimal handler work** — only unwind Python frames and record raw `(PyCodeObject*, instr_offset)` tuples. No string reads, no symbol resolution, no filename/line extraction in the handler.
- **Periodic flush** — every 15 seconds: drain collected samples, symbolize, build a pprof protobuf, HTTP POST it to a Pyroscope instance at `localhost:4040`.
- **Loadable via `dlopen`** — the profiler is a cdylib (`.so`). A single `extern "C"` function is called from Python via `ctypes`/`cffi` to start profiling. The profiler runs for the lifetime of the process — there is no stop function.
- **Reusable crates** — new crates must not depend on any existing workspace crates except `kindasafe` and `kindasafe_init`. They should be generic enough to reuse for Ruby/dotnet profilers later.
- **Small crates, minimal dependencies** — each crate does one thing and has as few external dependencies as possible.

### Non-Goals (Explicit Deferrals)

- Native/C/C++ frame unwinding — added later.
- Line numbers and filenames in the handler — symbolized later from code object pointers.
- Multiple Python version support in this iteration — 3.14 only, but offset table is version-parameterized.
- Free-threaded (no-GIL) Python support — future work.
- ARM64 support — x86_64 only initially, but keep architecture-specific code isolated.
- Production-grade error reporting, configuration API, or Python-level API.

---

## 2. Architecture Overview

### Data Flow

```
                              KERNEL
                                │
                 setitimer(ITIMER_PROF, 10ms)
                                │
                          SIGPROF delivery
                                │
                                ▼
                    ┌───────────────────────┐
                    │   Signal Handler      │
                    │                       │
                    │  1. [debug] Save errno│
                    │  2. Try-lock shard    │
                    │  3. Read TLS → find   │
                    │     PyThreadState     │
                    │  4. Walk Python       │
                    │     frame chain       │
                    │  5. Record raw stack  │
                    │     to collector      │
                    │  6. Unlock shard      │
                    │  7. [debug] Assert    │
                    │     errno unchanged   │
                    └──────────┬────────────┘
                               │
                               ▼
                  ┌────────────────────────┐
                  │  bbqueue SPSC Queue     │
                  │  (kit/sig_ring)         │
                  │  per-shard BipBuffer    │
                  │  variable-length records│
                  └──────────┬─────────────┘
                             │
                     eventfd notify every
                     N samples + 15s timer
                             │
                             ▼
                   ┌──────────────────────┐
                   │  Reader Thread        │
                   │  (kit/profiler_core)  │
                   │                       │
                   │  Wakes on:            │
                   │  - eventfd (batch)    │
                   │  - 15s timeout (flush)│
                   │                       │
                   │  1. Drain ring bufs   │
                   │  2. Aggregate stacks  │
                   │  3. Symbolize         │
                   │  4. Build pprof proto │
                   │  5. HTTP POST to      │
                   │     Pyroscope (on 15s)│
                   └──────────────────────┘
```

### Component Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                      pyroscope-rs workspace                         │
│                                                                     │
│  kit/                                                               │
│  ├── kindasafe/         (SPLIT FROM EXISTING) `#![no_std]` SIGSEGV- │
│  │                      safe memory reads — naked asm, no libc      │
│  ├── kindasafe_init/    (SPLIT FROM EXISTING) kindasafe init —      │
│  │                      sigaction-based SIGSEGV/SIGBUS recovery     │
│  │                      setup, depends on libc, NOT `#![no_std]`    │
│  ├── notlibc/        Async-signal-safe primitives                │
│  │                      raw mmap, eventfd, raw syscall helpers       │
│  ├── sig_ring/          Per-shard SPSC queue (wraps bbqueue)        │
│  ├── sighandler/        Signal registration, setitimer, timer mgmt  │
│  ├── python_offsets/    CPython version detection, _Py_DebugOffsets, │
│  │                      ELF symbol lookup, /proc/self/maps parsing  │
│  ├── python_unwind/     Signal-safe Python frame walking            │
│  ├── profiler_core/     Orchestration: reader thread, flush, symbol │
│  ├── pprof_enc/         Minimal pprof protobuf encoder              │
│  ├── pyroscope_ingest/  HTTP POST to Pyroscope push API             │
│  ├── pysignalprof/      Core profiler library: signal handler,      │
│  │                      reader thread, init, symbolization           │
│  └── pysignalprof_capi/ cdylib: thin C API wrapper, dlopen entry pt │
│                                                                     │
│  (existing crates — NOT depended upon by new crates)                │
│  ├── pyroscope/         Existing agent (not used)                   │
│  └── pyroscope_ffi/     Existing Python/Ruby FFI (not used)         │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 3. Crate Layout

Each crate has minimal dependencies. The dependency graph flows in one direction:

```
                     pysignalprof_capi (cdylib)
                             │
                        pysignalprof (lib)
                             │
                ┌────────────┼─────────────┐
                ▼            ▼              ▼
           sighandler   python_offsets   pprof_enc
                │            │
           ┌────┘       ┌────┘
           ▼            ▼
   kindasafe_init ──→ kindasafe     pyroscope_ingest
                      (#![no_std])
        python_unwind
             │
        ┌────┤
     kindasafe  notlibc
     (#![no_std])

     sig_ring
       │  │
       ▼  ▼
  notlibc  bbqueue
           (#![no_std])
```

**Note on kindasafe split**: The existing `kindasafe` crate is a single crate that depends on `libc` and `spin`, mixing signal-handler-safe read primitives (naked asm) with init-time code (`sigaction` installation, fallback handler chaining). It must be split into two crates before other signal-handler-path crates can depend on it:

- **`kindasafe`** (after split): `#![no_std]`, zero external dependencies. Contains only the naked-asm read primitives (`u64`, `slice`, `str`), the crash-point table, and the `crash_handler` function. The `crash_handler` currently references `libc::ucontext_t` for register access — this must be replaced with raw pointer arithmetic at known offsets (the `ucontext_t` layout is stable on Linux x86_64). No libc dependency after split.
- **`kindasafe_init`** (new crate): depends on `kindasafe`, `libc`, `spin`. Contains `init()`, `is_initialized()`, SIGSEGV/SIGBUS signal handler installation via `sigaction`, fallback handler chaining (`FALLBACK_SIGSEGV`/`FALLBACK_SIGBUS` statics), and `restore_default_signal_handler()`.

Signal-handler-path crates (`python_unwind`, `sig_ring`, etc.) depend on `kindasafe` (no_std). Init-time crates (`python_offsets`, `profiler_core`) depend on `kindasafe_init`.

### Crate Descriptions

| Crate | Type | Dependencies | Purpose |
|-------|------|-------------|---------|
| `kit/kindasafe` | lib (`#![no_std]`) | (none) | **Split from existing `kindasafe` crate.** SIGSEGV-safe memory read primitives: `u64()`, `slice()`, `str()` via naked assembly. Crash-point table and crash handler (manipulates `ucontext_t` via raw pointer offsets to skip faulting instructions). Currently the crash handler uses `libc::ucontext_t` types — these must be replaced with raw pointer arithmetic at fixed offsets for `#![no_std]`. **No libc dependency, no `std`** — uses only `core` and naked asm. Safe for use in signal handler context. |
| `kit/kindasafe_init` | lib | `kindasafe`, `libc`, `spin` | **Split from existing `kindasafe` crate.** Initialization for kindasafe: installs SIGSEGV/SIGBUS signal handlers via `sigaction` that delegate to `kindasafe::arch::crash_handler` for recovery. Manages fallback handler chaining (`FALLBACK_SIGSEGV`/`FALLBACK_SIGBUS` statics). Provides `init()` and `is_initialized()`. **Not `#![no_std]`** — depends on `libc` for `sigaction` and `ucontext_t` types. Called once at profiler startup, never from signal handler context. |
| `kit/notlibc` | lib (`#![no_std]`) | `spin` | Async-signal-safe primitives: raw `mmap`/`munmap` wrappers (via raw `syscall` instruction — no libc), `eventfd` wrapper. Re-exports `spin::Mutex` for shard locking. **No libc dependency.** Uses inline assembly for syscalls. |
| `kit/sig_ring` | lib (`#![no_std]`) | `bbqueue`, `notlibc` | Per-shard SPSC queue wrapping [`bbqueue`](https://github.com/jamesmunns/bbqueue) (a `#![no_std]`, lockless BipBuffer crate). One bbqueue instance per shard. Writer (signal handler) calls `grant_exact()` → fills record → `commit()`. Reader (background thread) calls `read()` → parses records → `release()`. Provides the record format (header + frames) and eventfd notification on top of bbqueue. **No libc dependency.** |
| `kit/sighandler` | lib | `libc` | Signal handler registration (`sigaction`), `setitimer` wrapper. Generic — not Python-specific. Note: this crate uses `libc` for `sigaction`/`setitimer` calls at **init time only** — it is never called from within the signal handler. |
| `kit/python_offsets` | lib | `kindasafe_init`, `libc` | CPython version detection, `_Py_DebugOffsets` reading, offset table structures. ELF symbol lookup for `_PyRuntime`, `Py_Version`, and `_PyThreadState_GetCurrent`. `/proc/self/maps` parsing. All done at **init time only** — not in signal handler. Uses `kindasafe` reads (via `kindasafe_init`) for safe memory access during discovery. |
| `kit/python_unwind` | lib (`#![no_std]`) | `kindasafe`, `notlibc` | Signal-safe Python frame walking. Reads `PyThreadState.current_frame` → `_PyInterpreterFrame` chain. Outputs `(PyCodeObject*, instr_offset)` tuples. **No libc dependency** — depends on `kindasafe` (the `#![no_std]` read crate), runs in signal handler context. |
| `kit/profiler_core` | lib | `sig_ring`, `python_unwind`, `python_offsets`, `pprof_enc`, `pyroscope_ingest`, `sighandler` | Orchestrator: owns the reader thread, periodic flush, stack aggregation, symbolication, pprof building, ingestion. |
| `kit/pprof_enc` | lib | `prost` | Minimal pprof protobuf encoder. String table, Function, Location, Sample messages. Gzip output via `flate2`. |
| `kit/pyroscope_ingest` | lib | `ureq` or `minreq` | HTTP POST of gzipped pprof to `{base_url}/ingest` with query parameters. |
| `kit/pysignalprof` | lib | `kindasafe_init`, `kindasafe`, `python_offsets`, `python_offsets_types`, `python_unwind`, `sig_ring`, `sighandler`, `notlibc`, `bbqueue`, `libc`, `pprof_enc`, `pyroscope_ingest` | Core profiler library. Contains all profiler logic: signal handler callback, reader thread, init sequence, symbolization, state management. Exposes `pub fn start(...)` for Rust consumers. |
| `kit/pysignalprof_capi` | cdylib | `pysignalprof` | Thin C API wrapper. Exposes `extern "C" pyroscope_start(...)` for `dlopen`/ctypes. Parses C strings, delegates to `pysignalprof::start()`. The `.so` that gets `dlopen`'d. |

### Dependency Policy

- New crates **must not** depend on the existing `pyroscope` crate, `py-spy`, `rbspy`, or any existing workspace member except `kindasafe` and `kindasafe_init`.
- External dependencies must be minimal:
  - `spin` — `#![no_std]` spinlock (in `notlibc`, `kindasafe_init`).
  - `bbqueue` — `#![no_std]` lockless SPSC BipBuffer queue (in `sig_ring`). Battle-tested in embedded/interrupt contexts, provides contiguous variable-length write grants without allocation.
  - `libc` — **only for init-time crates** (`kindasafe_init`, `sighandler`, `python_offsets`) that call `sigaction`/`setitimer`/file I/O. Never in signal-handler-path crates.
  - `prost` — protobuf encoding (in `pprof_enc` only).
  - `flate2` — gzip compression (in `pprof_enc` only).
  - `ureq` or `minreq` — HTTP client (in `pyroscope_ingest` only).
- **Signal-handler-path crates** (`kindasafe`, `notlibc`, `sig_ring`, `python_unwind`) **must be `#![no_std]` and must NOT depend on `libc`**. They use raw `syscall` instructions via inline assembly or naked asm for any OS interaction (e.g., `mmap`, `gettid`, memory reads). This ensures no libc function can ever be called from within the signal handler, regardless of interposition. `bbqueue` is permitted in the signal-handler path because it is `#![no_std]` and lockless — it uses only core atomics, no libc.

---

## 4. OS APIs and Syscalls

### 4.1 Signal Registration — `sigaction(2)`

**Crate:** `kit/sighandler`

```
sigaction(SIGPROF, &new_action, &old_action)

new_action:
  sa_sigaction = our_handler    (3-arg handler: sig, siginfo_t*, ucontext_t*)
  sa_flags     = SA_SIGINFO | SA_RESTART
  sa_mask      = {SIGPROF, SIGSEGV, SIGBUS}
```

- `SA_SIGINFO` — we need the 3-argument handler form to receive `ucontext_t*`.
- `SA_RESTART` — interrupted syscalls restart automatically so the profiler doesn't break the profiled application.
- `sa_mask = {SIGPROF, SIGSEGV, SIGBUS}` — signals blocked during handler execution:
  - `SIGPROF` — prevents re-entrant handler invocation on the same thread. If a signal is delivered while the handler is running, it would corrupt the per-shard frame buffer.
  - `SIGSEGV`, `SIGBUS` — the profiler signal handler must NOT be delivered while the kernel's SIGSEGV/SIGBUS handler is executing. `kindasafe_init` installs its own SIGSEGV/SIGBUS handlers for memory read recovery; if SIGPROF fires during that recovery, the profiler handler would run in a corrupted signal context. By masking SIGSEGV/SIGBUS, we ensure our handler never runs while a fault handler is active on the same thread.
- We do NOT use `SA_ONSTACK` initially — Python threads have sufficiently large stacks (default 8MB). Our handler uses minimal stack space (a few hundred bytes for local variables, pointers, and the MutexGuard) because the frame buffer lives in the locked shard, not on the signal handler's stack.

### 4.2 Timer Setup — `setitimer(2)`

**Crate:** `kit/sighandler`

```
setitimer(ITIMER_PROF, &interval, NULL)

interval:
  it_value    = { 0, 10000 }   // 10ms = 10000 µs
  it_interval = { 0, 10000 }   // repeating
```

- `ITIMER_PROF` counts CPU time (user + system) consumed by the **process**. The kernel delivers SIGPROF to whichever thread was executing when the timer expired.
- 10ms interval = 100 Hz sampling rate.
- The timer runs for the lifetime of the process — there is no stop.

### 4.3 Future: Per-Thread Timers — `timer_create(2)`

The design isolates timer management so that `setitimer` can be replaced with per-thread timers later. The `sighandler` crate exposes a simple `start_timer` function rather than a trait — traits add complexity without benefit when only one implementation exists. When per-thread timers are needed, refactor at that time.

Per-thread timers require:
- `timer_create(CLOCK_THREAD_CPUTIME_ID)` with `SIGEV_THREAD_ID` + `SIGEV_SIGNAL = SIGPROF`.
- Thread enumeration via `/proc/self/task/` at startup.
- Periodic poll or hook to discover new threads.
- Randomized initial delay (`random_in(0..10ms)`) to avoid synchronization artifacts (pattern from Go runtime).
- A timer registry mapping TID → timer_id.

### 4.4 Memory Allocation — Raw `mmap` Syscall

**Crate:** `kit/notlibc`

All memory used by signal-handler data structures is allocated via **raw `syscall` instruction**, NOT via libc's `mmap` wrapper (which can be interposed by jemalloc, tcmalloc, ASan, etc.):

```
// Raw syscall instruction via inline assembly — no libc involved
// Equivalent to: syscall(SYS_mmap, NULL, size, PROT_READ | PROT_WRITE,
//                        MAP_PRIVATE | MAP_ANONYMOUS, -1, 0)
```

These are wrapped in `notlibc::safe_mmap(size) -> *mut u8` and `notlibc::safe_munmap(addr, size)`, which use inline assembly to invoke the `mmap`/`munmap` syscalls directly without any libc dependency.

The signal handler itself **never calls mmap** — all memory is pre-allocated at profiler start.

### 4.5 Process Memory Introspection

| Operation | API | Crate | Context |
|-----------|-----|-------|---------|
| Read memory safely | `kindasafe::u64()`, `kindasafe::slice()` | `kindasafe` | Signal handler + init |
| Parse `/proc/self/maps` | `std::fs::read_to_string` | `python_offsets` | Init only |
| Read ELF headers/symbols | `kindasafe::slice()` on mapped regions | `python_offsets` | Init only |
| Read `_Py_DebugOffsets` | `kindasafe::slice()` | `python_offsets` | Init only |

### 4.6 Thread Identity

In the signal handler, we identify the current thread via `gettid()` (raw `syscall` instruction via inline assembly — not the libc `gettid()` wrapper). This gives the Linux thread ID, used for:
- Shard selection: `shard_index = tid % NUM_SHARDS`
- Thread identification in sample records

### 4.7 Syscall Summary

| Syscall | Where Called | Signal-Safe | Purpose |
|---------|-------------|-------------|---------|
| `sigaction` | Init | N/A | Register signal handler |
| `setitimer` | Init | N/A | Start process-wide timer |
| `SYS_mmap` | Init (pre-alloc) | Yes (raw) | Allocate bbqueue buffers, shard state |
| `SYS_eventfd2` | Init | N/A | Create eventfd for reader notification |
| `SYS_write` | Signal handler (every N samples) | Yes (raw) | Write 1 to eventfd to wake reader |
| `SYS_gettid` | Signal handler | Yes | Thread identification + shard selection |
| `read` | Init only | N/A | Read /proc/self/maps |
| `open` | Init only | N/A | Open /proc/self/maps |
| `write` | Reader thread | N/A | HTTP POST (not in handler) |

---

## 5. Initialization and Discovery

### 5.1 Overview

Before the signal handler can unwind Python stacks, we must discover:
1. Where `_PyRuntime` is in memory.
2. The Python version.
3. Struct field offsets (from `_Py_DebugOffsets` + hardcoded fallbacks).
4. How to find the current thread's `PyThreadState` (TLS offset).

All discovery happens at profiler initialization time (not in the signal handler) and can use `std`, allocate freely, etc.

### 5.2 Finding Python in Memory

**Crate:** `kit/python_offsets`

Parse `/proc/self/maps` to find memory regions mapped from the Python binary or `libpython`:

```
Pattern matching on pathname:
  - "libpython3" in the filename → prefer this (library has dynamic symbols)
  - "python3" in the filename → fallback (static binary)
  - Look for the first executable mapping (r-xp) of this file
```

Record the base address and path. The base address is needed to compute ASLR-adjusted symbol addresses.

### 5.3 ELF Symbol Resolution

**Crate:** `kit/python_offsets`

From the mapped Python binary, resolve these symbols:

| Symbol | Purpose |
|--------|---------|
| `_PyRuntime` | Runtime state — `_Py_DebugOffsets` is at offset 0 |
| `Py_Version` | Version integer — `(major << 24) | (minor << 16) | (micro << 8) | release` |

Procedure:
1. Open the binary file at the path found in `/proc/self/maps` and mmap it read-only (via `memmap2`).
2. Parse the ELF using the `object` crate: `object::File::parse(&mmap)`.
3. Call `file.dynamic_symbols()` to iterate the `.dynsym` table.
4. Match symbol names `"_PyRuntime"` and `"Py_Version"`.
5. Compute absolute addresses: `symbol.address() + load_bias`
   where `load_bias = mapped_base - file.relative_address_base()`.
   For PIE/shared objects the first LOAD vaddr is 0, so `load_bias = mapped_base`.

Returns `InitError::SymbolNotFound` (error code 3) if either symbol is absent.

### 5.4 Version Detection

**Crate:** `kit/python_offsets`

```
version_hex = kindasafe::u64(py_version_addr) & 0xFFFFFFFF
major = (version_hex >> 24) & 0xFF
minor = (version_hex >> 16) & 0xFF
```

Verify: `major == 3`, `minor == 14`. Return error for unsupported versions.

### 5.5 Reading `_Py_DebugOffsets`

**Crate:** `kit/python_offsets`

`_Py_DebugOffsets` is located at the very beginning of `_PyRuntime`. It provides offsets for navigating CPython's internal structures without hardcoding them.

#### Cookie and Version Validation

```
offset 0:  cookie[8]         — must equal "xdebugpy" (0x7970677562656478 LE)
offset 8:  version (u64)     — must match Py_Version
offset 16: free_threaded(u64) — must be 0 (we don't support free-threaded yet)
```

#### Offsets We Read From `_Py_DebugOffsets`

**Runtime state** (offsets within `_PyRuntime`):

| Field | Purpose |
|-------|---------|
| `runtime_state.interpreters_head` | Offset to `interpreters.head` — first `PyInterpreterState*` |

**Interpreter state** (offsets within `PyInterpreterState`):

| Field | Purpose |
|-------|---------|
| `interpreter_state.threads_head` | Offset to `threads.head` — first `PyThreadState*` |

**Thread state** (offsets within `PyThreadState`):

| Field | Purpose |
|-------|---------|
| `thread_state.current_frame` | Active `_PyInterpreterFrame*` |
| `thread_state.native_thread_id` | OS thread ID for matching |
| `thread_state.next` | Next thread in linked list |
| `thread_state.thread_id` | Python thread ID |

**Interpreter frame** (offsets within `_PyInterpreterFrame`):

| Field | Purpose |
|-------|---------|
| `interpreter_frame.previous` | Caller frame |
| `interpreter_frame.executable` | The `PyCodeObject*` |
| `interpreter_frame.instr_ptr` | Current bytecode instruction pointer (`_Py_CODEUNIT*`) |
| `interpreter_frame.owner` | Frame owner enum (u8) |

**Code object** (offsets within `PyCodeObject`):

| Field | Purpose |
|-------|---------|
| `code_object.qualname` | `co_qualname` — qualified function name (for symbolication) |
| `code_object.name` | `co_name` — function name (fallback) |
| `code_object.filename` | `co_filename` — source file path (for symbolication) |
| `code_object.firstlineno` | `co_firstlineno` — first line number |
| `code_object.co_code_adaptive` | Offset to bytecode array start (for instruction offset) |

**Unicode object** (for symbolication):

| Field | Purpose |
|-------|---------|
| `unicode_object.asciiobject_size` | Size of `PyASCIIObject` — data follows immediately after |

#### Offset Table Structure

```
PythonOffsets {
    // Runtime navigation
    py_runtime_addr: u64,                // Absolute address of _PyRuntime
    runtime_interpreters_head: u64,      // _PyRuntime + this → interp*
    interp_threads_head: u64,            // interp + this → tstate*

    // Thread state navigation
    tstate_current_frame: u64,
    tstate_native_thread_id: u64,
    tstate_next: u64,
    tstate_thread_id: u64,

    // Frame navigation
    frame_previous: u64,
    frame_executable: u64,               // → PyCodeObject*
    frame_instr_ptr: u64,                // → _Py_CODEUNIT*
    frame_owner: u64,                    // → u8 enum

    // Code object (for symbolication — NOT used in handler)
    code_qualname: u64,
    code_name: u64,
    code_filename: u64,
    code_firstlineno: u64,
    code_co_code_adaptive: u64,          // → start of bytecode array

    // Unicode (for symbolication)
    unicode_asciiobject_size: u64,       // data starts at this offset from object

    // _PyThreadState_GetCurrent function pointer
    get_tstate: fn() -> u64,             // resolved at init, called in signal handler
}
```

This struct is populated once at init time and then shared (read-only) with the signal handler via a global atomic pointer.

### 5.6 Resolving `_PyThreadState_GetCurrent`

The signal handler needs O(1) access to the current thread's `PyThreadState`. We call `_PyThreadState_GetCurrent` directly.

At init time, resolve `_PyThreadState_GetCurrent` from the ELF `.dynsym` table (same lookup used for `_PyRuntime`, `Py_Version`, `PyCode_Type`). Apply the ASLR load bias (`mapped_base - elf_base`) to get the runtime address, then transmute to `fn() -> u64` and store in handler state.

The signal handler calls this function pointer directly to get the current thread's `PyThreadState`:

```
tstate = (get_tstate)()
if tstate == 0 { return }
```

This works regardless of TLS model — Local Exec (`fs:`-relative), Initial Exec, or General Dynamic (`__tls_get_addr`). No disassembly, no FS segment reads, no architecture-specific TLS hacking.

### 5.7 Init Sequence Summary

```
pyroscope_start(config):
  1. kindasafe_init::init()                   — install SIGSEGV/SIGBUS recovery
  2. python_offsets::discover_python()       — parse /proc/self/maps
  3. python_offsets::read_elf_symbols()      — find _PyRuntime, Py_Version
  4. python_offsets::check_version()         — verify Python 3.14
  5. python_offsets::read_debug_offsets()    — read _Py_DebugOffsets from _PyRuntime
  6. transmute symbols.get_tstate_addr        — resolve _PyThreadState_GetCurrent as fn() -> u64
  7. Construct PythonOffsets struct
  8. Pre-allocate bbqueue buffers (16 shards × 256 KiB via safe_mmap), split into Producer/Consumer pairs + create eventfd
  9. Pre-allocate per-shard frame buffers, assign Producers to shards and Consumers to reader state
  10. Publish PythonOffsets + shard state to global state (atomic pointer store with Release)
  11. Spawn reader thread
  12. sighandler::install_handler(SIGPROF)   — register signal handler
  13. sighandler::start_timer(10ms)          — arm setitimer
```

**Important**: The signal handler is installed AFTER all data structures are allocated and published. The timer is started AFTER the handler is installed. This ordering ensures the handler never runs against uninitialized state.

---

## 6. Signal Handler

### 6.1 Handler Signature

**Crate:** `kit/sighandler` (generic registration) + `kit/pysignalprof` (Python-specific callback)

```
extern "C" fn signal_handler(
    sig: c_int,
    info: *mut siginfo_t,
    ucontext: *mut c_void,
)
```

### 6.2 Handler Flow

```
signal_handler(sig, info, ucontext):
  │
  ├─ 1. Load global profiler state (atomic Acquire load)
  │     If NULL → return
  │
  ├─ 3. Compute shard index: shard = gettid() % NUM_SHARDS
  │
  ├─ 4. Try-lock shard: spin::Mutex::try_lock(&shards[shard])
  │     On fail → try (shard+1) % N, then (shard+2) % N
  │     If all 3 fail → increment drop counter, return
  │
  ├─ 5. Get PyThreadState:
  │     tstate = (get_tstate)()    // calls _PyThreadState_GetCurrent
  │     If tstate == 0 → return
  │
  ├─ 6. Unwind Python stack:
  │     python_unwind::unwind(tstate, &offsets, &mut shard.frame_buffer)
  │     → walks _PyInterpreterFrame chain
  │     → fills frame_buffer with RawFrame structs
  │     → stops at max depth (128) or NULL/CSTACK frame
  │
  ├─ 7. Append stack to per-shard bbqueue:
  │     record_len = (12 + depth * 16 + 7) & !7
  │     grant = shard.bbqueue_producer.grant_exact(record_len)
  │     → if grant is None (queue full): increment overflow counter, skip
  │     → write record (header + frames) into grant slice
  │     → grant.commit(record_len)
  │
  ├─ 8. Increment samples_collected counter
  │     If samples_collected % N == 0:
  │       notify reader via eventfd (raw write(eventfd, &1u64, 8))
  │
  └─ 9. Unlock shard (MutexGuard drop)
         return
```

### 6.3 Async-Signal-Safety Guarantees

Every operation in the handler is async-signal-safe. **No libc functions are called — the entire handler path is `#![no_std]`.**

| Operation | How it's safe |
|-----------|---------------|
| Atomic load of global state | `AtomicPtr::load(Acquire)` — lock-free, no libc |
| `gettid()` | Raw `syscall` instruction via inline asm — no libc |
| `spin::Mutex::try_lock()` | Single `compare_exchange` — no libc, never blocks |
| `kindasafe::u64()` | Naked assembly with SIGSEGV recovery — no libc |
| bbqueue `grant_exact()` + `commit()` | Lock-free CAS on pre-allocated memory — `#![no_std]`, no libc |
| eventfd notify | Raw `write` syscall via inline asm (8 bytes to fd) — no libc |
| Atomic counter increment | `fetch_add(Relaxed)` — no libc |
| `spin::MutexGuard::drop()` | `store(Release)` — no libc |
**What the handler does NOT do:**
- No **libc function calls at all** — not `memcpy`, not `__errno_location`, not `gettid()` via libc, nothing. Every operation is either a Rust core/atomic intrinsic, inline assembly, or a raw `syscall` instruction.
- No `malloc` / `free` / `Box` / `Vec` / any Rust allocating type
- No `pthread_mutex_lock` or any blocking lock
- No `printf` / `write` / logging
- No `dlsym` / `dlopen`
- No reading `/proc` filesystem
- No CPython API calls
- No string reads or symbol resolution

**Why no libc at all?** Libc functions — even "simple" ones like `memcpy` or `errno` access — can be interposed by sanitizers (ASan, TSan), malloc replacements (jemalloc, tcmalloc), or LD_PRELOAD wrappers. Any interposed function might allocate, take a lock, or otherwise break async-signal-safety. By depending on zero libc functions in the handler path, we are immune to all such interposition.

### 6.4 Shard Design

We use **16 shards** (proven by async-profiler at scale):

```
SignalHandlerState:
  shards: [spin::Mutex<Shard>; 16]
  eventfd: i32                       // file descriptor for reader notification
  samples_since_notify: AtomicU32    // global counter for batch notification

Shard:
  frame_buffer: [RawFrame; 128]      // scratch buffer for unwinding
  bbqueue_producer: bbqueue::Producer // write half of per-shard bbqueue
  overflow_count: AtomicU64          // samples dropped due to full queue

ReaderState:
  bbqueue_consumers: [bbqueue::Consumer; 16]  // read halves (one per shard)
```

- Shard index: `gettid() % 16`
- 3 attempts on contention: `shard`, `(shard+1) % 16`, `(shard+2) % 16`
- With 16 shards and try-lock-only in the handler, the probability of dropping a sample is negligible even with many threads
- Each shard's `frame_buffer` is used as scratch space during unwinding (not on the signal handler's stack — the shard is pre-allocated via mmap)
- Each shard has its own `bbqueue::Producer` — true SPSC since the shard lock ensures single-producer. The corresponding `bbqueue::Consumer` lives in the reader thread.
- The `spin` crate's `Mutex` provides both `try_lock()` (used in handler — never blocks, async-signal-safe) and `lock()` (used by reader thread during drain — spins until acquired, ensures exclusive access to shard data)
- **Why we still need the shard lock with bbqueue**: bbqueue is SPSC — it assumes a *single* producer. Since `SIGPROF` can fire on any thread, multiple threads could try to call `grant_exact()` on the same shard concurrently. The `spin::Mutex::try_lock()` serializes access, preserving the SPSC invariant.

**Why `spin::Mutex` and not a custom lock**: The `spin` crate is well-tested, `#![no_std]`, and provides exactly the API we need — `try_lock()` for the signal handler and `lock()` for the reader thread. No need to reimplement a spinlock.

---

## 7. Python Stack Unwinding

### 7.1 Overview

**Crate:** `kit/python_unwind`

The unwinder walks the Python interpreter frame chain to collect raw `(code_object_ptr, instruction_offset)` tuples. It does NOT read function names, filenames, or line numbers — those are resolved later by the reader thread.

### 7.2 Frame Chain Structure (CPython 3.14)

```
PyThreadState
  └── current_frame → _PyInterpreterFrame
                        ├── executable → PyCodeObject*
                        ├── instr_ptr → _Py_CODEUNIT* (current instruction)
                        ├── owner → u8 (frame ownership enum)
                        └── previous → _PyInterpreterFrame (caller)
                                        └── ... → NULL at bottom
```

### 7.3 Raw Frame Representation

```
#[repr(C)]
#[derive(Copy, Clone)]
struct RawFrame {
    code_object: u64,    // PyCodeObject* address
    instr_offset: u64,   // byte offset of instr_ptr from co_code_adaptive start
}
```

We store the instruction offset for future line number resolution (not implemented in v1, but the data is captured).

### 7.4 Unwind Algorithm

```
fn unwind(
    tstate: u64,
    offsets: &PythonOffsets,
    buf: &mut [RawFrame; 128],
) -> usize:

  frame_ptr = kindasafe::u64(tstate + offsets.tstate_current_frame)?
  if frame_ptr == 0: return 0

  depth = 0
  prev_frame = 0  // cycle detection

  while frame_ptr != 0 && frame_ptr != prev_frame && depth < 128:
    // Read frame owner to classify the frame
    owner = kindasafe::u64(frame_ptr + offsets.frame_owner)? & 0xFF

    if owner == FRAME_OWNED_BY_CSTACK:  // value 3
      // C→Python entry shim — skip this frame, continue to previous
      prev_frame = frame_ptr
      frame_ptr = kindasafe::u64(frame_ptr + offsets.frame_previous)?
      continue

    // Read code object pointer
    code_obj = kindasafe::u64(frame_ptr + offsets.frame_executable)?
    if code_obj == 0:
      break  // invalid frame — stop

    // Read instruction pointer for future line number resolution
    instr_ptr = kindasafe::u64(frame_ptr + offsets.frame_instr_ptr)?

    buf[depth] = RawFrame {
      code_object: code_obj,
      instr_offset: instr_ptr,  // store raw pointer; symbolizer computes offset
    }
    depth += 1

    // Move to previous frame
    prev_frame = frame_ptr
    frame_ptr = kindasafe::u64(frame_ptr + offsets.frame_previous)?

  return depth
```

### 7.5 Frame Owner Values (CPython 3.14)

```
FRAME_OWNED_BY_THREAD       = 0   // Normal Python frame — INCLUDE
FRAME_OWNED_BY_GENERATOR    = 1   // Generator/coroutine — INCLUDE
FRAME_OWNED_BY_FRAME_OBJECT = 2   // Has visible PyFrameObject — INCLUDE
FRAME_OWNED_BY_CSTACK       = 3   // C→Python entry shim — SKIP
```

**Critical**: We skip ONLY `FRAME_OWNED_BY_CSTACK`. Generator frames (1) and frame-object-backed frames (2) represent valid Python function calls and must be included. Proposals 3 and 4 got this wrong by stopping at any non-zero owner value.

### 7.6 Safety Considerations

- Every memory read uses `kindasafe::u64()`, recovering gracefully from invalid pointers.
- If any read fails, the unwind stops and returns whatever frames were collected so far.
- Max depth of 128 frames prevents infinite loops from corrupted pointers.
- Cycle detection: if `frame_ptr == prev_frame`, break (circular list).
- The frame buffer is pre-allocated (in the shard), not on the signal handler's stack.

### 7.7 Instruction Offset Note

In CPython 3.14, `instr_ptr` is a `_Py_CODEUNIT*`, not a byte offset. The actual byte offset from `co_code_adaptive` is:
```
byte_offset = instr_ptr - co_code_adaptive_addr
```

We store the raw `instr_ptr` in the handler and compute the actual offset during symbolication (which can read `co_code_adaptive` at that time). This avoids an extra `kindasafe::u64()` read per frame in the handler.

---

## 8. Async-Signal-Safe Primitives

**Crate:** `kit/notlibc`

### 8.1 Shard Locking via `spin::Mutex`

We use the `spin` crate's `Mutex<T>` for shard locking. It provides two lock methods:

- **`try_lock() -> Option<MutexGuard>`** — single CAS, returns immediately. Used by the signal handler. Async-signal-safe (no syscalls, no blocking).
- **`lock() -> MutexGuard`** — spins until acquired. Used by the reader thread during dump to guarantee exclusive access to shard data (ensures no handler is mid-unwind into the frame buffer).

```
// Signal handler: never block
if let Some(guard) = shards[shard_idx].try_lock() {
    // unwind + record
} else {
    // contention — try next shard
}

// Reader thread during dump: must wait for any in-flight handler to finish
let guard = shards[shard_idx].lock();
// ensure no handler is mid-unwind, then snapshot counts
```

Properties:
- `#![no_std]` — no OS dependencies.
- `try_lock()` is async-signal-safe — single CAS.
- `lock()` spins with `core::hint::spin_loop()` — used only outside signal context.
- Guard-based RAII unlock — cannot forget to unlock.
- Well-tested, widely used crate — no need to reimplement.

### 8.2 Eventfd Wrapper

```
fn eventfd_create() -> Result<i32, i32>:
  // Inline assembly: syscall(SYS_eventfd2, 0, EFD_NONBLOCK | EFD_SEMAPHORE)
  // Returns file descriptor

fn eventfd_notify(fd: i32):
  // Inline assembly: syscall(SYS_write, fd, &1u64, 8)
  // Writes 1 to the eventfd counter — wakes the reader
  // Non-blocking, async-signal-safe (raw write syscall to a kernel fd)
```

The `eventfd` is created at init time (not in the handler). The handler only calls `eventfd_notify()` which is a single raw `write` syscall — async-signal-safe on Linux.

### 8.3 Raw Mmap Wrappers

```
fn safe_mmap(size: usize) -> Result<*mut u8, i32>:
  // Inline assembly: syscall instruction with SYS_mmap number
  // No libc dependency — direct kernel call
  // MAP_PRIVATE | MAP_ANONYMOUS, PROT_READ | PROT_WRITE

fn safe_munmap(addr: *mut u8, size: usize) -> Result<(), i32>:
  // Inline assembly: syscall instruction with SYS_munmap number
```

### 8.4 Raw Syscall Helpers

```
fn raw_gettid() -> u32:
  // Inline assembly: syscall instruction with SYS_gettid number
  // Returns Linux thread ID without calling libc

```

All syscall helpers use `core::arch::asm!` — no libc dependency.

---

## 9. Collection: Per-Shard SPSC Queue (`kit/sig_ring`)

A per-shard SPSC queue built on [`bbqueue`](https://github.com/jamesmunns/bbqueue), a `#![no_std]` lockless BipBuffer crate. The signal handler writes variable-length stack trace records via contiguous write grants; the reader thread drains them in batches via read grants. `kit/sig_ring` owns the record format and eventfd notification; bbqueue handles the underlying buffer management, atomics, and wrap-around.

### 9.1 Why bbqueue

The original design specified a hand-rolled SPSC ring buffer with manual atomic positions, wrap-around copy logic, and cache-line padding. bbqueue replaces all of this with a well-tested library:

- **`#![no_std]`, no libc** — safe for signal-handler-path crates.
- **Lockless BipBuffer** — `grant_exact(N)` returns a contiguous slice of N bytes, even near the buffer boundary (the BipBuffer design avoids split writes by using a watermark). No manual two-part copy needed.
- **Battle-tested** — widely used in embedded Rust for DMA + interrupt handler contexts, which have the same constraints as our signal handler (no allocation, no blocking, single producer).
- **Inline storage** — bbqueue supports const-generic inline backing (`BBQueue<N>`), so each shard's buffer can be a fixed-size array allocated via mmap at init time. No heap allocation.

**What we delete** by using bbqueue: custom `write_pos`/`read_pos` atomics, cache-line padding, `write_record_at`/`read_record_at` with two-part boundary copy, capacity/mask arithmetic. ~100 lines of subtle lock-free code replaced by library calls.

**What we keep**: the record format (header + frames), the shard lock (`spin::Mutex`), the eventfd notification, and the overflow counter.

### 9.2 Structure

```
// At init time, per shard:
bbqueue: BBQueue<262144>           // 256 KiB inline BipBuffer
  → producer: bbqueue::Producer    // given to signal handler (inside Shard, behind spin::Mutex)
  → consumer: bbqueue::Consumer    // given to reader thread (in ReaderState)

// Per shard (inside spin::Mutex<Shard>):
Shard:
  frame_buffer: [RawFrame; 128]    // scratch buffer for unwinding
  bbqueue_producer: Producer       // write half
  overflow_count: AtomicU64        // samples dropped due to full queue
```

The `Producer` and `Consumer` are the two halves of a bbqueue, obtained by splitting the `BBQueue` at init time. The `Producer` lives inside the shard (protected by `spin::Mutex`). The `Consumer` lives in the reader thread — it is safe to call `consumer.read()` without the shard lock because bbqueue's SPSC contract is upheld by the shard lock on the producer side.

### 9.3 Record Format

Each sample is a variable-length record written into a bbqueue grant:

```
┌───────────┬─────────┬──────────────────────────────────┐
│ thread_id │ depth   │ frames[0..depth]                 │
│ (u32)     │ (u32)   │ (code_object:u64, instr_ptr:u64) │
└───────────┴─────────┴──────────────────────────────────┘

record_len = (8 + depth * 16 + 7) & !7   (padded to 8-byte alignment)
```

Note: unlike the previous hand-rolled design, there is no `total_len` field in the record header. bbqueue's read grant already provides the exact byte length of the committed data, so the record length is implicit.

Variable-length records are space-efficient: a typical 20-frame stack uses `8 + 20*16 = 328 bytes` (padded to 328), not the 4KB fixed entries of Proposal 3.

### 9.4 Write Path (Signal Handler)

```
fn write(producer: &mut Producer, tid: u32, frames: &[RawFrame], depth: u32,
         overflow: &AtomicU64) -> bool:
  record_len = (8 + depth * 16 + 7) & !7  // 8-byte aligned

  match producer.grant_exact(record_len):
    Ok(mut grant):
      // bbqueue guarantees grant is a contiguous &mut [u8] slice
      // Write header
      grant[0..4].copy_from_slice(&tid.to_ne_bytes())
      grant[4..8].copy_from_slice(&depth.to_ne_bytes())
      // Write frames
      for i in 0..depth:
        let offset = 8 + i * 16
        grant[offset..offset+8].copy_from_slice(&frames[i].code_object.to_ne_bytes())
        grant[offset+8..offset+16].copy_from_slice(&frames[i].instr_offset.to_ne_bytes())
      // Commit — makes data visible to consumer
      grant.commit(record_len)
      return true

    Err(_):
      // Queue full — drop sample
      overflow.fetch_add(1, Relaxed)
      return false
```

**Key differences from hand-rolled version:**
- `grant_exact()` handles space checking and wrap-around internally. No manual `write_pos`/`read_pos` arithmetic.
- The grant is a contiguous `&mut [u8]` — no two-part copy even when the write spans the buffer boundary (BipBuffer watermark handles this).
- `commit()` publishes the data atomically to the consumer.

### 9.5 Read Path (Reader Thread)

```
fn drain(consumer: &mut Consumer, out: &mut Vec<RawSample>) -> usize:
  count = 0

  while let Ok(grant) = consumer.read():
    let buf = &*grant
    // Parse header
    let tid = u32::from_ne_bytes(buf[0..4])
    let depth = u32::from_ne_bytes(buf[4..8])
    // Parse frames
    let mut frames = Vec::with_capacity(depth as usize)
    for i in 0..depth as usize:
      let offset = 8 + i * 16
      let code_object = u64::from_ne_bytes(buf[offset..offset+8])
      let instr_offset = u64::from_ne_bytes(buf[offset+8..offset+16])
      frames.push(RawFrame { code_object, instr_offset })

    out.push(RawSample { tid, frames, depth })
    let len = grant.len()
    grant.release(len)  // free space for producer
    count += 1

  return count
```

**Key differences from hand-rolled version:**
- `consumer.read()` returns the next available contiguous record as a read grant, or `Err` if empty. No manual position tracking.
- `grant.release()` advances the consumer position atomically.
- The reader does NOT need the shard lock to call `consumer.read()` — the consumer half is exclusively owned by the reader thread. However, the reader still takes the shard lock during drain to ensure no signal handler is mid-unwind into the frame buffer (same as before).

### 9.6 Notification Mechanism

The signal handler notifies the reader thread via an `eventfd` every **N samples** (e.g., N = 32). This is separate from bbqueue — bbqueue has no built-in notification. The notification layer is identical to the original design:

```
// In signal handler, after successful grant.commit():
total = global_sample_counter.fetch_add(1, Relaxed)
if total % NOTIFY_INTERVAL == 0:
  eventfd_notify(state.eventfd)  // raw write(fd, &1u64, 8) — async-signal-safe
```

The notification is best-effort: if the write fails (fd full, etc.), it's harmless — the reader will still wake on the 15s timer. The `eventfd` is created with `EFD_NONBLOCK` so the handler never blocks.

### 9.7 Sizing

- 16 shards × 1 bbqueue per shard.
- Each bbqueue: **256 KiB** = 262144 bytes (inline const-generic storage).
- At 100 Hz with 20-frame stacks: each record ≈ 328 bytes.
- Per shard: `256 KiB / 328 ≈ 799` samples ≈ 8.0 seconds of data.
- Total across 16 shards: **4 MiB**, ~12784 samples.
- With reader draining on notification (every ~320ms at 100Hz/32), the buffers rarely fill up.
- Overflow is tracked by per-shard `overflow_count`.
- **BipBuffer overhead**: the BipBuffer watermark mechanism may leave some space unusable near the buffer end when a write doesn't fit contiguously. In the worst case this wastes up to one max-record-size of space (~2 KiB for a 128-frame stack) per wrap-around cycle — negligible relative to 256 KiB.

### 9.8 Properties

- **True SPSC per shard**: one writer (signal handler holding shard lock), one reader (reader thread). bbqueue's SPSC invariant is upheld by the shard lock.
- **Lock-free write path**: bbqueue uses CAS internally for the BipBuffer watermark, but with true SPSC this never contends.
- **Contiguous write grants**: BipBuffer guarantees the grant is a single contiguous `&mut [u8]` — no wrap-around copy logic needed.
- **Variable-length records**: space-efficient for varying stack depths.
- **No allocation in handler**: bbqueue buffer is pre-allocated at init (inline const-generic storage).
- **No hand-rolled atomics**: all buffer management (positions, wrap-around, space checking) is handled by bbqueue's well-tested implementation.

---

## 10. Reader Thread and Periodic Flush

### 10.1 Overview

**Crate:** `kit/profiler_core`

A background thread that:
- Wakes on **eventfd notification** (every N samples) to drain bbqueue consumers and aggregate stacks.
- Wakes on **15-second timeout** to flush: symbolize aggregated stacks, build pprof, send to Pyroscope.

This two-trigger design ensures low-latency batch processing (bbqueue buffers don't fill up) while still doing expensive symbolization/HTTP only every 15 seconds.

### 10.2 Thread Loop

```
fn reader_thread(state: Arc<ProfilerState>):
  let mut aggregated: HashMap<Vec<RawFrame>, u64> = HashMap::new()
  let mut last_flush = Instant::now()

  loop:
    // Wait for either: eventfd notification OR 15s timeout
    timeout = Duration::from_secs(15) - last_flush.elapsed()
    poll_result = poll([eventfd], timeout)

    // Drain all bbqueue consumers regardless of wake reason
    drain_all_shards(&state, &mut aggregated)

    if poll_result == TIMEOUT || last_flush.elapsed() >= 15s:
      // 15s elapsed — flush to Pyroscope
      flush_and_send(&state, &mut aggregated)
      last_flush = Instant::now()

fn drain_all_shards(state: &ProfilerState, aggregated: &mut HashMap<Vec<RawFrame>, u64>):
  for shard_idx in 0..16:
    // Lock shard to ensure no handler is mid-unwind into the frame buffer.
    // The bbqueue consumer.read() itself is safe without the lock (SPSC consumer),
    // but we need to ensure no handler is mid-write to the producer.
    let guard = shards[shard_idx].lock()  // wait for in-flight handler
    let mut raw_samples = Vec::new()
    sig_ring::drain(&mut state.bbqueue_consumers[shard_idx], &mut raw_samples)
    drop(guard)  // shard unlocked immediately after drain
    for sample in raw_samples:
      *aggregated.entry(sample.frames).or_insert(0) += 1

fn flush_and_send(state: &ProfilerState, aggregated: &mut HashMap<Vec<RawFrame>, u64>):
  if aggregated.is_empty():
    return

  // 1. Symbolize
  symbolized = symbolize(aggregated, &state.offsets, &mut state.symbol_cache)

  // 2. Build pprof
  pprof_bytes = pprof_enc::build(&symbolized, 100 /* sample_rate_hz */)

  // 3. Compute time range
  now = SystemTime::now()
  from = now - Duration::from_secs(15)

  // 4. Send to Pyroscope
  if let Err(e) = pyroscope_ingest::send(
    &state.config.server_url,
    &state.config.app_name,
    &pprof_bytes,
    from, now,
  ) {
    // Log error, continue — don't crash
  }

  // 5. Clear aggregation for next cycle
  aggregated.clear()
```

### 10.3 Drain Behavior

The reader drains one shard at a time, taking a **full `spin::Mutex::lock()`** on each shard. This ensures no signal handler is mid-unwind or mid-write (calling `grant_exact` / `commit` on the producer). The lock is held only for the duration of the drain (reading all available records from the bbqueue consumer), then immediately released — the shard is blocked for microseconds at most.

```
for shard_idx in 0..16:
  let guard = shards[shard_idx].lock()  // wait for in-flight handler
  sig_ring::drain(&mut bbqueue_consumers[shard_idx], &mut raw_samples)
  drop(guard)  // shard unlocked, handler can resume
```

Since only one shard is locked at a time, at most 1/16 of concurrent signals are affected during drain.

### 10.4 Two-Phase Design: Drain vs Flush

| Phase | Trigger | What happens | Cost |
|-------|---------|-------------|------|
| **Drain** | eventfd (every N samples) | Read records from bbqueue consumers, aggregate into `HashMap<stack, count>` | Cheap — no symbolization, no I/O |
| **Flush** | 15s timeout | Symbolize aggregated stacks, build pprof, HTTP POST to Pyroscope | Expensive — string reads, protobuf encoding, network I/O |

This separation means the bbqueue buffers are drained frequently (keeping them from overflowing) while the expensive flush happens only once per 15-second window. The aggregation `HashMap` lives in the reader thread and is standard Rust — no signal-safety concerns.

---

## 11. Symbolication

### 11.1 Overview

Performed by the reader thread in `kit/profiler_core`. Converts raw `(PyCodeObject*, instr_ptr)` tuples into human-readable function names.

### 11.2 Symbol Cache

```
SymbolCache:
  cache: HashMap<u64, SymbolInfo>    // PyCodeObject* → SymbolInfo

SymbolInfo:
  function_name: String,    // from co_qualname or co_name
  filename: String,         // from co_filename (for future use)
  first_line: i32,          // from co_firstlineno
```

### 11.3 Reading Code Object Fields

For each unique `PyCodeObject*` not in cache:

```
// Function name: co_qualname (preferred) or co_name (fallback)
qualname_ptr = kindasafe::u64(code_obj_ptr + offsets.code_qualname)?
function_name = read_python_ascii_string(qualname_ptr, offsets)?

// Filename
filename_ptr = kindasafe::u64(code_obj_ptr + offsets.code_filename)?
filename = read_python_ascii_string(filename_ptr, offsets)?

// First line number
firstlineno = kindasafe::u64(code_obj_ptr + offsets.code_firstlineno)? as i32
```

### 11.4 Reading Python Unicode Strings

Most Python code object names are ASCII:

```
fn read_python_ascii_string(obj_ptr: u64, offsets: &PythonOffsets) -> Option<String>:
  if obj_ptr == 0: return None
  // ASCII data starts immediately after PyASCIIObject header
  data_ptr = obj_ptr + offsets.unicode_asciiobject_size
  let mut buf = [0u8; 256]
  kindasafe::slice(&mut buf, data_ptr)?
  let len = buf.iter().position(|&b| b == 0).unwrap_or(buf.len())
  String::from_utf8_lossy(&buf[..len]).into_owned()
```

This runs in the reader thread (normal context), so `kindasafe` reads are safe. The SIGSEGV recovery handles stale code object pointers.

### 11.5 Cache Lifetime

For this initial implementation, the symbol cache persists for the profiler's lifetime. Code object addresses may be reused by CPython's allocator after a code object is freed, leading to stale cache entries. In practice this is rare for long-lived code (imports, class definitions) and acceptable for an initial implementation. Future improvement: validate cache entries by reading a secondary field.

---

## 12. Pprof Generation

**Crate:** `kit/pprof_enc`

### 12.1 Profile Structure

Following the [pprof format specification](https://github.com/google/pprof/blob/main/proto/profile.proto):

```
Profile:
  string_table: Vec<String>        // index 0 = "" (required by spec)
  sample_type: [ValueType]         // [{type: "cpu", unit: "nanoseconds"}]
  samples: Vec<Sample>
  locations: Vec<Location>
  functions: Vec<Function>

  period: i64                      // 10,000,000 ns (10ms)
  period_type: ValueType           // {type: "cpu", unit: "nanoseconds"}
  duration_nanos: i64              // 15,000,000,000 ns (15s)
  time_nanos: i64                  // profile start time (epoch ns)
```

### 12.2 Building Process

```
For each (symbolized_stack, count):
  sample = Sample {
    location_ids: [],
    values: [count * 10_000_000],   // count × period_ns = CPU nanoseconds
  }

  for frame in symbolized_stack:
    func = intern_function(frame.function_name, frame.filename, frame.first_line)
    loc = intern_location(func.id)
    sample.location_ids.push(loc.id)
```

### 12.3 String Table Deduplication

```
StringTable:
  strings: Vec<String>             // strings[0] = ""
  index: HashMap<String, i64>      // string → index

  fn intern(&mut self, s: &str) -> i64
```

### 12.4 Encoding

Use `prost` derive macros to define the pprof message structs inline (avoids .proto file management). Encode with `prost::Message::encode_to_vec()`, then gzip compress with `flate2`.

---

## 13. Pyroscope Ingestion

**Crate:** `kit/pyroscope_ingest`

### 13.1 API Endpoint

```
POST {base_url}/ingest

Query parameters:
  name       = {app_name}.cpu
  from       = {start_timestamp_unix_seconds}
  until      = {end_timestamp_unix_seconds}
  format     = pprof
  spyName    = pyroscope-cpython-rs
  sampleRate = 100

Headers:
  Content-Type: application/octet-stream

Body: gzipped pprof protobuf bytes
```

We use the `/ingest` endpoint for simplicity (it accepts raw gzipped pprof).

### 13.2 Implementation

Use `ureq` (minimal synchronous HTTP client, no async runtime):

```
fn send(base_url: &str, app_name: &str, pprof_gz: &[u8], from: u64, until: u64) -> Result<()>:
  let url = format!(
    "{}/ingest?name={}.cpu&from={}&until={}&format=pprof&spyName=pyroscope-cpython-rs&sampleRate=100",
    base_url, app_name, from, until
  )
  ureq::post(&url)
    .set("Content-Type", "application/octet-stream")
    .timeout(Duration::from_secs(5))
    .send_bytes(pprof_gz)?
  Ok(())
```

### 13.3 Error Handling

- Ingestion errors are logged but do not stop the profiler.
- If the Pyroscope server is down, samples are lost (not queued).
- Timeout: 5 seconds.
- No retries in this implementation.

---

## 14. Shared Library Interface

### 14.1 Overview

**Crate:** `kit/pysignalprof_capi` (thin C API wrapper around `kit/pysignalprof`)

Produces a `.so` (cdylib) loadable via `dlopen`:

```python
import ctypes
lib = ctypes.CDLL("./libpysignalprof_capi.so")
lib.pyroscope_start(b"my-python-app", b"http://localhost:4040", 0, 1)
# ... application runs, profiling continues for process lifetime ...
```

### 14.2 Exported Functions

```
#[no_mangle]
pub unsafe extern "C" fn pyroscope_start(
    app_name: *const c_char,
    server_url: *const c_char,
) -> c_int
// Returns 0 on success, nonzero error code on failure.
// There is no stop function — the profiler runs for the lifetime of the process.
```

### 14.3 Profiler Lifecycle

```
UNINITIALIZED (0) → RUNNING (1)
```

- `pyroscope_start()` transitions 0 → 1. Once started, the profiler runs until process exit.
- Calling `pyroscope_start()` when already running returns error code 9.
- The signal handler checks state == RUNNING (via the global AtomicPtr being non-null) before proceeding.
- No stop/cleanup is needed — the OS reclaims all mmap'd memory and timers on process exit.

---

## 15. Concurrency Model

### 15.1 Participants

| Participant | Runs on | What it accesses |
|-------------|---------|-----------------|
| Signal handler | Interrupted thread (any) | Shard lock, frame buffer, bbqueue producer (write side), atomic counters |
| Reader thread | Dedicated background thread | bbqueue consumers (read side), symbol cache (HashMap), pprof builder, HTTP |
| Init | Main thread (Python caller) | Everything — but runs before handler is installed |

### 15.2 Lock Hierarchy

| Level | Mechanism | Context |
|-------|-----------|---------|
| Signal handler | `spin::Mutex::try_lock()` on per-shard state | Async-signal-safe |
| Reader thread (dump) | `spin::Mutex::lock()` on per-shard state | Spins until acquired |
| Signal handler | bbqueue `grant_exact()` + `commit()` (lock-free CAS) | Async-signal-safe |
| Reader thread (dump) | bbqueue `read()` + `release()` (lock-free) under shard lock | Normal (spins briefly) |
| Reader thread | `HashMap` for symbol cache (local to reader) | Normal |
| Init | Sequential — runs before handler is installed | Sequential |

### 15.3 No Deadlocks: Proof by Construction

1. **Signal handler** only uses `try_lock()` (never blocks) → cannot deadlock.
2. **Reader thread** uses `lock()` on shard mutexes, but this is the only lock it acquires. The signal handler on the same thread cannot interrupt and deadlock because `sa_mask = {SIGPROF, SIGSEGV, SIGBUS}` blocks SIGPROF during handler execution, and the reader thread is not a signal handler.
3. **Reader thread spin duration is bounded**: the signal handler holds the shard lock for ~1-10µs (one unwind + one bbqueue grant/commit). The reader thread's `lock()` spin completes quickly.
4. **Init** runs before the handler is installed → no concurrent signal handler access during initialization.
5. `sa_mask = {SIGPROF, SIGSEGV, SIGBUS}` prevents re-entrant handler execution and prevents delivery during fault recovery → the shard lock is never held by the same thread trying to re-acquire it via signal.

### 15.4 Global State Management

```
static PROFILER_STATE: AtomicPtr<ProfilerState> = AtomicPtr::new(null_mut())

// Init: publish state (after all allocation is complete)
let state = Box::into_raw(Box::new(state))
PROFILER_STATE.store(state, Release)

// Signal handler: read state
let state = PROFILER_STATE.load(Acquire)
if state.is_null() { return }

// No shutdown — state and memory persist for process lifetime.
// The OS reclaims everything on process exit.
```

---

## 16. Memory Management

### 16.1 Allocation Overview

| Data Structure | Size | Allocated By | When Freed |
|---------------|------|-------------|-----------|
| Shard state (16 shards × lock + frame buf + producer) | 16 × (4 + 128×16 + ~64) ≈ 34 KiB | `safe_mmap` at init | Process exit |
| bbqueue buffers (16 shards × 256 KiB inline storage) | 4 MiB | `safe_mmap` at init | Process exit |
| bbqueue control structures (16 × Producer + Consumer) | ~2 KiB | `safe_mmap` at init | Process exit |
| eventfd | 1 fd | `eventfd2` syscall at init | Process exit |
| PythonOffsets struct | ~200 B | `Box::new` at init | Process exit (leaked) |
| Symbol cache | Dynamic | Reader thread heap | Process exit |
| Pprof buffer | Dynamic | Reader thread heap | Dropped after each send |

### 16.2 Signal Handler: Zero Heap Allocation

The signal handler path allocates **zero bytes from the heap**:
- Frame buffer: pre-allocated per-shard (via mmap).
- bbqueue buffers: pre-allocated at init (inline const-generic storage, backed by mmap'd memory).
- bbqueue `grant_exact()` / `commit()`: operate on pre-allocated buffer via lock-free atomics — no allocation.
- All atomic operations: on pre-allocated memory.

### 16.3 mmap vs malloc Boundary

- **`safe_mmap`** (raw `syscall` instruction): all memory touched by the signal handler.
- **`malloc`** (Rust's standard allocator): everything in the reader thread and initialization.

This strict separation ensures that even if the signal interrupts the reader thread inside `malloc`, the signal handler never calls into the allocator — no deadlock possible.

### 16.4 No-libc Guarantee in Handler Path

The signal handler path uses **zero libc functions**. This is enforced structurally:
- All handler-path crates (`kindasafe`, `notlibc`, `sig_ring`, `python_unwind`) are `#![no_std]` and do not have `libc` in their dependency tree.
- `kindasafe` (the read crate) uses naked assembly — no libc. The init-time code (`kindasafe_init`) depends on libc but is never in the handler path.
- `spin` is `#![no_std]` — no libc.
- `bbqueue` is `#![no_std]` — uses only `core` atomics, no libc.
- OS interactions (`gettid`, `mmap`) use raw `syscall` instructions via `core::arch::asm!`.

---

## 17. Error Handling

### 17.1 Signal Handler Error Strategy

The signal handler must never panic, abort, or call `unwrap()`. All errors result in early return with a counter increment:

| Situation | Counter Incremented |
|-----------|-------------------|
| Global state is NULL | (none — just return) |
| All 3 shard locks contended | `samples_lock_fail` |
| PyThreadState is NULL | (none — just return) |
| Unwind produced 0 frames | `samples_empty` |
| bbqueue full (`grant_exact` fails) | `samples_overflow` |
| Successful collection | `samples_collected` |

All counters are `AtomicU64` with `Relaxed` ordering — no synchronization needed for metrics.

### 17.2 Reader Thread Error Strategy

The reader thread uses standard Rust error handling:
- **Symbolication failure**: use placeholder `"<unknown>"` for the function name.
- **Pprof encoding failure**: log error, skip this flush cycle.
- **HTTP ingestion failure**: log error, drop the data, continue to next cycle.

The reader thread never crashes the host process.

### 17.3 Init Error Codes

| Return Code | Meaning |
|------------|---------|
| 0 | Success |
| 1 | kindasafe_init init failed |
| 2 | Python binary not found in /proc/self/maps |
| 3 | _PyRuntime or Py_Version symbol not found |
| 4 | _Py_DebugOffsets cookie/version validation failed |
| 5 | Unsupported Python version |
| 6 | TLS offset discovery failed |
| 7 | Memory allocation (mmap) failed |
| 8 | Signal handler installation failed |
| 9 | Profiler already running |

---

## 18. Future Work

| Feature | Where it Fits |
|---------|---------------|
| Native (C/C++) frame unwinding | Add `kit/native_unwind` crate, interleave native and Python frames |
| Line number resolution | Decode `co_linetable` in reader thread using `instr_offset` from `RawFrame` |
| Per-thread `timer_create` | Add per-thread timer in `sighandler`, thread discovery via `/proc/self/task/` |
| Multiple Python versions | Add offset tables for 3.12, 3.13 in `python_offsets`; version dispatch at init |
| Free-threaded Python (3.13t+) | Handle `free_threaded == 1` in debug offsets, adjust TLS access |
| ARM64 support | Add arch modules in `kindasafe` and `python_offsets` (FS register differs) |
| Ruby profiler | Reuse `notlibc`, `sig_ring`, `sighandler`, `pprof_enc`, `pyroscope_ingest`; create `ruby_offsets` + `ruby_unwind` |
| .NET profiler | Same reuse pattern |
| Wall-clock profiling | Use `ITIMER_REAL` + `SIGALRM` or `timer_create(CLOCK_MONOTONIC)` |
| Labels/tags | Add label fields to sample records, propagate to pprof |
| Configuration API | More `pyroscope_start` parameters or environment variable configuration |
| Auto-start via LD_PRELOAD | Constructor function (`__attribute__((constructor))`) with env var config |

---

## Appendix: CPython 3.14 Structures

### A.1 `_Py_DebugOffsets` Layout

Located at `_PyRuntime + 0`. Begins with:

```
Offset 0:   cookie[8]          "xdebugpy" (0x7970677562656478 LE)
Offset 8:   version (u64)      PY_VERSION_HEX, e.g. 0x030E00F0 for 3.14.0 final
Offset 16:  free_threaded(u64) 0 for standard build, 1 for free-threaded
```

Followed by sub-structures, each containing a `size` field and then offset fields (all u64):

- `runtime_state { size, finalizing, interpreters_head }`
- `interpreter_state { size, id, next, threads_head, threads_main, gc, ... }`
- `thread_state { size, prev, next, interp, current_frame, native_thread_id, thread_id, ... }`
- `interpreter_frame { size, previous, executable, instr_ptr, localsplus, owner, ... }`
- `code_object { size, filename, name, qualname, linetable, firstlineno, argcount, ..., co_code_adaptive, ... }`
- `pyobject { size, ob_type }`
- `type_object { size, tp_name, tp_repr, tp_flags }`
- `tuple_object { size, ob_item, ob_size }`
- `unicode_object { size, state, length, asciiobject_size }`
- `gen_object { size, gi_name, gi_iframe, gi_frame_state }`

The recommended approach to read:
1. Validate cookie (first 8 bytes == "xdebugpy") and version.
2. Read the entire `_Py_DebugOffsets` as a sequence of u64 values (it's at a known address).
3. Parse according to the known 3.14 field order (field count per sub-struct is fixed per minor version).
4. Store parsed values in `PythonOffsets`.

### A.2 Frame Owner Constants

```
FRAME_OWNED_BY_THREAD       = 0   // Normal Python frame
FRAME_OWNED_BY_GENERATOR    = 1   // Generator/coroutine frame
FRAME_OWNED_BY_FRAME_OBJECT = 2   // Has a visible PyFrameObject
FRAME_OWNED_BY_CSTACK       = 3   // C→Python entry shim — SKIP THIS
```

### A.3 Thread State Navigation

```
_PyRuntime (global, found via ELF symbol)
  + runtime_state.interpreters_head → PyInterpreterState*
    + interpreter_state.threads_head → PyThreadState* (head)
      + native_thread_id → OS TID
      + current_frame → _PyInterpreterFrame*
        + executable → PyCodeObject*
        + instr_ptr → _Py_CODEUNIT*
        + owner → u8
        + previous → next frame (or NULL)
      + next → next PyThreadState* (or NULL)
```

### A.4 `_PyThreadState_GetCurrent` Resolution

`_PyThreadState_GetCurrent` is resolved from the ELF dynamic symbol table at init time (same as other CPython symbols). Its runtime address is computed as `elf_va + load_bias` and transmuted to a `fn() -> u64` function pointer. The signal handler calls it directly — this works with any TLS model (Local Exec, Initial Exec, General Dynamic).

### A.5 Memory Read Patterns in Signal Handler

All memory reads in the signal handler follow this pattern:
```
let value = match kindasafe::u64(addr) {
    Ok(v) => v,
    Err(_) => return,  // read failed — abort this sample gracefully
};
```

No read failure crashes the handler. Every pointer dereference is wrapped in `kindasafe`, which uses SIGSEGV recovery to handle invalid addresses.
```

## File: `kit/pysignalprof/src/lib.rs`
```rust
#![cfg(all(target_arch = "x86_64", target_os = "linux"))]

use core::cell::UnsafeCell;
use core::ffi::{c_int, c_void};
use core::sync::atomic::{AtomicBool, AtomicPtr, AtomicU32, Ordering};
use std::collections::HashMap;
use std::time::{Duration, Instant};

use bbqueue::framed::{FrameConsumer, FrameProducer};
use python_offsets_types::py314;
use python_unwind::RawFrame;
use sig_ring::RING_SIZE;

const STATE_UNINITIALIZED: u32 = 0;
const STATE_RUNNING: u32 = 1;

/// Default number of shards for concurrent signal handler access.
const DEFAULT_NUM_SHARDS: usize = 16;

static LIFECYCLE: AtomicU32 = AtomicU32::new(STATE_UNINITIALIZED);

/// Whether to log diagnostic messages to stderr. Off by default.
static LOG_ENABLED: AtomicBool = AtomicBool::new(false);

// ── Error codes ──────────────────────────────────────────────────────────────

/// Error codes returned by `start`.
#[repr(i32)]
#[derive(Copy, Clone, Debug)]
pub enum InitError {
    KindasafeInit = 1,
    PythonNotFound = 2,
    SymbolNotFound = 3,
    DebugOffsetsMismatch = 4,
    UnsupportedVersion = 5,
    AllocFailed = 7,
    SignalHandler = 8,
    AlreadyRunning = 9,
    KindasafeSanityCheck = 10,
}

// ── Logging ──────────────────────────────────────────────────────────────────

fn log_info(msg: &str) {
    if LOG_ENABLED.load(Ordering::Relaxed) {
        eprintln!("pysignalprof: {}", msg);
    }
}

fn log_error(msg: &str) {
    if LOG_ENABLED.load(Ordering::Relaxed) {
        eprintln!("pysignalprof ERROR: {}", msg);
    }
}

// ── Per-shard state ──────────────────────────────────────────────────────────

/// Per-shard mutable state protected by a spin::Mutex.
///
/// The signal handler `try_lock()`s a shard, unwinds into `frame_buffer`,
/// then writes the result into the bbqueue `producer`.
struct Shard {
    frame_buffer: [RawFrame; python_unwind::MAX_DEPTH],
    producer: FrameProducer<'static, RING_SIZE>,
}

// ── Handler state (shared between init + signal handler + reader) ────────────

/// Global profiler state accessed by the signal handler via `AtomicPtr`.
///
/// Allocated once at init time via `Box::into_raw`. Published to the handler
/// with `Release`; the handler loads with `Acquire`. Never deallocated.
struct HandlerState {
    debug_offsets: py314::_Py_DebugOffsets,
    /// Function pointer to `_PyThreadState_GetCurrent()`, resolved at init time.
    get_tstate: fn() -> u64,
    /// Expected type-object addresses for runtime type checking.
    type_addrs: python_unwind::TypeAddrs,
    /// Asyncio module debug offsets (`None` if `_asyncio` was not loaded at init).
    /// Used by the reader thread for walking suspended async tasks (future work).
    #[allow(dead_code)]
    asyncio_offsets: Option<py314::Py_AsyncioModuleDebugOffsets>,
    /// Dynamically-sized shard array (length = num_shards).
    shards: Vec<notlibc::ShardMutex<Shard>>,
    /// Per-shard bbqueue consumers. Only accessed by the reader thread.
    /// Wrapped in UnsafeCell for interior mutability; safety is guaranteed
    /// by the single-reader-thread invariant.
    consumers: Vec<UnsafeCell<FrameConsumer<'static, RING_SIZE>>>,
    eventfd: notlibc::EventFd,
    samples_since_notify: AtomicU32,
    num_shards: usize,
    notify_interval: u32,
    app_name: String,
    server_url: Option<String>,
    tags: Vec<(String, String)>,
}

// SAFETY: HandlerState is initialized once and then only accessed via:
// - signal handler: loads AtomicPtr(Acquire), takes shard try_lock,
//   reads debug_offsets/get_tstate (immutable), writes to producer.
// - reader thread: takes shard lock, reads consumers (separate from handler).
// All accesses are properly synchronized via AtomicPtr + spin::Mutex.
unsafe impl Sync for HandlerState {}

static HANDLER_STATE: AtomicPtr<HandlerState> = AtomicPtr::new(core::ptr::null_mut());

// ── Signal handler ───────────────────────────────────────────────────────────

extern "C" fn on_sigprof(_sig: c_int, _info: *mut libc::siginfo_t, _ctx: *mut c_void) {
    // Step 1: Load global profiler state.
    let state_ptr = HANDLER_STATE.load(Ordering::Acquire);
    if state_ptr.is_null() {
        return;
    }
    let state = unsafe { &*state_ptr };

    // Step 2: Get current thread state by calling _PyThreadState_GetCurrent.
    let tstate = (state.get_tstate)();
    if tstate == 0 {
        return;
    }

    notlibc::debug::writes("sigprof: tstate=0x");
    notlibc::debug::write_hex(tstate as usize);
    notlibc::debug::puts("");

    // Step 4: Select shard via gettid, try-lock with 3 fallback attempts.
    let tid = notlibc::gettid();
    let num_shards = state.num_shards;
    let base = tid as usize % num_shards;

    let mut guard = None;
    for attempt in 0..3 {
        let idx = (base + attempt) % num_shards;
        if let Some(g) = state.shards[idx].try_lock() {
            guard = Some(g);
            break;
        }
    }
    let mut guard = match guard {
        Some(g) => g,
        None => return, // all 3 shards contended — drop sample
    };

    // Step 5: Unwind Python stack into the shard's pre-allocated frame buffer.
    let depth = python_unwind::unwind(
        tstate,
        &state.debug_offsets,
        &state.type_addrs,
        &mut guard.frame_buffer,
    );
    if depth == 0 {
        notlibc::debug::writes("sigprof: unwind depth=0 tstate=0x");
        notlibc::debug::write_hex(tstate as usize);
        notlibc::debug::puts("");
        return;
    }

    // Step 6: Write stack trace record into the shard's bbqueue producer.
    // Split the borrow: take a shared ref to the frame_buffer data, then
    // pass the producer as &mut. This is safe because write() only reads
    // from frames[..depth] and only writes to the producer.
    let shard = &mut *guard;
    sig_ring::write(&mut shard.producer, tid, &shard.frame_buffer, depth);

    // Step 7: Notify reader thread periodically.
    let total = state.samples_since_notify.fetch_add(1, Ordering::Relaxed);
    if total % state.notify_interval == 0 {
        state.eventfd.notify();
    }
}

// ── Unicode string reading ───────────────────────────────────────────────────

/// Read a Python unicode string object into `buf` and return a UTF-8 `&str`.
///
/// Handles all CPython compact string representations:
/// - ASCII (ascii=1): data at `obj + asciiobject_size`, null-terminated
/// - Non-ASCII with cached UTF-8: reads from the `utf8` pointer field
/// - UCS1/Latin-1 (kind=1, ascii=0): 1 byte/char, encoded to UTF-8
/// - UCS2 (kind=2): 2 bytes/char (little-endian u16), encoded to UTF-8
/// - UCS4 (kind=4): 4 bytes/char (little-endian u32), encoded to UTF-8
fn read_pyunicode<'a>(
    buf: &'a mut [u8],
    obj_ptr: u64,
    unicode_offsets: &py314::_Py_DebugOffsets__unicode_object,
    free_threaded: bool,
) -> Option<&'a str> {
    if obj_ptr == 0 {
        return None;
    }

    // Read state (u32 at the state offset within the unicode object).
    let state_raw = kindasafe::u64(obj_ptr + unicode_offsets.state).ok()? as u32;

    // Extract ascii and kind bits. The layout differs between standard and
    // free-threaded builds:
    //   Standard:      [interned:2][kind:3][compact:1][ascii:1][statically_allocated:1][pad:24]
    //   Free-threaded: [interned:8][kind:3][compact:1][ascii:1][statically_allocated:1][pad:18]
    let (ascii, kind) = if free_threaded {
        (((state_raw >> 12) & 1) != 0, (state_raw >> 8) & 0x7)
    } else {
        (((state_raw >> 6) & 1) != 0, (state_raw >> 2) & 0x7)
    };

    // ASCII fast path: data is null-terminated UTF-8 right after PyASCIIObject.
    if ascii {
        return kindasafe::str(buf, obj_ptr + unicode_offsets.asciiobject_size)
            .ok()
            .filter(|s| !s.is_empty());
    }

    // Non-ASCII: try the cached utf8 pointer in PyCompactUnicodeObject.
    // Layout: PyASCIIObject | utf8_length (8 bytes) | utf8 (8 bytes) | data...
    let utf8_ptr_addr = obj_ptr + unicode_offsets.asciiobject_size + 8;
    let utf8_ptr = kindasafe::u64(utf8_ptr_addr).unwrap_or(0);
    if utf8_ptr != 0 {
        // Read the cached UTF-8 representation directly.
        return kindasafe::str(buf, utf8_ptr).ok().filter(|s| !s.is_empty());
    }

    // No cached UTF-8: read raw UCS data and convert.
    let length = kindasafe::u64(obj_ptr + unicode_offsets.length).ok()? as usize;
    if length == 0 {
        return None;
    }

    // Data for compact non-ASCII strings starts after PyCompactUnicodeObject,
    // which is PyASCIIObject + 16 bytes (utf8_length + utf8 pointer).
    let data_addr = obj_ptr + unicode_offsets.asciiobject_size + 16;

    match kind {
        1 => read_ucs1_to_utf8(buf, data_addr, length),
        2 => read_ucs2_to_utf8(buf, data_addr, length),
        4 => read_ucs4_to_utf8(buf, data_addr, length),
        _ => None,
    }
}

/// Read UCS1 (Latin-1) data and encode to UTF-8.
fn read_ucs1_to_utf8(buf: &mut [u8], data_addr: u64, length: usize) -> Option<&str> {
    let max_read = length.min(128);
    let mut raw = [0u8; 128];
    kindasafe::slice(&mut raw[..max_read], data_addr).ok()?;

    let mut out = 0;
    for &byte in &raw[..max_read] {
        if let Some(c) = char::from_u32(byte as u32) {
            let len = c.len_utf8();
            if out + len > buf.len() {
                break;
            }
            c.encode_utf8(&mut buf[out..]);
            out += len;
        }
    }
    if out == 0 {
        return None;
    }
    core::str::from_utf8(&buf[..out]).ok()
}

/// Read UCS2 data (little-endian u16) and encode to UTF-8.
fn read_ucs2_to_utf8(buf: &mut [u8], data_addr: u64, length: usize) -> Option<&str> {
    let max_read = length.min(128);
    let byte_len = max_read * 2;
    let mut raw = [0u8; 256];
    kindasafe::slice(&mut raw[..byte_len], data_addr).ok()?;

    let mut out = 0;
    for i in 0..max_read {
        let cp = u16::from_le_bytes([raw[i * 2], raw[i * 2 + 1]]) as u32;
        if let Some(c) = char::from_u32(cp) {
            let len = c.len_utf8();
            if out + len > buf.len() {
                break;
            }
            c.encode_utf8(&mut buf[out..]);
            out += len;
        }
    }
    if out == 0 {
        return None;
    }
    core::str::from_utf8(&buf[..out]).ok()
}

/// Read UCS4 data (little-endian u32) and encode to UTF-8.
fn read_ucs4_to_utf8(buf: &mut [u8], data_addr: u64, length: usize) -> Option<&str> {
    let max_read = length.min(64);
    let byte_len = max_read * 4;
    let mut raw = [0u8; 256];
    kindasafe::slice(&mut raw[..byte_len], data_addr).ok()?;

    let mut out = 0;
    for i in 0..max_read {
        let cp = u32::from_le_bytes([raw[i * 4], raw[i * 4 + 1], raw[i * 4 + 2], raw[i * 4 + 3]]);
        if let Some(c) = char::from_u32(cp) {
            let len = c.len_utf8();
            if out + len > buf.len() {
                break;
            }
            c.encode_utf8(&mut buf[out..]);
            out += len;
        }
    }
    if out == 0 {
        return None;
    }
    core::str::from_utf8(&buf[..out]).ok()
}

// ── Symbolization helper ─────────────────────────────────────────────────────

/// Resolve the function name for a code object via `co_qualname` (with
/// `co_name` fallback). Returns an owned `String`, or `"<unknown>"` if
/// resolution fails.
fn resolve_function_name(code_object: u64, offsets: &py314::_Py_DebugOffsets) -> String {
    let mut name_buf = [0u8; 256];
    let free_threaded = offsets.free_threaded != 0;

    // Try co_qualname first.
    if let Ok(qualname_ptr) = kindasafe::u64(code_object + offsets.code_object.qualname)
        && let Some(name) = read_pyunicode(
            &mut name_buf,
            qualname_ptr,
            &offsets.unicode_object,
            free_threaded,
        )
    {
        return name.to_owned();
    }

    // Fallback to co_name.
    if let Ok(name_ptr) = kindasafe::u64(code_object + offsets.code_object.name)
        && let Some(name) = read_pyunicode(
            &mut name_buf,
            name_ptr,
            &offsets.unicode_object,
            free_threaded,
        )
    {
        return name.to_owned();
    }

    "<unknown>".to_owned()
}

// ── Reader thread ────────────────────────────────────────────────────────────

/// Reader thread entry point. Wakes on eventfd or timeout, drains all shard
/// consumers, symbolizes and feeds samples directly into the ProfileBuilder.
/// Every 15 seconds the builder is encoded to pprof and optionally sent to
/// Pyroscope, then reset for the next window.
fn reader_thread(state: &'static HandlerState) {
    let mut event_set = match notlibc::EventSet::new() {
        Ok(es) => es,
        Err(_) => {
            log_error("reader: failed to create EventSet");
            return;
        }
    };
    if event_set.add(&state.eventfd).is_err() {
        log_error("reader: failed to add eventfd to EventSet");
        return;
    }

    log_info(&format!(
        "reader thread started, {} shards",
        state.num_shards
    ));

    let flush_interval = Duration::from_secs(15);
    let period: i64 = 10_000_000; // 10 ms
    let mut last_flush = Instant::now();
    let mut builder = pprof_enc::ProfileBuilder::new(0, flush_interval.as_nanos() as i64, period);
    // Cache: code_object address → resolved function name.
    let mut symbol_cache: HashMap<u64, String> = HashMap::new();

    loop {
        // Phase 1: Wait with dynamic timeout so flush happens on time.
        let remaining = flush_interval.saturating_sub(last_flush.elapsed());
        let timeout_ms = remaining.as_millis() as i32;
        let _ = event_set.wait(timeout_ms);

        // Phase 2: Drain all shards, symbolize, feed into builder.
        let offsets = &state.debug_offsets;
        let log = LOG_ENABLED.load(Ordering::Relaxed);

        for shard_idx in 0..state.num_shards {
            let _shard_guard = state.shards[shard_idx].lock();
            let consumer = unsafe { &mut *state.consumers[shard_idx].get() };

            while let Some(grant) = consumer.read() {
                if let Some(record) = sig_ring::parse_record(&grant) {
                    let depth = record.depth as usize;

                    // Ensure all code objects are in the cache (mutable pass).
                    for i in 0..depth {
                        let raw = record.frame(i);
                        symbol_cache
                            .entry(raw.code_object)
                            .or_insert_with(|| resolve_function_name(raw.code_object, offsets));
                    }

                    // Build frames from cached names (immutable pass).
                    let frames: Vec<pprof_enc::Frame<'_>> = (0..depth)
                        .map(|i| {
                            let raw = record.frame(i);
                            pprof_enc::Frame {
                                function_name: symbol_cache[&raw.code_object].as_str(),
                                filename: "",
                                first_line: 0,
                            }
                        })
                        .collect();

                    if log {
                        let names: Vec<&str> = frames.iter().map(|f| f.function_name).collect();
                        eprintln!(
                            "pysignalprof: reader: tid=0x{:x} depth={} [{}]",
                            record.tid,
                            depth,
                            names.join(" < "),
                        );
                    }

                    builder.add_sample(&frames, 1);
                }
                grant.release();
            }
        }

        // Phase 3: Flush when 15 seconds have elapsed.
        if last_flush.elapsed() >= flush_interval {
            flush_pprof(state, &mut builder);
            symbol_cache.clear();
            last_flush = Instant::now();
        }
    }
}

/// Encode the accumulated profile, optionally send it, then reset the builder.
fn flush_pprof(state: &'static HandlerState, builder: &mut pprof_enc::ProfileBuilder) {
    if builder.is_empty() {
        log_info("flush: no samples, skipping");
        return;
    }

    let num_stacks = builder.len();
    let pprof = builder.encode();
    log_info(&format!(
        "flush: {} unique stacks, pprof {} bytes",
        num_stacks,
        pprof.len(),
    ));

    if let Some(ref url) = state.server_url {
        let now_secs = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap_or_default()
            .as_secs();
        let from_secs = now_secs.saturating_sub(15);
        let tag_refs: Vec<(&str, &str)> = state
            .tags
            .iter()
            .map(|(k, v)| (k.as_str(), v.as_str()))
            .collect();
        if let Err(e) =
            pyroscope_ingest::send(url, &state.app_name, &tag_refs, &pprof, from_secs, now_secs)
        {
            log_error(&format!("ingest send failed: {}", e));
        }
    }

    let now_nanos = std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)
        .unwrap_or_default()
        .as_nanos() as i64;
    builder.reset(now_nanos, 15_000_000_000);
}

// ── Public API ───────────────────────────────────────────────────────────────

/// Start the CPython profiler.
///
/// Runs the full init sequence: kindasafe crash recovery, Python binary
/// discovery, ELF symbol resolution, version detection, debug offsets,
/// TLS offset discovery, ring buffer allocation, reader thread spawn,
/// then installs a SIGPROF handler + 10 ms timer.
///
/// Parameters:
/// - `app_name`: application name (empty string if not specified).
/// - `server_url`: server URL (`None` to skip ingestion).
/// - `num_shards`: number of shards (0 = use default 16).
/// - `log_enabled`: if true, print diagnostic messages to stderr.
/// - `tags`: static key-value labels to attach to ingested profiles.
///
/// Returns `Ok(())` on success, `Err(InitError)` on failure.
pub fn start(
    app_name: String,
    server_url: Option<String>,
    num_shards: usize,
    log_enabled: bool,
    tags: Vec<(String, String)>,
) -> Result<(), InitError> {
    if LIFECYCLE
        .compare_exchange(
            STATE_UNINITIALIZED,
            STATE_RUNNING,
            Ordering::AcqRel,
            Ordering::Acquire,
        )
        .is_err()
    {
        return Err(InitError::AlreadyRunning);
    }

    if log_enabled {
        LOG_ENABLED.store(true, Ordering::Release);
    }

    let num_shards = if num_shards == 0 {
        DEFAULT_NUM_SHARDS
    } else {
        num_shards
    };

    log_info(&format!(
        "configured num_shards={}, ring_size={}KiB",
        num_shards,
        RING_SIZE / 1024,
    ));

    match init_sequence(num_shards, app_name, server_url, tags) {
        Ok(()) => Ok(()),
        Err(code) => {
            log_error(&format!("init failed with code {}", code as c_int));
            LIFECYCLE.store(STATE_UNINITIALIZED, Ordering::Release);
            Err(code)
        }
    }
}

fn init_sequence(
    num_shards: usize,
    app_name: String,
    server_url: Option<String>,
    tags: Vec<(String, String)>,
) -> Result<(), InitError> {
    let notify_interval = sig_ring::DEFAULT_NOTIFY_INTERVAL;

    log_info(&format!(
        "starting init: num_shards={}, ring_size={}KiB, notify_interval={}",
        num_shards,
        RING_SIZE / 1024,
        notify_interval,
    ));

    // Step 1: Install kindasafe SIGSEGV/SIGBUS recovery.
    kindasafe_init::init().map_err(|_| {
        log_error("kindasafe_init failed");
        InitError::KindasafeInit
    })?;
    log_info("kindasafe_init ok");

    // Step 2: Find Python binary in /proc/self/maps.
    let binary = python_offsets::find_python_in_maps().map_err(|e| {
        log_error(&format!("find_python_in_maps: {:?}", e));
        map_init_error(&e)
    })?;
    log_info("found Python binary");

    // Step 3: Resolve _PyRuntime and Py_Version ELF symbols.
    let symbols = python_offsets::resolve_elf_symbols(&binary).map_err(|e| {
        log_error(&format!("resolve_elf_symbols: {:?}", e));
        map_init_error(&e)
    })?;
    log_info("resolved ELF symbols");

    // Step 4: Detect and validate Python version.
    let version = python_offsets::detect_version(symbols.py_version_addr).map_err(|e| {
        log_error(&format!("detect_version: {:?}", e));
        map_init_error(&e)
    })?;
    log_info(&format!("detected Python version: {:?}", version));

    // Read raw version hex (needed by read_debug_offsets).
    let version_hex = python_offsets::read_version_hex(symbols.py_version_addr).map_err(|e| {
        log_error(&format!("read_version_hex: {:?}", e));
        map_init_error(&e)
    })?;

    // Step 5: Read _Py_DebugOffsets from _PyRuntime.
    let debug_offsets =
        python_offsets::read_debug_offsets(symbols.py_runtime_addr, &version, version_hex)
            .map_err(|e| {
                log_error(&format!("read_debug_offsets: {:?}", e));
                map_init_error(&e)
            })?;
    log_info("read debug offsets");

    // Step 5b: Try to read asyncio module debug offsets (non-fatal).
    let asyncio_offsets = match python_offsets::find_asyncio_in_maps() {
        Ok(asyncio_binary) => match python_offsets::resolve_asyncio_debug_symbol(&asyncio_binary) {
            Ok(addr) => match python_offsets::read_asyncio_debug_offsets(addr) {
                Ok(offsets) => {
                    log_info("read asyncio debug offsets");
                    Some(offsets)
                }
                Err(e) => {
                    log_info(&format!("asyncio debug offsets read failed: {:?}", e));
                    None
                }
            },
            Err(e) => {
                log_info(&format!("asyncio debug symbol not found: {:?}", e));
                None
            }
        },
        Err(_) => {
            log_info("_asyncio module not loaded yet");
            None
        }
    };

    // Step 6: Resolve _PyThreadState_GetCurrent as a callable function pointer.
    let get_tstate: fn() -> u64 = unsafe { core::mem::transmute(symbols.get_tstate_addr as usize) };
    log_info(&format!(
        "_PyThreadState_GetCurrent at 0x{:x}",
        symbols.get_tstate_addr
    ));

    // Step 7: Allocate bbqueue buffers and split into producer/consumer pairs.
    let mut producers: Vec<Option<FrameProducer<'static, RING_SIZE>>> =
        (0..num_shards).map(|_| None).collect();
    let mut consumers: Vec<Option<FrameConsumer<'static, RING_SIZE>>> =
        (0..num_shards).map(|_| None).collect();

    for i in 0..num_shards {
        let bb = Box::new(bbqueue::BBBuffer::<RING_SIZE>::new());
        let bb: &'static bbqueue::BBBuffer<RING_SIZE> = Box::leak(bb);
        let (prod, cons) = bb.try_split_framed().map_err(|_| {
            log_error(&format!("bbqueue split failed for shard {}", i));
            InitError::AllocFailed
        })?;
        producers[i] = Some(prod);
        consumers[i] = Some(cons);
    }
    log_info(&format!("allocated {} ring buffers", num_shards));

    // Step 8: Create eventfd for reader thread notification.
    let eventfd = notlibc::EventFd::new().map_err(|_| {
        log_error("eventfd creation failed");
        InitError::AllocFailed
    })?;

    // Step 9: Build shard and consumer vecs.
    let empty_frame = RawFrame {
        code_object: 0,
        instr_offset: 0,
    };
    let shards: Vec<notlibc::ShardMutex<Shard>> = (0..num_shards)
        .map(|i| {
            notlibc::ShardMutex::new(Shard {
                frame_buffer: [empty_frame; python_unwind::MAX_DEPTH],
                producer: producers[i].take().unwrap(),
            })
        })
        .collect();

    let consumers: Vec<UnsafeCell<FrameConsumer<'static, RING_SIZE>>> = consumers
        .into_iter()
        .map(|c| UnsafeCell::new(c.unwrap()))
        .collect();

    // Step 10: Publish handler state.
    let type_addrs = python_unwind::TypeAddrs {
        code_type: symbols.py_code_type_addr,
    };
    let state = Box::new(HandlerState {
        debug_offsets,
        get_tstate,
        type_addrs,
        asyncio_offsets,
        shards,
        consumers,
        eventfd,
        samples_since_notify: AtomicU32::new(0),
        num_shards,
        notify_interval,
        app_name,
        server_url,
        tags,
    });
    let state: &'static HandlerState = unsafe { &*Box::into_raw(state) };
    HANDLER_STATE.store(
        state as *const HandlerState as *mut HandlerState,
        Ordering::Release,
    );

    // Step 11: Spawn reader thread.
    std::thread::Builder::new()
        .name("pyroscope-reader".into())
        .spawn(move || reader_thread(state))
        .map_err(|_| {
            log_error("failed to spawn reader thread");
            InitError::AllocFailed
        })?;

    // Step 12: Install SIGPROF handler (but don't start the timer yet).
    unsafe {
        sighandler::register_sigaction(on_sigprof).map_err(|_| {
            log_error("signal handler installation failed");
            InitError::SignalHandler
        })?;
    }

    // Step 12b: Verify kindasafe crash recovery works under the SIGPROF
    // handler's signal mask (sa_mask). This catches misconfigurations like
    // SIGSEGV/SIGBUS being blocked during SIGPROF.
    kindasafe_init::sanity_check().map_err(|_| {
        log_error("kindasafe sanity check failed — crash recovery is not working");
        InitError::KindasafeSanityCheck
    })?;
    log_info("kindasafe sanity check passed");

    // Step 13: Start 10 ms ITIMER_PROF timer.
    unsafe {
        sighandler::start_timer().map_err(|_| {
            log_error("setitimer failed");
            InitError::SignalHandler
        })?;
    }

    log_info("init complete");
    notlibc::debug::puts("pysignalprof: init complete");
    Ok(())
}

/// Map `python_offsets::InitError` variants to our `InitError` enum.
fn map_init_error(err: &python_offsets::InitError) -> InitError {
    match err {
        python_offsets::InitError::KindasafeInitFailed => InitError::KindasafeInit,
        python_offsets::InitError::PythonNotFound => InitError::PythonNotFound,
        python_offsets::InitError::Io => InitError::PythonNotFound,
        python_offsets::InitError::SymbolNotFound(_) => InitError::SymbolNotFound,
        python_offsets::InitError::ElfParse => InitError::SymbolNotFound,
        python_offsets::InitError::DebugOffsetsMismatch => InitError::DebugOffsetsMismatch,
        python_offsets::InitError::UnsupportedVersion => InitError::UnsupportedVersion,
    }
}
```

## File: `kit/pysignalprof_capi/Cargo.toml`
```
[package]
name = "pysignalprof_capi"
version = "0.1.0"
edition = "2024"
publish = false

[lib]
crate-type = ["cdylib"]

[features]
default = []
debug-print = ["pysignalprof/debug-print"]

[dependencies]
pysignalprof = { path = "../pysignalprof" }
```

## File: `kit/pysignalprof_capi/src/lib.rs`
```rust
#![cfg(all(target_arch = "x86_64", target_os = "linux"))]

use core::ffi::{CStr, c_char, c_int};

/// Start the CPython profiler.
///
/// Parameters:
/// - `app_name`: application name (NUL-terminated C string, or null).
/// - `server_url`: server URL (NUL-terminated C string, or null).
/// - `num_shards`: number of shards (0 = use default 16). Must be >= 1.
/// - `log_enabled`: if nonzero, print diagnostic messages to stderr.
///
/// Returns 0 on success, nonzero error code on failure:
/// - 1: kindasafe init failed
/// - 2: Python binary not found
/// - 3: ELF symbol not found
/// - 4: debug offsets validation failed
/// - 5: unsupported Python version
/// - 7: memory allocation / resource creation failed
/// - 8: signal handler installation failed
/// - 9: profiler already running
/// - 10: kindasafe sanity check failed (crash recovery not working)
///
/// # Safety
///
/// `app_name` and `server_url` must be valid pointers to NUL-terminated
/// C strings, or null.
#[unsafe(no_mangle)]
pub unsafe extern "C" fn pyroscope_start(
    app_name: *const c_char,
    server_url: *const c_char,
    num_shards: c_int,
    log_enabled: c_int,
) -> c_int {
    let app_name = if app_name.is_null() {
        String::new()
    } else {
        unsafe { CStr::from_ptr(app_name) }
            .to_string_lossy()
            .into_owned()
    };

    let server_url = if server_url.is_null() {
        None
    } else {
        let s = unsafe { CStr::from_ptr(server_url) }
            .to_string_lossy()
            .into_owned();
        if s.is_empty() { None } else { Some(s) }
    };

    let num_shards = if num_shards <= 0 {
        0
    } else {
        num_shards as usize
    };

    match pysignalprof::start(
        app_name,
        server_url,
        num_shards,
        log_enabled != 0,
        Vec::new(),
    ) {
        Ok(()) => 0,
        Err(code) => code as c_int,
    }
}
```

## File: `kit/pysignalprof_capi/tests/test_cpython.py`
```python
#!/usr/bin/env python3
"""
Smoke test for pysignalprof_capi cdylib.

Loads the .so via ctypes, calls pyroscope_start() with logging enabled,
then burns CPU for 20 seconds so at least one 15-second pprof flush
is triggered. Uses nested function calls to produce multi-frame stacks.

Run with:
    cargo build -p pysignalprof_capi
    python3.14 kit/pysignalprof_capi/tests/test_cpython.py

Expected: pyroscope_start returns 0, flush log line appears at ~15s,
profile is sent to Pyroscope (if running on localhost:4040).
"""
import asyncio
import ctypes
import os
import sys
import time


def find_library():
    """Find the built .so in target/debug or target/release."""
    base = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(base, "..", "..", ".."))
    for profile in ("debug", "release"):
        path = os.path.join(repo_root, "target", profile, "libpysignalprof_capi.so")
        if os.path.exists(path):
            return path
    print(
        f"ERROR: libpysignalprof_capi.so not found under {repo_root}/target/",
        file=sys.stderr,
    )
    sys.exit(1)


def inner_work():
    """Inner function to produce deeper stacks."""
    total = 0
    for i in range(100_000):
        total += i
    return total


def outer_work():
    """Outer function that calls inner_work."""
    return inner_work()


def burn_cpu(seconds):
    """Burn CPU time to trigger ITIMER_PROF / SIGPROF signals."""
    end = time.monotonic() + seconds
    total = 0
    while time.monotonic() < end:
        total += outer_work()
    return total


# Function with Unicode characters in name: U+00E9 (é), U+00E0 (à), U+00FC (ü).
# These are Latin-1 range (>0x7F), so CPython stores the name as a non-ASCII
# compact string (kind=1, ascii=0). This exercises the non-ASCII reading path.
def burn_cpu_éàü(seconds):
    end = time.monotonic() + seconds
    total = 0
    while time.monotonic() < end:
        for i in range(100_000):
            total += i
    return total


# Function with CJK characters: U+4E16 (世), U+754C (界).
# These require UCS2 storage in CPython (kind=2).
def burn_cpu_世界(seconds):
    end = time.monotonic() + seconds
    total = 0
    while time.monotonic() < end:
        for i in range(100_000):
            total += i
    return total


# ── Async workload ───────────────────────────────────────────────────────────
# These exercise asyncio profiling. Running coroutines appear in SIGPROF
# samples (their frames are in the thread's frame chain). Suspended coroutines
# (e.g. awaiting asyncio.sleep) are NOT captured by SIGPROF — they require
# walking the cr_await chain from the asyncio task list.


async def async_cpu_work():
    """Burns CPU inside a coroutine — will appear in SIGPROF samples."""
    total = 0
    for i in range(500_000):
        total += i
    return total


async def async_inner():
    """Inner async function to create deeper async call stacks."""
    return await async_cpu_work()


async def async_outer():
    """Outer async function: async_outer > async_inner > async_cpu_work."""
    return await async_inner()


async def async_io_work():
    """Sleeps briefly — this is a suspended task, NOT visible in SIGPROF."""
    await asyncio.sleep(0.01)


async def async_mixed_workload():
    """Run a mix of CPU-bound and IO-bound async tasks concurrently."""
    tasks = []
    for _ in range(5):
        tasks.append(asyncio.create_task(async_outer()))
        tasks.append(asyncio.create_task(async_io_work()))
    await asyncio.gather(*tasks)


async def async_main():
    """Main async entry point — runs for ~5 seconds."""
    end = time.monotonic() + 5
    while time.monotonic() < end:
        await async_mixed_workload()


def main():
    lib_path = find_library()
    print(f"Loading: {lib_path}")
    lib = ctypes.CDLL(lib_path)

    lib.pyroscope_start.restype = ctypes.c_int
    lib.pyroscope_start.argtypes = [
        ctypes.c_char_p,  # app_name
        ctypes.c_char_p,  # server_url
        ctypes.c_int,     # num_shards (0 = default)
        ctypes.c_int,     # log_enabled
    ]

    # num_shards=0 (use default 16), log_enabled=1
    rc = lib.pyroscope_start(b"test-app", b"http://localhost:4040", 0, 1)
    print(f"pyroscope_start returned: {rc}")
    if rc != 0:
        print(f"ERROR: pyroscope_start failed with code {rc}", file=sys.stderr)
        sys.exit(rc)

    # Calling again should return 9 (already running).
    rc2 = lib.pyroscope_start(b"test-app", b"http://localhost:4040", 0, 0)
    print(f"second pyroscope_start returned: {rc2}")
    assert rc2 == 9, f"Expected 9 (already running), got {rc2}"

    print("Burning CPU for 20 seconds (flush expected at ~15s)...")
    burn_cpu(20)
    print("done with ASCII burn")

    # Burn CPU with unicode-named functions to test non-ASCII string reading.
    # The profiler should resolve these names in the debug output.
    print("Burning CPU with Latin-1 function name (burn_cpu_éàü) for 3 seconds...")
    burn_cpu_éàü(3)
    print("done with Latin-1 burn")

    print("Burning CPU with CJK function name (burn_cpu_世界) for 3 seconds...")
    burn_cpu_世界(3)
    print("done with CJK burn")

    # Async workload: running coroutines show up in SIGPROF, suspended ones don't.
    print("Running asyncio workload for 5 seconds...")
    asyncio.run(async_main())
    print("done with asyncio workload")


if __name__ == "__main__":
    main()
```

## File: `kit/python_offsets/Cargo.toml`
```
[package]
name = "python_offsets"
version = "0.1.0"
edition = "2024"
publish = false

[dependencies]
kindasafe = { path = "../kindasafe" }
kindasafe_init = { path = "../kindasafe_init" }
python_offsets_types = { path = "../python_offsets_types" }
object = { version = "0.38", default-features = false, features = ["read", "elf"] }
memmap2 = "0.9"

[dev-dependencies]
libc = "=0.2.182"
anyhow = "=1.0.102"
```

## File: `kit/python_offsets/gen_debug_offsets.sh`
```bash
#!/usr/bin/env bash
# Generate Rust #[repr(C)] structs for CPython's _Py_DebugOffsets and
# Py_AsyncioModuleDebugOffsets using bindgen.
#
# Downloads the full CPython source, runs ./configure to generate pyconfig.h,
# then runs bindgen on the real headers. No manual extraction or sed parsing
# for the main debug offsets. The asyncio struct is extracted from
# Modules/_asynciomodule.c (where it is defined, not in a public header).
#
# Usage (run from kit/python_offsets/):
#   ./gen_debug_offsets.sh <cpython-git-ref> <module-name>
#
# Examples:
#   ./gen_debug_offsets.sh v3.14.0 py314
#   ./gen_debug_offsets.sh v3.13.0 py313
#
# Prerequisites: bindgen-cli (cargo install bindgen-cli), clang, curl

set -euo pipefail

if [ $# -ne 2 ]; then
    echo "Usage: $0 <cpython-git-ref> <module-name>" >&2
    exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
GIT_REF="$1"
MODULE="$2"
OUT="${SCRIPT_DIR}/../python_offsets_types/src/${MODULE}.rs"

tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT

# 1. Download CPython source
echo "Downloading CPython ${GIT_REF}..."
curl -sfL "https://github.com/python/cpython/archive/refs/tags/${GIT_REF}.tar.gz" \
    -o "$tmpdir/cpython.tar.gz" 2>/dev/null \
|| curl -sfL "https://github.com/python/cpython/archive/refs/heads/${GIT_REF}.tar.gz" \
    -o "$tmpdir/cpython.tar.gz"

mkdir -p "$tmpdir/cpython"
tar xzf "$tmpdir/cpython.tar.gz" --strip-components=1 -C "$tmpdir/cpython"

SRC="$tmpdir/cpython"

# 2. Run ./configure to generate pyconfig.h (no compilation, ~30s)
echo "Running ./configure..."
(cd "$SRC" && ./configure --disable-shared --without-ensurepip > /dev/null 2>&1)

# 3. Create a wrapper header that includes via Python.h (sets up all types)
#    then includes the internal header containing _Py_DebugOffsets.
INTERNAL_HEADER="internal/pycore_runtime.h"
if [ -f "$SRC/Include/internal/pycore_debug_offsets.h" ]; then
    INTERNAL_HEADER="internal/pycore_debug_offsets.h"
fi

cat > "$tmpdir/wrapper.h" <<EOF
#include "Python.h"
#include "${INTERNAL_HEADER}"
EOF

# 4. Run bindgen for _Py_DebugOffsets
echo "Running bindgen for _Py_DebugOffsets..."
bindgen "$tmpdir/wrapper.h" \
    --formatter=rustfmt \
    --allowlist-type '_Py_DebugOffsets' \
    --no-layout-tests \
    --no-doc-comments \
    --raw-line "// @generated by gen_debug_offsets.sh ${GIT_REF} ${MODULE}" \
    --raw-line "// DO NOT EDIT — re-run the generator instead." \
    --raw-line "// See kit/python_offsets/gen_debug_offsets.sh for details." \
    --raw-line "" \
    --raw-line "#![allow(non_camel_case_types)]" \
    --raw-line "" \
    --raw-line "//! CPython \`_Py_DebugOffsets\` layout for \`${GIT_REF}\`." \
    --raw-line "//!" \
    --raw-line "//! Auto-generated by \`gen_debug_offsets.sh ${GIT_REF} ${MODULE}\`." \
    --raw-line "//! Do not edit by hand." \
    -- -DPy_BUILD_CORE -I"$SRC" -I"$SRC/Include" -I"$SRC/Include/internal" \
    | sed 's/::std::os::raw::c_char/u8/g' \
    > "$OUT"

# 5. Extract Py_AsyncioModuleDebugOffsets from _asynciomodule.c (if present)
#    and run a second bindgen pass to append it to the same output file.
ASYNCIO_MODULE="$SRC/Modules/_asynciomodule.c"
if [ -f "$ASYNCIO_MODULE" ] && grep -q 'Py_AsyncioModuleDebugOffsets' "$ASYNCIO_MODULE"; then
    echo "Extracting Py_AsyncioModuleDebugOffsets from _asynciomodule.c..."

    # Extract the typedef block: from "typedef struct _Py_AsyncioModuleDebugOffsets {"
    # to the closing "} Py_AsyncioModuleDebugOffsets;"
    sed -n '/^typedef struct _Py_AsyncioModuleDebugOffsets/,/^} Py_AsyncioModuleDebugOffsets;/p' \
        "$ASYNCIO_MODULE" > "$tmpdir/asyncio_offsets.h"

    if [ -s "$tmpdir/asyncio_offsets.h" ]; then
        # Prepend stdint.h for uint64_t
        { echo '#include <stdint.h>'; cat "$tmpdir/asyncio_offsets.h"; } > "$tmpdir/asyncio_wrapper.h"

        echo "Running bindgen for Py_AsyncioModuleDebugOffsets..."
        bindgen "$tmpdir/asyncio_wrapper.h" \
            --formatter=rustfmt \
            --allowlist-type 'Py_AsyncioModuleDebugOffsets' \
            --no-layout-tests \
            --no-doc-comments \
            | sed 's/::std::os::raw::c_char/u8/g' \
            | grep -v '^/\* automatically generated' \
            >> "$OUT"

        echo "Appended Py_AsyncioModuleDebugOffsets to ${OUT}"
    else
        echo "Warning: could not extract Py_AsyncioModuleDebugOffsets typedef"
    fi
else
    echo "Note: Py_AsyncioModuleDebugOffsets not found in this CPython version (skipped)"
fi

echo "Generated ${OUT} from ${GIT_REF}"
```

## File: `kit/python_offsets/src/lib.rs`
```rust
pub use python_offsets_types::py314;

use core::mem::size_of;
use std::io::BufRead;

use object::{Object, ObjectSegment, ObjectSymbol};

/// Expected cookie at `_Py_DebugOffsets` offset 0: `b"xdebugpy"` as little-endian u64.
/// This is version-independent — all CPython builds that have `_Py_DebugOffsets` use it.
pub const COOKIE: u64 = 0x7970_6775_6265_6478;

#[derive(Debug, PartialEq)]
pub enum InitError {
    KindasafeInitFailed,
    PythonNotFound,
    /// A required ELF dynamic symbol was not found.
    /// The contained `&str` names which symbol is missing.
    /// Corresponds to init error code 3.
    SymbolNotFound(&'static str),
    DebugOffsetsMismatch,
    UnsupportedVersion,
    /// The ELF file could not be parsed.
    ElfParse,
    /// Failed to open or mmap the binary file.
    Io,
}

/// Parsed CPython version from `PY_VERSION_HEX`.
#[derive(Debug, PartialEq, Clone, Copy)]
pub struct PythonVersion {
    pub major: u8,
    pub minor: u8,
    pub micro: u8,
}

/// Parse a raw `PY_VERSION_HEX` value into [`PythonVersion`].
///
/// The hex layout is `(major << 24) | (minor << 16) | (micro << 8) | release_level`.
pub fn parse_version(version_hex: u64) -> PythonVersion {
    PythonVersion {
        major: ((version_hex >> 24) & 0xFF) as u8,
        minor: ((version_hex >> 16) & 0xFF) as u8,
        micro: ((version_hex >> 8) & 0xFF) as u8,
    }
}

/// Absolute runtime addresses of key CPython symbols, after applying ASLR load bias.
#[derive(Debug, PartialEq)]
pub struct ElfSymbols {
    pub py_runtime_addr: u64,
    pub py_version_addr: u64,
    /// Address of `PyCode_Type` (the type object for `PyCodeObject`).
    pub py_code_type_addr: u64,
    /// Runtime address of `_PyThreadState_GetCurrent()`.
    pub get_tstate_addr: u64,
}

/// Open and mmap `binary.path`, parse the ELF dynamic symbol table, find
/// `_PyRuntime` and `Py_Version`, apply the ASLR load bias, and return their
/// absolute runtime addresses.
///
/// Returns [`InitError::SymbolNotFound`] (error code 3) if any required symbol is absent.
pub fn resolve_elf_symbols(binary: &PythonBinary) -> Result<ElfSymbols, InitError> {
    let file = std::fs::File::open(&binary.path).map_err(|_| InitError::Io)?;
    // SAFETY: the file is a read-only view of an on-disk ELF; no other code
    // modifies it during parsing.
    let mmap = unsafe { memmap2::Mmap::map(&file) }.map_err(|_| InitError::Io)?;
    resolve_elf_symbols_from_bytes(&mmap, binary.base)
}

/// Parse ELF dynamic symbols from a byte slice and compute absolute addresses.
///
/// `mapped_base` is the address at which the first mapping of this binary
/// appears in `/proc/self/maps` (i.e. the runtime base after ASLR).
fn resolve_elf_symbols_from_bytes(data: &[u8], mapped_base: u64) -> Result<ElfSymbols, InitError> {
    let obj = object::File::parse(data).map_err(|_| InitError::ElfParse)?;

    // load_bias = runtime base − ELF-file base (first LOAD segment vaddr).
    // For PIE/shared objects the first LOAD vaddr is 0, so load_bias == mapped_base.
    // For non-PIE executables (ET_EXEC) the first LOAD vaddr is already the
    // absolute address (e.g. 0x400000), so load_bias == 0.
    // NOTE: object::Object::relative_address_base() always returns 0 for ELF,
    // so we must compute the first LOAD vaddr ourselves from program headers.
    let elf_base = obj.segments().map(|s| s.address()).min().unwrap_or(0);
    let load_bias = mapped_base.wrapping_sub(elf_base);

    let mut py_runtime: Option<u64> = None;
    let mut py_version: Option<u64> = None;
    let mut py_code_type: Option<u64> = None;
    let mut get_tstate: Option<u64> = None;

    for sym in obj.dynamic_symbols() {
        match sym.name() {
            Ok("_PyRuntime") => py_runtime = Some(sym.address().wrapping_add(load_bias)),
            Ok("Py_Version") => py_version = Some(sym.address().wrapping_add(load_bias)),
            Ok("PyCode_Type") => py_code_type = Some(sym.address().wrapping_add(load_bias)),
            Ok("_PyThreadState_GetCurrent") => {
                get_tstate = Some(sym.address().wrapping_add(load_bias))
            }
            _ => {}
        }
        if py_runtime.is_some()
            && py_version.is_some()
            && py_code_type.is_some()
            && get_tstate.is_some()
        {
            break;
        }
    }

    let py_runtime_addr = py_runtime.ok_or(InitError::SymbolNotFound("_PyRuntime"))?;
    let py_version_addr = py_version.ok_or(InitError::SymbolNotFound("Py_Version"))?;
    let py_code_type_addr = py_code_type.ok_or(InitError::SymbolNotFound("PyCode_Type"))?;
    let get_tstate_addr =
        get_tstate.ok_or(InitError::SymbolNotFound("_PyThreadState_GetCurrent"))?;

    Ok(ElfSymbols {
        py_runtime_addr,
        py_version_addr,
        py_code_type_addr,
        get_tstate_addr,
    })
}

/// Read `Py_Version` from live memory, parse it, and validate it is a supported CPython version.
///
/// Currently supports CPython 3.14 only.
/// Returns [`PythonVersion`] on success, or [`InitError::UnsupportedVersion`]
/// for unsupported versions.
pub fn detect_version(py_version_addr: u64) -> Result<PythonVersion, InitError> {
    let raw = kindasafe::u64(py_version_addr).map_err(|_| InitError::UnsupportedVersion)?;
    let version_hex = raw & 0xFFFF_FFFF;
    let version = parse_version(version_hex);
    if version.major != 3 || version.minor != 14 {
        return Err(InitError::UnsupportedVersion);
    }
    Ok(version)
}

/// Read `Py_Version` raw value from live memory as a 32-bit `PY_VERSION_HEX`.
///
/// This is the raw value needed by [`read_debug_offsets`] for cookie validation.
pub fn read_version_hex(py_version_addr: u64) -> Result<u64, InitError> {
    let raw = kindasafe::u64(py_version_addr).map_err(|_| InitError::UnsupportedVersion)?;
    Ok(raw & 0xFFFF_FFFF)
}

/// Read `_Py_DebugOffsets` from `_PyRuntime` and return it as a
/// [`py314::_Py_DebugOffsets`].
///
/// `py_runtime_addr` is the absolute address of `_PyRuntime`.
/// `version` is the validated [`PythonVersion`] from [`detect_version`].
/// `version_hex` is the raw `PY_VERSION_HEX` from [`read_version_hex`].
///
/// Returns [`InitError::DebugOffsetsMismatch`] if cookie, version, or
/// `free_threaded` validation fails.
pub fn read_debug_offsets(
    py_runtime_addr: u64,
    version: &PythonVersion,
    version_hex: u64,
) -> Result<py314::_Py_DebugOffsets, InitError> {
    match version.minor {
        14 => {
            let mut buf = [0u8; size_of::<py314::_Py_DebugOffsets>()];
            kindasafe::slice(&mut buf, py_runtime_addr)
                .map_err(|_| InitError::DebugOffsetsMismatch)?;
            parse_repr_c::<py314::_Py_DebugOffsets>(&buf, version_hex)
        }
        _ => Err(InitError::UnsupportedVersion),
    }
}

/// Common header validation for any `_Py_DebugOffsets` layout.
///
/// Checks cookie, version, and free_threaded at the fixed offsets (0, 8, 16).
fn parse_repr_c<T>(buf: &[u8], expected_version: u64) -> Result<T, InitError> {
    let size = size_of::<T>();
    if buf.len() < size {
        return Err(InitError::DebugOffsetsMismatch);
    }
    // Cookie at offset 0 (8 bytes), version at offset 8, free_threaded at offset 16
    let cookie = u64::from_le_bytes(buf[0..8].try_into().unwrap());
    if cookie != COOKIE {
        return Err(InitError::DebugOffsetsMismatch);
    }
    let version = u64::from_le_bytes(buf[8..16].try_into().unwrap());
    if version != expected_version {
        return Err(InitError::DebugOffsetsMismatch);
    }
    let free_threaded = u64::from_le_bytes(buf[16..24].try_into().unwrap());
    if free_threaded != 0 {
        return Err(InitError::DebugOffsetsMismatch);
    }
    // SAFETY: buf is at least size_of::<T>() bytes. T is #[repr(C)] with only
    // u64 and [u8; 8] fields. Any bit pattern is valid.
    Ok(unsafe { core::ptr::read_unaligned(buf.as_ptr() as *const T) })
}

#[derive(Debug, PartialEq)]
pub struct PythonBinary {
    pub base: u64,
    pub path: String,
}

// Flags bitmask for /proc/maps permissions field
pub const FLAGS_READ: u32 = 0x1;
pub const FLAGS_WRITE: u32 = 0x2;
pub const FLAGS_EXEC: u32 = 0x4;
pub const FLAGS_SHARED: u32 = 0x8; // 's' = shared, 'p' = private (0)

/// Fields parsed from a single `/proc/maps` line, in order.
/// `path` is a subslice of the original line — no allocation.
type MapsLineFields<'a> = (u64, u64, u32, u64, u32, u32, u64, &'a [u8]);

/// Parse a single `/proc/maps` line.
///
/// Returns `(start, end, flags, offset, dev_major, dev_minor, inode, path_bytes)`.
/// `path_bytes` is a subslice of `line` — no allocation.
/// Returns `None` if the line is malformed.
fn parse_maps_line(line: &[u8]) -> Option<MapsLineFields<'_>> {
    // Format: start-end perms offset dev inode [path]
    // Example: 7f1234560000-7f1234580000 r--p 00000000 08:01 123456 /usr/lib/libpython3.11.so.1.0

    let mut iter = line.splitn(6, |&b| b == b' ');

    // Field 1: "start-end"
    let addr_field = iter.next()?;
    let dash = addr_field.iter().position(|&b| b == b'-')?;
    let start = u64::from_str_radix(core::str::from_utf8(&addr_field[..dash]).ok()?, 16).ok()?;
    let end = u64::from_str_radix(core::str::from_utf8(&addr_field[dash + 1..]).ok()?, 16).ok()?;

    // Field 2: "rwxp" or "rwxs"
    let perms = iter.next()?;
    if perms.len() < 4 {
        return None;
    }
    let mut flags: u32 = 0;
    if perms[0] == b'r' {
        flags |= FLAGS_READ;
    }
    if perms[1] == b'w' {
        flags |= FLAGS_WRITE;
    }
    if perms[2] == b'x' {
        flags |= FLAGS_EXEC;
    }
    if perms[3] == b's' {
        flags |= FLAGS_SHARED;
    }

    // Field 3: offset (hex)
    let offset_field = iter.next()?;
    let offset = u64::from_str_radix(core::str::from_utf8(offset_field).ok()?, 16).ok()?;

    // Field 4: "major:minor"
    let dev_field = iter.next()?;
    let colon = dev_field.iter().position(|&b| b == b':')?;
    let dev_major =
        u32::from_str_radix(core::str::from_utf8(&dev_field[..colon]).ok()?, 16).ok()?;
    let dev_minor =
        u32::from_str_radix(core::str::from_utf8(&dev_field[colon + 1..]).ok()?, 16).ok()?;

    // Field 5: inode (decimal)
    let inode_field = iter.next()?;
    let inode = core::str::from_utf8(inode_field)
        .ok()?
        .trim()
        .parse::<u64>()
        .ok()?;

    // Field 6: optional path (remainder), strip leading spaces and trailing newline
    let path_bytes = iter.next().map_or(b"".as_slice(), |rest| rest.trim_ascii());

    Some((
        start, end, flags, offset, dev_major, dev_minor, inode, path_bytes,
    ))
}

fn find_python_in_maps_reader<R: BufRead>(mut reader: R) -> Result<PythonBinary, InitError> {
    // We track the *first* mapping seen for each candidate.
    // libpython3 is preferred over python3.
    let mut libpython3: Option<PythonBinary> = None;
    let mut python3: Option<PythonBinary> = None;

    // Reuse a single buffer across all lines to avoid repeated allocations.
    let mut buf: Vec<u8> = Vec::with_capacity(256);

    loop {
        buf.clear();
        let n = reader
            .read_until(b'\n', &mut buf)
            .map_err(|_| InitError::PythonNotFound)?;
        if n == 0 {
            break;
        }

        let (start, _end, _flags, _offset, _dev_major, _dev_minor, _inode, path_bytes) =
            match parse_maps_line(&buf) {
                Some(e) => e,
                None => continue,
            };

        // Check for libpython3 (preferred)
        if libpython3.is_none() && path_contains(path_bytes, b"libpython3") {
            libpython3 = Some(PythonBinary {
                base: start,
                path: String::from_utf8_lossy(path_bytes).into_owned(),
            });
            // Once we have a libpython3 candidate we're done — it will always win.
            break;
        }

        // Check for python3 (fallback) — only if no python3 yet
        if python3.is_none() && path_contains(path_bytes, b"python3") {
            python3 = Some(PythonBinary {
                base: start,
                path: String::from_utf8_lossy(path_bytes).into_owned(),
            });
            // Don't break here: a later libpython3 entry would be preferred.
        }
    }

    libpython3.or(python3).ok_or(InitError::PythonNotFound)
}

/// Check whether `haystack` contains the byte-string `needle` as a substring.
/// No allocation.
fn path_contains(haystack: &[u8], needle: &[u8]) -> bool {
    if needle.is_empty() || haystack.len() < needle.len() {
        return false;
    }
    haystack.windows(needle.len()).any(|w| w == needle)
}

/// Parse `/proc/self/maps` and return the `PythonBinary` describing where Python
/// (or libpython3) is loaded.
///
/// Prefers a `libpython3` mapping over a bare `python3` mapping.
/// Returns [`InitError::PythonNotFound`] (error code 2) when neither is found.
pub fn find_python_in_maps() -> Result<PythonBinary, InitError> {
    let f = std::fs::File::open("/proc/self/maps").map_err(|_| InitError::PythonNotFound)?;
    find_python_in_maps_reader(std::io::BufReader::new(f))
}

/// Parse `/proc/self/maps` and return the `PythonBinary` describing where the
/// `_asyncio` CPython extension module is loaded.
///
/// Looks for a mapping whose path contains `_asyncio.cpython-3`.
/// Returns [`InitError::PythonNotFound`] when the module is not loaded.
pub fn find_asyncio_in_maps() -> Result<PythonBinary, InitError> {
    let f = std::fs::File::open("/proc/self/maps").map_err(|_| InitError::PythonNotFound)?;
    find_asyncio_in_maps_reader(std::io::BufReader::new(f))
}

fn find_asyncio_in_maps_reader<R: BufRead>(mut reader: R) -> Result<PythonBinary, InitError> {
    let mut buf: Vec<u8> = Vec::with_capacity(256);
    loop {
        buf.clear();
        let n = reader
            .read_until(b'\n', &mut buf)
            .map_err(|_| InitError::PythonNotFound)?;
        if n == 0 {
            break;
        }
        let (start, _end, _flags, _offset, _dev_major, _dev_minor, _inode, path_bytes) =
            match parse_maps_line(&buf) {
                Some(e) => e,
                None => continue,
            };
        if path_contains(path_bytes, b"_asyncio.cpython-3") {
            return Ok(PythonBinary {
                base: start,
                path: String::from_utf8_lossy(path_bytes).into_owned(),
            });
        }
    }
    Err(InitError::PythonNotFound)
}

/// Open the `_asyncio` extension module ELF binary, find the `_AsyncioDebug`
/// symbol, and return its absolute runtime address.
///
/// Lookup order: dynamic symbols (`.dynsym`), then regular symbols (`.symtab`),
/// then fall back to the `.AsyncioDebug` ELF section address.
pub fn resolve_asyncio_debug_symbol(binary: &PythonBinary) -> Result<u64, InitError> {
    let file = std::fs::File::open(&binary.path).map_err(|_| InitError::Io)?;
    let mmap = unsafe { memmap2::Mmap::map(&file) }.map_err(|_| InitError::Io)?;
    resolve_asyncio_debug_symbol_from_bytes(&mmap, binary.base)
}

fn resolve_asyncio_debug_symbol_from_bytes(
    data: &[u8],
    mapped_base: u64,
) -> Result<u64, InitError> {
    let obj = object::File::parse(data).map_err(|_| InitError::ElfParse)?;

    let elf_base = obj.segments().map(|s| s.address()).min().unwrap_or(0);
    let load_bias = mapped_base.wrapping_sub(elf_base);

    // Try dynamic symbols first (most common for .so files).
    for sym in obj.dynamic_symbols() {
        if sym.name() == Ok("_AsyncioDebug") {
            return Ok(sym.address().wrapping_add(load_bias));
        }
    }

    // Fall back to regular symbol table.
    for sym in obj.symbols() {
        if sym.name() == Ok("_AsyncioDebug") {
            return Ok(sym.address().wrapping_add(load_bias));
        }
    }

    // Last resort: look up the `.AsyncioDebug` section and use its address.
    use object::ObjectSection;
    for section in obj.sections() {
        if section.name() == Ok(".AsyncioDebug") {
            return Ok(section.address().wrapping_add(load_bias));
        }
    }

    Err(InitError::SymbolNotFound("_AsyncioDebug"))
}

/// Read `Py_AsyncioModuleDebugOffsets` from live memory at `addr`.
pub fn read_asyncio_debug_offsets(
    addr: u64,
) -> Result<py314::Py_AsyncioModuleDebugOffsets, InitError> {
    let mut buf = [0u8; size_of::<py314::Py_AsyncioModuleDebugOffsets>()];
    kindasafe::slice(&mut buf, addr).map_err(|_| InitError::DebugOffsetsMismatch)?;
    // SAFETY: Py_AsyncioModuleDebugOffsets is #[repr(C)] with only u64 fields.
    // Any bit pattern is valid.
    Ok(unsafe {
        core::ptr::read_unaligned(buf.as_ptr() as *const py314::Py_AsyncioModuleDebugOffsets)
    })
}

#[cfg(test)]
mod tests {
    use super::*;

    // ── parse_version tests ────────────────────────────────────────────────

    #[test]
    fn parse_version_3_14_0_final() {
        let v = parse_version(0x030E00F0);
        assert_eq!(
            v,
            PythonVersion {
                major: 3,
                minor: 14,
                micro: 0
            }
        );
    }

    #[test]
    fn parse_version_3_14_2_final() {
        let v = parse_version(0x030E02F0);
        assert_eq!(
            v,
            PythonVersion {
                major: 3,
                minor: 14,
                micro: 2
            }
        );
    }

    #[test]
    fn parse_version_3_13_1_unsupported() {
        // Python 3.13 is no longer supported — parse_version still works
        // but detect_version would reject it.
        let v = parse_version(0x030D01F0);
        assert_eq!(
            v,
            PythonVersion {
                major: 3,
                minor: 13,
                micro: 1
            }
        );
    }

    // ── parse_maps_line tests ────────────────────────────────────────────────

    #[test]
    fn parse_libpython3_ro_header() {
        let line =
            b"7f1234560000-7f1234580000 r--p 00000000 08:01 123456 /usr/lib/libpython3.11.so.1.0\n";
        let (start, end, flags, offset, dev_major, dev_minor, inode, path) =
            parse_maps_line(line).unwrap();
        assert_eq!(start, 0x7f1234560000);
        assert_eq!(end, 0x7f1234580000);
        assert_eq!(flags, FLAGS_READ);
        assert_eq!(offset, 0);
        assert_eq!(dev_major, 8);
        assert_eq!(dev_minor, 1);
        assert_eq!(inode, 123456);
        assert_eq!(path, b"/usr/lib/libpython3.11.so.1.0");
    }

    #[test]
    fn parse_libpython3_exec_mapping() {
        let line =
            b"7f1234580000-7f1234600000 r-xp 00020000 08:01 123456 /usr/lib/libpython3.11.so.1.0\n";
        let (start, _end, flags, offset, _dmaj, _dmin, _inode, path) =
            parse_maps_line(line).unwrap();
        assert_eq!(start, 0x7f1234580000);
        assert_eq!(flags, FLAGS_READ | FLAGS_EXEC);
        assert_eq!(offset, 0x20000);
        assert_eq!(path, b"/usr/lib/libpython3.11.so.1.0");
    }

    #[test]
    fn parse_static_python3() {
        let line = b"555555554000-5555555b2000 r--p 00000000 08:01 654321 /usr/bin/python3\n";
        let (start, _end, flags, _off, _dmaj, _dmin, inode, path) = parse_maps_line(line).unwrap();
        assert_eq!(start, 0x555555554000);
        assert_eq!(flags, FLAGS_READ);
        assert_eq!(inode, 654321);
        assert_eq!(path, b"/usr/bin/python3");
    }

    #[test]
    fn parse_anonymous_mapping() {
        let line = b"7fff12340000-7fff12360000 rw-p 00000000 00:00 0 \n";
        let (start, _end, flags, _off, dev_major, dev_minor, inode, path) =
            parse_maps_line(line).unwrap();
        assert_eq!(start, 0x7fff12340000);
        assert_eq!(flags, FLAGS_READ | FLAGS_WRITE);
        assert_eq!(dev_major, 0);
        assert_eq!(dev_minor, 0);
        assert_eq!(inode, 0);
        assert_eq!(path, b"");
    }

    #[test]
    fn parse_anonymous_mapping_no_trailing_space() {
        // Some kernels emit no trailing space for anonymous mappings
        let line = b"7fff12340000-7fff12360000 rw-p 00000000 00:00 0\n";
        let result = parse_maps_line(line);
        assert!(result.is_some());
        let (_s, _e, _f, _o, _dm, _dn, _i, path) = result.unwrap();
        assert_eq!(path, b"");
    }

    #[test]
    fn parse_vdso() {
        let line = b"7fff12370000-7fff12372000 r-xp 00000000 00:00 0 [vdso]\n";
        let (_s, _e, flags, _o, _dm, _dn, _i, path) = parse_maps_line(line).unwrap();
        assert_eq!(flags, FLAGS_READ | FLAGS_EXEC);
        assert_eq!(path, b"[vdso]");
    }

    #[test]
    fn parse_shared_mapping() {
        let line = b"7f0000000000-7f0000010000 rw-s 00000000 00:05 0 /dev/zero\n";
        let (_s, _e, flags, _o, _dm, _dn, _i, _path) = parse_maps_line(line).unwrap();
        assert_eq!(flags, FLAGS_READ | FLAGS_WRITE | FLAGS_SHARED);
    }

    #[test]
    fn parse_malformed_line_returns_none() {
        assert!(parse_maps_line(b"not a valid maps line\n").is_none());
        assert!(parse_maps_line(b"\n").is_none());
    }

    // ── find_python_in_maps_reader tests ────────────────────────────────────

    const MAPS_LIBPYTHON3_ONLY: &[u8] = b"\
7f0000000000-7f0000020000 r--p 00000000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
7f0000020000-7f0000100000 r-xp 00020000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
7fff00000000-7fff00020000 rw-p 00000000 00:00 0\n\
";

    const MAPS_PYTHON3_ONLY: &[u8] = b"\
555555554000-5555555b2000 r--p 00000000 08:01 222 /usr/bin/python3\n\
5555555b2000-555555600000 r-xp 0005e000 08:01 222 /usr/bin/python3\n\
7fff00000000-7fff00020000 rw-p 00000000 00:00 0\n\
";

    const MAPS_BOTH: &[u8] = b"\
555555554000-5555555b2000 r--p 00000000 08:01 222 /usr/bin/python3\n\
7f0000000000-7f0000020000 r--p 00000000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
7f0000020000-7f0000100000 r-xp 00020000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
";

    const MAPS_LIBPYTHON3_MULTIPLE: &[u8] = b"\
7f0000000000-7f0000020000 r--p 00000000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
7f0000020000-7f0000100000 r-xp 00020000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
7f0000200000-7f0000210000 r--p 00000000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
";

    const MAPS_NO_PYTHON: &[u8] = b"\
7f0000000000-7f0000020000 r--p 00000000 08:01 333 /usr/lib/libc.so.6\n\
7fff00000000-7fff00020000 rw-p 00000000 00:00 0\n\
";

    fn run(maps: &[u8]) -> Result<PythonBinary, InitError> {
        find_python_in_maps_reader(std::io::Cursor::new(maps))
    }

    #[test]
    fn finds_libpython3_only() {
        let bin = run(MAPS_LIBPYTHON3_ONLY).unwrap();
        assert_eq!(bin.base, 0x7f0000000000);
        assert!(bin.path.contains("libpython3"));
    }

    #[test]
    fn finds_python3_only() {
        let bin = run(MAPS_PYTHON3_ONLY).unwrap();
        assert_eq!(bin.base, 0x555555554000);
        assert!(bin.path.contains("python3"));
    }

    #[test]
    fn prefers_libpython3_over_python3() {
        let bin = run(MAPS_BOTH).unwrap();
        assert!(
            bin.path.contains("libpython3"),
            "expected libpython3, got {}",
            bin.path
        );
        assert_eq!(bin.base, 0x7f0000000000);
    }

    #[test]
    fn returns_first_mapping_base() {
        // The first mapping (r--p, offset 0) should be the base, not the r-xp one.
        let bin = run(MAPS_LIBPYTHON3_MULTIPLE).unwrap();
        assert_eq!(bin.base, 0x7f0000000000);
    }

    #[test]
    fn returns_python_not_found_when_absent() {
        assert_eq!(run(MAPS_NO_PYTHON), Err(InitError::PythonNotFound));
    }

    #[test]
    fn empty_maps_returns_not_found() {
        assert_eq!(run(b""), Err(InitError::PythonNotFound));
    }

    #[test]
    fn python3_before_libpython3_still_prefers_libpython3() {
        // python3 entry appears first, but libpython3 comes later — must prefer libpython3
        let maps = b"\
555555554000-5555555b2000 r--p 00000000 08:01 222 /usr/bin/python3\n\
7f0000000000-7f0000020000 r--p 00000000 08:01 111 /usr/lib/libpython3.11.so.1.0\n\
";
        let bin = run(maps).unwrap();
        assert!(bin.path.contains("libpython3"), "should prefer libpython3");
    }

    // ── resolve_elf_symbols_from_bytes tests ─────────────────────────────────

    // Real libpython3.14.so.1.0 committed as a test fixture.
    // Symbol values verified with `nm --dynamic`:
    //   _PyRuntime  0x71bd00
    //   Py_Version  0x61c1b0
    const LIBPYTHON314: &[u8] = include_bytes!("../testdata/libpython3.14.so.1.0");

    #[test]
    fn resolves_all_symbols() {
        // mapped_base = 0 → load_bias = 0 (ET_DYN, relative_address_base() = 0)
        // absolute addr = symbol st_value + 0 = st_value
        let result = resolve_elf_symbols_from_bytes(LIBPYTHON314, 0).unwrap();
        assert_eq!(result.py_runtime_addr, 0x71bd00);
        assert_eq!(result.py_version_addr, 0x61c1b0);
        assert_eq!(result.py_code_type_addr, 0x6e2b60);
        assert_eq!(result.get_tstate_addr, 0x2d2140);
    }

    #[test]
    fn applies_load_bias() {
        let mapped_base: u64 = 0x7f00_0000_0000;
        let result = resolve_elf_symbols_from_bytes(LIBPYTHON314, mapped_base).unwrap();
        assert_eq!(result.py_runtime_addr, mapped_base + 0x71bd00);
        assert_eq!(result.py_version_addr, mapped_base + 0x61c1b0);
        assert_eq!(result.py_code_type_addr, mapped_base + 0x6e2b60);
        assert_eq!(result.get_tstate_addr, mapped_base + 0x2d2140);
    }

    #[test]
    fn elf_invalid_bytes_returns_elf_parse_error() {
        let result = resolve_elf_symbols_from_bytes(b"not an elf file", 0);
        assert_eq!(result, Err(InitError::ElfParse));
    }

    // ── find_asyncio_in_maps_reader tests ────────────────────────────────────

    fn run_asyncio(maps: &[u8]) -> Result<PythonBinary, InitError> {
        find_asyncio_in_maps_reader(std::io::Cursor::new(maps))
    }

    const MAPS_WITH_ASYNCIO: &[u8] = b"\
7f0000000000-7f0000020000 r--p 00000000 08:01 111 /usr/lib/libpython3.14.so.1.0\n\
7f0000100000-7f0000110000 r--p 00000000 08:01 222 /usr/lib/python3.14/lib-dynload/_asyncio.cpython-314-x86_64-linux-gnu.so\n\
7f0000110000-7f0000120000 r-xp 00010000 08:01 222 /usr/lib/python3.14/lib-dynload/_asyncio.cpython-314-x86_64-linux-gnu.so\n\
";

    const MAPS_WITHOUT_ASYNCIO: &[u8] = b"\
7f0000000000-7f0000020000 r--p 00000000 08:01 111 /usr/lib/libpython3.14.so.1.0\n\
7fff00000000-7fff00020000 rw-p 00000000 00:00 0\n\
";

    #[test]
    fn finds_asyncio_module() {
        let bin = run_asyncio(MAPS_WITH_ASYNCIO).unwrap();
        assert_eq!(bin.base, 0x7f0000100000);
        assert!(bin.path.contains("_asyncio.cpython-314"));
    }

    #[test]
    fn returns_first_asyncio_mapping() {
        // Should return the first (r--p, offset 0) mapping, not the r-xp one.
        let bin = run_asyncio(MAPS_WITH_ASYNCIO).unwrap();
        assert_eq!(bin.base, 0x7f0000100000);
    }

    #[test]
    fn asyncio_not_found_when_absent() {
        assert_eq!(
            run_asyncio(MAPS_WITHOUT_ASYNCIO),
            Err(InitError::PythonNotFound)
        );
    }

    #[test]
    fn asyncio_not_found_in_empty_maps() {
        assert_eq!(run_asyncio(b""), Err(InitError::PythonNotFound));
    }

    // ── resolve_asyncio_debug_symbol_from_bytes tests ────────────────────────

    #[test]
    fn asyncio_debug_invalid_elf() {
        let result = resolve_asyncio_debug_symbol_from_bytes(b"not an elf file", 0);
        assert_eq!(result, Err(InitError::ElfParse));
    }

    // ── resolve_asyncio_debug_symbol_from_bytes against real _asyncio.so ─────

    // Real _asyncio.cpython-314-x86_64-linux-gnu.so committed as a test fixture.
    // The _AsyncioDebug symbol is only in the .AsyncioDebug ELF section (not .dynsym/.symtab).
    // Section address verified with: readelf -S ... | grep AsyncioDebug → 0x117c0
    const ASYNCIO_SO: &[u8] =
        include_bytes!("../testdata/_asyncio.cpython-314-x86_64-linux-gnu.so");

    #[test]
    fn resolves_asyncio_debug_section() {
        // mapped_base = 0 → load_bias = 0
        let addr = resolve_asyncio_debug_symbol_from_bytes(ASYNCIO_SO, 0).unwrap();
        assert_eq!(addr, 0x117c0, "expected .AsyncioDebug section address");
    }

    #[test]
    fn resolves_asyncio_debug_with_load_bias() {
        let mapped_base: u64 = 0x7f00_0000_0000;
        let addr = resolve_asyncio_debug_symbol_from_bytes(ASYNCIO_SO, mapped_base).unwrap();
        assert_eq!(addr, mapped_base + 0x117c0);
    }
}
```

## File: `kit/python_offsets/tests/integration.rs`
```rust
#[cfg(all(target_arch = "x86_64", target_os = "linux"))]
mod linux {
    use anyhow::{Result, anyhow};
    use std::ffi::CString;

    const LIBPYTHON_PATH: &str =
        concat!(env!("CARGO_MANIFEST_DIR"), "/testdata/libpython3.14.so.1.0");

    const ASYNCIO_SO_PATH: &str = concat!(
        env!("CARGO_MANIFEST_DIR"),
        "/testdata/_asyncio.cpython-314-x86_64-linux-gnu.so"
    );

    /// dlopen a shared library with the given flags. Panics if the handle is null.
    fn dlopen_flags(path: &str, flags: libc::c_int) -> *mut libc::c_void {
        let cstr = CString::new(path).unwrap();
        let handle = unsafe { libc::dlopen(cstr.as_ptr(), flags) };
        assert!(
            !handle.is_null(),
            "dlopen({path}) failed: {}",
            unsafe { std::ffi::CStr::from_ptr(libc::dlerror()) }.to_string_lossy()
        );
        handle
    }

    /// dlopen with RTLD_LAZY | RTLD_NODELETE (private symbols).
    fn dlopen_or_panic(path: &str) -> *mut libc::c_void {
        dlopen_flags(path, libc::RTLD_LAZY | libc::RTLD_NODELETE)
    }

    /// dlopen with RTLD_LAZY | RTLD_NODELETE | RTLD_GLOBAL so that
    /// subsequently loaded libraries can resolve symbols from this one.
    fn dlopen_global(path: &str) -> *mut libc::c_void {
        dlopen_flags(
            path,
            libc::RTLD_LAZY | libc::RTLD_NODELETE | libc::RTLD_GLOBAL,
        )
    }

    #[test]
    fn end_to_end_python_offsets() -> Result<()> {
        kindasafe_init::init().map_err(|e| anyhow!("kindasafe_init::init failed: {e:?}"))?;

        // RTLD_NODELETE keeps the library resident so dlclose doesn't run the
        // FINI destructors. The handle is intentionally leaked (not dlclosed)
        // since the test process is short-lived.
        let _handle = dlopen_or_panic(LIBPYTHON_PATH);

        let binary = python_offsets::find_python_in_maps()
            .map_err(|e| anyhow!("find_python_in_maps failed: {e:?}"))?;

        assert!(binary.path.contains("libpython3"));

        let symbols = python_offsets::resolve_elf_symbols(&binary)
            .map_err(|e| anyhow!("resolve_elf_symbols failed: {e:?}"))?;

        assert_ne!(symbols.py_runtime_addr, 0);
        assert_ne!(symbols.py_version_addr, 0);
        assert_ne!(symbols.get_tstate_addr, 0);

        // ── Version detection ────────────────────────────────────────────
        let version = python_offsets::detect_version(symbols.py_version_addr)
            .map_err(|e| anyhow!("detect_version failed: {e:?}"))?;

        assert_eq!(version.major, 3);
        assert_eq!(version.minor, 14);

        // ── Debug offsets parsing ────────────────────────────────────────
        let version_hex = python_offsets::read_version_hex(symbols.py_version_addr)
            .map_err(|e| anyhow!("read_version_hex failed: {e:?}"))?;

        let offsets =
            python_offsets::read_debug_offsets(symbols.py_runtime_addr, &version, version_hex)
                .map_err(|e| anyhow!("read_debug_offsets failed: {e:?}"))?;

        // Returns py314 layout directly.
        // Verify key offsets are populated. Some offsets can legitimately
        // be 0 (e.g. executable if f_executable is the first field of
        // _PyInterpreterFrame, as it is in 3.14.3+).
        assert_ne!(offsets.runtime_state.interpreters_head, 0);
        assert_ne!(offsets.interpreter_state.threads_head, 0);
        assert_ne!(offsets.thread_state.native_thread_id, 0);
        assert_ne!(offsets.thread_state.next, 0);
        assert_ne!(offsets.interpreter_frame.previous, 0);
        assert_ne!(offsets.code_object.filename, 0);
        assert_ne!(offsets.code_object.qualname, 0);
        assert_ne!(offsets.unicode_object.asciiobject_size, 0);

        Ok(())
    }

    #[test]
    fn end_to_end_asyncio_offsets() -> Result<()> {
        kindasafe_init::init().map_err(|e| anyhow!("kindasafe_init::init failed: {e:?}"))?;

        // _asyncio.so depends on libpython symbols (PyTraceBack_Type, etc.),
        // so load libpython first with RTLD_GLOBAL to export its symbols.
        let _libpython = dlopen_global(LIBPYTHON_PATH);
        let _handle = dlopen_or_panic(ASYNCIO_SO_PATH);

        // ── Find _asyncio in /proc/self/maps ─────────────────────────────
        let binary = python_offsets::find_asyncio_in_maps()
            .map_err(|e| anyhow!("find_asyncio_in_maps failed: {e:?}"))?;

        assert!(
            binary.path.contains("_asyncio.cpython-314"),
            "unexpected path: {}",
            binary.path
        );
        assert_ne!(binary.base, 0);

        // ── Resolve _AsyncioDebug symbol ─────────────────────────────────
        let addr = python_offsets::resolve_asyncio_debug_symbol(&binary)
            .map_err(|e| anyhow!("resolve_asyncio_debug_symbol failed: {e:?}"))?;

        assert_ne!(addr, 0, "_AsyncioDebug address must be nonzero");

        // ── Read Py_AsyncioModuleDebugOffsets from live memory ───────────
        let offsets = python_offsets::read_asyncio_debug_offsets(addr)
            .map_err(|e| anyhow!("read_asyncio_debug_offsets failed: {e:?}"))?;

        // Validate task_object sub-struct: size must be nonzero (it's sizeof(TaskObj)),
        // and the field offsets must be nonzero (they are byte offsets into TaskObj).
        assert_ne!(
            offsets.asyncio_task_object.size, 0,
            "task_object.size must be nonzero"
        );
        assert_ne!(
            offsets.asyncio_task_object.task_name, 0,
            "task_object.task_name must be nonzero"
        );
        assert_ne!(
            offsets.asyncio_task_object.task_coro, 0,
            "task_object.task_coro must be nonzero"
        );
        assert_ne!(
            offsets.asyncio_task_object.task_node, 0,
            "task_object.task_node must be nonzero"
        );

        // Validate thread_state sub-struct: size must be nonzero (it's
        // sizeof(_PyThreadStateImpl)), and the offsets must be nonzero.
        assert_ne!(
            offsets.asyncio_thread_state.size, 0,
            "thread_state.size must be nonzero"
        );
        assert_ne!(
            offsets.asyncio_thread_state.asyncio_running_loop, 0,
            "thread_state.asyncio_running_loop must be nonzero"
        );
        assert_ne!(
            offsets.asyncio_thread_state.asyncio_running_task, 0,
            "thread_state.asyncio_running_task must be nonzero"
        );
        assert_ne!(
            offsets.asyncio_thread_state.asyncio_tasks_head, 0,
            "thread_state.asyncio_tasks_head must be nonzero"
        );

        // Validate interpreter_state sub-struct.
        assert_ne!(
            offsets.asyncio_interpreter_state.size, 0,
            "interpreter_state.size must be nonzero"
        );
        assert_ne!(
            offsets.asyncio_interpreter_state.asyncio_tasks_head, 0,
            "interpreter_state.asyncio_tasks_head must be nonzero"
        );

        // Sanity: task_object.size should be a reasonable struct size
        // (at least 100 bytes for TaskObj, at most 4096).
        assert!(
            offsets.asyncio_task_object.size >= 100 && offsets.asyncio_task_object.size <= 4096,
            "task_object.size {} looks unreasonable",
            offsets.asyncio_task_object.size
        );

        Ok(())
    }
}
```

## File: `kit/python_offsets_types/Cargo.toml`
```
[package]
name = "python_offsets_types"
version = "0.1.0"
edition = "2024"
publish = false

[dependencies]
```

## File: `kit/python_offsets_types/src/lib.rs`
```rust
#![no_std]

pub mod py313;
pub mod py314;

/// Convert a 3.14 `_Py_DebugOffsets` into the 3.13 layout (common denominator).
/// Fields only present in 3.14 are dropped; shared sub-structs are copied
/// field-by-field since the 3.14 versions may have extra trailing fields.
impl From<&py314::_Py_DebugOffsets> for py313::_Py_DebugOffsets {
    fn from(v: &py314::_Py_DebugOffsets) -> Self {
        Self {
            cookie: v.cookie,
            version: v.version,
            free_threaded: v.free_threaded,
            runtime_state: py313::_Py_DebugOffsets__runtime_state {
                size: v.runtime_state.size,
                finalizing: v.runtime_state.finalizing,
                interpreters_head: v.runtime_state.interpreters_head,
            },
            interpreter_state: py313::_Py_DebugOffsets__interpreter_state {
                size: v.interpreter_state.size,
                id: v.interpreter_state.id,
                next: v.interpreter_state.next,
                threads_head: v.interpreter_state.threads_head,
                // 3.14 has threads_main here; 3.13 does not — skip it
                gc: v.interpreter_state.gc,
                imports_modules: v.interpreter_state.imports_modules,
                sysdict: v.interpreter_state.sysdict,
                builtins: v.interpreter_state.builtins,
                ceval_gil: v.interpreter_state.ceval_gil,
                gil_runtime_state: v.interpreter_state.gil_runtime_state,
                gil_runtime_state_enabled: v.interpreter_state.gil_runtime_state_enabled,
                gil_runtime_state_locked: v.interpreter_state.gil_runtime_state_locked,
                gil_runtime_state_holder: v.interpreter_state.gil_runtime_state_holder,
            },
            thread_state: py313::_Py_DebugOffsets__thread_state {
                size: v.thread_state.size,
                prev: v.thread_state.prev,
                next: v.thread_state.next,
                interp: v.thread_state.interp,
                current_frame: v.thread_state.current_frame,
                thread_id: v.thread_state.thread_id,
                native_thread_id: v.thread_state.native_thread_id,
                datastack_chunk: v.thread_state.datastack_chunk,
                status: v.thread_state.status,
            },
            interpreter_frame: py313::_Py_DebugOffsets__interpreter_frame {
                size: v.interpreter_frame.size,
                previous: v.interpreter_frame.previous,
                executable: v.interpreter_frame.executable,
                instr_ptr: v.interpreter_frame.instr_ptr,
                localsplus: v.interpreter_frame.localsplus,
                owner: v.interpreter_frame.owner,
                // 3.14 has stackpointer here; 3.13 does not — drop it
            },
            code_object: py313::_Py_DebugOffsets__code_object {
                size: v.code_object.size,
                filename: v.code_object.filename,
                name: v.code_object.name,
                qualname: v.code_object.qualname,
                linetable: v.code_object.linetable,
                firstlineno: v.code_object.firstlineno,
                argcount: v.code_object.argcount,
                localsplusnames: v.code_object.localsplusnames,
                localspluskinds: v.code_object.localspluskinds,
                co_code_adaptive: v.code_object.co_code_adaptive,
            },
            pyobject: py313::_Py_DebugOffsets__pyobject {
                size: v.pyobject.size,
                ob_type: v.pyobject.ob_type,
            },
            type_object: py313::_Py_DebugOffsets__type_object {
                size: v.type_object.size,
                tp_name: v.type_object.tp_name,
                tp_repr: v.type_object.tp_repr,
                tp_flags: v.type_object.tp_flags,
            },
            tuple_object: py313::_Py_DebugOffsets__tuple_object {
                size: v.tuple_object.size,
                ob_item: v.tuple_object.ob_item,
                ob_size: v.tuple_object.ob_size,
            },
            list_object: py313::_Py_DebugOffsets__list_object {
                size: v.list_object.size,
                ob_item: v.list_object.ob_item,
                ob_size: v.list_object.ob_size,
            },
            dict_object: py313::_Py_DebugOffsets__dict_object {
                size: v.dict_object.size,
                ma_keys: v.dict_object.ma_keys,
                ma_values: v.dict_object.ma_values,
            },
            float_object: py313::_Py_DebugOffsets__float_object {
                size: v.float_object.size,
                ob_fval: v.float_object.ob_fval,
            },
            long_object: py313::_Py_DebugOffsets__long_object {
                size: v.long_object.size,
                lv_tag: v.long_object.lv_tag,
                ob_digit: v.long_object.ob_digit,
            },
            bytes_object: py313::_Py_DebugOffsets__bytes_object {
                size: v.bytes_object.size,
                ob_size: v.bytes_object.ob_size,
                ob_sval: v.bytes_object.ob_sval,
            },
            unicode_object: py313::_Py_DebugOffsets__unicode_object {
                size: v.unicode_object.size,
                state: v.unicode_object.state,
                length: v.unicode_object.length,
                asciiobject_size: v.unicode_object.asciiobject_size,
            },
            gc: py313::_Py_DebugOffsets__gc {
                size: v.gc.size,
                collecting: v.gc.collecting,
            },
            // 3.14 sub-structs not in 3.13: set_object, gen_object, debugger_support — dropped
        }
    }
}
```

## File: `kit/python_offsets_types/src/py313.rs`
```rust
/* automatically generated by rust-bindgen 0.72.1 */

//! CPython `_Py_DebugOffsets` layout for `v3.13.0`.
//!
//! Auto-generated by `gen_debug_offsets.sh v3.13.0 py313`.
//! Do not edit by hand.

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets {
    pub cookie: [u8; 8usize],
    pub version: u64,
    pub free_threaded: u64,
    pub runtime_state: _Py_DebugOffsets__runtime_state,
    pub interpreter_state: _Py_DebugOffsets__interpreter_state,
    pub thread_state: _Py_DebugOffsets__thread_state,
    pub interpreter_frame: _Py_DebugOffsets__interpreter_frame,
    pub code_object: _Py_DebugOffsets__code_object,
    pub pyobject: _Py_DebugOffsets__pyobject,
    pub type_object: _Py_DebugOffsets__type_object,
    pub tuple_object: _Py_DebugOffsets__tuple_object,
    pub list_object: _Py_DebugOffsets__list_object,
    pub dict_object: _Py_DebugOffsets__dict_object,
    pub float_object: _Py_DebugOffsets__float_object,
    pub long_object: _Py_DebugOffsets__long_object,
    pub bytes_object: _Py_DebugOffsets__bytes_object,
    pub unicode_object: _Py_DebugOffsets__unicode_object,
    pub gc: _Py_DebugOffsets__gc,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__runtime_state {
    pub size: u64,
    pub finalizing: u64,
    pub interpreters_head: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__interpreter_state {
    pub size: u64,
    pub id: u64,
    pub next: u64,
    pub threads_head: u64,
    pub gc: u64,
    pub imports_modules: u64,
    pub sysdict: u64,
    pub builtins: u64,
    pub ceval_gil: u64,
    pub gil_runtime_state: u64,
    pub gil_runtime_state_enabled: u64,
    pub gil_runtime_state_locked: u64,
    pub gil_runtime_state_holder: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__thread_state {
    pub size: u64,
    pub prev: u64,
    pub next: u64,
    pub interp: u64,
    pub current_frame: u64,
    pub thread_id: u64,
    pub native_thread_id: u64,
    pub datastack_chunk: u64,
    pub status: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__interpreter_frame {
    pub size: u64,
    pub previous: u64,
    pub executable: u64,
    pub instr_ptr: u64,
    pub localsplus: u64,
    pub owner: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__code_object {
    pub size: u64,
    pub filename: u64,
    pub name: u64,
    pub qualname: u64,
    pub linetable: u64,
    pub firstlineno: u64,
    pub argcount: u64,
    pub localsplusnames: u64,
    pub localspluskinds: u64,
    pub co_code_adaptive: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__pyobject {
    pub size: u64,
    pub ob_type: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__type_object {
    pub size: u64,
    pub tp_name: u64,
    pub tp_repr: u64,
    pub tp_flags: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__tuple_object {
    pub size: u64,
    pub ob_item: u64,
    pub ob_size: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__list_object {
    pub size: u64,
    pub ob_item: u64,
    pub ob_size: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__dict_object {
    pub size: u64,
    pub ma_keys: u64,
    pub ma_values: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__float_object {
    pub size: u64,
    pub ob_fval: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__long_object {
    pub size: u64,
    pub lv_tag: u64,
    pub ob_digit: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__bytes_object {
    pub size: u64,
    pub ob_size: u64,
    pub ob_sval: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__unicode_object {
    pub size: u64,
    pub state: u64,
    pub length: u64,
    pub asciiobject_size: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__gc {
    pub size: u64,
    pub collecting: u64,
}
```

## File: `kit/python_offsets_types/src/py314.rs`
```rust
/* automatically generated by rust-bindgen 0.72.1 */

// @generated by gen_debug_offsets.sh v3.14.0 py314
// DO NOT EDIT — re-run the generator instead.
// See kit/python_offsets/gen_debug_offsets.sh for details.

#![allow(non_camel_case_types)]

//! CPython `_Py_DebugOffsets` layout for `v3.14.0`.
//!
//! Auto-generated by `gen_debug_offsets.sh v3.14.0 py314`.
//! Do not edit by hand.

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets {
    pub cookie: [u8; 8usize],
    pub version: u64,
    pub free_threaded: u64,
    pub runtime_state: _Py_DebugOffsets__runtime_state,
    pub interpreter_state: _Py_DebugOffsets__interpreter_state,
    pub thread_state: _Py_DebugOffsets__thread_state,
    pub interpreter_frame: _Py_DebugOffsets__interpreter_frame,
    pub code_object: _Py_DebugOffsets__code_object,
    pub pyobject: _Py_DebugOffsets__pyobject,
    pub type_object: _Py_DebugOffsets__type_object,
    pub tuple_object: _Py_DebugOffsets__tuple_object,
    pub list_object: _Py_DebugOffsets__list_object,
    pub set_object: _Py_DebugOffsets__set_object,
    pub dict_object: _Py_DebugOffsets__dict_object,
    pub float_object: _Py_DebugOffsets__float_object,
    pub long_object: _Py_DebugOffsets__long_object,
    pub bytes_object: _Py_DebugOffsets__bytes_object,
    pub unicode_object: _Py_DebugOffsets__unicode_object,
    pub gc: _Py_DebugOffsets__gc,
    pub gen_object: _Py_DebugOffsets__gen_object,
    pub llist_node: _Py_DebugOffsets__llist_node,
    pub debugger_support: _Py_DebugOffsets__debugger_support,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__runtime_state {
    pub size: u64,
    pub finalizing: u64,
    pub interpreters_head: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__interpreter_state {
    pub size: u64,
    pub id: u64,
    pub next: u64,
    pub threads_head: u64,
    pub threads_main: u64,
    pub gc: u64,
    pub imports_modules: u64,
    pub sysdict: u64,
    pub builtins: u64,
    pub ceval_gil: u64,
    pub gil_runtime_state: u64,
    pub gil_runtime_state_enabled: u64,
    pub gil_runtime_state_locked: u64,
    pub gil_runtime_state_holder: u64,
    pub code_object_generation: u64,
    pub tlbc_generation: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__thread_state {
    pub size: u64,
    pub prev: u64,
    pub next: u64,
    pub interp: u64,
    pub current_frame: u64,
    pub thread_id: u64,
    pub native_thread_id: u64,
    pub datastack_chunk: u64,
    pub status: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__interpreter_frame {
    pub size: u64,
    pub previous: u64,
    pub executable: u64,
    pub instr_ptr: u64,
    pub localsplus: u64,
    pub owner: u64,
    pub stackpointer: u64,
    pub tlbc_index: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__code_object {
    pub size: u64,
    pub filename: u64,
    pub name: u64,
    pub qualname: u64,
    pub linetable: u64,
    pub firstlineno: u64,
    pub argcount: u64,
    pub localsplusnames: u64,
    pub localspluskinds: u64,
    pub co_code_adaptive: u64,
    pub co_tlbc: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__pyobject {
    pub size: u64,
    pub ob_type: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__type_object {
    pub size: u64,
    pub tp_name: u64,
    pub tp_repr: u64,
    pub tp_flags: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__tuple_object {
    pub size: u64,
    pub ob_item: u64,
    pub ob_size: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__list_object {
    pub size: u64,
    pub ob_item: u64,
    pub ob_size: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__set_object {
    pub size: u64,
    pub used: u64,
    pub table: u64,
    pub mask: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__dict_object {
    pub size: u64,
    pub ma_keys: u64,
    pub ma_values: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__float_object {
    pub size: u64,
    pub ob_fval: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__long_object {
    pub size: u64,
    pub lv_tag: u64,
    pub ob_digit: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__bytes_object {
    pub size: u64,
    pub ob_size: u64,
    pub ob_sval: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__unicode_object {
    pub size: u64,
    pub state: u64,
    pub length: u64,
    pub asciiobject_size: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__gc {
    pub size: u64,
    pub collecting: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__gen_object {
    pub size: u64,
    pub gi_name: u64,
    pub gi_iframe: u64,
    pub gi_frame_state: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__llist_node {
    pub next: u64,
    pub prev: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_DebugOffsets__debugger_support {
    pub eval_breaker: u64,
    pub remote_debugger_support: u64,
    pub remote_debugging_enabled: u64,
    pub debugger_pending_call: u64,
    pub debugger_script_path: u64,
    pub debugger_script_path_size: u64,
}

#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_AsyncioModuleDebugOffsets {
    pub asyncio_task_object: _Py_AsyncioModuleDebugOffsets__asyncio_task_object,
    pub asyncio_interpreter_state: _Py_AsyncioModuleDebugOffsets__asyncio_interpreter_state,
    pub asyncio_thread_state: _Py_AsyncioModuleDebugOffsets__asyncio_thread_state,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_AsyncioModuleDebugOffsets__asyncio_task_object {
    pub size: u64,
    pub task_name: u64,
    pub task_awaited_by: u64,
    pub task_is_task: u64,
    pub task_awaited_by_is_set: u64,
    pub task_coro: u64,
    pub task_node: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_AsyncioModuleDebugOffsets__asyncio_interpreter_state {
    pub size: u64,
    pub asyncio_tasks_head: u64,
}
#[repr(C)]
#[derive(Debug, Copy, Clone)]
pub struct _Py_AsyncioModuleDebugOffsets__asyncio_thread_state {
    pub size: u64,
    pub asyncio_running_loop: u64,
    pub asyncio_running_task: u64,
    pub asyncio_tasks_head: u64,
}
pub type Py_AsyncioModuleDebugOffsets = _Py_AsyncioModuleDebugOffsets;
```

## File: `kit/python_unwind/Cargo.toml`
```
[package]
name = "python_unwind"
version = "0.1.0"
edition = "2024"
publish = false

[features]
default = []
debug-print = ["notlibc/debug-print"]

[dependencies]
kindasafe = { path = "../kindasafe" }
notlibc = { path = "../notlibc" }
python_offsets_types = { path = "../python_offsets_types" }
```

## File: `kit/python_unwind/src/lib.rs`
```rust
#![no_std]

use python_offsets_types::py314;

/// Minimum owner value to skip during unwinding.
///
/// In Python 3.14 the `owner` enum is:
///   0 = FRAME_OWNED_BY_THREAD       — include
///   1 = FRAME_OWNED_BY_GENERATOR    — include
///   2 = FRAME_OWNED_BY_FRAME_OBJECT — include
///   3 = FRAME_OWNED_BY_INTERPRETER  — skip
///   4 = FRAME_OWNED_BY_CSTACK       — skip
///
/// We skip any owner >= 3.
pub const FRAME_SKIP_OWNER_MIN: u64 = 3;

/// Maximum number of frames to collect in a single unwind.
pub const MAX_DEPTH: usize = 128;

/// Expected type-object addresses resolved at init time.
///
/// Used during unwinding to verify that object pointers have the correct
/// `ob_type`. A value of `0` means "unknown / skip check".
#[derive(Copy, Clone)]
pub struct TypeAddrs {
    pub code_type: u64,
}

/// A raw Python frame captured during unwinding.
///
/// Contains the `PyCodeObject*` address and the raw `instr_ptr` value.
/// The instruction offset from `co_code_adaptive` is computed later during
/// symbolication — storing the raw pointer avoids an extra `kindasafe::u64()`
/// read per frame in the signal handler.
#[repr(C)]
#[derive(Copy, Clone)]
pub struct RawFrame {
    pub code_object: u64,
    pub instr_offset: u64,
}

/// Walk the Python interpreter frame chain starting from `tstate` and collect
/// raw `(code_object, instr_ptr)` tuples into `buf`.
///
/// Returns the number of frames written to `buf`.
///
/// All memory reads use `kindasafe::u64()` for signal-safety. On any read
/// failure the walk stops and returns whatever frames were collected so far.
///
/// Frames with `owner >= FRAME_SKIP_OWNER_MIN` (interpreter shims, C-stack
/// entries) are skipped. Cycle detection and a max depth of `min(buf.len(), MAX_DEPTH)`
/// prevent infinite loops from corrupted pointers.
pub fn unwind(
    tstate: u64,
    offsets: &py314::_Py_DebugOffsets,
    type_addrs: &TypeAddrs,
    buf: &mut [RawFrame],
) -> usize {
    let max = if buf.len() < MAX_DEPTH {
        buf.len()
    } else {
        MAX_DEPTH
    };

    let frame_ptr = match kindasafe::u64(tstate + offsets.thread_state.current_frame) {
        Ok(v) => v,
        Err(_) => return 0,
    };
    if frame_ptr == 0 {
        return 0;
    }

    let mut frame_ptr = frame_ptr;
    let mut prev_frame: u64 = 0;
    let mut depth: usize = 0;

    while frame_ptr != 0 && frame_ptr != prev_frame && depth < max {
        let owner = match kindasafe::u64(frame_ptr + offsets.interpreter_frame.owner) {
            Ok(v) => v & 0xFF,
            Err(_) => break,
        };

        if owner >= FRAME_SKIP_OWNER_MIN {
            prev_frame = frame_ptr;
            frame_ptr = match kindasafe::u64(frame_ptr + offsets.interpreter_frame.previous) {
                Ok(v) => v,
                Err(_) => break,
            };
            continue;
        }

        let code_obj = match kindasafe::u64(frame_ptr + offsets.interpreter_frame.executable) {
            Ok(v) => v,
            Err(_) => break,
        };
        if code_obj == 0 {
            break;
        }

        if type_addrs.code_type != 0
            && let Ok(ob_type) = kindasafe::u64(code_obj + offsets.pyobject.ob_type)
            && ob_type != type_addrs.code_type
        {
            notlibc::debug::writes(
                "!!! ERROR python_unwind: ob_type mismatch for PyCodeObject at 0x",
            );
            notlibc::debug::write_hex(code_obj as usize);
            notlibc::debug::writes(" expected PyCode_Type=0x");
            notlibc::debug::write_hex(type_addrs.code_type as usize);
            notlibc::debug::writes(" got ob_type=0x");
            notlibc::debug::write_hex(ob_type as usize);
            notlibc::debug::puts("");
        }

        let instr_ptr = match kindasafe::u64(frame_ptr + offsets.interpreter_frame.instr_ptr) {
            Ok(v) => v,
            Err(_) => break,
        };

        buf[depth] = RawFrame {
            code_object: code_obj,
            instr_offset: instr_ptr,
        };

        // notlibc::debug::writes("  handler: [");
        // notlibc::debug::write_hex(depth);
        // notlibc::debug::writes("] code=0x");
        // notlibc::debug::write_hex(code_obj as usize);
        // notlibc::debug::writes(" instr=0x");
        // notlibc::debug::write_hex(instr_ptr as usize);
        // notlibc::debug::writes(" owner=");
        // notlibc::debug::write_hex(owner as usize);
        // notlibc::debug::puts("");

        depth += 1;

        prev_frame = frame_ptr;
        frame_ptr = match kindasafe::u64(frame_ptr + offsets.interpreter_frame.previous) {
            Ok(v) => v,
            Err(_) => break,
        };
    }

    // notlibc::debug::writes("handler: depth=");
    // notlibc::debug::write_hex(depth);
    // notlibc::debug::puts("");

    depth
}
```

## File: `kit/sig_ring/Cargo.toml`
```
[package]
name = "sig_ring"
version = "0.1.0"
edition = "2024"
publish = false

[features]
default = []
ring-512k = []
ring-1m = []

[dependencies]
bbqueue = "0.5"
python_unwind = { path = "../python_unwind" }
```

## File: `kit/sig_ring/src/lib.rs`
```rust
#![no_std]

use python_unwind::RawFrame;

/// Default size of each per-shard bbqueue buffer in bytes (256 KiB).
/// Can be overridden at compile time via the `ring-512k` or `ring-1m` features.
#[cfg(feature = "ring-1m")]
pub const RING_SIZE: usize = 1024 * 1024;
#[cfg(all(feature = "ring-512k", not(feature = "ring-1m")))]
pub const RING_SIZE: usize = 512 * 1024;
#[cfg(not(any(feature = "ring-512k", feature = "ring-1m")))]
pub const RING_SIZE: usize = 256 * 1024;

/// Default notification interval: notify the reader thread every N sample writes.
/// Can be overridden at runtime via the `notify_interval` field in profiler state.
pub const DEFAULT_NOTIFY_INTERVAL: u32 = 32;

/// Size of the record header: thread_id (u32) + depth (u32).
const HEADER_SIZE: usize = 8;

/// Size of one `RawFrame` in bytes (code_object: u64 + instr_offset: u64).
const FRAME_SIZE: usize = core::mem::size_of::<RawFrame>();

/// Compute the byte length of a record with `depth` frames.
fn record_len(depth: usize) -> usize {
    HEADER_SIZE + depth * FRAME_SIZE
}

/// Write a stack trace record into a framed bbqueue producer.
///
/// Record layout: `[thread_id: u32][depth: u32][frames[0..depth]]`
///
/// Called from the signal handler inside a shard lock.
/// Returns `true` on success, `false` if the queue is full.
///
/// Generic over const `N` to support different ring buffer sizes.
pub fn write<const N: usize>(
    producer: &mut bbqueue::framed::FrameProducer<'static, N>,
    tid: u32,
    frames: &[RawFrame],
    depth: usize,
) -> bool {
    let len = record_len(depth);

    let mut grant = match producer.grant(len) {
        Ok(g) => g,
        Err(_) => return false,
    };

    // Write header.
    grant[0..4].copy_from_slice(&tid.to_ne_bytes());
    grant[4..8].copy_from_slice(&(depth as u32).to_ne_bytes());

    // Write frames as raw bytes.
    // SAFETY: RawFrame is #[repr(C)], Copy, contains only u64 fields.
    // We reinterpret the &[RawFrame] as &[u8] for the copy.
    let frames_src = &frames[..depth];
    let src_bytes = unsafe {
        core::slice::from_raw_parts(frames_src.as_ptr() as *const u8, depth * FRAME_SIZE)
    };
    grant[HEADER_SIZE..HEADER_SIZE + src_bytes.len()].copy_from_slice(src_bytes);

    grant.commit(len);
    true
}

/// Parsed view of a record from a bbqueue read grant.
///
/// Holds a reference to the raw grant bytes. Frames are read via
/// [`frame()`](RecordView::frame) which handles potentially unaligned data.
pub struct RecordView<'a> {
    pub tid: u32,
    pub depth: u32,
    buf: &'a [u8],
}

impl<'a> RecordView<'a> {
    /// Read the frame at index `i`.
    ///
    /// Uses `read_unaligned` because bbqueue frame grants are not guaranteed
    /// to be 8-byte aligned.
    pub fn frame(&self, i: usize) -> RawFrame {
        let offset = HEADER_SIZE + i * FRAME_SIZE;
        let code_ptr = self.buf[offset..].as_ptr() as *const u64;
        let instr_ptr = self.buf[offset + 8..].as_ptr() as *const u64;
        // SAFETY: bounds checked by parse_record, and we use read_unaligned.
        unsafe {
            RawFrame {
                code_object: core::ptr::read_unaligned(code_ptr),
                instr_offset: core::ptr::read_unaligned(instr_ptr),
            }
        }
    }
}

/// Parse a raw byte slice (from a `FrameGrantR`) into a [`RecordView`].
///
/// Returns `None` if the buffer is too small or the depth field is
/// inconsistent with the buffer length.
pub fn parse_record(buf: &[u8]) -> Option<RecordView<'_>> {
    if buf.len() < HEADER_SIZE {
        return None;
    }

    let tid = u32::from_ne_bytes([buf[0], buf[1], buf[2], buf[3]]);
    let depth = u32::from_ne_bytes([buf[4], buf[5], buf[6], buf[7]]);

    let expected_len = record_len(depth as usize);
    if buf.len() < expected_len {
        return None;
    }

    Some(RecordView { tid, depth, buf })
}
```

## File: `kit/sighandler/Cargo.toml`
```
[package]
name = "sighandler"
version = "0.1.0"
edition = "2024"
publish = false

[dependencies]
libc = { version = "0.2.182" }

[dev-dependencies]
libc = { version = "=0.2.182" }
```

## File: `kit/sighandler/src/lib.rs`
```rust
use core::ffi::{c_int, c_void};

pub type HandlerFn = extern "C" fn(c_int, *mut libc::siginfo_t, *mut c_void);

#[derive(Debug, PartialEq)]
pub enum Error {
    SigactionFailed,
    SetitimerFailed,
}

/// Install `handler` as the SIGPROF signal handler and start a repeating
/// 10 ms ITIMER_PROF timer (100 Hz).
///
/// # Safety
/// The caller must ensure `handler` is safe to invoke from a signal context.
pub fn start(handler: HandlerFn) -> Result<(), Error> {
    unsafe {
        register_sigaction(handler)?;
        start_timer()?;
    }
    Ok(())
}

/// Install `handler` as the SIGPROF signal handler without starting the timer.
///
/// # Safety
/// The caller must ensure `handler` is safe to invoke from a signal context.
pub unsafe fn register_sigaction(handler: HandlerFn) -> Result<(), Error> {
    unsafe {
        let mut new_action: libc::sigaction = core::mem::zeroed();
        new_action.sa_sigaction = handler as usize;
        new_action.sa_flags = libc::SA_SIGINFO | libc::SA_RESTART;
        libc::sigemptyset(&mut new_action.sa_mask);
        libc::sigaddset(&mut new_action.sa_mask, libc::SIGPROF);
        // NOTE: Do NOT add SIGSEGV/SIGBUS to sa_mask here.
        // kindasafe relies on receiving SIGSEGV/SIGBUS during SIGPROF
        // to safely recover from bad memory reads. Blocking them
        // causes fatal crashes instead of graceful error returns.
        if libc::sigaction(libc::SIGPROF, &new_action, core::ptr::null_mut()) != 0 {
            return Err(Error::SigactionFailed);
        }
    }
    Ok(())
}

/// Start a repeating 10 ms ITIMER_PROF timer (100 Hz).
///
/// # Safety
///
/// Must be called after the SIGPROF handler has been installed via
/// `register_sigaction`. Calling this without a handler installed will
/// cause the default signal disposition (process termination).
pub unsafe fn start_timer() -> Result<(), Error> {
    unsafe {
        let interval = libc::itimerval {
            it_interval: libc::timeval {
                tv_sec: 0,
                tv_usec: 10_000,
            },
            it_value: libc::timeval {
                tv_sec: 0,
                tv_usec: 10_000,
            },
        };
        if libc::setitimer(libc::ITIMER_PROF, &interval, core::ptr::null_mut()) != 0 {
            return Err(Error::SetitimerFailed);
        }
    }
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
    use core::sync::atomic::{AtomicI32, Ordering};

    static LAST_SIG: AtomicI32 = AtomicI32::new(0);

    extern "C" fn test_handler(sig: c_int, _info: *mut libc::siginfo_t, _ctx: *mut c_void) {
        LAST_SIG.store(sig, Ordering::Relaxed);
    }

    #[test]
    fn start_returns_ok() {
        let result = start(test_handler);
        // Clean up: disarm the timer immediately.
        unsafe {
            let zero = libc::itimerval {
                it_interval: libc::timeval {
                    tv_sec: 0,
                    tv_usec: 0,
                },
                it_value: libc::timeval {
                    tv_sec: 0,
                    tv_usec: 0,
                },
            };
            libc::setitimer(libc::ITIMER_PROF, &zero, core::ptr::null_mut());
        }
        assert_eq!(result, Ok(()));
    }
}
```

## File: `kit/sighandler/tests/integration.rs`
```rust
use core::ffi::{c_int, c_void};
use core::sync::atomic::{AtomicU32, Ordering};
use std::time::{Duration, Instant};

static COUNTER: AtomicU32 = AtomicU32::new(0);

extern "C" fn counting_handler(_sig: c_int, _info: *mut libc::siginfo_t, _ctx: *mut c_void) {
    COUNTER.fetch_add(1, Ordering::Relaxed);
}

/// Burn CPU for at least `dur` so ITIMER_PROF (which counts CPU time) fires.
fn burn_cpu(dur: Duration) {
    let start = Instant::now();
    let mut x: u64 = 1;
    while start.elapsed() < dur {
        x = x
            .wrapping_mul(6364136223846793005)
            .wrapping_add(1442695040888963407);
    }
    // Prevent the loop from being optimized away.
    let _ = x;
}

#[test]
fn sigprof_fires_repeatedly() {
    COUNTER.store(0, Ordering::Relaxed);

    sighandler::start(counting_handler).expect("start failed");

    // Burn ~200 ms of CPU time; at 100 Hz we expect ~20 signals.
    burn_cpu(Duration::from_millis(200));

    // Disarm the timer before asserting so stray signals don't interfere.
    unsafe {
        let zero = libc::itimerval {
            it_interval: libc::timeval {
                tv_sec: 0,
                tv_usec: 0,
            },
            it_value: libc::timeval {
                tv_sec: 0,
                tv_usec: 0,
            },
        };
        libc::setitimer(libc::ITIMER_PROF, &zero, core::ptr::null_mut());
    }

    let count = COUNTER.load(Ordering::Relaxed);
    assert!(
        count > 0,
        "expected SIGPROF to fire at least once, got {count}"
    );
}
```

## File: `pyroscope_ffi/python/.gitignore`
```
*.pyc
*.swp

# Packages
*.egg
.eggs/
!/tests/**/*.egg
*/*.egg-info
*.egg-info
/dist/*
/wheelhouse/*
pip-wheel-metadata
build
_build
.cache
*.so

# Installer logs
pip-log.txt

# Unit test / coverage reports
.coverage
.tox
.pytest_cache

# Rust Library
**/*.rs.bk
```

## File: `pyroscope_ffi/python/python/pyroscope/__init__.py`
```python
import warnings
import logging
import json
from enum import Enum

from ._native import lib

from contextlib import contextmanager

LOGGER = logging.getLogger(__name__)

class LineNo(Enum):
    LastInstruction = lib.LastInstruction
    First = lib.First
    NoLine = lib.NoLine

def configure(
        app_name=None,
        application_name=None,
        server_address="http://localhost:4040",
        basic_auth_username="",
        basic_auth_password="",
        enable_logging=False,
        sample_rate=100,
        oncpu=True,
        native=None,
        gil_only=True,
        report_pid=False,
        report_thread_id=False,
        report_thread_name=False,
        tags=None,
        tenant_id="",
        http_headers=None,
        line_no=LineNo.LastInstruction,
):

    if app_name is not None:
        warnings.warn("app_name is deprecated, use application_name", DeprecationWarning)
        application_name = app_name

    if native is not None:
        warnings.warn("native is deprecated and not supported", DeprecationWarning)

    LOGGER.disabled = not enable_logging
    if enable_logging:
        log_level = LOGGER.getEffectiveLevel()
        lib.initialize_logging(log_level)

    lib.initialize_agent(
        application_name.encode("UTF-8"),
        server_address.encode("UTF-8"),
        basic_auth_username.encode("UTF-8"),
        basic_auth_password.encode("UTF-8"),
        sample_rate,
        oncpu,
        gil_only,
        report_pid,
        report_thread_id,
        report_thread_name,
        tags_to_string(tags).encode("UTF-8"),
        (tenant_id or "").encode("UTF-8"),
        http_headers_to_json(http_headers).encode("UTF-8"),
        line_no.value
    )

def shutdown():
    drop = lib.drop_agent()

    if drop:
        LOGGER.info("Pyroscope Agent successfully shutdown")
    else:
        LOGGER.warning("Pyroscope Agent shutdown failed")

def add_thread_tag(key, value):
    lib.add_thread_tag(key.encode("UTF-8"), value.encode("UTF-8"))

def remove_thread_tag(key, value):
    lib.remove_thread_tag(key.encode("UTF-8"), value.encode("UTF-8"))

def tags_to_string(tags):
    if tags is None:
        return ""
    return ",".join(["{}={}".format(key, value) for key, value in tags.items()])

def http_headers_to_json(headers):
    if headers is None:
        return "{}"
    return json.dumps(headers)

@contextmanager
def tag_wrapper(tags):
    for key, value in tags.items():
        lib.add_thread_tag(key.encode("UTF-8"), value.encode("UTF-8"))
    try:
        yield
    finally:
        for key, value in tags.items():
            lib.remove_thread_tag(key.encode("UTF-8"), value.encode("UTF-8"))

def stop():
    warnings.warn("deprecated, no longer applicable", DeprecationWarning)
def change_name(name):
    warnings.warn("deprecated, no longer applicable", DeprecationWarning)
def tag(tags):
    warnings.warn("deprecated, use tag_wrapper function", DeprecationWarning)
def remove_tags(*keys):
    warnings.warn("deprecated, no longer applicable", DeprecationWarning)
def build_summary():
    warnings.warn("deprecated, no longer applicable", DeprecationWarning)
def test_logger():
    warnings.warn("deprecated, no longer applicable", DeprecationWarning)
```

## File: `pyroscope_ffi/python/python/pyroscope/_cffi.py`
```python
# auto-generated file
import _cffi_backend

ffi = _cffi_backend.FFI('pyroscope',
    _version = 0x2601,
    _types = b'\x00\x00\x0A\x0D\x00\x00\x19\x03\x00\x00\x01\x11\x00\x00\x00\x0F\x00\x00\x0A\x0D\x00\x00\x01\x11\x00\x00\x01\x11\x00\x00\x01\x11\x00\x00\x01\x11\x00\x00\x16\x01\x00\x00\x01\x01\x00\x00\x01\x01\x00\x00\x01\x01\x00\x00\x01\x01\x00\x00\x01\x01\x00\x00\x01\x11\x00\x00\x01\x11\x00\x00\x01\x11\x00\x00\x00\x0B\x00\x00\x00\x0F\x00\x00\x0A\x0D\x00\x00\x16\x01\x00\x00\x00\x0F\x00\x00\x0A\x0D\x00\x00\x00\x0F\x00\x00\x02\x01',
    _globals = (b'\xFF\xFF\xFF\x0BFirst',1,b'\xFF\xFF\xFF\x0BLastInstruction',0,b'\xFF\xFF\xFF\x0BNoLine',2,b'\x00\x00\x00\x23add_thread_tag',0,b'\x00\x00\x17\x23drop_agent',0,b'\x00\x00\x04\x23initialize_agent',0,b'\x00\x00\x14\x23initialize_logging',0,b'\x00\x00\x00\x23remove_thread_tag',0),
    _enums = (b'\x00\x00\x00\x12\x00\x00\x00\x16$LineNo\x00LastInstruction,First,NoLine',),
    _typenames = (b'\x00\x00\x00\x12LineNo',),
)
```

## File: `pyroscope_ffi/python/python/pyroscope/_native.py`
```python

__all__ = ['lib', 'ffi']

import os
from ._cffi import ffi

lib = ffi.dlopen(os.path.join(os.path.dirname(__file__), '../pyroscope_python_extension', 'pyroscope_python_extension.abi3.so'))
del os
```

## File: `pyroscope_ffi/python/python/pyroscope_io/__init__.py`
```python
# this is left here for compatibility with previous versions where the package was called pyroscope_io
from pyroscope import *
```

## File: `pyroscope_ffi/python/rust/Cargo.toml`
```
[package]
name = "pyroscope_python_extension" # This is used as package name for so placement
# todo figure out how to put this into pyroscope package without renaming the main crate
version = "1.0.4"
authors = [
    "Tolyan Korniltsev <anatoly.korniltsev@grafana.com>"
]
edition = "2021"
rust-version = "1.66"

[lib]
crate-type = ["cdylib"]
name = "pyroscope_python_extension" # this is the name of the shared rust, e.g. pyroscope_python_extension.abi3.so

[dependencies]
pyroscope = { path = "../../../", default-features = false, features = ["native-tls"] }
py-spy = { workspace = true }
pretty_env_logger = { workspace = true }
log = { workspace = true }
libc = { workspace = true }
pysignalprof = { path = "../../../kit/pysignalprof", version = "0.1.0" }

[features]
default = ["rustls-tls"]
rustls-tls = ["pyroscope/rustls-tls"]
native-tls-vendored = ["pyroscope/native-tls-vendored"]
```

## File: `pyroscope_ffi/python/rust/cbindgen.toml`
```
language = "C"
documentation_style = "C"

style = "type"

include_guard = "PYROSCOPE_FFI_H_"
include_version = false

header = "/* Licensed under Apache-2.0 */"
autogen_warning = "/* Warning, this file is autogenerated by cbindgen. Don't modify this manually. */"

braces = "SameLine"
tab_width = 2
line_length = 80


[parse]
parse_deps = false
include = ["LineNoFFI"]

[export]
include = ["LineNoFFI"]
```

## File: `pyroscope_ffi/python/rust/include/pyroscope_ffi.h`
```c
/* Licensed under Apache-2.0 */

#ifndef PYROSCOPE_FFI_H_
#define PYROSCOPE_FFI_H_

/* Warning, this file is autogenerated by cbindgen. Don't modify this manually. */

#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

typedef enum {
  LastInstruction = 0,
  First = 1,
  NoLine = 2,
} LineNo;

bool initialize_logging(uint32_t logging_level);

/*
 # Safety
 All pointer arguments must be valid, non-null, null-terminated C strings.
 */
bool initialize_agent(const char *application_name,
                      const char *server_address,
                      const char *basic_auth_username,
                      const char *basic_auth_password,
                      uint32_t sample_rate,
                      bool oncpu,
                      bool gil_only,
                      bool report_pid,
                      bool report_thread_id,
                      bool report_thread_name,
                      const char *tags,
                      const char *tenant_id,
                      const char *http_headers_json,
                      LineNo line_no);

bool drop_agent(void);

/*
 # Safety
 `key` and `value` must be valid, non-null, null-terminated C strings.
 */
bool add_thread_tag(const char *key, const char *value);

/*
 # Safety
 `key` and `value` must be valid, non-null, null-terminated C strings.
 */
bool remove_thread_tag(const char *key, const char *value);

#endif  /* PYROSCOPE_FFI_H_ */
```

## File: `pyroscope_ffi/python/rust/src/backend.rs`
```rust
use py_spy::sampler::Sampler;
use pyroscope::{
    backend::{
        Backend, BackendConfig, Report, ReportBatch, ReportData, StackBuffer, StackFrame,
        StackTrace, ThreadTag, ThreadTagsSet,
    },
    error::{PyroscopeError, Result},
};
use std::{
    ops::Deref,
    sync::{
        atomic::{AtomicBool, Ordering},
        Arc, Mutex,
    },
    thread::JoinHandle,
};

const LOG_TAG: &str = "Pyroscope::Pyspy";

#[derive(Default)]
pub struct Pyspy {
    buffer: Arc<Mutex<StackBuffer>>,
    config: py_spy::config::Config,
    backend_config: BackendConfig,
    sampler_thread: Option<JoinHandle<Result<()>>>,
    running: Arc<AtomicBool>,
    ruleset: Arc<Mutex<ThreadTagsSet>>,
}

impl std::fmt::Debug for Pyspy {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Pyspy Backend")
    }
}

impl Pyspy {
    pub fn new(config: py_spy::config::Config, backend_config: BackendConfig) -> Self {
        Pyspy {
            buffer: Arc::new(Mutex::new(StackBuffer::default())),
            config,
            backend_config,
            sampler_thread: None,
            running: Arc::new(AtomicBool::new(false)),
            ruleset: Arc::new(Mutex::new(ThreadTagsSet::default())),
        }
    }
}

impl Backend for Pyspy {
    fn add_tag(&self, rule: ThreadTag) -> Result<()> {
        self.ruleset.lock()?.add(rule)?;

        Ok(())
    }

    fn remove_tag(&self, rule: ThreadTag) -> Result<()> {
        self.ruleset.lock()?.remove(rule)?;

        Ok(())
    }

    fn initialize(&mut self) -> Result<()> {
        if self.config.pid.is_none() {
            return Err(PyroscopeError::new("Pyspy: No Process ID Specified"));
        }

        let running = Arc::clone(&self.running);
        running.store(true, Ordering::Relaxed);

        let buffer = self.buffer.clone();

        let config = self.config.clone();

        let ruleset = self.ruleset.clone();

        let backend_config = self.backend_config;

        self.sampler_thread = Some(std::thread::spawn(move || {
            let pid = config
                .pid
                .ok_or_else(|| PyroscopeError::new("Pyspy: PID is not set"))?;

            let sampler = Sampler::new(pid, &config)
                .map_err(|e| PyroscopeError::new(&format!("Pyspy: Sampler Error: {}", e)))?;

            let sampler_output = sampler.take_while(|_x| running.load(Ordering::Relaxed));

            for sample in sampler_output {
                for trace in sample.traces {
                    if !(config.include_idle || trace.active) {
                        continue;
                    }

                    if config.gil_only && !trace.owns_gil {
                        continue;
                    }

                    let own_trace: StackTrace =
                        Into::<StackTraceWrapper>::into((trace.clone(), &backend_config)).into();

                    let stacktrace = own_trace.add_tag_rules(&*ruleset.lock()?);

                    buffer.lock()?.record(stacktrace)?;
                }
            }

            Ok(())
        }));

        Ok(())
    }

    fn shutdown(self: Box<Self>) -> Result<()> {
        log::trace!(target: LOG_TAG, "Shutting down sampler thread");

        self.running.store(false, Ordering::Relaxed);

        self.sampler_thread
            .ok_or_else(|| PyroscopeError::new("Pyspy: Failed to unwrap Sampler Thread"))?
            .join()
            .unwrap_or_else(|_| Err(PyroscopeError::new("Pyspy: Failed to join sampler thread")))?;

        Ok(())
    }

    fn report(&mut self) -> Result<ReportBatch> {
        let report: StackBuffer = self.buffer.lock()?.deref().to_owned();
        let reports: Vec<Report> = report.into();

        self.buffer.lock()?.clear();

        Ok(ReportBatch {
            profile_type: "process_cpu".into(),
            data: ReportData::Reports(reports),
        })
    }
}

/// Wrapper for StackFrame. This is needed because both StackFrame and
/// py_spy::Frame are not defined in the same module.
struct StackFrameWrapper(StackFrame);

impl From<StackFrameWrapper> for StackFrame {
    fn from(stack_frame: StackFrameWrapper) -> Self {
        stack_frame.0
    }
}

impl From<py_spy::Frame> for StackFrameWrapper {
    fn from(frame: py_spy::Frame) -> Self {
        // Format name as "module.function" when module is available,
        // otherwise just use the function name.
        let formatted_name = match &frame.module {
            Some(module) => format!("{}.{}", module, frame.name),
            None => frame.name.clone(),
        };

        StackFrameWrapper(StackFrame {
            module: frame.module.clone(),
            name: Some(formatted_name),
            filename: Some(frame.filename.clone()),
            relative_path: None,
            absolute_path: Some(frame.filename.clone()),
            line: Some(frame.line as u32),
        })
    }
}

/// Wrapper for StackTrace. This is needed because both StackTrace and
/// py_spy::StackTrace are not defined in the same module.
struct StackTraceWrapper(StackTrace);

impl From<StackTraceWrapper> for StackTrace {
    fn from(stack_trace: StackTraceWrapper) -> Self {
        stack_trace.0
    }
}

impl From<(py_spy::StackTrace, &BackendConfig)> for StackTraceWrapper {
    fn from(arg: (py_spy::StackTrace, &BackendConfig)) -> Self {
        let (stack_trace, config) = arg;
        // https://github.com/python/cpython/blob/main/Python/thread_pthread.h#L304
        let thread_id = stack_trace.thread_id as libc::pthread_t;
        let stacktrace = StackTrace::new(
            config,
            Some(stack_trace.pid as u32),
            Some(thread_id.into()),
            stack_trace.thread_name.clone(),
            stack_trace
                .frames
                .iter()
                .map(|frame| Into::<StackFrameWrapper>::into(frame.clone()).into())
                .collect(),
        );
        StackTraceWrapper(stacktrace)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    fn create_test_frame(
        name: &str,
        filename: &str,
        module: Option<&str>,
        line: i32,
    ) -> py_spy::Frame {
        py_spy::Frame {
            name: name.to_string(),
            filename: filename.to_string(),
            module: module.map(|s| s.to_string()),
            short_filename: None,
            line,
            locals: None,
            is_entry: false,
            is_shim_entry: false,
        }
    }

    #[test]
    fn test_frame_name_with_module() {
        // When module is provided (e.g., native frames or class methods),
        // name should be "module.function"
        let frame = create_test_frame(
            "find_longest_match",
            "/usr/lib/python3.12/difflib.py",
            Some("SequenceMatcher"),
            42,
        );

        let wrapper: StackFrameWrapper = frame.into();
        let stack_frame: StackFrame = wrapper.into();

        assert_eq!(
            stack_frame.name,
            Some("SequenceMatcher.find_longest_match".to_string())
        );
        assert_eq!(stack_frame.module, Some("SequenceMatcher".to_string()));
        // filename preserves the full absolute path
        assert_eq!(
            stack_frame.filename,
            Some("/usr/lib/python3.12/difflib.py".to_string())
        );
        assert_eq!(stack_frame.line, Some(42));
    }

    #[test]
    fn test_frame_name_without_module() {
        // When module is None, name should just be the function name
        let frame = create_test_frame("my_function", "/home/user/app/main.py", None, 10);

        let wrapper: StackFrameWrapper = frame.into();
        let stack_frame: StackFrame = wrapper.into();

        assert_eq!(stack_frame.name, Some("my_function".to_string()));
        assert_eq!(stack_frame.module, None);
        // filename preserves the full absolute path
        assert_eq!(
            stack_frame.filename,
            Some("/home/user/app/main.py".to_string())
        );
        assert_eq!(stack_frame.line, Some(10));
    }

    #[test]
    fn test_frame_absolute_path_preserved() {
        // absolute_path should always contain the full path
        let frame = create_test_frame("test_func", "/path/to/file.py", None, 1);

        let wrapper: StackFrameWrapper = frame.into();
        let stack_frame: StackFrame = wrapper.into();

        assert_eq!(
            stack_frame.absolute_path,
            Some("/path/to/file.py".to_string())
        );
        assert_eq!(stack_frame.filename, Some("/path/to/file.py".to_string()));
        assert_eq!(stack_frame.relative_path, None);
    }

    #[test]
    fn test_name_never_contains_path_separator() {
        // The function name field should NEVER contain path separators
        // This would indicate the filename is leaking into the name
        let test_cases = vec![
            ("func1", "/a/b/c.py", None),
            ("func2", "/very/long/path/to/module.py", Some("MyClass")),
            ("func3", "relative/path.py", None),
        ];

        for (func_name, filename, module) in test_cases {
            let frame = create_test_frame(func_name, filename, module, 1);
            let wrapper: StackFrameWrapper = frame.into();
            let stack_frame: StackFrame = wrapper.into();

            let name = stack_frame.name.unwrap();
            assert!(
                !name.contains('/'),
                "Function name '{}' should not contain '/' path separator! Input: func={}, file={}, module={:?}",
                name, func_name, filename, module
            );
        }
    }
}
```

## File: `pyroscope_ffi/python/rust/src/lib.rs`
```rust
mod backend;

use crate::backend::Pyspy;
use pyroscope::backend::{BackendConfig, BackendImpl, Tag};
use pyroscope::pyroscope::PyroscopeAgentBuilder;
use std::ffi::CStr;
use std::os::raw::c_char;
use std::sync::atomic::{AtomicBool, Ordering};

const LOG_TAG: &str = "Pyroscope::pyspy::ffi";

/// Tracks whether pysignalprof is the active backend (set once during init).
static USING_PYSIGNALPROF: AtomicBool = AtomicBool::new(false);
const PYSPY_NAME: &str = "pyspy";
const PYSPY_VERSION: &str = env!("CARGO_PKG_VERSION");

#[no_mangle]
pub extern "C" fn initialize_logging(logging_level: u32) -> bool {
    // Force rustc to display the log messages in the console.
    match logging_level {
        50 => {
            unsafe { std::env::set_var("RUST_LOG", "off") };
        }
        40 => {
            unsafe { std::env::set_var("RUST_LOG", "error") };
        }
        30 => {
            unsafe { std::env::set_var("RUST_LOG", "warn") };
        }
        20 => {
            unsafe { std::env::set_var("RUST_LOG", "info") };
        }
        10 => {
            unsafe { std::env::set_var("RUST_LOG", "debug") };
        }
        _ => {
            unsafe { std::env::set_var("RUST_LOG", "debug") };
        }
    }

    // Initialize the logger.
    pretty_env_logger::init_timed();
    true
}

#[no_mangle]
/// # Safety
/// All pointer arguments must be valid, non-null, null-terminated C strings.
pub unsafe extern "C" fn initialize_agent(
    application_name: *const c_char,
    server_address: *const c_char,
    basic_auth_username: *const c_char,
    basic_auth_password: *const c_char,
    sample_rate: u32,
    oncpu: bool,
    gil_only: bool,
    report_pid: bool,
    report_thread_id: bool,
    report_thread_name: bool,
    tags: *const c_char,
    tenant_id: *const c_char,
    http_headers_json: *const c_char,
    line_no: LineNo,
) -> bool {
    let application_name = unsafe { CStr::from_ptr(application_name) }
        .to_str()
        .unwrap()
        .to_string();

    let server_address = unsafe { CStr::from_ptr(server_address) }
        .to_str()
        .unwrap()
        .to_string();

    // When PYROSCOPE_PYSIGNALPROF=true, use the new signal-based profiler
    // instead of py-spy. Tags, shutdown, and other unsupported features become no-ops.
    // Only available on x86_64 Linux; silently ignored on other platforms.
    #[cfg(all(target_arch = "x86_64", target_os = "linux"))]
    if std::env::var("PYROSCOPE_PYSIGNALPROF").unwrap_or_default() == "true" {
        USING_PYSIGNALPROF.store(true, Ordering::Release);
        let server_url = if server_address.is_empty() {
            None
        } else {
            Some(server_address)
        };
        let log_enabled = std::env::var("RUST_LOG")
            .map(|v| v != "off")
            .unwrap_or(false);
        let tags_string = unsafe { CStr::from_ptr(tags) }.to_str().unwrap_or("");
        let tags: Vec<(String, String)> = string_to_tags(tags_string)
            .into_iter()
            .map(|(k, v)| (k.to_owned(), v.to_owned()))
            .collect();
        return pysignalprof::start(application_name, server_url, 0, log_enabled, tags).is_ok();
    }

    let basic_auth_username = unsafe { CStr::from_ptr(basic_auth_username) }
        .to_str()
        .unwrap()
        .to_string();

    let basic_auth_password = unsafe { CStr::from_ptr(basic_auth_password) }
        .to_str()
        .unwrap()
        .to_string();

    // tags
    let tags_string = unsafe { CStr::from_ptr(tags) }
        .to_str()
        .unwrap()
        .to_string();

    let tenant_id = unsafe { CStr::from_ptr(tenant_id) }
        .to_str()
        .unwrap()
        .to_string();

    let http_headers_json = unsafe { CStr::from_ptr(http_headers_json) }
        .to_str()
        .unwrap()
        .to_string();

    let pid = std::process::id();

    let backend_config = BackendConfig {
        report_thread_id,
        report_thread_name,
        report_pid,
    };

    let pid = pid.try_into().unwrap();

    let config = py_spy::Config {
        blocking: py_spy::config::LockingStrategy::NonBlocking,
        native: false,
        pid: Some(pid),
        sampling_rate: sample_rate.into(),
        include_idle: !oncpu,
        include_thread_ids: true,
        subprocesses: false,
        gil_only,
        lineno: line_no.into(),
        duration: py_spy::config::RecordDuration::Unlimited,
        ..py_spy::Config::default()
    };

    let tags_ref = tags_string.as_str();
    let tags = string_to_tags(tags_ref);

    let pyspy = BackendImpl::new(Box::new(Pyspy::new(config, backend_config)));

    let mut agent_builder = PyroscopeAgentBuilder::new(
        server_address,
        application_name,
        sample_rate,
        PYSPY_NAME,
        PYSPY_VERSION,
        pyspy,
    )
    .tags(tags);

    if !basic_auth_username.is_empty() && !basic_auth_password.is_empty() {
        agent_builder = agent_builder.basic_auth(basic_auth_username, basic_auth_password);
    }
    if !tenant_id.is_empty() {
        agent_builder = agent_builder.tenant_id(tenant_id);
    }

    let http_headers = pyroscope::pyroscope::parse_http_headers_json(http_headers_json);
    match http_headers {
        Ok(http_headers) => {
            agent_builder = agent_builder.http_headers(http_headers);
        }
        Err(e) => match e {
            pyroscope::PyroscopeError::Json(e) => {
                log::error!(target: LOG_TAG, "parse_http_headers_json error {}", e);
            }
            pyroscope::PyroscopeError::AdHoc(e) => {
                log::error!(target: LOG_TAG, "parse_http_headers_json {}", e);
            }
            _ => {}
        },
    }

    pyroscope::ffikit::run(agent_builder).is_ok()
}

#[no_mangle]
pub extern "C" fn drop_agent() -> bool {
    if USING_PYSIGNALPROF.load(Ordering::Acquire) {
        return true;
    }
    pyroscope::ffikit::send(pyroscope::ffikit::Signal::Kill).is_ok()
}

#[no_mangle]
/// # Safety
/// `key` and `value` must be valid, non-null, null-terminated C strings.
pub unsafe extern "C" fn add_thread_tag(key: *const c_char, value: *const c_char) -> bool {
    if USING_PYSIGNALPROF.load(Ordering::Acquire) {
        return true;
    }
    let key = unsafe { CStr::from_ptr(key) }.to_str().unwrap().to_owned();
    let value = unsafe { CStr::from_ptr(value) }
        .to_str()
        .unwrap()
        .to_owned();

    pyroscope::ffikit::send(pyroscope::ffikit::Signal::AddThreadTag(
        self_thread_id(),
        Tag { key, value },
    ))
    .is_ok()
}

#[no_mangle]
/// # Safety
/// `key` and `value` must be valid, non-null, null-terminated C strings.
pub unsafe extern "C" fn remove_thread_tag(key: *const c_char, value: *const c_char) -> bool {
    if USING_PYSIGNALPROF.load(Ordering::Acquire) {
        return true;
    }
    let key = unsafe { CStr::from_ptr(key) }.to_str().unwrap().to_owned();
    let value = unsafe { CStr::from_ptr(value) }
        .to_str()
        .unwrap()
        .to_owned();

    pyroscope::ffikit::send(pyroscope::ffikit::Signal::RemoveThreadTag(
        self_thread_id(),
        Tag { key, value },
    ))
    .is_ok()
}

fn string_to_tags(tags: &str) -> Vec<(&str, &str)> {
    let mut tags_vec = Vec::new();

    // check if string is empty
    if tags.is_empty() {
        return tags_vec;
    }

    for tag in tags.split(',') {
        let mut tag_split = tag.split('=');
        let key = tag_split.next().unwrap();
        let value = tag_split.next().unwrap();
        tags_vec.push((key, value));
    }

    tags_vec
}

#[repr(C)]
#[derive(Debug)]
pub enum LineNo {
    LastInstruction = 0,
    First = 1,
    NoLine = 2,
}

impl From<LineNo> for py_spy::config::LineNo {
    fn from(val: LineNo) -> Self {
        match val {
            LineNo::LastInstruction => py_spy::config::LineNo::LastInstruction,
            LineNo::First => py_spy::config::LineNo::First,
            LineNo::NoLine => py_spy::config::LineNo::NoLine,
        }
    }
}

pub fn self_thread_id() -> pyroscope::ThreadId {
    // https://github.com/python/cpython/blob/main/Python/thread_pthread.h#L304
    pyroscope::ThreadId::pthread_self()
}
```

## File: `pyroscope_ffi/python/scripts/tests/compile_ffi.py`
```python
import os
import re
import cffi
from cffi import recompiler as cffi_recompiler


_directive_re = re.compile(r'(?m)^\s*#.*?$')

_script_dir = os.path.dirname(os.path.abspath(__file__))
_python_ffi_dir = os.path.normpath(os.path.join(_script_dir, '..', '..'))

src = os.path.join(_python_ffi_dir, 'rust', 'include', 'pyroscope_ffi.h')
dst = os.path.join(_python_ffi_dir, 'python', 'pyroscope', '_cffi.py')
src = open(src, 'r').read()
src = _directive_re.sub('', src)

ffi = cffi.FFI()
ffi.cdef(src)
ffi.set_source('pyroscope', None)
res = cffi_recompiler.make_py_source(ffi, 'pyroscope', dst)
print(res)
```

## File: `pyroscope_ffi/python/scripts/tests/test.py`
```python
import hashlib
import os
import signal
import threading
import logging
import time
import traceback
import sys
import multiprocessing

import pyroscope
import threading

import uuid
from urllib.parse import quote

try:
    from urllib.request import Request, urlopen
except ImportError:
    from urllib2 import Request, urlopen


app_name = 'pyroscopers.python.test'
logger = logging.getLogger()

event = threading.Event()


def hash(string):
    string = string.encode()
    string = hashlib.sha256(string).hexdigest()

    return string


def multihash(string):
    while not event.is_set():
        time.sleep(0.2)
        e = time.time() + 0.1
        while time.time() < e:
            string = hash(string)
    return string


def multihash2(string):
    while not event.is_set():
        time.sleep(0.2)
        e = time.time() + 0.1
        while time.time() < e:
            string = hash(string)
    return string


def wait_render(canary):
    while True:
        time.sleep(2)
        query = f'process_cpu:cpu:nanoseconds:cpu:nanoseconds{{service_name="pyroscopers.python.test", canary="{canary}"}}'
        u = 'http://localhost:4040/pyroscope/render?from=now-1h&until=now&&query=' + quote(query)
        response = None
        try:
            logging.info('render %s', u)
            req = Request(u)
            response = urlopen(req)
            code = response.getcode()
            body = response.read()
            logging.info("render body %s", body.decode('utf-8'))
            if code == 200 and body != b'' and b'multihash' in body:
                print(f'good {canary}')
                return
        except Exception:
            if response is not None:
                response.close()
            traceback.print_exc()
            continue


def do_one_test(on_cpu, gil_only):
    logging.info("do_one_test on_cpu=%s gil_only=%s", on_cpu, gil_only)
    canary = uuid.uuid4().hex
    logging.info('canary %s', canary)
    pyroscope.configure(
        application_name=app_name,
        server_address="http://localhost:4040",
        enable_logging=True,
        oncpu=on_cpu,
        gil_only=gil_only,
        report_pid=True,
        report_thread_id=True,
        report_thread_name=True,

        tags={
            "oncpu": '{}'.format(on_cpu),
            "gil_only": '{}'.format(gil_only),
            "canary": canary,
        }
    )

    thread_1 = threading.Thread(target=multihash, args=('abc',))
    thread_2 = threading.Thread(target=multihash2, args=('abc',))
    thread_1.start()
    thread_2.start()

    def watchdog():
        logging.info('Watchdog expired. Test timeout. Exiting...')
        exit(7)

    alarm = threading.Timer(120, watchdog)
    alarm.start()

    wait_render(canary)

    alarm.cancel()

    pyroscope.shutdown()

    logging.info("done")

    event.set()
    thread_1.join()
    thread_2.join()


if __name__ == '__main__':
    do_multiprocessing = True
    logger.setLevel(logging.INFO)
    multiprocessing.log_to_stderr(logging.INFO)
    if do_multiprocessing:
        procs = []
        res = []
        for on_cpu in [True, False]:
            for gil_only in [True, False]:
                p = multiprocessing.Process(target=do_one_test, args=(on_cpu, gil_only))
                p.start()
                procs.append((p, "{} {}".format(on_cpu, gil_only)))
        for p in procs:
            p[0].join()
            res.append((p[0].exitcode, p[1]))
        for t in res:
            logging.info("%s", str(t))
        for t in res:
            if t[0] != 0:
                logging.info("test failed %s", str(t))
                exit(1)
    else:
        on_cpu = sys.argv[1] == "true"
        gil_only = sys.argv[2] == "true"
        do_one_test(on_cpu, gil_only)
```

## File: `pyroscope_ffi/ruby/.gitignore`
```
*.gem
.DS_Store
**/target
*.so*
*.bundle
/pkg
/doc
/coverage
/tmp
/vendor
/.bundle
.eggs
elflib/*/build
elflib/*/dist
elflib/*/wheelhouse
elflib/*/*egg-info
```

## File: `pyroscope_ffi/ruby/Gemfile`
```
source 'https://rubygems.org'

gemspec
```

## File: `pyroscope_ffi/ruby/Gemfile.lock`
```
PATH
  remote: .
  specs:
    pyroscope (1.0.1)
      ffi

GEM
  remote: https://rubygems.org/
  specs:
    ffi (1.17.3)
    ffi (1.17.3-x86_64-linux-gnu)
    rake (13.3.1)

PLATFORMS
  ruby
  x86_64-linux

DEPENDENCIES
  bundler
  pyroscope!
  rake (~> 13.0)

BUNDLED WITH
   2.5.3
```

## File: `pyroscope_ffi/ruby/LICENSE`
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

   Copyright 2022 Pyroscope

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

## File: `pyroscope_ffi/ruby/README.md`
```markdown
# Pyroscope Ruby Gem

**Pyroscope integration for Ruby**

[![license](https://img.shields.io/badge/license-Apache2.0-blue.svg)](LICENSE) 
![tests](https://github.com/pyroscope-io/pyroscope-rs/workflows/Tests/badge.svg)
![build](https://github.com/pyroscope-io/pyroscope-rs/workflows/Build/badge.svg)
[![Gem version](https://badge.fury.io/rb/pyroscope.svg)](https://badge.fury.io/rb/pyroscope)

---

### What is Pyroscope
[Pyroscope](https://github.com/pyroscope-io/pyroscope) is a tool that lets you continuously profile your applications to prevent and debug performance issues in your code. It consists of a low-overhead agent which sends data to the Pyroscope server which includes a custom-built storage engine. This allows for you to store and query any applications profiling data in an extremely efficient and cost effective way.


### Supported platforms

| Linux | macOS | Windows | Docker |
|:-----:|:-----:|:-------:|:------:|
|   ✅  |   ✅  |         |   ✅   |

### Profiling Ruby applications

Add the `pyroscope` gem to your Gemfile:

```bash
bundle add pyroscope
```

### Basic Configuration

Add the following code to your application. If you're using rails, put this into `config/initializers` directory. This code will initialize pyroscope profiler and start profiling:

```ruby
require 'pyroscope'

Pyroscope.configure do |config|
  config.application_name = "my.ruby.app" # replace this with some name for your application
  config.server_address   = "http://my-pyroscope-server:4040" # replace this with the address of your pyroscope server
end
```

### Tags

Pyroscope ruby integration provides a number of ways to tag profiling data. For example, you can provide tags when you're initializing the profiler:

```ruby
require 'pyroscope'

Pyroscope.configure do |config|
  config.application_name = "my.ruby.app"
  config.server_address   = "http://my-pyroscope-server:4040"

  config.tags = {
    "hostname" => ENV["HOSTNAME"],
  }
end
```

or you can dynamically tag certain parts of your code:

```ruby
Pyroscope.tag_wrapper({ "controller": "slow_controller_i_want_to_profile" }) do
  slow_code
end
```

### Example

Check out this [example ruby project in our repository](https://github.com/pyroscope-io/pyroscope/tree/main/examples/ruby) for examples of how you can use these features.
```

## File: `pyroscope_ffi/ruby/Rakefile`
```
# frozen_string_literal: true

require 'rubygems/package_task'
require_relative 'lib/pyroscope/version'

exec(*(["bundle", "exec", $PROGRAM_NAME] + ARGV)) if ENV['BUNDLE_GEMFILE'].nil?

begin
	Bundler.setup(:default, :development)
rescue Bundler::BundlerError => e
	$stderr.puts e.message
	$stderr.puts "Run `bundle install` to install missing gems"
	exit e.status_code
end

load File.expand_path('./ext/rbspy/Rakefile', __dir__)

task default: %w[hello]

task :hello do
  puts 'Hello!'
end


namespace :source do
  spec = Bundler.load_gemspec('pyroscope.gemspec')
  Gem::PackageTask.new(spec) do |pkg|
  end
end

namespace :x86_64_darwin do
  spec = Bundler.load_gemspec('pyroscope.gemspec')
  spec.platform = 'x86_64-darwin'
  spec.files += FileList['lib/rbspy/rbspy.*']
  spec.extensions = []

  Gem::PackageTask.new(spec) do |pkg|
  end
end

namespace :arm64_darwin do
  spec = Bundler.load_gemspec('pyroscope.gemspec')
  spec.platform = 'arm64-darwin'
  spec.files += FileList['lib/rbspy/rbspy.*']
  spec.extensions = []

  Gem::PackageTask.new(spec) do |pkg|
  end
end

namespace :x86_64_linux do
  spec = Bundler.load_gemspec('pyroscope.gemspec')
  spec.platform = 'x86_64-linux'
  spec.files += FileList['lib/rbspy/rbspy.*']
  spec.files += FileList['lib/rbspy.libs/*']
  spec.extensions = []

  Gem::PackageTask.new(spec) do |pkg|
  end
end

namespace :aarch64_linux do
  spec = Bundler.load_gemspec('pyroscope.gemspec')
  spec.platform = 'aarch64-linux'
  spec.files += FileList['lib/rbspy/rbspy.*']
  spec.files += FileList['lib/rbspy.libs/*']
  spec.extensions = []

  Gem::PackageTask.new(spec) do |pkg|
  end
end
```

## File: `pyroscope_ffi/ruby/pyroscope.gemspec`
```
# coding: utf-8
# frozen_string_literal: true

begin
  require File.expand_path(File.join(File.dirname(__FILE__), "lib/pyroscope/version"))
rescue LoadError
  puts "WARNING: Could not load Pyroscope::VERSION"
end

Gem::Specification.new do |s|
  s.name = 'pyroscope'
  s.version = Pyroscope::VERSION
  s.summary = 'Pyroscope'
  s.description = 'Pyroscope FFI Integration for Ruby'
  s.authors = ['Pyroscope Team']
  s.email = ['contact@pyroscope.io']
  s.homepage = 'https://pyroscope.io'
  s.license = 'Apache-2.0'
  s.metadata = {
    "homepage_uri" => "https://pyroscope.io",
    "bug_tracker_uri" => "https://github.com/pyroscope-io/pyroscope-rs/issues",
    "documentation_uri" => "https://pyroscope.io/docs/ruby/",
    "changelog_uri" => "https://github.com/pyroscope-io/pyroscope-rs/tree/main/pyroscope_ffi/ruby/CHANGELOG.md",
    "source_code_uri" => "https://github.com/pyroscope-io/pyroscope-rs/tree/main/pyroscope_ffi/ruby",
  }

  # Specify which files should be added to the gem when it is released.
  # The `git ls-files -z` loads the files in the RubyGem that have been added into git.
  #s.files = Dir.chdir(__dir__) do
    #`git ls-files -z`.split("\x0").reject do |f|
      #(f == __FILE__) || f.match(%r{\A(?:(?:bin|test|spec|features)/|\.(?:git|travis|circleci)|appveyor)})
    #end
  #end
#   s.files = `git ls-files -z`.split("\0").reject { |f| f =~ /^(\.|G|spec|Rakefile)/ }
  s.files = [
    "Gemfile",
    "Gemfile.lock",
    "LICENSE",
#     "Makefile",
    "README.md",
#     "Rakefile",
    "ext/rbspy/Cargo.toml",
    "ext/rbspy/Rakefile",
    "ext/rbspy/cbindgen.toml",
    "ext/rbspy/extconf.rb",
    "ext/rbspy/include/rbspy.h",
    "ext/rbspy/src/lib.rs",
    "lib/pyroscope.rb",
    "lib/pyroscope/version.rb",
    "pyroscope.gemspec",
#     "scripts/tests/test.rb",
  ]
  s.platform = Gem::Platform::RUBY

  s.required_ruby_version = ">= 1.9.3"

  s.extensions = ['ext/rbspy/extconf.rb']

  s.add_dependency 'ffi'

  s.add_development_dependency 'bundler'
  s.add_development_dependency 'rake', '~> 13.0'
end
```

## File: `pyroscope_ffi/ruby/ext/rbspy/Cargo.toml`
```
[package]
name = "ffiruby"
version = "1.0.1"
edition = "2021"
rust-version = "1.66"

[lib]
name = "rbspy"
crate-type = ["cdylib"]

[dependencies]
pyroscope = { path = "../../../../", default-features = false, features = ["native-tls"] }
rbspy = { workspace = true }
remoteprocess = { workspace = true }
anyhow = { workspace = true }
# todo remove this dependency
pretty_env_logger = { workspace = true }
log = { workspace = true }
libc = { workspace = true }
```

## File: `pyroscope_ffi/ruby/ext/rbspy/Rakefile`
```
# frozen_string_literal: true

require "shellwords"

class RbspyRakeCargoHelper
  attr_reader :gemname

  def initialize(gemname=File.basename(__dir__))
    @gemname = gemname
  end

  def self.command?(name)
    exts = ENV["PATHEXT"] ? ENV["PATHEXT"].split(";") : [""]
    ENV["PATH"].split(File::PATH_SEPARATOR).any? do |path|
      exts.any? do |ext|
        exe = File.join(path, "#{name}#{ext}")
        File.executable?(exe) && !File.directory?(exe)
      end
    end
  end

  def self.rust_toolchain
    # return env variable if set
    target = ENV["RUST_TARGET"]
    return target if target

    str = `rustc --version --verbose`
    info = str.lines.map {|l| l.chomp.split(/:\s+/, 2)}.drop(1).to_h
    info["host"]
  end

  def self.cargo_target_dir
    return @cargo_target_dir if defined? @cargo_target_dir

    str = `cargo metadata --format-version 1 --offline --no-deps --quiet`
    begin
      require "json"
      dir = JSON.parse(str)["target_directory"]
    rescue LoadError # json is usually part of the stdlib, but just in case
      /"target_directory"\s*:\s*"(?<dir>[^"]*)"/ =~ str
    end
    @cargo_target_dir = dir || "target"
  end

  def self.flags
    cc_flags = Shellwords.split(RbConfig.expand(RbConfig::MAKEFILE_CONFIG["CC"].dup))

    ["-C", "linker=#{cc_flags.shift}",
      *cc_flags.flat_map {|a| ["-C", "link-arg=#{a}"] },
      "-L", "native=#{RbConfig::CONFIG["libdir"]}",
      *dld_flags,
      *platform_flags,
    ]
  end

  def self.dld_flags
    Shellwords.split(RbConfig::CONFIG["DLDFLAGS"]).flat_map do |arg|
      arg = arg.gsub(/\$\((\w+)\)/) do
        $1 == "DEFFILE" ? nil : RbConfig::CONFIG[name]
      end.strip
      next [] if arg.empty?

      transform_flag(arg)
    end
  end

  def self.platform_flags
    return unless RbConfig::CONFIG["target_os"] =~ /mingw/i

    [*Shellwords.split(RbConfig::CONFIG["LIBRUBYARG"]).flat_map {|arg| transform_flag(arg)},
      "-C", "link-arg=-Wl,--dynamicbase",
      "-C", "link-arg=-Wl,--disable-auto-image-base",
      "-C", "link-arg=-static-libgcc"]
  end

  def self.transform_flag(arg)
    k, v = arg.split(/(?<=..)/, 2)
    case k
    when "-L"
      [k, "native=#{v}"]
    when "-l"
      [k, v]
    when "-F"
      ["-l", "framework=#{v}"]
    else
      ["-C", "link_arg=#{k}#{v}"]
    end
  end

  def install_dir
    File.expand_path(File.join("..", "..", "lib", gemname), __dir__)
  end

  def rust_name
    prefix = "lib" unless Gem.win_platform?
    suffix = if RbConfig::CONFIG["target_os"] =~ /darwin/i
      ".dylib"
    elsif Gem.win_platform?
      ".dll"
    else
      ".so"
    end
    "#{prefix}#{gemname}#{suffix}"
  end

  def ruby_name
    "#{gemname}.#{RbConfig::CONFIG["DLEXT"]}"
  end

end

task default: [:rbspy_install, :rbspy_clean]
task rbspy: [:rbspy_install, :rbspy_clean]

desc "set dev mode for subsequent task, run like `rake dev install`"
task :rbspy_dev do
  @dev = true
end

desc "build gem native extension and copy to lib"
task rbspy_install: [:rbspy_cd, :rbspy_build] do
  helper = RbspyRakeCargoHelper.new
  profile_dir = @dev ? "debug" : "release"
  arch_dir = RbspyRakeCargoHelper.rust_toolchain
  source = File.join(RbspyRakeCargoHelper.cargo_target_dir, arch_dir, profile_dir, helper.rust_name)
  dest = File.join(helper.install_dir, helper.ruby_name)
  mkdir_p(helper.install_dir)
  rm(dest) if File.exist?(dest)
  cp(source, dest)
end

desc "build gem native extension"
task rbspy_build: [:rbspy_cargo, :rbspy_cd] do
  sh "cargo", "rustc", *(["--locked", "--release"] unless @dev), "--target=#{RbspyRakeCargoHelper.rust_toolchain}", "--", *RbspyRakeCargoHelper.flags
end

desc "clean up release build artifacts"
task rbspy_clean: [:rbspy_cargo, :rbspy_cd] do
  sh "cargo clean --release"
end

desc "clean up build artifacts"
task rbspy_clobber: [:rbspy_cargo, :rbspy_cd] do
  sh "cargo clean"
end

desc "check for cargo"
task :rbspy_cargo do
  raise <<-MSG unless RbspyRakeCargoHelper.command?("cargo")
    This gem requires a Rust compiler and the `cargo' build tool to build the
    gem's native extension. See https://www.rust-lang.org/tools/install for
    how to install Rust. `cargo' is usually part of the Rust installation.
  MSG

  raise <<-MSG if Gem.win_platform? && RbspyRakeCargoHelper.rust_toolchain !~ /gnu/
    Found Rust toolchain `#{RbspyRakeCargoHelper.rust_toolchain}' but the gem native
    extension requires the gnu toolchain on Windows.
  MSG
end

# ensure task is running in the right dir
task :rbspy_cd do
  cd(__dir__) unless __dir__ == pwd
end
```

## File: `pyroscope_ffi/ruby/ext/rbspy/cbindgen.toml`
```
language = "C"
documentation_style = "C"

style = "type"

include_guard = "RBSPY_H_"
include_version = false

header = "/* Licensed under Apache-2.0 */"
autogen_warning = "/* Warning, this file is autogenerated by cbindgen. Don't modify this manually. */"

braces = "SameLine"
tab_width = 2
line_length = 80

[parse]
parse_deps = false
```

## File: `pyroscope_ffi/ruby/ext/rbspy/extconf.rb`
```ruby
require 'mkmf'
require 'rake'

create_makefile('rbspy')

app = Rake.application
app.init
app.add_import 'Rakefile'
app.load_rakefile

app['default'].invoke
```

## File: `pyroscope_ffi/ruby/ext/rbspy/include/rbspy.h`
```c
/* Licensed under Apache-2.0 */

#ifndef RBSPY_H_
#define RBSPY_H_

/* Warning, this file is autogenerated by cbindgen. Don't modify this manually. */

#include <stdarg.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdlib.h>

bool initialize_logging(uint32_t logging_level);

/*
 # Safety
 All pointer arguments must be valid, non-null, null-terminated C strings.
 */
bool initialize_agent(const char *application_name,
                      const char *server_address,
                      const char *basic_auth_user,
                      const char *basic_auth_password,
                      uint32_t sample_rate,
                      bool oncpu,
                      bool report_pid,
                      bool report_thread_id,
                      const char *tags,
                      const char *tenant_id,
                      const char *http_headers_json);

bool drop_agent(void);

/*
 # Safety
 `key` and `value` must be valid, non-null, null-terminated C strings.
 */
bool add_thread_tag(const char *key, const char *value);

/*
 # Safety
 `key` and `value` must be valid, non-null, null-terminated C strings.
 */
bool remove_thread_tag(const char *key, const char *value);

#endif  /* RBSPY_H_ */
```

## File: `pyroscope_ffi/ruby/ext/rbspy/src/backend.rs`
```rust
use pyroscope::{
    backend::{
        Backend, BackendConfig, Report, ReportBatch, ReportData, StackBuffer, StackFrame,
        StackTrace, ThreadTag, ThreadTagsSet,
    },
    error::{PyroscopeError, Result},
};
use rbspy::sampler::Sampler;
use std::{
    ops::Deref,
    sync::{
        mpsc::{channel, sync_channel, Receiver, Sender, SyncSender},
        Arc, Mutex,
    },
    thread::JoinHandle,
};

const LOG_TAG: &str = "Pyroscope::Rbspy";

pub struct Rbspy {
    sample_rate: u32,
    backend_config: BackendConfig,
    sampler: Sampler,
    /// Error Receiver
    error_receiver: Option<Receiver<std::result::Result<(), anyhow::Error>>>,
    /// Profiling buffer
    buffer: Arc<Mutex<StackBuffer>>,
    /// Rulset
    ruleset: ThreadTagsSet,
}

impl std::fmt::Debug for Rbspy {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "Rbspy Backend")
    }
}

impl Rbspy {
    /// Create a new Rbspy instance
    pub fn new(sampler: Sampler, sample_rate: u32, backend_config: BackendConfig) -> Self {
        Rbspy {
            sample_rate,
            sampler,
            backend_config,
            error_receiver: None,
            buffer: Arc::new(Mutex::new(StackBuffer::default())),
            ruleset: ThreadTagsSet::default(),
        }
    }
}

// Type aliases
type ErrorSender = Sender<std::result::Result<(), anyhow::Error>>;
type ErrorReceiver = Receiver<std::result::Result<(), anyhow::Error>>;

impl Backend for Rbspy {
    fn add_tag(&self, tag: ThreadTag) -> Result<()> {
        self.ruleset.add(tag)?;

        Ok(())
    }

    fn remove_tag(&self, tag: ThreadTag) -> Result<()> {
        self.ruleset.remove(tag)?;

        Ok(())
    }

    /// Initialize the backend
    fn initialize(&mut self) -> Result<()> {
        // Channel for Errors generated by the RubySpy Sampler
        let (error_sender, error_receiver): (ErrorSender, ErrorReceiver) = channel();

        // This is provides enough space for 100 threads.
        // It might be a better idea to figure out how many threads are running and determine the
        // size of the channel based on that.
        let queue_size: usize = self.sample_rate as usize * 10 * 100;

        // Channel for StackTraces generated by the RubySpy Sampler
        let (stack_sender, stack_receiver): (
            SyncSender<rbspy::StackTrace>,
            Receiver<rbspy::StackTrace>,
        ) = sync_channel(queue_size);

        // Set Error and Stack Receivers
        // self.stack_receiver = Some(stack_receiver);
        self.error_receiver = Some(error_receiver);

        self.sampler
            .start(stack_sender, error_sender)
            .map_err(|e| PyroscopeError::new(&format!("Rbspy: Sampler Error: {}", e)))?;

        // Start own thread
        //
        // Get an Arc reference to the Report Buffer
        let buffer = self.buffer.clone();

        // ruleset reference
        let ruleset = self.ruleset.clone();

        let backend_config = self.backend_config;

        let _: JoinHandle<Result<()>> = std::thread::spawn(move || {
            // Iterate over the StackTrace
            while let Ok(stack_trace) = stack_receiver.recv() {
                // convert StackTrace
                let own_trace: StackTrace =
                    Into::<StackTraceWrapper>::into((stack_trace, &backend_config)).into();

                let stacktrace = own_trace.add_tag_rules(&ruleset);

                buffer.lock()?.record(stacktrace)?;
            }

            Ok(())
        });

        Ok(())
    }

    fn shutdown(self: Box<Self>) -> Result<()> {
        log::trace!(target: LOG_TAG, "Shutting down sampler thread");

        self.sampler.stop();

        Ok(())
    }

    fn report(&mut self) -> Result<ReportBatch> {
        let v8: StackBuffer = self.buffer.lock()?.deref().to_owned();
        let reports: Vec<Report> = v8.into();

        self.buffer.lock()?.clear();

        Ok(ReportBatch {
            profile_type: "process_cpu".into(),
            data: ReportData::Reports(reports),
        })
    }
}

struct StackFrameWrapper(StackFrame);

impl From<StackFrameWrapper> for StackFrame {
    fn from(frame: StackFrameWrapper) -> Self {
        frame.0
    }
}

impl From<rbspy::StackFrame> for StackFrameWrapper {
    fn from(frame: rbspy::StackFrame) -> Self {
        StackFrameWrapper(StackFrame {
            module: None,
            name: Some(frame.name),
            filename: Some(frame.relative_path.clone()),
            relative_path: Some(frame.relative_path),
            absolute_path: frame.absolute_path,
            line: frame.lineno.map(|l| l as u32),
        })
    }
}

struct StackTraceWrapper(StackTrace);

impl From<StackTraceWrapper> for StackTrace {
    fn from(trace: StackTraceWrapper) -> Self {
        trace.0
    }
}

impl From<(rbspy::StackTrace, &BackendConfig)> for StackTraceWrapper {
    fn from(arg: (rbspy::StackTrace, &BackendConfig)) -> Self {
        let (trace, config) = arg;

        let thread_id = trace.thread_id.map(|tid| {
            // for rbspy we use pthread_t as thread id
            // https://github.com/ruby/ruby/blob/54a74c42033e42869e69e7dc9e67efa1faf225be/include/ruby/thread_native.h#L41
            let thread_id = tid as libc::pthread_t;
            thread_id.into()
        });

        StackTraceWrapper(StackTrace::new(
            config,
            trace.pid.map(|pid| pid as u32),
            thread_id,
            None,
            trace
                .iter()
                .map(|frame| Into::<StackFrameWrapper>::into(frame.clone()).into())
                .collect(),
        ))
    }
}

pub fn self_thread_id() -> pyroscope::ThreadId {
    // for rbspy we use pthread_t as thread id
    // https://github.com/ruby/ruby/blob/54a74c42033e42869e69e7dc9e67efa1faf225be/include/ruby/thread_native.h#L41
    pyroscope::ThreadId::pthread_self()
}
```

## File: `pyroscope_ffi/ruby/ext/rbspy/src/lib.rs`
```rust
mod backend;

use rbspy::sampler::Sampler;
use remoteprocess::Pid;
use std::env;
use std::ffi::CStr;
use std::os::raw::c_char;

use crate::backend::Rbspy;
use pyroscope::backend::{BackendConfig, BackendImpl, Report, StackFrame, Tag};
use pyroscope::pyroscope::PyroscopeAgentBuilder;

const LOG_TAG: &str = "Pyroscope::rbspy::ffi";
const RBSPY_NAME: &str = "rbspy";
const RBSPY_VERSION: &str = env!("CARGO_PKG_VERSION");

pub fn transform_report(report: Report) -> Report {
    let cwd = env::current_dir().unwrap();
    let cwd = cwd.to_str().unwrap_or("");

    let data = report
        .data
        .iter()
        .map(|(stacktrace, count)| {
            let new_frames = stacktrace
                .frames
                .iter()
                .map(|frame| {
                    let frame = frame.to_owned();
                    let mut s = frame.filename.unwrap();
                    if let Some(i) = s.find(cwd) {
                        s = s[(i + cwd.len() + 1)..].to_string();
                    } else if let Some(i) = s.find("/gems/") {
                        s = s[(i + 1)..].to_string();
                    } else if let Some(i) = s.find("/ruby/") {
                        s = s[(i + 6)..].to_string();
                        if let Some(i) = s.find('/') {
                            s = s[(i + 1)..].to_string();
                        }
                    }

                    // something
                    StackFrame::new(
                        frame.module,
                        frame.name,
                        Some(s.to_string()),
                        frame.relative_path,
                        frame.absolute_path,
                        frame.line,
                    )
                })
                .collect();

            let mut mystack = stacktrace.to_owned();

            mystack.frames = new_frames;

            (mystack, count.to_owned())
        })
        .collect();

    Report::new(data).metadata(report.metadata.clone())
}

#[no_mangle]
pub extern "C" fn initialize_logging(logging_level: u32) -> bool {
    // Force rustc to display the log messages in the console.
    match logging_level {
        50 => {
            std::env::set_var("RUST_LOG", "error");
        }
        40 => {
            std::env::set_var("RUST_LOG", "warn");
        }
        30 => {
            std::env::set_var("RUST_LOG", "info");
        }
        20 => {
            std::env::set_var("RUST_LOG", "debug");
        }
        10 => {
            std::env::set_var("RUST_LOG", "trace");
        }
        _ => {
            std::env::set_var("RUST_LOG", "debug");
        }
    }

    // Initialize the logger.
    pretty_env_logger::init_timed();

    true
}

#[no_mangle]
/// # Safety
/// All pointer arguments must be valid, non-null, null-terminated C strings.
pub unsafe extern "C" fn initialize_agent(
    application_name: *const c_char,
    server_address: *const c_char,
    basic_auth_user: *const c_char,
    basic_auth_password: *const c_char,
    sample_rate: u32,
    oncpu: bool,
    report_pid: bool,
    report_thread_id: bool,
    tags: *const c_char,
    tenant_id: *const c_char,
    http_headers_json: *const c_char,
) -> bool {
    let application_name = unsafe { CStr::from_ptr(application_name) }
        .to_str()
        .unwrap()
        .to_string();

    let server_address = unsafe { CStr::from_ptr(server_address) }
        .to_str()
        .unwrap()
        .to_string();

    let basic_auth_user = unsafe { CStr::from_ptr(basic_auth_user) }
        .to_str()
        .unwrap()
        .to_string();

    let basic_auth_password = unsafe { CStr::from_ptr(basic_auth_password) }
        .to_str()
        .unwrap()
        .to_string();

    let tags_string = unsafe { CStr::from_ptr(tags) }
        .to_str()
        .unwrap()
        .to_string();

    let tenant_id = unsafe { CStr::from_ptr(tenant_id) }
        .to_str()
        .unwrap()
        .to_string();

    let http_headers_json = unsafe { CStr::from_ptr(http_headers_json) }
        .to_str()
        .unwrap()
        .to_string();

    let pid = std::process::id();

    let backend_config = BackendConfig {
        report_thread_id,
        report_thread_name: false,
        report_pid,
    };

    let sampler = Sampler::new(pid as Pid, sample_rate, false, None, false, None, oncpu);

    let tags_ref = tags_string.as_str();
    let tags = string_to_tags(tags_ref);
    let rbspy = BackendImpl::new(Box::new(Rbspy::new(sampler, sample_rate, backend_config)));

    let mut agent_builder = PyroscopeAgentBuilder::new(
        server_address,
        application_name,
        sample_rate,
        RBSPY_NAME,
        RBSPY_VERSION,
        rbspy,
    )
    .func(transform_report)
    .tags(tags);

    if !basic_auth_user.is_empty() && !basic_auth_password.is_empty() {
        agent_builder = agent_builder.basic_auth(basic_auth_user, basic_auth_password);
    }

    if !tenant_id.is_empty() {
        agent_builder = agent_builder.tenant_id(tenant_id);
    }

    let http_headers = pyroscope::pyroscope::parse_http_headers_json(http_headers_json);
    match http_headers {
        Ok(http_headers) => {
            agent_builder = agent_builder.http_headers(http_headers);
        }
        Err(e) => match e {
            pyroscope::PyroscopeError::Json(e) => {
                log::error!(target: LOG_TAG, "parse_http_headers_json error {}", e);
            }
            pyroscope::PyroscopeError::AdHoc(e) => {
                log::error!(target: LOG_TAG, "parse_http_headers_json {}", e);
            }
            _ => {}
        },
    }

    pyroscope::ffikit::run(agent_builder).is_ok()
}

#[no_mangle]
pub extern "C" fn drop_agent() -> bool {
    pyroscope::ffikit::send(pyroscope::ffikit::Signal::Kill).is_ok()
}

#[no_mangle]
/// # Safety
/// `key` and `value` must be valid, non-null, null-terminated C strings.
pub unsafe extern "C" fn add_thread_tag(key: *const c_char, value: *const c_char) -> bool {
    let key = unsafe { CStr::from_ptr(key) }.to_str().unwrap().to_owned();
    let value = unsafe { CStr::from_ptr(value) }
        .to_str()
        .unwrap()
        .to_owned();

    pyroscope::ffikit::send(pyroscope::ffikit::Signal::AddThreadTag(
        backend::self_thread_id(),
        Tag { key, value },
    ))
    .is_ok()
}

#[no_mangle]
/// # Safety
/// `key` and `value` must be valid, non-null, null-terminated C strings.
pub unsafe extern "C" fn remove_thread_tag(key: *const c_char, value: *const c_char) -> bool {
    let key = unsafe { CStr::from_ptr(key) }.to_str().unwrap().to_owned();
    let value = unsafe { CStr::from_ptr(value) }
        .to_str()
        .unwrap()
        .to_owned();

    pyroscope::ffikit::send(pyroscope::ffikit::Signal::RemoveThreadTag(
        backend::self_thread_id(),
        Tag { key, value },
    ))
    .is_ok()
}

fn string_to_tags(tags: &str) -> Vec<(&str, &str)> {
    let mut tags_vec = Vec::new();
    // check if string is empty
    if tags.is_empty() {
        return tags_vec;
    }

    for tag in tags.split(',') {
        let mut tag_split = tag.split('=');
        let key = tag_split.next().unwrap();
        let value = tag_split.next().unwrap();
        tags_vec.push((key, value));
    }

    tags_vec
}
```

## File: `pyroscope_ffi/ruby/lib/pyroscope.rb`
```ruby
# coding: utf-8
# frozen_string_literal: true

require 'ffi'
require 'json'

module Pyroscope
  module Rust
    extend FFI::Library
    ffi_lib File.expand_path(File.dirname(__FILE__)) + "/rbspy/rbspy.#{RbConfig::CONFIG["DLEXT"]}"
    attach_function :initialize_logging, [:int], :bool
    attach_function :initialize_agent, [:string, :string, :string, :string, :int, :bool, :bool, :bool, :string, :string, :string], :bool
    attach_function :add_thread_tag, [:string, :string], :bool
    attach_function :remove_thread_tag, [:string, :string], :bool
    attach_function :drop_agent, [], :bool
  end

  if defined?(::Rails::Engine)
    class Engine < ::Rails::Engine
      config.after_initialize do
        next unless ::Pyroscope.current_config && ::Pyroscope.current_config.autoinstrument_rails

        ::Pyroscope.initialize_rails_hooks
      end
    end
  end

  Config = Struct.new(
    :application_name,
    :app_name,
    :server_address,
    :basic_auth_username,
    :basic_auth_password,
    :log_level,
    :sample_rate,
    :oncpu,
    :report_pid,
    :report_thread_id,
    :tags,
    :compression,
    :report_encoding,
    :autoinstrument_rails,
    :tenant_id,
    :http_headers,
  ) do
    def initialize(*)
      super
      # defaults:
      self.application_name = ''
      self.server_address = 'http://localhost:4040'
      self.basic_auth_username = ''
      self.basic_auth_password = ''
      self.sample_rate = 100
      self.oncpu = true
      self.report_pid = false
      self.report_thread_id = false
      self.log_level = 'error'
      self.tags = {}
      self.compression = 'gzip'
      self.report_encoding = 'pprof'
      self.autoinstrument_rails = true
      self.tenant_id = ''
      self.http_headers = {}
    end
  end

  class << self
    def current_config
      @config
    end

    def configure
      @config = Config.new

      # Pass config to the block
      yield @config

      # Determine Logging level (kinda like an enum).
      case @config.log_level
      when 'trace'
        @log_level = 10
      when 'debug'
        @log_level = 20
      when 'info'
        @log_level = 30
      when 'warn'
        @log_level = 40
      when 'error'
        @log_level = 50
      else
        @log_level = 50
      end

      Rust.initialize_logging(@log_level)

      Rust.initialize_agent(
        # these are defaults in case user-provided values are nil:
        @config.app_name || @config.application_name || "",
        @config.server_address || "",
        @config.basic_auth_username || "",
        @config.basic_auth_password || "",
        @config.sample_rate || 100,
        @config.oncpu || false,
        @config.report_pid || false,
        @config.report_thread_id || false,
        tags_to_string(@config.tags || {}),
        @config.tenant_id || "",
        http_headers_to_json(@config.http_headers || {})
      )
    end

    def initialize_rails_hooks
      block = lambda do |ctrl, action|
        Pyroscope.tag_wrapper({
          "action" => "#{ctrl.controller_name}/#{ctrl.action_name}"
        }, &action)
      end

      ActionController::API.__send__(:around_action, block) if defined? ActionController::API
      ActionController::Base.__send__(:around_action, block) if defined? ActionController::Base
    end

    def tag_wrapper(tags)
      _add_tags(tags)
      begin
        yield
      ensure
        _remove_tags(tags)
      end
    end

    def tag(tags)
      warn("deprecated. Use `Pyroscope.tag_wrapper` instead.")
    end

    def remove_tags(*tags)
      warn("deprecated. Use `Pyroscope.tag_wrapper` instead.")
    end

    def _add_tags(tags)
      tags.each do |tag_name, tag_value|
        Rust.add_thread_tag(tag_name.to_s, tag_value.to_s)
      end
    end

    def _remove_tags(tags)
      tags.each do |tag_name, tag_value|
        Rust.remove_thread_tag(tag_name.to_s, tag_value.to_s)
      end
    end

    def stop
      Rust.drop_agent
    end

    def shutdown
      stop
    end

    private

    def tags_to_string(tags)
      tags.map { |k, v| "#{k}=#{v}" }.join(',')
    end

    def http_headers_to_json(http_headers)
      JSON.dump(http_headers)
    end

  end
end
```

## File: `pyroscope_ffi/ruby/lib/pyroscope/version.rb`
```ruby
module Pyroscope
  VERSION = '1.0.1'.freeze
end
```

## File: `pyroscope_ffi/ruby/scripts/tests/test.rb`
```ruby
#!/usr/bin/env ruby

require "pyroscope"
require "pyroscope/version"

puts Pyroscope::VERSION
puts RUBY_VERSION

def start_local_pyroscope
  container_name = "pyroscope-ruby-test-#{Process.pid}"
  system(
    "docker", "run", "-d",
    "--name", container_name,
    "-p", "4040:4040",
    "grafana/pyroscope:latest",
    "-ingester.min-ready-duration=0s"
  )

  unless $?.success?
    warn "failed to start local grafana/pyroscope container"
    exit 1
  end

  20.times do
    ready = system("curl", "-fsS", "http://localhost:4040/ready")
    return container_name if ready
    sleep 1
  end

  warn "pyroscope container did not become ready"
  warn "==== pyroscope container status ===="
  system("docker", "ps", "-a", "--filter", "name=#{container_name}")
  warn "==== pyroscope container logs ===="
  system("docker", "logs", container_name)
  system("docker", "rm", "-f", container_name)
  exit 1
end

def stop_local_pyroscope(container_name)
  return if container_name.nil? || container_name.empty?

  system("docker", "rm", "-f", container_name)
end

pyroscope_container = start_local_pyroscope
at_exit { stop_local_pyroscope(pyroscope_container) }

Pyroscope.configure do |config|
  config.application_name = "#{ENV["PYROSCOPE_RUN_ID"]}"
  config.server_address = "http://localhost:4040"
  config.oncpu = ENV["PYROSCOPE_ONCPU"] == "1"
  config.log_level = "trace"
  config.report_pid = true
  config.report_thread_id = true
  config.tags = {
    :region => "us-east",
    :oncpu => ENV["PYROSCOPE_ONCPU"],
    :version => ENV["RUBY_VERSION"],
    :arch => ENV["PYROSCOPE_ARCH"]
  }
end

def work(n)
  i = 0
  while i < n
    i += 1
  end
end

def fast_function
  Pyroscope.tag_wrapper({"function": "fast"}) do
    work(2001002000)
  end
end

def slow_function
  work(8001008000)
end

child_pid = fork do
  puts "This is the child process"
  Pyroscope.tag_wrapper({"fork": "forked"}) do
    slow_function()
  end
end

puts "This is the master process."

Pyroscope.tag_wrapper({"fork": "master"}) do
  fast_function()
end

puts "The PID of the child process is #{child_pid}"

Pyroscope.shutdown()
```

## File: `src/error.rs`
```rust
pub type Result<T> = std::result::Result<T, PyroscopeError>;

/// Error type of Pyroscope
#[non_exhaustive]
#[derive(thiserror::Error, Debug)]
pub enum PyroscopeError {
    #[error("Other: {}", &.0)]
    AdHoc(String),

    #[error("{msg}: {source:?}")]
    Compat {
        msg: String,
        #[source]
        source: Box<dyn std::error::Error + Send + Sync + 'static>,
    },

    #[error("BackendImpl error")]
    BackendImpl,

    #[error(transparent)]
    Reqwest(#[from] reqwest::Error),

    #[error(transparent)]
    ParseError(#[from] url::ParseError),

    #[error(transparent)]
    TimeSource(#[from] std::time::SystemTimeError),

    #[error(transparent)]
    Io(#[from] std::io::Error),

    #[error(transparent)]
    Json(#[from] serde_json::Error),
}

impl PyroscopeError {
    /// Create a new instance of PyroscopeError
    pub fn new(msg: &str) -> Self {
        PyroscopeError::AdHoc(msg.to_string())
    }

    /// Create a new instance of PyroscopeError with source
    pub fn new_with_source<E>(msg: &str, source: E) -> Self
    where
        E: std::error::Error + Send + Sync + 'static,
    {
        PyroscopeError::Compat {
            msg: msg.to_string(),
            source: Box::new(source),
        }
    }
}

impl<T> From<std::sync::PoisonError<T>> for PyroscopeError {
    fn from(_err: std::sync::PoisonError<T>) -> Self {
        PyroscopeError::AdHoc("Poison Error".to_owned())
    }
}

impl<T: 'static + Send + Sync> From<std::sync::mpsc::SendError<T>> for PyroscopeError {
    fn from(err: std::sync::mpsc::SendError<T>) -> Self {
        PyroscopeError::Compat {
            msg: String::from("SendError Error"),
            source: Box::new(err),
        }
    }
}
```

## File: `src/ffikit.rs`
```rust
use crate::backend::Tag;
use crate::error::{PyroscopeError, Result};
use crate::pyroscope::{PyroscopeAgentBuilder, PyroscopeAgentRunning};
use crate::{PyroscopeAgent, ThreadId};
use lazy_static::lazy_static;
use std::sync::{
    mpsc::{self, Receiver, Sender},
    Mutex,
};

#[derive(Debug, PartialEq, Clone)]
pub enum Signal {
    Kill,
    AddThreadTag(ThreadId, Tag),
    RemoveThreadTag(ThreadId, Tag),
}

const TAG: &str = "pyroscope::ffikit";

lazy_static! {
    static ref SENDER: Mutex<Option<Sender<Signal>>> = Mutex::new(None);
}
pub fn run(agent: PyroscopeAgentBuilder) -> Result<()> {
    let mut sender_holder = SENDER.lock()?;
    if (*sender_holder).is_some() {
        return Err(PyroscopeError::new("FFI channel already initialized"));
    }

    let agent = agent.build()?;

    let agent = agent.start()?;

    let (sender, receiver): (Sender<Signal>, Receiver<Signal>) = mpsc::channel();

    *sender_holder = Some(sender);

    std::thread::spawn(move || {
        while let Ok(signal) = receiver.recv() {
            match signal {
                Signal::Kill => {
                    if let Err(err) = stop(agent) {
                        log::error!(target: TAG, "failed to stop agent {}", err);
                    }
                    break;
                }
                Signal::AddThreadTag(thread_id, tag) => {
                    if let Err(err) = agent.add_thread_tag(thread_id, tag) {
                        log::error!(target: TAG, "failed to add tag {}", err);
                    }
                }
                Signal::RemoveThreadTag(thread_id, tag) => {
                    if let Err(err) = agent.remove_thread_tag(thread_id, tag) {
                        log::error!(target: TAG, "failed to remove tag {}", err);
                    }
                }
            }
        }
    });

    Ok(())
}

pub fn send(signal: Signal) -> Result<()> {
    if let Some(sender) = &*SENDER.lock()? {
        sender.send(signal)?;
    } else {
        return Err(PyroscopeError::new("FFI channel not initialized"));
    }
    Ok(())
}

fn stop(agent: PyroscopeAgent<PyroscopeAgentRunning>) -> Result<()> {
    agent.stop()?;
    *SENDER.lock()? = None;
    Ok(())
}
```

## File: `src/lib.rs`
```rust
//! Rust integration for [Pyroscope](https://pyroscope.io).
//!
//! # Quick Start
//!
//! ## Add the Pyroscope Library and the pprof-rs backend to Cargo.toml
//!
//! ```toml
//! [dependencies]
//! pyroscope = { version = "2.0.0", features = ["backend-pprof-rs"] }
//! ```
//!
//! ## Configure a Pyroscope Agent
//!
//! ```ignore
//! let agent =
//!     PyroscopeAgent::builder("http://localhost:4040", "myapp")
//!     .backend(pprof_backend(PprofConfig { sample_rate: 100 }, BackendConfig::default()))
//!     .build()?;
//! ```
//!
//! ## Start/Stop profiling
//!
//! To start profiling code and sending data.
//!
//! ```ignore
//!  let agent_running = agent.start()?;
//! ```
//!
//! To stop profiling code. You can restart the profiling at a later point.
//!
//! ```ignore
//!  let agent_ready = agent.stop()?;
//! ```
//!
//! Before you drop the variable, make sure to shutdown the agent.
//!
//! ```ignore
//! agent_ready.shutdown();
//! ```

extern crate core;

// Re-exports structs
pub use crate::pyroscope::PyroscopeAgent;
pub use error::{PyroscopeError, Result};

pub mod backend;
pub mod encode;
pub mod error;
pub mod pyroscope;
pub mod session;
pub mod timer;

mod utils;
pub use utils::ThreadId;
pub mod ffikit;
```

## File: `src/pyroscope.rs`
```rust
use std::{
    collections::HashMap,
    marker::PhantomData,
    sync::{
        mpsc::{self, Sender},
        Arc, Condvar, Mutex,
    },
    thread::JoinHandle,
};

use crate::{
    backend::{BackendReady, BackendUninitialized, Report, Tag},
    error::Result,
    session::{Session, SessionManager, SessionSignal},
    timer::{Timer, TimerSignal},
    utils::get_time_range,
    PyroscopeError,
};

use crate::backend::{BackendImpl, ThreadTag};

const LOG_TAG: &str = "Pyroscope::Agent";
const PPROFRS_SPY_NAME: &str = "pyroscope-rs";
const PPROFRS_SPY_VERSION: &str = env!("CARGO_PKG_VERSION");

/// Pyroscope Agent Configuration. This is the configuration that is passed to the agent.
///
/// # Example
/// ```
/// use pyroscope::pyroscope::PyroscopeConfig;
/// let config = PyroscopeConfig::new("http://localhost:8080", "my-app", 100, "pyspy", "0.8.16");
/// ```
#[derive(Clone, Debug)]
pub struct PyroscopeConfig {
    /// Pyroscope Server Address
    pub url: String,
    /// Application Name
    pub application_name: String,
    /// Tags
    pub tags: HashMap<String, String>,
    /// Sample Rate
    pub sample_rate: u32,
    /// Spy Name
    pub spy_name: String,
    /// Spy Version
    pub spy_version: String,
    pub basic_auth: Option<BasicAuth>,
    /// Function to apply
    pub func: Option<fn(Report) -> Report>,
    pub tenant_id: Option<String>,
    pub http_headers: HashMap<String, String>,
}

#[derive(Clone, Debug)]
pub struct BasicAuth {
    pub username: String,
    pub password: String,
}

impl Default for PyroscopeConfig {
    fn default() -> Self {
        Self {
            url: "http://localhost:4040".to_string(),
            application_name: names::Generator::default()
                .next()
                .unwrap_or_else(|| "unassigned.app".to_string())
                .replace('-', "."),
            tags: HashMap::new(),
            sample_rate: 100u32,
            spy_name: PPROFRS_SPY_NAME.to_string(),
            spy_version: PPROFRS_SPY_VERSION.to_string(),
            basic_auth: None,
            func: None,
            tenant_id: None,
            http_headers: HashMap::new(),
        }
    }
}

impl PyroscopeConfig {
    /// Create a new PyroscopeConfig object.
    ///
    /// # Example
    /// ```ignore
    /// let config = PyroscopeConfig::new("http://localhost:8080", "my-app", 100, "pyspy", "0.8.16");
    /// ```
    pub fn new(
        url: impl AsRef<str>,
        application_name: impl AsRef<str>,
        sample_rate: u32,
        spy_name: impl AsRef<str>,
        spy_version: impl AsRef<str>,
    ) -> Self {
        Self {
            url: url.as_ref().to_owned(),
            application_name: application_name.as_ref().to_owned(),
            tags: HashMap::new(),
            sample_rate,
            spy_name: spy_name.as_ref().to_owned(),
            spy_version: spy_version.as_ref().to_owned(),
            basic_auth: None,
            func: None,
            tenant_id: None,
            http_headers: HashMap::new(),
        }
    }

    // Set the Pyroscope Server URL
    pub fn url(self, url: impl AsRef<str>) -> Self {
        Self {
            url: url.as_ref().to_owned(),
            ..self
        }
    }

    pub fn basic_auth(self, username: String, password: String) -> Self {
        Self {
            basic_auth: Some(BasicAuth { username, password }),
            ..self
        }
    }

    /// Set the Function.
    pub fn func(self, func: fn(Report) -> Report) -> Self {
        Self {
            func: Some(func),
            ..self
        }
    }

    /// Set the tags.
    ///
    /// # Example
    /// ```ignore
    /// use pyroscope::pyroscope::PyroscopeConfig;
    /// let config = PyroscopeConfig::new("http://localhost:8080", "my-app")
    ///    .tags(vec![("env", "dev")])?;
    /// ```
    pub fn tags(self, tags: Vec<(&str, &str)>) -> Self {
        // Convert &[(&str, &str)] to HashMap(String, String)
        let tags_hashmap: HashMap<String, String> = tags
            .to_owned()
            .iter()
            .cloned()
            .map(|(a, b)| (a.to_owned(), b.to_owned()))
            .collect();

        Self {
            tags: tags_hashmap,
            ..self
        }
    }

    pub fn tenant_id(self, tenant_id: String) -> Self {
        Self {
            tenant_id: Some(tenant_id),
            ..self
        }
    }

    pub fn http_headers(self, http_headers: HashMap<String, String>) -> Self {
        Self {
            http_headers,
            ..self
        }
    }
}

/// PyroscopeAgent Builder
///
/// Alternatively, you can use PyroscopeAgent::build() which is a short-hand
/// for calling PyroscopeAgentBuilder::new()
///
/// # Example
/// ```ignore
/// use pyroscope::pyroscope::PyroscopeAgentBuilder;
/// let builder = PyroscopeAgentBuilder::new("http://localhost:8080", "my-app", 100, "pyspy", "0.8.16", backend);
/// let agent = builder.build()?;
/// ```
pub struct PyroscopeAgentBuilder {
    /// Profiler backend
    backend: BackendImpl<BackendUninitialized>,
    /// Configuration Object
    config: PyroscopeConfig,
}

impl PyroscopeAgentBuilder {
    /// Create a new PyroscopeAgentBuilder object.
    ///
    /// # Example
    /// ```ignore
    /// let builder = PyroscopeAgentBuilder::new("http://localhost:8080", "my-app", 100, "pyspy", "0.8.16", backend);
    /// ```
    pub fn new(
        url: impl AsRef<str>,
        application_name: impl AsRef<str>,
        sample_rate: u32,
        spy_name: impl AsRef<str>,
        spy_version: impl AsRef<str>,
        backend: BackendImpl<BackendUninitialized>,
    ) -> Self {
        Self {
            backend,
            config: PyroscopeConfig::new(url, application_name, sample_rate, spy_name, spy_version),
        }
    }

    /// Set the Pyroscope Server URL. This can be used if the Builder was initialized with the default
    /// trait. Default is "http://localhost:4040".
    ///
    /// # Example
    /// ```ignore
    /// let builder = PyroscopeAgentBuilder::default()
    /// .url("http://localhost:8080")
    /// .build()?;
    /// ```
    pub fn url(self, url: impl AsRef<str>) -> Self {
        Self {
            config: self.config.url(url),
            ..self
        }
    }

    pub fn basic_auth(self, username: impl AsRef<str>, password: impl AsRef<str>) -> Self {
        Self {
            config: self
                .config
                .basic_auth(username.as_ref().to_owned(), password.as_ref().to_owned()),
            ..self
        }
    }

    /// Set the Function.
    /// This is optional. If not set, the agent will not apply any function.
    /// #Example
    /// ```ignore
    /// let builder = PyroscopeAgentBuilder::new("http://localhost:8080", "my-app")
    /// .func(|report| {
    ///    report
    ///    })
    ///    .build()
    ///    ?;
    ///    ```
    pub fn func(self, func: fn(Report) -> Report) -> Self {
        Self {
            config: self.config.func(func),
            ..self
        }
    }

    /// Set tags. Default is empty.
    ///
    /// # Example
    /// ```ignore
    /// let builder = PyroscopeAgentBuilder::new("http://localhost:8080", "my-app")
    /// .tags(vec![("env", "dev")])
    /// .build()?;
    /// ```
    pub fn tags(self, tags: Vec<(&str, &str)>) -> Self {
        Self {
            config: self.config.tags(tags),
            ..self
        }
    }

    pub fn tenant_id(self, tenant_id: String) -> Self {
        Self {
            config: self.config.tenant_id(tenant_id),
            ..self
        }
    }

    pub fn http_headers(self, http_headers: HashMap<String, String>) -> Self {
        Self {
            config: self.config.http_headers(http_headers),
            ..self
        }
    }

    /// Initialize the backend, timer and return a PyroscopeAgent with Ready
    /// state. While you can call this method, you should call it through the
    /// `PyroscopeAgent.build()` method.
    pub fn build(self) -> Result<PyroscopeAgent<PyroscopeAgentReady>> {
        let config = self.config;

        // Set Global Tags
        // for (key, value) in config.tags.iter() {
        // todo!("implement")
        // }

        // Initialize the Backend
        let backend_ready = self.backend.initialize()?;
        log::trace!(target: LOG_TAG, "Backend initialized");

        // Start the Timer
        let timer = Timer::initialize(std::time::Duration::from_secs(10))?;
        log::trace!(target: LOG_TAG, "Timer initialized");

        // Start the SessionManager
        let session_manager = SessionManager::new()?;
        log::trace!(target: LOG_TAG, "SessionManager initialized");

        // Return PyroscopeAgent
        Ok(PyroscopeAgent {
            backend: backend_ready,
            config,
            timer,
            session_manager,
            tx: None,
            handle: None,
            running: Arc::new((
                #[allow(clippy::mutex_atomic)]
                Mutex::new(false),
                Condvar::new(),
            )),
            _state: PhantomData,
        })
    }
}

/// This trait is used to encode the state of the agent.
pub trait PyroscopeAgentState {}

/// Marker struct for an Uninitialized state.
#[derive(Debug)]
pub struct PyroscopeAgentBare;

/// Marker struct for a Ready state.
#[derive(Debug)]
pub struct PyroscopeAgentReady;

/// Marker struct for a Running state.
#[derive(Debug)]
pub struct PyroscopeAgentRunning;

impl PyroscopeAgentState for PyroscopeAgentBare {}

impl PyroscopeAgentState for PyroscopeAgentReady {}

impl PyroscopeAgentState for PyroscopeAgentRunning {}

/// PyroscopeAgent is the main object of the library. It is used to start and stop the profiler, schedule the timer, and send the profiler data to the server.
pub struct PyroscopeAgent<S: PyroscopeAgentState> {
    /// Instance of the Timer
    timer: Timer,
    /// Instance of the SessionManager
    session_manager: SessionManager,
    /// Channel sender for the timer thread
    tx: Option<Sender<TimerSignal>>,
    /// Handle to the thread that runs the Pyroscope Agent
    handle: Option<JoinHandle<Result<()>>>,
    /// A structure to signal thread termination
    running: Arc<(Mutex<bool>, Condvar)>,
    /// Profiler backend
    pub backend: BackendImpl<BackendReady>,
    /// Configuration Object
    pub config: PyroscopeConfig,
    /// PyroscopeAgent State
    _state: PhantomData<S>,
}

impl<S: PyroscopeAgentState> PyroscopeAgent<S> {
    /// Transition the PyroscopeAgent to a new state.
    fn transition<D: PyroscopeAgentState>(self) -> PyroscopeAgent<D> {
        PyroscopeAgent {
            timer: self.timer,
            session_manager: self.session_manager,
            tx: self.tx,
            handle: self.handle,
            running: self.running,
            backend: self.backend,
            config: self.config,
            _state: PhantomData,
        }
    }
}

impl<S: PyroscopeAgentState> PyroscopeAgent<S> {
    /// Properly shutdown the agent.
    pub fn shutdown(mut self) {
        log::debug!(target: LOG_TAG, "PyroscopeAgent::drop()");

        // Shutdown Backend
        match self.backend.shutdown() {
            Ok(_) => log::debug!(target: LOG_TAG, "Backend shutdown"),
            Err(e) => log::error!(target: LOG_TAG, "Backend shutdown error: {}", e),
        }

        // Drop Timer listeners
        match self.timer.drop_listeners() {
            Ok(_) => log::trace!(target: LOG_TAG, "Dropped timer listeners"),
            Err(_) => log::error!(target: LOG_TAG, "Error Dropping timer listeners"),
        }

        // Wait for the Timer thread to finish
        if let Some(handle) = self.timer.handle.take() {
            match handle.join() {
                Ok(_) => log::trace!(target: LOG_TAG, "Dropped timer thread"),
                Err(_) => log::error!(target: LOG_TAG, "Error Dropping timer thread"),
            }
        }

        // Stop the SessionManager
        match self.session_manager.push(SessionSignal::Kill) {
            Ok(_) => log::trace!(target: LOG_TAG, "Sent kill signal to SessionManager"),
            Err(_) => log::error!(
                target: LOG_TAG,
                "Error sending kill signal to SessionManager"
            ),
        }

        if let Some(handle) = self.session_manager.handle.take() {
            match handle.join() {
                Ok(_) => log::trace!(target: LOG_TAG, "Dropped SessionManager thread"),
                Err(_) => log::error!(target: LOG_TAG, "Error Dropping SessionManager thread"),
            }
        }

        // Wait for main thread to finish
        if let Some(handle) = self.handle.take() {
            match handle.join() {
                Ok(_) => log::trace!(target: LOG_TAG, "Dropped main thread"),
                Err(_) => log::error!(target: LOG_TAG, "Error Dropping main thread"),
            }
        }

        log::debug!(target: LOG_TAG, "Agent Shutdown");
    }
}

impl PyroscopeAgent<PyroscopeAgentReady> {
    /// Start profiling and sending data. The agent will keep running until stopped. The agent will send data to the server every 10s seconds.
    ///
    /// # Example
    /// ```ignore
    /// let agent = PyroscopeAgent::builder("http://localhost:8080", "my-app").build()?;
    /// let agent_running = agent.start()?;
    /// ```
    pub fn start(mut self) -> Result<PyroscopeAgent<PyroscopeAgentRunning>> {
        log::debug!(target: LOG_TAG, "Starting");

        // Create a clone of Backend
        let backend = Arc::clone(&self.backend.backend);
        // Call start()

        // set running to true
        let pair = Arc::clone(&self.running);
        let (lock, _cvar) = &*pair;
        let mut running = lock.lock()?;
        *running = true;
        drop(running);

        // Create a channel to listen for timer signals
        let (tx, rx) = mpsc::channel();
        self.timer.attach_listener(tx.clone())?;
        self.tx = Some(tx);

        let config = self.config.clone();

        // Clone SessionManager Sender
        let stx = self.session_manager.tx.clone();

        self.handle = Some(std::thread::spawn(move || {
            log::trace!(target: LOG_TAG, "Main Thread started");

            while let Ok(signal) = rx.recv() {
                match signal {
                    TimerSignal::NextSnapshot(until) => {
                        log::trace!(target: LOG_TAG, "Sending session {}", until);

                        // Generate report from backend
                        let report = backend
                            .lock()?
                            .as_mut()
                            .ok_or_else(|| {
                                PyroscopeError::AdHoc(
                                    "PyroscopeAgent - Failed to unwrap backend".to_string(),
                                )
                            })?
                            .report()?;

                        // Send new Session to SessionManager
                        stx.send(SessionSignal::Session(Box::new(Session::new(
                            until,
                            config.clone(),
                            report,
                        )?)))?
                    }
                    TimerSignal::Terminate => {
                        log::trace!(target: LOG_TAG, "Session Killed");

                        // Notify the Stop function
                        let (lock, cvar) = &*pair;
                        let mut running = lock.lock()?;
                        *running = false;
                        cvar.notify_one();

                        // Kill the internal thread
                        return Ok(());
                    }
                }
            }
            Ok(())
        }));

        Ok(self.transition())
    }
}

impl PyroscopeAgent<PyroscopeAgentRunning> {
    /// Stop the agent. The agent will stop profiling and send a last report to the server.
    ///
    /// # Example
    /// ```ignore
    /// let agent = PyroscopeAgent::builder("http://localhost:8080", "my-app").build()?;
    /// let agent_running = agent.start()?;
    /// // Expensive operation
    /// let agent_ready = agent_running.stop();
    /// ```
    pub fn stop(mut self) -> Result<PyroscopeAgent<PyroscopeAgentReady>> {
        log::debug!(target: LOG_TAG, "Stopping");
        // get tx and send termination signal
        if let Some(sender) = self.tx.take() {
            // Send last session
            sender.send(TimerSignal::NextSnapshot(get_time_range(0)?.until))?;
            // Terminate PyroscopeAgent internal thread
            sender.send(TimerSignal::Terminate)?;
        } else {
            log::error!("PyroscopeAgent - Missing sender")
        }

        // Wait for the Thread to finish
        let pair = Arc::clone(&self.running);
        let (lock, cvar) = &*pair;
        let _guard = cvar.wait_while(lock.lock()?, |running| *running)?;

        Ok(self.transition())
    }

    /// Return a tuple of functions to add and remove tags to the agent across
    /// thread boundaries. This function can be called multiple times.
    ///
    /// # Example
    /// ```ignore
    /// let agent = PyroscopeAgent::builder("http://localhost:8080", "my-app").build()?;
    /// let agent_running = agent.start()?;
    /// let (add_tag, remove_tag) = agent_running.tag_wrapper();
    /// ```
    ///
    /// The functions can be later called from any thread.
    ///
    /// # Example
    /// ```ignore
    /// add_tag("key".to_string(), "value".to_string());
    /// // some computation
    /// remove_tag("key".to_string(), "value".to_string());
    /// ```
    #[allow(clippy::type_complexity)]
    pub fn tag_wrapper(
        &self,
    ) -> (
        impl Fn(String, String) -> Result<()>,
        impl Fn(String, String) -> Result<()>,
    ) {
        let backend_add = self.backend.backend.clone();
        let backend_remove = self.backend.backend.clone();

        (
            move |key, value| {
                // https://github.com/tikv/pprof-rs/blob/01cff82dbe6fe110a707bf2b38d8ebb1d14a18f8/src/profiler.rs#L405
                let thread_id = crate::utils::ThreadId::pthread_self();
                let rule = ThreadTag::new(thread_id, Tag::new(key, value));
                let backend = backend_add.lock()?;
                backend
                    .as_ref()
                    .ok_or_else(|| {
                        PyroscopeError::AdHoc(
                            "PyroscopeAgent - Failed to unwrap backend".to_string(),
                        )
                    })?
                    .add_tag(rule)?;

                Ok(())
            },
            move |key, value| {
                // https://github.com/tikv/pprof-rs/blob/01cff82dbe6fe110a707bf2b38d8ebb1d14a18f8/src/profiler.rs#L405
                let thread_id = crate::utils::ThreadId::pthread_self();
                let rule = ThreadTag::new(thread_id, Tag::new(key, value));
                let backend = backend_remove.lock()?;
                backend
                    .as_ref()
                    .ok_or_else(|| {
                        PyroscopeError::AdHoc(
                            "PyroscopeAgent - Failed to unwrap backend".to_string(),
                        )
                    })?
                    .remove_tag(rule)?;

                Ok(())
            },
        )
    }

    /// Add a thread Tag rule to the backend Ruleset. For tagging, it's
    /// recommended to use the `tag_wrapper` function.
    pub fn add_thread_tag(&self, thread_id: crate::utils::ThreadId, tag: Tag) -> Result<()> {
        let rule = ThreadTag::new(thread_id, tag);
        self.backend.add_tag(rule)?;

        Ok(())
    }

    /// Remove a thread Tag rule from the backend Ruleset. For tagging, it's
    /// recommended to use the `tag_wrapper` function.
    pub fn remove_thread_tag(&self, thread_id: crate::utils::ThreadId, tag: Tag) -> Result<()> {
        let rule = ThreadTag::new(thread_id, tag);
        self.backend.remove_tag(rule)?;

        Ok(())
    }
}

pub fn parse_http_headers_json(http_headers_json: String) -> Result<HashMap<String, String>> {
    let mut http_headers = HashMap::new();
    let parsed: serde_json::Value = serde_json::from_str(&http_headers_json)?;
    let parsed = parsed
        .as_object()
        .ok_or_else(|| PyroscopeError::AdHoc(format!("expected object, got {}", parsed)))?;
    for (k, v) in parsed {
        if let Some(value) = v.as_str() {
            http_headers.insert(k.to_string(), value.to_string());
        } else {
            return Err(PyroscopeError::AdHoc(format!(
                "invalid http header value, not a string: {}",
                v
            )));
        }
    }
    Ok(http_headers)
}

pub fn parse_vec_string_json(s: String) -> Result<Vec<String>> {
    let parsed: serde_json::Value = serde_json::from_str(&s)?;
    let parsed = parsed
        .as_array()
        .ok_or_else(|| PyroscopeError::AdHoc(format!("expected array, got {}", parsed)))?;
    let mut res = Vec::with_capacity(parsed.len());
    for v in parsed {
        if let Some(s) = v.as_str() {
            res.push(s.to_string());
        } else {
            return Err(PyroscopeError::AdHoc(format!(
                "invalid element value, not a string: {}",
                v
            )));
        }
    }
    Ok(res)
}
```

## File: `src/session.rs`
```rust
use std::{
    io::Write,
    sync::mpsc::{sync_channel, Receiver, SyncSender},
    thread::{self, JoinHandle},
    time::Duration,
};

use crate::encode::gen::push::{PushRequest, RawProfileSeries, RawSample};
use crate::encode::gen::types::LabelPair;
use crate::{
    backend::{Report, ReportBatch, ReportData},
    encode::pprof,
    pyroscope::PyroscopeConfig,
    utils::get_time_range,
    Result,
};
use libflate::gzip::Encoder;
use prost::Message;
use reqwest::Url;
use uuid::Uuid;

const LOG_TAG: &str = "Pyroscope::Session";

/// Session Signal
///
/// This enum is used to send data to the session thread. It can also kill the session thread.
pub enum SessionSignal {
    /// Send session data to the session thread.
    Session(Box<Session>),
    /// Kill the session thread.
    Kill,
}

/// Manage sessions and send data to the server.
#[derive(Debug)]
pub struct SessionManager {
    /// The SessionManager thread.
    pub handle: Option<JoinHandle<Result<()>>>,
    /// Channel to send data to the SessionManager thread.
    pub tx: SyncSender<SessionSignal>,
}

impl SessionManager {
    /// Create a new SessionManager
    pub fn new() -> Result<Self> {
        log::info!(target: LOG_TAG, "Creating SessionManager");

        // Create a channel for sending and receiving sessions
        let (tx, rx): (SyncSender<SessionSignal>, Receiver<SessionSignal>) = sync_channel(10);

        // Create a thread for the SessionManager
        let handle = Some(thread::spawn(move || {
            log::trace!(target: LOG_TAG, "Started");
            let client = reqwest::blocking::Client::new();
            while let Ok(signal) = rx.recv() {
                match signal {
                    SessionSignal::Session(session) => {
                        // Send the session
                        // Matching is done here (instead of ?) to avoid breaking
                        // the SessionManager thread if the server is not available.
                        match (*session).push(&client) {
                            Ok(_) => log::trace!("SessionManager - Session sent"),
                            Err(e) => log::error!("SessionManager - Failed to send session: {}", e),
                        }
                    }
                    SessionSignal::Kill => {
                        // Kill the session manager
                        log::trace!(target: LOG_TAG, "Kill signal received");
                        return Ok(());
                    }
                }
            }
            Ok(())
        }));

        Ok(SessionManager { handle, tx })
    }

    /// Push a new session into the SessionManager
    pub fn push(&self, session: SessionSignal) -> Result<()> {
        // Push the session into the SessionManager
        self.tx.send(session)?;

        log::trace!(target: LOG_TAG, "SessionSignal pushed");

        Ok(())
    }
}

pub struct Session {
    pub config: PyroscopeConfig,
    pub batch: ReportBatch,
    // unix time todo remove comment, use types
    pub from: u64,
    // unix time todo remove comment, use types
    pub until: u64,
}

impl Session {
    /// Create a new Session
    /// # Example
    /// ```ignore
    /// let config = PyroscopeConfig::new("https://localhost:8080", "my-app", 100, "pyspy", "0.8.16");
    /// let report = vec![1, 2, 3];
    /// let until = 154065120;
    /// let session = Session::new(until, config, report)?;
    /// ```
    pub fn new(until: u64, config: PyroscopeConfig, batch: ReportBatch) -> Result<Self> {
        log::info!(target: LOG_TAG, "Creating Session");

        // get_time_range should be used with "from". We balance this by reducing
        // 10s from the returned range.
        let time_range = get_time_range(until)?;

        Ok(Self {
            config,
            batch,
            from: time_range.from - 10,
            until: time_range.until - 10,
        })
    }

    fn push(self, client: &reqwest::blocking::Client) -> Result<()> {
        log::info!(target: LOG_TAG, "Sending Session: {} - {}", self.from, self.until);

        let ReportBatch { profile_type, data } = self.batch;

        let raw_profile = match data {
            ReportData::RawPprof(pprof_bytes) => {
                if self.config.func.is_some() {
                    log::warn!(target: LOG_TAG, "report transform function is not supported with raw pprof backends (e.g. jemalloc)");
                }
                pprof_bytes
            }
            ReportData::Reports(reports) => {
                let transformed: Vec<Report>;
                let encode_input = match self.config.func {
                    None => &reports,
                    Some(f) => {
                        transformed = reports.iter().map(|r| f(r.to_owned())).collect();
                        &transformed
                    }
                };
                pprof::encode(
                    encode_input,
                    self.config.sample_rate,
                    self.from * 1_000_000_000,
                    (self.until - self.from) * 1_000_000_000,
                )
                .encode_to_vec()
            }
        };

        let mut labels: Vec<LabelPair> = Vec::with_capacity(2 + self.config.tags.len());
        labels.push(LabelPair {
            name: "service_name".to_string(),
            value: self.config.application_name.clone(),
        });
        labels.push(LabelPair {
            name: "__name__".to_string(),
            value: profile_type,
        });
        for tag in self.config.tags {
            labels.push(LabelPair {
                name: tag.0,
                value: tag.1,
            })
        }
        let req = PushRequest {
            series: vec![RawProfileSeries {
                labels,
                samples: vec![RawSample {
                    raw_profile,
                    id: Uuid::new_v4().to_string(),
                }],
            }],
        };

        let req = Self::gzip(&req.encode_to_vec())?;

        let mut url = Url::parse(&self.config.url)?;
        url.path_segments_mut()
            .unwrap()
            .push("push.v1.PusherService")
            .push("Push");

        let mut req_builder = client
            .post(url.as_str())
            .header(
                "User-Agent",
                format!(
                    "pyroscope-rs/{}/{} reqwest",
                    self.config.spy_name, self.config.spy_version
                ),
            )
            .header("Content-Type", "application/proto")
            .header("Content-Encoding", "gzip");

        if let Some(basic_auth) = &self.config.basic_auth {
            req_builder = req_builder.basic_auth(
                basic_auth.username.clone(),
                Some(basic_auth.password.clone()),
            );
        }
        if let Some(tenant_id) = &self.config.tenant_id {
            req_builder = req_builder.header("X-Scope-OrgID", tenant_id);
        }
        for (k, v) in &self.config.http_headers {
            req_builder = req_builder.header(k, v);
        }

        let mut response = req_builder
            .body(req)
            .timeout(Duration::from_secs(10))
            .send()?;

        let status = response.status();

        if status.is_success() {
            let mut sink = std::io::sink();
            _ = response.copy_to(&mut sink);
        } else {
            let resp = response.text();
            let resp = match &resp {
                Ok(t) => t,
                Err(_) => "",
            };
            log::error!(target: LOG_TAG, "Sending Session failed {} {}", status.as_u16(), resp);
        }
        Ok(())
    }

    fn gzip(report: &[u8]) -> Result<Vec<u8>> {
        let mut encoder = Encoder::new(Vec::new())?;
        encoder.write_all(report)?;
        let compressed_data = encoder.finish().into_result()?;
        Ok(compressed_data)
    }
}
```

## File: `src/utils.rs`
```rust
use std::fmt;

use crate::{error::Result, PyroscopeError};

/// Error Wrapper for libc return. Only check for errors.
pub fn check_err<T: Ord + Default>(num: T) -> Result<T> {
    if num < T::default() {
        return Err(PyroscopeError::from(std::io::Error::last_os_error()));
    }
    Ok(num)
}

#[cfg(test)]
mod check_err_tests {
    use crate::utils::check_err;

    #[test]
    fn check_err_success() {
        assert_eq!(check_err(1).unwrap(), 1)
    }

    #[test]
    fn check_err_error() {
        assert!(check_err(-1).is_err())
    }
}

#[derive(Debug, Eq, PartialEq, Hash, Clone)]
pub struct ThreadId {
    pthread: libc::pthread_t,
}

// SAFETY: pthread_t is an opaque thread identifier used as a handle,
// never dereferenced. On musl it's *mut c_void, on glibc it's c_ulong.
unsafe impl Send for ThreadId {}
unsafe impl Sync for ThreadId {}

impl From<libc::pthread_t> for ThreadId {
    fn from(value: libc::pthread_t) -> Self {
        Self { pthread: value }
    }
}
impl ThreadId {
    pub fn pthread_self() -> Self {
        Self {
            pthread: unsafe { libc::pthread_self() },
        }
    }
}

impl fmt::Display for ThreadId {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{}", self.pthread as usize)
    }
}

/// Return the current time in seconds.
pub fn get_current_time_secs() -> Result<u64> {
    Ok(std::time::SystemTime::now()
        .duration_since(std::time::UNIX_EPOCH)?
        .as_secs())
}

#[cfg(test)]
mod get_current_time_secs_tests {
    use crate::utils::get_current_time_secs;

    #[test]
    fn get_current_time_secs_success() {
        assert!(get_current_time_secs().is_ok())
    }
}

/// A representation of a time range. The time range is represented by a start
/// time, an end time, a current time and remaining time in seconds. The
/// remaining time is the duration in seconds until the end time.
#[derive(Debug, PartialEq)]
pub struct TimeRange {
    pub from: u64,
    pub until: u64,
    pub current: u64,
    pub rem: u64,
}

/// Return a range of timestamps in the form [start, end).
/// The range is inclusive of start and exclusive of end.
pub fn get_time_range(timestamp: u64) -> Result<TimeRange> {
    // if timestamp is 0, then get the current time
    if timestamp == 0 {
        return get_time_range(get_current_time_secs()?);
    }

    // Determine the start and end of the range
    Ok(TimeRange {
        from: timestamp / 10 * 10,
        until: timestamp / 10 * 10 + 10,
        current: timestamp,
        rem: 10 - (timestamp % 10),
    })
}

#[cfg(test)]
mod get_time_range_tests {
    use crate::utils::{get_time_range, TimeRange};

    #[test]
    fn get_time_range_verify() {
        assert_eq!(
            get_time_range(1644194479).unwrap(),
            TimeRange {
                from: 1644194470,
                until: 1644194480,
                current: 1644194479,
                rem: 1,
            }
        );
        assert_eq!(
            get_time_range(1644194470).unwrap(),
            TimeRange {
                from: 1644194470,
                until: 1644194480,
                current: 1644194470,
                rem: 10,
            }
        );
        assert_eq!(
            get_time_range(1644194476).unwrap(),
            TimeRange {
                from: 1644194470,
                until: 1644194480,
                current: 1644194476,
                rem: 4,
            }
        );
    }
}
```

## File: `src/backend/backend.rs`
```rust
#![allow(clippy::module_inception)]

use crate::error::{PyroscopeError, Result};
use std::{
    fmt::Debug,
    sync::{Arc, Mutex},
};

use super::{ReportBatch, ThreadTag};

/// Backend Config
#[derive(Debug, Copy, Clone, Default)]
pub struct BackendConfig {
    pub report_thread_id: bool,
    pub report_thread_name: bool,
    pub report_pid: bool,
}

/// Backend Trait
pub trait Backend: Send {
    /// Initialize the backend.
    fn initialize(&mut self) -> Result<()>;
    /// Drop the backend.
    fn shutdown(self: Box<Self>) -> Result<()>;
    /// Generate profiling report
    fn report(&mut self) -> Result<ReportBatch>;
    fn add_tag(&self, tag: ThreadTag) -> Result<()>;
    fn remove_tag(&self, tag: ThreadTag) -> Result<()>;
}

/// Marker struct for Empty BackendImpl
#[derive(Debug)]
pub struct BackendBare;

/// Marker struct for Uninitialized Backend
#[derive(Debug)]
pub struct BackendUninitialized;

/// Marker struct for Initialized Backend
#[derive(Debug)]
pub struct BackendReady;

/// Backend State Trait
pub trait BackendState {}
impl BackendState for BackendBare {}
impl BackendState for BackendUninitialized {}
impl BackendState for BackendReady {}

/// Backend Accessibility Trait
pub trait BackendAccessible: BackendState {}
impl BackendAccessible for BackendUninitialized {}
impl BackendAccessible for BackendReady {}

/// Precursor Backend Implementation
/// This struct is used to implement the Backend trait. It serves two purposes:
/// 1. It enforces state transitions using the Type System.
/// 2. It manages the lifetime of the backend through an Arc<Mutex<T>>.
pub struct BackendImpl<S: BackendState + ?Sized> {
    /// Backend
    pub backend: Arc<Mutex<Option<Box<dyn Backend>>>>,

    /// Backend State
    _state: std::marker::PhantomData<S>,
}

impl BackendImpl<BackendBare> {
    /// Create a new BackendImpl instance
    pub fn new(backend_box: Box<dyn Backend>) -> BackendImpl<BackendUninitialized> {
        BackendImpl {
            backend: Arc::new(Mutex::new(Some(backend_box))),
            _state: std::marker::PhantomData,
        }
    }
}

impl BackendImpl<BackendUninitialized> {
    /// Initialize the backend
    pub fn initialize(self) -> Result<BackendImpl<BackendReady>> {
        let backend = self.backend.clone();

        // Initialize the backend
        backend
            .lock()?
            .as_mut()
            .ok_or(PyroscopeError::BackendImpl)?
            .initialize()?;

        // Transition to BackendReady
        Ok(BackendImpl {
            backend,
            _state: std::marker::PhantomData,
        })
    }
}

impl<S: BackendAccessible> BackendImpl<S> {
    pub fn add_tag(&self, tag: ThreadTag) -> Result<()> {
        self.backend
            .lock()?
            .as_ref()
            .ok_or(PyroscopeError::BackendImpl)?
            .add_tag(tag)
    }

    pub fn remove_tag(&self, rule: ThreadTag) -> Result<()> {
        self.backend
            .lock()?
            .as_ref()
            .ok_or(PyroscopeError::BackendImpl)?
            .remove_tag(rule)
    }
}

impl BackendImpl<BackendReady> {
    /// Shutdown the backend and destroy BackendImpl
    pub fn shutdown(self) -> Result<()> {
        self.backend
            .lock()?
            .take()
            .ok_or(PyroscopeError::BackendImpl)?
            .shutdown()?;

        Ok(())
    }

    /// Generate profiling report
    pub fn report(&mut self) -> Result<ReportBatch> {
        self.backend
            .lock()?
            .as_mut()
            .ok_or(PyroscopeError::BackendImpl)?
            .report()
    }
}
```

## File: `src/backend/jemalloc.rs`
```rust
use crate::backend::{
    Backend, BackendImpl, BackendUninitialized, ReportBatch, ReportData, ThreadTag,
};
use crate::error::{PyroscopeError, Result};

const LOG_TAG: &str = "Pyroscope::Jemalloc";

/// Create a jemalloc memory profiling backend.
///
/// # Example
///
/// ```ignore
/// use pyroscope::PyroscopeAgent;
/// use pyroscope::backend::jemalloc::jemalloc_backend;
///
/// let agent = PyroscopeAgent::builder("http://localhost:4040", "my-app")
///     .backend(jemalloc_backend())
///     .build()?;
/// agent.start()?;
/// ```
pub fn jemalloc_backend() -> BackendImpl<BackendUninitialized> {
    BackendImpl::new(Box::new(Jemalloc))
}

#[derive(Debug)]
struct Jemalloc;

impl Backend for Jemalloc {
    fn initialize(&mut self) -> Result<()> {
        let prof_ctl = jemalloc_pprof::PROF_CTL.as_ref().ok_or_else(|| {
            PyroscopeError::new(
                "jemalloc: PROF_CTL not available. Ensure jemalloc is configured with prof:true",
            )
        })?;
        let guard = prof_ctl.try_lock().map_err(|_| {
            PyroscopeError::new(
                "jemalloc: failed to acquire PROF_CTL lock during initialization. \
                 This is unexpected at startup; ensure no other code holds the lock.",
            )
        })?;
        if !guard.activated() {
            return Err(PyroscopeError::new(
                "jemalloc: profiling is not activated. Ensure malloc_conf includes prof:true,prof_active:true",
            ));
        }

        log::info!(target: LOG_TAG, "Jemalloc profiling backend initialized");

        Ok(())
    }

    fn shutdown(self: Box<Self>) -> Result<()> {
        log::trace!(target: LOG_TAG, "Shutting down jemalloc backend");
        Ok(())
    }

    fn report(&mut self) -> Result<ReportBatch> {
        let prof_ctl = jemalloc_pprof::PROF_CTL
            .as_ref()
            .ok_or_else(|| PyroscopeError::new("jemalloc: PROF_CTL not available"))?;
        let mut guard = prof_ctl.try_lock().map_err(|_| {
            PyroscopeError::new("jemalloc: failed to acquire PROF_CTL lock for report")
        })?;
        let pprof_data = guard
            .dump_pprof()
            .map_err(|e| PyroscopeError::new(&format!("jemalloc: dump_pprof failed: {}", e)))?;

        Ok(ReportBatch {
            profile_type: "memory".into(),
            data: ReportData::RawPprof(pprof_data),
        })
    }

    fn add_tag(&self, _tag: ThreadTag) -> Result<()> {
        Ok(())
    }

    fn remove_tag(&self, _tag: ThreadTag) -> Result<()> {
        Ok(())
    }
}
```

## File: `src/backend/mod.rs`
```rust
pub mod backend;
#[cfg(feature = "backend-jemalloc")]
pub mod jemalloc;
#[cfg(feature = "backend-pprof-rs")]
pub mod pprof;
pub mod ruleset;
pub mod tests;
pub mod types;

pub use backend::*;
#[cfg(feature = "backend-jemalloc")]
pub use jemalloc::*;
#[cfg(feature = "backend-pprof-rs")]
pub use pprof::*;
pub use ruleset::*;
pub use types::*;
```

## File: `src/backend/pprof.rs`
```rust
use crate::backend::{
    Backend, BackendConfig, BackendImpl, BackendUninitialized, Report, ReportBatch, ReportData,
    StackBuffer, StackFrame, StackTrace, ThreadTag, ThreadTagsSet,
};
use crate::error::{PyroscopeError, Result};
use pprof::{ProfilerGuard, ProfilerGuardBuilder};
use std::{
    collections::HashMap,
    ffi::OsStr,
    ops::Deref,
    sync::{Arc, Mutex},
};

const LOG_TAG: &str = "Pyroscope::Pprofrs";

pub fn pprof_backend(
    config: PprofConfig,
    backend_config: BackendConfig,
) -> BackendImpl<BackendUninitialized> {
    BackendImpl::new(Box::new(Pprof::new(config, backend_config)))
}

#[derive(Debug)]
pub struct PprofConfig {
    pub sample_rate: u32,
}

impl Default for PprofConfig {
    fn default() -> Self {
        PprofConfig { sample_rate: 100 }
    }
}

#[derive(Default)]
pub struct Pprof<'a> {
    buffer: Arc<Mutex<StackBuffer>>,
    config: PprofConfig,
    backend_config: BackendConfig,
    inner_builder: Arc<Mutex<Option<ProfilerGuardBuilder>>>,
    guard: Arc<Mutex<Option<ProfilerGuard<'a>>>>,
    ruleset: ThreadTagsSet,
}

impl std::fmt::Debug for Pprof<'_> {
    fn fmt(&self, fmt: &mut std::fmt::Formatter<'_>) -> std::result::Result<(), std::fmt::Error> {
        write!(fmt, "Pprof Backend")
    }
}

impl<'a> Pprof<'a> {
    pub fn new(config: PprofConfig, backend_config: BackendConfig) -> Self {
        Pprof {
            buffer: Arc::new(Mutex::new(StackBuffer::default())),
            config,
            backend_config,
            inner_builder: Arc::new(Mutex::new(None)),
            guard: Arc::new(Mutex::new(None)),
            ruleset: ThreadTagsSet::default(),
        }
    }
}

impl Backend for Pprof<'_> {
    fn shutdown(self: Box<Self>) -> Result<()> {
        log::trace!(target: LOG_TAG, "Shutting down sampler thread");
        Ok(())
    }

    fn initialize(&mut self) -> Result<()> {
        let profiler = ProfilerGuardBuilder::default().frequency(self.config.sample_rate as i32);

        *self.inner_builder.lock()? = Some(profiler);

        *self.guard.lock()? = Some(
            self.inner_builder
                .lock()?
                .as_ref()
                .ok_or_else(|| PyroscopeError::new("pprof-rs: ProfilerGuardBuilder error"))?
                .clone()
                .build()
                .map_err(|e| PyroscopeError::new(e.to_string().as_str()))?,
        );

        Ok(())
    }

    fn report(&mut self) -> Result<ReportBatch> {
        self.dump_report()?;

        let buffer = self.buffer.clone();

        let report: StackBuffer = buffer.lock()?.deref().to_owned();

        let reports: Vec<Report> = report.into();

        buffer.lock()?.clear();

        Ok(ReportBatch {
            profile_type: "process_cpu".into(),
            data: ReportData::Reports(reports),
        })
    }

    fn add_tag(&self, tag: ThreadTag) -> Result<()> {
        if self.guard.lock()?.as_ref().is_some() {
            self.dump_report()?;
        }

        self.ruleset.add(tag)?;

        Ok(())
    }

    fn remove_tag(&self, tag: ThreadTag) -> Result<()> {
        if self.guard.lock()?.as_ref().is_some() {
            self.dump_report()?;
        }

        self.ruleset.remove(tag)?;

        Ok(())
    }
}

impl Pprof<'_> {
    /// Workaround for pprof-rs to interrupt the profiler.
    pub fn dump_report(&self) -> Result<()> {
        let report = self
            .guard
            .lock()?
            .as_ref()
            .ok_or_else(|| PyroscopeError::new("pprof-rs: ProfilerGuard report error"))?
            .report()
            .build()
            .map_err(|e| PyroscopeError::new(e.to_string().as_str()))?;

        let stack_buffer = Into::<StackBuffer>::into(Into::<StackBufferWrapper>::into((
            report,
            &self.backend_config,
        )));

        let data: HashMap<StackTrace, usize> = stack_buffer
            .data
            .iter()
            .map(|(stacktrace, ss)| {
                let stacktrace = stacktrace.to_owned().add_tag_rules(&self.ruleset);
                (stacktrace, ss.to_owned())
            })
            .collect();

        let buffer = self.buffer.clone();

        for (stacktrace, count) in data {
            buffer.lock()?.record_with_count(stacktrace, count)?;
        }

        self.reset()?;

        Ok(())
    }

    pub fn reset(&self) -> Result<()> {
        drop(self.guard.lock()?.take());

        *self.guard.lock()? = Some(
            self.inner_builder
                .lock()?
                .as_ref()
                .ok_or_else(|| PyroscopeError::new("pprof-rs: ProfilerGuardBuilder error"))?
                .clone()
                .build()
                .map_err(|e| PyroscopeError::new(e.to_string().as_str()))?,
        );

        Ok(())
    }
}

struct StackBufferWrapper(StackBuffer);

impl From<StackBufferWrapper> for StackBuffer {
    fn from(stackbuffer: StackBufferWrapper) -> Self {
        stackbuffer.0
    }
}

impl From<(pprof::Report, &BackendConfig)> for StackBufferWrapper {
    fn from(arg: (pprof::Report, &BackendConfig)) -> Self {
        let (report, config) = arg;
        let buffer_data: HashMap<StackTrace, usize> = report
            .data
            .iter()
            .map(|(key, value)| {
                (
                    Into::<StackTraceWrapper>::into((key.to_owned(), config)).into(),
                    value.to_owned() as usize,
                )
            })
            .collect();
        StackBufferWrapper(StackBuffer::new(buffer_data))
    }
}

struct StackTraceWrapper(StackTrace);

impl From<StackTraceWrapper> for StackTrace {
    fn from(stack_trace: StackTraceWrapper) -> Self {
        stack_trace.0
    }
}

impl From<(pprof::Frames, &BackendConfig)> for StackTraceWrapper {
    fn from(arg: (pprof::Frames, &BackendConfig)) -> Self {
        let (frames, config) = arg;
        let thread_id = frames.thread_id as libc::pthread_t;
        StackTraceWrapper(StackTrace::new(
            config,
            None,
            Some(thread_id.into()),
            Some(frames.thread_name),
            frames
                .frames
                .concat()
                .iter()
                .map(|frame| Into::<StackFrameWrapper>::into(frame.to_owned()).into())
                .collect(),
        ))
    }
}

struct StackFrameWrapper(StackFrame);

impl From<StackFrameWrapper> for StackFrame {
    fn from(stack_frame: StackFrameWrapper) -> Self {
        stack_frame.0
    }
}

impl From<pprof::Symbol> for StackFrameWrapper {
    fn from(symbol: pprof::Symbol) -> Self {
        StackFrameWrapper(StackFrame::new(
            None,
            Some(symbol.name()),
            Some(
                symbol
                    .filename
                    .clone()
                    .unwrap_or_default()
                    .file_name()
                    .unwrap_or_else(|| OsStr::new(""))
                    .to_str()
                    .unwrap_or("")
                    .to_string(),
            ),
            Some(
                symbol
                    .filename
                    .unwrap_or_default()
                    .to_str()
                    .unwrap_or("")
                    .to_string(),
            ),
            None,
            symbol.lineno,
        ))
    }
}
```

## File: `src/backend/ruleset.rs`
```rust
use super::{StackTrace, Tag};
use crate::error::Result;
use std::collections::HashSet;
use std::sync::{Arc, Mutex};

#[derive(Debug, Eq, PartialEq, Hash, Clone)]
pub struct ThreadTag {
    tid: crate::utils::ThreadId,
    tag: Tag,
}

impl ThreadTag {
    pub fn new(tid: crate::ThreadId, tag: Tag) -> Self {
        Self { tid, tag }
    }
}

#[derive(Debug, Default, Clone)]
pub struct ThreadTagsSet {
    pub rules: Arc<Mutex<HashSet<ThreadTag>>>,
}

impl ThreadTagsSet {
    pub fn new() -> Self {
        Self {
            rules: Arc::new(Mutex::new(HashSet::new())),
        }
    }

    pub fn add(&self, rule: ThreadTag) -> Result<bool> {
        let rules = self.rules.clone();

        let insert = rules.lock()?.insert(rule);

        Ok(insert)
    }

    pub fn remove(&self, rule: ThreadTag) -> Result<bool> {
        let rules = self.rules.clone();

        let remove = rules.lock()?.remove(&rule);

        Ok(remove)
    }

    #[cfg(test)]
    pub fn thread_tags(&self, tid: crate::ThreadId) -> Vec<Tag> {
        let s = StackTrace {
            pid: None,
            thread_id: Some(tid.clone()),
            thread_name: None,
            frames: vec![],
            metadata: Default::default(),
        };
        let tags: Vec<Tag> = s.add_tag_rules(self).metadata.tags.into_iter().collect();
        tags
    }
}

impl StackTrace {
    pub fn add_tag_rules(self, other: &ThreadTagsSet) -> Self {
        let mut metadata = self.metadata;

        if let Ok(rules) = other.rules.lock() {
            rules.iter().for_each(|rule| {
                if let Some(stack_thread_id) = &self.thread_id {
                    if rule.tid == *stack_thread_id {
                        metadata.add_tag(rule.tag.clone());
                    }
                }
            })
        }

        Self {
            pid: self.pid,
            thread_id: self.thread_id,
            thread_name: self.thread_name,
            frames: self.frames,
            metadata,
        }
    }
}
```

## File: `src/backend/tests.rs`
```rust
#[cfg(test)]
use crate::backend::{
    BackendConfig, Report, StackBuffer, StackFrame, StackTrace, Tag, ThreadTag, ThreadTagsSet,
};
#[cfg(test)]
use std::collections::{HashMap, HashSet};

#[test]
fn test_stack_frame_display() {
    let frame = StackFrame::new(
        Some("module".to_string()),
        Some("name".to_string()),
        Some("filename".to_string()),
        Some("relative_path".to_string()),
        Some("absolute_path".to_string()),
        Some(1),
    );

    assert_eq!(format!("{}", frame), "filename:1 - name");
}

#[test]
fn test_stack_trace_display() {
    let frames = vec![
        StackFrame::new(
            Some("module".to_string()),
            Some("name".to_string()),
            Some("filename".to_string()),
            Some("relative_path".to_string()),
            Some("absolute_path".to_string()),
            Some(1),
        ),
        StackFrame::new(
            Some("module".to_string()),
            Some("name".to_string()),
            Some("filename".to_string()),
            Some("relative_path".to_string()),
            Some("absolute_path".to_string()),
            Some(2),
        ),
    ];

    let stack_trace = StackTrace::new(&BackendConfig::default(), None, None, None, frames);

    assert_eq!(
        format!("{}", stack_trace),
        "filename:2 - name;filename:1 - name"
    );
}

#[test]
fn test_report_record() {
    let mut report = Report::new(HashMap::new());

    let stack_trace = StackTrace::new(&BackendConfig::default(), None, None, None, vec![]);

    report.record(stack_trace);
    assert_eq!(report.data.len(), 1);
}

#[test]
fn test_tag_new() {
    let tag = Tag::new("key".to_string(), "value".to_string());

    assert_eq!(tag.key, "key");
    assert_eq!(tag.value, "value");
}

#[test]
fn test_rule_new() {
    let tid = crate::ThreadId::pthread_self();
    let rule = ThreadTag::new(
        tid.clone(),
        Tag::new("key".to_string(), "value".to_string()),
    );

    assert_eq!(
        rule,
        ThreadTag::new(tid, Tag::new("key".to_string(), "value".to_string()))
    );
}

#[cfg(test)]
fn test_thread_id(v: u64) -> crate::utils::ThreadId {
    (v as libc::pthread_t).into()
}

#[test]
fn test_ruleset_new() {
    let ruleset = ThreadTagsSet::new();

    assert_eq!(ruleset.rules.lock().unwrap().len(), 0);
}

#[test]
fn test_ruleset_add_rule() {
    let tid = crate::ThreadId::pthread_self();
    let ruleset = ThreadTagsSet::new();

    let rule = ThreadTag::new(tid, Tag::new("key".to_string(), "value".to_string()));

    ruleset.add(rule).unwrap();

    assert_eq!(ruleset.rules.lock().unwrap().len(), 1);
}

#[test]
fn test_ruleset_remove_rule() {
    let tid = crate::ThreadId::pthread_self();
    let ruleset = ThreadTagsSet::new();

    let add_rule = ThreadTag::new(
        tid.clone(),
        Tag::new("key".to_string(), "value".to_string()),
    );

    ruleset.add(add_rule).unwrap();

    assert_eq!(ruleset.rules.lock().unwrap().len(), 1);

    let remove_rule = ThreadTag::new(tid, Tag::new("key".to_string(), "value".to_string()));

    ruleset.remove(remove_rule).unwrap();

    assert_eq!(ruleset.rules.lock().unwrap().len(), 0);
}

#[test]
fn test_ruleset() {
    let ruleset = ThreadTagsSet::new();

    ruleset
        .add(ThreadTag::new(
            test_thread_id(1),
            Tag::new("key1".to_string(), "value".to_string()),
        ))
        .unwrap();

    ruleset
        .add(ThreadTag::new(
            test_thread_id(2),
            Tag::new("key1".to_string(), "value".to_string()),
        ))
        .unwrap();

    ruleset
        .add(ThreadTag::new(
            test_thread_id(3),
            Tag::new("key1".to_string(), "value".to_string()),
        ))
        .unwrap();

    // Remove ThreadTag number 2
    ruleset
        .remove(ThreadTag::new(
            test_thread_id(2),
            Tag::new("key1".to_string(), "value".to_string()),
        ))
        .unwrap();

    // Verify ThreadTag number 2 is removed from the ruleset Vector
    assert_eq!(
        ruleset.rules.lock().unwrap().clone(),
        HashSet::from([
            ThreadTag::new(
                test_thread_id(1),
                Tag::new("key1".to_string(), "value".to_string(),)
            ),
            ThreadTag::new(
                test_thread_id(3),
                Tag::new("key1".to_string(), "value".to_string(),)
            )
        ])
    );
}

#[test]
fn test_ruleset_duplicates() {
    let ruleset = ThreadTagsSet::new();

    let tid = crate::ThreadId::pthread_self();
    ruleset
        .add(ThreadTag::new(
            tid.clone(),
            Tag::new("key1".to_string(), "value".to_string()),
        ))
        .unwrap();

    ruleset
        .add(ThreadTag::new(
            tid.clone(),
            Tag::new("key1".to_string(), "value".to_string()),
        ))
        .unwrap();

    assert_eq!(
        ruleset.thread_tags(tid),
        vec![Tag::new("key1".to_string(), "value".to_string())]
    );
}

#[test]
fn test_ruleset_remove_nonexistent() {
    let ruleset = ThreadTagsSet::new();

    let tid = crate::ThreadId::pthread_self();
    ruleset
        .add(ThreadTag::new(
            tid.clone(),
            Tag::new("key1".to_string(), "value".to_string()),
        ))
        .unwrap();

    ruleset
        .remove(ThreadTag::new(
            tid.clone(),
            Tag::new("key2".to_string(), "value".to_string()),
        ))
        .unwrap();

    assert_eq!(
        ruleset.thread_tags(tid),
        vec![Tag::new("key1".to_string(), "value".to_string())]
    );
}

#[test]
fn test_stacktrace_add() {
    let ruleset = ThreadTagsSet::new();

    ruleset
        .add(ThreadTag::new(
            test_thread_id(55),
            Tag::new("keyA".to_string(), "valueA".to_string()),
        ))
        .unwrap();

    ruleset
        .add(ThreadTag::new(
            test_thread_id(100),
            Tag::new("keyB".to_string(), "valueB".to_string()),
        ))
        .unwrap();

    let backend_config = BackendConfig {
        report_pid: true,
        report_thread_id: true,
        report_thread_name: true,
    };

    let stacktrace = StackTrace::new(
        &backend_config,
        Some(1),
        Some(test_thread_id(55)),
        Some("thread_name".to_string()),
        vec![crate::backend::StackFrame::new(
            Some("file1".to_string()),
            Some("function1".to_string()),
            Some("file1".to_string()),
            Some("file1".to_string()),
            Some("file1".to_string()),
            Some(1),
        )],
    );

    // assert initial metadata of the stacktrace
    let mut initial_metadata = crate::backend::Metadata::default();
    initial_metadata.add_tag(Tag::new("pid".to_string(), "1".to_string()));
    initial_metadata.add_tag(Tag::new("thread_id".to_string(), "55".to_string()));
    initial_metadata.add_tag(Tag::new(
        "thread_name".to_string(),
        "thread_name".to_string(),
    ));

    assert_eq!(stacktrace.metadata, initial_metadata);

    // Add the Stacktrace to the Ruleset
    let applied_stacktrace = stacktrace.add_tag_rules(&ruleset);

    initial_metadata.add_tag(Tag::new("keyA".to_string(), "valueA".to_string()));

    // assert that the metadata of the stacktrace is updated
    assert_eq!(applied_stacktrace.metadata, initial_metadata);

    // Re-apply the Ruleset
    let re_applied_stacktrace = applied_stacktrace.add_tag_rules(&ruleset);

    // assert that the metadata of the stacktrace is the same
    assert_eq!(re_applied_stacktrace.metadata, initial_metadata);
}

#[test]
fn test_stackbuffer_record() {
    let mut buffer = StackBuffer::new(HashMap::new());
    let stack_trace = StackTrace::new(
        &BackendConfig::default(),
        None,
        None,
        None,
        vec![StackFrame::new(
            None,
            Some("test_record".to_string()),
            None,
            None,
            None,
            None,
        )],
    );
    // First record
    buffer.record(stack_trace.clone()).unwrap();
    assert_eq!(buffer.data.len(), 1);
    assert_eq!(buffer.data[&stack_trace], 1);

    // Second record
    buffer.record(stack_trace.clone()).unwrap();
    assert_eq!(buffer.data.len(), 1);
    assert_eq!(buffer.data[&stack_trace], 2);
}

#[test]
fn test_stackbuffer_record_with_count() {
    let mut buffer = StackBuffer::new(HashMap::new());
    let stack_trace = StackTrace::new(
        &BackendConfig::default(),
        None,
        None,
        None,
        vec![StackFrame::new(
            None,
            Some("test_record".to_string()),
            None,
            None,
            None,
            None,
        )],
    );
    // First record
    buffer.record_with_count(stack_trace.clone(), 1).unwrap();
    assert_eq!(buffer.data.len(), 1);
    assert_eq!(buffer.data[&stack_trace], 1);

    // Second record
    buffer.record_with_count(stack_trace.clone(), 2).unwrap();
    assert_eq!(buffer.data.len(), 1);
    assert_eq!(buffer.data[&stack_trace], 3);
}

#[test]
fn test_stackbuffer_clear() {
    let mut buffer = StackBuffer::new(HashMap::new());
    let stack_trace = StackTrace::new(
        &BackendConfig::default(),
        None,
        None,
        None,
        vec![StackFrame::new(
            None,
            Some("test_record".to_string()),
            None,
            None,
            None,
            None,
        )],
    );
    // First record
    buffer.record(stack_trace.clone()).unwrap();
    assert_eq!(buffer.data.len(), 1);
    assert_eq!(buffer.data[&stack_trace], 1);

    // Second record
    buffer.record(stack_trace.clone()).unwrap();
    assert_eq!(buffer.data.len(), 1);
    assert_eq!(buffer.data[&stack_trace], 2);

    // Clear
    buffer.clear();
    assert_eq!(buffer.data.len(), 0);
}
```

## File: `src/backend/types.rs`
```rust
use super::BackendConfig;
use crate::error::Result;
use std::{
    collections::{hash_map::DefaultHasher, BTreeSet, HashMap},
    hash::{Hash, Hasher},
};

/// Pyroscope Tag
#[derive(Debug, PartialOrd, Ord, Eq, PartialEq, Hash, Clone)]
pub struct Tag {
    /// Tag key
    pub key: String,
    /// Tag value
    pub value: String,
}

impl Tag {
    /// Create a new Tag
    pub fn new(key: String, value: String) -> Self {
        Self { key, value }
    }
}

impl std::fmt::Display for Tag {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{}={}", self.key, self.value)
    }
}

/// Stack buffer
#[derive(Debug, Default, Clone)]
pub struct StackBuffer {
    /// Buffer data bucket
    pub data: HashMap<StackTrace, usize>,
}

impl StackBuffer {
    /// Create a new StackBuffer with the given data
    pub fn new(data: HashMap<StackTrace, usize>) -> Self {
        Self { data }
    }

    /// Record a new stack trace
    pub fn record(&mut self, stack_trace: StackTrace) -> Result<()> {
        *self.data.entry(stack_trace).or_insert(0) += 1;

        Ok(())
    }

    /// Record a new stack trace with count
    pub fn record_with_count(&mut self, stack_trace: StackTrace, count: usize) -> Result<()> {
        *self.data.entry(stack_trace).or_insert(0) += count;

        Ok(())
    }

    /// Clear the buffer
    pub fn clear(&mut self) {
        self.data.clear();
    }
}

impl From<StackBuffer> for Vec<Report> {
    fn from(stack_buffer: StackBuffer) -> Self {
        stack_buffer
            .data
            .into_iter()
            .fold(
                HashMap::new(),
                |acc: HashMap<usize, Report>, (stacktrace, count): (StackTrace, usize)| {
                    let mut acc = acc;
                    if let Some(report) = acc.get_mut(&stacktrace.metadata.get_id()) {
                        report.record_with_count(stacktrace, count);
                    } else {
                        let report = Report::new(HashMap::new());
                        let report_id = stacktrace.metadata.get_id();
                        let mut report = report.metadata(stacktrace.metadata.clone());
                        report.record_with_count(stacktrace, count);
                        acc.insert(report_id, report);
                    }
                    acc
                },
            )
            .into_values()
            .collect()
    }
}

/// Metdata
/// Metadata attached to a StackTrace or a Report. For now, this is just tags.
#[derive(Debug, Default, Clone, Hash, PartialEq, Eq)]
pub struct Metadata {
    /// Tags
    pub tags: BTreeSet<Tag>,
}

impl Metadata {
    /// Add a tag to the metadata
    pub fn add_tag(&mut self, tag: Tag) {
        self.tags.insert(tag);
    }

    /// Get the id of the metadata. This uses the hash of the Metadata type.
    pub fn get_id(&self) -> usize {
        let mut hasher = DefaultHasher::new();
        self.hash(&mut hasher);
        hasher.finish() as usize
    }
}

/// The payload of a report batch: either structured stack-trace reports
/// (which will be encoded into pprof by the session layer) or pre-encoded
/// pprof bytes produced directly by a backend (e.g. jemalloc).
pub enum ReportData {
    /// Structured stack-trace reports that must be pprof-encoded before sending.
    Reports(Vec<Report>),
    /// Pre-encoded pprof bytes (may already be gzipped). Used by backends
    /// like jemalloc that produce a complete pprof profile directly.
    RawPprof(Vec<u8>),
}

/// A batch of reports with a shared profile type.
pub struct ReportBatch {
    /// Profile type name (e.g. "process_cpu", "memory")
    pub profile_type: String,
    /// Report data in this batch
    pub data: ReportData,
}

/// Report
#[derive(Debug, Default, Clone)]
pub struct Report {
    /// Report StackTraces
    pub data: HashMap<StackTrace, usize>,
    /// Metadata
    pub metadata: Metadata,
}

/// Custom implementation of the Hash trait for Report.
/// Only the metadata is hashed.
impl Hash for Report {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.metadata.hash(state);
    }
}

impl Report {
    /// Create a new Report.
    pub fn new(data: HashMap<StackTrace, usize>) -> Self {
        Self {
            data,
            metadata: Metadata::default(),
        }
    }

    /// Return an iterator over the StackTraces of the Report.
    pub fn iter(&self) -> impl Iterator<Item = (&StackTrace, &usize)> {
        self.data.iter()
    }

    /// Set the metadata of the report.
    pub fn metadata(self, metadata: Metadata) -> Self {
        Self {
            data: self.data,
            metadata,
        }
    }

    pub fn record(&mut self, stack_trace: StackTrace) {
        *self.data.entry(stack_trace).or_insert(0) += 1;
    }

    pub fn record_with_count(&mut self, stack_trace: StackTrace, count: usize) {
        *self.data.entry(stack_trace).or_insert(0) += count;
    }
}

/// StackTrace
/// A representation of a stack trace.
#[derive(Debug, Default, PartialEq, Eq, Hash, Clone)]
pub struct StackTrace {
    /// Process ID
    pub pid: Option<u32>,
    /// Thread ID
    pub thread_id: Option<crate::utils::ThreadId>,
    /// Thread Name
    pub thread_name: Option<String>,
    /// Stack Trace
    pub frames: Vec<StackFrame>,
    /// Metadata
    pub metadata: Metadata,
}

impl std::fmt::Display for StackTrace {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{}",
            &self
                .frames
                .iter()
                .rev()
                .map(|frame| format!("{}", frame))
                .collect::<Vec<_>>()
                .join(";")
        )
    }
}

impl StackTrace {
    /// Create a new StackTrace
    pub fn new(
        config: &BackendConfig,
        pid: Option<u32>,
        thread_id: Option<crate::utils::ThreadId>,
        thread_name: Option<String>,
        frames: Vec<StackFrame>,
    ) -> Self {
        let mut metadata = Metadata::default();

        if config.report_pid {
            if let Some(pid) = pid {
                metadata.add_tag(Tag::new("pid".to_owned(), pid.to_string()));
            }
        }

        if config.report_thread_id {
            if let Some(thread_id) = &thread_id {
                metadata.add_tag(Tag::new("thread_id".to_owned(), thread_id.to_string()));
            }
        }

        if config.report_thread_name {
            if let Some(thread_name) = thread_name.clone() {
                metadata.add_tag(Tag::new("thread_name".to_owned(), thread_name));
            }
        }

        Self {
            pid,
            thread_id,
            thread_name,
            frames,
            metadata,
        }
    }

    /// Return an iterator over the frames of the stacktrace.
    pub fn iter(&self) -> impl Iterator<Item = &StackFrame> {
        self.frames.iter()
    }
}

/// StackFrame
/// A representation of a stack frame.
#[derive(Debug, Default, PartialEq, Eq, Hash, Clone)]
pub struct StackFrame {
    /// Module name
    pub module: Option<String>,
    /// Function name
    pub name: Option<String>,
    /// File name
    pub filename: Option<String>,
    /// File relative path
    pub relative_path: Option<String>,
    /// File absolute path
    pub absolute_path: Option<String>,
    /// Line number
    pub line: Option<u32>,
}

impl StackFrame {
    /// Create a new StackFrame.
    pub fn new(
        module: Option<String>,
        name: Option<String>,
        filename: Option<String>,
        relative_path: Option<String>,
        absolute_path: Option<String>,
        line: Option<u32>,
    ) -> Self {
        Self {
            module,
            name,
            filename,
            relative_path,
            absolute_path,
            line,
        }
    }
}

impl std::fmt::Display for StackFrame {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(
            f,
            "{}:{} - {}",
            self.filename.as_ref().unwrap_or(&"".to_string()),
            self.line.unwrap_or(0),
            self.name.as_ref().unwrap_or(&"".to_string())
        )
    }
}
```

## File: `src/encode/mod.rs`
```rust
pub mod gen;
pub mod pprof;
```

## File: `src/encode/pprof.rs`
```rust
use std::collections::HashMap;

use crate::backend::types::Report;
use crate::encode::gen::google::{Function, Label, Line, Location, Profile, Sample, ValueType};

struct PProfBuilder {
    profile: Profile,
    strings: HashMap<String, i64>,
    functions: HashMap<FunctionMirror, u64>,
    locations: HashMap<LocationMirror, u64>,
}

#[derive(Hash, PartialEq, Eq, Clone)]
pub struct LocationMirror {
    pub function_id: u64,
    pub line: i64,
}

#[derive(Hash, PartialEq, Eq, Clone)]
pub struct FunctionMirror {
    pub name: i64,
    pub filename: i64,
}

impl PProfBuilder {
    fn add_string(&mut self, s: &String) -> i64 {
        let v = self.strings.get(s);
        if let Some(v) = v {
            return *v;
        }
        assert_ne!(self.strings.len(), self.profile.string_table.len() + 1);
        let id: i64 = self.strings.len() as i64;
        self.strings.insert(s.to_owned(), id);
        self.profile.string_table.push(s.to_owned());
        id
    }

    fn add_function(&mut self, fm: FunctionMirror) -> u64 {
        let v = self.functions.get(&fm);
        if let Some(v) = v {
            return *v;
        }
        assert_ne!(self.functions.len(), self.profile.function.len() + 1);
        let id: u64 = self.functions.len() as u64 + 1;
        let f = Function {
            id,
            name: fm.name,
            system_name: 0,
            filename: fm.filename,
            start_line: 0,
        };
        self.functions.insert(fm, id);
        self.profile.function.push(f);
        id
    }

    fn add_location(&mut self, lm: LocationMirror) -> u64 {
        let v = self.locations.get(&lm);
        if let Some(v) = v {
            return *v;
        }
        assert_ne!(self.locations.len(), self.profile.location.len() + 1);
        let id: u64 = self.locations.len() as u64 + 1;
        let l = Location {
            id,
            mapping_id: 0,
            address: 0,
            line: vec![Line {
                function_id: lm.function_id,
                line: lm.line,
            }],
            is_folded: false,
        };
        self.locations.insert(lm, id);
        self.profile.location.push(l);
        id
    }
}

pub fn encode(
    reports: &Vec<Report>,
    sample_rate: u32,
    start_time_nanos: u64,
    duration_nanos: u64,
) -> Profile {
    let mut b = PProfBuilder {
        strings: HashMap::new(),
        functions: HashMap::new(),
        locations: HashMap::new(),
        profile: Profile {
            sample_type: vec![],
            sample: vec![],
            mapping: vec![],
            location: vec![],
            function: vec![],
            string_table: vec![],
            drop_frames: 0,
            keep_frames: 0,
            time_nanos: start_time_nanos as i64,
            duration_nanos: duration_nanos as i64,
            period_type: None,
            period: 0,
            comment: vec![],
            default_sample_type: 0,
        },
    };
    b.add_string(&"".to_string());
    {
        let cpu = b.add_string(&"cpu".to_string());
        let nanoseconds = b.add_string(&"nanoseconds".to_string());
        b.profile.sample_type.push(ValueType {
            r#type: cpu,
            unit: nanoseconds,
        });
        b.profile.period = 1_000_000_000 / sample_rate as i64;
        b.profile.period_type = Some(ValueType {
            r#type: cpu,
            unit: nanoseconds,
        });
    }
    for report in reports {
        for (stacktrace, value) in &report.data {
            let mut sample = Sample {
                location_id: vec![],
                value: vec![*value as i64 * b.profile.period],
                label: vec![],
            };
            for sf in &stacktrace.frames {
                let name = b.add_string(sf.name.as_ref().unwrap_or(&"".to_string()));
                let filename = b.add_string(sf.filename.as_ref().unwrap_or(&"".to_string()));
                let line = sf.line.unwrap_or(0) as i64;
                let function_id = b.add_function(FunctionMirror { name, filename });
                let location_id = b.add_location(LocationMirror { function_id, line });
                sample.location_id.push(location_id);
            }
            let mut labels = HashMap::new();
            for l in &stacktrace.metadata.tags {
                let k = b.add_string(&l.key);
                let v = b.add_string(&l.value);
                labels.insert(k, v);
            }
            for l in &report.metadata.tags {
                let k = b.add_string(&l.key);
                let v = b.add_string(&l.value);
                labels.insert(k, v);
            }
            for (k, v) in &labels {
                sample.label.push(Label {
                    key: *k,
                    str: *v,
                    num: 0,
                    num_unit: 0,
                })
            }
            b.profile.sample.push(sample);
        }
    }
    b.profile
}
```

## File: `src/encode/gen/google.rs`
```rust
// @generated
// This file is @generated by prost-build.
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Profile {
    /// A description of the samples associated with each Sample.value.
    /// For a cpu profile this might be:
    ///    \[["cpu","nanoseconds"]\] or \[["wall","seconds"]\] or \[["syscall","count"]\]
    /// For a heap profile, this might be:
    ///    \[["allocations","count"\], \["space","bytes"]\],
    /// If one of the values represents the number of events represented
    /// by the sample, by convention it should be at index 0 and use
    /// sample_type.unit == "count".
    #[prost(message, repeated, tag = "1")]
    pub sample_type: ::prost::alloc::vec::Vec<ValueType>,
    /// The set of samples recorded in this profile.
    #[prost(message, repeated, tag = "2")]
    pub sample: ::prost::alloc::vec::Vec<Sample>,
    /// Mapping from address ranges to the image/binary/library mapped
    /// into that address range.  mapping\[0\] will be the main binary.
    #[prost(message, repeated, tag = "3")]
    pub mapping: ::prost::alloc::vec::Vec<Mapping>,
    /// Useful program location
    #[prost(message, repeated, tag = "4")]
    pub location: ::prost::alloc::vec::Vec<Location>,
    /// Functions referenced by locations
    #[prost(message, repeated, tag = "5")]
    pub function: ::prost::alloc::vec::Vec<Function>,
    /// A common table for strings referenced by various messages.
    /// string_table\[0\] must always be "".
    #[prost(string, repeated, tag = "6")]
    pub string_table: ::prost::alloc::vec::Vec<::prost::alloc::string::String>,
    /// frames with Function.function_name fully matching the following
    /// regexp will be dropped from the samples, along with their successors.
    ///
    /// Index into string table.
    #[prost(int64, tag = "7")]
    pub drop_frames: i64,
    /// frames with Function.function_name fully matching the following
    /// regexp will be kept, even if it matches drop_frames.
    ///
    /// Index into string table.
    #[prost(int64, tag = "8")]
    pub keep_frames: i64,
    // The following fields are informational, do not affect
    // interpretation of results.
    /// Time of collection (UTC) represented as nanoseconds past the epoch.
    #[prost(int64, tag = "9")]
    pub time_nanos: i64,
    /// Duration of the profile, if a duration makes sense.
    #[prost(int64, tag = "10")]
    pub duration_nanos: i64,
    /// The kind of events between sampled ocurrences.
    /// e.g \[ "cpu","cycles" \] or \[ "heap","bytes" \]
    #[prost(message, optional, tag = "11")]
    pub period_type: ::core::option::Option<ValueType>,
    /// The number of events between sampled occurrences.
    #[prost(int64, tag = "12")]
    pub period: i64,
    /// Freeform text associated to the profile.
    ///
    /// Indices into string table.
    #[prost(int64, repeated, tag = "13")]
    pub comment: ::prost::alloc::vec::Vec<i64>,
    /// Index into the string table of the type of the preferred sample
    /// value. If unset, clients should default to the last sample value.
    #[prost(int64, tag = "14")]
    pub default_sample_type: i64,
}
/// ValueType describes the semantics and measurement units of a value.
#[derive(Clone, Copy, PartialEq, Eq, Hash, ::prost::Message)]
pub struct ValueType {
    /// Index into string table.
    #[prost(int64, tag = "1")]
    pub r#type: i64,
    /// Index into string table.
    #[prost(int64, tag = "2")]
    pub unit: i64,
}
/// Each Sample records values encountered in some program
/// context. The program context is typically a stack trace, perhaps
/// augmented with auxiliary information like the thread-id, some
/// indicator of a higher level request being handled etc.
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Sample {
    /// The ids recorded here correspond to a Profile.location.id.
    /// The leaf is at location_id\[0\].
    #[prost(uint64, repeated, tag = "1")]
    pub location_id: ::prost::alloc::vec::Vec<u64>,
    /// The type and unit of each value is defined by the corresponding
    /// entry in Profile.sample_type. All samples must have the same
    /// number of values, the same as the length of Profile.sample_type.
    /// When aggregating multiple samples into a single sample, the
    /// result has a list of values that is the element-wise sum of the
    /// lists of the originals.
    #[prost(int64, repeated, tag = "2")]
    pub value: ::prost::alloc::vec::Vec<i64>,
    /// label includes additional context for this sample. It can include
    /// things like a thread id, allocation size, etc
    #[prost(message, repeated, tag = "3")]
    pub label: ::prost::alloc::vec::Vec<Label>,
}
#[derive(Clone, Copy, PartialEq, Eq, Hash, ::prost::Message)]
pub struct Label {
    /// Index into string table
    #[prost(int64, tag = "1")]
    pub key: i64,
    /// At most one of the following must be present
    ///
    /// Index into string table
    #[prost(int64, tag = "2")]
    pub str: i64,
    #[prost(int64, tag = "3")]
    pub num: i64,
    /// Should only be present when num is present.
    /// Specifies the units of num.
    /// Use arbitrary string (for example, "requests") as a custom count unit.
    /// If no unit is specified, consumer may apply heuristic to deduce the unit.
    /// Consumers may also  interpret units like "bytes" and "kilobytes" as memory
    /// units and units like "seconds" and "nanoseconds" as time units,
    /// and apply appropriate unit conversions to these.
    ///
    /// Index into string table
    #[prost(int64, tag = "4")]
    pub num_unit: i64,
}
#[derive(Clone, Copy, PartialEq, Eq, Hash, ::prost::Message)]
pub struct Mapping {
    /// Unique nonzero id for the mapping.
    #[prost(uint64, tag = "1")]
    pub id: u64,
    /// Address at which the binary (or DLL) is loaded into memory.
    #[prost(uint64, tag = "2")]
    pub memory_start: u64,
    /// The limit of the address range occupied by this mapping.
    #[prost(uint64, tag = "3")]
    pub memory_limit: u64,
    /// Offset in the binary that corresponds to the first mapped address.
    #[prost(uint64, tag = "4")]
    pub file_offset: u64,
    /// The object this entry is loaded from.  This can be a filename on
    /// disk for the main binary and shared libraries, or virtual
    /// abstractions like "\[vdso\]".
    ///
    /// Index into string table
    #[prost(int64, tag = "5")]
    pub filename: i64,
    /// A string that uniquely identifies a particular program version
    /// with high probability. E.g., for binaries generated by GNU tools,
    /// it could be the contents of the .note.gnu.build-id field.
    ///
    /// Index into string table
    #[prost(int64, tag = "6")]
    pub build_id: i64,
    /// The following fields indicate the resolution of symbolic info.
    #[prost(bool, tag = "7")]
    pub has_functions: bool,
    #[prost(bool, tag = "8")]
    pub has_filenames: bool,
    #[prost(bool, tag = "9")]
    pub has_line_numbers: bool,
    #[prost(bool, tag = "10")]
    pub has_inline_frames: bool,
}
/// Describes function and line table debug information.
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct Location {
    /// Unique nonzero id for the location.  A profile could use
    /// instruction addresses or any integer sequence as ids.
    #[prost(uint64, tag = "1")]
    pub id: u64,
    /// The id of the corresponding profile.Mapping for this location.
    /// It can be unset if the mapping is unknown or not applicable for
    /// this profile type.
    #[prost(uint64, tag = "2")]
    pub mapping_id: u64,
    /// The instruction address for this location, if available.  It
    /// should be within \[Mapping.memory_start...Mapping.memory_limit\]
    /// for the corresponding mapping. A non-leaf address may be in the
    /// middle of a call instruction. It is up to display tools to find
    /// the beginning of the instruction if necessary.
    #[prost(uint64, tag = "3")]
    pub address: u64,
    /// Multiple line indicates this location has inlined functions,
    /// where the last entry represents the caller into which the
    /// preceding entries were inlined.
    ///
    /// E.g., if memcpy() is inlined into printf:
    ///     line\[0\].function_name == "memcpy"
    ///     line\[1\].function_name == "printf"
    #[prost(message, repeated, tag = "4")]
    pub line: ::prost::alloc::vec::Vec<Line>,
    /// Provides an indication that multiple symbols map to this location's
    /// address, for example due to identical code folding by the linker. In that
    /// case the line information above represents one of the multiple
    /// symbols. This field must be recomputed when the symbolization state of the
    /// profile changes.
    #[prost(bool, tag = "5")]
    pub is_folded: bool,
}
#[derive(Clone, Copy, PartialEq, Eq, Hash, ::prost::Message)]
pub struct Line {
    /// The id of the corresponding profile.Function for this line.
    #[prost(uint64, tag = "1")]
    pub function_id: u64,
    /// Line number in source code.
    #[prost(int64, tag = "2")]
    pub line: i64,
}
#[derive(Clone, Copy, PartialEq, Eq, Hash, ::prost::Message)]
pub struct Function {
    /// Unique nonzero id for the function.
    #[prost(uint64, tag = "1")]
    pub id: u64,
    /// Name of the function, in human-readable form if available.
    ///
    /// Index into string table
    #[prost(int64, tag = "2")]
    pub name: i64,
    /// Name of the function, as identified by the system.
    /// For instance, it can be a C++ mangled name.
    ///
    /// Index into string table
    #[prost(int64, tag = "3")]
    pub system_name: i64,
    /// Source file containing the function.
    ///
    /// Index into string table
    #[prost(int64, tag = "4")]
    pub filename: i64,
    /// Line number in source file.
    #[prost(int64, tag = "5")]
    pub start_line: i64,
}
```

## File: `src/encode/gen/mod.rs`
```rust
pub mod google;
pub mod push;
pub mod types;
```

## File: `src/encode/gen/push.rs`
```rust
// @generated
// This file is @generated by prost-build.
#[derive(Clone, Copy, PartialEq, Eq, Hash, ::prost::Message)]
pub struct PushResponse {}
/// WriteRawRequest writes a pprof profile
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct PushRequest {
    /// series is a set raw pprof profiles and accompanying labels
    #[prost(message, repeated, tag = "1")]
    pub series: ::prost::alloc::vec::Vec<RawProfileSeries>,
}
/// RawProfileSeries represents the pprof profile and its associated labels
#[derive(Clone, PartialEq, ::prost::Message)]
pub struct RawProfileSeries {
    /// LabelPair is the key value pairs to identify the corresponding profile
    #[prost(message, repeated, tag = "1")]
    pub labels: ::prost::alloc::vec::Vec<super::types::LabelPair>,
    /// samples are the set of profile bytes
    #[prost(message, repeated, tag = "2")]
    pub samples: ::prost::alloc::vec::Vec<RawSample>,
}
/// RawSample is the set of bytes that correspond to a pprof profile
#[derive(Clone, PartialEq, Eq, Hash, ::prost::Message)]
pub struct RawSample {
    /// raw_profile is the set of bytes of the pprof profile
    #[prost(bytes = "vec", tag = "1")]
    pub raw_profile: ::prost::alloc::vec::Vec<u8>,
    /// UUID of the profile
    #[prost(string, tag = "2")]
    pub id: ::prost::alloc::string::String,
}
```

## File: `src/encode/gen/types.rs`
```rust
// @generated
// This file is @generated by prost-build.
#[derive(Clone, PartialEq, Eq, Hash, ::prost::Message)]
pub struct LabelPair {
    /// Label name
    #[prost(string, tag = "1")]
    pub name: ::prost::alloc::string::String,
    /// Label value
    #[prost(string, tag = "2")]
    pub value: ::prost::alloc::string::String,
}
```

## File: `src/timer/epoll.rs`
```rust
use super::TimerSignal;
use crate::{
    utils::{check_err, get_time_range},
    PyroscopeError, Result,
};

use std::sync::{
    mpsc::{channel, Sender},
    Arc, Mutex,
};
use std::{
    thread::{self, JoinHandle},
    time::Duration,
};

const LOG_TAG: &str = "Pyroscope::Timer";

/// A thread that sends a notification every 10th second
///
/// Timer will send an event to attached listeners (mpsc::Sender) every 10th
/// second (...10, ...20, ...)
///
/// The Timer thread will run continously until all Senders are dropped.
/// The Timer thread will be joined when all Senders are dropped.

#[derive(Debug)]
pub struct Timer {
    /// A vector to store listeners
    txs: Arc<Mutex<Vec<Sender<TimerSignal>>>>,

    /// Thread handle
    pub handle: Option<JoinHandle<Result<()>>>,
}

impl Timer {
    /// Initialize Timer and run a thread to send events to attached listeners
    pub fn initialize(cycle: Duration) -> Result<Self> {
        log::info!(target: LOG_TAG, "Initializing Timer");

        let txs = Arc::new(Mutex::new(Vec::new()));

        // Add a dummy tx so the below thread does not terminate early
        let (tx, _rx) = channel();
        txs.lock()?.push(tx);

        let timer_fd = Timer::set_timerfd(cycle)?;
        let epoll_fd = Timer::create_epollfd(timer_fd)?;

        let handle = Some({
            let txs = txs.clone();
            thread::spawn(move || {
                loop {
                    // Exit thread if there are no listeners
                    if txs.lock()?.is_empty() {
                        // Close file descriptors
                        unsafe { libc::close(timer_fd) };
                        unsafe { libc::close(epoll_fd) };

                        log::info!(target: LOG_TAG, "Timer thread terminated");

                        return Ok::<_, PyroscopeError>(());
                    }

                    // Fire @ 10th sec
                    let res = Timer::epoll_wait(timer_fd, epoll_fd);
                    if matches!(&res, Err(PyroscopeError::Io(err)) if err.kind() == std::io::ErrorKind::Interrupted)
                    {
                        continue;
                    }
                    res?;

                    // Get the current time range
                    let from = TimerSignal::NextSnapshot(get_time_range(0)?.from);

                    log::trace!(target: LOG_TAG, "Timer fired @ {}", from);

                    // Iterate through Senders
                    txs.lock()?.iter().for_each(|tx| {
                        // Send event to attached Sender
                        match tx.send(from) {
                            Ok(_) => {
                                log::trace!(target: LOG_TAG, "Sent event to listener @ {:?}", &tx)
                            }
                            Err(_e) => {} // There could be a less confusing message, or this
                                          // refactored to avoid a first sender
                                          //log::warn!(
                                          //target: LOG_TAG,
                                          //"Failed to send event to listener @ {:?} - {}",
                                          //&tx,
                                          //e
                                          //),
                        }
                    });
                }
            })
        });

        Ok(Self { handle, txs })
    }

    /// create and set a timer file descriptor
    fn set_timerfd(cycle: Duration) -> Result<libc::c_int> {
        // Set the timer to use the system time.
        let clockid: libc::clockid_t = libc::CLOCK_REALTIME;
        // Non-blocking file descriptor
        let clock_flags: libc::c_int = libc::TFD_NONBLOCK;

        // Create timer fd
        let tfd = timerfd_create(clockid, clock_flags)?;

        // Get the next event time
        let first_fire = get_time_range(0)?.until;

        // new_value sets the Timer
        let mut new_value = libc::itimerspec {
            it_interval: libc::timespec {
                tv_sec: cycle.as_secs() as i64,
                tv_nsec: cycle.subsec_nanos() as i64,
            },
            it_value: libc::timespec {
                tv_sec: first_fire as i64,
                tv_nsec: 0,
            },
        };

        // Empty itimerspec object
        let mut old_value = libc::itimerspec {
            it_interval: libc::timespec {
                tv_sec: 0,
                tv_nsec: 0,
            },
            it_value: libc::timespec {
                tv_sec: 0,
                tv_nsec: 0,
            },
        };

        let set_flags = libc::TFD_TIMER_ABSTIME;

        // Set the timer
        timerfd_settime(tfd, set_flags, &mut new_value, &mut old_value)?;

        // Return file descriptor
        Ok(tfd)
    }

    /// Create a new epoll file descriptor and add the timer to its interests
    fn create_epollfd(timer_fd: libc::c_int) -> Result<libc::c_int> {
        // create a new epoll fd
        let epoll_fd = epoll_create1(0)?;

        // event to pull
        let mut event = libc::epoll_event {
            events: libc::EPOLLIN as u32,
            u64: 1,
        };

        let epoll_flags = libc::EPOLL_CTL_ADD;

        // add event to the epoll
        epoll_ctl(epoll_fd, epoll_flags, timer_fd, &mut event)?;

        // return epoll fd
        Ok(epoll_fd)
    }

    /// Wait for an event on the epoll file descriptor
    fn epoll_wait(timer_fd: libc::c_int, epoll_fd: libc::c_int) -> Result<()> {
        // vector to store events
        let mut events = Vec::with_capacity(1);

        // wait for the timer to fire an event. This is function will block.
        unsafe {
            epoll_wait(epoll_fd, events.as_mut_ptr(), 1, -1)?;
        }

        // read the value from the timerfd. This is required to re-arm the timer.
        let mut buffer: u64 = 0;
        let bufptr: *mut _ = &mut buffer;
        unsafe {
            read(timer_fd, bufptr as *mut libc::c_void, 8)?;
        }

        Ok(())
    }

    /// Attach an mpsc::Sender to Timer
    ///
    /// Timer will dispatch an event with the timestamp of the current instant,
    /// every 10th second to all attached senders
    pub fn attach_listener(&mut self, tx: Sender<TimerSignal>) -> Result<()> {
        // Push Sender to a Vector of Sender(s)
        let txs = Arc::clone(&self.txs);
        txs.lock()?.push(tx);

        Ok(())
    }

    /// Clear the listeners (txs) from Timer. This will shutdown the Timer thread
    pub fn drop_listeners(&mut self) -> Result<()> {
        let txs = Arc::clone(&self.txs);
        txs.lock()?.clear();

        Ok(())
    }
}

// Wrapper for libc functions.
//
// Error wrapper for some libc functions used by the library. This only does
// Error (-1 return) wrapping. Alternatively, the nix crate could be used
// instead of expanding this wrappers (if more functions and types are used
// from libc)

// libc::timerfd wrapper
pub fn timerfd_create(clockid: libc::clockid_t, clock_flags: libc::c_int) -> Result<i32> {
    check_err(unsafe { libc::timerfd_create(clockid, clock_flags) })
}

/// libc::timerfd_settime wrapper
pub fn timerfd_settime(
    timer_fd: i32,
    set_flags: libc::c_int,
    new_value: &mut libc::itimerspec,
    old_value: &mut libc::itimerspec,
) -> Result<()> {
    check_err(unsafe { libc::timerfd_settime(timer_fd, set_flags, new_value, old_value) })?;
    Ok(())
}

/// libc::epoll_create1 wrapper
pub fn epoll_create1(epoll_flags: libc::c_int) -> Result<i32> {
    check_err(unsafe { libc::epoll_create1(epoll_flags) })
}

/// libc::epoll_ctl wrapper
pub fn epoll_ctl(
    epoll_fd: i32,
    epoll_flags: libc::c_int,
    timer_fd: i32,
    event: &mut libc::epoll_event,
) -> Result<()> {
    check_err(unsafe { libc::epoll_ctl(epoll_fd, epoll_flags, timer_fd, event) })?;
    Ok(())
}

/// libc::epoll_wait wrapper
///
/// # Safety
/// This function is a wrapper for libc::epoll_wait.
pub unsafe fn epoll_wait(
    epoll_fd: i32,
    events: *mut libc::epoll_event,
    maxevents: libc::c_int,
    timeout: libc::c_int,
) -> Result<()> {
    check_err(libc::epoll_wait(epoll_fd, events, maxevents, timeout))?;
    Ok(())
}

/// libc::read wrapper
///
/// # Safety
/// This function is a wrapper for libc::read.
pub unsafe fn read(timer_fd: i32, bufptr: *mut libc::c_void, count: libc::size_t) -> Result<()> {
    check_err(libc::read(timer_fd, bufptr, count))?;
    Ok(())
}
```

## File: `src/timer/kqueue.rs`
```rust
use super::TimerSignal;
use crate::{
    utils::{check_err, get_time_range},
    Result,
};

use std::sync::{
    mpsc::{channel, Receiver, Sender},
    Arc, Mutex,
};
use std::{
    thread::{self, JoinHandle},
    time::Duration,
};

const LOG_TAG: &str = "Pyroscope::Timer";

/// A thread that sends a notification every 10th second
///
/// Timer will send an event to attached listeners (mpsc::Sender) every 10th
/// second (...10, ...20, ...)
///
/// The Timer thread will run continously until all Senders are dropped.
/// The Timer thread will be joined when all Senders are dropped.

#[derive(Debug, Default)]
pub struct Timer {
    /// A vector to store listeners (mpsc::Sender)
    txs: Arc<Mutex<Vec<Sender<TimerSignal>>>>,

    /// Thread handle
    pub handle: Option<JoinHandle<Result<()>>>,
}

impl Timer {
    /// Initialize Timer and run a thread to send events to attached listeners
    pub fn initialize(cycle: Duration) -> Result<Self> {
        log::info!(target: LOG_TAG, "Initializing Timer");

        let txs = Arc::new(Mutex::new(Vec::new()));

        // Add Default tx
        let (tx, _rx): (Sender<TimerSignal>, Receiver<TimerSignal>) = channel();
        txs.lock()?.push(tx);

        let kqueue = kqueue()?;

        let handle = Some({
            let txs = txs.clone();
            thread::spawn(move || {
                // Wait for initial expiration
                let initial_event = Timer::register_initial_expiration(kqueue)?;
                Timer::wait_event(kqueue, [initial_event].as_mut_ptr())?;

                // Register loop event
                let loop_event = Timer::register_loop_expiration(kqueue, cycle)?;

                // Loop 10s
                loop {
                    // Exit thread if there are no listeners
                    if txs.lock()?.len() == 0 {
                        // TODO: should close file descriptors?
                        log::info!(target: LOG_TAG, "Timer thread terminated");
                        return Ok(());
                    }

                    // Get current time
                    let from = TimerSignal::NextSnapshot(get_time_range(0)?.from);

                    // Iterate through Senders
                    txs.lock()?.iter().for_each(|tx| {
                        // Send event to attached Sender
                        match tx.send(from) {
                            Ok(_) => {
                                log::trace!(target: LOG_TAG, "Sent event to listener @ {:?}", &tx)
                            }
                            Err(_e) => {} // There could be a less confusing message, or this
                                          // refactored to avoid a first sender
                                          //log::warn!(
                                          //target: LOG_TAG,
                                          //"Failed to send event to listener @ {:?} - {}",
                                          //&tx,
                                          //e
                                          //),
                        }
                    });

                    // Wait 10s
                    Timer::wait_event(kqueue, [loop_event].as_mut_ptr())?;
                }
            })
        });

        Ok(Self { handle, txs })
    }

    /// Attach an mpsc::Sender to Timer
    ///
    /// Timer will dispatch an event with the timestamp of the current instant,
    /// every 10th second to all attached senders
    pub fn attach_listener(&mut self, tx: Sender<TimerSignal>) -> Result<()> {
        // Push Sender to a Vector of Sender(s)
        let txs = Arc::clone(&self.txs);
        txs.lock()?.push(tx);

        Ok(())
    }

    /// Clear the listeners (txs) from Timer. This will shutdown the Timer thread
    pub fn drop_listeners(&mut self) -> Result<()> {
        let txs = Arc::clone(&self.txs);
        txs.lock()?.clear();

        Ok(())
    }

    /// Wait for the timer event
    fn wait_event(kqueue: i32, events: *mut libc::kevent) -> Result<()> {
        kevent(kqueue, [].as_mut_ptr(), 0, events, 1, std::ptr::null())?;
        Ok(())
    }

    /// Register an initial expiration event
    fn register_initial_expiration(kqueue: i32) -> Result<libc::kevent> {
        // Get first event time
        let first_fire = get_time_range(0)?.until;

        let initial_event = libc::kevent {
            ident: 1,
            filter: libc::EVFILT_TIMER,
            flags: libc::EV_ADD | libc::EV_ENABLE | libc::EV_ONESHOT,
            fflags: libc::NOTE_ABSOLUTE | libc::NOTE_SECONDS,
            data: first_fire as isize,
            udata: 0 as *mut libc::c_void,
        };

        // add first event
        kevent(
            kqueue,
            [initial_event].as_ptr() as *const libc::kevent,
            1,
            [].as_mut_ptr(),
            0,
            std::ptr::null(),
        )?;

        Ok(initial_event)
    }

    /// Register a loop expiration event
    fn register_loop_expiration(kqueue: i32, duration: Duration) -> Result<libc::kevent> {
        let loop_event = libc::kevent {
            ident: 1,
            filter: libc::EVFILT_TIMER,
            flags: libc::EV_ADD | libc::EV_ENABLE,
            fflags: 0,
            data: duration.as_millis() as isize,
            udata: 0 as *mut libc::c_void,
        };

        // add loop event
        let _ke = kevent(
            kqueue,
            [loop_event].as_ptr() as *const libc::kevent,
            1,
            [].as_mut_ptr(),
            0,
            std::ptr::null(),
        )?;

        Ok(loop_event)
    }
}

/// libc::kqueue wrapper
fn kqueue() -> Result<i32> {
    check_err(unsafe { libc::kqueue() }).map(|kq| kq as i32)
}

/// libc::kevent wrapper
fn kevent(
    kqueue: i32,
    change: *const libc::kevent,
    c_count: libc::c_int,
    events: *mut libc::kevent,
    e_count: libc::c_int,
    timeout: *const libc::timespec,
) -> Result<()> {
    check_err(unsafe { libc::kevent(kqueue, change, c_count, events, e_count, timeout) })?;
    Ok(())
}
```

## File: `src/timer/mod.rs`
```rust
/// A signal sent to the timer.
///
/// Either schedules another wake-up, or asks
/// the timer thread to terminate.
#[derive(Debug, Clone, Copy)]
pub enum TimerSignal {
    // Thread termination was requested.
    Terminate,
    // When to take the next snapshot using the `Backend`.
    NextSnapshot(u64),
}

impl std::fmt::Display for TimerSignal {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            Self::Terminate => write!(f, "Terminate"),
            Self::NextSnapshot(when) => write!(f, "NextSnapshot({})", when),
        }
    }
}

// Possibly: ios, netbsd, openbsd, freebsd
#[cfg(target_os = "macos")]
pub mod kqueue;

#[cfg(target_os = "macos")]
pub use kqueue::Timer;

// Possibly: android
#[cfg(target_os = "linux")]
pub mod epoll;
#[cfg(target_os = "linux")]
pub use epoll::Timer;

#[cfg(not(any(target_os = "linux", target_os = "macos")))]
pub mod sleep;
#[cfg(not(any(target_os = "linux", target_os = "macos")))]
pub use sleep::Timer;
```

## File: `src/timer/sleep.rs`
```rust
use super::TimerSignal;
use crate::{utils::get_time_range, Result};

use std::{
    sync::{
        mpsc::{channel, Receiver, Sender},
        Arc, Mutex,
    },
    thread::{self, JoinHandle},
    time::Duration,
};

const LOG_TAG: &str = "Pyroscope::Timer";

/// A thread that sends a notification every 10th second
///
/// Timer will send an event to attached listeners (mpsc::Sender) every 10th
/// second (...10, ...20, ...)
///
/// The Timer thread will run continously until all Senders are dropped.
/// The Timer thread will be joined when all Senders are dropped.

#[derive(Debug, Default)]
pub struct Timer {
    /// A vector to store listeners (mpsc::Sender)
    txs: Arc<Mutex<Vec<Sender<TimerSignal>>>>,

    /// Thread handle
    pub handle: Option<JoinHandle<Result<()>>>,
}

impl Timer {
    /// Initialize Timer and run a thread to send events to attached listeners
    pub fn initialize(cycle: Duration) -> Result<Self> {
        log::info!(target: LOG_TAG, "Initializing Timer");

        let txs = Arc::new(Mutex::new(Vec::new()));

        // Add Default tx
        let (tx, _rx): (Sender<TimerSignal>, Receiver<TimerSignal>) = channel();
        txs.lock()?.push(tx);

        // Spawn a Thread
        let handle = Some({
            let txs = txs.clone();

            thread::spawn(move || {
                // Get remaining time for 10th second fire event
                let rem = get_time_range(0)?.rem;

                // Sleep for rem seconds
                thread::sleep(Duration::from_secs(rem));

                loop {
                    // Exit thread if there are no listeners
                    if txs.lock()?.len() == 0 {
                        log::info!(target: LOG_TAG, "Timer thread terminated");

                        return Ok(());
                    }

                    // Get current time
                    let from = TimerSignal::NextSnapshot(get_time_range(0)?.from);

                    log::trace!(target: LOG_TAG, "Timer fired @ {}", from);

                    // Iterate through Senders
                    txs.lock()?.iter().for_each(|tx| {
                        // Send event to attached Sender
                        // Send event to attached Sender
                        match tx.send(from) {
                            Ok(_) => {
                                log::trace!(target: LOG_TAG, "Sent event to listener @ {:?}", &tx)
                            }
                            Err(_e) => {} // There could be a less confusing message, or this
                                          // refactored to avoid a first sender
                                          //log::warn!(
                                          //target: LOG_TAG,
                                          //"Failed to send event to listener @ {:?} - {}",
                                          //&tx,
                                          //e
                                          //),
                        }
                    });

                    // Sleep for 10s
                    thread::sleep(cycle);
                }
            })
        });

        Ok(Self { handle, txs })
    }

    /// Attach an mpsc::Sender to Timer
    ///
    /// Timer will dispatch an event with the timestamp of the current instant,
    /// every 10th second to all attached senders
    pub fn attach_listener(&mut self, tx: Sender<TimerSignal>) -> Result<()> {
        // Push Sender to a Vector of Sender(s)
        let txs = Arc::clone(&self.txs);
        txs.lock()?.push(tx);

        Ok(())
    }

    /// Clear the listeners (txs) from Timer. This will shutdown the Timer thread
    pub fn drop_listeners(&mut self) -> Result<()> {
        let txs = Arc::clone(&self.txs);
        txs.lock()?.clear();

        Ok(())
    }
}
```

## File: `tests/agent.rs`
```rust
use pyroscope::pyroscope::PyroscopeConfig;

#[test]
fn test_config_new() {
    let config = PyroscopeConfig::new("http://localhost:8080", "myapp", 100, "testspy", "1.2.3");
    assert_eq!(config.url, "http://localhost:8080");
    assert_eq!(config.application_name, "myapp");
    assert_eq!(config.sample_rate, 100u32);
    assert_eq!(config.tags.len(), 0);
}

#[test]
fn test_config_constructor_values() {
    let config = PyroscopeConfig::new("http://localhost:8080", "myapp", 10, "testspy", "1.2.3");
    assert_eq!(config.sample_rate, 10u32);
    assert_eq!(config.spy_name, "testspy");
    assert_eq!(config.spy_version, "1.2.3");
}

#[test]
fn test_config_tags_empty() {
    let config = PyroscopeConfig::new("http://localhost:8080", "myapp", 100, "testspy", "1.2.3");
    assert_eq!(config.tags.len(), 0);
}

#[test]
fn test_config_tags() {
    let config = PyroscopeConfig::new("http://localhost:8080", "myapp", 100, "testspy", "1.2.3")
        .tags([("tag", "value")].to_vec());
    assert_eq!(config.tags.len(), 1);
    assert_eq!(config.tags.get("tag"), Some(&"value".to_owned()));
}

#[test]
fn test_config_tags_multiple() {
    let config = PyroscopeConfig::new("http://localhost:8080", "myapp", 100, "testspy", "1.2.3")
        .tags([("tag1", "value1"), ("tag2", "value2")].to_vec());
    assert_eq!(config.tags.len(), 2);
    assert_eq!(config.tags.get("tag1"), Some(&"value1".to_owned()));
    assert_eq!(config.tags.get("tag2"), Some(&"value2".to_owned()));
}
```

## File: `tests/pprof_backend.rs`
```rust
#[cfg(feature = "backend-pprof-rs")]
mod tests {
    use pyroscope::backend::{pprof_backend, BackendConfig, PprofConfig};
    use std::collections::hash_map::DefaultHasher;
    use std::hash::{Hash, Hasher};
    use std::sync::atomic::{AtomicBool, Ordering};
    use std::sync::Arc;
    use std::time::{Duration, Instant};

    fn next_size(hasher: &mut DefaultHasher) -> usize {
        Instant::now().hash(hasher);
        (hasher.finish() as usize) % (256 * 1024) + 1
    }

    // NOTE: This test is not reliable — it only exercises the initialize/report
    // lifecycle against a live workload and makes no assertions on the output.
    // No failures have been observed so far; kept as a smoke test for the future.
    #[test]
    fn test_pprof_backend_alloc_loop() {
        let stop = Arc::new(AtomicBool::new(false));
        let stop_thread = stop.clone();

        // Start the alloc loop slightly before the profiler initializes
        let alloc_thread = std::thread::spawn(move || {
            let mut hasher = DefaultHasher::new();
            while !stop_thread.load(Ordering::Relaxed) {
                // Vary allocation size between 1 B and 256 KiB
                let size = next_size(&mut hasher);
                let v: Vec<u8> = vec![0u8; size];
                drop(v);
            }
        });

        // Brief pause so the alloc thread is running before profiling starts
        std::thread::sleep(Duration::from_millis(50));

        let mut backend = pprof_backend(PprofConfig::default(), BackendConfig::default())
            .initialize()
            .expect("failed to initialize pprof backend");

        std::thread::sleep(Duration::from_secs(5));

        let reports = backend.report().expect("failed to dump report");
        drop(reports);

        stop.store(true, Ordering::Relaxed);
        alloc_thread.join().expect("alloc thread panicked");
    }
}
```

## File: `tests/session.rs`
```rust
use claims::assert_ok;
use pyroscope::{
    backend::{Report, ReportBatch, ReportData},
    pyroscope::PyroscopeConfig,
    session::{Session, SessionManager, SessionSignal},
};
use std::collections::HashMap;

#[test]
fn test_session_manager_new() {
    let session_manager = SessionManager::new().unwrap();
    assert!(session_manager.handle.is_some());
}

#[test]
fn test_session_manager_push_kill() {
    let session_manager = SessionManager::new().unwrap();
    session_manager.push(SessionSignal::Kill).unwrap();
    assert_ok!(session_manager.handle.unwrap().join().unwrap());
}

#[test]
fn test_session_new() {
    let config = PyroscopeConfig {
        url: "http://localhost:8080".to_string(),
        application_name: "test".to_string(),
        tags: HashMap::new(),
        sample_rate: 100u32,
        spy_name: "test-rs".to_string(),
        ..Default::default()
    };

    let batch = ReportBatch {
        profile_type: "process_cpu".into(),
        data: ReportData::Reports(vec![Report::new(HashMap::new())]),
    };

    let session = Session::new(1950, config, batch).unwrap();

    assert_eq!(session.from, 1940);
    assert_eq!(session.until, 1950);
}

#[test]
fn test_session_send_error() {
    let config = PyroscopeConfig {
        url: "http://invalid_url".to_string(),
        application_name: "test".to_string(),
        tags: HashMap::new(),
        sample_rate: 100u32,
        spy_name: "test-rs".to_string(),
        ..Default::default()
    };

    let batch = ReportBatch {
        profile_type: "process_cpu".into(),
        data: ReportData::Reports(vec![Report::new(HashMap::new())]),
    };

    let _session = Session::new(1950, config, batch).unwrap();
}
```

## File: `tests/timer-epoll.rs`
```rust
#[cfg(target_os = "linux")]
mod tests {
    use claims::assert_ok;
    use pyroscope::timer::epoll::{
        epoll_create1, epoll_ctl, epoll_wait, timerfd_create, timerfd_settime,
    };

    #[test]
    fn test_timerfd_create() {
        let timer_fd = timerfd_create(libc::CLOCK_REALTIME, libc::TFD_NONBLOCK).unwrap();
        assert!(timer_fd > 0);
    }

    #[test]
    fn test_timerfd_settime() {
        let mut new_value = libc::itimerspec {
            it_interval: libc::timespec {
                tv_sec: 10,
                tv_nsec: 0,
            },
            it_value: libc::timespec {
                tv_sec: 0,
                tv_nsec: 0,
            },
        };

        let mut old_value = libc::itimerspec {
            it_interval: libc::timespec {
                tv_sec: 0,
                tv_nsec: 0,
            },
            it_value: libc::timespec {
                tv_sec: 0,
                tv_nsec: 0,
            },
        };

        let timer_fd = timerfd_create(libc::CLOCK_REALTIME, libc::TFD_NONBLOCK).unwrap();
        assert_ok!(timerfd_settime(
            timer_fd,
            libc::TFD_TIMER_ABSTIME,
            &mut new_value,
            &mut old_value,
        ));
    }

    #[test]
    fn test_epoll_create1() {
        let epoll_fd = epoll_create1(0).unwrap();
        assert!(epoll_fd > 0);
    }

    #[test]
    fn test_epoll_ctl() {
        let mut event = libc::epoll_event {
            events: libc::EPOLLIN as u32,
            u64: 1,
        };

        let epoll_fd = epoll_create1(0).unwrap();
        let timer_fd = timerfd_create(libc::CLOCK_REALTIME, libc::TFD_NONBLOCK).unwrap();
        assert_ok!(epoll_ctl(
            epoll_fd,
            libc::EPOLL_CTL_ADD,
            timer_fd,
            &mut event
        ));
    }

    #[test]
    fn test_epoll_wait() {
        let mut event = libc::epoll_event {
            events: libc::EPOLLIN as u32,
            u64: 1,
        };

        let epoll_fd = epoll_create1(0).unwrap();
        let timer_fd = timerfd_create(libc::CLOCK_REALTIME, libc::TFD_NONBLOCK).unwrap();
        epoll_ctl(epoll_fd, libc::EPOLL_CTL_ADD, timer_fd, &mut event).unwrap();

        let mut events = vec![libc::epoll_event { events: 0, u64: 0 }];

        // Expire in 1ms
        assert_ok!(unsafe { epoll_wait(epoll_fd, events.as_mut_ptr(), 1, 1) });
    }
}
```

## File: `tests/timer.rs`
```rust
use assert_matches::assert_matches;
use pyroscope::timer::{Timer, TimerSignal};
use std::time::Duration;

#[test]
fn test_timer() {
    // Initialize Timer
    let mut timer = Timer::initialize(Duration::from_secs(10)).unwrap();

    // Attach a listener
    let (tx, rx) = std::sync::mpsc::channel();
    timer.attach_listener(tx).unwrap();

    // Wait for event (should arrive in 10s)
    let planned = rx.recv().unwrap();
    assert_matches!(planned, TimerSignal::NextSnapshot(planned) => {
        // Get current time
        let now = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_secs();

        // Check that recv and now are within 10s of each other
        assert!(planned - now < 10);

        // Check that recv is divisible by 10
        assert!(planned % 10 == 0);
    })
}
```

