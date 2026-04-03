---
id: github.com-kijewski-zipsign-70175dbd-knowledge
type: document
owner: OHD
tags: [auto-healed]
healed_at: 2026-04-02T20:20:19.478259
---

# KNOWLEDGE EXTRACT: github.com_Kijewski_zipsign_70175dbd
> **Extracted on:** 2026-04-01 07:28:21
> **Source:** D:/LongLeo/AI OS CORP/AI OS/system/security/QUARANTINE/KI-BATCH-20260331205007518963/github.com_Kijewski_zipsign_70175dbd

---

## File: `.gitignore`
```
/target
Cargo.lock

run.cgi

*.pyc
*.swp*
*.nfs*
*~
*.~*
*.tmp
*.old
*.bak
*.orig
*.pid
*.so
*.so.*
*.cpp
*.py[co]
*.egg-info
*.whl

.*
!.git*
!.readthedocs.yaml
```

## File: `Cargo.toml`
```
[workspace]
resolver = "3"
members = ["api", "cli"]
default-members = ["api", "cli"]

[workspace.dependencies]
base64 = "0.22.0"
clap = { version = "4.4.0", features = ["derive"] }
ed25519-dalek = { version = "2.0.0", features = ["digest"] }
getrandom = { version = ">= 0.3.0, < 0.5.0", features = ["std"] }
normalize-path = "0.2.0"
pretty-error-debug = "0.3.0"
tempfile = "3.0.0"
thiserror = "2.0.8"
zip = { version = ">= 2.0.0, < 9.0.0", default-features = false }

[workspace.dependencies.zipsign-api]
version = "0.2.0"
path = "api"
default-features = false
features = ["tar", "zip"]

[workspace.lints.rust]
unknown_lints = { level = "allow", priority = -1 }
unsafe_code = { level = "forbid", priority = -1 }

absolute_paths_not_starting_with_crate = "warn"
elided_lifetimes_in_paths = "warn"
explicit_outlives_requirements = "warn"
meta_variable_misuse = "warn"
missing_copy_implementations = "warn"
missing_debug_implementations = "warn"
missing_docs = "warn"
non_ascii_idents = "warn"
noop_method_call = "warn"
rust_2024_compatibility = "warn"
single_use_lifetimes = "warn"
trivial_casts = "warn"
unreachable_pub = "warn"
unused_crate_dependencies = "warn"
unused_extern_crates = "warn"
unused_lifetimes = "warn"
unused_results = "warn"
warnings = "warn"

[workspace.lints.clippy]
collapsible_match = "warn"
expect_used = "warn"
match_bool = "warn"
match_ref_pats = "warn"
match_same_arms = "warn"
match_single_binding = "warn"
needless_bool = "deny"
needless_late_init = "warn"
needless_match = "warn"
redundant_guards = "warn"
redundant_pattern = "warn"
redundant_pattern_matching = "warn"
single_match = "warn"
single_match_else = "warn"
unwrap_used = "warn"
```

## File: `LICENSE-APACHE`
```
Copyright (c) 2023-2025 René Kijewski <crates.io@k6i.de>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

--- LLVM Exceptions to the Apache 2.0 License ----

As an exception, if, as a result of your compiling your source code, portions
of this Software are embedded into an Object form of such source code, you
may redistribute such embedded portions in such Object form without complying
with the conditions of Sections 4(a), 4(b) and 4(d) of the License.

In addition, if you combine or link compiled forms of this Software with
software that is licensed under the GPLv2 ("Combined Software") and if a
court of competent jurisdiction determines that the patent provision (Section
3), the indemnity provision (Section 9) or other Section of the License
conflicts with the conditions of the GPLv2, you may retroactively and
prospectively choose to deem waived or otherwise exclude such Section(s) of
the License, but only in their entirety and only with respect to the Combined
Software.

-------------------------------------------------------------------------------

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

## File: `LICENSE-MIT`
```
Copyright (c) 2023-2025 René Kijewski <crates.io@k6i.de>

Permission is hereby granted, free of charge, to any
person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the
Software without restriction, including without
limitation the rights to use, copy, modify, merge,
publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software
is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice
shall be included in all copies or substantial portions
of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF
ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED
TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A
PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT
SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR
IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
```

## File: `README.md`
```markdown
## zipsign

A tool to sign and verify `.zip` and `.tar.gz` files with an ed25519 signing key.

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Kijewski/zipsign/ci.yml?branch=main&style=flat-square&logoColor=white)](https://github.com/Kijewski/zipsign/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/zipsign?logo=rust&style=flat-square&logoColor=white)](https://crates.io/crates/zipsign)

### Install

```text
cargo install zipsign
```

or

```text
cargo install --git https://github.com/Kijewski/zipsign
```

### Example

* .zip:

    ```sh
    # Generate key pair:
    $ zipsign gen-key priv.key pub.key

    # ZIP a file and list the content of the ZIP file:
    $ zip Cargo.lock.zip Cargo.lock
    $ unzip -l Cargo.lock.zip
    Cargo.lock

    # Sign the ZIP file:
    $ zipsign sign zip Cargo.lock.zip priv.key
    $ unzip -l Cargo.lock.zip
    Cargo.lock

    # Verify that the generated signature is valid:
    $ zipsign verify zip Cargo.lock.zip pub.key
    OK
    ```

* .tar:

    ```sh
    # Generate key pair:
    $ zipsign gen-key priv.key pub.key

    # TAR a file and list the content of the ZIP file:
    $ tar czf Cargo.lock.tgz Cargo.lock
    $ tar tzf Cargo.lock.tgz
    Cargo.lock

    # Sign the .tar.gz file:
    $ zipsign sign tar Cargo.lock.tgz priv.key
    $ tar tzf Cargo.lock.tgz
    Cargo.lock

    # Verify that the generated signature is valid:
    $ zipsign verify tar Cargo.lock.tgz pub.key
    OK
    ```

### Generate key

Usage: `zipsign gen-key <PRIVATE_KEY> <VERIFYING_KEY>`

Arguments:

* `PRIVATE_KEY`:    Private key file to create
* `VERIFYING_KEY`:  Verifying key (public key) file to create

Options:

* `-e`, `--extract`: Don't create new key pair, but extract public key from private key
* `-f`, `--force`: Overwrite output file if it exists

### Sign a .zip or .tar.gz file

Usage: `zipsign sign [zip|tar] [-o <OUTPUT>] <INPUT> <KEYS>...`

Subcommands:

* `zip`: Sign a .zip file
* `tar`: Sign a .tar.gz file

Options:

* `-o`, `--output <OUTPUT>`:   Signed file to generate (if omitted, the input is overwritten)
* `-c`, `--context <CONTEXT>`: Arbitrary string used to salt the input, defaults to file name of `<INPUT>`
* `-f`, `--force`:             Overwrite output file if it exists

Arguments:

* `<INPUT>`:   Input file to sign
* `<KEYS>...`: One or more files containing private keys

### Verify a signature

Usage: `zipsign verify [zip|tar] <INPUT>`

Subcommands:

* `zip`: Verify a signed `.zip` file
* `tar`: Verify a signed `.tar.gz` file

Options:

* `-c`, `--context <CONTEXT>`: An arbitrary string used to salt the input, defaults to file name of `<INPUT>`
* `-q`, `--quiet`:             Don't write "OK" if the verification succeeded

Arguments:

* `<INPUT>`:   Signed `.zip` or `.tar.gz` file
* `<KEYS>...`: One or more files containing verifying keys

### Remove signatures

Usage: `zipsign unsign [zip|tar] [-o <OUTPUT>] <INPUT>`

Subcommands:

* `zip`: Removed signatures from `.zip` file
* `tar`: Removed signatures from `.tar.gz` file

Arguments:

* `<INPUT>`:   Signed `.zip` or `.tar.gz` file

Options:

* `-o`, `--output <OUTPUT>`: Unsigned file to generate (if omitted, the input is overwritten)
* `-f`, `--force`:           Overwrite output file if it exists

### How does it work?

The files are signed with one or more private keys using [ed25519ph](https://datatracker.ietf.org/doc/html/rfc8032#section-5.1).
The signatures are stored transparently next to the data.

For .tar.gz files the signatures are encoded as [base64](https://datatracker.ietf.org/doc/html/rfc4648#page-5) string.
The string gets encapsulated as the comment of a GZIP file, and this GZIP file is appended to the input document.
This works, because multiple GZIP files can be freely concatenated.

For .zip files the signature gets prepended to the input document.
This works because ZIP files can be prepended with any data as long as all relative addresses are fixed up afterwards.
This feature is used e.g. in self-extracting ZIP files.
```

## File: `_typos.toml`
```
[default]
locale = "en-us"

[files]
extend-exclude = ["/.*"]
```

## File: `deny.toml`
```
[licenses]
version = 2
allow = [
    "Apache-2.0",
    "Apache-2.0 WITH LLVM-exception",
    "BSD-3-Clause",
    "MIT",
    "Unicode-3.0",
]
private = { ignore = true }
```

## File: `rustfmt.toml`
```
combine_control_expr = false
edition = "2024"
format_macro_matchers = true
group_imports = "StdExternalCrate"
imports_granularity = "Module"
match_block_trailing_comma = true
newline_style = "Unix"
normalize_doc_attributes = true
overflow_delimited_expr = true
reorder_impl_items = true
style_edition = "2024"
unstable_features = true
use_field_init_shorthand = true
use_try_shorthand = true
```

## File: `tomlfmt.toml`
```
# Keep in the same order as <https://doc.rust-lang.org/cargo/reference/manifest.html>
table_order = [
    "package",
    # targets
    "lib",
    "bin",
    "example",
    "test",
    "bench",
    # dependencies
    "dependencies",
    "dev-dependencies",
    "build-dependencies",
    "target",
    # misc
    "badges",
    "features",
    "lints",
    "patch",
    "replace",
    "profile",
    "workspace",
]
```

## File: `api/Cargo.toml`
```
[package]
name = "zipsign-api"
description = "Sign and verify `.zip` and `.tar.gz` files with an ed25519 signing key"
version = "0.2.1"
edition = "2024"
authors = ["René Kijewski <crates.io@k6i.de>"]
repository = "https://github.com/Kijewski/zipsign"
license = "MIT OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception"
rust-version = "1.85"

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--generate-link-to-definition", "--cfg=docsrs"]

[dependencies]
base64 = { workspace = true, optional = true }
ed25519-dalek.workspace = true
thiserror.workspace = true
zip = { workspace = true, optional = true }

[features]
default = ["tar", "zip"]

verify-tar = ["dep:base64"]
verify-zip = []

unsign-tar = ["dep:base64"]
unsign-zip = ["dep:zip"]

sign-tar = ["dep:base64"]
sign-zip = ["dep:zip"]

tar = ["sign-tar", "unsign-tar", "verify-tar"]
zip = ["sign-zip", "unsign-zip", "verify-zip"]
```

## File: `api/LICENSE-APACHE`
```
../LICENSE-APACHE
```

## File: `api/LICENSE-MIT`
```
../LICENSE-MIT
```

## File: `api/README.md`
```markdown
## zipsign-api

Sign and verify `.zip` and `.tar.gz` files with an ed25519 signing key.

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/Kijewski/zipsign/ci.yml?branch=main&style=flat-square&logoColor=white)](https://github.com/Kijewski/zipsign/actions/workflows/ci.yml)
[![Crates.io](https://img.shields.io/crates/v/zipsign-api?logo=rust&style=flat-square&logoColor=white)](https://crates.io/crates/zipsign-api)
[![docs.rs](https://img.shields.io/docsrs/zipsign-api?logo=docsdotrs&style=flat-square&logoColor=white "docs.rs")](https://docs.rs/zipsign-api/)

This library contains the brains of [`zipsign`](https://github.com/Kijewski/zipsign).
You can use it in your projects to verify and sign `.zip` and `.tar.gz` files
without running a separate application, e.g. to verify a self-update.

### Features

* `default`: sign and verify `.tar.gz` and `.zip` files
* `sign-tar`: sign a `.tar.gz` file
* `verify-tar`: verify a signed `.tar.gz` file
* `sign-zip`: sign a `.zip` file
* `verify-zip`: verify a signed `.zip` file
* `tar`: combines `sign-tar` and `verify-tar`
* `zip`: combines `sign-zip` and `verify-zip`
```

## File: `api/_typos.toml`
```
../_typos.toml
```

## File: `api/clippy.toml`
```
msrv = "1.85.0"
```

## File: `api/deny.toml`
```
../deny.toml
```

## File: `api/rustfmt.toml`
```
../rustfmt.toml
```

## File: `api/tomlfmt.toml`
```
../tomlfmt.toml
```

## File: `api/src/constants.rs`
```rust
// "\x0c\x04\x01" -- form feed, end of text, start of header
// "ed25519ph" -- used algorithm
// "\x00\x00" -- version number in network byte order
/// Bytes preceding signatures
pub(crate) const MAGIC_HEADER: &[u8; 14] = b"\x0c\x04\x01ed25519ph\x00\x00";

/// Total number of bytes in a [`MAGIC_HEADER`] + [`SignatureCountLeInt`]
pub(crate) const HEADER_SIZE: usize = 16;

/// Integer type to tell the number of signatures in a signed file, stored in little endian
pub(crate) type SignatureCountLeInt = u16;

/// Prefix of the signature block in a signed .tar.gz file
///
/// Followed by base64 encoded signatures string, the current stream position before this block
/// encoded as zero-padded 16 bytes hexadecimal string, and [`GZIP_END`]
/// [`GZIP_END`]
#[cfg(any(feature = "sign-tar", feature = "unsign-tar", feature = "verify-tar"))]
pub(crate) const GZIP_START: &[u8; 10] = {
    const EPOCH: u32 = 978_307_200; // 2001-01-01 00:00:00 Z

    let [m1, m2, m3, m4] = EPOCH.to_le_bytes();
    &[
        0x1f, 0x8b, // gzip: magic number
        0x08, // gzip: compression method (deflate)
        0x10, // gzip: flags (binary, no checksum, no extra fields, no name, has comment)
        m1, m2, m3, m4,   // gzip: modification time
        0x00, // gzip: extra flags (unset)
        0xff, // gzip: Operating system ID: unknown
    ]
};

/// Suffix of the signature block in a signed .tar.gz file
#[cfg(any(feature = "sign-tar", feature = "unsign-tar", feature = "verify-tar"))]
pub(crate) const GZIP_END: &[u8; 14] = &[
    0x00, // deflate: NUL terminator, end of comments
    0x01, // deflate: block header (final block, uncompressed)
    0x00, 0x00, // deflate: length
    0xff, 0xff, // deflate: negated length
    0, 0, 0, 0, // gzip: crc32 of uncompressed data
    0, 0, 0, 0, // gzip: total uncompressed size
];

/// Total overhead the signature block in a signed .tar.gz file excluding signature data
#[cfg(feature = "sign-tar")]
pub(crate) const GZIP_EXTRA: usize = GZIP_START.len() + GZIP_END.len() + u64::BITS as usize / 4;

/// Maximum number of bytes the encoded signatures may have
///
/// This number equates to 1022 signatures in a `.zip` file, and 767 signatures in `.tar.gz` file.
pub(crate) const BUF_LIMIT: usize = 1 << 16;
```

## File: `api/src/lib.rs`
```rust
#![cfg_attr(docsrs, feature(doc_cfg))]
#![forbid(unsafe_code)]
#![allow(unknown_lints)]
#![warn(absolute_paths_not_starting_with_crate)]
#![warn(elided_lifetimes_in_paths)]
#![warn(explicit_outlives_requirements)]
#![warn(meta_variable_misuse)]
#![warn(missing_copy_implementations)]
#![warn(missing_debug_implementations)]
#![warn(missing_docs)]
#![warn(non_ascii_idents)]
#![warn(noop_method_call)]
#![warn(rust_2021_idioms)]
#![warn(single_use_lifetimes)]
#![warn(trivial_casts)]
#![warn(unreachable_pub)]
#![warn(unused_crate_dependencies)]
#![warn(unused_extern_crates)]
#![warn(unused_lifetimes)]
#![warn(unused_results)]
#![allow(clippy::enum_variant_names)]
#![doc = include_str!("../README.md")]

mod constants;
pub mod sign;
#[cfg(any(feature = "sign-zip", feature = "unsign-zip"))]
mod sign_unsign_zip;
pub mod unsign;
pub mod verify;
#[cfg(any(feature = "verify-tar", feature = "unsign-tar"))]
mod verify_unsign_tar;

use std::fmt;
use std::io::{self, Read};

#[doc(no_inline)]
pub use ed25519_dalek::{
    KEYPAIR_LENGTH, PUBLIC_KEY_LENGTH, SIGNATURE_LENGTH, Signature, SignatureError, SigningKey,
    VerifyingKey,
};

/// The unsigned hash of an input file
///
/// Use [`io::Write`] to update the prehash.
#[derive(Clone, Default)]
pub struct Prehash(ed25519_dalek::Sha512);

impl fmt::Debug for Prehash {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        f.debug_struct("Prehash").finish_non_exhaustive()
    }
}

impl Prehash {
    /// Instantiate a new prehash
    pub fn new() -> Self {
        Self(ed25519_dalek::Sha512::default())
    }

    /// Combination of [`Prehash::new()`] and [`io::Write`]
    pub fn calculate<I>(input: &mut I) -> io::Result<Self>
    where
        I: ?Sized + Read,
    {
        let mut this = Self::new();
        let _: u64 = io::copy(input, &mut this.0)?;
        Ok(this)
    }
}

impl io::Write for Prehash {
    #[inline]
    fn write(&mut self, buf: &[u8]) -> io::Result<usize> {
        self.0.write(buf)
    }

    #[inline]
    fn flush(&mut self) -> io::Result<()> {
        self.0.flush()
    }
}

/// A collection of all errors this library can return
#[non_exhaustive]
#[derive(Debug, thiserror::Error)]
#[error(transparent)]
pub enum ZipsignError {
    /// An error returned by [`gather_signature_data()`][self::sign::gather_signature_data]
    GatherSignatureData(#[from] self::sign::GatherSignatureDataError),
    /// An error returned by [`read_signing_keys()`][self::sign::read_signing_keys]
    ReadSigningKeys(#[from] self::sign::ReadSigningKeysError),
    /// An error returned by [`copy_and_sign_tar()`][self::sign::copy_and_sign_tar]
    #[cfg(feature = "sign-tar")]
    #[cfg_attr(docsrs, doc(cfg(feature = "sign-tar")))]
    SignTar(#[from] self::sign::SignTarError),
    /// An error returned by [`copy_and_sign_zip()`][self::sign::copy_and_sign_zip]
    #[cfg(feature = "sign-zip")]
    #[cfg_attr(docsrs, doc(cfg(feature = "sign-zip")))]
    SignZip(#[from] self::sign::SignZipError),

    /// No matching key/signature pair found
    NoMatch(#[from] self::verify::NoMatch),
    /// An error returned by [`collect_keys()`][self::verify::collect_keys]
    CollectKeys(#[from] self::verify::CollectKeysError),
    /// An error returned by [`read_signatures()`][self::verify::read_signatures]
    ReadSignatures(#[from] self::verify::ReadSignaturesError),
    /// An error returned by [`verify_tar()`][self::verify::verify_tar]
    #[cfg(feature = "verify-tar")]
    #[cfg_attr(docsrs, doc(cfg(feature = "verify-tar")))]
    VerifyTar(#[from] self::verify::VerifyTarError),
    /// An error returned by [`verify_zip()`][self::verify::verify_zip]
    #[cfg(feature = "verify-zip")]
    #[cfg_attr(docsrs, doc(cfg(feature = "verify-zip")))]
    VerifyZip(#[from] self::verify::VerifyZipError),

    /// An error returned by [`copy_and_unsign_tar()`][self::unsign::copy_and_unsign_tar]
    #[cfg(feature = "unsign-tar")]
    #[cfg_attr(docsrs, doc(cfg(feature = "unsign-tar")))]
    UnsignTar(#[from] self::unsign::UnsignTarError),
    /// An error returned by [`copy_and_unsign_zip()`][self::unsign::copy_and_unsign_zip]
    #[cfg(feature = "unsign-zip")]
    #[cfg_attr(docsrs, doc(cfg(feature = "unsign-zip")))]
    UnsignZip(#[from] self::unsign::UnsignZipError),

    /// An I/O occurred
    Io(#[from] io::Error),
}

macro_rules! Error {
    (
        $(#[$meta:meta])+
        $vis:vis struct $outer:ident($inner:ident) { $(
            $(#[$field_meta:meta])+
            $field:ident $(( $(
                $(#[$ty_meta:meta])*
                $field_type:ty
            ),+ $(,)? ))?
        ),+ $(,)? }
    ) => {
        $(#[$meta])+
        $vis struct $outer(Box<$inner>);

        #[derive(Debug, thiserror::Error)]
        enum $inner { $(
            $(#[$field_meta])+
            $field $(( $(
                $(#[$ty_meta])* $field_type,
            )+ ))?,
        )+ }

        const _: () = {
            impl std::fmt::Debug for $outer {
                #[inline]
                fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                    std::fmt::Debug::fmt(&*self.0, f)
                }
            }

            impl std::fmt::Display for $outer {
                #[inline]
                fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
                    std::fmt::Display::fmt(&*self.0, f)
                }
            }

            impl From<$inner> for $outer {
                #[inline]
                fn from(value: $inner) -> Self {
                    Self(Box::new(value))
                }
            }

            impl std::error::Error for $outer {
                #[inline]
                fn source(&self) -> Option<&(dyn std::error::Error + 'static)> {
                    self.0.source()
                }
            }
        };
    };
}

pub(crate) use Error;
```

## File: `api/src/sign_unsign_zip.rs`
```rust
use std::io::{BufReader, BufWriter, Read, Seek, Write};

use zip::result::ZipError;
use zip::{ZipArchive, ZipWriter};

#[derive(Debug, thiserror::Error)]
pub(crate) enum CopyZipError {
    #[error("could not read input ZIP")]
    InputZip(#[source] ZipError),
    #[error("could not read file #{1} inside input ZIP")]
    InputZipIndex(#[source] ZipError, usize),
    #[error("could not write to output")]
    OutputWrite(#[source] std::io::Error),
    #[error("could not write ZIP file #{1} to output")]
    OutputZip(#[source] ZipError, usize),
    #[error("could not finish writing output ZIP")]
    OutputZipFinish(#[source] ZipError),
}

pub(crate) fn copy_zip<I, O>(input: &mut I, output: &mut O) -> Result<(), CopyZipError>
where
    I: ?Sized + Seek + Read,
    O: ?Sized + Seek + Write,
{
    let mut input = ZipArchive::new(BufReader::new(input)).map_err(CopyZipError::InputZip)?;
    let mut output = ZipWriter::new(BufWriter::new(output));

    output.set_raw_comment(input.comment().into());
    for idx in 0..input.len() {
        let file = input
            .by_index_raw(idx)
            .map_err(|err| CopyZipError::InputZipIndex(err, idx))?;
        output
            .raw_copy_file(file)
            .map_err(|err| CopyZipError::OutputZip(err, idx))?;
    }
    output
        .finish()
        .map_err(CopyZipError::OutputZipFinish)?
        .flush()
        .map_err(CopyZipError::OutputWrite)?;

    Ok(())
}
```

## File: `api/src/verify_unsign_tar.rs`
```rust
use std::io::{Read, Seek, SeekFrom};
use std::mem::size_of;

use base64::Engine;
use base64::prelude::BASE64_STANDARD;
use ed25519_dalek::{SIGNATURE_LENGTH, Signature, SignatureError};

use crate::constants::{
    BUF_LIMIT, GZIP_END, GZIP_START, HEADER_SIZE, MAGIC_HEADER, SignatureCountLeInt,
};

#[derive(Debug, thiserror::Error)]
pub(crate) enum TarFindDataStartAndLenError {
    #[error("the expected last GZIP block was missing or corrupted")]
    Gzip,
    #[error("could not read input")]
    Read(#[source] std::io::Error),
    #[error("could not seek inside the input")]
    Seek(#[source] std::io::Error),
    #[error("too many signatures in input")]
    TooManySignatures,
}

pub(crate) fn tar_find_data_start_and_len<I>(
    input: &mut I,
) -> Result<(u64, usize), TarFindDataStartAndLenError>
where
    I: ?Sized + Read + Seek,
{
    let mut tail = [0; u64::BITS as usize / 4 + GZIP_END.len()];
    let data_end = input
        .seek(SeekFrom::End(-(tail.len() as i64)))
        .map_err(TarFindDataStartAndLenError::Seek)?;

    input
        .read_exact(&mut tail)
        .map_err(TarFindDataStartAndLenError::Read)?;
    if tail[u64::BITS as usize / 4..] != *GZIP_END {
        return Err(TarFindDataStartAndLenError::Gzip);
    }
    let Ok(gzip_start) = std::str::from_utf8(&tail[..16]) else {
        return Err(TarFindDataStartAndLenError::Gzip);
    };
    let Ok(gzip_start) = u64::from_str_radix(gzip_start, 16) else {
        return Err(TarFindDataStartAndLenError::Gzip);
    };
    let Some(data_start) = gzip_start.checked_add(10) else {
        return Err(TarFindDataStartAndLenError::Gzip);
    };
    let Some(data_len) = data_end.checked_sub(data_start) else {
        return Err(TarFindDataStartAndLenError::Gzip);
    };
    let Ok(data_len) = usize::try_from(data_len) else {
        return Err(TarFindDataStartAndLenError::Gzip);
    };
    if data_len > BUF_LIMIT {
        return Err(TarFindDataStartAndLenError::TooManySignatures);
    }

    Ok((gzip_start, data_len + GZIP_START.len()))
}

#[derive(Debug, thiserror::Error)]
pub(crate) enum TarReadSignaturesError {
    #[error("the input contained invalid base64 encoded data")]
    Base64,
    #[error("the input contained no signatures")]
    Empty,
    #[error("the expected last GZIP block was missing or corrupted")]
    Gzip,
    #[error("the encoded length did not fit the expected length")]
    LengthMismatch,
    #[error("the expected magic header was missing or corrupted")]
    MagicHeader,
    #[error("could not read input")]
    Read(#[source] std::io::Error),
    #[error("the input contained an illegal signature at index #{1}")]
    Signature(#[source] SignatureError, usize),
}

pub(crate) fn tar_read_signatures<I>(
    data_start: u64,
    data_len: usize,
    input: &mut I,
) -> Result<Vec<Signature>, TarReadSignaturesError>
where
    I: ?Sized + Read + Seek,
{
    let _: u64 = input
        .seek(SeekFrom::Start(data_start))
        .map_err(TarReadSignaturesError::Read)?;

    let mut data = vec![0; data_len];
    input
        .read_exact(&mut data)
        .map_err(TarReadSignaturesError::Read)?;

    if data[..GZIP_START.len()] != *GZIP_START {
        return Err(TarReadSignaturesError::Gzip);
    }
    // `base64` already ensures that no `NUL` was contained in the input. A `NUL` would mean that
    // the signature data was broken / contained inside another `DEFLATE` block. I don't think
    // forging a `.tar.gz` file this way could be used for an attack, anyway, because an empty
    // `DEFLATE` block cannot contain data. Being "empty" and "containing data" at the same time …
    // But without any `NUL` check, `zipsign-api` could possibly say "this file is fine", when it's
    // actually broken.
    let Ok(data) = BASE64_STANDARD.decode(&data[GZIP_START.len()..]) else {
        return Err(TarReadSignaturesError::Base64);
    };
    if data.len() < HEADER_SIZE {
        return Err(TarReadSignaturesError::MagicHeader);
    }
    if data[..MAGIC_HEADER.len()] != *MAGIC_HEADER {
        return Err(TarReadSignaturesError::MagicHeader);
    }

    let signature_count = data[MAGIC_HEADER.len()..][..size_of::<SignatureCountLeInt>()]
        .try_into()
        .unwrap();
    let signature_count = SignatureCountLeInt::from_le_bytes(signature_count) as usize;
    if signature_count == 0 {
        return Err(TarReadSignaturesError::Empty);
    }
    if data.len() != HEADER_SIZE + signature_count * SIGNATURE_LENGTH {
        return Err(TarReadSignaturesError::LengthMismatch);
    }

    let signatures = data[HEADER_SIZE..]
        .chunks_exact(SIGNATURE_LENGTH)
        .enumerate()
        .map(|(idx, bytes)| {
            Signature::from_slice(bytes).map_err(|err| TarReadSignaturesError::Signature(err, idx))
        })
        .collect::<Result<Vec<_>, _>>()?;
    Ok(signatures)
}
```

## File: `api/src/sign/mod.rs`
```rust
//! Functions to sign a file

#[cfg(feature = "sign-tar")]
mod tar;
#[cfg(feature = "sign-zip")]
mod zip;

use std::io::Read;

#[cfg(feature = "sign-tar")]
pub use self::tar::{SignTarError, copy_and_sign_tar};
#[cfg(feature = "sign-zip")]
pub use self::zip::{SignZipError, copy_and_sign_zip};
use crate::constants::{BUF_LIMIT, HEADER_SIZE, MAGIC_HEADER, SignatureCountLeInt};
use crate::{KEYPAIR_LENGTH, Prehash, SIGNATURE_LENGTH, SignatureError, SigningKey};

crate::Error! {
    /// An error returned by [`read_signing_keys()`]
    pub struct ReadSigningKeysError(KeysError) {
        #[error("input #{1} did not contain a valid key")]
        Construct(#[source] ed25519_dalek::ed25519::Error, usize),
        #[error("no signing keys provided")]
        Empty,
        #[error("could not read key in file #{1}")]
        Read(#[source] std::io::Error, usize),
    }
}

/// Read signing keys from an [`Iterator`] of [readable][Read] inputs
pub fn read_signing_keys<I, R>(inputs: I) -> Result<Vec<SigningKey>, ReadSigningKeysError>
where
    I: IntoIterator<Item = std::io::Result<R>>,
    R: Read,
{
    // read signing keys
    let mut keys = inputs
        .into_iter()
        .enumerate()
        .map(|(key_index, input)| {
            let mut key = [0; KEYPAIR_LENGTH];
            input
                .and_then(|mut input| input.read_exact(&mut key))
                .map_err(|err| KeysError::Read(err, key_index))?;
            SigningKey::from_keypair_bytes(&key).map_err(|err| KeysError::Construct(err, key_index))
        })
        .collect::<Result<Vec<_>, _>>()?;
    if keys.is_empty() {
        return Err(KeysError::Empty.into());
    }
    keys.sort_by(|l, r| {
        l.verifying_key()
            .as_bytes()
            .cmp(r.verifying_key().as_bytes())
    });
    Ok(keys)
}

crate::Error! {
    /// An error returned by [`gather_signature_data()`]
    pub struct GatherSignatureDataError(SignaturesError) {
        #[error("no signing keys provided")]
        Empty,
        #[error("could not sign data with key #{1}")]
        Signature(#[source] SignatureError, usize),
        #[error("too many signing keys provided")]
        TooManyKeys,
    }
}

/// Sign a pre-hashed message with all provided signing keys, and return a signature block incl.
/// a header
pub fn gather_signature_data(
    keys: &[SigningKey],
    prehashed_message: &Prehash,
    context: Option<&[u8]>,
) -> Result<Vec<u8>, GatherSignatureDataError> {
    if keys.is_empty() {
        return Err(SignaturesError::Empty.into());
    }

    let signature_bytes = keys
        .len()
        .checked_mul(SIGNATURE_LENGTH)
        .and_then(|s| s.checked_add(HEADER_SIZE))
        .ok_or(SignaturesError::TooManyKeys)?;
    if signature_bytes > BUF_LIMIT {
        return Err(SignaturesError::TooManyKeys.into());
    }

    let mut header = [0; HEADER_SIZE];
    header[..MAGIC_HEADER.len()].copy_from_slice(MAGIC_HEADER);
    header[MAGIC_HEADER.len()..]
        .copy_from_slice(&(keys.len() as SignatureCountLeInt).to_le_bytes());

    let mut buf = Vec::with_capacity(signature_bytes);
    buf.extend(header);
    for (idx, key) in keys.iter().enumerate() {
        let signature = key
            .sign_prehashed(prehashed_message.0.clone(), context)
            .map_err(|err| SignaturesError::Signature(err, idx))?;
        buf.extend(signature.to_bytes());
    }
    Ok(buf)
}
```

## File: `api/src/sign/tar.rs`
```rust
#![cfg_attr(docsrs, doc(cfg(feature = "sign-tar")))]

use std::io::{Read, Seek, Write, copy};

use base64::Engine;
use base64::prelude::BASE64_STANDARD;
use ed25519_dalek::SIGNATURE_LENGTH;

use super::{GatherSignatureDataError, gather_signature_data};
use crate::constants::{
    BUF_LIMIT, GZIP_END, GZIP_EXTRA, GZIP_START, HEADER_SIZE, SignatureCountLeInt,
};
use crate::{Prehash, SigningKey};

crate::Error! {
    /// An error returned by [`copy_and_sign_tar()`]
    pub struct SignTarError(Error) {
        #[error("could not copy input to output")]
        Copy(#[source] std::io::Error),
        #[error("could not read input")]
        InputRead(#[source] std::io::Error),
        #[error("could not seek in input")]
        InputSeek(#[source] std::io::Error),
        #[error("could not seek in output")]
        OutputSeek(#[source] std::io::Error),
        #[error("could not write output")]
        OutputWrite(#[source] std::io::Error),
        #[error("could not sign pre-hashed message")]
        Sign(#[source] GatherSignatureDataError),
        #[error("too many keys")]
        TooManyKeys,
    }
}

/// Copy a `.tar.gz` file and sign its content
pub fn copy_and_sign_tar<I, O>(
    input: &mut I,
    output: &mut O,
    keys: &[SigningKey],
    context: Option<&[u8]>,
) -> Result<(), SignTarError>
where
    I: ?Sized + Seek + Read,
    O: ?Sized + Seek + Write,
{
    if keys.len() > SignatureCountLeInt::MAX as usize {
        return Err(Error::TooManyKeys.into());
    }
    let signature_bytes = SIGNATURE_LENGTH * keys.len() + HEADER_SIZE;
    if (signature_bytes.saturating_add(2) / 3).saturating_mul(4) > BUF_LIMIT {
        return Err(Error::TooManyKeys.into());
    }

    // gather signature
    let prehashed_message = Prehash::calculate(input).map_err(Error::InputRead)?;
    let buf = gather_signature_data(keys, &prehashed_message, context).map_err(Error::Sign)?;
    let buf = BASE64_STANDARD.encode(buf);
    if buf.len() > BUF_LIMIT {
        return Err(Error::TooManyKeys.into());
    }

    // copy input
    input.rewind().map_err(Error::InputSeek)?;
    let _: u64 = copy(input, output).map_err(Error::Copy)?;

    // write signature
    let start = output.stream_position().map_err(Error::OutputSeek)?;
    let mut start_buf = [0u8; 16];
    write!(&mut start_buf[..], "{start:016x}").unwrap();

    let mut tail = Vec::with_capacity(GZIP_EXTRA + buf.len());
    tail.extend(GZIP_START);
    tail.extend(buf.into_bytes()); // GZIP comment
    tail.extend(start_buf); // GZIP comment
    tail.extend(GZIP_END);
    output.write_all(&tail).map_err(Error::OutputWrite)?;

    Ok(())
}
```

## File: `api/src/sign/zip.rs`
```rust
#![cfg_attr(docsrs, doc(cfg(feature = "sign-zip")))]

use std::io::{IoSlice, Read, Seek, SeekFrom, Write};

use super::{GatherSignatureDataError, gather_signature_data};
use crate::constants::{BUF_LIMIT, HEADER_SIZE, SignatureCountLeInt};
use crate::sign_unsign_zip::{CopyZipError, copy_zip};
use crate::{Prehash, SIGNATURE_LENGTH, SigningKey};

crate::Error! {
    /// An error returned by [`copy_and_sign_zip()`]
    pub struct SignZipError(Error) {
        #[error("could not copy ZIP data")]
        Copy(#[source] CopyZipError),
        #[error("could not write to output, device full?")]
        OutputFull,
        #[error("could not read output")]
        OutputRead(#[source] std::io::Error),
        #[error("could not seek in output")]
        OutputSeek(#[source] std::io::Error),
        #[error("could not write to output")]
        OutputWrite(#[source] std::io::Error),
        #[error("could not gather signature data")]
        Sign(#[source] GatherSignatureDataError),
        #[error("too many keys")]
        TooManyKeys,
    }
}

/// Copy a `.zip` file and sign its content
pub fn copy_and_sign_zip<I, O>(
    input: &mut I,
    output: &mut O,
    keys: &[SigningKey],
    context: Option<&[u8]>,
) -> Result<(), SignZipError>
where
    I: ?Sized + Read + Seek,
    O: ?Sized + Read + Seek + Write,
{
    if keys.len() > SignatureCountLeInt::MAX as usize {
        return Err(Error::TooManyKeys.into());
    }
    let signature_bytes = keys
        .len()
        .checked_mul(SIGNATURE_LENGTH)
        .and_then(|s| s.checked_add(HEADER_SIZE))
        .ok_or(Error::TooManyKeys)?;
    if signature_bytes > BUF_LIMIT {
        return Err(Error::TooManyKeys.into());
    }

    // copy ZIP
    write_padding(signature_bytes, output)?;
    copy_zip(input, output).map_err(Error::Copy)?;

    // gather signature
    let _ = output
        .seek(SeekFrom::Start(signature_bytes.try_into().unwrap()))
        .map_err(Error::OutputSeek)?;
    let prehashed_message = Prehash::calculate(output).map_err(Error::OutputRead)?;
    let buf = gather_signature_data(keys, &prehashed_message, context).map_err(Error::Sign)?;

    // write signature
    output.rewind().map_err(Error::OutputSeek)?;
    output.write_all(&buf).map_err(Error::OutputWrite)?;
    Ok(())
}

fn write_padding<O>(mut padding_to_write: usize, output: &mut O) -> Result<(), Error>
where
    O: ?Sized + Write,
{
    while padding_to_write > 0 {
        const PADDING: &[u8; 512] = &[0; 512];
        let result = if padding_to_write > PADDING.len() {
            let num_slices = padding_to_write.div_ceil(PADDING.len()).min(128);
            let mut slices = vec![IoSlice::new(PADDING); num_slices];
            slices[num_slices - 1] = IoSlice::new(&PADDING[..padding_to_write % PADDING.len()]);
            output.write_vectored(&slices)
        } else {
            output.write(&PADDING[..padding_to_write])
        };
        let written = result.map_err(Error::OutputWrite)?;

        if written == 0 {
            return Err(Error::OutputFull);
        }
        padding_to_write -= written;
    }
    Ok(())
}
```

## File: `api/src/unsign/mod.rs`
```rust
//! Functions to remove signatures from a file

#[cfg(feature = "unsign-tar")]
mod tar;
#[cfg(feature = "unsign-zip")]
mod zip;

#[cfg(feature = "unsign-tar")]
pub use self::tar::{UnsignTarError, copy_and_unsign_tar};
#[cfg(feature = "unsign-zip")]
pub use self::zip::{UnsignZipError, copy_and_unsign_zip};
```

## File: `api/src/unsign/tar.rs`
```rust
#![cfg_attr(docsrs, doc(cfg(feature = "unsign-tar")))]

use std::io::{Read, Seek, Write, copy};

use crate::verify_unsign_tar::{
    TarFindDataStartAndLenError, TarReadSignaturesError, tar_find_data_start_and_len,
    tar_read_signatures,
};

crate::Error! {
    /// An error returned by [`copy_and_unsign_tar()`]
    pub struct UnsignTarError(Error) {
        #[error("could not copy data")]
        Copy(#[source] std::io::Error),
        #[error("could not find read signatures in .tar.gz file")]
        FindDataStartAndLen(#[source] TarFindDataStartAndLenError),
        #[error("could not find read signatures in .tar.gz file")]
        ReadSignatures(#[source] TarReadSignaturesError),
        #[error("could not seek inside the input")]
        Seek(#[source] std::io::Error),
    }
}

/// Copy a signed `.tar.gz` file without the signatures
pub fn copy_and_unsign_tar<I, O>(input: &mut I, output: &mut O) -> Result<(), UnsignTarError>
where
    I: ?Sized + Seek + Read,
    O: ?Sized + Seek + Write,
{
    // seek to start of base64 encoded signatures
    let (data_start, data_len) =
        tar_find_data_start_and_len(input).map_err(Error::FindDataStartAndLen)?;

    // read base64 encoded signatures
    let _ = tar_read_signatures(data_start, data_len, input).map_err(Error::ReadSignatures)?;

    // copy data
    input.rewind().map_err(Error::Seek)?;
    let _ = copy(&mut input.take(data_start), output).map_err(Error::Copy)?;

    Ok(())
}
```

## File: `api/src/unsign/zip.rs`
```rust
#![cfg_attr(docsrs, doc(cfg(feature = "unsign-zip")))]

use std::io::{Read, Seek, Write};

use crate::sign_unsign_zip::{CopyZipError, copy_zip};

crate::Error! {
    /// An error returned by [`copy_and_unsign_zip()`]
    pub struct UnsignZipError(Error) {
        #[error("could not copy ZIP data")]
        Copy(#[source] CopyZipError),
    }
}

/// Copy a signed `.zip` file without the signatures
pub fn copy_and_unsign_zip<I, O>(input: &mut I, output: &mut O) -> Result<(), UnsignZipError>
where
    I: ?Sized + Read + Seek,
    O: ?Sized + Read + Seek + Write,
{
    copy_zip(input, output).map_err(Error::Copy)?;
    Ok(())
}
```

## File: `api/src/verify/mod.rs`
```rust
//! Functions to verify a signed file

#[cfg(feature = "verify-tar")]
mod tar;
#[cfg(feature = "verify-zip")]
mod zip;

use std::io::Read;

#[cfg(feature = "verify-tar")]
pub use self::tar::{VerifyTarError, verify_tar};
#[cfg(feature = "verify-zip")]
pub use self::zip::{VerifyZipError, verify_zip};
use crate::constants::{BUF_LIMIT, HEADER_SIZE, MAGIC_HEADER, SignatureCountLeInt};
use crate::{
    PUBLIC_KEY_LENGTH, Prehash, SIGNATURE_LENGTH, Signature, SignatureError, VerifyingKey,
};

crate::Error! {
    /// An error returned by [`collect_keys()`]
    pub struct CollectKeysError(KeysError) {
        #[error("the input was empty")]
        Empty,
        #[error("could not read key #{1}")]
        Io(#[source] std::io::Error, usize),
        #[error("input contained an illegal key at #{1}")]
        Signature(#[source] SignatureError, usize),
    }
}

/// Convert a slice of key bytes into a [`Vec`] of [`VerifyingKey`]s.
pub fn collect_keys<K>(keys: K) -> Result<Vec<VerifyingKey>, CollectKeysError>
where
    K: IntoIterator<Item = std::io::Result<[u8; PUBLIC_KEY_LENGTH]>>,
{
    let keys = keys
        .into_iter()
        .enumerate()
        .map(|(idx, key)| {
            let key = key.map_err(|err| KeysError::Io(err, idx))?;
            VerifyingKey::from_bytes(&key).map_err(|err| KeysError::Signature(err, idx))
        })
        .collect::<Result<Vec<_>, _>>()?;
    if keys.is_empty() {
        return Err(KeysError::Empty.into());
    }
    Ok(keys)
}

/// No matching key/signature pair found
#[derive(Debug, Clone, Copy, thiserror::Error)]
#[error("no matching key/signature pair found")]
pub struct NoMatch;

/// Iterate signatures and keys, and return the indices of the first match
/// match
pub fn find_match(
    keys: &[VerifyingKey],
    signatures: &[Signature],
    prehashed_message: &Prehash,
    context: Option<&[u8]>,
) -> Result<(usize, usize), NoMatch> {
    for (key_idx, key) in keys.iter().enumerate() {
        for (sig_idx, signature) in signatures.iter().enumerate() {
            let is_ok = key
                .verify_prehashed_strict(prehashed_message.0.clone(), context, signature)
                .is_ok();
            if is_ok {
                return Ok((key_idx, sig_idx));
            }
        }
    }
    Err(NoMatch)
}

crate::Error! {
    /// An error returned by [`read_signatures()`]
    pub struct ReadSignaturesError(SignaturesError) {
        #[error("the input contained no signatures")]
        Empty,
        #[error("could not read signatures")]
        Read(#[source] std::io::Error),
        #[error("the expected magic header was missing or corrupted")]
        MagicHeader,
        #[error("input contained an illegal signature at #{1}")]
        Signature(#[source] SignatureError, usize),
    }
}

/// Collect all signatures in a file
pub fn read_signatures<I>(input: &mut I) -> Result<Vec<Signature>, ReadSignaturesError>
where
    I: ?Sized + Read,
{
    let mut header = [0; HEADER_SIZE];
    input
        .read_exact(&mut header)
        .map_err(SignaturesError::Read)?;
    if header[..MAGIC_HEADER.len()] != *MAGIC_HEADER {
        return Err(SignaturesError::MagicHeader.into());
    }

    let signature_count = header[MAGIC_HEADER.len()..].try_into().unwrap();
    let signature_count = SignatureCountLeInt::from_le_bytes(signature_count) as usize;
    if signature_count == 0 {
        return Err(SignaturesError::Empty.into());
    }
    let signature_bytes = signature_count
        .checked_mul(SIGNATURE_LENGTH)
        .ok_or(SignaturesError::MagicHeader)?;
    if signature_bytes > BUF_LIMIT {
        return Err(SignaturesError::MagicHeader.into());
    }

    let mut signatures = vec![0; signature_bytes];
    input
        .read_exact(&mut signatures)
        .map_err(SignaturesError::Read)?;

    let signatures = signatures
        .chunks_exact(SIGNATURE_LENGTH)
        .enumerate()
        .map(|(idx, bytes)| {
            Signature::from_slice(bytes).map_err(|err| SignaturesError::Signature(err, idx))
        })
        .collect::<Result<Vec<_>, _>>()?;

    Ok(signatures)
}
```

## File: `api/src/verify/tar.rs`
```rust
#![cfg_attr(docsrs, doc(cfg(feature = "verify-tar")))]

use std::io::{Read, Seek};

use super::{NoMatch, find_match};
use crate::verify_unsign_tar::{
    TarFindDataStartAndLenError, TarReadSignaturesError, tar_find_data_start_and_len,
    tar_read_signatures,
};
use crate::{Prehash, VerifyingKey};

crate::Error! {
    /// An error returned by [`verify_tar()`]
    pub struct VerifyTarError(Error) {
        #[error("could not find read signatures in .tar.gz file")]
        FindDataStartAndLen(#[source] TarFindDataStartAndLenError),
        #[error("no matching key/signature pair found")]
        NoMatch(NoMatch),
        #[error("could not read input")]
        Read(#[source] std::io::Error),
        #[error("could not find read signatures in .tar.gz file")]
        ReadSignatures(#[source] TarReadSignaturesError),
        #[error("could not seek inside the input")]
        Seek(#[source] std::io::Error),
    }
}

/// Find the index of the first [`VerifyingKey`] that matches the a signature in a signed `.tar.gz`
/// file
pub fn verify_tar<I>(
    input: &mut I,
    keys: &[VerifyingKey],
    context: Option<&[u8]>,
) -> Result<usize, VerifyTarError>
where
    I: ?Sized + Read + Seek,
{
    // seek to start of base64 encoded signatures
    let (data_start, data_len) =
        tar_find_data_start_and_len(input).map_err(Error::FindDataStartAndLen)?;

    // read base64 encoded signatures
    let signatures =
        tar_read_signatures(data_start, data_len, input).map_err(Error::ReadSignatures)?;

    // pre-hash file
    input.rewind().map_err(Error::Seek)?;
    let prehashed_message = Prehash::calculate(&mut input.take(data_start)).map_err(Error::Read)?;

    // find match
    let (key_idx, _) =
        find_match(keys, &signatures, &prehashed_message, context).map_err(Error::NoMatch)?;
    Ok(key_idx)
}
```

## File: `api/src/verify/zip.rs`
```rust
#![cfg_attr(docsrs, doc(cfg(feature = "verify-zip")))]

use std::io::{Read, Seek};

use super::{NoMatch, ReadSignaturesError, VerifyingKey, find_match, read_signatures};
use crate::{Prehash, Signature};

crate::Error! {
    /// An error returned by [`verify_zip()`]
    pub struct VerifyZipError(Error) {
        #[error("could not read input")]
        InputRead(#[source] std::io::Error),
        #[error("no matching key/signature pair found")]
        NoMatch(NoMatch),
        #[error("could not read signatures from input")]
        ReadSignaturesError(#[source] ReadSignaturesError),
    }
}

/// Find the index of the first [`VerifyingKey`] that matches the a signature in a signed `.zip`
/// file
pub fn verify_zip<R>(
    signed_file: &mut R,
    keys: &[VerifyingKey],
    context: Option<&[u8]>,
) -> Result<usize, VerifyZipError>
where
    R: ?Sized + Read + Seek,
{
    let (prehashed_message, signatures) = read_zip(signed_file)?;
    let (key_idx, _) =
        find_match(keys, &signatures, &prehashed_message, context).map_err(Error::NoMatch)?;
    Ok(key_idx)
}

fn read_zip<R>(signed_file: &mut R) -> Result<(Prehash, Vec<Signature>), VerifyZipError>
where
    R: ?Sized + Read + Seek,
{
    let signatures = read_signatures(signed_file).map_err(Error::ReadSignaturesError)?;
    let prehashed_message = Prehash::calculate(signed_file).map_err(Error::InputRead)?;
    Ok((prehashed_message, signatures))
}
```

## File: `cli/Cargo.toml`
```
[package]
name = "zipsign"
description = "Sign and verify `.zip` and `.tar.gz` files with an ed25519 signing key"
version = "0.2.1"
edition = "2024"
authors = ["René Kijewski <crates.io@k6i.de>"]
repository = "https://github.com/Kijewski/zipsign"
license = "MIT OR Apache-2.0 OR Apache-2.0 WITH LLVM-exception"
rust-version = "1.85"

[package.metadata.docs.rs]
all-features = true
rustdoc-args = ["--generate-link-to-definition", "--cfg=docsrs"]

[dependencies]
clap.workspace = true
ed25519-dalek.workspace = true
getrandom.workspace = true
normalize-path.workspace = true
pretty-error-debug.workspace = true
tempfile.workspace = true
thiserror.workspace = true
zipsign-api.workspace = true
```

## File: `cli/LICENSE-APACHE`
```
../LICENSE-APACHE
```

## File: `cli/LICENSE-MIT`
```
../LICENSE-MIT
```

## File: `cli/README.md`
```markdown
../README.md
```

## File: `cli/_typos.toml`
```
../_typos.toml
```

## File: `cli/clippy.toml`
```
msrv = "1.85.0"
```

## File: `cli/rustfmt.toml`
```
../rustfmt.toml
```

## File: `cli/tomlfmt.toml`
```
../tomlfmt.toml
```

## File: `cli/src/generate.rs`
```rust
use std::fs::OpenOptions;
use std::io::{Read, Write};
#[cfg(unix)]
use std::os::unix::prelude::OpenOptionsExt;
use std::path::PathBuf;

use clap::Parser;
use ed25519_dalek::{KEYPAIR_LENGTH, SecretKey, SigningKey};

/// Generate a signing key
#[derive(Debug, Parser, Clone)]
pub(crate) struct Cli {
    /// Private key file to create
    private_key: PathBuf,
    /// Verifying key (public key) file to create
    verifying_key: PathBuf,
    /// Don't create new key pair, but extract public key from private key
    #[arg(long, short = 'e')]
    extract: bool,
    /// Overwrite output files if they exists
    #[arg(long, short = 'f')]
    force: bool,
}

#[derive(Debug, thiserror::Error)]
pub(crate) enum Error {
    #[error("could not open {1:?} for writing")]
    OpenWrite(#[source] std::io::Error, PathBuf),
    #[error("could not open {1:?} for reading")]
    OpenRead(#[source] std::io::Error, PathBuf),
    #[error("could not write to {1:?}")]
    Write(#[source] std::io::Error, PathBuf),
    #[error("could not read from {1:?}")]
    Read(#[source] std::io::Error, PathBuf),
    #[error("no valid key found in from {1:?}")]
    IllegalKey(#[source] ed25519_dalek::SignatureError, PathBuf),
    #[error("could not get random data")]
    Random(#[source] getrandom::Error),
}

pub(crate) fn main(args: Cli) -> Result<(), Error> {
    let key = if args.extract {
        let result = OpenOptions::new().read(true).open(&args.private_key);
        let mut f = match result {
            Ok(f) => f,
            Err(err) => return Err(Error::OpenRead(err, args.private_key)),
        };
        let mut key = [0; KEYPAIR_LENGTH];
        if let Err(err) = f.read_exact(&mut key) {
            return Err(Error::Read(err, args.private_key));
        }
        match SigningKey::from_keypair_bytes(&key) {
            Ok(key) => key,
            Err(err) => return Err(Error::IllegalKey(err, args.private_key)),
        }
    } else {
        let mut secret = SecretKey::default();
        getrandom::fill(secret.as_mut_slice()).map_err(Error::Random)?;
        let key = SigningKey::from_bytes(&{ secret });

        let result = OpenOptions::new()
            .write(true)
            .create(true)
            .create_new(!args.force)
            .truncate(true)
            .mode(0o600)
            .open(&args.private_key);
        let mut f = match result {
            Ok(f) => f,
            Err(err) => return Err(Error::OpenWrite(err, args.private_key)),
        };
        f.write_all(&key.to_keypair_bytes())
            .map_err(|err| Error::Write(err, args.private_key))?;
        key
    };

    let result = OpenOptions::new()
        .write(true)
        .create(true)
        .create_new(!args.force)
        .truncate(true)
        .open(&args.verifying_key);
    let mut f = match result {
        Ok(f) => f,
        Err(err) => return Err(Error::OpenWrite(err, args.verifying_key)),
    };
    f.write_all(key.verifying_key().as_bytes())
        .map_err(|err| Error::Write(err, args.verifying_key))
}

#[allow(dead_code)]
trait NotUnixOpenOptionsExt {
    #[inline(always)]
    fn mode(&mut self, _mode: u32) -> &mut Self {
        self
    }
}

#[cfg(not(unix))]
impl NotUnixOpenOptionsExt for OpenOptions {}
```

## File: `cli/src/main.rs`
```rust
#![cfg_attr(docsrs, feature(doc_cfg))]
#![forbid(unsafe_code)]
#![allow(unknown_lints)]
#![doc = include_str!("../README.md")]

mod generate;
mod sign;
mod unsign;
mod verify;

use std::path::Path;

use clap::{Parser, Subcommand};

/// Sign a file with an ed25519 signing key.
#[derive(Debug, Parser)]
#[command(author, version, about, long_about = None)]
#[command(propagate_version = true)]
struct Cli {
    #[command(subcommand)]
    subcommand: CliSubcommand,
}

#[derive(Debug, Subcommand, Clone)]
enum CliSubcommand {
    GenKey(generate::Cli),
    Verify(verify::Cli),
    Sign(sign::Cli),
    Unsign(unsign::Cli),
}

#[derive(pretty_error_debug::Debug, thiserror::Error)]
enum MainError {
    #[error("could not generate key")]
    GenKey(#[from] generate::Error),
    #[error("could not verify file")]
    Verify(#[from] verify::Error),
    #[error("could not sign file")]
    Sign(#[from] sign::Error),
    #[error("could not remove sign from file")]
    Unsign(#[from] unsign::Error),
}

fn main() -> Result<(), MainError> {
    let args = Cli::parse();
    match args.subcommand {
        CliSubcommand::GenKey(args) => generate::main(args)?,
        CliSubcommand::Verify(args) => verify::main(args)?,
        CliSubcommand::Sign(args) => sign::main(args)?,
        CliSubcommand::Unsign(args) => unsign::main(args)?,
    }
    Ok(())
}

#[derive(Debug, Clone, Copy, thiserror::Error)]
enum ImplicitContextError {
    #[error("could not determine basename")]
    Basename,
    #[error("path could not be interpreted as UTF-8 string")]
    Utf8,
}

fn get_context<'a>(
    explicit: Option<&'a str>,
    implicit: &'a Path,
) -> Result<&'a [u8], ImplicitContextError> {
    if let Some(context) = explicit {
        Ok(context.as_bytes())
    } else {
        // This function does not use `std::os::unix::prelude::OsStrExt` so that the windows and
        // linux implementation work the same for non-ASCII filenames. Otherwise a file signed on
        // linux might not successfully verify on windows, and vice versa.
        implicit
            .file_name()
            .ok_or(ImplicitContextError::Basename)?
            .to_str()
            .ok_or(ImplicitContextError::Utf8)
            .map(str::as_bytes)
    }
}
```

## File: `cli/src/sign.rs`
```rust
use std::fs::{File, rename};
use std::io::Write;
use std::path::{Path, PathBuf};

use clap::{Args, Parser, Subcommand};
use normalize_path::NormalizePath;
use zipsign_api::Prehash;
use zipsign_api::sign::{
    GatherSignatureDataError, ReadSigningKeysError, SignTarError, SignZipError, copy_and_sign_tar,
    copy_and_sign_zip, gather_signature_data, read_signing_keys,
};

use crate::{ImplicitContextError, get_context};

/// Generate signature for a file
#[derive(Debug, Parser, Clone)]
pub(crate) struct Cli {
    #[command(subcommand)]
    subcommand: CliKind,
}

impl CliKind {
    fn split(self) -> (ArchiveKind, CommonArgs) {
        match self {
            CliKind::Separate(common) => (ArchiveKind::Separate, common),
            CliKind::Zip(common) => (ArchiveKind::Zip, common),
            CliKind::Tar(common) => (ArchiveKind::Tar, common),
        }
    }
}

#[derive(Debug, Subcommand, Clone)]
enum CliKind {
    /// Store generated signature in a separate file
    Separate(#[command(flatten)] CommonArgs),
    /// `<INPUT>` is a .zip file.
    /// Its data is copied and the signatures are stored next to the data.
    Zip(#[command(flatten)] CommonArgs),
    /// `<INPUT>` is a gzipped .tar file.
    /// Its data is copied and the signatures are stored next to the data.
    Tar(#[command(flatten)] CommonArgs),
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum ArchiveKind {
    Separate,
    Zip,
    Tar,
}

#[derive(Debug, Args, Clone)]
struct CommonArgs {
    /// Input file to sign
    input: PathBuf,
    /// Signed file to generate (if omitted, the input is overwritten)
    #[arg(long, short = 'o')]
    output: Option<PathBuf>,
    /// One or more files containing private keys
    #[arg(required = true)]
    keys: Vec<PathBuf>,
    /// Arbitrary string used to salt the input, defaults to file name of `<INPUT>`
    #[arg(long, short = 'c')]
    context: Option<String>,
    /// Overwrite output file if it exists
    #[arg(long, short = 'f')]
    force: bool,
}

#[derive(Debug, thiserror::Error)]
pub(crate) enum Error {
    #[error("could not determine `context` string by the input name")]
    Context(#[from] ImplicitContextError),
    #[error("output exists, use `--force` allow replacing a file")]
    Exists,
    #[error("could not gather signature data")]
    GatherSignatureData(#[from] GatherSignatureDataError),
    #[error("could not open input file")]
    InputOpen(#[source] std::io::Error),
    #[error("could not read input")]
    InputRead(#[source] std::io::Error),
    #[error("could not rename output file")]
    OutputRename(#[source] std::io::Error),
    #[error("could not write to output")]
    OutputWrite(#[source] std::io::Error),
    #[error("could not read signing keys")]
    ReadSigningKeys(#[from] ReadSigningKeysError),
    #[error("could not copy and sign the input")]
    Tar(#[from] SignTarError),
    #[error("could not create temporary file in output directory")]
    Tempfile(#[source] std::io::Error),
    #[error("could not copy and sign the input")]
    Zip(#[from] SignZipError),
}

pub(crate) fn main(args: Cli) -> Result<(), Error> {
    let (kind, args) = args.subcommand.split();

    let context = get_context(args.context.as_deref(), &args.input)?;

    let keys = args.keys.into_iter().map(File::open);
    let keys = read_signing_keys(keys)?;

    let output_path = args.output.as_deref().unwrap_or(&args.input).normalize();
    if args.output.is_some() && !args.force {
        return Err(Error::Exists);
    }
    let output_dir = output_path.parent().unwrap_or(Path::new("."));
    let tempdir = tempfile::Builder::new()
        .prefix(".zipsign.")
        .suffix(".tmp")
        .tempdir_in(output_dir)
        .map_err(Error::Tempfile)?;
    let mut temp_file = tempfile::Builder::new()
        .tempfile_in(&tempdir)
        .map_err(Error::Tempfile)?;
    let output_file = temp_file.as_file_mut();

    let mut input = File::open(&args.input).map_err(Error::InputOpen)?;
    match kind {
        ArchiveKind::Separate => {
            let prehashed_message = Prehash::calculate(&mut input).map_err(Error::InputRead)?;
            let data = gather_signature_data(&keys, &prehashed_message, Some(context))?;
            output_file.write_all(&data).map_err(Error::OutputWrite)?;
        },
        ArchiveKind::Zip => copy_and_sign_zip(&mut input, output_file, &keys, Some(context))?,
        ArchiveKind::Tar => {
            copy_and_sign_tar(&mut input, output_file, &keys, Some(context))?;
        },
    }
    // drop input so it can be overwritten if input=output
    drop(input);

    rename(temp_file.into_temp_path(), output_path).map_err(Error::OutputRename)?;
    Ok(())
}
```

## File: `cli/src/unsign.rs`
```rust
use std::fs::{File, rename};
use std::path::{Path, PathBuf};

use clap::{Args, Parser, Subcommand};
use normalize_path::NormalizePath;
use zipsign_api::unsign::{
    UnsignTarError, UnsignZipError, copy_and_unsign_tar, copy_and_unsign_zip,
};

/// Generate signature for a file
#[derive(Debug, Parser, Clone)]
pub(crate) struct Cli {
    #[command(subcommand)]
    subcommand: CliKind,
}

impl CliKind {
    fn split(self) -> (ArchiveKind, CommonArgs) {
        match self {
            CliKind::Zip(common) => (ArchiveKind::Zip, common),
            CliKind::Tar(common) => (ArchiveKind::Tar, common),
        }
    }
}

#[derive(Debug, Subcommand, Clone)]
enum CliKind {
    /// `<INPUT>` is a .zip file.
    /// Its data is copied and the signatures are stored next to the data.
    Zip(#[command(flatten)] CommonArgs),
    /// `<INPUT>` is a gzipped .tar file.
    /// Its data is copied and the signatures are stored next to the data.
    Tar(#[command(flatten)] CommonArgs),
}

#[derive(Debug, Clone, Copy, PartialEq, Eq)]
enum ArchiveKind {
    Zip,
    Tar,
}

#[derive(Debug, Args, Clone)]
struct CommonArgs {
    /// Input file to sign
    input: PathBuf,
    /// Signed file to generate (if omitted, the input is overwritten)
    #[arg(long, short = 'o')]
    output: Option<PathBuf>,
    /// Overwrite output file if it exists
    #[arg(long, short = 'f')]
    force: bool,
}

#[derive(Debug, thiserror::Error)]
pub(crate) enum Error {
    #[error("output exists, use `--force` allow replacing a file")]
    Exists,
    #[error("could not open input file")]
    InputOpen(#[source] std::io::Error),
    #[error("could not rename output file")]
    OutputRename(#[source] std::io::Error),
    #[error(transparent)]
    Tar(#[from] UnsignTarError),
    #[error("could not create temporary file in output directory")]
    Tempfile(#[source] std::io::Error),
    #[error(transparent)]
    Zip(#[from] UnsignZipError),
}

pub(crate) fn main(args: Cli) -> Result<(), Error> {
    let (kind, args) = args.subcommand.split();

    let output_path = args.output.as_deref().unwrap_or(&args.input).normalize();
    if args.output.is_some() && !args.force {
        return Err(Error::Exists);
    }
    let output_dir = output_path.parent().unwrap_or(Path::new("."));
    let tempdir = tempfile::Builder::new()
        .prefix(".zipsign.")
        .suffix(".tmp")
        .tempdir_in(output_dir)
        .map_err(Error::Tempfile)?;
    let mut temp_file = tempfile::Builder::new()
        .tempfile_in(&tempdir)
        .map_err(Error::Tempfile)?;
    let output_file = temp_file.as_file_mut();

    let mut input = File::open(&args.input).map_err(Error::InputOpen)?;
    match kind {
        ArchiveKind::Zip => copy_and_unsign_zip(&mut input, output_file)?,
        ArchiveKind::Tar => copy_and_unsign_tar(&mut input, output_file)?,
    }
    // drop input so it can be overwritten if input=output
    drop(input);

    rename(temp_file.into_temp_path(), output_path).map_err(Error::OutputRename)?;
    Ok(())
}
```

## File: `cli/src/verify.rs`
```rust
use std::fs::File;
use std::io::Read;
use std::path::PathBuf;

use clap::{Args, Parser, Subcommand};
use zipsign_api::verify::{
    CollectKeysError, NoMatch, ReadSignaturesError, VerifyTarError, VerifyZipError, collect_keys,
    find_match, read_signatures, verify_tar, verify_zip,
};
use zipsign_api::{PUBLIC_KEY_LENGTH, Prehash};

use crate::{ImplicitContextError, get_context};

/// Verify a signature
#[derive(Debug, Parser, Clone)]
pub(crate) struct Cli {
    #[command(subcommand)]
    subcommand: CliKind,
}

impl CliKind {
    fn split(self) -> (ArchiveKind, PathBuf, CommonArgs) {
        match self {
            CliKind::Separate {
                common,
                input,
                signature,
            } => (ArchiveKind::Separate { signature }, input, common),
            CliKind::Zip { common, input } => (ArchiveKind::Zip, input, common),
            CliKind::Tar { common, input } => (ArchiveKind::Tar, input, common),
        }
    }
}

#[derive(Debug, Subcommand, Clone)]
enum CliKind {
    /// Store generated signature in a separate file
    Separate {
        /// File to verify
        input: PathBuf,
        /// Signature file
        signature: PathBuf,
        #[command(flatten)]
        common: CommonArgs,
    },
    /// `<INPUT>` is a .zip file.
    /// Its data is copied and the signatures are stored next to the data.
    Zip {
        /// Signed .zip file
        input: PathBuf,
        #[command(flatten)]
        common: CommonArgs,
    },
    /// `<INPUT>` is an uncompressed or gzipped .tar file.
    /// Its data is copied and the signatures are stored next to the data.
    Tar {
        /// Signed .tar file
        input: PathBuf,
        #[command(flatten)]
        common: CommonArgs,
    },
}

#[derive(Debug, Clone, PartialEq, Eq)]
enum ArchiveKind {
    Separate { signature: PathBuf },
    Zip,
    Tar,
}

#[derive(Debug, Args, Clone)]
struct CommonArgs {
    /// One or more files containing verifying keys
    #[arg(required = true)]
    keys: Vec<PathBuf>,
    /// An arbitrary string used to salt the input, defaults to file name of `<INPUT>`
    #[arg(long, short = 'c')]
    context: Option<String>,
    /// Don't write "OK" if the verification succeeded
    #[arg(long, short = 'q')]
    quiet: bool,
}

#[derive(Debug, thiserror::Error)]
pub(crate) enum Error {
    #[error("could not collect keys")]
    CollectKeys(#[from] CollectKeysError),
    #[error("could not determine `context` string by the input name")]
    Context(#[from] ImplicitContextError),
    #[error("could not open input")]
    InputOpen(#[source] std::io::Error),
    #[error("could not read input")]
    InputRead(#[source] std::io::Error),
    #[error(transparent)]
    NoMatch(#[from] NoMatch),
    #[error("could not open signatures")]
    SignaturesOpen(#[source] std::io::Error),
    #[error("could not read signatures")]
    SignaturesRead(#[from] ReadSignaturesError),
    #[error("could not verify `.tar.gz` file")]
    Tar(#[from] VerifyTarError),
    #[error("could not verify `.zip` file")]
    Zip(#[from] VerifyZipError),
}

pub(crate) fn main(args: Cli) -> Result<(), Error> {
    let (kind, input, args) = args.subcommand.split();

    let context = get_context(args.context.as_deref(), &input)?;

    let keys = args.keys.into_iter().map(|path| {
        let mut buf = [0; PUBLIC_KEY_LENGTH];
        File::open(path)?.read_exact(&mut buf)?;
        Ok(buf)
    });
    let keys = collect_keys(keys)?;

    let mut input = File::open(&input).map_err(Error::InputOpen)?;

    let _idx = match kind {
        ArchiveKind::Separate { signature } => {
            let signatures =
                read_signatures(&mut File::open(signature).map_err(Error::SignaturesOpen)?)?;
            let prehashed_message = Prehash::calculate(&mut input).map_err(Error::InputRead)?;
            let (key_idx, _) = find_match(&keys, &signatures, &prehashed_message, Some(context))
                .map_err(Error::NoMatch)?;
            key_idx
        },
        ArchiveKind::Zip => verify_zip(&mut input, &keys, Some(context))?,
        ArchiveKind::Tar => verify_tar(&mut input, &keys, Some(context))?,
    };
    if !args.quiet {
        println!("OK")
    }
    Ok(())
}
```

