---
id: zipsign
type: knowledge
owner: OA_Triage
---
# zipsign
Raw knowledge dump assimilated by OA.

## SWALLOW ENGINE DISTILLATION

### File: README.md
```md
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

### File: api\README.md
```md
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

### File: cli\README.md
```md
../README.md
```

### File: api\src\constants.rs
```rs
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

### File: api\src\lib.rs
```rs
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

### File: api\src\sign_unsign_zip.rs
```rs
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

### File: api\src\verify_unsign_tar.rs
```rs
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

### File: cli\src\generate.rs
```rs
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

### File: cli\src\main.rs
```rs
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

### File: cli\src\sign.rs
```rs
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

### File: cli\src\unsign.rs
```rs
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

### File: cli\src\verify.rs
```rs
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

